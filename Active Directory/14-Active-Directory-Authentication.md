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

# Active-Directory/

# 14-Active-Directory-Authentication.md

# Part 2 — Kerberos Authentication, Tickets, KDC, TGT, Service Tickets, NTLM Authentication, and Authentication Flow

---

# Learning Objectives

After completing this part, you will be able to:

- Understand how Kerberos works.
- Learn the role of the Key Distribution Center (KDC).
- Understand Ticket Granting Tickets (TGTs).
- Learn Service Tickets (TGS).
- Understand Kerberos authentication flow.
- Compare Kerberos with NTLM.
- Understand enterprise authentication design.

---

# Review

In Part 1, we learned:

- Authentication fundamentals
- Authentication vs Authorization
- Domain Controllers
- Secure Channel
- Single Sign-On
- Kerberos overview
- NTLM overview

Now we'll study **how authentication actually works inside Active Directory.**

---

# Why Kerberos?

Before Kerberos, systems often relied on repeatedly transmitting or validating passwords through older mechanisms.

Kerberos improves security by using **tickets** instead of repeatedly sending user passwords after the initial authentication process.

Benefits include:

- Mutual authentication
- Single Sign-On (SSO)
- Ticket-based authentication
- Reduced password exposure
- Better scalability

---

# Kerberos Components

A Kerberos environment contains:

```text
Client

↓

Key Distribution Center (KDC)

↓

Application Server
```

---

# Key Distribution Center (KDC)

The **Key Distribution Center (KDC)** is a service running on every Domain Controller.

It contains two logical components:

```text
KDC

│

├── Authentication Service (AS)

└── Ticket Granting Service (TGS)
```

---

# Authentication Service (AS)

The Authentication Service:

- Verifies the user's identity.
- Issues a **Ticket Granting Ticket (TGT)** after successful authentication.

---

# Ticket Granting Service (TGS)

The Ticket Granting Service:

- Receives a valid TGT.
- Issues service tickets for requested services.

Examples:

- File Server
- SQL Server
- Print Server
- Web Server

---

# Kerberos Ticket Types

Two primary tickets exist:

```text
Ticket Granting Ticket (TGT)

↓

Used to Request

↓

Service Tickets (TGS Tickets)
```

---

# Ticket Granting Ticket (TGT)

The TGT is issued after the user's identity has been successfully verified.

Purpose:

- Proves that the user has already authenticated.
- Requests additional service tickets without requiring the user to enter credentials again.

The TGT is **not** presented directly to application servers.

---

# Service Ticket

A Service Ticket allows access to a specific service.

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

Each service receives its own ticket.

---

# High-Level Kerberos Flow

```text
User

↓

Domain Controller (KDC)

↓

TGT Issued

↓

Request Service Ticket

↓

Service Ticket Issued

↓

Access Resource
```

---

# Step 1 — User Logs On

```text
User

↓

Username

↓

Password
```

The workstation receives the credentials.

The password is **not** repeatedly transmitted to every server.

---

# Step 2 — Contact the KDC

The client contacts the Domain Controller.

```text
Client

↓

Authentication Service (AS)
```

The AS verifies the user's identity.

---

# Step 3 — TGT Issued

After successful authentication:

```text
Authentication Service

↓

Ticket Granting Ticket

↓

Client
```

The TGT is securely protected and can later be used to request additional tickets.

---

# Step 4 — User Opens a Resource

Example:

```text
Finance Share
```

The client does **not** send the password again.

Instead:

```text
Client

↓

Uses TGT

↓

Requests Service Ticket
```

---

# Step 5 — Contact Ticket Granting Service

```text
Client

↓

Ticket Granting Service

↓

Service Ticket Requested
```

The client presents its TGT to request access to a specific service.

---

# Step 6 — Service Ticket Issued

```text
Ticket Granting Service

↓

Service Ticket

↓

Client
```

The ticket is specific to the requested service.

---

# Step 7 — Access Resource

```text
Client

↓

Service Ticket

↓

File Server

↓

Access Granted
```

The server validates the service ticket before providing access.

---

# Kerberos Authentication Diagram

