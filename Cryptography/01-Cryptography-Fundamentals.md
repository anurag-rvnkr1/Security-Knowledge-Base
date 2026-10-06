# Chapter 01 – Cryptography Fundamentals

## Overview

**Cryptography** is the science of protecting information using mathematical algorithms, cryptographic keys, and security protocols.

It is one of the fundamental building blocks of modern cybersecurity.

Cryptography enables systems to provide:

```text
Confidentiality
Integrity
Authentication
Non-Repudiation
```

It is used in:

- HTTPS
- TLS
- SSH
- VPNs
- Password protection
- Digital signatures
- Secure APIs
- Messaging applications
- Cloud platforms
- Banking systems
- Digital certificates
- Software signing
- Secure storage

The purpose of this chapter is to establish the fundamental concepts required to understand the rest of the Cryptography module.

---

# 1. What is Cryptography?

Cryptography is the practice of transforming information so that only authorized parties can access or verify it.

A simplified model is:

```text
Plaintext
    │
    ▼
Encryption Algorithm + Key
    │
    ▼
Ciphertext
    │
    ▼
Decryption Algorithm + Key
    │
    ▼
Plaintext
```

Example:

```text
Plaintext:
Hello

Encryption:
AES + Secret Key

Ciphertext:
<encrypted data>

Decryption:
AES + Secret Key

Plaintext:
Hello
```

The actual ciphertext produced by a secure algorithm should not reveal the original plaintext without the appropriate key.

---

# 2. Cryptography vs Cryptanalysis vs Cryptology

These terms are related but different.

## Cryptography

Cryptography focuses on designing and using mechanisms that protect information.

```text
Cryptography
    ↓
Secure Algorithms
    ↓
Secure Protocols
    ↓
Secure Systems
```

---

## Cryptanalysis

Cryptanalysis focuses on analyzing cryptographic systems and finding ways to break or weaken them.

```text
Cryptographic System
        ↓
Analysis
        ↓
Weakness
        ↓
Attack
```

Examples include:

- Brute-force attacks
- Frequency analysis
- Cryptographic implementation attacks
- Side-channel analysis
- Protocol attacks

---

## Cryptology

Cryptology is the broader field encompassing:

```text
Cryptography
      +
Cryptanalysis
      =
Cryptology
```

---

# 3. Why Cryptography is Needed

Without cryptography, sensitive information could be exposed or modified while being transmitted or stored.

Consider:

```text
User
 │
 │ Username + Password
 ▼
Internet
 │
 ▼
Server
```

Without protection, an attacker positioned between the user and server could potentially observe or modify the communication.

With cryptographic protection:

```text
User
 │
 │ Encrypted Communication
 ▼
Internet
 │
 │ Attacker sees ciphertext
 ▼
Server
```

The attacker may observe network traffic but should not be able to recover or modify the protected information without detection.

---

# 4. Core Security Properties

Cryptography primarily supports four major security properties.

```text
                Cryptography
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
Confidentiality   Integrity   Authentication
                     │
                     ▼
              Non-Repudiation
```

---

# 5. Confidentiality

**Confidentiality** means preventing unauthorized parties from reading information.

Example:

```text
Plaintext:
Transfer ₹10,000

        ↓ Encryption

Ciphertext:
<unreadable encrypted data>
```

Only an authorized party possessing the appropriate key should be able to recover:

```text
Transfer ₹10,000
```

Common technologies providing confidentiality include:

- AES
- ChaCha20
- TLS
- Disk encryption
- Database encryption

---

# 6. Integrity

**Integrity** means detecting unauthorized modification of information.

Suppose:

```text
Original:
Transfer ₹10,000
```

An attacker changes it to:

```text
Transfer ₹90,000
```

A secure integrity mechanism should allow the recipient to detect that the message has been modified.

Integrity can be provided using:

- Cryptographic hashes
- MACs
- Digital signatures
- Authenticated encryption

---

# 7. Authentication

Authentication answers:

> **Who created or sent this information?**

For example:

```text
Client
   │
   │ Authentication
   ▼
Server
```

The server needs to determine whether the client is legitimate.

Cryptographic authentication mechanisms include:

- HMAC
- Digital signatures
- Certificates
- Public-key authentication
- Cryptographic challenge-response protocols

---

# 8. Non-Repudiation

**Non-repudiation** is the ability to provide evidence that a particular party performed an action.

Digital signatures can provide cryptographic evidence that a private key was used to sign data.

Example:

```text
Document
    │
    ▼
Private Key
    │
    ▼
Digital Signature
    │
    ▼
Signed Document
```

