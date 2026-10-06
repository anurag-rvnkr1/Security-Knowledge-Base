# Chapter 04 – Asymmetric-Key Cryptography

## Overview

**Asymmetric-key cryptography**, also called **public-key cryptography**, uses a mathematically related pair of keys:

```text
Public Key
Private Key
```

Unlike symmetric cryptography, the communicating parties do not need to share the same secret key before communication begins.

A simplified model is:

```text
                 Key Pair
              ┌─────────────┐
              │             │
              ▼             ▼
         Public Key     Private Key
         Shareable       Secret
```

Asymmetric cryptography is fundamental to:

- Secure key exchange
- Digital signatures
- Digital certificates
- TLS
- PKI
- SSH
- Secure software distribution
- Identity systems
- Secure authentication

Important asymmetric algorithms and constructions include:

```text
RSA
Diffie-Hellman
ECDH
ECDSA
EdDSA
Elliptic Curve Cryptography
```

---

# 1. What is Asymmetric Cryptography?

Asymmetric cryptography uses a pair of mathematically related keys.

```text
Public Key
    │
    │ Can generally be distributed
    ▼

Private Key
    │
    │ Must remain secret
    ▼
Owner
```

The public key can be shared openly.

The private key must be protected.

---

# 2. Why Asymmetric Cryptography Exists

Symmetric cryptography has a major challenge:

```text
How do Alice and Bob securely obtain the same secret key?
```

Suppose:

```text
Alice ───── Internet ───── Bob
```

If Alice sends:

```text
Secret Key
```

an attacker may intercept it.

Asymmetric cryptography provides mechanisms that allow parties to establish shared secrets or authenticate without directly transmitting a shared secret in plaintext.

---

# 3. Basic Public-Key Model

Each participant generates:

```text
Public Key
Private Key
```

For Alice:

```text
Alice
 ├── Public Key
 └── Private Key
```

For Bob:

```text
Bob
 ├── Public Key
 └── Private Key
```

Public keys can be distributed.

Private keys remain secret.

---

# 4. Public Key

A public key is intended to be shared.

Depending on the cryptographic system, it may be used for:

```text
Encryption
Signature Verification
Key Agreement
Identity Binding
```

Examples:

```text
RSA Public Key
EC Public Key
Ed25519 Public Key
```

---

# 5. Private Key

A private key is secret cryptographic material.

Depending on the system, it may be used for:

```text
Decryption
Digital Signing
Key Agreement
Authentication
```

Examples:

```text
RSA Private Key
EC Private Key
Ed25519 Private Key
```

If a private key is compromised, the consequences can be severe.

---

# 6. Public vs Private Key

| Property | Public Key | Private Key |
|---|---|---|
| Share publicly | Yes | No |
| Confidential | Usually no | Yes |
| Used for signatures | Verification | Signing |
| Used for encryption | Encryption | Decryption |
| Used in key agreement | Public contribution | Private contribution |

The exact operations depend on the algorithm.

---

# 7. Mathematical Relationship

The public and private keys are mathematically related.

Conceptually:

```text
Private Key
     │
     │ Mathematical Transformation
     ▼
Public Key
```

However:

```text
Public Key
     ↓
Private Key
```

should be computationally infeasible to derive under the security assumptions of the cryptosystem.

This is based on mathematical problems believed to be difficult.

---

# 8. Computational Hardness

Modern public-key cryptography relies on mathematical problems that are computationally difficult.

Examples include:

```text
Integer Factorization
Discrete Logarithm
Elliptic Curve Discrete Logarithm
```

The basic idea is:

```text
Easy to compute in one direction
            ↓
Difficult to reverse without secret information
```

---

# 9. Trapdoor Functions

A trapdoor function is conceptually a function that is:

```text
Easy to compute
```

but:

```text
Difficult to reverse
```

unless special secret information is available.

Conceptually:

```text
Input
  ↓
Easy Computation
  ↓
Output

Reverse:
Output
  ↓
Computationally Difficult
```

The private key acts as the "trapdoor" in relevant constructions.

---

# 10. RSA

**RSA** is one of the best-known public-key cryptosystems.

It was introduced by:

```text
Rivest
Shamir
Adleman
```

Hence:

```text
RSA
```

RSA is based on properties related to integer factorization.

It has historically been used for:

```text
Encryption
Digital Signatures
Key Transport
Authentication
```

Modern protocols should use carefully specified RSA schemes rather than textbook RSA.

---

# 11. RSA Mathematical Foundation

RSA uses two large prime numbers:

```text
p
q
```

Calculate:

```text
n = p × q
```

The modulus:

```text
n
```

is part of the public key.

The difficulty of factoring a sufficiently large modulus into its original prime factors is central to RSA's security assumptions.

---

# 12. RSA Key Generation

A simplified educational process:

```text
Choose large primes
       ↓
      p, q
       ↓
Calculate n = p × q
       ↓
Calculate φ(n)
       ↓
Choose public exponent e
       ↓
Calculate private exponent d
       ↓
Public Key  = (n, e)
Private Key = (n, d)
```

Real RSA implementations use additional requirements and optimizations.

---

# 13. RSA Public Key

