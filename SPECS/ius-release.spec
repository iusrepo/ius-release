
Name:           ius-release       
Version:        1.0 
Release:        10.ius%{?dist}

Summary:        IUS Community Project repository configuration

Group:          System Environment/Base 
License:        IUS Community Project End User Agreement 
Vendor:         IUS Community Project
URL:            http://dl.iuscommunity.org/pub/ius

Source0:        http://dl.iuscommunity.org/pub/ius/IUS-COMMUNITY-GPG-KEY 
Source1:        IUS-COMMUNITY-EUA
Source2:        ius.repo.el4	
Source3:        ius-testing.repo.el4
Source4:        ius.repo.el5
Source5:        ius-testing.repo.el5	
Source6:        ius-dev.repo.el5	
Source7:        ius.repo.el6
Source8:        ius-testing.repo.el6
Source9:        ius-dev.repo.el6	
Source10:       ius-archive.repo.el4
Source11:       ius-archive.repo.el5
Source12:       ius-archive.repo.el6

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Provides:       ius
Requires:       epel-release

%if 0%{?el4}
Requires:       redhat-release >= 4
%endif
%if 0%{?el5}
Requires:       redhat-release >= 5
%endif
%if 0%{?el6}
Requires:       redhat-release >= 6
%endif

%description
This package contains the IUS Community Project (IUS) repository
GPG key as well as configuration for yum%{?el4: and up2date}.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .
install -pm 644 %{SOURCE1} .

%build


%install
rm -rf $RPM_BUILD_ROOT

#GPG Key
install -Dpm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

%if 0%{?el4}
install -pm 644 %{SOURCE2} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE3} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE10} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
%endif
%if 0%{?el5}
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-dev.repo
install -pm 644 %{SOURCE11} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
%endif
%if 0%{?el6}
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE9} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-dev.repo
install -pm 644 %{SOURCE12} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
%endif

%if 0%{?el4}
%post
if [ $1 = 1 ]; then
    RHN_SOURCES=/etc/sysconfig/rhn/sources
    if [ -e ${RHN_SOURCES} ]; then
        if ! grep -q "^#DONT UPDATE %{name}" ${RHN_SOURCES} > /dev/null 2>&1; then
        # remove existing config
        perl -n -i -e 'print if not /^#BEGIN %{name}/ ... /^#END %{name}/' ${RHN_SOURCES}

        # add updated config unless user specifies not to
        echo "#BEGIN %{name}" >> ${RHN_SOURCES}
        echo "# This block is managed by the %{name} RPM." >> ${RHN_SOURCES}
        echo "" >> ${RHN_SOURCES}
        echo "yum IUS http://dl.iuscommunity.org/pub/ius/stable/Redhat/4/\$ARCH" >> ${RHN_SOURCES}
        echo "" >> ${RHN_SOURCES}
        echo "#END %{name}" >> ${RHN_SOURCES}
        fi
    fi
fi
exit 0


%postun 
RHN_SOURCES=/etc/sysconfig/rhn/sources
if [ $1 = 0 ]; then 
 # remove up2date config here
  if [ -e $RHN_SOURCES ]; then
    perl -n -i -e 'print if not /^#BEGIN %{name}/ ... /^#END %{name}/' ${RHN_SOURCES}
  fi
fi
exit 0
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc IUS-COMMUNITY-EUA 
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/*


%changelog
* Tue Feb 14 2012 BJ Dierkes <wdierkes@rackspace.com> - 1.0-10.ius
- Add trailing slash in yum configs to prevent 301 redirects on dMirr.

* Mon Jan 16 2012 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0-9.ius
- Adding a disabled repo for archive, this will help with 
  yum history undo: https://bugs.launchpad.net/ius/+bug/916943

* Mon Jul 11 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0-8.ius
- Setting gpgcheck=1 for all repos
- Adding IUS for EL6

* Fri Nov 26 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0-7.ius
- Rebuild (testing build system)

* Wed Aug 11 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0-6.ius
- No longer require yum-plugin-replace

* Tue Jul 13 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0-5.ius
- Requires: yum-plugin-replace

* Wed Feb 10 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0-4.ius
- Fixed baseurl url's (even though they are commented out
- Added ius-dev.repo

* Tue Jan 05 2010 BJ Dierkes <wdierkes@rackspace.com> - 1.0-3.ius
- Updated for new dMirr host urls, previous urls will continue to work
  for now.

* Wed Sep 02 2009 BJ Dierkes <wdierkes@rackspace.com> - 1.0-2.ius
- Initial Package Build (copied and modified from the epel-release package)
