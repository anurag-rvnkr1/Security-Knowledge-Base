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

# How Namespaces Work Internally

## Overview

Namespaces are one of Kubernetes' most fundamental organizational features.

They provide **logical isolation** within a single Kubernetes cluster, allowing multiple teams, environments, and applications to share the same cluster safely and efficiently.

Unlike virtual machines or separate Kubernetes clusters, Namespaces do **not** create isolated operating systems or separate control planes.

Instead, they organize Kubernetes resources at the API level.

---

# High-Level Architecture

```
                  Kubernetes Cluster

                           │

        ┌──────────────────┼──────────────────┐

        ▼                  ▼                  ▼

   Development         Production        Monitoring

        │                  │                  │

   Deployments        Deployments        Prometheus

   ReplicaSets        ReplicaSets        Grafana

   Pods               Pods

   Services           Services
```

The cluster is shared, but resources are logically grouped.

---

# How Kubernetes Stores Namespaces

Every Kubernetes object contains metadata.

Example:

```yaml
metadata:

  namespace: development
```

Internally, Kubernetes stores resources using:

```
Namespace

+

Resource Name
```

For example:

```
development/nginx

production/nginx
```

These are treated as two completely different objects.

---

# Internal Workflow

Suppose a user creates a Deployment.

Command:

```bash
kubectl apply -f deployment.yaml
```

Manifest:

```yaml
metadata:

  namespace: production
```

Workflow:

```
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

Namespace Check

↓

Store in etcd

↓

Deployment Controller

↓

ReplicaSet

↓

Pods
```

---

# Namespace Resolution

If a Namespace is specified:

```yaml
namespace: production
```

Kubernetes stores the object there.

If omitted:

```
default
```

is generally used.

---

# API Server Processing

The API Server performs several checks.

```
Request

↓

Namespace Exists?

↓

Yes

↓

Store Object

↓

Controller Watches Namespace
```

If the Namespace does not exist:

```
Error

↓

Namespace Not Found
```

---

# etcd Storage

Internally:

```
Namespace

↓

Objects

↓

Pods

↓

Deployments

↓

Services
```

The Namespace becomes part of the resource identity.

---

# Resource Lookup

Example:

```bash
kubectl get pods
```

Without specifying a Namespace:

```
Current Namespace

↓

Pods
```

With:

```bash
kubectl get pods -n production
```

Workflow:

```
API Server

↓

Production Namespace

↓

Return Pods
```

---

# Viewing All Namespaces

Command:

```bash
kubectl get pods -A
```

Workflow:

```
API Server

↓

Development

Production

Monitoring

↓

Return Everything
```

This is useful for cluster administrators.

---

# Namespace Creation

Command:

```bash
kubectl create namespace testing
```

Workflow:

```
kubectl

↓

API Server

↓

Namespace Object

↓

etcd
```

After creation:

```
Ready For Resources
```

---

# Resource Creation

Example:

```
Namespace

↓

Deployment

↓

ReplicaSet

↓

Pods
```

All namespace-scoped resources are associated with the Namespace.

---

# Namespace Deletion

Delete:

```bash
kubectl delete namespace testing
```

Workflow:

```
Namespace

↓

Find Resources

↓

Delete Resources

↓

Delete Namespace
```

This process is managed by Kubernetes controllers.

---

# Namespace Finalization

Before a Namespace is removed:

```
Namespace

↓

Delete Resources

↓

Cleanup

↓

Finalize

↓

Removed
```

If resources cannot be removed, the Namespace may remain in a **Terminating** state until cleanup is complete.

---

# Namespace Isolation

Example:

Development:

```
Pod

↓

frontend
```

Production:

```
Pod

↓

frontend
```

These Pods have identical names but exist independently because their Namespaces differ.

---

# Object Identity

Internally:

```
Namespace

+

Object Name

=

Unique Resource
```

Example:

```
development/api

production/api
```

Both are valid.

---

# Namespace Communication

Namespaces organize resources but **do not block network traffic** by default.

Example:

```
Development Pod

↓

Production Pod
```

Communication is generally allowed unless restricted by **Network Policies** or other security controls.

---

# Resource Discovery

