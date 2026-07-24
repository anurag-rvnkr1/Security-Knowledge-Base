# Active-Directory/

# 14-Active-Directory-Authentication.md

# Part 1 — Introduction to Active Directory Authentication, Identity Verification, Kerberos Fundamentals, NTLM Overview, and Enterprise Authentication Architecture

---

# Learning Objectives

After completing this part, you will be able to:

- Understand authentication in Active Directory.
- Differentiate authentication from authorization.
- Learn how users authenticate to a Windows domain.
- Understand Kerberos and NTLM at a high level.
- Learn the components involved in authentication.
- Understand enterprise authentication architecture.

---

# Introduction

Imagine a multinational company with:

- 300,000 employees
- 200,000 computers
- 8,000 servers
- Thousands of business applications
- Multiple Active Directory domains

Every day, millions of authentication requests occur before users can access:

- Email
- VPN
- File Servers
- Databases
- HR Systems
- ERP Applications
- Cloud Services

Authentication is the first security checkpoint.

---

# What is Authentication?

**Authentication** is the process of verifying the identity of a user, computer, or service.

Authentication answers the question:

> **"Who are you?"**

Example:

```text
Username

↓

john.smith

↓

Password

↓

Verified

↓

Identity Confirmed
```

Only after successful authentication can access decisions be made.

---

# Authentication vs Authorization

These concepts are often confused.

Authentication:

```text
Identity Verification
```

Authorization:

```text
Permission Evaluation
```

Authentication happens **before** authorization.

---

# Example

```text
John

↓

Logs In

↓

Authentication Successful

↓

Attempts to Open Finance Folder

↓

Authorization Checks Permissions

↓

Access Granted
```

Authentication proves identity.

Authorization determines access.

---

# Real-World Analogy

Airport example:

Authentication:

```text
Passport Check
```

Authorization:

```text
Boarding Pass

↓

Allowed Flight
```

Showing a valid passport does not automatically authorize boarding every flight.

---

# Authentication Components

Active Directory authentication involves several components.

```text
User

↓

Computer

↓

Domain Controller

↓

Active Directory

↓

Authentication Protocol
```

---

# Authentication Architecture

```text
User

↓

Domain-Joined Computer

↓

Domain Controller

↓

Kerberos / NTLM

↓

Identity Verified
```

---

# Domain Controller's Role

A Domain Controller:

- Stores Active Directory
- Verifies credentials
- Issues authentication data
- Enforces domain policies
- Participates in Kerberos authentication

Domain Controllers are central to domain authentication.

---

# Authentication Factors

Authentication may involve one or more factors.

### Something You Know

Examples:

- Password
- PIN

---

### Something You Have

Examples:

- Smart Card
- Hardware Token
- Security Key

---

### Something You Are

Examples:

- Fingerprint
- Facial Recognition
- Iris Recognition

---

# Multi-Factor Authentication (MFA)

MFA combines multiple authentication factors.

Example:

```text
Password

+

Authenticator App

↓

Authentication
```

Although Active Directory supports technologies that integrate with MFA, the second factor is often provided through services such as Microsoft Entra ID or third-party identity platforms.

---

# Authentication Methods

Windows environments commonly use:

```text
Kerberos

NTLM
```

Kerberos is the default authentication protocol for modern Active Directory domains.

NTLM is primarily maintained for compatibility with systems or scenarios where Kerberos cannot be used.

---

# Why Kerberos?

Kerberos provides:

- Mutual authentication
- Ticket-based authentication
- Improved security
- Reduced password exposure
- Single Sign-On (SSO)

It is designed to avoid repeatedly transmitting passwords across the network.

---

# Why NTLM Still Exists

NTLM may be used when:

- Kerberos cannot be negotiated.
- Legacy systems require it.
- Certain workgroup or compatibility scenarios exist.

Modern enterprise environments should minimize NTLM usage where practical.

---

# Authentication Workflow (High Level)

```text
User

↓

Enter Credentials

↓

Computer

↓

Domain Controller

↓

Credentials Verified

↓

Authentication Successful
```

This overview will be expanded in later parts when discussing Kerberos in detail.

---

# Identity Components

A user identity commonly includes:

- Username
- Password
- SID
- Group Membership
- UPN
- Security Attributes

These values contribute to authentication and subsequent authorization.

---

# Computer Authentication

Computers also authenticate.

Example:

```text
Computer Starts

↓

Computer Account

↓

Domain Controller

↓

Authentication Successful

↓

Secure Channel Established
```

A domain-joined computer has its own account and password in Active Directory.

---

# User Logon Process

Typical sequence:

```text
Computer Starts

↓

Computer Authenticates

↓

Ctrl + Alt + Delete (where applicable)

↓

User Enters Credentials

↓

Authentication

↓

Desktop
```

