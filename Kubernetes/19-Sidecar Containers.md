# Chapter 19 – Sidecar Containers

## Overview

A **Sidecar Container** is a secondary container that runs **alongside the main application container inside the same Pod**.

Both containers:

- Share the same Pod
- Share the same network namespace
- Can share storage volumes
- Have independent container images
- Start as part of the same Pod lifecycle

A Sidecar extends or enhances the functionality of the main application **without modifying the application's code**.

Common uses include:

- Log collection
- Service mesh proxies
- Monitoring agents
- Security agents
- Configuration synchronization
- File synchronization
- Metrics exporters
- Authentication proxies

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Sidecar Container is
- Why Sidecar Containers are needed
- Sidecar Architecture
- Pod Lifecycle
- Shared Networking
- Shared Storage
- Communication Between Containers
- Sidecar Use Cases
- Native Sidecar Containers
- Best Practices

---

# Why Sidecar Containers?

Imagine a web application.

```
Web Application

↓

Generates Logs

↓

Need to Send Logs

↓

ElasticSearch
```

Option 1:

Modify application code.

Problems:

- More complexity
- More maintenance
- Application-specific implementation

---

# Better Solution

```
Application

↓

Writes Logs

↓

Shared Volume

↓

Sidecar

↓

ElasticSearch
```

The application remains unchanged.

---

# Another Example

Application needs:

```
TLS

↓

Authentication

↓

Metrics

↓

Logging

↓

Tracing
```

Embedding all these capabilities into the application increases complexity.

---

# Solution

```
Application

+

Sidecar

↓

Extra Features
```

---

# What is a Sidecar Container?

A Sidecar Container runs alongside the primary application container.

```
Pod

│

├── Application

└── Sidecar
```

Both containers work together.

---

# Pod Architecture

```
                 Pod

        ┌────────┴────────┐

        ▼                 ▼

 Application        Sidecar

        │                 │

        └──────┬──────────┘

               ▼

      Shared Network

      Shared Volumes
```

---

# Shared Network

Containers inside a Pod share:

- IP Address
- Network Namespace
- localhost

Example:

```
Application

↓

localhost:8080

↓

Sidecar
```

Containers communicate without external networking.

---

# Shared Storage

Containers can share volumes.

```
Application

↓

Shared Volume

↓

Sidecar
```

Example:

```
Application

↓

app.log

↓

Sidecar Reads

↓

ElasticSearch
```

---

# Lifecycle

Unlike Init Containers:

```
Sidecar

↓

Runs Continuously
```

Workflow:

```
Pod Starts

↓

Application Starts

↓

Sidecar Starts

↓

Both Run
```

When the Pod terminates:

```
Application Stops

↓

Sidecar Stops
```

---

# Sidecar vs Init Container

| Sidecar | Init Container |
|----------|----------------|
| Runs continuously | Runs once |
| Supports application | Initializes application |
| Active during Pod lifetime | Exits before app starts |
| Can serve traffic | Never serves application traffic |

---

# Sidecar vs Main Container

| Main Container | Sidecar |
|----------------|----------|
| Business logic | Supporting functionality |
| Handles client requests | Enhances application |
| Primary workload | Auxiliary workload |

---

# Communication

Containers communicate through:

```
localhost
```

Example:

```
Application

↓

localhost:9090

↓

Metrics Sidecar
```

No Service is required.

---

# Shared Process Example

```
Application

↓

Write File

↓

Shared Volume

↓

Sidecar Reads

↓

Upload
```

---

# Logging Sidecar

```
Application

↓

/logs/app.log

↓

Fluent Bit

↓

ElasticSearch
```

One of the most common Sidecar patterns.

---

# Monitoring Sidecar

```
Application

↓

Metrics

↓

Prometheus Exporter

↓

Prometheus
```

---

# Reverse Proxy Sidecar

```
Internet

↓

NGINX Sidecar

↓

Application
```

The Sidecar handles:

- TLS termination
- Authentication
- Routing
- Compression

---

# Service Mesh Sidecar

Example:

```
Istio Proxy

↓

Application
```

Traffic Flow:

```
Client

↓

Envoy

↓

Application
```

The application remains unaware of the proxy.

---

# Security Sidecar

```
Application

↓

Security Agent

↓

Threat Detection
```

---

# Backup Sidecar

