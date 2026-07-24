# 22-Windows-Hardening.md

# Part 1 — Windows Hardening Fundamentals, Security Baselines, Attack Surface Reduction, and Enterprise Hardening Principles

---

# Introduction

A freshly installed Windows system is functional, but it is **not fully hardened**.

Default configurations prioritize:

- Compatibility
- Ease of use
- Broad hardware support
- User convenience

Enterprise environments require additional security controls to reduce the likelihood and impact of attacks.

**Windows Hardening** is the process of reducing the operating system's attack surface by disabling unnecessary functionality, enforcing secure configurations, limiting privileges, and continuously monitoring compliance.

Hardening is one of the most effective preventive cybersecurity measures.

---

# Learning Objectives

By the end of this section, you will understand:

- Windows hardening concepts
- Security baselines
- Attack surface reduction
- Defense in depth
- Least privilege
- Secure configuration principles
- Enterprise hardening strategy
- Windows hardening lifecycle

---

# What is Windows Hardening?

Windows hardening is the process of configuring Windows to minimize security risks while maintaining required business functionality.

Hardening focuses on:

- Reducing exposed services
- Removing unnecessary software
- Restricting administrative privileges
- Securing authentication
- Enforcing security policies
- Monitoring compliance

The objective is to make systems significantly more difficult to compromise.

---

# Why Hardening Matters

Unnecessary services, weak configurations, and excessive privileges increase the attack surface.

Example:

```text
Default Installation

↓

Many Services Enabled

↓

Large Attack Surface

↓

Higher Risk
```

After hardening:

```text
Required Services Only

↓

Least Privilege

↓

Reduced Attack Surface

↓

Improved Security
```

---

# Security Goals

Windows hardening supports the CIA Triad.

| Goal | Description |
|------|-------------|
| Confidentiality | Prevent unauthorized disclosure |
| Integrity | Prevent unauthorized modification |
| Availability | Maintain reliable operation |

Every hardening decision should balance these objectives.

---

# Defense in Depth

Hardening is one layer within a broader security strategy.

```text
User Awareness

↓

Identity Protection

↓

Windows Hardening

↓

Firewall

↓

Endpoint Protection

↓

Monitoring

↓

Incident Response
```

Multiple defensive layers provide better protection than relying on a single control.

---

# Principle of Least Privilege

Users and services should receive only the permissions necessary to perform assigned tasks.

Instead of:

```text
Everyone

↓

Local Administrator
```

Use:

```text
Standard User

↓

Temporary Elevation (When Required)

↓

Administrative Task
```

Least privilege limits the damage that can result from compromised accounts.

---

# Attack Surface

The attack surface consists of every point through which an attacker may interact with a system.

Examples include:

- Open network ports
- Running services
- Installed applications
- Administrative accounts
- Scheduled tasks
- Remote management interfaces
- Browser plugins
- Shared folders

Reducing unnecessary exposure lowers overall risk.

---

# Attack Surface Reduction (ASR)

Attack Surface Reduction (ASR) is the practice of limiting opportunities for exploitation.

Examples:

- Disable unused services
- Block unnecessary applications
- Restrict Office macros
- Limit script execution
- Prevent credential theft
- Restrict removable media
- Reduce administrative privileges

Attack Surface Reduction should be guided by business requirements.

---

# Microsoft Security Baselines

Microsoft publishes recommended security baselines for Windows.

These baselines provide:

- Secure default settings
- Group Policy recommendations
- Registry configurations
- Audit policy settings
- Administrative guidance

Organizations commonly customize these baselines to meet operational requirements.

---

# Security Baseline Workflow

```text
Microsoft Baseline

↓

Review

↓

Customize

↓

Testing

↓

Deployment

↓

Monitoring

↓

Periodic Review
```

Baselines should never be applied directly to production without validation.

---

# Hardening Lifecycle

```text
Assess

↓

Plan

↓

Implement

↓

Test

↓

Deploy

↓

Monitor

↓

Review

↓

Improve
```

Hardening is a continuous process rather than a one-time project.

---

# Enterprise Hardening Strategy

Typical strategy:

```text
Security Requirements

↓

Baseline Configuration

↓

Group Policy

↓

Automation

↓

Monitoring

↓

Compliance Validation
```

Standardized configurations improve consistency across large environments.

---

# Common Hardening Areas

| Area | Examples |
|------|-----------|
| Accounts | Least privilege, MFA |
| Services | Disable unnecessary services |
| Networking | Firewall, SMB configuration |
| Authentication | Password policies |
| Storage | BitLocker |
| Logging | Advanced auditing |
| Updates | Security patching |
| Applications | Application control |

---

# Operating System Hardening

Key objectives include:

- Remove unused features
- Disable unnecessary services
- Secure startup
- Protect credentials
- Restrict remote access
- Enable security logging
- Keep systems updated

Operating system hardening forms the foundation of endpoint security.

---

# Application Hardening

Applications should also be hardened.

Examples:

- Remove unused software
- Update applications regularly
- Disable unnecessary plugins
- Restrict macro execution
- Enable application allowlisting
- Review permissions

Applications are frequent attack vectors.

---

# Service Hardening

Services should be reviewed regularly.

Questions to ask:

- Is this service required?
- Is it running unnecessarily?
- Can it use a lower privilege account?
- Is network access required?

Unused services should be disabled after testing.

---

# Network Hardening

Network-related controls include:

- Windows Defender Firewall
- Secure DNS configuration
- Disable obsolete protocols
- Restrict SMB exposure
- Secure remote management
- Network segmentation

Network hardening reduces opportunities for unauthorized access.

---

# Authentication Hardening

Recommended controls:

- Multi-Factor Authentication (MFA)
- Strong password policies
- Windows Hello for Business
- Credential Guard
- Account lockout policies
- Smart cards (where applicable)

Identity is a primary security boundary.

---

# Hardening and Compliance

Hardening contributes to compliance with:

- ISO/IEC 27001
- NIST Cybersecurity Framework
- CIS Controls
- PCI DSS
- HIPAA
- SOC 2

Compliance requirements should be mapped to organizational security objectives.

---

# Enterprise Example

A financial institution deploys a standard Windows image with:

- Microsoft security baseline
- BitLocker enabled
- Windows Defender Firewall enabled
- Credential Guard enabled
- PowerShell logging enabled
- Local administrator restrictions
- Automatic updates
- Centralized monitoring

Every workstation receives the same approved baseline, simplifying administration and improving security consistency.

---

# Cybersecurity Perspective

Most successful attacks exploit:

- Weak configurations
- Excessive privileges
- Missing patches
- Misconfigured services
- Unnecessary exposure

Hardening addresses these weaknesses before attackers can exploit them.

---

# Business Impact

Windows hardening provides:

- Reduced attack surface
- Improved compliance
- Lower operational risk
- Better resilience
- Fewer security incidents
- Simplified management
- Stronger customer confidence

---

# Enterprise Best Practices

- Adopt standardized security baselines.
- Apply least privilege across all accounts.
- Remove unnecessary software and services.
- Enable security features by default.
- Test all hardening changes before production deployment.
- Document configuration standards.
- Continuously monitor compliance.
- Automate baseline deployment where possible.
- Review hardening standards regularly.
- Align hardening with business requirements.

---

# Practical Labs

## Lab 1 — Identify the Attack Surface

List every possible attack surface on a Windows workstation, including:

- Services
- Ports
- Applications
- Remote management
- User accounts

Prioritize items that should be reviewed for hardening.

---

## Lab 2 — Compare Default vs Hardened Configuration

Create a comparison table showing:

- Default Windows settings
- Recommended hardened settings
- Business justification

---

## Lab 3 — Review Running Services

Run:

```powershell
Get-Service
```

Identify services that may not be required in a typical enterprise workstation environment.

> Note: Do not disable services on production systems without testing and organizational approval.

---

## Lab 4 — Design a Security Baseline

Create a baseline for employee workstations including:

- Firewall
- BitLocker
- Windows Defender
- Password policy
- Logging
- Automatic updates

Explain why each control is included.

---

# Key Takeaways

- Windows hardening reduces the operating system's attack surface.
- Security baselines provide standardized secure configurations.
- Least privilege is a fundamental hardening principle.
- Hardening is an ongoing lifecycle, not a one-time activity.
- Enterprise hardening should balance security with business functionality.
- Consistent baselines simplify compliance and administration.

---

# Interview Questions

1. What is Windows hardening?
2. Why is attack surface reduction important?
3. What is the principle of least privilege?
4. Why should organizations use security baselines?
5. What is included in a Windows security baseline?
6. How does hardening improve compliance?
7. Why should hardening changes be tested before deployment?
8. What are common areas of Windows hardening?
9. How does hardening support defense in depth?
10. Why is Windows hardening considered a continuous process?

---

# References

- Microsoft Learn
- Microsoft Security Baselines Documentation
- Microsoft Defender Documentation
- Microsoft Security Compliance Toolkit
- NIST SP 800-53
- NIST Cybersecurity Framework
- CIS Microsoft Windows Benchmarks
- CIS Controls v8
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 22-Windows-Hardening.md

# Part 2 — Account Hardening, Authentication Security, Credential Protection, Windows Defender, BitLocker, and Secure Configuration

---

# Introduction

Compromising user credentials is one of the most common techniques used by attackers after gaining initial access to a Windows system.

Because identity is the primary security boundary in modern Windows environments, protecting accounts, authentication mechanisms, and stored credentials is one of the most important aspects of system hardening.

This section focuses on:

- Account security
- Authentication hardening
- Credential protection
- Microsoft Defender security features
- BitLocker
- Secure configuration practices

---

# Account Hardening

Account hardening limits the opportunities for attackers to misuse user or administrator accounts.

Objectives include:

- Reducing privileged accounts
- Enforcing strong authentication
- Limiting administrative access
- Monitoring account activity
- Protecting credentials

---

# Types of Windows Accounts

| Account Type | Purpose |
|--------------|----------|
| Standard User | Daily activities |
| Local Administrator | Local administration |
| Domain User | Enterprise authentication |
| Domain Administrator | Enterprise administration |
| Service Account | Application and service execution |
| Managed Service Account (MSA/gMSA) | Automated service authentication |

Each account type should receive only the permissions required for its role.

---

# Administrator Account Hardening

Recommendations:

- Rename the built-in Administrator account where organizational policy permits.
- Use a separate administrative account for privileged tasks.
- Do not use administrative accounts for email or web browsing.
- Require MFA where supported.
- Monitor administrative logons.
- Remove unused administrator accounts.

Administrative accounts should be tightly controlled.

---

# Local Administrator Management

Risks of shared local administrator passwords include:

- Lateral movement
- Credential reuse
- Difficult auditing

Enterprise environments commonly use:

- Windows Local Administrator Password Solution (Windows LAPS)
- Managed administrative accounts
- Privileged Identity Management (PIM)

These solutions reduce credential exposure and improve accountability.

---

# Least Privilege

Users should perform daily work using standard user accounts.

Example:

```text
Employee

↓

Standard User

↓

Administrative Task Required

↓

Temporary Elevation

↓

Task Complete

↓

Return to Standard User
```

This limits the impact of malware and accidental changes.

---

# Password Policy

A strong password policy includes:

- Minimum length
- Password complexity (where appropriate for organizational policy)
- Password history
- Maximum failed logon attempts
- Account lockout
- Password expiration (as dictated by organizational policy and current guidance)

Organizations should balance usability with security and follow current password management recommendations.

---

# Account Lockout Policy

Example configuration:

| Setting | Example |
|----------|----------|
| Failed attempts | 5 |
| Lockout duration | 15 minutes |
| Reset counter | 15 minutes |

Account lockout policies help reduce online password guessing attacks.

---

# Multi-Factor Authentication (MFA)

MFA requires two or more authentication factors.

Examples:

```text
Password

+

Authenticator App
```

or

```text
Password

+

Smart Card
```

or

```text
Windows Hello

+

PIN
```

MFA significantly reduces the effectiveness of stolen passwords.

---

# Windows Hello for Business

Windows Hello replaces passwords with stronger authentication.

