# 26-Software-and-Data-Integrity-Failures.md

# Part 1 — Fundamentals of Software & Data Integrity, Trust, Supply Chain Security, and Enterprise Overview

> **"Integrity means ensuring that software, data, and systems remain accurate, complete, authentic, and unmodified unless an authorized change has occurred."**

---

# Learning Objectives

After completing this part, you will understand:

- OWASP A08:2021 Overview
- Software Integrity
- Data Integrity
- Trust Relationships
- Software Supply Chain
- Trusted Components
- Integrity Verification
- Digital Signatures
- Checksums and Hashes
- Enterprise Integrity Architecture

---

# What are Software and Data Integrity Failures?

Software and Data Integrity Failures occur when applications fail to verify that software, updates, configuration, or data have remained authentic and unaltered throughout their lifecycle.

These failures may result in:

- Unauthorized software modification
- Deployment of untrusted code
- Data corruption
- Supply chain compromise
- Loss of customer trust
- Business disruption

Integrity protects systems against unauthorized or unintended modification.

---

# CIA Triad Review

```
Cybersecurity

│

├── Confidentiality

├── Integrity

└── Availability
```

Integrity ensures information remains accurate and trustworthy.

---

# What is Integrity?

Integrity means information has not been altered without authorization.

```
Original Data

↓

Authorized Storage

↓

Integrity Verification

↓

Trusted Data
```

Users and systems should be able to trust that data remains unchanged unless legitimate modifications occur.

---

# Software Integrity

Software integrity ensures applications execute exactly as intended.

```
Source Code

↓

Build

↓

Package

↓

Deployment

↓

Execution
```

Every stage should preserve software authenticity.

---

# Data Integrity

Data integrity ensures stored and transmitted information remains complete and accurate.

```
Create Data

↓

Store

↓

Transfer

↓

Retrieve

↓

Verify Integrity
```

Integrity should be maintained throughout the data lifecycle.

---

# Integrity vs Confidentiality

| Confidentiality | Integrity |
|-----------------|-----------|
| Prevents unauthorized disclosure | Prevents unauthorized modification |
| Focuses on secrecy | Focuses on correctness |
| Encryption is common | Validation and verification are common |
| Protects information from being read | Protects information from being altered |

Both properties are essential for secure systems.

---

# Why Integrity Matters

```
Without Integrity

↓

Incorrect Decisions

↓

Business Impact

↓

Financial Loss

↓

Loss of Trust
```

Organizations rely on accurate software and trustworthy data to operate safely.

---

# Software Supply Chain

Modern applications depend on numerous components.

```
Application

│

├── Source Code

├── Framework

├── Libraries

├── Build Tools

├── Container Image

├── Operating System

└── Cloud Services
```

Each component contributes to the application's overall integrity.

---

# Enterprise Software Supply Chain

```
Developer

↓

Source Repository

↓

Build Pipeline

↓

Artifact Repository

↓

Deployment

↓

Production
```

Integrity checks should exist throughout the entire supply chain.

---

# Trust Relationships

Applications depend on trusted relationships.

```
Organization

↓

Trusted Vendor

↓

Trusted Component

↓

Application

↓

Business Service
```

Trust should be established deliberately and reviewed periodically.

---

# Chain of Trust

```
Trusted Developer

↓

Source Code

↓

Build System

↓

Signed Artifact

↓

Deployment

↓

Production
```

Breaking any link weakens overall integrity.

---

# Trusted Components

Organizations should evaluate software components before adoption.

```
Component Review

│

├── Vendor Reputation

├── Maintenance

├── Security History

├── Compatibility

├── Licensing

└── Support Status
```

Component selection should consider both functionality and security.

---

# Integrity Verification

Integrity verification confirms that software or data has not changed unexpectedly.

```
Object

↓

Integrity Verification

↓

Match?

↓

Trusted

OR

Investigate
```

Verification should occur before software is executed or sensitive data is relied upon.

---

# Checksums

A checksum is a calculated value used to detect accidental or unauthorized changes.

