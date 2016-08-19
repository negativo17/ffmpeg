Summary:        A complete solution to record, convert and stream audio and video
Name:           ffmpeg
Version:        3.1.2
Release:        1%{?dist}
License:        LGPLv3+
URL:            http://%{name}.org/
Epoch:          1

Source0:        http://%{name}.org/releases/%{name}-%{version}.tar.xz

# https://trac.ffmpeg.org/ticket/5587
Source1:        scale_npp.txt

# OpenH264 1.6 support:
# http://git.videolan.org/?p=ffmpeg.git;a=commit;h=c5d326f551b0312ff581bf1df35b21d956e01523
# http://git.videolan.org/?p=ffmpeg.git;a=commit;h=293676c476733e81d7b596736add6cd510eb6960
Patch0:         ffmpeg-openh264-16.patch

Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}

BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  faac-devel
BuildRequires:  freetype-devel
BuildRequires:  frei0r-devel
BuildRequires:  fribidi-devel
BuildRequires:  gnutls-devel
BuildRequires:  gsm-devel
BuildRequires:  kvazaar-devel >= 0.8.1
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  libass-devel
BuildRequires:  libbluray-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libdc1394-devel
BuildRequires:  libfdk-aac-devel
Buildrequires:  libmfx-devel
Buildrequires:  libmodplug-devel
BuildRequires:  librtmp-devel
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libv4l-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  libvpx-devel
# libwebp at >= 0.2.0, but libwepmux at 0.4.0
BuildRequires:  libwebp-devel >= 0.4.0
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  nvenc >= 5
Buildrequires:  ocl-icd-devel
Buildrequires:  openal-soft-devel
Buildrequires:  opencl-headers
Buildrequires:  opencore-amr-devel
Buildrequires:  openh264-devel
BuildRequires:  openjpeg-devel
BuildRequires:  opus-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  schroedinger-devel
BuildRequires:  SDL-devel
BuildRequires:  soxr-devel
BuildRequires:  speex-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  x264-devel >= 0.118
BuildRequires:  x265-devel >= 0.68
BuildRequires:  xvidcore-devel
BuildRequires:  zlib-devel
BuildRequires:  zvbi-devel >= 0.2.28

%ifarch %{ix86} x86_64
BuildRequires:  libXvMC-devel
BuildRequires:  libva-devel
BuildRequires:  yasm
%endif

# Nvidia CUVID support and Performance Primitives based code
%ifarch x86_64
BuildRequires:  cuda-devel
BuildRequires:  nvidia-driver-devel
%endif

%description
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.

%package        libs
Summary:        Libraries for %{name}

%description    libs
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains the libraries for %{name}.

%package     -n libavdevice
Summary:        Special devices muxing/demuxing library

%description -n libavdevice
Libavdevice is a complementary library to libavf "libavformat". It provides
various "special" platform-specific muxers and demuxers, e.g. for grabbing
devices, audio capture and playback etc.

%package        devel
Summary:        Development package for %{name}
Requires:       %{name}-libs%{_isa} = %{?epoch}:%{version}-%{release}
Requires:       libavdevice%{_isa} = %{?epoch}:%{version}-%{release}
Requires:       pkgconfig

%description    devel
FFmpeg is a complete and free Internet live audio and video
broadcasting solution for Linux/Unix. It also includes a digital
VCR. It can encode in real time in many formats including MPEG1 audio
and video, MPEG4, h263, ac3, asf, avi, real, mjpeg, and flash.
This package contains development files for %{name}.

%prep
%setup -q
%patch0 -p1
# Use CUDA entry point versioned library (SONAME)
sed -i -e 's/libcuda.so/libcuda.so.1/g' libavcodec/nvenc.c
cp %{SOURCE1} .

# Uncomment to enable debugging while configuring
#sed -i -e 's|#!/bin/sh|#!/bin/sh -x|g' configure

