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

