# 15 - Network Devices

# Part 1 — Network Device Fundamentals, OSI Layer Mapping, Repeaters, Hubs, Bridges, Switches, Routers, Gateways, and Enterprise Network Infrastructure

---

# Overview

Modern computer networks rely on specialized devices that perform functions such as forwarding traffic, connecting network segments, enforcing security policies, optimizing performance, and ensuring high availability.

From a small office with a single router to a global enterprise operating thousands of network devices across multiple continents, these components form the foundation of reliable communication.

Common network devices include:

- Network Interface Cards (NICs)
- Repeaters
- Hubs
- Bridges
- Switches
- Routers
- Gateways
- Wireless Access Points
- Firewalls
- Load Balancers
- Proxies
- IDS/IPS Appliances
- Web Application Firewalls (WAFs)
- SD-WAN Appliances
- Cloud Virtual Network Devices

Understanding how each device operates and where it fits into the OSI model is essential for Network Engineers, Cybersecurity Professionals, SOC Analysts, Cloud Engineers, and System Administrators.

---

# Learning Objectives

After completing this chapter, you will understand:

- Network device fundamentals
- Device classification
- OSI layer mapping
- Network Interface Cards (NICs)
- Repeaters
- Hubs
- Bridges
- Switches
- Routers
- Gateways
- Enterprise networking infrastructure
- Business applications
- Best practices

---

# What is a Network Device?

A **network device** is a hardware or virtual appliance that enables communication between systems by transmitting, forwarding, filtering, securing, or managing network traffic.

These devices perform different functions depending on the OSI layer at which they operate.

---

# Why Network Devices Matter

Every enterprise depends on network devices to provide:

- Connectivity
- Scalability
- Performance
- Security
- Availability
- Fault tolerance
- Monitoring
- Centralized management

Without properly designed network infrastructure, business applications cannot function reliably.

---

# Network Device Classification

Network devices can be grouped into several categories.

| Category | Examples |
|----------|----------|
| Connectivity Devices | Hub, Switch, Router |
| Security Devices | Firewall, IDS, IPS, WAF |
| Wireless Devices | Access Point, Wireless Controller |
| Optimization Devices | Load Balancer, Proxy |
| Monitoring Devices | TAP, Network Packet Broker |
| Cloud Devices | Virtual Router, Virtual Firewall, Cloud Load Balancer |

---

# OSI Layer Mapping

Different devices primarily operate at different OSI layers.

| Device | Primary OSI Layer |
|----------|------------------|
| Repeater | Layer 1 |
| Hub | Layer 1 |
| Bridge | Layer 2 |
| Switch | Layer 2 (some also Layer 3) |
| Router | Layer 3 |
| Gateway | Layers 4–7 (implementation dependent) |
| Firewall | Layers 3–7 |
| Load Balancer | Layers 4 and 7 |
| WAF | Layer 7 |

---

# Enterprise Network Architecture

A simplified enterprise topology:

```
Internet

↓

ISP Router

↓

Edge Firewall

↓

Core Router

↓

Core Switch

↓

Distribution Switches

↓

Access Switches

↓

Endpoints
```

Additional devices such as IDS/IPS, WAFs, VPN gateways, and load balancers are commonly integrated throughout the architecture.

---

# Network Interface Card (NIC)

## Overview

A **Network Interface Card (NIC)** is the hardware or virtual adapter that connects a device to a network.

Every host communicating over Ethernet or Wi-Fi uses a NIC.

```
Computer

↓

NIC

↓

Ethernet Cable

↓

Switch
```

---

# Responsibilities of a NIC

A NIC is responsible for:

- Physical network connectivity
- MAC addressing
- Frame transmission
- Frame reception
- Error detection (Frame Check Sequence handling)
- Speed and duplex negotiation

---

# NIC Components

Typical components include:

- MAC Address
- PHY (Physical Interface)
- Network Controller
- Buffers
- Transceiver
- Driver/Firmware

---

# MAC Address

Every NIC contains a unique hardware identifier.

Example:

```
00:1A:2B:3C:4D:5E
```

The MAC address operates at the Data Link Layer.

---

# NIC Speeds

Common Ethernet speeds include:

| Standard | Speed |
|-----------|-------|
| Fast Ethernet | 100 Mbps |
| Gigabit Ethernet | 1 Gbps |
| 10 Gigabit Ethernet | 10 Gbps |
| 25 Gigabit Ethernet | 25 Gbps |
| 40 Gigabit Ethernet | 40 Gbps |
| 100 Gigabit Ethernet | 100 Gbps |
| 400 Gigabit Ethernet | 400 Gbps |

Modern data centers increasingly deploy 100G and 400G links for high-throughput workloads.

---

# Repeater

## Overview

A **Repeater** is a Layer 1 device that regenerates weakened electrical or optical signals.

```
Signal

↓

Weak

↓

Repeater

↓

Regenerated Signal
```

Repeaters extend the distance over which signals can travel.

---

# Functions of a Repeater

A repeater:

- Receives signals
- Regenerates signals
- Retransmits signals

It does **not**:

- Inspect frames
- Filter traffic
- Learn MAC addresses
- Route packets

---

# Enterprise Use Cases

Repeaters are less common in modern LANs but may still be found in:

- Fiber optic links
- Industrial networks
- Long-distance communication systems

---

# Hub

## Overview

A **Hub** is a multiport repeater operating at Layer 1.

```
PC 1

↓

Hub

↓

PC 2

↓

PC 3

↓

PC 4
```

Any incoming signal is repeated to every connected device.

---

# Hub Operation

Example:

```
PC A Sends Frame

↓

Hub

↓

Broadcast to Every Port
```

Every device receives the frame, even if it is not the intended recipient.

---

# Limitations of Hubs

Hubs:

- Create one collision domain.
- Operate in half-duplex mode.
- Waste bandwidth.
- Provide no traffic isolation.
- Offer no security features.

Consequently, hubs have largely been replaced by switches.

---

# Bridge

## Overview

A **Bridge** operates at Layer 2 and connects two LAN segments.

```
LAN A

↓

Bridge

↓

LAN B
```

Unlike a hub, a bridge forwards frames selectively.

---

# Bridge Functions

A bridge:

- Learns MAC addresses.
- Builds a forwarding table.
- Filters unnecessary traffic.
- Reduces collisions.

---

# MAC Learning

Example:

```
MAC AA

↓

Port 1

────────────

MAC BB

↓

Port 2
```

The bridge records which MAC addresses are reachable through each interface.

---

# Bridge Forwarding

```
Destination MAC Known

↓

Forward

──────────────

Unknown

↓

Flood
```

This process is similar to switch forwarding.

---

# Switch

## Overview

A **Network Switch** is the primary Layer 2 forwarding device used in modern Ethernet networks.

```
PC

↓

Switch

↓

Server

↓

Printer

↓

VoIP Phone
```

Switches forward frames only to the destination port instead of broadcasting to all devices.

---

# Switch Responsibilities

Switches perform:

- MAC learning
- Frame forwarding
- Frame filtering
- VLAN segmentation
- Loop prevention
- QoS support
- Port security
- Link aggregation

---

# Switch MAC Address Table

Example:

| MAC Address | Port |
|-------------|------|
| AA:AA:AA | Gi0/1 |
| BB:BB:BB | Gi0/2 |
| CC:CC:CC | Gi0/3 |

The switch uses this table to determine where frames should be forwarded.

---

# Switch Forwarding Process

```
Frame Received

↓

Destination MAC Lookup

↓

Known?

↓

Yes

↓

Forward

──────────────

No

↓

Flood
```

Over time, MAC learning reduces unnecessary flooding.

---

# Collision Domains

Unlike hubs, switches create separate collision domains.

```
Switch

↓

Port 1

↓

Host A

────────────

Port 2

↓

Host B
```

Each switch port represents an independent collision domain.

---

# Broadcast Domains

By default, all ports within the same VLAN belong to the same broadcast domain.

Broadcast traffic includes:

- ARP
- DHCP Discover
- Certain IPv6 Neighbor Discovery messages (within the local segment)

Broadcast domains can be separated using:

- VLANs
- Routers
- Layer 3 switches

---

# Router

## Overview

A **Router** is a Layer 3 device that forwards packets between different IP networks.

```
LAN A

↓

Router

↓

LAN B

↓

Internet
```

Routers make forwarding decisions using IP addresses and routing tables.

---

# Router Responsibilities

Routers:

- Forward IP packets.
- Maintain routing tables.
- Separate broadcast domains.
- Connect WANs and LANs.
- Perform Network Address Translation (NAT).
- Support dynamic routing protocols.
- Enforce routing policies.

---

# Routing Decision Process

