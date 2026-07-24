# 09-Windows-Permissions-and-NTFS.md

# Part 1 — NTFS Fundamentals, Permissions, Access Control Lists (ACLs), Security Descriptors, Ownership, and Authorization Basics

---

# Introduction

One of the most important responsibilities of an operating system is controlling **who can access which resources**.

Imagine a company where every employee could:

- Read confidential HR files
- Modify payroll records
- Delete company databases
- Access executive documents

Such an environment would be insecure and unmanageable.

Windows prevents this by implementing **NTFS permissions** and the **Windows authorization model**.

NTFS (New Technology File System) allows administrators to control access to:

- Files
- Folders
- Drives
- Volumes
- Certain system objects

Understanding NTFS permissions is essential for:

- Windows Administrators
- Cybersecurity Engineers
- SOC Analysts
- Penetration Testers
- Incident Responders
- Active Directory Administrators
- Digital Forensic Analysts

---

# Learning Objectives

By the end of this part, you will understand:

- NTFS security model
- Authorization workflow
- Permissions
- Access Control Lists (ACLs)
- Security Descriptors
- Access Control Entries (ACEs)
- Ownership
- Inheritance overview
- Permission evaluation fundamentals

---

# Authentication vs Authorization

These two concepts are closely related but serve different purposes.

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Determines access |
| Login process | Resource access |
| Uses credentials | Uses permissions |
| Occurs first | Occurs after authentication |

Workflow:

```text
User

↓

Authentication

↓

Access Token

↓

Authorization

↓

Access Resource
```

---

# Windows Authorization Model

Every resource access request follows a similar process.

```text
User

↓

Access Token

↓

Requested Resource

↓

Security Descriptor

↓

ACL Evaluation

↓

Allow

or

Deny
```

Windows performs this evaluation automatically whenever a protected resource is accessed.

---

# What is NTFS?

**NTFS (New Technology File System)** is the primary file system used by modern Windows operating systems.

Besides storing files, NTFS provides advanced security features including:

- File permissions
- Folder permissions
- Ownership
- Encryption (EFS)
- Compression
- Auditing
- Disk quotas
- Alternate Data Streams (ADS)

NTFS is significantly more secure and feature-rich than older file systems such as FAT32.

---

# Why NTFS Permissions Exist

Without permissions:

```text
Everyone

↓

Everything

↓

Full Access
```

With NTFS:

```text
User

↓

Permission Check

↓

Authorized Access

↓

Protected Resource
```

Permissions enforce the principle of least privilege and help protect sensitive information.

---

# Security Principals

Permissions are assigned to **security principals**.

Examples include:

- Users
- Groups
- Computers (domain environments)
- Service accounts
- Virtual accounts

Each security principal is identified internally by a **Security Identifier (SID)**.

---

# Objects Protected by NTFS

NTFS can secure:

```text
NTFS Objects

├── Files
├── Folders
├── Volumes
└── Certain Metadata Objects
```

Each object contains security information describing who can access it.

---

# Security Descriptor

Every secured NTFS object has a **Security Descriptor**.

It contains:

```text
Security Descriptor

├── Owner
├── Group (primarily for compatibility)
├── DACL
└── SACL
```

The Security Descriptor is the central structure Windows uses to make authorization decisions.

---

# Components of a Security Descriptor

| Component | Purpose |
|------------|----------|
| Owner | Controls ownership-related rights |
| DACL | Determines allowed or denied access |
| SACL | Defines auditing rules |
| Security Information | Metadata describing object security |

---

# What is an ACL?

An **Access Control List (ACL)** is a list of rules attached to an object.

Each rule specifies:

- Who the rule applies to
- What access is granted or denied

There are two primary ACL types:

```text
ACL

├── DACL
└── SACL
```

---

# Discretionary Access Control List (DACL)

The **DACL** determines whether access is allowed or denied.

Example:

```text
Payroll Folder

↓

DACL

↓

HR Group → Allow Read

Finance Group → Allow Modify

Everyone → No Entry
```

If no applicable permissions allow the requested action, access is denied.

---

# System Access Control List (SACL)

The **SACL** controls **auditing**, not permissions.

Example:

```text
Sensitive File

↓

Read Attempt

↓

Audit Rule

↓

Security Event Log
```

SACLs define which access attempts should generate audit events.

---

# Access Control Entry (ACE)

An ACL is composed of multiple **Access Control Entries (ACEs)**.

Example:

```text
ACL

├── ACE 1
├── ACE 2
├── ACE 3
└── ACE 4
```

Each ACE contains one permission rule.

---

# ACE Structure

An ACE typically specifies:

- Security Principal (SID)
- Allow or Deny
- Permission mask
- Inheritance information
- Flags

Example:

```text
Alice

↓

Allow

↓

Read
```

---

# Allow ACE

Example:

```text
Engineering Group

↓

Allow

↓

Modify
```

Members of the Engineering group can modify the resource (subject to overall permission evaluation).

---

# Deny ACE

Example:

```text
Interns

↓

Deny

↓

Delete
```

Deny entries should be used carefully because they can override allow permissions during evaluation.

---

# Common NTFS Permissions

Windows provides several standard NTFS permissions.

| Permission | Description |
|------------|-------------|
| Full Control | Complete access, including changing permissions and ownership |
| Modify | Read, write, execute, and delete |
| Read & Execute | Read files and run executable files |
| List Folder Contents | View folder contents (folders only) |
| Read | View data and attributes |
| Write | Create or modify files and folders |

These standard permissions are combinations of more granular special permissions.

---

# Permission Hierarchy

```text
Full Control

↓

Modify

↓

Read & Execute

↓

Read

↓

Write
```

Higher permission levels generally include the capabilities of lower levels.

---

# Full Control

Allows users to:

- Read
- Write
- Modify
- Delete
- Change permissions
- Take ownership (subject to applicable privileges)

Because of its broad capabilities, Full Control should be granted only when necessary.

---

# Modify

Allows users to:

- Read
- Write
- Execute
- Delete

However, users generally cannot change the object's permissions unless additional rights are granted.

---

# Read & Execute

Users can:

- Read files
- Execute applications
- Open folders
- View attributes

Commonly assigned for application directories.

---

# Read

Allows:

- View file contents
- View attributes
- View permissions
- Read metadata

Read permission does not allow modifying content.

---

# Write

Allows:

- Create files
- Modify data
- Create folders
- Update file contents

Write permission alone does not automatically allow deleting objects.

---

# Basic vs Special Permissions

Windows exposes:

```text
Permissions

├── Basic Permissions
└── Special Permissions
```

Basic permissions are predefined combinations of individual special permissions.

---

# Special Permissions

Examples include:

- Read Attributes
- Write Attributes
- Read Extended Attributes
- Write Extended Attributes
- Delete
- Delete Subfolders and Files
- Read Permissions
- Change Permissions
- Take Ownership
- Synchronize

Administrators can configure these for fine-grained access control.

---

# Viewing Permissions

Graphical interface:

```text
Right Click

↓

Properties

↓

Security

↓

Permissions
```

Command-line tools and PowerShell can also display security information.

---

# Permission Example

```text
Finance Folder

↓

Finance Group

↓

Modify

↓

Employee Can Edit Files
```

Group-based permission assignment simplifies administration.

---

# File vs Folder Permissions

Permissions may behave differently depending on the object.

| File | Folder |
|------|---------|
| Controls file access | Controls folder access and inheritance |
| Individual object | Container object |
| No child objects | May contain child files and folders |

Inheritance is covered in the next part.

---

# Ownership

Every NTFS object has an **owner**.

The owner has special authority over the object, including the ability (subject to policy and privileges) to manage permissions.

Ownership is distinct from permission assignment.

---

# Ownership Workflow

```text
Create File

↓

Assign Owner

↓

Permissions Applied

↓

Resource Protected
```

---

# Enterprise Example

An HR department stores payroll information.

```text
Payroll Folder

↓

HR Security Group

↓

Modify

↓

Managers

↓

Read

↓

Other Users

↓

No Access
```

Instead of assigning permissions individually, administrators assign permissions to groups.

---

# Cybersecurity Perspective

Incorrect NTFS permissions are a frequent cause of security incidents.

Common risks include:

- World-writable folders
- Excessive Full Control assignments
- Unauthorized permission inheritance
- Sensitive data exposed to broad groups
- Unnecessary administrative access

Attackers often search for overly permissive directories to:

- Access confidential information
- Replace executable files
- Escalate privileges
- Establish persistence

Regular permission reviews help reduce these risks.

---

# Business Impact

Proper NTFS permission management provides:

- Confidentiality of sensitive data
- Controlled collaboration
- Regulatory compliance
- Reduced insider risk
- Improved auditability
- Protection against accidental modification

Poor permission management can result in unauthorized access, data loss, and compliance violations.

---

# Enterprise Best Practices

- Assign permissions to groups rather than individual users.
- Apply the Principle of Least Privilege (PoLP).
- Avoid granting Full Control unless required.
- Use Deny permissions sparingly.
- Review permissions periodically.
- Protect sensitive folders with restricted access.
- Document permission structures for critical systems.

---

# Practical Labs

## Lab 1 — View NTFS Permissions

Create a test folder.

Open:

```text
Right Click

↓

Properties

↓

Security
```

Identify:

- Users
- Groups
- Assigned permissions

---

## Lab 2 — Compare Permissions

Create:

```text
Folder A

Folder B
```

Assign different permissions to each.

Compare:

- Read
- Modify
- Full Control

Observe how the permission entries differ.

---

## Lab 3 — View Owner

Open:

```text
Properties

↓

Security

↓

Advanced
```

Identify:

- Current owner
- Permission entries
- Inheritance status

Do not modify production permissions.

---

# Key Takeaways

- NTFS permissions provide fine-grained authorization for files and folders.
- Authentication identifies users; authorization determines access.
- Every secured NTFS object contains a Security Descriptor.
- ACLs consist of Access Control Entries (ACEs).
- DACLs control permissions, while SACLs control auditing.
- Ownership and permissions are related but distinct concepts.
- Group-based permission assignment simplifies enterprise administration.

---

# Interview Questions

1. What is the difference between authentication and authorization?
2. What is an Access Control List (ACL)?
3. What is the difference between a DACL and a SACL?
4. What is an Access Control Entry (ACE)?
5. What information does a Security Descriptor contain?
6. What is the difference between Modify and Full Control?
7. Why should Full Control be granted sparingly?
8. What is the purpose of NTFS permissions?
9. Who can be assigned NTFS permissions?
10. Why are groups preferred over individual user permissions?

---

# References

- Microsoft Learn
- Microsoft Windows Security Documentation
- Microsoft NTFS Documentation
- Microsoft Access Control Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

