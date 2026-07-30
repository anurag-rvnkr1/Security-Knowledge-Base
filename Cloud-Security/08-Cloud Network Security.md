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

