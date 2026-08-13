# Cryptography Cheatsheet

> A practical, interview-focused and cybersecurity-oriented cryptography reference covering fundamentals, algorithms, protocols, attacks, key management, TLS, application security, and post-quantum cryptography.

---

# 1. Cryptography at a Glance

Cryptography provides four primary security properties:

```text
Confidentiality
Integrity
Authentication
Non-Repudiation
```

### Confidentiality

Prevents unauthorized parties from reading data.

```text
Plaintext
   ↓
Encryption
   ↓
Ciphertext
```

### Integrity

Ensures data has not been modified.

```text
Data
 ↓
Hash / MAC / Signature
 ↓
Verification
```

### Authentication

Verifies the identity of a party or authenticity of a message.

```text
Identity
   ↓
Cryptographic Proof
   ↓
Verified
```

### Non-Repudiation

Digital signatures can provide evidence that a particular private key was used to sign data, subject to the trust model and key protection.

---

# 2. Core Cryptography Terminology

| Term | Meaning |
|---|---|
| Plaintext | Original readable data |
| Ciphertext | Encrypted data |
| Encryption | Plaintext → Ciphertext |
| Decryption | Ciphertext → Plaintext |
| Key | Secret/public value controlling cryptographic operation |
| IV | Initialization Vector |
| Nonce | Number used once |
| Salt | Random value used with password processing |
| Hash | Fixed-length digest of input |
| MAC | Message Authentication Code |
| HMAC | Keyed hash-based MAC |
| KDF | Key Derivation Function |
| AEAD | Authenticated Encryption with Associated Data |
| Signature | Publicly verifiable cryptographic proof |
| Certificate | Binding between identity and public key |
| PKI | Public Key Infrastructure |
| KEM | Key Encapsulation Mechanism |
| CSPRNG | Cryptographically Secure Pseudorandom Number Generator |

---

# 3. Cryptography Categories

```text
Cryptography
│
├── Symmetric
│   ├── AES
│   ├── ChaCha20
│   └── etc.
│
├── Asymmetric
│   ├── RSA
│   ├── ECC
│   ├── Diffie-Hellman
│   └── Ed25519
│
├── Hashing
│   ├── SHA-256
│   ├── SHA-3
│   └── BLAKE
│
├── Authentication
│   ├── HMAC
│   └── Digital Signatures
│
├── Key Derivation
│   ├── HKDF
│   ├── Argon2
│   ├── scrypt
│   └── PBKDF2
│
└── Post-Quantum
    ├── ML-KEM
    ├── ML-DSA
    └── SLH-DSA
```

---

# 4. Symmetric Cryptography

Symmetric cryptography uses the same secret key for encryption and decryption.

```text
           Secret Key
               │
               ▼
Plaintext ──► Encrypt ──► Ciphertext
                              │
                              ▼
                         Decrypt
                              │
                              ▼
                           Plaintext
```

### Examples

```text
AES
ChaCha20
3DES   ← Legacy
DES    ← Broken/obsolete
RC4    ← Broken/obsolete
```

### Advantages

```text
Fast
Efficient
Suitable for large amounts of data
```

### Disadvantage

```text
Key distribution
```

---

# 5. Asymmetric Cryptography

Asymmetric cryptography uses:

```text
Public Key
Private Key
```

The private key must remain secret.

The public key can generally be distributed.

---

# 6. Public-Key Encryption

Conceptually:

```text
Sender
  │
  │ Encrypt with recipient's Public Key
  ▼
Ciphertext
  │
  ▼
Recipient
  │
  │ Decrypt with Private Key
  ▼
Plaintext
```

---

# 7. Digital Signature

Conceptually:

```text
Message
   │
   ▼
Hash
   │
   ▼
Sign with Private Key
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
   ├───────────────┐
   ▼               ▼
Calculated Hash   Signature
                   │
                   ▼
            Verify Public Key
                   │
                   ▼
                Valid/Invalid
```

---

# 8. Symmetric vs Asymmetric

| Feature | Symmetric | Asymmetric |
|---|---|---|
| Keys | One shared secret | Public + private |
| Speed | Very fast | Slower |
| Large data | Excellent | Usually inefficient |
| Key exchange | Difficult | Easier |
| Digital signatures | No | Yes |
| Examples | AES, ChaCha20 | RSA, ECC, Ed25519 |
| Quantum impact | Reduced security margin | Major threat |

---

# 9. Hybrid Cryptography

Modern protocols generally combine both.

```text
Asymmetric Cryptography
        ↓
Establish Shared Secret
        ↓
KDF
        ↓
Symmetric Key
        ↓
AES-GCM / ChaCha20-Poly1305
        ↓
Bulk Data Encryption
```

This gives:

```text
Asymmetric:
Key establishment / authentication

Symmetric:
Fast data encryption
```

---

# 10. AES

**AES = Advanced Encryption Standard**

Block size:

```text
128 bits
```

Common key sizes:

```text
AES-128
AES-192
AES-256
```

AES is a:

```text
Symmetric Block Cipher
```

---

# 11. AES Key Sizes

| Algorithm | Key Size |
|---|---:|
| AES-128 | 128 bits |
| AES-192 | 192 bits |
| AES-256 | 256 bits |

AES always uses:

```text
128-bit block size
```

regardless of key size.

---

# 12. Recommended AES Modes

Preferred modern choice:

```text
AES-GCM
```

Other authenticated modes may be appropriate depending on the protocol.

Avoid:

```text
AES-ECB
```

for normal application encryption.

---

# 13. ECB

ECB:

```text
Electronic Codebook
```

is generally unsuitable for encrypting structured application data because identical plaintext blocks can produce identical ciphertext blocks under the same key.

```text
Plaintext Block A
        ↓
       AES
        ↓
Ciphertext A

Plaintext Block A
        ↓
       AES
        ↓
Ciphertext A
```

Patterns can leak.

---

# 14. CBC

CBC:

```text
Cipher Block Chaining
```

can provide confidentiality when correctly implemented.

However, CBC does not inherently provide authentication.

Incorrect implementations can become vulnerable to:

```text
Padding Oracle Attacks
```

Modern applications generally prefer AEAD constructions.

---

# 15. CTR

CTR:

```text
Counter Mode
```

turns a block cipher into a stream-like construction.

Important:

```text
Never reuse the same nonce/counter combination with the same key.
```

---

# 16. GCM

GCM:

```text
Galois/Counter Mode
```

provides:

```text
Encryption
+
Authentication
```

Therefore:

```text
AES-GCM = AEAD
```

Critical rule:

> Never reuse a nonce with the same key.

---

# 17. ChaCha20-Poly1305

Combines:

```text
ChaCha20
+
Poly1305
```

Provides:

```text
Confidentiality
+
Integrity
+
Authentication
```

It is an AEAD construction.

Nonce uniqueness is critical.

---

# 18. AEAD

**AEAD = Authenticated Encryption with Associated Data**

Provides:

```text
Confidentiality
Integrity
Authentication
```

Examples:

```text
AES-GCM
ChaCha20-Poly1305
```

---

