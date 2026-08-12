# Chapter 33 – Storage Classes

## Overview

In the previous chapters, we learned:

```text
Volume
   ↓
Persistent Volume (PV)
   ↓
Persistent Volume Claim (PVC)
```

With **static provisioning**, an administrator must manually create Persistent Volumes before applications can use them.

Imagine a production cluster with hundreds of applications.

Manually creating:

```text
PV 1
PV 2
PV 3
PV 4
...
PV 500
```

would be difficult to manage.

Kubernetes solves this problem with **StorageClasses**.

A **StorageClass** describes a class or type of storage that can be dynamically provisioned.

Instead of an administrator creating a PV first:

```text
Administrator
    ↓
Create PV
    ↓
Developer creates PVC
```

the developer can simply create:

```text
PVC
 ↓
StorageClass
 ↓
Provisioner / CSI Driver
 ↓
New PV
 ↓
Storage Backend
```

> **StorageClass is the mechanism Kubernetes uses to describe how storage should be dynamically provisioned.**

---

# Learning Objectives

After completing this chapter, you will understand:

* What a StorageClass is
* Why StorageClasses are needed
* Static vs Dynamic Provisioning
* StorageClass Architecture
* Provisioners
* CSI Drivers
* Default StorageClass
* Parameters
* Reclaim Policies
* Volume Binding Modes
* Allow Volume Expansion
* StorageClass Selection
* Production Best Practices

---

# Why Do We Need StorageClasses?

Without StorageClasses:

```text
Administrator

↓

Create PV

↓

Developer

↓

Create PVC
```

This requires manual infrastructure management.

With StorageClasses:

```text
Developer

↓

PVC

↓

StorageClass

↓

Automatic Storage Provisioning

↓

PV
```

The infrastructure can create storage automatically.

---

# What is a StorageClass?

A **StorageClass** is a Kubernetes object that defines a category of storage and the parameters required to provision it.

It can specify:

* Provisioner
* Storage backend parameters
* Reclaim policy
* Volume binding mode
* Volume expansion support
* Allowed topologies

---

# High-Level Architecture

```text
                    Application

                         │

                         ▼

                        Pod

                         │

                         ▼

                        PVC

                         │
                         ▼
                  StorageClass
                         │
                         ▼
                   CSI Driver
                         │
                         ▼
                   Storage Backend
                         │
                         ▼
                        PV
```

---

# Static vs Dynamic Provisioning

## Static Provisioning

```text
Administrator

↓

Create PV

↓

Developer creates PVC

↓

PVC binds to PV
```

---

## Dynamic Provisioning

```text
Developer

↓

Create PVC

↓

StorageClass

↓

CSI Provisioner

↓

Create Storage

↓

Create PV

↓

Bind PVC
```

Dynamic provisioning is the preferred approach for most modern production environments.

---

# StorageClass YAML

Example:

```yaml
apiVersion: storage.k8s.io/v1

kind: StorageClass

metadata:
  name: fast-storage

provisioner: example.com/fast

reclaimPolicy: Delete

volumeBindingMode: WaitForFirstConsumer

allowVolumeExpansion: true
```

The exact `provisioner` depends on the storage implementation.

---

# StorageClass Components

A StorageClass commonly contains:

```text
StorageClass

├── provisioner
├── parameters
├── reclaimPolicy
├── volumeBindingMode
├── allowVolumeExpansion
└── allowedTopologies
```

---

# Provisioner

The `provisioner` identifies the component responsible for creating storage.

Modern Kubernetes storage commonly uses **CSI drivers**.

Conceptually:

```text
StorageClass

↓

CSI Driver

↓

Storage Backend
```

Examples include drivers for:

* AWS EBS
* Azure Disk
* Azure Files
* Google Persistent Disk
* Ceph
* NFS
* NetApp
* VMware

The exact provisioner name is implementation-specific.

---

# Parameters

StorageClasses can pass parameters to the provisioner.

For example, a cloud storage implementation may support parameters representing:

```text
Storage Type
Disk Performance
Replication
Encryption
Filesystem
```

Example conceptually:

```yaml
parameters:
  type: fast
```

The supported parameters depend on the provisioner.

---

# Reclaim Policy

StorageClasses can define the default reclaim behavior of dynamically created PVs.

Common values:

```text
Delete
```

and:

```text
Retain
```

---

## Delete

```text
PVC Deleted

↓

PV Deleted

↓

Underlying Storage Deleted
```

Useful when storage should automatically be cleaned up.

---

## Retain

```text
PVC Deleted

↓

PV Retained

↓

Underlying Data Preserved
```

Useful for critical data where accidental deletion must be avoided.

---

# Volume Binding Mode

StorageClasses can define when a dynamically provisioned volume should be created and bound.

Two important modes are:

```text
Immediate
```

and:

```text
WaitForFirstConsumer
```

---

# Immediate

With:

```yaml
volumeBindingMode: Immediate
```

the storage can be provisioned as soon as the PVC is created.

Workflow:

```text
PVC Created

↓

Storage Provisioned

↓

PV Created

↓

PVC Bound
```

---

# WaitForFirstConsumer

With:

```yaml
volumeBindingMode: WaitForFirstConsumer
```

Kubernetes waits until a Pod actually uses the PVC before provisioning/binding the storage.

Workflow:

```text
PVC Created

↓

Wait

↓

Pod Created

↓

Scheduler Determines Placement

↓

Storage Provisioned

↓

PV Bound
```

This is especially important when storage is constrained by topology, such as:

* Availability Zones
* Regions
* Nodes
* Local storage

---

# Why WaitForFirstConsumer Matters

Imagine a cluster:

```text
Zone A

Zone B

Zone C
```

A storage volume is created in Zone A.

But the Pod is scheduled to Zone C.

Result:

```text
Pod

↓

Zone C

X

Storage

↓

Zone A
```

The Pod may not be able to attach the volume.

`WaitForFirstConsumer` allows scheduling and storage provisioning to take topology into account.

---

# Allow Volume Expansion

A StorageClass may support volume expansion:

```yaml
allowVolumeExpansion: true
```

Example:

```text
20Gi

↓

50Gi
```

This allows supported PVCs to request more storage.

Important:

```text
Expansion

✅ Supported by some backends

❌ Not universally available
```

Shrinking a PVC is generally not supported.

---

# Allowed Topologies

A StorageClass can restrict where storage may be provisioned.

Example concept:

```text
Zone A
Zone B
```

This is useful for:

* Multi-zone clusters
* Local storage
* Cloud block storage
* Topology-aware applications

---

# Default StorageClass

A Kubernetes cluster can have a **default StorageClass**.

If a PVC does not specify:

```yaml
storageClassName:
```

Kubernetes may use the default StorageClass.

---

# View StorageClasses

```bash
kubectl get storageclass
```

Short form:

```bash
kubectl get sc
```

Example:

```text
NAME            PROVISIONER        RECLAIMPOLICY
standard        example.com/csi    Delete
fast-storage    example.com/csi    Delete
```

---

# Describe StorageClass

```bash
kubectl describe storageclass fast-storage
```

or:

```bash
kubectl describe sc fast-storage
```

---

# Marking a Default StorageClass

A StorageClass is commonly marked as default using an annotation.

Conceptually:

```yaml
metadata:
  annotations:
    storageclass.kubernetes.io/is-default-class: "true"
```

Check:

```bash
kubectl get storageclass
```

The default class is typically shown with:

```text
(default)
```

---

# PVC Using a StorageClass

Example:

```yaml
apiVersion: v1

kind: PersistentVolumeClaim

metadata:
  name: database-pvc

spec:
  storageClassName: fast-storage

  accessModes:
    - ReadWriteOnce

  resources:
    requests:
      storage: 20Gi
```

Workflow:

```text
PVC

↓

fast-storage

↓

Provisioner

↓

Storage

↓

PV

↓

PVC Bound
```

---

# PVC Without StorageClass

Example:

```yaml
spec:
  accessModes:
    - ReadWriteOnce

  resources:
    requests:
      storage: 20Gi
```

If a default StorageClass exists:

```text
PVC

↓

Default StorageClass

↓

Dynamic Provisioning
```

---

# Explicitly Requesting No StorageClass

A PVC can explicitly disable dynamic provisioning with:

```yaml
storageClassName: ""
```

This is different from simply omitting the field.

Conceptually:

```text
storageClassName omitted

↓

Default StorageClass may be used
```

while:

```text
storageClassName: ""

↓

Do not use a StorageClass
```

This distinction is important during troubleshooting.

---

# Multiple StorageClasses

A cluster can have multiple storage classes.

Example:

```text
standard
```

```text
fast-ssd
```

```text
high-iops
```

```text
shared-filesystem
```

Applications select the appropriate class.

---

# Example Architecture

```text
                   Kubernetes Cluster

          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼

      standard        fast-ssd       shared-rwx

          │              │              │
          ▼              ▼              ▼

      Standard        SSD Storage     Shared FS
```

---

# Real-World Example

Consider a database.

Requirements:

```text
High Performance
ReadWriteOnce
SSD
```

The application requests:

```yaml
storageClassName: fast-ssd
```

The workflow becomes:

```text
PostgreSQL

↓

PVC

↓

fast-ssd

↓

CSI Driver

↓

Cloud Block Storage

↓

PV
```

The application does not need to know how the underlying storage is created.

---

# StorageClass and CSI

Modern Kubernetes storage commonly follows:

```text
PVC

↓

StorageClass

↓

CSI Driver

↓

Storage Backend
```

