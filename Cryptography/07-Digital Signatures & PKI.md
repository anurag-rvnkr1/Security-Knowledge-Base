# Chapter 07 – Digital Signatures & PKI

## Overview

A **digital signature** is a cryptographic mechanism used to provide:

- Authentication
- Integrity
- Proof of possession of a private key
- Publicly verifiable authenticity

Digital signatures use an asymmetric key pair:

```text
Private Key
    │
    │ Signing
    ▼
Digital Signature

Public Key
    │
    │ Verification
    ▼
Valid / Invalid
```

Unlike a MAC, a digital signature does not require the verifier to possess the signing secret.

Digital signatures are fundamental to:

```text
TLS Certificates
PKI
Software Signing
Code Signing
Secure Email
Document Signing
SSH
Package Verification
Identity Systems
Certificate Authorities
Supply Chain Security
```

Important signature algorithms include:

```text
RSA-PSS
ECDSA
Ed25519
```

---

# 1. What is a Digital Signature?

A digital signature is a cryptographic value generated using:

```text
Message
+
Private Key
```

The corresponding public key can be used to verify the signature.

Conceptually:

```text
                  Message
                     │
                     ▼
                   Hash
                     │
                     ▼
              Signing Algorithm
                     │
                Private Key
                     │
                     ▼
                Signature
```

Verification:

```text
Message
   │
   ▼
 Hash
   │
   +
Signature
   +
Public Key
   │
   ▼
Valid / Invalid
```

---

# 2. What Does a Digital Signature Provide?

A correctly implemented digital signature can provide:

```text
Integrity
+
Authentication
+
Proof of Private-Key Possession
```

If a signature verifies under a trusted public key, the verifier has cryptographic evidence that the signer controlling the corresponding private key authorized the signed data.

---

# 3. Digital Signature vs MAC

Both provide integrity and authentication, but their trust models differ.

### MAC

```text
Shared Secret
```

Both sender and receiver know the same secret.

### Digital Signature

```text
Private Key → Sign
Public Key  → Verify
```

Only the signer should possess the private key.

---

# 4. Comparison

| Property | MAC | Digital Signature |
|---|---|---|
| Secret | Shared key | Private key |
| Verification key | Same secret | Public key |
| Public verification | No | Yes |
| Private signing key | No | Yes |
| Typical performance | Fast | Generally slower |
| Non-repudiation support | No | Can support it |
| Examples | HMAC | RSA-PSS, ECDSA, Ed25519 |

---

# 5. Digital Signature Does Not Mean Encryption

A digital signature does not hide the message.

```text
Message
   +
Private Key
   ↓
Signature
```

Anyone with the public key can verify it.

For confidentiality:

```text
Encryption
```

is required.

---

# 6. Signing Process

A simplified signing process:

```text
Message
   ↓
Hash
   ↓
Signature Scheme
   +
Private Key
   ↓
Digital Signature
```

The message itself is often not directly processed by the expensive public-key operation.

Instead, a cryptographic hash is incorporated into the signature scheme.

---

# 7. Verification Process

The verifier has:

```text
Message
Signature
Public Key
```

The verifier checks:

```text
Signature
+
Public Key
+
Message
```

If the cryptographic verification succeeds:

```text
Signature = Valid
```

Otherwise:

```text
Signature = Invalid
```

---

# 8. What a Valid Signature Means

A valid signature generally means:

```text
The signature matches the supplied data
under the supplied public key
according to the signature algorithm.
```

It does **not automatically mean**:

```text
The public key belongs to the person you think it belongs to.
```

That requires a trust mechanism such as:

```text
PKI
Certificate
Trusted Key Distribution
Application Trust Store
```

---

# 9. Trust Is Separate From Verification

This is a critical concept.

Cryptographic verification:

```text
Signature
+
Public Key
+
Message
   ↓
Valid
```

Identity verification:

```text
Public Key
   ↓
Who owns this key?
```

PKI helps answer the second question.

---

# 10. Public-Key Infrastructure

**PKI** stands for:

```text
Public-Key Infrastructure
```

PKI is a system of:

```text
People
Processes
Policies
Keys
Certificates
Certificate Authorities
Trust Stores
Validation Mechanisms
Revocation Systems
```

used to manage digital identities and public keys.

---

# 11. PKI Architecture

A simplified PKI hierarchy:

```text
                    Root CA
                       │
                       ▼
               Intermediate CA
                       │
                       ▼
              End-Entity Certificate
                       │
                       ▼
                    Server
```

For example:

```text
Root CA
   ↓
Intermediate CA
   ↓
example.com Certificate
   ↓
Web Server
```

---

# 12. Certificate

A digital certificate binds:

```text
Identity
+
Public Key
```

using a trusted digital signature.

Conceptually:

```text
Identity
   +
Public Key
   +
Certificate Information
   ↓
CA Signature
   ↓
Certificate
```

---

# 13. X.509 Certificates

**X.509** is the widely used certificate standard used in many PKI systems.

X.509 certificates contain information such as:

```text
Subject
Issuer
Public Key
Validity Period
Serial Number
Signature Algorithm
Extensions
CA Signature
```

---

# 14. Certificate Example

A simplified certificate:

```text
Subject:
example.com

Issuer:
Example Intermediate CA

Public Key:
ECDSA P-256

Validity:
Start → End

Serial Number:
123456

Signature:
CA Signature
```

The actual certificate contains many additional fields and extensions.

---

# 15. Subject

The subject identifies the entity represented by the certificate.

Historically, this could contain:

```text
Common Name
Organization
Country
Organizational Unit
```

For modern TLS hostname validation, the **Subject Alternative Name (SAN)** extension is the important field.

---

# 16. Subject Alternative Name

SAN can contain identities such as:

```text
DNS Names
IP Addresses
Email Addresses
URIs
```

For example:

```text
DNS:
example.com
www.example.com
api.example.com
```

Modern TLS clients validate hostnames against SAN entries rather than relying solely on the legacy Common Name field.

---

# 17. Issuer

The issuer identifies the CA that signed the certificate.

Example:

```text
Subject:
api.example.com

Issuer:
Example Intermediate CA
```

This creates part of the certificate chain.

---

# 18. Certificate Serial Number

Each certificate generally has a serial number assigned by its issuer.

It helps identify a particular certificate.

Conceptually:

```text
Certificate
   +
Serial Number
   ↓
Unique Certificate Identifier
```

