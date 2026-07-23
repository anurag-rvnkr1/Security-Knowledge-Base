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

# 08 - Switching

# Part 3 — Spanning Tree Protocol (STP), RSTP, MSTP, BPDU, Root Bridge Election, and Enterprise Layer 2 Redundancy

---

# Overview

Redundancy is essential in enterprise networks.

Organizations deploy multiple switches and redundant links to improve:

- High Availability (HA)
- Fault tolerance
- Business continuity
- Maintenance flexibility

However, redundant Layer 2 links introduce a serious problem:

> **Switching loops**

Unlike IP packets, traditional Ethernet frames do **not** contain a field equivalent to IPv4's **Time To Live (TTL)**. Without a loop prevention mechanism, frames may circulate indefinitely.

To solve this problem, Ethernet networks use the **Spanning Tree Protocol (STP)**.

---

# Learning Objectives

After completing this section, you should be able to:

- Explain why switching loops occur.
- Understand broadcast storms.
- Describe MAC address table instability.
- Explain STP operation.
- Understand Root Bridge election.
- Identify STP port roles and states.
- Compare STP, RSTP, and MSTP.
- Configure enterprise Layer 2 redundancy.
- Apply Layer 2 protection features.

---

# Why Redundant Links Are Needed

Enterprise networks require redundancy.

Example:

```
          Switch A
         /        \
        /          \
Switch B ---------- Switch C
```

Benefits:

- Link failure protection
- High availability
- Faster maintenance
- Better resilience

Without redundancy, a single cable failure can disconnect an entire part of the network.

---

# The Layer 2 Loop Problem

Consider:

```
       Switch A
      /        \
     /          \
Switch B ------ Switch C
```

A broadcast frame entering this topology may circulate continuously.

Unlike routed packets, Ethernet frames do not normally expire due to a hop count.

Consequences include:

- Broadcast storms
- Duplicate frames
- MAC address instability
- High CPU utilization
- Network outages

---

# Broadcast Storm

A broadcast storm occurs when broadcast frames are replicated repeatedly because of a switching loop.

Example:

```
Broadcast

↓

Switch A

↓

Switch B

↓

Switch C

↓

Back to Switch A

↓

Repeat
```

The amount of traffic increases rapidly, consuming available bandwidth and device resources.

---

# MAC Address Table Instability

Switches learn MAC addresses based on incoming frames.

With a loop:

```
MAC Address

↓

Port 1

↓

Port 2

↓

Port 3

↓

Port 1
```

The switch repeatedly updates the same MAC address to different ports.

This condition is known as **MAC address table instability** (or MAC flapping).

---

# Duplicate Frames

Because loops allow multiple copies of the same frame to circulate, destination devices may receive duplicate frames.

Potential impacts:

- Application errors
- Excessive bandwidth usage
- Unexpected behavior

---

# What is STP?

**Spanning Tree Protocol (STP)** prevents Layer 2 loops by logically blocking redundant links while preserving them as backup paths.

Normal topology:

```
      A
     / \
    /   \
   B-----C
```

Logical topology after STP:

```
      A
     / \
    /   X
   B     C
```

The blocked link is not used for normal forwarding but can become active if another link fails.

---

# IEEE Standards

| Standard | Name |
|----------|------|
| IEEE 802.1D | Spanning Tree Protocol (STP) |
| IEEE 802.1w | Rapid Spanning Tree Protocol (RSTP) |
| IEEE 802.1s | Multiple Spanning Tree Protocol (MSTP) |

---

# STP Goals

- Prevent switching loops
- Eliminate broadcast storms
- Provide redundant paths
- Automatically recover from failures
- Maintain a loop-free Layer 2 topology

---

# Root Bridge

Every STP topology elects one switch as the **Root Bridge**.

The Root Bridge serves as the logical center of the spanning tree.

Example:

```
          Root Bridge
               │
        ┌──────┴──────┐
        │             │
    Switch B      Switch C
```

All path calculations are performed relative to the Root Bridge.

---

# Bridge ID (BID)

STP elects the Root Bridge using the **Bridge ID**.

A Bridge ID consists of:

```
Bridge Priority

↓

MAC Address
```

The switch with the **lowest Bridge ID** becomes the Root Bridge.

---

# Root Bridge Election

Election process:

```
Compare Priorities

↓

Lowest Priority Wins

↓

Tie?

↓

Lowest MAC Address Wins
```

Default bridge priority is commonly:

```
32768
```

Administrators often lower the priority of a core switch so it becomes the preferred Root Bridge.

---

# Root Port

Each **non-root switch** selects one **Root Port**.

The Root Port is the port with the **lowest path cost** to the Root Bridge.

Example:

```
Root Bridge
      │
      │
Switch B

↓

Root Port
```

Each non-root switch has exactly one Root Port.

---

# Designated Port

Every network segment has one **Designated Port**.

Responsibilities:

- Forwards traffic toward the segment
- Sends BPDUs for that segment

The Designated Port is selected based on the lowest path cost to the Root Bridge.

---

# Blocked (Alternate) Port

Ports that would create a Layer 2 loop are placed into a non-forwarding role.

Example:

```
Switch A

↓

Blocked Link

↓

Switch B
```

The blocked link remains available for failover if the active path fails.

---

# STP Port Roles

| Port Role | Purpose |
|-----------|----------|
| Root Port | Best path to the Root Bridge |
| Designated Port | Forwards traffic for a network segment |
| Alternate Port | Backup path (RSTP terminology) |
| Backup Port | Redundant path on the same segment (RSTP terminology) |

Classic STP often refers to blocked ports simply as **non-designated** or **blocked** ports.

---

# STP Port States (IEEE 802.1D)

Ports transition through several states before forwarding traffic.

```
Blocking

↓

Listening

↓

Learning

↓

Forwarding
```

A disabled port is administratively or operationally down and does not participate.

---

## Blocking

Characteristics:

- Receives BPDUs
- Does not forward user traffic
- Prevents loops

---

## Listening

The switch:

- Processes BPDUs
- Determines topology
- Does not learn MAC addresses
- Does not forward frames

---

## Learning

The switch:

- Learns source MAC addresses
- Builds the CAM table
- Still does not forward user traffic

---

## Forwarding

The port:

- Learns MAC addresses
- Forwards frames
- Operates normally

---

# BPDU (Bridge Protocol Data Unit)

STP switches exchange **Bridge Protocol Data Units (BPDUs)**.

BPDUs contain information such as:

- Root Bridge ID
- Sender Bridge ID
- Path Cost
- Timers

These messages allow switches to build and maintain a loop-free topology.

---

# Path Cost

STP selects paths based on **path cost**.

Generally:

- Higher-bandwidth links have lower costs.
- Lower total path cost is preferred.

Example:

| Link Speed | Relative Preference |
|------------|--------------------|
| 10 Gbps | Preferred |
| 1 Gbps | Next |
| 100 Mbps | Less preferred |

---

# STP Convergence

Convergence is the process of recalculating the spanning tree after a topology change.

Classic STP convergence can take tens of seconds, depending on timers.

During convergence:

- Ports change states.
- Forwarding paths are recalculated.
- Previously blocked links may become active.

---

# Rapid Spanning Tree Protocol (RSTP)

**RSTP (IEEE 802.1w)** improves upon classic STP.

Advantages:

- Faster convergence
- Improved recovery after failures
- Simplified port roles and states
- Better performance in enterprise networks

RSTP is widely deployed in modern campus environments.

---

# RSTP Port Roles

RSTP introduces:

- Root Port
- Designated Port
- Alternate Port
- Backup Port

Alternate ports provide an immediately available backup path, reducing failover time.

---

# RSTP Port States

RSTP simplifies the port states:

```
Discarding

↓

Learning

↓

Forwarding
```

The older Blocking, Listening, and Disabled operational behavior is consolidated into the **Discarding** state where appropriate.

---

# Multiple Spanning Tree Protocol (MSTP)

Large enterprise networks often deploy many VLANs.

Running a separate spanning tree instance for every VLAN may become inefficient.

