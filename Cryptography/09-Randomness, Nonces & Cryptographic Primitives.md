# Chapter 09 – Randomness, Nonces & Cryptographic Primitives

## Overview

Cryptography depends heavily on values that attackers cannot predict or manipulate.

A cryptographic system can use mathematically strong algorithms and still become vulnerable because of:

```text
Weak Randomness
Predictable Nonces
Nonce Reuse
IV Reuse
Poor Entropy
Weak Seeds
Bad PRNGs
Incorrect Primitive Composition
```

This chapter focuses on the foundations that make cryptographic algorithms safe in real systems:

```text
Entropy
Randomness
CSPRNG
PRNG
DRBG
Seeds
Nonces
IVs
Salts
Counters
Freshness
Uniqueness
Cryptographic Primitives
AEAD
Hash Functions
MACs
Encryption
Digital Signatures
KDFs
Domain Separation
Cryptographic Composition
Implementation Failures
```

The central principle is:

> **Cryptographic algorithms assume that their inputs satisfy specific security properties. Violating those assumptions can completely break the security guarantees of the algorithm.**

---

# 1. Why Randomness Matters

Suppose an encryption key is:

```text
123456789
```

The encryption algorithm may be AES-256, but the effective security is still extremely weak.

An attacker can simply try likely values.

Good cryptography requires:

```text
Strong Algorithm
+
Secure Key
+
Secure Randomness
+
Correct Protocol
+
Correct Implementation
```

---

# 2. Randomness in Cryptography

Random values are used for:

```text
Encryption Keys
Private Keys
Nonces
Initialization Vectors
Salts
Session Identifiers
Challenges
Ephemeral Keys
Authentication Tokens
Reset Tokens
Protocol Values
```

If an attacker can predict these values, security can fail.

---

# 3. Entropy

**Entropy** is a measure of uncertainty or unpredictability.

For a uniformly random value with:

```text
n bits
```

there are:

```text
2^n
```

possible values.

For example:

```text
8 bits  → 2^8   = 256 values
128 bits → 2^128
256 bits → 2^256
```

The important security property is not merely the length but the actual unpredictability.

---

# 4. High Entropy vs Low Entropy

High entropy:

```text
Cryptographically random 256-bit value
```

Low entropy:

```text
Current timestamp
User ID
Process ID
Counter
Username
Predictable device state
```

An output can contain many bits while still having low effective entropy.

---

# 5. Entropy Source

An entropy source is where unpredictable information originates.

Potential sources include:

```text
Hardware Randomness
Operating-System Entropy
Hardware Events
System Noise
Trusted Hardware RNG
```

Applications should normally rely on the operating system's cryptographic randomness APIs rather than attempting to build their own entropy source.

---

# 6. Operating-System Randomness

Modern operating systems provide cryptographically secure randomness facilities.

Examples:

Linux:

```text
/dev/urandom
getrandom()
```

Windows:

```text
BCryptGenRandom
```

Modern programming languages generally expose secure APIs that internally use OS randomness.

---

# 7. CSPRNG

**CSPRNG** stands for:

```text
Cryptographically Secure Pseudorandom Number Generator
```

It produces pseudorandom output that should be computationally infeasible to predict without knowledge of the generator's internal secret state.

Conceptually:

```text
Entropy
   ↓
Seed / Internal State
   ↓
CSPRNG
   ↓
Random-Looking Output
```

---

# 8. PRNG vs CSPRNG

A conventional PRNG may be designed for:

```text
Simulation
Games
Statistics
Testing
Modeling
```

A CSPRNG is designed for:

```text
Cryptographic Keys
Tokens
Nonces
Private Keys
Security Protocols
```

Do not assume every random-number API is cryptographically secure.

---

# 9. Python Random Example

This is not appropriate for generating cryptographic secrets:

```python
import random

token = random.randint(0, 2**128)
```

The `random` module is designed for general-purpose pseudorandomness, not cryptographic security.

---

# 10. Python Secure Randomness

Use:

```python
import secrets

token = secrets.token_bytes(32)
```

or:

```python
import secrets

token = secrets.token_hex(32)
```

For security-sensitive values, `secrets` is the appropriate standard-library interface.

---

# 11. Cryptographic Random Bytes

Example:

```python
import secrets

key = secrets.token_bytes(32)

print(key.hex())
```

This produces:

```text
32 bytes
=
256 bits
```

of cryptographically secure random data, assuming the underlying platform is functioning correctly.

---

# 12. CSPRNG State

A CSPRNG internally maintains state.

Conceptually:

```text
Seed
 ↓
Internal State
 ↓
Output
 ↓
Updated State
 ↓
Next Output
```

An attacker who gains sufficient information about internal state may potentially predict outputs.

Therefore secure implementations protect:

```text
Seed
Internal State
Entropy Input
```

---

# 13. Seed

A seed initializes a pseudorandom generator.

Bad:

```python
seed = 12345
```

for security-sensitive randomness.

An attacker who knows the seed may reproduce the generator's output.

Good cryptographic systems obtain seed material from a secure entropy source.

---

# 14. Seed Reuse

Suppose:

```text
Server A → Seed X
Server B → Seed X
```

and both use the same deterministic generator.

Their outputs may become correlated or identical.

Therefore cryptographic generators require appropriate initialization and state management.

---

# 15. Predictable Seed Attack

Consider:

```python
seed = int(time.time())
```

An attacker can estimate:

```text
Time
```

and reproduce the sequence.

Therefore:

```text
Timestamp ≠ Cryptographic Entropy
```

