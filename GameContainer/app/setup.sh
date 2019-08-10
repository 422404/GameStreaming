#!/bin/sh

cp /opt/app/nginx/nginx.conf /etc/nginx/nginx.conf
rm /usr/local/janus/etc/janus/*
cp /opt/app/janus/janus.jcfg /usr/local/janus/etc/janus/janus.jcfg
cp /opt/app/janus/janus.plugin.streaming.jcfg /usr/local/janus/etc/janus/janus.plugin.streaming.jcfg
cp /opt/app/janus/janus.transport.websockets.jcfg /usr/local/janus/etc/janus/janus.transport.websockets.jcfg
mkdir -p /var/log/janus
mkdir /tmp/janus

# Test
# firefox &

while true
do
    sleep 1
done
