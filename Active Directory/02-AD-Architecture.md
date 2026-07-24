# Active-Directory/

# 02-AD-Architecture.md

# Part 1 — Active Directory Architecture Fundamentals, Components, Logical vs Physical Architecture, and Enterprise Design

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the architecture of Active Directory.
- Explain how Active Directory components interact.
- Distinguish between logical and physical architecture.
- Understand enterprise Active Directory design.
- Learn the role of Domain Controllers.
- Understand authentication flow at an architectural level.
- Prepare for advanced topics such as replication, FSMO roles, DNS, and trusts.

---

# What is Active Directory Architecture?

Active Directory architecture is the overall design that defines:

- How identities are organized.
- How authentication occurs.
- How authorization is enforced.
- How information is stored.
- How Domain Controllers communicate.
- How changes replicate.
- How administrators manage enterprise resources.

Think of the architecture as the blueprint that determines how Active Directory functions across an organization.

---

# High-Level Architecture

```text
                     Users

                       │

                       ▼

              Active Directory

       ┌───────────┼───────────┐

       │           │           │

 Authentication  Authorization  Management

       │           │           │

       └───────────┼───────────┘

                   ▼

            Enterprise Resources
```

---

# Core Architectural Components

Every Active Directory environment consists of several interconnected components.

```text
                     Forest

                       │

                  Domains

                       │

            Domain Controllers

                       │

             Active Directory DB

                       │

        Users • Groups • Computers

                       │

           Organizational Units

                       │

               Group Policies
```

Each layer has a specific responsibility.

---

# Architectural Layers

## Layer 1 — Identity Layer

Responsible for storing identities.

Includes:

- Users
- Groups
- Computers
- Service Accounts
- Contacts

Purpose:

Identify every security principal within the organization.

---

## Layer 2 — Authentication Layer

Responsible for verifying identities.

Primary technologies:

- Kerberos
- NTLM (legacy compatibility)

Outputs:

- Authentication success or failure
- Security tokens
- Access tickets

---

## Layer 3 — Authorization Layer

Responsible for determining access rights.

Uses:

- Security Identifiers (SIDs)
- Access Control Lists (ACLs)
- Group memberships
- Security descriptors

Authentication answers:

> Who are you?

Authorization answers:

> What are you allowed to access?

---

## Layer 4 — Management Layer

Responsible for centralized administration.

Includes:

- Active Directory Users and Computers (ADUC)
- Active Directory Administrative Center (ADAC)
- PowerShell
- Group Policy Management
- RSAT tools

Administrators interact with this layer daily.

---

## Layer 5 — Replication Layer

Ensures consistency between Domain Controllers.

Responsibilities:

- Replicate new users
- Replicate password changes
- Replicate Group Policy updates
- Replicate configuration changes

Replication is automatic and secure.

---

# Active Directory Services

The Active Directory family includes multiple services.

| Service | Purpose |
|----------|---------|
| Active Directory Domain Services (AD DS) | Identity and authentication |
| Active Directory Lightweight Directory Services (AD LDS) | LDAP directory without domains |
| Active Directory Certificate Services (AD CS) | Public Key Infrastructure (PKI) |
| Active Directory Federation Services (AD FS) | Federated authentication |
| Active Directory Rights Management Services (AD RMS)* | Information protection |

\* In modern environments, Microsoft Purview Information Protection is commonly used for information protection scenarios.

This handbook primarily focuses on **Active Directory Domain Services (AD DS)**.

---

# Active Directory Domain Services (AD DS)

AD DS provides:

- Authentication
- Authorization
- Centralized management
- Group Policy
- Directory storage
- Replication
- Trust relationships

It is the core service used in Windows enterprise environments.

---

# Logical Architecture

Logical architecture organizes identities regardless of physical location.

Components include:

- Forests
- Trees
- Domains
- Organizational Units
- Users
- Groups

Example:

```text
Forest

│

├── company.com

│      ├── Finance

│      ├── HR

│      └── IT

└── europe.company.com

       ├── Sales

       └── Support
```

Logical architecture focuses on **administration and organization**.

---

# Physical Architecture

Physical architecture represents the actual infrastructure.

Components include:

- Domain Controllers
- Sites
- Site Links
- Replication topology
- Network connections

Example:

```text
New York

│

├── DC01

├── DC02

│

London

│

├── DC03

│

Tokyo

│

└── DC04
```

Physical architecture focuses on **network efficiency and availability**.

---

# Logical vs Physical Architecture

| Logical | Physical |
|----------|----------|
| Forest | Domain Controller |
| Domain | Site |
| OU | Site Link |
| User | Replication |
| Group | Network topology |

Logical architecture organizes **objects**.

Physical architecture organizes **infrastructure**.

---

