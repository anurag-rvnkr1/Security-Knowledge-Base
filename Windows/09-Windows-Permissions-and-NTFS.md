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

# 09-Windows-Permissions-and-NTFS.md

# Part 2 — NTFS Permission Inheritance, Effective Permissions, Ownership, Special Permissions, and Permission Evaluation

---

# Introduction

Assigning permissions is only the beginning of Windows authorization.

When a user attempts to access a file or folder, Windows must determine:

- Which permissions apply
- Which permissions were inherited
- Whether multiple group memberships affect access
- Whether explicit permissions override inherited permissions
- Whether any **Deny** entries exist
- What the user's **effective permissions** are

Understanding this evaluation process is critical for administrators and cybersecurity professionals because many access-related issues arise from misunderstandings of inheritance and permission evaluation.

---

# Permission Evaluation Workflow

```text
User Requests Access

↓

Authenticate User

↓

Access Token

↓

Collect User & Group SIDs

↓

Read Security Descriptor

↓

Evaluate DACL

↓

Apply Allow/Deny Rules

↓

Grant or Deny Access
```

This process occurs automatically whenever Windows protects an NTFS resource.

---

# Permission Inheritance

By default, child objects inherit permissions from their parent folder.

Example:

```text
Projects

├── Reports
├── Source
└── Documentation
```

If **Projects** grants:

```text
Engineering → Modify
```

then the child folders inherit the same permission unless inheritance is changed.

---

# Benefits of Inheritance

Inheritance provides:

- Consistent permissions
- Easier administration
- Reduced configuration effort
- Lower risk of mistakes
- Scalable enterprise management

Without inheritance, administrators would need to configure permissions on every individual file and folder.

---

# Inheritance Example

```text
Root Folder

↓

Finance

↓

Payroll

↓

Salary.xlsx
```

If the **Finance** folder grants:

```text
Finance Group → Modify
```

then:

- Payroll
- Salary.xlsx

inherit those permissions unless inheritance is disabled or overridden.

---

# Explicit Permissions

Explicit permissions are assigned directly to an object.

Example:

```text
Payroll Folder

↓

HR Group

↓

Modify
```

These permissions exist only on the Payroll folder unless inherited by child objects.

---

# Inherited Permissions

Inherited permissions come from a parent object.

Example:

```text
Company

↓

Finance

↓

Payroll

↓

Inherited Permissions
```

No manual assignment is required on the child object.

---

# Explicit vs Inherited Permissions

| Explicit | Inherited |
|-----------|-----------|
| Assigned directly | Received from parent |
| Higher precedence | Lower precedence |
| Local to object | Originates from ancestor |
| Easier to customize | Easier to manage consistently |

Explicit permissions generally take precedence over inherited permissions.

---

# Viewing Inheritance

Graphically:

```text
Right Click

↓

Properties

↓

Security

↓

Advanced
```

Windows indicates whether permissions are:

- Explicit
- Inherited

This helps administrators understand where permissions originate.

---

# Disabling Inheritance

Administrators can disable inheritance on an object.

Workflow:

```text
Parent Folder

↓

Child Folder

↓

Disable Inheritance

↓

Choose:

• Convert inherited permissions to explicit

or

• Remove inherited permissions
```

Removing inherited permissions without careful planning can unintentionally deny legitimate access.

---

# Converting Inherited Permissions

When disabling inheritance, administrators often choose:

```text
Convert

↓

Inherited Permissions

↓

Explicit Permissions
```

This preserves existing access while allowing independent modification.

---

# Removing Inherited Permissions

Alternative option:

```text
Disable Inheritance

↓

Remove Inherited Entries

↓

Start with Clean ACL
```

This approach is useful when creating highly restricted folders but should be used cautiously.

---

# Effective Permissions

A user's **effective permissions** represent the final permissions Windows applies after evaluating:

- User permissions
- Group memberships
- Explicit permissions
- Inherited permissions
- Allow entries
- Deny entries

Effective permissions determine whether access is ultimately granted.

---

# Effective Permission Workflow

```text
User

↓

User SID

+

Group SIDs

↓

Permission Evaluation

↓

Effective Permissions

↓

Access Decision
```

---

# Multiple Group Memberships

Users often belong to multiple groups.

Example:

```text
Alice

├── Users
├── Finance
├── Managers
└── Remote Desktop Users
```

Windows combines applicable permissions before making an access decision.

---

# Combining Allow Permissions

Example:

```text
Finance Group

↓

Read


Managers Group

↓

Write
```

Alice belongs to both groups.

Effective result:

```text
Read

+

Write

↓

Modify Capabilities
```

Allow permissions generally accumulate unless affected by Deny entries.

---

# Deny Permissions

Windows supports explicit **Deny** permissions.

Example:

```text
Finance Group

↓

Allow Read


Interns

↓

Deny Read
```

If a user belongs to both groups, the explicit Deny entry generally overrides the Allow entry for that permission.

Because Deny entries can create complexity, they should be used carefully.

---

# Permission Evaluation Order (Simplified)

A simplified view of evaluation is:

```text
Explicit Deny

↓

Explicit Allow

↓

Inherited Deny

↓

Inherited Allow
```

Windows performs detailed access checks internally, but this order helps explain many common scenarios.

---

# Example 1

Folder:

```text
Reports
```

Permissions:

```text
Engineering

↓

Modify
```

Alice belongs to Engineering.

Result:

```text
Modify Access
```

---

# Example 2

Permissions:

```text
Users

↓

Read


Managers

↓

Write
```

Alice belongs to both.

Result:

```text
Read + Write
```

Combined permissions allow broader access than either permission alone.

---

# Example 3

Permissions:

```text
Managers

↓

Allow Modify


Interns

↓

Deny Delete
```

Alice belongs to both groups.

Result:

```text
Modify

Except

Delete
```

The Deny entry affects the specific denied operation.

---

# Ownership Review

Every NTFS object has an owner.

Example:

```text
Create File

↓

Owner Assigned

↓

Owner Can Manage Security
```

Ownership is separate from ordinary read/write permissions.

---

# Changing Ownership

Administrators (or users with appropriate rights) can change ownership.

Graphical workflow:

```text
Properties

↓

Security

↓

Advanced

↓

Owner

↓

Change
```

Ownership changes should follow organizational authorization procedures.

---

# Take Ownership Permission

One special NTFS permission is:

```text
Take Ownership
```

This permission allows an authorized user to become the owner of an object.

Because ownership affects security administration, this permission should be tightly controlled.

---

# Change Permissions Permission

Another important special permission is:

```text
Change Permissions
```

Users with this permission can modify the object's DACL.

They do **not** automatically become the owner.

---

# Delete vs Delete Subfolders and Files

These special permissions are different.

| Permission | Purpose |
|------------|----------|
| Delete | Delete the object itself |
| Delete Subfolders and Files | Delete child objects within a folder |

Understanding the distinction is important when designing secure folder structures.

---

# Read Permissions

Allows users to:

- View current ACL
- View security settings
- Inspect assigned permissions

This permission does not allow modifying the ACL.

---

# Synchronize Permission

The **Synchronize** permission is used internally by Windows for coordinating access to objects.

Administrators rarely modify this permission directly.

---

# Advanced Security Settings

The **Advanced Security Settings** dialog provides:

- Owner information
- Permission entries
- Inheritance controls
- Effective Access (supported Windows versions)
- Auditing configuration (where available)

It is the primary graphical interface for advanced NTFS security management.

---

# Effective Access Tool

Windows includes an **Effective Access** feature (supported editions).

Workflow:

```text
Choose User

↓

Analyze Permissions

↓

Effective Access Report
```

This helps administrators troubleshoot complex permission issues.

---

# Command-Line Permission Tools

Windows provides command-line utilities for managing NTFS permissions.

Common examples include:

| Tool | Purpose |
|------|----------|
| `icacls` | Display and modify NTFS permissions |
| `takeown` | Take ownership of files and folders |
| `whoami` | Display identity information |
| `cacls` *(legacy)* | Older ACL utility (superseded) |

PowerShell also provides advanced security management capabilities, covered in a later chapter.

---

# ICACLS Example

Display permissions:

```cmd
icacls C:\Projects
```

Typical output includes:

- Users
- Groups
- Permission levels
- Inheritance indicators

`icacls` is the recommended command-line tool for NTFS permission management.

---

# TAKEOWN Example

Take ownership:

```cmd
takeown /F C:\Projects
```

Administrative privileges are typically required.

Ownership should only be changed when authorized.

---

# Enterprise Example

A confidential HR folder requires stricter security.

```text
Company

↓

HR

↓

Disable Inheritance

↓

Convert Existing Entries

↓

Remove Unnecessary Groups

↓

HR Group → Modify

↓

Managers → Read

↓

Auditing Enabled
```

This approach limits access while preserving required functionality.

---

# Cybersecurity Perspective

Misconfigured NTFS permissions are a common source of privilege escalation.

Examples include:

- Writable application directories
- Overly permissive shared folders
- Unauthorized inheritance
- Incorrect ownership
- Excessive Full Control assignments

Attackers frequently enumerate:

- Weak ACLs
- Writable services
- Startup folders
- Sensitive configuration files

Regular permission reviews and least-privilege design reduce these risks.

---

# Business Impact

Proper inheritance and permission management provide:

- Consistent access control
- Easier administration
- Lower operational costs
- Better compliance
- Reduced insider risk
- Faster troubleshooting

Poorly designed ACLs can expose confidential information or disrupt business operations.

---

# Enterprise Best Practices

- Keep inheritance enabled unless there is a clear business requirement.
- Assign permissions to groups instead of individual users.
- Minimize explicit Deny entries.
- Review ownership of sensitive resources.
- Document exceptions to inherited permissions.
- Regularly audit critical file and folder ACLs.
- Use the Effective Access tool when troubleshooting complex authorization issues.

---

# Practical Labs

## Lab 1 — Observe Inheritance

1. Create a parent folder.
2. Create two child folders.
3. Assign permissions to the parent.
4. Verify that the child folders inherit those permissions.

Document the inherited entries.

---

## Lab 2 — Disable Inheritance

Using a test folder:

1. Open:

```text
Properties

↓

Security

↓

Advanced
```

2. Disable inheritance.

3. Compare:

- Convert inherited permissions
- Remove inherited permissions

Observe how the permission entries change.

---

## Lab 3 — View Permissions Using ICACLS

Open **Command Prompt**.

Run:

```cmd
icacls %USERPROFILE%
```

Identify:

- Users
- Groups
- Permission entries
- Inheritance indicators

Do not modify permissions on production systems.

---

# Key Takeaways

- Inheritance simplifies permission management by propagating permissions from parent objects.
- Explicit permissions generally take precedence over inherited permissions.
- Effective permissions are calculated using user, group, allow, deny, and inheritance information.
- Ownership and permissions are related but independent concepts.
- `icacls` and `takeown` are important NTFS administration tools.
- Least privilege and regular ACL reviews improve enterprise security.

---

# Interview Questions

1. What is permission inheritance?
2. What is the difference between explicit and inherited permissions?
3. What are effective permissions?
4. How does Windows combine permissions from multiple groups?
5. Why should Deny permissions be used carefully?
6. What is the purpose of the `icacls` command?
7. What does the `takeown` command do?
8. What happens when inheritance is disabled?
9. What is the difference between ownership and Full Control?
10. Why is the Effective Access tool useful?

---

# References

- Microsoft Learn
- Microsoft NTFS Security Documentation
- Microsoft Access Control Documentation
- Microsoft `icacls` Documentation
- Microsoft `takeown` Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 09-Windows-Permissions-and-NTFS.md

# Part 3 — NTFS Advanced Permissions, Sharing Permissions, Encrypting File System (EFS), Auditing, Access-Based Enumeration, and Enterprise File Security

---

# Introduction

NTFS permissions provide fine-grained access control for local file systems, but enterprise environments require additional security capabilities.

Organizations often need to:

- Share folders across the network
- Encrypt sensitive files
- Audit access attempts
- Hide confidential resources
- Monitor unauthorized activity
- Protect data from insider threats

