# Eradication and Recovery

> **An enterprise guide to removing attacker access and persistence, restoring trustworthy systems, validating security controls, and safely returning affected environments to normal operations.**

---

# Overview

Eradication and recovery are the phases in which the organization moves from:

> **"The attacker has been contained."**

to:

> **"The attacker has been removed and the environment is trustworthy again."**

Containment limits the incident.

Eradication removes the underlying cause and attacker presence.

Recovery restores systems and services safely.

```text
Incident
   │
   ▼
Detection
   │
   ▼
Analysis
   │
   ▼
Containment
   │
   ▼
Eradication
   │
   ▼
Recovery
   │
   ▼
Validation
   │
   ▼
Normal Operations
```

These phases should not be treated as independent activities.

For example:

```text
Containment
     │
     ├── Investigation
     │
     ├── Evidence Collection
     │
     └── Eradication Planning
              │
              ▼
          Recovery
              │
              ▼
        Validation
```

---

# Why It Matters

Containment does not necessarily mean that the attacker has been removed.

An attacker may have established:

- Malware
- Scheduled tasks
- Services
- Startup persistence
- Web shells
- Backdoors
- SSH keys
- OAuth applications
- Cloud access keys
- New accounts
- Privileged memberships
- Registry persistence
- Cron jobs
- Modified security controls

If the organization restores a system without removing persistence:

```text
Compromise
   │
   ▼
Containment
   │
   ▼
Recovery
   │
   ▼
Attacker Reconnects
   │
   ▼
Reinfection
```

This creates a **containment failure and recovery failure**.

---

# Eradication vs Recovery

## Eradication

Removes the cause and attacker presence.

Examples:

- Remove malware
- Remove persistence
- Remove unauthorized accounts
- Revoke stolen credentials
- Remove malicious services
- Patch exploited vulnerabilities

## Recovery

Returns affected systems to trusted operational state.

Examples:

- Restore from clean backup
- Rebuild systems
- Reinstall applications
- Restore data
- Reconnect networks
- Monitor restored assets

```text
Eradication
     │
     ▼
Trusted State
     │
     ▼
Recovery
     │
     ▼
Operational State
```

---

# Core Objectives

Eradication should:

- Remove attacker persistence
- Remove malicious software
- Eliminate unauthorized access
- Close exploited vulnerabilities
- Rotate compromised secrets
- Remove unauthorized privileges
- Correct security misconfigurations
- Prevent reinfection

Recovery should:

- Restore trusted systems
- Restore business services
- Validate system integrity
- Confirm security controls
- Monitor for recurrence
- Return systems gradually to production

---

# Eradication Strategy

A mature eradication process looks like:

```text
Identify Root Cause
       │
       ▼
Identify Persistence
       │
       ▼
Identify Compromised Credentials
       │
       ▼
Identify Vulnerability
       │
       ▼
Remove Attacker Access
       │
       ▼
Patch / Harden
       │
       ▼
Validate
```

---

# Determine the Root Cause

Eradication should address **why the compromise happened**.

Possible causes:

- Phishing
- Vulnerable application
- Weak password
- Credential reuse
- Exposed API key
- Misconfigured cloud storage
- Excessive privileges
- Unpatched operating system
- Insecure remote access
- Compromised third party

Example:

```text
Phishing Email
      │
      ▼
Credential Theft
      │
      ▼
Account Compromise
      │
      ▼
Cloud Access
      │
      ▼
Data Access
```

Simply resetting the password does not necessarily fix the phishing weakness.

---

# Persistence Removal

Persistence should be investigated systematically.

## Windows

Potential persistence locations include:

- Services
- Scheduled Tasks
- Registry Run keys
- Startup folders
- WMI subscriptions
- Local accounts
- Group memberships
- Remote management mechanisms

## Linux

Potential persistence locations include:

- Cron
- systemd services
- SSH keys
- Shell profiles
- Startup scripts
- User accounts
- Sudo configuration

## Cloud

Potential persistence includes:

- Access keys
- Service principals
- OAuth applications
- IAM roles
- Automation identities
- Serverless functions
- Scheduled jobs

---

# Windows Persistence Investigation

List services:

```powershell
Get-Service
```

Inspect scheduled tasks:

```powershell
Get-ScheduledTask
```

Inspect local users:

```powershell
Get-LocalUser
```

Inspect local administrators:

```powershell
Get-LocalGroupMember Administrators
```

Registry locations should be reviewed according to organizational forensic procedures.

---

# Linux Persistence Investigation

