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

# 19 - Linux Firewalls

# Part 2 — iptables, nftables, firewalld, UFW, Rule Management, Chains, Tables, and Packet Processing

---

# Introduction

Linux firewalls are implemented in the kernel through **Netfilter**, but administrators typically interact with them using user-space tools.

The most common tools are:

- iptables
- nftables
- firewalld
- UFW (Uncomplicated Firewall)

Each tool ultimately configures Netfilter, but they differ in syntax, management approach, and capabilities.

---

# Linux Firewall Stack

```text
Administrator

↓

Firewall Tool

↓

Netfilter

↓

Kernel

↓

Network Interface
```

---

# Evolution of Linux Firewalls

```text
ipchains

↓

iptables

↓

nftables

↓

Future Enhancements
```

Many enterprise environments still maintain legacy `iptables` configurations, while newer distributions increasingly adopt `nftables`.

---

# iptables Overview

`iptables` is the traditional Linux firewall management utility.

It allows administrators to:

- Filter packets
- Perform NAT
- Log traffic
- Forward packets
- Modify packets

---

# iptables Architecture

```text
Incoming Packet

↓

Table

↓

Chain

↓

Rules

↓

Target

↓

Decision
```

---

# iptables Tables

Each table has a specific purpose.

| Table | Purpose |
|---------|----------|
| filter | Packet filtering (most common) |
| nat | Network Address Translation |
| mangle | Specialized packet modification |
| raw | Connection tracking exceptions |
| security | Security-related processing (e.g., SELinux integration) |

---

# Default Table

If no table is specified:

```text
filter
```

is used.

---

# iptables Chains

The filter table contains:

```text
INPUT

FORWARD

OUTPUT
```

---

# Chain Responsibilities

| Chain | Purpose |
|---------|----------|
| INPUT | Traffic destined for the local machine |
| OUTPUT | Traffic generated locally |
| FORWARD | Traffic passing through the system |

---

# Packet Flow

Packets destined for the host:

```text
Packet

↓

PREROUTING

↓

INPUT

↓

Local Process
```

Packets leaving the host:

```text
Application

↓

OUTPUT

↓

POSTROUTING

↓

Network
```

Forwarded traffic:

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

---

# Viewing Rules

Display rules:

```bash
sudo iptables -L
```

Verbose output:

```bash
sudo iptables -L -v
```

Numeric output:

```bash
sudo iptables -L -n
```

Combine options:

```bash
sudo iptables -L -v -n
```

---

# Rule Structure

A rule generally contains:

- Chain
- Match conditions
- Target

Conceptually:

```text
IF

Source

Destination

Protocol

Port

↓

THEN

Accept

Drop

Reject
```

---

# Common Targets

| Target | Meaning |
|----------|----------|
| ACCEPT | Permit packet |
| DROP | Silently discard packet |
| REJECT | Reject packet and respond appropriately |
| LOG | Record packet information |
| RETURN | Return to calling chain |

---

# Example Rules

Allow SSH:

```bash
sudo iptables -A INPUT -p tcp --dport 22 -j ACCEPT
```

Allow HTTPS:

```bash
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

Allow HTTP:

```bash
sudo iptables -A INPUT -p tcp --dport 80 -j ACCEPT
```

---

# Blocking Traffic

Drop Telnet:

```bash
sudo iptables -A INPUT -p tcp --dport 23 -j DROP
```

---

# Default Policy

View policies:

```bash
sudo iptables -L
```

Set INPUT policy:

```bash
sudo iptables -P INPUT DROP
```

A default-deny policy should be applied carefully to avoid unintentionally blocking required administrative access.

---

# Rule Order

Rules are processed sequentially.

```text
Packet

↓

Rule 1

↓

Match?

↓

Yes

↓

Stop Processing
```

If no match:

```text
↓

Rule 2

↓

Rule 3

↓

Default Policy
```

Order is therefore critical.

---

# Deleting Rules

List with numbers:

```bash
sudo iptables -L --line-numbers
```

Delete:

```bash
sudo iptables -D INPUT 3
```

---

# Flushing Rules

Remove all rules:

```bash
sudo iptables -F
```

**Warning:** Flushing rules on a remote production server can immediately expose services or lock you out, depending on default policies. Always ensure you have an appropriate recovery plan.

---

# Saving Rules

Persistence varies by distribution.

Common approaches include:

- Distribution-specific persistence packages
- Startup scripts
- Native firewall management tools

Always verify that rules survive a reboot according to your platform's documentation.

---

# nftables

`nftables` is the modern replacement for `iptables`.

Advantages include:

- Simpler rule management
- Better performance
- Unified IPv4/IPv6 handling
- More efficient rule evaluation
- Improved scalability

---

# nftables Architecture

```text
Netfilter

↓

nftables

↓

Tables

↓

Chains

↓

Rules
```

---

# Checking nftables

View rules:

```bash
sudo nft list ruleset
```

Check service status (distribution-dependent):

```bash
systemctl status nftables
```

---

# nftables Concepts

Like `iptables`, `nftables` uses:

- Tables
- Chains
- Rules

However, syntax is more consistent and expressive.

---

# Example nftables Rule

Conceptual example:

```text
Allow TCP

Port 22

↓

Accept
```

(Exact command syntax is covered in advanced administration documentation and varies by configuration.)

---

# firewalld

`firewalld` is a dynamic firewall management daemon.

Common on:

- RHEL
- Rocky Linux
- AlmaLinux
- Fedora

---

# firewalld Features

- Dynamic rule changes
- Zones
- Services
- Runtime configuration
- Permanent configuration
- Rich rules

---

# firewalld Architecture

```text
Administrator

↓

firewall-cmd

↓

firewalld

↓

Netfilter
```

---

# Checking firewalld

Status:

```bash
sudo systemctl status firewalld
```

---

# Viewing Active Zones

```bash
sudo firewall-cmd --get-active-zones
```

---

# Listing Configuration

```bash
sudo firewall-cmd --list-all
```

---

# firewalld Zones

Zones represent different trust levels.

Common zones:

| Zone | Typical Use |
|-------|-------------|
| drop | Drop all unsolicited incoming traffic |
| block | Reject incoming connections |
| public | Public networks |
| external | External network interfaces |
| dmz | Demilitarized zone |
| work | Trusted work networks |
| home | Home networks |
| trusted | Highly trusted networks |

---

# Runtime vs Permanent Configuration

Runtime:

```text
Active Until Reboot
```

Permanent:

```text
Persistent Across Reboots
```

Reload after permanent changes:

```bash
sudo firewall-cmd --reload
```

---

# UFW (Uncomplicated Firewall)

UFW simplifies firewall administration.

Common on:

- Ubuntu
- Debian

---

# Checking UFW

Status:

```bash
sudo ufw status
```

Verbose:

```bash
sudo ufw status verbose
```

---

# Enabling UFW

```bash
sudo ufw enable
```

Disable:

```bash
sudo ufw disable
```

---

# Allowing Services

Allow SSH:

```bash
sudo ufw allow ssh
```

Allow HTTP:

```bash
sudo ufw allow http
```

Allow HTTPS:

```bash
sudo ufw allow https
```

Allow a port:

```bash
sudo ufw allow 8080/tcp
```

---

# Denying Traffic

Block Telnet:

```bash
sudo ufw deny 23/tcp
```

---

# Removing Rules

Delete by rule:

```bash
sudo ufw delete allow 8080/tcp
```

---

# UFW Application Profiles

Available profiles:

```bash
sudo ufw app list
```

Application details:

```bash
sudo ufw app info "Nginx Full"
```

---

# Comparing Firewall Tools

| Feature | iptables | nftables | firewalld | UFW |
|----------|-----------|-----------|------------|------|
| Learning Curve | Moderate | Moderate | Easy | Very Easy |
| IPv4/IPv6 | Separate legacy syntax | Unified | Unified | Unified |
| Dynamic Changes | Limited | Yes | Yes | Yes |
| Enterprise Adoption | Legacy environments | Growing | Common on RHEL-family | Common on Ubuntu |

---

# Packet Processing Example

```text
Incoming Packet

