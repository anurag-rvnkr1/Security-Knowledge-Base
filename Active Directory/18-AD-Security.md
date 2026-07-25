# 18-AD-Security.md

# Part 1 — Introduction to Active Directory Security, Security Principles, Identity Protection and Administrative Security

---

# Learning Objectives

After completing this part, you will understand:

- Why Active Directory Security is Critical
- Active Directory Threat Landscape
- Identity as the New Security Perimeter
- CIA Triad in Active Directory
- Authentication vs Authorization
- Principle of Least Privilege
- Administrative Tiering
- Privileged Accounts
- Secure Administrative Workstations (SAWs/PAWs)
- Security Baselines
- Enterprise Security Model

---

# Introduction

Active Directory is often called the **heart of a Windows enterprise** because it stores and manages:

- User identities
- Computer identities
- Authentication
- Authorization
- Group memberships
- Organizational Units
- Trust relationships
- Group Policies
- Service Accounts

If an attacker gains control of Active Directory, they can often gain control of the entire Windows environment.

Therefore, securing Active Directory is one of the highest priorities for enterprise defenders.

---

# Why Active Directory is a High-Value Target

Almost every business-critical system depends on Active Directory.

```
Employees

        │

        ▼

Active Directory

        │

 ┌──────┼───────────────┐

 ▼      ▼               ▼

Email  File Servers   Business Apps

        ▼

Databases

        ▼

Cloud Services

        ▼

Production Systems
```

Compromising Active Directory may allow unauthorized access to many enterprise resources.

---

# Active Directory Security Goals

The primary objectives are:

- Protect identities
- Protect privileged accounts
- Protect authentication
- Protect Domain Controllers
- Protect sensitive data
- Ensure service availability
- Detect malicious activity
- Support rapid incident response

---

# Security Objectives

```
Prevent

↓

Detect

↓

Respond

↓

Recover

↓

Improve
```

Modern Active Directory security is built on continuous improvement rather than one-time configuration.

---

# The CIA Triad

The CIA Triad forms the foundation of information security.

```
            Security

      ┌────────┼────────┐

      ▼        ▼        ▼

Confidentiality

Integrity

Availability
```

---

# Confidentiality

Confidentiality ensures information is only accessible to authorized users.

Examples:

- User passwords
- Group memberships
- Administrative credentials
- Certificate private keys
- Security policies

Controls include:

- Access control
- Encryption
- Least privilege
- Strong authentication

---

# Integrity

Integrity ensures information is accurate and protected from unauthorized modification.

Examples:

- Group Policy Objects
- User attributes
- DNS records
- Security groups
- Trust relationships

Controls include:

- Access permissions
- Auditing
- Change management
- Digital signatures (where applicable)

---

# Availability

Availability ensures systems remain operational for legitimate users.

Examples:

- Domain Controllers
- DNS
- Kerberos
- LDAP
- Global Catalog
- SYSVOL

Controls include:

- Redundant Domain Controllers
- Backups
- Monitoring
- Replication
- Disaster recovery planning

---

# Identity is the New Security Perimeter

Traditional security focused primarily on protecting network boundaries.

Modern enterprise environments rely heavily on protecting identities.

```
Old Model

Firewall

↓

Internal Network

-------------------------

Modern Model

Identity

↓

Authentication

↓

Authorization

↓

Resources
```

Identity protection is therefore a core element of Active Directory security.

---

# Authentication vs Authorization

These concepts are related but distinct.

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you access?" |
| Uses credentials | Uses permissions and policies |
| Occurs before access | Occurs after authentication |

Both processes are essential for secure access control.

---

# Principle of Least Privilege

The Principle of Least Privilege (PoLP) states that users and administrators should receive only the permissions required to perform their tasks.

```
Employee

↓

Only Required Access

↓

Nothing More
```

Benefits include:

- Reduced attack surface
- Lower risk of accidental changes
- Easier auditing
- Improved security

---

# Excessive Privileges

Granting unnecessary permissions can increase organizational risk.

Example:

```
Help Desk

↓

Domain Admin Rights

↓

High Risk
```

Instead:

```
Help Desk

↓

Password Reset

Unlock Accounts

↓

Limited Risk
```

Delegated permissions are generally preferable to broad administrative privileges.

---

# Administrative Tiering

Administrative Tiering separates administrative responsibilities based on the sensitivity of managed systems.

Example:

```
Tier 0

Domain Controllers

Forest

Authentication

--------------------

Tier 1

Servers

Applications

--------------------

Tier 2

User Workstations
```

Administrative accounts should be restricted to the tier they are intended to manage.

---

# Tiered Administration Benefits

- Reduces credential exposure
- Limits lateral movement opportunities
- Protects privileged identities
- Simplifies administrative boundaries
- Improves incident containment

---

# Privileged Accounts

Privileged accounts include:

- Domain Administrators
- Enterprise Administrators
- Schema Administrators
- Backup Operators
- Server Administrators
- Service Accounts with elevated privileges

These accounts require additional protection.

---

# Administrative Account Separation

A common enterprise practice is to use separate accounts for different activities.

Example:

```
Normal User Account

↓

Email

Web Browsing

Documentation

-----------------------

Administrative Account

↓

Server Management

Active Directory

PowerShell

Administration
```

This separation reduces the likelihood that privileged credentials are exposed during routine activities.

---

# Secure Administrative Workstations (SAWs/PAWs)

Many organizations use dedicated administrative workstations for privileged tasks.

```
Privileged Access Workstation

↓

Administrative Login

↓

Domain Controller

↓

Administrative Tasks
```

Characteristics include:

- Restricted software
- Hardened configuration
- Limited internet access
- Enhanced monitoring
- Dedicated administrative use

---

# Security Baselines

A security baseline defines a secure starting configuration.

Examples include:

- Password policy
- Account lockout policy
- Audit policy
- Firewall settings
- Remote management configuration
- Administrative restrictions

Baselines help ensure consistency across systems.

---

# Defense in Depth

No single security control is sufficient.

```
User Awareness

↓

Identity Security

↓

Least Privilege

↓

Endpoint Protection

↓

Network Security

↓

Monitoring

↓

Incident Response
```

Multiple overlapping controls improve resilience.

---

# Shared Responsibility

Active Directory security involves multiple teams.

```
IT Operations

↓

Identity Team

↓

Security Operations

↓

Help Desk

↓

Management

↓

Compliance
```

Effective security depends on coordination across these groups.

---

# Enterprise Security Workflow

```
User Requests Access

↓

Manager Approval

↓

Identity Provisioning

↓

Least Privilege

↓

Authentication

↓

Authorization

↓

Monitoring

↓

Periodic Review
```

Regular access reviews help ensure permissions remain appropriate.

---

# Enterprise Example

Company:

```
Apex Manufacturing
```

Environment:

- 70,000 Users
- 25 Domain Controllers
- Multiple Regional Offices

Security Controls:

- Tiered Administration
- Dedicated Administrative Accounts
- Secure Administrative Workstations
- Multi-Factor Authentication (where implemented)
- Continuous Monitoring
- Centralized Logging
- Regular Privileged Access Reviews

These layered controls reduce the likelihood and impact of credential compromise.

---

# Cybersecurity Perspective

Modern attackers frequently target identities rather than infrastructure alone.

Defensive priorities include:

- Protect privileged accounts.
- Minimize standing administrative privileges.
- Use separate administrative accounts.
- Restrict administrative logon locations.
- Monitor privileged authentication events.
- Regularly review privileged group memberships.
- Apply security updates promptly.
- Conduct periodic security assessments.

Protecting identities is often the most effective way to protect the entire Active Directory environment.

---

# Hands-on Lab

## Objective

Review the security posture of an Active Directory environment.

### Step 1

Identify privileged groups such as:

- Domain Admins
- Enterprise Admins
- Schema Admins
- Account Operators

Document their intended responsibilities.

---

### Step 2

Review the organization's administrative account model.

Determine whether separate standard and administrative accounts are used.

---

### Step 3

Map the environment into administrative tiers.

Identify which systems belong to:

- Tier 0
- Tier 1
- Tier 2

---

### Step 4

Review the current password and account lockout policies.

Document key settings and compare them with organizational standards.

---

### Step 5

Create a simple diagram showing how authentication and authorization work together within Active Directory.

---

# Interview Questions

### Q1: Why is Active Directory considered a high-value target?

**Answer:** Because it manages authentication, authorization, identities, and access to critical enterprise resources. Compromising Active Directory can significantly affect the security of the entire environment.

---

### Q2: What is the Principle of Least Privilege?

**Answer:** It is the practice of granting users and administrators only the permissions necessary to perform their assigned responsibilities.

---

### Q3: What is the difference between authentication and authorization?

**Answer:** Authentication verifies a user's identity, while authorization determines what resources and actions that authenticated user is permitted to access.

---

### Q4: Why should organizations use separate administrative accounts?

**Answer:** Separate administrative accounts reduce the exposure of privileged credentials during routine activities such as email, web browsing, or document editing.

---

### Q5: What is administrative tiering?

**Answer:** Administrative tiering separates privileged administration based on system sensitivity, helping reduce credential exposure and limit the impact of compromise.

---

### Q6: What is the purpose of a Privileged Access Workstation (PAW)?

**Answer:** A PAW is a hardened, dedicated workstation used exclusively for administrative tasks, reducing the risk of privileged credential theft.

---

# Best Practices

- Apply the Principle of Least Privilege.
- Use dedicated administrative accounts.
- Protect Tier 0 assets with the strongest controls.
- Use secure administrative workstations where feasible.
- Review privileged group memberships regularly.
- Enable comprehensive auditing.
- Implement layered security controls.
- Conduct periodic access reviews.

---

# Common Mistakes

- Using Domain Administrator accounts for everyday work.
- Granting excessive permissions.
- Sharing privileged accounts.
- Ignoring administrative account reviews.
- Allowing privileged logons from unmanaged devices.
- Treating identity security as solely a network security issue.
- Relying on a single security control.

---

# Key Takeaways

- Active Directory is one of the most critical components of enterprise infrastructure.
- Identity protection is central to modern cybersecurity.
- The CIA Triad provides the foundation for securing Active Directory.
- Least privilege, administrative tiering, and dedicated administrative accounts significantly reduce organizational risk.
- Layered security, monitoring, and governance are essential for protecting enterprise identity systems.

---

**Next:** Part 2