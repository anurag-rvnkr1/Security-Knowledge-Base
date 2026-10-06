# Chapter 71 – Resource Optimization

## Overview

Resource Optimization in Kubernetes is the process of using compute, memory, storage, and networking resources efficiently while maintaining application performance, reliability, and availability.

The goal is not simply:

```text
Use Less Resources
```

The real goal is:

```text
Right Resources
+
Right Capacity
+
Right Performance
+
Right Cost
+
Right Availability
```

A simplified optimization lifecycle:

```text
Measure
   ↓
Analyze
   ↓
Right-Size
   ↓
Schedule Efficiently
   ↓
Autoscale
   ↓
Monitor
   ↓
Repeat
```

Kubernetes resource optimization involves:

```text
CPU
Memory
Storage
Network
Pods
Nodes
Scheduling
Autoscaling
Capacity
Cost
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Resource optimization fundamentals
- Kubernetes resource management
- CPU optimization
- Memory optimization
- Storage optimization
- Network optimization
- Pod resource requests
- Pod resource limits
- Quality of Service classes
- Guaranteed QoS
- Burstable QoS
- BestEffort QoS
- CPU requests
- CPU limits
- Memory requests
- Memory limits
- ResourceQuota
- LimitRange
- Namespace resource management
- Resource utilization
- Overprovisioning
- Underprovisioning
- Bin packing
- Scheduling efficiency
- Node utilization
- Pod density
- Vertical Pod Autoscaler
- Horizontal Pod Autoscaler
- Cluster Autoscaler
- Node autoscaling
- Cost optimization
- Right-sizing
- Workload profiling
- Capacity planning
- Headroom
- Requests vs actual usage
- CPU throttling
- Memory pressure
- OOMKilled
- Evictions
- Disk pressure
- Ephemeral storage
- Storage optimization
- Image optimization
- Network efficiency
- DNS optimization
- Logging cost optimization
- Monitoring cost optimization
- Idle resources
- Unused resources
- Resource cleanup
- Scheduling optimization
- Node affinity
- Taints and tolerations
- Topology spread
- Priority Classes
- Preemption
- Autoscaling strategies
- HPA optimization
- VPA optimization
- Cluster Autoscaler optimization
- Cost allocation
- Namespace cost management
- Multi-tenant optimization
- Production optimization
- Resource efficiency metrics
- Optimization runbooks
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is Resource Optimization?

Resource optimization means allocating enough resources for workloads without unnecessarily wasting capacity.

Poor optimization:

```text
Application
   ↓
Requests: 8 CPU
Actual:   1 CPU
```

This may result in:

```text
Low Node Utilization
Higher Cost
Lower Scheduling Efficiency
```

Overly aggressive optimization is also dangerous:

```text
Application
   ↓
Requests: 100m CPU
Actual Peak: 2 CPU
```

This may cause:

```text
CPU Contention
Performance Problems
Throttling
```

---

# The Optimization Balance

A production system should balance:

```text
Performance
    +
Reliability
    +
Availability
    +
Cost
```

---

# Kubernetes Resource Types

Major resource categories include:

```text
CPU
Memory
Ephemeral Storage
Persistent Storage
Network
```

---

# CPU

CPU is generally measured in:

```text
cores
millicores
```

Example:

```text
1 CPU
```

is equivalent to:

```text
1000m
```

Therefore:

```text
500m = 0.5 CPU
```

---

# Memory

Memory is commonly represented using:

```text
Mi
Gi
```

Example:

```text
512Mi
1Gi
2Gi
```

---

# Resource Requests

Requests tell Kubernetes how much resource a container requires for scheduling purposes.

Example:

```yaml
resources:

  requests:
    cpu: "500m"
    memory: "512Mi"
```

---

# Resource Limits

Limits define the maximum resource boundary for a container.

Example:

```yaml
resources:

  limits:
    cpu: "1"
    memory: "1Gi"
```

---

# Complete Resource Configuration

Example:

```yaml
resources:

  requests:
    cpu: "500m"
    memory: "512Mi"

  limits:
    cpu: "1"
    memory: "1Gi"
```

---

# Requests vs Limits

| Property | Purpose |
|---|---|
| Request | Scheduling and reserved capacity |
| Limit | Maximum resource boundary |

---

# CPU Requests

Example:

```yaml
requests:
  cpu: "250m"
```

The scheduler considers the requested CPU when deciding where to place the Pod.

---

# Memory Requests

Example:

```yaml
requests:
  memory: "256Mi"
```

The scheduler uses the memory request when evaluating node capacity.

---

# CPU Limits

Example:

```yaml
limits:
  cpu: "1"
```

The container cannot continuously consume more than its configured CPU limit under normal Linux cgroup enforcement behavior.

---

# Memory Limits

Example:

```yaml
limits:
  memory: "512Mi"
```

If a container exceeds its memory limit, it can be terminated by the kernel/cgroup mechanism and may appear as:

```text
OOMKilled
```

---

# CPU vs Memory Behavior

CPU:

```text
Excess Usage
 ↓
Throttling / Scheduling Constraint
```

Memory:

```text
Excess Usage
 ↓
