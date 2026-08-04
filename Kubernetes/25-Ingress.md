# Chapter 25 – Ingress

## Overview

As Kubernetes applications grow, exposing each Service using its own **LoadBalancer** becomes expensive, difficult to manage, and inefficient.

Imagine a microservices application with:

- Frontend
- Backend API
- Authentication Service
- Payment Service
- Admin Portal
- Notification Service

Creating one **LoadBalancer** for each Service means:

```
6 Services

↓

6 Load Balancers

↓

6 Public IPs
```

This increases:

- Cost
- Complexity
- Operational overhead

---

## Solution

Use **Ingress**.

Ingress provides a **single entry point** into the Kubernetes cluster.

Instead of exposing every Service separately:

```
Internet

↓

Ingress

↓

Multiple Services
```

One public IP can serve many applications.

---

# Learning Objectives

After completing this chapter, you will understand:

- What Ingress is
- Why Ingress is needed
- Ingress Architecture
- Ingress Rules
- Host-Based Routing
- Path-Based Routing
- TLS Termination
- Default Backend
- Ingress vs Services
- Best Practices

---

# Why Do We Need Ingress?

Without Ingress:

```
Internet

↓

LoadBalancer A

↓

Frontend
```

```
Internet

↓

LoadBalancer B

↓

Backend
```

```
Internet

↓

LoadBalancer C

↓

Payment
```

Problems:

- Multiple public IPs
- Higher cloud cost
- Difficult certificate management
- Complicated DNS configuration

---

# Better Solution

```
Internet

↓

Ingress

↓

Frontend

↓

Backend

↓

Payment
```

One endpoint.

Multiple applications.

---

# What is Ingress?

Ingress is a Kubernetes API resource that defines **HTTP and HTTPS routing rules**.

It determines:

- Which hostname to match
- Which URL path to match
- Which Service should receive the request

Important:

> **Ingress itself does not process traffic.**

It only defines routing rules.

The actual traffic is handled by an **Ingress Controller**.

---

# High-Level Architecture

```
                   Internet

                       │

                       ▼

                Public IP Address

                       │

                       ▼

              Ingress Controller

                       │

          ┌────────────┼────────────┐

          ▼            ▼            ▼

      Frontend     Backend      Payment

       Service      Service      Service

          │            │            │

          ▼            ▼            ▼

        Pods         Pods         Pods
```

---

# Ingress Characteristics

- Layer 7 (HTTP/HTTPS)
- Host-based routing
- Path-based routing
- TLS termination
- Reverse proxy
- Load balancing
- SSL certificate support

---

# Ingress vs Service

| Ingress | Service |
|----------|----------|
| Layer 7 | Layer 4 |
| HTTP/HTTPS | TCP/UDP |
| Routes traffic | Exposes Pods |
| Uses Ingress Controller | Uses kube-proxy |

---

# Ingress Workflow

```
Client

↓

Ingress

↓

Matching Rule

↓

Service

↓

Pods
```

---

# Host-Based Routing

Example:

```
api.example.com

↓

API Service
```

```
shop.example.com

↓

Shop Service
```

```
admin.example.com

↓

Admin Service
```

Each hostname routes to a different Service.

---

# Path-Based Routing

Example:

```
example.com/

↓

Frontend
```

```
example.com/api

↓

Backend
```

```
example.com/payment

↓

Payment
```

One domain.

Multiple applications.

---

# Host + Path Routing

```
api.company.com/users

↓

User Service
```

```
api.company.com/orders

↓

Order Service
```

```
shop.company.com

↓

Shop Service
```

---

# Example Ingress YAML

```yaml
apiVersion: networking.k8s.io/v1

kind: Ingress

metadata:

  name: web-ingress

spec:

  rules:

  - host: example.com

    http:

      paths:

      - path: /

        pathType: Prefix

        backend:

          service:

            name: frontend

            port:

              number: 80
```

---

# YAML Breakdown

```
Ingress

↓

Rules

↓

Host

↓

Path

↓

Backend Service
```

---

# Path Types

Kubernetes supports:

### Prefix

```
/api

↓

/api/users

/api/orders
```

Matches everything starting with `/api`.

---

### Exact

```
/login
```

Matches only:

```
/login
```

Not:

```
/login/admin
```

---

### ImplementationSpecific

Behavior depends on the Ingress Controller implementation.

---

# Default Backend

Suppose:

```
Unknown URL
```

Example:

```
example.com/random
```

Request goes to:

```
Default Backend
```

Typically returns:

```
404 Not Found
```

---

# TLS Termination

Without TLS:

```
HTTP

↓

Ingress

↓

Service
```

With TLS:

```
HTTPS

↓

TLS Termination

↓

Ingress

↓

HTTP

↓

Service
```

The Ingress Controller decrypts HTTPS traffic before forwarding it.

---

# TLS Secret

Certificates are stored as Kubernetes Secrets.

Example:

```yaml
tls:

- hosts:

  - example.com

  secretName: tls-secret
```

---

# Multiple Domains

Example:

```
example.com

↓

Frontend
```

```
api.example.com

↓

Backend
```

```
admin.example.com

↓

Admin
```

One Ingress resource can manage multiple hosts.

---

# Reverse Proxy

Ingress functions as a reverse proxy.

```
Client

↓

Ingress

↓

Backend Service
```

The client never communicates directly with Pods.

---

# Load Balancing

Suppose:

```
Frontend Service

↓

3 Pods
```

Ingress forwards traffic to the Service, and the Service distributes traffic across backend Pods.

---

# Authentication

Many Ingress Controllers support:

- OAuth
- OpenID Connect (OIDC)
- Basic Authentication
- JWT validation

through controller-specific configuration.

---

# URL Rewrite

Example:

Incoming request:

```
/shop/products
```

Ingress can rewrite it as:

```
/products
```

before forwarding it to the backend.

---

# Rate Limiting

Ingress Controllers commonly support:

- Request throttling
- Rate limiting
- Connection limits

to protect applications.

---

# Viewing Ingress

```bash
kubectl get ingress
```

Example:

```
NAME

HOSTS

ADDRESS
```

---

# Describe Ingress

```bash
kubectl describe ingress web-ingress
```

Displays:

- Rules
- Hosts
- Paths
- Backends
- TLS configuration

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f ingress.yaml
```

View:

```bash
kubectl get ingress
```

Describe:

```bash
kubectl describe ingress web-ingress
```

Delete:

```bash
kubectl delete ingress web-ingress
```

---

# Ingress Architecture Summary

```
Internet

↓

Ingress

↓

Routing Rules

↓

Services

↓

Pods
```

---

# Best Practices

### 1. Use One Ingress for Related Applications

Group related HTTP/HTTPS routes into a single Ingress when appropriate.

---

### 2. Always Enable HTTPS

Protect traffic using TLS certificates.

---

### 3. Use Host-Based Routing

Separate applications by hostname whenever possible.

---

### 4. Keep Rules Organized

Avoid large, difficult-to-maintain Ingress definitions.

---

### 5. Use an Ingress Controller Designed for Production

Examples include:

- NGINX Ingress Controller
- HAProxy Ingress
- Traefik
- Kong
- AWS Load Balancer Controller

---

