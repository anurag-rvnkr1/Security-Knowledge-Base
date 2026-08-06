# Chapter 27 – Network Policies

## Overview

By default, Kubernetes follows an **allow-all** networking model.

This means:

- Every Pod can communicate with every other Pod.
- Pods can usually access external networks.
- Any Pod can send traffic to any Service.

For small clusters, this may be acceptable.

However, in **production environments**, unrestricted communication introduces significant security risks.

**Network Policies** allow you to control how Pods communicate with:

- Other Pods
- Namespaces
- External IP addresses
- The Internet

They function similarly to **firewall rules** for Kubernetes Pods.

> **Important:** Network Policies only work if your cluster's CNI plugin supports them (for example, Calico, Cilium, Antrea, or Weave Net with policy support).

---

# Learning Objectives

After completing this chapter, you will understand:

- What Network Policies are
- Why Network Policies are important
- Network Policy Architecture
- Ingress Rules
- Egress Rules
- Pod Selectors
- Namespace Selectors
- IP Blocks
- Policy Types
- Default Deny Model
- Best Practices

---

# Why Do We Need Network Policies?

Imagine an e-commerce application.

```
Frontend

↓

Backend

↓

Database
```

Without Network Policies:

```
Frontend

↓

Database
```

Allowed.

```
Random Pod

↓

Database
```

Also allowed.

This violates the **Principle of Least Privilege**.

---

# Solution

Use Network Policies.

```
Frontend

↓

Backend

↓

Database
```

Only approved communication is permitted.

---

# High-Level Architecture

```
                  Namespace

     ┌─────────────────────────────────┐

     │                                 │

     │  Frontend Pod                   │

     │         │                       │

     │         ▼                       │

     │    Backend Pod                  │

     │         │                       │

     │         ▼                       │

     │    Database Pod                 │

     │                                 │

     └─────────────────────────────────┘

          ▲                 ▲

          │                 │

      Allowed         Blocked

          │                 │

      Network Policy
```

---

# What is a Network Policy?

A Network Policy defines **which traffic is allowed** to or from selected Pods.

It does **not** define blocked traffic directly.

Instead:

```
Allowed Traffic

↓

Everything Else

↓

Denied
```

---

# Network Policy Components

```
Network Policy

│

├── Pod Selector

├── Policy Types

├── Ingress Rules

├── Egress Rules

└── Peers
```

---

# Pod Selector

A Network Policy targets Pods using labels.

Example:

```yaml
podSelector:

  matchLabels:

    app: backend
```

Applies only to:

```
Backend Pods
```

---

# Policy Types

Two primary policy types exist:

```
Ingress
```

and

```
Egress
```

A policy may define one or both.

---

# Ingress Policy

Controls:

```
Incoming Traffic

↓

Selected Pod
```

Example:

```
Frontend

↓

Backend

Allowed
```

```
Random Pod

↓

Backend

Denied
```

---

# Egress Policy

Controls:

```
Outgoing Traffic

↓

Destination
```

Example:

```
Backend

↓

Database

Allowed
```

```
Backend

↓

Internet

Denied
```

---

# Ingress vs Egress

| Ingress | Egress |
|----------|---------|
| Incoming traffic | Outgoing traffic |
| Controls who can reach a Pod | Controls where a Pod can connect |

---

# Default Behavior

Without Network Policies:

```
All Traffic

↓

Allowed
```

Once a Pod is selected by a Network Policy:

```
Only Explicitly Allowed Traffic

↓

Permitted
```

---

# Default Deny

A common security practice:

```
Everything

↓

Denied
```

Then:

```
Required Traffic

↓

Allowed
```

---

# Default Deny Example

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: default-deny

spec:

  podSelector: {}

  policyTypes:

  - Ingress
```

This denies all ingress traffic to Pods in the namespace unless another policy explicitly allows it.

---

# Allow Frontend to Backend

Example:

```
Frontend

↓

Backend

Allowed
```

All other Pods:

```
↓

Backend

Denied
```

---

# Namespace Selector

Traffic can also be allowed based on namespaces.

Example:

```yaml
namespaceSelector:

  matchLabels:

    team: production
```

Only Pods in matching namespaces are permitted.

---

# Pod Selector + Namespace Selector

Both can be combined.

```
Namespace

↓

Pod

↓

Allowed
```

This provides fine-grained access control.

---

# IP Block

External IPs can also be allowed.

Example:

```yaml
ipBlock:

  cidr: 192.168.1.0/24
```

Meaning:

```
Only

192.168.1.x

Allowed
```

---

# Excluding Addresses

Example:

```yaml
except:

- 192.168.1.50/32
```

Meaning:

```
Entire Network

↓