A simplified RSA public key contains:

```text
(n, e)
```

where:

```text
n = modulus
e = public exponent
```

The public key can be distributed.

---

# 14. RSA Private Key

A simplified RSA private key contains:

```text
(n, d)
```

where:

```text
d = private exponent
```

Real private keys also contain additional values used for efficient and secure implementations.

---

# 15. RSA Encryption Concept

At a simplified mathematical level:

```text
C = M^e mod n
```

where:

```text
M = message representative
e = public exponent
n = modulus
C = ciphertext
```

Decryption:

```text
M = C^d mod n
```

This is the mathematical core of textbook RSA.

However:

> **Textbook RSA should never be used directly in production.**

Secure RSA encryption requires standardized padding such as:

```text
RSA-OAEP
```

---

# 16. RSA-OAEP

**OAEP** stands for:

```text
Optimal Asymmetric Encryption Padding
```

RSA-OAEP adds randomized padding to RSA encryption.

Conceptually:

```text
Plaintext
    ↓
OAEP Encoding
    ↓
RSA
    ↓
Ciphertext
```

OAEP helps prevent attacks against deterministic textbook RSA.

---

# 17. Why Textbook RSA is Dangerous

Suppose:

```text
Same Message
+
Same Public Key
```

with textbook RSA.

The resulting ciphertext is deterministic.

Therefore:

```text
Same Plaintext
       ↓
Same Ciphertext
```

This can leak information.

Modern RSA encryption should use an appropriate randomized encoding scheme such as OAEP.

---

# 18. RSA Key Size

Common historical RSA sizes include:

```text
1024-bit
2048-bit
3072-bit
4096-bit
```

1024-bit RSA is considered too weak for modern security applications.

Common modern deployments use:

```text
2048-bit RSA
```

or larger depending on requirements.

Key size should be selected according to current standards and expected security lifetime.

---

# 19. RSA Performance

RSA is computationally expensive compared with symmetric encryption.

Therefore, RSA is generally not used to encrypt large amounts of application data directly.

Instead:

```text
RSA
 ↓
Protect / establish a small secret
 ↓
Symmetric Key
 ↓
AES-GCM
 ↓
Bulk Data
```

This is a form of:

```text
Hybrid Cryptography
```

---

# 20. RSA and Digital Signatures

RSA can also be used for digital signatures.

Conceptually:

```text
Message
   ↓
Hash
   ↓
Signature Algorithm
   +
Private Key
   ↓
Signature
```

Verification:

```text
Message
   ↓
Hash
   ↓
Verification
   +
Public Key
   ↓
Valid / Invalid
```

Modern RSA signatures should use standardized schemes such as:

```text
RSA-PSS
```

for new designs where appropriate.

---

# 21. RSA-PSS

**Probabilistic Signature Scheme (PSS)** is a modern RSA signature encoding.

Conceptually:

```text
Message
   ↓
Hash / PSS Encoding
   ↓
RSA Private-Key Operation
   ↓
Signature
```

PSS provides randomized encoding and is preferred for modern RSA signatures in many standards and applications.

---

# 22. RSA Encryption vs RSA Signature

| Operation | Key Used |
|---|---|
| RSA-OAEP Encryption | Public key |
| RSA-OAEP Decryption | Private key |
| RSA-PSS Signing | Private key |
| RSA-PSS Verification | Public key |

The underlying mathematics is related, but encryption and signatures use different standardized constructions.

---

# 23. RSA Padding

Modern RSA should not be used without appropriate padding/encoding.

Common schemes:

```text
RSA-OAEP
RSA-PSS
```

Historical schemes include:

```text
PKCS#1 v1.5 encryption/signature schemes
```

These require careful standards-based use.

---

# 24. Diffie-Hellman

**Diffie-Hellman (DH)** is a key-agreement mechanism.

Its purpose is:

> Allow two parties to establish shared secret material over an insecure communication channel.

Conceptually:

```text
Alice                         Bob
  │                             │
  │ Public Parameters           │
  │────────────────────────────>│
  │                             │
  │ Public Contribution         │
  │<────────────────────────────│
  │                             │
  └────── Shared Secret ────────┘
```

The shared secret is not directly transmitted.

---

# 25. Diffie-Hellman Concept

Alice chooses:

```text
Private value = a
```

Bob chooses:

```text
Private value = b
```

They exchange public values derived from these private values.

Both can independently calculate the same shared secret.

Conceptually:

```text
Alice:
Private a
   ↓
Public A

Bob:
Private b
   ↓
Public B

Alice + B → Shared Secret
Bob + A   → Shared Secret
```

Both arrive at the same secret.

---

# 26. Simplified Diffie-Hellman Mathematics

Choose public parameters:

```text
p = large prime
g = generator
```

Alice chooses:

```text
a = private value
```

and computes:

```text
A = g^a mod p
```

Bob chooses:

```text
b = private value
```

and computes:

```text
B = g^b mod p
```

They exchange:

```text
A
B
```

Alice calculates:

```text
S = B^a mod p
```

Bob calculates:

```text
S = A^b mod p
```

Both obtain:

```text
S = g^(ab) mod p
```

