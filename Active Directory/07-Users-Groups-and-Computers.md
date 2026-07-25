# 07-Users-Groups-and-Computers.md

# Part 1 — Active Directory Objects: Users, Groups, and Computers Fundamentals

---

# Learning Objectives

After completing this part, you will be able to:

- Understand Active Directory objects.
- Learn the difference between Users, Groups, and Computers.
- Understand object attributes.
- Learn how Active Directory uniquely identifies objects.
- Understand object classes.
- Learn enterprise object organization.
- Prepare for authentication, authorization, and Group Policy.

---

# Introduction

Everything stored inside Active Directory is an **Object**.

Examples include:

- Users
- Groups
- Computers
- Organizational Units
- Printers
- Shared Folders
- Contacts
- Service Accounts
- Domain Controllers

Active Directory stores each object in its directory database along with numerous attributes that describe it.

---

# What is an Active Directory Object?

An **Active Directory Object** is an entity stored within the directory that represents a person, device, resource, or service.

Each object has:

- A unique identity
- A specific object class
- Attributes
- Permissions
- Security identifiers (where applicable)

---

# Types of Objects

```text
Active Directory

│

├── User

├── Group

├── Computer

├── Organizational Unit

├── Contact

├── Printer

├── Shared Folder

├── Service Account

└── Domain Controller
```

---

# Categories of Objects

Objects generally fall into two categories:

## Container Objects

These can contain other objects.

Examples:

- Domain
- Organizational Unit (OU)
- Container

---

## Leaf Objects

These cannot contain child objects.

Examples:

- User
- Group
- Computer
- Printer
- Contact

---

# Active Directory Object Structure

Every object consists of:

```text
Object

│

├── Name

├── Object Class

├── GUID

├── Distinguished Name

├── Attributes

├── Permissions

└── Security Identifier (if security principal)
```

---

# Object Classes

An object class defines what type of object it is and what attributes it can contain.

Examples:

| Object | Class |
|---------|-------|
| User | user |
| Group | group |
| Computer | computer |
| OU | organizationalUnit |
| Printer | printQueue |
| Contact | contact |

---

# Object Attributes

Each object contains attributes.

Example User:

```text
Name

↓

John Smith
```

Other attributes include:

- First Name
- Last Name
- Display Name
- Email
- Department
- Manager
- Telephone Number
- Office
- Employee ID
- Company
- Job Title
- Account Status

---

# Example User Object

```text
User

├── Name
├── Username
├── Display Name
├── Email
├── Department
├── Office
├── Manager
├── Phone
├── SID
├── GUID
└── Password (stored securely as credential data, not plaintext)
```

---

# Distinguished Name (DN)

Every object has a unique Distinguished Name.

Example:

```text
CN=John Smith,OU=Finance,DC=company,DC=com
```

Breaking it down:

```text
CN

↓

Common Name

OU

↓

Organizational Unit

DC

↓

Domain Component
```

---

# Relative Distinguished Name (RDN)

The **Relative Distinguished Name (RDN)** uniquely identifies an object within its parent container.

Example:

```text
CN=John Smith
```

Combined with the parent path:

```text
CN=John Smith

OU=Finance

DC=company

DC=com
```

This forms the full Distinguished Name.

---

# Globally Unique Identifier (GUID)

Every Active Directory object receives a **GUID** when it is created.

Example:

```text
550e8400-e29b-41d4-a716-446655440000
```

Characteristics:

- Globally unique
- Never reused
- Remains constant even if the object is renamed or moved
- Used internally by Active Directory

---

# Security Identifier (SID)

Security principals such as users, groups, and computers also receive a **Security Identifier (SID).**

Example:

```text
S-1-5-21-3623811015-3361044348-30300820-1013
```

The SID is used for:

- Authentication
- Authorization
- Access Control Lists (ACLs)
- Security auditing

Even if a user changes their username, the SID remains the same.

---

# GUID vs SID

| GUID | SID |
|------|-----|
| Identifies directory object | Identifies security principal |
| Used internally by AD | Used by Windows security |
| Never changes | Remains constant for the object |
| Exists for all AD objects | Exists only for security principals |

---

# User Objects

A **User Object** represents a person or identity that can authenticate to Active Directory.

Typical uses:

- Employee accounts
- Administrator accounts
- Service accounts
- Test accounts

---

# Example User

```text
John Smith

↓

Logs into Windows

↓

Accesses Email

↓

Uses Company Applications

↓

Accesses Shared Resources
```

The user account becomes the identity used throughout the enterprise.

---

# Computer Objects

Every domain-joined computer receives its own computer object.

Examples:

- Desktop
- Laptop
- Virtual Machine
- Windows Server

