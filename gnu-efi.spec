#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : gnu-efi
Version  : 3.0.13
Release  : 64
URL      : file:///aot/build/clearlinux/packages/gnu-efi/gnu-efi-v3.0.13.tar.gz
Source0  : file:///aot/build/clearlinux/packages/gnu-efi/gnu-efi-v3.0.13.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: gnu-efi-data = %{version}-%{release}

%description
-------------------------------------------------
Building EFI Applications Using the GNU Toolchain
-------------------------------------------------

%package data
Summary: data components for the gnu-efi package.
Group: Data

%description data
data components for the gnu-efi package.


%package dev
Summary: dev components for the gnu-efi package.
Group: Development
Requires: gnu-efi-data = %{version}-%{release}
Provides: gnu-efi-devel = %{version}-%{release}
Requires: gnu-efi = %{version}-%{release}

%description dev
dev components for the gnu-efi package.


%package staticdev
Summary: staticdev components for the gnu-efi package.
Group: Default
Requires: gnu-efi-dev = %{version}-%{release}

%description staticdev
staticdev components for the gnu-efi package.


%prep
%setup -q -n gnu-efi
cd %{_builddir}/gnu-efi

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1626874547
export GCC_IGNORE_WERROR=1
## altflags1 content
export CFLAGS=""
export CXXFLAGS=""
export FCFLAGS=""
export FFLAGS=""
export CFFLAGS=""
export LDFLAGS=""
export ARCH=x86_64
export CC=gcc
export AS=as
export LD=ld.bfd
export AR=ar
export RANLIB=ranlib
export OBJCOPY=objcopy
## altflags1 end
## make_macro content
make ARCH=x86_64 V=1 VERBOSE=1 -j16
make ARCH=x86_64 V=1 VERBOSE=1 -j16 apps
## make_macro end


%install
export SOURCE_DATE_EPOCH=1626874547
rm -rf %{buildroot}
%make_install
## install_append content
install -dm 0755 %{buildroot}/usr/share/efi
install -m 755 -p x86_64/apps/*.efi %{buildroot}/usr/share/efi/
## install_append end

%files
%defattr(-,root,root,-)
/usr/lib64/crt0-efi-x86_64.o
/usr/lib64/elf_x86_64_efi.lds

%files data
%defattr(-,root,root,-)
/usr/share/efi/AllocPages.efi
/usr/share/efi/FreePages.efi
/usr/share/efi/bltgrid.efi
/usr/share/efi/debughook.efi
/usr/share/efi/drv0.efi
/usr/share/efi/drv0_use.efi
/usr/share/efi/exit.efi
/usr/share/efi/lfbgrid.efi
/usr/share/efi/modelist.efi
/usr/share/efi/printenv.efi
/usr/share/efi/route80h.efi
/usr/share/efi/setdbg.efi
/usr/share/efi/setjmp.efi
/usr/share/efi/t.efi
/usr/share/efi/t2.efi
/usr/share/efi/t3.efi
/usr/share/efi/t4.efi
/usr/share/efi/t5.efi
/usr/share/efi/t6.efi
/usr/share/efi/t7.efi
/usr/share/efi/t8.efi
/usr/share/efi/tcc.efi
/usr/share/efi/unsetdbg.efi

%files dev
%defattr(-,root,root,-)
/usr/include/efi/efi.h
/usr/include/efi/efi_nii.h
/usr/include/efi/efi_pxe.h
/usr/include/efi/efiapi.h
/usr/include/efi/eficompiler.h
/usr/include/efi/eficon.h
/usr/include/efi/eficonex.h
/usr/include/efi/efidebug.h
/usr/include/efi/efidef.h
/usr/include/efi/efidevp.h
/usr/include/efi/efierr.h
/usr/include/efi/efifs.h
/usr/include/efi/efigpt.h
/usr/include/efi/efiip.h
/usr/include/efi/efilib.h
/usr/include/efi/efilink.h
/usr/include/efi/efinet.h
/usr/include/efi/efipart.h
/usr/include/efi/efipciio.h
/usr/include/efi/efipoint.h
/usr/include/efi/efiprot.h
/usr/include/efi/efipxebc.h
/usr/include/efi/efirtlib.h
/usr/include/efi/efiser.h
/usr/include/efi/efisetjmp.h
/usr/include/efi/efishell.h
/usr/include/efi/efishellintf.h
/usr/include/efi/efistdarg.h
/usr/include/efi/efitcp.h
/usr/include/efi/efiudp.h
/usr/include/efi/efiui.h
/usr/include/efi/lib.h
/usr/include/efi/libsmbios.h
/usr/include/efi/pci22.h
/usr/include/efi/protocol/adapterdebug.h
/usr/include/efi/protocol/eficonsplit.h
/usr/include/efi/protocol/efidbg.h
/usr/include/efi/protocol/efivar.h
/usr/include/efi/protocol/intload.h
/usr/include/efi/protocol/legacyboot.h
/usr/include/efi/protocol/piflash64.h
/usr/include/efi/protocol/vgaclass.h
/usr/include/efi/romload.h
/usr/include/efi/x86_64/efibind.h
/usr/include/efi/x86_64/efilibplat.h
/usr/include/efi/x86_64/efisetjmp_arch.h
/usr/include/efi/x86_64/pe.h
/usr/lib64/pkgconfig/gnu-efi.pc

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libefi.a
/usr/lib64/libgnuefi.a
