# 18 - Linux Security

# Part 1 — Linux Security Fundamentals, Security Principles, Threat Landscape, Authentication, Password Security, and PAM

---

# Introduction

Linux is widely regarded as one of the most secure operating systems available.

It powers:

- Internet infrastructure
- Cloud platforms
- Enterprise servers
- Banking systems
- Government infrastructure
- Supercomputers
- Kubernetes clusters
- Security appliances
- IoT devices

However, **Linux is not secure by default**.

Security depends on:

- Proper configuration
- Regular updates
- Least privilege
- Continuous monitoring
- Secure administration
- User awareness

Poorly configured Linux systems are vulnerable regardless of the operating system itself.

---

# Learning Objectives

After completing this chapter, you will understand:

- Linux security fundamentals
- Core security principles
- Common attack vectors
- Authentication mechanisms
- Password security
- PAM (Pluggable Authentication Modules)
- Enterprise security models
- Defense-in-depth

---

# What is Linux Security?

Linux security is the practice of protecting:

- Users
- Data
- Applications
- Services
- Networks
- Storage
- Kernel
- Hardware

Goals include:

- Prevent unauthorized access
- Protect sensitive information
- Maintain service availability
- Preserve system integrity
- Support compliance requirements

---

# Security Goals (CIA Triad)

Every security control ultimately supports one or more of these goals.

```text
Confidentiality

↓

Integrity

↓

Availability
```

---

## Confidentiality

Protect information from unauthorized disclosure.

Examples:

- File permissions
- Encryption
- Access controls
- VPNs

---

## Integrity

Ensure data remains accurate and unmodified.

Examples:

- Checksums
- Digital signatures
- File integrity monitoring
- Version control

---

## Availability

Ensure systems remain accessible.

Examples:

- Backups
- High availability
- Redundancy
- Monitoring
- Disaster recovery

---

# Additional Security Principles

Large organizations also consider:

- Authenticity
- Accountability
- Non-repudiation
- Auditability

---

# Security Architecture

```text
Users

↓

Authentication

↓

Authorization

↓

Applications

↓

Kernel

↓

Hardware

↓

Data
```

Multiple layers reduce the impact of individual failures.

---

# Defense in Depth

Security should not rely on a single control.

```text
Firewall

↓

Authentication

↓

Permissions

↓

SELinux/AppArmor

↓

Logging

↓

Monitoring

↓

Incident Response
```

If one layer fails, additional controls continue to provide protection.

---

# Principle of Least Privilege

Every user, application, and service should receive **only the permissions required** to perform its tasks.

Examples:

✔ Good

```text
Web server

↓

Read web files

↓

Cannot modify system files
```

✘ Poor

```text
Web server

↓

Runs as root

↓

Full system access
```

Benefits:

- Limits damage
- Reduces attack surface
- Simplifies auditing
- Improves compliance

---

# Separation of Duties

Critical tasks should be divided among multiple roles.

Example:

| Role | Responsibility |
|-------|----------------|
| System Administrator | Infrastructure |
| Database Administrator | Databases |
| Security Team | Monitoring |
| Auditor | Compliance |

---

# Zero Trust

Modern security assumes:

> Never trust, always verify.

Requirements include:

- Strong authentication
- Device verification
- Continuous authorization
- Network segmentation
- Logging and monitoring

---

# Linux Threat Landscape

Linux systems face many types of threats.

---

## External Threats

Examples:

- SSH brute-force attacks
- Web application attacks
- Remote code execution
- Distributed Denial-of-Service (DDoS)
- Credential theft
- Exploitation of unpatched software

---

## Internal Threats

Examples:

- Insider misuse
- Weak passwords
- Excessive privileges
- Misconfigurations
- Accidental deletion
- Unauthorized software installation

---

## Malware

Examples include:

- Cryptominers
- Ransomware
- Worms
- Backdoors
- Trojans
- Botnet clients

---

# Common Attack Surface

```text
Internet

↓

Firewall

↓

SSH

↓

Web Server

↓

Application

↓

Database

↓

Operating System
```

Each exposed service increases the potential attack surface.

---

# Common Linux Attack Vectors

| Attack | Description |
|----------|-------------|
| Brute Force | Password guessing |
| Credential Theft | Stolen usernames/passwords |
| Privilege Escalation | Gain higher privileges |
| Kernel Exploitation | Exploit kernel vulnerabilities |
| Misconfiguration | Insecure settings |
| Vulnerable Services | Outdated software |
| Supply Chain | Compromised packages or dependencies |
| Social Engineering | User manipulation |

---

# Authentication

Authentication answers:

> "Who are you?"

Linux supports several authentication methods.

Examples:

- Passwords
- SSH public keys
- Smart cards
- Multi-factor authentication (MFA)
- Kerberos
- LDAP
- OAuth/OpenID Connect (application-dependent)

---

# Authentication Workflow

```text
User

↓

Credentials

↓

Authentication

↓

Success

↓

Access Granted
```

Or:

```text
Failure

↓

Access Denied
```

---

# Authentication vs Authorization

| Authentication | Authorization |
|----------------|---------------|
| Identity verification | Permission verification |
| "Who are you?" | "What can you do?" |
| Login | Resource access |

Both are required for secure systems.

---

# Password Security

Passwords remain one of the most common authentication mechanisms.

Strong password policies reduce the risk of:

- Brute-force attacks
- Password spraying
- Credential stuffing
- Guessing attacks

---

# Characteristics of Strong Passwords

Recommended characteristics:

- Long (preferably 14+ characters where policies allow)
- Unique
- Random
- Difficult to guess
- Not reused across services
- Stored in a password manager

---

# Weak Password Examples

```text
password123

admin

welcome

12345678
```

These passwords are easily guessed or appear in common password dictionaries.

---

# Strong Password Example

```text
River!Copper-Cloud27?Orbit
```

A randomly generated password from a reputable password manager is generally even better.

---

# Password Storage

Passwords should **never** be stored in plaintext.

Linux stores password hashes.

Relevant files:

```text
/etc/passwd
```

User account information.

Password hashes:

```text
/etc/shadow
```

Access to `/etc/shadow` is restricted to privileged users.

---

# Understanding `/etc/passwd`

Example:

```text
alice:x:1001:1001:Alice:/home/alice:/bin/bash
```

Fields:

| Field | Description |
|---------|-------------|
| Username | Login name |
| Password placeholder | Usually `x` |
| UID | User ID |
| GID | Primary Group ID |
| Description | GECOS field |
| Home Directory | User home |
| Shell | Login shell |

---

# Understanding `/etc/shadow`

Example:

```text
alice:$y$...:19700:0:99999:7:::
```

Common fields:

| Field | Purpose |
|---------|----------|
| Username | Account name |
| Password hash | Hashed password |
| Last password change | Days since epoch |
| Minimum age | Minimum days before change |
| Maximum age | Maximum password lifetime |
| Warning period | Days before expiration warning |
| Inactive period | Optional account inactivity |
| Expiration | Optional account expiration |

The exact hash format depends on the configured hashing algorithm.

---

# Password Hashing

Modern Linux systems commonly use strong password hashing algorithms such as:

- yescrypt (many modern distributions)
- SHA-512 (older deployments)
- bcrypt (some applications)
- Argon2 (application-dependent)

These algorithms are designed to make password cracking significantly more difficult than simple cryptographic hashes.

---

# Account Locking

Organizations often configure account lockout policies after repeated failed authentication attempts.

Example workflow:

```text
5 Failed Logins

↓

Temporary Lock

↓

Administrator Review
```

Exact thresholds vary according to organizational policy.

---

# Password Aging

Password aging policies may define:

- Minimum password age
- Maximum password age
- Expiration warning period
- Account inactivity period

Display aging information:

```bash
chage -l username
```

---

# Changing Password Policy

Example:

```bash
sudo chage -M 90 username
```

Meaning:

```text
Maximum password age

↓

90 Days
```

---

# Password Complexity

Typical enterprise requirements:

- Uppercase letters
- Lowercase letters
- Numbers
- Special characters
- Minimum length
- Block common passwords
- Prevent password reuse