```text
User

↓

Login

↓

Authentication Service

↓

TGT

↓

Ticket Granting Service

↓

Service Ticket

↓

Application Server

↓

Access Granted
```

---

# Single Sign-On

Suppose a user opens:

```text
File Server
```

Later:

```text
SQL Server
```

Later:

```text
Print Server
```

The workflow becomes:

```text
Login Once

↓

TGT

↓

Service Ticket

↓

File Server

↓

Service Ticket

↓

SQL Server

↓

Service Ticket

↓

Print Server
```

The user typically does not re-enter credentials because Kerberos obtains new service tickets as needed.

---

# Mutual Authentication

Kerberos supports **mutual authentication**.

Meaning:

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

Both parties confirm each other's identity before communication continues.

---

# Ticket Lifetime

Kerberos tickets are not permanent.

Typical characteristics:

- TGTs have a limited lifetime.
- Service tickets also expire.
- Renewable tickets may be available depending on policy.

When a ticket expires, the client follows Kerberos procedures to obtain a new one if permitted.

---

# Service Principal Name (SPN)

Every Kerberos-enabled service is identified using a:

```text
Service Principal Name

(SPN)
```

Examples:

```text
HTTP/WebServer

HOST/FileServer

MSSQLSvc/SQLServer
```

The KDC uses the SPN when issuing service tickets.

---

# Why SPNs Matter

If SPNs are:

- Missing
- Incorrect
- Duplicated

Kerberos authentication may fail or use an unexpected authentication method.

Proper SPN management is essential in enterprise environments.

---

# NTLM Authentication

NTLM is an older Windows authentication protocol.

High-level workflow:

```text
Client

↓

Challenge

↓

Response

↓

Domain Controller

↓

Authentication
```

NTLM uses a challenge-response process instead of Kerberos tickets.

---

# NTLM vs Kerberos

| Kerberos | NTLM |
|-----------|------|
| Ticket-based | Challenge-response |
| Supports mutual authentication | Does not provide mutual authentication in the same way |
| Designed for Single Sign-On | Limited SSO capabilities |
| Preferred in Active Directory | Primarily compatibility-focused |
| Requires KDC | Does not use Kerberos tickets |

---

# When NTLM May Be Used

Examples:

- Legacy applications
- Workgroup authentication
- Kerberos negotiation failure
- Missing or invalid SPNs
- Certain compatibility scenarios

Modern enterprise environments should reduce NTLM usage wherever practical.

---

# Authentication Decision Flow

```text
User Requests Resource

↓

Kerberos Available?

↓

Yes

↓

Kerberos

↓

No

↓

NTLM (if supported)
```

The actual negotiation depends on the environment, configuration, and capabilities of both client and server.

---

# Enterprise Example

Organization:

- 180,000 users
- 55 Domain Controllers

Workflow:

```text
Morning Login

↓

Kerberos TGT

↓

Email

↓

Service Ticket

↓

File Server

↓

Service Ticket

↓

ERP

↓

Service Ticket

↓

Database
```

Users experience seamless Single Sign-On.

---

# Common Kerberos Problems

Examples:

- Incorrect DNS configuration
- Time synchronization issues
- Invalid SPNs
- Expired tickets
- Domain Controller unavailable
- Trust relationship problems

---

# Time Synchronization

Kerberos depends on accurate system time.

```text
Client

↓

Time

↓

Domain Controller

↓

Within Allowed Skew

↓

Authentication
```

Significant time differences may cause authentication failures.

Windows domains typically synchronize time through the Windows Time service.

---

# Best Practices

- Use Kerberos whenever possible.
- Keep DNS healthy.
- Maintain accurate time synchronization.
- Register SPNs correctly.
- Monitor authentication failures.
- Reduce NTLM dependencies.
- Keep Domain Controllers highly available.

---

# Common Misconceptions

## Myth 1

> Kerberos sends the password to every server.

**Reality:**

Kerberos primarily relies on tickets after the initial authentication process rather than repeatedly transmitting passwords.

---

## Myth 2

> One ticket grants access to every resource.

**Reality:**

