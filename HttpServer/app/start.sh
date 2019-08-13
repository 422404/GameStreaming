#!/bin/sh
cd /opt/app/game_streaming_frontend
python3 manage.py migrate --no-input
python3 manage.py collectstatic --no-input
python3 manage.py runserver 0.0.0.0:80