Potential OOM Kill
```

---

# Quality of Service Classes

Kubernetes assigns Pods to QoS classes:

```text
Guaranteed
Burstable
BestEffort
```

---

# Guaranteed QoS

A Pod is generally Guaranteed when all containers have CPU and memory requests and limits configured, with requests equal to limits for those resources.

Example:

```yaml
resources:

  requests:
    cpu: "500m"
    memory: "512Mi"

  limits:
    cpu: "500m"
    memory: "512Mi"
```

---

# Burstable QoS

A Pod is Burstable when it has resource requests or limits but does not meet the conditions for Guaranteed QoS.

Example:

```yaml
resources:

  requests:
    cpu: "250m"
    memory: "256Mi"

  limits:
    cpu: "1"
    memory: "512Mi"
```

---

# BestEffort QoS

A Pod is generally BestEffort when none of its containers specify CPU or memory requests or limits.

Example:

```yaml
containers:

  - name: app
    image: nginx
```

---

# QoS Comparison

| QoS | Requests/Limits | Typical Use |
|---|---|---|
| Guaranteed | Equal CPU/Memory requests and limits | Critical predictable workloads |
| Burstable | Partial/different requests and limits | Most applications |
| BestEffort | None | Low-priority workloads |

---

# Why Requests Matter

Suppose a node has:

```text
4 CPU
```

and:

```text
Pod A requests 2 CPU
Pod B requests 2 CPU
```

The scheduler understands:

```text
4 CPU allocated
```

Even if actual usage is temporarily lower.

---

# Overprovisioning

Overprovisioning means requesting significantly more resources than workloads actually use.

Example:

```text
Request: 4 CPU
Actual: 500m CPU
```

Problems:

```text
Wasted Capacity
More Nodes
Higher Cost
```

---

# Underprovisioning

Underprovisioning means requests are too low.

Example:

```text
Request: 100m
Actual: 2 CPU
```

Potential problems:

```text
Contention
Performance Degradation
OOM
Scheduling Issues
```

---

# Right-Sizing

Right-sizing means selecting resource requests and limits based on measured workload behavior.

Process:

```text
Measure
 ↓
Analyze
 ↓
Set Requests
 ↓
Set Limits
 ↓
Monitor
 ↓
Adjust
```

---

# Workload Profiling

Before right-sizing, measure:

```text
Average CPU
Peak CPU
Average Memory
Peak Memory
Restart Count
Latency
Throughput
```

---

# Requests Should Reflect Reality

Example:

```text
Average CPU = 300m
Peak CPU = 800m
```

A reasonable request might be closer to the sustained requirement than the absolute peak, depending on workload characteristics and scaling strategy.

---

# Headroom

Headroom is spare capacity available for:

```text
Traffic Spikes
Node Failure
Rolling Updates
Scheduling
```

Example:

```text
Node Capacity = 16 CPU
Normal Usage = 11 CPU
Headroom = 5 CPU
```

---

# Why Headroom Matters

Without headroom:

```text
Traffic Spike
 ↓
No Capacity
 ↓
Performance Degradation
```

With headroom:

```text
Traffic Spike
 ↓
Available Capacity
 ↓
Application Continues
```

---

# Bin Packing

Bin packing means placing workloads efficiently onto available nodes.

Example:

```text
Node-1
 ├── Pod A
 ├── Pod B
 └── Pod C
```

rather than spreading tiny workloads unnecessarily across many nodes.

---

# Bin Packing Trade-Off

Higher utilization:

```text
Lower Cost
```

but potentially:

```text
Less Failure Headroom
More Contention
```

Therefore optimization must not sacrifice resilience.

---

# Node Utilization

Monitor:

```text
CPU Utilization
Memory Utilization
Pod Density
Disk Usage
Network Usage
```

---

# Pod Density

Pod density describes how many Pods run on a node.

Too low:

```text
Wasted Capacity
```

Too high:

```text
Scheduling Pressure
Network Pressure
Runtime Overhead
Failure Blast Radius
```

---

# ResourceQuota

ResourceQuota limits aggregate resource consumption within a namespace.

Example:

```yaml
apiVersion: v1
kind: ResourceQuota

metadata:
  name: team-quota

spec:

  requests.cpu: "10"

  requests.memory: 20Gi

  limits.cpu: "20"

  limits.memory: 40Gi
```

---

# Why ResourceQuota?

ResourceQuota helps prevent one namespace from consuming all cluster resources.

Example:

```text
Team A
   ↓
Quota
   ↓
Controlled Usage
```

---

# LimitRange

LimitRange can define default or allowed resource values within a namespace.

Example:

```yaml
apiVersion: v1
kind: LimitRange

metadata:
  name: container-limits

spec:

  limits:

    - type: Container

      default:
        cpu: "500m"
        memory: "512Mi"

      defaultRequest:
        cpu: "100m"
        memory: "128Mi"
```

---

# ResourceQuota vs LimitRange

| Resource | Purpose |
|---|---|
| ResourceQuota | Namespace-wide resource limits |
| LimitRange | Per-object/container defaults and constraints |

---

# Namespace Resource Management

A multi-team cluster can use:

```text
Namespace
+
ResourceQuota
+
LimitRange
+
RBAC
```

This improves governance and resource isolation.

---

# CPU Optimization

CPU optimization can involve:

```text
Right-Sized Requests
Appropriate Limits
HPA
Efficient Applications
Node Packing
```

---

# CPU Throttling

When CPU limits are configured, a container may be throttled when it reaches its CPU limit.

High throttling can cause:

```text
Latency
Slow Requests
Poor Performance
```

Monitor before blindly lowering CPU limits.

---

# Memory Optimization

Memory optimization involves:

```text
Right-Sized Requests
Appropriate Limits
Memory Leak Detection
Application Tuning
Garbage Collection
```

---

# OOMKilled

A container can be terminated after exceeding its memory limit.

Check:

```bash
kubectl describe pod <pod-name>
```

Look for:

```text
OOMKilled
```

---

# Memory Pressure

A node under memory pressure may begin evicting Pods according to Kubernetes eviction behavior.

Check:

```bash
kubectl describe node <node>
```

---

# Evictions

Eviction may occur because of:

```text
Memory Pressure
Disk Pressure
PID Pressure
```

---

# Ephemeral Storage

Containers can consume node-local ephemeral storage through:

```text
Writable Container Layer
Logs
EmptyDir
Temporary Files
```

---

# Ephemeral Storage Requests

Example:

```yaml
resources:

  requests:
    ephemeral-storage: "1Gi"

  limits:
    ephemeral-storage: "2Gi"
```

---

# Storage Optimization

Optimize:

```text
Persistent Volumes
Ephemeral Storage
Snapshots
Retention
Data Duplication
```

---

# Persistent Volume Optimization

Review:

```text
Requested Size
Actual Usage
StorageClass
Performance
IOPS
Throughput
Retention
```

---

# Oversized PVC

Example:

```text
PVC = 1Ti
Actual = 50Gi
```

This may indicate an opportunity for optimization, depending on the storage backend and expansion/shrink capabilities.

---

# Image Optimization

Large container images increase:

```text
Pull Time
Disk Usage
Network Traffic
Startup Time
```

Use:

```text
Minimal Base Images
Multi-Stage Builds
Layer Optimization
Unused Package Removal
```

---

# Image Optimization Example

Instead of:

```text
Large OS Image
+
Build Tools
+
Application
```

use:

```text
Build Stage
     ↓
Minimal Runtime Image
```

---

# Network Optimization

Network optimization includes:

```text
Reduce Unnecessary Traffic
Efficient Service Communication
Connection Reuse
Compression Where Appropriate
Caching
```

---

# DNS Optimization

Excessive DNS requests can increase:

```text
CoreDNS Load
Network Traffic
Application Latency
```

Applications should use sensible DNS behavior and connection reuse.

---

# Logging Optimization

Logs can consume substantial:

```text
CPU
Memory
Disk
Network
Storage
```

Use:

```text
Appropriate Log Levels
Retention
Sampling
Centralized Storage
```

---

# Monitoring Optimization

Metrics systems can also consume resources.

Optimize:

```text
Scrape Frequency
Metric Cardinality
Retention
Label Design
```

---

# High Cardinality

A metric with too many unique label combinations can create excessive time-series data.

Avoid unnecessary labels such as:

```text
request_id
user_id
session_id
```

in high-volume metrics.

---

# Idle Resources

Identify:

```text
Unused Deployments
Unused Services
Idle Load Balancers
Unused PVCs
Old Jobs
Unused Namespaces
```

---

# Resource Cleanup

Regular cleanup reduces:

```text
Cost
Complexity
Storage Usage
Operational Noise
```

---

# HPA

Horizontal Pod Autoscaler adjusts the number of Pod replicas.

Conceptually:

```text
Traffic
 ↓
CPU / Memory / Custom Metric
 ↓
HPA
 ↓
Replica Count
```

---

# HPA Example

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler

metadata:
  name: api-hpa

spec:

  scaleTargetRef:

    apiVersion: apps/v1
    kind: Deployment
    name: api

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

# HPA Optimization

Avoid:

```text
minReplicas = 1
```

for critical workloads unless the availability requirements support it.

Consider:

```text
minReplicas
maxReplicas
Scale-Up Behavior
Scale-Down Behavior
Metrics
Startup Time
```

---

# VPA

Vertical Pod Autoscaler adjusts Pod resource requests and limits based on observed usage, depending on its configured mode and implementation.

Conceptually:

```text
Usage
 ↓
VPA
 ↓
Recommended Resources
```

---

# VPA Modes

Common modes include:

```text
Off
Initial
Recreate
Auto
```

The exact behavior depends on the VPA version and configuration.

---

# VPA Use Case

VPA is useful when:

```text
Workload Replica Count Is Stable
+
Resource Requirements Change
```

---

# HPA vs VPA

| HPA | VPA |
|---|---|
| Changes replica count | Changes resource sizing |
| Horizontal scaling | Vertical scaling |
| Useful for variable traffic | Useful for changing resource needs |

---

# HPA and VPA Together

Using HPA and VPA together requires careful metric design.

Avoid having both mechanisms independently manipulate the same resource signal in conflicting ways.

---

# Cluster Autoscaler

Cluster Autoscaler changes node count based on scheduling needs and node utilization policies supported by the environment.

Conceptually:

```text
Pending Pods
     ↓
Insufficient Capacity
     ↓
Cluster Autoscaler
     ↓
New Node
```

---

# Cluster Autoscaler Scale Down

When nodes become unnecessary:

```text
Low Utilization
 ↓
Evaluate Constraints
 ↓
Remove Node
```

It must respect workload and scheduling constraints.

---

# HPA + Cluster Autoscaler

A common architecture:

```text
Traffic
 ↓
HPA
 ↓
More Pods
 ↓
Insufficient Node Capacity
 ↓
Cluster Autoscaler
 ↓
More Nodes
```

---

# Autoscaling Feedback Loop

```text
Load Increase
     ↓
HPA
     ↓
More Pods
     ↓
More Node Capacity
     ↓
Cluster Autoscaler
```

During decreasing demand:

```text
Load Decrease
     ↓
HPA
     ↓
Fewer Pods
     ↓
Unused Node Capacity
     ↓
Cluster Autoscaler
     ↓
Fewer Nodes
```

---

# Autoscaling Risks

Poor configuration can cause:

```text
Scaling Oscillation
Slow Recovery
Excessive Cost
Insufficient Capacity
Application Instability
```

---

# Priority Classes

Priority classes assign relative importance to Pods.

Example:

```yaml
apiVersion: scheduling.k8s.io/v1
kind: PriorityClass

metadata:
  name: critical

value: 100000

globalDefault: false

description: "Critical workloads"
```

---

# Preemption

When a high-priority Pod cannot be scheduled, Kubernetes may preempt lower-priority Pods if configured and appropriate.

Conceptually:

```text
High Priority Pod
       ↓
No Capacity
       ↓
Lower Priority Pod
       ↓
Preempted
       ↓
High Priority Pod Scheduled
```

---

# Resource Optimization and Priority

Use priority carefully.

Do not mark everything:

```text
Critical
```

or priority loses meaning.

---

# Taints and Tolerations

Taints can reserve nodes for specific workloads.

Example:

```text
Dedicated Node
   ↓
Taint
   ↓
Only Tolerating Pods
```

This can improve isolation but may reduce overall utilization.

---

# Node Affinity

Node affinity can place workloads on appropriate nodes.

Example:

```text
GPU Workload
   ↓
GPU Node
```

But strict affinity can reduce scheduling flexibility.

---

# Topology Spread

Topology spread can improve resilience:

```text
Zone A
Zone B
Zone C
```

but strict spread constraints may make packing less efficient.

Optimization must balance:

```text
Availability
+
Utilization
```

---

# Cost Optimization

Kubernetes cost optimization includes:

```text
Right-Sizing
Autoscaling
Node Selection
Spot / Preemptible Capacity
Idle Resource Cleanup
Storage Optimization
Logging Optimization
Monitoring Optimization
```

---

# Spot / Preemptible Nodes

These lower-cost nodes can be useful for workloads that tolerate interruption.

Suitable examples:

```text
Batch Jobs
CI Workloads
Stateless Workers
Fault-Tolerant Processing
```

Avoid placing critical workloads on interruptible capacity unless the architecture explicitly supports it.

---

# Node Pools

Different workloads can use different node pools.

Example:

```text
General Pool
GPU Pool
Memory-Optimized Pool
Compute-Optimized Pool
Spot Pool
```

---

# Specialized Hardware

Do not schedule ordinary workloads onto expensive specialized nodes unless necessary.

Example:

```text
GPU Node
 ↓
GPU Workload
```

---

# Resource Efficiency Metrics

Important metrics include:

```text
CPU Utilization
Memory Utilization
Requested / Allocatable Ratio
Actual / Requested Ratio
Pod Density
Node Utilization
Cost per Workload
```

---

# Requested vs Actual Usage

A useful metric:

```text
Actual Usage / Requested Resource
```

Example:

```text
Request = 2 CPU
Actual = 500m

Efficiency = 25%
```

Very low values may indicate over-requesting.

---

# Utilization Ratio

Conceptually:

```text
Utilization =
Actual Usage / Allocated Capacity
```

Use appropriate time windows and percentiles rather than relying only on a single instantaneous value.

---

# Percentiles

For production sizing, consider:

```text
P50
P90
P95
P99
```

Example:

```text
P95 CPU = 800m
```

This may be more useful for capacity planning than average usage alone.

---

# Capacity Planning

Capacity planning estimates:

```text
Current Demand
+
Growth
+
Failure Headroom
+
Maintenance Headroom
```

---

# Capacity Formula

Conceptually:

```text
Required Capacity =
Expected Demand
+
Headroom
+
Failure Reserve
```

---

# Resource Fragmentation

A cluster may have enough total CPU but still fail to schedule a Pod.

Example:

```text
Node-1 → 500m free
Node-2 → 500m free
```

Total:

```text
1 CPU
```

But a Pod requiring:

```text
1 CPU
```

cannot fit on either node.

This is resource fragmentation.

---

# Bin Packing and Fragmentation

Better packing can reduce fragmentation:

```text
Node-1
 ├── Pod A
 ├── Pod B
 └── Pod C
```

But excessive packing can reduce failure headroom.

---

# Resource Optimization Strategy

Use:

```text
Measure
 ↓
Right-Size
 ↓
Pack Efficiently
 ↓
Autoscale
 ↓
Maintain Headroom
 ↓
Monitor
```

---

# Multi-Tenant Optimization

For multiple teams:

```text
Namespace
+
ResourceQuota
+
LimitRange
+
RBAC
+
Cost Allocation
```

---

# Cost Allocation

Track cost by:

```text
Team
Namespace
Application
Environment
Workload
```

This enables:

```text
Cost Visibility
Accountability
Optimization
```

---

# Production Optimization

A production cluster should optimize:

```text
Cost
Performance
Reliability
Availability
Security
```

not cost alone.

---

# Optimization Trade-Off

Example:

```text
Reduce Replicas
 ↓
Lower Cost
 ↓
Lower Availability
```

Therefore:

```text
Cost Optimization
≠
Remove Redundancy
```

---

# Resource Optimization and HA

HA requires spare capacity.

Therefore:

```text
100% Utilization
```

is usually not an appropriate production target.

---

# Resource Optimization and DR

DR environments can optimize cost through:

```text
Cold Standby
Warm Standby
Reduced Capacity
On-Demand Scaling
```

depending on RTO requirements.

---

# Resource Optimization Runbook

A basic optimization process:

```text
1. Collect Metrics
2. Identify Waste
3. Identify Bottlenecks
4. Right-Size Resources
5. Review Autoscaling
6. Review Node Pools
7. Review Storage
8. Review Logging
9. Review Monitoring
10. Validate Performance
11. Measure Cost
12. Repeat
```

---

# Common Mistakes

## 1. Setting Requests Too High

```text
Actual = 500m
Request = 4 CPU
```

This wastes schedulable capacity.

---

## 2. Setting Requests Too Low

```text
Actual = 2 CPU
Request = 100m
```

This may create scheduling and performance problems.

---

## 3. Ignoring Memory

Memory problems can result in:

```text
OOMKilled
Eviction
Node Pressure
```

---

## 4. Setting CPU Limits Blindly

Aggressive CPU limits may introduce throttling.

---

## 5. Removing All Headroom

A cluster running near saturation has little room for:

```text
Traffic Spikes
Node Failures
Maintenance
```

---

## 6. Using HPA Without Capacity

More replicas require more nodes.

---

## 7. Using VPA Without Understanding Its Mode

Some VPA modes may require Pod restarts/recreation to apply recommendations.

---

## 8. Using HPA and VPA Carelessly Together

Conflicting scaling behavior can occur if both independently react to overlapping signals.

---

## 9. Ignoring Fragmentation

Total free resources may not be usable for a specific Pod.

---

## 10. Overusing Specialized Nodes

Expensive nodes should be reserved for workloads that need them.

---

## 11. Ignoring Logging Costs

High-volume logs can become expensive.

---

## 12. Optimizing Cost at the Expense of Reliability

The cheapest architecture is not necessarily the best architecture.

---

# Best Practices

### 1. Measure Before Optimizing

Use actual workload data.

---

### 2. Right-Size Requests

Base requests on observed usage and workload behavior.

---

### 3. Set Appropriate Limits

Avoid arbitrary limits.

---

### 4. Maintain Headroom

Keep enough capacity for:

```text
Spikes
Failures
Maintenance
```

---

### 5. Use Autoscaling

Use:

```text
HPA
VPA
Cluster Autoscaler
```

where appropriate.

---

### 6. Use ResourceQuota

Prevent namespace-level resource abuse.

---

### 7. Use LimitRange

Provide sensible defaults and constraints.

---

### 8. Optimize Node Pools

Match workloads to appropriate infrastructure.

---

### 9. Clean Unused Resources

Regularly review:

```text
PVC
Jobs
ReplicaSets
Load Balancers
Images
Namespaces
```

---

### 10. Monitor Efficiency

Track:

```text
Actual / Requested
Requested / Allocatable
Cost / Workload
```

---

# Hands-on Lab 1 – Resource Requests

Create:

```yaml
resources:

  requests:
    cpu: "250m"
    memory: "256Mi"

  limits:
    cpu: "500m"
    memory: "512Mi"
```

Deploy it and inspect scheduling.

---

# Hands-on Lab 2 – ResourceQuota

Create:

```yaml
apiVersion: v1
kind: ResourceQuota

metadata:
  name: team-quota

spec:

  requests.cpu: "2"
  requests.memory: 4Gi
  limits.cpu: "4"
  limits.memory: 8Gi
```

Deploy workloads and observe quota enforcement.

---

# Hands-on Lab 3 – LimitRange

Create namespace defaults:

```yaml
apiVersion: v1
kind: LimitRange

metadata:
  name: defaults

spec:

  limits:

    - type: Container

      default:
        cpu: "500m"
        memory: "512Mi"

      defaultRequest:
        cpu: "100m"
        memory: "128Mi"
