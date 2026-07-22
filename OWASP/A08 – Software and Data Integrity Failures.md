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

# Software Supply Chain Integrity

---

# Overview

Modern applications depend on software produced by many different parties.

A typical enterprise application may include:

- Open-source libraries
- Third-party SDKs
- Container images
- Build tools
- Operating system packages
- Cloud SDKs
- CI/CD pipelines

Every component must be trusted.

A compromise at any point can affect every downstream system.

```
Developer

↓

Source Code

↓

Dependencies

↓

Build Pipeline

↓

Artifact Repository

↓

Deployment

↓

Production
```

This entire path is known as the **software supply chain**.

---

# Trust in Software

Software should never be trusted simply because it exists.

Instead, organizations should verify:

- Who created it
- Whether it has been modified
- Whether it originated from a trusted source
- Whether it is the expected version
- Whether it has been approved for deployment

Trust should always be established through verification rather than assumption.

---

# Software Integrity Verification

```
Software

↓

Checksum

↓

Digital Signature

↓

Publisher Verification

↓

Deployment
```

If any verification step fails, deployment should stop until the issue is investigated.

---

# Hash Functions

## Overview

Hash functions produce a fixed-length digest representing data.

Example:

```
Installer.exe

↓

SHA-256

↓

A94F9E...
```

If the file changes—even by a single byte—the resulting hash changes.

---

# Why Hashes Matter

Imagine downloading software from the internet.

Without verification:

```
Download

↓

Install

↓

Hope It Is Genuine
```

With verification:

```
Download

↓

Calculate Hash

↓

Compare Vendor Hash

↓

Match?

↓

Install
```

A matching hash indicates the file has not been altered since the vendor generated the reference value.

---

# Checksums

A checksum is a value used to detect accidental or unauthorized modifications.

Common algorithms:

- SHA-256
- SHA-384
- SHA-512

Legacy algorithms such as **MD5** and **SHA-1** should not be relied upon for modern integrity verification due to known cryptographic weaknesses.

---

# Digital Signatures

## Overview

Hashes verify integrity, but they do not identify **who created the file**.

Digital signatures provide:

- Integrity
- Authenticity
- Non-repudiation

Signing process:

```
Software

↓

Hash

↓

Sign Hash

↓

Digital Signature
```

Verification process:

```
Software

↓

Hash

↓

Verify Signature

↓

Trusted?
```

---

# Code Signing

Code signing applies a digital signature to software before distribution.

```
Developer

↓

Compile

↓

Sign Binary

↓

Publish

↓

Customer Verifies Signature
```

Benefits include:

- Detecting tampering
- Identifying the publisher
- Building user trust

---

# Signing Certificates

Code signing relies on cryptographic certificates issued by trusted Certificate Authorities (CAs).

```
Certificate Authority

↓

Developer Certificate

↓

Sign Application

↓

Verify Publisher
```

If signing keys are compromised, attackers may produce software that appears legitimate.

Protecting signing keys is therefore critical.

---

# Package Integrity

Package managers often support integrity verification.

Examples include:

```
Python

↓

PyPI
```

```
Node.js

↓

npm
```

```
Java

↓

Maven Central
```

Organizations should:

- Prefer official repositories.
- Verify package authenticity where supported.
- Avoid downloading packages from untrusted mirrors.

---

# Artifact Signing

Artifacts include:

- Executables
- Container images
- Libraries
- Packages
- Archives

Before deployment:

```
Artifact

↓

Verify Signature

↓

Deploy
```

Unsigned or unexpectedly modified artifacts should be investigated before use.

---

# Container Image Integrity

Containers should originate from trusted registries.

Example workflow:

```
Container Image

↓

Scan

↓

Verify Signature

↓

Deploy
```

Organizations should avoid relying on mutable tags such as `latest` in production deployments. Prefer version-pinned or digest-pinned images.

---

# Secure Boot

Secure Boot protects the startup process by ensuring that only trusted boot components execute.

```
Power On

↓

Firmware Verification

↓

Bootloader Verification

↓

Operating System

↓

System Starts
```

This helps prevent unauthorized boot-time malware.

---

# Trusted Platform Module (TPM)

A TPM is a hardware security component that securely stores cryptographic material and measures aspects of the system state.

Common uses include:

- Secure Boot support
- Disk encryption key protection
- Device identity
- Platform attestation

---

# Platform Attestation

Attestation allows one system to verify another system's integrity.

