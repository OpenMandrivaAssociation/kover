%define	name	kover
%define	version	3
%define	release %mkrel 3

Name:           %{name}
Summary:        WYSIWYG CD cover printer with CDDB support
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.bz2
Patch0:		%{name}-fix-mimetypes.patch
URL:            http://lisas.de/kover
Group:          Archiving/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2 or later
BuildRequires:	kdelibs-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcddb-devel
BuildRequires:	desktop-file-utils

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support. 

%post
%update_menus
%update_icon_cache hicolor
%update_icon_cache locolor
%update_mime_database

%postun
%clean_menus
%clean_icon_cache hicolor
%clean_icon_cache locolor
%clean_mime_database

%files -f %name.lang
%defattr(-,root,root,0755)
%doc AUTHORS README TODO THANKS ChangeLog
%{_bindir}/kover
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/locolor/*/apps/*.png
%{_datadir}/apps/%{name}
%{_mandir}/man1/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_datadir}/mimelnk/application/*

#--------------------------------------------------------------------
%prep
%setup -q

%build
%if "%{_lib}" != "lib"
kdelibsuffix="--enable-libsuffix=%(A=%{_lib}; echo ${A/lib/})"
%endif
%configure2_5x --disable-rpath $kdelibsuffix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/applnk/Multimedia/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-install --vendor="" \
  --add-category="Utility" \
  --add-category="DiscBurning" \
  --add-category="KDE" \
  --add-category="Qt" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT
