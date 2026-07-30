# Cloud Network Security

## Overview

Cloud Network Security is the practice of protecting cloud networking infrastructure, communication channels, workloads, and data from unauthorized access, attacks, and misuse.

Unlike traditional on-premises networks that rely heavily on physical boundaries and perimeter firewalls, cloud networks are software-defined, highly dynamic, and distributed across multiple regions and availability zones. As a result, network security in the cloud requires a combination of identity-based controls, network segmentation, encryption, monitoring, and Zero Trust principles.

Cloud Network Security protects:

- Virtual Networks
- Virtual Machines
- Containers
- Kubernetes Clusters
- Serverless Functions
- APIs
- Databases
- Storage Services
- Hybrid Connectivity
- Internet-facing Applications

Every communication path within a cloud environment should be considered untrusted until verified.

---

## Why It Matters

Modern cloud workloads communicate continuously across:

- Virtual Networks
- Availability Zones
- Cloud Regions
- Hybrid Networks
- Third-party Services
- Internet-facing APIs

Without proper network security controls, attackers may exploit weak configurations to:

- Access sensitive resources
- Move laterally across environments
- Exfiltrate data
- Compromise workloads
- Launch denial-of-service attacks
- Intercept network traffic

Cloud Network Security helps organizations:

- Protect critical workloads
- Reduce attack surfaces
- Prevent unauthorized communication
- Secure hybrid connectivity
- Improve visibility into network activity
- Support regulatory compliance
- Enable secure cloud adoption

---

## Architecture

A secure cloud network is built using multiple security layers rather than relying on a single perimeter defense.

```
                    Internet

                        │

                        ▼

              DDoS Protection Service

                        │

                        ▼

              Web Application Firewall

                        │

                        ▼

                  Load Balancer

                        │

                        ▼

              Virtual Cloud Network

        ┌─────────────┼─────────────┐

        ▼             ▼             ▼

   Public Subnet  Private Subnet  Management Subnet

        │             │             │

        ▼             ▼             ▼

   Web Servers   Application Tier   Bastion Host

                        │

                        ▼

                 Database Subnet

                        │

                        ▼

                 Backup & Storage
```

Every layer provides additional protection and limits the impact of a successful attack.

---

## Key Concepts

### Virtual Private Cloud (VPC) / Virtual Network (VNet)

A Virtual Private Cloud (VPC) or Virtual Network (VNet) is a logically isolated network created within a public cloud.

It allows organizations to define:

- IP address ranges
- Subnets
- Routing
- Security controls
- Connectivity
- DNS settings

```
Cloud Account

↓

Virtual Network

├── Public Subnet

├── Private Subnet

├── Database Subnet

└── Management Subnet
```

Each virtual network should be designed according to business and security requirements.

---

### Subnets

Subnets divide a virtual network into smaller logical segments.

Common subnet types include:

| Subnet | Purpose |
|---------|----------|
| Public | Internet-facing workloads |
| Private | Internal application servers |
| Database | Databases and storage |
| Management | Administrative systems |
| DMZ | Controlled external access |

Segmentation reduces the attack surface and limits lateral movement.

---

### Network Segmentation

Network segmentation separates workloads based on security requirements.

Example:

```
Internet

↓

Public Web Tier

↓

Application Tier

↓

Database Tier

↓

Management Network
```

Each layer communicates only with explicitly authorized systems.

Benefits include:

- Reduced attack surface
- Improved isolation
- Better compliance
- Easier monitoring
- Reduced lateral movement

---

### Microsegmentation

Microsegmentation extends network segmentation by applying security policies at the workload level rather than only at the subnet level.

```
Application Server A

↓

Policy

↓

Can Access Database

────────────────────

Application Server B

↓

Policy

↓

Access Denied
```

Microsegmentation is commonly implemented using software-defined networking and service mesh technologies.

---

### Security Groups

Security Groups act as virtual firewalls attached directly to cloud resources.

They define which inbound and outbound traffic is allowed.

Example:

| Direction | Port | Source | Action |
|-----------|------|--------|--------|
| Inbound | 443 | Internet | Allow |
| Inbound | 22 | Bastion Host | Allow |
| Inbound | 3306 | Internet | Deny |
| Outbound | All | Required Services | Allow |

Security Groups are typically stateful, meaning return traffic is automatically permitted.

---

### Network Access Control Lists (Network ACLs)

Network ACLs provide subnet-level filtering.

Unlike Security Groups, they generally evaluate traffic entering and leaving an entire subnet.

```
Internet

↓

Network ACL

↓

Subnet

↓

Virtual Machines
```

Network ACLs are useful for implementing broad network restrictions before traffic reaches workloads.

---

### Route Tables

Route tables determine how traffic flows within cloud networks.

Example:

```
Destination

↓

Route Table

↓

Internet Gateway

or

NAT Gateway

or

VPN Gateway

or

Peering Connection
```

Incorrect routing can expose sensitive resources or disrupt application connectivity.

---

### Internet Gateway

An Internet Gateway enables communication between public cloud resources and the internet.

```
Internet

↓

Internet Gateway

↓

Public Subnet

↓

Web Server
```

Only resources intended to be publicly accessible should use an Internet Gateway.

---

### NAT Gateway

A Network Address Translation (NAT) Gateway allows private resources to access the internet without exposing them to inbound internet traffic.

```
Private VM

↓

NAT Gateway

↓

Internet

↓

Software Updates
```

This design allows secure outbound communication while preventing direct inbound access.

---

### Bastion Host

A Bastion Host is a hardened administrative server used to securely access private cloud resources.

```
Administrator

↓

MFA

↓

Bastion Host

↓

Private Server
```

Best practices include:

- Restrict administrator access
- Enable MFA
- Log all sessions
- Disable unnecessary services
- Regularly patch the host

---

### Virtual Private Network (VPN)

VPNs establish encrypted tunnels between on-premises environments and cloud networks.

```
Corporate Network

↓

Encrypted VPN Tunnel

↓

Cloud Virtual Network
```

VPNs are commonly used for:

- Hybrid cloud
- Remote administration
- Secure branch connectivity
- Disaster recovery

---

### Dedicated Private Connectivity

Organizations with high-performance or compliance requirements often use dedicated private connections instead of the public internet.

Benefits include:

- Lower latency
- Predictable performance
- Reduced internet exposure
- Improved reliability

---

### Network Firewalls

Cloud firewalls inspect and filter network traffic based on defined security rules.

Typical firewall functions include:

- Allow or deny traffic
- Port filtering
- Protocol filtering
- IP filtering
- Stateful inspection
- Threat detection

```
Incoming Traffic

↓

Firewall

↓

Rule Evaluation

↓

Allow or Block
```

---

### Web Application Firewall (WAF)

A Web Application Firewall protects HTTP and HTTPS applications against common web attacks.

Typical protections include:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- Directory Traversal
- Malicious Bots
- HTTP Floods

Unlike traditional firewalls, WAFs understand application-layer traffic.

---

### Distributed Denial-of-Service (DDoS) Protection

DDoS attacks attempt to overwhelm applications with excessive traffic.

Cloud DDoS protection services help by:

- Filtering malicious traffic
- Absorbing attack traffic
- Rate limiting
- Traffic scrubbing
- Automatic mitigation

```
Attack Traffic

↓

DDoS Protection

↓

Legitimate Requests

↓

Application
```

---

### East-West and North-South Traffic

Cloud networks contain two primary traffic types.

| Traffic Type | Description |
|--------------|-------------|
| North-South | Traffic entering or leaving the cloud environment |
| East-West | Traffic between internal cloud workloads |

Modern attacks often exploit East-West communication after an initial compromise, making internal segmentation and monitoring essential.

---

### Hybrid Cloud Networking

Many enterprises operate hybrid environments connecting:

- On-premises data centers
- Public cloud
- Private cloud
- SaaS services
- Remote users

```
Corporate Data Center

↓

VPN / Dedicated Link

↓

Cloud Network

↓

Applications
```

Secure hybrid networking requires encryption, routing controls, identity verification, and continuous monitoring.

---

## How It Works

Cloud Network Security works by enforcing multiple security controls at different layers of the cloud network. Instead of relying on a single firewall, cloud providers implement **defense in depth**, where every network component validates, filters, encrypts, or monitors traffic before it reaches a workload.

Every packet entering or leaving a cloud resource typically passes through several security checkpoints.

```
Internet

↓

DDoS Protection

↓

Web Application Firewall (WAF)

↓

Load Balancer

↓

Security Group

↓

Network ACL

↓

Virtual Machine / Container

↓

Application

↓

Database
```

If any security layer determines that traffic violates a policy, the request is blocked before reaching the destination.

---

### Step 1 – Request Initiation

A user or application sends a request to a cloud-hosted service.

Example:

```
User

↓

https://company.example

↓

Cloud Network
```

The request may originate from:

- Web browsers
- Mobile applications
- APIs
- Virtual machines
- Containers
- Partner networks
- On-premises environments

