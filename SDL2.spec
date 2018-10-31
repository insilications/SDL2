#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x30A59377A7763BE6 (slouken@libsdl.org)
#
Name     : SDL2
Version  : 2.0.9
Release  : 24
URL      : https://www.libsdl.org/release/SDL2-2.0.9.tar.gz
Source0  : https://www.libsdl.org/release/SDL2-2.0.9.tar.gz
Source99 : https://www.libsdl.org/release/SDL2-2.0.9.tar.gz.sig
Summary  : Simple DirectMedia Layer
Group    : Development/Tools
License  : BSD-3-Clause BSD-4-Clause-UC CPL-1.0 GPL-3.0 ISC MIT Zlib
Requires: SDL2-bin = %{version}-%{release}
Requires: SDL2-lib = %{version}-%{release}
Requires: SDL2-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-qmake
BuildRequires : libXxf86vm-dev
BuildRequires : libXxf86vm-dev32
BuildRequires : mesa-dev
BuildRequires : pkgconfig(32alsa)
BuildRequires : pkgconfig(32dbus-1)
BuildRequires : pkgconfig(32gl)
BuildRequires : pkgconfig(32libpulse-simple)
BuildRequires : pkgconfig(32libusb-1.0)
BuildRequires : pkgconfig(32wayland-protocols)
BuildRequires : pkgconfig(32x11)
BuildRequires : pkgconfig(32xcursor)
BuildRequires : pkgconfig(32xext)
BuildRequires : pkgconfig(32xi)
BuildRequires : pkgconfig(32xinerama)
BuildRequires : pkgconfig(32xkbcommon)
BuildRequires : pkgconfig(32xrandr)
BuildRequires : pkgconfig(alsa)
BuildRequires : pkgconfig(dbus-1)
BuildRequires : pkgconfig(egl)
BuildRequires : pkgconfig(gbm)
BuildRequires : pkgconfig(gl)
BuildRequires : pkgconfig(libdrm)
BuildRequires : pkgconfig(libpulse-simple)
BuildRequires : pkgconfig(libudev)
BuildRequires : pkgconfig(libusb-1.0)
BuildRequires : pkgconfig(wayland-client)
BuildRequires : pkgconfig(wayland-cursor)
BuildRequires : pkgconfig(wayland-egl)
BuildRequires : pkgconfig(wayland-protocols)
BuildRequires : pkgconfig(wayland-scanner)
BuildRequires : pkgconfig(x11)
BuildRequires : pkgconfig(xcursor)
BuildRequires : pkgconfig(xext)
BuildRequires : pkgconfig(xi)
BuildRequires : pkgconfig(xinerama)
BuildRequires : pkgconfig(xkbcommon)
BuildRequires : pkgconfig(xrandr)

%description
This is the Simple DirectMedia Layer, a generic API that provides low
level access to audio, keyboard, mouse, and display framebuffer across
multiple platforms.

%package bin
Summary: bin components for the SDL2 package.
Group: Binaries
Requires: SDL2-license = %{version}-%{release}

%description bin
bin components for the SDL2 package.


%package dev
Summary: dev components for the SDL2 package.
Group: Development
Requires: SDL2-lib = %{version}-%{release}
Requires: SDL2-bin = %{version}-%{release}
Provides: SDL2-devel = %{version}-%{release}

%description dev
dev components for the SDL2 package.


%package lib
Summary: lib components for the SDL2 package.
Group: Libraries
Requires: SDL2-license = %{version}-%{release}

%description lib
lib components for the SDL2 package.


%package license
Summary: license components for the SDL2 package.
Group: Default

%description license
license components for the SDL2 package.


%prep
%setup -q -n SDL2-2.0.9

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1541010290
mkdir -p clr-build
pushd clr-build
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake .. -DSDL_SHARED=ON -DALSA_SHARED=ON -DX11_SHARED=ON
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1541010290
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/SDL2
cp COPYING.txt %{buildroot}/usr/share/package-licenses/SDL2/COPYING.txt
cp Xcode-iOS/Demos/data/bitmapfont/license.txt %{buildroot}/usr/share/package-licenses/SDL2/Xcode-iOS_Demos_data_bitmapfont_license.txt
cp Xcode/SDL/pkg-support/resources/License.txt %{buildroot}/usr/share/package-licenses/SDL2/Xcode_SDL_pkg-support_resources_License.txt
cp debian/copyright %{buildroot}/usr/share/package-licenses/SDL2/debian_copyright
cp src/hidapi/LICENSE-bsd.txt %{buildroot}/usr/share/package-licenses/SDL2/src_hidapi_LICENSE-bsd.txt
cp src/hidapi/LICENSE-gpl3.txt %{buildroot}/usr/share/package-licenses/SDL2/src_hidapi_LICENSE-gpl3.txt
cp src/hidapi/LICENSE-orig.txt %{buildroot}/usr/share/package-licenses/SDL2/src_hidapi_LICENSE-orig.txt
cp src/video/yuv2rgb/LICENSE %{buildroot}/usr/share/package-licenses/SDL2/src_video_yuv2rgb_LICENSE
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
/usr/include/SDL2/SDL_log.h
/usr/include/SDL2/SDL_main.h
/usr/include/SDL2/SDL_messagebox.h
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
/usr/lib/cmake/SDL2/SDL2Config.cmake
/usr/lib/cmake/SDL2/SDL2ConfigVersion.cmake
/usr/lib/cmake/SDL2/SDL2Targets-relwithdebinfo.cmake
/usr/lib/cmake/SDL2/SDL2Targets.cmake
/usr/lib64/libSDL2-2.0.so
/usr/lib64/libSDL2.so
/usr/lib64/pkgconfig/sdl2.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libSDL2-2.0.so.0
/usr/lib64/libSDL2-2.0.so.0.9.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/SDL2/COPYING.txt
/usr/share/package-licenses/SDL2/Xcode-iOS_Demos_data_bitmapfont_license.txt
/usr/share/package-licenses/SDL2/Xcode_SDL_pkg-support_resources_License.txt
/usr/share/package-licenses/SDL2/debian_copyright
/usr/share/package-licenses/SDL2/src_hidapi_LICENSE-bsd.txt
/usr/share/package-licenses/SDL2/src_hidapi_LICENSE-gpl3.txt
/usr/share/package-licenses/SDL2/src_hidapi_LICENSE-orig.txt
/usr/share/package-licenses/SDL2/src_video_yuv2rgb_LICENSE
