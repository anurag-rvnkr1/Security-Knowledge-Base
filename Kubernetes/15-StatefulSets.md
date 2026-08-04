# Chapter 15 – StatefulSets

## Overview

A **StatefulSet** is a Kubernetes workload controller used to manage **stateful applications**.

Unlike Deployments, StatefulSets provide:

- Stable Pod identities
- Stable network identities
- Persistent storage
- Ordered deployment
- Ordered scaling
- Ordered updates

StatefulSets are designed for applications where **each Pod must maintain its own identity and persistent data**, even after restarts.

Common examples include:

- MySQL
- PostgreSQL
- MongoDB
- Cassandra
- Kafka
- Elasticsearch
- ZooKeeper
- Redis Cluster

---

# Learning Objectives

After completing this chapter, you will understand:

- What a StatefulSet is
- Why StatefulSets are needed
- StatefulSet Architecture
- Stable Pod Identity
- Stable Network Identity
- Persistent Storage
- Ordered Deployment
- Ordered Scaling
- Ordered Updates
- Headless Services
- StatefulSet Best Practices

---

# Why StatefulSets?

Imagine a Deployment with three Pods.

```
Deployment

↓

Pod

↓

Deleted

↓

New Pod

↓

Different Name

↓

Different Storage
```

For stateless applications:

```
No Problem
```

For databases:

```
Major Problem
```

Database nodes require:

- Stable identity
- Persistent storage
- Predictable startup order

---

# Solution

Use a StatefulSet.

```
StatefulSet

↓

database-0

↓

database-1

↓

database-2
```

Each Pod has:

- Permanent name
- Permanent storage
- Stable DNS name

---

# What is a StatefulSet?

A StatefulSet is a controller that manages stateful workloads requiring:

- Persistent identity
- Persistent storage
- Ordered lifecycle management

Unlike Deployments:

```
Pods

↓

Not Interchangeable
```

Each Pod is unique.

---

# Deployment vs StatefulSet

| Deployment | StatefulSet |
|------------|-------------|
| Stateless applications | Stateful applications |
| Random Pod names | Stable Pod names |
| Shared identity | Unique identity |
| Pods are interchangeable | Pods have individual identities |
| Storage optional | Persistent storage commonly used |

---

# StatefulSet Architecture

```
               StatefulSet

                    │

        ┌───────────┼───────────┐

        ▼           ▼           ▼

    mysql-0     mysql-1     mysql-2

        │           │           │

        ▼           ▼           ▼

      PVC-0       PVC-1       PVC-2

        │           │           │

        ▼           ▼           ▼

 Persistent   Persistent   Persistent

   Volume        Volume        Volume
```

Every Pod receives its own PersistentVolumeClaim (PVC).

---

# Stable Pod Identity

Pods receive predictable names.

Example:

```
mysql-0

mysql-1

mysql-2
```

If:

```
mysql-1

↓

Restart
```

New Pod:

```
mysql-1
```

The name remains unchanged.

---

# Stable Network Identity

Each Pod receives a stable DNS name.

Example:

```
mysql-0.mysql.default.svc.cluster.local
```

```
mysql-1.mysql.default.svc.cluster.local
```

Applications can reliably communicate with specific Pods.

---

# Headless Service Requirement

StatefulSets require a **Headless Service**.

Example:

```yaml
clusterIP: None
```

Architecture:

```
Headless Service

↓

DNS

↓

mysql-0

mysql-1

mysql-2
```

Without a Headless Service, stable Pod DNS names cannot be provided.

---

# Persistent Storage

Each Pod gets its own storage.

```
mysql-0

↓

PVC-0

↓

PV
```

```
mysql-1

↓

PVC-1

↓

PV
```

Each Pod owns its PersistentVolumeClaim.

---

# Why Separate Storage?

Suppose:

```
mysql-1

↓

Deleted
```

Storage:

```
PVC-1

↓

Still Exists
```

When recreated:

```
mysql-1

↓

Same PVC

↓

Same Data
```

Data survives Pod recreation.

