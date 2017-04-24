#include "global.h"
//----------------------------------------------------------------------------------------------
#include "storage/storage_factory.h"
//----------------------------------------------------------------------------------------------
AGlobal* g_global = NULL;
//----------------------------------------------------------------------------------------------

AGlobal* AGlobal::getInstance ()
{
	if (g_global != NULL)
		return g_global;

	return new AGlobal();
}
//----------------------------------------------------------------------------------------------

AGlobal::AGlobal ()
{
	g_global = this;

	// предпочитаемый список шифров
	static const char* AVALON_CIPHERS[] =
	{
		"ECDHE-RSA-AES128-SHA",     // SSLv3 Kx=ECDH Au=RSA   Enc=AES(128) Mac=SHA1
		"ECDHE-ECDSA-AES128-SHA",   // SSLv3 Kx=ECDH Au=ECDSA Enc=AES(128) Mac=SHA1
		"ECDHE-RSA-AES256-SHA",     // SSLv3 Kx=ECDH Au=RSA   Enc=AES(256) Mac=SHA1
		"ECDHE-ECDSA-AES256-SHA",   // SSLv3 Kx=ECDH Au=ECDSA Enc=AES(256) Mac=SHA1
		"AES128-SHA",               // SSLv3 Kx=RSA  Au=RSA   Enc=AES(128) Mac=SHA1
		"AES256-SHA",               // SSLv3 Kx=RSA  Au=RSA   Enc=AES(256) Mac=SHA1
		NULL
	};

	// поддерживаемый список шифров
	QList<QSslCipher> cipher_list;

	const char** ciphers = AVALON_CIPHERS;
	while ((*ciphers) != NULL)
	{
		QSslCipher cipher(*ciphers, QSsl::SslV3);
		if (cipher.isNull() == false)
			cipher_list.append(cipher);

		ciphers++;
	}

	// задание конфигурации ssl по умолчанию
	QSslConfiguration ssl_default = QSslConfiguration::defaultConfiguration();

	ssl_default.setProtocol(QSsl::TlsV1);
	ssl_default.setCiphers(cipher_list);

	QSslConfiguration::setDefaultConfiguration(ssl_default);

	// значения по умолчанию
	AnonymousName = QString::fromUtf8("Аноним");
	DateFormat    = "dd.MM.yyyy hh:mm:ss";

	Me.ID = 0;

	reload();
}
//----------------------------------------------------------------------------------------------

AGlobal::~AGlobal ()
{
	g_global = NULL;
}
//----------------------------------------------------------------------------------------------

void AGlobal::reload ()
{
	QSettings settings;

#ifdef AVALON_USE_ZLIB
	Compression = settings.value("storage/compression", false).toInt();
#endif

	m_rsdn_port = settings.value("rsdn/port", 443).toInt();
	m_rsdn_host = settings.value("rsdn/host", "rsdn.org").toString().toLower();

	if (m_rsdn_port == 443)
		m_rsdn_proto = "https";
	else
		m_rsdn_proto = "http";

	m_rsdn_url = QString("%1://%2").arg(m_rsdn_proto).arg(m_rsdn_host);

	// информация о текущем пользователе avalon
	Me.ID             = -1;
	Me.Name           = "(n/a)";
	Me.Nick           = "(n/a)";
	Me.RealName       = "(n/a)";
	Me.Email          = "(n/a)";
	Me.Homepage       = "(n/a)";
	Me.Specialization = "(n/a)";
	Me.WhereFrom      = "(n/a)";
	Me.Origin         = "(n/a)";

	std::auto_ptr<IAStorage> storage(AStorageFactory::getStorage());

	if (storage.get() != NULL)
	{
		Me.Name = settings.value("rsdn/login", "").toString();
		storage->whoAmI(Me);
	}
}
//----------------------------------------------------------------------------------------------
