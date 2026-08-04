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

# How Ingress Works Internally

## Overview

Many beginners think that an **Ingress** itself receives network traffic.

This is **not correct**.

An **Ingress is only a Kubernetes API object** that stores HTTP/HTTPS routing rules.

It does **not**:

- Listen on network ports
- Accept client connections
- Forward packets
- Load balance traffic

Instead, an **Ingress Controller** continuously watches the Kubernetes API Server and converts Ingress rules into the configuration required by a reverse proxy (such as NGINX, HAProxy, Traefik, or Envoy).

> **Think of an Ingress as a configuration file, while the Ingress Controller is the software that actually processes traffic.**

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

          (NGINX / Traefik / HAProxy)

                        │

                        ▼

              Read Ingress Rules

                        │

                        ▼

                   ClusterIP Service

                        │

                  EndpointSlice

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

       Pod A         Pod B         Pod C
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

Ingress Object

↓

Ingress Controller

↓

Generate Proxy Rules

↓

Reload Configuration

↓

Client Traffic

↓

Backend Service
```

---

# Step 1 – Create Ingress

Example:

```yaml
kind: Ingress
```

Deploy:

```bash
kubectl apply -f ingress.yaml
```

---

# Step 2 – API Server

The API Server:

- Validates the Ingress
- Stores it in etcd

```
kubectl

↓

API Server

↓

Ingress Stored
```

At this point:

```
No Traffic

Yet
```

because an Ingress Controller is required.

---

# Step 3 – Ingress Controller Watches API

The Ingress Controller continuously watches:

- Ingress objects
- Services
- EndpointSlices
- Secrets
- IngressClasses

Whenever something changes:

```
API Update

↓

Controller

↓

Reload Configuration
```

---

# Step 4 – Generate Reverse Proxy Configuration

Suppose:

```yaml
host: example.com
```

```
path: /api
```

The Ingress Controller generates internal proxy configuration.

Example (conceptually):

```
example.com

↓

/api

↓

backend-service
```

For an NGINX Ingress Controller, this becomes an NGINX configuration file.

---

# Step 5 – Public Endpoint

The Ingress Controller itself is usually exposed through:

```
LoadBalancer
```

or

```
NodePort
```

Traffic reaches:

```
Internet

↓

Ingress Controller
```

---

# Step 6 – HTTP Request

Suppose:

```
https://example.com/api/users
```

Request arrives:

```
Ingress Controller
```

---

# Step 7 – Host Matching

Ingress Controller checks:

```
Host

↓

example.com
```

If matched:

```
Continue
```

Otherwise:

```
Default Backend
```

---

# Step 8 – Path Matching

Request:

```
/api/users
```

Ingress Rules:

```
/

↓

Frontend
```

```
/api

↓

Backend
```

Match:

```
Backend Service
```

---

# Step 9 – Service Lookup

Ingress forwards traffic to:

```
ClusterIP

↓

backend-service
```

The Service abstracts the backend Pods.

---

# Step 10 – EndpointSlice

The Service resolves to:

```
Pod A

Pod B

Pod C
```

through EndpointSlices.

One healthy Pod is selected.

---

# Step 11 – Backend Pod

Traffic reaches:

```
Container

↓

Application
```

Response:

```
Pod

↓

Ingress Controller

↓

Client
```

---

# Complete Packet Flow

```
Internet

↓

LoadBalancer

↓

Ingress Controller

↓

Ingress Rules

↓

ClusterIP

↓

EndpointSlice

↓

Pod

↓

Application
```

---

# Host-Based Routing Example

```
shop.example.com

↓

Shop Service
```

```
api.example.com

↓

API Service
```

```
admin.example.com

↓

Admin Service
```

Each hostname maps to a different backend.

---

# Path-Based Routing Example

```
/

↓

Frontend
```

```
/api

↓

Backend
```

```
/admin

↓

Admin
```

One domain can expose multiple applications.

---

# TLS Handshake

Client:

```
HTTPS Request
```

↓

Ingress Controller

↓

TLS Certificate

↓

Decrypt Traffic

↓

HTTP Request

↓

Backend Service
```

TLS terminates at the Ingress Controller unless configured otherwise.

---

# TLS Secret

Certificates are stored in:

```
Secret

↓

tls-secret
```

Ingress references the Secret to enable HTTPS.

---

# Reverse Proxy

The Ingress Controller acts as a reverse proxy.

```
Client

↓

Ingress Controller

↓

Backend
```

The client never connects directly to Pods.

---

# Load Balancing

Suppose:

```
Frontend

↓

5 Pods
```

Ingress:

```
↓

Service

↓

Pod Selection
```

The Service distributes traffic among healthy Pods.

---

# URL Rewrite

Incoming request:

```
/shop/products
```

Rewrite:

```
/products
```

before forwarding to the backend.

This is commonly configured using controller-specific annotations.

---

# Sticky Sessions

Optional:

```
Client

↓

Same Pod
```

Useful for applications requiring session persistence.

Support depends on the Ingress Controller.

---

# Authentication

Many Ingress Controllers support:

- OAuth
- OIDC
- JWT
- Basic Authentication
- External authentication services

These capabilities are configured using controller-specific features.

---

# Rate Limiting

Example:

```
100 Requests

↓

Per Minute
```

Excess requests:

```
Rejected
```

This helps protect backend applications.

---

