#!/bin/bash
./get_network_info.sh

echo "accessing shell of attacker..."
docker exec -it attacker bash -c "cd /home/ubuntu && bash"
echo ""
echo ""
echo ""
