#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ryu
Version  : 3.25.1
Release  : 2
URL      : https://pypi.python.org/packages/source/r/ryu/ryu-3.25.1.tar.gz
Source0  : https://pypi.python.org/packages/source/r/ryu/ryu-3.25.1.tar.gz
Summary  : Component-based Software-defined Networking Framework
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: ryu-bin
Requires: ryu-config
Requires: ryu-python
BuildRequires : FormEncode-python
BuildRequires : eventlet-python
BuildRequires : lxml-python
BuildRequires : msgpack-python-python
BuildRequires : oslo.config
BuildRequires : paramiko-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pylint-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : repoze.lru-python
BuildRequires : routes-python
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
BuildRequires : stevedore
BuildRequires : webob-python

%description
What's Ryu
==========
Ryu is a component-based software defined networking framework.

%package bin
Summary: bin components for the ryu package.
Group: Binaries
Requires: ryu-config

%description bin
bin components for the ryu package.


%package config
Summary: config components for the ryu package.
Group: Default

%description config
config components for the ryu package.


%package python
Summary: python components for the ryu package.
Group: Default
Requires: eventlet-python
Requires: msgpack-python-python
Requires: routes-python
Requires: six-python
Requires: webob-python

%description python
python components for the ryu package.


%prep
%setup -q -n ryu-3.25.1

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ryu
/usr/bin/ryu-manager

%files config
%defattr(-,root,root,-)
%config /usr/etc/ryu/ryu.conf

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
