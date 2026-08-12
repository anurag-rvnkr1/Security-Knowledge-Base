# Chapter 36 – CSI Drivers

## Overview

The **Container Storage Interface (CSI)** is the standard interface that allows Kubernetes to communicate with storage systems.

Before CSI became the standard, Kubernetes contained many storage integrations directly inside the Kubernetes codebase.

This created problems:

* Storage integrations were tightly coupled to Kubernetes.
* Storage vendors had to coordinate changes with Kubernetes releases.
* Adding new storage systems was more difficult.
* Feature development was slower.

CSI solved this by separating Kubernetes from storage implementations.

Instead of Kubernetes directly understanding every storage platform:

```text
Kubernetes

↓

CSI Driver

↓

Storage System
```

The CSI driver acts as the bridge between Kubernetes and the storage provider.

> **CSI is a standard interface; a CSI driver is a concrete implementation for a particular storage system.**

---

# Learning Objectives

After completing this chapter, you will understand:

* What CSI is
* Why CSI was introduced
* CSI architecture
* CSI Controller
* CSI Node Plugin
* External Provisioner
* External Attacher
* External Resizer
* External Snapshotter
* Volume lifecycle
* Attach and Mount workflow
* Dynamic provisioning
* CSI StorageClasses
* Topology-aware provisioning
* CSI troubleshooting
* Production best practices

---

# Why Do We Need CSI?

Suppose Kubernetes wants to support:

```text
AWS EBS
Azure Disk
Google Persistent Disk
Ceph
NetApp
Dell Storage
Pure Storage
VMware
```

Without a standardized interface, Kubernetes would need provider-specific logic for each storage system.

This becomes difficult to maintain.

CSI introduces a standard interface:

```text
Kubernetes

↓

CSI Specification

↓

Vendor Driver

↓

Storage Backend
```

---

# What is CSI?

**Container Storage Interface (CSI)** is a standardized specification for exposing storage systems to container orchestration platforms.

CSI is not itself a storage driver.

Instead:

```text
CSI

↓

Defines Interface
```

A driver implements that interface.

Examples:

```text
AWS EBS CSI Driver
```

```text
Azure Disk CSI Driver
```

```text
GCE Persistent Disk CSI Driver
```

```text
Ceph CSI
```

---

# CSI Architecture

A typical CSI implementation consists of two major sides:

```text
                    Kubernetes

                         │

             ┌───────────┴───────────┐

             │                       │

             ▼                       ▼

      CSI Controller           CSI Node Plugin

             │                       │

             ▼                       ▼

     Storage API              Worker Node

                                     │

                                     ▼

                                    Pod
```

---

# CSI Controller

The **CSI Controller** performs control-plane operations.

Typical responsibilities include:

* Create volumes
* Delete volumes
* Attach volumes
* Detach volumes
* Expand volumes
* Create snapshots

It normally runs as Pods in the cluster.

---

# CSI Node Plugin

The **CSI Node Plugin** runs on worker Nodes.

Its responsibilities include:

* Preparing storage for Pods
* Mounting volumes
* Unmounting volumes
* Publishing volumes into Pods
* Node-specific storage operations

Typically it runs as a **DaemonSet**, allowing one instance on each eligible Node.

---

# Controller vs Node

| CSI Controller           | CSI Node                     |
| ------------------------ | ---------------------------- |
| Cluster-level operations | Node-level operations        |
| Creates volumes          | Mounts volumes               |
| Deletes volumes          | Unmounts volumes             |
| Attaches volumes         | Publishes volumes            |
| Expands volumes          | Performs node-side expansion |

---

# CSI Sidecar Containers

CSI deployments commonly use Kubernetes-maintained sidecar containers.

Examples include:

```text
external-provisioner
```

```text
external-attacher
```

```text
external-resizer
```

```text
external-snapshotter
```

```text
node-driver-registrar
```

These components watch Kubernetes resources and communicate with the CSI driver.

---

# External Provisioner

The **external-provisioner** watches PVCs.

Workflow:

```text
PVC

↓

StorageClass

↓

External Provisioner

↓

CSI Driver

↓

Create Volume
```

The resulting storage is represented by a Persistent Volume.