```
System

↓

Measurements

↓

Attestation

↓

Verifier

↓

Trusted?
```

This is commonly used in cloud computing and zero-trust environments.

---

# Sigstore

Sigstore is an open-source ecosystem for signing and verifying software artifacts.

Its goals include:

- Simplifying artifact signing
- Improving transparency
- Supporting modern software supply chains

Developers can verify that an artifact was produced by the expected identity and has not been modified.

---

# Cosign

Cosign is a popular tool within the Sigstore ecosystem for signing and verifying container images and other artifacts.

Example workflow:

```
Container Image

↓

Sign

↓

Registry

↓

Verify Before Deployment
```

Integrating verification into CI/CD pipelines helps prevent unauthorized artifacts from reaching production.

---

# SLSA (Supply-chain Levels for Software Artifacts)

SLSA is a security framework designed to strengthen software build integrity.

It provides guidance for:

- Secure build systems
- Provenance generation
- Artifact integrity
- Build isolation
- Tamper resistance

Higher SLSA levels generally provide stronger assurances about the software build process.

---

# Build Provenance

Build provenance records how software was produced.

Typical information includes:

- Source repository
- Commit identifier
- Build system
- Build configuration
- Build timestamp
- Builder identity

Example:

```
Source Code

↓

Build Server

↓

Signed Provenance

↓

Artifact
```

This information helps organizations verify that an artifact originated from an expected build process.

---

# in-toto Attestations

in-toto is a framework for recording and verifying each step of the software supply chain.

Example:

```
Developer

↓

Source Commit

↓

Build

↓

Test

↓

Package

↓

Deploy
```

Each stage produces signed metadata, allowing consumers to verify that required steps were completed and were not tampered with.

---

# Reproducible Builds

A reproducible build produces identical outputs when built from the same source code and environment.

```
Source Code

↓

Build A

↓

Artifact X
```

```
Same Source

↓

Build B

↓

Artifact X
```

Matching outputs increase confidence that the build process has not introduced unauthorized changes.

---

# Secure Update Mechanisms

Applications should verify updates before installation.

```
Update Available

↓

Download

↓

Verify Signature

↓

Verify Version

↓

Install
```

Applications should reject updates that fail verification.

---

# Real-World Case Studies

## SolarWinds (2020)

Attackers compromised the software build process.

```
Build Server

↓

Malicious Build

↓

Signed Update

↓

Thousands of Customers
```

This incident demonstrated that trusted software updates can become large-scale attack vectors when build integrity is compromised.

---

## XZ Utils (2024)

Attackers gradually gained influence within an open-source project and introduced a backdoor into a widely used compression library.

The incident highlighted the importance of maintainer trust, code review, and independent verification throughout the supply chain.

---

## Codecov (2021)

Attackers modified the Codecov Bash uploader.

Result:

```
CI/CD

↓

Environment Variables

↓

Credentials Exposed
```

This showed how compromising development tooling can impact many organizations simultaneously.

---

## NotPetya via MeDoc (2017)

Attackers compromised the update mechanism of the MeDoc accounting software.

```
Trusted Update

↓

Malicious Payload

↓

Organization Compromise
```

The attack spread rapidly across organizations and caused widespread operational disruption.

---

# Enterprise Supply Chain Security Principles

A mature software supply chain should include:

- Trusted repositories
- Dependency governance
- Artifact signing
- Build provenance
- Secure CI/CD
- Continuous vulnerability scanning
- SBOM generation
- Cryptographic verification
- Separation of duties
- Change management

---

# Key Takeaways

- Software integrity depends on verifying both the origin and integrity of every component.
- Hashes detect modification, while digital signatures also verify authenticity.
- Code signing, artifact signing, and secure update mechanisms reduce the risk of tampered software reaching production.
- Frameworks and technologies such as Sigstore, Cosign, SLSA, in-toto, Secure Boot, and TPM strengthen software supply chain security.
- Real-world incidents such as SolarWinds, XZ Utils, Codecov, and NotPetya demonstrate that attacks on trusted software distribution channels can have global consequences.

# Detection

Software and Data Integrity Failures are often difficult to detect because attackers abuse
trusted processes rather than exploiting traditional application vulnerabilities.

Instead of attacking production servers directly, they target:

- Source code repositories
- CI/CD pipelines
- Build systems
- Dependency repositories
- Software update mechanisms
- Artifact repositories
- Signing infrastructure

Early detection requires visibility across the entire Software Development Lifecycle (SDLC).

