# Chapter 54 – Image Security

## Overview

Kubernetes workloads run container images.

A container image contains:

```text
Application Code
Dependencies
Libraries
Runtime
Operating System Components
Configuration
Metadata
```

If an image is compromised, the application running inside the Pod may also be compromised.

Therefore, container image security is a critical part of Kubernetes security.

A secure image lifecycle should look like:

```text
Source Code
    ↓
Build
    ↓
Scan
    ↓
Sign
    ↓
Store
    ↓
Verify
    ↓
Deploy
    ↓
Monitor
```

Image security should protect against:

```text
Vulnerable Dependencies
Malicious Images
Compromised Base Images
Supply Chain Attacks
Credential Leakage
Malicious Packages
Image Tampering
Untrusted Registries
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Container image security
- Why image security matters
- Container image lifecycle
- Trusted base images
- Minimal images
- Image registries
- Private registries
- Image Pull Secrets
- Image tags
- `latest` tag risks
- Immutable image digests
- Image signing
- Cosign
- Sigstore
- Software Bill of Materials (SBOM)
- Image vulnerability scanning
- CVE management
- Critical vulnerabilities
- Dependency security
- Base image updates
- Distroless images
- Rootless containers
- Image provenance
- SLSA
- Supply chain attacks
- Admission-based image policies
- Trusted registries
- Registry authentication
- `imagePullPolicy`
- Image verification
- Runtime image security
- Kubernetes image security architecture
- CI/CD image security
- Image promotion
- Production image governance
- Image incident response
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Is Container Image Security?

Container image security is the process of protecting container images throughout their lifecycle.

This includes:

```text
Build
Scan
Sign
Store
Transfer
Verify
Deploy
Monitor
```

---

# Why Image Security Matters

Consider:

```text
Developer
   ↓
Build Image
   ↓
Compromised Dependency
   ↓
Production Image
   ↓
Kubernetes
   ↓
Compromised Pod
```

The vulnerability may have entered the environment long before the container was deployed.

Therefore:

> **Kubernetes security starts before the image reaches the cluster.**

---

# Image Security Lifecycle

A secure lifecycle:

```text
Developer
    ↓
Source Repository
    ↓
Secure Build
    ↓
Dependency Validation
    ↓
Image Build
    ↓
Vulnerability Scan
    ↓
SBOM Generation
    ↓
Image Signing
    ↓
Trusted Registry
    ↓
Admission Verification
    ↓
Kubernetes
    ↓
Runtime Monitoring
```

---

# Container Image Structure

A container image generally contains multiple filesystem layers.

Conceptually:

```text
Application Layer
       ↓
Dependency Layer
       ↓
Runtime Layer
       ↓
Base Image
```

Each layer can introduce:

```text
Packages
Libraries
Files
Vulnerabilities
```

---

# Base Images

A base image provides the starting filesystem and runtime environment.

Examples:

```dockerfile
FROM ubuntu:24.04
```

or:

```dockerfile
FROM python:3.13-slim
```

or:

```dockerfile
FROM nginx:alpine
```

---

# Base Image Security

The base image should be:

```text
Trusted
Maintained
Updated
Minimal
Scanned
```

Avoid arbitrary images from unknown sources.

---

# Trusted Base Images

Organizations may maintain approved base images:

```text
company/python
company/node
company/java
company/nginx
```

These images can be:

```text
Hardened
Scanned
Signed
Approved
Regularly Updated
```

---

# Minimal Images

A minimal image contains only what the application requires.

Instead of:

```text
Large OS
+
Many Utilities
+
Compilers
+
Debugging Tools
```

use:

```text
Application
+
Required Runtime
+
Required Libraries
```

---

# Why Minimal Images?

Smaller images generally mean:

```text
Fewer Packages
Fewer Dependencies
Smaller Attack Surface
Faster Downloads
Reduced Vulnerability Exposure
```

---

# Example

Large:

```dockerfile
FROM ubuntu:24.04
```

Minimal runtime:

```dockerfile
FROM python:3.13-slim
```

For suitable applications, a distroless image may reduce the runtime footprint further.

---

# Distroless Images

Distroless images aim to contain only the application and required runtime components, without a traditional shell and many common operating-system utilities.

Conceptually:

```text
Traditional Image
 ├── Application
 ├── Runtime
 ├── Shell
 ├── Package Manager
 ├── Utilities
 └── Other Tools

Distroless
 ├── Application
 └── Required Runtime
```

---

# Distroless Security Benefits

Potential benefits include:

```text
Smaller Attack Surface
Fewer Packages
Fewer Utilities
Reduced Runtime Footprint
```

However, troubleshooting can be more difficult because common debugging tools may not exist inside the image.

---

# Multi-Stage Builds

Multi-stage Docker builds help keep build tools out of the production image.

Example:

```dockerfile
FROM golang:1.25 AS builder

WORKDIR /app

COPY . .

RUN go build -o server .

FROM gcr.io/distroless/base

COPY --from=builder /app/server /server

ENTRYPOINT ["/server"]
```

Conceptually:

```text
Builder Image
    ↓
Compile
    ↓
Binary
    ↓
