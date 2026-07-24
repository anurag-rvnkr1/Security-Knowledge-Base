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
# 23-Active-Directory.md

# Part 2 — Active Directory Authentication, Kerberos, NTLM, DNS Integration, FSMO Roles, Trusts, and Replication

---

# Introduction

The primary purpose of Active Directory is to provide secure authentication and authorization for enterprise resources.

When a user signs in to a domain-joined computer, multiple Windows technologies work together behind the scenes:

- DNS
- Domain Controllers
- Kerberos
- LDAP
- Group Policy
- Active Directory Database

Understanding this authentication process is essential for Windows administrators, SOC analysts, penetration testers, and security engineers.

---

# Active Directory Authentication Flow

A simplified authentication process:

```text
User

↓

Enter Username & Password

↓

DNS Locates Domain Controller

↓

Kerberos Authentication

↓

Ticket Issued

↓

Access Enterprise Resources
```

Authentication should occur securely and efficiently with minimal user interaction.

---

# Authentication Components

| Component | Purpose |
|------------|----------|
| DNS | Locate Domain Controllers |
| Domain Controller | Authenticate users |
| Kerberos | Secure authentication |
| LDAP | Directory queries |
| Global Catalog | Forest-wide searches |
| Group Policy | Apply security settings |

---

# Kerberos Authentication

Kerberos is the default authentication protocol in Active Directory environments.

Advantages:

- Mutual authentication
- Strong encryption
- Single Sign-On (SSO)
- Reduced password transmission
- Efficient access to multiple resources

Kerberos authenticates users without repeatedly sending passwords across the network.

---

# Kerberos Terminology

| Component | Description |
|------------|-------------|
| Client | User or computer requesting access |
| KDC | Key Distribution Center |
| TGT | Ticket Granting Ticket |
| TGS | Ticket Granting Service |
| Service Ticket | Access ticket for a specific service |

The Key Distribution Center (KDC) runs on every Domain Controller.

---

# Kerberos Authentication Process

```text
User Login

↓

KDC

↓

Ticket Granting Ticket (TGT)

↓

Request Service Ticket

↓

Service Ticket

↓

Access Server
```

The user's password is used to verify identity during the initial authentication process, after which tickets are used to access services.

---

# Step 1 — Initial Authentication (AS Exchange)

```text
User

↓

Username

↓

KDC

↓

Verify Credentials

↓

Issue TGT
```

The Authentication Service (AS) validates the user's credentials and issues a Ticket Granting Ticket (TGT).

---

# Step 2 — Ticket Request (TGS Exchange)

```text
User

↓

Present TGT

↓

Request File Server Access

↓

KDC

↓

Issue Service Ticket
```

The Ticket Granting Service (TGS) issues a ticket for the requested service.

---

# Step 3 — Resource Access

```text
User

↓

Service Ticket

↓

File Server

↓

Validate Ticket

↓

Access Granted
```

The server validates the ticket before granting access.

---

# Kerberos Ticket Lifetime

Typical enterprise environments configure ticket lifetimes to balance usability and security.

Example concepts:

- Ticket lifetime
- Renewal period
- Session duration

Administrators can configure these values through Group Policy.

---

# Single Sign-On (SSO)

Kerberos enables users to authenticate once and access multiple services without repeatedly entering credentials.

Example:

```text
Login Once

↓

Email

↓

File Server

↓

Print Server

↓

SharePoint

↓

SQL Server
```

This improves both user experience and security.

---

# Mutual Authentication

Kerberos verifies:

- The user to the server
- The server to the user

This helps reduce the risk of impersonation attacks.

---

# NTLM Authentication

NTLM is the legacy Windows authentication protocol.

Although still supported for compatibility, Kerberos is preferred whenever possible.

NTLM may still be used when:

- Kerberos is unavailable
- Systems are not domain joined
- Legacy applications require it

---

# Kerberos vs NTLM

| Kerberos | NTLM |
|-----------|------|
| Default in AD | Legacy protocol |
| Ticket-based | Challenge-response |
| Mutual authentication | Client authentication only |
| Supports SSO | Limited SSO |
| Better performance | More network overhead |
| Stronger security | Less secure than Kerberos |

Organizations should reduce NTLM usage where feasible.

---

# DNS Integration

Active Directory relies heavily on DNS.

DNS enables clients to locate:

