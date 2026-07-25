# 28-Active-Directory-Cheat-Sheet.md

# Part 1 — Ultimate Active Directory Cheat Sheet (Quick Revision Guide)

> **Purpose**
>
> This chapter is designed as a **rapid revision guide** for interviews, certifications, troubleshooting, and day-to-day administration. It summarizes the most important Active Directory concepts covered throughout this handbook.

---

# Learning Objectives

After completing this part, you will have a quick reference for:

- Core Active Directory concepts
- Important terminology
- Authentication
- Directory structure
- Administration
- Security
- Troubleshooting
- Interview revision

---

# Active Directory Overview

| Item | Description |
|------|-------------|
| Full Name | Active Directory Domain Services (AD DS) |
| Vendor | Microsoft |
| Purpose | Centralized Identity and Access Management |
| Introduced | Windows Server 2000 |
| Primary Function | Authentication & Authorization |

---

# Core Components

```
Forest
   │
   ▼
Tree
   │
   ▼
Domain
   │
   ▼
Organizational Unit
   │
   ▼
Users / Groups / Computers
```

---

# Logical Components

| Component | Purpose |
|-----------|---------|
| Forest | Highest security boundary |
| Tree | Collection of related domains |
| Domain | Administrative boundary |
| OU | Organize objects & apply GPOs |
| Group | Permission management |
| User | Identity |
| Computer | Managed endpoint |

---

# Physical Components

| Component | Purpose |
|-----------|---------|
| Domain Controller | Stores directory database |
| Site | Physical network location |
| Site Link | Connects sites |
| Global Catalog | Partial searchable directory |
| DNS | Service discovery |

---

# Authentication

```
User

↓

Kerberos

↓

Domain Controller

↓

Authentication

↓

Access Granted
```

---

# Authentication Protocols

| Protocol | Purpose |
|----------|----------|
| Kerberos | Default authentication |
| NTLM | Legacy authentication |
| LDAP | Directory queries |
| DNS | Locate AD services |

---

# Authorization

```
Authentication

↓

Authorization

↓

Resource Access
```

Authentication proves **who you are**.

Authorization determines **what you can access**.

---

# Important Ports

| Service | Port |
|----------|------|
| DNS | 53 |
| Kerberos | 88 |
| LDAP | 389 |
| LDAPS | 636 |
| Global Catalog | 3268 |
| Global Catalog SSL | 3269 |

---

# Active Directory Objects

| Object | Purpose |
|---------|----------|
| User | Identity |
| Computer | Endpoint |
| Group | Permission management |
| Contact | Directory information |
| Printer | Shared resource |
| Shared Folder | File access |
| Organizational Unit | Administration |

---

# Group Types

| Type | Purpose |
|------|----------|
| Security Group | Access permissions |
| Distribution Group | Email distribution |

---

# Group Scopes

| Scope | Usage |
|--------|-------|
| Domain Local | Resource permissions |
| Global | Users within domain |
| Universal | Multi-domain environments |

---

# FSMO Roles

| Role | Scope |
|------|--------|
| Schema Master | Forest |
| Domain Naming Master | Forest |
| RID Master | Domain |
| PDC Emulator | Domain |
| Infrastructure Master | Domain |

---

# Replication

```
Directory Change

↓

Replication

↓

Other Domain Controllers

↓

Directory Updated
```

Purpose:

- Consistency
- Availability
- Fault tolerance

---

# Group Policy

Can be linked to:

- Site
- Domain
- Organizational Unit

Common Uses:

- Password Policy
- Desktop Configuration
- Security Settings
- Software Deployment
- Administrative Templates

---

# DNS Quick Facts

- Required for Active Directory
- Locates Domain Controllers
- Supports Kerberos
- Enables replication
- Required for Group Policy processing

---

# Global Catalog

Purpose:

- Universal searches
- Universal Group Membership
- Forest-wide object lookup
- User logon support

---

# Organizational Units

Purpose:

- Organize objects
- Delegate administration
- Apply Group Policy
- Simplify management

---

# Trust Types

| Trust | Purpose |
|--------|----------|
| Parent-Child | Automatic |
| Tree Root | Automatic |
| External | Separate forests/domains |
| Forest Trust | Forest communication |
| Shortcut Trust | Faster authentication |

---

# Common Administrative Tools

| Tool | Purpose |
|------|----------|
| Active Directory Users and Computers | Manage objects |
| Active Directory Sites and Services | Replication |
| Active Directory Domains and Trusts | Trust management |
| Group Policy Management | GPO administration |
| DNS Manager | DNS management |
| Event Viewer | Logs |
| PowerShell | Automation |

---

# Microsoft Entra ID

Purpose:

- Cloud identity
- Hybrid identity
- SSO
- MFA
- Conditional Access
- Identity governance

---

# Security Principles

- Least Privilege
- Defense in Depth
- Multi-Factor Authentication
- Zero Trust
- Identity Governance
- Continuous Monitoring
- Separation of Duties

---

# Troubleshooting Workflow

```
Identify Problem

↓

Determine Scope

↓

Collect Evidence

↓

Analyze

↓

Root Cause

↓

Fix

↓

Validate

↓

Document
```

---

# Common Problems

| Problem | First Thing to Check |
|----------|----------------------|
| Login Failure | DNS |
| Slow Login | DNS & Network |
| GPO Failure | OU & Replication |
| Replication Delay | Replication Health |
| Authentication Failure | Time & DNS |
| Cloud Login Issue | Identity Synchronization |

---

# Interview Keywords

Know these terms:

- Forest
- Domain
- Tree
- OU
- LDAP
- Kerberos
- NTLM
- FSMO
- Global Catalog
- Replication
- GPO
- DNS
- Domain Controller
- Microsoft Entra ID
- Conditional Access
- MFA

---

# Memory Trick

```
Forest

↓

Tree

↓

Domain

↓

OU

↓

Users
```

Remember:

> **F → T → D → O → U**

---

# 15-Second Revision

- Forest = Highest boundary
- Domain = Security boundary
- OU = Organization
- Group = Permissions
- Kerberos = Authentication
- LDAP = Directory access
- DNS = Service discovery
- GPO = Configuration management
- DC = Authentication server
- Entra ID = Cloud identity

---

# Beginner Interview Revision

You should confidently answer:

- What is Active Directory?
- What is a Domain?
- What is a Forest?
- What is an OU?
- What is LDAP?
- What is Kerberos?
- What is DNS?
- What is a Domain Controller?
- What is Group Policy?
- What is Replication?

---

# Administrator Revision

Know how to:

- Create users
- Manage groups
- Join computers to a domain
- Apply Group Policy
- Delegate administration
- Monitor replication
- Review event logs
- Troubleshoot authentication

---

# Security Revision

Remember:

- MFA
- Least Privilege
- Conditional Access
- Zero Trust
- Identity Governance
- Auditing
- Monitoring
- Secure Backups

---

# Key Takeaways

- Active Directory is Microsoft's centralized identity platform.
- DNS, Kerberos, LDAP, and Group Policy are foundational technologies.
- Forests, Domains, OUs, and Domain Controllers form the core architecture.
- Security, monitoring, and documentation are essential for enterprise environments.
- A structured troubleshooting approach improves reliability and operational maturity.

---

**Next:** Part 2