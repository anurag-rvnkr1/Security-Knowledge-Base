# 19 - Linux Firewalls

# Part 1 — Firewall Fundamentals, Packet Filtering, Netfilter Architecture, Stateful Firewalls, and Linux Firewall Overview

---

# Introduction

Every Linux server connected to a network is exposed to potential threats.

Attackers constantly scan networks searching for:

- Open ports
- Vulnerable services
- Misconfigured servers
- Weak authentication
- Unpatched applications

A firewall is the **first line of network defense**, controlling which network traffic is allowed or denied.

Whether running:

- A personal Linux workstation
- A cloud virtual machine
- A Kubernetes node
- A web server
- A database server
- An enterprise data center

a properly configured firewall is essential for securing the system.

---

# Learning Objectives

After completing this chapter, you will understand:

- Firewall fundamentals
- Packet filtering
- Netfilter architecture
- Stateful firewalls
- Linux firewall frameworks
- Packet processing
- Enterprise firewall concepts
- Security best practices

---

# What is a Firewall?

A firewall is a security mechanism that monitors and controls incoming and outgoing network traffic according to predefined rules.

Its primary objectives are to:

- Allow legitimate traffic
- Block unauthorized access
- Reduce attack surface
- Enforce security policies
- Log security events

---

# Firewall Workflow

```text
Internet

↓

Incoming Packet

↓

Firewall Rules

↓

Allow?

↓

Yes ─────────► Server

↓

No

↓

Drop / Reject
```

---

# Why Firewalls Matter

Firewalls help organizations:

- Prevent unauthorized access
- Limit exposed services
- Reduce exploitation opportunities
- Enforce network segmentation
- Improve compliance
- Generate security logs
- Support incident investigations

Without a firewall, any service listening on the network may be directly reachable if routing permits.

---

# Security Layers

```text
Internet

↓

Firewall

↓

Operating System

↓

Applications

↓

Database

↓

Data
```

The firewall is one layer in a defense-in-depth strategy.

---

# Types of Firewalls

| Firewall Type | Description |
|---------------|-------------|
| Packet Filtering | Filters packets using header information |
| Stateful Firewall | Tracks connection state |
| Proxy Firewall | Acts as an intermediary between client and server |
| Application Firewall | Inspects application-layer traffic |
| Next-Generation Firewall (NGFW) | Combines filtering with advanced inspection and threat prevention |
| Host-Based Firewall | Runs directly on the endpoint |
| Network Firewall | Protects multiple systems at the network perimeter |

Linux commonly implements **host-based firewalls**.

---

# Host-Based vs Network Firewalls

| Host Firewall | Network Firewall |
|---------------|------------------|
| Protects one machine | Protects many devices |
| Installed on the OS | Dedicated appliance or gateway |
| Fine-grained per-host rules | Centralized network policy |
| Useful for cloud workloads | Useful for perimeter protection |

In enterprise environments, both are typically used together.

---

# Firewall Policies

A firewall evaluates traffic against a rule set.

Typical policies include:

| Policy | Description |
|----------|-------------|
| Allow | Permit traffic |
| Deny | Block traffic |
| Drop | Silently discard traffic |
| Reject | Refuse traffic and notify the sender when appropriate |

---

# Drop vs Reject

### Drop

```text
Packet

↓

Discard

↓

No Response
```

The sender receives no firewall-generated response.

---

### Reject

```text
Packet

↓

Reject

↓

Error Response
```

The sender receives a response such as an ICMP unreachable message or a TCP reset, depending on the protocol and configuration.

---

# Packet Filtering

Packet filtering examines packet headers.

Typical fields include:

- Source IP
- Destination IP
- Source port
- Destination port
- Protocol
- Interface
- Connection state

Based on these attributes, the firewall decides whether to allow or block the packet.

---

# Packet Flow

```text
Packet

↓

Read Header

↓

Match Rule

↓

Decision

↓

Allow

or

↓

Drop
```

---

# Firewall Rule Components

Typical rule criteria include:

| Field | Example |
|---------|----------|
| Source IP | `192.168.1.50` |
| Destination IP | `10.0.0.20` |
| Source Port | `55000` |
| Destination Port | `22` |
| Protocol | TCP |
| Interface | `eth0` |
| State | ESTABLISHED |

---

# Example Rule

Conceptually:

```text
Allow

Source:
192.168.1.0/24

Destination:
Server

Protocol:
TCP

Port:
22
```

Meaning:

Only SSH traffic from the specified subnet is permitted.

---

# Packet Filtering Advantages

- Fast
- Efficient
- Simple
- Low overhead
- Suitable for most server workloads

---

# Packet Filtering Limitations

Traditional stateless filtering:

- Does not understand sessions
- Cannot distinguish new versus established connections
- Has limited context

This led to the development of **stateful firewalls**.

---

# Stateful Firewalls

Stateful firewalls maintain a **connection tracking table**.

Instead of treating every packet independently, they understand the state of a connection.

---

# Connection Tracking

```text
Client

↓

SYN

↓

Firewall

↓

Record Connection

↓

Server

↓

SYN/ACK

↓

Firewall

↓

Allow

↓

Established Session
```

---

# Common Connection States

