%define _build_name_fmt %{NAME}-%{VERSION}-%{RELEASE}.%{ARCH}.rpm
%define _rpmdir %{expand:%%(pwd)}/..

Name:      kvm-no-cloud-init
Version:   1.26
Release:   1%{?dist}
Vendor:    socha.it
Summary:   Simple cloud-init like script.
Group:     System
License:   Public Domain
URL:       https://github.com/rjsocha/kvm-no-cloud-init
Packager:  Robert Socha
Requires:  bash
Requires:  dmidecode
Requires:  curl
Source:     %{expand:%%(pwd)}

%description
Simple cloud-init like script for local kvm/qemu configuration (via SMBios oem-strings).

%prep
%setup -T -c
rsync -aq --delete "%{SOURCEURL0}/../lib" "%{SOURCEURL0}/../sbin" .
echo  %{_target}, %{_target_arch}, and %{_target_os}.
exit

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 ${RPM_BUILD_ROOT}/usr/lib/systemd/system
install -d -m755 ${RPM_BUILD_ROOT}/sbin
install -m644 lib/systemd/system/kvm-no-cloud-init-network.service $RPM_BUILD_ROOT/usr/lib/systemd/system/
install -m644 lib/systemd/system/kvm-no-cloud-init-no-network.service $RPM_BUILD_ROOT/usr/lib/systemd/system/
install -m755 sbin/kvm-no-cloud-init $RPM_BUILD_ROOT/sbin/

%files
%attr(0755, root, root) /sbin/kvm-no-cloud-init
%attr(0644, root, root) /usr/lib/systemd/system/*.service

%post
%systemd_post kvm-no-cloud-init-network.service kvm-no-cloud-init-no-network.service
systemctl enable kvm-no-cloud-init-network.service kvm-no-cloud-init-no-network.service

%preun
systemctl disable kvm-no-cloud-init-network.service kvm-no-cloud-init-no-network.service
%systemd_preun kvm-no-cloud-init-network.service kvm-no-cloud-init-no-network.service