- Domain Controllers
- Kerberos services
- LDAP services
- Global Catalog servers

Without properly functioning DNS, users may experience authentication failures.

---

# Service (SRV) Records

DNS Service (SRV) records advertise Active Directory services.

Examples include records for:

- LDAP
- Kerberos
- Global Catalog

Clients query these records to locate the appropriate Domain Controller.

---

# Domain Join Process

```text
Computer

↓

Locate DNS

↓

Find Domain Controller

↓

Authenticate

↓

Join Domain

↓

Receive Group Policy
```

A successful domain join depends on network connectivity, DNS, and appropriate permissions.

---

# Active Directory Replication

Every Domain Controller maintains a copy of the Active Directory database.

Changes must replicate to other Domain Controllers.

```text
DC1

↔

DC2

↔

DC3

↔

DC4
```

Replication ensures consistency throughout the environment.

---

# Replication Benefits

Replication provides:

- High availability
- Fault tolerance
- Consistent authentication
- Disaster resilience
- Load distribution

---

# Replication Types

| Type | Description |
|------|-------------|
| Intra-site | Within the same AD site |
| Inter-site | Between different AD sites |

Intra-site replication is generally optimized for speed, while inter-site replication is optimized for bandwidth efficiency.

---

# Replication Workflow

```text
Administrator

↓

Create User

↓

Domain Controller

↓

Replication

↓

Other Domain Controllers

↓

Consistent Directory
```

---

# Flexible Single Master Operations (FSMO)

Although Active Directory uses multi-master replication, some operations must be performed by only one Domain Controller.

These special responsibilities are called **FSMO Roles**.

There are five FSMO roles.

---

# Forest-Wide FSMO Roles

## Schema Master

Responsibilities:

- Updates Active Directory schema
- Controls schema modifications
- Ensures schema consistency

Only one Schema Master exists per forest.

---

## Domain Naming Master

Responsibilities:

- Adds domains
- Removes domains
- Maintains domain namespace consistency

Only one Domain Naming Master exists per forest.

---

# Domain-Wide FSMO Roles

## RID Master

Responsibilities:

- Allocates Relative Identifiers (RIDs)
- Prevents duplicate Security Identifiers (SIDs)

Every security principal requires a unique SID.

---

## PDC Emulator

Responsibilities include:

- Password updates
- Account lockout processing
- Time synchronization reference
- Legacy client compatibility
- Group Policy coordination

The PDC Emulator is one of the busiest FSMO roles.

---

## Infrastructure Master

Responsibilities:

- Updates object references across domains
- Maintains cross-domain object consistency

This role is particularly important in multi-domain environments.

---

# FSMO Overview

| FSMO Role | Scope |
|------------|-------|
| Schema Master | Forest |
| Domain Naming Master | Forest |
| RID Master | Domain |
| PDC Emulator | Domain |
| Infrastructure Master | Domain |

---

# Active Directory Trusts

A trust allows users in one domain or forest to access resources in another.

Example:

```text
Domain A

⇄ Trust ⇄

Domain B
```

Trusts simplify resource sharing across administrative boundaries.

---

# Types of Trusts

| Trust Type | Purpose |
|-------------|----------|
| Parent-Child | Automatic within a tree |
| Tree-Root | Between trees in the same forest |
| External | Between separate domains |
| Forest | Between separate forests |
| Shortcut | Optimizes authentication paths |
| Realm | Interoperability with non-Windows Kerberos realms |

Trusts should be configured only when required by business needs.

---

# Trust Direction

Trusts may be:

```text
One-Way

A → B
```

or

```text
Two-Way

A ↔ B
```

Direction determines which domain accepts authentication requests.

---

# Active Directory Sites and Authentication

Clients normally authenticate against the nearest Domain Controller.

```text
Client

↓

Nearest Site

↓

Nearest Domain Controller

↓

Authentication
```

This minimizes network latency and reduces WAN traffic.

---

# Time Synchronization

Kerberos requires accurate time synchronization.

Large time differences between systems may cause authentication failures.

Typical hierarchy:

```text
Reliable Time Source

↓

PDC Emulator

↓

Other Domain Controllers

↓

Domain Members
```

Consistent time is also important for event correlation and forensic investigations.

---

# Enterprise Example

A global organization has offices in:

- New York
- London
- Bengaluru
- Tokyo

Each location contains:

- Local DNS servers
- Local Domain Controllers
- Separate Active Directory Sites

Authentication occurs locally, while replication synchronizes directory changes across all regions.

This design improves performance and resilience.

---

# Cybersecurity Perspective

Authentication infrastructure is frequently targeted by attackers.

Examples include:

- Kerberoasting
- Password spraying
- Pass-the-Hash
- Golden Ticket attacks
- Silver Ticket attacks
- NTLM relay attacks

Understanding authentication workflows helps defenders detect abnormal behavior and implement appropriate mitigations.

---

# Business Impact

Proper Active Directory authentication design provides:

- Reliable user access
- Single Sign-On
- Reduced administrative overhead
- Faster authentication
- Improved scalability
- Better disaster recovery
- Enhanced security

---

# Enterprise Best Practices

- Prefer Kerberos over NTLM.
- Maintain healthy DNS infrastructure.
- Deploy multiple Domain Controllers.
- Monitor replication health.
- Protect FSMO role holders.
- Synchronize time across the domain.
- Review trust relationships periodically.
- Restrict unnecessary trusts.
- Monitor authentication failures.
- Document authentication architecture.

---

# Practical Labs

## Lab 1 — Observe Kerberos Tickets

Run:

```cmd
klist
```

Identify:

- Ticket Granting Ticket (TGT)
- Service Tickets
- Expiration times

---

## Lab 2 — Verify FSMO Roles

Run:

```cmd
netdom query fsmo
```

Document the server holding each FSMO role.

---

## Lab 3 — Review Replication Topology

Using **Active Directory Sites and Services**:

- Identify sites
- Identify Domain Controllers
- Explain replication paths

---

## Lab 4 — Compare Kerberos and NTLM

Create a comparison table covering:

- Authentication method
- Security
- Performance
- Use cases
- Enterprise recommendations

---

# Key Takeaways

- Kerberos is the preferred authentication protocol for Active Directory.
- DNS is essential for locating Domain Controllers and directory services.
- Replication keeps Domain Controllers synchronized.
- FSMO roles manage operations that require a single authoritative server.
- Trusts enable secure resource sharing between domains and forests.
- Accurate time synchronization is critical for Kerberos authentication.

---

# Interview Questions

1. Explain the Kerberos authentication process.
2. What is a Ticket Granting Ticket (TGT)?
3. What is the role of the Key Distribution Center (KDC)?
4. Compare Kerberos and NTLM.
5. Why is DNS required for Active Directory?
6. What are the five FSMO roles?
7. Why does Active Directory use replication?
8. What is the difference between intra-site and inter-site replication?
9. What are Active Directory trusts used for?
10. Why is time synchronization important in a domain environment?

---

# References

- Microsoft Learn
- Microsoft Active Directory Documentation
- Microsoft Kerberos Documentation
- Microsoft Windows Server Documentation
- Microsoft DNS Documentation
- Microsoft Replication Documentation
- NIST SP 800-53
- CIS Microsoft Windows Server Benchmarks
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- *Mastering Active Directory* (Dishan Francis)

---

# 23-Active-Directory.md

# Part 3 — Active Directory Administration, Users, Groups, Organizational Units, Group Scope, Delegation, and Administrative Best Practices

---

# Introduction

After deploying Active Directory, administrators spend most of their time managing:

- Users
- Groups
- Computers
- Organizational Units (OUs)
- Group memberships
- Delegated permissions
- Administrative roles

Proper administration ensures that users have the correct access while maintaining security, scalability, and operational efficiency.

---

# Active Directory Administrative Tools

Common administration tools include:

| Tool | Purpose |
|------|----------|
| Active Directory Users and Computers (ADUC) | Manage users, groups, computers, and OUs |
| Active Directory Administrative Center (ADAC) | Modern administrative interface |
| Active Directory Sites and Services | Manage replication and sites |
| Active Directory Domains and Trusts | Manage domains and trust relationships |
| Group Policy Management Console (GPMC) | Manage Group Policy Objects |
| PowerShell Active Directory Module | Automation and bulk administration |

Each tool serves a specific administrative purpose.

---

# Active Directory Users

A user object represents an identity that can authenticate and access enterprise resources.

User accounts typically include:

- Username (sAMAccountName)
- User Principal Name (UPN)
- Display Name
- Email Address
- Department
- Job Title
- Manager
- Phone Number
- Security Identifier (SID)