```
Application

↓

Shared Volume

↓

Backup Sidecar

↓

Cloud Storage
```

---

# File Synchronization

```
Application

↓

Shared Files

↓

Sync Sidecar

↓

Remote Storage
```

---

# Metrics Exporter

```
Application

↓

Metrics

↓

Exporter

↓

Prometheus
```

---

# Sidecar YAML

Example:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: sidecar-demo

spec:

  containers:

  - name: app

    image: nginx

  - name: logger

    image: busybox
```

Notice:

```
Multiple Containers

↓

Same Pod
```

---

# Native Sidecar Containers

Modern Kubernetes introduces **native sidecar containers**, allowing specific containers to start during Pod initialization while remaining active for the lifetime of the Pod.

Benefits include:

- Better startup ordering
- Improved lifecycle management
- Clearer semantics for long-running supporting containers

> Availability depends on the Kubernetes version and feature gate configuration.

---

# Common Sidecar Use Cases

## Log Shipping

```
Application

↓

Fluent Bit
```

---

## Metrics

```
Application

↓

Exporter
```

---

## Proxy

```
NGINX

↓

Application
```

---

## Service Mesh

```
Envoy

↓

Application
```

---

## Secrets Sync

```
Vault Agent

↓

Application
```

---

## Backup

```
Application

↓

Backup Sidecar
```

---

# Viewing Containers

Describe Pod:

```bash
kubectl describe pod sidecar-demo
```

Observe:

```
Containers:

app

logger
```

---

# Logs

Application:

```bash
kubectl logs sidecar-demo \
-c app
```

Sidecar:

```bash
kubectl logs sidecar-demo \
-c logger
```

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
kubectl describe pod sidecar-demo
```

Logs:

```bash
kubectl logs sidecar-demo \
-c logger
```

Delete:

```bash
kubectl delete pod sidecar-demo
```

---

# Sidecar Architecture Summary

```
Pod

↓

Application

+

Sidecar

↓

Shared Network

↓

Shared Storage
```

---

# Best Practices

### 1. Keep Sidecars Focused

One Sidecar should perform one supporting responsibility.

---

### 2. Use Shared Volumes

Exchange files using Kubernetes volumes instead of external storage when appropriate.

---

### 3. Monitor Resource Usage

Sidecars consume CPU and memory independently.

Configure appropriate resource requests and limits.

---

### 4. Avoid Business Logic

Business functionality belongs in the main application container.

---

### 5. Use Sidecars for Cross-Cutting Concerns

Examples:

- Logging
- Monitoring
- Security
- Networking
- Configuration

---

# How Sidecar Containers Work Internally

## Overview

A Sidecar Container is **not a special Kubernetes resource**.

From Kubernetes' perspective, a Sidecar is simply another container defined in the Pod specification. The "sidecar" behavior comes from **how it is designed and used**, not from a separate API object (except for the newer Native Sidecar feature introduced in recent Kubernetes versions).

Internally, Kubernetes treats Sidecars as regular containers that:

- Share the Pod lifecycle
- Share networking
- Share storage volumes
- Are managed by the same kubelet
- Are scheduled together with the application container

This tight integration allows Sidecars to extend application functionality without modifying application code.

---

# High-Level Architecture

```
                      Pod

                        │

        ┌───────────────┼────────────────┐

        ▼                                ▼

  Application Container          Sidecar Container

        │                                │

        ├──────── Shared Network ────────┤

        ├──────── Shared Volumes ────────┤

        └──────── Shared IPC (Optional) ─┘
```

Both containers run inside the same Pod.

---

# Complete Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Store Pod

↓

Scheduler

↓

Choose Node

↓

kubelet

↓

Pull Images

↓

Create Containers

↓

Start Containers

↓

Pod Running
```

---

# Step 1 – Pod Creation

Example:

```yaml
containers:

- name: app

- name: logger
```

The Pod specification contains multiple containers.

---

# Step 2 – API Server

The API Server:

- Authenticates request
- Validates Pod
- Stores Pod in etcd

```
kubectl

↓

API Server

↓

Pod Stored
```

---

# Step 3 – Scheduler

Unlike Deployments or DaemonSets:

The Scheduler selects **one Node** for the **entire Pod**.

```
Pod

↓

Scheduler

↓

Node Selected
```

Both containers are always scheduled together.

---

# Step 4 – kubelet

The kubelet receives:

```
Pod