↓

INPUT Chain

↓

Allow SSH?

↓

Yes

↓

Accept

↓

No

↓

Next Rule

↓

Default Policy
```

---

# Enterprise Firewall Workflow

```text
Security Policy

↓

Firewall Rules

↓

Deployment

↓

Testing

↓

Monitoring

↓

Review

↓

Optimization
```

---

# Firewall Logging

Logging helps identify:

- Blocked connections
- Port scans
- Invalid packets
- Misconfigured applications
- Suspicious traffic

Logs should be reviewed regularly and integrated with centralized logging systems where appropriate.

---

# Firewall Rule Design

Well-designed rules are:

- Specific
- Minimal
- Documented
- Ordered logically
- Regularly reviewed

Avoid:

- Duplicate rules
- Overly broad "allow any" rules
- Unused exceptions

---

# Enterprise Example

## Secure Web Server

Allow:

- SSH (administration)
- HTTPS (users)

Block:

- Telnet
- FTP (if unused)
- Unnecessary management ports

```text
Internet

↓

Firewall

↓

22

443

↓

Web Server
```

---

# Cybersecurity Perspective

Poor firewall configuration is a common source of security exposure.

Common issues include:

- Unnecessary open ports
- Overly permissive rules
- Missing logging
- Forgotten temporary exceptions
- Unused services left accessible

Regular firewall audits help identify and remediate these weaknesses.

---

# Business Impact

Effective firewall management:

- Reduces attack surface
- Protects critical services
- Supports compliance
- Improves network segmentation
- Simplifies incident investigations
- Reduces operational risk

---

# Enterprise Best Practices

- Adopt a default-deny policy where practical.
- Document every firewall rule.
- Remove obsolete rules promptly.
- Use the simplest tool that meets operational requirements.
- Test rule changes before production deployment.
- Log security-relevant events.
- Regularly review firewall configurations.
- Integrate firewall logs into centralized monitoring.

---

# Key Takeaways

- `iptables` organizes packet filtering using tables, chains, and rules.
- `nftables` is the modern successor to `iptables`.
- `firewalld` provides dynamic firewall management with zones.
- UFW simplifies firewall administration for many Ubuntu and Debian systems.
- Rule order and default policies significantly influence firewall behavior.
- Effective firewall management requires ongoing review and maintenance.

---

# 19 - Linux Firewalls

# Part 3 — NAT, Port Forwarding, Firewall Logging, Enterprise Firewall Architecture, Troubleshooting, and Security Best Practices

---

# Introduction

Modern enterprise networks rarely consist of a single server connected directly to the Internet.

Instead, they include:

- Internal networks
- DMZs (Demilitarized Zones)
- Cloud networks
- VPNs
- Firewalls
- Load balancers
- Reverse proxies
- Kubernetes clusters

To support these environments, Linux firewalls provide capabilities beyond simple packet filtering, including:

- Network Address Translation (NAT)
- Port forwarding
- Connection tracking
- Firewall logging
- Traffic troubleshooting

---

# Enterprise Network Architecture

```text
                Internet
                    │
                    ▼
          Perimeter Firewall
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
      DMZ                    Internal LAN
        │                       │
   Web Servers          Database Servers
        │                       │
        └───────────┬───────────┘
                    ▼
             Backup Network
```

---

# Network Address Translation (NAT)

NAT changes IP address information as packets travel through the firewall.

Common reasons:

- Internet access
- Address conservation (especially IPv4)
- Internal network protection
- Network isolation
- Cloud networking

---

# NAT Workflow

```text
Private Host

192.168.1.20

↓

Firewall

↓

Public IP

203.0.113.10

↓

Internet
```

The firewall maintains translation information so that return traffic reaches the correct internal host.

---

# Types of NAT

| Type | Description |
|------|-------------|
| SNAT | Source Network Address Translation |
| DNAT | Destination Network Address Translation |
| MASQUERADE | Dynamic source NAT, commonly used when the external IP changes |
| PAT | Port Address Translation (many private hosts share one public IP using different ports) |

---

# Source NAT (SNAT)

Changes the **source** IP address.

```text
Client

