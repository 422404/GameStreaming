#!/bin/sh
sudo docker run --device /dev/snd -it --rm -p 8000:8000 -p 8001:8001 -v $(pwd)/app:/opt/app:ro --name test game-container:1.0 bash
