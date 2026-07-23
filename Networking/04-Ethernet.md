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

# 04 - Ethernet

# Part 2 — Ethernet Frames, MAC Addressing, Frame Processing, MTU, and Wireshark Analysis

---

# Overview

Every Ethernet communication occurs through an **Ethernet Frame**.

Unlike IP packets, which are responsible for communication across networks, Ethernet frames are responsible for communication **within the local Layer 2 network**.

Whenever a computer sends data to another device on the same LAN, the information is encapsulated inside an Ethernet frame before transmission.

Understanding Ethernet frames is essential for:

- Network Engineers
- SOC Analysts
- Detection Engineers
- Incident Responders
- Digital Forensics Analysts
- Penetration Testers

---

# What is an Ethernet Frame?

An Ethernet frame is the **Layer 2 Protocol Data Unit (PDU)** used for transmitting data across an Ethernet network.

```
Application Data

↓

TCP Segment

↓

IP Packet

↓

Ethernet Frame

↓

Bits
```

The Ethernet frame wraps the IP packet with local addressing information so that switches can deliver it to the correct destination.

---

# Ethernet II Frame Format

The most common Ethernet frame format used today is **Ethernet II**.

```
+----------+----------+-----------+--------------------+-----------+
| Dest MAC | Src MAC  | EtherType | Payload            | FCS       |
| 6 Bytes  | 6 Bytes  | 2 Bytes   | 46–1500 Bytes      | 4 Bytes   |
+----------+----------+-----------+--------------------+-----------+
```

> The **Preamble** and **Start Frame Delimiter (SFD)** are transmitted on the wire by the physical layer but are typically not displayed by packet analyzers such as Wireshark.

---

# Ethernet Frame Components

## 1. Destination MAC Address

Length:

```
6 Bytes
```

Purpose:

Specifies the intended recipient on the local network.

Example:

```
00:1A:2B:3C:4D:5E
```

The switch uses this address to determine the correct outgoing interface.

---

## 2. Source MAC Address

Length:

```
6 Bytes
```

Purpose:

Identifies the sender of the frame.

Example:

```
F4:92:BF:11:22:33
```

Switches learn this address and associate it with the incoming port.

---

## 3. EtherType

Length:

```
2 Bytes
```

Purpose:

Identifies the protocol encapsulated in the payload.

Common EtherType values:

| EtherType | Protocol |
|-----------|----------|
| 0x0800 | IPv4 |
| 0x0806 | ARP |
| 0x86DD | IPv6 |
| 0x8100 | IEEE 802.1Q VLAN Tag |
| 0x88CC | LLDP |

Example:

```
EtherType

↓

IPv4
```

The receiving device uses this field to determine how to interpret the payload.

---

## 4. Payload

Contains the encapsulated Layer 3 packet.

Example:

```
IPv4 Packet

↓

TCP Segment

↓

HTTPS Request
```

Payload size:

```
46–1500 Bytes
```

If the payload is smaller than 46 bytes, padding is added to satisfy the minimum Ethernet frame size.

---

## 5. Frame Check Sequence (FCS)

Length:

```
4 Bytes
```

Purpose:

Detects accidental transmission errors.

The sender computes a **Cyclic Redundancy Check (CRC)** value and places it in the FCS field.

The receiver recalculates the CRC:

- If the values match, the frame is accepted.
- If they differ, the frame is discarded.

> FCS detects random transmission errors but does **not** provide cryptographic integrity or authentication.

---

# Ethernet Frame Size

| Component | Size |
|-----------|------|
| Destination MAC | 6 Bytes |
| Source MAC | 6 Bytes |
| EtherType | 2 Bytes |
| Payload | 46–1500 Bytes |
| FCS | 4 Bytes |

Typical frame sizes:

| Frame | Size |
|--------|------|
| Minimum Ethernet Frame | 64 Bytes |
| Maximum Standard Frame | 1518 Bytes |
| Maximum with 802.1Q VLAN Tag | 1522 Bytes |

---

# Jumbo Frames

Some environments support **jumbo frames**, which allow payloads larger than the standard MTU.

Typical values:

```
9000 Bytes MTU
```

Benefits:

- Reduced CPU overhead
- Fewer packets for large transfers
- Improved storage and virtualization performance

Common use cases:

- Data centers
- Storage Area Networks (SANs)
- VMware environments
- Backup networks
- High-performance computing

All devices along the communication path must support the configured jumbo frame size.

---

# IEEE 802.3 Frame Format

Historically, IEEE 802.3 used a **Length** field instead of EtherType.

```
+-----------+-----------+---------+---------+---------+
| Dest MAC  | Src MAC   | Length  | Payload | FCS     |
+-----------+-----------+---------+---------+---------+
```

Modern enterprise networks predominantly use **Ethernet II**, while IEEE 802.3 with LLC/SNAP headers is encountered less frequently.

---

# MAC Address

A **Media Access Control (MAC) Address** is a Layer 2 hardware identifier assigned to a network interface.

Example:

```
3C:52:82:9F:10:7A
```

Characteristics:

- 48 bits
- 6 bytes
- Usually represented in hexadecimal
- Intended to be unique within the global address space

---

# MAC Address Structure

```
3C:52:82 : 9F:10:7A

↑           ↑

OUI      Device Identifier
```

The first 24 bits identify the vendor.

The last 24 bits identify the specific interface assigned by that vendor.

---

# Organizationally Unique Identifier (OUI)

The **OUI** identifies the manufacturer of the network interface.

Example:

```
3C:52:82

↓

Vendor
```

Examples of vendors include:

- Intel
- Dell
- Cisco
- HPE
- Lenovo

Wireshark can often resolve the OUI and display the associated vendor name.

---

# Types of MAC Addresses

## Unicast

Communication to a single device.

```
PC A

↓

PC B
```

Most Ethernet communication is unicast.

---

## Broadcast

Communication to **every device** within the broadcast domain.

Broadcast MAC:

```
FF:FF:FF:FF:FF:FF
```

Examples:

- ARP Requests
- DHCP Discover

---

## Multicast

Communication to a selected group of devices.

```
Server

↓

Multiple Subscribers
```

Examples:

- IPTV
- Streaming
- Routing protocols
- Service discovery

---

# MAC Learning

Ethernet switches build a **MAC Address Table** (also called a CAM table) by observing the source MAC address of incoming frames.

Example:

```
Port 1

↓

MAC A

Port 2

↓

MAC B

Port 3

↓

MAC C
```

When a frame arrives:

1. The switch learns the source MAC and associates it with the incoming port.
2. The switch looks up the destination MAC in its table.
3. If found, it forwards the frame only to the correct port.
4. If unknown, it floods the frame to all ports except the incoming port.

This learning process allows efficient forwarding while minimizing unnecessary traffic.

---

# MAC Address Table Example

| MAC Address | Switch Port |
|-------------|-------------|
| 00:11:22:33:44:55 | Gi0/1 |
| 08:AA:BB:CC:DD:EE | Gi0/2 |
| 3C:52:82:9F:10:7A | Gi0/3 |

The table is continuously updated as devices communicate.

---

# MTU (Maximum Transmission Unit)

The **Maximum Transmission Unit (MTU)** defines the largest Layer 3 packet that can be carried within an Ethernet frame without fragmentation.

Standard Ethernet MTU:

```
1500 Bytes
```

If a packet exceeds the MTU:

- IPv4 may fragment the packet (unless fragmentation is prohibited).
- Many modern networks rely on **Path MTU Discovery (PMTUD)** to avoid fragmentation.
- IPv6 routers do not fragment packets; fragmentation is handled only by the source host when necessary.

---

# Ethernet Encapsulation

```
Application Data

↓

TCP Header

↓

IP Header

↓

Ethernet Header

↓

Transmission

↓

Ethernet Trailer (FCS)
```

This encapsulation enables local delivery while preserving the higher-layer information.

---

# Example Ethernet Frame

```
+------------------------------------------------------+
| Destination MAC                                      |
+------------------------------------------------------+
| Source MAC                                           |
+------------------------------------------------------+
| EtherType = IPv4                                     |
+------------------------------------------------------+
| IPv4 Header                                          |
+------------------------------------------------------+
| TCP Header                                           |
+------------------------------------------------------+
| HTTPS Data                                           |
+------------------------------------------------------+
| FCS                                                  |
+------------------------------------------------------+
```

