# 33-OAuth-and-OIDC.md

# Part 1 — Introduction to OAuth 2.0, OpenID Connect (OIDC), Authentication vs Authorization, and Enterprise Identity

> **"OAuth 2.0 answers the question 'What is this application allowed to do?', while OpenID Connect answers 'Who is the user?'"**

---

# Learning Objectives

After completing this part, you will understand:

- Identity and Access Management (IAM)
- Authentication vs Authorization
- OAuth 2.0 Fundamentals
- OpenID Connect (OIDC)
- Why OAuth Exists
- OAuth Roles
- OAuth Tokens
- OAuth Architecture
- Enterprise Identity Providers
- Real-World OAuth Workflows

---

# Identity and Access Management (IAM)

Identity and Access Management (IAM) is the collection of policies, technologies, and processes used to manage digital identities and control access to resources.

```
Identity

↓

Authentication

↓

Authorization

↓

Resource Access

↓

Audit & Monitoring
```

IAM forms the foundation of modern enterprise security.

---

# Why Identity Matters

Modern organizations manage access for:

```
Users

│

├── Employees

├── Customers

├── Partners

├── Vendors

├── Mobile Apps

├── Web Applications

└── APIs
```

Each identity requires controlled access based on organizational policies.

---

# Authentication vs Authorization

These terms are often confused but represent different security functions.

| Authentication | Authorization |
|----------------|---------------|
| Verifies identity | Determines permissions |
| "Who are you?" | "What can you access?" |
| Occurs first | Happens after authentication |
| Identity-focused | Permission-focused |

---

# Simple Example

```
User

↓

Login

↓

Authentication

↓

Verified Identity

↓

Authorization

↓

Access Granted
```

A user must first prove their identity before permissions can be evaluated.

---

# What is OAuth 2.0?

OAuth 2.0 is an authorization framework that allows an application to obtain limited access to another application's protected resources **without sharing the user's password**.

OAuth is designed for **delegated authorization**.

---

# Why OAuth Was Created

Before OAuth:

```
User

↓

Shares Password

↓

Third-Party Application

↓

Full Account Access
```

Problems included:

- Password sharing
- Excessive privileges
- Difficult revocation
- Increased security risk

OAuth solved these issues by introducing delegated access using tokens.

---

# OAuth Concept

```
User

↓

Approves Access

↓

Authorization Server

↓

Access Token

↓

Application

↓

Protected Resource
```

The application receives a token—not the user's password.

---

# What OAuth Does

OAuth enables an application to:

- Request permission
- Receive delegated authorization
- Access approved resources
- Operate with limited privileges
- Revoke access independently of user credentials

---

# What OAuth Does NOT Do

OAuth **does not** identify the user by itself.

OAuth primarily answers:

```
Can this application access this resource?
```

It does **not** inherently answer:

```
Who is the user?
```

That is where OpenID Connect becomes important.

---

# What is OpenID Connect (OIDC)?

OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0.

It allows applications to authenticate users while continuing to use OAuth for delegated authorization.

---

# OAuth vs OIDC

| OAuth 2.0 | OpenID Connect |
|------------|----------------|
| Authorization | Authentication + Identity |
| Access Tokens | ID Token + Access Token |
| Resource Access | User Identity |
| Delegated Permissions | User Login |

---

# Why OIDC Was Introduced

Applications often need to know:

- Who logged in?
- What is the user's identity?
- Which identity provider authenticated them?

OAuth alone does not standardize identity information.

OIDC adds that capability.

---

# Enterprise Login Example

```
User

↓

Enterprise Login

↓

Identity Provider

↓

Authentication

↓

ID Token

↓

Application
```

The application can verify the authenticated user's identity using the ID Token.

---

# Common Enterprise Identity Providers

```
Identity Providers

│

├── Microsoft Entra ID

├── Okta

├── Auth0

├── Google Identity

├── Keycloak

├── Ping Identity

├── ForgeRock

└── OneLogin
```

Organizations commonly integrate these platforms with OAuth and OIDC.

---

# OAuth Roles

OAuth defines four primary roles.

```
OAuth Roles

│

├── Resource Owner

├── Client

├── Authorization Server

└── Resource Server
```

These roles cooperate to securely provide delegated access.

---

# Resource Owner

The Resource Owner is typically the user who owns protected resources.

```
User

↓

Owns Data

↓

Grants Permission
```

---

# Client

The Client is the application requesting access on behalf of the user.

Examples include:

- Mobile applications
- Web applications
- Desktop applications
- Backend services

---

# Authorization Server

The Authorization Server:

- Authenticates users
- Obtains consent
- Issues tokens
- Validates client requests

```
User

↓

Authentication

↓

Consent

↓

Token Issuance
```

---

# Resource Server

The Resource Server hosts protected APIs or data.

```
Application

↓

Access Token

↓

Resource Server

↓

Protected Data
```

The server validates the token before serving protected resources.

---

# OAuth Components

```
OAuth

│

├── Authorization Endpoint

├── Token Endpoint

├── Client

├── Resource Server

├── Authorization Server

├── Access Token

└── Scopes
```

---

# High-Level OAuth Flow

```
User

↓

Client Application

↓

Authorization Server

↓

User Consent

↓

Access Token

↓

Resource Server

↓

Protected Resource
```

This flow separates authentication, authorization, and resource access.

---

# OAuth in Enterprise Architecture

```
Internet

↓

Load Balancer

↓

Application

↓

Identity Provider

↓

Authorization Server

↓

Resource Server

↓

Database
```

Identity services are often centralized across the enterprise.

---

# Real-World Example

A project management application wants to access a user's cloud storage files.

```
User

↓

Approves Request

↓

Identity Platform

↓

Access Token

↓

Cloud Storage API

↓

Authorized Files
```

The application receives only the permissions approved by the user.

---

# Benefits of OAuth

```
OAuth Benefits

│

├── No Password Sharing

├── Delegated Access

├── Least Privilege

├── Revocable Access

├── Better User Experience

├── Enterprise Integration

└── Improved Security
```

---

# Hands-on Lab (Conceptual)

1. Draw the OAuth architecture showing all four roles.
2. Compare Authentication and Authorization.
3. Identify where OAuth and OIDC fit within an enterprise login process.
4. Design a conceptual identity architecture using an Identity Provider and Resource Server.
5. Explain why token-based delegated authorization is preferable to password sharing.

> Perform all activities only in environments where you have explicit authorization. Focus on understanding architecture and identity concepts rather than implementation.

---

# Interview Questions

1. What is OAuth 2.0?
2. Why was OAuth created?
3. What problem does OAuth solve?
4. What is OpenID Connect?
5. How does OAuth differ from OIDC?
6. What are the four OAuth roles?
7. What is a Resource Server?
8. What is an Authorization Server?
9. Why should applications avoid password sharing?
10. Why is delegated authorization important?

---

# Best Practices

- Use OAuth 2.0 for delegated authorization.
- Use OpenID Connect when user authentication and identity are required.
- Centralize identity management using trusted Identity Providers.
- Apply the principle of least privilege.
- Separate authentication from authorization responsibilities.
- Regularly review delegated permissions.

---

# Common Mistakes

- Assuming OAuth performs authentication by itself.
- Confusing Access Tokens with user identity.
- Granting broader permissions than required.
- Sharing user passwords with third-party applications.
- Treating authentication and authorization as the same process.

---

# Key Takeaways

- OAuth 2.0 is an authorization framework for delegated access.
- OpenID Connect extends OAuth by providing standardized user authentication and identity.
- OAuth eliminates the need for password sharing between applications.
- The four OAuth roles form the foundation of secure delegated authorization.
- Modern enterprise identity platforms commonly use OAuth 2.0 and OIDC together.

# 33-OAuth-and-OIDC.md

# Part 2 — OAuth 2.0 Tokens, Authorization Flows, Scopes, Claims, JWT, ID Tokens, Refresh Tokens, and Secure Token Management

> **"OAuth security revolves around one principle: applications receive limited, temporary, and revocable access through tokens instead of permanent credentials."**

---

# Learning Objectives

After completing this part, you will understand:

- OAuth Tokens
- Access Tokens
- Refresh Tokens
- ID Tokens
- JWT Fundamentals
- OAuth Scopes
- Claims
- OAuth Authorization Flows
- PKCE
- Secure Token Management

---

# OAuth Tokens

A token is a credential issued by the Authorization Server after successful authorization.

```
User

↓

Authorization

↓

Authorization Server

↓

Token

↓

Client
```

Tokens allow applications to access approved resources without storing the user's password.

---

# Why Tokens?

Instead of sharing credentials:

```
User

↓

Password

↓

Application
```

OAuth uses:

```
User

↓

Authorization

↓

Access Token

↓

Application
```

This significantly reduces credential exposure.

---

# Types of OAuth Tokens

```
OAuth Tokens

│

├── Access Token

├── Refresh Token

└── ID Token (OIDC)
```

Each token serves a different purpose.

---

# Access Token

An Access Token authorizes a client to access protected resources.