Allowed

Except

↓

192.168.1.50
```

---

# Port Restrictions

Policies can also limit ports.

Example:

```yaml
ports:

- protocol: TCP

  port: 443
```

Only HTTPS traffic is permitted.

---

# Multiple Rules

A Network Policy may contain multiple ingress or egress rules.

```
Rule 1

OR

Rule 2

OR

Rule 3
```

If any rule matches, the traffic is allowed.

---

# Example Architecture

```
Internet

↓

Ingress

↓

Frontend

↓

Backend

↓

Database
```

Allowed:

```
Frontend

↓

Backend
```

```
Backend

↓

Database
```

Denied:

```
Frontend

↓

Database
```

---

# Network Policy Workflow

```
Packet

↓

Network Policy

↓

Allowed?

↓

Yes

↓

Forward
```

```
Packet

↓

Network Policy

↓

No Match

↓

Drop
```

---

# YAML Example

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: allow-frontend

spec:

  podSelector:

    matchLabels:

      app: backend

  policyTypes:

  - Ingress

  ingress:

  - from:

    - podSelector:

        matchLabels:

          app: frontend
```

---

# Common Use Cases

### Secure Databases

```
Backend

↓

Database

Allowed
```

Others:

```
Denied
```

---

### Restrict Internet Access

```
Pod

↓

Internet

Denied
```

---

### Namespace Isolation

```
Namespace A

↓

Namespace B

Denied
```

---

### Microservice Security

```
Frontend

↓

Backend

↓

Database
```

Only the required paths are allowed.

---

# Viewing Policies

```bash
kubectl get networkpolicy
```

---

# Describe Policy

```bash
kubectl describe networkpolicy allow-frontend
```

Displays:

- Pod selectors
- Policy types
- Allowed peers
- Allowed ports

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f networkpolicy.yaml
```

View:

```bash
kubectl get networkpolicy
```

Describe:

```bash
kubectl describe networkpolicy allow-frontend
```

Delete:

```bash
kubectl delete networkpolicy allow-frontend
```

---

# Network Policy Architecture Summary

```
Source Pod

↓

Network Policy

↓

Allowed?

↓

Destination Pod
```

---

# Best Practices

### 1. Start with Default Deny

Deny all traffic first.

Then explicitly allow only required communication.

---

### 2. Use Labels Carefully

Policies depend on accurate Pod labels.

---

### 3. Apply Least Privilege

Allow only:

- Required Pods
- Required Namespaces
- Required Ports

---

### 4. Test Before Production

Incorrect policies can accidentally isolate applications.

---

### 5. Verify CNI Support

Ensure your CNI plugin enforces Network Policies.

---

# How Network Policies Work Internally

## Overview

A **Network Policy** is only a Kubernetes API resource.

By itself, it **does not block or allow traffic**.

Instead:

1. The Network Policy is stored in the Kubernetes API Server.
2. The **Container Network Interface (CNI)** plugin watches for NetworkPolicy objects.
3. The CNI converts the policy into low-level networking rules.
4. The Linux kernel enforces those rules when packets are transmitted.

The actual enforcement depends on the networking implementation.

Examples:

- Calico → iptables, nftables, or eBPF
- Cilium → eBPF
- Antrea → Open vSwitch
- Weave Net → iptables

> Kubernetes defines **what** the policy is. The CNI plugin determines **how** it is enforced.

---

# High-Level Architecture

```
                Kubernetes API Server

                        │

                        ▼

                 NetworkPolicy Object

                        │

                        ▼

                 CNI Plugin Watches

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

      Calico        Cilium        Antrea

                        │

                        ▼

             Linux Networking Stack

                        │

                        ▼

              Packet Allow / Deny
```

---

# Complete Internal Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

NetworkPolicy

↓

CNI Plugin

↓

Kernel Rules

↓

Packet Inspection

↓

Allow / Drop
```

---

# Step 1 – Create Network Policy

Example:

```yaml
kind: NetworkPolicy
```

Deploy:

```bash
kubectl apply -f policy.yaml
```

---

# Step 2 – API Server

The API Server:

- Validates the policy
- Stores it in etcd

```
kubectl

↓

API Server

↓

NetworkPolicy Stored
```

No packet filtering occurs yet.

---

# Step 3 – CNI Watches Policies

The CNI plugin continuously watches:

- Pods
- Namespaces
- Labels
- NetworkPolicies

Whenever a policy changes:

```
Policy Updated

↓

CNI

↓

Recalculate Rules
```

---

# Step 4 – Identify Target Pods

Suppose:

```yaml
podSelector:

  matchLabels:

    app: database
```

The CNI identifies all Pods matching:

```
app=database
```

Only these Pods are affected.

---

# Step 5 – Build Rule Set

Suppose:

```
Frontend

↓

Database

Allowed
```

Rules become:

```
Allow

↓

Frontend

↓

Database
```

Everything else is denied once the selected Pods are isolated.

---

# Step 6 – Program Linux Networking

Depending on the CNI:

```
Calico

↓

iptables / nftables / eBPF
```

```
Cilium

↓

eBPF
```

```
Antrea

↓

Open vSwitch
```

The operating system now enforces the policy.

---

# Packet Flow

Suppose:

```
Frontend

↓

Database
```

Packet:

```
Application

↓

Kernel

↓

Network Policy Check

↓

Allowed?

↓

Forward
```

If no rule allows the packet:

```
Application

↓

Kernel

↓

Policy Check

↓

Denied

↓

Drop Packet
```

---

# Ingress Processing

Example:

```
Frontend

↓

Database
```

Policy:

```
Allow

↓

Frontend
```

Traffic:

```
Accepted
```

Random Pod:

```
↓

Database
```

Result:

```
Dropped
```

---

# Egress Processing

Suppose:

```
Backend

↓

Database
```

Allowed.

```
Backend

↓

Internet
```

Denied.

The CNI evaluates outgoing packets before they leave the Pod.

---

# Pod Isolation

Once a Pod is selected by an ingress policy:

```
Pod

↓

Isolated
```

Only explicitly allowed ingress traffic is accepted.

Similarly, an egress policy isolates outgoing traffic.

---

# Default Deny

Example:

```
Network Policy

↓

No Allow Rules
```

Result:

```
All Traffic

↓

Denied
```

This is commonly used as the foundation of Zero Trust networking.

---

# Policy Evaluation

Multiple Network Policies can select the same Pod.

```
Policy A

OR

Policy B

OR

Policy C
```

If **any policy allows** the traffic:

```
Traffic

↓

Allowed
```

There is **no explicit "deny" rule** in Kubernetes Network Policies.

Denied traffic is simply traffic that does not match any allow rule.

---

# Example Evaluation

Policies:

```
Policy 1

↓

Allow Frontend
```

```
Policy 2

↓

Allow Monitoring
```

Traffic:

```
Frontend

↓

Allowed
```

```
Prometheus

↓

Allowed
```

```
Random Pod

↓

Denied
```

---

# Namespace Selector Processing

Suppose:

```yaml
namespaceSelector:

  matchLabels:

    team: production
```

CNI evaluates:

```
Source Namespace

↓

team=production?

↓

Yes

↓

Allow
```

---

# Pod Selector Processing

Suppose:

```yaml
podSelector:

  matchLabels:

    app: frontend
```

Packet:

```
Source Pod

↓

Label Match?

↓

Yes

↓

Continue
```

---

# IP Block Processing

Example:

```yaml
cidr:

10.10.0.0/16
```

Packet:

```
Source IP

↓

Inside CIDR?

↓

Allow
```

Otherwise:

```
Drop
```

---

# Port Filtering

Suppose:

```
TCP

↓

443
```

Allowed.

Packet:

```
TCP 22

↓

Denied
```

Ports are evaluated alongside selectors.

---

# Internal Architecture

```
Application

↓

Network Namespace

↓

Kernel

↓

CNI Rules

↓

Allow?

↓

Destination
```

---

# Calico Enforcement

Calico may implement policies using:

```
Network Policy

↓

Felix Agent

↓

iptables / nftables / eBPF

↓

Linux Kernel
```

Felix is Calico's policy programming component.

---

# Cilium Enforcement

Cilium uses:

```
Network Policy

↓

eBPF Program

↓

Kernel

↓

Packet Decision
```

This avoids large iptables rule sets and offers high performance.

---

# Antrea Enforcement

Antrea translates Network Policies into Open vSwitch flow rules.

```
Network Policy

↓

Open vSwitch

↓

Forward / Drop
```

---

# Packet Life Cycle

```
Application

↓

Container

↓

Pod Network Namespace

↓

veth Pair

↓

Policy Check

↓

Linux Networking

↓

Destination
```

Policy enforcement occurs before the packet leaves (egress) or after it enters (ingress), depending on direction.

---

# Zero Trust Model

```
Default Deny

↓

Explicit Allow

↓

Application Access
```

Every communication path must be intentionally permitted.

---

# Hands-on Lab 1 – Create Default Deny Policy

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: default-deny

spec:

  podSelector: {}

  policyTypes:

  - Ingress
```

Apply:

```bash
kubectl apply -f default-deny.yaml
```

Observe that ingress traffic is blocked unless additional policies allow it.

---

# Hands-on Lab 2 – Allow Frontend Access

Create a policy allowing:

```
Frontend

