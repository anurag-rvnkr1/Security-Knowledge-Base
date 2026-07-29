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

# OAuth Security Threats

OAuth is widely deployed across enterprise applications, but incorrect implementation can introduce serious security vulnerabilities.

Common OAuth attack categories include:

- CSRF attacks
- Authorization code interception
- Redirect URI manipulation
- Token leakage
- Token replay
- Client impersonation
- Scope abuse
- Refresh token theft
- Clickjacking
- Consent phishing

Understanding these threats is essential for secure OAuth deployments.

---

# OAuth Threat Landscape

```
                     OAuth

                       │

        ┌──────────────┼────────────────┐

        ▼              ▼                ▼

   Client Attacks   Token Attacks   Flow Attacks

        │              │                │

        ▼              ▼                ▼

Redirect URI      Token Replay     PKCE Bypass

CSRF              Token Theft      Consent Abuse

Clickjacking      Refresh Theft    Code Interception
```

---

# Cross-Site Request Forgery (CSRF)

An attacker tricks a user's browser into sending an unintended authorization request.

Without proper protection,

the Authorization Server may associate the wrong authorization response with the client.

---

# OAuth CSRF Attack

```
Victim

   │

Already Logged In

   │

Visits Malicious Website

   │

Hidden OAuth Request

   │

Authorization Server

   ▼

Authorization Response

   ▼

Attacker's Session
```

---

# State Parameter

The **state** parameter protects OAuth authorization requests against CSRF.

Client

```
Generate Random State

↓

Authorization Request

↓

Authorization Server

↓

Authorization Response

↓

Validate State
```

---

# State Validation

```
Authorization Response

         │

Compare State

         │

Matches?

    ┌────┴────┐

    ▼         ▼

   Yes       No

    │         │

 Continue   Reject
```

State values should be:

- Random
- Unpredictable
- Single use
- Bound to the user's session

---

# Authorization Code Interception

An attacker intercepts the authorization code before it reaches the legitimate client.

```
User

 │

Authorization Code

 │

Attacker Intercepts

 │

Attempts Token Exchange

 ▼

Authorization Server
```

Without PKCE,

the attacker may obtain an access token.

---

# PKCE Protection

```
Authorization Code

         │

Code Verifier

         │

Verification

         │

Challenge Matches?

    ┌────┴────┐

    ▼         ▼

   Yes       No

    │         │

 Issue     Reject

 Token
```

PKCE prevents attackers from exchanging intercepted authorization codes.

---

# Redirect URI Manipulation

Attackers attempt to redirect authorization responses to attacker-controlled locations.

Example

```
Registered

https://client.example/callback
```

Attacker attempts

```
https://evil.example/callback
```

---

# Redirect URI Validation

```
Incoming Redirect

         │

Registered?

    ┌────┴────┐

    ▼         ▼

   Yes       No

    │         │

 Allow     Reject
```

Never allow wildcard redirect URIs.

---

# Open Redirect Vulnerabilities

Poor redirect validation may allow attackers to steal authorization codes or tokens.

Example

```
client.example

↓

Open Redirect

↓

evil.example
```

Open redirects should be eliminated before integrating OAuth.

---

# Token Leakage

Access tokens may leak through:

- Browser history
- URL parameters
- Proxy logs
- Referrer headers
- Application logs
- Screen captures

Tokens should never appear in URLs.

---

# Secure Token Transmission

Correct

```
Authorization:

Bearer <Access Token>
```

Avoid

```
GET /profile?token=abcdef
```

---

# Token Replay Attack

A stolen access token is reused by an attacker.

```
Valid Token

     │

Copied

     │

Replay

     ▼

Protected API
```

Mitigations

- HTTPS
- Short-lived access tokens
- Token revocation
- Continuous monitoring

---

# Refresh Token Theft

Refresh tokens represent high-value credentials.

```
Refresh Token

       │

Stolen

       │

Request New Access Token

       ▼

Account Compromise
```

Protect refresh tokens with stronger controls than access tokens.

---

# Refresh Token Rotation

```
Refresh Token A

        │

Used

        ▼

Refresh Token B

        │

Old Token Revoked
```

Reuse detection can identify compromised refresh tokens.

---

# Consent Phishing

Attackers create malicious applications requesting excessive permissions.

```
Fake Application

        │

Requests

Read Email

Read Files

Admin Access

        │

User Approves
```

Users should review requested scopes carefully.

---

# Excessive Scopes

Applications sometimes request more permissions than necessary.

Poor example

```
Application

↓

Full Account Access
```

Better

```
Read Calendar Only
```

Always follow the principle of least privilege.

---

# Scope Escalation

An attacker attempts to obtain unauthorized scopes.

```
Requested Scope

↓

read:profile

-----------------

Attacker Requests

↓

admin
```

The Authorization Server must validate permitted scopes.

