Summary: A program to extract Microsoft Cabinet files
Name: cabextract
Version: 1.4
Release: %mkrel 1
Group: Archiving/Compression
License: GPLv2+
Source: http://www.cabextract.org.uk/%{name}-%{version}.tar.gz
URL: http://www.cabextract.org.uk/
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
Cabinet (.CAB) files are a form of archive, which Microsoft use to
distribute their software, and things like Windows Font Packs. The
cabextract program simply unpacks such files.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(0644, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%attr(0755, root, root) %{_bindir}/cabextract
%{_mandir}/man1/cabextract.1*


