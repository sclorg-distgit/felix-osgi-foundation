%global pkg_name felix-osgi-foundation
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global bundle org.osgi.foundation
%global felixdir %{_javadir}/felix
%global POM %{_mavenpomdir}/JPP.felix-%{bundle}.pom

Name:    %{?scl_prefix}%{pkg_name}
Version: 1.2.0
Release: 16.10%{?dist}
Summary: Felix OSGi Foundation EE Bundle

License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: %{?scl_prefix_java_common}javapackages-tools
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-plugin-bundle
BuildRequires: maven30-felix-parent

%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{bundle}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x

%mvn_file : felix/%{bundle}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE
%dir %{_mavenpomdir}/felix
%dir %{felixdir}

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 1.2.0-16.10
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.9
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 1.2.0-16.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 1.2.0-16.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.3
- Remove requires on java

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-16.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.2.0-16
- Mass rebuild 2013-12-27

* Thu Sep 19 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-15
- Add missing BR: felix-parent

* Mon Aug 19 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-14
- Migrate away from mvn-rpmbuild (#997448)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-13
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Feb 25 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-12
- Add missing BR: maven-local

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 16 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.2.0-10
- Install LICENSE and NOTICE
- Fix directory permissions
- Remove rpm bug workaround

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Nov 30 2011 Alexander Kurtakov <akurtako@redhat.com> 1.2.0-7
- Build with maven 3.
- Adapt to current guidelines.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Dec 27 2010 Mat Booth <fedora@matbooth.co.uk> - 1.2.0-5
- Update maven plug-in BRs.

* Mon Dec 13 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.2.0-4
- Versionless jars & javadocs
- Fix pom filename (#655800)

* Wed Jun 30 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.0-3
- The javadoc subpackage should have requires on jpackage-utils
- Use the mavenpomdir macro
- Rename the mavenPOM macro to publicPOM

* Tue Jun 29 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.0-2
- Use maven to build the project instead of ant

* Thu Jun 24 2010 Victor G. Vasilyev <victor.vasilyev@sun.com> 1.2.0-1
- Release 1.2.0
