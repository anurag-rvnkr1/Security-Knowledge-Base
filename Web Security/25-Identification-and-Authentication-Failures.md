# 25-Identification-and-Authentication-Failures.md

# Part 1 — Fundamentals of Identification & Authentication Failures, Identity Management, Authentication Lifecycle, and Enterprise Overview

> **"Authentication answers *Who are you?* Authorization answers *What are you allowed to do?* Confusing these two concepts has led to some of the most significant security incidents in modern applications."**

---

# Learning Objectives

After completing this part, you will understand:

- OWASP A07:2021 Overview
- Identification vs Authentication vs Authorization
- Digital Identity
- Authentication Factors
- Authentication Lifecycle
- Identity Providers (IdP)
- Credential Management
- Session Creation
- Enterprise Authentication Architecture
- Defense in Depth

---

# What are Identification and Authentication Failures?

**Identification and Authentication Failures** occur when an application incorrectly identifies users, improperly verifies their identity, or fails to securely manage authentication throughout the user session.

These failures can lead to:

- Unauthorized account access
- Account takeover
- Identity impersonation
- Unauthorized transactions
- Data exposure
- Business disruption

---

# Authentication Terminology

Authentication systems rely on several related concepts.

| Term | Purpose |
|------|----------|
| Identification | Claiming an identity |
| Authentication | Verifying the claimed identity |
| Authorization | Determining permitted actions |
| Accounting | Recording security events |

---

# Identification

Identification is the process of claiming an identity.

```
User

↓

Username

↓

Email Address

↓

Employee ID

↓

Identity Claimed
```

At this stage, the system has **not yet verified** the user's identity.

---

# Authentication

Authentication verifies that the claimed identity is genuine.

```
Identity Claimed

↓

Credential Verification

↓

Identity Confirmed

↓

Authenticated Session
```

Authentication provides confidence that the user is who they claim to be.

---

# Authorization

Authorization occurs **after successful authentication**.

```
Authenticated User

↓

Permission Check

↓

Resource Access

↓

Allowed

OR

Denied
```

Authentication and authorization are separate security processes.

---

# Authentication Flow

```
User

↓

Identify

↓

Authenticate

↓

Authorize

↓

Access Resource
```

Each step depends on the successful completion of the previous one.

---

# Digital Identity

A digital identity represents a user within an information system.

```
Digital Identity

│

├── Username

├── Employee ID

├── Email Address

├── Roles

├── Groups

├── Attributes

└── Permissions
```

Identity information supports authentication and authorization decisions.

---

# Authentication Factors

Authentication factors are grouped into different categories.

```
Authentication Factors

│

├── Something You Know

├── Something You Have

├── Something You Are

├── Somewhere You Are

└── Something You Do
```

Using multiple independent factors generally improves assurance.

---

# Something You Know

Examples include:

- Password
- PIN
- Passphrase
- Security answer

Knowledge-based factors should be protected with strong credential policies.

---

# Something You Have

Examples include:

- Hardware security key
- Mobile authenticator application
- Smart card
- One-time password (OTP) device

Possession-based factors complement knowledge-based authentication.

---

# Something You Are

Biometric examples include:

- Fingerprint
- Face recognition
- Iris recognition
- Voice recognition

Biometric systems should be implemented with appropriate privacy protections.

---

# Authentication Methods

| Method | Example |
|---------|----------|
| Password-based | Username + Password |
| Certificate-based | Client Certificate |
| Token-based | Security Token |
| Multi-Factor Authentication (MFA) | Password + Authenticator App |
| Passwordless | Passkey or Security Key |

Different applications require different authentication methods depending on business and security requirements.

---

# Authentication Lifecycle

```
User Registration

↓

Identity Verification

↓

Credential Creation

↓

Login

↓

Session Creation

↓

Resource Access

↓

Logout

↓

Session Termination
```

Security controls should exist throughout the entire lifecycle.

---

# Credential Management

Credentials require secure lifecycle management.

```
Create

↓

Store Securely

↓

Verify

↓

Rotate

↓

Recover

↓

Retire
```

Credential management should include strong storage, recovery, and revocation procedures.

---

# Identity Providers (IdP)

Many enterprise environments centralize authentication.

```
User

↓

Identity Provider

↓

Authentication

↓

Application
```

