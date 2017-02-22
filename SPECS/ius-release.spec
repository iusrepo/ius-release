Name:               ius-release
Version:            1.0
Release:            14.ius%{?dist}
Summary:            IUS Community Project repository configuration
Group:              System Environment/Base
License:            IUS Community Project End User Agreement
Vendor:             IUS Community Project
URL:                http://dl.iuscommunity.org/pub/ius/
Source0:            IUS-COMMUNITY-GPG-KEY
Source1:            IUS-COMMUNITY-EUA
Source2:            ius.repo.template
Source3:            ius-testing.repo.template
Source4:            ius-dev.repo.template
Source5:            ius-archive.repo.template
Provides:           ius = %{version}
BuildArch:          noarch
%{?el5:BuildRoot:   %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)}
%{?el5:Requires:    epel-release = 5}
%{?el6:Requires:    epel-release = 6}
%{?el7:Requires:    epel-release = 7}


%description
This package contains the IUS Community Project (IUS) repository
GPG key as well as configuration for yum.


%prep
%setup -q -c -T
# copy gpg key and eua to builddir
%{__cp} -p %{SOURCE0} .
%{__cp} -p %{SOURCE1} .
# copy and rename template files to builddir
%{__cp} %{SOURCE2} ius.repo
%{__cp} %{SOURCE3} ius-testing.repo
%{__cp} %{SOURCE4} ius-dev.repo
%{__cp} %{SOURCE5} ius-archive.repo
# %centos is undefined on CentOS 5, must be set in build system
# mock configuration:  config_opts['macros']['%centos'] = '5'
# insert distro and id
%if 0%{?centos}
%{__sed} -i 's_@DISTRO@_CentOS_' *.repo
%{__sed} -i 's_@ID@_centos_' *.repo
%else
%{__sed} -i 's_@DISTRO@_Redhat_' *.repo
%{__sed} -i 's_@ID@_el_' *.repo
%endif
# insert release
%{?el5:%{__sed} -i 's_@RELEASE@_5_' *.repo}
%{?el6:%{__sed} -i 's_@RELEASE@_6_' *.repo}
%{?el7:%{__sed} -i 's_@RELEASE@_7_' *.repo}


%install
%{?el5:%{__rm} -rf %{buildroot}}
%{__install} -Dpm644 IUS-COMMUNITY-GPG-KEY %{buildroot}%{_sysconfdir}/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY
%{__install} -Dpm644 ius.repo         %{buildroot}%{_sysconfdir}/yum.repos.d/ius.repo
%{__install} -Dpm644 ius-testing.repo %{buildroot}%{_sysconfdir}/yum.repos.d/ius-testing.repo
%{__install} -Dpm644 ius-dev.repo     %{buildroot}%{_sysconfdir}/yum.repos.d/ius-dev.repo
%{__install} -Dpm644 ius-archive.repo %{buildroot}%{_sysconfdir}/yum.repos.d/ius-archive.repo


%{?el5:%clean}
%{?el5:%{__rm} -rf %{buildroot}}


%files
%doc IUS-COMMUNITY-EUA
%config(noreplace) %{_sysconfdir}/yum.repos.d/*
%{_sysconfdir}/pki/rpm-gpg/IUS-COMMUNITY-GPG-KEY


%changelog
* Mon Apr 06 2015 Carl George <carl.george@rackspace.com> - 1.0-14.ius
- Switch to new mirrorlist endpoint url
- Switch baseurl (commented out) to https

* Tue Aug 05 2014 Carl George <carl.george@rackspace.com> - 1.0-13.ius
- Don't use $basearch for source repos
- Enable mirrorlist for archive repos

* Mon Jul 14 2014 Carl George <carl.george@rackspace.com> - 1.0-12.ius
- Deprecate el4
- Use conditionals for el5 only sections
- Add support for el7
- Improve use of macros
- Use templates for repo files, and render the template in %%prep

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
