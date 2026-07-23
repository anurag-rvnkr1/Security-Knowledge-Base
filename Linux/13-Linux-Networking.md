# 13 - Linux Networking

# Part 1 — Networking Fundamentals, OSI Model, TCP/IP Model, IP Addressing, Subnetting, and Network Architecture

---

# Introduction

Networking is the foundation of modern computing.

Every Linux server communicates with other systems through networks, whether it is:

- A web server serving users
- A database communicating with an application
- A cloud virtual machine
- A Kubernetes cluster
- A SIEM collecting logs
- An SSH server
- A DNS server
- A firewall
- An endpoint detection agent

Understanding networking is essential for:

- Linux Administration
- DevOps
- Cloud Computing
- Cybersecurity
- SOC Operations
- Incident Response
- Digital Forensics

---

# Learning Objectives

After completing this chapter, you will understand:

- Networking fundamentals
- OSI model
- TCP/IP model
- IP addressing
- Subnetting
- Network communication
- Enterprise network architecture
- Cybersecurity considerations

---

# What is a Computer Network?

A **computer network** is a collection of devices connected together to exchange data.

Examples of connected devices include:

- Servers
- Workstations
- Laptops
- Smartphones
- Routers
- Switches
- Firewalls
- Printers
- IoT devices

---

# Why Networks Exist

Networks enable:

- Communication
- Resource sharing
- Internet access
- Centralized management
- Remote administration
- Distributed applications
- Cloud computing
- Security monitoring

---

# Enterprise Network Example

```text
Internet

        │

        ▼

Firewall

        │

        ▼

Core Switch

   ┌────┴────┐

   ▼         ▼

Web Server  Database

   │

   ▼

Employees
```

---

# Types of Networks

| Network | Description |
|----------|-------------|
| PAN | Personal Area Network |
| LAN | Local Area Network |
| WLAN | Wireless Local Area Network |
| MAN | Metropolitan Area Network |
| WAN | Wide Area Network |
| VPN | Virtual Private Network |

---

# Local Area Network (LAN)

A LAN connects devices within a limited geographical area.

Examples:

- Office
- School
- Home
- Laboratory

Characteristics:

- High speed
- Low latency
- Privately managed

---

# Wide Area Network (WAN)

A WAN connects geographically separated networks.

Examples:

- Corporate branches
- Internet connectivity
- Cloud regions

Characteristics:

- Larger coverage
- Higher latency
- Uses service providers

---

# Virtual Private Network (VPN)

A VPN creates an encrypted connection across an untrusted network.

Benefits:

- Confidentiality
- Secure remote access
- Traffic protection
- Privacy

---

# Basic Network Components

```text
Computer

↓

Switch

↓

Router

↓

Firewall

↓

Internet
```

---

# Common Networking Devices

| Device | Function |
|----------|----------|
| Hub | Broadcasts traffic to all ports |
| Switch | Forwards frames based on MAC addresses |
| Router | Routes packets between networks |
| Firewall | Filters and controls network traffic |
| Wireless Access Point | Provides Wi-Fi connectivity |
| Load Balancer | Distributes traffic across servers |

---

# Network Communication

Communication occurs through:

```text
Application

↓

Operating System

↓

Network Stack

↓

Network Interface

↓

Cable / Wireless

↓

Destination
```

---

# Data Encapsulation

As data moves down the networking stack, protocol headers are added.

```text
Application Data

↓

TCP/UDP Segment

↓

IP Packet

↓

Ethernet Frame

↓

Bits on the Wire
```

The receiving host removes these headers in reverse order.

---

# The OSI Model

The **Open Systems Interconnection (OSI)** model describes network communication using seven logical layers.

---

# OSI Layers

```text
7 Application

6 Presentation

5 Session

4 Transport

3 Network

2 Data Link

1 Physical
```

---

# Layer 7 — Application

Responsible for:

- User-facing network services
- Application protocols

Examples:

- HTTP
- HTTPS
- SMTP
- FTP
- SSH
- DNS (application protocol)

---

# Layer 6 — Presentation

Responsible for:

- Data formatting
- Encryption
- Compression
- Character encoding

Examples:

- TLS encryption
- UTF-8 encoding

---

# Layer 5 — Session

Responsible for:

- Session establishment
- Session maintenance
- Session termination

Examples:

- Remote login sessions
- RPC sessions

---

# Layer 4 — Transport

Responsible for:

- End-to-end communication
- Reliability
- Flow control
- Segmentation

Protocols:

- TCP
- UDP

---

# Layer 3 — Network

Responsible for:

- Logical addressing
- Routing
- Packet forwarding

Protocols:

- IPv4
- IPv6
- ICMP

Devices:

- Routers
- Layer 3 switches

---

# Layer 2 — Data Link

Responsible for:

- MAC addressing
- Frame delivery
- Error detection on the local link

Devices:

- Switches
- Bridges

---

# Layer 1 — Physical

Responsible for:

- Electrical signals
- Fiber optics
- Radio transmission
- Physical connectors

Examples:

- Ethernet cable
- Fiber cable
- Wireless radio

---

# OSI Summary Table

| Layer | Name | Example |
|--------|------|----------|
| 7 | Application | HTTP |
| 6 | Presentation | TLS |
| 5 | Session | RPC |
| 4 | Transport | TCP |
| 3 | Network | IP |
| 2 | Data Link | Ethernet |
| 1 | Physical | Cable |

---

# Memory Aid

Top to bottom:

```text
Application

Presentation

Session

Transport

Network

Data Link

Physical
```

Bottom to top:

```text
Please

Do

Not

Throw

Sausage

Pizza

Away
```

(One of several commonly used mnemonics.)

---

# TCP/IP Model

The TCP/IP model is the practical networking model used on modern networks.

---

# TCP/IP Layers

```text
Application

↓

Transport

↓

Internet

↓

Network Access
```

---

# OSI vs TCP/IP

| OSI | TCP/IP |
|------|---------|
| Application | Application |
| Presentation | Application |
| Session | Application |
| Transport | Transport |
| Network | Internet |
| Data Link | Network Access |
| Physical | Network Access |

---

# Why TCP/IP Matters

The TCP/IP suite powers:

- The Internet
- Cloud platforms
- Corporate networks
- Linux networking
- Kubernetes
- VPNs
- DNS
- Email
- SSH

---

# IP Address

An **IP address** uniquely identifies a device on a network.

Example IPv4 address:

```text
192.168.1.10
```

Example IPv6 address:

```text
2001:db8::10
```

---

# IPv4 Structure

IPv4 uses:

```text
32 bits
```

Represented as:

```text
192.168.1.10
```

Four octets:

```text
192

168

1

10
```

Each octet ranges from:

```text
0–255
```

---

# Public vs Private IP Addresses

| Type | Example |
|------|----------|
| Public | Assigned for Internet routing by service providers or organizations |
| Private | `192.168.1.10` |

Private IPv4 ranges:

| Range | CIDR |
|--------|------|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

These ranges are not routable on the public Internet.

---

# Loopback Address

IPv4 loopback:

```text
127.0.0.1
```

Common hostname:

```text
localhost
```

Used for communication with the local machine.

---

# IPv6 Loopback

```text
::1
```

Performs the same function as IPv4 loopback.

---

# Subnet Mask

A subnet mask separates:

```text
Network Portion

↓

Host Portion
```

Example:

```text
255.255.255.0
```

Equivalent CIDR notation:

```text
/24
```

---

# CIDR Notation

Examples:

| CIDR | Subnet Mask |
|------|-------------|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |

---

# Subnet Example

Network:

```text
192.168.1.0/24
```

Typical host range:

```text
192.168.1.1

↓

192.168.1.254
```

