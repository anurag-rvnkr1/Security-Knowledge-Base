# Chapter 14 – DaemonSets

## Overview

A **DaemonSet** is a Kubernetes workload controller that ensures **exactly one Pod (or a specified number of Pods) runs on every eligible Node** in a cluster.

Unlike Deployments, which manage a desired number of replicas, DaemonSets manage **Node coverage**.

When a new Node joins the cluster, the DaemonSet automatically schedules a Pod onto it.

When a Node is removed, the corresponding DaemonSet Pod is also removed.

DaemonSets are commonly used for:

- Log Collection
- Monitoring Agents
- Security Agents
- Network Plugins
- Storage Plugins
- Node Management
- System Services

---

# Learning Objectives

After completing this chapter, you will understand:

- What a DaemonSet is
- Why DaemonSets are needed
- DaemonSet Architecture
- DaemonSet Scheduling
- DaemonSet Lifecycle
- Updating DaemonSets
- Node Selectors
- Taints & Tolerations
- Common Use Cases
- Best Practices

---

# Why DaemonSets?

Imagine a cluster.

```
Cluster

│

├── Node 1

├── Node 2

├── Node 3

└── Node 4
```

You want a monitoring agent on **every Node**.

Using a Deployment:

```
Deployment

↓

3 Pods
```

Problem:

```
Node 4

↓

No Monitoring Agent
```

A Deployment controls the **number of Pods**, not where they run.

---

# Solution

Use a DaemonSet.

```
DaemonSet

↓

Node 1

↓

Monitoring Pod

↓

Node 2

↓

Monitoring Pod

↓

Node 3

↓

Monitoring Pod

↓

Node 4

↓

Monitoring Pod
```

Every eligible Node receives a Pod.

---

# What is a DaemonSet?

A DaemonSet is a controller that ensures a Pod runs on every eligible Node.

```
DaemonSet

↓

All Nodes

↓

One Pod Per Node
```

---

# DaemonSet Architecture

```
                 DaemonSet

                     │

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

    Node 1         Node 2         Node 3

      │              │              │

      ▼              ▼              ▼

     Pod            Pod            Pod
```

If more Nodes are added, more Pods are created automatically.

---

# DaemonSet Responsibilities

DaemonSets:

- Ensure Node coverage
- Schedule Pods automatically
- Replace failed Pods
- Handle Node additions
- Handle Node removals
- Support rolling updates

---

# Deployment vs DaemonSet

| Deployment | DaemonSet |
|------------|-----------|
| Fixed number of Pods | One Pod per eligible Node |
| Scales by replicas | Scales automatically with Nodes |
| Used for applications | Used for Node-level services |
| User controls replica count | Kubernetes controls Pod count based on Nodes |

---

# ReplicaSet vs DaemonSet

| ReplicaSet | DaemonSet |
|-------------|-----------|
| Desired replica count | Desired Node coverage |
| Replica-based scheduling | Node-based scheduling |
| Multiple Pods may run on one Node | Typically one Pod per eligible Node |

---

# DaemonSet Workflow

```
DaemonSet

↓

Watch Nodes

↓

Find Eligible Nodes

↓

Schedule Pod

↓

Monitor Pod

↓

Replace if Needed
```

---

# DaemonSet YAML

```yaml
apiVersion: apps/v1

kind: DaemonSet

metadata:

  name: fluentd

spec:

  selector:

    matchLabels:

      app: fluentd

  template:

    metadata:

      labels:

        app: fluentd

    spec:

      containers:

      - name: fluentd

        image: fluent/fluentd
```

---

# YAML Structure

```
DaemonSet

↓

Metadata

↓

Selector

↓

Pod Template
```

Notice:

```
No replicas field
```

The number of Pods depends on the number of eligible Nodes.

---

# Scheduling Process

Suppose:

```
Cluster

↓

5 Nodes
```

DaemonSet:

```
Fluentd
```

Result:

```
5 Pods
```

One Pod per Node.

---

# New Node Added

Current:

```
4 Nodes

↓

4 Pods
```

New Node joins:

```
Node 5
```

DaemonSet detects:

```
New Node

↓

Create Pod
```

Automatically.

---

# Node Removed

Suppose:

```
Node 3

↓

Removed
```

DaemonSet:

```
Delete Corresponding Pod
```

No manual cleanup required.

---

# Node Failure

Suppose:

```
Node

↓

Offline
```

DaemonSet:

```
Pod Lost
```

If the Node returns:

```
Pod Created Again
```

---

# Common DaemonSet Use Cases

## Logging

```
Node

↓

Fluent Bit

↓

ElasticSearch
```

---

## Monitoring

```
Node

↓

Node Exporter

↓

Prometheus
```

---

## Security

```
Node

↓

Falco

↓

Security Events
```

---

## Networking

```
Node

↓

CNI Plugin
```

Examples:

- Calico
- Cilium
- Flannel

---

## Storage

```
Node

↓

CSI Driver
```

Storage plugins commonly use DaemonSets.

---

# Node Selectors

Sometimes:

```
Only Linux Nodes
```

Example:

```yaml
nodeSelector:

  kubernetes.io/os: linux
```

Result:

```
Linux

↓

Pod

Windows

↓

Ignored
```

---

# Taints & Tolerations

Suppose:

```
Master Node

↓

NoSchedule
```

DaemonSet can tolerate:

```yaml
tolerations:
```

Result:

```
Control Plane

↓

DaemonSet Pod
```

Useful for cluster-level agents.

---

# Rolling Updates

DaemonSets support rolling updates.

Workflow:

```
Old Pod

↓

New Pod

↓

Old Pod

↓

New Pod
```

Node-by-node updates minimize disruption.

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

With `OnDelete`, Pods are updated only when they are manually deleted.

---

# Viewing DaemonSets

List:

```bash
kubectl get daemonsets
```

or

```bash
kubectl get ds
```

Describe:

```bash
kubectl describe daemonset fluentd
```

---

# Updating DaemonSet

Edit:

```bash
kubectl edit daemonset fluentd
```

or

```bash
kubectl apply -f daemonset.yaml
```

---

# Deleting DaemonSet

Delete:

```bash
kubectl delete daemonset fluentd
```

Result:

```
DaemonSet

↓

Pods Removed
```

The managed Pods are deleted unless orphaning behavior is explicitly requested.

---

# DaemonSet Lifecycle

```
Create

↓

Watch Nodes

↓

Create Pods

↓

Monitor Nodes

↓

Update Pods

↓

Delete
```

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f daemonset.yaml
```

View:

```bash
kubectl get ds
```

Describe:

```bash
kubectl describe ds fluentd
```

View Pods:

```bash
kubectl get pods -o wide
```

Delete:

```bash
kubectl delete ds fluentd
```

---

# DaemonSet Architecture Summary

```
DaemonSet

↓

Eligible Nodes

↓

One Pod Per Node

↓

System Service
```

---

# Best Practices

### 1. Use DaemonSets for Node-Level Services

Examples:

- Logging
- Monitoring
- Networking
- Security

---

### 2. Use Node Selectors

Schedule Pods only on compatible Nodes.

---

### 3. Configure Tolerations Carefully

Only allow Pods onto tainted Nodes when required.

---

### 4. Monitor DaemonSet Status

Check:

```bash
kubectl get ds
```

to verify desired, current, ready, and available Pods.

---

### 5. Keep DaemonSet Containers Lightweight

DaemonSet Pods run on many or all Nodes, so optimize CPU and memory usage.

---

