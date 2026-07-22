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

# Enterprise Authentication Protocols and Session Management

Modern authentication does not end after a user enters their password.

After successful authentication, applications must securely maintain the user's authenticated state while ensuring that attackers cannot steal, modify, or abuse it.

This is accomplished using:

- Sessions
- Cookies
- Tokens
- Identity Providers (IdP)
- Authentication Protocols
- Single Sign-On (SSO)

---

# Authentication vs Session Management

Authentication proves identity.

Session management maintains that authenticated identity.

```
User

↓

Login

↓

Authentication

↓

Session Created

↓

User Makes Requests

↓

Session Validated

↓

Access Granted
```

Without secure session management, authentication becomes meaningless.

---

# What is a Session?

A session is the server's way of remembering an authenticated user.

Instead of asking for the password on every request:

```
GET /profile

↓

Password?

↓

GET /orders

↓

Password?

↓

GET /settings

↓

Password?
```

The server creates a session after login.

Example:

```
Login

↓

Session ID Generated

↓

Browser Stores Cookie

↓

Every Request Includes Cookie
```

---

# Session Architecture

```
           User
             │
             ▼
        Login Request
             │
             ▼
      Authentication
             │
             ▼
Generate Session Identifier
             │
             ▼
 Store Session (Server)
             │
             ▼
 Session Cookie Sent
             │
             ▼
 Browser Stores Cookie
             │
             ▼
 Future Requests
             │
             ▼
Cookie Validated
             │
             ▼
Authenticated User
```

---

# Session Identifier

The session ID acts as the user's identity after login.

Example:

```
SESSIONID=81fd9381af81f9d8...
```

A secure session ID should be:

- Random
- Unpredictable
- Cryptographically secure
- Long enough to resist guessing

Never use:

```
SESSIONID=12345

SESSIONID=admin

SESSIONID=user1
```

Predictable identifiers enable session guessing attacks.

---

# Cookies

Sessions are commonly maintained using HTTP cookies.

Example:

```
Set-Cookie:

SESSIONID=abc123...
```

The browser automatically includes the cookie in future requests.

---

# Cookie Flow

```
Login

↓

Server

↓

Set-Cookie

↓

Browser Stores Cookie

↓

Future Requests

↓

Cookie Included

↓

Server Validates Session
```

---

# Important Cookie Attributes

## HttpOnly

```
Set-Cookie:

HttpOnly
```

Prevents JavaScript from reading the cookie.

Helps reduce the impact of Cross-Site Scripting (XSS).

---

## Secure

```
Set-Cookie:

Secure
```

Only transmits the cookie over HTTPS.

Never send authentication cookies over HTTP.

---

## SameSite

Controls when cookies are sent with cross-site requests.

Values:

```
Strict

Lax

None
```

Helps reduce Cross-Site Request Forgery (CSRF).

---

# Cookie Security

Good:

```
HttpOnly

Secure

SameSite=Lax
```

Better:

```
HttpOnly

Secure

SameSite=Strict
```

The appropriate value depends on application requirements.

---

# Session Timeout

Sessions should expire automatically.

Example:

```
Login

↓

30 Minutes Idle

↓

Session Expires
```

Benefits:

- Reduces risk from abandoned devices
- Limits session hijacking window
- Improves overall security

---

# Session Rotation

After authentication:

```
Old Session ID

↓

Login

↓

New Session ID
```

Changing the session ID after login helps prevent session fixation.

---

# Session Fixation

## Overview

In a session fixation attack, the attacker causes the victim to authenticate using a session ID already known to the attacker.

Example:

```
Attacker Creates Session

↓

Victim Uses Same Session

↓

Victim Logs In

↓

Attacker Reuses Session
```

---

## Prevention

- Generate a new session after login.
- Rotate session IDs after privilege changes.
- Never accept user-controlled session identifiers.

---

# Session Hijacking

## Overview

Instead of stealing passwords, attackers steal authenticated sessions.

Example:

```
Victim Logged In

↓

Session Cookie Stolen

↓

Attacker Uses Cookie

↓

Authenticated
```

Attack methods include:

- Cross-Site Scripting (XSS)
- Malware
- Network interception (without HTTPS)
- Device compromise

---

# Session Management Best Practices

- Use HTTPS everywhere.
- Rotate session identifiers.
- Set idle and absolute timeouts.
- Store sessions securely.
- Invalidate sessions on logout.
- Revoke sessions after password changes.
- Allow users to view and terminate active sessions.

---

# Token-Based Authentication

Many modern APIs use tokens instead of server-side sessions.

```
Login

↓

Server Issues Token

↓

Client Stores Token

↓

Client Sends Token

↓

Server Verifies Token
```

Common in:

- REST APIs
- Mobile applications
- Microservices
- Single Page Applications (SPA)

