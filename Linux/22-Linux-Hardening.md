# 22 - Linux Hardening

# Part 1 — Linux Hardening Fundamentals, Attack Surface Reduction, Security Principles, and Enterprise Baselines

---

# Introduction

Linux is considered one of the most secure operating systems, but **default installations are not automatically secure**.

Every installed package, running service, open port, user account, and configuration increases the potential attack surface.

**Linux Hardening** is the systematic process of reducing security risks while maintaining system functionality.

It involves:

- Removing unnecessary components
- Strengthening authentication
- Restricting access
- Securing configurations
- Applying security updates
- Continuous monitoring
- Periodic auditing

Hardening is a continuous lifecycle rather than a one-time task.

---

# Learning Objectives

By the end of this chapter, you will understand:

- Linux hardening concepts
- Security principles
- Attack surface reduction
- Defense in depth
- Principle of least privilege
- System baselines
- Security policies
- Enterprise hardening methodology
- Common hardening frameworks

---

# What is Linux Hardening?

Linux hardening is the process of improving the security posture of a Linux system by reducing vulnerabilities and limiting opportunities for attackers.

The goal is to make successful attacks significantly more difficult while preserving business functionality.

---

# Hardening Lifecycle

```text
Install

↓

Configure

↓

Reduce Attack Surface

↓

Apply Security Controls

↓

Monitor

↓

Audit

↓

Improve

↓

Repeat
```

---

# Why Hardening Matters

Without hardening, systems may contain:

- Default passwords
- Unnecessary services
- Weak authentication
- Excessive permissions
- Unpatched software
- Open network ports
- Misconfigured security settings

These weaknesses can be exploited by attackers.

---

# Enterprise Security Objectives

Hardening supports the **CIA Triad**.

| Objective | Description |
|-----------|-------------|
| Confidentiality | Prevent unauthorized disclosure |
| Integrity | Prevent unauthorized modification |
| Availability | Ensure systems remain operational |

---

# Security Principles

Effective hardening is based on established security principles.

---

# Principle of Least Privilege (PoLP)

Users, applications, and services should receive **only the permissions necessary** to perform their tasks.

```text
User

↓

Minimum Required Permission

↓

Required Task
```

Benefits:

- Limits damage from compromised accounts
- Reduces accidental changes
- Simplifies auditing

---

# Defense in Depth

Security should consist of multiple layers.

```text
Firewall

↓

Authentication

↓

Authorization

↓

System Hardening

↓

Application Security

↓

Monitoring
```

If one layer fails, additional controls continue protecting the system.

---

# Zero Trust

Modern enterprise security increasingly follows a **Zero Trust** approach.

Core concepts:

- Never trust by default
- Verify every request
- Continuously validate identity
- Apply least privilege
- Assume breach

---

# Secure by Default

Whenever practical:

- Disable unused features
- Require authentication
- Restrict network exposure
- Enable logging
- Use secure defaults

---

# Attack Surface

The attack surface includes every point through which an attacker may attempt to compromise a system.

Examples:

- Running services
- Open ports
- User accounts
- Installed software
- Scheduled tasks
- Web applications
- APIs
- Remote administration interfaces

---

# Attack Surface Diagram

```text
Linux Server

├── SSH
├── Web Server
├── Database
├── Cron Jobs
├── User Accounts
├── Installed Packages
├── File Shares
└── Open Ports
```

Every exposed component increases the potential attack surface.

---

# Attack Surface Reduction

Hardening focuses on minimizing unnecessary exposure.

Typical actions include:

- Removing unused packages
- Disabling unused services
- Closing unused ports
- Restricting user access
- Removing obsolete accounts
- Limiting administrative privileges

---

# Enterprise Hardening Workflow

```text
Inventory

↓

Risk Assessment

↓

Hardening

↓

Validation

↓

Monitoring

↓

Continuous Improvement
```

---

# Security Baselines

A **security baseline** defines the minimum acceptable security configuration for systems.

Baselines typically specify:

- Password policy
- SSH configuration
- Firewall rules
- Logging requirements
- Patch levels
- Approved software
- File permissions

---

# Baseline Benefits

| Benefit | Description |
|----------|-------------|
| Consistency | Standardized configurations |
| Compliance | Easier regulatory audits |
| Security | Reduced misconfigurations |
| Maintenance | Simplified administration |

---

# System Inventory

Before hardening, identify:

- Operating system version
- Installed packages
- Running services
- Active users
- Open ports
- Mounted filesystems
- Scheduled jobs
- Network interfaces

---

# Useful Inventory Commands

Operating system:

```bash
cat /etc/os-release
```

Kernel:

```bash
uname -r
```

Installed packages (Debian/Ubuntu):

```bash
dpkg -l
```

Installed packages (RHEL-family):

```bash
rpm -qa
```