The TGT requests **individual service tickets** for different services.

---

## Myth 3

> NTLM is more secure because it uses a challenge.

**Reality:**

Kerberos provides stronger security features for modern Active Directory environments, including mutual authentication and ticket-based Single Sign-On.

---

# Cybersecurity Perspective

Kerberos is frequently targeted because it is central to enterprise authentication.

Examples of attacks include:

- Kerberoasting
- AS-REP Roasting
- Golden Ticket
- Silver Ticket
- Pass-the-Ticket

These techniques will be covered in later chapters focused on Active Directory security.

Security teams should:

- Monitor Kerberos activity.
- Audit privileged accounts.
- Detect unusual ticket requests.
- Reduce NTLM usage.
- Protect Domain Controllers.

---

# Hands-on Lab

## Objective

Observe Kerberos authentication.

### Tasks

1. Sign in to a domain-joined computer.

2. Open:

```powershell
klist
```

View:

- Ticket Granting Ticket
- Service Tickets

3. Access:

- File Share
- Printer
- Internal Web Application

4. Run:

```powershell
klist
```

again and compare newly acquired service tickets.

5. Verify:

- System time
- Domain membership
- DNS configuration

---

# Key Takeaways

- Kerberos is the default authentication protocol in Active Directory.
- The KDC runs on every Domain Controller.
- The Authentication Service issues TGTs.
- The Ticket Granting Service issues Service Tickets.
- Kerberos enables Single Sign-On through ticket-based authentication.
- NTLM is primarily maintained for compatibility.

---

# Interview Questions

1. What is Kerberos?
2. What is the KDC?
3. What are the two logical components of the KDC?
4. What is a Ticket Granting Ticket (TGT)?
5. What is a Service Ticket?
6. What is the purpose of an SPN?
7. Why is time synchronization important for Kerberos?
8. How does Kerberos support Single Sign-On?
9. What is the difference between Kerberos and NTLM?
10. When might NTLM still be used?

---

# References

- Microsoft Learn – Kerberos Authentication
- Microsoft Learn – Kerberos Key Distribution Center
- Microsoft Learn – Service Principal Names (SPNs)
- Microsoft Learn – Windows Authentication
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# Active-Directory/

# 14-Active-Directory-Authentication.md

# Part 3 — Kerberos Internals, Privilege Attribute Certificate (PAC), Access Tokens, Logon Process, Trust Authentication, PowerShell, Troubleshooting, and Enterprise Operations

---

# Learning Objectives

After completing this part, you will be able to:

- Understand Kerberos authentication internals.
- Learn the complete Windows logon process.
- Understand the Privilege Attribute Certificate (PAC).
- Learn how Windows creates access tokens.
- Understand cross-domain authentication using trusts.
- Troubleshoot authentication issues.
- Perform authentication-related administration using PowerShell.

---

# Review

In Part 2, we learned:

- Kerberos
- Key Distribution Center (KDC)
- Authentication Service (AS)
- Ticket Granting Service (TGS)
- Ticket Granting Ticket (TGT)
- Service Tickets
- Service Principal Names (SPNs)
- NTLM comparison

Now we'll dive deeper into how Windows processes authentication internally.

---

# Complete Windows Logon Process

The simplified Windows domain logon process is:

```text
Computer Starts

↓

Computer Authenticates

↓

User Enters Credentials

↓

Credential Verification

↓

TGT Issued

↓

Access Token Created

↓

Desktop Loaded
```

Several Windows components participate in this process.

---

# Windows Authentication Components

Common components include:

| Component | Purpose |
|-----------|----------|
| Winlogon | Manages interactive sign-in |
| LSASS | Local Security Authority Subsystem Service |
| Netlogon | Secure communication with the Domain Controller |
| KDC | Kerberos authentication service |
| Active Directory | Identity store |
| DNS | Domain Controller location |

---

# Winlogon

**Winlogon** manages the interactive sign-in experience.

Responsibilities include:

- Secure attention sequence (Ctrl + Alt + Del where applicable)
- User sign-in
- User logoff
- Session management

Winlogon passes credentials to the appropriate authentication components.

---

# LSASS

The **Local Security Authority Subsystem Service (LSASS)** is one of the most important Windows security processes.

Responsibilities include:

- Authentication
- Creating logon sessions
- Creating access tokens
- Managing local security policy
- Processing Kerberos and NTLM authentication

Process name:

```text
lsass.exe
```

---

# Netlogon Service

Netlogon helps establish and maintain the secure channel between a domain-joined computer and a Domain Controller.

Responsibilities:

- Domain logon support
- Secure channel maintenance
- Domain Controller discovery
- Authentication assistance

---

# DNS During Authentication

Authentication begins with locating a Domain Controller.

```text
Client

↓

DNS Query

↓

Domain Controller Located

↓

Kerberos Begins
```

Incorrect DNS configuration is one of the most common causes of authentication failures.

---

# Kerberos Authentication Flow (Detailed)

```text
User

↓

Winlogon

↓

LSASS

↓

KDC

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

# Privilege Attribute Certificate (PAC)

The **Privilege Attribute Certificate (PAC)** is additional authorization data included in Kerberos tickets within Active Directory environments.

The PAC commonly contains:

- User SID
- Group SIDs
- User privileges
- Logon information

The PAC enables services to make authorization decisions without independently querying Active Directory for every request.

---

# PAC Overview

```text
Kerberos Ticket

│

├── Authentication Data

└── PAC

     ├── User SID

     ├── Group Membership

     ├── Privileges

     └── Logon Information
```

---

# Why the PAC Matters

Suppose:

```text
John

↓

Finance Group

↓

VPN Group

↓

Remote Desktop Users
```

The PAC contains information about these memberships, allowing servers to evaluate access efficiently.

---

# Access Token Creation

After successful authentication:

```text
Authentication Successful

↓

LSASS

↓

Access Token Created
```

The access token represents the user's security context for the session.

---

# Access Token Contents

An access token commonly includes:

- User SID
- Group SIDs
- Privileges
- User rights
- Logon session information
- Integrity level (where applicable)

Applications consult the access token during authorization.

---

# Access Token Flow

```text
Authentication

↓

PAC

↓

LSASS

↓

Access Token

↓

Application Access
```

---

# Access Decision

When accessing a resource:

```text
User

↓

Access Token

↓

ACL

↓

Allow / Deny
```

The operating system compares the SIDs in the access token against the Access Control List (ACL).

---

# Logon Session

Each successful authentication creates a logon session.

Example:

```text
User Login

↓

Logon Session

↓

Desktop

↓

Applications
```

The logon session persists until the user signs out or the session ends.

---

# Credential Caching

Windows can cache domain credentials locally to support certain scenarios where a Domain Controller is temporarily unavailable.

Example:

```text
Laptop

↓

Offline

↓

Cached Credentials

↓

User Signs In
```

Policies control the number of cached logons and should align with organizational security requirements.

---

# Computer Authentication

Computers authenticate using their own accounts.

```text
Computer Account

↓

Kerberos

↓

Secure Channel

↓

Authentication
```

This occurs independently of user authentication.

---

# Cross-Domain Authentication

Suppose:

```text
User

↓

Domain A
```

needs access to:

```text
Server

↓

Domain B
```

If an appropriate trust exists, Kerberos can authenticate the user across domains.

---

# Trust Authentication

Example:

```text
Domain A

⇄ Trust ⇄

Domain B
```

Workflow:

```text
User

↓

Home Domain

↓

Trust

↓

Resource Domain

↓

Service Ticket

↓

Access
```

The user's home domain authenticates the identity, while the resource domain authorizes access based on the relevant permissions.

---

# Cross-Forest Authentication

Example:

```text
Forest A

⇄ Trust ⇄

Forest B
```

Trusts allow authentication across forests when properly configured and authorized.

---

# Enterprise Authentication Example

Company:

- 12 domains
- 3 forests

Workflow:

```text
User

↓

Home Domain

↓

Kerberos

↓

Trust

↓

Resource Forest

↓

