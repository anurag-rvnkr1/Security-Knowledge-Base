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

```text id="rrks28"
**Next:** Part 2
```