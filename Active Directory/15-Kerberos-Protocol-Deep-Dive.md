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

**Next:** **Part 2 — Complete Kerberos Message Flow (AS-REQ, AS-REP, TGS-REQ, TGS-REP, AP-REQ, AP-REP), Ticket Structure, PAC, Encryption Types, and Enterprise Authentication Sequence**