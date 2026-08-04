# Chapter 6 – ReplicaSets

## Overview

A **ReplicaSet** is a Kubernetes controller responsible for ensuring that a specified number of identical Pod replicas are running at all times.

If a Pod fails, is deleted, or becomes unavailable, the ReplicaSet automatically creates a replacement Pod to maintain the desired number of replicas.

Although ReplicaSets can be created directly, they are **most commonly managed automatically by Deployments** in production environments.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a ReplicaSet is
- Why ReplicaSets exist
- ReplicaSet Architecture
- Desired State Management
- Pod Replica Management
- Label Selectors
- Scaling ReplicaSets
- ReplicaSet YAML
- ReplicaSet Lifecycle
- Best Practices

---

# Why ReplicaSets?

Imagine you have a single Pod.

```
User

↓

Pod

↓

Application
```

If the Pod crashes:

```
Pod

↓

Crash

↓

Application Down
```

There is no automatic recovery.

ReplicaSets solve this problem.

```
ReplicaSet

↓

Desired Pods = 3

↓

Pod 1

Pod 2

Pod 3
```

If one Pod fails:

```
ReplicaSet

↓

Pod Missing

↓

Create New Pod
```

The desired number of Pods is automatically restored.

---

# What is a ReplicaSet?

A ReplicaSet is a Kubernetes controller that ensures a specified number of Pods are always running.

```
ReplicaSet

↓

Desired State

↓

Current State

↓

Reconciliation

↓

Maintain Replicas
```

ReplicaSets continuously monitor the cluster.

---

# ReplicaSet Responsibilities

A ReplicaSet is responsible for:

- Creating Pods
- Deleting excess Pods
- Replacing failed Pods
- Maintaining desired replicas
- Matching Pods using labels

It does **not** perform rolling updates or deployment strategies—that is the role of a Deployment.

---

# ReplicaSet Architecture

```
                ReplicaSet

        Desired Replicas = 3

                │

      ┌─────────┼─────────┐

      ▼         ▼         ▼

    Pod A     Pod B     Pod C
```

The ReplicaSet continuously compares the desired number of replicas with the current number.

---

# Desired State

Example:

```yaml
replicas: 3
```

Desired state:

```
3 Pods
```

Current state:

```
2 Pods
```

ReplicaSet detects:

```
Difference

↓

Create New Pod

↓

3 Pods Running
```

---

# ReplicaSet Reconciliation Loop

```
Desired Replicas

↓

Current Pods

↓

Compare

↓

Difference?

↓

Create/Delete Pods

↓

Desired State Restored
```

This reconciliation loop runs continuously.

---

# ReplicaSet vs Pod

| Pod | ReplicaSet |
|------|------------|
| Runs application | Manages Pods |
| No automatic recovery | Self-healing |
| Single instance | Multiple replicas |
| Manual scaling | Automatic reconciliation |

---

# ReplicaSet vs Deployment

| ReplicaSet | Deployment |
|------------|------------|
| Maintains replicas | Manages ReplicaSets |
| No rolling updates | Rolling updates |
| No rollback support | Rollbacks |
| Basic controller | Production controller |

In production, Deployments usually create and manage ReplicaSets automatically.

---

# ReplicaSet YAML

Example:

```yaml
apiVersion: apps/v1

kind: ReplicaSet

metadata:
  name: nginx-rs

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

        image: nginx
```

---

# YAML Structure

```
ReplicaSet

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

# Understanding Selectors

A ReplicaSet identifies Pods using labels.

Example:

```
ReplicaSet

↓

Selector

↓

app=nginx

↓

Matching Pods
```

Only Pods whose labels match the selector are managed.

---

# Label Matching

Example:

Pod:

```yaml
labels:

  app: nginx
```

ReplicaSet:

```yaml
matchLabels:

  app: nginx
```

Result:

```
Match

↓

ReplicaSet Manages Pod
```

---

# Non-Matching Pods

Example:

Pod:

```yaml
labels:

  app: apache
```

ReplicaSet:

```yaml
matchLabels:

  app: nginx
```

Result:

```
No Match

↓

ReplicaSet Ignores Pod
```

---

# Creating a ReplicaSet

Apply:

```bash
kubectl apply -f replicaset.yaml
```

Verify:

```bash
kubectl get replicasets
```

Pods:

```bash
kubectl get pods
```

---

# Viewing ReplicaSets

List:

```bash
kubectl get replicasets
```

Describe:

```bash
kubectl describe replicaset nginx-rs
```

The description includes:

- Desired replicas
- Current replicas
- Labels
- Events
- Pod template

---

# Scaling ReplicaSets

Scale to five replicas:

```bash
kubectl scale replicaset nginx-rs \
--replicas=5
```

Workflow:

```
3 Pods

↓

Scale

↓

5 Pods
```

Scale down:

```bash
kubectl scale replicaset nginx-rs \
--replicas=2
```

---

# Self-Healing Example

Initial state:

```
ReplicaSet

↓

3 Pods
```

Administrator deletes one Pod:

```bash
kubectl delete pod pod-name
```

ReplicaSet detects:

```
Only 2 Pods

↓

Create Replacement

↓

3 Pods Running
```

---

# Pod Ownership

Every Pod created by a ReplicaSet has an owner reference.

```
ReplicaSet

↓

Owner

↓

Pod
```

If the ReplicaSet is deleted, Kubernetes can determine how managed Pods should be handled based on the deletion strategy.

---

# ReplicaSet Lifecycle

```
ReplicaSet Created

↓

Create Pods

↓

Monitor Pods

↓

Replace Failed Pods

↓

Scale

↓

Delete
```

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f replicaset.yaml
```

View:

```bash
kubectl get rs
```

Describe:

```bash
kubectl describe rs nginx-rs
```

Scale:

```bash
kubectl scale rs nginx-rs \
--replicas=4
```

Delete:

```bash
kubectl delete rs nginx-rs
```

---

# ReplicaSet Architecture Summary

```
ReplicaSet

↓

Desired Replicas

↓

Label Selector

↓

Matching Pods

↓

Continuous Reconciliation
```

---

# Best Practices

### 1. Use Deployments for Long-Running Applications

ReplicaSets are fundamental, but Deployments provide additional capabilities such as rolling updates and rollbacks.

---

### 2. Use Consistent Labels

Ensure Pod template labels exactly match the ReplicaSet selector.

---

### 3. Avoid Overlapping Selectors

Two ReplicaSets should not unintentionally manage the same Pods.

---

### 4. Monitor Replica Health

Regularly review:

- Desired replicas
- Ready replicas
- Available replicas
- Events

---

### 5. Scale Declaratively

For production environments, update manifests and apply changes rather than relying solely on imperative scaling commands.

---

## Next Section

How ReplicaSets Work Internally

ReplicaSet Lifecycle Deep Dive

Label Selectors

Hands-on Labs

Common Mistakes

Quick Revision

References

---