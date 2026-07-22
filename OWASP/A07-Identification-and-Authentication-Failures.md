# A07:2021 – Identification and Authentication Failures

---

# Overview

Every secure application must answer three fundamental questions before granting access to protected resources:

1. **Who are you?**
2. **Can you prove your identity?**
3. **What are you allowed to do?**

These questions correspond to three core security concepts:

- Identification
- Authentication
- Authorization

A failure in any of these areas may allow attackers to impersonate legitimate users, compromise accounts, access sensitive information, or escalate privileges.

OWASP A07 focuses on weaknesses in **identity verification and authentication mechanisms** rather than authorization decisions (covered in A01).

---

# Why It Matters

Almost every application requires users to authenticate.

Examples include:

- Banking applications
- Email services
- Cloud platforms
- E-commerce websites
- Enterprise portals
- Healthcare systems
- Social media
- Government services

If authentication is weak, attackers may gain access **without exploiting traditional software vulnerabilities**.

---

# Authentication Architecture

A simplified authentication flow:

```
                 User
                   │
                   ▼
           Identification
                   │
                   ▼
          Authentication
                   │
                   ▼
        Session / Token Issued
                   │
                   ▼
            Authorization
                   │
                   ▼
          Protected Resources
```

Each stage depends on the previous one.

---

# Identification

## Overview

Identification is the process by which a user claims an identity.

Examples:

```
Username

Email Address

Employee ID

Customer Number

Phone Number
```

Example:

```
Username:

alice@example.com
```

The application now knows **who the user claims to be**, but has not yet verified the claim.

---

# Authentication

## Overview

Authentication verifies that the claimed identity is genuine.

Examples:

- Password
- One-Time Password (OTP)
- Hardware Security Key
- Biometrics
- Smart Card
- Digital Certificate

Authentication answers:

> "Can you prove you are Alice?"

---

# Authorization

## Overview

Authorization determines which resources an authenticated user may access.

Example:

```
Alice

↓

Authenticated

↓

Customer Role

↓

View Own Orders
```

Another example:

```
Administrator

↓

Authenticated

↓

Manage Users

Delete Accounts

View Audit Logs
```

Authorization decisions occur **after successful authentication**.

---

# Identification vs Authentication vs Authorization

| Concept | Question Answered | Example |
|----------|------------------|---------|
| Identification | Who are you? | Username or email |
| Authentication | Can you prove it? | Password, MFA, Passkey |
| Authorization | What can you access? | Role-based permissions |

Remember:

Identification ≠ Authentication

Authentication ≠ Authorization

These are separate security processes.

---

# Authentication Factors

Authentication is based on one or more factors.

---

## 1. Something You Know

Examples:

- Password
- PIN
- Security answer

```
User

↓

Password
```

---

## 2. Something You Have

Examples:

- Mobile phone
- Hardware token
- Smart card
- Security key

```
User

↓

Security Key
```

---

## 3. Something You Are

Examples:

- Fingerprint
- Face recognition
- Iris scan
- Voice recognition

```
User

↓

Fingerprint
```

---

## 4. Somewhere You Are (Contextual)

Examples:

- Office network
- GPS location
- Country
- Trusted corporate network

Used primarily as a **risk signal**, not a standalone authentication factor.

---

## 5. Something You Do (Behavioral)

Examples:

- Typing rhythm
- Mouse movement
- Walking pattern
- Touchscreen interaction

Behavioral biometrics are often used for continuous authentication and fraud detection.

---

# Single-Factor Authentication (SFA)

Only one authentication factor is used.

Example:

```
Username

↓

Password

↓

Access
```

Advantages:

- Simple
- Fast
- Low cost

Disadvantages:

- Password theft compromises the account.
- Vulnerable to phishing.
- Vulnerable to credential stuffing.

---

# Multi-Factor Authentication (MFA)

MFA requires two or more **different** authentication factors.

Example:

```
Username

↓

Password

↓

Authenticator App

↓

Access
```

Another example:

```
Username

↓

Password

↓

Hardware Security Key

↓

Access
```

Even if a password is stolen, attackers still require the second factor.

---

# Multi-Step vs Multi-Factor

These terms are often confused.

---

## Multi-Step Authentication

Example:

```
Password

↓

Security Question
```

Both are **something you know**.

This is **not** true MFA.

---

## True Multi-Factor Authentication

Example:

```
Password

↓

Hardware Security Key
```

Two different authentication factors are involved.

---

# Identity Lifecycle

Identity management begins before authentication and continues until the account is removed.

```
Registration

↓

Identity Verification

↓

Account Creation

↓

Authentication

↓

Session Management

↓

Password Changes

↓

Privilege Updates

↓

Account Suspension

↓

Account Deletion
```

Every stage should be secured.

---

# Registration Security

Secure registration should include:

- Email verification
- Phone verification (when appropriate)
- CAPTCHA or bot protection
- Strong password policy
- Duplicate account checks
- Secure password storage

Avoid:

- Weak default passwords
- Predictable usernames
- Automatic administrator privileges

---

# Account Recovery

Password recovery is a common attack target.

