%define name clutter
%define version 0.8.7
%define git 20090218
%if %git
%define release %mkrel 0.%git.1
%else
%define release %mkrel 1
%endif

%define api 0.8
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
Source0:       http://www.clutter-project.org/sources/clutter/0.8/%{name}-%{version}.tar.bz2
%endif
Patch1:	       clutter-0.8.6-fix-str-fmt.patch
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: X11-devel
BuildRequires: GL-devel
BuildRequires: pango-devel
BuildRequires: glib2-devel
BuildRequires: libgdk_pixbuf2.0-devel
BuildRequires: gtk-doc
BuildConflicts: %{name}-devel < %{version}

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
Group:         Graphics

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
%patch1 -p0

%build
%configure2_5x --enable-gtk-doc
%make

%install
rm -rf %buildroot

%makeinstall_std

%clean
rm -rf %buildroot

%files -n %libname
%defattr(-,root,root)
%_libdir/lib%{name}-glx-%{api}.so.*

%files -n %libnamedevel
%_libdir/pkgconfig/%{name}-%{api}.pc
%_libdir/pkgconfig/%{name}-glx-%{api}.pc
%_libdir/pkgconfig/%{name}-x11-%{api}.pc
%_libdir/lib%{name}-glx-%{api}.la
%_libdir/lib%{name}-glx-%{api}.so
%dir %_includedir/%{name}-%{api}
%_includedir/%{name}-%{api}/%{name}
%_includedir/%{name}-%{api}/cogl
%dir %_datadir/gtk-doc/html/%name
%doc %_datadir/gtk-doc/html/%name/*
%dir %_datadir/gtk-doc/html/cogl
%doc %_datadir/gtk-doc/html/cogl/*
