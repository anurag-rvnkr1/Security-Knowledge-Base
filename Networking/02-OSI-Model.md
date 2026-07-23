# 02 - OSI Model

# Part 1 — Introduction to the OSI Model

---

# Overview

The **Open Systems Interconnection (OSI) Model** is one of the most important concepts in computer networking and cybersecurity.

Although the Internet primarily operates using the **TCP/IP model**, the OSI model remains the universal framework for:

- Understanding network communication
- Learning networking concepts
- Troubleshooting connectivity issues
- Designing network architectures
- Understanding security controls
- Analyzing network attacks
- Performing packet analysis

Nearly every networking interview, cybersecurity certification, and enterprise networking discussion references the OSI Model.

Understanding the OSI Model allows engineers to determine **where communication occurs, where failures happen, and where security controls should be implemented.**

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain why the OSI Model was created.
- Understand the responsibilities of each layer.
- Describe how data moves through the layers.
- Understand encapsulation and decapsulation.
- Identify protocols operating at each layer.
- Troubleshoot networking issues using the OSI approach.
- Map cybersecurity attacks to individual OSI layers.
- Compare the OSI and TCP/IP models.

---

# What is the OSI Model?

The **OSI (Open Systems Interconnection) Model** is a **seven-layer conceptual framework** developed by the **International Organization for Standardization (ISO)** to standardize communication between different computer systems and networking devices.

Instead of defining specific protocols, the OSI model describes **how communication should occur**, dividing the networking process into independent layers with clearly defined responsibilities.

This layered approach enables equipment and software from different vendors to interoperate more effectively.

---

# Why Was the OSI Model Created?

Before networking standards existed, different manufacturers implemented proprietary networking solutions.

Examples included:

- Vendor-specific hardware
- Proprietary communication protocols
- Incompatible operating systems
- Closed networking ecosystems

This created interoperability challenges.

The OSI Model introduced a standardized reference architecture that separated networking into independent functional layers.

Benefits included:

- Vendor interoperability
- Modular design
- Easier troubleshooting
- Standardized development
- Technology independence

---

# Goals of the OSI Model

The primary objectives are:

- Standardize network communication
- Promote interoperability
- Simplify troubleshooting
- Support modular protocol design
- Separate networking responsibilities
- Enable future protocol development

---

# The Seven Layers of the OSI Model

The OSI Model consists of seven layers.

```
+----------------------+
| Layer 7 Application  |
+----------------------+
| Layer 6 Presentation |
+----------------------+
| Layer 5 Session      |
+----------------------+
| Layer 4 Transport    |
+----------------------+
| Layer 3 Network      |
+----------------------+
| Layer 2 Data Link    |
+----------------------+
| Layer 1 Physical     |
+----------------------+
```

Each layer provides services to the layer above while relying on services from the layer below.

---

# OSI Layer Order

Communication begins at the Application Layer on the sending device and moves downward to the Physical Layer.

At the receiving device, the process is reversed.

```
Sender

Application

↓

Presentation

↓

Session

↓

Transport

↓

Network

↓

Data Link

↓

Physical

========================

Transmission Medium

========================

Physical

↓

Data Link

↓

Network

↓

Transport

↓

Session

↓

Presentation

↓

Application

Receiver
```

This process ensures that data is prepared for transmission, transported across the network, and reconstructed for the receiving application.

---

# Why Does Layering Matter?

Each layer has a single, well-defined responsibility.

For example:

| Layer | Primary Responsibility |
|--------|------------------------|
| Application | User-facing network services |
| Presentation | Data formatting and encryption |
| Session | Session establishment and management |
| Transport | Reliable end-to-end delivery |
| Network | Logical addressing and routing |
| Data Link | Local delivery and framing |
| Physical | Transmission of electrical, optical, or radio signals |

This separation simplifies maintenance and allows technologies at one layer to evolve without requiring changes at every other layer.

---

# Layer Independence

Each layer communicates with:

- The layer directly above
- The layer directly below
- Its corresponding layer on the remote system

```
Application ───────────── Application

Presentation ─────────── Presentation

Session ──────────────── Session

Transport ────────────── Transport

Network ──────────────── Network

Data Link ────────────── Data Link

Physical ─────────────── Physical
```

Although actual communication traverses the network, each layer behaves as though it is communicating directly with its peer layer.

---

# Protocol Data Units (PDUs)

Each OSI layer processes a different form of data known as a **Protocol Data Unit (PDU).**

| OSI Layer | PDU |
|------------|-----|
| Application | Data |
| Presentation | Data |
| Session | Data |
| Transport | Segment (TCP) / Datagram (UDP) |
| Network | Packet |
| Data Link | Frame |
| Physical | Bits |

