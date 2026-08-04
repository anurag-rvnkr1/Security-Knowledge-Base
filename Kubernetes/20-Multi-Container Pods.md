# Chapter 20 – Multi-Container Pods

## Overview

A **Multi-Container Pod** is a Kubernetes Pod that contains **two or more containers** working together to provide a single application or service.

Unlike separate Pods that communicate over the network, containers inside the same Pod:

- Share the same network namespace
- Share the same IP address
- Can communicate over `localhost`
- Can share storage volumes
- Are scheduled together
- Share the Pod lifecycle

The **Pod** is the smallest deployable unit in Kubernetes—not the individual container.

Multi-container Pods are commonly implemented using design patterns such as:

- Sidecar Pattern
- Ambassador Pattern
- Adapter Pattern

---

# Learning Objectives

After completing this chapter, you will understand:

- What Multi-Container Pods are
- Why they are needed
- Pod Architecture
- Shared Networking
- Shared Storage
- Container Communication
- Multi-Container Design Patterns
- Lifecycle Management
- Resource Management
- Best Practices

---

# Why Multi-Container Pods?

Imagine an application.

```
Application

↓

Needs Logging

↓

Needs Monitoring

↓

Needs Proxy

↓

Needs Metrics
```

One option:

```
Everything

↓

Inside One Container
```

Problems:

- Large image
- Hard to maintain
- Difficult upgrades
- Tight coupling

---

# Better Solution

Separate responsibilities.

```
Pod

├── Application

├── Logger

├── Metrics

└── Proxy
```

Each container has a single responsibility.

---

# What is a Multi-Container Pod?

A Pod can contain multiple containers.

```
Pod

│

├── App

├── Logger

├── Metrics

└── Proxy
```

Containers cooperate to deliver one logical application.

---

# Pod Architecture

```
                 Pod

     ┌───────────┼───────────┐

     ▼           ▼           ▼

 Application   Logger     Metrics

         \        │        /

          \       │       /

           └──── Shared ───┘

              Network

              Volumes
```

---

# Shared Network

Every container shares:

- Same IP address
- Same network namespace
- Same localhost interface

Example:

```
Application

↓

localhost:8080

↓

Logger
```

Communication is fast because it never leaves the Pod.

---

# Shared Storage

Containers can mount the same volume.

```
Application

↓

Shared Volume

↓

Logger
```

Example:

```
Application

↓

Writes Log

↓

Logger Reads

↓

ElasticSearch
```

---

# Pod Lifecycle

Containers are managed together.

```
Create Pod

↓

Start Containers

↓

Run Together

↓

Stop Together

↓

Delete Pod
```

---

# Container Independence

Although containers share the Pod:

- They have separate processes
- Separate filesystems (except shared volumes)
- Separate images
- Separate logs
- Separate resource limits

---

# Communication

Containers communicate using:

```
localhost
```

Example:

```
Application

↓

127.0.0.1:9090

↓

Metrics Container
```

No Service is required.

---

# Shared Volumes

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

Files written by one container are immediately available to the other.

---

# Common Design Patterns

```
Multi-Container Pods

│

├── Sidecar

├── Ambassador

└── Adapter
```

These patterns solve different architectural problems.

---

# 1. Sidecar Pattern

Purpose:

```
Support

↓

Main Application
```

Examples:

- Logging
- Monitoring
- Service Mesh
- Backup
- Configuration Sync

Architecture:

```
Application

↓

Sidecar

↓

Supporting Functionality
```

---

# 2. Ambassador Pattern

Purpose:

```
Proxy

↓

External Service
```

The Ambassador acts as a local proxy between the application and external resources.

Example:

```
Application

↓

Ambassador

↓

Database
```

Benefits:

- Simplified application configuration
- Transparent routing
- Easy endpoint changes

---

# 3. Adapter Pattern

Purpose:

```
Convert

↓

Application Output

↓

Expected Format
```

Example:

```
Application Logs

↓

Adapter

↓

Monitoring System
```

The Adapter transforms data without modifying the application.

---

# Multi-Container Workflow

```
Pod Created

↓

Containers Started

↓

Shared Network

↓

Shared Volumes

↓

Application Runs
```

---

# YAML Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: multi-container

spec:

  containers:

  - name: app

    image: nginx

  - name: logger

    image: busybox
```

Two containers.

One Pod.

---

# Container Communication

Application:

```
localhost:8080
```

Proxy:

```
localhost:8080
```

Metrics:

```
localhost:9090
```

Every container accesses services through the shared network namespace.

---

# Resource Allocation

Each container has independent:

- CPU requests
- CPU limits
- Memory requests
- Memory limits

Example:

```
Application

↓

500m CPU
```

```
Logger

↓

100m CPU
```

The scheduler considers the combined resource requests of all containers in the Pod.

---

# Restart Behavior

If:

```
Logger

↓

Crash
```

The container may restart according to the Pod's `restartPolicy`.

The Pod itself is not automatically recreated solely because one container restarts.

---

# Logging

View application logs:

```bash
kubectl logs pod-name \
-c app
```

View logger logs:

```bash
kubectl logs pod-name \
-c logger
```

Each container has separate log streams.

---

# Viewing Containers

```bash
kubectl describe pod multi-container
```

Observe:

```
Containers

↓

app

logger
```

---

# Common Use Cases

## Logging

```
Application

↓

Logger

↓

ElasticSearch
```

---

## Monitoring

```
Application

↓

Exporter

↓

Prometheus
```

---

## Security

```
Application

↓

Security Agent
```

---

## Reverse Proxy

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

## File Synchronization

```
Application

↓

Shared Volume

↓

Sync Container
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
kubectl describe pod multi-container
```

Application Logs:

```bash
kubectl logs pod-name -c app
```

Sidecar Logs:

```bash
kubectl logs pod-name -c logger
```

Delete:

```bash
kubectl delete pod multi-container
```

---

# Multi-Container Pod Architecture Summary

```
Pod

↓

Multiple Containers

↓

Shared Network

↓

Shared Storage

↓

Single Application
```

---

# Best Practices

### 1. Follow the Single Responsibility Principle

Each container should perform one well-defined task.

---

### 2. Use Shared Volumes Carefully

Share only the data required by cooperating containers.

---

### 3. Keep Containers Independent

Separate images and dependencies improve maintainability.

---

### 4. Monitor Resource Consumption

Remember that all containers share the Pod's node resources.

---

### 5. Choose the Correct Pattern

- **Sidecar** → Add supporting functionality.
- **Ambassador** → Proxy external communication.
- **Adapter** → Transform application output.

---

