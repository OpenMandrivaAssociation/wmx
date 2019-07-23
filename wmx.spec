%define name wmx
%define version 6pl1
%define release  10

Summary: A minimal window manager
Name: %{name}
Version: %{version}
Release:	1
License: BSD-like
Url: http://www.all-day-breakfast.com/wmx/
Group: Graphical desktop/Other
Source0: %{name}-%{version}.tar.bz2
Patch1: wmx-syntax-fix.patch
Patch2: wmx-my-config.patch
Patch3: wmx-64bitptr.patch
Requires: rxvt
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xext)
BuildRequires: pkgconfig(xpm)

%description
wmx is another window manager for X. It provides a unusual style of
window decoration and only minimal functionality--no icons, no toolbars,
no docks. wmx is barely configurable except by editing the source and
recompiling the code.

%prep
%setup -q
%patch1 -p0
%patch2 -p0
%patch3 -p0

%build
%configure2_5x
%make

%install
rm -fr %buildroot
install -d %buildroot%_bindir
install -d %buildroot/%_sysconfdir/X11/wmsession.d/
install -m 755 wmx %buildroot%_bindir/wmx

cat << EOF > %buildroot/%_sysconfdir/X11/wmsession.d/25wmx
NAME=wmx
EXEC=/usr/bin/wmx
DESC=Minimal windows manager without configuration
SCRIPT:
exec /usr/bin/wmx
EOF
cat <<XCLIENTS > Xclients
#!/bin/sh
# This is an example of ~/.Xclients file to start wmx

xdaliclock -transparent -fg black -builtin1 -24 -noseconds -geometry -5-5 -xrm "*overrideRedirect: True" &
exec wmx
XCLIENTS

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%doc README* UPDATES Xclients Config.h
%{_bindir}/wmx
%config(noreplace) %{_sysconfdir}/X11/wmsession.d/25wmx



%changelog
* Tue Feb 01 2011 Funda Wang <fwang@mandriva.org> 6pl1-8mdv2011.0
+ Revision: 634848
- simplify BR
- bunzip2 the patches

* Wed Sep 09 2009 Thierry Vignaud <tv@mandriva.org> 6pl1-7mdv2010.0
+ Revision: 434941
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tv@mandriva.org> 6pl1-6mdv2009.0
+ Revision: 262122
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 6pl1-5mdv2009.0
+ Revision: 256337
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 6pl1-3mdv2008.1
+ Revision: 129441
- kill re-definition of %%buildroot on Pixel's request
- buildrequires X11-devel instead of XFree86-devel
- import wmx


* Mon Jan 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 6pl1-3mdk
- Fix build on x86_64 (patch 3)

* Fri Jul 01 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 6pl1-2mdk
- Rebuild

* Tue Jun 08 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 6pl1-1mdk
- New version: 6 patch level 1

* Sun Jun 06 2004 Michael Scherer <misc@mandrake.org> 6-3mdk 
- rebuild for new gcc

* Wed Jun 02 2004 Michael Scherer <misc@mandrake.org> 6-2mdk
- add wmsession.d files
- add BuildRequires
- strip is done automatically
- add Config.h to %%doc
 
* Thu May 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 6-1mdk
- Initial package
- Use rxvt by default
- Don't use ugly pixmaps
- Reduce workspace flip delay