View resources:

```bash
kubectl get all \
-n development
```

Workflow:

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
```

---

# Namespace Context

kubectl can operate within a chosen Namespace.

View current context:

```bash
kubectl config view
```

Set a default Namespace for the current context:

```bash
kubectl config set-context --current \
--namespace=development
```

Verify:

```bash
kubectl config view --minify
```

After this, many `kubectl` commands will use the selected Namespace unless overridden with `-n`.

---

# Internal Architecture

```
Kubernetes Cluster

↓

API Server

↓

Namespaces

↓

Controllers

↓

Resources
```

Each controller watches only the resources relevant to its operation.

---

# Namespace Lifecycle

```
Namespace Created

↓

Resources Added

↓

Applications Running

↓

Resources Deleted

↓

Namespace Removed
```

---

# Hands-on Lab 1 – Create Namespace

Create:

```bash
kubectl create namespace development
```

Verify:

```bash
kubectl get ns
```

---

# Hands-on Lab 2 – Deploy Application

```bash
kubectl create deployment nginx \
--image=nginx \
-n development
```

Verify:

```bash
kubectl get deployments \
-n development
```

---

# Hands-on Lab 3 – View Resources

Pods:

```bash
kubectl get pods \
-n development
```

Everything:

```bash
kubectl get all \
-n development
```

---

# Hands-on Lab 4 – View Across All Namespaces

```bash
kubectl get pods -A
```

Observe:

- kube-system
- default
- development

---

# Hands-on Lab 5 – Delete Namespace

```bash
kubectl delete namespace development
```

Watch:

```bash
kubectl get ns
```

Observe the Namespace progressing toward deletion.

---

# Resource Quotas (Preview)

Namespaces can limit resource consumption.

Example:

```
Namespace

↓

Maximum CPU

↓

Maximum Memory

↓

Maximum Pods
```

This prevents a single Namespace from consuming all cluster resources.

---

# LimitRanges (Preview)

LimitRanges define default or maximum/minimum resource values for containers and Pods within a Namespace.

Example:

```
Namespace

↓

Default CPU

↓

Default Memory
```

---

# RBAC with Namespaces (Preview)

RBAC commonly grants permissions at the Namespace level.

Example:

```
Developer

↓

Development Namespace

✓ Allowed

↓

Production Namespace

✗ Denied
```

This is a fundamental security practice.

---

# Best Practices

### 1. Use Namespaces to Organize Workloads

Separate applications and environments logically.

---

### 2. Apply Namespace-Level Security

Combine Namespaces with:

- RBAC
- Network Policies
- Resource Quotas

for stronger isolation.

---

### 3. Avoid Using `default` for Everything

Create dedicated Namespaces for production workloads.

---

### 4. Monitor Namespace Resources

Regularly inspect CPU, memory, and object usage per Namespace.

---

### 5. Keep Namespace Names Predictable

Examples:

```
development

testing

staging

production

monitoring
```

Consistent naming simplifies automation and administration.

---

# Resource Quotas

## Overview

A **ResourceQuota** is a Kubernetes object that limits the total amount of resources a Namespace can consume.

Without ResourceQuotas, a single application or team could consume excessive:

- CPU
- Memory
- Storage
- Pods
- Services
- ConfigMaps
- Secrets

This could negatively impact other workloads sharing the same cluster.

ResourceQuotas help ensure **fair resource allocation** among teams and applications.

---

# Why Resource Quotas?

Imagine three teams sharing one cluster.

Without quotas:

```
Cluster

│

├── Team A

│      200 Pods

│

├── Team B

│      2 Pods

│

└── Team C

       Cannot Schedule Pods
```

Team A consumes most of the cluster resources.

With quotas:

```
Cluster

│

├── Team A

│      Maximum 50 Pods

│

├── Team B

│      Maximum 50 Pods

│

└── Team C

       Maximum 50 Pods
```

Each team receives a controlled allocation.

---

# ResourceQuota Architecture

```
Namespace

↓

ResourceQuota

↓

CPU

↓

Memory

↓

Pods

↓

Storage

↓

