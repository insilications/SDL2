#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : SDL2
Version  : 2.0.14
Release  : 401
URL      : https://www.libsdl.org/release/SDL2-2.0.14.tar.gz
Source0  : https://www.libsdl.org/release/SDL2-2.0.14.tar.gz
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0 Zlib
Requires: SDL2-bin = %{version}-%{release}
Requires: SDL2-lib = %{version}-%{release}
BuildRequires : ImageMagick-dev
BuildRequires : Sphinx
BuildRequires : Vulkan-Headers
BuildRequires : Vulkan-Headers-dev
BuildRequires : Vulkan-Loader
BuildRequires : Vulkan-Loader-dev
BuildRequires : Vulkan-Tools
BuildRequires : Vulkan-ValidationLayers
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : acl
BuildRequires : acl-dev
BuildRequires : acl-staticdev
BuildRequires : alsa-firmware
BuildRequires : alsa-lib-dev
BuildRequires : alsa-lib-lib
BuildRequires : alsa-plugins
BuildRequires : alsa-plugins-lib
BuildRequires : alsa-tools
BuildRequires : alsa-ucm-conf
BuildRequires : alsa-utils
BuildRequires : binutils
BuildRequires : binutils-dev
BuildRequires : binutils-staticdev
BuildRequires : brotli
BuildRequires : brotli-dev
BuildRequires : brotli-staticdev
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : bzip2
BuildRequires : bzip2-dev
BuildRequires : bzip2-staticdev
BuildRequires : ca-certs
BuildRequires : ca-certs-static
BuildRequires : cairo
BuildRequires : cairo-dev
BuildRequires : cairo-lib
BuildRequires : ccache
BuildRequires : clazy
BuildRequires : cmake
BuildRequires : cppcheck
BuildRequires : cuda
BuildRequires : cuda-dev
BuildRequires : cuda-staticdev
BuildRequires : curl-dev
BuildRequires : dbus
BuildRequires : dbus-broker
BuildRequires : dbus-dev
BuildRequires : dbus-glib
BuildRequires : dbus-glib-dev
BuildRequires : dbus-python
BuildRequires : doxygen
BuildRequires : e2fsprogs-dev
BuildRequires : elfutils-dev
BuildRequires : evtest
BuildRequires : expat-dev
BuildRequires : expat-dev32
BuildRequires : expat-staticdev
BuildRequires : findutils
BuildRequires : fontconfig-data
BuildRequires : fontconfig-dev
BuildRequires : fontconfig-lib
BuildRequires : freetype-dev
BuildRequires : freetype-lib
BuildRequires : fribidi-dev
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : gdb
BuildRequires : gdb-dev
BuildRequires : gettext
BuildRequires : glib
BuildRequires : glib-bin
BuildRequires : glib-data
BuildRequires : glib-dev
BuildRequires : glib-dev32
BuildRequires : glib-lib
BuildRequires : glibc
BuildRequires : glibc-dev
BuildRequires : glibc-dev32
BuildRequires : glibc-lib-avx2
BuildRequires : glibc-libc32
BuildRequires : glibc-staticdev
BuildRequires : glu
BuildRequires : glu-dev
BuildRequires : gmp
BuildRequires : gmp-dev
BuildRequires : gmp-staticdev
BuildRequires : gnutls
BuildRequires : gnutls-dev
BuildRequires : googletest
BuildRequires : googletest-dev
BuildRequires : graphite
BuildRequires : graphite-dev
BuildRequires : gsm-dev
BuildRequires : gtk+-data
BuildRequires : gtk+-lib
BuildRequires : gtk3-lib
BuildRequires : harfbuzz-dev
BuildRequires : harfbuzz-lib
BuildRequires : icu4c-lib
BuildRequires : jack2
BuildRequires : jack2-dev
BuildRequires : jsoncpp
BuildRequires : jsoncpp-dev
BuildRequires : jsoncpp-lib
BuildRequires : jsoncpp-staticdev
BuildRequires : keyutils
BuildRequires : keyutils-dev
BuildRequires : krb5
BuildRequires : krb5-dev
BuildRequires : libICE-dev
BuildRequires : libSM-dev
BuildRequires : libX11-data
BuildRequires : libX11-dev
BuildRequires : libX11-lib
BuildRequires : libXScrnSaver
BuildRequires : libXScrnSaver-dev
BuildRequires : libXScrnSaver-lib
BuildRequires : libXau-dev
BuildRequires : libXau-lib
BuildRequires : libXcursor-dev
BuildRequires : libXcursor-lib
BuildRequires : libXdamage-dev
BuildRequires : libXdamage-lib
BuildRequires : libXdmcp-dev
BuildRequires : libXdmcp-lib
BuildRequires : libXext-dev
BuildRequires : libXext-lib
BuildRequires : libXfont2-dev
BuildRequires : libXft-dev
BuildRequires : libXft-lib
BuildRequires : libXi-dev
BuildRequires : libXi-lib
BuildRequires : libXrender-dev
BuildRequires : libXrender-lib
BuildRequires : libXtst-dev
BuildRequires : libXtst-lib
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-dev32
BuildRequires : libXxf86vm-lib
BuildRequires : libarchive
BuildRequires : libarchive-dev
BuildRequires : libarchive-staticdev
BuildRequires : libatomic_ops-dev
BuildRequires : libatomic_ops-staticdev
BuildRequires : libcap
BuildRequires : libcap-dev
BuildRequires : libcap-ng-dev
BuildRequires : libconfig-dev
BuildRequires : libdrm
BuildRequires : libdrm-dev
BuildRequires : libdrm-lib
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libepoxy
BuildRequires : libepoxy-dev
BuildRequires : libffi
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libgcrypt
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error
BuildRequires : libgpg-error-dev
BuildRequires : libidn2
BuildRequires : libidn2-dev
BuildRequires : libidn2-staticdev
BuildRequires : libinput-data
BuildRequires : libinput-dev
BuildRequires : libinput-lib
BuildRequires : libinput-libexec
BuildRequires : libjpeg-turbo-dev
BuildRequires : libogg
BuildRequires : libogg-dev
BuildRequires : libpciaccess
BuildRequires : libpciaccess-dev
BuildRequires : libplacebo
BuildRequires : libplacebo-dev
BuildRequires : libpng-dev
BuildRequires : libpng-lib
BuildRequires : libsamplerate-dev
BuildRequires : libsamplerate-dev32
BuildRequires : libsamplerate-staticdev
BuildRequires : libsamplerate-staticdev32
BuildRequires : libstdc++
BuildRequires : libstdc++-dev
BuildRequires : libtasn1-dev
BuildRequires : libunistring-dev
BuildRequires : libunistring-staticdev
BuildRequires : libunwind
BuildRequires : libunwind-dev
BuildRequires : libunwind-dev32
BuildRequires : libusb
BuildRequires : libusb-dev
BuildRequires : libusb-dev32
BuildRequires : libva
BuildRequires : libva-dev
BuildRequires : libva-lib
BuildRequires : libvdpau
BuildRequires : libvdpau-dev
BuildRequires : libvorbis
BuildRequires : libvorbis-dev
BuildRequires : libwebp-dev
BuildRequires : libxcb-dev
BuildRequires : libxcb-lib
BuildRequires : libxkbcommon
BuildRequires : libxkbcommon-dev
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : libxslt-bin
BuildRequires : libxvid-staticdev
BuildRequires : libzimg-dev
BuildRequires : libzimg-staticdev
BuildRequires : lz4
BuildRequires : lz4-dev
BuildRequires : lz4-staticdev
BuildRequires : lzo
BuildRequires : lzo-dev
BuildRequires : lzo-staticdev
BuildRequires : md4c
BuildRequires : md4c-dev
BuildRequires : md4c-staticdev
BuildRequires : mediasdk-dev
BuildRequires : mesa
BuildRequires : mesa-demos
BuildRequires : mesa-dev
BuildRequires : mesa-lib
BuildRequires : mm-common-dev
BuildRequires : nasm
BuildRequires : nasm-bin
BuildRequires : ncurses-dev
BuildRequires : nettle
BuildRequires : nettle-dev
BuildRequires : ninja
BuildRequires : not-ffmpeg
BuildRequires : not-ffmpeg-dev
BuildRequires : numlockx
BuildRequires : nvidia
BuildRequires : nvidia-dev
BuildRequires : nvidia-lib
BuildRequires : opencl-headers
BuildRequires : opencl-headers-dev
BuildRequires : openjpeg-dev
BuildRequires : openssl
BuildRequires : openssl-dev
BuildRequires : openssl-lib
BuildRequires : openssl-staticdev
BuildRequires : orc-dev
BuildRequires : orc-staticdev
BuildRequires : p11-kit
BuildRequires : p11-kit-dev
BuildRequires : pacrunner
BuildRequires : pacrunner-dev
BuildRequires : pango-lib
BuildRequires : pcre-dev
BuildRequires : pcre-staticdev
BuildRequires : perl
BuildRequires : perl(XML::Parser)
BuildRequires : perl-Config-General
BuildRequires : perl-Config-Tiny
BuildRequires : perl-Crypt-SSLeay
BuildRequires : perl-DBI
BuildRequires : perl-DateTime-TimeZone
BuildRequires : perl-Encode-Locale
BuildRequires : perl-Error
BuildRequires : perl-File-Listing
BuildRequires : perl-HTML-Parser
BuildRequires : perl-HTML-Tagset
BuildRequires : perl-HTTP-Cookies
BuildRequires : perl-HTTP-Date
BuildRequires : perl-HTTP-Message
BuildRequires : perl-HTTP-Negotiate
BuildRequires : perl-IO-HTML
BuildRequires : perl-LWP-MediaTypes
BuildRequires : perl-LWP-Protocol-https
BuildRequires : perl-Params-Validate
BuildRequires : perl-Test-Simple
BuildRequires : perl-Try-Tiny
BuildRequires : perl-URI
BuildRequires : perl-XML-NamespaceSupport
BuildRequires : perl-XML-Parser
BuildRequires : perl-libwww-perl
BuildRequires : perl-man
BuildRequires : pixman
BuildRequires : pixman-dev
BuildRequires : pixman-lib
BuildRequires : pixman-staticdev
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(alsa-topology)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(dri)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gdm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(glesv1_cm)
BuildRequires : pkgconfig(glesv2)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(glu)
BuildRequires : pkgconfig(gmock)
BuildRequires : pkgconfig(gmock_main)
BuildRequires : pkgconfig(gtest)
BuildRequires : pkgconfig(gtest_main)
BuildRequires : pkgconfig(ice)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libsystemd)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libunwind)
BuildRequires : pkgconfig(libunwind-coredump)
BuildRequires : pkgconfig(libunwind-generic)
BuildRequires : pkgconfig(libunwind-ptrace)
BuildRequires : pkgconfig(libunwind-setjmp)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(osmesa)
BuildRequires : pkgconfig(samplerate)
BuildRequires : pkgconfig(sm)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(vulkan)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xatracker)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xextproto)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xmu)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xpm)
BuildRequires : pkgconfig(xproto)
BuildRequires : pkgconfig(xrandr)
BuildRequires : pkgconfig(xscrnsaver)
BuildRequires : pkgconfig(xt)
BuildRequires : pkgconfig(zlib)
BuildRequires : pulseaudio
BuildRequires : pulseaudio-dev
BuildRequires : python3-core
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : setxkbmap
BuildRequires : shared-mime-info
BuildRequires : snappy-dev
BuildRequires : solid-dev
BuildRequires : sonnet-dev
BuildRequires : sqlite-autoconf
BuildRequires : sqlite-autoconf-dev
BuildRequires : syntax-highlighting
BuildRequires : syntax-highlighting-data
BuildRequires : syntax-highlighting-dev
BuildRequires : syntax-highlighting-lib
BuildRequires : systemd
BuildRequires : systemd-dev
BuildRequires : texinfo
BuildRequires : util-linux
BuildRequires : util-linux-dev
BuildRequires : util-linux-staticdev
BuildRequires : valgrind
BuildRequires : valgrind-dev
BuildRequires : wayland
BuildRequires : wayland-dev
BuildRequires : weston
BuildRequires : wmctrl
BuildRequires : xauth
BuildRequires : xcb-proto
BuildRequires : xcb-proto-dev
BuildRequires : xcb-util-cursor-dev
BuildRequires : xcb-util-dev
BuildRequires : xcb-util-image-dev
BuildRequires : xcb-util-keysyms-dev
BuildRequires : xcb-util-renderutil-dev
BuildRequires : xcb-util-wm-dev
BuildRequires : xcb-util-xrm-dev
BuildRequires : xclip
BuildRequires : xdg-dbus-proxy
BuildRequires : xdg-desktop-portal
BuildRequires : xdg-desktop-portal-dev
BuildRequires : xdg-desktop-portal-gtk
BuildRequires : xdg-desktop-portal-kde
BuildRequires : xdg-user-dirs
BuildRequires : xdg-user-dirs-gtk
BuildRequires : xdg-utils
BuildRequires : xdotool
BuildRequires : xdpyinfo
BuildRequires : xf86-input-libinput
BuildRequires : xf86-video-amdgpu
BuildRequires : xf86-video-ati
BuildRequires : xf86-video-fbdev
BuildRequires : xf86-video-nouveau
BuildRequires : xf86-video-qxl
BuildRequires : xf86-video-vboxvideo
BuildRequires : xf86-video-vesa
BuildRequires : xf86-video-vmware
BuildRequires : xfontsel
BuildRequires : xhost
BuildRequires : xinit
BuildRequires : xinput
BuildRequires : xkbcomp
BuildRequires : xkeyboard-config
BuildRequires : xkill
BuildRequires : xmodmap
BuildRequires : xorg-server
BuildRequires : xorg-server-dev
BuildRequires : xorgproto
BuildRequires : xorgproto-dev
BuildRequires : xprop
BuildRequires : xrandr
BuildRequires : xrdb
BuildRequires : xrdp
BuildRequires : xrestop
BuildRequires : xscreensaver
BuildRequires : xsel
BuildRequires : xset
BuildRequires : xsetroot
BuildRequires : xvfb-run
BuildRequires : xwd
BuildRequires : xwininfo
BuildRequires : xz
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
BuildRequires : zstd-dev
BuildRequires : zstd-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the SDL2 package.
Group: Binaries

