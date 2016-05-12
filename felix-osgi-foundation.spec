%{?scl:%scl_package felix-osgi-foundation}
%{!?scl:%global pkg_name %{name}}

%{?scl:%thermostat_find_provides_and_requires}

# Prevent brp-java-repack-jars from being run.
%define __jar_repack %{nil}

%global bundle org.osgi.foundation
%global felixdir %{_javadir}/felix
%global POM %{_mavenpomdir}/JPP.felix-%{bundle}.pom

Name:    %{?scl_prefix}felix-osgi-foundation
Version: 1.2.0
Release: 17%{?dist}
Summary: Felix OSGi Foundation EE Bundle

License: ASL 2.0
URL:     http://felix.apache.org
Source0: http://www.apache.org/dist/felix/%{bundle}-%{version}-project.tar.gz

BuildArch: noarch

BuildRequires: java-devel >= 1:1.6.0
BuildRequires: jpackage-utils
BuildRequires: maven-local
BuildRequires: maven-resources-plugin
BuildRequires: maven-plugin-bundle
BuildRequires: felix-parent

%{?scl:Requires: %scl_runtime}

%description
OSGi Foundation Execution Environment (EE) Classes.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
%{?scl:scl enable %{scl} - << "EOF"}
%setup -q -n %{bundle}-%{version}

%mvn_file : felix/%{bundle}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE
%dir %{felixdir}

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Tue Jan 21 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1.2.0-17
- Rebuild in order to fix build root which had broken
  jpackages-tools provides. See RHBZ#1042912.
- Related: RHBZ#1054813

* Wed Nov 27 2013 Elliott Baron <ebaron@redhat.com> - 1.2.0-16
- Properly enable SCL.

* Fri Nov 15 2013 Omair Majid <omajid@redhat.com> - 1.2.0-15
- Find provides and requires automatically

* Fri Nov 8 2013 Omair Majid <omajid@redhat.com> - 1.2.0-15
- SCL-ize package

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
