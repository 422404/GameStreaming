#!/bin/sh
cp nginx.conf /etc/nginx/
/usr/sbin/nginx

cd game_streaming
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
python3 manage.py runserver 0.0.0.0:8080
