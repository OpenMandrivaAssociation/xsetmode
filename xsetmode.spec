Name:		xsetmode
Version:	1.0.0
Release:	14
Summary:	Set the mode for an XInput device
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xi) >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
Xsetmode sets the mode of an XInput device to either absolute or relative.

%prep
%setup -q -n %{name}-%{version}

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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-10mdv2011.0
+ Revision: 671364
- mass rebuild

* Sat Dec 04 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-9mdv2011.0
+ Revision: 608239
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.0-8mdv2010.1
+ Revision: 524466
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.0-7mdv2009.1
+ Revision: 350777
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-6mdv2009.0
+ Revision: 226077
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.0-5mdv2008.1
+ Revision: 154302
- Updated BuildRequires and resubmit package.

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.0-4mdv2008.0
+ Revision: 76592
- rebuild for 2008
- minor spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Tue May 30 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-30 16:15:56 (31710)
- fill in a few more missing descriptions

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

