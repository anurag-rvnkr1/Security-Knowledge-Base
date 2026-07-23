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

