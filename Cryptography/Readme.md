# 🔐 Cryptography

> A structured, practical guide to **cryptography, cryptographic algorithms, secure protocols, key management, applied cryptography, and modern post-quantum cryptography**.

---

## 📖 Overview

**Cryptography** is the science and engineering of protecting information through mathematical techniques.

It provides the foundation for many modern security systems, including:

- Secure communication
- Data confidentiality
- Data integrity
- Authentication
- Digital signatures
- Password protection
- Secure key exchange
- HTTPS/TLS
- Digital certificates
- Blockchain systems
- Cloud security
- Identity and access management
- Secure software development

This module progresses from the fundamental concepts of cryptography to modern cryptographic systems and post-quantum cryptography.

The goal is not simply to memorize algorithms, but to understand:

```text
Why cryptography is needed
        ↓
How cryptographic primitives work
        ↓
How algorithms provide security
        ↓
How keys are generated and managed
        ↓
How cryptographic protocols are designed
        ↓
How implementations can fail
        ↓
How modern systems defend against attacks
```

---

# 🎯 Learning Objectives

By completing this module, you should be able to:

- Understand fundamental cryptographic concepts
- Explain confidentiality, integrity, authentication, and non-repudiation
- Understand classical and modern encryption techniques
- Differentiate symmetric and asymmetric cryptography
- Understand hashing and message authentication
- Explain digital signatures and certificates
- Understand public key infrastructure (PKI)
- Understand key exchange and key management
- Explain TLS and HTTPS at a cryptographic level
- Identify common cryptographic vulnerabilities
- Recognize insecure cryptographic implementations
- Understand modern authenticated encryption
- Understand the impact of quantum computing on cryptography
- Explain post-quantum cryptographic approaches

---

# 📚 Chapters

## Chapter 01 – Cryptography Fundamentals

Introduces the foundations of cryptography and establishes the terminology used throughout the module.

### Topics include

- What is cryptography?
- Cryptography vs cryptanalysis vs cryptology
- Security goals
- Confidentiality
- Integrity
- Authentication
- Non-repudiation
- Plaintext and ciphertext
- Encryption and decryption
- Keys and keyspaces
- Cryptographic algorithms
- Cryptographic primitives
- Kerckhoffs's principle
- Threat models
- Computational security

---

## Chapter 02 – Classical Cryptography & Historical Ciphers

Explores early cryptographic techniques and how cryptanalysis evolved.

### Topics include

- Caesar cipher
- Substitution ciphers
- Transposition ciphers
- Vigenère cipher
- Affine cipher
- Playfair cipher
- One-Time Pad
- Frequency analysis
- Brute-force attacks
- Classical cryptanalysis
- Historical cryptographic systems
- Limitations of classical cryptography

These concepts provide useful intuition for understanding why modern cryptographic designs use substantially stronger mathematical constructions.

---

## Chapter 03 – Symmetric-Key Cryptography

Covers encryption systems where the same secret key, or closely related secret material, is used for encryption and decryption.

### Topics include

- Symmetric cryptography
- Block ciphers
- Stream ciphers
- AES
- DES
- 3DES
- Block sizes
- Key sizes
- Initialization vectors
- Nonces
- Padding
- Modes of operation
- ECB
- CBC
- CTR
- GCM
- Authenticated encryption
- AEAD

Special attention is given to why simply selecting a strong algorithm is not enough—the algorithm must also be used correctly.

---

## Chapter 04 – Asymmetric-Key Cryptography

Introduces public-key cryptography and its role in secure communication and authentication.

### Topics include

- Public keys
- Private keys
- RSA
- Diffie-Hellman
- Elliptic Curve Cryptography
- ECC
- ECDH
- Computational hardness
- Public-key encryption
- Hybrid encryption
- Key exchange
- Forward secrecy

This chapter explains why asymmetric cryptography is generally used differently from symmetric cryptography in real-world systems.

---

## Chapter 05 – Hash Functions & Message Integrity

Explores cryptographic hash functions and their role in integrity, authentication, password storage, and digital signatures.

### Topics include

