# 34-JWT-Security.md

# Part 1 — Introduction to JSON Web Tokens (JWT), Token-Based Authentication, JWT Structure, and Enterprise Identity

> **"A JSON Web Token (JWT) is a compact, digitally signed token that securely carries claims between parties. A JWT is trusted only after successful validation—it should never be trusted merely because it exists."**

---

# Learning Objectives

After completing this part, you will understand:

- What JWT is
- Why JWT Exists
- Token-Based Authentication
- JWT Architecture
- JWT Components
- JWT Claims
- Signed vs Encrypted Tokens
- JWT in OAuth & OpenID Connect
- Enterprise JWT Architecture
- Security Fundamentals

---

# What is JWT?

**JSON Web Token (JWT)** is an open standard (RFC 7519) for securely transmitting claims between parties as a compact JSON object.

JWTs are commonly used for:

- Authentication
- Authorization
- Identity Federation
- API Security
- Single Sign-On (SSO)
- Microservices

---

# Why JWT?

Traditional session-based authentication often requires server-side session storage.

```
User

↓

Login

↓

Server Session

↓

Database / Session Store
```

JWT enables stateless authentication.

```
User

↓

Login

↓

JWT

↓

Client

↓

Protected APIs
```

The server validates the token instead of maintaining session state.

---

# Stateless Authentication

In stateless authentication:

```
Client

↓

JWT

↓

Server Validation

↓

Access Decision
```

The server does not rely on per-user session storage for every request.

---

# Why Organizations Use JWT

```
JWT Benefits

│

├── Compact Format

├── Stateless Authentication

├── API Friendly

├── Cross-Platform

├── Distributed Systems

├── Microservices Support

└── Identity Federation
```

JWT integrates well with modern web and cloud architectures.

---

# Common JWT Use Cases

```
Applications

│

├── Web Applications

├── Mobile Applications

├── REST APIs

├── GraphQL APIs

├── Microservices

├── Cloud Applications

├── Single Sign-On

└── API Gateways
```

---

# JWT Lifecycle

```
User Login

↓

Authentication

↓

JWT Issued

↓

Client Stores Token

↓

Protected Requests

↓

JWT Validation

↓

Access Granted
```

The token is validated before access is granted.

---

# JWT Architecture

```
Client

↓

Identity Provider

↓

JWT Issuance

↓

API Gateway

↓

Resource Server

↓

Business Service
```

Identity and business services remain logically separated.

---

# JWT Structure

A JWT consists of three Base64URL-encoded sections.

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

Each component has a distinct purpose.

---

# JWT Header

The Header contains metadata about the token.

Typical information includes:

```
Header

↓

Algorithm

↓

Token Type
```

The Header tells the verifier how the token is protected.

---

# JWT Payload

The Payload contains **claims**.

```
Payload

↓

Claims

↓

Application Data
```

Claims provide information used by applications during authorization and identity decisions.

---

# JWT Signature

The Signature protects token integrity.

```
Header

+

Payload

↓

Signing Process

↓

Signature
```

If the signature validation fails, the token should not be trusted.

---

# JWT Visualization

```
+----------------+

Header

+----------------+

|

v

+----------------+

Payload

+----------------+

|

v

+----------------+

Signature

+----------------+
```

All three sections together form the complete JWT.

---

# JWT Claims

Claims represent statements about a user, client, or token.

```
Claims

│

├── Registered Claims

├── Public Claims

└── Private Claims
```

---

# Registered Claims

Common registered claims include:

| Claim | Purpose |
|--------|----------|
| iss | Issuer |
| sub | Subject |
| aud | Audience |
| exp | Expiration Time |
| nbf | Not Before |
| iat | Issued At |
| jti | JWT Identifier |

These standardized claims improve interoperability.

---

# Public Claims

Public claims are standardized or publicly defined claims that applications may share across systems.

Examples include:

- Profile information
- Identity attributes
- Application-specific metadata using collision-resistant names

---

# Private Claims

Private claims are agreed upon between participating applications.

```
Organization

↓

Custom Claims

↓

Business Application
```

Organizations should include only information necessary for application functionality.

---

# Signed vs Encrypted Tokens

JWTs may be:

```
JWT

│

├── Signed (JWS)

└── Encrypted (JWE)
```

---

# Signed JWT (JWS)

A signed JWT protects integrity.

```
Header

↓

Payload

↓

Signature

↓

Validation
```

