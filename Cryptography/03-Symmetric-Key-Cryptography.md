# Chapter 03 – Symmetric-Key Cryptography

## Overview

**Symmetric-key cryptography** is a cryptographic approach in which the communicating parties use shared secret key material to perform cryptographic operations.

It is one of the most important foundations of modern information security because symmetric algorithms are generally efficient enough to protect large amounts of data.

A simplified model is:

```text
                 Shared Secret Key
                  /            \
                 ▼              ▼
              Sender         Receiver
                 │              ▲
                 ▼              │
             Encryption     Decryption
                 │              │
                 ▼              │
              Ciphertext ───────┘
```

Symmetric cryptography is commonly used for:

- File encryption
- Disk encryption
- Database encryption
- Network traffic
- TLS session encryption
- VPNs
- Secure messaging
- Cloud storage
- Application data protection

Modern systems commonly use algorithms and constructions such as:

```text
AES
ChaCha20
AES-GCM
ChaCha20-Poly1305
```

---

# 1. What is Symmetric Cryptography?

Symmetric cryptography uses a shared secret key.

Conceptually:

```text
Plaintext
    +
Secret Key
    ↓
Encryption Algorithm
    ↓
Ciphertext
```

The recipient uses the appropriate shared key to recover the plaintext:

```text
Ciphertext
    +
Secret Key
    ↓
Decryption Algorithm
    ↓
Plaintext
```

The key must be protected from unauthorized parties.

---

# 2. Basic Symmetric Encryption Model

Let:

```text
P = Plaintext
K = Secret Key
E = Encryption Function
C = Ciphertext
```

Encryption:

```text
C = E(K, P)
```

Decryption:

```text
P = D(K, C)
```

Where:

```text
D(K, E(K, P)) = P
```

for a valid encryption/decryption pair.

---

# 3. Main Characteristics

Symmetric cryptography generally provides:

```text
High Performance
Efficient Bulk Encryption
Lower Computational Cost
Small Ciphertext Overhead
```

However, it introduces a major challenge:

```text
How do communicating parties securely obtain the shared secret key?
```

This is known as the **key distribution problem**.

---

# 4. Symmetric Key Distribution Problem

Suppose:

```text
Alice
  │
  │ needs secret key
  ▼
Bob
```

Alice and Bob need the same secret:

```text
K
```

But sending:

```text
K
```

over an insecure network can expose it to an attacker.

Therefore:

```text
Symmetric Encryption
        +
Secure Key Establishment
```

are usually combined in modern systems.

Examples of key-establishment mechanisms include:

```text
Diffie-Hellman
ECDH
Pre-shared keys
Key management systems
```

---

# 5. Symmetric vs Asymmetric Cryptography

| Feature | Symmetric | Asymmetric |
|---|---|---|
| Key model | Shared secret | Public/private pair |
| Performance | Generally fast | Generally slower |
| Bulk encryption | Excellent | Usually inefficient |
| Key distribution | Challenging | Easier for public keys |
| Digital signatures | No | Yes |
| Examples | AES, ChaCha20 | RSA, ECC |

Modern protocols often combine both.

---

# 6. Hybrid Encryption

A common architecture is:

```text
              Asymmetric Cryptography
                        │
                        ▼
                 Key Establishment
                        │
                        ▼
                 Session Key
                        │
                        ▼
              Symmetric Encryption
                        │
                        ▼
                  Application Data
```

For example, TLS can use public-key mechanisms during connection establishment and symmetric authenticated encryption for application traffic.

---

# 7. Types of Symmetric Ciphers

Symmetric cryptography can broadly be divided into:

```text
Block Ciphers
      +
Stream Ciphers
```

---

# 8. Block Cipher

A block cipher processes data in fixed-size blocks.

Conceptually:

```text
Plaintext
   │
   ├── Block 1
   ├── Block 2
   ├── Block 3
   └── Block 4
        │
        ▼
    Block Cipher
        │
        ▼
   Ciphertext Blocks
```

Examples:

```text
AES
DES
3DES
```

---

# 9. Stream Cipher

A stream cipher encrypts data using a generated keystream.

Conceptually:

```text
Plaintext
    XOR
Keystream
    ↓
Ciphertext
```

Examples include:

```text
ChaCha20
```

Historically:

```text
RC4
```

was widely used but is now considered insecure and should not be used in modern systems.

---

# 10. Block Cipher vs Stream Cipher

| Property | Block Cipher | Stream Cipher |
|---|---|---|
| Processing | Fixed-size blocks | Stream of bytes/bits |
| Example | AES | ChaCha20 |
| Padding | May be required depending on mode | Generally unnecessary |
| Common use | Bulk encryption | Network streams |
| Modern authenticated use | AES-GCM | ChaCha20-Poly1305 |

The distinction can become less rigid in modern constructions, but it remains useful conceptually.

---

