# 16-Active-Directory-Administration.md

# Part 1 — Introduction to Active Directory Administration, Administrative Tools, RSAT, ADUC and Administrative Center

---

# Learning Objectives

After completing this part, you will understand:

- What Active Directory Administration is
- Responsibilities of an Active Directory Administrator
- Administrative Roles
- Administrative Interfaces
- Remote Server Administration Tools (RSAT)
- Active Directory Users and Computers (ADUC)
- Active Directory Administrative Center (ADAC)
- MMC Snap-ins
- Server Manager
- Enterprise Administrative Workflow

---

# Introduction

Active Directory (AD) Administration is the process of managing and maintaining an organization's identity infrastructure.

An Active Directory Administrator is responsible for ensuring that:

- Users can authenticate successfully.
- Computers can join the domain.
- Group Policies are applied correctly.
- Security policies are enforced.
- Directory services remain available.
- Identity information remains accurate.
- Administrative changes follow organizational policies.

In small organizations, one administrator may manage the entire environment, whereas large enterprises often have specialized teams for identity management, security, infrastructure, and operations.

---

# What is Active Directory Administration?

Active Directory Administration involves creating, maintaining, securing, and monitoring directory objects and services.

Typical administrative responsibilities include:

- Creating users
- Managing passwords
- Managing computers
- Creating Organizational Units (OUs)
- Managing Groups
- Configuring Group Policies
- Managing Domain Controllers
- Monitoring replication
- Delegating administrative rights
- Auditing directory changes

---

# Enterprise Administration Overview

```
                Active Directory

                       │

      ┌────────────────┼────────────────┐

      ▼                ▼                ▼

 Identity         Infrastructure      Security

      ▼                ▼                ▼

 Users          Domain Controllers    Auditing

 Groups          DNS Services         Monitoring

 Computers       Replication          Compliance

 OUs             Trusts               Incident Response
```

---

# Why Proper Administration Matters

Poor administration can lead to:

- Authentication failures
- Security incidents
- Unauthorized privilege escalation
- Incorrect permissions
- Replication failures
- Service outages
- Compliance violations

Proper administration improves:

- Availability
- Security
- Reliability
- Compliance
- Operational efficiency

---

# Role of an Active Directory Administrator

An AD Administrator commonly performs:

```
Morning

↓

Review Alerts

↓

Verify Domain Health

↓

Process User Requests

↓

Create Users

↓

Reset Passwords

↓

Manage Groups

↓

Review Event Logs

↓

Document Changes
```

Administration is a continuous operational process rather than a one-time task.

---

# Administrative Responsibilities

Daily responsibilities often include:

- Unlocking user accounts
- Password resets
- Creating new users
- Disabling departed employee accounts
- Managing security groups
- Joining computers to the domain
- Troubleshooting authentication
- Reviewing replication status
- Monitoring Domain Controllers
- Reviewing security events

---

# Enterprise Administrative Teams

Large organizations commonly separate responsibilities.

Example:

| Team | Primary Responsibility |
|------|-------------------------|
| Identity Team | User and Group Management |
| Infrastructure Team | Domain Controllers and Services |
| Security Team | Auditing and Monitoring |
| Messaging Team | Exchange Integration |
| Endpoint Team | Workstations and Device Management |
| Service Desk | First-level User Support |

This separation reduces operational risk and supports the Principle of Least Privilege.

---

# Administrative Roles

Common administrative roles include:

- Domain Administrator
- Enterprise Administrator
- Schema Administrator
- DNS Administrator
- PKI Administrator
- Help Desk Administrator
- Server Administrator
- Security Administrator

Each role should have clearly defined responsibilities.

---

# Administrative Principle

```
Minimal Access

↓

Specific Role

↓

Specific Task

↓

Temporary Access (when applicable)

↓

Audit

↓

Review
```

Administrators should receive only the permissions required to perform their assigned duties.

---

# Administrative Interfaces

Windows provides multiple interfaces for Active Directory administration.

Common tools include:

- Server Manager
- MMC
- Active Directory Users and Computers
- Active Directory Administrative Center
- PowerShell
- Windows Admin Center (where deployed)

Each tool serves different administrative scenarios.

---

# Server Manager

Server Manager is the central management console for Windows Server.

Administrators use it to:

- Add Roles
- Remove Roles
- Install Features
- Monitor Server Status
- Manage Services
- Access Administrative Tools

Example:

```
Server Manager

├── Dashboard

├── Local Server

├── AD DS

├── DNS

├── File Services

├── Events

└── Performance
```

---

# Microsoft Management Console (MMC)

Many administrative tools are delivered as MMC snap-ins.

```
MMC

│

├── ADUC

├── DNS

├── DHCP

├── Sites and Services

├── Domains and Trusts

└── Certificate Authority
```

Administrators can combine multiple snap-ins into a custom console.

---

# Benefits of MMC

- Centralized administration
- Custom console creation
- Remote management
- Consistent interface
- Multiple snap-ins in one workspace

---

# Remote Server Administration Tools (RSAT)

RSAT allows administrators to manage Windows Server roles remotely from supported Windows client systems.

Instead of logging into every server:

```
Administrator PC

↓

RSAT

↓

Remote Domain Controller

↓

Manage Active Directory
```

This improves operational efficiency and reduces unnecessary interactive logons to servers.

---

# Common RSAT Components

RSAT includes tools such as:

- Active Directory Users and Computers
- Active Directory Administrative Center
- DNS Manager
- DHCP Manager
- Group Policy Management
- Sites and Services
- Domains and Trusts
- Certificate Services tools

---

# Benefits of RSAT

- Remote administration
- Reduced server logons
- Centralized management
- Faster troubleshooting
- Improved administrator productivity

---

# Active Directory Users and Computers (ADUC)

ADUC is one of the most frequently used Active Directory management consoles.

Administrators use ADUC to:

- Create users
- Disable accounts
- Reset passwords
- Create groups
- Manage computers
- Create OUs
- Move objects
- Delegate control

---

# ADUC Layout

```
Active Directory
Users and Computers

├── Domain

│   ├── Built-in

│   ├── Computers

│   ├── Users

│   ├── Domain Controllers

│   └── Organizational Units
```

---

# Managing a User with ADUC

Typical workflow:

```
Open ADUC

↓

Locate User

↓

Open Properties

↓

Modify Attributes

↓

Apply Changes

↓

Replication

↓

Updated Across Domain
```

---

# Common User Properties

Administrators frequently modify:

- First Name
- Last Name
- Display Name
- User Logon Name
- Telephone Number
- Department
- Manager
- Office
- Email Address
- Group Membership

---

# Active Directory Administrative Center (ADAC)

ADAC is Microsoft's modern management interface for Active Directory.

It provides:

- Enhanced search
- PowerShell integration
- Fine-Grained Password Policy management
- Active Directory Recycle Bin management
- History navigation
- Task-based administration

---

# ADUC vs ADAC

| Feature | ADUC | ADAC |
|----------|------|------|
| Classic Interface | ✓ | No |
| Modern Interface | No | ✓ |
| PowerShell Integration | Limited | ✓ |
| Recycle Bin Management | Limited | ✓ |
| Fine-Grained Password Policy | Limited | ✓ |
| Advanced Navigation | Limited | ✓ |

Both tools remain valuable depending on the administrative task.

---

# Administrative Workflow Example

```
HR Requests New Employee

↓

Identity Team

↓

Create User

↓

Assign Groups

↓

Create Home Folder

↓

Apply Policies

↓

Notify Manager

↓

User Ready
```

---

# Enterprise Administration Example

Company:

```
Global Retail Ltd.
```

Infrastructure:

- 35,000 Employees
- 22 Domain Controllers
- 14 Regional Offices
- Hybrid Identity

Daily administration includes:

- 120 New User Requests
- 90 Password Resets
- 70 Group Membership Changes
- 25 Computer Joins
- Continuous Domain Health Monitoring

Administration is divided among specialized teams with documented approval workflows.

---

# Administrative Documentation

Every organization should document:

- Naming conventions
- OU structure
- Group standards
- Administrative roles
- Change procedures
- Emergency contacts
- Recovery procedures
- Delegation model

Documentation reduces operational errors and improves consistency.

---

# Cybersecurity Perspective

Administrative accounts are among the most valuable assets in an Active Directory environment.

Security teams should:

- Use separate administrative accounts.
- Avoid performing administrative work from standard user accounts.
- Apply Multi-Factor Authentication where supported.
- Monitor privileged account activity.
- Audit administrative changes.
- Follow the Principle of Least Privilege.
- Review privileged group membership regularly.

Administrative convenience should never outweigh security requirements.

---

# Hands-on Lab

## Objective

Explore the primary Active Directory administrative tools.

### Step 1

Open:

```
Server Manager
```

Review installed roles and available management options.

---

### Step 2

Open:

```
Active Directory Users and Computers
```

Navigate through:

- Users
- Computers
- Domain Controllers
- Organizational Units

---

### Step 3

Open:

```
Active Directory Administrative Center
```

Compare its interface and available features with ADUC.

---

### Step 4

Launch:

```
mmc.exe
```

Add the following snap-ins:

- Active Directory Users and Computers
- DNS
- Group Policy Management

Save the custom console.

---

### Step 5

If RSAT is available, connect remotely to a lab domain controller and verify that administrative tools function correctly.

---

# Interview Questions

### Q1: What is the primary purpose of Active Directory Administration?

**Answer:** To manage users, computers, groups, Organizational Units, authentication services, and directory security while maintaining availability and compliance.

---

### Q2: What is RSAT?

**Answer:** Remote Server Administration Tools allow administrators to remotely manage Windows Server roles and Active Directory from supported Windows client systems.

---

### Q3: What is ADUC used for?

**Answer:** Active Directory Users and Computers is used to manage users, groups, computers, OUs, and many common Active Directory administrative tasks.

---

### Q4: What advantages does ADAC provide over ADUC?

**Answer:** ADAC includes a modern interface, integrated PowerShell support, Active Directory Recycle Bin management, enhanced search, and Fine-Grained Password Policy management.

---

### Q5: Why should administrative roles be separated?

**Answer:** Separation of duties reduces risk, limits privilege exposure, improves accountability, and supports security best practices.

---

### Q6: Why is documentation important in Active Directory administration?

**Answer:** It promotes consistency, simplifies troubleshooting, supports change management, and assists with disaster recovery and audits.

---

# Best Practices

- Use dedicated administrative accounts.
- Follow least-privilege principles.
- Use RSAT instead of logging directly onto servers whenever possible.
- Document all administrative changes.
- Standardize naming conventions.
- Review privileged group memberships regularly.
- Use ADAC for modern administrative features while maintaining familiarity with ADUC.

---

# Common Mistakes

- Performing administrative tasks using standard user accounts.
- Granting excessive privileges.
- Failing to document directory changes.
- Logging directly onto Domain Controllers for routine tasks.
- Ignoring administrative auditing.
- Maintaining inconsistent naming conventions across OUs and groups.

---

# Key Takeaways

- Active Directory administration is the operational foundation of identity management.
- Administrators use tools such as Server Manager, MMC, RSAT, ADUC, and ADAC to manage enterprise environments.
- Role separation, documentation, and least privilege improve both security and operational efficiency.
- Modern enterprise administration combines graphical tools with structured operational processes and security monitoring.

---

# 16-Active-Directory-Administration.md

# Part 2 — User Administration, Group Administration, Computer Administration, OU Management, Delegation of Control and Bulk Administration

---

# Learning Objectives

After completing this part, you will understand:

- User Administration
- Group Administration
- Computer Administration
- Organizational Unit (OU) Management
- Delegation of Control
- Account Lifecycle Management
- Bulk Administration
- Administrative Best Practices
- Enterprise User Provisioning

---

# Introduction

The majority of an Active Directory administrator's daily work revolves around managing directory objects.

The most commonly managed objects are:

- Users
- Groups
- Computers
- Organizational Units (OUs)

Efficient management of these objects ensures:

- Secure authentication
- Correct authorization
- Consistent policy application
- Simplified administration

---

# Active Directory Object Management

```
                 Active Directory

                       │

      ┌────────────────┼────────────────┐

      ▼                ▼                ▼

    Users           Groups         Computers

                       │

                       ▼

             Organizational Units

                       │

                       ▼

               Group Policy Applied
```

---

# User Administration

User administration includes managing the complete lifecycle of a user account.

Typical tasks include:

- Creating users
- Updating user information
- Resetting passwords
- Unlocking accounts
- Enabling accounts
- Disabling accounts
- Deleting accounts (where permitted)
- Restoring deleted accounts
- Managing group memberships

---

# User Account Lifecycle

```
Recruitment

↓

HR Approval

↓

User Created

↓

Account Enabled

↓

Assigned Groups

↓

Employee Active

↓

Role Change

↓

Group Updates

↓

Employee Leaves

↓

Disable Account

↓

Archive

↓

Delete (per policy)
```

User lifecycle management should follow organizational policies and retention requirements.

---

# Creating a User

