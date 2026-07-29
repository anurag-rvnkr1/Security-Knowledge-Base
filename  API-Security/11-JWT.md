# 11 - JWT Security

# Introduction

JSON Web Token (JWT) is a compact, URL-safe token format used to securely transmit claims between two parties.

JWT has become the de facto standard for stateless authentication in:

- REST APIs
- GraphQL APIs
- Microservices
- Cloud-native applications
- Mobile applications
- Single Page Applications (SPAs)
- Identity Providers (IdPs)

JWT enables applications to verify user identity and authorization without maintaining server-side session state.

However, incorrect JWT implementation can introduce serious security vulnerabilities including:

- Token forgery
- Privilege escalation
- Account takeover
- Authentication bypass
- Information disclosure

Understanding JWT internals is essential for secure API development and penetration testing.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand JWT fundamentals.
- Learn JWT structure.
- Understand claims.
- Explore signing algorithms.
- Learn token validation.
- Differentiate access and refresh tokens.
- Identify JWT implementation mistakes.
- Understand common JWT attacks.
- Perform JWT security assessments.

---

# What is JWT?

JWT (JSON Web Token) is a digitally signed token that contains information about a user or client.

Instead of repeatedly querying a database,

the server verifies the token's integrity.

```
User

 │

Login

 ▼

Authentication Server

 │

Generate JWT

 ▼

Client

 │

JWT

 ▼

Protected API
```

JWT is defined by RFC 7519.

---

# Stateless Authentication

Traditional authentication

```
User

 │

Session ID

 ▼

Server

 │

Session Database

 ▼

Authenticated
```

JWT authentication

```
User

 │

JWT

 ▼

Server

 │

Verify Signature

 ▼

Authenticated
```

JWT reduces dependency on centralized session storage.

---

# JWT Structure

A JWT consists of three parts.

```
Header

.

Payload

.

Signature
```

Example

```
xxxxx.yyyyy.zzzzz
```

Each section is Base64URL encoded.

---

# JWT Anatomy

```
JWT

 │

 ├───────────────┐

 ▼               ▼

Header       Payload

       │

       ▼

   Signature
```

The signature protects the integrity of the token.

---

# JWT Header

The header specifies metadata.

Example

```json
{
  "alg": "HS256",
  "typ": "JWT"
}
```

Common fields

| Field | Purpose |
|--------|----------|
| alg | Signing algorithm |
| typ | Token type |
| kid | Key identifier |
| cty | Content type |

---

# JWT Payload

The payload contains claims.

Example

```json
{
  "sub":"12345",
  "name":"Alice",
  "role":"Admin"
}
```

Payloads are **encoded**, not encrypted.

Anyone possessing the token can decode the payload.

Sensitive information should never be stored inside JWT payloads.

---

# JWT Signature

The signature protects token integrity.

```
Header

+

Payload

+

Secret Key

↓

Signing Algorithm

↓

Signature
```

If any part of the token changes,

signature verification fails.

---

# JWT Creation Process

```
Header

      │

Payload

      │

Base64URL Encode

      │

Sign

      │

JWT Generated
```

Only trusted authentication services should generate JWTs.

---

# JWT Validation Process

```
Receive JWT

       │

Parse Header

       │

Verify Signature

       │

Validate Claims

       │

Allow / Deny
```

Validation must occur before processing any protected request.

---

# JWT Claims

Claims are pieces of information stored in the payload.

Three categories exist.

```
Claims

    │

 ┌──┼────────────┐

 ▼  ▼            ▼

Registered Public Private
```

---

# Registered Claims

Standard JWT claims include:

| Claim | Purpose |
|--------|----------|
| iss | Issuer |
| sub | Subject |
| aud | Audience |
| exp | Expiration |
| nbf | Not Before |
| iat | Issued At |
| jti | JWT Identifier |

These claims improve interoperability.

---

# Issuer (iss)

Identifies the entity that issued the token.

Example

```json
{
  "iss":"https://auth.company.com"
}
```

Applications should verify the issuer.

---

# Subject (sub)