This enables consistent identity management across multiple applications.

---

# Enterprise Authentication Architecture

```
             User

               │

               ▼

        Identity Provider

               │

      ┌────────┼────────┐

      ▼        ▼        ▼

   HR Portal CRM Portal Finance Portal
```

Centralized identity simplifies user management and improves consistency.

---

# Authentication vs Authorization

| Authentication | Authorization |
|---------------|---------------|
| Verifies identity | Verifies permissions |
| Occurs first | Occurs after authentication |
| Login process | Access control process |
| Identity focused | Resource focused |

Both are required for secure applications.

---

# Session Creation

After successful authentication:

```
Authenticate

↓

Create Session

↓

Assign Identity

↓

Access Resources
```

Sessions should be securely managed throughout their lifetime.

---

# Enterprise Authentication Workflow

```
User

↓

Identity Verification

↓

Authentication

↓

Session Creation

↓

Authorization

↓

Application Access

↓

Audit Logging
```

Each stage contributes to overall application security.

---

# Defense in Depth

Authentication should be supported by multiple security layers.

```
Identity

↓

Authentication

↓

Authorization

↓

Logging

↓

Monitoring

↓

Incident Response
```

No single security control should be relied upon exclusively.

---

# Enterprise Example

A corporate employee portal:

```
Employee

↓

Identity Provider

↓

Multi-Factor Authentication

↓

Corporate Portal

↓

Business Applications
```

Authentication is centralized while authorization remains application-specific.

---

# Common Authentication Failures

| Failure | Potential Impact |
|---------|------------------|
| Weak password policy | Increased risk of account compromise |
| Missing MFA | Reduced identity assurance |
| Poor session management | Unauthorized session use |
| Weak credential storage | Credential exposure |
| Insecure recovery process | Unauthorized account recovery |
| Excessive trust | Unauthorized access |

---

# Enterprise Authentication Lifecycle

```
Registration

↓

Identity Verification

↓

Authentication

↓

Session Management

↓

Continuous Monitoring

↓

Logout
```

Authentication security extends beyond the login page.

---

# Hands-on Lab (Conceptual)

1. Draw the authentication workflow of a sample web application.
2. Identify authentication and authorization stages.
3. List authentication factors used by the application.
4. Identify where sessions are created and terminated.
5. Document security controls at each stage.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is identification?
2. What is authentication?
3. How does authentication differ from authorization?
4. What is a digital identity?
5. What are authentication factors?
6. What is an Identity Provider (IdP)?
7. Why is MFA considered stronger than single-factor authentication?
8. What happens after successful authentication?
9. Why is session management important?
10. Why should authentication be considered throughout the user lifecycle?

---

# Best Practices

- Separate identification, authentication, and authorization responsibilities.
- Centralize identity management where appropriate.
- Support strong, modern authentication mechanisms.
- Protect credentials throughout their lifecycle.
- Apply defense in depth around authentication systems.
- Monitor authentication events and maintain audit logs.
- Review authentication architecture periodically.

---

# Common Mistakes

- Confusing authentication with authorization.
- Using weak or outdated authentication methods.
- Failing to secure credential storage.
- Ignoring session lifecycle management.
- Treating login as the only authentication concern.
- Assuming authenticated users automatically have appropriate permissions.

---

# Key Takeaways

- Identification claims an identity, while authentication verifies it.
- Authorization is a separate process that determines what authenticated users may access.
- Authentication is a lifecycle that includes registration, credential management, session creation, and logout.
- Identity Providers help centralize authentication in enterprise environments.
- Strong authentication architecture combines secure identity management, credential protection, session management, logging, and monitoring.

# 25-Identification-and-Authentication-Failures.md

# Part 2 — Password Security, Multi-Factor Authentication (MFA), Passwordless Authentication, Session Security, and Enterprise Identity Protection

> **"Strong authentication is not achieved by a strong password alone. It is achieved through multiple, layered controls that verify identity, protect credentials, and continuously secure user sessions."**

---

# Learning Objectives

After completing this part, you will understand:

- Password Security
- Password Policies
- Password Storage
- Password Managers
- Multi-Factor Authentication (MFA)
- Passwordless Authentication
- Passkeys
- Session Management
- Account Recovery
- Enterprise Identity Protection

---

# Password Security

