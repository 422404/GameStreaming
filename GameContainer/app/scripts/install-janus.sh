#!/bin/sh
apt install -y \
    libmicrohttpd-dev \
    libjansson-dev \
	libssl-dev \
    libsrtp2-dev \
    libglib2.0-dev \
	libconfig-dev \
    pkg-config \
    gengetopt \
    libtool \
    automake \
    gtk-doc-tools \
    cmake

git clone https://gitlab.freedesktop.org/libnice/libnice
cd libnice
# turn it into release because cast-align warnings turn into errors on pre-release
sed -i 's/^LIBNICE_RELEASE=\"no\"/LIBNICE_RELEASE=\"yes\"/' ./configure.ac
sh autogen.sh
./configure --prefix=/usr/local
make
make install
cd ..

git clone https://libwebsockets.org/repo/libwebsockets
cd libwebsockets
# If you want the stable version of libwebsockets, uncomment the next line
# git checkout v2.4-stable
mkdir build
cd build
# See https://github.com/meetecho/janus-gateway/issues/732 re: LWS_MAX_SMP
cmake -DLWS_MAX_SMP=1 -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_C_FLAGS="-fpic" ..
make && sudo make install
cd ../..

git clone https://github.com/meetecho/janus-gateway.git
cd janus-gateway
sh autogen.sh
./configure --prefix=/usr/local/janus
make
make install
make configs
