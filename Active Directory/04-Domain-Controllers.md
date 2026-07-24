# Active-Directory/

# 04-Domain-Controllers.md

# Part 1 — Introduction to Domain Controllers, AD DS Installation, Roles, Responsibilities, and Enterprise Architecture

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand what a Domain Controller (DC) is.
- Explain the responsibilities of a Domain Controller.
- Understand how a server becomes a Domain Controller.
- Learn the components installed with AD DS.
- Understand Domain Controller architecture.
- Learn enterprise deployment models.
- Build a foundation for replication, FSMO roles, and authentication.

---

# What is a Domain Controller?

A **Domain Controller (DC)** is a Windows Server that hosts the **Active Directory Domain Services (AD DS)** role and participates in an Active Directory domain.

A Domain Controller is responsible for:

- Authenticating users and computers
- Authorizing access to resources
- Maintaining a writable copy of the Active Directory database
- Replicating directory changes
- Applying Group Policy
- Publishing directory services through DNS
- Maintaining domain security

A Domain Controller is **not** merely a login server—it is the authoritative identity service for the domain.

---

# Domain Controller in Enterprise Architecture

```text
                     Users

                       │

                 Workstations

                       │

                  DNS Lookup

                       │

               Domain Controller

        ┌──────────────┼──────────────┐

        │              │              │

    Authentication   Directory DB   SYSVOL

        │              │              │

        └──────────────┼──────────────┘

               Enterprise Resources
```

---

# Why Are Domain Controllers Important?

Without Domain Controllers:

- Users cannot authenticate to the domain.
- Group Policy cannot be centrally applied.
- New domain accounts cannot be created.
- Directory replication cannot occur.
- Enterprise identity management becomes impossible.

For this reason, Domain Controllers are among the most critical systems in a Windows enterprise.

---

# Responsibilities of a Domain Controller

| Responsibility | Description |
|---------------|-------------|
| Authentication | Verifies user and computer identities |
| Authorization | Evaluates permissions and access |
| Directory Services | Stores and manages AD objects |
| Replication | Synchronizes directory information |
| Group Policy | Distributes policy settings |
| DNS Integration | Publishes and locates AD services |
| Time Synchronization | Supports Kerberos authentication hierarchy |
| Security Auditing | Logs security and directory events |

---

# Active Directory Domain Services (AD DS)

A Windows Server becomes a Domain Controller by installing the **Active Directory Domain Services (AD DS)** server role and promoting the server into a domain.

The promotion process:

```text
Windows Server

↓

Install AD DS Role

↓

Promote to Domain Controller

↓

Create or Join Domain

↓

Install Directory Database

↓

Server Becomes Domain Controller
```

---

# Components Installed During Promotion

When promoting a server, several core components are configured.

| Component | Purpose |
|-----------|---------|
| NTDS.DIT | Active Directory database |
| SYSVOL | Group Policy and logon scripts |
| Kerberos KDC | Authentication service |
| Netlogon | Secure domain communication |
| DNS (optional but common) | Name resolution for AD |
| Replication Configuration | Synchronization with other DCs |

---

# Domain Controller Architecture

```text
                   Domain Controller

        ┌──────────────────────────────────┐

        │ Active Directory Domain Services │

        ├──────────────────────────────────┤

        │ NTDS.DIT Database                │

        │ SYSVOL                           │

        │ Kerberos                         │

        │ Netlogon                         │

        │ LDAP                             │

        │ Replication Engine               │

        │ DNS Integration                  │

        └──────────────────────────────────┘
```

Each component contributes to identity, authentication, and centralized management.

---

# Domain Controller Communication

```text
Client

↓

DNS

↓

Domain Controller

↓

Kerberos

↓

Security Token

↓

Resource Access
```

If the client cannot locate a Domain Controller through DNS, authentication generally cannot proceed.

---

# Multiple Domain Controllers

A production environment should deploy more than one Domain Controller.

Example:

```text
                company.com

                     │

        ┌────────────┼────────────┐

        │                         │

      DC01                      DC02

        │                         │

        └──────── Replication ────┘
```

Benefits:

- Redundancy
- High availability
- Improved authentication performance
- Disaster recovery
- Maintenance flexibility

---

# Domain Controller Placement

Typical enterprise placement:

```text
Head Office

├── DC01

├── DC02

│

Regional Office A

├── DC03

│

Regional Office B

├── DC04

│

Regional Office C

└── DC05
```

Placement should reflect:

- User population
- Network latency
- WAN bandwidth
- Business continuity requirements

---

# Writable Domain Controllers

Standard Domain Controllers are writable.

They can:

- Create users
- Delete users
- Modify passwords
- Update groups
- Receive replicated changes
- Initiate replicated changes

Because changes can originate on multiple writable Domain Controllers, Active Directory uses a **multi-master replication** model.

---

# Read-Only Domain Controllers (RODCs)

Some environments deploy **Read-Only Domain Controllers (RODCs)**.

Characteristics:

- Read-only copy of the directory database
- Commonly deployed in branch offices
- Reduces risk if a remote server is compromised
- Supports local authentication for permitted accounts
- Does not accept normal writable directory changes

A dedicated chapter later in this handbook discusses RODCs in detail.

---

# Domain Controller Lifecycle

```text
Planning

↓

Install Windows Server

↓

Install AD DS

↓

Promote to Domain Controller

↓

Replication

↓

Operational Management

↓

Monitoring

↓

Maintenance

↓

Retirement
```

Proper planning and documentation should accompany every stage.

---

# Domain Controller Naming

Consistent naming conventions simplify administration.

Examples:

```text
DC01

DC02

NYC-DC01

LON-DC01

BLR-DC01

SGP-DC02
```

Recommendations:

- Include location where appropriate.
- Use sequential numbering.
- Follow enterprise naming standards.
- Avoid ambiguous names.

---

# Minimum Enterprise Recommendations

For production environments:

| Recommendation | Reason |
|---------------|--------|
| Two or more Domain Controllers | Redundancy |
| Static IP addresses | Reliable service discovery |
| Integrated DNS | Simplified AD operations |
| Regular backups | Disaster recovery |
| Monitoring | Detect failures quickly |
| Time synchronization | Kerberos reliability |

---

# Enterprise Example

Organization:

- 8,000 employees
- Four regional offices
- Hybrid identity
- Two central data centers

Deployment:

```text
Data Center A

├── DC01

├── DC02

│

Data Center B

├── DC03

├── DC04

│

Regional Offices

├── DC05

├── DC06

└── DC07
```

This design supports:

- Local authentication
- High availability
- Efficient replication
- Business continuity

---

# Cybersecurity Perspective

Domain Controllers are among the highest-value assets in a Windows environment.

They contain:

- Authentication services
- Privileged account information
- Directory database
- Group Policy
- Replication configuration

Security recommendations:

- Restrict interactive logon.
- Use dedicated administrative workstations.
- Patch promptly.
- Enable security auditing.
- Protect backups.
- Limit privileged access.
- Physically secure Domain Controllers.

Compromise of a Domain Controller can have domain-wide consequences.

---

# Hands-on Lab

## Objective

Explore a Domain Controller after installation.

### Tasks

1. Open **Server Manager**.
2. Verify the **Active Directory Domain Services** role.
3. Launch:
   - Active Directory Users and Computers
   - Active Directory Administrative Center
   - Active Directory Sites and Services
4. Locate:
   - `C:\Windows\NTDS`
   - `C:\Windows\SYSVOL`
5. Record the purpose of each directory and management tool.

---

# Key Takeaways

- A Domain Controller hosts Active Directory Domain Services.
- It authenticates users and authorizes access.
- It stores a writable copy of the directory database.
- Multiple Domain Controllers improve resilience and scalability.
- DNS and Kerberos are fundamental to Domain Controller operation.
- Domain Controllers should be carefully protected and monitored.

---

# Interview Questions

1. What is a Domain Controller?
2. What server role must be installed before promoting a Domain Controller?
3. Why are multiple Domain Controllers recommended?
4. What is stored in NTDS.DIT?
5. What is the purpose of SYSVOL?
6. What is the difference between a writable Domain Controller and an RODC?
7. Why are static IP addresses recommended for Domain Controllers?
8. Why are Domain Controllers considered critical assets?
9. What services are commonly installed during Domain Controller promotion?
10. What factors influence Domain Controller placement?

---

# References

- Microsoft Learn – Active Directory Domain Services
- Microsoft Learn – Install Active Directory Domain Services
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices
- CIS Microsoft Windows Benchmarks

---

# 04-Domain-Controllers.md

# Part 2 — Domain Controller Promotion, Installation Requirements, Database Components, SYSVOL, and Core Services

---

# Learning Objectives

By the end of this part, you will be able to:

- Understand the prerequisites for deploying a Domain Controller.
- Learn how Domain Controller promotion works.
- Understand the files and services installed during promotion.
- Explore NTDS.DIT, SYSVOL, and supporting database files.
- Learn about the core Windows services that enable Active Directory.
- Understand why proper planning is essential before deployment.

---

# Planning Before Deployment

Before promoting a server to a Domain Controller, verify the following:

| Requirement | Why It Matters |
|-------------|----------------|
| Windows Server installed | Required platform |
| Static IP address | Reliable network communication |
| Correct DNS configuration | Enables service discovery |
| Accurate system time | Required for Kerberos |
| Reliable storage | Protects directory database |
| Backup strategy | Supports disaster recovery |
| Security baseline | Reduces attack surface |

Skipping these prerequisites can lead to authentication or replication issues later.

---

# Typical Deployment Process

```text
Install Windows Server

↓

Configure Static IP

↓

Configure DNS

↓

Install AD DS Role

↓

Promote Server

↓

Install Directory Database

↓

Configure SYSVOL

↓

Restart

↓

Server Becomes Domain Controller
```

---

# Installing the AD DS Role

The **Active Directory Domain Services** role installs the software required to host a directory service.

Installation alone does **not** make the server a Domain Controller.

The server must also be **promoted**.

---

# Promotion to Domain Controller

Promotion configures the server to participate in Active Directory.

Depending on the scenario, promotion may:

- Create a new forest
- Create a new domain
- Add a Domain Controller to an existing domain

During promotion, Windows:

- Creates the directory database
- Configures replication
- Creates SYSVOL
- Installs Kerberos services
- Registers DNS records
- Configures secure domain communications

---

# Promotion Scenarios

```text
                  Promote Server

                        │

      ┌─────────────────┼─────────────────┐

      │                 │                 │

 New Forest      New Child Domain   Existing Domain
                                      (Additional DC)
```

Each option is selected based on the organization's Active Directory design.

---

# Core Components Created

After promotion:

```text
Domain Controller

│

├── NTDS.DIT

├── SYSVOL

├── DNS Records

├── Kerberos

├── Netlogon

└── Replication Configuration
```

These components work together to provide identity services.

---

# Active Directory Database

The primary database file:

```text
C:\Windows\NTDS\NTDS.DIT
```

Contains:

- Users
- Groups
- Computers
- Organizational Units
- Domains
- Trust metadata
- Configuration information
- Replication metadata

It is a writable directory database on standard Domain Controllers.

---

# Supporting Database Files

Active Directory also maintains supporting files.

| File Type | Purpose |
|-----------|---------|
| NTDS.DIT | Directory database |
| Transaction Logs | Record database transactions |
| Checkpoint File | Assists crash recovery |
| Temporary Files | Internal database operations |

Transaction logging helps ensure database consistency during unexpected failures.

---

# SYSVOL

The SYSVOL folder stores files that must be available across Domain Controllers.

Default location:

```text
C:\Windows\SYSVOL
```

Common contents:

- Group Policy templates
- Logon scripts
- Startup scripts
- Administrative templates
- Public domain files used by clients

---

# SYSVOL Structure

```text
SYSVOL

│

├── Policies

├── Scripts

└── Domain Information
```

SYSVOL is shared with authenticated domain clients so they can retrieve policies and scripts.

---

# Why SYSVOL Is Important

Without SYSVOL:

- Group Policy processing would fail.
- Logon scripts would not be distributed.
- Startup scripts would be unavailable.
- Administrative consistency would be reduced.

SYSVOL is a fundamental component of Active Directory.

---

# Core Windows Services

Several Windows services are essential for Domain Controller operation.

| Service | Purpose |
|----------|---------|
| Active Directory Domain Services | Directory service |
| Kerberos Key Distribution Center (KDC) | Authentication |
| Netlogon | Secure domain communication |
| DNS Server* | Name resolution |
| DFS Replication (DFSR) | SYSVOL replication |
| Windows Time | Time synchronization |

\* DNS may be hosted on the Domain Controller or on dedicated DNS servers.

---

# Active Directory Service Interaction

```text
Client

↓

DNS

↓

Domain Controller

↓

Kerberos

↓

NTDS.DIT

↓

Security Token

↓

Access Granted
```

Each service contributes to successful authentication.

---

# Netlogon Service

The **Netlogon** service:

- Maintains secure communication between computers and Domain Controllers.
- Registers important DNS records.
- Supports domain logon operations.
- Maintains secure channels with domain members.

If Netlogon is unavailable, authentication-related problems may occur.

---

# Kerberos Key Distribution Center (KDC)

The KDC:

- Authenticates users and computers.
- Issues Kerberos tickets.
- Supports secure single sign-on within the domain.

Simplified flow:

```text
User

↓

KDC

↓

Ticket Issued

↓

Access Resources
```

Kerberos will be covered in depth in a later chapter.

---

# DFS Replication (DFSR)

Modern Active Directory environments use **DFS Replication (DFSR)** to replicate SYSVOL contents.

Benefits include:

- Efficient replication
- Reduced bandwidth usage
- Automatic synchronization
- Improved reliability

Older environments historically used **File Replication Service (FRS)**, which has been replaced for SYSVOL replication in modern supported deployments.

---

# DNS Registration

During promotion, the Domain Controller registers important DNS records.

These records allow clients to locate services automatically.

Example:

```text
Client

↓

DNS Query

↓

SRV Record

↓

Domain Controller Located
```

Without proper DNS registration, clients may fail to discover available Domain Controllers.

---

# Time Synchronization

Kerberos depends on synchronized clocks.

Typical hierarchy:

```text
Reliable Time Source

↓

Primary Domain Controller (time hierarchy root)

↓

Other Domain Controllers

↓

Member Servers

↓

Client Computers
```

Significant time differences can cause authentication failures.

---

# Storage Considerations

Recommendations:

- Use reliable storage for the Active Directory database.
- Monitor available disk space.
- Separate operating system and database storage when appropriate for enterprise requirements.
- Protect backup media.
- Monitor storage health.

Reliable storage contributes to overall directory stability.

---

# Enterprise Example

Company:

- 5,000 employees
- Three offices
- Four Domain Controllers

Deployment:

```text
DC01

↓

Promotion

↓

NTDS.DIT Created

↓

SYSVOL Created

↓

Replication Configured

↓

Clients Authenticate
```

The additional Domain Controllers receive replicated directory information after joining the domain.

---

# Common Deployment Mistakes

Avoid:

- Using dynamic IP addresses for Domain Controllers.
- Incorrect DNS configuration.
- Ignoring backup planning.
- Weak administrator passwords.
- Promoting servers before planning replication.
- Deploying only one Domain Controller.
- Poor documentation.

Careful planning reduces operational issues.

---

# Cybersecurity Perspective

The promotion process establishes a server as a trusted identity provider.

Security recommendations:

- Harden the operating system before promotion.
- Apply security updates.
- Restrict administrative access.
- Protect the NTDS directory.
- Audit administrative activity.
- Validate backups after deployment.
- Monitor authentication and directory service events.

A newly promoted Domain Controller should immediately become part of the organization's security monitoring program.

---

# Hands-on Lab

## Objective

Review the components installed after Domain Controller promotion.

### Tasks

1. Verify the **Active Directory Domain Services** role.
2. Locate:
   - `C:\Windows\NTDS`
   - `C:\Windows\SYSVOL`
3. Identify the purpose of:
   - NTDS.DIT
   - SYSVOL
   - Netlogon
   - Kerberos
4. Open the **Services** console and locate:
   - Active Directory Domain Services
   - DFS Replication
   - Netlogon
   - Windows Time
5. Record the purpose of each service.

---

# Key Takeaways

- Installing AD DS is separate from promoting a Domain Controller.
- Promotion creates the directory database and configures core services.
- NTDS.DIT stores Active Directory data.
- SYSVOL stores Group Policy and scripts.
- DNS, Kerberos, Netlogon, DFSR, and Windows Time are critical dependencies.
- Proper planning before promotion improves reliability and security.

---

# Interview Questions

1. What is the difference between installing AD DS and promoting a Domain Controller?
2. What files are created during Domain Controller promotion?
3. What is the purpose of SYSVOL?
4. Why is DFS Replication important?
5. What does the Netlogon service do?
6. Why is DNS required during promotion?
7. Why should Domain Controllers use static IP addresses?
8. Why is accurate system time required?
9. What information is stored in NTDS.DIT?
10. What deployment mistakes should administrators avoid?

---

# References

- Microsoft Learn – Deploy Active Directory Domain Services
- Microsoft Learn – Domain Controller Installation
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices
- CIS Microsoft Windows Benchmarks

---

**Next:** **Part 3 — Domain Controller Replication, Authentication Flow, Read-Only Domain Controllers (RODC), and Enterprise Operations**