# Chapter 78 – GitOps

## Overview

GitOps is an operational model where Git repositories act as the source of truth for declarative infrastructure and application configuration.

Instead of manually changing Kubernetes resources:

```text
Engineer
   ↓
kubectl apply
   ↓
Kubernetes
```

GitOps uses:

```text
Developer
   ↓
Git Commit
   ↓
Pull Request
   ↓
Review
   ↓
Git Repository
   ↓
GitOps Controller
   ↓
Kubernetes
```

The GitOps controller continuously compares:

```text
Desired State
      vs
Actual State
```

and reconciles the cluster toward the desired state.

A simplified GitOps lifecycle is:

```text
Define
  ↓
Commit
  ↓
Review
  ↓
Validate
  ↓
Merge
  ↓
Reconcile
  ↓
Deploy
  ↓
Observe
  ↓
Detect Drift
  ↓
Self-Heal / Remediate
```

Popular Kubernetes GitOps tools include:

```text
Argo CD
Flux
```

---

# Learning Objectives

After completing this chapter, you will understand:

- GitOps fundamentals
- What GitOps means
- GitOps principles
- Git as the source of truth
- Declarative infrastructure
- Desired state
- Actual state
- Reconciliation
- Continuous delivery
- GitOps vs traditional CI/CD
- GitOps architecture
- GitOps workflow
- Kubernetes and GitOps
- Git repository structure
- Environment management
- Development
- Staging
- Production
- Configuration management
- Secrets with GitOps
- Sealed Secrets
- External Secrets
- Helm with GitOps
- Kustomize with GitOps
- Argo CD
- Flux
- Argo CD architecture
- Flux architecture
- Applications
- ApplicationSets
- Sync
- Auto-Sync
- Manual Sync
- Health status
- Drift detection
- Self-healing
- Rollback
- Progressive delivery
- Canary deployments
- Blue-green deployments
- GitOps security
- RBAC
- Repository security
- Commit signing
- Image verification
- Supply-chain security
- Policy as Code
- CI integration
- Pull Requests
- Change management
- Auditability
- Compliance
- Multi-cluster GitOps
- Multi-environment GitOps
- Monorepo vs multi-repo
- Branching strategies
- Repository layout
- Deployment promotion
- Disaster recovery
- GitOps observability
- Notifications
- Troubleshooting
- Production best practices
- Common mistakes
- Hands-on labs
- Quick revision
- Interview questions

---

# What Is GitOps?

GitOps is a way of managing infrastructure and applications using:

```text
Git
+
Declarative Configuration
+
Automated Reconciliation
```

The desired state is stored in Git.

Example:

```yaml
replicas: 3
image: myapp:v2.0.0
```

GitOps continuously attempts to make the Kubernetes cluster match that state.

---

# Declarative vs Imperative

## Imperative

You tell Kubernetes what action to perform.

Example:

```bash
kubectl scale deployment api --replicas=5
```

This describes an action.

---

## Declarative

You describe the desired state.

Example:

```yaml
spec:
  replicas: 5
```

Kubernetes determines the actions required to reach that state.

---

# GitOps Is Declarative

GitOps primarily uses declarative configuration.

Example:

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: api
spec:
  replicas: 3
```

Git stores the desired configuration.

---

# Desired State

Desired state means:

```text
What the system should look like.
```

Example:

```text
3 API Pods
Image v2
2 CPU
4Gi Memory
```

---

# Actual State

Actual state means:

```text
What is currently running.
```

Example:

```text
2 API Pods
Image v1
```

---

# Reconciliation

The GitOps controller continuously compares:

```text
Desired State
      ↓
Git
      │
      │ Compare
      ▼
Actual State
      ↓
Kubernetes
```

If they differ:

```text
Drift Detected
      ↓
Reconcile
      ↓
Cluster Updated
```

---

# GitOps Reconciliation

```text
             Git Repository
                   │
                   ▼
             Desired State
                   │
                   ▼
            GitOps Controller
                   │
              Compare State
                   │
          ┌────────┴────────┐
          ▼                 ▼
       In Sync             Drift
          │                 │
          │                 ▼
          │              Reconcile
          │                 │
          └────────┬────────┘
                   ▼
               Kubernetes
```

---

# Git as the Source of Truth

Git can contain:

```text
Deployments
Services
ConfigMaps
Namespaces
NetworkPolicies
RBAC
Helm Values
Kustomize Overlays
Policies
```

---

# Why Git?

Git provides:

```text
Version History
Code Review
Audit Trail
Rollback
Branching
Collaboration
Access Control
```

---

# GitOps Principles

Common GitOps principles include:

```text
Declarative
Versioned
Immutable
Pulled Automatically
Continuously Reconciled
```

---

# Principle 1 – Declarative

Describe the desired state rather than manually executing every operational step.

---

# Principle 2 – Versioned

Configuration should be stored in version control.

---

# Principle 3 – Immutable History

Git provides a history of changes.

Example:

```text
Commit A
   ↓