---

# JSON Web Token (JWT)

## Overview

JWT is a compact token format used to securely transmit claims.

Structure:

```
Header

.

Payload

.

Signature
```

Example:

```
xxxxx.yyyyy.zzzzz
```

---

# JWT Architecture

```
User Login

↓

Authentication

↓

JWT Generated

↓

Client Stores Token

↓

Authorization Header

↓

Server Verifies Signature

↓

Access Granted
```

---

# JWT Claims

Typical claims:

```
sub

iss

aud

exp

iat

role
```

Examples:

- Subject
- Issuer
- Audience
- Expiration
- Issued Time
- User Role

Never store sensitive secrets inside the JWT payload because it is only encoded, not encrypted.

---

# Access Tokens

Access tokens authorize API requests.

```
Login

↓

Access Token

↓

API Requests
```

Characteristics:

- Short lifetime
- Frequently renewed
- Limited scope

---

# Refresh Tokens

Refresh tokens obtain new access tokens without requiring the user to log in again.

```
Access Token Expired

↓

Refresh Token

↓

New Access Token
```

Refresh tokens should:

- Have longer lifetimes than access tokens.
- Be stored securely.
- Be revocable.

---

# OAuth 2.0

## Overview

OAuth 2.0 is an authorization framework.

It allows one application to access resources on behalf of a user without exposing the user's password.

Example:

```
User

↓

Google Login

↓

Website
```

The website never learns the user's Google password.

---

# OAuth 2.0 Components

```
Resource Owner

↓

Client

↓

Authorization Server

↓

Resource Server
```

Each component has a distinct role in the authorization process.

---

# OAuth Authorization Flow

```
User

↓

Client Application

↓

Authorization Server

↓

User Authenticates

↓

Authorization Code

↓

Access Token

↓

API Access
```

The Authorization Code Flow with PKCE is widely recommended for web and mobile applications.

---

# OpenID Connect (OIDC)

OAuth answers:

```
Can this application access the resource?
```

OIDC answers:

```
Who is the user?
```

OIDC extends OAuth 2.0 by adding an identity layer.

It introduces the **ID Token**, which contains information about the authenticated user.

---

# SAML

Security Assertion Markup Language (SAML) is an XML-based protocol commonly used for enterprise Single Sign-On.

Common environments:

- Corporate portals
- Government organizations
- Universities
- Legacy enterprise applications

Flow:

```
User

↓

Identity Provider

↓

SAML Assertion

↓

Application
```

---

# Identity Provider (IdP)

An Identity Provider authenticates users and issues authentication assertions or tokens.

Examples include enterprise identity platforms that support standards such as SAML, OAuth 2.0, and OpenID Connect.

---

# Service Provider (SP)

The Service Provider is the application that trusts the Identity Provider.

Example:

```
Identity Provider

↓

Authenticated User

↓

Service Provider

↓

Application Access
```

---

# Single Sign-On (SSO)

SSO allows users to authenticate once and access multiple applications.

```
Login Once

↓

Identity Provider

↓

Application A

Application B

Application C
```

Benefits:

- Improved user experience
- Centralized authentication
- Simplified account management
- Consistent security policies

---

# Common Authentication Mistakes

- Weak session identifiers
- Missing HTTPS
- Cookies without `HttpOnly` or `Secure`
- Long-lived sessions
- Missing logout invalidation
- Unsigned or improperly validated JWTs
- Excessive token lifetimes
- Storing secrets in JWT payloads
- Insecure refresh token storage
- Incorrect OAuth flow selection
- Accepting expired or malformed tokens

---

# Enterprise Authentication Flow

```
                User
                  │
                  ▼
         Identity Provider
                  │
      Authentication + MFA
                  │
                  ▼
        Identity Assertion
                  │
                  ▼
        Access / ID Token
                  │
                  ▼
         Service Provider
                  │
                  ▼
         Session Established
                  │
                  ▼
         Protected Resources
```

---

# Key Takeaways

- Authentication verifies identity, while session management preserves that authenticated state.
- Sessions and cookies must be protected using secure identifiers, HTTPS, and appropriate cookie attributes.
- Session fixation and session hijacking are common threats mitigated through session rotation, secure cookie handling, and proper invalidation.
- JWTs are widely used for token-based authentication but require careful validation and secure token lifecycle management.
- OAuth 2.0 provides delegated authorization, while OpenID Connect adds authentication and identity information.
- SAML and Single Sign-On enable centralized authentication for enterprise environments.
- Secure session and token management are as important as the initial authentication process.

# Authentication Attacks

Modern authentication systems are constantly targeted by attackers because compromising an account often provides direct access to sensitive data without requiring exploitation of software vulnerabilities.

The most common attacks target:

- Passwords
- Authentication workflows
- Session management
- Multi-Factor Authentication (MFA)
- Identity recovery mechanisms
- User behavior

