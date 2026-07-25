# 18-AD-Security.md

# Part 1 — Introduction to Active Directory Security, Security Principles, Identity Protection and Administrative Security

---

# Learning Objectives

After completing this part, you will understand:

- Why Active Directory Security is Critical
- Active Directory Threat Landscape
- Identity as the New Security Perimeter
- CIA Triad in Active Directory
- Authentication vs Authorization
- Principle of Least Privilege
- Administrative Tiering
- Privileged Accounts
- Secure Administrative Workstations (SAWs/PAWs)
- Security Baselines
- Enterprise Security Model

---

# Introduction

Active Directory is often called the **heart of a Windows enterprise** because it stores and manages:

- User identities
- Computer identities
- Authentication
- Authorization
- Group memberships
- Organizational Units
- Trust relationships
- Group Policies
- Service Accounts

If an attacker gains control of Active Directory, they can often gain control of the entire Windows environment.

Therefore, securing Active Directory is one of the highest priorities for enterprise defenders.

---

# Why Active Directory is a High-Value Target

Almost every business-critical system depends on Active Directory.

```
Employees

        │

        ▼

Active Directory

        │

 ┌──────┼───────────────┐

 ▼      ▼               ▼

Email  File Servers   Business Apps

        ▼

Databases

        ▼

Cloud Services

        ▼

Production Systems
```

Compromising Active Directory may allow unauthorized access to many enterprise resources.

---

# Active Directory Security Goals

The primary objectives are:

- Protect identities
- Protect privileged accounts
- Protect authentication
- Protect Domain Controllers
- Protect sensitive data
- Ensure service availability
- Detect malicious activity
- Support rapid incident response

---

# Security Objectives

```
Prevent

↓

Detect

↓

Respond

↓

Recover

↓

Improve
```

Modern Active Directory security is built on continuous improvement rather than one-time configuration.

---

# The CIA Triad

The CIA Triad forms the foundation of information security.

```
            Security

      ┌────────┼────────┐

      ▼        ▼        ▼

Confidentiality

Integrity

Availability
```

---

# Confidentiality

Confidentiality ensures information is only accessible to authorized users.

Examples:

- User passwords
- Group memberships
- Administrative credentials
- Certificate private keys
- Security policies

Controls include:

- Access control
- Encryption
- Least privilege
- Strong authentication

---

# Integrity

Integrity ensures information is accurate and protected from unauthorized modification.

Examples:

- Group Policy Objects
- User attributes
- DNS records
- Security groups
- Trust relationships

Controls include:

- Access permissions
- Auditing
- Change management
- Digital signatures (where applicable)

---

# Availability

Availability ensures systems remain operational for legitimate users.

Examples:

- Domain Controllers
- DNS
- Kerberos
- LDAP
- Global Catalog
- SYSVOL

Controls include:

- Redundant Domain Controllers
- Backups
- Monitoring
- Replication
- Disaster recovery planning

---

# Identity is the New Security Perimeter

Traditional security focused primarily on protecting network boundaries.

Modern enterprise environments rely heavily on protecting identities.

```
Old Model

Firewall

↓

Internal Network

-------------------------

Modern Model

Identity

↓

Authentication

↓

Authorization

↓

Resources
```

Identity protection is therefore a core element of Active Directory security.

---

# Authentication vs Authorization

These concepts are related but distinct.

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you access?" |
| Uses credentials | Uses permissions and policies |
| Occurs before access | Occurs after authentication |

Both processes are essential for secure access control.

---

# Principle of Least Privilege

The Principle of Least Privilege (PoLP) states that users and administrators should receive only the permissions required to perform their tasks.

```
Employee

↓

Only Required Access

↓

Nothing More
```

Benefits include:

- Reduced attack surface
- Lower risk of accidental changes
- Easier auditing
- Improved security

---

# Excessive Privileges

Granting unnecessary permissions can increase organizational risk.

Example:

```
Help Desk

↓

Domain Admin Rights

↓

High Risk
```

Instead:

```
Help Desk

↓

Password Reset

Unlock Accounts

↓

Limited Risk
```

Delegated permissions are generally preferable to broad administrative privileges.

---

# Administrative Tiering

Administrative Tiering separates administrative responsibilities based on the sensitivity of managed systems.

Example:

```
Tier 0

Domain Controllers

Forest

Authentication

--------------------

Tier 1

Servers

Applications

--------------------

Tier 2

User Workstations
```

Administrative accounts should be restricted to the tier they are intended to manage.

---

# Tiered Administration Benefits

- Reduces credential exposure
- Limits lateral movement opportunities
- Protects privileged identities
- Simplifies administrative boundaries
- Improves incident containment

---

# Privileged Accounts

Privileged accounts include:

- Domain Administrators
- Enterprise Administrators
- Schema Administrators
- Backup Operators
- Server Administrators
- Service Accounts with elevated privileges

These accounts require additional protection.

---

# Administrative Account Separation

A common enterprise practice is to use separate accounts for different activities.

Example:

```
Normal User Account

↓

Email

Web Browsing

Documentation

-----------------------

Administrative Account

↓

Server Management

Active Directory

PowerShell

Administration
```

This separation reduces the likelihood that privileged credentials are exposed during routine activities.

---

# Secure Administrative Workstations (SAWs/PAWs)

Many organizations use dedicated administrative workstations for privileged tasks.

```
Privileged Access Workstation

↓

Administrative Login

↓

Domain Controller

↓

Administrative Tasks
```

Characteristics include:

- Restricted software
- Hardened configuration
- Limited internet access
- Enhanced monitoring
- Dedicated administrative use

---

# Security Baselines

A security baseline defines a secure starting configuration.

Examples include:

- Password policy
- Account lockout policy
- Audit policy
- Firewall settings
- Remote management configuration
- Administrative restrictions

Baselines help ensure consistency across systems.

---

# Defense in Depth

No single security control is sufficient.

```
User Awareness

↓

Identity Security

↓

Least Privilege

↓

Endpoint Protection

↓

Network Security

↓

Monitoring

↓

Incident Response
```

Multiple overlapping controls improve resilience.

---

# Shared Responsibility

Active Directory security involves multiple teams.

```
IT Operations

↓

Identity Team

↓

Security Operations

↓

Help Desk

↓

Management

↓

Compliance
```

Effective security depends on coordination across these groups.

---

# Enterprise Security Workflow

```
User Requests Access

↓

Manager Approval

↓

Identity Provisioning

↓

Least Privilege

↓

Authentication

↓

Authorization

↓

Monitoring

↓

Periodic Review
```

Regular access reviews help ensure permissions remain appropriate.

---

# Enterprise Example

Company:

```
Apex Manufacturing
```

Environment:

- 70,000 Users
- 25 Domain Controllers
- Multiple Regional Offices

Security Controls:

- Tiered Administration
- Dedicated Administrative Accounts
- Secure Administrative Workstations
- Multi-Factor Authentication (where implemented)
- Continuous Monitoring
- Centralized Logging
- Regular Privileged Access Reviews

These layered controls reduce the likelihood and impact of credential compromise.

---

# Cybersecurity Perspective

Modern attackers frequently target identities rather than infrastructure alone.

Defensive priorities include:

- Protect privileged accounts.
- Minimize standing administrative privileges.
- Use separate administrative accounts.
- Restrict administrative logon locations.
- Monitor privileged authentication events.
- Regularly review privileged group memberships.
- Apply security updates promptly.
- Conduct periodic security assessments.

Protecting identities is often the most effective way to protect the entire Active Directory environment.

---

# Hands-on Lab

## Objective

Review the security posture of an Active Directory environment.

### Step 1

Identify privileged groups such as:

- Domain Admins
- Enterprise Admins
- Schema Admins
- Account Operators

Document their intended responsibilities.

---

### Step 2

Review the organization's administrative account model.

Determine whether separate standard and administrative accounts are used.

---

### Step 3

Map the environment into administrative tiers.

Identify which systems belong to:

- Tier 0
- Tier 1
- Tier 2

---

### Step 4

Review the current password and account lockout policies.

Document key settings and compare them with organizational standards.

---

### Step 5

Create a simple diagram showing how authentication and authorization work together within Active Directory.

---

# Interview Questions

### Q1: Why is Active Directory considered a high-value target?

**Answer:** Because it manages authentication, authorization, identities, and access to critical enterprise resources. Compromising Active Directory can significantly affect the security of the entire environment.

---

### Q2: What is the Principle of Least Privilege?

**Answer:** It is the practice of granting users and administrators only the permissions necessary to perform their assigned responsibilities.

---

### Q3: What is the difference between authentication and authorization?

**Answer:** Authentication verifies a user's identity, while authorization determines what resources and actions that authenticated user is permitted to access.

---

### Q4: Why should organizations use separate administrative accounts?

**Answer:** Separate administrative accounts reduce the exposure of privileged credentials during routine activities such as email, web browsing, or document editing.

---

### Q5: What is administrative tiering?

**Answer:** Administrative tiering separates privileged administration based on system sensitivity, helping reduce credential exposure and limit the impact of compromise.

---

### Q6: What is the purpose of a Privileged Access Workstation (PAW)?

**Answer:** A PAW is a hardened, dedicated workstation used exclusively for administrative tasks, reducing the risk of privileged credential theft.

---

# Best Practices

- Apply the Principle of Least Privilege.
- Use dedicated administrative accounts.
- Protect Tier 0 assets with the strongest controls.
- Use secure administrative workstations where feasible.
- Review privileged group memberships regularly.
- Enable comprehensive auditing.
- Implement layered security controls.
- Conduct periodic access reviews.

---

# Common Mistakes

- Using Domain Administrator accounts for everyday work.
- Granting excessive permissions.
- Sharing privileged accounts.
- Ignoring administrative account reviews.
- Allowing privileged logons from unmanaged devices.
- Treating identity security as solely a network security issue.
- Relying on a single security control.

---

# Key Takeaways

- Active Directory is one of the most critical components of enterprise infrastructure.
- Identity protection is central to modern cybersecurity.
- The CIA Triad provides the foundation for securing Active Directory.
- Least privilege, administrative tiering, and dedicated administrative accounts significantly reduce organizational risk.
- Layered security, monitoring, and governance are essential for protecting enterprise identity systems.

---

# 18-AD-Security.md

# Part 2 — Active Directory Security Controls, Password Policies, Privileged Access Management, Service Accounts and Auditing

---

# Learning Objectives

After completing this part, you will understand:

- Account Security
- Password Policies
- Fine-Grained Password Policies (FGPP)
- Account Lockout Policies
- Privileged Access Management (PAM)
- Administrative Groups
- Service Accounts
- Managed Service Accounts
- Security Auditing
- Security Logging
- Enterprise Security Monitoring

---

# Introduction

Securing Active Directory requires implementing multiple security controls that work together.

These controls help protect:

- Identities
- Credentials
- Administrative accounts
- Authentication
- Authorization
- Domain Controllers
- Sensitive directory objects

No single control is sufficient on its own.

---

# Defense in Depth

Enterprise Active Directory security uses multiple overlapping controls.

```
            User Awareness

                   │

                   ▼

         Strong Authentication

                   │

                   ▼

          Least Privilege

                   │

                   ▼

      Administrative Controls

                   │

                   ▼

        Security Monitoring

                   │

                   ▼

       Incident Response
```

If one control fails, others continue providing protection.

---

# Account Security

Every Active Directory account represents an identity that must be protected.

Account types include:

- User Accounts
- Computer Accounts
- Service Accounts
- Managed Service Accounts
- Group Managed Service Accounts
- Administrative Accounts

Each account type has different security requirements.

---

# Password Policies

Password policies help reduce the risk of unauthorized access.

Typical settings include:

- Minimum Password Length
- Password Complexity
- Password History
- Maximum Password Age
- Minimum Password Age

Example:

| Setting | Example Value |
|----------|---------------|
| Minimum Length | 14 Characters |
| Complexity | Enabled |
| Password History | 24 Passwords |
| Maximum Age | 90 Days |
| Minimum Age | 1 Day |

Actual values should align with organizational policy and applicable standards.

---

# Strong Password Characteristics

Strong passwords should:

- Be sufficiently long
- Include multiple character types when required by policy
- Avoid dictionary words
- Avoid personal information
- Be unique for each account

Examples of information to avoid:

- Employee names
- Company names
- Birth dates
- Predictable sequences

---

# Fine-Grained Password Policies (FGPP)

Organizations often require stronger password policies for privileged accounts.

```
Standard Users

↓

Standard Password Policy

----------------------------

Privileged Users

↓

Stronger Password Policy
```

FGPP enables multiple password policies within the same Active Directory domain.

---

# Password Settings Objects (PSOs)

Fine-Grained Password Policies are implemented using **Password Settings Objects (PSOs).**

A PSO can define:

- Password Length
- Password History
- Lockout Threshold
- Lockout Duration
- Complexity Requirements
- Password Age

Different PSOs can be assigned to different groups.

---

# Account Lockout Policies

Account lockout policies help slow automated password guessing attempts.

Typical configuration includes:

- Lockout Threshold
- Lockout Duration
- Reset Counter Interval

Example workflow:

```
Incorrect Password

↓

Repeated Attempts

↓

Account Locked

↓

Administrator Verification

↓

Unlock Account
```

Lockout values should balance usability and security.

---

# Password Policy Workflow

```
User Creates Password

↓

Policy Validation

↓

Accepted?

↓

Yes

↓

Password Stored

-------------------------

No

↓

User Chooses New Password
```

---

# Privileged Access Management (PAM)

Privileged Access Management (PAM) refers to controlling, monitoring, and protecting administrative access.

Goals include:

- Reduce standing privileges
- Monitor privileged activity
- Require approval where appropriate
- Improve accountability

---

# Administrative Groups

Examples of privileged groups include:

```
Enterprise Admins

Domain Admins

Schema Admins

Administrators

Backup Operators

Account Operators

Server Operators
```

Membership should be reviewed regularly.

---

# Privileged Access Workflow

```
Administrative Request

↓

Approval

↓

Temporary Access (if applicable)

↓

Administrative Task

↓

Access Removed

↓

Audit
```

Limiting the duration of privileged access reduces risk.

---

# Service Accounts

Many applications require service accounts.

Examples:

- SQL Server
- IIS
- Backup Software
- Monitoring Solutions
- Identity Synchronization
- Enterprise Applications

Service accounts should not be treated like ordinary user accounts.

---

# Risks Associated with Service Accounts

Potential risks include:

- Excessive privileges
- Static passwords
- Shared usage
- Poor documentation
- Forgotten accounts

Poorly managed service accounts are a common source of operational and security issues.

---

# Managed Service Accounts (MSA)

Managed Service Accounts simplify administration.

Benefits:

- Automatic password management
- Reduced password exposure
- Improved security
- Simplified administration

MSAs are intended for a single computer.

---

# Group Managed Service Accounts (gMSA)

Group Managed Service Accounts extend the concept to multiple authorized systems.

Typical uses include:

- Load-balanced applications
- Web server farms
- Scheduled tasks
- Enterprise services

Benefits:

- Automatic password rotation
- Centralized management
- Reduced administrative effort
- Stronger credential management

---

# Service Account Lifecycle

```
Request

↓

Approval

↓

Create Account

↓

Assign Permissions

↓

Deploy Application

↓

Monitor

↓

Review

↓

Retire
```

Documenting the lifecycle improves governance.

---

# Auditing Active Directory

Auditing records important security events.

Examples include:

- User creation
- User deletion
- Group membership changes
- Password resets
- Administrative logons
- Policy changes
- Object modifications

Auditing provides accountability and supports investigations.

---

# Audit Workflow

```
Administrative Action

↓

Windows Security Log

↓

Log Collection

↓

SIEM

↓

Alert

↓

Investigation
```

Centralized logging improves visibility across the enterprise.

---

# Security Logging

Important log sources include:

- Domain Controllers
- Windows Security Logs
- Directory Service Logs
- DNS Logs
- Group Policy Events
- Authentication Events

Security teams should review these logs regularly.

---

# Security Monitoring

Security monitoring helps detect unusual activity.

Examples:

- Repeated failed logons
- Unexpected privileged logons
- Group membership changes
- Account lockouts
- Disabled security controls
- Authentication anomalies

Monitoring should be integrated into broader security operations.

---

# Enterprise Monitoring Workflow

```
Domain Controllers

↓

Security Logs

↓

Central Log Collection

↓

SIEM

↓

Correlation

↓

Alert

↓

Security Analyst
```

---

# Security Review Checklist

```
✓ Privileged Groups Reviewed

✓ Password Policies Verified

✓ Lockout Policies Verified

✓ Service Accounts Documented

✓ Logging Enabled

✓ Auditing Enabled

✓ Administrative Changes Reviewed

✓ Security Alerts Investigated
```

---

# Enterprise Example

Company:

```
Contoso Financial Services
```

Environment:

- 85,000 Users
- 3 Forests
- 41 Domain Controllers

Security Controls:

- Fine-Grained Password Policies
- Privileged Access Management
- Managed Service Accounts
- Centralized Logging
- Continuous Monitoring
- Quarterly Access Reviews

These controls help reduce credential-related risks while supporting compliance requirements.

---

# Cybersecurity Perspective

Identity and credential protection are fundamental to Active Directory security.

Recommended practices include:

- Use strong password policies appropriate to account sensitivity.
- Protect privileged accounts with additional controls.
- Prefer Managed Service Accounts or Group Managed Service Accounts where supported.
- Review privileged group memberships frequently.
- Monitor authentication activity for anomalies.
- Investigate unexpected administrative actions promptly.
- Enable centralized logging and auditing.

Strong credential management significantly reduces the likelihood of identity compromise.

---

# Hands-on Lab

## Objective

Review identity protection settings within a lab Active Directory environment.

### Step 1

Review the domain password policy.

Document:

- Minimum password length
- Password history
- Maximum password age
- Lockout threshold

---

### Step 2

Identify privileged groups.

List:

- Domain Admins
- Enterprise Admins
- Schema Admins

Review current membership.

---

### Step 3

Locate service accounts.

Determine:

- Purpose
- Assigned permissions
- Whether an MSA or gMSA would be appropriate

---

### Step 4

Review Windows Security Logs on a Domain Controller.

Identify:

- Successful logons
- Failed logons
- Account lockouts
- Group membership changes

---

### Step 5

Create a simple security review checklist for monthly Active Directory account audits.

---

# Interview Questions

### Q1: Why are Fine-Grained Password Policies useful?

**Answer:** They allow different password and lockout policies to be applied to different users or groups, enabling stronger protection for privileged accounts.

---

### Q2: What is the purpose of an account lockout policy?

**Answer:** It helps slow automated password guessing attempts by temporarily locking an account after a defined number of failed authentication attempts.

---

### Q3: What is Privileged Access Management (PAM)?

**Answer:** PAM is the practice of controlling, monitoring, and protecting privileged access to reduce the risk associated with administrative accounts.

---

### Q4: Why are Managed Service Accounts more secure than traditional service accounts?

**Answer:** Managed Service Accounts automatically manage passwords and reduce manual credential administration, lowering the risk of password-related issues.

---

### Q5: Why is auditing important in Active Directory?

**Answer:** Auditing provides accountability, supports investigations, detects unauthorized changes, and helps organizations meet compliance requirements.

---

### Q6: Why should privileged group membership be reviewed regularly?

**Answer:** Regular reviews help ensure only authorized users retain elevated permissions, reducing unnecessary privilege and security risk.

---

# Best Practices

- Apply strong password policies based on account sensitivity.
- Use Fine-Grained Password Policies for privileged accounts where appropriate.
- Review privileged groups on a regular schedule.
- Prefer gMSAs or MSAs for supported services.
- Enable comprehensive auditing and centralized logging.
- Document all service accounts and their owners.
- Investigate unusual authentication patterns promptly.
- Conduct periodic access reviews.

---

# Common Mistakes

- Using the same password policy for all account types without evaluating risk.
- Leaving obsolete service accounts enabled.
- Granting excessive privileges to service accounts.
- Ignoring audit logs.
- Failing to document privileged access.
- Not reviewing administrative group memberships.
- Delaying investigation of repeated account lockouts.

---

# Key Takeaways

- Active Directory security relies on layered controls rather than a single defense.
- Password policies, account lockout policies, and FGPP strengthen identity protection.
- Privileged Access Management reduces the risks associated with elevated permissions.
- Managed Service Accounts simplify credential management and improve security.
- Auditing and centralized monitoring provide visibility into security-relevant activity and support rapid response.

---

# 18-AD-Security.md

# Part 3 — Securing Domain Controllers, Group Policy Security, Administrative Protection, Delegation, Network Security and Monitoring

---

# Learning Objectives

After completing this part, you will understand:

- Domain Controller Security
- Physical Security
- Operating System Hardening
- Group Policy Security
- Administrative Delegation
- Tiered Administration
- Secure DNS
- Time Synchronization Security
- Windows Firewall
- Security Monitoring
- Enterprise Hardening Strategies

---

# Introduction

Domain Controllers (DCs) are the most critical systems in an Active Directory environment.

A compromised Domain Controller can expose:

- User accounts
- Computer accounts
- Password hashes
- Kerberos authentication
- Group Policy Objects
- DNS
- Trust relationships
- Certificate information (where integrated)

Because of this, Domain Controllers require significantly stronger protection than ordinary servers.

---

# Domain Controller Security Model

```
              Domain Controller

                     │

     ┌───────────────┼────────────────┐

     ▼               ▼                ▼

Authentication   Authorization    Directory Database

     ▼               ▼                ▼

Kerberos         LDAP            SYSVOL

     ▼               ▼                ▼

Enterprise Identity Infrastructure
```

---

# Why Domain Controllers Must Be Protected

Every authentication request typically involves a Domain Controller.

```
User

↓

Logon Request

↓

Domain Controller

↓

Authentication

↓

Authorization

↓

Access Granted
```

If attackers gain administrative control of a Domain Controller, they may be able to manipulate identity services across the domain.

---

# Physical Security

Domain Controllers should be physically protected.

Recommended controls:

- Restricted server rooms
- Badge-controlled access
- CCTV monitoring
- Environmental monitoring
- Locked racks
- Visitor logging
- Hardware inventory

Physical compromise can bypass many software security controls.

---

# Operating System Hardening

Domain Controllers should have a minimal attack surface.

Recommended practices:

- Install only required roles
- Remove unnecessary software
- Disable unused services
- Apply security updates promptly
- Use supported Windows Server versions
- Enable Windows Defender or approved endpoint protection

Hardening reduces opportunities for exploitation.

---

# Domain Controller Hardening Workflow

```
Install Windows Server

↓

Apply Updates

↓

Promote to Domain Controller

↓

Apply Security Baseline

↓

Enable Auditing

↓

Continuous Monitoring
```

---

# Security Baselines

Security baselines provide a consistent starting configuration.

Typical baseline areas include:

- Password policies
- Audit policies
- Firewall rules
- Remote management
- Security options
- User rights assignments
- Event log settings

Applying standardized baselines improves consistency across Domain Controllers.

---

# Administrative Access Restrictions

Administrative access should be tightly controlled.

```
Administrator

↓

Privileged Account

↓

Privileged Access Workstation

↓

Domain Controller

↓

Administrative Session
```

Avoid administering Domain Controllers from unmanaged or non-administrative systems.

---

# Group Policy Security

Group Policy is one of the most powerful administrative mechanisms in Active Directory.