---

# 16. Randomness Failure

A cryptographic system can fail even when:

```text
AES = Strong
RSA = Strong
SHA-256 = Strong
```

if:

```text
Private Key = Predictable
```

or:

```text
Nonce = Predictable / Reused
```

---

# 17. Famous Randomness Failures

Historical failures demonstrate the importance of randomness.

Examples include:

```text
Debian OpenSSL PRNG vulnerability
Weak embedded-device RNGs
Bad ECDSA nonce generation
Predictable session tokens
Repeated encryption nonces
```

---

# 18. Debian OpenSSL Bug

A famous historical incident involved Debian's OpenSSL package.

A change inadvertently reduced the available entropy used for key generation.

The result:

```text
Small Set of Predictable Keys
```

Some generated cryptographic keys became practically guessable.

This demonstrates:

> **A secure algorithm cannot compensate for broken key generation.**

---

# 19. ECDSA Randomness Failure

ECDSA requires a nonce for each signature.

If:

```text
Nonce = Reused
```

or:

```text
Nonce = Predictable
```

the private key may become recoverable.

This is one of the most important examples of randomness directly affecting asymmetric cryptography.

---

# 20. Nonce

A **nonce** means:

```text
Number Used Once
```

A nonce is generally not intended to be secret.

Its most important property depends on the cryptographic construction.

Often:

```text
Uniqueness
```

is critical.

---

# 21. Nonce vs Random Number

A nonce does not necessarily need to be random.

For some constructions:

```text
Counter
```

is sufficient.

Example:

```text
Nonce 1
Nonce 2
Nonce 3
Nonce 4
```

If uniqueness is guaranteed, randomness may not be required.

---

# 22. Nonce Properties

Depending on the protocol, a nonce may require:

```text
Uniqueness
Freshness
Unpredictability
Fixed Length
Protocol Binding
```

Never assume every nonce has the same requirements.

---

# 23. IV

**IV** stands for:

```text
Initialization Vector
```

An IV is auxiliary input used by some encryption modes.

Depending on the algorithm and mode, an IV may require:

```text
Uniqueness
Unpredictability
Randomness
```

The exact requirement depends on the mode.

---

# 24. Nonce vs IV

The terms are sometimes used interchangeably, but conceptually:

```text
Nonce
→ Number used once

IV
→ Initialization input for an encryption construction
```

The security requirement depends on the specific cryptographic scheme.

---

# 25. Salt

A salt is another type of non-secret value.

It is commonly used with:

```text
Password Hashing
Password KDFs
Key Derivation
```

Conceptually:

```text
Password
+
Unique Salt
↓
KDF
↓
Derived Output
```

---

# 26. Salt vs Nonce vs IV

| Value | Typical Purpose | Secret? | Main Requirement |
|---|---|---|---|
| Salt | Password hashing/KDF | No | Usually unique |
| Nonce | Protocol freshness/uniqueness | Usually no | Often unique |
| IV | Encryption mode input | Usually no | Depends on mode |
| Key | Cryptographic secret | Yes | Secret + unpredictable |

---

# 27. Counter

A counter can be used as a nonce:

```text
0
1
2
3
4
```

This is often useful because uniqueness is easy to guarantee.

But the counter must not reset unexpectedly when the same key is reused.

---

# 28. Counter Reuse Problem

Suppose:

```text
Key = K
Nonce = 10
```

is used once.

Then after restart:

```text
Key = K
Nonce = 10
```

is used again.

This is:

```text
Nonce Reuse
```

and may completely break certain AEAD modes.

---

# 29. AES-GCM Nonce Reuse

AES-GCM is extremely sensitive to nonce reuse.

If the same key and nonce are reused:

```text
K + Nonce N
```

for multiple messages, serious security failures can occur.

Potential consequences include:

```text
Plaintext Relationships
Authentication Key Leakage
Forgery
Message Integrity Failure
```

Therefore:

> **Never reuse an AES-GCM nonce with the same key.**

---

# 30. AES-GCM Mental Model

```text
Key
 +
Unique Nonce
 +
Plaintext
 ↓
AES-GCM
 ↓
Ciphertext + Authentication Tag
```

The nonce does not need to be secret.

But reuse under the same key must be prevented.

---

# 31. ChaCha20-Poly1305

ChaCha20-Poly1305 is an AEAD construction.

It uses:

```text
ChaCha20
+
Poly1305
```

and requires proper nonce handling.

Nonce reuse under the same key is also dangerous.

---

# 32. AEAD

**AEAD** stands for:

```text
Authenticated Encryption with Associated Data
```

It provides:

```text
Confidentiality
+
Integrity
+
Authentication
```

and allows selected metadata to be authenticated without being encrypted.

Examples:

```text
AES-GCM
ChaCha20-Poly1305
```

---

# 33. AEAD Structure

Conceptually:

```text
Key
 +
Nonce
 +
Plaintext
 +
AAD
 ↓
AEAD
 ↓
Ciphertext
 +
Authentication Tag
```

During decryption:

```text
Ciphertext
+
Tag
+
Nonce
+
AAD
+
Key
 ↓
Verify
 ↓
Decrypt
```

---

# 34. Associated Data

AAD means:

```text
Additional Authenticated Data
```

It is authenticated but not encrypted.

Example:

```text
User ID
Record ID
Protocol Version
Message Type
```

If AAD is modified:

```text
Authentication Failure
```

---

# 35. Why AAD Matters

Suppose:

```text
Encrypted Data:
"Transfer ₹100"

Metadata:
Account = Alice
```

If metadata is not authenticated, an attacker might attempt to alter:

```text
Account = Bob
```

AAD allows the metadata to be cryptographically bound to the ciphertext.

---

# 36. Cryptographic Primitive

A cryptographic primitive is a basic cryptographic building block.

Examples:

```text
Hash Function
MAC
Block Cipher
Stream Cipher
KDF
Digital Signature
AEAD
Random Generator
```

Protocols combine primitives to achieve larger security goals.

---

# 37. Hash Function

A cryptographic hash maps arbitrary input to a fixed-size output.

```text
Message
   ↓
Hash Function
   ↓
Digest
```

Examples:

```text
SHA-256
SHA-512
SHA-3
BLAKE2
BLAKE3
```

---

# 38. Hash Properties

Important properties:

```text
Preimage Resistance
Second-Preimage Resistance
Collision Resistance
Deterministic Output
Fixed Output Size
Avalanche Effect
```

---

# 39. Preimage Resistance

Given:

```text
Hash = H(x)
```

it should be computationally difficult to find:

```text
x
```

from:

```text
H(x)
```

---

# 40. Second-Preimage Resistance

Given:

```text
Message A
```

it should be difficult to find:

```text
Message B ≠ A
```

such that:

```text
H(A) = H(B)
```

---

# 41. Collision Resistance

It should be difficult to find any:

```text
A ≠ B
```

such that:

```text
H(A) = H(B)
```

---

# 42. Avalanche Effect

A small change in input should produce a substantially different hash.

Example:

```text
Input:
Hello

Input:
hello
```

should produce very different digests.

---

# 43. MAC

A Message Authentication Code uses:

```text
Secret Key
+
Message
```

to produce an authentication value.

Example:

```text
HMAC
```

Conceptually:

```text
Message + Secret
       ↓
      HMAC
       ↓
     Tag
```

---

# 44. Encryption Primitive

Encryption provides confidentiality.

```text
Plaintext
   +
Key
   ↓
Encryption
   ↓
Ciphertext
```

Modern secure encryption should generally also provide integrity through an authenticated construction such as AEAD.

---

# 45. Block Cipher

A block cipher processes fixed-size blocks.

Example:

```text
AES
```

AES has:

```text
128-bit Block Size
```

with key sizes:

```text
128
192
256 bits
```

---

# 46. Stream Cipher

A stream cipher generates a keystream that is combined with plaintext.

Example:

```text
ChaCha20
```

Conceptually:

```text
Key
 +
Nonce
 ↓
Keystream
 ↓
Plaintext XOR Keystream
 ↓
Ciphertext
```

Never reuse the same keystream under the same key.

---

# 47. One-Time Pad

A one-time pad uses:

```text
Truly Random Key
=
Message Length
```

and:

```text
Key Used Exactly Once
```

Under ideal conditions, it provides information-theoretic secrecy.

But key distribution makes it impractical for most modern systems.

---

# 48. XOR

XOR is a fundamental operation:

```text
0 XOR 0 = 0
0 XOR 1 = 1
1 XOR 0 = 1
1 XOR 1 = 0
```

Important property:

```text
A XOR B XOR B = A
```

This is why stream ciphers can encrypt and decrypt using XOR.

---

# 49. Why XOR Alone Is Not Encryption

If:

```text
Ciphertext = Plaintext XOR Key
```

and the key is:

```text
Weak
Short
Repeated
Predictable
```

the system is insecure.

XOR is merely an operation.

Security comes from the cryptographic construction and key properties.

---

# 50. Digital Signature Primitive

A signature provides:

```text
Authentication
+
Integrity
```

Conceptually:

```text
Message
   ↓
Signature Algorithm
   +
Private Key
   ↓
Signature
```

Verification uses:

```text
Public Key
```

---

# 51. KDF Primitive

A KDF transforms secret material:

```text
Secret
 ↓
KDF
 ↓
Derived Key
```

Examples:

```text
HKDF
PBKDF2
scrypt
Argon2
```

They serve different use cases and should not be treated as interchangeable.

---

# 52. Password KDF vs General KDF

### Password KDF

Designed to resist password guessing:

```text
Argon2
scrypt
PBKDF2
```

### General KDF

Designed to derive keys from high-entropy secret material:

```text
HKDF
```

---

# 53. Cryptographic Composition

Individual primitives are rarely enough.

A secure system may combine:

```text
Randomness
+
Key Exchange
+
KDF
+
AEAD
+
Digital Signature
+
Certificate
```

to build:

```text
Secure Communication
```

---

# 54. Primitive Composition Example

TLS conceptually uses:

```text
Certificate
      ↓
Authentication

ECDHE
      ↓
Shared Secret

HKDF
      ↓
Session Keys

AES-GCM / ChaCha20-Poly1305
      ↓
Encrypted Application Data
```

---

# 55. Don't Invent Cryptography

A common security mistake is designing:

```text
Custom Encryption
Custom Hash
Custom MAC
Custom KDF
Custom Token Format
```

without cryptographic expertise and formal analysis.

Prefer:

```text
Standardized Algorithms
+
Well-Tested Libraries
+
Established Protocols
```

---

# 56. Cryptographic API Design

A good cryptographic API should make insecure usage difficult.

For example:

```python
encrypt(key, plaintext)
```

is potentially dangerous if the library silently generates or reuses an unsafe nonce.

Better APIs explicitly handle:

```text
Nonce
Authentication Tag
AAD
Key
```

and enforce safe defaults.

---

