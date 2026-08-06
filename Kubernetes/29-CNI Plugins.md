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

# Chapter 29 – How CNI Plugins Work Internally

## Overview

Installing a CNI plugin is only the beginning.

The real magic happens **when a Pod is created**.

Every time Kubernetes schedules a new Pod, multiple components work together to configure networking automatically.

The workflow involves:

- API Server
- Scheduler
- kubelet
- Container Runtime
- CNI Plugin
- IPAM
- Linux Kernel
- Network Namespace
- Virtual Ethernet (veth)
- Routing Tables

Within milliseconds, a new Pod receives:

- A unique IP address
- Network interfaces
- Routing information
- Connectivity to every other Pod

This chapter explains exactly how that happens.

---

# Learning Objectives

After completing this chapter, you will understand:

- Complete Pod networking lifecycle
- kubelet and CNI interaction
- CNI ADD and DEL commands
- IPAM internals
- Network namespace creation
- Virtual Ethernet (veth) creation
- Linux bridge integration
- Overlay networking
- Packet flow
- Network teardown

---

# High-Level Architecture

```
               Kubernetes API

                     │

                     ▼

                 Scheduler

                     │

                     ▼

                  Worker Node

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

      ┌──────────────┼──────────────┐

      ▼              ▼              ▼

   IPAM          veth Pair      Routing

                     │

                     ▼

                    Pod
```

---

# Complete Workflow

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

CNI ADD

↓

Network Ready

↓

Pod Starts
```

---

# Step 1 – Pod Creation

Example:

```bash
kubectl apply -f pod.yaml
```

The API Server stores the Pod definition.

---

# Step 2 – Scheduler

The Scheduler selects the most suitable Node.

```
Pending Pod

↓

Worker Node 2
```

The Pod is assigned to that Node.

---

# Step 3 – kubelet

The kubelet on the selected Node notices the assignment.

Responsibilities:

- Create the Pod
- Start containers
- Configure networking
- Monitor Pod health

Before application containers start:

```
Networking

↓

Must Exist
```

---

# Step 4 – Container Runtime

The container runtime (for example, containerd or CRI-O):

- Creates the Pod sandbox
- Creates the pause container
- Creates the network namespace

```
Container Runtime

↓

Pause Container

↓

Network Namespace
```

---

# Pause Container

Every Pod contains a hidden **pause container**.

Its primary job is to own shared namespaces:

- Network namespace
- IPC namespace
- UTS namespace

All application containers join these namespaces.

---

# Step 5 – CNI ADD Command

The container runtime invokes the CNI plugin.

Command:

```
ADD
```

The CNI receives details such as:

- Pod name
- Namespace
- Container ID
- Network namespace path
- Interface name

---

# CNI ADD Workflow

```
Container Runtime

↓

CNI Plugin

↓

Configure Networking
```

---

# Step 6 – Create Network Namespace

The CNI enters the Pod's network namespace.

Creates:

```
Network Namespace

↓

eth0

↓

Routing Table

↓

Loopback Interface
```

---

# Step 7 – Create veth Pair

The CNI creates a virtual Ethernet pair.

```
Pod

↓

eth0

══════════════

veth

↓

Worker Node
```

One interface is moved into the Pod.

The other stays on the host.

---

# Step 8 – Connect to Linux Bridge

Many CNIs attach the host-side interface to a bridge.

```
Pod

↓

veth

↓

Linux Bridge

↓

Other Pods
```

Local Pod communication now becomes possible.

---

# Step 9 – IPAM Allocation

The CNI contacts its IP Address Management (IPAM) component.

Example:

```
Available Pool

↓

10.244.2.0/24
```

Assigned:

```
Pod

↓

10.244.2.15
```

The IP is reserved until the Pod is deleted.

---

# Step 10 – Configure Interfaces

Inside the Pod:

```
eth0

↓

10.244.2.15/24
```

Loopback:

```
lo
```

Both interfaces become active.

---

# Step 11 – Configure Routes

Example routing table:

```
Destination

↓

Default Gateway

↓

Linux Bridge
```

The Pod can now communicate beyond its namespace.

---

# Step 12 – Configure ARP

The Linux kernel updates:

- ARP tables
- Neighbor tables
- Interface state

Network communication becomes possible.

---

# Step 13 – Return Success

The CNI reports:

```
Success
```

The container runtime continues starting application containers.

```
Networking

↓

Ready

↓

Containers Start
```

---

# Pod Ready

Final state:

```
Pod

↓

IP Address

↓

Routes

↓

Interfaces

↓

Reachable
```

---

# Packet Flow (Same Node)

```
Pod A

↓

eth0

↓

veth

↓

Linux Bridge

↓

veth

↓

Pod B
```

Traffic never leaves the Node.

---

# Packet Flow (Different Nodes)

```
Pod A

↓

Bridge

↓

Overlay Network

↓

Bridge

↓

Pod B
```

The CNI handles inter-node transport.

---

# Overlay Networking

Most CNIs use encapsulation.

Common technologies:

- VXLAN
- Geneve
- IP-in-IP (plugin dependent)

Example:

```
Node 1

↓

VXLAN Tunnel

↓

Node 2
```

---

# Underlay Networking

Some CNIs use direct routing.

```
Pod

↓

Physical Network

↓

Destination Pod
```

Requires the network infrastructure to understand Pod CIDRs.

---

# CNI DEL Command

When a Pod is deleted:

```
Pod Deleted

↓

Container Runtime

↓

CNI DEL
```

The plugin:

- Removes interfaces
- Releases IP
- Deletes routes
- Cleans namespaces

---

# CNI DEL Workflow

```
Delete Pod

↓

Release IP

↓

Delete veth

↓

Remove Routes

↓

Cleanup Complete
```

---

# CNI CHECK Command

Some plugins support:

```
CHECK
```

Purpose:

- Validate network configuration
- Detect inconsistencies
- Verify interface state

Support is optional.

---

# Internal Architecture

```
API Server

↓

Scheduler

↓

kubelet

↓

Container Runtime

↓

CNI ADD

↓

IPAM

↓

veth

↓

Bridge

↓

Routes

↓

Pod Ready
```

---

# CNI Configuration Files

Typical location:

```bash
/etc/cni/net.d/
```

Example:

```json
{
  "cniVersion": "1.0.0",
  "name": "cluster-network",
  "type": "calico"
}
```

---

# CNI Binary Directory

Typical location:

```bash
/opt/cni/bin/
```

Contains plugin executables such as:

- bridge
- host-local
- loopback
- calico
- flannel
- cilium

---

# Hands-on Lab 1 – View CNI Configuration

```bash
ls /etc/cni/net.d/
```

Observe available network configuration files.

---

# Hands-on Lab 2 – View Installed Plugins

```bash
ls /opt/cni/bin/
```

Review installed CNI binaries.

---

# Hands-on Lab 3 – Inspect Pod Networking

Create a Pod:

```bash
kubectl run nginx \
--image=nginx
```

View:

```bash
kubectl get pod nginx -o wide
```

Observe the assigned Pod IP.

---

# Hands-on Lab 4 – Inspect Interfaces

Inside the Pod:

```bash
ip addr
```

Observe:

- `eth0`
- `lo`

---

# Hands-on Lab 5 – Inspect Routes

Inside the Pod:

```bash
ip route
```

Observe:

- Default route
- Pod network
- Gateway

---

# Common Mistakes

## 1. Assuming Kubernetes Configures Networking

Incorrect:

```
Kubernetes

↓

Creates Network
```

Correct:

```
Kubernetes

↓

Calls CNI

↓

CNI Configures Network
```

---

## 2. Forgetting the Pause Container

The pause container owns the Pod's shared network namespace.

Without it, containers in the Pod could not share networking.

---

## 3. Ignoring IPAM

Every Pod IP comes from an IPAM component.

Duplicate IP addresses are prevented through IPAM management.

---

## 4. Confusing Bridge with Overlay

Bridge:

```
Local Node
```

Overlay:

```
Multiple Nodes
```

They solve different networking problems.

---

## 5. Forgetting Cleanup

A correct CNI implementation must release:

- IP addresses
- Interfaces
- Routes

when Pods are deleted.

---

# Quick Revision

## Pod Creation

```
Scheduler

↓

kubelet

↓

Container Runtime

↓

CNI ADD

↓

Pod Ready
```

---

## Networking Setup

```
Network Namespace

↓

veth Pair

↓

Bridge

↓

IP Address

↓

Routes
```

---

## Pod Deletion

```
Delete Pod

↓

CNI DEL

↓

Release IP

↓

Cleanup
```

---

# Essential Commands

View Pod IPs:

```bash
kubectl get pods -o wide
```

View CNI Pods:

```bash
kubectl get pods -A
```

View CNI Config:

```bash
ls /etc/cni/net.d/
```

View CNI Plugins:

```bash
ls /opt/cni/bin/
```

Inspect Pod Network:

```bash
kubectl exec -it <pod> -- ip addr
```

Inspect Routes:

```bash
kubectl exec -it <pod> -- ip route
```

---

# Interview Questions

### Basic

- What is a CNI plugin?
- Why is a CNI required in Kubernetes?
- What is the purpose of IPAM?

---

### Intermediate

- What happens when the CNI `ADD` command is executed?
- Why does Kubernetes use a pause container?
- What is a veth pair?

---

### Advanced

- Explain the complete Pod networking lifecycle from scheduling to a running Pod.
- Compare overlay and underlay networking.
- What happens during the `DEL` operation?
- How do CNI plugins integrate with the Linux kernel?
- Why is the bridge used only for local Pod communication?

---

# References

## Official Documentation

- CNI Specification
- Kubernetes Networking
- CRI Specification
- Kubernetes Pod Lifecycle

---

## CNCF Resources

- Container Network Interface
- SIG Network
- Kubernetes Networking Guide

---

## Security & Operations

- Kubernetes Production Networking
- CIS Kubernetes Benchmark
- NIST SP 800-190

---

# Chapter Summary

```
kubectl

↓

API Server

↓

Scheduler

↓

kubelet

↓

Container Runtime

↓

CNI ADD

↓

Network Namespace

↓

veth Pair

↓

IPAM

↓

Routes

↓

Pod Ready
```

The **Container Network Interface (CNI)** is the networking engine behind every Kubernetes Pod. It creates network namespaces, assigns IP addresses, configures interfaces and routing, and connects Pods to the cluster network. By following the standardized CNI specification, Kubernetes can support multiple networking implementations while providing consistent Pod-to-Pod communication across the cluster.

Topics include:

- Calico Architecture
- Felix
- Typha
- BGP
- VXLAN
- IP-in-IP
- eBPF Mode
- Network Policy Enforcement
- Production Deployment
- Troubleshooting
- Hands-on Labs

---