Windows combines NTFS with additional technologies to provide layered file security.

---

# Enterprise File Security Model

```text
User

↓

Authentication

↓

Access Token

↓

Share Permissions (Network Access)

↓

NTFS Permissions

↓

Auditing

↓

Protected Resource
```

For network access, both **Share Permissions** and **NTFS Permissions** participate in authorization.

---

# NTFS Permissions vs Share Permissions

These permission systems serve different purposes.

| NTFS Permissions | Share Permissions |
|------------------|-------------------|
| Apply locally and over the network | Apply only to network access |
| Configured on Security tab | Configured on Sharing tab |
| More granular | Simpler permission model |
| Stored in NTFS | Stored as share configuration |

A user accessing a shared folder over the network must satisfy **both** permission sets.

---

# Share Permissions

Windows provides three standard share permissions.

| Permission | Capabilities |
|------------|--------------|
| Read | View files and folders |
| Change | Read, create, modify, delete |
| Full Control | Change permissions and manage sharing settings (subject to ownership and administrative rights) |

Share permissions are evaluated only for network access.

---

# Share Permission Workflow

```text
Remote User

↓

Network Share

↓

Share Permission Check

↓

NTFS Permission Check

↓

Access Granted or Denied
```

Both permission systems must allow the requested operation.

---

# Combined Permission Evaluation

Consider:

```text
Share Permission

↓

Read


NTFS Permission

↓

Modify
```

Effective network access:

```text
Read
```

The **most restrictive effective result** applies across the combined share and NTFS evaluation.

---

# Example 1

Share:

```text
Read
```

NTFS:

```text
Full Control
```

Result:

```text
Read
```

---

# Example 2

Share:

```text
Full Control
```

NTFS:

```text
Modify
```

Result:

```text
Modify
```

---

# Example 3

Share:

```text
Change
```

NTFS:

```text
Read
```

Result:

```text
Read
```

---

# Recommended Enterprise Practice

Many organizations configure:

```text
Share

↓

Everyone

↓

Full Control


↓

Control Access Using NTFS
```

This approach centralizes detailed authorization in NTFS permissions, reducing administrative complexity.

Note: Modern organizations often replace broad **Everyone** access with authenticated or role-based groups depending on security requirements.

---

# Hidden Shares

Windows supports hidden administrative-style shares.

Example:

```text
Finance$
```

The trailing:

```text
$
```

prevents casual browsing of the share name.

Users who know the share path and have appropriate permissions can still access it.

---

# Administrative Shares

Windows automatically creates administrative shares such as:

| Share | Purpose |
|--------|----------|
| `C$` | System drive administration |
| `ADMIN$` | Windows directory administration |
| `IPC$` | Inter-process communication |

These shares are intended for administrative use and should be protected appropriately.

---

# Encrypting File System (EFS)

**Encrypting File System (EFS)** provides file-level encryption on NTFS volumes.

Workflow:

```text
File

↓

Encrypt

↓

Encryption Key

↓

Encrypted Data
```

Only authorized users with the appropriate encryption keys can decrypt the data.

---

# EFS Characteristics

EFS provides:

- File-level encryption
- Folder-level encryption
- Transparent operation after authentication
- Integration with NTFS

Unlike full-disk encryption, EFS protects selected files and folders.

---

# EFS Example

```text
Payroll.xlsx

↓

Encrypt

↓

Encrypted on Disk

↓

Authorized User Opens File

↓

Automatic Decryption
```

Encryption and decryption occur transparently for authorized users.

---

# EFS vs BitLocker

| EFS | BitLocker |
|------|-----------|
| File-level protection | Volume-level protection |
| Selective encryption | Entire drive encryption |
| User-based | Device/volume-based |
| Protects individual files | Protects offline storage |

Many enterprise environments use BitLocker for device protection and EFS only where file-level encryption is specifically required.

---

# Data Recovery Agent (DRA)

Organizations may configure **Data Recovery Agents (DRAs)** for EFS.

Purpose:

```text
Encrypted File

↓

Recovery Certificate

↓

Authorized Recovery

↓

Business Continuity
```

DRAs help organizations recover encrypted data under approved procedures.

---

# File Auditing

Windows can audit file access using **SACLs**.

Examples:

- Read attempts
- Write attempts
- Delete attempts
- Permission changes
- Ownership changes

Auditing helps detect unauthorized access and supports forensic investigations.

---

# Auditing Workflow

```text
User Accesses File

↓

SACL Evaluation

↓

Audit Rule Matches

↓

Security Event Generated

↓

Event Log
```

Audit generation depends on both SACL configuration and system audit policy.

---

# Audit Policies

Administrators configure auditing through:

```text
Local Security Policy

↓

Advanced Audit Policy

↓

Object Access

↓

File System
```

Audit policies determine whether configured SACLs generate events.

---

# Common Audit Events

Organizations commonly audit:

- Failed access attempts
- Successful access to sensitive files
- Permission modifications
- Ownership changes
- Deletion of critical data

Not every file requires auditing; excessive auditing may increase log volume.

---

# Access-Based Enumeration (ABE)

**Access-Based Enumeration (ABE)** hides folders that users cannot access.

Without ABE:

```text
Finance

HR

Legal

Engineering
```

Every folder may be visible.

With ABE:

```text
Finance User

↓

Finance
```

Only authorized folders appear.

This improves usability and reduces unnecessary information disclosure.

---

# Access-Based Enumeration Workflow

```text
User

↓

Permission Check

↓

Visible Resources

↓

Hidden Unauthorized Folders
```

ABE does **not** replace NTFS permissions; it complements them.

---

# Offline Files

Windows supports cached copies of network files.

Workflow:

```text
File Server

↓

Offline Cache

↓

User Works Offline

↓

Reconnect

↓

Synchronization
```

Offline Files improve availability for mobile users.

---

# File Synchronization Conflicts

Synchronization may produce conflicts when:

```text
User A

↓

Edit File

↑

↓

File Server

↑

↓

User B

↓

Edit Same File
```

Administrators should establish version control and collaboration procedures to minimize conflicts.

---

# Sensitive Data Protection

Examples of sensitive enterprise data include:

- Payroll
- HR records
- Customer information
- Intellectual property
- Legal documents
- Financial reports

These resources often require:

- Restricted NTFS permissions
- Encryption
- Auditing
- Backup
- Monitoring

---

# Data Classification

Organizations commonly classify data.

Example:

```text
Public

↓

Internal

↓

Confidential

↓

Highly Confidential
```

Higher classifications typically require stronger security controls.

---

# Information Barriers

Sensitive departments often require isolation.

Example:

```text
HR

↓

HR Group Only

--------------------

Finance

↓

Finance Group Only
```

Proper permission design supports confidentiality.

---

# Enterprise Example

A Human Resources department stores employee records.

Security configuration:

```text
HR Share

↓

NTFS

↓

HR Group → Modify

Managers → Read

Auditing Enabled

EFS Applied to Sensitive Files

ABE Enabled
```

This layered approach combines authorization, encryption, and auditing.

---

# Cybersecurity Perspective

Misconfigured shares are a common attack vector.

Examples include:

- World-readable shares
- Writable shared folders
- Excessive administrative shares
- Missing auditing
- Weak encryption practices

Attackers frequently enumerate:

- Shared folders
- Administrative shares
- Writable locations
- Sensitive documents

Security teams should regularly review both share and NTFS permissions.

---

# Business Impact

Enterprise file security provides:

- Data confidentiality
- Regulatory compliance
- Reduced insider risk
- Improved forensic visibility
- Business continuity
- Better protection of intellectual property

Weak file security can expose confidential data and increase operational and legal risk.

---

# Enterprise Best Practices

- Use NTFS permissions as the primary authorization mechanism.
- Apply the Principle of Least Privilege (PoLP).
- Enable auditing only where business requirements justify it.
- Encrypt highly sensitive data.
- Review shared folders regularly.
- Restrict administrative share access.
- Implement Access-Based Enumeration where appropriate.
- Classify sensitive data and align permissions with classification.

---