↓

Application Container

+

Sidecar Container
```

It prepares:

- Networking
- Volumes
- Container runtime

---

# Step 5 – Image Pull

Example:

```
Application Image

↓

Pulled
```

```
Sidecar Image

↓

Pulled
```

Both images must be available before startup.

---

# Step 6 – Container Startup

After preparation:

```
Application

↓

Running
```

```
Sidecar

↓

Running
```

Both containers become part of the same Pod.

---

# Pod Networking

Every Pod receives:

```
One IP Address
```

Example:

```
Pod

↓

10.244.2.15
```

Application:

```
localhost:8080
```

Sidecar:

```
localhost:8080
```

Both containers communicate using the loopback interface.

---

# Shared Network Namespace

Inside a Pod:

```
Application

↓

127.0.0.1

↓

Sidecar
```

No Kubernetes Service is required for communication within the Pod.

---

# Shared Storage

Example:

```
emptyDir

↓

Mounted

↓

Application

↓

Sidecar
```

Both containers access the same files.

---

# Shared Volume Workflow

```
Application

↓

Write Log

↓

Shared Volume

↓

Sidecar Reads

↓

Upload
```

This is the most common Sidecar pattern.

---

# Logging Example

```
Application

↓

/logs/app.log

↓

Fluent Bit

↓

ElasticSearch
```

Application code never changes.

---

# Monitoring Example

```
Application

↓

Metrics

↓

Exporter Sidecar

↓

Prometheus
```

---

# Reverse Proxy Example

```
Client

↓

NGINX Sidecar

↓

Application
```

The proxy handles:

- TLS
- Compression
- Authentication
- Routing

---

# Service Mesh Example

```
Client

↓

Envoy Sidecar

↓

Application
```

Traffic Flow:

```
Inbound

↓

Envoy

↓

Application

↓

Envoy

↓

Outbound
```

This enables:

- mTLS
- Traffic shaping
- Retries
- Circuit breaking
- Observability

without changing the application.

---

# Secret Synchronization

```
Vault

↓

Vault Agent Sidecar

↓

Shared Volume

↓

Application
```

The application reads secrets from files instead of calling Vault directly.

---

# Configuration Synchronization

```
Git Repository

↓

Config Sync Sidecar

↓

Shared Volume

↓

Application
```

Configuration updates become available without rebuilding the application image.

---

# Backup Example

```
Application

↓

Shared Data

↓

Backup Sidecar

↓

Object Storage
```

---

# Crash Scenario

Suppose:

```
Application

↓

Crash
```

Pod status:

```
Not Ready
```

Depending on the Pod's restart policy, Kubernetes may restart the failed container.

The Sidecar generally continues running unless the Pod itself is terminated.

---

# Sidecar Crash

Suppose:

```
Logger Sidecar

↓

Crash
```

Container:

```
Restart
```

according to the Pod's restart policy.

The application container may continue running, but the Pod's readiness and overall behavior depend on configuration.

---

# Pod Termination

```
Pod Deleted

↓

SIGTERM

↓

Application Stops

↓

Sidecar Stops

↓

Pod Removed
```

All containers terminate together.

---

# Resource Allocation

Each container has independent resources.

Example:

```
Application

↓

500m CPU

↓

512Mi Memory
```

```
Sidecar

↓

100m CPU

↓

128Mi Memory
```

The Pod's scheduling requirements consider the combined resource requests of all containers.

---

# Internal Architecture

```
API Server

↓

Scheduler

↓

kubelet

↓

Pod

↓

Application

+

Sidecar

↓

Shared Resources
```

---

# Native Sidecars

Modern Kubernetes introduces **Native Sidecar Containers**.

Benefits:

- Improved startup ordering
- Better lifecycle control
- More predictable initialization behavior
- Enhanced interaction with Init Containers

Unlike traditional sidecars, native sidecars can be started during Pod initialization while continuing to run after startup.

---

# Hands-on Lab 1 – Basic Sidecar

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: sidecar-demo

spec:

  containers:

  - name: app

    image: nginx

  - name: logger

    image: busybox

    command:

    - sh

    - -c

    - while true; do echo "Logging"; sleep 5; done
```

Deploy:

```bash
kubectl apply -f sidecar.yaml
```

---

# Hands-on Lab 2 – View Containers

```bash
kubectl describe pod sidecar-demo
```