```
File

↓

Checksum Calculation

↓

Reference Value

↓

Compare

↓

Integrity Status
```

Checksums help identify whether files remain unchanged.

---

# Cryptographic Hashes

Hash functions generate a fixed-length representation of data.

```
Input Data

↓

Hash Function

↓

Hash Value
```

If the data changes, the resulting hash value also changes.

Hashes are commonly used for integrity verification rather than confidentiality.

---

# Digital Signatures

Digital signatures help verify:

- Authenticity
- Integrity
- Origin

```
Software Package

↓

Digital Signature

↓

Verification

↓

Trusted Distribution
```

Digital signatures help establish confidence that software originates from an expected publisher and has not been modified.

---

# Checksums vs Digital Signatures

| Checksums | Digital Signatures |
|-----------|--------------------|
| Detect changes | Verify changes and publisher authenticity |
| Focus on integrity | Support integrity and authenticity |
| Simple comparison | Cryptographic verification |
| Often published separately | Created using signing keys |

---

# Data Integrity Lifecycle

```
Create

↓

Validate

↓

Store

↓

Transfer

↓

Verify

↓

Use

↓

Archive
```

Integrity controls should exist throughout the lifecycle.

---

# Enterprise Integrity Architecture

```
Developer

↓

Version Control

↓

CI Pipeline

↓

Artifact Repository

↓

Integrity Verification

↓

Production
```

Verification should occur before deployment into production.

---

# Enterprise Example

A financial organization develops an online banking platform.

```
Developer

↓

Source Repository

↓

Build

↓

Integrity Verification

↓

Artifact Repository

↓

Deployment

↓

Online Banking
```

Every software release undergoes integrity validation before deployment.

---

# Common Integrity Risks

| Risk | Potential Impact |
|------|------------------|
| Untrusted software | Unauthorized code execution |
| Modified configuration | Operational instability |
| Corrupted data | Incorrect business decisions |
| Weak verification | Reduced confidence in software authenticity |
| Missing integrity checks | Increased supply chain risk |
| Poor governance | Inconsistent deployment practices |

---

# Enterprise Integrity Workflow

```
Source Code

↓

Review

↓

Build

↓

Integrity Verification

↓

Artifact Repository

↓

Deployment

↓

Continuous Monitoring
```

Integrity should be maintained throughout development and operations.

---

# Hands-on Lab (Conceptual)

1. Draw the software supply chain for a sample application.
2. Identify where integrity verification should occur.
3. List trusted and untrusted software sources.
4. Document how integrity should be maintained during deployment.
5. Design a conceptual integrity verification workflow.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is software integrity?
2. What is data integrity?
3. Why is integrity important in cybersecurity?
4. How does integrity differ from confidentiality?
5. What is a software supply chain?
6. What is a checksum?
7. What is a cryptographic hash?
8. What is a digital signature?
9. Why should organizations verify software integrity?
10. Why is trust important in software deployment?

---

# Best Practices

- Verify software before deployment.
- Use trusted software sources and approved repositories.
- Validate the integrity of critical data throughout its lifecycle.
- Maintain documented trust relationships.
- Review software supply chain processes regularly.
- Apply integrity verification at multiple stages of development and deployment.
- Continuously monitor production environments for unauthorized changes.

---

# Common Mistakes

- Trusting software without verification.
- Ignoring integrity validation during deployments.
- Using unapproved software sources.
- Failing to verify important configuration files.
- Assuming downloaded software is automatically trustworthy.
- Neglecting integrity checks in automated pipelines.

---

# Key Takeaways

- Integrity ensures software and data remain authentic, accurate, and unmodified without authorization.
- Modern applications depend on trusted software supply chains.
- Checksums, cryptographic hashes, and digital signatures support integrity verification.
- Trust relationships should be carefully established and periodically reviewed.
- Integrity verification should occur throughout the software development and deployment lifecycle.

# 26-Software-and-Data-Integrity-Failures.md