The recipient can use the corresponding public key to verify the signature.

Non-repudiation is more nuanced than simply saying "digital signatures prove who signed something." Legal and organizational non-repudiation also depends on key custody, identity binding, procedures, and applicable law.

---

# 9. Plaintext

**Plaintext** is the original information before encryption.

Example:

```text
Hello World
```

or:

```text
username=anurag&role=user
```

Plaintext does not necessarily mean human-readable text. It can represent:

- Text
- Binary data
- Images
- Files
- Network messages
- Database records

---

# 10. Ciphertext

**Ciphertext** is the output produced by encryption.

```text
Plaintext
   +
Encryption Algorithm
   +
Key
   ↓
Ciphertext
```

Secure ciphertext should not expose useful information about the plaintext to an attacker who lacks the required key.

---

# 11. Encryption

**Encryption** transforms plaintext into ciphertext.

```text
Plaintext
    │
    ▼
Encryption
    │
    │ Key
    ▼
Ciphertext
```

---

# 12. Decryption

**Decryption** transforms ciphertext back into plaintext.

```text
Ciphertext
    │
    ▼
Decryption
    │
    │ Key
    ▼
Plaintext
```

---

# 13. Encryption vs Encoding

These concepts are frequently confused.

## Encryption

Purpose:

```text
Security
```

Requires a cryptographic key.

Example:

```text
AES
```

---

## Encoding

Purpose:

```text
Data Representation / Compatibility
```

Usually does not require a secret key.

Examples:

```text
Base64
Hexadecimal
URL Encoding
```

Base64 is **not encryption**.

Example:

```text
Hello
   ↓ Base64
SGVsbG8=
```

Anyone can decode it.

---

# 14. Encryption vs Hashing

Encryption is generally designed to be reversible with the appropriate key.

```text
Encryption:

Plaintext
   ↓
Ciphertext
   ↓
Decryption
   ↓
Plaintext
```

Hashing is designed as a one-way transformation.

```text
Data
  ↓
Hash Function
  ↓
Digest
```

You do not normally "decrypt" a cryptographic hash.

Examples:

```text
Encryption → AES
Hashing    → SHA-256
```

---

# 15. Encryption vs Hashing vs Encoding

| Property | Encryption | Hashing | Encoding |
|---|---|---|---|
| Primary purpose | Confidentiality | Integrity / fingerprinting | Representation |
| Reversible | Yes, with key | No practical inverse | Yes |
| Requires secret key | Usually | No | No |
| Example | AES | SHA-256 | Base64 |
| Security mechanism | Yes | Yes | No |

---

# 16. Cryptographic Keys

A **cryptographic key** is information used by a cryptographic algorithm to control a cryptographic operation.

Example:

```text
Plaintext
    +
Secret Key
    +
AES
    ↓
Ciphertext
```

The security of a properly designed cryptosystem should depend on protecting the key rather than hiding the algorithm.

---

# 17. Keyspace

A **keyspace** is the set of all possible keys for a cryptographic algorithm.

For an ideal key of `n` bits:

```text
Number of possible keys = 2^n
```

Examples:

```text
8-bit key  → 2^8   = 256
128-bit key → 2^128
256-bit key → 2^256
```

A larger keyspace generally makes exhaustive search more difficult, assuming the algorithm and key generation are otherwise sound.

---

# 18. Brute-Force Attack

A brute-force attack attempts possible keys until the correct key is found.

Conceptually:

```text
Key 1 → Fail
Key 2 → Fail
Key 3 → Fail
...
Correct Key → Success
```

For an ideal `n`-bit key, an attacker may need up to:

```text
2^n
```

trials.

On average, an exhaustive search finds the key after roughly half the keyspace has been tested.

---

# 19. Kerckhoffs's Principle

A fundamental cryptographic principle states that a cryptosystem should remain secure even if everything about the system except the secret key is public.

In simplified form:

```text
Security should depend on:
        ↓
Secret Key
```

not:

```text
Secret Algorithm
```

This means:

```text
Public Algorithm
+
Secret Key
=
Secure System
```

when the algorithm and implementation are sound.

---

# 20. Security Through Obscurity

Security through obscurity relies primarily on keeping system details secret.

Example:

```text
"Our encryption is secure because nobody knows how it works."
```

This is not a sound cryptographic security model.

A stronger approach is:

```text
Publicly Analyzed Algorithm
+
Secure Implementation
+
Strong Key Management
```

---

# 21. Cryptographic Algorithm

