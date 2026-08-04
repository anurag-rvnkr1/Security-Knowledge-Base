# Chapter 7 – Deployments

## Overview

A **Deployment** is one of the most important Kubernetes objects.

While a ReplicaSet ensures that a certain number of Pods are running, a Deployment manages ReplicaSets and provides advanced application lifecycle management such as:

- Rolling Updates
- Rollbacks
- Version History
- Controlled Scaling
- Zero (or near-zero) Downtime Deployments
- Declarative Updates

In production Kubernetes clusters, applications are almost always deployed using **Deployments**, not standalone Pods or ReplicaSets.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Deployment is
- Why Deployments exist
- Deployment Architecture
- Deployment Lifecycle
- ReplicaSet Management
- Rolling Updates
- Rollbacks
- Deployment Strategies
- Scaling Deployments
- Deployment YAML
- Best Practices

---

# Why Deployments?

Suppose you create a ReplicaSet.

```
ReplicaSet

↓

3 Pods
```

It provides:

- Self-healing
- Scaling

However, updating the application version is difficult.

Example:

```
NGINX v1

↓

Need

↓

NGINX v2
```

A Deployment automates this process.

---

# What is a Deployment?

A Deployment is a Kubernetes controller that manages ReplicaSets and Pods.

```
Deployment

↓

ReplicaSet

↓

Pods
```

The Deployment is responsible for application lifecycle management.

---

# Deployment Responsibilities

Deployments provide:

- Create ReplicaSets
- Create Pods
- Rolling Updates
- Rollbacks
- Scaling
- Version History
- Self-Healing (through ReplicaSets)

---

# Deployment Architecture

```
               Deployment

                     │

             ReplicaSet

                     │

        ┌────────────┼────────────┐

        ▼            ▼            ▼

      Pod 1        Pod 2        Pod 3
```

The Deployment never manages Pods directly.

Instead:

```
Deployment

↓

ReplicaSet

↓

Pods
```

---

# Deployment Hierarchy

```
Deployment

↓

ReplicaSet

↓

Pods

↓

Containers
```

Each layer has a different responsibility.

---

# Deployment YAML

Example:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:
  name: nginx

spec:

  replicas: 3

  selector:

    matchLabels:

      app: nginx

  template:

    metadata:

      labels:

        app: nginx

    spec:

      containers:

      - name: nginx

        image: nginx:1.29
```

---

# YAML Structure

```
Deployment

↓

Metadata

↓

Spec

↓

Replicas

↓

Selector

↓

Pod Template
```

---

# Creating a Deployment

Apply:

```bash
kubectl apply -f deployment.yaml
```

Verify:

```bash
kubectl get deployments
```

View ReplicaSets:

```bash
kubectl get rs
```

View Pods:

```bash
kubectl get pods
```

---

# Deployment Lifecycle

```
Create Deployment

↓

Create ReplicaSet

↓

Create Pods

↓

Running

↓

Scale

↓

Update

↓

Rollback

↓

Delete
```

---

# Deployment Creation Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Deployment Controller

↓

ReplicaSet

↓

Pods

↓

Running
```

---

# Scaling Deployments

Scale:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Workflow:

```
Deployment

↓

ReplicaSet

↓

5 Pods
```

Scale down:

```bash
kubectl scale deployment nginx \
--replicas=2
```

---

# Updating an Application

Suppose current image:

```
nginx:1.29
```

Need:

```
nginx:1.30
```

Update:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Deployment automatically begins a rolling update.

---

# Rolling Update

Instead of deleting all Pods:

```
Old Pods

↓

Delete All

↓

Create New
```

Kubernetes performs:

```
Old Pod

↓

New Pod

↓

Old Pod

↓

New Pod

↓

Complete
```

Applications remain available during the update.

---

# Rolling Update Workflow

```
Deployment

↓

New ReplicaSet

↓

Create New Pod

↓

Ready

↓

Delete Old Pod

↓

Repeat
```

This process continues until all Pods are updated.

---

# ReplicaSets During Updates

Before update:

```
Deployment

↓

ReplicaSet A

↓

3 Pods
```

After update starts:

```
Deployment

↓

ReplicaSet A

↓

ReplicaSet B

↓

Pods Transition
```

Eventually:

```
ReplicaSet B

↓

3 Pods
```

ReplicaSet A is retained for rollback history (subject to revision history limits).

---

# Rollback

Suppose update fails.

Command:

```bash
kubectl rollout undo deployment nginx
```

Workflow:

```
ReplicaSet B

↓

Rollback

↓

ReplicaSet A

↓

Application Restored
```

---

# Deployment Status

Check rollout:

```bash
kubectl rollout status deployment nginx
```

History:

```bash
kubectl rollout history deployment nginx
```

---

# Viewing Deployments

List:

```bash
kubectl get deployments
```

Describe:

```bash
kubectl describe deployment nginx
```

The output includes:

- Replicas
- Strategy
- Conditions
- Events
- ReplicaSets

---

# Deleting Deployments

Delete:

```bash
kubectl delete deployment nginx
```

Workflow:

```
Deployment

↓

ReplicaSets

↓

Pods

↓

Removed
```

---

# Deployment Strategies

Kubernetes supports multiple deployment strategies.

The most common:

```
RollingUpdate
```

Alternative:

```
Recreate
```

RollingUpdate is the default.

---

# RollingUpdate Strategy

```
Old Pod

↓

New Pod

↓

Healthy

↓

Remove Old Pod

↓

Repeat
```

Advantages:

- High availability
- Minimal downtime
- Controlled updates

---

# Recreate Strategy

```
Old Pods

↓

Delete All

↓

Create New Pods
```

Advantages:

- Simpler
- Useful when multiple versions cannot run simultaneously

Disadvantage:

- Downtime during deployment

---

# Deployment vs ReplicaSet

| Deployment | ReplicaSet |
|------------|------------|
| Manages ReplicaSets | Manages Pods |
| Rolling Updates | No Rolling Updates |
| Rollbacks | No Rollbacks |
| Version History | No Version History |
| Production Standard | Internal Building Block |

---

# Deployment vs Pod

| Deployment | Pod |
|------------|-----|
| Multiple replicas | Single workload |
| Automatic updates | No update management |
| Self-healing | None by itself |
| Scalable | Single instance |

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f deployment.yaml
```

View:

```bash
kubectl get deployments
```

Describe:

```bash
kubectl describe deployment nginx
```

Scale:

```bash
kubectl scale deployment nginx \
--replicas=5
```

Update image:

```bash
kubectl set image deployment/nginx \
nginx=nginx:1.30
```

Status:

```bash
kubectl rollout status deployment nginx
```

History:

```bash
kubectl rollout history deployment nginx
```

Rollback:

```bash
kubectl rollout undo deployment nginx
```

Delete:

```bash
kubectl delete deployment nginx
```

---

# Deployment Architecture Summary

```
Deployment

↓

ReplicaSet

↓

Pods

↓

Containers
```

---

# Best Practices

### 1. Use Deployments for Stateless Applications

Deployments are the standard controller for web applications, APIs, and microservices.

---

### 2. Use Versioned Images

Avoid:

```yaml
image: nginx:latest
```

Prefer:

```yaml
image: nginx:1.29.1
```

---

### 3. Monitor Rollouts

Always verify:

```bash
kubectl rollout status
```

after deploying a new version.

---

### 4. Keep Revision History

Revision history enables fast rollbacks when problems occur.

---

### 5. Store Deployment Manifests in Git

Use GitOps or Infrastructure as Code practices for reproducible deployments.

---

