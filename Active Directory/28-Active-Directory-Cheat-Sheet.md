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

# 28-Active-Directory-Cheat-Sheet.md

# Part 2 — Active Directory Administration, PowerShell, Security and Troubleshooting Cheat Sheet

> **Purpose**
>
> This section provides a quick-reference guide for Active Directory administrators, system engineers, and cybersecurity professionals. It summarizes common administrative tasks, PowerShell cmdlets, security concepts, troubleshooting workflows, and operational best practices.

---

# Active Directory Administrative Workflow

```
Create User

↓

Assign Groups

↓

Move to OU

↓

Apply GPO

↓

Verify Access

↓

Monitor

↓

Audit
```

---

# Daily Administrator Checklist

| Task | Purpose |
|------|---------|
| Review Domain Controller health | Ensure availability |
| Check replication | Verify consistency |
| Review authentication logs | Detect issues |
| Monitor DNS | Ensure name resolution |
| Verify backups | Recovery readiness |
| Review privileged accounts | Security |
| Check storage and resources | Performance |
| Validate monitoring alerts | Operational awareness |

---

# Weekly Administrator Checklist

- Review inactive user accounts
- Review inactive computer accounts
- Validate Group Policy changes
- Review DNS health
- Verify replication status
- Review privileged group membership
- Check failed authentication trends
- Review system updates

---

# Monthly Administrator Checklist

- Test backup restoration procedures
- Review access permissions
- Audit administrative accounts
- Review delegated permissions
- Validate disaster recovery documentation
- Update operational documentation
- Review monitoring thresholds
- Conduct security review

---

# User Administration

Typical lifecycle:

```
Create User

↓

Assign Password

↓

Assign Groups

↓

Move to Correct OU

↓

Verify Login

↓

Assign Applications

↓

Monitor
```

---

# Group Administration

Best practices:

- Use groups instead of assigning permissions directly to users.
- Follow Role-Based Access Control (RBAC).
- Remove unused groups.
- Review memberships regularly.
- Document purpose and ownership.

---

# Computer Administration

Typical tasks:

- Join domain
- Rename computer (if required)
- Move to correct OU
- Apply Group Policy
- Verify updates
- Confirm security baseline

---

# Organizational Unit Administration

Use OUs to:

- Organize objects
- Delegate administration
- Apply Group Policies
- Separate departments
- Simplify management

Example:

```
Company

├── HR

├── Finance

├── IT

├── Sales

└── Servers
```

---

# PowerShell Cheat Sheet

## Get AD User

```powershell
Get-ADUser username
```

Purpose:

Retrieve user information.

---

## Get All Users

```powershell
Get-ADUser -Filter *
```

Purpose:

List all users.

---

## Get AD Computer

```powershell
Get-ADComputer -Filter *
```

Purpose:

List computers.

---

## Get AD Groups

```powershell
Get-ADGroup -Filter *
```

Purpose:

List groups.

---

## Get Group Members

```powershell
Get-ADGroupMember "IT Admins"
```

Purpose:

View members of a group.

---

## Unlock User Account

```powershell
Unlock-ADAccount username
```

Purpose:

Unlock a locked account.

---

## Disable User

```powershell
Disable-ADAccount username
```

Purpose:

Disable an account.

---

## Enable User

```powershell
Enable-ADAccount username
```

Purpose:

Enable an account.

---

## Reset Password

```powershell
Set-ADAccountPassword
```

Purpose:

Reset a user's password.

---

> **Note:** Exact parameters vary depending on your environment and organizational policies.

---

# Active Directory Security Cheat Sheet

## Least Privilege

```
Only Required Permissions

↓

Reduced Risk
```

---

## Defense in Depth

```
Identity

↓

Authentication

↓

Authorization

↓

Monitoring

↓

Auditing
```

---

## Multi-Factor Authentication

```
Password

+

Second Factor

↓

Authentication
```

---

## Zero Trust

```
Never Trust

↓

Always Verify

↓

Grant Access
```

---

## Privileged Accounts

Recommendations:

- Separate admin accounts
- MFA
- Access reviews
- Strong passwords
- Continuous monitoring
- Auditing

---

# Active Directory Health Checks

Review:

| Component | Verify |
|-----------|--------|
| Domain Controller | Healthy |
| DNS | Healthy |
| Replication | Successful |
| Authentication | Working |
| Group Policy | Applying |
| Time Service | Synchronized |
| Event Logs | No critical issues |

