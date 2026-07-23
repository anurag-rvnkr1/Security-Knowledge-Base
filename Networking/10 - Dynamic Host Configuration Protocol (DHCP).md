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

# 10 - Dynamic Host Configuration Protocol (DHCP)

# Part 2 — DHCP Lease Lifecycle, Renewal Process, Relay Agents, DHCP Options, DHCPv6, High Availability, and Enterprise Architecture

---

# Overview

Receiving an IP address is only the beginning of the DHCP process.

Enterprise DHCP deployments continuously manage:

- Lease renewals
- Lease expiration
- Address recycling
- DHCP relay
- Multiple DHCP servers
- High Availability (HA)
- IPv6 addressing
- Configuration options

Understanding these mechanisms is essential for designing scalable and resilient enterprise networks.

---

# DHCP Lease Lifecycle

A DHCP lease is **temporary** unless configured as a reservation.

Typical lifecycle:

```
DHCP ACK

↓

Lease Starts

↓

Client Uses Address

↓

Renew Lease

↓

Continue Using Address

──────────────

OR

↓

Lease Expires

↓

Address Returns to Pool
```

This allows efficient reuse of available IP addresses.

---

# Lease Timers

A lease contains several important timers.

```
Lease Start

↓

T1 (50%)

↓

T2 (87.5%)

↓

Lease Expiration
```

These timers control how and when a client renews its address.

---

# T1 — Renewal Timer

At approximately **50% of the lease duration**, the client attempts to renew its lease with the original DHCP server.

Example:

```
8 Hour Lease

↓

4 Hours

↓

Renew Request
```

The renewal is typically sent as a **unicast** message to the server that granted the lease.

---

# T2 — Rebinding Timer

If the original server does not respond, the client waits until approximately **87.5% of the lease duration**.

Example:

```
8 Hour Lease

↓

7 Hours

↓

Broadcast Renewal Request
```

At this stage, the client attempts to contact **any available DHCP server**.

---

# Lease Expiration

If renewal attempts fail:

```
Lease Expires

↓

Client Removes Address

↓

Restart DORA Process
```

The client can no longer use the expired lease and must request a new configuration.

---

# Lease Renewal Workflow

```
Client

↓

T1 Reached

↓

Renew Request

↓

DHCP Server

↓

ACK

↓

Lease Extended
```

If the renewal succeeds, communication continues without interruption.

---

# Lease Rebinding Workflow

```
Original DHCP Server

↓

Unavailable

↓

Client

↓

Broadcast Renewal

↓

Backup DHCP Server

↓

ACK

↓

Lease Continues
```

This mechanism improves availability during server failures.

---

# DHCP Release

A client may voluntarily return its address.

```
Client

↓

DHCP Release

↓

Server

↓

Address Returned

↓

Available Again
```

This commonly occurs during a graceful shutdown or interface deactivation.

---

# DHCP Decline

Sometimes a client detects that an offered address is already in use.

Example:

```
Server Offers

↓

192.168.10.120

↓

Client Detects Duplicate

↓

DHCP Decline
```

The server marks the address as unusable until further validation or administrative action.

---

# DHCP NAK (Negative Acknowledgment)

A server sends a **DHCP NAK** when:

- The requested address is invalid.
- The client is on the wrong subnet.
- The lease is no longer valid.
- The configuration has changed.

Workflow:

```
Client

↓

DHCP Request

↓

Server

↓

DHCP NAK

↓

Restart DORA
```

---

# DHCP Inform

Some devices already have an IP address (for example, through static configuration) but still want additional DHCP options.

Example:

```
Client

↓

Static IP

↓

DHCP Inform

↓

Receive DNS, NTP, Domain Information
```

The IP address itself is not reassigned.

---

# DHCP Relay Agent

## Why Relay Agents Are Needed

Routers normally **do not forward broadcasts**.

Since a new DHCP client uses broadcast messages, clients on one subnet cannot directly reach a DHCP server on another subnet.

Example:

```
Client

↓

Broadcast

↓

Router

×

↓

DHCP Server
```

A relay agent solves this limitation.

---

# Relay Agent Operation

```
Client

↓

DHCP Discover

↓

Router (Relay Agent)

↓

Unicast

↓

DHCP Server
```

