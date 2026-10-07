Name:           ooifconfig
Version:        0.1.0
Release:        1%{?dist}
Summary:        Legacy network interface display reporting MAC addresses, MTUs, and packet RX/TX.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/ooifconfig
Source0:        ooifconfig-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
ooifconfig is a sovereign, capability-bounded INTERFACE CONFIG written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/ooifconfig
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/ooifconfig-uninstall

%files
/usr/bin/ooifconfig
/usr/bin/ooifconfig-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
