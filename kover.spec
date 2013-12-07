Summary:	WYSIWYG CD cover printer with CDDB support
Name:		kover
Version:	6
Release:	4
Group:		Archiving/Other
License:	GPLv2+
Url:		http://lisas.de/kover
Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	cdda-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	pkgconfig(libcddb)
BuildRequires:	pkgconfig(libcdio)

%description
Kover is an easy to use WYSIWYG CD cover printer with CDDB support. 

%files -f %{name}.lang
%{_bindir}/kover
%{_datadir}/apps/%{name}
%{_datadir}/applications/kde4/%{name}.desktop
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/locolor/*/apps/*.png
%{_iconsdir}/kover_back_content.png
%{_iconsdir}/kover_back_title_content.png
%{_iconsdir}/kover_cdaudio.png
%{_iconsdir}/kover_front_title-content-right_content-left.png
%{_iconsdir}/kover_front_title-right_content-left.png
%{_iconsdir}/kover_front_title_only.png
%{_iconsdir}/kover_one_page.png
%{_mandir}/man1/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%find_lang %{name}