---

# Clickjacking

Attackers overlay invisible elements over authorization pages.

```
Victim

↓

Invisible Frame

↓

Approves Authorization
```

Mitigations

- CSP
- X-Frame-Options
- Frame restrictions

---

# Client Secret Exposure

Client secrets should remain confidential.

Common exposure sources

- Source code
- Public repositories
- Mobile applications
- Browser JavaScript
- Configuration mistakes

Public clients should not rely on client secrets.

---

# OAuth Client Impersonation

Attackers impersonate legitimate OAuth clients.

```
Fake Client

      │

Requests Authorization

      │

User Trusts

      ▼

Sensitive Data
```

Client registration and redirect URI validation reduce this risk.

---

# Authorization Server Impersonation

Attackers create fake authorization pages.

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

- HTTPS
- Trusted domains
- User awareness
- Passkeys
- MFA

---

# Token Substitution Attack

A token intended for one client or API is presented to another.

```
Token

↓

Wrong Resource Server

↓

Audience Validation

↓

Reject
```

Resource servers must validate the `aud` claim.

---

# Mix-Up Attack

A client communicating with multiple Authorization Servers may accept responses from the wrong server.

```
Client

  │

Auth Server A

Auth Server B

  │

Wrong Response Accepted
```

Clients should validate the expected issuer and endpoint.

---

# OAuth Threat Summary

| Threat | Primary Mitigation |
|---------|--------------------|
| CSRF | State parameter |
| Code interception | PKCE |
| Redirect manipulation | Exact redirect URI validation |
| Token replay | Short-lived tokens and monitoring |
| Refresh theft | Rotation and secure storage |
| Consent phishing | User awareness and scope review |
| Scope escalation | Scope validation |
| Client impersonation | Client authentication |
| Token substitution | Audience validation |
| Mix-Up attack | Issuer validation |

---

# OAuth Security Best Practices

Authorization

- Use Authorization Code with PKCE.
- Require HTTPS.
- Validate every redirect URI.
- Validate issuer and audience.
- Validate scopes.

Client Security

- Protect confidential client secrets.
- Avoid secrets in public clients.
- Register exact redirect URIs.
- Rotate credentials.

Operational Security

- Enable MFA.
- Rotate refresh tokens.
- Monitor abnormal token issuance.
- Audit consent events.
- Revoke compromised tokens promptly.

---

# OAuth Logging

Log

- Authorization requests
- Consent approvals
- Consent denials
- Token issuance
- Token refresh
- Token revocation
- Failed client authentication
- Invalid redirect URI attempts
- Scope validation failures

Do not log

- Access tokens
- Refresh tokens
- Client secrets
- User passwords

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Invalid State | State mismatch during callback |
| Redirect URI Abuse | Requests using unregistered redirect URIs |
| Authorization Code Reuse | Same code exchanged multiple times |
| Refresh Token Reuse | Previously rotated token used again |
| Excessive Scope Requests | Requests for unusually privileged scopes |
| Token Replay | Same access token used from different locations |
| Consent Abuse | Large number of consent approvals for a new client |
| Client Authentication Failures | Multiple failed confidential client logins |
| Issuer Mismatch | Unexpected issuer values |
| Audience Mismatch | Tokens presented to the wrong resource server |

Behavior-based detection provides stronger protection than signature-based detection alone.

---

# SIEM Integration

Recommended log sources

```
Authorization Server

          │

Identity Provider

          │

API Gateway

          │

Application Logs

          │

Reverse Proxy

          │

Cloud IAM

          ▼

Enterprise SIEM

          │

Correlation Rules

          ▼

SOC Alerts
```

Example correlation rules

- Authorization code used more than once
- Refresh token reuse followed by successful login
- Multiple invalid redirect URI attempts
- Excessive OAuth consent approvals within a short period
- Same access token used from multiple countries
- New OAuth client immediately requesting administrative scopes

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

         │                  │

         ▼                  ▼

   Authentication      Consent Engine

         │                  │

         └──────────┬───────┘

                    ▼

              Access Token

                    │

                    ▼

               API Gateway

                    │

          Token Validation

                    │

                    ▼

             Resource Server

                    │

                    ▼

         Logging & Monitoring

                    │

                    ▼

               SIEM / SOC
