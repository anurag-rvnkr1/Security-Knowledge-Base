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

## How Kubernetes Architecture Works Internally

Kubernetes is built around a **control loop architecture**. Every component continuously communicates with the Kubernetes API Server to ensure that the **actual state** of the cluster matches the **desired state** defined by users.

Unlike traditional systems where administrators manually manage infrastructure, Kubernetes continuously automates cluster operations.

---

# Complete Kubernetes Request Flow

Suppose a developer deploys an application.

Command:

```bash
kubectl apply -f deployment.yaml
```

Complete workflow:

```
Developer

↓

kubectl

↓

API Server

↓

Authentication

↓

Authorization

↓

Validation

↓

Admission Controllers

↓

Store in etcd

↓

Controller Detects New Deployment

↓

ReplicaSet Created

↓

Scheduler Selects Node

↓

kubelet Receives Assignment

↓

Container Runtime Pulls Image

↓

Container Starts

↓

Pod Running

↓

Status Reported Back

↓

API Server Updated

↓

etcd Updated
```

Everything revolves around the API Server.

---

# Step 1 – User Sends Request

Example:

```bash
kubectl apply -f nginx.yaml
```

The request is converted into an API request.

```
kubectl

↓

REST API

↓

API Server
```

---

# Step 2 – Authentication

The API Server verifies:

```
Who is making the request?
```

Possible methods include:

- Client certificates
- Bearer tokens
- OpenID Connect (OIDC)
- Service Accounts
- External identity providers

If authentication fails:

```
Request Rejected
```

---

# Step 3 – Authorization

After identity is verified:

```
Can this user perform the requested action?
```

Common authorization mechanisms:

- RBAC
- Node Authorization
- Webhook Authorization

If unauthorized:

```
403 Forbidden
```

---

# Step 4 – Request Validation

The API Server validates:

- YAML syntax
- Object schema
- API version
- Required fields

Example:

```yaml
apiVersion: apps/v1

kind: Deployment
```

Invalid manifests are rejected before reaching the cluster.

---

# Step 5 – Admission Controllers

Admission Controllers may:

- Apply defaults
- Validate policies
- Mutate objects
- Reject requests

Example workflow:

```
Deployment

↓

Policy Check

↓

Approved

↓

Stored
```

Examples include namespace lifecycle management, image policy enforcement, and resource validation.

---

# Step 6 – Store in etcd

Validated objects are stored.

```
API Server

↓

etcd
```

etcd becomes the authoritative source of truth.

Stored objects include:

- Pods
- Deployments
- Services
- ConfigMaps
- Secrets
- Nodes

---

# Step 7 – Controller Manager

Controllers constantly monitor Kubernetes objects.

Example:

```
Deployment

↓

Desired Replicas = 3

↓

Current = 0

↓

Create ReplicaSet
```

Controllers do not directly run containers.

They create or update Kubernetes objects.

---

# Step 8 – ReplicaSet Controller

ReplicaSet ensures:

```
Desired

↓

3 Pods

↓

Current

↓

0 Pods

↓

Create 3 Pods
```

Pods initially remain:

```
Pending
```

because no node has been assigned yet.

---

# Step 9 – Scheduler

Scheduler evaluates available nodes.

Decision factors include:

- CPU availability
- Memory availability
- Resource requests
- Taints and tolerations
- Node affinity
- Pod affinity
- Scheduling policies

Workflow:

```
Pending Pod

↓

Evaluate Nodes

↓

Best Node Selected
```

---

# Step 10 – kubelet

The kubelet running on the selected worker node receives the assignment.

Workflow:

```
API Server

↓

kubelet

↓

Container Runtime

↓

Start Pod
```

The kubelet continuously reports node and Pod status back to the Control Plane.

---

# Step 11 – Container Runtime

The runtime performs:

```
Pull Image

↓

Create Container

↓

Start Container
```

If the image already exists locally:

```
Use Local Image
```

Otherwise:

```
Pull From Registry
```

---

# Step 12 – Pod Initialization

Before the application begins serving traffic:

```
Pod Created

↓

Containers Start

↓

Initialization

↓

Readiness Check

↓

Ready
```

Only after the Pod is ready will it receive traffic through a Service (if configured).

---

# Step 13 – Status Updates

The kubelet continuously reports:

- Pod status
- Container status
- Node health
- Resource usage

Workflow:

```
Worker Node

↓

API Server

↓

etcd Updated
```

---

# Continuous Reconciliation

Controllers never stop working.

```
Desired State

↓

Current State

↓

Difference?

↓

Correct Difference

↓

Desired State Restored
```

This loop runs throughout the lifetime of the cluster.

---

# Example – Pod Failure

Suppose one Pod crashes.

Current state:

```
Deployment

↓

3 Desired

↓

2 Running
```

Controller detects:

```
Missing Pod

↓

Create New Pod

↓

Scheduler

↓

Worker Node

↓

Running
```

No administrator intervention is required.

---

# Example – Node Failure

Worker Node:

```
Node A

↓

Offline
```

Result:

```
Pods Lost

↓

Node Controller Detects Failure

↓

Scheduler

↓

Healthy Nodes

↓

Replacement Pods
```

Provided sufficient cluster capacity exists, workloads are recreated on other nodes.

---

# Kubernetes Watches

Most Kubernetes components use **watch mechanisms** rather than continuously polling.

Example:

```
Deployment Updated

↓

API Server

↓

Notify Controllers

↓

Controllers React
```

This event-driven design improves scalability and efficiency.

---

# API-Centric Architecture

Every component communicates through the API Server.

```
kubectl

↓

API Server

↓

Scheduler

↓

Controller Manager

↓

kubelet

↓

Controllers
```

Direct communication between most components is intentionally minimized.

---

# Control Plane Responsibilities

```
Receive Requests

↓

Validate

↓

Store State

↓

Schedule Work

↓

Maintain Desired State

↓

Report Status
```

---

# Worker Node Responsibilities

```
Receive Pod Assignment

↓

Pull Images

↓

Start Containers

↓

Run Applications

↓

Report Health
```

---

# Complete Internal Workflow

```
Developer

↓

Git

↓

CI/CD

↓

Container Registry

↓

kubectl

↓

API Server

↓

Authentication

↓

Authorization

↓

Validation

↓

Admission Controllers

↓

etcd

↓

Controller Manager

↓

ReplicaSet

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

↓

Service

↓

User
```

This represents the complete lifecycle from deployment to a running application.

---

# Hands-on Commands

## View Cluster Information

```bash
kubectl cluster-info
```

---

## View Nodes

```bash
kubectl get nodes -o wide
```

---

## View All Pods

```bash
kubectl get pods -A
```

---

## View Deployments

```bash
kubectl get deployments -A
```

---

## View ReplicaSets

```bash
kubectl get replicasets -A
```

---

## View Services

```bash
kubectl get services -A
```

---

## Describe a Node

```bash
kubectl describe node <node-name>
```

Useful information includes:

- Capacity
- Allocatable resources
- Conditions
- Labels
- Taints

---

## Describe a Pod

```bash
kubectl describe pod <pod-name>
```

This provides details about:

- Events
- Scheduling
- Containers
- Volumes
- Conditions

---

## View Cluster Events

```bash
kubectl get events -A
```

Events are often the first place to investigate deployment or scheduling issues.

---

# Best Practices

### 1. Think in Desired State

Define what the system should look like rather than manually managing individual Pods.

---

### 2. Treat the API Server as the Central Entry Point

All cluster changes should flow through the Kubernetes API.

---

### 3. Avoid Modifying Running Pods

Update manifests and perform new deployments instead of manually changing live workloads.

---

### 4. Monitor Control Plane Health

A healthy Control Plane is essential for cluster stability.

---

### 5. Keep etcd Protected

Because etcd contains the cluster's state, secure access, perform backups, and monitor its health carefully.

---