---

# Troubleshooting Quick Guide

## Login Failure

Check:

- User account
- Password
- DNS
- Domain Controller
- Time synchronization

---

## Group Policy Failure

Check:

- OU
- GPO Link
- Replication
- Client processing
- Event logs

---

## DNS Issues

Check:

- DNS service
- Zone health
- Client configuration
- Name resolution

---

## Replication Issues

Check:

- Domain Controller health
- Network
- Site topology
- Event logs
- Replication status

---

## Hybrid Identity Issues

Check:

- Synchronization
- User object
- Microsoft Entra ID
- Authentication
- Licensing (if applicable)

---

# Event Logs to Review

| Log | Purpose |
|-----|----------|
| System | Operating system events |
| Security | Authentication and auditing |
| Directory Service | Active Directory events |
| DNS Server | DNS operations |
| Application | Application events |

---

# Important Active Directory Services

| Service | Purpose |
|----------|----------|
| Active Directory Domain Services | Directory database |
| DNS Server | Name resolution |
| Netlogon | Domain logon |
| Kerberos KDC | Authentication |
| Windows Time | Time synchronization |

---

# Security Monitoring Checklist

Monitor:

- Failed logons
- Account lockouts
- Administrative changes
- Group membership changes
- Domain Controller health
- Replication issues
- Authentication trends
- Policy changes

---

# Backup Checklist

```
Backup Completed

↓

Verify Success

↓

Validate Integrity

↓

Store Securely

↓

Test Restoration

↓

Document Results
```

---

# Incident Response Workflow

```
Detect

↓

Investigate

↓

Analyze

↓

Resolve

↓

Validate

↓

Document

↓

Review
```

---

# Change Management Workflow

```
Request

↓

Risk Assessment

↓

Approval

↓

Implementation

↓

Validation

↓

Documentation
```

---

# Quick Architecture Diagram

```
                 Forest

                    │

          ┌─────────┴─────────┐

       Domain A           Domain B

           │                   │

        OUs                OUs

           │                   │

 Users • Groups • Computers
```

---

# Active Directory Best Practices

- Use multiple Domain Controllers.
- Keep DNS healthy.
- Apply Least Privilege.
- Enable MFA where possible.
- Review privileged accounts regularly.
- Test backups periodically.
- Monitor replication.
- Maintain documentation.
- Follow change management.
- Review logs frequently.

---

# 60-Second Administrator Revision

Remember:

- Forest = Highest logical boundary
- Domain = Security boundary
- OU = Administrative organization
- DNS = Required for AD
- Kerberos = Default authentication
- LDAP = Directory protocol
- GPO = Centralized configuration
- FSMO = Single-master operations
- Replication = Directory consistency
- Domain Controller = Authentication server
- Microsoft Entra ID = Cloud identity
- MFA = Strong authentication
- Zero Trust = Verify continuously

---

# Interview Flash Cards

| Question | Answer |
|----------|--------|
| Highest logical boundary? | Forest |
| Authentication protocol? | Kerberos |
| Directory protocol? | LDAP |
| Name resolution? | DNS |
| Cloud identity platform? | Microsoft Entra ID |
| Policy engine? | Group Policy |
| Authentication server? | Domain Controller |
| Security principle? | Least Privilege |
| Cloud access control? | Conditional Access |
| Strong authentication? | MFA |

---

# Key Takeaways

- Standardized administration improves operational consistency.
- PowerShell simplifies repetitive Active Directory management tasks.
- Security relies on identity governance, least privilege, MFA, and monitoring.
- Regular health checks and structured troubleshooting reduce downtime.
- Documentation, validation, and change management are essential enterprise practices.

---

# 28-Active-Directory-Cheat-Sheet.md

# Part 3 — Active Directory Security, Hybrid Identity, PowerShell, Ports, Services and Interview Revision Cheat Sheet

> **Purpose**
>
> This section is a **high-speed revision guide** for certifications, interviews, enterprise administration, and cybersecurity roles. It consolidates the most frequently referenced Active Directory security concepts, hybrid identity topics, PowerShell commands, networking information, and troubleshooting reminders.

---

# Active Directory Security Model

```
Identity

↓

Authentication

↓

Authorization

↓

Access Control

↓

Monitoring

↓

Auditing
```

Security begins with **identity** and continues throughout the user's lifecycle.

---

