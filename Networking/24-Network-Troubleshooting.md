# 24 - Network Troubleshooting

# Part 1 — Troubleshooting Fundamentals, Methodologies, OSI Model Approach, TCP/IP Troubleshooting, Root Cause Analysis, and Enterprise Best Practices

---

# Overview

Network Troubleshooting is the systematic process of identifying, isolating, diagnosing, and resolving problems that affect network availability, performance, reliability, and security.

Enterprise networks are highly interconnected and consist of:

- Routers
- Switches
- Firewalls
- Wireless Infrastructure
- VPN Gateways
- Cloud Services
- Data Centers
- SD-WAN
- Endpoints
- Applications

A failure in one component can quickly impact multiple business services.

Effective troubleshooting minimizes:

- Downtime
- Revenue loss
- Customer impact
- Security risks
- Operational costs

Modern organizations rely on structured troubleshooting methodologies rather than trial-and-error approaches.

---

# Learning Objectives

After completing this chapter, you will understand:

- Enterprise troubleshooting methodologies
- OSI model troubleshooting
- TCP/IP troubleshooting
- Root Cause Analysis (RCA)
- Incident prioritization
- Change validation
- Escalation procedures
- Enterprise troubleshooting best practices

---

# What is Network Troubleshooting?

Network troubleshooting is the process of diagnosing and correcting faults within network infrastructure.

Its objectives include:

- Restoring service availability
- Identifying root causes
- Preventing recurrence
- Maintaining business continuity
- Improving operational resilience

Troubleshooting is both a technical and analytical discipline.

---

# Why Troubleshooting Matters

Effective troubleshooting enables organizations to:

- Reduce Mean Time to Detect (MTTD)
- Reduce Mean Time to Repair (MTTR)
- Improve service availability
- Meet Service Level Agreements (SLAs)
- Enhance customer satisfaction
- Strengthen operational efficiency

---

# Enterprise Troubleshooting Lifecycle

```
Problem Reported

↓

Validate Problem

↓

Determine Scope

↓

Collect Information

↓

Analyze Data

↓

Identify Root Cause

↓

Implement Resolution

↓

Validate Fix

↓

Monitor Environment

↓

Document Findings

↓

Lessons Learned
```

Following a repeatable lifecycle ensures consistency and reduces the risk of introducing new issues.

---

# Structured Troubleshooting Methodology

A structured methodology generally includes:

1. Identify the problem.
2. Establish the scope.
3. Gather relevant information.
4. Formulate possible causes.
5. Test hypotheses.
6. Implement the solution.
7. Verify service restoration.
8. Document findings and preventive actions.

Skipping steps often leads to incomplete resolutions.

---

# Incident Prioritization

Not all incidents require the same urgency.

| Priority | Description | Typical Response |
|----------|-------------|------------------|
| P1 | Critical outage affecting core business | Immediate |
| P2 | Major degradation with limited workarounds | High |
| P3 | Partial service disruption | Normal |
| P4 | Minor issue or cosmetic problem | Low |

Prioritization ensures that critical business services receive immediate attention.

---

# Incident Severity vs Priority

These terms are related but different.

| Severity | Priority |
|-----------|----------|
| Measures technical impact | Measures business urgency |
| Evaluated by engineers | Influenced by business needs |
| Often objective | May be subjective |

Example:

A minor network fault affecting a hospital emergency system may receive the highest priority due to business impact.

---

# Defining the Scope

Before troubleshooting, determine:

- Who is affected?
- Which services are affected?
- Which locations are affected?
- When did the issue begin?
- Is the issue intermittent or continuous?
- Were any recent changes made?

A clearly defined scope prevents unnecessary investigation.

---

# Gathering Information

Collect information from multiple sources:

- Monitoring dashboards
- Syslog
- SNMP
- NetFlow/IPFIX
- Firewall logs
- Authentication logs
- Cloud telemetry
- User reports
- Change management records

The more context collected, the faster the root cause can often be identified.

---

# Root Cause Analysis (RCA)

Root Cause Analysis identifies the underlying reason for an incident rather than only addressing symptoms.

```
Service Outage

↓

High Latency

↓

Interface Errors

↓

Faulty Cable

↓

Root Cause
```

Resolving the root cause reduces repeat incidents.

---

# The Five Whys Technique

The "Five Whys" is a simple RCA method.

Example:

```
Application unavailable

↓

Why?

Database unreachable

↓

Why?

Network interface down

↓

Why?

Switch port disabled

↓

Why?

Incorrect configuration applied

↓

Root Cause Identified
```

The number of "whys" may vary depending on the complexity of the issue.

---

# Fault Domains

Divide the infrastructure into logical fault domains.

```
Client

↓

Access Network

↓

Distribution Layer

↓

Core Network

↓

WAN

↓

Cloud

↓

Application

↓

Database
```

Isolating fault domains narrows the investigation.

---

# OSI Model Troubleshooting

The OSI model provides a structured framework for troubleshooting.

```
Layer 7  Application

↓

Layer 6  Presentation

↓

Layer 5  Session

↓

Layer 4  Transport

↓

Layer 3  Network

↓

Layer 2  Data Link

↓

Layer 1  Physical
```

Engineers can troubleshoot from the bottom up, top down, or by targeting the suspected layer.

---

# Bottom-Up Approach

Begin with the Physical Layer and work upward.

```
Physical

↓

Data Link

↓

Network

↓

Transport

↓

Application
```

Advantages:

- Quickly identifies hardware failures.
- Effective for connectivity issues.

---

# Top-Down Approach

Begin with the application and move downward.

```
Application

↓

Transport

↓

Network

↓

Data Link

↓

Physical
```

Advantages:

- Ideal when users report application problems.
- Efficient for software-related issues.

---

# Divide-and-Conquer Approach

Start at the layer most likely to contain the fault.

```
Network Layer

↓

Working?

↓

Yes → Move Up

↓

No → Move Down
```

Experienced engineers frequently use this approach to reduce troubleshooting time.

---

# Follow-the-Path Method

Trace the complete communication path.

```
Client

↓

Switch

↓

Router

↓

Firewall

↓

WAN

↓

Cloud

↓

Application

↓

Database
```

Verify each hop individually to isolate failures.

---

# Troubleshooting by TCP/IP Model

The TCP/IP model can also guide investigations.

| Layer | Common Problems |
|--------|-----------------|
| Application | DNS, HTTP, SMTP, FTP |
| Transport | TCP resets, UDP loss |
| Internet | Routing, IP addressing |
| Network Access | Ethernet, ARP, VLANs |

---

# Physical Layer Issues

Common causes include:

- Damaged cables
- Loose connectors
- Failed transceivers
- Power failures
- Hardware defects

Symptoms:

- Link down
- Interface flapping
- CRC errors
- Packet loss

---

# Data Link Layer Issues

Typical problems include:

- VLAN misconfiguration
- STP issues
- Duplex mismatch
- MAC table problems
- Port security violations

Symptoms:

- Intermittent connectivity
- Broadcast storms
- Switching loops

---

# Network Layer Issues

Common issues:

- Incorrect IP addresses
- Routing failures
- Missing routes
- Subnet mismatch
- ACL blocking

Symptoms:

- Destination unreachable
- One-way communication
- Inter-site connectivity failures

---

# Transport Layer Issues

Potential causes:

- Closed ports
- TCP retransmissions
- Session timeouts
- Firewall filtering
- Load balancer configuration

Symptoms:

- Connection resets
- Slow applications
- Failed sessions

---

# Application Layer Issues

Examples:

- DNS failures
- HTTP 500 errors
- Authentication failures
- Database connectivity issues
- API errors

Application problems often appear as network issues from the user's perspective.

---

# Layered Verification Example

```
User Cannot Access Website

↓

Ping Gateway

↓

DNS Resolution

↓

Traceroute

↓

TCP Port 443

↓

TLS Handshake

↓

Application Logs

↓

Root Cause
```

Verifying each layer systematically reduces troubleshooting time.

---

# Business Impact

Structured troubleshooting enables organizations to:

- Restore services faster
- Reduce operational costs
- Improve customer satisfaction
- Minimize downtime
- Strengthen service reliability
- Meet regulatory and contractual obligations

---

# Enterprise Troubleshooting Best Practices

Organizations should:

- Follow documented troubleshooting procedures.
- Clearly define incident scope before making changes.
- Use monitoring data to support decisions.
- Perform Root Cause Analysis for significant incidents.
- Validate fixes before closing incidents.
- Document lessons learned.
- Coordinate changes through change management.
- Maintain accurate network documentation.
- Regularly train engineers on troubleshooting methodologies.

---

# Key Takeaways

- Network troubleshooting is a structured process, not guesswork.
- Root Cause Analysis prevents recurring incidents.
- The OSI and TCP/IP models provide systematic troubleshooting frameworks.
- Clearly defining the scope reduces investigation time.
- Fault domain isolation improves troubleshooting efficiency.
- Documentation and post-incident reviews strengthen long-term operational resilience.

---

# Part 2 — Routing, Switching, VLAN, DHCP, DNS, Wireless, Firewall, VPN, Cloud, and Enterprise Connectivity Troubleshooting

---

# Introduction

After identifying the affected OSI or TCP/IP layer, engineers must troubleshoot the individual network technologies responsible for connectivity.

Enterprise connectivity depends on many interconnected services:

- Routing
- Switching
- VLANs
- DHCP
- DNS
- Firewalls
- VPNs
- Wireless Networks
- Load Balancers
- Cloud Networking
- SD-WAN

A failure in any of these services can affect thousands of users.

---

# Enterprise Connectivity Troubleshooting Workflow

```
User Reports Issue

↓

Identify Affected Service

↓

Verify Physical Connectivity

↓

Verify Layer 2

↓

Verify Layer 3

↓

Verify Security Controls

↓

Verify Application

↓

Validate Resolution
```

This layered workflow reduces unnecessary troubleshooting.

---

# Routing Troubleshooting

Routing determines how packets travel between different networks.

Common routing issues include:

- Missing routes
- Incorrect static routes
- Dynamic routing failures
- Routing loops
- Route flapping
- Asymmetric routing
- Incorrect default gateway

---

# Routing Verification

Verify:

- Routing table
- Default route
- Dynamic routing neighbors
- Administrative distance
- Route metrics
- Network advertisements

```
Client

↓

Gateway

↓

Router

↓

Core

↓

Destination
```

Each hop should have a valid route toward the destination.

---

# Common Routing Symptoms

| Symptom | Possible Cause |
|----------|----------------|
| Destination unreachable | Missing route |
| High latency | Suboptimal routing |
| Intermittent connectivity | Route flapping |
| One-way traffic | Asymmetric routing |
| Complete outage | Gateway failure |

---

# Static Route Troubleshooting

Verify:

- Destination network
- Next-hop address
- Interface status
- Route priority

Example workflow:

```
Static Route

↓

Correct Network?

↓

Correct Next Hop?

↓

Reachable?

↓

Traffic Forwarded
```

---

# Dynamic Routing Troubleshooting

Review:

- Neighbor relationships
- Authentication
- Network advertisements
- Route convergence
- Timer configuration

Failures often occur because neighboring routers cannot establish adjacency.

---

# Switching Troubleshooting

Switches forward Ethernet frames within a local network.

Common switching problems include:

- VLAN misconfiguration
- MAC address issues
- STP failures
- Port security
- Interface errors
- Duplex mismatch
- Speed mismatch

---

# Switch Verification

Review:

- Interface status
- VLAN assignment
- Trunk configuration
- MAC address table
- Port errors

```
Host

↓

Access Switch

↓

Distribution

↓

Core
```

---

# MAC Address Table Verification

Switches learn MAC addresses dynamically.

Verify:

- MAC learning
- Incorrect entries
- Aging timers
- Duplicate MAC addresses

Failure to learn MAC addresses often indicates Layer 2 issues.

---

# VLAN Troubleshooting

Common VLAN issues:

- Wrong VLAN assignment
- Missing VLAN
- Incorrect trunk
- Native VLAN mismatch
- VLAN pruning errors

Symptoms:

- Devices cannot communicate
- Broadcast isolation failures
- Intermittent connectivity

---

# VLAN Validation

Verify:

- VLAN exists
- Access ports
- Trunk ports
- Allowed VLAN list
- Native VLAN

```
Access Port

↓

Correct VLAN?

↓

Switch Trunk

↓

Destination VLAN
```

---

# Spanning Tree Troubleshooting

Review:

- Root bridge
- Blocked ports
- Port roles
- Port states
- Topology changes

Frequent topology changes often indicate loops or unstable links.

---

# DHCP Troubleshooting

DHCP automatically assigns network configuration.

Common problems include:

- No IP address
- Incorrect subnet
- Gateway missing
- DHCP exhaustion
- Rogue DHCP server

---

# DHCP Process Review

```
Client

↓

Discover

↓

Offer

↓

Request

↓

Acknowledge
```

Failure at any stage prevents successful IP assignment.

---

# DHCP Investigation

Verify:

- DHCP server status
- Scope availability
- Lease duration
- Relay agents
- Network connectivity

---

# DNS Troubleshooting

DNS translates names into IP addresses.

Common DNS issues include:

- Missing records
- Incorrect records
- Resolver failures
- Slow responses
- Zone replication failures
- Cache corruption

---

# DNS Verification

Check:

- Resolver configuration
- Forward lookup
- Reverse lookup
- Response time
- DNS server availability

```
Client

↓

DNS Query

↓

Resolver

↓

Authoritative Server

↓

IP Address
```

---

# DNS Symptoms

| Symptom | Possible Cause |
|----------|----------------|
| Website unavailable | DNS resolution failure |
| Slow application | Slow DNS response |
| Wrong destination | Incorrect DNS record |
| Intermittent access | Replication issue |

---

# Wireless Troubleshooting

Wireless issues often involve multiple factors.

Common causes:

- Weak signal
- Interference
- Channel congestion
- Authentication failures
- Roaming issues
- Controller failures

---

# Wireless Investigation

Review:

- Signal strength
- Channel utilization
- Client count
- Authentication logs
- Access Point health

```
Client

↓

Access Point

↓

Wireless Controller

↓

Network
```

---

# Firewall Troubleshooting

Firewalls enforce security policies.

Common issues:

- Blocked traffic
- Incorrect rules
- NAT errors
- Zone configuration
- Logging disabled

---

# Firewall Validation

Verify:

- Rule order
- Source IP
- Destination IP
- Ports
- Protocol
- NAT
- Security zones

```
Traffic

↓

Firewall

↓

Allowed?

↓

Yes → Forward

No → Drop
```

---

# VPN Troubleshooting

VPNs provide secure remote connectivity.

Common problems include:

- Authentication failures
- Tunnel instability
- Encryption mismatch
- Certificate expiration
- Routing issues
- MTU problems

---

# VPN Verification

Review:

- Tunnel status
- Phase 1 negotiation
- Phase 2 negotiation
- Authentication
- Encryption
- Routing

---

# Load Balancer Troubleshooting

Common issues:

- Unhealthy backend servers
- Health check failures
- SSL certificate problems
- Session persistence issues
- Incorrect routing rules

---

# Load Balancer Workflow

```
Client

↓

Load Balancer

↓

Health Check

↓

Healthy Server

↓

Response
```

---

# Cloud Connectivity Troubleshooting

Cloud environments introduce additional networking components.

Verify:

- Security Groups
- Network ACLs
- Route Tables
- Internet Gateway
- NAT Gateway
- VPN Gateway
- Cloud Firewall
- Private Connectivity

---

# Cloud Network Validation

```
Virtual Machine

↓

Subnet

↓

Route Table

↓

Security Group

↓

Gateway

↓

Internet
```

Each component must permit the required traffic.

---

# Hybrid Network Troubleshooting

Hybrid networks connect on-premises infrastructure to cloud services.

Investigate:

- VPN status
- Direct Connect / ExpressRoute
- BGP sessions
- Route advertisements
- DNS
- Identity services

---

# SD-WAN Troubleshooting

Common issues include:

- Path selection errors
- Overlay tunnel failures
- Policy misconfiguration
- Link degradation
- Controller communication failures

Monitor:

- Path quality
- Link latency
- Packet loss
- Jitter
- Tunnel health

---

# Connectivity Testing Tools

Common tools include:

| Tool | Purpose |
|------|----------|
| Ping | Connectivity |
| Traceroute | Path analysis |
| Nslookup/Dig | DNS verification |
| Tcpdump | Packet capture |
| Wireshark | Packet analysis |
| Netstat | Active connections |
| SNMP | Device metrics |
| NetFlow | Traffic analysis |

---

# Linux Verification Commands

Interface Status

```bash
ip addr
```

---

Routing Table

```bash
ip route
```

---

DNS Lookup

```bash
dig example.com
```

---

Connectivity Test

```bash
ping
```

---

Network Path

```bash
traceroute
```

---

Packet Capture

```bash
tcpdump -i eth0
```

---

Socket Information

```bash
ss -tulnp
```

---

# Windows Verification Commands

IP Configuration

```text
ipconfig /all
```

---

DNS Lookup

```text
nslookup
```

---

Connectivity

```text
ping
```

---

Trace Route

```text
tracert
```

---

Routing Table

```text
route print
```

---

ARP Cache

```text
arp -a
```

---

Network Connections

```text
netstat -ano
```

---

# Business Impact

Efficient connectivity troubleshooting enables organizations to:

- Reduce downtime
- Restore user productivity
- Prevent revenue loss
- Maintain SLA compliance
- Improve customer satisfaction
- Strengthen infrastructure resilience

---

# Enterprise Best Practices

Organizations should:

- Validate each network layer before moving to the next.
- Compare current behavior against historical baselines.
- Review recent configuration changes before implementing new ones.
- Use centralized monitoring and logging platforms.
- Test changes in staging environments when possible.
- Maintain accurate network diagrams and documentation.
- Verify cloud and on-premises configurations together in hybrid environments.
- Record troubleshooting steps for future reference.

---

# Key Takeaways

- Routing and switching form the foundation of enterprise connectivity.
- DHCP and DNS issues frequently appear as broader network outages.
- Firewalls and VPNs should always be validated during connectivity investigations.
- Cloud networking introduces additional security and routing components.
- Structured troubleshooting reduces Mean Time to Repair (MTTR).
- Combining monitoring data with systematic verification improves troubleshooting accuracy.

---