Objects
```

Every ResourceQuota belongs to a Namespace.

---

# What Can ResourceQuota Limit?

Examples include:

### Compute Resources

- CPU Requests
- CPU Limits
- Memory Requests
- Memory Limits

---

### Storage

- Persistent Volume Claims (PVCs)
- Requested Storage

---

### Object Counts

- Pods
- Services
- Secrets
- ConfigMaps
- Jobs
- CronJobs
- PersistentVolumeClaims

---

# ResourceQuota Workflow

```
User

↓

Create Pod

↓

API Server

↓

ResourceQuota Check

↓

Within Limit?

↓

Yes

↓

Create Pod
```

If limits are exceeded:

```
Rejected
```

---

# ResourceQuota YAML

Example:

```yaml
apiVersion: v1

kind: ResourceQuota

metadata:

  name: dev-quota

spec:

  hard:

    requests.cpu: "4"

    requests.memory: 8Gi

    limits.cpu: "8"

    limits.memory: 16Gi

    pods: "20"

    services: "10"
```

---

# Understanding the YAML

```
Namespace

↓

ResourceQuota

↓

Hard Limits
```

Example:

```
Pods

↓

Maximum = 20
```

Once 20 Pods exist, additional Pods are rejected until resources become available.

---

# Creating a ResourceQuota

Apply:

```bash
kubectl apply -f quota.yaml
```

Verify:

```bash
kubectl get resourcequota
```

or

```bash
kubectl get quota
```

---

# Describe ResourceQuota

```bash
kubectl describe quota dev-quota
```

Example output:

```
Used CPU

↓

Allowed CPU

↓

Remaining CPU
```

This shows current usage versus configured limits.

---

# ResourceQuota Example

Suppose:

```
Maximum Pods

↓

5
```

Current:

```
4 Pods
```

Create another:

```
Success
```

Current:

```
5 Pods
```

Create one more:

```
Rejected
```

The quota prevents exceeding the configured limit.

---

# CPU Quota Example

Quota:

```
CPU Requests

↓

4
```

Current requests:

```
3 CPU
```

New Pod:

```
Requests 2 CPU
```

Result:

```
Total = 5 CPU

↓

Rejected
```

---

# Memory Quota Example

Namespace:

```
Memory Limit

↓

8 GiB
```

Current usage:

```
7 GiB
```

New Pod:

```
Requests 2 GiB
```

Result:

```
Rejected
```

---

# Object Count Quotas

Example:

```
Secrets

↓

Maximum = 20
```

After:

```
20 Secrets
```

Create another:

```
Rejected
```

The same concept applies to other supported resource types.

---

# ResourceQuota Scope

ResourceQuotas apply only to:

```
Namespace
```

Example:

```
Development

↓

20 Pods
```

Production:

```
Unlimited
```

unless another ResourceQuota exists.

---

# Multiple Namespaces

```
Development

↓

Quota A
```

```
Testing

↓

Quota B
```

```
Production

↓

Quota C
```

Each Namespace can have its own limits.

---

# Viewing Resource Usage

Describe:

```bash
kubectl describe quota
```

Example:

```
Resource

↓

Used

↓

Hard
```

This helps administrators monitor consumption.

---

# Hands-on Lab 1 – Create Namespace

```bash
kubectl create namespace development
```

---

# Hands-on Lab 2 – Create ResourceQuota

Example:

```yaml
apiVersion: v1

kind: ResourceQuota

metadata:

  name: development-quota

spec:

  hard:

    pods: "5"

    requests.cpu: "2"

    requests.memory: 4Gi
```

Deploy:

```bash
kubectl apply -f quota.yaml \
-n development
```

---

# Hands-on Lab 3 – Verify

```bash
kubectl get quota \
-n development
```

Describe:

```bash
kubectl describe quota development-quota \
-n development
```

---

# Hands-on Lab 4 – Create Pods

Create several Pods.

Observe quota usage:

```bash
kubectl describe quota \
-n development
```

Watch the **Used** values increase.

---

# Hands-on Lab 5 – Exceed Quota

Attempt to create more Pods than allowed.

Expected result:

```
Forbidden

↓

Quota Exceeded
```

Kubernetes rejects the request.

---

# ResourceQuota Lifecycle

```
Namespace Created

↓

Quota Created

↓

Resources Created

↓

Quota Updated

↓

Resources Deleted
```

---

# ResourceQuota vs LimitRange

| ResourceQuota | LimitRange |
|---------------|------------|
| Limits Namespace totals | Limits individual Pods and Containers |
| Controls overall resource consumption | Controls per-object resource configuration |
| Prevents one team from exhausting cluster resources | Prevents individual workloads from using unreasonable defaults or values |

These two resources are commonly used together.

---

# Benefits

- Fair resource sharing
- Prevents resource exhaustion
- Improves cluster stability
- Supports multi-tenancy
- Simplifies capacity planning

---

# Best Practices

### 1. Configure ResourceQuotas for Shared Clusters

Especially when multiple teams or applications share the same environment.

---

### 2. Combine with LimitRanges

Use LimitRanges to control individual Pods while ResourceQuotas manage Namespace-wide consumption.

---

### 3. Monitor Usage

Review:

```bash
kubectl describe quota
```

regularly.

---

### 4. Set Realistic Limits

Avoid values that unnecessarily block legitimate workloads.

---

### 5. Review Quotas Periodically

As applications evolve, adjust quotas to reflect current operational requirements.

---

# LimitRanges

## Overview

A **LimitRange** is a Kubernetes object that defines **default, minimum, and maximum resource constraints** for individual Pods and Containers within a Namespace.

While **ResourceQuota** controls the **total resources** a Namespace can consume, **LimitRange** controls **how much each Pod or Container can request or use**.

These two objects complement each other and are commonly used together in production clusters.

---

# Why LimitRanges?

Imagine a shared Kubernetes cluster.

Without LimitRanges:

```
Namespace

↓

Container A

↓

Memory = 32 GiB
```

One developer accidentally requests excessive resources.

Result:

```
Scheduler

↓

Cannot Place Pods

↓

Resource Waste
```

With a LimitRange:

```
Namespace

↓

Maximum Memory

↓

2 GiB
```

The oversized request is rejected.

---

# LimitRange Architecture

```
Namespace

↓

LimitRange

↓

Minimum Resources

↓

Default Resources

↓

Maximum Resources
```

Every new Pod or Container is evaluated against these rules.

---

# ResourceQuota vs LimitRange

| ResourceQuota | LimitRange |
|---------------|------------|
| Limits the Namespace as a whole | Limits each Pod or Container |
| Controls total CPU and Memory | Controls per-object CPU and Memory |
| Prevents one team from exhausting cluster resources | Prevents individual workloads from requesting unreasonable resources |
| Tracks aggregate usage | Applies validation and defaults |

Think of them together:

```
Namespace

│

├── ResourceQuota

│      Total Limits

│

└── LimitRange

       Individual Limits
```

---

# What Can a LimitRange Control?

A LimitRange can define:

- Default CPU requests
- Default CPU limits
- Default memory requests
- Default memory limits
- Minimum CPU
- Maximum CPU
- Minimum memory
- Maximum memory
- Maximum request-to-limit ratio (for certain resources)

---

# LimitRange Workflow

```
User

↓

Create Pod

↓

API Server

↓

LimitRange Validation

↓

Valid?

↓

Yes

↓

Create Pod
```

If the resource specification violates the LimitRange:

```
Rejected
```

---

# Default Values

Suppose a developer creates:

```yaml
containers:

- name: app

  image: nginx
```

No CPU or memory values are specified.

LimitRange automatically applies defaults:

```
CPU Request

↓

100m

Memory Request

↓

128Mi
```

The exact values depend on the configured LimitRange.

---

# LimitRange YAML

Example:

```yaml
apiVersion: v1

kind: LimitRange

metadata:

  name: container-limits

spec:

  limits:

  - type: Container

    default:

      cpu: "500m"

      memory: "512Mi"

    defaultRequest:

      cpu: "250m"

      memory: "256Mi"

    min:

      cpu: "100m"

      memory: "128Mi"

    max:

      cpu: "2"

      memory: "2Gi"
```

---

# YAML Structure

```
LimitRange

↓

Container Rules

↓

Minimum

↓

