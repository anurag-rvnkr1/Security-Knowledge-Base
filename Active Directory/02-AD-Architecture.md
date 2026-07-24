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

**Next:** **Part 2 — Active Directory Database (NTDS.DIT), Schema, Naming Contexts, Global Catalog Architecture, and Data Storage**