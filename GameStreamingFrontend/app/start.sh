#!/bin/sh
cp nginx.conf /etc/nginx/
/usr/sbin/nginx || exit 1

while :
do
    sh ./start-server.sh
done
