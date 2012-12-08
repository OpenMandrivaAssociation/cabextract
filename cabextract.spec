Summary: A program to extract Microsoft Cabinet files
Name: cabextract
Version: 1.4
Release: %mkrel 2
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
rm -rf ${RPM_BUILD_ROOT}
%makeinstall_std

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(0644, root, root, 0755)
%doc AUTHORS ChangeLog NEWS README
%attr(0755, root, root) %{_bindir}/cabextract
%{_mandir}/man1/cabextract.1*




%changelog
* Thu May 12 2011 Oden Eriksson <oeriksson@mandriva.com> 1.4-1mdv2011.0
+ Revision: 673762
- 1.4

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.3-3
+ Revision: 663350
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.3-2mdv2011.0
+ Revision: 564230
- rebuild for perl 5.12.1

* Sat Jul 24 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.3-1mdv2011.0
+ Revision: 557819
- new version
- new URL
- update license

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2-7mdv2010.1
+ Revision: 520017
- rebuilt for 2010.1

* Sun Aug 09 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2-6mdv2010.0
+ Revision: 413216
- rebuild

* Sat Dec 20 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2-5mdv2009.1
+ Revision: 316513
- rebuild

* Mon Jun 16 2008 Thierry Vignaud <tv@mandriva.org> 1.2-4mdv2009.0
+ Revision: 220498
- rebuild

* Fri Jan 11 2008 Thierry Vignaud <tv@mandriva.org> 1.2-3mdv2008.1
+ Revision: 149053
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 1.2-2mdv2008.1
+ Revision: 140691
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Jan 24 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.2-2mdv2007.0
+ Revision: 112781
- rebuild
- Import cabextract

* Fri Sep 22 2006 Götz Waschk <waschk@mandriva.org> 1.2-1mdv2007.0
- New version 1.2

* Sat May 13 2006 Stefan van der Eijk <stefan@eijk.nu> 1.1-3mdk
- rebuild for sparc

* Wed Nov 02 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.1-2mdk
- Rebuild

* Tue Oct 19 2004 Goetz Waschk <waschk@linux-mandrake.com> 1.1-1mdk
- New release 1.1

* Mon Mar 15 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0-1mdk
- autoconf 2.5 macro
- new version

