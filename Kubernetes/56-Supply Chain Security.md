# Chapter 56 – Supply Chain Security

## Overview

Modern Kubernetes applications depend on a large software supply chain.

A typical application may depend on:

```text
Source Code
    ↓
Third-Party Libraries
    ↓
Operating System Packages
    ↓
Base Images
    ↓
Build Tools
    ↓
CI/CD Pipelines
    ↓
Container Images
    ↓
Container Registry
    ↓
Kubernetes
    ↓
Production
```

Every component in this chain can become a security risk.

Supply chain security focuses on ensuring that:

```text
Software comes from trusted sources
        +
Dependencies are trustworthy
        +
Builds are secure
        +
Artifacts are authentic
        +
Artifacts are not modified
        +
Deployment policies are enforced
```

A secure Kubernetes software supply chain should follow:

```text
Source
  ↓
Dependencies
  ↓
Secure Build
  ↓
Scan
  ↓
SBOM
  ↓
Provenance
  ↓
Sign
  ↓
Trusted Registry
  ↓
Verify
  ↓
Deploy
  ↓
Monitor
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes software supply chains
- Supply chain security fundamentals
- Supply chain threat models
- Source code security
- Dependency security
- Dependency confusion
- Typosquatting
- Malicious packages
- Compromised dependencies
- Container image supply chains
- Base image security
- Image provenance
- SBOM
- SPDX
- CycloneDX
- Image signing
- Cosign
- Sigstore
- Rekor
- Fulcio
- SLSA
- Build provenance
- Reproducible builds
- Secure CI/CD
- Build isolation
- Build attestations
- Artifact integrity
- Registry security
- Image immutability
- Digest pinning
- Admission control
- Policy enforcement
- Trusted builders
- Vulnerability management
- Secret security in CI/CD
- GitOps supply chain security
- Helm supply chain security
- Kubernetes admission security
- Dependency pinning
- Artifact promotion
- Release security
- Supply chain attack scenarios
- Compromised CI/CD
- Malicious images
- Dependency confusion attacks
- Build system compromise
- Signing key compromise
- Incident response
- Supply chain forensics
- Production supply chain architecture
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions

---

# What Is a Software Supply Chain?

A software supply chain is the collection of:

```text
People
Source Code
Dependencies
Build Systems
Tools
Artifacts
Registries
Deployment Systems
```

used to create and deliver software.

For Kubernetes:

```text
Developer
   ↓
Git
   ↓
CI/CD
   ↓
Container Build
   ↓
Registry
   ↓
Kubernetes
```

---

# Why Supply Chain Security Matters

An attacker does not always need to attack Kubernetes directly.

They may compromise:

```text
Dependency
    ↓
Build System
    ↓
Container Image
    ↓
Production
```

This can allow malicious code to reach production through a trusted deployment pipeline.

---

# Supply Chain Security Principle

> **Trust must be established at every stage of the software lifecycle.**

Do not automatically trust:

```text
Source Code
Dependencies
Builds
Images
Registries
CI/CD
```

Verify them.

---

# Kubernetes Supply Chain

A typical Kubernetes supply chain:

```text
Developer
    ↓
Source Repository
    ↓
Dependencies
    ↓
CI/CD Pipeline
    ↓
Container Build
    ↓
Security Scan
    ↓
SBOM
    ↓
Image Signing
    ↓
Container Registry
    ↓
Admission Control
    ↓
Kubernetes
    ↓
Runtime
```

---

# Supply Chain Threat Model

Potential attackers may target:

```text
Developer
Source Repository
Dependencies
Package Registry
Build Server
CI/CD Credentials
Container Registry
Signing Infrastructure
Deployment System
```

---

# Supply Chain Attack

A supply chain attack compromises a trusted component used by the target.

Instead of:

```text
Attacker
   ↓
Target
```

the attacker may use:

```text
Attacker
   ↓
Trusted Dependency
   ↓
Target
```

---

# Example

```text
Popular Package
      ↓
Compromised Maintainer Account
      ↓
Malicious Release
      ↓
Developer Installs Package
      ↓
Application
      ↓
Container Image
      ↓
Kubernetes
```

---

# Major Supply Chain Threats

```text
Dependency Confusion
Typosquatting
Malicious Packages
Compromised Dependencies
Compromised Base Images
Compromised CI/CD
Registry Compromise
Signing Key Theft
Build Tampering
Artifact Replacement
Credential Theft
```

---

# Source Code Security

The source repository is the starting point of the software supply chain.

Protect:

```text
Repositories
Branches
Pull Requests
Tags
Release Pipelines
Developer Accounts
Deploy Keys
CI Tokens
```

---

# Source Code Controls

Use:

```text
Branch Protection
Code Review
Required Approvals
Signed Commits where appropriate
MFA
Least Privilege
Secret Scanning
Dependency Scanning
Audit Logs
```

---

# Branch Protection

Production code should not normally be changed directly.

Use:

```text
Feature Branch
     ↓
Pull Request
     ↓
Review
     ↓
Security Checks
     ↓
Merge
```

---

# Code Review

Security-sensitive changes should receive appropriate review.

Examples:

```text
Authentication
Authorization
Secrets
Deployment
CI/CD
Dockerfiles
Infrastructure
```

---

# Developer Account Security

Compromised developer accounts can become supply-chain entry points.

Protect them using:

```text
MFA
Strong Authentication
Least Privilege
Device Security
Session Controls
Audit Logging
```

---

# Dependency Security

Modern applications depend heavily on third-party packages.

Examples:

```text
Python
npm
Java
Go
Rust
OS Packages
```

A vulnerability or malicious dependency can compromise the application.

---

# Dependency Pinning

Avoid unconstrained dependency versions.

Example:

```text
package >= 1.0
```

may allow unexpected versions.

Prefer controlled versions such as:

```text
package==1.5.2
```

or lock files:

```text
package-lock.json
poetry.lock
requirements.lock
go.sum
```

The exact approach depends on the package ecosystem.

---

# Lock Files

Lock files capture resolved dependency versions.

Example:

```text
Application
   ↓
Dependency Definition
   ↓
Lock File
   ↓
Reproducible Dependency Set
```

---

# Dependency Updates

Dependencies should be:

```text
Monitored
Scanned
Updated
Tested
Reviewed
```

Do not automatically accept every update into production without appropriate controls.

---

# Dependency Confusion

Dependency confusion occurs when a malicious package is selected instead of the intended internal package.

Example:

```text
Internal package:
company-auth
```

Attacker publishes:

```text
company-auth
```

to a public registry.

If the build configuration resolves the public package, malicious code may enter the build.

---

# Preventing Dependency Confusion

Use:

```text
Private Package Registries
Explicit Package Sources
Dependency Pinning
Lock Files
Namespace Controls
Allowlisting
Dependency Verification
```

---

# Typosquatting

An attacker creates a package name similar to a legitimate package.

Example:

```text
requests
```

vs:

```text
request
```

A developer may install the wrong package.

---

# Preventing Typosquatting

Use:

```text
Approved Dependencies
Dependency Review
Lock Files
Private Registries
Package Verification
Security Scanning
```

---

# Malicious Packages

A malicious package may contain:

```text
Credential Theft
Data Exfiltration
Backdoors
Cryptocurrency Mining
Command Execution
Persistence
```

---

# Compromised Dependency

A legitimate package can also become compromised.

Example:

```text
Trusted Package
      ↓
Maintainer Account Compromised
      ↓
Malicious Release
      ↓
Application
```

Therefore:

```text
Trusted Name
≠
Automatically Trusted Version
```

---

# Dependency Provenance

Ask:

```text
Where did this dependency come from?
Who published it?
Which version is used?
Was it modified?
```

---

# Container Image Supply Chain

A container image includes:

```text
Base Image
Application
Dependencies
Build Tools
Configuration
```

Every component must be considered.

---

# Base Image Supply Chain

Example:

```dockerfile
FROM python:3.13-slim
```

The application inherits dependencies from the base image.

Therefore:

```text
Base Image Security
=
Application Supply Chain Security
```

---

# Trusted Base Images

Use:

```text
Official Images
Enterprise Approved Images
Hardened Images
Maintained Images
Signed Images
```

where appropriate.

---

# Base Image Updates

Base images should be regularly rebuilt.

Example:

```text
Old Base Image
      ↓
Security Patch Released
      ↓
Rebuild
      ↓
Scan
      ↓
Sign
      ↓
Deploy
```

---

# Build System Security

The build system is one of the most important components in the supply chain.

If attackers compromise the build system:

```text
Trusted Source
      ↓
Compromised Build
      ↓
Malicious Artifact
```

The resulting artifact may appear legitimate.

---

# CI/CD Threats

Potential attacks include:

```text
Stolen CI Token
Malicious Pipeline Modification
Compromised Runner
Secret Theft
Build Tampering
Artifact Replacement
Signing Key Theft
```

---

# CI/CD Least Privilege

A build pipeline should receive only the permissions it requires.

Avoid:

```text
CI Job
 ↓
Cluster-admin
```

when the pipeline only needs:

```text
Push Image
```

---

# Build Isolation

Build systems should isolate workloads where possible.

For example:

```text
Build Job
   ↓
Ephemeral Runner
   ↓
Build Artifact
   ↓
Runner Destroyed
```

This reduces persistence opportunities.

---

# Ephemeral Build Runners

Ephemeral runners are created for individual jobs.

Conceptually:

```text
Job Starts
   ↓
Runner Created
   ↓
Build
   ↓
Artifact
   ↓
Runner Destroyed
```

This can reduce contamination between builds.

---

# Build Secrets

CI/CD systems often need:

```text
Registry Credentials
Signing Credentials
Cloud Credentials
Deployment Tokens
```

These must be protected.

---

# Avoid Long-Lived CI Credentials

Prefer:

```text
Short-Lived Credentials
OIDC
Workload Identity
Federated Identity
```

where supported.

---

# OIDC in CI/CD

OpenID Connect can allow a CI platform to obtain short-lived cloud credentials based on workload identity.

Conceptually:

```text
CI Job
  ↓
OIDC Identity
  ↓
Cloud IAM
  ↓
Temporary Credential
```

This reduces reliance on static secrets.

---

# Artifact Integrity

An artifact should be protected against unauthorized modification.

Examples:

```text
Container Image
Helm Chart
Binary
Package
SBOM
Manifest
```

---

# Image Digest

A digest provides a content-addressed reference.

Example:

```text
image@sha256:<digest>
```

This helps ensure that the deployed image corresponds to known content.

---

# Digest Pinning

Instead of:

```yaml
image: myapp:1.4.2
```

use:

```yaml
image: myapp@sha256:<digest>
```

for high-assurance deployments.

---

# Image Signing

Signing establishes trust in an artifact.

Conceptually:

```text
Image
 ↓
Signature
 ↓
Registry
 ↓
Verification
 ↓
Deployment
```

---

# Cosign

Cosign is commonly used for signing and verifying container images and other artifacts.

Conceptually:

```text
Build
 ↓
Sign
 ↓
Push
 ↓
Verify
```

---

# Sigstore

Sigstore is a collection of tools and services for software signing and supply-chain security.

Important components include:

```text
Cosign
Fulcio
Rekor
```

---

# Fulcio

Fulcio is a certificate authority used by Sigstore's keyless signing ecosystem.

It can issue short-lived certificates tied to verified identities.

Conceptually:

```text
Identity
   ↓
Fulcio
   ↓
Certificate
   ↓
Artifact Signing
```

---

# Rekor

Rekor is a transparency log.

It provides a public record of signed artifact-related metadata.

Conceptually:

```text
Signature
   ↓
Rekor
   ↓
Transparency Record
```

---

# Why Transparency Matters

Transparency helps security teams investigate:

```text
When was an artifact signed?
Who signed it?
What identity was associated with it?
Was the signature recorded?
```

---

# Image Verification

Before deployment:

```text
Image
 ↓
Signature
 ↓
Provenance
 ↓
Policy
 ↓
Allow / Reject
```

---

# Software Bill of Materials

An SBOM describes the components inside an artifact.

Example:

```text
Application
 ├── Python
 ├── Flask
 ├── OpenSSL
 ├── libc
 └── Other Dependencies
```

---

# SBOM Formats

Common formats:

```text
SPDX
CycloneDX
```

---

# Why SBOM Matters

Suppose a new vulnerability is announced:

```text
Critical CVE
```

Security teams can query:

```text
Which images contain the affected library?
```

without manually inspecting every image.

---

# SBOM in Incident Response

Example:

```text
CVE Discovered
      ↓
SBOM Database
      ↓
Affected Images
      ↓
Affected Workloads
      ↓
Patch
```

---

# Provenance

Provenance provides information about how an artifact was produced.

Example:

```text
Source Repository
Commit
Builder
Build Process
Dependencies
Timestamp
Artifact
```

---

# Build Provenance

Conceptually:

```text
Git Commit
    ↓
CI Pipeline
    ↓
Build Environment
    ↓
Container Image
```

Provenance records this relationship.

---

# Why Provenance Matters

It helps answer:

```text
Which source produced this image?
Which build system produced it?
Was the build authorized?
Which workflow ran?
```

---

# SLSA

SLSA stands for:

```text
Supply-chain Levels for Software Artifacts
```

It provides a framework for increasing software supply-chain security.

It focuses on concepts such as:

```text
Build Integrity
Provenance
Source Integrity
Artifact Integrity
```

---

# Reproducible Builds

A reproducible build attempts to produce the same artifact from the same inputs.

Conceptually:

```text
Same Source
+
Same Dependencies
+
Same Build Configuration
        ↓
Same Artifact
```

---

# Why Reproducibility Matters

It can help detect:

```text
Unexpected Build Changes
Build Tampering
Undocumented Dependencies
```

---

# Build Attestations

Attestations provide signed statements about an artifact.

Examples:

```text
Build Provenance
SBOM
Test Results
Security Scan Results
```

Conceptually:

```text
Artifact
  │
  ├── Provenance
  ├── SBOM
  └── Scan Result
```

---

# Artifact Promotion

Do not rebuild an artifact for every environment.

Prefer:

```text
Build Once
    ↓
Test
    ↓
Sign
    ↓
Development
    ↓
Staging
    ↓
Production
```

---

# Why Build Once?

If you rebuild:

```text
Development Image
```

then:

```text
Production Image
```

may differ.

Build-once promotion improves artifact consistency.

---

# Trusted Builders

Organizations can restrict production artifacts to approved build systems.

Example:

```text
Approved CI Platform
        ↓
Trusted Build
        ↓
Signed Artifact
```

An artifact built elsewhere may be rejected.

---

# Registry Security

A registry is part of the software supply chain.

Protect it using:

```text
Authentication
Authorization
TLS
Image Signing
Scanning
Immutability
Audit Logging
Retention
```

---

# Registry Access Control

Example:

```text
Developer
 ↓
Pull

CI
 ↓
Push

Release System
 ↓
Promote

Security Team
 ↓
Audit
```

Do not give every user:

```text
Push
Delete
Modify
```

permissions.

---

# Image Immutability

Production artifacts should not silently change.

For example:

```text
myapp:1.4.2
```

should ideally remain associated with the same content.

Registry immutability controls can help prevent tag replacement.

---

# Admission Control

Kubernetes admission controls can enforce supply-chain policies.

Example:

```text
Pod Submitted
      ↓
Admission Controller
      ↓
Image Trusted?
      ↓
Signed?
      ↓
Approved Registry?
      ↓
Policy Satisfied?
      ↓
Allow / Reject
```

---

# Admission Policy

A production policy may require:

```text
Approved Registry
+
Signed Image
+
Valid Provenance
+
Allowed Digest
+
Security Scan
```

---

# Policy Engines

Kubernetes environments may use policy tools such as:

```text
Kyverno
OPA Gatekeeper
Validating Admission Policies
```

to enforce organizational rules.

---

# Example Policy

Conceptually:

```text
IF image registry != trusted-registry
THEN reject
```

Another:

```text
IF image is not signed
THEN reject
```

Another:

```text
IF privileged == true
THEN reject
```

---

# GitOps Supply Chain

GitOps introduces another important supply-chain component:

```text
Git Repository
```

Example:

```text
Application
 ↓
Container Image
 ↓
GitOps Manifest
 ↓
Deployment Controller
 ↓
Kubernetes
```

---

# GitOps Risks

Potential threats:

```text
Compromised Git Account
Malicious Commit
Unauthorized Manifest Change
Compromised GitOps Controller
Stolen Repository Token
```

---

# GitOps Security

Use:

```text
Branch Protection
MFA
Code Review
Signed Changes
Secret Management
Least Privilege
Admission Policies
Audit Logs
```

---

# Helm Supply Chain

Helm charts can also introduce supply-chain risk.

A chart may contain:

```text
Deployments
Services
RBAC
Secrets
ConfigMaps
Pods
```

Therefore verify:

```text
Chart Source
Chart Version
Dependencies
Values
Templates
```

---

# Helm Chart Security

Use:

```text
Trusted Repositories
Version Pinning
Chart Verification
Code Review
Security Scanning
```

---

# Kubernetes Manifest Security

Review manifests for:

```text
privileged: true
hostPath
hostNetwork
hostPID
hostIPC
cluster-admin
Unrestricted RBAC
Unsafe Capabilities
Secrets
Untrusted Images
```

---

# Dependency Pinning

Pin:

```text
Application Dependencies
Base Images
Container Images
Helm Charts
Git Dependencies
Build Tools
```

where practical.

---

# Security Update Pipeline

A mature pipeline:

```text
New Vulnerability
      ↓
Identify Affected Dependencies
      ↓
Identify Affected Images
      ↓
Patch
      ↓
Rebuild
      ↓
Scan
      ↓
Sign
      ↓
Promote
      ↓
Deploy
```

---

# Supply Chain Attack Scenario 1

## Compromised Dependency

```text
Legitimate Package
      ↓
Maintainer Account Compromised
      ↓
Malicious Version
      ↓
Application Build
      ↓
Container Image
      ↓
Production
```

Controls:

```text
Lock Files
Dependency Scanning
Version Pinning
Trusted Registries
SBOM
Behavior Monitoring
```

---

# Supply Chain Attack Scenario 2

## Dependency Confusion

```text
Internal Package
      ↓
Public Package With Same Name
      ↓
Build Resolves Malicious Package
      ↓
Malicious Code
```

Controls:

```text
Private Registry
Explicit Sources
Namespace Controls
Dependency Pinning
```

---

# Supply Chain Attack Scenario 3

## Compromised CI/CD

```text
CI Account Compromised
      ↓
Pipeline Modified
      ↓
Malicious Image Built
      ↓
Image Signed
      ↓
Production
```

This is particularly dangerous because the malicious artifact may appear legitimate.

Controls:

```text
MFA
Least Privilege
Protected Pipelines
Build Isolation
Attestations
Audit Logging
Separate Signing Identity
```

---

# Supply Chain Attack Scenario 4

## Registry Compromise

```text
Registry
   ↓
Image Replaced
   ↓
Pod Pulls Modified Image
```

Controls:

```text
Image Digests
Signing
Registry Immutability
Signature Verification
```

---

# Supply Chain Attack Scenario 5

## Signing Key Compromise

```text
Signing Key Stolen
      ↓
Attacker Signs Malicious Image
      ↓
Image Appears Trusted
```

Controls:

```text
Hardware-backed Keys
KMS
Keyless Signing
Short-Lived Credentials
Identity-Based Signing
Key Rotation
Transparency Logs
```

---

# Supply Chain Attack Scenario 6

## Malicious Base Image

```text
Base Image
     ↓
Compromised
     ↓
Application Builds
     ↓
Production Image
```

Controls:

```text
Trusted Base Images
Image Scanning
Image Signing
Provenance
SBOM
Digest Pinning
```

---

# Supply Chain Security and Zero Trust

Zero trust applies to artifacts too.

Instead of:

```text
Image from trusted registry = trusted
```

use:

```text
Registry
+
Digest
+
Signature
+
Provenance
+
Policy
```

---

# Supply Chain Security Architecture

```text
                    Source Repository
                           │
                           ▼
                    Dependency Scan
                           │
                           ▼
                     Secure Build
                           │
               ┌───────────┼───────────┐
               ▼           ▼           ▼
             Scan         SBOM     Provenance
               │           │           │
               └───────────┼───────────┘
                           ▼
                         Sign
                           │
                           ▼
                   Trusted Registry
                           │
                           ▼
                 Admission Verification
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                  Allow         Reject
                    │
                    ▼
                 Kubernetes
                    │
                    ▼
              Runtime Security
```

---

# Supply Chain Security Layers

```text
1. Source Security
2. Dependency Security
3. Build Security
4. Artifact Security
5. Registry Security
6. Deployment Security
7. Runtime Security
```

---

# Source Security

Protect:

```text
Git
Branches
Commits
Tags
Developers
CI Tokens
```

---

# Dependency Security

Protect against:

```text
CVE
Malicious Package
Dependency Confusion
Typosquatting
```

---

# Build Security

Protect:

```text
CI/CD
Build Runner
Build Secrets
Signing
Build Configuration
```

---

# Artifact Security

Protect:

```text
Image
SBOM
Provenance
Signature
Digest
```

---

# Registry Security

Protect:

```text
Authentication
Authorization
Transport
Immutability
Audit
```

---

# Deployment Security

Enforce:

```text
Admission Policy
Image Verification
RBAC
Pod Security
NetworkPolicy
```

---

# Runtime Security

Monitor:

```text
Processes
Network
Files
System Calls
Behavior
```

---

# Supply Chain Security Maturity

## Level 1 – Basic

```text
Dependency Scanning
Image Scanning
```

---

## Level 2 – Controlled

```text
Version Pinning
Trusted Registry
Private Dependencies
```

---

## Level 3 – Verified

```text
SBOM
Signing
Digest Pinning
Provenance
```

---

## Level 4 – Enforced

```text
Admission Verification
Policy Enforcement
Build Attestations
```

---

## Level 5 – Mature

```text
Continuous Verification
Automated Remediation
Runtime Correlation
Incident Response
```

---

# Supply Chain Security and SOC

A SOC can correlate:

```text
Dependency Alert
+
Image Vulnerability
+
Runtime Event
```

Example:

```text
New CVE
   ↓
Affected Image
   ↓
Production Pod
   ↓
Unexpected Process
   ↓
High-Priority Incident
```

---

# Supply Chain Incident Response

If a malicious artifact is discovered:

```text
Identify Artifact
      ↓
Stop Promotion
      ↓
Identify Affected Versions
      ↓
Identify Running Workloads
      ↓
Quarantine
      ↓
Revoke Credentials
      ↓
Rebuild
      ↓
Rescan
      ↓
Resign
      ↓
Redeploy
      ↓