%build
./configure \
    --arch=%{_target_cpu} \
    --bindir=%{_bindir} \
    --datadir=%{_datadir}/%{name} \
    --disable-debug \
    --disable-static \
    --disable-stripping \
    --enable-avfilter \
    --enable-avresample \
    --enable-bzlib \
%ifarch x86_64
    --enable-cuda \
    --enable-cuvid \
%endif
    --enable-doc \
    --enable-fontconfig \
    --enable-frei0r \
    --enable-gnutls \
    --enable-gpl \
    --enable-iconv \
    --enable-libass \
    --enable-libbluray \
    --enable-libcdio \
    --enable-libdc1394 \
    --enable-libfaac \
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --enable-libkvazaar \
    --enable-libmfx \
    --enable-libmp3lame \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopus \
    --enable-libnpp \
    --enable-libpulse \
    --enable-librtmp \
    --enable-libschroedinger \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtheora \
    --enable-libtwolame \
    --enable-libv4l2 \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxcb \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxcb-shape \
    --enable-libxvid \
    --enable-libzvbi \
    --enable-lzma \
    --enable-nonfree \
    --enable-openal \
    --enable-opencl \
    --enable-nvenc \
    --enable-opengl \
    --enable-postproc \
    --enable-pthreads \
    --enable-sdl \
    --enable-shared \
    --enable-version3 \
    --enable-x11grab \
    --enable-xlib \
    --enable-zlib \
    --extra-cflags="-I%{_includedir}/nvenc -I%{_includedir}/cuda" \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --optflags="%{optflags}" \
    --prefix=%{_prefix} \
    --shlibdir=%{_libdir} \
%ifarch %{ix86}
    --cpu=%{_target_cpu} \
%endif
%ifarch %{ix86} x86_64 ppc ppc64
    --enable-runtime-cpudetect \
%endif
%ifarch ppc
    --cpu=g3 \
    --enable-pic \
%endif
%ifarch ppc64
    --cpu=g5 \
    --enable-pic \
%endif
%ifarch %{arm}
    --disable-runtime-cpudetect --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%ifarch armv7hnl
    --enable-neon \
%endif
%endif

make %{?_smp_mflags}
make documentation
make alltools