Identifies the authenticated identity.

Example

```json
{
  "sub":"user-1001"
}
```

Typically contains:

- User ID
- UUID
- Service Account ID

---

# Audience (aud)

Specifies the intended recipient.

Example

```json
{
  "aud":"inventory-api"
}
```

Tokens should only be accepted by the intended audience.

---

# Expiration (exp)

Defines when the token expires.

Example

```json
{
  "exp":1735689600
}
```

Expired tokens must be rejected.

---

# Not Before (nbf)

Specifies the earliest valid time.

Example

```json
{
  "nbf":1735680000
}
```

Tokens should not be accepted before this timestamp.

---

# Issued At (iat)

Indicates when the token was created.

Example

```json
{
  "iat":1735680000
}
```

Useful for replay detection and token age evaluation.

---

# JWT ID (jti)

Provides a unique identifier.

Example

```json
{
  "jti":"bfa6d761"
}
```

Useful for:

- Revocation
- Replay detection
- Audit logging

---

# Public Claims

Public claims are standardized but not reserved.

Examples

```
email

tenant

department

region
```

They should be clearly defined to avoid naming conflicts.

---

# Private Claims

Private claims are application-specific.

Example

```json
{
  "role":"Manager",
  "tenant":"India"
}
```

Applications should validate all authorization-related claims.

---

# Common JWT Algorithms

| Algorithm | Type |
|------------|------|
| HS256 | HMAC |
| HS384 | HMAC |
| HS512 | HMAC |
| RS256 | RSA |
| RS384 | RSA |
| RS512 | RSA |
| ES256 | ECDSA |
| EdDSA | Edwards Curve |

Modern deployments commonly use RS256, ES256, or EdDSA.

---

# Symmetric Algorithms

Example

```
Authentication Server

 │

Shared Secret

 │

Sign

 │

Verify
```

Characteristics

- Fast
- Simple
- Single shared secret

Suitable for trusted environments.

---

# Asymmetric Algorithms

Example

```
Private Key

↓

Sign

↓

JWT

↓

Public Key

↓

Verify
```

Advantages

- Public verification
- Better key separation
- Improved scalability
- Preferred for enterprise identity systems

---

# HS256 vs RS256

| HS256 | RS256 |
|--------|--------|
| Shared secret | Public/private key pair |
| Simpler | Better key management |
| Secret shared with verifier | Public key distributed safely |
| Suitable for smaller deployments | Preferred for enterprise APIs |

---

# Base64URL Encoding

JWT components use Base64URL encoding.

Encoding is **not encryption**.

Example

```
Payload

↓

Base64URL

↓

Readable After Decoding
```

Attackers can inspect payload contents without breaking the signature.

---

# JWT Example

```
Header

↓

{
 "alg":"RS256",
 "typ":"JWT"
}

↓

Payload

↓

{
 "sub":"1001",
 "role":"User"
}

↓

Signature
```

Changing any signed content invalidates the signature.

---

# JWT Request Flow

```
User

 │

Login

 ▼

Identity Provider

 │

JWT Issued

 ▼

Client

 │

Authorization:

Bearer <JWT>

 ▼

API Gateway

 │

Signature Validation

 ▼

Application
```

Bearer tokens should always be transmitted over HTTPS.

---

# Enterprise JWT Architecture

```
                 User

                   │

                   ▼

           Identity Provider

                   │

          JWT Generation

                   │

                   ▼

             API Gateway

                   │

      Signature Validation

                   │

                   ▼

          Microservices

                   │

                   ▼

          Authorization
```

Centralized validation improves consistency and simplifies key management.

---

# Best Practices

Token Design

- Keep tokens small.
- Include only necessary claims.
- Avoid sensitive information.
- Use standard claims where appropriate.

Security

- Always use HTTPS.
- Validate signatures.
- Validate issuer and audience.
- Reject expired tokens.
- Rotate signing keys.

Operations

- Log token validation failures.
- Protect signing keys.
- Short token lifetime.
- Separate access and refresh tokens.

---

# Common Mistakes

Avoid:

- Trusting unsigned tokens
- Accepting expired tokens
- Ignoring issuer validation
- Ignoring audience validation
- Storing secrets in JWT payloads
- Long-lived access tokens
- Weak signing keys
- Sharing signing keys unnecessarily
- Logging full JWTs in plaintext

---

# Key Takeaways

- JWT is a compact, signed token format used for stateless authentication.
- A JWT consists of a header, payload, and signature.
- Claims provide identity and authorization information.
- Payloads are encoded, not encrypted.
- Proper validation of signatures and registered claims is essential.
- Strong key management and short-lived tokens improve security.

---

# Access Tokens

Access tokens are short-lived credentials used by clients to access protected resources.

After successful authentication,

the Identity Provider issues an access token.

```
User

 │

Authenticate

 ▼

Identity Provider

 │

Access Token

 ▼

Client

 │

Bearer Token

 ▼

Protected API
```

Access tokens should have a short lifetime to reduce the impact of token theft.

---

# Characteristics of Access Tokens

Typical characteristics

- Short-lived
- Digitally signed
- Self-contained
- Stateless
- Sent with each request
- Intended for resource servers

Example

```
Authorization:

Bearer eyJhbGciOiJSUzI1NiIs...
```

---

# Access Token Lifecycle

```
Authentication

        │

Issue Token

        │

Use Token

        │

Expires

        │

Refresh

        ▼

New Access Token
```

Expired access tokens should never be accepted.

---

# Refresh Tokens

Refresh tokens allow clients to obtain new access tokens without requiring the user to authenticate again.

```
User

 │

Login

 ▼

Identity Provider

 │

Access Token

+

Refresh Token

 ▼

Client
```

Refresh tokens are generally longer-lived than access tokens.

---

# Refresh Token Flow

```
Access Token

Expired

      │

Refresh Token

      │

Identity Provider

      │

Issue New Access Token

      ▼

Continue Session
```

Only the authorization server should process refresh tokens.

---

# Access Token vs Refresh Token

| Access Token | Refresh Token |
|--------------|---------------|
| Short-lived | Long-lived |
| Access APIs | Obtain new access tokens |
| Sent frequently | Sent only to authorization server |
| Higher exposure | Better protected |
| Used by resource server | Used by identity provider |

---

# Refresh Token Security

Refresh tokens require stronger protection than access tokens.

Recommendations

- Store securely
- Rotate regularly
- Encrypt at rest
- Detect reuse
- Bind to trusted clients
- Revoke upon logout

A compromised refresh token may allow attackers to obtain new access tokens repeatedly.

---

# Refresh Token Rotation

Instead of reusing refresh tokens,

a new refresh token is issued after every successful refresh.

```
Refresh Token A

        │

Used

        ▼

Access Token B

+

Refresh Token B

        │

Old Token Invalid
```

Token rotation reduces replay risk.

---

# Refresh Token Reuse Detection

```
Refresh Token

        │

Previously Used?

   ┌────┴────┐

   ▼         ▼

No         Yes

   │         │

Issue     Revoke Session

New Token
```

Reuse often indicates token theft.

---

# Token Expiration

Every JWT should include an expiration claim.

Example

```json
{
  "exp": 1735689600
}
```

Benefits

- Limits exposure
- Reduces replay window
- Supports session lifecycle

---

# Recommended Token Lifetimes

These values vary depending on business requirements.

| Token Type | Typical Lifetime |
|------------|------------------|
| Access Token | Minutes |
| Refresh Token | Days to Weeks |
| Password Reset Token | Minutes |
| Email Verification Token | Hours |

Security should take precedence over convenience for privileged environments.

---

# Token Revocation

Sometimes tokens must be invalidated before expiration.

Examples

- User logout
- Password reset
- Account compromise
- Device loss
- Privilege changes

---

# Revocation Workflow

```
Compromise Detected

        │

Revoke Token

        │

Revocation Store

        │

Future Requests

        ▼

Rejected
```

Revocation mechanisms are particularly important for long-lived tokens.

