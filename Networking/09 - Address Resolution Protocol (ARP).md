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