# Chapter 28 – DNS in Kubernetes

## Overview

Imagine a Kubernetes cluster with hundreds of Pods.

Every Pod has its own IP address.

Example:

```
Frontend

↓

10.244.1.5
```

```
Backend

↓

10.244.2.18
```

```
Database

↓

10.244.3.22
```

Pods are **ephemeral**.

When a Pod is recreated:

```
Old Pod

↓

Deleted
```

```
New Pod

↓

10.244.7.45
```

The IP changes.

If applications communicate using Pod IPs, they would constantly break.

**DNS solves this problem.**

Instead of remembering IP addresses, applications communicate using **Service names**.

Example:

```
Frontend

↓

database

↓

CoreDNS

↓

10.96.18.20
```

Kubernetes automatically resolves names into IP addresses.

---

# Learning Objectives

After completing this chapter, you will understand:

- Why Kubernetes DNS exists
- CoreDNS Architecture
- Service Discovery
- DNS Resolution
- Pod DNS
- Service DNS
- FQDN (Fully Qualified Domain Name)
- DNS Policies
- DNS Configuration
- Best Practices

---

# Why Kubernetes DNS?

Without DNS:

```
Frontend

↓

10.244.1.18
```

If Backend Pod restarts:

```
10.244.1.18

↓

10.244.5.91
```

Application fails.

---

## Better Solution

```
Frontend

↓

backend.default.svc.cluster.local
```

DNS automatically resolves the correct Service IP.

---

# What is CoreDNS?

**CoreDNS** is the default DNS server in Kubernetes.

Responsibilities:

- Service discovery
- Name resolution
- Internal DNS
- External DNS forwarding
- Kubernetes API integration

CoreDNS runs as Pods inside the cluster.

---

# High-Level Architecture

```
                Application

                      │

                      ▼

                 DNS Request

                      │

                      ▼

                   CoreDNS

                      │

            ┌─────────┼─────────┐

            ▼         ▼         ▼

        Services   Pods*   External DNS

            │

            ▼

        ClusterIP
```

> *Pod DNS records are available in specific scenarios (for example, StatefulSets and headless Services), but Service-based discovery is the standard approach.

---

# DNS Workflow

```
Application

↓

backend

↓

CoreDNS

↓

ClusterIP

↓

Backend Pods
```

---

# Kubernetes DNS Components

```
DNS

│

├── CoreDNS

├── kubelet

├── DNS Policy

├── resolv.conf

└── Services
```

---

# Service Discovery

Suppose:

```
Backend Service

↓

ClusterIP

↓

10.96.25.18
```

Application uses:

```
backend
```

instead of:

```
10.96.25.18
```

---

# DNS Resolution Process

```
Application

↓

DNS Query

↓

CoreDNS

↓

Service

↓

ClusterIP

↓

Response
```

---

# Service Name

Example:

```
backend
```

Inside the same namespace:

```
backend

↓

Resolved
```

No additional domain is required.

---

# Namespace-Aware DNS

Suppose:

Namespace:

```
production
```

Service:

```
backend
```

DNS:

```
backend.production
```

Applications in other namespaces can use namespace-qualified names.

---

# Fully Qualified Domain Name (FQDN)

Every Service has a complete DNS name.

Format:

```
service.namespace.svc.cluster.local
```

Example:

```
backend.default.svc.cluster.local
```

---

# DNS Name Structure

```
backend

↓

default

↓

svc

↓

cluster.local
```

Meaning:

```
Service

↓

Namespace

↓

Service Domain

↓

Cluster Domain
```

---

# Cluster Domain

Default:

```
cluster.local
```

Some organizations customize the cluster domain during cluster setup.

---

# Service DNS Example

Service:

```
payment
```

Namespace:

```
finance
```

FQDN:

```
payment.finance.svc.cluster.local
```

---

# DNS Search Domains

Pods automatically receive search domains.

Example:

```
default.svc.cluster.local

svc.cluster.local

cluster.local
```

This allows:

```
backend
```

instead of the full FQDN when communicating within the cluster.

---

# DNS Search Example

Application:

```
database
```

Resolver tries:

```
database.default.svc.cluster.local
```

If found:

```
Return ClusterIP
```

---

# Pod DNS Policy

Common DNS policies:

```
ClusterFirst
```

```
Default
```

```
ClusterFirstWithHostNet
```

```
None
```

The default for most Pods is:

```
ClusterFirst
```

---

# ClusterFirst

```
Application

↓

CoreDNS

↓

Internal Service?
```

If yes:

```
Cluster DNS
```

Otherwise:

```
Forward

↓

External DNS
```

---

# Default Policy

Uses the Node's DNS configuration instead of cluster-first behavior.

---

# None

Allows custom DNS configuration.

Example:

```yaml
dnsPolicy: None
```

Must be used with `dnsConfig`.

---

# dnsConfig

Example:

```yaml
dnsConfig:

  nameservers:

  - 8.8.8.8
```

Allows additional DNS customization such as nameservers, search domains, and resolver options.

---

# External DNS Lookup

Suppose:

```
google.com
```

CoreDNS:

```
↓

External DNS

↓

Response
```

CoreDNS forwards unknown domains to upstream DNS servers.

---

# Service Discovery Example

```
Frontend

↓

backend

↓

CoreDNS

↓

10.96.20.8

↓

Backend Pods
```

---

# Headless Service DNS

Normal Service:

```
backend

↓

ClusterIP
```

Headless Service:

```
backend

↓

Pod A

↓

Pod B

↓

Pod C
```

CoreDNS returns Pod IPs directly because there is no ClusterIP.

This is commonly used with StatefulSets.

---

# StatefulSet DNS

Example:

```
mysql-0.mysql.default.svc.cluster.local
```

```
mysql-1.mysql.default.svc.cluster.local
```

Each Pod receives a stable DNS name.

---

# Internal Architecture

```
Application

↓

Resolver

↓

CoreDNS

↓

Kubernetes API

↓

Service

↓

ClusterIP
```

CoreDNS watches the Kubernetes API to maintain up-to-date DNS records.

---

# Viewing CoreDNS

```bash
kubectl get pods -n kube-system
```

Example:

```
coredns
```

---

# View CoreDNS Service

```bash
kubectl get svc -n kube-system
```

Observe the ClusterIP used by Pods for DNS queries.

---

# View DNS Configuration

Inside a Pod:

```bash
cat /etc/resolv.conf
```

Typical output contains:

- nameserver
- search domains
- resolver options

---

# Important kubectl Commands

View CoreDNS Pods:

```bash
kubectl get pods -n kube-system
```

View Services:

```bash
kubectl get svc -n kube-system
```

View DNS Config:

```bash
kubectl exec -it <pod> -- cat /etc/resolv.conf
```

Test DNS:

```bash
kubectl exec -it <pod> -- nslookup kubernetes.default
```

---

# Kubernetes DNS Architecture

```
Application

↓

DNS Query

↓

CoreDNS

↓

Kubernetes API

↓

Service

↓

ClusterIP

↓

Response
```

---

# Best Practices

### 1. Always Use Service Names

Prefer:

```
database
```

instead of:

```
10.96.20.5
```

---

### 2. Avoid Pod IPs

Pod IPs are temporary.

Services provide stable endpoints.

---

### 3. Use FQDN for Cross-Namespace Communication

Example:

```
database.finance.svc.cluster.local
```

---

### 4. Keep CoreDNS Healthy

Monitor:

- Pod status
- CPU usage
- Memory usage
- DNS latency

---

### 5. Test DNS During Troubleshooting

A simple `nslookup` or `dig` from inside a Pod can quickly identify name resolution issues.

---