A cryptographic algorithm is a mathematical procedure used to perform a security-related operation.

Examples:

```text
AES
RSA
SHA-256
ECDSA
ChaCha20
```

Different algorithms serve different purposes.

---

# 22. Cryptographic Primitive

A **cryptographic primitive** is a fundamental building block used to construct secure systems.

Examples include:

```text
Block Cipher
Stream Cipher
Hash Function
MAC
Digital Signature
Key Exchange
KDF
```

A primitive by itself does not necessarily constitute a complete secure protocol.

---

# 23. Cryptographic Protocol

A cryptographic protocol defines how multiple cryptographic mechanisms interact between parties.

Example:

```text
TLS
```

TLS may combine:

```text
Certificates
+
Digital Signatures
+
Key Exchange
+
Key Derivation
+
Symmetric Encryption
+
Authentication
```

---

# 24. Cryptographic System

A complete cryptographic system includes more than an algorithm.

It may include:

```text
Algorithm
+
Keys
+
Key Management
+
Protocol
+
Implementation
+
Configuration
+
Trust Model
```

A strong algorithm can still be deployed insecurely if the surrounding system is poorly designed.

---

# 25. Symmetric Cryptography

Symmetric cryptography uses shared secret key material.

Conceptually:

```text
          Shared Secret Key
             /       \
            ▼         ▼
         Sender     Receiver
            │         ▲
            ▼         │
        Encryption → Decryption
```

Examples:

```text
AES
ChaCha20
```

---

# 26. Asymmetric Cryptography

Asymmetric cryptography uses a key pair:

```text
Public Key
Private Key
```

The keys are mathematically related.

Conceptually:

```text
Public Key  → Can be shared
Private Key → Must be protected
```

Examples:

```text
RSA
ECC
EdDSA
```

---

# 27. Symmetric vs Asymmetric Cryptography

| Property | Symmetric | Asymmetric |
|---|---|---|
| Keys | Shared secret | Public/private pair |
| Speed | Generally fast | Generally slower |
| Main uses | Bulk encryption | Key exchange, signatures |
| Examples | AES, ChaCha20 | RSA, ECC |
| Key distribution | Challenging | Easier for public keys |
| Typical data encryption | Yes | Usually not for bulk data |

Modern systems often combine both.

---

# 28. Hybrid Cryptography

Many real-world systems use symmetric and asymmetric cryptography together.

Example:

```text
Asymmetric Cryptography
        ↓
Securely establish / protect key material
        ↓
Symmetric Session Key
        ↓
Encrypt large amounts of data
```

This combines:

```text
Asymmetric Cryptography
        +
Symmetric Cryptography
```

---

# 29. Cryptographic Hash Function

A cryptographic hash function takes input of arbitrary length and produces a fixed-size digest.

```text
Input
  ↓
Hash Function
  ↓
Fixed-Length Digest
```

Example:

```text
"Hello"
   ↓
SHA-256
   ↓
256-bit digest
```

Important properties include:

- Preimage resistance
- Second-preimage resistance
- Collision resistance
- Deterministic output
- Avalanche behavior

These are explored in detail in Chapter 05.

---

# 30. Message Authentication Code

A MAC provides integrity and authentication using shared secret key material.

```text
Message
   +
Secret Key
   ↓
MAC Algorithm
   ↓
MAC Tag
```

The receiver recomputes and verifies the tag.

Example:

```text
HMAC
```

---

# 31. Digital Signature

Digital signatures provide a public-key mechanism for signing and verifying data.

Conceptually:

```text
Message
   +
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

---

# 32. Key Exchange

Key exchange allows parties to establish shared cryptographic key material.

Example:

```text
Alice
  │
  │ Key Exchange
  ▼
Bob
  │
  ▼
Shared Secret
```

A classic example is:

```text
Diffie-Hellman
```

Modern systems often use elliptic-curve variants such as:

```text
ECDH
```

---

# 33. Key Derivation

A Key Derivation Function (KDF) derives cryptographic keys from existing secret material.

```text
Secret Material
      ↓
     KDF
      ↓
Derived Key
```

Examples include:

```text
HKDF
PBKDF2
scrypt
Argon2
```

Different KDFs serve different use cases.

---

# 34. Randomness in Cryptography

Cryptographic systems require high-quality randomness for tasks such as:

```text
Key Generation
Nonces
Initialization Vectors
Tokens
Seeds
```

Predictable randomness can compromise security.

For security-sensitive randomness, systems should use a:

```text
Cryptographically Secure Pseudorandom Number Generator
```

or an appropriate operating-system cryptographic random source.

---

# 35. Entropy

**Entropy** represents uncertainty or unpredictability.

Cryptographic systems require sufficient entropy to generate unpredictable secret values.

Conceptually:

```text
More Unpredictability
        ↓