```

---

# Hands-on Lab 1 – Redirect URI Validation

**Objective**

Review redirect URI validation in an authorized test environment.

**Steps**

1. Register a valid redirect URI.
2. Attempt authorization using an unregistered URI.
3. Confirm the Authorization Server rejects the request.
4. Review logs for validation events.

**Learning Outcomes**

- Redirect URI security
- OAuth endpoint validation
- Secure client registration

---

# Hands-on Lab 2 – PKCE Verification

**Objective**

Verify PKCE enforcement.

**Steps**

1. Generate a valid code challenge.
2. Complete the authorization request.
3. Exchange the authorization code with the correct verifier.
4. Attempt an exchange using an incorrect verifier and confirm rejection.

**Learning Outcomes**

- PKCE workflow
- Authorization code protection
- Secure OAuth implementation

---

# Hands-on Lab 3 – Scope Review

**Objective**

Evaluate OAuth scope assignments.

**Steps**

1. Review client registrations.
2. Identify excessive permissions.
3. Remove unnecessary scopes.
4. Verify least-privilege operation.

**Learning Outcomes**

- Scope management
- Least privilege
- OAuth governance

---

# Troubleshooting

## Invalid Redirect URI

Possible causes

- URI not registered
- Typographical error
- HTTP instead of HTTPS
- Trailing slash mismatch

---

## Invalid State

Possible causes

- CSRF protection working correctly
- Session expired
- Callback tampering
- Incorrect client implementation

---

## Authorization Code Rejected

Possible causes

- Code already used
- Code expired
- PKCE verification failed
- Incorrect client

---

## Token Refresh Failure

Possible causes

- Refresh token expired
- Refresh token revoked
- Refresh token reuse detected
- Client authentication failure

---

## Invalid Scope

Possible causes

- Scope not registered
- Excessive permission request
- Client restriction
- Policy denial

---

# Interview Questions

## Fundamental

1. What problem does OAuth 2.0 solve?
2. Why is OAuth considered an authorization framework rather than an authentication protocol?
3. What is the purpose of the `state` parameter?
4. What is PKCE?
5. Why should redirect URIs be validated?
6. What is a refresh token?
7. Why are scopes important?
8. What is consent in OAuth?
9. What is token replay?
10. Why should client secrets never be embedded in public applications?

---

## Intermediate

11. Explain the Authorization Code Flow.
12. How does PKCE prevent authorization code interception?
13. What is a Mix-Up attack?
14. How would you secure OAuth in a mobile application?
15. Why should refresh token rotation be enabled?
16. How would you detect OAuth token replay?
17. What logs should be forwarded to a SIEM?
18. How would you protect confidential client secrets?
19. Why should wildcard redirect URIs be avoided?
20. How would you investigate excessive scope requests?

---

## Scenario-Based

**Scenario 1**

A confidential client repeatedly receives callback requests with invalid `state` values.

- What attack may be occurring?
- What should you verify first?

---

**Scenario 2**

A refresh token that was already rotated is used again several hours later.

- What does this likely indicate?
- What immediate containment actions would you take?

---

**Scenario 3**

A newly registered OAuth client begins requesting highly privileged scopes across multiple users.

- Which detections should trigger?
- How would you investigate and respond?

---

# Chapter Summary

In this section, we explored OAuth 2.0 security and common implementation threats.

We covered:

- CSRF protection
- State parameter
- PKCE
- Redirect URI validation
- Token replay
- Refresh token security
- Consent phishing
- Scope abuse
- OAuth threat detection
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Secure OAuth deployments rely on strong client validation, least-privilege scopes, robust token handling, and continuous monitoring to defend against modern attack techniques.

---

# Chapter Review

You should now be able to answer:

- Why is the `state` parameter essential?
- How does PKCE protect authorization codes?
- Why should redirect URIs require exact matching?
- How can refresh token reuse indicate compromise?
- Which OAuth events should be monitored by a SIEM?
- How can excessive scope requests be detected?
- What controls reduce the risk of OAuth token replay?

If you can confidently answer these questions, you are ready to continue with **Chapter 13 – OpenID Connect (OIDC)**, where you'll learn how authentication is layered on top of OAuth 2.0 using ID Tokens, discovery endpoints, UserInfo, session management, and enterprise identity federation.

---

# References

## Standards

- RFC 6749 – OAuth 2.0 Authorization Framework
- RFC 6750 – Bearer Token Usage
- RFC 7636 – PKCE
- RFC 7009 – Token Revocation
- RFC 7662 – Token Introspection

## Security Standards

- OAuth 2.0 Security Best Current Practice
- OWASP OAuth Security Cheat Sheet
- OWASP API Security Top 10
- NIST SP 800-63
- NIST Cybersecurity Framework (CSF)

## Further Reading

- OAuth 2.1 Draft Specification
- Financial-grade API (FAPI) Security Profiles
- Enterprise Identity and Access Management Best Practices

---

# What's Next?

➡️ **Chapter 13 – OpenID Connect (OIDC)**

In the next chapter, we will explore:

- OpenID Connect fundamentals
- OAuth vs OIDC
- ID Tokens
- UserInfo Endpoint
- Discovery Document
- Dynamic Client Registration
- Session Management
- Logout Flows
- Federation
- Enterprise Identity Architecture
- Detection Engineering
- SIEM Integration
- Hands-on Labs
- Interview Questions