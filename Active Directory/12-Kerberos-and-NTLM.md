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

# 12-Kerberos-and-NTLM.md

# Part 2 — Kerberos Architecture, Ticket Granting, KDC, AS, TGS, PAC and Authentication Flow

---

# Learning Objectives

After completing this part, you will understand:

- Kerberos architecture
- Key Distribution Center (KDC)
- Authentication Server (AS)
- Ticket Granting Server (TGS)
- Ticket Granting Ticket (TGT)
- Service Ticket (ST)
- Privilege Attribute Certificate (PAC)
- Service Principal Names (SPNs)
- Kerberos authentication flow
- Ticket lifetime
- Encryption in Kerberos
- Enterprise authentication examples

---

# Introduction

Kerberos is one of the most important technologies in Active Directory.

Almost every authentication inside a Windows domain uses Kerberos.

When a user logs in, Windows does **not** continuously send the user's password across the network.

Instead, Kerberos uses encrypted **tickets**.

These tickets prove the user's identity securely.

---

# What is Kerberos?

Kerberos is:

> A secure, ticket-based network authentication protocol designed to authenticate users and services over an insecure network without transmitting passwords in plaintext.

Kerberos provides:

- Secure authentication
- Mutual authentication
- Single Sign-On (SSO)
- Delegation support
- Strong encryption
- Replay attack protection

---

# Why Ticket-Based Authentication?

Imagine logging into ten different servers.

Without Kerberos:

```
Login

↓

Password

↓

Server 1

↓

Password

↓

Server 2

↓

Password

↓

Server 3

...
```

The password would be transmitted or processed repeatedly.

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

The password is used only during the initial authentication process.

---

# Kerberos Components

Kerberos consists of several major components.

```
User

↓

Client Computer

↓

Key Distribution Center (KDC)

↓

Authentication Server (AS)

↓

Ticket Granting Server (TGS)

↓

Application Server
```

---

# Key Distribution Center (KDC)

The **Key Distribution Center (KDC)** is the heart of Kerberos.

In Active Directory:

> Every Domain Controller acts as a KDC.

The KDC has two logical services:

- Authentication Server (AS)
- Ticket Granting Server (TGS)

---

# KDC Responsibilities

The KDC:

- Authenticates users
- Issues Ticket Granting Tickets
- Issues Service Tickets
- Validates credentials
- Maintains secure authentication

Without the KDC, Kerberos authentication cannot occur.

---

# Authentication Server (AS)

The Authentication Server performs the initial authentication.

Responsibilities:

- Verify user credentials
- Authenticate the user
- Issue a Ticket Granting Ticket (TGT)

Think of the AS as the "identity verifier."

---

# Ticket Granting Server (TGS)

After the user has a TGT, they no longer need to authenticate with their password for every service.

Instead, they contact the Ticket Granting Server.

Responsibilities:

- Validate the TGT
- Issue Service Tickets
- Support Single Sign-On

Think of the TGS as the "ticket issuer."

---

# Kerberos Ticket Types

Kerberos primarily uses two ticket types.

```
Authentication

↓

Ticket Granting Ticket (TGT)

↓

Request Service

↓

Service Ticket

↓

Access Resource
```

---

# Ticket Granting Ticket (TGT)

The **Ticket Granting Ticket** is issued immediately after successful authentication.

Purpose:

- Proves the user's identity
- Allows requests for additional Service Tickets
- Enables Single Sign-On

The TGT is **not** presented directly to application servers.

It is presented only to the TGS.

---

# Service Ticket

When the user wants to access a service such as:

- File Server
- SQL Server
- SharePoint
- IIS
- Print Server

the client requests a **Service Ticket**.

The Service Ticket is presented to the destination service to prove the user's identity.

---

# Privilege Attribute Certificate (PAC)

A Service Ticket contains a structure called the **Privilege Attribute Certificate (PAC).**

The PAC includes:

- User SID
- Group Memberships
- User Privileges
- Logon Information
- Authorization Data

Windows uses the PAC to determine what the authenticated user is authorized to do.

---

# Service Principal Name (SPN)

Every Kerberos-enabled service is identified by a **Service Principal Name (SPN).**

Examples:

```
HTTP/webserver

HOST/server01

MSSQLSvc/sql01

CIFS/fileserver
```

SPNs uniquely identify services within Active Directory.

---

# Kerberos Authentication Flow

The complete authentication process occurs in three phases:

```
1.

Authentication

↓

Receive TGT

↓

2.

Request Service Ticket

↓

Receive Service Ticket

↓

3.

Access Service
```

Let's examine each phase.

---

# Phase 1 — Initial Authentication

```
User

↓

Enters Username

Password

↓

Client

↓

Authentication Server (AS)

↓

Credentials Verified

↓

TGT Issued
```

The client now possesses a Ticket Granting Ticket.

---

# Phase 2 — Request Service Ticket

Suppose the user wants to access:

```
\\FILESERVER
```

The client sends:

```
TGT

↓

Ticket Granting Server

↓

Request

↓

Service Ticket
```

The TGS verifies the TGT and issues a Service Ticket.

---

# Phase 3 — Access Resource

```
Client

↓

Service Ticket

↓

File Server

↓

Ticket Verified

↓

Access Granted
```

The user gains access without entering the password again.

---

# Complete Kerberos Flow

```
          User

            │

      Enter Password

            │

            ▼

        Authentication
         Server (AS)

            │

     Issue TGT

            ▼

        Client Stores TGT

            │

            ▼

   Requests Service Ticket

            │

            ▼

 Ticket Granting Server (TGS)

            │

 Issue Service Ticket

            ▼

        Application Server

            │

      Validate Ticket

            ▼

       Access Granted
```

---

# Ticket Lifetime

Kerberos tickets are temporary.

Typical enterprise configuration:

| Ticket | Purpose |
|---------|----------|
| TGT | Valid for several hours (commonly 10 hours by default) |
| Service Ticket | Valid for a limited period based on domain policy |

After expiration:

- Tickets may be renewed (if permitted).
- Users may need to obtain new tickets.

Ticket lifetime is configurable through Group Policy.

---

# Ticket Cache

Windows stores Kerberos tickets in memory.

```
User Login

↓

Receive TGT

↓

Stored in Cache

↓

Reuse Ticket

↓

Single Sign-On
```

This avoids repeated authentication requests.

---

# Viewing Kerberos Tickets

Administrators can inspect cached tickets using:

```
klist
```

Example output includes:

- TGT
- Service Tickets
- Expiration Time
- Encryption Type
- Client Principal
- Server Principal

---

# Mutual Authentication

Unlike many legacy authentication methods,

Kerberos provides **Mutual Authentication**.

This means:

```
Client verifies Server

AND

Server verifies Client
```

Both parties authenticate each other.

This reduces the risk of impersonation attacks.

---

# Encryption in Kerberos

Kerberos supports modern encryption algorithms.

Commonly used algorithms include:

- AES-128
- AES-256

Older environments may still support legacy algorithms for compatibility, but modern deployments should prioritize strong encryption.

---

# Enterprise Authentication Example

Company:

```
Contoso
```

User:

```
Alice
```

Resource:

```
SQL Server
```

Workflow:

```
Alice

↓

Login

↓

Domain Controller (KDC)

↓

Receive TGT

↓

Request SQL Service Ticket

↓

Receive Ticket

↓

SQL Server

↓

Access Database
```

Alice authenticates once while securely accessing multiple enterprise resources.

---

# Cybersecurity Perspective

Kerberos provides several important security benefits:

- Passwords are not repeatedly transmitted.
- Mutual authentication helps prevent impersonation.
- Ticket expiration limits long-term misuse.
- Strong encryption protects authentication data.
- Single Sign-On reduces password prompts, improving usability while maintaining security.

To strengthen Kerberos security:

- Prefer AES encryption.
- Keep Domain Controllers synchronized with accurate time.
- Monitor authentication logs.
- Review SPN registrations.
- Regularly audit service accounts.

---

# Hands-on Lab

## Objective

Inspect Kerberos tickets.

### Step 1

Log into a domain-joined Windows computer.

### Step 2

Open Command Prompt.

### Step 3

Run:

```
klist
```

Observe:

- Ticket Granting Ticket
- Service Tickets
- Expiration Time
- Encryption Type

### Step 4

Access a network file share.

### Step 5

Run:

```
klist
```

again.

Notice that a new Service Ticket has been added for the accessed service.

---

# Interview Questions

### Q1: What is the Key Distribution Center (KDC)?

**Answer:** The KDC is the Kerberos service running on Domain Controllers that authenticates users and issues Kerberos tickets.

---

### Q2: What is a Ticket Granting Ticket (TGT)?

**Answer:** A TGT is issued after successful authentication and allows a user to request Service Tickets without repeatedly entering credentials.

---

### Q3: What is a Service Ticket?

**Answer:** A Service Ticket allows an authenticated client to access a specific network service, such as a file server or SQL Server.

---

### Q4: What is the role of the Ticket Granting Server (TGS)?

**Answer:** The TGS validates the user's TGT and issues Service Tickets for requested services.

---

### Q5: What information is stored in the Privilege Attribute Certificate (PAC)?

**Answer:** The PAC contains authorization-related information such as the user's SID, group memberships, privileges, and logon details.

---

### Q6: What command displays Kerberos tickets?

**Answer:**

```
klist
```

---

# Best Practices

- Use Kerberos as the default authentication protocol.
- Prefer AES-based encryption.
- Maintain accurate time synchronization across Domain Controllers and clients.
- Regularly review Service Principal Names (SPNs).
- Monitor Kerberos authentication events.
- Keep service account permissions to the minimum required.

---

# Common Mistakes

- Confusing the KDC with the Domain Controller (the KDC is a service hosted on a Domain Controller).
- Assuming the TGT is sent directly to application servers.
- Misconfiguring SPNs, causing authentication failures.
- Ignoring time synchronization issues.
- Relying on deprecated encryption algorithms.

---

# Key Takeaways

- Kerberos is a secure, ticket-based authentication protocol used by Active Directory.
- Every Domain Controller hosts a Key Distribution Center (KDC).
- The Authentication Server (AS) issues Ticket Granting Tickets (TGTs).
- The Ticket Granting Server (TGS) issues Service Tickets.
- The Privilege Attribute Certificate (PAC) carries authorization information.
- Kerberos enables secure Single Sign-On while minimizing password exposure.

---

**Next:** Part 3