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

# How DaemonSets Work Internally

## Overview

A DaemonSet continuously monitors the Kubernetes cluster and ensures that **every eligible Node** runs exactly one DaemonSet Pod.

Unlike Deployments, which monitor the number of Pods, DaemonSets monitor the **set of Nodes** in the cluster.

Whenever:

- A new Node joins
- A Node is removed
- A Pod crashes
- A Node becomes schedulable

the DaemonSet Controller automatically reconciles the cluster state.

This behavior makes DaemonSets ideal for **Node-level infrastructure services**.

---

# High-Level Architecture

```
                 Kubernetes Cluster

                         │

                 API Server

                         │

              DaemonSet Controller

                         │

      ┌──────────────────┼──────────────────┐

      ▼                  ▼                  ▼

   Node 1             Node 2             Node 3

      │                  │                  │

      ▼                  ▼                  ▼

 Fluent Bit         Fluent Bit         Fluent Bit
```

Every eligible Node receives one DaemonSet Pod.

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

Store DaemonSet

↓

DaemonSet Controller

↓

Watch Nodes

↓

Find Eligible Nodes

↓

Create Pods

↓

Scheduler

↓

Worker Nodes

↓

Running
```

---

# Step 1 – DaemonSet Creation

Example:

```yaml
kind: DaemonSet
```

Deploy:

```bash
kubectl apply -f daemonset.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates request
- Authorizes request
- Validates YAML
- Stores DaemonSet

Workflow:

```
kubectl

↓

API Server

↓

DaemonSet Stored
```

---

# Step 3 – Store in etcd

```
API Server

↓

etcd
```

Current state:

```
DaemonSet Exists

↓

No Pods Yet
```

---

# Step 4 – DaemonSet Controller

The DaemonSet Controller continuously watches:

```
Nodes

↓

DaemonSet

↓

Pod Status
```

Its responsibility is to ensure every eligible Node has the required Pod.

---

# Step 5 – Node Discovery

Suppose:

```
Cluster

↓

5 Nodes
```

Controller discovers:

```
Node 1

Node 2

Node 3

Node 4

Node 5
```

Each Node is evaluated.

---

# Step 6 – Eligibility Check

The controller checks:

- Node selectors
- Node affinity
- Taints
- Tolerations
- Operating system
- Architecture

Example:

```
Linux Node

↓

Eligible

Windows Node

↓

Ignored
```

---

# Step 7 – Pod Creation

Eligible Node:

```
Node

↓

No DaemonSet Pod

↓

Create Pod
```

Result:

```
Node

↓

DaemonSet Pod
```

---

# Step 8 – Scheduler

Normally:

```
Scheduler

↓

Select Node
```

For DaemonSets:

```
DaemonSet Controller

↓

Chooses Target Node

↓

Scheduler Binds Pod
```

The controller determines **which Node** should receive the Pod.

---

# Step 9 – kubelet

Worker Node:

```
API Server

↓

kubelet

↓

Container Runtime

↓

Start Pod
```

---

# Final State

```
Cluster

↓

Node 1

↓

Pod

↓

Node 2

↓

Pod

↓

Node 3

↓

Pod
```

Desired state achieved.

---

# Continuous Monitoring

DaemonSet Controller never stops.

```
Nodes

↓

Compare

↓

Missing Pod?

↓

Create
```

This is Kubernetes' reconciliation loop.

---

# New Node Added

Current:

```
Cluster

↓

4 Nodes

↓

4 Pods
```

New Node joins:

```
Node 5
```

Controller detects:

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

Deleted
```

Result:

```
DaemonSet Pod

↓

Removed
```

The DaemonSet now targets only the remaining eligible Nodes.

---

# Node Failure

Current:

```
Node 2

↓

Offline
```

Pod becomes unavailable.

If the Node recovers:

```
Node Returns

↓

DaemonSet Pod

↓

Running
```

If the Node is permanently removed from the cluster, the corresponding Pod disappears with it.

---

# Pod Failure

Suppose:

```
Fluent Bit

↓

Crash
```

Current:

```
Node

↓

No Running Pod
```

DaemonSet:

```
Create Replacement

↓

Running
```

The DaemonSet restores the desired state.

---

# Node Labels

Example:

```yaml
nodeSelector:

  kubernetes.io/os: linux
```

Workflow:

```
Linux

↓

Pod

Windows

↓

Ignored
```

Only matching Nodes receive Pods.

---

# Node Affinity

More advanced scheduling:

```yaml
affinity:

  nodeAffinity:
```

Workflow:

```
Node Labels

↓

Affinity Rules

↓

Eligible?
```

Affinity provides more flexible placement than node selectors.

---

# Taints & Tolerations

Suppose:

```
Control Plane

↓

NoSchedule
```

DaemonSet:

```
Toleration

↓

Allowed
```

Without the matching toleration:

```
Ignored
```

Many infrastructure DaemonSets include tolerations so they can run on control plane nodes when appropriate.

---

# Rolling Updates

Suppose:

```
Image

↓

v1

↓

Need

↓

v2
```

DaemonSet:

```
Node 1

↓

Update

↓

Healthy

↓

Node 2

↓

Update
```

The rollout proceeds node by node.

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

With `OnDelete`, Pods are updated only after they are manually deleted.

---

# Internal Architecture

```
API Server

↓

DaemonSet Controller

↓

Eligible Nodes

↓

Pods

↓

Containers
```

---

# Logging Example

```
DaemonSet

↓

Fluent Bit

↓

Read Logs

↓

ElasticSearch
```

Every Node forwards logs.

---

# Monitoring Example

```
DaemonSet

↓

Node Exporter

↓

Prometheus
```

Every Node exports metrics.

---

# Security Example

```
DaemonSet

↓

Falco

↓

Runtime Detection
```

Every Node performs runtime security monitoring.

---

# CNI Example

```
DaemonSet

↓

Cilium

↓

Networking
```

Network plugins typically require one Pod on each Node.

---

# CSI Example

```
DaemonSet

↓

CSI Driver

↓

Storage
```

Storage plugins commonly use DaemonSets for Node-level operations.

---

# Hands-on Lab 1 – Create DaemonSet

Example:

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

Deploy:

```bash
kubectl apply -f daemonset.yaml
```

---

# Hands-on Lab 2 – Verify

```bash
kubectl get ds

kubectl get pods -o wide
```

Observe:

```
One Pod

↓

Each Node
```

---

# Hands-on Lab 3 – Add New Node

If using a lab cluster:

```
Add Worker Node
```

Observe:

```bash
kubectl get pods -o wide
```

A new DaemonSet Pod is scheduled automatically.

---

# Hands-on Lab 4 – Rolling Update

Update image:

```bash
kubectl set image daemonset/fluentd \
fluentd=fluent/fluentd:v2
```

Watch:

```bash
kubectl rollout status daemonset/fluentd
```

Observe Pods updating one node at a time.

---

# Hands-on Lab 5 – Describe DaemonSet

```bash
kubectl describe ds fluentd
```

Review:

- Desired Number Scheduled
- Current Number Scheduled
- Number Ready
- Updated Number Scheduled
- Events

---

# Common Mistakes

## 1. Using Deployments Instead of DaemonSets

Incorrect:

```
Deployment

↓

Monitoring Agent
```

Correct:

```
DaemonSet

↓

Monitoring Agent
```

---

## 2. Forgetting Node Selectors

Without scheduling constraints:

```
DaemonSet

↓

Every Node
```

Ensure this is the intended behavior.

---

## 3. Missing Tolerations

Control plane nodes often have taints.

Without appropriate tolerations:

```
DaemonSet

↓

Control Plane

↓

No Pod
```

---

## 4. Heavy Resource Usage

DaemonSets run on many or all Nodes.

An inefficient DaemonSet can consume significant cluster resources.

---

## 5. Assuming Replica Count

DaemonSets do **not** use:

```yaml
replicas:
```

The number of Pods depends on the number of eligible Nodes.

---

# DaemonSets Quick Revision

## Architecture

```
DaemonSet

↓

Eligible Nodes

↓

One Pod Per Node
```

---

## Workflow

```
DaemonSet

↓

Watch Nodes

↓

Create Pods

↓

Monitor

↓

Update
```

---

## Common Use Cases

```
Logging

↓

Monitoring

↓

Networking

↓

Storage

↓

Security
```

---

# Essential kubectl Commands

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

Update:

```bash
kubectl set image daemonset/fluentd \
fluentd=fluent/fluentd:v2
```

Rollout Status:

```bash
kubectl rollout status daemonset/fluentd
```

Delete:

```bash
kubectl delete ds fluentd
```

---

# Interview Questions

### Basic

- What is a DaemonSet?
- How is a DaemonSet different from a Deployment?
- Why doesn't a DaemonSet use replicas?

---

### Intermediate

- How does a DaemonSet determine where to schedule Pods?
- What happens when a new Node joins the cluster?
- Why are DaemonSets commonly used for monitoring agents?

---

### Advanced

- How does the DaemonSet Controller reconcile cluster state?
- What role do taints and tolerations play with DaemonSets?
- How do rolling updates work for DaemonSets?
- Why are most CNI plugins implemented as DaemonSets?
- What happens if a DaemonSet Pod is manually deleted?

---

# References

## Official Kubernetes Documentation

- DaemonSets
- Workload Controllers
- Scheduling
- Node Affinity
- Taints and Tolerations
- Rolling Updates

---

## CNCF Resources

- Kubernetes Best Practices
- Kubernetes Scheduling Guide
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- NSA/CISA Kubernetes Hardening Guidance
- Kubernetes Production Best Practices
- NIST SP 800-190

---

## Recommended Practice

1. Deploy a DaemonSet that runs a simple container on every Node.
2. Observe Pod placement with `kubectl get pods -o wide`.
3. Add node selectors to limit scheduling.
4. Configure tolerations to run on control plane nodes.
5. Perform a rolling update and monitor rollout progress.
6. Compare DaemonSet behavior with a Deployment.
7. Examine real-world DaemonSets such as Fluent Bit, Prometheus Node Exporter, or Cilium in a lab cluster.

---

# Chapter Summary

```
Developer

↓

DaemonSet

↓

API Server

↓

DaemonSet Controller

↓

Eligible Nodes

↓

One Pod Per Node

↓

Continuous Reconciliation
```

DaemonSets ensure that **Node-level services** such as logging agents, monitoring exporters, network plugins, and storage drivers run consistently across every eligible Node. They automatically adapt to cluster growth and shrinkage, making them an essential workload controller for Kubernetes infrastructure components.

---

