# 23-Active-Directory.md

# Part 1 — Active Directory Fundamentals, Architecture, Components, and Enterprise Identity Management

---

# Introduction

Modern enterprise environments may contain hundreds, thousands, or even hundreds of thousands of users, computers, printers, servers, and applications.

Managing every device individually quickly becomes impossible.

Microsoft **Active Directory (AD)** solves this problem by providing a centralized identity and access management (IAM) platform.

Instead of configuring each computer separately, administrators manage identities, authentication, authorization, security policies, and resources from a centralized directory service.

Today, Active Directory remains one of the most important technologies in enterprise Windows infrastructure and is heavily targeted by cyber attackers, making it essential knowledge for Windows administrators and cybersecurity professionals.

---

# Learning Objectives

By the end of this section, you will understand:

- What Active Directory is
- Why organizations use Active Directory
- Active Directory architecture
- Logical and physical components
- Domains
- Forests
- Trees
- Organizational Units (OUs)
- Domain Controllers
- Global Catalog
- Sites
- LDAP basics
- Active Directory terminology

---

# What is Active Directory?

**Active Directory Domain Services (AD DS)** is Microsoft's centralized directory service used to:

- Authenticate users
- Authorize access
- Manage computers
- Store directory information
- Apply security policies
- Centralize administration

Think of Active Directory as the enterprise "phonebook" for everything connected to the Windows environment.

Instead of remembering information for every system individually, Active Directory stores and manages it centrally.

---

# Why Active Directory Exists

Without Active Directory:

```text
Administrator

↓

PC1

↓

PC2

↓

PC3

↓

PC4

↓

PC500
```

Every computer requires individual administration.

With Active Directory:

```text
Administrator

↓

Active Directory

↓

PC1
PC2
PC3
PC500

↓

Centralized Management
```

Centralized administration significantly reduces operational overhead.

---

# Enterprise Benefits

Active Directory provides:

- Centralized authentication
- Centralized authorization
- Single Sign-On (SSO)
- Group Policy management
- Resource management
- Delegated administration
- Security auditing
- Enterprise scalability

---

# Identity Management

Identity management answers questions such as:

- Who are you?
- What groups do you belong to?
- What devices can you access?
- What permissions do you have?
- Which applications are available?

Active Directory stores this information within the directory database.

---

# Authentication vs Authorization

These terms are frequently confused.

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you access?" |
| Username + Password | Access Control Lists |
| Kerberos / NTLM | Security Groups |

Example:

```text
Employee

↓

Authentication

↓

Identity Verified

↓

Authorization

↓

Access Granted
```

---

# Active Directory Database

Directory information is stored in the **NTDS.dit** database.

The database contains information about:

- Users
- Groups
- Computers
- Printers
- Shared folders
- Policies
- Organizational Units

Every Domain Controller maintains a copy of this database.

---

# Active Directory Architecture

AD consists of logical and physical components.

```text
Forest

↓

Tree

↓

Domain

↓

Organizational Unit

↓

Objects
```

Physical components:

```text
Domain Controllers

↓

Sites

↓

Replication
```

---

# Active Directory Objects

Everything stored inside AD is called an **object**.

Common object types include:

| Object | Purpose |
|---------|----------|
| User | Person account |
| Computer | Workstation/server |
| Group | Permission management |
| Printer | Shared printer |
| Contact | Directory contact |
| Shared Folder | Network resource |

---

# Active Directory Attributes

Objects contain attributes.

Example:

User object:

| Attribute | Example |
|------------|----------|
| Name | John Smith |
| Username | jsmith |
| Email | john@company.com |
| Department | Finance |
| Phone | +1-555-1000 |

Attributes describe the properties of an object.

---

# Distinguished Name (DN)

Each object has a unique Distinguished Name.

Example:

```text
CN=John Smith

OU=Finance

DC=company

DC=com
```

DN identifies the object's exact location within the directory hierarchy.

---

# Organizational Units (OUs)

Organizational Units organize directory objects.

Example:

```text
Company

↓

HR

↓

Finance

↓

IT

↓

Sales
```

Benefits:

- Easier administration
- Group Policy assignment
- Delegation
- Logical organization

---

# Domains

A domain is the core administrative boundary in Active Directory.

A domain contains:

- Users
- Groups
- Computers
- Domain Controllers
- Policies

Example:

```text
company.com
```

All domain objects share the same directory database and security policies.

---

# Trees

A tree is a collection of related domains sharing a common namespace.

Example:

```text
company.com

↓

india.company.com

↓

usa.company.com

↓

uk.company.com
```

Domains automatically trust each other within the same tree.

---

# Forests

A forest is the highest-level logical structure.

Example:

```text
Forest

↓

company.com

↓

research.company.com

↓

sales.company.com
```

Characteristics:

- Shared schema
- Shared Global Catalog
- Forest-wide trust relationships
- Common configuration

A forest is the security boundary of Active Directory.

---

# Logical Structure Overview

```text
Forest

↓

Tree

↓

Domain

↓

Organizational Unit

↓

Objects
```

Logical structures organize directory information independently of physical network layout.

---

# Physical Structure

The physical structure consists of:

- Domain Controllers
- Sites
- Site Links
- Replication

These components optimize authentication and replication traffic.

---

# Domain Controllers (DCs)

A Domain Controller is a Windows Server running Active Directory Domain Services.

Responsibilities:

- User authentication
- Kerberos ticket issuance
- Policy enforcement
- Directory replication
- DNS integration
- Directory database storage

Every authentication request typically communicates with a Domain Controller.

---

# Domain Controller Architecture

```text
User Login

↓

Domain Controller

↓

NTDS Database

↓

Authentication

↓

Access Granted
```

---

# Read-Only Domain Controller (RODC)

RODCs contain a read-only copy of the directory database.

Advantages:

- Improved security
- Branch office deployment
- Reduced credential exposure
- Lower administrative risk

RODCs are commonly deployed in locations with limited physical security.

---

# Global Catalog (GC)

The Global Catalog stores a partial copy of every object in the forest.

Benefits:

- Faster searches
- Universal group membership
- Forest-wide object lookup
- Improved authentication efficiency

---

# Active Directory Sites

Sites represent the physical network topology.

Example:

```text
Bangalore Office

↓

Domain Controller

↓

Employees
```

Another site:

```text
London Office

↓

Domain Controller

↓

Employees
```

Sites reduce authentication latency and optimize replication.

---

# Site Replication

```text
Site A

↓

Replication

↓

Site B

↓

Replication

↓

Site C
```

Replication keeps Domain Controllers synchronized.

---

# Multi-Master Replication

Unlike traditional databases with a single write server, Active Directory uses **multi-master replication**.

```text
DC1

↔

DC2

↔

DC3
```

Changes made on one Domain Controller replicate to others.

This improves availability and fault tolerance.

---

# Lightweight Directory Access Protocol (LDAP)

LDAP is the protocol used to query and manage directory information.

Examples:

- Search users
- Find groups
- Query computers
- Retrieve attributes

LDAP commonly uses:

| Port | Purpose |
|------|----------|
| 389 | LDAP |
| 636 | LDAP over SSL/TLS (LDAPS) |

LDAPS should be preferred for secure communication.

---

# DNS and Active Directory

Active Directory depends heavily on DNS.

DNS is used to locate:

- Domain Controllers
- Kerberos services
- Global Catalog servers
- LDAP services

Without functioning DNS, Active Directory authentication is severely impacted.

---

# Enterprise Example

A multinational company has:

```text
Forest

↓

company.com

├── india.company.com

├── usa.company.com

├── germany.company.com

└── japan.company.com
```

Each regional office has:

- Local Domain Controllers
- Local Sites
- Centralized authentication
- Common security policies
- Replicated directory information

Employees authenticate using their nearest Domain Controller while maintaining access to enterprise resources.

---

# Cybersecurity Perspective

Active Directory is frequently targeted because it controls:

- User identities
- Authentication
- Authorization
- Administrative privileges
- Enterprise resources

Compromising Active Directory often enables attackers to gain widespread access across the organization.

Protecting AD is therefore a top priority for defenders.

---

# Business Impact

Active Directory enables:

- Centralized identity management
- Faster onboarding and offboarding
- Simplified administration
- Improved security
- Single Sign-On
- Scalable enterprise management
- Reduced operational costs

---

# Enterprise Best Practices

- Design a logical OU structure.
- Limit Domain Administrator accounts.
- Secure Domain Controllers.
- Use redundant Domain Controllers.
- Protect DNS infrastructure.
- Deploy Global Catalog servers appropriately.
- Monitor Active Directory continuously.
- Document forest and domain architecture.
- Separate administrative duties.
- Review directory structure periodically.

---

# Practical Labs

## Lab 1 — Explore Active Directory Objects

Using **Active Directory Users and Computers (ADUC)**:

Identify:

- Users
- Groups
- Computers
- Organizational Units

Document the hierarchy.

---

## Lab 2 — Draw an AD Forest

Create a diagram containing:

- One forest
- Two trees
- Four domains
- Multiple OUs

Explain the purpose of each component.

---

## Lab 3 — Compare Logical vs Physical Structure

Create a comparison table explaining:

- Forest
- Tree
- Domain
- OU
- Site
- Domain Controller

Describe whether each is a logical or physical component.

---

## Lab 4 — DNS Dependency

Explain how DNS assists:

- Domain logon
- LDAP
- Kerberos
- Global Catalog discovery

---

# Key Takeaways

- Active Directory centralizes identity and access management.
- Domains are the primary administrative boundary.
- Forests represent the highest logical structure and security boundary.
- Domain Controllers authenticate users and store the directory database.
- Organizational Units simplify administration and Group Policy application.
- DNS is essential for Active Directory operation.

---

# Interview Questions

1. What is Active Directory?
2. What is the purpose of a Domain Controller?
3. Explain the difference between a forest and a domain.
4. What is an Organizational Unit (OU)?
5. What is the Global Catalog?
6. Why is DNS critical for Active Directory?
7. What is multi-master replication?
8. What is the difference between authentication and authorization?
9. What is LDAP used for?
10. Why are Domain Controllers considered critical assets?

---

# References

- Microsoft Learn
- Microsoft Active Directory Documentation
- Microsoft Windows Server Documentation
- Microsoft LDAP Documentation
- Microsoft Kerberos Documentation
- NIST SP 800-53
- CIS Microsoft Windows Server Benchmarks
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- *Mastering Active Directory* (Dishan Francis)

---

**Next:** **Part 2 — Active Directory Authentication, Kerberos, NTLM, DNS Integration, FSMO Roles, Trusts, and Replication**