---

# Blacklisting Tokens

A blacklist stores revoked token identifiers.

```
Incoming JWT

      │

Extract jti

      │

Blacklist Lookup

 ┌────┴────┐

 ▼         ▼

Found    Not Found

 ▼         ▼

Reject   Continue Validation
```

Useful for emergency revocation.

---

# Whitelisting Tokens

Some systems maintain a whitelist of valid sessions.

```
JWT

 │

Session Store

 │

Valid?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Allow    Reject
```

Provides greater control but reduces the benefits of fully stateless authentication.

---

# JWT Signing Keys

The security of JWT depends heavily on signing key protection.

```
Private Key

       │

Sign JWT

       ▼

Token

       │

Public Key

       ▼

Verify
```

Private keys should never be exposed.

---

# Key Management

Good key management includes:

- Secure generation
- Hardware-backed storage where possible
- Restricted access
- Rotation
- Backup
- Auditing

Signing keys are among the most sensitive secrets in an authentication system.

---

# Key Rotation

Signing keys should be rotated periodically.

```
Old Key

 │

New Key Generated

 │

Both Keys Valid

 │

Old Key Retired

 ▼

Rotation Complete
```

Gradual rotation avoids disrupting active sessions.

---

# Key Identifier (kid)

The `kid` header identifies the signing key.

Example

```json
{
  "alg":"RS256",
  "kid":"key-2026-07"
}
```

Applications use the key identifier to select the correct verification key.

---

# JSON Web Key (JWK)

A JSON Web Key represents a cryptographic key using JSON.

Example

```json
{
  "kty":"RSA",
  "kid":"key-2026",
  "use":"sig"
}
```

JWK simplifies key distribution.

---

# JSON Web Key Set (JWKS)

A JWKS endpoint publishes public verification keys.

```
Identity Provider

       │

JWKS Endpoint

       │

Public Keys

       ▼

Applications
```

Resource servers retrieve public keys without exposing private keys.

---

# JWKS Validation Flow

```
JWT

 │

Read kid

 │

Download JWKS

 │

Select Matching Key

 │

Verify Signature

 ▼

Accept / Reject
```

JWKS should be retrieved securely and cached appropriately.

---

# JWT Validation Checklist

Every JWT should be validated for:

- Signature
- Algorithm
- Issuer
- Audience
- Expiration
- Not Before
- Issued At
- Token Identifier (when applicable)

Skipping any validation step may weaken security.

---

# JWT Algorithm Validation

Applications must verify the expected algorithm.

```
JWT

 │

alg = RS256?

 ┌────┴────┐

 ▼         ▼

Yes       No

 ▼         ▼

Continue Reject
```

Never trust the algorithm specified by an attacker-controlled token without enforcing an expected value.

---

# The "alg:none" Attack

Historically, some implementations accepted unsigned JWTs.

Example

```json
{
  "alg":"none"
}
```

If signature verification is skipped,

an attacker may create arbitrary tokens.

Modern libraries generally reject this configuration by default, but verification is still essential.

---

# Algorithm Confusion Attack

Some vulnerable implementations incorrectly treat asymmetric and symmetric algorithms as interchangeable.

Example

```
Expected

RS256

↓

Attacker Uses

HS256

↓

Incorrect Verification
```

Applications should explicitly enforce supported algorithms.

---

# Weak Secret Attack

Weak HMAC secrets may be guessed through offline attacks.

Example of poor secrets

- password
- secret
- admin123

Recommendations

- Long random secrets
- Secure secret storage
- Regular rotation

---

# Token Replay Attack

An attacker reuses a stolen token.

```
Valid JWT

     │

Stolen

     │

Replay

     ▼

Unauthorized Access
```

Mitigations

- Short expiration
- TLS
- Token binding (where applicable)
- Device-aware monitoring
- Revocation

---

# JWT Theft

Tokens may be stolen through:

- Cross-Site Scripting (XSS)
- Malware
- Memory disclosure
- Browser extensions
- Insecure storage
- Logging

Secure storage is critical.