Investigate
```

---

# Supply Chain Forensics

Investigate:

```text
Source Commit
Dependency Version
Build Job
Build Runner
Build Logs
Image Digest
Registry Events
Signature
Provenance
Deployment Manifest
Kubernetes Audit Logs
Runtime Events
```

---

# Supply Chain Timeline

Create a timeline:

```text
T1 → Dependency Published
T2 → Dependency Added
T3 → Build Executed
T4 → Image Created
T5 → Image Signed
T6 → Image Deployed
T7 → Suspicious Activity
T8 → Detection
```

This helps determine:

```text
Initial Entry
Affected Artifacts
Affected Workloads
Attack Duration
```

---

# Evidence Sources

Useful evidence includes:

```text
Git Logs
CI/CD Logs
Registry Logs
SBOM
Provenance
Signature Records
Kubernetes Audit Logs
Pod Logs
Runtime Alerts
Network Logs
```

---

# Supply Chain Security Metrics

Track metrics such as:

```text
Percentage of Images Scanned
Percentage of Images Signed
Percentage Using Digests
Critical Vulnerabilities
Mean Time to Remediate
Unapproved Images
Unsigned Images
Dependency Age
SBOM Coverage
Provenance Coverage
```

---

# Example Security Dashboard

```text
Images Scanned             98%
Images Signed              94%
Digest Pinned              91%
SBOM Coverage              96%
Critical CVEs               2
Unsigned Production Images  1
Unapproved Registries       0
```

---

# Secure CI/CD Pipeline

```text
Checkout
   ↓
Authenticate Securely
   ↓
Dependency Scan
   ↓
Build
   ↓
Image Scan
   ↓
SBOM
   ↓
Provenance
   ↓
Sign
   ↓
Push
   ↓
Verify
   ↓
Promote
```

---

# Secure Production Deployment

```text
Artifact
   ↓
Signature Verification
   ↓
Provenance Verification
   ↓
Vulnerability Policy
   ↓
Registry Policy
   ↓
Admission
   ↓
Kubernetes
```

---

# Example Supply Chain Policy

A production cluster could require:

```text
Registry:
trusted-registry.example.com

Image:
Digest required

Signature:
Required

Provenance:
Required

Critical Vulnerabilities:
Blocked

SBOM:
Required
```

---

# Common Mistakes

## 1. Trusting Dependencies Blindly

A popular dependency can still become compromised.

---

## 2. Using Unpinned Dependencies

Uncontrolled updates reduce reproducibility.

---

## 3. Using Unknown Base Images

A compromised base image can affect every downstream image.

---

## 4. Trusting Image Tags

Tags can potentially change.

Prefer:

```text
Digest
```

for high-assurance deployments.

---

## 5. Not Signing Images

Without signatures, artifact authenticity is harder to establish.

---

## 6. Not Generating SBOMs

Without an SBOM, identifying affected artifacts during a vulnerability incident becomes harder.

---

## 7. Giving CI/CD Excessive Permissions

Avoid:

```text
CI → cluster-admin
```

unless absolutely necessary.

---

## 8. Storing Long-Lived CI Secrets

Prefer:

```text
OIDC
Workload Identity
Short-Lived Tokens
```

---

## 9. Rebuilding Artifacts Between Environments

Prefer:

```text
Build Once
Promote
```

---

## 10. No Admission Enforcement

Policies that are only documented but not enforced can be bypassed accidentally.

---

## 11. Ignoring GitOps Security

GitOps repositories are part of the deployment supply chain.

---

## 12. Trusting a Signature Without Checking Identity

A valid signature is not enough.

Verify:

```text
Who signed?
What artifact?
Under what policy?
```

---

# Best Practices

### 1. Protect Source Repositories

Use:

```text
MFA
Branch Protection
Code Review
Audit Logging
```

---

### 2. Pin Dependencies

Use:

```text
Lock Files
Version Constraints
Approved Sources
```

---

### 3. Use Trusted Registries

Restrict production images to approved registries.

---

### 4. Scan Dependencies

Scan:

```text
Application Dependencies
Base Images
OS Packages
```

---

### 5. Generate SBOMs

Maintain component visibility.

---

### 6. Generate Provenance

Record:

```text
Source
Builder
Workflow
Artifact
```

---

### 7. Sign Artifacts

Use:

```text
Cosign
Sigstore
```

or another trusted signing solution.

---

### 8. Verify Before Deployment

Use admission policies.

---

### 9. Pin Production Images

Prefer:

```text
Digest
```

over mutable tags.

---

### 10. Protect CI/CD

Use:

```text
Least Privilege
Ephemeral Runners
MFA
OIDC
Isolated Builds
```

---

### 11. Protect Signing Infrastructure

Use:

```text
KMS
Hardware-backed Keys
Keyless Signing
Short-Lived Credentials
```

where appropriate.

---

### 12. Use Build Attestations

Record:

```text
Provenance
SBOM
Security Results
```

---

### 13. Promote the Same Artifact

Use:

```text
Build Once
Promote Everywhere
```

---

### 14. Enforce Policies

Use:

```text
Admission Control
Kyverno
OPA Gatekeeper
Validating Admission Policies
```

as appropriate.

---

### 15. Monitor Continuously

Supply-chain security does not end at deployment.

---

# Production Supply Chain Checklist

```text
☑ MFA enabled
☑ Branch protection
☑ Code review
☑ Secret scanning
☑ Dependency scanning
☑ Dependency pinning
☑ Trusted package sources
☑ Trusted base images
☑ Image scanning
☑ SBOM generation
☑ Provenance generation
☑ Image signing
☑ Digest pinning
☑ Private registry
☑ Registry immutability
☑ Secure CI/CD
☑ Ephemeral build runners
☑ Least-privilege CI permissions
☑ Short-lived CI credentials
☑ Secure signing
☑ Admission verification
☑ Artifact promotion
☑ Runtime monitoring
☑ Incident response
```

---

# Hands-on Lab 1 – Dependency Scanning

Choose a test application.

Run a dependency scanner appropriate for its language.

Identify:

```text
Package
Version
Vulnerability
Severity
Fixed Version
```

---

# Hands-on Lab 2 – Dependency Pinning

Create a test project with unpinned dependencies.

Then introduce a lock file.

Compare:

```text
Uncontrolled Dependencies
```

with:

```text
Locked Dependencies
```

---

# Hands-on Lab 3 – Build an SBOM

Build a container image.

Generate:

```bash
trivy image \
  --format cyclonedx \
  --output sbom.json \
  myapp:1.0
```

Review the components.

---

# Hands-on Lab 4 – Image Provenance

Create a test CI pipeline.

Record:

```text
Git Commit
Build Job
Builder
Image Digest
```

Map:

```text
Source → Build → Artifact
```

---

# Hands-on Lab 5 – Sign an Image

Use Cosign in a disposable environment.

Practice:

```text
Build
 ↓
Push
 ↓
Sign
 ↓
Verify
```

---

# Hands-on Lab 6 – Digest Pinning

Deploy:

```text
myapp:1.0
```

then identify its digest.

Change the Kubernetes Deployment to:

```text
myapp@sha256:<digest>
```

Verify the running workload.

---

# Hands-on Lab 7 – Admission Policy

Create a policy requiring:

```text
Approved Registry
```

Deploy:

```text
Approved Image
```

Then attempt:

```text
Unapproved Image
```

Observe the rejection.

---

# Hands-on Lab 8 – Unsigned Image Policy

In a disposable cluster, configure an admission policy requiring signed images.

Test:

```text
Unsigned Image
```

Expected:

```text
Rejected
```

---

# Hands-on Lab 9 – CI Vulnerability Gate

Create a pipeline:

```text
Build
 ↓
Scan
 ↓
Critical CVE?
 ├── Yes → Fail
 └── No → Continue
```

Test using a deliberately vulnerable lab image.

---

# Hands-on Lab 10 – Build Once, Promote

Build:

```text
myapp:1.0
```

Promote it through:

```text
Development
Staging
Production
```

Verify the digest remains identical.

---

# Hands-on Lab 11 – Dependency Confusion Simulation

In a controlled private environment:

```text
Internal Package
Public Package With Same Name
```

Study how package resolution can create risk.

Do not publish malicious packages to public registries.

---

# Hands-on Lab 12 – CI Credential Review

Inspect a test CI pipeline for:

```text
Long-Lived Secrets
Overprivileged Tokens
Registry Credentials
Cloud Access Keys
```

Replace them with:

```text
OIDC
Workload Identity
Short-Lived Credentials
```

where supported.

---

# Hands-on Lab 13 – Supply Chain Incident

Simulate:

```text
Critical Dependency Vulnerability
```

Practice:

```text
Identify
 ↓
Find Affected Images
 ↓
Find Running Pods
 ↓
Patch
 ↓
Rebuild
 ↓
Scan
 ↓
Sign
 ↓
Redeploy
```

---

# Hands-on Lab 14 – Supply Chain Forensics

Build a timeline using:

```text
Git
CI/CD
Registry
Kubernetes
Runtime
```

Answer:

```text
Which source produced the image?
Which build created it?
Which digest was deployed?
When was it deployed?
Which workload ran it?
```

---

# Hands-on Lab 15 – End-to-End Supply Chain

Build the complete workflow:

```text
Git
 ↓
CI/CD
 ↓
Dependency Scan
 ↓
Container Build
 ↓
Image Scan
 ↓
SBOM
 ↓
Provenance
 ↓
Sign
 ↓
Registry
 ↓
Admission
 ↓
Kubernetes
 ↓
Runtime Monitoring
```

This is the most important practical exercise in this chapter.

---

# Quick Revision

## Supply Chain

```text
Everything involved in producing and delivering software
```

---

## Dependency Confusion

```text
Malicious public package selected instead of intended internal package
```

---

## Typosquatting

```text
Malicious package with a similar name to a legitimate package
```

---

## Dependency Pinning

```text
Controlling exact dependency versions/sources
```

---

## SBOM

```text
Inventory of software components
```

---

## Provenance

```text
Information about how an artifact was produced
```

---

## Attestation

```text
Signed statement about an artifact or build property
```

---

## Image Signing

```text
Establish artifact authenticity/integrity
```

---

## Cosign

```text
Artifact signing and verification tool
```

---

## Sigstore

```text
Software supply-chain security ecosystem
```

---

## Fulcio

```text
Certificate authority used in Sigstore's keyless signing ecosystem
```

---

## Rekor

```text
Transparency log
```

---

## SLSA

```text
Framework for software supply-chain security
```

---

## Digest Pinning

```text
Deploying a specific immutable image content reference
```

---

## Admission Control

```text
Enforce policies before workloads enter the cluster
```

---

## Artifact Promotion

```text
Move the same tested artifact through environments
```

---

# Essential Commands

Build image:

```bash
docker build -t myapp:1.0 .
```

Scan image:

```bash
trivy image myapp:1.0
```

Generate SBOM:

```bash
trivy image \
  --format cyclonedx \
  --output sbom.json \
  myapp:1.0
```

Inspect image digest:

```bash
docker inspect myapp:1.0
```

List Kubernetes images:

```bash
kubectl get pods -A \
  -o jsonpath='{range .items[*]}{.metadata.namespace}{" "}{.metadata.name}{" "}{.spec.containers[*].image}{"\n"}{end}'
```

Inspect Deployment image:

```bash
kubectl get deployment <name> \
  -o jsonpath='{.spec.template.spec.containers[*].image}'
```

Inspect Pod:

```bash
kubectl describe pod <pod>
```

Check admission-related resources:

```bash
kubectl get validatingadmissionpolicies
```

Check Kyverno policies if installed:

```bash
kubectl get clusterpolicies
```

Check Gatekeeper constraints if installed:

```bash
kubectl get constraints
```

---

# Interview Questions

## Basic

- What is software supply chain security?
- Why is supply chain security important in Kubernetes?
- What is a supply chain attack?
- What is dependency security?
- What is dependency confusion?
- What is typosquatting?
- What is dependency pinning?
- What is an SBOM?
- What is software provenance?
- What is image signing?
- What is Cosign?
- What is Sigstore?
- What is SLSA?
- What is an image digest?
- What is admission control?

---

## Intermediate

- How would you secure a Kubernetes software supply chain?
- Why should dependencies be pinned?
- Why should production images use digests?
- What is the purpose of an SBOM?
- What is the difference between an SBOM and provenance?
- What is the difference between signing and scanning?
- What is the purpose of Rekor?
- What is the purpose of Fulcio?
- How would you secure a CI/CD pipeline?
- How would you prevent dependency confusion?
- How would you secure a private registry?
- What are build attestations?
- What is a reproducible build?
- Why should you build an artifact once and promote it?
- How can admission control improve supply-chain security?

---

## Advanced

- Design an enterprise Kubernetes software supply-chain security architecture.
- How would you implement end-to-end artifact verification?
- How would you enforce signed images in Kubernetes?
- How would you implement provenance verification?
- How would you use SBOMs during a zero-day vulnerability response?
- How would you protect CI/CD from credential theft?
- How would you secure container image signing?
- How would you handle signing-key compromise?
- How would you respond to a compromised dependency?
- How would you investigate a suspected malicious image?
- How would you implement supply-chain security for GitOps?
- How would you secure Helm chart dependencies?
- How would you design a build-once-promote-everywhere pipeline?
- How would you prevent a compromised CI system from producing trusted malicious artifacts?
- How would you combine SLSA, SBOM, signing, provenance, and admission control?

---

# Interview Scenario 1

### Question

> What is the difference between image scanning and image signing?

### Answer

Image scanning asks:

```text
Does the image contain known vulnerabilities?
```

Image signing asks:

```text
Can we establish that this artifact came from a trusted signing identity and has not been altered?
```

Therefore:

```text
Scanning
=
Vulnerability Detection
```

```text
Signing
=
Authenticity / Integrity
```

They solve different problems.

---

# Interview Scenario 2

### Question

> Why is an SBOM important during a security incident?

### Answer

Suppose a critical vulnerability is discovered in:

```text
OpenSSL
```

The SBOM can help identify:

```text
Which Images
 ↓
Contain OpenSSL
 ↓
Which Pods
 ↓
Are Running Those Images
```

This dramatically speeds up incident response.

---

# Interview Scenario 3

### Question

> A malicious image was built by a compromised CI pipeline and signed successfully. How is that possible?

### Answer

Signing only establishes trust in the signing process or identity.

If the attacker compromises the trusted build pipeline or signing identity:

```text
Compromised CI
 ↓
Malicious Image
 ↓
Trusted Signing Identity
 ↓
Valid Signature
```

Therefore supply-chain security also requires:

```text
Secure CI/CD
+
Build Provenance
+
Trusted Build Environment
+
Least Privilege
+
Attestation
+
Audit
```

---

# Interview Scenario 4

### Question

> How would you prevent unsigned images from running in production?

### Answer

Use admission control.

Architecture:

```text
Pod Request
    ↓
Admission Controller
    ↓
Image Signature Verification
    ↓
Valid?
 ├── Yes → Allow
 └── No  → Reject
```

Tools/policies can include:

```text
Kyverno
OPA Gatekeeper
Validating Admission Policies
```

along with an image-signing system.

---

# Interview Scenario 5

### Question

> Why should production deployments use image digests?

### Answer

A tag can potentially be moved:

```text
myapp:1.0
 ↓
Image A
```

later:

```text
myapp:1.0
 ↓
Image B
```

A digest identifies specific content:

```text
myapp@sha256:<digest>
```

Therefore digest pinning improves:

```text
Reproducibility
Traceability
Deployment Integrity
Rollback Confidence
```

---

# Interview Scenario 6

### Question

> What happens if a critical dependency vulnerability is discovered?

### Answer

Use the SBOM to identify affected artifacts:

```text
CVE
 ↓
Affected Dependency
 ↓
Affected Images
 ↓
Affected Pods
```

Then:

```text
Patch
 ↓
Rebuild
 ↓
Scan
 ↓
Generate SBOM
 ↓
Sign
 ↓
Promote
 ↓
Deploy
```

---

# Interview Scenario 7

### Question

> How would you secure CI/CD credentials?

### Answer

Prefer:

```text
OIDC
+
Workload Identity
+
Short-Lived Credentials
+
Least Privilege
```

instead of:

```text
Long-Lived Static Credentials
```

Also use:

```text
Ephemeral Runners
Protected Pipelines
Audit Logs
Secret Masking
```

---

# Production Supply Chain Architecture

A mature enterprise implementation can look like:

```text
                         Developer
                             │
                             ▼
                      Source Repository
                             │
                     Branch Protection
                             │
                             ▼
                      Pull Request
                             │
                       Code Review
                             │
                             ▼
                         CI/CD
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
          Dependency       Static       Secret
             Scan          Analysis      Scan
                │            │            │
                └────────────┼────────────┘
                             ▼
                         Secure Build
                             │
                             ▼
                      Container Image
                             │
                ┌────────────┼────────────┐
                ▼            ▼            ▼
             CVE Scan       SBOM       Provenance
                │            │            │
                └────────────┼────────────┘
                             ▼
                           Sign
                             │
                             ▼
                    Trusted Registry
                             │
                             ▼
                    Artifact Promotion
                             │
                             ▼
                   Kubernetes Admission
                             │
                ┌────────────┴────────────┐
                ▼                         ▼
             Verify                    Reject
                │
                ▼
             Kubernetes
                │
                ▼
         Runtime Security
                │
                ▼
              SIEM
                │
                ▼
               SOC
