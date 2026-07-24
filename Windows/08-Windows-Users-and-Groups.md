# 08-Windows-Users-and-Groups.md

# Part 1 — Windows User Accounts, Authentication Fundamentals, User Profiles, Security Identifiers (SIDs), and Account Types

---

# Introduction

Every interaction with Windows begins with a **user account**.

Whether someone logs on locally, remotely, or through a domain, Windows must first identify **who the user is** before determining **what the user is allowed to do**.

User accounts form the foundation of:

- Authentication
- Authorization
- Access Control
- Auditing
- User Profile Management
- Enterprise Identity Management

Understanding Windows user accounts is essential for:

- Windows Administrators
- Cybersecurity Engineers
- SOC Analysts
- Active Directory Administrators
- Incident Responders
- Digital Forensic Investigators
- Cloud Identity Engineers

This chapter focuses on **local Windows users and groups**. Domain identities and Active Directory are covered in later chapters.

---

# Learning Objectives

By the end of this part, you will understand:

- Windows identity model
- User accounts
- Local users
- Microsoft accounts
- Service accounts
- Built-in accounts
- User profiles
- Security Identifiers (SIDs)
- Authentication overview
- Account lifecycle

---

# Windows Identity Model

Windows identifies every user using a unique identity.

```text
User

↓

Username

↓

Security Identifier (SID)

↓

Authentication

↓

Access Token

↓

Access Resources
```

The username is what users recognize, while the **SID** is what Windows primarily uses internally.

---

# Authentication vs Authorization

These concepts are often confused.

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you access?" |
| Performed during sign-in | Evaluated whenever resources are accessed |

Example:

```text
User

↓

Enter Password

↓

Authentication Successful

↓

Access File

↓

Permission Check

↓

Authorization
```

---

# What is a User Account?

A Windows user account represents a digital identity that allows someone or something to interact with the operating system.

A user account contains information such as:

- Username
- SID
- Password (or credential)
- Group memberships
- Profile location
- Security settings
- Account status

---

# Types of Windows Accounts

Windows supports multiple account types.

```text
Windows Accounts

├── Local User
├── Microsoft Account
├── Domain User
├── Service Account
├── Built-in Accounts
└── Virtual Accounts
```

Each serves a different purpose.

---

# Local User Account

A **local user account** exists only on one Windows computer.

Characteristics:

- Stored locally
- Authenticates against the local Security Account Manager (SAM)
- Cannot automatically access domain resources
- Suitable for standalone systems

Example:

```text
PC01

↓

User: Alice

↓

Stored Locally
```

---

# Microsoft Account

A Microsoft account is an online identity used with Windows and Microsoft services.

Examples of integrated services include:

- OneDrive
- Microsoft Store
- Microsoft 365 (where applicable)
- Device synchronization

Benefits:

- Cloud synchronization
- Password recovery options
- Cross-device settings synchronization

---

# Domain User Account

A domain user account is managed centrally by **Active Directory Domain Services (AD DS)**.

```text
User

↓

Domain Controller

↓

Authentication

↓

Access Enterprise Resources
```

Benefits include:

- Centralized management
- Single Sign-On (SSO)
- Group Policy
- Enterprise authentication

This topic is covered in detail in the Active Directory chapter.

---

# Service Accounts

Service accounts allow Windows services and applications to run securely.

Examples include:

- Database services
- Backup software
- Monitoring tools
- Web servers

Unlike interactive users, service accounts are intended for applications rather than people.

---

# Built-in Windows Accounts

Windows creates several built-in accounts automatically.

Common examples:

| Account | Purpose |
|----------|----------|
| Administrator | Local administration |
| Guest | Limited access (disabled by default on modern Windows) |
| DefaultAccount | System-managed account |
| WDAGUtilityAccount | Used by Windows Defender Application Guard (supported editions) |

Organizations should review and secure built-in accounts according to policy.

---

# Virtual Accounts

Windows can create virtual service identities for certain services.

Advantages:

- Reduced password management
- Limited privileges
- Improved security
- Service isolation

Virtual accounts help minimize the need for manually managed service credentials.

---

# User Account Lifecycle

```text
Create

↓

Configure

↓

Assign Groups

↓

Use

↓

Modify

↓

Disable

↓

Delete
```

Administrators should manage accounts throughout their lifecycle.

---

# User Profiles

A **user profile** stores a user's personal environment.

Typical contents include:

- Desktop
- Documents
- Downloads
- Pictures
- AppData
- User settings
- Application preferences

---

# User Profile Location

Default path:

```text
C:\Users\Username
```

Example:

```text
C:\Users\Alice
```

---

# User Profile Structure

```text
C:\Users\Alice

├── Desktop
├── Documents
├── Downloads
├── Pictures
├── Music
├── Videos
├── Favorites
└── AppData
```

Each profile is isolated from other users by NTFS permissions.

---

# AppData Folder

The **AppData** directory stores application-specific data.

Structure:

```text
AppData

├── Local
├── LocalLow
└── Roaming
```

---

# Local

Stores machine-specific data.

Examples:

- Cache
- Temporary application files
- Large local databases

Typically not synchronized between devices.

---

# Roaming

Stores user-specific settings that can roam with the user in supported enterprise environments.

Examples:

- Application preferences
- User configurations
- Certain application data

