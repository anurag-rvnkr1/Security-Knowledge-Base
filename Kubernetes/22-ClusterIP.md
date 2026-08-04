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

# How ClusterIP Works Internally

## Overview

A **ClusterIP** is one of the most fundamental networking abstractions in Kubernetes.

Although it appears to be a normal IP address, a ClusterIP is actually a **virtual IP (VIP)**.

No Pod, Node, or network interface owns this IP.

Instead, Kubernetes uses **kube-proxy** together with Linux networking technologies such as:

- iptables
- IPVS
- nftables (newer Kubernetes versions)
- EndpointSlices
- Linux Kernel Packet Forwarding

to transparently redirect traffic from the Service IP to one of the backend Pods.

---

# High-Level Architecture

```
                   Client Pod

                        │

                        ▼

                 Service DNS Name

                        │

                        ▼

                    CoreDNS

                        │

                        ▼

                 ClusterIP (VIP)

                        │

                        ▼

                  kube-proxy

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

       Pod A         Pod B         Pod C
```

---

# Complete Internal Workflow

```
Application

↓

DNS Lookup

↓

CoreDNS

↓

ClusterIP

↓

kube-proxy

↓

Endpoint Selection

↓

Backend Pod

↓

Application Response
```

---

# Step 1 – Create Service

Example:

```yaml
kind: Service
```

Deploy:

```bash
kubectl apply -f service.yaml
```

---

# Step 2 – API Server

The API Server:

- Validates the Service
- Stores it in etcd

```
kubectl

↓

API Server

↓

Service Stored
```

---

# Step 3 – Service Controller

The Service Controller watches:

- Services
- Pods
- Labels

Workflow:

```
Service

↓

Find Matching Pods

↓

Create Endpoint Objects
```

---

# Step 4 – Endpoint Creation

Suppose:

Pods:

```
backend-1

↓

10.244.1.5
```

```
backend-2

↓

10.244.2.8
```

Endpoints become:

```
backend

↓

10.244.1.5

10.244.2.8
```

---

# EndpointSlice

Modern Kubernetes uses **EndpointSlices** instead of one large Endpoints object.

Advantages:

- Better scalability
- Faster updates
- Reduced API load
- Efficient handling of thousands of Pods

Architecture:

```
Service

↓

EndpointSlices

↓

Backend Pods
```

---

# Step 5 – ClusterIP Allocation

Suppose:

```
Service

↓

ClusterIP

↓

10.96.20.15
```

Important:

```
No Pod Owns

10.96.20.15
```

It exists only as a virtual destination.

---

# Step 6 – CoreDNS

Application:

```
curl backend
```

DNS lookup:

```
backend.default.svc.cluster.local
```

CoreDNS returns:

```
10.96.20.15
```

The application now sends packets to the ClusterIP.

---

# Step 7 – kube-proxy Watches Services

Every worker Node runs:

```
kube-proxy
```

It watches:

- Services
- EndpointSlices
- Nodes

Whenever something changes:

```
New Pod

↓

Update Rules
```

---

# kube-proxy Responsibilities

```
Service

↓

Forward Traffic

↓

Backend Pods
```

It never processes application data itself.

Instead, it programs the Linux networking stack.

---

# Packet Flow

Suppose:

```
Application

↓

10.96.20.15
```

Linux checks:

```
iptables

↓

Match Rule

↓

Backend Pod
```

Traffic is redirected before reaching a physical network interface.

---

# iptables Mode

Historically, kube-proxy created **iptables rules**.

Architecture:

```
ClusterIP

↓

iptables Rule

↓

Backend Pod
```

Example:

```
10.96.20.15

↓

10.244.1.5
```

Linux rewrites the packet destination.

---

# IPVS Mode

IPVS is a Linux kernel load balancer.

Architecture:

```
ClusterIP

↓

IPVS

↓

Pod A

↓

Pod B

↓

Pod C
```

Benefits:

- Better performance
- Better scalability
- Advanced scheduling algorithms

---

# nftables Mode

Modern Linux systems increasingly use **nftables**.

Benefits:

- Simpler rule management
- Improved performance
- Unified packet filtering framework

Recent Kubernetes versions support kube-proxy with nftables on compatible systems.

---

# Packet Rewriting

Original packet:

```
Destination

↓

10.96.20.15
```

After kube-proxy:

```
Destination

↓

10.244.2.8
```

The application never notices the change.

---

# Response Flow

Backend Pod:

```
Application Response

↓

Client
```

The connection appears to be directly with the Service.

---

# Load Balancing

Suppose:

```
Three Pods
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

The exact algorithm depends on kube-proxy mode and kernel implementation.

---

# Pod Failure

Suppose:

```
Pod B

↓

Crash
```

EndpointSlice:

```
Updated

↓

Remove Pod B
```

kube-proxy:

```
Update Rules
```

Traffic is automatically routed only to healthy Pods.

---

# Scaling Up

Current:

```
3 Pods
```

Scale:

```
6 Pods
```

Workflow:

```
New Pods

↓

EndpointSlice Updated

↓

kube-proxy Updated

↓

Traffic Balanced
```

No Service restart is required.

---

# Service Without Endpoints

Suppose:

```
Service

↓

No Matching Pods
```

Result:

```
ClusterIP Exists

↓

No Backend

↓

Connection Fails
```

A common troubleshooting step is checking Endpoints.

---

# Internal Architecture

```
Application

↓

CoreDNS

↓

ClusterIP

↓

kube-proxy

↓

iptables / IPVS / nftables

↓

EndpointSlice

↓

Backend Pod
```

---

# kube-proxy Modes

| Mode | Description |
|------|-------------|
| Userspace | Legacy mode (rarely used today) |
| iptables | Default on many clusters |
| IPVS | High-performance kernel load balancing |
| nftables | Modern Linux packet filtering support |

---

# Endpoint vs EndpointSlice

| Endpoints | EndpointSlice |
|-----------|---------------|
| Older API | Modern API |
| One large object | Multiple smaller objects |
| Less scalable | Highly scalable |
| Higher API load | Lower API load |

---

# DNS Resolution Flow

```
Application

↓

backend.default.svc.cluster.local

↓

CoreDNS

↓

10.96.20.15
```

---

# Full Packet Flow

```
Client

↓

DNS

↓

CoreDNS

↓

ClusterIP

↓

kube-proxy

↓

Linux Kernel

↓

EndpointSlice

↓

Pod

↓

Application
```

---

# Hands-on Lab 1 – Create Deployment

```bash
kubectl create deployment nginx \
--image=nginx \
--replicas=3
```

---

# Hands-on Lab 2 – Expose Deployment

```bash
kubectl expose deployment nginx \
--port=80
```

Verify:

```bash
kubectl get svc
```

---

# Hands-on Lab 3 – Inspect EndpointSlices

```bash
kubectl get endpointslices
```

Observe backend Pod IP addresses associated with the Service.

---

# Hands-on Lab 4 – Test DNS

```bash
kubectl run tester \
--image=busybox \
-it --rm --restart=Never -- sh
```

Inside the Pod:

```bash
nslookup nginx
```

Observe the returned ClusterIP.

---

# Hands-on Lab 5 – Test Load Balancing

Inside the BusyBox Pod:

```bash
wget -qO- http://nginx
```

Repeat the request multiple times.

Then inspect the backend Pods to observe traffic distribution.

---

# Common Mistakes

## 1. Connecting Directly to Pod IPs

Incorrect:

```
Application

↓

10.244.x.x
```

Correct:

```
Application

↓

Service DNS
```

---

## 2. Forgetting Labels

Service:

```
Selector

↓

app=backend
```

Pods:

```
app=web
```

Result:

```
No Endpoints
```

---

## 3. Confusing ClusterIP with Pod IP

```
ClusterIP

↓

Virtual
```

```
Pod IP

↓

Real
```

---

## 4. Ignoring EndpointSlices

When troubleshooting Services:

```bash
kubectl get endpointslices
```

is often more useful than checking only Pods.

---

## 5. Assuming kube-proxy Forwards Packets Directly

kube-proxy generally **programs the kernel's networking tables** rather than acting as an inline proxy for every packet.

---

# ClusterIP Quick Revision

## Internal Flow

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

EndpointSlice

↓

Pod
```

---

## Networking Components

```
CoreDNS

↓

ClusterIP

↓

EndpointSlice

↓

iptables/IPVS/nftables

↓

Pod
```

---

## Packet Processing

```
Virtual IP

↓

Kernel Rules

↓

Backend Pod
```

---

# Essential kubectl Commands

View Services:

```bash
kubectl get svc
```

Describe Service:

```bash
kubectl describe svc backend
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

View Endpoints:

```bash
kubectl get endpoints
```

Test DNS:

```bash
kubectl exec -it <pod> -- nslookup backend
```

Test Connectivity:

```bash
kubectl exec -it <pod> -- wget -qO- http://backend
```

---

# Interview Questions

### Basic

- What is a ClusterIP?
- Why is ClusterIP the default Service type?
- What is the difference between a Pod IP and a ClusterIP?

---

### Intermediate

- What is the role of kube-proxy?
- What are EndpointSlices?
- How does DNS resolution work for Services?

---

### Advanced

- Explain the complete internal packet flow from a client Pod to a backend Pod through a ClusterIP Service.
- Compare iptables, IPVS, and nftables modes.
- Why doesn't a ClusterIP belong to any Pod?
- How does Kubernetes update Service routing when Pods are added or removed?
- Why are EndpointSlices preferred over Endpoints in large clusters?

---

# References

## Official Kubernetes Documentation

- Services
- ClusterIP
- EndpointSlices
- kube-proxy
- CoreDNS

---

## CNCF Resources

- Kubernetes Networking Model
- Kubernetes Best Practices
- SIG Network Documentation
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Networking
- NIST SP 800-190
- Linux Kernel Networking Documentation

---

## Recommended Practice

1. Deploy a three-replica application and expose it with a ClusterIP Service.
2. Inspect the generated Endpoints and EndpointSlices.
3. Verify DNS resolution from another Pod.
4. Scale the Deployment and observe EndpointSlice updates.
5. Delete a backend Pod and verify automatic failover.
6. Compare kube-proxy behavior in iptables and IPVS modes.
7. Trace the packet flow from a client Pod to a backend Pod.

---

# Chapter Summary

```
Application

↓

CoreDNS

↓

ClusterIP (Virtual IP)

↓

kube-proxy

↓

iptables / IPVS / nftables

↓

EndpointSlice

↓

Backend Pod

↓

Application Response
```

A **ClusterIP Service** is the foundation of Kubernetes service discovery and internal communication. By combining **CoreDNS**, **kube-proxy**, **EndpointSlices**, and Linux kernel networking, Kubernetes provides a stable virtual endpoint that automatically load-balances traffic across healthy backend Pods while hiding the dynamic nature of Pod lifecycles.

---