**MSTP (IEEE 802.1s)** allows multiple VLANs to share a single spanning tree instance.

Example:

```
Instance 1

↓

VLAN 10

VLAN 20

────────────

Instance 2

↓

VLAN 30

VLAN 40
```

Benefits:

- Better scalability
- Reduced CPU usage
- Improved resource utilization

---

# Enterprise STP Design

Example:

```
             Core Switch
            (Root Bridge)
             /        \
            /          \
 Distribution      Distribution
      │                 │
 Access Layer      Access Layer
```

Recommended practice:

- Place the Root Bridge in the core layer.
- Place the secondary Root Bridge in a redundant core/distribution device.
- Avoid accidental Root Bridge elections at the access layer.

---

# Common STP Problems

| Problem | Possible Cause |
|----------|----------------|
| Broadcast storm | Switching loop |
| Incorrect Root Bridge | Default priorities |
| Slow convergence | Legacy STP timers |
| Frequent topology changes | Unstable links or devices |
| Unexpected blocked port | Incorrect path cost or bridge priority |

---

# Enterprise Best Practices

- Explicitly configure the Root Bridge.
- Configure a secondary Root Bridge for redundancy.
- Use RSTP or MSTP instead of legacy STP where supported.
- Monitor topology changes.
- Document Layer 2 topology.
- Minimize unnecessary trunk links.
- Design predictable Layer 2 paths.

---

# Key Takeaways

- Redundant Layer 2 links improve availability but can create switching loops.
- **STP** prevents loops by logically blocking redundant paths.
- Every STP topology has one **Root Bridge** selected by the lowest **Bridge ID**.
- **Root Ports** provide the best path to the Root Bridge, while **Designated Ports** forward traffic for each segment.
- **BPDUs** allow switches to exchange topology information.
- **RSTP** provides much faster convergence than classic STP.
- **MSTP** improves scalability by allowing multiple VLANs to share spanning tree instances.

# 08 - Switching

# Part 4 — EtherChannel, Layer 2 Security, Enterprise Hardening, Troubleshooting, Practical Labs, Interview Questions, and Chapter Review

---

# Overview

Enterprise switches are expected to provide much more than basic Layer 2 connectivity.

Modern switching infrastructures must deliver:

- High Availability (HA)
- Redundancy
- Scalability
- High throughput
- Secure access
- Protection against Layer 2 attacks
- Fast convergence
- Simplified management

This section focuses on enterprise switching technologies and security mechanisms commonly deployed in production environments.

---

# EtherChannel

## What is EtherChannel?

**EtherChannel** is a technology that combines multiple physical Ethernet links into a single logical connection.

Instead of forwarding traffic over one cable, multiple links operate as one logical interface.

```
      Switch A
   ┌─────────────┐
   │             │
===│=============│===
===│=============│===
===│=============│===
   │             │
   └─────────────┘
      Switch B

Multiple Physical Links

↓

One Logical Link
```

---

## Why EtherChannel?

Benefits include:

- Increased bandwidth
- Link redundancy
- Load balancing
- Faster failover
- Simplified management

Instead of configuring four individual interfaces, administrators manage one logical interface.

---

# EtherChannel Protocols

There are two primary negotiation protocols.

| Protocol | Standard | Vendor |
|----------|----------|--------|
| LACP | IEEE 802.3ad / IEEE 802.1AX | Open Standard |
| PAgP | Cisco Proprietary | Cisco |

Modern enterprise environments typically prefer **LACP** because it supports multivendor interoperability.

---

# LACP Modes

| Mode | Description |
|------|-------------|
| Active | Actively negotiates an EtherChannel |
| Passive | Waits for negotiation requests |

A successful LACP EtherChannel requires at least one side to operate in **Active** mode.

---

# EtherChannel Requirements

Member interfaces should have matching characteristics:

- Speed
- Duplex
- VLAN configuration
- Trunk or access mode
- Allowed VLANs (for trunks)
- Native VLAN (for trunks)

Configuration mismatches can prevent the EtherChannel from forming.

---

# Load Balancing

