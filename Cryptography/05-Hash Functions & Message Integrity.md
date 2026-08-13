# Chapter 05 – Hash Functions & Message Integrity

## Overview

A **cryptographic hash function** is a mathematical function that converts input data of arbitrary length into a fixed-size output called a **hash**, **digest**, or **message digest**.

Conceptually:

```text
                    Arbitrary Input
                         │
                         ▼
                Cryptographic Hash
                         │
                         ▼
                   Fixed-Length
                      Digest
```

For example:

```text
"Hello"
   ↓
SHA-256
   ↓
185f8db32271fe25...
```

Cryptographic hashes are fundamental to:

- Data integrity
- Digital signatures
- Message authentication
- Password storage
- File verification
- Software integrity
- Blockchain systems
- Certificates
- Content-addressable storage
- Deduplication
- Secure protocols

Important hash algorithms include:

```text
MD5
SHA-1
SHA-2
SHA-256
SHA-384
SHA-512
SHA-3
```

Modern applications should generally use:

```text
SHA-256
SHA-384
SHA-512
SHA-3
```

for general cryptographic hashing, depending on the use case.

---

# 1. What is a Hash Function?

A hash function takes an input and produces a fixed-length output.

```text
Input
  │
  ▼
Hash Function
  │
  ▼
Hash / Digest
```

The input can be:

```text
Text
File
Image
Password
Network Packet
Database Record
Software Binary
```

The output has a fixed size for a particular algorithm.

---

# 2. Example

Using SHA-256:

```text
Input:

Hello
```

produces a 256-bit digest.

In hexadecimal representation:

```text
185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
```

The exact output is determined by:

```text
Algorithm
+
Input
```

---

# 3. Hash vs Encryption

Hashing and encryption are fundamentally different.

### Encryption

```text
Plaintext
   ↓
Encryption + Key
   ↓
Ciphertext
   ↓
Decryption + Key
   ↓
Plaintext
```

Encryption is designed to be reversible with the appropriate key.

### Hashing

```text
Input
   ↓
Hash Function
   ↓
Digest
```

A cryptographic hash is designed to be computationally infeasible to reverse.

---

# 4. Hashing vs Encryption

| Property | Hashing | Encryption |
|---|---|---|
| Primary purpose | Integrity / fingerprinting | Confidentiality |
| Reversible | No | Yes with key |
| Uses secret key | Not necessarily | Yes |
| Output | Fixed length | Usually variable / related to input |
| Example | SHA-256 | AES-GCM |
| Password storage | Yes, with password KDF | Generally no |
| Data recovery | No | Yes |

---

# 5. Cryptographic Hash Function

A cryptographic hash function should provide several security properties.

Important properties include:

```text
Deterministic
Fixed-Length Output
Preimage Resistance
Second-Preimage Resistance
Collision Resistance
Avalanche Effect
Efficient Computation
```

---

# 6. Deterministic

A cryptographic hash function is deterministic.

The same input always produces the same digest.

```text
H("Hello")
=
H("Hello")
```

Therefore:

```text
Same Input
    ↓
Same Hash
```

---

# 7. Fixed-Length Output

Hash functions produce fixed-size outputs.

For SHA-256:

```text
Input:
1 byte

or:

1 GB
```

Both produce:

```text
256-bit digest
```

This is one reason hashes are useful as compact fingerprints.

---

# 8. SHA-256

SHA-256 produces:

```text
256 bits
```

which equals:

```text
32 bytes
```

and:

```text
64 hexadecimal characters
```

because:

```text
1 hexadecimal character = 4 bits
```

Therefore:

```text
256 / 4 = 64
```

---

# 9. SHA-512

SHA-512 produces:

```text
512 bits
```

which equals:

```text
64 bytes
```

and:

```text
128 hexadecimal characters
```

---

# 10. SHA-384

SHA-384 produces:

```text
384 bits
```

which equals:

```text
48 bytes
```

and:

```text
96 hexadecimal characters
```

---

# 11. SHA-3

SHA-3 is a newer hash-function family standardized by NIST.

It is based on a fundamentally different internal construction from SHA-2.

SHA-3 variants include:

```text
SHA3-224
SHA3-256
SHA3-384
SHA3-512
```

---

# 12. SHA-2 Family

SHA-2 includes several algorithms:

```text
SHA-224
SHA-256
SHA-384
SHA-512
SHA-512/224
SHA-512/256
```

Commonly used variants include:

```text
SHA-256
SHA-384
SHA-512
```

---

# 13. SHA-1

SHA-1 produces:

```text
160-bit digest
```

SHA-1 is no longer considered collision-resistant for security-sensitive applications.

A practical collision attack against SHA-1 was publicly demonstrated by Google and CWI Amsterdam in 2017.

Therefore:

```text
Do not use SHA-1 for new cryptographic integrity or signature designs.
```

---

# 14. MD5

MD5 produces:

```text
128-bit digest
```

MD5 has known practical collision attacks.

Therefore:

```text
Do not use MD5 for security-sensitive cryptographic integrity.
```

It may still appear in non-security legacy contexts, but that does not make it suitable for modern security designs.

---

# 15. Collision

A collision occurs when two different inputs produce the same hash.

Formally:

```text
A ≠ B

but:

H(A) = H(B)
```

Because hash outputs are finite, collisions must theoretically exist for arbitrary-sized inputs.

The security goal is to make finding such collisions computationally infeasible.

---

# 16. Birthday Paradox

Collision resistance is related to the birthday paradox.

For an ideal `n`-bit hash, generic collision attacks require roughly:

```text
2^(n/2)
```

operations.

Therefore:

```text
128-bit hash
≈ 2^64 collision security

256-bit hash
≈ 2^128 collision security
```

This is why hash output length matters for collision resistance.

---

# 17. Preimage Resistance

Given a hash:

```text
h = H(M)
```

an attacker should find it computationally difficult to recover a message `M` such that:

```text
H(M) = h
```

This property is called:

```text
Preimage Resistance
```

For an ideal `n`-bit hash, generic preimage attacks require approximately:

```text
2^n
```

operations.

---

# 18. Second-Preimage Resistance

Suppose an attacker already knows:

```text
M1
```

and:

```text
H(M1)
```

They should find it difficult to construct another message:

```text
M2 ≠ M1
```

such that:

```text
H(M2) = H(M1)
```

This is:

```text
Second-Preimage Resistance
```

---

# 19. Collision vs Second Preimage

### Collision

Attacker can choose:

```text
M1
M2
```

and attempts to find:

```text
M1 ≠ M2

H(M1) = H(M2)
```

### Second Preimage

Attacker is given:

```text
M1
```

and attempts to find:

```text
M2 ≠ M1
```

such that:

```text
H(M2) = H(M1)
```

These are different security properties.

---

# 20. Hash Security Properties

| Property | Goal |
|---|---|
| Preimage Resistance | Hard to recover input from digest |
| Second-Preimage Resistance | Hard to find another input matching a known digest |
| Collision Resistance | Hard to find any two inputs with same digest |
| Avalanche Effect | Small input changes produce large output changes |

---

# 21. Avalanche Effect

A tiny change in the input should produce a dramatically different digest.

Example:

```text
Input 1:
Hello

Input 2:
hello
```

Only one character changed.

But:

```text
H(Input 1)
```

and:

```text
H(Input 2)
```

should appear completely unrelated.

This is called the:

```text
Avalanche Effect
```

---

# 22. Why Avalanche Effect Matters

Without strong diffusion:

```text
Small Input Change
        ↓
Small Hash Change
```

could reveal information about the input.

A strong cryptographic hash instead aims for:

```text
1-bit input change
       ↓
Many output bits change
```

---

# 23. Hash Function Model

A simplified model:

```text
               Input
                 │
                 ▼
        ┌────────────────┐
        │ Hash Algorithm │
        └────────────────┘
                 │
                 ▼
              Digest
```

Unlike encryption:

```text
Digest
   ↓
No practical general inverse
   ↓
Original input not recovered
```

---

# 24. Hashing Files

Hashes can be used to verify whether a file changed.

Example:

```text
Original File
     ↓
SHA-256
     ↓
Digest A
```

Later:

```text
Downloaded File
     ↓
SHA-256
     ↓
Digest B
```

Compare:

```text
Digest A == Digest B
```

If equal, the file is consistent with the expected digest under the assumptions of the hash function.

---

# 25. File Integrity Example

Suppose a software vendor publishes:

```text
SHA256:
abc123...
```

You download:

```text
application.zip
```

Calculate:

```bash
sha256sum application.zip
```

Then compare the result with the vendor's trusted published digest.

---

# 26. Important Limitation

A hash alone does not tell you who generated it.

An attacker could modify:

```text
File
```

and also replace:

```text
Published Hash
```

Therefore:

```text
Hash
≠
Authentication
```

To authenticate the digest, use mechanisms such as:

```text
Digital Signature
MAC
Trusted Distribution Channel
```

---

# 27. Hash + Digital Signature

A digital signature can authenticate the integrity of data.

Conceptually:

```text
Data
  ↓
Hash
  ↓
Digital Signature
  +
Private Key
```

Verification:

```text
Data
  ↓
Hash
  ↓
Compare with verified signature
  ↓
Valid / Invalid
```

This is widely used in software signing and certificates.

---

# 28. Hash + MAC

A MAC combines secret-key authentication with cryptographic processing.

Conceptually:

```text
Message
   +
Secret Key
   ↓
HMAC
   ↓
Authentication Tag
```

An attacker without the secret key should not be able to generate a valid tag.

---

# 29. HMAC

**HMAC** stands for:

```text
Hash-based Message Authentication Code
```

It combines:

```text
Cryptographic Hash
+
Secret Key
```

Common forms include:

```text
HMAC-SHA-256
HMAC-SHA-384
HMAC-SHA-512
```

---

# 30. HMAC Purpose

HMAC provides:

```text
Integrity
+
Authentication
```

It does not provide confidentiality.

Conceptually:

```text
Message
   +
Secret Key
   ↓
HMAC
   ↓
Tag
```

---

# 31. HMAC Verification

Sender:

```text
Message + Secret Key
        ↓
      HMAC
        ↓
       Tag
```

Receiver:

```text
Message + Secret Key
        ↓
      HMAC
        ↓
Expected Tag
```

Then compare:

```text
Expected Tag
     ==
Received Tag
```

using an appropriate constant-time comparison method where required.

---

# 32. HMAC vs Hash

| Property | Hash | HMAC |
|---|---|---|
| Secret key | No | Yes |
| Integrity | Yes, if digest is trusted | Yes |
| Authentication | No | Yes |
| Example | SHA-256 | HMAC-SHA-256 |
| Confidentiality | No | No |

---

# 33. HMAC vs Encryption

HMAC:

```text
Message
   ↓
Authentication Tag
```

Encryption:

```text
Message
   ↓
Ciphertext
```

Therefore:

```text
HMAC → Integrity + Authentication
Encryption → Confidentiality
AEAD → Confidentiality + Integrity + Authentication
```

---

# 34. Password Hashing

Passwords should generally not be stored as plaintext.

Bad:

```text
username | password
```

Better:

```text
username | password_hash
```

But simply using:

```text
SHA-256(password)
```

is generally not sufficient for password storage.

---

# 35. Why Fast Hashes Are Bad for Password Storage

A password attacker can perform enormous numbers of guesses against a fast hash.

For example:

```text
Password
   ↓
SHA-256
```

is extremely fast.

That is useful for file hashing but undesirable for password storage.

Password storage requires:

```text
Slow
Memory-Hard
Configurable Cost
Salted
```

password hashing/KDF algorithms.

---

# 36. Password Hashing Algorithms

Modern password storage should use dedicated password hashing functions such as:

```text
Argon2id
scrypt
bcrypt
PBKDF2
```

The exact choice depends on the application's requirements and current security guidance.

---

# 37. Salt

A **salt** is a unique random value associated with a password.

Conceptually:

```text
Password
   +
Random Salt
   ↓
Password KDF
   ↓
Stored Hash
```

The salt does not need to be secret.

---

# 38. Why Salts Matter

Without salts:

```text
User A:
password123 → Hash X

User B:
password123 → Hash X
```

An attacker can identify identical passwords.

With unique salts:

```text
password123 + saltA → Hash A

password123 + saltB → Hash B
```

The resulting stored values differ.

---

# 39. Salt Does Not Make Passwords Secret

A salt is normally stored alongside the password hash.

Example:

```text
username
salt
password_hash
```

Security comes from:

```text
Unique Salt
+
Strong Password KDF
+
Strong Password
```

not from hiding the salt.

---

# 40. Pepper

A **pepper** is an additional secret value used in some password-storage architectures.

Conceptually:

```text
Password
   +
Salt
   +
Pepper
   ↓
Password KDF
   ↓
Stored Hash
```

Unlike a salt:

```text
Pepper should remain secret.
```

It may be stored separately from the database.

---

# 41. Password Storage Architecture

A robust conceptual model:

```text
User Password
      │
      ├── Unique Salt
      │
      └── Optional Pepper
              │
              ▼
          Argon2id
              │
              ▼
       Password Hash
              │
              ▼
           Database
```

---

# 42. Hashing Passwords with Argon2id

Argon2id is designed specifically for password hashing and resistance against certain hardware-accelerated guessing attacks.

Conceptually:

```text
Password
   +
Salt
   +
Cost Parameters
   ↓
Argon2id
   ↓
Stored Hash
```

The encoded output typically contains the parameters needed for verification.

---

# 43. Password Verification

During login:

```text
User Password
      ↓
Read Stored Salt + Parameters
      ↓
Run Password KDF
      ↓
Compare Derived Value
      ↓
Valid / Invalid
```

The original password is not recovered from the stored hash.

---

# 44. Brute-Force Password Attack

An attacker may obtain a password hash database.

Then:

```text
Candidate Password
      ↓
Password KDF
      ↓
Candidate Hash
      ↓
Compare
```

Repeated many times.

Password hashing algorithms slow down this process.

---

# 45. Dictionary Attack

Instead of trying every possible character combination, attackers often use lists of likely passwords.

Examples:

```text
password
password123
qwerty
admin
companyname
welcome
```

This is a:

```text
Dictionary Attack
```

---

# 46. Credential Stuffing

Credential stuffing is different from password cracking.

Attackers use:

```text
Previously leaked
username + password pairs
```

against other services.

Hashing does not directly prevent credential stuffing.

Defenses include:

```text
MFA
Rate Limiting
Credential Breach Detection
Password Managers
Login Monitoring
Risk-Based Authentication
```

---

# 47. Rainbow Tables

A rainbow table is a precomputed structure used to accelerate certain password-hash cracking attacks.

Unique salts dramatically reduce the usefulness of precomputed tables.

Therefore:

```text
Unique Salt per Password
```

is essential.

---

# 48. Hash Length and Security

For an ideal hash:

```text
Preimage security ≈ 2^n
Collision security ≈ 2^(n/2)
```

where `n` is the output size in bits.

For SHA-256:

```text
Preimage ≈ 2^256
Collision ≈ 2^128
```

These are idealized generic security estimates, not guarantees against every cryptanalytic attack.

---

# 49. SHA-256 vs SHA-512

| Feature | SHA-256 | SHA-512 |
|---|---:|---:|
| Digest | 256 bits | 512 bits |
| Hex length | 64 | 128 |
| Family | SHA-2 | SHA-2 |
| Common use | Very common | Common |
| Collision security | ~128-bit generic | ~256-bit generic |

The correct choice depends on the application and platform.

---

# 50. SHA-2 vs SHA-3

SHA-2:

```text
Merkle-Damgård-style family
```

SHA-3:

```text
Sponge construction
```

SHA-3 provides an independently designed hash family with different internal structure.

Both can be used for modern cryptographic hashing when appropriate.

---

# 51. Sponge Construction

SHA-3 is based on a sponge construction.

Conceptually:

```text
Input
  ↓
Absorb
  ↓
Internal State
  ↓
Squeeze
  ↓
Output
```

This differs fundamentally from the internal construction used by SHA-2.

---

# 52. SHAKE

SHA-3 also introduced extendable-output functions:

```text
SHAKE128
SHAKE256
```

These can produce variable-length outputs.

Conceptually:

```text
Input
  ↓
SHAKE
  ↓
Requested Output Length
```

This is different from fixed-length functions such as SHA-256.

---

# 53. Length-Extension Attacks

Some hash constructions based on the Merkle-Damgård design can be vulnerable to length-extension attacks when used incorrectly.

Conceptually, an attacker may know:

```text
H(secret || message)
```

and attempt to construct a valid hash for:

```text
secret || message || attacker_data
```

without knowing the secret.

This is one reason naive constructions such as:

```text
SHA256(secret || message)
```

should not be used as a replacement for HMAC.

---

# 54. HMAC Prevents Naive Length-Extension Problems

Instead of:

```text
SHA256(secret || message)
```

use:

```text
HMAC-SHA-256(secret, message)
```

HMAC is specifically designed for keyed message authentication.

---

# 55. Hashing and Digital Signatures

Digital signature systems usually sign a digest rather than the entire message directly.

Conceptually:

```text
Large Message
      ↓
Hash
      ↓
Small Digest
      ↓
Signature Algorithm
      ↓
Signature
```

This improves efficiency.

---

# 56. Hashing in Certificates

Certificates contain signed information.

Conceptually:

```text
Certificate Data
       ↓
Signature Algorithm
       ↓
CA Signature
```

The signature mechanism internally uses hashing.

This helps protect:

```text
Certificate Integrity
Certificate Authenticity
```

---

# 57. Hashing in Software Security

Software vendors can publish:

```text
SHA-256
```

digests for releases.

Users can verify:

```text
Downloaded File
      ↓
SHA-256
      ↓
Compare with trusted digest
```

For stronger authenticity, software signatures are preferred over relying on an unauthenticated hash alone.

---

# 58. Hashing in Git

Git uses cryptographic object identifiers based on hashes.

Historically:

```text
SHA-1
```

was used extensively.

Modern Git supports:

```text
SHA-256 repositories
```

for stronger cryptographic properties.

The Git ecosystem has additional mechanisms beyond simply "hashing a file."

---

# 59. Hashing in Blockchain

Blockchain systems commonly use cryptographic hashes for:

```text
Block Linking
Transaction Identification
Data Integrity
Merkle Trees
Proof-of-Work
```

Conceptually:

```text
Block N
   ↓
Hash
   ↓
Referenced by Block N+1
```

Changing an earlier block can therefore affect subsequent hashes.

---

# 60. Merkle Trees

A Merkle tree organizes hashes hierarchically.

Example:

```text
              Root Hash
              /       \
           Hash A     Hash B
           /  \       /  \
         H1   H2     H3   H4
         │    │      │    │
        Data Data   Data Data
```

This allows efficient verification of whether a particular data item belongs to a larger dataset.

---

# 61. Hash Commitments

A commitment scheme can use a hash to commit to a value without revealing it immediately.

Conceptually:

```text
Secret Value
     +
Randomness
     ↓
Hash
     ↓
Commitment
```

Later:

```text
Reveal Value + Randomness
     ↓
Verify Hash
```

This concept appears in cryptographic protocols.

---

# 62. Content-Addressable Storage

Some systems identify data using its cryptographic digest.

Conceptually:

```text
Data
 ↓
Hash
 ↓
Content Identifier
```

If the content changes:

```text
New Content
 ↓
Different Hash
 ↓
Different Identifier
```

This provides useful integrity properties.

---

# 63. Hash Collision Attacks

An attacker attempting to find:

```text
M1 ≠ M2
```

such that:

```text
H(M1) = H(M2)
```

is performing a collision attack.

For weak algorithms:

```text
MD5
SHA-1
```

practical collision attacks exist.

---

# 64. Chosen-Prefix Collisions

A particularly powerful collision scenario is a **chosen-prefix collision**.

The attacker chooses:

```text
Prefix A
Prefix B
```

and attempts to construct:

```text
Message A
Message B
```

such that:

```text
H(Message A)
=
H(Message B)
```

This can have serious implications when a vulnerable hash is used in signatures or certificates.

---

# 65. SHAttered

In 2017, Google and CWI Amsterdam demonstrated a practical collision attack against SHA-1 called:

```text
SHAttered
```

This demonstrated that SHA-1 could no longer be considered collision-resistant for security-sensitive applications.

---

# 66. Hash Security vs Password Security

These are different requirements.

### General Hashing

Needs:

```text
Fast
Collision Resistant
Preimage Resistant
```

### Password Hashing

Needs:

```text
Slow
Memory-Hard where appropriate
Salted
Cost Adjustable
Attack Resistant
```

Therefore:

```text
SHA-256
```

is excellent for many integrity applications but is not a password-storage algorithm by itself.

---

# 67. Hashing vs KDF

A KDF derives cryptographic key material.

Examples:

```text
HKDF
PBKDF2
Argon2id
scrypt
```

Their purposes differ.

```text
Hash:
Input → Digest

KDF:
Input Secret → Derived Key
```

Password KDFs are specifically designed to make password guessing more expensive.

---

# 68. HKDF

**HKDF** stands for:

```text
HMAC-based Key Derivation Function
```

It is useful for deriving cryptographic keys from existing high-entropy secret material.

Conceptually:

```text
Input Key Material
       ↓
HKDF-Extract
       ↓
Pseudorandom Key
       ↓
HKDF-Expand
       ↓
Derived Key Material
```

---

# 69. HKDF vs Password KDF

Do not confuse:

```text
HKDF
```

with:

```text
Argon2id / scrypt / bcrypt / PBKDF2
```

HKDF is generally intended for deriving keys from already strong secret material.

Password KDFs are specifically designed to resist password guessing.

---

# 70. Hash-Based Integrity Verification

A simple integrity workflow:

```text
Trusted Digest
      │
      │
      ▼
Downloaded File
      │
      ▼
SHA-256
      │
      ▼
Calculated Digest
      │
      ▼
Compare
```

If:

```text
Calculated == Trusted
```

the file matches the trusted digest.

---

# 71. Why Trust Matters

Suppose an attacker controls both:

```text
File
```

and:

```text
Hash
```

They can modify both.

Therefore:

```text
Hash verification is only meaningful
when the expected hash is obtained
through a trusted channel.
```

Digital signatures can provide stronger authenticity.

---

# 72. Hash-Based Integrity vs MAC

### Hash

```text
No secret
```

Useful when the expected digest is distributed through a trusted channel.

### HMAC

```text
Shared secret
```

Provides authentication between parties sharing the secret.

### Digital Signature

```text
Private/Public key pair
```

Provides verifiable authenticity without requiring the verifier to possess the signing secret.

---

# 73. Comparison

| Mechanism | Confidentiality | Integrity | Authentication |
|---|---:|---:|---:|
| SHA-256 | No | Yes* | No |
| HMAC | No | Yes | Yes |
| Digital Signature | No | Yes | Yes |
| AES-GCM | Yes | Yes | Yes |
| Plain AES-CTR | Yes | No | No |

`*` Hashes provide integrity checking only when the expected digest itself is trusted.

---

# 74. Practical Python – SHA-256

```python
import hashlib

message = b"Hello Cryptography"

digest = hashlib.sha256(message).hexdigest()

print(digest)
```

---

# 75. Practical Python – SHA-512

```python
import hashlib

message = b"Hello Cryptography"

digest = hashlib.sha512(message).hexdigest()

print(digest)
```

---

# 76. Practical Python – File Hashing

```python
import hashlib

def sha256_file(path):
    digest = hashlib.sha256()

    with open(path, "rb") as file:
        for chunk in iter(lambda: file.read(8192), b""):
            digest.update(chunk)

    return digest.hexdigest()


print(sha256_file("application.zip"))
```

Reading in chunks avoids loading an entire large file into memory.

---

# 77. Practical Python – HMAC

```python
import hmac
import hashlib

key = b"secret-key"
message = b"Hello Cryptography"

tag = hmac.new(
    key,
    message,
    hashlib.sha256,
).hexdigest()

print(tag)
```

---

# 78. HMAC Verification

```python
expected = hmac.new(
    key,
    message,
    hashlib.sha256,
).digest()

received = expected

if hmac.compare_digest(expected, received):
    print("Valid")
else:
    print("Invalid")
```

Use constant-time comparison functions where appropriate when comparing authentication tags or other secret-derived values.

---

# 79. Password Hashing Example

With a suitable password-hashing library, a conceptual workflow is:

```python
password = "user-password"

# Use a dedicated password hashing library.
# Example:
# hash = argon2.hash(password)

# During login:
# verify(password, stored_hash)
```

Do not implement Argon2, bcrypt, or password-KDF internals yourself.

---

# 80. Practical Exercise – Avalanche Effect

Calculate:

```text
SHA256("Hello")
SHA256("hello")
```

Compare the two outputs.

Observe that:

```text
Small Input Change
        ↓
Large Digest Difference
```

---

# 81. Practical Exercise – File Integrity

1. Create a file:

```text
hello.txt
```

2. Calculate:

```bash
sha256sum hello.txt
```

3. Modify one character.

4. Calculate the hash again.

Observe:

```text
Original Hash
≠
Modified Hash
```

---

# 82. Practical Exercise – HMAC

Create:

```text
Message
Secret Key
```

Generate:

```text
HMAC-SHA-256
```

Then modify the message.

Observe:

```text
Original Tag
≠
Modified Message Tag
```

---

# 83. Practical Exercise – Password Hashing

Using a password-hashing library:

```text
Password
   ↓
Argon2id
   ↓
Stored Hash
```

Then verify:

```text
Correct Password → Valid
Wrong Password   → Invalid
```

Repeat hashing the same password.

Observe that properly salted password hashing produces different stored outputs.

---

# 84. VAPT Testing Checklist

When assessing an application:

```text
☐ Identify hashing algorithms
☐ Check for MD5 usage
☐ Check for SHA-1 usage
☐ Check password hashing algorithm
☐ Check password salts
☐ Check password KDF cost
☐ Check HMAC implementation
☐ Check integrity verification
☐ Check signature verification
☐ Check for length-extension-prone constructions
☐ Check whether hashes are trusted/authenticated
```

---

# 85. Example VAPT Findings

Potential findings include:

```text
MD5 Used for Security
SHA-1 Used for Security
Weak Password Hashing
Unsalted Password Hashes
Fast Hash Used for Password Storage
Weak KDF Parameters
Naive Secret Hashing
Missing HMAC
Improper Integrity Validation
Untrusted Hash Comparison
Weak File Integrity Mechanism
```

Severity depends on:

```text
Affected Function
Exploitability
Data Sensitivity
Attack Preconditions
Business Impact
```

---

# 86. Common Hashing Mistakes

```text
❌ Storing plaintext passwords
❌ Using MD5 for password storage
❌ Using SHA-1 for security-sensitive hashing
❌ Using SHA-256 alone for passwords
❌ Using one salt for every password
❌ Using predictable salts
❌ Using unsalted password hashes
❌ Treating a hash as encryption
❌ Assuming a hash provides authentication
❌ Using SHA256(secret || message) as a replacement for HMAC
❌ Trusting an unauthenticated downloaded hash
```

---

# 87. Secure Hashing Checklist

```text
☐ Use SHA-256/SHA-384/SHA-512/SHA-3 where appropriate
☐ Use HMAC for keyed message authentication
☐ Use Argon2id/scrypt/bcrypt/PBKDF2 for passwords
☐ Generate unique random password salts
☐ Store password-hashing parameters
☐ Use secure comparison methods
☐ Authenticate integrity metadata where required
☐ Avoid MD5 and SHA-1 for security-sensitive purposes
☐ Use established cryptographic libraries
```

---

# 88. Hash Functions in SOC Operations

SOC analysts may encounter hashes constantly.

Common examples:

```text
File Hash
Process Hash
Malware Hash
IOC Hash
Artifact Hash
Certificate Hash
Container Image Digest
```

Common formats include:

```text
MD5
SHA-1
SHA-256
SHA-512
```

---

# 89. File Hash as an IOC

Security teams may use:

```text
SHA-256
```

as a malware indicator of compromise.

Example:

```text
Malicious File
      ↓
SHA-256
      ↓
IOC
      ↓
SIEM / EDR / Threat Intelligence
```

A hash can identify a specific file version.

---

# 90. Limitations of Hash-Based IOCs

A hash identifies a specific artifact.

An attacker can modify a malicious file:

```text
Malware Version A
      ↓
Modify 1 byte
      ↓
Malware Version B
```

The hash changes.

Therefore, defenders should also use:

```text
Behavioral Indicators
Network Indicators
Domain Intelligence
Process Behavior
Command Lines
File Paths
Registry Activity
Detection Rules
```

---

# 91. Container Image Digests

Container registries commonly identify images using content digests.

Conceptually:

```text
Container Image
      ↓
Cryptographic Digest
      ↓
Image Reference
```

This allows systems to refer to an immutable content version.

For example:

```text
image@sha256:<digest>
```

is more precise than relying only on a mutable tag such as:

```text
image:latest
```

---

# 92. Kubernetes Security Relevance

Cryptographic hashes are important in Kubernetes environments for:

```text
Container Image Digests
Admission Policies
Artifact Verification
Supply Chain Security
Software Signing
Configuration Integrity
Secrets / Credential Workflows
```

Image digests help ensure that the referenced container content matches a specific artifact.

---

# 93. Hashes and Digital Forensics

Digital forensic investigators use hashes to:

```text
Identify Known Files
Verify Evidence Integrity
Compare Artifacts
Detect Changes
Identify Malware
Validate Acquisitions
```

For example:

```text
Evidence
   ↓
SHA-256
   ↓
Recorded Digest
```

If the evidence changes:

```text
New Digest
≠
Recorded Digest
```

---

# 94. Hashes and Evidence Integrity

A hash can demonstrate that two datasets produce the same digest under the selected algorithm.

However:

```text
Hash ≠ Complete Chain of Custody
```

Forensic integrity also requires:

```text
Documentation
Access Controls
Acquisition Procedures
Chain of Custody
Secure Storage
```

---

# 95. Cryptographic Hashes and Compliance

Hash functions may be involved in:

```text
Audit Evidence
Digital Signatures
File Integrity Monitoring
Log Integrity
Software Verification
Data Validation
```

The exact algorithm requirements depend on the applicable standard or regulatory framework.

---

# 96. Log Integrity

Logs can be protected against undetected modification using techniques such as:

```text
HMAC
Digital Signatures
Hash Chains
Immutable Storage
Write-Once Storage
```

A simple hash alone is insufficient if an attacker can modify both:

```text
Log
+
Stored Hash
```

---

# 97. Hash Chains

A hash chain links records together.

Conceptually:

```text
Record 1
   ↓
Hash 1
   ↓
Record 2 + Hash 1
   ↓
Hash 2
   ↓
Record 3 + Hash 2
   ↓
Hash 3
```

Changing an earlier record changes subsequent hashes.

This concept is useful for tamper-evident data structures.

---

# 98. Merkle Tree vs Hash Chain

| Feature | Hash Chain | Merkle Tree |
|---|---|---|
| Structure | Sequential | Tree |
| Verification | Sequential dependency | Efficient membership proof |
| Parallelism | Limited | Better |
| Common use | Logs / linked records | Blockchains / distributed systems |

---

# 99. Hashing in Digital Forensics

Typical workflow:

```text
Acquire Evidence
      ↓
Calculate SHA-256
      ↓
Record Digest
      ↓
Analyze Copy
      ↓
Recalculate
      ↓
Compare
```

This helps detect accidental or unauthorized modification.

---

# 100. Hashing in Supply Chain Security

Modern software supply chains use:

```text
Hashes
+
Digital Signatures
+
Provenance
+
Trusted Build Systems
```

Conceptually:

```text
Source Code
    ↓
Build
    ↓
Artifact
    ↓
Hash
    ↓
Sign
    ↓
Publish
```

Consumers can verify:

```text
Integrity
+
Authenticity
```

---

# 101. Hash vs Digital Signature in Supply Chain

A hash provides:

```text
Integrity Fingerprint
```

A digital signature provides:

```text
Integrity
+
Authentication / Provenance Binding
```

Therefore:

```text
Hash alone
```

is not equivalent to:

```text
Signed Artifact
```

---

# 102. Security Architecture

A modern software verification architecture can look like:

```text
                    Signing Private Key
                           │
                           ▼
Source → Build → Artifact → Hash → Signature
                                      │
                                      ▼
                                   Registry
                                      │
                                      ▼
                                  Consumer
                                      │
                                      ▼
                            Signature Verification
                                      │
                                      ▼
                              Digest Verification
```

This provides stronger supply-chain assurances than a standalone hash.

---

# 103. Important Algorithm Guidance

For general cryptographic hashing:

```text
Preferred:
SHA-256
SHA-384
SHA-512
SHA-3
```

For message authentication:

```text
HMAC-SHA-256
HMAC-SHA-384
HMAC-SHA-512
```

For passwords:

```text
Argon2id
scrypt
bcrypt
PBKDF2
```

Avoid for new security-sensitive applications:

```text
MD5
SHA-1
```

---

# 104. Hash Algorithm Selection

Choose based on:

```text
Purpose
Security Requirements
Standards
Performance
Compatibility
Protocol Requirements
```

Do not select an algorithm merely because:

```text
"More bits = always better."
```

Correct construction matters as much as output size.

---

# 105. Security Design Principle

A strong security design separates:

```text
Hashing
Encryption
Authentication
Key Derivation
Digital Signatures
Password Storage
```

Do not assume one primitive can safely replace another.

For example:

```text
SHA-256
≠
AES
≠
HMAC
≠
Argon2id
≠
ECDSA
```

Each solves a different problem.

---

# 106. Cryptographic Primitive Selection

| Requirement | Suitable Primitive |
|---|---|
| General digest | SHA-256 / SHA-3 |
| Message authentication | HMAC |
| Bulk encryption | AES-GCM / ChaCha20-Poly1305 |
| Password storage | Argon2id / scrypt / bcrypt / PBKDF2 |
| Key derivation | HKDF |
| Digital signature | RSA-PSS / ECDSA / Ed25519 |
| Key agreement | ECDH / X25519 |

---

# 107. Common Interview Questions

## What is a cryptographic hash?

A function that maps arbitrary-length input to a fixed-length digest while providing security properties such as preimage, second-preimage, and collision resistance.

---

## Is hashing encryption?

No. Encryption is designed to be reversible with the appropriate key, while cryptographic hashing is designed as a one-way transformation.

---

## What is SHA-256?

SHA-256 is a member of the SHA-2 family that produces a 256-bit digest.

---

## What is collision resistance?

The property that makes it computationally difficult to find two different inputs producing the same hash.

---

## What is preimage resistance?

The property that makes it computationally difficult to recover an input corresponding to a known digest.

---

## What is second-preimage resistance?

The property that makes it difficult to find a different message producing the same hash as a specific known message.

---

## What is the avalanche effect?

A small input change causes a large and unpredictable change in the hash output.

---

## Why is MD5 insecure?

MD5 has practical collision attacks and should not be used for security-sensitive cryptographic integrity.

---

## Why is SHA-1 insecure?

SHA-1 has practical collision attacks and is no longer considered collision-resistant for security-sensitive applications.

---

## Can SHA-256 be used to store passwords?

A raw SHA-256 hash is generally inappropriate for password storage because it is too fast. Use a dedicated password hashing/KDF algorithm such as Argon2id.

---

## What is a salt?

A unique random value added to password hashing so identical passwords do not produce identical stored hashes and precomputed attacks become less useful.

---

## What is HMAC?

HMAC is a keyed message authentication construction based on a cryptographic hash function.

---

## Does HMAC encrypt data?

No. HMAC provides integrity and authentication, not confidentiality.

---

## What is the difference between HMAC and a digital signature?

HMAC uses a shared secret, while digital signatures use a private/public key pair and can provide publicly verifiable authentication.

---

## What is a length-extension attack?

An attack applicable to certain hash constructions where knowledge of a digest can allow an attacker to construct a valid digest for an extended message without knowing a secret prefix.

---

## Why should SHA-256(secret || message) not replace HMAC?

Because some hash constructions have length-extension properties. HMAC is specifically designed for keyed message authentication.

---

# 108. Quick Revision Table

| Concept | Meaning |
|---|---|
| Hash | Fixed-length digest |
| Digest | Hash output |
| SHA-256 | 256-bit SHA-2 hash |
| SHA-512 | 512-bit SHA-2 hash |
| SHA-3 | Sponge-based hash family |
| Collision | Two different inputs, same hash |
| Preimage | Recover input from digest |
| Second Preimage | Find alternate input matching known hash |
| Avalanche | Small input change → large output change |
| HMAC | Keyed hash-based authentication |
| Salt | Unique non-secret password value |
| Pepper | Additional secret password-protection value |
| Argon2id | Password hashing algorithm |
| HKDF | Key derivation function |
| Merkle Tree | Hierarchical hash structure |
| Hash Chain | Sequential hash-linked records |

---

# 109. Key Takeaways

```text
1. Hash functions map arbitrary input to fixed-length digests.

2. Hashing is not encryption.

3. Cryptographic hashes should provide preimage, second-preimage, and collision resistance.

4. The avalanche effect makes small input changes produce dramatically different outputs.

5. SHA-256 is a widely used modern cryptographic hash.

6. SHA-2 and SHA-3 provide modern hash-function families.

7. MD5 and SHA-1 should not be used for security-sensitive cryptographic purposes.

8. Generic collision security for an ideal n-bit hash is approximately 2^(n/2).

9. Generic preimage security is approximately 2^n.

10. HMAC adds a secret key to provide message authentication.

11. Hashes alone do not authenticate the source of a digest.

12. Passwords should use dedicated password-hashing functions rather than fast general-purpose hashes.

13. Password salts should be unique and randomly generated.

14. HKDF is designed for deriving keys from suitable secret material.

15. Length-extension attacks demonstrate why naive keyed hashing constructions can be dangerous.

16. Digital signatures commonly hash messages before signing.

17. Hashes are widely used in software integrity, forensics, malware analysis, Git, blockchain systems, and supply-chain security.

18. A cryptographic primitive should be selected according to the security problem it is intended to solve.
```

---

# 110. Chapter Summary

This chapter covered the fundamentals and practical applications of cryptographic hash functions.

We learned:

```text
Cryptographic Hash Functions
SHA-2
SHA-256
SHA-384
SHA-512
SHA-3
SHAKE
MD5
SHA-1
Collision Resistance
Preimage Resistance
Second-Preimage Resistance
Avalanche Effect
Birthday Attacks
HMAC
Password Hashing
Salts
Peppers
Argon2id
scrypt
bcrypt
PBKDF2
HKDF
Length-Extension Attacks
Merkle Trees
Hash Chains
Digital Signatures
File Integrity
Software Integrity
Supply Chain Security
Forensics
IOC Hashes
Container Image Digests
```

The central principle is:

> **A hash provides a compact cryptographic fingerprint, but hashing alone does not provide confidentiality or authentication. The correct primitive must be selected according to the security objective.**

A useful mental model is:

```text
             Security Requirement
                     │
       ┌─────────────┼──────────────┐
       ▼             ▼              ▼
   Integrity    Authentication   Confidentiality
       │             │              │
       ▼             ▼              ▼
     Hash           HMAC           AEAD
                     │
                     │
                     ▼
              Digital Signature
```

---

# Next Chapter

## Chapter 06 – Message Authentication Codes (MAC & HMAC)

The next chapter focuses specifically on **message authentication** and will cover:

```text
Message Authentication
MAC
HMAC
HMAC-SHA-256
HMAC-SHA-512
CMAC
GMAC
Authentication Tags
Integrity vs Authentication
MAC vs Hash
MAC vs Digital Signature
HMAC Construction
HMAC Security
Timing Attacks
Constant-Time Comparison
Key Management
Replay Protection
API Authentication
Webhook Verification
JWT Signing Concepts
Secure Message Authentication
VAPT Testing
Real-World Applications
```

The key question for the next chapter will be:

> **How can two parties sharing a secret key verify that a message was not modified and was generated by someone who knows that secret?**