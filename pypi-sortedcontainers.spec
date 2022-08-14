#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sortedcontainers
Version  : 2.4.0
Release  : 36
URL      : https://files.pythonhosted.org/packages/e8/c4/ba2f8066cceb6f23394729afe52f3bf7adec04bf9ed2c820b39e19299111/sortedcontainers-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/e8/c4/ba2f8066cceb6f23394729afe52f3bf7adec04bf9ed2c820b39e19299111/sortedcontainers-2.4.0.tar.gz
Summary  : Sorted Containers -- Sorted List, Sorted Dict, Sorted Set
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-sortedcontainers-license = %{version}-%{release}
Requires: pypi-sortedcontainers-python = %{version}-%{release}
Requires: pypi-sortedcontainers-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(tox)

%description
========================
        
        `Sorted Containers`_ is an Apache2 licensed `sorted collections library`_,
        written in pure-Python, and fast as C-extensions.
        
        Python's standard library is great until you need a sorted collections
        type. Many will attest that you can get really far without one, but the moment
        you **really need** a sorted list, sorted dict, or sorted set, you're faced
        with a dozen different implementations, most using C-extensions without great
        documentation and benchmarking.
        
        In Python, we can do better. And we can do it in pure-Python!

%package license
Summary: license components for the pypi-sortedcontainers package.
Group: Default

%description license
license components for the pypi-sortedcontainers package.


%package python
Summary: python components for the pypi-sortedcontainers package.
Group: Default
Requires: pypi-sortedcontainers-python3 = %{version}-%{release}

%description python
python components for the pypi-sortedcontainers package.


%package python3
Summary: python3 components for the pypi-sortedcontainers package.
Group: Default
Requires: python3-core
Provides: pypi(sortedcontainers)

%description python3
python3 components for the pypi-sortedcontainers package.


%prep
%setup -q -n sortedcontainers-2.4.0
cd %{_builddir}/sortedcontainers-2.4.0
pushd ..
cp -a sortedcontainers-2.4.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656408371
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}$(python -c "import sys; print(sys.path[-1])") python setup.py test || :
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sortedcontainers
cp %{_builddir}/sortedcontainers-2.4.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sortedcontainers/e79dc019b36c084ccc00738699f7c50030a3a0b6
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sortedcontainers/e79dc019b36c084ccc00738699f7c50030a3a0b6

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