---

# Credential Stuffing

## Overview

Credential stuffing is an attack where previously leaked username/password combinations are automatically tested against another application.

Attackers exploit the fact that many users reuse passwords across multiple services.

Example:

```
Data Breach

↓

Email + Password Leaked

↓

Automated Login Attempts

↓

Another Website

↓

Successful Login
```

---

## Why Credential Stuffing Works

Users frequently reuse passwords.

Example:

```
Netflix

↓

Password:

Summer@2025

↓

Bank

↓

Same Password

↓

Account Compromised
```

---

## Detection Indicators

Possible indicators include:

- High volume of failed logins
- Multiple usernames from one IP
- Multiple IPs targeting one account
- Known breached credentials
- Automated browser behavior
- Login attempts from unusual locations

---

## Prevention

- Multi-Factor Authentication
- Password managers
- Breached password detection
- Rate limiting
- Device fingerprinting
- Risk-based authentication

---

# Password Spraying

## Overview

Instead of trying many passwords for one account, attackers try one common password against many accounts.

Example:

```
Password:

Welcome@123

↓

Alice

Bob

Charlie

David

Emma
```

This avoids triggering traditional account lockout policies.

---

## Detection

Look for:

- One password attempted against many usernames
- Distributed login failures
- Authentication spikes
- Geographic anomalies

---

## Prevention

- MFA
- Strong password policies
- Detection rules
- Intelligent rate limiting
- Monitoring failed logins

---

# Brute Force Attack

## Overview

A brute force attack systematically tries many password combinations until one succeeds.

```
Password?

↓

123456

↓

password

↓

Admin123

↓

Correct Password
```

---

## Types

### Simple Brute Force

Every possible combination is attempted.

---

### Dictionary Attack

Uses lists of common passwords.

---

### Hybrid Attack

Combines:

- Dictionary words
- Numbers
- Symbols
- Predictable substitutions

Example:

```
password

↓

P@ssword123
```

---

## Prevention

- MFA
- Account lockout
- CAPTCHA (where appropriate)
- Rate limiting
- Password hashing
- Monitoring

---

# Account Enumeration

## Overview

Applications sometimes reveal whether a username exists.

Example:

Bad responses:

```
Unknown username
```

or

```
Incorrect password
```

Attackers can identify valid accounts before attempting password attacks.

---

## Secure Response

Always return a generic message:

```
Invalid username or password.
```

Avoid revealing which field was incorrect.

---

# MFA Fatigue Attack

## Overview

Attackers repeatedly trigger MFA push notifications until a user approves one by mistake.

Example:

```
Attacker

↓

Push Notification

↓

Reject

↓

Push Notification

↓

Reject

↓

Push Notification

↓

Approve

↓

Account Access
```

---

## Prevention

- Number matching
- User education
- Limit repeated prompts
- Risk-based authentication
- Hardware security keys

---

# SIM Swapping

## Overview

Attackers convince a mobile carrier to transfer a victim's phone number to a SIM card they control.

Result:

```
SMS OTP

↓

Attacker Receives Code

↓

Account Compromise
```

---

## Prevention

- Prefer authenticator apps or hardware keys over SMS
- Carrier account PINs
- User awareness
- Monitor phone number changes

---

# Authentication Bypass

Authentication bypass occurs when an attacker gains access without completing the intended authentication process.

Examples include:

- Logic flaws
- Misconfigured authentication checks
- Broken access control interactions
- Default credentials
- Insecure debug functionality

---

# Session Theft

Attackers may steal authenticated sessions through:

- Cross-Site Scripting (XSS)
- Malware
- Browser compromise
- Physical access
- Insecure networks (without HTTPS)

---

# Detection

Authentication monitoring should include:

## Login Events

Monitor:

- Successful logins
- Failed logins
- Password resets
- Account lockouts
- MFA failures
- New device registrations
- Session creation
- Session termination

---

## Behavioral Analytics

Look for:

- Impossible travel
- New countries
- New devices
- Unusual login times
- Multiple failed attempts
- High-risk IP addresses
- Anonymous proxies or VPNs (where relevant)

---

## Security Logs

Important authentication events include:

```
Authentication Success

Authentication Failure

Password Reset

MFA Enrollment

MFA Failure

Account Locked

Privilege Change

Session Created

Session Destroyed
```

---

# Prevention

A secure authentication system should implement layered controls.

---

## Strong Authentication

- MFA
- Passkeys
- FIDO2/WebAuthn
- Hardware security keys

---

## Password Security

- Argon2, bcrypt, scrypt, or PBKDF2
- Unique salts
- Strong password policy
- Password managers
- Breached password detection

---

## Session Security

- HTTPS
- Secure cookies
- HttpOnly
- SameSite
- Session rotation
- Session expiration
- Logout invalidation

