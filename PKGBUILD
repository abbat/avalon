# Maintainer: Anton Batenev <antonbatenev@yandex.ru>

pkgname=('avalon')
pkgver=1.0.446
pkgrel=1
pkgdesc="RSDN offline client"
arch=('i686' 'x86_64')
url="https://github.com/abbat/avalon/tree/1.0"
license=('BSD')
depends=('qt4' 'qtwebkit' 'aspell' 'zlib')
makedepends=('git')
optdepends=('aspell-ru: Russian dictionary for aspell' 'aspell-en: English dictionary for aspell')
conflicts=('avalon')
source=("git+https://github.com/abbat/avalon.git#tag=v${pkgver}")
sha256sums=('SKIP')

build() {
    cd "${pkgname}"

    qmake-qt4 -project -recursive -Wall -nopwd -o "avalon.pro" \
        "CONFIG += release"                                \
        "QT += network sql webkit"                         \
        "INCLUDEPATH += src"                               \
        "DEFINES += AVALON_PACKAGE"                        \
        "LIBS += -laspell -lz"                             \
        src

    qmake-qt4 "avalon.pro"
    make
}

package() {
    cd "${pkgname}"

    install -d "${pkgdir}/usr/bin"
    install -d "${pkgdir}/usr/share/pixmaps"
    install -d "${pkgdir}/usr/share/applications"

    install -D -m755 avalon               "${pkgdir}/usr/bin/avalon"
    install -D -m644 avalon.desktop       "${pkgdir}/usr/share/applications/avalon.desktop"
    install -D -m644 src/icons/avalon.xpm "${pkgdir}/usr/share/pixmaps/avalon.xpm"
    install -D -m644 README.md            "${pkgdir}/usr/share/doc/avalon/README.md"
    install -D -m644 debian/copyright     "${pkgdir}/usr/share/licenses/avalon/LICENSE"
}
