Name:      kvm-no-cloud-init
Version:   1.25
Release:   1%{?dist}
Vendor:    socha.it
Summary:   Simple cloud-init like script for local kvm/qemu configuration (via SMBios oem-strings)
Group:     System
License:   Public Domain
URL:       https://github.com/rjsocha/kvm-no-cloud-init
Packager:  Robert Socha
Requires:  bash
Requires:  dmidecode
Requires:  curl
Source:     %{expand:%%(pwd)}

%description
Simple cloud-init like script for local kvm/qemu configuration (via SMBios oem-strings)

%prep
%setup -T -c
rsync -aq --delete "%{SOURCEURL0}/../lib" "%{SOURCEURL0}/../sbin" .
exit

%install
rm -rf $RPM_BUILD_ROOT
install -d -m755 ${RPM_BUILD_ROOT}/usr/lib/systemd/system
install -d -m755 ${RPM_BUILD_ROOT}/sbin
install -m644 lib/systemd/system/kvm-no-cloud-init-network.service $RPM_BUILD_ROOT/usr/lib/systemd/system/
install -m644 lib/systemd/system/kvm-no-cloud-init-no-network.service $RPM_BUILD_ROOT/usr/lib/systemd/system/
install -m755 sbin/kvm-no-cloud-init $RPM_BUILD_ROOT/sbin/

%files
%attr(-, root, root) /sbin/kvm-no-cloud-init
%attr(-, root, root) /usr/lib/systemd/system/*.service
