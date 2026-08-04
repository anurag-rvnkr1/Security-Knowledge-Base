# Chapter 26 – Gateway API

## Overview

The **Gateway API** is the next-generation Kubernetes networking API designed to overcome many of the limitations of the traditional **Ingress** resource.

While **Ingress** is primarily focused on HTTP/HTTPS routing, the Gateway API provides a **more expressive, extensible, and role-oriented model** for managing network traffic.

It supports:

- HTTP
- HTTPS
- TCP
- UDP
- TLS
- gRPC
- Advanced traffic routing
- Multi-team environments
- Multi-cluster deployments (implementation dependent)

> **Gateway API is developed by the Kubernetes SIG Network community and is intended to complement and, over time, replace many Ingress use cases.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Gateway API is
- Why Gateway API was introduced
- Gateway API Architecture
- GatewayClass
- Gateway
- HTTPRoute
- TCPRoute
- TLSRoute
- Reference Grants
- Traffic Flow
- Gateway API vs Ingress
- Best Practices

---

# Why Was Gateway API Introduced?

Traditional Ingress works well for simple applications.

Example:

```
Internet

↓

Ingress

↓

Service

↓

Pods
```

However, Ingress has limitations:

- Limited routing capabilities
- Mostly HTTP/HTTPS focused
- Vendor-specific annotations
- Difficult multi-team management
- Limited protocol support
- Controller-specific behavior

---

# Solution

Gateway API introduces dedicated resources for:

- Infrastructure administrators
- Platform teams
- Application developers

Each team manages only its responsibilities.

---

# Gateway API Architecture

```
                    Internet

                        │

                        ▼

                  GatewayClass

                        │

                        ▼

                    Gateway

                        │

         ┌──────────────┼──────────────┐

         ▼              ▼              ▼

     HTTPRoute      TCPRoute      TLSRoute

         │              │              │

         ▼              ▼              ▼

      Services       Services      Services

         ▼              ▼              ▼

        Pods           Pods          Pods
```

---

# Core Components

Gateway API consists of:

```
GatewayClass

↓

Gateway

↓

Routes

↓

Services

↓

Pods
```

---

# GatewayClass

A **GatewayClass** defines:

- Which Gateway implementation should be used
- Controller responsible for Gateways
- Infrastructure-specific configuration

Think of it as:

```
StorageClass

↓

Persistent Volume

```

Similarly:

```
GatewayClass

↓

Gateway
```

---

# Example

```yaml
kind: GatewayClass
```

Controller example:

```
nginx

↓

Gateway Controller
```

---

# Gateway

A **Gateway** represents the actual networking infrastructure.

Examples:

- External Load Balancer
- Internal Load Balancer
- Reverse Proxy
- API Gateway

Think of it as:

```
Real Entry Point
```

---

# Gateway Architecture

```
Internet

↓

Gateway

↓

Routes

↓

Services
```

Unlike Ingress:

The Gateway is a dedicated resource separate from routing rules.

---

# HTTPRoute

An **HTTPRoute** defines:

- Hostnames
- URL paths
- Header matching
- Backend Services

Example:

```
HTTPRoute

↓

Frontend Service
```

---

# TCPRoute

Used for:

- Databases
- TCP Applications
- Message Brokers
- SSH
- Custom TCP Protocols

Architecture:

```
TCP

↓

Gateway

↓

TCPRoute

↓

Backend
```

---

# TLSRoute

Supports:

- TLS passthrough
- Secure backend routing

Example:

```
TLS

↓

Gateway

↓

TLSRoute

↓

Backend
```

---

# UDPRoute

Some Gateway implementations support:

```
UDP

↓

Gateway

↓

Backend
```

Useful for:

- DNS
- Streaming
- Gaming
- Custom UDP services

---

# Route Attachment

Routes connect to Gateways.

```
Gateway

↓

Attach Route

↓

Traffic Enabled
```

Multiple Routes can share the same Gateway.

---

# Host-Based Routing

```
api.company.com

↓

API Service
```

```
shop.company.com

↓

Shop Service
```

---

# Path-Based Routing

```
example.com/api

↓

Backend
```

```
example.com/shop

↓

Frontend
```

---

# Header Matching

Gateway API supports matching on:

```
HTTP Header

↓

Specific Service
```

Example:

```
Version: v2

↓

Canary Deployment
```

---

# Traffic Splitting

Gateway API supports weighted routing.

Example:

```
90%

↓

Version 1
```

```
10%

↓

Version 2
```

Useful for:

- Canary releases
- Progressive delivery
- A/B testing

---

# ReferenceGrant

Security feature.

Allows:

```
Namespace A

↓

Access

↓

Namespace B
```

Only when explicitly permitted.

Prevents unauthorized cross-namespace references.

---

# Gateway API Workflow

```
Internet

↓

Gateway

↓

HTTPRoute

↓

Service

↓

Pods
```

---

# Example Resources

```
GatewayClass

↓

Gateway

↓

HTTPRoute

↓

Service

↓

Pods
```

---

# Gateway API vs Ingress

| Ingress | Gateway API |
|----------|-------------|
| Single Resource | Multiple Specialized Resources |
| Limited Routing | Advanced Routing |
| Mostly HTTP | HTTP, TCP, TLS, UDP |
| Vendor Annotations | Standardized API |
| Simpler | More Flexible |

---

# Gateway vs Ingress

Ingress:

```
One Object

↓

Everything
```

Gateway API:

```
GatewayClass

↓

Gateway

↓

Routes
```

Responsibilities are clearly separated.

---

# Multi-Team Architecture

Infrastructure Team:

```
GatewayClass
```

Platform Team:

```
Gateway
```

Application Team:

```
HTTPRoute
```

Each team manages only its own resources.

---

# Viewing Gateway Resources

View GatewayClasses:

```bash
kubectl get gatewayclass
```

---

View Gateways:

```bash
kubectl get gateway
```

---

View HTTPRoutes:

```bash
kubectl get httproute
```

---

Describe Gateway:

```bash
kubectl describe gateway web-gateway
```

---

# Important kubectl Commands

View GatewayClasses:

```bash
kubectl get gatewayclass
```

View Gateways:

```bash
kubectl get gateway
```

View Routes:

```bash
kubectl get httproute
```

Delete Gateway:

```bash
kubectl delete gateway web-gateway
```

---

# Gateway API Architecture Summary

```
Internet

↓

Gateway

↓

Routes

↓

Services

↓

Pods
```

---

# Best Practices

### 1. Separate Infrastructure and Application Ownership

Use:

- GatewayClass for infrastructure
- Gateway for entry points
- Routes for application teams

---

### 2. Use Gateway API for New Deployments

When supported by your Kubernetes platform, Gateway API provides a richer and more standardized networking model than traditional Ingress.

---

### 3. Minimize Cross-Namespace Access

Use `ReferenceGrant` only where necessary.

---

### 4. Prefer Weighted Routing for Deployments

Leverage Gateway API features for:

- Canary releases
- Blue/Green deployments
- Gradual rollouts

---

### 5. Use TLS Everywhere

Terminate or pass through encrypted traffic appropriately.

---

