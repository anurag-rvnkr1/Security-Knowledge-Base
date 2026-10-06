# Chapter 59 – Metrics Server

## Overview

Metrics Server is a Kubernetes component that collects resource usage metrics from nodes and Pods and exposes them through the Kubernetes Metrics API.

It is primarily used for:

```text
kubectl top
Horizontal Pod Autoscaler (HPA)
Vertical Pod Autoscaler (VPA)
```

A simplified architecture is:

```text
                 Kubernetes API Server
                         │
                         ▼
                  Metrics API
                         │
                         ▼
                  Metrics Server
                    /         \
                   /           \
                  ▼             ▼
             Kubelet Node 1  Kubelet Node 2
                  │             │
                  ▼             ▼
             Node / Pod     Node / Pod
               Metrics        Metrics
```

Metrics Server is **not a replacement for Prometheus**.

Its primary purpose is to provide near-real-time resource metrics for Kubernetes workloads rather than acting as a full observability platform.

---

# Learning Objectives

After completing this chapter, you will understand:

- Metrics Server fundamentals
- Why Metrics Server exists
- Kubernetes Metrics API
- Resource metrics
- CPU metrics
- Memory metrics
- Node metrics
- Pod metrics
- Metrics Server architecture
- Metrics Server components
- Metrics API
- API Aggregation Layer
- Kubelet metrics
- Metrics collection
- Metrics scraping
- `kubectl top`
- `kubectl top nodes`
- `kubectl top pods`
- Metrics Server installation
- Helm installation
- Manifest installation
- TLS
- Kubelet certificates
- Kubelet authentication
- Kubelet authorization
- API Server integration
- Metrics Server configuration
- Resource requests
- HPA integration
- VPA integration
- Metrics Server limitations
- Metrics Server vs Prometheus
- Metrics Server vs Node Exporter
- Troubleshooting Metrics Server
- Metrics API errors
- `Metrics API not available`
- `kubectl top` errors
- Certificate problems
- Network problems
- RBAC problems
- Resource consumption
- Production considerations
- Security
- Best practices
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Metrics Server?

Metrics Server is a lightweight, cluster-level aggregator of resource usage data.

It collects metrics from:

```text
Kubelets
```

and exposes them through:

```text
Kubernetes Metrics API
```

The primary resource metrics are:

```text
CPU
Memory
```

for:

```text
Nodes
Pods
```

---

# Why Metrics Server Exists

Kubernetes needs current resource information for features such as:

```text
HPA
VPA
kubectl top
```

For example:

```text
Application CPU Usage
        ↓
Metrics Server
        ↓
HPA
        ↓
Increase Pod Replicas
```

---

# Metrics Server Architecture

```text
                     Kubernetes API Server
                              │
                              │
                        Metrics API
                              │
                              ▼
                       Metrics Server
                              │
                 ┌────────────┴────────────┐
                 ▼                         ▼
              Kubelet                   Kubelet
              Node 1                    Node 2
                 │                         │
                 ▼                         ▼
             Pod Metrics              Pod Metrics
             Node Metrics             Node Metrics
```

---

# Metrics Server Components

The major components involved are:

```text
Metrics Server
Kubelet
Kubernetes API Server
API Aggregation Layer
Metrics API
```

---

# Kubelet

The kubelet runs on each Kubernetes node.

It provides resource-related information that Metrics Server collects.

Conceptually:

```text
Node
 └── Kubelet
       ├── Container Metrics
       └── Pod Metrics
```

---

# Metrics Collection Flow

The general flow is:

```text
Container
   ↓
Kubelet / Runtime Metrics
   ↓
Metrics Server
   ↓
Metrics API
   ↓
Kubernetes Consumers
```

Consumers include:

```text
kubectl top
HPA
VPA
```

---

# Kubernetes Metrics API

The Metrics API provides resource metrics through Kubernetes API machinery.

A commonly used API group is:

```text
metrics.k8s.io
```

---

# Metrics API

For nodes:

```text
/apis/metrics.k8s.io/v1beta1/nodes
```

For Pods:

```text
/apis/metrics.k8s.io/v1beta1/pods
```

The exact API version exposed can depend on the installed Metrics Server version.

---

# Checking the Metrics API

Run:

```bash
kubectl get apiservice
```

Look for:

```text
v1beta1.metrics.k8s.io
```

---

# Querying the Metrics API

You can inspect the API directly:

```bash
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
```

For Pods:

```bash
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/pods"
```

---

# `kubectl top`

The most common interface is:

```bash
kubectl top
```

It retrieves resource metrics from the Metrics API.

---

# `kubectl top nodes`

Run:

```bash
kubectl top nodes
```

Example:

```text
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
worker-1   420m         21%    2.1Gi          27%
worker-2   310m         15%    1.8Gi          23%
```

This gives a quick overview of node resource consumption.

---

# `kubectl top pods`

Run:

```bash
kubectl top pods
```

Example:

```text
NAME       CPU(cores)   MEMORY(bytes)
backend    150m         256Mi
frontend   80m          128Mi
worker     500m         512Mi
```

---

# Namespace Pod Metrics

```bash
kubectl top pods -n production
```

---

# All Namespace Metrics

