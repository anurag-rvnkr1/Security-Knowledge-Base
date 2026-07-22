# A02:2021 – Cryptographic Failures

---

# Overview

**Cryptographic Failures** is the **second category in the OWASP Top 10 (2021)**. It refers to vulnerabilities that arise when applications fail to properly protect sensitive data using modern cryptographic techniques.

Before the 2021 release, this category was known as **Sensitive Data Exposure**. The name was changed because the real issue is not merely exposing data—it is the failure to correctly implement cryptography to protect that data.

Cryptography is the science of securing information so that only authorized parties can access or understand it. Modern applications rely on cryptography to protect:

- User passwords
- Credit card information
- Banking transactions
- Government records
- Healthcare data
- Authentication tokens
- API keys
- Personal Identifiable Information (PII)
- Business secrets

When cryptography is implemented incorrectly—or omitted entirely—attackers can intercept, steal, modify, or impersonate sensitive information.

---

# Why It Matters

Nearly every modern application processes sensitive information.

Examples include:

```
Banking Applications
↓

Account Numbers

Balances

Transactions
```

```
Healthcare Systems
↓

Medical Records

Prescriptions

Insurance Data
```

```
E-commerce Websites
↓

Passwords

Credit Cards

Addresses
```

If this data is not protected using strong cryptographic controls, attackers may exploit weaknesses to gain unauthorized access.

Possible consequences include:

- Identity theft
- Financial fraud
- Credential theft
- Regulatory fines (GDPR, HIPAA, PCI DSS)
- Business reputation damage
- Data breaches
- Customer trust loss
- Account takeover

Unlike Broken Access Control, which focuses on **who can access data**, Cryptographic Failures focus on **how sensitive data is protected**.

---

# Evolution of the Category

## OWASP Top 10 (2017)

The category was called:

```
A3: Sensitive Data Exposure
```

Many developers interpreted this as simply "data leakage."

However, investigations showed that the root problem was usually:

- Weak encryption
- Missing encryption
- Poor key management
- Weak TLS configuration
- Insecure password storage

To better reflect these root causes, OWASP renamed the category.

---

## OWASP Top 10 (2021)

```
A02: Cryptographic Failures
```

The new name emphasizes implementing cryptography correctly rather than focusing only on exposed data.

---

# Architecture / Diagram

## Secure Communication

```
Client

    │

HTTPS (TLS)

    │

Encrypted Data

    │

Server

    │

Encrypted Database

    │

Sensitive Information
```

Attackers intercepting traffic see only encrypted data.

---

## Insecure Communication

```
Client

    │

HTTP

    │

Plaintext Data

    │

Internet

    │

Attacker

    │

Reads Everything
```

Without encryption, usernames, passwords, cookies, and personal data may be exposed.

---

# Key Concepts

To understand Cryptographic Failures, it is important to understand several fundamental concepts.

---

# What Is Cryptography?

Cryptography is the practice of protecting information by transforming readable data into an unreadable format.

Only someone possessing the correct secret (a key) can recover the original information.

Example:

Original:

```
Password123
```

Encrypted:

```
4f8b7e9c3d91...
```

Without the correct key, recovering the original value should be computationally infeasible.

---

# Plaintext

Plaintext is the original, readable information before any cryptographic operation.

Example:

```
Username:

alice
```

```
Password:

Summer@2026
```

Anyone who intercepts plaintext can immediately read it.

---

# Ciphertext

Ciphertext is the encrypted version of plaintext.

Example:

```
a83fd91cd84efab92873...
```

Ciphertext should reveal no useful information without the appropriate cryptographic key.

---

# Encryption

Encryption converts plaintext into ciphertext using an algorithm and a cryptographic key.

```
Plaintext

↓

Encryption Algorithm

↓

Secret Key

↓

Ciphertext
```

Only authorized parties possessing the correct key should be able to decrypt the information.

---

# Decryption

Decryption reverses encryption.

```
Ciphertext

↓

Correct Key

↓

Original Plaintext
```

If an attacker lacks the key, the data should remain unreadable.

---

# The CIA Triad

Cryptography primarily supports the **Confidentiality** pillar of the CIA Triad, while also contributing to Integrity and, in some cases, Authentication.

```
        CIA Triad

      Confidentiality
             ▲
             │
Integrity ◄──┼──► Availability
```

## Confidentiality

Ensures that only authorized users can access sensitive information.

Example:

- HTTPS
- Database encryption
- VPNs

---

## Integrity

Ensures that data has not been altered.

Mechanisms include:

- Hash functions
- Digital signatures
- Message Authentication Codes (MACs)

---

## Availability

Ensures that authorized users can access systems and data when needed.

Although availability is not provided directly by encryption, secure key management and resilient cryptographic systems contribute to maintaining it.

---

# Encryption vs Hashing vs Encoding

These terms are frequently confused.

| Encryption | Hashing | Encoding |
|------------|----------|----------|
| Reversible | One-way | Reversible |
| Uses a key | No key | No key |
| Protects confidentiality | Verifies integrity | Data representation |
| Can be decrypted | Cannot be reversed (practically) | Easily decoded |

