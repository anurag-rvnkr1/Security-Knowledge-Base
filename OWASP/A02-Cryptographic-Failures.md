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