# 12-Kerberos-and-NTLM.md

# Part 1 — Windows Authentication Fundamentals

---

# Learning Objectives

After completing this chapter, you will understand:

- Why authentication is important
- Authentication vs Authorization
- Identity in Active Directory
- Windows authentication methods
- Kerberos
- NTLM
- Single Sign-On (SSO)
- Authentication workflow
- Domain logon process
- Credentials and tokens
- Enterprise authentication architecture
- Security concepts and best practices

---

# Introduction

Every day, millions of users log into Windows computers.

When a user enters:

```
Username

Password
```

Windows must answer several questions:

- Who is this user?
- Is the password correct?
- Which Domain Controller should verify it?
- What resources can this user access?
- Which permissions should be granted?

This entire process is called **Authentication**.

---

# What is Authentication?

Authentication is the process of verifying the identity of a user, computer, or service.

Simply put:

> Authentication answers the question:

```
Who are you?
```

Examples:

- Logging into Windows
- Connecting to a VPN
- Accessing Outlook
- Opening a file share
- Signing into Microsoft Teams
- Connecting to SQL Server

All require authentication.

---

# Authentication vs Authorization

These two terms are often confused.

They are completely different.

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you do?" |
| Happens first | Happens after authentication |
| Checks credentials | Checks access rights |

---

# Example

A user logs into Windows.

Step 1

```
Username

anurag
```

Password

```
********
```

Windows verifies identity.

↓

Authentication

After successful authentication:

User attempts to access

```
Finance Folder
```

Windows checks permissions.

↓

Authorization

---

# Real-Life Analogy

Airport Example

Authentication

```
Show Passport

↓

Identity Verified
```

Authorization

```
Allowed into VIP Lounge?

YES

or

NO
```

Identity and permissions are separate decisions.

---

# Identity in Active Directory

Every security principal has an identity.

Examples include:

- Users
- Computers
- Service Accounts
- Managed Service Accounts
- Groups (for authorization purposes)

Each object has a unique identifier.

Example:

```
Administrator

↓

Security Identifier (SID)

↓

S-1-5-21-...
```

Windows uses SIDs internally rather than usernames.

---

# Authentication Components

The authentication process involves several components.

```
User

↓

Computer

↓

Domain Controller

↓

Authentication Protocol

↓

Security Token

↓

Access Granted
```

---

# Windows Authentication Protocols

Microsoft Active Directory primarily supports:

1. Kerberos
2. NTLM

```
Windows Client

↓

Kerberos (Preferred)

↓

If unavailable

↓

NTLM (Fallback)
```

---

# Why Two Protocols?

Historically:

```
Windows NT

↓

NTLM
```

Later:

```
Windows 2000

↓

Kerberos
```

Modern Active Directory environments use Kerberos by default, while NTLM remains available for compatibility with older systems and certain scenarios.

---

# Evolution of Windows Authentication

```
Windows NT

↓

NTLM

↓

Windows 2000

↓

Kerberos Introduced

↓

Windows Server 2003

↓

Kerberos Improvements

↓

Windows Server 2012+

↓

Advanced Kerberos Features

↓

Modern Windows

↓

Kerberos Preferred
```

---

# What is Kerberos?

Kerberos is a secure, ticket-based authentication protocol.

Instead of repeatedly sending passwords across the network, Kerberos uses encrypted tickets to prove a user's identity.

Advantages include:

- Mutual authentication
- Single Sign-On (SSO)
- Strong encryption
- Reduced password exposure
- Better scalability

Kerberos is the default authentication protocol in Active Directory.

---

# What is NTLM?

NTLM (NT LAN Manager) is Microsoft's older challenge-response authentication protocol.

Characteristics:

- Password hash-based authentication
- No ticketing system
- Limited delegation support
- Legacy compatibility

NTLM is still supported but should be minimized where possible.

---

# Authentication Flow Overview

High-level process:

```
User

↓

Enters Credentials

↓

Windows Client

↓

Domain Controller

↓

Authentication

↓

Security Token Created

↓

Desktop Loaded
```

---

# What is a Security Token?

After successful authentication, Windows creates an **Access Token** (also called a Security Token).

The token contains:

- User SID
- Group SIDs
- Privileges
- User Rights
- Integrity Level
- Logon Session Information

Applications use this token to determine what the user is allowed to access.

---

# Simplified Authentication Process

```
User

↓

Username

Password

↓

Computer

↓

Domain Controller

↓

Verify Credentials

↓

Create Security Token

↓

User Logged In
```

---

# Single Sign-On (SSO)

One of Kerberos' biggest advantages is **Single Sign-On**.

