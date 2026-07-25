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

**Next:** Part 2