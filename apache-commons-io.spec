Name:		apache-commons-io
Epoch:		1
Version:	2.22.0
Release:	2
Summary:	Utilities for stream, file, and writer I/O
Group:		Development/Java
License:	ASL 2.0
URL:		https://commons.apache.org/proper/commons-io/
Source0:	https://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz
# Gradle 9.9.1 strictly pins commons-io:commons-io 2.20.0.
# The test fixture jar is not in this archive.
Source1:	https://archive.apache.org/dist/commons/io/source/commons-io-2.20.0-src.tar.gz

BuildArch:	noarch
BuildRequires:	mvn(org.apache.commons:commons-parent:pom::)
# Literal, so the first rpmbuild -bs records them before sysjar is installed.
BuildRequires:	maven
BuildRequires:	java-current-devel
BuildSystem:	maven
BuildOption(install):	--file-name commons-io --link %{name} --alias commons-io:commons-io

%description
Apache Commons IO is a library of utilities to assist with developing
IO functionality. 2.22.0 stays the default jar. Gradle 9.9.1 strictly
pins 2.20.0, so that jar is installed beside it.

%prep
%setup -q -n commons-io-%{version}-src
%setup -q -T -D -a 1 -n commons-io-%{version}-src
find . -name '*.jar' -delete

%build -a
export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/java}"
mkdir -p io220/classes
find commons-io-2.20.0-src/src/main/java -name '*.java' > io220/sources.list
test -s io220/sources.list
"$JAVA_HOME/bin/javac" --release 8 -encoding UTF-8 -Xlint:-options \
	-d io220/classes @io220/sources.list
"$JAVA_HOME/bin/jar" cf io220/commons-io.jar -C io220/classes .
cat > io220/commons-io.pom << 'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0">
  <modelVersion>4.0.0</modelVersion>
  <groupId>commons-io</groupId>
  <artifactId>commons-io</artifactId>
  <version>2.20.0</version>
  <name>Apache Commons IO</name>
  <description>Utilities for stream, file, and writer I/O.</description>
  <url>https://commons.apache.org/proper/commons-io/</url>
  <licenses>
    <license>
      <name>Apache-2.0</name>
      <url>https://www.apache.org/licenses/LICENSE-2.0.txt</url>
    </license>
  </licenses>
</project>
EOF

%install -p
sysjar install --buildroot %{buildroot} \
	--artifact io220/commons-io.pom:io220/commons-io.jar \
	--file-name commons-io-2.20.0 \
	--filelist .mfiles220
# 2.22.0 owns commons-io.sysjar. 2.20.0 keeps a second index file.
/bin/mv %{buildroot}/usr/share/sysjar/index/commons-io/commons-io.sysjar \
	%{buildroot}/usr/share/sysjar/index/commons-io/commons-io-2.20.0.sysjar
sed -i 's|/usr/share/sysjar/index/commons-io/commons-io\.sysjar|/usr/share/sysjar/index/commons-io/commons-io-2.20.0.sysjar|' .mfiles220

%install -a
while IFS= read -r line; do
	grep -qxF -- "$line" .mfiles || printf '%s\n' "$line" >> .mfiles
done < .mfiles220

%check -a
export JAVA_HOME="${JAVA_HOME:-/usr/lib/jvm/java}"
cat > IoSmoke.java << 'EOF'
import org.apache.commons.io.FilenameUtils;
public class IoSmoke {
	public static void main(String[] args) {
		String ext = FilenameUtils.getExtension("pin.txt");
		if (!"txt".equals(ext)) {
			throw new AssertionError(ext);
		}
		System.out.println(args[0] + " " + ext);
	}
}
EOF
"$JAVA_HOME/bin/javac" --release 8 -encoding UTF-8 -Xlint:-options \
	-cp %{buildroot}%{_javadir}/commons-io.jar IoSmoke.java
"$JAVA_HOME/bin/java" -cp "%{buildroot}%{_javadir}/commons-io.jar:." IoSmoke io222_ok | tee check222.log
grep -F -q 'io222_ok txt' check222.log
"$JAVA_HOME/bin/javac" --release 8 -encoding UTF-8 -Xlint:-options \
	-cp %{buildroot}%{_javadir}/commons-io-2.20.0.jar IoSmoke.java
"$JAVA_HOME/bin/java" -cp "%{buildroot}%{_javadir}/commons-io-2.20.0.jar:." IoSmoke io220_ok | tee check220.log
grep -F -q 'io220_ok txt' check220.log

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt
