# To do:
#   --enable-avisynth
#   --enable-libflite       flite-devel
#   --enable-libklvanc      libklvanc-devel
#   --enable-liblensfun     requires liblensfun 0.3.95+
#   --enable-libmysofa      pkgconfig(libmysofa)
#   --enable-libopencv      pkgconfig(opencv)
#   --enable-libopenmpt     pkgconfig(libopenmpt) >= 0.2.6557
#   --enable-libshine       pkgconfig(shine)
#   --enable-libsmbclient   pkgconfig(smbclient)
#   --enable-libsrt         pkgconfig(srt) >= 1.3.0
#   --enable-libtensorflow  libtensorflow-devel
#   --enable-tls            pkgconfig(libtls)
#   --enable-pocketsphinx   pkgconfig(pocketsphinx)

%global _lto_cflags %{nil}

Summary:        A complete solution to record, convert and stream audio and video
Name:           ffmpeg
Version:        4.4
Release:        1%{?dist}
License:        LGPLv3+
URL:            http://%{name}.org/
Epoch:          1

Source0:        http://%{name}.org/releases/%{name}-%{version}.tar.xz
# Excerpt from Nvidia's Video Codec SDK document: Using_FFmpeg_with_NVIDIA_GPU_Hardware_Acceleration.pdf
Source1:        using_ffmpeg_with_nvidia_gpus.txt

# https://github.com/OpenVisualCloud/SVT-VP9/tree/master/ffmpeg_plugin
Patch0:         %{name}-svt-vp9.patch
# https://github.com/OpenVisualCloud/SVT-HEVC/tree/master/ffmpeg_plugin
Patch1:         %{name}-svt-hevc.patch
# https://framagit.org/tytan652/ffmpeg-ndi-patch
Patch2:         %{name}-ndi.patch

Requires:       %{name}-libs%{?_isa} = %{?epoch}:%{version}-%{release}

BuildRequires:  bzip2-devel
BuildRequires:  codec2-devel
BuildRequires:  decklink-devel >= 11.5
BuildRequires:  doxygen
BuildRequires:  freetype-devel
BuildRequires:  frei0r-devel
BuildRequires:  gsm-devel
BuildRequires:  ilbc-devel
BuildRequires:  lame-devel >= 3.98.3
BuildRequires:  ladspa-devel
BuildRequires:  libavc1394-devel
BuildRequires:  libcdio-paranoia-devel
BuildRequires:  libchromaprint-devel
BuildRequires:  libdav1d-devel
BuildRequires:  libdrm-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  libiec61883-devel
%ifarch i686 x86_64 armv7hl
BuildRequires:  libndi-devel
%endif
BuildRequires:  libtheora-devel
BuildRequires:  libvdpau-devel
BuildRequires:  libvorbis-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxcb-devel >= 1.4
BuildRequires:  libxml2-devel
BuildRequires:  libX11-devel
BuildRequires:  libXv-devel
BuildRequires:  libXvMC-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  nasm
BuildRequires:  ocl-icd-devel
BuildRequires:  openal-soft-devel
BuildRequires:  opencl-headers
BuildRequires:  opencore-amr-devel
BuildRequires:  perl(Pod::Man)
BuildRequires:  snappy-devel
BuildRequires:  soxr-devel
BuildRequires:  subversion
BuildRequires:  texinfo
BuildRequires:  twolame-devel >= 0.3.10
BuildRequires:  vo-amrwbenc-devel
BuildRequires:  xvidcore-devel
BuildRequires:  xz-devel
BuildRequires:  zvbi-devel >= 0.2.28

BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(aom) >= 1.0.0
BuildRequires:  pkgconfig(caca)
BuildRequires:  pkgconfig(davs2) >= 1.5.115
BuildRequires:  pkgconfig(fdk-aac)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(kvazaar) >= 0.8.1
#BuildRequires:  pkgconfig(lensfun) >= 0.3.95
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libbluray)
BuildRequires:  pkgconfig(libbs2b)
BuildRequires:  pkgconfig(libdc1394-2)
BuildRequires:  pkgconfig(libgme)
BuildRequires:  pkgconfig(libmodplug)
BuildRequires:  pkgconfig(libopenjp2) >= 2.1.0
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(opencv)
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(vidstab) >= 0.98
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(xavs2) >= 1.2.77
BuildRequires:  pkgconfig(xcb) >= 1.4
BuildRequires:  pkgconfig(xcb-shape)
BuildRequires:  pkgconfig(xcb-shm)
BuildRequires:  pkgconfig(xcb-xfixes)
BuildRequires:  pkgconfig(x264) >= 0.118
BuildRequires:  pkgconfig(x265) >= 0.68
BuildRequires:  pkgconfig(zimg) >= 2.7.0
BuildRequires:  pkgconfig(zlib)

%if 0%{?fedora}
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(lv2)
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libzmq) >= 4.2.1
%endif

%ifarch x86_64
# Nvidia CUVID support and Performance Primitives based code
BuildRequires:  cuda-devel
BuildRequires:  pkgconfig(ffnvcodec) >= 8.1.24.2
BuildRequires:  pkgconfig(libmfx)
BuildRequires:  pkgconfig(libvmaf) >= 1.3.9
BuildRequires:  pkgconfig(SvtAv1Enc)
BuildRequires:  pkgconfig(SvtHevcEnc)
BuildRequires:  pkgconfig(SvtVp9Enc)
%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(vapoursynth-script) >= 42
%endif
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
%autosetup -p1
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
    --enable-avcodec \
    --enable-avdevice \
    --enable-avfilter \
    --enable-avformat \
    --enable-avresample \
    --enable-alsa \
    --enable-bzlib \
    --enable-chromaprint \
    --enable-decklink \
    --enable-frei0r \
    --enable-gcrypt \
    --enable-gmp \
    --enable-gnutls \
    --enable-gpl \
    --enable-gray \
    --enable-iconv \
    --enable-ladspa \
    --enable-libass \
    --enable-libaom \
    --enable-libbluray \
    --enable-libbs2b \
    --enable-libcaca \
    --enable-libcdio \
    --enable-libcodec2 \
    --enable-libdc1394 \
    --enable-libdav1d \
    --enable-libdavs2 \
    --enable-libdrm \
    --enable-libfdk-aac \
    --enable-libfontconfig \
    --enable-libfreetype \
    --enable-libfribidi \
    --enable-libgme \
    --enable-libgsm \
    --enable-libiec61883 \
    --enable-libilbc \
    --enable-libjack \
    --enable-libkvazaar \
    --enable-libmodplug \
    --enable-libmp3lame \
%ifarch i686 x86_64 armv7hl
    --enable-libndi_newtek \
%endif
    --enable-libopencore-amrnb \
    --enable-libopencore-amrwb \
    --enable-libopenh264 \
    --enable-libopenjpeg \
    --enable-libopus \
    --enable-libpulse \
    --enable-librsvg \
    --enable-librtmp \
    --enable-librubberband \
    --enable-libsnappy \
    --enable-libsoxr \
    --enable-libspeex \
    --enable-libssh \
    --enable-libtesseract \
    --enable-libtheora \
    --enable-libtwolame \
    --enable-libv4l2 \
    --enable-libvidstab \
    --enable-libvo-amrwbenc \
    --enable-libvorbis \
    --enable-libvpx \
    --enable-libwebp \
    --enable-libx264 \
    --enable-libx265 \
    --enable-libxavs2 \
    --enable-libxcb \
    --enable-libxcb-shape \
    --enable-libxcb-shm \
    --enable-libxcb-xfixes \
    --enable-libxml2 \
    --enable-libxvid \
    --enable-libzimg \
    --enable-libzvbi \
    --enable-lzma \
    --enable-nonfree \
    --enable-openal \
    --enable-opencl \
    --enable-opengl \
    --enable-postproc \
    --enable-sdl2 \
    --enable-shared \
    --enable-swresample \
    --enable-swscale \
    --enable-vaapi \
    --enable-version3 \
    --enable-vdpau \
    --enable-xlib \
    --enable-zlib \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --optflags="%{optflags}" \
    --prefix=%{_prefix} \
    --shlibdir=%{_libdir} \
