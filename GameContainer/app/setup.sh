#!/bin/bash

mkdir /etc/nginx
cp ./nginx/stream.conf /etc/nginx/nginx.conf
mkdir /mnt/test
cp ./test.html /mnt/test/
supervisorctl start nginx
supervisorctl start ffmpeg

# Test
firefox &

sleep 1
