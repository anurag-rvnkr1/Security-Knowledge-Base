# Network and Network Traffic Forensics

> **A practical enterprise guide to investigating network evidence through packet captures, flow telemetry, DNS, HTTP, TLS, DHCP, ARP, firewall and proxy logs, VPN activity, lateral movement, command-and-control behavior, and data-exfiltration patterns.**

---

# Overview

Network forensics is the investigation of network communications to reconstruct:

- Who communicated
- With whom
- When communication occurred
- Which protocols were used
- Which systems were involved
- What applications were involved
- Whether the communication was expected
- Whether suspicious activity occurred

A network investigation combines:

```text
PCAP
+
Network Flows
+
DNS
+
DHCP
+
Firewall
+
Proxy
+
VPN
+
Endpoint Telemetry
+
Identity
```

The objective is not simply to inspect packets.

> **The objective is to reconstruct communication and determine its security significance.**

---

# Why Network Forensics Matters

Network evidence can reveal activity that endpoint evidence alone may miss.

Examples include:

```text
Command and Control
Malware Communication
Credential Attacks
Lateral Movement
Data Exfiltration
Port Scanning
DNS Abuse
Unauthorized Remote Access
Cloud Communication
Suspicious External Connections
```

---

# Network Forensic Architecture

```text
                         Enterprise Network
                                │
       ┌────────────────────────┼────────────────────────┐
       ▼                        ▼                        ▼
   Endpoints                  Servers                  Cloud
       │                        │                        │
       └────────────────────────┼────────────────────────┘
                                ▼
                       Network Infrastructure
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
       Firewall              Proxy                 DNS
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                         Network Telemetry
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                   PCAP       Flow        Logs
                    │           │           │
                    └───────────┼───────────┘
                                ▼
                           Investigation
```

---

# Network Investigation Questions

A strong investigation should answer:

```text
Who communicated?
When?
From which IP?
To which destination?
Which port?
Which protocol?
Which process?
Which user?
How much data?
Was DNS involved?
Was encryption used?
Was the activity expected?
```

---

# Network Evidence Sources

| Evidence Source | Primary Value |
|---|---|
| PCAP | Packet-level investigation |
| NetFlow/IPFIX | Communication metadata |
| DNS logs | Name resolution |
| DHCP | IP-to-host mapping |
| Firewall | Allowed/blocked traffic |
| Proxy | Web communication |
| VPN | Remote access |
| IDS/IPS | Security detections |
| Zeek | Protocol metadata |
| EDR | Process-to-network correlation |
| Cloud flow logs | Cloud network visibility |

---

# Packet Capture

A packet capture, commonly called **PCAP**, contains captured network packets.

Conceptually:

```text
Network Traffic
      │
      ▼
Packet Capture
      │
      ▼
Ethernet
      │
      ▼
IP
      │
      ▼
TCP / UDP
      │
      ▼
Application Protocol
```

---

# Packet-Level vs Flow-Level Evidence

## PCAP

Provides detailed packet information.

Useful for:

- Protocol analysis
- Payload analysis
- Session reconstruction
- DNS investigation
- HTTP analysis

## Flow Data

Usually provides:

```text
Source IP
Destination IP
Source Port
Destination Port
Protocol
Bytes
Packets
Start Time
End Time
```

Flow data is smaller and more scalable.

---

# PCAP Limitations

PCAP may be:

- Huge
- Incomplete
- Encrypted
- Missing packets
- Limited to selected network segments
- Difficult to retain long-term

Therefore:

> More packets do not automatically mean better evidence.

---

# Network Investigation Workflow

```text
Alert
 │
 ▼
Identify Hosts
 │
 ▼
Identify Time Window
 │
 ▼
Review Network Flows
 │
 ▼
Review DNS
 │
 ▼
Inspect PCAP
 │
 ▼
Identify Protocol
 │
 ▼
Correlate Endpoint
 │
 ▼
Assess Behavior
 │
 ▼
Scope
 │
 ▼
Report
```

---

# IP Addressing

Investigators should understand:

```text
IPv4
IPv6
Private Addresses
Public Addresses
NAT
Subnets
Routing
```

Private IPv4 ranges commonly include:

```text
10.0.0.0/8
172.16.0.0/12
192.168.0.0/16
```

---

# NAT Considerations

Network Address Translation can make multiple internal systems appear behind one public IP.

Therefore:

```text
Public IP
    │
    ▼
NAT Gateway
    │
 ┌──┼──┐
 ▼  ▼  ▼
Host Host Host
```

Investigators may require:

- NAT logs
- Firewall logs
- DHCP
- Endpoint telemetry

to identify the actual internal system.

---

# TCP/IP Model

A simplified investigation model:

```text
Application
    │
Transport
    │
Internet
    │
Link
```

Common protocols include:

```text
HTTP
DNS
SSH
TLS
TCP
UDP
ICMP
ARP
DHCP
```

---

# TCP

TCP provides:

- Connection establishment
- Reliability
- Sequencing
- Flow control

Important forensic concepts include:

```text
Source
Destination
Ports
Flags
Sequence
Timing
Connection State
```

---

# TCP Three-Way Handshake

```text
Client                  Server
  │                       │
  │──── SYN ────────────►│
  │◄─── SYN/ACK ─────────│
  │──── ACK ────────────►│
  │                       │
  │     Connection        │
```

A handshake can help establish whether a connection was actually established.

---

# TCP Flags

Common flags:

```text
SYN
ACK
FIN
RST
PSH
URG
```

Unusual patterns may be relevant to:

- Scanning
- Connection failures
- Resets
- Network instability

But flags should always be interpreted in context.

---

# UDP

UDP is connectionless.

Common UDP applications include:

```text
DNS
DHCP
NTP
Streaming
Some VPN protocols
```

Because UDP lacks TCP-style connection establishment, investigation relies more heavily on:

- Timing
- Endpoints
- Ports
- Application metadata
- Flow records

---

# DNS Forensics

DNS is one of the most valuable network evidence sources.

Investigate:

```text
Client
Query
Record Type
Response
Resolved IP
Timestamp
```

---

# DNS Investigation Model

```text
Endpoint
   │
   ▼
DNS Query
   │
   ▼
Domain
   │
   ▼
IP Address
   │
   ▼
Network Connection
   │
   ▼
Process
```

---

# DNS Record Types

Important records include:

```text
A
AAAA
CNAME
MX
TXT
NS
PTR
```

Each can provide different investigative context.

---

# Suspicious DNS Indicators

Potential indicators include:

- Newly observed domain
- Rare domain
- High query frequency
- Random-looking subdomains
- Unusual record types
- Unexpected resolver
- DNS communication from unusual hosts

None is automatically malicious.

---

# DNS Tunneling

DNS can be abused to transport information through DNS queries and responses.

Conceptually:

```text
Host
 │
 ▼
Encoded Subdomain
 │
 ▼
DNS Resolver
 │
 ▼
Authoritative Server
```

Potential indicators include:

```text
High Query Volume
Long Labels
High Entropy
Repeated Queries
Unusual Domains
```

Behavior should be validated against legitimate applications.

---

# DNS Timeline

Example:

```text
10:01 — Host queries suspicious domain
10:02 — Domain resolves
10:02 — HTTPS connection established
10:03 — Process starts
```

This becomes stronger when endpoint evidence supports it.

---

# HTTP Forensics

HTTP can expose valuable metadata.

Common fields include:

```text
Method
URI
Host
User-Agent
Status Code
Content-Type
Headers
Source
Destination
```

---

# HTTP Investigation

Questions:

```text
Which host was contacted?
Which URI?
Which method?
What was the response?
What user agent?
Which process generated it?
```

---

# HTTP Methods

Common methods:

```text
GET
POST
PUT
DELETE
PATCH
HEAD
OPTIONS
```

Method alone is not a malicious indicator.

---

# HTTP Status Codes

Examples:

```text
200 — Success
301/302 — Redirect
400 — Client Error
401 — Unauthorized
403 — Forbidden
404 — Not Found
500 — Server Error
```

Investigate sequences rather than isolated codes.

---

# HTTP User-Agent

The User-Agent may help identify:

- Browser
- Operating system
- Application
- Script
- Automation

It can also be spoofed.

Therefore:

> User-Agent is contextual evidence, not identity proof.

---

# HTTPS

HTTPS encrypts application content using TLS.

Network investigators may still observe:

```text
Source IP
Destination IP
Port
TLS Version
Certificates
Handshake Metadata
Timing
Traffic Volume
SNI where available
```

---

# TLS Investigation

Encryption does not eliminate network evidence.

A simplified model:

```text
Client
 │
 ▼
TLS Handshake
 │
 ├── Certificate
 ├── Version
 └── Metadata
 │
 ▼
Encrypted Application Data
```

---

# TLS Limitations

Depending on protocol version and deployment, investigators may not see:

- HTTP URI
- HTTP body
- Application payload

Network metadata may still be valuable.

---

# Certificate Analysis

Investigate:

```text
Issuer
Subject
Validity
Fingerprint
Algorithm
SAN
```

A certificate anomaly does not automatically indicate malicious activity.

---

# SNI

Server Name Indication may expose the intended hostname during TLS establishment in environments where it is visible.

Modern encrypted transport technologies can reduce traditional visibility.

---

# QUIC and HTTP/3

Modern applications may use:

```text
QUIC
HTTP/3
UDP
```

This changes traditional HTTP/TCP investigation techniques.

Investigators should understand:

- UDP transport
- TLS integration
- Flow behavior
- Application telemetry

---

# DHCP Forensics

DHCP can map:

```text
MAC Address
IP Address
Hostname
Lease Time
```

This can help identify which endpoint used an IP at a particular time.

---

# DHCP Investigation

Example:

```text
10:00
MAC A → 10.0.0.25

10:30
MAC B → 10.0.0.25
```

A network investigation that only uses IP addresses may therefore misattribute activity.

---

# ARP

ARP maps:

```text
IP Address
     ↕
MAC Address
```

ARP evidence can help understand local network relationships.

---

# ARP Investigation

Potentially relevant activity includes:

- Unexpected ARP changes
- Duplicate addresses
- ARP poisoning indicators
- Unexpected gateways

Again, investigate within network context.

---

# Firewall Forensics

Firewall logs may show:

```text
Source
Destination
Port
Protocol
Action
Rule
Timestamp
Bytes
```

Firewall evidence can answer:

> Was the communication allowed or blocked?

---

# Proxy Forensics

Web proxies can provide:

```text
User
Host
URL
Method
Response
Bytes
Policy
Timestamp
```

Proxy logs are especially useful when endpoint telemetry is incomplete.

---

# VPN Forensics

VPN logs may provide:

```text
User
Source IP
Assigned IP
Login Time
Logout Time
Authentication
Device
```

This helps correlate remote users with internal network activity.

---

# Network Scanning

Scanning may produce patterns such as:

```text
One Source
   │
   ├── Port A
   ├── Port B
   ├── Port C
   ├── Port D
   └── Port E
```

Indicators may include:

- Many destinations
- Many ports
- Short-lived connections
- Repeated connection attempts

But legitimate vulnerability scanners produce similar patterns.

---

# Lateral Movement

Network evidence can help identify movement between internal systems.

Example:

```text
Host A
  │
  ▼
Host B
  │
  ▼
Host C
```

Investigate:

```text
Source
Destination
Protocol
User
Authentication
Process
Time
```

---

# Common Lateral Movement Protocols

Depending on environment:

```text
SMB
RDP
SSH
WinRM
Remote Management
Database Protocols
```

The presence of these protocols is not inherently malicious.

---

# Beaconing

Command-and-control traffic may exhibit recurring communication.

Conceptually:

```text
10:00 ─────►
10:05 ─────►
10:10 ─────►
10:15 ─────►
```

Potential indicators:

- Regular intervals
- Repeated destination
- Similar packet sizes
- Long-lived relationship

Legitimate applications can also beacon.

---

# Beaconing Analysis

Compare:

```text
Timing
+
Destination
+
Process
+
Bytes
+
DNS
+
TLS
```

A process generating regular encrypted connections to an unusual destination may warrant investigation.

---

# Command and Control

Network C2 investigation can use:

```text
DNS
IP
Domain
TLS
HTTP
Proxy
Flow
Endpoint
```

A conceptual chain:

```text
Process
   │
   ▼
DNS Query
   │
   ▼
Domain
   │
   ▼
IP
   │
   ▼
TLS
   │
   ▼
Repeated Connection
```

---

# Data Exfiltration

Potential indicators include:

```text
Large Outbound Transfer
Unexpected Destination
Unusual Protocol
Compression
Encryption
After-Hours Activity
Cloud Storage
```

Volume alone is insufficient.

---

# Exfiltration Investigation

Ask:

```text
What data?
How much?
From which host?
Which process?
Which destination?
Which account?
Which protocol?
Was transfer authorized?
```

---

# Data Volume Analysis

Example:

```text
Normal:
10 MB/day outbound

Observed:
4 GB outbound
```

This is an anomaly, but investigators must determine whether it corresponds to:

- Backup
- Software distribution
- Cloud synchronization
- Business operation
- Data exfiltration

---

# NetworkMiner

NetworkMiner can assist with network traffic analysis and extraction of information from captured traffic.

Potentially useful evidence includes:

```text
Hosts
Files
Credentials
Sessions
DNS
Network Metadata
```

Use only authorized captures.

---

# Wireshark

Wireshark is a widely used packet-analysis tool.

Official site:

https://www.wireshark.org/

It provides:

- Packet inspection
- Protocol decoding
- Stream reconstruction
- Filtering
- Statistics
- Export capabilities

---

# Wireshark Investigation Workflow

```text
PCAP
 │
 ▼
Capture Statistics
 │
 ▼
Endpoints
 │
 ▼
Conversations
 │
 ▼
Protocols
 │
 ▼
DNS
 │
 ▼
HTTP/TLS
 │
 ▼
Suspicious Sessions
 │
 ▼
Stream Analysis
```

---

# Wireshark Filters

Common examples:

```text
dns
```

```text
http
```

```text
tcp
```

```text
udp
```

```text
ip.addr == 10.0.0.25
```

```text
tcp.port == 443
```

Use filters to reduce noise rather than blindly reviewing every packet.

---

# TCP Stream Analysis

A TCP stream can reconstruct application communication when the traffic is available and not protected by encryption.

Conceptually:

```text
Packets
  │
  ▼
TCP Stream
  │
  ▼
Application Data
```

---

# Zeek

Zeek is a network security monitoring platform that generates rich protocol-level metadata.

It can produce logs related to:

```text
Connections
DNS
HTTP
SSL/TLS
SSH
Files
Certificates
```

Official site:

https://zeek.org/

---

# Zeek Investigation Model

```text
Network Traffic
      │
      ▼
     Zeek
      │
 ┌────┼──────────────┐
 ▼    ▼              ▼
conn dns            http
 │    │               │
 ▼    ▼               ▼
Flow Domain         Web
```

---

# Network Forensic Correlation

A strong investigation connects:

```text
PCAP
  +
DNS
  +
Firewall
  +
Proxy
  +
EDR
  +
Identity
```

Example:

```text
Endpoint
   │
   ▼
Process
   │
   ▼
DNS Query
   │
   ▼
External IP
   │
   ▼
Firewall Connection
   │
   ▼
TLS Session
```

---

# Network Timeline

Example:

```text
09:01:02 — User authentication
09:01:15 — Process starts
09:01:20 — DNS query
09:01:21 — TCP connection
09:01:22 — TLS handshake
09:03:10 — Large outbound transfer
```

Correlation helps reconstruct the sequence.

---

# Network Evidence Gaps

Document limitations such as:

```text
No PCAP
Limited Retention
Encrypted Traffic
Missing DNS Logs
NAT Ambiguity
Clock Drift
Packet Loss
Unmonitored Network Segment
```

Evidence gaps are part of the investigation result.

---

# Common Network Forensic Mistakes

## Treating IP Reputation as Proof

An IP reputation score is an indicator, not a complete conclusion.

## Assuming Encryption Means No Evidence

TLS still leaves metadata.

## Ignoring NAT

Public IPs may represent many internal hosts.

## Ignoring DHCP

IP-to-host attribution can become inaccurate.

## Ignoring Time

Network correlation depends heavily on accurate timestamps.

## Inspecting Only PCAP

Logs and endpoint data provide important context.

## Assuming Large Transfers Are Exfiltration

Backups and cloud synchronization can generate large transfers.

---

# Network Forensic Decision Tree

```text
                    Alert
                      │
                      ▼
                Identify Host
                      │
                      ▼
                Identify Time
                      │
                      ▼
               Flow Available?
                 │         │
                Yes        No
                 │          │
                 ▼          ▼
              PCAP        DNS/Logs
                 │          │
                 └────┬─────┘
                      ▼
                 Identify Peer
                      │
                      ▼
                 Identify Process
                      │
                      ▼
                  Analyze
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
         DNS         TLS         HTTP
          │           │           │
          └───────────┼───────────┘
                      ▼
                  Correlate
                      │
                      ▼
                   Scope
```

---

# Practical Lab 01 — PCAP Triage

## Objective

Given an authorized PCAP:

Identify:

```text
Top Talkers
Protocols
Endpoints
Conversations
DNS Queries
Suspicious Connections
```

Start with:

```text
Capture Statistics
```

Then move toward specific traffic.

---

# Practical Lab 02 — DNS Investigation

Find:

```text
Domains
Clients
Query Frequency
Resolved Addresses
Rare Domains
Suspicious Patterns
```

Construct:

```text
Host
 ↓
DNS Query
 ↓
Domain
 ↓
IP
 ↓
Connection
```

---

# Practical Lab 03 — HTTP Investigation

Identify:

```text
Hosts
Methods
URIs
User Agents
Status Codes
Files
```

Determine whether suspicious activity occurred.

---

# Practical Lab 04 — TLS Investigation

Analyze available:

```text
TLS Version
Certificate
Server Name
Destination
Timing
Traffic Volume
```

Determine what can and cannot be concluded from encrypted traffic.

---

# Practical Lab 05 — Beaconing Investigation

Scenario:

> An endpoint repeatedly communicates with the same external destination.

Analyze:

```text
Interval
Destination
Bytes
Packets
Process
DNS
TLS
```

Determine whether the behavior is:

```text
Expected
Suspicious
Likely Automated
Unknown
```

---

# Practical Lab 06 — Lateral Movement Investigation

Scenario:

```text
Host A
  │
  ├── SMB → Host B
  │
  ├── RDP → Host C
  │
  └── SSH → Host D
```

Determine:

- Source
- Destination
- User
- Protocol
- Time
- Authentication
- Process

---

# Practical Lab 07 — Exfiltration Investigation

Scenario:

> A server generated an unusually large outbound transfer.

Investigate:

```text
Destination
Bytes
Protocol
Process
User
Data Source
Time
Business Context
```

Determine whether the activity is:

```text
Backup
Synchronization
Expected Transfer
Suspicious
Potential Exfiltration
```

---

# Practical Lab 08 — Complete Network Forensic Investigation

Scenario:

```text
Security Alert
      │
      ▼
Endpoint
      │
      ▼
DNS Query
      │
      ▼
External Domain
      │
      ▼
TLS Connection
      │
      ▼
Repeated Communication
      │
      ▼
Large Transfer
```

Your investigation should establish:

1. Which host initiated communication?
2. Which process generated it?
3. Which destination was contacted?
4. How was the destination resolved?
5. Was communication encrypted?
6. Was the behavior periodic?
7. Was data transferred?
8. Was the destination expected?
9. What additional systems were involved?
10. What evidence gaps remain?

---

# Network Forensic Report Template

```text
# Network Forensic Investigation

## Case Information

Case ID:
Host:
IP:
Time Window:
Analyst:

## Evidence

PCAP:
Flow Logs:
DNS:
Firewall:
Proxy:
VPN:
EDR:

## Investigation Scope

## Network Architecture

## Endpoint Identification

## DNS Analysis

## Connection Analysis

## Protocol Analysis

## TLS Analysis

## HTTP Analysis

## Lateral Movement

## C2 Assessment

## Exfiltration Assessment

## Timeline

## Evidence Correlation

## Findings

## Evidence Gaps

## Confidence

## Recommendations

## Conclusion
```

---

# Example Finding

```text
Finding ID:
NET-001

Title:
Repeated Outbound Communication to an Unusual Destination

Observation:
An endpoint repeatedly initiated encrypted connections to an external destination at relatively regular intervals.

Supporting Evidence:
Network flow data
DNS telemetry
Endpoint process telemetry
TLS metadata

Assessment:
The communication pattern is suspicious and may represent automated application or command-and-control activity.

Confidence:
Medium

Limitation:
Application payload was encrypted and no endpoint process capture was available for part of the observation period.
```

---

# Network Forensics and Incident Response

Network forensics supports:

```text
Detection
   ↓
Triage
   ↓
Network Scoping
   ↓
Host Identification
   ↓
Containment
   ↓
Evidence Collection
   ↓
Root Cause
   ↓
Recovery
```

Network telemetry can identify additional compromised hosts even when endpoint evidence is incomplete.

---

# Network Forensics and Threat Hunting

A forensic discovery can become a hunt:

```text
Forensic Finding
      │
      ▼
Suspicious Domain
      │
      ▼
Search DNS
      │
      ▼
Identify All Clients
      │
      ▼
Search Network Flows
      │
      ▼
Correlate Processes
      │
      ▼
Scope
```

---

# Network Forensics and Detection Engineering

Example:

```text
Forensic Finding:
Periodic encrypted outbound connections

        ↓

Detection Hypothesis:
Identify rare external destinations with periodic communication

        ↓

Telemetry:
DNS + Flow + EDR

        ↓

Detection:
Alert on anomalous recurring communication
```

---

# Enterprise Network Forensics Architecture

```text
                         Enterprise Network
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
          Endpoints           Servers            Cloud
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                         Network Sensors
                                │
       ┌────────────────────────┼────────────────────────┐
       ▼                        ▼                        ▼
     PCAP                     Zeek                  Flow Logs
       │                        │                        │
       └────────────────────────┼────────────────────────┘
                                ▼
                       DNS / Firewall / Proxy
                                │
                                ▼
                              SIEM
                                │
                                ▼
                           Investigation
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
              SOC              IR             Threat Hunt
```

---

# Network Forensic Readiness

Organizations should maintain:

```text
Network Visibility
PCAP Strategy
Flow Collection
DNS Logging
DHCP Logging
Firewall Logging
Proxy Logging
VPN Logging
Time Synchronization
Retention Policies
Sensor Coverage
```

---

# Network Time Synchronization

Accurate timestamps are essential.

Use a consistent enterprise time source where possible.

Investigators should record:

```text
Sensor Time
Endpoint Time
Server Time
Timezone
UTC Conversion
Clock Offset
```

---

# Network Evidence Retention

Retention strategy should consider:

- Incident response requirements
- Storage costs
- Regulatory obligations
- Network volume
- Critical network segments
- Security architecture

A practical architecture may retain:

```text
Longer:
Flow + DNS + Firewall

Shorter:
Full PCAP

Extended:
High-value network segments
```

---

# Encrypted Traffic Strategy

When payload inspection is unavailable, use metadata:

```text
Source
Destination
Timing
Bytes
DNS
Certificate
Process
Identity
```

This supports behavioral detection without decrypting every connection.

---

# Cloud Network Forensics

Cloud environments may provide:

```text
VPC / VNet Flow Logs
Load Balancer Logs
DNS Logs
Firewall Logs
API Logs
Proxy Logs
Endpoint Telemetry
```

Cloud network investigation should correlate identity and infrastructure metadata.

---

# Container Network Forensics

Containerized workloads introduce:

```text
Pod IPs
Container IPs
Node IPs
Service IPs
Overlay Networks
Ingress
Egress
```

Attribution should consider:

```text
Container
Pod
Node
Workload
Identity
```

---

# Network Evidence Confidence

## High Confidence

Multiple independent sources agree.

```text
PCAP
+
DNS
+
Firewall
+
EDR
```

## Medium Confidence

Flow and endpoint evidence support the finding.

## Low Confidence

Only an isolated IP/domain indicator exists.

## Unknown

Insufficient telemetry.

---

# Interview Questions

## 1. What is network forensics?

The investigation of network communications and associated telemetry to reconstruct activity and identify security-relevant behavior.

---

## 2. What is PCAP?

A packet capture containing captured network packets.

---

## 3. What is the difference between PCAP and NetFlow?

PCAP provides packet-level detail.

Flow telemetry generally provides connection metadata without full packet payloads.

---

## 4. Why is DNS important?

DNS can connect:

```text
Host
→ Domain
→ IP
→ Connection
```

making it valuable for investigation.

---

## 5. Does HTTPS hide everything?

No.

It generally protects application content but network metadata may remain visible.

---

## 6. What can investigators still see with encrypted traffic?

Potentially:

- IPs
- Ports
- Timing
- Traffic volume
- TLS metadata
- Certificates
- DNS

Visibility depends on protocol and deployment.

---

## 7. What is beaconing?

Repeated communication between a host and destination, often exhibiting a recurring pattern.

Legitimate applications can also beacon.

---

## 8. What is DNS tunneling?

Using DNS queries/responses as a communication or data-transfer channel.

---

## 9. Why is DHCP useful?

It can help associate IP addresses with devices over time.

---

## 10. Why is NAT important?

Multiple internal systems can appear behind one public address.

---

## 11. How would you investigate possible lateral movement?

Correlate:

```text
Source
Destination
Protocol
User
Authentication
Process
Time
```

---

## 12. How would you investigate suspected exfiltration?

Examine:

```text
Destination
Volume
Protocol
Process
User
Data Source
Timing
Business Context
```

---

## 13. What is Zeek?

A network security monitoring platform that generates rich protocol-level telemetry.

---

## 14. What is Wireshark?

A packet-analysis tool used to inspect and decode network traffic.

---

# Scenario Interview Question

### Scenario

> A workstation makes HTTPS connections to an unfamiliar domain every five minutes.

Investigate:

```text
DNS
   ↓
Domain
   ↓
IP
   ↓
TLS
   ↓
Process
   ↓
Timing
   ↓
Bytes
   ↓
Business Context
```

Do not automatically label it C2.

---

# Scenario Interview Question

### Scenario

> A public IP appears in firewall logs during an incident.

What additional evidence do you need?

```text
NAT Logs
DHCP
Endpoint IP
VPN
Firewall
EDR
Identity
Timestamp
```

This avoids incorrect host attribution.

---

# Scenario Interview Question

### Scenario

> A server transferred several gigabytes to an external cloud provider.

Possible explanations include:

```text
Backup
Cloud Synchronization
Software Distribution
Business Transfer
Data Exfiltration
```

Investigate:

```text
Process
User
Destination
Data
Timing
Authorization
```

---

# Network Forensic Maturity Model

## Level 1 — Basic

- Firewall logs
- Basic packet analysis
- DNS investigation

## Level 2 — Repeatable

- Flow telemetry
- PCAP workflows
- Standard network investigations

## Level 3 — Managed

- Centralized network monitoring
- Zeek
- SIEM
- Retention policies

## Level 4 — Integrated

- Network + EDR
- Threat hunting
- Detection engineering
- Automated enrichment

## Level 5 — Advanced

- Enterprise network analytics
- Large-scale PCAP investigation
- Behavioral detection
- Cloud/container network correlation
- Automated network forensics

---

# Chapter Completion Checklist

```text
[ ] Understand network forensics
[ ] Understand PCAP
[ ] Understand flow telemetry
[ ] Understand TCP
[ ] Understand UDP
[ ] Understand DNS
[ ] Understand HTTP
[ ] Understand HTTPS
[ ] Understand TLS
[ ] Understand DHCP
[ ] Understand ARP
[ ] Understand NAT
[ ] Understand firewall logs
[ ] Understand proxy logs
[ ] Understand VPN evidence
[ ] Understand scanning
[ ] Understand lateral movement
[ ] Understand beaconing
[ ] Understand C2 investigation
[ ] Understand exfiltration investigation
[ ] Understand Wireshark
[ ] Understand Zeek
[ ] Understand NetworkMiner
[ ] Understand network timelines
[ ] Understand evidence gaps
[ ] Complete PCAP lab
[ ] Complete DNS lab
[ ] Complete TLS lab
[ ] Complete beaconing lab
[ ] Complete lateral movement lab
[ ] Complete exfiltration lab
[ ] Complete full network investigation
```

---

# Key Takeaways

Network forensics transforms communications into investigative evidence.

A strong investigation connects:

```text
DNS
 +
Network Flow
 +
PCAP
 +
Firewall
 +
Proxy
 +
Identity
 +
Endpoint
```

Remember:

- PCAP provides detail but can be expensive to retain.
- Flow telemetry provides scalable metadata.
- DNS is essential for domain-to-host correlation.
- DHCP helps establish IP ownership over time.
- NAT complicates attribution.
- HTTPS does not eliminate metadata.
- Beaconing is behavioral, not automatically malicious.
- Large outbound transfers are not automatically exfiltration.
- Network evidence should be correlated with endpoint and identity evidence.
- Time synchronization is essential.
- Missing telemetry should be documented as an evidence gap.

> **Network forensics is the reconstruction of communication, identity, timing, protocol behavior, and data movement across an environment.**

---

# References

### Wireshark

https://www.wireshark.org/

### Zeek

https://zeek.org/

### NetworkMiner

https://www.netresec.com/?page=NetworkMiner

### NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response

https://csrc.nist.gov/publications/detail/sp/800-86/final

### NIST SP 800-61 — Incident Response

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### MITRE ATT&CK

https://attack.mitre.org/

### CISA

https://www.cisa.gov/

### RFC 9293 — Transmission Control Protocol

https://www.rfc-editor.org/rfc/rfc9293

### RFC 1034 — Domain Names

https://www.rfc-editor.org/rfc/rfc1034

### RFC 8446 — TLS 1.3

https://www.rfc-editor.org/rfc/rfc8446

### SANS Network Forensics

https://www.sans.org/cyber-security-skills-roadmap/

---

> **Follow the connection. Identify the process. Correlate the identity. Reconstruct the timeline. Network evidence becomes powerful when communication is connected to the system and user that generated it.**
