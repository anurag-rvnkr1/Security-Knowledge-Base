# Chapter 34 – Dynamic Provisioning

## Overview

In the previous chapters, we learned:

```text
Volume
   ↓
Persistent Volume (PV)
   ↓
Persistent Volume Claim (PVC)
   ↓
StorageClass
```

A **Persistent Volume** can be created manually by an administrator. This is called **static provisioning**.

However, manually creating PVs does not scale well.

Imagine a production cluster with hundreds of applications:

```text
Application 1 → PV
Application 2 → PV
Application 3 → PV
...
Application 500 → PV
```

An administrator would have to continuously:

* Create storage
* Create PV objects
* Configure capacity
* Configure access modes
* Configure storage backends
* Manage lifecycle
* Reclaim unused storage

Kubernetes provides **Dynamic Provisioning** to automate this process.

With dynamic provisioning, an application creates a PVC and Kubernetes automatically requests the required storage from the configured storage system.

```text
Developer

↓

PVC

↓

StorageClass

↓

CSI Provisioner

↓

Storage Backend

↓

Persistent Volume

↓

PVC Bound
```

> **Dynamic provisioning automatically creates storage and its corresponding Persistent Volume when a PVC requests a StorageClass capable of provisioning it.**

---

# Learning Objectives

After completing this chapter, you will understand:

* What dynamic provisioning is
* Static vs dynamic provisioning
* Complete dynamic provisioning workflow
* StorageClass interaction
* CSI provisioner
* Volume creation
* PV creation
* PVC binding
* Volume attachment
* Volume mounting
* Topology-aware provisioning
* `WaitForFirstConsumer`
* Volume expansion
* Reclaim behavior
* Troubleshooting dynamic provisioning

---

# Why Do We Need Dynamic Provisioning?

## Static Provisioning

```text
Administrator

↓

Create Physical Storage

↓

Create PV

↓

Developer

↓

Create PVC

↓

Bind
```

This requires manual work.

---

## Dynamic Provisioning

```text
Developer

↓

Create PVC

↓

StorageClass

↓

CSI Driver

↓

Create Storage

↓

Create PV

↓

Bind PVC
```

No administrator needs to manually create a PV for every application.

---

# Static vs Dynamic Provisioning

| Static Provisioning           | Dynamic Provisioning                    |
| ----------------------------- | --------------------------------------- |
| Administrator creates PV      | Kubernetes provisions storage           |
| Manual process                | Automated                               |
| Harder to scale               | Scales easily                           |
| Requires pre-created capacity | Storage created on demand               |
| Useful for special storage    | Preferred for many production workloads |

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

                  CSI Provisioner

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

# Complete Dynamic Provisioning Workflow

```text
1. Developer creates PVC
            ↓
2. PVC references StorageClass
            ↓
3. Kubernetes detects provisioning request
            ↓
4. CSI provisioner receives request
            ↓
5. Storage backend creates volume
            ↓
6. PV object is created
            ↓
7. PVC binds to PV
            ↓
8. Pod references PVC
            ↓
9. Volume is attached
            ↓
10. Volume is mounted
            ↓
11. Application uses storage
```

---

# Step 1 – Developer Creates PVC

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

The developer is requesting:

```text
20Gi

ReadWriteOnce

fast-storage
```

The developer does not need to manually create a PV.

---

# Step 2 – Kubernetes Finds StorageClass

PVC:

```text
storageClassName: fast-storage
```

Kubernetes looks for:

```text
StorageClass

↓

fast-storage
```

The StorageClass contains information about how storage should be provisioned.

---

# Step 3 – Provisioner Receives Request

The StorageClass identifies the provisioner.

Conceptually:

```text
PVC

↓

StorageClass

↓

Provisioner
```

The provisioner communicates with the storage system.

Modern Kubernetes environments commonly use CSI drivers.

---

# Step 4 – CSI Driver Creates Storage

The CSI driver requests storage from the backend.

Example:

```text
CSI Driver

↓

Cloud Block Storage

↓

20Gi Volume
```

The exact process depends on the storage provider.

---

# Step 5 – Storage Backend Creates Volume

The storage platform creates the actual storage resource.

Example:

```text
20Gi SSD Volume
```

At this point, the physical or virtual storage exists outside the Kubernetes API objects.

---

# Step 6 – Kubernetes Creates PV

After successful provisioning:

```text
Storage Backend

↓

New Volume

↓

PersistentVolume Object
```

The PV represents the newly created storage inside Kubernetes.

Example:

```text
PV

↓

20Gi

↓

ReadWriteOnce

↓

fast-storage
```

---

# Step 7 – PVC Becomes Bound

The PVC now connects to the newly created PV.

```text
PVC

       ↕

PV
```

Check:

```bash
kubectl get pvc
```

You should see:

```text
STATUS

Bound
```

---

# Step 8 – Pod Uses PVC

The application Pod references:

```yaml
volumes:

- name: database-storage

  persistentVolumeClaim:

    claimName: database-pvc
```

The Pod does not need to know the underlying storage provider.

---

# Step 9 – Volume Attachment

If the storage backend requires attachment, Kubernetes coordinates attaching the volume to the Node where the Pod is running.

Conceptually:

```text
Pod

↓

Node

↓

VolumeAttachment

↓

Storage Device
```

This process is handled through the CSI ecosystem and Kubernetes storage components.

---

# Step 10 – Volume Mount

After the volume is attached:

```text
Node

↓

Filesystem

↓

Pod

↓

Mount Path
```

Example:

```text
/data
```

The application can now read and write data.

---

# Complete Production Flow

```text
Developer

↓

PVC

↓

StorageClass

↓

CSI Controller

↓

Storage Backend

↓

Persistent Volume

↓

PVC Bound

↓

Pod Scheduled

↓

Volume Attached

↓

Volume Mounted

↓

Application
```

---

# Dynamic Provisioning Components

The main components involved are:

```text
PVC
StorageClass
CSI Driver
CSI Provisioner
PersistentVolume
Storage Backend
kubelet
```

---

# CSI Controller Side

The CSI controller typically handles operations such as:

* Provisioning
* Deleting volumes
* Attaching volumes
* Detaching volumes
* Expanding volumes

Conceptually:

```text
Kubernetes

↓

CSI Controller

↓

Storage Backend
```

---

# CSI Node Side

The CSI node component runs on Kubernetes Nodes.

It is responsible for operations such as:

* Node-side volume setup
* Mounting
* Unmounting
* Making the storage available to the Pod

Conceptually:

```text
Node

↓

CSI Node Plugin

↓

Mounted Volume

↓

Pod
```

The next chapter covers CSI drivers in much greater depth.

---

# `Immediate` Provisioning

StorageClass:

```yaml
volumeBindingMode: Immediate
```

Workflow:

```text
PVC Created

↓

Storage Provisioned

↓

PV Created

↓

PVC Bound

↓

Pod Scheduled
```

Storage can be provisioned before Kubernetes knows which Node will consume it.

---

# `WaitForFirstConsumer`

StorageClass:

```yaml
volumeBindingMode: WaitForFirstConsumer
```

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

PV Created

↓

PVC Bound
```

This is especially useful for topology-aware storage.

---

# Why Topology Matters

Suppose a cloud cluster has:

```text
Zone A
Zone B
Zone C
```

A block-storage volume may exist only in one zone.

If Kubernetes creates the volume in Zone A:

```text
Volume

↓

Zone A
```

but schedules the Pod to Zone C:

```text
Pod

↓

Zone C
```

the volume may not be attachable there.

With:

```text
WaitForFirstConsumer
```

Kubernetes can consider the Pod's scheduling constraints before provisioning storage.

---

# Topology-Aware Provisioning

Conceptually:

```text
Pod Requirements

+

Node Topology

+

Storage Topology

↓

Provision Storage
```

This prevents many incorrect storage placements.

---

# Dynamic Provisioning with StatefulSets

Dynamic provisioning is commonly used with StatefulSets.

Example:

```text
StatefulSet

