# 03 - TCP/IP Model

# Part 1 — Introduction to the TCP/IP Model

---

# Overview

The **TCP/IP Model** (Transmission Control Protocol/Internet Protocol) is the foundation of modern computer networking.

Unlike the OSI Model, which serves primarily as a conceptual reference framework, the TCP/IP Model is the **actual protocol suite used by the Internet and nearly every modern enterprise network**.

Every online activity relies on the TCP/IP protocol suite, including:

- Browsing websites
- Sending emails
- Streaming videos
- Cloud computing
- Mobile applications
- IoT communication
- Enterprise networking
- Remote access
- API communication

Understanding the TCP/IP Model is essential for:

- Network Engineers
- Cybersecurity Professionals
- SOC Analysts
- Penetration Testers
- Cloud Engineers
- DevOps Engineers
- System Administrators
- Incident Responders

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain the purpose of the TCP/IP Model.
- Understand each TCP/IP layer.
- Compare TCP/IP with the OSI Model.
- Describe packet flow across the Internet.
- Understand protocol interactions.
- Troubleshoot network communication.
- Analyze packets using Wireshark.
- Understand enterprise network communication.

---

# What is TCP/IP?

TCP/IP stands for:

```
Transmission Control Protocol

/

Internet Protocol
```

Although the name references only two protocols, TCP/IP actually represents **an entire suite of networking protocols** that work together to enable communication across interconnected networks.

Examples include:

- TCP
- UDP
- IPv4
- IPv6
- ICMP
- ARP
- DNS
- DHCP
- HTTP
- HTTPS
- FTP
- SMTP
- SSH
- TLS
- SNMP
- NTP

Together, these protocols define how devices communicate across local networks, enterprise environments, and the global Internet.

---

# History of TCP/IP

The TCP/IP protocol suite originated from research funded by the **United States Department of Defense (DoD)** through the **Defense Advanced Research Projects Agency (DARPA)**.

### Timeline

| Year | Milestone |
|------|-----------|
| 1969 | ARPANET established |
| 1974 | TCP proposed by Vinton Cerf and Bob Kahn |
| 1983 | TCP/IP adopted as the ARPANET standard |
| 1990 | Commercial Internet expansion |
| Today | Foundation of the global Internet |

The transition to TCP/IP enabled networks built with different technologies to communicate using a common protocol suite.

---

# Why Was TCP/IP Developed?

Early networking systems often relied on proprietary protocols that were incompatible with one another.

TCP/IP addressed these limitations by providing:

- Vendor-independent communication
- Interoperability
- Scalability
- Reliability
- Flexible routing
- Support for heterogeneous networks

Its design allows networks of varying sizes and technologies to interconnect seamlessly.

---

# Goals of the TCP/IP Model

The TCP/IP Model was designed to:

- Enable communication between networks.
- Support reliable and unreliable data delivery.
- Provide logical addressing.
- Route packets efficiently.
- Scale to millions of connected devices.
- Remain resilient during failures.

These goals have allowed the Internet to grow into the largest interconnected network in the world.

---

# TCP/IP Architecture

The TCP/IP Model consists of four layers.

```
+----------------------------+
|     Application Layer      |
+----------------------------+
|      Transport Layer       |
+----------------------------+
|       Internet Layer       |
+----------------------------+
|   Network Access Layer     |
+----------------------------+
```

Each layer has specific responsibilities while interacting with adjacent layers.

---

# Layer Responsibilities

```
Application

↓

Provides services to applications

↓

Transport

↓

End-to-end communication

↓

Internet

↓

Logical addressing and routing

↓

Network Access

↓

Local network communication
```

---

# Why Only Four Layers?

Unlike the OSI Model, the TCP/IP Model combines several related responsibilities.

For example:

- The OSI Application, Presentation, and Session Layers are combined into the TCP/IP Application Layer.
- The OSI Data Link and Physical Layers are combined into the TCP/IP Network Access Layer.

This simplification reflects the practical implementation of Internet protocols.

---

# Communication Workflow

A simplified communication process:

```
Web Browser

↓

TCP

↓

IP

↓

Ethernet

↓

Internet

↓

Server

↓

Response
```

Each protocol contributes a specific function to deliver the data successfully.

---

# TCP/IP Layer Overview

## 1. Application Layer

Provides network services directly to user applications.

Examples:

- HTTP
- HTTPS
- DNS
- FTP
- SMTP
- SSH
- SNMP

