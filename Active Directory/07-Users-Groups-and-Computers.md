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

**Next:** Part 2