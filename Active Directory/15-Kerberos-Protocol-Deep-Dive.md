# Active-Directory/

# 15-Kerberos-Protocol-Deep-Dive.md

# Part 1 — Kerberos Deep Dive, History, Components, Cryptography, Ports, Tickets, and Enterprise Architecture

---

# Learning Objectives

After completing this part, you will be able to:

- Understand why Kerberos was created.
- Learn the complete Kerberos architecture.
- Understand every Kerberos component.
- Learn how Kerberos uses cryptography.
- Understand Kerberos terminology.
- Learn enterprise authentication architecture.
- Prepare for advanced Windows Server and Active Directory interviews.

---

# Introduction

Kerberos is **the default authentication protocol** used in Microsoft Active Directory environments.

Almost every domain authentication depends on Kerberos.

Examples include:

- Windows Login
- File Servers
- SQL Server
- IIS Web Servers
- Exchange
- SharePoint
- Remote Desktop
- Domain Administration

Without Kerberos, modern Active Directory could not provide seamless Single Sign-On (SSO).

---

# Why Was Kerberos Created?

Before Kerberos, authentication relied heavily on sending passwords or reusable credentials across the network.

Problems included:

- Password exposure
- Replay attacks
- Weak authentication
- No mutual authentication
- Poor scalability

MIT developed Kerberos to solve these issues using **strong cryptography and ticket-based authentication**.

---

# Kerberos History

| Version | Description |
|----------|-------------|
| Kerberos v1-v3 | Internal MIT research versions |
| Kerberos v4 | First widely adopted implementation |
| Kerberos v5 | Current standard (RFC 4120) |
| Microsoft Kerberos | Windows implementation with Active Directory integration |

Windows Server uses Kerberos Version 5 with Microsoft-specific extensions.

---

# Why the Name "Kerberos"?

Kerberos is named after the **three-headed dog** from Greek mythology that guarded the entrance to the underworld.

The name symbolizes guarding access to protected resources.

---

# Kerberos Design Goals

Kerberos was designed to provide:

- Strong authentication
- Mutual authentication
- Single Sign-On
- Password protection
- Scalability
- Secure communication
- Replay attack resistance

---

# Kerberos in Active Directory

Every Domain Controller runs a:

```text
Key Distribution Center (KDC)
```

The KDC integrates with Active Directory Domain Services (AD DS) to authenticate users and issue tickets.

---

# High-Level Architecture

```text
           User
             │
             ▼
      Domain Computer
             │
             ▼
     Domain Controller
       (KDC + AD DS)
             │
             ▼
     Kerberos Tickets
             │
             ▼
      Application Server
```

---

# Kerberos Components

The major components are:

```text
Kerberos

│

├── Client

├── Key Distribution Center (KDC)

├── Authentication Service (AS)

├── Ticket Granting Service (TGS)

├── Ticket Granting Ticket (TGT)

├── Service Ticket

└── Service Principal
```

---

# Client

The client is usually:

- User workstation
- Laptop
- Server
- Service

The client requests authentication from the KDC.

---

# Domain Controller

The Domain Controller performs two major functions:

- Stores Active Directory
- Hosts the Kerberos KDC

Every writable Domain Controller can authenticate users.

---

# Key Distribution Center (KDC)

The KDC is the heart of Kerberos.

Responsibilities include:

- Verify identities
- Issue TGTs
- Issue Service Tickets
- Validate requests
- Apply Kerberos policies

---

# Authentication Service (AS)

The Authentication Service handles the **first authentication**.

Responsibilities:

- Validate credentials
- Issue the Ticket Granting Ticket (TGT)

---

# Ticket Granting Service (TGS)

The Ticket Granting Service issues tickets for services after validating a TGT.

Examples:

```text
File Server

↓

Service Ticket
```

```text
SQL Server

↓

Different Service Ticket
```

---

# Ticket Granting Ticket (TGT)

The TGT proves that the user has already authenticated successfully.

Characteristics:

- Issued once after initial logon
- Used to request service tickets
- Not presented directly to application servers
- Has a limited lifetime

---

# Service Ticket

A Service Ticket is issued for a **specific service**.

Examples:

- CIFS/File Server
- HTTP/Web Server
- LDAP
- MSSQL
- RDP

Each service receives its own ticket.

---

# Service Principal

Every Kerberos-enabled service has an identity called a **Service Principal Name (SPN)**.

Examples:

```text
HTTP/web01.contoso.com
```

```text
HOST/server01.contoso.com
```

```text
MSSQLSvc/sql01.contoso.com
```

SPNs allow the KDC to identify the target service.

---

# Kerberos Database

Active Directory stores information required for Kerberos.

Examples include:

- User accounts
- Computer accounts
- Service accounts
- Password-derived secrets
- SPNs

The KDC retrieves this information during authentication.

---

# Authentication Flow Overview

```text
User

↓

Authentication Service

↓

TGT

↓

Ticket Granting Service

↓

Service Ticket

↓

Application
```

---

# Cryptography in Kerberos

Kerberos relies on cryptography rather than repeatedly sending passwords.

Core concepts include:

- Shared secrets
- Session keys
- Ticket encryption
- Integrity protection

The goal is to authenticate securely while minimizing password exposure.

---

# Session Keys

A **session key** is generated for secure communication between parties during an authenticated session.

Benefits:

- Temporary
- Short-lived
- Limits exposure if compromised
- Supports secure communication

---

# Ticket Encryption

Kerberos tickets are encrypted so they cannot be easily modified or read by unauthorized parties.

This protects:

- Authentication data
- Session information
- Authorization-related information

---

# Time-Based Authentication

Kerberos depends on accurate system time.

```text
Client

↓

Timestamp

↓

Domain Controller

↓

Validation
```

If clocks differ significantly, authentication may fail.

This helps reduce replay attacks.

---

# Kerberos Ports

Common ports:

| Protocol | Port |
|----------|------|
| Kerberos | TCP/UDP 88 |
| LDAP | TCP/UDP 389 |
| LDAPS | TCP 636 |
| DNS | TCP/UDP 53 |
| SMB | TCP 445 |

These services often work together during authentication and resource access.

---

# Kerberos Terminology

| Term | Meaning |
|------|----------|
| KDC | Key Distribution Center |
| AS | Authentication Service |
| TGS | Ticket Granting Service |
| TGT | Ticket Granting Ticket |
| SPN | Service Principal Name |
| PAC | Privilege Attribute Certificate |
| Realm | Administrative Kerberos boundary (typically maps to an AD domain) |
| Principal | A Kerberos identity (user, computer, or service) |

---

# Enterprise Authentication Example

Company:

- 250,000 users
- 45 Domain Controllers
- 6 domains

Authentication flow:

```text
User

↓

Nearest Domain Controller

↓

TGT

↓

Service Ticket

↓

File Server

↓

SQL Server

↓

Web Application
```

This enables efficient and scalable authentication across the enterprise.

---

# Benefits of Kerberos

- Single Sign-On
- Strong authentication
- Mutual authentication
- Reduced password exposure
- Scalability
- Enterprise integration
- Efficient authorization workflow

---

# Common Misconceptions

## Myth 1

> Kerberos stores passwords inside tickets.

**Reality:**

Tickets contain authentication and authorization data, not user passwords.

---

## Myth 2

> One ticket works for every service forever.

**Reality:**

Different services require their own Service Tickets, and tickets have limited lifetimes.

---

## Myth 3

> Kerberos only authenticates users.

**Reality:**

Users, computers, and services can all authenticate using Kerberos.

---

# Cybersecurity Perspective

Kerberos is central to enterprise identity, making it a high-value target.

Security teams should:

- Protect Domain Controllers.
- Monitor Kerberos-related events.
- Audit privileged accounts.
- Detect unusual ticket activity.
- Maintain healthy DNS and time synchronization.
- Secure service accounts.

---

# Hands-on Lab

