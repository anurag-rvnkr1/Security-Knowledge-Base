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

## How It Works

Cloud Networking enables secure communication between users, cloud workloads, applications, databases, storage services, and external systems through software-defined networking components. Unlike traditional physical networks, cloud networks are dynamically provisioned, policy-driven, and managed through cloud control planes.

Every network request passes through multiple security and routing components before reaching its destination. These components authenticate traffic, enforce security policies, determine routing paths, and monitor network activity.

A secure cloud networking workflow typically consists of:

1. User or service initiates a connection
2. DNS resolves the destination
3. Traffic enters through the appropriate gateway
4. Firewalls and security controls inspect traffic
5. Route tables determine the network path
6. Security Groups and Network ACLs enforce access policies
7. Traffic reaches the destination workload
8. Network events are logged and monitored
9. Security tools analyze network behavior
10. Security teams investigate anomalies

This layered architecture minimizes unauthorized access while ensuring reliable communication.

---

## Cloud Networking Workflow

```
                User / Application

                        │

                        ▼

                 DNS Resolution

                        │

                        ▼

              Internet / Private Link

                        │

                        ▼

          Internet Gateway / VPN Gateway

                        │

                        ▼

          Firewall / Web Application Firewall

                        │

                        ▼

                Route Table Lookup

                        │

                        ▼

        Security Groups + Network ACLs

                        │

                        ▼

            Cloud Workload (VM / Pod)

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

      Database      Object Storage   APIs

                        │

                        ▼

          Logging • Monitoring • SIEM
```

Each network component performs a dedicated function before allowing communication.

---

## Step 1 – DNS Resolution

Communication begins by resolving a domain name into an IP address.

```
Client

↓

DNS Query

↓

Cloud DNS

↓

Destination IP
```

Secure DNS services help prevent spoofing, cache poisoning, and unauthorized redirection.

---

## Step 2 – Establish Network Connectivity

Depending on the workload, traffic may enter through:

- Internet Gateway
- VPN Gateway
- Dedicated private connection
- Private Endpoint
- Service Endpoint

Only approved entry points should be exposed publicly.

---

## Step 3 – Firewall Inspection

Traffic should be inspected before entering the cloud environment.

Security controls include:

- Web Application Firewall (WAF)
- Network Firewall
- Distributed Firewall
- Intrusion Detection Systems (IDS)
- Intrusion Prevention Systems (IPS)

```
Incoming Traffic

↓

Firewall Inspection

↓

Allowed / Blocked
```

Only legitimate traffic should proceed to backend resources.

---

## Step 4 – Route Selection

Route tables determine where traffic should be forwarded.

Routes may direct traffic to:

- Internet Gateway
- NAT Gateway
- VPN Gateway
- Peered VPC/VNet
- Private Endpoint
- Local subnet

Incorrect routing may expose internal services or disrupt communication.

---

## Step 5 – Security Group Evaluation

Security Groups inspect traffic destined for specific resources.

Typical rules evaluate:

- Source IP
- Destination port
- Protocol
- Direction (inbound/outbound)

Example:

```
HTTPS (443)

↓

Security Group

↓

Web Server
```

Only explicitly permitted traffic should reach protected workloads.

---

## Step 6 – Network ACL Evaluation

Network ACLs evaluate traffic at the subnet level.

Characteristics:

- Stateless
- Ordered rule evaluation
- Separate inbound and outbound rules

Network ACLs provide an additional security layer alongside Security Groups.

---

## Step 7 – Resource Communication

After passing all security controls, traffic reaches cloud resources.

Examples include:

- Virtual Machines
- Kubernetes Pods
- Serverless Functions
- Databases
- Storage Services

Applications should communicate using private networking whenever possible.

---

## Step 8 – Secure Hybrid Connectivity

Organizations frequently connect on-premises infrastructure with cloud environments.

```
Corporate Network

↓

Encrypted VPN

↓

Cloud VPN Gateway

↓

Cloud Resources
```

Dedicated private circuits may also be used for higher performance and reliability.

---

## Step 9 – Generate Network Logs

Cloud networking components should generate logs for:

- Accepted traffic
- Rejected traffic
- Route changes
- Firewall events
- VPN connections
- DNS queries
- Administrative actions

Sensitive information should be protected while retaining sufficient detail for investigations.

---

## Step 10 – Continuous Network Monitoring

Network telemetry should be analyzed continuously.

```
Network Logs

↓

Monitoring Platform

↓

SIEM

↓

Threat Detection

↓

SOC Investigation
```

Monitoring enables rapid detection of suspicious activity and network-based attacks.

---

## Cloud Network Traffic Flow

```
Client

↓

DNS

↓

Gateway

↓

Firewall

↓

Routing

↓

Security Controls

↓

Application

↓

Database

↓

Response
```

Every stage contributes to secure and reliable communication.

---

## Public and Private Subnet Example

```
                 Internet

                     │

                     ▼

             Internet Gateway

                     │

          ┌──────────┴──────────┐

          ▼                     ▼

   Public Subnet          Public Subnet

     Web Server          Load Balancer

          │

          ▼

     Private Subnet

      Application

          │

          ▼

     Database Subnet

        Database
```

Only the public subnet communicates directly with the internet, while backend resources remain isolated.

---

## Hybrid Cloud Example

```
Head Office

     │

     ▼

Encrypted VPN

     │

     ▼

Cloud VPN Gateway

     │

     ▼

Private Cloud Network

     │

     ▼

Applications
```

Encryption protects communications across untrusted networks.

---

## Practical Example

### Example 1 – Secure Web Application

A user accesses an e-commerce website hosted in the cloud.

```
User

↓

DNS

↓

Load Balancer

↓

Web Server

↓

Application

↓

Database
```

The database remains in a private subnet and is inaccessible from the internet.

---

### Example 2 – Private Software Updates

A virtual machine in a private subnet downloads operating system updates.

```
Private VM

↓

NAT Gateway

↓

Internet

↓

Software Repository
```

The VM initiates outbound traffic while remaining protected from inbound internet connections.

---

### Example 3 – Hybrid Connectivity

A company connects its headquarters to its cloud environment.

```
Office Network

↓

VPN Tunnel

↓

Cloud Gateway

↓

Private Resources
```

Traffic is encrypted throughout the connection.

---

### Example 4 – Blocking Unauthorized SSH Access

A Security Group allows SSH access only from the corporate administration network.

```
Unknown IP

↓

Security Group

↓

Connection Denied
```

Unauthorized administrative access is prevented.

---

### Example 5 – Secure Private Database Access

An application accesses a database using private networking.

```
Application

↓

Private Subnet

↓

Database

↓

Response
```

The database has no direct internet exposure.

---

## Cloud Networking Components

| Component | Purpose |
|-----------|---------|
| VPC / VNet | Isolated virtual network |
| Subnet | Logical network segmentation |
| Route Table | Determine traffic paths |
| Internet Gateway | Public internet connectivity |
| NAT Gateway | Secure outbound internet access |
| VPN Gateway | Encrypted hybrid connectivity |
| Security Group | Stateful workload firewall |
| Network ACL | Stateless subnet firewall |
| Load Balancer | Distribute incoming traffic |
| DNS Service | Resolve domain names |
| Private Endpoint | Secure private service access |
| SIEM | Analyze network security telemetry |

---

## Indicators of Network Compromise (Detection)

Continuous monitoring is essential because attackers frequently target cloud networks for reconnaissance, lateral movement, persistence, and data exfiltration.

---

### Unusual Network Traffic

Monitor for:

- Unexpected outbound connections
- Large data transfers
- Unknown destinations
- High bandwidth usage

```
Network Flow

↓

Behavior Analysis

↓

Security Alert
```

---

### Port Scanning

Repeated connection attempts across multiple ports may indicate reconnaissance activity.

Indicators include:

- Sequential port access
- High connection rates
- Multiple failed connection attempts

---

### Unexpected Administrative Connections

Alert on:

- SSH access from unknown IP addresses
- RDP access outside business hours
- Administrative logins from unfamiliar locations

Administrative access should be tightly controlled and monitored.

---

### DNS Anomalies

Watch for:

- Suspicious DNS queries
- Excessive DNS requests
- Connections to newly registered domains
- DNS tunneling behavior

DNS activity often provides early indicators of compromise.

---

### Firewall Rule Changes

Monitor for:

- Newly opened ports
- Deleted firewall rules
- Modified Security Groups
- Network ACL changes

Unauthorized rule modifications may expose protected resources.

---

### VPN and Gateway Events

Monitor:

- Failed VPN authentication
- New VPN tunnels
- Unexpected gateway configuration changes
- Excessive connection attempts

Hybrid connectivity components are high-value targets.

---

### Lateral Movement Indicators

Watch for:

- Unexpected east-west traffic
- Connections between unrelated workloads
- Unauthorized subnet access
- Service-to-service communication anomalies

Network segmentation helps reduce the impact of lateral movement.

---

### Audit Log Analysis

Continuously review:

- VPC Flow Logs
- Firewall logs
- DNS logs
- Gateway events
- Routing changes
- Security Group modifications
- Network ACL updates
- Administrative activities

Forward network telemetry to the organization's SIEM for centralized correlation and investigation.

---

## Detection Best Practices

- Enable flow logs for all virtual networks.
- Continuously monitor firewall and gateway activity.
- Alert on unexpected administrative connections.
- Analyze DNS traffic for anomalous behavior.
- Review routing and firewall rule changes regularly.
- Monitor east-west traffic between workloads.
- Correlate network events with identity and application logs.
- Integrate networking telemetry into the SIEM.
- Establish normal traffic baselines and detect deviations.
- Perform periodic reviews of network segmentation and connectivity.

---