Stronger Secret Material
```

Poor entropy can result in:

```text
Predictable Keys
Predictable Tokens
Predictable Nonces
```

---

# 36. Nonce

A **nonce** is a value intended to be used in a particular cryptographic context, often to ensure uniqueness.

The exact security requirement depends on the algorithm.

For some constructions:

```text
Nonce must be unique
```

For others:

```text
Nonce must be unpredictable
```

Nonce misuse can have severe consequences.

For example, reusing a nonce with certain AEAD constructions can compromise confidentiality and integrity.

---

# 37. Initialization Vector

An **Initialization Vector (IV)** is an input used by certain encryption modes.

Its required properties depend on the algorithm and mode.

Do not assume:

```text
IV = Secret
```

An IV is often transmitted alongside ciphertext.

Example:

```text
IV + Ciphertext
```

The security requirement is generally about properties such as uniqueness or unpredictability rather than secrecy.

---

# 38. Salt

A **salt** is additional data used with password hashing or key derivation.

Conceptually:

```text
Password + Salt
       ↓
     KDF
       ↓
Stored Hash
```

Salts help prevent attackers from efficiently reusing precomputed tables across users with the same password.

A salt generally does **not** need to be secret.

---

# 39. Passwords and Cryptography

Passwords should not normally be stored as plaintext.

Bad:

```text
username | password
```

Better:

```text
username | password_hash
```

Modern password storage generally uses dedicated password hashing/KDF functions such as:

```text
Argon2
scrypt
bcrypt
PBKDF2
```

with appropriate parameters and unique salts.

---

# 40. Authentication vs Authorization

These concepts are different.

## Authentication

Answers:

```text
Who are you?
```

## Authorization

Answers:

```text
What are you allowed to do?
```

Example:

```text
Authentication
      ↓
User = Alice
      ↓
Authorization
      ↓
Alice can access /reports
```

Cryptography can support authentication, but authorization is an access-control decision.

---

# 41. Digital Certificates

A digital certificate binds an identity or subject to a public key through a trust framework.

Simplified:

```text
Identity
   +
Public Key
   +
CA Signature
   ↓
Certificate
```

Certificates are heavily used in:

```text
HTTPS
TLS
PKI
Enterprise Authentication
Software Signing
```

---

# 42. Public Key Infrastructure

PKI provides infrastructure for managing trust in public keys.

Typical structure:

```text
Root CA
   │
   ▼
Intermediate CA
   │
   ▼
Certificate
   │
   ▼
Server / Identity
```

PKI involves:

```text
Certificates
Certificate Authorities
Private Keys
Public Keys
Validation
Revocation
Trust Chains
```

---

# 43. Cryptographic Agility

**Cryptographic agility** is the ability to replace or upgrade cryptographic algorithms and parameters without redesigning the entire system.

This is important because:

```text
Algorithms age
     ↓
Standards evolve
     ↓
Threats change
     ↓
Systems need upgrades
```

Modern systems should avoid hard-coding assumptions that make cryptographic migration extremely difficult.

---

# 44. Cryptographic Failures

A system can use a strong algorithm and still be vulnerable.

Common causes include:

```text
Weak Keys
Poor Randomness
Nonce Reuse
Hard-Coded Secrets
Weak Password Hashing
Incorrect API Usage
Insecure Modes
Certificate Validation Errors
Poor Key Management
Outdated Algorithms
Protocol Design Errors
Side Channels
```

Therefore:

> **Cryptographic security depends on the entire system, not just the algorithm.**

---

# 45. Common Weak Algorithms

Some historical algorithms are no longer appropriate for modern security use.

Examples:

```text
DES
3DES
MD5
SHA-1
RC4
```

The exact status and acceptable use can depend on the context and standard, but new systems should generally use modern, approved algorithms and configurations.

---

# 46. Why MD5 is Not Suitable for Security Integrity

MD5 has known collision attacks.

Conceptually:

```text
Message A
    ↓
  MD5
    ↓
Digest X

Message B
    ↓
  MD5
    ↓