---

# Ordered Deployment

Deployment creates Pods:

```
All Together
```

StatefulSet creates Pods sequentially:

```
mysql-0

↓

Ready

↓

mysql-1

↓

Ready

↓

mysql-2
```

The next Pod is created only after the previous Pod is ready.

---

# Ordered Scaling

Scale up:

```
Current

↓

mysql-0

mysql-1
```

Increase replicas:

```
mysql-2
```

Scale down:

```
mysql-2

↓

Deleted

↓

mysql-1

↓

Deleted

↓

mysql-0
```

Pods are removed in reverse order.

---

# Ordered Updates

Suppose:

```
Version

↓

v1
```

Update:

```
v2
```

Order:

```
mysql-2

↓

mysql-1

↓

mysql-0
```

By default, StatefulSets update Pods one at a time in reverse ordinal order, ensuring application stability.

---

# StatefulSet Workflow

```
StatefulSet

↓

Headless Service

↓

Stable DNS

↓

Pod

↓

PVC

↓

Persistent Volume
```

---

# StatefulSet YAML

```yaml
apiVersion: apps/v1

kind: StatefulSet

metadata:

  name: mysql

spec:

  serviceName: mysql

  replicas: 3

  selector:

    matchLabels:

      app: mysql

  template:

    metadata:

      labels:

        app: mysql

    spec:

      containers:

      - name: mysql

        image: mysql:8
```

---

# Volume Claim Template

StatefulSets automatically create PVCs.

Example:

```yaml
volumeClaimTemplates:

- metadata:

    name: mysql-data

  spec:

    accessModes:

    - ReadWriteOnce

    resources:

      requests:

        storage: 10Gi
```

Each replica gets its own PVC.

---

# Scaling Example

Current:

```
Replicas

↓

3
```

Scale:

```bash
kubectl scale statefulset mysql \
--replicas=5
```

Result:

```
mysql-3

mysql-4
```

Each receives:

- Unique identity
- Unique storage

---

# Common Stateful Applications

```
MySQL

↓

Persistent Storage
```

```
MongoDB

↓

Replica Set
```

```
Kafka

↓

Broker Identity
```

```
ZooKeeper

↓

Stable Cluster Nodes
```

```
Elasticsearch

↓

Node Identity
```

---

# Viewing StatefulSets

List:

```bash
kubectl get statefulsets
```

or

```bash
kubectl get sts
```

Describe:

```bash
kubectl describe sts mysql
```

---

# Updating StatefulSets

Apply:

```bash
kubectl apply -f statefulset.yaml
```

Monitor rollout:

```bash
kubectl rollout status sts mysql
```

---

# Deleting StatefulSets

Delete:

```bash
kubectl delete sts mysql
```

By default:

```
StatefulSet

↓

Deleted
```

PVCs are **not** automatically deleted, protecting persistent data.

---

# StatefulSet Lifecycle

```
Create

↓

Headless Service

↓

Pod

↓

PVC

↓

Persistent Volume

↓

Update

↓

Scale

↓

Delete
```

---

# Important kubectl Commands

View:

```bash
kubectl get sts
```

Describe:

```bash
kubectl describe sts mysql
```

Scale:

```bash
kubectl scale sts mysql \
--replicas=5
```

Rollout:

```bash
kubectl rollout status sts mysql
```

Delete:

```bash
kubectl delete sts mysql
```

---

# StatefulSet Architecture Summary

```
StatefulSet

↓

Stable Identity

↓

Stable DNS

↓

Persistent Storage

↓

Ordered Operations
```

---

# Best Practices

### 1. Use StatefulSets Only for Stateful Workloads

Databases, distributed storage, and clustered applications are ideal candidates.

---

### 2. Always Use a Headless Service

It provides stable DNS records required by StatefulSets.

---

### 3. Use Persistent Volumes

Avoid ephemeral storage for stateful applications.

---

### 4. Test Scaling Carefully

Ensure the application itself supports scaling and replica synchronization.

---

### 5. Protect Persistent Data

