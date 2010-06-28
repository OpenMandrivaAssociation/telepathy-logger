%define major 1
%define api 0.1
%define libname %mklibname %name %major
%define develname %mklibname -d %name
Name:           telepathy-logger
Version:        0.1.3
Release:        %mkrel 1
Summary:        A logger for the telepathy framework

Group:          Networking/Instant messaging
License:        LGPLv2+
URL:            http://telepathy.freedesktop.org/wiki/
Source0:        http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires:  dbus-glib-devel
BuildRequires: libtelepathy-glib-devel >= 0.11.7
BuildRequires:  libxslt-proc
BuildRequires:  python-devel
Requires: %libname >= %version

%description
%name is a logger for the telepathy framework.

%package -n %libname
Group: System/Libraries
Summary: A logger library for the telepathy framework
Provides: %name
Obsoletes: %name
Requires:       telepathy-filesystem

%description -n %libname
%name is a logger library for the telepathy framework.

%package -n %develname
Group: Development/C
Summary: A logger library for the telepathy framework
Requires: %libname = %version-%release
Provides: lib%name-devel = %version-%release

%description -n %develname
%name is a logger library for the telepathy framework.

%files
%defattr(-,root,root,-)
%_sysconfdir/gconf/schemas/telepathy-logger.schemas
%_libexecdir/%name
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Client.Logger.service
%_datadir/dbus-1/services/org.freedesktop.Telepathy.Logger.service
%_datadir/telepathy/clients/Logger.client

%files -n %libname
%defattr(-,root,root,-)
%{_libdir}/libtelepathy-logger.so.%{major}*

%files -n %develname
%defattr(-,root,root,-)
%{_libdir}/libtelepathy-logger.la
%{_libdir}/libtelepathy-logger.so
%{_includedir}/%name-%api
%{_datadir}/gtk-doc/html/telepathy-logger/
%_libdir/pkgconfig/telepathy-logger-%api.pc

#--------------------------------------------------------------------

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %buildroot
%makeinstall_std
rm -f %buildroot%{_libdir}/libtelepathy-logger.a

%clean
rm -rf %buildroot

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%preun
%preun_uninstall_gconf_schemas %name
