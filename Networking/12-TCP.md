# 12 - Transmission Control Protocol (TCP)

# Part 1 — TCP Fundamentals, Architecture, Header Format, Three-Way Handshake, and Reliable Communication

---

# Overview

The **Transmission Control Protocol (TCP)** is one of the core protocols of the Internet Protocol Suite (TCP/IP). It operates at the **Transport Layer (Layer 4)** of both the TCP/IP and OSI networking models and provides **reliable, connection-oriented communication** between applications running on different hosts.

Unlike protocols that simply transmit data without guarantees, TCP ensures that data is delivered:

- Reliably
- In order
- Without duplication
- With error checking
- With congestion and flow control

TCP is the foundation for many critical Internet services, including:

- Web Browsing (HTTP/HTTPS)
- Secure Shell (SSH)
- Email (SMTP, POP3, IMAP)
- File Transfer (FTP, SFTP)
- Database Connections
- Remote Desktop Protocol (RDP)
- Application APIs
- Cloud Services
- Enterprise Applications

Almost every business-critical application depends on TCP to ensure accurate and consistent communication.

---

# Learning Objectives

After completing this chapter, you will understand:

- Why TCP was developed
- Connection-oriented communication
- TCP architecture
- TCP header structure
- Port numbers
- Sequence numbers
- Acknowledgments
- TCP flags
- Three-Way Handshake
- Reliable communication mechanisms
- Enterprise TCP communication workflow
- TCP packet structure
- Business applications of TCP

---

# Why TCP Exists

Early networking protocols focused on sending data from one device to another. However, networks are inherently unreliable.

Problems include:

- Packet loss
- Packet duplication
- Packet corruption
- Out-of-order delivery
- Congestion
- Network failures
- High latency

Applications such as banking, healthcare systems, enterprise databases, and cloud services cannot tolerate unreliable communication.

TCP was designed to solve these problems by providing a mechanism that guarantees reliable delivery of application data.

---

# What is TCP?

**Transmission Control Protocol (TCP)** is a **connection-oriented transport layer protocol** that establishes a communication session before transmitting data.

TCP provides:

- Reliable delivery
- Ordered delivery
- Error detection
- Flow control
- Congestion control
- Connection management

Unlike UDP, TCP tracks every byte transmitted and ensures successful delivery before considering the transmission complete.

---

# Transport Layer Overview

TCP operates at **Layer 4 (Transport Layer)**.

```
+---------------------------+
| Application Layer         |
+---------------------------+
| Transport Layer (TCP)     |
+---------------------------+
| Internet Layer (IP)       |
+---------------------------+
| Data Link Layer           |
+---------------------------+
| Physical Layer            |
+---------------------------+
```

The Transport Layer is responsible for communication between applications rather than just hosts.

---

# Responsibilities of TCP

TCP performs several critical functions:

- Segmentation
- Reliable delivery
- Sequencing
- Error recovery
- Flow control
- Congestion control
- Multiplexing
- Connection establishment
- Connection termination
- Data integrity verification

---

# Characteristics of TCP

| Feature | Description |
|----------|-------------|
| Connection-Oriented | Requires session establishment |
| Reliable | Lost packets are retransmitted |
| Ordered Delivery | Data arrives in sequence |
| Error Detection | Uses checksum validation |
| Flow Control | Prevents receiver overload |
| Congestion Control | Prevents network congestion |
| Full Duplex | Simultaneous two-way communication |
| Byte Stream | Data treated as continuous stream |

---

# TCP vs UDP

| Feature | TCP | UDP |
|----------|-----|-----|
| Connection | Yes | No |
| Reliability | High | None |
| Ordering | Guaranteed | Not Guaranteed |
| Retransmission | Yes | No |
| Flow Control | Yes | No |
| Congestion Control | Yes | No |
| Speed | Slower | Faster |
| Header Size | 20–60 Bytes | 8 Bytes |
| Use Cases | Web, Email, SSH | Streaming, VoIP, DNS |

---

# Connection-Oriented Communication

TCP requires establishing a session before exchanging data.

```
Client

↓

Connection Request

↓

Server

↓

Connection Established

↓

Data Transfer

↓

Connection Closed
```

This ensures both devices are synchronized before transmitting application data.

---

# Reliable Communication

TCP reliability is achieved through:

- Sequence Numbers
- Acknowledgments (ACKs)
- Retransmissions
- Checksums
- Sliding Windows
- Timers

If any segment is lost, TCP retransmits it automatically.

---

# TCP Segment

Unlike UDP datagrams, TCP transmits **segments**.

```
+------------------------+
| TCP Header             |
+------------------------+
| Application Data       |
+------------------------+
```

Each segment contains control information required to maintain reliable communication.

---

# TCP Header Format

```
0                   15 16                  31

+-------------------+----------------------+
| Source Port       | Destination Port     |
+-------------------+----------------------+
| Sequence Number                          |
+------------------------------------------+
| Acknowledgment Number                    |
+------------------------------------------+
| Data Offset | Reserved | Flags           |
+------------------------------------------+
| Window Size                            |
+------------------------------------------+
| Checksum                               |
+------------------------------------------+
| Urgent Pointer                         |
+------------------------------------------+
| Options (Optional)                     |
+------------------------------------------+
| Data                                   |
+------------------------------------------+
```

Minimum Header Size:

```
20 Bytes
```

Maximum Header Size:

```
60 Bytes
```

---

# Source Port

The Source Port identifies the sending application.

Example:

```
Chrome Browser

↓

Source Port

49518
```

The operating system dynamically assigns this port.

---

# Destination Port

The Destination Port identifies the receiving service.

Examples:

| Service | Port |
|----------|------|
| HTTP | 80 |
| HTTPS | 443 |
| SSH | 22 |
| FTP | 21 |
| SMTP | 25 |
| POP3 | 110 |
| IMAP | 143 |
| MySQL | 3306 |

---

# Port Number Categories

| Range | Description |
|--------|-------------|
| 0–1023 | Well-Known Ports |
| 1024–49151 | Registered Ports |
| 49152–65535 | Dynamic/Ephemeral Ports |

---

# Sequence Number

Every byte transmitted over TCP is assigned a sequence number.

Example:

```
Client

Seq = 1000

↓

Server
```

If 500 bytes are transmitted:

```
Next Sequence Number

1500
```

Sequence numbers allow the receiver to reconstruct the original byte stream in the correct order.

---

# Acknowledgment Number

The acknowledgment number indicates the next expected byte.

Example:

```
Client

Seq = 1000

Length = 500

↓

Server

ACK = 1500
```

This tells the sender that bytes up to 1499 have been received successfully.

---

# Data Offset

The Data Offset field specifies the size of the TCP header.

Typical values:

- 20 Bytes (no options)
- Larger values when options are present

This allows the receiver to determine where the application data begins.

---

# Reserved Bits

Reserved bits are set aside for future protocol enhancements and are normally set to zero.

---

# TCP Flags

TCP uses control flags to manage the state of a connection.

| Flag | Name | Purpose |
|------|------|---------|
| SYN | Synchronize | Start connection |
| ACK | Acknowledgment | Confirm received data |
| FIN | Finish | Gracefully close connection |
| RST | Reset | Immediately terminate connection |
| PSH | Push | Deliver data immediately |
| URG | Urgent | Urgent data present |
| ECE | ECN Echo | Congestion notification |
| CWR | Congestion Window Reduced | Congestion response |
| NS | Nonce Sum | ECN protection (rare) |

---

# SYN Flag

The SYN flag initiates a TCP connection.

```
Client

SYN

↓

Server
```

It synchronizes sequence numbers between both endpoints.

---

# ACK Flag

The ACK flag acknowledges successful receipt of data.

```
Server

ACK

↓

Client
```

Almost every TCP segment after the initial SYN includes the ACK flag.

---

# FIN Flag

FIN is used for graceful connection termination.

```
Client

FIN

↓

Server
```

Both endpoints exchange FIN and ACK segments to close the connection cleanly.

---

# RST Flag

RST immediately aborts a connection.

Common reasons:

- Invalid port
- Unexpected packet
- Application crash
- Firewall rejection

Unlike FIN, RST does not complete pending data transfers.

---

# PSH Flag

The PSH (Push) flag instructs the receiver to deliver data to the application immediately instead of buffering it.