EtherChannel distributes traffic across member links using a hashing algorithm.

Common hashing inputs include:

- Source MAC
- Destination MAC
- Source IP
- Destination IP
- Layer 4 ports (platform dependent)

Traffic from an individual flow generally remains on a single member link to preserve packet ordering.

---

# Port Security

## What is Port Security?

Port Security restricts which devices may connect to a switch port by controlling permitted MAC addresses.

Example:

```
Access Port

↓

Allowed MAC

↓

00:11:22:33:44:55
```

Unknown devices can be restricted or blocked based on the configured policy.

---

# Port Security Features

Administrators can:

- Limit the number of MAC addresses.
- Statically configure allowed MAC addresses.
- Dynamically learn secure MAC addresses.
- Use sticky MAC learning.

---

# Sticky MAC

Sticky MAC automatically learns MAC addresses and retains them as secure entries.

Benefits:

- Easier deployment
- Reduced manual configuration
- Better endpoint control

---

# Port Security Violation Modes

| Mode | Behavior |
|------|----------|
| Protect | Drops frames from unauthorized MAC addresses |
| Restrict | Drops frames and records/logs the violation |
| Shutdown | Places the port into an error-disabled state |

The appropriate mode depends on operational and security requirements.

---

# BPDU Guard

**BPDU Guard** protects edge (access) ports.

If a switch unexpectedly sends a BPDU to an access port:

```
Unexpected BPDU

↓

BPDU Guard

↓

Port Disabled
```

Benefits:

- Prevents unauthorized switches from influencing STP.
- Helps maintain a stable spanning tree topology.

---

# Root Guard

Root Guard prevents an unauthorized switch from becoming the Root Bridge.

Example:

```
Access Switch

↓

Attempts Root Election

↓

Root Guard

↓

Blocked
```

Deploy Root Guard on ports where the current Root Bridge should not change.

---

# Loop Guard

Loop Guard helps prevent certain Layer 2 loops caused by lost BPDUs.

If expected BPDUs stop arriving unexpectedly, Loop Guard places the port into a protected state rather than allowing an unintended forwarding loop.

---

# UDLD (Unidirectional Link Detection)

A fiber or copper link may fail in only one direction.

```
Switch A

↓

Transmit

↓

×

↓

Receive
```

UDLD detects unidirectional link failures and helps prevent forwarding inconsistencies.

---

# Storm Control

Storm Control limits excessive:

- Broadcast traffic
- Multicast traffic
- Unknown unicast traffic

Benefits:

- Protects bandwidth
- Reduces CPU utilization
- Mitigates broadcast storms
- Improves overall network stability

---

# Layer 2 Security Threats

Common Layer 2 attacks include:

- MAC flooding
- ARP spoofing
- VLAN hopping
- DHCP starvation
- Rogue DHCP servers
- STP manipulation
- CAM table exhaustion

These attacks target switching infrastructure rather than higher-layer services.

---

# MAC Flooding Attack

## Attack Overview

An attacker transmits a large number of frames with spoofed source MAC addresses.

```
Fake MAC

↓

Fake MAC

↓

Fake MAC

↓

CAM Table Full
```

The switch's CAM table can become saturated.

---

## Impact

When the CAM table cannot learn new entries, the switch may begin flooding unknown unicast traffic.

Potential consequences:

- Increased visibility of traffic to unauthorized devices.
- Higher bandwidth consumption.
- Reduced network performance.

---

## Mitigation

- Port Security
- MAC address limits
- Network monitoring
- Access control policies
- Physical security

---

# ARP Spoofing (ARP Poisoning)

An attacker sends forged ARP messages to associate their MAC address with another device's IP address.

Example:

```
Victim

↓

Incorrect ARP Entry

↓

Attacker
```

Potential consequences:

- Traffic interception
- Session hijacking
- Man-in-the-middle attacks
- Denial of service

---

## Mitigation

- Dynamic ARP Inspection (DAI)
- DHCP Snooping
- Static ARP entries (where appropriate)
- Network segmentation
- Encryption for sensitive communications

---

# VLAN Hopping

