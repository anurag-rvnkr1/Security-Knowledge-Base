# 20-AD-Defense-and-Hardening.md

# Part 1 — Active Directory Defense Strategy, Enterprise Hardening Principles, Tier-0 Protection and Secure Administration

> **Important Note**
>
> This chapter focuses exclusively on **defensive security**. The objective is to help system administrators, security engineers, SOC analysts, blue teams, and security architects harden Active Directory against modern threats.

---

# Learning Objectives

After completing this part, you will understand:

- Defense-in-Depth
- Zero Trust Principles
- Active Directory Hardening Strategy
- Tier-0 Protection
- Identity Hardening
- Administrative Security
- Secure Administration Model
- Security Baselines
- Enterprise Hardening Roadmap

---

# Introduction

Active Directory is the identity backbone of most enterprise Windows environments.

Since almost every authentication and authorization request depends on AD, protecting it requires **multiple overlapping security controls** rather than relying on a single defense.

Enterprise hardening is built on three principles:

- Prevent compromise
- Detect abnormal activity
- Recover rapidly

---

# Enterprise Defense Model

```
                   Active Directory

                          │

      ┌───────────────────┼───────────────────┐

      ▼                   ▼                   ▼

 Prevention          Detection          Recovery

      ▼                   ▼                   ▼

Hardening         Monitoring         Backup

Least Privilege   SIEM              DR

MFA               Logging           Recovery

Tiering           Hunting           Validation
```

---

# Modern Security Philosophy

Traditional security focused on protecting the network perimeter.

```
Internet

↓

Firewall

↓

Internal Network
```

Modern enterprises instead protect **identities**.

```
Identity

↓

Authentication

↓

Authorization

↓

Business Resources
```

This identity-first model underpins Microsoft's current security recommendations.

---

# Defense-in-Depth

Multiple independent controls reduce overall risk.

```
Security Awareness

↓

Identity Protection

↓

Least Privilege

↓

Administrative Tiering

↓

Endpoint Protection

↓

Network Segmentation

↓

Monitoring

↓

Incident Response
```

No individual control should be considered sufficient by itself.

---

# Zero Trust Principles

Zero Trust assumes that no user, device, or application should be trusted automatically.

Core principles:

- Verify explicitly
- Use least privilege
- Assume breach
- Continuously validate identity
- Monitor continuously

```
Request Access

↓

Authenticate

↓

Authorize

↓

Evaluate Risk

↓

Grant Limited Access

↓

Continuous Verification
```

---

# Active Directory Hardening Goals

The primary objectives are:

- Protect identities
- Protect Domain Controllers
- Protect privileged accounts
- Reduce attack surface
- Minimize administrative exposure
- Improve visibility
- Strengthen recovery capability

---

# Hardening Layers

```
Layer 1

Identity

↓

Layer 2

Endpoints

↓

Layer 3

Servers

↓

Layer 4

Domain Controllers

↓

Layer 5

Monitoring

↓

Layer 6

Governance
```

Each layer contributes to the organization's overall security posture.

---

# Tier-0 Protection

Tier-0 assets represent the highest-value systems in an Active Directory environment.

Examples:

```
Tier 0

├── Domain Controllers

├── Enterprise Admins

├── Domain Admins

├── PKI / AD CS

├── Authentication Services

├── Azure AD Connect / Entra Connect

└── Privileged Identity Infrastructure
```

Tier-0 assets should receive the strongest available protections.

---

# Tiered Administration

Administrative responsibilities should be separated by security tier.

```
Tier 0

↓

Identity Infrastructure

--------------------------

Tier 1

↓

Enterprise Servers

--------------------------

Tier 2

↓

Workstations
```

Administrative credentials from higher tiers should not routinely be used on lower-tier systems.

---

# Identity Hardening

Identity protection includes:

- Strong authentication
- Least privilege
- Dedicated administrative accounts
- Regular privilege reviews
- Secure password policies
- Multi-Factor Authentication (where supported)
- Conditional Access (hybrid/cloud environments)

Identity is the organization's primary security boundary.

---

# Administrative Account Separation

Recommended account model:

```
Employee

│

├── Standard User Account

│      ├── Email

│      ├── Web

│      └── Office Work

│

└── Administrative Account

       ├── AD Administration

       ├── PowerShell

       └── Server Management
```

Routine work should never be performed using privileged accounts.

---

# Privileged Access Workstations (PAWs)

Administrative activities should ideally be performed from dedicated hardened systems.

Characteristics:

- Restricted software
- Hardened operating system
- Enhanced monitoring
- Limited internet access
- Dedicated administrative use

```
Administrator

↓

PAW

↓

Domain Controller

↓

Administrative Task
```

---

# Security Baselines

Security baselines define approved configurations.

Typical areas include:

| Area | Example |
|------|----------|
| Password Policy | Strong password requirements |
| Audit Policy | Advanced auditing enabled |
| Firewall | Enabled |
| SMB | Secure configuration |
| Remote Management | Restricted |
| User Rights | Least privilege |

Baselines improve consistency across the enterprise.

---

# Reducing Attack Surface

Examples include:

- Remove unnecessary software
- Disable unused services
- Eliminate obsolete protocols
- Remove inactive accounts
- Remove unused administrative groups
- Restrict administrative logons

Smaller attack surfaces are generally easier to secure.

---

# Secure Administrative Workflow

```
Administrative Request

↓

Approval

↓

Privileged Account

↓

Privileged Workstation

↓

Administrative Task

↓

Audit

↓

Review
```

---

# Enterprise Hardening Checklist

```
✓ Tier-0 Assets Identified

✓ Privileged Accounts Protected

✓ Administrative Accounts Separated

✓ Security Baselines Applied

✓ MFA Implemented (where supported)

✓ Windows Firewall Enabled

✓ Logging Enabled

✓ SIEM Connected

✓ Backups Verified

✓ Recovery Tested
```

---

# Enterprise Example

Company:

```
Contoso Manufacturing
```

Environment:

- 130,000 Users
- 60 Domain Controllers
- Hybrid Active Directory

Hardening Program:

- Tiered Administration
- Privileged Access Workstations
- Quarterly Security Reviews
- Continuous SIEM Monitoring
- Security Baselines
- Dedicated Tier-0 Administrators

Results:

- Reduced privileged account exposure
- Improved audit readiness
- Faster incident response
- Stronger operational consistency

---

# Cybersecurity Perspective

Hardening is not a one-time project.

A mature security program continuously:

- Reviews configurations
- Applies updates
- Removes unnecessary privileges
- Monitors identity activity
- Validates backups
- Tests recovery
- Improves detections

Security posture should improve incrementally over time.

---

# Hands-on Lab

## Objective

Assess the hardening posture of a lab Active Directory environment.

### Step 1

Identify:

- Tier-0 assets
- Administrative accounts
- Privileged groups

---

### Step 2

Review:

- Password policy
- Audit policy
- Firewall configuration
- Administrative account usage

---

### Step 3

Verify whether administrative tasks are performed using dedicated accounts.

---

### Step 4

Document opportunities to reduce the attack surface.

---

### Step 5

Create a Tier-0 protection plan for the environment.

---

# Interview Questions

### Q1: What is Defense-in-Depth?

**Answer:** A layered security strategy that combines multiple preventive, detective, and recovery controls so that the failure of one control does not compromise the entire environment.

---

### Q2: Why are Tier-0 assets critical?

**Answer:** They control enterprise authentication and identity infrastructure. Compromise of Tier-0 assets can affect the entire Active Directory environment.

---

### Q3: What is the purpose of Privileged Access Workstations?

**Answer:** They reduce exposure of privileged credentials by providing hardened, dedicated systems for administrative tasks.

---

### Q4: Why should administrative accounts be separated from standard user accounts?

**Answer:** Separation minimizes the risk of exposing privileged credentials during routine activities such as email or web browsing.

---

### Q5: What is the purpose of security baselines?

**Answer:** Security baselines establish standardized secure configurations that improve consistency and reduce misconfigurations.

---

### Q6: Why should organizations continuously review their hardening posture?

**Answer:** Enterprise environments and threats evolve over time, requiring ongoing improvement of security controls.

---

# Best Practices

- Protect Tier-0 assets with the strongest controls.
- Use dedicated administrative accounts.
- Implement Privileged Access Workstations.
- Apply standardized security baselines.
- Continuously monitor identity infrastructure.
- Reduce unnecessary attack surface.
- Review privileged access regularly.
- Validate recovery capabilities.

---

# Common Mistakes

- Using Domain Admin accounts for everyday tasks.
- Ignoring Tier-0 boundaries.
- Allowing unmanaged administrative workstations.
- Failing to remove obsolete privileged accounts.
- Delaying security baseline updates.
- Treating hardening as a one-time project.

---

# Key Takeaways

- Active Directory hardening is based on layered defensive controls.
- Tier-0 protection is the foundation of enterprise identity security.
- Identity-first security, Zero Trust, and least privilege significantly reduce organizational risk.
- Continuous improvement is essential for maintaining a strong security posture.

