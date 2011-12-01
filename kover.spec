%define	name	kover
%define	version	4
%define	release %mkrel 7

Name:           %{name}
Summary:        WYSIWYG CD cover printer with CDDB support
Version:        %{version}
Release:        %{release}
Source:         %{name}-%{version}.tar.bz2
Patch0:		    %{name}-fix-mimetypes.patch
Patch1:		kover-4-gcc44.patch
URL:            http://lisas.de/kover
Group:          Archiving/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
BuildRequires:	kdelibs4-devel
BuildRequires:	libcdio-devel
BuildRequires:	libcddb-devel

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support. 

%files
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
%patch1 -p1

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
cd build
make DESTDIR=%buildroot install

%clean
rm -rf %{buildroot}