---

# User Account Lifecycle

```text
Request

↓

Create Account

↓

Assign Groups

↓

Apply Policies

↓

Employee Uses Account

↓

Role Change

↓

Disable Account

↓

Delete or Archive
```

The lifecycle should align with organizational HR and security processes.

---

# Creating User Accounts

Information commonly required:

- Full name
- Username
- Department
- Password
- Organizational Unit
- Group memberships

Accounts should follow standardized naming conventions.

---

# User Naming Standards

Example:

| Attribute | Example |
|------------|----------|
| Display Name | John Smith |
| Username | jsmith |
| UPN | jsmith@company.com |
| Email | john.smith@company.com |

Consistent naming simplifies administration and auditing.

---

# User Account States

| State | Description |
|---------|-------------|
| Enabled | User can authenticate |
| Disabled | Authentication blocked |
| Locked Out | Temporarily blocked after failed logons |
| Expired | Account validity ended |

Inactive accounts should be reviewed regularly.

---

# Password Management

Administrators should:

- Reset passwords securely
- Verify user identity before reset
- Enforce password policies
- Require password change when appropriate
- Monitor repeated password resets

Password reset procedures should follow organizational security policies.

---

# Computer Objects

Each domain-joined computer has a computer object.

The object stores:

- Computer name
- SID
- Group memberships
- Operating system
- Authentication information

Computer accounts authenticate to the domain similarly to user accounts.

---

# Organizational Units (OUs)

Organizational Units organize objects logically.

Example:

```text
Company

├── IT

├── Finance

├── HR

├── Sales

└── Servers
```

Benefits include:

- Simplified administration
- Group Policy targeting
- Delegation of control
- Logical organization

---

# Designing OU Structures

Common approaches:

### Department-Based

```text
Company

↓

Finance

↓

HR

↓

IT
```

### Location-Based

```text
Company

↓

India

↓

USA

↓

Germany
```

### Function-Based

```text
Company

↓

Workstations

↓

Servers

↓

Service Accounts
```

The design should reflect administrative requirements rather than the organizational chart alone.

---

# Groups

Groups simplify permission management.

Instead of assigning permissions directly to individual users:

```text
Users

↓

Security Group

↓

Resource
```

This approach is easier to manage and audit.

---

# Types of Groups

| Group Type | Purpose |
|-------------|----------|
| Security Group | Access control |
| Distribution Group | Email distribution |

Only Security Groups can be used for permission assignments.

---

# Group Scope

There are three primary security group scopes.

| Scope | Typical Use |
|---------|-------------|
| Domain Local | Resource permissions within a domain |
| Global | Users with similar job roles |
| Universal | Cross-domain membership in a forest |

Choosing the appropriate scope improves scalability and replication efficiency.

---

# Group Scope Overview

```text
Global Groups

↓

Universal Groups

↓

Domain Local Groups

↓

Permissions
```

A commonly recommended approach is to assign users to Global Groups, nest those into Universal Groups when necessary, and grant permissions to Domain Local Groups.

---

# AGDLP Model

A widely used permission model is **AGDLP**:

```text
Accounts

↓

Global Groups

↓

Domain Local Groups

↓

Permissions
```

Benefits:

- Simplified administration
- Reduced permission sprawl
- Easier auditing
- Better scalability

---

# AGUDLP Model

In multi-domain environments, the **AGUDLP** model is often used:

```text
Accounts

↓

Global Groups

↓

Universal Groups

↓

Domain Local Groups

↓

Permissions
```

Universal Groups facilitate access across domains within the same forest.

---

# Nested Groups

Groups may contain other groups.

Example:

```text
Finance Users

↓

Finance Managers

↓

Payroll Access
```

Nested groups simplify permission management but should be documented to avoid unnecessary complexity.

---

# Delegation of Administration

Delegation allows administrative responsibilities to be assigned without granting full Domain Administrator privileges.

Example:

```text
Domain Admin

↓

Delegate Password Resets

↓

Help Desk
```

This follows the principle of least privilege.

---

# Common Delegated Tasks

Examples:

- Reset passwords
- Unlock user accounts
- Create users
- Create computer accounts
- Join computers to the domain
- Manage specific OUs
- Modify group membership

Delegation reduces operational risk.

---

# Administrative Roles

Examples:

| Role | Responsibilities |
|------|------------------|
| Domain Administrator | Full domain administration |
| Enterprise Administrator | Forest-wide administration |
| Schema Administrator | Schema modifications |
| Account Operator | Limited account management |
| Backup Operator | Backup and restore operations |

Highly privileged groups should contain only approved personnel.

---

# Built-in Administrative Groups

Common built-in groups include:

- Domain Admins
- Enterprise Admins
- Schema Admins
- Administrators
- Account Operators
- Backup Operators
- Server Operators
- Print Operators

Membership should be reviewed regularly.

---

# Service Accounts

Applications often require dedicated accounts.

Best practices:

- Least privilege
- No interactive logon
- Strong credential management
- Prefer Managed Service Accounts (MSA/gMSA)
- Monitor account usage

Service accounts should not be shared between unrelated applications.

---

# Bulk Administration

PowerShell simplifies repetitive tasks.

Examples:

- Create users
- Disable inactive accounts
- Update attributes
- Export reports
- Manage group membership

Automation reduces manual effort and improves consistency.

---

# User Provisioning Workflow

```text
HR Request

↓

Create User

↓

Assign Groups

↓

Apply Group Policy

↓

Issue Device

↓

User Ready
```

Standardized provisioning improves security and operational efficiency.

---

# User Deprovisioning Workflow

```text
Termination Notice

↓

Disable Account

↓

Remove Group Membership

↓

Disable Access

↓

Archive Data

↓

Delete Account (According to Policy)
```

Prompt deprovisioning reduces the risk of unauthorized access.

---

# Auditing Administrative Changes

Monitor events such as:

- User creation
- User deletion
- Password resets
- Group membership changes
- OU modifications
- Privileged account changes

Auditing supports investigations and compliance.

---

# Enterprise Example

A company with 8,000 employees organizes its directory as follows:

```text
Company

├── Users

├── Workstations

├── Servers

├── Service Accounts

├── IT

├── HR

└── Finance
```

Permissions are assigned using the AGDLP model.

Help Desk staff are delegated authority to:

- Reset passwords
- Unlock accounts
- Manage user objects within designated OUs

Domain Administrator access is reserved for a small number of senior administrators.

---

# Cybersecurity Perspective

Improper administration may result in:

- Excessive privileges
- Privilege escalation
- Orphaned accounts
- Shared administrator credentials
- Unauthorized access
- Difficult auditing

Applying least privilege and proper delegation significantly reduces these risks.

---

# Business Impact

Effective administration provides:

- Faster onboarding
- Faster offboarding
- Improved security
- Simplified permission management
- Better compliance
- Lower administrative overhead
- Easier audits

---

# Enterprise Best Practices

- Use standardized naming conventions.
- Design OUs around administrative needs.
- Assign permissions to groups rather than individual users.
- Follow the AGDLP or AGUDLP model.
- Delegate routine administration instead of granting Domain Admin rights.
- Review privileged group membership regularly.
- Automate repetitive administrative tasks with PowerShell.
- Disable inactive accounts promptly.
- Audit administrative changes.
- Document directory structure and delegation.

---

# Practical Labs

## Lab 1 — Create an OU Structure

Design an OU hierarchy for an organization with:

- IT
- HR
- Finance
- Sales
- Servers
- Workstations

Explain your design decisions.

---

## Lab 2 — Design a Group Strategy

Using the AGDLP model, create:

- Three Global Groups
- Three Domain Local Groups
- Two shared resources

Map users to resources through groups.

---

## Lab 3 — Delegation Exercise

Design a delegation model allowing Help Desk staff to:

- Reset passwords
- Unlock accounts
- Manage user objects in the HR OU

Explain why Domain Administrator privileges are unnecessary.

---

## Lab 4 — User Lifecycle

Document the complete lifecycle for:

- New employee onboarding
- Department transfer
- Employee termination

Include security controls at each stage.

---

# Key Takeaways

- Active Directory administration centers on users, groups, computers, and OUs.
- Organizational Units simplify management and Group Policy application.
- Groups should be used to assign permissions instead of individual users.
- AGDLP and AGUDLP provide scalable permission management models.
- Delegation enables secure administration using least privilege.
- Regular auditing of privileged accounts and administrative changes is essential.

---

# Interview Questions

