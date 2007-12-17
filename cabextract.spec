Summary: A program to extract Microsoft Cabinet files
Name: cabextract
Version: 1.2
Release: %mkrel 2
Group: Archiving/Compression
License: GPL
Source: http://www.kyz.uklinux.net/downloads/%{name}-%{version}.tar.bz2
URL: http://www.kyz.uklinux.net/cabextract.php3

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
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(0644, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%attr(0755, root, root) %{_bindir}/cabextract
%{_mandir}/man1/cabextract.1*