%description bin
bin components for the SDL2 package.


%package dev
Summary: dev components for the SDL2 package.
Group: Development
Requires: SDL2-lib = %{version}-%{release}
Requires: SDL2-bin = %{version}-%{release}
Provides: SDL2-devel = %{version}-%{release}
Requires: SDL2 = %{version}-%{release}

%description dev
dev components for the SDL2 package.


%package lib
Summary: lib components for the SDL2 package.
Group: Libraries

%description lib
lib components for the SDL2 package.


%package staticdev
Summary: staticdev components for the SDL2 package.
Group: Default
Requires: SDL2-dev = %{version}-%{release}

%description staticdev
staticdev components for the SDL2 package.


%prep
%setup -q -n SDL2-2.0.14
cd %{_builddir}/SDL2-2.0.14

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1620988898
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-DHAVE_OPENGL -DTEST_NATIVE_X11 -DSDL_VIDEO_DRIVER_X11 -g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-DHAVE_OPENGL -DTEST_NATIVE_X11 -DSDL_VIDEO_DRIVER_X11 -g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables -lGL $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common -Wl,--whole-archive /usr/lib64/libsamplerate.a -Wl,--no-whole-archive
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-DHAVE_OPENGL -DTEST_NATIVE_X11 -DSDL_VIDEO_DRIVER_X11 -g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-DHAVE_OPENGL -DTEST_NATIVE_X11 -DSDL_VIDEO_DRIVER_X11 -g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -lGL $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
export DISPLAY=:0
#export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
export LD_LIBRARY_PATH="/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export LIBRARY_PATH="/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:../"
export PATH="/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
%cmake .. -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DSDL_SHARED:BOOL=ON \
-DSDL_STATIC:BOOL=ON \
-DALSA:BOOL=ON \
-DALSA_SHARED:BOOL=OFF \
-DPULSEAUDIO:BOOL=ON \
-DPULSEAUDIO_SHARED:BOOL=OFF \
-DLIBSAMPLERATE:BOOL=ON \
-DLIBSAMPLERATE_SHARED:BOOL=OFF \
-DVIDEO_OPENGL:BOOL=ON \
-DVIDEO_OPENGLES:BOOL=ON \
-DVIDEO_WAYLAND_QT_TOUCH:BOOL=ON \
-DVIDEO_KMSDRM:BOOL=ON \
-DKMSDRM_SHARED:BOOL=OFF \
-DVIDEO_X11:BOOL=ON \
-DX11_SHARED:BOOL=OFF \
-DVIDEO_X11_XCURSOR:BOOL=ON \
-DVIDEO_X11_XINERAMA:BOOL=ON \
-DVIDEO_X11_XINPUT:BOOL=ON \
-DVIDEO_X11_XRANDR:BOOL=ON \
-DVIDEO_X11_XSCRNSAVER:BOOL=ON \
-DVIDEO_X11_XSHAPE:BOOL=ON \
-DVIDEO_X11_XVM:BOOL=ON \
-DBUILD_TOOLS=ON \
-DSDL_DLOPEN:BOOL=ON \
-DVIDEO_VULKAN:BOOL=ON \
-DSDL_VIDEO_VULKAN:BOOL=ON \
-DJACK:BOOL=OFF \
-DJACK_SHARED:BOOL=OFF \
-DASSEMBLY:BOOL=ON \
-DSSEMATH:BOOL=ON \
-DVIDEO_WAYLAND:BOOL=ON \
-DPTHREADS:BOOL=ON \
-DASSERTIONS=disabled \
-DSSE3:BOOL=ON \
-DSSEMATH:BOOL=ON \
-D3DNOW:BOOL=OFF \
-DMMX:BOOL=OFF \
-DRPATH:BOOL=ON \
-DSDL_TEST:BOOL=ON
## make_prepend content
sd "/usr/lib64/libsamplerate.a" -- "-Wl,--whole-archive /usr/lib64/libsamplerate.a -Wl,--no-whole-archive" $(fd -uu link.txt)
sd "\-lsamplerate" -- "-Wl,--whole-archive /usr/lib64/libsamplerate.a -Wl,--no-whole-archive" $(fd -uu link.txt)
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 V=1 VERBOSE=1
## ccache stats
ccache -s
## ccache stats

pushd test
export DISPLAY=:0
#export __GL_ALLOW_UNOFFICIAL_PROTOCOL=1
export __GL_SYNC_TO_VBLANK=0
export LANG=en_US.UTF-8
export XDG_CONFIG_DIRS=/usr/share/xdg:/etc/xdg
export XDG_SEAT=seat0
export XDG_SESSION_TYPE=tty
export XDG_CURRENT_DESKTOP=KDE
export XDG_SESSION_CLASS=user
export XDG_VTNR=1
export XDG_SESSION_ID=1
export XDG_RUNTIME_DIR=/run/user/1000
export XDG_DATA_DIRS=/usr/local/share:/usr/share
export KDE_SESSION_VERSION=5
export KDE_SESSION_UID=1000
export KDE_FULL_SESSION=true
export KDE_APPLICATIONS_AS_SCOPE=1
export VDPAU_DRIVER=nvidia
export LIBVA_DRIVER_NAME=vdpau
export LIBVA_DRIVERS_PATH=/usr/lib64/dri
export GTK_RC_FILES=/etc/gtk/gtkrc
export FONTCONFIG_PATH=/usr/share/defaults/fonts
export LD_LIBRARY_PATH="/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export LIBRARY_PATH="/usr/cuda/lib64:/usr/cuda/targets/x86_64-linux/lib:/usr/nvidia/lib64:/usr/nvidia/lib:/usr/nvidia/lib/vdpau:/usr/nvidia/lib64/xorg/modules/drivers:/usr/nvidia/lib64/xorg/modules/extensions:/usr/lib64/dri:/usr/lib64/haswell:/usr/lib64:/usr/lib:/usr/share"
export PKG_CONFIG_PATH="/usr/lib64/pkgconfig:../"
export PATH="/usr/nvidia/bin:/usr/bin/haswell:/usr/bin:/usr/sbin"
export $(dbus-launch)
./testautomation || :
timeout 6 ./testdraw2 || :
timeout 6 ./testsprite2 || :
timeout 6 ./testgles2 || :
timeout 6 ./testgl2 || :
timeout 6 ./testshader || :
timeout 6 ./testvulkan || :
timeout 6 ./testnative || :
./testmultiaudio || :
./checkkeys || :
timeout 6 ./loopwave || :
timeout 6 ./loopwavequeue || :
./testaudioinfo || :
./testerror || :
./testfile || :
./testiconv || :
./testkeys || :
timeout 6 ./testoverlay2 || :
./testplatform || :
./testsem || :
./testshape ../../test/shapes/trollface_32alpha.bmp ../../test/shapes/trollface_24.bmp ../../test/shapes/p16_shape24.bmp ../../test/shapes/p16_shape8.bmp ../../test/shapes/p16_shape1.bmp ../../test/shapes/p15_shape32alpha.bmp ../../test/shapes/p15_shape24.bmp ../../test/shapes/p15_shape8.bmp ../../test/shapes/p14_shape24.bmp ../../test/shapes/p14_shape8.bmp ../../test/shapes/p13_shape32alpha.bmp ../../test/shapes/p13_shape24.bmp ../../test/shapes/p13_shape8.bmp ../../test/shapes/p12_shape24.bmp ../../test/shapes/p12_shape8.bmp ../../test/shapes/p11_shape32alpha.bmp ../../test/shapes/p11_shape24.bmp ../../test/shapes/p11_shape8.bmp ../../test/shapes/p10_shape32alpha.bmp ../../test/shapes/p10_shape24.bmp ../../test/shapes/p10_shape8.bmp ../../test/shapes/p10_shape1.bmp ../../test/shapes/p09_shape32alpha.bmp ../../test/shapes/p09_shape24.bmp ../../test/shapes/p09_shape8.bmp ../../test/shapes/p08_shape32alpha.bmp ../../test/shapes/p08_shape24.bmp ../../test/shapes/p08_shape8.bmp ../../test/shapes/p07_shape32alpha.bmp ../../test/shapes/p07_shape24.bmp ../../test/shapes/p07_shape8.bmp ../../test/shapes/p06_shape32alpha.bmp ../../test/shapes/p06_shape24.bmp ../../test/shapes/p06_shape8.bmp ../../test/shapes/p06_shape1alpha.bmp ../../test/shapes/p05_shape8.bmp ../../test/shapes/p04_shape32alpha.bmp ../../test/shapes/p04_shape24.bmp ../../test/shapes/p04_shape8.bmp ../../test/shapes/p04_shape1.bmp ../../test/shapes/p03_shape24.bmp ../../test/shapes/p03_shape8.bmp ../../test/shapes/p02_shape32alpha.bmp ../../test/shapes/p02_shape24.bmp ../../test/shapes/p02_shape8.bmp ../../test/shapes/p01_shape32alpha.bmp ../../test/shapes/p01_shape24.bmp ../../test/shapes/p01_shape8.bmp || :
./testthread || :
./testtimer || :
./torturethread || :
glxinfo ||:
popd
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
%cmake .. -DCMAKE_BUILD_TYPE=Release \
-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
-DSDL_SHARED:BOOL=ON \
-DSDL_STATIC:BOOL=ON \
-DALSA:BOOL=ON \
-DALSA_SHARED:BOOL=OFF \
-DPULSEAUDIO:BOOL=ON \
-DPULSEAUDIO_SHARED:BOOL=OFF \
-DLIBSAMPLERATE:BOOL=ON \
-DLIBSAMPLERATE_SHARED:BOOL=OFF \
-DVIDEO_OPENGL:BOOL=ON \
-DVIDEO_OPENGLES:BOOL=ON \
-DVIDEO_WAYLAND_QT_TOUCH:BOOL=ON \
-DVIDEO_KMSDRM:BOOL=ON \
-DKMSDRM_SHARED:BOOL=OFF \
-DVIDEO_X11:BOOL=ON \
-DX11_SHARED:BOOL=OFF \
-DVIDEO_X11_XCURSOR:BOOL=ON \
-DVIDEO_X11_XINERAMA:BOOL=ON \
-DVIDEO_X11_XINPUT:BOOL=ON \
-DVIDEO_X11_XRANDR:BOOL=ON \
-DVIDEO_X11_XSCRNSAVER:BOOL=ON \
-DVIDEO_X11_XSHAPE:BOOL=ON \
-DVIDEO_X11_XVM:BOOL=ON \
-DBUILD_TOOLS=ON \
-DSDL_DLOPEN:BOOL=ON \
-DVIDEO_VULKAN:BOOL=ON \
-DSDL_VIDEO_VULKAN:BOOL=ON \
-DJACK:BOOL=OFF \
-DJACK_SHARED:BOOL=OFF \
-DASSEMBLY:BOOL=ON \
-DSSEMATH:BOOL=ON \
-DVIDEO_WAYLAND:BOOL=ON \
-DPTHREADS:BOOL=ON \
-DASSERTIONS=disabled \
-DSSE3:BOOL=ON \
-DSSEMATH:BOOL=ON \
-D3DNOW:BOOL=OFF \
-DMMX:BOOL=OFF \
-DRPATH:BOOL=ON \
-DSDL_TEST:BOOL=OFF
## make_prepend content
sd "/usr/lib64/libsamplerate.a" -- "-Wl,--whole-archive /usr/lib64/libsamplerate.a -Wl,--no-whole-archive" $(fd -uu link.txt)
sd "\-lsamplerate" -- "-Wl,--whole-archive /usr/lib64/libsamplerate.a -Wl,--no-whole-archive" $(fd -uu link.txt)
## make_prepend end
make  %{?_smp_mflags}  V=1 VERBOSE=1 V=1 VERBOSE=1
## ccache stats
ccache -s
## ccache stats
fi
popd

