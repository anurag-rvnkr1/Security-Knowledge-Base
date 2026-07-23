# 05 - IP Addressing

# Part 1 — IP Address Fundamentals, IPv4, IPv6, Address Types, and Enterprise Network Design

---

# Overview

Every device connected to a network requires an address so that other devices know where to send data.

This address is called an **Internet Protocol (IP) Address**.

Unlike MAC addresses, which identify devices on a local network, IP addresses provide **logical addressing** that enables communication across different networks and the Internet.

Every modern network depends on IP addressing, including:

- Enterprise LANs
- Cloud environments
- Data centers
- Mobile networks
- Home networks
- Internet Service Providers (ISPs)
- Industrial Control Systems (ICS)
- Internet of Things (IoT)

Understanding IP addressing is fundamental for:

- Network Engineers
- Cloud Engineers
- Cybersecurity Analysts
- SOC Analysts
- Penetration Testers
- DevOps Engineers
- System Administrators

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain the purpose of IP addressing.
- Differentiate IPv4 and IPv6.
- Understand logical addressing.
- Distinguish public and private IP addresses.
- Identify special-purpose IP addresses.
- Understand address assignment methods.
- Design enterprise IP addressing schemes.
- Analyze IP traffic in Wireshark.

---

# What is an IP Address?

An **IP Address** is a logical identifier assigned to a network interface.

It enables devices to:

- Identify themselves
- Locate other devices
- Send packets across networks
- Receive packets from remote hosts

Think of an IP address as a postal address.

```
House

↓

Street

↓

City

↓

Country
```

Similarly,

```
Application

↓

Device

↓

IP Address

↓

Network

↓

Internet
```

Without IP addresses, routers would not know where to forward packets.

---

# Why Do We Need IP Addresses?

Suppose two computers communicate.

```
PC A

↓

?

↓

PC B
```

Without logical addressing:

- Routers cannot determine packet destinations.
- Multiple interconnected networks cannot communicate.
- Internet communication becomes impossible.

IP addresses provide globally understood logical identifiers that allow routing decisions to be made.

---

# Logical Address vs Physical Address

| Feature | IP Address | MAC Address |
|----------|------------|-------------|
| Layer | Network (Layer 3) | Data Link (Layer 2) |
| Purpose | Routing between networks | Local delivery within a LAN |
| Assigned By | Administrator or DHCP | Manufacturer (typically) |
| Changes? | Can change | Usually remains constant |
| Scope | Network-wide / Internet | Local network segment |

Both addresses work together during communication:

```
Destination IP

↓

Routing

↓

Destination MAC

↓

Local Delivery
```

---

# Internet Protocol Versions

Two versions are widely used today:

- IPv4
- IPv6

```
Internet Protocol

↓

IPv4

↓

IPv6
```

Both provide logical addressing, but they differ significantly in address size, notation, and capabilities.

---

# IPv4

IPv4 is the fourth version of the Internet Protocol and remains the most widely deployed.

### Address Size

```
32 Bits
```

### Representation

```
192.168.1.100
```

The address is divided into four octets.

```
192

168

1

100
```

Each octet ranges from:

```
0–255
```

---

# Binary Representation

Example:

```
192.168.1.10
```

Binary:

```
11000000

10101000

00000001

00001010
```

Routers and hosts process addresses in binary even though humans typically use dotted-decimal notation.

---

# IPv4 Structure

```
32 Bits

↓

8

↓

8

↓

8

↓

8
```

Example

```
192

168

10

15
```

Each octet contains exactly 8 bits.

---

# IPv6

IPv6 was developed to address the limitations of IPv4, particularly address exhaustion.

### Address Size

```
128 Bits
```

Example:

```
2001:db8:abcd:1234::100
```

IPv6 uses hexadecimal notation and colon-separated groups.

---

# Why IPv6 Was Developed

IPv4 provides approximately:

```
4.29 Billion Addresses
```

Due to the growth of:

- Smartphones
- Cloud computing
- IoT
- Data centers
- Enterprise networks

the available IPv4 address space became insufficient.

IPv6 offers an extremely large address space capable of supporting current and future Internet growth.

---

# IPv4 vs IPv6

| Feature | IPv4 | IPv6 |
|----------|------|------|
| Address Size | 32 bits | 128 bits |
| Notation | Decimal | Hexadecimal |
| Address Space | ~4.29 billion | Approximately 3.4 × 10³⁸ addresses |
| Header Size | Variable (20–60 bytes) | Fixed (40 bytes) |
| Broadcast | Supported | Not supported (uses multicast and anycast instead) |
| NAT Usage | Common | Often unnecessary, though it may still be deployed in some environments |

---

# Types of IP Addresses

IP addresses can be categorized by their scope and intended use.

Common categories include:

- Public
- Private
- Loopback
- Link-Local
- Multicast
- Anycast (primarily IPv6, but also used in routing architectures)
- Broadcast (IPv4 only)

---

# Public IP Address

Public IP addresses are globally routable on the Internet.

Example:

```
203.0.113.25
```

Characteristics:

- Assigned by an ISP or Regional Internet Registry (RIR)
- Globally unique
- Reachable over the public Internet (subject to routing and security policies)

Typical uses:

- Web servers
- VPN gateways
- Cloud services
- Public APIs

---

# Private IP Addresses

Private addresses are reserved for internal networks and are **not routable on the public Internet**.

RFC 1918 private IPv4 ranges:

| Range | CIDR |
|--------|------|
| 10.0.0.0 – 10.255.255.255 | 10.0.0.0/8 |
| 172.16.0.0 – 172.31.255.255 | 172.16.0.0/12 |
| 192.168.0.0 – 192.168.255.255 | 192.168.0.0/16 |

Example:

```
192.168.1.50
```

Private addresses require technologies such as **NAT** to communicate with the public Internet.

---

# Loopback Address

Loopback enables a host to communicate with itself.

IPv4:

```
127.0.0.1
```

IPv6:

```
::1
```

Common uses:

- Local testing
- Application development
- Service verification

---

# Link-Local Addresses

A link-local address allows communication within the same local network segment without requiring a router.

### IPv4 (Automatic Private IP Addressing - APIPA)

```
169.254.0.0/16
```

### IPv6

```
FE80::/10
```

Typical uses:

- Automatic addressing when DHCP is unavailable
- Neighbor discovery
- Local communication

---

# Broadcast Address (IPv4)

A broadcast address reaches every host within the local broadcast domain.

Example:

```
192.168.1.255
```

Used for:

- ARP-related communication (at Layer 2)
- Service discovery
- Legacy protocols

IPv6 replaces broadcast functionality with multicast.

---

# Multicast Address

Multicast delivers traffic to a selected group of receivers.

### IPv4

```
224.0.0.0/4
```

### IPv6

```
FF00::/8
```

Examples:

- IPTV
- Video conferencing
- Routing protocols
- Streaming services

---

# Enterprise IP Addressing Example

```
                Internet
                    │
            Public IP Address
                    │
              Edge Firewall
                    │
          10.0.0.0/8 Enterprise LAN
          ├──────────┬──────────┐
          │          │          │
     HR VLAN    IT VLAN    Server VLAN
     10.10.10.0 10.20.20.0 10.30.30.0
```

Benefits include:

- Improved scalability
- Simplified troubleshooting
- Security segmentation
- Easier routing
- Efficient IP management

---

# Common Address Assignment Methods

## Static Addressing

An administrator manually configures the IP address.

Typical uses:

- Servers
- Routers
- Firewalls
- Network appliances

---

## Dynamic Addressing

A DHCP server automatically assigns addresses.

Typical uses:

- User workstations
- Laptops
- Mobile devices
- Guest networks

---

# Wireshark Observation

In Wireshark, selecting an IPv4 or IPv6 packet reveals fields such as:

```
Source IP

↓

Destination IP

↓

Protocol

↓

TTL / Hop Limit
```

These fields help analysts trace communication paths and investigate network activity.

---

# Business Impact

Proper IP addressing enables:

- Reliable routing
- Enterprise scalability
- Cloud connectivity
- Secure network segmentation
- High availability
- Efficient troubleshooting
- Consistent network management

Poor IP planning can result in address conflicts, routing issues, and operational downtime.

---

# Key Takeaways

- IP addresses provide logical identification for devices across networks.
- IPv4 uses 32-bit addresses, while IPv6 uses 128-bit addresses.
- Public addresses are Internet-routable, whereas private addresses are intended for internal use.
- Special-purpose addresses include loopback, link-local, multicast, and broadcast (IPv4).
- Well-designed IP addressing schemes are fundamental to secure, scalable enterprise networks.

# 05 - IP Addressing

# Part 2 — IPv4 Addressing, Binary Representation, Address Classes, CIDR Introduction, and Enterprise Address Planning

---

# Overview

IPv4 remains the most widely deployed Internet Protocol despite the adoption of IPv6.

Understanding IPv4 addressing is essential because almost every enterprise network still uses IPv4 internally, and many Internet-facing services continue to support it.

This section explains:

- IPv4 address structure
- Binary representation
- Network ID vs Host ID
- Classful addressing
- Classless Inter-Domain Routing (CIDR) basics
- Special IPv4 ranges
- Enterprise addressing strategies

---

# IPv4 Address Structure

An IPv4 address contains:

```
32 Bits
```

These bits are divided into:

```
8 Bits

↓

8 Bits

↓

8 Bits

↓

8 Bits
```

Example

```
192.168.10.25
```

Each group is called an **octet**.

---

# Binary Representation

Computers process IP addresses as binary values.

Example:

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

Each octet consists of eight binary digits (bits).

---

# Binary Place Values

Each bit represents a power of two.

```
128

64

32

16

8

4

2

1
```

Example

```
11000000

↓

128 + 64

↓

192
```

Another example:

```
00011001

↓

16 + 8 + 1

↓

25
```

Understanding binary conversion is fundamental for subnetting and routing.

---

# Converting Binary to Decimal

Example:

```
11111111
```

Calculation:

```
128 + 64 + 32 + 16 + 8 + 4 + 2 + 1

=

255
```

Example:

```
00101010
```

Calculation:

```
32 + 8 + 2

=

42
```

---

# Converting Decimal to Binary

Example:

```
150
```

Binary:

```
128 + 16 + 4 + 2

↓

10010110
```

Another example:

```
75
```

Binary:

```
64 + 8 + 2 + 1

↓

01001011
```

---

# Network ID and Host ID

Every IPv4 address contains two logical parts:

```
Network Portion

+

Host Portion
```

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

The subnet mask (or prefix length) determines where the network portion ends and the host portion begins.

---

# Why Separate Network and Host?

Routers forward traffic based on the **network portion**.

Hosts communicate using the **host portion** within that network.

Example:

```
Network

192.168.10.0

↓

Hosts

192.168.10.1

192.168.10.2

192.168.10.100
```

---

# Classful Addressing

Historically, IPv4 addresses were divided into fixed classes.

Although modern networks use CIDR, understanding classful addressing remains useful for interviews and legacy systems.

---

# Class A

```
First Octet

1–126
```

Default Mask

```
255.0.0.0

/

8
```

Structure

```
Network

Host

Host

Host
```

Example

```
10.20.30.40
```

Large organizations historically used Class A networks because they supported a very large number of hosts.

---

# Class B

First Octet

```
128–191
```

Default Mask

```
255.255.0.0

/

16
```

Structure

```
Network

Network

Host

Host
```

Example

```
172.16.25.10
```

---

# Class C

First Octet

```
192–223
```

Default Mask

```
255.255.255.0

/

24
```

Structure

```
Network

Network

Network

Host
```

Example

```
192.168.10.50
```

---

# Class D

Range

```
224–239
```

Purpose

```
Multicast
```

Examples:

- IPTV
- Routing protocols
- Video conferencing

---

# Class E

Range

```
240–255
```

Purpose

Reserved for experimental and future use.

Generally not assigned to end hosts.

---

# Class Summary

| Class | First Octet | Default Prefix | Typical Purpose |
|--------|-------------|----------------|-----------------|
| A | 1–126 | /8 | Very large networks (historically) |
| B | 128–191 | /16 | Medium-sized networks (historically) |
| C | 192–223 | /24 | Smaller networks (historically) |
| D | 224–239 | N/A | Multicast |
| E | 240–255 | N/A | Experimental |

> Modern networks typically use CIDR rather than fixed address classes, but these ranges remain useful for understanding address allocation history.

---

# Reserved IPv4 Addresses

Certain addresses have special meanings.

---

## Network Address

Represents the network itself.

Example:

```
192.168.1.0/24
```

Cannot be assigned to a host.

---

## Broadcast Address

Represents every device within the subnet.

Example:

```
192.168.1.255
```

Cannot be assigned to a host.

---

## Default Route

```
0.0.0.0
```

Represents:

```
Unknown Network

↓

Default Gateway
```

---

## Loopback

```
127.0.0.1
```

Communication with the local device.

---

## APIPA

```
169.254.0.0/16
```

Automatically assigned when a DHCP server is unavailable.

---

## Private Networks

RFC 1918 ranges:

```
10.0.0.0/8

172.16.0.0/12

192.168.0.0/16
```

---

# Public vs Private Addressing

Example Enterprise Network

```
Internet

↓

Public

198.51.100.20

↓

Firewall

↓

NAT

↓

Private

10.20.30.40
```

Benefits of private addressing:

- Conserves public IPv4 addresses
- Simplifies internal addressing
- Supports network segmentation
- Works with NAT for Internet access

---

# Address Exhaustion

IPv4 supports approximately:

```
4,294,967,296

Addresses
```

However, not all addresses are available for general use because some are reserved or allocated for special purposes.

Rapid growth in:

- Mobile devices
- Cloud computing
- IoT
- Enterprise expansion

led to IPv4 address exhaustion.

Solutions include:

- CIDR
- NAT
- IPv6 deployment

---

# Introduction to CIDR

CIDR stands for:

```
Classless Inter-Domain Routing
```

Instead of relying on fixed address classes, CIDR uses a **prefix length**.

Example:

```
192.168.10.25

/

24
```

The `/24` indicates that the first 24 bits identify the network.

Advantages:

- Flexible address allocation
- Reduced address waste
- More efficient routing
- Better scalability

A deeper exploration of CIDR and subnetting will follow in the dedicated subnetting chapter.

---

# Enterprise IP Allocation Example

```
Corporate Network

10.0.0.0/8

├──────────────┐
│              │
HR        10.10.10.0/24
IT        10.20.20.0/24
Finance   10.30.30.0/24
Servers   10.40.40.0/24
Guest Wi-Fi 10.50.50.0/24
```

Benefits:

- Clear separation of departments
- Simplified routing
- Easier security policy enforcement
- Better scalability

---

# Wireshark Observation

Select an IPv4 packet and inspect:

```
Version

↓

Header Length

↓

Total Length

↓

Identification

↓

TTL

↓

Protocol

↓

Source IP

↓

Destination IP
```

These fields are essential for troubleshooting connectivity and investigating network incidents.

---

# Common IPv4 Addressing Problems

| Problem | Possible Cause |
|----------|----------------|
| Duplicate IP Address | Static configuration conflict or DHCP issue |
| Incorrect Subnet Mask | Hosts believe they are on different networks |
| Wrong Default Gateway | Unable to reach remote networks |
| APIPA Address | DHCP server unavailable |
| IP Address Conflict | Two devices configured with the same address |
| Routing Failure | Incorrect network configuration or missing route |

---

# Business Impact

Proper IPv4 planning enables:

- Efficient routing
- Reduced address conflicts
- Easier troubleshooting
- Improved scalability
- Better security segmentation
- Simplified network management

Poor IP planning can lead to downtime, connectivity issues, and operational inefficiencies.

---

# Key Takeaways

- IPv4 uses 32-bit logical addresses represented in dotted-decimal notation.
- Each address contains a network portion and a host portion.
- Historical classful addressing divided addresses into Classes A through E, but modern networks use CIDR.
- Special-purpose addresses include network, broadcast, loopback, APIPA, and private ranges.
- Careful IPv4 address planning is essential for secure, scalable, and manageable enterprise networks.

