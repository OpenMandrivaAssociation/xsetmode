Name:		xsetmode
Version:	1.0.0
Release:	%mkrel 4
Summary:	Set the mode for an XInput device
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxi-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
Xsetmode sets the mode of an XInput device to either absolute or relative.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

#

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xsetmode
%{_mandir}/man1/xsetmode.1*

