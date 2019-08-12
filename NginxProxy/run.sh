#!/bin/sh
sudo docker run -d --rm --network game-streaming-net -p 8000:80 -v $(pwd)/app:/opt/app:ro --name game-streaming-proxy nginx-proxy:1.0
