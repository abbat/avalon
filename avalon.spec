Name:           avalon
Version:        1.0.445
Release:        1
Summary:        RSDN offline client
Group:          Applications/Internet
License:        BSD-2-clause
URL:            https://github.com/abbat/avalon/tree/1.0
Conflicts:      avalon2
BuildRequires:  libqt4-devel >= 4.4, aspell-devel, zlib-devel
Source0:        https://build.opensuse.org/source/home:antonbatenev:avalon/avalon/avalon_%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
BuildRequires:  libQtWebKit-devel
%endif

%if 0%{?fedora} || 0%{?centos}
BuildRequires:  qtwebkit-devel
%endif

%define qmake qmake
%if 0%{?fedora} || 0%{?centos}
%define qmake qmake-qt4
%endif

%description
Offile client for Russian Software Developer Network


%prep
%setup -q -n %{name}


%build
%{qmake} -project -recursive -Wall -nopwd -o avalon.pro \
    "CONFIG += release"                                 \
    "QT += network sql webkit"                          \
    "INCLUDEPATH += src"                                \
    "DEFINES += AVALON_PACKAGE"                         \
    "LIBS += -laspell -lz"                              \
    src
%{qmake} avalon.pro
make %{?_smp_mflags}


%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_datadir}/pixmaps
install -d %{buildroot}%{_datadir}/applications

install -m755 avalon %{buildroot}%{_bindir}/avalon
install -m644 src/icons/avalon.xpm %{buildroot}%{_datadir}/pixmaps/avalon.xpm
install -m644 avalon.desktop %{buildroot}%{_datadir}/applications/avalon.desktop


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc README.md
%{_bindir}/avalon
%{_datadir}/pixmaps/avalon.xpm
%{_datadir}/applications/avalon.desktop


%changelog
* Fri Jun 24 2016 Anton Batenev <antonbatenev@yandex.ru> 1.0.445-1
- Initial RPM release