Observe:

```
Containers

↓

app

logger
```

---

# Hands-on Lab 3 – View Logs

Application:

```bash
kubectl logs sidecar-demo \
-c app
```

Sidecar:

```bash
kubectl logs sidecar-demo \
-c logger
```

---

# Hands-on Lab 4 – Shared Volume

Create:

```yaml
emptyDir: {}
```

Application:

```
Writes File
```

Sidecar:

```
Reads File
```

Verify shared data access.

---

# Hands-on Lab 5 – Test Localhost Communication

Application:

```
Port 8080
```

Sidecar:

```bash
wget localhost:8080
```

Verify that containers communicate over `localhost`.

---

# Common Mistakes

## 1. Putting Business Logic in the Sidecar

Incorrect:

```
Sidecar

↓

Business Application
```

Correct:

```
Application

↓

Business Logic
```

The Sidecar should provide supporting functionality.

---

## 2. Ignoring Resource Usage

Each Sidecar consumes:

- CPU
- Memory
- Storage
- Network

Configure resource requests and limits appropriately.

---

## 3. Assuming Separate Networking

Incorrect:

```
Application

↓

Different IP
```

Correct:

```
Same Pod

↓

Same IP

↓

localhost
```

---

## 4. Forgetting Shared Volumes

Without a shared volume:

```
Application

↓

Writes File

↓

Sidecar

↓

Cannot Read
```

Use shared volumes for file-based communication.

---

## 5. Overloading a Single Sidecar

Avoid one Sidecar handling:

- Logging
- Metrics
- Backup
- Security
- Proxy

Prefer focused, single-responsibility containers when practical.

---

# Sidecar Containers Quick Revision

## Architecture

```
Pod

↓

Application

+

Sidecar

↓

Shared Network

↓

Shared Volumes
```

---

## Workflow

```
Create Pod

↓

Scheduler

↓

kubelet

↓

Application

↓

Sidecar

↓

Running Together
```

---

## Communication

```
localhost

↓

Shared Volumes
```

---

# Essential kubectl Commands

View Pods:

```bash
kubectl get pods
```

Describe:

```bash
kubectl describe pod sidecar-demo
```

Application Logs:

```bash
kubectl logs sidecar-demo -c app
```

Sidecar Logs:

```bash
kubectl logs sidecar-demo -c logger
```

Delete:

```bash
kubectl delete pod sidecar-demo
```

---

# Interview Questions

### Basic

- What is a Sidecar Container?
- Why are Sidecar Containers useful?
- How does a Sidecar differ from an Init Container?

---

### Intermediate

- How do Sidecars communicate with application containers?
- What resources are shared within a Pod?
- What are common Sidecar use cases?

---

### Advanced

- Explain how Kubernetes manages Sidecar Containers internally.
- Why are Sidecars widely used in service meshes?
- How do Native Sidecars differ from traditional Sidecars?
- What happens if a Sidecar crashes?
- How do shared volumes enable cooperation between containers?

---

# References

## Official Kubernetes Documentation

- Sidecar Containers
- Multi-Container Pods
- Native Sidecars
- Pod Lifecycle
- Volumes

---

## CNCF Resources

- Kubernetes Best Practices
- Pod Design Patterns
- Service Mesh Architecture
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- Istio Documentation
- Envoy Proxy Documentation
- CIS Kubernetes Benchmark
- NIST SP 800-190

---

## Recommended Practice

1. Create a Pod with an application container and a logging Sidecar.
2. Share log files using an `emptyDir` volume.
3. Test communication over `localhost`.
4. Deploy a metrics exporter as a Sidecar.
5. Explore a service mesh (such as Istio) to observe Envoy Sidecars.
6. Compare traditional Sidecars with Native Sidecars in a recent Kubernetes release.
7. Monitor CPU and memory consumption of both containers within the same Pod.

---

# Chapter Summary

```
Developer

↓

Pod

↓

API Server

↓

Scheduler

↓

kubelet

↓

Application Container

+

Sidecar Container

↓

Shared Network

↓

Shared Storage

↓

Supporting Services
```

Sidecar Containers are one of Kubernetes' most powerful design patterns. By colocating **supporting services** with the main application inside the same Pod, they enable capabilities such as **logging, monitoring, security, service mesh integration, configuration synchronization, and backups** without requiring changes to application code.

---