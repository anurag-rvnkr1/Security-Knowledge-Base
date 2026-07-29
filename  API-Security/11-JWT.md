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

**Next:** Access Tokens, Refresh Tokens, Key Rotation, JWT Attacks (alg:none, algorithm confusion, token replay), JWKS, JWK, Detection Engineering, SIEM Integration, Hands-on Labs, and Interview Questions.