---

## Encryption Example

```
Original

↓

Encrypt

↓

Ciphertext

↓

Decrypt

↓

Original
```

Used for:

- Files
- Network traffic
- Databases
- Backups

---

## Hashing Example

```
Password

↓

SHA-256

↓

9b876b...

(No Decryption)
```

Hashing is commonly used for:

- Password verification
- File integrity
- Digital signatures

---

## Encoding Example

```
hello

↓

Base64

↓

aGVsbG8=
```

Base64 is **not encryption**.

Anyone can decode it:

```
aGVsbG8=

↓

hello
```

Encoding is designed for compatibility and data transport—not security.

---

# Why Base64 Is Not Secure

A common misconception among beginners is that Base64 "encrypts" data.

Example:

```
admin:password
```

Encoded:

```
YWRtaW46cGFzc3dvcmQ=
```

Anyone can decode it instantly.

Base64 provides **zero confidentiality**.

Never use Base64 to protect sensitive information.

---

# Real-World Uses of Cryptography

Modern systems rely on cryptography in many areas:

### Authentication

- Password hashing
- Multi-factor authentication
- OAuth tokens
- JWT signatures

### Secure Communication

- HTTPS (TLS)
- SSH
- VPNs
- Secure email

### Data Storage

- Encrypted databases
- Disk encryption
- Cloud storage encryption
- Backup encryption

### Digital Trust

- Certificates
- Code signing
- Digital signatures
- Software update verification

---

# Key Takeaways

- Cryptographic Failures occur when sensitive information is not adequately protected.
- The category was renamed from **Sensitive Data Exposure** to emphasize the importance of implementing cryptography correctly.
- Encryption protects confidentiality, while hashing verifies integrity.
- Base64 encoding is **not** a security mechanism.
- Strong cryptographic design is essential for protecting modern applications, user data, and communications.

# Core Cryptographic Concepts

To implement secure applications, it is essential to understand the major cryptographic techniques and where each should be used. Using the wrong cryptographic primitive—or using the right one incorrectly—is a common cause of security vulnerabilities.

---

# Symmetric Encryption

## Overview

Symmetric encryption uses **a single secret key** for both encryption and decryption.

```
          Secret Key
              │
              ▼
Plaintext → Encrypt → Ciphertext
                           │
                           ▼
                   Decrypt → Plaintext
              ▲
              │
          Same Secret Key
```

Both the sender and the receiver must know the same secret key.

---

## Advantages

- Very fast
- Efficient for large amounts of data
- Low CPU usage
- Ideal for databases, files, backups, and VPN traffic

---

## Disadvantages

- Secure key distribution is difficult
- If the key is compromised, all encrypted data is compromised
- Not suitable for exchanging secrets over an insecure channel

---

## Common Algorithms

### AES (Advanced Encryption Standard)

The current industry standard.

Supports:

- AES-128
- AES-192
- AES-256

Widely used in:

- HTTPS
- BitLocker
- FileVault
- VPNs
- Cloud Storage
- Database Encryption

---

### ChaCha20

A modern stream cipher.

Advantages:

- Very fast on mobile devices
- Excellent software performance
- Resistant to timing attacks

Frequently paired with:

```
ChaCha20-Poly1305
```

---

## Example

```
Message

↓

AES-256

↓

Ciphertext

↓

AES-256

↓

Original Message
```

---

# Asymmetric Encryption

## Overview

Asymmetric encryption uses **two mathematically related keys**.

```
Public Key

↓

Encrypt

↓

Ciphertext

↓

Private Key

↓

Decrypt
```

The keys are different.

```
Public Key

Can be shared.
```

```
Private Key

Must remain secret.
```

---

## Advantages

- No need to share a secret key beforehand
- Enables secure communication over the Internet
- Supports digital signatures
- Enables certificate-based authentication

---

## Disadvantages

- Much slower than symmetric encryption
- Computationally expensive
- Not suitable for encrypting large files

---

## Common Algorithms

### RSA

One of the oldest public-key algorithms.

Common key sizes:

```
2048-bit

3072-bit

4096-bit
```

Used for:

- Key exchange
- Digital signatures
- Certificates

---

### ECC (Elliptic Curve Cryptography)

Provides equivalent security with much smaller keys.

Advantages:

- Faster
- Smaller certificates
- Better mobile performance

Widely used in:

- TLS
- Mobile applications
- Cryptocurrency
- Modern authentication systems

---

# Why HTTPS Uses Both

Many people assume HTTPS uses only RSA.

It actually combines symmetric and asymmetric cryptography.

```
Browser

        │

Public Key

        │

Generate AES Session Key

        │

Encrypt Session Key

        │

Server

Decrypt Session Key

        │

Both now share AES Key

        │

Encrypted Communication
```

After the secure handshake, nearly all communication uses fast symmetric encryption (AES or ChaCha20).

---

# TLS (Transport Layer Security)

TLS secures communication between client and server.

Examples:

```
Browser

↓

HTTPS

↓

Web Server
```

```
Mobile App

↓

TLS

↓

API
```

```
Email Client

↓

TLS

↓

Mail Server
```