---

## Monitoring

- Centralized logging
- SIEM integration
- UEBA (User and Entity Behavior Analytics)
- Alerting
- Threat intelligence integration

---

# Best Practices

✔ Enforce MFA for all privileged accounts.

✔ Encourage password manager usage.

✔ Never store plaintext passwords.

✔ Hash passwords using modern password hashing algorithms.

✔ Rotate session identifiers after authentication.

✔ Protect cookies using `HttpOnly`, `Secure`, and appropriate `SameSite` settings.

✔ Implement account lockout or adaptive throttling to slow automated attacks.

✔ Monitor authentication events and investigate anomalies.

✔ Review authentication logs regularly.

✔ Prefer phishing-resistant authentication methods such as passkeys or hardware security keys.

---

# Practical Lab

## Objective

Evaluate the authentication security of a web application.

---

## Scenario

The application provides:

- User registration
- Login
- Password reset
- MFA
- Session management

---

## Tasks

1. Review the password policy.
2. Verify passwords are securely hashed.
3. Test account lockout behavior.
4. Evaluate password reset workflow.
5. Assess MFA implementation.
6. Inspect cookie attributes.
7. Review session expiration.
8. Attempt account enumeration.
9. Review authentication logs.
10. Recommend improvements.

---

## Expected Learning Outcomes

After completing this lab, you should be able to:

- Identify authentication weaknesses.
- Assess session management.
- Evaluate MFA implementation.
- Recommend secure authentication controls.
- Understand common authentication attack techniques.

---

# Interview Questions

## Beginner

### What is the difference between identification, authentication, and authorization?

- **Identification** is claiming an identity (e.g., username or email).
- **Authentication** verifies that claimed identity (e.g., password, MFA, passkey).
- **Authorization** determines what an authenticated user is allowed to access.

---

### Why should passwords be hashed instead of encrypted?

Hashing is a one-way process designed for password verification. Encryption is reversible with a key, making it unsuitable as the primary mechanism for password storage.

---

### What is Multi-Factor Authentication (MFA)?

MFA requires two or more different authentication factors (such as a password and a hardware security key), making account compromise significantly more difficult.

---

## Intermediate

### What is credential stuffing?

Credential stuffing uses leaked username/password pairs from previous data breaches to attempt automated logins on other services where users may have reused the same credentials.

---

### Why is Argon2 recommended for password hashing?

Argon2 is memory-hard, configurable, and specifically designed for secure password storage, making offline password cracking more expensive for attackers.

---

### Explain the difference between OAuth 2.0 and OpenID Connect.

OAuth 2.0 is an authorization framework that allows delegated access to resources. OpenID Connect builds on OAuth 2.0 by adding an identity layer for user authentication through ID tokens.

---

## Advanced

### How would you design a secure authentication system?

A secure design should include:

1. Strong password hashing (Argon2, bcrypt, scrypt, or PBKDF2).
2. MFA or phishing-resistant authentication (passkeys/FIDO2).
3. Secure session management.
4. HTTPS everywhere.
5. Rate limiting and account protection.
6. Secure password recovery.
7. Centralized logging and monitoring.
8. Risk-based authentication.
9. Regular security testing and reviews.

---

### How would you investigate suspected credential stuffing in a SOC?

A structured approach includes:

1. Review authentication logs for spikes in failed logins.
2. Identify affected accounts and IP addresses.
3. Correlate with threat intelligence (known breached credentials or malicious IPs).
4. Check for successful logins following repeated failures.
5. Force password resets for impacted users if necessary.
6. Require MFA enrollment or re-verification.
7. Block or throttle malicious sources.
8. Document findings and tune detection rules.

---

# References

## OWASP

- OWASP Top 10 (2021)
- OWASP Authentication Cheat Sheet
- OWASP Session Management Cheat Sheet
- OWASP Password Storage Cheat Sheet
- OWASP Multifactor Authentication Cheat Sheet

## NIST

- NIST SP 800-63 Digital Identity Guidelines
- NIST Cybersecurity Framework (CSF)
- NIST Secure Software Development Framework (SSDF)

## FIDO Alliance

- FIDO2 Specifications
- WebAuthn Guidance

## IETF

- OAuth 2.0
- OpenID Connect
- JSON Web Token (JWT)

---

# Summary

Identification and Authentication Failures remain one of the most common causes of account compromise. Secure authentication requires more than strong passwords—it demands a layered approach that includes modern password hashing, phishing-resistant MFA, secure session management, robust account recovery, continuous monitoring, and risk-based controls. Organizations should adopt standards such as OAuth 2.0, OpenID Connect, WebAuthn, and FIDO2 where appropriate, while continuously monitoring authentication events to detect and respond to credential attacks and unauthorized access attempts.