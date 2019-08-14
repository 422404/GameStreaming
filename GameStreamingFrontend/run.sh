#!/bin/sh
sudo docker run -d --rm --network game-streaming-net -p 8000:80 -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/app:/opt/app:rw --name game-streaming-frontend game-streaming-frontend:1.0