# Part 2 — Code Signing, Digital Signatures, Secure Build Pipelines, CI/CD Integrity, Artifact Repositories, and Supply Chain Security

> **"A secure build pipeline ensures that only trusted source code becomes trusted software. Every stage—from source control to production—must preserve integrity."**

---

# Learning Objectives

After completing this part, you will understand:

- Code Signing
- Digital Signature Lifecycle
- Secure Build Pipelines
- CI/CD Integrity
- Artifact Repositories
- Build Provenance
- Trusted Build Systems
- Supply Chain Verification
- Release Integrity
- Enterprise Deployment Security

---

# Secure Software Development Lifecycle (SSDLC)

Integrity begins long before deployment.

```
Requirements

↓

Design

↓

Development

↓

Code Review

↓

Build

↓

Testing

↓

Deployment

↓

Monitoring
```

Each phase should include integrity controls.

---

# Why Build Integrity Matters

Without build integrity:

```
Source Code

↓

Unverified Build

↓

Untrusted Software

↓

Production Risk
```

With build integrity:

```
Source Code

↓

Verified Build

↓

Trusted Artifact

↓

Secure Deployment
```

---

# Secure Build Pipeline

A secure build pipeline transforms reviewed source code into deployable software.

```
Developer

↓

Version Control

↓

Code Review

↓

CI Build

↓

Security Checks

↓

Artifact

↓

Deployment
```

Integrity should be maintained throughout the pipeline.

---

# Enterprise Build Workflow

```
Developer

↓

Source Repository

↓

Automated Build

↓

Testing

↓

Integrity Verification

↓

Artifact Repository

↓

Production
```

Automation improves consistency while reducing manual errors.

---

# Code Signing

Code signing provides assurance that software originates from a trusted publisher and has not been altered after signing.

```
Software

↓

Signing Process

↓

Digital Signature

↓

Distribution
```

Recipients can verify the authenticity of the software before installation or execution.

---

# Benefits of Code Signing

```
Code Signing

│

├── Publisher Verification

├── Integrity Protection

├── Trusted Distribution

├── Tamper Detection

└── Improved User Confidence
```

---

# Digital Signature Lifecycle

```
Software Created

↓

Code Review

↓

Build

↓

Digital Signing

↓

Distribution

↓

Signature Verification

↓

Execution
```

Verification should occur before software is trusted.

---

# Integrity Verification During Deployment

```
Artifact

↓

Verify Signature

↓

Verify Integrity

↓

Deployment Approval

↓

Production
```

Deployment should only proceed after successful verification.

---

# Build Provenance

Build provenance records how software was produced.

```
Build Provenance

│

├── Source Repository

├── Commit Reference

├── Build System

├── Build Time

├── Builder Identity

├── Dependencies

└── Artifact Version
```

This information improves traceability and incident response.

---

# Reproducible Builds

A reproducible build aims to produce identical outputs when the same source code and build process are used.

```
Source Code

↓

Controlled Build

↓

Artifact

↓

Repeat Build

↓

Equivalent Artifact
```

Reproducibility helps verify build consistency.

---

# CI/CD Pipeline Integrity

Continuous Integration and Continuous Deployment (CI/CD) pipelines should include integrity verification.

```
Developer

↓

Commit

↓

CI Pipeline

↓

Security Validation

↓

Artifact

↓

Approval

↓

Production
```

Security validation should be integrated into the pipeline rather than performed only at the end.

---

# CI/CD Security Controls

```
CI/CD Controls

│

├── Branch Protection

├── Code Review

├── Automated Testing

├── Dependency Review

├── Build Verification

├── Secret Protection

├── Artifact Signing

└── Audit Logging
```

Each control contributes to overall software integrity.

---

# Artifact Repository

An artifact repository stores verified build outputs.

```
Build

↓

Verified Artifact

↓

Artifact Repository

↓

Deployment
```

Repositories improve consistency and support controlled software releases.

---

# Benefits of Artifact Repositories

