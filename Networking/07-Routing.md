# 07 - Routing

# Part 1 — Routing Fundamentals, Router Architecture, Packet Forwarding, and Routing Tables

---

# Overview

Routing is the process of forwarding packets from one network to another.

While **switches** primarily forward traffic within the same Layer 2 network using **MAC addresses**, **routers** operate at **Layer 3 (Network Layer)** and make forwarding decisions based on **IP addresses**.

Every packet that travels across the Internet—from opening a website to accessing a cloud service—passes through multiple routers before reaching its destination.

Routing is therefore one of the fundamental technologies that enables modern communication across enterprise networks, cloud environments, and the global Internet.

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain the purpose of routing.
- Differentiate routing from switching.
- Understand router architecture.
- Explain packet forwarding.
- Interpret routing tables.
- Describe default gateways.
- Understand routing decisions.
- Follow a packet from source to destination.
- Recognize enterprise routing architectures.

---

# What is Routing?

**Routing** is the process of selecting the best path for IP packets to travel between different networks.

Example:

```
Laptop
192.168.10.20

        │

Access Switch

        │

Router

        │

Internet

        │

Web Server
203.0.113.10
```

Without routing, communication would be limited to devices within the same subnet.

---

# Why Routing is Important

Routing enables:

- Communication between different subnets
- Internet connectivity
- Cloud connectivity
- Branch office communication
- Data center communication
- VPN connectivity
- Disaster recovery
- Hybrid cloud networking

Without routers, modern enterprise networks would be isolated islands.

---

# Routing vs Switching

| Feature | Switching | Routing |
|----------|-----------|----------|
| OSI Layer | Layer 2 | Layer 3 |
| Address Used | MAC Address | IP Address |
| Device | Switch | Router |
| Broadcast Domains | Same | Separate |
| Collision Domains | Separate per port | Separate |
| Typical Purpose | Local communication | Inter-network communication |

Example:

```
PC A

↓

Switch

↓

PC B

(Same VLAN)
```

No router is required.

```
PC A

↓

Switch

↓

Router

↓

Switch

↓

PC C

(Different Network)
```

A router is required because the devices are on different subnets.

---

# Router Fundamentals

A **router** is a Layer 3 device responsible for:

- Connecting different IP networks
- Selecting optimal paths
- Forwarding packets
- Maintaining routing tables
- Performing route lookups
- Enforcing routing policies

Many enterprise routers also provide:

- NAT
- VPN termination
- Firewall capabilities
- QoS
- Traffic shaping
- High Availability
- MPLS support

---

# Router Components

A modern router consists of several key components.

```
                Router
        ┌────────────────────┐
        │        CPU         │
        ├────────────────────┤
        │        RAM         │
        ├────────────────────┤
        │      Flash         │
        ├────────────────────┤
        │     Interfaces     │
        ├────────────────────┤
        │ Routing Table (RIB)│
        └────────────────────┘
```

---

## CPU

Responsible for:

- Routing protocol calculations
- Control plane operations
- Route computation
- Network management
- Packet processing (where hardware offload is unavailable)

---

## RAM

Stores:

- Routing tables
- ARP cache
- Neighbor tables
- Packet buffers
- Running configuration
- Dynamic protocol information

---

## Flash Storage

Stores:

- Operating system image
- Startup configuration
- Firmware
- Logs (platform dependent)

---

## Network Interfaces

Interfaces connect routers to networks.

Examples:

- Ethernet
- Fiber
- Serial (legacy)
- MPLS
- VPN tunnels
- Loopback interfaces

Each interface belongs to a different Layer 3 network.

---

# Router Interfaces Example

```
                Router

Interface G0/0

192.168.10.1/24

──────────────

Interface G0/1

192.168.20.1/24

──────────────

Interface G0/2

203.0.113.2/30
```

Each interface acts as the gateway for its connected subnet.

---

# What is a Default Gateway?

A **default gateway** is the router interface that a host uses to reach networks outside its own subnet.

Example:

```
Laptop

IP:

192.168.10.50

Mask:

255.255.255.0

Gateway:

192.168.10.1
```

When the laptop needs to communicate with a remote network, it forwards packets to its configured default gateway.