Typical workflow:

```
Forgot Password

↓

Identity Verification

↓

Reset Token

↓

New Password

↓

Login
```

Common mistakes include:

- Predictable reset tokens
- Long-lived reset links
- Missing expiration
- No rate limiting
- No notification after password reset

---

# Identity Proofing

Some applications require stronger verification before creating an account.

Examples:

- Government ID
- Employee verification
- Banking KYC (Know Your Customer)
- Video verification
- In-person verification

The required level depends on the application's risk profile.

---

# Authentication Architecture Example

```
                User
                  │
                  ▼
          Enter Username
                  │
                  ▼
        Verify User Exists
                  │
                  ▼
         Request Password
                  │
                  ▼
      Verify Password Hash
                  │
                  ▼
       Request Second Factor
                  │
                  ▼
      Verify MFA Challenge
                  │
                  ▼
      Create Authenticated Session
                  │
                  ▼
          Access Application
```

Each step should include appropriate validation, logging, and error handling.

---

# Common Authentication Failures

Examples include:

- Weak password policies
- Default passwords
- Missing MFA
- Predictable password reset tokens
- Session fixation
- Insecure session management
- Password reuse
- Credential stuffing susceptibility
- Missing account lockout
- Insecure "remember me" functionality

These weaknesses often lead directly to account compromise.

---

# Business Impact

Authentication failures can result in:

- Account takeover
- Identity theft
- Financial fraud
- Unauthorized transactions
- Data breaches
- Regulatory violations
- Loss of customer trust
- Privilege escalation
- Lateral movement within enterprise environments

---

# Key Takeaways

- Identification, authentication, and authorization are distinct but closely related security concepts.
- Authentication verifies identity using one or more authentication factors.
- True MFA combines different authentication factors rather than multiple credentials of the same type.
- The identity lifecycle includes registration, authentication, account recovery, and deprovisioning.
- Weak authentication mechanisms are a leading cause of account compromise and should be designed with layered security controls from the outset.

# Password Security

## Overview

Passwords remain the most widely used authentication mechanism.

Despite the growth of passwordless authentication, billions of users still authenticate using passwords every day.

Because passwords are frequently targeted by attackers, secure password handling is one of the most important responsibilities of an application.

---

# Password Lifecycle

```
User Creates Password

↓

Application Validates Policy

↓

Password Hashed

↓

Salt Added

↓

Stored Securely

↓

User Logs In

↓

Password Verified

↓

Access Granted
```

At no point should the original plaintext password be stored or recoverable.

---

# Strong Password Characteristics

A secure password should be:

- Long
- Unique
- Random
- Difficult to guess
- Not reused across services

Example:

```
CorrectHorseBatteryStaple!92
```

Long passphrases are generally easier for users to remember and harder for attackers to crack than short, complex passwords.

---

# Weak Password Examples

```
password

admin123

qwerty

welcome

company2024
```

Weak passwords are vulnerable to:

- Dictionary attacks
- Brute-force attacks
- Credential stuffing
- Password spraying

---

# Password Policies

A modern password policy should emphasize strength without creating unnecessary complexity.

Recommended practices include:

- Minimum length (e.g., 12–16 characters)
- Allow passphrases
- Block commonly used passwords
- Prevent reuse of recent passwords
- Encourage password managers
- Avoid arbitrary composition rules that reduce usability

Forced periodic password changes are generally discouraged unless there is evidence of compromise.

---

# Why Passwords Should Never Be Stored in Plaintext

Imagine the database contains:

```
Username        Password

Alice           MyPassword123

Bob             Admin@123
```

If the database is compromised, every password is immediately exposed.

Instead, applications should store only **password hashes**.

---

# Hashing

## Overview

A hash function converts data into a fixed-length value.

```
Password

↓

Hash Function

↓

Hash Value
```

Hashing is a **one-way operation**.

The original password should not be recoverable from the hash.

---

# Encryption vs Hashing

| Encryption | Hashing |
|------------|---------|
| Reversible with a key | One-way operation |
| Used to protect data | Used to verify passwords |
| Original data can be recovered | Original password should not be recoverable |

Passwords should be **hashed**, not encrypted.

---

# Password Verification

Registration:

```
Password

↓

Hash

↓

Database
```

Login:

```
Entered Password

↓

Hash

↓

Compare

↓

Match?

↓

Access
```

The application compares hashes, not plaintext passwords.

---

# Salt

## Overview

A salt is a random value added to each password before hashing.

Example:

```
Password

↓

Random Salt

↓

Hash
```

Every user should have a unique salt.

---

# Why Salt Matters

Without salt:

```
Alice

password123

↓

Hash A

Bob

password123

↓

Hash A
```

Both users have identical hashes.

With unique salts:

```
Alice

password123 + Salt1

↓

Hash X

Bob

password123 + Salt2

↓

Hash Y
```

Different hashes make large-scale attacks such as rainbow table attacks significantly less effective.

---

# Pepper

A pepper is an additional secret value stored separately from the password database.

```
Password

↓

Salt

↓

Pepper

↓

Hash
```

Unlike salts, peppers are not stored alongside password hashes.

If implemented, the pepper should be protected using secure key management.

---

# Password Hashing Algorithms

General-purpose hash functions such as MD5 and SHA-1 are **not appropriate for password storage** because they are too fast.

Modern password hashing algorithms are intentionally computationally expensive to slow down offline attacks.

---

## Argon2

Argon2 is widely regarded as the modern recommendation for password hashing.

Features:

- Memory-hard
- Configurable cost
- Resistant to GPU attacks
- Designed specifically for password storage

---

## bcrypt

bcrypt has been widely used for many years.

Advantages:

- Adaptive work factor
- Broad library support
- Proven in production

---

## scrypt

scrypt is another memory-hard password hashing algorithm.

Advantages:

- High memory requirements
- Increased resistance to specialized hardware attacks

---

## PBKDF2

PBKDF2 remains widely supported and is commonly used in enterprise environments.

It increases computational cost through many hashing iterations.

---

# Comparison of Password Hashing Algorithms

| Algorithm | Recommended | Memory Hard | Adaptive Cost |
|-----------|-------------|-------------|---------------|
| Argon2 | Yes | Yes | Yes |
| bcrypt | Yes | Limited | Yes |
| scrypt | Yes | Yes | Yes |
| PBKDF2 | Acceptable | No | Yes |
| SHA-256 | No (alone) | No | No |
| MD5 | No | No | No |

---

# Password Managers

Password managers help users create and store:

- Long passwords
- Unique passwords
- Random passwords

Benefits:

- Reduces password reuse
- Simplifies account management
- Improves overall password quality

Organizations should encourage, not discourage, password manager usage.

---

# Passwordless Authentication

Passwords are vulnerable to:

- Phishing
- Credential stuffing
- Password reuse
- Offline cracking

Passwordless authentication removes the shared secret entirely.

Examples include:

- Passkeys
- FIDO2 security keys
- Platform authenticators
- Biometrics (used locally to unlock credentials)

---

# Passkeys

Passkeys are a modern, phishing-resistant authentication method based on public-key cryptography.

Instead of storing a password, the device generates a **public/private key pair**.

Registration:

```
Device

↓

Generate Key Pair

↓

Public Key

↓

Server
```

The **private key never leaves the user's device**.

---

# Authentication with Passkeys

```
Server

↓

Challenge

↓

Device Signs Challenge

↓

Server Verifies Signature

↓

Login Successful
```

No password is transmitted or stored on the server.

---

# FIDO2

FIDO2 is an open authentication standard designed to support strong, phishing-resistant authentication.

It consists of:

- WebAuthn
- CTAP (Client to Authenticator Protocol)

FIDO2 enables authentication using:

- Security keys
- Built-in platform authenticators
- Passkeys

---

# WebAuthn

WebAuthn is a web standard that allows browsers to communicate securely with authenticators.

Supported authenticators include:

- USB security keys
- NFC security keys
- Platform authenticators
- Passkeys
- Biometrics (used to unlock local credentials)

---

# Hardware Security Keys

Examples include:

```
USB

NFC

Bluetooth
```

Authentication flow:

```
Username

↓

Insert Security Key

↓

Touch Key

↓

Authenticated
```

Advantages:

- Phishing resistant
- Strong cryptographic authentication
- Private keys remain on the device

---

# One-Time Passwords (OTP)

OTPs provide temporary authentication codes.

Common types:

- HOTP (counter-based)
- TOTP (time-based)

---

# Time-Based One-Time Password (TOTP)

Example:

```
Authenticator App

↓

6-digit Code

↓

30 Seconds

↓

Expires
```

Examples of authenticator applications include those implementing the TOTP standard.

---

# SMS OTP

SMS-based OTPs remain common but have limitations.

Risks include:

- SIM swapping
- SMS interception
- Mobile network attacks
- Social engineering

Where possible, authenticator apps or security keys provide stronger protection.

---

# Push Authentication

Authentication flow:

```
Login Attempt

↓

Push Notification

↓

Approve

↓

Authenticated
```

Benefits:

- Convenient
- No manual code entry

Potential risk:

Repeated prompts may lead users to approve malicious requests ("MFA fatigue").

---

# Authentication Method Comparison

| Method | Security | Phishing Resistance | User Convenience |
|---------|----------|--------------------|------------------|
| Password | Medium | Low | High |
| Password + TOTP | High | Moderate | Moderate |
| SMS OTP | Moderate | Low | High |
| Push Authentication | High | Moderate | High |
| Hardware Security Key | Very High | High | Moderate |
| Passkey (FIDO2/WebAuthn) | Very High | High | High |

---

# Key Takeaways

- Passwords should always be stored using modern password hashing algorithms such as Argon2, bcrypt, scrypt, or PBKDF2.
- Salts protect against precomputed attacks, while peppers add an additional layer of defense when managed securely.
- Password managers improve password quality and reduce reuse.
- Passwordless authentication eliminates many risks associated with shared secrets.
- FIDO2, WebAuthn, passkeys, and hardware security keys provide strong, phishing-resistant authentication and represent the direction of modern identity systems.