# Enterprise Architecture Example

```text
                    Forest

                      │

        ┌─────────────┴─────────────┐

        │                           │

 company.com                 europe.company.com

        │                           │

   ┌────┴────┐                 ┌────┴────┐

 Finance     IT              Sales      HR

        │

   Domain Controllers

        │

    Replication
```

---

# Domain Controller Placement

Example enterprise:

```text
Head Office

├── DC01

├── DC02

│

Branch Office A

├── DC03

│

Branch Office B

├── DC04
```

Reasons:

- Local authentication
- Reduced WAN traffic
- High availability
- Faster logon
- Fault tolerance

---

# Why Multiple Domain Controllers?

Never rely on a single Domain Controller.

Benefits include:

- High availability
- Load distribution
- Replication redundancy
- Disaster recovery
- Improved authentication performance

If one Domain Controller becomes unavailable, others can continue providing services.

---

# Authentication Architecture

```text
User

↓

Domain-Joined Computer

↓

DNS Locates Domain Controller

↓

Kerberos Authentication

↓

Security Token Created

↓

Access Granted to Authorized Resources
```

Every step depends on multiple Active Directory components working together.

---

# Authorization Architecture

```text
Authenticated User

↓

Group Membership Evaluation

↓

Security Identifier (SID)

↓

Access Control List (ACL)

↓

Access Decision
```

Permissions are evaluated using SIDs and ACLs, not usernames alone.

---

# Active Directory Data Flow

```text
Administrator

↓

Management Console / PowerShell

↓

Domain Controller

↓

NTDS.DIT Database

↓

Replication

↓

Other Domain Controllers
```

Changes made on one Domain Controller are replicated according to the configured topology.

---

# Administrative Tools

Common tools include:

| Tool | Purpose |
|------|---------|
| Active Directory Users and Computers (ADUC) | Manage users, groups, computers, OUs |
| Active Directory Administrative Center (ADAC) | Modern management interface |
| Group Policy Management Console (GPMC) | Manage Group Policy |
| Active Directory Sites and Services | Replication and sites |
| Active Directory Domains and Trusts | Trust management |
| PowerShell | Automation and bulk administration |

---

# Enterprise Design Goals

A well-designed Active Directory environment should provide:

- Scalability
- Availability
- Security
- Simplicity
- Delegation
- Performance
- Disaster recovery
- Compliance support

These goals influence decisions throughout the deployment lifecycle.

---

# Cybersecurity Perspective

From a security standpoint, the architecture should:

- Minimize privileged accounts.
- Separate administrative roles.
- Protect Domain Controllers.
- Limit administrative access paths.
- Monitor authentication events.
- Secure replication traffic.
- Apply least privilege consistently.

A well-architected environment reduces attack surface and simplifies incident response.

---

# Hands-on Lab

## Objective

Explore Active Directory management tools in a lab environment.

### Steps

1. Open **Server Manager** on a Windows Server with AD DS installed.
2. Launch:
   - Active Directory Users and Computers
   - Active Directory Administrative Center
   - Active Directory Sites and Services
   - Group Policy Management
3. Identify which tool is best suited for:
   - Managing users
   - Viewing sites
   - Managing Group Policies
   - Delegating administration
4. Document the purpose of each tool.

---

# Key Takeaways

- Active Directory architecture combines logical organization and physical infrastructure.
- AD DS is the core identity service in Windows environments.
- Logical architecture organizes directory objects.
- Physical architecture organizes Domain Controllers and replication.
- Multiple Domain Controllers improve availability and resilience.
- Authentication and authorization are separate but interconnected processes.
- Administrative tools provide centralized management capabilities.

---

# Interview Questions

1. What is Active Directory architecture?
2. Explain the difference between logical and physical architecture.
3. Why are multiple Domain Controllers recommended?
4. What services are included in the Active Directory family?
5. What is the purpose of AD DS?
6. How does authentication differ from authorization in the architecture?
7. Why is replication necessary?
8. Which management tools are commonly used for Active Directory?
9. What are the goals of a well-designed AD architecture?
10. How does architecture influence Active Directory security?

---

# References

- Microsoft Learn – Active Directory Architecture
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Identity Documentation
- Microsoft Security Best Practices

---

# 02-AD-Architecture.md

# Part 2 — Active Directory Database (NTDS.DIT), Schema, Naming Contexts, Global Catalog Architecture, and Data Storage

---

# Learning Objectives

By the end of this chapter, you will be able to:

- Understand how Active Directory stores data.
- Explain the purpose of the NTDS.DIT database.
- Understand the Extensible Storage Engine (ESE).
- Learn how the Active Directory Schema defines objects.
- Understand naming contexts (directory partitions).
- Learn the purpose of the Global Catalog.
- Understand how directory information is queried in enterprise environments.