```

Deploy a container without explicit resources.

Observe the resulting Pod specification.

---

# Hands-on Lab 4 – QoS Classes

Create three Pods:

```text
Guaranteed
Burstable
BestEffort
```

Check:

```bash
kubectl get pod <pod-name> \
  -o jsonpath='{.status.qosClass}'
```

---

# Hands-on Lab 5 – CPU Usage

Deploy a workload with CPU requests.

Check:

```bash
kubectl top pods
```

Compare:

```text
Request
vs
Actual Usage
```

---

# Hands-on Lab 6 – Memory Usage

Deploy a memory-consuming test application.

Monitor:

```bash
kubectl top pod <pod-name>
```

Observe memory behavior.

---

# Hands-on Lab 7 – OOMKilled

In a disposable environment, create a Pod with a low memory limit.

Cause controlled memory consumption.

Inspect:

```bash
kubectl describe pod <pod-name>
```

Observe:

```text
OOMKilled
```

---

# Hands-on Lab 8 – CPU Throttling

Create a workload with a deliberately restrictive CPU limit in a test environment.

Generate CPU load.

Observe application performance and throttling metrics where available.

---

# Hands-on Lab 9 – HPA

Deploy an application and configure HPA.

Example:

```bash
kubectl autoscale deployment web \
  --cpu-percent=70 \
  --min=2 \
  --max=10
```

Check:

```bash
kubectl get hpa
```

---

# Hands-on Lab 10 – HPA Load Test

Generate controlled traffic.

Observe:

```text
Traffic
 ↓
CPU
 ↓
HPA
 ↓
Replicas
```

---

# Hands-on Lab 11 – VPA

Install VPA in a test cluster.

Create a VPA recommendation.

Observe:

```text
Current Resources
Recommended Resources
```

Do not blindly apply recommendations to production.

---

# Hands-on Lab 12 – Cluster Autoscaler

In a supported environment:

```text
Create Pending Pods
 ↓
Insufficient Capacity
 ↓
Cluster Autoscaler
 ↓
New Node
```

Observe scaling behavior.

---

# Hands-on Lab 13 – Node Utilization

Inspect:

```bash
kubectl top nodes
```

Identify:

```text
Underutilized Nodes
Highly Utilized Nodes
```

---

# Hands-on Lab 14 – Resource Fragmentation

Create Pods with resource requests that demonstrate:

```text
Total Free CPU ≥ Pod Requirement
```

but:

```text
No Individual Node Can Fit the Pod
```

Observe scheduling behavior.

---

# Hands-on Lab 15 – Pod Density

Deploy multiple small workloads.

Observe:

```text
Pods per Node
CPU
Memory
Network
```

---

# Hands-on Lab 16 – Ephemeral Storage

Create a Pod that uses:

```yaml
resources:

  requests:
    ephemeral-storage: "500Mi"

  limits:
    ephemeral-storage: "1Gi"
```

Observe node storage behavior.

---

# Hands-on Lab 17 – Image Optimization

Create two images:

```text
Large Image
Minimal Image
```

Compare:

```text
Image Size
Pull Time
Disk Usage
Startup
```

---

# Hands-on Lab 18 – Resource Right-Sizing

Collect workload metrics for several days.

Compare:

```text
Requests
P50
P95
P99
Peak
```

Adjust requests.

Measure the effect on:

```text
Utilization
Scheduling
Performance
Cost
```

---

# Hands-on Lab 19 – Cost Optimization

Identify:

```text
Idle Nodes
Idle Pods
Unused PVCs
Old Jobs
Large Images
```

Clean them in a test environment.

Estimate the resource savings.

---

# Hands-on Lab 20 – Full Optimization Exercise

Optimize a test cluster:

```text
Measure
 ↓
Right-Size
 ↓
Configure Quotas
 ↓
Configure Autoscaling
 ↓
Optimize Nodes
 ↓
Clean Resources
 ↓
Validate Performance
 ↓
Measure Cost
```

Document:

```text
Before
After
CPU
Memory
Node Count
Pod Count
Cost
Performance
Availability
```

---

# Quick Revision

## Resource Request

```text
Amount considered for scheduling
```

---

## Resource Limit

```text
Configured maximum resource boundary
```

---

## Guaranteed

```text
Predictable resource configuration with required requests and limits
```

---

## Burstable

```text
Pod with resource configuration that does not qualify as Guaranteed
```

---

## BestEffort

```text
No CPU or memory requests/limits configured
```

---

## ResourceQuota

```text
Namespace-wide resource consumption control
```

---

## LimitRange

```text
Per-object resource defaults and constraints
```

---

## Right-Sizing

```text
Matching resource configuration to actual workload needs
```

---

## HPA

```text
Scales Pod replicas
```

---

## VPA

```text
Adjusts/recommends Pod resource sizing
```

---

## Cluster Autoscaler

```text
Adjusts node capacity based on cluster scheduling needs
```

---

## Bin Packing

```text
Efficiently placing workloads onto nodes
```

---

## Headroom

```text
Unused capacity reserved for spikes, failures, and operations
```

---

## OOMKilled

```text
Container terminated because of memory exhaustion / limit enforcement
```

---

## CPU Throttling

```text
CPU usage restricted by configured CPU limits/cgroup enforcement
```

---

# Essential Commands

Check node resources:

```bash
kubectl describe nodes
```

Check resource usage:

```bash
kubectl top nodes
```

Check Pod usage:

```bash
kubectl top pods -A
```

Check Pod resources:

```bash
kubectl get pod <pod-name> -o yaml
```

Check QoS:

```bash
kubectl get pod <pod-name> \
  -o jsonpath='{.status.qosClass}'
```

Check quotas:

```bash
kubectl get resourcequota -A
```

Describe quota:

```bash
kubectl describe resourcequota <quota-name>
```

Check LimitRanges:

```bash
kubectl get limitrange -A
```

Describe LimitRange:

```bash
kubectl describe limitrange <name>
```

Check HPA:

```bash
kubectl get hpa -A
```

Describe HPA:

```bash
kubectl describe hpa <hpa-name>
```

Check VPA:

```bash
kubectl get vpa -A
```

Check Pods:

```bash
kubectl get pods -A
```

Check node placement:

```bash
kubectl get pods -A -o wide
```

Check nodes:

```bash
kubectl get nodes -o wide
```

Check PDB:

```bash
kubectl get pdb -A
```

Check events:

```bash
kubectl get events -A
```

Check PVCs:

```bash
kubectl get pvc -A
```

Check StorageClasses:

```bash
kubectl get storageclass
```

---

# Interview Questions

## Basic

- What is resource optimization in Kubernetes?
- What are CPU requests?
- What are memory requests?
- What are CPU limits?
- What are memory limits?
- What is the difference between requests and limits?
- What are Kubernetes QoS classes?
- What is Guaranteed QoS?
- What is Burstable QoS?
- What is BestEffort QoS?
- What is ResourceQuota?
- What is LimitRange?
- What is HPA?
- What is VPA?
- What is Cluster Autoscaler?
- What is right-sizing?
- What is bin packing?
- What is resource fragmentation?

---

## Intermediate

- Why are resource requests important for scheduling?
- What happens when a container exceeds its memory limit?
- What is CPU throttling?
- Why can excessive CPU limits cause performance problems?
- How do you identify overprovisioned workloads?
- How do you identify underprovisioned workloads?
- How do ResourceQuota and LimitRange differ?
- How does HPA work?
- How does VPA work?
- How does Cluster Autoscaler work?
- How do HPA and Cluster Autoscaler work together?
- Why is spare capacity important?
- How do you optimize node utilization?
- How do you optimize container images?
- How do you optimize logging costs?

---

## Advanced

- How would you right-size resources for a production application?
- How would you optimize a 1,000-node Kubernetes cluster?
- How would you balance cost and high availability?
- How would you prevent resource starvation between teams?
- How would you design namespace-level resource governance?
- How would you use HPA, VPA, and Cluster Autoscaler together?
- How would you diagnose OOMKilled Pods?
- How would you diagnose CPU throttling?
- How would you solve resource fragmentation?
- How would you optimize workloads across multiple node pools?
- How would you optimize a cluster without reducing availability?
- How would you optimize Kubernetes for cloud cost?
- How would you determine appropriate CPU and memory requests?
- How would you optimize a multi-tenant Kubernetes platform?

---

# Interview Scenario 1

### Question

> What is the difference between a resource request and a resource limit?

### Answer

A request represents the resource amount Kubernetes considers when scheduling a Pod.

A limit defines the configured maximum boundary for the container.

Example:

```yaml
resources:

  requests:
    cpu: "500m"
    memory: "512Mi"

  limits:
    cpu: "1"
    memory: "1Gi"
```

Here:

```text
Request:
500m CPU
512Mi Memory

Limit:
1 CPU
1Gi Memory
```

---

# Interview Scenario 2

### Question

> What happens when a container exceeds its memory limit?

### Answer

The container can be terminated due to memory exhaustion and may show:

```text
OOMKilled
```

Check:

```bash
kubectl describe pod <pod-name>
```

---

# Interview Scenario 3

### Question

> Why should resource requests be configured?

### Answer

Requests help Kubernetes:

```text
Schedule Pods
Plan Capacity
Perform Autoscaling Decisions
Manage Resource Allocation
```

Without realistic requests, scheduling and capacity decisions can become inaccurate.

---

# Interview Scenario 4

### Question

> How would you identify overprovisioned Pods?

### Answer

Compare:

```text
Resource Requests
vs
Actual Usage
```

For example:

```text
Request = 4 CPU
P95 Usage = 500m
```

This may indicate the request is much higher than necessary, although workload spikes and failure headroom must also be considered.

---

# Interview Scenario 5

### Question

> How would you identify underprovisioned Pods?

### Answer

Look for:

```text
High CPU Saturation
CPU Throttling
OOMKilled
Memory Pressure
High Latency
Frequent Restarts
```

Then compare actual usage against configured requests and limits.

---

# Interview Scenario 6

### Question

> How does HPA help resource optimization?

### Answer

HPA changes the number of replicas based on configured metrics.

```text
Low Demand
 ↓
