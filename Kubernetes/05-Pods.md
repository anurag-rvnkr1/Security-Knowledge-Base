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

## How Pods Work Internally

Although a Pod appears to be a simple Kubernetes object, several Kubernetes components work together behind the scenes to create, monitor, and maintain it.

Understanding this internal workflow is essential for troubleshooting, performance optimization, and production operations.

---

# Pod Creation Workflow

Suppose a user creates a Pod.

Command:

```bash
kubectl apply -f pod.yaml
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

Every Pod follows this lifecycle.

---

# Step 1 – User Creates a Pod

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

Deploy:

```bash
kubectl apply -f pod.yaml
```

---

# Step 2 – API Server Receives Request

Workflow:

```
kubectl

↓

API Server
```

The API Server:

- Authenticates the user
- Checks permissions
- Validates the manifest
- Stores the Pod definition

---

# Step 3 – Pod Stored in etcd

```
API Server

↓

etcd
```

At this point:

```
Pod Exists

↓

Not Yet Running
```

The Pod has not yet been assigned to a worker node.

---

# Step 4 – Scheduler Detects Pending Pod

Initially:

```
Pod

↓

Pending
```

Scheduler evaluates:

- Available nodes
- CPU availability
- Memory availability
- Resource requests
- Scheduling rules
- Taints and tolerations
- Affinity rules

---

# Step 5 – Scheduler Selects Worker Node

Example:

```
Node A

CPU Busy

Memory Busy

↓

Node B

Enough Resources

↓

Selected
```

The Scheduler writes the selected node assignment back to the API Server.

---

# Step 6 – kubelet Receives Assignment

Worker Node:

```
API Server

↓

kubelet
```

The kubelet observes that a new Pod has been assigned to its node.

Responsibilities include:

- Creating the Pod
- Monitoring containers
- Reporting status
- Restarting containers when appropriate

---

# Step 7 – Image Pull

The kubelet asks the container runtime to pull the image if it is not already available locally.

Workflow:

```
Container Runtime

↓

Registry

↓

Download Image
```

Example registry:

```
Docker Hub
```

If the image already exists locally:

```
Use Local Image
```

---

# Step 8 – Container Creation

The container runtime creates:

```
Pod Sandbox

↓

Container

↓

Application
```

The **Pod Sandbox** provides the shared environment for all containers within the Pod, including networking.

---

# Step 9 – Networking

Each Pod receives:

```
Unique Pod IP
```

Example:

```
Pod

↓

10.244.0.5
```

All containers inside the Pod share:

- Network namespace
- IP address
- Port space

Containers communicate with each other using:

```
localhost
```

---

# Step 10 – Storage

If volumes are defined:

```
Volume

↓

Mounted

↓

Containers
```

Every container in the Pod can access the mounted volume according to its configuration.

---

# Step 11 – Container Startup

The runtime executes:

```
ENTRYPOINT

↓

CMD

↓

Application Starts
```

If startup succeeds:

```
Running
```

Otherwise:

```
Crash

↓

Restart (depending on restart policy)
```

---

# Step 12 – kubelet Monitoring

The kubelet continuously monitors:

- Container health
- Restart status
- Resource usage
- Probe results
- Pod lifecycle

Status updates are sent back to the API Server.

---

# Pod Networking Internals

Inside a Pod:

```
Pod

├── Container A

├── Container B

└── Shared IP
```

Example:

```
Container A

↓

localhost:8080

↓

Container B
```

Containers do **not** require separate Services to communicate within the same Pod.

---

# Pod Storage Internals

Example:

```
Volume

↓

/data

↓

Container A

↓

Container B
```

Shared storage enables containers to exchange files and data.

---

# Pod Scheduling Lifecycle

```
Pod Created

↓

Pending

↓

Scheduler

↓

Worker Node

↓

kubelet

↓

Image Pulled

↓

Container Started

↓

Running
```

---

# Pod Deletion

Command:

```bash
kubectl delete pod nginx
```

Workflow:

```
Delete Request

↓

API Server

↓

kubelet

↓

Graceful Shutdown

↓

Container Stops

↓

Resources Released

↓

Pod Removed
```

If the Pod is managed by a controller:

```
Deployment

↓

New Pod Created
```

---

# Pod Restart

Suppose the application crashes.

```
Application

↓

Crash

↓

kubelet

↓

Restart Container
```

The behavior depends on the configured restart policy and the managing controller.

---

# Pod Lifecycle Diagram

```
Pending

↓

Container Creating

↓

Running

↓

Succeeded

or

Failed

↓

Deleted
```

---

# Pod Conditions

Common Pod conditions include:

- PodScheduled
- Initialized
- ContainersReady
- Ready

View:

```bash
kubectl describe pod nginx
```

These conditions help explain where a Pod is in its lifecycle.

---

# Hands-on Exercise

## Create a Pod

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

Deploy:

```bash
kubectl apply -f pod.yaml
```

---

## Verify

```bash
kubectl get pods
```

---

## Inspect

```bash
kubectl describe pod nginx
```

---

## View Logs

```bash
kubectl logs nginx
```

---

## Execute a Command

```bash
kubectl exec -it nginx -- /bin/sh
```

If `/bin/sh` is unavailable in the image, use the appropriate shell provided by the container.

---

## Delete

```bash
kubectl delete pod nginx
```

---

# Useful kubectl Commands

View Pods:

```bash
kubectl get pods
```

Wide output:

```bash
kubectl get pods -o wide
```

Describe:

```bash
kubectl describe pod nginx
```

Logs:

```bash
kubectl logs nginx
```

YAML:

```bash
kubectl get pod nginx -o yaml
```

JSON:

```bash
kubectl get pod nginx -o json
```

Watch:

```bash
kubectl get pods -w
```

---

# Best Practices

### 1. Let Controllers Manage Long-Running Pods

Create Deployments instead of standalone Pods for production workloads.

---

### 2. Keep Images Small

Smaller images generally reduce image pull time and improve deployment speed.

---

### 3. Define Resource Requests and Limits

This improves scheduling decisions and cluster stability.

---

### 4. Configure Health Probes

Use readiness, liveness, and startup probes where appropriate to improve reliability.

---

### 5. Observe Before Acting

When troubleshooting, inspect:

1. `kubectl get pods`
2. `kubectl describe pod`
3. `kubectl logs`
4. `kubectl get events`

before making changes.

---

# Multi-Container Pods

## Overview

Although most Kubernetes Pods contain a **single container**, Kubernetes allows a Pod to run **multiple containers** that work together as a single unit.

Containers inside the same Pod:

- Share the same network namespace
- Share the same IP address
- Share the same storage volumes (when configured)
- Are scheduled together
- Have the same lifecycle

A multi-container Pod is useful when containers have a **strong dependency** on each other and need to cooperate closely.

---

# Single vs Multi-Container Pods

## Single-Container Pod

```
Pod

┌──────────────────┐

│                  │

│   NGINX          │

│                  │

└──────────────────┘
```

Most production applications follow this pattern.

---

## Multi-Container Pod

```
Pod

┌─────────────────────────────┐

│                             │

│  Web Server                 │

│                             │

│  Log Collector              │

│                             │

│  Shared Network             │

│                             │

│  Shared Volume              │

└─────────────────────────────┘
```

Both containers cooperate to perform one logical task.

---

# Why Use Multiple Containers?

Typical reasons include:

- Log collection
- Monitoring
- Proxying traffic
- Configuration generation
- Data synchronization
- Service mesh sidecars
- Supporting utilities

---

# Shared Network

Every container shares:

```
Pod

↓

One IP Address
```

Example:

```
Container A

↓

localhost:8080

↓

Container B
```

Communication occurs over `localhost` because all containers share the same network namespace.

---

# Shared Storage

Containers may share volumes.

```
Volume

↓

Container A

↓

Container B
```

Example:

```
Application

↓

Writes Logs

↓

Shared Volume

↓

Log Collector

↓

Reads Logs
```

---

# Multi-Container Pod YAML

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:
  name: multi-container

spec:

  containers:

  - name: web

    image: nginx

  - name: logger

    image: busybox

    command:
    - sh
    - -c
    - while true; do sleep 3600; done
```

This Pod contains two containers.

---

# Viewing Containers

Display Pods:

```bash
kubectl get pods
```

Describe:

```bash
kubectl describe pod multi-container
```

The output lists both containers.

---

# Viewing Logs

Specify the container:

```bash
kubectl logs multi-container \
-c web
```

Another container:

```bash
kubectl logs multi-container \
-c logger
```

Without specifying `-c`, Kubernetes cannot determine which container's logs you want if there are multiple regular containers.

---

# Executing Commands

Example:

```bash
kubectl exec -it multi-container \
-c web -- /bin/sh
```

Logger container:

```bash
kubectl exec -it multi-container \
-c logger -- /bin/sh
```

Always specify the container name when multiple containers are present.

---

# Container Startup

Containers within a Pod are generally started by Kubernetes as part of the Pod startup process, but applications should **not rely on a particular startup order** between regular containers.

If initialization must occur before application containers start, use **Init Containers**, which are covered later in this chapter.

---

# Multi-Container Communication

Example:

```
Web Container

↓

localhost

↓

Logging Container
```

or

```
Application

↓

localhost

↓

Proxy
```

No Kubernetes Service is required for communication within the same Pod.

---

# Common Multi-Container Patterns

---

## 1. Sidecar Pattern

A sidecar extends the functionality of the main application.

Example:

```
Pod

├── Application

└── Log Collector
```

Examples:

- Log forwarding
- Metrics collection
- Service mesh proxy
- Configuration reload helper

This is the most common multi-container pattern.

---

## 2. Ambassador Pattern

An ambassador container acts as a local proxy.

```
Application

↓

Ambassador

↓

External Service
```

Examples:

- Database proxy
- API gateway helper
- TLS proxy

---

## 3. Adapter Pattern

An adapter transforms application output.

```
Application

↓

Adapter

↓

Monitoring System
```

Example:

- Convert custom metrics into Prometheus-compatible metrics.

---

# Example Architecture

```
                 Pod

     ┌──────────────────────────────┐

     │                              │

     │  Application                 │

     │                              │

     │  Prometheus Exporter         │

     │                              │

     │  Shared Volume               │

     │                              │

     │  localhost Communication     │

     └──────────────────────────────┘
```

---

# Advantages

- Shared networking
- Shared storage
- Tight integration
- Simplified communication
- Unified deployment
- Single scheduling unit

---

# Disadvantages

- Containers cannot scale independently.
- Increased resource sharing complexity.
- Debugging may become more involved.
- A poorly designed Pod can become tightly coupled.

Use multiple containers only when they represent a single logical workload.

---

# Hands-on Exercise

## Create a Multi-Container Pod

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:
  name: demo

spec:

  containers:

  - name: web

    image: nginx

  - name: helper

    image: busybox

    command:
    - sh
    - -c
    - while true; do sleep 3600; done
```

Deploy:

```bash
kubectl apply -f pod.yaml
```

---

## Verify

```bash
kubectl get pods
```

---

## Describe

```bash
kubectl describe pod demo
```

---

## Logs

```bash
kubectl logs demo \
-c web
```

---

## Execute

```bash
kubectl exec -it demo \
-c helper -- /bin/sh
```

---

## Delete

```bash
kubectl delete pod demo
```

---

# Best Practices

### 1. Use Multiple Containers Only When Necessary

If containers can operate independently, deploy them in separate Pods.

---

### 2. Keep One Main Application Container

Supporting containers should complement—not replace—the primary application.

---

### 3. Use Shared Volumes Carefully

Only share data that must be accessed by multiple containers.

---

### 4. Prefer localhost Communication

Containers inside the same Pod should communicate over the shared network namespace.

---

### 5. Avoid Tight Coupling

If two containers require independent scaling, upgrades, or lifecycles, they likely belong in separate Pods.

---
