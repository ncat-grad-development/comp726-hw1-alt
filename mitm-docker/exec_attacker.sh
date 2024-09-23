#!/bin/bash
echo "accessing shell of attacker..."
docker exec -it attacker bash -c "cd /home/ubuntu && bash"
