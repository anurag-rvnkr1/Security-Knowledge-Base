# Chapter 2 – Kubernetes Architecture

## Overview

Kubernetes architecture defines how all Kubernetes components work together to deploy, manage, scale, secure, and maintain containerized applications.

Unlike Docker, which manages containers on a single machine, Kubernetes manages an entire cluster of machines using a distributed architecture.

Understanding Kubernetes architecture is essential because every operation—creating Pods, scaling applications, rolling updates, networking, storage, and security—depends on these components working together.

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes Cluster Architecture
- Control Plane Components
- Worker Node Components
- Kubernetes Control Loops
- Request Lifecycle
- Pod Scheduling
- Cluster Communication
- High Availability
- Component Responsibilities

---

# High-Level Kubernetes Architecture

A Kubernetes cluster consists of two major parts:

```
                Kubernetes Cluster

        ┌──────────────────────────┐
        │      Control Plane       │
        └──────────────────────────┘
                  │
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Worker Node  Worker Node  Worker Node
     │            │            │
    Pods         Pods         Pods
```

---

# Kubernetes Cluster

A cluster is a collection of machines working together to run applications.

A cluster contains:

- Control Plane
- Worker Nodes
- Networking
- Storage
- Applications

```
Cluster

↓

Control Plane

↓

Worker Nodes

↓

Pods
```

---

# Architecture Overview

```
                    User

                     │

               kubectl CLI

                     │

                     ▼

              Kubernetes API Server

                     │

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

   Scheduler   Controller Manager   etcd

                     │

                     ▼

             Worker Nodes

        ┌────────┬────────┐

        ▼        ▼        ▼

     kubelet kube-proxy Runtime

        │

        ▼

       Pods
```

Every Kubernetes operation passes through the API Server.

---

# Two Major Components

## 1. Control Plane

The Control Plane makes decisions.

Responsibilities:

- Scheduling
- Cluster management
- State management
- API handling
- Automation

---

## 2. Worker Nodes

Worker Nodes execute workloads.

Responsibilities:

- Run Pods
- Run Containers
- Report status
- Handle networking

---

# Control Plane Components

```
Control Plane

↓

API Server

↓

Scheduler

↓

Controller Manager

↓

etcd
```

Each component performs a specialized role.

---

# API Server

The API Server is the central communication hub of Kubernetes.

Everything communicates through it.

```
kubectl

↓

API Server

↓

Cluster
```

Responsibilities:

- Authentication
- Authorization
- Request validation
- Admission control
- REST API
- Object management

Without the API Server, the cluster cannot be managed.

---

# Scheduler

The Scheduler decides where Pods should run.

Workflow:

```
Pending Pod

↓

Available Nodes

↓

CPU

↓

Memory

↓

Policies

↓

Selected Node
```

The Scheduler does **not** run Pods.

It only selects the most appropriate node.

---

# Controller Manager

The Controller Manager continuously compares:

```
Desired State

↓

Current State
```

If differences exist:

```
Take Corrective Action
```

Examples:

- Replace failed Pods
- Scale applications
- Create ReplicaSets
- Manage Nodes

---

# etcd

etcd is Kubernetes' distributed key-value database.

It stores:

- Cluster state
- Deployments
- Pods
- Secrets
- ConfigMaps
- Nodes
- Networking information

```
API Server

↓

etcd
```

Without etcd, Kubernetes loses its source of truth.

---

# Worker Node Components

Every worker node contains:

```
Worker Node

↓

kubelet

↓

kube-proxy

↓

Container Runtime

↓

Pods
```

---

# kubelet

The kubelet is the primary node agent.

Responsibilities:

- Communicate with API Server
- Create Pods
- Monitor Pods
- Report node status

Workflow:

```
API Server

↓

kubelet

↓

Container Runtime

↓

Pod Running
```

---

# kube-proxy

kube-proxy manages network communication.

Responsibilities:

- Service networking
- Load balancing
- Network rules
- Traffic forwarding

```
Service

↓

kube-proxy

↓

Pod
```

---

# Container Runtime

The container runtime executes containers.

Examples:

- containerd
- CRI-O

Responsibilities:

- Pull images
- Start containers
- Stop containers
- Manage container lifecycle

---

# Pods

Pods are the smallest deployable Kubernetes object.

```
Pod

↓

Container

↓

Application
```

A Pod may contain:

- One container
- Multiple tightly coupled containers

---

# Component Communication

```
User

↓

kubectl

↓

API Server

↓

Scheduler

↓

Worker Node

↓

kubelet

↓

Container Runtime

↓

Pod
```

Every request flows through the API Server.

---

# Request Lifecycle

Suppose a user runs:

```bash
kubectl apply -f deployment.yaml
```

Workflow:

```
kubectl

↓

API Server

↓

Validate

↓

Store in etcd

↓

Scheduler

↓

Select Node

↓

kubelet

↓

Container Runtime

↓

Pod Created
```

---

# Cluster State Management

Kubernetes constantly compares:

```
Desired State

↓

Current State

↓

Difference?

↓

Correct
```

This continuous reconciliation enables self-healing.

---

# Self-Healing Example

Suppose:

```
Deployment

↓

3 Pods
```

Current state:

```
Only 2 Pods
```

Controller:

```
Create New Pod

↓

3 Pods Restored
```

---

# Scaling Example

Update:

```yaml
replicas: 5
```

Workflow:

```
Deployment

↓

Controller

↓

Scheduler

↓

New Pods

↓

5 Running Pods
```

---

# High Availability

Production clusters usually have multiple Control Plane nodes.

```
Control Plane A

Control Plane B

Control Plane C
```

Benefits:

- Fault tolerance
- Reduced downtime
- Better reliability

Worker Nodes are also distributed across multiple machines.

---

# Cluster Communication

```
kubectl

↓

API Server

↓

Control Plane

↓

Worker Nodes

↓

Pods
```

Worker Nodes communicate with the Control Plane through the API Server.

---

# Kubernetes Architecture Layers

```
Applications

↓

Pods

↓

Worker Nodes

↓

Control Plane

↓

Infrastructure
```

Each layer depends on the one below it.

---

# Architecture Benefits

Kubernetes architecture provides:

- High availability
- Automation
- Scalability
- Self-healing
- Resource optimization
- Declarative management
- Cloud portability

---

# Important Terminology

| Component | Purpose |
|-----------|---------|
| Cluster | Collection of machines |
| Control Plane | Manages the cluster |
| Worker Node | Runs workloads |
| API Server | Central communication point |
| Scheduler | Selects nodes for Pods |
| Controller Manager | Maintains desired state |
| etcd | Distributed key-value database |
| kubelet | Node agent |
| kube-proxy | Network management |
| Container Runtime | Runs containers |
| Pod | Smallest deployable object |

---

# Architecture Summary

```
Developer

↓

kubectl

↓

API Server

↓

etcd

↓

Scheduler

↓

Worker Node

↓

kubelet

↓

Container Runtime

↓

Pod Running
```

This architecture enables Kubernetes to manage thousands of workloads across many nodes in a consistent and automated manner.

---