VLAN hopping attempts to access traffic from another VLAN.

Common techniques include:

### 1. Switch Spoofing

The attacker attempts to negotiate a trunk connection.

### 2. Double Tagging

The attacker crafts specially tagged frames in an attempt to cross VLAN boundaries under specific misconfigurations.

---

## Mitigation

- Disable Dynamic Trunking Protocol (DTP) where unnecessary.
- Manually configure access ports.
- Change the native VLAN from the default.
- Restrict VLANs permitted on trunks.
- Disable unused ports.

---

# DHCP Starvation

An attacker sends numerous DHCP requests using spoofed MAC addresses.

Result:

```
DHCP Pool

↓

Exhausted

↓

Legitimate Users

↓

No IP Address
```

---

## Mitigation

- DHCP Snooping
- Rate limiting
- Port Security
- Network Access Control (NAC)

---

# Rogue DHCP Server

An unauthorized DHCP server may assign:

- Incorrect gateways
- Incorrect DNS servers
- Malicious network settings

This can redirect or disrupt user traffic.

---

## Mitigation

- DHCP Snooping
- Trusted DHCP interfaces
- Switch port restrictions
- Continuous monitoring

---

# Enterprise Switching Best Practices

- Use dedicated management VLANs.
- Disable unused ports.
- Place unused ports into an unused VLAN.
- Enable Port Security on access ports.
- Enable BPDU Guard on edge ports.
- Configure Root Guard where appropriate.
- Use Storm Control on access interfaces.
- Authenticate management access.
- Document VLAN assignments and trunk links.
- Monitor switch logs and topology changes.

---

# Cisco IOS Verification Commands

Display MAC address table:

```text
show mac address-table
```

Display VLANs:

```text
show vlan brief
```

Display trunk interfaces:

```text
show interfaces trunk
```

Display spanning tree status:

```text
show spanning-tree
```

Display EtherChannel summary:

```text
show etherchannel summary
```

Display Port Security:

```text
show port-security
```

These commands are commonly used to verify Layer 2 operation and security features.

---

# Linux Verification

View neighbor cache:

```bash
ip neigh
```

Display interfaces:

```bash
ip link
```

Capture Ethernet traffic:

```bash
tcpdump -i eth0
```

---

# Windows Verification

Display ARP cache:

```cmd
arp -a
```

Display interface information:

```cmd
ipconfig /all
```

Display MAC address:

```cmd
getmac
```

---

# Wireshark Analysis

Useful display filters:

```text
arp
```

```text
stp
```

```text
lldp
```

```text
eth
```

Observe:

- ARP Requests and Replies
- BPDUs
- VLAN tags (802.1Q)
- Ethernet source and destination MAC addresses

Wireshark is invaluable for validating switching behavior and diagnosing Layer 2 issues.

---

# Practical Lab 1 — VLANs and Trunking

Objectives:

1. Create VLANs 10, 20, and 30.
2. Configure access ports.
3. Configure an 802.1Q trunk.
4. Verify communication within each VLAN.
5. Confirm that devices in different VLANs require Layer 3 routing.

---

# Practical Lab 2 — STP Verification

Tasks:

1. Build a triangle topology with three switches.
2. Observe Root Bridge election.
3. Identify blocked ports.
4. Disconnect an active link.
5. Observe convergence and path recalculation.

---

# Practical Lab 3 — EtherChannel

Tasks:

1. Connect two switches using four links.
2. Configure an LACP EtherChannel.
3. Verify bundle formation.
4. Generate traffic and observe load distribution.

---

# Practical Lab 4 — Port Security

Tasks:

1. Enable Port Security on an access port.
2. Limit the number of secure MAC addresses.
3. Test a violation using a different device.
4. Observe the configured violation action.

---

# Enterprise Case Study

## Scenario

A financial organization operates:

- Two data centers
- One headquarters
- Twenty branch offices

Requirements:

- High availability
- Department isolation
- Voice support
- Guest Wi-Fi
- Secure Layer 2 infrastructure

### Solution

