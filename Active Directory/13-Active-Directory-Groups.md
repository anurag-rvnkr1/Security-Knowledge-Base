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

# Active-Directory/

# 13-Active-Directory-Groups.md

# Part 2 — Group Scope Rules, AGDLP, AGUDLP, Nested Groups, Membership Rules, and Enterprise Access Design

---

# Learning Objectives

After completing this part, you will be able to:

- Understand Group Scope rules in detail.
- Learn membership rules for each group scope.
- Understand nested groups.
- Learn AGDLP and AGUDLP access models.
- Design scalable enterprise access management.
- Avoid common group design mistakes.

---

# Review

In Part 1, we learned:

- What Active Directory Groups are
- Security vs Distribution Groups
- Global Groups
- Domain Local Groups
- Universal Groups
- Group-based administration

Now we'll study **how these groups work together in enterprise environments.**

---

# Why Group Scope Rules Exist

Imagine an enterprise with:

- 30 Domains
- 250,000 Users
- Thousands of Servers
- Millions of Objects

Without scope rules:

- Replication would increase significantly.
- Administration would become difficult.
- Permission management would become inconsistent.

Microsoft introduced **Group Scope** to improve scalability and organization.

---

# The Three Group Scopes

```text
Groups

│

├── Global

├── Domain Local

└── Universal
```

Each has different:

- Membership rules
- Permission scope
- Replication behavior
- Enterprise use cases

---

# Global Group

A **Global Group (GG)** typically represents users performing the same job function within a single domain.

Example:

```text
Finance Users

HR Users

Developers

Helpdesk
```

---

# Global Group Membership

Global Groups can contain:

- User accounts
- Computer accounts
- Managed Service Accounts
- Other Global Groups (from the same domain)

Example:

```text
Finance Users

│

├── John

├── Anita

├── Sarah

└── Finance Interns (GG)
```

---

# Global Group Permissions

Permissions assigned to a Global Group can be granted on resources:

- Within the same domain
- In trusted domains
- Anywhere the group is recognized through trust relationships

This makes Global Groups ideal for representing **business roles**.

---

# Enterprise Example

```text
Finance Employees

↓

GG_Finance

↓

Business Identity
```

No resource permissions are assigned directly to users.

---

# Domain Local Group

A **Domain Local Group (DL)** is generally used to assign permissions to resources located in its own domain.

Example:

```text
Finance File Server

↓

DL_Finance_RW

↓

Read / Write Permission
```

---

# Domain Local Membership

A Domain Local Group may contain:

- Users
- Computers
- Global Groups
- Universal Groups
- Other Domain Local Groups (from the same domain)

Example:

```text
DL_Finance_RW

│

├── GG_Finance

├── GG_Managers

└── UG_GlobalFinance
```

---

# Domain Local Permissions

A Domain Local Group is commonly granted permissions on:

- NTFS folders
- File shares
- Printers
- Applications
- Servers

located **within its domain**.

---

# Universal Group

Universal Groups are designed for **multi-domain forests**.

Example:

```text
Company

├── India Domain

├── USA Domain

└── Germany Domain
```

Each domain has its own Finance group.

---

# Universal Group Example

```text
GG_Finance_India

GG_Finance_USA

GG_Finance_Germany

↓

UG_GlobalFinance
```

The Universal Group provides a single enterprise-wide representation.

---

# Universal Group Membership

Universal Groups may contain:

- Users
- Computers
- Global Groups
- Other Universal Groups

from any domain within the forest.

---

# Universal Group Permissions

Universal Groups can be granted permissions wherever appropriate across trusted domains.

They are often used as an intermediate layer in multi-domain environments.

---

# Group Scope Comparison

| Scope | Represents | Typical Usage |
|--------|------------|---------------|
| Global | Business role | User organization |
| Domain Local | Resource access | Permission assignment |
| Universal | Cross-domain organization | Enterprise-wide grouping |

---

# Visualizing the Three Scopes

```text
Users

↓

Global Group

↓

Universal Group

↓

Domain Local Group

↓

Resource
```

---

# Nested Groups

A **nested group** is a group that contains another group as a member.

Example:

```text
GG_IT

↓

UG_IT

↓

DL_IT_Admin

↓

File Server
```

Nested groups reduce administrative effort by avoiding repeated individual assignments.

---

# Why Nest Groups?

Without nesting:

```text
500 Users

↓

500 Permission Entries
```

With nesting:

```text
500 Users

↓

One Global Group

↓

One Permission Assignment
```

This approach is significantly easier to maintain.

---

# AGDLP Model

The most common access model in a **single-domain** environment is:

```text
Accounts

↓

Global Groups

↓

Domain Local Groups

↓

Permissions
```

Abbreviation:

```text
A → G → DL → P
```

---

# AGDLP Example

Finance Department:

