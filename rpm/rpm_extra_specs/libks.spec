%global commit0      68069c3e404d6d0b2d8c00eca57bcd7c8c02a742
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: libks
Version: 1.8.4
Release: 0
Summary: Foundational support for signalwire C products 
Group: System/Libraries
License: MIT
Url: https://github.com/signalwire/libks
Source0: https://github.com/sergey-safarov/libks/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz
BuildRequires: cmake ninja-build gcc-c++ ninja-build libatomic
BuildRequires: pkgconfig(uuid) pkgconfig(openssl)

%description
Foundational support for signalwire C products

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version

%description devel
Development files for %name

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%{cmake} -D KS_PLAT_LIN=true \
	-D CENTOS_FOUND=true \
	-G Ninja \
	-D CMAKE_BUILD_TYPE=Release .
%{cmake_build} -j 1

%install
%{cmake_install}
find %{buildroot} -name '*.a' -delete


%files -n %name
%_libdir/libks.so.*

%files devel
%doc %_docdir/libks/copyright
%_includedir/libks
%_libdir/pkgconfig/libks.pc
%_libdir/libks.so

%changelog
* Tue Feb 28 2023 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.0 -> 1.8.2

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.7.0 -> 1.8.0

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- first build for ALT
