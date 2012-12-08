%define api 1.0
%define major 0
%define girmajor	1.0

%define libname		%mklibname %{name} %{api} %{major}
%define girname		%mklibname %{name}-gir %{girmajor}
%define develname	%mklibname -d %{name} %{api}

Summary:       Software library for fast, visually rich GUIs
Name:          clutter
Version:       1.12.2
Release:       1
License:       LGPLv2+
Group:         Graphics
Url:           http://clutter-project.org/
Source0:       ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/1.12/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(atk)
BuildRequires:	pkgconfig(cairo-gobject)
BuildRequires:	pkgconfig(cogl-1.0)
BuildRequires:	pkgconfig(cogl-pango-1.0)
BuildRequires:	pkgconfig(gdk-3.0)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(json-glib-1.0)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(pangoft2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xcomposite)
BuildRequires:	pkgconfig(xdamage)
BuildRequires:	pkgconfig(xext)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	pkgconfig(xi)

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

%description i18n
This contains the translation data for %{name}.

%package -n %{libname}
Summary:	Software library for fast, visually rich GUIs
Group:		System/Libraries
Suggests:	%{name}-i18n >= %{version}-%{release}

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Development headers/libraries for %{name}
Group:		Development/X11
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Obsoletes:	%mklibname %{name} %{api} %{major} -d

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
%{_libdir}/girepository-1.0/ClutterGdk-%{girmajor}.typelib
%{_libdir}/girepository-1.0/ClutterX11-%{api}.typelib

%files -n %{develname}
%dir %{_includedir}/%{name}-%{api}
%{_includedir}/%{name}-%{api}/cally
%{_includedir}/%{name}-%{api}/%{name}
%{_libdir}/lib%{name}-%{api}.so
%{_libdir}/lib%{name}-glx-%{api}.so
%{_libdir}/pkgconfig/cally-%{api}.pc
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/pkgconfig/%{name}-cogl-%{api}.pc
%{_libdir}/pkgconfig/%{name}-gdk-%{api}.pc
%{_libdir}/pkgconfig/%{name}-glx-%{api}.pc
%{_libdir}/pkgconfig/%{name}-x11-%{api}.pc
%{_datadir}/gir-1.0/Cally-%{api}.gir
%{_datadir}/gir-1.0/Clutter-%{api}.gir
%{_datadir}/gir-1.0/ClutterGdk-%{girmajor}.gir
%{_datadir}/gir-1.0/ClutterX11-%{api}.gir
%{_datadir}/gtk-doc/html/cally
%{_datadir}/gtk-doc/html/%{name}



%changelog
* Mon Oct 29 2012 Arkady L. Shane <ashejn@rosalab.ru> 1.12.2-1
- update to 0.12.2

* Tue Oct  2 2012 Arkady L. Shane <ashejn@rosalab.ru> 1.12.0-2
- rebuilt againt new cogl

* Mon Oct  1 2012 Arkady L. Shane <ashejn@rosalab.ru> 1.12.0-1
- update to 1.12.0

* Tue Jun 19 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.10.8-1
+ Revision: 806221
- update to new version 1.10.8

* Tue May 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.10.6-1
+ Revision: 801026
- update to new version 1.10.6

* Wed May 16 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.10.4-1
+ Revision: 799158
- new version 1.10.4

* Sun Apr 29 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.10.2-1
+ Revision: 794459
- new version 1.10.2
- cleaned up spec

* Mon Jan 30 2012 Götz Waschk <waschk@mandriva.org> 1.8.4-1
+ Revision: 769851
- new version

* Mon Nov 28 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.8.2-1
+ Revision: 734779
- fixed files list
- adjust configure options for current version
- new version 1.8.2
- cleaned up spec
- split out gir pkg
- dropped major from devel pkg
- removed clean section
- disable static, gtk-doc & rpath builds
- removed .la files
- enabled gdk & x11 backends
- converted BRs to pkgconfig provides
- removed mkrel & BuildRoot

* Thu Sep 15 2011 Götz Waschk <waschk@mandriva.org> 1.6.20-2
+ Revision: 699836
- update to new version 1.6.20

* Tue Jun 14 2011 Götz Waschk <waschk@mandriva.org> 1.6.16-2
+ Revision: 685109
- new version
- new source URL

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.6.14-2
+ Revision: 663386
- mass rebuild

