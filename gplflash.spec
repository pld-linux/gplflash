Summary:	Flash animations redering library
Summary(pl):	Biblioteka renderuj�ca animacje Flash
Name:		gplflash
Version:	0.4.13
Release:	2
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
BuildConflicts:	flash
Obsoletes:	flash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPLFLash is based on Olivier Debons original work, which hasn't had a
release since June 2000. This project hope to bring GPLFlash back as a
free, portable and useable alternative to the Flash-decoder released
by Macromedia. The project contains a decoding library, a player and
(perhaps most importantly) a Mozilla/Netscape plugin.

%description -l pl
GPLFlash to biblioteka oparta na pocz�tkowej pracy Olivera Debonsa,
kt�ra nie by�a wydawana od czerwca 2000. Autorzy maj� nadziej�, �e ten
projekt wskrzesi GPLFlash jako wolnodost�pn�, przeno�n� i u�ywaln�
alternatyw� dla dekodera Flasha wydawanego przez Macromedi�. Projekt
zawiera bibliotek� dekoduj�c�, odtwarza� i (prawdopodobnie
najwa�niejsz�) wtyczk� Mozilli/Netscape'a.

%package devel
Summary:	Header file required to build programs using gplflash library
Summary(pl):	Pliki nag��wkowe wymagane przez programy u�ywaj�ce gplflash
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	flash-devel

%description devel
Header files required to build programs using gplflash library.

%description devel -l pl
Pliki nag��wkowe niezb�dne do kompilacji program�w korzystaj�cych z
biblioteki gplflash.

%package static
Summary:	Static gplflash library
Summary(pl):	Statyczna biblioteka gplflash
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	flash-static

%description static
Static gplflash library.

%description static -l pl
Statyczna biblioteka gplflash.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla plugin for Flash rendering
Summary(pl):	Wtyczka Mozilli wu�wietlaj�ca animacje Flash
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Obsoletes:	mozilla-plugin-flash

%description -n mozilla-plugin-%{name}
Mozilla plugin for rendering of Flash animations based on gplflash
library.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka Mozilli wy�wietlaj�ca animacje Flash bazuj�ca na bibliotece
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
	--with-plugin-dir=%{_libdir}/mozilla/plugins \
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

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/lib*flash.so
