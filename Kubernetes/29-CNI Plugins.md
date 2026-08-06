# Chapter 29 – CNI Plugins (Container Network Interface)

## Overview

One of the most common misconceptions among Kubernetes beginners is:

> **"Kubernetes provides networking."**

This is **not true**.

Kubernetes defines **how networking should behave**, but **it does not implement Pod networking**.

Instead, Kubernetes delegates networking responsibilities to a **Container Network Interface (CNI) plugin**.

The CNI plugin is responsible for:

- Assigning IP addresses to Pods
- Connecting Pods to the network
- Configuring routing
- Enabling Pod-to-Pod communication
- Supporting Network Policies (plugin dependent)

Without a CNI plugin:

```
Pods

↓

No Network

↓

Cluster Unusable
```

Every Kubernetes cluster **must** have a compatible CNI plugin.

---

# Learning Objectives

After completing this chapter, you will understand:

- What CNI is
- Why Kubernetes needs CNI
- CNI Architecture
- CNI Specification
- How CNI Plugins Work
- Popular CNI Plugins
- CNI Components
- Pod Networking
- IP Address Management (IPAM)
- Best Practices

---

# Why Do We Need CNI?

Imagine:

```
Node

↓

New Pod
```

Questions arise:

- Which IP should the Pod receive?
- How can it communicate with other Pods?
- How does it communicate across Nodes?
- Who creates the network interface?
- Who configures routes?

Kubernetes does not answer these questions directly.

The **CNI plugin** does.

---

# Kubernetes Without CNI

```
Worker Node

↓

Pod

↓

No IP

↓

No Communication
```

The Pod may exist, but networking will not function.

---

# Kubernetes With CNI

```
Worker Node

↓

CNI Plugin

↓

Pod IP

↓

Network Interface

↓

Routes

↓

Communication Enabled
```

---

# What is CNI?

**Container Network Interface (CNI)** is an open specification that defines how container runtimes configure networking.

It standardizes how Kubernetes and other container platforms interact with networking plugins.

Originally developed for container networking, it is now maintained under the CNCF ecosystem.

---

# High-Level Architecture

```
                Kubernetes

                     │

                     ▼

                  kubelet

                     │

                     ▼

               Container Runtime

                     │

                     ▼

                 CNI Plugin

                     │

          ┌──────────┼──────────┐

          ▼          ▼          ▼

      Network      IPAM      Routes

                     │

                     ▼

                    Pod
```

---

# Kubernetes Networking Stack

```
Application

↓

Pod

↓

Container Runtime

↓

CNI Plugin

↓

Linux Network

↓

Physical Network
```

---

# CNI Responsibilities

A CNI plugin performs:

- Network interface creation
- IP allocation
- Route configuration
- Network namespace setup
- Pod connectivity
- Policy enforcement (if supported)

---

# Pod Creation Workflow

```
kubectl apply

↓

API Server

↓

Scheduler

↓

Worker Node

↓

kubelet

↓

Container Runtime

↓

CNI Plugin

↓

Pod Ready
```

---

# Step-by-Step Networking

Suppose:

```
New Pod
```

The kubelet requests the container runtime to create it.

Before the Pod starts:

```
Container Runtime

↓

CNI Plugin
```

The CNI configures networking.

---

# Network Namespace

Each Pod receives:

```
Network Namespace
```

Containing:

- Network interfaces
- Routing table
- IP addresses
- ARP table

Containers within the Pod share this namespace.

---

# Virtual Ethernet Pair (veth)

The CNI creates:

```
Pod

↓

veth

══════════════

veth

↓

Node
```

One end is placed inside the Pod.

The other remains on the Node.

---

# Linux Bridge

Many CNI plugins connect Pods through a bridge.

```
Pod A

↓

Bridge

↓

Pod B
```

The bridge switches traffic between local Pods.

---

# IP Address Assignment

The CNI allocates an IP.

Example:

```
Pod

↓

10.244.1.18
```

Every Pod receives a unique IP address within the cluster.

---

# IPAM (IP Address Management)

Most CNI plugins use an **IPAM** component.

Responsibilities:

- Allocate IPs
- Release IPs
- Prevent duplicate assignments
- Manage address pools

```
IPAM

↓

Pod IP
```

---

# Route Configuration

The CNI adds routing entries.

Example:

```
10.244.2.0/24

↓

Worker Node 2
```

This enables Pods on different Nodes to communicate.

---

# Packet Flow

```
Pod

↓

veth

↓

Bridge

↓

CNI Network

↓

Destination Node

↓

Destination Pod
```

---

# Overlay Networks

Many CNI plugins create an **overlay network**.

Example:

```
Node 1

↓

VXLAN Tunnel

↓

Node 2
```

Overlay networking allows Pods on different Nodes to communicate without requiring the underlying physical network to know Pod IPs.

---

# Underlay Networks

Some CNIs use the physical network directly.

```
Pod

↓

Physical Network

↓

Destination
```

This avoids encapsulation but requires network infrastructure capable of routing Pod CIDRs.

---

# CNI Configuration

CNI configuration files are commonly stored under:

```
/etc/cni/net.d/
```

These files describe:

- Plugin type
- IPAM configuration
- Network settings

---

# CNI Binaries

Plugin executables are typically stored in:

```
/opt/cni/bin/
```

The container runtime executes these binaries when creating or deleting Pod networking.

---

# CNI Commands

The CNI specification defines operations such as:

```
ADD
```

Creates networking for a Pod.

```
DEL
```

Removes networking when a Pod is deleted.

```
CHECK
```

(Optional) Verifies network configuration.

---

# Popular CNI Plugins

| Plugin | Highlights |
|----------|------------|
| Calico | Routing, Network Policies, eBPF support |
| Cilium | eBPF-based networking and security |
| Flannel | Simple overlay networking |
| Weave Net | Automatic mesh networking |
| Antrea | Open vSwitch-based networking |
| Canal | Flannel + Calico policy combination |

---

# Calico

Features:

- Layer 3 networking
- BGP support
- Network Policies
- eBPF mode
- Production-ready

---

# Cilium

Features:

- eBPF
- High performance
- Observability
- Network Policies
- Service Mesh integration

---

# Flannel

Features:

- Simple deployment
- VXLAN overlay
- Lightweight
- Good for learning and smaller environments

Flannel does **not** natively implement Kubernetes Network Policies.

---

# Weave Net

Features:

- Automatic peer discovery
- Mesh networking
- Simple installation
- Network Policy support (depending on configuration)

---

# Antrea

Features:

- Open vSwitch
- Kubernetes Network Policies
- Flow visibility
- Multi-cluster capabilities

---

# CNI Architecture Summary

```
Kubernetes

↓

kubelet

↓

Container Runtime

↓

CNI Plugin

↓

IPAM

↓

Network Interface

↓

Pod
```

---

# View CNI Pods

```bash
kubectl get pods -A
```

Examples:

```
calico-node
```

```
cilium
```

```
antrea-agent
```

---

# View CNI Configuration

```bash
ls /etc/cni/net.d/
```

---

# View CNI Binaries

```bash
ls /opt/cni/bin/
```

---

# Important kubectl Commands

View Nodes:

```bash
kubectl get nodes
```

View Pods:

```bash
kubectl get pods -o wide
```

View CNI Pods:

```bash
kubectl get pods -A
```

Inspect Node:

```bash
kubectl describe node <node-name>
```

---

# Best Practices

### 1. Choose the Right CNI

Select a plugin based on:

- Scale
- Performance
- Security
- Cloud compatibility
- Network Policy support

---

### 2. Monitor IP Usage

Prevent Pod CIDR exhaustion.

---

### 3. Secure Pod Networking

Use Network Policies where supported.

---

### 4. Keep CNI Updated

Networking plugins receive important:

- Security patches
- Performance improvements
- Kubernetes compatibility updates

---

### 5. Test Multi-Node Connectivity

Verify Pod-to-Pod communication across Nodes after cluster changes.

---