# 19. Associated Data

Associated data is authenticated but not encrypted.

Example:

```text
Encrypted:
    Message

Authenticated:
    User ID
    Protocol Version
    Message Type
```

If associated data changes:

```text
Authentication fails
```

---

# 20. Nonce vs IV vs Salt

| Value | Main Purpose |
|---|---|
| Nonce | Uniqueness / freshness |
| IV | Initialization value for cipher mode |
| Salt | Password/KDF randomization |

They are not interchangeable concepts.

---

# 21. Nonce

Nonce:

```text
Number Used Once
```

Depending on the construction, it may not need to be secret.

For AEAD:

```text
Same Key
+
Same Nonce
=
Potentially catastrophic failure
```

---

# 22. IV

Initialization Vector.

Requirements depend on the cipher mode.

Never assume:

```text
IV = Nonce = Salt
```

They serve different purposes.

---

# 23. Salt

A salt is typically used with password hashing/KDFs.

```text
Password
+
Unique Salt
+
KDF
 ↓
Password Verifier
```

The salt generally:

```text
Does not need to be secret.
```

---

# 24. Randomness

Cryptographic systems require secure randomness.

Use:

```text
CSPRNG
```

not ordinary pseudo-random functions for:

```text
Keys
Tokens
Nonces
Session Secrets
Reset Tokens
Authentication Secrets
```

---

# 25. Python Secure Randomness

Use:

```python
import secrets

token = secrets.token_urlsafe(32)
```

Avoid:

```python
import random

random.randint(...)
```

for security-sensitive secrets.

---

# 26. Hash Functions

A cryptographic hash maps arbitrary input to a fixed-size digest.

```text
Input
  ↓
Hash Function
  ↓
Fixed-Length Digest
```

Properties:

```text
Deterministic
One-way
Avalanche effect
Collision resistance
Preimage resistance
Second-preimage resistance
```

---

# 27. Hash Examples

Modern:

```text
SHA-256
SHA-384
SHA-512
SHA-3
SHAKE
BLAKE2
BLAKE3
```

Legacy / unsuitable for new security designs:

```text
MD5
SHA-1
```

---

# 28. SHA-256

SHA-256 produces:

```text
256-bit digest
```

or:

```text
32 bytes
```

Hexadecimal representation:

```text
64 hex characters
```

---

# 29. SHA-512

SHA-512 produces:

```text
512-bit digest
```

or:

```text
64 bytes
```

Hexadecimal representation:

```text
128 hex characters
```

---

# 30. SHA-3

SHA-3 is based on:

```text
Keccak
```

and is structurally different from SHA-2.

Variants include:

```text
SHA3-224
SHA3-256
SHA3-384
SHA3-512
```

---

# 31. Hash Collision

Collision:

```text
A ≠ B
```

but:

```text
Hash(A) = Hash(B)
```

---

# 32. Birthday Bound

For an n-bit hash, generic collision search requires approximately:

```text
2^(n/2)
```

operations.

Therefore:

```text
SHA-256
≈ 128-bit generic collision resistance
```

under idealized assumptions.

---

# 33. Preimage Attack

Given:

```text
Hash(M) = H
```

attacker attempts to find:

```text
M
```

such that:

```text
Hash(M) = H
```

---

# 34. Second-Preimage Attack

Given:

```text
M1
```

attacker tries to find:

```text
M2 ≠ M1
```

such that:

```text
Hash(M1) = Hash(M2)
```

---

# 35. Hashing ≠ Encryption

Hash:

```text
Data
 ↓
Digest
```

Encryption:

```text
Data
 ↓
Ciphertext
 ↓
Decrypt
 ↓
Data
```

Hashing is generally one-way.

Encryption is designed to be reversible with the correct key.

---

# 36. Password Storage

Never store:

```text
Plaintext Password
```

Prefer:

```text
Password
+
Unique Salt
+
Password KDF
 ↓
Verifier
```

Recommended password KDFs include:

```text
Argon2
scrypt
PBKDF2
```

---

# 37. Why Not SHA-256 for Passwords?

SHA-256 is designed to be fast.

Password hashing should deliberately be:

```text
Expensive
Memory-Hard where appropriate
Configurable
Salted
```

Fast hashes make offline password guessing easier.

---

# 38. Argon2

Argon2 is a modern password hashing/KDF family.

Important parameters:

```text
Memory
Time
Parallelism
```

Argon2id is commonly preferred for password storage where supported and appropriately configured.

---

# 39. HMAC

**HMAC = Hash-based Message Authentication Code**

Conceptually:

```text
Secret Key
+
Message
 ↓
HMAC
 ↓
Authentication Tag
```

Provides:

```text
Integrity
Authentication
```

---

# 40. HMAC vs Hash

Hash:

```text
Hash(message)
```

HMAC:

```text
HMAC(secret, message)
```

HMAC requires a secret key.

---

# 41. Never Build a Custom MAC

Avoid:

```python
hash(secret + message)
```

Use:

```python
hmac.new(
    secret,
    message,
    hashlib.sha256
).digest()
```

---

# 42. Length Extension

Certain hash constructions can be vulnerable to length-extension attacks when incorrectly used as MACs.

Avoid:

```text
Hash(secret || message)
```

as a homemade MAC.

Use:

```text
HMAC
```

---

# 43. KDF

**KDF = Key Derivation Function**

Converts existing secret material into cryptographic keys.

Example:

```text
Master Secret
      ↓
     KDF
      ↓
 ┌────┼────┐
 ▼    ▼    ▼
Key A Key B Key C
```

---

# 44. HKDF

**HKDF = HMAC-based Key Derivation Function**

Useful for:

```text
Key Derivation
Key Expansion
Key Separation
Protocol Key Generation
```

Basic conceptual stages:

```text
Extract
  ↓
Expand
```

---

# 45. Password KDF vs HKDF

| Function | Primary Use |
|---|---|
| HKDF | Derive keys from high-entropy secret material |
| Argon2 | Password hashing/KDF |
| scrypt | Password hashing/KDF |
| PBKDF2 | Password-based KDF |

Do not automatically substitute one for another.

---

# 46. Key Separation

Use different derived keys for different purposes:

```text
Master Secret
    │
    ├── Encryption Key
    ├── Authentication Key
    ├── Export Key
    └── Session Key
```

---

# 47. RSA

RSA is an asymmetric cryptographic algorithm based on integer factorization.

Uses:

```text
Digital Signatures
Encryption
Key Encapsulation in legacy systems
```

RSA is not considered post-quantum secure.

---

# 48. RSA Key Pair

```text
Public Key
Private Key
```

Public key:

```text
Can be distributed
```

Private key:

```text
Must remain secret
```

---

# 49. RSA Encryption

Conceptually:

```text
Plaintext
   ↓
Recipient Public Key
   ↓
Ciphertext
```

Decryption:

```text
Ciphertext
   ↓
Recipient Private Key
   ↓
Plaintext
```

Modern implementations should use secure padding schemes such as RSA-OAEP rather than textbook RSA.

---

# 50. RSA Signatures

Signing:

```text
Message
 ↓
Hash
 ↓
Private Key
 ↓
Signature
```

Verification:

```text
Message
+
Signature
+
Public Key
 ↓
Valid / Invalid
```

Modern applications should use standardized secure signature encodings such as RSA-PSS where appropriate.

---

# 51. Diffie-Hellman

Diffie-Hellman enables two parties to establish a shared secret over an insecure channel.

Conceptually:

```text
Alice                          Bob
  │                              │
  │──── Public Information ─────►│
  │                              │
  │◄──── Public Information ─────│
  │                              │
  └──── Shared Secret ───────────┘
```

The shared secret itself is never directly transmitted.

---

# 52. ECDH

Elliptic Curve Diffie-Hellman.

Provides:

```text
Key Agreement
```

Common modern variant:

```text
X25519
```

---

# 53. Forward Secrecy

Forward secrecy means compromise of a long-term private key does not automatically expose previously established session secrets, assuming the protocol and ephemeral keys were used correctly.

Usually achieved through:

```text
Ephemeral Diffie-Hellman
```

such as:

```text
ECDHE
X25519
```

---

# 54. ECDSA

ECDSA:

```text
Elliptic Curve Digital Signature Algorithm
```

Provides:

```text
Digital Signatures
```

Critical:

```text
Secure nonce generation
```

is essential.

Nonce reuse can expose the private key.

---

# 55. Ed25519

Ed25519 is an EdDSA signature scheme.

Advantages:

```text
Fast
Small Keys
Small Signatures
Deterministic Signing
Simple APIs
```

It is:

```text
Classical
```

not post-quantum.

---

# 56. X25519

X25519 is used for:

```text
Elliptic-Curve Diffie-Hellman
```

It provides:

```text
Key Agreement
```

It is not a digital signature algorithm.

---

# 57. ECC Quick Map

```text
ECC
│
├── ECDH
│   └── Key Agreement
│
├── ECDSA
│   └── Digital Signature
│
├── Ed25519
│   └── Digital Signature
│
└── X25519
    └── Key Agreement
```

---

# 58. Certificates

A certificate binds:

```text
Identity
+
Public Key
```

A typical TLS certificate contains:

```text
Subject
Issuer
Public Key
Validity
SAN
Signature
Extensions
```

---

# 59. SAN

SAN:

```text
Subject Alternative Name
```

Modern hostname validation relies primarily on SAN entries.

Example:

```text
DNS:example.com
DNS:api.example.com
```

---

# 60. Certificate Chain

Typical structure:

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
```

The client validates the chain back to a trusted root.

---

# 61. PKI

**PKI = Public Key Infrastructure**

Includes:

```text
Certificate Authorities
Certificates
Public Keys
Private Keys
Trust Stores
Certificate Policies
Revocation
Certificate Lifecycle
```

---

# 62. Root CA

Root CA certificates are trust anchors.

They are typically self-signed and distributed through trusted trust stores.

---

# 63. Intermediate CA

Intermediate CAs are used to issue end-entity certificates.

Architecture:

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
```

This reduces the need to use the root private key for routine issuance.

---

# 64. Certificate Validation

Check:

```text
Signature
Validity Period
Hostname
Trust Chain
Key Usage
Extended Key Usage
Revocation Status where applicable
```

---

# 65. TLS

TLS:

```text
Transport Layer Security
```

Provides:

```text
Confidentiality
Integrity
Server Authentication
Optional Client Authentication
```

---

# 66. HTTPS

HTTPS is essentially:

```text
HTTP
+
TLS
```

Conceptually:

```text
HTTP
 ↓
TLS
 ↓
TCP
 ↓
IP
```

For HTTP/3:

```text
HTTP
 ↓
QUIC
 ↓
UDP
```

with TLS 1.3 integrated into QUIC.

---

# 67. TLS 1.2 vs TLS 1.3

TLS 1.3 provides:

```text
Simplified Handshake
Removal of Many Legacy Algorithms
Forward-Secrecy-Oriented Key Exchange
Fewer Round Trips in Common Cases
Modern Cipher Suite Design
```

Preferred modern protocol:

```text
TLS 1.3
```

TLS 1.2 may still be required for compatibility.

---

# 68. TLS 1.3 Cipher Suites

TLS 1.3 uses AEAD cipher suites such as:

```text
TLS_AES_128_GCM_SHA256
TLS_AES_256_GCM_SHA384
TLS_CHACHA20_POLY1305_SHA256
```

Key exchange and authentication are negotiated separately from the symmetric cipher suite.

---

# 69. TLS Handshake

Simplified:

```text
Client
  │
  │ ClientHello
  ▼
Server
  │
  │ ServerHello
  │ Certificate
  │ Key Exchange
  ▼
Client
  │
  │ Finished
  ▼
Server
  │
  ▼
Encrypted Application Data
```

---

# 70. TLS Provides

```text
Confidentiality
Integrity
Authentication
Key Establishment
```

TLS does not automatically guarantee:

```text
Application Authorization
```

---

# 71. TLS Certificate Attack

Potential issues:

```text
Expired Certificate
Wrong Hostname
Untrusted CA
Weak Validation
Compromised CA
Mis-issued Certificate
Disabled Verification
```

---

# 72. Never Disable TLS Verification

Dangerous:

```python
requests.get(
    url,
    verify=False
)
```

This can expose the application to server impersonation and MITM attacks.

---

# 73. mTLS

Mutual TLS:

```text
Client authenticates Server
+
Server authenticates Client
```

Useful for:

```text
Service-to-Service Authentication
Microservices
APIs
Enterprise Networks
Zero Trust Architectures
```

---

# 74. TLS Forward Secrecy

Modern TLS commonly uses ephemeral key exchange:

```text
ECDHE
X25519
```

This helps protect previously established sessions if long-term keys are compromised later.

---

# 75. Replay Attack

A replay attack:

```text
Capture Valid Request
        ↓
Send Again
        ↓
Server Accepts
```

Possible defenses:

```text
Nonce
Timestamp
Sequence Number
Request ID
Challenge
Server-Side State
```

---

# 76. MITM

Man-in-the-Middle:

```text
Alice
  │
  ▼
Attacker
  │
  ▼
Bob
```

The attacker attempts to:

```text
Read
Modify
Inject
Replay
```

TLS certificate validation helps prevent server impersonation.

---

# 77. Downgrade Attack

Attacker attempts:

```text
Strong Protocol
      ↓
Weak Protocol
```

Examples:

```text
TLS 1.3
 ↓
Older TLS

Strong Cipher
 ↓
Weak Cipher
```

Mitigate through secure protocol configuration and downgrade protections.

---

# 78. Brute Force

Trying many possible:

```text
Keys
Passwords
Secrets
Tokens
```

For an ideal n-bit key:

```text
Search Space = 2^n
```

---

# 79. Dictionary Attack

Uses likely passwords:

```text
password
admin
qwerty
welcome
companyname
```

---

# 80. Credential Stuffing

Uses previously leaked credentials:

```text
Username + Password
        ↓
Try Another Website
```

Password reuse is the underlying enabler.

---

# 81. Password Spraying

Uses one/few common passwords across many accounts:

```text
alice → Password123
bob → Password123
charlie → Password123
```

---

# 82. Offline Password Cracking

Attacker obtains:

```text
Password Hashes
```

and performs guesses locally.

Defenses:

```text
Strong Password KDF
Unique Salts
Strong Passwords
MFA
```

---

# 83. Rainbow Tables

Precomputed password-hash structures.

Unique salts make precomputed tables much less useful because each salt changes the derived output.

---

# 84. Padding Oracle

Typically associated with poorly protected block-cipher constructions such as CBC.

Concept:

```text
Modified Ciphertext
        ↓
Decryption
        ↓
Padding Check
        ↓
Observable Difference
```

This can leak information about plaintext.

---

# 85. Timing Attack

Attacker measures execution time:

```text
Input A → 10.1 ms
Input B → 10.8 ms
```

Small differences can potentially reveal information.

Use constant-time comparison functions for sensitive comparisons.

---

# 86. Constant-Time Comparison

Python:

```python
import hmac

hmac.compare_digest(
    expected,
    received
)
```

Useful for:

```text
HMAC Tags
Tokens
Authentication Codes
Other Security-Sensitive Values
```

---

# 87. Side-Channel Attack

Examples:

```text
Timing
Cache
Power
Electromagnetic
Memory Access
Error Messages
```

Side channels exploit implementation behavior rather than directly breaking the mathematical primitive.

---

# 88. Length Extension

Dangerous construction:

```text
Hash(secret || message)
```

Potentially vulnerable to length-extension attacks depending on the hash construction.

Prefer:

```text
HMAC(secret, message)
```

---

# 89. Birthday Attack

For an n-bit hash:

```text
Collision complexity ≈ 2^(n/2)
```

Example:

```text
SHA-256
≈ 2^128 generic collision work
```

---

# 90. JWT

JWT:

```text
JSON Web Token
```

Common structure:

```text
HEADER.PAYLOAD.SIGNATURE
```

---

# 91. JWT Is Not Automatically Encrypted

A signed JWT generally contains an encoded payload that can be decoded by anyone possessing the token.

Therefore:

```text
JWT
≠
Encryption
```

A JWE can provide encryption.

---

# 92. JWT Security Checklist

```text
☐ Verify signature
☐ Explicitly allow algorithms
☐ Reject unexpected algorithms
☐ Validate issuer
☐ Validate audience
☐ Validate expiration
☐ Validate not-before where required
☐ Validate required claims
☐ Use strong keys
☐ Protect tokens
☐ Consider token replay
```

---

# 93. JWT Algorithm Confusion

Example:

```text
Expected:
RS256

Attacker attempts:
HS256
```

A vulnerable implementation may misuse an RSA public key as an HMAC secret.

Defense:

```text
Explicit algorithm allowlisting
Correct key type
Modern JWT library
```

---

# 94. JWT `none`

Historical vulnerability:

```text
alg = none
```

Some vulnerable implementations accepted unsigned tokens.

Modern secure libraries should reject unsafe configurations.

---

# 95. JWT Claims

Important claims:

```text
iss → Issuer
sub → Subject
aud → Audience
exp → Expiration
nbf → Not Before
iat → Issued At
jti → JWT ID
```

---

# 96. Key Management

Key lifecycle:

```text
Generate
   ↓
Store
   ↓
Distribute
   ↓
Use
   ↓
Rotate
   ↓
Revoke
   ↓
Destroy
```

---

# 97. Key Management Principles

```text
Least Privilege
Key Separation
Rotation
Secure Storage
Access Control
Audit Logging
Backup
Recovery
Revocation
Destruction
```

---

# 98. KMS

KMS:

```text
Key Management Service
```

Provides capabilities such as:

```text
Key Generation
Key Storage
Encryption
Decryption
Signing
Verification
Rotation
Access Control
Audit Logging
```

---

# 99. HSM

HSM:

```text
Hardware Security Module
```

Used for:

```text
Private Key Protection
Signing
Encryption
Key Generation
Certificate Operations
```

---

# 100. KMS vs HSM

| KMS | HSM |
|---|---|
| Key management service | Dedicated cryptographic hardware |
| Often cloud-managed | Hardware security boundary |
| APIs | Cryptographic operations |
| Access policies | Strong physical/hardware protections |
| Scalable | Specialized security |

Cloud KMS may itself rely on HSM-backed infrastructure.

---

# 101. Envelope Encryption

Instead of encrypting all data directly with a master key:

```text
Master Key
    ↓
Encrypts DEK
    ↓
Encrypted DEK

DEK
 ↓
Encrypts Data
 ↓
Ciphertext
```

DEK:

```text
Data Encryption Key
```

---

# 102. Secret Management

Do not store production secrets in:

```text
Source Code
Git
Logs
Docker Images
Public Config
Client-Side JavaScript
```

Use:

```text
Secrets Manager
KMS
HSM
Protected Environment
Short-Lived Credentials
```

where appropriate.

---

# 103. Secret Leak Response

If a secret leaks:

```text
1. Revoke
2. Rotate
3. Investigate
4. Audit usage
5. Remove exposure
6. Improve controls
```

Do not simply delete the secret from the current file and assume the problem is solved.

---

# 104. Git Secret Exposure

Secrets may remain in:

```text
Git History
Branches
Tags
Forks
CI Logs
Artifacts
Caches
```

Use:

```text
Secret Scanning
Gitleaks
TruffleHog
Platform Secret Scanning
```

---

# 105. Certificate Lifecycle

```text
Generate Key
      ↓
Create CSR
      ↓
CA Validation
      ↓
Certificate Issued
      ↓
Deploy
      ↓
Monitor
      ↓
Renew
      ↓
Revoke
```

---

# 106. Digital Signature Properties

Digital signatures provide:

```text
Integrity
Authentication
Signature Verification
```

They can also support non-repudiation within an appropriate legal and operational framework.

---

# 107. Signature vs HMAC

| HMAC | Digital Signature |
|---|---|
| Symmetric | Asymmetric |
| Shared secret | Private/public key |
| Fast | Slower |
| Both parties need secret | Verifier only needs public key |
| No public verification | Public verification |

---

# 108. MAC vs Encryption

MAC:

```text
Authentication
+
Integrity
```

Encryption:

```text
Confidentiality
```

AEAD:

```text
Confidentiality
+
Integrity
+
Authentication
```

---

# 109. Encoding vs Encryption

Base64:

```text
Encoding
```

not:

```text
Encryption
```

Example:

```text
Secret
 ↓
Base64
 ↓
Encoded Secret
```

Anyone can decode it.

---

# 110. Obfuscation vs Encryption

Obfuscation attempts to make information harder to understand.

Encryption provides cryptographic confidentiality based on a key.

Do not treat:

```text
Obfuscation
```

as a replacement for:

```text
Encryption
```

---

# 111. Secure Token Generation

Bad:

```python
import random

token = random.randint(100000, 999999)
```

Better:

```python
import secrets

token = secrets.token_urlsafe(32)
```

Additional protections:

```text
Expiration
Single Use
Rate Limiting
Server-Side Validation
Revocation
```

---

# 112. Cryptographic API Mistakes

Common vulnerabilities:

```text
Hard-Coded Keys
Static IVs
Nonce Reuse
Weak RNG
Weak Hashes
Weak Password KDF
ECB
Disabled TLS Validation
Incorrect JWT Validation
Custom Cryptography
Ignored Authentication Errors
```

---

# 113. Secure Development Rules

```text
Use trusted libraries.
Use standardized algorithms.
Use CSPRNG.
Use AEAD.
Use password-specific KDFs.
Protect private keys.
Rotate secrets.
Validate certificates.
Allowlist algorithms.
Use constant-time comparisons where appropriate.
Avoid custom cryptographic protocols.
Fail closed.
```

---

# 114. Cryptographic Attack Map

```text
Cryptographic Attacks
│
├── Key Attacks
│   ├── Brute Force
│   ├── Weak Keys
│   └── Key Leakage
│
├── Password Attacks
│   ├── Dictionary
│   ├── Credential Stuffing
│   ├── Password Spraying
│   └── Offline Cracking
│
├── Protocol Attacks
│   ├── MITM
│   ├── Replay
│   └── Downgrade
│
├── Implementation Attacks
│   ├── Timing
│   ├── Padding Oracle
│   ├── Nonce Reuse
│   └── Side Channel
│
├── Hash Attacks
│   ├── Collision
│   ├── Birthday
│   └── Length Extension
│
└── JWT / Application
    ├── Algorithm Confusion
    ├── Weak Secret
    ├── Claim Validation
    └── Token Replay
```

---

# 115. Quantum Computing

Quantum computers use:

```text
Qubits
```

and exploit:

```text
Superposition
Entanglement
Interference
```

---

# 116. Shor's Algorithm

Threatens:

```text
RSA
Diffie-Hellman
ECDH
ECDSA
Ed25519
```

because it can efficiently solve:

```text
Integer Factorization
Discrete Logarithms
```

on sufficiently capable quantum computers.

---

# 117. Grover's Algorithm

Provides quadratic speedup for certain search problems.

Simplified:

```text
Classical:
2^n

Quantum:
2^(n/2)
```

---

# 118. Quantum Impact Summary

| Primitive | Quantum Effect |
|---|---|
| RSA | Major threat |
| DH | Major threat |
| ECDH | Major threat |
| ECDSA | Major threat |
| Ed25519 | Major threat |
| AES-128 | Reduced margin |
| AES-256 | Larger margin |
| SHA-256 | Reduced generic search margin |
| SHA-3 | Reduced generic search margin |

---

# 119. Post-Quantum Cryptography

PQC algorithms are designed to resist:

```text
Classical Attackers
+
Quantum Attackers
```

Important standardized algorithms include:

```text
ML-KEM
ML-DSA
SLH-DSA
```

---

# 120. ML-KEM

Purpose:

```text
Post-Quantum Key Encapsulation
```

Use:

```text
Shared Secret Establishment
```

Not bulk data encryption.

Typical architecture:

```text
ML-KEM
 ↓
Shared Secret
 ↓
KDF
 ↓
AES-GCM
```

---

# 121. ML-DSA

Purpose:

```text
Post-Quantum Digital Signatures
```

Applications:

```text
Authentication
Certificates
Software Signing
Document Signing
```

---

# 122. SLH-DSA

Purpose:

```text
Post-Quantum Digital Signatures
```

Based on:

```text
Hash-Based Cryptography
```

---

# 123. Hybrid PQC

Transitional architecture:

```text
Classical Key Exchange
+
PQC KEM
        ↓
Combined Secret
        ↓
KDF
        ↓
Symmetric Key
```

Example concept:

```text
X25519 + ML-KEM
```

---

# 124. Harvest Now, Decrypt Later

Attack lifecycle:

```text
Capture encrypted traffic
        ↓
Store encrypted data
        ↓
Wait for stronger computing capability
        ↓
Attempt decryption
```

High-risk data:

```text
Government
Military
Healthcare
Financial
Trade Secrets
Long-Term Research
Private Communications
```

---

# 125. Crypto Agility

Design systems so:

```text
Algorithm
Key Size
KEM
Signature
Cipher
```

can be changed without redesigning the entire system.

---

# 126. PQC Migration

Recommended high-level process:

```text
Inventory
 ↓
Classify
 ↓
Identify Long-Lived Data
 ↓
Assess Dependencies
 ↓
Implement Crypto Agility
 ↓
Test PQC
 ↓
Deploy Hybrid
 ↓
Migrate
 ↓
Retire Legacy Crypto
```

---

# 127. Modern Cryptography

Other important technologies:

```text
Zero-Knowledge Proofs
Homomorphic Encryption
Secure Multi-Party Computation
Secret Sharing
Threshold Cryptography
Trusted Execution Environments
Hardware-Backed Keys
WebAuthn
FIDO2
Passkeys
```

---

# 128. Zero-Knowledge Proof

Prove:

```text
"I know X"
```

without revealing:

```text
X
```

Applications:

```text
Privacy
Identity
Anonymous Credentials
Blockchain
Secure Verification
```

---

# 129. Homomorphic Encryption

Allows computation over encrypted data.

```text
Encrypt(Data)
     ↓
Compute on Ciphertext
     ↓
Encrypted Result
     ↓
Decrypt
```

---

# 130. Secure Multi-Party Computation

Multiple parties jointly compute:

```text
f(A, B, C)
```

without necessarily revealing:

```text
A
B
C
```

to each other.

---

# 131. Secret Sharing

Split a secret:

```text
Secret
 ↓
Share 1
Share 2
Share 3
Share 4
Share 5
```

Example threshold:

```text
3-of-5
```

Any three shares reconstruct the secret.

---

# 132. Threshold Cryptography

Instead of:

```text
One person
 ↓
Private Key
```

use:

```text
Multiple parties
       ↓
Threshold
       ↓
Cryptographic Operation
```

Example:

```text
3 of 5 administrators
```

must authorize an operation.

---

# 133. Passkeys

Passkeys use public-key cryptography.

```text
Device
 ↓
Private Key
```

Server stores:

```text
Public Key
```

Authentication:

```text
Challenge
 ↓
Private-Key Signature
 ↓
Server Verification
```

---

# 134. Passkey Advantages

Can reduce:

```text
Password Reuse
Phishing
Credential Stuffing
Password Database Attacks
```

---

# 135. WebAuthn

WebAuthn enables:

```text
Public-Key Authentication
```

using:

```text
Browser
+
Authenticator
+
Website
```

---

# 136. Modern Cryptography Decision Table

| Requirement | Preferred Direction |
|---|---|
| Bulk encryption | AES-GCM / ChaCha20-Poly1305 |
| Password storage | Argon2id / scrypt / PBKDF2 |
| Key derivation | HKDF |
| Message authentication | HMAC |
| Classical key agreement | X25519 |
| Classical signatures | Ed25519 |
| TLS | TLS 1.3 |
| PQ key encapsulation | ML-KEM |
| PQ signatures | ML-DSA / SLH-DSA |
| Key management | KMS / HSM |
| Passwordless authentication | Passkeys / WebAuthn |

