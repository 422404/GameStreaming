#!/bin/sh
sudo docker run -it --rm --network game-streaming-net -v /etc/localtime:/etc/localtime:ro -v /etc/timezone:/etc/timezone:ro -v $(pwd)/app:/opt/app:rw --name game-streaming-frontend http-server:1.0 bash
