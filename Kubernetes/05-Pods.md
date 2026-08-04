# Chapter 5 – Pods

## Overview

A **Pod** is the **smallest deployable unit** in Kubernetes.

Unlike Docker, where the smallest deployable object is a **container**, Kubernetes deploys and manages **Pods**, which may contain **one or more containers** that share the same execution environment.

Every application running inside a Kubernetes cluster ultimately runs inside a Pod.

Whether you deploy:

- NGINX
- Python API
- Java Application
- Node.js Service
- Machine Learning Model
- Database Agent

it always runs inside a Pod.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Pod is
- Pod Architecture
- Pod Lifecycle
- Single-container Pods
- Multi-container Pods
- Init Containers
- Shared Networking
- Shared Storage
- Pod Phases
- Restart Policies
- Pod YAML
- Pod Best Practices

---

# What is a Pod?

A Pod is a logical wrapper around one or more containers.

```
Pod

↓

Container(s)

↓

Application
```

The Pod provides:

- Networking
- Storage
- Lifecycle
- Scheduling

Containers inside the same Pod work together.

---

# Why Kubernetes Uses Pods

Suppose Kubernetes managed containers directly.

```
Container A

Container B

Container C
```

Managing tightly coupled containers would become difficult.

Instead:

```
Pod

├── Container A

├── Container B

└── Shared Resources
```

The Pod becomes the deployment unit.

---

# Pod Characteristics

A Pod:

- Has one IP address
- Shares network namespace
- Shares storage volumes
- Runs on one node
- Is scheduled as one unit
- Is ephemeral
- Can contain one or more containers

---

# Pod Architecture

```
                Pod

     ┌──────────────────────┐

     │                      │

     │  Container A         │

     │                      │

     │  Container B         │

     │                      │

     │ Shared Network       │

     │ Shared Storage       │

     └──────────────────────┘
```

---

# Single-Container Pod

Most Pods contain one container.

```
Pod

↓

NGINX Container
```

Advantages:

- Simple
- Easy to manage
- Common production pattern

Example:

```
Pod

↓

Python API
```

---

# Multi-Container Pod

Sometimes multiple containers work together.

Example:

```
Pod

├── Web Server

└── Log Collector
```

Both containers:

- Share localhost
- Share storage
- Start on the same node
- Have the same lifecycle

---

# Pod Networking

Every Pod receives:

```
Pod

↓

Unique IP Address
```

Containers inside the Pod communicate using:

```
localhost
```

Example:

```
Container A

↓

localhost

↓

Container B
```

No external networking is required between containers in the same Pod.

---

# Shared Storage

Containers share mounted volumes.

```
Pod

↓

Volume

↓

Container A

↓

Container B
```

Both containers can access the same files.

---

# Pod Lifecycle

```
Create

↓

Schedule

↓

Initialize

↓

Run

↓

Terminate
```

Every Pod follows this lifecycle.

---

# Pod Phases

Common Pod phases include:

```
Pending

↓

Running

↓

Succeeded

↓

Failed

↓

Unknown
```

---

## Pending

The Pod has been accepted by Kubernetes but is not yet running.

Possible reasons:

- Waiting for scheduling
- Pulling container image
- Initializing volumes

---

## Running

The Pod is executing.

Containers are running or starting.

```
Running

↓

Application Available
```

---

## Succeeded

All containers exited successfully.

Common for:

- Batch jobs
- One-time tasks

---

## Failed

One or more containers terminated unsuccessfully.

Possible causes:

- Application error
- Crash
- Configuration issue

---

## Unknown

Kubernetes cannot determine Pod state.

Usually caused by communication issues with the node.

---

# Pod Lifecycle Example

```
Create YAML

↓

kubectl apply

↓

Pending

↓

Scheduled

↓

Running

↓

Deleted
```

---

# Pod Scheduling

Pods begin in:

```
Pending
```

Scheduler selects:

```
Worker Node
```

Workflow:

```
Pending

↓

Scheduler

↓

Node Selected

↓

kubelet

↓

Pod Running
```

---

# Pod IP Address

Each Pod gets:

```
Unique Cluster IP
```

Example:

```
Pod A

↓

10.244.1.2

Pod B

↓

10.244.1.3
```

These IPs are generally dynamic and should not be relied upon directly by applications.

---

# Pod Communication

Pods communicate through:

```
Services
```

Instead of:

```
Pod IP
```

Because Pod IPs can change when Pods are recreated.

---

# Pod Restart Policy

Supported restart policies:

```
Always

OnFailure

Never
```

Default:

```
Always
```

Restart behavior depends on the workload type and controller.

---

# Pod YAML Structure

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:
  name: nginx

spec:
  containers:

  - name: nginx

    image: nginx
```

This is the minimum structure required for a simple Pod.

---

# Creating a Pod

```bash
kubectl apply -f pod.yaml
```

Verify:

```bash
kubectl get pods
```

Describe:

```bash
kubectl describe pod nginx
```

Logs:

```bash
kubectl logs nginx
```

---

# Deleting a Pod

```bash
kubectl delete pod nginx
```

If the Pod is managed by a Deployment or ReplicaSet, Kubernetes recreates it automatically.

---

# Pod vs Container

| Pod | Container |
|------|-----------|
| Kubernetes object | Runtime process |
| Can contain multiple containers | Runs application |
| Has shared networking | Individual process |
| Smallest deployable Kubernetes unit | Smallest Docker runtime unit |

---

# Pod vs Virtual Machine

| Pod | Virtual Machine |
|------|-----------------|
| Lightweight | Heavyweight |
| Shares host kernel | Own guest OS |
| Starts quickly | Slower startup |
| Managed by Kubernetes | Managed by Hypervisor |

---

# Pod Use Cases

Pods are used for:

- Web applications
- APIs
- Background workers
- Batch jobs
- Machine learning inference
- Monitoring agents
- Log collection
- Sidecar patterns

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f pod.yaml
```

View:

```bash
kubectl get pods
```

Describe:

```bash
kubectl describe pod nginx
```

Logs:

```bash
kubectl logs nginx
```

Delete:

```bash
kubectl delete pod nginx
```

Execute command:

```bash
kubectl exec -it nginx -- /bin/sh
```

---

# Pod Architecture Summary

```
Pod

↓

Container(s)

↓

Shared Network

↓

Shared Storage

↓

Application
```

---

# Best Practices

### 1. Prefer One Main Application Container Per Pod

Most workloads should follow the single-container Pod model unless there is a strong architectural reason to colocate containers.

---

### 2. Treat Pods as Ephemeral

Pods are designed to be replaced rather than repaired.

---

### 3. Do Not Depend on Pod IPs

Use Kubernetes Services for stable network access.

---

### 4. Keep Pods Small and Focused

A Pod should have a clear responsibility.

---

### 5. Use Controllers

In production, avoid creating standalone Pods for long-running applications.

Instead, use:

- Deployments
- StatefulSets
- DaemonSets

These controllers manage Pod lifecycle automatically.

---

