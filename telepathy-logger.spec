%define major 2
%define api 0.2
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname -d %{name}

Name:		telepathy-logger
Version:	0.2.12
Release:   	3
Summary:   	A logger for the telepathy framework
Group:     	Networking/Instant messaging
License:	LGPLv2+
URL:       	http://telepathy.freedesktop.org/wiki/
Source0:   	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2

BuildRequires:	glib2.0-common
BuildRequires:	intltool
BuildRequires:	libxslt-proc
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(farsight2-0.10)
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
This package contains the development library and header files for %{name}.

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

