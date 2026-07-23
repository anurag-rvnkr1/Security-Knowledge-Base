# 08 - Switching

# Part 1 — Layer 2 Switching Fundamentals, Switch Architecture, MAC Addresses, CAM Tables, and Frame Forwarding

---

# Overview

Switching is the foundation of every modern Local Area Network (LAN).

While **routers** connect different Layer 3 networks using IP addresses, **switches** enable efficient communication between devices within the same Layer 2 network using **MAC addresses**.

Every office, enterprise campus, data center, and cloud edge relies on switching technologies to connect:

- Workstations
- Servers
- Printers
- IP Phones
- Wireless Access Points
- IoT Devices

Understanding switching is essential for:

- Network Engineers
- SOC Analysts
- Security Engineers
- Cloud Engineers
- System Administrators
- Penetration Testers

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain Layer 2 switching.
- Differentiate switches, hubs, and routers.
- Understand Ethernet frame forwarding.
- Explain MAC address learning.
- Interpret CAM tables.
- Describe switching methods.
- Understand collision and broadcast domains.
- Recognize enterprise switching architectures.

---

# What is Switching?

**Switching** is the process of forwarding Ethernet frames between devices within the same Layer 2 network based on **MAC addresses**.

Unlike routers, switches do **not** normally make forwarding decisions using IP addresses.

Example:

```
Laptop

↓

Switch

↓

Printer
```

The switch examines the **destination MAC address** and forwards the frame only to the correct port.

---

# Why Switching is Important

Switching provides:

- High-speed LAN communication
- Efficient frame forwarding
- Reduced collisions
- Dedicated bandwidth per port
- Scalability
- Enterprise network segmentation (with VLANs)

Without switches, all devices would share the same communication medium, leading to poor performance.

---

# Hub vs Switch vs Router

| Feature | Hub | Switch | Router |
|----------|-----|--------|--------|
| OSI Layer | Layer 1 | Layer 2 | Layer 3 |
| Address Used | None | MAC Address | IP Address |
| Collision Domains | One | One per Port | One per Interface |
| Broadcast Domains | One | One (per VLAN) | One per Interface |
| Intelligent Forwarding | No | Yes | Yes |

---

# Hub Operation

A hub simply repeats electrical signals.

```
PC A

↓

Hub

↓

PC B

↓

PC C

↓

PC D
```

Every connected device receives every transmission, regardless of the intended destination.

Problems:

- Shared bandwidth
- High collisions
- Low efficiency
- No traffic isolation

Hubs are rarely used in modern enterprise networks.

---

# Switch Operation

Switches learn MAC addresses and forward frames only where needed.

```
PC A

↓

Switch

↓

PC B
```

Only the destination port receives the frame.

Benefits:

- Better performance
- Reduced unnecessary traffic
- Dedicated collision domains
- Improved scalability

---

# Router Operation

Routers connect separate Layer 3 networks.

```
Subnet A

↓

Router

↓

Subnet B
```

Traffic between different IP networks must pass through a router or another Layer 3 device.

---

# Switch Architecture

A simplified enterprise switch consists of:

```
            Ethernet Switch
     ┌──────────────────────────┐
     │          CPU             │
     ├──────────────────────────┤
     │          RAM             │
     ├──────────────────────────┤
     │     Switching ASICs      │
     ├──────────────────────────┤
     │        CAM Table         │
     ├──────────────────────────┤
     │       Interfaces         │
     └──────────────────────────┘
```

---

## CPU

Handles:

- Device management
- STP calculations
- VLAN management
- Control plane functions
- Configuration

---

## RAM

Stores:

- Running configuration
- CAM entries (platform dependent)
- Buffers
- Control plane information

---

## Switching ASICs

Modern enterprise switches use specialized hardware called **Application-Specific Integrated Circuits (ASICs)**.

Benefits:

- Hardware forwarding
- Wire-speed performance
- Low latency
- High throughput

ASICs allow switches to forward millions of frames per second.

---

# Ethernet Frame Review

An Ethernet frame contains:

```
Destination MAC

↓

Source MAC

↓

EtherType

↓

Payload

↓

Frame Check Sequence (FCS)
```

The switch primarily examines the **destination MAC address** to decide where to forward the frame.

---

# MAC Address Review

Every Ethernet network interface has a **48-bit MAC address**.

Example:

```
00:1A:2B:3C:4D:5E
```

Structure:

```
OUI (Vendor)

↓

Device Identifier
```

The first 24 bits identify the manufacturer, and the remaining 24 bits identify the specific interface.

---

# MAC Address Types

## Unicast

Sent to one device.

```
PC A

↓

PC B
```

---

## Broadcast

