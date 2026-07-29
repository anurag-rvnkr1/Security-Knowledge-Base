# 12 - OAuth 2.0

# Introduction

OAuth 2.0 is an authorization framework that enables applications to obtain limited access to protected resources on behalf of a user **without exposing the user's credentials**.

Instead of sharing usernames and passwords with third-party applications, users authorize applications by granting limited permissions.

OAuth 2.0 is widely used by:

- REST APIs
- Mobile Applications
- Single Page Applications (SPAs)
- Cloud Platforms
- SaaS Applications
- Social Login Providers
- Enterprise Identity Platforms
- Microservices

OAuth is **not an authentication protocol**.

Its primary purpose is **delegated authorization**.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand OAuth 2.0 fundamentals.
- Learn OAuth terminology.
- Understand OAuth roles.
- Explore OAuth authorization flows.
- Understand grant types.
- Learn access tokens and scopes.
- Understand refresh tokens.
- Identify OAuth security threats.
- Learn enterprise OAuth deployments.

---

# Why OAuth?

Without OAuth,

users often share their credentials directly with applications.

```
User

 │

Username & Password

 │

Third-Party Application

 │

Access User Account
```

This creates several risks.

- Password theft
- Password reuse
- Excessive privileges
- Difficult credential revocation

OAuth eliminates the need to expose user passwords.

---

# OAuth Solution

OAuth separates authentication from authorization.

```
User

        │

        ▼

Identity Provider

        │

Authorization

        ▼

Access Token

        │

        ▼

Application

        │

Protected Resource
```

The application never receives the user's password.

---

# OAuth vs Authentication

OAuth provides authorization.

Authentication verifies identity.

```
Authentication

↓

Who are you?

------------------------

Authorization

↓

What may you access?
```

OAuth is commonly combined with OpenID Connect (OIDC) for authentication.

---

# OAuth Roles

OAuth defines four primary roles.

```
OAuth

 │

 ├─────────────┬──────────────┬──────────────┬─────────────┐

 ▼             ▼              ▼             ▼

Resource    Client      Authorization   Resource
Owner                    Server         Server
```

Each role has a specific responsibility.

---

# Resource Owner

The Resource Owner is the entity that owns the protected data.

Examples

- Customer
- Employee
- Administrator

Example

```
Alice

↓

Owns Photos

↓

Authorizes Access
```

The Resource Owner decides whether access should be granted.

---

# Client

The Client is the application requesting access.

Examples

- Mobile App
- Web Application
- Desktop Application
- API Gateway
- Backend Service

Example

```
Expense App

↓

Requests Access

↓

Accounting API
```

Clients should request only the permissions they require.

---

# Authorization Server

The Authorization Server authenticates users and issues OAuth tokens.

Responsibilities

- User authentication
- User consent
- Token generation
- Token validation
- Refresh token processing
- Client authentication

Examples

- Microsoft Entra ID
- Keycloak
- Okta
- Auth0
- Ping Identity

---

# Resource Server

The Resource Server hosts protected APIs.

Responsibilities

- Validate access tokens
- Verify scopes
- Enforce authorization
- Return protected resources

Examples

- Payment API
- Inventory API
- Customer API
- Banking API

---

# OAuth Architecture

```
                 Resource Owner

                        │

                        ▼

                 Client Application

                        │

                        ▼

              Authorization Server

                        │

               Access Token Issued

                        ▼

                 Resource Server

                        │

                        ▼

                 Protected Resource
```

---

# OAuth Terminology

Common OAuth terms

| Term | Description |
|------|-------------|
| Access Token | Credential used to access resources |
| Refresh Token | Used to obtain new access tokens |
| Scope | Permissions granted |
| Grant Type | Authorization workflow |
| Redirect URI | Client callback endpoint |
| Consent | User approval |
| Authorization Code | Temporary code exchanged for tokens |

---

# OAuth Authorization Flow

High-level workflow

```
User

 │

Login

 │

Consent

 │

Authorization Code

 │

Access Token

 │

Protected API
```

The exact flow depends on the selected grant type.

---

# OAuth Tokens

OAuth commonly uses

```
Access Token

↓

API Access
```

```
Refresh Token

↓

New Access Token
```

Some deployments also issue

```
ID Token

↓

Authentication

(OpenID Connect)
```

---

# OAuth Scopes

Scopes define what the client may access.

Example

```
read:users

write:users

delete:users
```

Another example

```
profile

email

calendar

contacts
```

Scopes should follow the principle of least privilege.

