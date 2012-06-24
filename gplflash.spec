Summary:	Flash animations redering library
Summary(pl.UTF-8):   Biblioteka renderująca animacje Flash
Name:		gplflash
Version:	0.4.13
Release:	2.3
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gplflash/%{name}-%{version}.tar.bz2
# Source0-md5:	1b14c21094eb07416842ac0f5298b3f1
Patch0:		%{name}-link.patch
URL:		http://gplflash.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	zlib-devel >= 1.1.4
BuildRequires:	rpmbuild(macros) >= 1.224
BuildConflicts:	flash
Obsoletes:	flash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_plugindir	%{_libdir}/browser-plugins

%description
GPLFLash is based on Olivier Debons original work, which hasn't had a
release since June 2000. This project hope to bring GPLFlash back as a
free, portable and useable alternative to the Flash-decoder released
by Macromedia. The project contains a decoding library, a player and
(perhaps most importantly) a Mozilla/Netscape plugin.

%description -l pl.UTF-8
GPLFlash to biblioteka oparta na początkowej pracy Olivera Debonsa,
która nie była wydawana od czerwca 2000. Autorzy mają nadzieję, że ten
projekt wskrzesi GPLFlash jako wolnodostępną, przenośną i używalną
alternatywę dla dekodera Flasha wydawanego przez Macromedię. Projekt
zawiera bibliotekę dekodującą, odtwarzać i (prawdopodobnie
najważniejszą) wtyczkę Mozilli/Netscape'a.

%package devel
Summary:	Header file required to build programs using gplflash library
Summary(pl.UTF-8):   Pliki nagłówkowe wymagane przez programy używające gplflash
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	flash-devel

%description devel
Header files required to build programs using gplflash library.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
biblioteki gplflash.

%package static
Summary:	Static gplflash library
Summary(pl.UTF-8):   Statyczna biblioteka gplflash
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	flash-static

%description static
Static gplflash library.

%description static -l pl.UTF-8
Statyczna biblioteka gplflash.

%package -n browser-plugin-%{name}
Summary:	Browser plugin for Flash rendering
Summary(pl.UTF-8):   Wtyczka Mozilli wuświetlająca animacje Flash
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-plugin-flash
Obsoletes:	mozilla-plugin-gplflash
Requires:	browser-plugins

# use macro, otherwise extra LF isinserted along with the ifarch
%ifarch %{ix86} ppc sparc sparc64
%define	browsers mozilla, mozilla-firefox, opera, konqueror
%else
%define	browsers mozilla, mozilla-firefox, konqueror
%endif

%description -n browser-plugin-%{name}
Browser plugin for rendering of Flash animations based on gplflash
library.

Supported browsers: %{browsers}.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka Mozilli wyświetlająca animacje Flash bazująca na bibliotece
gplflash.

Supported browsers: %{browsers}.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--with-plugin-dir=%{_plugindir} \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%triggerin -n browser-plugin-%{name} -- mozilla-firefox
%ns_plugin_install -d %{_libdir}/mozilla-firefox/plugins libnpflash.so

%triggerun -n browser-plugin-%{name} -- mozilla-firefox
%ns_plugin_uninstall -d %{_libdir}/mozilla-firefox/plugins libnpflash.so

%triggerin -n browser-plugin-%{name} -- mozilla
%ns_plugin_install -d %{_libdir}/mozilla/plugins libnpflash.so

%triggerun -n browser-plugin-%{name} -- mozilla
%ns_plugin_uninstall -d %{_libdir}/mozilla/plugins libnpflash.so

%ifarch %{ix86} ppc sparc sparc64
%triggerin -n browser-plugin-%{name} -n browser-plugin-%{name} -- opera
%ns_plugin_install -d %{_libdir}/opera/plugins libnpflash.so

%triggerun -n browser-plugin-%{name} -- opera
%ns_plugin_uninstall -d %{_libdir}/opera/plugins libnpflash.so
%endif

%triggerin -n browser-plugin-%{name} -- konqueror
%ns_plugin_install -d %{_libdir}/kde3/plugins/konqueror libnpflash.so

%triggerun -n browser-plugin-%{name} -- konqueror
%ns_plugin_uninstall -d %{_libdir}/kde3/plugins/konqueror libnpflash.so

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files -n browser-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_plugindir}/libnpflash.so