List services:

```bash
systemctl list-units --type=service
```

Inspect cron configuration:

```bash
crontab -l
```

Inspect system-wide cron locations:

```bash
ls -la /etc/cron.*
```

Inspect users:

```bash
cat /etc/passwd
```

Inspect SSH authorization:

```bash
find ~/.ssh -maxdepth 2 -type f
```

These commands should be used only on systems where you have authorization.

---

# Malware Removal

Malware eradication can involve:

- Quarantine
- Removal
- Reimaging
- Rebuilding
- Restoring clean versions

The appropriate strategy depends on confidence in system integrity.

---

# When to Reimage

Reimaging is often preferable when:

- Root-level compromise is suspected
- System integrity cannot be trusted
- Persistence is extensive
- Malware scope is uncertain
- Recovery from a known-good image is practical

Conceptually:

```text
Compromised System
       │
       ▼
Evidence Collection
       │
       ▼
Trusted Image
       │
       ▼
Rebuild
       │
       ▼
Patch
       │
       ▼
Harden
       │
       ▼
Validate
```

---

# When Cleaning May Be Appropriate

Cleaning may be appropriate when:

- Scope is well understood
- Compromise is limited
- System integrity can be validated
- Rebuild would create disproportionate operational impact
- Organizational procedures support it

However:

> **A system that cannot be trusted should not be considered clean simply because the obvious malware file was deleted.**

---

# Credential Remediation

Credentials must be considered across the entire attack path.

```text
Compromised Endpoint
       │
       ├── User Password
       ├── Browser Credentials
       ├── Service Credentials
       ├── API Keys
       └── Cloud Tokens
```

Potential remediation:

- Reset passwords
- Rotate service credentials
- Revoke sessions
- Rotate API keys
- Rotate cloud keys
- Replace SSH keys
- Reissue certificates
- Review privileged accounts

---

# Credential Blast Radius

If an administrator account was compromised:

```text
Admin Account
     │
     ├── Server Access
     ├── Database Access
     ├── Cloud Access
     ├── Security Tools
     └── Network Access
```

The organization should investigate all systems accessible by that identity.

---

# Privilege Remediation

Review:

- Administrative groups
- IAM roles
- Service accounts
- Sudo permissions
- Application permissions
- API scopes
- Cloud policies

Remove privileges that were:

- Added by the attacker
- No longer necessary
- Excessive
- Associated with compromised identities

---

# Patch the Root Cause

If exploitation occurred through a vulnerability:

```text
Vulnerability
     │
     ▼
Exploit
     │
     ▼
Compromise
```

Recovery should not simply restore the vulnerable system.

Instead:

```text
Vulnerability
     │
     ▼
Patch / Mitigate
     │
     ▼
Validate
     │
     ▼
Restore Service
```

---

# Security Configuration Remediation

Review relevant controls:

- Firewall
- EDR
- Antivirus
- MFA
- IAM
- Logging
- Network segmentation
- Application security
- Endpoint hardening

The incident should improve the environment rather than simply return it to its previous insecure state.

---

# Data Integrity

Eradication and recovery must consider whether data was modified.

Potential checks:

- File integrity
- Database integrity
- Configuration integrity
- Application integrity
- Backup integrity
- Security log integrity

Example:

```text
Known-Good State
      │
      ▼
Compare
      │
      ├── Expected Changes
      │
      └── Unexpected Changes
```

---

# Backup Strategy

Backups are critical during recovery.

A mature backup architecture should consider:

```text
Production
    │
    ▼
Backup
    │
    ├── Offline
    ├── Immutable
    └── Separate Credentials
```

Backups should be protected from the same compromise affecting production.

---

# Backup Validation

A backup existing does not mean it is usable.

Validate:

- Backup completeness
- Backup age
- Integrity
- Restoration process
- Application consistency
- Security state

Test restores regularly.

---

# Recovery Point Objective

**RPO** describes how much data loss the organization can tolerate.

Example:

```text
Last Good Backup
      │
      ├──────────► Incident
      │
      ▼
Potential Data Loss
```

An RPO of 4 hours means the organization may accept up to approximately four hours of data loss under the defined recovery model.

---

# Recovery Time Objective

**RTO** describes the targeted time to restore a service.

```text
Incident
   │
   ▼
Recovery Starts
   │
   ▼
Service Restored
```

Organizations should define RTOs according to business requirements.

---

# Recovery Architecture

```text
             Incident
                │
                ▼
           Containment
                │
                ▼
           Eradication
                │
                ▼
         Trusted Baseline
                │
       ┌────────┴────────┐
       ▼                 ▼
   Restore Data       Rebuild Host
       │                 │
       └────────┬────────┘
                ▼
            Validation
                │
                ▼
         Controlled Return
                │
                ▼
          Normal Operations
```

---

# Recovery Validation

Before returning a system to production, validate:

```text
[ ] Malware removed
[ ] Persistence removed
[ ] Credentials remediated
[ ] Vulnerability patched
[ ] Security controls active
[ ] Logging working
[ ] EDR active
[ ] Network access validated
[ ] Application functioning
[ ] Data integrity verified
```

---

# Controlled Recovery

Avoid restoring everything simultaneously when possible.

A safer model:

```text
Critical Systems
      │
      ▼
Restore
      │
      ▼
Validate
      │
      ▼
Monitor
      │
      ▼
Next Systems
```

This allows the response team to detect recurrence before the entire environment is restored.

---

# Recovery Monitoring

Monitoring should continue after restoration.

Potential telemetry:

- Authentication
- Process creation
- Network traffic
- DNS
- Endpoint alerts
- Cloud API activity
- File modifications
- Privilege changes

```text
Recovery
   │
   ▼
Enhanced Monitoring
   │
   ├── Clean
   │
   └── Suspicious Activity
           │
           ▼
       Reinvestigate
```

---

# Recovery Watch Period

Organizations may define an enhanced monitoring period after recovery.

For example:

```text
Recovery
   │
   ▼
24h / 72h / Organization-defined Period
   │
   ▼
Enhanced Monitoring
```

The duration should depend on the incident.

---

# Recompromise Detection

One of the most important recovery questions is:

> "Did the attacker actually leave?"

Look for:

- Recreated accounts
- Reappearing scheduled tasks
- Recreated services
- Repeated C2
- New credentials
- Suspicious authentication
- New cloud identities
- Recurring malicious processes

---

# Recovery Failure

Recovery has failed if:

```text
Restored System
      │
      ▼
Attacker Activity Returns
      │
      ▼
Recompromise
```

Possible causes:

- Persistence missed
- Credential not rotated
- Vulnerability not patched
- Another host remained compromised
- Backup was contaminated
- Attacker retained cloud access
- Security controls were not restored

---

# Recovery Decision Gate

Before returning to production:

```text
Is the root cause understood?
        │
       YES
        │
Are persistence mechanisms removed?
        │
       YES
        │
Are credentials remediated?
        │
       YES
        │
Are security controls functioning?
        │
       YES
        │
Is monitoring active?
        │
       YES
        │
        ▼
   Restore Service
```

If critical answers are unknown, recovery may need to pause.

---

# Business Continuity

Security recovery must account for business operations.

Questions:

- Which services are critical?
- Which systems can remain offline?
- What temporary controls are available?
- Which dependencies must be restored first?
- Who approves service restoration?

Example:

```text
Security
   │
   ├── Risk
   ├── Evidence
   └── Threat
          │
          ▼
Business
   │
   ├── Availability
   ├── Revenue
   └── Customer Impact
```

Recovery decisions should balance both.

---

# Third-Party Dependencies

An incident may involve:

- SaaS
- Cloud providers
- Managed service providers
- Payment processors
- Identity providers
- External APIs

Coordinate recovery with affected third parties when necessary.

---

# Certificate and Secret Rotation

Some incidents require rotation of:

- TLS certificates
- Signing keys
- API secrets
- Encryption keys
- Application secrets
- Service credentials

A compromised secret should not remain active simply because the original system has been rebuilt.

---

# Cloud Recovery

Cloud recovery may involve:

```text
Compromised Identity
        │
        ▼
Credential Rotation
        │
        ▼
IAM Remediation
        │
        ▼
Resource Integrity Review
        │
        ▼
Logging Validation
        │
        ▼
Service Recovery
```

Review:

- IAM
- CloudTrail / audit logs
- Security groups
- Network policies
- Storage
- Compute
- Secrets
- Serverless functions
- CI/CD credentials

---

# Active Directory Recovery

For identity incidents, validate:

- Domain administrators
- Enterprise administrators
- Delegated privileges
- Group memberships
- Service accounts
- GPO modifications
- Domain controllers
- Kerberos-related activity
- Replication health

A domain-level compromise requires substantially more extensive recovery than a single endpoint compromise.

---

# Application Recovery

Application recovery should validate:

- Application binaries
- Dependencies
- Configuration
- Secrets
- Database connectivity
- Authentication
- Authorization
- Logging
- Security headers
- WAF controls

---

# Container Recovery

For compromised containers:

```text
Compromised Image
      │
      ▼
Identify Source
      │
      ▼
Build Trusted Image
      │
      ▼
Scan
      │
      ▼
Deploy
      │
      ▼
Monitor
```

Avoid simply restarting a compromised container without understanding the image and underlying environment.

---

# Kubernetes Recovery

Review:

- Images
- Pods
- Deployments
- Nodes
- Service accounts
- Secrets
- RBAC
- Network policies
- Admission controls

A compromised workload may indicate a broader cluster problem.

---

# Common Eradication Mistakes

## 1. Deleting Only the Malware File

Persistence may remain.

## 2. Resetting Only One Password

Other credentials may have been stolen.

## 3. Restoring an Unpatched System

The attacker can exploit the same vulnerability again.

## 4. Restoring from an Untrusted Backup

Malicious content may return.

## 5. Failing to Investigate Persistence

The attacker can reconnect.

## 6. Reconnecting Systems Too Quickly

Recovery may occur before validation.

## 7. Ignoring Cloud Access

Cloud identities may remain compromised.

## 8. Ignoring Service Accounts

Attackers frequently abuse non-human identities.

## 9. Disabling EDR During Recovery

This reduces visibility exactly when monitoring matters.

## 10. Declaring Recovery Complete Too Early

Recovery requires validation.

---

# Detection During Eradication

Detection engineering should continue during eradication.

Potential detections:

```text
New Admin Account
Suspicious Scheduled Task
Unexpected Service
New OAuth Application
New Cloud Access Key
Unusual Authentication
Repeated C2
Unexpected Privilege Change
```

Eradication is not a period where monitoring stops.

---

# Practical Commands

These commands support authorized defensive investigation and validation.

## Windows

### List Services

```powershell
Get-Service
```

### List Scheduled Tasks

```powershell
Get-ScheduledTask
```

### List Local Users

```powershell
Get-LocalUser
```

### List Administrators

```powershell
Get-LocalGroupMember Administrators
```

### Verify Windows Defender Status

```powershell
Get-MpComputerStatus
```

---

# Linux

### System Services

```bash
systemctl list-units --type=service
```

### Running Processes

```bash
ps aux
```

### Network Connections

```bash
ss -tunap
```

### Logged-In Users

```bash
who
```

### Scheduled Jobs

```bash
crontab -l
```

---

# File Integrity

A simple cryptographic hash can help compare files against a known-good reference.

Linux:

```bash
sha256sum <file>
```

PowerShell:

```powershell
Get-FileHash <file> -Algorithm SHA256
```

Hash comparison alone does not prove that a system is clean.

---

# Practical Lab

# Lab — Endpoint Eradication and Recovery

## Scenario

A workstation was compromised through phishing.

Investigation determined:

```text
Initial Access:
Phishing

Execution:
PowerShell

Persistence:
Scheduled Task

Credential Access:
Browser credentials suspected

C2:
Confirmed

Containment:
Host isolated
```

---

# Step 1 — Identify Persistence

Investigate:

```text
Scheduled Tasks
Services
Startup locations
Local accounts
Network connections
```

---

# Step 2 — Remove Persistence

Document:

```text
Persistence Mechanism
Location
Evidence
Removal Action
Validation
```

---

# Step 3 — Credential Remediation

Determine:

```text
User credentials
Browser credentials
Cached credentials
Service credentials
Cloud sessions
```

Apply appropriate credential remediation.

---

# Step 4 — Patch Root Cause

Determine:

```text
How did the attacker gain access?

Was a vulnerability involved?

Was MFA available?

Was the application configured securely?
```

---

# Step 5 — Recovery Decision

Choose between:

```text
Clean and Validate
        OR
Rebuild from Trusted Image
```

Document the reasoning.

---

# Step 6 — Restore

Restore:

- Required applications
- Required data
- Security controls
- Logging
- EDR

---

# Step 7 — Validate

Confirm:

```text
[ ] No persistence
[ ] No malware
[ ] Credentials remediated
[ ] Vulnerability fixed
[ ] EDR active
[ ] Logs working
[ ] Network behavior normal
```

---

# Step 8 — Monitor

Monitor for:

```text
New processes
New persistence
C2
Authentication anomalies
Privilege changes
Suspicious DNS
```

---

# Advanced Lab — Enterprise Recovery

## Scenario

An attacker compromised:

```text
USER-101
     │
     ▼
WS-101
     │
     ▼
ADMIN-ACCOUNT
     │
     ▼
SERVER-01
     │
     ▼
DATABASE-01
```

The organization has:

- EDR
- SIEM
- Active Directory
- Cloud infrastructure
- Immutable backups

---

## Task

Design a recovery strategy covering:

1. Identity
2. Endpoints
3. Servers
4. Database
5. Cloud
6. Credentials
7. Backups
8. Monitoring

---

## Expected Architecture

```text
             Compromise
                 │
                 ▼
             Containment
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    Identity   Endpoint   Network
       │         │         │
       └─────────┼─────────┘
                 ▼
            Eradication
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    Rebuild    Restore   Harden
       │         │         │
       └─────────┼─────────┘
                 ▼
             Validation
                 │
                 ▼
        Enhanced Monitoring
                 │
                 ▼
          Normal Operations
```

---

# Recovery Checklist

## Eradication

```text
[ ] Root cause identified
[ ] Malware identified
[ ] Persistence identified
[ ] Persistence removed
[ ] Unauthorized accounts removed
[ ] Unauthorized privileges removed
[ ] Credentials rotated
[ ] Vulnerabilities patched
[ ] Security configuration corrected
```

## Recovery

```text
[ ] Trusted backup selected
[ ] Backup integrity validated
[ ] System rebuilt/restored
[ ] Data integrity checked
[ ] EDR restored
[ ] Logging restored
[ ] Network controls restored
[ ] Application validated
[ ] Business owner approval obtained
```

## Post-Recovery

```text
[ ] Enhanced monitoring enabled
[ ] IOC monitoring active
[ ] Authentication monitoring active
[ ] Persistence monitoring active
[ ] Cloud monitoring active
[ ] Incident record updated
[ ] Recovery formally closed
```

---

# Professional Eradication and Recovery Record

```text
Incident ID:
________________________

Root Cause:
________________________

Affected Systems:
________________________

Persistence Identified:
________________________

Credentials Compromised:
________________________

Eradication Actions:
________________________

Patch / Configuration Changes:
________________________

Recovery Method:
[ ] Rebuild
[ ] Restore
[ ] Clean
[ ] Other

Backup Used:
________________________

Validation Performed:
________________________

Monitoring Period:
________________________

Business Owner:
________________________

Security Approval:
________________________

Recovery Date:
________________________
```

---

# Recovery Metrics

## Mean Time to Recover

Measures the time required to restore affected services.

## Recompromise Rate

Measures how often recovered systems become compromised again.

## Recovery Validation Failure Rate

Measures how frequently restored systems fail security validation.

## Backup Restore Success Rate

Measures whether backups can actually support recovery.

## Credential Remediation Coverage

Measures the percentage of identified compromised credentials successfully remediated.

---

# Eradication and Recovery Maturity

## Level 1 — Reactive

- Manual cleanup
- Ad hoc recovery
- Limited backup testing

## Level 2 — Repeatable

- Recovery procedures
- Standard rebuild process
- Basic credential rotation

## Level 3 — Defined

- Trusted images
- Tested recovery plans
- Formal validation

## Level 4 — Measured

- Recovery metrics
- Backup restoration testing
- Recompromise monitoring

## Level 5 — Optimized

- Automated recovery workflows
- Immutable infrastructure
- Continuous validation
- Rapid rebuild capability
- Identity-aware recovery
- Automated security verification

---

# Interview Questions

## 1. What is eradication?

Eradication is the process of removing malware, persistence, unauthorized access, compromised credentials, vulnerabilities, and other causes of attacker presence.

---

## 2. What is the difference between eradication and recovery?

Eradication removes the threat.

Recovery restores affected systems and services to a trusted operational state.

---

## 3. When would you reimage a system instead of cleaning it?

Reimaging may be preferred when:

- Root-level compromise is suspected
- System integrity cannot be trusted
- Persistence is extensive
- Scope is uncertain
- A trusted rebuild process exists

---

## 4. Why should credentials be rotated during eradication?

Because attackers may have stolen credentials that remain usable even after the compromised endpoint is removed.

---

## 5. Why are service accounts important?

Service accounts often have persistent access and may possess significant privileges. Attackers can abuse them for continued access.

---

## 6. What is RTO?

Recovery Time Objective defines the targeted time for restoring a service after disruption.

---

## 7. What is RPO?

Recovery Point Objective describes the acceptable amount of data loss measured relative to the recovery point.