Passwords remain one of the most widely used authentication mechanisms.

A secure password system should address:

- Password creation
- Secure storage
- Secure verification
- Password updates
- Password recovery
- Password retirement

```
User

↓

Create Password

↓

Secure Storage

↓

Authentication

↓

Session

↓

Logout
```

---

# Characteristics of Strong Passwords

A good password should be:

```
Strong Password

│

├── Long

├── Unique

├── Difficult to Guess

├── Random

└── Used for One Account Only
```

Length and uniqueness generally contribute more to security than overly complex composition rules alone.

---

# Password Policy

Organizations typically define password policies covering:

| Policy | Purpose |
|----------|----------|
| Minimum Length | Improve resistance to guessing |
| Maximum Length | Support passphrases |
| Password Reuse Restrictions | Prevent repeated use |
| Account Lockout | Reduce repeated login attempts |
| Password History | Prevent immediate reuse |
| Password Change Process | Secure credential updates |

Policies should balance usability with security.

---

# Password Lifecycle

```
Create

↓

Store

↓

Verify

↓

Update

↓

Recover

↓

Retire
```

Passwords should be protected during every stage of their lifecycle.

---

# Password Storage

Applications should **never** store passwords in plaintext.

Instead:

```
Password

↓

Hash Function

↓

Stored Hash

↓

Database
```

During login:

```
User Password

↓

Hash Function

↓

Compare

↓

Authentication Result
```

This allows verification without storing the original password.

---

# Characteristics of Secure Password Storage

```
Password Storage

│

├── One-Way Hashing

├── Unique Salt

├── Modern Password Hashing Algorithm

├── Secure Configuration

└── Periodic Review
```

Password storage should follow current industry recommendations.

---

# Password Managers

Password managers help users maintain strong, unique passwords.

Benefits include:

```
Password Manager

│

├── Unique Passwords

├── Long Passwords

├── Secure Storage

├── Autofill

└── Reduced Password Reuse
```

Organizations often encourage their use as part of security awareness programs.

---

# Multi-Factor Authentication (MFA)

MFA combines multiple independent authentication factors.

```
User

↓

Password

↓

Authenticator App

↓

Authentication Complete
```

Compromising one factor alone is generally insufficient for access.

---

# Common MFA Factors

| Factor | Example |
|----------|----------|
| Knowledge | Password |
| Possession | Security Key |
| Possession | Authenticator Application |
| Possession | Smart Card |
| Biometrics | Fingerprint |
| Biometrics | Face Recognition |

Using factors from different categories provides stronger assurance.

---

# MFA Authentication Flow

```
User

↓

Username

↓

Password

↓

Second Factor

↓

Authenticated Session
```

Authentication succeeds only after all required factors are verified.

---

# Enterprise MFA Architecture

```
Employee

↓

Identity Provider

↓

Password

↓

Authenticator

↓

Business Applications
```

Centralized MFA simplifies identity management across enterprise systems.

---

# Passwordless Authentication

Modern authentication increasingly reduces dependence on passwords.

```
User

↓

Device Verification

↓

Authentication

↓

Application
```

Passwordless methods aim to improve both security and user experience.

---

# Passkeys

Passkeys are a modern authentication technology that enables passwordless sign-in using cryptographic credentials managed by trusted devices.

General benefits include:

```
Passkeys

│

├── Improved User Experience

├── Reduced Password Reuse

├── Device-Based Authentication

├── Strong Cryptography

└── Simplified Sign-In
```

Passkeys are increasingly supported across modern platforms and browsers.

---

# Session Management

After authentication, applications establish a session.

```
Authentication

↓

Session Created

↓

Authenticated Requests

↓

Logout

↓

Session Destroyed
```

Sessions represent authenticated users and should be protected appropriately.

---

# Session Lifecycle

```
Login

↓

Session Creation

↓

Session Validation

↓

Session Renewal

↓

Logout

↓

Session Termination
```

Applications should manage sessions throughout their lifetime.

---

# Session Timeout

Sessions should not remain active indefinitely.

Common timeout strategies include:

```
Session

↓

Inactive

↓

Timeout

↓

Reauthentication
```

Timeout policies help reduce the impact of unattended authenticated sessions.

---

# Session Invalidation

Sessions should be invalidated when appropriate.

Examples include:

- User logout
- Password change
- Account disablement
- Administrative session termination
- Extended inactivity

Proper invalidation helps prevent unintended continued access.

---

# Secure Cookies

Sessions commonly rely on cookies.

```
Browser

↓

Session Cookie

↓

Application

↓

Authenticated Session
```

Session cookies should be configured according to current security best practices.

---

# Account Recovery

Users occasionally forget credentials.

Recovery should verify identity before allowing credential changes.

```
Recovery Request

↓

Identity Verification

↓

Credential Reset

↓

New Authentication
```

Recovery processes should provide assurance comparable to normal authentication.

---

# Enterprise Identity Protection

Modern identity protection includes multiple controls.

```
Identity Protection

│

├── MFA

├── Password Policies

├── Session Management

├── Device Verification

├── Logging

├── Monitoring

└── Risk Evaluation
```

These controls work together to reduce account compromise risk.

---

# Authentication Monitoring

Organizations monitor authentication events.

```
Authentication Events

↓

Central Logging

↓

Monitoring

↓

Alerting

↓

Investigation
```

Monitoring supports security operations and incident response.

---

# Enterprise Example

A multinational organization:

```
Employee

↓

Identity Provider

↓

Password

↓

Authenticator App

↓

Corporate Applications

↓

Audit Logs

↓

Security Operations Center
```

Authentication events are centrally managed and continuously monitored.

---

# Common Authentication Weaknesses

| Weakness | Potential Impact |
|----------|------------------|
| Weak passwords | Easier account compromise |
| Password reuse | Multiple accounts affected by one credential disclosure |
| Missing MFA | Reduced authentication assurance |
| Long-lived sessions | Increased exposure if a session is left unattended |
| Weak recovery process | Unauthorized account recovery |
| Inadequate monitoring | Delayed detection of suspicious authentication activity |

---

# Enterprise Authentication Workflow

```
User

↓

Identity Verification

↓

Password Verification

↓

MFA

↓

Session Creation

↓

Authorization

↓

Application Access

↓

Logging

↓

Monitoring
```

---

# Hands-on Lab (Conceptual)

1. Draw the authentication flow of an enterprise web application.
2. Identify authentication factors used by the application.
3. Review the session lifecycle.
4. Design a password policy suitable for an enterprise environment.
5. Document where authentication events should be logged and monitored.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What makes a password strong?
2. Why should passwords never be stored in plaintext?
3. What is one-way password hashing?
4. What are the different authentication factors?
5. What is Multi-Factor Authentication?
6. What are passkeys?
7. Why are session timeouts important?
8. What events should invalidate a session?
9. Why must account recovery be secured?
10. Why should authentication events be monitored?

---

# Best Practices

- Encourage long, unique passwords or passphrases.
- Store passwords using modern password hashing algorithms with unique salts.
- Enable MFA for sensitive applications.
- Consider passwordless authentication where appropriate.
- Apply secure session management throughout the authentication lifecycle.
- Secure account recovery with strong identity verification.
- Continuously monitor authentication activity.

---

# Common Mistakes

- Storing passwords in plaintext or using reversible encryption.
- Allowing password reuse across multiple accounts.
- Treating MFA as optional for high-risk systems.
- Keeping sessions active longer than necessary.
- Implementing weak account recovery processes.
- Failing to monitor authentication events.

---

# Key Takeaways

- Password security involves secure creation, storage, verification, recovery, and retirement.
- Modern password hashing and unique salts help protect stored credentials.
- MFA significantly strengthens identity assurance by combining independent authentication factors.
- Passwordless authentication and passkeys represent modern alternatives to traditional passwords.
- Session management, secure recovery, and continuous monitoring are essential components of enterprise authentication.

# 25-Identification-and-Authentication-Failures.md

# Part 3 — Authentication Protocols, Federation, Single Sign-On (SSO), OAuth 2.0, OpenID Connect (OIDC), SAML, and Enterprise Identity Architecture

> **"Modern enterprise authentication extends beyond usernames and passwords. Organizations increasingly rely on centralized identity, federation, and standardized authentication protocols to securely connect users, applications, and cloud services."**

---

# Learning Objectives

After completing this part, you will understand:

- Identity Federation
- Single Sign-On (SSO)
- Identity Providers (IdP)
- Service Providers (SP)
- OAuth 2.0
- OpenID Connect (OIDC)
- SAML
- Authentication Tokens
- Enterprise Identity Architecture
- Authentication Monitoring

