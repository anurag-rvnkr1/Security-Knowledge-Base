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