Because Group Policy can configure thousands of computers simultaneously, unauthorized modification presents significant risk.

---

# Protecting Group Policy Objects

Recommendations:

- Restrict GPO editing permissions.
- Delegate administration carefully.
- Audit GPO changes.
- Document critical policies.
- Review linked GPOs periodically.

Only authorized administrators should modify security-related Group Policy Objects.

---

# Group Policy Security Workflow

```
Change Request

↓

Approval

↓

Modify GPO

↓

Testing

↓

Deployment

↓

Monitoring

↓

Audit
```

Production GPO changes should follow formal change management procedures.

---

# Delegation Security

Delegation improves operational efficiency but must be implemented carefully.

Example:

```
Domain Admin

↓

Delegate

↓

Help Desk

↓

Password Reset

↓

No Domain Admin Rights
```

Grant only the permissions necessary for assigned responsibilities.

---

# Secure Delegation Principles

- Delegate to groups instead of individual users.
- Document delegated permissions.
- Review delegations regularly.
- Remove obsolete delegations.
- Follow least privilege.

---

# Administrative Tiering

Separating administration by security tier reduces credential exposure.

```
Tier 0

↓

Domain Controllers

Forest

Authentication

-------------------------

Tier 1

↓

Application Servers

File Servers

Database Servers

-------------------------

Tier 2

↓

User Workstations

Laptops

Desktops
```

Credentials from higher tiers should not routinely be used on lower-tier systems.

---

# Protecting Administrative Credentials

Administrative credentials should never be exposed unnecessarily.

Recommendations:

- Use separate admin accounts.
- Avoid internet browsing with admin accounts.
- Use dedicated administrative workstations.
- Sign out after administrative tasks.
- Rotate credentials according to policy.

Credential hygiene is essential for protecting privileged identities.

---

# DNS Security

Active Directory depends heavily on DNS.

Threats include:

- Unauthorized DNS changes
- Incorrect DNS configuration
- Zone manipulation
- Service disruption

Recommendations:

- Use secure dynamic updates where appropriate.
- Restrict DNS administration.
- Monitor DNS changes.
- Audit administrative actions.

---

# Time Synchronization Security

Kerberos relies on accurate time.

```
Time Source

↓

Domain Controller

↓

Member Servers

↓

Client Computers
```

Significant time differences can prevent successful authentication.

Protect the organization's time synchronization hierarchy and monitor for unexpected drift.

---

# Windows Firewall

Windows Firewall should remain enabled on Domain Controllers unless a documented operational requirement exists.

Benefits:

- Network filtering
- Reduced attack surface
- Protection from unnecessary inbound connections

Firewall rules should follow organizational standards.

---

# Network Segmentation

Many enterprises isolate Domain Controllers from general-purpose systems.

Example:

```
Users

↓

Corporate Network

↓

Administrative Network

↓

Domain Controllers
```

Segmentation limits unnecessary communication paths and reduces exposure.

---

# Security Monitoring

Continuous monitoring helps detect suspicious activity.

Monitor for:

- Administrative logons
- Group membership changes
- GPO modifications
- DNS changes
- Authentication failures
- Replication failures
- Service failures

Monitoring supports early detection of operational and security issues.

---

# Security Monitoring Workflow

```
Domain Controllers

↓

Security Events

↓

Log Collection

↓

SIEM

↓

Correlation

↓

Alert

↓

Security Operations Center
```

---

# Administrative Reviews

Regular reviews should include:

- Privileged group memberships
- Delegated permissions
- Service accounts
- Group Policy administrators
- Domain Controller configuration
- Security baselines

Periodic reviews help maintain a secure environment.

---

# Enterprise Hardening Checklist

```
✓ Supported Windows Server Version

✓ Latest Security Updates

✓ Security Baseline Applied

✓ Windows Firewall Enabled

✓ Privileged Access Restricted

✓ Logging Enabled

✓ Auditing Enabled

✓ DNS Protected

✓ Time Synchronization Healthy

✓ GPO Permissions Reviewed
```

---