---

# Evolution of Authentication

Authentication has evolved significantly.

```
Username + Password

↓

Multi-Factor Authentication

↓

Single Sign-On

↓

Federated Identity

↓

Passwordless Authentication

↓

Continuous Authentication
```

Modern authentication focuses on both security and usability.

---

# Enterprise Authentication Architecture

```
                User

                  │

                  ▼

          Identity Provider

      ┌───────────┼───────────┐

      ▼           ▼           ▼

 HR Portal   Finance App   CRM System

      │           │           │

      └───────────┼───────────┘

                  ▼

           Enterprise Services
```

Centralized identity reduces administrative complexity.

---

# Identity Federation

Identity federation allows one trusted identity system to authenticate users for multiple independent applications.

```
User

↓

Identity Provider

↓

Authentication

↓

Trusted Applications
```

Applications rely on the identity provider instead of maintaining separate authentication systems.

---

# Benefits of Federation

```
Federation

│

├── Centralized Identity

├── Consistent Authentication

├── Simplified User Experience

├── Reduced Password Fatigue

├── Easier Account Management

└── Improved Security Monitoring
```

---

# Single Sign-On (SSO)

Single Sign-On allows users to authenticate once and access multiple applications without repeatedly entering credentials.

```
User

↓

Login Once

↓

Identity Provider

↓

Application A

Application B

Application C
```

SSO improves usability while simplifying centralized identity management.

---

# SSO Workflow

```
User

↓

Authenticate

↓

Identity Provider

↓

Authentication Assertion

↓

Application Access
```

Applications trust the authentication performed by the identity provider.

---

# Identity Provider (IdP)

An Identity Provider is responsible for authenticating users.

Responsibilities include:

```
Identity Provider

│

├── User Authentication

├── MFA

├── Credential Management

├── Identity Verification

├── Session Management

└── Token Issuance
```

---

# Service Provider (SP)

A Service Provider relies on an Identity Provider to authenticate users.

```
Service Provider

↓

Receive Identity Information

↓

Validate Trust

↓

Authorize User

↓

Provide Services
```

Authentication and authorization remain separate responsibilities.

---

# Authentication Tokens

After successful authentication, identity information is commonly represented using tokens.

```
Authenticate

↓

Identity Verified

↓

Token Issued

↓

Application Access
```

Tokens reduce the need to repeatedly submit credentials during authenticated sessions.

---

# OAuth 2.0 Overview

OAuth 2.0 is an **authorization framework**.

It allows applications to obtain limited access to protected resources on behalf of a user without requiring the user's password to be shared with every application.

```
User

↓

Application

↓

Authorization

↓

Access Granted

↓

Protected Resource
```

> **Important:** OAuth 2.0 primarily addresses **authorization**, not user authentication.

---

# OAuth 2.0 Components

```
OAuth 2.0

│

├── Resource Owner

├── Client

├── Authorization Server

├── Resource Server

└── Access Token
```

Each component has a defined responsibility within the authorization process.

---

# OpenID Connect (OIDC)

OpenID Connect builds on OAuth 2.0 to provide **authentication**.

```
User

↓

Identity Provider

↓

Authentication

↓

Identity Token

↓

Application
```

OIDC allows applications to verify the authenticated identity of users using standardized protocols.

---

# OAuth 2.0 vs OpenID Connect

| OAuth 2.0 | OpenID Connect |
|-----------|----------------|
| Authorization framework | Authentication layer built on OAuth 2.0 |
| Controls access to resources | Verifies user identity |
| Uses access tokens | Uses identity information in addition to OAuth tokens |
| Focuses on permissions | Focuses on authentication |

---

# Security Assertion Markup Language (SAML)

SAML is an XML-based standard widely used for enterprise Single Sign-On.

```
User

↓

Identity Provider

↓

SAML Assertion

↓

Enterprise Application
```

Many enterprise environments use SAML for web-based authentication.

---

# SAML Components

```
SAML

│

├── Identity Provider

├── Service Provider

├── Authentication Assertion

├── Attribute Assertion

└── Trust Relationship
```

---

# Federation Trust

Applications trust authenticated identities through established trust relationships.