## Objective

Identify Kerberos infrastructure components.

### Tasks

1. Identify a Domain Controller in your environment.

2. Verify:

- Kerberos service availability
- DNS configuration
- Domain membership

3. Run:

```powershell
klist
```

Observe:

- TGT
- Service Tickets

4. Document:

- Domain name
- Domain Controller
- Kerberos port
- Authentication protocol in use

---

# Key Takeaways

- Kerberos is the default authentication protocol in Active Directory.
- The KDC runs on every writable Domain Controller.
- The Authentication Service issues TGTs.
- The Ticket Granting Service issues Service Tickets.
- SPNs identify Kerberos-enabled services.
- Kerberos relies on cryptography and accurate time synchronization.

---

# Interview Questions

1. Why was Kerberos developed?
2. What are the goals of Kerberos?
3. What is the role of the KDC?
4. What is the difference between the AS and the TGS?
5. What is a TGT?
6. What is a Service Ticket?
7. What is an SPN?
8. Why is time synchronization important?
9. Which network port does Kerberos commonly use?
10. What is the difference between a principal and a service?

---

# References

- RFC 4120 – The Kerberos Network Authentication Service (V5)
- Microsoft Learn – Kerberos Authentication Overview
- Microsoft Learn – Active Directory Kerberos
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# Active-Directory/

# 15-Kerberos-Protocol-Deep-Dive.md

# Part 2 — Complete Kerberos Message Flow (AS-REQ, AS-REP, TGS-REQ, TGS-REP, AP-REQ, AP-REP), Ticket Structure, PAC, Encryption Types, and Enterprise Authentication Sequence

---

# Learning Objectives

After completing this part, you will be able to:

- Understand every Kerberos message.
- Learn the complete Kerberos authentication sequence.
- Understand the structure of Kerberos tickets.
- Learn how encryption is used throughout the protocol.
- Understand where the PAC fits into authentication.
- Follow enterprise authentication step-by-step.

---

# Kerberos Communication Overview

Kerberos is a **message-based authentication protocol**.

Instead of simply sending a username and password, the client and the Key Distribution Center (KDC) exchange a series of structured protocol messages.

The primary message sequence is:

```text
AS-REQ

↓

AS-REP

↓

TGS-REQ

↓

TGS-REP

↓

AP-REQ

↓

AP-REP
```

---

# Authentication Phases

Kerberos authentication can be divided into three phases.

```text
Phase 1

Initial Authentication

↓

Phase 2

Service Ticket Request

↓

Phase 3

Service Authentication
```

---

# Phase 1

```text
Client

↓

Authentication Service

↓

Ticket Granting Ticket
```

Purpose:

Authenticate the identity of the client.

---

# Phase 2

```text
Client

↓

Ticket Granting Service

↓

Service Ticket
```

Purpose:

Request access to a particular service.

---

# Phase 3

```text
Client

↓

Application Server

↓

Authenticated Session
```

Purpose:

Access the requested resource.

---

# Complete Enterprise Flow

```text
User

↓

Logon

↓

AS-REQ

↓

AS-REP

↓

TGT

↓

TGS-REQ

↓

TGS-REP

↓

Service Ticket

↓

AP-REQ

↓

AP-REP

↓

Application Access
```

---

# Step 1 — User Enters Credentials

Example:

```text
Username

↓

alice@contoso.com

↓

Password
```

Windows prepares the information required for Kerberos authentication.

---

# Step 2 — Locate Domain Controller

Before authentication begins:

```text
Client

↓

DNS

↓

Locate KDC
```

Without DNS:

```text
No KDC

↓

Authentication Fails
```

---

# Step 3 — AS-REQ

Meaning:

```text
Authentication Service Request
```

The client sends an authentication request to the Authentication Service on the KDC.

High-level contents include:

- Client identity
- Target realm
- Requested options
- Current timestamp-related information
- Supported encryption types

---

# AS-REQ Diagram

```text
Client

──────────►

Authentication Service

AS-REQ
```

