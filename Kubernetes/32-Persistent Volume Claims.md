# Chapter 32 – Persistent Volume Claims (PVC)

## Overview

In the previous chapter, we learned that a **Persistent Volume (PV)** is a cluster-level storage resource.

However, applications do **not** use Persistent Volumes directly.

Instead, they request storage through a **Persistent Volume Claim (PVC).**

Think of it like renting an apartment.

```
Apartment

↓

Persistent Volume
```

```
Tenant

↓

Persistent Volume Claim
```

The tenant never owns the apartment directly.

Instead, they request one that matches their requirements.

Similarly, applications request storage through a PVC.

Kubernetes automatically finds a matching Persistent Volume and binds them together.

> **Pods use PVCs, and PVCs use Persistent Volumes.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What a PVC is
- Why PVCs are required
- PVC Architecture
- PV-PVC Binding Process
- Storage Requests
- Binding Lifecycle
- Claim Status
- Static vs Dynamic Binding
- Best Practices

---

# Why Do We Need PVCs?

Imagine hundreds of developers sharing one Kubernetes cluster.

Without PVCs:

```
Developer

↓

Chooses Storage

↓

Direct PV Access
```

Problems:

- Storage conflicts
- Manual management
- Security concerns
- Poor scalability

---

## Solution

Use PVCs.

```
Developer

↓

PVC

↓

Kubernetes

↓

Matching PV
```

Developers request storage without knowing implementation details.

---

# What is a Persistent Volume Claim?

A **Persistent Volume Claim (PVC)** is a request for storage.

It specifies requirements such as:

- Capacity
- Access mode
- StorageClass
- Volume mode

Kubernetes searches for a matching Persistent Volume.

---

# High-Level Architecture

```
                 Application

                      │

                      ▼

                     Pod

                      │

                      ▼

         Persistent Volume Claim

                      │

                      ▼

          Persistent Volume (PV)

                      │

                      ▼

              Physical Storage
```

---

# Storage Workflow

```
Developer

↓

Create PVC

↓

Kubernetes

↓

Find Matching PV

↓

Bind

↓

Pod Uses Storage
```

---

# Persistent Volume Claim YAML

```yaml
apiVersion: v1

kind: PersistentVolumeClaim

metadata:

  name: app-pvc

spec:

  accessModes:

  - ReadWriteOnce

  resources:

    requests:

      storage: 5Gi
```

---

# YAML Breakdown

```
requests

↓

5Gi
```

Storage requested.

---

```
accessModes

↓

ReadWriteOnce
```

Required access mode.

---

# PVC Lifecycle

```
Pending

↓

Bound

↓

Released

↓

Deleted
```

---

# Pending State

```
PVC

↓

Searching

↓

Matching PV
```

No suitable PV has been found yet.

---

# Bound State

```
PVC

↓

PV

↓

Connected
```

The claim now has exclusive use of the Persistent Volume.

---

# Released

```
PVC Deleted

↓

PV Released
```

The Persistent Volume enters the Released state.

What happens next depends on the reclaim policy.

---

# Deleted

```
PVC

↓

Removed
```

The associated PV may remain or be deleted depending on its reclaim policy.

---

# Binding Process

```
PVC

↓

Compare Requirements

↓

Find PV

↓

Bind
```

Kubernetes performs this automatically.

---

# Matching Criteria

A PV must satisfy the PVC requirements.

Matching includes:

- Requested capacity
- Access mode
- StorageClass
- Volume mode

Example:

PVC:

```
5Gi
```

PV:

```
10Gi
```

Result:

```
Match
```

The PV can provide more storage than requested.

---

# Capacity Matching

PVC:

```
5Gi
```

PV:

```
2Gi
```

Result:

```
No Match
```

The PV is too small.

---

# Access Mode Matching

PVC:

```
ReadWriteMany
```

PV:

```
ReadWriteOnce
```

Result:

```
No Match
```

The storage backend cannot satisfy the request.

---

# One-to-One Relationship

Normally:

```
One PVC

↓

One PV
```

Once bound, the PV is reserved for that PVC until it is released.

---

# Pod Uses PVC

A Pod references the PVC rather than the PV.

Example:

```yaml
volumes:

- name: app-storage

  persistentVolumeClaim:

    claimName: app-pvc
```

The Pod never needs to know which PV was selected.

---

# Complete Storage Flow

```
Application

↓

Pod

↓

PVC

↓

PV

↓

Storage Backend
```

---

# Static Binding

Administrator creates:

```
Persistent Volume
```

Developer creates:

```
Persistent Volume Claim
```

Kubernetes:

```
Bind
```

---

# Dynamic Binding

Developer creates:

```
PVC
```

No matching PV exists.

StorageClass provisions new storage automatically.

```
PVC

↓

StorageClass

↓

New PV

↓

Bound
```

Dynamic provisioning is covered in a later chapter.

---

# StorageClass Example

PVC:

```yaml
storageClassName: fast-storage
```

Kubernetes searches for:

```
StorageClass

↓

fast-storage
```

If dynamic provisioning is enabled, a new PV is created automatically.

---

# Claim Expansion

Some storage providers support increasing PVC size.

Example:

```
5Gi

↓

10Gi
```

This requires support from the StorageClass and CSI driver.

Shrinking PVCs is generally **not supported**.

---

# Internal Architecture

```
Pod

↓

PersistentVolumeClaim

↓

PersistentVolume

↓

CSI Driver

↓

Storage Backend
```

---

# Real-World Example

E-commerce application:

```
Frontend

↓

PVC

↓

PV

↓

AWS EBS
```

Database:

```
PostgreSQL

↓

PVC

↓

PV

↓

SSD Storage
```

Developers only manage the PVC.

---

# Viewing PVCs

```bash
kubectl get pvc
```

Example:

```
NAME

STATUS

VOLUME

CAPACITY
```

---

# Describe PVC

```bash
kubectl describe pvc app-pvc
```

Observe:

- Status
- Bound PV
- Capacity
- StorageClass
- Events

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f pvc.yaml
```

View:

```bash
kubectl get pvc
```

Describe:

```bash
kubectl describe pvc app-pvc
```

Delete:

```bash
kubectl delete pvc app-pvc
```

---

# PVC Architecture Summary

```
Developer

↓

Persistent Volume Claim

↓

Persistent Volume

↓

Storage
```

---

# Best Practices

### 1. Let Applications Use PVCs

Pods should reference PVCs rather than specific Persistent Volumes.

---

### 2. Request Only Required Capacity

Avoid requesting significantly more storage than necessary.

---

### 3. Use Appropriate Access Modes

Choose the access mode that matches your workload.

---

### 4. Prefer Dynamic Provisioning

In production, StorageClasses simplify storage management.

---

### 5. Monitor PVC Usage

Track:

- Capacity
- Utilization
- Expansion needs
- Pending claims

---

# Hands-on Lab 1 – Create a PVC

Create:

```yaml
resources:

  requests:

    storage: 5Gi
```

Apply:

```bash
kubectl apply -f pvc.yaml
```

Verify:

```bash
kubectl get pvc
```

---

# Hands-on Lab 2 – Observe Pending State

Create a PVC without any matching PV.

Observe:

```
STATUS

↓

Pending
```

---

# Hands-on Lab 3 – Create Matching PV

Create a PV that satisfies the PVC requirements.

Observe:

```
Pending

↓

Bound
```

---

# Hands-on Lab 4 – Mount PVC into a Pod

Create a Pod:

```yaml
volumes:

- persistentVolumeClaim:

    claimName: app-pvc
```

Write data inside the mounted directory.

Delete and recreate the Pod.

Verify that the data persists.

---

# Hands-on Lab 5 – Compare Multiple PVCs

Create:

- 5Gi PVC
- 10Gi PVC
- RWX PVC

Observe which PVs bind successfully.

---

# Common Mistakes

## 1. Mounting PVs Directly

Incorrect:

```
Pod

↓

Persistent Volume
```

Correct:

```
Pod

↓

Persistent Volume Claim

↓

Persistent Volume
```

---

## 2. Requesting Unsupported Access Modes

Example:

```
RWX

↓

Storage Supports Only RWO
```

The PVC remains Pending.

---

## 3. Requesting More Storage Than Available

PVC:

```
100Gi
```

Available PV:

```
20Gi
```

Result:

```
Pending
```

---

## 4. Deleting a PVC Without Understanding the Reclaim Policy

Deleting a PVC may trigger deletion of the underlying storage if the PV reclaim policy is `Delete`.

---

## 5. Assuming PVC Expansion Always Works

PVC resizing depends on:

- StorageClass
- CSI driver
- Underlying storage provider

---

# Quick Revision

## Workflow

```
Developer

↓

PVC

↓

Kubernetes

↓

Matching PV

↓

Bound

↓

Pod
```

---

## Lifecycle

```
Pending

↓

Bound

↓

Released

↓

Deleted
```

---

## Architecture

```
Pod

↓

PVC

↓

PV

↓

Storage
```

---

# Essential kubectl Commands

View PVCs:

```bash
kubectl get pvc
```

Describe PVC:

```bash
kubectl describe pvc <pvc-name>
```

View PVs:

```bash
kubectl get pv
```

Delete PVC:

```bash
kubectl delete pvc <pvc-name>
```

View YAML:

```bash
kubectl get pvc <pvc-name> -o yaml
```

---

# Interview Questions

### Basic

- What is a Persistent Volume Claim?
- Why do Pods use PVCs instead of PVs?
- What is the difference between a PV and a PVC?

---

### Intermediate

- Explain the PVC lifecycle.
- How does Kubernetes bind a PVC to a PV?
- What happens when no matching PV exists?

---

### Advanced

- Explain the complete storage workflow from a Pod to the storage backend.
- Compare static and dynamic provisioning.
- Why is PVC abstraction useful in multi-tenant clusters?
- Which fields are considered during PV-PVC binding?
- Under what conditions can a PVC be resized?

---

# References

## Official Kubernetes Documentation

- Persistent Volume Claims
- Persistent Volumes
- Storage Classes
- Volume Expansion

---

## CNCF Resources

- Kubernetes Storage Concepts
- SIG Storage
- CSI Documentation
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- Kubernetes Storage Best Practices
- CIS Kubernetes Benchmark
- NIST SP 800-190

---

## Recommended Practice

1. Create PVCs with different storage requests.
2. Observe Pending and Bound states.
3. Experiment with matching and non-matching access modes.
4. Mount PVCs into Pods and verify data persistence across Pod recreation.
5. Prepare for StorageClasses and dynamic provisioning by comparing manual and automatic storage workflows.

---

# Chapter Summary

```
Developer

↓

Persistent Volume Claim

↓

Persistent Volume

↓

Storage Backend

↓

Pod
```

A **Persistent Volume Claim (PVC)** provides a storage abstraction that allows applications to request storage without knowing the underlying implementation. Kubernetes automatically binds PVCs to suitable Persistent Volumes, enabling portable, scalable, and maintainable storage management while separating application concerns from infrastructure management.

---

## Next Chapter

**Chapter 33 – Storage Classes**

Topics include:

- What is a StorageClass?
- Static vs Dynamic Provisioning
- Provisioners
- Default StorageClass
- Volume Binding Modes
- Reclaim Policies
- Production Storage Workflows
- Hands-on Labs
- Interview Questions

---