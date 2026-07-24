# Active-Directory/

# 12-Active-Directory-Users-and-Computers.md

# Part 1 — Introduction to Active Directory Users and Computers (ADUC), Object Fundamentals, User Accounts, Computer Accounts, and Enterprise Administration

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Active Directory Users and Computers (ADUC) is.
- Learn Active Directory object fundamentals.
- Understand User and Computer objects.
- Learn object attributes.
- Understand object identity.
- Understand enterprise account administration.

---

# Introduction

Imagine an enterprise with:

- 150,000 employees
- 80 offices
- 120,000 computers
- Thousands of servers
- Thousands of service accounts

Every identity needs:

- Authentication
- Authorization
- Management
- Auditing
- Lifecycle management

The administrative tool used most frequently for this is:

> **Active Directory Users and Computers (ADUC)**

---

# What is ADUC?

**Active Directory Users and Computers (ADUC)** is the primary Microsoft Management Console (MMC) snap-in used to administer objects stored in Active Directory Domain Services (AD DS).

Administrators use ADUC to:

- Create users
- Create groups
- Create computer accounts
- Manage OUs
- Reset passwords
- Unlock accounts
- Delegate administration
- Move objects
- View object properties

---

# Launching ADUC

Common methods:

```text
Run

↓

dsa.msc
```

or

```text
Server Manager

↓

Tools

↓

Active Directory Users and Computers
```

---

# What Can ADUC Manage?

ADUC manages many Active Directory object types, including:

- Users
- Groups
- Computers
- Organizational Units (OUs)
- Contacts
- Shared folders (published)
- Managed Service Accounts
- Domain Controllers
- Containers

---

# ADUC Architecture

```text
Administrator

↓

ADUC Console

↓

Domain Controller

↓

Active Directory Database

↓

Directory Objects
```

---

# Active Directory Objects

Everything stored in Active Directory is an **object**.

Examples:

```text
User

Computer

Group

Printer

Contact

OU
```

Each object has:

- Attributes
- Permissions
- Unique identity
- Object class

---

# Object Hierarchy

```text
Forest

↓

Domain

↓

OU

↓

Objects
```

Objects are organized logically within the directory.

---

# What is a User Object?

A **User Object** represents an identity that can authenticate to Active Directory.

Typical examples:

- Employees
- Contractors
- Administrators
- Service accounts (traditional user-based service accounts)

---

# User Account Example

```text
Anita

↓

Username

↓

Password

↓

Permissions

↓

Group Membership

↓

Authentication
```

---

# Common User Attributes

Every user object stores numerous attributes.

Examples:

| Attribute | Purpose |
|-----------|----------|
| Display Name | Friendly name |
| Given Name | First name |
| Surname | Last name |
| User Logon Name (UPN) | Sign-in name |
| sAMAccountName | Legacy logon name |
| Email | Mail address |
| Department | Business unit |
| Manager | Reporting relationship |
| Telephone | Contact information |
| Office | Physical location |

---

# User Identity

A user is identified using several values.

Examples:

```text
Display Name

↓

John Smith
```

```text
UPN

↓

john.smith@company.com
```

```text
sAMAccountName

↓

jsmith
```

```text
SID

↓

Unique Security Identifier
```

Each serves a different administrative purpose.

---

# What is a SID?

A **Security Identifier (SID)** is a unique value assigned to every security principal.

Example:

```text
S-1-5-21-XXXXXXXX-XXXXXXXX-XXXXXXXX-1105
```

Windows uses the SID internally for security decisions rather than relying on object names.

---

# Why Names Are Not Enough

Suppose:

```text
John Smith
```

changes to:

```text
John Wilson
```

The display name changes.

The SID remains the same.

Permissions continue to work because access control is based on the SID.

---

# Distinguished Name (DN)

Every object has a Distinguished Name that identifies its location in the directory.

Example:

```text
CN=John Smith,
OU=Finance,
DC=company,
DC=com
```

If the object moves to another OU, the Distinguished Name changes because the object's location changes.

---

# Relative Distinguished Name (RDN)

The first component of the Distinguished Name is the:

```text
CN=John Smith
```

This is the **Relative Distinguished Name (RDN)**.

---

# Object GUID

Every Active Directory object also has a globally unique identifier.

Example:

```text
Object GUID

↓

550e8400-e29b-41d4-a716-446655440000
```

Unlike the Distinguished Name, the Object GUID does **not** change when the object is moved or renamed.

---

# Identity Comparison

| Identifier | Changes? | Purpose |
|------------|----------|----------|
| Display Name | Yes | Friendly display |
| UPN | Can change | User sign-in |
| sAMAccountName | Can change | Legacy logon |
| Distinguished Name | Changes when moved/renamed | Directory location |
| SID | Remains constant | Security |
| Object GUID | Remains constant | Permanent object identity |

---

# What is a Computer Object?

A **Computer Object** represents a domain-joined computer.

Examples:

- Windows 11 workstation
- Windows Server
- Virtual machine
- Kiosk
- Laptop

---

# Computer Account

Joining a computer to a domain creates:

```text
Computer

↓

Computer Object

↓

Authentication Identity
```

The computer authenticates to the domain using its own account.

---

# Computer Naming

Example:

```text
BLR-PC-001

NYC-LT-105

SRV-FILE-01
```

Consistent naming standards simplify administration.

---

# Computer Account Password

Like user accounts, computer accounts also have passwords.

These passwords are:

- Generated automatically.
- Managed automatically by Windows.
- Changed periodically by domain-joined systems.

Administrators normally do not manage these passwords manually.

---

# Workstation Authentication

```text
Computer Starts

↓

Computer Account Authenticates

↓

Secure Channel Established

↓

User Logs In
```

Both the computer and the user participate in authentication.

---

# Enterprise Example

Company:

```text
40,000 Computers
```

Each computer has:

- Computer account
- SID
- Group memberships
- Policies
- Authentication relationship

---

# User Lifecycle

Typical lifecycle:

```text
Hire

↓

Create Account

↓

Assign Groups

↓

Grant Access

↓

Modify

↓

Disable

↓

Delete
```

Identity management is an ongoing administrative process.

---

# Computer Lifecycle

Typical lifecycle:

```text
Purchase

↓

Join Domain

↓

Move to OU

↓

Receive Policies

↓

Retire

↓

Disable

↓

Delete
```

---

# Common Administrative Tasks

User administration:

- Create users
- Disable users
- Reset passwords
- Unlock accounts
- Move users
- Manage group membership

Computer administration:

- Join domain
- Reset computer account
- Move computer
- Disable computer
- Delete computer
- Manage delegated administration

---

# Enterprise Organization

```text
Company

↓

Departments

↓

Users
```

```text
Company

↓

Locations

↓

Computers
```

Separating users and computers into appropriate OUs improves administration and policy management.

---

# Best Practices

- Use standardized naming conventions.
- Populate important user attributes.
- Place objects in the correct OUs.
- Disable unused accounts before deletion when appropriate.
- Document administrative standards.
- Follow least-privilege principles.

---

# Common Misconceptions

## Myth 1

> Users are identified by their names.

**Reality:**

Windows primarily uses the SID for security decisions.

---

## Myth 2

> Computer accounts are optional.

**Reality:**

Domain-joined computers require computer accounts for secure authentication.

---

## Myth 3

> Renaming a user changes permissions.

**Reality:**

Permissions continue to work because they are associated with the SID, not the display name.

---

# Cybersecurity Perspective

Proper identity management is fundamental to enterprise security.

Security teams should:

- Disable inactive accounts promptly.
- Review administrative accounts regularly.
- Maintain accurate user attributes.
- Monitor privileged group membership.
- Audit account lifecycle events.
- Protect service and administrative accounts.

Poor account management increases the risk of unauthorized access and compliance issues.

---

# Hands-on Lab

## Objective

Explore Active Directory objects using ADUC.

### Tasks

1. Open:

```text
dsa.msc
```

2. Browse:

- Users
- Computers
- OUs
- Groups

3. Create a test user.

4. View:

- Attribute Editor (if Advanced Features are enabled)
- User properties
- Computer properties

5. Record:

- Distinguished Name
- UPN
- sAMAccountName
- SID (using PowerShell or appropriate tools)
- Object GUID

---

# Key Takeaways

- ADUC is the primary GUI tool for Active Directory administration.
- Everything stored in Active Directory is an object.
- User and computer accounts each have unique identities.
- SID and Object GUID provide persistent identity.
- Proper object organization supports enterprise administration.

---

# Interview Questions

1. What is Active Directory Users and Computers (ADUC)?
2. What is a User Object?
3. What is a Computer Object?
4. What is a SID?
5. Why is the SID important?
6. What is a Distinguished Name?
7. What is the difference between a DN and an Object GUID?
8. Why do computer accounts have passwords?
9. What happens when a computer joins a domain?
10. What are common administrative tasks performed in ADUC?

---

# References

- Microsoft Learn – Active Directory Users and Computers
- Microsoft Learn – Active Directory Object Management
- Microsoft Learn – Security Identifiers (SIDs)
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 2 — User Account Management, Computer Account Management, Account Properties, Password Policies, and Enterprise Administration**