Responsibilities include:

- Web communication
- Email
- File transfer
- Name resolution
- Remote management

---

## 2. Transport Layer

Provides end-to-end communication between applications.

Protocols:

- TCP
- UDP

Responsibilities:

- Segmentation
- Reliability
- Flow control
- Error recovery
- Port addressing

---

## 3. Internet Layer

Responsible for logical addressing and routing packets between networks.

Protocols include:

- IPv4
- IPv6
- ICMP
- IPsec

Responsibilities:

- Routing
- Packet forwarding
- Logical addressing
- Fragmentation (IPv4)

---

## 4. Network Access Layer

Responsible for communication over the local network.

Technologies include:

- Ethernet
- Wi-Fi
- PPP
- ARP

Responsibilities:

- Framing
- MAC addressing
- Error detection
- Physical transmission

---

# Comparison with the OSI Model

```
OSI Model                    TCP/IP Model

Application     ┐
Presentation    ├──────► Application
Session         ┘

Transport  ─────────────► Transport

Network    ─────────────► Internet

Data Link  ┐
Physical   ┘──────► Network Access
```

---

# OSI vs TCP/IP

| Feature | OSI Model | TCP/IP Model |
|----------|-----------|--------------|
| Number of Layers | 7 | 4 |
| Purpose | Reference model | Practical protocol suite |
| Developed By | ISO | DARPA |
| Internet Implementation | No | Yes |
| Used for Troubleshooting | Yes | Yes |
| Used for Education | Yes | Yes |
| Used by Modern Networks | Indirectly | Directly |

---

# Why TCP/IP Became the Internet Standard

TCP/IP became the dominant networking model because it offered:

### Scalability

Supports networks ranging from a few devices to billions of connected systems.

### Flexibility

Works across different hardware platforms, operating systems, and communication technologies.

### Reliability

Provides mechanisms for reliable communication through protocols such as TCP.

### Open Standards

The protocol suite is defined through publicly available standards, enabling widespread adoption and interoperability.

---

# Enterprise Communication Example

Consider an employee accessing a cloud-hosted application.

```
Employee Laptop

↓

HTTPS

↓

TCP

↓

IP

↓

Ethernet

↓

Switch

↓

Router

↓

Firewall

↓

Internet

↓

Cloud Load Balancer

↓

Application Server

↓

Database
```

Each layer of the TCP/IP Model contributes to delivering the request and returning the response.

---

# TCP/IP in Cybersecurity

Cybersecurity professionals analyze and defend communication at every TCP/IP layer.

Examples include:

| Layer | Security Examples |
|--------|-------------------|
| Application | Web attacks, API abuse, DNS attacks |
| Transport | SYN Floods, Port Scanning |
| Internet | IP Spoofing, ICMP Abuse |
| Network Access | ARP Spoofing, MAC Flooding |

Understanding the TCP/IP Model helps identify where attacks occur and where defensive controls should be applied.

---

# Benefits of the TCP/IP Model

- Vendor-independent communication
- Modular architecture
- Proven scalability
- Reliable communication
- Efficient routing
- Internet-wide interoperability
- Support for modern cloud infrastructures
- Foundation for enterprise networking

---

# Limitations

Although highly successful, the TCP/IP Model has some limitations:

- Less granular than the OSI Model.
- Does not explicitly separate presentation and session responsibilities.
- Some protocol responsibilities overlap across layers.
- Security was not a primary design objective in the earliest versions, requiring additional protocols such as TLS and IPsec.

---

# Key Takeaways

- The TCP/IP Model is the practical networking model used by the Internet.
- It consists of four layers: Application, Transport, Internet, and Network Access.
- The model defines how data is transmitted across interconnected networks using a suite of standardized protocols.
- TCP/IP emphasizes interoperability, scalability, and reliable communication.
- Understanding the TCP/IP Model is essential for networking, cloud computing, and cybersecurity professionals.

# 03 - TCP/IP Model

# Part 2 — TCP/IP Layers (In Depth)

---

# Overview

The TCP/IP Model divides network communication into four logical layers.

Each layer performs a specific set of responsibilities and communicates with the adjacent layers.

Unlike the OSI Model, the TCP/IP Model represents the **actual implementation** used by modern operating systems, enterprise networks, cloud platforms, and the Internet.

