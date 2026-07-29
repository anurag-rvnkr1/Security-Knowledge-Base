# 13 - OpenID Connect (OIDC)

# Introduction

OpenID Connect (OIDC) is an identity layer built on top of OAuth 2.0.

While OAuth 2.0 provides **authorization**,

OpenID Connect provides **authentication**.

OIDC allows applications to verify the identity of a user and obtain basic profile information in a standardized manner.

It has become the industry standard for modern authentication across:

- Cloud Applications
- Enterprise Portals
- Mobile Applications
- Single Page Applications (SPAs)
- REST APIs
- Microservices
- Identity Providers
- SaaS Platforms

Major identity platforms support OIDC, including:

- Microsoft Entra ID
- Okta
- Auth0
- Keycloak
- Google Identity
- Ping Identity

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand OpenID Connect fundamentals.
- Differentiate OAuth 2.0 from OIDC.
- Learn OIDC components.
- Understand ID Tokens.
- Explore UserInfo endpoints.
- Learn OIDC Discovery.
- Understand authentication flows.
- Learn enterprise federation.
- Identify OIDC security threats.
- Perform OIDC security assessments.

---

# Why OpenID Connect?

OAuth answers:

```
Can this application access the resource?
```

OIDC answers:

```
Who is the authenticated user?
```

OAuth delegates authorization.

OIDC standardizes authentication.

---

# OAuth vs OpenID Connect

| OAuth 2.0 | OpenID Connect |
|-----------|----------------|
| Authorization | Authentication + Authorization |
| Access Token | Access Token + ID Token |
| Resource Access | User Identity |
| API Permissions | Identity Verification |
| Scopes | Identity Claims |

OIDC extends OAuth instead of replacing it.

---

# OpenID Connect Architecture

```
                 User

                   │

                   ▼

          Client Application

                   │

                   ▼

         OpenID Provider (OP)

                   │

        Authentication

                   │

     ID Token + Access Token

                   ▼

        Protected Resources
```

---

# OIDC Terminology

| Term | Description |
|------|-------------|
| OP | OpenID Provider |
| RP | Relying Party |
| ID Token | Identity Token |
| Access Token | API Authorization |
| UserInfo | User Profile Endpoint |
| Discovery | Provider Metadata |
| Claims | User Attributes |

---

# OpenID Provider (OP)

The OpenID Provider authenticates users.

Responsibilities

- Authenticate users
- Issue ID Tokens
- Issue Access Tokens
- Publish metadata
- Publish public keys
- Support discovery

Examples

- Microsoft Entra ID
- Auth0
- Keycloak
- Okta
- Google Identity

---

# Relying Party (RP)

The Relying Party is the application trusting the OpenID Provider.

Examples

- Enterprise Portal
- Banking Application
- HR Portal
- Customer Dashboard
- Mobile Application

The RP verifies the identity information contained in the ID Token.

---

# OIDC Authentication Flow

```
User

 │

Login

 ▼

OpenID Provider

 │

Authenticate

 ▼

ID Token

Access Token

 ▼

Client Application

 │

Verify Identity

 ▼

Authenticated User
```

---

# OpenID Connect Flow

```
             User

               │

               ▼

        Client Application

               │

Authorization Request

               ▼

        OpenID Provider

               │

Authentication

               │

Consent

               ▼

 Authorization Code

               │

               ▼

       Token Endpoint

               │

               ▼

 ID Token + Access Token

               │

               ▼

      Client Application
```

The Authorization Code Flow with PKCE is the recommended deployment model.

---

# ID Token

The ID Token is a JWT containing information about the authenticated user.

Example

```
Header

↓

Payload

↓

Signature
```

Unlike an Access Token,

an ID Token is intended for the client application,

not the Resource Server.

---

# ID Token Example

```json
{
  "iss":"https://login.company.com",
  "sub":"123456",
  "aud":"inventory-app",
  "exp":1735689600,
  "iat":1735680000,
  "email":"alice@example.com"
}
```

The client verifies these claims before trusting the identity.

---

# ID Token Claims

Common claims

| Claim | Purpose |
|--------|----------|
| iss | Issuer |
| sub | Subject |
| aud | Audience |
| exp | Expiration |
| iat | Issued At |
| auth_time | Authentication Time |
| nonce | Replay Protection |
| email | User Email |
| name | Display Name |

---

# Authentication Time (auth_time)

Indicates when the user authenticated.

Example

```json
{
  "auth_time":1735680000
}
```

Useful for enforcing re-authentication policies.

---

# Nonce

The **nonce** protects OIDC authentication against replay attacks.

Client