Running services:

```bash
systemctl list-units --type=service
```

Listening ports:

```bash
ss -tulpn
```

Logged-in users:

```bash
who
```

---

# Risk Assessment

Evaluate:

- Business impact
- Asset value
- Threats
- Vulnerabilities
- Existing controls
- Likelihood
- Potential consequences

Prioritize high-risk systems first.

---

# Hardening Priorities

```text
Critical Systems

↓

Internet-Facing Servers

↓

Authentication

↓

Remote Access

↓

Network Services

↓

Applications
```

---

# Removing Unnecessary Software

Unused software increases:

- Attack surface
- Maintenance effort
- Patch workload

Examples of software that may not be required on a server:

- Games
- Graphical desktop environments
- Development tools (on production servers)
- Test utilities

Always verify dependencies before removing packages.

---

# Reviewing Installed Packages

Ubuntu/Debian:

```bash
dpkg -l
```

RHEL-family:

```bash
rpm -qa
```

Review packages regularly to identify obsolete or unnecessary software.

---

# Removing Packages

Ubuntu/Debian:

```bash
sudo apt remove package-name
```

RHEL-family:

```bash
sudo dnf remove package-name
```

Use caution when removing packages required by other applications.

---

# Service Hardening

Every running service:

- Consumes resources
- May contain vulnerabilities
- Increases the attack surface

Disable services that are not required.

---

# Viewing Active Services

```bash
systemctl list-units --type=service --state=running
```

---

# Disable Unused Service

```bash
sudo systemctl disable service-name
```

Stop immediately:

```bash
sudo systemctl stop service-name
```

Verify that disabling the service will not impact required business functionality.

---

# Open Ports

Each listening port represents a potential entry point.

Review active ports:

```bash
ss -tulpn
```

Questions to ask:

- Is the service required?
- Is it restricted by a firewall?
- Is it up to date?
- Is it monitored?

---

# User Account Review

Review local accounts:

```bash
cat /etc/passwd
```

Identify:

- Unused accounts
- Shared accounts
- Default accounts
- Service accounts with interactive shells

---

# Administrative Access

Administrative privileges should be granted only to authorized personnel.

Review `sudo` configuration regularly.

Avoid using shared administrative accounts whenever possible.

---

# Security Policy

Organizations typically define policies covering:

- Passwords
- Authentication
- Remote access
- Patch management
- Logging
- Incident response
- Change management

Hardening should align with organizational policy.

---

# Hardening Documentation

Document:

- Configuration changes
- Justification
- Date of implementation
- Responsible administrator
- Rollback procedure

Documentation supports audits and simplifies troubleshooting.

---

# Enterprise Hardening Workflow

```text
Policy

↓

Baseline

↓

Configuration

↓

Validation

↓

Deployment

↓

Monitoring

↓

Audit
```

---

# Cybersecurity Perspective

Attackers frequently exploit:

- Default configurations
- Weak authentication
- Unpatched software
- Excessive privileges
- Unnecessary services

Reducing the attack surface makes exploitation more difficult and limits the impact of successful attacks.

---

# Business Impact

A hardened Linux environment helps organizations:

- Reduce security incidents
- Improve regulatory compliance
- Lower operational risk
- Increase system reliability
- Simplify maintenance
- Strengthen customer trust

---

# Enterprise Best Practices

- Maintain a documented security baseline.
- Remove unnecessary software and services.
- Review user accounts regularly.
- Apply the principle of least privilege.
- Restrict administrative access.
- Inventory systems before making changes.
- Validate hardening changes in a test environment.
- Continuously monitor and audit security posture.

---

# Key Takeaways

- Linux hardening reduces the system's attack surface.
- Security should be layered using defense in depth.
- Least privilege is a foundational security principle.
- Baselines ensure consistent and secure configurations.
- Inventory, documentation, and continuous improvement are essential for enterprise hardening.

---

# 22 - Linux Hardening

# Part 2 — User & Account Hardening, Password Policies, Filesystem Hardening, Kernel Hardening, and Package Security

---

# Introduction

Most successful Linux compromises do not begin with sophisticated kernel exploits.

Instead, attackers frequently gain an initial foothold through:

- Weak passwords
- Compromised user accounts
- Excessive privileges
- Misconfigured filesystems
- Insecure kernel parameters
- Outdated software

This section focuses on strengthening these critical security areas.

---

# User Account Hardening

User accounts are one of the primary attack targets.

Every account should be:

- Identified
- Documented
- Authorized
- Periodically reviewed
- Disabled when no longer needed

---

# Account Lifecycle

```text
Create

↓

Assign Permissions

↓

Monitor

↓

Review

↓

Disable

↓

Delete
```

---

# Review Local Accounts

Display all local accounts:

```bash
cat /etc/passwd
```

Display only usernames:

```bash
cut -d: -f1 /etc/passwd
```

Questions to ask:

- Is the account still required?
- Who owns it?
- Is it interactive?
- Does it require administrative access?

---

# Identify Accounts with Login Shells

```bash
grep "/bin/bash" /etc/passwd
```

or

```bash
grep -E "/bin/(bash|sh|zsh)" /etc/passwd
```

Review whether each interactive account is still necessary.

---

# Lock an Account

Temporarily disable logins:

```bash
sudo passwd -l username
```

Unlock:

```bash
sudo passwd -u username
```

Locking is often preferred over deletion when preserving ownership of files or audit history.

---

# Disable an Account

Expire the account immediately:

```bash
sudo chage -E 0 username
```

This prevents future logins while retaining account information.

---

# Delete an Account

Remove a user:

```bash
sudo userdel username
```

Remove the home directory as well:

```bash
sudo userdel -r username
```

Ensure important data is backed up before deleting accounts.

---

# Password Policies

Strong password policies reduce the risk of:

- Brute-force attacks
- Password spraying
- Credential stuffing
- Unauthorized access

---

# Password Policy Components

| Control | Purpose |
|----------|----------|
| Minimum length | Increase password complexity |
| Complexity requirements | Encourage stronger passwords |
| Password aging | Require periodic updates where policy mandates |
| Password history | Reduce password reuse |
| Account lockout | Slow repeated authentication attempts |

---

# Password Aging

View password settings:

```bash
chage -l username
```

Configure expiration:

```bash
sudo chage -M 90 username
```

Example:

Maximum password age:

```text
90 days
```

Specific values should follow organizational policy and applicable regulations.

---

# Minimum Password Length

Many distributions use PAM modules such as `pam_pwquality` to enforce password quality.

Typical enterprise requirements may include:

- Minimum length
- Character diversity
- Dictionary checks
- Similarity restrictions

Exact configuration depends on the Linux distribution and authentication stack.

---

# Secure Password Practices

Recommendations:

- Use long passphrases.
- Avoid dictionary words.
- Avoid password reuse.
- Protect password managers with strong authentication.
- Enable multi-factor authentication where supported.

---

# Administrative Access

Instead of sharing privileged accounts:

```text
Administrator

↓

Individual User Account

↓

sudo

↓

Administrative Task
```

Benefits:

- Better accountability
- Improved auditing
- Reduced credential sharing

---

# Review sudo Access

List a user's sudo privileges:

```bash
sudo -l
```

Review group membership:

```bash
groups username
```

Audit privileged access regularly.

---

# Filesystem Hardening

Improper filesystem permissions can expose sensitive information or allow privilege escalation.

Important areas include:

- Sensitive files
- Temporary directories
- User home directories
- System binaries
- Shared storage

---

# Critical Files

| File | Purpose |
|------|----------|
| `/etc/passwd` | User information |
| `/etc/shadow` | Password hashes |
| `/etc/group` | Group information |
| `/etc/sudoers` | sudo policy |

---

# Protect `/etc/shadow`

Verify permissions:

```bash
ls -l /etc/shadow
```

Only privileged users should have access to password hashes.

---

# Home Directory Permissions

Check permissions:

```bash
ls -ld /home/*
```

Restrict unnecessary access to user home directories according to organizational policy.

---

# Temporary Directories

Common temporary locations:

```text
/tmp

/var/tmp
```

These directories require careful management because many applications use them.

---

# Mount Options

Additional filesystem protection can be provided through mount options.

Common examples:

| Option | Purpose |
|----------|----------|
| `nodev` | Ignore device files |
| `nosuid` | Ignore SUID/SGID bits |
| `noexec` | Prevent direct execution of binaries |

These options are often applied to locations such as `/tmp` when compatible with application requirements.

---

# Example `/etc/fstab`

```text
UUID=...

/tmp

ext4

defaults,nodev,nosuid,noexec

0 0
```

Always test mount option changes before deploying them broadly.

---

# SUID and SGID Review

Locate SUID files:

```bash
find / -perm -4000 -type f 2>/dev/null
```

Locate SGID files:

```bash
find / -perm -2000 -type f 2>/dev/null
```

Review whether elevated permissions are still required.

---

# World-Writable Files

Locate world-writable files:

```bash
find / -type f -perm -0002 2>/dev/null
```

Unexpected world-writable files should be investigated.

---

# Kernel Hardening

The Linux kernel provides security controls that can reduce attack opportunities.

Common areas include:

- Networking
- Memory protections
- Process behavior
- System limits

---

# sysctl

Kernel parameters can be viewed using:

```bash
sysctl -a
```

View a specific parameter:

```bash
sysctl net.ipv4.ip_forward
```

---

# Temporary Configuration

Example:

```bash
sudo sysctl -w net.ipv4.ip_forward=0
```

Changes made this way are not persistent after reboot.

---

# Persistent Configuration

Store settings in configuration files such as:

```text
/etc/sysctl.conf
```

or distribution-specific files under:

```text
/etc/sysctl.d/
```

Apply changes:

```bash
sudo sysctl --system
```

---

# Common Kernel Parameters

| Parameter | Purpose |
|-----------|----------|
| `net.ipv4.ip_forward` | IP forwarding |
| `kernel.randomize_va_space` | Address Space Layout Randomization (ASLR) |
| `net.ipv4.conf.all.accept_redirects` | ICMP redirect handling |
| `net.ipv4.conf.all.send_redirects` | ICMP redirect generation |
| `net.ipv4.conf.all.rp_filter` | Reverse path filtering |

Recommended values depend on the server's role and organizational security requirements.

---

# Address Space Layout Randomization (ASLR)

ASLR randomizes memory locations used by processes.

Benefits:

- Makes exploitation more difficult
- Reduces reliability of certain memory corruption attacks

Check status:

```bash
cat /proc/sys/kernel/randomize_va_space
```

---

# Package Security

Keeping software current is one of the most effective security controls.

Benefits:

- Vulnerability remediation
- Bug fixes
- Stability improvements
- Security enhancements

---

# Update Package Metadata

Ubuntu/Debian:

```bash
sudo apt update
```

RHEL-family:

```bash
sudo dnf check-update
```

---

# Upgrade Installed Packages

Ubuntu/Debian:

```bash
sudo apt upgrade
```

RHEL-family:

```bash
sudo dnf upgrade
```

Test updates in staging environments before deploying to production where possible.

---

# Verify Package Integrity

Many package managers verify digital signatures to ensure packages originate from trusted repositories.

Avoid installing software from untrusted or unknown sources.

---

# Remove Unused Packages

Ubuntu/Debian:

```bash
sudo apt autoremove
```

RHEL-family:

```bash
sudo dnf autoremove
```

Removing unnecessary software reduces the attack surface.

---

# Enterprise Patch Management

Typical workflow:

```text
Security Advisory

↓

Risk Assessment

↓

Testing

↓

Approval

↓

Deployment

↓

Verification

↓

Monitoring
```

---

# Hardening Workflow

```text
Users

↓

Passwords

↓

Filesystem

↓

Kernel

↓

Packages

↓

Validation
```

---

# Cybersecurity Perspective

Attackers frequently target:

- Weak credentials
- Misconfigured permissions
- Outdated packages
- Excessive privileges
- Insecure kernel settings

Strengthening these areas significantly reduces the likelihood and impact of compromise.

---

# Business Impact

Strong account and system hardening:

- Protects sensitive information
- Reduces unauthorized access
- Improves compliance
- Lowers operational risk
- Simplifies security audits
- Supports business continuity

---

# Enterprise Best Practices

- Remove or disable inactive accounts promptly.
- Review privileged access regularly.
- Enforce strong password policies aligned with organizational standards.
- Protect sensitive filesystem locations with appropriate permissions.
- Review SUID/SGID binaries periodically.
- Apply kernel hardening settings after testing.
- Keep systems patched using trusted repositories.
- Document and audit all security configuration changes.

---

# Key Takeaways

- User accounts are a primary attack target and require continuous review.
- Password policies help defend against credential-based attacks.
- Filesystem permissions are essential for protecting sensitive data.
- Kernel parameters can strengthen system security.
- Regular patching is a foundational hardening practice.
- Secure configuration should balance protection with operational requirements.

---


# 22 - Linux Hardening

# Part 3 — Network Hardening, SSH Hardening, Service Hardening, Logging, Auditing, Security Monitoring, and Compliance

---

# Introduction

After securing user accounts, filesystems, and the kernel, the next priority is protecting the system from network-based attacks.

Enterprise environments continuously monitor:

- Network exposure
- Remote administration
- Running services
- Authentication attempts
- Security events
- Configuration drift

These controls significantly reduce the likelihood of unauthorized access and improve incident detection.

---

# Network Hardening

Network hardening reduces unnecessary exposure by limiting communication to only required services.

Objectives:

- Reduce attack surface
- Restrict inbound connections
- Restrict outbound traffic where appropriate
- Secure remote administration
- Improve monitoring

---

# Network Hardening Workflow

```text
Identify Services

↓

Review Open Ports

↓

Close Unused Ports

↓

Configure Firewall

↓

Monitor

↓

Audit
```

---

# Review Listening Ports

Display listening ports:

```bash
ss -tulpn
```

Alternative:

```bash
netstat -tulpn
```

(if available)

Questions:

- Is this service required?
- Who uses it?
- Should it be Internet accessible?
- Is it protected by a firewall?