Network address:

```text
192.168.1.0
```

Broadcast address (IPv4):

```text
192.168.1.255
```

---

# Why Subnetting?

Subnetting provides:

- Better scalability
- Reduced broadcast traffic
- Improved performance
- Security segmentation
- Efficient address allocation

---

# Enterprise Network Segmentation

```text
Corporate Network

├── HR

├── Finance

├── IT

├── Security

└── Guest Wi-Fi
```

Benefits:

- Isolation
- Reduced attack surface
- Easier policy enforcement
- Improved performance

---

# Cybersecurity Perspective

Network architecture directly affects security.

Security teams rely on:

- Segmentation
- Firewalls
- VLANs
- Access control
- Secure routing
- Network monitoring

Proper segmentation limits lateral movement if an attacker compromises a system.

---

# Business Impact

Well-designed network architecture enables:

- Reliable communication
- High availability
- Scalability
- Efficient troubleshooting
- Secure remote access
- Regulatory compliance
- Business continuity

---

# Enterprise Best Practices

- Use private addressing internally where appropriate.
- Segment networks by business function.
- Document IP address allocations.
- Minimize unnecessary broadcast domains.
- Protect network boundaries with firewalls.
- Use secure remote access solutions such as VPNs.
- Regularly review network architecture and addressing plans.

---

# Key Takeaways

- Networking enables communication between devices and services.
- The OSI model provides a conceptual framework for networking.
- TCP/IP is the practical protocol suite used by Linux and the Internet.
- IP addresses uniquely identify devices.
- Subnetting improves scalability, security, and performance.
- Network segmentation is a foundational enterprise security control.

---


# 13 - Linux Networking

# Part 2 — TCP, UDP, ARP, DNS, DHCP, Routing, Network Interfaces, and Linux Network Configuration

---

# Introduction

After understanding network architecture, the next step is learning **how devices actually communicate**.

Every Linux server continuously exchanges data using networking protocols.

Examples include:

- Web browsing (HTTP/HTTPS)
- SSH remote login
- DNS lookups
- Email
- Cloud APIs
- Kubernetes communication
- Database connections
- SIEM log forwarding

Understanding these protocols is critical for:

- Linux Administration
- DevOps
- SOC Operations
- Penetration Testing
- Incident Response
- Network Engineering

---

# Network Communication Process

```text
Application

↓

TCP / UDP

↓

IP

↓

Ethernet

↓

Switch

↓

Router

↓

Destination Server
```

---

# Transport Layer Protocols

The Transport Layer primarily uses two protocols:

- TCP
- UDP

Both provide communication between applications but are designed for different purposes.

---

# TCP (Transmission Control Protocol)

TCP is a:

- Connection-oriented
- Reliable
- Ordered
- Error-checked protocol

It guarantees delivery of data.

---

# TCP Characteristics

| Feature | Description |
|----------|-------------|
| Reliable | Yes |
| Ordered Delivery | Yes |
| Error Detection | Yes |
| Retransmission | Yes |
| Connection-Oriented | Yes |
| Speed | Moderate |

---

# TCP Three-Way Handshake

Before data transfer begins, TCP establishes a connection.

```text
Client                    Server

SYN --------------------->

      <------------------ SYN-ACK

ACK --------------------->
```

After this process, communication begins.

---

# TCP Connection Termination

```text
FIN --------------------->

      <------------------- ACK

      <------------------- FIN

ACK --------------------->
```

---

# Common TCP Services

| Protocol | Port |
|----------|------|
| SSH | 22 |
| HTTP | 80 |
| HTTPS | 443 |
| FTP | 21 |
| SMTP | 25 |
| IMAP | 143 |
| POP3 | 110 |

---

# UDP (User Datagram Protocol)

UDP is:

- Connectionless
- Fast
- Lightweight
- Best-effort delivery

No guarantee exists that packets arrive.

---