Digest X
```

An attacker may construct different inputs with the same digest under practical attack models.

Therefore MD5 should not be relied upon for modern cryptographic collision resistance.

---

# 47. Why SHA-1 is Deprecated for Many Security Uses

SHA-1 has practical collision weaknesses.

Modern systems should generally prefer:

```text
SHA-256
SHA-384
SHA-512
SHA-3
```

depending on the use case and required standard.

---

# 48. ECB Mode Problem

Electronic Codebook (ECB) encrypts identical plaintext blocks into identical ciphertext blocks when using the same key.

Conceptually:

```text
Plaintext Block A
      ↓
     AES
      ↓
Ciphertext A

Same Plaintext Block A
      ↓
     AES
      ↓
Same Ciphertext A
```

This can reveal structural patterns.

ECB should generally not be used for encrypting structured data.

---

# 49. Hard-Coded Keys

Bad practice:

```python
SECRET_KEY = "my-secret-key"
```

Problems:

```text
Source Code Exposure
Repository Leaks
Credential Reuse
Difficult Rotation
```

Prefer secure secret-management mechanisms appropriate to the environment.

---

# 50. Cryptographic Implementation vs Algorithm

Consider:

```text
AES
```

AES itself is a well-studied algorithm.

But an implementation can still be vulnerable through:

```text
Weak Key Generation
Nonce Reuse
Incorrect Mode
Bad API Usage
Side Channels
Hard-Coded Keys
Poor Error Handling
```

Therefore:

```text
Secure Algorithm
      ≠
Automatically Secure Application
```

---

# 51. Side-Channel Attacks

Side-channel attacks attempt to extract information from physical or implementation-level behavior rather than directly breaking the mathematical algorithm.

Possible signals include:

```text
Timing
Power Consumption
Electromagnetic Emissions
Cache Behavior
Memory Access Patterns
```

This is particularly important in high-assurance cryptographic implementations.

---

# 52. Threat Model

Before selecting cryptographic protections, define the threat model.

Ask:

```text
Who is the attacker?
What can they observe?
What can they modify?
What secrets are they targeting?
What resources do they have?
What security property must be protected?
```

Example:

```text
Attacker
   │
   ├── Can observe network traffic
   ├── Can modify packets
   └── Cannot directly access server private key
```

The cryptographic protocol should be designed against the relevant attacker capabilities.

---

# 53. Security by Design

Cryptography should be considered during system design, not added at the end.

Example:

```text
Application Design
        ↓
Threat Model
        ↓
Security Requirements
        ↓
Cryptographic Design
        ↓
Implementation
        ↓
Testing
        ↓
Deployment
```

---

# 54. Common Cryptographic Mistakes

Avoid:

```text
❌ Creating your own encryption algorithm
❌ Using Base64 as encryption
❌ Storing plaintext passwords
❌ Using weak hashes for password storage
❌ Reusing nonces incorrectly
❌ Hard-coding encryption keys
❌ Using outdated algorithms
❌ Ignoring certificate validation
❌ Using ECB for structured data
❌ Generating keys with predictable randomness
❌ Assuming encryption automatically provides authentication
❌ Assuming hashing provides confidentiality
```

---

# 55. Cryptographic Best Practices

Prefer:

```text
☑ Standardized algorithms
☑ Well-maintained cryptographic libraries
☑ Strong key generation
☑ Secure key storage
☑ Appropriate key rotation
☑ Modern authenticated encryption
☑ Secure password KDFs
☑ Proper certificate validation
☑ Secure randomness
☑ Threat modeling
☑ Cryptographic agility
☑ Regular security review
```

---

# 56. Modern Cryptographic Building Blocks

Modern secure applications commonly use:

```text
AES-GCM
ChaCha20-Poly1305
SHA-256 / SHA-3
HMAC
HKDF
ECDH
EdDSA
TLS 1.3
```

The appropriate choice depends on the protocol, platform, compliance requirements, and implementation library.

---

# 57. Authenticated Encryption

Encryption alone provides confidentiality.

Authenticated encryption provides:

```text
Confidentiality
+
Integrity
+
Authentication of Ciphertext / Associated Data
```

Common AEAD constructions include:

```text
AES-GCM
ChaCha20-Poly1305
```

This is an important concept in modern protocol design.

---

# 58. Associated Data

AEAD can protect both:

```text
Encrypted Data
```

and:

```text
Additional Authenticated Data
```

The additional data is authenticated but not encrypted.

Conceptually:

```text
Plaintext
    +
AAD
    +
Key
    +
Nonce
    ↓
AEAD
    ↓
Ciphertext + Authentication Tag
```

Examples of AAD might include protocol headers or metadata that must remain visible but must not be modified unnoticed.

---

# 59. Cryptographic Lifecycle

Cryptographic material has a lifecycle:

```text
Generate
   ↓
Distribute
   ↓
Store
   ↓
Use
   ↓
Rotate
   ↓
Revoke
   ↓
Destroy
```

Every stage must be considered.

---

# 60. Key Compromise

If a private or secret key is compromised:

```text
Detect
 ↓
Contain
 ↓
Revoke / Disable
 ↓
Rotate
 ↓
Investigate
 ↓
Assess Historical Exposure
 ↓
Recover
```

The impact depends on:

```text
Key Type
Key Lifetime
Forward Secrecy
Data Protected
Attacker Access
```

---

# 61. Forward Secrecy

Forward secrecy means compromise of a long-term private key should not allow an attacker to decrypt previously captured sessions, assuming the protocol and implementation provide the property correctly.

Conceptually:

```text
Long-Term Key
      │
      ├── Session A
      ├── Session B
      └── Session C
```

With appropriate ephemeral key exchange:

```text
Compromise Long-Term Key
       ↓
Past Session Keys remain protected
```

Modern TLS deployments commonly use ephemeral Diffie-Hellman key exchange to provide forward secrecy.

---

# 62. Cryptographic Trust

Cryptography alone does not automatically tell you who to trust.

For example:

```text
Public Key
```

does not inherently prove:

```text
"This key belongs to example.com."
```

A trust system such as PKI can establish that binding.

Thus:

```text
Cryptography
+
Identity
+
Trust Model
=
Secure Authentication
```

---

# 63. Mathematical Foundations

Cryptography relies on mathematical concepts such as:

```text
Modular Arithmetic
Prime Numbers
Probability
Number Theory
Discrete Logarithms
Integer Factorization
Elliptic Curves
Complexity Theory
```

The level of mathematics required depends on whether you are:

```text
Using cryptography
        vs
Implementing cryptography
        vs
Designing cryptographic algorithms
```

---

# 64. Computational Security

Modern cryptography often does not claim that an attack is mathematically impossible.

Instead, it aims for attacks to be computationally infeasible.

Example:

```text
Attack exists theoretically
        ↓
Required computation
        ↓
Practically impossible with available resources
```

This distinction is fundamental to modern cryptographic security.

---

# 65. Security Parameters

Cryptographic algorithms have security parameters such as:

```text
Key Size
Hash Output Size
Group Size
Iteration Count
Memory Cost
Time Cost
```

These parameters affect resistance to attacks.

For example:

```text
Password KDF
    ↓
More computational cost
    ↓
Higher attacker cost
```

Parameters should be selected according to current standards and threat models.

---

# 66. Cryptographic Standards

Modern cryptographic systems should generally rely on established standards and well-reviewed implementations.

Examples of organizations and standards ecosystems include:

```text
NIST
IETF
ISO/IEC
RFCs
FIPS
```

The appropriate standard depends on the application and regulatory environment.

---

# 67. Cryptographic Libraries

Application developers should generally use established cryptographic libraries rather than implementing primitives from scratch.

Examples include libraries supporting:

```text
AES
RSA
ECC
SHA
HMAC
HKDF
AEAD
TLS
```

A library must still be:

```text
Supported
Updated
Correctly Configured
Correctly Used
```

---

# 68. Secure Cryptographic API Usage

Even a safe library can be misused.

Example risks:

```text
Wrong Mode
Wrong Key Size
Nonce Reuse
Incorrect Padding
Disabled Certificate Validation
Weak Randomness
Improper Error Handling
```

Always follow the library's security guidance and use high-level APIs where appropriate.

---

# 69. Cryptography in Web Security

Modern web applications depend heavily on cryptography.

```text
Browser
   │
   ▼
TLS
   │
   ▼
HTTPS
   │
   ▼
Web Application
```

Cryptography protects:

```text
Credentials
Session Cookies
API Requests
Personal Data
Payment Information
Authentication
```

---

# 70. Cryptography in Cloud Security

Cloud environments commonly use cryptography for:

```text
Encryption at Rest
Encryption in Transit
Key Management
Secrets Management
Certificate Management
Object Storage
Database Encryption
Disk Encryption
```

Cloud KMS systems help manage cryptographic keys, but correct access control and key lifecycle management remain essential.

---

# 71. Cryptography in Cybersecurity

Cryptography appears throughout cybersecurity:

```text
Identity
     ↓
Authentication
     ↓
Authorization
     ↓
Secure Communication
     ↓
Data Protection
     ↓
Software Integrity
     ↓