Example:

```text
HR-PC-101

↓

Computer Object

↓

Domain Authentication
```

---

# Why Computers Need Accounts

Computers authenticate just like users.

During startup:

```text
Computer

↓

Domain Controller

↓

Authentication

↓

Secure Channel Established
```

This secure relationship allows:

- Group Policy processing
- Domain authentication
- Kerberos communication
- Certificate enrollment
- Secure management

---

# Group Objects

Groups simplify permission management.

Instead of assigning permissions to every user individually:

```text
Users

↓

Group

↓

Resource
```

This approach is more scalable and easier to maintain.

---

# Example

Instead of:

```text
Alice → Folder

Bob → Folder

Charlie → Folder

David → Folder
```

Use:

```text
Finance Group

↓

Folder Permissions

↓

All Members
```

Adding or removing users from the group automatically changes their access.

---

# Security Principals

Security principals are objects that can be authenticated and assigned permissions.

Examples:

| Object | Security Principal |
|---------|--------------------|
| User | Yes |
| Group | Yes |
| Computer | Yes |
| Contact | No |
| Printer | No |
| OU | No |

Security principals possess SIDs and participate in access control.

---

# Object Relationships

```text
User

↓

Member Of

↓

Group

↓

Permissions

↓

Shared Folder
```

This relationship is central to authorization in Windows.

---

# Enterprise Example

A company employs 15,000 people.

Objects include:

```text
15,000 Users

↓

1,200 Groups

↓

10,000 Computers

↓

500 Servers

↓

Hundreds of OUs
```

Each object is uniquely identified and managed through Active Directory.

---

# Cybersecurity Perspective

Accurate object management is essential for enterprise security.

Poorly managed objects can result in:

- Unauthorized access
- Privilege escalation
- Orphaned accounts
- Stale computer accounts
- Excessive group membership
- Compliance violations

Security teams should regularly review:

- Disabled accounts
- Inactive users
- Dormant computers
- Privileged groups
- Unused service accounts

---

# Common Mistakes

Avoid:

- Sharing user accounts.
- Renaming accounts without documentation.
- Leaving disabled accounts indefinitely.
- Forgetting to remove stale computer accounts.
- Assigning permissions directly to users instead of groups.
- Creating duplicate objects for the same purpose.

---

# Hands-on Lab

## Objective

Explore Active Directory objects.

### Tasks

1. Open **Active Directory Users and Computers (ADUC)**.
2. Locate:
   - A user object
   - A computer object
   - A group object
3. View the properties of each object.
4. Identify:
   - Distinguished Name (DN)
   - Object class
   - Common attributes
5. Compare the properties of a user and a computer account.

---

# Interview Questions

1. What is an Active Directory object?
2. What is the difference between a container object and a leaf object?
3. What is an object class?
4. What is the purpose of object attributes?
5. What is a Distinguished Name?
6. What is the difference between a GUID and a SID?
7. Why do computer accounts exist?
8. What is a security principal?
9. Why should permissions generally be assigned to groups instead of individual users?
10. Name three common Active Directory object types.

---

# Key Takeaways

- Everything stored in Active Directory is represented as an object.
- Objects have classes, attributes, Distinguished Names, and unique identifiers.
- Users, groups, and computers are security principals and receive Security Identifiers (SIDs).
- GUIDs uniquely identify directory objects regardless of name changes.
- Proper object management is foundational for authentication, authorization, and enterprise security.

---

# 07-Users-Groups-and-Computers.md

# Part 2 — User Accounts, Computer Accounts, Group Types, Group Scopes, AGDLP, and Enterprise Identity Management

---

# Learning Objectives

After completing this part, you will be able to:

- Understand different types of user accounts.
- Learn the lifecycle of user accounts.
- Understand computer accounts.
- Differentiate security groups and distribution groups.
- Learn group scopes.
- Understand AGDLP and AGUDLP.
- Learn enterprise identity management best practices.

---

# User Accounts in Active Directory

A **User Account** represents a digital identity that can authenticate to Active Directory and access enterprise resources.

Examples include:

- Employee accounts
- Administrator accounts
- Service accounts
- Temporary contractor accounts
- Test accounts

Every user account has:

- Username
- Password
- SID
- GUID
- Group Memberships
- Attributes
- Permissions

---

# Types of User Accounts

| Account Type | Purpose |
|--------------|----------|
| Standard User | Daily work |
| Administrator | Administrative tasks |
| Service Account | Runs applications/services |
| Guest | Limited temporary access |
| Contractor | External workforce |
| Test Account | Lab/testing purposes |

---

# Standard User Accounts

Most employees receive a standard user account.

