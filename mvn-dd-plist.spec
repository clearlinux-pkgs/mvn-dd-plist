#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-dd-plist
Version  : 1.20
Release  : 2
URL      : https://github.com/3breadt/dd-plist/archive/dd-plist-1.20.tar.gz
Source0  : https://github.com/3breadt/dd-plist/archive/dd-plist-1.20.tar.gz
Source1  : https://repo.gradle.org/gradle/libs-releases/com/googlecode/plist/dd-plist/1.20/dd-plist-1.20.jar
Source2  : https://repo.gradle.org/gradle/libs-releases/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.jar
Source3  : https://repo.gradle.org/gradle/libs-releases/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.pom
Source4  : https://repo.gradle.org/gradle/libs-releases/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-dd-plist-data = %{version}-%{release}
Requires: mvn-dd-plist-license = %{version}-%{release}
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
# com.dd.plist - A Java library for working with property lists
[![Build Status](https://travis-ci.org/3breadt/dd-plist.svg?branch=master)](https://travis-ci.org/3breadt/dd-plist)

%package data
Summary: data components for the mvn-dd-plist package.
Group: Data

%description data
data components for the mvn-dd-plist package.


%package license
Summary: license components for the mvn-dd-plist package.
Group: Default

%description license
license components for the mvn-dd-plist package.


%prep
%setup -q -n dd-plist-dd-plist-1.20

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-dd-plist
cp LICENSE.txt %{buildroot}/usr/share/package-licenses/mvn-dd-plist/LICENSE.txt
mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.20
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.20/dd-plist-1.20.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.20/dd-plist-1.20.jar
/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.jar
/usr/share/java/.m2/repository/com/googlecode/plist/dd-plist/1.21/dd-plist-1.21.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-dd-plist/LICENSE.txt
