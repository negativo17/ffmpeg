Summary:        A complete solution to record, convert and stream audio and video
Name:           ffmpeg
Version:        3.3.2
Release:        3%{?dist}
License:        LGPLv3+
URL:            http://%{name}.org/
Epoch:          1

Source0:        http://%{name}.org/releases/%{name}-%{version}.tar.xz
# Excerpt from Nvidia's Video Codec SDK document: Using_FFmpeg_with_NVIDIA_GPU_Hardware_Acceleration.pdf
Source1:        using_ffmpeg_with_nvidia_gpus.txt

Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}

BuildRequires:  bzip2-devel
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  frei0r-devel
BuildRequires:  gsm-devel
BuildRequires:  ilbc-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libfdk-aac-devel
BuildRequires:  libssh-devel
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
# libwebp at >= 0.2.0, but libwepmux at 0.4.0
BuildRequires:  libwebp-devel >= 0.4.0
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  mesa-libGL-devel
BuildRequires:  nvenc >= 7
Buildrequires:  ocl-icd-devel
Buildrequires:  openal-soft-devel
Buildrequires:  opencl-headers
Buildrequires:  opencore-amr-devel
BuildRequires:  openjpeg-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  soxr-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  xvidcore-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
BuildRequires:  zvbi-devel >= 0.2.28

BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(kvazaar) >= 0.8.1
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libmodplug)
#BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libwebp) >= 0.2.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(libzmq)
BuildRequires:  pkgconfig(netcdf)
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openh264) >= 1.6
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
BuildRequires:  pkgconfig(schroedinger-1.0)
BuildRequires:  pkgconfig(sdl2)
#BuildRequires:  pkgconfig(shine)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(tesseract)
#BuildRequires:  pkgconfig(vidstab) >= 0.98
BuildRequires:  pkgconfig(vpx) >= 1.3.0
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(x264) >= 0.118
BuildRequires:  pkgconfig(x265) >= 0.68
#BuildRequires:  pkgconfig(zimg) >= 2.3.0

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
    --enable-libnpp \
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
    --enable-libfdk-aac \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgsm \
    --enable-libilbc \
    --enable-libkvazaar \
    --enable-libmfx \
    --enable-libmp3lame \
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopus \
    --enable-libpulse \
    --enable-librtmp \
    --enable-librubberband \
    --enable-libschroedinger \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtesseract \
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
    --enable-netcdf \
    --enable-nonfree \
    --enable-openal \
    --enable-opencl \
    --enable-nvenc \
    --enable-opengl \
    --enable-postproc \
    --enable-pthreads \
    --enable-sdl2 \
    --enable-shared \
    --enable-version3 \
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
%doc doc/ffserver.conf using_ffmpeg_with_nvidia_gpus.txt
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
%license COPYING.* LICENSE.md
%doc MAINTAINERS README.md CREDITS Changelog RELEASE_NOTES
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
* Sun Jun 25 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.2-3
- Move Nvidia doc in main package.

* Thu Jun 22 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.2-2
- Add extensive notes for Nvidia GPUs taken from Nvidia Video Codec SDK.

* Thu Jun 08 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.2-1
- Update to 3.3.2.

* Mon May 29 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.1-1
- Update to 3.3.1.

* Sat May 13 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3-1
- Update to 3.3.
- Enable ilbc, netcdf, rubberband, tesseract support.
- Update build requirements to pkgconfig format where appropriate.

* Wed Mar 22 2017 Simone Caronni <negativo17@gmail.com> - 1:3.2.4-3
- Rebuild for libbluray update.

* Thu Feb 23 2017 Simone Caronni <negativo17@gmail.com> - 1:3.2.4-2
- Rebuild for x265 update.

* Sun Feb 12 2017 Simone Caronni <negativo17@gmail.com> - 1:3.2.4-1
- Update to 3.2.4.

* Tue Jan 03 2017 Simone Caronni <negativo17@gmail.com> - 1:3.2.2-2
- Rebuild for x265 2.2.

* Wed Dec 07 2016 Simone Caronni <negativo17@gmail.com> - 1:3.2.2-1
- Update to 3.2.2.

* Mon Nov 28 2016 Simone Caronni <negativo17@gmail.com> - 1:3.2.1-1
- Update to 3.2.1.

* Fri Nov 18 2016 Simone Caronni <negativo17@gmail.com> - 1:3.2-2
- Enable libebur128 support.

* Mon Nov 07 2016 Simone Caronni <negativo17@gmail.com> - 1:3.2-1
- Update to 3.2, remove upstreamed patch.
- Remove obsolete faac and SDL options
- Enable SDL2.

* Sun Oct 23 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.5-1
- Update to latest release.

* Tue Oct 18 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.4-3
- Update NVENC build requirement for 10-bit HEVC encoding support (3.2 feature).

* Mon Oct 17 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.4-2
- Explicitly enable NVIDIA Performance Primitives.
- Rebase OpenH264 1.6 patch from 3.2 to 3.1.4.

* Mon Oct 03 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.4-1
- Update to 3.1.4.

* Sun Oct 02 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.3-2
- Rebuild for x265 update.

* Tue Sep 06 2016 Simone Caronni <negativo17@gmail.com> - 1:3.1.3-1
- Update to 3.1.3.

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
