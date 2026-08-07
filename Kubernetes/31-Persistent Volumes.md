# Chapter 31 – Persistent Volumes (PV)

## Overview

In the previous chapter, we learned about **Volumes**.

Most volume types like:

- emptyDir
- ConfigMap
- Secret
- Projected

are **Pod-scoped**.

When the Pod is deleted:

```
Pod

↓

Deleted

↓

Volume

↓

Deleted
```

This is acceptable for temporary data but **not for critical application data**.

Imagine a MySQL database:

```
Pod

↓

Database Files
```

If the Pod is deleted:

```
Database

↓

Lost
```

This is unacceptable in production.

Kubernetes solves this problem using **Persistent Volumes (PV)**.

A **Persistent Volume** is a cluster-wide storage resource that exists independently of any Pod.

> **A Persistent Volume is owned by the cluster, not by a Pod.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Persistent Volume (PV) is
- Why Persistent Volumes are needed
- PV Architecture
- Static Provisioning
- PV Lifecycle
- Storage Capacity
- Access Modes
- Reclaim Policies
- Volume Binding
- Best Practices

---

# Why Do We Need Persistent Volumes?

Consider a database application.

```
Database Pod

↓

Stores Data
```

Pod crashes:

```
Pod Deleted
```

If using `emptyDir`:

```
Database

↓

Lost
```

---

## Solution

Store the data on a Persistent Volume.

```
Database Pod

↓

Persistent Volume

↓

Physical Storage
```

If the Pod is recreated:

```
New Pod

↓

Same Persistent Volume

↓

Data Preserved
```

---

# What is a Persistent Volume?

A **Persistent Volume (PV)** is a storage resource managed by the Kubernetes cluster.

Characteristics:

- Independent of Pods
- Independent of containers
- Can outlive Pod deletion
- Represents actual storage
- Can be reused

---

# High-Level Architecture

```
                  Kubernetes Cluster

        ┌──────────────────────────────────┐

        │                                  │

        │    Persistent Volume (PV)         │

        │                                  │

        └───────────────┬──────────────────┘
                        │
                        ▼
                Physical Storage

        AWS EBS / Azure Disk / NFS /
        Ceph / SAN / Local Disk
```

The PV represents real storage infrastructure.

---

# Persistent Storage Architecture

```
Application

↓

Pod

↓

Persistent Volume Claim (PVC)

↓

Persistent Volume (PV)

↓

Storage Backend
```

> A Pod does **not** use a PV directly.
>
> It accesses storage through a **Persistent Volume Claim (PVC)**.

PVCs are covered in the next chapter.

---

# Static Provisioning

Originally, storage administrators created Persistent Volumes manually.

Workflow:

```
Administrator

↓

Create PV

↓

Developers Use It
```

This is called:

```
Static Provisioning
```

---

# Persistent Volume Lifecycle

```
Create

↓

Available

↓

Bound

↓

Released

↓

Reclaimed
```

Each state represents a different phase of the PV lifecycle.

---

# Lifecycle States

### Available

```
PV

↓

Waiting
```

No claim is using it.

---

### Bound

```
PVC

↓

Connected

↓

PV
```

The storage is reserved for one claim.

---

### Released

```
PVC Deleted

↓

PV Released
```

The data may still exist depending on the reclaim policy.

---

### Failed

The PV encountered an error or cannot be reclaimed successfully.

---

# Persistent Volume YAML

```yaml
apiVersion: v1

kind: PersistentVolume

metadata:

  name: app-pv

spec:

  capacity:

    storage: 10Gi

  accessModes:

  - ReadWriteOnce

  persistentVolumeReclaimPolicy: Retain

  hostPath:

    path: /data/app
```

---

# YAML Breakdown

```
capacity

↓

10Gi
```

Defines storage size.

---

```
accessModes

↓

ReadWriteOnce
```

Defines how the storage may be mounted.

---

```
persistentVolumeReclaimPolicy

↓

Retain
```

Defines what happens after the claim is deleted.

---

```
hostPath
```

Specifies the storage backend for this example.

In production, cloud or network storage is generally preferred.

---

# Storage Capacity

Example:

```
10Gi
```

Meaning:

```
10 Gigabytes
```