---

# 20-AD-Defense-and-Hardening.md

# Part 2 — Enterprise Identity Protection, Privileged Access Security, Credential Protection, Secure Configuration and Attack Surface Reduction

> **Important Note**
>
> This chapter focuses exclusively on **defensive Active Directory hardening**. The objective is to strengthen enterprise identity infrastructure against unauthorized access and reduce opportunities for attackers.

---

# Learning Objectives

After completing this part, you will understand:

- Identity Protection Strategy
- Privileged Identity Security
- Credential Protection
- Multi-Factor Authentication (MFA)
- Secure Administrative Configuration
- Attack Surface Reduction (ASR)
- Windows Defender Security Features
- Secure Service Account Management
- Enterprise Configuration Management

---

# Introduction

Identity is now the most valuable asset in an enterprise.

Modern attackers rarely begin by targeting Domain Controllers directly. Instead, they often attempt to compromise:

- User accounts
- Administrator accounts
- Service accounts
- Authentication tokens
- Identity infrastructure

Protecting identities significantly reduces overall enterprise risk.

---

# Enterprise Identity Protection Model

```
             Enterprise Identity

                     │

     ┌───────────────┼────────────────┐

     ▼               ▼                ▼

Authentication  Authorization   Monitoring

     ▼               ▼                ▼

Access Control   Least Privilege   SIEM
```

Identity protection should be integrated across every security layer.

---

# Identity Hardening Principles

Core principles include:

- Verify identities before granting access.
- Minimize privileges.
- Protect administrative credentials.
- Continuously monitor authentication.
- Review permissions regularly.
- Remove unnecessary access promptly.

---

# Privileged Identity Security

Privileged identities require stronger protection than standard user accounts.

Examples include:

```
Enterprise Admins

↓

Domain Admins

↓

Backup Operators

↓

Schema Admins

↓

Service Administrators
```

Recommended controls:

- Separate administrative accounts
- Dedicated workstations
- Enhanced auditing
- Frequent access reviews
- Strong authentication

---

# Administrative Identity Lifecycle

```
Request

↓

Approval

↓

Provision

↓

Use

↓

Monitor

↓

Review

↓

Remove Access
```

Administrative privileges should be granted only for legitimate business needs.

---

# Multi-Factor Authentication (MFA)

Where supported, MFA adds an additional verification step beyond passwords.

Typical factors include:

- Something you know (password)
- Something you have (security key or authenticator app)
- Something you are (biometric verification)

```
Password

+

Authenticator

↓

Access Granted
```

MFA significantly reduces the impact of compromised passwords but should be combined with other security controls.

---

# Credential Protection

Credential protection aims to reduce exposure of authentication secrets.

Recommended practices:

- Never share passwords.
- Avoid storing passwords in plain text.
- Use password managers where approved.
- Protect administrative credentials.
- Disable inactive accounts.
- Rotate sensitive credentials according to policy.

---

# Secure Password Management

```
Strong Password

↓

Policy Validation

↓

Secure Storage

↓

Periodic Review

↓

Credential Rotation
```

Organizations should follow applicable standards and vendor guidance for password management.

---

# Service Account Security

Service accounts require careful governance.

Recommended controls:

- Document ownership.
- Assign minimum required permissions.
- Review regularly.
- Remove unused accounts.
- Prefer Managed Service Accounts (MSA) or Group Managed Service Accounts (gMSA) where appropriate.

```
Service Account

↓

Owner Assigned

↓

Permissions Granted

↓

Monitoring

↓

Periodic Review
```

---

# Group Managed Service Accounts (gMSA)

Advantages include:

- Automatic password management
- Reduced administrative overhead
- Improved credential security
- Support for multiple authorized systems

gMSAs help reduce operational risk associated with manually managed service account passwords.

---

# Secure Administrative Configuration

Administrative systems should follow strict configuration standards.

Examples:

- Hardened operating system
- Latest security updates
- Endpoint protection enabled
- Firewall enabled
- Unnecessary software removed
- Administrative tools only

---

# Attack Surface Reduction

Attack Surface Reduction (ASR) is the practice of minimizing opportunities for attackers.

Examples:

- Disable unused services.
- Remove obsolete software.
- Eliminate legacy protocols.
- Restrict administrative logons.
- Remove inactive accounts.
- Limit local administrator usage.

```
Large Attack Surface

↓

Hardening

↓

Smaller Attack Surface

↓

Reduced Risk
```

---

# Windows Defender Security Features

Organizations should evaluate and implement appropriate Windows security capabilities, such as:

