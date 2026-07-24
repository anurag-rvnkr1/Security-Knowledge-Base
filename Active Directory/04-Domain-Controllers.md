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

**Next:** **Part 2 — Domain Controller Promotion, Installation Requirements, Database Components, SYSVOL, and Core Services**