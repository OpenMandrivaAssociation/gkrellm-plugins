%define _disable_ld_no_undefined 1
%define _disable_lto 1

%define name	gkrellm-plugins
%define version	2.3.10
%define release 	1

%define debug_package %{nil}

%define gkrellweather_version	2.0.8
%define seti_version		0.7.0b
%define gkrellStock_version	0.5.1
%define gkrellShoot_version	0.4.4
%define snmp_version		1.1
%define gkrellmitime_version	1.0
%define volume_version		2.1.13
%define mailwatch_version	2.4.3
%define gkrellmss_version	2.6
%define gkrellmwireless_version	2.0.3
%define radio_version		2.0.4
%define gkrellkam_version	2.0.0
%define fmonitor_version	2.0.4
%define reminder_version	2.0.0
%define gkrellmoon_version	0.6
%define gkleds_version		0.8.0
%define gkrellmbgchg2_version	0.1.9
%define gkrellsun_version	1.0.0
%define hddtemp_version		0.2-beta
%define timers_version		1.3
%define gkrelltop_version	2.2.13
%define gkrellmlaunch_version 0.5
%define cpufreq_version		0.6.1

Name:		%{name}
Summary:	Plugins for gkrellm
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
URL:		http://gkrellm.net
Source2:	gkrellm-volume-%{volume_version}.tar.gz
Source3:	gkrellm-mailwatch-%{mailwatch_version}.tar.gz
Source4:	gkrellmitime-%{gkrellmitime_version}.tar.bz2
Source5:	gkrellstock-%{gkrellStock_version}.tar.bz2
Patch5:		gkrellstock-0.5.1.path.patch.bz2
Source6:	http://prdownloads.sourceforge.net/gkrellshoot/gkrellshoot-%{gkrellShoot_version}.tar.gz
Source7:	http://members.dslextreme.com/~billw/gkrellmss/gkrellmss-%{gkrellmss_version}.tar.gz
Source8:	gkrellmwireless-%{gkrellmwireless_version}.tar.bz2
Source9:	gkrellm-radio-%{radio_version}.tar.bz2
Source10:	gkrellkam_%{gkrellkam_version}.tar.bz2
Source11:	gkrellweather-%{gkrellweather_version}.tgz
Patch4:		gkrellweather-2.0.8-fix-path.patch
Source12:	gkrellm-fmonitor-%{fmonitor_version}.tgz
Source13:	gkrellm-reminder-%{reminder_version}.tar.bz2
Source14:	gkrellmoon-%{gkrellmoon_version}.tar.bz2
Source15:	gkrellm_snmp-%{snmp_version}.tar.gz
Source16:	gkleds-%{gkleds_version}.tar.bz2
Source17:	http://www.bender-suhl.de/stefan/comp/sources/gkrellmbgchg2-%{gkrellmbgchg2_version}.tar.gz
Source18:	http://sourceforge.net/projects/gkrellsun/files/gkrellsun%20gkrellm-2.2/1.0.0/gkrellsun-%{gkrellsun_version}.tar.gz
Source20:	seti-%{seti_version}.tar.bz2
Patch2:		seti-%{seti_version}-gkrellm2.patch.bz2
Source21:	gkrellm-hddtemp-%{hddtemp_version}.tar.bz2
Source22:	gkrellm_timers-%{timers_version}.tar.bz2
Source23:	http://sourceforge.net/projects/gkrelltop/files/gkrelltop/2.2.13/gkrelltop_%{gkrelltop_version}.orig.tar.gz
Source24:	gkrellmlaunch-%{gkrellmlaunch_version}.tar.bz2 
Source25:	gkrellm2-cpufreq-%{cpufreq_version}.tar.gz

Requires:	gkrellm = %{version}
BuildRequires:	gkrellm-devel = %{version}
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(liblircclient0)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	libmcrypt-devel
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  cpupower-devel

%description
This package contains some plugins for gkrellm.  Included are the following
plugins:

  * volume, controls mixer
  * mailwatch, watches individual mailboxes for new mail
  * gkrellmitime, displays internet time
  * gkrellmss, sound scope
  * gkrellmwireless, monitors the link quality of a wirless LAN card
  * gkrellm-radio, radio tuner interface
  * gkrellweather, checks and reports weather conditions
  * fmonitor, displays contents of files
  * reminder, a cron-lick scheduler
  * gkleds, plugin which monitors CapsLock, NumLock, ScrollLock
  * gkrellmbgchg, Change your background on a schedule
  * gkrellsun, Sunrise and Sunset display
  * gkx86info, Calculates Mhz/Ghz of processor
  * gkrellmoon, shows the phases of the moon
  * seti, displays information about your seti progress
  * gkrellm-hddtemp, displays temperatures of hard disks
  * gkrellmlaunch, allows one click access to programs

%package snmp
Summary:	SNMP plugin for %{name}
Group:		Monitoring
Requires:	gkrellm = %{version}
BuildRequires:	net-snmp-devel

%description snmp
gkrellm_snmp, SNMP monitor.

%package stock
Summary:	Stock plugin for %{name}
Group:		Monitoring
Requires:	gkrellm = %{version}

%description stock
gkrellStock, a stock monitor.

%package shoot
Summary:	Shoot plugin for %{name}
Group:		Monitoring
Requires:	gkrellm = %{version}
Requires:	imagemagick

%description shoot
gkrellShoot, a screen locker and screen capture krell.

%package kam
Summary:	Kam plugin for %{name}
Group:		Monitoring
Requires:	gkrellm = %{version}
Requires:	wget

%description kam
gkrellkam, monitor static images such as webcams.

%prep
%setup -T -c -n %{name}
#%setup -q -T -D -c -a 1 -n %{name}
%setup -q -T -D -c -a 2 -n %{name}
%setup -q -T -D -c -a 3 -n %{name}
%setup -q -T -D -c -a 4 -n %{name}
%setup -q -T -D -c -a 5 -n %{name}
%setup -q -T -D -c -a 6 -n %{name}
%setup -q -T -D -c -a 7 -n %{name}
%setup -q -T -D -c -a 8 -n %{name}
%setup -q -T -D -c -a 9 -n %{name}
%setup -q -T -D -c -a 10 -n %{name}
%setup -q -T -D -c -a 11 -n %{name}
%setup -q -T -D -c -a 12 -n %{name}
%setup -q -T -D -c -a 13 -n %{name}
%setup -q -T -D -c -a 14 -n %{name}
%setup -q -T -D -c -a 15 -n %{name}
%setup -q -T -D -c -a 16 -n %{name}
%setup -q -T -D -c -a 17 -n %{name}
%setup -q -T -D -c -a 18 -n %{name}
%setup -q -T -D -c -a 20 -n %{name}
%setup -q -T -D -c -a 21 -n %{name}
%setup -q -T -D -c -a 22 -n %{name}
%setup -q -T -D -c -a 23 -n %{name}
%setup -q -T -D -c -a 24 -n %{name}
%setup -q -T -D -c -a 25 -n %{name}

(cd seti-%{seti_version}
%patch2 -p1 -b .gtk2
)
(cd gkrellweather-%{gkrellweather_version}
%patch4 -p1 -b .path
)
(cd gkrellStock-%{gkrellStock_version}
%patch5 -p0 -b .path
)

sed -i 's/-Wl /-Wl,/' gkrellmitime-%{gkrellmitime_version}/Makefile
sed -i 's/-Wl//' gkrellm-radio/Makefile
sed -i 's/-Wl//' gkrellkam-%{gkrellkam_version}/Makefile
sed -i 's/-Wl//' seti-%{seti_version}/Makefile
sed -i 's/-Wl//' gkrellm-hddtemp-%{hddtemp_version}/Makefile
sed -i 's/-W1//' gkrellmlaunch-%{gkrellmlaunch_version}/Makefile
sed -i 's/lcpufreq/lcpupower/' gkrellm2-cpufreq-%{cpufreq_version}/Makefile