# 57. Safe AEAD Example

Conceptually:

```python
nonce = secure_random_nonce()

ciphertext = aead.encrypt(
    nonce,
    plaintext,
    aad
)
```

Store:

```text
nonce
+
ciphertext
```

The nonce normally does not need to be secret.

---

# 58. Authentication Tag

AEAD generates an authentication tag.

Conceptually:

```text
Ciphertext
+
Tag
```

The tag allows detection of:

```text
Modified Ciphertext
Modified AAD
Incorrect Key
Incorrect Nonce
```

---

# 59. Never Ignore Authentication Failures

If AEAD verification fails:

```text
DO NOT
↓
Decrypt Anyway
```

Instead:

```text
Reject Message
```

Authentication failure indicates that the cryptographic integrity check did not succeed.

---

# 60. Padding

Some block cipher modes use padding.

For example:

```text
CBC
```

may use:

```text
PKCS#7
```

Improper padding validation can create serious vulnerabilities such as padding oracles.

Modern applications should generally prefer AEAD modes when available.

---

# 61. Padding Oracle

A padding oracle occurs when an attacker can distinguish:

```text
Valid Padding
```

from:

```text
Invalid Padding
```

through observable application behavior.

The attacker may exploit this to recover plaintext or manipulate ciphertext.

---

# 62. Timing Side Channels

Suppose:

```text
Valid Secret → 100 ms
Invalid Secret → 90 ms
```

An attacker may use timing differences to infer information.

Cryptographic comparisons should use constant-time mechanisms where required.

---

# 63. Constant-Time Comparison

Do not necessarily compare security-sensitive MACs using ordinary string comparison.

Use a constant-time comparison function.

Python:

```python
import hmac

hmac.compare_digest(a, b)
```

This reduces timing leakage from early-exit comparisons.

---

# 64. Side-Channel Security

Cryptographic implementations may leak information through:

```text
Timing
Power Consumption
Cache Access
Memory Access
Electromagnetic Radiation
Errors
```

These are called:

```text
Side Channels
```

---

# 65. Fault Injection

An attacker may intentionally cause:

```text
Voltage Changes
Clock Manipulation
Hardware Faults
Memory Faults
```

to influence cryptographic operations.

High-assurance systems may use:

```text
Fault Detection
Redundant Computation
Hardware Protections
Secure Environments
```

---

# 66. Error Handling

Avoid revealing detailed cryptographic state through errors.

Bad:

```text
Invalid padding
Wrong MAC
Wrong key
Invalid signature
```

in a context where attackers can distinguish these conditions.

Better:

```text
Authentication failed
```

when appropriate.

---

# 67. Randomness and Session Tokens

Session tokens should be generated using cryptographically secure randomness.

Bad:

```python
token = str(random.randint(100000, 999999))
```

Better:

```python
import secrets

token = secrets.token_urlsafe(32)
```

---

# 68. Token Entropy

A token should have enough effective entropy to resist guessing.

If an authentication token contains:

```text
6 decimal digits
```

there are only:

```text
1,000,000
```

possible values.

This may be insufficient for long-lived authentication credentials.

---

# 69. OTP vs Authentication Token

A short OTP can be appropriate when:

```text
Short Lifetime
Rate Limiting
Limited Attempts
Strong Server Controls
```

are present.

A long-lived session token generally needs substantially more entropy.

---

# 70. Nonce Reuse Detection

During a security assessment, investigate whether:

```text
Same Key
+
Same Nonce
```

can occur more than once.

Sources include:

```text
Process Restart
Counter Reset
VM Snapshot
Container Cloning
State Rollback
Incorrect Randomness
Concurrent Processes
```

---

# 71. VM Snapshot Problem

Consider:

```text
VM State
 ↓
CSPRNG State = S
```

Snapshot:

```text
Snapshot
```

Two machines resume from:

```text
Same State S
```

If the randomness implementation does not correctly reseed or otherwise handle this situation, outputs may repeat.

Modern operating systems are designed to mitigate such issues, but application and platform design should still consider cloning and rollback.

---

# 72. Container Cloning

If multiple containers are created from the same improperly initialized state:

```text
Container A
Container B
Container C
```

they could potentially generate correlated values.

Use the operating system's secure randomness facilities rather than custom deterministic generators.

---

# 73. Distributed Systems and Nonces

Distributed applications need special care.

Suppose:

```text
Server A → Nonce 100
Server B → Nonce 100
```

If both share:

```text
Same Encryption Key
```

nonce reuse may occur.

Possible solutions:

```text
Unique Node ID
+
Counter
```

or:

```text
Centralized Nonce Allocation
```

or carefully designed random nonces with sufficiently low collision probability.

---

# 74. Nonce Construction

A common pattern:

```text
Nonce =
   Fixed Unique Prefix
   +
   Counter
```

Example:

```text
Node ID | Counter
```

This can provide uniqueness if the prefix and counter lifecycle are correctly managed.

---

# 75. Random Nonce Collision

Random nonces can collide.

Suppose a nonce has:

```text
n bits
```

and many random nonces are generated.

The probability of collisions increases according to the birthday bound.

Approximately:

```text
Collision becomes non-negligible
around
2^(n/2)
samples
```

Therefore the nonce size and generation strategy must match the construction's requirements.

---

# 76. Birthday Bound

For a hash function with:

```text
n-bit output
```

collision attacks have generic complexity around:

```text
2^(n/2)
```

For SHA-256:

```text
Collision resistance ≈ 2^128
```

under ideal assumptions.

This is why SHA-256 provides much stronger collision resistance than a 128-bit hash.

---

# 77. Hash Truncation

A hash may be truncated:

```text
SHA-256
 ↓
First 128 bits
```

This reduces the effective security of the truncated value.

For authentication tags, truncation can increase forgery probability.

The acceptable size depends on the protocol and threat model.

---

# 78. Randomness for Private Keys

Private keys should be generated using:

```text
CSPRNG
```

Examples:

```text
RSA Private Key
ECDSA Private Key
Ed25519 Private Key
```

Never generate them from:

```text
Timestamp
Username
Password
Predictable Seed
```

---

# 79. Randomness for Password Salts

Password salts should normally be:

```text
Unique
Random
Non-secret
```

A common design:

```text
Salt = CSPRNG()
```

Then:

```text
Password + Salt
       ↓
Password KDF
```

---

# 80. Randomness for CSRF Tokens

CSRF tokens should be:

```text
Unpredictable
Unique enough for their context
Bound to the session or action where appropriate
```

Generate using:

```text
CSPRNG
```

not ordinary PRNGs.

---

# 81. Randomness for Password Reset Tokens

Password reset tokens are high-value authentication credentials.

They should be:

```text
Cryptographically Random
Sufficiently Long
Short-Lived
Single-Use
Invalidated After Use
```

---

# 82. Cryptographic Primitive Selection

Before selecting a primitive ask:

```text
What security property do I need?
```

Examples:

```text
Confidentiality
→ Encryption / AEAD

Integrity + Authentication
→ MAC / AEAD

Password Protection
→ Argon2 / scrypt / PBKDF2

Key Derivation
→ HKDF

Digital Authentication
→ Signature

Fingerprint
→ Cryptographic Hash
```

---

# 83. Security Property Mapping

| Requirement | Appropriate Primitive |
|---|---|
| Hashing | SHA-256 / SHA-3 / BLAKE2 |
| Password Hashing | Argon2 / scrypt / PBKDF2 |
| Encryption + Integrity | AES-GCM / ChaCha20-Poly1305 |
| MAC | HMAC |
| Key Derivation | HKDF |
| Digital Signature | RSA-PSS / ECDSA / Ed25519 |
| Key Agreement | DH / ECDH / ECDHE |
| Randomness | CSPRNG |

---

# 84. Don't Use Hashing as Encryption

This is incorrect:

```text
Password
 ↓
SHA-256
 ↓
"Encrypted Password"
```

Hashing does not provide reversible encryption.

For password storage:

```text
Password
 ↓
Password KDF
 ↓
Password Verifier
```

---

# 85. Don't Use Encryption as Password Hashing

This is also problematic:

```text
Password
 ↓
AES
 ↓
Encrypted Password
```

Passwords require resistance to offline guessing.

Use a password-specific KDF such as:

```text
Argon2
scrypt
PBKDF2
```

with a unique salt.

---

# 86. Don't Use MD5 for Security

MD5 has serious collision weaknesses.

Avoid it for:

```text
Digital Signatures
Password Security
Integrity Security
Security Tokens
Certificate Security
```

It can still appear in legacy non-adversarial contexts such as checksums, but it should not be selected for new security designs.

---

# 87. Don't Use SHA-1 for New Security Designs

SHA-1 collision resistance is considered broken.

Avoid SHA-1 for new:

```text
Digital Signatures
Certificates
Security Hashes
```

Use modern alternatives such as:

```text
SHA-256
SHA-384
SHA-512
SHA-3
```

as appropriate.

---

# 88. Don't Build Custom MACs

Avoid:

```text
SHA256(secret + message)
```

as a homemade authentication construction.

Use:

```text
HMAC
```

or a standard AEAD construction.

---

# 89. Length-Extension Attacks

Some Merkle-Damgård hash constructions can be vulnerable to length-extension attacks when incorrectly used as:

```text
Hash(secret || message)
```

for authentication.

This is another reason to use:

```text
HMAC
```

instead of designing a custom MAC.

---

# 90. Domain Separation

Suppose one key is used with multiple protocols:

```text
Protocol A
Protocol B
```

Without domain separation, outputs or messages may accidentally become valid in another context.

Use explicit context:

```text
protocol-A
protocol-B
```

within the cryptographic derivation or signing construction where appropriate.

---

# 91. Keyed Hashing

A keyed hash provides authentication.

Example:

```text
HMAC-SHA256
```

Conceptually:

```text
Key
 +
Message
 ↓
HMAC
 ↓
Authentication Tag
```

---

# 92. Hash-Based Fingerprints

Hashes can identify:

```text
Files
Certificates
Artifacts
Public Keys
```

Example:

```text
SHA-256(file)
```

produces a fingerprint.

However, a hash alone does not authenticate who produced the file.

---

# 93. Hash vs Digital Signature

Hash:

```text
Data
 ↓
Digest
```

Signature:

```text
Data
+
Private Key
 ↓
Signature
```

A hash provides a fingerprint.

A signature provides cryptographic authentication of the data under a private key.

---

# 94. MAC vs Digital Signature

MAC:

```text
Shared Secret
```

Signature:

```text
Private Key
+
Public Key
```

MAC verification requires the verifier to possess the secret.

Signature verification does not require the verifier to possess the private signing key.

---

# 95. Primitive Misuse

Common mistakes:

```text
Wrong Key
Wrong Nonce
Nonce Reuse
Wrong Encoding
Weak Randomness
Incorrect Padding
Wrong Hash
Improper MAC
Missing Authentication
Improper Verification
Custom Cryptography
```

---

# 96. Encoding vs Encryption

Base64 is not encryption.

```text
Plaintext
 ↓
Base64
 ↓
Encoded Text
```

Anyone can decode it.

Similarly:

```text
Hex
URL Encoding
Base32
```

are encodings, not encryption.

---

# 97. Serialization Security

Cryptographic data often crosses serialization boundaries.

Examples:

```text
JSON
CBOR
ASN.1
DER
PEM
Protocol Buffers
```

Incorrect serialization or canonicalization can cause signature verification problems.

---

# 98. Canonicalization

Suppose two representations mean the same logical object:

```json
{"a":1,"b":2}
```

and:

```json
{"b":2,"a":1}
```

If a signature is computed over raw bytes, the two byte sequences may produce different signatures.

Protocols therefore sometimes require:

```text
Canonical Serialization
```

before signing.

---

# 99. Cryptographic Agility

Applications should avoid hard-coding assumptions such as:

```text
Only AES-128 forever
Only RSA forever
Only SHA-256 forever
```

Instead design systems that can migrate to stronger algorithms when necessary.

---

# 100. Algorithm Deprecation

Security teams should maintain inventories of:

```text
Algorithms
Key Sizes
Libraries
Certificates
Protocols
```

and identify:

```text
Legacy
Deprecated
Weak
Unsupported
```

components.

---

# 101. Randomness Security Checklist

```text
☐ Use OS-provided CSPRNG
☐ Never use timestamps as secret seeds
☐ Never use ordinary PRNGs for keys
☐ Protect CSPRNG state
☐ Generate private keys using secure randomness
☐ Generate security tokens using secure randomness
☐ Generate password-reset tokens securely
☐ Generate salts securely
☐ Understand nonce requirements
☐ Prevent nonce reuse
☐ Handle process restart safely
☐ Consider distributed systems
☐ Test randomness assumptions
```

---

# 102. Nonce Security Checklist

```text
☐ Understand the algorithm's nonce requirement
☐ Guarantee uniqueness where required
☐ Never reuse GCM nonce with same key
☐ Never reuse ChaCha20-Poly1305 nonce with same key
☐ Prevent counter reset
☐ Handle VM rollback
☐ Handle container cloning
☐ Handle multi-node deployments
☐ Store nonce with ciphertext where appropriate
☐ Never assume nonce secrecy
```

---

# 103. Cryptographic Primitive Checklist

```text
☐ Use standardized primitives
☐ Use trusted libraries
☐ Prefer AEAD
☐ Use HMAC instead of homemade MACs
☐ Use KDFs for key derivation
☐ Use password-specific KDFs for passwords
☐ Use secure signatures
☐ Avoid MD5
☐ Avoid SHA-1 for new security designs
☐ Avoid custom cryptography
☐ Validate authentication tags
☐ Use constant-time comparisons where required
☐ Handle errors safely
```

---

# 104. VAPT – Randomness Testing

During an assessment look for:

```text
Predictable Tokens
Predictable Session IDs
Timestamp-Based Secrets
Weak Password Reset Tokens
Weak CSRF Tokens
Weak API Keys
Repeated Nonces
Static IVs
Repeated IVs
Weak Key Generation
```

---

# 105. Source-Code Review

Search for suspicious patterns:

```python
random.random()
random.randint()
time.time()
```

used in:

```text
Keys
Tokens
Nonces
Passwords
Authentication
```

This does not automatically prove a vulnerability, but it is a strong review indicator.

---

# 106. Search for Hard-Coded IVs

Suspicious:

```python
iv = b"1234567890123456"
```

or:

```python
IV = "0000000000000000"
```

A static IV may be unsafe depending on the encryption mode.

---

# 107. Search for Static Nonces

Suspicious:

```python
nonce = b"fixed-nonce"
```

Especially dangerous with:

```text
AES-GCM
ChaCha20-Poly1305
```

when the same key is reused.

---

# 108. Search for Homemade Encryption

Suspicious code:

```python
ciphertext = plaintext[::-1]
```

or:

```python
ciphertext = xor(data, key)
```

or:

```python
encrypted = base64.b64encode(data)
```

These are not secure encryption designs.

---

# 109. SOC Monitoring

SOC teams can monitor for:

```text
Mass Token Generation
Repeated Nonces
Cryptographic Errors
Certificate Failures
KMS Failures
Randomness Service Failures
Unexpected Key Generation
Signature Failures
Authentication Failures
```

---

# 110. Cryptographic Incident Example

Suppose a service generates:

```text
AES-GCM Nonce:
000000000000
```

for every request.

An attacker discovers:

```text
Same Key
+
Same Nonce
```

repeated across messages.

Response:

```text
1. Disable affected encryption path.
2. Rotate encryption keys.
3. Assess historical ciphertext exposure.
4. Determine whether forgery is possible.
5. Re-encrypt affected data if required.
6. Fix nonce-generation logic.
7. Add automated tests.
8. Monitor for exploitation.
```

---

# 111. Practical Lab – Secure Randomness

Run:

```python
import secrets

for _ in range(5):
    print(secrets.token_hex(16))
```

Observe:

```text
Different outputs
```

Use this pattern for security-sensitive random values rather than the general-purpose `random` module.

---

# 112. Practical Lab – Compare PRNG and CSPRNG

For demonstration only:

```python
import random
import secrets

random.seed(12345)

print(random.random())
print(random.random())

print(secrets.token_hex(16))
print(secrets.token_hex(16))
```

The seeded PRNG is reproducible.

The CSPRNG output is intended for security-sensitive use.

---

# 113. Practical Lab – Hash

```python
import hashlib

message = b"Hello World"

digest = hashlib.sha256(message).hexdigest()

print(digest)
```

Modify:

```text
Hello World
```

to:

```text
hello World
```

and compare the digest.

---

# 114. Practical Lab – HMAC

```python
import hmac
import hashlib

key = b"secret-key"
message = b"important message"

tag = hmac.new(
    key,
    message,
    hashlib.sha256
).hexdigest()

print(tag)
```

Change the message and observe that the tag changes.

---

# 115. Practical Lab – Secure Token

```python
import secrets

token = secrets.token_urlsafe(32)

print(token)
```

This can be used as a high-entropy token value when combined with appropriate lifecycle controls.

---

# 116. Practical Lab – Nonce Tracking

Build a small test that generates nonces and checks for duplicates:

```python
import secrets

seen = set()

for _ in range(100000):
    nonce = secrets.token_bytes(12)

    if nonce in seen:
        print("Collision detected")
        break

    seen.add(nonce)
else:
    print("No collision detected")
```

This is an educational demonstration, not a proof of collision resistance.

---

# 117. Practical Lab – AEAD

Using `cryptography`:

```python
import os

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

key = AESGCM.generate_key(bit_length=256)

aesgcm = AESGCM(key)

nonce = os.urandom(12)

plaintext = b"Sensitive data"
aad = b"record-123"

ciphertext = aesgcm.encrypt(
    nonce,
    plaintext,
    aad
)

decrypted = aesgcm.decrypt(
    nonce,
    ciphertext,
    aad
)

print(decrypted)
```

The nonce must be managed so that it is not reused with the same key.

---

# 118. Practical Lab – Tamper Detection

Modify:

```text
Ciphertext
```

or:

```text
AAD
```

and attempt decryption.

Expected:

```text
Authentication failure
```

This demonstrates AEAD integrity protection.

---

# 119. Practical Lab – Nonce Reuse Experiment

For educational purposes, encrypt two messages using the same:

```text
AES-GCM Key
+
Nonce
```

Observe that nonce reuse violates the security requirements of GCM.

Do not perform this against real production data.

---

# 120. Practical Lab – Hash Collision Concept

You do not need to find an actual SHA-256 collision.

Instead demonstrate the birthday principle:

```text
n-bit Hash
 ↓
Generic collision complexity ≈ 2^(n/2)
```

Compare:

```text
MD5
SHA-1
SHA-256
```

and research their historical collision attacks.

---

# 121. Practical Lab – Domain Separation

Use HKDF with different `info` values:

```python
info_a = b"application-A"
info_b = b"application-B"
```

Derive:

```text
Key A
Key B
```

from the same secret.

Observe:

```text
Key A ≠ Key B
```

---

# 122. Interview Questions

## What is entropy?

Entropy represents the unpredictability of information. Cryptographic systems require sufficient effective entropy to prevent attackers from predicting secret values.

---

## What is a CSPRNG?

A Cryptographically Secure Pseudorandom Number Generator produces pseudorandom values designed to resist prediction by attackers.

---

## What is the difference between PRNG and CSPRNG?

A PRNG is generally designed for simulation or general randomness, while a CSPRNG is designed to provide unpredictable outputs suitable for cryptographic applications.

---

## Why should `random()` not be used for security tokens?

General-purpose PRNGs may be predictable and are not designed to protect secrets.

---

## What is a nonce?

A nonce is a value intended to be used in a cryptographic protocol, commonly to provide uniqueness or freshness.

---

## Does a nonce need to be secret?

Usually no. Many cryptographic constructions require nonce uniqueness rather than secrecy.

---

## What happens if an AES-GCM nonce is reused?

Nonce reuse under the same key can severely compromise confidentiality and integrity and may enable forgery.

---

## What is an IV?

An initialization vector is auxiliary input used by certain cryptographic constructions. Its required security properties depend on the specific mode.

---

## What is a salt?

A salt is non-secret data, usually unique per password, used with password hashing or KDFs to prevent identical passwords from producing identical outputs and to hinder precomputation attacks.

---

## What is AEAD?

Authenticated Encryption with Associated Data provides confidentiality and integrity while allowing additional data to be authenticated without encryption.

---

## Give examples of AEAD algorithms.

```text
AES-GCM
ChaCha20-Poly1305
```

---

## What is HKDF?

HKDF is an HMAC-based key derivation function used to derive cryptographic keys from secret material.

---

## Why should you not build your own cryptographic algorithm?

Custom cryptography is difficult to design, analyze, implement, and securely compose. Standardized, peer-reviewed primitives and trusted libraries are preferred.

---

## What is a cryptographic primitive?

A primitive is a basic cryptographic building block such as a hash function, MAC, encryption algorithm, KDF, signature scheme, or random generator.

---

## What is a side-channel attack?

A side-channel attack extracts information from implementation behavior such as timing, power consumption, cache access, or error behavior rather than directly breaking the mathematical algorithm.

---

## What is a padding oracle?

A padding oracle is a vulnerability where observable differences in padding validation allow an attacker to infer information about encrypted data.

---

## Why is constant-time comparison important?

It reduces timing leakage that could otherwise reveal information about secret values.

---

## What is the birthday bound?

For an ideal n-bit hash, generic collision attacks require roughly `2^(n/2)` work.

---

# 123. Quick Revision Table