---

# Verify Open Ports

Example output:

```text
22/tcp     SSH

80/tcp     HTTP

443/tcp    HTTPS
```

Unexpected ports should be investigated immediately.

---

# Firewall Strategy

Firewalls should follow a **default deny** philosophy whenever practical.

```text
Incoming Traffic

↓

Firewall

↓

Allowed?

├── Yes → Forward
│
└── No

     ↓

    Block
```

Only explicitly authorized services should be reachable.

---

# Network Segmentation

Enterprise environments rarely place all systems on one network.

Example:

```text
Internet

↓

Firewall

↓

DMZ

↓

Application Network

↓

Database Network
```

Benefits:

- Limits lateral movement
- Reduces attack impact
- Improves access control
- Supports compliance

---

# Restrict Administrative Access

SSH should ideally be accessible only from:

- VPN
- Bastion hosts
- Administrative networks
- Approved management workstations

Avoid exposing administrative services unnecessarily.

---

# Disable Unused Network Services

Examples may include:

- FTP
- Telnet
- rlogin
- rsh
- Unused RPC services

Replace legacy protocols with secure alternatives such as SSH or SFTP where appropriate.

---

# SSH Hardening

SSH is one of the most frequently targeted Linux services.

Recommended hardening measures include:

- Public key authentication
- Restrict administrative users
- Disable direct root login
- Limit authentication attempts
- Use modern cryptographic algorithms
- Monitor authentication logs

---

# SSH Hardening Workflow

```text
Install

↓

Configure

↓

Key Authentication

↓

Restrict Users

↓

Logging

↓

Monitoring
```

---

# Review SSH Configuration

Configuration file:

```text
/etc/ssh/sshd_config
```

Validate before applying changes:

```bash
sudo sshd -t
```

---

# Recommended SSH Controls

| Control | Benefit |
|----------|----------|
| Disable direct root login | Reduces privileged attack surface |
| Prefer public key authentication | Stronger authentication |
| Restrict users/groups | Limits access |
| Limit authentication attempts | Mitigates brute-force attacks |
| Idle session timeout | Reduces abandoned sessions |

Specific settings should align with organizational security policies.

---

# Service Hardening

Every running service represents a potential attack vector.

Review active services:

```bash
systemctl list-units --type=service --state=running
```

Questions:

- Is the service required?
- Is it updated?
- Is it monitored?
- Is it reachable only by authorized systems?

---

# Disable Unused Services

Stop immediately:

```bash
sudo systemctl stop service-name
```

Disable at boot:

```bash
sudo systemctl disable service-name
```

Confirm that disabling the service will not affect business operations.

---

# Service Hardening Workflow

```text
Inventory

↓

Risk Review

↓

Disable Unused

↓

Patch

↓

Monitor
```

---

# Logging

Security logging provides visibility into system activity.

Important log sources include:

- Authentication
- Kernel
- Services
- Firewall
- Applications
- Package management

---

# Common Log Locations

| Distribution | Authentication Log |
|--------------|--------------------|
| Ubuntu/Debian | `/var/log/auth.log` |
| RHEL-family | `/var/log/secure` |

Systemd systems also provide centralized logging through:

```bash
journalctl
```

---

# Authentication Monitoring

Examples:

Successful logins

```bash
grep "Accepted" /var/log/auth.log
```

Failed logins

```bash
grep "Failed password" /var/log/auth.log
```

Equivalent log locations vary by distribution.

---

# Audit Logging

Linux systems may use the Linux Audit Framework (`auditd`) for detailed event logging.

Common audit targets include:

- Authentication events
- File access
- Privilege escalation
- System configuration changes

---

# Audit Workflow

```text
User Action

↓

Kernel

↓

Audit Rules

↓

Audit Log

↓

Analysis
```

---

# Security Monitoring

Continuous monitoring helps detect:

- Unauthorized logins
- Configuration changes
- Suspicious processes
- Service failures
- Unexpected network activity

Monitoring should be proactive rather than reactive.

---

# Monitoring Workflow

```text
Events

↓

Logs

↓

Analysis

↓

Alert

↓

Investigation

↓

Response
```

---

# File Integrity Monitoring

Critical files can be monitored for unexpected changes.

Typical targets include:

```text
/etc/passwd

/etc/shadow

/etc/group

/etc/sudoers

SSH configuration

Firewall configuration
```

Unexpected modifications should trigger investigation.

---

# Configuration Drift

Configuration drift occurs when systems gradually diverge from the approved security baseline.

Causes include:

- Manual changes
- Emergency fixes
- Unauthorized modifications
- Inconsistent deployments

Regular audits help detect and correct drift.

---

# Compliance

Hardening often supports compliance requirements.

Common frameworks include:

| Framework | Focus |
|-----------|-------|
| CIS Benchmarks | Secure configuration guidance |
| NIST Cybersecurity Framework | Risk management |
| ISO/IEC 27001 | Information security management |
| PCI DSS | Payment card security |
| HIPAA | Healthcare information protection |

Specific requirements depend on the organization's regulatory obligations.

---

# Security Baseline Validation

Validation checklist:

```text
Users

↓

Services

↓

Ports

↓

Packages

↓

Firewall

↓

Logging

↓

Monitoring

↓

Documentation
```

---

# Change Management

Hardening changes should follow a structured process.

```text
Request

↓

Review

↓

Approval

↓

Testing

↓

Deployment

↓

Validation

↓

Documentation
```

Benefits:

- Reduced operational risk
- Easier rollback
- Improved accountability

---

# Incident Response Readiness

A hardened system should support rapid incident response through:

- Centralized logs
- Accurate time synchronization
- Documented configurations
- Reliable backups
- Secure remote access

Preparation before an incident is critical.

---

# Enterprise Hardening Architecture

```text
Internet

↓

Firewall

↓

VPN

↓

Bastion Host

↓

Application Servers

↓

Database Servers

↓

Central Logging

↓

Security Monitoring
```

---

# Security Review Checklist

| Control | Status |
|----------|--------|
| Firewall configured | ✓ |
| Unused ports closed | ✓ |
| SSH hardened | ✓ |
| Unused services disabled | ✓ |
| Logging enabled | ✓ |
| Audit logging configured | ✓ |
| Monitoring implemented | ✓ |
| Baseline documented | ✓ |
| Changes approved | ✓ |
| Compliance reviewed | ✓ |

---

# Cybersecurity Perspective

Most enterprise attacks rely on multiple weaknesses rather than a single vulnerability.

Examples include:

- Weak authentication
- Excessive privileges
- Poor network segmentation
- Inadequate monitoring
- Delayed patching

Layered hardening significantly reduces attacker success rates and improves detection capabilities.

---

# Business Impact

Network and service hardening help organizations:

- Reduce unauthorized access
- Improve service availability
- Support regulatory compliance
- Strengthen incident detection
- Protect business-critical infrastructure
- Reduce operational risk

---

# Enterprise Best Practices

- Expose only required network services.
- Restrict administrative access to trusted networks.
- Harden SSH according to organizational policy.
- Monitor authentication events continuously.
- Enable centralized logging where feasible.
- Detect and remediate configuration drift.
- Perform periodic security reviews.
- Integrate hardening with change management processes.

---

# Key Takeaways

- Network hardening reduces exposure to external threats.
- SSH requires careful configuration and monitoring.
- Running services should be reviewed and minimized.
- Logging and auditing provide essential security visibility.
- Continuous monitoring strengthens incident detection.
- Compliance and hardening should work together to improve the overall security posture.

---

# 22 - Linux Hardening

# Part 4 — Practical Labs, Enterprise Case Studies, Hardening Checklists, Chapter Summary, Interview Questions, and References

---

# Introduction

Linux hardening is not a single command or configuration.

It is an ongoing process involving:

- Secure configuration
- Continuous patching
- Monitoring
- Auditing
- Compliance
- Incident response
- Periodic reviews

This chapter concludes with practical exercises, enterprise scenarios, comprehensive hardening checklists, interview preparation, and references.

---

# Enterprise Hardening Lifecycle

```text
Asset Inventory

↓

Baseline Configuration

↓

Hardening

↓

Validation

↓

Deployment

↓

Continuous Monitoring

↓

Periodic Auditing

↓

Continuous Improvement
```

---

# Practical Lab 1 — Identify System Information

Display operating system details:

```bash
cat /etc/os-release
```

Display kernel version:

```bash
uname -r
```

Display hostname:

```bash
hostnamectl
```

Objectives:

- Verify operating system
- Identify kernel version
- Record baseline information

---

# Practical Lab 2 — Inventory Installed Packages

Ubuntu/Debian:

```bash
dpkg -l
```

RHEL-family:

```bash
rpm -qa
```

Objectives:

- Review installed software
- Identify unnecessary packages
- Compare against the approved software baseline

---

# Practical Lab 3 — Review Running Services

List running services:

```bash
systemctl list-units --type=service --state=running
```

Objectives:

- Identify active services
- Determine business necessity
- Document services that can be disabled

---

# Practical Lab 4 — Review Open Network Ports

Display listening ports:

```bash
ss -tulpn
```

Objectives:

- Identify exposed services
- Verify expected ports
- Investigate unexpected listeners

---

# Practical Lab 5 — Audit User Accounts

List all users:

```bash
cut -d: -f1 /etc/passwd
```

Identify interactive accounts:

```bash
grep -E "/bin/(bash|sh|zsh)" /etc/passwd
```

Objectives:

- Identify unused accounts
- Review administrative users
- Verify account ownership

---

# Practical Lab 6 — Review Password Aging

Display password policy:

```bash
chage -l username
```

Replace `username` with an existing account.

Objectives:

- Review password aging
- Verify organizational policy compliance

---

# Practical Lab 7 — Review Sudo Access

Check privileges:

```bash
sudo -l
```

Review group membership:

```bash
groups username
```

Objectives:

- Verify least privilege
- Audit administrative access

---

# Practical Lab 8 — Review Filesystem Permissions

Check sensitive files:

```bash
ls -l /etc/passwd
```

```bash
ls -l /etc/shadow
```

Check home directories:

```bash
ls -ld /home/*
```

Objectives:

- Verify permissions
- Identify excessive access

---

# Practical Lab 9 — Find SUID and SGID Files

Locate SUID binaries:

```bash
find / -perm -4000 -type f 2>/dev/null
```

Locate SGID binaries:

```bash
find / -perm -2000 -type f 2>/dev/null
```

Objectives:

- Inventory privileged binaries
- Investigate unexpected entries

---

# Practical Lab 10 — Identify World-Writable Files

```bash
find / -type f -perm -0002 2>/dev/null
```

Objectives:

- Detect insecure permissions
- Reduce privilege escalation opportunities

---

# Practical Lab 11 — Review Kernel Parameters

Display all kernel parameters:

```bash
sysctl -a
```

Check ASLR:

```bash
cat /proc/sys/kernel/randomize_va_space
```

Objectives:

- Review kernel security settings
- Understand runtime configuration

---

# Practical Lab 12 — Validate SSH Configuration

Review active configuration:

```bash
grep -v "^#" /etc/ssh/sshd_config
```

Validate syntax:

```bash
sudo sshd -t
```

Objectives:

- Review SSH hardening
- Prevent configuration errors

---

# Practical Lab 13 — Review Authentication Logs

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

Objectives:

- Identify failed login attempts
- Detect brute-force activity

---

# Practical Lab 14 — Review Firewall Configuration

Examples:

```bash
sudo ufw status
```

or

```bash
sudo firewall-cmd --list-all
```

Objectives:

- Verify firewall rules
- Confirm only required services are exposed

---

# Practical Lab 15 — Perform a Basic Hardening Audit

Create a checklist covering:

- Packages
- Users
- Services
- Ports
- SSH
- Firewall
- Logging
- Kernel
- Filesystem
- Monitoring

Objectives:

- Build a repeatable audit process
- Document findings and remediation

---

# Enterprise Case Study 1

# Internet-Facing Web Server

Architecture:

```text
Internet

↓

Firewall

↓

Reverse Proxy

↓

Web Server

↓

Database
```

Hardening Actions:

- Remove unnecessary packages
- Disable unused services
- Restrict SSH access
- Enable firewall
- Monitor authentication logs
- Apply security updates

Benefits:

- Reduced attack surface
- Improved resilience

---

# Enterprise Case Study 2

# Secure Administrative Access

Architecture:

```text
Administrator

↓

VPN

↓

Bastion Host

↓

Production Servers
```

Controls:

- Public key authentication
- Individual user accounts
- Multi-factor authentication (where supported)
- Centralized logging
- Session auditing

---

# Enterprise Case Study 3

# Patch Management

Workflow:

```text
Security Advisory

↓

Risk Assessment

↓

Testing

↓

Approval

↓

Deployment

↓

Verification

↓

Documentation
```

Benefits:

- Faster vulnerability remediation
- Reduced operational risk

---

# Enterprise Case Study 4

# Configuration Drift Detection

Workflow:

```text
Baseline

↓

Periodic Audit

↓

Difference Found?

├── No → Continue Monitoring
│
└── Yes

     ↓

 Investigate

     ↓

 Remediate

     ↓

 Update Documentation
```

Benefits:

- Consistent configurations
- Improved compliance

---

# Enterprise Case Study 5

# Compliance Readiness

Quarterly audit validates:

- Password policy
- SSH configuration
- Firewall
- Logging
- Installed packages
- Running services
- File permissions
- Kernel settings

Results are documented and reviewed before external audits.

---

# Enterprise Hardening Checklist

| Control | Status |
|----------|--------|
| Operating system inventory | ✓ |
| Security baseline documented | ✓ |
| Unnecessary packages removed | ✓ |
| Unused services disabled | ✓ |
| Open ports reviewed | ✓ |
| Firewall configured | ✓ |
| SSH hardened | ✓ |
| User accounts audited | ✓ |
| Least privilege enforced | ✓ |
| Password policy applied | ✓ |
| Sensitive file permissions reviewed | ✓ |
| SUID/SGID reviewed | ✓ |
| Kernel parameters reviewed | ✓ |
| Package updates applied | ✓ |
| Logs monitored | ✓ |
| Audit logging enabled | ✓ |
| Monitoring implemented | ✓ |
| Configuration documented | ✓ |
| Backups verified | ✓ |
| Periodic review scheduled | ✓ |

---

# Common Hardening Mistakes

| Mistake | Risk | Better Practice |
|----------|------|-----------------|
| Leaving default settings | Increased exposure | Apply security baseline |
| Unpatched systems | Known vulnerabilities | Regular patch management |
| Unused services enabled | Larger attack surface | Disable unnecessary services |
| Shared administrative accounts | Poor accountability | Individual accounts with `sudo` |
| Weak passwords | Credential compromise | Strong password policy |
| Excessive permissions | Privilege escalation | Principle of least privilege |
| Ignoring logs | Delayed detection | Continuous monitoring |
| Poor documentation | Difficult audits | Maintain configuration records |

---

# Cybersecurity Perspective

Linux hardening is a preventive control that complements detection and response.

A hardened system:

- Reduces attacker opportunities
- Limits privilege escalation
- Improves visibility
- Supports faster investigations
- Strengthens overall resilience

Security teams should combine hardening with:

- Vulnerability management
- Threat detection
- Incident response
- Continuous monitoring

---

# Business Impact

Comprehensive hardening helps organizations:

- Reduce security incidents
- Protect sensitive information
- Meet regulatory obligations
- Improve system stability
- Lower operational costs
- Increase customer confidence
- Enhance business continuity

---

# Chapter Summary

In this chapter, you learned:

- Linux hardening fundamentals
- Attack surface reduction
- Security principles
- Least privilege
- Defense in depth
- User and account hardening
- Password policies
- Filesystem hardening
- Kernel hardening
- Package security
- Network hardening
- SSH hardening
- Service hardening
- Logging and auditing
- Security monitoring
- Compliance
- Enterprise hardening strategies

---

# Interview Questions

## Beginner

1. What is Linux hardening?
2. Why is attack surface reduction important?
3. What is the principle of least privilege?
4. What is defense in depth?
5. Why should unused services be disabled?
6. What is the purpose of `sysctl`?
7. Why is SSH hardening necessary?
8. What is a security baseline?
9. Why are software updates important?
10. What is configuration drift?

---

## Intermediate

1. Explain the Linux hardening lifecycle.
2. How would you review user accounts on a Linux server?
3. Describe common filesystem hardening techniques.
4. What are SUID and SGID, and why should they be audited?
5. Compare security baselines and compliance frameworks.
6. Explain the purpose of centralized logging.
7. How would you harden an Internet-facing Linux server?
8. Describe an enterprise patch management workflow.
9. Why is documentation important during hardening?
10. How would you validate that hardening changes were successful?

---

## Advanced

1. Design a hardening strategy for a production Linux environment.
2. Explain how you would secure SSH access for hundreds of servers.
3. Describe a layered security architecture for enterprise Linux systems.
4. How would you detect and remediate configuration drift?
5. Explain how hardening supports compliance requirements.
6. Design a security baseline for a cloud-hosted Linux server.
7. How would you integrate hardening into CI/CD or infrastructure-as-code workflows?
8. Describe the role of auditing in enterprise hardening.
9. How would you prioritize hardening tasks after deploying a new server?
10. Explain how Linux hardening complements vulnerability management and incident response.

---

# Key Takeaways

- Hardening is an ongoing lifecycle, not a one-time activity.
- Security baselines promote consistency across systems.
- Least privilege and defense in depth are fundamental principles.
- User, filesystem, kernel, network, and service hardening work together to reduce risk.
- Continuous monitoring, auditing, and documentation are essential for maintaining a secure Linux environment.
- Enterprise hardening should balance strong security with operational requirements.

---

# References

## Official Documentation

- `man sysctl`
- `man passwd`
- `man chage`
- `man sudo`
- `man systemctl`
- `man sshd_config`
- `man journalctl`
- `man find`

## Standards & Best Practices

- CIS Benchmarks for Linux
- Linux Foundation Documentation
- Red Hat Enterprise Linux Security Guide
- Ubuntu Server Guide
- NIST SP 800-53 (Security and Privacy Controls)
- NIST Cybersecurity Framework (CSF)
- ISO/IEC 27001
- MITRE ATT&CK Framework
- OWASP Cheat Sheet Series

---

# Next Chapter

➡️ **23-Linux-for-Cybersecurity.md**

## Topics Covered

- Linux in Cybersecurity
- Red Team vs Blue Team
- Penetration Testing Workflow
- Digital Forensics
- Incident Response
- Threat Hunting
- Malware Analysis
- Security Tools
- SOC Operations
- Practical Labs
- Enterprise Case Studies
- Interview Questions
- References