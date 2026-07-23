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

# Part 2 — TCP Data Transfer, Sliding Window, Flow Control, Congestion Control, and Connection Termination

---

# Introduction

After successfully establishing a TCP connection through the **Three-Way Handshake**, both endpoints are ready to exchange application data.

Unlike UDP, TCP continuously monitors the connection throughout its lifetime to ensure:

- Reliable delivery
- Ordered delivery
- Error recovery
- Network congestion avoidance
- Receiver protection
- Graceful session termination

This section explains how TCP manages reliable communication after the connection has been established.

---

# TCP Data Transfer

TCP treats application data as a **continuous stream of bytes** rather than independent messages.

For example:

```
Application Data

"Hello Enterprise TCP World"
```

TCP divides this stream into smaller segments before transmission.

```
Application

↓

Byte Stream

↓

TCP Segments

↓

IP Packets

↓

Ethernet Frames

↓

Network
```

Each segment is independently acknowledged by the receiver.

---

# Byte-Oriented Communication

Unlike UDP, TCP does not preserve application message boundaries.

Example:

Application sends:

```
10000 Bytes
```

TCP may transmit:

```
Segment 1

1460 Bytes

↓

Segment 2

1460 Bytes

↓

Segment 3

1460 Bytes

↓

...

↓

Final Segment
```

The receiving TCP stack reconstructs the original byte stream before delivering it to the application.

---

# Segmentation

Segmentation divides large amounts of application data into manageable TCP segments.

Example:

```
File Size

20 KB

↓

TCP

↓

14 Segments

↓

Transmission
```

Advantages include:

- Efficient retransmissions
- Better error recovery
- Flow control
- Congestion handling

---

# Reassembly

The receiver reconstructs all incoming segments into the original byte stream.

```
Segment 1

↓

Segment 2

↓

Segment 3

↓

Segment 4

↓

Application Data
```

Even if packets arrive out of order, TCP uses sequence numbers to restore the correct order.

---

# Ordered Delivery

Suppose packets arrive as:

```
3

↓

1

↓

4

↓

2
```

TCP buffers the out-of-order segments until the missing data arrives.

The application ultimately receives:

```
1

↓

2

↓

3

↓

4
```

This guarantees consistent application behavior.

---

# Reliable Delivery

Every transmitted segment requires an acknowledgment (ACK).

```
Client

Segment 1

↓

Server

ACK

↓

Client

Segment 2

↓

Server

ACK
```

If an acknowledgment is not received within a specified timeout, TCP retransmits the missing segment.

---

# Retransmission

Example:

```
Client

Segment 3

↓

Lost

↓

No ACK

↓

Timeout

↓

Retransmit Segment 3
```

This mechanism ensures reliable delivery despite packet loss.

---

# Duplicate Detection

If duplicate segments arrive due to retransmissions:

```
Segment 1000

↓

Segment 1000

↓

TCP

↓

Discard Duplicate
```

Sequence numbers allow TCP to identify and ignore duplicate data.

---

# Sliding Window

The Sliding Window mechanism allows multiple segments to be transmitted before waiting for acknowledgments.

Without Sliding Window:

```
Send

↓

Wait

↓

ACK

↓

Send

↓

Wait
```

With Sliding Window:

```
Segment 1

↓

Segment 2

↓

Segment 3

↓

Segment 4

↓

ACK for All
```

This significantly improves throughput.

---

# Sliding Window Example

Window Size:

```
4000 Bytes
```

Sender:

```
Byte 1–4000

↓

Transmit

↓

ACK

↓

Window Slides

↓

4001–8000
```

As acknowledgments arrive, the transmission window advances.

---

# Window Advertisement

The receiver informs the sender how much buffer space is available.

Example:

```
Receiver

Window = 8192 Bytes

↓

Sender

May Send

8192 Bytes
```

If the receiver's buffer fills, it advertises a smaller window.

---

# Zero Window

If the receiver cannot accept additional data:

```
Window = 0
```

The sender temporarily pauses transmission until the receiver advertises a non-zero window.

This prevents receiver buffer overflow.

---

# Flow Control

Flow Control ensures that a fast sender does not overwhelm a slower receiver.

```
Fast Server

↓

Large Data

↓

Slow Client

↓

TCP Flow Control
```

The receiver dynamically adjusts the advertised window size based on available buffer space.

---

# Why Flow Control Matters

Without flow control:

```
Sender

↓

100 MB/s

↓

Receiver

↓

10 MB/s
```

The receiver would quickly exhaust its buffers, causing packet loss.

Flow control prevents this by regulating the transmission rate.

---

# Congestion Control

While Flow Control protects the receiver, **Congestion Control protects the network**.

Network congestion occurs when routers become overloaded.

Symptoms include:

- Packet loss
- High latency
- Retransmissions
- Reduced throughput

TCP uses congestion control algorithms to prevent network collapse.

---

# Congestion Window (cwnd)

TCP maintains a **Congestion Window (cwnd)** that limits the amount of data in transit.

The sender can transmit only up to:

```
Minimum

Receiver Window

AND

Congestion Window
```

This balances receiver capacity and network conditions.

---

# Slow Start

TCP begins cautiously.

```
Initial Window

↓

1 MSS

↓

2 MSS

↓

4 MSS

↓

8 MSS

↓

16 MSS
```

The congestion window doubles every round-trip time (RTT) until a threshold is reached or packet loss occurs.

---

# Slow Start Threshold (ssthresh)

The **Slow Start Threshold (ssthresh)** determines when TCP switches from exponential growth to linear growth.

```
cwnd

↓

Exponential

↓

ssthresh

↓

Linear Growth
```

This helps prevent congestion.

---

# Congestion Avoidance

After reaching `ssthresh`, TCP increases the congestion window more gradually.

```
1

↓

2

↓

3

↓

4

↓

5
```

Instead of doubling each RTT, the window grows approximately one MSS per RTT.

---

# Packet Loss

TCP interprets packet loss as a sign of congestion.

Possible causes:

- Router buffer overflow
- Link congestion
- Wireless interference
- Network failures

When packet loss is detected, TCP reduces its transmission rate.

---

# Fast Retransmit

If the sender receives **three duplicate ACKs**, it assumes a segment has been lost.

```
ACK 1000

↓

ACK 1000

↓

ACK 1000

↓

Retransmit
```

This avoids waiting for the retransmission timeout, improving recovery time.

---

# Fast Recovery

Instead of restarting from one segment, Fast Recovery reduces the congestion window and continues transmitting.

Benefits:

- Faster recovery
- Higher throughput
- Reduced latency

---

# Selective Acknowledgment (SACK)

Without SACK:

```
Segments

1

2

3 Lost

4

5

↓

Retransmit

3

4

5
```

With SACK:

```
Retransmit

Only Segment 3
```

SACK improves efficiency by retransmitting only missing data.

---

# Delayed ACK

To reduce protocol overhead, receivers may delay acknowledgments briefly.

Instead of:

```
ACK

ACK

ACK

ACK
```

TCP may send:

```
Single ACK

For Multiple Segments
```

This reduces network traffic.

---

# Nagle Algorithm

The Nagle Algorithm combines small packets into larger ones.

Without Nagle:

```
1 Byte

↓

1 Packet

↓

1 Byte

↓

1 Packet
```

With Nagle:

```
Several Small Writes

↓

Single Larger Packet
```

Advantages:

- Reduced overhead
- Improved bandwidth efficiency

Disadvantages:

- Increased latency for interactive applications

Applications such as SSH or gaming often disable the Nagle Algorithm.

---

# Keepalive

TCP Keepalive detects inactive or dead connections.

```
Idle Connection

↓

Keepalive Probe

↓

Response?

↓

Yes → Continue

No → Close Connection
```

Keepalive helps remove stale sessions.

---

# TCP Connection States

TCP maintains a finite state machine to track each connection.

Common states include:

- LISTEN
- SYN_SENT
- SYN_RECEIVED
- ESTABLISHED
- FIN_WAIT_1
- FIN_WAIT_2
- CLOSE_WAIT
- LAST_ACK
- TIME_WAIT
- CLOSED

Each state represents a different phase of the connection lifecycle.

---

# TCP State Transition

```
CLOSED

↓

LISTEN

↓

SYN_RECEIVED

↓

ESTABLISHED

↓

FIN_WAIT

↓

TIME_WAIT

↓

CLOSED
```

Understanding these states is essential for troubleshooting network issues.

---

# Four-Way Handshake

TCP closes connections gracefully using a **Four-Way Handshake**.

```
Client                     Server

FIN ----------------------->

      <---------------- ACK

      <---------------- FIN

ACK ----------------------->
```

Each direction of communication is terminated independently.

---

# Step 1 – FIN

The client indicates it has finished sending data.

```
Client

FIN

↓

Server
```

---

# Step 2 – ACK

The server acknowledges the FIN.

```
Server

ACK

↓

Client
```

The client stops sending data but can still receive data.

---

# Step 3 – FIN

When the server finishes transmitting, it sends its own FIN.

```
Server

FIN

↓

Client
```

---

# Step 4 – ACK

The client acknowledges the server's FIN.

```
Client

ACK

↓

Server
```

The connection is now closed.

---

# TIME_WAIT

After sending the final ACK, the client enters the **TIME_WAIT** state.

Purpose:

- Ensure delayed packets expire.
- Prevent old segments from affecting new connections.
- Allow retransmission of the final ACK if necessary.

TIME_WAIT is a normal and important part of TCP.

---

# CLOSE_WAIT

A connection remains in **CLOSE_WAIT** when the local application has not yet closed the socket after receiving a FIN.

Persistent CLOSE_WAIT states may indicate application issues or resource leaks.

---

# Half-Open Connections

A half-open connection occurs when one endpoint believes the session is active while the other does not.

Possible causes:

- Network interruptions
- Firewall timeouts
- Device crashes
- Power failures

TCP Keepalive mechanisms help identify and remove such connections.

---

# Enterprise Load Balancers

Modern load balancers manage millions of concurrent TCP connections.

Typical workflow:

```
Client

↓

TCP Connection

↓

Load Balancer

↓

Web Server 1

↓

Web Server 2

↓

Web Server 3
```

The load balancer distributes connections while preserving TCP session integrity.

---

# High Availability

Enterprise environments deploy redundant TCP-based services.

```
Client

↓

Primary Server

↓

Failure

↓

Automatic Failover

↓

Secondary Server
```

This ensures continuous availability during failures.

---

# TCP in Cloud Environments

Cloud providers optimize TCP for distributed workloads.

Examples include:

- Elastic Load Balancers
- Kubernetes Services
- Service Meshes
- Managed Databases
- API Gateways

Efficient TCP tuning improves scalability and performance in cloud-native architectures.

---

# Business Impact

TCP's data transfer mechanisms enable:

- Reliable financial transactions
- Database synchronization
- Secure file transfers
- Web application availability
- Cloud service reliability
- Enterprise messaging

Without these mechanisms, modern business applications could not guarantee data integrity or consistent user experiences.

---

# Key Takeaways

- TCP divides application data into segments and reassembles it at the receiver.
- Sequence numbers and acknowledgments provide reliable, ordered delivery.
- Sliding Windows improve throughput by allowing multiple outstanding segments.
- Flow Control protects receivers, while Congestion Control protects the network.
- Algorithms such as Slow Start, Congestion Avoidance, Fast Retransmit, and Fast Recovery optimize performance.
- TCP gracefully terminates connections using the Four-Way Handshake and maintains well-defined connection states.

---

# Part 3 — TCP Security, Attack Techniques, Hardening, IDS/IPS, Enterprise Protection, and Best Practices

---

# Introduction

TCP is the backbone of modern enterprise communication. Nearly every critical service—including web applications, email, databases, cloud workloads, VPNs, APIs, and remote administration—depends on TCP.

Because of its widespread adoption, TCP is also one of the most targeted protocols by attackers.

A successful TCP attack can lead to:

- Service disruption
- Unauthorized access
- Session hijacking
- Data theft
- Denial of Service (DoS)
- Distributed Denial of Service (DDoS)
- Network reconnaissance
- Firewall evasion

Understanding TCP attacks and defensive strategies is essential for Network Engineers, Security Engineers, SOC Analysts, Incident Responders, and Penetration Testers.

---

# TCP Security Objectives

A secure TCP implementation should provide:

- Confidentiality (with TLS/IPsec)
- Integrity
- Availability
- Reliable communication
- Authentication
- Session protection
- Attack detection
- Resilience against spoofing

---

# Common TCP Threats

Modern enterprise networks commonly encounter:

- SYN Flood
- ACK Flood
- RST Attack
- Session Hijacking
- TCP Spoofing
- Sequence Prediction
- FIN Scan
- NULL Scan
- Xmas Scan
- TCP Fragmentation
- Port Scanning
- Reflection Attacks
- Distributed Denial of Service

Each technique targets different aspects of the TCP protocol.

---

# SYN Flood Attack

## Overview

A SYN Flood is one of the most common TCP-based Denial-of-Service attacks.

The attacker repeatedly initiates TCP connections but never completes the Three-Way Handshake.

```
Attacker

↓

SYN

↓

Server

↓

SYN-ACK

↓

No ACK

↓

Half-Open Connection
```

The server allocates resources for each incomplete connection.

Eventually:

```
Connection Table

↓

Full

↓

Legitimate Clients Rejected
```

---

# Half-Open Connections

A half-open connection occurs when:

- Server believes connection exists.
- Client never completes handshake.

```
Client

SYN

↓

Server

SYN-ACK

↓

No Response
```

Thousands of these sessions consume memory and CPU resources.

---

# Business Impact

Possible consequences include:

- Website unavailable
- API failures
- Banking interruption
- Cloud outage
- Lost revenue
- Customer dissatisfaction
- SLA violations

---

# Detection

SOC analysts should monitor for:

- Large number of SYN packets
- Very few ACK packets
- Many half-open sessions
- High SYN rate from single IP
- Numerous unique source ports
- Increased retransmissions

---

# Mitigation

Recommended controls:

- SYN Cookies
- Rate limiting
- Stateful firewalls
- TCP Intercept
- Load balancers
- DDoS protection services
- Network ACLs
- Upstream filtering

---

# SYN Cookies

Instead of allocating memory immediately, the server encodes connection state within the SYN-ACK response.

```
Client

↓

SYN

↓

Server

↓

SYN Cookie

↓

ACK?

↓

Allocate Resources
```

This prevents attackers from exhausting connection tables.

---

# TCP Session Hijacking

## Overview

TCP Session Hijacking occurs when an attacker takes control of an existing TCP session.

```
Victim

↓

Authenticated Session

↓

Attacker Injects Packets

↓

Server Accepts Them
```

If successful, the attacker impersonates the legitimate client.

---

# Requirements

Successful hijacking typically requires:

- Packet sniffing
- Correct sequence numbers
- Correct acknowledgment numbers
- Network positioning (or another method of observing traffic)

Modern encryption (TLS) greatly reduces the usefulness of session hijacking by protecting application data.

---

# Business Impact

Potential consequences:

- Unauthorized transactions
- Account takeover
- Data manipulation
- Information disclosure
- Financial fraud

---

# Mitigation

Organizations should:

- Use TLS
- Enable HTTPS everywhere
- Encrypt internal communications
- Segment networks
- Use VPNs
- Monitor unusual TCP behavior

---

# TCP Reset (RST) Attack

An attacker injects forged TCP Reset packets.

```
Attacker

↓

RST Packet

↓

Connection Closed
```

Possible effects:

- VPN disconnects
- SSH termination
- Database interruption
- Service disruption

---

# Detection

Indicators include:

- Unexpected RST packets
- Frequent session resets
- Abnormal connection termination
- User complaints

---

# TCP Spoofing

TCP Spoofing involves forging source IP addresses.

```
Attacker

↓

Fake Source IP

↓

Server

↓

Trusts Packet
```

Spoofing is commonly combined with other attacks.

---

# Mitigation

Best practices include:

- Ingress filtering
- Egress filtering
- Anti-spoofing ACLs
- Reverse Path Forwarding (uRPF)
- Stateful inspection

---

# Sequence Number Prediction

Early TCP implementations generated predictable Initial Sequence Numbers (ISNs).

```
1000

↓

2000

↓

3000
```

Attackers could guess future sequence numbers and inject packets.

Modern operating systems use cryptographically strong random sequence numbers.

---

# ACK Flood Attack

Attackers send massive numbers of ACK packets.

```
Attacker

↓

Millions of ACK Packets

↓

Firewall

↓

CPU Exhaustion
```

Some devices expend significant resources validating unsolicited ACK traffic.

---

# FIN Scan

FIN Scan sends packets with only the FIN flag set.

```
FIN

↓

Target

↓

Closed Port → RST

↓

Open Port → No Response
```

Attackers use this behavior to identify open ports while attempting to evade basic filtering.

---

# NULL Scan

A NULL Scan sends packets with **no TCP flags**.

```
Flags

000000

↓

Target
```

Expected behavior:

- Closed port → RST
- Open port → No response

---

# Xmas Scan

An Xmas Scan sets multiple TCP flags simultaneously.

```
FIN

PSH

URG
```

The packet appears "lit up" like a Christmas tree.

It is used for stealthier reconnaissance on systems that follow RFC behavior.

---

# Why FIN/NULL/Xmas Scans Work

RFC-compliant TCP stacks respond differently to open and closed ports.

```
Closed Port

↓

RST

────────────

Open Port

↓

No Response
```

Attackers leverage these differences for reconnaissance.

---

# Fragmentation Attacks

Attackers split malicious packets into multiple IP fragments.

```
Packet

↓

Fragment 1

↓

Fragment 2

↓

Fragment 3
```

Some security devices may inspect fragments incorrectly, allowing payloads to bypass detection if reassembly is inadequate.

---

# TCP Port Scanning

Port scanning identifies listening services.

Common scan types:

- SYN Scan
- Connect Scan
- ACK Scan
- FIN Scan
- NULL Scan
- Xmas Scan
- Window Scan
- Maimon Scan

Example:

```
Attacker

↓

22

↓

80

↓

443

↓

3389

↓

Open Ports Identified
```

---

# TCP Reflection

Although less common than UDP reflection, TCP can be abused in reflection-style attacks under certain conditions.

Attackers:

```
Spoof Source

↓

Send Requests

↓

Responses

↓

Victim
```

Ingress filtering helps mitigate source address spoofing.

---

# Distributed Denial of Service (DDoS)

Thousands of compromised systems generate TCP traffic simultaneously.

```
Bot 1

↓

Bot 2

↓

Bot 3

↓

Bot 50000

↓

Victim
```

Large-scale TCP floods can overwhelm:

- Firewalls
- Load balancers
- Web servers
- API gateways

---

# Enterprise Firewall Protection

Modern firewalls perform **Stateful Packet Inspection (SPI)**.

Instead of inspecting packets individually, the firewall tracks every TCP session.

```
Firewall

↓

Connection Table

↓

Established Sessions

↓

Allow

↓

Unknown Packets

↓

Drop
```

This prevents many spoofing and session attacks.

---

# Stateful Packet Inspection (SPI)

Example workflow:

```
Client

↓

SYN

↓

Firewall

↓

Track State

↓

Server

↓

SYN-ACK

↓

Firewall Updates State

↓

ACK

↓

Connection Established
```

Packets that do not match an existing state are typically dropped.

---

# Intrusion Detection Systems (IDS)

IDS platforms inspect TCP traffic for malicious behavior.

Common detections include:

- SYN Floods
- Port Scanning
- Session Hijacking Attempts
- TCP Resets
- Abnormal Flags
- Exploit Signatures

Popular IDS solutions:

- Zeek
- Suricata
- Snort

---

# Intrusion Prevention Systems (IPS)

Unlike IDS, IPS can actively block malicious TCP traffic.

Possible actions:

- Drop packets
- Reset connections
- Block IP addresses
- Rate limit connections
- Generate alerts

---

# Linux TCP Hardening

Common Linux hardening measures:

Enable SYN Cookies:

```bash
sysctl -w net.ipv4.tcp_syncookies=1
```

Increase backlog:

```bash
sysctl -w net.core.somaxconn=4096
```

Enable reverse path filtering:

```bash
sysctl -w net.ipv4.conf.all.rp_filter=1
```

