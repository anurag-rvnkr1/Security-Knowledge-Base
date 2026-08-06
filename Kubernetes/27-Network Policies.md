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

## Next Section

How Network Policies Work Internally

CNI Enforcement

Packet Flow

Ingress vs Egress Processing

Hands-on Labs

Common Mistakes

Quick Revision

References

---