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

# 08 - Switching

# Part 2 — VLANs, IEEE 802.1Q Trunking, Inter-VLAN Routing, Voice VLANs, and Enterprise Network Segmentation

---

# Overview

A modern enterprise rarely operates as a single flat Layer 2 network.

Instead, organizations divide their networks into multiple **Virtual Local Area Networks (VLANs)** to improve:

- Security
- Performance
- Scalability
- Broadcast control
- Department isolation
- Compliance

Without VLANs, every connected device belongs to the same broadcast domain, making networks inefficient and difficult to secure.

---

# What is a VLAN?

A **Virtual Local Area Network (VLAN)** is a logical Layer 2 network created on a switch.

Instead of separating devices using different physical switches, VLANs allow multiple isolated networks to exist on the same switching infrastructure.

Example:

```
                    Switch
          ┌───────────────────────┐
          │                       │
 HR PCs   │ VLAN 10               │
 Finance  │ VLAN 20               │
 Servers  │ VLAN 30               │
 Guests   │ VLAN 40               │
          └───────────────────────┘
```

Each VLAN acts as a separate broadcast domain.

---

# Why VLANs are Needed

Without VLANs:

```
Entire Office

↓

Single Broadcast Domain
```

Problems:

- Excessive broadcasts
- Limited security
- Difficult policy enforcement
- Poor scalability

With VLANs:

```
HR

↓

VLAN 10

──────────────

Finance

↓

VLAN 20

──────────────

Servers

↓

VLAN 30

──────────────

Guest Wi-Fi

↓

VLAN 40
```

Benefits:

- Reduced broadcasts
- Department isolation
- Easier access control
- Improved security

---

# Broadcast Domains

Remember:

```
One VLAN

↓

One Broadcast Domain
```

Example:

```
VLAN 10

PC1

PC2

PC3

──────────────

VLAN 20

PC4

PC5

PC6
```

Broadcasts from VLAN 10 are **not** forwarded into VLAN 20.

---

# Collision Domains vs Broadcast Domains

| Feature | Collision Domain | Broadcast Domain |
|----------|-----------------|------------------|
| Controlled By | Switch Port | VLAN |
| Traffic Type | Frame collisions | Broadcast frames |
| Modern Switch | One per Port | One per VLAN |

---

# VLAN Identification

Each VLAN has a unique **VLAN ID**.

Range:

```
1–4094
```

Common examples:

| VLAN | Purpose |
|------|---------|
| 1 | Default VLAN |
| 10 | HR |
| 20 | Finance |
| 30 | IT |
| 40 | Servers |
| 50 | Guest Wi-Fi |
| 99 | Management (common convention) |

> VLAN 1 exists by default on many switches, but best practice is to avoid using it for user traffic.

---

# Access Ports

An **access port** belongs to a single VLAN.

Example:

```
PC

↓

Switch Port

↓

VLAN 10
```

Characteristics:

- Carries one VLAN
- Frames are untagged
- Typically used for:

  - Workstations
  - Printers
  - IP phones (with voice VLAN support)
  - Servers (single network)

---

# Trunk Ports

A **trunk port** carries traffic for multiple VLANs.

Example:

```
Switch A

↓

Trunk Link

↓

Switch B
```

Traffic for VLANs:

```
10

20

30

40
```

All travel over the same physical connection.

---

# IEEE 802.1Q Trunking

The most widely used VLAN trunking standard is:

```
IEEE 802.1Q
```

802.1Q inserts a VLAN tag into Ethernet frames.

Simplified frame:

```
Destination MAC

↓

Source MAC

↓

802.1Q Tag

↓

EtherType

↓

Payload

↓

FCS
```

The VLAN tag identifies which VLAN the frame belongs to while it traverses a trunk link.

---

# VLAN Tag Fields

The 802.1Q tag contains:

- VLAN Identifier (VID)
- Priority Code Point (PCP)
- Drop Eligible Indicator (DEI)

For most networking tasks, the VLAN Identifier is the primary field of interest.

---

# Native VLAN

On an 802.1Q trunk, one VLAN is designated as the **native VLAN**.

Characteristics:

- Frames belonging to the native VLAN are sent **without** an 802.1Q tag (on traditional configurations).
- Both ends of the trunk must agree on the native VLAN.
- A native VLAN mismatch can cause connectivity issues and increase security risk.

Best practices:

- Use an unused VLAN as the native VLAN.
- Do not use VLAN 1 as the native VLAN for production environments.
- Restrict access to trunk ports.

---

# VLAN Tagging Example

```
Switch A

↓

Frame

↓

VLAN 20 Tag Added

↓

Trunk

↓

Switch B

↓

Tag Removed

↓

Destination Device
```

End devices connected to access ports typically receive untagged frames.

---

# Inter-VLAN Communication

Devices in different VLANs cannot communicate directly because each VLAN is a separate Layer 2 broadcast domain.

Example:

```
PC

VLAN 10

↓

×

↓

Server

VLAN 30
```

