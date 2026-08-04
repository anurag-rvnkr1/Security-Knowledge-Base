# Chapter 22 – Kubernetes Networking Fundamentals

## Overview

Networking is one of the most important concepts in Kubernetes.

Unlike traditional virtual machines, Kubernetes networking is designed so that **every Pod can communicate with every other Pod without Network Address Translation (NAT)** inside the cluster.

Kubernetes networking enables communication between:

- Pods
- Services
- Nodes
- External clients
- Control Plane Components

A production Kubernetes cluster relies on multiple networking components working together:

- Pod Network
- Service Network
- Cluster DNS
- kube-proxy
- CNI Plugins
- Ingress
- Network Policies

Understanding Kubernetes networking is essential for:

- Cluster administration
- Application deployment
- Troubleshooting
- Security
- CKA/CKAD certification

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes Networking Model
- Pod Networking
- Node Networking
- Service Networking
- Cluster Networking
- CNI (Container Network Interface)
- Pod-to-Pod Communication
- Pod-to-Service Communication
- External Connectivity
- Networking Best Practices

---

# Why Kubernetes Networking?

Imagine a cluster.

```
Node 1

↓

Pod A
```

```
Node 2

↓

Pod B
```

Applications need:

```
Pod A

↓

Pod B
```

Communication should work regardless of:

- Node location
- Pod restarts
- Scheduling decisions

---

# Kubernetes Networking Model

Kubernetes follows four fundamental networking principles.

---

## Rule 1

Every Pod gets its own IP address.

```
Pod A

↓

10.244.1.5
```

```
Pod B

↓

10.244.2.9
```

Pods never share IP addresses.

---

## Rule 2

Pods communicate directly.

```
Pod A

↓

Pod B
```

No NAT is required within the cluster.

---

## Rule 3

Nodes communicate with Pods.

```
Node

↓

Pod
```

Every Node can reach every Pod.

---

## Rule 4

Applications should use **Services** instead of Pod IPs.

```
Application

↓

Service

↓

Pods
```

Because Pod IPs change when Pods are recreated.

---

# Kubernetes Network Architecture

```
                     Internet

                         │

                         ▼

                    LoadBalancer

                         │

                         ▼

                      Ingress

                         │

                         ▼

                     Service

                         │

             ┌───────────┼───────────┐

             ▼           ▼           ▼

           Pod A      Pod B      Pod C

                         │

                         ▼

                      Worker Nodes
```

---

# Cluster Networking Components

```
Kubernetes Network

│

├── Pod Network

├── Service Network

├── Cluster DNS

├── kube-proxy

├── CNI Plugin

├── Ingress

└── Network Policies
```

---

# Pod Networking

Each Pod receives:

- One unique IP
- One network namespace
- One hostname

Example:

```
Pod

↓

10.244.3.8
```

Containers inside the Pod share that IP.

---

# Pod Communication

```
Pod A

↓

10.244.1.5

↓

Pod B

↓

10.244.2.9
```

Communication works even across different Nodes.

---

# Multi-Container Pod Networking

```
Pod

↓

IP Address

↓

Containers

↓

localhost
```

Containers communicate using:

```
127.0.0.1
```

---

# Node Networking

Worker Nodes also have IP addresses.

Example:

```
Node 1

↓

192.168.1.10
```

```
Node 2

↓

192.168.1.11
```

These IPs are different from Pod IPs.

---

# Service Networking

Services provide stable networking.

```
Client

↓

Service

↓

Pods
```

Service IP:

```
10.96.x.x
```

Pod IP:

```
10.244.x.x
```

They are different networks.

---

# Service Virtual IP

```
ClusterIP

↓

Virtual IP

↓

Pods
```

ClusterIP is managed by Kubernetes and does not belong to an individual Pod.

---

# Cluster DNS

Every Service receives:

```
DNS Name
```

Example:

```
frontend.default.svc.cluster.local
```

Applications should use DNS rather than Pod IPs.

---

# kube-proxy

kube-proxy manages Service networking.

```
Service

↓

kube-proxy

↓

Pods
```

Responsibilities:

- Load balancing
- Packet forwarding
- Service routing

---

# CNI Plugin

Kubernetes itself does **not** implement Pod networking.

Instead it uses:

```
CNI

↓

Container Network Interface
```

Common CNI plugins:

- Calico
- Cilium
- Flannel
- Weave Net
- Canal
- Antrea

---

# CNI Responsibilities

A CNI plugin:

- Assigns Pod IPs
- Creates virtual interfaces
- Configures routes
- Enables Pod communication
- Implements network policies (plugin dependent)

---

# Pod-to-Pod Communication

Example:

```
Pod A

↓

CNI Network

↓

Pod B
```

Whether Pods are on:

- Same Node
- Different Nodes

communication should work transparently.

---

# Pod-to-Service Communication

```
Pod

↓

Service DNS

↓

ClusterIP

↓

Backend Pods
```

Applications rarely communicate directly with Pod IPs.

---

# External Communication

```
Internet

↓

Ingress

↓

Service

↓

Pods
```

or

```
Internet

↓

LoadBalancer

↓

Pods
```

---

# Network Namespaces

Each Pod gets its own network namespace.

```
Pod

↓

Network Namespace

↓

Containers
```

All containers inside the Pod share it.

---

# IP Address Types

```
Node IP

↓

192.168.x.x
```

```
Pod IP

↓

10.244.x.x
```

```
ClusterIP

↓

10.96.x.x
```

Each serves a different purpose.

---

# Network Flow

```
Client

↓

Ingress

↓

Service

↓

kube-proxy

↓

Pod

↓

Container
```

---

# DNS Resolution

Application:

```
backend
```

DNS:

```
CoreDNS

↓

ClusterIP
```

Service:

```
ClusterIP

↓

Pods
```

---

# Common Network Traffic

## Pod → Pod

```
Direct
```

---

## Pod → Service

```
DNS

↓

ClusterIP
```

---

## External → Service

```
Ingress

↓

Service
```

---

## Pod → Internet

```
Node

↓

Internet
```

Outbound internet access is typically provided through the Node's networking configuration.

---

# Kubernetes Networking Layers

```
Application

↓

Pod

↓

Service

↓

Node

↓

Cluster Network

↓

Internet
```

---

# Important kubectl Commands

View Pods:

```bash
kubectl get pods -o wide
```

View Services:

```bash
kubectl get svc
```

View Nodes:

```bash
kubectl get nodes -o wide
```

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

---

# Networking Best Practices

### 1. Never Depend on Pod IPs

Always communicate through Services or stable DNS names.

---

### 2. Use DNS Names

Example:

```
database

api

frontend
```

instead of hardcoded IP addresses.

---

### 3. Choose the Right Service Type

- ClusterIP → Internal communication
- NodePort → Development or basic external access
- LoadBalancer → Production cloud environments

---

### 4. Secure Network Traffic

Implement Network Policies where supported by the CNI plugin.

---

### 5. Select an Appropriate CNI Plugin

Choose a CNI solution that matches your requirements for:

- Performance
- Security
- Observability
- Network Policy support

---

## Next Section

How Kubernetes Networking Works Internally

Container Network Interface (CNI)

Network Namespaces

Packet Flow

Hands-on Labs

Common Mistakes

Quick Revision

References

---