- Cryptographic hash functions
- SHA-2
- SHA-3
- MD5
- SHA-1
- Preimage resistance
- Second-preimage resistance
- Collision resistance
- Avalanche effect
- Message integrity
- Hash-based constructions
- Password hashing
- Salting
- Hash-based identifiers

The chapter also explains why encryption and hashing solve fundamentally different problems.

---

## Chapter 06 – Message Authentication & MACs

Focuses on mechanisms that allow systems to verify that a message came from an expected source and was not modified.

### Topics include

- Message Authentication Codes
- MACs
- HMAC
- CMAC
- Authentication vs integrity
- Secret-key authentication
- MAC verification
- Replay considerations
- MAC-then-encrypt
- Encrypt-then-MAC
- Authenticated encryption
- AEAD

The chapter connects MACs with practical protocols and secure application design.

---

## Chapter 07 – Digital Signatures & PKI

Covers asymmetric authentication, digital signatures, certificates, and the Public Key Infrastructure ecosystem.

### Topics include

- Digital signatures
- Signing and verification
- RSA signatures
- ECDSA
- EdDSA
- Digital certificates
- Certificate Authorities
- Root CAs
- Intermediate CAs
- Certificate chains
- X.509
- Certificate validation
- Certificate revocation
- CRL
- OCSP
- Public Key Infrastructure

This chapter explains how trust is established between parties that have never directly exchanged a secret key.

---

## Chapter 08 – Key Management & Key Exchange

Covers one of the most important practical aspects of cryptography: managing cryptographic keys securely throughout their lifecycle.

### Topics include

- Key generation
- Key exchange
- Diffie-Hellman
- ECDH
- Key derivation
- KDFs
- HKDF
- Key storage
- Key rotation
- Key expiration
- Key destruction
- Key backup
- Key recovery
- Hardware Security Modules
- Key Management Systems
- Secrets management
- Forward secrecy

A major principle explored in this chapter is:

> **Strong cryptography cannot compensate for poorly managed keys.**

---

## Chapter 09 – Randomness, Nonces & Cryptographic Primitives

Examines the supporting building blocks required for secure cryptographic implementations.

### Topics include

- Entropy
- Randomness
- CSPRNG
- Secure random number generation
- Nonces
- Initialization vectors
- Salts
- Seeds
- Key Derivation Functions
- KDFs
- HKDF
- Cryptographic primitives
- Domain separation
- Secure parameter generation

This chapter focuses heavily on implementation correctness because predictable randomness or incorrect nonce usage can completely undermine otherwise secure algorithms.

---

## Chapter 10 – TLS, HTTPS & Cryptographic Protocols

Explains how cryptographic primitives are combined into real-world security protocols.

### Topics include

- TLS
- HTTPS
- TLS handshake
- Client authentication
- Server authentication
- Certificates
- Key exchange
- Session keys
- Symmetric encryption
- AEAD
- Forward secrecy
- TLS 1.2
- TLS 1.3
- Certificate validation
- Secure protocol design
- Cryptographic negotiation

The objective is to understand what happens cryptographically when a browser establishes a secure HTTPS connection.

---

## Chapter 11 – Applied Cryptography & Common Attacks

Connects cryptographic theory with real-world security failures.

### Topics include

- Brute-force attacks
- Dictionary attacks
- Man-in-the-Middle attacks
- Replay attacks
- Padding oracle attacks
- Downgrade attacks
- Weak key attacks
- Weak randomness
- Nonce reuse
- Hash collisions
- Length-extension attacks
- Certificate attacks
- Cryptographic implementation flaws
- Insecure modes
- Hard-coded keys
- Weak password hashing
- Improper key management
- Cryptographic side channels

The chapter emphasizes that many real-world cryptographic failures occur because secure primitives are implemented or integrated incorrectly.

---

## Chapter 12 – Modern Cryptography & Post-Quantum Cryptography

Introduces modern cryptographic approaches and the transition toward quantum-resistant systems.

### Topics include

- Modern cryptographic design
- AEAD
- Modern encryption schemes
- Modern digital signatures
- Elliptic-curve cryptography
- Secure protocol design
- Quantum computing threats
- Shor's algorithm
- Grover's algorithm
- Post-quantum cryptography
- Lattice-based cryptography
- ML-KEM
- ML-DSA
- SLH-DSA
- Hybrid cryptographic systems
- Cryptographic migration
- Crypto-agility
- Post-quantum TLS

The chapter focuses on how organizations can prepare cryptographic infrastructure for the transition to post-quantum security.

---

# 🧭 Learning Path

The chapters are intentionally arranged from foundational concepts to practical security engineering.

```text
                    CRYPTOGRAPHY
                         │
                         ▼
              ┌─────────────────────┐
              │ 1. Fundamentals     │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 2. Classical Crypto │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 3. Symmetric Crypto │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 4. Asymmetric Crypto│
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 5. Hash Functions   │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 6. MACs             │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 7. Signatures & PKI │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 8. Key Management   │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 9. Crypto Primitives│
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 10. TLS & Protocols │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 11. Attacks         │
              └──────────┬──────────┘
                         ▼
              ┌─────────────────────┐
              │ 12. Modern & PQC    │
              └─────────────────────┘
```

---

# 🔗 How the Concepts Connect

Cryptography is not a collection of isolated algorithms.

Modern secure systems combine multiple cryptographic mechanisms.

For example, HTTPS can conceptually involve:

```text
Certificate
     ↓
Digital Signature
     ↓
Server Authentication
     ↓
Key Exchange
     ↓
Session Key
     ↓
Symmetric Encryption
     ↓
AEAD
     ↓
Confidentiality + Integrity
```

Similarly, secure password storage involves:

```text
Password
   ↓
Salt
   ↓
Password Hash / KDF
   ↓
Stored Verification Data
```

And secure application authentication may involve:

```text
Private Key
   ↓
Digital Signature
   ↓
Public Key
   ↓
Signature Verification
```

---

# 🧩 Core Cryptographic Building Blocks

The entire module can be understood through a small set of fundamental primitives:

```text
Encryption
Hashing
MAC
Digital Signature
Key Exchange
Key Derivation
Randomness
```

These primitives are then combined to create:

```text
TLS
HTTPS
VPNs
SSH
PKI
Authentication Systems
Secure APIs
Encrypted Storage
Messaging Systems
```

---

# 🔐 Major Cryptographic Categories

| Category | Primary Purpose | Examples |
|---|---|---|
| Symmetric Encryption | Confidentiality | AES |
| Asymmetric Cryptography | Key exchange / encryption / signatures | RSA, ECC |
| Hashing | Integrity / fingerprints | SHA-256, SHA-3 |
| MAC | Authentication + integrity | HMAC |
| Digital Signatures | Authentication / integrity / non-repudiation | ECDSA, EdDSA |
| KDF | Derive cryptographic keys | HKDF |
| Randomness | Secure key/nonce generation | CSPRNG |
| PKI | Establish trust | X.509, CA |
| AEAD | Encryption + integrity | AES-GCM, ChaCha20-Poly1305 |
| PQC | Quantum-resistant security | ML-KEM, ML-DSA |

---

# 🛡️ Security Properties

Cryptography primarily supports four major security properties:

```text
Confidentiality
      │
      ▼
Prevent unauthorized disclosure


Integrity
      │
      ▼
Detect unauthorized modification


Authentication
      │
      ▼
Verify identity / origin


Non-Repudiation
      │
      ▼
Provide cryptographic evidence of signing
```

These properties are often implemented together rather than independently.

---

# ⚠️ Cryptography vs Cryptanalysis

## Cryptography

Designs mechanisms for protecting information.

```text
Design
 ↓
Algorithm
 ↓
Implementation
 ↓
Security
```

## Cryptanalysis

Studies methods for breaking or analyzing cryptographic systems.

```text
Ciphertext
 ↓
Analysis
 ↓
Weakness
 ↓
Attack
```

Together:

```text
Cryptography + Cryptanalysis
          ↓
       Cryptology
```

---

# 🧪 Practical Focus

Each chapter will emphasize practical understanding rather than purely theoretical definitions.

Where appropriate, examples will use:

```text
Python
OpenSSL
Linux
Kali Linux
Wireshark
Burp Suite
curl
```

