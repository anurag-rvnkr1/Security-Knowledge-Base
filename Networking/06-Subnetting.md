# 06 - Subnetting

# Part 1 — Subnetting Fundamentals, Binary Mathematics, CIDR, and Network Design Principles

---

# Overview

Subnetting is one of the most important concepts in networking.

It allows a large IP network to be divided into multiple smaller, manageable networks called **subnets**.

Every modern enterprise network relies on subnetting for:

- Network segmentation
- Efficient IP address utilization
- Security isolation
- Performance optimization
- Route summarization
- Cloud networking
- High Availability (HA)

Whether you are configuring routers, designing enterprise networks, securing cloud infrastructure, or preparing for cybersecurity interviews, subnetting is an essential skill.

---

# Learning Objectives

After completing this chapter, you should be able to:

- Understand why subnetting is required.
- Explain CIDR notation.
- Calculate network and broadcast addresses.
- Determine usable host ranges.
- Design enterprise subnet layouts.
- Perform binary subnet calculations.
- Understand VLSM and route summarization.
- Troubleshoot subnet-related issues.

---

# What is a Subnet?

A **subnet** (subnetwork) is a logical division of a larger IP network into smaller networks.

Instead of one large network:

```
10.0.0.0/8
```

we can create multiple smaller networks:

```
10.10.10.0/24

10.10.20.0/24

10.10.30.0/24

10.10.40.0/24
```

Each subnet functions as an independent Layer 3 network.

---

# Why Do We Need Subnetting?

Imagine an organization with 5,000 employees using a single network.

```
10.0.0.0/8

↓

Everyone
```

Problems include:

- Large broadcast domains
- Difficult troubleshooting
- Poor security
- High network congestion
- Limited policy enforcement

Instead:

```
HR

10.10.10.0/24

↓

Finance

10.10.20.0/24

↓

IT

10.10.30.0/24

↓

Servers

10.10.40.0/24
```

Benefits:

- Better security
- Reduced broadcasts
- Easier management
- Improved performance
- Simplified routing

---

# What is a Broadcast Domain?

A **broadcast domain** is the set of devices that receive Layer 2 broadcast traffic.

Without subnetting:

```
Entire Office

↓

One Broadcast Domain
```

With subnetting:

```
HR

↓

Broadcast Domain 1

──────────────

Finance

↓

Broadcast Domain 2

──────────────

IT

↓

Broadcast Domain 3
```

Each subnet creates a separate broadcast domain when connected through Layer 3 routing.

---

# Benefits of Subnetting

### Security

Different departments can be isolated.

Example:

```
Finance

↓

Accessible Only

↓

Finance Servers
```

---

### Performance

Broadcast traffic remains within each subnet.

```
Smaller Broadcast Domain

↓

Less Network Congestion
```

---

### Scalability

Organizations can grow without redesigning the entire network.

---

### Easier Troubleshooting

Problems can be isolated to individual subnets.

---

### Better Routing

Routers forward traffic more efficiently when networks are logically organized.

---

# IPv4 Address Review

IPv4 consists of:

```
32 Bits
```

Represented as:

```
192.168.10.25
```

Binary:

```
11000000

10101000

00001010

00011001
```

Each octet contains:

```
8 Bits
```

---

# Network Portion vs Host Portion

Example:

```
192.168.10.25/24
```

```
Network

192.168.10

↓

Host

25
```

The subnet mask determines where the network portion ends and the host portion begins.

---

# Binary Refresher

Each octet consists of:

| Bit Position | Value |
|--------------|------:|
| 1 | 128 |
| 2 | 64 |
| 3 | 32 |
| 4 | 16 |
| 5 | 8 |
| 6 | 4 |
| 7 | 2 |
| 8 | 1 |

Example:

```
10101100

↓

128 + 32 + 8 + 4

↓

172
```

Understanding binary is essential for manual subnet calculations.

---

# What is a Subnet Mask?

A **subnet mask** identifies which bits belong to the **network** and which belong to the **host**.

Example:

```
255.255.255.0
```

Binary:

```
11111111

11111111

11111111

00000000
```

Meaning:

```
Network

24 Bits

↓

Host

8 Bits
```

---

