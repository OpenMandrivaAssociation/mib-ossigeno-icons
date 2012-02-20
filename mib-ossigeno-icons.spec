%define		oname		MIB-Ossigeno-Ultimate-Icons
%define		oversion	4.3

Name:		mib-ossigeno-icons
Version:	4.3.0
Release:	%mkrel 69.3
Summary:	MIB-Ossigeno icon theme
# http://kde-look.org/content/show.php/?content=128221
Source0:	%{oname}-%{oversion}.tar.gz
License:	LGPL
Group:		Graphical desktop/KDE
URL:		http://mib.pianetalinux.org/mib/
BuildArch:	noarch
Obsoletes:	mib-ossigeno-icon-theme < %{version}

%description
MIB-Ossigeno Ultimate Icons is a blue icon theme derived from Oxygen Icons.
It differs from Oxygen mainly for folder icons, completely redesigned.
MIB-Ossigeno Ultimate Icons theme has been developed by emanueleeeee.

%prep
%setup -q -n %{oname}

%build

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_iconsdir}/%{oname}

%__cp -rf ./* %{buildroot}%{_iconsdir}/%{oname}/

%__rm -f %{buildroot}%{_iconsdir}/%{oname}/README
%__rm -f %{buildroot}%{_iconsdir}/%{oname}/Changelog

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc README Changelog
%{_iconsdir}/%{oname}/*

