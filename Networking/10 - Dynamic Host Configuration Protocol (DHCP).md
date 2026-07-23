# 10 - Dynamic Host Configuration Protocol (DHCP)

# Part 1 — DHCP Fundamentals, Architecture, DORA Process, Lease Allocation, and Enterprise Operations

---

# Overview

Modern enterprise networks may contain **thousands to millions of devices** including:

- Employee laptops
- Desktop computers
- Servers
- Mobile devices
- Printers
- IP phones
- Security cameras
- IoT devices
- Virtual machines
- Containers
- Cloud workloads

Manually assigning an IP address to every device would be:

- Time-consuming
- Error-prone
- Difficult to scale
- Expensive to manage

To solve this problem, organizations use the **Dynamic Host Configuration Protocol (DHCP)**.

DHCP automatically provides network configuration to clients, allowing devices to join a network with minimal manual intervention.

---

# Learning Objectives

After completing this chapter, you should be able to:

- Explain the purpose of DHCP.
- Understand DHCP architecture.
- Describe the DORA process.
- Explain DHCP lease allocation.
- Understand DHCP scopes and pools.
- Differentiate static and dynamic addressing.
- Understand enterprise DHCP deployment.
- Troubleshoot common DHCP issues.

---

# What is DHCP?

**Dynamic Host Configuration Protocol (DHCP)** is an application-layer protocol that automatically assigns IP configuration information to network devices.

Typical information includes:

- IPv4 address
- Subnet mask
- Default gateway
- DNS server
- Domain name
- Lease duration
- Additional DHCP options

Instead of configuring every device manually, a DHCP server supplies these values automatically.

---

# Why DHCP is Important

Without DHCP:

```
Administrator

↓

Configure Every Device

↓

Manual IP Assignment
```

With DHCP:

```
Client

↓

DHCP Request

↓

DHCP Server

↓

Automatic Configuration
```

Benefits include:

- Faster deployment
- Simplified administration
- Centralized management
- Reduced configuration errors
- Better scalability

---

# Evolution of DHCP

Before DHCP, many networks used **BOOTP (Bootstrap Protocol)**.

BOOTP allowed devices to obtain basic network information but lacked flexible lease management.

DHCP extended BOOTP by introducing:

- Dynamic address allocation
- Lease timers
- Automatic renewal
- Expanded configuration options

Modern DHCP implementations remain compatible with many BOOTP concepts while providing significantly greater functionality.

---

# DHCP Architecture

A DHCP deployment typically consists of:

```
Client

↓

Access Switch

↓

Router (Optional)

↓

DHCP Server
```

The client requests configuration, while the DHCP server allocates addressing information.

---

# DHCP Components

## DHCP Client

The client is any device requesting configuration.

Examples:

- Windows workstation
- Linux server
- IP phone
- Wireless laptop
- Printer
- Virtual machine

---

## DHCP Server

The DHCP server maintains:

- Address pools
- Lease database
- Reservations
- Configuration options
- Scope information

The server determines which IP address is assigned to each client.

---

## Relay Agent (Optional)

When clients and servers reside on different networks, a **DHCP Relay Agent** forwards DHCP messages across routers.

Example:

```
Client

↓

Access Switch

↓

Router (Relay)

↓

DHCP Server
```

Without a relay agent, DHCP broadcasts normally do not cross routers.

---

# DHCP Ports

DHCP uses UDP.

| Device | Port |
|----------|------|
| Client | UDP 68 |
| Server | UDP 67 |

Communication occurs over:

```
UDP

67

↓

68
```

---

# DHCP Address Allocation Methods

DHCP supports multiple allocation strategies.

## Dynamic Allocation

Addresses are leased temporarily.

Example:

```
Pool

↓

192.168.10.100

↓

Assigned

↓

Lease Expires

↓

Returned to Pool
```

This is the most common enterprise deployment.

---

## Automatic Allocation

The first assigned address is permanently associated with the client until manually changed by the administrator.

---

## Manual Allocation (Reservation)

Specific MAC addresses receive predefined IP addresses.

Example:

```
MAC

↓

00:11:22:33:44:55

↓

Always Receives

↓

192.168.10.10
```

Typical use cases:

- Printers
- Servers
- Firewalls
- Network appliances
- IP cameras

---

# DHCP Scope

A **scope** defines the range of addresses available for assignment.

Example:

```
Scope

192.168.10.100

↓

192.168.10.200
```

The DHCP server leases addresses only from this configured range unless reservations or exclusions apply.

---

# Exclusion Range

Certain addresses should never be leased dynamically.

Example:

```
Reserved

192.168.10.1

↓

Gateway

──────────────

192.168.10.2

↓

Firewall

──────────────

192.168.10.3

↓

Core Switch
```

These addresses are excluded from the dynamic pool.

---

# DHCP Lease

A **lease** is the temporary assignment of an IP address to a client.

Example:

```
Assigned

↓

192.168.10.120

↓

Lease

↓

8 Hours
```

At lease expiration, the address may be renewed or returned to the available pool.

---

# Lease Database

The DHCP server maintains a database containing:

- Client MAC address
- Assigned IP address
- Lease start time
- Lease expiration
- Hostname (if provided)
- Reservation status

This database prevents duplicate assignments and tracks active clients.

---

# The DORA Process

DHCP uses a four-step exchange known as **DORA**:

```
Discover

↓

Offer

↓

Request

↓

Acknowledge
```

This sequence allows clients to obtain valid network configuration.

---

# Step 1 — DHCP Discover

A new client does not yet have an IP address.

It broadcasts a discovery message:

```
DHCP Discover

↓

Broadcast

↓

Looking for DHCP Server
```

Since the client lacks an address, it cannot send a unicast request to a known server.

---

# Step 2 — DHCP Offer

One or more DHCP servers may respond with an offer.

Example:

```
DHCP Server

↓

Offer

↓

192.168.10.115
```

The offer typically includes:

- Proposed IP address
- Subnet mask
- Gateway
- Lease duration
- DNS servers

---

# Step 3 — DHCP Request

The client selects one offer and broadcasts a request indicating the chosen server and requested address.

```
Client

↓

DHCP Request

↓

I Accept

192.168.10.115
```

Other DHCP servers withdraw any outstanding offers.

---

# Step 4 — DHCP Acknowledgment (ACK)

The selected server confirms the lease.

```
DHCP ACK

↓

Configuration Complete
```

The client configures its network interface and can begin communication.

---

# Complete DORA Workflow

```
Client

↓

DHCP Discover

↓

DHCP Server

↓

DHCP Offer

↓

Client

↓

DHCP Request

↓

DHCP Server

↓

DHCP ACK

↓

Client Configures Interface
```

---

# What Information Does DHCP Provide?

Typical configuration includes:

| Parameter | Example |
|------------|----------|
| IP Address | 192.168.10.120 |
| Subnet Mask | 255.255.255.0 |
| Default Gateway | 192.168.10.1 |
| DNS Server | 8.8.8.8 (or enterprise DNS) |
| Domain Name | corp.example.local |
| Lease Time | 8 Hours |

Additional parameters are delivered using DHCP options.

---

# DHCP Message Types

| Message | Purpose |
|----------|----------|
| Discover | Locate DHCP servers |
| Offer | Offer an IP configuration |
| Request | Request the offered address |
| ACK | Confirm lease assignment |
| NAK | Reject invalid request |
| Decline | Client reports offered address is already in use |
| Release | Client returns an address to the server |
| Inform | Client requests additional DHCP options while already configured |

---

# Broadcast vs Unicast

During initial configuration:

```
Discover

↓

Broadcast

↓

Offer

↓

Broadcast or Unicast (implementation dependent)

↓

Request

↓

Broadcast

↓

ACK

↓

Broadcast or Unicast (implementation dependent)
```

The exact behavior depends on the client state and DHCP flags.

---

# Enterprise Example

```
Employee Laptop

↓

Access Switch

↓

Distribution Switch

↓

Core Router

↓

DHCP Relay

↓

Enterprise DHCP Cluster
```

The user connects a laptop.

Within seconds, the device automatically receives:

- IP address
- Gateway
- DNS servers
- Domain suffix
- Lease information

No manual configuration is required.

---

# Common DHCP Problems

| Problem | Possible Cause |
|----------|----------------|
| No IP address | DHCP server unavailable |
| APIPA address (169.254.x.x) | DHCP request failed |
| Duplicate IP address | Misconfiguration or rogue DHCP |
| Wrong gateway | Incorrect DHCP scope options |
| No internet access | DNS or gateway configuration issue |

---

# Business Impact

Reliable DHCP services enable:

- Rapid user onboarding
- Automated endpoint provisioning
- Consistent network configuration
- Reduced administrative effort
- Improved operational efficiency
- Support for large-scale enterprise environments

A DHCP outage can prevent new devices from joining the network and disrupt normal business operations.

---

# Key Takeaways

- DHCP automatically assigns IP configuration to network devices.
- It replaces time-consuming manual IP configuration.
- DHCP uses UDP ports **67 (server)** and **68 (client)**.
- The **DORA** process consists of **Discover, Offer, Request, and Acknowledge**.
- DHCP supports dynamic, automatic, and manual (reserved) address allocation.
- Scopes, exclusions, and leases allow administrators to manage address distribution efficiently.
- DHCP is a foundational service in modern enterprise, campus, data center, and cloud-connected networks.