---

# Active Directory Database Overview

Every Active Directory Domain Controller stores its directory information in a database.

This database is called:

```text
NTDS.DIT
```

It is the heart of Active Directory Domain Services.

The database contains:

- Users
- Groups
- Computers
- Organizational Units
- Domains
- Trust information
- Group Policy references
- Security descriptors
- Replication metadata
- Configuration information

---

# Database Architecture

```text
                Active Directory

                       │

                Domain Controller

                       │

                  NTDS.DIT Database

        ┌──────────────┼──────────────┐

        │              │              │

      Users         Groups       Computers

        │              │              │

        └──────────────┼──────────────┘

               Other Directory Objects
```

---

# Location of NTDS.DIT

The default location is:

```text
C:\Windows\NTDS\NTDS.DIT
```

Although administrators can specify a different location during installation, the default path is widely used.

Access to this file is restricted because it contains sensitive directory information.

---

# What Does NTDS.DIT Store?

| Category | Examples |
|----------|----------|
| Users | Employee accounts, service accounts |
| Groups | Security groups, distribution groups |
| Computers | Domain-joined devices |
| Organizational Units | Administrative containers |
| Domains | Domain configuration |
| Trusts | Trust relationships |
| Replication metadata | Change tracking information |
| Security information | SIDs, ACL-related data |
| Configuration | Forest-wide settings |

> **Note:** Passwords are **not stored in plain text**. Active Directory stores password-related data using secure one-way hashing mechanisms and related authentication material.

---

# Extensible Storage Engine (ESE)

Active Directory uses Microsoft's **Extensible Storage Engine (ESE)**, also known as **JET Blue**, as its database engine.

ESE provides:

- High-performance indexing
- Transaction logging
- Crash recovery
- Efficient searches
- Reliable updates

It is optimized for directory workloads rather than general-purpose relational data.

---

# Simplified Storage Flow

```text
Administrator

↓

Create User

↓

Domain Controller

↓

ESE Database Engine

↓

NTDS.DIT Updated

↓

Replication

↓

Other Domain Controllers
```

---

# Supporting Database Files

In addition to `NTDS.DIT`, Active Directory uses log and checkpoint files.

| File Type | Purpose |
|-----------|---------|
| Database (`NTDS.DIT`) | Directory information |
| Transaction logs | Record pending and completed database changes |
| Checkpoint file | Tracks committed transactions to support recovery |

These files help maintain database consistency after unexpected shutdowns.

---

# Active Directory Schema

The **Schema** defines:

- Which object classes exist.
- Which attributes those objects can contain.
- The data types of attributes.
- Validation rules.

Think of the schema as the blueprint for the directory.

---

# Schema Architecture

```text
Schema

│

├── Object Classes

│      ├── User

│      ├── Computer

│      ├── Group

│      └── Printer

│

└── Attributes

       ├── Name

       ├── Department

       ├── Email

       ├── Phone

       └── Description
```

---

# Object Classes

An object class defines what type of object can exist.

Examples:

| Object Class | Description |
|--------------|-------------|
| User | Human or service identity |
| Computer | Domain-joined device |
| Group | Collection of security principals |
| Contact | Directory-only contact |
| Printer | Shared printer |
| Organizational Unit | Logical administrative container |

---

# Attributes

Attributes describe properties of an object.

Example:

```text
User

↓

Name

↓

Department

↓

Manager

↓

Email

↓

Office

↓

Telephone Number
```

Each attribute has a defined data type and behavior.

---

# Mandatory vs Optional Attributes

| Type | Description |
|------|-------------|
| Mandatory | Required when creating the object |
| Optional | May be added if needed |

Example:

User:

Mandatory:

- Common Name (CN)

Optional:

- Mobile number
- Department
- Office location
- Manager

The exact set of required attributes depends on the object class and schema definitions.

---

# Schema Extension

Applications can extend the Active Directory Schema.

Examples include:

- Microsoft Exchange Server
- Microsoft Configuration Manager
- Identity management platforms
- Third-party enterprise software

Schema extensions affect the **entire forest** and should be carefully planned, tested, and documented.

---

# Naming Contexts (Directory Partitions)

The Active Directory database is divided into logical partitions called **Naming Contexts**.

```text
Active Directory

│

├── Schema Partition

├── Configuration Partition

├── Domain Partition

└── Application Partition
```

This design improves scalability and replication efficiency.

---

# 1. Schema Partition

Contains:

- Object classes
- Attributes
- Schema rules

Characteristics:

- Shared across the forest.
- Changes infrequently.
- Replicated to every Domain Controller in the forest.

---

# 2. Configuration Partition

Contains:

- Site information
- Services
- Replication topology
- Forest-wide configuration