# WebSocket Support

Modern Ingress Controllers support:

```
HTTP

↓

WebSocket Upgrade

↓

Persistent Connection
```

Useful for:

- Chat applications
- Dashboards
- Real-time monitoring

---

# Internal Architecture

```
Internet

↓

LoadBalancer

↓

Ingress Controller

↓

Routing Rules

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

# NGINX Example

```
Internet

↓

NGINX Ingress

↓

Reverse Proxy

↓

Service

↓

Pods
```

---

# Traefik Example

```
Internet

↓

Traefik

↓

Dynamic Routing

↓

Pods
```

---

# HAProxy Example

```
Internet

↓

HAProxy

↓

Service

↓

Pods
```

---

# Kong Example

```
Internet

↓

Kong

↓

API Gateway

↓

Pods
```

---

# Hands-on Lab 1 – Install an Ingress Controller

For example, install the **NGINX Ingress Controller** (refer to the official documentation for your Kubernetes environment).

Verify:

```bash
kubectl get pods -n ingress-nginx
```

Ensure the controller is running.

---

# Hands-on Lab 2 – Create Deployment

```bash
kubectl create deployment web \
--image=nginx
```

---

# Hands-on Lab 3 – Create Service

```bash
kubectl expose deployment web \
--port=80
```

---

# Hands-on Lab 4 – Create Ingress

Apply an Ingress resource that routes traffic to the `web` Service.

Verify:

```bash
kubectl get ingress
```

---

# Hands-on Lab 5 – Test Routing

Configure DNS (or your hosts file in a lab) so that:

```
example.com
```

points to the Ingress Controller.

Test:

```text
http://example.com
```

Verify that requests reach the backend application.

---

# Common Mistakes

## 1. Creating an Ingress Without an Ingress Controller

```
Ingress

↓

No Controller

↓

No Traffic
```

An Ingress resource alone cannot process requests.

---

## 2. Expecting Ingress to Expose TCP/UDP by Default

Ingress is designed primarily for:

- HTTP
- HTTPS

Raw TCP/UDP services require additional controller configuration or different Kubernetes resources.

---

## 3. Forgetting DNS

```
example.com

↓

Wrong IP
```

DNS must point to the Ingress Controller's external address.

---

## 4. Misconfigured TLS Secrets

If the referenced Secret is missing or invalid:

```
HTTPS

↓

Certificate Error
```

---

## 5. Incorrect Path Matching

Be mindful of:

- `Prefix`
- `Exact`
- `ImplementationSpecific`

Choosing the wrong `pathType` can lead to unexpected routing.

---

# Ingress Quick Revision

## Packet Flow

```
Internet

↓

LoadBalancer

↓

Ingress Controller

↓

Routing Rules

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

## Processing Flow

```
Ingress

↓

Controller

↓

Reverse Proxy

↓

Service

↓

Pod
```

---

## Routing

```
Host

↓

Path

↓

Service

↓

Pods
```

---

# Essential kubectl Commands

View Ingress:

```bash
kubectl get ingress
```

Describe Ingress:

```bash
kubectl describe ingress web-ingress
```

View Ingress Controller Pods:

```bash
kubectl get pods -n ingress-nginx
```

View Services:

```bash
kubectl get svc
```

Delete Ingress:

```bash
kubectl delete ingress web-ingress
```

---

# Interview Questions

### Basic

- What is an Ingress?
- Why is an Ingress Controller required?
- How does Ingress differ from a Service?

---

### Intermediate

- Explain host-based and path-based routing.
- How does TLS termination work?
- What is the role of an IngressClass?

---

### Advanced

- Explain the complete request flow from the Internet to a backend Pod through an Ingress.
- How does an Ingress Controller generate routing configuration?
- Why is Ingress considered a Layer 7 solution?
- Compare NGINX, Traefik, HAProxy, and Kong as Ingress Controllers.
- What happens when an Ingress rule is modified?

---

# References

## Official Kubernetes Documentation

- Ingress
- IngressClass
- Services
- EndpointSlices
- Networking Concepts

---

## CNCF Resources

- Kubernetes Networking
- SIG Network
- Kubernetes Best Practices
- Cloud Native Computing Foundation (CNCF)

---

## Ingress Controller Documentation

- NGINX Ingress Controller
- Traefik
- HAProxy Ingress
- Kong Ingress Controller

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Networking
- NIST SP 800-190
- OWASP Secure Headers Guidance

---

## Recommended Practice

1. Install an Ingress Controller in a lab cluster.
2. Deploy multiple applications and expose them through a single Ingress.
3. Configure host-based routing for different domains.
4. Configure path-based routing for multiple APIs.
5. Enable HTTPS using a TLS Secret.
6. Experiment with URL rewrites and controller annotations.
7. Compare how different Ingress Controllers implement the same Ingress resource.

---

# Chapter Summary

```
Internet

↓

LoadBalancer

↓

Ingress Controller

↓

Host & Path Matching

↓

ClusterIP Service

↓

EndpointSlice

↓

Backend Pods

↓

Application Response
```

An **Ingress** provides **declarative Layer 7 routing rules**, while an **Ingress Controller** enforces those rules by acting as a reverse proxy. Together with **Services**, **EndpointSlices**, and **TLS termination**, Ingress enables scalable, secure, and cost-effective exposure of multiple applications through a single external entry point.

---

