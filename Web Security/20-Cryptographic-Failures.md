# 20-Cryptographic-Failures.md

# Part 1 — Fundamentals of Cryptographic Failures, Data Protection, Encryption Concepts, and Enterprise Overview

> **"Cryptography is not about hiding information—it is about ensuring that only authorized parties can read, verify, and trust information throughout its lifecycle."**

---

# Learning Objectives

After completing this part, you will understand:

- What Cryptographic Failures Are
- Why Cryptography Matters
- Confidentiality, Integrity, and Authenticity
- Encryption Fundamentals
- Plaintext vs Ciphertext
- Keys and Key Management
- Cryptographic Goals
- Enterprise Data Protection
- Common Misconceptions
- Business Impact

---

# What are Cryptographic Failures?

**Cryptographic Failures** occur when sensitive information is not adequately protected due to incorrect, weak, or missing use of cryptographic controls.

These failures may involve:

- Missing encryption
- Weak encryption algorithms
- Poor key management
- Improper certificate handling
- Weak random number generation
- Incorrect implementation of cryptographic protocols

---

# Why Cryptography Matters

Modern applications continuously process sensitive information.

```
Web Application

│

├── User Credentials

├── Personal Information

├── Financial Records

├── Health Data

├── API Secrets

├── Authentication Tokens

├── Payment Information

└── Business Documents
```

Without proper cryptographic protection, unauthorized parties may gain access to confidential information.

---

# Security Goals of Cryptography

Cryptography supports multiple security objectives.

```
Cryptography

│

├── Confidentiality

├── Integrity

├── Authenticity

└── Non-Repudiation
```

Together, these goals help establish trust in digital systems.

---

# Confidentiality

Confidentiality ensures that information is accessible only to authorized parties.

```
Sensitive Data

↓

Encryption

↓

Ciphertext

↓

Authorized User

↓

Decryption

↓

Original Data
```

---

# Integrity

Integrity ensures that information has not been altered unexpectedly.

```
Original Data

↓

Integrity Verification

↓

Received Data

↓

Valid?

↓

Yes

OR

Integrity Failure
```

---

# Authenticity

Authenticity verifies the identity of the communicating party.

```
Client

↓

Identity Verification

↓

Trusted Server

↓

Secure Communication
```

Users should have confidence that they are communicating with the intended system.

---

# Non-Repudiation

Non-repudiation provides evidence that a specific action occurred.

```
Action

↓

Verification

↓

Evidence

↓

Audit Trail
```

This supports accountability in business transactions.

---

# Plaintext vs Ciphertext

```
Plaintext

↓

Encryption

↓

Ciphertext

↓

Decryption

↓

Plaintext
```

| Plaintext | Ciphertext |
|-----------|------------|
| Human-readable | Encrypted representation |
| Original information | Protected information |
| Directly understandable | Requires appropriate cryptographic processing |

---

# Encryption Overview

Encryption transforms readable information into a protected form.

```
Readable Data

↓

Encryption Process

↓

Protected Data

↓

Secure Storage

OR

Secure Transmission
```

Encryption reduces the likelihood of unauthorized disclosure.

---

# Keys

Cryptographic systems depend on keys.

```
Data

↓

Encryption Algorithm

+

Key

↓

Ciphertext
```

The security of encrypted data depends heavily on protecting cryptographic keys.

---

# Why Key Management Matters

```
Strong Encryption

+

Poor Key Management

↓

Weak Overall Security
```

A strong algorithm cannot compensate for exposed or poorly managed keys.

---

# Data at Rest

Data stored on devices or servers is referred to as **data at rest**.

```
Database

↓

Encrypted Storage

↓

Protected Data
```

Examples:

- Databases
- Backup files
- Hard drives
- Cloud storage
- Portable media

---

# Data in Transit

Information moving across networks is known as **data in transit**.

```
Client

↓

Network

↓

Server
```

Protecting data during transmission helps prevent interception and unauthorized disclosure.

---

# Data in Use

Data currently being processed by an application is known as **data in use**.

```
Application

↓

Memory

↓

Business Logic

↓

Response
```

Protecting data during processing is also an important consideration.

---

# Data Protection Lifecycle

```
Create

↓

Store

↓

Transmit

↓

Process

↓

Archive

↓

Delete
```

Sensitive information should be protected throughout its entire lifecycle.

---

# Enterprise Example

An online banking application handles:

```
Customer Login

↓

Authentication

↓

Account Data

↓

Transactions

↓

Statements

↓

Audit Logs
```

Each stage may require cryptographic protections appropriate to the data being handled.

---

# Trust Model

```
User

↓

Browser

↓

HTTPS

↓

Application

↓

Database

↓

Encrypted Storage
```

Multiple security controls work together to protect information.

---

# Cryptography in Enterprise Systems

```
Enterprise

│

├── Secure Login

├── Secure APIs

├── Database Protection

├── Backup Protection

├── Certificate Management

├── VPN

├── Email Security

└── Cloud Security
```

Cryptography is integrated into many different enterprise technologies.

---

# Common Causes of Cryptographic Failures

Examples include:

- Sensitive information stored without encryption
- Weak or obsolete algorithms
- Improper certificate validation
- Hardcoded secrets
- Poor key storage
- Weak randomness
- Misconfigured cryptographic libraries

---

# Business Impact

Cryptographic failures can result in:

```
Sensitive Data Exposure

↓

Loss of Customer Trust

↓

Financial Loss

↓

Legal Consequences

↓

Regulatory Penalties

↓

Reputation Damage
```

---

# Common Misconceptions

| Myth | Reality |
|------|---------|
| Encryption solves every security problem | Cryptography is only one layer of security |
| Strong algorithms alone provide security | Proper key management is equally important |
| Only financial applications require cryptography | Nearly all modern applications handle sensitive information |
| Encryption removes the need for access control | Cryptography and authorization complement each other |

---

# Enterprise Workflow

```
Sensitive Data

↓

Classify

↓

Apply Cryptographic Controls

↓

Secure Storage

↓

Secure Transmission

↓

Monitor

↓

Review
```

Organizations should classify data before determining appropriate protections.

---

# Hands-on Lab (Conceptual)

1. List different types of sensitive information in a sample web application.
2. Categorize the data as:
   - Data at rest
   - Data in transit
   - Data in use
3. Identify where cryptographic protection is required.
4. Discuss how poor key management could affect each category.
5. Document the potential business impact of exposing the data.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What are Cryptographic Failures?
2. Why was this OWASP category renamed from "Sensitive Data Exposure"?
3. What are the primary goals of cryptography?
4. What is the difference between plaintext and ciphertext?
5. What is a cryptographic key?
6. Why is key management important?
7. What is the difference between data at rest, data in transit, and data in use?
8. What business risks arise from cryptographic failures?
9. Why does encryption not replace access control?
10. Why should organizations classify data before applying cryptographic protections?

---

# Best Practices

- Identify and classify sensitive data before selecting cryptographic controls.
- Protect data throughout its lifecycle.
- Use well-established cryptographic libraries and protocols.
- Manage cryptographic keys securely.
- Regularly review cryptographic configurations and policies.
- Combine cryptography with authentication, authorization, logging, and monitoring.
- Train development teams on secure cryptographic practices.

---

# Common Mistakes

- Assuming encryption alone guarantees security.
- Storing sensitive information without protection.
- Treating key management as an afterthought.
- Using outdated or weak cryptographic mechanisms.
- Forgetting to protect backups and archived data.
- Ignoring the protection of data while it is being transmitted.

---

# Key Takeaways

- Cryptographic Failures involve the incorrect, weak, or missing use of cryptographic protections.
- Cryptography supports confidentiality, integrity, authenticity, and non-repudiation.
- Sensitive data should be protected at rest, in transit, and during processing.
- Strong cryptography requires secure key management.
- Enterprise security combines cryptography with other security controls to protect business-critical information.

# 20-Cryptographic-Failures.md

# Part 2 — Encryption Types, Hashing, Digital Signatures, Key Management, Certificates, and Enterprise Cryptography

> **"Strong cryptography is not achieved by selecting a secure algorithm alone. Security depends equally on proper key management, trusted certificates, secure implementation, and correct operational practices."**

---

# Learning Objectives

After completing this part, you will understand:

- Symmetric Encryption
- Asymmetric Encryption
- Hash Functions
- Digital Signatures
- Public Key Infrastructure (PKI)
- Certificates
- Key Management
- Cryptographic Randomness
- Enterprise Cryptography
- Common Cryptographic Weaknesses

---

# Types of Cryptography

Modern cryptography consists of several complementary techniques.

```
Cryptography

│

├── Symmetric Encryption

├── Asymmetric Encryption

├── Hash Functions

├── Digital Signatures

└── Certificate Infrastructure
```

Each serves a different security purpose.

---

# Symmetric Encryption

Symmetric encryption uses **one shared key** for both encryption and decryption.

```
Plaintext

↓

Encrypt

↓

Shared Secret Key

↓

Ciphertext

↓

Decrypt

↓

Shared Secret Key

↓

Plaintext
```

Both communicating parties must securely possess the same secret key.

---

# Characteristics of Symmetric Encryption

Advantages:

- Fast
- Efficient
- Suitable for large volumes of data

Challenges:

- Secure key distribution
- Key storage
- Key rotation
- Key compromise

---

# Enterprise Example

```
Database

↓

Sensitive Records

↓

Symmetric Encryption

↓

Encrypted Storage
```

Organizations commonly use symmetric encryption to protect stored data.

---

# Asymmetric Encryption

Asymmetric encryption uses **two mathematically related keys**.

```
Key Pair

│

├── Public Key

└── Private Key
```

The keys have different purposes and should never be confused.

---

# Asymmetric Encryption Workflow

```
Sender

↓

Public Key

↓

Encryption

↓

Ciphertext

↓

Private Key

↓

Decryption

↓

Recipient
```

The private key must remain confidential.

---

# Symmetric vs Asymmetric Encryption

| Symmetric | Asymmetric |
|------------|------------|
| One shared key | Public and private key pair |
| Faster | Slower |
| Suitable for bulk data | Suitable for key exchange and identity verification |
| Simpler mathematically | More computationally intensive |

---

# Hybrid Cryptography

Modern secure communication often combines both approaches.

```
Client

↓

Asymmetric Encryption

↓

Secure Session Key Exchange

↓

Symmetric Encryption

↓

Secure Communication
```

This combines the strengths of each technique.

---

# Hash Functions

Hash functions transform data into a fixed-length value.

```
Original Data

↓

Hash Function

↓

Hash Value
```

Hashes are designed for integrity verification rather than encryption.

---

# Properties of Hash Functions

A secure hash function should exhibit:

```
Input

↓

Hash Function

↓

Fixed-Length Output

↓

Integrity Verification
```

Desired characteristics include:

- Deterministic output
- Fixed output length
- Efficient computation
- Strong resistance to collisions and reversal

---

# Integrity Verification

```
Original File

↓

Hash

↓

Stored Hash

────────────

Received File

↓

Hash

↓

Compare

↓

Match?

↓

Integrity Verified
```

Matching hashes indicate the content has not changed.

---

# Encryption vs Hashing

| Encryption | Hashing |
|------------|----------|
| Protects confidentiality | Verifies integrity |
| Reversible with appropriate keys | Designed to be one-way |
| Produces ciphertext | Produces a hash value |
| Supports secure communication | Supports integrity verification |

---

# Digital Signatures

Digital signatures help verify authenticity and integrity.

Conceptually:

```
Document

↓

Digital Signature

↓

Transmission

↓

Verification

↓

Trusted?
```

Digital signatures provide confidence that content originates from the expected source and has not been altered unexpectedly.

---

# Why Digital Signatures Matter

```
Document

↓

Modified?

↓

Verification

↓

Success

OR

Failure
```

Verification failures indicate that integrity or authenticity cannot be confirmed.

---

# Public Key Infrastructure (PKI)

PKI provides a framework for managing digital certificates and trust relationships.

```
PKI

│

├── Certificates

├── Public Keys

├── Private Keys

├── Certificate Authorities

└── Trust Chain
```

PKI enables secure communication across untrusted networks.

---

# Digital Certificates

Certificates associate a public key with an identity.

```
Organization

↓

Certificate

↓

Trusted Identity

↓

Secure Communication
```

Certificates help browsers and applications establish trust.

---

# Certificate Chain

```
Root Authority

↓

Intermediate Authority

↓

Server Certificate

↓

Browser Trust
```

Each level contributes to establishing trust.

---

# Certificate Validation

Before establishing secure communication:

```
Certificate Received

↓

Validity Check

↓

Trusted Issuer?

↓

Expiration Check

↓

Accept

OR

Reject
```

Certificates should be valid, trusted, and unexpired.

---

# Key Management Lifecycle

Cryptographic keys require management throughout their lifecycle.

```
Generate

↓

Store

↓

Use

↓

Rotate

↓

Archive

↓

Destroy
```

Improper key management can undermine otherwise strong cryptographic systems.

---

# Key Rotation

Organizations periodically replace cryptographic keys.

```
Existing Key

↓

New Key Generated

↓

Migration

↓

Old Key Retired
```

Regular rotation limits the impact of long-term key exposure.

---

# Secure Key Storage

Keys should be protected separately from encrypted data.

```
Encrypted Data

↓

Application

↓

Secure Key Storage

↓

Key Retrieval

↓

Decryption
```

Separating keys from protected data reduces overall risk.

---

# Random Number Generation

Many cryptographic operations rely on unpredictable random values.

```
Random Source

↓

Cryptographic Operation

↓

Secure Output
```

Predictable randomness can weaken cryptographic protections.

---

# Secrets Management

Applications often rely on sensitive secrets.

Examples include:

- API keys
- Database credentials
- Encryption keys
- Signing keys
- Authentication secrets

Secrets should be managed securely throughout their lifecycle.

---

# Enterprise Cryptography

```
Enterprise

│

├── TLS

├── Database Encryption

├── Disk Encryption

├── VPN

├── Secure Email

├── Cloud Storage

├── Authentication Tokens

└── Digital Certificates
```

Cryptography is integrated into numerous enterprise technologies.

---

# Enterprise Cryptographic Workflow

```
Sensitive Data

↓

Classification

↓

Encryption

↓

Secure Storage

↓

Transmission

↓

Monitoring

↓

Key Rotation

↓

Audit
```

---

# Common Cryptographic Weaknesses

| Weakness | Security Impact |
|----------|-----------------|
| Weak key management | Key exposure |
| Hardcoded secrets | Unauthorized access |
| Expired certificates | Trust failures |
| Weak randomness | Predictable cryptographic values |
| Improper certificate validation | Increased communication risk |
| Shared secrets without proper management | Larger compromise impact |

---

# Hands-on Lab (Conceptual)

1. List where a sample application uses cryptography.
2. Classify each use as:
   - Symmetric encryption
   - Asymmetric encryption
   - Hashing
   - Digital signatures
3. Create a conceptual key lifecycle.
4. Identify where certificates would be required.
5. Document potential risks associated with poor key management.

> Perform all testing only in environments where you have explicit authorization.

---

# Interview Questions

1. What is the difference between symmetric and asymmetric encryption?
2. Why is symmetric encryption generally faster?
3. What is a cryptographic hash function?
4. How does hashing differ from encryption?
5. What is a digital signature?
6. What is PKI?
7. Why are digital certificates important?
8. What is key rotation?
9. Why should cryptographic keys be stored securely?
10. Why is cryptographically secure randomness important?

---

# Best Practices

- Use well-established cryptographic algorithms and libraries.
- Separate encrypted data from cryptographic keys.
- Rotate keys according to organizational policy.
- Validate certificates before establishing trust.
- Protect secrets using dedicated secrets management solutions.
- Monitor certificate expiration and renewal.
- Review cryptographic configurations periodically.

---

# Common Mistakes

- Confusing encryption with hashing.
- Hardcoding secrets into application code.
- Leaving expired certificates in production.
- Using predictable random values for cryptographic operations.
- Failing to rotate long-lived keys.
- Storing encryption keys alongside encrypted data.

---

# Key Takeaways

- Symmetric and asymmetric encryption serve different purposes and are often used together.
- Hashing supports integrity verification rather than confidentiality.
- Digital signatures provide authenticity and integrity assurance.
- PKI and certificates establish trust in secure communications.
- Strong cryptography depends on secure key management, certificate validation, and proper operational practices.

```text id="rrks28"
**Next:** Part 3
```