Other examples:

```
20Gi
```

```
100Gi
```

```
1Ti
```

Capacity represents the maximum storage available through the PV.

---

# Access Modes

Kubernetes defines how a volume may be mounted.

### ReadWriteOnce (RWO)

```
One Node

↓

Read + Write
```

Most block storage systems use this mode.

---

### ReadOnlyMany (ROX)

```
Many Nodes

↓

Read Only
```

Suitable for shared read-only content.

---

### ReadWriteMany (RWX)

```
Many Nodes

↓

Read + Write
```

Typically provided by shared filesystems such as NFS, CephFS, or Azure Files.

---

### ReadWriteOncePod (RWOP)

```
One Pod

↓

Read + Write
```

Ensures only a single Pod in the cluster can mount the volume for read-write access.

Useful for preventing accidental concurrent writers.

---

# Access Mode Comparison

| Mode | Nodes | Read | Write |
|------|-------|------|-------|
| RWO | One | ✅ | ✅ |
| ROX | Many | ✅ | ❌ |
| RWX | Many | ✅ | ✅ |
| RWOP | One Pod | ✅ | ✅ |

> The actual access modes available depend on the storage backend.

---

# Storage Backend Examples

A PV can represent storage from many providers.

Examples:

```
AWS EBS
```

```
Azure Disk
```

```
Azure Files
```

```
Google Persistent Disk
```

```
NFS
```

```
Ceph
```

```
iSCSI
```

```
Local Disk
```

```
Fibre Channel
```

---

# hostPath Example

```
Worker Node

↓

/data

↓

Persistent Volume
```

Suitable for:

- Development
- Single-node clusters
- Local testing

Not recommended for highly available production workloads.

---

# NFS Example

```
Multiple Nodes

↓

NFS Server

↓

Persistent Volume
```

Supports:

```
ReadWriteMany
```

---

# Cloud Storage Example

```
AWS EBS

↓

Persistent Volume

↓

Database Pod
```

Cloud providers often create PVs dynamically through Storage Classes.

---

# Reclaim Policies

A reclaim policy determines what happens when the PVC is deleted.

Three options exist.

---

## Retain

```
PVC Deleted

↓

PV Exists

↓

Data Preserved
```

Administrator intervention is required before reuse.

Suitable for critical data.

---

## Delete

```
PVC Deleted

↓

PV Deleted

↓

Storage Deleted
```

Commonly used with dynamically provisioned cloud storage.

---

## Recycle (Deprecated)

Previously:

```
Delete Data

↓

Reuse PV
```

This policy has been deprecated and should not be used.

---

# Volume Binding

Workflow:

```
PVC

↓

Matches PV

↓

Bound
```

Binding occurs automatically when requirements match.

---

# Matching Criteria

A PVC matches a PV based on factors such as:

- Storage capacity
- Access modes
- StorageClass (if applicable)
- Volume mode

---

# Internal Architecture

```
Pod

↓

PVC

↓

PV

↓

Storage Backend
```

Pods never interact with physical storage directly.

---

# Real-World Example

Production database:

```
MySQL

↓

PVC

↓

Persistent Volume

↓

AWS EBS
```

Even if the Pod restarts:

```
Data

↓

Still Exists
```

---

# View Persistent Volumes

```bash
kubectl get pv
```

Example:

```
NAME

CAPACITY

ACCESS MODES

STATUS
```

---

# Describe Persistent Volume

```bash
kubectl describe pv app-pv
```

Observe:

- Capacity
- Access modes
- Reclaim policy
- Storage backend
- Status

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f pv.yaml
```

View:

```bash
kubectl get pv
```

Describe:

```bash
kubectl describe pv app-pv
```

Delete:

```bash
kubectl delete pv app-pv
```

---

# Persistent Volume Architecture Summary

```
Application

↓

Pod

↓

PVC

↓

Persistent Volume

↓

