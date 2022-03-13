Summary:	A program to extract Microsoft Cabinet files
Name:		cabextract
Version:	1.9.1
Release:	3
License:	GPLv2+
Group:		Archiving/Compression
Url:		http://www.cabextract.org.uk
Source0:	http://www.cabextract.org.uk/%{name}-%{version}.tar.gz
BuildRequires:	autoconf automake gettext-devel

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to distribute
their software, and things like Windows Font Packs. The cabextract program
simply unpacks such files.

%files
%doc AUTHORS ChangeLog NEWS README
%{_bindir}/cabextract
%{_mandir}/man1/cabextract.1*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