# Enterprise Example

Company:

```
Northwind Energy
```

Infrastructure:

- 55 Domain Controllers
- 120,000 Users
- 4 Forests
- Multiple Geographic Regions

Security Controls:

- Tiered Administration
- Dedicated Privileged Access Workstations
- Restricted GPO Editors
- Security Baselines
- Centralized SIEM
- Continuous Health Monitoring
- Quarterly Administrative Reviews

These layered controls reduce operational risk while improving visibility into administrative activity.

---

# Cybersecurity Perspective

Domain Controllers should be treated as **Tier 0 assets** with the highest level of protection.

Defensive recommendations:

- Restrict interactive logons to authorized administrators.
- Limit software installed on Domain Controllers.
- Apply security updates in accordance with change management.
- Monitor privileged authentication and configuration changes.
- Protect DNS and time synchronization infrastructure.
- Audit Group Policy modifications.
- Review delegated permissions regularly.
- Maintain tested backup and recovery procedures.

Strong operational discipline is as important as technical security controls.

---

# Hands-on Lab

## Objective

Review Domain Controller hardening and administrative security.

### Step 1

Inspect a Domain Controller and document:

- Installed roles
- Installed features
- Running services

Identify unnecessary components for further review.

---

### Step 2

Review the Windows Firewall configuration.

Confirm that required rules are enabled and document any exceptions.

---

### Step 3

Review the permissions on a critical Group Policy Object.

Identify:

- Editors
- Owners
- Delegated administrators

---

### Step 4

Review privileged group memberships.

Verify that all members have a documented business justification.

---

### Step 5

Create a Domain Controller security checklist for quarterly reviews.

---

# Interview Questions

### Q1: Why are Domain Controllers considered Tier 0 assets?

**Answer:** They provide authentication, authorization, and directory services for the domain. Compromise of a Domain Controller can significantly impact the security of the entire Active Directory environment.

---

### Q2: Why should Group Policy modifications be tightly controlled?

**Answer:** Group Policy can configure thousands of systems simultaneously, so unauthorized or incorrect changes may have widespread operational and security impacts.

---

### Q3: Why is DNS security important in Active Directory?

**Answer:** Active Directory depends on DNS for locating domain services. Unauthorized or incorrect DNS changes can disrupt authentication and other directory operations.

---

### Q4: Why should administrative accounts be separated from normal user accounts?

**Answer:** Using separate accounts reduces the exposure of privileged credentials during routine activities and supports the Principle of Least Privilege.

---

### Q5: Why is accurate time synchronization critical?

**Answer:** Kerberos authentication relies on synchronized time. Significant clock differences can cause authentication failures.

---

### Q6: Why should delegated permissions be reviewed regularly?

**Answer:** Regular reviews help ensure permissions remain appropriate, remove obsolete access, and reduce the risk of privilege accumulation.

---

# Best Practices

- Treat Domain Controllers as Tier 0 systems.
- Apply standardized security baselines.
- Restrict administrative access to authorized personnel.
- Protect Group Policy administration.
- Keep Windows Firewall enabled unless a documented exception exists.
- Monitor DNS and time synchronization health.
- Conduct periodic administrative and configuration reviews.
- Maintain comprehensive logging and centralized monitoring.

---

# Common Mistakes

- Installing unnecessary software on Domain Controllers.
- Allowing broad Group Policy editing permissions.
- Using privileged accounts for routine user activities.
- Ignoring DNS or time synchronization issues.
- Failing to review delegated permissions.
- Delaying security updates without proper risk assessment.
- Neglecting documentation of administrative changes.

---

# Key Takeaways

- Domain Controllers are the most sensitive systems in an Active Directory environment and require the strongest protections.
- Group Policy, DNS, and privileged administration are critical security components.
- Administrative tiering, security baselines, and least privilege significantly reduce organizational risk.
- Continuous monitoring, auditing, and periodic reviews improve security posture.
- Operational discipline, documentation, and governance are essential for maintaining a secure Active Directory infrastructure.

---

**Next:** Part 4