---

# Wireshark Analysis

A captured Ethernet frame typically appears as:

```
Frame

↓

Ethernet II

↓

Internet Protocol Version 4

↓

Transmission Control Protocol

↓

Transport Layer Security

↓

Hypertext Transfer Protocol
```

Selecting **Ethernet II** reveals:

- Destination MAC
- Source MAC
- EtherType

Selecting **IPv4** reveals:

- Source IP
- Destination IP
- TTL

Selecting **TCP** reveals:

- Source Port
- Destination Port
- Sequence Number
- Flags

---

# Common Ethernet Frame Issues

| Issue | Description |
|--------|-------------|
| CRC Errors | Corrupted frame detected by FCS |
| Runts | Frames smaller than the minimum valid size |
| Giants | Frames larger than the configured maximum size |
| MTU Mismatch | Devices use incompatible MTU values |
| Unknown Unicast Flooding | Destination MAC not present in the switch's MAC table |
| Excessive Broadcast Traffic | Large numbers of broadcast frames reducing network efficiency |

---

# Business Impact

Understanding Ethernet frames enables professionals to:

- Diagnose Layer 2 connectivity issues
- Investigate packet corruption
- Analyze packet captures
- Optimize LAN performance
- Troubleshoot switching problems
- Detect abnormal Layer 2 behavior
- Perform effective network forensics

---

# Key Takeaways

- Ethernet II is the dominant frame format in modern networks.
- Every Ethernet frame contains destination and source MAC addresses, an EtherType field, payload, and an FCS.
- MAC addresses identify network interfaces on the local network, while switches use MAC tables to forward frames efficiently.
- Standard Ethernet MTU is 1500 bytes, while jumbo frames are commonly used in specialized environments.
- Packet analyzers such as Wireshark expose Ethernet headers, making them invaluable for troubleshooting and cybersecurity investigations.

# 04 - Ethernet

# Part 3 — Ethernet Switching, CAM Tables, Frame Forwarding, Collision Domains, Broadcast Domains, Duplex Modes, and Enterprise Layer 2 Communication

---

# Overview

Modern Ethernet networks rely heavily on **switches**.

Unlike early Ethernet networks that used hubs and shared communication media, enterprise networks today use **Layer 2 Ethernet switches** to provide:

- High bandwidth
- Dedicated communication paths
- Low latency
- Collision-free communication
- Efficient frame forwarding
- Network segmentation

Understanding how switches operate is essential for:

- Network Engineers
- SOC Analysts
- Incident Responders
- Penetration Testers
- Detection Engineers
- Infrastructure Engineers

---

# What is an Ethernet Switch?

An Ethernet switch is a **Layer 2 networking device** that forwards Ethernet frames based on **MAC addresses**.

Unlike routers, switches **do not normally examine IP addresses** when making forwarding decisions.

Instead, they inspect:

```
Destination MAC Address
```

and determine which switch port should receive the frame.

---

# Enterprise Example

```
            Core Switch
                 │
      ┌──────────┼──────────┐
      │          │          │
   Access      Access     Access
   Switch      Switch     Switch
      │          │          │
   Laptop      Server    Printer
```

Every switch maintains a MAC address table that allows it to forward frames efficiently.

---

# Switch Components

A managed Ethernet switch typically contains:

- Switching ASIC (Application-Specific Integrated Circuit)
- CPU (management plane)
- CAM Table
- Memory buffers
- Ethernet interfaces
- Backplane/Fabric
- Management interface (CLI/Web/SNMP)

```
+--------------------------------+
|            Switch              |
|                                |
|  CPU                           |
|  Switching ASIC                |
|  CAM Table                     |
|  Buffers                       |
|                                |
| Gi0/1 Gi0/2 Gi0/3 Gi0/24       |
+--------------------------------+
```

---

# What is a CAM Table?

CAM stands for:

```
Content Addressable Memory
```

A CAM table stores:

```
MAC Address

↓

Switch Port
```

Example