# 11. DES

**DES (Data Encryption Standard)** was historically one of the most important symmetric block ciphers.

It uses:

```text
64-bit block size
56-bit effective key
```

The original key representation is 64 bits, but 8 bits are used for parity, leaving 56 effective key bits.

---

# 12. DES Structure

DES uses a Feistel-style structure with multiple rounds.

Simplified:

```text
Plaintext
    ↓
Initial Transformation
    ↓
Multiple Feistel Rounds
    ↓
Final Transformation
    ↓
Ciphertext
```

DES was once considered secure but is now obsolete.

---

# 13. Why DES is Insecure

The major problem is its small effective key size:

```text
56 bits
```

Modern computing makes exhaustive key search practical enough that DES is not suitable for protecting modern sensitive data.

Therefore:

```text
Do not use DES.
```

---

# 14. 3DES

**Triple DES (3DES)** applies the DES primitive multiple times.

A common construction is:

```text
Encrypt
   ↓
Decrypt
   ↓
Encrypt
```

This is often represented as:

```text
EDE
```

3DES significantly increased security compared with DES, but it is now considered legacy technology.

For new systems:

```text
Use AES instead.
```

---

# 15. AES

**AES (Advanced Encryption Standard)** is one of the most widely used modern symmetric encryption algorithms.

AES operates on:

```text
128-bit blocks
```

Supported key sizes include:

```text
128 bits
192 bits
256 bits
```

AES is used in:

```text
TLS
VPNs
Disk Encryption
Cloud Encryption
Database Encryption
Applications
Secure Storage
```

---

# 16. AES Variants

AES supports three standard key sizes:

| AES Variant | Key Size | Block Size |
|---|---:|---:|
| AES-128 | 128 bits | 128 bits |
| AES-192 | 192 bits | 128 bits |
| AES-256 | 256 bits | 128 bits |

The block size remains:

```text
128 bits
```

regardless of key size.

---

# 17. AES Rounds

AES uses a different number of rounds depending on key size.

```text
AES-128 → 10 rounds
AES-192 → 12 rounds
AES-256 → 14 rounds
```

The internal transformations include:

```text
SubBytes
ShiftRows
MixColumns
AddRoundKey
```

The final round omits MixColumns.

---

# 18. AES Internal Structure

A simplified view:

```text
Input Block
     │
     ▼
AddRoundKey
     │
     ▼
┌───────────────┐
│ SubBytes      │
│ ShiftRows     │
│ MixColumns    │
│ AddRoundKey   │
└───────────────┘
     │
     ▼
     ...
     │
     ▼
Final Round
     │
     ▼
Ciphertext
```

The exact internal mathematics is more detailed than this conceptual representation.

---

# 19. SubBytes

SubBytes applies a nonlinear substitution to each byte using the AES S-box.

Conceptually:

```text
Input Byte
    ↓
S-Box
    ↓
Substituted Byte
```

This contributes to:

```text
Confusion
```

---

# 20. ShiftRows

ShiftRows rearranges the bytes in the AES state matrix.

Conceptually:

```text
Before:

A B C D
E F G H
I J K L
M N O P

After:

A B C D
F G H E
K L I J
P M N O
```

The exact shifts depend on the row.

This contributes to diffusion.

---

# 21. MixColumns

MixColumns transforms each column of the AES state using finite-field arithmetic.

Conceptually:

```text
Column
  ↓
Mathematical Transformation
  ↓
Mixed Column
```

This spreads the influence of individual bytes across the state.

---

# 22. AddRoundKey

AddRoundKey combines the current state with a round key using XOR.

```text
State
  XOR
Round Key
  ↓
New State
```

This introduces secret-key material into each round.

---

# 23. AES Key Expansion

The original AES key is expanded into multiple round keys.

Conceptually:

```text
Original Key
     ↓
Key Expansion
     ↓
Round Key 0
Round Key 1
Round Key 2
...
Round Key N
```

Each round uses the appropriate round key.

---

# 24. AES Security

AES is considered secure when:

```text
Modern Key Size
+
Secure Mode
+
Correct Nonce / IV Handling
+
Secure Key Management
+
Correct Implementation
```

is used.

AES itself does not solve:

```text
Authentication
Key Distribution
Key Storage
Nonce Management
```

These are system-level concerns.

---

# 25. AES Key Size Selection

Common choices:

```text
AES-128
AES-256
```

Both provide strong security when used correctly.

AES-256 provides a larger keyspace, while AES-128 already offers a very large security margin against conventional brute-force attacks.

The correct choice depends on:

```text
Threat Model
Performance
Standards
Compliance
Long-Term Security Requirements
```

---

# 26. Block Cipher Modes of Operation

A block cipher alone is not normally enough to encrypt arbitrary-length messages safely.

A **mode of operation** defines how blocks are processed.

Important modes include:

```text
ECB
CBC
CTR
GCM
```

The mode can dramatically affect security.

---

# 27. ECB Mode

**Electronic Codebook (ECB)** encrypts each block independently.

Conceptually:

```text
P1 → AES(K) → C1
P2 → AES(K) → C2
P3 → AES(K) → C3
```

Identical plaintext blocks produce identical ciphertext blocks.

---

# 28. ECB Pattern Leakage

If:

```text
P1 = P3
```

then:

```text
C1 = C3
```

This can expose structural patterns.

Therefore:

```text
ECB should generally not be used for encrypting structured data.
```

---

# 29. ECB Diagram

```text
Plaintext:

[Block A] [Block B] [Block A]

     │         │         │
     ▼         ▼         ▼

    AES       AES       AES
     │         │         │
     ▼         ▼         ▼

[Cipher A] [Cipher B] [Cipher A]
```

The repeated structure remains visible.

---

# 30. CBC Mode

**Cipher Block Chaining (CBC)** chains blocks together.

For the first block:

```text
P1 XOR IV
     ↓
   AES
     ↓
C1
```

For later blocks:

```text
P2 XOR C1
     ↓
   AES
     ↓
C2
```

---

# 31. CBC Encryption Formula

For the first block:

```text
C1 = E(K, P1 XOR IV)
```

For subsequent blocks:

```text
Ci = E(K, Pi XOR C(i-1))
```

Decryption:

```text
P1 = D(K, C1) XOR IV
```

and:

```text
Pi = D(K, Ci) XOR C(i-1)
```

---

# 32. CBC IV

CBC requires an initialization vector.

The IV generally does not need to be secret.

However, for secure CBC encryption, the IV must be generated according to the security requirements of the mode, typically unpredictably and freshly for each encryption.

---

# 33. CBC Padding

Because AES has:

```text
128-bit blocks
```

plaintext may need padding if its length is not an exact multiple of the block size.

A common padding scheme is:

```text
PKCS#7
```

Example concept:

```text
Plaintext:
HELLO

Padding:
HELLO + padding bytes
```

The exact padding depends on the block size and plaintext length.

---

# 34. CBC Padding Oracle

CBC implementations can become vulnerable to **padding oracle attacks** when they expose information about padding validity through distinguishable behavior.

Conceptually:

```text
Attacker
   │
   ▼
Modified Ciphertext
   │
   ▼
Application
   │
   ├── Valid Padding
   └── Invalid Padding
```

If the attacker can reliably distinguish these outcomes, they may recover plaintext under vulnerable constructions.

The lesson is:

> Avoid exposing distinguishable decryption errors and prefer modern authenticated encryption.

---

# 35. CTR Mode

**Counter (CTR) mode** turns a block cipher into a stream-like construction.

Conceptually:

```text
Nonce + Counter
      ↓
    AES
      ↓
Keystream
      ↓
   XOR with
   Plaintext
      ↓
 Ciphertext
```

---

# 36. CTR Encryption

For block `i`:

```text
Keystream_i = AES(K, Nonce || Counter_i)
```

Then:

```text
Ciphertext_i = Plaintext_i XOR Keystream_i
```

---

# 37. CTR Nonce Reuse

Reusing the same nonce/counter combination with the same key is dangerous.

Suppose:

```text
C1 = P1 XOR KS
C2 = P2 XOR KS
```

Then:

```text
C1 XOR C2
=
P1 XOR P2
```

The same fundamental problem appears as with OTP key reuse.

Therefore:

```text
Never reuse a CTR nonce/counter combination with the same key.
```

---

# 38. GCM

**Galois/Counter Mode (GCM)** combines:

```text
CTR-style encryption
+
Authentication
```

It is an **AEAD** construction.

AEAD means:

```text
Authenticated Encryption with Associated Data
```

GCM provides:

```text
Confidentiality
+
Integrity
+
Authentication of ciphertext and associated data
```

---

# 39. AES-GCM

AES-GCM is one of the most widely used modern authenticated-encryption constructions.

Conceptually:

```text
Plaintext
   +
Key
   +
Nonce
   +
AAD
   ↓
AES-GCM
   ↓
Ciphertext + Authentication Tag
```

---

# 40. GCM Authentication Tag

GCM produces an authentication tag.

The recipient verifies the tag before accepting the decrypted plaintext.

```text
Ciphertext
     +
Authentication Tag
     ↓
Verification
     ↓
Valid / Invalid
```

If verification fails:

```text
Reject message
```

The application should not treat unauthenticated plaintext as trustworthy.

---

# 41. GCM Nonce Requirements

Nonce management is critical.

For common GCM usage:

```text
Never reuse a nonce with the same key.
```

Nonce reuse can seriously compromise both confidentiality and authentication.

This is one of the most important practical rules when using AES-GCM.

---

# 42. Associated Authenticated Data

GCM can authenticate data without encrypting it.

Example:

```text
AAD:
Content-Type: application/json
```

The AAD remains visible but cannot be modified without causing authentication failure.

Conceptually:

```text
             ┌── Plaintext ──→ Encrypted
             │
AES-GCM ─────┤
             │
             └── AAD ────────→ Authenticated
```

---

# 43. AEAD

**Authenticated Encryption with Associated Data** combines:

```text
Encryption
+
Integrity
+
Authentication
```

Common AEAD constructions include:

```text
AES-GCM
ChaCha20-Poly1305
```

AEAD is generally preferred over manually combining separate encryption and authentication mechanisms when a vetted AEAD construction is available.

---

# 44. ChaCha20

**ChaCha20** is a modern stream cipher designed by Daniel J. Bernstein.

It operates using:

```text
256-bit key
Nonce
Counter
```

It is designed for high performance and strong security.

---

# 45. ChaCha20-Poly1305

ChaCha20 is commonly paired with:

```text
Poly1305
```

to form:

```text
ChaCha20-Poly1305
```

This is an AEAD construction.

It provides:

```text
Confidentiality
+
Integrity
+
Authentication
```

---

# 46. AES-GCM vs ChaCha20-Poly1305

| Feature | AES-GCM | ChaCha20-Poly1305 |
|---|---|---|
| Encryption primitive | AES | ChaCha20 |
| Authentication | GHASH | Poly1305 |
| Type | AEAD | AEAD |
| Common key size | 128/256-bit AES key | 256-bit |
| Common use | TLS, storage, applications | TLS, mobile/software environments |
| Hardware acceleration | Often available | Not required |
| Nonce reuse | Dangerous | Dangerous |

Both are widely used modern AEAD constructions.

---

# 47. Stream Cipher Key Reuse

For stream-like encryption:

```text
Ciphertext = Plaintext XOR Keystream
```

If the same keystream is reused:

```text
C1 XOR C2 = P1 XOR P2
```

Therefore:

```text
Unique nonce / counter
```

management is essential.

---

# 48. Initialization Vector vs Nonce

These terms are related but not always interchangeable.

### IV

An input used to initialize certain cryptographic modes.

### Nonce

A value intended to be used once in a particular cryptographic context.

The exact required property depends on the algorithm.

For example:

```text
CBC → IV requirements include unpredictability
CTR → nonce/counter uniqueness
GCM → nonce uniqueness is critical
```

Do not assume every IV or nonce follows the same rule.

---

# 49. Padding

Padding adds extra bytes so plaintext fits the required block size.

Example:

```text
Plaintext length = 10 bytes
Block size       = 16 bytes
```

Padding is required for some block cipher modes.

However:

```text
CTR
GCM
ChaCha20
```

do not require traditional block-padding because they operate in stream-like/AEAD constructions.

---

# 50. PKCS#7 Padding

For a block size of 16 bytes:

```text
Plaintext length = 14 bytes
```

Two padding bytes are added:

```text
02 02
```

If the plaintext already fills the entire block:

```text
16 bytes
```

a complete padding block may be added:

```text
10 10 10 ... 10
```

---

# 51. Padding Mistakes

Common problems include:

```text
Incorrect Padding Validation
Padding Oracle
Improper Error Handling
Manual Padding Bugs
```

Using modern AEAD modes avoids many of these issues.

---

# 52. Encryption Does Not Automatically Mean Authentication

This is a critical concept.

Suppose:

```text
AES-CTR
```

is used alone.

It can provide confidentiality, but an attacker may be able to modify ciphertext without the recipient detecting the modification.

Therefore:

```text
Encryption
≠
Authentication
```

Prefer:

```text
AEAD
```

where appropriate.

---

# 53. Encrypt-then-MAC

One historical construction is:

```text
Plaintext
   ↓
Encrypt
   ↓
Ciphertext
   ↓
MAC
   ↓
Authenticated Ciphertext
```

This is generally safer than some alternative composition orders when designed correctly.

However, modern applications should usually use standardized AEAD constructions rather than designing their own composition.

---

# 54. MAC-then-Encrypt

Conceptually:

```text
Plaintext
   ↓
MAC
   ↓
Plaintext + MAC
   ↓
Encrypt
```

This has historically been used in some protocols but can introduce subtle issues depending on implementation.

Modern protocol design generally favors robust AEAD constructions.

---

# 55. Encrypt-and-MAC

Conceptually:

```text
Plaintext
 ├──→ Encrypt
 │
 └──→ MAC
```

The exact security properties depend on the construction and how the outputs are combined.

Again:

```text
Use standardized AEAD
```

instead of inventing cryptographic composition.

---

# 56. Why AEAD is Preferred

AEAD provides a well-defined interface:

```text
Encrypt(
    key,
    nonce,
    plaintext,
    associated_data
)
```

producing:

```text
ciphertext + authentication tag
```

and:

```text
Decrypt(
    key,
    nonce,
    ciphertext,
    associated_data
)
```

returns plaintext only if authentication succeeds.

---

# 57. Secure Symmetric Encryption Model

A modern conceptual model is:

```text
                 Secret Key
                     │
                     ▼
Plaintext ───────► AEAD
                     ▲
                     │
                  Nonce
                     │
                     +
                    AAD
                     │
                     ▼
              Ciphertext + Tag
```

The receiver verifies the tag before accepting the plaintext.

---

# 58. Key Management

The encryption algorithm is only one part of the system.

You also need:

```text
Key Generation
Key Storage
Key Distribution
Key Rotation
Key Revocation
Key Destruction
```

A strong algorithm with a leaked key provides no meaningful confidentiality.

---

# 59. Key Generation

Keys should be generated using cryptographically secure randomness.

Avoid:

```python
import random
```

for cryptographic key generation.

Use a cryptographically secure source provided by the operating system or a trusted cryptographic library.

---

# 60. Python Secure Randomness

Python provides:

```python
import secrets

key = secrets.token_bytes(32)

print(key.hex())
```

For security-sensitive randomness, use APIs designed for cryptographic purposes.

---

# 61. AES Key Storage

Avoid:

```python
AES_KEY = "password123"
```

Prefer:

```text
Secrets Manager
KMS
HSM
Protected Environment Configuration
Secure Key Store
```

depending on the environment.

---

# 62. Key Rotation

Keys should be rotated according to:

```text
Threat Model
Compliance
Key Lifetime
Data Sensitivity
Operational Requirements
```

Rotation should not be treated as a substitute for preventing key compromise.

---

# 63. Key Compromise

If a symmetric key is compromised:

```text
Attacker obtains key
       ↓
Can potentially decrypt protected data
       ↓
Contain
       ↓
Rotate key
       ↓
Assess exposed data
       ↓
Recover
```

The exact impact depends on:

```text
Key lifetime
Data lifetime
Encryption architecture
Forward secrecy
Key separation
```

---

# 64. Key Separation

Do not unnecessarily use one key for unrelated purposes.

Instead:

```text
Master Secret
     ↓
KDF
     ├── Encryption Key
     ├── Authentication Key
     └── Other Derived Keys
```

This reduces cross-protocol and cross-purpose risks.

---

# 65. Key Derivation with HKDF

A simplified model:

```text
Input Key Material
       ↓
HKDF
       ↓
Derived Key 1
Derived Key 2
Derived Key 3
```

This allows applications to derive independent keys for different purposes.

---

# 66. Data at Rest

Symmetric encryption is commonly used to protect stored data.

Examples:

```text
Disk Encryption
Database Encryption
File Encryption
Object Storage Encryption
Backup Encryption
```

Conceptually:

```text
Application
     ↓
Encrypted Data
     ↓
Storage
```

---

# 67. Data in Transit

Symmetric encryption is also used for network traffic.

Example:

```text
Client
   │
   │ TLS
   │
   ▼
Server
```

After the TLS handshake establishes appropriate session keys, symmetric AEAD commonly protects application data.

---

# 68. Data in Use

Traditional encryption does not automatically protect data while an application is actively processing plaintext.

Conceptually:

```text
Encrypted at Rest
      ↓
Decryption
      ↓
Plaintext in Memory
      ↓
Processing
```

Protecting data in use may require additional mechanisms such as:

```text
Memory Protection
Hardware-backed Trusted Execution Environments
Application Isolation
Access Control
```

---

# 69. Disk Encryption

Disk encryption protects data stored on a device.

Examples:

```text
Full-Disk Encryption
Volume Encryption
File-Level Encryption
```

Important distinction:

```text
Disk encryption protects stored data
```

but may not protect against:

```text
An already-compromised running system
```

---

# 70. Database Encryption

Database systems may use:

```text
Transparent Data Encryption
Column-Level Encryption
Application-Level Encryption
```

Each provides different security and operational properties.

Application-level encryption may provide stronger separation from database administrators in some threat models, but also increases key-management complexity.

---

# 71. Envelope Encryption

Envelope encryption uses a hierarchy of keys.

Conceptually:

```text
Data
 ↓
Data Encryption Key (DEK)
 ↓
Encrypted Data

DEK
 ↓
Key Encryption Key (KEK)
 ↓
Encrypted DEK
```

This is widely used in cloud and enterprise key management.

---

# 72. Envelope Encryption Flow

```text
                Master / KEK
                    │
                    ▼
             Encrypt DEK
                    │
                    ▼
              Encrypted DEK
                    │
                    │
Data ──→ DEK ──→ Ciphertext
```

The master key does not need to directly encrypt every data block.

---

# 73. Why Envelope Encryption is Useful

It allows:

```text
Fast Data Encryption
+
Centralized Key Management
+
Key Rotation
+
Separation of Data and Key Protection
```

A KMS can manage higher-level keys while applications use short-lived or data-specific encryption keys.

---

# 74. Key Wrapping

Key wrapping protects one cryptographic key using another key.

Conceptually:

```text
Data Encryption Key
        ↓
Key-Wrapping Key
        ↓
Wrapped Key
```

This is useful when securely storing or transporting encryption keys.

---

# 75. Cryptographic Context

Keys should often be associated with a specific context or purpose.

For example:

```text
Production
Application A
Encryption
Version 3
```

This can help prevent accidental cross-use of keys.

---

# 76. Nonce Management

Nonce generation must be carefully designed.

Possible approaches include:

```text
Random Nonces
Counters
Unique IDs
Protocol-Managed Nonces
```

The correct method depends on the algorithm.

For high-volume systems, blindly generating random nonces may create collision risks if the nonce space is not sufficiently large.

---

# 77. Deterministic vs Randomized Encryption

### Deterministic

Same plaintext + same key:

```text
Same ciphertext
```

### Randomized

Same plaintext + same key:

```text
Different ciphertext
```

Randomized encryption generally prevents attackers from easily identifying repeated plaintext values.

Modern encryption modes use nonces/IVs to ensure secure separation between encryptions.

---

# 78. Ciphertext Expansion

Encryption may add overhead.

For example:

```text
Plaintext
+
Nonce
+
Authentication Tag
```

may produce:

```text
Ciphertext + Metadata
```

Applications should account for this when designing storage or network protocols.

---

# 79. Authentication Tag

An authentication tag allows the recipient to verify that ciphertext and associated authenticated data have not been modified.

Conceptually:

```text
Ciphertext
   +
Tag
   ↓
Verification
   ↓
Valid / Invalid
```

The tag is not a secret key.

---

# 80. Tag Verification

A secure application should:

```text
Receive ciphertext
      ↓
Verify authentication tag
      ↓
If valid → decrypt / accept
If invalid → reject
```

It should not expose sensitive information through detailed verification errors.

---

# 81. Timing Considerations

Cryptographic comparisons should use appropriate constant-time comparison functions where timing side channels could otherwise expose secret information.

For example, Python provides:

```python
import hmac

hmac.compare_digest(a, b)
```

for suitable constant-time-style comparison use cases.

---

# 82. Side-Channel Considerations

Symmetric cryptographic implementations can leak information through:

```text
Timing
Cache Access
Memory Access
Power
Electromagnetic Signals
```

Well-designed cryptographic libraries implement countermeasures where necessary.

Application developers should prefer established libraries rather than implementing AES internals themselves.

---

# 83. Hardware Acceleration

Modern CPUs may provide hardware acceleration for AES.

Examples include:

```text
AES-NI
```

Hardware acceleration can significantly improve:

```text
Performance
Throughput
Efficiency
```

while maintaining strong security when correctly implemented.

---

# 84. AES-GCM vs CBC

| Property | AES-GCM | AES-CBC |
|---|---|---|
| Encryption | Yes | Yes |
| Authentication | Built-in | No |
| AEAD | Yes | No |
| Padding | No traditional padding | Usually required |
| Nonce/IV | Nonce | IV |
| Modern recommendation | Preferred | Legacy use cases |
| Padding oracle risk | No CBC padding oracle | Possible |

For new application designs, authenticated encryption such as AES-GCM is generally preferred.

---

# 85. AES-GCM vs CTR

| Property | AES-GCM | AES-CTR |
|---|---|---|
| Confidentiality | Yes | Yes |
| Integrity | Yes | No |
| Authentication | Yes | No |
| AEAD | Yes | No |
| Nonce uniqueness | Critical | Critical |
| Modern use | Preferred | Usually needs separate authentication |

---

# 86. AES-GCM vs ChaCha20-Poly1305

Both provide:

```text
Confidentiality
Integrity
Authentication
```

Choice depends on:

```text
Hardware
Performance
Platform
Protocol
Library Support
Standards
```

Do not choose based solely on algorithm popularity.

---

# 87. Secure Symmetric Cryptography Checklist

```text
☐ Use modern algorithms
☐ Prefer AES-GCM or ChaCha20-Poly1305 where appropriate
☐ Generate keys securely
☐ Protect keys
☐ Never hard-code production secrets
☐ Never reuse prohibited nonces
☐ Use appropriate IV/nonce generation
☐ Authenticate ciphertext
☐ Validate authentication tags
☐ Avoid ECB
☐ Avoid obsolete algorithms
☐ Use vetted libraries
☐ Rotate keys appropriately
☐ Separate keys by purpose
```

---

# 88. Common Symmetric Cryptography Mistakes