When creating a user, administrators typically specify:

- First Name
- Last Name
- Display Name
- Username (UPN)
- SAM Account Name
- Initial Password
- Department
- Manager
- Office Location

Example:

```
New User

↓

Create Account

↓

Set Password

↓

Assign Groups

↓

Apply Policies

↓

Ready for Login
```

---

# Password Administration

Common password-related tasks include:

- Reset Password
- Force Password Change at Next Logon
- Unlock Account
- Verify Password Policy Compliance

Password resets should follow the organization's identity verification procedures.

---

# Account Lockout Management

A user account may become locked after repeated failed authentication attempts.

```
Incorrect Password

↓

Multiple Attempts

↓

Account Locked

↓

Administrator Verification

↓

Unlock Account
```

Before unlocking an account, administrators should verify the cause of the lockout.

---

# Disabling vs Deleting Users

| Action | Recommended Use |
|---------|-----------------|
| Disable Account | Temporary or departed employees |
| Delete Account | Permanent removal according to retention policy |

Many organizations disable accounts first and delete them only after the required retention period.

---

# Group Administration

Groups simplify permission management.

Instead of assigning permissions directly to individual users:

```
Users

↓

Security Group

↓

Permission

↓

Resource
```

This approach is easier to manage and audit.

---

# Types of Administrative Group Tasks

Administrators commonly:

- Create groups
- Rename groups
- Delete groups
- Add members
- Remove members
- Review memberships
- Assign permissions (outside AD where applicable)

---

# Group Membership Workflow

```
New Employee

↓

Department

↓

Add to Security Groups

↓

Inherited Permissions

↓

Resource Access
```

Proper group assignment enables users to access only the resources they need.

---

# Nested Groups

Large enterprises often use nested groups.

Example:

```
Finance Users

↓

Finance Managers

↓

Finance Executives

↓

Access Sensitive Reports
```

Nested groups simplify permission management but should be documented to avoid unnecessary complexity.

---

# Computer Administration

Computers are also Active Directory objects.

Administrators commonly:

- Join computers to the domain
- Move computers to OUs
- Rename computers
- Disable computer accounts
- Remove inactive computer accounts
- Verify Group Policy application

---

# Computer Lifecycle

```
New Computer

↓

Domain Join

↓

Move to Correct OU

↓

Receive Group Policies

↓

Operational

↓

Retired

↓

Disable

↓

Remove
```

---

# Joining a Computer to the Domain

Typical process:

```
Install Windows

↓

Configure Network

↓

Join Domain

↓

Restart

↓

Receive Group Policy

↓

Ready for Users
```

---

# Computer Naming Standards

Organizations typically adopt naming conventions.

Example:

```
BLR-LAP-0001

NYC-SRV-0205

LON-DC-001
```

Benefits include:

- Easier inventory management
- Faster troubleshooting
- Consistent documentation

---

# Organizational Unit (OU) Administration

Organizational Units organize Active Directory objects logically.

Administrators use OUs to:

- Separate departments
- Delegate administration
- Apply Group Policy
- Simplify management

---

# Example OU Structure

```
Company

├── HR

├── Finance

├── IT

├── Sales

├── Servers

├── Workstations

└── Service Accounts
```

---

# Moving Objects Between OUs

Example:

```
Employee Transfers

↓

Sales

↓

Marketing

↓

Move User

↓

New Policies Applied
```

Moving objects between OUs can affect Group Policy processing.

---

# Delegation of Control

Delegation allows limited administrative rights without granting Domain Administrator privileges.

Example:

```
Domain Admin

↓

Delegate

↓

Help Desk

↓

Reset Passwords

↓

Unlock Accounts
```

This supports least-privilege administration.

---

# Benefits of Delegation

- Reduced administrative workload
- Better separation of duties
- Improved security
- Clear accountability
- Reduced privilege exposure

---

# Delegation Example

Help Desk permissions:

```
✓ Reset Password

✓ Unlock Account

✓ Read User Information

✗ Delete User

✗ Modify Groups

✗ Domain Administration
```

The Help Desk receives only the permissions necessary for its responsibilities.

---

# Bulk Administration

Large organizations rarely manage users one at a time.

Instead, administrators perform bulk operations.

Examples:

- Create multiple users
- Disable multiple accounts
- Update departments
- Modify phone numbers
- Change managers
- Import new employees

---

# Bulk Administration Workflow

