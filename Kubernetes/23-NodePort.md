# Chapter 23 – NodePort Service

## Overview

A **NodePort** Service exposes an application running inside a Kubernetes cluster to external clients by opening a **specific port on every worker Node**.

Unlike a **ClusterIP**, which is accessible only within the cluster, a NodePort allows clients outside the cluster to access the application using:

```
<Node-IP>:<NodePort>
```

Example:

```
192.168.1.10:30080
```

NodePort is commonly used for:

- Development environments
- Testing
- On-premises Kubernetes clusters
- Labs
- Small production deployments
- Demonstrations

> In cloud production environments, **LoadBalancer** or **Ingress** is usually preferred over direct NodePort access.

---

# Learning Objectives

After completing this chapter, you will understand:

- What NodePort is
- Why NodePort is needed
- NodePort Architecture
- NodePort Workflow
- Internal Packet Flow
- NodePort Allocation
- NodePort Range
- kube-proxy's Role
- External Access
- Best Practices

---

# Why Do We Need NodePort?

Suppose we have:

```
Client

↓

Internet
```

Application:

```
Pod

↓

ClusterIP
```

Problem:

```
ClusterIP

↓

Internal Only
```

External users cannot reach the application.

---

# Solution

Use a NodePort Service.

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

---

# What is a NodePort?

A NodePort Service opens a port on **every Node** in the cluster.

Example:

```
Worker Node

↓

30080
```

Traffic arriving on that port is forwarded to the Service and then to backend Pods.

---

# High-Level Architecture

```
                  Internet

                      │

                      ▼

          192.168.1.10:30080

                      │

                      ▼

                 Worker Node

                      │

                      ▼

                 NodePort Service

                      │

                      ▼

                 ClusterIP Service

          ┌───────────┼───────────┐

          ▼           ▼           ▼

       Pod A      Pod B      Pod C
```

---

# NodePort Characteristics

- Accessible from outside the cluster
- Opens the same port on every Node
- Automatically creates a ClusterIP
- Supports load balancing
- Uses kube-proxy
- Works without a cloud provider

---

# Service Hierarchy

```
NodePort

↓

ClusterIP

↓

Pods
```

Every NodePort Service automatically includes a ClusterIP.

---

# NodePort Workflow

```
Client

↓

Node IP

↓

NodePort

↓

ClusterIP

↓

Backend Pod
```

---

# NodePort Range

Default Kubernetes range:

```
30000

↓

32767
```

Example:

```
30080

30090

32000
```

This range can be customized by the cluster administrator.

---

# NodePort YAML

```yaml
apiVersion: v1

kind: Service

metadata:

  name: web-service

spec:

  type: NodePort

  selector:

    app: web

  ports:

  - port: 80

    targetPort: 8080

    nodePort: 30080
```

---

# YAML Breakdown

```
Service

↓

NodePort

↓

ClusterIP

↓

TargetPort

↓

Pods
```

---

# Port vs TargetPort vs NodePort

Example:

```yaml
port: 80

targetPort: 8080

nodePort: 30080
```

Meaning:

```
Client

↓

30080

↓

Service Port

80

↓

Container Port

8080
```

---

# Automatic NodePort Assignment

If:

```yaml
nodePort:
```

is omitted:

Kubernetes automatically assigns an available port from the configured NodePort range.

---

# External Access

Example:

```
Node

↓

192.168.1.20
```

Application:

```
http://192.168.1.20:30080
```

This reaches the backend Pods through the Service.

---

# Multiple Nodes

Suppose:

```
Node 1

192.168.1.10
```

```
Node 2

192.168.1.11
```

```
Node 3

192.168.1.12
```

The same NodePort exists on all Nodes:

```
30080
```

Clients can connect using any Node IP.

---

# Traffic Flow

```
Client

↓

NodePort

↓

ClusterIP

↓

Pod
```

The destination Pod may be on the same Node or a different Node.

---

# Internal Load Balancing

Suppose:

```
Pod A

Pod B

Pod C
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

Traffic distribution is handled by kube-proxy.

---

# Pod Scaling

Current:

```
3 Pods
```

Scale:

```
6 Pods
```

The Service automatically includes the new Pods.

No NodePort changes are required.

---

# Pod Failure

Suppose:

```
Pod B

↓