---

# Local vs Remote Traffic

Suppose:

```
PC

192.168.10.25/24
```

Destination:

```
192.168.10.100
```

The destination is in the same subnet.

Result:

```
Direct Layer 2 Communication
```

No router is involved.

---

Destination:

```
192.168.20.50
```

Different subnet.

Result:

```
Send Packet

↓

Default Gateway

↓

Router
```

The router forwards the packet toward the destination network.

---

# Packet Forwarding Process

When a packet arrives at a router:

```
Receive Packet

↓

Verify Packet

↓

Inspect Destination IP

↓

Consult Routing Table

↓

Determine Best Route

↓

Rewrite Layer 2 Header

↓

Forward Packet
```

The router does **not** change the destination IP address during normal forwarding. It removes the incoming Layer 2 frame and encapsulates the packet in a new Layer 2 frame appropriate for the outgoing interface.

---

# Packet Journey Example

Source:

```
192.168.10.25
```

Destination:

```
172.16.20.50
```

Flow:

```
PC

↓

Switch

↓

Default Gateway

↓

Core Router

↓

ISP

↓

Destination Router

↓

Switch

↓

Server
```

At every router:

- The Layer 2 frame is replaced.
- The IP packet is examined.
- The routing table is consulted.
- The packet is forwarded to the next hop.

---

# What is a Routing Table?

A **routing table** is a database containing information about reachable networks and the paths used to reach them.

Example:

| Destination | Next Hop | Interface |
|-------------|----------|-----------|
| 192.168.10.0/24 | Connected | G0/0 |
| 192.168.20.0/24 | Connected | G0/1 |
| 10.0.0.0/8 | 203.0.113.1 | G0/2 |
| 0.0.0.0/0 | ISP Gateway | G0/2 |

The router consults this table for every packet it forwards.

---

# Routing Table Components

A routing table entry typically includes:

- Destination network
- Prefix length
- Next-hop IP address
- Outgoing interface
- Route source
- Metric
- Administrative Distance (platform dependent)

---

# Types of Routes

Routers can learn routes from different sources.

### Connected Routes

Automatically created when an interface is configured with an IP address.

Example:

```
192.168.10.0/24

Connected
```

---

### Static Routes

Manually configured by an administrator.

Example:

```
Destination:

10.10.10.0/24

↓

Next Hop:

192.168.20.254
```

---

### Dynamic Routes

Learned automatically through routing protocols such as:

- RIP
- OSPF
- EIGRP
- IS-IS
- BGP

These protocols are covered later in this chapter.

---

# Default Route

A **default route** is used when no more specific route exists.

Representation:

```
0.0.0.0/0
```

Meaning:

```
Unknown Destination

↓

Forward to Default Gateway
```

This is commonly referred to as the **Gateway of Last Resort**.

---

# Longest Prefix Match Review

Consider the routing table:

| Route | Prefix |
|--------|--------|
| 10.0.0.0/8 | General |
| 10.10.0.0/16 | More Specific |
| 10.10.20.0/24 | Most Specific |

Destination:

```
10.10.20.55
```

The router chooses:

```
10.10.20.0/24
```

because it has the **longest matching prefix**.

---

# Enterprise Routing Example

```
                 Internet
                     │
               Edge Router
                     │
              Core Router
        ┌────────┼────────┐
        │        │        │
      HR VLAN  IT VLAN  Data Center
```

The core router maintains routes to all internal networks and forwards traffic between departments and toward the Internet.

---

# Common Routing Issues

| Problem | Possible Cause |
|----------|----------------|
| Destination unreachable | Missing route |
| No Internet access | Missing default route |
| Routing loop | Incorrect route configuration |
| Asymmetric routing | Different forward and return paths |
| High latency | Suboptimal routing path |
| Black hole | Packets dropped due to incorrect routing |

---

# Business Impact

Efficient routing provides:

- Reliable communication
- High application availability
- Faster response times
- Better scalability
- Secure inter-network connectivity
- Cloud integration
- Disaster recovery support

Poor routing design can result in outages, degraded performance, and operational complexity.

---

# Key Takeaways