Serial numbers are important for certificate management and revocation.

---

# 19. Validity Period

Certificates contain:

```text
Not Before
Not After
```

Example:

```text
Not Before:
2026-01-01

Not After:
2027-01-01
```

A certificate outside its validity period should generally not be accepted for normal certificate validation.

---

# 20. Public Key Information

The certificate contains the subject's public key.

Examples:

```text
RSA
ECDSA
Ed25519
```

The public key is used according to the certificate's intended key usage and the protocol.

---

# 21. Certificate Signature

The certificate issuer signs certificate data.

Conceptually:

```text
Certificate Data
      ↓
Hash / Signature Processing
      ↓
CA Private Key
      ↓
Certificate Signature
```

The verifier uses:

```text
CA Public Key
```

to verify the certificate signature.

---

# 22. Certificate Chain

A certificate usually belongs to a chain.

Example:

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
```

The chain establishes:

```text
Server Public Key
       ↓
Intermediate CA
       ↓
Root CA
```

---

# 23. Root CA

A root CA is a trust anchor.

Its certificate is typically distributed through:

```text
Operating System Trust Store
Browser Trust Store
Enterprise Trust Store
Application Trust Store
```

The root certificate is normally self-signed.

---

# 24. Why Root CAs Are Trusted

A root CA is trusted because the relevant platform, organization, or application has explicitly included it in a trusted trust store.

Therefore:

```text
Root CA
=
Configured Trust Anchor
```

Trust ultimately depends on the security of that trust-store ecosystem.

---

# 25. Intermediate CA

Intermediate CAs are signed by a root CA or another authorized CA.

Example:

```text
Root CA
   ↓
Intermediate CA 1
   ↓
Intermediate CA 2
   ↓
Server Certificate
```

Intermediate CAs reduce the need to use the root private key for routine certificate issuance.

---

# 26. Why Use Intermediate CAs?

Using intermediate CAs provides:

```text
Root Key Protection
Delegated Issuance
Operational Separation
Limited Blast Radius
Easier Revocation
Policy Separation
```

The root CA can remain offline or highly protected.

---

# 27. Root CA vs Intermediate CA

| Property | Root CA | Intermediate CA |
|---|---|---|
| Trust role | Trust anchor | Delegated trust |
| Usually self-signed | Yes | No |
| Signed by | Itself | Parent CA |
| Operational exposure | Ideally low | Higher |
| Can issue certificates | Yes | Yes if authorized |
| Trust store | Commonly included | Usually validated through chain |

---

# 28. End-Entity Certificate

The final certificate in the chain is usually the certificate presented by the server, user, device, or application.

Example:

```text
Root CA
   ↓
Intermediate CA
   ↓
api.example.com
```

The `api.example.com` certificate is an end-entity certificate.

---

# 29. Certificate Path Validation

A client validates:

```text
End Certificate
       ↓
Issuer
       ↓
Intermediate
       ↓
Root
```

The client checks whether the chain leads to a trusted root and whether the certificates satisfy relevant constraints.

---

# 30. Certificate Validation

Important checks include:

```text
Signature
Issuer
Validity Period
SAN / Identity
Key Usage
Extended Key Usage
Basic Constraints
Certificate Policies
Chain Building
Trust Anchor
Revocation Status
Algorithm Security
```

Exact validation behavior depends on the protocol and implementation.

---

# 31. Hostname Validation

Suppose the server presents:

```text
Certificate:
example.com
```

The client connects to:

```text
api.example.com
```

If:

```text
api.example.com
```

is not covered by the certificate's SAN entries, hostname validation should fail.

---

# 32. Why Hostname Validation Matters

Without hostname validation:

```text
Attacker Certificate
       ↓
Trusted CA
       ↓
Victim Client
```

could potentially be accepted for the wrong host if other validation checks pass.

Hostname verification binds the certificate to the intended service identity.

---

# 33. Certificate Authority Validation

A client should verify that:

```text
Certificate
```

was signed by:

```text
Trusted CA
```

through a valid chain.

An arbitrary self-signed certificate should not automatically be trusted.

---

# 34. Self-Signed Certificate

A self-signed certificate is signed by its own private key.

Conceptually:

```text
Certificate
    ↓
Signed by itself
```

Self-signed certificates can be legitimate in:

```text
Internal Systems
Development
Testing
Private PKI
```

but they must be explicitly trusted by clients.

---

# 35. Self-Signed Certificate vs Invalid Certificate

A self-signed certificate is not inherently "broken."

The key question is:

```text
Is this certificate trusted for this environment?
```

For example:

```text
Internal Enterprise CA
       ↓
Explicitly Trusted
       ↓
Valid Internal Certificate
```

---

# 36. Certificate Signing Request

A **CSR** stands for:

```text
Certificate Signing Request
```

It is generated by the entity requesting a certificate.

Conceptually:

```text
Private Key
   │
   ▼
Public Key
   │
   +
Requested Identity
   ↓
CSR
   ↓
Certificate Authority
```

---

# 37. CSR Contents

A CSR commonly contains:

```text
Public Key
Subject Information
Requested Extensions
Signature
```

The requester signs the CSR using the corresponding private key.

---

# 38. CSR Does Not Contain the Private Key

A properly generated CSR contains:

```text
Public Key
```

and a proof of possession using the corresponding private key.

It should not contain:

```text
Private Key
```

The private key must remain under the control of the requester.

---

# 39. Generate a CSR

Example with OpenSSL:

```bash
openssl req \
    -new \
    -key server.key \
    -out server.csr
```

The CA can then process the CSR according to its issuance policy.

---

# 40. Inspect a CSR

```bash
openssl req \
    -in server.csr \
    -text \
    -noout
```

Inspect:

```text
Subject
Public Key
Requested Extensions
Signature
```

---

# 41. Certificate Authority Workflow

A simplified issuance workflow:

```text
Administrator
     │
     ▼
Generate Private Key
     │
     ▼
Generate CSR
     │
     ▼
Submit to CA
     │
     ▼
Identity Validation
     │
     ▼
Certificate Issued
     │
     ▼
Install Certificate
```

The validation process depends on the certificate type and CA policy.

---

# 42. Domain Validation

A CA may verify control of a domain through mechanisms such as:

```text
DNS
HTTP
Email
```

The exact validation method depends on the certificate issuance process.

---

# 43. Organization Validation

Some certificates involve additional organization validation.

The CA may verify information about the requesting organization.

The certificate can then communicate more identity information than a simple domain-control validation process.

---

# 44. Extended Validation

Extended Validation (EV) certificates involve additional organizational validation requirements.

Modern browser UI generally does not display EV certificates with the prominent visual treatment historically associated with them.

The underlying PKI validation remains based on certificate and CA processes.

---

# 45. Certificate Revocation

A certificate may need to be revoked before its expiration date.

Reasons include:

```text
Private Key Compromise
Mis-issuance
Domain Ownership Change
Certificate Misconfiguration
CA Policy Violation
Organizational Changes
```

---

# 46. Certificate Revocation List

A **CRL** is a:

```text
Certificate Revocation List
```

It contains certificates that have been revoked by an issuer.

Conceptually:

```text
CA
 ↓
CRL
 ↓
Revoked Certificate Serial Numbers
```

---

# 47. CRL Distribution Point

A certificate can contain an extension identifying where revocation information can be obtained.

Example concept:

```text
CRL Distribution Point
        ↓
CRL
```

Clients may retrieve the CRL and check whether the certificate's serial number appears on it.

---

# 48. OCSP

**OCSP** stands for:

```text
Online Certificate Status Protocol
```

It allows a client or intermediary to query certificate status.

Conceptually:

```text
Client
  ↓
OCSP Request
  ↓
OCSP Responder
  ↓
Good / Revoked / Unknown
```

---

# 49. OCSP Stapling

With OCSP stapling:

```text
Server
   ↓
Obtains OCSP Response
   ↓
Sends it during TLS connection
   ↓
Client
```

The client does not necessarily need to directly contact the CA's OCSP responder.

This can improve privacy and reduce client-side latency.

---

# 50. CRL vs OCSP

| Feature | CRL | OCSP |
|---|---|---|
| Model | Download list | Query status |
| Size | Can become large | Usually smaller response |
| Freshness | Depends on CRL update | Query-based |
| Network | Periodic retrieval | Online query |
| Privacy | Less query-specific | Can reveal certificate checks |
| Example | Revocation list | Certificate status response |

---

# 51. Certificate Transparency

**Certificate Transparency (CT)** is a system designed to make publicly trusted certificate issuance auditable.

Public TLS certificates are logged in:

```text
Certificate Transparency Logs
```

This allows domain owners and security researchers to detect unexpected certificate issuance.

---

# 52. Certificate Transparency Workflow

Conceptually:

```text
CA Issues Certificate
       ↓
Certificate Logged
       ↓
CT Log
       ↓
Public Monitoring
       ↓
Unexpected Certificate Detection
```

---

# 53. Certificate Transparency Security Value

CT helps detect:

```text
Misissued Certificates
Unauthorized Certificates
CA Abuse
Compromised CA Processes
Unexpected Domain Certificates
```

It does not prevent issuance by itself.

It improves:

```text
Visibility
Accountability
Detection
```

---

# 54. Certificate Pinning

Certificate or public-key pinning historically attempted to restrict which certificates or keys an application accepts.

However:

```text
Browser HPKP
```

is deprecated.

Modern applications should follow current platform and protocol guidance rather than implementing obsolete browser pinning mechanisms.

---

# 55. TLS Certificate

A TLS server generally presents:

```text
Server Certificate
+
Certificate Chain
```

during the TLS handshake.

The client validates the certificate before trusting the server identity.

---

# 56. TLS Authentication

Simplified:

```text
Client
   │
   │ TLS Connection
   ▼
Server
   │
   │ Certificate
   ▼
Client
   │
   │ Validate Certificate
   ▼
Trusted / Rejected
```

After authentication, the protocol establishes session keys for encrypted communication.

---

# 57. Certificate Authentication Is Not Encryption

A certificate primarily provides:

```text
Identity
+
Public Key
```

TLS then uses cryptographic protocols to establish:

```text
Session Keys
```

which protect application data.

---

# 58. Mutual TLS

In normal TLS:

```text
Client → Server Authentication
```

In mutual TLS:

```text
Client ↔ Server Authentication
```

Both sides present certificates.

Conceptually:

```text
Client Certificate
       ↕
     mTLS
       ↕
Server Certificate
```

---

# 59. mTLS Use Cases

mTLS is commonly used for:

```text
Microservices
Service Meshes
Enterprise APIs
Device Authentication
Zero Trust Systems
Financial Systems
Internal Services
```

---

# 60. Code Signing

Digital signatures can authenticate software.

Conceptually:

```text
Software
   ↓
Hash
   ↓
Private Signing Key
   ↓
Signature
```

The recipient verifies:

```text
Software
+
Signature
+
Trusted Public Key
```

---

# 61. Code Signing Benefits

Code signing can help verify:

```text
Publisher Identity
Artifact Integrity
Software Authenticity
Update Authenticity
```

It is an important component of software supply-chain security.

---

# 62. Software Update Security

A secure update system can use:

```text
Software Update
      ↓
Signature Verification
      ↓
Trusted Publisher Key
      ↓
Install
```

If verification fails:

```text
Reject Update
```

---

# 63. Supply Chain Attack

An attacker may compromise:

```text
Build System
Package Registry
Developer Account
Signing Key
Release Pipeline
```

and attempt to distribute malicious software.

Digital signatures help only if:

```text
Signing Key
+
Build Process
+
Trust Model
```

are protected.

---

# 64. Signing Key Compromise

If an attacker obtains a legitimate software signing private key:

```text
Attacker
   ↓
Stolen Private Key
   ↓
Signs Malicious Software
   ↓
Signature May Verify
```

Therefore code-signing keys require strong protection.

---

# 65. Hardware Security Modules

An **HSM** can protect sensitive private keys.

Conceptually:

```text
Application
    │
    │ Sign Request
    ▼
   HSM
    │
    │ Private Key
    │ stays inside HSM
    ▼
Signature
```

The application does not necessarily receive the private key itself.

---

# 66. Cloud Key Management

Cloud environments commonly provide:

```text
KMS
HSM-backed Keys
Key Rotation
Access Policies
Audit Logging
```

These services can help protect signing and encryption keys.

---

# 67. Private Key Protection

Private keys should be protected against:

```text
Unauthorized Access
Theft
Memory Exposure
Filesystem Access
Backup Leakage
Source-Control Exposure
Credential Dumping
Insider Threats
```

Possible protections:

```text
HSM
TPM
Secure Enclave
KMS
Encrypted Key Store
Strict File Permissions
```

---

# 68. Key Lifecycle

A signing key has a lifecycle:

```text
Generate
   ↓