---

# 27. Diffie-Hellman Security

The attacker sees:

```text
p
g
A
B
```

but should not be able to efficiently calculate:

```text
g^(ab) mod p
```

without the private values under the relevant hardness assumptions.

This relates to the difficulty of the discrete logarithm problem and the computational Diffie-Hellman problem.

---

# 28. Diffie-Hellman Does Not Automatically Authenticate

A critical limitation:

```text
Diffie-Hellman
```

by itself does not prove who is on the other side.

An attacker can potentially perform a:

```text
Man-in-the-Middle Attack
```

unless the key exchange is authenticated.

---

# 29. Diffie-Hellman Man-in-the-Middle Attack

Conceptually:

```text
Alice ←→ Attacker ←→ Bob
```

The attacker establishes:

```text
Secret 1 with Alice
Secret 2 with Bob
```

Alice thinks she is communicating with Bob.

Bob thinks he is communicating with Alice.

Therefore:

```text
Key Exchange
≠
Authentication
```

unless an authentication mechanism is added.

---

# 30. Authenticated Key Exchange

Modern protocols combine key exchange with authentication.

For example:

```text
Diffie-Hellman
      +
Digital Signature
      +
Certificate
      ↓
Authenticated Key Exchange
```

TLS is a major example.

---

# 31. Ephemeral Diffie-Hellman

Ephemeral Diffie-Hellman uses temporary key pairs.

Conceptually:

```text
Session 1 → Ephemeral Key Pair A
Session 2 → Ephemeral Key Pair B
Session 3 → Ephemeral Key Pair C
```

The keys are not reused indefinitely.

This supports:

```text
Forward Secrecy
```

when used appropriately.

---

# 32. Forward Secrecy

Forward secrecy means that compromise of a long-term private key should not automatically allow decryption of previously captured sessions.

Conceptually:

```text
Long-Term Authentication Key
          │
          ▼
Authenticate Session
          │
          ▼
Ephemeral Key Exchange
          │
          ▼
Session Key
          │
          ▼
Encrypted Data
```

If the long-term key is later compromised:

```text
Past ephemeral session keys
        ↓
Remain protected
```

assuming the protocol and implementation provide forward secrecy and ephemeral secrets were not separately compromised.

---

# 33. ECDH

**Elliptic Curve Diffie-Hellman (ECDH)** is a key agreement mechanism based on elliptic curve cryptography.

Conceptually:

```text
Alice Private Key
        ↓
Alice Public Key

Bob Private Key
        ↓
Bob Public Key

Exchange Public Keys
        ↓
ECDH
        ↓
Shared Secret
```

ECDH provides the same general purpose as DH but uses elliptic-curve mathematics.

---

# 34. Why ECC?

Elliptic Curve Cryptography can provide strong security with relatively small key sizes.

This can result in:

```text
Smaller Keys
Smaller Certificates
Lower Bandwidth
Lower Storage Requirements
Efficient Operations
```

ECC is widely used in modern protocols.

---

# 35. Elliptic Curve Cryptography

ECC is based on mathematical operations involving points on elliptic curves over finite fields.

Conceptually:

```text
Private Scalar
      ↓
Elliptic Curve Operation
      ↓
Public Point
```

The security relies on the difficulty of solving the elliptic curve discrete logarithm problem for appropriately selected curves.

---

# 36. Elliptic Curve Concept

An elliptic curve can be represented mathematically in a simplified form such as:

```text
y² = x³ + ax + b
```

over an appropriate finite field.

Cryptographic ECC does not operate on ordinary real-number graphs.

It operates over finite mathematical structures.

---

# 37. ECC Point Operations

Important operations include:

```text
Point Addition
Point Doubling
Scalar Multiplication
```

The most important operation is:

```text
k × P
```

where:

```text
k = private scalar
P = public base point
```

This produces another point on the curve.

---

# 38. ECC Security Concept

An attacker may know:

```text
P
Q = kP
```

but should not be able to efficiently recover:

```text
k
```

This is related to the elliptic curve discrete logarithm problem.

---

# 39. Common ECC Curves

Common curves and curve families include:

```text
secp256k1
P-256
X25519
Ed25519
```

Their purposes differ.

For example:

```text
X25519 → Key Agreement
Ed25519 → Digital Signatures
```

---

# 40. X25519

**X25519** is a modern elliptic-curve Diffie-Hellman function based on Curve25519.

It is widely used for:

```text
Key Agreement
TLS
Secure Messaging
Modern Cryptographic Protocols
```

It is designed to provide efficient and secure key exchange.

---

# 41. Ed25519

**Ed25519** is a digital signature scheme based on Edwards-curve cryptography.

It provides:

```text
Signing
Verification
Authentication
Integrity
```

Conceptually:

```text
Private Key
    ↓
Signature

Public Key
    ↓
Signature Verification
```

---

# 42. ECDSA

**ECDSA** stands for:

```text
Elliptic Curve Digital Signature Algorithm
```

It is used for digital signatures.

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

Verification uses the public key.

---

# 43. ECDSA Nonce Security

ECDSA requires careful handling of its per-signature nonce.

If the nonce is:

```text
Reused
Predictable
Leaked
Weakly Generated
```

the private key may be recoverable in certain attack scenarios.

This is a classic example of:

```text
Strong Algorithm
+
Bad Randomness
=
Compromised Security
```

---

# 44. RSA vs ECC

| Property | RSA | ECC |
|---|---|---|
| Mathematical basis | Integer factorization | Elliptic-curve discrete logarithm |
| Key size for comparable security | Larger | Smaller |
| Performance | Depends on operation | Often efficient |
| Common uses | Signatures, legacy encryption | Key exchange, signatures |
| Modern examples | RSA-PSS, RSA-OAEP | ECDH, ECDSA, Ed25519 |

Security equivalence depends on the exact algorithm and security level.

---

# 45. RSA vs ECDH

RSA and ECDH should not be treated as interchangeable.

```text
RSA
→ Can support encryption and signatures.

ECDH
→ Key agreement.
```

For example:

```text
RSA-PSS
→ Digital signatures

RSA-OAEP
→ Public-key encryption

ECDH
→ Key agreement
```

---

# 46. RSA vs ECDSA

```text
RSA-PSS
→ RSA digital signatures

ECDSA
→ Elliptic-curve digital signatures
```

Both can provide signatures, but they use different mathematical foundations and key formats.

---

# 47. Public-Key Encryption vs Key Exchange

These are different concepts.

### Public-Key Encryption

```text
Encrypt
using recipient's
public key
```

Example:

```text
RSA-OAEP
```

### Key Exchange

```text
Two parties
derive shared secret
```

Example:

```text
ECDH
```

Modern protocols often favor ephemeral key agreement rather than using RSA encryption for session-key establishment.

---

# 48. Hybrid Cryptography

A practical secure communication architecture often looks like:

```text
Client
  │
  │ Public-Key / Key Agreement
  ▼
Shared Session Secret
  │
  ▼
KDF
  │
  ▼
Session Keys
  │
  ▼
AES-GCM / ChaCha20-Poly1305
  │
  ▼
Application Data
```

This combines:

```text
Asymmetric Cryptography
+
Symmetric Cryptography
```

---

# 49. Key Derivation After ECDH

ECDH produces shared secret material.

Applications generally should not simply use the raw ECDH output directly as an encryption key.

Instead:

```text
ECDH Shared Secret
       ↓
KDF / HKDF
       ↓
Derived Session Keys
```

This provides better key separation and protocol context binding.

---

# 50. Public-Key Certificates

A public key needs a way to be associated with an identity.

Certificates provide this binding.

Conceptually:

```text
Identity
   +
Public Key
   +
CA Signature
   ↓
Certificate
```

Example:

```text
example.com
     +
Public Key
     ↓
TLS Certificate
```

---

# 51. Certificate Authority

A **Certificate Authority (CA)** signs certificates.

Simplified:

```text
Root CA
   ↓
Intermediate CA
   ↓
Server Certificate
   ↓
example.com
```

The client verifies the certificate chain against trusted roots.

PKI is covered in detail in Chapter 07.

---

# 52. Public-Key Infrastructure

PKI manages:

```text
Public Keys
Private Keys
Certificates
Certificate Authorities
Trust Chains
Revocation
Validation
```

It is essential to many enterprise and Internet security systems.

---

# 53. SSH and Asymmetric Cryptography

SSH uses public-key cryptography for authentication and key establishment.

Conceptually:

```text
Client
   │
   │ Public-Key Authentication
   ▼
SSH Server
```

A user's private key remains on the client.

The server stores the corresponding public key.

---

# 54. Software Signing

Digital signatures can verify that software originated from an expected signing identity and was not modified after signing.

Conceptually:

```text
Software
   ↓
Hash
   ↓
Private Key
   ↓
Signature
```

Verification:

```text
Software
   +
Signature
   +
Public Key
   ↓
Valid / Invalid
```

---

# 55. Secure Boot

Secure Boot mechanisms can use cryptographic signatures to verify software components before execution.

Conceptually:

```text
Firmware
   ↓
Verify Bootloader Signature
   ↓
Verify Operating System
   ↓
Verify Components
   ↓
Boot
```

This helps establish a chain of trust.

---

# 56. Digital Identity

Public-key cryptography can support identity systems.

Example:

```text
Private Key
     ↓
Proof of Possession
     ↓
Authentication
```

The private key does not need to be transmitted.

This is an important advantage of public-key authentication.

---

# 57. Proof of Possession

A server can challenge a client to prove possession of a private key.

Conceptually:

```text
Server
   ↓
Challenge
   ↓
Client
   ↓
Sign Challenge
   ↓
Server
   ↓
Verify Signature
```

The private key itself is never sent to the server.

---

# 58. Asymmetric Cryptography and TLS

A simplified TLS architecture:

```text
Client
   │
   │ Server Certificate
   ▼
Authenticate Server
   │
   ▼
Ephemeral Key Exchange
   │
   ▼
Shared Secret
   │
   ▼
KDF
   │
   ▼
Session Keys
   │
   ▼
AES-GCM / ChaCha20-Poly1305
```

Modern TLS generally uses ephemeral key agreement for forward secrecy.

---

# 59. Asymmetric Cryptography Does Not Replace Symmetric Cryptography

Asymmetric algorithms are generally not used to encrypt every byte of a large file or network stream.

Instead:

```text
Asymmetric
    ↓
Establish / authenticate
    ↓
Symmetric
    ↓
Encrypt bulk data
```

This architecture is both efficient and secure when implemented correctly.

---

# 60. Man-in-the-Middle Attack

A public-key system must authenticate public keys appropriately.

Otherwise:

```text
Alice
  │
  ▼
Attacker
  │
  ▼
Bob
```

The attacker can substitute their own public key.

Therefore:

```text
Key Exchange
+
Authentication
=
Secure Communication
```

---

# 61. Certificate Validation

When connecting to:

```text
https://example.com
```

a client should validate relevant certificate properties such as:

```text
Certificate Chain
Signature
Validity Period
Subject / SAN
Trusted Issuer
Key Usage
Basic Constraints
```

Incorrect certificate validation can enable serious attacks.

---

# 62. Public Key Pinning

Historically, some applications used public-key pinning to restrict which keys were trusted.

However, traditional browser HTTP Public Key Pinning (HPKP) is deprecated and should not be introduced for modern web applications.

Modern systems should follow current platform and protocol guidance for certificate trust.

---

# 63. Private Key Protection

Private keys should be protected using appropriate mechanisms.

Examples:

```text
File Permissions
Encrypted Key Storage
Hardware Security Modules
Trusted Platform Modules
Secure Enclaves
Cloud KMS
Hardware-backed Keystores
```

The appropriate mechanism depends on the threat model.

---

# 64. Private Key Compromise

If a private key is compromised:

```text
Attacker obtains Private Key
          ↓
Potential Impersonation
          ↓
Potential Signature Forgery
          ↓
Potential Decryption
```

The exact impact depends on what the key is used for.

Possible response:

```text
Revoke
Rotate
Replace
Investigate
Assess Exposure
```

---

# 65. Key Lifecycle

Public-key infrastructure requires lifecycle management:

```text
Generate
   ↓
Register
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

# 66. Key Separation

Do not unnecessarily reuse one private key for unrelated functions.

For example:

```text
Signing Key
      ≠
Encryption Key
      ≠
Key Exchange Key
```

Using separate keys can limit the impact of compromise and simplify security management.

---

# 67. RSA Attacks

RSA can be vulnerable to problems such as:

```text
Small / weak keys
Bad padding
Textbook RSA
Weak randomness
Poor implementation
Side-channel attacks
Improper key generation
Oracle attacks
```

Modern standardized padding and secure implementations are essential.

---

# 68. RSA Padding Oracle

Some historical RSA padding schemes can be vulnerable to oracle attacks if an application leaks information about whether decrypted ciphertext has valid padding.

Conceptually:

```text
Attacker
   ↓
Modified Ciphertext
   ↓
Server
   ├── Valid
   └── Invalid
```

Different responses can reveal information.

Secure applications should use modern constructions and avoid exposing decryption oracles.

---

# 69. Bleichenbacher Attack

The **Bleichenbacher attack** is a well-known class of attacks against vulnerable RSA PKCS#1 v1.5 decryption implementations.

It demonstrated that:

```text
Cryptographic Algorithm
+
Incorrect Protocol Behavior
=
Practical Vulnerability
```

The broader lesson is to use modern standardized constructions such as RSA-OAEP where appropriate and to handle failures safely.

---

# 70. Small Exponent Problems

Poorly designed RSA systems using small public exponents without proper randomized encoding can be vulnerable to attacks.

This is another reason:

```text
Do not use textbook RSA.
```

Use standardized padding such as:

```text
RSA-OAEP
RSA-PSS
```

for appropriate purposes.

---

# 71. ECC Attacks

ECC implementations can fail because of:

```text
Weak Randomness
Invalid Curve Handling
Small-Subgroup Problems
Nonce Reuse
Side Channels
Bad Parameter Validation
Weak Curves
Implementation Bugs
```

The mathematical security of the curve does not protect a flawed implementation.

---

# 72. ECDSA Nonce Reuse Attack

Suppose an ECDSA signing nonce is reused incorrectly.

Conceptually:

```text
Signature 1
   +
Signature 2
   +
Same Nonce
   ↓
Private Key Recovery
```

This has happened in real-world systems.

Therefore:

```text
Secure Nonce Generation
```

is critical for ECDSA.

---

# 73. Deterministic ECDSA

Some systems use deterministic nonce generation for ECDSA, such as the approach specified in RFC 6979.

Conceptually:

```text
Private Key
+
Message
   ↓
Deterministic Nonce
   ↓
ECDSA Signature
```

This can reduce dependence on external randomness during signing, although implementations still need to be correct and securely designed.

---

# 74. Side-Channel Attacks Against Public-Key Crypto

Attackers may exploit:

```text
Timing
Cache
Power
Memory Access
Faults
```

to recover secret information.

Therefore:

```text
Constant-Time Implementations
+
Secure Libraries
+
Hardware Protections
```

may be required.

---

# 75. Quantum Computing Threat

Large-scale quantum computers could threaten widely used public-key systems.

Shor's algorithm could theoretically break cryptosystems based on:

```text
Integer Factorization
Discrete Logarithms
Elliptic Curve Discrete Logarithms
```

This affects:

```text
RSA
Diffie-Hellman
ECDH
ECDSA
EdDSA
```

under sufficiently capable quantum computers.

Symmetric cryptography is affected differently.

---

# 76. Quantum Impact on Symmetric Cryptography

Grover's algorithm provides a theoretical quadratic speedup for unstructured search.

This means that, roughly speaking:

```text
n-bit symmetric key
```

may offer around:

```text
n/2 bits
```

of brute-force security against an idealized quantum search.

This is one reason larger symmetric keys such as AES-256 are relevant for long-term security planning.

---

# 77. Post-Quantum Cryptography

Post-quantum cryptography (PQC) aims to provide security against attackers equipped with quantum computers while running on conventional computers.

Modern PQC includes standardized families such as:

```text
ML-KEM
ML-DSA
SLH-DSA
```

These will be discussed in detail in Chapter 12.

---

# 78. Crypto-Agility

Systems should be able to transition between algorithms.

Conceptually:

```text
RSA / ECC
    ↓
Hybrid Transition
    ↓
Post-Quantum Algorithms
```

This requires:

```text
Algorithm Abstraction
Key Versioning
Certificate Updates
Protocol Support
Migration Planning
```

---

# 79. Asymmetric Cryptography Checklist

```text
☐ Protect private keys
☐ Use appropriate key sizes
☐ Use standardized algorithms
☐ Use RSA-OAEP for appropriate RSA encryption use cases
☐ Use RSA-PSS for appropriate RSA signatures
☐ Prefer modern elliptic-curve constructions where appropriate
☐ Use authenticated key exchange
☐ Validate certificates
☐ Use secure randomness
☐ Protect signing nonces
☐ Plan for key rotation
☐ Separate keys by purpose
☐ Consider post-quantum migration
```

---

# 80. Common Mistakes

```text
❌ Sharing private keys
❌ Using textbook RSA
❌ Using RSA without proper padding
❌ Using weak RSA key sizes
❌ Reusing ECDSA nonces
❌ Trusting unauthenticated Diffie-Hellman
❌ Skipping certificate validation
❌ Hard-coding private keys
❌ Reusing one key for unrelated purposes
❌ Implementing RSA/ECC mathematics manually
```

---

# 81. Practical OpenSSL – Generate RSA Key

Generate a 2048-bit RSA private key:

```bash
openssl genpkey \
    -algorithm RSA \
    -pkeyopt rsa_keygen_bits:2048 \
    -out private-key.pem
```

Extract the public key:

```bash
openssl pkey \
    -in private-key.pem \
    -pubout \
    -out public-key.pem
```

---

# 82. Inspect RSA Key

```bash
openssl pkey \
    -in private-key.pem \
    -text \
    -noout
```

Public key:

```bash
openssl pkey \
    -pubin \
    -in public-key.pem \
    -text \
    -noout
```

---

# 83. Generate an EC Private Key

For a commonly used NIST curve:

```bash
openssl genpkey \
    -algorithm EC \
    -pkeyopt ec_paramgen_curve:P-256 \
    -out ec-private-key.pem
```

Extract the public key:

```bash
openssl pkey \
    -in ec-private-key.pem \
    -pubout \
    -out ec-public-key.pem
```

---

# 84. Generate an Ed25519 Key

Where supported:

```bash
openssl genpkey \
    -algorithm ED25519 \
    -out ed25519-private.pem
```

Extract the public key:

```bash
openssl pkey \
    -in ed25519-private.pem \
    -pubout \
    -out ed25519-public.pem
```

---

# 85. Generate X25519 Key Material

OpenSSL versions with X25519 support can generate an X25519 private key:

```bash
openssl genpkey \
    -algorithm X25519 \
    -out x25519-private.pem
```

X25519 is used for key agreement rather than digital signatures.

---

# 86. RSA Signing with OpenSSL

Create a file:

```bash
echo "Hello Cryptography" > message.txt
```

Sign using RSA-PSS:

```bash
openssl dgst \
    -sha256 \
    -sign private-key.pem \
    -out signature.bin \
    message.txt
```

Verification:

```bash
openssl dgst \
    -sha256 \
    -verify public-key.pem \
    -signature signature.bin \
    message.txt
```

For production use, ensure the chosen command and parameters match the required signature scheme and current OpenSSL behavior.

---

# 87. Practical Python – RSA Concept

Using a well-maintained cryptographic library:

```python
from cryptography.hazmat.primitives.asymmetric import rsa

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
)

public_key = private_key.public_key()
```

The library performs the difficult cryptographic implementation work.

---

# 88. Practical Python – RSA-PSS Signature

```python
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

message = b"Hello Cryptography"

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

# 89. Practical Python – ECDH Concept

Using a vetted library:

```python
from cryptography.hazmat.primitives.asymmetric import ec

alice_private = ec.generate_private_key(ec.SECP256R1())
bob_private = ec.generate_private_key(ec.SECP256R1())

alice_public = alice_private.public_key()
bob_public = bob_private.public_key()

alice_shared = alice_private.exchange(
    ec.ECDH(),
    bob_public,
)

bob_shared = bob_private.exchange(
    ec.ECDH(),
    alice_public,
)

assert alice_shared == bob_shared

print("Shared secret established")
```

In a real protocol, the resulting secret should normally be processed through an appropriate KDF before being used as key material.

---

# 90. Practical Exercise – RSA

Generate:

```text
RSA private key
RSA public key
```

Then:

```text
1. Inspect the public key.
2. Inspect the private key.
3. Sign a message.
4. Verify the signature.
5. Modify the message.
6. Verify again.
```

Observe:

```text
Original Message
→ Signature Valid

Modified Message
→ Signature Invalid
```

---

# 91. Practical Exercise – ECDH

Create:

```text
Alice private key
Alice public key

Bob private key
Bob public key
```

Perform:

```text
Alice private + Bob public
```

and:

```text
Bob private + Alice public
```

Verify:

```text
Shared Secret A
=
Shared Secret B
```

Then derive an encryption key using a KDF.

---

# 92. Practical Exercise – Certificate Inspection

Inspect a public TLS certificate:

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com
```

Identify:

```text
Subject
Issuer
Public Key Algorithm
Signature Algorithm
Validity
SAN
Certificate Chain
```

---

# 93. VAPT Testing Workflow

When assessing asymmetric cryptography:

```text
Identify Algorithm
       ↓
Identify Key Size
       ↓
Inspect Certificate
       ↓
Inspect Key Usage
       ↓
Check Certificate Validation
       ↓
Check Signature Algorithms
       ↓
Check TLS Configuration
       ↓
Check Private-Key Protection
       ↓
Check Deprecated Algorithms
       ↓
Assess Key Lifecycle
```

---

# 94. Example VAPT Findings

Potential issues include:

```text
Weak RSA Key Size
Weak Certificate Signature
Expired Certificate
Invalid Certificate Chain
Hostname Validation Disabled
Weak TLS Configuration
Insecure RSA Padding
ECDSA Nonce Reuse
Exposed Private Key
Hard-Coded Private Key
Unsupported / Deprecated Algorithms
```

---

# 95. Asymmetric Cryptography in SOC

SOC analysts may encounter:

```text
Certificate Alerts
TLS Handshake Failures
Unexpected Certificates
Private-Key Exposure
Certificate Expiration
Suspicious Signing Activity
SSH Key Abuse
Code-Signing Anomalies
```

Understanding public-key cryptography helps analysts interpret these events.

---

# 96. Asymmetric Cryptography in Cloud Security

Cloud systems commonly use:

```text
KMS
HSM
Certificates
Key Pairs
Identity Systems
Secrets Management
Envelope Encryption
```

Public-key cryptography may be used for:

```text
Authentication
Certificates
Key Exchange
Software Signing
```

---

# 97. Asymmetric Cryptography in Zero Trust

Zero Trust architectures commonly use:

```text
Certificates
Public-Key Authentication
Mutual TLS
Short-Lived Credentials
Digital Signatures
Key Rotation
```

Conceptually:

```text
Identity
   ↓
Certificate / Key
   ↓
Authentication
   ↓
Authorization
   ↓
Encrypted Communication
```

---

# 98. Symmetric + Asymmetric Architecture

A typical modern architecture:

```text
                 Certificate / Identity
                         │
                         ▼
                    Authentication
                         │
                         ▼
                 ECDH / Key Agreement
                         │
                         ▼
                       HKDF
                         │
                         ▼
                   Session Keys
                         │
                         ▼
                AES-GCM / ChaCha20
                         │
                         ▼
                   Application Data