| Concept | Key Idea |
|---|---|
| Entropy | Unpredictability |
| CSPRNG | Secure random generation |
| PRNG | General-purpose pseudorandomness |
| Seed | Initial generator state |
| Nonce | Number used once |
| IV | Encryption initialization input |
| Salt | Non-secret KDF/password input |
| Counter | Deterministic nonce construction |
| AEAD | Encryption + Integrity |
| AAD | Authenticated but unencrypted data |
| Hash | Fixed-size digest |
| HMAC | Keyed authentication |
| KDF | Key derivation |
| HKDF | HMAC-based KDF |
| Block Cipher | Fixed-size block encryption |
| Stream Cipher | Keystream-based encryption |
| Signature | Public-key authentication |
| Side Channel | Leakage through implementation |
| Padding Oracle | Exploitable padding feedback |
| Domain Separation | Context-specific cryptographic outputs |
| Birthday Bound | ~2^(n/2) generic hash collision work |

---

# 124. Key Takeaways

```text
1. Cryptography depends on unpredictable secret values.

2. Entropy represents unpredictability.

3. Use OS-provided CSPRNGs for cryptographic randomness.

4. Never use ordinary PRNGs for security-sensitive secrets.

5. Never use timestamps as cryptographic seeds.

6. Private keys require strong randomness.

7. Security tokens require strong randomness.

8. A nonce usually does not need to be secret.

9. Nonce requirements depend on the cryptographic construction.

10. AES-GCM nonce reuse can severely compromise security.

11. ChaCha20-Poly1305 also requires correct nonce management.

12. Counters can be used as nonces when uniqueness is guaranteed.

13. Counter reset can cause catastrophic nonce reuse.

14. Distributed systems require careful nonce coordination.

15. AEAD provides confidentiality and integrity.

16. AAD authenticates metadata without encrypting it.

17. Authentication failures must cause rejection.

18. Hashes, MACs, encryption, signatures, and KDFs solve different problems.

19. Do not use hashing as encryption.

20. Do not use encryption as password hashing.

21. Use HMAC instead of homemade MAC constructions.

22. Use password-specific KDFs for password storage.

23. Avoid MD5 and SHA-1 for new security-sensitive designs.

24. Avoid custom cryptographic algorithms.

25. Constant-time operations can reduce timing side channels.

26. Cryptographic failures often come from implementation rather than mathematics.

27. Domain separation prevents accidental cross-context key reuse.

28. Cryptographic libraries should provide safe defaults.

29. Randomness failures have historically caused real-world key compromise.

30. Correct primitive composition is as important as primitive selection.
```

---

# 125. Chapter Summary

This chapter covered:

```text
Randomness
Entropy
Entropy Sources
CSPRNG
PRNG
DRBG
Seeds
Seed Reuse
Predictable Randomness
Operating-System Randomness
Debian OpenSSL Failure
Cryptographic Nonces
IVs
Salts
Counters
Freshness
Uniqueness
Nonce Reuse
AES-GCM
ChaCha20-Poly1305
AEAD
AAD
Hash Functions
Preimage Resistance
Second-Preimage Resistance
Collision Resistance
Avalanche Effect
Birthday Bound
MAC
HMAC
Block Ciphers
Stream Ciphers
XOR
KDF
HKDF
Password KDFs
Digital Signatures
Cryptographic Primitives
Primitive Composition
Domain Separation
Canonicalization
Constant-Time Operations
Timing Attacks
Side Channels
Padding Oracles
Fault Injection
Secure Error Handling
Random Session Tokens
Secure Password Reset Tokens
Distributed Nonces
VM Snapshots
Container Cloning
Cryptographic Agility
VAPT Testing
SOC Monitoring
Practical Labs
```

The central mental model is:

```text
             CRYPTOGRAPHIC SECURITY
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
    RANDOMNESS       PRIMITIVES       PROTOCOL
       │               │                │
       ▼               ▼                ▼
     CSPRNG        Hash / MAC /       Key Exchange
     Entropy       AEAD / KDF        Authentication
       │               │                │
       ▼               ▼                ▼
     Keys           Security         Secure
    Nonces          Properties      Composition
       │               │                │
       └───────────────┼────────────────┘
                       ▼
                 Secure System
```

A useful rule to remember:

> **Never ask only "Is the algorithm secure?" Ask whether its keys, randomness, nonces, inputs, implementation, and protocol usage satisfy the algorithm's security assumptions.**

---

# Next Chapter

## Chapter 10 – TLS, HTTPS & Cryptographic Protocols

The next chapter will bring the previous cryptographic concepts together and examine how they operate in real-world protocols:

```text
TLS Fundamentals
SSL vs TLS
TLS Architecture
TLS Handshake
TLS 1.2
TLS 1.3
ClientHello
ServerHello
SNI
ALPN
Cipher Suites
ECDHE
Diffie-Hellman
Certificate Authentication
Certificate Chains
Key Schedule
HKDF
Session Keys
Traffic Keys
AEAD
AES-GCM
ChaCha20-Poly1305
Forward Secrecy
HTTPS
HTTP over TLS
mTLS
TLS Session Resumption
PSK
0-RTT
TLS Downgrade
MITM
Certificate Validation
Certificate Pinning
HSTS
TLS Configuration
Weak Cipher Suites
Legacy Protocols
OpenSSL Testing
Browser Security
VAPT
SOC Monitoring
Production TLS Hardening
```

The key question for the next chapter will be:

> **How do key exchange, certificates, digital signatures, HKDF, AEAD, nonces, and session keys work together during a real HTTPS/TLS connection?**