Name:           ius-release
Version:        2
Release:        1%{?dist}
Summary:        IUS repository configuration
License:        MIT
URL:            https://ius.io

Source0:        LICENSE

Source10:       https://repo.ius.io/RPM-GPG-KEY-IUS-6
Source11:       ius-6.repo
Source12:       ius-testing-6.repo
Source13:       ius-archive-6.repo

Source20:       https://repo.ius.io/RPM-GPG-KEY-IUS-7
Source21:       ius-7.repo
Source22:       ius-testing-7.repo
Source23:       ius-archive-7.repo

Source30:	ius-6-x86_64.cfg
Source31:	ius-7-x86_64.cfg

BuildArch:      noarch

%{?el6:Requires: epel-release = 6}
%{?el7:Requires: epel-release = 7}


%description
This package contains the IUS repository GPG key as well as configuration for
yum.


%prep
%setup -q -c -T
install -p -m 0644 %{S:0} .


%install
%if %{defined el6}
install -D -p -m 0644 %{S:10} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-IUS-6
install -D -p -m 0644 %{S:11} %{buildroot}%{_sysconfdir}/yum.repos.d/ius.repo
install -D -p -m 0644 %{S:12} %{buildroot}%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -D -p -m 0644 %{S:13} %{buildroot}%{_sysconfdir}/yum.repos.d/ius-archive.repo
install -Dm0644 %{S:30} %{buildroot}%{_sysconfdir}/mock/ius-6-x86_64.cfg
%endif
%if %{defined el7}
install -D -p -m 0644 %{S:20} %{buildroot}%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-IUS-7
install -D -p -m 0644 %{S:21} %{buildroot}%{_sysconfdir}/yum.repos.d/ius.repo
install -D -p -m 0644 %{S:22} %{buildroot}%{_sysconfdir}/yum.repos.d/ius-testing.repo
install -D -p -m 0644 %{S:23} %{buildroot}%{_sysconfdir}/yum.repos.d/ius-archive.repo
install -Dm0644 %{S:31} %{buildroot}%{_sysconfdir}/mock/ius-7-x86_64.cfg
%endif


%files
%license LICENSE
%{_sysconfdir}/pki/rpm-gpg/RPM-GPG-KEY-IUS-*
%config(noreplace) %{_sysconfdir}/yum.repos.d/ius.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/ius-testing.repo
%config(noreplace) %{_sysconfdir}/yum.repos.d/ius-archive.repo


%package -n ius-mock-cfg
Version:	1
Summary:	IUS configuration file for use with mock
BuildArch:	noarch

Requires:	mock


%description -n	ius-mock-cfg
%{summary}


%files -n ius-mock-cfg
%if %{defined el6}
%config(noreplace) %{_sysconfdir}/mock/ius-6-x86_64.cfg
%endif
%if %{defined el7}
%config(noreplace) %{_sysconfdir}/mock/ius-7-x86_64.cfg
%endif


%changelog
* Wed May 15 2019 evitalis <evitalis@users.noreply.github.com> - 2-2
- Add subpackage for IUS mock configuration

* Wed May 01 2019 Carl George <carl@george.computer> - 2-1
- Switch from IUS mirrorlist service to CDN

* Wed Feb 22 2017 Carl George <carl.george@rackspace.com> - 1.0-15.ius
- Don't preserve permissions in %%prep (see GH#4)

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