---

# Authentication Service Processing

The Authentication Service:

- Locates the account.
- Verifies policy requirements.
- Validates the authentication request.
- Determines whether a TGT can be issued.

---

# Step 4 — AS-REP

Meaning:

```text
Authentication Service Reply
```

If authentication succeeds:

```text
Authentication Service

↓

Ticket Granting Ticket

↓

Session Key

↓

Client
```

---

# AS-REP Diagram

```text
Authentication Service

──────────►

Client

AS-REP
```

---

# Result of AS-REP

The client now possesses:

```text
TGT

+

Client/TGS Session Key
```

These will be used to obtain service tickets.

---

# Ticket Granting Ticket

The TGT represents successful authentication.

Conceptually:

```text
User Authenticated

↓

TGT

↓

Future Service Requests
```

The TGT is presented to the Ticket Granting Service—not directly to application servers.

---

# Step 5 — User Requests a Resource

Example:

```text
\\fileserver\Finance
```

or

```text
https://portal.contoso.com
```

The client recognizes that a service ticket is required.

---

# Step 6 — TGS-REQ

Meaning:

```text
Ticket Granting Service Request
```

The client sends:

- TGT
- Authenticator
- Requested Service (SPN)

to the Ticket Granting Service.

---

# TGS-REQ Diagram

```text
Client

──────────►

Ticket Granting Service

TGS-REQ
```

---

# Ticket Granting Service Validation

The TGS:

- Validates the TGT.
- Verifies the authenticator.
- Confirms policy.
- Locates the requested SPN.
- Creates a Service Ticket.

---

# Step 7 — TGS-REP

Meaning:

```text
Ticket Granting Service Reply
```

The reply includes:

```text
Service Ticket

+

Client/Service Session Key
```

---

# TGS-REP Diagram

```text
Ticket Granting Service

──────────►

Client

TGS-REP
```

---

# Client State After TGS-REP

The client now has:

```text
TGT

+

Service Ticket

+

Session Keys
```

The Service Ticket is used to authenticate to the target service.

---

# Step 8 — AP-REQ

Meaning:

```text
Application Request
```

The client sends:

- Service Ticket
- Authenticator

to the application server.

---

# AP-REQ Diagram

```text
Client

──────────►

Application Server

AP-REQ
```

---

# Application Server Processing

The server:

- Validates the Service Ticket.
- Verifies the authenticator.
- Confirms the ticket is valid.
- Extracts authorization information (including the PAC where applicable).
- Establishes an authenticated session.

---

# Step 9 — AP-REP

Meaning:

```text
Application Reply
```

When mutual authentication is required:

```text
Application Server

──────────►

Client

AP-REP
```

This confirms the server's identity to the client.

---

# Complete Message Sequence

```text
Client

│

├── AS-REQ ─────────► KDC

│

├── AS-REP ◄──────── KDC

│

├── TGS-REQ ───────► KDC

│

├── TGS-REP ◄─────── KDC

│

├── AP-REQ ─────────► Server

│

└── AP-REP ◄──────── Server
```

---

# Kerberos Ticket Structure

Conceptually, a Kerberos ticket contains information such as:

- Client identity
- Service identity
- Validity period
- Session key information
- Authorization data (such as the PAC in Active Directory)
- Encryption metadata

The exact structure is defined by the Kerberos protocol specification.

---

# PAC Location

```text
Kerberos Ticket

│

├── Ticket Information

└── PAC

     ├── User SID

     ├── Group Membership

     ├── User Rights

     └── Authorization Data
```

The PAC enables servers to make authorization decisions efficiently.

---

# Ticket Lifetime

Kerberos tickets are intentionally temporary.

Typical concepts include:

- Start time
- Expiration time
- Renewal period (where allowed)

Short-lived tickets reduce the impact of credential theft.

---

# Renewable Tickets

Some tickets can be renewed without requiring the user to enter credentials again, subject to policy.

Example:

```text
Original TGT

↓

Renewal Request

↓

Renewed TGT
```