%install
export SOURCE_DATE_EPOCH=1620988898
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sdl2-config

%files dev
%defattr(-,root,root,-)
/usr/include/SDL2/SDL.h
/usr/include/SDL2/SDL_assert.h
/usr/include/SDL2/SDL_atomic.h
/usr/include/SDL2/SDL_audio.h
/usr/include/SDL2/SDL_bits.h
/usr/include/SDL2/SDL_blendmode.h
/usr/include/SDL2/SDL_clipboard.h
/usr/include/SDL2/SDL_config.h
/usr/include/SDL2/SDL_config_android.h
/usr/include/SDL2/SDL_config_iphoneos.h
/usr/include/SDL2/SDL_config_macosx.h
/usr/include/SDL2/SDL_config_minimal.h
/usr/include/SDL2/SDL_config_os2.h
/usr/include/SDL2/SDL_config_pandora.h
/usr/include/SDL2/SDL_config_psp.h
/usr/include/SDL2/SDL_config_windows.h
/usr/include/SDL2/SDL_config_winrt.h
/usr/include/SDL2/SDL_config_wiz.h
/usr/include/SDL2/SDL_copying.h
/usr/include/SDL2/SDL_cpuinfo.h
/usr/include/SDL2/SDL_egl.h
/usr/include/SDL2/SDL_endian.h
/usr/include/SDL2/SDL_error.h
/usr/include/SDL2/SDL_events.h
/usr/include/SDL2/SDL_filesystem.h
/usr/include/SDL2/SDL_gamecontroller.h
/usr/include/SDL2/SDL_gesture.h
/usr/include/SDL2/SDL_haptic.h
/usr/include/SDL2/SDL_hints.h
/usr/include/SDL2/SDL_joystick.h
/usr/include/SDL2/SDL_keyboard.h
/usr/include/SDL2/SDL_keycode.h
/usr/include/SDL2/SDL_loadso.h
/usr/include/SDL2/SDL_locale.h
/usr/include/SDL2/SDL_log.h
/usr/include/SDL2/SDL_main.h
/usr/include/SDL2/SDL_messagebox.h
/usr/include/SDL2/SDL_metal.h
/usr/include/SDL2/SDL_misc.h
/usr/include/SDL2/SDL_mouse.h
/usr/include/SDL2/SDL_mutex.h
/usr/include/SDL2/SDL_name.h
/usr/include/SDL2/SDL_opengl.h
/usr/include/SDL2/SDL_opengl_glext.h
/usr/include/SDL2/SDL_opengles.h
/usr/include/SDL2/SDL_opengles2.h
/usr/include/SDL2/SDL_opengles2_gl2.h
/usr/include/SDL2/SDL_opengles2_gl2ext.h
/usr/include/SDL2/SDL_opengles2_gl2platform.h
/usr/include/SDL2/SDL_opengles2_khrplatform.h
/usr/include/SDL2/SDL_pixels.h
/usr/include/SDL2/SDL_platform.h
/usr/include/SDL2/SDL_power.h
/usr/include/SDL2/SDL_quit.h
/usr/include/SDL2/SDL_rect.h
/usr/include/SDL2/SDL_render.h
/usr/include/SDL2/SDL_revision.h
/usr/include/SDL2/SDL_rwops.h
/usr/include/SDL2/SDL_scancode.h
/usr/include/SDL2/SDL_sensor.h
/usr/include/SDL2/SDL_shape.h
/usr/include/SDL2/SDL_stdinc.h
/usr/include/SDL2/SDL_surface.h
/usr/include/SDL2/SDL_system.h
/usr/include/SDL2/SDL_syswm.h
/usr/include/SDL2/SDL_test.h
/usr/include/SDL2/SDL_test_assert.h
/usr/include/SDL2/SDL_test_common.h
/usr/include/SDL2/SDL_test_compare.h
/usr/include/SDL2/SDL_test_crc32.h
/usr/include/SDL2/SDL_test_font.h
/usr/include/SDL2/SDL_test_fuzzer.h
/usr/include/SDL2/SDL_test_harness.h
/usr/include/SDL2/SDL_test_images.h
/usr/include/SDL2/SDL_test_log.h
/usr/include/SDL2/SDL_test_md5.h
/usr/include/SDL2/SDL_test_memory.h
/usr/include/SDL2/SDL_test_random.h
/usr/include/SDL2/SDL_thread.h
/usr/include/SDL2/SDL_timer.h
/usr/include/SDL2/SDL_touch.h
/usr/include/SDL2/SDL_types.h
/usr/include/SDL2/SDL_version.h
/usr/include/SDL2/SDL_video.h
/usr/include/SDL2/SDL_vulkan.h
/usr/include/SDL2/begin_code.h
/usr/include/SDL2/close_code.h
/usr/lib64/cmake/SDL2/SDL2Config.cmake
/usr/lib64/cmake/SDL2/SDL2ConfigVersion.cmake
/usr/lib64/cmake/SDL2/SDL2Targets-release.cmake
/usr/lib64/cmake/SDL2/SDL2Targets.cmake
/usr/lib64/libSDL2-2.0.so
/usr/lib64/libSDL2.so
/usr/lib64/pkgconfig/sdl2.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2-2.0.so.0
/usr/lib64/libSDL2-2.0.so.0.14.0

%files staticdev
%defattr(-,root,root,-)
/usr/lib64/libSDL2.a
/usr/lib64/libSDL2main.a
