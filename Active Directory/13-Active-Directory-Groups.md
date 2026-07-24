# Active-Directory/

# 13-Active-Directory-Groups.md

# Part 1 — Introduction to Active Directory Groups, Group Fundamentals, Scope, Types, Membership, and Enterprise Access Management

---

# Learning Objectives

After completing this part, you will be able to:

- Understand what Active Directory Groups are.
- Learn why groups exist.
- Understand group-based access management.
- Differentiate between Security and Distribution groups.
- Learn the concept of Group Scope.
- Understand enterprise access management principles.

---

# Introduction

Imagine an enterprise with:

- 250,000 employees
- 180,000 computers
- 8,000 servers
- 4,500 applications
- Millions of files

Without groups, administrators would have to assign permissions individually to every user.

Example:

```text
John

↓

Finance Folder

↓

Permission

Jane

↓

Finance Folder

↓

Permission

David

↓

Finance Folder

↓

Permission

...
```

Managing permissions this way becomes impractical.

Instead, Active Directory uses **Groups**.

---

# What is an Active Directory Group?

A **Group** is a collection of Active Directory objects that are managed as a single unit.

Objects that can belong to groups include:

- Users
- Computers
- Service Accounts
- Managed Service Accounts
- Other Groups (depending on scope rules)

Instead of assigning permissions directly to each object, permissions are assigned to the group.

---

# Why Groups Exist

Groups simplify administration.

Instead of:

```text
100 Users

↓

100 Individual Permissions
```

Use:

```text
100 Users

↓

Finance Group

↓

Single Permission Assignment
```

Benefits include:

- Easier administration
- Reduced errors
- Simplified auditing
- Faster onboarding
- Consistent permissions

---

# Enterprise Example

A company has:

```text
Finance Department

↓

500 Employees
```

Without groups:

```text
500 Permission Entries
```

With groups:

```text
Finance Users

↓

Single Permission Entry
```

When a new employee joins:

```text
Create User

↓

Add to Finance Group

↓

Access Granted
```

No individual permission changes are required.

---

# Active Directory Group Architecture

```text
Users

↓

Groups

↓

Permissions

↓

Resources
```

This model is the foundation of enterprise access control.

---

# Common Resources Protected by Groups

Groups commonly control access to:

- File Servers
- Network Shares
- Printers
- Databases
- Applications
- VPN
- Remote Desktop
- Microsoft SQL Server
- SharePoint
- Microsoft 365 resources
- Administrative tools

---

# Group Object

Like every AD object, a Group has:

- Name
- SID
- Distinguished Name
- Object GUID
- Attributes
- Members
- Scope
- Type

---

# Group Properties

Common properties include:

| Property | Description |
|----------|-------------|
| Name | Group name |
| Description | Purpose of group |
| Members | Objects in the group |
| Managed By | Responsible administrator |
| Group Scope | Domain Local, Global, Universal |
| Group Type | Security or Distribution |

---

# Group Membership

Example:

```text
Finance Users

│

├── John

├── Sarah

├── David

└── Anita
```

Permissions assigned to the group apply to its members, subject to applicable authorization rules.

---

# Group-Based Administration

Instead of:

```text
User

↓

Permission
```

Use:

```text
User

↓

Group

↓

Permission
```

This model scales efficiently.

---

# Group Types

There are two primary group types:

```text
Security Groups

Distribution Groups
```

---

# Security Groups

Security Groups are used for:

- Access Control
- NTFS Permissions
- Share Permissions
- Application Authorization
- Group Policy Filtering
- Administrative Delegation

Security Groups have SIDs and participate in authorization.

---

# Distribution Groups

Distribution Groups are used primarily for:

- Email Distribution
- Mailing Lists

Examples:

```text
All Finance Staff

HR Team

Marketing Team
```

Distribution Groups do **not** provide security permissions.

---

# Security vs Distribution

| Security Group | Distribution Group |
|---------------|--------------------|
| Access control | Email distribution |
| Has SID | No security authorization |
| Used for permissions | Used for communication |
| Can be used in ACLs | Cannot be used for ACLs |

---

# Group Scope

Every Security Group has a **scope**.

The three scopes are:

```text
Domain Local

Global

Universal
```

Scope determines:

- Where members can come from.
- Where permissions can be assigned.
- Where the group can be used.

---

# Why Group Scope Exists

Large enterprises may have:

```text
Forest

↓

Multiple Domains

↓

Thousands of Groups
```

Scope helps control replication, administration, and authorization.

---

# Group Scope Overview

```text
Groups

│

├── Domain Local

├── Global

└── Universal
```

Each scope has different membership and usage rules.

---

# Global Groups

Global Groups usually represent users with similar job functions from the **same domain**.

