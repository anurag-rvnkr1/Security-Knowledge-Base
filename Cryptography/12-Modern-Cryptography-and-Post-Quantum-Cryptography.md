# Chapter 12 – Modern Cryptography & Post-Quantum Cryptography

## Overview

Modern cryptography is evolving rapidly.

Traditional cryptographic systems continue to protect:

```text
Web Applications
APIs
Cloud Infrastructure
Mobile Applications
Banking Systems
VPNs
Messaging Systems
Digital Identity
Software Updates
IoT
```

However, advances in:

```text
Quantum Computing
Cloud Computing
AI-Assisted Attacks
Hardware Acceleration
Distributed Computing
```

are changing the cryptographic threat landscape.

The most important long-term concern is:

```text
Quantum Computing
        ↓
Threat to Current Public-Key Cryptography
        ↓
Need for Post-Quantum Cryptography
```

This chapter covers modern cryptographic technologies and explains how organizations can prepare for the transition to post-quantum cryptography.

---

# 1. Modern Cryptography

Modern cryptography is built around several major primitives:

```text
Symmetric Encryption
Hash Functions
MACs
Digital Signatures
Key Exchange
KDFs
Randomness
Authenticated Encryption
```

Modern systems combine these primitives into protocols.

---

# 2. Modern Cryptographic Stack

A simplified architecture:

```text
Application
     │
     ▼
Security Protocol
     │
     ├── Authentication
     ├── Key Exchange
     ├── Encryption
     ├── Integrity
     └── Key Derivation
              │
              ▼
       Cryptographic Primitives
```

---

# 3. Cryptographic Agility

**Cryptographic agility** means designing systems so cryptographic algorithms can be changed without completely redesigning the application.

For example:

```text
Current:
ECDHE + AES-GCM

Future:
PQC KEM + AES-GCM
```

A cryptographically agile system can make this transition with limited architectural changes.

---

# 4. Why Cryptographic Agility Matters

Algorithms can become obsolete because of:

```text
New Attacks
Performance Requirements
Compliance Requirements
Quantum Computing
Implementation Vulnerabilities
Protocol Changes
```

Therefore:

> **Cryptographic algorithms should not be permanently hard-coded into system architecture.**

---

# 5. Modern Symmetric Cryptography

Important modern primitives include:

```text
AES
ChaCha20
Poly1305
SHA-2
SHA-3
HMAC
HKDF
```

These remain important even in a post-quantum world.

---

# 6. AES

AES remains one of the primary symmetric encryption standards.

Common variants:

```text
AES-128
AES-192
AES-256
```

Modern applications should generally use secure authenticated modes such as:

```text
AES-GCM
```

rather than unsafe or outdated constructions.

---

# 7. ChaCha20-Poly1305

ChaCha20-Poly1305 combines:

```text
ChaCha20
+
Poly1305
```

to provide:

```text
Confidentiality
+
Integrity
```

It is particularly useful on systems where AES hardware acceleration is unavailable or undesirable.

---

# 8. Modern Hash Functions

Important modern hash families include:

```text
SHA-256
SHA-384
SHA-512
SHA-3
SHAKE
BLAKE2
BLAKE3
```

The appropriate choice depends on:

```text
Protocol
Security Requirement
Performance
Compatibility
Standardization
```

---

# 9. SHA-3

SHA-3 is based on:

```text
Keccak
```

and uses a different internal construction from SHA-2.

SHA-3 provides an alternative standardized hash family.

---

# 10. SHAKE

SHAKE functions are extendable-output functions:

```text
SHAKE128
SHAKE256
```

Unlike fixed-output hashes, they can produce variable-length output.

They are useful in several modern cryptographic constructions.

---

# 11. Modern Digital Signatures

Important modern signature families include:

```text
RSA
ECDSA
EdDSA
Ed25519
Ed448
```

However, RSA and elliptic-curve signatures are vulnerable to sufficiently capable quantum computers.

This is one reason post-quantum signatures are being standardized.

---

# 12. Ed25519

Ed25519 is a modern elliptic-curve signature scheme.

It is widely valued for:

```text
Fast Signing
Fast Verification
Small Keys
Small Signatures
Deterministic Signing
Good Software APIs
```

It is still vulnerable to large-scale quantum attacks because it relies on elliptic-curve discrete-logarithm security.

---

# 13. X25519

X25519 is commonly used for elliptic-curve Diffie-Hellman key agreement.

Conceptually:

```text
Client Private Key
+
Server Public Key
        ↓
Shared Secret
```

It is widely used in modern secure protocols.

---

# 14. Modern KDFs

Important key-derivation mechanisms include:

```text
HKDF
Argon2
scrypt
PBKDF2
```

Their purposes differ.

### HKDF

Used primarily for cryptographic key derivation and key separation.

### Argon2 / scrypt / PBKDF2

Primarily used for password-based key derivation.

---

# 15. Key Separation

A secure system should avoid using one key for unrelated purposes.

Instead:

```text
Master Secret
      ↓
     KDF
      ↓
 ┌────┼────┐
 ▼    ▼    ▼
Key A Key B Key C
```

For example:

```text
Encryption Key
Authentication Key
Export Key
```

---

# 16. Domain Separation

Domain separation prevents the same cryptographic output from unintentionally being reused across different purposes.

Conceptually:

```text
Master Key
   ↓
KDF("encryption")
   ↓
Encryption Key

Master Key
   ↓
KDF("authentication")
   ↓
Authentication Key
```

---

# 17. Authenticated Encryption

Modern applications should generally prefer:

```text
AEAD
```

Examples:

```text
AES-GCM
ChaCha20-Poly1305
```

AEAD provides:

```text
Confidentiality
+
Integrity
+
Authentication of Associated Data
```

---

# 18. Associated Data

AEAD can authenticate data without encrypting it.

For example:

```text
Encrypted:
Message

Authenticated but visible:
User ID
Protocol Version
Message Type
```

This is called:

```text
Associated Data
```

---

# 19. Modern Key Exchange

Modern systems commonly use:

```text
ECDHE
X25519
```

These provide efficient ephemeral key agreement and forward secrecy.

However:

```text
ECC
+
RSA
```

are not resistant to sufficiently powerful quantum computers.

---

# 20. Quantum Computing

Quantum computers operate using:

```text
Qubits
```

rather than only classical bits.

A classical bit:

```text
0 or 1
```

A qubit can exist in a quantum superposition of states.

Quantum computers exploit:

```text
Superposition
Entanglement
Interference
```

to solve certain problems differently from classical computers.

---

# 21. Why Quantum Computing Matters to Cryptography

Quantum algorithms threaten some mathematical assumptions used by modern public-key cryptography.

The most important algorithm is:

```text
Shor's Algorithm
```

---

# 22. Shor's Algorithm

Shor's algorithm can theoretically solve:

```text
Integer Factorization
Discrete Logarithms
```

efficiently on a sufficiently powerful fault-tolerant quantum computer.

This threatens:

```text
RSA
Diffie-Hellman
ECDH
ECDSA
Ed25519
```

and other systems based on related mathematical problems.

---

# 23. RSA and Quantum Computing

RSA relies on the difficulty of:

```text
Integer Factorization
```

Classically:

```text
Large Integer
 ↓
Difficult to Factor
```

With a sufficiently powerful quantum computer:

```text
Shor's Algorithm
 ↓
Efficient Factorization
```

Therefore RSA is not considered post-quantum secure.

---

# 24. ECC and Quantum Computing

ECC relies on the difficulty of:

```text
Elliptic Curve Discrete Logarithm Problem
```

Shor's algorithm also threatens this problem.

Therefore:

```text
ECDSA
ECDH
Ed25519
X25519
```

are not post-quantum algorithms.

---

# 25. Grover's Algorithm

Grover's algorithm provides a quadratic speedup for certain brute-force search problems.

For an ideal n-bit symmetric key:

```text
Classical Search:
≈ 2^n

Quantum Search:
≈ 2^(n/2)
```

This does not mean AES is immediately broken.

---

# 26. Quantum Impact on AES

Conceptually:

```text
AES-128
 ↓
Quantum search ≈ 2^64

AES-256
 ↓
Quantum search ≈ 2^128
```

Therefore AES-256 provides a larger security margin against generic quantum search.

Real-world quantum attack costs are more complicated than this simplified model.

---

# 27. Quantum Impact on Hashes

Grover-like attacks can reduce the effective brute-force security of hash preimage searches.

For example:

```text
SHA-256
```

has approximately:

```text
128-bit classical preimage security
```

and a simplified quantum-search estimate of roughly:

```text
64-bit
```

against generic preimage search.

Hash collision security follows different considerations.

---

# 28. Symmetric vs Asymmetric Quantum Threat

| Cryptography | Quantum Impact |
|---|---|
| AES | Reduced security margin |
| SHA-256 | Reduced generic search security |
| SHA-3 | Reduced generic search security |
| RSA | Fundamentally threatened |
| DH | Fundamentally threatened |
| ECDH | Fundamentally threatened |
| ECDSA | Fundamentally threatened |
| Ed25519 | Fundamentally threatened |

This distinction is critical.

---

# 29. Post-Quantum Cryptography

**Post-Quantum Cryptography (PQC)** refers to cryptographic algorithms designed to resist attacks from both:

```text
Classical Computers
+
Cryptographically Relevant Quantum Computers
```

PQC is also called:

```text
Quantum-Resistant Cryptography
```

---

# 30. PQC Does Not Mean Quantum Cryptography

These concepts are different.

### Post-Quantum Cryptography

```text
Classical Computer
+
Classical Algorithm
=
Quantum-Resistant Security
```

### Quantum Cryptography

Uses quantum physical properties.

Example:

```text
Quantum Key Distribution
```

PQC is generally much more practical for upgrading existing Internet protocols.

---

# 31. Major PQC Families

Important approaches include:

```text
Lattice-Based
Hash-Based
Code-Based
Multivariate
Isogeny-Based
```

However, not all historically proposed families remain secure or standardized.

---

# 32. Lattice-Based Cryptography

Lattice-based cryptography relies on difficult mathematical problems involving lattices.

It is one of the major foundations of modern PQC standardization.

Examples include:

```text
ML-KEM
ML-DSA
```

---

# 33. ML-KEM

**ML-KEM** is a standardized post-quantum Key Encapsulation Mechanism based on the Module-LWE problem family.

It is intended for establishing shared secrets over potentially hostile networks.

Conceptually:

```text
Client
   │
   │ Encapsulate
   ▼
Server Public Key
   │
   ▼
Ciphertext
   │
   ▼
Shared Secret
```

The recipient decapsulates the ciphertext using its private key.

---

# 34. KEM

**KEM** stands for:

```text
Key Encapsulation Mechanism
```

A KEM provides:

```text
Key Generation
Encapsulation
Decapsulation
```

It establishes a shared secret rather than directly encrypting arbitrary application data.

---

# 35. KEM Flow

Conceptually:

```text
Recipient
   │
Generate Key Pair
   │
Public Key ───────────────► Sender
   │                          │
Private Key                   │
                              ▼
                         Encapsulation
                              │
                        Ciphertext
                              │
                              ▼
Recipient ◄───────────────────┘
   │
Decapsulation
   │
Shared Secret
```

Both sides obtain the same secret.

---

# 36. KEM + Symmetric Encryption

A KEM is normally combined with symmetric encryption.

```text
PQC KEM
   ↓
Shared Secret
   ↓
KDF
   ↓
AES-GCM / ChaCha20-Poly1305
   ↓
Application Data
```

This is analogous to how traditional public-key key exchange is combined with symmetric encryption.

---

# 37. ML-DSA

**ML-DSA** is a standardized post-quantum digital signature algorithm based on lattice problems.

It is designed for:

```text
Authentication
Digital Signatures
Software Signing
Certificates
Document Signing
```

---

# 38. Digital Signature Flow with ML-DSA

```text
Message
   ↓
ML-DSA Signing
   ↓
Signature
   ↓
Verifier
   ↓
Valid / Invalid
```

The private key remains with the signer.

---

# 39. SLH-DSA

**SLH-DSA** is a standardized hash-based digital signature scheme.

It is based on:

```text
Hash Functions
```

rather than lattice assumptions.

This provides a valuable alternative security foundation.

---

# 40. Hash-Based Signatures

Hash-based signatures rely on the security of cryptographic hash functions.

Their major advantage:

```text
Strong Conservative Security Foundation
```

Their disadvantages can include:

```text
Larger Signatures
Different Performance Characteristics
State Management for Some Schemes
```

Stateless constructions reduce some operational complexity.

---

# 41. ML-KEM vs ML-DSA vs SLH-DSA

| Algorithm | Purpose | Family |
|---|---|---|
| ML-KEM | Key Encapsulation | Lattice |
| ML-DSA | Digital Signature | Lattice |
| SLH-DSA | Digital Signature | Hash-Based |

Remember:

```text
ML-KEM
→ Key Establishment

ML-DSA
→ Digital Signatures

SLH-DSA
→ Digital Signatures
```

---

# 42. Post-Quantum Migration

Organizations should not wait until quantum computers become capable of breaking current public-key systems.

Migration begins with:

```text
Inventory
 ↓
Classification
 ↓
Risk Assessment
 ↓
Crypto Agility
 ↓
Pilot
 ↓
Hybrid Deployment
 ↓
Migration
 ↓
Retirement of Legacy Algorithms
```

---

# 43. Cryptographic Inventory

Organizations should identify where cryptography is used.

Examples:

```text
TLS
VPN
SSH
Certificates
Digital Signatures
Code Signing
Email
Database Encryption
Backups
Cloud KMS
IoT
Mobile Applications
APIs
Authentication
```

---

# 44. Crypto Inventory Questions

For every system ask:

```text
Which algorithm?
Which key?
Where stored?
Who controls it?
How long is the data sensitive?
Can the algorithm be replaced?
Is the protocol upgradeable?
```

---

# 45. Harvest Now, Decrypt Later

This is one of the most important PQC concepts.

An attacker can:

```text
Today
 ↓
Capture Encrypted Traffic
 ↓
Store It
 ↓
Wait for Quantum Capability
 ↓
Attempt Decryption
```

This is called:

```text
Harvest Now, Decrypt Later
```

or:

```text
Store Now, Decrypt Later
```

---

# 46. Why Long-Lived Data Is at Risk

Suppose information must remain confidential for:

```text
20 years
```

but quantum-resistant migration takes:

```text
5–10+ years
```

An attacker can capture the encrypted data today.

Therefore organizations need to consider:

```text
Data Lifetime
+
Migration Timeline
```

---

# 47. High-Value Long-Lived Data

Examples:

```text
Government Secrets
Military Data
Healthcare Records
Financial Records
Trade Secrets
Private Communications
Source Code
Strategic Research
Identity Data
```

These can have long confidentiality lifetimes.

---

# 48. Hybrid Cryptography

A practical migration strategy is:

```text
Classical Algorithm
+
Post-Quantum Algorithm
```

Example concept:

```text
X25519
+
ML-KEM
```

The resulting shared secret can be combined using a KDF.

---

# 49. Why Hybrid Key Exchange?

Hybrid designs provide defense against uncertainty.

If:

```text
Classical Algorithm
```

is later broken by quantum computing, the PQC component can still provide protection, assuming the hybrid construction and implementation are sound.

Likewise, if an unexpected weakness appears in the PQC component, the classical component may still contribute security against classical attackers.

---

# 50. Hybrid TLS Concept

Conceptually:

```text
Client
   │
   ├── X25519 Key Share
   │
   └── ML-KEM Key Share
          │
          ▼
       Server
          │
          ▼
     Combined Secret
          │
          ▼
          KDF
          │
          ▼
     Traffic Keys
```

Exact protocol details depend on the TLS implementation and standardized hybrid scheme being used.

---

# 51. PQC and TLS

TLS will need to support:

```text
PQC Key Exchange
+
PQC Authentication
```

A common migration path is likely to involve:

```text
Hybrid Key Exchange
```

before complete replacement of classical public-key mechanisms.

---

# 52. PQC and Certificates

Digital certificates depend on:

```text
Public-Key Signatures
```

Therefore PQC migration also affects:

```text
Certificate Authorities
Server Certificates
Client Certificates
Certificate Chains
Code Signing Certificates
```

---

# 53. PQC and Code Signing

Software updates often rely on digital signatures:

```text
Software
   ↓
Private Signing Key
   ↓
Signature
   ↓
User / Device
   ↓
Verify
```

If the signing algorithm becomes quantum-vulnerable, long-term software authenticity could become a concern.

---

# 54. PQC and Firmware

IoT and embedded devices can be especially challenging because:

```text
Hardware Lifetime
=
10–20+ Years
```

Devices deployed today may still exist when quantum-resistant migration becomes necessary.

---

# 55. PQC and IoT

Challenges include:

```text
Limited CPU
Limited Memory
Large Signatures
Firmware Update Constraints
Long Device Lifetimes
Poor Remote Management
```

PQC migration should therefore be considered during product design.

---

# 56. PQC and Cloud

Cloud providers increasingly provide cryptographic infrastructure through:

```text
KMS
HSM
Certificate Services
Secret Managers
Key Management APIs
```

Organizations should evaluate:

```text
PQC Support
Hybrid Support
Key Rotation
Crypto Agility
Provider Roadmaps
```

---

# 57. Hardware Security Modules

An HSM is a specialized device for protecting cryptographic keys.

Typical functions include:

```text
Key Generation
Key Storage
Digital Signing
Encryption
Decryption
Key Wrapping
Certificate Operations
```

---

# 58. Why HSMs Matter

An HSM can protect keys from direct exposure to application processes.

Conceptually:

```text
Application
     │
     │ Sign
     ▼
    HSM
     │
Private Key
     │
     ▼
Signature
```

The private key can remain inside the protected hardware boundary.

---

# 59. HSM and PQC

HSMs will need to evolve to support:

```text
PQC Key Generation
PQC Signatures
PQC KEM Operations
Hybrid Algorithms
Larger Keys / Signatures
```

Organizations should consider hardware lifecycle planning.

---

# 60. Hardware-Backed Keys

Modern devices may use:

```text
TPM
Secure Enclave
HSM
TEE
Hardware Security Module
```

to protect keys.

Hardware-backed cryptography can reduce exposure to software compromise, although it does not eliminate all attacks.

---

# 61. Trusted Execution Environment

A TEE provides an isolated execution environment.

Conceptually:

```text
Normal OS
    │
    ├───────────────┐
    │               │
    ▼               ▼
Normal App        Secure Environment
                       │
                       ▼
                    Secrets
```

---

# 62. Zero-Knowledge Proofs

A zero-knowledge proof allows one party to demonstrate knowledge of information without revealing the information itself.

Conceptually:

```text
Prover
  │
  │ Proof
  ▼
Verifier

Verifier learns:
"Statement is true"

without learning:
"Secret itself"
```

---

# 63. Zero-Knowledge Example

Suppose a user wants to prove:

```text
I know the password
```

without sending:

```text
The password
```

A suitable zero-knowledge protocol can allow verification of knowledge without directly revealing the secret.

Modern applications can use zero-knowledge techniques for:

```text
Privacy
Identity
Blockchain Systems
Anonymous Credentials
Scalable Verification
```

---

# 64. Homomorphic Encryption

Homomorphic encryption allows computation over encrypted data.

Conceptually:

```text
Encrypt(Data)
      ↓
Encrypted Computation
      ↓
Encrypted Result
      ↓
Decrypt
      ↓
Result
```

This can enable computation without exposing plaintext to the computing environment.

---

# 65. Types of Homomorphic Encryption

Common classifications:

```text
Partially Homomorphic
Somewhat Homomorphic
Fully Homomorphic Encryption
```

Fully homomorphic encryption supports arbitrary computations in principle, although practical performance and engineering constraints remain significant.

---

# 66. Secure Multi-Party Computation

**MPC** allows multiple parties to jointly compute a result without revealing their individual private inputs beyond what the protocol permits.

Example:

```text
Company A
   │
   │ Private Data
   ▼
    MPC
   ▲
   │
Company B
   │
   │ Private Data
   ▼
Result
```

Potential applications include:

```text
Privacy-Preserving Analytics
Financial Collaboration
Healthcare Research
Private Set Intersection
```

---

# 67. Secret Sharing

Secret sharing divides a secret into multiple pieces.

For example:

```text
Secret
 ↓
Share 1
Share 2
Share 3
Share 4
Share 5
```

A threshold scheme may require:

```text
3 of 5 shares
```

to reconstruct the secret.

---

# 68. Threshold Cryptography

Threshold cryptography allows cryptographic operations to be distributed across multiple parties.

For example:

```text
5 Administrators
      ↓
Need any 3
      ↓
Authorize Signature
```

No single administrator needs complete control of the private key.

---

# 69. Modern Authentication

Modern cryptography is also changing authentication.

Important technologies include:

```text
WebAuthn
FIDO2
Passkeys
Hardware Security Keys
Public-Key Authentication
```

---

# 70. Passkeys

Passkeys use public-key cryptography rather than traditional password authentication.

Conceptually:

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
Server Challenge
 ↓
Device
 ↓
Private-Key Signature
 ↓
Server Verifies Public Key
```

---

# 71. Benefits of Passkeys

Passkeys can reduce:

```text
Password Reuse
Phishing
Credential Stuffing
Password Database Risk
```

because the server does not need to store the user's password.

---

# 72. WebAuthn

WebAuthn allows browsers and applications to use public-key credentials for authentication.

It commonly involves:

```text
Authenticator
+
Browser
+
Website
```

The private key remains protected by the authenticator/device.

---

# 73. FIDO2

FIDO2 is an authentication ecosystem involving technologies such as:

```text
WebAuthn
CTAP
```

It enables strong public-key-based authentication.

---

# 74. Modern PKI

PKI continues to evolve through:

```text
Automated Certificates
Short-Lived Certificates
Cloud PKI
mTLS
Machine Identity
PQC Certificates
Certificate Transparency
Automated Rotation
```

---

# 75. Machine Identity

Modern organizations may have:

```text
Millions of:
Services
Containers
Devices
APIs
Workloads
```

Each may require a cryptographic identity.

This creates a major:

```text
Machine Identity Management
```

challenge.

---

# 76. Short-Lived Certificates

Instead of certificates lasting for long periods:

```text
Long-Lived Certificate
```

systems can use:

```text
Short-Lived Certificate
```

This reduces the window of exposure after compromise.

---

# 77. Automated Certificate Lifecycle

A mature system automates:

```text
Issue
 ↓
Deploy
 ↓
Monitor
 ↓
Renew
 ↓
Rotate
 ↓
Revoke
```

Manual certificate management does not scale well.

---

# 78. Cryptographic Key Lifecycle

A secure lifecycle:

```text
Generate
   ↓
Distribute
   ↓
Use
   ↓
Rotate
   ↓
Archive
   ↓
Revoke
   ↓
Destroy
```

Every stage requires appropriate access control.

---

# 79. Key Destruction

When a key is no longer required:

```text
Destroy Securely
```

However, key destruction must be coordinated with:

```text
Backups
Archives
Encrypted Data
Compliance Requirements
Recovery Procedures
```

---

# 80. Crypto Agility Architecture

A flexible architecture might look like:

```text
Application
     │
     ▼
Crypto Abstraction Layer
     │
 ┌───┼─────────────┐
 ▼   ▼             ▼
AES  X25519       ML-KEM
GCM  ECDSA        ML-DSA
     │
     ▼
Provider / Library
```

The application should avoid embedding algorithm-specific assumptions everywhere.

---

# 81. Algorithm Identifiers

Protocols can negotiate or identify algorithms using standardized identifiers.

Example:

```text
Algorithm ID
     ↓
Crypto Provider
     ↓
Implementation
```

However:

> **Algorithm agility must not become algorithm downgrade vulnerability.**

Only approved algorithms should be accepted.

---

# 82. Secure Algorithm Agility

Bad:

```text
Accept Any Algorithm
```

Better:

```text
Supported Algorithms:
AES-GCM
ChaCha20-Poly1305
```

and:

```text
Reject Everything Else
```

---

# 83. PQC Migration Strategy

A practical enterprise strategy:

```text
Phase 1
Inventory

Phase 2
Risk Classification

Phase 3
Crypto Agility

Phase 4
PQC Lab

Phase 5
Hybrid Pilot

Phase 6
Production Deployment

Phase 7
Legacy Retirement
```

---

# 84. Phase 1 – Inventory

Identify:

```text
Algorithms
Protocols
Keys
Certificates
Libraries
Hardware
Data
Vendors
Dependencies
```

---

# 85. Phase 2 – Risk Classification

Prioritize systems based on:

```text
Data Sensitivity
Data Lifetime
Public Exposure
Migration Complexity
Device Lifetime
Business Impact
```

---

# 86. Phase 3 – Crypto Agility

Refactor systems so algorithms can be replaced.

Avoid:

```python
if algorithm == "RSA":
    ...
```

spread throughout hundreds of application modules.

Centralize cryptographic decisions where practical.

---

# 87. Phase 4 – PQC Lab

Create an isolated test environment:

```text
TLS
Certificates
APIs
VPN
KMS
Mobile
IoT
```

Test:

```text
Performance
Compatibility
Bandwidth
CPU
Memory
Latency
Signature Size
Key Size
```

---

# 88. Phase 5 – Hybrid Pilot

Test:

```text
Classical
+
PQC
```

before removing classical mechanisms.

Measure:

```text
Handshake Size
Latency
CPU
Memory
Failure Rate
Interoperability
```

---

# 89. Phase 6 – Production Deployment

Prioritize:

```text
Long-Lived Secrets
High-Value Data
Internet-Facing Systems
Long-Lived Devices
Software Signing
Identity Infrastructure
```

---

# 90. Phase 7 – Legacy Retirement

After sufficient compatibility:

```text
Disable Legacy Algorithms
 ↓
Remove Dependencies
 ↓
Rotate Keys
 ↓
Update Certificates
 ↓
Retest
```

Do not remove algorithms without understanding recovery and interoperability requirements.

---

# 91. PQC Migration Challenges

Organizations may face:

```text
Large Keys
Large Signatures
Performance Cost
Legacy Protocols
Old Hardware
Vendor Dependencies
Certificate Ecosystem
Firmware Limitations
Compliance
Operational Complexity
```

---

# 92. PQC Bandwidth Impact

Some PQC algorithms have larger:

```text
Public Keys
Ciphertexts
Signatures
```

This can affect:

```text
TLS Handshakes
Certificates
Mobile Networks
IoT
Bandwidth
Storage
```

---

# 93. PQC Performance

Measure:

```text
Key Generation
Encapsulation
Decapsulation
Signing
Verification
Memory
CPU
Latency
```

Do not assume an algorithm is suitable merely because it is cryptographically secure.

---

# 94. PQC and Mobile Applications

Mobile applications may face:

```text
Battery Constraints
Binary Size
CPU Constraints
Backward Compatibility
Certificate Pinning
OS Support
```

PQC migration should therefore be tested carefully.

---

# 95. PQC and Embedded Systems

Embedded systems often have:

```text
Small RAM
Slow CPUs
Long Lifetimes
Limited Updates
```

PQC can be particularly challenging in these environments.

---

# 96. PQC and Software Supply Chain

Every dependency that handles:

```text
TLS
SSH
Certificates
Signatures
Key Exchange
```

may require PQC support.

Organizations need vendor visibility.

---

# 97. Vendor PQC Assessment

Ask vendors:

```text
Do you support PQC?
Which standards?
Hybrid algorithms?
Which protocols?
When will certificates support PQC?
How will key rotation work?
What hardware is required?
What is the migration plan?
```

---

# 98. PQC and SOC

SOC teams should prepare to monitor:

```text
New Cryptographic Algorithms
Unexpected Algorithm Changes
Certificate Changes
New KEM Usage
New Signature Algorithms
Crypto Library Updates
KMS Activity
PQC Deployment Errors
```

---

# 99. Cryptographic Telemetry

Useful telemetry:

```text
TLS Version
Cipher Suite
KEM
Signature Algorithm
Certificate
Key ID
KMS Operation
Application
User
Device
Source IP
Destination
```

Avoid logging sensitive key material.

---

# 100. PQC Detection Scenario

Suppose:

```text
Expected:
X25519

Observed:
Unexpected PQC / Hybrid Group
```

Possible explanations:

```text
Planned Migration
New Client
Configuration Change
Malicious Modification
```

SOC should correlate with:

```text
Change Management
Deployment
Certificate
Source
Application Version
```

---

# 101. Post-Quantum VAPT

A VAPT assessment can check:

```text
Algorithm Inventory
Classical Dependencies
PQC Support
Hybrid Support
Crypto Agility
Certificate Infrastructure
Key Lifecycle
Long-Lived Data
Vendor Dependencies
```

---

# 102. PQC VAPT Questions

Ask:

```text
Can algorithms be upgraded?

Are RSA/ECC dependencies hard-coded?

Are certificates tightly coupled to classical algorithms?

Can TLS negotiate hybrid key exchange?

Can devices receive firmware updates?

Are signing keys quantum-vulnerable?

How long must encrypted data remain confidential?
```

---

# 103. Quantum Risk Matrix

| Asset | Current Crypto | Data Lifetime | Quantum Risk |
|---|---|---:|---|
| Web Session | TLS/ECDHE | Short | Medium |
| Banking Records | ECC/RSA | Long | High |
| Government Archive | RSA/ECC | Very Long | Critical |
| IoT Firmware | ECC | 10+ years | High |
| Password Hash | Argon2 | Long | Lower |
| AES-256 Data | AES-256 | Long | Lower relative risk |

Risk depends on implementation, exposure, and data lifetime.

---

# 104. Important Distinction

Quantum computing does **not** mean:

```text
All cryptography becomes useless.
```

The major immediate conceptual distinction is:

```text
Public-Key Cryptography
→ Major Quantum Threat

Symmetric Cryptography
→ Security Margin Reduction
```

Therefore migration focuses heavily on:

```text
RSA
DH
ECDH
ECDSA
EdDSA
```

and related public-key systems.

---

# 105. Quantum-Safe Architecture

A future architecture may look like:

```text
                Client
                   │
                   ▼
             Hybrid TLS
             ┌─────┴─────┐
             ▼           ▼
          X25519       ML-KEM
             │           │
             └─────┬─────┘
                   ▼
                  KDF
                   │
                   ▼
              AES-GCM
                   │
                   ▼
             Application
```

Authentication can similarly migrate toward:

```text
Classical Signature
+
PQC Signature
```

during transitional periods.

---

# 106. Modern Cryptography Cheat Sheet

```text
AES-GCM
→ Authenticated Encryption

ChaCha20-Poly1305
→ Authenticated Encryption

SHA-256 / SHA-3
→ Hashing

HMAC
→ Message Authentication

HKDF
→ Key Derivation

Argon2
→ Password Hashing

X25519
→ Classical Key Agreement

Ed25519
→ Classical Digital Signature

ML-KEM
→ Post-Quantum Key Encapsulation

ML-DSA
→ Post-Quantum Digital Signature

SLH-DSA
→ Hash-Based Post-Quantum Signature
```

---

# 107. Modern Cryptography Decision Guide

### Need encryption?

```text
AES-GCM
or
ChaCha20-Poly1305
```

### Need a hash?

```text
SHA-256
SHA-384
SHA-512
SHA-3
```

### Need password storage?

```text
Argon2
scrypt
PBKDF2
```

### Need key derivation?

```text
HKDF
```

### Need classical key exchange?

```text
X25519
```

### Need classical signatures?

```text
Ed25519
```

### Need post-quantum KEM?

```text
ML-KEM
```

### Need post-quantum signature?

```text
ML-DSA
SLH-DSA
```

Always select algorithms based on the protocol, standards, implementation, and security requirements rather than simply choosing from a list.

---

# 108. Practical Lab – OpenSSL Algorithm Inspection

Inspect your installed OpenSSL:

```bash
openssl version
```

List supported algorithms:

```bash
openssl list -cipher-algorithms
```

and:

```bash
openssl list -digest-algorithms
```

Use this to understand what your environment supports.

---

# 109. Practical Lab – Modern TLS

Inspect TLS 1.3:

```bash
openssl s_client \
    -connect example.com:443 \
    -servername example.com \
    -tls1_3
```

Record:

```text
Protocol
Cipher
Certificate
```

Only use authorized targets for security testing.

---

# 110. Practical Lab – Crypto Inventory

Create a spreadsheet containing:

```text
Application
Protocol
Algorithm
Key Size
Key Location
Certificate
Data Lifetime
Owner
Replacement Difficulty
Quantum Risk
```

Example:

```text
API Gateway
TLS
ECDHE + AES-GCM
256-bit
Cloud KMS
RSA Certificate
10 years
Security Team
Medium
High
```

---

# 111. Practical Lab – PQC Experiment

Use a controlled PQC-capable cryptographic library or test environment.

Measure:

```text
Key Generation
Encapsulation
Decapsulation
Signature
Verification
```

Compare:

```text
Classical
vs
PQC
```

Record:

```text
Latency
Memory
Key Size
Ciphertext Size
Signature Size
```

---

# 112. Practical Lab – Hybrid Key Exchange

Build a controlled demonstration:

```text
Classical Shared Secret
+
PQC Shared Secret
        ↓
HKDF
        ↓
Application Key
```

Do not invent your own production protocol.

Use standardized constructions and reviewed libraries.

---

# 113. Practical Lab – Passkey/WebAuthn

Create a local test application implementing:

```text
Registration
Authentication
Challenge
Signature
Verification
```

Observe:

```text
Private Key
→ Remains with Authenticator

Public Key
→ Stored by Server
```

---

# 114. Practical Lab – Secret Sharing

Implement a test threshold scheme:

```text
Secret
 ↓
5 Shares
 ↓
Any 3
 ↓
Recover Secret
```

Test:

```text
2 shares
→ Failure

3 shares
→ Success
```

Use a reviewed implementation for real applications.

---

# 115. Practical Lab – HSM / KMS Simulation

Design:

```text
Application
   ↓
KMS API
   ↓
Key Operation
   ↓
Encrypted Data
```

Ensure the application does not directly handle master key material.

---

# 116. Practical Lab – Cryptographic Agility

Create a small application supporting:

```text
Algorithm A
Algorithm B
```

through a centralized cryptographic interface.

Then switch algorithms through configuration.

The goal is to understand:

```text
Application
 ↓
Crypto Interface
 ↓
Algorithm Provider
```

rather than:

```text
Application
 ↓
Hard-Coded Algorithm Everywhere
```

---

# 117. Practical Lab – Quantum Threat Modeling

Choose a fictional organization.

Identify:

```text
Data
 ↓
Encryption
 ↓
Key Exchange
 ↓
Signature
 ↓
Data Lifetime
```

Classify:

```text
Low
Medium
High
Critical
```

based on quantum migration requirements.

---

# 118. Interview Questions

## What is post-quantum cryptography?

Cryptography designed to remain secure against attackers using sufficiently capable quantum computers as well as classical computers.

---

## What is Shor's algorithm?

A quantum algorithm that can efficiently solve integer factorization and discrete logarithm problems on sufficiently powerful fault-tolerant quantum computers.

---

## Which major cryptographic systems does Shor's algorithm threaten?

Systems based on integer factorization and discrete logarithms, including RSA, Diffie-Hellman, ECDH, ECDSA, and EdDSA.

---

## What is Grover's algorithm?

A quantum search algorithm that provides a quadratic speedup for certain unstructured search problems.

---

## Does quantum computing completely break AES?

No. Grover's algorithm reduces the generic brute-force security margin, but AES-256 retains a substantial security margin.

---

## Why is AES-256 relevant to post-quantum security?

Its larger key size provides a greater margin against generic quantum search than AES-128.

---

## What is ML-KEM?

A standardized post-quantum key encapsulation mechanism based on lattice cryptography.

---

## What is ML-DSA?

A standardized post-quantum digital signature algorithm based on lattice cryptography.

---

## What is SLH-DSA?

A standardized hash-based post-quantum digital signature algorithm.

---

## What is a KEM?

A Key Encapsulation Mechanism establishes a shared secret using public-key cryptographic operations.

---

## Why do we need KEMs?

They allow public-key mechanisms to establish a shared symmetric secret efficiently, after which symmetric encryption can protect bulk application data.

---

## What is hybrid cryptography?

Using classical and post-quantum cryptographic mechanisms together during the migration period.

---

## Why use hybrid key exchange?

It can provide protection based on both classical and post-quantum assumptions during the transition.

---

## What is crypto agility?

The ability to replace cryptographic algorithms and parameters without major architectural redesign.

---

## What is Harvest Now, Decrypt Later?

An attacker captures encrypted data today and stores it with the expectation of decrypting it in the future using improved capabilities, potentially including quantum computers.

---

## Why is PQC migration urgent?

Some sensitive data needs confidentiality for many years, and attackers can capture encrypted traffic before quantum computers become capable of breaking the underlying public-key cryptography.

---

## Is post-quantum cryptography the same as quantum cryptography?

No.

PQC uses classical cryptographic algorithms designed to resist quantum attacks. Quantum cryptography uses quantum physical phenomena.

---

## What is a digital signature?

A cryptographic mechanism that allows a verifier to establish authenticity and integrity of signed data and, depending on the system, evidence of possession of a signing private key.

---

## What is Ed25519?

A modern elliptic-curve digital signature scheme.

---

## Is Ed25519 post-quantum secure?

No. It relies on elliptic-curve discrete-logarithm security and is therefore vulnerable to sufficiently powerful quantum attacks.

---

## Is X25519 post-quantum secure?

No. It is a classical elliptic-curve key-agreement mechanism.

---

## What happens to RSA after a cryptographically relevant quantum computer exists?

RSA's security assumption can be defeated using Shor's algorithm, so it should be replaced with quantum-resistant mechanisms.

---

## What happens to ECC?

Elliptic-curve systems such as ECDH and ECDSA are also threatened by Shor's algorithm.

---

## What is a zero-knowledge proof?

A method for proving a statement without revealing the underlying secret information beyond what is necessary to establish that the statement is true.

---

## What is homomorphic encryption?

Encryption that allows certain computations to be performed directly on encrypted data.

---

## What is MPC?

Secure Multi-Party Computation allows multiple parties to jointly compute a function while protecting their private inputs according to the protocol's security guarantees.

---

## What is threshold cryptography?

A system where cryptographic authorization or operations require cooperation from a threshold number of participants rather than a single key holder.

---

## What are passkeys?

Public-key-based authentication credentials designed to replace or reduce dependence on passwords.

---

# 119. Quick Revision Table

| Concept | Key Idea |
|---|---|
| Crypto Agility | Replace algorithms safely |
| AES-GCM | Authenticated encryption |
| ChaCha20-Poly1305 | Authenticated encryption |
| SHA-3 | Modern hash family |
| HKDF | Key derivation |
| X25519 | Classical key exchange |
| Ed25519 | Classical signature |
| Shor | Threatens RSA/ECC |
| Grover | Quadratic search speedup |
| PQC | Quantum-resistant classical cryptography |
| KEM | Shared-secret establishment |
| ML-KEM | Standardized PQ KEM |
| ML-DSA | Standardized PQ signature |
| SLH-DSA | Hash-based PQ signature |
| Hybrid Crypto | Classical + PQC |
| HSM | Hardware key protection |
| TEE | Isolated secure execution |
| ZKP | Prove without revealing secret |
| FHE | Compute on encrypted data |
| MPC | Joint computation with private inputs |
| Secret Sharing | Split secret into shares |
| Threshold Crypto | Multiple parties required |
| WebAuthn | Public-key authentication |
| Passkeys | Passwordless public-key authentication |
| HNDL | Capture now, decrypt later |

---

# 120. Modern Cryptographic Architecture

A future-oriented architecture may look like:

```text
                         APPLICATION
                              │
                              ▼
                     Security Protocol
                              │
                ┌─────────────┴─────────────┐
                ▼                           ▼
        Authentication                 Key Exchange
                │                           │
        ┌───────┴───────┐           ┌───────┴───────┐
        ▼               ▼           ▼               ▼
     ML-DSA         SLH-DSA      X25519          ML-KEM
        │                           │               │
        └──────────────┬────────────┴───────────────┘
                       ▼
                      KDF
                       │
                       ▼
              AES-GCM / ChaCha20
                       │
                       ▼
               Encrypted Data
```

During migration:

```text
Classical
   +
PQC
```

can coexist.

---

# 121. Post-Quantum Migration Architecture

A transitional system might use:

```text
                 CLIENT
                    │
                    ▼
              Hybrid TLS
              ┌─────┴─────┐
              ▼           ▼
           X25519       ML-KEM
              │           │
              └─────┬─────┘
                    ▼
              Combined Secret
                    │
                    ▼
                   HKDF
                    │
                    ▼
              AES-256-GCM
                    │
                    ▼
                 SERVER
```

Authentication may similarly use:

```text
Classical Signature
+
PQC Signature
```

where supported and appropriate.

---

# 122. PQC Migration Checklist

```text
☐ Inventory all cryptographic usage
☐ Identify RSA/ECC dependencies
☐ Identify long-lived sensitive data
☐ Identify long-lived devices
☐ Identify certificates
☐ Identify code-signing keys
☐ Identify TLS dependencies
☐ Identify VPN dependencies
☐ Identify SSH dependencies
☐ Identify KMS/HSM dependencies
☐ Evaluate vendor PQC roadmaps
☐ Implement crypto agility
☐ Establish PQC test environment
☐ Test hybrid mechanisms
☐ Measure performance
☐ Plan certificate migration
☐ Plan signing-key migration
☐ Prioritize long-lived secrets
☐ Deploy hybrid mechanisms where appropriate
☐ Retire vulnerable legacy mechanisms
```

---

# 123. Secure Modern Cryptography Checklist

```text
ALGORITHMS
☐ Use standardized algorithms
☐ Use modern AEAD
☐ Use modern hashes
☐ Use appropriate KDFs
☐ Avoid obsolete algorithms

KEYS
☐ Generate keys using CSPRNG
☐ Protect private keys
☐ Use KMS/HSM where appropriate
☐ Rotate keys
☐ Apply least privilege
☐ Destroy retired keys appropriately

PROTOCOLS
☐ TLS 1.2/1.3 as appropriate
☐ Prefer TLS 1.3
☐ Use forward secrecy
☐ Validate certificates
☐ Avoid downgrade
☐ Protect against replay

APPLICATION
☐ Avoid custom cryptography
☐ Use secure libraries
☐ Avoid hard-coded secrets
☐ Use constant-time comparison where required
☐ Validate cryptographic failures
☐ Fail closed

PQC
☐ Inventory classical public-key crypto
☐ Assess data lifetime
☐ Implement crypto agility
☐ Evaluate hybrid PQC
☐ Monitor standards
☐ Test vendors
☐ Plan migration
```

---

# 124. Cryptography Career Relevance

For cybersecurity roles, modern cryptography knowledge is useful in:

```text
SOC
VAPT
Application Security
Cloud Security
Identity Security
Security Engineering
DevSecOps
Incident Response
Threat Detection
PKI Administration
Cloud KMS
Security Architecture
```

A security analyst should understand:

```text
What TLS does
How certificates work
How JWT works
How keys are protected
How encryption fails
How secrets leak
How authentication works
How cryptographic attacks are detected
```

A security engineer should additionally understand:

```text
KMS
HSM
PKI
mTLS
Key Lifecycle
Crypto Agility
PQC Migration
Secure Architecture
```

---

# 125. Cryptography Interview Master Revision

Remember these relationships:

```text
AES
→ Symmetric Encryption

AES-GCM
→ Authenticated Encryption

SHA-256
→ Hash

HMAC
→ Authentication / Integrity

HKDF
→ Key Derivation

Argon2
→ Password Hashing

X25519
→ Classical Key Exchange

Ed25519
→ Classical Digital Signature

RSA
→ Classical Public-Key Cryptography

Shor
→ Threatens RSA / ECC

Grover
→ Weakens Generic Search Security

ML-KEM
→ Post-Quantum Key Encapsulation

ML-DSA
→ Post-Quantum Digital Signature

SLH-DSA
→ Hash-Based Post-Quantum Signature

Hybrid
→ Classical + PQC

Crypto Agility
→ Easier Future Migration

