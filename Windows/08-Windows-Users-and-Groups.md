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

# 08-Windows-Users-and-Groups.md

# Part 2 — Windows Groups, Built-in Security Groups, Privileges, User Rights, Account Management, and Local Security Policies

---

# Introduction

Managing hundreds or thousands of individual user permissions quickly becomes difficult and error-prone.

Instead of assigning permissions directly to every user, Windows uses **groups**.

A group is a collection of user accounts that share common permissions and privileges.

Example:

```text
Without Groups

Alice  ─┐
Bob    ─┼──> Assign Permissions Individually
John   ─┘


With Groups

Alice ─┐
Bob   ─┼──> Finance Group ──> Shared Permissions
John  ─┘
```

Groups simplify administration, improve security, and make enterprise management scalable.

---

# Learning Objectives

By the end of this section, you will understand:

- Windows groups
- Local groups
- Security groups
- Built-in groups
- Administrative groups
- User rights
- Privileges
- Group membership
- Local Security Policy
- Account management tools

---

# What is a Group?

A **group** is a security principal that contains multiple users.

Instead of assigning permissions individually:

```text
User

↓

Group

↓

Permission

↓

Resource
```

Windows evaluates permissions based on the user's group memberships.

---

# Advantages of Groups

Using groups provides:

- Easier administration
- Reduced configuration errors
- Simplified permission management
- Centralized access control
- Improved scalability
- Better auditing

---

# Types of Windows Groups

Windows supports multiple types of groups.

```text
Windows Groups

├── Local Groups
├── Domain Local Groups
├── Global Groups
├── Universal Groups
├── Built-in Groups
└── Special Identity Groups
```

This chapter primarily focuses on **local groups**.

Active Directory group scopes are covered later.

---

# Local Groups

Local groups exist only on a single Windows computer.

Characteristics:

- Stored locally
- Manage access to local resources
- Managed using Local Users and Groups
- Not replicated across computers

Example:

```text
PC01

↓

Administrators

↓

Local Users
```

---

# Security Groups

Security groups are used to assign permissions.

Example:

```text
Finance Group

↓

Read

↓

Write

↓

Finance Folder
```

Adding a new employee simply requires adding the user to the group.

---

# Distribution Groups

Distribution groups are used primarily for email systems.

Characteristics:

- Not used for Windows authorization
- Used by messaging platforms
- Simplify email distribution

Examples include departmental mailing lists.

---

# Group Membership

A user can belong to multiple groups.

Example:

```text
Alice

├── Users
├── Finance
├── Remote Desktop Users
└── Backup Operators
```

Windows combines permissions from all applicable group memberships.

---

# Built-in Windows Groups

Windows automatically creates several built-in groups.

Common examples include:

| Group | Purpose |
|--------|----------|
| Administrators | Full system administration |
| Users | Standard users |
| Guests | Limited access |
| Backup Operators | Backup and restore operations |
| Remote Desktop Users | Remote Desktop access |
| Network Configuration Operators | Network configuration tasks |
| Performance Monitor Users | Performance monitoring |
| Event Log Readers | Read Windows Event Logs |
| Hyper-V Administrators | Manage Hyper-V |

---

# Administrators Group

Members of the **Administrators** group can perform tasks such as:

- Install software
- Create users
- Modify system settings
- Install drivers
- Manage services
- Change security policies
- Access protected resources

Because of these powerful capabilities, administrator membership should be tightly controlled.

---

# Users Group

Most users belong to the **Users** group.

Capabilities include:

- Run applications
- Create personal files
- Change personal settings
- Use installed software

Restrictions include:

- Cannot install many system-wide applications
- Cannot modify protected operating system settings
- Cannot manage other users without elevation

---

# Guests Group

The **Guests** group provides highly restricted access.

Modern Windows installations typically disable the Guest account by default for security reasons.

---

# Backup Operators

Members of this group can:

- Perform backup operations
- Restore files
- Access files during backup processes

These permissions are intended for backup-related tasks and should be assigned carefully.

---

# Remote Desktop Users

Members can log on using Remote Desktop (subject to other policies and configuration).

Example:

```text
Remote User

↓

Remote Desktop Users

↓

RDP Login

↓

Desktop Session
```

---

# Event Log Readers

Allows users to read Windows Event Logs without granting full administrative rights.

Useful for:

- SOC Analysts
- Auditors
- Security Teams
- Help Desk Personnel

---

# Special Identity Groups