| MAC Address | Port |
|-------------|------|
| 00:11:22:33:44:55 | Gi0/1 |
| 10:AA:BB:CC:DD:EE | Gi0/2 |
| 3C:52:82:9F:10:7A | Gi0/3 |

The CAM table allows the switch to forward frames directly to the correct destination.

---

# MAC Learning Process

Switches automatically build their CAM table by inspecting the **source MAC address** of every incoming frame.

### Step 1

Frame arrives:

```
Source MAC

AA:AA:AA:AA:AA:AA

↓

Port Gi0/1
```

The switch learns:

```
AA:AA:AA:AA:AA:AA

↓

Gi0/1
```

### Step 2

Another frame arrives.

```
Source MAC

BB:BB:BB:BB:BB:BB

↓

Gi0/2
```

The switch stores:

```
BB:BB:BB:BB:BB:BB

↓

Gi0/2
```

Over time the CAM table becomes a map of the local network.

---

# Frame Forwarding Process

Every Ethernet frame follows three basic steps.

## Step 1

Receive frame.

↓

Read

```
Source MAC
Destination MAC
```

---

## Step 2

Learn Source MAC

If new:

```
Store in CAM Table
```

If already known:

```
Refresh timer
```

---

## Step 3

Lookup Destination MAC

If found:

```
Forward to one port
```

If unknown:

```
Flood
```

---

# Example Communication

```
PC A

↓

Switch

↓

PC B
```

Frame

```
Destination

BB:BB:BB:BB:BB:BB
```

Switch checks CAM table.

Found.

↓

Forward only to

```
Gi0/2
```

No other devices receive the frame.

---

# Unknown Unicast

Suppose:

```
Destination MAC

CC:CC:CC:CC:CC:CC
```

is not present in the CAM table.

The switch performs:

```
Unknown Unicast Flood
```

```
Incoming Port

↓

All Other Ports
```

Eventually:

```
Destination Replies

↓

Switch Learns MAC
```

Future frames become unicast.

---

# Broadcast Frames

Broadcast destination:

```
FF:FF:FF:FF:FF:FF
```

Example:

ARP Request

```
Who has

192.168.1.10

?
```

Switch forwards broadcast frames to:

```
Every Port

Except Incoming Port
```

Broadcasts remain within the broadcast domain unless routed.

---

# Multicast Frames

Multicast traffic targets a selected group of devices.

Example applications:

- IPTV
- Video conferencing
- Routing protocols
- Streaming
- Service discovery

Without multicast optimization, switches may flood multicast traffic similarly to broadcast traffic.

Enterprise switches often use protocols such as **IGMP Snooping** to forward multicast traffic only to interested receivers.

---

# Unknown vs Broadcast vs Multicast

| Traffic Type | Destination | Forwarding Behavior |
|--------------|-------------|---------------------|
| Unicast | One MAC | One port |
| Unknown Unicast | Unknown MAC | Flood |
| Broadcast | FF:FF:FF:FF:FF:FF | Flood |
| Multicast | Multicast MAC | Selected ports (or flooded if unmanaged) |

---

# CAM Table Aging

MAC entries are **not permanent**.

If a device stops communicating:

```
Timer Expires

↓

Entry Removed
```

When communication resumes:

```
Switch Learns Again
```

This keeps the CAM table current.

---

# Collision Domains

A collision occurs when multiple devices transmit simultaneously on a shared medium.

Older Ethernet networks using hubs experienced frequent collisions.

Modern switches eliminate this problem.

```
Switch

↓

Each Port

↓

Separate Collision Domain
```

Example

```
PC1

↓

Switch

↓

PC2

↓

Switch

↓

Server
```

Every switch port is its own collision domain.

---

# Broadcast Domains

A broadcast domain is the set of devices that receive Layer 2 broadcast traffic.

Without VLANs:

```
Entire Switch

↓

One Broadcast Domain
```

With VLANs:

```
VLAN 10

↓

Broadcast Domain 1

────────────

VLAN 20

↓

Broadcast Domain 2
```

Routers and Layer 3 interfaces separate broadcast domains.

---

# Collision Domain vs Broadcast Domain