* Tue Apr 05 2011 Götz Waschk <waschk@mandriva.org> 1.6.14-1
+ Revision: 650738
- update to new version 1.6.14

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 1.6.12-1
+ Revision: 650296
- update to new version 1.6.12

* Thu Mar 24 2011 Funda Wang <fwang@mandriva.org> 1.6.10-1
+ Revision: 648350
- new version 1.6.10

* Thu Mar 24 2011 Funda Wang <fwang@mandriva.org> 1.6.8-1
+ Revision: 648213
- update BR
- drop conditioned git
- new version 1.6.8

* Fri Sep 24 2010 Götz Waschk <waschk@mandriva.org> 1.4.0-1mdv2011.0
+ Revision: 580909
- new version

* Fri Sep 17 2010 Götz Waschk <waschk@mandriva.org> 1.3.14-1mdv2011.0
+ Revision: 579248
- new version
- update file list
- build with Xvfb

* Mon Sep 13 2010 Götz Waschk <waschk@mandriva.org> 1.3.12-3mdv2011.0
+ Revision: 577979
- rebuild for new g-i

* Fri Aug 20 2010 Götz Waschk <waschk@mandriva.org> 1.3.12-2mdv2011.0
+ Revision: 571445
- fix deps (teuf)

* Tue Aug 17 2010 Götz Waschk <waschk@mandriva.org> 1.3.12-1mdv2011.0
+ Revision: 570827
- update to new version 1.3.12

* Thu Aug 05 2010 Götz Waschk <waschk@mandriva.org> 1.3.10-1mdv2011.0
+ Revision: 566363
- new version
- drop patch
- add i18n package

* Sat Jul 31 2010 Funda Wang <fwang@mandriva.org> 1.3.8-2mdv2011.0
+ Revision: 563842
- rebuild

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 1.3.8-1mdv2011.0
+ Revision: 563632
- fix introspection build
- new version
- add cally

* Fri Jul 30 2010 Funda Wang <fwang@mandriva.org> 1.2.12-2mdv2011.0
+ Revision: 563498
- rebuild for new gobject-introspection

* Wed Jul 14 2010 Götz Waschk <waschk@mandriva.org> 1.2.12-1mdv2011.0
+ Revision: 553388
- update to new version 1.2.12

* Mon May 10 2010 Frederic Crozat <fcrozat@mandriva.com> 1.2.8-1mdv2010.1
+ Revision: 544362
- Release 1.2.8

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 1.2.6-2mdv2010.1
+ Revision: 540013
- rebuild so that shared libraries are properly stripped again

* Mon Apr 19 2010 Götz Waschk <waschk@mandriva.org> 1.2.6-1mdv2010.1
+ Revision: 536785
- new version
- drop patch

