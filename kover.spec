%define	name	kover
%define	version	2.9.6
%define	release %mkrel 5

Name:           %{name}
Summary:        WYSIWYG CD cover printer with CDDB support
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.bz2
Source2:        kover.png
Source3:        kover16.png
Source4:        kover32.png
Source5:        kover48.png
Patch2:         kover-2.9.6-fix-windowsize.patch
URL:            http://lisas.de/kover
Group:          Archiving/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	kdelibs-devel

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support. 

%prep
%setup -q
cp %{SOURCE2} .
%patch2  -p1

%build
%if "%{_lib}" != "lib"
kdelibsuffix="--enable-libsuffix=%(A=%{_lib}; echo ${A/lib/})"
%endif
%configure2_5x --disable-rpath $kdelibsuffix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall


#Menu

install -m644 %{SOURCE3} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
install -m644 %{SOURCE4} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -m644 %{SOURCE5} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

install -d $RPM_BUILD_ROOT%{_menudir}
kdedesktop2mdkmenu.pl %{name} "System/Archiving/Other" $RPM_BUILD_ROOT%{_datadir}/applnk/Multimedia/kover.desktop $RPM_BUILD_ROOT%{_menudir}/%{name}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS README TODO THANKS ChangeLog
%{_bindir}/kover
%{_bindir}/cddb-id
%{_bindir}/cd-text
%{_menudir}/%{name}
%{_miconsdir}/*.png
%{_iconsdir}/*.png
%{_liconsdir}/*.png
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/locolor/*/apps/*.png

%dir %_datadir/apps/
%dir %_datadir/apps/kover/
%_datadir/apps/kover/koverui.rc
%dir %_datadir/apps/kover/pics
%_datadir/apps/kover/pics/*.png

%_mandir/man1/*

%dir %_datadir/applnk/
%dir %_datadir/applnk/Multimedia/
%_datadir/applnk/Multimedia/kover.desktop

%dir %_datadir/mimelnk/
%dir %_datadir/mimelnk/application/
%_datadir/mimelnk/application/*.desktop