---

# 137. Algorithm Quick Reference

```text
AES
→ Symmetric block cipher

AES-GCM
→ AEAD

ChaCha20
→ Stream cipher

Poly1305
→ MAC

ChaCha20-Poly1305
→ AEAD

SHA-256
→ Cryptographic hash

SHA-3
→ Cryptographic hash family

HMAC
→ Keyed authentication

HKDF
→ Key derivation

Argon2id
→ Password KDF

RSA
→ Public-key cryptography

ECDH
→ Key agreement

X25519
→ Key agreement

ECDSA
→ Digital signatures

Ed25519
→ Digital signatures

ML-KEM
→ PQ key encapsulation

ML-DSA
→ PQ signatures

SLH-DSA
→ Hash-based PQ signatures
```

---

# 138. Key Size Quick Reference

```text
AES-128
→ 128-bit key

AES-192
→ 192-bit key

AES-256
→ 256-bit key

SHA-256
→ 256-bit digest

SHA-512
→ 512-bit digest
```

Do not directly compare key sizes across unrelated cryptographic systems.

For example:

```text
256-bit AES
```

is not equivalent to:

```text
256-bit RSA
```

Cryptographic security depends on the underlying mathematical problem and construction.

---

# 139. Common Security Mistakes

```text
❌ MD5 for security
❌ SHA-1 for new security designs
❌ DES
❌ 3DES for new systems
❌ RC4
❌ ECB for application data
❌ Hard-coded keys
❌ Static GCM nonce
❌ Reused IV
❌ Predictable random tokens
❌ Plaintext passwords
❌ SHA-256 directly for password storage
❌ Homemade encryption
❌ Homemade MAC
❌ Disabled TLS verification
❌ Trusting JWT algorithm blindly
❌ Logging secrets
❌ Secrets in Git
❌ Ignoring certificate validation
❌ One key for unrelated purposes
```

---

# 140. Secure Alternatives

```text
❌ MD5
→ SHA-256 / SHA-3 where appropriate

❌ SHA-1
→ SHA-256 / SHA-3

❌ DES
→ AES

❌ 3DES
→ AES

❌ RC4
→ AES-GCM / ChaCha20-Poly1305

❌ ECB
→ AEAD

❌ Plain SHA-256(password)
→ Argon2id / scrypt / PBKDF2

❌ random.random()
→ secrets / OS CSPRNG

❌ Hash(secret + message)
→ HMAC

❌ Custom encryption
→ Established cryptographic library

❌ Disabled TLS verification
→ Proper certificate validation

❌ Hard-coded secret
→ KMS / Secrets Manager / secure secret store
```

---

# 141. VAPT Cryptography Checklist

## Discovery

```text
☐ Identify TLS endpoints
☐ Identify certificates
☐ Identify encryption libraries
☐ Identify JWTs
☐ Identify password storage
☐ Identify KMS/HSM
☐ Identify cryptographic protocols
```

## Configuration

```text
☐ TLS versions
☐ Cipher suites
☐ Certificate chain
☐ Certificate expiry
☐ Hostname validation
☐ Key sizes
☐ Algorithm selection
```

## Application

```text
☐ Hard-coded keys
☐ Static IVs
☐ Nonce reuse
☐ Weak randomness
☐ Weak password KDF
☐ JWT issues
☐ Custom cryptography
☐ Authentication failures
```

## Secrets

```text
☐ Git
☐ Logs
☐ Containers
☐ CI/CD
☐ Environment
☐ Backups
```

## PQC

```text
☐ RSA dependencies
☐ ECC dependencies
☐ Long-lived data
☐ Crypto agility
☐ PQC support
☐ Hybrid support
```

---

# 142. TLS Testing Commands

### OpenSSL Version

```bash
openssl version
```

### TLS 1.3 Test

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com \
    -tls1_3
```

### Nmap TLS Enumeration

```bash
nmap --script ssl-enum-ciphers -p 443 example.com
```

Use only against systems you are authorized to test.

---

# 143. Useful Cryptography Tools

```text
OpenSSL
Wireshark
Nmap
Burp Suite
Hashcat
John the Ripper
Gitleaks
TruffleHog
Cloud KMS
HSM
CyberChef
```

---

# 144. OpenSSL Useful Commands

### List Ciphers

```bash
openssl list -cipher-algorithms
```

### List Digests

```bash
openssl list -digest-algorithms
```

### Inspect Certificate

```bash
openssl x509 \
    -in certificate.pem \
    -text \
    -noout
```

### Inspect TLS

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com
```

---

# 145. Python Cryptography Examples

## Secure Random Token

```python
import secrets

token = secrets.token_urlsafe(32)
```

## HMAC

```python
import hmac
import hashlib

tag = hmac.new(
    key,
    message,
    hashlib.sha256
).digest()
```

## Constant-Time Comparison

```python
hmac.compare_digest(
    expected,
    received
)
```

Use established cryptographic libraries rather than implementing primitives manually.

---

# 146. Password Storage Flow

```text
User Password
      ↓
Unique Random Salt
      ↓
Argon2id
      ↓
Password Verifier
      ↓
Database
```

Authentication:

```text
Entered Password
      ↓
Same KDF + Stored Salt
      ↓
Calculated Verifier
      ↓
Compare
```

---

# 147. Encryption Flow

Modern application pattern:

```text
Plaintext
    │
    ▼
AES-GCM / ChaCha20-Poly1305
    │
    ├── Key
    ├── Nonce
    └── Associated Data
    │
    ▼
Ciphertext + Authentication Tag
```

---

# 148. Key Exchange Flow

Classical:

```text
X25519
   ↓
Shared Secret
   ↓
HKDF
   ↓
Traffic Keys
```

Post-quantum:

```text
ML-KEM
   ↓
Shared Secret
   ↓
HKDF
   ↓
Traffic Keys
```

Hybrid:

```text
X25519
   +
ML-KEM
   ↓
Combined Secret
   ↓
HKDF
   ↓
Traffic Keys
```

---

# 149. Signature Flow

```text
Message
   ↓
Hash / Signature Scheme
   ↓
Private Key
   ↓
Signature
```

Verification:

```text
Message
+
Signature
+
Public Key
 ↓
Verification
 ↓
Valid / Invalid
```

---

# 150. Certificate Flow

```text
Server
 ↓
Generate Key Pair
 ↓
Create CSR
 ↓
Certificate Authority
 ↓
Certificate
 ↓
Deploy
 ↓
Client Validates
```

---

# 151. Cryptographic Incident Response

## Secret Leak

```text
Detect
 ↓
Revoke
 ↓
Rotate
 ↓
Audit
 ↓
Investigate
 ↓
Remediate
```

## Private-Key Compromise

```text
Revoke Certificate
 ↓
Generate New Key
 ↓
Issue New Certificate
 ↓
Deploy
 ↓
Investigate Historical Exposure
```

## Weak Password Hashing

```text
Upgrade KDF
 ↓
Reset Passwords if Required
 ↓
Monitor
 ↓
Remove Legacy Hashing
```

---

# 152. SOC Detection Opportunities

Monitor:

```text
Unusual KMS Usage
Certificate Changes
TLS Failures
TLS Downgrades
JWT Failures
Token Replay
Secret Access
Mass Decryption
Unusual Signing
Credential Stuffing
Password Spraying
Certificate Anomalies
Unexpected Cryptographic Library Changes
```

---

# 153. Example SOC Detection

Normal:

```text
Application
→ 100 KMS decrypt operations/hour
```

Anomaly:

```text
Application
→ 1,000,000 decrypt operations/hour
```

Possible:

```text
Compromised Application
Compromised Credentials
Misconfiguration
Legitimate Batch Job
```

Correlate with:

```text
IAM
Application Logs
Deployment Events
Network
User
Time
```

---

# 154. Cryptographic Security Architecture

```text
                  Identity
                     │
                     ▼
                    IAM
                     │
                     ▼
Client ───────► API Gateway
                     │
                    TLS
                     │
                     ▼
                Application
                     │
           ┌─────────┴─────────┐
           ▼                   ▼
         KMS              Secrets Manager
           │                   │
           ▼                   ▼
         Keys               Secrets
           │
           ▼
      Encrypted Data
```

---

# 155. Secure Cryptography Principles

```text
1. Do not invent cryptography.
2. Use reviewed libraries.
3. Use standardized algorithms.
4. Use CSPRNG.
5. Use AEAD.
6. Protect keys.
7. Rotate secrets.
8. Separate keys by purpose.
9. Never reuse AEAD nonces.
10. Validate certificates.
11. Allowlist algorithms.
12. Use password-specific KDFs.
13. Use constant-time comparison where necessary.
14. Fail closed.
15. Plan for cryptographic agility.
16. Prepare for post-quantum migration.
```

---

# 156. Interview One-Liners

### What is cryptography?

> The science of protecting information using mathematical techniques.

### What is encryption?

> Transforming plaintext into ciphertext using a cryptographic key.

### What is decryption?

> Recovering plaintext from ciphertext using the appropriate key.

### What is hashing?

> A one-way transformation that produces a fixed-length digest.

### What is symmetric encryption?

> Encryption using the same secret key for encryption and decryption.

### What is asymmetric cryptography?

> Cryptography using a public/private key pair.

### What is AES?

> A symmetric block cipher standardized for secure encryption.

### What is AES-GCM?

> An authenticated encryption mode providing confidentiality and integrity.

### What is a nonce?

> A value intended to be used once within a cryptographic context.

### Why is nonce reuse dangerous?

> Reusing an AEAD nonce with the same key can compromise confidentiality and integrity.

### What is HMAC?

> A keyed message-authentication construction based on a cryptographic hash.

### What is HKDF?

> An HMAC-based key derivation function used to derive cryptographic keys.

### Why not use SHA-256 for passwords?

> It is too fast for password storage and enables efficient offline guessing.

### What is Argon2?

> A password hashing/KDF family designed to make password guessing expensive.

### What is RSA?

> An asymmetric cryptographic algorithm based on integer factorization.

### What is ECDH?

> An elliptic-curve key-agreement mechanism.

### What is X25519?

> A modern elliptic-curve Diffie-Hellman key-agreement mechanism.

### What is Ed25519?

> A modern elliptic-curve digital signature scheme.

### What is a digital signature?

> A cryptographic mechanism that allows verification of authenticity and integrity using a public key.

### What is PKI?

> The infrastructure used to manage certificates, public keys, private keys, and trust relationships.

### What is TLS?

> A protocol that provides secure communication over networks.

### What is HTTPS?

> HTTP protected by TLS.

### What is a certificate?

> A signed credential that binds an identity to a public key.

### What is MITM?

> An attack where an adversary positions themselves between communicating parties.

### What is a replay attack?

> Reusing a previously valid message or request.

### What is a padding oracle?

> A vulnerability where observable padding-validation behavior leaks information about encrypted data.

### What is a timing attack?

> An attack that extracts information from measurable execution-time differences.

### What is JWT?

> A token format commonly used to carry signed claims.

### Is JWT encrypted?

> Not necessarily; ordinary signed JWTs are encoded and signed, not encrypted.

### What is algorithm confusion?

> A vulnerability where an application verifies cryptographic data using an unintended algorithm.

### What is forward secrecy?

> Protection of previous session secrets even if a long-term key is compromised later.

### What is quantum-resistant cryptography?

> Cryptography designed to resist attacks from sufficiently capable quantum computers.

### What is Shor's algorithm?

> A quantum algorithm that threatens factorization- and discrete-log-based public-key cryptography.

### What is Grover's algorithm?

> A quantum algorithm providing a quadratic speedup for certain search problems.

### What is ML-KEM?

> A standardized post-quantum key encapsulation mechanism.

### What is ML-DSA?

> A standardized post-quantum digital signature algorithm.

### What is SLH-DSA?

> A standardized hash-based post-quantum digital signature algorithm.

### What is crypto agility?

> The ability to replace cryptographic algorithms and parameters without major system redesign.

### What is HNDL?

> Harvest Now, Decrypt Later: capturing encrypted information today for possible future decryption.

---

# 157. Most Important Numbers

```text
AES block size
→ 128 bits

AES-128
→ 128-bit key

AES-192
→ 192-bit key

AES-256
→ 256-bit key

SHA-256
→ 256-bit digest

SHA-512
→ 512-bit digest

SHA-256 generic collision security
→ ~128 bits

SHA-256 generic preimage security
→ ~256 bits classically

AES-128 classical brute-force
→ ~2^128

AES-256 classical brute-force
→ ~2^256

Simplified Grover estimate:
AES-128 → ~2^64
AES-256 → ~2^128
```

These are simplified theoretical security estimates, not direct predictions of practical attack cost.

---

# 158. Most Important Relationships

```text
AES
→ Encryption

AES-GCM
→ Encryption + Authentication

ChaCha20-Poly1305
→ Encryption + Authentication

SHA-256
→ Hashing

HMAC
→ Authentication + Integrity

Argon2id
→ Password Protection

HKDF
→ Key Derivation

X25519
→ Key Exchange

Ed25519
→ Digital Signature

RSA
→ Classical Public-Key Cryptography

TLS
→ Secure Network Communication

PKI
→ Certificate Trust Infrastructure

KMS
→ Key Management

HSM
→ Hardware Key Protection

ML-KEM
→ PQ Key Encapsulation

ML-DSA
→ PQ Digital Signature

SLH-DSA
→ PQ Hash-Based Signature
```

---

# 159. What to Use vs What to Avoid

