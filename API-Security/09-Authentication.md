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

# Passwordless Authentication

Passwordless authentication eliminates traditional passwords and replaces them with stronger authentication mechanisms.

Common passwordless technologies include:

- Passkeys
- FIDO2
- WebAuthn
- Hardware Security Keys
- Biometrics
- Certificate-Based Authentication

Benefits

- Eliminates password reuse
- Reduces phishing attacks
- Removes password reset overhead
- Improves user experience
- Strengthens enterprise security

---

# Passwordless Authentication Flow

```
          User

            │

            ▼

    Authentication Request

            │

            ▼

      Device Authenticator

            │

   Biometric / PIN / Key

            │

            ▼

     Signed Challenge

            │

            ▼

 Authentication Server

            │

 Signature Verified

            ▼

 Access Granted
```

No password is transmitted or stored during authentication.

---

# Passkeys

Passkeys are a modern authentication technology based on public-key cryptography.

Instead of storing passwords,

the system stores:

- Public Key
- User Identifier
- Credential Metadata

The private key never leaves the user's trusted device.

---

# Passkey Registration

```
User

 │

Create Account

 │

Generate Key Pair

 │

Private Key

Stored Securely

 │

Public Key

Sent to Server

 ▼

Registration Complete
```

---

# Passkey Authentication

```
Login

 │

Server Sends Challenge

 │

Private Key Signs Challenge

 │

Signature Returned

 │

Server Verifies Signature

 ▼

Authenticated
```

Since the private key never leaves the device,

credential theft becomes significantly more difficult.

---

# FIDO2

FIDO2 is an open authentication standard developed by the FIDO Alliance.

It combines:

- WebAuthn
- CTAP (Client to Authenticator Protocol)

Supports:

- Passwordless login
- MFA
- Hardware authenticators
- Platform authenticators

---

# WebAuthn

Web Authentication (WebAuthn) is a W3C standard supported by modern browsers.

Example

```
Browser

 │

WebAuthn API

 │

Authenticator

 │

Cryptographic Signature

 ▼

Authentication
```

Benefits

- Resistant to phishing
- Resistant to replay attacks
- No shared secrets
- Strong cryptography

---

# Platform Authenticators

Examples

- Windows Hello
- Apple Face ID
- Apple Touch ID
- Android Biometrics

These authenticators are built into user devices.

---

# Roaming Authenticators

External authenticators include:

- YubiKey
- Feitian Keys
- Smart Cards
- NFC Security Keys
- USB Security Keys

Useful for enterprise environments.

---

# Certificate-Based Authentication

Certificates authenticate users or devices using Public Key Infrastructure (PKI).

```
Client

 │

Certificate

 ▼

Server

 │

Certificate Validation

 ▼

Authenticated
```

Commonly used for:

- Enterprise VPNs
- Device authentication
- Internal APIs
- Government systems

---

# Mutual TLS (mTLS)

Mutual TLS authenticates both parties.

Normal HTTPS

```
Client

 │

Verify Server

 ▼

Secure Connection
```

Mutual TLS

```
Client

 │

Verify Server

 │

Server Verifies Client

 ▼

Mutually Authenticated
```

Widely used for service-to-service communication.

---

# API Key Authentication

API keys uniquely identify applications accessing APIs.

Example

```
GET /api/users

X-API-Key:

abc123xyz
```

API keys authenticate applications,

not end users.

---

# API Key Lifecycle

```
Generate Key

      │

Distribute

      │

Use

      │

Rotate

      │

Revoke

      ▼

Archive
```

Keys should be rotated regularly.

---

# API Key Best Practices

Use

- Long random values
- Secure storage
- HTTPS
- Rotation
- Usage monitoring
- Least privilege

Avoid

- Hardcoding keys
- Sharing keys
- Logging keys
- Embedding keys in client-side JavaScript

---

# Service Accounts

Service accounts authenticate applications rather than humans.

Examples

```
Microservice A

↓

Microservice B
```

```
CI/CD Pipeline

↓

Cloud Platform
```

Security recommendations

- Least privilege
- Secret rotation
- Separate identities
- Audit logging

---

# Machine-to-Machine Authentication

```
Application A

 │

JWT

Certificate

API Key

 ▼

API Gateway

 │

Authentication

 ▼

Application B
```

Machine identities should be managed separately from human users.

---

# Single Sign-On (SSO)

Single Sign-On allows users to authenticate once and access multiple applications.

```
User

 │

Login

 ▼

Identity Provider

 │

Authenticated

 ├──────────────┐

 ▼              ▼

App A        App B

       ▼

App C
```

Benefits

- Improved user experience
- Centralized identity management
- Reduced password fatigue
- Easier auditing

---

# Identity Provider (IdP)

An Identity Provider manages authentication.

Examples include:

- Microsoft Entra ID
- Okta
- Keycloak
- Ping Identity
- ForgeRock

Responsibilities

- Identity verification
- Credential management
- MFA
- Token issuance
- Federation

---

# Service Provider (SP)

A Service Provider relies on an Identity Provider.

```
Identity Provider

 │

Authentication

 ▼

Service Provider

 │

Grant Access
```

Examples

- SaaS applications
- Enterprise portals
- Cloud services

---

# Federation

Federation enables identity sharing across organizations.

```
Company A

 │

Identity Provider

 │

Trust

 ▼

Company B

Applications
```

Users authenticate with their home organization.

---

# Kerberos

Kerberos is a ticket-based authentication protocol.

Workflow

```
User

 │

Authentication Server

 │

Ticket Granting Ticket

 │

Service Ticket

 ▼

Application
```

Commonly used in Microsoft Active Directory environments.

---

# Security Assertion Markup Language (SAML)

SAML is an XML-based authentication standard used primarily for enterprise SSO.

```
User

 │

Identity Provider

 │

SAML Assertion

 ▼

Service Provider

 ▼

Access
```

SAML is commonly used with:

- Enterprise portals
- HR systems
- Business applications

---

# Authentication Attacks

Common attacks include:

- Credential stuffing
- Password spraying
- Brute force
- Phishing
- MFA fatigue
- Session hijacking
- Replay attacks
- Token theft
- API key leakage
- Certificate theft

---

# Brute Force Attack

```
Attacker

 │

Password Guess

 │

Password Guess

 │

Password Guess

 ▼

Login
```

Mitigations

- Rate limiting
- MFA
- Account lockout
- CAPTCHA (where appropriate)
- Monitoring

---

# Credential Stuffing

Attackers reuse credentials leaked from unrelated breaches.

```
Leaked Database

 │

Credentials

 ▼

Target Website
```

Mitigations

- MFA
- Breached password detection
- Passwordless authentication
- Login anomaly detection

---

# Password Spraying

Instead of many passwords against one account,

attackers try one common password against many accounts.

```
Password123!

↓

User1

User2

User3

User4
```

Mitigations

- MFA
- Smart lockout
- Detection rules
- Strong password policies

---

# Phishing

```
Victim

 │

Fake Login Page

 │

Credentials Entered

 ▼

Attacker
```

Mitigations

- Passkeys
- FIDO2
- User awareness
- Email security
- MFA

---

# MFA Fatigue Attack

Attackers repeatedly trigger MFA prompts hoping the user approves one.

```
Repeated MFA Requests

↓

User Fatigue

↓

Approval

↓

Compromise
```

Mitigations

- Number matching
- Push throttling
- Risk-based authentication
- User education

---

# Replay Attack

Captured authentication data is resent.

```
Captured Token

↓

Replay

↓

Unauthorized Access
```

Mitigations

- Nonces
- Short-lived tokens
- TLS
- Token binding where applicable

---

# Session Hijacking

```
Session Cookie

↓

Stolen

↓

Attacker

↓

Authenticated Session
```

Mitigations

- Secure cookies
- HttpOnly
- SameSite
- HTTPS
- Session expiration

---

# Authentication Logging

Log

- Successful logins
- Failed logins
- Password changes
- Password resets
- MFA enrollment
- MFA failures
- Token issuance
- Token revocation
- Account lockouts
- Device registration

Avoid logging:

- Passwords
- Secrets
- API Keys
- Tokens
- Private Keys

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Brute Force | Multiple failed logins from one source |
| Password Spraying | One password attempted across many accounts |
| Credential Stuffing | Many usernames with known breached patterns |
| Impossible Travel | Logins from distant locations within unrealistic timeframes |
| MFA Fatigue | Excessive MFA prompts followed by approval |
| API Key Abuse | Key used from unexpected networks or regions |
| Certificate Misuse | Unexpected client certificate usage |
| Service Account Abuse | Interactive login using service account credentials |
| Token Replay | Same token observed from multiple devices simultaneously |

Detection thresholds should be tailored to normal enterprise behavior.

---

# SIEM Integration

Recommended log sources

```
Identity Provider

        │

Authentication Server

        │

API Gateway

        │

VPN

        │

Cloud Identity

        │

Web Applications

        ▼

Enterprise SIEM

        │

Correlation Rules

        ▼

SOC Alerts
```

Example correlation rules

- Five consecutive failed logins followed by a successful login
- New device registration followed by privileged access
- Multiple password reset requests for one account
- Service account authenticating from an interactive workstation
- API key suddenly used from multiple geographic regions

---

# Enterprise Authentication Architecture

```
                    Internet

                        │

                        ▼

                  Load Balancer

                        │

                        ▼

                  API Gateway

                        │

                        ▼

                Identity Provider

                        │

            MFA / Passkeys / FIDO2

                        │

                        ▼

             Token / Session Issuance

                        │

                        ▼

             Applications & APIs

                        │

                        ▼

             Logging & Monitoring

                        │

                        ▼

                 SIEM / SOC
```

---

# Hands-on Lab 1 – Password Policy Assessment

**Objective**

Review the password policy of an authorized application.

**Steps**

1. Examine password requirements.
2. Verify minimum length and support for long passphrases.
3. Check whether common or breached passwords are rejected.
4. Confirm that password changes require appropriate verification.

**Learning Outcomes**

- Password policy analysis
- Authentication assessment
- Secure credential management