Incident Investigation
```

---

# 72. Cryptography and VAPT

During a security assessment, inspect:

```text
TLS Configuration
Certificate Validation
Password Storage
Hash Algorithms
Encryption Algorithms
Key Management
Secret Exposure
Randomness
JWT Configuration
Cryptographic APIs
```

Typical findings include:

```text
Weak TLS
Expired Certificates
Weak Ciphers
Hard-Coded Secrets
Weak Password Hashing
Improper Certificate Validation
Weak Randomness
```

---

# 73. Cryptography and SOC Operations

SOC teams may investigate:

```text
Certificate Alerts
TLS Anomalies
Credential Compromise
Malicious Certificates
Encrypted Traffic
Key Exposure
Authentication Failures
```

Cryptographic understanding helps analysts interpret these events correctly.

---

# 74. Cryptography and Zero Trust

Zero Trust architectures commonly depend on:

```text
Strong Identity
Mutual Authentication
TLS
Certificates
Short-Lived Credentials
Encryption
Key Management
```

A simplified model:

```text
Never Trust Automatically
        ↓
Verify Identity
        ↓
Authenticate
        ↓
Authorize
        ↓
Encrypt Communication
        ↓
Continuously Monitor
```

---

# 75. Cryptographic Security Model

A secure system should consider:

```text
Algorithm
   +
Key
   +
Randomness
   +
Implementation
   +
Protocol
   +
Key Management
   +
Trust Model
   +
Operational Security
```

A weakness in any layer can undermine the overall system.

---

# 76. Fundamental Cryptography Diagram

```text
                         CRYPTOGRAPHY
                              │
              ┌───────────────┼────────────────┐
              ▼               ▼                ▼
        Confidentiality    Integrity      Authentication
              │               │                │
              ▼               ▼                ▼
        Encryption         Hash/MAC        Signatures
              │               │                │
              └───────────────┼────────────────┘
                              ▼
                       Secure Protocols
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
               TLS           SSH           VPN
                │             │             │
                └─────────────┼─────────────┘
                              ▼
                     Secure Applications
```

---

# 77. Key Concepts to Remember

```text
Cryptography
→ Protects information using mathematical mechanisms.

Encryption
→ Provides confidentiality.

Hashing
→ Provides fixed-length cryptographic fingerprints and supports integrity-related constructions.

MAC
→ Provides authentication and integrity using shared secrets.

Digital Signature
→ Provides public-key verification of signed data.

Key Exchange
→ Establishes shared secret material.

KDF
→ Derives cryptographic keys.

PKI
→ Establishes trust around public keys.

TLS
→ Combines multiple cryptographic mechanisms into a secure communication protocol.

AEAD
→ Provides encryption plus integrity/authentication.

Cryptographic Agility
→ Allows cryptographic systems to evolve safely.
```

---

# 78. Quick Comparison

| Mechanism | Secret Key | Public/Private Keys | Reversible | Primary Purpose |
|---|---:|---:|---:|---|
| Encryption | Yes | Sometimes | Yes | Confidentiality |
| Hash | No | No | No | Digest / integrity support |
| MAC | Yes | No | No | Integrity + authentication |
| Digital Signature | No shared secret | Yes | No | Authentication / signing |
| Key Exchange | Depends | Often | N/A | Establish shared secret |
| KDF | Input-dependent | No | No | Derive keys |
| Certificate | No | Yes | N/A | Identity ↔ public key binding |

---

# 79. Common Interview Questions

## What is cryptography?

Cryptography is the science of protecting information using mathematical algorithms and keys to provide properties such as confidentiality, integrity, authentication, and non-repudiation.

---

## What is the difference between encryption and hashing?

Encryption is designed to be reversible using the appropriate key, while cryptographic hashing produces a digest and is designed to be computationally infeasible to reverse.

---

## What is the difference between symmetric and asymmetric cryptography?

Symmetric cryptography uses shared secret key material, while asymmetric cryptography uses a public/private key pair.

---

## What is a cryptographic key?

A cryptographic key is secret or public information used by a cryptographic algorithm to control a cryptographic operation.

---

## What is a hash function?

A cryptographic hash function maps input data to a fixed-size digest while providing properties such as preimage and collision resistance.

---

## What is a MAC?

A MAC is a keyed cryptographic mechanism that provides message integrity and authentication.

---

## What is a digital signature?

A digital signature is a cryptographic value generated using a private key and verified using a corresponding public key.

---

## What is PKI?

PKI is an infrastructure for managing public keys and establishing trust using certificates, certificate authorities, and related mechanisms.

---

## What is Kerckhoffs's principle?

A cryptosystem should remain secure even if the design and algorithm are public, with security relying on the secrecy of the key.

---

## Why is Base64 not encryption?

Base64 is an encoding mechanism designed for data representation, not confidentiality. Anyone can decode it without a secret key.

---

## Why should passwords not be encrypted for storage?

Passwords are normally verified rather than recovered. Dedicated password hashing/KDF functions such as Argon2, scrypt, bcrypt, or PBKDF2 are designed for this purpose.

---

# 80. Practical Commands

## Generate a Random Secret with OpenSSL

```bash
openssl rand -hex 32
```

This can generate random bytes represented in hexadecimal.

---

## Calculate SHA-256

```bash
echo -n "Hello" | sha256sum
```

---

## Calculate SHA-512

```bash
echo -n "Hello" | sha512sum
```

---

## Inspect a TLS Certificate

```bash
openssl s_client -connect example.com:443
```

For a more focused certificate inspection:

```bash
openssl s_client -connect example.com:443 </dev/null 2>/dev/null \
  | openssl x509 -noout -text
