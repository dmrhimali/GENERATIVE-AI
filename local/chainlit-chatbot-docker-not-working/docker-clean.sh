#!/bin/bash
echo "Cleaning all containers and images!"
docker rm -vf $(docker ps -a)
docker rmi -f $(docker images -aq)
echo "Cleaning all containers and images completed!"