# Practical Labs

## Lab 1 — Compare Share and NTFS Permissions

Create a test shared folder.

Configure:

- Share permissions
- NTFS permissions

Access the share from another authorized device (where available) and compare the effective permissions.

---

## Lab 2 — Review Administrative Shares

Open **Command Prompt**.

Run:

```cmd
net share
```

Identify:

- Administrative shares
- User-created shares
- Share names ending with `$`

Do not modify production shares without authorization.

---

## Lab 3 — Explore Advanced Security

Open:

```text
Properties

↓

Security

↓

Advanced
```

Review:

- Permission entries
- Inheritance
- Owner
- Auditing (if available)

Document the security configuration of a test folder.

---

# Key Takeaways

- Share permissions apply only to network access.
- NTFS permissions apply locally and across the network.
- Effective network access depends on both share and NTFS permissions.
- EFS provides file-level encryption for NTFS volumes.
- SACLs enable auditing of file access.
- Access-Based Enumeration hides resources users cannot access.
- Layered security improves enterprise data protection.

---

# Interview Questions

1. What is the difference between NTFS permissions and share permissions?
2. Which permission set determines effective access over a network?
3. What is Encrypting File System (EFS)?
4. How does EFS differ from BitLocker?
5. What is the purpose of a Data Recovery Agent (DRA)?
6. What is a SACL?
7. What is Access-Based Enumeration (ABE)?
8. Why are hidden shares identified with a `$` suffix?
9. Why should sensitive files be audited?
10. Why do organizations classify data?

---

# References

- Microsoft Learn
- Microsoft NTFS Documentation
- Microsoft EFS Documentation
- Microsoft Windows File Services Documentation
- Microsoft Access-Based Enumeration Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 09-Windows-Permissions-and-NTFS.md

# Part 4 — Enterprise NTFS Administration, Permission Management Tools, Security Best Practices, Chapter Summary, and Interview Preparation

---

# Introduction

NTFS permissions are one of the most important security controls in Windows.

In enterprise environments, administrators must not only configure permissions but also:

- Standardize permission structures
- Troubleshoot access issues
- Audit security configurations
- Monitor permission changes
- Protect sensitive information
- Maintain regulatory compliance
- Respond to security incidents

This chapter concludes with enterprise administration techniques, security best practices, and a complete review of NTFS permissions.

---

# Enterprise Permission Management Workflow

A well-managed organization typically follows this workflow:

```text
Business Requirement

↓

Data Classification

↓

Create Security Groups

↓

Assign NTFS Permissions

↓

Verify Effective Access

↓

Enable Auditing

↓

Periodic Review

↓

Continuous Monitoring
```

This structured approach reduces configuration errors and supports long-term maintainability.

---

# Designing Secure Folder Structures

Rather than assigning permissions randomly, enterprise environments use a hierarchical design.

Example:

```text
CompanyData

├── Finance
├── HR
├── Engineering
├── Legal
└── Shared
```

Each department receives dedicated security groups and clearly defined access.

---

# Role-Based Permission Assignment

Example:

```text
Finance_Read

↓

Read Access

----------------------

Finance_Modify

↓

Modify Access

----------------------

Finance_Admin

↓

Full Control
```

Instead of assigning permissions directly to users, administrators assign users to the appropriate role-based groups.

---

# Permission Management Strategy

A common enterprise strategy is:

```text
Users

↓

Department Groups

↓

Role Groups

↓

NTFS Permissions

↓

Protected Resources
```

This minimizes administrative effort and simplifies audits.

---

# Common NTFS Administration Tools

Windows provides several tools for managing permissions.

| Tool | Purpose |
|------|----------|
| File Explorer | Graphical permission management |
| `icacls` | View and modify NTFS permissions |
| `takeown` | Take ownership |
| `whoami` | Display identity information |
| PowerShell | Automate permission management |
| Computer Management | General administration |

PowerShell is covered in detail in a later chapter.

---

# Using ICACLS

Display permissions:

```cmd
icacls C:\Finance
```

Save permissions to a file:

```cmd
icacls C:\Finance /save perms.txt /t
```

