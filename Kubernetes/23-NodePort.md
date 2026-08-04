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

## Next Section

How NodePort Works Internally

kube-proxy Packet Flow

iptables vs IPVS

Hands-on Labs

Common Mistakes

Quick Revision

References

---