```

This architecture demonstrates why modern cryptography uses multiple primitives together.

---

# 99. Important Distinction

Remember:

```text
RSA
```

is not simply:

```text
"Encryption"
```

RSA can support multiple cryptographic operations depending on the standardized scheme.

Similarly:

```text
ECC
```

is a broader family of techniques.

Examples:

```text
ECDH → Key Agreement
ECDSA → Digital Signatures
Ed25519 → Digital Signatures
X25519 → Key Agreement
```

---

# 100. Common Interview Questions

## What is asymmetric cryptography?

Asymmetric cryptography uses mathematically related public and private keys to support operations such as encryption, digital signatures, and key agreement.

---

## Why is asymmetric cryptography slower than symmetric cryptography?

Public-key operations generally involve more computationally expensive mathematical operations than symmetric encryption.

---

## What is RSA?

RSA is a public-key cryptosystem based on mathematical properties related to integer factorization and can support encryption and digital signatures using appropriate standardized schemes.

---

## What is Diffie-Hellman?

Diffie-Hellman is a key-agreement mechanism that allows two parties to derive shared secret material over an insecure channel.

---

## Does Diffie-Hellman authenticate users?

No. Plain Diffie-Hellman does not inherently authenticate the participants and can be vulnerable to man-in-the-middle attacks without an authentication mechanism.

---

## What is ECDH?

ECDH is an elliptic-curve-based key agreement mechanism.

---

## What is ECDSA?

ECDSA is an elliptic-curve digital signature algorithm.

---

## What is Ed25519?

Ed25519 is a modern digital signature scheme based on Edwards-curve cryptography.

---

## What is X25519?

X25519 is an elliptic-curve Diffie-Hellman function used for key agreement.

---

## What is forward secrecy?

Forward secrecy is a property where compromise of long-term authentication keys does not automatically expose previously established session keys.

---

## Why is RSA not normally used for bulk encryption?

RSA is computationally expensive and has limitations on the amount of data it can encrypt under a given key and padding scheme. Symmetric encryption is much more efficient for bulk data.

---

## What is hybrid encryption?

Hybrid encryption combines asymmetric cryptography for key establishment or protection with symmetric cryptography for efficient bulk encryption.

---

## Why is RSA-OAEP used?

RSA-OAEP provides randomized encoding for RSA encryption and is designed to avoid weaknesses of deterministic textbook RSA.

---

## Why is RSA-PSS used?

RSA-PSS provides a modern randomized encoding for RSA digital signatures.

---

## Why is ECDSA nonce reuse dangerous?

Reusing or predictably generating the per-signature nonce can expose enough mathematical information to recover the private signing key in vulnerable implementations.

---

# 101. Quick Revision Table

| Concept | Primary Purpose |
|---|---|
| Public Key | Shareable cryptographic information |
| Private Key | Secret cryptographic material |
| RSA | Encryption / signatures |
| RSA-OAEP | RSA encryption |
| RSA-PSS | RSA signatures |
| Diffie-Hellman | Key agreement |
| ECDH | Elliptic-curve key agreement |
| ECC | Family of elliptic-curve cryptographic techniques |
| ECDSA | Digital signatures |
| Ed25519 | Digital signatures |
| X25519 | Key agreement |
| Certificate | Identity ↔ public key binding |
| CA | Certificate issuer / trust anchor infrastructure |
| PKI | Public-key trust infrastructure |
| Forward Secrecy | Limits impact of long-term key compromise |
| Hybrid Encryption | Asymmetric + symmetric cryptography |
| KDF | Derives usable keys from secret material |

---

# 102. Key Takeaways

```text
1. Asymmetric cryptography uses public/private key pairs.

2. Public keys can generally be shared; private keys must remain protected.

3. RSA is based on mathematical problems related to integer factorization.

4. Textbook RSA should never be used in production.

5. RSA-OAEP is used for appropriate RSA encryption applications.

6. RSA-PSS is used for modern RSA signatures.

7. Diffie-Hellman provides key agreement rather than authentication.

8. ECDH provides elliptic-curve key agreement.

9. ECDSA and Ed25519 provide digital signatures.

10. X25519 provides modern elliptic-curve key agreement.

11. Key exchange should be authenticated to prevent MITM attacks.

12. Ephemeral key exchange can provide forward secrecy.

13. RSA/ECC are generally not used for bulk data encryption.

14. Modern systems combine asymmetric cryptography with symmetric AEAD.

15. Private-key protection is critical.

16. Secure randomness is essential for many public-key operations.

17. ECDSA nonce failures can expose private keys.

18. Certificate validation establishes trust in public keys.

19. Public-key cryptography is fundamental to TLS, SSH, PKI, and secure identity.

20. Quantum computing creates long-term risks for RSA and ECC.
```

---

# 103. Chapter Summary

This chapter introduced public-key cryptography and its major applications.

We covered:

```text
Asymmetric Cryptography
Public Keys
Private Keys
Computational Hardness
Trapdoor Functions
RSA
RSA Key Generation
RSA Encryption
RSA-OAEP
RSA-PSS
RSA Signatures
Diffie-Hellman
ECDH
ECC
X25519
ECDSA
Ed25519
Hybrid Encryption
Key Agreement
Forward Secrecy
Certificates
PKI
Certificate Validation
MITM Attacks
Private-Key Protection
Key Lifecycle
Side-Channel Attacks
Quantum Threats
Post-Quantum Migration
```

The central principle is:

> **Asymmetric cryptography solves problems that shared-secret cryptography alone cannot solve efficiently, particularly key establishment and public-key authentication.**

However, asymmetric cryptography is normally combined with symmetric cryptography rather than replacing it:

```text
Asymmetric Cryptography
          ↓
Authentication / Key Agreement
          ↓
Symmetric Session Keys
          ↓
AEAD
          ↓
Secure Data Communication
```

---

# Next Chapter

## Chapter 05 – Hash Functions & Message Integrity

The next chapter focuses on cryptographic hash functions and will cover:

```text
Cryptographic Hash Functions
Hash Properties
Preimage Resistance
Second-Preimage Resistance
Collision Resistance
Avalanche Effect
SHA-1
SHA-2
SHA-256
SHA-384
SHA-512
SHA-3
MD5
Hash Collisions
Length-Extension Attacks
Hash-Based Integrity
Password Hashing
Salts
Hashing vs Encryption
Practical Hashing
Security Applications
```

The key question for the next chapter will be:

> **How can a system produce a compact cryptographic fingerprint of data and detect whether that data has changed?**