---

## TLS Handshake

Simplified process:

```
Client

↓

Hello

↓

Server

↓

Certificate

↓

Public Key Verification

↓

Generate Session Key

↓

Encrypted Channel

↓

Secure Communication
```

The handshake:

- Verifies server identity
- Negotiates encryption algorithms
- Establishes secure session keys

---

# Public Key Infrastructure (PKI)

PKI enables trust on the Internet.

```
Certificate Authority

↓

Signs Certificate

↓

Website

↓

Browser

↓

Trusted Connection
```

Without PKI, attackers could easily impersonate websites.

---

## Digital Certificates

A certificate contains:

- Domain Name
- Public Key
- Certificate Authority
- Expiration Date
- Signature
- Serial Number

Example:

```
www.bank.com

↓

Certificate

↓

Trusted
```

---

# Certificate Authorities (CA)

Examples:

- DigiCert
- GlobalSign
- Let's Encrypt
- Sectigo

Browsers trust these authorities.

If a certificate is signed by a trusted CA, browsers establish a secure connection.

---

# Digital Signatures

Encryption protects confidentiality.

Digital signatures protect:

- Authenticity
- Integrity
- Non-repudiation

Process:

```
Message

↓

Hash

↓

Private Key

↓

Digital Signature
```

Verification:

```
Message

↓

Hash

↓

Public Key

↓

Verify Signature
```

If verification succeeds:

✔ Message has not changed

✔ Sender is authentic

---

# Hash Functions

A cryptographic hash converts data into a fixed-length value.

```
Input

↓

SHA-256

↓

64-character Hash
```

Properties:

- Deterministic
- Fast
- One-way
- Collision resistant
- Avalanche effect

---

## Example

```
Password123

↓

SHA-256

↓

ef92b778...
```

Changing one character completely changes the output.

---

# Password Hashing

Passwords should **never** be encrypted for storage.

Instead:

```
Password

↓

Password Hash Function

↓

Store Hash
```

During login:

```
User Password

↓

Hash

↓

Compare

↓

Stored Hash
```

---

## Modern Password Hashing Algorithms

### Argon2

Winner of the Password Hashing Competition.

Recommended for new systems.

Provides protection against:

- GPU attacks
- ASIC attacks
- Rainbow tables

---

### bcrypt

Still widely used.

Features:

- Automatic salting
- Configurable work factor
- Resistant to brute-force attacks

---

### scrypt

Designed to require large amounts of memory.

Helps defend against specialized cracking hardware.

---

### PBKDF2

Recommended in many enterprise environments.

Uses:

- Iterations
- Salt
- Configurable work factor

---

## Never Use

❌ MD5

❌ SHA-1

❌ Plain SHA-256 for password storage

These algorithms are too fast and unsuitable for protecting passwords against offline attacks.

---

# Salting

A salt is a random value added before hashing.

Instead of:

```
Password

↓

Hash
```

Use:

```
Random Salt

+

Password

↓

Hash
```

Benefits:

- Prevents rainbow table attacks
- Ensures identical passwords produce different hashes
- Forces attackers to crack each password individually

---

## Example

User A

```
Password123
```

Salt

```
AB12
```

Stored:

```
AB12 + Hash
```

---

User B

Same password:

```
Password123
```

Different salt:

```
XY91
```

Different hash produced.

---

# Pepper

A pepper is an additional secret value stored separately from the database.

```
Password

+

Salt

+

Pepper

↓

Hash
```

Unlike salts, peppers are **not stored alongside user records**.

Even if the database is compromised, the attacker still needs the server-side pepper to verify guesses efficiently.

---

# Cryptographically Secure Random Number Generator (CSPRNG)

Randomness is essential for generating:

- Session IDs
- Password reset tokens
- API keys
- Encryption keys
- Initialization Vectors (IVs)
- Nonces

Weak random number generators can make these values predictable.

Examples of secure sources include:

- `/dev/urandom` (Linux)
- `os.urandom()` (Python)
- `SecureRandom` (Java)
- `crypto.randomBytes()` (Node.js)

Avoid general-purpose pseudo-random generators (such as `rand()` or `Math.random()`) for security-sensitive values.

---

# Key Management

Even the strongest encryption is ineffective if cryptographic keys are mishandled.

Best practices include:

- Generate strong keys using a CSPRNG.
- Store keys separately from encrypted data.
- Rotate keys periodically.
- Restrict key access using least privilege.
- Back up keys securely.
- Use dedicated key management systems (KMS) or Hardware Security Modules (HSMs) for sensitive environments.

---

# Key Takeaways

- **Symmetric encryption** is fast and ideal for protecting large amounts of data.
- **Asymmetric encryption** enables secure key exchange and digital signatures.
- **TLS** combines both approaches to secure Internet communications.
- **Hashing** is used for integrity and password verification, not confidentiality.
- Passwords should be stored using dedicated password-hashing algorithms such as **Argon2**, **bcrypt**, **scrypt**, or **PBKDF2**.
- Salts and peppers strengthen password storage against offline attacks.
- Secure random number generation and proper key management are critical components of any cryptographic system.