Physical Storage
```

---

# Best Practices

### 1. Use Persistent Volumes for Important Data

Examples:

- Databases
- User uploads
- Business documents
- ML datasets

---

### 2. Prefer Dynamic Provisioning

Manual PV creation is useful for learning but dynamic provisioning is preferred in production.

---

### 3. Choose the Correct Access Mode

Match the application's sharing requirements to the storage backend.

---

### 4. Use `Retain` for Critical Data

Prevent accidental deletion of valuable information.

---

### 5. Monitor Storage Capacity

Track:

- Available space
- Volume utilization
- Growth trends

---

# Hands-on Lab 1 – Create a Persistent Volume

Create:

```yaml
capacity:

  storage: 5Gi
```

Verify:

```bash
kubectl get pv
```

---

# Hands-on Lab 2 – Describe the PV

```bash
kubectl describe pv app-pv
```

Observe:

- Status
- Capacity
- Access mode
- Reclaim policy

---

# Hands-on Lab 3 – Compare Reclaim Policies

Create test PVs using:

- `Retain`
- `Delete`

Observe behavior after deleting the associated PVC (covered in the next chapter).

---

# Hands-on Lab 4 – Create Multiple PVs

Create:

- 5Gi
- 10Gi
- 20Gi

Compare capacities and binding behavior.

---

# Hands-on Lab 5 – Observe Lifecycle

Watch the PV status change as PVCs are created and deleted in later chapters.

---

# Common Mistakes

## 1. Confusing PV with a Volume

A regular Volume is Pod-scoped.

A Persistent Volume is cluster-scoped.

---

## 2. Mounting a PV Directly into a Pod

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

PVC

↓

Persistent Volume
```

---

## 3. Using `hostPath` for Production Databases

`hostPath` ties storage to a single Node and lacks high availability.

---

## 4. Choosing the Wrong Access Mode

Example:

```
RWX

↓

Requested

↓

Storage Supports Only RWO
```

The claim cannot bind.

---

## 5. Using `Delete` for Critical Data

Deleting the PVC may also remove the underlying storage, depending on the backend and reclaim policy.

---

# Quick Revision

## Storage Flow

```
Application

↓

Pod

↓

PVC

↓

PV

↓

Storage
```

---

## Lifecycle

```
Available

↓

Bound

↓

Released

↓

Reclaimed
```

---

## Reclaim Policies

```
Retain

Delete

Recycle (Deprecated)
```

---

# Essential kubectl Commands

View PVs:

```bash
kubectl get pv
```

Describe PV:

```bash
kubectl describe pv <pv-name>
```

Delete PV:

```bash
kubectl delete pv <pv-name>
```

View YAML:

```bash
kubectl get pv <pv-name> -o yaml
```

---

# Interview Questions

### Basic

- What is a Persistent Volume?
- Why do we need a PV?
- What is the difference between a Volume and a Persistent Volume?

---

### Intermediate

- Explain the lifecycle of a Persistent Volume.
- What are the available access modes?
- What is the purpose of a reclaim policy?

---

### Advanced

- Explain the complete storage architecture from Pod to storage backend.
- Compare static and dynamic provisioning.
- Why can't a Pod use a PV directly?
- How does Kubernetes bind a PV to a PVC?
- Which reclaim policy would you choose for a production database, and why?

---

# References

## Official Kubernetes Documentation

- Persistent Volumes
- Storage Concepts
- Volume Access Modes
- Reclaim Policies

---

## CNCF Resources

- Kubernetes Storage
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

1. Create multiple Persistent Volumes with different capacities.
2. Experiment with different access modes.
3. Compare reclaim policies in a lab environment.
4. Observe PV lifecycle transitions.
5. Prepare for the next chapter by creating PVCs that bind to existing PVs.

---

# Chapter Summary

```
Application

↓

Pod

↓

Persistent Volume Claim

↓

Persistent Volume

↓

Physical Storage
```

A **Persistent Volume (PV)** is a cluster-managed storage resource that provides durable storage independent of Pod lifecycles. By separating storage from applications, Kubernetes enables reliable data persistence for stateful workloads while supporting multiple storage backends, configurable access modes, and flexible reclaim policies.

---

## Next Chapter

**Chapter 32 – Persistent Volume Claims (PVC)**

Topics include:

- What is a PVC?
- PV-PVC Binding Process
- Claim Lifecycle
- Static vs Dynamic Binding
- Storage Requests
- Binding Algorithm
- Production Workflows
- Hands-on Labs
- Interview Questions

---