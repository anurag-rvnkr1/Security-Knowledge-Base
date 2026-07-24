# 18-Windows-Security.md

# Part 1 — Windows Security Fundamentals, Security Architecture, Authentication, Authorization, and Core Security Components

---

# Introduction

Windows Security is a comprehensive framework of technologies, services, policies, and mechanisms designed to protect:

- Users
- Devices
- Applications
- Data
- Networks
- Enterprise infrastructure

Modern Windows operating systems provide multiple layers of defense that work together to protect against malware, ransomware, credential theft, insider threats, and advanced persistent threats (APTs).

Security in Windows follows the principle of **Defense in Depth**, meaning multiple independent security controls protect the system.

---

# Learning Objectives

By the end of this section, you will understand:

- Windows security architecture
- Security principles
- CIA Triad
- Defense in Depth
- Authentication
- Authorization
- Security Identifiers (SID)
- Access Tokens
- User Account Control (UAC)
- Local Security Authority (LSA)
- Security Accounts Manager (SAM)
- Windows security components
- Enterprise security architecture

---

# What is Windows Security?

Windows Security is the collection of built-in technologies that protect the operating system from:

- Unauthorized access
- Malware
- Credential theft
- Data leakage
- Privilege escalation
- System compromise

It combines hardware, software, and policy-based protections.

---

# Security Goals

Windows Security aims to ensure:

- Confidentiality
- Integrity
- Availability
- Accountability
- Authenticity
- Non-repudiation

These goals guide the design of enterprise security controls.

---

# CIA Triad

The CIA Triad forms the foundation of information security.

```text
        Confidentiality
              ▲
             / \
            /   \
Integrity -------- Availability
```

### Confidentiality

Protect information from unauthorized access.

Examples:

- Encryption
- Access control
- Authentication

---

### Integrity

Ensure data remains accurate and unmodified.

Examples:

- Hashing
- Digital signatures
- File integrity monitoring

---

### Availability

Ensure systems remain accessible.

Examples:

- Backups
- Redundancy
- High Availability
- Disaster Recovery

---

# Defense in Depth

Windows applies multiple security layers.

```text
User

↓

Authentication

↓

Authorization

↓

Operating System

↓

Applications

↓

Network

↓

Hardware
```

If one control fails, additional layers continue to provide protection.

---

# Principle of Least Privilege

Users and applications should receive **only the permissions required** to perform their tasks.

Example:

```text
Employee

↓

Read Documents

✓

Delete System Files

✗
```

Least privilege reduces the impact of compromised accounts.

---

# Zero Trust Concept

Modern enterprise security follows the **Zero Trust** model.

Core principles:

- Never trust automatically.
- Verify every request.
- Assume breach.
- Continuously validate identity.
- Limit access.

```text
User

↓

Verify Identity

↓

Verify Device

↓

Verify Policy

↓

Grant Limited Access
```

---

# Windows Security Architecture

```text
Applications

↓

Security APIs

↓

Local Security Authority (LSA)

↓

Authentication Packages

↓

SAM / Active Directory

↓

Access Token

↓

Protected Resource
```

Multiple components cooperate during authentication and authorization.

---

# Windows Security Components

Major security components include:

| Component | Purpose |
|----------|----------|
| LSA | Security policy enforcement |
| SAM | Local account database |
| Active Directory | Domain authentication |
| UAC | Privilege management |
| Windows Defender | Malware protection |
| BitLocker | Disk encryption |
| Windows Firewall | Network protection |
| Secure Boot | Boot integrity |
| Credential Guard | Credential protection |

Each component contributes to the overall security posture.

---

# Authentication

Authentication answers the question:

> **"Who are you?"**

Common authentication methods:

- Password
- PIN
- Smart Card
- Biometrics
- Windows Hello
- Multi-Factor Authentication (MFA)

Authentication verifies identity before access is granted.

---

# Authentication Workflow

```text
User

↓

Credentials

↓

Authentication Service

↓

Identity Verified

↓

Access Token Created
```

Successful authentication does not automatically grant unrestricted access.

---

# Authorization

Authorization answers:

> **"What are you allowed to do?"**

Examples:

| User | Permission |
|------|------------|
| Alice | Read |
| Bob | Read + Write |
| Admin | Full Control |

Authorization occurs after successful authentication.

---

# Authentication vs Authorization

| Authentication | Authorization |
|---------------|---------------|
| Identifies user | Determines permissions |
| Occurs first | Occurs second |
| Verifies identity | Grants resource access |
| Password/MFA | ACLs/Permissions |

Both processes are essential.

---

# Security Identifier (SID)

Every Windows security principal receives a unique **Security Identifier (SID).**

Examples:

- User accounts
- Groups
- Computer accounts

Example:

```text
S-1-5-21-3623811015-
3361044348-
30300820-1013
```

Windows uses SIDs internally rather than usernames.

---

# SID Structure

```text
Revision

↓

Authority

↓

Domain Identifier

↓

Relative Identifier (RID)
```

The RID uniquely identifies the account within a domain or local system.

---

# Relative Identifier (RID)

Common RIDs include:

| RID | Account |
|------|----------|
| 500 | Built-in Administrator |
| 501 | Guest |
| 512 | Domain Admins |
| 513 | Domain Users |

