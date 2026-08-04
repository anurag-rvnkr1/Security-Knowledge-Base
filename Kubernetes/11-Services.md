# Chapter 11 – Services

## Overview

A **Service** is a Kubernetes object that provides a **stable network endpoint** for a group of Pods.

Pods in Kubernetes are **ephemeral**:

- Pods can be deleted
- Pods can be recreated
- Pod IP addresses can change
- Pods may be scheduled on different Nodes

If applications communicated directly using Pod IP addresses, connectivity would frequently break.

A Service solves this problem by providing a **stable virtual IP address (ClusterIP)** and a **DNS name** that remains consistent even when the underlying Pods change.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Service is
- Why Services are required
- Service Architecture
- Service Discovery
- Service Types
- ClusterIP
- NodePort
- LoadBalancer
- ExternalName
- Headless Services
- Service Selectors
- Endpoint & EndpointSlice Concepts
- Best Practices

---

# Why Services?

Imagine an application with three Pods.

```
Deployment

↓

Pod A

10.244.1.5

↓

Pod B

10.244.2.8

↓

Pod C

10.244.3.4
```

Suppose Pod B crashes.

```
Pod B

↓

Deleted

↓

New Pod

↓

10.244.4.12
```

The IP address changes.

Applications depending on the old IP will fail.

---

# Solution

Instead of using Pod IPs:

```
Application

↓

Service

↓

Pods
```

The Service always remains available.

---

# What is a Service?

A Service is an abstraction that exposes a group of Pods as a **single network endpoint**.

```
Client

↓

Service

↓

Pods
```

Applications communicate with the Service—not individual Pods.

---

# Service Architecture

```
                 Client

                    │

                    ▼

               Kubernetes Service

                    │

        ┌───────────┼───────────┐

        ▼           ▼           ▼

      Pod A       Pod B       Pod C
```

The Service automatically routes requests to healthy Pods.

---

# Service Responsibilities

A Service provides:

- Stable IP address
- Stable DNS name
- Load balancing
- Service discovery
- Pod abstraction
- Loose coupling between clients and Pods

---

# Service Workflow

```
Client

↓

Service

↓

Selector

↓

Matching Pods

↓

Response
```

The Service uses **Label Selectors** to determine which Pods receive traffic.

---

# Service YAML

Example:

```yaml
apiVersion: v1

kind: Service

metadata:

  name: nginx-service

spec:

  selector:

    app: nginx

  ports:

  - port: 80

    targetPort: 80
```

---

# YAML Structure

```
Service

↓

Metadata

↓

Selector

↓

Ports

↓

Type
```

---

# Understanding Selectors

Service:

```yaml
selector:

  app: nginx
```

Pods:

```yaml
labels:

  app: nginx
```

Workflow:

```
Service

↓

Selector

↓

Matching Pods
```

If labels do not match, the Service has no endpoints.

---

# Service Types

Kubernetes supports four primary Service types.

```
Services

│

├── ClusterIP

├── NodePort

├── LoadBalancer

└── ExternalName
```

Additionally, Kubernetes supports **Headless Services**, which behave differently from standard Services.

---

# ClusterIP (Default)

```
Client

↓

ClusterIP

↓

Pods
```

Characteristics:

- Internal cluster access only
- Default Service type
- Stable virtual IP
- Accessible only within the cluster

Example:

```yaml
spec:

  type: ClusterIP
```

---

# NodePort

```
External Client

↓

Node IP

↓

NodePort

↓

Pods
```

Characteristics:

- Opens a port on every Node
- Allows external access
- Uses a port typically in the range 30000–32767 (default configuration)

Example:

```yaml
spec:

  type: NodePort
```

---

# LoadBalancer

```
Internet

↓

Cloud Load Balancer

↓

Service

↓

Pods
```

Characteristics:

- Integrates with supported cloud providers
- Creates an external load balancer
- Common in managed Kubernetes services

Example:

```yaml
spec:

  type: LoadBalancer
```

---

# ExternalName

Instead of forwarding traffic to Pods:

```
Service

↓

External DNS

↓

Database
```

Example:

```yaml
spec:

  type: ExternalName

  externalName: database.example.com
```

This Service acts as a DNS alias.

---

# Headless Service

A Headless Service does not allocate a ClusterIP.

```
Client

↓

DNS

↓

Pod A

Pod B

Pod C
```

Configuration:

```yaml
clusterIP: None
```

Common use cases:

- StatefulSets
- Direct Pod discovery
- Custom client-side load balancing

---

# Service Discovery

Every Service receives a DNS name.

Example:

```
nginx-service
```

Within the same Namespace:

```
http://nginx-service
```

Across Namespaces:

```
http://nginx-service.production.svc.cluster.local
```

Applications should use Service DNS names instead of Pod IPs.

---

# Service Ports

Example:

```yaml
ports:

- port: 80

  targetPort: 8080
```

Meaning:

```
Service Port

80

↓

Pod Port

8080
```

---

# Port Terminology

| Field | Meaning |
|--------|---------|
| port | Port exposed by the Service |
| targetPort | Port used by the Pod |
| nodePort | External Node port (NodePort Services only) |

---

# Creating a Service

Apply:

```bash
kubectl apply -f service.yaml
```

Verify:

```bash
kubectl get services
```

or

```bash
kubectl get svc
```

---

# Viewing Services

List:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc nginx-service
```

Review:

- Type
- Cluster IP
- Ports
- Selectors
- Endpoints

---

# Service Lifecycle

```
Create Service

↓

Assign ClusterIP

↓

Find Matching Pods

↓

Receive Traffic

↓

Route Requests

↓

Delete Service
```

---

# Important kubectl Commands

View:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc nginx-service
```

Delete:

```bash
kubectl delete svc nginx-service
```

View Endpoints:

```bash
kubectl get endpoints
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

---

# Services vs Pods

| Service | Pod |
|----------|-----|
| Stable endpoint | Ephemeral workload |
| Stable IP | Dynamic IP |
| DNS name | No permanent DNS identity |
| Load balancing | Runs application |
| Selects multiple Pods | Single instance |

---

# Service Architecture Summary

```
Client

↓

Service

↓

Selector

↓

Pods

↓

Containers
```

---

# Best Practices

### 1. Never Communicate Directly Using Pod IPs

Always use Services for application-to-application communication.

---

### 2. Use Meaningful Service Names

Examples:

```
frontend

backend

database

auth-service
```

---

### 3. Verify Label Selectors

Ensure the Service selector matches the labels applied to the target Pods.

---

### 4. Choose the Correct Service Type

- ClusterIP → Internal communication
- NodePort → Basic external access
- LoadBalancer → Cloud environments
- ExternalName → External DNS integration

---

### 5. Prefer DNS Names

Applications should connect using Service DNS names rather than hard-coded IP addresses.

---

## Next Section

How Services Work Internally

Endpoints & EndpointSlices

kube-proxy

Service Load Balancing

Hands-on Labs

Common Mistakes

Quick Revision

References

---