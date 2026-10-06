# Chapter 79 – CI/CD with Kubernetes

## Overview

CI/CD stands for:

```text
Continuous Integration
Continuous Delivery
Continuous Deployment
```

CI/CD automates the software lifecycle from source code changes to testing, packaging, security validation, and deployment.

With Kubernetes, a typical modern pipeline looks like:

```text
Developer
   ↓
Git
   ↓
CI Pipeline
   ↓
Build
   ↓
Test
   ↓
Security Scan
   ↓
Container Image
   ↓
Image Registry
   ↓
Deployment Configuration
   ↓
GitOps / CD
   ↓
Kubernetes
   ↓
Verification
   ↓
Monitoring
```

A production-grade Kubernetes CI/CD system should provide:

```text
Automation
+
Security
+
Repeatability
+
Traceability
+
Fast Feedback
+
Safe Deployment
+
Rollback
```

---

# Learning Objectives

After completing this chapter, you will understand:

- CI/CD fundamentals
- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- Kubernetes CI/CD
- CI/CD architecture
- Source control
- Build automation
- Testing
- Unit testing
- Integration testing
- Security testing
- Container builds
- Docker
- BuildKit
- Image registries
- Image tagging
- Image digests
- Image scanning
- SBOM
- Image signing
- Supply-chain security
- Deployment automation
- Kubernetes manifests
- Helm
- Kustomize
- GitOps integration
- Argo CD
- Flux
- GitHub Actions
- GitLab CI
- Jenkins
- Tekton
- Pipeline stages
- Environment promotion
- Development
- Staging
- Production
- Deployment strategies
- Rolling updates
- Blue-green deployment
- Canary deployment
- Progressive delivery
- Automated rollbacks
- Deployment gates
- Approval gates
- Secrets management
- CI/CD security
- RBAC
- Runner security
- Pipeline isolation
- Artifact security
- Dependency security
- Vulnerability scanning
- Policy as Code
- Compliance
- Deployment verification
- Smoke testing
- Health checks
- Observability
- Notifications
- Failure handling
- Pipeline troubleshooting
- Production CI/CD architecture
- Best practices
- Common mistakes
- Hands-on labs
- Quick revision
- Interview questions

---

# What Is CI?

Continuous Integration means frequently integrating code changes into a shared repository and automatically validating them.

Typical CI flow:

```text
Code Change
    ↓
Pull Request
    ↓
Build
    ↓
Unit Tests
    ↓
Static Analysis
    ↓
Security Scanning
    ↓
Artifact
```

---

# What Is CD?

CD can mean:

```text
Continuous Delivery
```

or:

```text
Continuous Deployment
```

---

# Continuous Delivery

Continuous Delivery keeps software in a deployable state.

A production deployment may require approval.

```text
Build
 ↓
Test
 ↓
Package
 ↓
Ready for Production
 ↓
Approval
 ↓
Deploy
```

---

# Continuous Deployment

Continuous Deployment automatically releases validated changes to production.

```text
Code
 ↓
Build
 ↓
Test
 ↓
Validate
 ↓
Deploy
```

No manual production approval is necessarily required.

---

# Continuous Delivery vs Continuous Deployment

| Continuous Delivery | Continuous Deployment |
|---|---|
| Production-ready | Automatically deployed |
| May require approval | No manual approval required for normal changes |
| Controlled release | Fully automated release |
| Common in regulated environments | Common in highly automated environments |

---

# Kubernetes CI/CD Architecture

```text
                    Developer
                        │
                        ▼
                  Source Control
                        │
                        ▼
                       CI
             ┌──────────┼──────────┐
             ▼          ▼          ▼
           Build       Test       Scan
             │          │          │
             └──────────┼──────────┘
                        ▼
                  Container Image
                        │
                        ▼
                  Image Registry
                        │
                        ▼
               Deployment Config
                        │
                        ▼
                 GitOps / CD
                        │
                        ▼
                   Kubernetes
                        │
                        ▼
              Verification / Tests
                        │
                        ▼
                  Monitoring
```

---

# Why CI/CD With Kubernetes?

Kubernetes environments are dynamic.

Applications may need frequent:

```text
Deployments
Updates
Scaling
Configuration Changes
Security Patches
```

Manual deployment does not scale efficiently.

---

# Manual Deployment

Example:

```bash
kubectl apply -f deployment.yaml
```

Problems at scale:

```text
Manual Errors
Poor Auditability
Configuration Drift
Inconsistent Environments
Slow Releases
```

---

# Automated Deployment

```text
Git Commit
 ↓
Pipeline
 ↓
Validation
 ↓
Deployment
 ↓
Verification
```

This makes the process repeatable.

---

# CI/CD Pipeline Stages

A common pipeline:

```text
1. Checkout
2. Install Dependencies
3. Lint
4. Unit Test
5. Build
6. Security Scan
7. Container Build
8. Image Scan
9. Push Image
10. Update Deployment
11. Deploy
12. Smoke Test
13. Monitor
```

---

# Stage 1 – Checkout

The pipeline retrieves source code.

Example:

```bash
git checkout <commit>
```

---

# Stage 2 – Dependency Installation

Install application dependencies.

Examples:

```bash
npm ci
```

or:

```bash
pip install -r requirements.txt
```

Use deterministic dependency management where possible.

---

# Stage 3 – Linting

Linting detects:

```text
Syntax Problems
Style Issues
Potential Errors
```

---

# Stage 4 – Unit Testing

Unit tests validate individual components.

Example:

```text
Function
 ↓
Input
 ↓
Expected Output
```

---

# Stage 5 – Integration Testing

Integration tests validate interactions between components.

Example:

```text
Application
   ↓
Database
```

---

# Stage 6 – Build

Build the application artifact.

Example:

```text
Source
 ↓
Compiler / Build Tool
 ↓
Artifact
```

---

# Stage 7 – Security Scanning

Scan:

```text
Source Code
Dependencies
Secrets
Container Images
Kubernetes Manifests
```

---

# Stage 8 – Container Build

Example Dockerfile:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]
```

Production images should be minimized and hardened.

---

# Multi-Stage Builds

Multi-stage builds can reduce final image size.

Example:

```dockerfile
FROM node:22 AS builder

WORKDIR /app

COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html
```

The final image contains only what is needed to run the application.

---

# BuildKit

BuildKit provides modern Docker image building capabilities.

Benefits can include:

```text
Caching
Parallel Builds
Secret Handling
Build Efficiency
```

---

# Container Registry

The registry stores container images.

Examples include:

```text
GitHub Container Registry
Amazon ECR
Google Artifact Registry
Azure Container Registry
Harbor
Docker Hub
```

---

# Image Naming

Example:

```text
registry.example.com/team/api:2.4.1
```

Components:

```text
Registry
Repository
Image
Tag
```

---

# Image Tags

Example:

```text
api:1.0.0
api:1.1.0
api:2.0.0
```

Avoid relying exclusively on mutable tags.

---

# Image Digest

An image digest provides a content-addressed identifier.

Example:

```text
sha256:abc123...
```

A digest provides stronger deployment determinism than a mutable tag.

---

# Tag vs Digest

| Tag | Digest |
|---|---|
| Human-friendly | Content-addressed |
| Can be mutable | Identifies exact image content |
| Easy to read | Stronger reproducibility |

---

# Production Recommendation

A deployment may use:

```yaml
image: registry.example.com/api@sha256:<digest>
```

when immutable image references are desired.

---

# Image Scanning

Scan images for:

```text
CVEs
Malware
Misconfigurations
Outdated Packages
```

---

# Vulnerability Severity

Common classifications:

```text
Critical
High
Medium
Low
```

---

# Vulnerability Gate

A pipeline may reject an image containing unacceptable vulnerabilities.

Example:

```text
Critical CVE
    ↓
Pipeline
    ↓
FAIL
```

The exact policy should account for exploitability, exposure, compensating controls, and organizational risk tolerance.

---

# SBOM

SBOM means:

```text
Software Bill of Materials
```

It provides an inventory of software components.

Example:

```text
Application
 ├── OpenSSL
 ├── Python
 ├── Requests
 └── PostgreSQL Driver
```

---

# Why SBOM Matters

SBOMs help with:

```text
Vulnerability Management
Supply-Chain Visibility
Incident Response
License Management
Compliance
```

---

# Image Signing

Image signing helps establish trust in an artifact.

Conceptually:

```text
Build
 ↓
Image
 ↓
Sign
 ↓
Registry
 ↓
Verify
 ↓
Deploy
```

Tools and ecosystems can include:

```text
Cosign
Sigstore
```

---

# Supply-Chain Security

Secure the entire chain:

```text
Source
 ↓
Dependencies
 ↓
Build
 ↓
Artifact
 ↓
Registry
 ↓
Deployment
```

---

# Dependency Security

Dependencies should be:

```text
Tracked
Versioned
Scanned
Updated
Reviewed
```

---

# Dependency Pinning

Prefer controlled versions.

Avoid uncontrolled dependency resolution in production builds.

---

# Kubernetes Manifest Validation

Validate:

```text
YAML
Kubernetes Schema
Security Policy
Resource Configuration
```

---

# Helm Validation

Example:

```bash
helm lint ./chart
```

Render manifests:

```bash
helm template api ./chart
```

---

# Kustomize Validation

Example:

```bash
kubectl kustomize overlays/production
```

Review the generated manifests before deployment.

---

# Kubernetes Dry Run

Example:

```bash
kubectl apply --dry-run=server -f deployment.yaml
```

This can validate the manifest against the Kubernetes API without persisting the change.

---

# Policy as Code

CI can enforce policies before deployment.

Example:

```text
IF privileged = true
THEN FAIL
```

---

# CI/CD Security Gates

Possible gates:

```text
Unit Tests
Security Scan
Dependency Scan
Secret Scan
Image Scan
SBOM
Signature
Policy Validation
Approval
```

---

# Secret Scanning

Detect accidentally committed secrets such as:

```text
API Keys
Cloud Credentials
Passwords
Tokens
Private Keys
```

---

# Never Print Secrets

Avoid:

```bash
echo "$PASSWORD"
```

in CI logs.

---

# CI Secrets

Use the CI platform's secret-management mechanism.

Do not hardcode:

```text
Passwords
Tokens
Private Keys
```

inside pipeline files.

---

# Kubernetes Secrets in CI/CD

CI/CD may need access to:

```text
Registry Credentials
Cloud Credentials
Deployment Credentials
Signing Keys
```

Use short-lived credentials where possible.

---

# Workload Identity

Cloud environments can use workload identity mechanisms instead of long-lived static credentials.

Conceptually:

```text
CI Identity
 ↓
Cloud IAM
 ↓
Temporary Permissions
```

---

# CI Runner Security

CI runners execute potentially untrusted code.

Therefore:

```text
Runner Isolation
+
Least Privilege
+
Ephemeral Runners
+
Network Restrictions
```

can reduce risk.

---

# Self-Hosted Runners

Self-hosted runners provide greater control but also increase security responsibility.

Protect:

```text
Runner Host
Credentials
Network
Cache
Artifacts
```

---

# Pipeline Isolation

Separate workloads when appropriate:

```text
Development Runner
Staging Runner
Production Runner
```

Highly privileged production runners should have especially strong isolation.

---

# Artifact Security

Artifacts should be:

```text
Versioned
Traceable
Scanned
Protected
```

---

# Artifact Promotion

A useful approach is:

```text
Build Once
      ↓
Scan Once
      ↓
Promote Same Artifact
```

instead of rebuilding the application separately for each environment.

---

# Environment Promotion

Typical flow:

```text
Build
 ↓
Dev
 ↓
Test
 ↓
Staging
 ↓
Production
```

---

# Immutable Promotion

Example:

```text
api@sha256:ABC
```

is promoted across:

```text
Dev
 ↓
Staging
 ↓
Production
```

The exact same artifact is deployed.

---

# Deployment Strategies

Common strategies:

```text
Rolling
Blue-Green
Canary
Progressive Delivery
```

---

# Rolling Deployment

```text
v1 v1 v1
 ↓
v1 v1 v2
 ↓
v1 v2 v2
 ↓
v2 v2 v2
```

---

# Blue-Green Deployment

```text
Blue
Current

Green
New
```

Traffic switches from:

```text
Blue → Green
```

---

# Canary Deployment

Start with:

```text
95% → v1
5%  → v2
```

Monitor the new version.

Increase gradually if healthy.

---

# Progressive Delivery

A deployment can progress through stages:

```text
5%
 ↓
10%
 ↓
25%
 ↓
50%
 ↓
100%
```

Each stage can have automated health checks.

---

# Deployment Gates

A gate prevents deployment until a condition is satisfied.

Examples:

```text
Tests Passed
Security Scan Passed
Approval Received
Error Rate Acceptable
Latency Acceptable
```

---

# Manual Approval

Production deployment may require:

```text
Engineer Approval
Security Approval
Change Management Approval
```

depending on organizational requirements.

---

# Automated Approval

Automated gates can evaluate:

```text
Tests
Metrics
Security
Policies
```

---

# Deployment Verification

After deployment verify:

```text
Pods
Services
Endpoints
Health
Metrics
Logs
Errors
Latency
```

---

# Smoke Tests

Smoke tests validate basic functionality.

Example:

```text
GET /health
```

Expected:

```text
HTTP 200
```

---

# Health Check Pipeline

```text
Deploy
 ↓
Wait
 ↓
Readiness
 ↓
Smoke Test
 ↓
Metrics
 ↓
Success / Rollback
```

---

# Automated Rollback

A pipeline may roll back when:

```text
Error Rate ↑
Latency ↑
Availability ↓
Pods Failing
Health Checks Failing
```

---

# Kubernetes Rollout Status

```bash
kubectl rollout status deployment/api
```

---

# Kubernetes Rollback

```bash
kubectl rollout undo deployment/api
```

However, in a GitOps-managed environment, the desired configuration should also be updated in Git to avoid reintroducing the failed state.

---

# GitOps Integration

A modern CI/CD architecture may separate:

```text
CI
```

from:

```text
CD
```

CI builds the artifact.

GitOps performs deployment.

```text
Source Code
    ↓
CI
    ↓
Image
    ↓
Registry
    ↓
GitOps Repository
    ↓
Argo CD / Flux
    ↓
Kubernetes
```

---

# CI Updates GitOps Repository

Example:

```text
Build Image
 ↓
Push Image
 ↓
Update image digest in Git
 ↓
Pull Request
 ↓
Review
 ↓
Merge
 ↓
GitOps Sync
```

---

# Why Separate CI and CD?

Benefits include:

```text
Clear Responsibilities
Better Auditability
Reduced Cluster Credentials in CI
Git-Based Deployment History
Improved Security
```

---

# GitHub Actions

GitHub Actions can automate CI/CD workflows.

Conceptual workflow:

```text
Push
 ↓
Build
 ↓
Test
 ↓
Scan
 ↓
Build Image
 ↓
Push Registry
 ↓
Update GitOps
```

---

# GitLab CI

GitLab CI provides pipeline automation using configuration files such as:

```text
.gitlab-ci.yml
```

---

# Jenkins

Jenkins is a widely used automation server.

Typical flow:

```text
Jenkins
 ↓
Build
 ↓
Test
 ↓
Scan
 ↓
Deploy
```

---

# Tekton

Tekton provides Kubernetes-native CI/CD building blocks.

Conceptually:

```text
Pipeline
 ↓
Tasks
 ↓
Containers
 ↓
Results
```

---

# CI/CD Tool Comparison

| Tool | Primary Strength |
|---|---|
| GitHub Actions | GitHub-integrated automation |
| GitLab CI | Integrated DevSecOps platform |
| Jenkins | Highly extensible automation |
| Tekton | Kubernetes-native pipelines |
| Argo CD | GitOps CD |
| Flux | GitOps reconciliation |

These tools can be combined rather than treated as direct substitutes.

---

# CI vs GitOps CD

```text
CI:
Code
 ↓
Build
 ↓
Test
 ↓
Scan
 ↓
Image

GitOps CD:
Image
 ↓
Deployment Configuration
 ↓
Reconciliation
 ↓
Kubernetes
```

---

# Production CI/CD Architecture

```text
                       Developer
                           │
                           ▼
                         Git
                           │
                    Pull Request
                           │
                           ▼
                          CI
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
      Tests              SAST             Dependency
                                             Scan
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                    Container Build
                           │
                           ▼
                     Image Scan
                           │
                           ▼
                         SBOM
                           │
                           ▼
                       Sign Image
                           │
                           ▼
                     Image Registry
                           │
                           ▼
                   GitOps Repository
                           │
                     Pull Request
                           │
                           ▼
                    Argo CD / Flux
                           │
                           ▼
                      Kubernetes
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
           Health        Metrics       Logs
              │            │            │
              └────────────┼────────────┘
                           ▼
                       Monitoring
```

---

# Production CI/CD Security

Use:

```text
Least Privilege
+
Secret Management
+
Ephemeral Credentials
+
Runner Isolation
+
Artifact Signing
+
Image Scanning
+
Policy Enforcement
```

---

# Kubernetes Deployment Credentials

Avoid giving CI unrestricted:

```text
cluster-admin
```

access.

Prefer:

```text
GitOps
```

or narrowly scoped deployment identities.

---

# RBAC for CI/CD

Define permissions based on what the pipeline needs.

Example:

```text
Read:
Deployments
Pods
Services

Write:
Specific Deployment Resources
```

Avoid unnecessary access to:

```text
Secrets
RBAC
Nodes
Cluster Configuration
```

---

# Admission Control

Even if CI passes, Kubernetes admission policies can provide another security layer.

```text
CI
 ↓
Admission
 ↓
Kubernetes
```

---

# Defense in Depth

A secure pipeline should not depend on one security control.

Example:

```text
Developer Review
      ↓
CI Security Scan
      ↓
Image Verification
      ↓
Policy Validation
      ↓
Admission Control
      ↓
Runtime Security
```

---

# Compliance

CI/CD can provide evidence of:

```text
Change Approval
Testing
Security Scanning
Deployment History
Artifact Traceability
```

---

# Audit Trail

A strong pipeline can answer:

```text
Who Changed It?
What Changed?
When?
Which Commit?
Which Image?
Which Tests?
Who Approved?
Which Environment?
When Was It Deployed?
```

---

# Deployment Metadata

Record:

```text
Git Commit
Image Digest
Build Number
Pipeline ID
Environment
Deployment Time
```

---

# Observability in CI/CD

Track:

```text
Deployment Frequency
Lead Time
Change Failure Rate
Mean Time to Recovery
```

These are commonly used software delivery performance indicators.

---

# Deployment Frequency

Measures how frequently production deployments occur.

---

# Lead Time for Changes

Measures the time between:

```text
Code Change
```

and:

```text
Production Deployment
```

---

# Change Failure Rate

Measures how often deployments cause failures requiring remediation.

---

# Mean Time to Recovery

Measures how quickly service is restored after an incident.

---

# DORA Metrics

Common software delivery performance metrics include:

```text
Deployment Frequency
Lead Time for Changes
Change Failure Rate
Time to Restore Service
```

These metrics should be interpreted in context rather than optimized blindly.

---

# Notifications

Notify appropriate teams for:

```text
Pipeline Failure
Security Failure
Deployment Failure
Rollback
Production Deployment
```

---

# Pipeline Failure Handling

If tests fail:

```text
Stop Pipeline
 ↓
Report Failure
 ↓
Fix
 ↓
Retry
```

Do not deploy a failed build simply to keep the pipeline green.

---

# Deployment Failure

```text
Deployment
 ↓
Health Check
 ↓
Failure
 ↓
Rollback
 ↓
Alert
 ↓
Investigation
```

---

# Failed Build

A failed build should prevent downstream deployment stages.

---

# Failed Security Scan

Depending on policy:

```text
Critical Finding
 ↓
Block
```

or:

```text
Finding
 ↓
Exception Workflow
 ↓
Approved Risk
 ↓
Continue
```

---

# Pipeline Caching

Caching can improve build speed.

Examples:

```text
Dependency Cache
Docker Build Cache
Package Cache
```

But caches should not be trusted blindly.

Consider:

```text
Integrity
Isolation
Poisoning
Expiration
```

---

# Dependency Lock Files

Use lock files where supported.

Examples:

```text
package-lock.json
poetry.lock
requirements lock mechanisms
```

This improves reproducibility.

---

# Reproducible Builds

A reproducible build should produce the same artifact from the same source and controlled build inputs.

Important factors:

```text
Pinned Dependencies
Controlled Build Environment
Deterministic Inputs
Immutable Artifacts
```

---

# Build Once, Promote Many

Preferred architecture:

```text
Source
 ↓
Build Once
 ↓
Image
 ↓
Scan
 ↓
Sign
 ↓
Dev
 ↓
Staging
 ↓
Production
```

Avoid rebuilding the image independently for every environment.

---

# Environment Configuration

Environment differences should usually be represented through configuration.

Example:

```text
Same Image
+
Different Configuration
```

---

# Example

Development:

```text
replicas: 1
```

Production:

```text
replicas: 5
```

But:

```text
Image:
api@sha256:ABC
```

can remain identical.

---

# Deployment Manifests

Keep manifests:

```text
Versioned
Reviewed
Validated
Secure
```

---

# Helm Best Practices

Use:

```text
Versioned Charts
Values Per Environment
Schema Validation
Linting
Controlled Dependencies
```

---

# Kustomize Best Practices

Use:

```text
Reusable Base
Environment Overlays
Small Patches
Clear Structure
```

---

# CI/CD and GitOps Combined

Recommended architecture:

```text
               Application Repository
                       │
                       ▼
                      CI
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
     Test            Scan            Build
       │               │               │
       └───────────────┼───────────────┘
                       ▼
                 Container Image
                       │
                       ▼
                    Registry
                       │
                       ▼
               GitOps Repository
                       │
                  Pull Request
                       │
                       ▼
                Argo CD / Flux
                       │
                       ▼
                  Kubernetes
```

---

# Common Mistakes

## 1. Deploying Directly From CI With Cluster Admin

This creates unnecessary risk.

---

## 2. Hardcoding Secrets

Never place production credentials directly in pipeline files.

---

## 3. Using Mutable Image Tags

Tags such as:

```text
latest
```

can make deployments unpredictable.

---

## 4. Rebuilding for Every Environment

This can result in different artifacts being tested and deployed.

Prefer:

```text
Build Once
Promote Same Artifact
```

---

## 5. Skipping Tests

A fast deployment is useless if it frequently breaks production.

---

## 6. Ignoring Security Scanning

CI should identify security issues before deployment.

---

## 7. No Rollback

Production deployment must have a recovery strategy.

---

## 8. No Deployment Verification

A successful pipeline does not necessarily mean the application is healthy.

---

## 9. Overly Privileged Runners

Compromised CI runners can become a major security risk.

---

## 10. No Pipeline Isolation

Sensitive environments should have appropriate isolation.

---

## 11. No Artifact Traceability

Always know:

```text
Source Commit
→
Build
→
Image
→
Deployment
```

---

## 12. Treating Security Gates as Optional

Critical security controls should not be bypassed casually.

---

## 13. No Admission Controls

CI can fail to catch runtime or configuration changes. Kubernetes admission provides another enforcement layer.

---

## 14. No Monitoring After Deployment

Deployment is not the end of the pipeline.

---

# Best Practices

### 1. Automate Testing

Every important change should be validated automatically.

---

### 2. Build Immutable Artifacts

Use:

```text
Versioned Images
+
Digests
```

---

### 3. Scan Before Deployment

Scan:

```text
Dependencies
Images
Manifests
Secrets
```

---

### 4. Use GitOps for Kubernetes CD

Separate:

```text
Build
```

from:

```text
Deployment Reconciliation
```

where appropriate.

---

### 5. Minimize CI Credentials

Use short-lived identities and narrowly scoped permissions.

---

### 6. Protect Production

Use:

```text
Reviews
Approvals
Policy
RBAC
Admission
```

---

### 7. Verify Deployments

Use:

```text
Smoke Tests
Health Checks
Metrics
Logs
```

---

### 8. Automate Rollbacks Carefully

Define explicit rollback conditions.

---

### 9. Track Delivery Metrics

Monitor:

```text
Deployment Frequency
Lead Time
Change Failure Rate
Recovery Time
```

---

### 10. Secure the Entire Supply Chain

Protect:

```text
Source
Dependencies
Build
Artifacts
Registry
Deployment
```

---

# Hands-on Lab 1 – Basic CI Pipeline

Create a simple application repository.

Pipeline stages:

```text
Checkout
 ↓
Install
 ↓
Test
 ↓
Build
```

---

# Hands-on Lab 2 – Container Build

Create a Dockerfile.

Build:

```bash
docker build -t example/api:1.0.0 .
```

Run locally:

```bash
docker run --rm -p 8080:8080 example/api:1.0.0
```

---

# Hands-on Lab 3 – Container Registry

Push an image to a test registry.

Verify:

```text
Repository
Tag
Digest
```

---

# Hands-on Lab 4 – Image Scanning

Scan the container image.

Identify:

```text
Critical
High
Medium
Low
```

vulnerabilities.

Create a policy for acceptable risk.

---

# Hands-on Lab 5 – SBOM

Generate an SBOM for the application image.

Review:

```text
Packages
Versions
Dependencies
```

---

# Hands-on Lab 6 – Kubernetes Manifest Validation

Validate a Deployment:

```bash
kubectl apply --dry-run=server -f deployment.yaml
```

---

# Hands-on Lab 7 – Helm CI

Create a Helm chart.

Run:

```bash
helm lint ./chart
```

Render:

```bash
helm template api ./chart
```

Validate the generated manifests.

---

# Hands-on Lab 8 – Kustomize CI

Create:

```text
base/
overlays/dev/
overlays/production/
```

Render:

```bash
kubectl kustomize overlays/production
```

---

# Hands-on Lab 9 – CI to Registry

Build a pipeline:

```text
Git Push
 ↓
Test
 ↓
Build Image
 ↓
Scan
 ↓
Push Registry
```

---

# Hands-on Lab 10 – CI With GitOps

Build:

```text
Source Repository
 ↓
CI
 ↓
Image
 ↓
Registry
 ↓
Update GitOps Repository
 ↓
Argo CD
 ↓
Kubernetes
```

---

# Hands-on Lab 11 – Deployment Verification

After deployment:

```text
Check Rollout
 ↓
Check Pods
 ↓
Run Smoke Test
 ↓
Check Metrics
```

---

# Hands-on Lab 12 – Automated Rollback

Deploy a working version.

Then deploy an intentionally broken version.

Detect:

```text
Health Failure
```

and execute a controlled rollback.

---

# Hands-on Lab 13 – Security Gate

Configure a pipeline to reject:

```text
Critical Vulnerability
```

or another defined policy violation.

---

# Hands-on Lab 14 – Secret Scanning

Commit a test secret in a disposable repository.

Run a secret-scanning tool.

Verify that the pipeline detects it.

Immediately remove and rotate the test credential.

---

# Hands-on Lab 15 – Image Signing

Build an image.

Sign it using an appropriate signing tool.

Verify the signature before deployment.

---

# Hands-on Lab 16 – Policy as Code

Create a policy:

```text
Reject privileged containers.
```

Run it against Kubernetes manifests during CI.

---

# Hands-on Lab 17 – Canary Deployment

Deploy:

```text
v1 = 95%
v2 = 5%
```

Monitor:

```text
Latency
Errors
Availability
```

Progressively increase traffic.

---

# Hands-on Lab 18 – Production Approval

Create a pipeline:

```text
Dev
 ↓
Automated Tests
 ↓
Staging
 ↓
Approval
 ↓
Production
```

---

# Hands-on Lab 19 – DORA Metrics

Collect:

```text
Deployment Frequency
Lead Time
Change Failure Rate
Recovery Time
```

Analyze the results.

---

# Hands-on Lab 20 – Complete CI/CD Platform

Build:

```text
Developer
 ↓
Git
 ↓
Pull Request
 ↓
CI
 ├── Unit Tests
 ├── SAST
 ├── Dependency Scan
 ├── Secret Scan
 ├── Build
 ├── Image Scan
 ├── SBOM
 └── Sign
 ↓
Registry
 ↓
GitOps Repository
 ↓
Argo CD / Flux
 ↓
Kubernetes
 ↓
Smoke Test
 ↓
Monitoring
 ↓
Alert / Rollback
```

---

# Quick Revision

## CI

```text
Continuously integrate and validate code changes
```

---

## Continuous Delivery

```text
Keep software deployable and production-ready
```

---

## Continuous Deployment

```text
Automatically deploy validated changes
```

---

## Container Registry

```text
Stores container images
```

---

## Image Digest

```text
Content-addressed identifier for an image
```

---

## SBOM

```text
Software Bill of Materials
```

---

## Image Signing

```text
Mechanism for establishing artifact authenticity and integrity
```

---

## GitOps

```text
Git-based desired state + continuous reconciliation
```

---

## Deployment Gate

```text
Condition that must pass before continuing
```

---

## Smoke Test

```text
Basic test confirming that the deployment works
```

---

## Rollback

```text
Return to a known-good application version or desired state
```

---

## DORA Metrics

```text
Deployment Frequency
Lead Time for Changes
Change Failure Rate
Time to Restore Service
```

---

# Essential Commands

Git status:

```bash
git status
```

Git log:

```bash
git log --oneline
```

Build image:

```bash
docker build -t example/api:1.0.0 .
```

List images:

```bash
docker images
```

Push image:

```bash
docker push example/api:1.0.0
```

Inspect image:

```bash
docker inspect example/api:1.0.0
```

Helm lint:

```bash
helm lint ./chart
```

Helm render:

```bash
helm template api ./chart
```

Kustomize render:

```bash
kubectl kustomize overlays/production
```

Validate Kubernetes configuration:

```bash
kubectl apply --dry-run=server -f deployment.yaml
```

Deploy:

```bash
kubectl apply -f deployment.yaml
```

Check rollout:

```bash
kubectl rollout status deployment/api
```

View rollout history:

```bash
kubectl rollout history deployment/api
```

Rollback:

```bash
kubectl rollout undo deployment/api
```

Check Pods:

```bash
kubectl get pods -A
```

Check services:

```bash
kubectl get svc -A
```

Check events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

View logs:

```bash
kubectl logs <pod>
```

View previous logs:

```bash
kubectl logs <pod> --previous
```

Check resources:

```bash
kubectl top pods -A
```

---

# Interview Questions

## Basic

- What is CI/CD?
- What is Continuous Integration?
- What is Continuous Delivery?
- What is Continuous Deployment?
- What is the difference between Continuous Delivery and Continuous Deployment?
- Why is CI/CD important for Kubernetes?
- What is a container registry?
- What is an image tag?
- What is an image digest?
- What is an SBOM?
- What is image signing?
- What is a deployment gate?
- What is a smoke test?
- What is a rollback?
- What is GitOps?

---

## Intermediate

- How would you design a CI/CD pipeline for Kubernetes?
- What stages should a Kubernetes CI pipeline contain?
- How do you secure container images?
- How do you scan images for vulnerabilities?
- Why should images be immutable?
- Why is Build Once, Promote Many useful?
- How do you integrate CI with GitOps?
- How do you manage secrets in CI/CD?
- How do you secure CI runners?
- What is the role of RBAC in CI/CD?
- How do you implement automated rollback?
- How do you validate Kubernetes manifests in CI?
- How do you use Helm in CI/CD?
- How do you use Kustomize in CI/CD?
- How do you implement canary deployments?

---

## Advanced

- Design a secure Kubernetes CI/CD architecture.
- How would you implement CI/CD for multiple Kubernetes clusters?
- How would you secure the complete software supply chain?
- How would you prevent compromised CI credentials from accessing production?
- How would you implement artifact signing and verification?
- How would you design a Build Once, Promote Many pipeline?
- How would you integrate policy as code into CI/CD?
- How would you design automated rollback based on production metrics?
- How would you implement GitOps with CI/CD?
- How would you design CI/CD for a regulated production environment?
- How would you secure self-hosted CI runners?
- How would you design progressive delivery for Kubernetes?

---

# Interview Scenario 1

### Question

> What should happen when a developer pushes code to Git?

### Answer

A typical pipeline is:

```text
Git Push
 ↓
Build
 ↓
Unit Tests
 ↓
Security Scans
 ↓
Container Build
 ↓
Image Scan
 ↓
SBOM
 ↓
Image Signing
 ↓
Push Registry
 ↓
Update GitOps Configuration
 ↓
Deployment
```

---

# Interview Scenario 2

### Question

> Why should you not give CI `cluster-admin`?

### Answer

Because compromise of the CI pipeline could result in complete cluster compromise.

Instead:

```text
Least Privilege
+
Scoped RBAC
+
Short-Lived Credentials
+
GitOps
```

should be preferred.

---

# Interview Scenario 3

### Question

> Why is Build Once, Promote Many better?

### Answer

It ensures that the same tested artifact moves through:

```text
Development
 ↓
Staging
 ↓
Production
```

rather than rebuilding potentially different artifacts for each environment.

This improves:

```text
Consistency
Traceability
Reproducibility
```

---

# Interview Scenario 4

### Question

> How would you automatically rollback a bad deployment?

### Answer

Use:

```text
Deployment
 ↓
Health Checks
 ↓
Metrics
 ↓
Error Detection
 ↓
Rollback
 ↓
Alert
```

For GitOps environments, the desired state in Git should also be corrected so the failed configuration is not immediately reapplied.

---

# Interview Scenario 5

### Question

> How do you secure a container image pipeline?

### Answer

Use:

```text
Trusted Source
+
Dependency Scanning
+
Minimal Base Image
+
Image Scanning
+
SBOM
+
Image Signing
+
Immutable Digest
+
Admission Verification
```

---

# Interview Scenario 6

### Question

> How would you deploy the same image to development, staging, and production?

### Answer

Build once:

```text
api@sha256:ABC
```

Then promote the same digest:

```text
Dev
 ↓
Staging
 ↓
Production
```

Environment-specific configuration can change independently.

---

# Interview Scenario 7

### Question

> How do you prevent secrets from leaking through CI logs?

### Answer

Use:

```text
CI Secret Store
+
Masked Variables
+
Short-Lived Credentials
+
No Secret Echoing
+
Restricted Logs
```

Also scan source and artifacts for accidentally exposed credentials.

---

# Interview Scenario 8

### Question

> How do you verify that a Kubernetes deployment actually succeeded?

### Answer

I would not rely only on a successful `kubectl apply`.

I would verify:

```text
Rollout
 ↓
Pod Readiness
 ↓
Service
 ↓
Smoke Test
 ↓
Metrics
 ↓
Logs
 ↓
Error Rate
```

---

# Interview Scenario 9

### Question

> How would you design Kubernetes CI/CD for production?

### Answer

```text
Developer
 ↓
Pull Request
 ↓
Code Review
 ↓
CI
 ├── Tests
 ├── SAST
 ├── Dependency Scan
 ├── Secret Scan
 ├── Build
 ├── Image Scan
 ├── SBOM
 └── Signing
 ↓
Registry
 ↓
GitOps Repository
 ↓
Approval
 ↓
Argo CD / Flux
 ↓
Kubernetes
 ↓
Deployment Verification
 ↓
Monitoring
 ↓
Rollback if Required
```

---

# Production CI/CD Checklist

```text
☑ Source control protected
☑ Pull requests required
☑ Code review enabled
☑ Unit tests automated
☑ Integration tests automated
☑ Security scans enabled
☑ Dependency scanning enabled
☑ Secret scanning enabled
☑ Container images scanned
☑ SBOM generated
☑ Images signed where required
☑ Immutable image references used
☑ Build artifacts traceable
☑ Registry protected
☑ CI secrets protected
☑ CI runners isolated
☑ Least-privilege RBAC configured
☑ Kubernetes manifests validated
☑ Helm/Kustomize validation enabled
☑ Policy as Code enabled
☑ GitOps integrated where appropriate
☑ Production approval configured
☑ Deployment verification enabled
☑ Smoke tests implemented
☑ Monitoring enabled
☑ Automated rollback tested
☑ Notifications configured
☑ Audit trail retained
☑ Disaster recovery considered
☑ DORA metrics tracked
☑ Production deployment process documented
```

---

# Chapter Summary

CI/CD automates the path from source code to production.

A secure Kubernetes CI/CD lifecycle is:

```text
Code
 ↓
Review
 ↓
Test
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
GitOps
 ↓
Kubernetes
 ↓
Verify
 ↓
Monitor
 ↓
Rollback if Required
```

The most important production principles are:

```text
Build Once
+
Promote the Same Artifact
+
Use Immutable Images
+
Scan Everything Important
+
Protect CI Credentials
+
Use Least Privilege
+
Separate CI From Cluster Deployment Where Appropriate
+
Use GitOps for Reconciliation
+
Verify Deployments
+
Automate Safe Rollbacks
```

A mature Kubernetes CI/CD system is not merely a deployment script. It is a secure software delivery system connecting:

```text
Development
+
Security
+
Operations
+
Kubernetes
+
Governance
```

The most important principle is:

> **Build and validate immutable artifacts through a secure CI pipeline, promote the same trusted artifact across environments, use controlled deployment mechanisms such as GitOps, verify production health automatically, and maintain a complete audit trail from source commit to running workload.**

---

## Next Chapter

# Chapter 80 – Helm

Topics will include:

- Helm Fundamentals
- What Is Helm?
- Why Helm?
- Helm Architecture
- Helm CLI
- Helm Charts
- Chart Structure
- Chart.yaml
- values.yaml
- templates/
- templates/_helpers.tpl
- charts/
- crds/
- README
- LICENSE
- Helm Releases
- Helm Repositories
- Helm Registry
- Helm Installation
- Helm Upgrade
- Helm Rollback
- Helm Uninstall
- Helm History
- Helm Status
- Helm List
- Helm Values
- Default Values
- Custom Values
- Value Precedence
- Helm Templates
- Go Templates
- Template Functions
- Pipelines
- Conditionals
- Loops
- Variables
- Named Templates
- Helpers
- `include`
- `required`
- `default`
- `lookup`
- `tpl`
- `toYaml`
- `nindent`
- `with`
- `range`
- `if`
- Chart Dependencies
- Subcharts
- Library Charts
- Helm Hooks
- Helm Tests
- Helm Upgrade Strategies
- Helm Rollbacks
- Helm Secrets
- Helm Security
- OCI Registries
- Chart Signing
- Provenance
- Helm Lint
- Helm Template
- Helm Diff
- Helm with Kubernetes
- Helm with GitOps
- Helm with Argo CD
- Helm with Flux
- Helm with CI/CD
- Environment Management
- Production Helm
- Helm Best Practices
- Common Mistakes
- Hands-on Labs
- Quick Revision
- Interview Questions
- References

---