↓

Backend
```

Verify that only the frontend can access the backend.

---

# Hands-on Lab 3 – Test Connectivity

Launch a temporary Pod:

```bash
kubectl run tester \
--image=busybox \
-it --rm --restart=Never -- sh
```

Inside:

```bash
wget http://backend
```

Observe whether traffic is allowed or denied.

---

# Hands-on Lab 4 – Test Namespace Isolation

Create two namespaces.

Allow traffic only from one namespace using a `namespaceSelector`.

Verify that Pods in the other namespace cannot connect.

---

# Hands-on Lab 5 – Verify CNI Support

Check which CNI is running:

```bash
kubectl get pods -A
```

Look for components such as:

- calico-node
- cilium
- antrea-agent

Confirm that your CNI supports Network Policies.

---

# Common Mistakes

## 1. Assuming Kubernetes Enforces Policies

Kubernetes stores the policy.

The **CNI plugin** enforces it.

Without a compatible CNI:

```
Policy Exists

↓

No Enforcement
```

---

## 2. Forgetting Default Allow

Without any Network Policy:

```
All Traffic

↓

Allowed
```

---

## 3. Looking for "Deny" Rules

Kubernetes Network Policies only define **allow** rules.

Everything not allowed is implicitly denied for isolated Pods.

---

## 4. Incorrect Labels

Policies rely entirely on labels.

If labels do not match:

```
Policy

↓

No Effect
```

---

## 5. Ignoring DNS

A strict egress policy may accidentally block DNS requests.

Without DNS:

```
Application

↓

Cannot Resolve Services
```

Remember to allow traffic to your cluster DNS service (for example, CoreDNS) when appropriate.

---

# Network Policies Quick Revision

## Workflow

```
Developer

↓

NetworkPolicy

↓

API Server

↓

CNI Plugin

↓

Kernel Rules

↓

Packet Decision
```

---

## Evaluation

```
Packet

↓

Selector Match

↓

Port Match

↓

Allow?

↓

Forward / Drop
```

---

## Security Model

```
Default Deny

↓

Explicit Allow

↓

Least Privilege
```

---

# Essential kubectl Commands

View Policies:

```bash
kubectl get networkpolicy
```

Describe Policy:

```bash
kubectl describe networkpolicy default-deny
```

View Namespaces:

```bash
kubectl get namespaces
```

View Pod Labels:

```bash
kubectl get pods --show-labels
```

Delete Policy:

```bash
kubectl delete networkpolicy default-deny
```

---

# Interview Questions

### Basic

- What is a Network Policy?
- What is the difference between ingress and egress policies?
- Why are Network Policies not enforced by Kubernetes itself?

---

### Intermediate

- How does a CNI plugin enforce Network Policies?
- What happens when multiple Network Policies apply to the same Pod?
- Why is there no explicit deny rule?

---

### Advanced

- Explain the complete packet flow through Network Policy enforcement.
- Compare Network Policy implementations in Calico and Cilium.
- What happens if a cluster does not support Network Policies?
- How does a default-deny policy implement Zero Trust networking?
- Why must DNS be considered when writing egress policies?

---

# References

## Official Kubernetes Documentation

- Network Policies
- Network Policy Concepts
- CNI Specification
- Namespace Selectors

---

## CNCF Resources

- Kubernetes Networking
- SIG Network
- Kubernetes Security Best Practices
- Cloud Native Computing Foundation (CNCF)

---

## CNI Documentation

- Calico
- Cilium
- Antrea
- Weave Net

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Hardening Guide
- NIST SP 800-190
- Zero Trust Architecture (NIST SP 800-207)

---

## Recommended Practice

1. Apply a default-deny policy to a namespace.
2. Create allow policies for only required application communication.
3. Test Pod-to-Pod connectivity before and after applying policies.
4. Restrict egress traffic while preserving DNS resolution.
5. Experiment with namespace selectors and IP blocks.
6. Compare policy enforcement using Calico and Cilium in separate lab environments.
7. Design a Zero Trust network model for a three-tier application.

---

# Chapter Summary

```
Developer

↓

NetworkPolicy

↓

API Server

↓

CNI Plugin

↓

Linux Kernel

↓

Packet Evaluation

↓

Allow / Drop

↓

Destination Pod
```

Network Policies provide **Kubernetes-native microsegmentation** by controlling which Pods can communicate with one another and with external networks. The Kubernetes API defines the desired policy, while the **CNI plugin** translates it into low-level networking rules enforced by the operating system. Combined with a **default-deny** approach, Network Policies form a critical foundation for implementing **Zero Trust security** in Kubernetes clusters.

---

