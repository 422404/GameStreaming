#!/bin/sh
sudo docker run -d --rm --network game-streaming-net -p 5432:5432 -v $(pwd)/postgres_data:/var/lib/postgresql/data:rw --name game-streaming-db game-streaming-db:1.0
