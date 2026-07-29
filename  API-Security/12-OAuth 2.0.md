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


# OAuth 2.0 Grant Types

Grant types define how a client obtains an access token from the Authorization Server.

```
OAuth 2.0

      │

 ┌────┼─────────┬────────────┬──────────────┐

 ▼    ▼         ▼            ▼

Authorization  Client     Device      Refresh
Code           Credentials Authorization Token

            (+ PKCE)
```

Modern deployments primarily use:

- Authorization Code + PKCE
- Client Credentials
- Device Authorization
- Refresh Token

Some older grant types are now deprecated or discouraged.

---

# OAuth Authorization Code Flow

The Authorization Code Flow is the recommended OAuth flow for:

- Web Applications
- Server-side Applications
- Enterprise Applications

It separates user authentication from token issuance.

---

# Authorization Code Flow Overview

```
+--------+                                +----------------------+
|  User  |                                | Authorization Server |
+--------+                                +----------------------+
     |                                              |
     | Access Client                                |
     ▼                                              |
+------------+                                       |
|   Client   |-------------------------------------->|
+------------+   Authorization Request               |
     |                                              |
     |<----------------------------------------------|
     |        Login & Consent                        |
     |                                              |
     |---------------------------------------------->|
     |      Authorization Code                      |
     |                                              |
     |----------------------/token------------------>|
     |                                              |
     |<----------------------------------------------|
     |   Access Token + Refresh Token               |
     |                                              |
     ▼
Protected Resource
```

---

# Step 1 - Authorization Request

The client redirects the user to the Authorization Server.

Typical parameters include:

- client_id
- redirect_uri
- response_type
- scope
- state

Example

```
GET /authorize

client_id=inventory-app

response_type=code

scope=read:products

state=random-value
```

---

# Step 2 - User Authentication

The Authorization Server authenticates the Resource Owner.

```
User

 │

Username

Password

MFA

 ▼

Authenticated
```

Authentication mechanisms may include:

- Passwords
- Passkeys
- MFA
- Smart Cards
- Enterprise SSO

---

# Step 3 - User Consent

The Authorization Server requests approval.

```
Inventory Application

Requests Permission

-----------------------

Read Products

Read Orders

-----------------------

Approve?

Yes / No
```

Only approved scopes should be granted.

---

# Step 4 - Authorization Code

After successful authentication and consent,

the Authorization Server returns a temporary authorization code.

```
Authorization Server

        │

Authorization Code

        ▼

Client
```

Characteristics

- Short-lived
- Single use
- Not an access token

---

# Step 5 - Token Exchange

The client exchanges the authorization code.

```
Authorization Code

        │

POST /token

        │

Authorization Server

        ▼

Access Token

Refresh Token
```

Only trusted clients should perform this exchange.

---

# Authorization Code Lifetime

Typical characteristics

- Very short lifetime
- One-time use
- Invalid after exchange

If reused,

the Authorization Server should reject the request.

---

# PKCE (Proof Key for Code Exchange)

PKCE protects the Authorization Code Flow against authorization code interception.

Originally designed for public clients,

PKCE is now recommended for virtually all OAuth clients.

---

# Why PKCE?

Without PKCE

```
Attacker

↓

Steals Authorization Code

↓

Exchanges Code

↓

Receives Access Token
```

PKCE prevents unauthorized token exchange.

---

# PKCE Components

PKCE introduces two values.

```
Code Verifier

↓

Random Secret

--------------------

Code Challenge

↓

Hashed Verifier
```

The verifier remains known only to the client.

---

# PKCE Flow

```
Client

 │

Generate Code Verifier

 │

Generate Code Challenge

 │

Authorization Request

 ▼

Authorization Server

 │

Authorization Code

 ▼

Client

 │

Send Authorization Code

+

Code Verifier

 ▼

Authorization Server

 │

Challenge Matches?

 ┌────┴─────┐

 ▼          ▼

Yes        No

 ▼          ▼

Issue      Reject

Token
```

---

# PKCE Benefits

Advantages

- Prevents authorization code interception
- No client secret required
- Ideal for public clients
- Recommended for SPAs
- Recommended for mobile applications

---

# Client Credentials Grant

The Client Credentials Grant is used for machine-to-machine communication.

No user participates.

```
Application

 │

Client ID

Client Secret

 ▼

Authorization Server

 │

Access Token

 ▼

API
```

Typical use cases

- Internal APIs
- Microservices
- Background jobs
- Scheduled tasks

---

# Client Credentials Flow

```
Service A

 │

Authenticate Client

 │

Receive Access Token

 │

Access Service B

 ▼

Protected API
```

No refresh token is typically issued.

---

# Device Authorization Grant

The Device Authorization Grant supports devices with limited input capabilities.

Examples

- Smart TVs
- IoT Devices
- Gaming Consoles
- Embedded Devices

---

# Device Authorization Flow

```
Smart TV

 │

Device Code

 ▼

Authorization Server

 │

Display User Code

 ▼

User

 │

Visit Browser

 │

Authenticate

 ▼

Authorization Server

 │

Approve

 ▼

TV Receives Access Token
```

The user authenticates on a separate trusted device.

---

# Refresh Token Grant

When the access token expires,

the refresh token obtains a replacement.

```
Expired Access Token

        │

Refresh Token

        ▼

Authorization Server

        │

New Access Token

        ▼

Continue Session
```

Refresh tokens should never be sent to Resource Servers.

---

# OAuth Scopes

Scopes limit client permissions.

Examples

```
read:users

write:users

delete:users
```

Cloud examples

```
storage.read

storage.write

billing.read
```

Applications should request only required scopes.

---

# Scope Evaluation

```
Access Token

      │

Contains Scope?

      │

read:orders

      │

API Request

      │

Permission Check

 ┌────┴────┐

 ▼         ▼

Allow    Deny
```

Authorization decisions should include scope validation.

---

# Incremental Authorization

Applications may request additional permissions only when needed.

Example

```
Initial Login

↓

Read Profile

-------------------

Later

↓

Request Calendar Access
```

Benefits

- Better user trust
- Reduced permissions
- Improved security

---

# OAuth Token Types

```
OAuth Tokens

      │

 ┌────┼─────────┐

 ▼    ▼         ▼

Access Refresh ID Token
```

ID Tokens are provided by OpenID Connect rather than OAuth itself.

---

# OAuth Error Responses

Common errors

| Error | Meaning |
|--------|----------|
| invalid_request | Missing or invalid parameters |
| invalid_client | Client authentication failed |
| invalid_grant | Invalid authorization code or refresh token |
| invalid_scope | Requested scope not allowed |
| unauthorized_client | Client not permitted for grant type |
| access_denied | User denied authorization |
| unsupported_grant_type | Unsupported OAuth flow |

Applications should handle errors securely without exposing sensitive information.

---

# OAuth Flow Comparison

| Flow | User Present | Typical Use Case |
|------|--------------|------------------|
| Authorization Code + PKCE | Yes | Web, Mobile, SPA |
| Client Credentials | No | Service-to-Service |
| Device Authorization | Yes | Smart Devices |
| Refresh Token | No | Session Continuation |

---

# Deprecated OAuth Grant Types

The following grant types are no longer recommended.

### Implicit Grant

Previously used for browser applications.

Problems

- Token exposed in browser
- Token leakage
- Weak security

Modern recommendation

```
Authorization Code

+

PKCE
```

---

### Resource Owner Password Credentials (ROPC)

The user provides credentials directly to the client.

```
User

↓

Username

Password

↓

Application
```

Problems

- Password exposure
- Phishing risk
- No delegated authorization
- Weak separation of trust

ROPC should be avoided except in limited legacy scenarios.

---

# OAuth Security Best Practices

Authorization

- Always use Authorization Code with PKCE for user-facing applications.
- Validate redirect URIs.
- Validate scopes.
- Use short-lived access tokens.
- Rotate refresh tokens.

Client Security

- Protect client secrets.
- Register exact redirect URIs.
- Use HTTPS exclusively.
- Authenticate confidential clients.

Operations

- Monitor token issuance.
- Audit consent events.
- Remove unused clients.
- Rotate secrets regularly.

---

# Common Security Mistakes

Avoid

- Using the Implicit Grant
- Using ROPC in new applications
- Missing PKCE
- Excessive scopes
- Wildcard redirect URIs
- Long-lived tokens
- Shared client secrets
- Missing state validation
- Ignoring refresh token reuse

---

# Key Takeaways

- Authorization Code + PKCE is the recommended OAuth flow for most user-facing applications.
- Client Credentials is designed for service-to-service communication.
- Device Authorization supports devices with limited input capabilities.
- Refresh tokens enable session continuity.
- PKCE significantly strengthens OAuth security by protecting authorization codes.

---

**Next:** OAuth Threats, State Parameter, CSRF Protection, Redirect URI Attacks, Token Leakage, OAuth Client Authentication, Detection Engineering, SIEM Integration, Hands-on Labs, Interview Questions, and Enterprise OAuth Architecture.