```
Identity Provider

↓

Trusted Assertion

↓

Application

↓

User Access
```

Trust relationships must be carefully managed and periodically reviewed.

---

# Authentication Flow Comparison

```
Traditional Login

↓

Application

↓

Local Authentication

────────────────────

Federated Login

↓

Identity Provider

↓

Trusted Authentication

↓

Application
```

Federated identity centralizes authentication while allowing applications to focus on authorization.

---

# Continuous Authentication

Modern systems increasingly evaluate authentication continuously.

```
Login

↓

Authenticated Session

↓

Risk Evaluation

↓

Additional Verification (if required)

↓

Continued Access
```

Continuous evaluation strengthens long-lived sessions.

---

# Enterprise Identity Architecture

```
                  Employees

                      │

                      ▼

             Identity Provider

          ┌───────────┼───────────┐

          ▼           ▼           ▼

      Web Apps    Cloud Apps    Mobile Apps

          │           │           │

          └───────────┼───────────┘

                      ▼

            Central Audit Logging

                      ▼

          Security Operations Center
```

Identity services provide centralized authentication while applications enforce authorization.

---

# Authentication Logging

Authentication systems should generate security-relevant events.

```
Authentication

↓

Audit Log

↓

Central Logging

↓

Monitoring

↓

Alerting
```

Logs support compliance, investigations, and operational monitoring.

---

# Authentication Events

Examples include:

```
Authentication Events

│

├── Login Success

├── Login Failure

├── MFA Completion

├── Password Change

├── Account Recovery

├── Logout

├── Session Timeout

└── Administrative Changes
```

Sensitive information should never be recorded in logs.

---

# Enterprise Example

A multinational organization:

```
Employee

↓

Identity Provider

↓

MFA

↓

SSO

↓

ERP

↓

CRM

↓

HR Portal

↓

Audit Logs
```

Authentication is centralized while each application independently evaluates authorization.

---

# Common Authentication Architecture Weaknesses

| Weakness | Potential Impact |
|----------|------------------|
| Separate authentication systems | Inconsistent identity management |
| Weak trust relationships | Increased authentication risk |
| Poor logging | Delayed detection of suspicious activity |
| Weak session controls | Increased exposure after login |
| Missing MFA | Lower identity assurance |
| Poor governance | Inconsistent authentication policies |

---

# Enterprise Identity Workflow

```
User

↓

Identity Verification

↓

Authentication

↓

MFA

↓

Identity Provider

↓

SSO

↓

Application

↓

Authorization

↓

Audit Logging
```

---

# Hands-on Lab (Conceptual)

1. Draw an enterprise authentication architecture.
2. Identify the Identity Provider and Service Providers.
3. Document where SSO is used.
4. Compare traditional authentication with federated authentication.
5. Identify authentication events that should be logged.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is identity federation?
2. What is Single Sign-On (SSO)?
3. What is an Identity Provider (IdP)?
4. What is a Service Provider (SP)?
5. What is OAuth 2.0?
6. How does OpenID Connect differ from OAuth 2.0?
7. What is SAML?
8. Why do enterprises centralize authentication?
9. Why should authentication events be logged?
10. What is continuous authentication?

---

# Best Practices

- Centralize authentication using trusted identity providers.
- Separate authentication from authorization responsibilities.
- Enable MFA for federated authentication systems.
- Establish and regularly review trust relationships.
- Monitor authentication events continuously.
- Use standardized authentication protocols appropriate for the environment.
- Periodically review identity architecture and access policies.

---

# Common Mistakes

- Confusing OAuth 2.0 with authentication.
- Assuming SSO eliminates the need for authorization checks.
- Maintaining inconsistent authentication mechanisms across applications.
- Failing to review federation trust relationships.
- Neglecting centralized authentication logging.
- Treating authentication as a one-time event rather than an ongoing process.

---

# Key Takeaways

- Identity federation enables centralized authentication across multiple applications.
- Single Sign-On improves usability while simplifying enterprise identity management.
- OAuth 2.0 is an authorization framework, while OpenID Connect adds standardized authentication.
- SAML remains a widely adopted enterprise authentication protocol.
- Enterprise authentication architectures rely on trusted identity providers, centralized monitoring, and continuous evaluation of authentication events.

```text id="rrks28"
**Next:** Part 4
```