%define name	gkrellm-plugins
%define version	2.3.4
%define release	%mkrel 4

%define gkrellmms_version	2.1.22
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
Source1:	http://gkrellm.luon.net/files/gkrellmms-%{gkrellmms_version}.tar.gz
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
BuildRequires:	libgtk+2.0-devel
BuildRequires:	liblirc-devel
BuildRequires:	libfftw-devel
BuildRequires:	libmcrypt-devel
BuildRequires:	libesound-devel
BuildRequires:  libopenssl-devel
BuildRequires:  libxtst-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}


%description
This package contains some plugins for gkrellm.  Included are the following
plugins:

  * gkrellmms, controls xmms
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

%package mms
Summary:	Xmms plugin for %{name}
Group:		Monitoring
Requires:	gkrellm = %{version}
Requires:	xmms
BuildRequires:	xmms-devel
BuildRequires:	gtk+1.2-devel

%description mms
GKrellMMS, allows you to control XMMS from within GKrellM.

%prep
%setup -T -c -n %{name}
%setup -q -T -D -c -a 1 -n %{name}
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

%build
(cd gkrellmms
make CFLAGS="%{optflags}"
)
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
make CFLAGS="%{optflags}"
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
install -c -s -m 755 gkrellmms/gkrellmms.so %{buildroot}%{_libdir}/gkrellm2/plugins
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
%exclude %{_libdir}/gkrellm2/plugins/gkrellmms.so
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

%files mms
%defattr(-,root,root)
%doc gkrellmms/README
%doc gkrellmms/FAQ
%doc gkrellmms/Changelog
%doc gkrellmms/Themes
%{_libdir}/gkrellm2/plugins/gkrellmms.so
