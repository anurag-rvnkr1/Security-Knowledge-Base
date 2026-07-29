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

# OIDC Authentication Flows

OpenID Connect supports multiple authentication flows depending on the client type and security requirements.

Modern deployments should primarily use:

- Authorization Code Flow with PKCE
- Hybrid Flow (limited enterprise scenarios)

The following are considered legacy and should generally be avoided for new applications:

- Implicit Flow

---

# OIDC Flow Overview

```
                    OpenID Connect

                           │

          ┌────────────────┼────────────────┐

          ▼                ▼                ▼

 Authorization       Hybrid Flow      Implicit Flow
 Code + PKCE                           (Legacy)
```

The Authorization Code Flow with PKCE is recommended for nearly all applications.

---

# Authorization Code Flow with PKCE

```
User

 │

Login

 ▼

OpenID Provider

 │

Authentication

 │

Authorization Code

 ▼

Client

 │

PKCE Verification

 ▼

Token Endpoint

 │

ID Token

Access Token

Refresh Token

 ▼

Application
```

Advantages

- Most secure
- Supports public clients
- Prevents code interception
- Recommended by modern security guidance

---

# Hybrid Flow

Hybrid Flow returns some tokens directly from the authorization endpoint while also returning an authorization code.

Example

```
Authorization Endpoint

        │

Authorization Code

+

ID Token

        │

Client

        │

Token Endpoint

        ▼

Access Token
```

Typical enterprise use cases

- Legacy enterprise integrations
- Specialized identity platforms

Most new deployments should use Authorization Code + PKCE instead.

---

# Implicit Flow (Legacy)

Historically,

tokens were returned directly through the browser.

```
Browser

 │

ID Token

Access Token

 ▼

Application
```

Security concerns

- Token exposure
- Browser history
- Referrer leakage
- Increased interception risk

Modern guidance recommends replacing the Implicit Flow with Authorization Code + PKCE.

---

# OIDC Session Management

Session management allows applications to determine whether the user remains authenticated.

```
User

 │

Authenticated Session

 │

Application

 │

Session Check

 ▼

OpenID Provider
```

Benefits

- Improved user experience
- Centralized identity management
- Consistent authentication state

---

# Local Session vs Identity Session

```
Application Session

        │

Local Cookie

-------------------------

Identity Provider Session

        │

Central Authentication
```

These sessions are related but independent.

Ending one session does not automatically terminate the other unless logout mechanisms are implemented.

---

# Session Lifecycle

```
Authentication

      │

Session Created

      │

Session Active

      │

Session Renewal

      │

Logout

      ▼

Session Destroyed
```

Applications should define reasonable session expiration policies.

---

# Silent Authentication

Silent authentication checks whether an existing authentication session is still valid.

```
Application

      │

Silent Authentication

      ▼

OpenID Provider

      │

Existing Session?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

New ID   Login Required

Token
```

This improves usability while maintaining security.

---

# Single Sign-On (SSO)

OIDC enables centralized authentication across multiple applications.

```
               User

                 │

                 ▼

          OpenID Provider

        ┌────────┼─────────┐

        ▼        ▼         ▼

     App A    App B     App C
```

Users authenticate once and gain access to multiple trusted applications.

---

# Single Logout (SLO)

Single Logout terminates authenticated sessions across connected applications.

```
User

 │

Logout

 ▼

OpenID Provider

 │

Notify Applications

 │

Terminate Sessions

 ▼

Logged Out
```

This prevents lingering authenticated sessions after logout.

---

# Front-Channel Logout

Front-channel logout uses the user's browser.

```
Browser

 │

Logout Request

 ▼

Application

 │

Session Removed
```

Advantages

- Simple implementation

Limitations

- Depends on browser availability
- Less reliable if applications are unreachable

---

# Back-Channel Logout

Back-channel logout communicates directly between servers.

```
OpenID Provider

        │

Server-to-Server Notification

        ▼

Application

        │

Terminate Session
```

Advantages

- More reliable
- Browser independent
- Better suited for enterprise deployments

---

# Dynamic Client Registration

OIDC supports automated client registration.

```
Application

      │

Registration Request

      ▼

OpenID Provider

      │

Client ID

Client Metadata

      ▼

Registered Client
```

Dynamic registration should be carefully controlled in enterprise environments.

---

# Client Metadata

Typical registration metadata includes:

- Client ID
- Redirect URIs
- Grant Types
- Response Types
- Authentication Method
- Supported Algorithms
- Contacts

Proper validation prevents unauthorized client registration.

---

# Identity Federation

Federation enables trusted authentication across organizations.

```
Organization A

        │

Trust Relationship

        │

Organization B

        │

Shared Authentication
```

Users authenticate with their home organization while accessing external services.

---

# Federation Architecture

```
          Enterprise A

               │

         OpenID Provider

               │

Trust

               │

         OpenID Provider

               ▼

          Enterprise B

               │

          Applications
```

Federation reduces identity duplication while maintaining organizational control.

---

# Home Realm Discovery

Home Realm Discovery identifies the user's Identity Provider.