HNDL
→ Capture Now, Decrypt Later
```

---

# 126. Final Cryptography Knowledge Map

```text
                         CRYPTOGRAPHY
                              │
        ┌─────────────────────┼─────────────────────┐
        ▼                     ▼                     ▼
    SYMMETRIC             ASYMMETRIC             HASHING
        │                     │                     │
    AES / ChaCha         RSA / ECC              SHA-2
        │                     │                 SHA-3
        ▼                     ▼                     │
      AEAD                Key Exchange             │
        │                 Signatures               │
        │                     │                     │
        └──────────────┬──────┴─────────────────────┘
                       ▼
                  KEY MANAGEMENT
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
         KDF          KMS          HSM
          │
          ▼
                 SECURITY PROTOCOLS
                       │
              ┌────────┴────────┐
              ▼                 ▼
             TLS               SSH
              │
              ▼
             HTTPS
              │
              ▼
          APPLICATIONS
              │
              ▼
        REAL-WORLD ATTACKS
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
     Nonce   JWT    Keys
     Reuse  Bugs   Leakage
       │      │      │
       └──────┼──────┘
              ▼
        MODERN CRYPTO
              │
       ┌──────┼────────────┐
       ▼      ▼            ▼
      ZKP     MPC         FHE
       │
       ▼
     QUANTUM
       │
   ┌───┴──────────┐
   ▼              ▼
 Shor           Grover
   │              │
   ▼              ▼
RSA/ECC        Symmetric
Threat         Security
   │
   ▼
 POST-QUANTUM CRYPTOGRAPHY
   │
   ├── ML-KEM
   ├── ML-DSA
   └── SLH-DSA
          │
          ▼
    HYBRID MIGRATION
          │
          ▼
     CRYPTO AGILITY
```

---

# 127. The Most Important Lessons

```text
1. Modern cryptography is about using secure primitives correctly.

2. AES and ChaCha20 remain important in the post-quantum era.

3. RSA and elliptic-curve public-key systems face major quantum threats.

4. Shor's algorithm is the primary theoretical threat to RSA and ECC.

5. Grover's algorithm reduces the effective security of generic symmetric-key search.

6. AES-256 provides a larger quantum security margin than AES-128.

7. Post-quantum cryptography uses classical algorithms designed to resist quantum attacks.

8. ML-KEM is used for post-quantum key encapsulation.

9. ML-DSA and SLH-DSA provide post-quantum digital signatures.

10. KEMs establish shared secrets; symmetric encryption protects bulk data.

11. Hybrid cryptography combines classical and PQC mechanisms during migration.

12. Crypto agility makes future algorithm replacement easier.

13. Harvest Now, Decrypt Later makes long-lived sensitive data particularly important.

14. PQC migration is an organizational process, not simply a library upgrade.

15. Organizations need a complete cryptographic inventory.

16. Certificates, TLS, VPNs, SSH, code signing, KMS, HSMs, and IoT systems may all require migration.

17. Hardware security can protect keys but does not eliminate protocol or implementation vulnerabilities.

18. Zero-knowledge proofs can provide privacy-preserving verification.

19. Homomorphic encryption enables computation over encrypted data.

20. MPC enables privacy-preserving collaborative computation.

21. Threshold cryptography distributes trust across multiple parties.

22. Passkeys use public-key cryptography to reduce password-based authentication risks.

23. Machine identity is becoming increasingly important in cloud-native environments.

24. Cryptographic keys require complete lifecycle management.

25. Strong cryptography still requires secure implementation and configuration.

26. Never design production cryptography from scratch without expert review.

27. Never hard-code sensitive production keys.

28. Never reuse AEAD nonces under the same key.

29. Never disable certificate verification as a permanent solution.

30. The future of cryptography is increasingly defined by crypto agility and post-quantum readiness.
```

---

# 128. Final Chapter Summary

This chapter covered the modern and future direction of cryptography:

```text
Modern Symmetric Cryptography
AES
ChaCha20-Poly1305
SHA-2
SHA-3
SHAKE
HMAC
HKDF
Ed25519
X25519
Cryptographic Agility
Key Separation
Domain Separation
Authenticated Encryption
Quantum Computing
Qubits
Shor's Algorithm
Grover's Algorithm
Quantum Threats
Post-Quantum Cryptography
KEM
ML-KEM
ML-DSA
SLH-DSA
Lattice-Based Cryptography
Hash-Based Cryptography
Hybrid Cryptography
Harvest Now, Decrypt Later
PQC Migration
Crypto Inventory
Crypto Agility
PQC TLS
PQC Certificates
PQC Code Signing
PQC IoT
PQC Cloud
HSM
KMS
TEE
Hardware-Backed Keys
Zero-Knowledge Proofs
Homomorphic Encryption
Secure Multi-Party Computation
Secret Sharing
Threshold Cryptography
WebAuthn
FIDO2
Passkeys
Machine Identity
Modern PKI
Short-Lived Certificates
Key Lifecycle
PQC VAPT
SOC Monitoring
Quantum Risk Assessment
```

The most important mental model is:

```text
                 TODAY
                   │
                   ▼
          Classical Cryptography
                   │
          ┌────────┴────────┐
          ▼                 ▼
      Symmetric          Public-Key
          │                 │
       AES-GCM          RSA / ECC
          │                 │
          │            Quantum Threat
          │                 │
          │                 ▼
          │              PQC
          │                 │
          │          ┌──────┴──────┐
          │          ▼             ▼
          │       ML-KEM        ML-DSA
          │                       │
          └──────────┬────────────┘
                     ▼
                Hybrid Crypto
                     │
                     ▼
               Crypto Agility
                     │
                     ▼
            Quantum-Resistant Future
```

> **The goal of modern cryptography is not simply to find an algorithm that is secure today. It is to build systems that can remain secure as algorithms, implementations, infrastructure, and computational capabilities evolve.**

---

# Cryptography Section Complete

The complete 12-chapter roadmap is:

```text
Chapter 01 – Cryptography Fundamentals
Chapter 02 – Symmetric Cryptography
Chapter 03 – Asymmetric Cryptography
Chapter 04 – Hash Functions & Message Authentication
Chapter 05 – Digital Signatures & Certificates
Chapter 06 – Password Cryptography & Authentication
Chapter 07 – Classical Cryptographic Algorithms
Chapter 08 – Key Management & Key Exchange
Chapter 09 – Randomness, Nonces & Cryptographic Primitives
Chapter 10 – TLS, HTTPS & Cryptographic Protocols
Chapter 11 – Applied Cryptography & Common Attacks
Chapter 12 – Modern Cryptography & Post-Quantum Cryptography
```

Together, these chapters take you from:

```text
Cryptographic Fundamentals
        ↓
Symmetric Encryption
        ↓
Asymmetric Cryptography
        ↓
Hashing & Authentication
        ↓
Digital Signatures
        ↓
Passwords
        ↓
Algorithms
        ↓
Key Management
        ↓
Randomness & Nonces
        ↓
TLS / HTTPS
        ↓
Cryptographic Attacks
        ↓
Modern Cryptography
        ↓
Post-Quantum Cryptography
```

This gives you a complete foundation for understanding cryptography from a **Cybersecurity, VAPT, SOC, Security Engineering, Application Security, and interview perspective**.