These identifiers are consistent across Windows domains.

---

# Security Principals

Security principals include:

- Users
- Groups
- Computers
- Managed Service Accounts
- Services

Each principal possesses its own SID.

---

# Access Token

After authentication, Windows creates an **Access Token**.

The token contains:

- User SID
- Group SIDs
- Privileges
- Integrity Level
- Security Attributes

Windows uses the access token during authorization.

---

# Access Token Workflow

```text
User Login

↓

Authentication

↓

Access Token Created

↓

Application Starts

↓

Application Uses Token

↓

Resource Access
```

Every process launched by a user inherits that user's access token unless elevation occurs.

---

# Access Check

Whenever a protected resource is accessed:

```text
Application

↓

Access Token

↓

ACL

↓

Access Decision
```

Windows compares the user's token with the resource's permissions.

---

# Local Security Authority (LSA)

The **Local Security Authority (LSA)** is responsible for:

- User authentication
- Security policy enforcement
- Access token creation
- Password validation
- Security auditing

The primary process is:

```text
lsass.exe
```

LSA is one of the most critical Windows security components.

---

# Security Accounts Manager (SAM)

SAM stores:

- Local user accounts
- Local groups
- Password hashes

Location:

```text
C:\Windows\System32\config\SAM
```

Direct access is restricted while Windows is running.

---

# Active Directory Authentication

In a domain environment:

```text
User

↓

Domain Controller

↓

Kerberos

↓

Access Token

↓

Domain Resources
```

Active Directory replaces local authentication for domain accounts.

---

# User Account Control (UAC)

UAC reduces the risk of unintended administrative actions.

Workflow:

```text
Standard Token

↓

Administrative Action

↓

UAC Prompt

↓

Approval

↓

Elevated Token
```

UAC helps prevent silent privilege escalation.

---

# Integrity Levels

Windows assigns integrity levels to processes.

| Integrity Level | Typical Usage |
|----------------|---------------|
| Low | Sandboxed applications |
| Medium | Standard user processes |
| High | Elevated administrator processes |
| System | Operating system components |

Higher integrity processes can perform more privileged operations.

---

# Windows Security Model

```text
User

↓

Authentication

↓

Access Token

↓

Authorization

↓

Security Reference Monitor

↓

Protected Object
```

The Security Reference Monitor evaluates every access request.

---

# Enterprise Authentication Example

An employee signs in using Windows Hello for Business.

Workflow:

```text
Windows Hello

↓

Biometric Verification

↓

Kerberos Authentication

↓

Access Token

↓

Corporate Resources
```

This reduces reliance on passwords while improving security.

---

# Cybersecurity Perspective

Attackers commonly target:

- Password hashes
- LSASS memory
- Access tokens
- Privileged accounts
- Misconfigured permissions

Defenders protect these components using technologies such as Credential Guard, MFA, and least privilege.

---

# Business Impact

Strong Windows security provides:

- Reduced cyber risk
- Regulatory compliance
- Protection of sensitive data
- Improved user trust
- Reduced incident response costs
- Better operational resilience

Security failures can result in data breaches, downtime, financial loss, and reputational damage.

---

# Enterprise Best Practices

- Enforce Multi-Factor Authentication (MFA).
- Implement least privilege.
- Keep systems fully patched.
- Use Windows Hello for Business where appropriate.
- Restrict local administrator usage.
- Monitor privileged account activity.
- Protect LSASS using Credential Guard.
- Regularly review account permissions.
- Remove unused accounts promptly.
- Follow Zero Trust principles.

---

# Practical Labs

## Lab 1 — View Current User SID

Run:

```cmd
whoami /user
```

Record:

- Username
- SID

---

## Lab 2 — View Group Membership

Run:

```cmd
whoami /groups
```

Identify all security groups associated with the current user.

---

## Lab 3 — Display Current Privileges

Run:

```cmd
whoami /priv
```

Review enabled and disabled privileges.

---

## Lab 4 — Examine UAC

Attempt to open **Command Prompt** as Administrator.

Observe:

- UAC prompt
- Permission request
- Elevated session

---

# Key Takeaways

- Windows Security is built on layered defense principles.
- Authentication verifies identity; authorization determines permissions.
- SIDs uniquely identify security principals.
- Access Tokens carry security information for running processes.
- LSA performs authentication and creates access tokens.
- SAM stores local account information.
- UAC reduces unintended privilege escalation.
- Least privilege and Zero Trust significantly strengthen enterprise security.

---

# Interview Questions

1. What is the difference between authentication and authorization?
2. What is a Security Identifier (SID)?
3. What information is stored in an Access Token?
4. What is the purpose of LSASS?
5. What is the Security Accounts Manager (SAM)?
6. Why is UAC important?
7. What are Windows Integrity Levels?
8. Explain the Principle of Least Privilege.
9. How does Windows enforce access control?
10. Why is Defense in Depth important?

---

# References

- Microsoft Learn
- Microsoft Windows Security Documentation
- Microsoft Windows Authentication Documentation
- Microsoft Security Architecture Documentation
- NIST Cybersecurity Framework
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

**Next:** **Part 2 — Windows Defender, Microsoft Defender Antivirus, Firewall Integration, SmartScreen, Secure Boot, TPM, BitLocker, and Credential Guard**