%build
(cd gkrellm-volume
make CFLAGS="%{optflags}"
)
(cd gkrellm-mailwatch
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellmitime-%{gkrellmitime_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellStock-%{gkrellStock_version}
make CFLAGS="%{optflags}"
)
(cd gkrellShoot-%{gkrellShoot_version}
make CFLAGS="%{optflags}"
)
(cd gkrellmss-%{gkrellmss_version}
make without-esd=yes CFLAGS="%{optflags}"
)
(cd gkrellmwireless
make CFLAGS="%{optflags}"
)
(cd gkrellm-radio
make WITH_LIRC=1
)
(cd gkrellkam-%{gkrellkam_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkleds-%{gkleds_version}
%ifarch x86_64
make X11_LIB="-L/usr/X11R6/lib64 -lX11 -lXtst" CFLAGS="%{optflags} -fPIC"
%else
make CFLAGS="%{optflags}"
%endif
)
(cd gkrellmbgchg2-%{gkrellmbgchg2_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellm-fmonitor-%{fmonitor_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellmoon-%{gkrellmoon_version}
make CFLAGS="%{optflags}"
)
(cd gkrellm-reminder-%{reminder_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellm_snmp-%{snmp_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellsun-%{gkrellsun_version}/src20
make CFLAGS="%{optflags}"
)
(cd gkrellweather-%{gkrellweather_version}
make PREFIX=%{_prefix} CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd seti-%{seti_version}
make CFLAGS="%{optflags} -fPIC `pkg-config gtk+-2.0 --cflags`"
)
(cd gkrellm-hddtemp-%{hddtemp_version}
make gkrellm2 CFLAGS="%{optflags} -fPIC"
)
(cd gkrellm_timers-%{timers_version}
make CFLAGS="%{optflags}"
)
( cd gkrelltop-%{gkrelltop_version}.orig
make clean
make CFLAGS="%{optflags}"
)
( cd gkrellmlaunch-%{gkrellmlaunch_version}
make CFLAGS="%{optflags}"
)
(cd gkrellm2-cpufreq-%{cpufreq_version}
make CFLAGS="%{optflags}"
)

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_libdir}/gkrellm2/plugins
mkdir -p %{buildroot}%{_datadir}/gkrellm2/scripts
install -c -s -m 755 gkrellm-volume/volume.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellm-mailwatch/mailwatch.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellmitime-%{gkrellmitime_version}/gkrellm_itime.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellStock-%{gkrellStock_version}/gkrellstock.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -m 755 gkrellStock-%{gkrellStock_version}/GetQuote2 %{buildroot}%{_datadir}/gkrellm2/scripts
install -c -s -m 755 gkrellShoot-%{gkrellShoot_version}/gkrellshoot.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellmss-%{gkrellmss_version}/src/gkrellmss.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellmwireless/wireless.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellm-radio/radio.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellkam-%{gkrellkam_version}/gkrellkam2.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellweather-%{gkrellweather_version}/gkrellweather.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -m 755 gkrellweather-%{gkrellweather_version}/GrabWeather %{buildroot}%{_datadir}/gkrellm2/scripts
install -c -s -m 755 gkrellm-fmonitor-%{fmonitor_version}/fmonitor.so  %{buildroot}%{_libdir}/gkrellm2/plugins
#install -c -s -m 755 gkrellm-fmonitor-%{fmonitor_version}/sensors.tcl %{buildroot}%{_bindir}
install -c -s -m 755 gkrellm-reminder-%{reminder_version}/reminder.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellm_snmp-%{snmp_version}/gkrellm_snmp.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkleds-%{gkleds_version}/gkleds.so  %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellmbgchg2-%{gkrellmbgchg2_version}/gkrellmbgchg.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellsun-%{gkrellsun_version}/src20/gkrellsun.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellmoon-%{gkrellmoon_version}/gkrellmoon.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 seti-%{seti_version}/seti.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellm-hddtemp-%{hddtemp_version}/gkrellm-hddtemp.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellm_timers-%{timers_version}/gkrellm_timers.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrelltop-%{gkrelltop_version}.orig/gkrelltop{,d}.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellmlaunch-%{gkrellmlaunch_version}/gkrellmlaunch.so %{buildroot}%{_libdir}/gkrellm2/plugins
install -c -s -m 755 gkrellm2-cpufreq-%{cpufreq_version}/cpufreq.so %{buildroot}%{_libdir}/gkrellm2/plugins

# setup various docs
mkdir -p doc/gkleds
cp gkleds-%{gkleds_version}/{COPYING,Changelog,License,README,TODO,Themes} doc/gkleds
mkdir -p doc/gkrellm-fmonitor
cp gkrellm-fmonitor-%{fmonitor_version}/README doc/gkrellm-fmonitor
mkdir -p doc/gkrellm-hddtemp
cp gkrellm-hddtemp-%{hddtemp_version}/{COPYING,README} doc/gkrellm-hddtemp
mkdir -p doc/gkrellm-mailwatch
cp gkrellm-mailwatch/{Changelog,README} doc/gkrellm-mailwatch
mkdir -p doc/gkrellm-radio
cp gkrellm-radio/{CHANGES,README,lirc.example} doc/gkrellm-radio
mkdir -p doc/gkrellm-reminder
cp gkrellm-reminder-%{reminder_version}/{COPYING,ChangeLog,INSTALL,README} doc/gkrellm-reminder
mkdir -p doc/gkrellm-volume
cp gkrellm-volume/{COPYRIGHT,Changelog,README,THEMING} doc/gkrellm-volume
mkdir -p doc/timers
cp gkrellm_timers-%{timers_version}/{ChangeLog,README,TODO} doc/timers
mkdir -p doc/gkrellmbgchg2
cp gkrellmbgchg2-%{gkrellmbgchg2_version}/{ChangeLog,README,TODO} doc/gkrellmbgchg2
mkdir -p doc/gkrellmitime
cp gkrellmitime-%{gkrellmitime_version}/{COPYING,ChangeLog,README} doc/gkrellmitime
mkdir -p doc/gkrellmlaunch
cp gkrellmlaunch-%{gkrellmlaunch_version}/{CHANGELOG,COPYING,LICENSE,README} doc/gkrellmlaunch
mkdir -p doc/gkrellmoon
cp gkrellmoon-%{gkrellmoon_version}/{AUTHORS,COPYING,ChangeLog,INSTALL,NEWS,README} doc/gkrellmoon
mkdir -p doc/gkrellmss
cp gkrellmss-%{gkrellmss_version}/{COPYRIGHT,Changelog,INSTALL,README,Themes} doc/gkrellmss
mkdir -p doc/gkrellmwireless
cp gkrellmwireless/{Changelog,README} doc/gkrellmwireless
mkdir -p doc/gkrellsun
cp gkrellsun-%{gkrellsun_version}/{AUTHORS,COPYING,INSTALL,README} doc/gkrellsun
mkdir -p doc/gkrelltop
cp gkrelltop-%{gkrelltop_version}.orig/README doc/gkrelltop
mkdir -p doc/gkrellweather
cp gkrellweather-%{gkrellweather_version}/{COPYING,ChangeLog,README} doc/gkrellweather
mkdir -p doc/seti
cp seti-%{seti_version}/{AUTHORS,BUGS,COPYING,ChangeLog,INSTALL,INSTALL.gtk2,LICENSE,NEWS,README,README-pcpu,TODO} doc/seti
mkdir -p doc/cpufreq
cp gkrellm2-cpufreq-%{cpufreq_version}/{ChangeLog,LICENSE,README} doc/cpufreq

# fix some perms
chmod 644 doc/gkrellmoon/*
chmod 644 doc/gkleds/*
chmod 644 doc/gkrelltop/*

%clean
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc doc/*
%{_libdir}/gkrellm2/plugins/*
%exclude %{_libdir}/gkrellm2/plugins/gkrellm_snmp.so
%exclude %{_libdir}/gkrellm2/plugins/gkrellstock.so
%exclude %{_libdir}/gkrellm2/plugins/gkrellshoot.so
%exclude %{_libdir}/gkrellm2/plugins/gkrellkam2.so
%{_datadir}/gkrellm2/scripts/GrabWeather

%files snmp
%defattr(-,root,root)
%doc gkrellm_snmp-%{snmp_version}/ChangeLog
%doc gkrellm_snmp-%{snmp_version}/FAQ
%doc gkrellm_snmp-%{snmp_version}/README
%doc gkrellm_snmp-%{snmp_version}/TODO
%{_libdir}/gkrellm2/plugins/gkrellm_snmp.so

%files stock
%defattr(-,root,root)
%doc gkrellStock-%{gkrellStock_version}/COPYING
%doc gkrellStock-%{gkrellStock_version}/ChangeLog
%doc gkrellStock-%{gkrellStock_version}/README
%{_libdir}/gkrellm2/plugins/gkrellstock.so
%{_datadir}/gkrellm2/scripts/GetQuote2

%files shoot
%defattr(-,root,root)
%doc gkrellShoot-%{gkrellShoot_version}/ChangeLog
%doc gkrellShoot-%{gkrellShoot_version}/README
%{_libdir}/gkrellm2/plugins/gkrellshoot.so

%files kam
%defattr(-,root,root)
%doc gkrellkam-%{gkrellkam_version}/README
%doc gkrellkam-%{gkrellkam_version}/COPYING
%doc gkrellkam-%{gkrellkam_version}/Changelog
%doc gkrellkam-%{gkrellkam_version}/INSTALL
%doc gkrellkam-%{gkrellkam_version}/Release
%doc gkrellkam-%{gkrellkam_version}/Todo
%doc gkrellkam-%{gkrellkam_version}/example.list
%{_libdir}/gkrellm2/plugins/gkrellkam2.so


%changelog
* Mon Jul 18 2011 Oden Eriksson <oeriksson@mandriva.com> 2.3.5-2mdv2011
+ Revision: 690291
- rebuilt against new net-snmp libs

* Tue Oct 12 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.5-1mdv2011.0
+ Revision: 585213
- rebuild for latest gkrellm

* Sun Jul 18 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.4-4mdv2011.0
+ Revision: 554861
- fix compilation on x86_64, and ensure proper CFLAGS use
- update fmonitor plugin to 2.0.4
- update mailwatch plugin to 2.4.3
- update snmp plugin to 1.1
- update bgchg2 plugin to 0.1.9
- update mms plugin to 2.1.22
- update mss plugin to 2.6
- update sun plugin to 1.0.0
- update top plugin to 2.2.13
- update weather plugin to 2.0.8
- drop i86-specific gkx86info plugin
- add cpufreq plugin
- update volume plugin version to 2.1.13 (#60229)

* Fri Apr 23 2010 Funda Wang <fwang@mandriva.org> 2.3.4-3mdv2010.1
+ Revision: 538092
- rebuild for openssl

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.4-2mdv2010.1
+ Revision: 488716
- rebuild for missing binaries

* Wed Jan 06 2010 Frederik Himpe <fhimpe@mandriva.org> 2.3.4-1mdv2010.1
+ Revision: 486903
- update to new version 2.3.4

* Wed Dec 30 2009 Frederik Himpe <fhimpe@mandriva.org> 2.3.3-1mdv2010.1
+ Revision: 484042
- Rebuild for new gkrellm 2.3.3

* Thu Oct 15 2009 Oden Eriksson <oeriksson@mandriva.com> 2.3.2-3mdv2010.0
+ Revision: 457689
- rebuild
- lowercase ImageMagick

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Oct 11 2008 Frederik Himpe <fhimpe@mandriva.org> 2.3.2-1mdv2009.1
+ Revision: 291685
- Update for new gkrellm 2.3.2 version

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 2.3.1-3mdv2009.0
+ Revision: 246163
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Dec 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.1-1mdv2008.1
+ Revision: 118058
- update to new version 2.3.1

* Thu Aug 16 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.0-3mdv2008.0
+ Revision: 64656
- updates:
- gkrellshoot 0.4.4
- gkrelltop 2.2.10

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt against latest net-snmp-devel

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.3.0-1mdv2008.0
+ Revision: 56013
- new version

* Sun May 13 2007 Michael Scherer <misc@mandriva.org> 2.2.10-1mdv2008.0
+ Revision: 26570
- rebuild for gkrellm 2.2.10
- Import gkrellm-plugins



* Fri Jun 30 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.9-3mdv2007.0
- buildrequires libxtst-devel

* Wed Jun 21 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.9-2mdv2007.0
- gkrellm_snmp 1.0

* Mon Apr 03 2006 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.9-1mdk
- rebuild for new gkrellm

* Tue Jan 10 2006 Oden Eriksson <oeriksson@mandriva.com> 2.2.7-6mdk
- rebuilt against new snmp-libs with new major (10)

* Wed Dec 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-5mdk
- %%mkrel

* Thu Sep 01 2005 Michael Scherer <misc@mandriva.org> 2.2.7-4mdk
- Rebuild without glitz deps

* Mon Aug 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-3mdk
- really fix helper scripts path 

* Mon Aug 22 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-2mdk
- gkrellweather 2.0.7 
- fix helper script path 
- mv all helper scripts to %%{_datadir}/gkrellm2, no need to have them in %%{_bindir}
- drop fetcho (unknown origin)

* Tue Jun 21 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.7-1mdk 
- rebuild against gkrellm 2.2.7
- gkrellsun 1.0.6
- fix build with gcc4

* Tue Apr 26 2005 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.5-1mdk 
- rebuild against gkrellm 2.2.5
- GkrellMBgChg2 0.1.4

* Mon Jan 17 2005 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.4-3mdk 
- GkrellMBgChg2 0.1.2
- gkrelltop 2.2.6
- GKrellShoot 0.4.2
- GKrellMMS 2.1.21

* Sat Jan 08 2005 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.4-2mdk
- buildrequires gtk+1.2-devel for gkrellmms (altough xmms-devel should maybe requires it instead?) 
- fix x86_64 build

* Tue Nov 09 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.4-1mdk 
- new version

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.2-1mdk
- new version

* Fri Jun 11 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.2.1-1mdk 
- new version

* Sat May 08 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.28-3mdk
- gkrellmms 2.1.19

* Fri Apr 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.28-2mdk
- gkrellmbgchg2 0.1.0
- gkrellmms 2.1.17

* Tue Apr 06 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.28-1mdk
- rebuild against gkrellm 2.1.28

* Wed Feb 25 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.25-2mdk
- gkrellm-mss -> 2.4
- gkrellm-mms -> 2.1.14
- gkrellm-sun -> 0.10.4
- drop patch 3, use PREFIX instead

* Fri Jan 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.25-1mdk
- rebuild against gkrellm 2.1.25
- timers 1.3

* Mon Jan 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.24-3mdk
- gkrellm_snmp 0.21
- drop patches 1 and 4

* Mon Jan 12 2004 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.24-2mdk
- build gkrellm_snmp againsnt libnet-smp (Luca Berra <bluca@comedia.it>)
- fix gkrellmitime build

* Sun Dec 28 2003 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.24-1mdk
- rebuild against gkrellm 2.1.24

* Thu Dec 18 2003 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.22-1mdk
- rebuild against gkrellm 2.1.22

* Fri Dec 12 2003 Guillaume Rousse <guillomovitch@mandrake.org> 2.1.21-2mdk
- patch for gkrellmweather path problem
- gkrellm-mms -> 2.1.13
- gkrellm-wireless -> 2.0.3
- gkrellm-mms subpackage
- included missing doc files
- spec cleanup

* Tue Nov 18 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.1.21-1mdk
- rebuild against gkrellm 2.1.21
- gkrellm-radio -> 2.0.4
- gkrellm-volume -> 2.1.9
- gkrellm-fmonitor -> 2.0.3
- gkrellmbgchg -> 2.0.8
- fixed buildrequires

* Sat Aug 30 2003 Michael Scherer <scherer.michael@free.fr> 2.1.16-2mdk
- BuildRequires libopenssl-devel, for snmp plugin

* Sat Aug 23 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.1.16-1mdk
- rebuild against gkrellm 2.1.16

* Sat Aug 09 2003 Michael Scherer <scherer.michael@free.fr> 2.1.15-2mdk
- + gkrellmlaunch ( 0.5 )
 
* Thu Aug 07 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.1.15-1mdk
- rebuild against gkrellm 2.1.15
- no buildrequires libgtk1.2-devel

* Mon Jun 30 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.1.14-1mdk
- rebuild against gkrellm 2.1.14
- gkrellweather -> 2.0.6
- gkrellstock -> 0.5.1
- gkrellm-volume -> 2.1.8
- gkrellmms -> 2.1.12
- gkrellm-mailwatch -> 2.4.2
- gkrelltop -> 2.2
- used macros for specific plugins versions

* Thu Jun 19 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.1.12-2mdk
- split up some subpackages to leverage depndencies
- spec cleanup

* Tue Jun 17 2003 Guillaume Rousse <guillomovitch@linux-mandrake.com> 2.1.12-1mdk
- rebuild against gkrellm 2.1.12

* Thu May 01 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.1.7a-4mdk
- buildrequires (stefan spam ;)
- distlint error

* Sat Apr 12 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.1.7a-3mdk
- gkrellmms -> 2.1.9
- gkrellm-mailwatch -> 2.3.1
- gkrellm-radio -> 2.0.3
- + gkrellm_timers (1.2)
- + gkrelltop (2.1)

* Sat Feb 08 2003 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.1.7a-2mdk
- %%ix86 sucks, gkx86info does not exist on ppc/alpha/sparc

* Thu Jan 30 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.1.7a-1mdk
- rebuild against gkrellm 2.1.7a

* Fri Jan 24 2003 Vincent Danen <vdanen@mandrakesoft.com> 2.1.5-2mdk
- changes from Ben Reser:
  - Lots of new goodies:
    gkrellweather 2.0.5
    fmonitor 2.0.2
    reminder 2.0.0
    gkrellm_snmp 0.18 (patched for gkrellm2)
    gkleds 0.8.0
    bkrellmbgchg2 0.0.4
    gkrellsun 0.9.1
    gkx86info 0.0.2
    gkrellmoon 0.6
  - Removed uneeded ppc pmud requires since there is
    no pmud plugin for gkrellm2 :(
  - Updated gkrellmss to 2.3 and re-enabled it now that fftw is
    in contrib
  - Updated gkrellmvolume & gkrellmms to 2.1.7
  - Cleanup so package no longer uses /usr/X11R6

* Tue Jan 14 2003 Frederic Crozat <fcrozat@mandrakesoft.com> 2.1.5-1mdk
- Recompiled against gkrellm 2.1.5
- Remove old prefix, since main package don't use it anymore
- gkrellmms 2.1.6
- gkrellm-volume 2.1.6
- gkrellm-mailwatch 2.1
- gkrellmss 2.3
- gkrellmwireless 2.0.2
- gkrellm-radio 2.0.2

* Tue Oct 29 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 2.0.4-2mdk
- Add gkrellkam2 2.0.0
- Fix build for gkrellmitime
- Remove obsolete build lines for gkrellm-gnome
- Fix dependencies

* Wed Oct 16 2002 Vincent Danen <vdanen@mandrakesoft.com> 2.0.4-1mdk
- gkrellm-volume 2.1.4
- gkrellmms 2.1.2
- gkrellm-mailwatch 2.0
- gkrellmwireless 2.0.0
- gkrellm-radio 2.0.1
- gkrellmitime 1.0
- gkrellstock 0.5
- gkrellshoot 0.4.1
- gkrellmss 2.0 (disabled currently)
- remove all 1.x plugins not ported to 2.x

* Thu Oct 03 2002 Antoine Ginies <aginies@mandrakesoft.com> 1.2.13-2mdk
- gkleds 0.6.1

* Sat Aug 10 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.2.13-1mdk
- rebuild for 1.2.13
- gkrellkam-0.3.4
- gkrellm-radio-0.3.3
- Requires: wget (for gkrellkam)
- more macros
- BuildRequires: liblirc-devel

* Mon May 06 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.2.11-1mdk
- rebuild for 1.2.11
- gkrellmms 0.5.6
- new gktaskman-0.0.7
- new gkrelmwireless-0.2.2

* Thu Jan 31 2002 Vincent Danen <vdanen@mandrakesoft.com> 1.2.8-1mdk
- rebuild for 1.2.8
- Requires: gnome-libs-devel
- Requires: s/ucd-snmp-devel/libsnmp-devel/

* Wed Nov 21 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.4-1mdk
- rebuild for 1.2.4 by Ryan T. Sammartino <ryants@shaw.ca>

* Sun Sep 30 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.2.2-1mdk
- rebuild for 1.2.2
- need to define IMLIB_INCLUDE and GTK_INCLUDE in spec so can use
  optimization for all krells
- updated mailwatch to 0.7
- lots of new goodies:
  - fmonitor 0.3
  - gkrellmitime 0.4
  - gkrellscore 0.0.2
  - glogwatch 1.0
  - gkrellstock 0.2 
  - gkrellshoot 0.2
  - gkrinn 0.5-1
  - gkrellmwho 0.4
  - reminder 0.3.1
  - gkrellmoon 0.3
  - gkrellm_snmp 0.18
  - gkrellmss 0.2

* Wed Aug  9 2001 Stew Benedict <sbenedict@mandrakesoft.com> 1.2.1-1mdk
- rebuild for 1.2.1 - move plugins to /usr/lib/gkrellm per FHS
- add gkrellm-pmu, gkrellm-gnome (marc heckmann)

* Mon Jul 16 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.0.8-1mdk
- rebuild for 1.0.8
- updated plugins

* Wed Mar 14 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.7-1mdk
- rebuild for 1.0.7

* Wed Jan 31 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.6-1mdk
- rebuild for 1.0.6

* Tue Jan 23 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.5-1mdk
- rebuild for 1.0.5

* Tue Jan 16 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.4-1mdk
- rebuild for 1.0.4
- plugin_fan compiles again so it's back in

* Sun Jan 07 2001 Vincent Danen <vdanen@mandrakesoft.com> 1.0.3-1mdk
- rebuild for 1.0.3
- remove the plugin_fan plugin...  doesn't look like it's supported anymore
  and it won't build anymore either

* Wed Nov 15 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.2-1mdk
- build for 1.0.2
- rename primary sourcefile so it has no version (silly to keep changing
  it for every new version since the plugins don't change)

* Fri Oct 20 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.1-1mdk
- build for 1.0.1

* Fri Oct 13 2000 Vincent Danen <vdanen@mandrakesoft.com> 1.0.0-1mdk
- build for 1.0.0

* Mon Aug  7 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.10.5-1mdk
- build for 0.10.5
- added stricter version checking for dependencies

* Wed Jul 12 2000 Vincent Danen <vdanen@mandrakesoft.com> 0.10.4-1mdk
- new package for gkrellm plugins
- gkrellmms 0.5.4
- add gkrellweather 0.2.3
- add volume 0.6
- add mailwatch 0.2
- added slim fetcho email fetching client
- remove seti@home since it never compiles properly
