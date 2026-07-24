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

# 12-Active-Directory-Users-and-Computers.md

# Part 2 — User Account Management, Computer Account Management, Account Properties, Password Policies, and Enterprise Administration

---

# Learning Objectives

After completing this part, you will be able to:

- Create and manage user accounts.
- Create and manage computer accounts.
- Understand user account properties.
- Learn account lifecycle management.
- Understand password-related account settings.
- Apply enterprise administration best practices.

---

# Review

From Part 1:

We learned:

- ADUC overview
- Active Directory objects
- User objects
- Computer objects
- SID
- Distinguished Name
- Object GUID

Now we'll focus on **day-to-day administration** performed by Active Directory administrators.

---

# User Account Creation

Typical workflow:

```text
HR

↓

New Employee

↓

IT Receives Request

↓

Create User

↓

Assign Groups

↓

Set Password

↓

Provide Access
```

---

# Creating a User in ADUC

Steps:

```text
Right Click OU

↓

New

↓

User

↓

Enter Details

↓

Set Password

↓

Finish
```

---

# Required Information

Common fields:

- First Name
- Last Name
- Full Name
- User Logon Name (UPN)
- sAMAccountName (legacy logon)
- Initial Password

Example:

```text
Name

↓

John Smith

↓

UPN

↓

john.smith@company.com
```

---

# User Properties

Right-click a user:

```text
Properties
```

Common tabs include:

- General
- Address
- Account
- Profile
- Organization
- Member Of
- Security (Advanced Features)
- Attribute Editor (Advanced Features)

---

# General Tab

Contains:

- Display Name
- Description
- Office
- Telephone
- Email
- Web Page

Useful for contact information and directory searches.

---

# Organization Tab

Stores business information:

- Job Title
- Department
- Company
- Manager

Example:

```text
Department

↓

Finance
```

---

# Member Of Tab

Displays security and distribution group memberships.

Example:

```text
Domain Users

Finance Users

VPN Users
```

Group membership determines many of the user's permissions.

---

# Account Tab

One of the most important administrative tabs.

Contains:

- User logon name
- Logon hours
- Logon workstations
- Account options
- Account expiration
- Unlock account (when applicable)

---

# Password Options

Common options:

```text
User Must Change Password

Password Never Expires

Store Password Using Reversible Encryption

Smart Card Required

Account Is Sensitive and Cannot Be Delegated
```

Not every option should be used routinely; apply settings based on business and security requirements.

---

# Account Expiration

Useful for:

- Contractors
- Temporary employees
- Interns
- Consultants

Example:

```text
Start

↓

July 1

↓

Expires

↓

December 31
```

After expiration, the account cannot authenticate until re-enabled or extended.

---

# Disable vs Delete

Disable:

```text
Account

↓

Cannot Log In

↓

Object Preserved
```

Delete:

```text
Object

↓

Removed
```

Enterprise environments commonly disable accounts first, then delete them according to retention policies.

---

# Unlocking Accounts

If a user exceeds the configured account lockout threshold:

```text
Account Locked

↓

Administrator

↓

Unlock Account

↓

User Signs In
```

Always investigate repeated lockouts to determine the root cause.

---

# Password Reset

Workflow:

```text
Helpdesk

↓

Reset Password

↓

Temporary Password

↓

User Changes Password
```

This is one of the most common delegated administrative tasks.

---

# User Rename

Example:

```text
Mary Johnson

↓

Mary Brown
```

Administrators may update:

- Display Name
- UPN
- sAMAccountName (if required)
- Email address

The SID remains unchanged.

---

# Moving Users

Example:

Before:

```text
Sales OU
```

After:

```text
Marketing OU
```

Effects:

- Distinguished Name changes.
- Different delegated administrators may manage the account.
- Different Group Policies may apply.

---

# Copying Users

ADUC allows administrators to copy an existing user.

Useful because:

- Group memberships
- Basic properties
- Organizational settings

can be reused for similar roles.

Example:

```text
New Finance Employee

↓

Copy Existing Finance User

↓

Modify Name

↓

Complete
```

---

# User Lifecycle

```text
Recruitment

↓

Account Creation

↓

Daily Administration

↓

Department Transfer

↓

Promotion

↓

Disable

↓

Delete
```

Lifecycle management is essential for security and compliance.

---

# Computer Account Management

Computer accounts are administered similarly.

Tasks include:

- Create
- Move
- Rename
- Disable
- Delete
- Reset account

---

# Joining a Domain

Workflow:

```text
Computer

↓

Domain Join

↓

Computer Account Created

↓

Restart

↓

Authentication Ready
```

A secure channel is established between the computer and the domain.

---

# Reset Computer Account

Sometimes a computer loses its secure channel with the domain.

Example causes:

- Restoring an old virtual machine snapshot
- Extended offline periods
- Domain trust issues
- Improper cloning

Administrator:

```text
Reset Computer Account

↓

Rejoin Domain (if required)

↓

Authentication Restored
```

---

# Disable Computer Account

Useful when:

- Device is stolen
- Device retired
- Device under investigation
- Device temporarily removed from service

Disabling prevents the computer from authenticating to the domain.

---

# Delete Computer Account

Delete only after confirming:

- Device is permanently retired.
- No dependencies remain.
- Organizational retention requirements are satisfied.

---

# Logon Hours

Administrators can restrict when a user may log on.

Example:

```text
Monday–Friday

08:00–18:00
```

Outside these hours:

```text
Authentication Denied
```

This feature is useful for specific operational requirements.

---

# Logon Workstations

Administrators can restrict which computers a user may use.

Example:

```text
Allowed

↓

HR-PC-01

HR-PC-02
```

Attempting to log on elsewhere is denied.

---

# Enterprise Example

Organization:

```text
50,000 Users

↓

Automated Provisioning

↓

Correct OU

↓

Correct Groups

↓

Correct Policies
```

Automation ensures consistency across large environments.

---

# Administrative Workflow

```text
Create User

↓

Assign Groups

↓

Move to OU

↓

Apply Policies

↓

Grant Application Access

↓

Audit
```

---

# PowerShell Management

The **ActiveDirectory** PowerShell module supports automation.

---

# Create User

```powershell
New-ADUser `
-Name "John Smith" `
-SamAccountName "jsmith" `
-UserPrincipalName "john.smith@company.com"
```

---

# Get User

```powershell
Get-ADUser `
-Identity jsmith
```

---

# Disable User

```powershell
Disable-ADAccount `
-Identity jsmith
```

---

# Enable User

```powershell
Enable-ADAccount `
-Identity jsmith
```

---

# Unlock User

```powershell
Unlock-ADAccount `
-Identity jsmith
```

---

# Reset Password

```powershell
Set-ADAccountPassword
```

Typically used with a secure string containing the new password.

---

# Create Computer

```powershell
New-ADComputer `
-Name "BLR-PC-101"
```

---

# Disable Computer

```powershell
Disable-ADAccount `
-Identity "BLR-PC-101$"
```

---

# Troubleshooting User Issues

Common issues:

- Incorrect password
- Locked account
- Disabled account
- Expired account
- Missing group membership
- Wrong OU
- Replication delays

---

# Troubleshooting Workflow

```text
User Cannot Log In

↓

Account Enabled?

↓

Password Correct?

↓

Locked?

↓

Expired?

↓

Correct Group Membership?

↓

Resolved
```

---

# Enterprise Best Practices

- Use standardized account naming.
- Populate business attributes.
- Assign access through groups rather than directly.
- Review inactive accounts regularly.
- Disable accounts promptly when users leave.
- Automate provisioning wherever possible.
- Audit administrative actions.

---

# Common Administrative Mistakes

Avoid:

- Deleting accounts immediately after employee departure.
- Granting permissions directly to users instead of groups.
- Leaving inactive accounts enabled.
- Using generic shared user accounts.
- Forgetting to update attributes after departmental changes.
- Ignoring account lockout investigations.

---

# Cybersecurity Perspective

Identity is a primary security boundary.

Recommendations:

- Enforce strong authentication policies.
- Review privileged accounts frequently.
- Monitor account creation and deletion.
- Audit password resets.
- Remove unnecessary privileges.
- Disable dormant accounts.
- Investigate repeated authentication failures.

---

# Hands-on Lab

## Objective

Manage user and computer accounts.

### Tasks

1. Open:

```text
Active Directory Users and Computers
```

2. Create:

- One user
- One computer account

3. Configure:

- Department
- Manager
- Group memberships
- Account expiration

4. Disable and re-enable the user.

5. Unlock a test account (if available).

6. Document:

- User properties
- Computer properties
- Lifecycle actions
- Security observations

---

# Key Takeaways

- ADUC is the primary tool for user and computer administration.
- User properties store identity, business, and security information.
- Group membership is central to authorization.
- Computer accounts authenticate just like user accounts.
- Proper lifecycle management improves security and compliance.

---

# Interview Questions

1. How do you create a user account in ADUC?
2. What information is stored on the Account tab?
3. What is the purpose of the Member Of tab?
4. What is the difference between disabling and deleting an account?
5. Why would you configure account expiration?
6. What happens when a computer joins a domain?
7. When should a computer account be reset?
8. Which PowerShell cmdlet creates a user?
9. Which cmdlet unlocks a locked account?
10. Why should permissions be assigned through groups instead of directly to users?

---

# References

- Microsoft Learn – Manage User Accounts
- Microsoft Learn – Manage Computer Accounts
- Microsoft Learn – ActiveDirectory PowerShell Module
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

# 12-Active-Directory-Users-and-Computers.md

# Part 3 — Advanced Object Management, Attribute Editor, Saved Queries, PowerShell Automation, Troubleshooting, and Enterprise Operations

---

# Learning Objectives

After completing this part, you will be able to:

- Perform advanced object management in ADUC.
- Understand the Attribute Editor.
- Use Saved Queries.
- Automate administration with PowerShell.
- Troubleshoot user and computer object issues.
- Apply enterprise operational best practices.

---

# Review

From previous parts:

We learned:

- ADUC fundamentals
- Active Directory objects
- User management
- Computer management
- Account lifecycle
- PowerShell basics

Now we'll focus on **advanced administration** performed in enterprise Active Directory environments.

---

# Advanced Features

Many administrative options are hidden by default.

Enable them:

```text
View

↓

Advanced Features
```

This exposes additional containers, tabs, and object properties.

---

# Benefits of Advanced Features

Enabling Advanced Features allows administrators to:

- View System containers
- Access Security tabs
- Open Attribute Editor
- View advanced object properties
- Perform detailed troubleshooting

---

# Attribute Editor

One of the most important administrative tools.

Found under:

```text
User Properties

↓

Attribute Editor
```

This tab displays nearly every LDAP attribute associated with an object.

---

# What are Attributes?

Every Active Directory object consists of attributes.

Example:

```text
User

↓

Display Name

↓

Department

↓

Manager

↓

Telephone

↓

SID

↓

ObjectGUID

↓

mail

↓

memberOf
```

---

# Common User Attributes

| LDAP Attribute | Description |
|---------------|-------------|
| cn | Common Name |
| displayName | Display Name |
| givenName | First Name |
| sn | Surname |
| mail | Email |
| department | Department |
| company | Company |
| title | Job Title |
| manager | Manager |
| telephoneNumber | Phone Number |

---

# Security Attributes

Important security-related attributes include:

| Attribute | Purpose |
|-----------|----------|
| objectSID | Security Identifier |
| objectGUID | Permanent Object Identifier |
| userAccountControl | Account behavior flags |
| memberOf | Group membership |
| primaryGroupID | Primary group |
| lastLogonTimestamp | Approximate last logon replication attribute |

---

# UserAccountControl

The **userAccountControl** attribute stores account configuration using a bitmask.

Examples of account characteristics include:

- Account disabled
- Password not required
- Smart card required
- Password never expires
- Trusted for delegation

Administrators typically manage these settings through ADUC rather than editing the value directly.

---

# Distinguished Name Attribute

Example:

```text
CN=John Smith