---

### Step 2 – DNS Resolution

The client resolves the domain name into an IP address.

```
Client

↓

DNS Query

↓

Cloud DNS

↓

Public IP Address
```

Secure DNS services should support:

- DNSSEC
- Logging
- Threat intelligence
- Private DNS zones

---

### Step 3 – DDoS Protection

Before traffic reaches the application, cloud DDoS protection services inspect incoming requests.

```
Incoming Traffic

↓

DDoS Detection

↓

Legitimate Traffic

↓

Application
```

Malicious traffic such as volumetric attacks or protocol floods is filtered before entering the virtual network.

---

### Step 4 – Web Application Firewall (WAF)

For web applications, traffic is inspected at Layer 7.

The WAF checks for attacks including:

- SQL Injection
- Cross-Site Scripting (XSS)
- Command Injection
- File Inclusion
- HTTP Floods
- Malicious Bots

```
HTTP Request

↓

WAF

↓

Policy Evaluation

↓

Allow / Block
```

Requests violating security rules are rejected immediately.

---

### Step 5 – Load Balancer

After passing the WAF, traffic reaches the cloud load balancer.

Responsibilities include:

- Traffic distribution
- SSL/TLS termination
- Health checks
- Session persistence
- High availability

```
Incoming Request

↓

Load Balancer

├── Server A

├── Server B

└── Server C
```

The load balancer routes traffic only to healthy backend resources.

---

### Step 6 – Virtual Network Routing

The cloud networking service determines where traffic should be delivered.

```
Destination IP

↓

Route Table

↓

Correct Subnet

↓

Target Resource
```

Possible routing targets include:

- Internet Gateway
- NAT Gateway
- VPN Gateway
- Peering Connection
- Private Endpoint
- Transit Gateway

---

### Step 7 – Network ACL Evaluation

Before entering a subnet, traffic is evaluated against Network ACL rules.

```
Incoming Packet

↓

Network ACL

↓

Allow?

↓

Yes → Continue

No → Drop Packet
```

ACLs typically provide subnet-level filtering.

Example:

| Source | Port | Action |
|---------|------|--------|
| Internet | 443 | Allow |
| Internet | 22 | Deny |
| Unknown IP | Any | Deny |

---

### Step 8 – Security Group Evaluation

Security Groups protect individual cloud resources.

```
Packet

↓

Security Group

↓

Rule Evaluation

↓

Virtual Machine
```

Example rules:

| Protocol | Port | Source | Result |
|-----------|------|--------|--------|
| HTTPS | 443 | Internet | Allow |
| SSH | 22 | Bastion Host | Allow |
| Database | 3306 | Internet | Deny |

Only explicitly permitted traffic reaches the workload.

---

### Step 9 – Host Firewall

Some organizations implement host-based firewalls in addition to cloud networking controls.

```
Packet

↓

Cloud Security Group

↓

Operating System Firewall

↓

Application
```

This provides another layer of protection.

---

### Step 10 – Application Processing

Once traffic successfully passes all security controls, the application processes the request.

```
Application

↓

Business Logic

↓

Database

↓

Response
```

If authentication or authorization fails, the application rejects the request.

---

### Step 11 – Logging and Monitoring

Every significant network event should be recorded.

Typical logs include:

- Firewall logs
- Flow logs
- VPN logs
- DNS logs
- Load balancer logs
- WAF logs
- API gateway logs
- Security alerts

```
Network Event

↓

Logs

↓

SIEM

↓

Security Analyst
```

Continuous monitoring enables rapid detection of abnormal behavior.

---

## End-to-End Traffic Flow

```
Client

↓

DNS

↓

DDoS Protection

↓

Web Application Firewall

↓

Load Balancer

↓

Route Table

↓

Network ACL

↓

Security Group

↓

Virtual Machine

↓

Application

↓

Database

↓

Response
```

Each layer contributes to overall network security.

---

## Practical Example

### Example 1 – Secure Web Application

A company hosts an e-commerce platform.

Architecture:

```
Internet

↓

DDoS Protection

↓

WAF

↓

Load Balancer

↓

Public Web Servers

↓

Application Servers

↓

Private Database
```

Traffic flow:

1. Customer visits the website.
2. DNS resolves the domain.
3. DDoS protection filters malicious traffic.
4. WAF blocks application-layer attacks.
5. Load balancer distributes traffic.
6. Security Groups permit HTTPS only.
7. Application servers access the database through private networking.
8. Database is never exposed to the internet.

---

### Example 2 – Private Database Access

Application servers require database connectivity.

```
Application Server

↓

Private Subnet

↓

Security Group

↓

Database

↓

Response
```

Database rules:

Allow:

- Application subnet
- Database administrators

Deny:

- Internet
- Public IP addresses
- Unknown networks

---

### Example 3 – Administrator Access

Administrators should never connect directly to production servers from the internet.

Secure architecture:

```
Administrator

↓

VPN

↓

MFA

↓

Bastion Host

↓

Private Server
```

Benefits:

- Reduced attack surface
- Session logging
- Centralized administration
- Better auditability

---

### Example 4 – Hybrid Cloud

A financial institution connects its headquarters to the cloud.

```
Corporate Network

↓

Encrypted VPN

↓

Cloud Virtual Network

↓

Private Applications
```

Traffic never traverses the internet unencrypted.

---

### Example 5 – Microsegmentation

A Kubernetes environment hosts multiple microservices.

```
Frontend

↓

API Service

↓

Payment Service

↓

Database
```

Policies enforce:

- Frontend → API ✔

- API → Payment ✔

- Payment → Database ✔

- Frontend → Database ✘

Even if one workload is compromised, attackers cannot freely move between services.

---

## Network Traffic Examples

| Source | Destination | Expected Result |
|---------|-------------|-----------------|
| Internet | Web Server (HTTPS) | Allow |
| Internet | Database | Deny |
| Bastion Host | Linux VM (SSH) | Allow |
| Public User | Management Server | Deny |
| Application Server | Database | Allow |
| Unknown Network | Internal API | Deny |

---

## Common Cloud Network Components

| Component | Purpose |
|-----------|---------|
| VPC / VNet | Logical network isolation |
| Subnet | Workload segmentation |
| Route Table | Traffic routing |
| Internet Gateway | Internet connectivity |
| NAT Gateway | Secure outbound internet access |
| Security Group | Resource-level firewall |
| Network ACL | Subnet-level filtering |
| VPN Gateway | Encrypted hybrid connectivity |
| Load Balancer | Traffic distribution |
| WAF | Web application protection |
| Bastion Host | Secure administrative access |

---

## Indicators of Network Security Issues (Detection)

Cloud networks should be continuously monitored for abnormal activity.

---

### Unusual Inbound Connections

Unexpected connections may indicate:

- Port scanning
- Exploitation attempts
- Reconnaissance
- Malware communication

Example:

```
Single IP

↓

Ports 20–1000

↓

Security Alert
```

---

### Unauthorized Open Ports

Resources exposing unnecessary services increase attack surface.

Examples:

- SSH open to the internet
- RDP publicly accessible
- Database ports exposed
- Kubernetes API publicly reachable

Continuous configuration monitoring helps identify these issues.

---

### Excessive Failed Connections

Large numbers of failed network connections may indicate:

- Brute-force attacks
- Reconnaissance
- Firewall probing
- Misconfigured applications

---

### Unexpected East-West Traffic

After compromising one workload, attackers often attempt lateral movement.

Example:

```
Compromised VM

↓

Connect to Every Internal Server

↓

Detection Alert
```

Microsegmentation and flow monitoring help identify this behavior.

---

### Data Exfiltration

Large outbound transfers to unknown destinations should be investigated.

Indicators include:

- Unusual upload volumes
- Unknown destinations
- Unexpected protocols
- Off-hours transfers

---

### DNS Anomalies

Suspicious DNS activity includes:

- Queries to malicious domains
- High-frequency lookups
- Algorithmically generated domains
- DNS tunneling attempts

---

### VPN Misuse

Indicators include:

- Logins from unexpected countries
- Simultaneous sessions
- Excessive connection failures
- Unauthorized administrator access

---

### Network Monitoring Sources

Security teams typically monitor:

- VPC/VNet Flow Logs
- Firewall logs
- WAF logs
- Load Balancer logs
- VPN logs
- DNS logs
- IDS/IPS alerts
- Cloud audit logs
- Network telemetry

---

## Detection Best Practices

- Enable network flow logging for every production environment.
- Continuously monitor Security Group and Network ACL changes.
- Detect unusual east-west traffic patterns.
- Alert on newly exposed internet-facing services.
- Monitor outbound traffic for potential data exfiltration.
- Integrate network logs into a centralized SIEM.
- Perform continuous configuration monitoring.
- Baseline normal network behavior to improve anomaly detection.
- Review firewall and routing changes regularly.
- Investigate all unexpected privileged network access.

---

