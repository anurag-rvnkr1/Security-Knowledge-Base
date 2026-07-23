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


