Name:          libphonenumber
# Newer release require com.google.protobuf.nano available only on protobuf >= 3.0.0-alpha-1 
Version:       8.10.7
Release:       1%{?dist}
Summary:       Library to handle international phone numbers
# BSD:  cpp/src/phonenumbers/base/*
# tools/cpp/src/base/*
# MIT: cpp/src/phonenumbers/utf/rune.c
# cpp/src/phonenumbers/utf/utf.h
# cpp/src/phonenumbers/utf/utfdef.h
License:       ASL 2.0 and BSD and MIT
URL:           https://github.com/googlei18n/libphonenumber/
Source0:       https://github.com/google/libphonenumber/archive/v%{version}/%{name}-v%{version}.tar.gz

Requires: boost-thread
BuildRequires: boost-thread
BuildRequires: boost-devel
BuildRequires: cmake
BuildRequires: gtest-devel
BuildRequires: libicu-devel
BuildRequires: protobuf-compiler
BuildRequires: protobuf-devel
BuildRequires: re2-devel

%description
Google's common C++ library for parsing, formatting,
storing and validating international phone numbers.
Optimized for running on  smart-phones.

This library is a C++ port of the Java version.

%package devel
Summary:       Development files for %{name}
Requires:      %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package carrier
Summary:       Java library to handle international phone numbers
BuildArch:     noarch

%description carrier
A phone prefix mapper which provides carrier
information related to a phone number.

%package common-build
Summary:       Libphonenumber common library for build tools
BuildArch:     noarch

%description common-build
Libphonenumber common Java library for build tools.

%package cpp-build
Summary:       Java Libphonenumber C++ build tools
BuildArch:     noarch

%description cpp-build
C++ build tools that download dependencies under base/
from the Chromium source repository, and
generate the C++ meta-data code needed to build the
libphonenumber library.

%package data-tools
Summary:       Libphonenumber Java Data tools
BuildArch:     noarch

%description data-tools
Libphonenumber Java Data tools.

%package geocoder
Summary:       Java library to handle international phone numbers
BuildArch:     noarch

%description geocoder
An offline geocoder which provides geographical information
related to a phone number.

%package java
Summary:       Java library to handle international phone numbers
BuildArch:     noarch

%description java
Google's common Java library for parsing, formatting,
storing and validating international phone numbers.
Optimized for running on  smart-phones.

%package java-build
Summary:       Libphonenumber Java and JavaScript build tools
BuildArch:     noarch

%description java-build
Java and JavaScript build tools that generate the
Java and JavaScript meta-data code needed to
build the libphonenumber library. The Java build tools
also transform the geocoding data from text to binary format.

%package parent
Summary:       Parent POM for %{name}
BuildArch:     noarch

%description parent
Parent POM for %{name}.

%package build-parent
Summary:       Top Parent POM for %{name}
BuildArch:     noarch

%description build-parent
Top Parent POM for %{name}.

%package prefixmapper
Summary:       Java library to handle international phone numbers
BuildArch:     noarch

%description prefixmapper
Utilities to handle the phone prefix mappers to use.

%package tools
Summary:       Libphonenumber build tools Parent POM
BuildArch:     noarch

%description tools
Libphonenumber build tools Parent POM.

%package javadoc
Summary:       Javadoc for %{name}
BuildArch:     noarch

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{name}-%{version}
find -name "*.class" -delete
find -name "*.jar" -print -delete
rm -rf javadoc debian


# Disable classpath in manifest file
#%pom_xpath_set "pom:addClasspath" false tools/java/cpp-build

#%pom_change_dep -r :servlet-api :javax.servlet-api:3.1.0

#%pom_disable_module demo java


# TODO JavaScript library. Skip for now, use unavailable build tools: closure-library, closure-linter

%build

#%mvn_build -s

mkdir -p cpp/build
cd cpp/build 
%{cmake} ..
%{make_build} -j 1 phonenumber phonenumber-shared

%install
make install DESTDIR=%{buildroot} -C cpp/build
find %{buildroot} -name '*.a' -delete
find %{buildroot} -name '*.la' -delete

%check
cd cpp/build 
%{cmake} ..
%{make_build} libphonenumber_test
./libphonenumber_test

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libgeocoding.so.*
%{_libdir}/libphonenumber.so.*
%license cpp/LICENSE
%doc cpp/README

%files devel
%dir %{_includedir}/phonenumbers
%dir %{_includedir}/phonenumbers/base
%dir %{_includedir}/phonenumbers/base/memory
%dir %{_includedir}/phonenumbers/base/synchronization
%dir %{_includedir}/phonenumbers/geocoding
%dir %{_includedir}/phonenumbers/utf
%{_includedir}/phonenumbers/*.h
%{_includedir}/phonenumbers/base/*.h
%{_includedir}/phonenumbers/base/memory/*.h
%{_includedir}/phonenumbers/base/synchronization/*.h
%{_includedir}/phonenumbers/geocoding/*.h
%{_includedir}/phonenumbers/utf/*.h
%{_libdir}/libgeocoding.so
%{_libdir}/libphonenumber.so

%changelog
* Sat Nov 07 2015 gil cattaneo <puntogil@libero.it> 7.1.1-1
- update to 7.1.1

* Sat Aug 29 2015 gil cattaneo <puntogil@libero.it> 7.0.9-1
- update to 7.0.9

* Wed Jul 15 2015 gil cattaneo <puntogil@libero.it> 7.0.8-1
- update to 7.0.8

* Tue Apr 28 2015 gil cattaneo <puntogil@libero.it> 7.0.5-1
- update to 7.0.5

* Mon Mar 09 2015 gil cattaneo <puntogil@libero.it> 7.0.3-1
- initial rpm