Crash
```

Endpoints are updated.

Traffic is automatically redirected to healthy Pods.

---

# Node Failure

Suppose:

```
Node 1

↓

Offline
```

Clients can connect using:

```
Node 2

↓

30080
```

or

```
Node 3

↓

30080
```

provided the cluster networking remains healthy.

---

# NodePort vs ClusterIP

| ClusterIP | NodePort |
|------------|----------|
| Internal only | External access |
| Default | Optional |
| No Node port | Opens port on every Node |
| Internal communication | External communication |

---

# NodePort vs LoadBalancer

| NodePort | LoadBalancer |
|-----------|--------------|
| Manual external access | Cloud-managed external access |
| Uses Node IP | Uses public load balancer IP |
| Suitable for labs | Suitable for production cloud environments |

---

# NodePort vs Ingress

| NodePort | Ingress |
|-----------|----------|
| One port per Service | Many Services through one endpoint |
| Basic routing | Advanced HTTP/HTTPS routing |
| Limited features | TLS, host-based and path-based routing |

---

# Viewing Services

```bash
kubectl get svc
```

Example:

```
NAME

TYPE

CLUSTER-IP

PORT(S)

web-service

NodePort

10.96.15.20

80:30080/TCP
```

---

# Describe Service

```bash
kubectl describe svc web-service
```

Displays:

- ClusterIP
- NodePort
- Endpoints
- Selectors

---

# Viewing Endpoints

```bash
kubectl get endpoints
```

Verify backend Pods.

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
kubectl describe svc web-service
```

Delete:

```bash
kubectl delete svc web-service
```

---

# NodePort Architecture Summary

```
Client

↓

Node IP

↓

NodePort

↓

ClusterIP

↓

Endpoints

↓

Pods
```

---

# Best Practices

### 1. Use NodePort Mainly for Development

For production cloud environments, prefer:

- LoadBalancer
- Ingress

---

### 2. Avoid Hardcoding Node IPs

When possible, place a load balancer or Ingress in front of NodePort Services.

---

### 3. Verify Firewall Rules

Ensure the NodePort range is allowed through firewalls and security groups.

---

### 4. Monitor Exposed Services

Every open NodePort increases the cluster's externally reachable surface.

---

### 5. Use Labels Consistently

Incorrect labels lead to Services without backend Pods.

---

# How NodePort Works Internally

## Overview

A **NodePort Service** extends the functionality of a **ClusterIP Service** by exposing the Service on a port of every Kubernetes worker Node.

Internally, Kubernetes does **not** create a process that listens on the NodePort.

Instead, **kube-proxy** programs the Linux networking stack (using **iptables**, **IPVS**, or **nftables**) so that packets arriving on the NodePort are automatically redirected to the appropriate backend Pods.

The packet forwarding is handled entirely by the Linux kernel, making NodePort efficient and scalable.

---

# High-Level Architecture

```
                    Internet

                        │

                        ▼

             Node IP : NodePort

             192.168.1.10:30080

                        │

                        ▼

                   kube-proxy

                        │

                 ClusterIP (VIP)

                        │

                  EndpointSlice

                        │

          ┌─────────────┼─────────────┐

          ▼             ▼             ▼

       Pod A         Pod B         Pod C
```

---

# Complete Packet Flow

```
Client

↓

Node IP

↓

NodePort

↓

Linux Kernel

↓

kube-proxy Rules

↓

ClusterIP

↓

EndpointSlice

↓

Backend Pod

↓

Application Response
```

---

# Step 1 – Create NodePort Service

Example:

```yaml
kind: Service

type: NodePort
```

Deploy:

```bash
kubectl apply -f service.yaml
```

---

# Step 2 – API Server

The API Server:

- Validates the Service
- Stores it in etcd

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

- Finds matching Pods
- Creates EndpointSlices
- Allocates a ClusterIP
- Allocates a NodePort (if not specified)

Workflow:

```
Service

↓

EndpointSlices

↓

ClusterIP

↓

NodePort
```

---

# Step 4 – ClusterIP Creation

Every NodePort Service automatically creates a ClusterIP.

Example:

```
ClusterIP

↓

10.96.25.15
```

NodePort is therefore built **on top of** ClusterIP.

---

# Step 5 – NodePort Allocation

Example:

```
NodePort

↓

30080
```

Kubernetes reserves this port on every Node.

```
Node 1

↓

30080
```

```
Node 2

↓

30080
```

```
Node 3

↓

30080
```

---

# Step 6 – kube-proxy Watches Services

Each worker Node runs:

```
kube-proxy
```

It watches:

- Services
- EndpointSlices
- Nodes

Whenever changes occur:

```
New Pod

↓

Update Kernel Rules
```

---

# Step 7 – Linux Kernel Rules

kube-proxy programs:

- iptables
- IPVS
- nftables

Example:

```
30080

↓

10.96.25.15

↓

Backend Pod
```

The packet is redirected before any application process receives it.

---

# Packet Flow Example

Client:

```
192.168.1.10:30080
```

Linux Kernel:

```
NodePort Rule

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

The client is unaware of the internal routing.

---

# Step 8 – EndpointSlice Selection

Suppose:

```
Pod A

↓

10.244.1.5
```

```
Pod B

↓

10.244.2.8
```

```
Pod C

↓

10.244.3.7
```

EndpointSlice contains:

```
All Healthy Pods
```

One Pod is selected for the request.

---

# Internal Load Balancing

Traffic:

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

Load balancing is handled by the Linux networking rules configured by kube-proxy.

---

# Same Node Traffic

Suppose:

```
Client

↓

Node 1

↓

Pod A

↓

Node 1
```

Flow:

```
NodePort

↓

iptables

↓

Pod
```

No inter-node communication occurs.

---

# Different Node Traffic

Suppose:

```
Client

↓

Node 1
```

Backend:

```
Pod

↓

Node 3
```

Flow:

```
NodePort

↓

ClusterIP

↓

CNI Network

↓

Node 3

↓

Pod
```

The CNI plugin transports the packet between Nodes.

---

# Source NAT (SNAT)

By default (`externalTrafficPolicy: Cluster`), traffic may be source NATed when forwarded across Nodes.

Example:

```
Client IP

↓

Translated

↓

Backend Pod
```

The Pod may see the Node's IP instead of the original client IP.

---

# Destination NAT (DNAT)

The destination address is rewritten.

Original:

```
NodeIP:30080
```

Rewritten:

```
PodIP:8080
```

The application receives traffic on its container port.

---

# externalTrafficPolicy

Two modes are available.

### Cluster (Default)

```
Client

↓

Any Node

↓

Any Backend Pod
```

Advantages:

- Uses all Pods
- Better load distribution

Disadvantage:

- Original client IP may not be preserved.

---

### Local

```
Client

↓

Node

↓

Local Pod Only
```

Advantages:

- Preserves client IP

Disadvantages:

- Traffic is accepted only on Nodes with local backend Pods.
- Load balancing opportunities are reduced.

---

# Cluster Mode Example

```
Client

↓

Node 1

↓

Pod

↓

Node 3
```

Cross-node forwarding is allowed.

---

# Local Mode Example

```
Client

↓

Node 1

↓

Local Pod
```

If Node 1 has no matching Pod, traffic is not forwarded to another Node.

---

# Scaling

Current:

```
3 Pods
```

Scale:

```
6 Pods
```

Workflow:

```
New Pods

↓

EndpointSlice Updated

↓

kube-proxy Updated

↓

Traffic Distributed
```

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

kube-proxy Updated

↓

Traffic Routed

↓

Remaining Pods
```

---

# Node Failure

Suppose:

```
Node 2

↓

Offline
```

Remaining Nodes continue exposing:

```
NodePort

↓

30080
```

Clients can use another healthy Node.

---

# Internal Architecture

```
Internet

↓

Node IP

↓

NodePort

↓

Linux Kernel

↓

kube-proxy

↓

ClusterIP

↓

EndpointSlice

↓

Backend Pod
```

---

# iptables Mode

Flow:

```
NodePort

↓

iptables

↓

ClusterIP

↓

Pod
```

Simple and widely used.

---

# IPVS Mode

Flow:

```
NodePort

↓

IPVS

↓

Backend Pod
```

Advantages:

- Higher performance
- Better scalability
- Advanced scheduling algorithms

---

# nftables Mode

Modern Linux distributions increasingly use:

```
nftables
```

Benefits:

- Simplified rule management
- Better performance
- Unified packet filtering framework

---

# Hands-on Lab 1 – Create Deployment

```bash
kubectl create deployment nginx \
--image=nginx \
--replicas=3
```

---

# Hands-on Lab 2 – Expose Deployment

```bash
kubectl expose deployment nginx \
--type=NodePort \
--port=80
```

Verify:

```bash
kubectl get svc
```

---

# Hands-on Lab 3 – Find NodePort

```bash
kubectl get svc nginx
```

Example output:

```
80:32045/TCP
```

Access:

```
http://<Node-IP>:32045
```

---

# Hands-on Lab 4 – Inspect EndpointSlices

```bash
kubectl get endpointslices
```

Observe backend Pod IP addresses.

---

# Hands-on Lab 5 – Test externalTrafficPolicy

Edit the Service:

```yaml
externalTrafficPolicy: Local
```

Compare:

- Client IP visibility
- Traffic routing
- Node behavior

---

# Common Mistakes

## 1. Using NodePort for Internet-Scale Production

Prefer:

- LoadBalancer
- Ingress

for most production deployments.

---

## 2. Forgetting Firewall Rules

The NodePort range must be allowed through:

- Firewalls
- Security Groups
- Network ACLs

---

## 3. Hardcoding Node IPs

Nodes may change.

Prefer a load balancer or DNS in front of NodePort.

---

## 4. Ignoring externalTrafficPolicy

If preserving the client IP is required, understand the trade-offs between `Cluster` and `Local`.

---

## 5. Confusing NodePort with Container Port

Example:

```
NodePort

30080
```

```
Service Port

80
```

```
Container Port

8080
```

Each serves a different purpose.

---

# NodePort Quick Revision

## Packet Flow

```
Client

↓

Node IP

↓

NodePort

↓

kube-proxy

↓

ClusterIP

↓

EndpointSlice

↓

Pod
```

---

## Service Hierarchy

```
NodePort

↓

ClusterIP

↓

Pod
```

---

## Traffic Policies

```
Cluster

↓

All Nodes

↓

All Pods
```

```
Local

↓

Node

↓

Local Pod
```

---

# Essential kubectl Commands

View Services:

```bash
kubectl get svc
```

Describe Service:

```bash
kubectl describe svc web-service
```

View EndpointSlices:

```bash
kubectl get endpointslices
```

Edit Service:

```bash
kubectl edit svc web-service
```

Delete:

```bash
kubectl delete svc web-service
```

---

# Interview Questions

### Basic

- What is a NodePort Service?
- How is NodePort different from ClusterIP?
- What is the default NodePort range?

---

### Intermediate

- Why does a NodePort Service automatically create a ClusterIP?
- What is `externalTrafficPolicy`?
- How does kube-proxy process NodePort traffic?

---

### Advanced

- Explain the complete packet flow from an external client to a backend Pod through a NodePort Service.
- Compare `externalTrafficPolicy: Cluster` and `Local`.
- What are the differences between iptables, IPVS, and nftables modes?
- Why is NodePort considered a building block for LoadBalancer Services?
- How does Kubernetes handle NodePort traffic when backend Pods are located on different Nodes?

---

# References

## Official Kubernetes Documentation

- Services
- NodePort
- kube-proxy
- EndpointSlices
- externalTrafficPolicy

---

## CNCF Resources

- Kubernetes Networking Model
- SIG Network Documentation
- Kubernetes Best Practices
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- Kubernetes Production Networking
- NIST SP 800-190
- Linux Kernel Networking Documentation

---

## Recommended Practice

1. Deploy a multi-replica application.
2. Expose it using a NodePort Service.
3. Access the application from multiple Nodes.
4. Switch between `externalTrafficPolicy: Cluster` and `Local`.
5. Scale the Deployment and observe EndpointSlice updates.
6. Delete backend Pods and verify automatic failover.
7. Compare NodePort behavior with ClusterIP in a lab environment.

---

# Chapter Summary

```
Internet

↓

Node IP

↓

NodePort

↓

Linux Kernel

↓

kube-proxy

↓

ClusterIP

↓

EndpointSlice

↓

Backend Pod

↓

Application Response
```

A **NodePort Service** extends **ClusterIP** by exposing an application through a port on every Kubernetes Node. Using **kube-proxy**, **EndpointSlices**, and Linux kernel networking, Kubernetes transparently forwards external traffic to healthy backend Pods while maintaining load balancing and automatic failover. It provides a simple way to expose applications outside the cluster and serves as the foundation for higher-level networking abstractions such as **LoadBalancer Services**.

---