```text
John

Sarah

David

↓

GG_Finance

↓

DL_Finance_RW

↓

Finance Share
```

Permission exists only on the Domain Local Group.

---

# Why AGDLP?

Advantages:

- Easy onboarding
- Easy offboarding
- Centralized permission management
- Reduced ACL complexity
- Easier auditing

---

# AGUDLP Model

For **multiple-domain forests**, Microsoft recommends:

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

Abbreviation:

```text
A → G → U → DL → P
```

---

# AGUDLP Example

```text
India Users

↓

GG_India_Finance

↓

UG_GlobalFinance

↓

DL_Finance_RW

↓

Finance Share
```

Similarly:

```text
USA Users

↓

GG_USA_Finance

↓

UG_GlobalFinance
```

All members receive consistent access through the same Universal Group.

---

# Enterprise Access Architecture

```text
Employees

↓

Global Groups

↓

Universal Groups

↓

Domain Local Groups

↓

Resources
```

This architecture separates:

- Identity
- Organization
- Authorization

---

# Resource-Centric Design

Instead of:

```text
Users

↓

Permissions
```

Use:

```text
Users

↓

Role Groups

↓

Resource Groups

↓

Permissions
```

This greatly simplifies permission administration.

---

# Access Change Example

Employee transfers:

```text
Finance

↓

HR
```

Administrator only changes:

```text
Remove

↓

GG_Finance

Add

↓

GG_HR
```

All resource permissions adjust automatically through group nesting.

---

# Membership Rules Summary

| Group Scope | Common Members | Typical Purpose |
|--------------|----------------|-----------------|
| Global | Users, Computers, Global Groups (same domain) | Organize identities |
| Universal | Users, Computers, Global Groups, Universal Groups | Cross-domain organization |
| Domain Local | Users, Computers, Global Groups, Universal Groups, Domain Local Groups (same domain) | Resource permissions |

---

# Replication Considerations

Global Group membership:

```text
Primarily relevant within the originating domain.
```

Universal Group membership:

```text
Replicated across the Global Catalog to support forest-wide access decisions.
```

Because of this, administrators should avoid unnecessary changes to Universal Group membership in very large environments.

---

# Common Enterprise Design

```text
Human Resources

↓

HR Users

↓

GG_HR

↓

DL_HR_RW

↓

HR File Server
```

The file server only recognizes the Domain Local Group.

---

# Common Administrative Mistakes

Avoid:

- Assigning permissions directly to users.
- Using Universal Groups when Global Groups are sufficient.
- Creating unnecessary nested groups.
- Mixing business roles and resource permissions in the same group.
- Using inconsistent naming standards.

---

# Best Practices

- Represent job roles with Global Groups.
- Assign permissions through Domain Local Groups.
- Use Universal Groups only when cross-domain grouping is required.
- Document group ownership.
- Review memberships regularly.
- Keep nesting simple and intentional.
- Follow AGDLP or AGUDLP consistently.

---

# Cybersecurity Perspective

Improper group design can lead to:

- Excessive permissions
- Privilege creep
- Difficult audits
- Hidden privilege escalation paths

Security teams should:

- Audit nested administrative groups.
- Review privileged memberships frequently.
- Remove obsolete groups.
- Monitor group membership changes.
- Apply least privilege using role-based groups.

---

# Hands-on Lab

## Objective

Design enterprise group nesting.

### Tasks

1. Create:

```text
GG_Finance
```

2. Create:

```text
DL_Finance_RW
```

3. Add:

```text
GG_Finance

↓

DL_Finance_RW
```

4. Assign:

```text
DL_Finance_RW

↓

Finance Folder

↓

Modify Permission
```

5. Add a test user to:

```text
GG_Finance
```

6. Verify that the user receives access through group membership.

7. Draw both:

- AGDLP model
- AGUDLP model

for a multi-domain organization.

---

# Key Takeaways

- Group Scope determines membership and usage.
- Global Groups typically represent business roles.
- Domain Local Groups typically receive permissions.
- Universal Groups simplify cross-domain administration.
- AGDLP and AGUDLP are proven enterprise access models.
- Nested groups reduce administrative overhead and improve scalability.

---

# Interview Questions

1. What is the purpose of Group Scope?
2. What is a Global Group used for?
3. What is a Domain Local Group used for?
4. When should a Universal Group be used?
5. What is a nested group?
6. Explain the AGDLP model.
7. Explain the AGUDLP model.
8. Why should permissions generally be assigned to Domain Local Groups?
9. Why should unnecessary Universal Groups be avoided?
10. How do nested groups improve enterprise administration?

---

# References

- Microsoft Learn – Active Directory Group Scope
- Microsoft Learn – Security Groups
- Microsoft Learn – Access Control in Active Directory
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 3 — Built-in Groups, Administrative Groups, Token Generation, SID History, PowerShell Management, Troubleshooting, and Enterprise Operations**