```
Generate Random Nonce

↓

Authentication Request

↓

ID Token

↓

Validate Nonce
```

Nonce values should be:

- Random
- Unpredictable
- Single use
- Session-bound

---

# Nonce Validation

```
ID Token

    │

Compare Nonce

    │

Matches?

 ┌──┴────┐

 ▼       ▼

Yes      No

 ▼        ▼

Allow   Reject
```

Nonce validation is mandatory for flows where ID Tokens are returned through the browser.

---

# OIDC Scopes

OIDC introduces identity-related scopes.

Common scopes

```
openid
```

```
profile
```

```
email
```

```
phone
```

```
address
```

```
offline_access
```

The `openid` scope is mandatory for OIDC.

---

# Common Scope Usage

| Scope | Information Returned |
|--------|----------------------|
| openid | ID Token |
| profile | Name, picture, locale |
| email | Email address |
| phone | Phone number |
| address | Address claims |
| offline_access | Refresh token eligibility |

Applications should request only the required scopes.

---

# UserInfo Endpoint

The UserInfo endpoint returns profile information about the authenticated user.

```
Client

 │

Access Token

 ▼

UserInfo Endpoint

 │

User Claims

 ▼

Application
```

---

# UserInfo Response

Example

```json
{
  "sub":"123456",
  "name":"Alice",
  "email":"alice@example.com",
  "preferred_username":"alice"
}
```

The `sub` claim should match the ID Token.

---

# OIDC Discovery

Discovery allows clients to automatically locate provider configuration.

Example endpoint

```
/.well-known/openid-configuration
```

The discovery document publishes:

- Authorization endpoint
- Token endpoint
- JWKS URI
- UserInfo endpoint
- Supported scopes
- Supported algorithms

---

# Discovery Workflow

```
Client

 │

Discovery Request

 ▼

OpenID Provider

 │

Metadata

 ▼

Client Configuration
```

Discovery simplifies client configuration.

---

# Discovery Document Example

```json
{
  "issuer":"https://login.company.com",
  "authorization_endpoint":"...",
  "token_endpoint":"...",
  "userinfo_endpoint":"...",
  "jwks_uri":"..."
}
```

Clients should validate the issuer before trusting metadata.

---

# JWKS Endpoint

OIDC providers publish public signing keys.

```
OpenID Provider

      │

JWKS Endpoint

      │

Public Keys

      ▼

Client
```

Clients use these keys to verify ID Token signatures.

---

# ID Token Validation

Every ID Token should be validated.

```
Receive ID Token

        │

Verify Signature

        │

Validate Issuer

        │

Validate Audience

        │

Validate Expiration

        │

Validate Nonce

        │

Accept / Reject
```

Skipping validation may allow authentication bypass.

---

# Authentication Request Parameters

Common parameters

| Parameter | Purpose |
|-----------|----------|
| client_id | Client Identifier |
| response_type | Requested OAuth response |
| scope | Requested permissions |
| redirect_uri | Callback location |
| state | CSRF protection |
| nonce | Replay protection |

---

# Enterprise OIDC Architecture

```
                 User

                   │

                   ▼

           Client Application

                   │

                   ▼

          OpenID Provider

         │      │      │

         ▼      ▼      ▼

 Authentication Tokens Discovery

                   │

                   ▼

          Enterprise APIs

                   │

                   ▼

         Logging & Monitoring

                   │

                   ▼

             SIEM / SOC
```

---

# Best Practices

Authentication

- Use Authorization Code with PKCE.
- Validate ID Token signatures.
- Validate issuer.
- Validate audience.
- Validate nonce.

Application Security

- Request minimum scopes.
- Verify UserInfo responses.
- Use HTTPS.
- Rotate signing keys.
- Protect refresh tokens.

Operations

- Monitor authentication events.
- Audit client registrations.
- Log validation failures.
- Review provider metadata.

---

# Common Mistakes

Avoid

- Treating OAuth as authentication
- Skipping nonce validation
- Ignoring issuer validation
- Ignoring audience validation
- Accepting expired ID Tokens
- Using ID Tokens to authorize API access
- Failing to verify signatures
- Logging sensitive token contents
- Requesting excessive identity scopes

---

# Key Takeaways

- OIDC adds authentication capabilities to OAuth 2.0.
- The ID Token represents the authenticated user's identity.
- The `openid` scope enables OIDC.
- Nonce protects against replay attacks.
- Discovery and JWKS simplify secure integration.
- Proper ID Token validation is mandatory.

---

**Next:** OIDC Authentication Flows, Session Management, Single Logout, Dynamic Client Registration, Federation, OIDC Security Threats, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.