---

# Detection Architecture

```
             Source Code
                  │
                  ▼
         Source Repository Scan
                  │
                  ▼
        Dependency Verification
                  │
                  ▼
        Build Pipeline Security
                  │
                  ▼
       Artifact Integrity Check
                  │
                  ▼
     Container Image Verification
                  │
                  ▼
        Production Monitoring
                  │
                  ▼
         Continuous Auditing
```

Every stage should include integrity verification and security monitoring.

---

# What Should Be Monitored?

Organizations should continuously monitor:

## Source Code

- Unauthorized commits
- Suspicious pull requests
- Force pushes
- Branch protection bypasses
- Unexpected contributor activity

---

## Dependencies

Monitor for:

- New CVEs
- Malicious packages
- Package ownership changes
- Unexpected dependency updates
- Dependency confusion attempts
- Typosquatting packages

---

## CI/CD Pipeline

Monitor:

- Pipeline configuration changes
- New secrets
- Build failures
- Build script modifications
- Unauthorized workflow execution
- Unexpected artifacts

---

## Build Systems

Review:

- Compiler versions
- Build environment
- Build scripts
- Build logs
- Generated binaries
- Build provenance

Unexpected differences may indicate compromise.

---

## Artifact Repository

Verify:

- Digital signatures
- Checksums
- Publisher identity
- Version consistency
- Upload history

Artifacts should never be trusted solely because they exist in a repository.

---

## Container Images

Monitor:

- Base image updates
- Image signatures
- Image digests
- Vulnerability scan results
- Registry activity

---

## Production Systems

Look for:

- Unexpected binaries
- Unauthorized configuration changes
- Unsigned software
- Integrity verification failures
- Unexpected software versions

---

# Integrity Monitoring Workflow

```
Software Created

↓

Sign Artifact

↓

Publish

↓

Verify Signature

↓

Deploy

↓

Monitor Integrity

↓

Alert on Modification
```

Continuous verification is more effective than one-time validation.

---

# Detection Tools

| Tool | Purpose |
|------|----------|
| OWASP Dependency-Check | Dependency vulnerability detection |
| Trivy | Containers, filesystems, repositories, IaC scanning |
| Grype | Vulnerability scanning |
| Syft | SBOM generation |
| osv-scanner | Open Source Vulnerability database scanning |
| GitHub Dependabot | Dependency monitoring |
| GitHub Code Scanning | Static analysis |
| Cosign | Artifact signing & verification |
| Sigstore | Software signing ecosystem |
| in-toto | Supply chain attestation |
| OpenSSF Scorecard | Repository security assessment |

---

# Prevention

The best defense is to establish trust at every stage of software development.

---

# Secure Software Development Lifecycle (SSDLC)

Security should be integrated throughout development.

```
Requirements

↓

Design

↓

Development

↓

Testing

↓

Build

↓

Deployment

↓

Monitoring
```

Integrity verification belongs at every phase.

---

# Secure CI/CD

Protect:

- Build servers
- Secrets
- Signing keys
- Pipeline definitions
- Artifact repositories

Recommendations:

- Require MFA for pipeline administrators.
- Separate development and production pipelines.
- Use ephemeral build runners where practical.
- Limit permissions using least privilege.
- Audit all pipeline changes.

---

# Secure Source Code Management

Implement:

- Branch protection
- Mandatory code reviews
- Signed commits (where supported)
- MFA for repository access
- Protected release branches
- Secret scanning
- Commit history auditing

---

# Secure Dependency Management

Organizations should:

- Approve new dependencies.
- Remove unused packages.
- Pin dependency versions.
- Continuously monitor CVEs.
- Maintain Software Bills of Materials (SBOMs).
- Prefer trusted package repositories.

---

# Secure Build Systems

Every build should be:

- Repeatable
- Auditable
- Isolated
- Logged
- Verifiable

Avoid:

- Manual production builds
- Shared build accounts
- Unsigned artifacts
- Untrusted plugins

---

# Artifact Protection

Before deployment:

```
Artifact

↓

Verify Publisher

↓

Verify Signature

↓

Verify Checksum

↓

Deploy
```

Reject artifacts that fail any verification step.

---

# Secure Update Mechanisms

Software updates should:

- Use HTTPS
- Be digitally signed
- Verify signatures before installation
- Prevent downgrade attacks
- Validate version numbers

Never install unsigned updates automatically.

---

# Data Integrity Protection

