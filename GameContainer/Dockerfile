FROM ubuntu:18.04

# Port 8000 is used to stream video
# Port 8001 is for receiving game inputs
EXPOSE 8000 8001

# Avoid user input during installs
ENV DEBIAN_FRONTEND=noninteractive
# Tell the game which server uses xvfb
ENV DISPLAY=:0

# Download base tools
RUN apt update && apt install -y \
    git \
    xvfb \
    nginx \
    pulseaudio \
    socat \
    alsa-utils \
    ffmpeg

# Download and compile Janus
RUN apt install -y \
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
    cmake \
    # Build libnice first
    && git clone https://gitlab.freedesktop.org/libnice/libnice.git \
    && cd libnice \
    # Turn it into release because cast-align warnings turn into errors on pre-release
    && sed -i 's/^LIBNICE_RELEASE=\"no\"/LIBNICE_RELEASE=\"yes\"/' ./configure.ac \
    && sh autogen.sh \
    && ./configure --prefix=/usr/local \
    && make \
    && make install \
    && cd .. \
    # Build libwebsockets
    && git clone https://libwebsockets.org/repo/libwebsockets \
    && cd libwebsockets \
    && mkdir build \
    && cd build \
    && cmake -DLWS_MAX_SMP=1 -DCMAKE_INSTALL_PREFIX:PATH=/usr -DCMAKE_C_FLAGS="-fpic" .. \
    && make \
    && make install \
    && cd ../.. \
    # Build janus
    && git clone https://github.com/meetecho/janus-gateway.git \
    && cd janus-gateway \
    && sh autogen.sh \
    && ./configure --prefix=/usr/local/janus \
    && make \
    && make install \
    && make configs

# Tests
RUN apt install -y firefox vim

CMD ["sh /opt/app/setup.sh"]
