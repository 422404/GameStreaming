FROM ubuntu:18.04

# Port 8000 is used to stream video
# Port 8001 is for receiving game inputs
EXPOSE 8000 8001

# Avoid user input during installs
ENV DEBIAN_FRONTEND=noninteractive
# Tell the game which server uses xvfb
ENV DISPLAY=:0

################################
# Misc. downloads and installs #
################################

# Download needed tools
RUN apt update && apt install -y \
    wget \
    git \
    # Virtual screen
    xvfb \
    # For Supervisord
    python \
    python-pip \
    python3 \
    python3-pip \
    # Enables screen recording and streaming
    ffmpeg \
# Supervisord will launch NGINX and GameSupervisor
 && pip install supervisor

###############################################################
# Compile NGINX from sources with RTMP streaming module added #
###############################################################

# Install NGINX dependencies
RUN apt install -y \
    # Bundles gcc and make
    build-essential \
    libpcre3 \
    libpcre3-dev \
    libssl-dev \
    zlib1g-dev \
# This module will enable streaming out of the container
 && git clone https://github.com/sergey-dryabzhinsky/nginx-rtmp-module.git \
# Actually donwload NGINX sources
 && wget http://nginx.org/download/nginx-1.15.12.tar.gz \
 && tar -xf nginx-1.15.12.tar.gz \
 && cd nginx-1.15.12 \
# Build with RTMP streaming module added
 && ./configure --with-http_ssl_module --add-module=../nginx-rtmp-module \
 && make -j 1 \
 && make install

# Test
RUN apt install -y firefox

CMD ["supervisord", "-c", "/opt/app/supervisord/supervisord.conf"]
