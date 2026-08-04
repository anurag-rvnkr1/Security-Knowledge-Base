# Chapter 1 – Introduction to Kubernetes

## Overview

Kubernetes (often abbreviated as **K8s**) is an open-source container orchestration platform that automates the deployment, scaling, management, networking, and lifecycle of containerized applications.

Originally developed by Google based on over a decade of experience running large-scale production workloads, Kubernetes is now maintained by the **Cloud Native Computing Foundation (CNCF)** and has become the industry standard for container orchestration.

Kubernetes enables organizations to manage applications consistently across:

- On-Premises Data Centers
- Public Cloud
- Private Cloud
- Hybrid Cloud
- Multi-Cloud Environments

It provides automation for tasks that would otherwise require significant manual effort.

---

# Why Kubernetes Was Created

Before Kubernetes, organizations often managed containers manually.

Example:

```
Server 1

↓

Docker Container

↓

Application
```

As applications grew:

```
Server 1

↓

10 Containers


Server 2

↓

15 Containers


Server 3

↓

20 Containers
```

Managing hundreds or thousands of containers manually became increasingly difficult.

Common challenges included:

- Scaling applications
- Load balancing
- Service discovery
- High availability
- Self-healing
- Rolling updates
- Resource scheduling

Kubernetes was designed to solve these operational challenges.

---

# What is Container Orchestration?

Container orchestration is the automated management of containerized applications.

It includes:

- Deployment
- Scheduling
- Scaling
- Networking
- Load Balancing
- Health Monitoring
- Self-Healing
- Rolling Updates
- Rollbacks
- Resource Management

Instead of manually managing containers, Kubernetes continuously maintains the desired state of the system.

---

# Why "K8s"?

The word:

```
Kubernetes
```

contains:

```
K

8 Letters

s
```

Hence:

```
K8s
```

---

# Evolution of Application Deployment

## Traditional Deployment

```
Physical Server

↓

Application
```

Problems:

- Resource wastage
- Poor scalability
- Difficult maintenance

---

## Virtual Machines

```
Physical Server

↓

Hypervisor

↓

VM

↓

Operating System

↓

Application
```

Benefits:

- Better isolation
- Multiple workloads
- Improved utilization

Challenges:

- Higher resource usage
- Slower startup
- Full guest operating systems

---

## Containers

```
Host OS

↓

Container Runtime

↓

Containers
```

Benefits:

- Lightweight
- Fast startup
- Efficient resource utilization

Challenge:

Managing large numbers of containers.

---

## Kubernetes

```
Cluster

↓

Nodes

↓

Pods

↓

Applications
```

Benefits:

- Automated deployment
- Self-healing
- Scaling
- High availability
- Efficient resource management

---

# Why Organizations Use Kubernetes

Major organizations adopt Kubernetes because it provides:

- High Availability
- Automatic Scaling
- Self-Healing
- Rolling Updates
- Rollbacks
- Service Discovery
- Load Balancing
- Infrastructure Portability
- Resource Optimization
- Vendor Neutrality

---

# Real-World Example

Imagine an e-commerce platform.

Architecture:

```
Internet

↓

Load Balancer

↓

Frontend Pods

↓

Backend Pods

↓

Database
```

During a sale:

```
100 Users

↓

2 Pods


10,000 Users

↓

20 Pods
```

Kubernetes can automatically increase the number of application instances (Pods) based on demand when configured with autoscaling.

After traffic decreases:

```
20 Pods

↓

4 Pods
```

Resources are used more efficiently.

---

# Kubernetes Goals

Kubernetes is designed to:

- Automate deployments
- Maintain desired state
- Scale applications
- Improve availability
- Optimize resource usage
- Simplify operations
- Support cloud-native architectures

---

# Key Features

## Automated Deployment

Deploy applications using declarative YAML manifests.

---

## Self-Healing

If a Pod fails:

```
Pod Crash

↓

Kubernetes Detects Failure

↓

Creates Replacement Pod
```

Applications recover automatically without manual intervention.

---

## Horizontal Scaling

```
2 Pods

↓

5 Pods

↓

20 Pods
```

Scaling can be:

- Manual
- Automatic (using autoscaling)

---

## Rolling Updates

Instead of replacing every application instance simultaneously:

```
Version 1

↓

Version 2

↓

One Pod at a Time
```

This minimizes downtime.

---

## Rollback

If deployment fails:

```
Version 2

↓

Issue Detected

↓

Rollback

↓

Version 1
```

Applications can return to a previously working version.

---

## Service Discovery

Applications communicate using stable service names instead of changing IP addresses.

---

## Load Balancing

Traffic is distributed across multiple Pods.

```
Incoming Traffic

↓

Service

↓

Pod A

Pod B

Pod C
```

---

## Resource Scheduling

Kubernetes determines where Pods should run based on available cluster resources and scheduling policies.

---

# Kubernetes Architecture (High-Level)

```
                Kubernetes Cluster

          ┌───────────────────────────┐

          │      Control Plane         │

          └───────────────────────────┘

                    │

     ┌──────────────┼──────────────┐

     ▼              ▼              ▼

 Worker Node   Worker Node   Worker Node

     │              │              │

    Pods           Pods           Pods
```

A deeper exploration of the architecture is covered in the next chapter.

---

# Kubernetes Components (Preview)

Control Plane:

- API Server
- Scheduler
- Controller Manager
- etcd

Worker Nodes:

- kubelet
- kube-proxy
- Container Runtime
- Pods

Each component has a specific responsibility for maintaining the cluster.

---

# Kubernetes Objects

Common Kubernetes objects include:

- Pods
- Deployments
- ReplicaSets
- Services
- ConfigMaps
- Secrets
- Namespaces
- Jobs
- StatefulSets
- DaemonSets

These objects define the desired state of applications and infrastructure.

---

# Kubernetes Ecosystem

```
Application

↓

Container

↓

Docker / containerd

↓

Kubernetes

↓

Cloud Infrastructure
```

Supporting tools often include:

- Helm
- Prometheus
- Grafana
- Argo CD
- Istio
- Falco

---

# Benefits

Organizations adopting Kubernetes commonly achieve:

- Faster deployments
- Improved reliability
- Better scalability
- Higher resource utilization
- Easier application management
- Consistent environments
- Improved disaster recovery
- Cloud portability

---

# Common Use Cases

Kubernetes is widely used for:

- Microservices
- APIs
- Web Applications
- Machine Learning Workloads
- Data Processing
- CI/CD Platforms
- Edge Computing
- Batch Processing
- AI Services

---

# Important Terminology

| Term | Description |
|------|-------------|
| Cluster | A group of machines managed by Kubernetes |
| Node | A worker or control plane machine in the cluster |
| Pod | The smallest deployable Kubernetes unit |
| Deployment | Manages stateless application Pods |
| Service | Provides stable network access to Pods |
| Namespace | Logical isolation within a cluster |
| kubectl | Command-line tool for Kubernetes |

---

# Kubernetes Workflow

```
Developer

↓

YAML Manifest

↓

kubectl

↓

API Server

↓

Scheduler

↓

Worker Node

↓

Pod Running
```

Kubernetes continuously monitors the cluster to ensure the running state matches the declared desired state.

---

# Key Principles

## Declarative Configuration

Describe the desired state instead of issuing imperative step-by-step instructions.

---

## Desired State

Kubernetes continuously works to maintain the state defined in configuration.

---

## Self-Healing

Failed Pods are replaced automatically.

---

## Automation

Routine operational tasks are automated to reduce manual effort.

---

## Scalability

Applications can grow or shrink based on workload demands.

---

## Portability

Applications can run across different infrastructure providers with minimal changes.

---

## How Kubernetes Works

Kubernetes operates using a **declarative model**. Instead of telling Kubernetes **how** to perform every action, you declare **what** the desired state of the application should be. Kubernetes continuously compares the **desired state** with the **current state** and automatically performs the actions required to make them match.

This is one of the biggest differences between Kubernetes and traditional infrastructure management.

---

# Desired State vs Current State

Suppose you want your application to always have **3 running Pods**.

Desired State

```
Application

↓

3 Pods
```

Current State

```
Application

↓

2 Pods
```

Kubernetes detects the difference.

```
Desired State

↓

3 Pods

↓

Current State

↓

2 Pods

↓

Create 1 New Pod
```

The cluster automatically returns to the desired state.

---

# Kubernetes Control Loop

Kubernetes continuously runs reconciliation loops.

```
Desired State

↓

Observe Current State

↓

Compare

↓

Difference Found?

↓

Yes

↓

Take Action

↓

Current State Updated
```

This process runs continuously throughout the lifetime of the cluster.

---

# High-Level Kubernetes Workflow

```
Developer

↓

Write YAML

↓

kubectl apply

↓

API Server

↓

Store Configuration (etcd)

↓

Scheduler

↓

Worker Node

↓

Pod Created

↓

Application Running
```

Every deployment follows this general workflow.

---

# Step 1 – Developer Creates a Manifest

Example:

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:
  name: nginx

spec:
  replicas: 3
```

This file describes the desired state.

---

# Step 2 – kubectl Sends Request

Command:

```bash
kubectl apply -f deployment.yaml
```

The request is sent to the Kubernetes API Server.

```
kubectl

↓

API Server
```

The API Server is the entry point for all cluster operations.

---

# Step 3 – API Server Validates Request

The API Server performs checks such as:

- Authentication
- Authorization
- Schema validation
- Admission control

If valid:

```
Request

↓

Validated

↓

Stored
```

---

# Step 4 – Desired State Stored in etcd

```
API Server

↓

etcd
```

etcd stores:

- Cluster configuration
- Object definitions
- Cluster state

It acts as Kubernetes' distributed key-value database.

---

# Step 5 – Scheduler Selects a Node

The Scheduler determines:

```
Available Nodes

↓

CPU

↓

Memory

↓

Policies

↓

Best Node
```

It decides **where** the Pod should run.

---

# Step 6 – kubelet Starts the Pod

The selected worker node receives instructions.

```
Worker Node

↓

kubelet

↓

Container Runtime

↓

Create Pod
```

The kubelet communicates with the container runtime to start the workload.

---

# Step 7 – Pod Becomes Running

```
Pod

↓

Container Started

↓

Application Ready
```

If readiness probes are configured, traffic is sent only after the Pod reports it is ready.

---

# Step 8 – Continuous Monitoring

Kubernetes never stops monitoring.

```
Pod Running

↓

Health Check

↓

Still Healthy?

↓

Yes

↓

Continue
```

---

# Self-Healing Example

Suppose one Pod crashes.

```
3 Pods

↓

1 Pod Crash

↓

Only 2 Pods Running
```

Kubernetes notices the difference.

```
Desired

↓

3 Pods

↓

Current

↓

2 Pods

↓

Create New Pod
```

The application returns to its desired state automatically.

---

# Scaling Example

Current state:

```
3 Pods
```

Administrator updates:

```yaml
replicas: 6
```

Workflow:

```
Deployment Updated

↓

Scheduler

↓

3 Additional Pods

↓

6 Running Pods
```

Scaling is handled automatically by Kubernetes.

---

# Rolling Update Example

Current version:

```
v1

↓

Pod 1

Pod 2

Pod 3
```

Deploy version 2.

```
Replace Pod 1

↓

Healthy?

↓

Yes

↓

Replace Pod 2

↓

Healthy?

↓

Yes

↓

Replace Pod 3
```

This minimizes downtime and risk during deployments.

---

# Rollback Example

Deployment:

```
Version 2

↓

Application Errors
```

Rollback:

```bash
kubectl rollout undo deployment nginx
```

Workflow:

```
Rollback

↓

Restore Previous ReplicaSet

↓

Application Healthy
```

---

# Service Discovery

Pods receive dynamic IP addresses.

Instead of connecting directly to Pods:

```
Application

↓

Service

↓

Pods
```

Applications communicate through Services, which provide stable endpoints.

---

# Load Balancing

```
Incoming Request

↓

Service

↓

Pod A

Pod B

Pod C
```

The Service distributes traffic among healthy Pods.

---

# Automatic Recovery

Suppose a worker node fails.

```
Worker Node

↓

Unavailable
```

If the cluster has additional capacity:

```
Pods Lost

↓

Scheduler

↓

Healthy Node

↓

New Pods
```

Kubernetes recreates workloads on other available nodes.

---

# Kubernetes Reconciliation

Everything in Kubernetes revolves around reconciliation.

```
Desired State

↓

Controller

↓

Current State

↓

Match?

↓

No

↓

Correct State
```

Controllers continuously work to maintain the declared configuration.

---

# Real-World Deployment Workflow

```
Developer

↓

Git Repository

↓

CI/CD Pipeline

↓

Docker Image

↓

Container Registry

↓

kubectl

↓

API Server

↓

Scheduler

↓

Worker Nodes

↓

Pods

↓

Users
```

Modern organizations typically integrate Kubernetes with automated delivery pipelines.

---

# Hands-on Commands

## Check Cluster Information

```bash
kubectl cluster-info
```

---

## View Nodes

```bash
kubectl get nodes
```

---

## View Pods

```bash
kubectl get pods
```

---

## View Deployments

```bash
kubectl get deployments
```

---

## View Services

```bash
kubectl get services
```

---

## Apply Configuration

```bash
kubectl apply -f deployment.yaml
```

---

## Delete Resources

```bash
kubectl delete -f deployment.yaml
```

---

## Describe Resource

```bash
kubectl describe pod pod-name
```

Provides detailed information about the selected resource.

---

## View Logs

```bash
kubectl logs pod-name
```

Displays application output from the Pod.

---

# Best Practices

### 1. Use Declarative Configuration

Store manifests in version control and apply them consistently.

---

### 2. Treat Infrastructure as Code

Manage Kubernetes manifests alongside application code where appropriate.

---

### 3. Keep Deployments Immutable

Update images and redeploy rather than modifying running Pods.

---

### 4. Configure Health Checks

Use readiness and liveness probes to improve reliability.

---

### 5. Monitor Continuously

Track:

- CPU
- Memory
- Pod status
- Events
- Logs
- Application metrics

---

### 6. Automate Deployments

Use CI/CD pipelines to improve consistency and reduce manual errors.

---

### 7. Document Cluster Architecture

Maintain diagrams, manifests, runbooks, and recovery procedures.

---

