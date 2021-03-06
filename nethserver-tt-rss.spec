
%define name nethserver-tt-rss
%define version 1.1.4
%define release 1
Summary: NethServer integration of tt-rss
Name: %{name}
Version: %{version}
Release: %{release}%{?dist}
License: GNU GPL version 2
URL: http://dev.nethserver.org/projects/nethforge/wiki/%{name} 
Group: Neth/addon
Source: %{name}-%{version}.tar.gz

BuildArchitectures: noarch
BuildRequires: perl
BuildRequires: nethserver-devtools 
BuildRoot: /var/tmp/%{name}-%{version}
Requires: tt-rss >= 1.15.3
Requires: nethserver-httpd, nethserver-mysql, nethserver-rh-php71-php-fpm
Requires: mod_authnz_pam
Requires: rh-php71-php-mbstring, rh-php71-php-mysqlnd, rh-php71-php-opcache, rh-php71-php-process
AutoReqProv: no

%description
NethServer integration of TIny Tiny RSS
Tiny Tiny RSS is a feature rich, web based feed reader

%prep
%setup
%build
perl ./createlinks
%{__mkdir_p} root/var/log/tt-rss_update

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-filelist
%{genfilelist} $RPM_BUILD_ROOT \
  --file /etc/rc.d/init.d/tt-rss 'attr(0755,root,root)' \
  --dir /var/log/tt-rss_update 'attr(0770,apache,apache)' \
  --dir /var/lock/tt-rss 'attr(0775,apache,apache)' \
  > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add tt-rss 2>&1 > /dev/null

%preun
if [ "$1" = 0 ]; then
    # stop tt-rss silently, but only if it's running
    /sbin/service tt-rss stop &>/dev/null
    /sbin/chkconfig --del tt-rss
fi

exit 0

%postun
if [ "$1" != 0 ]; then
	/sbin/service tt-rss restart 2>&1 > /dev/null
fi

exit 0

%changelog
* Sat May 26 2018 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.4-1.ns7
- A domain name could be specified to be relevant to SELF_URL_PATH
- Use $tt-rss{DomainName} or $DomainName in dashboard aplet

* Sun Sep 10 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.2-1.ns7
- Restart httpd service on trusted-network

* Wed Mar 29 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.1-1.ns7
- Template expansion on trusted-network

* Sun Mar 12 2017 Stephane de Labrusse <stephdl@de-labrusse.fr> 1.1.0-4.ns7
- GPL license

* Sat Nov 5 2016 stephane de labrusse <stephdl@de-labrusse.fr> 1.1.0-3.ns7
- creation of apache:apache /var/lock/tt-rss.
- the admin (without the FQDN) can be used.

* Mon Oct 10 2016 stephane de labrusse <stephdl@de-labrusse.fr> 1.1.0-2.ns7
- The default admin user is now admin@yourdomain

* Sat Oct 8 2016 stephane de labrusse <stephdl@de-labrusse.fr> 1.1.0-1.ns7
- New version for NS7, now we authenticate by pam in apache

* Sun May 3 2015 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.0-4.ns6
- disclamer

* Tue Apr 21 2015 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.0-3.ns6
- The event runlevel-adjust is now called in actions

* Sat Mar 7 2015 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.0-2.ns6
- url is present in nethgui

* Sat Mar 7 2015 stephane de labrusse <stephdl@de-labrusse.fr> 1.0.0-1.ns6
- First release to Nethserver
- set 'CHECK_FOR_UPDATES' to 'false'
- sysvinit tt-rss script incorporated

* Thu Feb 6 2014 Daniel Berteaud <daniel@firewall-services.com> 0.2.8-1.sme
- Fix database upgrades

* Mon Jan 20 2014 Daniel Berteaud <daniel@firewall-services.com> 0.2.7-1.sme
- Remove the default Authentication prop (but the default value is still http)

* Wed Dec 18 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.6-1.sme
- Add DETECT_ARTICLE_LANGUAGE, for tt-rss 1.11
- Automatically update database schema when needed

* Wed Jun 12 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.5-1.sme
- Add SMTP_SECURE, for tt-rss 1.8

* Tue May 14 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.4-1.sme
- Support tt-rss 1.7.9

* Sun Mar 24 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.3-1.sme
- update daemon run script to use --daemon argument

* Sat Mar 23 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.2-1.sme
- Add missing SMTP_PORT

* Tue Mar 5 2013 Daniel Berteaud <daniel@firewall-services.com> 0.2.1-1.sme
- Support tt-rss 1.7.1

* Wed Nov 14 2012 Daniel Berteaud <daniel@firewall-services.com> 0.2.0-1.sme
- Support tt-rss 1.6.1

* Tue Apr 24 2012 Daniel Berteaud <daniel@firewall-services.com> 0.1.0-1.sme
- Migrate to GIT

* Fri Nov 25 2011 Daniel Berteaud <daniel@firewall-services.com> 0.1-8.sme
- Define SELF_URL_PATH in config
- Update config version to 23 (1.5.7)

* Mon Jul 25 2011 Daniel Berteaud <daniel@firewall-services.com> 0.1-7.sme
- Configure cache dir (prevent log noise)

* Tue Jun 07 2011 Daniel B. <daniel@firewall-services.com> 0.1-6.sme
- MySQL schema files are not doc files anymore

* Tue May 17 2011 Daniel B. <daniel@firewall-services.com> 0.1-5
- Deny access to the /schema directory

* Wed Jan 26 2011 Daniel B. <daniel@firewall-services.com> 0.1-4
- Add DB_PORT param in config file

* Wed Jan 26 2011 Daniel B. <daniel@firewall-services.com> 0.1-3
- Support tt-rss 1.5.1

* Mon Jan 03 2011 Daniel B. <daniel@firewall-services.com> 0.1-2
- disable cron job, as feeds are updated via the daemon

* Mon Jan 03 2011 Daniel B. <daniel@firewall-services.com> 0.1-1
- initial release