Application
```

This design enables centralized identity with distributed resources.

---

# PowerShell

Useful authentication-related commands include:

---

# Current User

```powershell
whoami
```

---

# Current Groups

```powershell
whoami /groups
```

---

# Current Privileges

```powershell
whoami /priv
```

---

# View Kerberos Tickets

```powershell
klist
```

---

# Purge Kerberos Tickets

```powershell
klist purge
```

This removes cached Kerberos tickets for the current logon session. New tickets are obtained when required.

---

# Check Computer Secure Channel

```powershell
Test-ComputerSecureChannel
```

This command helps verify the relationship between the workstation and the domain.

---

# Authentication Troubleshooting

Common issues:

- Incorrect password
- Locked account
- Expired password
- DNS issues
- Time synchronization problems
- Secure channel failures
- Missing or duplicate SPNs
- Trust issues

---

# Troubleshooting Workflow

```text
Authentication Failed

↓

DNS Working?

↓

Time Correct?

↓

Domain Reachable?

↓

Secure Channel Healthy?

↓

Kerberos Tickets Valid?

↓

Resolved
```

---

# Useful Diagnostic Tools

| Tool | Purpose |
|------|----------|
| Event Viewer | Authentication events |
| klist | Kerberos tickets |
| whoami | Identity information |
| Test-ComputerSecureChannel | Secure channel validation |
| nltest | Domain and trust diagnostics |
| dcdiag | Domain Controller diagnostics |

---

# Enterprise Best Practices

- Use Kerberos as the primary authentication protocol.
- Maintain accurate DNS configuration.
- Synchronize system clocks.
- Monitor Domain Controller health.
- Audit authentication failures.
- Protect privileged accounts.
- Limit NTLM where feasible.
- Monitor trust relationships.

---

# Common Administrative Mistakes

Avoid:

- Configuring clients to use incorrect DNS servers.
- Ignoring system time synchronization.
- Registering duplicate SPNs.
- Leaving broken secure channels unresolved.
- Creating unnecessary trust relationships.
- Ignoring repeated authentication failures.

---

# Cybersecurity Perspective

Authentication infrastructure is a high-value target.

Security teams should monitor:

- Unusual authentication patterns.
- Failed logons.
- Kerberos ticket anomalies.
- Privileged account usage.
- Trust relationship changes.
- Domain Controller security events.

Compromised authentication systems can affect the entire enterprise.

---

# Hands-on Lab

## Objective

Explore Kerberos internals.

### Tasks

1. Run:

```powershell
whoami
```

2. View:

```powershell
whoami /groups
```

3. Display Kerberos tickets:

```powershell
klist
```

4. Verify:

```powershell
Test-ComputerSecureChannel
```

5. Open:

```text
Event Viewer
```

Review authentication-related logs.

6. Document:

- Current user
- Current groups
- Kerberos tickets
- Secure channel status

---

# Key Takeaways

- LSASS creates access tokens after successful authentication.
- The PAC carries authorization information within Kerberos tickets.
- Access tokens contain SIDs and privileges used during authorization.
- Trusts enable cross-domain and cross-forest authentication.
- PowerShell and built-in diagnostic tools assist with authentication troubleshooting.

---

# Interview Questions

1. What is LSASS?
2. What is the purpose of the PAC?
3. How is an access token created?
4. What information does an access token contain?
5. What is a logon session?
6. What is credential caching?
7. How does cross-domain authentication work?
8. Which command displays Kerberos tickets?
9. Which command checks the secure channel?
10. What are common causes of Kerberos authentication failures?

---

# References

- Microsoft Learn – Kerberos Authentication
- Microsoft Learn – LSASS
- Microsoft Learn – Kerberos PAC
- Microsoft Learn – Test-ComputerSecureChannel
- Microsoft Learn – Active Directory Trusts
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# Active-Directory/

# 14-Active-Directory-Authentication.md

# Part 4 — Authentication Security, Monitoring, Kerberos Attack Overview, Best Practices, Final Revision, Chapter Summary, and Interview Preparation

---

# Learning Objectives

After completing this part, you will be able to:

- Secure Active Directory authentication in enterprise environments.
- Monitor authentication events.
- Understand common Kerberos and NTLM attacks at a high level.
- Apply authentication security best practices.
- Review the complete Active Directory Authentication chapter.
- Prepare for Windows Server and Cybersecurity interviews.

> **Note:** This section provides defensive, administrator-focused overviews of common attack techniques. Detailed offensive methodologies are covered in dedicated security chapters with appropriate defensive context.

---

# Why Authentication Security Matters

Authentication is the gateway to every enterprise resource.

If authentication is compromised, attackers may gain access to:

- File Servers
- Domain Controllers
- Email
- Databases
- VPN
- Cloud Applications
- Administrative Consoles

Therefore, protecting authentication systems is one of the highest priorities for security teams.

---

# Enterprise Authentication Architecture

```text
                Users
                   │
                   ▼
          Domain-Joined Computer
                   │
                   ▼
                  DNS
                   │
                   ▼
           Domain Controller
             (KDC + AD DS)
                   │
                   ▼
            Kerberos / NTLM
                   │
                   ▼
            Access Token Created
                   │
                   ▼
             Enterprise Resources