- Routing enables communication between different IP networks.
- Routers operate at OSI Layer 3 using IP addresses.
- Hosts send remote traffic to their default gateway.
- Routers make forwarding decisions using routing tables.
- Routes may be connected, static, dynamic, or default.
- The **Longest Prefix Match** rule ensures the most specific route is selected.
- Routing is a foundational technology for enterprise, cloud, and Internet connectivity.

# 07 - Routing

# Part 2 — Routing Decisions, Administrative Distance, Routing Metrics, FIB, CEF, ECMP, and Packet Forwarding

---

# Overview

In the previous section, we learned that routers use **routing tables** to forward packets between networks.

However, enterprise routers do much more than simply look up a destination network.

For every packet, a router must determine:

- Is the destination directly connected?
- Which route is the most trustworthy?
- Which path is the most efficient?
- Which interface should be used?
- What is the next-hop MAC address?
- Should multiple equal-cost paths be used?

Understanding these decisions is essential for network engineers, SOC analysts, cloud engineers, and cybersecurity professionals.

---

# Packet Forwarding Workflow

When a router receives a packet, it follows a structured forwarding process.

```
Receive Ethernet Frame

↓

Verify Frame Integrity

↓

Remove Layer 2 Header

↓

Inspect Destination IP

↓

Routing Table Lookup

↓

Select Best Route

↓

Resolve Next-Hop MAC

↓

Build New Ethernet Frame

↓

Transmit Packet
```

> **Important:** During normal routing, the router changes the Layer 2 frame but preserves the Layer 3 source and destination IP addresses (unless features such as NAT are applied).

---

# Control Plane vs Data Plane

Enterprise routers separate responsibilities into different operational planes.

```
                Router
        ┌───────────────────┐
        │   Control Plane   │
        ├───────────────────┤
        │    Data Plane     │
        └───────────────────┘
```

---

## Control Plane

Responsible for:

- Learning routes
- Running routing protocols
- Building the Routing Information Base (RIB)
- ARP/Neighbor Discovery
- Network management
- Device configuration

Examples:

- OSPF calculations
- BGP updates
- Static route configuration

The control plane decides **where traffic should go**.

---

## Data Plane

Responsible for:

- High-speed packet forwarding
- Looking up forwarding entries
- Rewriting Layer 2 headers
- Sending packets to the correct interface

The data plane determines **how traffic is forwarded**.

---

# Routing Information Base (RIB)

The **Routing Information Base (RIB)** is the logical routing table maintained by the control plane.

It stores:

- Connected routes
- Static routes
- Dynamic routes
- Default routes

Example:

| Destination | Next Hop | Source |
|-------------|----------|--------|
| 192.168.10.0/24 | Connected | Connected |
| 10.10.0.0/16 | 192.168.20.1 | OSPF |
| 0.0.0.0/0 | ISP | Static |

The RIB is responsible for route selection.

---

# Forwarding Information Base (FIB)

The **Forwarding Information Base (FIB)** is an optimized forwarding table used by the data plane.

```
Routing Protocols

↓

RIB

↓

FIB

↓

Packet Forwarding
```

Unlike the RIB, the FIB is optimized for rapid lookups so packets can be forwarded efficiently.

---

# Why Routers Use a FIB

If routers searched the full routing table for every packet, forwarding performance would suffer.

Instead:

- The control plane computes the best routes.
- The FIB stores optimized forwarding information.
- The data plane performs fast lookups using the FIB.

This separation improves scalability and throughput.

---

# Cisco Express Forwarding (CEF)

**Cisco Express Forwarding (CEF)** is Cisco's high-performance Layer 3 forwarding architecture.

CEF uses two primary tables:

```
Forwarding Information Base (FIB)

↓

Adjacency Table
```

Benefits include:

- Faster forwarding
- Lower CPU utilization
- Reduced packet processing latency
- Better scalability
- Hardware acceleration on supported platforms

Modern enterprise routers and multilayer switches typically rely on CEF or equivalent forwarding technologies.

---

# Adjacency Table

The adjacency table maps:

```
Next-Hop IP Address

↓

Destination MAC Address

↓

Outgoing Interface
```

Example:

| Next Hop | MAC Address | Interface |
|----------|-------------|-----------|
| 192.168.1.1 | 00:11:22:33:44:55 | G0/0 |

This allows the router to quickly build the outgoing Ethernet frame.

---

# ARP and Next-Hop Resolution

Before sending a packet on an Ethernet network, the router must know the destination MAC address.

Process:

```
Destination IP

↓

Routing Table

↓

Next-Hop IP

↓

ARP Lookup

↓

MAC Address

↓

Forward Frame
```

If the MAC address is unknown:

1. The router sends an ARP Request.
2. The next-hop device replies with an ARP Reply.
3. The mapping is stored in the ARP cache.

For IPv6, this process uses **Neighbor Discovery Protocol (NDP)** instead of ARP.

---

# Route Lookup Process

A simplified route lookup:

```
Packet Arrives

↓

Destination IP

↓

Search FIB

↓

Longest Prefix Match

↓

Determine Next Hop

↓

Resolve MAC

↓

Forward Packet
```

---

# Longest Prefix Match (LPM)

Routers may have multiple matching routes.

Example:

| Route | Prefix |
|--------|--------|
| 10.0.0.0/8 | Broad |
| 10.10.0.0/16 | More Specific |
| 10.10.20.0/24 | Most Specific |

Destination:

```
10.10.20.50
```

The router chooses:

```
10.10.20.0/24
```

because it has the **longest matching prefix**.

---

# Administrative Distance (AD)

Sometimes, a router learns the same destination through multiple sources.

Example:

```
Static Route

↓

OSPF

↓

RIP
```

Which route should be trusted?

The answer is **Administrative Distance (AD)**.

Administrative Distance measures the **trustworthiness of the route source**.

Lower values are preferred.

---

# Common Administrative Distances

| Route Source | Administrative Distance |
|---------------|-----------------------:|
| Connected | 0 |
| Static | 1 |
| eBGP | 20 |
| EIGRP (Internal) | 90 |
| OSPF | 110 |
| IS-IS | 115 |
| RIP | 120 |
| EIGRP (External) | 170 |
| Unknown / Unreachable | 255 |

> These values are Cisco defaults. Other vendors may use different defaults.

---

# Example — Administrative Distance

Suppose the router learns:

```
10.20.0.0/16

↓

Static Route

AD = 1
```

and

```
10.20.0.0/16

↓

OSPF

AD = 110
```

The router selects:

```
Static Route
```

because it has the lower Administrative Distance.

---

# Routing Metrics

Administrative Distance decides **which routing source is trusted**.

A **metric** decides the **best path within the same routing protocol**.

Different routing protocols use different metrics.

Examples:

| Protocol | Metric |
|----------|--------|
| RIP | Hop Count |
| OSPF | Cost |
| EIGRP | Composite Metric |
| IS-IS | Cost |
| BGP | Path Attributes |

---

# Hop Count

RIP selects routes based on:

```
Number of Routers Traversed
```

Example:

```
Router A

↓

Router B

↓

Router C
```

Hop count:

```
2
```

Smaller hop counts are preferred.

---

# OSPF Cost

OSPF uses **cost**, which is generally based on interface bandwidth.

Higher-bandwidth links typically have lower costs and are preferred over slower links.

---

# Equal-Cost Multi-Path (ECMP)

Sometimes multiple routes have:

- Same destination
- Same Administrative Distance
- Same metric

Example:

```
           Router
          /      \
         /        \
Route A        Route B
```

Both paths are equally good.

Instead of selecting only one path, the router can install both.

This feature is called **Equal-Cost Multi-Path (ECMP)**.

---

# Benefits of ECMP

- Load sharing
- Better bandwidth utilization
- Increased redundancy
- Improved availability
- Faster failover

Many enterprise networks and data centers use ECMP extensively.

---

# Recursive Route Lookup

Sometimes a route points to a next-hop IP address rather than a directly connected interface.

Example:

```
Destination

10.20.0.0/16

↓

Next Hop

192.168.1.1
```

The router must first determine how to reach:

```
192.168.1.1
```

This process is known as a **recursive lookup**.

The router repeats route lookups until it finds a directly connected interface.

---

# TTL (Time To Live)

Each IPv4 packet contains a **Time To Live (TTL)** field.

Purpose:

- Prevent infinite routing loops.

Example:

```
TTL = 64
```

Each router decrements the TTL by **1**.

If TTL reaches:

```
0
```

The router discards the packet and returns an ICMP **Time Exceeded** message.

IPv6 uses a similar field called the **Hop Limit**.

---

# Enterprise Packet Walkthrough

Consider the following path:

```
Client
192.168.10.25

↓

Access Switch

↓

Core Router

↓

Firewall

↓

ISP

↓

Cloud Service
```

The forwarding sequence:

1. Client determines the destination is remote.
2. Packet is sent to the default gateway.
3. Router performs an FIB lookup.
4. Longest Prefix Match selects the best route.
5. Next-hop MAC is resolved (ARP/NDP).
6. Router rewrites the Ethernet header.
7. Packet is forwarded toward the firewall.
8. The process repeats at each hop until the destination is reached.

---

# Common Routing Decision Problems

| Problem | Possible Cause |
|----------|----------------|
| Incorrect route selected | Administrative Distance or metric issue |
| Traffic black hole | Missing or invalid next hop |
| Routing loop | Misconfigured routes or protocol issues |
| ARP resolution failure | Layer 2 connectivity problem |
| ECMP imbalance | Hashing behavior or asymmetric traffic |
| Excessive CPU usage | Software forwarding or control plane overload |

---

# Key Takeaways

- The **RIB** stores learned routes, while the **FIB** is optimized for fast forwarding.
- The **control plane** computes routes; the **data plane** forwards packets.
- **Administrative Distance** determines which routing source is trusted.
- **Metrics** determine the best path within a routing protocol.
- **Longest Prefix Match** always selects the most specific route.
- **ECMP** allows traffic to be distributed across multiple equal-cost paths.
- ARP (IPv4) and Neighbor Discovery (IPv6) resolve next-hop Layer 2 addresses before packets are forwarded.

# 07 - Routing

# Part 3 — Static Routing, Dynamic Routing Protocols, OSPF, EIGRP, IS-IS, BGP, and Enterprise Routing Design

---

# Overview

Routers need a way to learn how to reach remote networks.

There are three primary methods:

```
Connected Routes

↓

Static Routes

↓

Dynamic Routing Protocols
```

The appropriate method depends on:

- Network size
- Complexity
- Scalability requirements
- Redundancy
- Administrative overhead

Small networks may rely entirely on static routes, while enterprise networks typically use dynamic routing protocols.

---

# Route Learning Methods

| Method | Learned From | Typical Use |
|----------|--------------|-------------|
| Connected | Router Interface | Directly attached networks |
| Static | Administrator | Small or predictable networks |
| Dynamic | Routing Protocol | Medium to large enterprise networks |

---

# Connected Routes

Whenever an IP address is assigned to an active router interface, the router automatically installs a connected route.

Example:

```
Interface:

GigabitEthernet0/0

↓

IP:

192.168.10.1/24
```

Routing table entry:

```
192.168.10.0/24

↓

Connected
```

No manual configuration is required.

---

# Static Routing

A **static route** is manually configured by a network administrator.

Example:

```
Router A

↓

Router B

↓

10.20.0.0/16
```

Router A is configured with:

```
Destination

10.20.0.0/16

↓

Next Hop

192.168.1.2
```

---

# Advantages of Static Routing

- Simple
- Predictable
- Low CPU usage
- No routing protocol overhead
- Better control
- Useful for security-sensitive paths

---

# Disadvantages

- Manual configuration
- Poor scalability
- Difficult maintenance
- No automatic failover (unless configured)
- Not suitable for rapidly changing topologies

---

# Default Route

Instead of configuring routes to every possible destination, a router can use a **default route**.

Representation:

```
0.0.0.0/0
```

Meaning:

```
Unknown Destination

↓

Forward to Default Gateway
```

Typical deployment:

```
Branch Office

↓

Internet Router

↓

ISP
```

---

# Floating Static Route

A **floating static route** acts as a backup route.

It is configured with a higher **Administrative Distance** than the primary route.

Example:

Primary:

```
OSPF

AD = 110
```

Backup:

```
Static Route

AD = 120
```

The static route remains inactive until the OSPF route is lost.

---

# Dynamic Routing

Dynamic routing protocols automatically:

- Discover neighbors
- Exchange routing information
- Learn new networks
- Detect failures
- Recalculate routes

Benefits include:

- Scalability
- Redundancy
- Faster convergence
- Reduced administrative effort

---

# Distance Vector vs Link-State

Routing protocols are commonly categorized as:

| Category | Examples |
|----------|----------|
| Distance Vector | RIP |
| Advanced Distance Vector | EIGRP |
| Link-State | OSPF, IS-IS |
| Path Vector | BGP |

Each category uses a different algorithm to determine the best path.

---

# Routing Protocol Comparison

| Protocol | Type | Metric | Typical Scale |
|----------|------|--------|---------------|
| RIP | Distance Vector | Hop Count | Small |
| OSPF | Link-State | Cost | Enterprise |
| EIGRP | Advanced Distance Vector | Composite Metric | Enterprise (primarily Cisco) |
| IS-IS | Link-State | Cost | Service Providers |
| BGP | Path Vector | Path Attributes | Internet / Large Enterprises |

---

# RIP (Routing Information Protocol)

RIP is one of the oldest dynamic routing protocols.

Characteristics:

- Distance Vector
- Uses hop count
- Maximum of 15 hops
- 16 hops = unreachable
- Periodic updates (typically every 30 seconds)

Example:

```
Router A

↓

Router B

↓

Router C
```

Hop count:

```
2
```

---

## Advantages of RIP

- Simple configuration
- Easy to understand
- Suitable for small networks

---

## Limitations

- Slow convergence
- Limited scalability
- Hop-count restriction
- Less efficient than modern protocols

RIP is rarely deployed in large enterprise environments today.

---

# OSPF (Open Shortest Path First)

OSPF is one of the most widely used enterprise Interior Gateway Protocols (IGPs).

Characteristics:

- Link-State protocol
- Fast convergence
- Hierarchical design
- Uses Dijkstra's Shortest Path First (SPF) algorithm
- Supports VLSM and CIDR
- Scales well in large networks

---

# OSPF Areas

Large OSPF deployments divide the network into **areas**.

```
             Area 0
          (Backbone Area)
         /       |       \
    Area 1   Area 2   Area 3
```

Area 0 is the backbone and connects all other areas.

Benefits:

- Smaller routing tables
- Reduced SPF calculations
- Better scalability

---

# OSPF Router Types

Common OSPF router roles include:

- Internal Router
- Backbone Router
- Area Border Router (ABR)
- Autonomous System Boundary Router (ASBR)

Each role has specific responsibilities for route exchange and area connectivity.

---

# OSPF Neighbor States

Routers establish neighbor relationships before exchanging routes.

Simplified progression:

```
Down

↓

Init

↓

2-Way

↓

ExStart

↓

Exchange

↓

Loading

↓

Full
```

Only routers in the **Full** state have synchronized link-state databases.

---

# Designated Router (DR) and Backup Designated Router (BDR)

On multi-access networks (such as Ethernet), OSPF elects:

- Designated Router (DR)
- Backup Designated Router (BDR)

Purpose:

- Reduce routing update traffic
- Improve efficiency
- Minimize adjacency overhead

---

# Link-State Advertisements (LSAs)

OSPF shares topology information using **Link-State Advertisements (LSAs)**.

LSAs describe:

- Networks
- Routers
- Links
- External routes
- Area information

Routers build a common **Link-State Database (LSDB)** from received LSAs.

---

# Dijkstra's SPF Algorithm

OSPF uses the **Shortest Path First (SPF)** algorithm to calculate the most efficient path.

Simplified process:

```
Collect LSAs

↓

Build Topology Database

↓

Run SPF Algorithm

↓

Install Best Routes
```

---

# OSPF Cost

OSPF chooses paths based on **cost**, which is generally derived from interface bandwidth.

Example:

| Link | Cost |
|------|-----:|
| 10 Gbps | Lower |
| 1 Gbps | Moderate |
| 100 Mbps | Higher |

Lower total cost is preferred.

---

# EIGRP (Enhanced Interior Gateway Routing Protocol)

EIGRP is an advanced distance-vector protocol originally developed by Cisco.

Characteristics:

- Fast convergence
- Supports unequal-cost load balancing
- Efficient updates
- Low bandwidth usage

It uses the **Diffusing Update Algorithm (DUAL)** to calculate loop-free paths.

---

# EIGRP Metric

EIGRP uses a composite metric based primarily on:

- Bandwidth
- Delay

Additional optional factors include:

- Reliability
- Load
- MTU (recorded but not directly used in the default metric)

---

# DUAL Algorithm

DUAL provides:

- Loop-free routing
- Rapid convergence
- Backup paths (feasible successors)

This reduces downtime during network failures.

---

# IS-IS (Intermediate System to Intermediate System)

IS-IS is another link-state routing protocol.

Commonly deployed in:

- Service provider networks
- Large enterprise backbones
- Carrier infrastructures

Characteristics:

- Highly scalable
- Fast convergence
- Efficient flooding
- Hierarchical design

---

# BGP (Border Gateway Protocol)

BGP is the routing protocol that powers the Internet.

Unlike IGPs, BGP exchanges routing information between **Autonomous Systems (ASes)**.

Example:

```
Enterprise AS

↓

ISP

↓

Cloud Provider

↓

Another ISP
```

Each organization advertises reachable networks to its neighbors.

---

# Interior vs Exterior Routing

| Type | Protocols |
|------|-----------|
| Interior Gateway Protocol (IGP) | RIP, OSPF, EIGRP, IS-IS |
| Exterior Gateway Protocol (EGP) | BGP |

IGPs operate **within** an organization.

BGP operates **between** organizations or autonomous systems.

---

# Autonomous System (AS)

An **Autonomous System** is a collection of IP networks managed under a single administrative authority.

Each AS is assigned a unique **Autonomous System Number (ASN)**.

Example:

```
Enterprise

AS65001

↓

ISP

AS64512

↓

Cloud Provider

AS15169
```

---

# BGP Path Selection (Simplified)

BGP evaluates multiple attributes to determine the preferred route.

Common attributes include:

- Local Preference
- AS Path
- Origin
- MED (Multi-Exit Discriminator)
- Next Hop

Unlike IGPs, BGP focuses on routing policy in addition to path efficiency.

---

# Route Convergence

**Convergence** is the time required for routers to agree on the current network topology after a change.

Fast convergence results in:

- Minimal downtime
- Faster recovery
- Improved application availability

---

# Route Redistribution

Organizations sometimes run multiple routing protocols.

Example:

```
OSPF

↓

Redistribution

↓

BGP
```

Route redistribution exchanges routing information between different routing domains.

Because it can introduce routing loops or suboptimal paths if misconfigured, it should be planned carefully.

---

# Enterprise Routing Protocol Selection

| Environment | Recommended Protocol |
|-------------|----------------------|
| Small Office | Static Routing |
| Small Branch | Static + Default Route |
| Enterprise Campus | OSPF |
| Large Service Provider | IS-IS |
| Internet Edge | BGP |
| Cisco-Centric Enterprise | OSPF or EIGRP (where appropriate) |

Protocol selection depends on scalability, interoperability, operational requirements, and organizational standards.

---

# Common Routing Protocol Issues

| Problem | Possible Cause |
|----------|----------------|
| Neighbor adjacency fails | Authentication mismatch, interface mismatch, area mismatch |
| Slow convergence | Protocol timers, topology size |
| Routing loops | Redistribution or configuration errors |
| Missing routes | Advertisement filters or incorrect network statements |
| Asymmetric routing | Policy differences or multiple paths |

---

# Key Takeaways

- **Static routing** is simple and predictable but does not scale well.
- **Dynamic routing protocols** automatically discover and maintain routes.
- **OSPF** is the most common enterprise IGP due to its scalability and fast convergence.
- **EIGRP** provides rapid convergence and advanced features, primarily in Cisco environments.
- **IS-IS** is widely used by service providers and large backbones.
- **BGP** connects autonomous systems and forms the foundation of Internet routing.
- Route convergence, redistribution, and protocol selection are critical aspects of enterprise network design.