```
User

 │

Email Address

 ▼

Application

 │

Determine Organization

 ▼

Correct Identity Provider
```

Common examples

- alice@company.com
- bob@partner.org

---

# Multi-Tenant Identity

Many SaaS platforms support multiple organizations.

```
Application

      │

Tenant A

Tenant B

Tenant C

      │

Separate Identity Policies
```

Each tenant maintains independent authentication and authorization policies.

---

# OIDC Security Threats

Common threats include:

- ID Token replay
- Nonce bypass
- Token substitution
- Discovery poisoning
- JWKS manipulation
- Issuer spoofing
- Session fixation
- Logout abuse
- Client impersonation
- Metadata tampering

---

# ID Token Replay

An attacker reuses a previously issued ID Token.

```
Valid ID Token

      │

Copied

      │

Replay

      ▼

Application
```

Mitigations

- Validate nonce
- Validate expiration
- Short token lifetime
- Session binding

---

# Nonce Bypass

If applications ignore nonce validation,

attackers may replay authentication responses.

```
ID Token

 │

Nonce Ignored

 ▼

Authentication Accepted
```

Always validate the nonce.

---

# Discovery Poisoning

An attacker attempts to redirect clients to malicious provider metadata.

```
Client

 │

Fake Discovery Document

 ▼

Malicious Endpoints
```

Mitigations

- Validate issuer
- Use trusted provider URLs
- Verify TLS certificates

---

# JWKS Manipulation

Attackers attempt to influence which public keys are trusted.

```
Malicious JWKS

        │

Client Trusts

        ▼

Forged Validation
```

Mitigations

- Retrieve JWKS only from trusted providers
- Validate issuer
- Cache securely
- Monitor unexpected key changes

---

# Issuer Validation

Applications must verify the expected issuer.

```
ID Token

 │

Issuer

 │

Matches Expected?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Allow    Reject
```

Issuer validation prevents trust in unauthorized identity providers.

---

# Audience Validation

The client should verify that the ID Token was issued for itself.

```
ID Token

 │

Audience

 │

Client ID Match?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Allow    Reject
```

---

# Enterprise OIDC Best Practices

Authentication

- Use Authorization Code + PKCE.
- Validate ID Token signatures.
- Validate issuer.
- Validate audience.
- Validate nonce.
- Validate expiration.

Identity

- Use MFA for privileged users.
- Protect refresh tokens.
- Rotate signing keys.
- Enable Single Logout where appropriate.

Operations

- Audit client registrations.
- Review federation trusts.
- Monitor login anomalies.
- Regularly review provider metadata.

---

# OIDC Logging

Log

- Successful authentications
- Failed authentications
- ID Token validation failures
- Nonce mismatches
- Discovery failures
- JWKS updates
- Client registrations
- Logout events
- Federation authentication
- Session expiration

Do not log

- ID Tokens
- Access Tokens
- Refresh Tokens
- Client secrets
- Passwords

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Invalid Nonce | Nonce validation failures |
| Invalid Issuer | Unexpected issuer values |
| Invalid Audience | Audience mismatch |
| ID Token Replay | Same ID Token used repeatedly from different environments |
| Discovery Changes | Unexpected provider metadata updates |
| JWKS Rotation Anomalies | Unplanned signing key changes |
| Excessive Authentication Failures | Brute force or credential attacks |
| Multiple Federation Failures | Cross-organization authentication issues |
| Logout Abuse | Repeated logout requests affecting many users |
| Dynamic Client Registration Abuse | Unusual volume of new client registrations |

---

# SIEM Integration

Recommended telemetry

```
OpenID Provider

        │

Authentication Logs

        │

Discovery Events

        │

JWKS Updates

        │

Application Logs

        │

API Gateway

        ▼

Enterprise SIEM

        │

Correlation Rules

        ▼

SOC Alerts
```

Example correlation rules

- Multiple nonce validation failures from the same client
- Unexpected issuer combined with failed signature validation
- ID Token replay across multiple IP addresses
- Sudden increase in failed federation logins
- Unplanned JWKS updates followed by authentication failures
- Repeated dynamic client registration attempts from unknown sources

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

      ┌────────────┼────────────┐

      ▼            ▼            ▼

 Authentication  Discovery    JWKS

      │            │            │

      └────────────┼────────────┘

                   ▼

             ID Token Issued

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

# Hands-on Lab 1 – ID Token Validation

**Objective**

Review ID Token validation in an authorized environment.

**Steps**

1. Obtain an ID Token from a test identity provider.
2. Verify its signature.
3. Validate the issuer, audience, expiration, and nonce.
4. Confirm that invalid tokens are rejected.

**Learning Outcomes**

- ID Token validation
- Secure OIDC implementation
- Authentication verification

---

# Hands-on Lab 2 – Discovery Verification

**Objective**

Review OIDC discovery configuration.

**Steps**

1. Retrieve the discovery document.
2. Verify published endpoints.
3. Validate the issuer value.
4. Confirm the JWKS URI is trusted.

**Learning Outcomes**

