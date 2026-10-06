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

# How DNS Works Internally in Kubernetes

## Overview

When an application inside Kubernetes communicates with another application, it almost never uses an IP address directly.

Instead, it performs a **DNS lookup**.

For example:

```
Frontend

↓

database
```

The application does **not** know the database Pod IP.

Instead, Kubernetes automatically resolves:

```
database.default.svc.cluster.local

↓

10.96.18.25
```

This process happens in milliseconds and involves several Kubernetes components.

---

# Learning Objectives

After completing this chapter, you will understand:

- Internal DNS architecture
- CoreDNS internals
- DNS packet flow
- Service discovery
- CoreDNS plugins
- Kubernetes API integration
- DNS cache
- External DNS forwarding
- FQDN resolution
- DNS troubleshooting

---

# High-Level Architecture

```
                Application

                      │

                      ▼

               libc Resolver

                      │

                      ▼

               /etc/resolv.conf

                      │

                      ▼

                  CoreDNS

                      │

          ┌───────────┼───────────┐

          ▼           ▼           ▼

      Kubernetes   External DNS  Cache

          │

          ▼

      ClusterIP

          ▼

      Backend Pods
```

---

# Complete Workflow

```
Application

↓

DNS Query

↓

Resolver

↓

CoreDNS

↓

Kubernetes API

↓

ClusterIP

↓

Application Connects
```

---

# Step 1 – Application Requests Service

Suppose:

```bash
curl http://database
```

Application:

```
database
```

No IP address is provided.

---

# Step 2 – libc Resolver

Linux applications use the system resolver library.

Workflow:

```
Application

↓

libc

↓

DNS Query
```

The resolver reads:

```
/etc/resolv.conf
```

---

# Step 3 – resolv.conf

Example:

```text
nameserver 10.96.0.10

search default.svc.cluster.local svc.cluster.local cluster.local

options ndots:5
```

Meaning:

- **nameserver** → CoreDNS Service IP
- **search** → DNS search domains
- **ndots** → Controls when search domains are applied

---

# Step 4 – DNS Search

Application requests:

```
database
```

Resolver tries:

```
database.default.svc.cluster.local
```

If not found:

```
database.svc.cluster.local
```

Then:

```
database.cluster.local
```

---

# Step 5 – CoreDNS Receives Query

Packet:

```
UDP 53

↓

CoreDNS
```

Most DNS requests use UDP port **53**.

TCP is used when responses are large or UDP retries fail.

---

# CoreDNS Architecture

```
CoreDNS

│

├── kubernetes Plugin

├── cache Plugin

├── forward Plugin

├── health Plugin

├── ready Plugin

└── prometheus Plugin
```

CoreDNS functionality is built using plugins.

---

# Kubernetes Plugin

The Kubernetes plugin watches:

- Services
- EndpointSlices
- Namespaces
- Pods (where applicable)

Example:

```
Service Created

↓

API Server

↓

CoreDNS Updated
```

No manual configuration is required.

---

# Step 6 – Service Lookup

CoreDNS searches:

```
database.default
```

Finds:

```
ClusterIP

↓

10.96.18.25
```

---

# Step 7 – DNS Response

CoreDNS sends:

```
database

↓

10.96.18.25
```

Back to the application.

---

# Step 8 – Application Connects

Application now sends packets to:

```
10.96.18.25
```

Traffic continues through:

```
ClusterIP

↓

EndpointSlice

↓

Backend Pod
```

---

# Complete Packet Flow

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

EndpointSlice

↓

Pod
```

---

# CoreDNS Cache

CoreDNS caches DNS records.

Example:

```
database

↓

Cache

↓

Response
```

Benefits:

- Faster lookups
- Lower API Server load
- Reduced latency

---

# External DNS

Suppose:

```
google.com
```

CoreDNS:

```
↓

Forward Plugin

↓

Upstream DNS

↓

Response
```

CoreDNS acts as a DNS forwarder for external domains.

---

# CoreDNS Plugins

## Kubernetes Plugin

```
Internal DNS
```

---

## Cache Plugin

```
DNS Cache
```

---

## Forward Plugin

```
External DNS
```

---

## Health Plugin

```
Health Checks
```

---

## Ready Plugin

```
Readiness Endpoint
```

---

## Prometheus Plugin

```
Metrics
```

---

# DNS Cache Flow

```
Application

↓

Cache Hit?

↓

Yes

↓

Return Result
```

Otherwise:

```
CoreDNS

↓

API Lookup
```

---

# Service Discovery

Suppose:

```
Backend

↓

ClusterIP

↓

10.96.18.20
```

Application:

```
backend
```

DNS:

```
↓

10.96.18.20
```

---

# Headless Service

Normal Service:

```
database

↓

10.96.x.x
```

Headless Service:

```
database

↓

10.244.1.8

10.244.2.5

10.244.3.4
```

CoreDNS returns Pod IPs directly.

---

# StatefulSet Example

```
mysql-0.mysql.default.svc.cluster.local
```

```
mysql-1.mysql.default.svc.cluster.local
```

Each Pod has a predictable DNS identity.

---

# EndpointSlice Integration

Service:

```
database
```

↓

```
EndpointSlice
```

↓

```
Pod A

Pod B

Pod C
```

CoreDNS provides the Service record.

kube-proxy handles load balancing to the endpoints.

---

# DNS TTL

DNS responses include a **Time To Live (TTL)** value.

```
Response