Used by interactive applications such as:

- SSH
- Telnet
- Remote administration tools

---

# URG Flag

URG indicates that the Urgent Pointer field contains high-priority data.

This feature is rarely used in modern applications.

---

# Window Size

The Window Size field controls how much data can be sent before an acknowledgment is required.

Example:

```
Window = 8192 Bytes

↓

Sender may transmit

8192 Bytes

↓

Wait for ACK
```

This mechanism supports efficient flow control.

---

# Checksum

The Checksum verifies the integrity of the TCP header and payload.

```
Sender

↓

Calculate Checksum

↓

Transmit

↓

Receiver

↓

Verify Checksum
```

If the checksum validation fails, the segment is discarded and retransmitted.

---

# Urgent Pointer

The Urgent Pointer identifies the end of urgent data when the URG flag is set.

Although part of the TCP specification, it is seldom used in modern networking.

---

# TCP Options

TCP Options extend the protocol with additional capabilities.

Common options include:

- Maximum Segment Size (MSS)
- Window Scaling
- Selective Acknowledgment (SACK)
- Timestamp
- No-Operation (NOP)

These options improve efficiency and performance.

---

# Maximum Segment Size (MSS)

MSS specifies the maximum amount of application data that can be carried in a TCP segment.

Example:

```
Ethernet MTU

1500 Bytes

↓

IP Header

20 Bytes

↓

TCP Header

20 Bytes

↓

MSS

1460 Bytes
```

Negotiating MSS during connection establishment helps avoid fragmentation.

---

# Enterprise Example

A user opens:

```
https://company.example
```

The communication sequence:

```
Browser

↓

TCP Port 443

↓

Firewall

↓

Load Balancer

↓

Web Server

↓

Application Server

↓

Database Server
```

Every step depends on TCP to deliver requests and responses reliably.

---

# Three-Way Handshake

Before any application data is exchanged, TCP establishes a connection using the **Three-Way Handshake**.

```
Client                     Server

  SYN  --------------------->

       <------------------ SYN + ACK

  ACK --------------------->
```

After these three steps, both endpoints agree on:

- Initial Sequence Numbers (ISNs)
- Connection parameters
- Window sizes
- TCP options

The connection is then ready for data transfer.

---

# Step 1 – SYN

The client initiates communication.

```
Client

Seq = X

SYN

↓

Server
```

The SYN segment advertises the client's initial sequence number and TCP options.

---

# Step 2 – SYN + ACK

The server acknowledges the client's SYN and sends its own SYN.

```
Server

Seq = Y

ACK = X + 1

↓

Client
```

This synchronizes sequence numbers in both directions.

---

# Step 3 – ACK

The client acknowledges the server's SYN.

```
Client

ACK = Y + 1

↓

Server
```

At this point, the TCP connection is fully established.

---

# Why Three-Way Handshake Is Important

The handshake ensures:

- Both hosts are reachable.
- Initial sequence numbers are synchronized.
- TCP options are negotiated.
- Resources are allocated.
- Communication can begin reliably.

Without this process, reliable byte-stream communication would not be possible.

---

# Enterprise Communication Workflow

```
Employee Browser

↓

DNS Resolution

↓

TCP Three-Way Handshake

↓

TLS Handshake (HTTPS)

↓

HTTP Request

↓

Application Processing

↓

Database Query

↓

HTTP Response

↓

TCP Connection Maintained
```

TCP serves as the transport foundation for higher-layer protocols such as TLS and HTTP.

---

# Business Impact

Reliable TCP communication is essential for:

- Online banking
- E-commerce
- ERP systems
- Healthcare platforms
- Financial trading
- Cloud applications
- Video conferencing control channels
- Enterprise databases

Failures in TCP connectivity can lead to service outages, transaction failures, and degraded user experience.

---

# Key Takeaways

- TCP is a connection-oriented Transport Layer protocol.
- It provides reliable, ordered, and error-checked delivery of data.
- TCP segments contain a rich header with sequencing and control information.
- Sequence and acknowledgment numbers enable reliable byte-stream communication.
- The Three-Way Handshake establishes synchronized communication before data transfer.
- TCP underpins the majority of enterprise and Internet applications.

---

