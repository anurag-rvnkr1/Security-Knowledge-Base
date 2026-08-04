# Chapter 8 – Namespaces

## Overview

A **Namespace** is a logical partition within a Kubernetes cluster that allows multiple teams, applications, or environments to share the same cluster while remaining isolated from one another.

Namespaces do **not** create separate Kubernetes clusters. Instead, they provide **logical isolation** for Kubernetes resources.

They help organize resources, apply security policies, manage quotas, and simplify administration.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Namespace is
- Why Namespaces are used
- Namespace Architecture
- Default Kubernetes Namespaces
- Creating and Managing Namespaces
- Resource Isolation
- Resource Quotas
- RBAC with Namespaces
- Best Practices

---

# Why Namespaces?

Imagine a single Kubernetes cluster shared by multiple teams.

Without Namespaces:

```
Kubernetes Cluster

↓

Frontend Pods

Backend Pods

Database Pods

Monitoring Pods

Testing Pods

Development Pods
```

Everything exists together, making management difficult.

With Namespaces:

```
Kubernetes Cluster

│

├── Development

├── Testing

├── Staging

├── Production

└── Monitoring
```

Resources become organized and easier to manage.

---

# What is a Namespace?

A Namespace is a logical boundary for Kubernetes resources.

```
Namespace

↓

Deployments

↓

ReplicaSets

↓

Pods

↓

Services

↓

ConfigMaps

↓

Secrets
```

Each Namespace maintains its own collection of resources.

---

# Namespace Architecture

```
               Kubernetes Cluster

     ┌─────────────────────────────────┐

     │                                 │

     │   Namespace: Development        │

     │      ├── Pods                   │
     │      ├── Services               │
     │      └── Deployments            │
     │                                 │

     │   Namespace: Production         │

     │      ├── Pods                   │
     │      ├── Services               │
     │      └── Deployments            │
     │                                 │

     │   Namespace: Monitoring         │

     │      ├── Prometheus             │
     │      └── Grafana                │
     │                                 │
     └─────────────────────────────────┘
```

---

# Default Namespaces

A new Kubernetes cluster typically includes several built-in Namespaces.

---

## default

The default Namespace for user-created resources.

```
default

↓

Applications
```

If no Namespace is specified, resources are generally created here.

---

## kube-system

Contains Kubernetes system components.

Examples:

- API Server
- CoreDNS
- kube-proxy
- Controller Manager

```
kube-system

↓

Cluster Components
```

Avoid deploying application workloads here.

---

## kube-public

A Namespace intended for publicly readable cluster information.

```
kube-public

↓

Public Cluster Data
```

---

## kube-node-lease

Stores Lease objects used by nodes to report their availability efficiently.

```
kube-node-lease

↓

Node Leases
```

---

# Viewing Namespaces

List all Namespaces:

```bash
kubectl get namespaces
```

or

```bash
kubectl get ns
```

Example:

```
NAME

default

kube-system

kube-public

kube-node-lease
```

---

# Creating a Namespace

Command:

```bash
kubectl create namespace development
```

Verify:

```bash
kubectl get namespaces
```

---

# Namespace YAML

Example:

```yaml
apiVersion: v1

kind: Namespace

metadata:

  name: development
```

Apply:

```bash
kubectl apply -f namespace.yaml
```

---

# Deploying Resources into a Namespace

Create a Deployment:

```bash
kubectl create deployment nginx \
--image=nginx \
-n development
```

or

```bash
kubectl apply -f deployment.yaml \
-n development
```

---

# Viewing Resources in a Namespace

Pods:

```bash
kubectl get pods \
-n development
```

Deployments:

```bash
kubectl get deployments \
-n development
```

Services:

```bash
kubectl get services \
-n development
```

---

# Viewing Resources Across All Namespaces

Pods:

```bash
kubectl get pods -A
```

Deployments:

```bash
kubectl get deployments -A
```

Services:

```bash
kubectl get services -A
```

---

# Namespace Isolation

Example:

```
Namespace A

↓

Pod nginx
```

```
Namespace B

↓

Pod nginx
```

Both Pods can have the same name because they exist in different Namespaces.

---

# Resource Naming

Within one Namespace:

```
nginx

↓

Unique
```

Across multiple Namespaces:

```
development/nginx

production/nginx
```

Both are valid.

---

# Namespace Scope

Common namespace-scoped resources include:

- Pods
- Deployments
- ReplicaSets
- Services
- ConfigMaps
- Secrets
- Jobs
- CronJobs
- StatefulSets
- DaemonSets

Examples of cluster-scoped resources include:

- Nodes
- Namespaces
- PersistentVolumes
- StorageClasses

---

# Namespace Communication

Namespaces provide logical organization—not complete network isolation.

Example:

```
Development Namespace

↓

Pod A

↓

Production Namespace

↓

Pod B
```

Pods in different Namespaces may still communicate unless restricted by **Network Policies**.

---

# Switching Namespace

For a single command:

```bash
kubectl get pods \
-n production
```

Or specify the Namespace in manifests:

```yaml
metadata:

  namespace: production
```

---

# Deleting a Namespace

Delete:

```bash
kubectl delete namespace development
```

Workflow:

```
Namespace

↓

All Resources

↓

Deleted
```

Deleting a Namespace removes the namespace-scoped resources it contains.

---

# Namespace Lifecycle

```
Create Namespace

↓

Deploy Resources

↓

Manage Applications

↓

Delete Namespace
```

---

# Common Use Cases

Namespaces are commonly used for:

- Development
- Testing
- Staging
- Production
- Monitoring
- Logging
- Security Tools
- CI/CD Pipelines
- Team Isolation

---

# Namespace Hierarchy Example

```
Cluster

│

├── development

│     ├── frontend

│     ├── backend

│     └── database

│

├── testing

│

├── staging

│

└── production
```

---

# Important kubectl Commands

View:

```bash
kubectl get ns
```

Create:

```bash
kubectl create namespace dev
```

Delete:

```bash
kubectl delete namespace dev
```

View Pods:

```bash
kubectl get pods \
-n dev
```

View Everything:

```bash
kubectl get all \
-n dev
```

View All Namespaces:

```bash
kubectl get pods -A
```

---

# Namespace Architecture Summary

```
Cluster

↓

Namespaces

↓

Deployments

↓

ReplicaSets

↓

Pods

↓

Containers
```

---

# Best Practices

### 1. Separate Environments

Use dedicated Namespaces for:

- Development
- Testing
- Staging
- Production

---

### 2. Do Not Deploy Applications into `kube-system`

Reserve the `kube-system` Namespace for Kubernetes components.

---

### 3. Apply Resource Quotas

Limit CPU, memory, and object creation within each Namespace using ResourceQuota objects.

---

### 4. Use RBAC with Namespaces

Grant users access only to the Namespaces they require.

---

### 5. Use Consistent Naming

Examples:

```
development

testing

staging

production

monitoring
```

Consistent naming improves automation and administration.

---