1. What is an Organizational Unit (OU)?
2. What is the difference between Security Groups and Distribution Groups?
3. Explain the AGDLP model.
4. When should Universal Groups be used?
5. Why is delegation preferred over granting Domain Administrator access?
6. What information is stored in a user object?
7. Why should permissions be assigned to groups rather than users?
8. What are Managed Service Accounts (MSAs)?
9. Describe the lifecycle of a user account.
10. Why should privileged group membership be reviewed regularly?

---

# References

- Microsoft Learn
- Microsoft Active Directory Documentation
- Microsoft Windows Server Documentation
- Microsoft PowerShell Active Directory Module Documentation
- Microsoft Group Management Documentation
- NIST SP 800-53
- CIS Microsoft Windows Server Benchmarks
- *Mastering Active Directory* (Dishan Francis)
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 23-Active-Directory.md

# Part 4 — Active Directory Security, Attacks, Hardening, Monitoring, Troubleshooting, and Enterprise Best Practices

---

# Introduction

Active Directory is one of the most valuable assets in a Windows enterprise.

Because it controls:

- User identities
- Authentication
- Authorization
- Group Policy
- Administrative privileges
- Enterprise resources

it is a primary target for attackers.

A compromised Active Directory environment can allow attackers to control large portions of an organization's infrastructure.

This section focuses on securing Active Directory through hardening, monitoring, auditing, and operational best practices.

---

# Active Directory Threat Landscape

Common attack objectives include:

- Credential theft
- Privilege escalation
- Lateral movement
- Persistence
- Domain dominance
- Data exfiltration

Attackers frequently attempt to compromise AD because it provides centralized control over enterprise resources.

---

# Common Attack Path

```text
Phishing

↓

Compromised Workstation

↓

Credential Theft

↓

Privilege Escalation

↓

Lateral Movement

↓

Domain Controller

↓

Domain Compromise
```

Breaking the attack chain at any stage reduces overall risk.

---

# Privileged Accounts

Privileged accounts require enhanced protection.

Examples:

- Domain Admins
- Enterprise Admins
- Schema Admins
- Backup Operators
- Service Accounts with elevated permissions

Recommendations:

- Limit membership
- Require MFA where supported
- Use separate administrative accounts
- Monitor logons
- Review membership regularly

---

# Tiered Administration

Separate administrative activities into security tiers.

Example:

```text
Tier 0

↓

Domain Controllers

↓

Enterprise Admins

----------------

Tier 1

↓

Servers

↓

Server Administrators

----------------

Tier 2

↓

Workstations

↓

Help Desk
```

Tiered administration reduces opportunities for credential theft and privilege escalation.

---

# Securing Domain Controllers

Domain Controllers should receive the highest level of protection.

Recommendations:

- Physically secure servers
- Restrict interactive logon
- Enable BitLocker
- Apply security baselines
- Enable advanced auditing
- Patch promptly
- Restrict internet access
- Monitor continuously

Only authorized administrators should manage Domain Controllers.

---

# Protecting Administrative Credentials

Administrative credentials should never be used for:

- Email
- Web browsing
- Routine office work
- Untrusted applications

Recommended approach:

```text
Daily Account

↓

Normal Work

----------------

Administrative Account

↓

Administrative Tasks Only
```

Separate accounts reduce exposure.

---

# Active Directory Hardening

Key hardening measures include:

- Least privilege
- Secure OU design
- Strong password policies
- MFA
- Windows LAPS
- Credential Guard
- Secure administrative workstations
- Restricted service accounts

Hardening should be continuously reviewed and updated.

---

# Secure Administrative Workstations (SAWs)

Administrative tasks should be performed from dedicated systems.

Benefits:

- Reduced malware exposure
- Controlled software installation
- Stronger monitoring
- Improved credential protection

Administrative workstations should not be used for general productivity tasks.

---

# Group Policy Security

Use Group Policy to enforce:

- Password policies
- Account lockout policies
- Firewall configuration
- Audit policies
- PowerShell logging
- BitLocker settings
- Defender configuration

Group Policy enables consistent enforcement across the domain.

---

# Monitoring Active Directory

Monitor for:

- Failed logons
- Privileged logons
- Group membership changes
- Account lockouts
- New administrator accounts
- Domain Controller changes
- Replication failures
- GPO modifications

Continuous monitoring improves detection of suspicious activity.

---

# Important Security Events

Examples of Windows Security Event IDs:

| Event ID | Description |
|-----------|-------------|
| 4624 | Successful logon |
| 4625 | Failed logon |
| 4720 | User account created |
| 4722 | User account enabled |
| 4725 | User account disabled |
| 4726 | User account deleted |
| 4728 | Added to a security-enabled global group |
| 4732 | Added to a security-enabled local group |
| 4738 | User account changed |
| 4740 | Account locked out |
| 4768 | Kerberos TGT requested |
| 4769 | Kerberos service ticket requested |
| 5136 | Directory object modified |

These events should be forwarded to a centralized logging or SIEM platform for analysis.

---

# Auditing Active Directory

Audit regularly:

- Privileged groups
- OU permissions
- Service accounts
- GPO changes
- Trust relationships
- Replication health
- FSMO role holders
- Inactive accounts

Routine audits improve security posture and compliance.

---

# Active Directory Backup

Backups should include:

- System State
- Active Directory database
- SYSVOL
- Group Policy Objects
- DNS (if integrated)

Backups should be encrypted, tested, and stored securely.

---

# Disaster Recovery

Recovery planning should address:

- Domain Controller failure
- Accidental object deletion
- Database corruption
- Site failure
- Ransomware incidents

Organizations should regularly test recovery procedures.

---

# Active Directory Recycle Bin

The Active Directory Recycle Bin allows recovery of deleted directory objects without requiring an authoritative restore.

Benefits:

- Faster recovery
- Preserved object attributes
- Reduced downtime

The feature should be enabled early in the lifecycle of a new forest after validating organizational requirements.

---

# Replication Health Monitoring

Monitor for:

- Replication latency
- Failed replication
- Lingering objects
- Site connectivity issues

Useful tools include:

- `repadmin`
- Event Viewer
- Active Directory Sites and Services

Healthy replication is essential for consistent authentication.

---

# Time Synchronization

Incorrect system time can cause:

- Kerberos failures
- Authentication errors
- Replication issues
- Inaccurate audit logs

Time should be synchronized using a reliable enterprise time source.

---

# Common Active Directory Attacks

Administrators should understand common attack techniques, including:

| Attack | Description |
|----------|-------------|
| Password Spraying | Trying common passwords across many accounts |
| Kerberoasting | Requesting service tickets to attempt offline password cracking |
| Pass-the-Hash | Reusing NTLM password hashes |
| Golden Ticket | Forging Kerberos TGTs using the KRBTGT account key |
| Silver Ticket | Forging Kerberos service tickets for a specific service |
| NTLM Relay | Relaying NTLM authentication to another service |
| DCSync | Abusing replication permissions to request password data from a Domain Controller |

Understanding these attacks helps defenders detect suspicious activity and implement appropriate mitigations.

---

# Defensive Measures

Recommended protections include:

- Enforce MFA for privileged users where supported
- Limit Domain Admin membership
- Enable Credential Guard
- Deploy Windows LAPS
- Disable legacy protocols where possible
- Monitor privileged group changes
- Secure Domain Controllers
- Regularly patch servers
- Enable advanced auditing
- Use secure administrative workstations

Defense should rely on multiple complementary controls.

---

# Active Directory Health Checks

Perform regular health checks for:

- DNS
- Replication
- FSMO roles
- Group Policy
- Time synchronization
- Domain Controller availability
- SYSVOL replication
- Backup status

Routine validation helps identify problems before they affect users.

---

# Troubleshooting Active Directory

General troubleshooting workflow:

```text
Identify Problem

↓

Collect Logs

↓

Verify DNS

↓

Check Domain Controller

↓

Review Replication

↓

Test Authentication

↓

Resolve Issue

↓

Document Findings
```

Structured troubleshooting reduces downtime.

---

# Common Issues

| Problem | Possible Cause | Resolution |
|----------|----------------|------------|
| Logon failure | DNS issue | Verify DNS configuration |
| Replication failure | Network connectivity | Check site links and replication status |
| Group Policy not applied | GPO scope or replication | Verify GPO linkage and replication |
| Authentication delay | Domain Controller unavailable | Check DC health and connectivity |
| Account lockouts | Repeated failed authentication | Investigate source and review logs |
| Kerberos errors | Time synchronization | Verify system time across the domain |

Always determine the root cause before applying corrective actions.

---

# Enterprise Example

A multinational enterprise operates:

- 25 Domain Controllers
- 8 Active Directory Sites
- 60,000 users