- Discovery validation
- Provider metadata review
- Secure configuration

---

# Hands-on Lab 3 – Federation Assessment

**Objective**

Review federation trust relationships.

**Steps**

1. Identify configured identity providers.
2. Review trust relationships.
3. Verify issuer validation.
4. Review authentication logs for federation events.

**Learning Outcomes**

- Federation assessment
- Identity trust validation
- Enterprise authentication governance

---

# Common Security Mistakes

Avoid

- Treating ID Tokens as Access Tokens
- Skipping nonce validation
- Ignoring issuer verification
- Ignoring audience verification
- Accepting expired ID Tokens
- Trusting unverified discovery documents
- Exposing tokens in browser storage without appropriate protections
- Missing logout implementation
- Excessive identity scopes
- Weak federation governance

---

# Troubleshooting

## Invalid ID Token

Possible causes

- Signature validation failure
- Incorrect issuer
- Invalid audience
- Expired token
- Nonce mismatch

---

## Discovery Failure

Possible causes

- Incorrect discovery URL
- Network issue
- TLS validation failure
- Provider unavailable

---

## JWKS Validation Failure

Possible causes

- Key rotation delay
- Incorrect key identifier (`kid`)
- Cache inconsistency
- Provider configuration issue

---

## Single Logout Not Working

Possible causes

- Incomplete application support
- Back-channel communication failure
- Session synchronization issues
- Browser restrictions (front-channel logout)

---

## Federation Authentication Failure

Possible causes

- Trust configuration error
- Issuer mismatch
- Certificate issue
- Incorrect client registration

---

# Interview Questions

## Fundamental

1. What is OpenID Connect?
2. How does OIDC differ from OAuth 2.0?
3. What is an ID Token?
4. What is the purpose of the `openid` scope?
5. What is the UserInfo endpoint?
6. What is the purpose of the nonce parameter?
7. What is OIDC Discovery?
8. What is JWKS?
9. What is a Relying Party?
10. What is an OpenID Provider?

---

## Intermediate

11. Explain the Authorization Code Flow with PKCE in OIDC.
12. Why should an ID Token never be used as an API access token?
13. How would you validate an ID Token?
14. What is identity federation?
15. Compare front-channel and back-channel logout.
16. How would you investigate ID Token replay?
17. Which OIDC events should be forwarded to a SIEM?
18. Why is issuer validation critical?
19. How would you secure Dynamic Client Registration?
20. How would you troubleshoot JWKS validation failures?

---

## Scenario-Based

**Scenario 1**

A client application begins accepting ID Tokens issued by an unexpected identity provider.

- Which validation failed?
- What risks does this create?
- How would you remediate the issue?

---

**Scenario 2**

Multiple authentication requests fail because the nonce value in the ID Token does not match the original request.

- What security control is functioning correctly?
- What implementation issues should be investigated?

---

**Scenario 3**

A security monitoring system reports repeated authentication failures immediately after an unexpected JWKS update.

- Which components should be investigated first?
- How would you determine whether the change was legitimate or malicious?

---

# Chapter Summary

In this chapter, we explored OpenID Connect (OIDC), the identity layer built on top of OAuth 2.0.

We covered:

- OIDC fundamentals
- OAuth vs OIDC
- ID Tokens
- Claims
- UserInfo endpoint
- Discovery documents
- JWKS
- Session management
- Single Sign-On
- Single Logout
- Federation
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

OIDC provides standardized, interoperable authentication for modern applications while leveraging OAuth 2.0 for delegated authorization.

---

# Chapter Review

You should now be able to answer:

- How does OIDC extend OAuth 2.0?
- What is the difference between an ID Token and an Access Token?
- Why are issuer, audience, and nonce validation mandatory?
- How do Discovery and JWKS simplify secure integration?
- What are the benefits of Single Sign-On and Single Logout?
- Which OIDC events should be monitored by a SIEM?
- How would you investigate an ID Token replay attack?

If you can confidently answer these questions, you are ready to continue with **Chapter 14 – API Gateways**, where you'll explore gateway architecture, request routing, authentication, authorization, rate limiting, caching, WAF integration, observability, and enterprise security controls.

---

# References

## Standards

- OpenID Connect Core 1.0
- OpenID Connect Discovery 1.0
- OpenID Connect Session Management 1.0
- OpenID Connect Front-Channel Logout 1.0
- OpenID Connect Back-Channel Logout 1.0

## Security Standards

- OAuth 2.0 Security Best Current Practice
- OWASP API Security Top 10
- OWASP ASVS
- NIST SP 800-63
- NIST SP 800-207 (Zero Trust Architecture)

## Further Reading

- OpenID Foundation Specifications
- Financial-grade API (FAPI) Security Profiles
- Enterprise Identity and Access Management Best Practices

---

# What's Next?

➡️ **Chapter 14 – API Gateways**

In the next chapter, we will explore:

- API Gateway fundamentals
- Gateway architecture
- Request routing
- Load balancing
- Authentication and authorization
- Rate limiting
- Caching
- API transformation
- WAF integration
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions