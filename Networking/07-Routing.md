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