Security measures include:

- Tiered administration
- Windows LAPS
- Credential Guard
- BitLocker
- Microsoft Defender
- Dedicated administrative workstations
- Centralized SIEM monitoring
- Quarterly privileged access reviews
- Automated replication health monitoring

The organization significantly reduces the likelihood of unauthorized privilege escalation while improving operational resilience.

---

# Cybersecurity Perspective

Active Directory often represents the "crown jewels" of a Windows enterprise.

Security priorities include:

- Protecting privileged identities
- Monitoring authentication
- Detecting abnormal administrative activity
- Preventing credential theft
- Maintaining replication integrity
- Ensuring rapid recovery

A layered security strategy provides the strongest protection.

---

# Business Impact

A secure Active Directory environment provides:

- Reliable authentication
- Stronger access control
- Faster user provisioning
- Simplified compliance
- Reduced security incidents
- Improved business continuity
- Lower operational costs

Compromise of Active Directory can disrupt nearly every business function, making proactive protection essential.

---

# Enterprise Best Practices

- Minimize privileged account membership.
- Use dedicated administrative accounts.
- Implement tiered administration.
- Secure Domain Controllers physically and logically.
- Enable advanced auditing and centralized logging.
- Review privileged groups regularly.
- Monitor replication and DNS health.
- Test backups and disaster recovery procedures.
- Automate security and health checks where possible.
- Review Active Directory architecture periodically.

---

# Practical Labs

## Lab 1 — Review Privileged Groups

Using **Active Directory Users and Computers**:

Review membership of:

- Domain Admins
- Enterprise Admins
- Schema Admins

Identify whether all members require their assigned privileges.

---

## Lab 2 — Design a Tiered Administration Model

Create a three-tier administrative model for:

- Domain Controllers
- Member Servers
- Workstations

Assign appropriate administrative roles to each tier.

---

## Lab 3 — Active Directory Health Checklist

Develop a weekly checklist covering:

- DNS
- Replication
- Backups
- FSMO roles
- Event logs
- Privileged group review

Explain how each check contributes to security and availability.

---

## Lab 4 — Incident Response Scenario

Assume an administrator account has been added unexpectedly to the **Domain Admins** group.

Document the response process, including:

- Detection
- Verification
- Containment
- Investigation
- Recovery
- Lessons learned

---

# Chapter Summary

In this chapter, you learned:

- Active Directory architecture
- Forests, trees, domains, and OUs
- Domain Controllers
- LDAP and DNS integration
- Kerberos and NTLM authentication
- FSMO roles
- Replication
- Trust relationships
- User and group administration
- Delegation
- Active Directory security
- Hardening
- Monitoring
- Disaster recovery
- Troubleshooting

These concepts form the foundation of enterprise identity and access management in Windows environments.

---

# Key Takeaways

- Active Directory centralizes authentication and authorization.
- Kerberos is the preferred authentication protocol.
- DNS is critical for Active Directory functionality.
- Least privilege and delegated administration improve security.
- Domain Controllers require the highest level of protection.
- Continuous monitoring and auditing strengthen Active Directory security.
- Regular backups and tested recovery procedures are essential for resilience.

---

# Interview Questions

1. What is the purpose of Active Directory?
2. Explain the difference between a forest, tree, and domain.
3. What are the five FSMO roles?
4. How does Kerberos authentication work?
5. Why is DNS required for Active Directory?
6. What is the AGDLP model?
7. What is tiered administration?
8. Why are Domain Controllers considered critical assets?
9. What is the Active Directory Recycle Bin?
10. Name several common attacks targeting Active Directory and explain how they can be mitigated.

---

# References

- Microsoft Learn
- Microsoft Active Directory Documentation
- Microsoft Windows Server Documentation
- Microsoft Kerberos Documentation
- Microsoft Group Policy Documentation
- Microsoft Security Baselines
- NIST SP 800-53
- CIS Microsoft Windows Server Benchmarks
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- *Mastering Active Directory* (Dishan Francis)

---

# Congratulations!

You have successfully completed **Chapter 23 – Active Directory**.

You now understand Active Directory architecture, authentication, administration, replication, security, monitoring, and enterprise best practices. These concepts are fundamental for Windows administrators, SOC analysts, incident responders, penetration testers, security engineers, and enterprise infrastructure professionals.

---
