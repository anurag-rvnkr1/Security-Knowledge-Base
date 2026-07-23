# 04 - Ethernet

# Part 1 — Ethernet Fundamentals, Architecture, Standards, and Enterprise LAN Communication

---

# Overview

Ethernet is the **most widely deployed Local Area Network (LAN) technology** in the world. Nearly every enterprise network, data center, campus infrastructure, cloud edge environment, and office LAN relies on Ethernet for reliable communication between devices.

Originally standardized by the **Institute of Electrical and Electronics Engineers (IEEE)** as **IEEE 802.3**, Ethernet defines how devices communicate over wired networks by specifying:

- Frame format
- Physical media
- MAC addressing
- Data transmission
- Error detection
- Link establishment
- Speed standards

Today, Ethernet supports communication ranging from **10 Mbps to 800 Gbps**, making it the backbone of modern enterprise networking.

---

# Learning Objectives

After completing this chapter, you should be able to:

- Understand Ethernet architecture.
- Explain IEEE 802.3 standards.
- Understand Ethernet frame structure.
- Explain MAC addressing.
- Differentiate collision domains and broadcast domains.
- Understand duplex communication.
- Identify Ethernet devices.
- Analyze Ethernet traffic in Wireshark.
- Understand enterprise Ethernet deployments.

---

# What is Ethernet?

Ethernet is a family of networking technologies used for communication within a **Local Area Network (LAN)**.

It operates primarily at:

- **OSI Layer 1 (Physical Layer)** — Defines how bits are transmitted over the medium.
- **OSI Layer 2 (Data Link Layer)** — Defines framing, MAC addressing, and local delivery.

In the TCP/IP Model, Ethernet belongs to the **Network Access Layer**.

---

# History of Ethernet

| Year | Milestone |
|------|-----------|
| 1973 | Ethernet developed at Xerox PARC by Robert Metcalfe |
| 1980 | Ethernet Version 1.0 released |
| 1983 | IEEE standardized Ethernet as IEEE 802.3 |
| 1995 | Fast Ethernet (100 Mbps) |
| 1998 | Gigabit Ethernet |
| 2002 | 10 Gigabit Ethernet |
| Today | 25G, 40G, 100G, 200G, 400G, and 800G Ethernet deployments |

Ethernet evolved from a shared-medium technology using coaxial cables into today's switched full-duplex architecture used in enterprise and cloud environments.

---

# Why Ethernet Became the Industry Standard

Ethernet became dominant because it provides:

- Open standards
- Vendor interoperability
- High performance
- Low cost
- Scalability
- Reliability
- Backward compatibility
- Ease of deployment

These characteristics allowed Ethernet to replace many proprietary LAN technologies.

---

# Ethernet Architecture

A simplified enterprise Ethernet network:

```
                 Internet
                     │
               Edge Firewall
                     │
                 Core Router
                     │
              Layer 3 Switch
                     │
        ┌────────────┼────────────┐
        │            │            │
   Access Switch  Access Switch  Access Switch
        │            │            │
     PC / Laptop   IP Phone     Printer
        │
   Wireless Access Point
```

In this architecture:

- Routers connect different networks.
- Switches forward Ethernet frames within the LAN.
- End devices communicate using MAC addresses.

---

# Ethernet Communication

Communication occurs using **frames**.

Unlike IP packets, Ethernet frames are designed for communication within the local network segment.

Example:

```
Laptop

↓

Ethernet Frame

↓

Switch

↓

Server
```

Each frame contains addressing information that enables switches to forward traffic efficiently.

---

# IEEE 802 Standards

Ethernet is part of the IEEE 802 family of networking standards.

| Standard | Description |
|----------|-------------|
| IEEE 802.3 | Ethernet |
| IEEE 802.11 | Wi-Fi |
| IEEE 802.1Q | VLAN Tagging |
| IEEE 802.1D | Spanning Tree Protocol (STP) |
| IEEE 802.1X | Port-Based Network Access Control |
| IEEE 802.3af | Power over Ethernet (PoE) |
| IEEE 802.3at | PoE+ |
| IEEE 802.3bt | PoE++ |

These standards define how enterprise networks achieve interoperability and consistent behavior across vendors.

---

# Ethernet Components