Fewer Pods

High Demand
 ↓
More Pods
```

This allows capacity to follow workload demand.

---

# Interview Scenario 7

### Question

> How does Cluster Autoscaler work with HPA?

### Answer

The sequence can be:

```text
Traffic Increase
 ↓
HPA Increases Replicas
 ↓
Pods Cannot Fit
 ↓
Pods Pending
 ↓
Cluster Autoscaler Adds Nodes
 ↓
Pods Scheduled
```

---

# Interview Scenario 8

### Question

> Why shouldn't you run a production cluster at 100% utilization?

### Answer

Because production systems need capacity for:

```text
Traffic Spikes
Node Failures
Rolling Updates
Maintenance
Rescheduling
```

High utilization without headroom increases operational risk.

---

# Interview Scenario 9

### Question

> How would you optimize a multi-tenant Kubernetes cluster?

### Answer

Use:

```text
Namespaces
+
ResourceQuota
+
LimitRange
+
RBAC
+
Priority Classes
+
Node Policies
+
Cost Allocation
+
Monitoring
```

This prevents one tenant from consuming disproportionate resources.

---

# Interview Scenario 10

### Question

> How would you optimize Kubernetes costs without reducing availability?

### Answer

Focus on waste rather than simply removing redundancy:

```text
Right-Size Requests
+
Remove Idle Resources
+
Use Autoscaling
+
Optimize Node Pools
+
Use Suitable Lower-Cost Capacity
+
Optimize Storage
+
Optimize Logging
+
Maintain HA Headroom
```

---

# Production Optimization Checklist

```text
☑ CPU requests reviewed
☑ Memory requests reviewed
☑ CPU limits reviewed
☑ Memory limits reviewed
☑ QoS classes reviewed
☑ ResourceQuota configured
☑ LimitRange configured
☑ HPA reviewed
☑ VPA reviewed
☑ Cluster Autoscaler reviewed
☑ Node utilization monitored
☑ Pod density reviewed
☑ Resource fragmentation reviewed
☑ Headroom maintained
☑ N+1 capacity considered
☑ OOMKilled monitored
☑ CPU throttling monitored
☑ Disk pressure monitored
☑ Ephemeral storage reviewed
☑ PVC utilization reviewed
☑ Container images optimized
☑ Logging optimized
☑ Monitoring cardinality reviewed
☑ Idle resources cleaned
☑ Cost allocation configured
☑ Specialized node pools optimized
☑ Availability requirements preserved
```

---

# Chapter Summary

Resource optimization is about achieving the right balance between:

```text
Performance
+
Availability
+
Reliability
+
Cost
```

The most important Kubernetes resource controls are:

```text
Requests
Limits
ResourceQuota
LimitRange
HPA
VPA
Cluster Autoscaler
Priority Classes
```

A mature optimization strategy follows:

```text
Measure
 ↓
Profile
 ↓
Right-Size
 ↓
Schedule
 ↓
Autoscale
 ↓
Maintain Headroom
 ↓
Monitor
 ↓
Optimize Again
```

Resource optimization should never mean simply reducing resource allocations.

The correct objective is:

> **Use the minimum practical resources required to meet performance, reliability, availability, and recovery objectives while maintaining sufficient capacity for traffic spikes, failures, maintenance, and future growth.**

---

## Next Chapter

# Chapter 72 – Vulnerability Management

Topics will include:

- Kubernetes Vulnerability Management Fundamentals
- Vulnerability Lifecycle
- Asset Discovery
- Kubernetes Attack Surface
- Vulnerability Identification
- Vulnerability Assessment
- CVE
- CVSS
- Severity
- Exploitability
- Risk Scoring
- Kubernetes Version Vulnerabilities
- API Server Vulnerabilities
- kubelet Vulnerabilities
- etcd Vulnerabilities
- Container Runtime Vulnerabilities
- CNI Vulnerabilities
- CSI Vulnerabilities
- Container Image Vulnerabilities
- Base Image Vulnerabilities
- Application Dependencies
- OS Package Vulnerabilities
- Helm Chart Vulnerabilities
- Manifest Security
- Configuration Vulnerabilities
- RBAC Misconfiguration
- Network Policy Gaps
- Pod Security Issues
- Exposed Services
- Insecure Ingress
- Secret Exposure
- Supply Chain Risks
- SBOM
- Image Scanning
- Registry Security
- Vulnerability Scanners
- Trivy
- Grype
- Kube-bench
- Kubescape
- Admission-Time Scanning
- Runtime Scanning
- Continuous Vulnerability Management
- Vulnerability Prioritization
- Risk-Based Remediation
- Patch Management
- Kubernetes Upgrades
- Node Patching
- Image Updates
- Dependency Updates
- Emergency Patching
- Compensating Controls
- Vulnerability Exceptions
- False Positives
- Security Advisories
- CVE Monitoring
- Vulnerability Reporting
- Security Dashboards
- Compliance
- Vulnerability SLAs
- Remediation Tracking
- Verification
- Rescanning
- Security Automation
- CI/CD Integration
- GitOps Security
- Production Vulnerability Management
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---