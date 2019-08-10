#!/bin/sh
ffmpeg -f x11grab -s 640x480 -r 30 -i :0.0 -c:v libvpx -b:v 800k -an -deadline realtime -f rtp rtp://127.0.0.1:5004 &
ffmpeg -f alsa -ac 2 -i default -c:a libopus -vn  -f rtp rtp://127.0.0.1:5002 &