```bash
kubectl top pods -A
```

---

# Sorting Pod Metrics

Depending on the kubectl version, you can use:

```bash
kubectl top pods --sort-by=cpu
```

or:

```bash
kubectl top pods --sort-by=memory
```

---

# Container-Level Metrics

For Pods containing multiple containers:

```bash
kubectl top pod <pod> --containers
```

This can help identify which container is consuming resources.

---

# Node Metrics

Metrics Server provides information such as:

```text
CPU Usage
Memory Usage
```

at the node level.

---

# Pod Metrics

At the Pod level, Metrics Server can provide resource usage information for:

```text
Pod
Container
```

depending on the API query.

---

# CPU Metrics

CPU usage is commonly represented in millicores.

Example:

```text
100m
```

means approximately:

```text
0.1 CPU
```

Therefore:

```text
1000m = 1 CPU
```

---

# Memory Metrics

Memory is commonly displayed using units such as:

```text
Mi
Gi
```

Example:

```text
256Mi
1Gi
```

---

# Metrics Server and Resource Requests

Metrics Server reports actual resource usage.

Kubernetes scheduling uses resource requests.

For example:

```yaml
resources:

  requests:

    cpu: "500m"

    memory: "512Mi"
```

Metrics Server does not determine the request.

It reports observed usage.

---

# Usage vs Request

Suppose:

```text
CPU Request = 500m
CPU Usage  = 250m
```

The workload is currently using approximately:

```text
50% of its CPU request
```

This distinction is important.

---

# Usage vs Limit

Suppose:

```text
CPU Limit = 1
CPU Usage = 700m
```

The container is currently using:

```text
0.7 CPU
```

The limit is:

```text
1 CPU
```

Metrics Server reports usage; it does not enforce the limit.

---

# Metrics Server and HPA

One of the most important uses of Metrics Server is supporting HPA with resource metrics.

Architecture:

```text
Pod
 ↓
CPU / Memory Usage
 ↓
Metrics Server
 ↓
Metrics API
 ↓
HPA
 ↓
Deployment
 ↓
Replica Count
```

---

# HPA Example

Suppose:

```yaml
targetCPUUtilization:
70%
```

and the application reaches:

```text
90%
```

HPA may increase replicas.

Conceptually:

```text
CPU ↑
 ↓
HPA
 ↓
Replicas ↑
```

---

# HPA Dependency

A typical resource-based HPA requires resource metrics to be available.

If Metrics Server is unavailable:

```text
HPA
 ↓
Cannot obtain required resource metrics
```

and autoscaling behavior can be affected.

---

# Metrics Server and VPA

VPA can also use resource usage information when recommending resource requests.

Conceptually:

```text
Pod Usage
 ↓
Metrics
 ↓
VPA
 ↓
Resource Recommendation
```

VPA's complete behavior depends on its installed components and configuration.

---

# API Aggregation Layer

Metrics Server integrates with Kubernetes through the API aggregation mechanism.

Architecture:

```text
kubectl
   ↓
API Server
   ↓
API Aggregation Layer
   ↓
Metrics API
   ↓
Metrics Server
```

---

# Why API Aggregation Matters

It allows additional APIs to appear as part of the Kubernetes API ecosystem.

Metrics Server exposes:

```text
metrics.k8s.io
```

rather than modifying the core Kubernetes API directly.

---

# APIService

Kubernetes uses an `APIService` object to register aggregated APIs.

Check:

```bash
kubectl get apiservice
```

You may see:

```text
v1beta1.metrics.k8s.io
```

---

# Inspect Metrics APIService

```bash
kubectl describe apiservice v1beta1.metrics.k8s.io
```

This can help diagnose:

```text
Availability
Service
CA Bundle
API Registration
```

---

# Metrics Server Service

Metrics Server normally runs behind a Kubernetes Service.

Check:

```bash
kubectl get svc -n kube-system
```

Look for:

```text
metrics-server
```

---

# Metrics Server Deployment

Check:

```bash
kubectl get deployment -n kube-system metrics-server
```

Check Pods:

```bash
kubectl get pods -n kube-system \
  -l k8s-app=metrics-server
```

Labels can vary depending on the installation.

---

# Metrics Server Installation

There are multiple ways to install Metrics Server.

Common approaches include:

```text
Official Manifest
Helm
Managed Kubernetes Add-on
```

Always use documentation matching your Kubernetes and Metrics Server versions.

---

# Manifest Installation

A typical workflow is:

```bash
kubectl apply -f <metrics-server-manifest>
```

Then verify:

```bash
kubectl get pods -n kube-system
```

---

# Helm Installation

If using Helm:

```bash
helm repo add metrics-server https://kubernetes-sigs.github.io/metrics-server/
```

Then:

```bash
helm repo update
```

Install:

```bash
helm install metrics-server \
  metrics-server/metrics-server \
  -n kube-system
```

Use the chart's current documented configuration for your environment.

---

# Verify Installation

Check:

```bash
kubectl get deployment metrics-server -n kube-system
```

Then:

```bash
kubectl get pods -n kube-system
```

Then:

```bash
kubectl top nodes
```

and:

```bash
kubectl top pods -A
```

---

