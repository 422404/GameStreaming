#!/bin/sh
sudo docker rmi $(sudo docker images -f dangling=true -q)