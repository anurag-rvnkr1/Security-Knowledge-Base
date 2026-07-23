# 25 - Interview Questions

# Part 1 — Networking Fundamentals, OSI Model, TCP/IP Model, Ethernet, IPv4, IPv6, and Subnetting Interview Questions

---

# Introduction

Technical interviews for Network Engineer, SOC Analyst, System Administrator, Cybersecurity Engineer, Cloud Engineer, and DevOps roles frequently assess networking fundamentals.

Interviewers evaluate not only technical knowledge but also the ability to explain concepts clearly, troubleshoot problems logically, and apply networking principles to real-world enterprise environments.

This chapter provides questions ranging from beginner to advanced levels, along with concise, recruiter-friendly answers.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Answer common networking interview questions confidently.
- Explain networking concepts using practical examples.
- Prepare for technical and scenario-based interviews.
- Strengthen troubleshooting and communication skills.

---

# Networking Fundamentals

---

## Q1. What is a computer network?

**Answer:**

A computer network is a collection of interconnected devices that communicate and share resources such as files, printers, applications, and Internet connectivity using standardized communication protocols.

---

## Q2. Why do organizations use networks?

**Answer:**

Organizations use networks to:

- Share information
- Improve collaboration
- Centralize resources
- Reduce operational costs
- Improve security
- Support business continuity

---

## Q3. What are the main types of networks?

**Answer:**

- PAN (Personal Area Network)
- LAN (Local Area Network)
- CAN (Campus Area Network)
- MAN (Metropolitan Area Network)
- WAN (Wide Area Network)
- SD-WAN
- VPN
- Cloud Networks

---

## Q4. What is bandwidth?

**Answer:**

Bandwidth is the maximum amount of data that can be transmitted across a network connection per unit of time, typically measured in bits per second (bps).

---

## Q5. What is throughput?

**Answer:**

Throughput is the actual amount of data successfully transferred over the network, which is usually lower than the available bandwidth due to protocol overhead and congestion.

---

## Q6. What is latency?

**Answer:**

Latency is the time taken for a packet to travel from the source to the destination. Lower latency improves application responsiveness.

---

## Q7. What is jitter?

**Answer:**

Jitter is the variation in packet arrival times. High jitter negatively affects real-time applications such as Voice over IP (VoIP) and video conferencing.

---

## Q8. What is packet loss?

**Answer:**

Packet loss occurs when packets fail to reach their destination due to congestion, hardware failures, routing issues, or network errors.

---

# OSI Model

---

## Q9. What is the OSI Model?

**Answer:**

The Open Systems Interconnection (OSI) Model is a seven-layer conceptual framework that standardizes network communication and simplifies troubleshooting.

---

## Q10. Name all seven OSI layers.

**Answer:**

1. Physical
2. Data Link
3. Network
4. Transport
5. Session
6. Presentation
7. Application

---

## Q11. Which OSI layer handles routing?

**Answer:**

The **Network Layer (Layer 3)** is responsible for logical addressing and routing packets between networks.

---

## Q12. Which OSI layer uses MAC addresses?

**Answer:**

The **Data Link Layer (Layer 2)** uses MAC addresses for communication within the same local network.

---

## Q13. Which layer is responsible for reliable communication?

**Answer:**

The **Transport Layer (Layer 4)** provides reliable communication using TCP.

---

## Q14. Which OSI layer handles encryption?

**Answer:**

The **Presentation Layer (Layer 6)** is responsible for data encryption, compression, and format translation.

---

## Q15. Which layer interacts directly with users?

**Answer:**

The **Application Layer (Layer 7)** provides services used by applications such as HTTP, DNS, FTP, and SMTP.

---

## Q16. Why is the OSI model important?

**Answer:**

The OSI model provides a standardized framework that simplifies network design, troubleshooting, interoperability, and protocol development.

---

# TCP/IP Model

---

## Q17. What is the TCP/IP Model?

**Answer:**

The TCP/IP Model is the practical networking model used on the Internet. It consists of four layers:

1. Network Access
2. Internet
3. Transport
4. Application

---

## Q18. What is the difference between the OSI and TCP/IP models?

| OSI | TCP/IP |
|------|---------|
| Seven layers | Four layers |
| Reference model | Practical implementation |
| Primarily educational | Used in production networks |

---

## Q19. Which protocol provides reliable communication?

**Answer:**

TCP (Transmission Control Protocol) provides reliable, connection-oriented communication using acknowledgments, sequencing, and retransmissions.

---

## Q20. Which protocol is connectionless?

**Answer:**

UDP (User Datagram Protocol) is connectionless and provides faster communication without guaranteeing packet delivery.

---

# Ethernet

---

## Q21. What is Ethernet?

**Answer:**

Ethernet is the most widely used wired Local Area Network (LAN) technology defined by the IEEE 802.3 standard.

---

## Q22. What is a MAC address?

**Answer:**

A Media Access Control (MAC) address is a unique 48-bit hardware identifier assigned to a network interface card (NIC).

Example:

```
00:1A:2B:3C:4D:5E
```

---

## Q23. What is the difference between a MAC address and an IP address?

| MAC Address | IP Address |
|--------------|------------|
| Physical address | Logical address |
| Layer 2 | Layer 3 |
| Assigned by manufacturer | Assigned by administrator or DHCP |
| Used within LAN | Used for routing between networks |

---

## Q24. What is a broadcast domain?

**Answer:**

A broadcast domain is a group of devices that receive the same broadcast traffic. Routers separate broadcast domains, while switches forward broadcasts within the same VLAN.

---

## Q25. What is a collision domain?

**Answer:**

A collision domain is a network segment where packet collisions can occur. Modern switches create a separate collision domain for each port.

---

# IPv4

---

## Q26. What is IPv4?

**Answer:**

IPv4 is a 32-bit Internet Protocol used for logical addressing and routing.

Example:

```
192.168.1.100
```

---

## Q27. How many addresses does IPv4 support?

**Answer:**

IPv4 provides approximately **4.3 billion** unique addresses (2³²).

---

## Q28. What are private IPv4 address ranges?

**Answer:**

| Range | CIDR |
|---------|------|
| 10.0.0.0 – 10.255.255.255 | /8 |
| 172.16.0.0 – 172.31.255.255 | /12 |
| 192.168.0.0 – 192.168.255.255 | /16 |

---

## Q29. What is a subnet mask?

**Answer:**

A subnet mask separates the network portion of an IP address from the host portion.

Example:

```
255.255.255.0
```

---

## Q30. What is the default gateway?

**Answer:**

The default gateway is the router used to forward traffic from the local network to other networks.

---

## Q31. What is NAT?

**Answer:**

Network Address Translation (NAT) translates private IP addresses into public IP addresses, conserving IPv4 address space and providing an additional layer of abstraction.

---

# IPv6

---

## Q32. Why was IPv6 introduced?

**Answer:**

IPv6 was introduced to overcome IPv4 address exhaustion and provide improved scalability, security, and routing efficiency.

---

## Q33. How large is an IPv6 address?

**Answer:**

IPv6 uses **128-bit** addresses.

Example:

```
2001:db8::1
```

---

## Q34. What are the advantages of IPv6?

**Answer:**

Advantages include:

- Larger address space
- Better routing efficiency
- Simplified header format
- Built-in support for IPsec
- Stateless Address Autoconfiguration (SLAAC)
- Improved multicast support

---

## Q35. What is SLAAC?

**Answer:**

Stateless Address Autoconfiguration (SLAAC) enables IPv6 hosts to automatically configure their own addresses without requiring a DHCP server.

---

# Subnetting

---

## Q36. Why is subnetting used?

**Answer:**

Subnetting divides a large network into smaller logical networks to improve performance, security, address utilization, and routing efficiency.

---

## Q37. What is CIDR?

**Answer:**

Classless Inter-Domain Routing (CIDR) uses prefix notation (for example, `/24`) instead of traditional address classes to allocate IP address ranges more efficiently.

---

## Q38. How many usable hosts are available in a /24 subnet?

**Answer:**

A `/24` subnet contains:

- Total addresses: **256**
- Usable host addresses: **254**

(The network and broadcast addresses are reserved.)

---

## Q39. How many usable hosts are available in a /30 subnet?

**Answer:**

A `/30` subnet contains:

- Total addresses: **4**
- Usable host addresses: **2**

This is commonly used for point-to-point links.

---

## Q40. Why is subnetting important in enterprise networks?

**Answer:**

Subnetting improves:

- Network performance
- Security through segmentation
- Efficient IP address allocation
- Broadcast control
- Routing scalability
- Administrative management

---

# Quick Interview Tips

During networking interviews:

- Explain concepts using simple language before adding technical detail.
- Relate answers to real-world enterprise environments.
- Mention troubleshooting methodologies when appropriate.
- Use networking terminology accurately.
- If asked a scenario, explain your investigation process step by step.

---

# Key Takeaways

- Networking fundamentals form the foundation of every infrastructure and cybersecurity role.
- A strong understanding of the OSI and TCP/IP models is essential for troubleshooting.
- Ethernet, IPv4, IPv6, and subnetting are frequently tested in technical interviews.
- Interviewers value both conceptual understanding and practical problem-solving skills.

---


# Part 2 — Routing, Switching, VLANs, STP, ARP, DHCP, DNS, TCP, UDP, ICMP, Firewalls, VPNs, Wireless, and Enterprise Networking Interview Questions

---

# Introduction

Enterprise networking interviews typically move beyond basic networking concepts and focus on how networks actually operate in production environments.

Interviewers often expect candidates to explain:

- Packet forwarding
- Routing decisions
- Switching operations
- VLAN segmentation
- DHCP and DNS workflows
- Firewall behavior
- VPN connectivity
- Wireless networking
- Enterprise architectures
- Troubleshooting methodologies

This section contains commonly asked interview questions with concise, technically accurate answers.

---

# Routing

---

## Q41. What is routing?

**Answer:**

Routing is the process of forwarding packets between different networks using routing tables and routing protocols to determine the best available path.

---

## Q42. What is the difference between routing and switching?

| Routing | Switching |
|----------|-----------|
| Operates at Layer 3 | Operates at Layer 2 |
| Uses IP addresses | Uses MAC addresses |
| Connects different networks | Connects devices within the same LAN |
| Performed by routers or Layer 3 switches | Performed by switches |

---

## Q43. What is a routing table?

**Answer:**

A routing table contains information about destination networks, next-hop addresses, outgoing interfaces, metrics, and administrative distances used to forward packets.

---

## Q44. What is the default route?

**Answer:**

A default route is used when no more specific route exists for the destination network.

Example:

```
0.0.0.0/0
```

---

## Q45. What is the difference between static and dynamic routing?

| Static Routing | Dynamic Routing |
|----------------|-----------------|
| Configured manually | Learned automatically |
| Simple environments | Large enterprise networks |
| Minimal overhead | Adapts to topology changes |
| Limited scalability | Highly scalable |

---

## Q46. Name some dynamic routing protocols.

**Answer:**

Common routing protocols include:

- RIP
- OSPF
- EIGRP (Cisco proprietary)
- IS-IS
- BGP

---

## Q47. Which routing protocol is primarily used on the Internet?

**Answer:**

Border Gateway Protocol (BGP) is the primary routing protocol used to exchange routing information between Autonomous Systems (AS).

---

## Q48. What is route convergence?

**Answer:**

Route convergence is the process by which routers update their routing tables and agree on the current network topology after a topology change.

---

# Switching

---

## Q49. What is a network switch?

**Answer:**

A switch forwards Ethernet frames between devices within the same LAN using MAC address tables.

---

## Q50. How does a switch learn MAC addresses?

**Answer:**

A switch learns MAC addresses by recording the source MAC address of incoming frames and associating it with the receiving interface.

---

## Q51. What happens when the destination MAC address is unknown?

**Answer:**

The switch floods the frame to all ports within the VLAN except the port on which it was received.

---

## Q52. What is a Layer 3 switch?

**Answer:**

A Layer 3 switch combines switching and routing capabilities, allowing high-speed routing between VLANs.

---

# VLANs

---

## Q53. What is a VLAN?

**Answer:**

A Virtual Local Area Network (VLAN) logically separates devices into independent broadcast domains regardless of physical location.

---

## Q54. Why are VLANs used?

**Answer:**

VLANs improve:

- Security
- Broadcast control
- Network organization
- Performance
- Administrative flexibility

---

## Q55. What is an access port?

**Answer:**

An access port belongs to a single VLAN and connects end devices such as computers, printers, and IP phones.

---

## Q56. What is a trunk port?

**Answer:**

A trunk port carries traffic for multiple VLANs between switches or between a switch and a router using IEEE 802.1Q tagging.

---

## Q57. What is the native VLAN?

**Answer:**

The native VLAN carries untagged traffic on an IEEE 802.1Q trunk link. Both ends of the trunk should use the same native VLAN to avoid communication issues.

---

# Spanning Tree Protocol (STP)

---

## Q58. Why is STP required?

**Answer:**

STP prevents Layer 2 loops by blocking redundant paths while maintaining backup links.

---

## Q59. What happens if STP is disabled in a redundant switched network?

**Answer:**

Disabling STP can lead to:

- Broadcast storms
- MAC address instability
- Multiple frame copies
- Network outages

---

## Q60. What is the root bridge?

**Answer:**

The root bridge is the central reference switch selected by STP. All path calculations are performed relative to the root bridge.

---

# ARP

---

## Q61. What is ARP?

**Answer:**

The Address Resolution Protocol (ARP) maps IPv4 addresses to MAC addresses within a local network.

---

## Q62. How does ARP work?

**Answer:**

1. A host broadcasts an ARP Request asking, "Who has this IP address?"
2. The device with the matching IP replies with its MAC address.
3. The sender stores the mapping in its ARP cache.

---

## Q63. What is ARP spoofing?

**Answer:**

ARP spoofing is an attack in which an attacker sends forged ARP replies to associate their MAC address with another device's IP address, enabling traffic interception or manipulation.

---

# DHCP

---

## Q64. What is DHCP?

**Answer:**

Dynamic Host Configuration Protocol (DHCP) automatically assigns IP configuration to network devices, including IP address, subnet mask, default gateway, and DNS servers.

---

## Q65. Explain the DHCP process.

**Answer:**

The DHCP process follows the DORA sequence:

```
Discover

↓

Offer

↓

Request

↓

Acknowledge
```

---

## Q66. What is a DHCP relay agent?

**Answer:**

A DHCP relay agent forwards DHCP requests between clients and DHCP servers located on different IP subnets.

---

# DNS

---

## Q67. What is DNS?

**Answer:**

The Domain Name System (DNS) translates human-readable domain names into IP addresses.

---

## Q68. What happens when you type a website into a browser?

**Answer:**

The simplified process is:

```
User

↓

DNS Lookup

↓

IP Address

↓

TCP Connection

↓

TLS Handshake (HTTPS)

↓

HTTP Request

↓

Web Server Response
```

---

## Q69. What is the difference between recursive and iterative DNS queries?

| Recursive Query | Iterative Query |
|-----------------|-----------------|
| Resolver returns the final answer | Each DNS server returns the best available information |
| Common for clients | Common between DNS servers |

---

## Q70. What is DNS caching?

**Answer:**

DNS caching stores previously resolved domain names locally to reduce lookup times and decrease DNS server load.

---

# TCP

---

## Q71. What is TCP?

**Answer:**

Transmission Control Protocol (TCP) is a connection-oriented transport protocol that provides reliable, ordered, and error-checked data delivery.

---

## Q72. Explain the TCP three-way handshake.

**Answer:**

```
Client → SYN

↓

Server → SYN-ACK

↓

Client → ACK

↓

Connection Established
```

---

## Q73. Why does TCP use acknowledgments?

**Answer:**

Acknowledgments confirm successful packet delivery and enable retransmission if packets are lost.

---

# UDP

---

## Q74. What is UDP?

**Answer:**

User Datagram Protocol (UDP) is a connectionless transport protocol that prioritizes speed over reliability.

---

## Q75. When is UDP preferred?

**Answer:**

UDP is commonly used for:

- DNS
- VoIP
- Video streaming
- Online gaming
- Live broadcasts

---

## Q76. What is the primary difference between TCP and UDP?

| TCP | UDP |
|------|-----|
| Connection-oriented | Connectionless |
| Reliable | Best effort |
| Ordered delivery | No delivery guarantee |
| Higher overhead | Lower overhead |

---

# ICMP

---

## Q77. What is ICMP?

**Answer:**

Internet Control Message Protocol (ICMP) is used for network diagnostics and error reporting.

---

## Q78. Which commands commonly use ICMP?

**Answer:**

- `ping`
- `traceroute` (or `tracert` on Windows, which may also use ICMP depending on the implementation)

---

## Q79. Why might ICMP be blocked?

**Answer:**

Organizations may restrict ICMP to reduce network reconnaissance opportunities or limit certain denial-of-service attack vectors, while still allowing necessary diagnostic traffic.

---

# Firewalls

---

## Q80. What is a firewall?

**Answer:**

A firewall monitors and controls inbound and outbound network traffic according to predefined security policies.

---

## Q81. What is the difference between a stateful firewall and a stateless firewall?

| Stateless Firewall | Stateful Firewall |
|--------------------|------------------|
| Examines individual packets | Tracks connection state |
| Faster | More secure |
| Limited context | Context-aware decisions |

---

## Q82. What is NAT?

**Answer:**

Network Address Translation (NAT) translates private IP addresses into public IP addresses or vice versa.

---

## Q83. What is the purpose of a DMZ?

**Answer:**

A Demilitarized Zone (DMZ) isolates public-facing servers from internal networks to reduce the risk of compromise.

---

# VPN

---

## Q84. What is a VPN?

**Answer:**

A Virtual Private Network (VPN) creates an encrypted tunnel across an untrusted network, allowing secure communication between users or sites.

---

## Q85. What are the two common VPN types?

**Answer:**

- Site-to-Site VPN
- Remote Access VPN

---

## Q86. What is IPsec?

**Answer:**

IPsec is a suite of protocols that provides authentication, integrity, and encryption for IP communications.

---

# Wireless Networking

---

## Q87. What is an SSID?

**Answer:**

The Service Set Identifier (SSID) is the name of a wireless network that clients use to identify and connect to it.

---

## Q88. What are common causes of poor Wi-Fi performance?

**Answer:**

- Weak signal strength
- RF interference
- Channel congestion
- Too many connected clients
- Physical obstacles
- Misconfigured access points

---

## Q89. What is WPA3?

**Answer:**

WPA3 is the latest Wi-Fi security standard, providing stronger authentication and improved protection against password guessing attacks compared to WPA2.

---

# Enterprise Networking

---

## Q90. Why is network segmentation important?

**Answer:**

Network segmentation limits broadcast traffic, improves performance, enhances security, reduces lateral movement, and simplifies regulatory compliance.

---

## Quick Interview Tips

For enterprise networking interviews:

- Explain **why** a technology is used, not just **what** it does.
- Mention operational considerations such as scalability, security, and availability.
- Use troubleshooting examples where appropriate.
- Be prepared to compare similar technologies (for example, TCP vs UDP or static vs dynamic routing).

---

# Key Takeaways

- Routing and switching are fundamental to enterprise connectivity.
- VLANs, STP, DHCP, and DNS are among the most frequently tested networking topics.
- Understanding TCP, UDP, ICMP, firewalls, VPNs, and wireless networking is essential for infrastructure and cybersecurity roles.
- Employers value candidates who can connect theoretical knowledge to practical enterprise scenarios.

---


