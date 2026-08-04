# Chapter 24 – LoadBalancer Service

## Overview

A **LoadBalancer Service** is a Kubernetes Service type that exposes an application to the **Internet** using an **external load balancer**.

It is the most common method for exposing applications in **cloud environments** such as:

- Amazon EKS (AWS)
- Azure AKS
- Google GKE
- Oracle OKE
- IBM Cloud Kubernetes
- DigitalOcean Kubernetes

Unlike a NodePort Service, where users connect directly to a Node, a LoadBalancer Service creates an external load balancer that automatically distributes traffic across Kubernetes Nodes.

> A **LoadBalancer Service builds on top of a NodePort Service**, which itself builds on top of a ClusterIP Service.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a LoadBalancer Service is
- Why LoadBalancer is needed
- LoadBalancer Architecture
- Cloud Provider Integration
- External IP Allocation
- Internal Packet Flow
- NodePort Relationship
- Health Checks
- Traffic Distribution
- Best Practices

---

# Why Do We Need LoadBalancer?

Suppose users access:

```
Node 1

↓

192.168.1.10:30080
```

Problems:

- Users must know Node IPs
- Nodes may fail
- Node IPs may change
- No centralized traffic distribution

---

# Solution

Use a cloud Load Balancer.

```
Internet

↓

Load Balancer

↓

Worker Nodes

↓

Pods
```

Users connect through one stable endpoint.

---

# What is a LoadBalancer Service?

A LoadBalancer Service creates an external load balancer that forwards requests to backend Kubernetes Services.

```
Internet

↓

External Load Balancer

↓

NodePort

↓

ClusterIP

↓

Pods
```

---

# High-Level Architecture

```
                    Internet

                        │

                        ▼

              External Load Balancer

                  35.201.25.10

                        │

        ┌───────────────┼───────────────┐

        ▼               ▼               ▼

     Worker 1       Worker 2       Worker 3

        │               │               │

        └───────────────┼───────────────┘

                        ▼

                  NodePort Service

                        ▼

                  ClusterIP Service

                        ▼

         ┌──────────────┼──────────────┐

         ▼              ▼              ▼

      Pod A          Pod B          Pod C
```

---

# LoadBalancer Characteristics

- External public IP
- Automatic cloud integration
- Health checks
- Automatic failover
- Load balancing
- Built on NodePort
- Suitable for production

---

# Service Hierarchy

```
LoadBalancer

↓

NodePort

↓

ClusterIP

↓

Pods
```

Every LoadBalancer Service automatically creates:

- ClusterIP
- NodePort

unless configured otherwise by supported implementations.

---

# LoadBalancer Workflow

```
Client

↓

Public IP

↓

Load Balancer

↓

NodePort

↓

ClusterIP

↓

Pod
```

---

# LoadBalancer YAML

```yaml
apiVersion: v1

kind: Service

metadata:

  name: web-service

spec:

  type: LoadBalancer

  selector:

    app: web

  ports:

  - port: 80

    targetPort: 8080
```

---

# YAML Breakdown

```
LoadBalancer

↓

Public Port

↓

NodePort

↓

ClusterIP

↓

TargetPort

↓

Container
```

---

# External IP Allocation

Cloud provider allocates:

```
Public IP

↓

35.201.25.10
```

Example:

```
kubectl get svc

↓

EXTERNAL-IP

↓

35.201.25.10
```

---

# Cloud Controller Manager

The **Cloud Controller Manager (CCM)** communicates with the cloud provider's APIs.

Responsibilities:

- Create Load Balancer
- Allocate Public IP
- Register Nodes
- Configure Health Checks

Workflow:

```
Service

↓

Cloud Controller Manager

↓

Cloud API

↓

Load Balancer
```

---

# Health Checks

Cloud Load Balancer continuously checks:

```
Worker Node

↓

Healthy?
```

Healthy Nodes:

```
Receive Traffic
```

Unhealthy Nodes:

```
Removed
```

---

# Traffic Distribution

Suppose:

```
Three Worker Nodes
```

Traffic:

```
Request 1

↓

Worker 1
```

```
Request 2

↓

Worker 2
```

```
Request 3

↓

Worker 3
```

Each Node forwards traffic to backend Pods.

---

# Pod Scaling

Current:

```
3 Pods
```

Scale:

```
8 Pods
```

Service:

```
Automatically

↓

EndpointSlices Updated

↓

Traffic Balanced
```

---

# Pod Failure

Suppose:

```
Pod B

↓

Crash
```

Traffic:

```
Automatically

↓

Pod A

↓

Pod C
```

No client changes are required.

---

# Worker Node Failure

Suppose:

```
Worker Node 2

↓

Offline
```

Cloud Load Balancer:

```
Health Check

↓

Remove Node 2

↓

Continue Routing
```

---

# External Traffic Flow

```
Internet

↓

Load Balancer

↓

NodePort

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

# Internal Communication

Pods inside the cluster usually communicate through:

```
ClusterIP
```

They typically do **not** use the external LoadBalancer address.

---

# LoadBalancer vs NodePort

| NodePort | LoadBalancer |
|-----------|--------------|
| Manual external access | Automatic public endpoint |
| Node IP required | Public IP or DNS |
| Best for labs | Best for cloud production |

---

# LoadBalancer vs ClusterIP

| ClusterIP | LoadBalancer |
|------------|--------------|
| Internal only | External access |
| Virtual IP | Public IP |
| Cluster traffic | Internet traffic |

---

# LoadBalancer vs Ingress

| LoadBalancer | Ingress |
|---------------|----------|
| One Service | Many Services |
| Layer 4 (TCP/UDP) by default | Layer 7 (HTTP/HTTPS) |
| One public IP per Service (typically) | Multiple applications behind one endpoint |

---

# Viewing Services

```bash
kubectl get svc
```

Example:

```
NAME

TYPE

EXTERNAL-IP

web

LoadBalancer

35.201.25.10
```

---

# Describe Service

```bash
kubectl describe svc web
```

Observe:

- External IP
- ClusterIP
- NodePort
- Endpoints

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f service.yaml
```

View:

```bash
kubectl get svc
```

Describe:

```bash
kubectl describe svc web
```

Delete:

```bash
kubectl delete svc web
```

---

# LoadBalancer Architecture Summary

```
Internet

↓

Public IP

↓

Load Balancer

↓

NodePort

↓

ClusterIP

↓

Pods
```

---

# Best Practices

### 1. Use LoadBalancer in Cloud Environments

Ideal for:

- Production
- Public APIs
- External applications

---

### 2. Use Ingress for Multiple Applications

Avoid creating many separate public load balancers when HTTP/HTTPS routing can be centralized.

---

### 3. Enable Health Checks

Ensure backend Pods expose proper readiness probes so unhealthy Pods are not added to the Service endpoints.

---

### 4. Secure Public Endpoints

Use:

- TLS
- Network Policies
- Authentication
- Web Application Firewall (WAF) where appropriate

---

### 5. Monitor Cloud Costs

Every cloud Load Balancer may incur additional charges.

---

# How LoadBalancer Works Internally

## Overview

A **LoadBalancer Service** is the highest-level Kubernetes Service type used to expose applications to external users.

Although it appears that Kubernetes creates a public IP address, Kubernetes itself **does not create load balancers**.

Instead, Kubernetes communicates with the underlying infrastructure through the **Cloud Controller Manager (CCM)**.

The Cloud Controller Manager interacts with the cloud provider's APIs to:

- Create an external Load Balancer
- Allocate a Public IP
- Register Worker Nodes
- Configure Health Checks
- Synchronize backend Nodes

Internally, a LoadBalancer Service builds upon:

```
LoadBalancer

↓

NodePort

↓

ClusterIP

↓

EndpointSlice

↓

Pods
```

---

# High-Level Architecture

```
                    Internet

                        │

                        ▼

                Public IP Address

                  35.201.25.10

                        │

                        ▼

          Cloud Load Balancer (AWS ELB / Azure LB /
                 GCP Load Balancer)

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

      Worker 1      Worker 2      Worker 3

          │             │             │

          ▼             ▼             ▼

         NodePort     NodePort     NodePort

                 ▼

             ClusterIP

                 ▼

           EndpointSlice

                 ▼

          Backend Pods
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

Service Created

↓

Cloud Controller Manager

↓

Cloud Provider API

↓

Load Balancer Created

↓

Public IP Assigned

↓

Traffic Starts
```

---

# Step 1 – Create LoadBalancer Service

Example:

```yaml
kind: Service

type: LoadBalancer
```

Deploy:

```bash
kubectl apply -f service.yaml
```

---

# Step 2 – API Server

The API Server:

- Validates Service
- Stores Service in etcd

```
kubectl

↓

API Server

↓

Service Stored
```

---

# Step 3 – Service Controller

The Service Controller:

- Allocates ClusterIP
- Creates EndpointSlices
- Allocates NodePort

```
LoadBalancer

↓

NodePort

↓

ClusterIP

↓

EndpointSlice
```

At this stage, the Service is still internal.

---

# Step 4 – Cloud Controller Manager (CCM)

The Cloud Controller Manager continuously watches the API Server.

When it detects:

```
type: LoadBalancer
```

it performs cloud-specific operations.

```
Service

↓

Cloud Controller Manager

↓

Cloud API
```

---

# Step 5 – Cloud Provider API

Examples:

- AWS → Elastic Load Balancer (ELB/NLB)
- Azure → Azure Load Balancer
- Google Cloud → Cloud Load Balancer
- Oracle Cloud → OCI Load Balancer

The cloud platform provisions the external load balancer.

---

# Step 6 – Public IP Allocation

The cloud provider assigns:

```
Public IP

↓

35.201.25.10
```

This IP becomes visible through:

```bash
kubectl get svc
```

Example:

```
EXTERNAL-IP

35.201.25.10
```

---

# Step 7 – Register Worker Nodes

The Load Balancer registers backend Nodes.

Example:

```
Worker 1

192.168.1.10
```

```
Worker 2

192.168.1.11
```

```
Worker 3

192.168.1.12
```

The Load Balancer sends traffic to Nodes, **not directly to Pods**.

---

# Step 8 – Health Checks

The cloud Load Balancer periodically checks each registered Node.

```
Health Check

↓

Worker Node

↓

Healthy?
```

If healthy:

```
Receive Traffic
```

If unhealthy:

```
Removed From Rotation
```

---

# Step 9 – NodePort

Traffic reaches:

```
Node IP

↓

NodePort
```

Example:

```
192.168.1.10:32045
```

The NodePort forwards traffic to the Service.

---

# Step 10 – kube-proxy

kube-proxy matches the incoming packet.

```
NodePort

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

Linux kernel rules perform the forwarding.

---

# Step 11 – EndpointSlice

Suppose:

```
Pod A

↓

10.244.1.8
```

```
Pod B

↓

10.244.2.9
```

```
Pod C

↓

10.244.3.7
```

EndpointSlice contains:

```
Healthy Backend Pods
```

One Pod is selected.

---

# Step 12 – Backend Pod

The request reaches:

```
Container

↓

Application

↓

Response
```

The response follows the reverse path.

---

# Complete Packet Flow

```
Client

↓

Public IP

↓

Cloud Load Balancer

↓

Worker Node

↓

NodePort

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

# Scaling

Current:

```
3 Pods
```

Scale:

```
8 Pods
```

Workflow:

```
Deployment

↓

New Pods

↓

EndpointSlice Updated

↓

kube-proxy Updated

↓

Traffic Balanced
```

The Load Balancer does not need to know individual Pod IPs.

---

# Pod Failure

Suppose:

```
Pod B

↓

Crash
```

Workflow:

```
EndpointSlice Updated

↓

Removed

↓

Traffic Continues
```

Clients experience minimal disruption.

---

# Node Failure

Suppose:

```
Worker 2

↓

Offline
```

Cloud Health Check:

```
Fail
```

Result:

```
Remove Worker 2

↓

Traffic

↓

Worker 1

Worker 3
```

---

# Cluster Autoscaling

Suppose:

```
New Worker Node
```

Cloud Controller Manager:

```
Registers

↓

Load Balancer
```

New Nodes become eligible for traffic after registration and health checks.

---

# Internal Architecture

```
Internet

↓

Public IP

↓

Cloud Load Balancer

↓

Worker Node

↓

NodePort

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

# AWS Example

```
Internet

↓

AWS ELB

↓

EC2 Worker Nodes

↓

NodePort

↓

Pods
```

---

# Azure Example

```
Internet

↓

Azure Load Balancer

↓

AKS Nodes

↓

Pods
```

---

# Google Cloud Example

```
Internet

↓

GCP Load Balancer

↓

GKE Nodes

↓

Pods
```

---

# Bare-Metal Clusters

On bare-metal Kubernetes:

```
LoadBalancer

↓

Pending
```

unless additional software is installed.

Common solutions:

- MetalLB
- kube-vip
- Cilium BGP (depending on deployment)

These projects provide LoadBalancer functionality in environments without a cloud provider.

---

# Session Affinity

Optional configuration:

```yaml
sessionAffinity: ClientIP
```

Behavior:

```
Client

↓

Same Backend Pod
```

Useful for applications requiring sticky sessions.

---

# externalTrafficPolicy

### Cluster (Default)

```
Load Balancer

↓

Any Node

↓

Any Pod
```

Pros:

- Better distribution
- Uses all Pods

Cons:

- Original client IP may be translated.

---

### Local

```
Load Balancer

↓

Node

↓

Local Pod
```

Pros:

- Preserves original client IP

Cons:

- Requires backend Pods on the receiving Node.

---

# Hands-on Lab 1 – Create Deployment

```bash
kubectl create deployment nginx \
--image=nginx \
--replicas=3
```

---

# Hands-on Lab 2 – Create LoadBalancer Service

```bash
kubectl expose deployment nginx \
--type=LoadBalancer \
--port=80
```

Verify:

```bash
kubectl get svc
```

Observe the assigned external IP (cloud environments).

---

# Hands-on Lab 3 – Describe Service

```bash
kubectl describe svc nginx
```

Inspect:

- ClusterIP
- NodePort
- External IP
- Endpoints

---

# Hands-on Lab 4 – Inspect EndpointSlices

```bash
kubectl get endpointslices
```

Observe backend Pod IPs.

---

# Hands-on Lab 5 – Scale Deployment

```bash
kubectl scale deployment nginx \
--replicas=6
```

Observe:

```bash
kubectl get endpointslices
```

Verify automatic updates.

---

# Common Mistakes

## 1. Expecting LoadBalancer to Work Everywhere

On bare-metal clusters:

```
EXTERNAL-IP

↓

Pending
```

Install a LoadBalancer implementation such as MetalLB if cloud integration is unavailable.

---

## 2. Forgetting Cloud Costs

Each cloud Load Balancer may incur ongoing charges.

---

## 3. Creating One LoadBalancer per Microservice

For HTTP/HTTPS workloads, consider using an Ingress Controller to expose multiple Services through a single external endpoint.

---

## 4. Ignoring Health Checks

Unhealthy Nodes or Pods should be excluded using readiness probes and cloud health checks.

---

## 5. Misunderstanding Traffic Flow

The Load Balancer forwards traffic to **Nodes**, while kube-proxy and EndpointSlices handle forwarding to **Pods**.

---

# LoadBalancer Quick Revision

## Service Hierarchy

```
LoadBalancer

↓

NodePort

↓

ClusterIP

↓

Pods
```

---

## Packet Flow

```
Internet

↓

Public IP

↓

Load Balancer

↓

NodePort

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

## Cloud Integration

```
Service

↓

Cloud Controller Manager

↓

Cloud Provider

↓

Load Balancer
```

---

# Essential kubectl Commands

View Services:

```bash
kubectl get svc
```

Describe Service:

```bash
kubectl describe svc nginx
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

Scale Deployment:

```bash
kubectl scale deployment nginx --replicas=6
```

Delete Service:

```bash
kubectl delete svc nginx
```

---

# Interview Questions

### Basic

- What is a LoadBalancer Service?
- How does it differ from NodePort?
- Why is it commonly used in cloud environments?

---

### Intermediate

- What is the role of the Cloud Controller Manager?
- Why does a LoadBalancer Service automatically create a NodePort?
- How are health checks performed?

---

### Advanced

- Explain the complete packet flow from the Internet to a backend Pod through a LoadBalancer Service.
- Why does the Load Balancer target Nodes instead of Pods?
- How does Kubernetes keep the Load Balancer synchronized with cluster changes?
- Compare `externalTrafficPolicy: Cluster` and `Local`.
- How can bare-metal Kubernetes clusters implement LoadBalancer functionality?

---

# References

## Official Kubernetes Documentation

- Services
- LoadBalancer Services
- Cloud Controller Manager
- EndpointSlices
- kube-proxy

---

## CNCF Resources

- Kubernetes Networking
- SIG Network
- Kubernetes Best Practices
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Networking
- NIST SP 800-190
- Cloud Provider Networking Documentation

---

## Recommended Practice

1. Deploy a multi-replica application.
2. Expose it with a LoadBalancer Service.
3. Verify the external IP assignment.
4. Scale the Deployment and observe EndpointSlice updates.
5. Delete backend Pods and verify failover.
6. Experiment with `externalTrafficPolicy`.
7. If using a bare-metal lab, install MetalLB and compare its behavior with a cloud-managed LoadBalancer.

---

# Chapter Summary

```
Internet

↓

Public IP

↓

Cloud Load Balancer

↓

Worker Nodes

↓

NodePort

↓

ClusterIP

↓

EndpointSlice

↓

Backend Pods

↓

Application Response
```

A **LoadBalancer Service** extends Kubernetes networking by integrating with cloud infrastructure to provide a **publicly accessible endpoint**. Through the **Cloud Controller Manager**, cloud APIs, **NodePort**, **ClusterIP**, **kube-proxy**, and **EndpointSlices**, Kubernetes delivers scalable, highly available, and production-ready external access to applications while automatically adapting to Pod and Node lifecycle changes.

---