Protect critical data using:

- Input validation
- Digital signatures (where appropriate)
- Cryptographic hashes
- Database integrity controls
- Secure transport (TLS)

---

# Enterprise Best Practices

✔ Verify every software artifact before deployment.

✔ Use cryptographic signatures.

✔ Protect signing keys using secure key management.

✔ Maintain SBOMs for all production applications.

✔ Continuously monitor dependency vulnerabilities.

✔ Protect CI/CD infrastructure.

✔ Enforce MFA for source code repositories.

✔ Generate build provenance.

✔ Implement reproducible builds where feasible.

✔ Perform regular security reviews of the software supply chain.

✔ Audit third-party software providers.

✔ Maintain incident response procedures for supply chain compromises.

---

# Practical Lab

## Objective

Evaluate the integrity of a software delivery pipeline.

---

## Scenario

Application Components:

- Git repository
- GitHub Actions
- Docker
- Kubernetes
- Python
- PostgreSQL

---

## Tasks

1. Generate an SBOM.
2. Scan dependencies.
3. Verify container image signatures.
4. Review CI/CD permissions.
5. Identify unsigned artifacts.
6. Verify build provenance.
7. Review repository security settings.
8. Recommend improvements.

---

## Expected Learning Outcomes

After completing this lab, you should be able to:

- Assess software supply chain security.
- Verify artifact integrity.
- Identify insecure build practices.
- Recommend improvements to CI/CD security.
- Understand modern integrity verification workflows.

---

# Interview Questions

## Beginner

### What is software integrity?

Software integrity ensures that software has not been modified without authorization and originates from a trusted source.

---

### What is a digital signature?

A digital signature uses asymmetric cryptography to verify both the integrity and authenticity of software or data.

---

### What is code signing?

Code signing is the process of digitally signing executables or software packages so users and systems can verify the publisher and detect tampering.

---

## Intermediate

### Why are hashes alone insufficient for software verification?

Hashes detect whether data has changed but do not identify who created the software. Digital signatures combine integrity verification with publisher authentication.

---

### What is build provenance?

Build provenance records how, where, and from which source code an artifact was produced, helping verify that it came from an expected and trusted build process.

---

### Why is SBOM important?

An SBOM provides a complete inventory of software components, enabling organizations to quickly identify applications affected by newly disclosed vulnerabilities and improve supply chain visibility.

---

## Advanced

### How would you secure an enterprise CI/CD pipeline?

A secure CI/CD pipeline should include:

1. MFA for administrators.
2. Least-privilege access.
3. Isolated build environments.
4. Secret management.
5. Artifact signing.
6. Build provenance.
7. Dependency scanning.
8. Container image scanning.
9. Policy enforcement before deployment.
10. Continuous monitoring and auditing.

---

### How would you respond to a suspected software supply chain compromise?

A structured response includes:

1. Identify affected repositories, pipelines, and artifacts.
2. Stop deployments involving potentially compromised artifacts.
3. Verify signatures, hashes, and build provenance.
4. Rotate credentials and signing keys if compromise is suspected.
5. Rebuild artifacts from trusted source code.
6. Review logs for unauthorized changes.
7. Notify stakeholders and affected customers if required.
8. Conduct a post-incident review and strengthen controls.

---

# References

## OWASP

- OWASP Top 10 (2021)
- OWASP Software Supply Chain Security Guidance
- OWASP Dependency-Check

## NIST

- NIST Secure Software Development Framework (SSDF)
- NIST Cybersecurity Framework (CSF)
- NIST SP 800-53

## CISA

- Secure by Design
- Secure by Demand
- Software Supply Chain Guidance

## OpenSSF

- OpenSSF Scorecard
- OpenSSF Best Practices

## Supply Chain Security

- Sigstore
- Cosign
- in-toto
- SLSA
- SPDX
- CycloneDX

---

# Summary

Software and Data Integrity Failures arise when organizations place implicit trust in software, data, or build processes without verifying their authenticity and integrity. Modern applications rely heavily on complex software supply chains, making secure development practices, artifact signing, dependency governance, SBOM generation, and protected CI/CD pipelines essential.

A mature integrity program verifies every stage of the software lifecycle—from source code to deployment—using cryptographic signatures, build provenance, continuous monitoring, and controlled release processes. By integrating these controls into the Secure Software Development Lifecycle (SSDLC), organizations can significantly reduce the risk of software supply chain attacks and unauthorized modifications.