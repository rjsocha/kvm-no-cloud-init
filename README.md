# kvm-no-cloud-init

Simple cloud-init like configuration tool for KVM virtual machines.
kvm/qemu guest configuration support via SMBIOS OEM strings.

Supported configuration options
 - name - hostname
 - user - create new user/set password
 - group - user's group membership
 - ssh - authorized keys
 - regenerate-ssh-host-keys - ssh host keys
 - dns-registry - register hotname in central (private) DNS service

 
Configuration via:

```
virt-install ...
  --sysinfo oemStrings.entry0=kvm-cnf-no-net!user:socha!group:sudo@socha!name=vm-name
```
