# Network Threat Hunting

## Overview

Network Threat Hunting is the proactive investigation of network activity to identify malicious behavior that may not be detected by traditional security controls.

While endpoint telemetry explains what happened on a host, network telemetry helps answer:

- Where did the host communicate?
- Who did it communicate with?
- Which protocol was used?
- What data was exchanged?
- Was the destination expected?
- Did the communication resemble command and control?
- Was lateral movement occurring?
- Was data being transferred outside the organization?

A mature network-hunting capability combines:

- DNS telemetry
- DHCP telemetry
- Firewall logs
- Proxy logs
- NetFlow
- IPFIX
- Zeek
- IDS/IPS
- Network Detection and Response
- Packet capture
- TLS metadata
- HTTP metadata
- VPN logs
- Authentication telemetry
- Endpoint network telemetry
- Threat intelligence

The central principle is:

> **Network hunting is about understanding communication patterns, not merely searching for malicious IP addresses.**

---

# Why Network Threat Hunting Matters

Modern attacks frequently generate network activity.

A typical intrusion may look like:

```text
Initial Access
      │
      ▼
Compromised Endpoint
      │
      ├──────────────► C2
      │
      ├──────────────► Internal Discovery
      │
      ├──────────────► Lateral Movement
      │
      └──────────────► Data Access
                              │
                              ▼
                         Exfiltration
```

Even when malware is unknown, network behavior can expose:

- Beaconing
- DNS tunneling
- Unusual outbound connections
- Lateral movement
- Port scanning
- Remote administration
- Command-and-control traffic
- Data staging
- Exfiltration
- Protocol abuse

---

# Network Hunting Architecture

A typical enterprise network-hunting architecture:

```text
                         INTERNET
                            │
                            ▼
                     ┌─────────────┐
                     │   Firewall  │
                     └──────┬──────┘
                            │
                 ┌──────────┴──────────┐
                 │                     │
                 ▼                     ▼
              Proxy                  DNS
                 │                     │
                 └──────────┬──────────┘
                            │
                            ▼
                       Network Core
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
    Endpoints            Servers              Cloud
        │                   │                   │
        └───────────────────┼───────────────────┘
                            │
                     Network Sensors
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
        Zeek              IDS/IPS          NetFlow
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                           SIEM
                            │
                            ▼
                           SOC
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
              Detection              Hunting
```

---

# Network Telemetry

Different telemetry sources answer different questions.

| Source | Primary Visibility |
|---|---|
| DNS | Domain resolution |
| DHCP | IP-to-host assignments |
| Firewall | Allowed/blocked connections |
| Proxy | Web activity |
| NetFlow | Connection metadata |
| Zeek | Protocol metadata |
| IDS/IPS | Suspicious network patterns |
| PCAP | Full packet-level investigation |
| VPN | Remote access |
| Endpoint | Process-to-network relationship |

No single data source provides complete visibility.

---

# Network Telemetry Model

A network event can be represented conceptually as:

```text
Timestamp
Source IP
Source Port
Destination IP
Destination Port
Protocol
Bytes
Packets
Direction
Action
Hostname
User
Process
```

Example:

```text
2026-10-06 10:21:13
10.10.15.42
53122
203.0.113.50
443
TCP
Outbound
Allowed
```

The event alone does not prove malicious activity.

Context is required.

---

# Network Flow

Network flow records summarize communication without storing every packet.

Common fields include:

```text
Source IP
Destination IP
Source Port
Destination Port
Protocol
Start Time
End Time
Bytes
Packets
```

Example:

```text
10.10.1.20
    │
    └──► 10.10.2.50:445
          8,421 bytes
          143 packets
```

This could indicate legitimate SMB activity or lateral movement.

The surrounding context determines the significance.

---

# NetFlow and IPFIX

NetFlow/IPFIX can help identify:

- Large transfers
- Unusual destinations
- Internal scanning
- Rare communication
- Long-lived connections
- Periodic communication
- Unexpected protocols

Flow data is particularly useful for identifying behavioral patterns.

---

# DNS Threat Hunting

DNS is one of the most valuable sources for threat hunting.

Attackers may use DNS for:

- Command and control
- Infrastructure discovery
- Malware resolution
- Domain generation algorithms
- DNS tunneling
- Data exfiltration

A normal query:

```text
workstation
     │
     ▼
DNS Resolver
     │
     ▼
www.example.com
```

Potentially suspicious activity:

```text
workstation
     │
     ▼
DNS Resolver
     │
     ├── a8f72.example.com
     ├── k92jd.example.com
     ├── p0x91.example.com
     ├── q7m2a.example.com
     └── ...
```

The pattern requires investigation.

---

# DNS Hunting Signals

Useful signals include:

- High query frequency
- Long domain names
- High subdomain entropy
- Rare domains
- Newly observed domains
- High NXDOMAIN rates
- Unusual record types
- Excessive TXT queries
- Repeated queries at regular intervals
- Hosts querying unusual resolvers

---

# DNS Entropy

Attackers may encode information into subdomains.

Example:

```text
aGVsbG93b3JsZA.example.com
```

High-entropy labels can be suspicious when combined with:

```text
High Frequency
+
Rare Domain
+
Long Labels
+
Regular Timing
```

However, CDNs and legitimate applications can also generate long or random-looking hostnames.

---

# DNS Beaconing

Potential beacon:

```text
10:00:00 → abc.example.com
10:05:00 → def.example.com
10:10:00 → ghi.example.com
10:15:00 → jkl.example.com
10:20:00 → mno.example.com
```

Regular intervals can be an important signal.

But periodic traffic can also come from:

- Monitoring agents
- Software updates
- Cloud applications
- Collaboration software
- Telemetry services

Therefore:

> **Periodic communication is a hunting signal, not proof of C2.**

---

# NXDOMAIN Hunting

An unusual number of failed DNS queries may indicate:

```text
Possible DGA
Misconfigured Software
Malware
Scanning
Application Failure
```

Conceptual detection:

```text
Host
  │
  ▼
DNS Queries
  │
  ├── Successful
  └── NXDOMAIN
          │
          ▼
     High Frequency
          │
          ▼
       Investigate
```

---

# DNS Tunneling

DNS tunneling can encode data inside DNS queries or responses.

Conceptual pattern:

```text
Endpoint
   │
   ▼
Encoded Data
   │
   ▼
DNS Query
   │
   ▼
Attacker DNS Infrastructure
```

Potential indicators:

- High DNS volume
- Long labels
- High entropy
- Repeated subdomains
- Unusual TXT records
- Low normal domain prevalence
- Persistent communication

---

# HTTP Threat Hunting

HTTP telemetry can provide:

- Host
- URI
- Method
- User-Agent
- Status code
- Response size
- Referrer
- Destination
- Request frequency

Example:

```text
POST /api/update
Host: example.com
User-Agent: Mozilla/5.0
```

The request may be legitimate.

The hunter should investigate the surrounding behavior.

---

# HTTP POST Hunting

POST requests are commonly used by legitimate applications.

They can also be used for:

- C2
- Credential submission
- Data exfiltration
- Web shells
- Malware communication

Useful context:

```text
POST
+
Rare Destination
+
Unusual User-Agent
+
Endpoint Process
+
Periodic Timing
```

---

# HTTPS Hunting

HTTPS encrypts application content.

However, metadata can still be useful.

Available signals may include:

```text
Source
Destination
Port
SNI
Certificate
TLS Version
JA3/JA4 where available
Connection Duration
Bytes
Packets
Frequency
```

Encryption does not eliminate network visibility.

---

# TLS Metadata

Useful TLS hunting attributes can include:

- Server Name Indication
- Certificate information
- TLS version
- Cipher characteristics
- Connection timing
- Destination IP
- Certificate age
- Certificate reuse

TLS fingerprints can sometimes help cluster similar clients.

They should be treated as behavioral signals rather than definitive attribution.

---

# Proxy Hunting

Enterprise proxies may provide:

```text
User
Source IP
URL
Domain
Category
HTTP Method
Response Code
Bytes
User-Agent
Timestamp
```

A useful hunting workflow:

```text
User
 │
 ▼
Proxy Request
 │
 ▼
Domain
 │
 ▼
Threat Intelligence
 │
 ▼
Endpoint Process
 │
 ▼
Investigation
```

---

# Firewall Hunting

Firewall logs can reveal:

- Allowed connections
- Blocked connections
- Source
- Destination
- Port
- Protocol
- Application
- NAT information

Example:

```text
10.10.20.15
      │
      ├──► 443 → Internet
      ├──► 53  → DNS
      └──► 445 → Internal
```

Unexpected communication should be investigated.

---

# Allowed vs Blocked Traffic

Blocked traffic can be valuable.

Repeated blocked connections:

```text
Host
 │
 ├──► C2 IP ── BLOCK
 ├──► C2 IP ── BLOCK
 ├──► C2 IP ── BLOCK
 └──► C2 IP ── BLOCK
```

may indicate a compromised endpoint attempting persistence or reconnection.

Therefore:

> **Do not ignore blocked events.**

---

# Internal Network Hunting

Threat hunting should not stop at the Internet boundary.

Important internal protocols include:

```text
SMB       445
RDP       3389
WinRM     5985/5986
LDAP      389/636
Kerberos  88
DNS       53
SSH       22
RPC       Dynamic ports
```

Unexpected internal communication can indicate:

- Lateral movement
- Discovery
- Remote administration
- Credential abuse
- Malware propagation

---

# SMB Hunting

SMB is legitimate in Windows environments.

Potentially suspicious patterns include:

```text
Workstation
   │
   ├──► Server A
   ├──► Server B
   ├──► Server C
   ├──► Server D
   └──► Server E
```

A workstation suddenly connecting to many systems over SMB deserves investigation.

Correlate with:

- User
- Authentication
- Process
- File access
- Administrative shares

---

# RDP Hunting

RDP is widely used for administration.

Potentially suspicious behavior:

```text
User Workstation
      │
      ▼
Internal Server
      │
      ▼
RDP
      │
      ▼
Privileged Account
```

Investigate:

- Source host
- Destination
- User
- Time
- Authentication
- Frequency
- Geographic context
- Previous activity

---

# WinRM Hunting

WinRM can support legitimate administration and remote execution.

Monitor:

```text
Source Host
Destination Host
User
Authentication
Frequency
Process Activity
```

A new workstation-to-server WinRM relationship can be significant.

---

# Network Scanning

Scanning can be identified through connection patterns.

Example:

```text
10.10.1.20
 │
 ├──► 10.10.2.1:22
 ├──► 10.10.2.2:22
 ├──► 10.10.2.3:22
 ├──► 10.10.2.4:22
 └──► ...
```

Signals include:

- High destination count
- Sequential IP addresses
- Sequential ports
- Short-lived connections
- High failure rates

But legitimate scanners also generate this behavior.

Always identify authorized scanning infrastructure.

---

# Port Scanning

Conceptually:

```text
Host A
 │
 ├──► Port 21
 ├──► Port 22
 ├──► Port 23
 ├──► Port 25
 ├──► Port 53
 ├──► Port 80
 └──► ...
```

Potential indicators:

```text
Many Ports
+
Many Targets
+
Short Time Window
+
Low Success Rate
```

---

# Horizontal vs Vertical Scanning

## Horizontal Scan

One port across many hosts:

```text
Attacker
 │
 ├──► Host 1:445
 ├──► Host 2:445
 ├──► Host 3:445
 └──► Host 4:445
```

## Vertical Scan

Many ports against one host:

```text
Attacker
 │
 ├──► Host 1:22
 ├──► Host 1:80
 ├──► Host 1:443
 └──► Host 1:445
```

These patterns can help identify reconnaissance.

---

# C2 Hunting

Command and control traffic may have characteristics such as:

- Periodic communication
- Rare destinations
- Small regular packets
- Persistent connections
- Unusual protocols
- Uncommon ports
- Dynamic infrastructure
- Encrypted communication

A generic C2 pattern:

```text
Endpoint
   │
   ├──── Request ────► C2
   │
   ◄─── Response ─────┤
   │
   ├──── Request ────► C2
   │
   ◄─── Response ─────┤
   │
   └──── Repeat ──────►
```

---

# Beaconing Analysis

Beaconing can be analyzed through:

```text
Interval
Jitter
Connection Duration
Bytes Sent
Bytes Received
Destination
DNS
Process
```

Example:

```text
Interval:
60 seconds
60 seconds
59 seconds
61 seconds
60 seconds
```

Regularity can be suspicious.

However, legitimate software also uses scheduled communication.

---

# Beaconing Detection Model

```text
Connection
     │
     ▼
Group by Host + Destination
     │
     ▼
Calculate Intervals
     │
     ▼
Measure Regularity
     │
     ▼
Check Destination Rarity
     │
     ▼
Correlate Endpoint Process
```

This produces a stronger signal than searching for a known C2 IP.

---

# C2 Over Common Ports

Attackers may communicate over:

```text
80
443
53
22
```

Using common ports does not make the communication legitimate.

A useful rule:

> **Port number describes transport behavior, not application intent.**

---

# User-Agent Hunting

Unusual User-Agent strings can provide clues.

Examples of suspicious characteristics:

```text
Rare User-Agent
Unusual Version
Malformed String
Inconsistent Browser Identity
```

But custom applications may legitimately use non-browser User-Agents.

Correlate with:

```text
Process
Host
User
Destination
Frequency
```

---

# Network-Based Malware Hunting

A suspicious endpoint may generate:

```text
DNS
 ↓
TCP
 ↓
TLS
 ↓
HTTP
 ↓
File Download
 ↓
Process Execution
```

This can reveal a compromise even when endpoint malware signatures are unavailable.

---

# Network Data Exfiltration

Potential exfiltration signals include:

- Large outbound transfers
- Rare external destinations
- Unusual protocols
- High upload-to-download ratio
- Compression before transfer
- Cloud storage uploads
- Long-lived connections

Conceptual pattern:

```text
Internal Server
      │
      ▼
Sensitive Data
      │
      ▼
Staging
      │
      ▼
Compression
      │
      ▼
External Destination
```

---

# Volume-Based Hunting

Example:

```text
Normal:
Host → Internet
50 MB/day

Observed:
Host → New External IP
4 GB in 30 minutes
```

This should be investigated.

However, legitimate backups, software updates, and cloud synchronization can also generate large transfers.

---

# Data Staging

Attackers may collect data before exfiltration.

Potential indicators:

```text
Many Files
    │
    ▼
Temporary Directory
    │
    ▼
Archive
    │
    ▼
Large Outbound Transfer
```

Correlate:

```text
File Activity
+
Process Activity
+
Network Transfer
```

---

# Cloud Exfiltration Hunting

Modern organizations frequently use:

- Cloud storage
- SaaS applications
- Collaboration platforms
- Developer repositories

Therefore, exfiltration may occur through legitimate services.

Network-only detection can become difficult.

Combine:

```text
Network
+
Identity
+
Cloud Audit Logs
+
Endpoint
```

---

# Network Tunneling

Tunneling can hide one protocol inside another.

Examples conceptually include:

```text
Application Data
      │
      ▼
Tunnel
      │
      ▼
Allowed Protocol
```

Potential indicators:

- Unexpected protocol behavior
- Long-lived connections
- Unusual packet patterns
- High-frequency communication
- Rare destinations
- Protocol misuse

---

# ICMP Hunting

ICMP is commonly used for diagnostics.

Suspicious patterns can include:

```text
Large ICMP Packets
High Frequency
Unusual External Destination
Encoded Payload Patterns
```

But legitimate monitoring systems can generate significant ICMP traffic.

---

# IPv6 Hunting

Organizations should not ignore IPv6.

Important telemetry includes:

- IPv6 addresses
- DNS AAAA records
- Neighbor discovery
- IPv6 firewall events
- Endpoint connections

Security controls should provide equivalent visibility for IPv4 and IPv6.

---

# Zeek

Zeek is a network security monitoring framework that produces rich protocol metadata.

Common Zeek logs include:

```text
conn.log
dns.log
http.log
ssl.log
files.log
ssh.log
smtp.log
```

---

# Zeek Connection Hunting

Conceptually:

```text
Source
Destination
Port
Protocol
Duration
Bytes
```

Example:

```text
10.10.1.15
   │
   └──► 203.0.113.20:443
          Duration: 32s
          Bytes: 14KB
```

The value comes from correlation.

---

# Zeek DNS Hunting

Example fields can include:

```text
query
qtype
rcode
answers
client
server
```

Potential hunting workflow:

```text
DNS Query
   │
   ▼
Rare Domain
   │
   ▼
High Frequency
   │
   ▼
Endpoint Correlation
   │
   ▼
Investigate
```

---

# Zeek HTTP Hunting

Potential fields include:

```text
method
host
uri
user_agent
status_code
request_body_len
response_body_len
```

Useful for investigating:

- Suspicious downloads
- Web shells
- C2
- Unusual User-Agents
- Data transfer

---

# IDS/IPS Hunting

IDS/IPS systems provide alerts for known suspicious patterns.

However:

> **IDS alerts should be treated as investigation leads, not complete incident conclusions.**

For every alert:

```text
Alert
 │
 ▼
Source
 │
 ▼
Destination
 │
 ▼
Protocol
 │
 ▼
Endpoint
 │
 ▼
User
 │
 ▼
Timeline
```

---

# Signature vs Behavioral Network Detection

## Signature

```text
Known IOC
    ↓
Match
    ↓
Alert
```

## Behavioral

```text
Rare Destination
+
Periodic Traffic
+
Suspicious Process
+
Unusual User
    ↓
Investigate
```

Behavioral approaches can identify previously unknown activity.

---

# Threat Intelligence Enrichment

Network indicators can be enriched with:

```text
IP Reputation
Domain Reputation
ASN
WHOIS
Passive DNS
Certificate Data
Malware Associations
Threat Actor Intelligence
ATT&CK Mapping
```

Do not automatically classify an event as malicious based solely on reputation.

---

# IP Reputation Limitations

Shared infrastructure creates false positives.

An IP may host:

```text
CDN
Cloud Services
Shared Hosting
Multiple Customers
Legitimate Applications
```

Therefore:

```text
IP Reputation
+
Observed Behavior
+
Endpoint Context
```

is stronger than reputation alone.

---

# Domain Age

Newly registered domains can be useful hunting signals.

But legitimate organizations also register new domains.

Use:

```text
Domain Age
+
Rare Host
+
Suspicious Process
+
Unusual DNS
```

rather than:

```text
Domain Age < X
→ Malicious
```

---

# JA3/JA4 and TLS Fingerprinting

TLS fingerprinting can help identify similar TLS client behavior.

Conceptually:

```text
TLS Client
    │
    ▼
Fingerprint
    │
    ▼
Cluster
    │
    ▼
Compare Known / Unknown Clients
```

Fingerprints can be useful for hunting but should not be treated as immutable malware identifiers.

Applications and libraries can share fingerprints.

---

# Network Investigation Workflow

## Step 1 — Identify the Communication

```text
Source
Destination
Port
Protocol
Time
```

## Step 2 — Identify the Host

```text
Hostname
Asset Type
Owner
Role
Location
```

## Step 3 — Identify the User

```text
Account
Department
Privilege
Session
```

## Step 4 — Identify the Process

Where endpoint telemetry exists:

```text
Process
Parent
Command Line
```

## Step 5 — Enrich Destination

```text
Domain
IP
ASN
Reputation
Threat Intelligence
```

## Step 6 — Analyze Behavior

```text
Frequency
Volume
Timing
Rarity
Direction
Protocol
```

## Step 7 — Build Timeline

```text
DNS
 ↓
Connection
 ↓
Process
 ↓
File
 ↓
Persistence
```

## Step 8 — Scope

Search for:

```text
Same IP
Same Domain
Same Hash
Same User
Same Process
Same Destination
```

---

# Practical Lab 1 — DNS Anomaly Hunt

## Objective

Identify endpoints generating unusual DNS activity.

### Step 1

Group DNS queries by host.

### Step 2

Calculate:

```text
Query Count
Unique Domains
NXDOMAIN Count
Unique Subdomains
```

### Step 3

Identify unusual hosts.

### Step 4

Investigate:

```text
Rare Domains
Long Labels
High Entropy
High Frequency
```

### Step 5

Correlate with endpoint processes.

---

# Practical Lab 2 — Beaconing Hunt

## Objective

Identify periodic network communication.

Workflow:

```text
Network Events
      │
      ▼
Group Host + Destination
      │
      ▼
Sort by Timestamp
      │
      ▼
Calculate Intervals
      │
      ▼
Measure Regularity
      │
      ▼
Investigate
```

Questions:

- Is the destination rare?
- Is the interval regular?
- Which process generated the traffic?
- Is the destination legitimate?
- Does the behavior persist?

---

# Practical Lab 3 — Internal SMB Hunt

Search for:

```text
Source
Destination
Port = 445
```

Identify:

```text
Workstation → Workstation
Workstation → Server
Server → Workstation
```

Pay particular attention to unusual workstation-to-workstation communication.

Correlate with authentication and process activity.

---

# Practical Lab 4 — Network Scanning Hunt

Identify hosts that contact unusually large numbers of destinations.

Example:

```text
Source Host
    │
    ├──► 100 destinations
    ├──► 200 destinations
    └──► 500 destinations
```

Separate:

```text
Authorized Scanner
```

from:

```text
Unknown Endpoint
```

---

# Practical Lab 5 — Large Outbound Transfer

Find:

```text
Source Host
Destination
Bytes Sent
Bytes Received
Duration
```

Sort by outbound volume.

Then ask:

```text
Is the destination expected?
Was the user authorized?
Was the process expected?
Was the data transfer business-related?
```

---

# Practical Lab 6 — Rare External Destination

Find destinations contacted by very few endpoints.

Example:

```text
Destination
    │
    ▼
Host Count = 1
```

Then correlate:

```text
Process
User
Domain
DNS
Time
Volume
```

Rare destinations can provide excellent hunting leads.

---

# Practical Lab 7 — C2 Correlation

Hypothesis:

> A compromised endpoint periodically communicates with external infrastructure.

Search for:

```text
Periodic Connections
+
Rare Destination
+
Unusual Process
```

Then investigate:

```text
DNS
TLS
Process
User
File
Persistence
```

---

# Practical Lab 8 — Exfiltration Investigation

Hypothesis:

> An endpoint may be transferring sensitive data externally.

Search for:

```text
Large Outbound Transfer
+
Rare Destination
+
File Staging
```

Build:

```text
Collection
 ↓
Staging
 ↓
Compression
 ↓
Network Transfer
```

timeline.

---

# SIEM Query Concepts

A generic network hunting query may resemble:

```text
source_ip
destination_ip
destination_port
protocol
bytes_sent
bytes_received
timestamp
```

Then group by:

```text
source_ip + destination_ip
```

and calculate:

```text
connection_count
total_bytes
first_seen
last_seen
```

---

# Example Splunk-Style Hunt

Conceptual:

```spl
index=network
| stats
    count as connections
    sum(bytes_out) as bytes_out
    sum(bytes_in) as bytes_in
    min(_time) as first_seen
    max(_time) as last_seen
    by src_ip, dest_ip, dest_port
| sort - bytes_out
```

This is a hunting starting point and should be adapted to the organization's schema.

---

# Example DNS Hunt

```spl
index=dns
| stats
    count as queries
    dc(query) as unique_domains
    by src_ip
| sort - queries
```

Investigate hosts with unusually high DNS activity.

---

# Example Rare Destination Hunt

```spl
index=network
| stats dc(src_ip) as host_count by dest_ip
| where host_count <= 2
```

This identifies destinations observed from very few internal hosts.

It should then be enriched and investigated.

---

# Network Hunting With Python

Python can be useful for analyzing exported network telemetry.

Example:

```python
import pandas as pd

df = pd.read_csv("network.csv")

summary = (
    df.groupby(["src_ip", "dest_ip"])
      .agg(
          connections=("dest_ip", "count"),
          bytes_sent=("bytes_sent", "sum"),
          bytes_received=("bytes_received", "sum")
      )
      .reset_index()
)

print(summary.sort_values("bytes_sent", ascending=False).head(20))
```

This is particularly useful for exploratory hunting and offline analysis.

---

# Network Hunting With Wireshark

Wireshark is useful when metadata is insufficient and packet-level analysis is required.

Useful display filters include:

```text
dns
```

```text
http
```

```text
tls
```

```text
tcp
```

```text
icmp
```

For a specific host:

```text
ip.addr == 10.10.10.20
```

For a specific port:

```text
tcp.port == 443
```

For DNS queries:

```text
dns.qry.name
```

Use packet captures carefully and only within authorized environments.

---

# PCAP Investigation Workflow

```text
PCAP
 │
 ▼
Identify Hosts
 │
 ▼
Identify Protocols
 │
 ▼
Identify Conversations
 │
 ▼
Inspect DNS
 │
 ▼
Inspect HTTP/TLS
 │
 ▼
Follow TCP Streams
 │
 ▼
Extract Indicators
 │
 ▼
Correlate With Endpoint
```

---

# Network Hunting and MITRE ATT&CK

Useful techniques include:

| Technique | Description |
|---|---|
| T1046 | Network Service Scanning |
| T1071 | Application Layer Protocol |
| T1071.001 | Web Protocols |
| T1071.004 | DNS |
| T1095 | Non-Application Layer Protocol |
| T1571 | Non-Standard Port |
| T1041 | Exfiltration Over C2 Channel |
| T1048 | Exfiltration Over Alternative Protocol |
| T1105 | Ingress Tool Transfer |
| T1021 | Remote Services |
| T1021.001 | RDP |
| T1021.002 | SMB/Windows Admin Shares |
| T1021.006 | Windows Remote Management |
| T1210 | Exploitation of Remote Services |
| T1090 | Proxy |
| T1572 | Protocol Tunneling |

ATT&CK mappings should be validated against the current ATT&CK knowledge base when used in production material.

---

# Network Hunting Checklist

## DNS

- [ ] Query volume reviewed
- [ ] Rare domains reviewed
- [ ] NXDOMAIN analyzed
- [ ] Long labels reviewed
- [ ] High entropy investigated
- [ ] TXT queries reviewed
- [ ] DNS resolver behavior checked

## Web

- [ ] HTTP requests reviewed
- [ ] HTTPS metadata reviewed
- [ ] User-Agent analyzed
- [ ] Rare destinations checked
- [ ] Proxy logs correlated

## Network Flow

- [ ] Source identified
- [ ] Destination identified
- [ ] Port identified
- [ ] Protocol identified
- [ ] Bytes analyzed
- [ ] Connection frequency analyzed

## Internal Network

- [ ] SMB reviewed
- [ ] RDP reviewed
- [ ] WinRM reviewed
- [ ] LDAP/Kerberos reviewed
- [ ] Scanning behavior reviewed

## C2

- [ ] Beaconing checked
- [ ] Periodicity checked
- [ ] Rare destinations checked
- [ ] Process-to-network relationship checked
- [ ] DNS correlation completed

## Exfiltration

- [ ] Outbound volume reviewed
- [ ] Destination reputation checked
- [ ] Staging activity reviewed
- [ ] Compression/archive activity reviewed
- [ ] Identity context reviewed

---

# Common Network Hunting Mistakes

## 1. Blocking Every Suspicious IP

Cloud and shared infrastructure can produce false positives.

---

## 2. Hunting Only Known IOCs

Unknown infrastructure will not match IOC lists.

---

## 3. Ignoring Internal Traffic

Lateral movement often occurs inside the trusted network.

---

## 4. Ignoring DNS

DNS often provides early clues about malicious infrastructure.

---

## 5. Ignoring Blocked Connections

Repeated blocked C2 attempts can reveal compromised hosts.

---

## 6. Ignoring Endpoint Context

Network activity becomes much stronger when tied to a process.

---

## 7. Assuming HTTPS Means Invisible

Metadata remains available even when payload content is encrypted.

---

# Network Detection Engineering

Successful hunts should become detections where appropriate.

Pipeline:

```text
Hunt
 │
 ▼
Behavior Identified
 │
 ▼
Validate
 │
 ▼
Build Detection
 │
 ▼
Test
 │
 ▼
Tune
 │
 ▼
Deploy
 │
 ▼
Measure
```

Example:

```text
Rare External Destination
+
Periodic Communication
+
Unknown Process
```

may become a detection candidate.

---

# Network Detection Quality

A useful detection should answer:

```text
What happened?
Why is it suspicious?
Which host?
Which user?
Which destination?
What process?
What ATT&CK technique?
What should the analyst do next?
```

A detection without investigation context creates unnecessary analyst workload.

---

# Enterprise Network Visibility

A mature environment should provide visibility across:

```text
Internet
 │
 ├── DNS
 ├── Proxy
 ├── Firewall
 └── TLS
       │
       ▼
Internal Network
 │
 ├── Servers
 ├── Endpoints
 ├── Identity
 └── Network Services
       │
       ▼
Cloud
 │
 ├── SaaS
 ├── IaaS
 └── PaaS
```

---

# Network Hunting Maturity Model

## Level 1 — Perimeter Monitoring

```text
Firewall
IDS
Proxy
```

---

## Level 2 — Flow Visibility

```text
NetFlow
IPFIX
DNS
```

---

## Level 3 — Protocol Visibility

```text
Zeek
HTTP
TLS
DNS
SMTP
SSH
```

---

## Level 4 — Behavioral Hunting

```text
Baseline
+
Anomaly
+
Correlation
```

---

## Level 5 — Detection Engineering

```text
Threat Intelligence
       ↓
Hypothesis
       ↓
Network Hunt
       ↓
Detection
       ↓
Automation
       ↓
Continuous Improvement
```

---

# Professional Network Investigation Template

```text
Incident ID:

Date/Time:

Source Host:
Source IP:
User:

Destination:
Destination IP:
Destination Port:
Protocol:

DNS Activity:

HTTP/HTTPS Activity:

Firewall Activity:

Proxy Activity:

Flow Information:

Endpoint Process:

Command Line:

Threat Intelligence:

First Seen:
Last Seen:

Related Hosts:

Related Users:

Potential ATT&CK Techniques:

Timeline:

Assessment:

Containment:

Remediation:

Detection Improvement:

Lessons Learned:
```

---

# Interview Questions

## 1. What is network threat hunting?

Network threat hunting is the proactive investigation of network telemetry to identify suspicious or malicious communication that may not have generated an existing alert.

---

## 2. What is NetFlow?

NetFlow is flow-level network telemetry describing communication metadata such as source, destination, ports, protocol, timing, and traffic volume.

---

## 3. What is the difference between NetFlow and PCAP?

NetFlow provides metadata about network conversations.

PCAP contains packet-level information and can provide significantly more detail.

---

## 4. Why is DNS useful for threat hunting?

DNS can reveal:

- Malicious domains
- C2
- DGA behavior
- DNS tunneling
- Rare infrastructure
- Malware resolution patterns

---

## 5. What is beaconing?

Beaconing is repeated communication between a host and another system, often with recognizable timing or periodicity.

---

## 6. Is beaconing always malicious?

No.

Legitimate monitoring, update, synchronization, and cloud applications can generate periodic traffic.

---

## 7. How would you detect network scanning?

I would look for unusually high numbers of destinations or ports contacted in a short period and distinguish authorized scanners from unexpected endpoints.

---

## 8. What is DNS tunneling?

DNS tunneling is the use of DNS queries or responses to transport information that is not ordinary DNS application data.

---

## 9. How would you detect data exfiltration?

I would correlate:

```text
Large Outbound Transfer
+
Rare Destination
+
File Staging
+
Compression
+
Unusual Process/User
```

---

## 10. Why should blocked firewall traffic be investigated?

Repeated blocked communication can indicate a compromised endpoint attempting to reach malicious infrastructure.

---

## 11. How would you hunt for lateral movement?

I would examine unusual internal connections involving:

```text
SMB
RDP
WinRM
SSH
LDAP
Kerberos
RPC
```

and correlate them with authentication and endpoint telemetry.

---

## 12. How does EDR improve network hunting?

EDR can associate network connections with the process and user that generated them.

---

## 13. What is beaconing jitter?

Jitter is variation around an otherwise periodic communication interval. Attackers may introduce it to make communication less obviously periodic.

---

## 14. Can HTTPS traffic be hunted?

Yes.

Even when payloads are encrypted, metadata such as destination, timing, SNI where available, certificate information, connection duration, and traffic volume can remain useful.

---

## 15. What is the biggest limitation of IOC-based network hunting?

It can miss unknown infrastructure and previously unseen attacker behavior.

Behavioral and hypothesis-driven hunting provides broader coverage.

---

# Key Takeaways

1. **Network telemetry provides critical visibility into attacker communication.**
2. **DNS is one of the most valuable sources for network hunting.**
3. **Internal traffic is just as important as Internet traffic.**
4. **Beaconing can reveal command-and-control behavior.**
5. **Rare destinations can be valuable hunting leads.**
6. **Network scanning can reveal reconnaissance and lateral movement.**
7. **SMB, RDP, WinRM, SSH, LDAP, and Kerberos deserve careful monitoring.**
8. **HTTPS encryption does not eliminate metadata-based hunting.**
9. **Large outbound transfers require contextual investigation.**
10. **Network activity becomes significantly more valuable when correlated with endpoint processes and identities.**
11. **Blocked connections can reveal attempted malicious communication.**
12. **Behavioral hunting is stronger than IOC-only hunting.**
13. **PCAP is valuable when metadata is insufficient.**
14. **Zeek can provide rich protocol-level telemetry for threat hunting.**
15. **Successful network hunts should feed detection engineering.**

The core mindset is:

> **Don't ask only "Did this IP communicate with the organization?" Ask "Why did this host communicate with this destination, using this protocol, at this time, through this process, under this identity?"**

---

# References

- MITRE ATT&CK — Enterprise  
  https://attack.mitre.org/

- Zeek Documentation  
  https://docs.zeek.org/

- Wireshark Documentation  
  https://www.wireshark.org/docs/

- CISA Cybersecurity Resources  
  https://www.cisa.gov/topics/cybersecurity

- RFC 1034 — Domain Names  
  https://www.rfc-editor.org/rfc/rfc1034

- RFC 1035 — Domain Names  
  https://www.rfc-editor.org/rfc/rfc1035

- RFC 7011 — IPFIX Protocol  
  https://www.rfc-editor.org/rfc/rfc7011

- RFC 3954 — Cisco Systems NetFlow Services Export Version 9  
  https://www.rfc-editor.org/rfc/rfc3954

- Suricata Documentation  
  https://docs.suricata.io/

- Snort Documentation  
  https://docs.snort.org/

- Security Onion Documentation  
  https://docs.securityonion.net/

- MITRE ATT&CK Data Sources  
  https://attack.mitre.org/datasources/

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework
