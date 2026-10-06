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

# How Gateway API Works Internally

## Overview

The **Gateway API** provides a modern, modular networking architecture for Kubernetes.

Unlike **Ingress**, which combines routing configuration into a single resource, the Gateway API separates responsibilities into multiple resources.

Internally, the Gateway API relies on a **Gateway Controller**, which continuously watches Gateway resources and configures the underlying networking infrastructure.

A Gateway Controller may configure:

- NGINX
- Envoy
- HAProxy
- Traefik
- Cloud Load Balancers
- Service Mesh Gateways
- Hardware Load Balancers

depending on the implementation.

> **The Gateway API defines the standard Kubernetes resources. The Gateway Controller implements their behavior.**

---

# High-Level Architecture

```
                    Internet

                        │

                        ▼

                 Public IP Address

                        │

                        ▼

                Gateway Controller

                        │

                        ▼

                    GatewayClass

                        │

                        ▼

                     Gateway

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

      HTTPRoute     TCPRoute      TLSRoute

                        │

                        ▼

                    Services

                        │

                  EndpointSlices

                        │

                        ▼

                       Pods
```

---

# Complete Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Gateway Resources

↓

Gateway Controller

↓

Generate Configuration

↓

Load Balancer

↓

Client Traffic

↓

Backend Pods
```

---

# Step 1 – Create GatewayClass

Example:

```yaml
kind: GatewayClass
```

The GatewayClass specifies:

- Controller
- Infrastructure type

Example:

```
gateway.networking.k8s.io

↓

GatewayClass
```

---

# Step 2 – API Server

The API Server:

- Validates Gateway resources
- Stores them in etcd

```
kubectl

↓

API Server

↓

Gateway Stored
```

---

# Step 3 – Gateway Controller Watches API

The Gateway Controller watches:

- GatewayClasses
- Gateways
- HTTPRoutes
- TCPRoutes
- TLSRoutes
- Services
- EndpointSlices
- Secrets

Whenever resources change:

```
API Update

↓

Controller

↓

Regenerate Configuration
```

---

# Step 4 – GatewayClass

Suppose:

```
GatewayClass

↓

nginx
```

The controller determines:

```
NGINX Gateway

↓

Manage This Gateway
```

Different controllers ignore GatewayClasses that do not belong to them.

---

# Step 5 – Gateway Creation

Example:

```
Gateway

↓

Public Listener

↓

Port 80

↓

Port 443
```

The Gateway defines where traffic enters the cluster.

---

# Gateway Listeners

Example:

```
HTTP

↓

80
```

```
HTTPS

↓

443
```

```
TLS

↓

8443
```

Each listener accepts specific protocols and ports.

---

# Step 6 – Route Attachment

Suppose:

```
HTTPRoute

↓

Gateway
```

The controller validates:

- Parent references
- Namespace permissions
- Route compatibility

If valid:

```
Route Attached
```

---

# Step 7 – HTTPRoute Processing

Example:

```
Host

↓

example.com
```

Path:

```
/api
```

Backend:

```
backend-service
```

The controller converts these rules into proxy configuration.

---

# Step 8 – Backend Service

Gateway routes traffic to:

```
ClusterIP Service
```

The Service resolves backend Pods through EndpointSlices.

---

# Step 9 – EndpointSlice

Suppose:

```
Pod A

↓

10.244.1.6
```

```
Pod B

↓

10.244.2.7
```

```
Pod C

↓

10.244.3.8
```

EndpointSlice stores healthy backend endpoints.

---

# Step 10 – Pod Selection

Traffic:

```
Gateway

↓

Service

↓

EndpointSlice

↓

Pod
```

The selected Pod receives the request.

---

# Complete Request Flow

```
Client

↓

Public IP

↓

Gateway

↓

HTTPRoute

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

# Host Matching

Incoming request:

```
shop.example.com
```

Gateway:

```
Match Host

↓

Shop Route
```

---

# Path Matching

Incoming request:

```
/api/users
```

Route:

```
/api

↓

Backend Service
```

---

# Header Matching

Example:

```
Header

↓

Version=v2
```

Route:

```
Canary Service
```

Gateway API supports sophisticated routing decisions.

---

# Query Parameter Matching

Example:

```
?beta=true
```

↓

```
Beta Service
```

Support depends on the Gateway implementation.

---

# Traffic Splitting

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

Gateway Controller configures weighted load balancing.

Useful for:

- Canary releases
- Progressive rollouts
- A/B testing

---

# TLS Termination

```
HTTPS

↓

Gateway

↓

TLS Secret

↓

Decrypt

↓

HTTP

↓

Backend
```

The Gateway terminates TLS before forwarding traffic.

---

# TLS Passthrough

Alternative mode:

```
HTTPS

↓

Gateway

↓

Encrypted

↓

Backend
```

The backend performs TLS decryption.

---

# TCP Routing

Example:

```
Client

↓

TCP Listener

↓

TCPRoute

↓

Database
```

Useful for:

- PostgreSQL
- MySQL
- Redis
- Kafka

---

# UDP Routing

Example:

```
DNS Client

↓

UDP Listener

↓

UDPRoute

↓

DNS Server
```

Availability depends on the Gateway implementation.

---

# Cross-Namespace Routing

Gateway API supports controlled routing across namespaces.

Security is enforced through:

```
ReferenceGrant
```

Without a valid ReferenceGrant:

```
Route Rejected
```

---

# Dynamic Updates

Suppose:

```
New Route

↓

API Server

↓

Gateway Controller

↓

Configuration Updated

↓

No Downtime
```

Traffic routing changes dynamically.

---

# Internal Architecture

```
Internet

↓

Gateway

↓

Gateway Controller

↓

Routes

↓

ClusterIP

↓

EndpointSlice

↓

Pods
```

---

# NGINX Gateway

```
Internet

↓

NGINX Gateway

↓

Routes

↓

Pods
```

---

# Envoy Gateway

```
Internet

↓

Envoy Gateway

↓

HTTPRoute

↓

Pods
```

---

# Traefik Gateway

```
Internet

↓

Traefik

↓

Gateway API

↓

Pods
```

---

# HAProxy Gateway

```
Internet

↓

HAProxy

↓

Gateway

↓

Pods
```

---

# Cloud Gateway

Cloud providers can implement Gateway API using managed infrastructure.

Example:

```
Gateway

↓

Cloud Load Balancer

↓

Nodes

↓

Pods
```

---

# Hands-on Lab 1 – Verify Gateway API CRDs

```bash
kubectl get crds | grep gateway
```

Observe resources such as:

- `gatewayclasses.gateway.networking.k8s.io`
- `gateways.gateway.networking.k8s.io`
- `httproutes.gateway.networking.k8s.io`

---

# Hands-on Lab 2 – View GatewayClasses

```bash
kubectl get gatewayclass
```

Observe available Gateway implementations.

---

# Hands-on Lab 3 – Create Gateway

Deploy a Gateway resource.

Verify:

```bash
kubectl get gateway
```

---

# Hands-on Lab 4 – Create HTTPRoute

Deploy an HTTPRoute.

Verify:

```bash
kubectl get httproute
```

Check attachment status using:

```bash
kubectl describe httproute
```

---

# Hands-on Lab 5 – Test Routing

Access:

```
http://example.com
```

Verify that traffic reaches the intended backend Service.

---

# Common Mistakes

## 1. Assuming Gateway Replaces the Controller

Incorrect:

```
Gateway

↓

Traffic
```

Correct:

```
Gateway

↓

Gateway Controller

↓

Traffic
```

The controller performs the actual networking operations.

---

## 2. Forgetting GatewayClass

Without a valid GatewayClass:

```
Gateway

↓

Not Accepted
```

---

## 3. Missing Parent References

Routes must explicitly reference the Gateway they attach to.

---

## 4. Missing ReferenceGrant

Cross-namespace routing requires explicit authorization.

Without it:

```
Route

↓

Rejected
```

---

## 5. Expecting All Controllers to Support Every Feature

Different Gateway implementations may support different capabilities.

Always consult the controller's documentation.

---

# Gateway API Quick Revision

## Architecture

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

## Request Flow

```
Internet

↓

Gateway

↓

HTTPRoute

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

## Routing Features

```
Host

↓

Path

↓

Headers

↓

Traffic Split

↓

Backend
```

---

# Essential kubectl Commands

View GatewayClasses:

```bash
kubectl get gatewayclass
```

View Gateways:

```bash
kubectl get gateway
```

View HTTPRoutes:

```bash
kubectl get httproute
```

Describe Gateway:

```bash
kubectl describe gateway web-gateway
```

Describe HTTPRoute:

```bash
kubectl describe httproute web-route
```

Delete Gateway:

```bash
kubectl delete gateway web-gateway
```

---

# Interview Questions

### Basic

- What is the Gateway API?
- How does it differ from Ingress?
- What is a GatewayClass?

---

### Intermediate

- What is the role of a Gateway Controller?
- How does an HTTPRoute attach to a Gateway?
- What is a ReferenceGrant?

---

### Advanced

- Explain the complete request flow through the Gateway API.
- Compare Gateway API and Ingress architectures.
- How does the Gateway Controller generate proxy configuration?
- Why is Gateway API better suited for multi-team environments?
- Explain weighted traffic routing and TLS termination in the Gateway API.

---

# References

## Official Kubernetes Documentation

- Gateway API
- GatewayClass
- Gateway
- HTTPRoute
- TCPRoute
- TLSRoute
- ReferenceGrant

---

## CNCF Resources

- SIG Network
- Gateway API Specification
- Kubernetes Networking Best Practices
- Cloud Native Computing Foundation (CNCF)

---

## Gateway Implementations

- Envoy Gateway
- NGINX Gateway Fabric
- Traefik
- HAProxy Kubernetes Ingress
- Kong Gateway

---

## Security & Operations

- CIS Kubernetes Benchmark
- NIST SP 800-190
- Kubernetes Production Networking
- Gateway API Conformance Documentation

---

## Recommended Practice

1. Install a Gateway API-compatible controller.
2. Create a GatewayClass and Gateway.
3. Attach multiple HTTPRoutes to the same Gateway.
4. Configure host-based and path-based routing.
5. Experiment with weighted traffic splitting for canary deployments.
6. Enable HTTPS using TLS Secrets.
7. Test cross-namespace routing with `ReferenceGrant`.

---

# Chapter Summary

```
Internet

↓

Gateway

↓

Gateway Controller

↓

GatewayClass

↓

HTTPRoute / TCPRoute / TLSRoute

↓

ClusterIP Service

↓

EndpointSlice

↓

Backend Pods

↓

Application Response
```

The **Gateway API** modernizes Kubernetes networking by separating **infrastructure**, **traffic entry points**, and **routing rules** into dedicated resources. Through the **Gateway Controller**, it supports advanced routing, multi-protocol traffic, delegated administration, and progressive delivery, making it the recommended direction for building scalable and flexible Kubernetes networking solutions.

---

## What's Next?

The recommended sequence after Gateway API is:

1. **Network Policies**
2. **Container Network Interface (CNI) Deep Dive**
3. **Calico**
4. **Cilium & eBPF**
5. **CoreDNS**
6. **kube-proxy (iptables, IPVS & nftables)**
7. **Service Mesh (Istio & Envoy)**

This follows the natural progression from **traffic ingress** to **network security** and then into **cluster networking internals**.

---