A typical Ethernet network includes:

- Network Interface Cards (NICs)
- Switches
- Routers
- Ethernet cables
- Fiber optic links
- Patch panels
- Connectors (RJ-45, LC, SC)
- Transceivers (SFP, SFP+, QSFP)

---

# Ethernet Transmission Media

Ethernet supports both copper and fiber optic media.

## Copper

Common cable categories:

| Cable | Maximum Speed | Typical Distance |
|--------|---------------|------------------|
| Cat5e | 1 Gbps | 100 meters |
| Cat6 | 1–10 Gbps* | 100 m (1 Gbps), shorter for 10 Gbps depending on installation |
| Cat6a | 10 Gbps | 100 meters |
| Cat7* | 10 Gbps | 100 meters |
| Cat8 | 25–40 Gbps | 30 meters |

> *Cat7 is not part of the IEEE 802.3 twisted-pair cabling recommendations but is used in some environments.

---

## Fiber Optic

Common fiber types:

| Fiber Type | Core Size | Typical Use |
|-------------|-----------|-------------|
| Single Mode (SMF) | ~9 µm | Long-distance links |
| Multi Mode (MMF) | 50/62.5 µm | Campus and data centers |

Fiber provides:

- Higher bandwidth
- Longer transmission distances
- Resistance to electromagnetic interference
- Lower attenuation

---

# Ethernet Speeds

| Standard | Speed |
|----------|-------|
| Ethernet | 10 Mbps |
| Fast Ethernet | 100 Mbps |
| Gigabit Ethernet | 1 Gbps |
| 10 Gigabit Ethernet | 10 Gbps |
| 25 Gigabit Ethernet | 25 Gbps |
| 40 Gigabit Ethernet | 40 Gbps |
| 100 Gigabit Ethernet | 100 Gbps |
| 200 Gigabit Ethernet | 200 Gbps |
| 400 Gigabit Ethernet | 400 Gbps |
| 800 Gigabit Ethernet | 800 Gbps |

Modern enterprise backbones and hyperscale data centers commonly use 100G, 200G, 400G, or higher links.

---

# Ethernet Interfaces

Examples include:

```
RJ-45 Copper

↓

SFP

↓

SFP+

↓

QSFP+

↓

QSFP28

↓

QSFP-DD
```

These interfaces support different speeds, cable types, and deployment scenarios.

---

# Enterprise Example

Consider an employee accessing an internal file server.

```
Laptop

↓

NIC

↓

Access Switch

↓

Distribution Switch

↓

Core Switch

↓

File Server
```

The communication remains within the enterprise LAN, and Ethernet frames are forwarded based on destination MAC addresses.

---

# Ethernet Advantages

- High throughput
- Low latency
- Reliable communication
- Vendor interoperability
- Cost-effective deployment
- Scalable architecture
- Mature ecosystem
- Strong standards support

---

# Ethernet Limitations

- Designed primarily for local area communication.
- Frame delivery is limited to the local Layer 2 domain.
- Broadcast traffic can increase as networks grow without segmentation.
- Physical infrastructure requires careful planning and maintenance.

---

# Ethernet in Cybersecurity

Ethernet is frequently analyzed during:

- Network traffic monitoring
- Packet analysis
- Digital forensics
- Incident response
- Threat hunting
- Malware investigations
- Intrusion detection

Understanding Ethernet helps analysts identify abnormal Layer 2 behavior such as unauthorized devices, MAC spoofing, and ARP-based attacks.

---

# Wireshark Observation

When capturing Ethernet traffic, the first protocol shown is typically:

```
Frame

↓

Ethernet II

↓

IPv4 / IPv6

↓

TCP / UDP

↓

Application Protocol
```

Selecting the Ethernet header reveals fields such as source MAC, destination MAC, and EtherType.

---

# Key Takeaways

- Ethernet is the dominant LAN technology standardized as IEEE 802.3.
- It operates at the Physical and Data Link layers of the OSI Model and the Network Access layer of the TCP/IP Model.
- Ethernet uses frames and MAC addresses for local communication.
- Modern Ethernet supports speeds ranging from 10 Mbps to hundreds of gigabits per second.
- Enterprise networks rely on Ethernet for reliable, scalable, and interoperable local connectivity.