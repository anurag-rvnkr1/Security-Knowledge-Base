# 09 - Address Resolution Protocol (ARP)

# Part 1 — ARP Fundamentals, MAC Resolution, ARP Cache, Gratuitous ARP, Proxy ARP, and Enterprise Operations

---

# Overview

Communication on an Ethernet network requires **both Layer 2 (MAC)** and **Layer 3 (IP)** addressing.

When a device wants to communicate with another device on the same network, it usually knows the **destination IP address**, but Ethernet frames cannot be delivered using an IP address alone.

Instead, the sender must determine the **destination MAC address**.

This mapping between an IPv4 address and a MAC address is performed by the **Address Resolution Protocol (ARP)**.

ARP is one of the most fundamental protocols in IPv4 networking and is used by:

- Every workstation
- Servers
- Switches
- Routers
- Firewalls
- Wireless devices
- Virtual machines
- Cloud workloads

Understanding ARP is critical for:

- Network Engineers
- Cybersecurity Engineers
- SOC Analysts
- Cloud Engineers
- Incident Responders
- Penetration Testers

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain why ARP is required.
- Describe how ARP resolves MAC addresses.
- Understand ARP Request and Reply messages.
- Explain ARP cache operation.
- Differentiate Dynamic and Static ARP entries.
- Understand Gratuitous ARP.
- Explain Proxy ARP.
- Analyze ARP traffic using Wireshark.
- Troubleshoot enterprise ARP issues.

---

# Why ARP Exists

IP addresses identify devices logically.

Example:

```
PC A

IP:
192.168.10.15
```

Ethernet, however, delivers frames using MAC addresses.

Example:

```
MAC

00:11:22:33:44:55
```

Before sending a frame, the sender must know:

```
Destination IP

↓

Destination MAC
```

ARP performs this translation.

---

# IP Address vs MAC Address

| IP Address | MAC Address |
|------------|-------------|
| Layer 3 | Layer 2 |
| Logical | Physical (hardware) |
| Can change | Usually fixed for an interface (though it can be administratively changed) |
| Used for routing | Used for local delivery |

---

# What is ARP?

**Address Resolution Protocol (ARP)** maps an IPv4 address to a MAC address within the same Layer 2 broadcast domain.

Example:

```
192.168.10.20

↓

00:50:56:AA:12:45
```

Once the MAC address is known, Ethernet communication can begin.

---

# When ARP is Used

ARP is required whenever a device needs to send an IPv4 packet over an Ethernet-like Layer 2 network and does not already know the destination MAC address.

Typical scenarios:

- PC to PC
- PC to Printer
- PC to Server
- PC to Default Gateway
- Server to Firewall

If the destination is on another subnet, the host resolves the **default gateway's MAC address**, not the remote host's MAC address.

---

# Same Network Communication

Example:

```
PC A

192.168.1.10

↓

Switch

↓

PC B

192.168.1.20
```

Both hosts belong to:

```
192.168.1.0/24
```

PC A performs ARP to discover PC B's MAC address.

---

# Different Network Communication

Example:

```
PC A

↓

Switch

↓

Router

↓

Server
```

PC A does **not** ARP for the remote server.

Instead:

```
PC A

↓

ARP

↓

Default Gateway
```

The router then performs ARP on the destination network if necessary.

---

# ARP Resolution Process

Step-by-step:

```
Need Destination MAC

↓

Check ARP Cache

↓

Entry Found?

↓

Yes → Send Frame

↓

No

↓

Broadcast ARP Request

↓

Receive ARP Reply

↓

Update Cache

↓

Send Frame
```

---

# ARP Request

An ARP Request is a **broadcast** frame.

Destination MAC:

```
FF:FF:FF:FF:FF:FF
```

Example:

```
Who has

192.168.10.20

?

Tell

192.168.10.15
```

Every device on the VLAN receives the request.

---

# ARP Reply

Only the device owning the requested IP responds.

Example:

```
192.168.10.20

↓

My MAC is

00:50:56:AA:12:45
```

The reply is normally **unicast** back to the requester.

---

# Complete ARP Workflow

```
PC A

Needs MAC

↓

Broadcast ARP Request

↓

Switch Floods Request

↓

PC B Receives Request

↓

PC B Sends ARP Reply

↓

Switch Forwards Reply

↓

PC A Updates Cache

↓

Communication Begins
```

---

# ARP Cache

To avoid repeated broadcasts, operating systems store learned mappings in an **ARP cache**.

Example:

| IP Address | MAC Address |
|------------|-------------|
| 192.168.10.1 | 00:11:22:33:44:55 |
| 192.168.10.20 | 00:AA:BB:CC:DD:EE |

Future communication uses cached information until entries expire or are refreshed.

---

# Dynamic ARP Entries

Dynamic entries are:

- Learned automatically
- Cached temporarily
- Removed after aging or inactivity
- Refreshed when needed

This is the default behavior on most operating systems.

---

# Static ARP Entries

Static entries are manually configured.

Advantages:

- Predictable
- Not overwritten by normal ARP learning
- Useful for specialized environments

Disadvantages:

- Manual maintenance
- Limited scalability
- Administrative overhead

---

# Gratuitous ARP

A **Gratuitous ARP** is an ARP message sent for the sender's own IP address.

Example:

```
Host

↓

Announces

↓

"I am 192.168.10.20"
```

Common purposes:

- Detect duplicate IP addresses
- Update neighboring ARP caches
- Notify devices after failover events
- Support High Availability protocols

---

# Example — High Availability

Consider:

```
HSRP

↓

Active Router Fails

↓

Standby Router Becomes Active

↓

Gratuitous ARP

↓

Hosts Update Gateway MAC
```

This helps devices quickly learn the MAC address associated with the virtual gateway.

---

# Proxy ARP

With **Proxy ARP**, a router answers an ARP Request on behalf of another device.

Example:

```
Host

↓

Who has

10.10.10.5

?

↓

Router Responds

↓

"My MAC"
```

The router forwards the traffic toward the actual destination.

Proxy ARP is less common in modern enterprise designs because proper routing and subnetting are generally preferred.

---

# ARP Packet Structure

An ARP packet contains fields such as:

- Hardware Type
- Protocol Type
- Hardware Address Length
- Protocol Address Length
- Operation (Request or Reply)
- Sender MAC Address
- Sender IP Address
- Target MAC Address
- Target IP Address

Understanding these fields helps during packet analysis and troubleshooting.

---

# Broadcast Domain Impact

ARP Requests are broadcasts.

Example:

```
VLAN 10

↓

ARP Request

↓

All Devices in VLAN 10
```

Routers do not normally forward ARP broadcasts between broadcast domains.

---

# Enterprise ARP Example

```
Employee Laptop

↓

Access Switch

↓

Core Switch

↓

Default Gateway

↓

Application Server
```

ARP occurs only where Layer 2 resolution is required. Once traffic crosses a router, ARP resolution is performed independently on each Layer 2 segment.

---

# Common ARP Problems

| Problem | Possible Cause |
|----------|----------------|
| Cannot reach local device | Missing or incorrect ARP entry |
| Intermittent connectivity | Duplicate IP address |
| High ARP traffic | Broadcast-heavy network or misconfiguration |
| Incorrect MAC mapping | ARP spoofing or stale cache |
| Slow first connection | Initial ARP resolution |

---

# Business Impact

Reliable ARP operation supports:

- Stable LAN communication
- Efficient IPv4 connectivity
- High Availability failovers
- Consistent application access
- Reduced troubleshooting time

Even though ARP is simple, failures can disrupt business-critical services.

---

# Key Takeaways

- ARP maps **IPv4 addresses** to **MAC addresses** within a local broadcast domain.
- ARP Requests are **broadcast**, while ARP Replies are typically **unicast**.
- Hosts maintain an **ARP cache** to reduce unnecessary broadcasts.
- **Gratuitous ARP** is commonly used for duplicate address detection and high-availability updates.
- **Proxy ARP** allows a router to respond on behalf of another device in specific scenarios.
- ARP operates only within a Layer 2 broadcast domain and is not routed across networks.

# 09 - Address Resolution Protocol (ARP)

# Part 2 — ARP Cache, ARP Spoofing, ARP Poisoning, Man-in-the-Middle (MITM), Dynamic ARP Inspection (DAI), and Enterprise Security

---

# Overview

Although ARP is a simple protocol, it was designed for trusted local networks and **does not provide authentication**.

This means a device generally accepts ARP replies without verifying whether the sender is legitimate.

Attackers can exploit this behavior to:

- Redirect traffic
- Intercept communications
- Launch Man-in-the-Middle (MITM) attacks
- Cause denial-of-service conditions
- Steal credentials
- Capture sensitive information

For this reason, ARP security is a critical topic for enterprise networking and cybersecurity.

---

# ARP Cache Review

Every operating system maintains an **ARP cache**.

Example:

| IP Address | MAC Address | Type |
|------------|-------------|------|
| 192.168.10.1 | 00:11:22:33:44:55 | Dynamic |
| 192.168.10.20 | 00:AA:BB:CC:DD:EE | Dynamic |
| 192.168.10.50 | 00:99:88:77:66:55 | Static |

Instead of broadcasting every time, the host first checks this table.

---

# ARP Cache Lifecycle

```
Need MAC Address

↓

Check Cache

↓

Entry Exists?

↓

Yes

↓

Use Cached Entry

──────────────

No

↓

Send ARP Request

↓

Receive Reply

↓

Store Entry

↓

Use Entry

↓

Timer Expires

↓

Entry Removed
```

This process minimizes unnecessary broadcast traffic.

---

# Cache Aging

Dynamic ARP entries are temporary.

Typical lifecycle:

```
Learn Entry

↓

Store

↓

Use

↓

Idle

↓

Age Out

↓

Remove
```

The exact timeout depends on the operating system and device configuration.

---

# Why ARP is Vulnerable

ARP was designed before modern security threats became common.

Key limitations include:

- No authentication
- No integrity protection
- No encryption
- Trust-based design

As a result, hosts generally accept unsolicited ARP replies and update their ARP cache.

---

# What is ARP Spoofing?

**ARP Spoofing** is an attack in which an attacker sends forged ARP replies to associate their MAC address with another device's IP address.

Example:

```
Gateway IP

↓

Attacker MAC
```

Victims update their ARP cache with incorrect information.

---

# What is ARP Poisoning?

**ARP Poisoning** is the result of successful ARP spoofing.

The victim's ARP cache contains false IP-to-MAC mappings.

Example:

| IP Address | Correct MAC | Poisoned MAC |
|------------|-------------|--------------|
| 192.168.10.1 | 00:11:22:33:44:55 | AA:AA:AA:AA:AA:AA |

Traffic intended for the gateway is now sent to the attacker.

---

# ARP Spoofing Attack Workflow

```
Victim

↓

Needs Gateway MAC

↓

Attacker Sends Fake ARP Reply

↓

Victim Updates Cache

↓

Traffic Redirected

↓

Attacker

↓

Gateway
```

The attacker positions themselves between the victim and the legitimate gateway.

---

# Man-in-the-Middle (MITM)

One of the most common outcomes of ARP spoofing is a **Man-in-the-Middle (MITM)** attack.

```
Victim

↓

Attacker

↓

Gateway

↓

Internet
```

The attacker can:

- Inspect packets
- Modify traffic
- Forward packets
- Drop packets
- Record sensitive information

---

# Two-Way ARP Poisoning

To remain invisible, an attacker often poisons both devices.

```
Victim

↓

Gateway = Attacker MAC

──────────────

Gateway

↓

Victim = Attacker MAC
```

Now all traffic flows through the attacker.

---

# Potential Attack Consequences

Successful ARP poisoning may lead to:

- Credential theft
- Session hijacking
- Packet manipulation
- Data interception
- DNS manipulation
- Service disruption
- Denial of Service (DoS)

Encrypted protocols such as HTTPS reduce the risk of content disclosure but do not eliminate the networking impact of ARP manipulation.

---

# Example Attack Scenario

```
Employee Laptop

↓

Access Switch

↓

Attacker Laptop

↓

Default Gateway

↓

Corporate Server
```

The attacker impersonates the default gateway.

The victim unknowingly forwards all traffic through the attacker's system.

---

# Detecting ARP Spoofing

Indicators include:

- Multiple IP addresses mapped to the same MAC address.
- Frequent unsolicited ARP replies.
- Sudden gateway MAC address changes.
- Unexpected connectivity issues.
- Duplicate MAC notifications.
- Increased ARP traffic.

Monitoring tools can help identify these anomalies.

---

# Enterprise Detection Methods

Organizations commonly detect suspicious ARP activity using:

- Network monitoring platforms
- SIEM solutions
- IDS/IPS platforms
- Endpoint detection tools
- Packet capture analysis
- Switch security features

Repeated ARP changes should be investigated promptly.

---

# Dynamic ARP Inspection (DAI)

**Dynamic ARP Inspection (DAI)** is a Layer 2 security feature available on many managed switches.

Purpose:

- Validate ARP packets.
- Block forged ARP messages.
- Prevent ARP spoofing.

---

# How DAI Works

Simplified process:

```
ARP Packet

↓

Switch Receives Packet

↓

Validate Against DHCP Snooping Database

↓

Valid?

↓

Yes

↓

Forward

──────────────

No

↓

Drop Packet
```

Only validated ARP messages are forwarded.

---

# DHCP Snooping Review

DAI depends on **DHCP Snooping** in many enterprise deployments.

DHCP Snooping builds a trusted binding table containing:

- MAC Address
- IP Address
- VLAN
- Switch Port

Example:

| MAC | IP | VLAN | Port |
|------|----|------|------|
| 00:11:22:33:44:55 | 192.168.10.20 | 10 | Gi1/0/5 |

DAI compares incoming ARP packets against this trusted information.

---

# Trusted vs Untrusted Ports

Enterprise switches classify interfaces as:

```
Trusted

↓

Uplink

↓

DHCP Server

──────────────

Untrusted

↓

User Devices
```

ARP validation is generally performed on untrusted access ports.

---

# Static Hosts and DAI

Some environments contain devices using static IP addresses.

Since these hosts may not appear in the DHCP Snooping database, administrators may need to create static bindings or use supported configuration methods to ensure legitimate traffic is not blocked.

---

# Rate Limiting

Switches can also limit ARP packet rates.

Benefits:

- Reduces flooding attacks.
- Helps mitigate denial-of-service attempts.
- Protects switch CPU resources.

---

# ARP Inspection Workflow

```
Client Sends ARP

↓

Access Switch

↓

DAI Validation

↓

Binding Matches?

↓

Yes

↓

Forward

──────────────

No

↓

Drop

↓

Log Event
```

---

# Enterprise Security Controls

Recommended controls include:

- Dynamic ARP Inspection
- DHCP Snooping
- Port Security
- VLAN segmentation
- 802.1X Network Access Control
- Secure switch management
- Continuous monitoring
- SIEM correlation

These controls work together to reduce the risk of Layer 2 attacks.

---

# Wireshark Analysis

Useful display filter:

```text
arp
```

Typical observations:

### ARP Request

```
Who has 192.168.10.1?

Tell 192.168.10.20
```

### ARP Reply

```
192.168.10.1

is at

00:11:22:33:44:55
```

Suspicious indicators include:

- Numerous unsolicited ARP replies.
- Frequent MAC address changes for the same IP.
- Excessive ARP traffic.

---

# Linux Verification

Display ARP/neighbor table:

```bash
ip neigh
```

Legacy command (if available):

```bash
arp -n
```

---

# Windows Verification

Display ARP cache:

```cmd
arp -a
```

Clear ARP cache (administrative privileges may be required):

```cmd
arp -d *
```

---

# Cisco IOS Verification

Display ARP table:

```text
show ip arp
```

Display DHCP Snooping bindings:

```text
show ip dhcp snooping binding
```

Display Dynamic ARP Inspection status:

```text
show ip arp inspection
```

Display interface trust configuration (platform dependent):

```text
show ip arp inspection interfaces
```

---

# Common ARP Problems

| Problem | Possible Cause |
|----------|----------------|
| Wrong gateway MAC | ARP spoofing |
| Duplicate IP alerts | IP conflict |
| Frequent ARP broadcasts | Cache expiration or unstable network |
| DAI drops legitimate traffic | Missing DHCP Snooping binding or incorrect configuration |
| Intermittent connectivity | Poisoned ARP cache |

---

# Enterprise Example

```
Employee

↓

Access Switch

↓

DAI Enabled

↓

Core Switch

↓

Gateway
```

Result:

- Forged ARP packets are discarded.
- Legitimate ARP traffic is forwarded.
- Network integrity is improved.

---

# Business Impact

Securing ARP helps organizations:

- Protect sensitive communications.
- Reduce the risk of MITM attacks.
- Improve network stability.
- Prevent unauthorized traffic interception.
- Meet enterprise security and compliance objectives.

---

# Key Takeaways

- ARP lacks built-in authentication, making it susceptible to spoofing.
- **ARP Spoofing** injects false ARP replies; **ARP Poisoning** is the resulting corruption of the ARP cache.
- Successful poisoning can enable **Man-in-the-Middle (MITM)** attacks and traffic interception.
- **Dynamic ARP Inspection (DAI)** validates ARP messages and helps prevent forged ARP traffic.
- **DHCP Snooping** provides trusted IP-to-MAC bindings that DAI uses for validation.
- Continuous monitoring, segmentation, and Layer 2 security features are essential for defending enterprise networks against ARP-based attacks.


