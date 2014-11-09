Summary: Bloonix plugins for Postfix.
Name: bloonix-plugins-postfix
Version: 0.4
Release: 1%{dist}
License: Commercial
Group: Utilities/System
Distribution: RHEL and CentOS

Packager: Jonny Schulz <js@bloonix.de>
Vendor: Bloonix

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Source0: http://download.bloonix.de/sources/%{name}-%{version}.tar.gz
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

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%dir %{blxdir}
%dir %{blxdir}/plugins
%{blxdir}/plugins/check-*
%{blxdir}/etc/plugins/plugin-*

%dir %attr(0755, root, root) %{docdir}
%doc %attr(0444, root, root) %{docdir}/ChangeLog
%doc %attr(0444, root, root) %{docdir}/LICENSE

%changelog
* Mon Nov 03 2014 Jonny Schulz <js@bloonix.de> - 0.4-1
- Updated the license information.
* Tue Aug 26 2014 Jonny Schulz <js@bloonix.de> - 0.3-1
- Licence added and old releases deleted.
* Tue Apr 15 2014 Jonny Schulz <js@bloonix.de> - 0.2-1
- Initial package.