# Metrics Availability Delay

After installation, metrics may not be immediately available.

Allow time for:

```text
Metrics Server
 ↓
Kubelet Scraping
 ↓
Metrics Collection
 ↓
API Availability
```

---

# TLS

Metrics Server communicates with kubelets over HTTPS.

Therefore:

```text
Metrics Server
       ↓ HTTPS
Kubelet
```

TLS configuration is important.

---

# Kubelet Certificates

Metrics Server needs to establish secure communication with kubelets.

Problems with kubelet certificates can cause errors such as:

```text
x509 certificate errors
```

---

# Certificate Error Example

You may see an error similar to:

```text
x509: cannot validate certificate
```

Possible causes include:

```text
Certificate SAN mismatch
Untrusted CA
Incorrect kubelet address
Improper certificate configuration
```

---

# `--kubelet-insecure-tls`

You may encounter configurations using:

```text
--kubelet-insecure-tls
```

This disables certificate verification when connecting to kubelets.

This can help diagnose certain lab environments, but it weakens transport security.

Do not treat it as a default production security solution.

---

# Kubelet Address Selection

Metrics Server may attempt to connect using node addresses such as:

```text
InternalIP
Hostname
ExternalIP
```

depending on configuration and environment.

A relevant option is:

```text
--kubelet-preferred-address-types
```

Example conceptually:

```text
InternalIP
Hostname
ExternalIP
```

---

# Why Address Selection Matters

Suppose:

```text
Hostname
```

does not resolve correctly.

Metrics Server may fail to scrape the kubelet.

Selecting an appropriate node address can solve the issue.

---

# Kubelet Authentication

Metrics Server must authenticate appropriately when accessing kubelet metrics.

Kubernetes environments commonly use:

```text
TLS
Service Account
RBAC
Kubelet Authentication
```

The exact configuration depends on cluster setup.

---

# Kubelet Authorization

Authentication answers:

```text
Who are you?
```

Authorization answers:

```text
What are you allowed to access?
```

Metrics Server requires appropriate permissions to obtain node and Pod resource information.

---

# RBAC

Metrics Server uses Kubernetes RBAC permissions.

Inspect its ServiceAccount:

```bash
kubectl get serviceaccount \
  metrics-server \
  -n kube-system
```

The exact ServiceAccount name can vary by installation.

---

# Inspect RBAC

Check:

```bash
kubectl get clusterrole
```

and:

```bash
kubectl get clusterrolebinding
```

Search for Metrics Server-related objects.

---

# Metrics Server Resource Usage

Metrics Server itself consumes resources.

Monitor:

```text
CPU
Memory
Network
```

For large clusters, resource requirements increase with:

```text
Node Count
Pod Count
Scrape Frequency
```

Use the current Metrics Server documentation and release notes for sizing guidance.

---

# Metrics Server Scaling

Metrics Server is designed for cluster-scale resource metrics.

For very large environments, evaluate:

```text
Resource Requirements
Availability
API Load
Scrape Frequency
High Availability
```

---

# High Availability

Production environments may run multiple Metrics Server replicas depending on requirements and supported configuration.

Conceptually:

```text
             API Server
                 │
        ┌────────┴────────┐
        ▼                 ▼
 Metrics Server A   Metrics Server B
        │                 │
        └────────┬────────┘
                 ▼
              Kubelets
```

---

# Metrics Server Is Not a Database

Metrics Server is not intended to be a long-term metrics database.

It is primarily designed to provide current resource metrics.

For historical metrics:

```text
Prometheus
```

or another time-series platform is more appropriate.

---

# Metrics Server vs Prometheus

| Feature | Metrics Server | Prometheus |
|---|---|---|
| Primary Purpose | Kubernetes resource metrics | General monitoring |
| CPU/Memory | Yes | Yes, with suitable metric sources |
| `kubectl top` | Yes | No, not directly |
| HPA Resource Metrics | Commonly | Via adapters/integrations |
| Historical Storage | Not designed for it | Yes |
| PromQL | No | Yes |
| Rich Dashboards | No | Commonly with Grafana |
| Alerting | Not its primary role | Supported through ecosystem |
| General Application Metrics | Limited | Strong |

---

# Metrics Server vs Node Exporter

Node Exporter focuses on host-level metrics.

Example:

```text
CPU
Memory
Disk
Filesystem
Network
```

Metrics Server focuses on Kubernetes resource usage metrics exposed through the Metrics API.

Architecture:

```text
Node Exporter
      ↓
Prometheus
```

versus:

```text
Kubelet
   ↓
Metrics Server
   ↓
Metrics API
```

---

# Metrics Server vs kube-state-metrics

These are also different.

Metrics Server:

```text
Resource Usage
```

kube-state-metrics:

```text
Kubernetes Object State
```

Examples from kube-state-metrics include information about:

```text
Deployments
Pods
DaemonSets
Jobs
Nodes
```

It does not replace Metrics Server.

---

# Three Different Monitoring Sources

```text
Metrics Server
=
Resource Usage

kube-state-metrics
=
Kubernetes Object State

Node Exporter
=
Host/System Metrics
```

Prometheus can collect metrics from these sources.

---

# Troubleshooting Metrics Server

If:

```bash
kubectl top nodes
```

fails, follow a structured process.

---

# Step 1 – Check Metrics Server Pods

```bash
kubectl get pods -n kube-system
```

Look for:

```text
metrics-server
```

---

# Step 2 – Check Deployment

```bash
kubectl get deployment \
  metrics-server \
  -n kube-system
```

---

# Step 3 – Check Logs

```bash
kubectl logs \
  deployment/metrics-server \
  -n kube-system
```

Look for:

```text
TLS Errors
RBAC Errors
Connection Errors
Timeouts
Authentication Errors
```

---

# Step 4 – Check APIService

```bash
kubectl get apiservice
```

Look for:

```text
v1beta1.metrics.k8s.io
```

---

# Step 5 – Describe APIService

```bash
kubectl describe apiservice \
  v1beta1.metrics.k8s.io
```

Check:

```text
Conditions
Service
Endpoints
CA Bundle
```

---

# Step 6 – Check Metrics Server Service

```bash
kubectl get svc \
  metrics-server \
  -n kube-system
```

---

# Step 7 – Check Endpoints

Depending on Kubernetes version:

```bash
kubectl get endpoints \
  metrics-server \
  -n kube-system
```

or:

```bash
kubectl get endpointslices \
  -n kube-system
```

---

# Step 8 – Check Node Connectivity

Metrics Server must reach kubelets.

Potential problems:

```text
NetworkPolicy
Firewall
Security Group
Routing
Port
TLS
```

---

# Step 9 – Check Certificates

If logs contain:

```text
x509
```

investigate:

```text
Kubelet Certificate
CA
Node Address
SAN
```

---

# Step 10 – Check RBAC

Inspect:

```bash
kubectl get clusterrole
kubectl get clusterrolebinding
```

Verify Metrics Server has appropriate permissions.

---

# Error: Metrics API Not Available

Example:

```text
error: Metrics API not available
```

Potential causes:

```text
Metrics Server Not Running
APIService Unavailable
Kubelet Scraping Failure
TLS Problem
Network Problem
RBAC Problem
```

---

# Error: `kubectl top` Fails

Start:

```bash
kubectl top nodes
```

If it fails:

```text
Check Metrics Server
 ↓
Check APIService
 ↓
Check Logs
 ↓
Check Kubelet Connectivity
 ↓
Check TLS
 ↓
Check RBAC
```

---

# Error: x509 Certificate

Potential cause:

```text
Metrics Server cannot verify kubelet certificate
```

Investigate:

```text
Certificate Authority
SAN
Node Address
Kubelet Configuration
```

---

# Error: Connection Refused

Potential causes:

```text
Kubelet unavailable
Incorrect port
Firewall
NetworkPolicy
Node failure
```

---

# Error: Timeout

Potential causes:

```text
Network connectivity
Firewall
Kubelet overload
Incorrect address
Routing
```

---

# Error: Forbidden

Potential cause:

```text
RBAC Authorization Failure
```

Check:

```text
ServiceAccount
ClusterRole
ClusterRoleBinding
```

---

# Error: No Data

If Metrics Server is running but no metrics appear:

```text
Check Scraping
Check Kubelets
Check Node Addresses
Check Certificates
Check APIService
```

---

# Metrics Server Security

Metrics Server should follow least privilege.

Use:

```text
RBAC
TLS
Service Accounts
Secure Network Paths
```

---

# Network Security

If NetworkPolicies are used, ensure Metrics Server can reach kubelets.

Conceptually:

```text
Metrics Server
      │
      │ HTTPS
      ▼
Kubelet
```

A NetworkPolicy accidentally blocking this path can break metrics collection.

---

# Metrics Server and Secrets

Metrics Server should not require access to arbitrary application Secrets.

Follow least privilege.

---

# Monitoring Metrics Server

Monitor:

```text
Pod Availability
CPU
Memory
Scrape Errors
API Availability
Request Latency
```

---

# Production Metrics Server Architecture

```text
                         Kubernetes API Server
                                  │
                           API Aggregation
                                  │
                                  ▼
                            Metrics API
                                  │
                                  ▼
                         Metrics Server
                          /           \
                         /             \
                        ▼               ▼
                    Kubelet A       Kubelet B
                        │               │
                    Node/Pods       Node/Pods
```

---

# Metrics Server and Prometheus Architecture

A production observability platform may use both:

```text
                    Kubernetes
                        │
          ┌─────────────┴─────────────┐
          ▼                           ▼
   Metrics Server                 Prometheus
          │                           │
          ▼                           ▼
    Metrics API                Time-Series Data
          │                           │
      ┌───┴───┐                       ▼
      ▼       ▼                    Grafana
   kubectl   HPA                     │
      top                             ▼
                                  Alerting
```

These components solve different problems.

---

# When to Use Metrics Server

Use Metrics Server when you need:

```text
kubectl top
HPA Resource Metrics
VPA Resource Data
Current CPU/Memory Usage
```

---

# When to Use Prometheus

Use Prometheus when you need:

```text
Historical Metrics
Application Metrics
Custom Metrics
PromQL
Dashboards
Alerting Integration
Longer-Term Analysis
```