Commit B
   ↓
Commit C
```

---

# Principle 4 – Automated Delivery

A GitOps controller can automatically apply approved desired state.

---

# Principle 5 – Continuous Reconciliation

The controller continuously works to keep the cluster aligned with Git.

---

# Traditional CI/CD

A traditional pipeline may look like:

```text
Developer
   ↓
Git
   ↓
CI
   ↓
Build
   ↓
Test
   ↓
Deploy
   ↓
Kubernetes
```

---

# GitOps CI/CD

GitOps separates application build from deployment state.

```text
Developer
   ↓
Git
   ↓
CI
   ↓
Build Image
   ↓
Update Deployment Repository
   ↓
Git
   ↓
GitOps Controller
   ↓
Kubernetes
```

---

# Push vs Pull

Traditional deployment often uses:

```text
CI/CD
   ↓
Push
   ↓
Kubernetes
```

GitOps generally uses:

```text
GitOps Controller
   ↑
Pull
   │
Git
```

The controller runs inside or has access to the cluster and pulls desired state.

---

# GitOps Architecture

```text
                    Developer
                        │
                        ▼
                  Git Repository
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
             CI                Review
              │                   │
              └─────────┬─────────┘
                        ▼
                 Desired State
                        │
                        ▼
                 GitOps Controller
                        │
                        ▼
                   Kubernetes
                        │
                  ┌─────┴─────┐
                  ▼           ▼
               Workloads   Services
```

---

# Application Repository

Application source code may be stored separately:

```text
application-repo
```

Example:

```text
src/
Dockerfile
tests/
package.json
```

---

# Configuration Repository

GitOps manifests can be stored separately:

```text
platform-config/
```

Example:

```text
apps/
clusters/
environments/
policies/
```

---

# Separation of Concerns

A common architecture:

```text
Application Repository
        │
        ▼
       CI
        │
        ▼
   Container Image
        │
        ▼
Configuration Repository
        │
        ▼
    GitOps
        │
        ▼
   Kubernetes
```

---

# Repository Structure

Example:

```text
gitops-repo/
├── apps/
│   ├── api/
│   ├── frontend/
│   └── worker/
│
├── environments/
│   ├── dev/
│   ├── staging/
│   └── production/
│
├── clusters/
│   ├── dev-cluster/
│   └── prod-cluster/
│
├── policies/
└── README.md
```

---

# Monorepo

One repository contains multiple applications and environments.

Example:

```text
gitops/
├── app1/
├── app2/
├── app3/
├── dev/
├── staging/
└── production/
```

---

# Advantages of Monorepo

```text
Centralized Visibility
Shared Standards
Simpler Cross-Application Changes
```

---

# Disadvantages of Monorepo

Potential challenges:

```text
Large Repository
Complex Permissions
Large Change Surface
```

---

# Multi-Repo

Separate repositories may be used for:

```text
Application
Infrastructure
Environment
Security Policies
Platform Configuration
```

---

# Advantages of Multi-Repo

```text
Isolation
Independent Permissions
Smaller Repositories
Team Ownership
```

---

# Disadvantages of Multi-Repo

Potential challenges:

```text
Cross-Repository Coordination
More Administration
Version Synchronization
```

---

# Environment Management

Common environments:

```text
Development
Staging
Production
```

---

# Development

Used for:

```text
Rapid Changes
Testing
Experimentation
```

---

# Staging

Used for:

```text
Production-Like Validation
Integration Testing
Release Validation
```

---

# Production

Used for:

```text
Customer Workloads
High Availability
Strict Change Control
```

---

# Environment Promotion

A common flow:

```text
Development
     ↓
Testing
     ↓
Staging
     ↓
Production
```

---

# Promotion by Git Commit

Example:

```text
dev
image: app:v2.1.0
```

After testing:

```text
staging
image: app:v2.1.0
```

Then:

```text
production
image: app:v2.1.0
```

---

# Branch-Based Environments

An organization may use:

```text
main
develop
release
```

However, GitOps does not require a specific branching strategy.

---

# Directory-Based Environments

Another approach:

```text
environments/
├── dev/
├── staging/
└── production/
```

This can make environment differences explicit.

---

# Kustomize

Kustomize allows environment-specific overlays.

Example:

```text
base/
├── deployment.yaml
├── service.yaml
└── kustomization.yaml

overlays/
├── dev/
├── staging/
└── production/
```

---

# Kustomize Flow

```text
Base
 ↓
Overlay
 ↓