```

---

# 81. Practical Exercise

## Exercise 1 – Hashing

Calculate the SHA-256 hash of:

```text
Hello
```

Then calculate:

```text
hello
```

Compare the outputs.

Observe the avalanche effect:

```text
Small Input Change
        ↓
Significantly Different Digest
```

---

## Exercise 2 – Base64 vs Encryption

Encode:

```text
SecretMessage
```

using Base64.

Then decode it.

Observe:

```text
Encoding
≠
Encryption
```

---

## Exercise 3 – Random Key Generation

Generate random bytes:

```bash
openssl rand -hex 32
```

Observe that repeated executions produce different values.

---

## Exercise 4 – Certificate Inspection

Inspect a public TLS certificate:

```bash
openssl s_client -connect example.com:443 </dev/null
```

Identify:

```text
Subject
Issuer
Validity
Public Key
Signature Algorithm
Certificate Chain
```

---

# 82. Security Checklist

When evaluating a cryptographic implementation, ask:

```text
☐ Is the algorithm modern and appropriate?
☐ Is the key size appropriate?
☐ Is randomness cryptographically secure?
☐ Are keys protected?
☐ Are nonces / IVs used correctly?
☐ Is authentication provided where required?
☐ Is certificate validation enabled?
☐ Are passwords protected using a password KDF?
☐ Are secrets rotated?
☐ Are outdated algorithms disabled?
☐ Is the cryptographic library maintained?
☐ Is the implementation resistant to known misuse?
☐ Is the system designed for cryptographic migration?
```

---

# 83. Key Takeaways

Cryptography is more than encryption.

The major building blocks are:

```text
Encryption
Hashing
MACs
Digital Signatures
Key Exchange
KDFs
Randomness
Certificates
PKI
Secure Protocols
```

The most important principles are:

```text
1. Protect keys, not algorithms.
2. Use established cryptographic standards.
3. Never invent cryptography without expert review.
4. Use secure random number generation.
5. Use authenticated encryption where appropriate.
6. Never store passwords as plaintext.
7. Use dedicated password hashing/KDF algorithms.
8. Validate certificates correctly.
9. Plan for key rotation and compromise.
10. Design for cryptographic agility.
```

---

# 84. Chapter Summary

In this chapter, we established the foundation for cryptography.

We learned:

```text
Cryptography
Cryptanalysis
Cryptology
Plaintext
Ciphertext
Encryption
Decryption
Keys
Keyspace
Brute Force
Kerckhoffs's Principle
Symmetric Cryptography
Asymmetric Cryptography
Hashing
MACs
Digital Signatures
Key Exchange
KDFs
Randomness
Nonces
IVs
Salts
Certificates
PKI
Forward Secrecy
AEAD
Cryptographic Agility
Threat Modeling
```

The key idea is:

> **Cryptography is a system of mathematical primitives, keys, protocols, trust models, and implementations—not merely a method for encrypting data.**

---

# Next Chapter

## Chapter 02 – Classical Cryptography & Historical Ciphers

The next chapter explores the evolution of cryptography through classical techniques and introduces:

```text
Caesar Cipher
Substitution Ciphers
Transposition Ciphers
Affine Cipher
Vigenère Cipher
Playfair Cipher
One-Time Pad
Frequency Analysis
Brute-Force Cryptanalysis
Classical Cryptanalysis
Historical Cryptographic Systems
Limitations of Classical Cryptography
```

The chapter will establish the historical and conceptual foundation that led to modern cryptographic systems.