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

# Insecure Deserialization

---

# Overview

Serialization and deserialization are common techniques used to exchange, store, or transmit application data.

Examples include:

- Saving application state
- Session storage
- API communication
- Message queues
- Distributed systems
- Caching
- Object persistence

When applications deserialize **untrusted input** without proper validation, attackers may manipulate serialized data to alter application behavior or, in some implementations, achieve **Remote Code Execution (RCE)**.

---

# What is Serialization?

Serialization converts an object or data structure into a format that can be stored or transmitted.

```
Application Object

↓

Serialization

↓

Byte Stream / JSON / XML

↓

Storage or Network
```

Example object:

```
User

Name: Alice

Role: Customer
```

Serialized JSON:

```json
{
  "name": "Alice",
  "role": "Customer"
}
```

---

# What is Deserialization?

Deserialization reconstructs the original object from serialized data.

```
Serialized Data

↓

Deserializer

↓

Application Object
```

The application can then use the object normally.

---

# Serialization Workflow

```
Application

↓

Object

↓

Serialize

↓

Store / Send

↓

Receive

↓

Deserialize

↓

Application Object
```

This process is safe only when the serialized data is trusted or properly validated.

---

# Common Serialization Formats

| Format | Typical Use Case |
|---------|------------------|
| JSON | REST APIs |
| XML | Enterprise integrations |
| YAML | Configuration files |
| Protocol Buffers | High-performance RPC |
| Avro | Data pipelines |
| MessagePack | Compact binary messaging |
| Binary Serialization | Legacy applications |

Each format has different security considerations.

---

# Safe vs Unsafe Formats

Generally:

```
JSON

↓

Simple Data

↓

Lower Risk
```

```
Binary Object Serialization

↓

Executable Object Graph

↓

Higher Risk
```

The risk depends more on **how data is deserialized** than on the format itself.

---

# Why Deserialization is Dangerous

During deserialization, the runtime may:

- Instantiate objects
- Invoke constructors
- Trigger property setters
- Execute lifecycle callbacks
- Resolve references
- Allocate resources

If these operations occur on attacker-controlled data, unexpected behavior may follow.

---

# Attack Overview

```
Attacker

↓

Crafted Serialized Object

↓

Application

↓

Deserializer

↓

Application Executes Object Logic

↓

Privilege Escalation / RCE / DoS
```

---

# Real-World Scenario

Imagine an application stores user preferences in a serialized cookie.

```
Cookie

↓

Deserialize

↓

Load User Preferences
```

If the cookie is not protected against tampering:

```
Attacker

↓

Modify Serialized Data

↓

Application Accepts Changes

↓

Unexpected Behavior
```

Possible impacts include privilege escalation, unauthorized access, or application crashes.

---

# Java Serialization

Traditional Java serialization uses:

```
Serializable Interface
```

Serialized objects may contain:

- Object graphs
- Nested classes
- References
- Internal state

Historically, unsafe deserialization of untrusted Java objects has led to serious vulnerabilities.

---

# Java Deserialization Flow

```
Serialized Object

↓

ObjectInputStream

↓

Object Reconstruction

↓

Application
```

If untrusted objects are accepted, the application may instantiate unexpected classes or trigger dangerous code paths.

---

# Gadget Chains

## Overview

A gadget chain is a sequence of existing methods that perform unintended actions when combined during deserialization.

```
Object A

↓

Method A

↓

Object B

↓

Method B

↓

Sensitive Operation
```

Attackers do not necessarily inject new code—they abuse existing application or library behavior.

---

# Why Gadget Chains Exist

Large applications often include many third-party libraries.

```
Application

├── Library A
├── Library B
├── Library C
└── Framework
```

A vulnerable chain may span multiple components, making it difficult to identify without careful analysis.

---

# Python Pickle

Python's `pickle` module can serialize arbitrary Python objects.

```
Python Object

↓

pickle.dumps()

↓

Binary Data
```

Later:

```
pickle.loads()

↓

Original Object
```

Because `pickle` can recreate complex objects, it should never be used with untrusted input.

---

# Python Example Workflow

```
User Upload

↓

pickle.loads()

↓

Arbitrary Object Created

↓

Unexpected Behavior
```

Use safer formats such as JSON for untrusted data whenever possible.

---

# .NET BinaryFormatter

Historically, `.NET BinaryFormatter` supported object serialization.

```
Object

↓

BinaryFormatter

↓

Binary Stream
```

Modern guidance discourages its use for untrusted data due to security risks.

Applications should migrate to safer serialization mechanisms.

---

# PHP Object Injection

PHP applications may deserialize objects using functions such as:

```
unserialize()
```

If attacker-controlled input reaches this function without validation:

```
Attacker

↓

Serialized Object

↓

unserialize()

↓

Application
```

Magic methods (such as constructors or destructors) may execute during object lifecycle events, creating opportunities for abuse.

---

# YAML Deserialization

YAML is frequently used for:

- CI/CD pipelines
- Infrastructure as Code
- Configuration management

Unsafe YAML parsers may instantiate arbitrary object types if configured to do so.

Secure parsers should be configured to process only basic data types unless object construction is explicitly required.

---

# XML Deserialization

XML itself is not inherently unsafe.

However, applications that deserialize XML into complex objects without validation may expose additional attack surfaces.

XML processing should also defend against related risks such as XML External Entity (XXE) attacks (covered under a different OWASP category).

---

# JSON Deserialization

JSON generally represents primitive data:

```json
{
  "id": 123,
  "role": "Customer"
}
```

Although JSON is simpler than object serialization, applications must still validate:

- Data types
- Required fields
- Allowed values
- Business rules

Do not assume JSON input is trustworthy.

---

# Deserialization Risks

Improper deserialization may lead to:

- Remote Code Execution (RCE)
- Privilege escalation
- Denial of Service (DoS)
- Business logic manipulation
- Authentication bypass
- Data corruption
- Unexpected object creation
- Resource exhaustion

The exact impact depends on the application's implementation and available code paths.

---

# Unsafe Workflow

```
Receive Request

↓

Deserialize Immediately

↓

Trust Object

↓

Business Logic

↓

Database
```

No validation occurs before processing.

---

# Secure Workflow

```
Receive Request

↓

Validate Format

↓

Validate Schema

↓

Validate Business Rules

↓

Deserialize Safe Types

↓

Application Logic
```

Validation should occur as early as practical.

---

# Signs of Risk During Code Review

Reviewers should pay attention to:

- Deserialization of user-controlled data
- Legacy serialization libraries
- Unrestricted object creation
- Dynamic class loading
- Deserialization inside authentication flows
- Deserialization from cookies or HTTP headers
- Hidden object reconstruction in frameworks

---

# Business Impact

Insecure deserialization has resulted in:

- Enterprise server compromise
- Authentication bypass
- Privilege escalation
- Large-scale Remote Code Execution
- Supply chain compromise
- Complete application takeover

Because deserialization often occurs in trusted application code, successful exploitation can have severe consequences.

---

# Key Takeaways

- Serialization converts objects into transferable or storable formats.
- Deserialization reconstructs objects for application use.
- Deserializing untrusted input without validation can introduce severe security risks.
- Binary object serialization formats generally require greater caution than simple data formats.
- Use schema validation, trusted serializers, and least-privilege design to reduce deserialization risk.
- Prefer simple data formats (such as JSON) for untrusted input when practical, and avoid reconstructing arbitrary object graphs from external data.
