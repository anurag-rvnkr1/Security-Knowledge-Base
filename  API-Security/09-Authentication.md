# 09 - Authentication

# Introduction

Authentication is the process of verifying the identity of a user, application, service, or device before granting access to resources.

It answers a fundamental security question:

> **"Who are you?"**

Authentication is one of the most critical security controls in modern applications because it serves as the first line of defense against unauthorized access.

Every enterprise application—including:

- Web applications
- REST APIs
- GraphQL APIs
- gRPC services
- Cloud platforms
- Mobile applications
- IoT devices

depends on robust authentication mechanisms.

Authentication is closely related to, but distinct from, authorization.

```
Authentication

↓

Who are you?

↓

Identity Verified

↓

Authorization

↓

What are you allowed to do?
```

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand authentication fundamentals.
- Differentiate authentication from authorization.
- Learn authentication factors.
- Understand password-based authentication.
- Explore Multi-Factor Authentication (MFA).
- Learn API key authentication.
- Understand certificate-based authentication.
- Explore enterprise Identity Providers (IdPs).
- Identify authentication attacks.
- Perform authentication security assessments.

---

# What is Authentication?

Authentication verifies identity before allowing access.

Example

```
User

 │

Username

Password

 ▼

Authentication Server

 │

Identity Verified

 ▼

Access Granted
```

If authentication fails,

```
Access Denied
```

---

# Authentication vs Authorization

These concepts are often confused.

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Determines permissions |
| Happens first | Happens after authentication |
| "Who are you?" | "What can you access?" |
| Identity validation | Access control |

Example

```
Employee

↓

Authentication

↓

Verified

↓

Authorization

↓

Access Payroll System
```

---

# Authentication Architecture

```
               User

                 │

                 ▼

          Login Request

                 │

                 ▼

       Authentication Server

                 │

     Verify Credentials

                 │

     ┌───────────┴───────────┐

     ▼                       ▼

 Success                 Failure

     │                       │

 Issue Token          Reject Access

     │

     ▼

 Protected Resource
```

---

# Identity

Identity represents a unique entity.

Examples

- User
- Employee
- Customer
- Administrator
- Service Account
- API Client
- IoT Device

Each identity should have a unique identifier.

Examples

```
Employee ID

Email Address

Username

UUID
```

---

# Credentials

Credentials prove identity.

Examples include:

- Passwords
- API Keys
- Certificates
- Security Tokens
- Biometrics
- Hardware Keys

Credentials should always be protected.

---

# Authentication Factors

Authentication factors fall into three primary categories.

```
Authentication

      │

 ┌────┼────┐

 ▼    ▼    ▼

Know Have Are
```

---

# Knowledge Factor

Something the user knows.

Examples

- Password
- PIN
- Passphrase
- Security Question

Knowledge factors are the most common but are also vulnerable to guessing, phishing, and credential theft.

---

# Possession Factor

Something the user has.

Examples

- Mobile phone
- Smart card
- Hardware token
- USB security key
- Authenticator application

Possession factors significantly improve security.

---

# Inherence Factor

Something the user is.

Examples

- Fingerprint
- Face recognition
- Iris scan
- Voice recognition
- Palm recognition

Biometric systems should include anti-spoofing protections.

---

# Multi-Factor Authentication (MFA)

MFA combines multiple authentication factors.

Example

```
Password

+

Authenticator App

↓

Access Granted
```

Common combinations

```
Know

+

Have
```

or

```
Know

+

Are
```

MFA dramatically reduces the success rate of credential theft attacks.

---

# Single-Factor Authentication

Example

```
Password Only
```

Advantages

- Simple
- Low cost
- Familiar

Disadvantages

- Weak against phishing
- Vulnerable to credential reuse
- Susceptible to brute force attacks

---

# Two-Factor Authentication (2FA)

2FA is a specific form of MFA using exactly two factors.

Example

```
Password

+

One-Time Password
```

Both factors must be validated before access is granted.

---

# Common Authentication Methods

| Method | Typical Usage |
|---------|---------------|
| Username & Password | Web applications |
| API Key | APIs |
| JWT | REST APIs |
| OAuth 2.0 | Delegated access |
| OpenID Connect | User authentication |
| Client Certificates | Enterprise systems |
| Kerberos | Windows environments |
| SAML | Enterprise Single Sign-On |
| Passkeys | Modern passwordless authentication |

---

# Password-Based Authentication

Password authentication remains the most common method.

Workflow

```
User

 │

Username

Password

 ▼

Authentication Server

 │

Hash Password

 │

Compare Hash

 ▼

Decision
```

Passwords should never be stored in plaintext.

---

# Password Hashing

Applications should store password hashes instead of passwords.

```
Password

 │

Hash Function

 ▼

Password Hash

 │

Database
```

If the database is compromised, attackers should not obtain usable plaintext passwords.

---

# Modern Password Hashing Algorithms

Recommended algorithms

- Argon2id
- bcrypt
- scrypt

Characteristics

- Slow by design
- Resistant to brute-force attacks
- Configurable work factor
- Salt support

Avoid using general-purpose hashing algorithms such as:

- MD5
- SHA-1

for password storage.

---

# Password Salting

A salt is a unique random value added before hashing.

```
Password

+

Random Salt

↓

Hash

↓

Store
```

Benefits

- Prevents rainbow table attacks
- Ensures identical passwords produce different hashes
- Increases attack cost

Each password should use a unique salt.

---

# Password Policies

A strong password policy should include:

- Minimum length
- Maximum length support
- Allow passphrases
- Reject common passwords
- Block breached passwords
- Encourage password managers

Example

```
Correct Horse Battery Staple
```

Long passphrases are generally easier to remember and harder to guess than short complex passwords.

---

# Password Storage

Only the following should be stored:

```
Username

Salt

Password Hash
```

Never store:

- Plaintext passwords
- Reversible encryption keys for passwords
- Password hints revealing secrets

---

# Password Verification

```
User Password

 │

Hash Using Stored Salt

 │

Compare

 │

Match?

 ┌─────┴─────┐

Yes         No

 │           │

Login     Reject
```

The original password is never recovered from storage.

---

# Password Reset

A secure reset process should include:

- Identity verification
- Time-limited reset links
- Single-use reset tokens
- HTTPS
- Notification emails

Avoid:

- Predictable reset tokens
- Security questions as the sole verification mechanism
- Long-lived reset links

---

# Password Change

Recommended workflow

```
Authenticated User

 │

Current Password

 │

New Password

 │

Policy Validation

 ▼

Password Updated
```

High-risk accounts may also require MFA confirmation.

---

# Account Registration

Typical registration flow

```
User

 │

Registration Form

 │

Input Validation

 │

Email Verification

 │

Account Creation

 ▼

Login
```

Email verification helps confirm ownership of the supplied email address.

---

# Email Verification

```
Register

 │

Verification Email

 │

Click Link

 ▼

Account Activated
```

Verification links should:

- Expire quickly
- Be single-use
- Use cryptographically secure random tokens

---

# Authentication Lifecycle

```
Identity Created

      │

Registration

      │

Authentication

      │

Session Created

      │

Access Resources

      │

Logout

      ▼

Session Terminated
```

Authentication is an ongoing lifecycle rather than a single event.

---

# Enterprise Example

A banking platform authenticates users using:

```
Username

+

Password

+

Authenticator App

↓

Identity Provider

↓

JWT Issued

↓

Banking API
```

This layered approach combines strong authentication with secure token-based authorization.

---

# Best Practices

Authentication

- Require HTTPS.
- Use MFA for privileged accounts.
- Hash passwords with Argon2id, bcrypt, or scrypt.
- Use unique salts.
- Protect authentication endpoints with rate limiting.

Password Management

- Support long passphrases.
- Reject weak and breached passwords.
- Encourage password managers.
- Require secure password reset workflows.

Operations

- Log authentication events.
- Monitor failed login attempts.
- Rotate secrets where appropriate.
- Protect service accounts.

---

# Common Mistakes

Avoid:

- Storing plaintext passwords
- Using MD5 or SHA-1 for password storage
- Missing MFA for administrators
- Weak password reset workflows
- Predictable reset tokens
- Logging passwords
- Reusing API keys
- Sharing service account credentials
- Ignoring failed authentication monitoring

---

# Key Takeaways

- Authentication verifies identity before access is granted.
- Authentication and authorization serve different purposes.
- MFA combines multiple authentication factors for stronger security.
- Passwords should always be salted and hashed using modern password hashing algorithms.
- Secure password lifecycle management includes registration, verification, reset, change, and logout.
- Strong authentication is the foundation of enterprise security.

---

**Next:** Passwordless Authentication, API Keys, Certificates, SAML, Kerberos, OpenID Connect, Enterprise Identity Providers, Authentication Attacks, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.