The relay converts the broadcast into a unicast message destined for the DHCP server.

---

# Cisco Relay Configuration

On Cisco devices, a relay agent is commonly configured using:

```text
interface GigabitEthernet0/1

 ip helper-address 192.168.100.10
```

The `ip helper-address` command forwards DHCP requests (and certain other UDP broadcasts) to the specified server.

---

# Enterprise Relay Example

```
Branch Office

↓

Access Switch

↓

Branch Router

↓

WAN/MPLS/SD-WAN

↓

Central DHCP Cluster

↓

Address Assigned
```

Organizations often centralize DHCP services while using relay agents in remote offices.

---

# DHCP Options

DHCP provides more than just an IP address.

Additional configuration parameters are delivered using **DHCP Options**.

---

# Common DHCP Options

| Option | Purpose |
|----------|----------|
| Option 1 | Subnet Mask |
| Option 3 | Default Gateway |
| Option 6 | DNS Server |
| Option 12 | Host Name |
| Option 15 | Domain Name |
| Option 42 | NTP Server |
| Option 51 | Lease Time |
| Option 54 | DHCP Server Identifier |
| Option 66 | TFTP Server Name |
| Option 67 | Boot File Name |

Additional options exist for specialized enterprise applications.

---

# Example DHCP Configuration

```
IP Address

↓

192.168.10.120

↓

Gateway

↓

192.168.10.1

↓

DNS

↓

192.168.20.5

↓

Domain

↓

corp.example.local
```

The client receives all these values automatically during the DHCP exchange.

---

# DHCP Reservations

Critical devices should often receive consistent addresses.

Examples:

- Domain Controllers
- DNS Servers
- Printers
- Firewalls
- IP Phones
- Network Management Systems

A reservation binds a specific MAC address to a predefined IP address.

---

# DHCPv6

IPv6 networks use **DHCPv6**, which differs from IPv4 DHCP in several important ways.

DHCPv6 provides configuration such as:

- IPv6 address (stateful mode)
- DNS servers
- Domain search list
- Other network parameters

Neighbor Discovery (ND) replaces ARP in IPv6 environments.

---

# DHCPv6 Message Flow

A simplified DHCPv6 exchange:

```
Solicit

↓

Advertise

↓

Request

↓

Reply
```

Although conceptually similar to DORA, DHCPv6 uses different message types.

---

# SLAAC vs DHCPv6

IPv6 hosts can obtain configuration using different approaches.

| Feature | SLAAC | DHCPv6 |
|----------|--------|---------|
| Address Assignment | Automatic | Server-controlled |
| DNS Information | Limited (depends on RA options) | Supported |
| Central Management | Limited | Extensive |
| Address Tracking | Minimal | Centralized |

Many enterprise environments use both Router Advertisements (RA) and DHCPv6 together.

---

# Stateful vs Stateless DHCPv6

### Stateful DHCPv6

The DHCPv6 server assigns the IPv6 address and maintains lease information.

```
Server

↓

Assigns Address

↓

Tracks Lease
```

---

### Stateless DHCPv6

The client generates its own address (often via SLAAC), while the DHCPv6 server supplies only additional configuration such as DNS servers.

---

# Enterprise DHCP Architecture

Large organizations rarely rely on a single DHCP server.

Typical architecture:

```
Clients

↓

Access Layer

↓

Distribution Layer

↓

Core Network

↓

Relay Agents

↓

DHCP Cluster

↓

Redundant Database
```

This design improves scalability and resilience.

---

# High Availability (HA)

DHCP is a critical infrastructure service.

If DHCP becomes unavailable:

- New devices cannot join the network.
- Expired leases may not renew.
- User onboarding is disrupted.
- Operational efficiency declines.

High Availability minimizes these risks.

---

# DHCP Failover

Many enterprise DHCP implementations support failover.

Example:

```
Primary Server

↓

Synchronizes

↓

Secondary Server
```

If the primary server fails:

```
Secondary Server

↓

Continues Lease Management
```

This helps maintain uninterrupted address assignment.

---

# Load Balancing

Some environments distribute DHCP requests across multiple servers.

Benefits include:

- Increased scalability
- Reduced server load
- Improved redundancy
- Better performance during peak demand

The implementation varies depending on the DHCP platform and vendor.

---

# Enterprise Deployment Example

```
50 Branch Offices

↓

Relay Agents

↓

MPLS / SD-WAN

↓

Two DHCP Servers

↓

Shared Lease Database

↓

Automatic Failover
```

This design supports centralized management while ensuring high availability.

---

# Common Enterprise Considerations

Administrators should plan for:

- Appropriate lease durations
- Sufficient address pool size
- Scope segmentation
- Redundant DHCP servers
- Relay placement
- Reservation strategy
- Monitoring and alerting

Careful planning prevents address exhaustion and service disruption.

---

# Business Impact

Reliable DHCP infrastructure enables:

- Rapid endpoint provisioning
- Automated network onboarding
- Consistent configuration
- Reduced administrative effort
- Business continuity during failures
- Scalable enterprise growth

A resilient DHCP architecture is essential for modern campus, data center, and hybrid cloud environments.

---

# Key Takeaways

- DHCP leases progress through **renewal (T1)**, **rebinding (T2)**, and **expiration**.
- Clients can **Release**, **Decline**, or **Inform** the server depending on operational needs.
- **Relay Agents** enable DHCP communication across routed networks.
- **DHCP Options** distribute additional network configuration such as gateways, DNS servers, and NTP servers.
- **DHCPv6** supports IPv6 environments and complements Router Advertisements.
- Enterprise deployments typically use **redundant DHCP servers**, **relay agents**, and **high-availability designs** to ensure reliable address management.

# 10 - Dynamic Host Configuration Protocol (DHCP)

# Part 3 — DHCP Security, DHCP Snooping, Rogue DHCP, Starvation Attacks, Option 82, Virtualization, Cloud Networking, and Enterprise Best Practices

---

# Overview

DHCP is one of the most important infrastructure services in an enterprise network.

However, because DHCP operates before a client has complete network configuration, it is also an attractive target for attackers.

Compromising DHCP can allow an attacker to:

- Prevent devices from obtaining IP addresses
- Redirect user traffic
- Perform Man-in-the-Middle (MITM) attacks
- Disrupt business operations
- Launch phishing or credential theft attacks
- Bypass network segmentation

Modern enterprise networks protect DHCP using switch-based security features such as **DHCP Snooping**, secure switch configurations, and continuous monitoring.

---

# DHCP Security Challenges

Common DHCP-related threats include:

- Rogue DHCP servers
- DHCP starvation attacks
- Address pool exhaustion
- Fake gateway assignment
- Malicious DNS server assignment
- Network reconnaissance
- Unauthorized endpoint access

Without proper controls, these threats can impact an entire broadcast domain.

---

# DHCP Starvation Attack

## What is DHCP Starvation?

A DHCP starvation attack attempts to **exhaust all available IP addresses** in a DHCP scope.

The attacker rapidly sends numerous DHCP Discover messages using **spoofed MAC addresses**.

Example:

```
Attacker

↓

DHCP Discover

↓

Fake MAC 1

↓

Fake MAC 2

↓

Fake MAC 3

↓

...

↓

DHCP Pool Exhausted
```

Legitimate users are then unable to obtain an IP address.

---

# Attack Workflow

```
Attacker

↓

Generate Thousands of Fake MAC Addresses

↓

DHCP Discover Messages

↓

DHCP Server Issues Leases

↓

Address Pool Exhausted

↓

Legitimate Client Receives No Address
```

---

# Business Impact

A successful starvation attack may result in:

- Users unable to connect to the network
- New devices failing to join the domain
- VoIP phones remaining offline
- Wireless clients unable to authenticate
- Operational downtime
- Increased help desk incidents

---

# Detection

Indicators of starvation attacks include:

- Rapid DHCP lease consumption
- High number of DHCP Discover messages
- Large numbers of unique MAC addresses
- Unexpected address pool exhaustion
- DHCP server logs showing abnormal lease creation

Monitoring systems should alert on unusual lease growth.

---

# Mitigation

Recommended controls include:

- DHCP Snooping
- Port Security
- Rate limiting
- IEEE 802.1X authentication
- Network Access Control (NAC)
- Endpoint authentication
- Switch interface security

---

# Rogue DHCP Server

## What is a Rogue DHCP Server?

A rogue DHCP server is an **unauthorized DHCP server** connected to the network.

Example:

```
Legitimate DHCP Server

──────────────

Attacker DHCP Server

↓

Client Accepts Wrong Offer
```

The client may accept whichever valid offer arrives first.

---

# Rogue DHCP Attack

The attacker provides malicious configuration:

```
IP Address

↓

Correct

Gateway

↓

Attacker

DNS

↓

Malicious DNS Server
```

Traffic can then be intercepted or redirected.

---

# Business Impact

A rogue DHCP server may:

- Redirect web traffic
- Intercept corporate credentials
- Modify DNS resolution
- Prevent Internet access
- Create widespread connectivity problems

---

# Detection

Possible indicators:

- Unexpected DHCP Server Identifier
- Multiple DHCP Offers
- Unknown gateway address
- Incorrect DNS servers
- Clients using unexpected IP ranges

Packet captures and switch logs are valuable for identifying rogue servers.

---

# DHCP Snooping

## What is DHCP Snooping?

**DHCP Snooping** is a Layer 2 security feature available on managed switches.

It protects against:

- Rogue DHCP servers
- DHCP starvation attacks
- Unauthorized DHCP messages

DHCP Snooping also builds a trusted IP-to-MAC binding database used by other security features.

---

# DHCP Snooping Operation

```
DHCP Packet

↓

Switch Receives Packet

↓

Validate Interface

↓

Trusted?

↓

Yes

↓

Forward

──────────────

No

↓

Inspect

↓

Allow or Drop
```

---

# Trusted Ports

Trusted ports typically connect to:

- Legitimate DHCP servers
- Core switches
- Distribution switches
- Router relay agents

Example:

```
Core Switch

↓

Trusted Port

↓

DHCP Server
```

Only trusted ports are allowed to send DHCP server responses.

---

# Untrusted Ports

Access ports connected to endpoints are usually configured as **untrusted**.

Example:

```
User Laptop

↓

Access Port

↓

Untrusted
```

Clients can send DHCP Discover messages, but they cannot behave as DHCP servers.

---

# DHCP Snooping Binding Table

The switch records validated DHCP information.

Example:

| MAC Address | IP Address | VLAN | Interface | Lease Time |
|-------------|------------|------|-----------|------------|
| 00:11:22:33:44:55 | 192.168.10.100 | 10 | Gi1/0/5 | 8 Hours |

This table is fundamental for Dynamic ARP Inspection (DAI) and IP Source Guard.

---

# DHCP Snooping Workflow

```
Client

↓

DHCP Discover

↓

Access Switch

↓

Relay / DHCP Server

↓

DHCP ACK

↓

Switch Creates Binding

↓

Traffic Allowed
```

---

# Rate Limiting

DHCP Snooping can limit the number of DHCP packets accepted on an access port.

Benefits include:

- Slows starvation attacks
- Protects switch CPU resources
- Reduces broadcast abuse
- Limits rogue client behavior

Administrators should choose limits appropriate for the expected client density.

---

# Option 82 (Relay Agent Information)

## What is Option 82?

**DHCP Option 82** allows a relay agent or switch to insert additional information into DHCP requests before forwarding them to the server.

Typical information includes:

- Circuit ID
- Remote ID

This helps the DHCP server identify where the request originated.

---

# Option 82 Workflow

```
Client

↓

DHCP Discover

↓

Relay Agent

↓

Insert Option 82

↓

DHCP Server

↓

Policy Decision

↓

DHCP ACK
```

---

# Benefits of Option 82

Option 82 enables:

- Location-aware address assignment
- Enhanced auditing
- Subscriber identification
- Access policy enforcement
- Improved troubleshooting

It is commonly used in service provider and large enterprise environments.

---

# DHCP Snooping and DAI

DHCP Snooping works closely with **Dynamic ARP Inspection (DAI)**.

```
DHCP Snooping

↓

Creates Binding Table

↓

DAI Uses Binding

↓

Validates ARP Packets
```

Together, these features help prevent ARP spoofing attacks.

---

# DHCP Snooping and IP Source Guard

Another related feature is **IP Source Guard**.

```
Binding Table

↓

Validate

↓

IP Address

+

MAC Address

+

Switch Port

↓

Allow Traffic
```

Traffic that does not match the trusted binding can be blocked.

---

# Enterprise Security Architecture

```
User Device

↓

Access Switch

↓

DHCP Snooping

↓

Dynamic ARP Inspection

↓

IP Source Guard

↓

Distribution Layer

↓

Core Network
```

Multiple Layer 2 security features work together to provide defense in depth.

---

# DHCP in Virtualization

Virtualization platforms frequently provide integrated DHCP capabilities.

Examples include:

- VMware environments
- Hyper-V virtual switches
- KVM/libvirt networks
- Virtual appliances

Virtual DHCP services simplify lab and development environments, while production deployments often rely on centralized enterprise DHCP servers.

---

# VMware Example

```
Virtual Machine

↓

vSwitch

↓

DHCP Service

↓

Assigned Address
```

Administrators can also configure VMs to use external enterprise DHCP servers.

---

# Hyper-V Example

```
VM

↓

Virtual Switch

↓

Enterprise DHCP
```

The Hyper-V virtual switch forwards DHCP traffic to the configured DHCP infrastructure.

---

# Docker Networking

Docker bridge networks may include an integrated IP address management (IPAM) component that allocates addresses to containers.

Example:

```
Docker Bridge

↓

Container A

↓

Container B

↓

Container C
```

The mechanism differs from traditional enterprise DHCP but serves a similar purpose of automated address assignment.

---

# Kubernetes Networking

Kubernetes typically relies on its CNI (Container Network Interface) plugin to assign addresses to Pods.

Depending on the CNI implementation:

- DHCP may be used in some environments.
- Static allocation or IPAM managed by the CNI is common.
- Overlay networks abstract many underlying networking details.

Administrators should understand the networking model used by their chosen CNI.

---

# DHCP in Public Cloud

Public cloud providers automate address assignment through platform-managed networking services.

Examples include:

### AWS

```
EC2 Instance

↓

Elastic Network Interface

↓

Private IPv4 Assigned
```

---

### Microsoft Azure

```
Virtual Machine

↓

Virtual NIC

↓

Private Address Assigned
```

---

### Google Cloud Platform

```
VM Instance

↓

Virtual NIC

↓

Internal IPv4 Address
```

While the user experience resembles DHCP, the implementation is often tightly integrated with the provider's virtual networking infrastructure.

---

# Enterprise Best Practices

Organizations should:

- Enable DHCP Snooping on access switches.
- Mark only legitimate infrastructure ports as trusted.
- Enable rate limiting on access interfaces.
- Use reservations for critical systems.
- Monitor DHCP server logs.
- Document scopes and exclusions.
- Review lease utilization regularly.
- Segment users with VLANs.
- Secure switch management access.
- Integrate DHCP events with SIEM platforms.

---

# Common DHCP Security Issues

| Issue | Possible Cause |
|--------|----------------|
| Address pool exhausted | DHCP starvation attack |
| Wrong gateway assigned | Rogue DHCP server |
| Incorrect DNS server | Malicious DHCP configuration |
| Invalid bindings | Misconfigured DHCP Snooping |
| Users cannot obtain IP addresses | Trusted port or relay configuration issue |

---

# Business Impact

Securing DHCP helps organizations:

- Prevent network outages
- Protect user traffic
- Improve endpoint onboarding
- Reduce operational risk
- Support regulatory compliance
- Strengthen Layer 2 security

Reliable DHCP security contributes directly to enterprise resilience.

---

# Key Takeaways

- **DHCP starvation attacks** attempt to exhaust available address pools using spoofed MAC addresses.
- **Rogue DHCP servers** can redirect traffic by providing malicious network configuration.
- **DHCP Snooping** protects against unauthorized DHCP activity and builds a trusted binding database.
- **Trusted** and **untrusted** switch ports are fundamental to DHCP Snooping deployments.
- **Option 82** enables location-aware DHCP policies and enhanced auditing.
- DHCP Snooping integrates with **Dynamic ARP Inspection (DAI)** and **IP Source Guard** to strengthen Layer 2 security.
- Modern virtualization platforms and cloud providers automate IP address management, though implementation details differ from traditional on-premises DHCP.