```

---

# Authentication Security Layers

```text
Identity

↓

Strong Passwords

↓

Kerberos

↓

MFA

↓

Authorization

↓

Monitoring

↓

Incident Response
```

Each layer contributes to overall security.

---

# Password Security

Recommended practices:

- Long passwords or passphrases
- Unique passwords
- Password history enforcement
- Minimum password age (where appropriate)
- Account lockout policies
- Elimination of default passwords

Avoid:

- Dictionary words
- Company names
- Personal information
- Shared administrator passwords

---

# Multi-Factor Authentication (MFA)

MFA strengthens authentication by requiring more than one factor.

Example:

```text
Password

+

Authenticator App

↓

Authentication
```

Benefits include:

- Protection against stolen passwords
- Reduced risk from phishing (when paired with phishing-resistant methods)
- Improved identity assurance

---

# Windows Hello for Business

Windows Hello for Business provides a modern authentication experience using:

- PIN
- Biometrics
- Hardware-backed credentials (where supported)

Benefits:

- Reduced reliance on passwords
- Strong cryptographic authentication
- Improved user experience

---

# Smart Card Authentication

Many organizations use smart cards for privileged users.

Example:

```text
Smart Card

↓

PIN

↓

Kerberos Authentication
```

Advantages:

- Strong identity verification
- Hardware-backed credentials
- Reduced password exposure

---

# Authentication Logging

Authentication activity should be logged and monitored.

Examples:

- Successful logons
- Failed logons
- Account lockouts
- Kerberos events
- NTLM usage
- Privileged account logons

These logs are valuable for both operations and security investigations.

---

# Security Event Sources

Common log sources:

```text
Domain Controller

↓

Security Event Logs

↓

SIEM

↓

SOC

↓

Alerts
```

Centralized logging enables faster detection of suspicious activity.

---

# Monitoring Strategy

Security teams commonly monitor:

- Repeated failed logons
- Logons outside normal working hours
- Logons from unexpected locations
- Administrative account usage
- Authentication protocol usage
- Sudden spikes in account lockouts

---

# Authentication Event Flow

```text
User Login

↓

Domain Controller

↓

Security Log

↓

SIEM

↓

Alert

↓

SOC Investigation
```

---

# Account Lockout

Account lockout policies help reduce the effectiveness of password guessing attacks.

Example:

```text
Multiple Failed Logons

↓

Account Locked

↓

Administrator or Policy Unlock
```

Policies should balance security and operational needs.

---

# Kerberos Security Features

Kerberos provides:

- Mutual authentication
- Ticket-based authentication
- Limited ticket lifetime
- Single Sign-On
- Reduced password exposure

These features improve security compared to repeatedly transmitting credentials.

---

# High-Level Kerberos Threat Overview

Administrators should be aware of attacks that target Kerberos.

Examples include:

- Kerberoasting
- AS-REP Roasting
- Golden Ticket
- Silver Ticket
- Pass-the-Ticket

These attacks abuse authentication or ticket mechanisms rather than exploiting weaknesses in the Kerberos protocol itself.

---

# Kerberoasting (Overview)

Concept:

```text
Service Account