```text
❌ Using ECB
❌ Using DES
❌ Using RC4
❌ Reusing GCM nonces
❌ Reusing CTR nonces
❌ Hard-coding keys
❌ Using weak random numbers
❌ Encrypting without authentication
❌ Ignoring authentication failures
❌ Implementing AES manually
❌ Using passwords directly as encryption keys
❌ Using the same key for unrelated purposes
```

---

# 89. Passwords as Encryption Keys

Avoid directly using:

```text
password
```

as:

```text
AES key
```

Instead:

```text
Password
   ↓
Password KDF / KDF
   ↓
Derived Key
   ↓
Encryption
```

The KDF should use appropriate:

```text
Salt
Cost Parameters
Memory / Time Parameters
```

depending on the application.

---

# 90. Symmetric Cryptography in TLS

A simplified TLS model:

```text
Client
  │
  │ Handshake
  ▼
Key Establishment
  │
  ▼
Session Keys
  │
  ▼
AES-GCM / ChaCha20-Poly1305
  │
  ▼
Encrypted Application Data
```

This demonstrates the division of responsibility:

```text
Asymmetric / Key Exchange
        ↓
Establish Secret
        ↓
Symmetric Encryption
        ↓
Protect Data
```

---

# 91. Symmetric Cryptography in VPNs

VPN protocols use cryptographic mechanisms to protect traffic.

Conceptually:

```text
Device A
   │
   │ Encrypted Tunnel
   ▼
Internet
   │
   ▼
VPN Gateway
   │
   ▼
Device B
```

Symmetric encryption protects the bulk traffic because it is efficient.

---

# 92. Symmetric Cryptography in Cloud KMS

Cloud platforms commonly use:

```text
KMS
HSM
Envelope Encryption
Data Encryption Keys
Key Encryption Keys
```

A typical flow:

```text
Application
    ↓
Request DEK
    ↓
Encrypt Data
    ↓
Encrypt / Wrap DEK
    ↓
Store Ciphertext + Encrypted DEK
```

---

# 93. Symmetric Cryptography in Application Security

Common use cases:

```text
Encrypted Cookies
Encrypted Tokens
Database Fields
Sensitive Files
Session Data
Backup Data
API Payloads
```

However, encryption design should consider:

```text
Key Management
Authentication
Replay Protection
Nonce Management
Access Control
```

---

# 94. VAPT Testing Checklist

When assessing an application:

```text
☐ Identify encryption algorithms
☐ Identify cipher modes
☐ Check TLS configuration
☐ Check key storage
☐ Check key exposure
☐ Check nonce / IV handling
☐ Check authentication tags
☐ Check password-derived keys
☐ Check deprecated algorithms
☐ Check ECB usage
☐ Check error handling
```

---

# 95. Example VAPT Findings

Potential findings:

```text
Weak Encryption Algorithm
Use of ECB Mode
DES / 3DES Usage
RC4 Usage
AES-CBC Without Authentication
Nonce Reuse
Hard-Coded Encryption Key
Weak Key Derivation
Predictable IV
Improper Authentication Tag Validation
```

Severity depends on:

```text
Exploitability
Data Sensitivity
Attack Conditions
Exposure
Impact
```

---

# 96. Secure Encryption Architecture

A strong modern architecture might look like:

```text
             KMS / HSM
                 │
                 ▼
          Key Management
                 │
                 ▼
            Application
                 │
                 ▼
        AEAD Encryption
          /           \
         ▼             ▼
      Nonce           AAD
         │             │
         └──────┬──────┘
                ▼
        Ciphertext + Tag
                │
                ▼
             Storage
```

---

# 97. Production Design Principles

For production applications:

```text
1. Use established cryptographic libraries.

2. Prefer AEAD constructions.

3. Protect keys separately from encrypted data where practical.

4. Never reuse nonces when the construction prohibits it.

5. Do not use passwords directly as cryptographic keys.

6. Avoid obsolete algorithms.

7. Design for key rotation.

8. Handle authentication failures safely.

9. Separate cryptographic keys by purpose.

10. Test cryptographic failure paths.
```

---

# 98. Common Interview Questions

## What is symmetric encryption?

Symmetric encryption uses shared secret key material for encryption and decryption.

---

## Why is symmetric encryption faster than asymmetric encryption?

Symmetric algorithms are generally computationally more efficient and are therefore suitable for encrypting large amounts of data.

---

## What is AES?

AES is a standardized symmetric block cipher with a 128-bit block size and 128-, 192-, or 256-bit keys.

---

## What is the difference between AES-128 and AES-256?

They use different key sizes:

```text
AES-128 → 128-bit key
AES-256 → 256-bit key
```

Both use a 128-bit block size.

---

## Why is DES insecure?

Its effective 56-bit key size is too small to resist modern exhaustive key search.

---

## Why is ECB insecure?

ECB encrypts blocks independently, so identical plaintext blocks produce identical ciphertext blocks and can reveal structural patterns.

