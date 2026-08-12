# Chapter 37 – Node Selectors

## Overview

In the previous chapter, we learned how the Kubernetes Scheduler selects a suitable Node for a Pod.

By default, the Scheduler considers many factors when selecting a Node.

But sometimes an application has a specific requirement.

For example:

- Run the application only on SSD Nodes.
- Run GPU workloads only on GPU Nodes.
- Run production workloads only on production Nodes.
- Run workloads in a particular environment.
- Run workloads on Nodes with a specific architecture.

Kubernetes provides **Node Selectors** for simple Node selection.

A `nodeSelector` allows a Pod to specify:

> **"Schedule me only on Nodes that have these labels."**

The mechanism is simple:

```text
Node

↓

Label

↓

nodeSelector

↓

Scheduler

↓

Matching Node
```

---

# Learning Objectives

After completing this chapter, you will understand:

- What Node Selectors are
- What Node labels are
- How `nodeSelector` works
- How the Scheduler uses Node Selectors
- Creating Node labels
- Using multiple labels
- AND behavior of multiple selectors
- Node Selector vs nodeName
- Node Selector vs Node Affinity
- Real-world use cases
- Scheduling failures
- Hands-on Labs
- Best practices

---

# Why Do We Need Node Selectors?

Suppose a Kubernetes cluster contains:

```text
Worker Node 1
disk=ssd

Worker Node 2
disk=hdd

Worker Node 3
disk=ssd
```

A database application may require fast SSD storage.

Without Node selection:

```text
Database Pod

↓

Any suitable Node
```

The Pod could potentially run on:

```text
disk=hdd
```

which may not meet the workload's performance requirements.

With:

```yaml
nodeSelector:
  disk: ssd
```

the Scheduler considers only Nodes labeled:

```text
disk=ssd
```

---

# What is a Node Selector?

A `nodeSelector` is a simple Pod scheduling constraint based on Node labels.

Example:

```yaml
spec:

  nodeSelector:

    disk: ssd
```

This means:

```text
Pod

↓

Find Nodes where:

disk = ssd
```

Only Nodes satisfying the selector are eligible.

---

# What are Node Labels?

Labels are key-value pairs attached to Kubernetes objects.

For Nodes:

```text
key=value
```

Example:

```text
disk=ssd
```

Another example:

```text
environment=production
```

Another:

```text
workload=database
```

---

# Node Label Architecture

```text
Worker Node

┌─────────────────────────────┐
│                             │
│ disk=ssd                    │
│ environment=production      │
│ workload=database           │
│                             │
└─────────────────────────────┘
```

A Pod can select Nodes based on these labels.

---

# High-Level Architecture

```text
                    Pod

                     │

                     ▼

              nodeSelector

                     │

                     ▼

                  Scheduler

                     │

       ┌─────────────┼─────────────┐

       ▼             ▼             ▼

    Node 1         Node 2        Node 3

   disk=ssd       disk=hdd      disk=ssd

       │             X             │
       │                           │
       └────────── Candidates ─────┘

                     │

                     ▼

                Selected Node
```

---

# Creating Node Labels

Use:

```bash
kubectl label node <node-name> disk=ssd
```

Example:

```bash
kubectl label node worker-01 disk=ssd
```

Verify:

```bash
kubectl get nodes --show-labels
```

---

# View Node Labels

```bash
kubectl get nodes --show-labels
```

Example:

```text
NAME        STATUS   LABELS

worker-01   Ready    disk=ssd,...

worker-02   Ready    disk=hdd,...
```

---

# View Labels Using JSON

```bash
kubectl get node worker-01 -o json
```

Look for:

```text
metadata.labels
```

---

# View Labels More Clearly

```bash
kubectl get nodes \
-L disk \
-L environment \
-L workload
```

Example:

```text
NAME        STATUS   DISK   ENVIRONMENT   WORKLOAD

worker-01   Ready    ssd    production    database

worker-02   Ready    hdd    development   general
```

---

# Basic nodeSelector Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: ssd-pod

spec:

  nodeSelector:

    disk: ssd

  containers:

  - name: nginx

    image: nginx
```

The Pod can only be scheduled onto Nodes with:

```text
disk=ssd
```

---

# Scheduling Workflow

```text
Pod Created

↓

API Server

↓

Scheduler

↓

Read nodeSelector

↓

Inspect Node Labels

↓

Filter Nodes

↓

Select Matching Node

↓

Bind Pod
```

---

# Example Cluster

Suppose:

```text
Node 1
disk=ssd

Node 2
disk=hdd