---

## 8. Why should backups be protected during ransomware incidents?

Attackers frequently attempt to compromise or destroy backups to prevent recovery.

---

## 9. How do you know eradication succeeded?

Evidence should show that:

- Persistence is removed
- Credentials are remediated
- Root cause is fixed
- Malicious activity has stopped
- Security controls are restored
- Monitoring shows no recurrence

---

## 10. Why should systems be monitored after recovery?

Attackers may have established persistence that was initially missed, or another compromised system may still provide access.

---

## 11. What happens if you recover before fixing the root cause?

The organization may simply recreate the conditions that allowed the original compromise.

---

## 12. What is a trusted image?

A known-good system image whose origin, configuration, security state, and integrity are sufficiently understood and validated for organizational use.

---

## 13. How would you recover from a ransomware incident?

A high-level approach:

```text
Contain
  ↓
Preserve Evidence
  ↓
Determine Scope
  ↓
Protect Backups
  ↓
Secure Identity
  ↓
Eradicate
  ↓
Validate Backups
  ↓
Rebuild / Restore
  ↓
Validate
  ↓
Monitor
```

---

## 14. How would you recover from cloud credential compromise?

Potential actions include:

```text
Revoke Sessions
Rotate Keys
Remove Unauthorized Roles
Review API Activity
Validate Resources
Check Persistence
Restore Secure Configuration
Monitor
```

---

# Integration With Other Security Functions

## SOC

Provides:

- Detection
- Alerting
- Monitoring

## Incident Response

Provides:

- Investigation
- Eradication
- Recovery coordination

## Threat Hunting

Provides:

- Persistence discovery
- Recompromise detection
- Environment-wide searches

## Detection Engineering

Provides:

- New detections
- Recovery monitoring
- Control validation

## Vulnerability Management

Provides:

- Root cause remediation
- Patch verification

## Identity Security

Provides:

- Credential remediation
- Privilege review
- Session management

---

# Enterprise Eradication Architecture

```text
                  Incident
                     │
                     ▼
               Investigation
                     │
                     ▼
                Containment
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Identity    Endpoint   Network
          │          │          │
          └──────────┼──────────┘
                     ▼
                 Eradication
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Malware    Identity    Vulnerability
        Removal   Remediation   Fix
          │          │          │
          └──────────┼──────────┘
                     ▼
                  Recovery
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       Restore     Rebuild    Validate
          │          │          │
          └──────────┼──────────┘
                     ▼
              Enhanced Monitoring
                     │
                     ▼
              Normal Operations
```

---

# Key Takeaways

Eradication and recovery should never be treated as simply:

> **Delete malware → reboot → resume work.**

A mature process is:

```text
Understand Root Cause
        ↓
Identify Persistence
        ↓
Remediate Credentials
        ↓
Fix Vulnerabilities
        ↓
Remove Attacker Access
        ↓
Restore Trusted State
        ↓
Validate
        ↓
Monitor
        ↓
Return to Operations
```

The most important principles are:

- Remove the attacker, not just the visible malware.
- Investigate persistence before declaring eradication complete.
- Rotate compromised credentials and secrets.
- Fix the vulnerability or weakness that enabled the attack.
- Use trusted backups and images.
- Protect backups from the incident.
- Validate restored systems.
- Restore security controls before production service.
- Monitor aggressively after recovery.
- Treat recurrence as evidence that eradication may be incomplete.

> **Recovery is successful only when the organization can demonstrate that the environment is both operational and trustworthy.**

---

# References

### NIST

Computer Security Incident Handling Guide:

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

NIST Cybersecurity Framework:

https://www.nist.gov/cyberframework

### CISA

Cybersecurity guidance and incident response resources:

https://www.cisa.gov/

Ransomware guidance:

https://www.cisa.gov/stopransomware

### MITRE ATT&CK

Persistence and post-compromise techniques:

https://attack.mitre.org/

### CIS Controls

https://www.cisecurity.org/controls

### FIRST

https://www.first.org/

### SANS

https://www.sans.org/

---

# Chapter Summary

A mature organization does not consider an incident resolved simply because malicious activity has stopped.

It must demonstrate:

```text
Threat Removed
     +
Persistence Removed
     +
Credentials Secured
     +
Root Cause Fixed
     +
Systems Restored
     +
Security Controls Validated
     +
Monitoring Active
```

Only then should the organization transition toward formal post-incident review.

> **Eradication removes the adversary's foothold. Recovery restores trust. Validation proves that both were successful.**
