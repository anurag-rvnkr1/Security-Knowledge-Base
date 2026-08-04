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