```
Client

↓

Access Token

↓

Resource Server

↓

Protected API
```

The Resource Server validates the token before serving data.

---

# Access Token Characteristics

```
Access Token

│

├── Short-Lived

├── Limited Permissions

├── Revocable

├── Scope Restricted

└── Used for APIs
```

Short lifetimes reduce the impact of token compromise.

---

# Refresh Token

Refresh Tokens allow a client to obtain new Access Tokens without requiring the user to authenticate again.

```
Client

↓

Refresh Token

↓

Authorization Server

↓

New Access Token
```

Refresh Tokens are generally longer-lived and require stronger protection.

---

# Refresh Token Lifecycle

```
Login

↓

Access Token

↓

Expires

↓

Refresh Token

↓

New Access Token
```

Users experience seamless sessions while maintaining security controls.

---

# ID Token (OIDC)

OpenID Connect introduces the **ID Token**.

Its purpose is to provide information about the authenticated user.

```
User Login

↓

Identity Provider

↓

ID Token

↓

Client
```

Applications use the ID Token to identify the authenticated user.

---

# ID Token vs Access Token

| ID Token | Access Token |
|-----------|--------------|
| Identity Information | API Authorization |
| Used by Client | Used by Resource Server |
| OIDC | OAuth 2.0 |
| Contains User Claims | Contains Authorization Information |

---

# OAuth Scopes

Scopes define what a client is permitted to access.

```
Client

↓

Requested Scope

↓

Authorization Server

↓

Approved Scope

↓

Token
```

Scopes implement the principle of least privilege.

---

# Example Scope Concept

```
Application

↓

Read Profile

↓

Read Calendar

↓

Read Email

↓

Approved Permissions
```

Applications should request only the permissions necessary for their functionality.

---

# Least Privilege

```
Application

↓

Minimum Required Permissions

↓

Access Granted
```

Least privilege limits potential impact if a token is misused.

---

# OAuth Claims

Claims are pieces of information contained within a token.

Examples include:

```
Claims

│

├── Subject

├── Issuer

├── Audience

├── Expiration

├── Issued Time

├── Scope

└── Client Identifier
```

Claims help applications validate and interpret tokens.

---

# JSON Web Token (JWT)

Many OAuth and OIDC implementations use JSON Web Tokens (JWTs).

A JWT is a compact, structured format for securely conveying claims.

---

# JWT Structure

```
JWT

│

├── Header

├── Payload

└── Signature
```

```
Header.Payload.Signature
```

Each section serves a different purpose.

---

# JWT Header

The Header typically contains metadata.

```
Header

↓

Algorithm

↓

Token Type
```

It describes how the token is protected.

---

# JWT Payload

The Payload contains claims.

```
Payload

↓

User Information

↓

Scopes

↓

Expiration

↓

Issuer
```

Applications should avoid placing unnecessary sensitive information inside token payloads.

---

# JWT Signature

The Signature helps verify integrity.

```
Header

+

Payload

↓

Signature

↓

Validation
```

If the signature validation fails, the token should be rejected.

---

# Token Validation

Before accepting a token, applications typically validate:

```
Validation

│

├── Signature

├── Issuer

├── Audience

├── Expiration

├── Not Before

├── Scope

└── Token Status
```

Only successfully validated tokens should be trusted.

---

# Token Lifetime

```
Access Token

↓

Short Lifetime

↓

Expiration
```

```
Refresh Token

↓

Longer Lifetime

↓

Rotation / Expiration
```

Organizations commonly use shorter Access Token lifetimes to reduce risk.

---

# Token Rotation

Refresh Token rotation is commonly used to improve session security.

```
Refresh Token

↓

Authorization Server

↓

New Refresh Token

↓

Invalidate Previous Token
```

Rotation reduces the usefulness of previously issued Refresh Tokens.

---

# Token Revocation

Organizations may revoke tokens before their natural expiration.

```
Security Event

↓

Token Revocation

↓

Resource Server

↓

Access Denied
```

Revocation supports rapid response to account compromise or policy changes.

---

# OAuth Authorization Flows

OAuth defines several authorization flows for different client types.

```
Authorization Flows

│

├── Authorization Code

├── Authorization Code + PKCE

├── Client Credentials

├── Device Authorization

└── Refresh Token Flow
```

Different scenarios require different flows.

---

# Authorization Code Flow

The Authorization Code Flow is widely used for confidential clients such as traditional web applications.

```
User

↓

Client

↓

Authorization Server

↓

Authorization Code

↓

Access Token

↓

Protected API
```

The Authorization Code is exchanged securely for tokens.

---

# PKCE (Proof Key for Code Exchange)

PKCE strengthens the Authorization Code Flow, especially for public clients such as mobile and desktop applications.

```
Client

↓

PKCE Challenge

↓

Authorization Server

↓

Authorization Code

↓

PKCE Verification

↓

Access Token
```

PKCE reduces the risk of authorization code interception.

---

# Client Credentials Flow

This flow is intended for service-to-service communication.

```
Service

↓

Authorization Server

↓

Access Token

↓

Resource Server
```

No end user participates in this authorization flow.

---

# Device Authorization Flow

Designed for devices with limited input capabilities.

Examples include:

- Smart TVs
- Streaming devices
- Gaming consoles
- IoT devices

```
Device

↓

User Verification

↓

Authorization Server

↓

Access Token
```

---

# OAuth Flow Selection

| Scenario | Recommended Flow |
|-----------|------------------|
| Traditional Web Application | Authorization Code |
| Mobile Application | Authorization Code + PKCE |
| Desktop Application | Authorization Code + PKCE |
| Machine-to-Machine | Client Credentials |
| Smart TV / IoT Device | Device Authorization |

---

# Secure Token Storage

Applications should protect issued tokens appropriately.

```
Application

↓

Secure Storage

↓

Protected Token
```

Storage mechanisms depend on application architecture and platform capabilities.

---

# Token Security Principles

```
Token Security

│

├── Short Lifetimes

├── Least Privilege

├── Rotation

├── Revocation

├── Validation

├── Secure Storage

└── TLS Protection
```

These controls reduce the likelihood and impact of token misuse.

---

# Enterprise OAuth Architecture

```
Client

↓

Identity Provider

↓

Authorization Server

↓

Access Token

↓

API Gateway

↓

Resource Server

↓

Business Services
```

Identity and authorization are centralized while business services enforce token validation.

---

# Enterprise Example

A multinational enterprise provides employees with access to internal HR, payroll, and collaboration systems.

```
Employee

↓

Corporate Portal

↓

Identity Provider

↓

Authorization Server

↓

Access Token

↓

Internal APIs

↓

Business Applications
```

Each application validates tokens before providing access to protected resources.

---

# Common Enterprise Challenges

| Challenge | Recommended Approach |
|-----------|----------------------|
| Long-lived tokens | Short Access Token lifetime |
| Token compromise | Token revocation and rotation |
| Excessive permissions | Least privilege scopes |
| Weak client protection | Use PKCE where appropriate |
| Multiple APIs | Centralized token validation |
| Identity sprawl | Enterprise Identity Provider |

---

# Hands-on Lab (Conceptual)

1. Draw the lifecycle of an Access Token.
2. Compare Access Tokens, Refresh Tokens, and ID Tokens.
3. Design a secure token validation workflow.
4. Select the appropriate OAuth flow for five different application types.
5. Identify which claims should be validated before accepting a token.

> Perform all activities only in environments where you have explicit authorization. Focus on understanding token management, architecture, and secure identity design.

---

# Interview Questions

1. What is an Access Token?
2. What is the purpose of a Refresh Token?
3. What is an ID Token?
4. What is the difference between OAuth and OIDC tokens?
5. What are OAuth scopes?
6. What is a JWT?
7. Why should Access Tokens have short lifetimes?
8. What problem does PKCE solve?
9. Which OAuth flow is recommended for mobile applications?
10. Why is token validation important?

---

# Best Practices

- Use short-lived Access Tokens.
- Protect Refresh Tokens with stronger security controls.
- Validate token signatures, issuer, audience, expiration, and scopes.
- Use Authorization Code with PKCE for public clients.
- Request only the minimum scopes required.
- Rotate and revoke tokens when appropriate.
- Protect tokens in storage and during transmission with TLS.

---

# Common Mistakes

- Confusing ID Tokens with Access Tokens.
- Storing tokens insecurely.
- Granting excessive scopes.
- Accepting expired or improperly validated tokens.
- Using deprecated OAuth flows for modern applications.
- Treating Refresh Tokens with the same protection as Access Tokens.

---

# Key Takeaways

- OAuth uses tokens instead of passwords to enable delegated authorization.
- Access Tokens authorize API access, Refresh Tokens renew sessions, and ID Tokens identify authenticated users.
- JWTs commonly carry claims that applications validate before granting access.
- PKCE significantly strengthens the Authorization Code Flow for public clients.
- Secure token lifecycle management—including validation, rotation, revocation, and least privilege—is fundamental to enterprise OAuth security.

```text id="rrks28"
**Next:** Part 3
```