Example:

```text
Alice

↓

Sign in

↓

Email

↓

Office Applications

↓

Shared Drives

↓

Business Applications
```

A standard account should **not** have administrative privileges.

---

# Administrative Accounts

Administrators should use **separate privileged accounts**.

Example:

```text
John

↓

john.smith

(Standard Account)

Daily Work
```

```text
john.smith-admin

↓

Administrative Tasks
```

Benefits:

- Reduced attack surface
- Better auditing
- Supports least privilege
- Limits credential exposure

---

# Service Accounts

Applications often require accounts to run services.

Examples:

- SQL Server
- IIS
- Backup Software
- Monitoring Agents

Example:

```text
SQL Service

↓

Runs Database Service

↓

Accesses Required Resources
```

Service accounts should never be used for interactive logon unless absolutely necessary.

---

# User Account Lifecycle

Enterprise identity management follows a defined lifecycle.

```text
Recruitment

↓

Account Creation

↓

Active Employment

↓

Department Transfer

↓

Role Change

↓

Account Disable

↓

Account Deletion
```

Proper lifecycle management reduces security risks.

---

# New User Provisioning

Typical workflow:

```text
HR

↓

Employee Record

↓

Identity Created

↓

Group Membership Assigned

↓

Mailbox Created

↓

Applications Assigned

↓

User Starts Work
```

Automation often handles much of this process.

---

# User Attributes

Common user attributes include:

| Attribute | Example |
|-----------|----------|
| First Name | John |
| Last Name | Smith |
| Display Name | John Smith |
| Email | john.smith@company.com |
| Department | Finance |
| Job Title | Analyst |
| Manager | Sarah Brown |
| Office | Bengaluru |
| Employee ID | EMP10542 |
| Phone | +91-XXXXXXXXXX |

These attributes support searches, address books, automation, and reporting.

---

# Account States

User accounts may exist in different states.

```text
New

↓

Enabled

↓

Locked

↓

Disabled

↓

Deleted
```

Understanding these states helps administrators troubleshoot authentication issues.

---

# Disabled Accounts

Instead of immediately deleting accounts, organizations often disable them first.

Benefits:

- Preserves audit history
- Prevents accidental access
- Allows recovery if required
- Supports compliance requirements

---

# Locked Accounts

Accounts may become locked due to:

- Multiple failed logon attempts
- Password attacks
- Forgotten passwords
- Automated processes using old credentials

Administrators should determine the cause before unlocking an account.

---

# Computer Accounts

Every domain-joined computer receives a computer account.

Examples:

```text
FIN-PC-101

HR-LAPTOP-205

SQL-SERVER-01

WEB-SRV-10
```

Computer accounts are security principals and possess their own SID.

---

# Computer Authentication

Unlike user accounts, computer accounts authenticate automatically.

Example:

```text
Computer Starts

↓

Contacts Domain Controller

↓

Kerberos Authentication

↓

Secure Channel Established

↓

Policies Applied
```

This secure channel is essential for Active Directory communication.

---

# Computer Account Passwords

Computer accounts maintain passwords just like users.

Characteristics:

- Generated automatically
- Rotated automatically (by default in Windows environments)
- Not managed manually under normal circumstances
- Used to maintain the secure channel with the domain

---

# Computer Lifecycle

```text
Purchase

↓

Imaging

↓

Domain Join

↓

Production

↓

Maintenance

↓

Retirement

↓

Deletion
```

Lifecycle management helps maintain a clean directory.

---

# Group Objects

Groups simplify administration.

Instead of assigning permissions directly to users:

```text
User

↓

Group

↓

Permission

↓

Resource
```

This approach scales efficiently in enterprise environments.

---

# Why Groups Exist

Without groups:

```text
100 Users

↓

100 Individual Permissions
```

With groups:

```text
100 Users

↓

Finance Group

↓

One Permission Assignment
```

Administration becomes significantly easier.

---

# Types of Groups

There are two primary group types.

## Security Groups

Purpose:

- Assign permissions
- Control access
- Security filtering
- Group Policy filtering

Example:

```text
Finance_Read

↓

Shared Folder Access
```

---

## Distribution Groups

Purpose:

- Email distribution
- Messaging
- Collaboration

Distribution groups **cannot** be used to assign permissions.

Example:

```text
All Employees

↓

Email Announcement
```

---

# Security vs Distribution Groups

| Feature | Security Group | Distribution Group |
|----------|----------------|--------------------|
| Access Control | Yes | No |
| Email Distribution | Yes (if mail-enabled) | Yes |
| File Permissions | Yes | No |
| NTFS Permissions | Yes | No |
| Group Policy Filtering | Yes | No |