%install
%make_install
# Let rpmbuild pick up the docs
rm -fr %{buildroot}%{_docdir}/*
mkdir doc/html
mv doc/*.html doc/html

%post libs -p /sbin/ldconfig

%postun libs -p /sbin/ldconfig

%files
%doc doc/ffserver.conf
%{_bindir}/%{name}
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_bindir}/ffserver
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man1/ffplay*.1*
%{_mandir}/man1/ffprobe*.1*
%{_mandir}/man1/ffserver*.1*
%{_datadir}/%{name}

%files libs
%{!?_licensedir:%global license %%doc}
%license COPYING.* LICENSE.md
%doc MAINTAINERS README.md CREDITS Changelog RELEASE_NOTES scale_npp.txt
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libavdevice.so.*
%{_mandir}/man3/lib*.3.gz

%files -n libavdevice
%{_libdir}/libavdevice.so.*

%files devel
%doc doc/APIchanges doc/*.txt
%doc doc/html
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%changelog
* Mon Aug 15 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.2-1
- Update to 3.1.2, remove upstreamed patch.

* Fri Aug 05 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.1-3
- Rebuild for OpenH264 1.6.0.

* Thu Jul 14 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.1-2
- Enable Nvidia CUVID support and Performance Primitives based code (x86_64).
  Both require linking to CUDA libraries. As such, libs subpackage now requires
  libraries from both CUDA and Nvidia drivers.

* Thu Jul 14 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.1-1
- Update to 3.1.1.
- Add patch from upstream for runtime crashes.

* Wed May 25 2016 Simone Caronni <negativo17@gmail.com> - 1:3.0.2-1
- Update to 3.0.2.

* Wed Apr 20 2016 Simone Caronni <negativo17@gmail.com> - 1:3.0.1-1
- Update to 3.0.1.
- Enable kvazaar, libzvbi and libxcb support.
- Remove obsolete libvo-aacenc and libaacplus.

* Mon Apr 04 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.6-2
- Rebuild for libva update.

* Wed Mar 16 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.6-1
- Update to 2.8.6.

* Sat Jan 16 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.5-1
- Update to 2.8.5.
- Build with NVENC SDK 6.

* Wed Jan 06 2016 Simone Caronni <negativo17@gmail.com> - 1:2.8.4-1
- Update to 2.8.4.
- Look for libcuda.so.1 instead of libcuda.so.

* Sun Dec 13 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.3-2
- Remove VA-API conditional.
- Add libaacplus support.

* Tue Dec 01 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.3-1
- Update to 2.8.3.

* Mon Nov 30 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.2-4
- Add libcdio, opencl, frei0r and iconv support (fixes support for subtitles in
  HandBrake).

* Fri Nov 27 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.2-3
- Enable libmfx (Intel Quick Sync) and openal.
- Recommend instead of suggesting Nvidia CUDA libraries so they are installed
  automatically if the Nvidia repository is available.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 1:2.8.2-2
- Add doxygen for building docs.
- Bump Epoch so that is not overwritten by RPMFusion package.

* Fri Nov 20 2015 Simone Caronni <negativo17@gmail.com> - 2.8.2-1
- Update to 2.8.2.
- Enabled the following encoders/decoders/transports:
    libvpx, libwebp, fdk-aac, opengl, fontconfig, openal, lzma, libbluray,
    libssh, libvo-aacenc, libvo-amrwbenc, libopencore-amrwb, libopencore-amrnb,
    librtmp, libopenh264, libfribidi.
- Remove CrystalHD and libcelt options.
- Hardcode some other enablements.
- Introduce weak dependency for CUDA libraries to be used with NVENC.
- Sort buildrequires.
- Add additional license information and documentation.

* Mon Sep 28 2015 Simone Caronni <negativo17@gmail.com> - 2.7.2-1
- Update to 2.7.2.

* Wed Jul 29 2015 Simone Caronni <negativo17@gmail.com> - 2.6.4-1
- Update to 2.6.4.
- Switch to xz tarball.

* Mon Jun 08 2015 Simone Caronni <negativo17@gmail.com> - 2.6.3-1
- Update to 2.6.3.
- Disable OpenCL by default on CentOS/RHEL.
- Add license/make_install/_pkgdocdir macro.

* Wed May 06 2015 Simone Caronni <negativo17@gmail.com> - 2.6.2-2
- Add Nvidia library dependency for NVENC.

* Tue Apr 28 2015 Simone Caronni <negativo17@gmail.com> - 2.6.2-1
- Update to 2.6.2.

* Wed Apr 22 2015 Simone Caronni <negativo17@gmail.com> - 2.6.1-2
- Rebuild for x265 update.

* Fri Apr 10 2015 Simone Caronni <negativo17@gmail.com> - 2.4.8-2
- Update to 2.6.1.
- Remove support for snapshots from SPEC file, simplify a bit.
- Remove libdirac support.
- Add optional nvenc (Nvidia Encoder) support.

* Mon Mar 30 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.8-1
- Updated to 2.4.8

* Sun Feb 15 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.7-1
- Updated to 2.4.7

* Sun Feb 01 2015 Dominik Mierzejewski <rpm at greysector.net> - 2.4.6-3
- enable LADSPA support (rfbz#3134)

* Sun Feb 01 2015 Dominik Mierzejewski <rpm at greysector.net> - 2.4.6-2
- enable OpenCL support
- BR texinfo instead of texi2html to reduce BRs by half
- drop support for building on SPARC (no longer a Fedora Secondary Arch)
- move libavdevice to a subpackage (rfbz#3075)

* Wed Jan 14 2015 Julian Sikorski <belegdol@fedoraproject.org> - 2.4.6-1
- Updated to 2.4.6
