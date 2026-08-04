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

# How ReplicaSets Work Internally

## Overview

A ReplicaSet continuously ensures that the **actual number of running Pods** matches the **desired number of replicas** defined in its specification.

Unlike a Pod, which simply runs an application, a ReplicaSet actively watches the cluster and automatically creates or removes Pods to maintain the desired state.

This behavior is powered by Kubernetes' **reconciliation loop**.

---

# Complete ReplicaSet Workflow

Suppose a ReplicaSet specifies:

```yaml
replicas: 3
```

Complete workflow:

```
Developer

↓

kubectl apply

↓

API Server

↓

Authentication

↓

Authorization

↓

Validation

↓

etcd

↓

ReplicaSet Controller

↓

Compare Desired State

↓

Create Missing Pods

↓

Scheduler

↓

Worker Node

↓

kubelet

↓

Container Runtime

↓

Pods Running
```

---

# Step 1 – User Creates ReplicaSet

Example:

```yaml
apiVersion: apps/v1

kind: ReplicaSet

metadata:

  name: nginx-rs
```

Deploy:

```bash
kubectl apply -f replicaset.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates user
- Authorizes request
- Validates YAML
- Stores ReplicaSet

Workflow:

```
kubectl

↓

API Server

↓

ReplicaSet Stored
```

---

# Step 3 – Store in etcd

```
API Server

↓

etcd
```

At this point:

```
ReplicaSet Exists

↓

No Pods Yet
```

---

# Step 4 – ReplicaSet Controller

The ReplicaSet Controller continuously watches the API Server.

```
ReplicaSet

↓

Desired = 3

↓

Current = 0
```

Difference detected:

```
Need 3 Pods
```

---

# Step 5 – Pod Creation

ReplicaSet creates Pod objects.

```
ReplicaSet

↓

Pod 1

Pod 2

Pod 3
```

Initially:

```
Pending
```

because scheduling has not yet occurred.

---

# Step 6 – Scheduler

Scheduler evaluates:

- CPU
- Memory
- Labels
- Taints
- Affinity
- Policies

Example:

```
Pod 1

↓

Node A

Pod 2

↓

Node B

Pod 3

↓

Node A
```

---

# Step 7 – kubelet

Worker node:

```
API Server

↓

kubelet

↓

Container Runtime

↓

Pod Starts
```

---

# Step 8 – Running

Final state:

```
ReplicaSet

↓

3 Running Pods
```

Desired state achieved.

---

# Continuous Monitoring

ReplicaSet never stops monitoring.

```
Desired = 3

↓

Current = 3

↓

Healthy
```

Every few moments:

```
Compare

↓

Difference?

↓

Take Action
```

This is the reconciliation loop.

---

# Pod Failure Example

Suppose:

```
ReplicaSet

↓

3 Pods
```

Current state:

```
Pod 2 Crashes
```

Result:

```
Current = 2

↓

ReplicaSet Detects

↓

Create New Pod

↓

3 Pods Running
```

No administrator intervention is required.

---

# Manual Pod Deletion

Command:

```bash
kubectl delete pod pod-name
```

Workflow:

```
Delete Pod

↓

ReplicaSet

↓

Current = 2

↓

Create Replacement

↓

3 Pods
```

This surprises many beginners but is expected behavior.

---

# Scaling Up

Current:

```
3 Pods
```

Command:

```bash
kubectl scale rs nginx-rs \
--replicas=5
```

Workflow:

```
Desired = 5

↓

Current = 3

↓

Create 2 Pods

↓

5 Running
```

---

# Scaling Down

Command:

```bash
kubectl scale rs nginx-rs \
--replicas=2
```

Workflow:

```
Desired = 2

↓

Current = 5

↓

Delete 3 Pods

↓

2 Running
```

---

# Label Selectors

ReplicaSets identify Pods using labels.

Example:

ReplicaSet selector:

```yaml
selector:

  matchLabels:

    app: nginx
```

Pod:

```yaml
labels:

  app: nginx
```

Workflow:

```
Label Match

↓

Managed
```

---

# Non-Matching Pods

ReplicaSet:

```
app=nginx
```

Pod:

```
app=apache
```

Result:

```
Ignored
```

Only matching Pods are counted.

---

# Owner References

Every Pod contains:

```
Owner Reference

↓

ReplicaSet
```

This relationship allows Kubernetes to determine which controller owns the Pod.

View:

```bash
kubectl get pod <pod-name> -o yaml
```

Look for:

```yaml
ownerReferences:
```

---

# ReplicaSet Lifecycle

```
ReplicaSet Created

↓

Pods Created

↓

Pods Running

↓

Continuous Monitoring

↓

Scale

↓

Delete
```

---

# Internal Architecture

```
ReplicaSet

↓

Desired Replicas

↓

Selector

↓

Matching Pods

↓

Scheduler

↓

Worker Nodes

↓

Running Pods
```

---

# Self-Healing Architecture

```
Pod Failure

↓

ReplicaSet Detects

↓

Create Replacement

↓

Scheduler

↓

Worker Node

↓

Application Restored
```

This automatic recovery is one of Kubernetes' key features.

---

# Hands-on Lab 1 – Create a ReplicaSet

## Step 1 – Create YAML

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

## Step 2 – Deploy

```bash
kubectl apply -f replicaset.yaml
```

---

## Step 3 – Verify

```bash
kubectl get rs

kubectl get pods
```

Expected:

```
ReplicaSet

↓

3 Pods
```

---

# Hands-on Lab 2 – Observe Self-Healing

Delete one Pod:

```bash
kubectl delete pod <pod-name>
```

Immediately observe:

```bash
kubectl get pods -w
```

Expected:

```
Delete

↓

ReplicaSet Detects

↓

New Pod

↓

Running
```

---

# Hands-on Lab 3 – Scale ReplicaSet

Scale up:

```bash
kubectl scale rs nginx-rs \
--replicas=5
```

Verify:

```bash
kubectl get pods
```

Scale down:

```bash
kubectl scale rs nginx-rs \
--replicas=2
```

Observe Pod deletion.

---

# Hands-on Lab 4 – Describe ReplicaSet

```bash
kubectl describe rs nginx-rs
```

Review:

- Desired replicas
- Current replicas
- Ready replicas
- Pod template
- Events

---

# Hands-on Lab 5 – View Owner References

Choose a Pod:

```bash
kubectl get pod <pod-name> -o yaml
```

Locate:

```yaml
ownerReferences:
```

Confirm that the Pod belongs to the ReplicaSet.

---

# Common Mistakes

## 1. Creating Standalone Pods

Incorrect:

```
Pod

↓

Production
```

Correct:

```
ReplicaSet

↓

Pods
```

---

## 2. Label Mismatch

ReplicaSet:

```yaml
app: nginx
```

Pod:

```yaml
app: web
```

Result:

```
No Match

↓

ReplicaSet Creates Additional Pods
```

---

## 3. Deleting Pods Instead of Investigating

Deleting a managed Pod:

```bash
kubectl delete pod
```

does **not** solve the problem.

ReplicaSet immediately creates another Pod.

---

## 4. Editing Managed Pods

Changes made directly to ReplicaSet-managed Pods are temporary.

If the Pod is recreated:

```
Pod Deleted

↓

New Pod

↓

Changes Lost
```

Update the ReplicaSet (or Deployment) template instead.

---

## 5. Using ReplicaSets Instead of Deployments

ReplicaSets provide:

- Self-healing
- Scaling

Deployments additionally provide:

- Rolling updates
- Rollbacks
- Revision history

Production applications should generally use Deployments.

---

# ReplicaSet Quick Revision

## Architecture

```
ReplicaSet

↓

Desired State

↓

Current State

↓

Compare

↓

Create/Delete Pods

↓

Desired State Restored
```

---

## Lifecycle

```
Create

↓

Pods

↓

Monitor

↓

Scale

↓

Replace Failed Pods

↓

Delete
```

---

## Important Commands

Create:

```bash
kubectl apply -f replicaset.yaml
```

View:

```bash
kubectl get rs

kubectl get pods
```

Describe:

```bash
kubectl describe rs nginx-rs
```

Scale:

```bash
kubectl scale rs nginx-rs \
--replicas=5
```

Delete:

```bash
kubectl delete rs nginx-rs
```

---

# ReplicaSet Checklist

| Topic | Status |
|--------|:------:|
| ReplicaSet Basics | ✓ |
| Desired State | ✓ |
| Label Selectors | ✓ |
| Self-Healing | ✓ |
| Scaling | ✓ |
| Pod Ownership | ✓ |
| Lifecycle | ✓ |
| Hands-on Labs | ✓ |
| Common Mistakes | ✓ |

---

# References

## Official Kubernetes Documentation

- Kubernetes ReplicaSet Documentation
- Kubernetes Controllers
- Labels and Selectors
- Kubernetes API Reference

---

## CNCF Resources

- Kubernetes Learning Path
- Kubernetes Best Practices
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Best Practices
- NIST SP 800-190 — Application Container Security Guide

---

## Recommended Practice

- Create a ReplicaSet with 3 replicas.
- Delete Pods and observe automatic recreation.
- Scale up to 5 replicas, then down to 2.
- Modify labels and observe selector behavior.
- Inspect `ownerReferences` in Pod YAML.
- Compare ReplicaSet behavior with a Deployment in the next chapter.

---

# Chapter Summary

```
ReplicaSet Created

↓

Desired Replicas

↓

ReplicaSet Controller

↓

Create Pods

↓

Scheduler

↓

Worker Nodes

↓

Pods Running

↓

Continuous Monitoring

↓

Self-Healing & Scaling
```

ReplicaSets introduce one of Kubernetes' core capabilities: **automatic reconciliation**. They ensure that the cluster continuously moves toward the desired state by creating or removing Pods as needed. While ReplicaSets are fundamental to Kubernetes, in real-world environments they are almost always managed by **Deployments**, which build on ReplicaSets to provide rolling updates, rollbacks, and application version management.

---