| Benefit | Description |
|----------|-------------|
| Central Storage | Single location for approved artifacts |
| Version Control | Track released builds |
| Controlled Distribution | Prevent unauthorized releases |
| Audit Support | Improve traceability |
| Repeatable Deployments | Promote consistency |

---

# Release Approval Workflow

```
Build Complete

↓

Testing

↓

Integrity Verification

↓

Release Approval

↓

Production Deployment
```

Formal approval reduces deployment risk.

---

# Supply Chain Verification

Organizations should verify multiple aspects of software before deployment.

```
Software Package

│

├── Source

├── Version

├── Signature

├── Integrity

├── Dependencies

└── Approval Status
```

Verification should be part of every release process.

---

# Trusted Build Infrastructure

```
Build Infrastructure

│

├── Version Control

├── Build Servers

├── Security Controls

├── Access Control

├── Logging

└── Monitoring
```

Build infrastructure should receive the same level of protection as production systems.

---

# Configuration Integrity

Integrity also applies to configuration.

```
Configuration

↓

Version Control

↓

Review

↓

Approval

↓

Deployment
```

Unauthorized configuration changes can significantly affect application security.

---

# Enterprise Deployment Architecture

```
Developer

↓

Version Control

↓

CI Pipeline

↓

Security Validation

↓

Artifact Repository

↓

Deployment Platform

↓

Production Environment
```

Every transition should preserve integrity.

---

# Enterprise Example

A global e-commerce organization deploys applications using the following workflow:

```
Developer

↓

Source Repository

↓

Peer Review

↓

Automated Build

↓

Automated Testing

↓

Artifact Signing

↓

Artifact Repository

↓

Deployment Approval

↓

Production
```

Every production release is reviewed, verified, and traceable.

---

# Common Build Integrity Risks

| Risk | Potential Impact |
|------|------------------|
| Unauthorized code changes | Untrusted software |
| Missing code review | Reduced software quality |
| Weak pipeline security | Increased supply chain risk |
| Unverified artifacts | Deployment of untrusted software |
| Poor version control | Reduced traceability |
| Inadequate audit logging | Difficult investigations |

---

# Enterprise Integrity Workflow

```
Source Code

↓

Review

↓

Build

↓

Testing

↓

Signing

↓

Artifact Repository

↓

Verification

↓

Deployment
```

---

# Hands-on Lab (Conceptual)

1. Draw a secure CI/CD pipeline for a sample application.
2. Identify where integrity verification should occur.
3. Document where code signing fits into the release lifecycle.
4. List the metadata that should be recorded for build provenance.
5. Design an approval workflow before production deployment.

> Perform all assessments only in environments where you have explicit authorization.

---

# Interview Questions

1. What is code signing?
2. Why are digital signatures important?
3. What is build provenance?
4. Why are reproducible builds valuable?
5. What is an artifact repository?
6. Why should CI/CD pipelines include integrity verification?
7. What security controls protect build infrastructure?
8. Why is configuration integrity important?
9. Why should releases require formal approval?
10. How does build integrity improve software security?

---

# Best Practices

- Protect build infrastructure with strong access controls.
- Require peer review before merging production code.
- Verify software integrity before deployment.
- Use trusted artifact repositories for software distribution.
- Record build provenance for every release.
- Secure CI/CD pipelines with automated security validation.
- Maintain detailed audit logs for build and deployment activities.

---

# Common Mistakes

- Deploying software directly from unverified builds.
- Allowing unrestricted access to build systems.
- Skipping code reviews for production changes.
- Ignoring configuration integrity.
- Failing to maintain build metadata.
- Treating CI/CD security as optional.

---

# Key Takeaways

- Build integrity ensures trusted source code becomes trusted software.
- Code signing and digital signatures verify authenticity and integrity.
- Secure CI/CD pipelines integrate integrity checks throughout the development lifecycle.
- Artifact repositories provide controlled storage and distribution of approved software.
- Build provenance, reproducible builds, and strong governance improve traceability and supply chain security.

```text id="rrks28"
**Next:** Part 3
```