---

## What is CBC?

CBC is a block cipher mode in which each plaintext block is XORed with the previous ciphertext block before encryption, with an IV used for the first block.

---

## What is CTR mode?

CTR mode uses a block cipher to generate a keystream from nonce/counter values and XORs that keystream with plaintext.

---

## Why is nonce reuse dangerous?

For constructions such as CTR and GCM, nonce reuse can reuse keystream material or undermine authentication, potentially exposing plaintext relationships or compromising security.

---

## What is GCM?

GCM is an authenticated-encryption mode based on counter-mode encryption and GHASH authentication.

---

## What is AEAD?

AEAD provides authenticated encryption with associated data, combining confidentiality and integrity/authentication.

---

## Why is AES-GCM preferred over AES-CBC for many modern applications?

AES-GCM provides authenticated encryption directly, while CBC provides confidentiality but does not inherently authenticate ciphertext.

---

## What is ChaCha20-Poly1305?

It is an AEAD construction combining the ChaCha20 stream cipher with the Poly1305 authenticator.

---

## What is envelope encryption?

Envelope encryption encrypts data using a data encryption key and then protects that key using another key, often managed by a KMS or HSM.

---

# 99. Quick Revision Table

| Concept | Key Idea |
|---|---|
| Symmetric Cryptography | Shared secret key |
| Block Cipher | Fixed-size blocks |
| Stream Cipher | Keystream-based encryption |
| AES | Modern symmetric block cipher |
| DES | Obsolete 56-bit cipher |
| 3DES | Legacy triple-DES construction |
| ECB | Leaks repeated block patterns |
| CBC | Chained block encryption |
| CTR | Counter-based stream-like mode |
| GCM | Authenticated encryption mode |
| ChaCha20 | Modern stream cipher |
| Poly1305 | Message authenticator |
| AEAD | Encryption + authentication |
| IV | Mode initialization value |
| Nonce | Value used with uniqueness/freshness requirements |
| Padding | Makes data fit block size |
| DEK | Data Encryption Key |
| KEK | Key Encryption Key |
| Envelope Encryption | Encrypt data key with another key |

---

# 100. Key Takeaways

The most important concepts from this chapter are:

```text
1. Symmetric cryptography uses shared secret key material.

2. It is generally much faster than asymmetric cryptography.

3. AES is the dominant modern symmetric block cipher.

4. AES uses a 128-bit block size.

5. AES supports 128-, 192-, and 256-bit keys.

6. DES and 3DES are legacy technologies and should generally not be used for new designs.

7. ECB leaks plaintext patterns and should generally be avoided.

8. CBC requires careful IV and padding handling and does not provide authentication by itself.

9. CTR requires unique nonce/counter combinations for a given key.

10. GCM provides authenticated encryption.

11. ChaCha20-Poly1305 is another widely used AEAD construction.

12. Nonce misuse can completely undermine otherwise secure cryptography.

13. Encryption alone does not automatically provide integrity.

14. AEAD is generally preferred for modern application encryption.

15. Key management is as important as the encryption algorithm.

16. Envelope encryption separates data encryption from higher-level key management.

17. Never implement cryptographic primitives from scratch for production systems.

18. Use established libraries, modern constructions, secure randomness, and appropriate key-management systems.
```

---

# 101. Chapter Summary

This chapter covered the foundations and practical use of symmetric-key cryptography.

We learned:

```text
Symmetric Cryptography
Key Distribution
Hybrid Encryption
Block Ciphers
Stream Ciphers
DES
3DES
AES
AES Key Sizes
AES Rounds
SubBytes
ShiftRows
MixColumns
AddRoundKey
ECB
CBC
CTR
GCM
ChaCha20
Poly1305
AEAD
IVs
Nonces
Padding
PKCS#7
Padding Oracles
Key Management
Key Rotation
Key Separation
HKDF
Envelope Encryption
Data-at-Rest Encryption
Data-in-Transit Encryption
VAPT Considerations
```

The central principle is:

> **Strong symmetric encryption requires more than choosing AES. Secure key management, correct modes, nonce handling, authentication, randomness, implementation, and operational practices are all part of the security design.**

---

# Next Chapter

## Chapter 04 – Asymmetric-Key Cryptography

The next chapter moves from shared-secret cryptography to **public-key cryptography**.

It will cover:

```text
Public-Key Cryptography
Private Keys
Public Keys
RSA
RSA Encryption
RSA Signatures
Diffie-Hellman
ECDH
Elliptic Curve Cryptography
ECC Mathematics
Key Exchange
Hybrid Encryption
Forward Secrecy
Digital Signatures
Key Sizes
RSA vs ECC
Asymmetric Cryptography Attacks
Practical Applications
```

The key question for the next chapter will be:

> **How can two parties securely establish trust or shared secret material when they do not already possess the same secret key?**