* Thu Mar 25 2010 Frederic Crozat <fcrozat@mandriva.com> 1.2.4-2mdv2010.1
+ Revision: 527523
- Patch0 (Owen): fix actor allocation (OH bug #2024)

* Mon Mar 22 2010 Götz Waschk <waschk@mandriva.org> 1.2.4-1mdv2010.1
+ Revision: 526351
- new version

* Mon Mar 15 2010 Götz Waschk <waschk@mandriva.org> 1.2.2-1mdv2010.1
+ Revision: 520281
- update to new version 1.2.2

* Wed Mar 03 2010 Götz Waschk <waschk@mandriva.org> 1.2.0-1mdv2010.1
+ Revision: 513780
- new version

* Fri Feb 26 2010 Götz Waschk <waschk@mandriva.org> 1.1.14-1mdv2010.1
+ Revision: 511492
- update to new version 1.1.14

* Tue Feb 23 2010 Götz Waschk <waschk@mandriva.org> 1.1.12-1mdv2010.1
+ Revision: 510303
- new version
- drop patch

* Tue Feb 09 2010 Götz Waschk <waschk@mandriva.org> 1.1.10-1mdv2010.1
+ Revision: 503188
- add patch to fix build on x86_64
- new version
- add dep on json-glib
- update file list

* Mon Jan 11 2010 Götz Waschk <waschk@mandriva.org> 1.0.10-1mdv2010.1
+ Revision: 489816
- update to new version 1.0.10

* Fri Nov 06 2009 Götz Waschk <waschk@mandriva.org> 1.0.8-1mdv2010.1
+ Revision: 460938
- update to new version 1.0.8

* Thu Sep 24 2009 Götz Waschk <waschk@mandriva.org> 1.0.6-1mdv2010.0
+ Revision: 448147
- new version
- drop patch
- remove build workarounds

* Tue Aug 18 2009 Götz Waschk <waschk@mandriva.org> 1.0.2-4mdv2010.0
+ Revision: 417564
- fix introspection patch

* Mon Aug 17 2009 Götz Waschk <waschk@mandriva.org> 1.0.2-3mdv2010.0
+ Revision: 417255
- fix for new gobject-introspection

* Sat Aug 15 2009 Götz Waschk <waschk@mandriva.org> 1.0.2-2mdv2010.0
+ Revision: 416468
- update to new version 1.0.2
- update build deps for doc generation

* Wed Aug 12 2009 Götz Waschk <waschk@mandriva.org> 1.0.0-2mdv2010.0
+ Revision: 415261
- move typelib files to lib package
- fix library package group

* Wed Jul 29 2009 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2010.0
+ Revision: 403982
- new version
- new API version

* Sun Jul 19 2009 Götz Waschk <waschk@mandriva.org> 0.9.8-1mdv2010.0
+ Revision: 397473
- update to new version 0.9.8

* Thu Jul 02 2009 Götz Waschk <waschk@mandriva.org> 0.9.6-1mdv2010.0
+ Revision: 391812
- new version

* Sat Jun 20 2009 Götz Waschk <waschk@mandriva.org> 0.9.4-1mdv2010.0
+ Revision: 387483
- new version

* Tue Jun 16 2009 Götz Waschk <waschk@mandriva.org> 0.9.3-0.20090616.1mdv2010.0
+ Revision: 386340
- new snapshot
- drop patch
- bump introspection dep

* Tue Jun 02 2009 Götz Waschk <waschk@mandriva.org> 0.9.3-0.20090602.1mdv2010.0
+ Revision: 382274
- new snapshot
- fix installation
- add introspection support

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.9.3-0.20090511.1mdv2010.0
+ Revision: 374598
- git snapshot

* Mon May 11 2009 Götz Waschk <waschk@mandriva.org> 0.9.2-1mdv2010.0
+ Revision: 374502
- new version
- new api
- drop patch
- disable --as-needed
- update file list

* Sat Feb 21 2009 Götz Waschk <waschk@mandriva.org> 0.8.8-1mdv2009.1
+ Revision: 343557
- new version
- disable --no-undefined again

* Wed Feb 18 2009 Götz Waschk <waschk@mandriva.org> 0.8.7-0.20090218.1mdv2009.1
+ Revision: 342287
- new git snapshot needed for gnome-games
- reenable --no-undefined
- build gtk-docs

* Thu Feb 12 2009 Funda Wang <fwang@mandriva.org> 0.8.6-1mdv2009.1
+ Revision: 339713
- New version 0.8.6

* Sat Nov 08 2008 Oden Eriksson <oeriksson@mandriva.com> 0.8.2-1mdv2009.1
+ Revision: 301078
- 0.8.2
- drop one upstream patch (P0)
- added one upstream patch (P0)
- rebuilt against new libxcb

* Sat Sep 13 2008 Colin Guthrie <cguthrie@mandriva.org> 0.8.0-1mdv2009.0
+ Revision: 284359
- New version: 0.8.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers
    - normalize call to ldconfig in %%post/%%postun

* Wed Feb 20 2008 Colin Guthrie <cguthrie@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 173175
- New version

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 0.4.1-1mdv2008.1
+ Revision: 136322
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Colin Guthrie <cguthrie@mandriva.org>
    - New upstream version 0.4.1

* Wed Aug 08 2007 Colin Guthrie <cguthrie@mandriva.org> 0.4.0-1mdv2008.0
+ Revision: 60514
- New version: 0.4.0

* Fri Jun 22 2007 Colin Guthrie <cguthrie@mandriva.org> 0.2.3-1mdv2008.0
+ Revision: 42895
- Import clutter

