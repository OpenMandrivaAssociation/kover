%define	name	kover
%define	version	6
%define	release 1

Name:           %{name}
Summary:        WYSIWYG CD cover printer with CDDB support
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.bz2
URL:            http://lisas.de/kover
Group:          Archiving/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
BuildRequires:	kdelibs4-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcddb-devel
BuildRequires:	cdda-devel

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support. 

%files -f %{name}.lang
%defattr(-,root,root,0755)
%{_bindir}/kover
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/locolor/*/apps/*.png
%{_datadir}/apps/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/kover_back_content.png
%{_iconsdir}/kover_back_title_content.png
%{_iconsdir}/kover_cdaudio.png
%{_iconsdir}/kover_front_title-content-right_content-left.png
%{_iconsdir}/kover_front_title-right_content-left.png
%{_iconsdir}/kover_front_title_only.png
%{_iconsdir}/kover_one_page.png

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=%buildroot install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 4-6mdv2011.0
+ Revision: 666041
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 4-5mdv2011.0
+ Revision: 606271
- rebuild

* Thu Nov 12 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 4-4mdv2010.1
+ Revision: 465248
- Rebuild against new Qt

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 4-3mdv2010.0
+ Revision: 425496
- rebuild
- fix compilation with gcc 4.4

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - New upstream tarball including our "link fix"

  + Funda Wang <fwang@mandriva.org>
    - correct license

* Sat Nov 15 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 4-1mdv2009.1
+ Revision: 303469
- Fix file list
- Update to kde4 kover version

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Oden Eriksson <oeriksson@mandriva.com> 3-4mdv2008.1
+ Revision: 141734
- rebuilt against openldap-2.4.7 libs

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Sep 20 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 3-3mdv2008.0
+ Revision: 91460
- Fix File list
- Move kover in tools
- Install existing mimetype x-kover

* Sat Jul 14 2007 Adam Williamson <awilliamson@mandriva.org> 3-1mdv2008.0
+ Revision: 52158
- rebuild for 2008
- clean file list
- update MIME database and icon cache in %%post
- drop old menu file
- install menu entry to the right place and correct it
- buildrequires libcdio and libcddb (app now uses these)
- specify license as GPLv2 or later
- drop sourced icons (not needed)
- drop patch (no longer needed, larger values are now default upstream)
- new release 3
- Import kover



* Mon Jun 26 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.9.6-5mdv2007.0
- Rebuild to generate category

* Mon May 08 2006 Laurent MONTEL <lmontel@mandriva.com> 2.9.6-4
- Rebuild to generate category

* Mon Jan 16 2006 Nicolas L�cureuil <neoclust@mandriva.org> 2.9.6-3mdk
- Add patch2 : Fix ticket #20442
- clean spec
- use mkrel

* Fri Jul 08 2005 Laurent MONTEL <lmontel@mandriva.com> 2.9.6-2mdk
- Rebuild

* Fri Nov 12 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.9.6-1mdk
- 2.9.6
- cleanups

* Tue Oct 26 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 2.9.5-4mdk
- fix deps and build on lib64 platforms

* Thu Aug 12 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.5-3mdk
- Remove explicite dependance on kdebase

* Fri Jun 04 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.5-2mdk
- Rebuild

* Mon May 17 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.5-1mdk
- 2.9.5

* Tue Apr 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.3-1mdk
- 2.9.3

* Fri Jul 18 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.1-5mdk
- Rebuild

* Fri Apr 25 2003 Marcel Pol <mpol@gmx.net> 2.9.1-4mdk
- buildrequires

* Mon Mar 03 2003 Marcel Pol <mpol@gmx.net> 2.9.1-3mdk
- fix buildrequires

* Sat Mar 01 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 2.9.1-2mdk
- Rebuild

* Fri Feb 21 2003 Lenny Cartier <lenny@mandrakesoft.com> 2.9.1-1mdk
- 2.9.1

* Wed Oct 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.7-1mdk
- 2.8.7

* Sat Aug 17 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.6-3mdk
- Rebuild against gcc-3.2

* Sat Jul 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.6-2mdk
- Rebuild against gcc-3.2

* Wed Jul 24 2002  Lenny Cartier <lenny@mandrakesoft.com> 2.8.6-1mdk
- 2.8.6

* Tue Jul 09 2002 Lenny Cartier <lenny@mandrakesoft.com> 2.8.5-3mdk
- patch1: libtool tag

* Sat Jun 01 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.5-2mdk
- Rebuild

* Sat May 25 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 2.8.5-1mdk
- new version

* Fri Jan 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.3-2mdk
- Fix spec file

* Thu Nov 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.8.3-1mdk
- Update code (0.8.3)

* Tue Oct 23 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.8-2mdk
- fixes by Claudio Panichi <sorcla@tiscalinet.it> :
	- Added missing files
	- Added menu entry
	- Fixed permissions on source file

* Wed Oct 17 2001 Claudio Panichi <sorcla@tiscalinet.it> 0.8-1mdk
- First personal RPM for Linux Mandrake =:o)
