%define name clutter
%define version 0.8.2
%define svn 0
%if %svn
%define release %mkrel 0.%svn.1
%else
%define release %mkrel 1
%endif

%define api 0.8
%define major 0
%define libname %mklibname %name %api %major
%define libnamedevel %mklibname -d %name %api

# (cg) Do this for now, but fix propperly later.
%define _disable_ld_no_undefined 1

Summary:       Software library for fast, visually rich GUIs
Name:          %{name}
Version:       %{version}
Release:       %{release}
%if %svn
Source0:       %{name}-%{svn}.tar.bz2
%else
Source0:       %{name}-%{version}.tar.bz2
%endif
Patch0: clutter-0.8.2-bug1201.diff
License:       LGPL
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
%if %svn
%setup -q -n %name
./autogen.sh -V
%else
%setup -q
%endif

%patch0 -p0

%build
%configure
%make

%install
rm -rf %buildroot

%makeinstall

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