↓

Cache

↓

Expire

↓

Refresh
```

The TTL determines how long DNS responses may be cached before a new lookup is required.

---

# Internal Architecture

```
Application

↓

Resolver

↓

CoreDNS

↓

API Server

↓

Service

↓

ClusterIP

↓

Pod
```

---

# DNS Resolution Example

Request:

```bash
nslookup backend
```

Result:

```
Name:

backend.default.svc.cluster.local

Address:

10.96.18.25
```

---

# Troubleshooting DNS

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

---

Check Service:

```bash
kubectl get svc -n kube-system
```

---

Check DNS:

```bash
kubectl exec -it busybox -- nslookup kubernetes.default
```

---

Check Resolver:

```bash
kubectl exec -it busybox -- cat /etc/resolv.conf
```

---

# Hands-on Lab 1 – Create BusyBox Pod

```bash
kubectl run dns-test \
--image=busybox \
-it --rm --restart=Never -- sh
```

---

# Hands-on Lab 2 – Test Service Lookup

Inside BusyBox:

```bash
nslookup kubernetes.default
```

Observe the returned ClusterIP.

---

# Hands-on Lab 3 – Test External DNS

```bash
nslookup google.com
```

Verify that CoreDNS forwards external queries.

---

# Hands-on Lab 4 – Inspect Resolver

```bash
cat /etc/resolv.conf
```

Observe:

- nameserver
- search domains
- ndots

---

# Hands-on Lab 5 – Verify CoreDNS

```bash
kubectl get pods -n kube-system
```

Ensure CoreDNS Pods are running.

---

# Common Mistakes

## 1. Using Pod IPs Instead of Services

Incorrect:

```
10.244.x.x
```

Correct:

```
database
```

or

```
database.default.svc.cluster.local
```

---

## 2. Assuming CoreDNS Knows Static Records

CoreDNS dynamically watches Kubernetes resources.

Records change automatically as Services and EndpointSlices change.

---

## 3. Ignoring Search Domains

Within the same namespace:

```
database
```

is usually sufficient.

Across namespaces, use:

```
database.finance
```

or the full FQDN.

---

## 4. Forgetting CoreDNS Health

If CoreDNS Pods fail:

```
DNS

↓

Unavailable

↓

Applications Fail
```

Even healthy applications may become unreachable because names cannot be resolved.

---

## 5. Confusing DNS with Load Balancing

CoreDNS:

```
Resolves Names
```

kube-proxy:

```
Routes Traffic
```

They perform different functions.

---

# DNS Quick Revision

## Resolution Flow

```
Application

↓

Resolver

↓

CoreDNS

↓

Service

↓

ClusterIP
```

---

## External Query

```
Application

↓

CoreDNS

↓

Forward Plugin

↓

Internet DNS
```

---

## Internal Query

```
Application

↓

CoreDNS

↓

Kubernetes Plugin

↓

ClusterIP
```

---

# Essential kubectl Commands

View CoreDNS:

```bash
kubectl get pods -n kube-system
```

View CoreDNS Service:

```bash
kubectl get svc -n kube-system
```

Test DNS:

```bash
kubectl exec -it dns-test -- nslookup kubernetes.default
```

Inspect Resolver:

```bash
kubectl exec -it dns-test -- cat /etc/resolv.conf
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

---

# Interview Questions

### Basic

- What is CoreDNS?
- Why does Kubernetes use DNS?
- What is an FQDN?

---

### Intermediate

- How does CoreDNS discover Services?
- What is the purpose of `/etc/resolv.conf`?
- What is the difference between Service DNS and Pod DNS?

---

### Advanced

- Explain the complete DNS resolution process in Kubernetes.
- What is the role of the Kubernetes plugin in CoreDNS?
- How does CoreDNS forward external DNS queries?
- Why are EndpointSlices important even though CoreDNS returns a ClusterIP?
- How does `ndots` affect DNS resolution?

---

# References

## Official Kubernetes Documentation

- DNS for Services and Pods
- CoreDNS
- Service Discovery
- EndpointSlices

---

## CNCF Resources

- Kubernetes Networking
- CoreDNS Documentation
- SIG Network
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- Kubernetes Production Networking
- CIS Kubernetes Benchmark
- NIST SP 800-190
- CoreDNS Metrics & Monitoring

---

## Recommended Practice

1. Deploy multiple Services and resolve them using short names and FQDNs.
2. Explore `/etc/resolv.conf` inside Pods.
3. Test both internal and external DNS resolution.
4. Create a headless Service and compare DNS responses.
5. Observe CoreDNS logs while generating DNS traffic.
6. Simulate CoreDNS failures in a lab and practice troubleshooting.
7. Monitor CoreDNS metrics using Prometheus.

---

# Chapter Summary

```
Application

↓

libc Resolver

↓

/etc/resolv.conf

↓

CoreDNS

↓

Kubernetes Plugin

↓

ClusterIP

↓

kube-proxy

↓

EndpointSlice

↓

Backend Pod
```

DNS is the **foundation of service discovery** in Kubernetes. **CoreDNS** watches the Kubernetes API to dynamically maintain DNS records, allowing applications to communicate using stable Service names instead of changing IP addresses. Combined with **ClusterIP**, **EndpointSlices**, and **kube-proxy**, it provides reliable and scalable name resolution for modern cloud-native applications.

---
