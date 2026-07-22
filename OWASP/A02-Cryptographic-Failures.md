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

# Common Cryptographic Misconfigurations

Cryptography is only as secure as its implementation. Even when strong algorithms are available, poor configuration or misuse can completely undermine security.

Many real-world data breaches are caused not by breaking encryption, but by **incorrect implementation**.

---

# 1. Using Weak or Deprecated Algorithms

## Overview

Older cryptographic algorithms were once considered secure but are now vulnerable due to advances in cryptanalysis and computing power.

Applications that continue using deprecated algorithms expose sensitive data to unnecessary risk.

---

## Insecure Algorithms

### DES (Data Encryption Standard)

```
Key Size:
56 bits
```

Problems:

- Extremely small key size
- Vulnerable to brute-force attacks
- Deprecated

---

### 3DES (Triple DES)

Improved upon DES but is now deprecated.

Problems:

- Slow performance
- Vulnerable to birthday attacks
- Replaced by AES

---

### RC4

Previously used in SSL/TLS.

Problems:

- Biased keystream
- Practical attacks exist
- Officially prohibited in modern TLS

---

### MD5

Originally designed as a cryptographic hash.

Problems:

- Collision attacks
- Fast cracking
- Unsuitable for password storage
- Unsuitable for digital signatures

Example:

```
Password

↓

MD5

↓

5f4dcc3b5aa765d61d8327deb882cf99
```

Attackers can recover many MD5 hashes within seconds using rainbow tables or GPUs.

---

### SHA-1

Once widely trusted.

Now vulnerable to collision attacks.

Should not be used for:

- Certificates
- Digital signatures
- Password storage

Use SHA-256 or SHA-3 instead.

---

# Secure Alternatives

| Deprecated | Recommended |
|------------|-------------|
| DES | AES-256 |
| 3DES | AES-GCM |
| RC4 | ChaCha20-Poly1305 |
| MD5 | SHA-256 / SHA-3 (integrity only) |
| SHA-1 | SHA-256 / SHA-3 |
| Plain SHA-256 (passwords) | Argon2, bcrypt, scrypt, PBKDF2 |

---

# 2. Hardcoded Secrets

One of the most common developer mistakes is embedding secrets directly into source code.

Example:

```python
API_KEY = "1234567890abcdef"
```

Or:

```java
String password = "admin123";
```

Or:

```javascript
const jwtSecret = "secret123";
```

If source code is leaked or pushed to GitHub, attackers immediately obtain these secrets.

---

## Secure Approach

Store secrets using:

- Environment variables
- Secret management systems
- Cloud KMS
- HashiCorp Vault
- AWS Secrets Manager
- Azure Key Vault
- Google Secret Manager

---

# 3. Weak Password Storage

## Insecure

```
password

↓

MD5

↓

Database
```

Attackers can recover millions of passwords rapidly using GPU-based cracking.

---

## Secure

```
Password

↓

Salt

↓

Argon2

↓

Database
```

Argon2 is intentionally slow and memory-intensive, making offline attacks significantly more expensive.

---

# 4. Missing HTTPS

Some applications still transmit sensitive data over HTTP.

```
Browser

↓

HTTP

↓

Internet

↓

Server
```

Traffic is transmitted in plaintext.

Attackers on the same network can capture:

- Usernames
- Passwords
- Session cookies
- Tokens
- Personal data

---

## Secure Version

```
Browser

↓

HTTPS

↓

TLS Encryption

↓

Server
```

The data is encrypted in transit.

---

# 5. Weak TLS Configuration

Even when HTTPS is enabled, poor TLS configuration can introduce vulnerabilities.

Examples include:

- TLS 1.0 enabled
- TLS 1.1 enabled
- Weak cipher suites
- Self-signed certificates in production
- Expired certificates
- Missing certificate validation
- Weak Diffie-Hellman parameters

---

## Recommended Configuration

Enable only modern protocols:

- TLS 1.2
- TLS 1.3

Disable:

- SSLv2
- SSLv3
- TLS 1.0
- TLS 1.1

---

# 6. Poor Key Management

Strong encryption is ineffective if cryptographic keys are mishandled.

Common mistakes:

- Keys stored in source code
- Keys committed to Git
- Same key shared across environments
- No key rotation
- No access control
- Keys stored with encrypted data

---

## Secure Key Lifecycle

```
Generate

↓

Store Securely

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

# 7. Predictable Random Values

Applications often generate:

- Session IDs
- Password reset tokens
- API keys
- JWT secrets

Using insecure generators such as:

```javascript
Math.random()
```

or:

```c
rand()
```

can produce predictable values.

---

## Secure Generators

Python:

```python
import secrets

token = secrets.token_urlsafe(32)
```

Node.js:

```javascript
crypto.randomBytes(32)
```

Java:

```java
SecureRandom random = new SecureRandom();
```

---

# 8. Sensitive Data Stored in Plaintext

Examples:

```
Database

↓

Passwords

↓

Credit Cards

↓

API Keys

↓

Medical Records
```

If the database is compromised, attackers immediately obtain usable information.

Sensitive information should be encrypted at rest where appropriate, and passwords should be hashed using dedicated password-hashing algorithms.

---

# 9. Improper Certificate Validation

Some applications ignore certificate validation errors.

Example (Python):

```python
requests.get(
    url,
    verify=False
)
```

This disables TLS certificate verification and makes the application vulnerable to Man-in-the-Middle (MITM) attacks.

Similarly, mobile applications that trust all certificates or implement insecure certificate validation are at risk.

---

# 10. Client-Side Encryption Misuse

Developers sometimes believe encrypting data in JavaScript alone is sufficient.

Example:

```
Browser

↓

Encrypt

↓

Send
```

However:

- Attackers control the browser environment.
- Client-side code can be modified.
- Encryption keys embedded in client-side code can be extracted.

Client-side encryption should complement—not replace—server-side security and proper key management.

---

# Real-World Example: Heartbleed (CVE-2014-0160)

Heartbleed was a critical vulnerability in OpenSSL's implementation of the TLS Heartbeat extension.

Impact:

- Allowed attackers to read portions of server memory.
- Potentially exposed private keys, passwords, cookies, and other sensitive data.
- Affected millions of servers worldwide.

The flaw was not caused by weak cryptographic algorithms, but by an implementation error in a widely used cryptographic library.

---

# Real-World Example: Equifax (2017)

The Equifax breach exposed personal information of approximately 147 million individuals.

Root cause:

- An unpatched Apache Struts vulnerability.

While not a cryptographic failure itself, the incident highlighted the importance of protecting sensitive data through layered security, including strong cryptography and key management.

---

# Detecting Cryptographic Failures

Security testing should verify:

- Is HTTPS enforced?
- Are strong TLS versions enabled?
- Are weak ciphers disabled?
- Are passwords hashed correctly?
- Are secrets exposed?
- Is certificate validation implemented correctly?
- Are encryption keys stored securely?
- Is sensitive data encrypted where appropriate?

---

# Manual Testing Checklist

✔ Verify HTTPS on every sensitive page.

✔ Check HTTP response headers.

✔ Inspect cookies (`Secure`, `HttpOnly`, `SameSite`).

✔ Identify weak TLS versions.

✔ Review certificate validity.

✔ Search source code for hardcoded secrets.

✔ Verify password hashing algorithms.

✔ Review key management practices.

---

# Key Takeaways

- Strong cryptographic algorithms are ineffective if implemented incorrectly.
- Avoid deprecated algorithms such as DES, RC4, MD5, and SHA-1.
- Never hardcode secrets or cryptographic keys.
- Always enforce HTTPS with modern TLS configurations.
- Protect passwords using dedicated password-hashing algorithms like Argon2 or bcrypt.
- Secure key management is just as important as selecting strong algorithms.

# Detection

Detecting cryptographic failures requires evaluating how sensitive data is protected both **in transit** and **at rest**. Security assessments should verify algorithms, protocol versions, key management, certificate validation, and secret handling.

---

# Manual Testing

## 1. Verify HTTPS Enforcement

Check whether all sensitive pages automatically redirect from HTTP to HTTPS.

Example:

```
http://example.com/login
```

Expected:

```
301/302 Redirect

↓