Minimal Runtime Image
```

---

# Why Multi-Stage Builds Matter

Build environments may contain:

```text
Compilers
Package Managers
Source Code
Debugging Tools
Temporary Dependencies
```

These are usually unnecessary at runtime.

Multi-stage builds prevent many of these components from entering the production image.

---

# Image Registry

A registry stores and distributes container images.

Examples include:

```text
Docker Hub
GitHub Container Registry
Amazon ECR
Google Artifact Registry
Azure Container Registry
Harbor
```

---

# Private Registry

Organizations commonly use private registries for production images.

Architecture:

```text
CI/CD
  ↓
Private Registry
  ↓
Kubernetes
```

Benefits can include:

```text
Access Control
Private Images
Audit
Image Scanning
Image Signing Integration
```

---

# Registry Authentication

Kubernetes may need credentials to pull private images.

These can be supplied through:

```text
imagePullSecrets
```

Example:

```yaml
spec:

  imagePullSecrets:

  - name: registry-credentials
```

---

# Image Pull Secret

Create:

```bash
kubectl create secret docker-registry registry-credentials \
  --docker-server=registry.example.com \
  --docker-username=<username> \
  --docker-password=<password>
```

Then:

```yaml
imagePullSecrets:

- name: registry-credentials
```

Use the minimum permissions required.

---

# Registry Security

A production registry should use:

```text
Authentication
Authorization
TLS
Access Control
Vulnerability Scanning
Audit Logging
Image Retention
Immutability
```

---

# Image Tags

Example:

```text
nginx:1.30
```

The:

```text
1.30
```

portion is a tag.

Another example:

```text
myapp:latest
```

---

# `latest` Tag

Using:

```text
latest
```

can create deployment ambiguity.

Example:

```text
Pod A
 ↓
latest
 ↓
Image version X
```

Later:

```text
Pod B
 ↓
latest
 ↓
Image version Y
```

The same tag can point to different image content over time.

---

# Why `latest` Is Risky

Potential problems:

```text
Unpredictable Deployments
Difficult Rollbacks
Version Ambiguity
Reproducibility Problems
Supply Chain Risk
```

Avoid relying on:

```text
latest
```

for production deployments.

---

# Versioned Tags

Prefer meaningful version tags:

```text
myapp:1.4.2
```

instead of:

```text
myapp:latest
```

However, even version tags can potentially be moved or overwritten depending on registry configuration.

---

# Image Digest

An image digest identifies specific image content.

Example:

```text
myapp@sha256:abcdef...
```

Conceptually:

```text
Tag
 ↓
Reference

Digest
 ↓
Specific Content
```

---

# Tags vs Digests

| Reference | Behavior |
|---|---|
| Tag | Human-friendly, can potentially move |
| Digest | Content-addressed, immutable reference to specific content |

For high-assurance production deployments, digests provide stronger reproducibility.

---

# Immutable Image Reference

Example:

```yaml
image: registry.example.com/backend@sha256:<digest>
```

This ensures the workload references the image content identified by that digest.

---

# ImagePullPolicy

Kubernetes uses:

```yaml
imagePullPolicy:
```

to determine when to pull an image.

Common values:

```text
Always
IfNotPresent
Never
```

---

# `Always`

The kubelet checks the registry for the image reference when starting a container.

For tag-based references, this can result in pulling newer content when the tag resolves differently.

For digest references, the content is immutable even though the registry may still be contacted to resolve or retrieve the image.

---

# `IfNotPresent`

The image is pulled only if it is not already present locally.

This can reduce registry traffic but requires careful image management.

---

# `Never`

Kubernetes will not pull the image.

The image must already exist on the node.

---

# ImagePullPolicy Best Practice

Production environments should generally prefer:

```text
Explicit version
or
Digest
```

rather than:

```text
latest
```

---

# Image Vulnerability Scanning

Image scanners identify known vulnerabilities in:

```text
Operating System Packages
Libraries
Application Dependencies
Language Packages
```

Examples:

```text
Trivy
Grype
Clair
Docker Scout
Cloud Registry Scanners
```

---

# CVE

CVE stands for:

```text
Common Vulnerabilities and Exposures
```

A vulnerability may be associated with a CVE identifier such as:

```text
CVE-YYYY-NNNNN
```

---

# Vulnerability Severity

Vulnerabilities may be categorized as:

```text
Critical
High
Medium
Low
```

Severity alone should not determine risk.

Also consider:

```text
Exploitability
Exposure
Application Usage
Network Reachability
Compensating Controls
```

---

# Image Scanning Pipeline

```text
Source
 ↓
Build
 ↓
Image
 ↓
Scanner
 ↓
Vulnerabilities?
 ├── Yes → Remediate
 └── No  → Continue
```

---

# Example Trivy Scan

A local image can be scanned using:

```bash
trivy image myapp:1.0
```

A CI pipeline can fail based on configured severity thresholds.

Example concept:

```text
Critical vulnerability
        ↓
Build failed
```

---

# Vulnerability Management

Finding vulnerabilities is not enough.

A lifecycle is required:

```text
Discover
 ↓
Prioritize
 ↓
Remediate
 ↓
Rebuild
 ↓
Rescan
 ↓
Deploy
```

---

# False Positives

Scanners can sometimes report vulnerabilities that:

```text
Do not affect the application
Are unreachable
Have mitigating controls
Are incorrectly detected
```

Security teams should validate findings rather than blindly ignoring them.

---

# Dependency Security

Application dependencies can introduce vulnerabilities.

Examples:

```text
Python packages
npm packages
Java libraries
Go modules
OS packages
```

A secure build process should scan:

```text
Application Dependencies
+
Base Image Packages
```

---

# Software Bill of Materials

SBOM stands for:

```text
Software Bill of Materials
```

It describes the components contained in a software artifact.

Conceptually:

```text
Container Image
      ↓
SBOM
 ├── OS Package A
 ├── Library B
 ├── Library C
 └── Application Dependency D
```

---

# Why SBOM Matters

An SBOM helps answer:

```text
What components are inside this image?
```

This improves:

```text
Vulnerability Management
Compliance
Incident Response
Supply Chain Visibility
```

---

# SBOM Formats

Common formats include:

```text
CycloneDX
SPDX
```

---

# Generate an SBOM

Tools such as Trivy can generate SBOM output.

Example:

```bash
trivy image \
  --format cyclonedx \
  --output sbom.json \
  myapp:1.0
```

---

# Image Signing

Image signing provides a way to establish trust in an image artifact.

Conceptually:

```text
Image
 ↓
Private Key
 ↓
Signature
 ↓
Registry
 ↓
Verification
```

---

# Why Sign Images?

Signing can help establish:

```text
Who produced the image?
Was the image modified?
Is the image from a trusted build process?
```

---

# Cosign

Cosign is a tool from the Sigstore ecosystem for signing and verifying container images and other artifacts.

Conceptually:

```text
Build
 ↓
Image
 ↓
Cosign Sign
 ↓
Registry
 ↓
Verify Before Deployment
```

---

# Sigstore

Sigstore provides infrastructure and tools for software signing and supply-chain security.

Its ecosystem includes:

```text
Cosign
Fulcio
Rekor
```

These components support different aspects of artifact identity, signing, and transparency.

---

# Image Verification

Before deployment:

```text
Image
 ↓
Signature Verification
 ↓
Trusted?
 ├── Yes → Deploy
 └── No  → Reject
```

---

# Admission-Based Image Verification

An admission mechanism can enforce:

```text
Only signed images are allowed.
```

Architecture:

```text
Developer
   ↓
Kubernetes API
   ↓
Admission
   ↓
Signature Verification
   ↓
Trusted?
 ├── Yes → Allow
 └── No  → Reject
```

---

# Trusted Registries

Organizations may define:

```text
Allowed:
registry.company.com/*
```

and reject:

```text
docker.io/*
unknown-registry.example/*
```

This reduces the risk of untrusted image sources.

---

# Image Allowlisting

An admission policy can enforce:

```text
Only approved registries
```

Example:

```text
registry.example.com/team/*
```

This provides a strong supply-chain control.

---

# Image Denylisting

You can also block known problematic sources.

However:

```text
Allowlist
```

is generally stronger than attempting to maintain a large denylist.

---

# Image Provenance

Provenance answers:

```text
Where did this image come from?
How was it built?
Which source revision produced it?
Which build system created it?
```

---

# Build Provenance

Conceptually:

```text
Git Commit
    ↓
CI Build
    ↓
Container Image
    ↓
Signature
    ↓
Provenance
```

This creates traceability.

---

# SLSA

SLSA stands for:

```text
Supply-chain Levels for Software Artifacts
```

It provides a framework for improving software supply-chain security.

The goal is to strengthen:

```text
Build Integrity
Provenance
Source Control
Artifact Integrity
```

---

# Supply Chain Attack

A supply-chain attack compromises a dependency or build process rather than directly attacking the final target.

Example:

```text
Developer
   ↓
Third-Party Dependency
   ↓
Compromised Package
   ↓
Build
   ↓
Container Image
   ↓
Production
```

---

# Image Supply Chain Threats

Potential threats include:

```text
Compromised Base Image
Malicious Dependency
Registry Compromise
Build Pipeline Compromise
Credential Theft
Image Tampering
Malicious Maintainer
Typosquatting
Dependency Confusion
```

---

# Typosquatting

An attacker may publish a package or image with a name similar to a legitimate one.

Example:

```text
company/backend
```

vs:

```text
company/back-end
```

Developers may accidentally pull the malicious artifact.

---

# Dependency Confusion

An attacker may publish a malicious package using a name that causes package managers or build systems to select the attacker-controlled package.

Controls include:

```text
Private Registries
Dependency Pinning
Allowlisting
Package Verification
SBOM
Scanning
```

---

# Build Pipeline Security

Protect:

```text
Source Repository
CI/CD Credentials
Build Agents
Registry Credentials
Signing Keys
Deployment Credentials
```

A compromised build pipeline can produce malicious images that appear legitimate.

---

# Image Signing Key Security

Signing keys are highly sensitive.

Protect them using:

```text
KMS
Hardware-backed keys
Keyless signing
Short-lived identities
Access Controls
Audit Logging
```

---

# Keyless Signing

The Sigstore ecosystem supports keyless signing models based on workload or identity credentials.

Conceptually:

```text
Trusted Identity
      ↓
Signing
      ↓
Transparency Log
      ↓
Verification
```

This can reduce the need to manage long-lived private signing keys.

---

# Image Promotion

A secure deployment process can use:

```text
Development
     ↓
Testing
     ↓
Staging
     ↓
Production
```

Only approved artifacts are promoted.

---

# Image Promotion Architecture

```text
Build Image
    ↓
Scan
    ↓
Sign
    ↓
Development
    ↓
Tests
    ↓
Staging
    ↓
Approval
    ↓
Production
```

---

# Avoid Rebuilding Between Environments

Prefer:

```text
Build Once
 ↓
Test
 ↓
Promote Same Artifact
```

instead of:

```text
Build Development
 ↓
Rebuild Staging
 ↓
Rebuild Production
```

Rebuilding can produce different artifacts.

---

# Image Immutability

Production registries should ideally prevent overwriting approved image versions.

For example:

```text
myapp:1.4.2
```

should not silently change to a different image after deployment.

Even with immutable tags, digests remain the strongest content reference.

---

# Image Retention

Registries should have retention policies.

Remove:

```text
Unused Images
Old Vulnerable Images
Temporary Build Artifacts
```

while retaining:

```text
Required Release Artifacts
Compliance Artifacts
Incident Investigation Artifacts
```

---

# Image Access Control

Use:

```text
Least Privilege
```

for registry access.

Developers may need:

```text
Pull
```

but not necessarily:

```text
Delete
Push
Modify
```

---

# Runtime Image Security

Even a scanned image can become vulnerable later.

For example:

```text
Image scanned
 ↓
No critical CVEs
 ↓
New CVE discovered
 ↓
Existing deployed image becomes vulnerable
```

Therefore:

```text
Continuous Monitoring
```

is important.

---

# Image Security Monitoring

Monitor:

```text
New CVEs
Image Changes
Registry Events
Unexpected Images
Unsigned Images
Unapproved Registries
Deprecated Base Images
```

---

# Image Security and Pod Security

Image security and Pod security solve different problems.

```text
Image Security
=
What code are we running?
```

```text
Pod Security
=
How is that code allowed to run?
```

Both are necessary.

---

# Image Security and Runtime Security

```text
Image Security
 ↓
Prevent known vulnerable/malicious artifacts

Runtime Security
 ↓
Detect suspicious behavior after deployment
```

---

# Image Security Architecture

```text
                    Source Code
                         │
                         ▼
                    CI Pipeline
                         │
                ┌────────┼────────┐
                ▼        ▼        ▼
             Build     Scan      SBOM
                │        │        │
                └────────┼────────┘
                         ▼
                       Sign
                         │
                         ▼
                  Trusted Registry
                         │
                         ▼
                  Admission Policy
                         │
                  ┌──────┴──────┐
                  ▼             ▼
               Verify         Reject
                  │
                  ▼
                Pod
                  │
                  ▼
           Runtime Monitoring
```

---

# Kubernetes Image Security Controls

Kubernetes can contribute through:

```text
imagePullSecrets
Admission Policies
Pod Security
Service Accounts
RBAC
Audit Logging
```

External tools provide:

```text
Scanning
Signing
SBOM
Provenance
Registry Security
```

---

# Image Security in CI/CD

A production pipeline can implement:

```text
1. Checkout source
2. Dependency scan
3. Build image
4. Scan image
5. Generate SBOM
6. Sign image
7. Push image
8. Verify signature
9. Deploy
```

---

# Example CI Security Gate

```text
Build
 ↓
Critical CVE?
 ├── Yes → Fail
 └── No
      ↓
Generate SBOM
      ↓
Sign
      ↓
Push
      ↓
Deploy
```

---

# Vulnerability Gate

Organizations can define:

```text
Critical = Block
High = Review
Medium = Track
Low = Monitor
```

Do not blindly use severity alone.

Risk should consider:

```text
Exploitability
Exposure
Business Impact
Reachability
Compensating Controls
```

---

# Image Security Policy

A production policy may require:

```text
Approved Registry
+
Signed Image
+
Known Provenance
+
No Critical Vulnerabilities
+
SBOM Available
+
Immutable Reference
```

---

# Admission Policy Example

Conceptually:

```text
Pod submitted
      ↓
Image Registry Check
      ↓
Signature Check
      ↓
Vulnerability Policy
      ↓
Digest Check
      ↓
Allow / Reject
```

---

# Image Incident Response

Suppose a production image is discovered to contain a critical vulnerability.

Process:

```text
Identify Affected Images
        ↓
Identify Running Pods
        ↓
Assess Exposure
        ↓
Patch / Rebuild
        ↓
Rescan
        ↓
Sign
        ↓
Redeploy
        ↓
Verify
        ↓
Monitor
```

---

# Compromised Image Response

If an image itself is suspected to be malicious:

```text
Stop Promotion
      ↓
Quarantine Image
      ↓
Identify Running Workloads
      ↓
Replace Image
      ↓
Rotate Potentially Exposed Credentials
      ↓
Investigate
      ↓
Review Build Pipeline
      ↓
Review Registry
```

---

# Image Security and Secrets

Never bake secrets into images.

Bad:

```dockerfile
ENV API_KEY=secret123
```

or:

```dockerfile
COPY production-credentials.json /app/
```

These secrets may remain in image layers even if later deleted from the final filesystem.

---

# Why Deleting a Secret in a Later Layer Is Not Enough

Container images are layered.

Example:

```text
Layer 1
 └── secret.txt

Layer 2
 └── secret.txt deleted
```

The secret may still exist in:

```text
Layer 1
```

Therefore:

> **Do not put secrets into image layers in the first place.**

---

# Secure Build Pattern

Use:

```text
Build
 ↓
No Secrets Embedded
 ↓
Runtime Secret Injection
```

For example:

```text
External Secret Manager
        ↓
Kubernetes Secret
        ↓
Pod
```

---

# Rootless Containers

Running containers without root privileges can reduce risk.

Example:

```text
Container User
=
Non-root
```

This complements image security.

---

# Image Security and Rootless

A secure image may be built to run as:

```text
UID 1000
```

instead of:

```text
UID 0
```

---

# Image Security Threat Model

| Threat | Example | Control |
|---|---|---|
| Vulnerable dependency | Known CVE | Scanning |
| Malicious image | Untrusted registry | Allowlisting |
| Image tampering | Registry modification | Signing + digest |
| Compromised build | CI attack | Provenance |
| Secret leakage | Secret in image | Secret Manager |
| Dependency confusion | Malicious package | Pinning + trusted registries |
| Old base image | Unpatched OS | Rebuild |
| Unknown components | Hidden dependency | SBOM |

---

# Troubleshooting Image Pull Errors

If a Pod shows:

```text
ImagePullBackOff
```

investigate:

```text
Image name
Registry
Authentication
Network connectivity
Image existence
Tag
Digest
Registry permissions
```

---

# Check Pod Events

```bash
kubectl describe pod <pod>
```

Look under:

```text
Events
```

---

# Check Image

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.containers[*].image}'
```

---

# Common Image Pull Error

```text
unauthorized
```

Possible cause:

```text
Missing imagePullSecret
```

Check:

```bash
kubectl get pod <pod> -o yaml
```

Look for:

```yaml
imagePullSecrets:
```

---

# Common Image Pull Error

```text
manifest unknown
```

Possible causes:

```text
Incorrect tag
Incorrect repository
Image does not exist
```

---

# Common Image Pull Error

```text
x509: certificate signed by unknown authority
```

Potential cause:

```text
Registry TLS trust problem
```

---

# Common Image Pull Error

```text
ImagePullBackOff
```

This is a status indicating repeated image pull failures.

Always inspect:

```bash
kubectl describe pod <pod>
```

for the underlying reason.

---

# Hands-on Lab 1 – Scan an Image

Install a scanner such as Trivy.

Run:

```bash
trivy image nginx:1.30
```

Review:

```text
Critical
High
Medium
Low
```

vulnerabilities.

---

# Hands-on Lab 2 – Compare Image Sizes

Compare:

```text
ubuntu
python-slim
distroless
```

Observe:

```text
Image Size
Package Count
Available Tools
Attack Surface
```

---

# Hands-on Lab 3 – Build a Multi-Stage Image

Create a simple application.

Build using:

```text
Builder Stage
```

and:

```text
Minimal Runtime Stage
```

Compare the resulting image with a single-stage build.

---

# Hands-on Lab 4 – Generate an SBOM

Use:

```bash
trivy image \
  --format cyclonedx \
  --output sbom.json \
  myapp:1.0
```

Inspect:

```text
Packages
Versions
Dependencies
```

---

# Hands-on Lab 5 – Use an Immutable Digest

Pull an image and inspect its digest.

Use:

```text
image@sha256:<digest>
```

in a Kubernetes Deployment.

Verify that the Deployment references the digest.

---

# Hands-on Lab 6 – Private Registry

Create or use a disposable private registry.

Push:

```text
myapp:1.0
```

Create a Kubernetes registry Secret:

```bash
kubectl create secret docker-registry registry-credentials \
  --docker-server=<registry> \
  --docker-username=<username> \
  --docker-password=<password>
```

Deploy using:

```yaml
imagePullSecrets:

- name: registry-credentials
```

---

# Hands-on Lab 7 – Image Pull Failure

Use an intentionally invalid image:

```text
registry.example.com/nonexistent/image:999
```

Deploy it.

Observe:

```text
ImagePullBackOff
```

Run:

```bash
kubectl describe pod <pod>
```

Identify the exact failure.

---

# Hands-on Lab 8 – Test `imagePullPolicy`

Test:

```text
Always
IfNotPresent
Never
```

Observe image pulling behavior.

Use a disposable environment.

---

# Hands-on Lab 9 – Image Signing

Use Cosign in a test environment.

Conceptually:

```text
Build
 ↓
Push
 ↓
Sign
 ↓
Verify
```

Verify that the signature can be checked before deployment.

Never place production signing keys in an insecure lab environment.

---

# Hands-on Lab 10 – Image Admission

Deploy an admission policy in a disposable cluster that requires:

```text
Approved Registry
```

Attempt to deploy:

```text
Unapproved Registry
```

Expected:

```text
Admission Rejection
```

---

# Hands-on Lab 11 – Vulnerability Gate

Create a CI pipeline that:

```text
Builds Image
 ↓
Scans Image
 ↓
Fails if Critical vulnerability exists
```

Then test with an intentionally vulnerable lab image.

---

# Hands-on Lab 12 – Secret Detection

Create a test Dockerfile containing a fake credential.

Scan the repository and image.

Verify that the secret is detected.

Never use a real credential.

---

# Hands-on Lab 13 – Image Promotion

Build:

```text
myapp:1.0
```

Promote the same artifact through:

```text
Development
 ↓
Staging
 ↓
Production
```

Verify that the image digest remains unchanged.

---

# Common Mistakes

## 1. Using `latest`

Avoid:

```text
myapp:latest
```

for production workloads.

---

## 2. Trusting Tags as Immutable

Tags can potentially be moved.

Use:

```text
Digest
```

for stronger reproducibility.

---

## 3. Using Unknown Images

Do not blindly deploy:

```text
Random Docker Hub image
```

---

## 4. Ignoring Base Images

Your application may be secure while the base image contains vulnerable packages.

---

## 5. Ignoring Application Dependencies

Vulnerabilities can exist in:

```text
npm
pip
Maven
Go
OS packages
```

---

## 6. Embedding Secrets

Never put:

```text
Passwords
Tokens
Private Keys
```

inside images.

---

## 7. Scanning Only During Build

New vulnerabilities can be discovered after deployment.

Use continuous monitoring.

---

## 8. Ignoring Image Provenance

Know:

```text
Who built it?
From what source?
Using which pipeline?
```

---

## 9. Running as Root

A secure image should preferably run as a non-root user where possible.

---

## 10. Installing Unnecessary Tools

Avoid unnecessary:

```text
Shells
Compilers
Package Managers
Debug Utilities
```

in production images.

---

## 11. Rebuilding for Every Environment

Prefer:

```text
Build Once
Promote Same Artifact
```

---

## 12. Ignoring Registry Security

The registry is part of the software supply chain.

---

# Best Practices

### 1. Use Trusted Base Images

Prefer:

```text
Official
Maintained
Hardened
Scanned
```

base images.

---

### 2. Keep Images Minimal

Use:

```text
Slim
Alpine where appropriate
Distroless where appropriate
```

after compatibility testing.

---

### 3. Use Multi-Stage Builds

Keep build dependencies out of production images.

---

### 4. Scan Images

Scan:

```text
Base Image
Dependencies
Application
```

---

### 5. Generate SBOMs

Maintain visibility into image contents.

---

### 6. Sign Images

Use signing mechanisms such as:

```text
Cosign / Sigstore
```

where appropriate.

---

### 7. Verify Images Before Deployment

Use admission controls to enforce trust requirements.

---

### 8. Prefer Image Digests

For high-assurance production deployments:

```text
image@sha256:<digest>
```

---

### 9. Use Private Registries

Restrict production image sources.

---

### 10. Protect Registry Credentials

Use:

```text
Least Privilege
Short-Lived Credentials
Workload Identity
```

where supported.

---

### 11. Scan Continuously

New vulnerabilities can appear after an image is deployed.

---

### 12. Patch Base Images

Regularly rebuild when:

```text
OS Updates
Security Patches
Runtime Updates
```

are released.

---

### 13. Never Embed Secrets

Inject secrets at runtime.

---

### 14. Use Non-Root Containers

Prefer:

```text
UID != 0
```

where compatible.

---

### 15. Maintain Provenance

Record:

```text
Source Commit
Builder
Build Time
Dependencies
Image Digest
Signature
```

---

# Production Image Governance

An enterprise image policy may require:

```text
☑ Approved Registry
☑ Approved Base Image
☑ Vulnerability Scan
☑ No Critical Vulnerabilities
☑ SBOM
☑ Signed Image
☑ Verified Provenance
☑ Immutable Digest
☑ Non-root Runtime
☑ No Embedded Secrets
☑ Security Review
```

---

# Secure Image Pipeline

```text
Developer
    │
    ▼
Source Repository
    │
    ▼
Dependency Scan
    │
    ▼
Secure Build
    │
    ▼
Image Scan
    │
    ▼
SBOM
    │
    ▼
Sign
    │
    ▼
Trusted Registry
    │
    ▼
Admission Verification
    │
    ▼
Kubernetes
    │
    ▼
Runtime Monitoring
```

---

# Image Security Defense in Depth

```text
Source Security
      ↓
Dependency Security
      ↓
Build Security
      ↓
Image Scanning
      ↓
SBOM
      ↓
Signing
      ↓
Registry Security
      ↓
Admission Verification
      ↓
Pod Security
      ↓
Runtime Security
```

---

# Quick Revision

## Container Image

```text
Application + Runtime + Dependencies
```

---

## Base Image

```text
Starting filesystem/runtime
```

---

## Minimal Image

```text
Only required components
```

---

## Distroless

```text
Minimal runtime image without typical OS utilities
```

---

## Multi-Stage Build

```text
Separate build and runtime images
```

---

## Registry

```text
Stores container images
```

---

## Image Tag

```text
Human-friendly image reference
```

---

## Digest

```text
Content-addressed image identifier
```

---

## `latest`

```text
Mutable tag; avoid relying on it in production
```

---

## ImagePullPolicy

```text
Controls image pulling behavior
```

---

## CVE

```text
Common Vulnerabilities and Exposures
```

---

## SBOM

```text
Software Bill of Materials
```

---

## Image Signing

```text
Establish artifact authenticity/integrity
```

---

## Cosign

```text
Container/artifact signing tool
```

---

## Sigstore

```text
Software supply-chain security ecosystem
```

---

## Provenance

```text
Evidence of where/how an artifact was built
```

---

## SLSA

```text
Framework for improving software supply-chain security
```

---

# Essential Commands

Build an image:

```bash
docker build -t myapp:1.0 .
```

List local images:

```bash
docker images
```

Inspect image:

```bash
docker inspect myapp:1.0
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

Create registry Secret:

```bash
kubectl create secret docker-registry registry-credentials \
  --docker-server=<registry> \
  --docker-username=<username> \
  --docker-password=<password>
```

List image pull Secrets:

```bash
kubectl get secrets
```

Inspect Pod image:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.spec.containers[*].image}'
```

Inspect Pod events:

```bash
kubectl describe pod <pod>
```

Check Deployment image:

```bash
kubectl get deployment <name> \
  -o jsonpath='{.spec.template.spec.containers[*].image}'
```

Check Pods:

```bash
kubectl get pods
```

---

# Interview Questions

## Basic

- What is container image security?
- Why is image security important?
- What is a container image?
- What is a base image?
- Why should images be minimal?
- What is a container registry?
- What is a private registry?
- What is an image tag?
- What is an image digest?
- Why is `latest` risky?
- What is `imagePullPolicy`?
- What is an image vulnerability?
- What is a CVE?
- What is an SBOM?

---

## Intermediate

- What is the difference between an image tag and digest?
- How would you secure a private container registry?
- How do you scan a container image?
- What is multi-stage Docker build?
- What are distroless images?
- Why should secrets not be included in container images?
- What is image signing?
- What is Cosign?
- What is Sigstore?
- What is image provenance?
- What is SLSA?
- How can Kubernetes verify trusted images?
- How does `imagePullSecrets` work?
- How would you enforce approved registries?
- How would you prevent `latest` from being deployed?

---

## Advanced

- Design an enterprise container image security pipeline.
- How would you implement image signing and verification?
- How would you enforce signed images using admission control?
- How would you handle a critical CVE discovered in a production image?
- How would you secure the image build pipeline?
- How would you prevent supply-chain attacks?
- How would you implement image provenance?
- How would you use SBOMs during incident response?
- How would you design image promotion across development, staging, and production?
- How would you prevent secrets from entering image layers?
- How would you secure a private registry?
- How would you detect malicious images?
- How would you combine image security with Pod Security Standards?
- What is the difference between vulnerability scanning and image signing?
- Why is an image being signed not proof that it is vulnerability-free?
- Why is vulnerability scanning not proof that an image is trustworthy?

---

# Interview Scenario 1

### Question

> Why is `latest` not recommended for production?

### Answer

Because the tag can point to different image content over time.

For example:

```text
myapp:latest
    ↓
Image A
```

Later:

```text
myapp:latest
    ↓
Image B
```

This can cause:

```text
Unpredictable Deployments
Difficult Rollbacks
Version Ambiguity
```

A stronger approach is:

```text
myapp@sha256:<digest>
```

because the digest identifies specific image content.

---

# Interview Scenario 2

### Question

> Is an image digest better than a tag?

### Answer

For reproducibility and high-assurance deployments, yes.

A tag such as:

```text
myapp:1.0
```

can potentially be moved.

A digest:

```text
myapp@sha256:<digest>
```

identifies specific content.

Therefore:

```text
Tag
=
Human-friendly reference
```

```text
Digest
=
Content-addressed reference
```

---

# Interview Scenario 3

### Question

> An image has no Critical CVEs. Is it safe?

### Answer

Not necessarily.

Vulnerability scanning answers:

```text
Are known vulnerabilities detected?
```

It does not necessarily answer:

```text
Was the image produced by a trusted build?
Was the image tampered with?
Does it contain malicious code?
Was a dependency intentionally compromised?
```

Therefore image security should combine:

```text
Scanning
+
SBOM
+
Signing
+
Provenance
+
Trusted Registry
```

---

# Interview Scenario 4

### Question

> How would you prevent developers from deploying images from Docker Hub into production?

### Answer

Use admission control to enforce an approved registry allowlist.

For example:

```text
Allowed:
registry.company.com/*
```

and reject:

```text
Unapproved Registry
```

Architecture:

```text
Pod
 ↓
Admission
 ↓
Registry Policy
 ↓
Approved?
 ├── Yes → Allow
 └── No  → Reject
```

---

# Interview Scenario 5

### Question

> A critical CVE was discovered in an image already running in production. What would you do?

### Answer

First:

```text
Identify affected image
```

Then:

```text
Assess exposure
 ↓
Patch dependency/base image
 ↓
Rebuild
 ↓
Scan
 ↓
Generate SBOM
 ↓
Sign
 ↓
Push
 ↓
Redeploy
 ↓
Verify
```

Also determine whether:

```text
Credentials
Secrets
Data
```

could have been exposed.

If exploitation is suspected:

```text
Rotate credentials
Investigate logs
Contain workload
Perform incident response
```

---

# Interview Scenario 6

### Question

> Why should you not copy a production secret into a Dockerfile and delete it later?

### Answer

Container images are layered.

For example:

```text
Layer 1
 └── production-secret

Layer 2
 └── secret deleted
```

The secret may still exist in the earlier layer.

Therefore:

```text
Secret
 ↓
Image Layer
 ↓
Registry
```

can permanently expose the credential.

Instead:

```text
Secret Manager
 ↓
Kubernetes
 ↓
Runtime Injection
```

should be used.

---

# Production Image Security Checklist

```text
☑ Trusted base images
☑ Minimal images
☑ Multi-stage builds
☑ Non-root runtime
☑ No embedded secrets
☑ Private registry
☑ Registry access control
☑ Vulnerability scanning
☑ SBOM generation
☑ Image signing
☑ Provenance
☑ Immutable digests
☑ Admission verification
☑ Continuous vulnerability monitoring
☑ Secure CI/CD
☑ Secure signing keys
☑ Image promotion controls
☑ Image retention policy
☑ Incident response process
```

---

# Recommended Practice

1. Build a container image.
2. Inspect its layers.
3. Scan the image.
4. Identify vulnerable packages.
5. Update the base image.
6. Rebuild.
7. Rescan.
8. Generate an SBOM.
9. Compare image tags and digests.
10. Deploy using an immutable digest.
11. Configure a private registry.
12. Configure `imagePullSecrets`.
13. Test `imagePullPolicy`.
14. Build a multi-stage image.
15. Compare image sizes.
16. Test a distroless image.
17. Run the application as non-root.
18. Practice image signing.
19. Verify an image signature.
20. Build an admission policy for approved registries.
21. Create a CI vulnerability gate.
22. Implement image promotion.
23. Simulate a critical CVE response.
24. Simulate a compromised image response.
25. Design an enterprise image security architecture.

---

# References

## Official / Industry Documentation

- Kubernetes Images
- Kubernetes Secrets
- Kubernetes Admission Control
- Kubernetes Security
- Docker Image Documentation
- OCI Image Specification
- Sigstore
- Cosign
- SLSA
- SPDX
- CycloneDX
- Trivy
- Cloud Container Registry Security Documentation

---

# Chapter Summary

Container images are a critical component of Kubernetes security.

An image contains:

```text
Application
+
Dependencies
+
Runtime
+
Operating System Components
```

A vulnerable or malicious image can introduce risk into the Kubernetes cluster.

A secure image lifecycle is:

```text
Source
 ↓
Build
 ↓
Scan
 ↓
SBOM
 ↓
Sign
 ↓
Registry
 ↓
Verify
 ↓
Deploy
 ↓
Monitor
```

Use:

```text
Trusted Base Images
```

and keep images:

```text
Small
Minimal
Updated
Scanned
```

Multi-stage builds can keep build tools out of production images.

Distroless images can further reduce the runtime footprint when application compatibility allows.

Avoid:

```text
latest
```

for production workloads.

Prefer:

```text
Versioned Tags
```

and, for stronger reproducibility:

```text
Image Digests
```

such as:

```text
registry.example.com/app@sha256:<digest>
```

Image vulnerability scanning identifies known vulnerabilities in:

```text
OS Packages
Libraries
Application Dependencies
```

but scanning alone does not establish artifact trust.

Therefore combine:

```text
Vulnerability Scanning
+
SBOM
+
Image Signing
+
Provenance
```

SBOMs provide visibility into the components inside an image.

Image signing helps verify:

```text
Artifact Authenticity
Artifact Integrity
Artifact Origin
```

and tools such as:

```text
Cosign
```

and the:

```text
Sigstore
```

ecosystem can support image signing and verification.

Supply-chain security must also protect:

```text
Source Code
Dependencies
CI/CD
Build Systems
Signing
Registry
Deployment
```

A compromised build pipeline can produce malicious images even when the application source appears legitimate.

Kubernetes can strengthen image security through:

```text
imagePullSecrets
Admission Policies
RBAC
Pod Security
Audit Logging
```

Admission policies can enforce requirements such as:

```text
Approved Registry
Signed Image
Allowed Image Digest
Trusted Provenance
```

A production image governance policy may therefore require:

```text
Approved Registry
+
Trusted Base Image
+
No Critical Vulnerabilities
+
SBOM
+
Signature
+
Provenance
+
Immutable Digest
+
Non-root Runtime
+
No Embedded Secrets
```

The key principle is:

> **Do not assume an image is trustworthy simply because it runs successfully. Establish trust in the image's source, contents, build process, integrity, and deployment reference.**

A mature Kubernetes image-security architecture is:

```text
                    Source
                      │
                      ▼
                 CI/CD Build
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Scanning     SBOM      Provenance
          │           │           │
          └───────────┼───────────┘
                      ▼
                   Signing
                      │
                      ▼
              Trusted Registry
                      │
                      ▼
             Admission Verification
                      │
                ┌─────┴─────┐
                ▼           ▼
              Allow        Reject
                │
                ▼
              Kubernetes
                │
                ▼
           Runtime Security
```

The most important distinction to remember is:

```text
Scanning
=
Known vulnerability detection
```

```text
Signing
=
Artifact authenticity/integrity
```

```text
SBOM
=
Component visibility
```

```text
Provenance
=
Build origin and process
```

These controls complement each other rather than replacing one another.

---

## Next Chapter

# Chapter 55 – Runtime Security

Topics will include:

- Kubernetes Runtime Security
- Container Runtime Security
- Runtime Threat Model
- Runtime Attack Surface
- Container Escape
- Privilege Escalation
- Linux Capabilities
- Seccomp
- AppArmor
- SELinux
- Rootless Containers
- Runtime Detection
- Runtime Threat Detection
- Process Monitoring
- File Monitoring
- Network Monitoring
- System Call Monitoring
- eBPF
- Falco
- Tetragon
- Audit Logs
- Container Runtime Events
- Suspicious Processes
- Reverse Shell Detection
- Cryptocurrency Mining
- Malware Detection
- Persistence
- Lateral Movement
- Credential Theft
- Container Escape Detection
- Runtime Policies
- Kubernetes Runtime Security Architecture
- Runtime Security vs Image Security
- Runtime Security vs Pod Security
- Incident Response
- Evidence Collection
- Runtime Forensics
- Production Deployment
- Security Monitoring
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---