↓

3 Replicas
```

Each replica can receive its own PVC.

```text
postgres-0

↓

PVC-0

↓

PV-0
```

```text
postgres-1

↓

PVC-1

↓

PV-1
```

```text
postgres-2

↓

PVC-2

↓

PV-2
```

This is useful for stateful workloads.

---

# Storage Lifecycle

```text
PVC Created

↓

Provision

↓

PV Created

↓

Bound

↓

Pod Uses Storage

↓

PVC Deleted

↓

PV Reclaimed
```

What happens to the underlying storage depends on the reclaim policy.

---

# Reclaim Policy: Delete

```text
PVC Deleted

↓

PV Deleted

↓

Storage Backend Volume Deleted
```

This is convenient for disposable workloads.

---

# Reclaim Policy: Retain

```text
PVC Deleted

↓

PV Retained

↓

Storage Preserved
```

This is useful for critical data requiring manual recovery or controlled reuse.

---

# Dynamic Volume Expansion

If supported:

```yaml
allowVolumeExpansion: true
```

A PVC may request:

```text
20Gi

↓

50Gi
```

Workflow:

```text
PVC Updated

↓

CSI Driver

↓

Storage Expanded

↓

Filesystem Expanded
```

The exact behavior depends on the CSI driver and filesystem.

---

# Dynamic Provisioning vs Volume Mounting

These are different operations.

### Provisioning

```text
Create Storage
```

### Attachment

```text
Connect Storage to Node
```

### Mounting

```text
Make Storage Available to Pod
```

Complete lifecycle:

```text
Provision

↓

Attach

↓

Mount
```

---

# Important Kubernetes Storage Objects

```text
StorageClass
```

Defines how storage should be provisioned.

```text
PVC
```

Requests storage.

```text
PV
```

Represents provisioned storage.

```text
VolumeAttachment
```

Represents attachment of a volume to a Node for storage systems that require it.

---

# Internal Architecture

```text
                 Kubernetes API Server
                         │
                         ▼
                        PVC
                         │
                         ▼
                  StorageClass
                         │
                         ▼
                  CSI Controller
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
                       Node
                         │
                         ▼
                   CSI Node Plugin
                         │
                         ▼
                       Pod
```

---

# Hands-on Lab 1 – Create Dynamic PVC

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

# Hands-on Lab 2 – Watch Provisioning

Run:

```bash
kubectl get pvc -w
```

In another terminal:

```bash
kubectl get pv -w
```

Observe:

```text
PVC

↓

Pending

↓

Bound
```

and:

```text
PV

↓

Available

↓

Bound
```

---

# Hands-on Lab 3 – Inspect PVC Events

```bash
kubectl describe pvc dynamic-pvc
```

Look at:

```text
Events
```

You may see provisioning-related events.

---

# Hands-on Lab 4 – Create a Pod

```yaml
apiVersion: v1

kind: Pod

metadata:
  name: storage-test

spec:
  containers:

  - name: app

    image: nginx

    volumeMounts:

    - name: storage

      mountPath: /data

  volumes:

  - name: storage

    persistentVolumeClaim:

      claimName: dynamic-pvc
```

Apply:

```bash
kubectl apply -f pod.yaml
```

---

# Hands-on Lab 5 – Write Data

Enter the Pod:

```bash
kubectl exec -it storage-test -- sh
```

Create:

```bash
echo "Persistent Kubernetes Storage" > /data/test.txt
```

Verify:

```bash
cat /data/test.txt
```

---

# Hands-on Lab 6 – Recreate the Pod

Delete:

```bash
kubectl delete pod storage-test
```

Recreate the Pod using the same PVC.

Then:

```bash
kubectl exec -it storage-test -- cat /data/test.txt
```

Expected:

```text
Persistent Kubernetes Storage
```

The data remains because it is stored on the persistent volume rather than the container filesystem.

---

# Hands-on Lab 7 – Test PVC Expansion

First verify:

```bash
kubectl get sc
```

Confirm that the StorageClass supports expansion.

Edit the PVC:

```bash
kubectl edit pvc dynamic-pvc
```

Change:

```text
5Gi
```

to:

```text
10Gi
```

Then:

```bash
kubectl get pvc
```

Verify the new capacity.

---

# Hands-on Lab 8 – Investigate a Pending PVC

Create a PVC referencing a nonexistent StorageClass.

Example:

```yaml
storageClassName: nonexistent
```

Apply it.

Then:

```bash
kubectl get pvc
```

Expected:

```text
Pending
```

Troubleshoot:

```bash
kubectl describe pvc <pvc-name>
```

This is an excellent real-world troubleshooting exercise.

---

# Common Mistakes

## 1. Thinking Dynamic Provisioning Means Dynamic Mounting

Dynamic provisioning means:

```text
Storage is automatically created
```

It does not mean:

```text
Pod automatically mounts any storage
```

The Pod still needs to reference the PVC.

---

## 2. Missing StorageClass

If the PVC references a nonexistent StorageClass:

```text
PVC

↓

Pending
```

---

## 3. Missing CSI Driver

A StorageClass may exist while its CSI driver is unavailable.

Result:

```text
PVC

↓

Pending
```

or provisioning failures.

---

## 4. Ignoring Topology

Storage may be created in a location incompatible with Pod placement when topology-aware provisioning is not configured appropriately.

---

## 5. Confusing Provisioning with Attachment

These are separate operations:

```text
Provision

↓

Attach

↓

Mount
```

Failure can occur at any stage.

---

## 6. Assuming All Storage Supports RWX

Many block-storage systems support:

```text
RWO
```

but not:

```text
RWX
```

RWX generally requires an appropriate shared filesystem or storage backend.

---

## 7. Deleting PVCs Without Understanding Reclaim Policy

With:

```text
Delete
```

the underlying storage may also be deleted.

Always understand the lifecycle before deleting production PVCs.

---

# Troubleshooting Dynamic Provisioning

When a PVC is stuck in:

```text
Pending
```

check the following.

### Step 1

```bash
kubectl get pvc
```

---

### Step 2

```bash
kubectl describe pvc <pvc-name>
```

Check Events.

---

### Step 3

Check StorageClasses:

```bash
kubectl get storageclass
```

---

### Step 4

Check CSI Pods:

```bash
kubectl get pods -A
```

Look for:

```text
csi-controller
csi-node
```

The exact names depend on the CSI driver.

---

### Step 5

Check PVs:

```bash
kubectl get pv
```

---

### Step 6

Check the Pod if using `WaitForFirstConsumer`:

```bash
kubectl get pod
```

If there is no consuming Pod, provisioning may intentionally be waiting.

---

# Quick Revision

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

PVC Bound
```

---

## Complete Runtime Flow

```text
PVC

↓

Provision

↓

PV

↓

Pod

↓

Attach

↓

Mount

↓

Application
```

---

## Topology-Aware Provisioning