OU=Finance

DC=company

DC=com
```

This attribute identifies the object's location within the directory hierarchy.

---

# Viewing Hidden Attributes

Attribute Editor exposes values not normally visible through standard property tabs.

Examples:

```text
lastLogonTimestamp

pwdLastSet

whenCreated

whenChanged

objectGUID
```

These are frequently used during troubleshooting and audits.

---

# Saved Queries

Large enterprises may contain:

- 200,000 users
- 50,000 computers
- Thousands of groups

Finding objects manually is inefficient.

ADUC provides:

> **Saved Queries**

---

# Saved Query Purpose

Saved Queries allow administrators to repeatedly search for objects matching specified criteria.

Examples:

- Disabled users
- Locked users
- Expired accounts
- Computers
- Service accounts

---

# Saved Query Example

```text
Users

↓

Department = Finance
```

Result:

```text
Only Finance Users
```

---

# Example Queries

```text
Disabled Accounts
```

```text
Locked Accounts
```

```text
Password Never Expires
```

```text
Inactive Computers
```

These queries simplify routine administrative tasks.

---

# Object Search

ADUC supports searching by:

- Name
- Description
- Email
- UPN
- Computer name
- Custom LDAP attributes (through advanced search capabilities)

---

# Find Feature

```text
Right Click Domain

↓

Find
```

Useful when locating:

- Users
- Computers
- Groups
- Contacts

---

# Object Movement

Objects can be moved between OUs.

Example:

Before:

```text
Sales OU
```

After:

```text
Marketing OU
```

Effects:

- Distinguished Name changes.
- Different Group Policies may apply.
- Delegated administration may change.

---

# Object Protection

Administrators can protect important objects from accidental deletion.

Example:

```text
Properties

↓

Object

↓

Protect Object from Accidental Deletion
```

This is commonly enabled for critical OUs and important administrative objects.

---

# Bulk Administration

Enterprise administrators rarely create accounts one at a time.

Typical workflow:

```text
HR System

↓

CSV File

↓

PowerShell

↓

Bulk User Creation
```

Automation reduces manual effort and configuration errors.

---

# PowerShell Automation

PowerShell provides powerful management capabilities.

---

# Find Users

```powershell
Get-ADUser `
-Filter *
```

---

# Find Computers

```powershell
Get-ADComputer `
-Filter *
```

---

# Find Disabled Users

```powershell
Search-ADAccount `
-AccountDisabled
```

---

# Find Locked Accounts

```powershell
Search-ADAccount `
-LockedOut
```

---

# Find Inactive Accounts

```powershell
Search-ADAccount `
-AccountInactive
```

---

# Move Object

```powershell
Move-ADObject
```

Used to move users, computers, groups, and other directory objects.

---

# Rename Object

```powershell
Rename-ADObject
```

Allows administrators to rename objects without recreating them.

---

# Remove Object

```powershell
Remove-ADUser
```

or

```powershell
Remove-ADComputer
```

Deletion should follow organizational retention and approval processes.

---

# Reporting

PowerShell can generate reports such as:

- Disabled users
- Expired accounts
- Password expiration status
- Group memberships
- Inactive computers
- Organizational summaries

---

# Enterprise Example

Organization:

- 180,000 employees
- 95,000 computers

Automation:

```text
PowerShell

↓

HR Import

↓

Account Creation

↓

Group Assignment

↓

OU Placement

↓

Reporting
```

Benefits:

- Consistency
- Speed
- Reduced administrative effort

---

# Troubleshooting User Objects

Common issues:

- Missing attributes
- Incorrect department
- Wrong manager
- Missing email
- Incorrect group membership
- Wrong OU
- Replication delay

---

# Troubleshooting Computer Objects