Authentication methods include:

- PIN
- Fingerprint
- Facial recognition
- Security key

Benefits:

- Reduced password exposure
- Faster authentication
- TPM integration
- Phishing resistance (depending on deployment)

---

# Credential Guard

Credential Guard protects credentials stored in memory using virtualization-based security (VBS).

Architecture:

```text
Windows

↓

Virtualization-Based Security

↓

Isolated Credential Storage

↓

LSASS Protection
```

Credential Guard helps mitigate credential theft techniques such as Pass-the-Hash.

---

# Local Security Authority (LSASS)

LSASS is responsible for:

- User authentication
- Security policy enforcement
- Credential management

Because LSASS stores sensitive authentication material, it is a common target for attackers.

Hardening measures include:

- Credential Guard
- LSASS protection
- Limiting administrative access
- Endpoint protection

---

# Pass-the-Hash

Pass-the-Hash attacks use stolen password hashes instead of plaintext passwords.

Workflow:

```text
Compromised System

↓

Password Hash

↓

Reuse Hash

↓

Authenticate

↓

Lateral Movement
```

Mitigations include:

- Credential Guard
- Least privilege
- Restricted administrative access
- MFA
- Network segmentation

---

# Pass-the-Ticket

Attackers may also steal Kerberos tickets.

Example:

```text
User Logs In

↓

Kerberos Ticket

↓

Ticket Theft

↓

Unauthorized Authentication
```

Protecting privileged accounts and limiting ticket exposure reduce this risk.

---

# Microsoft Defender Antivirus

Microsoft Defender Antivirus provides built-in endpoint protection.

Capabilities include:

- Malware detection
- Real-time protection
- Cloud-based protection
- Behavior monitoring
- Automatic remediation

Defender should remain enabled unless replaced by an approved enterprise endpoint protection solution.

---

# Microsoft Defender SmartScreen

SmartScreen helps protect users from:

- Malicious downloads
- Phishing websites
- Untrusted applications

Workflow:

```text
Download

↓

SmartScreen Reputation Check

↓

Trusted?

↓

Allow or Warn
```

---

# Tamper Protection

Tamper Protection helps prevent unauthorized modification of Microsoft Defender security settings.

Examples:

- Disable antivirus
- Disable real-time protection
- Modify security configuration

Restricting these changes helps maintain endpoint protection.

---

# Microsoft Defender Attack Surface Reduction (ASR)

ASR rules help block common attack techniques.

Examples include:

- Blocking Office applications from creating child processes
- Blocking executable content from email
- Blocking credential stealing
- Restricting script abuse

ASR should be tested before organization-wide deployment to avoid application compatibility issues.

---

# BitLocker Drive Encryption

BitLocker encrypts data stored on Windows drives.

Benefits:

- Protects lost or stolen devices
- Encrypts operating system volumes
- Encrypts fixed data drives
- Supports removable media (BitLocker To Go)

Encryption protects data even if physical devices are compromised.

---

# BitLocker Architecture

```text
Windows

↓

TPM

↓

Encryption Key

↓

Encrypted Drive
```

The Trusted Platform Module (TPM) securely stores cryptographic material used during system startup.

---

# TPM (Trusted Platform Module)

TPM provides:

- Secure key storage
- Secure boot support
- Device identity
- Measured boot
- BitLocker integration

Modern enterprise systems typically include TPM 2.0 hardware.

---

# BitLocker Recovery Keys

Recovery keys should be stored securely.

Examples:

- Active Directory
- Microsoft Entra ID
- Enterprise key management systems
- Approved offline escrow

Recovery information should be protected with the same care as other sensitive credentials.

---

# Secure Boot

Secure Boot verifies trusted boot components before loading the operating system.

```text
Firmware

↓

Signature Verification

↓

Trusted Boot Loader

↓

Windows Starts
```

Secure Boot helps defend against bootkits and certain firmware-level attacks.

---

# Virtualization-Based Security (VBS)

VBS uses hardware virtualization to isolate sensitive security components.

Features built on VBS include:

- Credential Guard
- Hypervisor-Protected Code Integrity (HVCI)
- Secure Kernel

VBS strengthens protection against kernel-level attacks.

---

# Hypervisor-Protected Code Integrity (HVCI)

HVCI validates kernel-mode code before execution.

Benefits:

- Prevents unsigned kernel drivers
- Reduces kernel exploitation
- Improves platform integrity

Compatibility testing should be performed before enabling HVCI across all systems.

---

# Enterprise Secure Configuration

Recommended endpoint configuration:

- Windows Defender enabled
- Firewall enabled
- BitLocker enabled
- Secure Boot enabled
- TPM enabled
- Credential Guard enabled (where supported)
- Automatic updates enabled
- PowerShell logging enabled

Standardized configurations improve enterprise security.

---

# Enterprise Example

A healthcare organization deploys Windows laptops configured with:

- Windows Hello for Business
- BitLocker with TPM
- Credential Guard
- Microsoft Defender Antivirus
- Defender ASR rules
- SmartScreen
- Windows LAPS
- Secure Boot

If a laptop is stolen, the encrypted drive and protected credentials significantly reduce the risk of data exposure.

---

# Cybersecurity Perspective

Identity-focused attacks remain among the most common techniques observed in enterprise incidents.

Examples include:

- Password spraying
- Credential stuffing
- Pass-the-Hash
- Kerberos abuse
- Privilege escalation

Hardening identity and authentication significantly reduces attacker opportunities.

---

# Business Impact

Authentication hardening provides:

- Reduced credential theft
- Stronger endpoint security
- Improved regulatory compliance
- Better protection of sensitive information
- Lower incident response costs
- Increased user trust

---

# Enterprise Best Practices

- Require MFA for privileged accounts.
- Use Windows Hello for Business where appropriate.
- Deploy Windows LAPS for local administrator management.
- Enable BitLocker with TPM.
- Store BitLocker recovery keys securely.
- Enable Credential Guard and VBS where supported.
- Keep Microsoft Defender updated.
- Test ASR rules before broad deployment.
- Audit privileged account usage regularly.
- Review authentication policies periodically.

---

# Practical Labs

## Lab 1 — Review Local Administrators

Run:

```powershell
Get-LocalGroupMember `
-Group Administrators
```

Identify accounts with administrative privileges and determine whether they are required.

---

## Lab 2 — Verify BitLocker Status

Run:

```powershell
manage-bde -status
```

Document:

- Encryption status
- Protection status
- Volume type

---

## Lab 3 — Review Windows Security Features

Using Windows Security, verify whether the following are enabled:

- Microsoft Defender Antivirus
- Firewall
- SmartScreen
- Tamper Protection

Record any recommendations.

---

## Lab 4 — Design an Authentication Baseline

Create a security baseline specifying:

- Password policy
- MFA requirements
- Windows Hello deployment
- BitLocker configuration
- Local administrator management
- Credential protection controls

Explain how each recommendation reduces organizational risk.

---

# Key Takeaways

- Identity protection is central to Windows hardening.
- Least privilege reduces the impact of compromised accounts.
- Credential Guard helps protect authentication secrets.
- BitLocker protects data at rest using strong encryption.
- Secure Boot and TPM improve platform integrity.
- Microsoft Defender features provide layered endpoint protection.

---

# Interview Questions

1. Why is least privilege important?
2. What is Credential Guard?
3. How does BitLocker protect data?
4. What is the role of the TPM?
5. Explain Pass-the-Hash attacks.
6. What is Windows Hello for Business?
7. What is Tamper Protection?
8. Why should BitLocker recovery keys be protected?
9. What is Virtualization-Based Security (VBS)?
10. How do ASR rules improve security?

---

# References

- Microsoft Learn
- Microsoft Defender Documentation
- Microsoft BitLocker Documentation
- Microsoft Windows Hello for Business Documentation
- Microsoft Credential Guard Documentation
- Microsoft Security Baselines
- NIST SP 800-53
- CIS Microsoft Windows Benchmarks
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

**Next:** **Part 3 — Service Hardening, Network Hardening, Application Control, Patch Management, Logging, Monitoring, and Security Auditing**