A Layer 3 device is required to route traffic between VLANs.

---

# Inter-VLAN Routing

Example:

```
VLAN 10

↓

Layer 3 Switch / Router

↓

VLAN 20
```

Process:

1. The source host sends traffic to its default gateway.
2. The Layer 3 device routes the packet.
3. The packet is forwarded into the destination VLAN.

---

# Router-on-a-Stick

A common inter-VLAN routing design for smaller networks uses a single router interface configured with multiple subinterfaces.

```
           Router
              │
        802.1Q Trunk
              │
          Layer 2 Switch
      ┌──────┼──────┐
      │      │      │
   VLAN10 VLAN20 VLAN30
```

Each router subinterface corresponds to a specific VLAN.

Advantages:

- Cost-effective
- Simple for small deployments

Limitations:

- Single physical uplink
- Lower scalability compared to Layer 3 switching

---

# Layer 3 Switch

Modern enterprise networks often use **Layer 3 switches** for inter-VLAN routing.

```
         Layer 3 Switch
      ┌────────┼────────┐
      │        │        │
   VLAN10   VLAN20   VLAN30
```

Advantages:

- Hardware-based routing
- Low latency
- High throughput
- Better scalability
- Simplified campus design

---

# Voice VLAN

IP phones commonly use a dedicated **Voice VLAN**.

Example:

```
IP Phone

↓

Voice VLAN 100

↓

PC

↓

Data VLAN 10
```

Benefits:

- Traffic separation
- Simplified QoS
- Better security
- Easier troubleshooting

Voice traffic can be prioritized independently of user data.

---

# Management VLAN

Network devices often use a dedicated **Management VLAN** for administrative access.

Example:

```
Management VLAN

↓

Switches

↓

Routers

↓

Wireless Controllers
```

Benefits:

- Isolated management traffic
- Improved security
- Simplified monitoring
- Centralized administration

Access to the management VLAN should be tightly controlled.

---

# VLAN Planning

Example enterprise allocation:

| VLAN | Department |
|------|------------|
| 10 | HR |
| 20 | Finance |
| 30 | IT |
| 40 | Servers |
| 50 | Wireless Users |
| 60 | Guest Wi-Fi |
| 99 | Management |
| 100 | Voice |

Planning should leave room for future growth and maintain consistent numbering conventions across sites.

---

# VLAN Best Practices

- Separate departments into dedicated VLANs.
- Isolate guest users from internal resources.
- Use dedicated management and voice VLANs.
- Avoid using VLAN 1 for production traffic.
- Disable unused switch ports.
- Limit which VLANs are allowed on trunk links.
- Document VLAN assignments and purposes.
- Align VLAN design with security policies and firewall rules.

---

# Common VLAN Problems

| Problem | Possible Cause |
|----------|----------------|
| Devices cannot communicate | Wrong VLAN assignment |
| Trunk not working | 802.1Q mismatch |
| Native VLAN mismatch | Incorrect trunk configuration |
| Missing VLAN | VLAN not created on the switch |
| Inter-VLAN routing failure | Incorrect gateway or Layer 3 configuration |
| Voice issues | Voice VLAN or QoS misconfiguration |

---

# Enterprise Example

```
                    Core Layer
                         │
                 Layer 3 Switch
        ┌────────┼────────┼────────┐
        │        │        │        │
    VLAN10   VLAN20   VLAN30   VLAN40
       │         │         │         │
      HR     Finance      IT     Servers
```

This design:

- Reduces broadcast traffic
- Improves security
- Simplifies routing
- Supports scalable network growth

---

# Practical Lab 1 — Create VLANs

Objective:

Create the following VLANs on a managed switch:

| VLAN | Name |
|------|------|
| 10 | HR |
| 20 | Finance |
| 30 | IT |
| 40 | Servers |

Assign access ports to the appropriate VLANs and verify connectivity within each VLAN.

---

# Practical Lab 2 — Configure a Trunk

Tasks:

1. Connect two switches.
2. Configure the link as an 802.1Q trunk.
3. Allow VLANs 10, 20, 30, and 40.
4. Verify that traffic from each VLAN traverses the trunk correctly.

---

# Practical Lab 3 — Inter-VLAN Routing

Using a Layer 3 switch or Router-on-a-Stick:

1. Configure VLAN interfaces (SVIs) or router subinterfaces.
2. Assign default gateways.
3. Test communication between VLAN 10 and VLAN 20.
4. Verify routing with `ping` and `traceroute`.

---

# Key Takeaways

- A **VLAN** is a logical Layer 2 network that creates a separate broadcast domain.
- **Access ports** carry traffic for a single VLAN, while **trunk ports** carry multiple VLANs.
- **IEEE 802.1Q** is the standard protocol for VLAN tagging across trunk links.
- Devices in different VLANs require **Layer 3 routing** to communicate.
- Dedicated **Voice VLANs** and **Management VLANs** improve security, performance, and operational efficiency.
- Proper VLAN planning and trunk configuration are essential for scalable enterprise networks.