↓

Service Ticket Requested

↓

Offline Password Cracking Attempt
```

Mitigation:

- Strong service account passwords
- Managed Service Accounts (where appropriate)
- Regular password rotation
- Monitoring for unusual service ticket requests

---

# AS-REP Roasting (Overview)

Concept:

```text
Account

↓

Preauthentication Disabled

↓

Authentication Data Exposed

↓

Offline Password Cracking Attempt
```

Mitigation:

- Require Kerberos preauthentication for user accounts unless there is a documented exception.
- Audit accounts with preauthentication disabled.

---

# Golden Ticket (Overview)

Concept:

```text
Compromised KRBTGT Secret

↓

Forged TGT

↓

Potential Unauthorized Access
```

Mitigation:

- Protect Domain Controllers.
- Limit privileged access.
- Rotate the KRBTGT account password following Microsoft's guidance after compromise.
- Monitor for suspicious Kerberos activity.

---

# Silver Ticket (Overview)

Concept:

```text
Compromised Service Account Secret

↓

Forged Service Ticket

↓

Targeted Service Access
```

Mitigation:

- Protect service account credentials.
- Use Managed Service Accounts or Group Managed Service Accounts where appropriate.
- Rotate service account secrets regularly.

---

# Pass-the-Hash (Overview)

Concept:

```text
Compromised Password Hash

↓

Authentication Attempt

↓

Unauthorized Access
```

Mitigation:

- Protect credentials.
- Enable credential protection technologies where supported.
- Limit local administrator reuse.
- Apply least privilege.

---

# Pass-the-Ticket (Overview)

Concept:

```text
Stolen Kerberos Ticket

↓

Authentication Attempt

↓

Unauthorized Access
```

Mitigation:

- Protect endpoints.
- Monitor for abnormal Kerberos activity.
- Reduce privileged session exposure.
- Sign out of privileged sessions when work is complete.

---

# NTLM Risks

Because NTLM is maintained primarily for compatibility, organizations should:

- Identify NTLM usage.
- Replace legacy applications where possible.
- Prefer Kerberos.
- Audit NTLM authentication.

Reducing NTLM dependency improves security.

---

# Protecting Domain Controllers

Recommended controls:

- Dedicated administration
- Restricted interactive logons
- Frequent patching
- Strong physical security
- Secure backups
- Continuous monitoring
- Limited privileged access

Domain Controllers are among the most critical systems in an Active Directory environment.

---

# Authentication Hardening Checklist

| Control | Recommended |
|----------|-------------|
| Kerberos Preferred | ✔ |
| Reduce NTLM Usage | ✔ |
| MFA | ✔ |
| Windows Hello for Business | ✔ |
| Strong Password Policy | ✔ |
| Time Synchronization | ✔ |
| DNS Health | ✔ |
| Privileged Access Controls | ✔ |
| Centralized Logging | ✔ |
| Regular Auditing | ✔ |

---

# Enterprise Authentication Lifecycle

```text
HR Creates Employee

↓

Identity Created

↓

Group Membership Assigned

↓

Authentication Enabled

↓

User Accesses Resources

↓

Access Reviewed

↓

Employment Ends

↓

Account Disabled

↓

Account Removed
```

Identity lifecycle management is an essential part of enterprise security.

---

# Common Authentication Issues

| Problem | Possible Cause |
|----------|----------------|
| Cannot Log In | Incorrect password, expired account, account disabled |
| Kerberos Failure | DNS, time synchronization, SPN issue |
| Account Lockout | Repeated failed sign-in attempts |
| NTLM Fallback | Kerberos unavailable or incompatible application |
| Access Denied | Authorization or group membership issue |

---

# Enterprise Best Practices

- Use Kerberos whenever possible.
- Deploy MFA for privileged and remote access.
- Minimize NTLM usage.
- Monitor authentication logs continuously.
- Protect privileged accounts.
- Use strong password policies.
- Keep Domain Controllers secure.
- Maintain healthy DNS and time synchronization.
- Regularly review authentication policies.
- Test disaster recovery procedures.

---

# Common Administrative Mistakes

Avoid:

- Ignoring failed authentication events.
- Allowing excessive privileged accounts.
- Disabling security controls without justification.
- Misconfiguring DNS.
- Allowing inaccurate system time.
- Leaving obsolete service accounts enabled.
- Failing to rotate privileged credentials.

---

# Cybersecurity Perspective

Modern Security Operations Centers (SOCs) monitor authentication activity continuously.

Typical detections include:

- Excessive failed logons
- Unusual Kerberos activity
- Privileged account usage
- Account lockouts
- Geographic anomalies
- Authentication outside business hours
- Authentication from unexpected devices

Authentication telemetry is one of the most valuable data sources for detecting compromise.

---

# Hands-on Lab

## Objective

Review authentication behavior in a domain environment.

### Tasks

1. Sign in to a domain-joined computer.

2. Run:

```powershell
whoami
```

3. Display:

```powershell
klist
```

4. Open:

```text
Event Viewer
```

Review authentication-related events.

5. Verify:

- DNS configuration
- Time synchronization
- Domain membership

6. Document:

- Authentication protocol observed
- Kerberos tickets
- Current group memberships
- Authentication-related events

---

# Complete Chapter Summary

This chapter covered:

- Authentication fundamentals
- Authentication vs Authorization
- Domain Controllers
- DNS and authentication
- Secure Channel
- Kerberos
- NTLM
- KDC
- Authentication Service (AS)
- Ticket Granting Service (TGS)
- Ticket Granting Ticket (TGT)
- Service Tickets
- Service Principal Names (SPNs)
- Privilege Attribute Certificate (PAC)
- Access Tokens
- Logon Process
- Cross-domain authentication
- PowerShell tools
- Authentication security
- Monitoring
- Enterprise best practices

---

# Final Revision Table

| Topic | Key Point |
|--------|-----------|
| Authentication | Verifies identity |
| Authorization | Determines permissions |
| Kerberos | Default AD authentication protocol |
| NTLM | Legacy compatibility protocol |
| KDC | Issues Kerberos tickets |
| TGT | Used to request service tickets |
| Service Ticket | Grants access to a specific service |
| SPN | Identifies a Kerberos-enabled service |
| PAC | Contains authorization data |
| Access Token | Security context used for authorization |
| Secure Channel | Trusted communication between computer and domain |
| MFA | Improves authentication security |

---

# Interview Questions

## Basic

1. What is authentication?
2. What is the difference between authentication and authorization?
3. What is Kerberos?
4. What is NTLM?
5. What is the KDC?

## Intermediate

6. What is a TGT?
7. What is a Service Ticket?
8. What is the PAC?
9. What is an SPN?
10. Why is DNS important for authentication?

## Advanced

11. How does Kerberos enable Single Sign-On?
12. What is the role of LSASS during authentication?
13. How would you troubleshoot Kerberos authentication failures?
14. Why should NTLM usage be minimized?
15. How would you design authentication monitoring for a large enterprise?

---

# References

- Microsoft Learn – Windows Authentication
- Microsoft Learn – Kerberos Authentication
- Microsoft Learn – Active Directory Domain Services
- Microsoft Learn – Windows Hello for Business
- Microsoft Learn – Microsoft Defender for Identity
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices
- CIS Microsoft Windows Benchmarks
- NIST SP 800-63 Digital Identity Guidelines

---

# Congratulations!

You have successfully completed **Chapter 14 – Active Directory Authentication**.

You now understand:

- How authentication works in Active Directory.
- The differences between Kerberos and NTLM.
- The roles of the KDC, TGT, and Service Tickets.
- How access tokens and the PAC support authorization.
- How authentication works across trusted domains.
- Authentication monitoring and enterprise security best practices.
- Common authentication risks and defensive mitigations.

These concepts form the foundation for understanding enterprise identity systems and are essential for Windows Administrators, Active Directory Engineers, SOC Analysts, Incident Responders, Identity Administrators, and Cybersecurity Professionals.

---