Remember that deleting a StatefulSet does not automatically remove the associated PersistentVolumeClaims.

---

# How StatefulSets Work Internally

## Overview

StatefulSets are one of the most sophisticated workload controllers in Kubernetes.

Unlike Deployments, StatefulSets must maintain:

- Stable Pod identities
- Stable DNS records
- Persistent storage
- Ordered Pod creation
- Ordered Pod deletion
- Ordered rolling updates

To achieve this, Kubernetes combines several components:

- StatefulSet Controller
- Headless Service
- DNS (CoreDNS)
- PersistentVolumeClaims (PVCs)
- PersistentVolumes (PVs)
- Scheduler
- kubelet

These components work together to provide reliable, stateful workloads.

---

# High-Level Architecture

```
                 Kubernetes Cluster

                         │

                    API Server

                         │

               StatefulSet Controller

                         │

      ┌──────────────────┼──────────────────┐

      ▼                  ▼                  ▼

    mysql-0           mysql-1           mysql-2

      │                  │                  │

      ▼                  ▼                  ▼

    PVC-0              PVC-1              PVC-2

      │                  │                  │

      ▼                  ▼                  ▼

      PV                 PV                 PV
```

---

# Complete Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Validation

↓

Store StatefulSet

↓

StatefulSet Controller

↓

Headless Service

↓

Create PVC

↓

Bind PV

↓

Create Pod

↓

Scheduler

↓

kubelet

↓

Running Pod
```

---

# Step 1 – StatefulSet Creation

Example:

```yaml
kind: StatefulSet
```

Deploy:

```bash
kubectl apply -f statefulset.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates request
- Authorizes request
- Validates StatefulSet
- Stores object in etcd

Workflow:

```
kubectl

↓

API Server

↓

StatefulSet Stored
```

---

# Step 3 – StatefulSet Controller

The StatefulSet Controller continuously watches:

- StatefulSets
- Pods
- PVCs
- Nodes

Its responsibility is to maintain the desired state.

```
API Server

↓

StatefulSet Controller

↓

Desired State
```

---

# Step 4 – Headless Service

Unlike Deployments, StatefulSets require:

```
Headless Service

↓

clusterIP: None
```

Why?

Because every Pod needs an individual DNS record.

---

# Headless Service Workflow

```
Headless Service

↓

DNS Records

↓

mysql-0

mysql-1

mysql-2
```

No virtual ClusterIP is created.

---

# Step 5 – Pod Identity

Instead of random names:

```
deployment-76df87d5-xr9cz
```

StatefulSet creates:

```
mysql-0

mysql-1

mysql-2
```

These identities never change.

---

# Pod Identity Rules

Replica:

```
0

↓

mysql-0
```

Replica:

```
1

↓

mysql-1
```

Replica:

```
2

↓

mysql-2
```

Even after restart:

```
mysql-1

↓

Restart

↓

mysql-1
```

Identity remains stable.

---

# Step 6 – DNS Creation

CoreDNS automatically creates:

```
mysql-0.mysql.default.svc.cluster.local
```

```
mysql-1.mysql.default.svc.cluster.local
```

```
mysql-2.mysql.default.svc.cluster.local
```

Applications can reliably connect to specific Pods.

---

# Step 7 – VolumeClaimTemplates

Example:

```yaml
volumeClaimTemplates:
```

Controller creates:

```
mysql-data-mysql-0

mysql-data-mysql-1

mysql-data-mysql-2
```

Each replica receives its own PersistentVolumeClaim.

---

# PVC Creation

Workflow:

```
StatefulSet

↓

Replica

↓

PVC

↓

Persistent Volume
```

Each Pod has dedicated storage.

---

# Storage Binding

```
PVC

↓

StorageClass

↓

Persistent Volume

↓

Bound
```

After the PVC is bound, the Pod can start.

---

# Step 8 – Ordered Pod Creation

Suppose:

```
Replicas

↓

3
```

Creation order:

```
mysql-0

↓

Ready

↓

mysql-1

↓

Ready

↓

mysql-2
```

If:

```
mysql-0

↓

Not Ready
```

Result:

```
mysql-1

↓

Not Created
```

The controller waits for each Pod to become Ready.

---

# Step 9 – Scheduler

Once the PVC is available:

```
Scheduler

↓

Select Node

↓

Assign Pod
```

---

# Step 10 – kubelet

Worker Node:

```
API Server

↓

kubelet

↓

Mount Volume

↓

Start Container
```

---

# Final Running State

```
mysql-0

↓

PVC-0

↓

PV
```

```
mysql-1

↓

PVC-1

↓

PV
```

```
mysql-2

↓

PVC-2

↓

PV
```

---

# Scaling Up

Current:

```
mysql-0

mysql-1
```

Scale:

```
Replicas

↓

3
```

Controller creates:

```
PVC-2

↓

mysql-2
```

Only the new replica is added.

---

# Scaling Down

Current:

```
mysql-0

mysql-1

mysql-2
```

Scale:

```
Replicas

↓

2
```

Deletion order:

```
mysql-2

↓

Deleted
```

PVC:

```
Still Exists
```

Data is preserved.

---

# Pod Restart

Suppose:

```
mysql-1

↓

Crash
```

Controller creates:

```
mysql-1
```

Same:

- Name
- DNS
- Storage

Application continues using the same identity.

---

# Rolling Update Workflow

Suppose:

```
Version

↓

v1
```

Upgrade:

```
v2
```

Order:

```
mysql-2

↓

Ready

↓

mysql-1

↓

Ready

↓

mysql-0
```

This reverse-order update helps maintain application consistency.

---

# Update Strategy

Default:

```
RollingUpdate
```

Alternative:

```
OnDelete
```

With `OnDelete`:

```
Administrator

↓

Delete Pod

↓

New Version Starts
```

---

# Pod Management Policy

Default:

```
OrderedReady
```

Behavior:

```
Pod 0

↓

Ready

↓

Pod 1

↓

Ready

↓

Pod 2
```

Alternative:

```
Parallel
```

Pods can be created or deleted simultaneously, but identities remain stable.

---

# Failure Recovery

Suppose:

```
Node Failure
```

Pod:

```
Unavailable
```

If Kubernetes reschedules it:

```
Same Name

↓

Same PVC

↓

Same DNS
```

State is preserved.

---

# Internal Architecture

```
API Server

↓

StatefulSet Controller

↓

Headless Service

↓

DNS

↓

PVC

↓

PV

↓

Scheduler

↓

kubelet

↓

Container
```

---

# Database Example

```
PostgreSQL Cluster

↓

postgres-0

↓

Primary
```

```
postgres-1

↓

Replica
```

```
postgres-2

↓

Replica
```

Each Pod maintains a unique identity and storage.

---

# Kafka Example

```
Kafka

↓

broker-0

↓

broker-1

↓

broker-2
```

Each broker keeps its own data directory.

---

# Elasticsearch Example

```
es-0

↓

Data Node
```

```
es-1

↓

Data Node
```

Each node maintains its own index data.

---

# Hands-on Lab 1 – Create Headless Service

```yaml
apiVersion: v1

kind: Service

metadata:

  name: mysql

spec:

  clusterIP: None

  selector:

    app: mysql

  ports:

  - port: 3306
```

Deploy:

```bash
kubectl apply -f service.yaml
```

---

# Hands-on Lab 2 – Create StatefulSet

Deploy:

```bash
kubectl apply -f statefulset.yaml
```

Verify:

```bash
kubectl get sts

kubectl get pods
```

Observe:

```
mysql-0

mysql-1

mysql-2
```

---

# Hands-on Lab 3 – View PVCs

```bash
kubectl get pvc
```

Observe:

```
mysql-data-mysql-0

mysql-data-mysql-1

mysql-data-mysql-2
```

Each Pod has its own claim.

---

# Hands-on Lab 4 – Scale StatefulSet

```bash
kubectl scale sts mysql \
--replicas=5
```

