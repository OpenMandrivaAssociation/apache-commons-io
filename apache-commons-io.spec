%{?_javapackages_macros:%_javapackages_macros}
%global base_name       io
%global short_name      commons-%{base_name}

Name:           apache-%{short_name}
Version:        2.4
Release:        10.1%{?dist}
Epoch:          1
Summary:        Utilities to assist with developing IO functionality
License:        ASL 2.0
URL:            http://commons.apache.org/%{base_name}
Source0:        http://archive.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
BuildArch:      noarch

BuildRequires:  java-devel >= 1:1.6
BuildRequires:  maven-local
BuildRequires:  apache-commons-parent

Provides:       jakarta-%{short_name} = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name} < %{epoch}:%{version}-%{release}

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%package javadoc
Summary:        API documentation for %{name}
Provides:       jakarta-%{short_name}-javadoc = %{epoch}:%{version}-%{release}
Obsoletes:      jakarta-%{short_name}-javadoc < %{epoch}:%{version}-%{release}

%description javadoc
This package provides %{summary}.

%prep
%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' *.txt

%build
%mvn_file  : %{short_name} %{name}
%mvn_alias : org.apache.commons:
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Apr 22 2013 Michal Srb <msrb@redhat.com> - 1:2.4-9
- Rebuild

* Mon Apr 15 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-8
- Update to current packaging guidelines

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1:2.4-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jan  9 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-5
- Bump release tag

* Tue Jan  8 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-4
- Build with xmvn

* Mon Nov 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-3
- Add Provides/Obsoletes for jakarta-commons-io

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Jun 19 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.4-1
- Updae to 2.4

* Mon Apr 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.3-1
- Update to 2.3

* Wed Apr 4 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1:2.2-1
- Update to 2.2
- Remove rpm bug workaround
- Finalize renaming from jakarta-comons-io

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 7 2011 Alexander Kurtakov <akurtako@redhat.com> 1:2.1-1
- Update to latest upstream (2.1).

* Thu Jun 23 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.0.1-3
- Fix build with maven3
- Use new add_maven_depmap macro

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:2.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:2.0.1-1
- Update to 2.0.1
- Versionless jars & javadocs
- Use maven 3 to build
- Use apache-commons-parent for BR

* Fri Oct 22 2010 Chris Spike <chris.spike@arcor.de> 1:2.0-1
- Updated to 2.0
- Cleaned up BRs

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-6
- Add license to javadoc subpackage

* Fri May 21 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-5
- Correct depmap filename for backward compatibility

* Mon May 17 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-4
- Fix maven depmap JPP name to short_name

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-3
- Add obsoletes to javadoc sub-package

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-2
- Add symlink to short_name.jar
- Fix mavendepmapfragdir wildcard

* Tue May 11 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1:1.4-1
- Rename and rebase of jakarta-commons-io
- Clean up whole spec