```
Packet Arrives

↓

Destination IP

↓

Routing Table Lookup

↓

Best Route Selected

↓

Forward Packet
```

Routing decisions are based on the longest-prefix match and routing metrics.

---

# Default Gateway

Hosts send traffic destined for remote networks to their configured default gateway.

```
PC

↓

Default Gateway

↓

Router

↓

Internet
```

Without a valid gateway, hosts can communicate only within their local subnet.

---

# Gateway

## Overview

A **Gateway** connects networks that use different protocols, architectures, or communication methods.

Examples include:

- Email gateways
- VoIP gateways
- API gateways
- Industrial protocol gateways
- Cloud gateways

Unlike routers, gateways often perform protocol translation.

---

# Gateway Functions

A gateway may provide:

- Protocol conversion
- Data transformation
- Authentication
- Encryption
- Application inspection
- Session management

Gateways commonly operate at Layers 4–7, although implementations vary.

---

# Enterprise Example

An employee accesses a cloud-hosted business application.

```
Laptop

↓

Access Switch

↓

Core Switch

↓

Router

↓

Edge Firewall

↓

Internet

↓

Cloud Gateway

↓

Application
```

Each network device contributes to secure and reliable communication.

---

# Business Impact

Well-designed network infrastructure enables:

- Reliable connectivity
- High availability
- Scalable growth
- Secure communications
- Improved performance
- Efficient troubleshooting
- Reduced operational costs

Selecting the appropriate network devices is fundamental to enterprise architecture.

---

# Enterprise Best Practices

Organizations should:

- Deploy managed switches instead of hubs.
- Use redundant core routers.
- Implement VLAN segmentation.
- Harden network device configurations.
- Monitor interface health and utilization.
- Maintain accurate network documentation.
- Regularly update firmware and operating systems.
- Restrict administrative access using secure protocols.

---

# Key Takeaways

- Network devices perform specialized roles at different OSI layers.
- NICs provide physical and data link connectivity.
- Repeaters regenerate signals but do not inspect traffic.
- Hubs broadcast frames to all connected devices and are largely obsolete.
- Bridges reduce collisions by forwarding frames selectively.
- Switches provide efficient Layer 2 forwarding using MAC address tables.
- Routers connect different IP networks using routing tables.
- Gateways enable communication between different protocols or application environments.

---


# Part 2 — Firewalls, Wireless Access Points, Modems, Load Balancers, Proxies, IDS, IPS, WAF, SD-WAN, Cloud Network Devices, and Enterprise Architectures

---

# Introduction

Modern enterprise networks consist of far more than switches and routers.

Organizations deploy specialized devices that provide:

- Network security
- High availability
- Wireless connectivity
- Traffic optimization
- Threat detection
- Application delivery
- Cloud integration
- Remote connectivity

These devices are essential for supporting today's hybrid, multi-cloud, and Zero Trust environments.

---

# Firewall

## Overview

A **Firewall** is a network security device that monitors, filters, and controls traffic based on predefined security policies.

```
Internet

↓

Firewall

↓

Internal Network
```

Firewalls inspect traffic entering and leaving a network and decide whether to allow or block it.

---

# Primary Responsibilities

A firewall performs:

- Traffic filtering
- Access control
- Network segmentation
- NAT (Network Address Translation)
- VPN termination
- Threat logging
- Policy enforcement

---

# Firewall Types

| Type | Description |
|--------|-------------|
| Packet Filtering Firewall | Filters based on IP, Port, Protocol |
| Stateful Firewall | Tracks connection state |
| Circuit-Level Gateway | Monitors TCP sessions |
| Application Proxy Firewall | Inspects application traffic |
| Next-Generation Firewall (NGFW) | Deep packet inspection, IPS, application awareness |

---

# Packet Filtering Firewall

Operates using rules such as:

```
Source IP

↓

Destination IP

↓

Port

↓

Protocol

↓

Permit / Deny
```

Advantages:

- Fast
- Lightweight
- Simple configuration

Limitations:

- No session awareness
- Limited visibility

---

# Stateful Firewall

Stateful firewalls maintain a **state table**.

```
TCP Connection

↓

Firewall

↓

State Table

↓

Allow Return Traffic
```

Benefits:

- Tracks active sessions
- Prevents unsolicited inbound traffic
- Better security than stateless filtering

---

# Next-Generation Firewall (NGFW)

NGFWs combine traditional firewall functionality with advanced security features.

Capabilities include:

- Deep Packet Inspection (DPI)
- Application identification
- Intrusion Prevention System (IPS)
- Malware detection
- URL filtering
- SSL/TLS inspection
- User identity integration
- Threat intelligence

Popular enterprise NGFW vendors include Palo Alto Networks, Fortinet, Cisco, Check Point, and Sophos.

---

# Wireless Access Point (WAP)

## Overview

A **Wireless Access Point (WAP)** enables wireless devices to connect to a wired Ethernet network.

```
Laptop

↓

Wi-Fi

↓

Access Point

↓

Switch
```

---

# Responsibilities

A WAP provides:

- Wireless connectivity
- Authentication
- Encryption
- Client roaming
- SSID broadcasting
- Radio management

---

# Enterprise Wireless Architecture

```
Wireless Clients

↓

Access Points

↓

Wireless Controller

↓

Core Switch

↓

Firewall
```

Large organizations often use centralized wireless controllers for policy management and roaming.

---

# Wireless Security

Recommended enterprise security:

- WPA3 Enterprise
- 802.1X Authentication
- RADIUS
- Certificate-based authentication
- Network segmentation
- Guest isolation

---

# Modem

## Overview

A **Modem (Modulator/Demodulator)** converts digital signals into forms suitable for transmission across a service provider's network and converts incoming signals back into digital form.

```
ISP

↓

Modem

↓

Router

↓

LAN
```

Modern broadband technologies include:

- Fiber
- Cable
- DSL
- Cellular (4G/5G)

---

# Load Balancer

## Overview

A **Load Balancer** distributes incoming client requests across multiple backend servers.

```
Clients

↓

Load Balancer

↓

Server 1

↓

Server 2

↓

Server 3
```

This improves availability, scalability, and performance.

---

# Benefits

Load balancing provides:

- High availability
- Fault tolerance
- Scalability
- Better resource utilization
- Reduced response time

---

# Load Balancing Algorithms

Common algorithms:

| Algorithm | Description |
|------------|-------------|
| Round Robin | Sequential distribution |
| Least Connections | Fewest active sessions |
| Least Response Time | Fastest responding server |
| Weighted Round Robin | Capacity-aware distribution |
| Hash-Based | Consistent destination selection |

---

# Health Checks

Load balancers continuously verify server availability.

```
Load Balancer

↓

Health Check

↓

Server Healthy?

↓

Yes

↓

Send Traffic

──────────────

No

↓

Remove From Pool
```

---

# Layer 4 vs Layer 7 Load Balancing

| Layer | Characteristics |
|--------|----------------|
| Layer 4 | TCP/UDP based |
| Layer 7 | HTTP/HTTPS aware |

Layer 7 load balancers can make routing decisions based on:

- URL
- HTTP headers
- Cookies
- Hostnames
- API paths

---

# Proxy Server

## Overview

A **Proxy Server** acts as an intermediary between clients and servers.

```
Client

↓

Proxy

↓

Internet
```

---

# Forward Proxy

Used by internal users accessing external resources.

Benefits:

- Content filtering
- User authentication
- Malware inspection
- Internet access control
- Logging

---

# Reverse Proxy

Protects backend servers.

```
Internet

↓

Reverse Proxy

↓

Application Servers
```

Benefits:

- SSL termination
- Load balancing
- Web acceleration
- Application protection
- Hides backend infrastructure

---

# Intrusion Detection System (IDS)

## Overview

An IDS monitors network traffic and generates alerts for suspicious activity.

```
Network

↓

IDS

↓

Alert

↓

SOC
```

An IDS does **not** automatically block traffic.

---

# IDS Types

| Type | Description |
|--------|-------------|
| NIDS | Network-based IDS |
| HIDS | Host-based IDS |

---

# Common IDS Platforms

Examples:

- Snort
- Suricata
- Zeek

---

# Intrusion Prevention System (IPS)

## Overview

An IPS operates inline and can actively prevent attacks.

```
Traffic

↓

IPS

↓

Attack?

↓

Yes

↓

Block
```

Unlike an IDS, an IPS can enforce security policies in real time.

---

# IPS Capabilities

- Signature detection
- Anomaly detection
- Protocol analysis
- Threat blocking
- Rate limiting
- Exploit prevention

---

# IDS vs IPS

| Feature | IDS | IPS |
|----------|-----|-----|
| Inline | No | Yes |
| Detection | Yes | Yes |
| Blocking | No | Yes |
| Alerts | Yes | Yes |
| Traffic Modification | No | Yes |