# Identity Lifecycle

```
Hire

↓

Create User

↓

Assign Groups

↓

Apply Policies

↓

Daily Administration

↓

Role Change

↓

Access Review

↓

Disable Account

↓

Archive
```

---

# Defense in Depth

```
User

↓

Password Policy

↓

Multi-Factor Authentication

↓

Conditional Access

↓

Least Privilege

↓

Monitoring

↓

Auditing
```

Multiple security layers reduce organizational risk.

---

# Zero Trust Principles

Always remember:

```
Never Trust

↓

Always Verify

↓

Least Privilege

↓

Continuous Validation
```

---

# Authentication Flow

```
User

↓

DNS

↓

Domain Controller

↓

Kerberos

↓

Authentication

↓

Authorization

↓

Access
```

---

# Kerberos Quick Revision

Purpose:

- Secure authentication
- Ticket-based authentication
- Reduces repeated password transmission
- Default Active Directory authentication protocol

Remember:

```
Client

↓

Authentication Request

↓

Ticket

↓

Service Access
```

---

# LDAP Quick Revision

Purpose:

- Query directory objects
- Modify directory information
- Search Active Directory

Examples:

- User lookup
- Group lookup
- Organizational Unit lookup

---

# DNS Quick Revision

DNS provides:

- Domain Controller discovery
- Global Catalog discovery
- Kerberos service discovery
- Replication support

Without DNS:

- Authentication may fail.
- Group Policy may fail.
- Replication may fail.

---

# Group Policy Quick Revision

Applied to:

- Sites
- Domains
- Organizational Units

Common configurations:

- Password policy
- Desktop settings
- Security options
- Administrative templates
- Software deployment

---

# FSMO Roles

| Role | Responsibility |
|------|----------------|
| Schema Master | Schema updates |
| Domain Naming Master | Domain additions/removals |
| RID Master | RID allocation |
| PDC Emulator | Password updates & time |
| Infrastructure Master | Cross-domain object references |

---

# Replication

Purpose:

```
Consistency

+

Availability

+

Fault Tolerance
```

Replication ensures all Domain Controllers maintain consistent directory information.

---

# Global Catalog

Purpose:

- Forest-wide searches
- Universal Group Membership
- User logon support
- Partial attribute storage

---

# Organizational Units

Remember:

```
OU

↓

Organization

↓

Delegation

↓

Group Policy
```

OUs are **not** security boundaries.

---

# Group Scope Revision

| Scope | Typical Usage |
|--------|---------------|
| Domain Local | Resource permissions |
| Global | Users within a domain |
| Universal | Multi-domain environments |

---

# Common Administrative Tools

| Tool | Purpose |
|------|----------|
| Active Directory Users and Computers | Object management |
| Active Directory Administrative Center | Modern administration |
| Active Directory Sites and Services | Replication management |
| Active Directory Domains and Trusts | Trust administration |
| Group Policy Management | GPO management |
| DNS Manager | DNS administration |
| Event Viewer | Log analysis |
| PowerShell | Automation |

---

# Frequently Used PowerShell Cmdlets

| Cmdlet | Purpose |
|---------|----------|
| `Get-ADUser` | View users |
| `New-ADUser` | Create user |
| `Set-ADUser` | Modify user |
| `Remove-ADUser` | Remove user |
| `Get-ADComputer` | View computers |
| `Get-ADGroup` | View groups |
| `Get-ADGroupMember` | List group members |
| `New-ADGroup` | Create group |
| `Add-ADGroupMember` | Add members |
| `Remove-ADGroupMember` | Remove members |
| `Unlock-ADAccount` | Unlock account |
| `Enable-ADAccount` | Enable account |
| `Disable-ADAccount` | Disable account |

---

# Common Active Directory Ports

| Protocol | Port | Purpose |
|-----------|-----:|----------|
| DNS | 53 | Name resolution |
| Kerberos | 88 | Authentication |
| LDAP | 389 | Directory access |
| LDAPS | 636 | Secure LDAP |
| SMB | 445 | File and directory services |
| Global Catalog | 3268 | Directory search |
| Global Catalog SSL | 3269 | Secure GC |
| RPC Endpoint Mapper | 135 | RPC service discovery |

---

# Important Windows Services

| Service | Purpose |
|----------|----------|
| Active Directory Domain Services | Directory database |
| DNS Server | Name resolution |
| Netlogon | Domain authentication |
| Kerberos KDC | Ticket issuance |
| Windows Time | Time synchronization |

