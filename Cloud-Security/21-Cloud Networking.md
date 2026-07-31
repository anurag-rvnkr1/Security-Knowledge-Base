# Cloud Networking

## Overview

Cloud Networking is the design, implementation, management, and protection of network infrastructure within cloud environments. It enables secure communication between cloud resources, users, applications, on-premises data centers, and external services while providing scalability, high availability, and resilience.

Unlike traditional networking, cloud networking is software-defined, highly automated, and dynamically configurable. Network components such as routers, firewalls, load balancers, gateways, and DNS services are often provided as managed cloud services rather than physical appliances.

Cloud Networking forms the foundation upon which cloud applications, virtual machines, containers, serverless functions, and managed services communicate securely.

A typical cloud network consists of:

- Virtual Private Clouds (VPCs)
- Virtual Networks (VNets)
- Subnets
- Route tables
- Internet gateways
- NAT gateways
- VPN gateways
- Load balancers
- Firewalls
- Security groups
- Network Access Control Lists (Network ACLs)
- DNS services
- Private connectivity services

Cloud Networking Security focuses on protecting:

- Network traffic
- Cloud resources
- Internal communications
- External connectivity
- Routing infrastructure
- DNS services
- Administrative access
- Hybrid cloud connections

Proper cloud network design minimizes attack surfaces while maintaining performance, scalability, and reliability.

---

## Why It Matters

Every cloud workload communicates over a network.

Examples include:

- Users accessing web applications
- APIs communicating with databases
- Kubernetes services exchanging traffic
- Serverless functions invoking cloud services
- Virtual machines accessing storage
- Hybrid cloud connections
- Multi-cloud architectures

Poor network design may lead to:

- Unauthorized access
- Lateral movement
- Data interception
- Resource exposure
- Service disruption
- Compliance violations
- Increased attack surface

Cloud networking security enables organizations to:

- Isolate workloads
- Protect sensitive data
- Control traffic flow
- Secure internet-facing services
- Restrict administrative access
- Support Zero Trust architectures
- Enable secure hybrid connectivity

A secure network architecture significantly reduces the likelihood and impact of cyberattacks.

---

## Architecture

The following illustrates a typical secure cloud network architecture.

```
                     Internet

                         │

                         ▼

                Web Application Firewall

                         │

                         ▼

                  Load Balancer

                         │

                         ▼

                 Public Subnet (DMZ)

                         │

             ┌───────────┼───────────┐

             ▼                       ▼

       Web Application         Bastion Host

             │

             ▼

          Private Subnet

      ┌───────────┼────────────┐

      ▼           ▼            ▼

 Application   Database   Cache Services

      │

      ▼

  Private Storage

      │

      ▼

Logging • Monitoring • SIEM
```

This layered architecture separates publicly accessible services from private backend resources and limits direct exposure to the internet.

---

## Key Concepts

### Virtual Private Cloud (VPC)

A Virtual Private Cloud (VPC) is a logically isolated virtual network within a public cloud provider.

A VPC provides:

- IP address ranges
- Routing
- Network isolation
- Security controls
- Connectivity options

Each VPC operates independently while sharing the underlying cloud infrastructure.

---

### Virtual Network (VNet)

In some cloud platforms, the equivalent of a VPC is called a Virtual Network (VNet).

A Virtual Network provides:

- Private IP addressing
- Resource isolation
- Network segmentation
- Secure connectivity

Both VPCs and VNets provide the foundational networking environment for cloud resources.

---

### Subnets

A subnet divides a larger virtual network into smaller logical segments.

Typical subnet types include:

| Subnet Type | Purpose |
|-------------|---------|
| Public Subnet | Internet-facing resources |
| Private Subnet | Internal workloads |
| Management Subnet | Administrative services |
| Database Subnet | Data storage services |

Segmentation limits unauthorized access and reduces lateral movement.

---

### Route Tables

Route tables determine how network traffic travels within the cloud network.

They define:

- Destination networks
- Next-hop gateways
- Internal routing
- External routing

Incorrect routing configurations may unintentionally expose sensitive resources.

---

### Internet Gateway

An Internet Gateway enables communication between cloud resources and the public internet.

Typical uses include:

- Public websites
- Public APIs
- Internet-facing load balancers

Only resources that require internet connectivity should be attached to public routes.

---

### NAT Gateway

A Network Address Translation (NAT) Gateway allows private resources to initiate outbound internet connections without accepting inbound internet traffic.

```
Private VM

↓

NAT Gateway

↓

Internet
```

This design protects private workloads while allowing software updates and external service access.

---

### VPN Gateway

A VPN Gateway provides encrypted communication between cloud networks and external locations.

Common use cases include:

- Hybrid cloud
- Remote administration
- Branch office connectivity
- Disaster recovery

VPN tunnels help protect data transmitted over untrusted networks.

---

### Security Groups

Security Groups act as stateful virtual firewalls that control traffic to cloud resources.

Typical rules specify:

- Source
- Destination
- Protocol
- Port

Example:

| Source | Protocol | Port | Action |
|---------|----------|------|--------|
| Internet | HTTPS | 443 | Allow |
| Admin Network | SSH | 22 | Allow |
| All Others | Any | Any | Deny |

Security Groups are generally applied directly to workloads such as virtual machines or network interfaces.

---

### Network Access Control Lists (Network ACLs)

Network ACLs provide stateless filtering at the subnet level.

They evaluate inbound and outbound traffic independently.

Use Network ACLs to:

- Block unwanted traffic
- Restrict subnet communication
- Add an additional security layer

Combining Security Groups and Network ACLs provides layered network protection.

---

### Load Balancer

A Load Balancer distributes incoming traffic across multiple application instances.

Benefits include:

- High availability
- Fault tolerance
- Scalability
- Health monitoring
- Improved performance

Modern cloud load balancers can also terminate TLS connections and integrate with Web Application Firewalls (WAFs).

---

### Domain Name System (DNS)

DNS translates domain names into IP addresses.

Cloud DNS services provide:

- High availability
- Global distribution
- Health checks
- DNS-based routing
- Private DNS zones

DNS security is essential to prevent spoofing and traffic redirection.

---

### Private Connectivity

Cloud providers offer private connectivity services that avoid transmitting traffic over the public internet.

Examples include:

- Private endpoints
- Service endpoints
- Private links
- Dedicated interconnects

Private connectivity reduces exposure to external threats.

---

### Hybrid Cloud Networking

Hybrid cloud networking securely connects on-premises infrastructure with cloud environments.

Common technologies include:

- Site-to-site VPN
- Dedicated circuits
- Direct cloud connections
- Software-defined WAN (SD-WAN)

Proper segmentation and encryption are essential for hybrid environments.

---

### Network Segmentation

Network segmentation divides environments into isolated security zones.

Example:

```
Internet

↓

DMZ

↓

Application Tier

↓

Database Tier

↓

Management Network
```

Segmentation limits attacker movement between workloads.

---

### Zero Trust Networking

Zero Trust networking assumes no network location is inherently trusted.

Every connection requires:

- Authentication
- Authorization
- Encryption
- Continuous verification

Trust is established based on identity and policy rather than network location.

---