```
HR Employee List

↓

CSV File

↓

Administrative Tool

↓

Multiple User Accounts

↓

Verification

↓

Completed
```

Bulk operations reduce manual effort and improve consistency.

---

# User Provisioning Process

```
HR System

↓

Approval

↓

Identity Team

↓

Create User

↓

Assign License

↓

Assign Groups

↓

Apply Policies

↓

Notify Manager
```

Provisioning is often integrated with identity governance solutions in enterprise environments.

---

# Offboarding Process

Proper offboarding is critical for security.

```
Employee Departure

↓

Disable Account

↓

Revoke Access

↓

Remove Group Memberships

↓

Archive Data

↓

Delete per Policy
```

Timely account deactivation reduces the risk of unauthorized access.

---

# Enterprise Administration Example

Company:

```
Northwind Manufacturing
```

Daily Operations:

- 150 New Users
- 80 Password Resets
- 120 Group Membership Changes
- 60 Computer Joins
- 40 Employee Transfers
- 25 Offboarding Requests

To manage this scale:

- Delegation is used for Help Desk tasks.
- Standardized naming conventions are enforced.
- Bulk provisioning processes reduce manual work.
- Administrative actions are logged and reviewed.

---

# Administrative Documentation

Maintain documentation for:

- Naming conventions
- Group ownership
- OU hierarchy
- Delegated permissions
- Provisioning procedures
- Offboarding procedures
- Approval workflows

Documentation supports consistency and audit readiness.

---

# Cybersecurity Perspective

Identity administration has a direct impact on enterprise security.

Security teams should:

- Disable accounts immediately after employee departure.
- Review inactive accounts regularly.
- Avoid assigning permissions directly to users where groups are more appropriate.
- Audit delegated permissions.
- Monitor privileged group membership changes.
- Periodically review stale computer accounts and unused groups.

Strong identity governance reduces the attack surface and improves accountability.

---

# Hands-on Lab

## Objective

Perform common Active Directory administrative tasks in a lab environment.

### Step 1

Using **Active Directory Users and Computers (ADUC)**:

- Create a test user.
- Populate common user attributes.

---

### Step 2

Create:

- A Security Group
- An Organizational Unit

Add the test user to the new group.

---

### Step 3

Create a test computer account.

Move it into a workstation OU.

---

### Step 4

Delegate password reset permissions for a Help Desk OU to a designated administrative group.

Review the delegated permissions.

---

### Step 5

Document:

- User naming standard
- Computer naming standard
- Group naming standard
- OU hierarchy

---

# Interview Questions

### Q1: Why are groups preferred over assigning permissions directly to users?

**Answer:** Groups simplify permission management, improve scalability, and make auditing easier by assigning permissions once to the group rather than individually to each user.

---

### Q2: What is the benefit of Organizational Units?

**Answer:** OUs organize objects logically, support Group Policy application, and allow delegation of administrative tasks.

---

### Q3: What is delegation of control?

**Answer:** Delegation allows administrators to grant specific administrative permissions to selected users or groups without providing full Domain Administrator privileges.

---

### Q4: Why should accounts typically be disabled before deletion?

**Answer:** Disabling preserves the account for investigation, recovery, or retention requirements while immediately preventing sign-in.

---

### Q5: What is the advantage of bulk administration?

**Answer:** Bulk administration improves efficiency, reduces manual errors, and enables consistent management of large numbers of Active Directory objects.

---

### Q6: Why should offboarding be performed promptly?

**Answer:** Prompt offboarding prevents former employees from retaining access to organizational resources and reduces security risk.

---

# Best Practices

- Standardize naming conventions.
- Use groups to assign permissions.
- Delegate routine administration using least privilege.
- Document all administrative procedures.
- Review inactive users and computers regularly.
- Follow documented onboarding and offboarding workflows.
- Periodically audit delegated permissions.

---

# Common Mistakes

- Assigning permissions directly to individual users.
- Deleting accounts immediately instead of following retention policies.
- Using inconsistent naming conventions.
- Granting excessive delegated permissions.
- Leaving inactive computer accounts enabled.
- Failing to document administrative changes.

---

# Key Takeaways

- User, group, computer, and OU management form the core of daily Active Directory administration.
- Delegation enables secure distribution of administrative responsibilities.
- Bulk administration improves efficiency in large environments.
- Well-defined provisioning and offboarding processes strengthen both operational efficiency and security.
- Consistent documentation and least-privilege administration are essential for enterprise identity management.

---

**Next:** Part 3