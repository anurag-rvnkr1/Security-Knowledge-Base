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

# 10 - Dynamic Host Configuration Protocol (DHCP)

# Part 4 — Packet Analysis, Verification Commands, Enterprise Troubleshooting, Detection Engineering, Practical Labs, Interview Questions, and Chapter Review

---

# Overview

Deploying DHCP is only one aspect of enterprise network management.

Network engineers and cybersecurity professionals must also be able to:

- Verify DHCP operation
- Analyze DHCP packets
- Detect malicious DHCP activity
- Troubleshoot lease failures
- Monitor DHCP infrastructure
- Investigate security incidents
- Validate enterprise deployments

This section combines operational networking with security monitoring and incident response.

---

# DHCP Packet Analysis

DHCP is based on the BOOTP message format and exchanges several message types between clients and servers.

A typical DHCP packet contains fields such as:

| Field | Description |
|--------|-------------|
| Operation (Op) | Boot Request or Boot Reply |
| Hardware Type | Ethernet (1) |
| Hardware Address Length | Usually 6 bytes for MAC addresses |
| Transaction ID (XID) | Identifies the DHCP transaction |
| Client IP Address (CIADDR) | Existing client address (if any) |
| Your IP Address (YIADDR) | IP address offered to the client |
| Server IP Address (SIADDR) | DHCP server address |
| Gateway IP Address (GIADDR) | Relay agent address |
| Client Hardware Address (CHADDR) | Client MAC address |
| DHCP Options | Additional configuration parameters |

---

# DORA Packet Flow

The complete DHCP exchange follows the DORA sequence.

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

Each stage can be observed using packet capture tools such as Wireshark.

---

# DHCP Discover

Characteristics:

- Broadcast
- Source IP: `0.0.0.0`
- Destination IP: `255.255.255.255`
- Client has no usable IPv4 address yet
- Requests available DHCP servers

---

# DHCP Offer

The server responds with:

- Proposed IP address
- Lease duration
- Default gateway
- DNS servers
- Subnet mask
- Additional DHCP options

If multiple DHCP servers respond, the client selects one offer.

---

# DHCP Request

The client requests the selected lease.

Purpose:

- Accept one DHCP Offer
- Inform other DHCP servers that their offers are declined
- Continue the lease process

---

# DHCP ACK

The server confirms:

- Lease assignment
- Configuration parameters
- Lease timers

The client then configures its network interface.

---

# Wireshark Analysis

## Display Filter

```text
dhcp
```

or

```text
bootp
```

(Because DHCP uses the BOOTP protocol format.)

---

# Typical Packet Sequence

```
Frame 1

DHCP Discover

↓

Frame 2

DHCP Offer

↓

Frame 3

DHCP Request

↓

Frame 4

DHCP ACK
```

A successful DORA exchange should contain these four messages in order.

---

# Useful Wireshark Fields

During analysis, examine:

- Transaction ID (XID)
- Client MAC address
- Offered IP address
- DHCP Server Identifier
- Lease Time
- Option 3 (Default Gateway)
- Option 6 (DNS Server)
- Option 15 (Domain Name)
- Option 51 (Lease Duration)
- Option 54 (Server Identifier)
- Option 82 (if used)

---

# Cisco IOS Verification

Display DHCP bindings:

```text
show ip dhcp binding
```

Display DHCP pool statistics:

```text
show ip dhcp pool
```

Display DHCP conflicts:

```text
show ip dhcp conflict
```

Display DHCP server statistics:

```text
show ip dhcp server statistics
```

Display relay configuration:

```text
show running-config | include helper-address
```

Display DHCP Snooping information:

```text
show ip dhcp snooping
```

Display DHCP Snooping bindings:

```text
show ip dhcp snooping binding
```

These commands help verify both DHCP services and associated security features.

---

# Linux Verification

Display interface configuration:

```bash
ip addr
```

Display routing table:

```bash
ip route
```

Display DNS configuration:

```bash
cat /etc/resolv.conf
```

Request a new DHCP lease (client implementation dependent):

```bash
sudo dhclient
```

Release an existing lease:

```bash
sudo dhclient -r
```

Capture DHCP traffic:

```bash
sudo tcpdump -i eth0 port 67 or port 68
```

---

# Windows Verification

Display full network configuration:

```cmd
ipconfig /all
```

Release the current lease:

```cmd
ipconfig /release
```

Request a new lease:

```cmd
ipconfig /renew
```

Display DNS cache:

```cmd
ipconfig /displaydns
```

Flush DNS cache:

```cmd
ipconfig /flushdns
```

---

# Enterprise Troubleshooting Workflow

When a client fails to obtain an IP address:

```
Verify Physical Connectivity

↓

Verify Switch Port Status

↓

Verify VLAN Assignment

↓

Check DHCP Scope Availability

↓

Verify DHCP Server Health

↓

Verify Relay Agent

↓

Capture DHCP Traffic

↓

Review DHCP Logs

↓

Validate Client Configuration

↓

Test Again
```

Following a structured process helps isolate issues efficiently.

---

# Troubleshooting Scenario 1

## Symptom

A new laptop receives an **APIPA address (169.254.x.x)**.

### Investigation

Verify:

- DHCP server availability
- Switch connectivity
- VLAN membership
- Relay configuration
- DHCP scope capacity

Possible causes include:

- DHCP server unavailable
- Relay misconfiguration
- Exhausted address pool
- Broadcast not reaching the server

---

# Troubleshooting Scenario 2

## Symptom

Users receive incorrect DNS server addresses.

Possible causes:

- Incorrect DHCP scope options
- Rogue DHCP server
- Configuration changes
- Scope inheritance issues

Actions:

- Inspect DHCP options.
- Capture DORA traffic.
- Verify the DHCP Server Identifier.
- Review switch logs.

---

# Troubleshooting Scenario 3

## Symptom

Users at a remote branch cannot obtain addresses.

Verify:

- WAN connectivity
- Relay agent configuration
- Firewall rules
- UDP ports 67 and 68
- DHCP server reachability

---

# Practical Lab 1 — Observe the DORA Process

Topology:

```
Client

↓

Switch

↓

DHCP Server
```

Tasks:

1. Start Wireshark.
2. Release the existing DHCP lease.
3. Renew the lease.
4. Capture the DORA sequence.
5. Identify:
   - Transaction ID
   - Offered IP address
   - Lease duration
   - Default gateway
   - DNS server

---

# Practical Lab 2 — Configure DHCP Relay

Topology:

```
Client

↓

Access Switch

↓

Router

↓

DHCP Server
```

Tasks:

1. Configure the router as a DHCP relay.
2. Verify `ip helper-address`.
3. Renew the client lease.
4. Confirm successful address assignment.

---

# Practical Lab 3 — DHCP Snooping

Requirements:

- Managed switch
- DHCP Snooping enabled

Tasks:

1. Configure trusted and untrusted interfaces.
2. Verify the DHCP Snooping binding table.
3. Attempt to introduce a rogue DHCP server in a controlled lab.
4. Confirm that unauthorized DHCP Offers are blocked.

---

# Practical Lab 4 — DHCP Starvation (Controlled Lab)

**Warning:** Perform only in an isolated lab environment.

Tasks:

1. Generate multiple DHCP Discover messages with spoofed MAC addresses.
2. Observe lease allocation.
3. Enable DHCP Snooping and rate limiting.
4. Verify that the attack is mitigated.

The purpose of this lab is to understand defensive controls, not to attack production systems.

---

# SOC Detection Engineering

Security Operations Centers (SOCs) should monitor for:

- DHCP starvation attempts
- Rogue DHCP servers
- Unusual lease activity
- Address pool exhaustion
- Frequent DHCP Decline messages
- Unexpected DHCP Server Identifiers

Correlating DHCP events with switch logs and endpoint telemetry improves detection accuracy.

---

# SIEM Detection Ideas

Example 1:

```
IF

DHCP Server Identifier

↓

Not Approved

↓

Generate High-Severity Alert
```

Example 2:

```
IF

Hundreds of DHCP Discover Messages

↓

Single Switch Port

↓

Short Time Window

↓

Generate Starvation Alert
```

Example 3:

```
IF

Address Pool Utilization

>

90%

↓

Notify Network Operations
```

---

# Zeek Monitoring

Zeek can provide visibility into:

- DHCP transactions
- Assigned IP addresses
- Client MAC addresses
- Lease activity
- Server identifiers

This information can be correlated with authentication, DNS, and endpoint logs for comprehensive investigations.

---

# Suricata Monitoring

Depending on deployment architecture, Suricata can help identify:

- Rogue DHCP servers
- Abnormal DHCP traffic
- Broadcast anomalies
- Policy violations

Alerts should be validated using packet captures and infrastructure logs before concluding that malicious activity has occurred.

---

# Enterprise Best Practices

- Use redundant DHCP servers.
- Implement DHCP failover where supported.
- Configure relay agents correctly.
- Enable DHCP Snooping on access switches.
- Mark only legitimate infrastructure ports as trusted.
- Monitor lease utilization.
- Use reservations for critical infrastructure.
- Document scopes, exclusions, and options.
- Integrate DHCP logs with SIEM platforms.
- Regularly audit DHCP configurations.

---

# Enterprise Case Study

## Scenario

A multinational organization reports that new employees cannot join the corporate network.

### Investigation

Network engineers discover:

- DHCP scope utilization has reached 100%.
- A compromised endpoint generated thousands of DHCP Discover messages.
- DHCP Snooping was disabled on one access switch.

### Resolution

- Isolate the compromised endpoint.
- Reclaim expired leases.
- Enable DHCP Snooping and rate limiting.
- Expand the DHCP scope after capacity planning.
- Review switch security configurations.
- Monitor for recurring anomalies.

---

# Interview Questions

## Beginner

### What is DHCP?

DHCP (Dynamic Host Configuration Protocol) automatically assigns IP configuration to network devices.

---

### What does DORA stand for?

- Discover
- Offer
- Request
- Acknowledge

---

### Which transport protocol and ports does DHCP use?

DHCP uses **UDP**:

- Server: UDP 67
- Client: UDP 68

---

## Intermediate

### What is a DHCP lease?

A lease is the temporary assignment of an IP address and related configuration to a client.

---

### What is a DHCP relay agent?

A DHCP relay agent forwards DHCP requests between clients and servers on different IP subnets.

---

### What is DHCP Snooping?

DHCP Snooping is a Layer 2 security feature that prevents rogue DHCP servers and builds trusted IP-to-MAC binding tables.

---

## Advanced

### Explain a DHCP starvation attack.

A DHCP starvation attack exhausts the available address pool by sending numerous DHCP Discover messages with spoofed MAC addresses, preventing legitimate clients from obtaining leases.

---

### How would you troubleshoot a client that receives an APIPA address?

A strong answer should include:

1. Verify physical connectivity.
2. Check VLAN assignment.
3. Confirm DHCP server availability.
4. Validate relay configuration.
5. Inspect DHCP scope capacity.
6. Capture DORA traffic.
7. Review switch and server logs.

---

### How would you secure DHCP in an enterprise?

A comprehensive response should mention:

- DHCP Snooping
- Rate limiting
- Trusted/untrusted ports
- Reservations for critical devices
- Relay validation
- High Availability
- Continuous monitoring
- SIEM integration
- Regular audits

---

# References

## RFCs

- RFC 2131 — Dynamic Host Configuration Protocol
- RFC 2132 — DHCP Options and BOOTP Vendor Extensions
- RFC 3315 (Obsoleted by RFC 8415) — DHCP for IPv6
- RFC 8415 — DHCP for IPv6 (Current Specification)

## Organizations

- IETF
- IEEE
- NIST
- CIS

---

# Summary

DHCP is a foundational enterprise service that automates IP address allocation and network configuration. Understanding lease management, relay agents, security mechanisms such as DHCP Snooping, and enterprise troubleshooting techniques enables administrators to deploy scalable, resilient, and secure networks. Continuous monitoring and integration with broader security controls are essential for protecting DHCP infrastructure against operational failures and malicious activity.

---

# Chapter Review

After completing this chapter, you should understand:

✔ DHCP fundamentals and architecture

✔ DORA process

✔ Lease lifecycle (T1, T2, expiration)

✔ DHCP scopes, exclusions, and reservations

✔ DHCP relay agents

✔ DHCP options

✔ DHCPv6 and SLAAC concepts

✔ High Availability and failover

✔ DHCP starvation and rogue DHCP attacks

✔ DHCP Snooping and Option 82

✔ Virtualization and cloud DHCP concepts

✔ Cisco, Linux, and Windows verification commands

✔ Wireshark DHCP analysis

✔ Enterprise troubleshooting methodology

✔ SOC detection engineering and SIEM use cases

✔ Practical DHCP labs

✔ Interview preparation from beginner to advanced

---

# What's Next?

The next chapter, **`11-DNS.md`**, will cover:

- Domain Name System (DNS) fundamentals
- DNS hierarchy and namespace
- Recursive vs iterative queries
- DNS record types (A, AAAA, CNAME, MX, TXT, NS, PTR, SOA, SRV, CAA)
- Recursive resolvers and authoritative servers
- DNS caching and TTL
- Forward and reverse lookups
- DNSSEC
- Split-horizon DNS
- Enterprise DNS architecture
- DNS attacks, detection, troubleshooting, packet analysis, and security best practices