Node 3
disk=ssd
```

Pod:

```yaml
nodeSelector:

  disk: ssd
```

Scheduler:

```text
Node 1 → Match
Node 2 → Reject
Node 3 → Match
```

The Scheduler can choose:

```text
Node 1
```

or:

```text
Node 3
```

based on the rest of its scheduling process.

---

# Important Point

A `nodeSelector` does **not** tell Kubernetes:

```text
Run specifically on Node 1
```

It tells Kubernetes:

```text
Run on any Node matching these labels.
```

---

# Multiple Node Selector Labels

You can specify multiple key-value pairs.

Example:

```yaml
nodeSelector:

  disk: ssd

  environment: production
```

The Node must satisfy **both** conditions.

```text
disk=ssd

AND

environment=production
```

---

# Example

Nodes:

```text
Node 1

disk=ssd
environment=production
```

```text
Node 2

disk=ssd
environment=development
```

```text
Node 3

disk=hdd
environment=production
```

Selector:

```yaml
nodeSelector:

  disk: ssd

  environment: production
```

Result:

```text
Node 1 → Match
Node 2 → Reject
Node 3 → Reject
```

Only Node 1 is eligible.

---

# Node Selector Uses AND Logic

Multiple selectors mean:

```text
Condition A

AND

Condition B

AND

Condition C
```

All conditions must match.

---

# Example

```yaml
nodeSelector:

  disk: ssd

  environment: production

  architecture: amd64
```

A Node must have:

```text
disk=ssd

AND

environment=production

AND

architecture=amd64
```

---

# Node Selector and Architecture

Kubernetes Nodes commonly have architecture labels.

Example:

```text
kubernetes.io/arch=amd64
```

or:

```text
kubernetes.io/arch=arm64
```

A workload requiring a particular architecture can use an appropriate scheduling constraint.

Example:

```yaml
nodeSelector:

  kubernetes.io/arch: amd64
```

---

# Node Selector and Operating System

Nodes can also have OS labels such as:

```text
kubernetes.io/os=linux
```

Example:

```yaml
nodeSelector:

  kubernetes.io/os: linux
```

This can be useful when workloads are intended for a particular operating system.

---

# Node Selector and GPU Nodes

Suppose GPU Nodes have:

```text
accelerator=nvidia
```

A Pod can specify:

```yaml
nodeSelector:

  accelerator: nvidia
```

However, in production GPU workloads, simply selecting a GPU Node is generally not enough.

The workload should also request the appropriate GPU resource through the relevant device plugin.

Conceptually:

```text
Pod

↓

GPU Resource Request

+

Node Selection

↓

GPU Node
```

---

# Node Selector and Environments

Example labels:

```text
environment=production
```

```text
environment=staging
```

```text
environment=development
```

Production workload:

```yaml
nodeSelector:

  environment: production
```

---

# Node Selector and Workload Types

Example:

```text
workload=database
```

Database Pod:

```yaml
nodeSelector:

  workload: database
```

API workload:

```yaml
nodeSelector:

  workload: api
```

---

# Node Selector vs nodeName

These are often confused.

## nodeName

```yaml
nodeName: worker-01
```

Means:

```text
Run specifically on worker-01
```

---

## nodeSelector

```yaml
nodeSelector:

  disk: ssd
```

Means:

```text
Run on any Node where:

disk=ssd
```

---

# Comparison

| Feature | nodeName | nodeSelector |
|---|---|---|
| Selects exact Node | Yes | No |
| Uses labels | No | Yes |
| Scheduler flexibility | Very low | Higher |
| Supports multiple matching Nodes | No | Yes |
| Recommended for general scheduling | No | Yes |

---

# Node Selector vs Node Affinity

`nodeSelector` is intentionally simple.

It supports exact label matching:

```text
key=value
```

Node Affinity provides much more expressive scheduling rules.

For example:

```text
In
NotIn
Exists
DoesNotExist
Gt
Lt
```

Node Affinity also supports:

```text
requiredDuringSchedulingIgnoredDuringExecution
```

and:

```text
preferredDuringSchedulingIgnoredDuringExecution
```

Therefore:

```text
nodeSelector

↓

Simple requirements
```

while:

```text
nodeAffinity

↓

Advanced requirements
```

Node Affinity will be covered in the next chapter.

---

# Node Selector and Taints

Node Selector and Taints solve different problems.

Node Selector:

```text
Pod

↓

Which Nodes should I prefer/be allowed to run on?
```

Taint:

```text
Node

↓

Which Pods should NOT run here?
```

Toleration:

```text
Pod

↓

I am allowed to run on this tainted Node.
```

These mechanisms can work together.

---

# Example

Node:

```text
workload=database
```

and:

```text
dedicated=database:NoSchedule
```

Pod:

```yaml
nodeSelector:

  workload: database

tolerations:

- key: dedicated

  operator: Equal

  value: database

  effect: NoSchedule
```

The Pod:

1. Selects database Nodes.
2. Tolerates the database taint.

---

# Node Selector and Scheduler

The Scheduler uses the selector as part of its feasibility evaluation.

Conceptually:

```text
Pod

↓

nodeSelector

↓

Filter Nodes

↓

Matching Nodes

↓

Continue Scheduling
```

The selector does not directly schedule the Pod.

The Scheduler still performs the overall scheduling decision.

---

# Scheduling Failure

Suppose:

```text
Node 1
disk=hdd

Node 2
disk=hdd

Node 3
disk=hdd
```

Pod:

```yaml
nodeSelector:

  disk: ssd
```

No Node matches.

Result:

```text
Pod

↓

Pending
```

---

# Troubleshooting Pending Pods

Run:

```bash
kubectl get pods
```

Then:

```bash
kubectl describe pod <pod-name>
```

Look at:

```text
Events
```

You may see:

```text
FailedScheduling
```

with information indicating that no Nodes satisfy the scheduling requirements.

---

# Example Failure

```text
0/3 nodes are available:

3 node(s) didn't match Pod's node affinity/selector
```

Interpretation:

```text
Pod requires:

disk=ssd
```

but:

```text
Available Nodes:

disk=hdd
```

---

# Modifying Node Labels

Add:

```bash
kubectl label node worker-01 disk=ssd
```

Change:

```bash
kubectl label node worker-01 disk=nvme --overwrite
```

Remove:

```bash
kubectl label node worker-01 disk-
```

---

# Important Warning

Changing labels can affect future scheduling.

For example:

```text
Pod

nodeSelector:

disk=ssd
```

Node currently:

```text
disk=ssd
```

If the label is changed:

```text
disk=hdd
```

the Node no longer matches the selector.

The Pod's behavior after scheduling is governed by the semantics of the scheduling constraint; `nodeSelector` does not continuously evict already-running Pods merely because a label later changes.

For stronger dynamic placement behavior, more advanced scheduling mechanisms may be required.

---

# Built-in Node Labels

Kubernetes and the platform environment may provide standard labels such as:

```text
kubernetes.io/hostname
```

```text
kubernetes.io/os
```

```text
kubernetes.io/arch
```

Cloud environments may expose additional topology labels.

Always verify the labels available in your actual cluster:

```bash
kubectl get nodes --show-labels
```

---

# Custom Labels

Organizations commonly create their own labels.

Examples:

```text
environment=production
```

```text
team=security
```

```text
workload=database
```

```text
hardware=high-memory
```

```text
disk=nvme
```

---

# Label Naming Best Practices

Prefer meaningful labels.

Good:

```text
environment=production
```

```text
workload=database
```

```text
hardware=high-memory
```

Avoid meaningless labels such as:

```text
node1=yes
```

or:

```text
abc=true
```

unless they have a documented purpose.

---

# Label Key Namespaces

Kubernetes labels can use qualified names.

For example:

```text
example.com/workload=database
```

This helps organizations avoid conflicts with labels managed by Kubernetes or other components.

---

# Real-World Example – Database Nodes

Cluster:

```text
worker-01
worker-02
worker-03
```

Labels:

```text
worker-01
workload=database
```

```text
worker-02
workload=general
```

```text
worker-03
workload=database
```

Database Pod:

```yaml
nodeSelector:

  workload: database
```

Result:

```text
worker-01

OR

worker-03
```

---

# Real-World Example – Production Nodes

Labels:

```text
environment=production
```

Pod:

```yaml
nodeSelector:

  environment: production
```

The workload will only be considered for production-labeled Nodes.

---

# Real-World Example – SSD Nodes

Labels:

```text
disk=ssd
```

Pod:

```yaml
nodeSelector:

  disk: ssd
```

Useful for workloads that require specific hardware characteristics.

---

# Real-World Example – ARM Workloads

Labels:

```text
kubernetes.io/arch=arm64
```

Pod:

```yaml
nodeSelector:

  kubernetes.io/arch: arm64
