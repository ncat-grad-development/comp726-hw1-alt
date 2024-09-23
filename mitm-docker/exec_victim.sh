#!/bin/bash

echo "accessing shell of victim..."
docker exec -it victim bash -c "cd /home/ubuntu && bash"
