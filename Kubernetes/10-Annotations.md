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

## Next Section

How Annotations Work Internally

Annotations vs Labels (Deep Dive)

Hands-on Labs

Common Mistakes

Quick Revision

References

---