```text
PVC

↓

WaitForFirstConsumer

↓

Pod Scheduling

↓

Topology Decision

↓

Storage Provisioning
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

View StorageClasses:

```bash
kubectl get sc
```

View all resources:

```bash
kubectl get all
```

View events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

Inspect CSI-related Pods:

```bash
kubectl get pods -A
```

---

# Interview Questions

## Basic

* What is dynamic provisioning?
* How is dynamic provisioning different from static provisioning?
* What is the role of a StorageClass?

---

## Intermediate

* Explain the workflow of dynamic provisioning.
* What is the role of a CSI driver?
* What happens after a PVC is created?
* What is `WaitForFirstConsumer`?

---

## Advanced

* Explain the complete PVC → StorageClass → CSI → PV workflow.
* Why is `WaitForFirstConsumer` important for topology-aware storage?
* What is the difference between provisioning, attachment, and mounting?
* Why can a PVC remain Pending even when a StorageClass exists?
* How would you troubleshoot a dynamically provisioned PVC stuck in Pending?
* How does dynamic provisioning work with StatefulSets?
* What happens to dynamically provisioned storage when a PVC is deleted?
* How does volume expansion work with CSI drivers?

---

# Production Best Practices

### 1. Prefer Dynamic Provisioning

Use StorageClasses and CSI drivers instead of manually creating PVs for every workload.

---

### 2. Use `WaitForFirstConsumer` Where Appropriate

Especially for:

* Zonal block storage
* Local storage
* Topology-constrained environments

---

### 3. Define Clear Storage Classes

Avoid creating many classes without meaningful differences.

Use classes based on actual workload requirements.

---

### 4. Protect Critical Data

For important workloads, carefully evaluate:

```text
Reclaim Policy
Backup Strategy
Replication
Encryption
```

---

### 5. Monitor CSI Components

Monitor:

```text
Provisioning
Attachment
Mounting
Expansion
Deletion
```

---

### 6. Test Disaster Recovery

Persistent storage is not automatically a backup.

A PV can persist while the data is still vulnerable to:

* Accidental deletion
* Corruption
* Storage failure
* Application-level deletion
* Cluster-level incidents

Use an appropriate backup and recovery strategy.

---

# References

## Official Kubernetes Documentation

* Dynamic Volume Provisioning
* Persistent Volumes
* Persistent Volume Claims
* Storage Classes
* Volume Binding Modes
* Volume Expansion
* Storage Topology

---

## CNCF Resources

* Kubernetes SIG Storage
* Container Storage Interface
* Kubernetes Storage Architecture
* Cloud Native Computing Foundation (CNCF)

---

## CSI Ecosystem

Dynamic provisioning is commonly implemented through CSI drivers for storage systems such as:

* AWS EBS
* Azure Disk
* Azure Files
* Google Persistent Disk
* Ceph
* NFS
* NetApp
* VMware

Always consult the documentation for the specific CSI driver before configuring production storage.

---

# Recommended Practice

1. Create a PVC using an existing StorageClass.
2. Observe automatic PV creation.
3. Trace the PVC from `Pending` to `Bound`.
4. Mount the dynamically provisioned storage into a Pod.
5. Write data and recreate the Pod.
6. Test volume expansion.
7. Investigate a deliberately broken StorageClass.
8. Test `WaitForFirstConsumer`.
9. Examine CSI controller and node components.
10. Delete a test PVC and observe the reclaim policy.

---

# Chapter Summary

Dynamic provisioning transforms Kubernetes storage from a manually managed process into an automated workflow.

The complete process is:

```text
Developer

↓

PersistentVolumeClaim

↓

StorageClass

↓

CSI Provisioner

↓

CSI Driver

↓

Storage Backend

↓

PersistentVolume

↓

PVC Bound

↓

Pod Scheduled

↓

Volume Attached

↓

Volume Mounted

↓

Application
```

The most important distinction is:

```text
PV
↓
Represents storage

PVC
↓
Requests storage

StorageClass
↓
Defines how storage is provisioned

CSI Driver
↓
Implements the storage integration

Dynamic Provisioning
↓
Automatically creates the required storage
```

Dynamic provisioning is one of the most important concepts for running **stateful workloads in production Kubernetes environments**, because it allows storage to be created on demand while maintaining a clean separation between application requirements and infrastructure implementation.

---

## Next Chapter

# Chapter 35 – CSI Drivers

Topics:

* What is CSI?
* Why CSI was introduced
* CSI Architecture
* CSI Controller
* CSI Node Plugin
* CSI Sidecars
* `CreateVolume`
* `DeleteVolume`
* `ControllerPublishVolume`
* `NodeStageVolume`
* `NodePublishVolume`
* Volume Lifecycle
* CSI and Dynamic Provisioning
* CSI Snapshots
* Volume Expansion
* Topology Awareness
* Hands-on Labs
* Troubleshooting
* Common Mistakes
* Quick Revision
* Interview Questions
* References

---
