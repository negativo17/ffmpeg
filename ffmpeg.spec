%global _lto_cflags %{nil}

Summary:        A complete solution to record, convert and stream audio and video
Name:           ffmpeg
Version:        4.4
Release:        1%{?dist}
License:        LGPLv3+
URL:            http://%{name}.org/
Epoch:          1

Source0:        http://%{name}.org/releases/%{name}-%{version}.tar.xz

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
BuildRequires:  pkgconfig(libopenmpt) >= 0.2.6557
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(librabbitmq) >= 0.7.1
BuildRequires:  pkgconfig(librtmp)
BuildRequires:  pkgconfig(libssh)
BuildRequires:  pkgconfig(libtcmalloc)
BuildRequires:  pkgconfig(libva) >= 0.35.0
BuildRequires:  pkgconfig(libva-drm)
BuildRequires:  pkgconfig(libva-x11)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libwebp) >= 0.4.0
BuildRequires:  pkgconfig(libwebpmux) >= 0.4.0
BuildRequires:  pkgconfig(openh264)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(opus)
BuildRequires:  pkgconfig(rubberband) >= 1.8.1
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(smbclient)
BuildRequires:  pkgconfig(speex)
BuildRequires:  pkgconfig(tesseract)
BuildRequires:  pkgconfig(vidstab) >= 0.98
BuildRequires:  pkgconfig(vpx) >= 1.4.0
BuildRequires:  pkgconfig(vulkan) >= 1.1.97
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
BuildRequires:  glslang-devel
BuildRequires:  pkgconfig(lilv-0)
BuildRequires:  pkgconfig(pocketsphinx)
BuildRequires:  pkgconfig(rav1e) >= 0.4.0
%endif

%if 0%{?fedora} || 0%{?rhel} >= 8
BuildRequires:  pkgconfig(libzmq) >= 4.2.1
BuildRequires:  pkgconfig(lv2)
BuildRequires:  pkgconfig(srt) >= 1.3.0
BuildRequires:  pkgconfig(vapoursynth-script) >= 42
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
    --enable-libopenmpt \
    --enable-libopus \
    --enable-libpulse \
    --enable-librabbitmq \
    --enable-librsvg \
    --enable-librtmp \
    --enable-librubberband \
    --enable-libsmbclient \
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
    --enable-openssl \
    --enable-postproc \
    --enable-sdl2 \
    --enable-shared \
    --enable-swresample \
    --enable-swscale \
    --enable-v4l2-m2m \
    --enable-vaapi \
    --enable-version3 \
    --enable-vdpau \
    --enable-vulkan \
    --enable-xlib \
    --enable-zlib \
    --incdir=%{_includedir}/%{name} \
    --libdir=%{_libdir} \
    --mandir=%{_mandir} \
    --optflags="%{optflags}" \
    --prefix=%{_prefix} \
    --shlibdir=%{_libdir} \
%if 0%{?fedora}
    --enable-libglslang \
    --enable-librav1e \
    --enable-pocketsphinx \
%endif
%if 0%{?fedora} || 0%{?rhel} >= 8
    --enable-libsrt \
    --enable-libzmq \
    --enable-lv2 \
    --enable-vapoursynth \
%endif
%ifarch x86_64
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
- Update to 4.4, review libraries and options.
- Switch from GnuTLS to OpenSSL.
- Trim changelog.

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
