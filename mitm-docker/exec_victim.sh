#!/bin/bash


./get_network_info.sh

echo "accessing shell of victim..."
docker exec -it victim bash -c "cd /home/ubuntu && bash"
echo "" 
echo ""
echo ""
