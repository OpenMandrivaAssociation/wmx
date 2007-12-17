%define name wmx
%define version 6pl1
%define release %mkrel 3

Summary: A minimal window manager
Name: %{name}
Version: %{version}
Release: %{release}
License: BSD-like
Url: http://www.all-day-breakfast.com/wmx/
Group: Graphical desktop/Other
Source0: %{name}-%{version}.tar.bz2
Patch1: wmx-syntax-fix.patch.bz2
Patch2: wmx-my-config.patch.bz2
Patch3: wmx-64bitptr.patch.bz2
Requires: rxvt
BuildRequires: X11-devel

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
%configure
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