---

# Secure Token Storage

Preferred approaches depend on application architecture.

General guidance

- Protect tokens from client-side script access where appropriate.
- Avoid persistent storage unless necessary.
- Encrypt sensitive data at rest.
- Protect mobile secure storage.
- Never expose tokens in URLs.

---

# JWT in HTTP Requests

Standard format

```
Authorization:

Bearer <JWT>
```

Avoid transmitting JWTs through:

- URL query parameters
- Referrer headers
- Browser history
- Log files

---

# Enterprise JWT Flow

```
              User

                │

                ▼

         Identity Provider

                │

        Access Token

        Refresh Token

                │

                ▼

            API Gateway

                │

        Signature Validation

                │

        Authorization Check

                │

                ▼

          Protected APIs
```

The API Gateway often performs initial JWT validation before forwarding requests.

---

# JWT Best Practices

Design

- Short-lived access tokens
- Minimal claims
- Standard registered claims
- Separate access and refresh tokens

Security

- HTTPS only
- Strong signing keys
- Algorithm enforcement
- Validate every request
- Rotate signing keys

Operations

- Monitor failed validations
- Revoke compromised tokens
- Log validation outcomes
- Protect JWKS endpoints

---

# Common Security Mistakes

Avoid

- Accepting unsigned JWTs
- Ignoring expiration
- Weak signing secrets
- Missing issuer validation
- Missing audience validation
- Long-lived access tokens
- Exposing JWTs in URLs
- Logging entire tokens
- Storing sensitive data in JWT payloads
- Failing to rotate signing keys

---

# Detection Engineering

Recommended detections

| Detection | Indicator |
|-----------|-----------|
| Invalid Signature | Repeated signature verification failures |
| Expired Token Usage | Requests using expired JWTs |
| Unknown Issuer | Unexpected `iss` values |
| Invalid Audience | Incorrect `aud` claim |
| Token Replay | Same JWT observed from multiple devices or locations |
| Algorithm Mismatch | Unexpected `alg` values |
| Refresh Token Reuse | Repeated use of invalidated refresh tokens |
| Excessive Token Failures | High volume of authentication failures |

Correlation rules should distinguish between user error and malicious activity.

---

# SIEM Integration

Recommended telemetry

```
Identity Provider

        │

JWT Validation Logs

        │

API Gateway

        │

Application Logs

        │

Key Rotation Events

        ▼

Enterprise SIEM

        │

Correlation Rules

        ▼

SOC Alerts
```

Example correlation rules

- Multiple invalid JWT signatures from one source
- Successful login followed by token replay from another region
- Repeated refresh token reuse attempts
- Spike in expired token submissions
- Unexpected signing key changes

---

# Hands-on Lab 1 – JWT Inspection

**Objective**

Understand the structure of a JWT in an authorized environment.

**Steps**

1. Obtain a JWT from a test environment.
2. Decode the header and payload using approved tools.
3. Identify registered and private claims.
4. Verify that no sensitive information is stored in the payload.

**Learning Outcomes**

- JWT structure
- Claim analysis
- Secure token design

---

# Hands-on Lab 2 – Validation Review

**Objective**

Review JWT validation logic.

**Steps**

1. Verify signature validation.
2. Confirm issuer and audience verification.
3. Test expired token handling.
4. Ensure unsupported algorithms are rejected.

**Learning Outcomes**

- JWT validation
- Secure implementation
- Defensive configuration

---

# Hands-on Lab 3 – Key Rotation Review

**Objective**

Review signing key management.

**Steps**

1. Identify the current signing key strategy.
2. Verify support for key rotation.
3. Confirm JWKS publication of active public keys.
4. Review logging of key management events.

**Learning Outcomes**

- Key lifecycle management
- JWKS usage
- Operational security

---

# Troubleshooting

## JWT Rejected

Possible causes

- Invalid signature
- Incorrect issuer
- Invalid audience
- Corrupted token
- Unsupported algorithm

---

## Token Expired

Possible causes

- Normal expiration
- Client clock issues
- Long-running session
- Refresh token unavailable

