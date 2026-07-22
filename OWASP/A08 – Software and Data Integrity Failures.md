# A08:2021 – Software and Data Integrity Failures

---

# Overview

Software and Data Integrity Failures occur when an application cannot verify that:

- Software has not been modified.
- Updates are authentic.
- Dependencies are trusted.
- Build artifacts are genuine.
- Data originates from a trusted source.

Unlike many OWASP categories that focus on application vulnerabilities, **A08 focuses on trust**.

The fundamental security question is:

> **"Can I trust this software or data?"**

If the answer is **No**, attackers may execute arbitrary code, inject malicious updates, compromise CI/CD pipelines, or manipulate application behavior without exploiting traditional vulnerabilities.

---

# Why It Matters

Modern applications are built from numerous components:

```
Developer
      │
      ▼
Source Code
      │
      ▼
Dependencies
      │
      ▼
CI/CD Pipeline
      │
      ▼
Container Images
      │
      ▼
Cloud Infrastructure
      │
      ▼
Production
```

Every stage must preserve integrity.

A compromise anywhere in this chain can affect every deployed application.

---

# What is Integrity?

Integrity is one of the three pillars of the CIA Triad.

```
CIA

├── Confidentiality
├── Integrity
└── Availability
```

Integrity ensures that information and software remain:

- Accurate
- Complete
- Authentic
- Unmodified
- Trustworthy

---

# Integrity vs Confidentiality

| Confidentiality | Integrity |
|-----------------|-----------|
| Prevents unauthorized disclosure | Prevents unauthorized modification |
| Encryption | Hashes, signatures, verification |
| Focuses on secrecy | Focuses on correctness |

Example:

Encrypted malware is still malware.

Confidentiality alone does not guarantee integrity.

---

# Trust Chain

Software passes through multiple trusted entities before reaching production.

```
Developer

↓

Git Repository

↓

CI/CD

↓

Build Server

↓

Artifact Repository

↓

Deployment

↓

Production
```

Breaking trust at any point compromises downstream systems.

---

# Integrity Architecture

```
          Developer
               │
               ▼
        Source Repository
               │
               ▼
      Dependency Resolution
               │
               ▼
          Build Process
               │
               ▼
        Security Verification
               │
               ▼
         Artifact Signing
               │
               ▼
      Artifact Repository
               │
               ▼
        Production Release
```

Each transition should include integrity verification.

---

# Types of Integrity Failures

```
Software Integrity Failures

├── Insecure Updates
├── Insecure CI/CD
├── Unsigned Code
├── Compromised Dependencies
├── Malicious Build Artifacts
├── Insecure Deserialization
├── Tampered Packages
├── Configuration Tampering
├── Unverified Plugins
└── Data Integrity Violations
```

---

# Root Causes

Common causes include:

- Missing signature verification
- Blind trust in third-party packages
- Insecure CI/CD pipelines
- Weak update mechanisms
- Unverified software downloads
- Lack of checksum validation
- Poor access control on build systems
- Unsafe deserialization
- Supply chain compromise

---

# Real-World Example

Imagine an organization downloads software updates automatically.

```
Vendor

↓

Software Update

↓

Production Servers
```

If attackers compromise the update server:

```
Attacker

↓

Malicious Update

↓

Trusted Deployment

↓

Thousands of Servers Compromised
```

No application vulnerability is required.

The trusted update mechanism itself becomes the attack vector.

---

# Software Supply Chain

Modern applications rely on thousands of external components.

```
Application

│

├── Framework
├── Libraries
├── Container Images
├── Build Tools
├── Operating System
├── Cloud SDKs
└── APIs
```

Every dependency increases the trusted computing base.

---

# Trusted vs Untrusted Components

```
Trusted?

↓

Official Repository

↓

Verified Signature

↓

Approved Version

↓

Deploy
```

```
Unknown Repository

↓

Unknown Maintainer

↓

No Signature

↓

Reject
```

Organizations should define clear trust policies before introducing new software.

---

# Data Integrity

Integrity is not limited to software.

Applications also process:

- Configuration files
- API responses
- User uploads
- Database records
- Cloud metadata
- Serialized objects

These inputs must be validated before use.

---

# Data Flow Integrity

```
Client

↓

Application

↓

Validation

↓

Business Logic

↓

Database
```

Skipping validation allows malicious or corrupted data to influence application behavior.

---

# Configuration Integrity

Configuration files influence application behavior.

Examples:

```
config.yml

.env

settings.json

docker-compose.yml

application.properties
```

Attackers modifying configuration may:

- Disable security features
- Change authentication methods
- Redirect traffic
- Leak secrets
- Enable debug functionality

Configuration files should be protected with appropriate permissions and change controls.

---

# Build Integrity

Every software build should be reproducible and verifiable.

```
Source Code

↓

Compiler

↓

Binary

↓

Checksum

↓

Digital Signature
```

Unexpected differences between builds should be investigated.

---

# Artifact Integrity

Artifacts include:

- Executables
- Libraries
- Containers
- Packages
- Installers

Before deployment, verify:

- Origin
- Checksum
- Digital signature
- Version
- Publisher

---

# Integrity Verification Methods

Common verification mechanisms include:

```
Integrity Verification

├── SHA-256 Checksums
├── Digital Signatures
├── Code Signing Certificates
├── Package Signatures
├── Secure Boot
├── TPM Measurements
└── Artifact Attestations
```

Using multiple verification mechanisms provides stronger assurance than relying on a single control.

---

# Business Impact

Integrity failures may lead to:

- Remote Code Execution (RCE)
- Software supply chain compromise
- Credential theft
- Malware distribution
- Unauthorized system modifications
- Financial losses
- Regulatory violations
- Loss of customer trust
- Large-scale enterprise compromise

---

# Key Takeaways

- Integrity ensures software and data remain authentic and unmodified.
- Every stage of the software supply chain must preserve trust.
- Trust should never be assumed; it should be verified through checksums, digital signatures, and controlled build processes.
- Software, configuration, dependencies, and data all require integrity protection.
- Weak integrity controls can enable large-scale compromises without exploiting traditional application vulnerabilities.