Name:		apache-commons-io
Epoch:		1
Version:	2.22.0
Release:	1
Summary:	Utilities for stream, file, and writer I/O
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-io/
Source0:	https://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(org.apache.commons:commons-parent:pom:)
BuildSystem:	maven
BuildOption(install):	--file-name commons-io --link %{name} --alias commons-io:commons-io

%description
Apache Commons IO is a library of utilities to assist with developing
IO functionality.

%prep
%setup -q -n commons-io-%{version}-src

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
