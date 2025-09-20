#
# Conditional build:
%bcond_without	static_libs	# static library
%bcond_with	gles		# OpenGL ES instead of OpenGL
%bcond_with	wayland		# Wayland instead of X11

Summary:	A freely licensed alternative to the GLUT library
Summary(pl.UTF-8):	Zamiennik biblioteki GLUT na wolnej licencji
Name:		freeglut
Version:	3.6.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	https://downloads.sourceforge.net/freeglut/%{name}-%{version}.tar.gz
# Source0-md5:	1a1c4712b3100f49f5dea22a1ad57c34
URL:		https://freeglut.sourceforge.net/
%if %{with gles}
BuildRequires:	EGL-devel
BuildRequires:	OpenGLESv1-devel
BuildRequires:	OpenGLESv2-devel
%else
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	OpenGL-devel >= 1.0
%endif
BuildRequires:	cmake >= 3.1
%if %{with wayland}
BuildRequires:	EGL-devel
BuildRequires:	pkgconfig
BuildRequires:	wayland-devel
BuildRequires:	wayland-egl-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
%else
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
%endif
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
%if %{with wayland}
Requires:	EGL-devel
Requires:	wayland-devel
Requires:	wayland-egl-devel
Requires:	xorg-lib-libxkbcommon-devel
%else
Requires:	OpenGL-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXrandr-devel
Requires:	xorg-lib-libXxf86vm-devel
%endif
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
	%{!?with_static_libs:-DFREEGLUT_BUILD_STATIC_LIBS=OFF} \
	%{?with_gles:-DFREEGLUT_GLES=ON} \
	-DFREEGLUT_PRINT_WARNINGS=OFF \
	%{?with_wayland:-DFREEGLUT_WAYLAND=ON}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README.md
%attr(755,root,root) %{_libdir}/libglut.so.*.*.*
%ghost %{_libdir}/libglut.so.3

%files devel
%defattr(644,root,root,755)
%{_libdir}/libglut.so
%{_includedir}/GL/freeglut*.h
%{_includedir}/GL/glut.h
%{_pkgconfigdir}/glut.pc
%{_libdir}/cmake/FreeGLUT

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libglut.a
%endif
