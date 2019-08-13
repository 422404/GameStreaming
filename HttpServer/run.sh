#!/bin/sh
sudo docker run -d --rm --network game-streaming-net -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/app:/opt/app:rw --name game-streaming-frontend http-server:1.0