Renewal policies are managed by administrators.

---

# Encryption in Kerberos

Kerberos uses encryption to protect:

- Authentication exchanges
- Session keys
- Tickets
- Integrity of protocol messages

The exact encryption algorithms depend on the operating system configuration and domain policy.

---

# Encryption Types

Modern Active Directory environments commonly use AES-based encryption types.

Legacy environments may still contain older encryption types for compatibility.

Administrators should:

- Prefer modern encryption.
- Review legacy compatibility settings.
- Disable obsolete algorithms where organizational requirements permit.

---

# Session Keys

Kerberos uses different session keys for different communication stages.

Conceptually:

```text
Client

⇄

KDC

(Session Key)

⇄

Application Server

(New Session Key)
```

Using separate session keys limits the scope of exposure.

---

# Replay Protection

Kerberos includes mechanisms designed to reduce replay attacks.

Examples include:

- Time validation
- Authenticators
- Short ticket lifetimes

These protections depend on accurate time synchronization.

---

# Mutual Authentication

Unlike many older authentication protocols:

```text
Client

Verifies

Server
```

and

```text
Server

Verifies

Client
```

This reduces the risk of impersonation.

---

# Enterprise Authentication Example

Global company:

- 400,000 users
- 85 Domain Controllers
- 9 domains

Authentication:

```text
Morning Login

↓

AS-REQ

↓

AS-REP

↓

TGT

↓

TGS-REQ

↓

TGS-REP

↓

File Server

↓

AP-REQ

↓

Authenticated Session
```

The same TGT can later be used to request additional service tickets for other enterprise services.

---

# Common Authentication Failures

Examples include:

- DNS resolution problems
- Incorrect system time
- Invalid SPNs
- Expired tickets
- Broken trust relationships
- Domain Controller unavailable

---

# Best Practices

- Prefer Kerberos over NTLM.
- Maintain accurate DNS.
- Synchronize system time.
- Protect Domain Controllers.
- Use modern encryption types.
- Monitor ticket issuance.
- Review service account configuration.

---

# Cybersecurity Perspective

Security teams should monitor for:

- Unusual numbers of TGT requests.
- Unexpected service ticket activity.
- Authentication failures.
- Abnormal ticket lifetimes.
- Privileged account authentication.
- Kerberos protocol anomalies.

These events can indicate misconfiguration or malicious activity.

---

# Hands-on Lab

## Objective

Observe Kerberos ticket acquisition.

### Tasks

1. Sign in to a domain-joined workstation.

2. Run:

```powershell
klist
```

3. Identify:

- Ticket Granting Ticket
- Service Tickets

4. Access:

- File Server
- Internal Website

5. Run:

```powershell
klist
```

again and observe additional service tickets.

6. Document:

- Ticket types
- Services accessed
- Authentication flow

---

# Key Takeaways

- Kerberos authentication consists of three major phases.
- AS-REQ/AS-REP establish the initial authenticated state.
- TGS-REQ/TGS-REP obtain service-specific tickets.
- AP-REQ/AP-REP authenticate the client to the application server.
- The PAC provides authorization information.
- Kerberos uses encryption, timestamps, and session keys to provide secure authentication.

---

# Interview Questions

1. What is AS-REQ?
2. What information is returned in AS-REP?
3. What is the purpose of TGS-REQ?
4. What does TGS-REP contain?
5. What is AP-REQ used for?
6. Why is AP-REP important?
7. What is stored in a Kerberos ticket?
8. Why are Service Tickets separate from the TGT?
9. Why are tickets time-limited?
10. How does Kerberos provide replay protection?

---

# References

- RFC 4120 – The Kerberos Network Authentication Service (V5)
- Microsoft Learn – Kerberos Authentication
- Microsoft Learn – Kerberos Protocol Extensions
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 3 — Kerberos Internals, Ticket Lifecycle, Delegation, Constrained Delegation, Cross-Realm Authentication, PowerShell, Troubleshooting, and Enterprise Operations**