- Microsoft Defender Antivirus
- Microsoft Defender Firewall
- Microsoft Defender SmartScreen
- Exploit protection
- Controlled Folder Access (where appropriate)

Deployment should align with organizational policies and compatibility requirements.

---

# Endpoint Hardening

Recommended endpoint controls:

- Secure boot (where supported)
- BitLocker encryption
- Endpoint Detection and Response (EDR)
- Automatic updates
- Device control policies
- Application control (where appropriate)

Endpoints are often the initial entry point into enterprise environments.

---

# Administrative Session Security

```
Administrator

↓

Privileged Workstation

↓

Secure Authentication

↓

Administrative Session

↓

Logout

↓

Session Ends
```

Administrative sessions should be limited to authorized systems.

---

# Configuration Management

Configuration management ensures systems remain aligned with approved standards.

```
Baseline

↓

Deployment

↓

Monitoring

↓

Compliance Review

↓

Remediation
```

Configuration drift should be detected and corrected.

---

# Enterprise Identity Governance

Organizations should periodically review:

- Administrative accounts
- Group memberships
- Service accounts
- Delegated permissions
- Password policies
- Authentication settings

Governance supports long-term security and compliance.

---

# Enterprise Example

Company:

```
Northwind Financial Group
```

Environment:

- 180,000 Users
- Hybrid Identity
- 75 Domain Controllers

Identity Protection Strategy:

- Dedicated administrative accounts
- Privileged Access Workstations
- Multi-Factor Authentication
- Managed Service Accounts
- Centralized logging
- Quarterly privileged access reviews
- Automated configuration compliance

Results:

- Reduced privileged credential exposure
- Improved compliance
- Faster detection of identity anomalies
- Lower operational risk

---

# Cybersecurity Perspective

Identity protection is one of the highest-return security investments.

Defenders should prioritize:

- Strong authentication
- Least privilege
- Continuous monitoring
- Administrative account protection
- Secure configuration management
- Regular privilege reviews

These controls significantly improve resilience against identity-focused attacks.

---

# Hands-on Lab

## Objective

Evaluate identity protection controls in a lab Active Directory environment.

### Step 1

Identify:

- Privileged accounts
- Service accounts
- Administrative workstations

---

### Step 2

Review:

- Password policies
- MFA deployment (if available)
- Account lifecycle procedures

---

### Step 3

Inspect service accounts.

Determine:

- Owner
- Purpose
- Permission level
- Whether gMSA could be used

---

### Step 4

Compare endpoint configurations against the organization's security baseline.

---

### Step 5

Prepare a prioritized remediation plan to strengthen identity protection.

---

# Interview Questions

### Q1: Why should privileged identities receive stronger protection?

**Answer:** Because compromise of privileged accounts can significantly affect the security and integrity of the Active Directory environment.

---

### Q2: What are the benefits of Multi-Factor Authentication?

**Answer:** MFA requires an additional verification factor beyond a password, reducing the risk associated with compromised credentials.

---

### Q3: Why are gMSAs recommended over traditional service accounts?

**Answer:** gMSAs automatically manage passwords, reduce manual administration, and improve credential security for supported workloads.

---

### Q4: What is Attack Surface Reduction?

**Answer:** It is the practice of minimizing opportunities for attackers by removing unnecessary software, services, protocols, and privileges.

---

### Q5: Why is configuration management important?

**Answer:** It ensures systems remain compliant with approved security baselines and helps detect unauthorized or accidental configuration changes.

---

### Q6: Why should identity governance be performed regularly?

**Answer:** Regular reviews ensure permissions remain appropriate, inactive accounts are removed, and administrative access aligns with business requirements.

---

# Best Practices

- Protect privileged identities with enhanced controls.
- Implement MFA wherever supported.
- Prefer gMSAs for supported enterprise services.
- Apply standardized configuration baselines.
- Continuously reduce the attack surface.
- Monitor administrative authentication events.
- Conduct periodic identity governance reviews.
- Maintain accurate documentation of privileged access.

---

# Common Mistakes

- Sharing privileged credentials.
- Leaving obsolete service accounts enabled.
- Allowing configuration drift.
- Ignoring inactive privileged accounts.
- Delaying removal of unnecessary software or services.
- Treating identity governance as an annual activity instead of an ongoing process.

---

# Key Takeaways

- Identity protection is central to modern Active Directory defense.
- Strong authentication, secure credential management, and least privilege reduce enterprise risk.
- Attack Surface Reduction and configuration management strengthen system resilience.
- Continuous governance and monitoring are essential for maintaining a secure identity infrastructure.

---

**Next:** Part 3