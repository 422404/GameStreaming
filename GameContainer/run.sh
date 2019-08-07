sudo docker run -it --rm -p 8000:8000 -p 8001:8001 -v $(pwd)/app:/opt/app:ro --name test mc-container:0.1 bash
