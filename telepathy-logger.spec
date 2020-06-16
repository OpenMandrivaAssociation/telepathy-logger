%define major 3
%define api 0.2
%define libname %mklibname %{name} %{major}
%define girname %mklibname %{name}-gir %{api}
%define develname %mklibname -d %{name}

Name:		telepathy-logger
Version:	0.8.2
Release:	4
Summary:	A logger for the telepathy framework
Group:		Networking/Instant messaging
License:	LGPLv2+
URL:		http://telepathy.freedesktop.org/wiki/
Source0:	http://telepathy.freedesktop.org/releases/%{name}/%{name}-%{version}.tar.bz2
Patch0:		0001-tools-Fix-the-build-with-Python-3.patch
BuildRequires:	glib2.0-common
BuildRequires:	intltool
BuildRequires:	pkgconfig(libxslt)
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(sqlite3)
BuildRequires:	pkgconfig(telepathy-glib) >= 0.13.4
BuildRequires:	xsltproc
Requires:	telepathy-filesystem

%description
%{name} is a logger for the telepathy framework.

%package -n %{libname}
Group:		System/Libraries
Summary:	A logger library for the telepathy framework

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

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
%autosetup -p1

sed -i -e 's|"/lib /usr/lib|"/%{_lib} %{_libdir}|' configure

%build
%configure \
	--enable-call

sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

%make_build LIBS='-lgmodule-2.0'

%install
%make_install
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
