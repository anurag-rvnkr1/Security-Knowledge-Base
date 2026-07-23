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


