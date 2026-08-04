# Chapter 10 – Annotations

## Overview

**Annotations** are key-value metadata attached to Kubernetes objects.

Unlike **Labels**, which are designed for **selection and grouping**, Annotations are intended to store **descriptive, operational, or tool-specific information**.

Annotations are commonly used by:

- CI/CD Pipelines
- GitOps Tools
- Monitoring Systems
- Service Meshes
- Ingress Controllers
- Backup Solutions
- Security Scanners
- Kubernetes Extensions

Annotations allow Kubernetes and external tools to attach additional metadata to resources without affecting resource selection.

---

# Learning Objectives

After completing this chapter, you will understand:

- What Annotations are
- Why Annotations exist
- Annotation Architecture
- Labels vs Annotations
- Annotation Syntax
- Common Annotation Use Cases
- Annotations in Ingress
- Annotations in Deployments
- Annotations in Services
- Best Practices

---

# What is an Annotation?

An Annotation is a **key-value pair** stored in the metadata section of a Kubernetes object.

Example:

```yaml
metadata:

  annotations:

    owner: "security-team"

    build: "2026.08.15"

    description: "Production API"
```

Annotations provide additional information about an object but are **not used to identify or select resources**.

---

# Annotation Architecture

```
Deployment

│

├── Labels

│     app=frontend

│     env=production

│

└── Annotations

      owner=platform-team

      build=2026.08.15

      description=Production API
```

---

# Why Annotations?

Imagine a Deployment.

```
Deployment

↓

Frontend API
```

You also want to store:

- Build Number
- Git Commit
- Owner
- Documentation URL
- Deployment Timestamp

These values should not affect how Kubernetes manages resources.

Instead of Labels:

```
Annotations

↓

Metadata
```

---

# Labels vs Annotations

| Labels | Annotations |
|----------|-------------|
| Used for selection | Not used for selection |
| Used by controllers | Used by tools and humans |
| Indexed for fast lookups | Not indexed for selection |
| Small identifying metadata | Rich descriptive metadata |
| Used in selectors | Ignored by selectors |

---

# Annotation Syntax

General format:

```yaml
annotations:

  key: value
```

Example:

```yaml
annotations:

  owner: "platform"

  contact: "devops@example.com"

  description: "Frontend Application"
```

---

# Where Can Annotations Be Used?

Annotations can be attached to almost every Kubernetes object.

Examples:

- Pods
- Deployments
- ReplicaSets
- Services
- Ingresses
- StatefulSets
- DaemonSets
- Jobs
- CronJobs
- ConfigMaps
- Secrets
- Namespaces

---

# Deployment Example

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: frontend

  annotations:

    owner: "platform-team"

    release: "v2.0"

spec:
```

---

# Pod Example

```yaml
metadata:

  annotations:

    description: "Python API"

    environment: "Production"
```

---

# Service Example

```yaml
metadata:

  annotations:

    owner: "network-team"
```

---

# Viewing Annotations

Describe an object:

```bash
kubectl describe deployment frontend
```

or view YAML:

```bash
kubectl get deployment frontend \
-o yaml
```

Look for:

```yaml
metadata:

  annotations:
```

---

# Creating Annotations

Example:

```yaml
metadata:

  annotations:

    created-by: "Anurag"

    project: "CyberSOC"
```

Deploy:

```bash
kubectl apply -f deployment.yaml
```

---

# Adding Annotations

Command:

```bash
kubectl annotate deployment frontend \
owner=platform-team
```

---

# Updating Annotations

```bash
kubectl annotate deployment frontend \
owner=security-team --overwrite
```

---

# Removing Annotations

```bash
kubectl annotate deployment frontend \
owner-
```

---

# Common Annotation Examples

```
owner=platform

build=2026.08.15

release=v2.1

ticket=SEC-102

documentation=https://internal/wiki

git-commit=9fd1234
```

---

# CI/CD Example

Pipeline:

```
Git Commit

↓

Build

↓

Deployment

↓

Annotation Added
```

Example:

```yaml
annotations:

  git-commit: "9fd1234"

  pipeline: "GitHub Actions"

  build-number: "458"
```

This makes it easy to determine which build produced a deployment.

---

# GitOps Example

GitOps tools often record deployment metadata.

```
Git Repository

↓

Argo CD

↓

Deployment

↓

Annotations
```

Example:

```yaml
annotations:

  deployed-by: "ArgoCD"
```

---

# Monitoring Example

Monitoring platforms may use annotations for:

- Ownership
- Alert routing
- Dashboard links
- Documentation

Example:

```yaml
annotations:

  owner: "SRE Team"

  runbook: "https://company/wiki/runbook"
```

---

# Ingress Example

Many Ingress controllers use annotations to configure behavior.

Conceptually:

```
Ingress

↓

Annotations

↓

Controller Behavior
```

Examples include:

- TLS behavior
- Timeouts
- Rate limiting
- Redirects
- Load balancing options

> Note: The available annotations depend on the specific Ingress controller (such as NGINX, HAProxy, or Traefik).

---

# Service Mesh Example

Service mesh platforms can read annotations to enable or configure features.

```
Pod

↓

Annotation

↓

Sidecar Configuration
```

The exact annotations depend on the service mesh implementation.

---

# Security Tool Example

Security scanners may attach metadata such as:

```
Security Scan

↓

Deployment

↓

Annotation

↓

Last Scan Time
```

---

# Annotation Best Practices

### 1. Store Operational Metadata

Good examples:

- Owner
- Build number
- Git commit
- Documentation
- Ticket number

---

### 2. Do Not Use Annotations for Selection

If you need:

```bash
kubectl get pods -l ...
```

you need a **Label**, not an Annotation.

---

### 3. Keep Metadata Accurate

Update annotations when ownership, build versions, or operational details change.

---

### 4. Use Descriptive Keys

Prefer:

```
owner

git-commit

build-number
```

instead of:

```
x

a1

temp
```

---

### 5. Follow Organizational Standards

Establish consistent annotation conventions across teams to simplify automation and tooling.

---


# How Annotations Work Internally

## Overview

Although **Annotations** look similar to **Labels**, they serve a completely different purpose inside Kubernetes.

Labels are designed for:

- Resource selection
- Filtering
- Controller matching

Annotations are designed for:

- Additional metadata
- Tool integration
- Operational information
- Configuration hints

Kubernetes itself generally **does not use Annotations to identify resources**. Instead, many Kubernetes components and external tools read Annotations to determine how they should behave.

---

# High-Level Architecture

```
                 Kubernetes Object

                        │

        ┌───────────────┴───────────────┐

        ▼                               ▼

      Labels                      Annotations

        │                               │

Resource Selection           Additional Metadata

        │                               │

Controllers                External Tools
```

---

# Internal Storage

Every Kubernetes object contains metadata.

Example:

```yaml
metadata:

  labels:

    app: frontend

  annotations:

    owner: platform-team

    build: 2026.08.15
```

Internally:

```
Object

↓

Metadata

↓

Labels

↓

Annotations
```

Both are stored together as part of the Kubernetes object in **etcd**.

---

# API Server Workflow

Suppose a Deployment is created.

```
kubectl apply

↓

API Server

↓

Validation

↓

Store Metadata

↓

etcd
```

The metadata includes:

- Labels
- Annotations
- Name
- Namespace
- Owner References

---

# Annotation Retrieval

Command:

```bash
kubectl get deployment frontend \
-o yaml
```

Workflow:

```
API Server

↓

Retrieve Object

↓

Return Metadata

↓

Annotations Displayed
```

---

# Why Controllers Ignore Annotations

Example:

ReplicaSet:

```
Selector

↓

app=frontend
```

Pod:

```
Annotation

↓

owner=platform
```

Result:

```
Ignored
```

ReplicaSets match **Labels**, not Annotations.

The same applies to:

- Deployments
- Services
- Network Policies

---

# Tool Integration

Annotations are commonly read by external controllers and automation systems.

Example:

```
Deployment

↓

Annotations

↓

GitOps Tool

↓

Deployment Information
```

Unlike Labels, Annotations are often interpreted by software outside the Kubernetes core.

---

# CI/CD Workflow

```
Git Commit

↓

Pipeline

↓

Deployment

↓

Annotations Added

↓

Production
```

Example:

```yaml
annotations:

  build-number: "458"

  git-commit: "7bc19de"

  pipeline: "GitHub Actions"
```

Operations teams can later determine exactly which pipeline produced the deployment.

---

# GitOps Workflow

```
Git Repository

↓

Argo CD

↓

Deployment

↓

Annotation
```

Possible metadata:

```
Sync Time

↓

Revision

↓

Application Owner
```

GitOps platforms often use annotations to track synchronization state and deployment history.

---

# Monitoring Workflow

Monitoring platform:

```
Deployment

↓

Annotations

↓

Alert Routing

↓

Dashboard
```

Example:

```yaml
annotations:

  owner: SRE

  runbook: https://wiki/runbook
```

Operations teams can associate alerts with documentation and ownership.

---

# Ingress Controller Workflow

Example:

```
Ingress

↓

Annotations

↓

Ingress Controller

↓

Configuration Applied
```

Typical configuration areas:

- Timeouts
- TLS
- Redirects
- Rate Limits
- Compression

Each controller defines its own supported annotations.

---

# Service Mesh Workflow

```
Pod

↓

Annotation

↓

Sidecar Configuration
```

The service mesh reads annotations and adjusts behavior accordingly.

Examples include:

- Sidecar injection
- Traffic interception
- Proxy configuration

---

# Backup Workflow

Backup tools often store metadata.

```
Backup Tool

↓

Deployment

↓

Annotations

↓

Backup Information
```

Example:

```
Last Backup

↓

Timestamp
```

---

# Security Workflow

Security scanners:

```
Scan

↓

Deployment

↓

Annotation

↓

Scan Results
```

Possible metadata:

- Scan date
- Compliance status
- Vulnerability report identifier

---

# Metadata Flow

```
Developer

↓

Deployment YAML

↓

Annotations

↓

API Server

↓

etcd

↓

Tools Read Metadata
```

---

# Annotation Size

Unlike Labels, Annotations may contain larger values.

Examples:

- Long descriptions
- URLs
- Build metadata
- JSON configuration
- Documentation references

However, extremely large annotations should be avoided because they increase the size of Kubernetes objects stored in etcd.

---

# Labels vs Annotations Internally

```
Labels

↓

Indexed

↓

Selectors

↓

Controllers
```

```
Annotations

↓

Metadata

↓

Tools

↓

Humans
```

---

# Hands-on Lab 1 – Create Deployment

Example:

```yaml
metadata:

  annotations:

    owner: platform

    build: "102"

    description: "Frontend API"
```

Deploy:

```bash
kubectl apply -f deployment.yaml
```

---

# Hands-on Lab 2 – View Annotations

```bash
kubectl describe deployment frontend
```

or

```bash
kubectl get deployment frontend \
-o yaml
```

Locate:

```yaml
metadata:

  annotations:
```

---

# Hands-on Lab 3 – Add Annotation

```bash
kubectl annotate deployment frontend \
ticket=SEC-104
```

Verify:

```bash
kubectl get deployment frontend \
-o yaml
```

---

# Hands-on Lab 4 – Update Annotation

```bash
kubectl annotate deployment frontend \
owner=security-team \
--overwrite
```

Verify the updated value.

---

# Hands-on Lab 5 – Remove Annotation

```bash
kubectl annotate deployment frontend \
ticket-
```

Confirm removal:

```bash
kubectl get deployment frontend \
-o yaml
```

---

# Common Mistakes

## 1. Using Annotations for Selection

Incorrect:

```
Annotations

↓

kubectl get pods -l owner=platform
```

This will not work because selectors operate on Labels.

Use:

```
Labels

↓

Selectors
```

---

## 2. Storing Important Operational Data Only in Annotations

Annotations are useful metadata, but they should not replace proper documentation, source control, or configuration management.

---

## 3. Putting Large Files in Annotations

Avoid storing:

- Large JSON documents
- Certificates
- Logs
- Binary data

Use ConfigMaps, Secrets, or external storage instead.

---

## 4. Inconsistent Annotation Names

Poor:

```
a

b

temp
```

Better:

```
owner

build-number

git-commit

documentation
```

---

## 5. Confusing Labels and Annotations

Rule of thumb:

Need to **find or select** resources?

```
Label
```

Need to **describe** resources?

```
Annotation
```

---

# Annotations Quick Revision

## Architecture

```
Object

↓

Metadata

↓

Annotations

↓

Tools
```

---

## Workflow

```
Deployment

↓

Annotations

↓

API Server

↓

etcd

↓

Monitoring

↓

GitOps

↓

CI/CD
```

---

## Common Annotation Examples

```
owner=platform

build=458

git-commit=9fd1234

documentation=https://wiki

runbook=https://runbook

ticket=SEC-104
```

---

# Essential kubectl Commands

View YAML:

```bash
kubectl get deployment frontend \
-o yaml
```

Describe:

```bash
kubectl describe deployment frontend
```

Add:

```bash
kubectl annotate deployment frontend \
owner=platform
```

Update:

```bash
kubectl annotate deployment frontend \
owner=security \
--overwrite
```

Remove:

```bash
kubectl annotate deployment frontend \
owner-
```

---

# Interview Questions

### Basic

- What is an Annotation?
- How is an Annotation different from a Label?
- Where are Annotations stored?

---

### Intermediate

- Why can't Annotations be used with selectors?
- How do CI/CD systems use Annotations?
- How do Ingress controllers use Annotations?

---

### Advanced

- Why are Labels indexed but Annotations are not?
- What happens internally when an Annotation is added?
- Why should large datasets not be stored in Annotations?
- How do GitOps tools use Annotations?
- When should you choose an Annotation instead of a ConfigMap?

---

# References

## Official Kubernetes Documentation

- Annotations
- Labels and Selectors
- Kubernetes Object Metadata
- API Conventions
- kubectl Reference

---

## CNCF Resources

- Kubernetes Best Practices
- Cloud Native Computing Foundation (CNCF)
- Kubernetes Learning Path

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Best Practices
- NIST SP 800-190
- OWASP Kubernetes Top 10

---

## Recommended Practice

1. Create a Deployment with Labels and Annotations.
2. View object metadata using `kubectl get -o yaml`.
3. Add, update, and remove Annotations using `kubectl annotate`.
4. Compare the behavior of Labels and Annotations by attempting to filter resources.
5. Simulate a CI/CD pipeline by adding build numbers and Git commit hashes as Annotations.
6. Explore how your chosen Ingress controller or GitOps tool uses Annotations.

---

# Chapter Summary

```
Kubernetes Object

↓

Metadata

├── Labels

│     Used for Selection

│

└── Annotations

      Used for Metadata

↓

External Tools

↓

Automation
```

Annotations provide a flexible way to attach **rich, descriptive metadata** to Kubernetes resources. They enable seamless integration with CI/CD pipelines, GitOps platforms, monitoring systems, Ingress controllers, service meshes, and operational tooling without affecting Kubernetes resource selection or controller behavior.

---