Windows also defines dynamic identities that cannot typically be managed manually.

Examples:

| Special Identity | Description |
|------------------|-------------|
| Everyone | Broad identity representing applicable users |
| Authenticated Users | Successfully authenticated identities |
| Interactive | Users logged on locally |
| Network | Users accessing over the network |
| Anonymous Logon | Unauthenticated connections (limited scenarios) |
| SYSTEM | Operating system identity |

These identities are evaluated dynamically by Windows.

---

# Nested Groups

In Active Directory environments, groups can contain other groups.

Example:

```text
Finance Users

↓

Accounting Group

↓

Finance Share
```

Nested groups simplify large-scale administration.

This topic is explored further in the Active Directory chapter.

---

# Group Membership Evaluation

When a user logs in:

```text
Authenticate User

↓

Collect Group Memberships

↓

Create Access Token

↓

Apply Permissions
```

The resulting access token contains the user's security identifiers (SIDs) and group memberships.

---

# User Rights vs Permissions

These terms are different.

| User Rights | Permissions |
|-------------|-------------|
| Allow system-level actions | Control access to resources |
| Managed through security policy | Applied to files, folders, registry, etc. |
| Example: Log on locally | Example: Read a file |

---

# Examples of User Rights

Examples include:

- Log on locally
- Log on through Remote Desktop Services
- Shut down the system
- Back up files
- Restore files
- Change the system time
- Load device drivers
- Debug programs

These are assigned through Local Security Policy or Group Policy.

---

# Privileges

Privileges are special capabilities granted to users or groups.

Examples:

- Backup privilege
- Restore privilege
- Debug privilege
- Shutdown privilege
- Take ownership privilege

Many privileges are exercised only when required and subject to Windows security mechanisms such as User Account Control (UAC).

---

# Local Security Policy

Windows includes **Local Security Policy** for configuring security settings on standalone systems.

Launch:

```text
secpol.msc
```

Categories include:

- Account Policies
- Local Policies
- Audit Policies
- User Rights Assignment
- Security Options

---

# User Rights Assignment

Location:

```text
Local Security Policy

↓

Local Policies

↓

User Rights Assignment
```

Examples:

- Allow log on locally
- Deny log on locally
- Back up files
- Restore files
- Shut down the system

These settings determine which users or groups can perform specific system actions.

---

# Account Policies

Account Policies include:

- Password Policy
- Account Lockout Policy
- Kerberos Policy (domain environments)

Typical password settings:

- Minimum password length
- Password complexity
- Password history
- Maximum password age
- Minimum password age

---

# Account Lockout Policy

Example:

```text
5 Failed Logons

↓

Account Locked

↓

Administrator Unlock

or

Automatic Unlock After Policy Interval
```

Proper lockout settings reduce brute-force attacks while minimizing disruption to legitimate users.

---

# Local Users and Groups Console

Administrative console:

```text
lusrmgr.msc
```

Provides graphical management for:

- Users
- Groups
- Membership
- Account properties

Available on supported Windows editions (not typically included in Windows Home editions).

---

# NET USER

Display users.

```cmd
net user
```

View user details.

```cmd
net user Alice
```

Create a user.

```cmd
net user Alice Password123! /add
```

Disable a user.

```cmd
net user Alice /active:no
```

Enable a user.

```cmd
net user Alice /active:yes
```

Delete a user.

```cmd
net user Alice /delete
```

---

# NET LOCALGROUP

Display local groups.

```cmd
net localgroup
```

View members.

```cmd
net localgroup Administrators
```

Add a member.

```cmd
net localgroup Administrators Alice /add
```

Remove a member.

```cmd
net localgroup Administrators Alice /delete
```

---

# Computer Management

Another management interface:

```text
compmgmt.msc

↓

Local Users and Groups

↓

Users

↓

Groups
```

Computer Management centralizes several administrative tools into a single console.

---

# Enterprise Example

A new Finance employee joins the company.

Instead of assigning permissions individually:

```text
Create User

↓

Finance Group

↓

Remote Desktop Users

↓

File Access

↓

Printer Access

↓

Application Access
```

Adding the user to the appropriate groups automatically grants the required access.

---

# Cybersecurity Perspective

Improper group management is a common cause of privilege escalation.

Examples include:

- Too many local administrators
- Orphaned administrative accounts
- Excessive group nesting
- Unused privileged groups
- Unauthorized group membership changes

Security teams should monitor:

- New administrator accounts
- Group membership modifications
- Privileged group changes
- Disabled security groups
- Unexpected account activation

Privileged group membership changes are high-value events in enterprise monitoring.

---

# Business Impact

Effective group management enables organizations to:

- Reduce administrative effort
- Improve scalability
- Enforce least privilege
- Meet compliance requirements
- Simplify onboarding and offboarding
- Improve auditability

Poorly managed groups increase operational risk and the likelihood of unauthorized access.

---

# Enterprise Best Practices

- Assign permissions to groups rather than individual users whenever practical.
- Follow the Principle of Least Privilege (PoLP).
- Minimize membership in the Administrators group.
- Review privileged groups regularly.
- Remove inactive accounts promptly.
- Document administrative group membership.
- Audit changes to privileged groups.
- Use role-based access control (RBAC) principles where appropriate.

---

# Practical Labs

## Lab 1 — View Local Groups

Open **Command Prompt**.

Run:

```cmd
net localgroup
```

Identify the built-in groups available on your system.

---

## Lab 2 — View User Details

Run:

```cmd
net user

net user <YourUserName>
```

Observe:

- Local group memberships
- Password settings
- Account status

---

## Lab 3 — Explore Local Security Policy

If available on your edition of Windows:

1. Launch:

```text
secpol.msc
```

2. Navigate to:

```text
Local Policies

↓

User Rights Assignment
```

Review the configured rights without making changes.

---

# Key Takeaways

- Groups simplify permission management.
- Built-in groups provide predefined administrative roles.
- User rights differ from resource permissions.
- Local Security Policy manages security settings on standalone systems.
- Group memberships become part of the user's access token during logon.
- Privileged groups should be carefully monitored and audited.

---

# Interview Questions

1. Why are groups preferred over assigning permissions directly to users?
2. What is the difference between a local group and a domain group?
3. What is the purpose of the Administrators group?
4. What is the difference between user rights and permissions?
5. What is `lusrmgr.msc` used for?
6. What does `net localgroup` do?
7. Why should administrator membership be minimized?
8. What are Special Identity Groups?
9. What is the purpose of Local Security Policy?
10. How does group membership affect a user's access token?

---

# References

- Microsoft Learn
- Microsoft Windows Security Documentation
- Microsoft Local Users and Groups Documentation
- Microsoft Local Security Policy Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 08-Windows-Users-and-Groups.md

# Part 3 — User Account Control (UAC), Access Tokens, Credential Management, Authentication Process, Logon Types, and Enterprise Identity Security

---

# Introduction

Creating users and assigning them to groups is only one part of Windows identity management.

Every time a user signs in, Windows must:

- Verify the user's identity
- Create a secure session
- Determine available privileges
- Build an access token
- Protect stored credentials
- Control privilege elevation

These mechanisms work together to ensure users can perform authorized tasks while preventing unauthorized access.

Understanding these concepts is essential for:

- Windows Administrators
- SOC Analysts
- Blue Team Engineers
- Penetration Testers
- Incident Responders
- Digital Forensic Investigators

---

# Authentication Workflow

A simplified Windows authentication process:

```text
User

↓

Username + Credential

↓

Credential Validation

↓

Authentication Successful

↓

Create Access Token

↓

Load User Profile

↓

Desktop Session
```

If authentication fails, Windows denies access and records the attempt in the Security Event Log (subject to audit policy).

---

# Authentication vs Authorization Review

```text
Authentication

↓

"Who are you?"

↓

Authorization

↓

"What are you allowed to do?"
```

Both are required before a protected resource can be accessed.

---

# Windows Logon Components

Several Windows components participate during sign-in.

```text
User

↓

Windows Logon Interface

↓

Credential Processing

↓

Authentication Package

↓

Local Security Authority (LSA)

↓

Access Token

↓

Windows Session
```

Each component has a defined responsibility in the authentication process.

---

# Local Security Authority (LSA)

The **Local Security Authority (LSA)** is responsible for enforcing the local security policy.

Responsibilities include:

- Authentication support
- Access token generation
- Security policy enforcement
- Audit generation
- Credential-related operations

The LSA is a core Windows security component.

---

# Security Accounts Manager (SAM)

The **Security Accounts Manager (SAM)** stores information about local user accounts.

Contents include:

- Local usernames
- Account information
- Password-related data (stored securely)
- Group membership references

SAM is used for **local authentication**.

Domain authentication is handled differently through Active Directory.

---

# Authentication Methods

Windows supports multiple authentication methods.

Examples include:

| Method | Typical Usage |
|----------|---------------|
| Password | Traditional authentication |
| PIN | Windows Hello |
| Biometrics | Fingerprint, facial recognition |
| Smart Card | Enterprise authentication |
| Security Key | FIDO-compatible devices |
| Certificate-based | Enterprise environments |

Organizations often combine these with Multi-Factor Authentication (MFA).

---

# Windows Hello

Windows Hello provides modern authentication using:

- PIN
- Fingerprint
- Facial recognition

Advantages include:

- Faster sign-in
- Reduced reliance on passwords
- Integration with supported enterprise identity solutions

The exact implementation varies depending on device capabilities and organizational policies.

---

# Multi-Factor Authentication (MFA)

Authentication factors fall into three broad categories:

```text
Something You Know

↓

Password / PIN

+

Something You Have

↓

Security Key / Smart Card / Mobile Device

+

Something You Are

↓

Fingerprint / Face
```

MFA significantly improves account security by requiring more than one factor.

---

# What is an Access Token?

An **Access Token** is created after successful authentication.

It contains the security context of the user.

Windows uses the access token whenever the user attempts to access protected resources.

---

# Access Token Workflow

```text
Authenticate User

↓

Determine Groups

↓

Determine Privileges

↓

Create Access Token

↓

Launch User Session
```

The access token remains associated with processes started by that user unless a different security context is used.

---

# Access Token Contents

Typical contents include:

- User SID
- Group SIDs
- User privileges
- Integrity level
- Logon session information
- Security attributes

Windows compares this information with security descriptors when making authorization decisions.

---

# Access Check

Whenever a user accesses a resource:

```text
Access Token

↓

Compare with ACL

↓

Permission Evaluation

↓

Allow

or

Deny
```

This process is transparent to the user and occurs repeatedly during normal system operation.

---

# Standard User Token

A standard user receives an access token containing:

- Standard user groups
- Standard user privileges
- No administrative privileges

The user cannot perform administrative tasks without elevation.

---

# Administrator Token

Administrative users have administrative capabilities, but modern Windows protects these using **User Account Control (UAC)**.

This reduces unnecessary use of elevated privileges during everyday activities.

---

# User Account Control (UAC)

**User Account Control (UAC)** helps prevent unauthorized system changes.

Instead of granting full administrative privileges to every application automatically, Windows requires explicit approval for many administrative actions.

---

# UAC Workflow

```text
Administrator Starts Program

↓

Administrative Operation Requested

↓

UAC Prompt

↓

Approve

↓

Elevated Process

or

Cancel
```

Only the approved process is elevated—not every running application.

---

# Why UAC Exists

Without UAC:

```text
Administrator

↓

Every Program

↓

Full Administrative Rights
```

With UAC:

```text
Administrator

↓

Standard Privileges

↓

Elevation Required

↓

Administrative Task
```

This reduces the impact of accidental or malicious actions.

---

# UAC Prompt Types

Common prompts include:

| Situation | Prompt |
|------------|--------|
| Administrator account | Consent prompt |
| Standard user account | Credential prompt |
| Trusted Windows component | May proceed automatically depending on policy |

Behavior can vary according to local or domain security policy.

---

# Integrity Levels

Windows assigns integrity levels to processes.

Common levels include:

```text
Low

↓

Medium

↓

High

↓

System
```

Higher-integrity processes have greater authority than lower-integrity processes.

---

# Integrity Level Example

```text
Web Browser

↓

Medium Integrity

↓

Cannot Modify

↓

High Integrity Administrative Process
```

Integrity levels help isolate applications and reduce unintended interactions.

---

# Credential Manager

Windows stores certain credentials using **Credential Manager**.

Examples include:

- Saved network credentials
- Remote Desktop credentials
- Web credentials (depending on application support)
- Generic credentials

Credential Manager simplifies repeated authentication to trusted resources.

---

# Credential Types

Windows supports several credential categories.

```text
Credentials

├── Windows Credentials
├── Web Credentials
└── Generic Credentials
```

Stored credentials should be reviewed periodically.

---

# Secure Credential Practices

Organizations should:

- Avoid unnecessary saved credentials.
- Remove obsolete entries.
- Use MFA where possible.
- Prefer enterprise identity solutions.
- Protect devices with disk encryption and strong authentication.

---

# Logon Types

Windows supports multiple logon scenarios.