Environment Configuration
 ↓
Kubernetes Manifest
```

---

# Helm

Helm packages Kubernetes applications into charts.

GitOps controllers can manage Helm releases declaratively.

Example:

```text
Helm Chart
   +
Values
   ↓
GitOps
   ↓
Kubernetes
```

---

# Helm Values

Example:

```yaml
replicaCount: 3

image:
  repository: example/api
  tag: "2.1.0"
```

---

# GitOps With Helm

```text
Git
 ↓
Helm Values
 ↓
GitOps Controller
 ↓
Helm
 ↓
Kubernetes
```

---

# Secrets in GitOps

Never store plaintext production credentials in Git.

Bad:

```yaml
password: SuperSecret123
```

---

# Secret Management Options

Consider:

```text
External Secret Manager
Sealed Secrets
SOPS
Cloud KMS
Vault
```

The appropriate mechanism depends on the environment.

---

# Sealed Secrets

Sealed Secrets can allow encrypted Kubernetes Secret manifests to be stored in Git.

Conceptually:

```text
Secret
 ↓
Encrypt
 ↓
SealedSecret
 ↓
Git
 ↓
Controller
 ↓
Secret
```

---

# External Secrets

External Secrets can synchronize secrets from external secret-management systems into Kubernetes.

Conceptually:

```text
External Secret Manager
          ↓
   External Secrets
          ↓
      Kubernetes
```

---

# Secret Rotation

Production secrets should have controlled rotation processes.

Example:

```text
Old Credential
      ↓
Generate New
      ↓
Update Secret Store
      ↓
Synchronize
      ↓
Restart / Reload
      ↓
Validate
```

---

# Argo CD

Argo CD is a declarative GitOps continuous delivery tool for Kubernetes.

Its core model is:

```text
Git
 ↓
Desired State
 ↓
Argo CD
 ↓
Kubernetes
```

---

# Argo CD Architecture

Conceptually:

```text
Git Repository
      │
      ▼
Argo CD
 ├── API Server
 ├── Repository Server
 ├── Application Controller
 └── Identity / RBAC
      │
      ▼
Kubernetes
```

---

# Argo CD Application

An Argo CD Application represents:

```text
Source
+
Destination
+
Desired State
```

Conceptually:

```text
Git Repository
      ↓
Application
      ↓
Kubernetes Cluster
      ↓
Namespace
```

---

# Argo CD Application Example

Conceptually:

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: api
spec:
  source:
    repoURL: https://git.example.com/platform.git
    path: apps/api
  destination:
    server: https://kubernetes.default.svc
    namespace: production
```

Repository URLs in examples should be replaced with your organization's actual repository.

---

# Argo CD Sync

Sync means:

```text
Make Kubernetes match Git.
```

---

# Manual Sync

An operator initiates synchronization.

Useful when:

```text
Production Changes Require Approval
```

---

# Automated Sync

Argo CD can automatically synchronize approved desired state.

Example flow:

```text
Git Commit
   ↓
Argo CD Detects Change
   ↓
Sync
   ↓
Kubernetes
```

---

# Self-Healing

If someone manually changes a managed resource:

```text
Git:
replicas = 3

Cluster:
replicas = 5
```

Argo CD can detect drift and, when configured for automated self-healing, reconcile it back toward Git.

---

# Drift Detection

Drift means:

```text
Desired State ≠ Actual State
```

Example:

```text
Git:
image = v2

Cluster:
image = v3
```

---

# Why Drift Is Dangerous

Manual changes can:

```text
Bypass Review
Break Compliance
Create Inconsistency
Complicate Rollbacks
```

---

# GitOps Drift Flow

```text
Git
 ↓
Desired State
 ↓
Compare
 ↓
Cluster
 ↓
Drift
 ↓
Alert / Reconcile
```

---

# Flux

Flux is another GitOps toolkit for Kubernetes.

Its architecture centers around:

```text
Git
 ↓
Flux Controllers
 ↓
Kubernetes
```

---

# Flux Architecture

Flux uses specialized controllers for resources such as:

```text
GitRepository
Kustomization
HelmRelease
```

These controllers reconcile desired state.

---

# Argo CD vs Flux

| Argo CD | Flux |
|---|---|
| Strong UI | Kubernetes-native controller model |
| Application-centric | Resource/controller-centric |
| Rich visualization | Modular controller architecture |
| Strong multi-cluster workflows | Strong Kubernetes-native GitOps model |

Both are mature GitOps approaches.

---

# When to Use Argo CD

Argo CD can be attractive when you want:

```text
Visual UI
Application Dashboard
Application Health
Sync Visibility
Multi-Cluster Management
```

---

# When to Use Flux

Flux can be attractive when you prefer:

```text
Kubernetes-Native Resources
Controller-Based Architecture
Composable Components
```

---

# GitOps Security

Git becomes a critical security boundary.

Protect:

```text
Repositories
Branches
Deploy Keys
Tokens
CI Credentials
GitOps Controllers
```

---

# Repository Permissions

Use least privilege.

Not every developer should be able to modify:

```text
Production Configuration
RBAC
Security Policies
Cluster Infrastructure
```

---

# Branch Protection

Protect important branches using controls such as:

```text
Pull Requests
Required Reviews
Status Checks
Signed Commits
```

---

# Commit Signing

Commit signing can help verify that commits were created or approved by trusted identities.

Technologies can include:

```text
GPG
SSH Signing
Sigstore
```

---

# GitOps Supply Chain

A GitOps deployment chain may be:

```text
Source Code
   ↓
Build
   ↓
Test
   ↓
Image
   ↓
Scan
   ↓
Sign
   ↓
Git Update
   ↓
GitOps
   ↓
Kubernetes
```

Every stage should be protected.

---

# Image Verification

Before deployment, organizations may require:

```text
Approved Registry
+
Trusted Signature
+
Known Digest
+
Security Scan
```

---

# Policy as Code

GitOps works well with policy engines.

Example:

```text
Git
 ↓
Manifest
 ↓
Policy
 ↓
Validation
 ↓
Deploy
```

---

# CI Integration

CI can validate GitOps changes before they reach production.

Example:

```text
Pull Request
      ↓
Lint
      ↓
Test
      ↓
Security Scan
      ↓
Policy Check
      ↓
Review
      ↓
Merge
```

---

# Pull Requests

Production changes should ideally pass through review.

A PR can show:

```text
Before
vs
After
```

---

# GitOps Change Management

Every production change can have:

```text
Commit
Author
Reviewers
Timestamp
Diff
Approval
Deployment
```

This provides strong auditability.

---

# GitOps Audit Trail

```text
Git Commit
    ↓
Pull Request
    ↓
Approval
    ↓
Merge
    ↓
GitOps Sync
    ↓
Cluster Change
```

---

# Compliance Benefits

GitOps can help with:

```text
Traceability
Change Control
Auditability
Reproducibility
Access Control
Rollback
```

GitOps itself does not automatically guarantee compliance.

---

# Multi-Cluster GitOps

A central Git repository can manage:

```text
Cluster A
Cluster B
Cluster C
```

---

# Multi-Cluster Architecture

```text
                  Git
                   │
         ┌─────────┼─────────┐
         ▼         ▼         ▼
     Cluster A Cluster B Cluster C
         │         │         │
      GitOps     GitOps    GitOps
     Controller Controller Controller
```

---

# Cluster-Specific Configuration

Use overlays or directories:

```text
clusters/
├── dev-cluster/
├── staging-cluster/
└── production-cluster/
```

---

# Multi-Environment GitOps

```text
Base
 │
 ├── Dev
 ├── Staging
 └── Production
```

Shared configuration remains centralized while environment-specific differences are explicit.

---

# ApplicationSets

Argo CD ApplicationSets can help generate multiple Applications from templates.

Conceptually:

```text
Application Template
       ↓
Cluster List
       ↓
Multiple Applications
```

Useful for:

```text
Multi-Cluster
Multi-Environment
Many Applications
```

---

# Progressive Delivery

GitOps can support:

```text
Canary
Blue-Green
Traffic Splitting
Progressive Rollouts
```

---

# Canary Deployment

Example:

```text
95% → v1
5%  → v2
```

Monitor:

```text
Errors
Latency
Availability
Business Metrics
```

Then increase traffic gradually.

---

# Blue-Green Deployment

```text
Blue = Current
Green = New
```

GitOps can manage the desired state for the active environment.

---

# Rollback

Git provides version history.

Example:

```text
Commit C
 ↓
Commit B
 ↓
Commit A
```

Rollback can mean reverting to a known-good configuration.

---

# Git Revert

Example:

```bash
git revert <commit>
```

Then:

```text
Git
 ↓
GitOps Controller
 ↓
Kubernetes
```

---

# Rollback vs Manual kubectl

Manual rollback:

```bash
kubectl rollout undo
```

may correct the cluster temporarily.

GitOps rollback should also restore the desired state in Git to avoid drift.

---

# Disaster Recovery With GitOps

Git can preserve:

```text
Application Configuration
Infrastructure Configuration
Policies
Deployment Definitions
```

Therefore a cluster can potentially be reconstructed from:

```text
Infrastructure as Code
+
GitOps Repository
+
Data Backups
+
Secret Store
```

---

# GitOps Is Not a Backup

Git does not replace:

```text
Database Backups
Persistent Volume Backups
Object Storage Backups
```

---

# GitOps Observability

Monitor:

```text
Sync Status
Health Status
Drift
Deployment Failures
Controller Errors
Repository Availability
```

---

# Application Health

A GitOps system should distinguish:

```text
Synced
vs
Healthy
```

A workload can be synchronized with Git but still be unhealthy.

---

# Sync Status

Typical conceptual states:

```text
Synced
OutOfSync
Unknown
```

---

# Health Status

Typical conceptual states may include:

```text
Healthy
Progressing
Degraded
Missing
Unknown
```

Exact states depend on the GitOps tool and resource type.

---

# GitOps Notifications

Notify teams about:

```text
Deployment Failure
Sync Failure
Drift
Health Degradation
Production Changes
```

---

# GitOps Troubleshooting

A useful process:

```text
Check Git
 ↓
Check Controller
 ↓
Check Sync
 ↓
Check Manifest
 ↓
Check Kubernetes Events
 ↓
Check Pod
 ↓
Check Application
```

---

# Troubleshooting Git Changes

Verify:

```text
Correct Repository
Correct Branch
Correct Path
Correct Commit
```

---

# Troubleshooting Sync

Check:

```text
Repository Access
Authentication
Manifest Errors
Permissions
Admission Policies
Resource Conflicts
```

---

# Troubleshooting Application Health

If GitOps says:

```text
Synced
```

but application is unhealthy:

```text
Check Pods
Check Services
Check Probes
Check Logs
Check Dependencies
```

---

# GitOps and Manual Changes

Avoid:

```bash
kubectl edit
```

for Git-managed resources.

Prefer:

```text
Git Change
 ↓
Review
 ↓
Merge
 ↓
Reconcile
```

---

# Emergency Changes

Production incidents may occasionally require emergency intervention.

If a manual change is necessary:

```text
Make Emergency Change
        ↓
Restore Service
        ↓
Record Change
        ↓
Update Git
        ↓
Reconcile
```

Never leave an important manual production change undocumented.

---

# GitOps Security Architecture

```text
Developer
   │
   ▼
Git Repository
   │
   ├── Branch Protection
   ├── Review
   ├── Signing
   └── Security Scanning
   │
   ▼
GitOps Controller
   │
   ├── RBAC
   ├── Policy
   └── Credentials
   │
   ▼
Kubernetes
   │
   ├── Admission
   ├── RBAC
   ├── NetworkPolicy
   └── Runtime Security
```

---

# GitOps Best Practices

### 1. Treat Git as the Source of Truth

Avoid unmanaged manual changes.

---

### 2. Protect Production Repositories

Use:

```text
Branch Protection
Review
Least Privilege
MFA
```

---

### 3. Never Store Plaintext Secrets

Use appropriate secret-management mechanisms.

---

### 4. Use Immutable Image References

Prefer:

```text
Version
+
Digest
```

where appropriate.

---

### 5. Validate Before Merge

Run:

```text
Lint
Tests
Security Scan
Policy Checks
```

---

### 6. Separate Environments

Make production changes explicit.

---

### 7. Use Pull Requests

Require review for sensitive changes.

---

### 8. Monitor Drift

Detect unauthorized manual changes.

---

### 9. Test Rollbacks

Do not assume rollback works.

---

### 10. Monitor GitOps Controllers

GitOps itself is production infrastructure and requires observability.

---

# Common Mistakes

## 1. Storing Plaintext Secrets in Git

Never commit production credentials directly.

---

## 2. Giving Developers Production Write Access

Use Git-based review and least privilege.

---

## 3. Mixing Application Code and Deployment Configuration Without Structure

Large repositories become difficult to maintain.

---

## 4. No Branch Protection

A single compromised account could modify production state.

---

## 5. Manual `kubectl` Changes

These create drift.

---

## 6. No Rollback Strategy

Every production deployment needs a recovery path.

---

## 7. Treating GitOps as Backup

Git does not replace data backups.

---

## 8. No Policy Validation

Invalid or insecure manifests can reach the cluster.

---

## 9. No Drift Monitoring

Unauthorized changes may remain undetected.

---

## 10. Overly Broad GitOps Permissions

The GitOps controller should have only the permissions required for its scope.

---

## 11. One Huge Repository Without Ownership

Poor organization creates operational complexity.

---

## 12. No Production Approval

Automated deployment does not necessarily mean unrestricted deployment.

---

# Production GitOps Checklist

```text
☑ Git is source of truth
☑ Repository structure documented
☑ Production branches protected
☑ Pull requests required
☑ Required reviews configured
☑ CI validation enabled
☑ Security scanning enabled
☑ Policy validation enabled
☑ Secrets protected
☑ Image digests controlled
☑ GitOps controller deployed HA where required
☑ Controller RBAC minimized
☑ Repository credentials protected
☑ Sync status monitored
☑ Application health monitored
☑ Drift detection enabled
☑ Self-healing configured where appropriate
☑ Rollback tested
☑ Multi-environment strategy documented
☑ Multi-cluster strategy documented
☑ GitOps notifications configured
☑ Audit trail retained
☑ Emergency change procedure documented
☑ Disaster recovery strategy documented
☑ Git repositories backed up where required
☑ Data backups maintained separately
☑ Production changes traceable
```

---

# Hands-on Lab 1 – Basic GitOps Repository

Create:

```text
gitops/
├── apps/
│   └── nginx/
├── environments/
│   ├── dev/
│   └── production/
└── README.md
```

Add a Deployment and Service.

---

# Hands-on Lab 2 – Git-Based Deployment

Create a Kubernetes manifest.

Commit:

```bash
git add .
git commit -m "Add nginx application"
git push
```

Use a GitOps controller to synchronize it.

---

# Hands-on Lab 3 – Argo CD

Install Argo CD in a disposable cluster.

Create an Application pointing to your Git repository.

Observe:

```text
Sync
Health
Application Resources
```

---

# Hands-on Lab 4 – Automatic Sync

Enable automated synchronization.

Change:

```yaml
replicas: 2
```

to:

```yaml
replicas: 3
```

Commit and push.

Observe the reconciliation.

---

# Hands-on Lab 5 – Drift Detection

Deploy:

```text
replicas = 3
```

Then manually change the live resource to:

```text
replicas = 5
```

Observe:

```text
OutOfSync
```

If self-healing is enabled, observe reconciliation back toward Git.

---

# Hands-on Lab 6 – GitOps Rollback

Deploy:

```text
v1
```

Then:

```text
v2
```

Revert the Git commit.

Observe:

```text
Git
 ↓
GitOps
 ↓
Kubernetes
```

---

# Hands-on Lab 7 – Environment Promotion

Create:

```text
dev
staging
production
```

Promote:

```text
v1 → v2
```

through each environment.

---

# Hands-on Lab 8 – Kustomize With GitOps

Create:

```text
base/
overlays/dev/
overlays/staging/
overlays/production/
```

Deploy each overlay through GitOps.

---

# Hands-on Lab 9 – Helm With GitOps

Create or use a Helm chart.

Store environment-specific values in Git.

Deploy through a GitOps controller.

---

# Hands-on Lab 10 – Secret Management

Use a suitable test secret-management solution.

Verify that:

```text
Plaintext Secret
```

does not exist in Git.

---

# Hands-on Lab 11 – Policy as Code

Add a policy:

```text
Reject privileged containers
```

Attempt to deploy a violating manifest through GitOps.

Verify that the policy prevents the deployment.

---

# Hands-on Lab 12 – GitOps RBAC

Create different GitOps access levels:

```text
Viewer
Developer
Operator
Administrator
```

Verify each permission set.

---

# Hands-on Lab 13 – Multi-Cluster GitOps

Create:

```text
Cluster A
Cluster B
```

Deploy the same application to both through GitOps.

---

# Hands-on Lab 14 – Drift Detection Dashboard

Build a dashboard showing:

```text
Synced Applications
OutOfSync Applications
Degraded Applications
Failed Syncs
```

---

# Hands-on Lab 15 – Progressive Delivery

Implement:

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

Then progressively increase traffic.

---

# Hands-on Lab 16 – Production GitOps Exercise

Build:

```text
Application Repository
        ↓
CI
        ↓
Container Image
        ↓
GitOps Repository
        ↓
Policy Validation
        ↓
Argo CD / Flux
        ↓
Kubernetes
        ↓
Monitoring
```

Implement:

```text
Security
RBAC
Secrets
Rollback
Drift Detection
Notifications
```

---

# Quick Revision

## GitOps

```text
Git
+
Declarative Configuration
+
Automated Reconciliation
```

---

## Desired State

```text
What the cluster should look like
```

---

## Actual State

```text
What the cluster currently looks like
```

---

## Reconciliation

```text
Process of aligning actual state with desired state
```

---

## Drift

```text
Desired State ≠ Actual State
```

---

## Argo CD

```text
Kubernetes GitOps continuous delivery tool
```

---

## Flux

```text
Kubernetes GitOps toolkit based on controllers
```

---

## GitOps Rollback

```text
Restore a known-good Git state
```

---

## GitOps Self-Healing

```text
Automatically reconcile unauthorized drift
```

---

## Policy as Code

```text
Machine-readable policies evaluated automatically
```

---

## GitOps Source of Truth

```text
Version-controlled desired state
```

---

# Essential Commands

Clone repository:

```bash
git clone <repository>
```

Check status:

```bash
git status
```

Create branch:

```bash
git checkout -b feature/update-api
```

Stage changes:

```bash
git add .
```

Commit:

```bash
git commit -m "Update API deployment"
```

Push:

```bash
git push
```

Review history:

```bash
git log --oneline
```

Revert a commit:

```bash
git revert <commit>
```

Kubernetes application:

```bash
kubectl get applications -A
```

Check ApplicationSet:

```bash
kubectl get applicationsets -A
```

Check GitOps-related resources:

```bash
kubectl get all -n argocd
```

Check application:

```bash
kubectl get application <name> -n argocd
```

Check Kubernetes resources:

```bash
kubectl get pods -A
```

Check events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Check deployment:

```bash
kubectl rollout status deployment/<name>
```

---

# Interview Questions

## Basic

- What is GitOps?
- What are the core principles of GitOps?
- Why is Git used as the source of truth?
- What is desired state?
- What is actual state?
- What is reconciliation?
- What is configuration drift?
- What is the difference between GitOps and traditional CI/CD?
- What is Argo CD?
- What is Flux?
- What is a GitOps controller?
- What is declarative configuration?
- What is self-healing?
- What is automated synchronization?

---

## Intermediate

- How does Argo CD work?
- How does Flux work?
- How do you structure a GitOps repository?
- How do you manage development, staging, and production?
- How do you manage secrets with GitOps?
- How do you use Helm with GitOps?
- How do you use Kustomize with GitOps?
- How do you detect configuration drift?
- How do you implement GitOps rollback?
- How do you secure GitOps repositories?
- How do you implement multi-cluster GitOps?
- How do you integrate GitOps with CI/CD?
- How do you implement policy as code with GitOps?

---

## Advanced

- Design a production GitOps architecture for multiple Kubernetes clusters.
- How would you implement GitOps for 100+ clusters?
- How would you securely manage production secrets in GitOps?
- How would you prevent unauthorized production changes?
- How would you implement progressive delivery using GitOps?
- How would you design GitOps disaster recovery?
- How would you handle emergency production changes?
- How would you prevent a compromised Git account from modifying production?
- How would you secure the GitOps controller?
- How would you design GitOps for a regulated environment?
- How would you implement automated compliance with GitOps?
- How would you design a complete GitOps-based Kubernetes platform?

---

# Interview Scenario 1

### Question

> What happens if someone manually changes a Git-managed Kubernetes resource?

### Answer

The cluster enters a drifted state:

```text
Git
Desired = 3 replicas

Cluster
Actual = 5 replicas
```

The GitOps controller detects the difference.

Depending on configuration:

```text
Alert
```

or:

```text
Automatic Reconciliation
```

can restore the desired state.

---

# Interview Scenario 2

### Question

> Why is GitOps more auditable than manual kubectl deployments?

### Answer

GitOps can provide:

```text
Commit
+
Author
+
Review
+
Approval
+
Diff
+
Deployment
+
Synchronization History
```

This creates a strong traceability chain.

---

# Interview Scenario 3

### Question

> How should secrets be managed in GitOps?

### Answer

Do not store plaintext production secrets in Git.

Use mechanisms such as:

```text
External Secret Manager
+
Sealed Secrets
+
SOPS
+
KMS
```

depending on organizational requirements.

---

# Interview Scenario 4

### Question

> What is the difference between CI and GitOps CD?

### Answer

CI focuses on:

```text
Build
Test
Scan
Package
```

GitOps CD focuses on:

```text
Desired State
Reconciliation
Deployment
Drift Detection
```

A common architecture is:

```text
CI
 ↓
Image
 ↓
Git Configuration Change
 ↓
GitOps Controller
 ↓
Kubernetes
```

---

# Interview Scenario 5

### Question

> How would you implement multi-cluster GitOps?

### Answer

Use:

```text
Central Git Repository
        ↓
Cluster-Specific Configuration
        ↓
GitOps Controller per Cluster
        ↓
Kubernetes Clusters
```

Use overlays or cluster-specific directories to manage differences.

---

# Interview Scenario 6

### Question

> How do you prevent insecure manifests from reaching production?

### Answer

Use multiple layers:

```text
Pull Request
 ↓
Lint
 ↓
Security Scan
 ↓
Policy Check
 ↓
Review
 ↓
Admission Policy
 ↓
GitOps
 ↓
Kubernetes
```

This provides defense in depth.

---

# Interview Scenario 7

### Question

> What happens if Git is temporarily unavailable?

### Answer

The existing cluster state can continue running.

However:

```text
New Desired State
```

cannot be retrieved until repository access is restored.

Therefore production GitOps should consider:

```text
Git Availability
Controller Availability
Repository Credentials
Network Connectivity
```

---

# Interview Scenario 8

### Question

> Is GitOps a replacement for CI/CD?

### Answer

No.

GitOps is primarily a deployment and operational model.

A complete delivery pipeline may be:

```text
CI
 ↓
Build
 ↓
Test
 ↓
Scan
 ↓
Image
 ↓
GitOps
 ↓
Kubernetes
```

---

# Interview Scenario 9

### Question

> Why should you avoid manually changing GitOps-managed resources?

### Answer

Manual changes create:

```text
Drift
+
Poor Auditability
+
Configuration Inconsistency
+
Rollback Problems
```

The preferred workflow is:

```text
Git Change
 ↓
Review
 ↓
Merge
 ↓
Reconcile
```

---

# Interview Scenario 10

### Question

> Design a secure production GitOps architecture.

### Answer

```text
Developer
   │
   ▼
Git Repository
   │
   ├── Branch Protection
   ├── Pull Request
   ├── Code Review
   ├── Commit Verification
   └── Security Scanning
   │
   ▼
CI
   │
   ├── Tests
   ├── Image Scan
   ├── SBOM
   └── Policy Validation
   │
   ▼
GitOps Repository
   │
   ▼
Argo CD / Flux
   │
   ├── RBAC
   ├── Drift Detection
   └── Sync
   │
   ▼
Kubernetes
   │
   ├── Admission
   ├── RBAC
   ├── NetworkPolicy
   └── Runtime Security
   │
   ▼
Monitoring / SIEM
```

---

# Production GitOps Checklist

```text
☑ Git source of truth established
☑ Repository ownership defined
☑ Branch protection enabled
☑ Pull requests required
☑ Production review required
☑ CI validation configured
☑ Security scanning configured
☑ Policy as Code configured
☑ Secrets protected
☑ Image digests controlled
☑ GitOps controller secured
☑ GitOps RBAC minimized
☑ Repository credentials protected
☑ Automated sync configured appropriately
☑ Drift detection enabled
☑ Self-healing evaluated
☑ Application health monitored
☑ Rollback tested
☑ Multi-environment strategy documented
☑ Multi-cluster strategy documented
☑ Notifications configured
☑ Audit history retained
☑ Emergency procedure documented
☑ Git repository recovery strategy documented
☑ Data backups maintained separately
☑ Disaster recovery tested
```

---

# Chapter Summary

GitOps provides a declarative, version-controlled, continuously reconciled approach to Kubernetes operations.

The core model is:

```text
Git
 ↓
Desired State
 ↓
GitOps Controller
 ↓
Kubernetes
 ↓
Actual State
 ↓
Reconciliation
```

The major benefits are:

```text
Version Control
+
Auditability
+
Repeatability
+
Drift Detection
+
Automated Deployment
+
Rollback
+
Consistency
```

Popular tools include:

```text
Argo CD
Flux
```

GitOps should also integrate with:

```text
CI/CD
+
Policy as Code
+
Security Scanning
+
Secret Management
+
Monitoring
+
Incident Response
```

The most important principle is:

> **Treat Git as the authoritative source for desired state, protect the path from code to cluster, continuously reconcile the environment, and make every production change traceable, reviewable, reproducible, and recoverable.**

---

## Next Chapter

# Chapter 79 – CI/CD with Kubernetes

Topics will include:

- CI/CD Fundamentals
- Continuous Integration
- Continuous Delivery
- Continuous Deployment
- Kubernetes CI/CD
- CI/CD Architecture
- Source Control
- Build Automation
- Testing
- Unit Testing
- Integration Testing
- Security Testing
- Container Builds
- Docker
- BuildKit
- Image Registries
- Image Tagging
- Image Digests
- Image Scanning
- SBOM
- Image Signing
- Supply Chain Security
- Deployment Automation
- Kubernetes Manifests
- Helm
- Kustomize
- GitOps Integration
- Argo CD
- Flux
- GitHub Actions
- GitLab CI
- Jenkins
- Tekton
- Pipeline Stages
- Environment Promotion
- Development
- Staging
- Production
- Deployment Strategies
- Rolling Updates
- Blue-Green
- Canary
- Progressive Delivery
- Automated Rollbacks
- Deployment Gates
- Approval Gates
- Secrets Management
- CI/CD Security
- RBAC
- Runner Security
- Pipeline Isolation
- Artifact Security
- Dependency Security
- Vulnerability Scanning
- Policy as Code
- Compliance
- Deployment Verification
- Smoke Testing
- Health Checks
- Observability
- Notifications
- Failure Handling
- Pipeline Troubleshooting
- Production CI/CD Architecture
- Best Practices
- Common Mistakes
- Hands-on Labs
- Quick Revision
- Interview Questions
- References

---