```
+------------------------------+
|     Application Layer        |
+------------------------------+
|      Transport Layer         |
+------------------------------+
|       Internet Layer         |
+------------------------------+
|    Network Access Layer      |
+------------------------------+
```

Together, these layers enable secure, reliable, and scalable communication between billions of connected devices worldwide.

---

# 1. Application Layer

```
+------------------------------+
|      Application Layer       |
+------------------------------+
```

---

## Overview

The Application Layer is the highest layer of the TCP/IP Model.

It provides network services directly to user applications.

Unlike the OSI Model, this layer combines the responsibilities of:

- Application Layer
- Presentation Layer
- Session Layer

Applications do **not** communicate directly with the network. Instead, they rely on protocols provided by this layer.

---

# Responsibilities

- Web communication
- File transfer
- Email communication
- Remote login
- Name resolution
- Time synchronization
- Network management
- Session management
- Encryption support
- Data formatting

---

# Common Protocols

| Protocol | Purpose |
|----------|----------|
| HTTP | Web browsing |
| HTTPS | Secure web browsing |
| FTP | File transfer |
| SFTP | Secure file transfer |
| SSH | Secure remote administration |
| Telnet | Legacy remote login |
| DNS | Domain name resolution |
| DHCP | Automatic IP assignment |
| SMTP | Sending email |
| POP3 | Receiving email |
| IMAP | Email synchronization |
| SNMP | Network monitoring |
| NTP | Time synchronization |
| LDAP | Directory services |
| SMB | File and printer sharing |

---

# Enterprise Example

A user enters:

```
https://company.com
```

The Application Layer performs tasks such as:

- Resolving the domain name
- Creating the HTTPS request
- Establishing a secure TLS session
- Sending application data

---

# Cybersecurity Threats

Examples include:

- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Server-Side Request Forgery (SSRF)
- XML External Entity (XXE)
- Command Injection
- API attacks
- Authentication bypass
- DNS poisoning
- Email spoofing

---

# Security Controls

- Web Application Firewall (WAF)
- Secure coding practices
- Multi-Factor Authentication (MFA)
- DNS Security Extensions (DNSSEC)
- API gateways
- Input validation
- Secure session management
- TLS encryption
- Email authentication (SPF, DKIM, DMARC)

---

# Wireshark Observation

Typical protocols visible:

- HTTP
- HTTPS
- DNS
- FTP
- SMTP
- SSH

---

# 2. Transport Layer

```
+------------------------------+
|       Transport Layer        |
+------------------------------+
```

---

# Overview

The Transport Layer provides **end-to-end communication** between applications.

It ensures that data reaches the correct application on the destination device.

Depending on the protocol used, communication may be:

- Reliable
- Best-effort
- Connection-oriented
- Connectionless

---

# Responsibilities

- Segmentation
- Reassembly
- Flow control
- Error recovery
- Reliability
- Multiplexing
- Port addressing

---

# Major Protocols

## TCP

Characteristics:

- Connection-oriented
- Reliable
- Ordered delivery
- Error checking
- Flow control
- Congestion control

Used for:

- HTTPS
- SSH
- FTP
- Email
- Database communication

---

## UDP

Characteristics:

- Connectionless
- Low overhead
- Faster transmission
- No retransmissions
- No guaranteed delivery

Used for:

- DNS
- Streaming
- VoIP
- Online gaming
- DHCP
- SNMP

---

# Port Numbers

Ports identify applications on a device.

| Port | Protocol |
|------|----------|
| 20/21 | FTP |
| 22 | SSH |
| 23 | Telnet |
| 25 | SMTP |
| 53 | DNS |
| 67/68 | DHCP |
| 80 | HTTP |
| 110 | POP3 |
| 123 | NTP |
| 143 | IMAP |
| 161 | SNMP |
| 389 | LDAP |
| 443 | HTTPS |
| 445 | SMB |
| 3389 | RDP |

---

# Enterprise Example

```
Browser

↓

TCP Port 443

↓

Web Server
```

TCP guarantees that packets arrive correctly and in order before they are delivered to the application.

---

# Cybersecurity Threats

- TCP SYN Flood
- UDP Flood
- Port Scanning
- TCP Reset attacks
- Reflection attacks
- Amplification attacks

---

# Security Controls

- Stateful firewalls
- SYN Cookies
- Rate limiting
- IDS/IPS
- Port filtering
- Network segmentation

---

# Wireshark Observation

Typical fields:

- Source Port
- Destination Port
- Sequence Number
- Acknowledgment Number
- Window Size
- TCP Flags

---

# 3. Internet Layer

```
+------------------------------+
|       Internet Layer         |
+------------------------------+
```

---

# Overview

The Internet Layer is responsible for **logical addressing and routing packets between networks**.

This layer determines how packets travel from the source host to the destination host, even when they pass through multiple routers and networks.

---

# Responsibilities

- Logical addressing
- Packet forwarding
- Routing
- Fragmentation (IPv4)
- Path selection

---

# Major Protocols

| Protocol | Purpose |
|----------|----------|
| IPv4 | Logical addressing |
| IPv6 | Next-generation addressing |
| ICMP | Error reporting and diagnostics |
| IGMP | Multicast management |
| IPsec | Secure IP communication |

---

# IP Addressing

Example IPv4 addresses:

```
192.168.1.100

10.0.0.25

172.16.20.5
```

Example IPv6 address:

```
2001:db8:abcd::100
```

---

# Devices

- Routers
- Layer 3 Switches
- Firewalls
- VPN Gateways

---

# Enterprise Example

```
Laptop

↓

Router

↓

ISP

↓

Internet

↓

Cloud Network

↓

Server
```

The Internet Layer determines the best available path to reach the destination.

---

# Cybersecurity Threats

- IP Spoofing
- ICMP Abuse
- Route Hijacking
- Packet Fragmentation Attacks
- Routing Protocol Attacks

---

# Security Controls

- ACLs
- Anti-spoofing filters
- IPsec
- Secure routing protocols
- Network segmentation
- VPNs

---

# Wireshark Observation

Common fields include:

- Source IP
- Destination IP
- TTL / Hop Limit
- Protocol
- Fragment Offset

---

# 4. Network Access Layer

```
+------------------------------+
|    Network Access Layer      |
+------------------------------+
```

---

# Overview

The Network Access Layer is responsible for communication over the local network.

It combines the functions of the **Physical Layer** and the **Data Link Layer** from the OSI Model.

---

# Responsibilities

- Framing
- MAC addressing
- Media access control
- Error detection
- Physical transmission
- Local network communication

---

# Technologies

- Ethernet
- Wi-Fi
- PPP
- Frame Relay (legacy)
- ATM (legacy)

---

# Protocols

- ARP
- Ethernet
- IEEE 802.3
- IEEE 802.11
- VLAN (802.1Q)

---

# Address Used

```
MAC Address
```

Example:

```
00:1A:2B:3C:4D:5E
```

---

# Devices

- Switches
- Bridges
- Wireless Access Points
- NICs
- Repeaters
- Hubs

---

# Enterprise Example

```
Laptop

↓

Access Switch

↓

Core Switch

↓

Router
```

The Network Access Layer delivers frames between devices connected to the same local network.

---

# Cybersecurity Threats

- ARP Spoofing
- MAC Flooding
- VLAN Hopping
- Rogue Access Points
- MAC Spoofing

---

# Security Controls

- Port Security
- Dynamic ARP Inspection (DAI)
- BPDU Guard
- 802.1X Authentication
- VLAN Segmentation
- Secure Switch Configuration

---

# Wireshark Observation

Common fields include:

- Source MAC
- Destination MAC
- EtherType
- VLAN Tag
- Frame Check Sequence (FCS, typically validated by hardware and not shown)

---

# Layer Interaction

The TCP/IP layers work together to deliver application data.

```
Application Layer

↓

Transport Layer

↓

Internet Layer

↓

Network Access Layer

↓

Transmission Medium

↓

Network Access Layer

↓

Internet Layer

↓

Transport Layer

↓

Application Layer
```

Each layer provides services to the layer above while relying on the services of the layer below.

---

# TCP/IP Layer Summary

| Layer | Primary Function | Address Used | Example Protocols | Typical Devices |
|--------|------------------|--------------|-------------------|-----------------|
| Application | User-facing network services | URL, Domain Name | HTTP, HTTPS, DNS, SMTP, SSH | Proxy, WAF, API Gateway |
| Transport | End-to-end communication | Port Number | TCP, UDP | Firewall, Load Balancer |
| Internet | Logical addressing and routing | IP Address | IPv4, IPv6, ICMP, IPsec | Router, Layer 3 Switch |
| Network Access | Local network communication | MAC Address | Ethernet, ARP, Wi-Fi | Switch, Bridge, NIC |