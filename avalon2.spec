Name:           avalon2
Version:        2.0.8
Release:        1
Summary:        RSDN offline client
Group:          Applications/Internet
License:        BSD-2-clause
URL:            https://github.com/abbat/avalon
Conflicts:      avalon, avalon3
BuildRequires:  aspell-devel, zlib-devel
Source0:        https://build.opensuse.org/source/home:antonbatenev:avalon/avalon2/avalon2_%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%if 0%{?suse_version}
BuildRequires:  libqt5-qtbase-devel, libqt5-qttools-devel, libqt5-qtsvg-devel, libQt5WebKitWidgets-devel
%else
BuildRequires:  qt5-qtbase-devel, qt5-qttools-devel, qt5-qtsvg-devel, qt5-qtwebkit-devel
%endif

%description
Offile client for Russian Software Developer Network


%prep
%setup -q -n %{name}


%build
export builddir=$(pwd)

qmake-qt5 -project -recursive -Wall -nopwd -o avalon.pro       \
    "CONFIG         += release"                                \
    "QT             += network sql core widgets webkitwidgets" \
    "INCLUDEPATH    += src"                                    \
    "DEFINES        += AVALON_PACKAGE"                         \
    "LIBS           += -laspell -lz"                           \
    "QMAKE_CPPFLAGS *= ${RPM_OPT_FLAGS}"                       \
    "QMAKE_CFLAGS   *= ${RPM_OPT_FLAGS}"                       \
    "QMAKE_CXXFLAGS *= ${RPM_OPT_FLAGS}"                       \
    "QMAKE_LFLAGS   *= ${RPM_LD_FLAGS}"                        \
    "${builddir}/src"
qmake-qt5 avalon.pro
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
* Wed Jun 3 2020 Anton Batenev <antonbatenev@yandex.ru> 2.0.8-1
- Initial RPM release
