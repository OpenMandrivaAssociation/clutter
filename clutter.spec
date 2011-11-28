%define api 1.0
%define major 0
%define girmajor	1.0

%define libname		%mklibname %{name} %{api} %{major}
%define girname		%mklibname %{name}-gir %{girmajor}
%define develname	%mklibname -d %{name} %{api}

Summary:       Software library for fast, visually rich GUIs
Name:          clutter
Version:       1.8.2
Release:       1
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
Source0:       ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(atk) >= 2.1.5
BuildRequires:	pkgconfig(cairo-gobject) >= 1.10
BuildRequires:	pkgconfig(cogl-1.0) >= 1.8.0
BuildRequires:	pkgconfig(cogl-pango-1.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0) >= 2.26.0
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(json-glib-1.0) >= 0.12.0
BuildRequires:	pkgconfig(pangocairo) >= 1.20
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite) >= 0.4
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes) >= 3
BuildRequires:	pkgconfig(xi)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 0.9.5

%description
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

%package i18n
Summary: Translations for %{name}
Group: System/Internationalization
%define libnamedevel	%mklibname
%description i18n
This contains the translation data for %{name}.

%package -n %{libname}
Summary:       Software library for fast, visually rich GUIs
Group:         System/Libraries

%description -n %{libname}
Clutter is an open source software library for creating fast, visually rich
graphical user interfaces. The most obvious example of potential usage is in
media center type applications. We hope however it can be used for a lot more.

Clutter uses OpenGL (and soon optionally OpenGL ES) for rendering but with an
API which hides the underlying GL complexity from the developer. The Clutter
API is intended to be easy to use, efficient and flexible. 

%package -n %{girname}
Summary:        GObject Introspection interface description for %{name}
Group:          System/Libraries
Requires:       %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:       Development headers/libraries for %{name}
Group:         Development/X11
Provides:      %{name}-devel = %{version}-%{release}
Requires:      %{libname} = %{version}-%{release}
Obsoletes:		%mklibname %{name} %{api} %{major} -d

%description -n %{develname}
Development headers/libraries for %{name} (see %{libname} package)

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--disable-rpath \
	--enable-introspection=yes \
	--enable-gdk-backend=yes \
	--enable-x11-backend=yes

%make

%install
rm -rf %{buildroot}

%makeinstall_std
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang %{name}-%{api}

%files i18n -f %{name}-%{api}.lang

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/lib%{name}-glx-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Cally-%{api}.typelib
%{_libdir}/girepository-1.0/Clutter-%{api}.typelib
%{_libdir}/girepository-1.0/ClutterX11-%{api}.typelib
%{_libdir}/girepository-1.0/Cogl-%{api}.typelib

%files -n %{develname}
%{_libdir}/pkgconfig/cally-%{api}.pc
%{_libdir}/pkgconfig/cogl-%{api}.pc
%{_libdir}/pkgconfig/cogl-gl-%{api}.pc
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-glx-%{api}.pc
%{_libdir}/pkgconfig/%{name}-x11-%{api}.pc
%{_libdir}/lib%{name}-glx-%{api}.so
%dir %{_includedir}/%{name}-%{api}
%{_includedir}/%{name}-%{api}/cally
%{_includedir}/%{name}-%{api}/%{name}
%{_includedir}/%{name}-%{api}/cogl
%{_datadir}/gir-1.0/Cally-%{api}.gir
%{_datadir}/gir-1.0/Clutter-%{api}.gir
%{_datadir}/gir-1.0/ClutterX11-%{api}.gir
%{_datadir}/gir-1.0/Cogl-%{api}.gir
%{_datadir}/gtk-doc/html/cally
%{_datadir}/gtk-doc/html/%{name}
%{_datadir}/gtk-doc/html/cogl