| Feature | Collision Domain | Broadcast Domain |
|----------|------------------|------------------|
| Layer | Physical/Data Link | Data Link |
| Managed By | Switch Ports | Routers / VLANs |
| Modern Switch | One per Port | Shared unless segmented |
| Goal | Prevent collisions | Limit broadcast traffic |

---

# Duplex Communication

Ethernet devices support different transmission modes.

---

## Half Duplex

Only one device transmits at a time.

```
A

────►

B

(wait)

◄────

B
```

Characteristics:

- Shared medium
- Possible collisions
- Legacy environments
- Lower performance

---

## Full Duplex

Both devices transmit simultaneously.

```
A

────►

◄────

B
```

Characteristics:

- No collisions
- Higher throughput
- Lower latency
- Standard in modern switched Ethernet

---

# Auto-Negotiation

Modern Ethernet interfaces automatically negotiate:

- Speed
- Duplex mode
- Link capabilities

Example:

```
NIC

↓

1 Gbps

↓

Full Duplex
```

If negotiation fails because of configuration mismatches, performance issues such as retransmissions or poor throughput may occur.

---

# Switching Methods

---

## Store-and-Forward

The switch receives the **entire frame**, verifies the FCS, and forwards only valid frames.

Advantages:

- Detects corrupted frames
- Most common in enterprise switches

Disadvantages:

- Slightly higher latency

---

## Cut-Through Switching

The switch begins forwarding after reading the destination MAC address.

Advantages:

- Very low latency

Disadvantages:

- May forward corrupted frames because the FCS has not yet been verified.

---

## Fragment-Free Switching

The switch reads the first **64 bytes** before forwarding.

Advantages:

- Avoids forwarding most collision fragments.
- Lower latency than store-and-forward.

---

# Comparison of Switching Methods

| Method | Error Checking | Latency | Enterprise Usage |
|----------|---------------|---------|------------------|
| Store-and-Forward | Yes | Moderate | Very Common |
| Cut-Through | No | Very Low | Specialized |
| Fragment-Free | Partial | Low | Less Common |

---

# Enterprise Switching Architecture

```
              Core Layer
                   │
         High-Speed Layer 3 Switches
                   │
        ┌──────────┴──────────┐
        │                     │
  Distribution Layer     Distribution Layer
        │                     │
   Access Switches      Access Switches
        │                     │
 End Devices         Servers / Printers / Phones
```

This hierarchical design improves:

- Scalability
- Fault isolation
- Performance
- Manageability

---

# Wireshark Observation

During a packet capture, you can inspect:

- Source MAC Address
- Destination MAC Address
- EtherType
- VLAN Tag (if present)
- Payload

Switch forwarding decisions are **not visible** in Wireshark because they occur internally within the switch hardware.

However, the Ethernet headers provide valuable insight into Layer 2 communication.

---

# Common Switching Problems

| Problem | Description |
|----------|-------------|
| MAC Table Overflow | CAM table becomes full, potentially causing flooding behavior |
| Broadcast Storm | Excessive broadcast traffic consumes network bandwidth |
| Duplex Mismatch | One side uses full duplex while the other uses half duplex, causing performance degradation |
| MAC Flapping | A MAC address rapidly appears on different ports, often indicating loops or misconfigurations |
| Unknown Unicast Flooding | Switch does not know the destination MAC and floods the frame |
| Layer 2 Loop | Redundant paths without loop prevention can create continuous frame circulation |

---

# Business Impact

Efficient Ethernet switching provides:

- High-performance LAN communication
- Reduced unnecessary traffic
- Low latency
- Collision-free operation
- Improved application performance
- Scalable enterprise network design
- Reliable communication for business-critical services

---

# Key Takeaways

- Ethernet switches forward frames using **MAC addresses**.
- Switches learn device locations dynamically through the **CAM table**.
- Known unicast traffic is forwarded only to the destination port, while unknown unicast and broadcast traffic may be flooded.
- Modern switched Ethernet provides one **collision domain per switch port**, while broadcast domains are controlled using **routers or VLANs**.
- Full-duplex communication eliminates collisions and is the standard for enterprise Ethernet.
- Store-and-forward switching is the dominant forwarding method because it verifies frame integrity before transmission.