```

The container image must also support ARM64.

Node selection alone does not make an incompatible image runnable.

---

# Hands-on Lab 1 – List Nodes

Run:

```bash
kubectl get nodes
```

Then:

```bash
kubectl get nodes --show-labels
```

Identify existing labels.

---

# Hands-on Lab 2 – Add a Custom Label

Select a Node:

```bash
kubectl label node <node-name> disk=ssd
```

Verify:

```bash
kubectl get nodes -L disk
```

---

# Hands-on Lab 3 – Schedule Using nodeSelector

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: node-selector-demo

spec:

  nodeSelector:

    disk: ssd

  containers:

  - name: nginx

    image: nginx
```

Apply:

```bash
kubectl apply -f node-selector-demo.yaml
```

Check:

```bash
kubectl get pod node-selector-demo -o wide
```

---

# Hands-on Lab 4 – Inspect Scheduling Events

```bash
kubectl describe pod node-selector-demo
```

Look for:

```text
Scheduled
```

---

# Hands-on Lab 5 – Create an Impossible Selector

Create:

```yaml
nodeSelector:

  disk: quantum-storage
```

If no Node has this label:

```text
Pod

↓

Pending
```

Inspect:

```bash
kubectl describe pod <pod-name>
```

---

# Hands-on Lab 6 – Multiple Selectors

Label a Node:

```bash
kubectl label node <node-name> \
disk=ssd \
environment=production
```

Create:

```yaml
nodeSelector:

  disk: ssd

  environment: production
```

Verify the Pod is scheduled only on Nodes matching both labels.

---

# Hands-on Lab 7 – Modify a Label

Change:

```bash
kubectl label node <node-name> disk=hdd --overwrite
```

Inspect:

```bash
kubectl get nodes -L disk
```

Observe how the Node no longer matches:

```text
disk=ssd
```

---

# Hands-on Lab 8 – Compare nodeName

Create two Pods.

Pod A:

```yaml
nodeName: worker-01
```

Pod B:

```yaml
nodeSelector:

  disk: ssd
```

Compare their scheduling behavior.

---

# Common Mistakes

## 1. Forgetting to Label Nodes

Pod:

```yaml
nodeSelector:

  disk: ssd
```

but Nodes have no:

```text
disk=ssd
```

Result:

```text
Pending
```

---

## 2. Typing the Wrong Label Value

Node:

```text
disk=SSD
```

Pod:

```text
disk=ssd
```

Labels are case-sensitive.

Result:

```text
No Match
```

---

## 3. Assuming nodeSelector Selects One Specific Node

It doesn't.

It selects a set of matching Nodes.

The Scheduler decides which matching Node to use.

---

## 4. Using nodeName Instead of nodeSelector

Hard-coded Node assignments reduce scheduling flexibility.

---

## 5. Using Too Many Labels

Excessive scheduling labels can make cluster management complicated.

Use labels that represent meaningful infrastructure or workload characteristics.

---

## 6. Assuming Labels Guarantee Hardware Capability

A label is only metadata.

For example:

```text
gpu=true
```

does not automatically install GPU drivers or expose GPU resources.

The actual Node must have the required capability.

---

## 7. Ignoring Taints

A Node may match:

```text
nodeSelector
```

but still reject the Pod because of an untolerated taint.

---

# Node Selector vs Related Concepts

| Feature | Purpose |
|---|---|
| Node Labels | Describe Nodes |
| nodeSelector | Simple Node selection |
| Node Affinity | Advanced Node selection |
| Taints | Repel Pods |
| Tolerations | Allow Pods onto tainted Nodes |
| nodeName | Direct Node assignment |

---

# Quick Revision

## Node Selector

```text
Pod

↓

nodeSelector

↓

Node Labels

↓

Matching Nodes
```

---

## Multiple Selectors

```text
disk=ssd

AND

environment=production
```

---

## Scheduler

```text
nodeSelector

↓

Filter

↓

Matching Nodes

↓

Scheduler

↓

Selected Node
```

---

## Troubleshooting

```bash
kubectl describe pod <pod-name>
```

Look for:

```text
FailedScheduling
```

---

# Essential kubectl Commands

List Nodes:

```bash
kubectl get nodes
```

Show Labels:

```bash
kubectl get nodes --show-labels
```

Show Selected Labels:

```bash
kubectl get nodes -L disk
```

Add Label:

```bash
kubectl label node <node-name> disk=ssd
```

Update Label:

```bash
kubectl label node <node-name> disk=nvme --overwrite
```

Remove Label:

```bash
kubectl label node <node-name> disk-
```

Describe Node:

```bash
kubectl describe node <node-name>
```

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

---

# Interview Questions

## Basic

- What is a Node Selector?
- What is a Node label?
- How do you label a Kubernetes Node?
- How does `nodeSelector` work?
- Can multiple Nodes satisfy the same `nodeSelector`?

---

## Intermediate

- What happens if no Node matches a `nodeSelector`?
- Can you specify multiple labels in a `nodeSelector`?
- What logic is used when multiple selectors are specified?
- What is the difference between `nodeName` and `nodeSelector`?
- How do you troubleshoot a Pod stuck in Pending because of a selector?

---

## Advanced

- Explain how `nodeSelector` participates in the Scheduler's filtering process.
- Compare `nodeSelector` and Node Affinity.
- How can Node labels be used to implement workload isolation?
- How do taints and `nodeSelector` work together?
- What happens if a Node's label changes after a Pod has already been scheduled?
- Why is Node Affinity preferred over `nodeSelector` for complex scheduling requirements?
- How would you design labels for a large production Kubernetes cluster?

---

# Production Design Example

A production cluster could use labels such as:

```text
environment=production
```

```text
workload=database
```

```text
hardware=high-memory
```

```text
disk=nvme
```

```text
team=security
```

Applications can then express simple scheduling requirements.

Example:

```yaml
spec:

  nodeSelector:

    environment: production

    workload: database
```

Architecture:

```text
                    Production Cluster

                          │

             ┌────────────┼────────────┐

             ▼            ▼            ▼

        Database       API Nodes     Worker Nodes

        workload=      workload=     workload=
        database       api            worker

             │
             ▼

        nodeSelector
```

---

# Best Practices

### 1. Use Meaningful Labels

Labels should describe real Node characteristics or organizational requirements.

---

### 2. Avoid Hard-Coded nodeName

Prefer label-based scheduling when possible.

---

### 3. Document Custom Labels

For large clusters, maintain a clear labeling convention.

---

### 4. Use Node Affinity for Complex Requirements

If requirements involve:

- OR conditions
- preferred Nodes
- advanced expressions

use Node Affinity.

---

### 5. Combine with Taints When Necessary

Use:

```text
nodeSelector

+

taints/tolerations
```

when you need both selection and workload isolation.

---

### 6. Verify Labels Before Deployment

Run:

```bash
kubectl get nodes --show-labels
```

before creating workloads that depend on custom labels.

---

### 7. Use Stable Label Keys

Avoid frequently changing labels that can unexpectedly affect scheduling behavior.

---

# References

## Official Kubernetes Documentation

- Assigning Pods to Nodes
- Labels and Selectors
- Node Labels
- Node Affinity
- Taints and Tolerations
- Scheduling Framework

---

## CNCF Resources

- Kubernetes SIG Scheduling
- Kubernetes Node Management
- Cloud Native Computing Foundation (CNCF)

---

# Recommended Practice

1. List all Nodes in your cluster.
2. Inspect their existing labels.
3. Create custom labels for different Node types.
4. Deploy Pods using `nodeSelector`.
5. Use multiple selectors and observe AND behavior.
6. Create an invalid selector and troubleshoot the resulting Pending Pod.
7. Compare `nodeName` and `nodeSelector`.
8. Experiment with Node labels and taints together.
9. Design a realistic labeling strategy for a production cluster.
10. Move to Node Affinity once simple label matching becomes insufficient.

---

# Chapter Summary

```text
Node

↓

Labels

↓

nodeSelector

↓

Scheduler

↓

Matching Nodes

↓

Selected Node
```

A **Node Selector** provides a simple and predictable way to control where Kubernetes Pods can run. It works by matching Pod requirements against Node labels.

The fundamental relationship is:

```text
Node Label
    ↓
disk=ssd

Pod
    ↓
nodeSelector:
  disk: ssd

Scheduler
    ↓
Only matching Nodes are eligible
```

The key distinction to remember is:

```text
nodeName
    ↓
Specific Node

nodeSelector
    ↓
Any Node matching labels

Node Affinity
    ↓
Advanced Node selection
```

`nodeSelector` is excellent for simple scheduling requirements, but complex production scheduling often requires **Node Affinity**, which provides richer expressions and preferred scheduling behavior.

---

## Next Chapter

# Chapter 38 – Node Affinity

Topics will include:

- What is Node Affinity?
- Why Node Affinity is needed
- `requiredDuringSchedulingIgnoredDuringExecution`
- `preferredDuringSchedulingIgnoredDuringExecution`
- `In`
- `NotIn`
- `Exists`
- `DoesNotExist`
- `Gt`
- `Lt`
- Multiple Node Affinity Rules
- Required vs Preferred Affinity
- Node Selector vs Node Affinity
- Real-World Scheduling Patterns
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---