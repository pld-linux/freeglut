Summary:	A freely licensed alternative to the GLUT library
Summary(pl):	Zamiennik biblioteki GLUT na wolnej licencji
Name:		freeglut
Version:	2.4.0
Release:	1
License:	MIT
Group:		Libraries
Source0:	http://dl.sourceforge.net/freeglut/%{name}-%{version}.tar.gz
# Source0-md5:	6d16873bd876fbf4980a927cfbc496a1
Patch0:		%{name}-gcc4.patch
URL:		http://freeglut.sourceforge.net/
BuildRequires:	OpenGL-GLU-devel
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXxf86vm-devel
Provides:	OpenGL-glut = 3.7
Obsoletes:	glut
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

%description -l pl
Freeglut to Free OpenGL Utility Toolkit, maj±cy byæ wolnodostêpnym
zamiennikiem biblioteki GLUT Marka Kilgarda. Jest rozprowadzany na
licencji w stylu X-Consortium (szczegó³y w pliku COPYING), aby
umo¿liwiæ korzystanie i/lub modyfikowanie ¼róde³.

Korzysta z bibliotek OpenGL, GLU i pthread. Biblioteka nie korzysta z
¿adnego kodu GLUT-a i nie jest w 100% kompatybilna. Do dzia³ania
aplikacji z freeglutem mo¿e byæ konieczna rekompilacja kodu i/lub ma³e
modyfikacje.

%package devel
Summary:	Header files for freeglut library
Summary(pl):	Pliki nag³ówkowe biblioteki freeglut
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-GLU-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXxf86vm-devel
Provides:	OpenGL-glut-devel = 3.7
Obsoletes:	glut-devel

%description devel
Header files for freeglut library.

%description devel -l pl
Pliki nag³ówkowe biblioteki freeglut.

%package static
Summary:	Static freeglut library
Summary(pl):	Statyczna biblioteka freeglut
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	OpenGL-glut-static = 3.7
Obsoletes:	glut-static

%description static
Static freeglut library.

%description static -l pl
Statyczna biblioteka freeglut.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
%doc AUTHORS COPYING ChangeLog NEWS README TODO doc/{freeglut.html,index.html,progress.html,*.png}
%lang(fr) %doc LISEZ_MOI
%attr(755,root,root) %{_libdir}/libglut.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/{freeglut_user_interface.html,structure.html}
%attr(755,root,root) %{_libdir}/libglut.so
%{_libdir}/libglut.la
%{_includedir}/GL/freeglut*.h
%{_includedir}/GL/glut.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libglut.a