Historically used with roaming profiles in Active Directory environments.

---

# LocalLow

Stores data for applications running with lower integrity levels.

Examples:

- Protected Mode applications
- Sandboxed processes

---

# Default User Profile

Windows maintains a default profile used when creating new user profiles.

Location:

```text
C:\Users\Default
```

New user accounts inherit the initial profile configuration from this template.

---

# Public Profile

Windows also includes a shared profile.

Location:

```text
C:\Users\Public
```

Contents may be accessible to multiple local users depending on permissions.

---

# Security Identifier (SID)

A **Security Identifier (SID)** uniquely identifies every security principal.

Examples include:

- User accounts
- Groups
- Computers (in domain contexts)
- Service accounts

Windows uses SIDs internally rather than usernames.

---

# SID Example

Example format:

```text
S-1-5-21-XXXXXXXX-XXXXXXXX-XXXXXXXX-1001
```

Each SID is unique.

Even if a username changes, its SID remains the same.

---

# Why Windows Uses SIDs

Imagine this scenario:

```text
User

↓

Rename Account

↓

Username Changes

↓

SID Remains

↓

Permissions Continue Working
```

Because permissions reference the SID, renaming an account does not invalidate existing access control entries.

---

# Viewing SIDs

Using Command Prompt:

```cmd
whoami /user
```

Example output:

```text
User Name

↓

SID
```

PowerShell can also display SIDs using object-based commands (covered in later chapters).

---

# Security Principals

Windows refers to identities that can be authenticated as **security principals**.

Examples:

- Local users
- Domain users
- Groups
- Service accounts
- Computer accounts (domain environments)

Each security principal has a SID.

---

# Logon Process Overview

Simplified workflow:

```text
User

↓

Username

↓

Password

↓

Credential Verification

↓

Authentication

↓

Access Token Created

↓

Desktop Loaded
```

The authentication mechanisms themselves (such as NTLM and Kerberos) are covered in later chapters.

---

# Password Policies

Organizations typically enforce password requirements.

Common policy elements include:

- Minimum length
- Complexity requirements
- Password history
- Maximum age
- Minimum age
- Account lockout thresholds

Modern guidance increasingly emphasizes long, unique passwords and multi-factor authentication over frequent mandatory password changes.

---

# Account Lockout

Repeated failed authentication attempts may trigger account lockout.

Example:

```text
Incorrect Password

↓

Repeated Failures

↓

Threshold Reached

↓

Account Locked
```

Lockout policies help reduce brute-force attacks.

---

# Enterprise Example

A new employee joins an organization.

Workflow:

```text
HR Request

↓

Create User Account

↓

Assign Groups

↓

Create Profile

↓

Issue Credentials

↓

User Logs In

↓

Access Granted
```

Identity management is often integrated with HR onboarding processes.

---

# Cybersecurity Perspective

Compromised user accounts are one of the most common attack vectors.

Threats include:

- Password guessing
- Credential theft
- Phishing
- Pass-the-Hash attacks
- Stolen authentication tokens
- Privilege escalation

Security teams should monitor:

- Failed logons
- New account creation
- Privilege changes
- Disabled security controls
- Suspicious authentication patterns

---

# Business Impact

Proper user account management enables:

- Secure access
- Regulatory compliance
- Better auditing
- Controlled resource access
- Improved productivity
- Reduced insider risk

Poor identity management can lead to unauthorized access, data breaches, and operational disruption.

---

# Enterprise Best Practices

- Apply the principle of least privilege.
- Use separate administrative accounts for administrative tasks.
- Disable unused accounts promptly.
- Review user accounts regularly.
- Enable account lockout policies.
- Use strong, unique passwords or passphrases.
- Implement Multi-Factor Authentication (MFA) where supported.
- Audit authentication events continuously.

---

# Practical Labs

## Lab 1 — View Current User

Open **Command Prompt**.

Run:

```cmd
whoami

whoami /user
```

Record:

- Username
- SID

---

## Lab 2 — Explore User Profile

Navigate to:

```text
C:\Users
```

Identify:

- Your profile
- Default
- Public

Explore the folders inside your own profile.

Do **not** modify system profile folders.

---

## Lab 3 — Review Account Information

Run:

```cmd
net user
```

Then inspect your account:

```cmd
net user <YourUserName>
```

Observe:

- Password status
- Local group membership
- Account status
- Last logon (if available)

---

# Key Takeaways

- Windows uses accounts to identify users and services.
- Authentication verifies identity; authorization determines access.
- Every security principal has a unique SID.
- User profiles store personal settings and application data.
- Built-in accounts should be secured and monitored.
- Strong account management practices improve enterprise security.

---

# Interview Questions

1. What is the difference between authentication and authorization?
2. What is a Security Identifier (SID)?
3. Why does Windows use SIDs instead of usernames for permissions?
4. What is the difference between a local account and a domain account?
5. What is stored in a user profile?
6. What is the purpose of the AppData folder?
7. What are the differences between `Local`, `LocalLow`, and `Roaming` under AppData?
8. What are built-in Windows accounts?
9. What is the purpose of account lockout policies?
10. Why should organizations use separate administrative accounts?

---

# References

- Microsoft Learn
- Microsoft Windows Security Documentation
- Microsoft Account Management Documentation
- Microsoft Windows Authentication Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

