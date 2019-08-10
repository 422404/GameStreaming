#!/bin/sh
# Start the pulseaudio server
pulseaudio -D --exit-idle-time=-1

# Load the virtual sink and set it as default
pacmd load-module module-virtual-sink sink_name=snd_sink
pacmd set-default-sink snd_sink

# set the monitor of snd_sink sink to be the default source
pacmd set-default-source snd_sink.monitor