Both the computer and the user participate in the overall sign-in process.

---

# Secure Channel

A domain-joined computer maintains a secure relationship with a Domain Controller.

```text
Computer

⇄

Domain Controller
```

This trusted communication path is known as the **secure channel**.

---

# Authentication Services

Important services include:

- Active Directory Domain Services (AD DS)
- Kerberos Key Distribution Center (KDC)
- Netlogon
- DNS

These services work together to support authentication.

---

# Why DNS is Required

Active Directory depends heavily on DNS.

Example:

```text
User

↓

Needs Domain Controller

↓

DNS Query

↓

Domain Controller Located

↓

Authentication Begins
```

Without proper DNS configuration, authentication problems are common.

---

# Enterprise Example

Company:

- 120,000 employees
- 40 Domain Controllers

Workflow:

```text
User

↓

Nearest Domain Controller

↓

Kerberos

↓

Authentication

↓

Single Sign-On
```

This design improves performance and availability.

---

# Single Sign-On (SSO)

After authenticating once, users can often access multiple services without re-entering credentials.

Example:

```text
Log In Once

↓

File Server

↓

Print Server

↓

SharePoint

↓

SQL Server

↓

No Additional Password Prompts
```

Kerberos enables this behavior through ticket-based authentication.

---

# Benefits of Centralized Authentication

- One identity
- Central password management
- Consistent security policies
- Simplified auditing
- Easier account lifecycle management
- Reduced administrative effort

---

# Common Authentication Problems

Examples:

- Incorrect password
- Locked account
- Expired account
- Incorrect DNS configuration
- Time synchronization issues
- Domain Controller unavailable
- Secure channel failure

These issues are explored further in later parts.

---

# Authentication Flow Diagram

```text
User

↓

Credentials

↓

Workstation

↓

DNS

↓

Domain Controller

↓

Kerberos / NTLM

↓

Identity Verified

↓

Access Token Created

↓

Authorization Begins
```

---

# Best Practices

- Use Kerberos whenever possible.
- Maintain accurate DNS configuration.
- Keep Domain Controllers highly available.
- Synchronize system time.
- Use strong authentication policies.
- Review failed authentication attempts.
- Minimize NTLM usage.

---

# Common Misconceptions

## Myth 1

> Authentication and authorization are the same.

**Reality:**

Authentication verifies identity.

Authorization determines permissions.

---

## Myth 2

> Only users authenticate.

**Reality:**

Users, computers, and services can all authenticate.

---

## Myth 3

> Active Directory authentication only uses passwords.

**Reality:**

Modern environments can integrate passwords with smart cards, Windows Hello for Business, MFA, and other authentication technologies.

---

# Cybersecurity Perspective

Authentication is one of the primary targets of attackers.

Common attack objectives include:

- Password theft
- Credential replay
- Kerberos abuse
- NTLM abuse
- Pass-the-Hash
- Password spraying
- Brute-force attacks

Security teams should:

- Monitor authentication events.
- Detect unusual logon activity.
- Investigate repeated failures.
- Enforce strong password policies.
- Reduce legacy authentication where feasible.

---

# Hands-on Lab

## Objective

Explore Active Directory authentication components.

### Tasks

1. Verify the computer is domain joined.

2. Open:

```text
System Properties
```

3. Identify:

- Computer Name
- Domain
- Computer Account

4. Open:

```text
Event Viewer
```

Review authentication-related events.

5. Run:

```powershell
whoami
```

6. Record:

- Username
- Domain
- Computer Name

7. Verify that DNS resolves the Domain Controller.

---

# Key Takeaways

- Authentication verifies identity.
- Authorization evaluates permissions.
- Domain Controllers perform authentication services.
- Kerberos is the default protocol in Active Directory.
- DNS and the secure channel are essential for successful authentication.

---

# Interview Questions

1. What is authentication?
2. What is the difference between authentication and authorization?
3. What is the role of a Domain Controller during authentication?
4. Why is DNS important for Active Directory authentication?
5. What is a secure channel?
6. What is Single Sign-On (SSO)?
7. Which authentication protocols are commonly used in Active Directory?
8. Why is Kerberos preferred over NTLM?
9. Can computers authenticate to Active Directory?
10. What are common causes of authentication failures?

---

# References

- Microsoft Learn – Kerberos Authentication Overview
- Microsoft Learn – Active Directory Domain Services
- Microsoft Learn – Windows Authentication Architecture
- Microsoft Learn – Netlogon Service
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 2 — Kerberos Authentication, Tickets, KDC, TGT, Service Tickets, NTLM Authentication, and Authentication Flow**