---

# Hybrid Identity

```
On-Premises AD

↓

Identity Synchronization

↓

Microsoft Entra ID

↓

Microsoft 365

↓

Cloud Applications
```

---

# Microsoft Entra ID Features

- Single Sign-On (SSO)
- Multi-Factor Authentication (MFA)
- Conditional Access
- Identity Governance
- Cloud Identity
- Hybrid Identity
- Self-service capabilities

---

# Conditional Access

Evaluates:

- User
- Device
- Location
- Risk
- Application
- Organizational policy

```
User

↓

Policy Evaluation

↓

Allow

OR

Require Additional Verification

OR

Block
```

---

# Troubleshooting Checklist

## User Cannot Log In

Check:

- Account status
- Password
- DNS
- Domain Controller
- Time synchronization
- Network connectivity

---

## Replication Problems

Review:

- Domain Controllers
- DNS
- Network
- Site topology
- Event logs

---

## Group Policy Problems

Verify:

- OU placement
- GPO link
- Replication
- Policy processing
- Event logs

---

## DNS Problems

Review:

- DNS server health
- Zone configuration
- Client configuration
- Name resolution

---

# Event Logs

Most useful logs:

| Log | Purpose |
|------|----------|
| Security | Authentication |
| System | Operating system |
| Directory Service | AD events |
| DNS Server | DNS events |
| Application | Applications |

---

# Backup Checklist

```
Backup

↓

Verify

↓

Store Securely

↓

Test Restore

↓

Document
```

---

# Disaster Recovery Checklist

- Backup available
- Recovery documentation
- Domain Controller redundancy
- DNS redundancy
- Replication validation
- Authentication verification
- Business validation

---

# Security Checklist

Daily:

- Review failed logons
- Review privileged accounts
- Check replication
- Verify DNS
- Review alerts

Weekly:

- Review inactive accounts
- Review group memberships
- Validate backups
- Audit administrative changes

Monthly:

- Test recovery procedures
- Review access permissions
- Validate documentation
- Review security policies

---

# Active Directory Best Practices

- Deploy multiple Domain Controllers.
- Use Role-Based Access Control (RBAC).
- Follow Least Privilege.
- Protect privileged accounts.
- Enable MFA where supported.
- Keep DNS healthy.
- Monitor replication.
- Review logs regularly.
- Test backups.
- Document changes.

---

# One-Page Interview Revision

## Core Concepts

- Active Directory
- Forest
- Domain
- Tree
- Organizational Unit
- User
- Group
- Computer

---

## Authentication

- Kerberos
- LDAP
- DNS
- Domain Controller

---

## Administration

- User management
- Group management
- GPO
- Replication
- FSMO
- Global Catalog

---

## Security

- MFA
- Conditional Access
- Least Privilege
- Zero Trust
- Identity Governance

---

## Troubleshooting

- DNS
- Replication
- Authentication
- Group Policy
- Domain Controller Health

---

# 2-Minute Interview Revision

If you only have two minutes before an interview, remember:

1. Forest is the highest logical boundary.
2. Domains provide administrative and security boundaries.
3. OUs organize objects and receive GPOs.
4. Kerberos is the default authentication protocol.
5. LDAP queries directory data.
6. DNS is essential for Active Directory.
7. Domain Controllers authenticate users.
8. Replication keeps directory data consistent.
9. FSMO roles coordinate specific directory operations.
10. Microsoft Entra ID extends identity into the cloud.

---

# Memory Map

```
                Active Directory

                       │

      ┌────────────────┼────────────────┐

 Authentication   Administration    Security

      │                 │               │

 Kerberos          Users          Least Privilege

 LDAP              Groups         MFA

 DNS               GPO            Zero Trust

 DC                FSMO           Monitoring

 Replication       OUs            Auditing

 Hybrid Identity   PowerShell     Governance
```

---

# Key Takeaways

- Active Directory administration combines identity management, security, networking, and troubleshooting.
- DNS, Kerberos, LDAP, Group Policy, and replication form the foundation of AD.
- Microsoft Entra ID extends Active Directory into hybrid cloud environments.
- Consistent monitoring, documentation, and least privilege improve enterprise security and reliability.
- This cheat sheet is intended as a rapid revision guide before interviews, certifications, or operational tasks.

---

**Next:** Part 4