Understanding PDUs is essential when analyzing packet captures or troubleshooting network issues.

---

# Memory Mnemonics

## Top to Bottom (Layer 7 → Layer 1)

```
All

People

Seem

To

Need

Data

Processing
```

---

## Bottom to Top (Layer 1 → Layer 7)

```
Please

Do

Not

Throw

Sausage

Pizza

Away
```

These mnemonics are commonly used in networking education to remember the layer order.

---

# Enterprise Communication Example

Consider an employee opening an internal Human Resources portal.

```
Employee Browser

↓

Application Layer

↓

Presentation Layer

↓

Session Layer

↓

Transport Layer

↓

Network Layer

↓

Data Link Layer

↓

Physical Layer

↓

Switch

↓

Router

↓

Firewall

↓

Load Balancer

↓

Web Server

↓

Database
```

Every network request follows this layered communication process before the application generates a response.

---

# Benefits of the OSI Model

The layered architecture provides several advantages:

### Standardization

A common framework for networking technologies.

### Interoperability

Devices from different vendors can communicate using standardized protocols.

### Modularity

Each layer can evolve independently.

### Troubleshooting

Problems can be isolated to a specific layer.

### Scalability

New technologies can be introduced without redesigning the entire networking stack.

### Education

Provides a structured method for learning complex networking concepts.

---

# Limitations of the OSI Model

Although extremely valuable, the OSI Model has some limitations.

- It is a conceptual reference model rather than an implementation.
- Real-world Internet communication primarily follows the TCP/IP model.
- Some protocols span multiple OSI layers.
- Certain layer boundaries may overlap in practical implementations.

Despite these limitations, the OSI Model remains indispensable for learning and troubleshooting.

---

# OSI Model in Cybersecurity

Cybersecurity professionals frequently analyze attacks and defenses using the OSI framework.

Examples include:

| Layer | Security Examples |
|--------|-------------------|
| Application | SQL Injection, XSS, SSRF |
| Presentation | TLS, Encryption |
| Session | Session Hijacking |
| Transport | TCP SYN Flood |
| Network | IP Spoofing, Routing Attacks |
| Data Link | ARP Spoofing, MAC Flooding |
| Physical | Cable Tampering, Device Theft |

Mapping attacks to layers helps defenders select appropriate security controls.

---

# Key Takeaways

- The OSI Model is a seven-layer conceptual framework for network communication.
- Each layer has a clearly defined responsibility.
- Layered architecture improves interoperability, modularity, and troubleshooting.
- Communication moves from Layer 7 to Layer 1 on the sender and from Layer 1 to Layer 7 on the receiver.
- Each layer uses a specific Protocol Data Unit (PDU).
- The OSI Model is widely used in networking education, cybersecurity, packet analysis, and enterprise troubleshooting.


# 02 - OSI Model

# Part 2 — The Seven Layers of the OSI Model (In Depth)

---

# Overview

Every layer of the OSI Model performs a specific function in the communication process.

Instead of one large networking process, communication is divided into smaller, independent tasks.

This layered approach provides:

- Better organization
- Easier troubleshooting
- Vendor interoperability
- Modular protocol design
- Enhanced security implementation

The seven layers work together to move data from one application to another across local and global networks.

---

# Layer 7 — Application Layer

```
+----------------------+
| Layer 7              |
| Application Layer    |
+----------------------+
```

---

## Purpose

The Application Layer is the closest layer to the end user.

It provides network services directly to applications.

> **Important:**  
> The Application Layer **does not refer to the application itself** (such as Chrome or Outlook). Instead, it provides the networking interface that applications use to communicate over a network.

---

## Responsibilities

- Network services for applications
- Resource sharing
- File transfer
- Email services
- Name resolution
- Remote access
- Web communication

---

## Common Protocols

| Protocol | Purpose |
|-----------|----------|
| HTTP | Web communication |
| HTTPS | Secure web communication |
| FTP | File transfer |
| SFTP | Secure file transfer |
| SMTP | Email sending |
| POP3 | Email retrieval |
| IMAP | Email synchronization |
| DNS | Domain name resolution |
| DHCP | Automatic IP configuration |
| SNMP | Network management |
| NTP | Time synchronization |
| SSH | Secure remote login |
| Telnet | Remote login (legacy) |

---

## Data Unit

```
Data
```

---

## Address Used

Application-specific identifiers such as:

- URLs
- Email addresses
- Domain names
- Hostnames

---

## Enterprise Example

A user opens:

```
https://company.com
```

The browser creates an HTTPS request.

The Application Layer prepares the request before passing it to the Presentation Layer.

---

## Cybersecurity Threats

Common attacks include:

- SQL Injection
- Cross-Site Scripting (XSS)
- Cross-Site Request Forgery (CSRF)
- Server-Side Request Forgery (SSRF)
- XML External Entity (XXE)
- Command Injection
- Directory Traversal
- File Inclusion
- API Abuse
- Authentication Bypass

---

## Security Controls

- Web Application Firewall (WAF)
- Input validation
- Secure coding practices
- Multi-Factor Authentication (MFA)
- API gateways
- Rate limiting
- Secure session management

---

## Wireshark Observation

Typical protocols observed:

- HTTP
- HTTPS
- DNS
- SMTP
- FTP

---

# Layer 6 — Presentation Layer

```
+----------------------+
| Layer 6              |
| Presentation Layer   |
+----------------------+
```

---

## Purpose

The Presentation Layer is responsible for ensuring that data is in a format understandable by both communicating systems.

Think of it as the **translator** of the OSI Model.

---

## Responsibilities

- Data formatting
- Character encoding
- Encryption
- Decryption
- Compression
- Decompression
- Serialization

---

## Examples

Different systems may use different:

- Character sets
- Image formats
- File encodings

The Presentation Layer converts them into a common format.

---

## Encryption

This layer commonly handles:

- SSL/TLS encryption
- Certificate-based encryption
- Data confidentiality

---

## Compression

Compression reduces the amount of data transmitted.

Examples:

- ZIP
- JPEG
- PNG
- MPEG

---

## Data Unit

```
Data
```

---

## Enterprise Example

A browser encrypts data using TLS before it is transmitted to a secure web server.

---

## Cybersecurity Threats

- Weak encryption
- Deprecated cipher suites
- Certificate spoofing
- TLS downgrade attacks
- Improper certificate validation

---

## Security Controls

- TLS 1.3
- Strong cipher suites
- PKI
- Certificate validation
- Digital certificates
- HSTS

---

## Wireshark Observation

Encrypted HTTPS traffic appears unreadable without session keys.

---

# Layer 5 — Session Layer

```
+----------------------+
| Layer 5              |
| Session Layer        |
+----------------------+
```

---

## Purpose

The Session Layer establishes, manages, and terminates communication sessions between applications.

---

## Responsibilities

- Session establishment
- Session maintenance
- Authentication support
- Session synchronization
- Session termination
- Checkpointing

---

## Example

During an online banking session:

```
Login

↓

Authenticated Session

↓

Transactions

↓

Logout

↓

Session Ends
```

---

## Common Protocols

Examples include:

- NetBIOS
- RPC
- SMB Session Services

Modern applications often implement session management within higher-layer protocols.

---

## Data Unit

```
Data
```

---

## Cybersecurity Threats

- Session hijacking
- Session fixation
- Cookie theft
- Token replay
- Authentication bypass

---

## Security Controls

- Secure cookies
- HttpOnly
- SameSite
- Session expiration
- Token rotation
- Re-authentication

---

## Wireshark Observation

Session establishment and teardown can often be inferred from application and transport-layer exchanges.

---

# Layer 4 — Transport Layer

```
+----------------------+
| Layer 4              |
| Transport Layer      |
+----------------------+
```

---

## Purpose

The Transport Layer provides **end-to-end communication** between hosts.

It ensures data reaches the correct application reliably or efficiently, depending on the protocol used.

---

## Responsibilities

- Segmentation
- Reassembly
- Flow control
- Error recovery
- Reliability
- Multiplexing
- Port addressing

---

## Protocols

| Protocol | Characteristics |
|-----------|-----------------|
| TCP | Reliable, connection-oriented |
| UDP | Fast, connectionless |

---

## Data Unit

```
Segment (TCP)

Datagram (UDP)
```

---

## Address Used

```
Port Number
```

Examples:

| Port | Service |
|------|----------|
| 20/21 | FTP |
| 22 | SSH |
| 25 | SMTP |
| 53 | DNS |
| 80 | HTTP |
| 110 | POP3 |
| 143 | IMAP |
| 443 | HTTPS |
| 3389 | RDP |

---

## Enterprise Example

A browser sends an HTTPS request using:

```
Destination Port

443
```

The Transport Layer directs the traffic to the correct service running on the destination server.

---

## Cybersecurity Threats

- TCP SYN Flood
- Port scanning
- UDP Flood
- Session reset attacks
- Port abuse

---

## Security Controls

- Stateful firewalls
- TCP SYN cookies
- Rate limiting
- IDS/IPS
- Port filtering

---

## Wireshark Observation

You can observe:

- TCP three-way handshake
- Sequence numbers
- Acknowledgments
- Retransmissions
- UDP datagrams

---

# Layer 3 — Network Layer

```
+----------------------+
| Layer 3              |
| Network Layer        |
+----------------------+
```

---

## Purpose

The Network Layer is responsible for delivering packets between different networks.

It determines the best path from source to destination.

---

## Responsibilities

- Logical addressing
- Routing
- Packet forwarding
- Path determination
- Fragmentation (IPv4)

---

## Protocols

- IPv4
- IPv6
- ICMP
- IPsec
- OSPF
- BGP
- RIP
- EIGRP

---

## Data Unit

```
Packet
```

---

## Address Used

```
IP Address
```

Examples:

```
192.168.1.10

10.0.0.5

172.16.1.50

2001:db8::1
```

---

## Devices

- Routers
- Layer 3 Switches
- Firewalls

---

## Enterprise Example

A router forwards packets from a branch office to a cloud-hosted application over a WAN.

---

## Cybersecurity Threats

- IP spoofing
- Route hijacking
- ICMP abuse
- Routing protocol attacks
- Packet fragmentation attacks

---

## Security Controls

- ACLs
- Routing authentication
- IPsec VPNs
- Anti-spoofing filters
- Network segmentation

---

## Wireshark Observation

Fields commonly examined include:

- Source IP
- Destination IP
- TTL / Hop Limit
- Protocol
- Fragmentation flags

---

# Layer 2 — Data Link Layer

```
+----------------------+
| Layer 2              |
| Data Link Layer      |
+----------------------+
```

---

## Purpose

The Data Link Layer provides reliable communication between devices on the **same local network**.

---

## Responsibilities

- Framing
- MAC addressing
- Error detection
- Media access control
- VLAN tagging
- Switching

---

## Protocols and Standards

- Ethernet (IEEE 802.3)
- Wi-Fi (IEEE 802.11)
- PPP
- ARP
- STP
- VLAN (802.1Q)

---

## Data Unit

```
Frame
```

---

## Address Used

```
MAC Address
```

Example:

```
00:1A:2B:3C:4D:5E
```

---

## Devices

- Switches
- Bridges
- Wireless Access Points

---

## Enterprise Example

A switch forwards an Ethernet frame to the correct workstation using its MAC address table.

---

## Cybersecurity Threats

- ARP spoofing
- MAC flooding
- VLAN hopping
- STP manipulation

---

## Security Controls

- Port security
- Dynamic ARP Inspection (DAI)
- 802.1X authentication
- BPDU Guard
- VLAN segmentation

---

## Wireshark Observation

Typical fields include:

- Source MAC
- Destination MAC
- EtherType
- VLAN ID

---

# Layer 1 — Physical Layer

```
+----------------------+
| Layer 1              |
| Physical Layer       |
+----------------------+
```

---

## Purpose

The Physical Layer is responsible for transmitting raw bits across the communication medium.

It defines the physical characteristics of the network.

---

## Responsibilities

- Bit transmission
- Electrical signaling
- Optical signaling
- Radio signaling
- Connectors
- Cabling
- Pin layouts
- Voltage levels

---

## Examples of Media

- Copper Ethernet
- Fiber optic cable
- Wi-Fi radio waves
- Bluetooth
- Cellular networks

---

## Data Unit

```
Bits
```

---

## Devices

- Hubs
- Repeaters
- Cables
- Connectors
- Patch panels
- Transceivers

---

## Enterprise Example

A fiber optic cable connects two core switches between separate data center buildings.

---

## Cybersecurity Threats

- Cable tampering
- Device theft
- Hardware sabotage
- Electromagnetic interference (EMI)
- Unauthorized physical access

---

## Security Controls

- Locked server rooms
- CCTV
- Physical access control
- Tamper-evident seals
- Secure cable routing
- Environmental monitoring

---

## Wireshark Observation

The Physical Layer itself is **not directly visible** in packet captures because Wireshark analyzes frames after they have been successfully received.

---

# Summary of the Seven Layers

| Layer | PDU | Address | Typical Devices | Example Protocols |
|--------|-----|----------|-----------------|-------------------|
| 7. Application | Data | URL, Domain | Proxy, WAF | HTTP, HTTPS, DNS, SMTP |
| 6. Presentation | Data | — | SSL/TLS Gateway | TLS, SSL |
| 5. Session | Data | Session ID | Session Broker | RPC, NetBIOS |
| 4. Transport | Segment / Datagram | Port | Firewall | TCP, UDP |
| 3. Network | Packet | IP Address | Router | IPv4, IPv6, ICMP |
| 2. Data Link | Frame | MAC Address | Switch | Ethernet, ARP, VLAN |
| 1. Physical | Bits | — | Hub, Cable | Ethernet PHY, Fiber |

