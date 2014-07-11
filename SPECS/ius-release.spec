
Name:           ius-release       
Version:        1.0
Release:        11.ius%{?dist}

Summary:        IUS Community Project repository configuration

Group:          System Environment/Base 
License:        IUS Community Project End User Agreement 
Vendor:         IUS Community Project
URL:            http://dl.iuscommunity.org/pub/ius

Source0:        http://dl.iuscommunity.org/pub/ius/IUS-COMMUNITY-GPG-KEY
Source1:        http://dl.iuscommunity.org/pub/ius/IUS-COMMUNITY-EUA
Source4:        ius.repo.el5
Source5:        ius-testing.repo.el5
Source6:        ius-dev.repo.el5
Source7:        ius.repo.el6
Source8:        ius-testing.repo.el6
Source9:        ius-dev.repo.el6
Source11:       ius-archive.repo.el5
Source12:       ius-archive.repo.el6

Source13:       ius.repo.centos5
Source14:       ius.repo.centos6
Source15:       ius-testing.repo.centos5
Source16:       ius-testing.repo.centos6
Source17:       ius-dev.repo.centos5	
Source18:       ius-dev.repo.centos6	
Source19:       ius-archive.repo.centos5
Source20:       ius-archive.repo.centos6

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
Provides:       ius = %{version}

%if 0%{?el5}
Requires:       epel-release = 5
%endif
%if 0%{?el6}
Requires:       epel-release = 6
%endif


%description
This package contains the IUS Community Project (IUS) repository
GPG key as well as configuration for yum.


%prep
%setup -q -c -T
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

%if 0%{?el5}
if [ %{?dist} == .centos5 ] # hacky...
then
install -pm 644 %{SOURCE13} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE15} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE17} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-dev.repo
install -pm 644 %{SOURCE19} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
else
install -pm 644 %{SOURCE4} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE5} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE6} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-dev.repo
install -pm 644 %{SOURCE11} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
fi
%endif

%if 0%{?el6}
%if 0%{?centos} == 6
install -pm 644 %{SOURCE14} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE16} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE18} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-dev.repo
install -pm 644 %{SOURCE20} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
%else
install -pm 644 %{SOURCE7} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius.repo
install -pm 644 %{SOURCE8} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -pm 644 %{SOURCE9} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-dev.repo
install -pm 644 %{SOURCE12} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/ius-archive.repo
%endif
%endif


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc IUS-COMMUNITY-EUA 
%config(noreplace) /etc/yum.repos.d/*
/etc/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY


%changelog
* Mon Mar 25 2013 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.0-11.ius
- Adding repo files for CentOS
- Adding checks to place repo files for CentOS

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