Provision
   ↓
Activate
   ↓
Use
   ↓
Rotate
   ↓
Revoke
   ↓
Archive / Destroy
```

Lifecycle management is a critical part of PKI security.

---

# 69. Certificate Lifecycle

A certificate lifecycle:

```text
Generate Key
     ↓
Create CSR
     ↓
Request Certificate
     ↓
Validate Identity
     ↓
Issue Certificate
     ↓
Deploy
     ↓
Monitor Expiration
     ↓
Renew
     ↓
Revoke if Required
```

---

# 70. Certificate Expiration

Expired certificates can cause:

```text
TLS Failures
Application Outages
API Failures
Authentication Errors
Monitoring Alerts
```

Therefore organizations should monitor:

```text
Certificate Expiration Dates
```

automatically.

---

# 71. Certificate Automation

Modern environments often automate:

```text
Certificate Request
Certificate Validation
Certificate Issuance
Certificate Deployment
Certificate Renewal
Certificate Revocation
```

Automation reduces:

```text
Manual Errors
Expired Certificates
Operational Overhead
```

---

# 72. PKI Trust Store

A trust store contains trusted certificates or trust anchors.

Examples include:

```text
Operating System Trust Store
Browser Trust Store
Enterprise Trust Store
Application Trust Store
Container Trust Store
```

If a CA is added to a trust store:

```text
Certificates issued by that CA
```

may become trusted according to the validation rules of the application.

---

# 73. Enterprise Private PKI

Organizations can operate their own PKI:

```text
Enterprise Root CA
       ↓
Intermediate CA
       ↓
Internal Services
```

This can support:

```text
mTLS
Internal Websites
Device Identity
Employee Certificates
Service Authentication
```

Clients must explicitly trust the organization's CA.

---

# 74. PKI and Zero Trust

PKI can support Zero Trust identity:

```text
Workload
   ↓
Certificate
   ↓
Identity
   ↓
Authentication
   ↓
Authorization
```

This can provide short-lived, cryptographically verifiable workload identities.

---

# 75. SPIFFE and Workload Identity

Modern workload identity systems may use standardized identity frameworks such as:

```text
SPIFFE
```

A workload receives an identity that can be used for authentication between services.

This is particularly relevant to:

```text
Microservices
Kubernetes
Service Meshes
Zero Trust
```

---

# 76. SSH Public-Key Authentication

SSH can authenticate users using public-key cryptography.

Client:

```text
Private Key
```

Server:

```text
Authorized Public Key
```

Conceptually:

```text
Client
  │
  │ Proof of Private-Key Possession
  ▼
SSH Server
  │
  │ Public Key Verification
  ▼
Authenticated
```

---

# 77. SSH Authorized Keys

A server may maintain:

```text
~/.ssh/authorized_keys
```

containing trusted public keys.

The server does not need the user's private key.

---

# 78. SSH Host Keys

SSH servers also have host keys.

These allow the client to recognize:

```text
This is the server I previously trusted.
```

Host-key verification helps defend against man-in-the-middle attacks.

---

# 79. SSH Known Hosts

Clients commonly maintain:

```text
~/.ssh/known_hosts
```

containing known server host keys.

If a server's key unexpectedly changes, SSH may warn the user.

Such warnings should be investigated rather than blindly bypassed.

---

# 80. Digital Signatures in Email

Cryptographic signatures can protect email authenticity and integrity.

Examples include:

```text
S/MIME
OpenPGP
```

Conceptually:

```text
Email
   ↓
Hash
   ↓
Private Signing Key
   ↓
Signature
```

The recipient uses the corresponding public key to verify the signature.

---

# 81. Non-Repudiation

Digital signatures are sometimes described as providing:

```text
Non-repudiation
```

However, this should not be treated as an automatic cryptographic guarantee.

Real-world non-repudiation depends on:

```text
Private-Key Control
Identity Binding
Certificate Management
Legal Framework
Audit Logs
Key Protection
Signing Policy
```

---

# 82. Signature Algorithms

Important modern signature algorithms include:

```text
RSA-PSS
ECDSA
Ed25519
```

They differ in:

```text
Mathematical Foundation
Key Size
Signature Size
Performance
Implementation Requirements
Protocol Support
```

---

# 83. RSA-PSS

RSA-PSS is a modern RSA signature scheme.

Conceptually:

```text
Message
   ↓
Hash
   ↓
PSS Encoding
   ↓
RSA Private-Key Operation
   ↓
Signature
```

Verification uses:

```text
RSA Public Key
```

---

# 84. Why RSA-PSS?

RSA-PSS provides randomized encoding and is preferred for modern RSA signature applications over older deterministic RSA signature constructions where applicable.

It should be implemented using a trusted cryptographic library.

---

# 85. ECDSA

**ECDSA** stands for:

```text
Elliptic Curve Digital Signature Algorithm
```

It provides:

```text
Signing
+
Verification
```

Conceptually:

```text
Message
   ↓
Hash
   ↓
ECDSA + Private Key
   ↓
Signature
```

---

# 86. ECDSA Nonce

ECDSA uses a per-signature nonce.

If the nonce is improperly:

```text
Reused
Predicted
Leaked
Generated with Weak Randomness
```

the private key may be recoverable.

This makes secure implementation extremely important.

---

# 87. Ed25519

Ed25519 is a modern elliptic-curve signature scheme.

It provides:

```text
Private Key → Signature
Public Key  → Verification
```

It is designed to provide strong security with compact keys and signatures.

---

# 88. Ed25519 vs ECDSA

| Property | Ed25519 | ECDSA |
|---|---|---|
| Type | Digital signature | Digital signature |
| Curve family | Edwards | Weierstrass |
| Nonce concerns | Designed to avoid common random-nonce failure modes through deterministic signing | Nonce generation is critical |
| Common use | SSH, modern systems | TLS, certificates, many existing systems |
| Signature size | Compact | Compact |

Actual protocol support varies.

---

# 89. Signature Algorithm Selection

Do not select algorithms only based on:

```text
"Which is strongest?"
```

Consider:

```text
Protocol Support
Library Support
Interoperability
Key Management
Performance
Security Requirements
Standards
Migration Requirements
```

---

# 90. Certificate Key Usage

Certificates can restrict how keys are used.

Examples:

```text
Digital Signature
Key Encipherment
Certificate Sign
CRL Sign
```

The `keyUsage` extension can constrain permitted operations.

---

# 91. Extended Key Usage

Extended Key Usage (EKU) provides more specific purposes.

Examples include:

```text
Server Authentication
Client Authentication
Code Signing
Email Protection
```

A certificate should not automatically be treated as valid for every possible purpose.

---

# 92. Basic Constraints

The `basicConstraints` extension helps identify whether a certificate is a CA certificate.

Conceptually:

```text
CA = TRUE
```

means the certificate may be authorized to act as a CA subject to other constraints.

An end-entity certificate generally has:

```text
CA = FALSE
```

---

# 93. Path Length Constraints

A CA certificate can include constraints limiting how many subordinate CA levels may appear beneath it.

Conceptually:

```text
Root
 ↓