---

# Scope Example

User grants

```
Read Calendar
```

instead of

```
Full Account Access
```

OAuth allows granular permission delegation.

---

# Consent Screen

Users review requested permissions before granting access.

```
Application Requests

↓

Read Profile

Read Contacts

Read Calendar

↓

Approve?

Yes / No
```

Clear consent improves transparency and security.

---

# OAuth Endpoint Overview

Typical endpoints

```
/authorize

/token

/revoke

/introspect

/userinfo (OIDC)
```

Each endpoint serves a distinct purpose.

---

# Authorization Endpoint

The authorization endpoint

- Authenticates users
- Requests consent
- Returns authorization codes

```
Client

 │

/authorize

 ▼

Authorization Server
```

---

# Token Endpoint

The token endpoint exchanges credentials for tokens.

```
Authorization Code

↓

/token

↓

Access Token
```

Only trusted clients should access this endpoint.

---

# Token Introspection Endpoint

Some deployments validate opaque tokens through introspection.

```
Resource Server

        │

Introspection Request

        ▼

Authorization Server

        │

Token Status

        ▼

Resource Server
```

Useful for centralized token validation.

---

# Token Revocation Endpoint

Revocation invalidates issued tokens.

```
Client

 │

Revoke Token

 │

Authorization Server

 │

Token Invalid
```

Used during logout or compromise.

---

# Redirect URI

After authorization,

the user is redirected back to the client.

```
User

 │

Authorization Complete

 │

Redirect URI

 ▼

Client
```

Redirect URIs must be registered and validated.

---

# Redirect URI Validation

```
Incoming Redirect

        │

Matches Registered URI?

   ┌────┴─────┐

   ▼          ▼

Yes          No

   │          │

Allow      Reject
```

Never allow arbitrary redirect destinations.

---

# OAuth Client Types

OAuth defines different client categories.

```
Clients

   │

 ┌─┼─────────────┐

 ▼ ▼             ▼

Public       Confidential
```

---

# Public Clients

Public clients cannot securely protect secrets.

Examples

- Mobile Apps
- JavaScript SPAs
- Desktop Applications

Characteristics

- No secure secret storage
- Use PKCE
- Limited trust

---

# Confidential Clients

Confidential clients securely store credentials.

Examples

- Backend Servers
- Enterprise Applications
- API Gateways

Characteristics

- Client secret
- Server-side execution
- Stronger identity assurance

---

# Client Authentication

Confidential clients authenticate themselves to the authorization server.

Methods

- Client Secret
- Mutual TLS
- JWT Client Assertion
- Private Key JWT

Proper client authentication prevents unauthorized token issuance.

---

# OAuth Client Registration

Typical registration information

- Client ID
- Redirect URI
- Grant Types
- Allowed Scopes
- Client Authentication Method

Each client receives a unique identifier.

---

# Client Credentials

```
Client ID

+

Client Secret
```

These credentials identify the client,

not the user.

Client secrets should never be embedded in public applications.

---

# Enterprise OAuth Architecture

```
                 User

                   │

                   ▼

          Client Application

                   │

                   ▼

         Authorization Server

                   │

         Access Token Issued

                   ▼

             API Gateway

                   │

                   ▼

            Protected APIs

                   │

                   ▼

           Enterprise Services
```

---

# Best Practices

Authorization

- Request minimum scopes.
- Validate redirect URIs.
- Use HTTPS.
- Use short-lived access tokens.
- Rotate refresh tokens.

Development

- Protect client secrets.
- Register redirect URIs.
- Validate state parameters.
- Validate tokens.
- Log authorization events.

Operations

- Monitor token issuance.
- Detect abnormal consent activity.
- Review registered clients.
- Audit privileged scopes.

---

# Common Mistakes

Avoid

- Requesting excessive scopes
- Wildcard redirect URIs
- Exposing client secrets
- Missing token validation
- Ignoring consent
- Long-lived access tokens
- Reusing refresh tokens indefinitely
- Missing audit logs
- Accepting unregistered clients

---

# Key Takeaways

- OAuth 2.0 is a delegated authorization framework.
- OAuth eliminates password sharing with third-party applications.
- OAuth defines four primary roles.
- Scopes provide granular permissions.
- Redirect URI validation is essential.
- Confidential and public clients have different security requirements.

---

**Next:** OAuth 2.0 Grant Types, Authorization Code Flow, PKCE, Device Authorization Flow, Client Credentials Flow, Refresh Tokens, OAuth Security Threats, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.