Restore permissions:

```cmd
icacls C:\ /restore perms.txt
```

Reset inherited permissions:

```cmd
icacls C:\Finance /reset
```

**Important:** Test commands in a non-production environment before applying them to critical systems.

---

# Understanding ICACLS Output

Example:

```text
C:\Finance

BUILTIN\Administrators:(F)

Finance:(M)

Managers:(RX)
```

Common abbreviations:

| Symbol | Meaning |
|---------|----------|
| F | Full Control |
| M | Modify |
| RX | Read & Execute |
| R | Read |
| W | Write |

---

# Using TAKEOWN

Example:

```cmd
takeown /F C:\Finance
```

Recursive example:

```cmd
takeown /F C:\Finance /R
```

Administrative privileges are generally required.

Ownership should only be changed when authorized.

---

# Backup Before Permission Changes

Before modifying permissions:

```text
Review Current ACL

↓

Backup ACL

↓

Apply Changes

↓

Verify Access

↓

Document Changes
```

Backing up ACLs helps recover from accidental misconfiguration.

---

# Permission Troubleshooting Process

When a user cannot access a file:

```text
Verify User Identity

↓

Check Group Membership

↓

Check NTFS Permissions

↓

Check Share Permissions

↓

Check Inheritance

↓

Check Effective Access

↓

Review Audit Logs

↓

Resolve Issue
```

Following a consistent troubleshooting process reduces time to resolution.

---

# Common Permission Problems

| Problem | Possible Cause |
|----------|----------------|
| Access Denied | Missing permission or explicit Deny |
| Cannot Delete File | Missing Delete permission or file in use |
| Unexpected Access | Excessive group membership |
| Inheritance Issues | Broken inheritance |
| Missing Folder | Access-Based Enumeration |
| Permission Drift | Uncontrolled manual changes |

---

# Permission Drift

Permission drift occurs when ACLs gradually change over time without proper governance.

Example:

```text
Initial Folder

↓

Temporary Exception

↓

Another Exception

↓

Multiple Manual Changes

↓

Complex ACL

↓

Difficult to Audit
```

Periodic reviews help detect and correct permission drift.

---

# Periodic Access Reviews

Organizations should regularly review:

- Department folders
- Sensitive file shares
- Administrative permissions
- Ownership
- Group memberships
- Service account access

Periodic reviews improve compliance and reduce unnecessary privileges.

---

# Least Privilege Review

Questions administrators should ask:

- Does the user still require this access?
- Can permissions be reduced?
- Is Full Control necessary?
- Should access be time-limited?
- Is there a role-based alternative?

These reviews support continuous security improvement.

---

# Change Management

Permission changes should follow an approved process.

```text
Business Request

↓

Approval

↓

Implementation

↓

Testing

↓

Documentation

↓

Monitoring
```

Formal change management reduces the risk of accidental outages.

---

# Permission Documentation

Critical resources should have documented:

- Folder purpose
- Owner
- Security groups
- Permission model
- Data classification
- Business justification
- Review schedule

Good documentation simplifies audits and incident response.

---

# Security Monitoring

Security teams should monitor:

- Permission changes
- Ownership changes
- Failed file access
- Administrative actions
- Sensitive file access
- New shared folders

Many organizations forward these events to a SIEM for centralized analysis.

---

# Incident Response Example

SOC Alert:

```text
Critical File

↓

Permission Changed

↓

Unexpected User

↓

Sensitive File Read

↓

Investigation Started
```

Analysts investigate:

- Who changed the permission?
- Was the change authorized?
- Which files were accessed?
- Was data modified or copied?
- Should access be revoked?

---

# Ransomware Perspective

Attackers often attempt to:

- Encrypt shared folders
- Delete backups
- Modify permissions
- Disable security controls
- Spread through writable network shares

Well-designed NTFS permissions can reduce the attack surface and limit lateral movement.

---

# Insider Threat Perspective

Potential indicators include:

- Access to unrelated departments
- Large-scale file copying
- Unauthorized permission changes
- Ownership changes
- Access outside normal working hours

These indicators require investigation within the broader business context.