Common issues:

- Secure channel problems
- Incorrect OU
- Missing Group Policy
- Disabled account
- Duplicate computer names
- Replication issues

---

# Troubleshooting Workflow

```text
Problem

↓

Object Exists?

↓

Correct OU?

↓

Correct Attributes?

↓

Correct Groups?

↓

Replication Healthy?

↓

Resolved
```

---

# Useful Administrative Tools

| Tool | Purpose |
|------|----------|
| ADUC | Object administration |
| PowerShell | Automation |
| Event Viewer | Event analysis |
| Active Directory Administrative Center (ADAC) | Modern administration |
| ADSI Edit | Advanced directory editing |
| LDP | LDAP troubleshooting |

---

# ADSI Edit

**ADSI Edit** provides low-level access to directory objects.

It allows administrators to:

- View attributes
- Edit directory objects
- Access naming contexts
- Troubleshoot advanced issues

Use ADSI Edit with caution because changes bypass many of the safeguards provided by ADUC.

---

# Active Directory Administrative Center (ADAC)

ADAC is a newer management interface that supports:

- Modern administration
- PowerShell integration
- Fine-Grained Password Policies
- Recycle Bin management
- Enhanced object management

Many enterprises use both ADUC and ADAC depending on the task.

---

# Best Practices

- Enable Advanced Features when performing advanced administration.
- Populate important user attributes consistently.
- Use Saved Queries for repetitive searches.
- Automate repetitive tasks with PowerShell.
- Protect critical objects from accidental deletion.
- Review inactive accounts regularly.
- Document administrative procedures.

---

# Common Administrative Mistakes

Avoid:

- Editing advanced attributes without understanding their purpose.
- Using ADSI Edit for routine administration.
- Ignoring missing business attributes.
- Performing large bulk changes without testing.
- Deleting objects instead of disabling them first.
- Leaving stale computer accounts in the directory.

---

# Cybersecurity Perspective

Directory objects are valuable security assets.

Security teams should:

- Audit object modifications.
- Review privileged accounts regularly.
- Monitor changes to critical attributes.
- Detect inactive accounts.
- Remove obsolete computer objects.
- Review delegated permissions.
- Protect administrative accounts from unauthorized modification.

---

# Hands-on Lab

## Objective

Practice advanced object management.

### Tasks

1. Enable:

```text
View

↓

Advanced Features
```

2. Open:

```text
Attribute Editor
```

3. Record:

- objectGUID
- objectSID
- Distinguished Name
- lastLogonTimestamp
- userAccountControl

4. Create:

```text
Saved Query

↓

Disabled Users
```

5. Run:

```powershell
Search-ADAccount -LockedOut
```

6. Generate:

- Disabled user report
- Computer inventory
- OU summary

---

# Key Takeaways

- Attribute Editor exposes detailed LDAP attributes.
- Saved Queries simplify enterprise administration.
- PowerShell enables large-scale automation.
- ADAC and ADSI Edit complement ADUC for advanced administration.
- Proper object management improves security and operational efficiency.

---

# Interview Questions

1. What does the Attribute Editor display?
2. What is the purpose of userAccountControl?
3. What are Saved Queries?
4. Which PowerShell cmdlet finds locked accounts?
5. What is ADSI Edit used for?
6. What is Active Directory Administrative Center (ADAC)?
7. Why should ADSI Edit be used carefully?
8. Which attribute uniquely identifies an object permanently?
9. Why is object protection important?
10. How does PowerShell improve enterprise administration?

---

# References

- Microsoft Learn – Active Directory Users and Computers
- Microsoft Learn – Active Directory Administrative Center
- Microsoft Learn – ActiveDirectory PowerShell Module
- Microsoft Learn – ADSI Edit
- Microsoft Windows Server Documentation
- Windows Internals
- Microsoft Security Best Practices

---

**Next:** **Part 4 — ADUC Security, Monitoring, Best Practices, Final Revision, Chapter Summary, and Interview Preparation**