Intermediate
 ↓
Intermediate
 ↓
Server
```

A path-length constraint can restrict such delegation.

---

# 94. Certificate Misconfiguration

Common PKI issues include:

```text
Expired Certificate
Wrong SAN
Weak Algorithm
Weak Key Size
Missing Intermediate
Incorrect EKU
Incorrect Key Usage
Untrusted CA
Broken Chain
Private Key Exposure
Misissued Certificate
```

---

# 95. VAPT Certificate Testing

A security tester can inspect:

```text
Certificate Chain
SAN
Issuer
Validity
Signature Algorithm
Public-Key Algorithm
Key Size
Key Usage
Extended Key Usage
Basic Constraints
Revocation Information
TLS Configuration
```

---

# 96. OpenSSL Certificate Inspection

Retrieve a TLS certificate:

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com
```

For a more readable certificate:

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com \
    </dev/null 2>/dev/null \
    | openssl x509 -text -noout
```

---

# 97. Check Certificate Dates

```bash
openssl x509 \
    -in certificate.pem \
    -noout \
    -dates
```

Output includes:

```text
notBefore
notAfter
```

---

# 98. Check Certificate Subject

```bash
openssl x509 \
    -in certificate.pem \
    -noout \
    -subject
```

---

# 99. Check Certificate Issuer

```bash
openssl x509 \
    -in certificate.pem \
    -noout \
    -issuer
```

---

# 100. Check SAN

```bash
openssl x509 \
    -in certificate.pem \
    -noout \
    -ext subjectAltName
```

---

# 101. Check Public Key

```bash
openssl x509 \
    -in certificate.pem \
    -noout \
    -pubkey
```

---

# 102. Check Signature Algorithm

```bash
openssl x509 \
    -in certificate.pem \
    -text \
    -noout
```

Look for:

```text
Signature Algorithm
```

and:

```text
Public Key Algorithm
```

---

# 103. Verify Certificate Chain

If you have:

```text
server.pem
intermediate.pem
root.pem
```

you can use OpenSSL verification tools to validate the chain.

Example:

```bash
openssl verify \
    -CAfile root.pem \
    -untrusted intermediate.pem \
    server.pem
```

Expected result:

```text
server.pem: OK
```

if the supplied chain and trust relationship are valid.

---

# 104. Generate an RSA Private Key

```bash
openssl genpkey \
    -algorithm RSA \
    -pkeyopt rsa_keygen_bits:2048 \
    -out private.key
```

---

# 105. Generate a CSR

```bash
openssl req \
    -new \
    -key private.key \
    -out server.csr
```

For production certificates, requested SANs and other fields should be specified according to the CA's requirements.

---

# 106. Generate an EC Key

```bash
openssl genpkey \
    -algorithm EC \
    -pkeyopt ec_paramgen_curve:P-256 \
    -out ec-private.key
```

Generate CSR:

```bash
openssl req \
    -new \
    -key ec-private.key \
    -out ec-server.csr
```

---

# 107. Digital Signature with Python

Using the `cryptography` library:

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()

message = b"Important message"

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

public_key.verify(
    signature,
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH,
    ),
    hashes.SHA256(),
)

print("Signature valid")
```

---

# 108. Signature Tampering Exercise

Generate a signature for:

```text
Hello
```

Then attempt verification against:

```text
hello
```

Expected:

```text
Original → Valid
Modified → Invalid
```

Even a one-character change should cause verification failure.

---

# 109. Certificate Inspection Lab

Choose a public HTTPS service.

Inspect:

```text
Subject
Issuer
SAN
Validity
Public Key
Signature Algorithm
Key Usage
Extended Key Usage
Certificate Chain
```

Document:

```text
Leaf Certificate
Intermediate CA
Root CA
```

---

# 110. PKI Attack Surface

Important attack categories include:

```text
Private-Key Theft
CA Compromise
Certificate Mis-issuance
Weak Algorithms
Expired Certificates
Broken Validation
Trust-Store Abuse
MITM
DNS Compromise
ACME Account Compromise
Certificate Renewal Abuse
Signing-Key Compromise
```

---

# 111. Private-Key Theft

If a server's private key is stolen:

```text
Attacker
   ↓
Private Key
   ↓
Potential Impersonation
```

Depending on the protocol and key usage, the attacker may also gain other capabilities.

Incident response should include:

```text
Key Rotation
Certificate Revocation
New Certificate
Compromise Investigation
```

---

# 112. CA Compromise

A compromised CA can potentially issue fraudulent certificates for domains it is authorized to validate.

Conceptually:

```text
Compromised CA
      ↓
Fraudulent Certificate
      ↓
Trusted Client
      ↓
Potential MITM
```

Certificate Transparency and monitoring can help detect unexpected public certificates.

---

# 113. Trust Store Abuse

If an attacker can install a malicious root CA into a device's trust store:

```text
Attacker Root CA
      ↓
Trusted by Device
      ↓
Fraudulent Certificates
      ↓
Potential TLS Interception
```

Therefore root CA installation should be tightly controlled.

---

# 114. Certificate Mis-Issuance

A CA may accidentally or maliciously issue a certificate for:

```text
example.com
```

to an unauthorized party.

Monitoring CT logs can help domain owners detect such events.

---

# 115. Certificate Transparency Monitoring

Organizations can monitor:

```text
Certificate Transparency Logs
```

for:

```text
Unexpected Domains
Unexpected Subdomains
Unknown CAs
Unexpected Certificate Changes
```

This can be integrated into security monitoring.

---

# 116. PKI Incident Response

If a fraudulent certificate is discovered:

```text
1. Confirm certificate details.
2. Identify issuer.
3. Determine whether issuance was authorized.
4. Identify affected domains.
5. Check CT logs.
6. Contact relevant CA if necessary.
7. Revoke affected certificate.
8. Replace certificates if required.
9. Investigate private-key compromise.
10. Monitor for additional suspicious certificates.
```

---

# 117. Code-Signing Incident Response

If a code-signing key is compromised:

```text
1. Stop use of compromised key.
2. Revoke certificate if applicable.
3. Generate new signing key.
4. Secure new key.
5. Re-sign trusted releases.
6. Review signed artifacts.
7. Investigate unauthorized signatures.
8. Notify affected parties.
9. Update trust mechanisms.
```

---

# 118. PKI and DevSecOps

Modern DevSecOps environments should automate:

```text
Certificate Issuance
Certificate Renewal
Key Rotation
Secret Management
Code Signing
Artifact Verification
Certificate Monitoring
```

Security controls should be integrated into:

```text
CI/CD
Infrastructure as Code
Container Registries
Kubernetes
Cloud KMS
```

---

# 119. PKI in Kubernetes

Kubernetes environments commonly use certificates for:

```text
API Server
Kubelet
Cluster Components
Admission Webhooks
mTLS
Service Meshes
Workload Identity
```

Certificates may be automatically rotated depending on the component and configuration.

---

# 120. Kubernetes Certificate Security

Important controls include:

```text
Protect Private Keys
Use Short-Lived Certificates Where Appropriate
Automate Rotation
Monitor Expiration
Restrict Certificate Authorities
Audit Certificate Issuance
Use Least Privilege
```

---

# 121. Service Mesh and PKI

Service meshes such as:

```text
Istio
Linkerd
```

can use certificates to establish workload identities and mutual TLS.

Conceptually:

```text
Service A
   │
   │ mTLS
   ▼
Service B
```

Both services authenticate cryptographically.

---

# 122. Certificate Automation

A mature PKI system should provide:

```text
Automatic Issuance
Automatic Renewal
Automatic Rotation
Expiration Monitoring
Revocation
Audit Logging
```

This reduces manual certificate management errors.

---

# 123. Certificate Expiration Monitoring

A monitoring system can alert:

```text
90 days before expiration
30 days before expiration
7 days before expiration
1 day before expiration
```

The exact thresholds should match organizational requirements.

---

# 124. Key Rotation vs Certificate Renewal

These are related but different.

### Certificate Renewal

```text
New Certificate
```

may use:

```text
Same Key
```

depending on policy.

### Key Rotation

```text
New Private Key
+
New Public Key
```

is generated.

Strong security practices often combine renewal with appropriate key rotation.

---

# 125. Cryptographic Agility

PKI systems should support migration between algorithms.

For example:

```text
RSA
  ↓
ECC
  ↓
Post-Quantum / Hybrid
```

This requires:

```text
Algorithm Support
Certificate Profiles
Key Management
Library Support
Protocol Compatibility
Migration Planning
```

---

# 126. Post-Quantum Signatures

Quantum computing threatens many classical public-key signature algorithms.

Potentially affected:

```text
RSA
ECDSA
Ed25519
```

Post-quantum signature algorithms such as:

```text
ML-DSA
SLH-DSA
```

are designed to address this future threat.

Post-quantum cryptography is covered in Chapter 12.

---

# 127. Digital Signature Security Checklist

```text
☐ Use modern signature algorithms
☐ Protect private signing keys
☐ Use strong randomness where required
☐ Use deterministic signing where appropriate
☐ Validate signatures correctly
☐ Validate certificate chains
☐ Validate SAN
☐ Check certificate validity
☐ Check key usage
☐ Check extended key usage
☐ Monitor certificate expiration
☐ Monitor certificate transparency
☐ Rotate compromised keys
☐ Avoid deprecated algorithms
```

---

# 128. PKI Security Checklist

```text
☐ Protect root CA keys
☐ Use intermediate CAs
☐ Keep root CA exposure low
☐ Protect CA signing keys
☐ Maintain trusted root stores
☐ Monitor certificate issuance
☐ Automate certificate renewal
☐ Implement revocation processes
☐ Monitor CT logs
☐ Audit certificate issuance
☐ Enforce certificate policies
☐ Restrict CA privileges
☐ Maintain incident-response procedures
```

---

# 129. Common Mistakes

```text
❌ Trusting any certificate
❌ Disabling certificate validation
❌ Ignoring hostname validation
❌ Using expired certificates
❌ Exposing private keys
❌ Storing private keys in Git
❌ Using weak signature algorithms
❌ Reusing signing keys indefinitely
❌ Ignoring certificate revocation
❌ Installing unknown root CAs
❌ Treating certificate validity as proof of identity without checking trust
❌ Failing to monitor certificate issuance
❌ Signing malicious artifacts with legitimate keys
```

---

# 130. VAPT Checklist

During a PKI/TLS assessment:

```text
☐ Enumerate certificates
☐ Check certificate chains
☐ Check expiration
☐ Check SAN
☐ Check hostname validation
☐ Check signature algorithms
☐ Check public-key algorithms
☐ Check key sizes
☐ Check key usage
☐ Check EKU
☐ Check trust anchors
☐ Check revocation configuration
☐ Check private-key exposure
☐ Check certificate renewal
☐ Check mTLS configuration
☐ Check client certificate validation
☐ Check CT monitoring
```

---

# 131. SOC Monitoring

SOC teams can monitor:

```text
Certificate Issuance
Certificate Expiration
Certificate Replacement
Root CA Installation
Private-Key Access
Signing Events
Code-Signing Activity
TLS Errors
Certificate Validation Failures
OCSP Failures
Suspicious Certificates
```

---

# 132. Example SOC Alert

```text
Alert:
Unexpected certificate issued for:

api.company.example

Issuer:
Unknown / Unexpected CA

Observed:
2026-08-13 08:32 UTC
```

Investigation:

```text
1. Check CT logs.
2. Identify issuer.
3. Verify domain ownership.
4. Determine whether certificate is authorized.
5. Check deployment inventory.
6. Investigate potential account compromise.
7. Revoke if fraudulent.
```

---

# 133. Certificate Monitoring Architecture

```text
             Certificate Sources
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
       CT          TLS         PKI
      Logs       Scanners     Systems
        │           │           │
        └───────────┼───────────┘
                    ▼
              Monitoring
                    │
                    ▼
                   SIEM
                    │
                    ▼
                  Alert
```