%if 0%{?fedora}
    --enable-lv2 \
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
    --enable-libzmq \
%endif
%ifarch x86_64
%if 0%{?fedora} || 0%{?rhel} >= 8
    --enable-vapoursynth \
%endif
    --enable-cuda \
    --enable-cuvid \
    --enable-ffnvcodec \
    --enable-libmfx \
    --enable-libnpp \
    --enable-libsvtav1 \
    --enable-libsvthevc \
    --enable-libsvtvp9 \
    --enable-libvmaf \
    --enable-nvdec \
    --enable-nvenc \
    --extra-cflags="-I%{_includedir}/cuda" \
    --cpu=%{_target_cpu} \
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
    --arch=arm \
%ifarch armv6hl
    --cpu=armv6 \
%else
    --enable-thumb \
%endif
%endif

%make_build
make documentation
make alltools

%install
%make_install
# Let rpmbuild pick up the docs
rm -fr %{buildroot}%{_docdir}/*
rm -fr %{buildroot}%{_datadir}/examples
mkdir doc/html
mv doc/*.html doc/html

%ldconfig_scriptlets libs

%files
%doc using_ffmpeg_with_nvidia_gpus.txt
%{_bindir}/%{name}
%{_bindir}/ffplay
%{_bindir}/ffprobe
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man1/ffplay*.1*
%{_mandir}/man1/ffprobe*.1*
%{_datadir}/%{name}

%files libs
%license COPYING.* LICENSE.md
%doc MAINTAINERS README.md CREDITS Changelog RELEASE_NOTES
%{_libdir}/lib*.so.*
%exclude %{_libdir}/libavdevice.so.*
%{_mandir}/man3/lib*.3.gz

%files -n libavdevice
%license COPYING.* LICENSE.md
%{_libdir}/libavdevice.so.*

%files devel
%doc doc/APIchanges doc/*.txt
%doc doc/html doc/examples
%{_includedir}/%{name}
%{_libdir}/pkgconfig/lib*.pc
%{_libdir}/lib*.so

%changelog
* Thu Apr 22 2021 Simone Caronni <negativo17@gmail.com> - 1:4.4-1
- Update to 4.4.

* Tue Jul 20 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-4
- Rebuild for updated dependencies.

* Sun Jun 20 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-3
- Rebuild for updated dependencies.

* Thu Mar 25 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-2
- Re-enable NDI support.

* Mon Mar 01 2021 Simone Caronni <negativo17@gmail.com> - 1:4.3.2-1
- Update to 4.3.2.

* Sat Dec 05 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-4
- Rebuild for updated dependencies.

* Thu Nov 26 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-3
- Add SVT HEVC, AV1 and VP9 patches.

* Tue Nov 17 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-2
- Rebuild for updated CUDA libraries.

* Tue Aug 25 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3.1-1
- Update to 4.3.1.

* Tue Jul 14 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-4
- Rebuild for updated dependencies.

* Thu Jul 09 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-3
- Rebuild for updated dependencies.

* Tue Jun 30 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-2
- Enable AV1 support also on CentOS/RHEL.

* Tue Jun 23 2020 Simone Caronni <negativo17@gmail.com> - 1:4.3-1
- Update to 4.3.
- Enable VMAF support.
- Disable ZeroMQ support on RHEL/CentOS 7."

* Mon Jun 08 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.3-2
- Rebuild for updated dependencies.

* Sat May 23 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.3-1
- Update to 4.2.3.
- Update SPEC file.

* Fri May 15 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-6
- Rebuild for updated dependencies.

* Fri Mar 27 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-5
- Enable iec6188 to support DV capure wia Firewire.

* Sun Mar 15 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-4
- Fix build on Fedora 32.

* Sun Jan 19 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-3
- Rebuild for updated dependencies.

* Thu Jan 16 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-2
- Enable vapoursynth on Fedora & RHEL/CentOS 8.

* Sat Jan 11 2020 Simone Caronni <negativo17@gmail.com> - 1:4.2.2-1
- Update to 4.2.2.

* Wed Nov 27 2019 Simone Caronni <negativo17@gmail.com> - 1:4.2.1-2
- Rebuild for updated dependencies.

* Sun Oct 20 2019 Simone Caronni <negativo17@gmail.com> - 1:4.2.1-1
- Update to 4.2.1.

* Tue Sep 03 2019 Simone Caronni <negativo17@gmail.com> - 1:4.2-1
- Update to 4.2.

* Tue Jul 09 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.4-1
- Update to 4.1.4.

* Sun Jul 07 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.3-4
- Rebuild for updated dependencies.

* Sun Jun 09 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.3-3
- Enable davs2/xavs2 on x86_64.

* Mon May 27 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.3-2
- Rebuild for updated dependencies.

* Mon Apr 08 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.3-1
- Update to 4.1.3.

* Mon Apr 08 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.2-4
- Fix https transport #7.

* Sun Apr 07 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.2-3
- Rebuild for CUDA 10.1.

* Wed Mar 27 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.2-2
- Update build options.

* Sat Mar 23 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.2-1
- Update to 4.1.2.

* Thu Feb 28 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.1-2
- Rebuild for updated dependencies.

* Tue Feb 19 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1.1-1
- Update to 4.1.1.

* Thu Jan 03 2019 Simone Caronni <negativo17@gmail.com> - 1:4.1-2
- Rebuild for CUDA 10.0.

* Mon Nov 12 2018 Simone Caronni <negativo17@gmail.com> - 1:4.1-1
- Update to 4.1.

* Sat Oct 20 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.2-5
- Rebuild for updated dependencies.

* Thu Sep 20 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.2-4
- Rebuild for updated libraries.

* Tue Aug 28 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.2-3
- Rebuild for CUDA update.

* Sun Aug 19 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.2-2
- Enable libxml support (thanks barsnick).

* Fri Jul 20 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.2-1
- Update to 4.0.2.

* Mon Jul 16 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.1-2
- Rebuild for updated dependencies.
- Add missing Alsa build requirement (thanks Matteo).

* Fri Jun 22 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0.1-1
- Update to 4.0.1.

* Fri Apr 27 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0-3
- Move examples to devel subpackage.
- Remove OpenMAX support.

* Fri Apr 27 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0-2
- Update build options.

* Tue Apr 24 2018 Simone Caronni <negativo17@gmail.com> - 1:4.0-1
- Update to 4.0.
- Update build requirements.
- Momentarily disable VPX support in RHEL/CentOS 7.

* Wed Feb 14 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.2-1
- Update to 3.4.2.

* Fri Feb 02 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.1-4
- Enable DeckLink support.

* Fri Jan 19 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.1-3
- Enable Newtek NDI I/O support.

* Tue Jan 09 2018 Simone Caronni <negativo17@gmail.com> - 1:3.4.1-2
- Rebuild for the various updates.

* Thu Dec 14 2017 Simone Caronni <negativo17@gmail.com> - 1:3.4.1-1
- Update to 3.4.1

* Tue Oct 24 2017 Simone Caronni <negativo17@gmail.com> - 1:3.4-1
- Update to version 3.4.
- Add SVG rasterization and KMS screengrabber support.
- Remove schroedinger support.
- Remove netCDF support, it will be part of sofa filters.

* Tue Sep 12 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.4-1
- Update to 3.3.4.

* Mon Aug 14 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.3-2
- Rebuild for libwebp change.

* Tue Aug 08 2017 Simone Caronni <negativo17@gmail.com> - 1:3.3.3-1
- Update to 3.3.3.
- Bump Nvidia video codec sdk requirements to 8.0.14.

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
