Summary:	Flash animations redering library
Summary(pl):	Biblioteka renderuj±ca animacje flash
Name:		gplflash
Version:	0.4.13
Release:	1
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/gplflash/%{name}-%{version}.tar.bz2
# Source0-md5:	1b14c21094eb07416842ac0f5298b3f1
URL:		http://gplflash.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libjpeg-devel
BuildRequires:	zlib-devel >= 1.1.4
BuildRequires:	XFree86-devel
BuildRequires:	libmad-devel >= 0.14.2b
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GPLFLash is based on Olivier Debons original work, which hasen't had a
release since June 2000. This project hope to bring GPLFlash back as a
free, portable and useable alternative to the flash-decoder released
by Macromedia The project contains a decoding library, a player and
(perhaps most importantly) a mozilla/netscape plugin.

%package devel
Summary:	Header file required to build programs using gplflash library
Summary(pl):	Pliki nag³ówkowe wymagane przez programy u¿ywaj±ce gplflash
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files required to build programs using gplflash library.

%description devel -l pl
Pliki nag³ówkowe niezbêdne do kompilacji programów korzystaj±cych z
biblioteki gplflash.

%package static
Summary:	Static gplflash library
Summary(pl):	Statyczna biblioteka gplflash
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static gplflash library.

%description static -l pl
Statyczna biblioteka gplflash.

%package -n mozilla-plugin-%{name}
Summary:	Mozilla plugin for Flash rendering
Summary(pl):	Wtyczka mozilli wu¶wietlaj±ca animacje flash
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description -n mozilla-plugin-%{name}
Mozilla plugin for rendering of Flash animations based on gplflash
library.

%description -n mozilla-plugin-%{name} -l pl
Wtyczka mozilli wy¶wietlaj±ca animacje flash bazuj±ca na bibliotece
gplflash.

%prep
%setup -q

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
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.a

%files -n mozilla-plugin-%{name}
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/mozilla/plugins/lib*flash.so
