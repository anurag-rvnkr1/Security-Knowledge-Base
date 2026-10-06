# Chapter 06 – Message Authentication Codes (MAC & HMAC)

## Overview

A **Message Authentication Code (MAC)** is a cryptographic mechanism used to provide:

- Message integrity
- Message authentication
- Protection against unauthorized modification

A MAC uses:

```text
Message
   +
Secret Key
   ↓
MAC Algorithm
   ↓
Authentication Tag
```

The recipient, who also possesses the secret key, independently calculates the MAC and compares it with the received tag.

A simplified model is:

```text
                Shared Secret Key
                  /            \
                 ▼              ▼
              Sender         Receiver
                 │              │
              Message        Message
                 │              │
                 ▼              ▼
               MAC            MAC
                 │              │
                 ▼              ▼
              Tag A          Tag B
                 │              │
                 └──── Compare ─┘
                       │
                  Valid / Invalid
```

Important MAC constructions include:

```text
HMAC
CMAC
GMAC
```

MACs are widely used in:

```text
APIs
Webhooks
Secure Protocols
Network Authentication
Data Integrity
Message Authentication
Cryptographic Protocols
```

---

# 1. What is a Message Authentication Code?

A MAC is a cryptographic tag generated from:

```text
Message
+
Secret Key
```

The recipient uses the same secret key to verify the message.

Conceptually:

```text
MAC = F(Key, Message)
```

The exact construction depends on the MAC algorithm.

---

# 2. Purpose of a MAC

A MAC primarily provides:

```text
Integrity
+
Authentication
```

It answers two questions:

```text
Was the message modified?

Does the sender possess the shared secret key?
```

It does **not** inherently provide confidentiality.

---

# 3. MAC Example

Suppose Alice and Bob share:

```text
Secret Key = K
```

Alice sends:

```text
Message = "Transfer ₹1000"
```

Alice calculates:

```text
MAC(K, "Transfer ₹1000")
```

and sends:

```text
Message + MAC
```

Bob receives both and calculates the MAC again.

If the values match:

```text
MAC_received
=
MAC_calculated
```

the message passes authentication.

---

# 4. MAC Security Model

An attacker may see:

```text
Message
MAC
```

but should not be able to create a valid MAC for a modified message without knowing the secret key.

For example:

```text
Original:

Transfer ₹1000
MAC = ABC123

Attacker changes:

Transfer ₹9000
```

The attacker should not be able to produce the correct MAC for:

```text
Transfer ₹9000
```

without the secret key.

---

# 5. MAC vs Hash

A normal hash uses:

```text
Message
   ↓
Hash
```

A MAC uses:

```text
Message
   +
Secret Key
   ↓
MAC
```

Therefore:

```text
Hash → Integrity fingerprint
MAC  → Integrity + Authentication
```

---

# 6. MAC vs Encryption

Encryption provides:

```text
Confidentiality
```

A MAC provides:

```text
Integrity
+
Authentication
```

Conceptually:

```text
Encryption:

Message
  ↓
Ciphertext


MAC:

Message + Secret
  ↓
Authentication Tag
```

A MAC does not hide the message.

---

# 7. MAC vs Digital Signature

Both can provide authentication and integrity, but their trust models are different.

### MAC

```text
Shared Secret
```

Both parties possess the same secret.

### Digital Signature

```text
Private Key
+
Public Key
```

Only the signer possesses the private key.

Anyone with the public key can verify the signature.

---

# 8. MAC vs Digital Signature

| Property | MAC | Digital Signature |
|---|---|---|
| Secret | Shared key | Private key |
| Verification | Requires secret | Public key |
| Public verification | No | Yes |
| Non-repudiation | Generally no | Can support it |
| Performance | Generally fast | Generally slower |
| Examples | HMAC, CMAC | RSA-PSS, ECDSA, Ed25519 |

---

# 9. HMAC

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

Common variants include:

```text
HMAC-SHA-256
HMAC-SHA-384
HMAC-SHA-512
```

---

# 10. HMAC Formula

The standard HMAC construction can be represented as:

```text
HMAC(K, M)
=
H((K' XOR opad) || H((K' XOR ipad) || M))
```

Where:

```text
K'   = normalized key
M    = message
H    = hash function
ipad = inner padding
opad = outer padding
||   = concatenation
```

The construction is deliberately more sophisticated than simply:

```text
Hash(Key || Message)
```

---

# 11. HMAC Structure

Conceptually:

```text
             Secret Key
                 │
          ┌──────┴──────┐
          ▼             ▼
       Inner Pad      Outer Pad
          │             │
          ▼             │
      Message           │
          │             │
          ▼             │
      Inner Hash        │
          │             │
          └──────┬──────┘
                 ▼
             Outer Hash
                 │
                 ▼
             HMAC Tag
```

---

# 12. Why Not Simply Hash the Key and Message?

A naive construction such as:

```text
SHA256(Key || Message)
```

can be problematic with certain hash constructions because of length-extension properties.

HMAC was specifically designed to avoid these problems and provide a well-studied keyed authentication construction.

Therefore:

```text
Do not invent your own MAC construction.
```

Use:

```text
HMAC
CMAC
GMAC
AEAD
```

as appropriate.

---

# 13. HMAC-SHA-256

A common construction is:

```text
HMAC-SHA-256
```

It uses:

```text
SHA-256
+
Secret Key
```

and produces:

```text
256-bit authentication tag
```

or:

```text
32 bytes
```

---

# 14. HMAC-SHA-512

HMAC can also use SHA-512:

```text
HMAC-SHA-512
```

The output is:

```text
512 bits
=
64 bytes
```

The correct choice depends on:

```text
Protocol
Security Requirements
Compatibility
Performance
Standards
```

---

# 15. HMAC Verification

Sender:

```text
Message
   +
Secret Key
   ↓
HMAC
   ↓
Tag
```

Receiver:

```text
Message
   +
Secret Key
   ↓
HMAC
   ↓
Expected Tag
```

Then:

```text
Expected Tag
     ==
Received Tag
```

If valid:

```text
Accept
```

If invalid:

```text
Reject
```

---

# 16. Constant-Time Comparison

Authentication tags should not be compared using ordinary operations if doing so can expose timing information.

Avoid relying on patterns such as:

```python
if received == expected:
```

for sensitive authentication values in security-critical code.

Prefer a constant-time comparison function provided by a trusted library.

Python example:

```python
import hmac

if hmac.compare_digest(received, expected):
    print("Valid")
else:
    print("Invalid")
```

---

# 17. Timing Attack

A naive comparison might stop when the first differing byte is found.

Conceptually:

```text
AAAA
BBBB
```

may fail immediately.

But:

```text
AAAA
AAAB
```

may take longer.

Repeated measurements could potentially reveal information about the expected value.

This is a:

```text
Timing Side Channel
```

---

# 18. Constant-Time Comparison

A constant-time comparison aims to prevent the comparison time from depending on how many initial bytes match.

Conceptually:

```text
Tag A
Tag B
 ↓
Constant-Time Comparison
 ↓
Valid / Invalid
```

This does not make the entire application automatically constant-time, but it is an important defensive measure for comparing secret-derived authentication values.

---

# 19. MAC Key Requirements

A MAC key should be:

```text
Secret
Unpredictable
Sufficiently Strong
Generated Using CSPRNG
Protected During Storage
Rotated Appropriately
```

Do not use:

```text
password123
companyname
123456
```

as production MAC keys.

---

# 20. MAC Key Generation

Use a cryptographically secure random generator.

Python:

```python
import secrets

key = secrets.token_bytes(32)

print(key.hex())
```

This generates:

```text
256-bit key
```

using Python's cryptographically secure randomness facilities.

---

# 21. MAC Key Storage

Never hard-code:

```python
SECRET_KEY = "my-secret"
```

inside source code.

Prefer:

```text
Secrets Manager
KMS
HSM
Protected Environment Configuration
Secure Key Store
```

depending on the architecture.

---

# 22. HMAC Example in Python

```python
import hmac
import hashlib

key = b"very-secret-key"
message = b"Hello World"

tag = hmac.new(
    key,
    message,
    hashlib.sha256
).digest()

print(tag.hex())
```

---

# 23. HMAC Verification in Python

```python
expected = hmac.new(
    key,
    message,
    hashlib.sha256
).digest()

if hmac.compare_digest(tag, expected):
    print("Message authenticated")
else:
    print("Authentication failed")
```

---

# 24. Modified Message

Suppose an attacker changes:

```text
Hello World
```

to:

```text
Hello world
```

The HMAC changes completely.

```text
Original Message
      ↓
HMAC A

Modified Message
      ↓
HMAC B

HMAC A ≠ HMAC B
```

The attacker cannot produce a valid new tag without the key.

---

# 25. Modified MAC

Suppose an attacker modifies:

```text
Message
```

and keeps:

```text
Original MAC
```

The receiver calculates:

```text
MAC(modified_message)
```

which does not match the original tag.

Therefore:

```text
Authentication Failed
```

---

# 26. MAC Does Not Provide Confidentiality

Suppose:

```text
Message:
Transfer ₹1000

MAC:
ABC123
```

The MAC does not hide:

```text
Transfer ₹1000
```

Anyone who can observe the communication may still read the message.

For confidentiality, use:

```text
Encryption
```

or preferably:

```text
Authenticated Encryption
```

when appropriate.

---

# 27. AEAD vs HMAC

AEAD constructions combine encryption and authentication.

Examples:

```text
AES-GCM
ChaCha20-Poly1305
```

HMAC provides authentication but not encryption.

Conceptually:

```text
HMAC:

Message
  +
Key
  ↓
Tag


AEAD:

Message
  +
Key
  +
Nonce
  ↓
Ciphertext + Tag
```

---

# 28. HMAC vs AEAD

| Feature | HMAC | AEAD |
|---|---:|---:|
| Confidentiality | No | Yes |
| Integrity | Yes | Yes |
| Authentication | Yes | Yes |
| Secret key | Yes | Yes |
| Nonce | Usually no | Yes |
| Example | HMAC-SHA-256 | AES-GCM |

---

# 29. CMAC

**CMAC** stands for:

```text
Cipher-based Message Authentication Code
```

It is a MAC construction based on a block cipher.

A common form is:

```text
AES-CMAC
```

Conceptually:

```text
Message
   +
AES Key
   ↓
CMAC
   ↓
Authentication Tag
```

---

# 30. HMAC vs CMAC

| Feature | HMAC | CMAC |
|---|---|---|
| Based on | Hash function | Block cipher |
| Common algorithm | SHA-256 | AES |
| Example | HMAC-SHA-256 | AES-CMAC |
| Secret key | Yes | Yes |
| Purpose | Authentication | Authentication |

Use the construction required by the protocol or security architecture rather than selecting arbitrarily.

---

# 31. GMAC

**GMAC** is the authentication component associated with GCM.

It provides authentication without encrypting plaintext.

Conceptually:

```text
AAD / Data
     +
AES Key
     +
Nonce
     ↓
GMAC
     ↓
Authentication Tag
```

In practice, AES-GCM is usually used when both encryption and authentication are required.

---

# 32. GMAC and GCM

GCM combines:

```text
CTR Encryption
+
GHASH Authentication
```

When GCM is used without plaintext encryption, the authentication function is commonly referred to as:

```text
GMAC
```

---

# 33. MAC Key Separation

Avoid using the same secret key for unrelated cryptographic purposes.

Bad design:

```text
One Key
 ├── Encryption
 ├── MAC
 ├── Password Reset
 └── Token Signing
```

Better:

```text
Master Secret
      ↓
KDF
 ├── Encryption Key
 ├── MAC Key
 ├── Token Key
 └── Other Derived Keys
```

---

# 34. HMAC Key Separation

If multiple services use HMAC:

```text
Service A → Key A
Service B → Key B
Webhook  → Key C
Token    → Key D
```

This limits the impact if one key is compromised.

---

# 35. Webhook Authentication

Webhooks often use HMAC to prove that requests came from an expected sender.

Conceptually:

```text
Webhook Payload
      +
Shared Secret
      ↓
HMAC-SHA-256
      ↓
Signature Header
```

The receiver recalculates the HMAC.

---

# 36. Webhook Verification

Example:

```text
POST /webhook

Body:
{
    "event": "payment.completed"
}

Header:
X-Signature: <HMAC>
```

Server:

```text
Request Body
     +
Webhook Secret
     ↓
HMAC-SHA-256
     ↓
Expected Signature
     ↓
Compare
```

Only accept the request if the signature is valid.

---

# 37. Important Webhook Rule

Always calculate the signature over the exact bytes specified by the provider.

Do not arbitrarily:

```text
Parse JSON
↓
Reformat JSON
↓
Serialize JSON
↓
Hash
```

because different serialization can produce different bytes.

Prefer:

```text
Raw Request Body
        ↓
HMAC
```

when the protocol specifies signing the raw body.

---

# 38. Replay Attacks

A valid MAC does not automatically prevent replay.

Suppose an attacker captures:

```text
Message + Valid MAC
```

They may resend it later.

The MAC remains valid because:

```text
Message
+
Same Key
```

has not changed.

---

# 39. Replay Protection

Protocols can include:

```text
Timestamp
Nonce
Sequence Number
Request ID
Expiration
```

Conceptually:

```text
Message
+
Timestamp
+
Nonce
+
Secret Key
↓
MAC
```

The receiver checks:

```text
MAC Valid?
+
Timestamp Fresh?
+
Nonce Already Used?
```

---

# 40. Webhook Replay Protection

A secure webhook design might include:

```text
timestamp
+
request_id
+
payload
```

and calculate:

```text
HMAC(secret, timestamp || request_id || payload)
```

The server can then reject:

```text
Old timestamps
Repeated request IDs
Invalid signatures
```

The exact construction must follow the provider's documented protocol.

---

# 41. API Request Signing

Some APIs authenticate requests using HMAC.

Conceptually:

```text
HTTP Method
+
Path
+
Timestamp
+
Body
+
Secret
↓
HMAC
↓
Authorization Header
```

This can provide:

```text
Integrity
Authentication
Replay Resistance
```

if the protocol correctly incorporates freshness information.

---

# 42. HMAC-Based API Authentication

Example conceptual request:

```text
POST /api/payment

Timestamp: 1760000000
Request-ID: abc123
Signature: HMAC(...)
```

The server reconstructs the exact signing input.

```text
Method
+
Path
+
Timestamp
+
Request-ID
+
Body
```

Then verifies the signature.

---

# 43. JWT and HMAC

JSON Web Tokens can use symmetric signing algorithms such as:

```text
HS256
HS384
HS512
```

These use HMAC.

For example:

```text
HS256
=
HMAC-SHA-256
```

---

# 44. JWT Symmetric Signing Model

A JWT signed using HS256 conceptually uses:

```text
Header
+
Payload
+
Secret
↓
HMAC-SHA-256
↓
Signature
```

Verification requires the same secret.

Therefore:

```text
Signer
=
Verifier
```

must possess the shared secret.

---

# 45. HMAC JWT vs RSA JWT

### HMAC

```text
HS256
```

uses:

```text
Shared Secret
```

### RSA

```text
RS256
```

uses:

```text
Private Key → Sign
Public Key  → Verify
```

This creates different trust models.

---

# 46. JWT Key Management

With HMAC JWTs:

```text
Every verifier needs the secret.
```

Therefore, compromise of a verifier can potentially allow token forgery.

With asymmetric signatures:

```text
Signer
   ↓
Private Key

Verifier
   ↓
Public Key
```

Verifiers do not need the signing private key.

---

# 47. HMAC in TLS

HMAC has historically played important roles in TLS.

Modern TLS versions often use AEAD constructions for record protection, while HMAC-based functions can still be used in protocol components such as key derivation and transcript processing depending on the TLS version and cipher suite.

---

# 48. HMAC in SSH

HMAC-based algorithms can be used in SSH protocol integrity protection.

Conceptually:

```text
SSH Packet
    +
Session MAC Key
    ↓
MAC
```

The recipient verifies the MAC before accepting the packet.

Modern SSH configurations should use algorithms recommended by current security guidance.

---

# 49. MAC in Network Security

MACs can protect:

```text
Network Messages
Protocol Frames
API Requests
Control Messages
Session Data
```

The exact construction depends on the protocol.

---

# 50. MAC in Distributed Systems

Distributed services may share secrets and authenticate messages using HMAC.

Example:

```text
Service A
    │
    │ Message + HMAC
    ▼
Service B
```

Service B verifies:

```text
Message Integrity
+
Sender Knowledge of Shared Secret
```

---

# 51. HMAC and Microservices

A microservice architecture may use:

```text
Service A
   ↓
Request Signing
   ↓
API Gateway
   ↓
Service B
```

HMAC can be used for request authentication.

However, centralized secret management and key rotation become important at scale.

---

# 52. HMAC and Zero Trust

HMAC can authenticate service-to-service messages where shared secrets are appropriate.

But large-scale Zero Trust systems often favor:

```text
mTLS
Short-Lived Credentials
Certificates
Workload Identity
Public-Key Authentication
```

depending on the environment.

---

# 53. HMAC Key Rotation

A practical system may support:

```text
Key v1
Key v2
```

During rotation:

```text
New Requests → Key v2
Old Requests → Key v1 temporarily accepted
```

After the migration period:

```text
Key v1 → Retired
```

This requires versioning and controlled rollout.

---

# 54. Key Versioning

Include a key identifier when appropriate:

```text
Key-ID: v3
Signature: HMAC(...)
```

The receiver uses:

```text
Key-ID
```

to select the correct key.

This helps during rotation.

---

# 55. HMAC Tag Length

HMAC can produce a tag as large as the underlying hash output.

For example:

```text
HMAC-SHA-256 → 256-bit output
HMAC-SHA-512 → 512-bit output
```

Some protocols truncate tags.

If truncation is used:

```text
Follow the protocol's required tag length.
```

Do not arbitrarily shorten authentication tags.

---

# 56. Truncated MACs

Suppose:

```text
HMAC-SHA-256
```

produces:

```text
256-bit tag
```

A protocol may use only part of it.

For example:

```text
128-bit tag
```

The shorter the tag:

```text
Lower brute-force forgery resistance
```

Therefore tag length must be selected carefully.

---

# 57. MAC Forgery

An attacker attempts to produce:

```text
Message'
+
Valid MAC'
```

without knowing the secret key.

A secure MAC should make successful forgery computationally infeasible.

Conceptually:

```text
Known:
Message
MAC

Goal:
Modified Message
Valid MAC
```

---

# 58. Existential Unforgeability

A formal security goal for MACs is resistance to existential forgery under chosen-message attack.

Conceptually:

```text
Attacker
   │
   │ Can request MACs for chosen messages
   ▼
MAC Oracle
   │
   ▼
Attacker attempts new valid message + MAC
```

A secure MAC should prevent successful forgery except with negligible probability.

---

# 59. Chosen-Message Attack

An attacker may obtain valid MACs for messages they choose.

Example:

```text
M1 → MAC1
M2 → MAC2
M3 → MAC3
```

The attacker attempts:

```text
M4 → Forged MAC
```

A secure MAC should resist this.

---

# 60. MAC and Nonce

Traditional HMAC itself does not require a nonce for basic operation.

However, protocols using MACs may require:

```text
Nonce
Timestamp
Counter
Sequence Number
```

for replay protection.

Therefore:

```text
HMAC ≠ Replay Protection
```

unless freshness is incorporated into the authenticated protocol.

---

# 61. MAC and Confidentiality

A common secure architecture is:

```text
Encrypt
   +
Authenticate
```

Modern applications generally prefer:

```text
AEAD
```

rather than manually combining primitives.

Examples:

```text
AES-GCM
ChaCha20-Poly1305
```

---

# 62. Encrypt-then-MAC

A classical construction is:

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

If using a legacy protocol that requires this construction, follow its exact specification.

For new designs:

```text
Prefer standardized AEAD.
```

---

# 63. MAC-then-Encrypt

Another construction:

```text
Plaintext
    ↓
MAC
    ↓
Plaintext + MAC
    ↓
Encrypt
```

Historical protocols have used this design, but it has led to implementation and protocol vulnerabilities in some contexts.

Do not invent or select cryptographic composition without expert protocol design.

---

# 64. Encrypt-and-MAC

Another design is:

```text
Plaintext
 ├──→ Encrypt
 │
 └──→ MAC
```

This construction can leak information depending on what is authenticated and how outputs are combined.

Again:

```text
Prefer standardized AEAD constructions.
```

---

# 65. AEAD as Modern Alternative

Instead of manually designing:

```text
Encryption
+
MAC
```

use:

```text
AES-GCM
```

or:

```text
ChaCha20-Poly1305
```

where appropriate.

These provide integrated:

```text
Confidentiality
+
Integrity
+
Authentication
```

---

# 66. HMAC and Password Reset Tokens

HMAC can be used to authenticate application-generated tokens.

Conceptually:

```text
User ID
+
Expiration
+
Random Value
   ↓
HMAC Secret
   ↓
Token
```

However, modern applications may instead use:

```text
Random opaque tokens
+
Database lookup
```

or standardized signed-token mechanisms.

Security depends on token generation, expiration, storage, and replay protection.

---

# 67. HMAC-Based File Integrity

A shared secret can protect file integrity:

```text
File
+
Secret Key
↓
HMAC
↓
Tag
```

Anyone without the secret cannot easily generate a valid tag for a modified file.

This differs from a public hash because verification requires the secret.

---

# 68. HMAC vs Hash for File Integrity

### Public verification

Use:

```text
SHA-256
```

when the expected digest is distributed through a trusted channel.

### Shared-secret verification

Use:

```text
HMAC-SHA-256
```

when both parties share a secret.

### Publicly verifiable integrity

Use:

```text
Digital Signature
```

when third parties need verification without access to a shared secret.

---

# 69. HMAC and Logging

HMAC can provide tamper detection for logs.

Conceptually:

```text
Log Entry
    +
Secret Key
    ↓
HMAC
    ↓
Tag
```

However, key protection becomes critical.

If an attacker obtains:

```text
Logs
+
HMAC Key
```

they may be able to forge valid log entries.

---

# 70. HMAC and Audit Trails

A secure audit system can combine:

```text
Hash Chains
+
HMAC
+
Immutable Storage
+
Access Controls
```

to provide stronger tamper-evidence.

No single cryptographic mechanism solves every audit problem.

---

# 71. VAPT Testing – HMAC

During application security testing, examine:

```text
☐ Is HMAC used where authentication is required?
☐ Is the secret sufficiently random?
☐ Is the secret exposed?
☐ Is the correct algorithm used?
☐ Is tag comparison secure?
☐ Is the exact signing input defined?
☐ Is replay protection implemented?
☐ Are timestamps validated?
☐ Are nonces/request IDs unique?
☐ Is key rotation supported?
```

---

# 72. VAPT – Webhook Testing

A webhook assessment may check:

```text
1. Remove signature.
2. Modify payload.
3. Modify timestamp.
4. Replay old request.
5. Change request headers.
6. Change JSON formatting.
7. Change field ordering.
8. Test invalid signature.
9. Test expired timestamp.
10. Test reused request ID.
```

The exact tests must follow the webhook's documented signing protocol.

---

# 73. Example Vulnerability

Suppose an API receives:

```text
POST /transfer
```

with:

```text
amount=1000
signature=...
```

If the server verifies the signature only over:

```text
user_id
```

but not:

```text
amount
```

an attacker may modify:

```text
amount=1000
```

to:

```text
amount=9000
```

without invalidating the signature.

The lesson:

> **Every security-sensitive field must be included in the authenticated message according to the protocol design.**

---

# 74. Canonicalization

Signing structured data introduces a major issue:

```text
Different representations
```

For example:

```json
{"amount":1000,"user":"alice"}
```

and:

```json
{
  "user": "alice",
  "amount": 1000
}
```

may represent equivalent logical data but have different byte sequences.

If signatures are calculated over raw bytes:

```text
Different bytes
→ Different MAC
```

Protocols must define canonicalization or specify exactly which representation is authenticated.

---

# 75. Request Signing

A robust request-signing protocol might define:

```text
HTTP Method
+
Canonical Path
+
Canonical Query
+
Timestamp
+
Nonce
+
Body Hash
```

Then:

```text
Signing String
      +
Secret Key
      ↓
HMAC
```

The exact format should be standardized and unambiguous.

---

# 76. MAC Secret Exposure

If the secret is exposed:

```text
Attacker
   ↓
Obtains MAC Key
   ↓
Can potentially forge messages
```

Therefore:

```text
Key Protection
```

is as important as the MAC algorithm itself.

---

# 77. Secrets in Source Code

Bad:

```python
WEBHOOK_SECRET = "abc123"
```

inside Git.

Problems include:

```text
Git History
Backups
Forks
CI Logs
Developer Machines
Artifact Stores
```

Once committed, a secret may remain in repository history even after deletion.

---

# 78. Secrets in Environment Variables

Environment variables can be better than hard-coding:

```text
WEBHOOK_SECRET
```

but they are not automatically secure.

Consider:

```text
Process Inspection
Logs
Crash Dumps
Container Metadata
CI Systems
```

For higher-security environments, use dedicated secret-management systems.

---

# 79. HMAC in CI/CD

HMAC secrets may be used to:

```text
Authenticate Webhooks
Sign Build Requests
Verify Deployment Events
Protect Automation APIs
```

CI/CD systems should:

```text
Mask Secrets
Restrict Access
Rotate Keys
Avoid Logging Secrets
```

---

# 80. HMAC in Kubernetes

Kubernetes applications may receive HMAC secrets through:

```text
Kubernetes Secrets
External Secret Managers
Cloud KMS
Vault-like Systems
```

However, Kubernetes Secrets are not automatically equivalent to a dedicated secrets-management solution.

Additional controls may be required:

```text
Encryption at Rest
RBAC
Secret Rotation
External Secret Management
Least Privilege
```

---

# 81. HMAC and Kubernetes Webhooks

Admission webhooks or external integrations may authenticate requests using:

```text
TLS
Certificates
HMAC
Service Identity
```

The exact mechanism depends on the implementation.

For security-sensitive integrations:

```text
Authentication
+
Authorization
+
Replay Protection
```

should be considered.

---

# 82. HMAC in SOC Operations

SOC analysts may investigate:

```text
Invalid HMAC
Authentication Failures
Webhook Signature Errors
API Signature Failures
Repeated Request IDs
Replay Attempts
Key Rotation Events
```

Repeated failures can indicate:

```text
Misconfiguration
Expired Key
Credential Exposure
Attack Activity
Replay Attempt
```

---

# 83. Incident Response for MAC-Key Compromise

If a MAC secret is suspected to be compromised:

```text
1. Confirm exposure.
2. Identify affected systems.
3. Rotate the secret.
4. Revoke the old key.
5. Review authenticated requests.
6. Search for forged requests.
7. Review logs.
8. Investigate source of exposure.
9. Deploy new credentials.
10. Document the incident.
```

---

# 84. Key Rotation Strategy

A practical strategy:

```text
Current Key: K2
Previous Key: K1
```

Verification may temporarily support:

```text
K2
+
K1
```

while generation uses:

```text
K2
```

After migration:

```text
K1 → Disabled
```

This avoids abrupt service disruption.

---

# 85. HMAC Algorithm Selection

Recommended modern choices commonly include:

```text
HMAC-SHA-256
HMAC-SHA-384
HMAC-SHA-512
```

Do not use:

```text
HMAC-MD5
```

or:

```text
HMAC-SHA-1
```

for new designs unless a specific legacy protocol requires them and the security implications are understood.

---

# 86. HMAC Security Does Not Depend Only on Hash Collision Resistance

HMAC security has a more nuanced relationship with the underlying hash than simply:

```text
"Hash must have zero collisions."
```

HMAC was specifically designed as a keyed construction and has strong security properties under appropriate assumptions.

Nevertheless:

```text
Use modern hash functions.
```

Avoid deprecated primitives in new designs.

---

# 87. MAC Security Checklist

```text
☐ Use HMAC / CMAC / GMAC as appropriate
☐ Use modern hash functions
☐ Generate strong random keys
☐ Protect MAC keys
☐ Use key separation
☐ Rotate keys
☐ Authenticate all relevant fields
☐ Define canonical input
☐ Use constant-time tag comparison
☐ Add replay protection where needed
☐ Reject invalid tags
☐ Avoid leaking verification details
☐ Use AEAD when confidentiality is also required
```

---

# 88. Common Mistakes

```text
❌ Using a plain hash as authentication
❌ Using SHA256(secret || message) as a custom MAC
❌ Hard-coding HMAC keys
❌ Using weak secrets
❌ Logging HMAC secrets
❌ Comparing tags unsafely
❌ Forgetting replay protection
❌ Signing only part of a security-sensitive request
❌ Failing to define canonical input
❌ Reusing keys across unrelated purposes
❌ Using deprecated MAC algorithms
❌ Inventing a custom cryptographic protocol
```

---

# 89. Secure Webhook Architecture

A strong conceptual design:

```text
                 Webhook Provider
                       │
                       │
                Timestamp
                Request ID
                Payload
                       │
                       ▼
                     HMAC
                       │
                       ▼
                Signature Header
                       │
                       ▼
                Application Server
                       │
            ┌──────────┼──────────┐
            ▼          ▼          ▼
        Verify MAC  Check Time  Check Replay
            │          │          │
            └──────────┼──────────┘
                       ▼
                    Accept
```

---

# 90. Secure API Request Architecture

```text
Client
  │
  │ Method
  │ Path
  │ Timestamp
  │ Nonce
  │ Body
  │ Signature
  ▼
API Gateway
  │
  ├── Verify Timestamp
  ├── Verify Nonce
  ├── Reconstruct Signing Input
  ├── Calculate HMAC
  └── Constant-Time Compare
  │
  ▼
Backend Service
```

---

# 91. MAC + Encryption Architecture

Where both confidentiality and authentication are required:

```text
Plaintext
    │
    ▼
AEAD
    │
    ├── Key
    ├── Nonce
    └── AAD
    │
    ▼
Ciphertext + Authentication Tag
```

This is generally preferable to manually constructing:

```text
Encryption + MAC
```

---

# 92. MAC + Digital Signature Architecture

Some systems may use both:

```text
Digital Signature
+
MAC
```

for different trust boundaries.

For example:

```text
External Message
     ↓
Digital Signature
     ↓
Gateway Authentication
     ↓
Internal HMAC
     ↓
Service-to-Service Authentication
```

Whether this is necessary depends entirely on the system architecture.

---

# 93. Practical Exercise – HMAC Tampering

Create:

```text
message.txt
```

Generate:

```text
HMAC-SHA-256
```

Then:

```text
1. Modify one byte.
2. Recalculate HMAC.
3. Compare tags.
4. Restore original content.
5. Verify again.
```

Expected result:

```text
Original → Valid
Modified → Invalid
Restored → Valid
```

---

# 94. Practical Exercise – Replay Protection

Design a message:

```text
timestamp
nonce
message
```

Calculate:

```text
HMAC(secret, timestamp || nonce || message)
```

Implement validation:

```text
MAC valid?
timestamp fresh?
nonce unused?
```

Only accept if all three conditions succeed.

---

# 95. Practical Exercise – Key Rotation

Implement:

```text
key_v1
key_v2
```

Test:

```text
Messages signed with v1 → accepted during migration
Messages signed with v2 → accepted
New messages → signed using v2
After migration → v1 rejected
```

---

# 96. Practical Exercise – Webhook Verification

Build a small API:

```text
POST /webhook
```

Require:

```text
X-Timestamp
X-Request-ID
X-Signature
```

Calculate:

```text
HMAC-SHA-256
```

over the defined signing input.

Implement:

```text
Signature Verification
Timestamp Validation
Replay Detection
Constant-Time Comparison
```

---

# 97. Interview Questions

## What is a MAC?

A Message Authentication Code is a keyed cryptographic tag used to provide message integrity and authentication.

---

## What does HMAC stand for?

Hash-based Message Authentication Code.

---

## What does HMAC provide?

Primarily:

```text
Integrity
+
Authentication
```

It does not provide confidentiality.

---

## What is the difference between HMAC and hashing?

HMAC uses a secret key, while a normal hash does not.

---

## What is the difference between HMAC and encryption?

HMAC authenticates data but does not hide it. Encryption provides confidentiality.

---

## What is the difference between HMAC and a digital signature?

HMAC uses a shared secret, while digital signatures use a private/public key pair.

---

## Why should HMAC tags be compared carefully?

Naive comparisons can potentially expose timing information. Appropriate constant-time comparison functions should be used.

---

## Does HMAC prevent replay attacks?

No. Replay protection requires additional mechanisms such as timestamps, nonces, counters, or unique request IDs.

---

## Why is `SHA256(secret || message)` not recommended?

Some hash constructions have length-extension properties. HMAC is specifically designed for secure keyed hashing.

---

## What is CMAC?

CMAC is a message authentication code based on a block cipher, commonly AES.

---

## What is GMAC?

GMAC is the authentication-only component associated with GCM.

---

## What is AEAD?

Authenticated Encryption with Associated Data provides encryption, integrity, and authentication in a single standardized construction.

---

## Why is AES-GCM often preferred over AES-CTR + HMAC?

AES-GCM is a standardized AEAD construction that integrates confidentiality and authentication, reducing the risk of incorrect cryptographic composition.

---

# 98. Quick Revision Table

| Concept | Key Idea |
|---|---|
| MAC | Integrity + Authentication |
| HMAC | Hash-based MAC |
| HMAC-SHA-256 | HMAC using SHA-256 |
| HMAC-SHA-512 | HMAC using SHA-512 |
| CMAC | Block-cipher-based MAC |
| GMAC | Authentication component of GCM |
| Tag | MAC output |
| Secret Key | Shared authentication secret |
| Replay Attack | Reusing a previously valid message |
| Nonce | Fresh/unique value used for protocol security |
| Timestamp | Freshness mechanism |
| Constant-Time Comparison | Helps reduce timing leakage |
| AEAD | Encryption + Authentication |
| Digital Signature | Publicly verifiable authentication |
| Key Rotation | Replacing cryptographic keys |

---

# 99. Key Takeaways

```text
1. A MAC provides message integrity and authentication.

2. HMAC is a widely used hash-based MAC construction.

3. HMAC can use SHA-256, SHA-384, or SHA-512.

4. HMAC does not provide confidentiality.

5. A plain hash does not authenticate the sender.

6. HMAC uses a shared secret key.

7. Digital signatures use private/public key pairs and can be publicly verified.

8. MAC tags should be compared using appropriate constant-time mechanisms.

9. HMAC alone does not prevent replay attacks.

10. Replay protection requires timestamps, nonces, counters, or request identifiers.

11. MAC keys must be generated securely and protected.

12. MAC keys should be separated by purpose.

13. HMAC keys should be rotated according to operational requirements.

14. CMAC is a block-cipher-based MAC.

15. GMAC provides authentication associated with GCM.

16. AEAD constructions are generally preferred when both confidentiality and authentication are required.

17. Webhooks and APIs commonly use HMAC-based request authentication.

18. The exact bytes being authenticated must be clearly defined.

19. Structured data requires careful canonicalization or exact serialization rules.

20. Never invent custom cryptographic constructions when standardized primitives are available.
```

---

# 100. Chapter Summary

This chapter covered:

```text
Message Authentication Codes
MAC Security Model
HMAC
HMAC-SHA-256
HMAC-SHA-384
HMAC-SHA-512
CMAC
GMAC
Authentication Tags
HMAC Construction
HMAC Verification
Constant-Time Comparison
Timing Attacks
MAC Key Generation
Key Storage
Key Rotation
Key Separation
Replay Attacks
Replay Protection
Webhook Authentication
API Request Signing
JWT HMAC Signing
HMAC in TLS
HMAC in SSH
Microservice Authentication
Kubernetes Integrations
SOC Monitoring
VAPT Testing
AEAD
```

The central principle is:

> **A MAC proves that a message was generated by someone possessing the shared secret and that the authenticated data has not been modified.**

Remember the distinction:

```text
Hash
  ↓
Integrity Fingerprint

HMAC
  ↓
Integrity + Shared-Secret Authentication

Digital Signature
  ↓
Integrity + Publicly Verifiable Authentication

AEAD
  ↓
Confidentiality + Integrity + Authentication
```

---

# Next Chapter

## Chapter 07 – Digital Signatures & PKI

The next chapter will cover:

```text
Digital Signatures
Signature Generation
Signature Verification
RSA-PSS
ECDSA
Ed25519
Public-Key Infrastructure
PKI
Certificates
Certificate Authorities
Root CAs
Intermediate CAs
Certificate Chains
X.509
CSR
Certificate Validation
Certificate Revocation
CRL
OCSP
Certificate Transparency
TLS Certificates
Code Signing
Email Signing
SSH Authentication
Key Lifecycle
Trust Models
PKI Attacks
Certificate Misconfiguration
VAPT Testing
```

The key question for the next chapter will be:

> **How can someone prove that a message, certificate, software package, or communication endpoint genuinely belongs to a particular trusted identity?**
```