# CIDR Notation

CIDR stands for:

```
Classless Inter-Domain Routing
```

Instead of writing:

```
255.255.255.0
```

we write:

```
/24
```

Examples:

| CIDR | Subnet Mask |
|------|-------------|
| /8 | 255.0.0.0 |
| /16 | 255.255.0.0 |
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |
| /28 | 255.255.255.240 |
| /29 | 255.255.255.248 |
| /30 | 255.255.255.252 |

CIDR allows flexible network sizing instead of relying on traditional address classes.

---

# How CIDR Works

Example:

```
192.168.1.100/24
```

```
24 Network Bits

↓

8 Host Bits
```

Binary:

```
11111111.11111111.11111111.00000000
```

The first 24 bits identify the network.

The remaining 8 bits identify individual hosts.

---

# Network Address

The **network address** identifies the subnet itself.

Example:

```
Network

192.168.1.0/24
```

This address **cannot** be assigned to a host.

---

# Broadcast Address

The **broadcast address** is the highest address in the subnet.

Example:

```
192.168.1.255
```

Packets sent to this address are delivered to all hosts within the subnet.

---

# Usable Host Addresses

For:

```
192.168.1.0/24
```

Usable range:

```
192.168.1.1

↓

192.168.1.254
```

Reserved addresses:

```
192.168.1.0

(Network)

────────────

192.168.1.255

(Broadcast)
```

---

# Host Calculation Formula

The number of usable hosts is calculated as:

```
2^(Host Bits) − 2
```

The subtraction of **2** accounts for:

- Network address
- Broadcast address

Examples:

| Prefix | Host Bits | Usable Hosts |
|--------|----------:|-------------:|
| /24 | 8 | 254 |
| /25 | 7 | 126 |
| /26 | 6 | 62 |
| /27 | 5 | 30 |
| /28 | 4 | 14 |
| /29 | 3 | 6 |
| /30 | 2 | 2 |

> Note: `/31` and `/32` have specialized uses defined by RFCs and are discussed later in this chapter.

---

# Borrowing Bits

Subnetting works by borrowing bits from the host portion.

Example:

Original network:

```
192.168.1.0/24
```

Borrow one bit:

```
/25
```

Borrow two bits:

```
/26
```

Borrow three bits:

```
/27
```

Each borrowed bit:

- Creates more subnets
- Reduces the number of usable hosts per subnet

---

# Subnet Calculation Example

Original:

```
192.168.10.0/24
```

Convert to:

```
/26
```

Results:

```
192.168.10.0/26

192.168.10.64/26

192.168.10.128/26

192.168.10.192/26
```

Each subnet provides:

```
64 Addresses

↓

62 Usable Hosts
```

---

# Enterprise Example

```
Corporate Office

↓

10.50.0.0/16

├───────────────┐
│               │
HR          10.50.10.0/24
IT          10.50.20.0/24
Finance     10.50.30.0/24
Servers     10.50.40.0/24
Guest Wi-Fi 10.50.50.0/24
```

Advantages:

- Department isolation
- Simplified firewall rules
- Better routing
- Reduced broadcasts
- Easier network management

---

# Common Subnetting Mistakes

| Mistake | Result |
|----------|--------|
| Incorrect subnet mask | Communication failures |
| Overlapping subnets | Routing conflicts |
| Duplicate IP addresses | Address conflicts |
| Wrong default gateway | External connectivity failure |
| Ignoring future growth | Frequent network redesign |
| Oversized broadcast domains | Performance degradation |

---

# Business Impact

Proper subnetting enables:

- Efficient use of IPv4 space
- Reduced broadcast traffic
- Stronger network segmentation
- Easier troubleshooting
- Scalable enterprise growth
- Better security policy enforcement

Poor subnet design increases operational complexity and can introduce performance and security issues.

---

# Key Takeaways

- Subnetting divides a large network into smaller logical networks.
- CIDR provides flexible address allocation by using prefix lengths.
- Every subnet has a network address, a broadcast address, and a range of usable host addresses.
- Borrowing host bits creates additional subnets while reducing hosts per subnet.
- Thoughtful subnet planning is essential for secure, scalable, and manageable enterprise networks.