| Logon Type | Example |
|-------------|----------|
| Interactive | User signs in locally |
| Network | Access shared folders |
| Remote Interactive | Remote Desktop |
| Service | Windows service |
| Batch | Scheduled task |
| Unlock | Unlocking a workstation |

Each logon type is recorded differently in Windows security logs.

---

# Interactive Logon

```text
Keyboard

↓

Username

↓

Password

↓

Desktop Session
```

This is the most common logon type for end users.

---

# Network Logon

Example:

```text
User

↓

File Server

↓

Authentication

↓

Access Shared Folder
```

The user may not receive a full desktop session.

---

# Remote Interactive Logon

Example:

```text
Remote Desktop Client

↓

Authentication

↓

Remote Desktop Session
```

Used by administrators, help desk staff, and remote workers.

---

# Service Logon

```text
Windows Service

↓

Service Account

↓

Authentication

↓

Service Starts
```

Applications often use service logons to operate in the background.

---

# Batch Logon

Scheduled tasks frequently use batch logons.

```text
Task Scheduler

↓

Stored Credentials

↓

Authentication

↓

Script Executes
```

Proper credential protection is essential for scheduled automation.

---

# Account Disable vs Delete

| Disable | Delete |
|----------|---------|
| Prevents sign-in | Removes account |
| Preserves profile | May require profile cleanup |
| Suitable for temporary inactivity | Suitable when account is no longer needed |

Many organizations disable accounts before permanently removing them.

---

# Account Lifecycle Review

```text
Create

↓

Configure

↓

Assign Groups

↓

Use

↓

Review

↓

Disable

↓

Delete
```

Regular reviews help identify unused or excessive privileges.

---

# Enterprise Example

A new administrator receives two accounts.

```text
Normal User Account

↓

Daily Work


Separate Administrative Account

↓

Administrative Tasks
```

This reduces exposure of privileged credentials during routine activities.

---

# Cybersecurity Perspective

Identity attacks remain among the most common enterprise threats.

Examples include:

- Password spraying
- Credential stuffing
- Phishing
- Token theft
- Privilege escalation
- Unauthorized privilege assignment
- Session hijacking

Security teams should monitor:

- Failed authentication attempts
- New privileged accounts
- Unusual logon types
- Unexpected elevation events
- Credential-related policy changes

No single event should be interpreted in isolation; analysts should correlate identity activity with endpoint, network, and application telemetry.

---

# Business Impact

Strong identity management provides:

- Better security
- Reduced risk of unauthorized access
- Regulatory compliance
- Improved auditing
- Faster incident investigations
- More reliable access control

Weak authentication practices increase the likelihood of compromise and operational disruption.

---

# Enterprise Best Practices

- Implement Multi-Factor Authentication (MFA).
- Use separate accounts for administration.
- Apply the Principle of Least Privilege (PoLP).
- Review privileged access regularly.
- Disable inactive accounts promptly.
- Minimize stored credentials.
- Monitor authentication and elevation events.
- Protect endpoints with encryption and endpoint security solutions.

---

# Practical Labs

## Lab 1 — Identify Your Security Context

Open **Command Prompt**.

Run:

```cmd
whoami

whoami /groups

whoami /priv
```

Observe:

- Current user
- Group memberships
- Available privileges

---

## Lab 2 — Review Credential Manager

Open:

```text
Control Panel

↓

Credential Manager
```

Review the credential categories available on your system.

Do not modify production credentials unless authorized.

---

## Lab 3 — Observe UAC

Attempt to launch an application that requires administrative privileges.

Observe:

- UAC prompt behavior
- Whether consent or credentials are requested
- The difference between standard and elevated execution

---

# Key Takeaways

- Authentication verifies identity; authorization determines access.
- LSA and SAM are fundamental Windows security components.
- Windows creates an access token after successful authentication.
- UAC helps reduce unnecessary administrative privilege use.
- Integrity levels provide additional isolation between processes.
- Credential management and MFA strengthen enterprise identity security.

---

# Interview Questions

1. What is an access token?
2. What information does an access token contain?
3. What is the purpose of User Account Control (UAC)?
4. What is the role of the Local Security Authority (LSA)?
5. What is the Security Accounts Manager (SAM)?
6. What are the common Windows logon types?
7. Why should administrators use separate privileged accounts?
8. What are Windows integrity levels?
9. What is Credential Manager used for?
10. How does Multi-Factor Authentication improve security?

---

# References

- Microsoft Learn
- Microsoft Windows Security Documentation
- Microsoft Windows Hello Documentation
- Microsoft Identity Platform Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