---

# Web Application Firewall (WAF)

## Overview

A WAF protects web applications from Layer 7 attacks.

```
Internet

↓

WAF

↓

Web Application
```

---

# Common Threats Blocked

A WAF can detect or mitigate:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- File Inclusion
- HTTP Floods
- Malicious Bots
- OWASP Top 10 attacks

---

# SD-WAN

## Overview

Software-Defined Wide Area Networking (SD-WAN) centralizes WAN management and intelligently routes traffic across multiple network links.

```
Branch Office

↓

SD-WAN Edge

↓

Internet/MPLS/LTE

↓

Data Center
```

---

# SD-WAN Benefits

- Centralized management
- Dynamic path selection
- Application-aware routing
- WAN optimization
- Secure branch connectivity
- Reduced operational costs

---

# VPN Gateway

A VPN Gateway enables secure communication across untrusted networks.

```
Remote User

↓

Encrypted Tunnel

↓

VPN Gateway

↓

Corporate Network
```

Supported technologies commonly include:

- IPsec
- SSL/TLS VPN
- WireGuard (vendor dependent)
- OpenVPN (implementation dependent)

---

# Network TAP

A **Network TAP (Test Access Point)** provides a copy of network traffic for monitoring tools.

```
Network Link

↓

TAP

↓

IDS

↓

Packet Capture
```

Unlike SPAN ports, hardware TAPs generally introduce minimal packet loss during monitoring.

---

# Packet Broker

Packet Brokers aggregate, filter, and distribute network traffic to monitoring tools.

```
TAPs

↓

Packet Broker

↓

IDS

↓

NPM

↓

SIEM Sensors
```

This improves monitoring efficiency in large enterprise environments.

---

# Cloud Network Devices

Cloud providers offer virtual networking components.

Examples include:

AWS

- Virtual Private Cloud (VPC)
- Internet Gateway
- NAT Gateway
- Transit Gateway
- Elastic Load Balancer

Microsoft Azure

- Virtual Network (VNet)
- Azure Firewall
- Azure Load Balancer
- VPN Gateway
- Application Gateway

Google Cloud

- Virtual Private Cloud
- Cloud Router
- Cloud NAT
- Cloud Load Balancing
- Cloud Armor

These services provide functionality similar to traditional on-premises appliances.

---

# Enterprise Data Center Architecture

Example:

```
Internet

↓

Edge Router

↓

NGFW

↓

IPS

↓

Core Switch

↓

Load Balancer

↓

Application Servers

↓

Database Servers
```

Monitoring systems collect logs from each component for centralized analysis.

---

# Hybrid Cloud Architecture

```
Branch Office

↓

SD-WAN

↓

Data Center

↓

Cloud VPN

↓

Public Cloud

↓

Cloud Load Balancer

↓

Application
```

Hybrid architectures allow workloads to span on-premises and cloud environments securely.

---

# Zero Trust Network Architecture

Modern enterprises increasingly adopt Zero Trust principles.

Key concepts include:

- Verify explicitly
- Least privilege access
- Continuous authentication
- Micro-segmentation
- Device posture validation
- Identity-aware access

Network devices enforce these principles through integrated security controls.

---

# Business Impact

Deploying specialized network devices enables organizations to:

- Improve security posture
- Increase service availability
- Scale applications efficiently
- Reduce downtime
- Support remote work
- Enable cloud adoption
- Enhance user experience

---

# Enterprise Best Practices

Organizations should:

- Deploy NGFWs at network boundaries.
- Use WAFs to protect Internet-facing applications.
- Implement IDS and IPS for threat visibility and prevention.
- Secure wireless networks using WPA3 Enterprise and 802.1X.
- Configure redundant load balancers.
- Monitor VPN gateways and SD-WAN edges.
- Keep firmware and software updated.
- Centralize logging in a SIEM platform.

---

# Key Takeaways

- Firewalls enforce network security policies.
- NGFWs provide advanced application-aware inspection.
- WAPs enable secure wireless connectivity.
- Load balancers improve scalability and high availability.
- Proxies mediate client-server communications.
- IDS detects threats, while IPS can actively block them.
- WAFs protect web applications from Layer 7 attacks.
- SD-WAN simplifies WAN management and optimizes traffic.
- Cloud providers offer virtual equivalents of traditional networking devices.

---