Verify:

```bash
kubectl get pods

kubectl get pvc
```

New replicas receive new PVCs.

---

# Hands-on Lab 5 – Delete a Pod

Delete:

```bash
kubectl delete pod mysql-1
```

Observe:

```bash
kubectl get pods -w
```

New Pod:

```
mysql-1
```

Verify that:

- Name remains the same
- PVC is reused
- DNS name is unchanged

---

# Common Mistakes

## 1. Using Deployments for Databases

Incorrect:

```
Deployment

↓

MySQL
```

Correct:

```
StatefulSet

↓

MySQL
```

---

## 2. Forgetting the Headless Service

Without:

```yaml
clusterIP: None
```

Stable DNS records are unavailable.

---

## 3. Assuming PVCs Are Deleted Automatically

Deleting a StatefulSet does **not** automatically remove its PVCs.

Storage remains until explicitly cleaned up or managed by the configured retention policy.

---

## 4. Expecting Parallel Startup

Default behavior:

```
OrderedReady
```

Pods are created sequentially.

---

## 5. Sharing One PersistentVolume

Incorrect:

```
All Pods

↓

One PV
```

Preferred:

```
Each Pod

↓

Own PVC

↓

Own PV
```

---

# StatefulSets Quick Revision

## Architecture

```
StatefulSet

↓

Headless Service

↓

Stable DNS

↓

Stable Pod Name

↓

PVC

↓

PV
```

---

## Lifecycle

```
Create

↓

PVC

↓

Pod

↓

DNS

↓

Scale

↓

Update

↓

Delete
```

---

## Ordered Operations

```
Create

0 → 1 → 2
```

```
Delete

2 → 1 → 0
```

```
Update

2 → 1 → 0
```

---

# Essential kubectl Commands

View StatefulSets:

```bash
kubectl get sts
```

Describe:

```bash
kubectl describe sts mysql
```

Scale:

```bash
kubectl scale sts mysql \
--replicas=5
```

View PVCs:

```bash
kubectl get pvc
```

Rollout Status:

```bash
kubectl rollout status sts mysql
```

Delete:

```bash
kubectl delete sts mysql
```

---

# Interview Questions

### Basic

- What is a StatefulSet?
- How does a StatefulSet differ from a Deployment?
- Why do StatefulSets require a Headless Service?

---

### Intermediate

- What is a VolumeClaimTemplate?
- How are Pod names generated?
- Why does each replica need its own PVC?

---

### Advanced

- Explain the internal workflow of a StatefulSet.
- Why are Pods created sequentially by default?
- What happens when a StatefulSet Pod crashes?
- How do rolling updates work in StatefulSets?
- What is the difference between `OrderedReady` and `Parallel` Pod management?

---

# References

## Official Kubernetes Documentation

- StatefulSets
- Persistent Volumes
- PersistentVolumeClaims
- Headless Services
- DNS for Services and Pods
- StorageClasses

---

## CNCF Resources

- Kubernetes Best Practices
- Stateful Workloads Guide
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Best Practices
- NIST SP 800-190
- Kubernetes Storage Documentation

---

## Recommended Practice

1. Create a Headless Service and StatefulSet.
2. Observe stable Pod names and DNS entries.
3. Inspect automatically created PVCs.
4. Scale the StatefulSet up and down.
5. Delete individual Pods and verify identity and storage persistence.
6. Perform a rolling update and observe the update order.
7. Compare StatefulSet behavior with a Deployment using the same application.

---

# Chapter Summary

```
Developer

↓

StatefulSet

↓

API Server

↓

StatefulSet Controller

↓

Headless Service

↓

Stable DNS

↓

PVC

↓

PV

↓

Scheduler

↓

kubelet

↓

Stateful Application
```

StatefulSets provide the foundation for running **stateful, distributed applications** in Kubernetes. By combining **stable identities, persistent storage, predictable networking, and ordered lifecycle management**, they enable reliable deployment of databases, messaging systems, and clustered services that cannot be managed effectively with standard Deployments.

---