---

# External Attacher

The **external-attacher** handles volume attachment for storage systems that require a separate attach operation.

Example:

```text
PV

↓

Attach

↓

Worker Node
```

This is especially important for cloud block storage.

---

# External Resizer

The **external-resizer** handles supported PVC expansion workflows.

Example:

```text
20Gi

↓

PVC Expansion

↓

50Gi
```

Whether filesystem expansion is required and how it occurs depends on the driver and storage system.

---

# External Snapshotter

The **external-snapshotter** enables Kubernetes volume snapshot workflows for CSI drivers that support snapshots.

Conceptually:

```text
PVC

↓

Volume

↓

Snapshot

↓

New Volume
```

Snapshots can be useful for:

* Backup workflows
* Test environments
* Disaster recovery
* Data cloning workflows

---

# Node Driver Registrar

The `node-driver-registrar` helps register the CSI driver with the kubelet on a Node.

Conceptually:

```text
CSI Node Plugin

↓

Node Driver Registrar

↓

kubelet

↓

CSI Driver Registered
```

---

# Complete CSI Architecture

```text
                         Kubernetes API

                                │

                ┌───────────────┴────────────────┐

                │                                │

                ▼                                ▼

        CSI Controller                     CSI Node Plugin

        ┌───────────────┐                  ┌───────────────┐
        │ Provisioner   │                  │ Node Registrar│
        │ Attacher      │                  │               │
        │ Resizer       │                  │ CSI Driver    │
        │ Snapshotter   │                  │               │
        └───────┬───────┘                  └───────┬───────┘
                │                                  │
                ▼                                  ▼
           Storage API                         Worker Node
                                                   │
                                                   ▼
                                                  Pod
```

---

# Dynamic Provisioning with CSI

Suppose a developer creates:

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

The workflow becomes:

```text
PVC

↓

StorageClass

↓

External Provisioner

↓

CSI Controller

↓

Storage Backend

↓

Volume Created

↓

PV Created

↓

PVC Bound
```

---

# Step 1 – PVC Creation

Developer:

```bash
kubectl apply -f pvc.yaml
```

Kubernetes creates:

```text
PVC

↓

Pending
```

---

# Step 2 – StorageClass Lookup

The PVC specifies:

```text
fast-storage
```

Kubernetes finds:

```text
StorageClass

↓

fast-storage
```

The StorageClass identifies the CSI provisioner.

---

# Step 3 – External Provisioner

The external provisioner notices the PVC.

It determines:

```text
Requested Capacity = 20Gi
StorageClass = fast-storage
```

It then communicates with the CSI driver.

---

# Step 4 – Create Volume

The CSI controller requests the storage backend to create the volume.

Conceptually:

```text
CSI Driver

↓

Storage API

↓

Create 20Gi Volume
```

The backend returns a volume identifier.

Example:

```text
volume-abc123
```

---

# Step 5 – PV Creation

Kubernetes creates a Persistent Volume representing the newly created storage.

```text
Storage Backend

↓

PV

↓

PVC
```

The PVC becomes:

```text
Bound
```

---

# Step 6 – Pod Uses PVC

A Pod references:

```yaml
volumes:

- name: database-storage

  persistentVolumeClaim:

    claimName: database-pvc
```

Now Kubernetes must make the storage available to the Node running the Pod.

---

# Step 7 – Scheduling

The Scheduler determines:

```text
Pod

↓

Worker Node 2
```

Topology constraints may influence this decision.

---

# Step 8 – Attach

If the storage system requires attachment:

```text
Volume

↓

CSI Controller

↓

Attach to Worker Node 2
```

For some storage types, attachment may not be required.

---

# Step 9 – Node Stage

The CSI Node Plugin prepares the volume on the Node.

Conceptually:

```text
Attached Volume

↓

Node Plugin

↓

Format / Mount

↓

Staging Path
```

The exact operations depend on the CSI driver and volume type.

---

# Step 10 – Node Publish

The CSI Node Plugin makes the volume available to the Pod.

Conceptually:

```text
Staged Volume

↓

Pod Volume Path

↓

Container Mount
```

---

# Step 11 – Application Starts

The application sees:

```text
/data
```

and can read/write the persistent storage.

---

# Complete Volume Lifecycle

```text
PVC Created

↓

StorageClass

↓

Provision

↓

PV Created

↓

PVC Bound

↓

Pod Scheduled

↓

Attach

↓

Stage

↓

Publish

↓

Container Mount

↓

Application Uses Volume
```

---

# Volume Deletion

When the PVC is deleted and the PV reclaim policy is `Delete`:

```text
PVC Deleted

↓

PV Released

↓

CSI Controller

↓

Delete Volume

↓

Storage Backend Deletes Volume
```

With:

```text
Retain
```

the underlying storage is retained for administrator-controlled recovery or reuse.

---

# CSI RPC Model

CSI drivers communicate using standardized RPC interfaces.

Major CSI service categories include:

```text
Identity Service
```

```text
Controller Service
```

```text
Node Service
```

---

# Identity Service

Provides information about the driver.

Examples:

```text
Driver Name

Version

Capabilities
```

---

# Controller Service

Handles controller-side operations such as:

```text
CreateVolume
DeleteVolume
ControllerPublishVolume
ControllerUnpublishVolume
CreateSnapshot
DeleteSnapshot
ControllerExpandVolume
```

Exact capabilities depend on the CSI version and driver.

---

# Node Service

Handles Node-level operations such as:

```text
NodeStageVolume
NodeUnstageVolume
NodePublishVolume
NodeUnpublishVolume
NodeGetInfo
NodeGetCapabilities
```

---

# Attach vs Mount

These concepts are frequently confused.

## Attach

```text
Storage Volume

↓

Worker Node
```

The volume becomes available to a Node.

---

## Mount / Publish

```text
Worker Node

↓

Pod

↓

Container
```

The volume is made available to the Pod and mounted into the container filesystem.

---

# Example

Cloud block storage:

```text
EBS Volume

↓

Attach to Node

↓

Mount on Node

↓

Publish to Pod

↓

/var/lib/app
```

---

# CSI and StorageClasses

A StorageClass usually references a CSI driver through:

```yaml
provisioner: <csi-driver>
```

Example conceptually:

```yaml
apiVersion: storage.k8s.io/v1

kind: StorageClass

metadata:
  name: fast-storage

provisioner: example.csi.storage.k8s.io

volumeBindingMode: WaitForFirstConsumer
```

The exact provisioner name is driver-specific.

---

# Topology-Aware CSI Provisioning

Modern storage environments often have topology constraints.

Example:

```text
Cluster

├── Zone A
├── Zone B
└── Zone C
```

A storage volume may exist only in:

```text
Zone B
```

The CSI driver advertises supported topology.

Kubernetes can then coordinate:

```text
Pod Placement

+

Storage Placement
```

---

# WaitForFirstConsumer

With:

```yaml
volumeBindingMode: WaitForFirstConsumer
```

Kubernetes delays provisioning until it knows where the consuming Pod will run.

Workflow:

```text
PVC

↓

Pending

↓

Pod Created

↓

Scheduler Evaluates Placement

↓

CSI Provisioning

↓

Topology Selected

↓

PV Created
```

This prevents many topology mismatch problems.

---

# CSI and Network Storage

Not every storage backend requires attachment.

For example:

```text
NFS

↓

Network Mount

↓

Pod
```

There may be no cloud block-device attachment step.

Therefore:

> **CSI workflow depends on the storage driver's capabilities and backend.**

---

# CSI Driver Deployment

A typical CSI driver installation may contain:

```text
CSI Controller Deployment

↓

external-provisioner

external-attacher

external-resizer

external-snapshotter

CSI Driver
```

and:

```text
CSI Node DaemonSet

↓

node-driver-registrar

CSI Driver
```

---

# View CSI Components

```bash
kubectl get pods -A
```

Look for components containing names such as:

```text
csi
```

or provider-specific driver names.

---

# View CSI Drivers

```bash
kubectl get csidrivers
```

Example:

```text
NAME
----
example.csi.storage.k8s.io
```

---

# Describe CSI Driver

```bash
kubectl describe csidriver <driver-name>
```

You can inspect capabilities such as:

* Attach requirements
* Pod info requirements
* Storage capacity support
* Volume lifecycle behavior

---

# View StorageClasses

```bash
kubectl get storageclass
```

Identify the CSI provisioner used by each class.

---

# View PVCs

```bash
kubectl get pvc
```

---

# View PVs

```bash
kubectl get pv
```

---

# Hands-on Lab 1 – Discover CSI Drivers

Run:

```bash
kubectl get csidrivers
```

Record:

```text
Driver Name
Attach Required
Pod Info
Storage Capacity
```

---

# Hands-on Lab 2 – Inspect CSI Pods

Run:

```bash
kubectl get pods -A
```

Identify:

```text
CSI Controller

CSI Node DaemonSet
```

---

# Hands-on Lab 3 – Inspect StorageClass

```bash
kubectl get storageclass
```

Then:

```bash
kubectl describe storageclass <name>
```

Identify:

```text
Provisioner

Parameters

Reclaim Policy

Binding Mode
```

---

# Hands-on Lab 4 – Dynamic Provisioning

Create a PVC using an available CSI-backed StorageClass.

```bash
kubectl apply -f pvc.yaml
```

Watch:

```bash
kubectl get pvc -w
```

Then:

```bash
kubectl get pv
```

Observe:

```text
PVC

↓

PV
```

---

# Hands-on Lab 5 – Mount CSI Storage

Create a Pod that consumes the PVC.

Verify:

```bash
kubectl get pod -o wide
```

Then inspect:

```bash
kubectl describe pod <pod-name>
```

Look for volume-related events.

---

# Hands-on Lab 6 – Inspect Events

When troubleshooting:

```bash
kubectl describe pvc <pvc-name>
```

and:

```bash
kubectl describe pod <pod-name>
```

Look at the Events section.

Common problems include:

```text
ProvisioningFailed
FailedAttachVolume
FailedMount
```

---

# Troubleshooting CSI

## Problem 1 – PVC Stuck in Pending

Check:

```bash
kubectl describe pvc <pvc-name>
```

Potential causes:

* Wrong StorageClass
* CSI controller unavailable
* Insufficient storage
* Invalid parameters
* Topology constraints
* Permission problems

---

# Problem 2 – FailedAttachVolume

Check:

```bash
kubectl describe pod <pod-name>
```

Possible causes:

* Volume cannot attach
* Volume already attached elsewhere
* Cloud API failure
* Node issue
* Driver problem

---

# Problem 3 – FailedMount

Possible causes:

* Filesystem issue
* Node plugin failure
* Incorrect mount options
* Permission problems
* Volume attachment not ready

Check CSI Node Plugin logs.

---

# Problem 4 – CSI Controller Failure

Check:

```bash
kubectl get pods -A
```

Then inspect controller logs:

```bash
kubectl logs <csi-controller-pod>
```

---

# Problem 5 – Node Plugin Failure

Find the CSI Node Pod running on the affected worker Node.

Then:

```bash
kubectl logs <csi-node-pod>
```

---

# Common Mistakes

## 1. Confusing CSI with a CSI Driver

CSI:

```text
Standard Interface
```

CSI Driver:

```text
Implementation
```

---

## 2. Assuming Every CSI Driver Supports Every Feature

A driver may not support:

* Snapshots
* Expansion
* Cloning
* RWX
* Online expansion
* Topology features

Always verify driver capabilities.

---

## 3. Assuming All Volumes Need Attach

Some network filesystems can be mounted without a separate cloud-style attach operation.

---

## 4. Ignoring Topology

Zonal storage can create scheduling problems if topology is not considered.

---

## 5. Debugging Only the Pod

Storage failures can occur at several layers:

```text
Pod

↓

kubelet

↓

CSI Node

↓

CSI Controller

↓

Storage API

↓

Storage Backend
```

Troubleshoot from the Kubernetes resource toward the storage backend.

---

## 6. Using Wrong StorageClass Parameters

CSI driver parameters are implementation-specific.

Never assume parameters from one provider work with another.

---

# CSI Quick Revision

## Architecture

```text
Kubernetes

↓

CSI Controller

↓

Storage Backend
```

and:

```text
Kubernetes Node

↓

CSI Node Plugin

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

External Provisioner

↓

CSI Driver

↓

Storage Backend

↓

PV
```

---

## Volume Consumption

```text
PV

↓

Attach

↓

Stage

↓

Publish

↓

Container Mount
```

---

# Essential Commands

List CSI Drivers:

```bash
kubectl get csidrivers
```

Describe CSI Driver:

```bash
kubectl describe csidriver <name>
```

List StorageClasses:

```bash
kubectl get sc
```

List PVCs:

```bash
kubectl get pvc
```

List PVs:

```bash
kubectl get pv
```

List CSI Pods:

```bash
kubectl get pods -A
```

Inspect Pod Events:

```bash
kubectl describe pod <pod-name>
```

Inspect PVC Events:

```bash
kubectl describe pvc <pvc-name>
```

View CSI Logs:

```bash
kubectl logs <csi-pod>
```

---

# Interview Questions

## Basic

* What is CSI?
* Why was CSI introduced?
* What is the difference between CSI and a CSI driver?
* What is a CSI Node Plugin?
* What is a CSI Controller?

---

## Intermediate

* Explain the role of `external-provisioner`.
* What does `external-attacher` do?
* What is the purpose of `node-driver-registrar`?
* Explain the difference between volume attachment and mounting.
* How does a StorageClass interact with a CSI driver?

---

## Advanced

* Explain the complete lifecycle of a dynamically provisioned CSI volume.
* Describe the workflow from PVC creation to a mounted volume inside a Pod.
* What is the difference between `CreateVolume`, `ControllerPublishVolume`, `NodeStageVolume`, and `NodePublishVolume`?
* Why does CSI separate controller-side and node-side operations?
* How does `WaitForFirstConsumer` work with CSI topology?
* How would you troubleshoot a PVC stuck in `Pending`?
* How would you troubleshoot `FailedAttachVolume` and `FailedMount`?
* Why can two CSI drivers behave differently even though both implement CSI?
* Explain how CSI enables Kubernetes to remain independent of specific storage vendors.

---

# Production Architecture

A typical cloud deployment might look like:

```text
                    Kubernetes API

                          │
                          ▼
                    StorageClass
                          │
                          ▼
                  External Provisioner
                          │
                          ▼
                    CSI Controller
                          │
                          ▼
                    Cloud Storage
                          │
                          ▼
                         PV
                          │
                          ▼
                         PVC
                          │
                          ▼
                         Pod
                          │
                          ▼
                    CSI Node Plugin
                          │
                          ▼
                      Node Mount
```

---

# Security Considerations

CSI drivers have access to important storage infrastructure.

Therefore:

* Use trusted CSI drivers.
* Keep CSI components updated.
* Restrict unnecessary permissions.
* Monitor CSI controller activity.
* Monitor Node plugin activity.
* Protect cloud-provider credentials.
* Use encryption where supported.
* Avoid exposing storage credentials inside application containers.

---

# Best Practices

### 1. Use Official or Trusted CSI Drivers

Choose actively maintained drivers with strong Kubernetes compatibility.

---

### 2. Use StorageClasses

Applications should normally request storage through PVCs and StorageClasses instead of directly managing infrastructure.

---

### 3. Understand Driver Capabilities

Before deploying a CSI driver, verify support for:

```text
RWO
RWX
Expansion
Snapshots
Cloning
Topology
Encryption
```

---

### 4. Use `WaitForFirstConsumer` for Topology-Aware Storage

This is particularly useful with zonal cloud block storage.

---

### 5. Monitor CSI Components

Monitor:

```text
CSI Controller

CSI Node Plugin

Provisioner

Attacher

Resizer

Snapshotter
```

---

### 6. Plan Backup Separately

A CSI snapshot is **not automatically a complete disaster-recovery strategy**.

Consider:

* Application-consistent backups
* Off-cluster backups
* Cross-region replication
* Restore testing

---

# References

## Official Kubernetes Documentation

* Container Storage Interface
* Storage Classes
* Persistent Volumes
* Volume Snapshots
* Volume Expansion
* Storage Capacity
* CSI Drivers

---

## CSI Specification

Study the official CSI specification for:

* Identity Service
* Controller Service
* Node Service
* Volume Lifecycle
* Snapshot Operations

---

## CNCF Resources

* Kubernetes SIG Storage
* Container Storage Interface
* Cloud Native Computing Foundation (CNCF)

---

## Major CSI Drivers

Examples include:

* AWS EBS CSI Driver
* Azure Disk CSI Driver
* Azure Files CSI Driver
* Google Compute Engine Persistent Disk CSI Driver
* Ceph CSI
* NFS CSI
* NetApp CSI
* VMware vSphere CSI

Always consult the specific driver's documentation for supported features and configuration parameters.

---

# Recommended Practice

1. Identify every CSI driver installed in your cluster.
2. Inspect their `CSIDriver` objects.
3. Identify which StorageClasses use each CSI driver.
4. Create a dynamically provisioned PVC.
5. Follow the PVC → PV → Pod workflow.
6. Inspect CSI Controller and Node Plugin Pods.
7. Examine Kubernetes Events during provisioning.
8. Test volume expansion if supported.
9. Test volume snapshots if supported.
10. Practice troubleshooting `Pending`, `FailedAttachVolume`, and `FailedMount` conditions.
11. Investigate topology-aware provisioning with `WaitForFirstConsumer`.

---

# Chapter Summary

```text
                    Kubernetes

                         │
                         ▼
                    StorageClass
                         │
                         ▼
                  External Provisioner
                         │
                         ▼
                    CSI Controller
                         │
                         ▼
                  Storage Backend
                         │
                         ▼
                         PV
                         │
                         ▼
                         PVC
                         │
                         ▼
                         Pod
                         │
                         ▼
                   CSI Node Plugin
                         │
                         ▼
                      Mounted
                       Volume
```

The **Container Storage Interface (CSI)** provides the standard boundary between Kubernetes and external storage systems. CSI drivers implement this interface and provide the functionality required to provision, attach, mount, expand, snapshot, and manage storage.

The most important distinction is:

```text
CSI
 ↓
Standard Interface

CSI Driver
 ↓
Implementation

StorageClass
 ↓
Defines How Storage Is Provisioned

PVC
 ↓
Requests Storage

PV
 ↓
Represents Storage

Pod
 ↓
Consumes Storage
```

Together, these components create the modern Kubernetes storage architecture:

```text
Pod
 ↓
PVC
 ↓
PV
 ↓
StorageClass / CSI
 ↓
Storage Backend
```

This abstraction allows Kubernetes applications to remain largely independent of the underlying storage provider while still supporting sophisticated cloud, enterprise, and on-premises storage systems.

---

# Kubernetes Storage Section – Complete

You have now covered the complete storage progression:

```text
Chapter 30 – Volumes
        ↓
Chapter 31 – Persistent Volumes (PV)
        ↓
Chapter 32 – Persistent Volume Claims (PVC)
        ↓
Chapter 33 – Storage Classes
        ↓
Chapter 34 – Dynamic Provisioning
        ↓
Chapter 36 – CSI Drivers
```

> **Note:** Your requested numbering skips Chapter 35. If you want the sequence to remain strictly consecutive, the CSI Drivers chapter can be renumbered to **Chapter 35 – CSI Drivers**.

The storage architecture to remember is:

```text
                   Kubernetes Storage

                          │
                          ▼
                         Pod
                          │
                          ▼
                         PVC
                          │
                          ▼
                         PV
                          │
              ┌───────────┴───────────┐
              │                       │
              ▼                       ▼
        StorageClass              Static PV
              │
              ▼
          CSI Driver
              │
              ▼
       Storage Backend
```

---

## Next Recommended Section

After completing Kubernetes storage, the natural next area is:

**Kubernetes Security**

```text
Secrets
   ↓
Service Accounts
   ↓
Authentication
   ↓
Authorization
   ↓
RBAC
   ↓
Roles & RoleBindings
   ↓
ClusterRoles & ClusterRoleBindings
   ↓
Admission Controllers
   ↓
Pod Security Standards
   ↓
Security Contexts
   ↓
Secrets Management
   ↓
Network Security
```

This provides the foundation for the later **CKS-oriented security chapters**.
