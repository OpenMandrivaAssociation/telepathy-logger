%define major 2
%define api 0.2
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname -d %{name}

Name:		telepathy-logger
Version:	0.4.0
Release:   	2
Summary:   	A logger for the telepathy framework
Group:     	Networking/Instant messaging
License:	LGPLv2+
URL:       	http://telepathy.freedesktop.org/wiki/
Source0:   	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	glib2.0-common
BuildRequires:	intltool
BuildRequires:	libxslt-proc
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(farstream-0.1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gst-python-0.10)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(python)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:  pkgconfig(telepathy-glib) >= 0.13.4

Requires:       telepathy-filesystem

%description
%{name} is a logger for the telepathy framework.

%package -n %{libname}
Group:		System/Libraries
Summary:	A logger library for the telepathy framework

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{girname}
Summary:    GObject Introspection interface description for %{name}
Group:      System/Libraries
Requires:   %{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Group:		Development/C
Summary:	A logger library for the telepathy framework
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the development library and header files for 
%{name}.

%prep
%setup -q

%build
%configure2_5x \
	--enable-call \
	--disable-static

%make LIBS='-lgmodule-2.0'

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name "*.la" -delete

%files
%{_libexecdir}/%{name}
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.Logger.service
%{_datadir}/telepathy/clients/Logger.client
%{_datadir}/glib-2.0/schemas/org.freedesktop.Telepathy.Logger.gschema.xml

%files -n %{libname}
%{_libdir}/libtelepathy-logger.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/TelepathyLogger-%{api}.typelib

%files -n %{develname}
%{_libdir}/libtelepathy-logger.so
%{_includedir}/%{name}-%{api}
%{_datadir}/gtk-doc/html/telepathy-logger/
%{_libdir}/pkgconfig/telepathy-logger-%{api}.pc
%{_datadir}/gir-1.0/TelepathyLogger-%{api}.gir



%changelog
* Fri Apr 27 2012 Alexander Khrukin <akhrukin@mandriva.org> 0.4.0-1
+ Revision: 793935
- version update 0.4.0

* Sat Jan 21 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.12-3
+ Revision: 764339
- fixed devel pkg description length
- added build linking fix
- rebuild with call support

* Sat Dec 10 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.2.12-2
+ Revision: 740094
- bump for the BS
- fixed BRs
- new version 0.2.12
- cleaned up spec
- removed .la files
- disabled static build
- removed dep loop
- removed mkrel, BuildRoot, clean section, defattr
- split out gir pkg
- changed lib & devel descriptions
- converted BRs to pkgconfig provides
- api should be added to lib pkg name

* Thu Jun 16 2011 Götz Waschk <waschk@mandriva.org> 0.2.10-1
+ Revision: 685499
- update to new version 0.2.10

* Sat May 07 2011 Funda Wang <fwang@mandriva.org> 0.2.9-1
+ Revision: 672275
- update to new version 0.2.9

* Mon Apr 04 2011 Götz Waschk <waschk@mandriva.org> 0.2.8-1
+ Revision: 650292
- new version
- new api and major
- enable introspection
- bump telepathy-glib dep

* Wed Dec 01 2010 Götz Waschk <waschk@mandriva.org> 0.1.7-1mdv2011.0
+ Revision: 604282
- update to new version 0.1.7

* Fri Oct 15 2010 Götz Waschk <waschk@mandriva.org> 0.1.6-1mdv2011.0
+ Revision: 585760
- update to new version 0.1.6

* Fri Aug 20 2010 Götz Waschk <waschk@mandriva.org> 0.1.5-2mdv2011.0
+ Revision: 571430
- fix deps

* Wed Aug 18 2010 Götz Waschk <waschk@mandriva.org> 0.1.5-1mdv2011.0
+ Revision: 571157
- update build deps
- new version
- depend on new glib
- remove gconf stuff and replace by gsettings

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 0.1.4-1mdv2011.0
+ Revision: 563550
- update build deps
- update to new version 0.1.4
- import telepathy-logger

