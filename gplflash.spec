Summary:	Flash animations redering library
Summary(pl.UTF-8):	Biblioteka renderująca animacje Flash
Name:		gplflash
Version:	0.4.13
Release:	7
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gplflash/%{name}-%{version}.tar.bz2
# Source0-md5:	1b14c21094eb07416842ac0f5298b3f1
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-link.patch
URL:		http://gplflash.sourceforge.net/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.357
BuildRequires:	zlib-devel >= 1.1.4
BuildConflicts:	flash
Obsoletes:	flash
Obsoletes:	gplflash2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary(pl.UTF-8):	Pliki nagłówkowe wymagane przez programy używające gplflash
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	flash-devel
Obsoletes:	gplflash2-devel

%description devel
Header files required to build programs using gplflash library.

%description devel -l pl.UTF-8
Pliki nagłówkowe niezbędne do kompilacji programów korzystających z
biblioteki gplflash.

%package static
Summary:	Static gplflash library
Summary(pl.UTF-8):	Statyczna biblioteka gplflash
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	flash-static
Obsoletes:	gplflash2-static

%description static
Static gplflash library.

%description static -l pl.UTF-8
Statyczna biblioteka gplflash.

%package -n browser-plugin-%{name}
Summary:	Browser plugin for Flash rendering
Summary(pl.UTF-8):	Wtyczka przeglądarki wyświetlająca animacje Flash
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	browser-plugins(%{_target_base_arch})
Requires:	browser-plugins >= 2.0
Provides:	browser(flash)
# Provides for migrate purposes (greedy poldek upgrade)
Provides:	mozilla-plugin-gplflash
Obsoletes:	browser-plugin-gplflash2
Obsoletes:	mozilla-plugin-flash
Obsoletes:	mozilla-plugin-gplflash
Obsoletes:	mozilla-plugin-gplflash2

%description -n browser-plugin-%{name}
Browser plugin for rendering of Flash animations based on gplflash
library.

%description -n browser-plugin-%{name} -l pl.UTF-8
Wtyczka przeglądarki wyświetlająca animacje Flash oparta na bibliotece
gplflash.

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
	--with-plugin-dir=%{_browserpluginsdir} \
	--enable-shared \
	--enable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# include in -devel and -static instead?
rm -f $RPM_BUILD_ROOT%{_libdir}/browser-plugins/libnpflash.{l,}a

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/swfplayer.desktop
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}/swfplayer.png

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post -n browser-plugin-%{name}
%update_browser_plugins

%postun -n browser-plugin-%{name}
if [ "$1" = 0 ]; then
	%update_browser_plugins
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*

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
%attr(755,root,root) %{_browserpluginsdir}/libnpflash.so