| Requirement | Use | Avoid |
|---|---|---|
| Encryption | AES-GCM | ECB |
| Encryption | ChaCha20-Poly1305 | RC4 |
| Passwords | Argon2id | MD5 |
| Passwords | scrypt | SHA-256 directly |
| MAC | HMAC | `hash(secret + msg)` |
| Randomness | CSPRNG | `random` |
| Key Exchange | X25519 / approved modern protocol | Custom DH |
| Signatures | Ed25519 / approved scheme | Homemade signature |
| TLS | TLS 1.3 | SSL / old TLS |
| Secret Storage | KMS / Secret Manager | Git |
| Key Protection | HSM/KMS | Plaintext files |
| Tokens | CSPRNG | Predictable IDs |
| PQ Key Exchange | ML-KEM | RSA for future PQ security |
| PQ Signatures | ML-DSA / SLH-DSA | Classical-only signatures for long-term PQ requirements |

---

# 160. Final Cryptography Mind Map

```text
CRYPTOGRAPHY
│
├── Fundamentals
│   ├── Confidentiality
│   ├── Integrity
│   ├── Authentication
│   └── Non-Repudiation
│
├── Symmetric
│   ├── AES
│   ├── AES-GCM
│   ├── ChaCha20
│   └── Poly1305
│
├── Asymmetric
│   ├── RSA
│   ├── DH
│   ├── ECDH
│   ├── ECDSA
│   ├── Ed25519
│   └── X25519
│
├── Hashing
│   ├── SHA-256
│   ├── SHA-512
│   ├── SHA-3
│   └── BLAKE
│
├── Authentication
│   ├── HMAC
│   └── Digital Signatures
│
├── Passwords
│   ├── Argon2
│   ├── scrypt
│   └── PBKDF2
│
├── Key Management
│   ├── KDF
│   ├── HKDF
│   ├── KMS
│   ├── HSM
│   └── Rotation
│
├── PKI
│   ├── Certificates
│   ├── CA
│   ├── Trust Store
│   └── Certificate Chain
│
├── Protocols
│   ├── TLS
│   ├── HTTPS
│   ├── SSH
│   └── mTLS
│
├── Attacks
│   ├── Brute Force
│   ├── Dictionary
│   ├── Replay
│   ├── MITM
│   ├── Downgrade
│   ├── Padding Oracle
│   ├── Timing
│   ├── Side Channel
│   ├── Nonce Reuse
│   ├── JWT Confusion
│   └── Key Leakage
│
├── Modern Crypto
│   ├── ZKP
│   ├── MPC
│   ├── FHE
│   ├── Secret Sharing
│   └── Threshold Crypto
│
└── Post-Quantum
    ├── Shor
    ├── Grover
    ├── ML-KEM
    ├── ML-DSA
    ├── SLH-DSA
    ├── Hybrid Crypto
    ├── HNDL
    └── Crypto Agility
```

---

# 161. Final 30-Second Revision

```text
Symmetric
→ Same secret key

Asymmetric
→ Public + private key

AES
→ Symmetric encryption

AES-GCM
→ Authenticated encryption

ChaCha20-Poly1305
→ Authenticated encryption

Hash
→ One-way digest

SHA-256
→ 256-bit hash

HMAC
→ Keyed integrity/authentication

Argon2id
→ Password hashing

HKDF
→ Key derivation

X25519
→ Key exchange

Ed25519
→ Digital signature

RSA/ECC
→ Classical public-key crypto

TLS
→ Secure network communication

PKI
→ Certificate trust

KMS/HSM
→ Key protection

Nonce
→ Use correctly and avoid reuse

Salt
→ Password KDF randomization

JWT
→ Signed claims, not automatically encrypted

MITM
→ Intercept communication

Replay
→ Reuse valid message

Padding Oracle
→ Decryption feedback leakage

Timing Attack
→ Timing side channel

Shor
→ Threatens RSA/ECC

Grover
→ Reduces generic search security

ML-KEM
→ PQ key encapsulation

ML-DSA
→ PQ signatures

SLH-DSA
→ Hash-based PQ signatures

Crypto Agility
→ Prepare for algorithm replacement

HNDL
→ Data captured today may be decrypted later
```

---

# 162. Golden Rules of Cryptography

```text
1. Never implement cryptographic primitives yourself.

2. Use established, audited libraries.

3. Prefer standardized algorithms.

4. Use AEAD for modern application encryption.

5. Never reuse an AEAD nonce with the same key.

6. Use CSPRNG for security-sensitive randomness.

7. Never store plaintext passwords.

8. Never use fast general-purpose hashes as password KDFs.

9. Use unique salts for password hashing.

10. Use HMAC instead of homemade MAC constructions.

11. Protect private keys.

12. Never hard-code production secrets.

13. Rotate compromised keys immediately.

14. Never disable TLS certificate verification in production.

15. Explicitly allowlist cryptographic algorithms.

16. Validate JWT signatures and security-sensitive claims.

17. Use constant-time comparison for appropriate secret values.

18. Separate keys by purpose.

19. Follow least privilege for KMS/HSM access.

20. Monitor cryptographic operations.

21. Treat certificates as security-sensitive assets.

22. Use forward secrecy where appropriate.

23. Design protocols with replay protection.

24. Do not confuse encoding with encryption.

25. Do not confuse hashing with encryption.

26. Do not confuse authentication with authorization.

27. Do not assume encryption automatically provides integrity.

28. Do not assume a strong algorithm compensates for bad implementation.

29. Build cryptographic agility into long-lived systems.

30. Inventory RSA/ECC dependencies for post-quantum migration.

31. Prioritize long-lived sensitive data against HNDL threats.

32. Evaluate hybrid PQC migration strategies.

33. Keep cryptographic libraries patched.

34. Fail closed when cryptographic verification fails.

35. Security comes from the complete system—not merely the algorithm.
```

---

# 163. Final Mental Model

The entire subject can be reduced to:

```text
             SECURE CRYPTOGRAPHIC SYSTEM
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
    ALGORITHM            KEY             RANDOMNESS
       │                 │                 │
       ▼                 ▼                 ▼
    AES-GCM          Secure Storage       CSPRNG
    X25519           Rotation             Nonces
    Ed25519          KMS/HSM              IVs
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                     PROTOCOL
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
             TLS        PKI       Auth
              │          │          │
              └──────────┼──────────┘
                         ▼
                    APPLICATION
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
           JWT         Secrets      Data
             │           │           │
             └───────────┼───────────┘
                         ▼
                      ATTACKS
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
    Nonce Reuse       Key Leakage       MITM
    Replay            JWT Bugs          Timing
    Padding Oracle    Weak KDF          Downgrade
                         │
                         ▼
                   FUTURE THREATS
                         │
                    QUANTUM COMPUTING
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
            Shor                   Grover
              │                     │
              ▼                     ▼
          RSA / ECC             Symmetric
              │                     │
              └──────────┬──────────┘
                         ▼
                       PQC
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           ML-KEM     ML-DSA     SLH-DSA
              │          │          │
              └──────────┼──────────┘
                         ▼
                 CRYPTO AGILITY
                         │
                         ▼
               QUANTUM-RESILIENT
                    ARCHITECTURE
```

> **Cryptography is not just about encryption. It is the combination of algorithms, keys, randomness, protocols, identities, implementations, lifecycle management, and operational controls that creates real security.**