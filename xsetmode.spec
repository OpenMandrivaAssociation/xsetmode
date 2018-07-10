Name:		xsetmode
Version:	1.0.0
Release:	24
Summary:	Set the mode for an XInput device
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xi) >= 1.0.0
BuildRequires: pkgconfig(xfixes) pkgconfig(xcb) pkgconfig(pthread-stubs)
BuildRequires: x11-util-macros >= 1.0.1

%description
Xsetmode sets the mode of an XInput device to either absolute or relative.

%prep
%setup -q

%build
#fix build with new automake
sed -i -e 's,AM_CONFIG_HEADER,AC_CONFIG_HEADERS,g' configure.*
libtoolize --copy --force
autoreconf -fi
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%{_bindir}/xsetmode
%{_mandir}/man1/xsetmode.1*