Administrators should also review timeout values, backlog limits, and kernel networking parameters.

---

# Windows TCP Hardening

Recommended practices:

- Enable Windows Defender Firewall.
- Keep systems patched.
- Disable unnecessary services.
- Restrict inbound ports.
- Use SMB signing where appropriate.
- Monitor Event Viewer for TCP-related errors.

---

# Cisco TCP Protection

Cisco IOS offers several TCP protection features:

- TCP Intercept
- Control Plane Policing (CoPP)
- Access Control Lists (ACLs)
- Unicast Reverse Path Forwarding (uRPF)
- Rate limiting
- Stateful firewall inspection (platform dependent)

---

# TCP Security in Cloud Environments

Cloud providers offer additional protections:

AWS

- Security Groups
- Network ACLs
- AWS Shield
- AWS WAF

Microsoft Azure

- Network Security Groups
- Azure Firewall
- Azure DDoS Protection

Google Cloud

- VPC Firewall Rules
- Cloud Armor
- Hierarchical Firewall Policies

These services help defend TCP-based workloads from unauthorized access and volumetric attacks.

---

# Enterprise Best Practices

Organizations should:

- Enable SYN Cookies.
- Use Stateful Firewalls.
- Deploy IDS/IPS.
- Patch operating systems regularly.
- Restrict unnecessary TCP ports.
- Segment networks.
- Encrypt traffic using TLS.
- Monitor connection rates.
- Enable anti-spoofing protections.
- Log TCP connection events.
- Implement DDoS protection.
- Continuously review firewall policies.

---

# SOC Detection Engineering

SOC teams should monitor:

- SYN Flood indicators
- Large numbers of half-open connections
- High RST rates
- Repeated connection failures
- Excessive retransmissions
- Port scanning activity
- Long-lived idle sessions
- Unusual TCP flag combinations

Combining TCP telemetry with endpoint, DNS, authentication, and proxy logs improves detection accuracy.

---

# Zeek Monitoring

Zeek provides detailed TCP connection logging through `conn.log`.

Useful fields include:

- Source IP
- Destination IP
- Source Port
- Destination Port
- Protocol
- Connection Duration
- Bytes Sent
- Bytes Received
- Connection State
- Packet Counts

These logs are valuable for threat hunting and incident investigations.

---

# Suricata Monitoring

Suricata can detect:

- SYN Floods
- Port Scans
- TCP Flag Anomalies
- Exploit Attempts
- Malware Command-and-Control
- Protocol Violations

Alerts can be forwarded to SIEM platforms for correlation.

---

# Sigma Detection Ideas

Potential detection logic includes:

- Excessive SYN packets from a single host.
- Multiple failed TCP connections within a short period.
- High volume of RST packets.
- FIN/NULL/Xmas scan behavior.
- Connections to unusual destination ports.
- Internal hosts scanning multiple systems.

These detections should be tuned to reduce false positives.

---

# MITRE ATT&CK Mapping

| Technique | MITRE ATT&CK |
|-----------|--------------|
| Port Scanning | T1046 – Network Service Discovery |
| Session Hijacking | T1557 – Adversary-in-the-Middle |
| TCP Tunneling | T1572 – Protocol Tunneling (where applicable) |
| DDoS / Service Exhaustion | T1498 – Network Denial of Service |
| Network Reconnaissance | T1018 / T1046 |

---

# Business Impact

Weak TCP security can result in:

- Service outages
- Data breaches
- Regulatory violations
- Revenue loss
- Customer distrust
- Increased incident response costs

Securing TCP is therefore a foundational requirement for enterprise resilience.

---

# Key Takeaways

- TCP is frequently targeted because it supports most enterprise applications.
- SYN Floods exploit the connection establishment process to exhaust server resources.
- Session hijacking, spoofing, and sequence prediction attempt to manipulate established communications.
- FIN, NULL, and Xmas scans are reconnaissance techniques that leverage TCP behavior.
- Stateful firewalls, IDS/IPS, anti-spoofing controls, and SYN Cookies significantly improve TCP security.
- Continuous monitoring, hardening, and layered defenses are essential for protecting TCP-based services.

---