Practical exercises may include:

- Encrypting and decrypting data
- Generating cryptographic keys
- Computing hashes
- Creating and verifying HMACs
- Generating digital signatures
- Inspecting X.509 certificates
- Analyzing TLS connections
- Identifying weak cryptographic configurations
- Demonstrating cryptographic attacks in controlled environments
- Testing secure implementations

---

# 🎯 Cybersecurity Relevance

Cryptography is foundational to several cybersecurity domains.

### Application Security

```text
Password Storage
JWT
Session Security
TLS
API Authentication
Data Encryption
```

### Network Security

```text
TLS
VPN
IPsec
SSH
Certificates
```

### Cloud Security

```text
KMS
Secrets Management
Encryption at Rest
Encryption in Transit
Identity
```

### SOC / Blue Team

```text
TLS Investigation
Certificate Monitoring
Encrypted Traffic Analysis
Key Compromise
Credential Protection
```

### VAPT / Ethical Hacking

```text
Weak Cryptography
TLS Misconfiguration
Weak Password Hashing
Certificate Issues
Hard-coded Secrets
Insecure Randomness
```

---

# 📌 Important Principle

> **Do not invent your own cryptographic algorithm.**

Secure systems should generally use well-studied, standardized cryptographic algorithms and constructions with appropriate parameters and vetted implementations.

The challenge in practical cryptography is often not creating a new algorithm, but correctly selecting, implementing, configuring, and managing existing cryptographic primitives.

---

# 🧠 Prerequisites

Recommended knowledge:

```text
Basic Mathematics
Basic Probability
Computer Networks
Operating Systems
Programming Fundamentals
Cybersecurity Fundamentals
```

Advanced mathematical knowledge is helpful for deeper study of:

```text
Number Theory
Modular Arithmetic
Abstract Algebra
Elliptic Curves
Complexity Theory
Probability
```

However, the module is structured so that practical cybersecurity concepts can be learned without requiring advanced mathematics at the beginning.

---

# 🗂️ Module Structure

```text
Cryptography/
│
├── README.md
│
├── Chapter 01 – Cryptography Fundamentals.md
├── Chapter 02 – Classical Cryptography & Historical Ciphers.md
├── Chapter 03 – Symmetric-Key Cryptography.md
├── Chapter 04 – Asymmetric-Key Cryptography.md
├── Chapter 05 – Hash Functions & Message Integrity.md
├── Chapter 06 – Message Authentication & MACs.md
├── Chapter 07 – Digital Signatures & PKI.md
├── Chapter 08 – Key Management & Key Exchange.md
├── Chapter 09 – Randomness, Nonces & Cryptographic Primitives.md
├── Chapter 10 – TLS, HTTPS & Cryptographic Protocols.md
├── Chapter 11 – Applied Cryptography & Common Attacks.md
└── Chapter 12 – Modern Cryptography & Post-Quantum Cryptography.md
```

---

# 🚀 End Goal

By the end of this module, you should be able to look at a security architecture and answer:

```text
What needs encryption?
        ↓
Which encryption model is appropriate?
        ↓
How are keys exchanged?
        ↓
How are keys generated?
        ↓
How are keys stored?
        ↓
How is integrity verified?
        ↓
How is identity authenticated?
        ↓
How is trust established?
        ↓
How can the implementation fail?
        ↓
How can the system be attacked?
        ↓
How should it be secured?
```

The ultimate objective is to move from:

> **"I know what AES, RSA, SHA-256 and TLS are."**

to:

> **"I understand how cryptographic primitives are combined into secure systems, how those systems fail, and how to evaluate their security."**

---

## 🔐 Cryptography Learning Path

```text
Fundamentals
     ↓
Classical Ciphers
     ↓
Symmetric Encryption
     ↓
Asymmetric Cryptography
     ↓
Hashing
     ↓
MACs
     ↓
Digital Signatures
     ↓
PKI
     ↓
Key Management
     ↓
Cryptographic Protocols
     ↓
Attacks & Secure Implementation
     ↓
Modern & Post-Quantum Cryptography
```

**12 chapters. One complete cryptography foundation—from basic ciphers to modern post-quantum security.**