Many organizations now prioritize **long passphrases** and block compromised passwords rather than relying solely on complex composition rules.

---

# PAM (Pluggable Authentication Modules)

PAM provides a modular authentication framework.

Instead of each application implementing authentication independently, applications use PAM.

---

# PAM Architecture

```text
Application

↓

PAM

↓

Authentication Modules

↓

Authentication Backend

↓

Access Decision
```

---

# Advantages of PAM

- Centralized authentication
- Modular configuration
- Consistent policy enforcement
- Supports MFA integration
- Flexible authentication methods
- Reusable across applications

---

# PAM Module Types

| Module Type | Purpose |
|-------------|----------|
| auth | User authentication |
| account | Account validation |
| password | Password management |
| session | Session setup and teardown |

---

# PAM Control Flags

| Flag | Behavior |
|------|----------|
| required | Must succeed; failures reported after processing |
| requisite | Must succeed; failure stops processing immediately |
| sufficient | Success may allow authentication to complete if no prior required module failed |
| optional | Usually ignored unless it is the only relevant module |

---

# PAM Configuration

Common directory:

```text
/etc/pam.d/
```

Each service can have its own PAM configuration.

Example:

```text
/etc/pam.d/sshd
```

---

# Authentication Flow with PAM

```text
SSH Login

↓

PAM auth

↓

PAM account

↓

PAM session

↓

User Shell
```

---

# Enterprise Authentication Workflow

```text
User

↓

SSH

↓

PAM

↓

Directory Service (Optional)

↓

Authentication

↓

Authorization

↓

Logging

↓

Access
```

Directory services may include LDAP or Active Directory integrations.

---

# Cybersecurity Perspective

Authentication is a primary target for attackers.

Common attack techniques include:

- Password guessing
- Password spraying
- Credential stuffing
- Phishing
- SSH brute-force attacks
- Stolen SSH keys
- MFA fatigue attacks (where MFA is deployed)

Defensive measures include:

- MFA
- Strong password policies
- Account lockout
- Monitoring authentication logs
- SSH key authentication
- Least privilege

---

# Business Impact

Strong authentication and access controls help organizations:

- Prevent unauthorized access
- Protect sensitive data
- Meet regulatory requirements
- Reduce breach risk
- Improve audit readiness
- Maintain customer trust

---

# Enterprise Best Practices

- Enforce least privilege.
- Require MFA for administrative accounts where possible.
- Use SSH keys instead of passwords for remote administration when appropriate.
- Protect `/etc/shadow` and authentication-related files.
- Review inactive accounts regularly.
- Disable unused accounts promptly.
- Audit authentication logs frequently.
- Keep PAM configurations documented and tested.

---

# Key Takeaways

- Linux security relies on layered defenses rather than a single mechanism.
- The CIA Triad underpins most security decisions.
- Authentication verifies identity; authorization determines permissions.
- Passwords should be securely hashed and protected.
- PAM provides a flexible, centralized authentication framework.
- Strong authentication policies significantly reduce organizational risk.

---


# 18 - Linux Security

# Part 2 — File Security, Process Security, Linux Capabilities, SELinux, AppArmor, Kernel Security, and Secure System Configuration

---

# Introduction

Authentication is only the first layer of Linux security.

After a user or service is authenticated, Linux must enforce **what resources can be accessed** and **what actions are permitted**.

This is achieved through multiple security mechanisms including:

- File permissions
- Process isolation
- Linux capabilities
- Mandatory Access Control (MAC)
- Kernel security features
- Secure configuration (Hardening)

Enterprise environments combine these controls to minimize risk and reduce the impact of successful attacks.

---

# Linux Security Layers

```text
Users

↓

Authentication

↓

Authorization

↓

File Permissions

↓

Process Isolation

↓

Capabilities

↓

SELinux / AppArmor

↓

Kernel Security

↓

Hardware
```

---

# File Security

Linux protects files using:

- Ownership
- Permissions
- Access Control Lists (ACLs)
- Extended attributes
- Encryption (where implemented)
- Mandatory Access Control

---

# File Ownership

Every file has:

```text
Owner

↓

Group

↓

Others
```

Example:

```bash
ls -l
```

Output:

```text
-rw-r----- 1 alice developers 2048 Jul 22 report.txt
```

Meaning:

| Field | Value |
|--------|-------|
| Owner | alice |
| Group | developers |
| Permissions | rw-r----- |

---

# Permission Review

Display permissions:

```bash
ls -l
```

Change permissions:

```bash
chmod 640 report.txt
```

Change owner:

```bash
sudo chown alice report.txt
```

Change group:

```bash
sudo chgrp developers report.txt
```

---

# Secure Permission Examples

| File | Recommended Permissions |
|------|--------------------------|
| Private SSH key | `600` |
| SSH directory | `700` |
| `/etc/shadow` | Restricted to privileged users |
| Public web content | Readable by web server as required |
| Backup archives | Restricted to authorized administrators |

Exact permissions depend on organizational requirements.

---

# Special Permission Bits

Linux supports:

| Permission | Purpose |
|------------|----------|
| SUID | Run with owner's effective UID |
| SGID | Run with group's effective GID or inherit group on directories |
| Sticky Bit | Restrict deletion in shared directories |

---

# Sticky Bit Example

Common example:

```text
/tmp
```

Permissions:

```text
drwxrwxrwt
```

Behavior:

Users can remove only:

- Their own files
- Files they own
- Files removable by privileged users

---

# SUID Risk

A SUID program executes with the effective permissions of its owner.

Example:

```text
Normal User

↓

Execute SUID Binary

↓

Temporary Elevated Privileges

↓

Program Ends
```

Misconfigured or vulnerable SUID programs can become privilege escalation vectors.

---

# Finding SUID Files

```bash
find / -perm -4000 -type f 2>/dev/null
```

Review results periodically and investigate unexpected binaries.

---

# Access Control Lists (ACLs)

ACLs provide more granular permissions than standard owner/group/others.

Example:

```bash
setfacl -m u:alice:rwx project.txt
```

View ACLs:

```bash
getfacl project.txt
```

---

# File Integrity

Critical files should be monitored.

Examples:

```text
/etc/passwd

/etc/shadow

/etc/sudoers

/etc/ssh/sshd_config

/etc/fstab
```

Unexpected modifications should trigger investigation.

---

# Process Security

Processes should execute with only the privileges they require.

Each process has:

- Process ID (PID)
- User ID (UID)
- Group ID (GID)
- Memory space
- Environment
- Resource limits

---

# Process Isolation

Linux isolates processes.

```text
Process A

↓

Kernel

↓

Process B
```

A normal user process cannot directly access another process's memory without appropriate privileges.

---

# Viewing Processes

```bash
ps -ef
```

Or:

```bash
top
```

Review:

- Owner
- CPU usage
- Memory usage
- Command

---

# Killing a Process

Graceful termination:

```bash
kill PID
```

Force termination:

```bash
kill -9 PID
```

`SIGKILL` (`-9`) should generally be reserved for situations where a process cannot terminate gracefully.

---

# Process Limits

Display limits:

```bash
ulimit -a
```

Examples:

- Open files
- Stack size
- CPU time
- Memory limits
- Maximum user processes

These limits help protect systems from resource exhaustion.

---

# Linux Capabilities

Traditionally, the root user possessed all administrative privileges.

Linux capabilities divide those privileges into smaller, independently assignable units.

Examples include:

- Network administration
- Loading kernel modules
- Binding to privileged ports
- Changing file ownership

---

# Capability Model

```text
Traditional

Root

↓

Everything
```

```text
Capabilities

Capability A

Capability B

Capability C

↓

Only Required Privileges
```

---

# Viewing Capabilities

Installed capability information:

```bash
getcap /usr/bin/ping
```

Example output:

```text
/usr/bin/ping cap_net_raw=ep
```

List file capabilities:

```bash
getcap -r / 2>/dev/null
```

---

# Advantages of Capabilities

- Reduced privilege
- Smaller attack surface
- Better application isolation
- Improved security

---

# Mandatory Access Control (MAC)

Traditional permissions are **Discretionary Access Control (DAC)**.