# UDP Characteristics

| Feature | Description |
|----------|-------------|
| Reliable | No |
| Ordered Delivery | No |
| Retransmission | No |
| Speed | Very Fast |
| Connection-Oriented | No |

---

# Common UDP Services

| Protocol | Port |
|----------|------|
| DNS | 53 |
| DHCP | 67/68 |
| NTP | 123 |
| SNMP | 161 |
| TFTP | 69 |

---

# TCP vs UDP

| Feature | TCP | UDP |
|----------|-----|-----|
| Reliable | ✓ | ✗ |
| Fast | Moderate | ✓ |
| Connection | Yes | No |
| Ordered | ✓ | ✗ |
| Error Recovery | ✓ | ✗ |
| Streaming | Limited | Excellent |

---

# When to Use TCP

Choose TCP for:

- SSH
- HTTPS
- Banking
- File transfers
- Email
- Databases

Reliability is more important than speed.

---

# When to Use UDP

Choose UDP for:

- Video streaming
- Voice over IP
- Online gaming
- DNS
- Live broadcasts

Low latency is more important than guaranteed delivery.

---

# Ports

Ports identify applications running on a host.

Example:

```text
192.168.1.20

↓

Port 22 → SSH

Port 80 → HTTP

Port 443 → HTTPS
```

---

# Port Ranges

| Range | Description |
|--------|-------------|
| 0–1023 | Well-known ports |
| 1024–49151 | Registered ports |
| 49152–65535 | Dynamic/Ephemeral ports |

---

# Common Enterprise Ports

| Port | Service |
|------|----------|
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 67 | DHCP Server |
| 68 | DHCP Client |
| 80 | HTTP |
| 110 | POP3 |
| 123 | NTP |
| 143 | IMAP |
| 389 | LDAP |
| 443 | HTTPS |
| 445 | SMB |
| 3306 | MySQL |
| 5432 | PostgreSQL |
| 6379 | Redis |
| 8080 | Alternative HTTP |

---

# ARP (Address Resolution Protocol)

ARP maps an IPv4 address to a MAC address.

Example:

```text
Need:

192.168.1.15

↓

Who owns this IP?

↓

MAC Address Returned

↓

Frame Sent
```

---

# ARP Workflow

```text
Host A

↓

ARP Request (Broadcast)

↓

Switch

↓

All Hosts

↓

Correct Host Replies

↓

ARP Cache Updated
```

---

# ARP Cache

Linux stores recently learned mappings.

Example:

```text
IP Address

↓

MAC Address
```

View ARP cache:

```bash
ip neigh
```

or

```bash
arp -a
```

---

# DNS (Domain Name System)

Humans remember names.

Computers use IP addresses.

DNS translates:

```text
google.com

↓

142.x.x.x
```

---

# DNS Lookup Process

```text
Browser

↓

DNS Resolver

↓

DNS Server

↓

IP Address

↓

Connect to Server
```

---

# Common DNS Record Types

| Record | Purpose |
|----------|----------|
| A | IPv4 Address |
| AAAA | IPv6 Address |
| MX | Mail Server |
| NS | Name Server |
| CNAME | Alias |
| TXT | Text Information |
| PTR | Reverse Lookup |

---

# DNS Example

```text
www.company.com

↓

DNS

↓

203.0.113.20

↓

HTTP Connection
```

---

# DHCP (Dynamic Host Configuration Protocol)

DHCP automatically assigns:

- IP Address
- Gateway
- DNS Server
- Subnet Mask
- Lease Time

Without DHCP, clients require manual configuration.

---

# DHCP Process (DORA)

```text
Client

↓

Discover

↓

Offer

↓

Request

↓

Acknowledgement
```

This sequence is commonly called **DORA**.

---

# Routing

Routing determines how packets travel between different networks.

Routers examine destination IP addresses and forward packets along the most appropriate path.

---

# Routing Example