Also replicated to every Domain Controller in the forest.

---

# 3. Domain Partition

Contains:

- Users
- Groups
- Computers
- Organizational Units
- Domain-specific objects

Replicated only to Domain Controllers within the same domain.

---

# 4. Application Partition

Stores application-specific information.

Common example:

- Active Directory-integrated DNS zones

Replication scope is configurable depending on the application.

---

# Partition Replication

```text
                Forest

                  │

        ┌─────────┼─────────┐

        │                   │

 Schema Partition   Configuration Partition

        │                   │

   All Domain Controllers in the Forest

                  │

           Domain Partition

                  │

 Domain Controllers in That Domain

                  │

        Application Partition

       (Application-defined Scope)
```

---

# Why Partitions?

Benefits include:

- Improved scalability
- Reduced replication traffic
- Better performance
- Logical separation of data
- Flexible application storage

---

# Global Catalog (GC)

The **Global Catalog** is a specialized role provided by selected Domain Controllers.

It stores:

- A complete copy of objects in its own domain.
- A partial, searchable copy of objects from every other domain in the forest.

This enables efficient searches across the entire forest.

---

# Global Catalog Architecture

```text
              Forest

      ┌───────────────┐

      │ company.com   │

      └──────┬────────┘

             │

      Global Catalog

             │

     ┌───────┼────────┐

     │       │        │

 Domain A Domain B Domain C
```

---

# Why Use a Global Catalog?

Without a Global Catalog:

- Searches would need to query multiple domains individually.

With a Global Catalog:

- One query can locate objects across the forest.

This improves:

- User searches
- Application performance
- Authentication scenarios involving universal groups

---

# Partial Attribute Set (PAS)

The Global Catalog does **not** store every attribute for every object outside its own domain.

Instead, it stores a **Partial Attribute Set (PAS)**.

Example:

Stored in the GC:

- Name
- Email
- Department
- Office

Not necessarily stored:

- Every application-specific attribute
- Large or infrequently used attributes

This reduces storage and replication overhead.

---

# Query Flow

```text
Administrator

↓

LDAP Search

↓

Global Catalog

↓

Locate Object

↓

Return Matching Results
```

The GC enables forest-wide object discovery without querying every domain individually.

---

# Read vs Write Operations

| Operation | Behavior |
|-----------|----------|
| Read | Query object information |
| Write | Create or modify objects |
| Delete | Remove objects |
| Search | Locate objects based on attributes |

Read operations are significantly more frequent than write operations in most enterprise environments.

---

# Enterprise Example

Organization:

- 8 domains
- 40 Domain Controllers
- 6 Global Catalog servers

A user searches for:

```text
Alice Johnson
```

Instead of searching each domain individually, the Global Catalog returns matching objects across the forest, greatly reducing search complexity and improving responsiveness.

---

# Cybersecurity Perspective

From a security perspective, directory data is highly sensitive.

Protect:

- Domain Controllers
- NTDS.DIT
- Transaction logs
- Schema modifications
- Global Catalog servers

Attackers often attempt to obtain directory database information because it can reveal:

- User accounts
- Group memberships
- Organizational structure
- Privileged identities

Restrict administrative access, monitor changes, and follow least-privilege principles.

---

# Hands-on Lab

## Objective

Explore Active Directory Schema and Global Catalog concepts.

### Steps

1. Open **Active Directory Users and Computers** (`dsa.msc`).
2. Examine user object properties and identify common attributes.
3. If available, explore **Active Directory Sites and Services** and identify Global Catalog servers.
4. Research the purpose of the Partial Attribute Set (PAS).
5. Document the four naming contexts and what each stores.

---

# Key Takeaways

- NTDS.DIT is the Active Directory database.
- The Extensible Storage Engine (ESE) manages directory storage.
- The Schema defines object classes and attributes.
- Naming contexts separate directory information into logical partitions.
- The Global Catalog enables efficient forest-wide searches.
- The Partial Attribute Set minimizes unnecessary replication.
- Protecting directory data is a critical security responsibility.

---

# Interview Questions

1. What is NTDS.DIT?
2. What database engine does Active Directory use?
3. What is the purpose of the Active Directory Schema?
4. What is the difference between an object class and an attribute?
5. Name the four Active Directory naming contexts.
6. Why are directory partitions important?
7. What is the Global Catalog?
8. What is the Partial Attribute Set (PAS)?
9. Why is the Global Catalog important in large forests?
10. Why should access to NTDS.DIT be tightly controlled?

---

# References

- Microsoft Learn – Active Directory Database and Schema
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Identity Documentation
- Microsoft Security Best Practices

---

**Next:** **Part 3 — Domain Controllers, SYSVOL, Authentication Architecture, Replication Fundamentals, and Active Directory Service Dependencies**