https://example.com/login
```

If credentials can be submitted over HTTP, the application is vulnerable.

---

## 2. Inspect TLS Configuration

Review:

- Supported TLS versions
- Cipher suites
- Certificate chain
- Key length
- Expiration date
- HSTS configuration

---

## 3. Inspect Cookies

Authentication cookies should include:

```
Secure
```

```
HttpOnly
```

```
SameSite=Lax
```

or

```
SameSite=Strict
```

Missing attributes increase the risk of session theft.

---

## 4. Search for Sensitive Data Exposure

Look for:

- Passwords
- API keys
- Access tokens
- JWT secrets
- Database credentials
- Credit card numbers
- Personal information

Inspect:

- HTML source
- JavaScript files
- API responses
- Mobile application packages
- Git repositories
- Configuration files

---

## 5. Review Password Storage

Verify that passwords use modern password hashing algorithms:

✔ Argon2

✔ bcrypt

✔ scrypt

✔ PBKDF2

Never store:

- Plaintext passwords
- MD5 hashes
- SHA-1 hashes
- Unsalted hashes

---

# Automated Detection

## Burp Suite

Useful for:

- Identifying HTTP endpoints
- Inspecting cookies
- Finding mixed content
- Reviewing security headers
- Detecting exposed secrets in responses

---

## Nmap

Check supported TLS versions:

```bash
nmap --script ssl-enum-ciphers \
-p 443 example.com
```

Provides:

- TLS versions
- Supported ciphers
- Weak cipher identification

---

## OpenSSL

Retrieve certificate details:

```bash
openssl s_client \
-connect example.com:443
```

Useful for verifying:

- Certificate chain
- Expiration
- Issuer
- Supported protocol

---

## SSL Labs

Analyze:

- TLS configuration
- Cipher suites
- Certificate quality
- HSTS
- Forward secrecy
- Overall security rating

---

# Prevention

Strong cryptography requires secure implementation, continuous maintenance, and disciplined key management.

---

## 1. Use Modern Algorithms

Encryption:

- AES-256-GCM
- ChaCha20-Poly1305

Integrity:

- SHA-256
- SHA-3

Password Storage:

- Argon2id
- bcrypt
- scrypt
- PBKDF2

---

## 2. Disable Weak Algorithms

Remove support for:

- DES
- 3DES
- RC4
- MD5
- SHA-1
- SSLv2
- SSLv3
- TLS 1.0
- TLS 1.1

---

## 3. Enforce HTTPS Everywhere

Every page handling sensitive information should use HTTPS.

Implement:

- HTTP → HTTPS redirects
- HSTS
- Secure cookies
- Modern TLS

---

## 4. Protect Secrets

Never hardcode:

- Passwords
- API keys
- JWT secrets
- Database credentials
- Encryption keys

Use:

- Environment variables
- Secret managers
- KMS/HSM solutions

---

## 5. Secure Key Management

Follow the full key lifecycle:

```
Generate

↓

Store

↓

Rotate

↓

Backup

↓

Revoke

↓

Destroy
```

Limit key access using least privilege and audit all key usage.

---

## 6. Encrypt Sensitive Data at Rest

Examples:

- Database encryption
- Disk encryption
- Backup encryption
- Object storage encryption

Only encrypt data that requires confidentiality, and manage keys separately from the encrypted data.

---

# Secure Coding Examples

## Python

Password hashing with `bcrypt`:

```python
import bcrypt

password = b"StrongPassword123!"

hashed = bcrypt.hashpw(
    password,
    bcrypt.gensalt()
)

print(hashed)
```

---

## Java

Generate secure random bytes:

```java
import java.security.SecureRandom;

SecureRandom random =
    new SecureRandom();

byte[] key = new byte[32];

random.nextBytes(key);
```

---

## Node.js

Generate a secure token:

```javascript
const crypto = require("crypto");

const token =
    crypto.randomBytes(32)
          .toString("hex");

console.log(token);
```

---

## Environment Variables

Instead of:

```python
SECRET_KEY = "admin123"
```

Use:

```python
import os

