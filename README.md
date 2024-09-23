

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
Verify that you have Git installed.
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

### Step 3: Docker Compose Up
Run the following command from terminal:
```bash
docker-compose up -d --build
```

### Step 4: Gather Network Infomation
Run the following command. Take note of each IP address

./get_network_information.sh


### Step 5: Access You Victim and Attacker Containers
From local terminal session run the following:
```bash
docker exec -it victim bash -c "cd /home/ubuntu && bash"
```
From another terminal session run the following:
```bash
docker exec -it attacker bash -c "cd /home/ubuntu && bash"
```


This will start two containers: `victim` and `attacker`, both connected through a common network.

### Step 6: Launch the Attack
To launch the MITM attack, follow these steps:

1. Open a terminal window for the victim container and run the following:
   ```bash
   ./victim_browsing.sh
   ```

2. Run the MITM Python script inside the attacker container. The script will prompt you to enter the victim's IP and the gateway IP.

   
   ```bash
   python3 mitm_script.py
   ```


   This will initiate the ARP spoofing attack.



### Step 9: Clean Up
When you are done with the lab, you can stop and remove the Docker containers by running:

```bash
docker-compose down
```

## Conclusion
In this lab, you successfully simulated a Man-in-the-Middle attack using Docker and Docker Compose. You learned how ARP spoofing works and used `tcpdump` to analyze the network traffic.

