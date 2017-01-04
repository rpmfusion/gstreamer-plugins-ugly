# $Id: gstreamer-plugins-ugly.spec 5453 2007-05-31 10:59:47Z thias $
# Authority: matthias
# ExclusiveDist: fc5 fc6 el5 fc7

%define majorminor   0.10
%define gstreamer    gstreamer

%define gst_minver   0.10.26
%define gstpb_minver 0.10.26

Summary: GStreamer streaming media framework "ugly" plug-ins
Name: gstreamer-plugins-ugly
Version: 0.10.19
Release: 20%{?dist}
License: LGPLv2+
Group: Applications/Multimedia
URL: http://gstreamer.freedesktop.org/
Source: http://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.bz2
Patch1: 0001-new-libcdio.patch
Patch2: 0002-fix-build-with-new-gtkdoc.patch
Requires: %{gstreamer} >= %{gst_minver}
BuildRequires: %{gstreamer}-devel >= %{gst_minver}
BuildRequires: %{gstreamer}-plugins-base-devel >= %{gstpb_minver}

BuildRequires: gettext-devel
BuildRequires: gtk-doc

BuildRequires: a52dec-devel >= 0.7.3
BuildRequires: libdvdread-devel >= 0.9.0
BuildRequires: lame-devel >= 3.89
BuildRequires: libid3tag-devel >= 0.15.0
BuildRequires: libmad-devel >= 0.15.0
BuildRequires: mpeg2dec-devel >= 0.4.0
BuildRequires: orc-devel >= 0.4.5
BuildRequires: libcdio-devel >= 0.82
BuildRequires: twolame-devel
BuildRequires: x264-devel >= 0.0.0-0.28
BuildRequires: opencore-amr-devel

Provides: gstreamer-sid = %{version}-%{release}
Provides: gstreamer-lame = %{version}-%{release}
Provides: gstreamer-mad = %{version}-%{release}
Provides: gstreamer-a52dec = %{version}-%{release}
Provides: gstreamer-dvdread = %{version}-%{release}
Provides: gstreamer-mpeg2dec = %{version}-%{release}

%description
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains well-written plug-ins that can't be shipped in
gstreamer-plugins-good because:
- the license is not LGPL
- the license of the library is not LGPL
- there are possible licensing issues with the code.


%package devel-docs
Summary: Development documentation for the GStreamer "ugly" plug-ins
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description devel-docs
GStreamer is a streaming media framework, based on graphs of elements which
operate on media data.

This package contains the development documentation for the plug-ins that can't
be shipped in gstreamer-plugins-good because:
- the license is not LGPL
- the license of the library is not LGPL
- there are possible licensing issues with the code.


%prep
%setup -q -n gst-plugins-ugly-%{version}
%patch1 -p1
%patch2 -p1


%build
%configure \
    --with-package-name="gst-plugins-ugly rpmfusion rpm" \
    --with-package-origin="http://rpmfusion.org/" \
    --enable-debug --enable-gtk-doc \
    --disable-static
%{__make} %{?_smp_mflags}


%install
%{__make} install DESTDIR="%{buildroot}"
%find_lang gst-plugins-ugly-%{majorminor}

# Clean out files that should not be part of the rpm.
%{__rm} -f %{buildroot}%{_libdir}/gstreamer-%{majorminor}/*.la
%{__rm} -f %{buildroot}%{_libdir}/*.la


%files -f gst-plugins-ugly-%{majorminor}.lang
%doc AUTHORS README REQUIREMENTS
%license COPYING
%{_datadir}/gstreamer-%{majorminor}
# Plugins without external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgstasf.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdsub.so
%{_libdir}/gstreamer-%{majorminor}/libgstiec958.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegaudioparse.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpegstream.so
%{_libdir}/gstreamer-%{majorminor}/libgstrmdemux.so
# Plugins with external dependencies
%{_libdir}/gstreamer-%{majorminor}/libgsta52dec.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrnb.so
%{_libdir}/gstreamer-%{majorminor}/libgstamrwbdec.so
%{_libdir}/gstreamer-%{majorminor}/libgstcdio.so
%{_libdir}/gstreamer-%{majorminor}/libgstdvdread.so
%{_libdir}/gstreamer-%{majorminor}/libgstlame.so
%{_libdir}/gstreamer-%{majorminor}/libgstmad.so
%{_libdir}/gstreamer-%{majorminor}/libgstmpeg2dec.so
%{_libdir}/gstreamer-%{majorminor}/libgsttwolame.so
%{_libdir}/gstreamer-%{majorminor}/libgstx264.so

%files devel-docs
%doc %{_datadir}/gtk-doc/html/gst-plugins-ugly-plugins-0.10


%changelog
* Fri Nov 18 2016 Adrian Reber <adrian@lisas.de> - 0.10.19-20
- Rebuilt for libcdio-0.94

* Sat May 21 2016 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.19-19
- Fix FTBFS
- Prune changelog

* Mon Sep 01 2014 Sérgio Basto <sergio@serjux.com> - 0.10.19-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Mar 22 2014 Sérgio Basto <sergio@serjux.com> - 0.10.19-17
- Rebuilt for x264

* Thu Mar 06 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-16
- Rebuilt for x264

* Fri Feb 21 2014 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-15
- Rebuilt

* Tue Nov 05 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-14
- Rebuilt for x264/FFmpeg

* Tue Oct 22 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-13
- Rebuilt for x264

* Sat Jul 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-12
- Rebuilt for x264

* Tue May 07 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-11
- Rebuilt for x264

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.19-10
- Drop no longer needed PyXML BuildRequires (rf#2572)

* Sat Mar  2 2013 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.19-9
- Add upstream patch to fix building with latest libcdio (rf#2697)

* Thu Feb 28 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-8
- Disable libcdio for now

* Sun Feb 24 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-7
- Rebuilt for libcdio

* Sun Jan 20 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-6
- Rebuilt for FFmpeg/x264

* Fri Nov 23 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-5
- Rebuilt for x264

* Thu Sep 06 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-4
- Rebuilt for x264 ABI 125

* Mon Jun 25 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-3
- Drop orphaned libsidplay-devel

* Sun Jun 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-2
- Rebuilt for x264

* Tue May 15 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.19-1
- Update to 0.10.19

* Mon May 14 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.18-8
- Rebuilt for opencore-arm

* Tue Mar 13 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.18-7
- Rebuilt for x264 ABI 0.120

* Fri Mar 02 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.18-6
- Rebuilt for c++ ABI breakage

* Wed Feb 22 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.10.18-5
- Rebuilt for x264/FFmpeg

* Wed Nov 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.10.18-4
- Rebuilt for libcdio

* Sun Sep  4 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.18-3
- Rebuilt for new x264

* Fri Jul 15 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.10.18-2
- Rebuilt for x264 ABI 115

* Tue May 17 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.18-1
- New upstream release 0.10.18

* Thu Apr 21 2011 Hans de Goede <j.w.r.degoede@gmail.com> - 0.10.17-3
- Rebuild for proper package kit magic provides (rhbz#695730, rf#1706)

* Fri Mar 11 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.10.17-2
- Rebuilt for new x264/FFmpeg

* Fri Jan 28 2011 Hans de Goede <j.w.r.degoede@hhs.nl> - 0.10.17-1
- New upstream release 0.10.17
- Temporarily boost mp3parse element rank so that it gets prefered
  over the new (and buggy) mpegaudioparse element from
  gstreamer-plugins-bad-free (gnome#641047)