---

# 134. Digital Signature in Software Supply Chain

A secure artifact pipeline:

```text
Source Code
    ↓
Build System
    ↓
Artifact
    ↓
Digest
    ↓
Signing Key
    ↓
Digital Signature
    ↓
Registry
    ↓
Deployment
    ↓
Signature Verification
```

This establishes a stronger chain of trust.

---

# 135. Signing Key Isolation

High-value signing keys should ideally be isolated from ordinary developer systems.

Possible architecture:

```text
CI/CD
  │
  │ Signing Request
  ▼
Signing Service
  │
  ▼
HSM / KMS
  │
  │ Private Key
  ▼
Signature
```

The private key remains protected.

---

# 136. Certificate Authority Security Model

A mature CA architecture may look like:

```text
                    Offline Root CA
                         │
                         ▼
                 Intermediate CA
                    /         \
                   /           \
                  ▼             ▼
          TLS Issuing CA    Code Signing CA
                │                │
                ▼                ▼
          Server Certs      Software Signatures
```

Separate CA roles can reduce blast radius.

---

# 137. CA Compromise Blast Radius

If a dedicated intermediate CA is compromised:

```text
Compromised Intermediate
        ↓
Affected Certificates
```

If a root CA is compromised:

```text
Compromised Root
        ↓
Potentially Broad Trust Impact
```

This is why root CA private keys require exceptional protection.

---

# 138. Certificate Policies

Organizations should define:

```text
Allowed Algorithms
Key Sizes
Certificate Lifetimes
Allowed SANs
Key Usage
EKU
Issuance Approval
Revocation Procedures
Renewal Procedures
Key Protection
Audit Requirements
```

---

# 139. PKI Governance

PKI is not purely a technical problem.

It involves:

```text
Security
Operations
Identity
Compliance
Governance
Risk Management
Incident Response
```

A certificate is only as trustworthy as the system that manages its identity and keys.

---

# 140. Practical Lab – Build a Small CA

For learning purposes, OpenSSL can be used to create a private test CA.

Generate a CA private key:

```bash
openssl genpkey \
    -algorithm RSA \
    -pkeyopt rsa_keygen_bits:4096 \
    -out ca.key
```

Create a self-signed test certificate:

```bash
openssl req \
    -x509 \
    -new \
    -key ca.key \
    -sha256 \
    -days 3650 \
    -out ca.crt
```

**Use this only for controlled labs or private PKI testing.**

---

# 141. Create a Server Key

```bash
openssl genpkey \
    -algorithm RSA \
    -pkeyopt rsa_keygen_bits:2048 \
    -out server.key
```

---

# 142. Create a Server CSR

```bash
openssl req \
    -new \
    -key server.key \
    -out server.csr
```

---

# 143. Sign a Test Certificate

For a controlled lab, the CA can sign the server CSR.

The resulting chain becomes:

```text
Test Root CA
      ↓
Server Certificate
```

The client must explicitly trust the test CA for the certificate to validate.

---

# 144. Verify the Certificate

```bash
openssl verify \
    -CAfile ca.crt \
    server.crt
```

Expected:

```text
server.crt: OK
```

if the certificate was correctly issued and the chain is valid.

---

# 145. Practical Lab – Signature Verification

Create:

```text
message.txt
```

Sign:

```bash
openssl dgst \
    -sha256 \
    -sign private.key \
    -out signature.bin \
    message.txt
```

Verify:

```bash
openssl dgst \
    -sha256 \
    -verify public.key \
    -signature signature.bin \
    message.txt
```

Then modify the file.

Verification should fail.

---

# 146. Practical Lab – Certificate Enumeration

For a public TLS service:

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com \
    -showcerts
```

Record:

```text
Leaf Certificate
Intermediate Certificate
Issuer
Subject
SAN
Validity
Public Key
Signature Algorithm
```

---

# 147. Real-World PKI Workflow

A production certificate lifecycle might look like:

```text
Service Deployment
       ↓
Private Key Generation
       ↓
CSR
       ↓
Identity Validation
       ↓
CA Issuance
       ↓
Certificate Deployment
       ↓
TLS
       ↓
Monitoring
       ↓
Renewal
       ↓
Rotation
```

---

# 148. Digital Signature Mental Model

Remember:

```text
Private Key
    ↓
SIGN

Public Key
    ↓
VERIFY
```

Never reverse the security roles.

The private key must remain secret.

The public key is designed for distribution.

---

# 149. PKI Mental Model

Remember:

```text
Private Key
      ↓
Public Key
      ↓
Certificate
      ↓
CA Signature
      ↓
Certificate Chain
      ↓
Trusted Root
```

This connects:

```text
Cryptographic Key
+
Identity
+
Trust
```

---

# 150. Hash + Signature + Certificate

These three concepts solve different problems:

```text
Hash
  ↓
Data Fingerprint

Digital Signature
  ↓
Private-Key Authentication

Certificate
  ↓
