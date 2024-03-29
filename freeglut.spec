Summary:	A freely licensed alternative to the GLUT library
Summary(pl.UTF-8):	Zamiennik biblioteki GLUT na wolnej licencji
Name:		freeglut
Version:	3.2.2
Release:	2
License:	MIT
Group:		Libraries
Source0:	https://downloads.sourceforge.net/freeglut/%{name}-%{version}.tar.gz
# Source0-md5:	485c1976165315fc42c0b0a1802816d9
URL:		https://freeglut.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel
BuildRequires:	cmake >= 3.0.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Provides:	OpenGL-glut = 4.0
Obsoletes:	glut < 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Freeglut, the Free OpenGL Utility Toolkit, is meant to be a free
alternative to Mark Kilgard's GLUT library. It is distributed under an
X-Consortium style license (see COPYING for details), to offer you a
chance to use and/or modify the source.

It makes use of OpenGL, GLU, and pthread libraries. The library does
not make use of any GLUT code and is not 100% compatible. Code
recompilation and/or slight modifications might be required for your
applications to work with freeglut.

%description -l pl.UTF-8
Freeglut to Free OpenGL Utility Toolkit, mający być wolnodostępnym
zamiennikiem biblioteki GLUT Marka Kilgarda. Jest rozprowadzany na
licencji w stylu X-Consortium (szczegóły w pliku COPYING), aby
umożliwić korzystanie i/lub modyfikowanie źródeł.

Korzysta z bibliotek OpenGL, GLU i pthread. Biblioteka nie korzysta z
żadnego kodu GLUT-a i nie jest w 100% kompatybilna. Do działania
aplikacji z freeglutem może być konieczna rekompilacja kodu i/lub małe
modyfikacje.

%package devel
Summary:	Header files for freeglut library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki freeglut
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXxf86vm-devel
Provides:	OpenGL-glut-devel = 4.0
Obsoletes:	glut-devel < 4

%description devel
Header files for freeglut library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki freeglut.

%package static
Summary:	Static freeglut library
Summary(pl.UTF-8):	Statyczna biblioteka freeglut
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	OpenGL-glut-static = 4.0
Obsoletes:	glut-static < 4

%description static
Static freeglut library.

%description static -l pl.UTF-8
Statyczna biblioteka freeglut.

%prep
%setup -q

%build
install -d build
cd build
%cmake .. \
	-DFREEGLUT_PRINT_WARNINGS=OFF

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

# disable completeness check incompatible with split packaging
%{__sed} -i -e '/^foreach(target .*IMPORT_CHECK_TARGETS/,/^endforeach/d; /^unset(_IMPORT_CHECK_TARGETS)/d' \
	$RPM_BUILD_ROOT%{_libdir}/cmake/FreeGLUT/FreeGLUTTargets.cmake

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libglut.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglut.so.3

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libglut.so
%{_includedir}/GL/freeglut*.h
%{_includedir}/GL/glut.h
%{_pkgconfigdir}/glut.pc
%{_libdir}/cmake/FreeGLUT

%files static
%defattr(644,root,root,755)
%{_libdir}/libglut.a