The StorageClass tells the CSI-based provisioning system **what kind of storage to create**.

The CSI driver performs the storage operations.

---

# StorageClass Parameters vs PVC Parameters

PVC generally specifies:

```text
How much storage is required
```

and:

```text
How it will be accessed
```

StorageClass generally specifies:

```text
How the storage should be provisioned
```

Example:

```text
PVC

↓

20Gi

↓

ReadWriteOnce
```

StorageClass:

```text
SSD

↓

Encrypted

↓

Specific topology
```

---

# StorageClass Lifecycle

StorageClass itself does not represent a physical disk.

It is a **configuration object**.

```text
StorageClass Created

↓

PVC References It

↓

Provisioning Requested

↓

CSI Driver Creates Storage

↓

PV Created

↓

PVC Bound
```

---

# Hands-on Lab 1 – View StorageClasses

Run:

```bash
kubectl get storageclass
```

or:

```bash
kubectl get sc
```

Identify:

* Name
* Provisioner
* Reclaim Policy
* Binding Mode

---

# Hands-on Lab 2 – Describe a StorageClass

```bash
kubectl describe sc <storage-class-name>
```

Inspect:

```text
Provisioner
Parameters
Reclaim Policy
Volume Binding Mode
Allow Volume Expansion
```

---

# Hands-on Lab 3 – Create a PVC

Create:

```yaml
apiVersion: v1

kind: PersistentVolumeClaim

metadata:
  name: dynamic-pvc

spec:
  storageClassName: fast-storage

  accessModes:
    - ReadWriteOnce

  resources:
    requests:
      storage: 5Gi
```

Apply:

```bash
kubectl apply -f pvc.yaml
```

Check:

```bash
kubectl get pvc
```

---

# Hands-on Lab 4 – Observe Dynamic Provisioning

Run:

```bash
kubectl get pvc
```

Then:

```bash
kubectl get pv
```

You should observe:

```text
PVC

↓

PV
```

being created automatically if the StorageClass and provisioner are configured correctly.

---

# Hands-on Lab 5 – Inspect Events

If the PVC remains Pending:

```bash
kubectl describe pvc dynamic-pvc
```

Look at:

```text
Events
```

Common causes include:

* Missing CSI driver
* Incorrect provisioner
* Unsupported parameters
* No available storage backend
* Topology constraints

---

# Hands-on Lab 6 – Test PVC Expansion

If your StorageClass supports expansion:

```yaml
allowVolumeExpansion: true
```

Increase the PVC request:

```text
5Gi

↓

10Gi
```

Then:

```bash
kubectl get pvc
```

Observe the new capacity.

---

# Common Mistakes

## 1. Confusing StorageClass with Storage

A StorageClass is **not a disk**.

It describes how storage should be provisioned.

```text
StorageClass

≠

Physical Storage
```

---

## 2. Assuming Every Cluster Has the Same StorageClasses

StorageClasses depend on:

* Kubernetes distribution
* Cloud provider
* CSI drivers
* Cluster configuration

A StorageClass available in one cluster may not exist in another.

---

## 3. Using the Wrong Provisioner

If the provisioner does not exist:

```text
PVC

↓

Pending
```

---

## 4. Forgetting the Default StorageClass

A PVC without an explicit StorageClass may remain Pending if no suitable default provisioning mechanism exists.

---

## 5. Using Immediate Binding for Topology-Constrained Storage

This can create storage in a location where the Pod cannot run.

Prefer:

```text
WaitForFirstConsumer
```

when appropriate.

---

## 6. Assuming Volume Expansion Always Works

Both the StorageClass and underlying CSI driver must support expansion.

---

## 7. Assuming StorageClass Creates a PV Immediately

With:

```text
WaitForFirstConsumer
```

the PVC may remain Pending until a Pod consumes it.

That can be expected behavior.

---

# Quick Revision

## Static Provisioning

```text
Administrator

↓

PV

↓

PVC

↓

Pod
```

---

## Dynamic Provisioning

```text
PVC

↓

StorageClass

↓

CSI Driver

↓

Storage Backend

↓

PV

↓

Pod
```

---

## Important Fields

```text
provisioner
reclaimPolicy
volumeBindingMode
allowVolumeExpansion
parameters
allowedTopologies
```

---

# Essential kubectl Commands

List StorageClasses:

```bash
kubectl get storageclass
```

Short form:

```bash
kubectl get sc
```

Describe:

```bash
kubectl describe sc <name>
```

List PVCs:

```bash
kubectl get pvc
```

List PVs:

```bash
kubectl get pv
```

View StorageClass YAML:

```bash
kubectl get sc <name> -o yaml
```

---

# Interview Questions

## Basic

* What is a StorageClass?
* Why do we need StorageClasses?
* What is the difference between a StorageClass and a Persistent Volume?

---

## Intermediate

* What is dynamic provisioning?
* What is a provisioner?
* What is the difference between `Immediate` and `WaitForFirstConsumer`?
* What is a default StorageClass?
* What is `allowVolumeExpansion`?

---

## Advanced

* Explain the complete workflow from PVC creation to dynamic PV provisioning.
* Why is `WaitForFirstConsumer` important for topology-aware storage?
* How does a StorageClass interact with a CSI driver?
* What happens when a PVC references a nonexistent StorageClass?
* Why might a PVC remain Pending even though a StorageClass exists?
* Explain the difference between omitting `storageClassName` and setting it to `""`.
* How would you design multiple StorageClasses for a production cluster?

---

# Production StorageClass Design

A production cluster may have:

```text
                    StorageClasses

             ┌──────────┼──────────┐
             │          │          │
             ▼          ▼          ▼

         standard    fast-ssd    shared-rwx

             │          │          │
             ▼          ▼          ▼

          General     Database    Shared Apps
          Workloads   Workloads
```

Example usage:

```text
Frontend

↓

standard
```

```text
PostgreSQL

↓

fast-ssd
```

```text
Shared Content

↓

shared-rwx
```

This allows application teams to request storage based on workload requirements rather than infrastructure implementation.

---

# Best Practices

### 1. Define Storage Classes Based on Workload

Create classes such as:

```text
standard
fast
high-iops
shared
```

only when they represent meaningful differences in storage behavior.

---

### 2. Prefer CSI-Based Storage

Modern Kubernetes environments should generally use actively maintained CSI drivers rather than legacy in-tree storage integrations.

---

### 3. Use WaitForFirstConsumer Where Appropriate

Especially for topology-aware storage.

---

### 4. Carefully Choose Reclaim Policies

For disposable application data:

```text
Delete
```

For critical data:

```text
Retain
```

---

### 5. Enable Expansion Where Supported

Use:

```yaml
allowVolumeExpansion: true
```

when the storage backend supports safe online or offline expansion as appropriate.

---

### 6. Monitor Provisioning Failures

Monitor:

* Pending PVCs
* CSI controller errors
* Volume attachment failures
* Provisioning latency
* Storage capacity

---

# References

## Official Kubernetes Documentation

* Storage Classes
* Persistent Volumes
* Persistent Volume Claims
* Dynamic Volume Provisioning
* Volume Expansion
* Storage Topology

---

## CNCF Resources

* Kubernetes SIG Storage
* Container Storage Interface
* Kubernetes Storage Concepts
* Cloud Native Computing Foundation (CNCF)

---

## CSI Ecosystem

StorageClass behavior depends heavily on the CSI driver being used.

Examples include drivers for:

* AWS EBS
* Azure Disk
* Azure Files
* Google Persistent Disk
* Ceph
* NFS
* NetApp
* VMware

Always consult the documentation for the specific CSI driver when configuring production parameters.

---

# Recommended Practice

1. List all StorageClasses in your cluster.
2. Identify the default StorageClass.
3. Inspect its provisioner and parameters.
4. Create a PVC referencing a specific StorageClass.
5. Observe automatic PV creation.
6. Compare `Immediate` and `WaitForFirstConsumer`.
7. Test PVC expansion if supported.
8. Delete a test PVC and observe the reclaim behavior.
9. Investigate a deliberately broken PVC using `kubectl describe pvc`.
10. Create separate StorageClasses for different workload requirements in a lab cluster.

---

# Chapter Summary

```text
                    PVC
                     │
                     ▼
               StorageClass
                     │
                     ▼
                CSI Driver
                     │
                     ▼
             Storage Backend
                     │
                     ▼
                     PV
                     │
                     ▼
                    Pod
```

A **StorageClass** provides the abstraction required for **dynamic storage provisioning** in Kubernetes. Instead of administrators manually creating Persistent Volumes for every application, developers can create PVCs that reference an appropriate StorageClass. Kubernetes then works with the configured provisioner or CSI driver to create and bind the required storage.

The most important concepts to remember are:

```text
StorageClass
    ↓
Defines HOW storage is provisioned

PVC
    ↓
Defines WHAT storage the application requests

CSI Driver
    ↓
Implements storage operations

PV
    ↓
Represents the provisioned storage
```

---

## Next Chapter

# Chapter 34 – Dynamic Provisioning

Topics:

* What Dynamic Provisioning Actually Does
* Complete PVC → StorageClass → CSI → PV Workflow
* Provisioning Lifecycle
* CSI Provisioner
* Volume Creation
* Volume Attachment
* Volume Mounting
* Topology-Aware Provisioning
* `WaitForFirstConsumer`
* Volume Expansion
* Reclaim Behavior
* Hands-on Labs
* Troubleshooting
* Common Mistakes
* Quick Revision
* Interview Questions
* References

---