MAC adds an additional enforcement layer.

Examples:

- SELinux
- AppArmor

Even if traditional permissions allow access, MAC policies may deny it.

---

# DAC vs MAC

| DAC | MAC |
|------|-----|
| User controls permissions | Policy controls access |
| Flexible | Stronger enforcement |
| Easier to administer | More restrictive |
| Can be bypassed by privileged users | Policy-driven restrictions |

---

# SELinux

SELinux (Security-Enhanced Linux) provides Mandatory Access Control.

Common on:

- Red Hat Enterprise Linux
- CentOS Stream
- Fedora
- Rocky Linux
- AlmaLinux

---

# SELinux Workflow

```text
Application

↓

Permission Check

↓

SELinux Policy

↓

Allow or Deny
```

---

# SELinux Modes

Display current mode:

```bash
getenforce
```

Modes:

| Mode | Behavior |
|------|----------|
| Enforcing | Enforce policy and deny unauthorized actions |
| Permissive | Log violations without enforcing |
| Disabled | SELinux inactive |

---

# Viewing SELinux Status

```bash
sestatus
```

---

# SELinux Contexts

Display contexts:

```bash
ls -Z
```

Example:

```text
system_u:object_r:httpd_sys_content_t:s0
```

Typical fields:

| Field | Purpose |
|--------|----------|
| User | SELinux user |
| Role | Security role |
| Type | Primary access control type |
| Level | MLS/MCS security level |

---

# Why SELinux Matters

Example:

```text
Web Server

↓

Compromised

↓

Attempts to Read

/etc/shadow

↓

SELinux Policy

↓

Denied
```

Even when a service is compromised, SELinux can reduce its ability to access unrelated resources.

---

# AppArmor

AppArmor is another Mandatory Access Control framework.

Common on:

- Ubuntu
- Debian
- SUSE Linux Enterprise

---

# AppArmor Workflow

```text
Application

↓

Profile

↓

Allow

↓

or

↓

Deny
```

---

# Viewing AppArmor Status

```bash
sudo aa-status
```

---

# AppArmor Profiles

Profiles define:

- Allowed files
- Allowed capabilities
- Network access
- Execution permissions

Applications run according to their assigned profiles.

---

# SELinux vs AppArmor

| SELinux | AppArmor |
|----------|-----------|
| Label-based | Path-based |
| Fine-grained control | Simpler profile management |
| Common on RHEL-family systems | Common on Ubuntu/Debian/SUSE |
| Powerful but complex | Easier to learn for many administrators |

---

# Kernel Security

The Linux kernel enforces many security protections.

Examples include:

- Process isolation
- Memory protection
- Address Space Layout Randomization (ASLR)
- Secure module loading
- Namespaces
- Control groups (cgroups)
- Seccomp (application dependent)

---

# Address Space Layout Randomization (ASLR)

ASLR randomizes memory locations.

Without ASLR:

```text
Application

↓

Fixed Memory Address
```

With ASLR:

```text
Application

↓

Randomized Memory Address
```

This increases the difficulty of many memory corruption exploits.

---

# Checking ASLR

```bash
cat /proc/sys/kernel/randomize_va_space
```

Typical values:

| Value | Meaning |
|--------|----------|
| 0 | Disabled |
| 1 | Partial randomization |
| 2 | Full randomization (common default) |

---

# Kernel Modules

Loaded modules:

```bash
lsmod
```

Module information:

```bash
modinfo module_name
```

Kernel modules extend kernel functionality and should be managed carefully.

---

# Secure Boot

Secure Boot helps ensure that only trusted boot components are executed during system startup.

Benefits include:

- Boot integrity
- Reduced boot-time malware risk
- Trusted boot chain

Support depends on hardware and firmware configuration.

---

# Secure Configuration

A secure Linux system should include:

- Minimal installed software
- Strong authentication
- Regular updates
- Secure file permissions
- Firewall configuration
- Logging
- Monitoring
- Backup strategy

---

# Secure Configuration Workflow

```text
Install

↓

Patch

↓

Configure

↓

Harden

↓

Monitor

↓

Audit

↓

Improve
```

---

# Configuration Review

Administrators should regularly review:

- User accounts
- Services
- Open ports
- Installed packages
- Running processes
- Scheduled jobs
- Security policies

---

# Cybersecurity Perspective

Many Linux compromises exploit:

- Misconfigured permissions
- Excessive privileges
- Weak service isolation
- Outdated software
- Missing security controls

Defense mechanisms such as capabilities, SELinux, and AppArmor significantly increase the effort required for successful attacks.

---

# Business Impact

Strong operating system security:

- Protects sensitive information
- Reduces attack surface
- Limits lateral movement
- Supports regulatory compliance
- Improves service reliability
- Reduces incident recovery costs

---

# Enterprise Best Practices

- Apply the principle of least privilege.
- Regularly audit SUID/SGID binaries.
- Use ACLs only when additional granularity is required.
- Enable and maintain SELinux or AppArmor where supported.
- Review Linux capabilities assigned to binaries.
- Keep kernel and security packages updated.
- Remove unnecessary services and software.
- Perform periodic security configuration audits.

---

# Key Takeaways

- File and process security form the foundation of Linux access control.
- Linux capabilities divide root privileges into smaller, more manageable permissions.
- SELinux and AppArmor provide Mandatory Access Control beyond traditional file permissions.
- Kernel security features such as ASLR strengthen exploit resistance.
- Secure configuration and regular auditing are essential components of enterprise Linux security.

---

# 18 - Linux Security

# Part 3 — Security Monitoring, Malware & Rootkits, Vulnerability Management, System Hardening, Incident Response, Enterprise Security Practices, and Compliance

---

# Introduction

Even a properly configured Linux server is **never "finished" from a security perspective**.

New vulnerabilities, configuration drift, software updates, insider threats, and evolving attack techniques require continuous monitoring and improvement.

Enterprise security follows a continuous cycle:

```text
Protect

↓

Monitor

↓

Detect

↓

Investigate

↓

Respond

↓

Recover

↓

Improve
```

---

# Security Monitoring

Security monitoring is the continuous observation of systems to identify:

- Unauthorized access
- Malware activity
- Suspicious processes
- Configuration changes
- Network attacks
- Privilege escalation
- Data exfiltration attempts

Monitoring combines:

- Logs
- Metrics
- Alerts
- Threat intelligence
- Human analysis

---

# Security Monitoring Architecture

```text
Linux Servers

↓

System Logs

↓

Authentication Logs

↓

Firewall Logs

↓

Application Logs

↓

Central Log Server

↓

SIEM

↓

SOC Analysts

↓

Incident Response
```

---

# What Should Be Monitored?

Enterprise Linux systems should monitor:

| Category | Examples |
|-----------|----------|
| Authentication | Failed logins, root logins |
| Processes | Unknown processes |
| Files | Critical configuration changes |
| Services | Unexpected service starts/stops |
| Users | Account creation/deletion |
| Network | New listening ports |
| Kernel | Panic, hardware issues |
| Packages | Unauthorized software changes |

---

# Important Security Logs

| Log | Purpose |
|------|----------|
| `/var/log/auth.log` | Authentication (Debian/Ubuntu) |
| `/var/log/secure` | Authentication (RHEL family) |
| `journalctl` | Systemd journal |
| `/var/log/syslog` | General system log |
| `/var/log/messages` | General system log (distribution dependent) |
| `/var/log/kern.log` | Kernel events (where available) |
| `/var/log/audit/audit.log` | Linux Audit Framework logs |

---

# Daily Security Review

A security administrator should routinely review:

```text
Authentication

↓

Privilege Escalation

↓

Service Changes

↓

Configuration Changes

↓

Firewall Events

↓

Critical Errors
```

---

# Detecting Suspicious Logins

Useful commands:

Current users:

```bash
who
```

Login history:

```bash
last
```

Failed logins:

```bash
lastb
```

Current SSH sessions:

```bash
ss -tnp | grep ssh
```

---

# Monitoring Running Processes

List processes:

```bash
ps aux
```

Interactive monitoring:

```bash
top
```

Or:

```bash
htop
```

Look for:

- Unknown binaries
- Unexpected parent processes
- High CPU usage
- High memory usage
- Processes running as root unexpectedly

---

# Monitoring Open Network Ports

Display listening ports:

```bash
ss -tuln
```

Display associated processes:

```bash
ss -tulpn
```

Questions to ask:

- Is this service expected?
- Who started it?
- Is it publicly exposed?
- Is encryption enabled where appropriate?

---

# Monitoring File Changes

Critical files include:

```text
/etc/passwd

/etc/shadow

/etc/group

/etc/sudoers

/etc/ssh/sshd_config
```

Unexpected modifications should be investigated immediately.

---

# File Integrity Monitoring (FIM)

File Integrity Monitoring detects unauthorized changes.

Workflow:

```text
Baseline

↓

Monitor

↓

Detect Change

↓

Alert

↓

Investigate
```

Common uses:

- Compliance
- Malware detection
- Insider threat detection
- Configuration monitoring

---

# Malware on Linux

Although Linux experiences fewer malware infections than some desktop operating systems, it is **not immune**.

Examples include:

- Cryptocurrency miners
- Web shells
- Backdoors
- Remote Access Trojans (RATs)
- Worms
- Ransomware
- Botnet malware

---

# Malware Infection Chain

```text
Initial Access

↓

Execution

↓

Persistence

↓

Privilege Escalation

↓

Credential Access

↓

Lateral Movement

↓

Impact
```

---

# Indicators of Malware

Possible indicators include:

- Unexpected CPU usage
- High network traffic
- Unknown services
- New scheduled jobs
- Suspicious user accounts
- Disabled security tools
- Unexpected outbound connections

These indicators require investigation but are not, by themselves, proof of malware.

---

# Rootkits

A rootkit attempts to hide malicious activity by modifying or interfering with the operating system.

Objectives may include:

- Hiding processes
- Hiding files
- Hiding network connections
- Maintaining persistence
- Avoiding detection

---

# Rootkit Risks

```text
Attacker

↓

Privilege Escalation

↓

Rootkit Installed

↓

Persistence

↓

Hidden Activity
```

---

# Detecting Rootkits

Common approaches:

- File integrity monitoring
- Offline forensic analysis
- Secure boot verification
- Kernel module inspection
- Specialized detection tools

Examples of commonly used tools include:

- `rkhunter`
- `chkrootkit`

These tools help identify suspicious indicators but should not be considered definitive proof of compromise.

---

# Kernel Module Inspection

Loaded modules:

```bash
lsmod
```

Module details:

```bash
modinfo module_name
```

Investigate unexpected or unsigned modules according to organizational policy.

---

# Vulnerability Management

Vulnerability management is an ongoing process.

```text
Discover

↓

Assess

↓

Prioritize

↓

Patch

↓

Verify

↓

Monitor
```

---

# Types of Vulnerabilities

| Category | Examples |
|-----------|----------|
| Kernel | Privilege escalation |
| Application | Remote code execution |
| Libraries | Memory corruption |
| Configuration | Weak permissions |
| Network | Exposed services |
| Authentication | Weak credentials |

---

# Vulnerability Assessment

A vulnerability assessment identifies security weaknesses before attackers do.

Typical workflow:

```text
Asset Inventory

↓

Scan

↓

Validate Findings

↓

Prioritize

↓

Remediate

↓

Rescan
```

---

# Patch Management

Regular updates reduce exposure to known vulnerabilities.

Typical process:

```text
Identify Updates

↓

Test

↓

Approve

↓

Deploy

↓

Verify

↓

Document
```

Testing updates before production deployment helps reduce operational risk.

---

# Security Hardening

Hardening reduces the attack surface of a system.

Examples include:

- Remove unnecessary packages
- Disable unused services
- Restrict remote access
- Enforce strong authentication
- Configure firewalls
- Enable Mandatory Access Control
- Apply security updates
- Limit administrative access

---

# Hardening Workflow

```text
Install

↓

Update

↓

Remove Unused Software

↓

Secure Configuration

↓

Enable Monitoring

↓

Regular Audits
```

---

# Backup Strategy

Security includes recoverability.

Recommended practices:

- Regular backups
- Encryption where appropriate
- Off-site or geographically separate copies
- Backup verification
- Periodic recovery testing

---

# Incident Response

Incident response is the structured process of handling security events.

Typical phases:

```text
Preparation

↓

Detection

↓

Analysis

↓

Containment

↓

Eradication

↓

Recovery

↓

Lessons Learned
```

---

# Example Incident Workflow

```text
SIEM Alert

↓

SOC Investigation

↓

Collect Evidence

↓

Contain Threat

↓

Remove Malware

↓

Recover System

↓

Review Incident
```

---

# Digital Forensics

Forensics focuses on preserving and analyzing evidence.

Potential evidence sources:

- Logs
- Memory captures
- Disk images
- Network captures
- Audit records
- Authentication history

Evidence handling should follow organizational and legal requirements.

---

# Enterprise Security Architecture

```text
Users

↓

Authentication

↓

Linux Servers

↓

Logging

↓

SIEM

↓

SOC

↓

Incident Response

↓

Compliance
```

---

# Compliance

Many organizations must comply with security standards.

Examples include:

| Standard | Purpose |
|-----------|----------|
| ISO/IEC 27001 | Information Security Management |
| PCI DSS | Payment card security |
| HIPAA | Healthcare data protection (US) |
| GDPR | Personal data protection (EU) |
| CIS Benchmarks | Secure configuration guidance |
| NIST Cybersecurity Framework | Security risk management |

Applicable requirements depend on the organization and jurisdiction.

---

# Security Auditing

Regular audits evaluate:

- User accounts
- Permissions
- Services
- Firewall rules
- Installed packages
- Security configurations
- Logging
- Patch status

Audits help identify deviations from security policy.

---

# Enterprise Security Dashboard

```text
Security Dashboard

├── Authentication Events

├── Critical Alerts

├── Vulnerability Status

├── Patch Compliance

├── File Integrity

├── Endpoint Health

├── Firewall Activity

├── Malware Alerts

├── Audit Status

└── Incident Queue
```

---

# Enterprise Example

## Detecting an Unauthorized Service

```text
Monitoring Alert

↓

Unexpected Listening Port

↓

Review Process

↓

Identify Binary

↓

Verify Package

↓

Contain

↓

Remove

↓

Review Logs
```

---

# Enterprise Example

## Investigating a Suspicious Login

```text
Failed Logins

↓

Successful Login

↓

Privilege Escalation

↓

Configuration Change

↓

Evidence Collection

↓

Incident Response
```

---

# Enterprise Example

## Responding to Malware

```text
Detection

↓

Isolate Host

↓

Collect Logs

↓

Acquire Evidence

↓

Remove Malware

↓

Patch System

↓

Restore Services

↓

Monitor Closely
```

---

# Cybersecurity Perspective

Linux security is built on multiple complementary controls.

A mature security program combines:

- Least privilege
- Defense in depth
- Secure configuration
- Continuous monitoring
- Vulnerability management
- Incident response
- Regular auditing
- Ongoing improvement

No single control can stop every attack.

---

# Business Impact

Strong Linux security helps organizations:

- Protect critical assets
- Reduce downtime
- Meet compliance requirements
- Lower breach costs
- Improve customer trust
- Increase operational resilience
- Support business continuity

---

# Enterprise Best Practices

- Apply security updates promptly after appropriate testing.
- Enable centralized logging and monitoring.
- Enforce least privilege across users and services.
- Monitor privileged activity continuously.
- Review critical configuration files regularly.
- Conduct periodic vulnerability assessments.
- Maintain tested backups and recovery procedures.
- Document incident response procedures.
- Perform routine security audits.
- Continuously improve security controls based on lessons learned.

---

# Key Takeaways

- Security monitoring enables early detection of threats.
- Malware and rootkits require layered detection and response.
- Vulnerability management is a continuous lifecycle.
- System hardening reduces the attack surface.
- Incident response and forensics are essential for effective recovery.
- Compliance frameworks help organizations establish and maintain strong security practices.

---