Recipients can verify that the content has not been modified.

---

# Encrypted JWT (JWE)

An encrypted JWT protects confidentiality.

```
Plain Claims

↓

Encryption

↓

Encrypted JWT

↓

Authorized Recipient
```

Only authorized recipients can decrypt the protected content.

---

# JWS vs JWE

| JWS | JWE |
|------|------|
| Protects Integrity | Protects Confidentiality |
| Digitally Signed | Encrypted |
| Verifiable | Confidential |
| Common for APIs | Used when claim confidentiality is required |

Some systems may use both signing and encryption depending on security requirements.

---

# JWT in OAuth 2.0

Many OAuth deployments use JWTs as Access Tokens.

```
User

↓

Authorization Server

↓

JWT Access Token

↓

Resource Server
```

The Resource Server validates the JWT before granting access.

---

# JWT in OpenID Connect

OIDC commonly uses JWTs for ID Tokens.

```
User Login

↓

Identity Provider

↓

JWT ID Token

↓

Application
```

The application validates the token before trusting identity information.

---

# Enterprise Identity Architecture

```
Internet

↓

Load Balancer

↓

Identity Provider

↓

JWT Issuance

↓

API Gateway

↓

Business APIs

↓

Database
```

JWTs enable secure identity propagation across distributed services.

---

# Microservices Example

```
Client

↓

JWT

↓

API Gateway

↓

Service A

↓

Service B

↓

Service C
```

Each service independently validates the incoming JWT before processing requests.

---

# Enterprise Example

A multinational retail company provides a customer portal.

```
Customer

↓

Login

↓

Identity Provider

↓

JWT

↓

API Gateway

↓

Order Service

↓

Inventory Service

↓

Payment Service
```

Each backend service validates the JWT before providing access to protected resources.

---

# Advantages of JWT

```
Advantages

│

├── Stateless

├── Compact

├── Digitally Signed

├── Cross-Platform

├── Distributed Systems

├── Easy API Integration

└── Cloud Friendly
```

---

# Limitations

JWTs also introduce operational considerations.

```
Challenges

│

├── Token Revocation

├── Secure Storage

├── Short Lifetime Management

├── Signature Validation

├── Key Rotation

└── Claim Design
```

Proper implementation is essential to maintaining security.

---

# Hands-on Lab (Conceptual)

1. Draw the structure of a JWT.
2. Identify the purpose of each JWT section.
3. Compare JWS and JWE.
4. Map JWT usage within an OAuth authentication flow.
5. Design a conceptual microservice architecture using JWT-based authentication.

> Perform all activities only in environments where you have explicit authorization. Focus on architecture, identity, and secure design concepts.

---

# Interview Questions

1. What is a JWT?
2. What are the three parts of a JWT?
3. What is the purpose of the JWT signature?
4. What are registered claims?
5. What is the difference between JWS and JWE?
6. How is JWT used in OAuth?
7. How is JWT used in OpenID Connect?
8. Why is JWT considered stateless?
9. Why should applications validate JWTs?
10. What are the advantages of JWT in distributed systems?

---

# Best Practices

- Validate every JWT before trusting its contents.
- Use signed tokens to protect integrity.
- Use encrypted tokens when claim confidentiality is required.
- Include only necessary claims.
- Use short-lived tokens where appropriate.
- Centralize identity management through trusted Identity Providers.
- Review claim design regularly to avoid unnecessary exposure.

---

# Common Mistakes

- Trusting a JWT without validation.
- Assuming Base64URL encoding provides encryption.
- Including excessive sensitive information in claims.
- Confusing JWS with JWE.
- Treating JWTs as permanent credentials.
- Ignoring key management and token lifecycle planning.

---

# Key Takeaways

- JWT is a compact standard for securely transmitting claims.
- A JWT consists of a Header, Payload, and Signature.
- JWS provides integrity, while JWE provides confidentiality.
- JWTs are widely used in OAuth 2.0 and OpenID Connect.
- Secure validation, careful claim design, and proper lifecycle management are essential for enterprise JWT security.

# 34-JWT-Security.md

# Part 2 — JWT Validation, Digital Signatures, Key Management, Token Lifecycle, Claims Validation, and Secure JWT Handling

> **"A JWT is trusted only after successful validation. Every Resource Server must independently verify the token's integrity, issuer, audience, lifetime, and authorization information before granting access."**

---

# Learning Objectives

After completing this part, you will understand:

- JWT Validation
- Digital Signatures
- Signing Algorithms
- Key Management
- Claims Validation
- Token Lifecycle
- Token Expiration
- Key Rotation
- Secure JWT Storage
- Enterprise JWT Architecture

---

# JWT Validation

Receiving a JWT does **not** automatically mean it is trustworthy.

Every protected service should validate the token before processing requests.

```
Incoming JWT

↓

Validation

↓

Valid?

↓

Yes

↓

Access Decision

↓

No

↓

Reject
```

---

# Why Validation is Required

A JWT is merely a structured token.

Its contents should only be trusted after successful verification.

```
Client

↓

JWT

↓

Validation

↓

Trusted Identity
```

Skipping validation defeats the security provided by signed tokens.

---

# Validation Workflow

```
Incoming JWT

↓

Decode

↓

Verify Signature

↓

Validate Claims

↓

Evaluate Authorization

↓

Process Request
```

Each step contributes to secure authentication and authorization.

---

# Signature Validation

The signature ensures the JWT has not been modified.

```
Header

+

Payload

↓

Signature Verification

↓

Valid Signature?

↓

Trusted Token
```

If verification fails, the token must be rejected.

---

# Why Signatures Matter

```
Original JWT

↓

Digital Signature

↓

Transmission

↓

Verification

↓

Integrity Confirmed
```

Digital signatures help ensure that token contents remain unchanged.

---

# Common Signing Algorithms

```
Signing Algorithms

│

├── HS256

├── HS384

├── HS512

├── RS256

├── RS384

├── RS512

├── ES256

└── ES512
```

Organizations choose algorithms based on their security architecture and operational requirements.

---

# Symmetric vs Asymmetric Signing

| Symmetric | Asymmetric |
|------------|------------|
| Shared Secret | Public/Private Key Pair |
| Same Key Signs & Verifies | Private Key Signs |
| Shared Trust | Public Key Verification |
| Simpler Deployment | Better for Distributed Systems |

---

# HS256 Overview

HS256 uses a shared secret.

```
Application

↓

Shared Secret

↓

Token Signing

↓

Validation
```

The same secret is used for signing and verification.

---

# RS256 Overview

RS256 uses asymmetric cryptography.

```
Private Key

↓

Sign JWT

↓

Public Key

↓

Verify JWT
```

Only the private key signs tokens.

Public keys verify signatures.

---

# Enterprise Preference

Many enterprise environments prefer asymmetric signing.

```
Identity Provider

↓

Private Key

↓

JWT

↓

API Gateway

↓

Public Key

↓

Validation
```

This allows multiple services to validate tokens without sharing signing secrets.

---

# Public Key Distribution

Applications require access to trusted public keys.

```
Identity Provider

↓

Public Keys

↓

Resource Servers

↓

JWT Validation
```

Organizations should maintain secure key distribution mechanisms.

---

# Key Management

Cryptographic keys require careful lifecycle management.

```
Keys

│

├── Generation

├── Storage

├── Distribution

├── Rotation

├── Backup

└── Retirement
```

Key management is as important as algorithm selection.

---

# Secure Key Storage

Private signing keys should remain protected.

```
Private Key

↓

Secure Storage

↓

Signing Service
```

Access should be limited to authorized systems and administrators.

---

# Key Rotation

Keys should be replaced periodically according to organizational policy.

```
Old Key

↓

Rotation

↓

New Key

↓

JWT Signing
```

Regular rotation limits long-term exposure if a key is compromised.

---

# Claims Validation

Applications should validate important JWT claims.

```
JWT

↓

Claims Validation

↓

Identity

↓

Authorization
```

Claims provide context for authentication and authorization decisions.

---

# Registered Claim Validation

| Claim | Validation Purpose |
|--------|--------------------|
| iss | Verify trusted issuer |
| sub | Identify subject |
| aud | Confirm intended audience |
| exp | Ensure token has not expired |
| nbf | Ensure token is valid for current time |
| iat | Verify issuance timing |
| jti | Support token identification |

---

# Issuer Validation

```
JWT

↓

Issuer

↓

Trusted Identity Provider?

↓

Yes

↓

Continue
```

Only tokens from trusted issuers should be accepted.

---

# Audience Validation

```
JWT

↓

Audience

↓

Intended Application?

↓

Yes

↓

Continue
```

A token issued for one service should not automatically be accepted by another.

---

# Expiration Validation

```
JWT

↓

Expiration Time

↓

Expired?

↓

Yes

↓

Reject

↓

No

↓

Continue
```

Expired tokens should never be accepted.

---

# Not Before Validation

```
JWT

↓

Not Before

↓

Current Time

↓

Valid Yet?

↓

Yes

↓

Continue
```

This prevents use before the intended validity period.

---

# JWT Identifier (jti)

The JWT Identifier uniquely identifies a token.

```
JWT

↓

jti

↓

Unique Identifier
```

Organizations may use this claim to support auditing or token management workflows.

---

# Authorization Using Claims

Claims can support authorization decisions.

```
JWT

↓

Scopes

↓

Roles

↓

Permissions

↓

Access Decision
```

Authorization should still be enforced within application business logic.

---

# Token Lifetime

Short-lived tokens reduce exposure.

```
Authentication

↓

JWT Issued

↓

Valid

↓

Expiration

↓

Reauthentication or Refresh
```

Appropriate token lifetime depends on business and security requirements.

---

# Token Revocation

Some environments require the ability to revoke tokens before expiration.

```
Security Event

↓

Revocation

↓

Resource Server

↓

Access Denied
```

Revocation strategies vary depending on architecture and operational needs.

---

# Secure JWT Storage

Applications should protect JWTs appropriately.

```
Client

↓

Secure Storage

↓

JWT
```

Storage approaches depend on the client platform and application architecture.

---

# Transport Security

JWTs should be transmitted only over encrypted channels.

```
Client

↓

HTTPS

↓

JWT

↓

Server
```

TLS protects tokens during transmission.

---

# Enterprise JWT Validation Flow

```
Client

↓

JWT

↓

API Gateway

↓

Signature Validation

↓

Claims Validation

↓

Authorization

↓

Business Service
```

Every protected request should undergo validation before processing.

---

# Enterprise Example

A multinational insurance company secures internal APIs with JWTs.

```
Employee Portal

↓

Identity Provider

↓

JWT

↓

API Gateway

↓

Claims Validation

↓

Policy Service

↓

Claims Database
```

Every API independently validates signatures and claims before processing business requests.

---

# Common Enterprise Challenges

| Challenge | Recommended Approach |
|-----------|----------------------|
| Weak key protection | Secure key management |
| Long-lived tokens | Short token lifetimes |
| Multiple services | Centralized Identity Provider |
| Signature verification | Standardized validation libraries |
| Key rotation | Automated rotation policies |
| Token misuse | Strong claim validation |

---

# Hands-on Lab (Conceptual)

1. Draw a complete JWT validation workflow.
2. Compare symmetric and asymmetric JWT signing.
3. Design a secure key rotation process.
4. Identify which registered claims should be validated.
5. Create an enterprise JWT architecture with centralized identity services.

> Perform all activities only in environments where you have explicit authorization. Focus on defensive architecture, validation, and secure identity engineering.

---

# Interview Questions

1. Why should every JWT be validated?
2. What is the purpose of a digital signature?
3. What is the difference between HS256 and RS256?
4. Why is issuer validation important?
5. What is audience validation?
6. Why should expired JWTs be rejected?
7. What is the purpose of the `jti` claim?
8. Why is key rotation important?
9. Why do enterprises often prefer asymmetric signing?
10. Why should JWTs only be transmitted over HTTPS?

---

# Best Practices

- Validate signatures before trusting JWT contents.
- Verify issuer, audience, expiration, and other relevant claims.
- Use short-lived JWTs where appropriate.
- Protect signing keys with secure key management.
- Rotate signing keys periodically.
- Transmit JWTs only over HTTPS.
- Use centralized identity services for consistent validation.
- Apply authorization checks in addition to token validation.

---

# Common Mistakes

- Trusting decoded JWT contents without verification.
- Skipping issuer or audience validation.
- Using long-lived tokens unnecessarily.
- Storing signing keys insecurely.
- Accepting expired tokens.
- Assuming JWT validation alone replaces application authorization.

---

# Key Takeaways

- JWT validation is mandatory before trusting any token.
- Digital signatures protect token integrity.
- Claims such as issuer, audience, and expiration provide essential validation context.
- Strong key management and periodic rotation strengthen JWT security.
- Secure transport, proper validation, and layered authorization are fundamental to enterprise JWT deployments.

```text id="rrks28"
**Next:** Part 3
```