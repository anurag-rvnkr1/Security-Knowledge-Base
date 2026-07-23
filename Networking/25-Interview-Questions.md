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