---

# Hands-on Lab 2 – MFA Verification

**Objective**

Assess Multi-Factor Authentication implementation.

**Steps**

1. Enroll a test account in MFA.
2. Verify login with multiple factors.
3. Confirm recovery procedures are secure.
4. Review MFA-related logging.

**Learning Outcomes**

- MFA validation
- Authentication workflow analysis
- Enterprise identity controls

---

# Hands-on Lab 3 – API Key Security Review

**Objective**

Review API key management in an authorized environment.

**Steps**

1. Identify where API keys are generated.
2. Verify secure storage and transmission.
3. Review rotation and revocation procedures.
4. Confirm usage is logged and monitored.

**Learning Outcomes**

- API key lifecycle management
- Secret handling
- Operational security

---

# Common Security Mistakes

Avoid:

- Storing plaintext passwords
- Weak password hashing algorithms
- Missing MFA for privileged users
- Hardcoded API keys
- Long-lived authentication tokens
- Shared service accounts
- Logging secrets
- Weak password reset workflows
- Ignoring authentication anomalies
- Failing to rotate credentials

---

# Troubleshooting

## Users Cannot Authenticate

Possible causes

- Incorrect credentials
- Expired password
- Disabled account
- Authentication service outage

---

## MFA Failures

Possible causes

- Time synchronization issues
- Lost authenticator device
- Push notification delays
- Incorrect recovery configuration

---

## API Key Rejected

Possible causes

- Revoked key
- Expired key
- Incorrect permissions
- IP restrictions

---

## Certificate Authentication Failure

Possible causes

- Expired certificate
- Untrusted certificate authority
- Revoked certificate
- Incorrect client configuration

---

## Unexpected Account Lockouts

Possible causes

- Password spraying
- Automated tools
- User error
- Synchronization problems

---

# Interview Questions

## Fundamental

1. What is authentication?
2. How does authentication differ from authorization?
3. What are the three authentication factors?
4. What is Multi-Factor Authentication?
5. Why are passwords hashed instead of encrypted?
6. What is a passkey?
7. What is FIDO2?
8. What is an API key?
9. What is Single Sign-On?
10. What is an Identity Provider?

---

## Intermediate

11. Explain password salting.
12. Compare passkeys and passwords.
13. What are the security advantages of WebAuthn?
14. How would you secure service accounts?
15. Explain mutual TLS authentication.
16. What is credential stuffing?
17. How would you detect password spraying?
18. Why should authentication events be logged?
19. How should API keys be managed throughout their lifecycle?
20. What authentication events should be forwarded to a SIEM?

---

## Scenario-Based

**Scenario 1**

Your SOC observes thousands of failed login attempts against many accounts, all using the same password.

- Which attack does this indicate?
- How would you investigate and contain it?

---

**Scenario 2**

A developer accidentally commits an API key to a public repository.

- What immediate actions should be taken?
- How can similar incidents be prevented in the future?

---

**Scenario 3**

An executive reports receiving repeated MFA approval prompts despite not attempting to sign in.

- What attack might this represent?
- Which controls would you implement to reduce future risk?

---

# Chapter Summary

In this chapter, we explored authentication and enterprise identity verification.

We covered:

- Authentication fundamentals
- Authentication factors
- Password security
- Passkeys
- FIDO2 and WebAuthn
- API keys
- Mutual TLS
- SAML
- Kerberos
- Single Sign-On
- Authentication attacks
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Strong authentication forms the foundation of secure APIs, applications, cloud environments, and enterprise identity systems.

---

# Chapter Review

You should now be able to answer:

- How does authentication differ from authorization?
- Why are passkeys more resistant to phishing than passwords?
- How should passwords be securely stored?
- When should API keys, certificates, or federated identity be used?
- How can authentication attacks such as credential stuffing and password spraying be detected?
- Which authentication events should be monitored by a SIEM?
- How would you design an enterprise authentication architecture using MFA and an Identity Provider?

If you can confidently answer these questions, you are ready to continue with **Chapter 10 – Authorization**, where you'll learn how authenticated identities are granted permissions using RBAC, ABAC, ACLs, policy engines, and modern authorization frameworks.

---

# References

## Standards

- FIDO2 Specifications
- WebAuthn Level 3
- RFC 6749 – OAuth 2.0
- RFC 5280 – X.509 PKI
- RFC 4120 – Kerberos
- OASIS SAML 2.0

## Security Standards

- NIST SP 800-63 Digital Identity Guidelines
- OWASP ASVS
- OWASP Authentication Cheat Sheet
- OWASP API Security Top 10
- NIST Cybersecurity Framework (CSF)

## Further Reading

- FIDO Alliance Documentation
- WebAuthn Developer Guide
- Enterprise Identity Best Practices

---

# What's Next?

➡️ **Chapter 10 – Authorization**

In the next chapter, we will explore:

- Authorization fundamentals
- RBAC
- ABAC
- ACLs
- Policy-Based Access Control (PBAC)
- Object-Level Authorization
- Function-Level Authorization
- Least Privilege
- Zero Trust authorization
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions