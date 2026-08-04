# Chapter 11 – Services

## Overview

A **Service** is a Kubernetes object that provides a **stable network endpoint** for a group of Pods.

Pods in Kubernetes are **ephemeral**:

- Pods can be deleted
- Pods can be recreated
- Pod IP addresses can change
- Pods may be scheduled on different Nodes

If applications communicated directly using Pod IP addresses, connectivity would frequently break.

A Service solves this problem by providing a **stable virtual IP address (ClusterIP)** and a **DNS name** that remains consistent even when the underlying Pods change.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Service is
- Why Services are required
- Service Architecture
- Service Discovery
- Service Types
- ClusterIP
- NodePort
- LoadBalancer
- ExternalName
- Headless Services
- Service Selectors
- Endpoint & EndpointSlice Concepts
- Best Practices

---

# Why Services?

Imagine an application with three Pods.

```
Deployment

↓

Pod A

10.244.1.5

↓

Pod B

10.244.2.8

↓

Pod C

10.244.3.4
```

Suppose Pod B crashes.

```
Pod B

↓

Deleted

↓

New Pod

↓

10.244.4.12
```

The IP address changes.

Applications depending on the old IP will fail.

---

# Solution

Instead of using Pod IPs:

```
Application

↓

Service

↓

Pods
```

The Service always remains available.

---

# What is a Service?

A Service is an abstraction that exposes a group of Pods as a **single network endpoint**.

```
Client

↓

Service

↓

Pods
```

Applications communicate with the Service—not individual Pods.

---

# Service Architecture

```
                 Client

                    │

                    ▼

               Kubernetes Service

                    │

        ┌───────────┼───────────┐

        ▼           ▼           ▼

      Pod A       Pod B       Pod C
```

The Service automatically routes requests to healthy Pods.

---

# Service Responsibilities

A Service provides:

- Stable IP address
- Stable DNS name
- Load balancing
- Service discovery
- Pod abstraction
- Loose coupling between clients and Pods

---

# Service Workflow

```
Client

↓

Service

↓

Selector

↓

Matching Pods

↓

Response
```

The Service uses **Label Selectors** to determine which Pods receive traffic.

---

# Service YAML

Example:

```yaml
apiVersion: v1

kind: Service

metadata:

  name: nginx-service

spec:

  selector:

    app: nginx

  ports:

  - port: 80

    targetPort: 80
```

---

# YAML Structure

```
Service

↓

Metadata

↓

Selector

↓

Ports

↓

Type
```

---

# Understanding Selectors

Service:

```yaml
selector:

  app: nginx
```

Pods:

```yaml
labels:

  app: nginx
```

Workflow:

```
Service

↓

Selector

↓

Matching Pods
```

If labels do not match, the Service has no endpoints.

---

# Service Types

Kubernetes supports four primary Service types.

```
Services

│

├── ClusterIP

├── NodePort

├── LoadBalancer

└── ExternalName
```

Additionally, Kubernetes supports **Headless Services**, which behave differently from standard Services.

---

# ClusterIP (Default)

```
Client

↓

ClusterIP

↓

Pods
```

Characteristics:

- Internal cluster access only
- Default Service type
- Stable virtual IP
- Accessible only within the cluster

Example:

```yaml
spec:

  type: ClusterIP
```

---

# NodePort

```
External Client

↓

Node IP

↓

NodePort

↓

Pods
```

Characteristics:

- Opens a port on every Node
- Allows external access
- Uses a port typically in the range 30000–32767 (default configuration)

Example:

```yaml
spec:

  type: NodePort
```

---

# LoadBalancer

```
Internet

↓

Cloud Load Balancer

↓

Service

↓

Pods
```

Characteristics:

- Integrates with supported cloud providers
- Creates an external load balancer
- Common in managed Kubernetes services

Example:

```yaml
spec:

  type: LoadBalancer
```

---

# ExternalName

Instead of forwarding traffic to Pods:

```
Service

↓

External DNS

↓

Database
```

Example:

```yaml
spec:

  type: ExternalName

  externalName: database.example.com
```

This Service acts as a DNS alias.

---

# Headless Service

A Headless Service does not allocate a ClusterIP.

```
Client

↓

DNS

↓

Pod A

Pod B

Pod C
```

Configuration:

```yaml
clusterIP: None
```

Common use cases:

- StatefulSets
- Direct Pod discovery
- Custom client-side load balancing

---

# Service Discovery

Every Service receives a DNS name.

Example:

```
nginx-service
```

Within the same Namespace:

```
http://nginx-service
```

Across Namespaces:

```
http://nginx-service.production.svc.cluster.local
```

Applications should use Service DNS names instead of Pod IPs.

---

# Service Ports

Example:

```yaml
ports:

- port: 80

  targetPort: 8080
```

Meaning:

```
Service Port

80

↓

Pod Port

8080
```

---

# Port Terminology

| Field | Meaning |
|--------|---------|
| port | Port exposed by the Service |
| targetPort | Port used by the Pod |
| nodePort | External Node port (NodePort Services only) |

---

# Creating a Service

Apply:

```bash
kubectl apply -f service.yaml
```

Verify:

```bash
kubectl get services
```

or

```bash
kubectl get svc
```

---

# Viewing Services

List:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc nginx-service
```

Review:

- Type
- Cluster IP
- Ports
- Selectors
- Endpoints

---

# Service Lifecycle

```
Create Service

↓

Assign ClusterIP

↓

Find Matching Pods

↓

Receive Traffic

↓

Route Requests

↓

Delete Service
```

---

# Important kubectl Commands

View:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc nginx-service
```

Delete:

```bash
kubectl delete svc nginx-service
```

View Endpoints:

```bash
kubectl get endpoints
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

---

# Services vs Pods

| Service | Pod |
|----------|-----|
| Stable endpoint | Ephemeral workload |
| Stable IP | Dynamic IP |
| DNS name | No permanent DNS identity |
| Load balancing | Runs application |
| Selects multiple Pods | Single instance |

---

# Service Architecture Summary

```
Client

↓

Service

↓

Selector

↓

Pods

↓

Containers
```

---

# Best Practices

### 1. Never Communicate Directly Using Pod IPs

Always use Services for application-to-application communication.

---

### 2. Use Meaningful Service Names

Examples:

```
frontend

backend

database

auth-service
```

---

### 3. Verify Label Selectors

Ensure the Service selector matches the labels applied to the target Pods.

---

### 4. Choose the Correct Service Type

- ClusterIP → Internal communication
- NodePort → Basic external access
- LoadBalancer → Cloud environments
- ExternalName → External DNS integration

---

### 5. Prefer DNS Names

Applications should connect using Service DNS names rather than hard-coded IP addresses.

---

# How Services Work Internally

## Overview

A Kubernetes Service is much more than a simple IP address.

Behind every Service, Kubernetes automatically maintains:

- Service IP (ClusterIP)
- DNS Records
- Endpoints
- EndpointSlices
- kube-proxy Rules
- Load Balancing Rules

Understanding how these components work together is essential for troubleshooting networking problems and designing production-ready Kubernetes applications.

---

# High-Level Service Architecture

```
                   Client

                     │

                     ▼

              Kubernetes Service

                     │

              Label Selector

                     │

          ┌──────────┼──────────┐

          ▼          ▼          ▼

       Pod A      Pod B      Pod C
```

Notice that the Service never communicates directly with containers.

Instead:

```
Service

↓

Endpoints

↓

Pods
```

---

# Complete Service Workflow

Suppose an application sends a request.

```
Application

↓

Service DNS

↓

ClusterIP

↓

kube-proxy

↓

Endpoints

↓

Selected Pod

↓

Response
```

Every request follows this general flow.

---

# Step 1 – Client Uses DNS

Instead of:

```
10.244.1.20
```

Applications use:

```
http://frontend
```

DNS resolves:

```
frontend

↓

ClusterIP
```

---

# Step 2 – DNS Resolution

CoreDNS maintains DNS records.

```
frontend.default.svc.cluster.local

↓

ClusterIP
```

Applications rarely need to use the full DNS name because Kubernetes automatically appends the search domain for Pods within the same Namespace.

---

# Step 3 – ClusterIP

Example:

```
Frontend Service

↓

10.96.18.25
```

Important:

```
ClusterIP

≠

Pod IP
```

ClusterIP is a **virtual IP** managed by Kubernetes.

---

# Step 4 – kube-proxy

Each worker node runs:

```
kube-proxy
```

Workflow:

```
ClusterIP

↓

kube-proxy

↓

Routing Rules

↓

Pod
```

kube-proxy programs networking rules that forward traffic to healthy backend Pods.

Depending on cluster configuration, it may use technologies such as **iptables**, **IPVS**, or **nftables**.

---

# Step 5 – Service Selectors

Service:

```yaml
selector:

  app: frontend
```

Pods:

```
Pod A

↓

app=frontend

✓
```

```
Pod B

↓

app=database

✗
```

Only matching Pods become Service backends.

---

# Step 6 – Endpoints

Kubernetes automatically creates an Endpoints object.

Example:

```
Service

↓

Endpoints

↓

10.244.1.5

10.244.2.8

10.244.3.4
```

These are the backend Pod IP addresses.

View:

```bash
kubectl get endpoints
```

---

# Step 7 – EndpointSlices

Modern Kubernetes clusters use **EndpointSlices** to efficiently represent Service backends.

Instead of storing every endpoint in one large object:

```
Service

↓

EndpointSlice A

↓

EndpointSlice B

↓

EndpointSlice C
```

Benefits:

- Better scalability
- Lower API load
- Faster updates

View:

```bash
kubectl get endpointslices
```

---

# Step 8 – Load Balancing

Suppose:

```
Service

↓

3 Pods
```

Requests:

```
Request 1

↓

Pod A
```

```
Request 2

↓

Pod B
```

```
Request 3

↓

Pod C
```

The exact distribution depends on the Service implementation and networking components.

---

# Step 9 – Pod Response

```
Pod

↓

Application

↓

Response

↓

Client
```

The client never needs to know which Pod handled the request.

---

# Internal Service Architecture

```
Client

↓

DNS

↓

ClusterIP

↓

kube-proxy

↓

Endpoints

↓

Pods
```

---

# What Happens When a Pod Dies?

Current:

```
Pod A

↓

Running
```

Pod crashes:

```
Pod A

↓

Deleted
```

Deployment creates:

```
Pod D
```

Service automatically updates:

```
Endpoints

↓

Pod D Added
```

Applications continue using the same Service without changing configuration.

---

# Dynamic Endpoint Updates

Current:

```
Service

↓

Pod A

Pod B

Pod C
```

Pod B deleted:

```
Service

↓

Pod A

Pod C
```

New Pod created:

```
Service

↓

Pod A

Pod C

Pod D
```

This update happens automatically.

---

# ClusterIP Internals

ClusterIP is virtual.

```
Client

↓

ClusterIP

↓

Routing Rules

↓

Pod
```

Packets are redirected by the node's networking stack according to rules programmed by kube-proxy.

---

# NodePort Workflow

```
Internet

↓

Node IP

↓

NodePort

↓

ClusterIP

↓

Pods
```

Every worker node listens on the configured NodePort.

---

# LoadBalancer Workflow

```
Internet

↓

Cloud Load Balancer

↓

Node

↓

Service

↓

Pods
```

The cloud provider provisions and manages the external load balancer.

---

# Headless Service Workflow

Configuration:

```yaml
clusterIP: None
```

Workflow:

```
DNS

↓

Pod A

Pod B

Pod C
```

DNS returns Pod IP addresses directly instead of a virtual Service IP.

---

# Service Discovery

Every Service automatically receives DNS records.

Examples:

Within the same Namespace:

```
frontend
```

Fully qualified name:

```
frontend.default.svc.cluster.local
```

Applications should rely on DNS instead of fixed IP addresses.

---

# kube-proxy Monitoring

kube-proxy continuously watches:

```
API Server

↓

Services

↓

Endpoints

↓

Update Rules
```

Whenever Pods are added or removed, networking rules are updated automatically.

---

# Hands-on Lab 1 – Create Deployment

```bash
kubectl create deployment nginx \
--image=nginx \
--replicas=3
```

Verify:

```bash
kubectl get pods
```

---

# Hands-on Lab 2 – Create Service

```bash
kubectl expose deployment nginx \
--port=80
```

Verify:

```bash
kubectl get svc
```

---

# Hands-on Lab 3 – Inspect Endpoints

```bash
kubectl get endpoints

kubectl get endpointslices
```

Observe that backend Pod IP addresses are associated with the Service.

---

# Hands-on Lab 4 – Delete a Pod

Delete one Pod:

```bash
kubectl delete pod <pod-name>
```

Observe:

```bash
kubectl get endpoints -w
```

Watch Kubernetes update the backend list automatically.

---

# Hands-on Lab 5 – Describe Service

```bash
kubectl describe svc nginx
```

Review:

- ClusterIP
- Ports
- Selectors
- Endpoints
- Events

---

# Common Mistakes

## 1. Using Pod IPs

Incorrect:

```
Application

↓

10.244.x.x
```

Correct:

```
Application

↓

Service DNS
```

---

## 2. Label Selector Mismatch

Service:

```yaml
selector:

  app: frontend
```

Pods:

```yaml
labels:

  app: backend
```

Result:

```
No Endpoints
```

Traffic cannot reach the application.

---

## 3. Assuming ClusterIP Is a Pod

Remember:

```
ClusterIP

↓

Virtual IP
```

It is not assigned to any individual Pod.

---

## 4. Forgetting DNS

Avoid hard-coded addresses.

Use:

```
frontend

database

redis

api
```

instead of IP addresses.

---

## 5. Ignoring EndpointSlices

Large clusters primarily use EndpointSlices.

Administrators should know how to inspect them during troubleshooting.

---

# Services Quick Revision

## Architecture

```
Client

↓

DNS

↓

ClusterIP

↓

kube-proxy

↓

Endpoints

↓

Pods
```

---

## Request Flow

```
Application

↓

Service

↓

Selector

↓

Matching Pods

↓

Response
```

---

## Service Types

```
ClusterIP

↓

Internal
```

```
NodePort

↓

External Node Access
```

```
LoadBalancer

↓

Cloud Load Balancer
```

```
ExternalName

↓

External DNS
```

```
Headless

↓

Direct Pod Discovery
```

---

# Essential kubectl Commands

View Services:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc nginx
```

View Endpoints:

```bash
kubectl get endpoints
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

Delete:

```bash
kubectl delete svc nginx
```

---

# Interview Questions

### Basic

- What problem does a Service solve?
- What is a ClusterIP?
- Why shouldn't applications use Pod IP addresses directly?

---

### Intermediate

- Explain how a Service finds Pods.
- What are Endpoints?
- What are EndpointSlices?
- How does kube-proxy participate in Service networking?

---

### Advanced

- How does Kubernetes update a Service when a Pod is replaced?
- What is the difference between ClusterIP and Headless Services?
- Why are EndpointSlices preferred in large clusters?
- How does DNS resolution work for Services?
- What happens if a Service selector matches no Pods?

---

# References

## Official Kubernetes Documentation

- Services
- Service Concepts
- EndpointSlices
- DNS for Services and Pods
- kube-proxy
- Kubernetes Networking

---

## CNCF Resources

- Kubernetes Best Practices
- Kubernetes Networking Guide
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Best Practices
- NIST SP 800-190
- OWASP Kubernetes Top 10

---

## Recommended Practice

1. Create a Deployment with three replicas.
2. Expose it using a ClusterIP Service.
3. Inspect the Endpoints and EndpointSlices.
4. Delete Pods and observe automatic endpoint updates.
5. Test DNS-based communication between Pods.
6. Experiment with ClusterIP, NodePort, and Headless Services in a lab environment.
7. Compare Service behavior with and without matching selectors.

---

# Chapter Summary

```
Client

↓

DNS

↓

ClusterIP

↓

kube-proxy

↓

Endpoints

↓

EndpointSlices

↓

Pods

↓

Application
```

Services provide the **stable networking foundation** of Kubernetes. By abstracting ephemeral Pods behind a consistent virtual IP and DNS name, Services enable reliable communication, automatic load balancing, and seamless integration with Deployments, ReplicaSets, and other Kubernetes components.

---