192.168.1.25

↓

Firewall

↓

203.0.113.5

↓

Internet
```

Used for outbound Internet connectivity.

---

# Destination NAT (DNAT)

Changes the **destination** IP address.

```text
Internet

↓

203.0.113.5

↓

Firewall

↓

192.168.1.20
```

Commonly used to publish internal services.

---

# MASQUERADE

MASQUERADE is commonly used when:

- ISP address changes
- DHCP provides the public address
- Home routers
- Small offices
- Cloud instances with dynamic addresses

Conceptually:

```text
Private Network

↓

Firewall

↓

Dynamic Public Address

↓

Internet
```

---

# Port Address Translation (PAT)

Multiple internal hosts share one public address.

```text
Host A

↓

203.0.113.5:40001

Internet

Host B

↓

203.0.113.5:40002
```

Different source ports allow simultaneous connections.

---

# NAT Packet Flow

```text
Packet

↓

PREROUTING

↓

DNAT (Optional)

↓

Routing

↓

FORWARD

↓

POSTROUTING

↓

SNAT / MASQUERADE

↓

Network
```

---

# Port Forwarding

Port forwarding redirects incoming traffic to another host.

Example:

```text
Internet

↓

203.0.113.10:443

↓

Firewall

↓

192.168.1.50:443
```

Common uses:

- Web servers
- VPN gateways
- Mail servers
- Remote administration (where appropriate)

---

# Port Forwarding Workflow

```text
Client

↓

Firewall

↓

Destination Translation

↓

Internal Server
```

---

# Typical Published Services

| Port | Service |
|------|----------|
| 22 | SSH |
| 80 | HTTP |
| 443 | HTTPS |
| 25 | SMTP |
| 53 | DNS |
| 1194 | OpenVPN (default configuration) |

Only expose services that are required by business needs.

---

# DMZ (Demilitarized Zone)

A DMZ separates public-facing services from internal systems.

```text
Internet

↓

Firewall

↓

DMZ

↓

Web Server

↓

Internal Firewall

↓

Database
```

Benefits:

- Limits lateral movement
- Isolates public services
- Improves security architecture

---

# Firewall Logging

Firewalls can record:

- Allowed traffic (where configured)
- Blocked packets
- Invalid packets
- Port scans
- Rule matches
- NAT events (platform dependent)

---

# Firewall Logging Workflow

```text
Packet

↓

Rule Match

↓

Log Event

↓

Allow / Deny

↓

Log Storage

↓

SIEM
```

---

# Why Logging Matters

Logging helps administrators:

- Troubleshoot connectivity
- Detect attacks
- Verify firewall rules
- Support incident response
- Meet compliance requirements

---

# Logging Best Practices

- Log security-relevant events.
- Avoid excessive logging that impacts storage or performance.
- Synchronize system time.
- Protect log integrity.
- Forward logs to centralized collectors.
- Review logs regularly.

---

# Connection Tracking

Netfilter tracks active sessions.

```text
Client

↓

New Connection

↓

Connection Table

↓

Established Session

↓

Return Traffic Allowed
```

Benefits:

- Fewer rules
- Improved security
- Better performance
- Simplified management

---

# Viewing Connection Tracking

Connection tracking information may be inspected using tools such as:

```bash
conntrack -L
```

Availability depends on the installed packages and kernel support.

---

# Firewall Troubleshooting Workflow

```text
Connectivity Problem

↓

Verify Service

↓

Check Firewall Rules

↓

Review Logs

↓

Test Network

↓

Implement Fix

↓

Verify
```

---

# Basic Troubleshooting Commands

Check listening ports:

```bash
ss -tulpn
```

Test connectivity:

```bash
ping host
```

Trace route:

```bash
traceroute host
```

Review firewall:

```bash
sudo nft list ruleset
```

Or:

```bash
sudo iptables -L -n -v
```

Depending on the firewall implementation.

---

# Packet Capture

When firewall rules appear correct but connectivity still fails, packet capture is often useful.

Example:

```bash
sudo tcpdump -i eth0
```

Capture specific port:

```bash
sudo tcpdump port 443
```

Packet captures help determine:

- Did packets arrive?
- Were replies sent?
- Was NAT applied?
- Was traffic blocked elsewhere?

---

# Enterprise Troubleshooting Example

Scenario:

Users cannot access HTTPS.

Investigation:

```text
Web Server

↓

Running?

↓

Port 443 Listening?

↓

Firewall Rule Exists?

↓

Routing Correct?

↓

TLS Configuration?

↓

Resolved
```

---

# Enterprise Firewall Design

A large organization may deploy:

```text
Internet

↓

Edge Firewall

↓

Web Application Firewall (WAF)

↓

Load Balancer

↓

DMZ

↓

Application Firewall

↓

Application Servers

↓

Internal Firewall

↓

Databases
```

Each layer protects different assets.

---

# Microsegmentation

Instead of trusting an entire network, workloads are separated into smaller security zones.

```text
Application A

↓

Firewall Policy

↓

Application B

↓

Firewall Policy

↓

Database
```

Benefits:

- Reduced lateral movement
- Better access control
- Smaller blast radius

---

# High Availability Firewalls

Critical environments deploy redundant firewalls.

```text
Internet

↓

Primary Firewall

│

└────► Backup Firewall

↓

Servers
```

Features may include:

- Failover
- State synchronization
- Redundant links
- Health monitoring

---

# Cloud Firewalls

Cloud providers typically offer:

- Security groups
- Network ACLs
- Virtual firewalls

These work alongside the Linux host firewall rather than replacing it.

---

# Firewall Performance

Performance depends on:

- Rule count
- Rule order
- Hardware resources
- Connection tracking
- Logging volume
- Traffic patterns

Optimize by:

- Removing unused rules
- Placing frequently matched rules earlier when appropriate
- Minimizing unnecessary logging
- Reviewing policies regularly

---

# Common Firewall Mistakes

| Mistake | Impact | Better Practice |
|----------|--------|-----------------|
| Allowing all inbound traffic | Large attack surface | Allow only required services |
| Forgetting IPv6 rules | Unexpected exposure | Secure both IPv4 and IPv6 |
| Leaving temporary rules | Long-term risk | Remove after maintenance |
| No logging | Poor visibility | Log security-relevant events |
| Duplicate rules | Complexity | Review and simplify regularly |
| No documentation | Operational confusion | Document all changes |

---

# Enterprise Example

## Secure Web Infrastructure

```text
Internet

↓

Edge Firewall

↓

HTTPS Only

↓

Reverse Proxy

↓

Application Server

↓

Database Firewall

↓

Database
```

Only required ports are exposed at each layer.

---

# Cybersecurity Perspective

Firewalls play an important role in:

- Attack surface reduction
- Network segmentation
- Threat detection
- Incident response
- Regulatory compliance

However, they **cannot**:

- Patch vulnerable software
- Stop phishing attacks
- Prevent all insider threats
- Replace endpoint security
- Replace secure application development

They are one layer of a comprehensive defense strategy.

---

# Business Impact

Proper firewall architecture helps organizations:

- Reduce unauthorized access
- Protect sensitive systems
- Improve service availability
- Support compliance
- Reduce incident response costs
- Improve customer confidence

---

# Enterprise Best Practices

- Follow a default-deny strategy for inbound traffic where practical.
- Expose only necessary services.
- Separate public and internal systems using network segmentation.
- Enable centralized firewall logging.
- Review firewall rules periodically.
- Test firewall changes in staging before production deployment.
- Document rule ownership and business justification.
- Integrate firewall monitoring with SIEM platforms.
- Review NAT and port-forwarding rules regularly.
- Include firewall recovery procedures in disaster recovery plans.

---

# Key Takeaways

- NAT enables communication between private and public networks.
- Port forwarding publishes internal services securely when properly configured.
- Firewall logging supports troubleshooting and security monitoring.
- Connection tracking enables efficient stateful firewall operation.
- Enterprise firewall architecture uses multiple security layers rather than relying on a single firewall.
- Regular review and testing are essential to maintain an effective firewall configuration.

---