| State | Meaning |
|---------|----------|
| NEW | New connection attempt |
| ESTABLISHED | Existing connection |
| RELATED | Related to an existing connection (for example, certain ICMP or FTP helper traffic) |
| INVALID | Does not match a valid tracked state |

---

# Why Stateful Firewalls are Better

Stateful firewalls:

- Track active sessions
- Automatically allow return traffic for established connections
- Reduce unnecessary rules
- Improve security
- Simplify firewall management

---

# Enterprise Example

Without connection tracking:

```text
Allow Incoming

Allow Outgoing

Many Rules
```

With stateful inspection:

```text
New Connection

↓

Track State

↓

Automatically Permit Return Traffic
```

---

# Netfilter

Linux implements packet filtering through the **Netfilter** framework inside the kernel.

Netfilter is responsible for:

- Packet filtering
- Network Address Translation (NAT)
- Connection tracking
- Packet modification
- Packet mangling

User-space tools such as `iptables`, `nftables`, `firewalld`, and `ufw` interact with Netfilter.

---

# Netfilter Architecture

```text
Network Interface

↓

Kernel

↓

Netfilter

↓

Firewall Rules

↓

Decision

↓

Application
```

---

# Packet Processing Hooks

Netfilter processes packets through several hooks.

```text
Incoming Packet

↓

PREROUTING

↓

Routing Decision

↓

INPUT

↓

Local Process
```

Forwarded packets:

```text
Incoming

↓

PREROUTING

↓

FORWARD

↓

POSTROUTING

↓

Outgoing
```

Locally generated packets:

```text
Local Process

↓

OUTPUT

↓

POSTROUTING

↓

Network
```

---

# Netfilter Hooks

| Hook | Purpose |
|-------|----------|
| PREROUTING | Before routing decision |
| INPUT | Packets destined for the local system |
| FORWARD | Packets routed through the system |
| OUTPUT | Packets generated locally |
| POSTROUTING | Before packets leave the system |

---

# Linux Firewall Frameworks

Several user-space tools configure Netfilter.

| Tool | Purpose |
|------|----------|
| iptables | Traditional packet filtering framework |
| nftables | Modern replacement for iptables |
| firewalld | Dynamic firewall management daemon |
| UFW | Simplified firewall management (Ubuntu) |

Although many distributions now default to `nftables`, `iptables` remains widely encountered in production environments.

---

# Choosing a Firewall Tool

| Environment | Common Choice |
|-------------|---------------|
| Ubuntu Desktop | UFW |
| Ubuntu Server | UFW or nftables |
| RHEL / Rocky / AlmaLinux | firewalld |
| Enterprise Servers | nftables or firewalld |
| Legacy Systems | iptables |

The choice often depends on distribution defaults and organizational standards.

---

# Default Firewall Strategy

A common secure strategy:

```text
Default Policy

↓

Deny Incoming

↓

Allow Required Services

↓

Allow Established Connections

↓

Log Important Events
```

---

# Example Secure Server

```text
Internet

↓

Firewall

↓

Allow:

SSH

HTTPS

↓

Block:

Everything Else
```

This follows the principle of minimizing exposed services.

---

# Firewall Logging

Firewalls can record:

- Blocked connections
- Allowed connections (where configured)
- Suspicious packets
- Invalid packets
- Port scans
- Rule matches

Logs support:

- Troubleshooting
- Security monitoring
- Incident response
- Compliance

---

# Firewall Performance

Well-designed firewall rules should be:

- Simple
- Specific
- Ordered logically
- Regularly reviewed
- Free of unnecessary duplication

Efficient rule sets reduce processing overhead and simplify maintenance.

---

# Enterprise Firewall Deployment

```text
Internet

↓

Perimeter Firewall

↓

DMZ

↓

Internal Firewall

↓

Linux Server Firewall

↓

Application
```

Layered firewall deployment limits the impact of compromised systems.

---

# Cybersecurity Perspective

Attackers frequently begin by:

- Scanning ports
- Enumerating services
- Probing for exposed applications
- Testing weak configurations

Proper firewall configuration:

- Reduces attack surface
- Limits exposed services
- Slows automated attacks
- Supports monitoring and detection

A firewall is essential but should always be combined with secure configuration, patch management, authentication controls, and monitoring.

---

# Business Impact

Effective firewall management helps organizations:

- Reduce unauthorized access
- Improve regulatory compliance
- Protect business-critical services
- Reduce incident response costs
- Improve network segmentation
- Increase overall resilience

---

# Enterprise Best Practices

- Follow a default-deny approach for inbound traffic where practical.
- Allow only required ports and protocols.
- Regularly review and remove obsolete firewall rules.
- Enable logging for important security events.
- Document firewall policies and rule changes.
- Test firewall changes before production deployment.
- Combine host-based and network firewalls.
- Periodically audit firewall configurations.

---

# Key Takeaways

- Firewalls control network traffic based on security policies.
- Packet filtering evaluates packet header information.
- Stateful firewalls track connection state and simplify rule management.
- Netfilter is the Linux kernel framework responsible for packet processing.
- Tools such as `iptables`, `nftables`, `firewalld`, and `ufw` configure Netfilter.
- Host-based firewalls are a critical component of defense in depth.

---