---

# Enterprise Example

A financial institution protects customer records.

Security model:

```text
Customer Data

↓

Finance_Admin

↓

Full Control

↓

Finance_Staff

↓

Modify

↓

Auditors

↓

Read

↓

Auditing Enabled

↓

Daily Permission Review
```

This layered approach balances operational needs with regulatory requirements.

---

# Business Impact

Effective NTFS administration provides:

- Stronger access control
- Better compliance
- Reduced insider risk
- Improved operational efficiency
- Simplified audits
- Faster troubleshooting
- Better incident response

Poor permission management can lead to data breaches, service disruption, and regulatory penalties.

---

# Enterprise Best Practices

- Design permissions using security groups.
- Follow the Principle of Least Privilege (PoLP).
- Avoid assigning permissions directly to users whenever possible.
- Use inheritance unless a valid business requirement exists.
- Limit Full Control assignments.
- Review permissions periodically.
- Backup ACLs before major changes.
- Monitor permission and ownership changes.
- Classify sensitive data.
- Document permission models for critical resources.

---

# Practical Labs

## Lab 1 — Display Permissions with ICACLS

Open **Command Prompt**.

Run:

```cmd
icacls %USERPROFILE%
```

Identify:

- Groups
- Permission abbreviations
- Inheritance indicators

---

## Lab 2 — Compare Effective Access

Create two local test users (in a lab environment).

Assign:

- Different group memberships
- Different NTFS permissions

Verify which user can:

- Read
- Write
- Delete

Document the effective permissions.

---

## Lab 3 — Permission Review Exercise

Choose a non-production folder.

Review:

```text
Owner

↓

Permission Entries

↓

Inheritance

↓

Groups

↓

Special Permissions
```

Recommend improvements using least privilege principles.

---

# Chapter Summary

In this chapter, you learned:

- NTFS fundamentals
- Authorization workflow
- Security Descriptors
- Access Control Lists (ACLs)
- Access Control Entries (ACEs)
- DACLs and SACLs
- Standard and special NTFS permissions
- Ownership
- Inheritance
- Effective permissions
- Share permissions
- Encrypting File System (EFS)
- Data Recovery Agents (DRAs)
- File auditing
- Access-Based Enumeration (ABE)
- Administrative tools
- Enterprise permission management
- Security monitoring
- Permission troubleshooting

These concepts form the foundation of Windows file security and are essential for system administration, cybersecurity operations, and Active Directory environments.

---

# Key Takeaways

- NTFS is the primary authorization mechanism for Windows files and folders.
- Security Descriptors contain ownership and ACL information.
- DACLs determine access, while SACLs define auditing.
- Effective permissions depend on user identity, group memberships, inheritance, and Allow/Deny entries.
- Share permissions apply only to network access.
- EFS provides file-level encryption for NTFS volumes.
- Regular permission reviews and least privilege improve enterprise security.
- Group-based permission assignment simplifies administration and auditing.

---

# Interview Questions

1. What is the difference between NTFS and share permissions?
2. What is a Security Descriptor?
3. Explain the difference between a DACL and a SACL.
4. What are effective permissions?
5. What is permission inheritance?
6. Why should Full Control be granted sparingly?
7. What does the `icacls` command do?
8. What is Encrypting File System (EFS)?
9. What is Access-Based Enumeration (ABE)?
10. How would you troubleshoot an "Access Denied" error on a shared folder?

---

# References

- Microsoft Learn
- Microsoft Windows Security Documentation
- Microsoft NTFS Documentation
- Microsoft File Services Documentation
- Microsoft `icacls` Documentation
- Microsoft Access Control Documentation
- CIS Microsoft Windows Benchmarks
- NIST SP 800-53 Security and Privacy Controls
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# Congratulations!

You have successfully completed **Chapter 9 – Windows Permissions and NTFS**.

You now understand how Windows authorizes access to files and folders using Security Descriptors, ACLs, ACEs, ownership, inheritance, effective permissions, share permissions, encryption, and auditing. These concepts are fundamental for Windows administration, cybersecurity operations, incident response, and enterprise identity management.

---