- VLAN segmentation for departments
- Layer 3 switching for inter-VLAN routing
- RSTP for loop prevention
- LACP EtherChannels for uplinks
- Port Security on user-facing ports
- BPDU Guard and Root Guard on access interfaces
- DHCP Snooping and Dynamic ARP Inspection
- Dedicated management and voice VLANs

This architecture provides a scalable and resilient campus network while reducing Layer 2 attack exposure.

---

# Troubleshooting Methodology

When diagnosing switching issues:

```
Physical Connection

↓

Interface Status

↓

Speed and Duplex

↓

VLAN Assignment

↓

Trunk Status

↓

MAC Address Table

↓

STP State

↓

Port Security

↓

Packet Capture

↓

Application Testing
```

A systematic approach reduces troubleshooting time and helps isolate the root cause.

---

# Interview Questions

## Beginner

### What is a switch?

A switch is a Layer 2 device that forwards Ethernet frames using MAC addresses.

---

### What is a VLAN?

A VLAN is a logical Layer 2 network that creates a separate broadcast domain within a switch.

---

### What is a trunk port?

A trunk port carries traffic for multiple VLANs using IEEE 802.1Q tagging.

---

## Intermediate

### Explain STP.

STP prevents Layer 2 loops by electing a Root Bridge and placing redundant links into a non-forwarding state.

---

### What is EtherChannel?

EtherChannel combines multiple physical links into a single logical interface to improve bandwidth and redundancy.

---

### What is Port Security?

Port Security restricts access to a switch port by limiting or validating connected MAC addresses.

---

## Advanced

### How would you secure an enterprise switching environment?

A strong answer includes:

- VLAN segmentation
- Port Security
- BPDU Guard
- Root Guard
- Storm Control
- DHCP Snooping
- Dynamic ARP Inspection
- Secure management access
- Monitoring and logging

---

### How would you troubleshoot an STP issue?

An effective process includes:

1. Verify the Root Bridge.
2. Check port roles and states.
3. Review BPDU exchanges.
4. Confirm trunk configuration.
5. Identify blocked links.
6. Validate convergence after topology changes.

---

# References

## IEEE Standards

- IEEE 802.1D — Spanning Tree Protocol
- IEEE 802.1Q — VLAN Tagging
- IEEE 802.1w — Rapid Spanning Tree Protocol
- IEEE 802.1s — Multiple Spanning Tree Protocol
- IEEE 802.1AX — Link Aggregation (LACP)

## Organizations

- IEEE
- IETF
- NIST
- CIS

---

# Summary

Switching forms the foundation of enterprise LANs by enabling efficient Layer 2 communication. Features such as VLANs, STP, EtherChannel, and Layer 2 security controls allow organizations to build scalable, resilient, and secure campus networks. Proper design, hardening, and operational monitoring are essential to maintain high availability and defend against common Layer 2 threats.

---

# Chapter Review

After completing this chapter, you should understand:

✔ Layer 2 switching fundamentals

✔ MAC address learning and CAM tables

✔ Ethernet frame forwarding

✔ VLANs and broadcast domains

✔ IEEE 802.1Q trunking

✔ Inter-VLAN routing concepts

✔ Voice and management VLANs

✔ Spanning Tree Protocol (STP), RSTP, and MSTP

✔ Root Bridge election and BPDU operation

✔ EtherChannel with LACP

✔ Port Security and sticky MAC

✔ BPDU Guard, Root Guard, Loop Guard, UDLD, and Storm Control

✔ Common Layer 2 attacks and mitigations

✔ Cisco verification commands

✔ Wireshark Layer 2 analysis

✔ Enterprise troubleshooting methodology

✔ Practical switching labs

✔ Interview preparation from beginner to advanced

---

# What's Next?

The next chapter, **`09-ARP.md`**, will explore:

- Address Resolution Protocol (ARP)
- Gratuitous ARP
- Proxy ARP
- ARP cache behavior
- ARP request and reply workflow
- ARP poisoning and spoofing
- Dynamic ARP Inspection (DAI)
- Neighbor Discovery Protocol (IPv6 comparison)
- Packet capture analysis
- Enterprise troubleshooting and security