---

## Signature Verification Failure

Possible causes

- Incorrect public key
- Key rotation mismatch
- Token modification
- Wrong algorithm

---

## Refresh Token Failure

Possible causes

- Token reuse detected
- Revoked refresh token
- Expired refresh token
- Client configuration error

---

## JWKS Retrieval Failure

Possible causes

- Network issue
- Incorrect endpoint
- Cache problems
- Key publication delay

---

# Interview Questions

## Fundamental

1. What is a JWT?
2. What are the three parts of a JWT?
3. What is the purpose of the JWT signature?
4. Why is Base64URL encoding not encryption?
5. What is the difference between an access token and a refresh token?
6. What is the purpose of the `exp` claim?
7. What is JWKS?
8. What is the purpose of the `kid` header?
9. Why should JWTs be transmitted over HTTPS?
10. Why shouldn't sensitive information be stored in JWT payloads?

---

## Intermediate

11. Explain refresh token rotation.
12. What is the `alg:none` attack?
13. How does an algorithm confusion attack work?
14. How would you securely rotate JWT signing keys?
15. Compare HS256 and RS256.
16. How would you detect token replay?
17. Why is issuer validation important?
18. What events related to JWT should be logged?
19. How would you design JWT validation in a microservices environment?
20. How would you revoke a compromised JWT?

---

## Scenario-Based

**Scenario 1**

Multiple requests using the same valid JWT are observed simultaneously from different countries.

- What attack may be occurring?
- Which containment actions would you take?

---

**Scenario 2**

A security assessment reveals that an API accepts JWTs with `"alg":"none"`.

- Why is this dangerous?
- How should the implementation be corrected?

---

**Scenario 3**

Your organization rotates JWT signing keys monthly.

- How can active sessions continue working during key rotation?
- What role does JWKS play in this process?

---

# Chapter Summary

In this chapter, we explored JWT security in enterprise applications.

We covered:

- Access tokens
- Refresh tokens
- Token lifecycles
- Token revocation
- Signing algorithms
- JWK and JWKS
- Key rotation
- JWT validation
- Common JWT attacks
- Detection engineering
- SIEM integration
- Hands-on labs
- Troubleshooting
- Interview preparation

Proper JWT implementation combines strong cryptography, rigorous validation, secure key management, and continuous monitoring to provide secure, scalable authentication for modern APIs.

---

# Chapter Review

You should now be able to answer:

- How do access and refresh tokens differ?
- Why is refresh token rotation recommended?
- What validations should every JWT undergo?
- How do JWKS and `kid` support secure key rotation?
- How can token replay attacks be detected and mitigated?
- Why are algorithm enforcement and signature verification critical?
- Which JWT events should be monitored by a SIEM?

If you can confidently answer these questions, you are ready to continue with **Chapter 12 – OAuth 2.0**, where you'll explore delegated authorization, OAuth roles, grant types, PKCE, scopes, client authentication, security threats, and enterprise implementation patterns.

---

# References

## Standards

- RFC 7519 – JSON Web Token (JWT)
- RFC 7517 – JSON Web Key (JWK)
- RFC 7518 – JSON Web Algorithms (JWA)
- RFC 7515 – JSON Web Signature (JWS)
- RFC 8725 – JWT Best Current Practices

## Security Standards

- OWASP API Security Top 10
- OWASP ASVS
- OWASP JWT Cheat Sheet
- NIST SP 800-63
- NIST Cybersecurity Framework (CSF)

## Further Reading

- JSON Object Signing and Encryption (JOSE) Specifications
- Enterprise Identity Architecture Guides
- API Security Best Practices

---

# What's Next?

➡️ **Chapter 12 – OAuth 2.0**

In the next chapter, we will explore:

- OAuth 2.0 fundamentals
- OAuth roles
- Authorization framework
- Grant types
- Authorization Code Flow
- PKCE
- Client authentication
- Scopes
- Tokens
- OAuth attacks
- Detection engineering
- SIEM integration
- Hands-on labs
- Interview questions