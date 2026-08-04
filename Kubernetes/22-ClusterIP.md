# Chapter 22 – ClusterIP Service

## Overview

A **ClusterIP** is the **default Service type** in Kubernetes.

It provides a **stable virtual IP address** that enables communication **within the Kubernetes cluster**.

Instead of applications communicating directly with Pod IP addresses, they communicate with a **Service**, which automatically forwards requests to healthy backend Pods.

This solves one of Kubernetes' biggest challenges:

> **Pods are temporary, but Services are stable.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What ClusterIP is
- Why ClusterIP is needed
- ClusterIP Architecture
- How ClusterIP Works
- Service Discovery
- DNS Integration
- kube-proxy's Role
- Endpoint Objects
- Internal Load Balancing
- Best Practices

---

# Why Do We Need ClusterIP?

Imagine an application.

```
Frontend

↓

Backend Pod
```

Backend Pod IP:

```
10.244.1.25
```

Suddenly:

```
Pod Crashes
```

Kubernetes creates a new Pod.

New IP:

```
10.244.3.12
```

Now:

```
Frontend

↓

Old IP

↓

Connection Failed
```

---

# Solution

Use a Service.

```
Frontend

↓

ClusterIP Service

↓

Backend Pods
```

The Service IP never changes, even if Pods are recreated.

---

# What is ClusterIP?

A ClusterIP is a **virtual IP address** assigned to a Kubernetes Service.

```
Service

↓

ClusterIP

↓

Pods
```

Applications communicate with the Service instead of individual Pods.

---

# High-Level Architecture

```
                  Client Pod

                       │

                       ▼

                 ClusterIP Service

                 10.96.15.20

                       │

         ┌─────────────┼─────────────┐

         ▼             ▼             ▼

      Pod A         Pod B         Pod C

   10.244.1.5    10.244.2.7    10.244.3.8
```

---

# ClusterIP Characteristics

- Internal-only access
- Stable virtual IP
- Automatic load balancing
- Service discovery using DNS
- Selects Pods using Labels
- Default Kubernetes Service type

---

# Service Types

| Service Type | Accessible From |
|--------------|-----------------|
| ClusterIP | Inside Cluster |
| NodePort | Outside Cluster via Node |
| LoadBalancer | Internet / Cloud |
| ExternalName | External DNS |

ClusterIP is the default.

---

# How ClusterIP Works

```
Application

↓

ClusterIP

↓

kube-proxy

↓

Backend Pod
```

The application never knows which Pod receives the request.

---

# ClusterIP Workflow

```
Client

↓

DNS

↓

ClusterIP

↓

kube-proxy

↓

Healthy Pod
```

---

# Creating a ClusterIP Service

Example:

```yaml
apiVersion: v1

kind: Service

metadata:

  name: backend

spec:

  selector:

    app: backend

  ports:

  - port: 80

    targetPort: 8080

  type: ClusterIP
```

Notice:

```
type: ClusterIP
```

This field is optional because ClusterIP is the default.

---

# YAML Breakdown

```
Service

↓

Selector

↓

Port

↓

TargetPort

↓

ClusterIP
```

---

# Service Selector

Suppose:

```yaml
selector:

  app: backend
```

Pods:

```
Pod 1

↓

app=backend
```

```
Pod 2

↓

app=backend
```

These Pods automatically become backend endpoints.

---

# Endpoint Objects

When a Service is created:

```
Service

↓

Endpoints
```

Example:

```
backend

↓

10.244.1.5

10.244.2.7

10.244.3.8
```

These are the Pods selected by the Service.

---

# ClusterIP Address

Example:

```
ClusterIP

↓

10.96.15.20
```

Pod IPs:

```
10.244.x.x
```

ClusterIP belongs to the Service, not the Pods.

---

# DNS Integration

Every Service automatically receives a DNS name.

Example:

```
backend.default.svc.cluster.local
```

Application:

```
Database Client

↓

backend
```

CoreDNS resolves the name to the Service's ClusterIP.

---

# Packet Flow

```
Application

↓

DNS

↓

CoreDNS

↓

ClusterIP

↓

kube-proxy

↓

Backend Pod
```

---

# Internal Load Balancing

Suppose:

```
Pod A

Pod B

Pod C
```

Requests:

```
Request 1

↓

Pod A
```

```
Request 2

↓

Pod B
```

```
Request 3

↓

Pod C
```

kube-proxy distributes traffic among available Pods.

---

# Pod Scaling

Current:

```
3 Pods
```

Scale:

```
6 Pods
```

Service:

```
Automatically

↓

Updated Endpoints
```

No application changes are required.

---

# Pod Failure

Suppose:

```
Pod B

↓

Crash
```

Endpoints:

```
Updated

↓

Remove Pod B
```

Traffic is automatically sent only to healthy Pods.

---

# Service Without Matching Pods

Suppose:

```
Selector

↓

No Matching Labels
```

Result:

```
Service Exists

↓

No Endpoints
```

Requests fail because there are no backend Pods.

---

# Multiple Services

```
Frontend Service

↓

Frontend Pods
```

```
Backend Service

↓

Backend Pods
```

```
Database Service

↓

Database Pods
```

Each Service has its own ClusterIP.

---

# ClusterIP vs Pod IP

| ClusterIP | Pod IP |
|-----------|---------|
| Stable | Temporary |
| Virtual | Real Pod Address |
| Service | Individual Pod |
| Load Balances | Single Pod |

---

# ClusterIP vs NodePort

| ClusterIP | NodePort |
|------------|----------|
| Internal | External |
| Default | Optional |
| Uses Cluster Network | Uses Node Network |

---

# ClusterIP vs LoadBalancer

| ClusterIP | LoadBalancer |
|------------|--------------|
| Internal Traffic | Internet Traffic |
| No Cloud Integration | Cloud Load Balancer |
| Virtual IP | Public IP |

---

# Service Discovery

Application:

```
Frontend

↓

backend

↓

CoreDNS

↓

ClusterIP
```

The application never needs to know Pod IPs.

---

# Internal Communication

```
Frontend

↓

backend Service

↓

Backend Pods
```

This is the recommended communication model in Kubernetes.

---

# Viewing Services

```bash
kubectl get svc
```

Example:

```
NAME       TYPE        CLUSTER-IP

backend    ClusterIP   10.96.15.20
```

---

# Viewing Endpoints

```bash
kubectl get endpoints
```

Example:

```
backend

↓

10.244.1.5

10.244.2.7
```

---

# Describe Service

```bash
kubectl describe svc backend
```

Useful information:

- ClusterIP
- Ports
- Selectors
- Endpoints

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f service.yaml
```

View:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc backend
```

View Endpoints:

```bash
kubectl get endpoints
```

Delete:

```bash
kubectl delete svc backend
```

---

# ClusterIP Architecture Summary

```
Client

↓

DNS

↓

ClusterIP

↓

kube-proxy

↓

Endpoints

↓

Pods
```

---

# Best Practices

### 1. Always Use Services

Applications should communicate with Services rather than Pod IPs.

---

### 2. Use Labels Consistently

Services rely on label selectors to identify backend Pods.

---

### 3. Use DNS Names

Prefer:

```
backend
```

instead of:

```
10.96.15.20
```

---

### 4. Verify Endpoints

If a Service is unreachable:

```bash
kubectl get endpoints
```

is one of the first troubleshooting commands to run.

---

### 5. Keep Services Focused

One Service should expose one logical application or API.

---

## Next Section

How ClusterIP Works Internally

kube-proxy Deep Dive

EndpointSlices

iptables vs IPVS

Hands-on Labs

Common Mistakes

Quick Revision

References

---