Example:

```text
Finance Users

HR Users

Developers

Helpdesk
```

Members are typically users and other eligible groups from the same domain.

---

# Enterprise Example

```text
Company

↓

Finance Department

↓

Finance Global Group
```

All Finance employees become members.

---

# Domain Local Groups

Domain Local Groups are commonly used to assign permissions to resources located within their domain.

Example:

```text
Finance File Server

↓

Finance Share

↓

Finance DL Group

↓

Permission Granted
```

---

# Universal Groups

Universal Groups are designed for organizations with multiple domains.

Example:

```text
India Finance

USA Finance

Germany Finance

↓

Global Groups

↓

Universal Finance

↓

Enterprise Resource
```

Universal Groups help consolidate membership across domains.

---

# Scope Comparison

| Scope | Typical Purpose |
|--------|-----------------|
| Global | Organize users by role within a domain |
| Domain Local | Assign permissions to resources |
| Universal | Combine members across domains |

Detailed membership rules will be covered later in this chapter.

---

# Nested Groups

Groups can contain other groups when permitted by scope rules.

Example:

```text
Finance Users

↓

Finance Managers

↓

Finance Executives
```

Nested groups simplify administration in large environments.

---

# Enterprise Access Model

A commonly used enterprise model is:

```text
Users

↓

Global Groups

↓

Domain Local Groups

↓

Resources
```

This approach separates identity management from permission assignment.

---

# Example

Instead of:

```text
John

↓

Finance Folder

↓

Read
```

Use:

```text
John

↓

Finance Global Group

↓

Finance Folder Access

↓

Finance Folder
```

When John changes departments:

```text
Remove

↓

Finance Group

↓

Add

↓

HR Group
```

Permissions adjust through group membership.

---

# Built-in Groups

Active Directory includes many predefined groups.

Examples:

- Domain Admins
- Enterprise Admins
- Schema Admins
- Backup Operators
- Print Operators
- Account Operators
- Server Operators
- Domain Users
- Domain Computers

These groups provide predefined administrative or operational capabilities.

---

# Group Naming Standards

Examples:

```text
GG_Finance

GG_HR

GG_IT
```

```text
DL_Finance_RW

DL_HR_Read

DL_IT_Admin
```

```text
UG_Global_Managers
```

Consistent naming improves administration and auditing.

---

# Best Practices

- Assign permissions to groups rather than users.
- Use descriptive group names.
- Avoid unnecessary nested groups.
- Document group ownership.
- Review memberships regularly.
- Remove obsolete groups.
- Follow least-privilege principles.

---

# Common Misconceptions

## Myth 1

> Permissions should be assigned directly to users.

**Reality:**

Permissions should generally be assigned to groups to simplify management.

---

## Myth 2

> Distribution Groups can secure resources.

**Reality:**

Distribution Groups are intended for communication, not authorization.

---

## Myth 3

> Every employee needs a unique permission assignment.

**Reality:**

Employees with similar responsibilities should typically inherit access through shared group membership.

---

# Cybersecurity Perspective

Groups are one of the most important security mechanisms in Active Directory.

Security teams should:

- Audit privileged groups.
- Monitor membership changes.
- Remove inactive members.
- Review administrative groups regularly.
- Limit nested administrative groups.
- Follow least-privilege access principles.

Compromise of a privileged group can significantly impact an enterprise.

---

# Hands-on Lab

## Objective

Explore Active Directory Groups.

### Tasks

1. Open:

```text
Active Directory Users and Computers
```

2. Browse:

- Built-in Groups
- Domain Users
- Domain Computers
- Administrative Groups

3. Create:

```text
GG_Finance
```

4. Create:

```text
DL_Finance_RW
```

5. Add:

- Two users to the Global Group.

6. View:

- Group properties
- Members
- Managed By
- Group Scope
- Group Type

---

# Key Takeaways

- Groups simplify administration and access management.
- Security Groups control authorization.
- Distribution Groups support communication.
- Group Scope determines how groups are used.
- Group-based permissions are the enterprise standard.

---

# Interview Questions

1. What is an Active Directory Group?
2. Why are groups preferred over direct permissions?
3. What is the difference between Security and Distribution Groups?
4. What is Group Scope?
5. Name the three group scopes.
6. What is a Global Group typically used for?
7. What is a Domain Local Group typically used for?
8. What is a Universal Group?
9. Why are nested groups useful?
10. Why should privileged group membership be audited?

---

# References

- Microsoft Learn – Active Directory Groups
- Microsoft Learn – Group Scope
- Microsoft Learn – Security Groups
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 2 — Group Scope Rules, AGDLP, AGUDLP, Nested Groups, Membership Rules, and Enterprise Access Design**