Sent to all devices within the broadcast domain.

Example address:

```
FF:FF:FF:FF:FF:FF
```

---

## Multicast

Sent to a specific group of interested devices.

Common uses:

- Streaming
- Routing protocols
- Service discovery

---

# What is a CAM Table?

The **Content Addressable Memory (CAM) Table** stores mappings between MAC addresses and switch ports.

Example:

| MAC Address | Port |
|-------------|------|
| 00:11:22:33:44:55 | Gi0/1 |
| 00:AA:BB:CC:DD:EE | Gi0/5 |
| 00:99:88:77:66:55 | Gi0/10 |

The switch uses the CAM table to forward frames efficiently.

---

# MAC Learning Process

When a frame arrives:

```
Receive Frame

↓

Read Source MAC

↓

Store Source MAC

↓

Associate MAC with Incoming Port

↓

Update CAM Table
```

The switch continuously learns the location of connected devices.

---

# Frame Forwarding Process

Once the switch knows the destination MAC:

```
Receive Frame

↓

Read Destination MAC

↓

Search CAM Table

↓

Find Port

↓

Forward Frame
```

Only the destination interface receives the frame.

---

# Unknown Unicast

If the destination MAC is **not** in the CAM table:

```
Unknown Destination

↓

Flood Frame

↓

All Ports

↓

Except Incoming Port
```

When the destination replies, the switch learns its MAC address and updates the CAM table.

---

# Broadcast Forwarding

Broadcast traffic is sent to every port in the same broadcast domain (or VLAN).

Example:

```
Broadcast

↓

Switch

↓

All Ports
```

Typical examples:

- ARP Requests
- DHCP Discover
- Some service discovery protocols

---

# Multicast Forwarding

Basic switches flood multicast traffic similarly to broadcasts.

Enterprise switches often support features such as **IGMP Snooping** to forward multicast traffic only to interested receivers, reducing unnecessary traffic.

---

# CAM Table Aging

Devices may disconnect or move.

To keep entries current, CAM table entries expire after an inactivity timer.

```
Device Disconnects

↓

No Traffic

↓

Timer Expires

↓

Entry Removed
```

The exact aging time is vendor and configuration dependent.

---

# Collision Domains

A **collision domain** is a network segment where simultaneous transmissions can interfere.

Modern switches create:

```
One Collision Domain

↓

Per Port
```

This enables full-duplex communication and eliminates collisions under normal operating conditions.

---

# Broadcast Domains

By default:

```
One Switch

↓

One Broadcast Domain
```

When VLANs are introduced, each VLAN forms its own broadcast domain.

This topic is covered in the next section.

---

# Switching Methods

Enterprise switches use different forwarding methods.

---

## Store-and-Forward

Process:

```
Receive Entire Frame

↓

Verify FCS

↓

Forward Frame
```

Advantages:

- Detects corrupted frames
- High reliability

Most modern enterprise switches use this method.

---

## Cut-Through Switching

Process:

```
Read Destination MAC

↓

Immediately Forward
```

Advantages:

- Very low latency

Disadvantages:

- Corrupted frames may be forwarded because the FCS is not verified before forwarding.

---

## Fragment-Free Switching

This method waits for the first portion of the frame (typically enough to avoid forwarding most collision fragments) before forwarding.

It provides a compromise between latency and error handling.

---

# Enterprise Switching Example

```
                 Core Switch
                      │
        ┌─────────────┼─────────────┐
        │             │             │
 Distribution     Distribution   Distribution
        │             │             │
 Access Layer    Access Layer   Access Layer
```

This hierarchical design:

- Improves scalability
- Simplifies troubleshooting
- Supports redundancy
- Enables policy enforcement

---

# Common Switching Problems

| Problem | Possible Cause |
|----------|----------------|
| Unknown unicast flooding | CAM entry missing or expired |
| Duplicate MAC address | Misconfiguration or spoofing |
| Excessive broadcasts | Broadcast storm |
| CAM table overflow | MAC flooding attack |
| High latency | Interface congestion |
| Interface down | Physical or configuration issue |

---

# Business Impact

Efficient switching provides:

- Reliable LAN communication
- High throughput
- Low latency
- Better user experience
- Simplified network growth
- Strong foundation for VLANs and security controls

---

# Key Takeaways

- Switches operate primarily at **OSI Layer 2** using **MAC addresses**.
- The **CAM table** maps MAC addresses to switch ports for efficient forwarding.
- Switches learn source MAC addresses dynamically and update entries over time.
- Unknown unicast traffic is flooded until the destination is learned.
- Store-and-forward is the most common enterprise switching method due to its reliability.
- Each switch port forms its own collision domain, while broadcast domains are separated using VLANs.

