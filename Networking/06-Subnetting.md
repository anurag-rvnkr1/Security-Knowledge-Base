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

# 06 - Subnetting

# Part 2 — Manual Subnet Calculations, Magic Number Method, Binary Subnetting, and Interview Techniques

---

# Overview

One of the most frequently tested networking skills in technical interviews is **manual subnet calculation**.

Although subnet calculators exist, network engineers and cybersecurity professionals should understand how subnetting works without relying on tools.

This section explains:

- Binary subnet calculations
- Network address calculation
- Broadcast address calculation
- First and last usable host
- Block size (Magic Number) method
- Fast interview techniques
- Common subnet examples

---

# Steps for Manual Subnetting

Whenever you receive an IP address and subnet mask, answer these questions:

```
1. What is the Network Address?

↓

2. What is the Broadcast Address?

↓

3. What is the First Host?

↓

4. What is the Last Host?

↓

5. How many Usable Hosts exist?
```

Following the same process every time helps avoid mistakes.

---

# Example

```
IP Address

192.168.10.75

Subnet

/26
```

Our objective is to determine:

- Network
- Broadcast
- Host range
- Number of hosts

---

# CIDR to Subnet Mask

A prefix length represents the number of network bits.

| CIDR | Subnet Mask |
|------|-------------|
| /24 | 255.255.255.0 |
| /25 | 255.255.255.128 |
| /26 | 255.255.255.192 |
| /27 | 255.255.255.224 |
| /28 | 255.255.255.240 |
| /29 | 255.255.255.248 |
| /30 | 255.255.255.252 |

Always convert the CIDR prefix into its subnet mask before calculating.

---

# Binary View of /26

Subnet mask:

```
255.255.255.192
```

Binary:

```
11111111

11111111

11111111

11000000
```

Meaning:

```
26 Network Bits

↓

6 Host Bits
```

---

# Host Calculation

Formula:

```
2^(Host Bits) − 2
```

For:

```
/26
```

Host bits:

```
6
```

Calculation:

```
2⁶ − 2

=

64 − 2

=

62 Hosts
```

---

# Number of Subnets

Formula:

```
2^(Borrowed Bits)
```

Example:

Original network:

```
/24
```

Converted to:

```
/26
```

Borrowed bits:

```
2
```

Calculation:

```
2²

=

4 Subnets
```

---

# The Magic Number Method

The **Magic Number** (also called the block size) is the fastest manual subnetting technique.

Formula:

```
256 − Interesting Octet
```

For:

```
255.255.255.192
```

Interesting octet:

```
192
```

Calculation:

```
256 − 192

=

64
```

Therefore, subnet boundaries occur every:

```
64 Addresses
```

---

# Example — /26

Magic number:

```
64
```

Subnet ranges:

```
0

64

128

192
```

Resulting networks:

```
192.168.10.0

192.168.10.64

192.168.10.128

192.168.10.192
```

---

# Finding the Correct Subnet

Given:

```
192.168.10.75/26
```

Subnet boundaries:

```
0

64

128

192
```

The address:

```
75
```

Falls between:

```
64

↓

127
```

Therefore:

Network:

```
192.168.10.64
```

---

# Broadcast Address

Broadcast is always:

```
Next Network

−1
```

Next network:

```
192.168.10.128
```

Broadcast:

```
192.168.10.127
```

---

# First Host

```
Network

+

1
```

Result:

```
192.168.10.65
```

---

# Last Host

```
Broadcast

−1
```

Result:

```
192.168.10.126
```

---

# Final Answer

Given:

```
192.168.10.75/26
```

| Item | Value |
|------|-------|
| Network | 192.168.10.64 |
| Broadcast | 192.168.10.127 |
| First Host | 192.168.10.65 |
| Last Host | 192.168.10.126 |
| Hosts | 62 |

---

# Worked Example — /25

Given:

```
192.168.1.140/25
```

Subnet mask:

```
255.255.255.128
```

Magic number:

```
256 − 128

=

128
```

Subnet boundaries:

```
0

128
```

Address:

```
140
```

Falls in:

```
128–255
```

Results:

| Item | Value |
|------|-------|
| Network | 192.168.1.128 |
| Broadcast | 192.168.1.255 |
| First Host | 192.168.1.129 |
| Last Host | 192.168.1.254 |
| Hosts | 126 |

---

# Worked Example — /27

Given:

```
192.168.5.90/27
```

Subnet mask:

```
255.255.255.224
```

Magic number:

```
256 − 224

=

32
```

Subnet boundaries:

```
0

32

64

96

128

160

192

224
```

The address:

```
90
```

Falls between:

```
64–95
```

Results:

| Item | Value |
|------|-------|
| Network | 192.168.5.64 |
| Broadcast | 192.168.5.95 |
| First Host | 192.168.5.65 |
| Last Host | 192.168.5.94 |
| Hosts | 30 |

---

# Worked Example — /28

Given:

```
10.20.30.150/28
```

Subnet mask:

```
255.255.255.240
```

Magic number:

```
16
```

Boundaries:

```
0

16

32

48

64

80

96

112

128

144

160

...
```

Address:

```
150
```

Falls inside:

```
144–159
```

Results:

| Item | Value |
|------|-------|
| Network | 10.20.30.144 |
| Broadcast | 10.20.30.159 |
| First Host | 10.20.30.145 |
| Last Host | 10.20.30.158 |
| Hosts | 14 |

---

# Worked Example — /29

Magic number:

```
8
```

Hosts:

```
6
```

Example:

```
192.168.10.203/29
```

Boundaries:

```
192

200

208
```

Results:

| Item | Value |
|------|-------|
| Network | 192.168.10.200 |
| Broadcast | 192.168.10.207 |
| First Host | 192.168.10.201 |
| Last Host | 192.168.10.206 |

---

# Worked Example — /30

Subnet mask:

```
255.255.255.252
```

Magic number:

```
4
```

Hosts:

```
2
```

Example:

```
172.16.1.53/30
```

Boundaries:

```
48

52

56
```

Result:

| Item | Value |
|------|-------|
| Network | 172.16.1.52 |
| Broadcast | 172.16.1.55 |
| First Host | 172.16.1.53 |
| Last Host | 172.16.1.54 |

Common use:

- Point-to-point WAN links
- Router interconnections

---

# Special Prefix — /31

According to **RFC 3021**, `/31` networks can be used for point-to-point links.

Characteristics:

- Two addresses
- No traditional network/broadcast reservation
- Efficient use of address space

Example:

```
10.1.1.0/31

↓

10.1.1.0

10.1.1.1
```

---

# Special Prefix — /32

A `/32` identifies a **single host**.

Example:

```
192.168.10.25/32
```

Common uses:

- Loopback interfaces
- Firewall rules
- Routing policies
- Host-specific routes

---

# Quick Reference Table

| Prefix | Hosts | Block Size |
|---------|------:|-----------:|
| /24 | 254 | 256 |
| /25 | 126 | 128 |
| /26 | 62 | 64 |
| /27 | 30 | 32 |
| /28 | 14 | 16 |
| /29 | 6 | 8 |
| /30 | 2 | 4 |
| /31 | 2 (Point-to-Point) | 2 |
| /32 | 1 | 1 |

---

# Fast Interview Shortcut

Instead of converting every address to binary:

1. Find the subnet mask.
2. Calculate the magic number.
3. List subnet boundaries.
4. Locate the IP address.
5. Determine:
   - Network
   - Broadcast
   - First host
   - Last host

This method is widely used by experienced network engineers and is often sufficient for interview calculations.

---

# Common Interview Mistakes

| Mistake | Result |
|----------|--------|
| Using the wrong subnet boundary | Incorrect network address |
| Forgetting the broadcast address | Incorrect host range |
| Counting network/broadcast as usable hosts | Wrong host count |
| Mixing CIDR and subnet masks | Incorrect calculations |
| Ignoring `/31` behavior | Incorrect point-to-point design |

---

# Practice Questions

### Question 1

```
192.168.20.170/27
```

Find:

- Network
- Broadcast
- First host
- Last host

---

### Question 2

```
10.10.15.90/28
```

Calculate:

- Network
- Broadcast
- Usable hosts

---

### Question 3

```
172.20.30.101/26
```

Determine:

- Network
- Broadcast
- Host range

> **Tip:** Solve these manually before checking with a calculator to strengthen your understanding.

---

# Key Takeaways

- Manual subnetting follows a repeatable five-step process.
- The **Magic Number (Block Size)** method is faster than binary conversion for most interview scenarios.
- Network address = first address in the subnet.
- Broadcast address = last address in the subnet.
- First and last usable hosts are immediately after the network address and immediately before the broadcast address.
- `/31` and `/32` have specialized purposes and are important for enterprise routing and security.

# 06 - Subnetting

# Part 3 — Variable Length Subnet Masking (VLSM), Route Summarization, Longest Prefix Match, and Enterprise Network Design

---

# Overview

In real-world enterprise environments, not every network requires the same number of IP addresses.

For example:

- A data center server network may require only **30 hosts**.
- A user VLAN may require **500 hosts**.
- A point-to-point router link requires only **2 hosts**.

Using one subnet size for every network wastes valuable IPv4 addresses.

To solve this problem, organizations use **Variable Length Subnet Masking (VLSM)**.

---

# What is VLSM?

**Variable Length Subnet Masking (VLSM)** is the practice of assigning different subnet sizes to different networks based on their actual host requirements.

Instead of dividing a network into equal-sized subnets, VLSM creates subnets of varying sizes.

Example:

```
10.10.0.0/16

↓

HR

/24

↓

IT

/23

↓

Servers

/27

↓

WAN Link

/31
```

Each subnet is sized according to the number of devices it must support.

---

# Why Do We Need VLSM?

Consider an organization with four departments:

| Department | Required Hosts |
|------------|---------------:|
| HR | 200 |
| Finance | 50 |
| Servers | 20 |
| WAN Link | 2 |

If every department receives a `/24` subnet:

| Department | Allocated Hosts | Used Hosts | Wasted Hosts |
|------------|----------------:|-----------:|-------------:|
| HR | 254 | 200 | 54 |
| Finance | 254 | 50 | 204 |
| Servers | 254 | 20 | 234 |
| WAN | 254 | 2 | 252 |

Most of the available address space remains unused.

VLSM minimizes this waste.

---

# VLSM Design Process

A common design approach is:

```
1. List Host Requirements

↓

2. Sort Largest → Smallest

↓

3. Assign Largest Subnet First

↓

4. Continue Until Complete

↓

5. Reserve Space for Future Growth
```

Allocating the largest networks first reduces fragmentation and simplifies future expansion.

---

# Enterprise Example

Available network:

```
192.168.10.0/24
```

Requirements:

| Network | Hosts Needed |
|----------|-------------:|
| HR | 100 |
| IT | 50 |
| Servers | 25 |
| Printers | 10 |
| WAN | 2 |

---

# Step 1 — Largest Requirement

HR needs:

```
100 Hosts
```

Required subnet:

```
/25

126 Hosts
```

Assignment:

```
192.168.10.0/25
```

Host range:

```
192.168.10.1

↓

192.168.10.126
```

---

# Step 2 — IT

Remaining space begins at:

```
192.168.10.128
```

Requirement:

```
50 Hosts
```

Subnet:

```
/26

62 Hosts
```

Assignment:

```
192.168.10.128/26
```

---

# Step 3 — Servers

Requirement:

```
25 Hosts
```

Subnet:

```
/27

30 Hosts
```

Assignment:

```
192.168.10.192/27
```

---

# Step 4 — Printers

Requirement:

```
10 Hosts
```

Subnet:

```
/28

14 Hosts
```

Assignment:

```
192.168.10.224/28
```

---

# Step 5 — WAN Link

Requirement:

```
2 Hosts
```

Subnet:

```
/31

(Point-to-Point)
```

Assignment:

```
192.168.10.240/31
```

Remaining address space can be reserved for future expansion or additional infrastructure.

---

# Final VLSM Plan

| Network | Prefix | Host Capacity |
|----------|--------|--------------:|
| HR | /25 | 126 |
| IT | /26 | 62 |
| Servers | /27 | 30 |
| Printers | /28 | 14 |
| WAN | /31 | 2 |

This approach uses address space efficiently while allowing room for growth.

---

# Advantages of VLSM

- Efficient IPv4 utilization
- Smaller routing tables
- Better scalability
- Reduced address waste
- Flexible enterprise design
- Easier future expansion

---

# Disadvantages

- More planning required
- Increased configuration complexity
- Documentation becomes critical
- Incorrect planning may cause overlapping subnets

---

# What is Route Summarization?

Route Summarization (also called **Route Aggregation** or **Supernetting**) combines multiple contiguous networks into a single summarized route.

Instead of advertising many individual routes:

```
10.10.0.0/24

10.10.1.0/24

10.10.2.0/24

10.10.3.0/24
```

We advertise:

```
10.10.0.0/22
```

This reduces routing table size and improves routing efficiency.

---

# Benefits of Route Summarization

- Smaller routing tables
- Faster route lookup
- Lower CPU usage
- Reduced memory consumption
- Faster convergence
- Improved scalability

These benefits are especially important in large enterprise and service provider networks.

---

# Supernetting Example

Individual routes:

```
192.168.4.0/24

192.168.5.0/24

192.168.6.0/24

192.168.7.0/24
```

Summary:

```
192.168.4.0/22
```

A summarized route should only be created when the component networks are contiguous and share a common prefix.

---

# Longest Prefix Match (LPM)

Routers use the **Longest Prefix Match** rule when multiple routes match the destination.

Example routing table:

| Route | Prefix |
|--------|--------|
| 10.0.0.0/8 | Broad route |
| 10.10.0.0/16 | More specific |
| 10.10.10.0/24 | Most specific |

Destination:

```
10.10.10.25
```

Matching routes:

```
/8

↓

/16

↓

/24
```

The router selects:

```
10.10.10.0/24
```

because it has the **longest matching prefix**.

---

# Why Longest Prefix Match Matters

Without LPM, routers could forward packets to less specific routes, resulting in inefficient or incorrect paths.

LPM ensures traffic follows the most precise routing information available.

---

# Enterprise Routing Example

```
                     Core Router
                         │
      ┌──────────────────┼──────────────────┐
      │                  │                  │
10.10.0.0/22       10.20.0.0/22      10.30.0.0/22
      │                  │                  │
   HR / IT          Finance / Sales      Data Center
```

Each summarized route represents multiple smaller departmental subnets.

---

# Cloud Subnetting

Cloud providers also rely on subnetting for workload isolation.

---

## AWS Example

```
VPC

10.0.0.0/16

├──────────────┐
│              │
Public

10.0.1.0/24

Private

10.0.2.0/24
```

Public subnets typically host:

- Load balancers
- Bastion hosts
- NAT Gateways

Private subnets typically host:

- Application servers
- Databases
- Internal services

---

## Azure Example

```
Virtual Network

↓

Subnet A

↓

Subnet B

↓

Gateway Subnet
```

Azure reserves certain IP addresses within every subnet for platform use.

---

## Google Cloud Example

```
VPC

↓

Regional Subnet

↓

Compute Engine

↓

Managed Services
```

Google Cloud uses regional subnets that can span multiple availability zones within the same region.

---

# Enterprise Design Best Practices

- Allocate addresses hierarchically.
- Reserve space for future growth.
- Separate users, servers, management, and guest networks.
- Use route summarization wherever practical.
- Avoid overlapping address ranges.
- Document all allocations in IPAM.
- Standardize subnet sizes where operationally beneficial.

---

# Common VLSM Mistakes

| Mistake | Result |
|----------|--------|
| Allocating small networks first | Address fragmentation |
| Overlapping subnets | Routing conflicts |
| Ignoring growth | Frequent redesign |
| No documentation | Operational errors |
| Incorrect summarization | Traffic black holes |

---

# Practice Scenario

Available network:

```
172.16.0.0/24
```

Requirements:

| Department | Hosts |
|------------|------:|
| Sales | 120 |
| HR | 50 |
| IT | 20 |
| Guest Wi-Fi | 10 |
| WAN Link | 2 |

Exercise:

1. Sort the requirements from largest to smallest.
2. Allocate appropriate subnet sizes.
3. Determine network, broadcast, and usable host ranges.
4. Reserve any remaining address space for future use.

---

# Key Takeaways

- VLSM allocates subnet sizes based on actual host requirements, reducing IPv4 address waste.
- Plan from the largest network to the smallest to simplify allocation and future expansion.
- Route summarization combines contiguous networks into larger prefixes, reducing routing table size.
- Routers always use the **Longest Prefix Match (LPM)** when selecting routes.
- Cloud platforms such as AWS, Azure, and Google Cloud rely heavily on subnetting for network segmentation and security.
- Proper VLSM design and route summarization improve scalability, performance, and operational efficiency in enterprise environments.