Without SSO:

```
Login

↓

Open Outlook

↓

Enter Password

↓

Open SharePoint

↓

Enter Password

↓

Open File Server

↓

Enter Password
```

With Kerberos:

```
Login Once

↓

Receive Ticket

↓

Reuse Ticket

↓

Access Multiple Services
```

The user authenticates once and can access multiple domain resources without repeatedly entering credentials.

---

# Domain Logon Example

User:

```
Alice
```

Computer:

```
BLR-PC-101
```

Domain:

```
corp.example.com
```

Authentication sequence:

```
Alice

↓

Windows Login

↓

Nearest Domain Controller

↓

Credentials Verified

↓

Security Token Issued

↓

Desktop Loaded

↓

Access File Server

↓

Access Printer

↓

Access Email

↓

No Additional Password Prompt
```

---

# Authentication in a Multi-Site Environment

Suppose an organization has:

- Bangalore
- Mumbai
- London

Each location has a Domain Controller.

A user in Bangalore logs in.

The workstation:

- Identifies its Site
- Locates the nearest Domain Controller
- Authenticates locally
- Receives a security token

This minimizes WAN traffic and improves logon performance.

---

# Local Account vs Domain Account

| Local Account | Domain Account |
|--------------|----------------|
| Stored on one computer | Stored in Active Directory |
| Valid only on that computer | Valid across the domain |
| Managed individually | Centrally managed |
| No domain authentication | Authenticated by a Domain Controller |

---

# Authentication Factors

Authentication can rely on:

### Something You Know

- Password
- PIN

### Something You Have

- Smart Card
- Hardware Token
- Security Key

### Something You Are

- Fingerprint
- Face Recognition
- Iris Scan

Modern enterprise environments often combine multiple factors.

---

# Enterprise Authentication Example

A multinational organization:

- 30,000 users
- 25 Domain Controllers
- 12 Sites

Workflow:

```
User

↓

Nearest Domain Controller

↓

Kerberos Authentication

↓

Security Token

↓

Access ERP

↓

Access Email

↓

Access SharePoint

↓

Access SQL Database
```

The user authenticates once while securely accessing multiple services.

---

# Cybersecurity Perspective

Authentication is the first line of defense.

Weak authentication can lead to:

- Unauthorized access
- Credential theft
- Lateral movement
- Privilege escalation
- Data breaches

Organizations should:

- Prefer Kerberos over NTLM.
- Enforce Multi-Factor Authentication (MFA) where applicable.
- Disable unnecessary legacy authentication.
- Monitor authentication logs.
- Apply strong password policies.

---

# Hands-on Lab

## Objective

Observe authentication behavior.

### Step 1

Join a Windows client to an Active Directory domain.

### Step 2

Log on using a domain account.

### Step 3

Open Command Prompt and run:

```
whoami
```

Verify the logged-in domain user.

### Step 4

Run:

```
whoami /groups
```

Review group memberships contained in the access token.

### Step 5

Run:

```
whoami /priv
```

View the privileges assigned to the current logon session.

---

# Interview Questions

### Q1: What is authentication?

**Answer:** Authentication is the process of verifying the identity of a user, computer, or service.

---

### Q2: What is authorization?

**Answer:** Authorization determines what an authenticated user is allowed to access.

---

### Q3: Which authentication protocol is preferred in Active Directory?

**Answer:** Kerberos.

---

### Q4: Why is Kerberos preferred over NTLM?

**Answer:** Kerberos provides ticket-based authentication, mutual authentication, better security, and Single Sign-On.

---

### Q5: What is a Security Token?

**Answer:** A security token contains the user's SID, group memberships, privileges, and other information used by Windows to authorize access.

---

# Best Practices

- Use Kerberos wherever possible.
- Reduce NTLM usage to legacy compatibility scenarios.
- Implement strong password policies.
- Enable account lockout policies.
- Deploy MFA for sensitive accounts.
- Audit authentication events regularly.

---

# Common Mistakes

- Confusing authentication with authorization.
- Assuming Kerberos and NTLM are interchangeable.
- Relying on local accounts instead of domain accounts in enterprise environments.
- Leaving legacy NTLM enabled unnecessarily.
- Ignoring authentication-related security logs.

---

# Key Takeaways

- Authentication verifies identity; authorization determines permissions.
- Active Directory primarily uses Kerberos, with NTLM available for compatibility.
- Successful authentication results in the creation of a security token.
- Kerberos enables secure Single Sign-On across domain resources.
- Strong authentication practices are fundamental to securing enterprise Windows environments.

---

**Next:** Part 2