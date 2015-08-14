Summary: Bloonix plugins for Postfix.
Name: bloonix-plugins-postfix
Version: 0.7
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
Requires: bloonix-agent
Requires: bloonix-core
Requires: curl
AutoReqProv: no

%description
bloonix-plugins-postfix provides plugins to check postfix.

%define blxdir /usr/lib/bloonix
%define docdir %{_docdir}/%{name}-%{version}

%prep
%setup -q -n %{name}-%{version}

%build
%{__perl} Configure.PL --prefix /usr
%{__make}

%install
rm -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
mkdir -p ${RPM_BUILD_ROOT}%{docdir}
install -c -m 0444 LICENSE ${RPM_BUILD_ROOT}%{docdir}/
install -c -m 0444 ChangeLog ${RPM_BUILD_ROOT}%{docdir}/

%post
if [ ! -e "/etc/bloonix/agent/sudoers.d" ] ; then
    mkdir -p /etc/bloonix/agent/sudoers.d
    chown root:root /etc/bloonix/agent/sudoers.d
    chmod 755 /etc/bloonix/agent/sudoers.d
fi
if [ ! -e "/etc/bloonix/agent/conf.d" ] ; then
    mkdir -p /etc/bloonix/agent/conf.d
    chown root:bloonix /etc/bloonix/agent/conf.d
    chmod 750 /etc/bloonix/agent/conf.d
fi
for f in check-postfix ; do
    if [ ! -e "/etc/bloonix/agent/sudoers.d/$f" ] ; then
        cp -a /usr/lib/bloonix/etc/sudoers.d/$f /etc/bloonix/agent/sudoers.d/
        chmod 440 /etc/bloonix/agent/sudoers.d/$f
    fi
    if [ ! -e "/etc/bloonix/agent/conf.d/$f" ] ; then
        cp -a /usr/lib/bloonix/etc/conf.d/$f.conf /etc/bloonix/agent/conf.d/
        chmod 640 /etc/bloonix/agent/conf.d/$f.conf
        chown root:bloonix /etc/bloonix/agent/conf.d/$f.conf
    fi
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %{blxdir}/etc/sudoers.d
%{blxdir}/etc/sudoers.d/*

%dir %{blxdir}/etc/conf.d
%{blxdir}/etc/conf.d/*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Fri Aug 14 2015 Jonny Schulz <js@bloonix.de> - 0.7-1
- Added a configuration file with use_sudo for each check that
  to executed via sudo.
* Tue Dec 02 2014 Jonny Schulz <js@bloonix.de> - 0.6-1
- Fixed handling of sudo files.
* Sun Nov 30 2014 Jonny Schulz <js@bloonix.de> - 0.5-1
- Added the info that sudo is necessary to execute this plugin.
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.4-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.3-1
- Licence added and old releases deleted.
* Tue Apr 15 2014 Jonny Schulz <js@bloonix.de> - 0.2-1
- Initial package.