```text
Client

↓

Router A

↓

ISP

↓

Internet

↓

Router B

↓

Server
```

---

# Default Gateway

A **default gateway** is the router used when traffic is destined for another network.

```text
Linux Server

↓

Default Gateway

↓

Internet
```

Without a valid default gateway, external networks are generally unreachable.

---

# Routing Table

Linux maintains a routing table.

View routes:

```bash
ip route
```

Example:

```text
default via 192.168.1.1 dev eth0

192.168.1.0/24 dev eth0
```

---

# Static Routing

Administrator manually creates routes.

Example:

```bash
sudo ip route add 10.10.0.0/16 via 192.168.1.254
```

Useful for:

- Small environments
- Testing
- Lab networks

---

# Dynamic Routing

Large organizations often use routing protocols such as:

- OSPF
- BGP
- IS-IS
- RIP (legacy)

These protocols automatically exchange routing information between routers.

---

# Network Interface

A network interface connects Linux to a network.

Examples:

```text
eth0

ens33

enp0s3

wlan0
```

Modern Linux systems commonly use predictable interface names such as `enp0s3` or `ens160`.

---

# Viewing Network Interfaces

Display interfaces:

```bash
ip link show
```

Display addresses:

```bash
ip addr show
```

Short form:

```bash
ip a
```

---

# Interface States

| State | Meaning |
|--------|----------|
| UP | Interface enabled |
| DOWN | Interface disabled |
| UNKNOWN | State cannot be determined |

---

# Bringing Interfaces Up

Enable an interface:

```bash
sudo ip link set eth0 up
```

---

# Bringing Interfaces Down

Disable an interface:

```bash
sudo ip link set eth0 down
```

---

# Assigning an IP Address

Example:

```bash
sudo ip addr add 192.168.1.100/24 dev eth0
```

This change is typically temporary until reboot unless saved using the distribution's network configuration tools.

---

# Removing an IP Address

```bash
sudo ip addr del 192.168.1.100/24 dev eth0
```

---

# Viewing Interface Statistics

```bash
ip -s link
```

Shows statistics including:

- Packets
- Bytes
- Errors
- Dropped packets

---

# Network Configuration Workflow

```text
Interface

↓

IP Address

↓

Subnet Mask

↓

Gateway

↓

DNS

↓

Connectivity Test
```

---

# Enterprise Example

A new Linux web server is deployed.

Configuration steps:

```text
Configure Interface

↓

Assign IP

↓

Configure Gateway

↓

Configure DNS

↓

Verify Routing

↓

Test Connectivity

↓

Deploy Application
```

---

# Cybersecurity Perspective

Many attacks target network protocols.

Examples include:

- ARP spoofing
- DNS poisoning
- Rogue DHCP servers
- TCP SYN floods
- UDP amplification attacks

Security teams should:

- Monitor abnormal network traffic.
- Use secure DNS where appropriate.
- Segment networks.
- Restrict unnecessary services.
- Monitor open ports and listening applications.

---

# Business Impact

Reliable network configuration enables:

- Continuous business operations
- Stable application communication
- Faster troubleshooting
- Secure remote administration
- Cloud connectivity
- High service availability

---

# Enterprise Best Practices

- Use predictable interface naming.
- Document IP addressing schemes.
- Minimize unnecessary open ports.
- Use DHCP reservations where appropriate for critical systems.
- Monitor routing changes.
- Restrict management services such as SSH to trusted networks.
- Review ARP and routing anomalies during security investigations.

---

# Key Takeaways

- TCP provides reliable, connection-oriented communication.
- UDP prioritizes speed and low latency.
- ARP resolves IPv4 addresses to MAC addresses.
- DNS translates hostnames into IP addresses.
- DHCP automates network configuration.
- Routing directs packets between networks.
- Linux provides powerful tools (`ip`, `ip route`, `ip neigh`) for managing network interfaces and connectivity.

---