SECRET_KEY = os.getenv("SECRET_KEY")
```

---

# Best Practices

✔ Encrypt sensitive data in transit using TLS.

✔ Encrypt sensitive data at rest when appropriate.

✔ Use strong, well-vetted cryptographic algorithms.

✔ Hash passwords with dedicated password-hashing algorithms.

✔ Use unique salts for every password.

✔ Consider using a server-side pepper for additional protection.

✔ Rotate cryptographic keys periodically.

✔ Store secrets outside application code.

✔ Keep cryptographic libraries up to date.

✔ Validate TLS certificates correctly.

✔ Disable insecure protocols and cipher suites.

✔ Review cryptographic implementations during code reviews.

✔ Perform regular penetration testing and configuration audits.

---

# Useful Commands

## View Certificate

```bash
openssl s_client \
-connect example.com:443
```

---

## Check Certificate Dates

```bash
openssl x509 \
-noout \
-dates \
-in certificate.pem
```

---

## Generate SHA-256 Hash

```bash
echo "hello" | sha256sum
```

---

## Generate Random Bytes

```bash
openssl rand -hex 32
```

---

## Scan TLS Configuration

```bash
nmap \
--script ssl-enum-ciphers \
-p 443 example.com
```

---

# Practical Lab

## Objective

Assess the cryptographic posture of a web application.

---

## Lab Steps

1. Deploy or access a web application (e.g., OWASP Juice Shop).

2. Confirm all sensitive pages use HTTPS.

3. Inspect cookies for:

- Secure
- HttpOnly
- SameSite

4. Review the TLS certificate.

5. Scan supported TLS versions using Nmap.

6. Examine the certificate using OpenSSL.

7. Search responses and JavaScript files for exposed secrets.

8. Document findings and recommend mitigations.

---

## Expected Learning Outcomes

You should be able to:

- Evaluate HTTPS implementations.
- Identify weak TLS configurations.
- Recognize insecure password storage.
- Detect exposed secrets.
- Recommend modern cryptographic controls.

---

# Interview Questions

## Beginner

### What is a Cryptographic Failure?

A vulnerability caused by missing, weak, or improperly implemented cryptographic protections, resulting in exposure or compromise of sensitive information.

---

### Why was "Sensitive Data Exposure" renamed?

Because the underlying issue is incorrect implementation of cryptography rather than the exposure itself.

---

### What is the difference between encryption and hashing?

- Encryption is reversible with a key and provides confidentiality.
- Hashing is one-way and is primarily used for integrity verification and password storage.

---

### Why is Base64 not encryption?

Base64 is an encoding mechanism. It can be decoded by anyone and provides no confidentiality.

---

## Intermediate

### Why shouldn't passwords be encrypted?

Encrypted passwords can be decrypted if the key is compromised. Passwords should instead be hashed using dedicated password-hashing algorithms such as Argon2 or bcrypt.

---

### What is the purpose of a salt?

A salt is a unique random value added before hashing. It prevents identical passwords from producing identical hashes and defeats rainbow table attacks.

---

### What is the purpose of a pepper?

A pepper is a secret value stored separately from the database and combined with passwords before hashing. It adds an additional layer of defense if the password database is compromised.

---

### Why does HTTPS use both symmetric and asymmetric cryptography?

Asymmetric cryptography is used during the TLS handshake to establish trust and exchange session keys securely. Symmetric cryptography is then used for bulk data encryption because it is significantly faster.

---

## Advanced

### What is Forward Secrecy?

Forward Secrecy ensures that if a server's long-term private key is compromised, previously captured encrypted sessions remain secure because each session used a unique ephemeral key.

---

### Why is Argon2 preferred over MD5?

Argon2 is intentionally slow, memory-intensive, and resistant to GPU and ASIC attacks. MD5 is extremely fast and vulnerable to collisions, making it unsuitable for password storage.

---

### How would you assess an application's cryptographic implementation during a penetration test?

A thorough assessment includes:

- Verifying HTTPS enforcement.
- Reviewing TLS versions and cipher suites.
- Inspecting certificates.
- Checking cookie security attributes.
- Evaluating password storage.
- Searching for exposed secrets.
- Reviewing key management practices.
- Identifying deprecated algorithms or insecure protocol usage.

---

# References

## OWASP

- OWASP Top 10 (2021)
- OWASP Cryptographic Storage Cheat Sheet
- OWASP Transport Layer Security Cheat Sheet
- OWASP Password Storage Cheat Sheet
- OWASP ASVS
- OWASP Web Security Testing Guide

## Standards

- NIST SP 800-57 (Key Management)
- NIST SP 800-63B (Digital Identity Guidelines)
- FIPS 140-3
- RFC 8446 (TLS 1.3)

## MITRE

- CWE-295: Improper Certificate Validation
- CWE-321: Use of Hard-coded Cryptographic Key
- CWE-326: Inadequate Encryption Strength
- CWE-327: Use of a Broken or Risky Cryptographic Algorithm
- CWE-328: Use of Weak Hash

---

# Summary

Cryptographic Failures occur when applications fail to adequately protect sensitive information through proper cryptographic design and implementation. Strong algorithms alone are not sufficient—secure key management, modern TLS configurations, proper password hashing, certificate validation, and disciplined secret management are equally important.

By using well-established cryptographic standards, regularly reviewing implementations, and following OWASP and NIST guidance, organizations can significantly reduce the risk of data compromise and build resilient, trustworthy applications.