---

# Group Scopes

Active Directory defines three primary group scopes.

- Domain Local
- Global
- Universal

Choosing the correct scope is important for scalable access management.

---

# Domain Local Groups

Purpose:

Assign permissions to resources **within a single domain**.

Example:

```text
Finance Share

↓

Finance-Share-Access

↓

Users
```

Think of Domain Local groups as being **close to the resource**.

---

# Global Groups

Purpose:

Collect users with similar job roles or departmental functions.

Example:

```text
Finance Users

↓

Finance Global Group
```

Global groups are typically used to organize identities.

---

# Universal Groups

Purpose:

Provide membership across multiple domains within the same forest.

Example:

```text
India Finance

UK Finance

USA Finance

↓

Universal Finance Group
```

Useful in multi-domain forests.

---

# Group Scope Comparison

| Scope | Typical Members | Typical Use |
|--------|-----------------|-------------|
| Global | Users from same domain | Organize users |
| Domain Local | Users and groups | Assign permissions |
| Universal | Users/groups from multiple domains | Forest-wide access |

---

# AGDLP

AGDLP is Microsoft's recommended access management model for a **single-domain** environment.

It stands for:

```text
Accounts

↓

Global Groups

↓

Domain Local Groups

↓

Permissions
```

---

# AGDLP Example

```text
Alice

Bob

Charlie

↓

Finance Global Group

↓

Finance Share Domain Local Group

↓

Read/Write Permission

↓

Finance Folder
```

Benefits:

- Easy administration
- Simplified auditing
- Scalable permission management

---

# AGUDLP

For **multi-domain forests**, Microsoft recommends AGUDLP.

```text
Accounts

↓

Global Groups

↓

Universal Groups

↓

Domain Local Groups

↓

Permissions
```

This model supports resource sharing across domains while reducing administrative complexity.

---

# Enterprise Example

Company:

- India Domain
- UK Domain
- USA Domain

```text
India Finance Users

↓

Global Group

↓

Universal Finance

↓

Finance Resource Group

↓

Finance File Server
```

Each regional team manages its own users while permissions remain centralized.

---

# Identity Management Best Practices

✔ Use standard user accounts for daily work.

✔ Separate privileged accounts.

✔ Disable inactive accounts promptly.

✔ Review group memberships regularly.

✔ Assign permissions to groups, not users.

✔ Follow AGDLP or AGUDLP.

✔ Remove stale computer accounts.

✔ Document naming standards.

---

# Cybersecurity Perspective

Poor identity management is a frequent cause of security incidents.

Examples include:

- Dormant accounts
- Excessive privileges
- Shared accounts
- Orphaned service accounts
- Misconfigured group memberships
- Stale computer objects

Security teams should periodically review:

- Disabled accounts
- Inactive users
- Privileged groups
- Group nesting
- Service account usage
- Computer account health

---

# Common Mistakes

Avoid:

- Using administrator accounts for daily work.
- Assigning permissions directly to users.
- Sharing user credentials.
- Leaving disabled accounts indefinitely.
- Creating unnecessary Universal Groups.
- Forgetting to remove obsolete computer accounts.
- Ignoring periodic access reviews.

---

# Hands-on Lab

## Objective

Practice managing users, computers, and groups.

### Tasks

1. Create a test user named `John Test`.
2. Create a Global Security Group named `Finance-Users`.
3. Add `John Test` to the group.
4. Create a Domain Local Group named `Finance-Share-Access`.
5. Add the Global Group to the Domain Local Group.
6. Create a test computer account (or identify an existing lab computer account).
7. Review:
   - SID
   - Group memberships
   - Distinguished Name (DN)
8. Disable and then re-enable the test user account.

---

# Interview Questions

1. What is the difference between a standard user account and an administrator account?
2. Why should administrators use separate privileged accounts?
3. What is a service account?
4. Why do computers have Active Directory accounts?
5. What is the difference between a Security Group and a Distribution Group?
6. What are the three Active Directory group scopes?
7. Explain the AGDLP model.
8. When is AGUDLP preferred over AGDLP?
9. Why should permissions be assigned to groups rather than individual users?
10. What are common risks associated with inactive or stale accounts?

---

# Key Takeaways

- User, computer, and group objects form the foundation of Active Directory identity management.
- Standard and privileged accounts should be separated to improve security.
- Computer accounts authenticate automatically and maintain secure channels with the domain.
- Security Groups are used for authorization, while Distribution Groups are used primarily for messaging.
- AGDLP and AGUDLP are Microsoft-recommended models for scalable permission management.
- Regular identity reviews help reduce security risks and improve compliance.

---

**Next:** Part 3