```

---

# Supply Chain Security Checklist

```text
☑ Protect source repositories
☑ Enable MFA
☑ Use branch protection
☑ Review security-sensitive changes
☑ Scan dependencies
☑ Pin dependencies
☑ Use lock files
☑ Use trusted package sources
☑ Use trusted base images
☑ Scan container images
☑ Generate SBOMs
☑ Generate provenance
☑ Sign artifacts
☑ Verify signatures
☑ Pin production images by digest
☑ Secure container registries
☑ Enable image immutability
☑ Secure CI/CD runners
☑ Use ephemeral runners
☑ Use least-privilege CI permissions
☑ Prefer OIDC/workload identity
☑ Protect signing infrastructure
☑ Use admission policies
☑ Promote the same artifact
☑ Monitor runtime behavior
☑ Maintain incident response procedures
```

---

# Recommended Practice

1. Secure a Git repository.
2. Configure branch protection.
3. Enable secret scanning.
4. Scan application dependencies.
5. Pin dependencies.
6. Create a secure Dockerfile.
7. Use a trusted base image.
8. Build a container image.
9. Scan the image.
10. Generate an SBOM.
11. Generate build provenance.
12. Sign the image.
13. Push it to a private registry.
14. Pin the deployment to an image digest.
15. Configure admission control.
16. Reject untrusted registries.
17. Reject unsigned images.
18. Implement vulnerability gates.
19. Implement artifact promotion.
20. Use ephemeral CI runners.
21. Replace static cloud credentials with workload identity where supported.
22. Simulate a compromised dependency.
23. Simulate a compromised image.
24. Practice supply-chain incident response.
25. Build an end-to-end secure Kubernetes software supply chain.

---

# References

## Official / Industry Documentation

- Kubernetes Security Documentation
- Kubernetes Admission Control
- Kubernetes Validating Admission Policies
- Kubernetes Images
- Kubernetes RBAC
- Kubernetes Audit Logging
- Sigstore
- Cosign
- Fulcio
- Rekor
- SLSA
- SPDX
- CycloneDX
- OCI Image Specification
- Kyverno
- Open Policy Agent
- OPA Gatekeeper
- Trivy
- Container Registry Security Documentation

---

# Chapter Summary

Supply chain security protects the entire process used to produce and deploy software.

For Kubernetes, the supply chain extends across:

```text
Source
 ↓
Dependencies
 ↓
Build
 ↓
Container Image
 ↓
Registry
 ↓
Deployment
 ↓
Runtime
```

An attacker may compromise any stage.

Common attacks include:

```text
Dependency Confusion
Typosquatting
Malicious Packages
Compromised Dependencies
Compromised Base Images
CI/CD Compromise
Registry Compromise
Signing Key Theft
Build Tampering
```

Therefore:

> **A secure Kubernetes cluster cannot compensate for an insecure software supply chain.**

Source repositories should use:

```text
MFA
Branch Protection
Code Review
Least Privilege
Secret Scanning
```

Dependencies should use:

```text
Version Pinning
Lock Files
Trusted Sources
Dependency Scanning
```

Container images should use:

```text
Trusted Base Images
Vulnerability Scanning
SBOM
Provenance
Signing
Digest Pinning
```

CI/CD should use:

```text
Least Privilege
Ephemeral Runners
Short-Lived Credentials
OIDC
Workload Identity
Build Isolation
```

Registries should use:

```text
Authentication
Authorization
TLS
Immutability
Audit Logging
```

Kubernetes should enforce:

```text
Admission Policies
Image Verification
RBAC
Pod Security
NetworkPolicy
```

The key technologies include:

```text
SBOM
SPDX
CycloneDX
Cosign
Sigstore
Fulcio
Rekor
SLSA
```

Each solves a different problem.

```text
SBOM
=
What is inside the artifact?
```

```text
Provenance
=
How was the artifact produced?
```

```text
Signature
=
Who/what signed the artifact?
```

```text
Digest
=
Which exact artifact content is being deployed?
```

```text
Admission Policy
=
Should this artifact be allowed to run?
```

A mature deployment pipeline therefore becomes:

```text
Source
 ↓
Review
 ↓
Dependency Validation
 ↓
Secure Build
 ↓
Scan
 ↓
SBOM
 ↓
Provenance
 ↓
Sign
 ↓
Registry
 ↓
Verify
 ↓
Admission
 ↓
Kubernetes
 ↓
Runtime Monitoring
```

The most important principle is:

> **Do not trust software simply because it came from a trusted location. Verify its source, dependencies, build process, artifact integrity, provenance, and deployment policy.**

Supply chain security is therefore a combination of:

```text
Prevention
+
Verification
+
Policy Enforcement
+
Detection
+
Incident Response
```

This completes the foundational Kubernetes security module.

---

# Module 7 Complete

The security chapters covered:

```text
Chapter 46 – Kubernetes Security Fundamentals
Chapter 47 – Authentication
Chapter 48 – Authorization (RBAC)
Chapter 49 – Service Accounts
Chapter 50 – Admission Controllers
Chapter 51 – Pod Security Standards
Chapter 52 – Network Security
Chapter 53 – Secret Management
Chapter 54 – Image Security
Chapter 55 – Runtime Security
Chapter 56 – Supply Chain Security
```

---

## Next Module

# Module 8 — Kubernetes Observability

The next chapters are:

```text
Chapter 57 – Logging
Chapter 58 – Monitoring
Chapter 59 – Metrics Server
Chapter 60 – Prometheus
Chapter 61 – Grafana
Chapter 62 – Alertmanager
Chapter 63 – OpenTelemetry
Chapter 64 – Distributed Tracing
```

---

# Next Chapter

## Chapter 57 – Logging

Topics will include:

- Kubernetes Logging Fundamentals
- Why Logging Matters
- Application Logs
- Container Logs
- Pod Logs
- Node Logs
- Kubelet Logs
- Control Plane Logs
- Kubernetes API Server Logs
- Scheduler Logs
- Controller Manager Logs
- Container Runtime Logs
- System Logs
- `kubectl logs`
- Previous Container Logs
- Multi-Container Pod Logs
- Sidecar Logging
- Log Rotation
- Log Drivers
- CRI Logging
- Structured Logging
- JSON Logging
- Centralized Logging
- Fluent Bit
- Fluentd
- Logstash
- Elasticsearch
- OpenSearch
- Loki
- Log Collection Architecture
- Log Aggregation
- Log Retention
- Log Storage
- Log Indexing
- Log Parsing
- Log Enrichment
- Kubernetes Metadata
- Namespace-Based Logging
- Application Logging
- Security Logging
- Audit Logging
- Log Correlation
- Log-Based Alerting
- Sensitive Data in Logs
- Log Security
- Log Integrity
- Log Access Control
- Troubleshooting With Logs
- Production Logging Architecture
- Logging Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---