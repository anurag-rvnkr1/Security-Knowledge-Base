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

# How Kubernetes Networking Works Internally

## Overview

Kubernetes networking appears simple from the outside:

```
Pod A

↓

Pod B
```

However, internally, many Linux networking components work together to make this communication possible.

These include:

- Network Namespaces
- Virtual Ethernet (veth) Pairs
- Linux Bridge
- Container Network Interface (CNI)
- Routing Tables
- kube-proxy
- CoreDNS
- iptables / IPVS / nftables
- Overlay Networks

Understanding these components explains **how Kubernetes enables seamless communication across Pods, Nodes, and Services**.

---

# High-Level Architecture

```
                    Kubernetes Cluster

                           │

      ┌────────────────────┼────────────────────┐

      ▼                    ▼                    ▼

   Worker Node 1       Worker Node 2      Worker Node 3

      │                    │                    │

   Linux Bridge        Linux Bridge       Linux Bridge

      │                    │                    │

   veth Pair           veth Pair          veth Pair

      │                    │                    │

      ▼                    ▼                    ▼

    Pod A               Pod B               Pod C
```

Each Node independently manages its local networking while the CNI plugin connects Nodes into a unified cluster network.

---

# Complete Packet Flow

```
Application

↓

Container

↓

Pod Network Namespace

↓

veth Pair

↓

Linux Bridge

↓

CNI Network

↓

Destination Node

↓

Linux Bridge

↓

veth Pair

↓

Destination Pod
```

---

# Step 1 – Pod Creation

Suppose a Pod is created.

```
kubectl apply

↓

API Server

↓

Scheduler

↓

Worker Node
```

The kubelet requests the container runtime to create the Pod.

---

# Step 2 – Pod Sandbox

Before containers start:

```
Container Runtime

↓

Pause Container

↓

Pod Sandbox
```

The **pause container** creates and owns the Pod's shared namespaces.

These include:

- Network namespace
- IPC namespace
- UTS namespace (hostname)

Every application container joins these namespaces.

---

# Step 3 – Network Namespace

Each Pod receives its own network namespace.

```
Pod

↓

Network Namespace

↓

IP Address
```

Example:

```
Pod

↓

10.244.1.15
```

Containers inside the Pod share this namespace.

---

# Step 4 – Virtual Ethernet Pair (veth)

Kubernetes connects the Pod to the Node using a **veth pair**.

Think of it as a virtual network cable.

```
Node

↓

veth

══════════════

veth

↓

Pod
```

One end exists inside the Pod.

The other end exists on the Node.

---

# veth Pair Workflow

```
Pod

↓

eth0

↓

veth Pair

↓

Linux Bridge
```

Every Pod receives its own virtual Ethernet interface.

---

# Step 5 – Linux Bridge

The Node maintains a virtual switch called a **Linux Bridge**.

```
Pod A

↓

veth

↓

Linux Bridge

↓

veth

↓

Pod B
```

The bridge forwards traffic between local Pods.

---

# Same Node Communication

Suppose:

```
Pod A

↓

Node 1
```

```
Pod B

↓

Node 1
```

Traffic flow:

```
Pod A

↓

veth

↓

Linux Bridge

↓

veth

↓

Pod B
```

No physical network is involved.

---

# Different Node Communication

Suppose:

```
Pod A

↓

Node 1
```

```
Pod B

↓

Node 2
```

Traffic flow:

```
Pod A

↓

Linux Bridge

↓

CNI Network

↓

Node 2

↓

Linux Bridge

↓

Pod B
```

The CNI plugin handles routing between Nodes.

---

# Step 6 – Container Network Interface (CNI)

The kubelet invokes the CNI plugin whenever a Pod is created.

Responsibilities include:

- Creating network interfaces
- Assigning Pod IPs
- Configuring routes
- Connecting Pods to the cluster network

Workflow:

```
Pod Created

↓

kubelet

↓

CNI Plugin

↓

Configure Network
```

---

# Pod IP Assignment

Example:

```
Pod

↓

10.244.2.18
```

The IP address is assigned by the CNI plugin based on the cluster's configured Pod network.

---

# Step 7 – Routing

Each Node maintains routing information.

Example:

```
10.244.1.0/24

↓

Node 1
```

```
10.244.2.0/24

↓

Node 2
```

Routes ensure packets reach the correct Node hosting the destination Pod.

---

# Step 8 – kube-proxy

Pods usually communicate through Services.

Example:

```
Application

↓

Service

↓

ClusterIP

↓

Pods
```

The Service itself is virtual.

kube-proxy programs the Node to forward traffic appropriately.

---

# kube-proxy Workflow

```
Service

↓

iptables / IPVS / nftables

↓

Backend Pod
```

kube-proxy configures the operating system's packet forwarding rules.

---

# ClusterIP

Example:

```
Service

↓

10.96.15.20
```

This IP is virtual.

No container owns it.

Instead:

```
ClusterIP

↓

kube-proxy

↓

Backend Pods
```

---

# CoreDNS

Applications typically communicate using names.

Example:

```
database.default.svc.cluster.local
```

Resolution:

```
Application

↓

CoreDNS

↓

ClusterIP
```

CoreDNS converts Service names into IP addresses.

---

# Full Internal Packet Flow

```
Application

↓

DNS Query

↓

CoreDNS

↓

ClusterIP

↓

kube-proxy

↓

Destination Pod

↓

Application
```

---

# Pod-to-Pod Flow

```
Pod A

↓

eth0

↓

veth Pair

↓

Linux Bridge

↓

Routing

↓

Node Network

↓

Destination Bridge

↓

veth Pair

↓

Pod B
```

---

# Service-to-Pod Flow

```
Application

↓

Service

↓

ClusterIP

↓

iptables / IPVS

↓

Selected Pod
```

The application is unaware of which Pod actually receives the request.

---

# External Client Flow

```
Internet

↓

LoadBalancer

↓

Ingress

↓

Service

↓

kube-proxy

↓

Pod
```

---

# Overlay Networks

Most Kubernetes clusters use **overlay networking** to connect Pods across Nodes.

Examples:

- VXLAN
- Geneve
- IP-in-IP (depending on the CNI plugin)

Architecture:

```
Node 1

↓

Overlay Tunnel

↓

Node 2
```

This allows Pods on different Nodes to communicate as if they were on the same network.

---

# Packet Encapsulation

When Pods are on different Nodes:

```
Original Packet

↓

Encapsulation

↓

Physical Network

↓

Decapsulation

↓

Destination Pod
```

The overlay network hides the complexity from applications.

---

# Network Namespaces Summary

Each Pod has:

```
Own Network Namespace

↓

Own Interfaces

↓

Own Routing Table

↓

Own IP
```

Containers inside the Pod share these resources.

---

# Internal Networking Architecture

```
Application

↓

Container

↓

Network Namespace

↓

veth Pair

↓

Linux Bridge

↓

CNI

↓

Routing

↓

Destination Node

↓

Destination Pod
```

---

# Hands-on Lab 1 – View Pod IPs

```bash
kubectl get pods -o wide
```

Observe:

- Pod IP
- Node

---

# Hands-on Lab 2 – Test Pod Connectivity

Create two Pods.

From one Pod:

```bash
kubectl exec -it pod-a -- ping <pod-b-ip>
```

Verify Pod-to-Pod communication.

---

# Hands-on Lab 3 – Test Service Connectivity

Create a Service.

Access it using:

```bash
kubectl exec -it pod-a -- \
wget -qO- http://service-name
```

Observe successful Service routing.

---

# Hands-on Lab 4 – DNS Resolution

```bash
kubectl exec -it pod-a -- nslookup kubernetes.default
```

Observe:

- Cluster DNS
- ClusterIP

---

# Hands-on Lab 5 – Inspect Routes (Advanced)

Inside a Pod:

```bash
ip addr

ip route
```

Observe:

- Network interface (`eth0`)
- Assigned IP
- Default route

---

# Common Mistakes

## 1. Using Pod IPs Directly

Incorrect:

```
Application

↓

10.244.1.8
```

Correct:

```
Application

↓

Service DNS
```

Pod IPs are ephemeral.

---

## 2. Assuming Services Are Pods

A Service is a virtual abstraction.

It does **not** run as a container.

---

## 3. Ignoring the CNI Plugin

Without a CNI plugin:

```
Pods

↓

No Network
```

Kubernetes depends on the CNI implementation for Pod networking.

---

## 4. Confusing Node IP and Pod IP

```
Node

↓

192.168.x.x
```

```
Pod

↓

10.244.x.x
```

These belong to different network layers.

---

## 5. Forgetting DNS

Applications should communicate using Service names, not hardcoded IP addresses.

---

# Kubernetes Networking Quick Revision

## Internal Flow

```
Container

↓

Network Namespace

↓

veth Pair

↓

Linux Bridge

↓

CNI

↓

Destination Pod
```

---

## Service Flow

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

Pod
```

---

## Networking Components

```
Network Namespace

↓

veth

↓

Linux Bridge

↓

CNI

↓

CoreDNS

↓

kube-proxy
```

---

# Essential kubectl Commands

View Pod IPs:

```bash
kubectl get pods -o wide
```

View Services:

```bash
kubectl get svc
```

View Endpoints:

```bash
kubectl get endpoints
```

Test DNS:

```bash
kubectl exec -it <pod> -- nslookup kubernetes.default
```

Test Connectivity:

```bash
kubectl exec -it <pod> -- ping <pod-ip>
```

---

# Interview Questions

### Basic

- How do Pods communicate with each other?
- What is the role of the CNI plugin?
- Why does each Pod receive its own IP address?

---

### Intermediate

- What is a veth pair?
- What is the Linux Bridge?
- How does kube-proxy route traffic?

---

### Advanced

- Explain the complete internal packet flow from one Pod to another.
- How does Kubernetes enable communication between Pods on different Nodes?
- Why is the pause container important for networking?
- What is the purpose of overlay networking?
- Compare ClusterIP, Pod IP, and Node IP.

---

# References

## Official Kubernetes Documentation

- Cluster Networking
- Container Network Interface (CNI)
- Services
- CoreDNS
- kube-proxy

---

## CNCF Resources

- Kubernetes Networking Model
- Kubernetes Best Practices
- CNI Specification
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- Kubernetes Networking SIG
- CIS Kubernetes Benchmark
- NIST SP 800-190
- Kubernetes Production Networking

---

## Recommended Practice

1. Deploy multiple Pods across different Nodes.
2. Verify Pod-to-Pod communication using Pod IPs.
3. Create a Service and access it via DNS.
4. Explore network interfaces with `ip addr` inside a Pod.
5. Compare Pod IPs, Node IPs, and ClusterIPs.
6. Install and inspect a CNI plugin such as Calico or Cilium.
7. Trace packet flow from a client to a backend Pod using Kubernetes networking tools.

---

# Chapter Summary

```
Developer

↓

Pod

↓

Network Namespace

↓

veth Pair

↓

Linux Bridge

↓

CNI Plugin

↓

Routing

↓

CoreDNS

↓

kube-proxy

↓

Destination Pod
```

Kubernetes networking is built on **Linux networking primitives** combined with **CNI plugins, virtual networking, DNS, and Service routing**. By assigning every Pod its own IP address and providing a flat cluster network, Kubernetes enables seamless communication between applications regardless of where they are scheduled, forming the networking foundation for all higher-level Kubernetes features.

---