---

# Metrics Server Limitations

Metrics Server is not intended to provide:

```text
Full Application Observability
Long-Term Metrics Storage
Advanced Analytics
Full Alerting Platform
Distributed Tracing
```

---

# Metrics Server and HPA

A common architecture is:

```text
Application
   ↓
Container CPU
   ↓
Kubelet
   ↓
Metrics Server
   ↓
Metrics API
   ↓
HPA
   ↓
Replica Count
```

---

# HPA Troubleshooting

If HPA shows:

```text
unknown
```

or cannot determine resource usage, check:

```bash
kubectl describe hpa <hpa>
```

Then:

```bash
kubectl top pods
```

If `kubectl top` fails, Metrics Server may be the underlying problem.

---

# HPA and Resource Requests

For CPU utilization-based scaling, define resource requests.

Example:

```yaml
resources:

  requests:

    cpu: "200m"

  limits:

    cpu: "500m"
```

Then HPA can calculate utilization relative to the CPU request.

---

# Example HPA

```yaml
apiVersion: autoscaling/v2

kind: HorizontalPodAutoscaler

metadata:

  name: web-hpa

spec:

  scaleTargetRef:

    apiVersion: apps/v1

    kind: Deployment

    name: web

  minReplicas: 2

  maxReplicas: 10

  metrics:

  - type: Resource

    resource:

      name: cpu

      target:

        type: Utilization

        averageUtilization: 70
```

---

# Metrics Server and VPA

VPA can use resource usage information to recommend resource values.

Conceptually:

```text
Historical Usage
      ↓
Resource Recommendation
      ↓
VPA
      ↓
CPU / Memory Request Adjustment
```

VPA architecture and data collection can vary by implementation.

---

# Resource Efficiency

Metrics Server helps identify:

```text
Underutilized Pods
Overloaded Pods
Resource Imbalances
```

Example:

```text
CPU Request = 2 CPU
Actual Usage = 100m
```

This may indicate overprovisioning.

---

# Capacity Planning

Metrics Server is primarily designed for current resource usage rather than long-term historical analysis.

For long-term planning:

```text
Prometheus
```

or another time-series system is more appropriate.

---

# Common Mistakes

## 1. Treating Metrics Server as Prometheus

They have different purposes.

---

## 2. Expecting Long-Term Historical Data

Metrics Server is not a long-term metrics database.

---

## 3. Using `--kubelet-insecure-tls` Blindly

This weakens certificate verification.

Use only when appropriate and understand the security implications.

---

## 4. Ignoring APIService

The Metrics API depends on proper API aggregation.

---

## 5. Ignoring Kubelet Connectivity

Metrics Server must reach kubelets.

---

## 6. Ignoring RBAC

Authentication alone is not enough.

---

## 7. No Resource Requests

HPA resource utilization calculations depend on resource requests.

---

## 8. Assuming `Running` Means Healthy

Metrics Server can be Running while scraping is failing.

Check:

```text
Logs
APIService
Metrics API
```

---

## 9. Ignoring TLS Errors

Certificate problems are common causes of scrape failures.

---

## 10. Using Metrics Server for Application Monitoring

For rich application metrics use:

```text
Prometheus
```

or another monitoring platform.

---

# Best Practices

### 1. Use a Supported Version

Use a Metrics Server version compatible with your Kubernetes version.

---

### 2. Use Secure TLS

Prefer proper certificate validation.

---

### 3. Follow Least Privilege

Give Metrics Server only the required permissions.

---

### 4. Monitor Metrics Server

Track:

```text
Availability
Scrape Errors
Resource Usage
API Health
```

---

### 5. Use Prometheus for Long-Term Monitoring

Do not use Metrics Server as a historical monitoring database.

---

### 6. Validate Kubelet Connectivity

Ensure:

```text
Metrics Server → Kubelet
```

communication works.

---

### 7. Configure Correct Node Addresses

Use appropriate kubelet address selection.

---

### 8. Use Resource Requests

Required for meaningful resource-utilization-based HPA behavior.

---

### 9. Test HPA

Do not assume autoscaling works simply because Metrics Server is installed.

---

### 10. Monitor APIService Health

Check:

```bash
kubectl get apiservice
```

regularly during troubleshooting.

---

# Production Checklist

```text
☑ Metrics Server installed
☑ Kubernetes version compatible
☑ Metrics API available
☑ APIService healthy
☑ Kubelet connectivity working
☑ TLS configured correctly
☑ RBAC configured
☑ ServiceAccount configured
☑ Node address selection correct
☑ Network policies allow required traffic
☑ kubectl top works
☑ HPA receives metrics
☑ VPA integration tested if used
☑ Metrics Server resources sized appropriately
☑ Metrics Server monitored
☑ Prometheus used for historical monitoring
```

---

# Hands-on Lab 1 – Verify Metrics Server

Run:

```bash
kubectl get pods -n kube-system
```

Find:

```text
metrics-server
```

Then:

```bash
kubectl top nodes
```

---

# Hands-on Lab 2 – Pod Metrics

Run:

```bash
kubectl top pods -A
```

Identify:

```text
Highest CPU Pod
Highest Memory Pod
```

---

# Hands-on Lab 3 – Container Metrics

Run:

```bash
kubectl top pod <pod> --containers
```

Compare resource consumption between containers.

---

# Hands-on Lab 4 – Metrics API

Run:

```bash
kubectl get apiservice
```

Find:

```text
metrics.k8s.io
```

Then:

```bash
kubectl get --raw \
  "/apis/metrics.k8s.io/v1beta1/nodes"
```

---

# Hands-on Lab 5 – Metrics Server Logs

Run:

```bash
kubectl logs \
  deployment/metrics-server \
  -n kube-system
```

Identify:

```text
Scrape
TLS
Network
Authentication
Authorization
```

messages.

---

# Hands-on Lab 6 – Metrics Server and HPA

Deploy:

```text
Application
+
CPU Request
+
HPA
```

Verify:

```text
kubectl top pods
```

Then generate CPU load.

Observe:

```text
Metrics
 ↓
HPA
 ↓
Replica Count
```

---

# Hands-on Lab 7 – APIService Troubleshooting

Run:

```bash
kubectl describe apiservice \
  v1beta1.metrics.k8s.io
```

Identify:

```text
Available
```

and understand the conditions reported by the APIService.

---

# Hands-on Lab 8 – Simulate TLS Troubleshooting

In a disposable environment, study a configuration where Metrics Server cannot validate kubelet certificates.

Observe:

```text
x509
```

errors.

Then correct the certificate/address configuration.

---

# Hands-on Lab 9 – Network Troubleshooting

Temporarily introduce a network restriction that prevents Metrics Server from reaching kubelets.

Observe:

```text
Timeout
Connection Refused
```

or similar errors.

Restore connectivity.

---

# Hands-on Lab 10 – RBAC Troubleshooting

Inspect Metrics Server permissions:

```bash
kubectl get clusterrole
kubectl get clusterrolebinding
```

Understand:

```text
ServiceAccount
 ↓
ClusterRole
 ↓
ClusterRoleBinding
```

---

# Hands-on Lab 11 – Compare Monitoring Sources

Install:

```text
Metrics Server
Prometheus
Node Exporter
kube-state-metrics
```

Create a table:

```text
Tool
 ↓
What data does it provide?
 ↓
Who consumes it?
```

---

# Hands-on Lab 12 – Resource Utilization

Deploy:

```yaml
resources:

  requests:

    cpu: "500m"

    memory: "256Mi"

  limits:

    cpu: "1"

    memory: "512Mi"
```

Compare:

```text
Request
Limit
Actual Usage
```

using:

```bash
kubectl top pod
```

---

# Hands-on Lab 13 – HPA Failure Investigation

Create an HPA.

Break Metrics Server in a disposable cluster.

Observe:

```bash
kubectl describe hpa <hpa>
```

Identify how missing metrics affect autoscaling.

Restore Metrics Server.

---

# Hands-on Lab 14 – Metrics Server Resource Monitoring

Monitor:

```bash
kubectl top pod \
  -n kube-system
```

Observe the Metrics Server resource usage.

---

# Hands-on Lab 15 – End-to-End Architecture

Build:

```text
Application
     ↓
Kubelet
     ↓
Metrics Server
     ↓
Metrics API
     ↓
HPA
     ↓
Deployment
     ↓
Replica Scaling
```

At every stage verify:

```text
Data Flow
Authentication
Authorization
TLS
```

---

# Quick Revision

## Metrics Server

```text
Cluster-level resource metrics aggregator
```

---

## Primary Metrics

```text
CPU
Memory
```

---

## Primary Consumers

```text
kubectl top
HPA
VPA
```

---

## Metrics API

```text
metrics.k8s.io
```

---

## API Aggregation

```text
Allows additional APIs to be served through Kubernetes API infrastructure
```

---

## Kubelet

```text
Provides node-level management and resource-related metrics used by Metrics Server
```

---

## `kubectl top`

```text
Displays resource usage from the Metrics API
```

---

## APIService

```text
Registers an aggregated API with Kubernetes
```

---

## Metrics Server vs Prometheus

```text
Metrics Server
=
Current Kubernetes resource metrics
```

```text
Prometheus
=
General-purpose time-series monitoring
```

---

## Metrics Server vs Node Exporter

```text
Metrics Server
=
Kubernetes resource metrics
```

```text
Node Exporter
=
Host/system metrics
```

---

## Metrics Server vs kube-state-metrics

```text
Metrics Server
=
Resource Usage
```

```text
kube-state-metrics
=
Kubernetes Object State
```

---

# Essential Commands

Check Metrics Server:

```bash
kubectl get pods \
  -n kube-system
```

Check Deployment:

```bash
kubectl get deployment \
  metrics-server \
  -n kube-system
```

Check Service:

```bash
kubectl get svc \
  metrics-server \
  -n kube-system
```

Check APIService:

```bash
kubectl get apiservice
```

Describe APIService:

```bash
kubectl describe apiservice \
  v1beta1.metrics.k8s.io
```

View Metrics Server logs:

```bash
kubectl logs \
  deployment/metrics-server \
  -n kube-system
```

View node metrics:

```bash
kubectl top nodes
```

View Pod metrics:

```bash
kubectl top pods
```

View all namespaces:

```bash
kubectl top pods -A
```

View container metrics:

```bash
kubectl top pod <pod> --containers
```

Query Metrics API:

```bash
kubectl get --raw \
  "/apis/metrics.k8s.io/v1beta1/nodes"
```

Query Pod metrics:

```bash
kubectl get --raw \
  "/apis/metrics.k8s.io/v1beta1/pods"
```

Check HPA:

```bash
kubectl get hpa -A
```

Describe HPA:

```bash
kubectl describe hpa <hpa>
```

---

# Interview Questions

## Basic

- What is Metrics Server?
- Why do we need Metrics Server?
- What metrics does Metrics Server provide?
- What is the Metrics API?
- What is `metrics.k8s.io`?
- What does `kubectl top` use?
- What is the API Aggregation Layer?
- What is an APIService?
- What is the role of the kubelet?
- What is the difference between Metrics Server and Prometheus?
- What is the difference between Metrics Server and Node Exporter?
- What is the difference between Metrics Server and kube-state-metrics?

---

## Intermediate

- How does Metrics Server collect metrics?
- How does Metrics Server communicate with kubelets?
- Why does Metrics Server require TLS?
- What is `--kubelet-preferred-address-types`?
- Why might Metrics Server report x509 errors?
- What is the purpose of RBAC in Metrics Server?
- How does Metrics Server support HPA?
- How does `kubectl top` work?
- Why might `kubectl top nodes` fail?
- Why might `kubectl top pods` fail?
- What is the purpose of the Metrics API?
- How do you troubleshoot the Metrics API?
- What happens if Metrics Server is unavailable?
- Is Metrics Server a long-term metrics database?

---

## Advanced

- Explain the complete Metrics Server architecture.
- How does API aggregation work with Metrics Server?
- How would you troubleshoot `Metrics API not available`?
- How would you troubleshoot kubelet TLS failures?
- How would you troubleshoot Metrics Server network connectivity?
- How would you troubleshoot Metrics Server RBAC failures?
- How would you make Metrics Server highly available?
- How does Metrics Server interact with HPA?
- What is the difference between resource metrics and custom metrics?
- Why would you use Prometheus instead of Metrics Server?
- How would you secure Metrics Server in production?
- How would you troubleshoot an HPA that shows unknown metrics?
- How would you design Metrics Server for a large Kubernetes cluster?
- How would you distinguish a Metrics Server failure from a kubelet metrics failure?

---

# Interview Scenario 1

### Question

> `kubectl top nodes` returns "Metrics API not available". What do you do?

### Answer

Use a layered troubleshooting approach:

```bash
kubectl get pods -n kube-system
```

Check Metrics Server.

Then:

```bash
kubectl logs \
  deployment/metrics-server \
  -n kube-system
```

Check:

```bash
kubectl get apiservice
```

Then:

```bash
kubectl describe apiservice \
  v1beta1.metrics.k8s.io
```

If necessary investigate:

```text
Kubelet Connectivity
TLS
RBAC
NetworkPolicy
Node Address
Metrics Server Service
```

---

# Interview Scenario 2

### Question

> Metrics Server is Running, but `kubectl top` still fails. Why?

### Answer

A Pod being:

```text
Running
```

does not mean it is successfully scraping kubelets.

Possible causes:

```text
TLS Error
Network Error
RBAC Error
Kubelet Failure
APIService Failure
Incorrect Address
```

Therefore check:

```text
Pod
 ↓
Logs
 ↓
APIService
 ↓
Kubelet
```

---

# Interview Scenario 3

### Question

> Why is `--kubelet-insecure-tls` not ideal for production?

### Answer

Because it disables certificate verification when communicating with kubelets.

That reduces protection against:

```text
Man-in-the-Middle Attacks
Certificate Impersonation
```

It can be useful in controlled lab environments or for diagnosis, but production deployments should use proper certificate validation.

---

# Interview Scenario 4

### Question

> Why does HPA need Metrics Server?

### Answer

For resource-based autoscaling, HPA needs current resource utilization.

The flow is:

```text
Pod
 ↓
Kubelet
 ↓
Metrics Server
 ↓
Metrics API
 ↓
HPA
 ↓
Replica Count
```

Without the required resource metrics, HPA cannot make normal resource-based scaling decisions.

---

# Interview Scenario 5

### Question

> Is Metrics Server enough for production monitoring?

### Answer

No.

Metrics Server provides a focused set of current Kubernetes resource metrics.

A production observability platform generally needs:

```text
Metrics Server
+
Prometheus
+
Grafana
+
Alertmanager
+
Logging
+
Tracing
```

depending on requirements.

---

# Interview Scenario 6

### Question

> What is the difference between resource metrics and application metrics?

### Answer

Resource metrics describe infrastructure/workload resource usage:

```text
CPU
Memory
```

Application metrics describe application behavior:

```text
Requests
Errors
Latency
Transactions
Queue Depth
```

Metrics Server primarily addresses resource metrics.

Prometheus is commonly used for application metrics.

---

# Interview Scenario 7

### Question

> What is the difference between Metrics Server and kube-state-metrics?

### Answer

Metrics Server provides:

```text
Resource Usage
```

kube-state-metrics provides:

```text
Kubernetes Object State
```

For example:

```text
Deployment Desired Replicas
Deployment Available Replicas
Pod Phase
DaemonSet Status
```

They complement each other.

---

# Interview Scenario 8

### Question

> How would you secure Metrics Server?

### Answer

Use:

```text
TLS
+
RBAC
+
Least Privilege
+
Service Account
+
Network Controls
+
Secure Kubelet Communication
```

Avoid unnecessary access and avoid disabling TLS verification without a strong reason.

---

# Production Metrics Architecture

```text
                            Kubernetes Cluster
                                    │
          ┌─────────────────────────┼─────────────────────────┐
          ▼                         ▼                         ▼
       Node 1                    Node 2                    Node 3
          │                         │                         │
       Kubelet                   Kubelet                   Kubelet
          │                         │                         │
          └─────────────────────────┼─────────────────────────┘
                                    │
                              HTTPS Metrics
                                    │
                                    ▼
                            Metrics Server
                                    │
                                    ▼
                              Metrics API
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
              kubectl              HPA                VPA
                 │                  │                  │
                 ▼                  ▼                  ▼
              Operator          Scaling           Recommendations
```

---

# Combined Kubernetes Observability Architecture

Metrics Server is only one component of a larger observability architecture:

```text
                         Kubernetes Cluster
                                  │
             ┌────────────────────┼────────────────────┐
             ▼                    ▼                    ▼
           Logs                 Metrics              Traces
             │                    │                    │
             ▼                    ▼                    ▼
        Fluent Bit           Prometheus          OpenTelemetry
             │                    │                    │
             ▼                    ▼                    ▼
      OpenSearch/Loki          Grafana              Backend
             │                    │                    │
             └────────────────────┼────────────────────┘
                                  ▼
                             Observability
                                  │
                                  ▼
                             SOC / SRE
```

And for resource-based Kubernetes features:

```text
Kubelet
   ↓
Metrics Server
   ↓
Metrics API
   ├── kubectl top
   ├── HPA
   └── VPA
```

---

# Chapter Summary

Metrics Server is a lightweight Kubernetes component designed to provide current resource usage metrics.

Its primary metrics are:

```text
CPU
Memory
```

for:

```text
Nodes
Pods
```

Its major consumers are:

```text
kubectl top
HPA
VPA
```

The architecture is:

```text
Kubelet
 ↓
Metrics Server
 ↓
Metrics API
 ↓
Kubernetes Consumers
```

Metrics Server integrates with Kubernetes through the:

```text
API Aggregation Layer
```

and is registered using an:

```text
APIService
```

The commonly used API group is:

```text
metrics.k8s.io
```

Useful commands include:

```bash
kubectl top nodes
kubectl top pods
kubectl get apiservice
kubectl describe apiservice v1beta1.metrics.k8s.io
```

Metrics Server is **not** a replacement for Prometheus.

The distinction is:

```text
Metrics Server
=
Current Kubernetes Resource Metrics
```

```text
Prometheus
=
General-Purpose Metrics Monitoring
```

Other important distinctions:

```text
Node Exporter
=
Host Metrics
```

```text
kube-state-metrics
=
Kubernetes Object State
```

A common production observability architecture uses all of these components for different purposes.

The most important troubleshooting workflow is:

```text
kubectl top fails
      ↓
Check Metrics Server Pod
      ↓
Check Metrics Server Logs
      ↓
Check APIService
      ↓
Check Metrics API
      ↓
Check Kubelet Connectivity
      ↓
Check TLS
      ↓
Check RBAC
      ↓
Check Network
```

The most important principle is:

> **Metrics Server provides the current Kubernetes resource metrics needed by core resource-aware features, while Prometheus and related systems provide broader, richer, and longer-term observability.**

---

## Next Chapter

# Chapter 60 – Prometheus

Topics will include:

- Prometheus Fundamentals
- Why Prometheus
- Prometheus Architecture
- Prometheus Server
- Time-Series Database
- Pull-Based Monitoring
- Scraping
- Targets
- Exporters
- Service Discovery
- Kubernetes Service Discovery
- Prometheus Configuration
- `prometheus.yml`
- Jobs
- Targets
- Labels
- Metric Types
- Counter
- Gauge
- Histogram
- Summary
- PromQL
- Selectors
- Instant Vectors
- Range Vectors
- Functions
- Aggregations
- `rate()`
- `irate()`
- `increase()`
- `sum()`
- `avg()`
- `max()`
- `min()`
- `histogram_quantile()`
- Recording Rules
- Alerting Rules
- Alertmanager
- Prometheus Operator
- ServiceMonitor
- PodMonitor
- PrometheusRule
- kube-state-metrics
- Node Exporter
- Kubernetes Metrics
- Application Metrics
- Custom Metrics
- Prometheus Storage
- Retention
- Remote Write
- High Availability
- Federation
- Scaling
- Cardinality
- Label Design
- Security
- TLS
- Authentication
- RBAC
- Production Architecture
- Troubleshooting
- Prometheus Targets
- Scrape Failures
- PromQL Troubleshooting
- Performance Optimization
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---