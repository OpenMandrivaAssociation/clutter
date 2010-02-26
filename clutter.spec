%define name clutter
%define version 1.1.14
%define git 0
%if ! %git
%define release %mkrel 1
%else
%define release %mkrel -c %git 1
%endif

%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       Software library for fast, visually rich GUIs
Name:          %{name}
Version:       %{version}
Release:       %{release}
%if %git
Source0:       %{name}-%{git}.tar.bz2
%else
Source0:       http://www.clutter-project.org/sources/clutter/1.1/%{name}-%{version}.tar.bz2
%endif
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: X11-devel
BuildRequires: GL-devel
BuildRequires: pango-devel
BuildRequires: glib2-devel
BuildRequires: libgdk_pixbuf2.0-devel
BuildRequires: libjson-glib-devel
BuildRequires: gobject-introspection-devel >= 0.6.4
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml

%description
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

#----------------------------------------------------------------------------

%package -n %libname
Summary:       Software library for fast, visually rich GUIs
Group:         System/Libraries

%description -n %libname
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif

%postun -n %libname
%if %mdkversion < 200900
/sbin/ldconfig
%endif

#----------------------------------------------------------------------------

%package -n %libnamedevel
Summary:       Development headers/libraries for %name
Group:         Development/X11
Provides:      %name-devel = %version-%release
Requires:      %libname = %version-%release

%description -n %libnamedevel
Development headers/libraries for %name (see %libname package)

#----------------------------------------------------------------------------

%prep
%if %git
%setup -q -n %name
./autogen.sh -V
%else
%setup -q
%endif
%apply_patches

%build
%configure2_5x --enable-gtk-doc
#git from 20090602 does not work with parallel make
%make

%install
rm -rf %buildroot

%makeinstall_std

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{name}-glx-%{api}.so.*
%_libdir/girepository-1.0/Clutter-%api.typelib
%_libdir/girepository-1.0/Cogl-%api.typelib

%files -n %libnamedevel
%_libdir/pkgconfig/cogl-%{api}.pc
%_libdir/pkgconfig/cogl-gl-%{api}.pc
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/pkgconfig/%{name}-glx-%{api}.pc
%_libdir/pkgconfig/%{name}-x11-%{api}.pc
%_libdir/lib%{name}-glx-%{api}.la
%_libdir/lib%{name}-glx-%{api}.so
%dir %_includedir/%{name}-%{api}
%_includedir/%{name}-%{api}/%{name}
%_includedir/%{name}-%{api}/cogl
%_datadir/gir-1.0/Clutter-%api.gir
%_datadir/gir-1.0/Cogl-%api.gir
%dir %_datadir/gtk-doc/html/%name
%doc %_datadir/gtk-doc/html/%name/*
%dir %_datadir/gtk-doc/html/cogl
%doc %_datadir/gtk-doc/html/cogl/*
