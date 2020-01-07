#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ryu
Version  : 4.32
Release  : 28
URL      : https://files.pythonhosted.org/packages/f5/21/4defc2601049fc50dd924bc28d03c1da5116ea5250b5b6e58b85371c1447/ryu-4.32.tar.gz
Source0  : https://files.pythonhosted.org/packages/f5/21/4defc2601049fc50dd924bc28d03c1da5116ea5250b5b6e58b85371c1447/ryu-4.32.tar.gz
Summary  : Component-based Software-defined Networking Framework
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: ryu-bin = %{version}-%{release}
Requires: ryu-data = %{version}-%{release}
Requires: ryu-license = %{version}-%{release}
Requires: ryu-python = %{version}-%{release}
Requires: ryu-python3 = %{version}-%{release}
Requires: eventlet
Requires: msgpack
Requires: netaddr
Requires: oslo.config
Requires: ovs
Requires: six
Requires: tinyrpc
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : tinyrpc
Patch1: 0001-change-default-to-usr-share-defaults-ryu.patch

%description
What's Ryu
==========
Ryu is a component-based software defined networking framework.

%package bin
Summary: bin components for the ryu package.
Group: Binaries
Requires: ryu-data = %{version}-%{release}
Requires: ryu-license = %{version}-%{release}

%description bin
bin components for the ryu package.


%package data
Summary: data components for the ryu package.
Group: Data

%description data
data components for the ryu package.


%package license
Summary: license components for the ryu package.
Group: Default

%description license
license components for the ryu package.


%package python
Summary: python components for the ryu package.
Group: Default
Requires: ryu-python3 = %{version}-%{release}

%description python
python components for the ryu package.


%package python3
Summary: python3 components for the ryu package.
Group: Default
Requires: python3-core

%description python3
python3 components for the ryu package.


%prep
%setup -q -n ryu-4.32
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557250017
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/ryu
cp LICENSE %{buildroot}/usr/share/package-licenses/ryu/LICENSE
cp debian/copyright %{buildroot}/usr/share/package-licenses/ryu/debian_copyright
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
install -d -m 755 %{buildroot}/usr/share/defaults/ryu
install -p -D -m 644 etc/ryu/ryu.conf %{buildroot}/usr/share/defaults/ryu/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ryu
/usr/bin/ryu-manager

%files data
%defattr(-,root,root,-)
/usr/share/defaults/ryu/ryu.conf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/ryu/LICENSE
/usr/share/package-licenses/ryu/debian_copyright

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