Identity ↔ Public-Key Binding
```

Together:

```text
Certificate
+
Signature
+
Hash
```

form a foundation of modern PKI.

---

# 151. Common Interview Questions

## What is a digital signature?

A digital signature is a cryptographic value generated using a private key that allows others to verify the integrity and authenticity of signed data using the corresponding public key.

---

## What does a digital signature provide?

Primarily:

```text
Integrity
Authentication
Proof of Private-Key Possession
```

---

## Is a digital signature encryption?

No. A digital signature provides authenticity and integrity; encryption provides confidentiality.

---

## What is PKI?

PKI is the infrastructure of certificates, keys, certificate authorities, policies, trust stores, and processes used to establish and manage public-key trust.

---

## What is an X.509 certificate?

An X.509 certificate is a standardized structure that binds an identity to a public key and is signed by an issuer.

---

## What is a CA?

A Certificate Authority is a trusted entity that issues and signs certificates according to defined policies.

---

## What is a root CA?

A root CA is a trust anchor that is explicitly trusted by a platform, organization, or application.

---

## What is an intermediate CA?

An intermediate CA is a subordinate CA whose authority is delegated by another CA, often a root CA.

---

## What is a certificate chain?

A certificate chain is a sequence of certificates linking an end-entity certificate to a trusted root.

---

## What is a CSR?

A Certificate Signing Request contains a public key, requested identity information/extensions, and a proof of possession of the corresponding private key.

---

## Does a CSR contain the private key?

No. The private key should remain secret and under the requester's control.

---

## What is SAN?

Subject Alternative Name is a certificate extension containing identities such as DNS names and IP addresses.

---

## Why is SAN important?

TLS hostname verification uses SAN entries to determine whether a certificate is valid for the requested hostname.

---

## What is certificate revocation?

Revocation invalidates a certificate before its normal expiration time.

---

## What is CRL?

A Certificate Revocation List is a list of revoked certificate serial numbers published by a CA.

---

## What is OCSP?

Online Certificate Status Protocol allows certificate status to be queried from an OCSP responder.

---

## What is OCSP stapling?

The server provides a CA-signed OCSP response to the client during the TLS interaction, reducing the need for the client to contact the responder directly.

---

## What is Certificate Transparency?

Certificate Transparency provides public, auditable logs of publicly trusted certificate issuance.

---

## What is mTLS?

Mutual TLS authenticates both the server and client using certificates.

---

## What is RSA-PSS?

RSA-PSS is a modern RSA digital-signature scheme using probabilistic encoding.

---

## What is ECDSA?

ECDSA is an elliptic-curve digital signature algorithm.

---

## What is Ed25519?

Ed25519 is a modern elliptic-curve digital signature scheme.

---

## Why is ECDSA nonce reuse dangerous?

Improper nonce reuse can expose mathematical relationships that may allow recovery of the private signing key.

---

## What happens if a private signing key is compromised?

An attacker may be able to impersonate the key owner or create fraudulent signatures. The key should be considered compromised and replaced according to the incident-response process.

---

# 152. Quick Revision Table

| Concept | Purpose |
|---|---|
| Digital Signature | Integrity + Authentication |
| Private Key | Signing |
| Public Key | Verification |
| PKI | Public-key trust infrastructure |
| X.509 | Certificate standard |
| Certificate | Identity ↔ Public Key |
| CA | Issues certificates |
| Root CA | Trust Anchor |
| Intermediate CA | Delegated CA |
| CSR | Certificate request |
| SAN | Certificate identities |
| CRL | Revocation list |
| OCSP | Online certificate status |
| CT | Public certificate issuance logging |
| mTLS | Mutual certificate authentication |
| RSA-PSS | RSA signatures |
| ECDSA | ECC signatures |
| Ed25519 | Modern ECC signature scheme |
| HSM | Hardware-protected key operations |
| KMS | Managed cryptographic key infrastructure |

---

# 153. Key Takeaways

```text
1. Digital signatures provide integrity and authentication.

2. Signing uses a private key.

3. Verification uses the corresponding public key.

4. Digital signatures do not provide confidentiality.

5. PKI binds identities to public keys using certificates.

6. X.509 is the common certificate format used by many PKI systems.

7. Root CAs act as trust anchors.

8. Intermediate CAs provide delegated certificate issuance.

9. Certificate chains connect end-entity certificates to trusted roots.

10. SAN is critical for modern TLS hostname validation.

11. A CSR contains a public key and proof of private-key possession.

12. Private keys must never be included in CSRs or exposed unnecessarily.

13. Certificates have validity periods and may be revoked before expiration.

14. CRLs and OCSP provide certificate revocation/status mechanisms.

15. Certificate Transparency improves visibility into public certificate issuance.

16. mTLS authenticates both sides of a connection.

17. RSA-PSS, ECDSA, and Ed25519 are important digital signature schemes.

18. ECDSA nonce failures can expose private keys.

19. Signing keys should be protected using strong key-management controls.

20. Code signing is an important component of software supply-chain security.

21. Certificate validation must include identity, chain, validity, and usage checks.

22. Trusting a public key is different from merely verifying a mathematical signature.

23. PKI requires governance, lifecycle management, monitoring, and incident response.

24. Compromise of a root CA or signing key can have a very large security impact.
```

---

# 154. Chapter Summary

This chapter covered:

```text
Digital Signatures
Signature Generation
Signature Verification
RSA-PSS
ECDSA
Ed25519
Public-Key Infrastructure
PKI
X.509
Certificates
Certificate Authorities
Root CAs
Intermediate CAs
End-Entity Certificates
Certificate Chains
Certificate Validation
Subject
Issuer
SAN
Key Usage
Extended Key Usage
Basic Constraints
CSR
Certificate Revocation
CRL
OCSP
OCSP Stapling
Certificate Transparency
TLS Certificates
mTLS
Code Signing
Software Signing
SSH Authentication
Email Signing
Private-Key Protection
HSM
KMS
Certificate Lifecycle
Key Lifecycle
PKI Attacks
Certificate Misconfiguration
VAPT Testing
SOC Monitoring
Supply Chain Security
```

The central principle is:

> **A digital signature proves control of a private key over specific data, while PKI provides the infrastructure needed to associate that public key with a trusted identity.**

The overall trust model can be remembered as:

```text
                    PRIVATE KEY
                         │
                         ▼
                    SIGN DATA
                         │
                         ▼
                     SIGNATURE
                         │
                         ▼
              ┌─────────────────────┐
              │      PUBLIC KEY     │
              └─────────────────────┘
                         │
                         ▼
                  VERIFY SIGNATURE
                         │
                         ▼
                    VALID / INVALID


Identity
   │
   ▼
Public Key
   │
   ▼
Certificate
   │
   ▼
Intermediate CA
   │
   ▼
Root CA
   │
   ▼
Trusted Trust Store
```

---

# Next Chapter

## Chapter 08 – TLS/SSL & Secure Communications

The next chapter will cover:

```text
TLS Fundamentals
SSL vs TLS
TLS Architecture
TLS Handshake
TLS 1.2
TLS 1.3
Cipher Suites
Key Exchange
ECDHE
Certificates
Server Authentication
Client Authentication
mTLS
Session Keys
Forward Secrecy
AEAD
AES-GCM
ChaCha20-Poly1305
TLS Record Protocol
SNI
ALPN
HTTPS
Certificate Validation
Certificate Errors
TLS Downgrade Attacks
MITM Attacks
BEAST
POODLE
CRIME
BREACH
Heartbleed
ROBOT
Weak Cipher Suites
TLS Configuration
OpenSSL Testing
Browser Security
VAPT Testing
SOC Monitoring
Production TLS Hardening
```

The key question for the next chapter will be:

> **How do certificates, asymmetric cryptography, key exchange, symmetric encryption, and message authentication work together to create a secure HTTPS connection?**