Default Request

↓

Default Limit

↓

Maximum
```

---

# Minimum Resources

Example:

```
Minimum CPU

↓

100m
```

Developer requests:

```
50m
```

Result:

```
Rejected
```

The request is below the configured minimum.

---

# Maximum Resources

Example:

```
Maximum Memory

↓

2 GiB
```

Developer requests:

```
4 GiB
```

Result:

```
Rejected
```

---

# Default Requests

Developer submits:

```yaml
resources: {}
```

LimitRange automatically applies:

```
CPU Request

↓

250m

Memory Request

↓

256Mi
```

This helps the scheduler make informed placement decisions.

---

# Default Limits

If no limits are specified:

```
Container

↓

LimitRange

↓

CPU Limit

↓

500m

↓

Memory Limit

↓

512Mi
```

Defaults help prevent unbounded resource consumption.

---

# Namespace Scope

LimitRanges apply only within their Namespace.

Example:

```
Development

↓

Maximum CPU = 2
```

Production:

```
Maximum CPU = 8
```

Each Namespace can define its own policy.

---

# Multiple Namespaces

```
Development

↓

LimitRange A
```

```
Testing

↓

LimitRange B
```

```
Production

↓

LimitRange C
```

Each team or environment can have different limits.

---

# Creating a LimitRange

Apply:

```bash
kubectl apply -f limitrange.yaml
```

Verify:

```bash
kubectl get limitrange
```

or

```bash
kubectl get limits
```

---

# Describe LimitRange

```bash
kubectl describe limitrange container-limits
```

Example output:

```
Type

↓

Container

↓

Default

↓

Minimum

↓

Maximum
```

---

# Hands-on Lab 1 – Create Namespace

```bash
kubectl create namespace development
```

---

# Hands-on Lab 2 – Create LimitRange

Example:

```yaml
apiVersion: v1

kind: LimitRange

metadata:

  name: dev-limits

spec:

  limits:

  - type: Container

    default:

      cpu: "500m"

      memory: "512Mi"

    defaultRequest:

      cpu: "250m"

      memory: "256Mi"

    min:

      cpu: "100m"

      memory: "128Mi"

    max:

      cpu: "2"

      memory: "2Gi"
```

Deploy:

```bash
kubectl apply -f limitrange.yaml \
-n development
```

---

# Hands-on Lab 3 – Verify

```bash
kubectl get limits \
-n development
```

Describe:

```bash
kubectl describe limitrange dev-limits \
-n development
```

---

# Hands-on Lab 4 – Create a Pod Without Resources

Deploy a Pod that omits the `resources` section.

Inspect the Pod:

```bash
kubectl get pod <pod-name> -o yaml
```

Observe that Kubernetes has applied the default resource requests and limits defined by the LimitRange.

---

# Hands-on Lab 5 – Exceed Maximum

Create a Pod requesting:

```
CPU

↓

4
```

LimitRange:

```
Maximum = 2
```

Expected result:

```
Rejected
```

The API Server denies the request.

---

# Common Validation Flow

```
Create Pod

↓

LimitRange

↓

Within Limits?

↓

Yes

↓

Create
```

Otherwise:

```
Rejected
```

---

# Resource Scheduling

LimitRanges improve scheduling by ensuring Pods have predictable resource requests.

```
Pod

↓

CPU Request

↓

Scheduler

↓

Node Selected
```

Without requests, scheduling decisions become less accurate.

---

# Benefits

- Prevents oversized resource requests
- Provides sensible defaults
- Improves scheduling
- Supports fair resource usage
- Standardizes resource policies

---

# Best Practices

### 1. Use LimitRanges with ResourceQuotas

ResourceQuota controls Namespace totals.

LimitRange controls individual workloads.

Use both.

---

### 2. Always Define Defaults

This ensures developers who omit resource settings still receive reasonable values.

---

### 3. Set Practical Minimums

Avoid values that are unrealistically low or unnecessarily restrictive.

---

### 4. Prevent Oversized Containers

Maximum values help protect cluster stability.

---

### 5. Review Resource Policies Regularly

As workloads evolve, revisit LimitRanges to ensure they still meet operational needs.

---
