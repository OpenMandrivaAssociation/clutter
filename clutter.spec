%define name clutter
%define version 1.6.8
%define rel 1

%define api 1.0
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

Summary:       Software library for fast, visually rich GUIs
Name:          %{name}
Version:       %{version}
Release:       %mkrel 1
Source0:       http://www.clutter-project.org/sources/clutter/1.4/%{name}-%{version}.tar.bz2
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libx11-devel
BuildRequires: libxext-devel
BuildRequires: libxcomposite-devel >= 0.4
BuildRequires: libxdamage-devel
BuildRequires: libxfixes-devel >= 3
BuildRequires: GL-devel
BuildRequires: atk-devel >= 1.17
BuildRequires: pango-devel >= 1.20
BuildRequires: glib2-devel >= 2.26.0
BuildRequires: libgdk_pixbuf2.0-devel >=2.0
BuildRequires: libjson-glib-devel >= 0.12.0
BuildRequires: gobject-introspection-devel >= 0.9.5
BuildRequires: gtk-doc
BuildRequires: docbook-dtd412-xml
BuildRequires: x11-server-xvfb

%description
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

#----------------------------------------------------------------------------

%package i18n
Summary: Translations for %name
Group: System/Internationalization

%description i18n
This contains the translation data for %name.

%package -n %libname
Summary:       Software library for fast, visually rich GUIs
Group:         System/Libraries
Requires: %name-i18n >= %version

%description -n %libname
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

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
%setup -q
%apply_patches

%build
%configure2_5x --enable-gtk-doc
#git from 20090602 does not work with parallel make
xvfb-run %make

%install
rm -rf %buildroot

%makeinstall_std
%find_lang %name-%api

%clean
rm -rf %buildroot

%files i18n -f %name-%api.lang

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{name}-glx-%{api}.so.*
%_libdir/girepository-1.0/Cally-%api.typelib
%_libdir/girepository-1.0/Clutter-%api.typelib
%_libdir/girepository-1.0/ClutterX11-%api.typelib
%_libdir/girepository-1.0/Cogl-%api.typelib

%files -n %libnamedevel
%defattr(-,root,root)
%_libdir/pkgconfig/cally-%{api}.pc
%_libdir/pkgconfig/cogl-%{api}.pc
%_libdir/pkgconfig/cogl-gl-%{api}.pc
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/pkgconfig/%{name}-glx-%{api}.pc
%_libdir/pkgconfig/%{name}-x11-%{api}.pc
%_libdir/lib%{name}-glx-%{api}.la
%_libdir/lib%{name}-glx-%{api}.so
%dir %_includedir/%{name}-%{api}
%_includedir/%{name}-%{api}/cally
%_includedir/%{name}-%{api}/%{name}
%_includedir/%{name}-%{api}/cogl
%_datadir/gir-1.0/Cally-%api.gir
%_datadir/gir-1.0/Clutter-%api.gir
%_datadir/gir-1.0/ClutterX11-%api.gir
%_datadir/gir-1.0/Cogl-%api.gir
%_datadir/gtk-doc/html/cally
%_datadir/gtk-doc/html/%name
%_datadir/gtk-doc/html/cogl
