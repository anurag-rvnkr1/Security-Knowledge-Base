# Chapter 58 – Monitoring

## Overview

Monitoring is the process of continuously observing the health, performance, availability, and behavior of Kubernetes workloads and infrastructure.

Logging tells us:

```text
What happened?
```

Monitoring tells us:

```text
How is the system behaving?
```

Tracing tells us:

```text
Where did a request travel?
```

A production Kubernetes observability platform combines all three:

```text
                Observability
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
       Logs        Metrics      Traces
        │            │            │
        ▼            ▼            ▼
     Events       Trends       Requests
```

Kubernetes monitoring should cover multiple layers:

```text
Application
    ↓
Container
    ↓
Pod
    ↓
Node
    ↓
Cluster
    ↓
Control Plane
    ↓
External Dependencies
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes monitoring fundamentals
- Monitoring vs observability
- Monitoring architecture
- Infrastructure monitoring
- Cluster monitoring
- Node monitoring
- Pod monitoring
- Container monitoring
- Application monitoring
- Kubernetes metrics
- Resource metrics
- CPU metrics
- Memory metrics
- Disk metrics
- Network metrics
- Node health
- Pod health
- Container restarts
- OOMKilled
- CPU throttling
- Resource utilization
- API Server monitoring
- Scheduler monitoring
- Controller Manager monitoring
- Kubelet monitoring
- Control Plane monitoring
- Golden Signals
- RED Method
- USE Method
- SLI
- SLO
- SLA
- Monitoring dashboards
- Alerting
- Thresholds
- Baselines
- Anomaly detection
- Capacity planning
- Kubernetes Events
- Metrics collection
- Metrics aggregation
- Monitoring agents
- Node Exporter
- Metrics Server
- Prometheus
- Grafana
- Production monitoring architecture
- Monitoring security
- Monitoring best practices
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Monitoring?

Monitoring is the continuous collection and analysis of system information.

Example:

```text
CPU Usage
Memory Usage
Disk Usage
Network Traffic
Pod Restarts
Request Rate
Error Rate
Latency
```

Monitoring helps answer:

```text
Is the system healthy?
```

---

# Why Kubernetes Monitoring Matters

Kubernetes is a distributed system.

A failure in one component can affect another.

For example:

```text
Node Memory Pressure
       ↓
Pod Eviction
       ↓
Application Capacity Reduced
       ↓
Request Latency Increased
       ↓
Errors Increase
```

Without monitoring, the relationship may not be obvious.

---

# Monitoring vs Observability

Monitoring usually focuses on predefined signals:

```text
CPU
Memory
Availability
Errors
Latency
```

Observability is broader.

It asks:

```text
Can we understand the internal state of the system from its outputs?
```

Observability commonly uses:

```text
Logs
Metrics
Traces
Events
Profiles
```

---

# Monitoring Architecture

A simplified monitoring architecture:

```text
Kubernetes
     │
     ▼
Metrics Sources
     │
     ▼
Metrics Collection
     │
     ▼
Metrics Storage
     │
     ▼
Query Engine
     │
     ├── Dashboard
     └── Alerting
```

---

# What Should Be Monitored?

At minimum:

```text
Cluster
Nodes
Pods
Containers
Applications
Control Plane
Network
Storage
```

---

# Kubernetes Monitoring Layers

```text
Layer 1 → Application
Layer 2 → Container
Layer 3 → Pod
Layer 4 → Node
Layer 5 → Cluster
Layer 6 → Control Plane
Layer 7 → External Dependencies
```

---

# Application Monitoring

Application metrics can include:

```text
Request Rate
Error Rate
Latency
Active Connections
Queue Length
Database Connections
Cache Hit Rate
```

---

# Container Monitoring

Monitor:

```text
CPU
Memory
Network
Filesystem
Restarts
OOMKilled
```

---

# Pod Monitoring

Important Pod signals:

```text
Pod Status
Ready Containers
Restarts
CPU
Memory
Scheduling
Events
```

---

# Node Monitoring

Important Node signals:

```text
CPU
Memory
Disk
Network
Filesystem
Conditions
Pressure
Kubelet Health
```

---

# Cluster Monitoring

Cluster-level metrics include:

```text
Node Count
Pod Count
Pending Pods
Resource Utilization
API Server Health
Scheduler Health
Controller Health
```

---

# Control Plane Monitoring

Monitor:

```text
API Server
Scheduler
Controller Manager
etcd
```

depending on the cluster architecture and access to control-plane metrics.

---

# API Server Monitoring

Important signals:

```text
Request Rate
Request Latency
Error Rate
HTTP Status Codes
Request Saturation
Active Connections
```

---

# Scheduler Monitoring

Monitor:

```text
Scheduling Rate
Scheduling Latency
Scheduling Failures
Pending Pods
```

---

# Controller Manager Monitoring

Monitor:

```text
Controller Queue
Reconciliation Latency
Errors
Workqueue Depth
```

---

# Kubelet Monitoring

Monitor:

```text
Pod Operations
Container Operations
Runtime Errors
Resource Usage
Probe Failures
Node Health
```

---

# etcd Monitoring

For clusters where etcd metrics are available, monitor:

```text
Request Latency
Disk Performance
Database Size
Leader Status
Commit Latency
```

etcd is critical because Kubernetes control-plane state depends on it.

---

# Metrics

A metric is a numerical measurement describing system behavior.

Example:

```text
container_cpu_usage_seconds_total
```

or:

```text
http_requests_total
```

---

# Metric Components

A metric usually has:

```text
Name
Value
Labels
Timestamp
```

Example conceptually:

```text
http_requests_total{
    service="backend",
    status="200"
}
```

---

# Metric Types

Common Prometheus metric types include:

```text
Counter
Gauge
Histogram
Summary
```

---

# Counter

A Counter generally increases over time.

Example:

```text
http_requests_total
```

Conceptually:

```text
100
 ↓
101
 ↓
102
 ↓
103
```

Counters can reset when the process restarts.

---

# Gauge

A Gauge represents a value that can increase or decrease.

Examples:

```text
Memory Usage
CPU Temperature
Active Connections
Queue Size
```

---

# Histogram

Histograms measure distributions.

Common use:

```text
Request Latency
```

Example buckets:

```text
< 10ms
< 50ms
< 100ms
< 500ms
< 1s
```

---

# Summary

A Summary can provide quantile-related observations depending on implementation.

For many Kubernetes monitoring architectures, Histograms are preferred when aggregation across instances is important.

---

# CPU Monitoring

CPU metrics help identify:

```text
High Utilization
CPU Saturation
CPU Throttling
Capacity Problems
```

---

# CPU Usage

Example:

```text
Pod A → 100m
Pod B → 500m
Pod C → 1500m
```

Remember:

```text
1000m = 1 CPU
```

---

# CPU Request

Example:

```yaml
resources:

  requests:

    cpu: "500m"
```

The scheduler uses requests when deciding placement.

---

# CPU Limit

Example:

```yaml
resources:

  limits:

    cpu: "1"
```

The container can be throttled when it attempts to use more CPU than its configured limit.

---

# CPU Throttling

If a container repeatedly reaches its CPU limit:

```text
CPU Demand
    ↓
CPU Limit
    ↓
Throttling
    ↓
Application Slower
```

Monitor CPU throttling when diagnosing latency or performance problems.

---

# Memory Monitoring

Monitor:

```text
Working Set
RSS
Memory Requests
Memory Limits
Memory Pressure
OOM Events
```

---

# OOMKilled

OOM means:

```text
Out Of Memory
```

A container may be terminated because it exceeded its memory limit or the node experienced memory pressure.

Check:

```bash
kubectl describe pod <pod>
```

Look for:

```text
OOMKilled
```

---

# Memory Pressure

A node can experience:

```text
MemoryPressure
```

when available memory becomes critically low.

This can lead to:

```text
Pod Eviction
Performance Problems
Process Termination
```

---

# Disk Monitoring

Monitor:

```text
Disk Usage
Filesystem Usage
Inodes
Container Storage
Log Storage
Ephemeral Storage
```

---

# Disk Pressure

Kubernetes nodes can report:

```text
DiskPressure
```

when disk resources become constrained.

Potential causes:

```text
Large Logs
Container Images
Temporary Files
Ephemeral Storage
```

---

# Network Monitoring

Monitor:

```text
Bytes In
Bytes Out
Packets
Errors
Drops
Connections
Latency
```

---

# Network Saturation

High network utilization may cause:

```text
Latency
Packet Loss
Connection Failures
Application Errors
```

---

# Pod Restarts

Restart count is an important signal.

Example:

```text
Pod
 └── Container
      Restarts: 25
```

A high restart count may indicate:

```text
Application Crash
OOMKilled
Probe Failure
Configuration Error
```

---

# Pod Status

Common statuses include:

```text
Pending
Running
Succeeded
Failed
Unknown
```

---

# Pending Pods

A large number of Pending Pods may indicate:

```text
Insufficient CPU
Insufficient Memory
Node Selector
Affinity
Taints
Resource Quotas
Scheduling Constraints
```

---

# Failed Pods

Investigate:

```text
Application Errors
Image Problems
Configuration
Secrets
Volumes
Probes
```

---

# Readiness

A Pod can be running but not ready.

Example:

```text
Running
Ready: False
```

This means:

```text
Process Exists
```

but:

```text
Traffic Should Not Yet Be Sent
```

---

# Liveness

Liveness probes determine whether a container should be restarted.

Poorly configured liveness probes can cause:

```text
Restart Loops
```

---

# Startup Probe

Startup probes help applications that take a long time to initialize.

Architecture:

```text
Container Starts
      ↓
Startup Probe
      ↓
Application Ready
      ↓
Liveness / Readiness
```

---

# Monitoring Probes

Monitor:

```text
Probe Success Rate
Probe Failures
Restart Correlation
Latency
```

---

# Golden Signals

A widely used observability model is:

```text
Latency
Traffic
Errors
Saturation
```

---

# Latency

How long requests take.

Example:

```text
P50 = 50ms
P95 = 200ms
P99 = 700ms
```

---

# Traffic

How much demand the system receives.

Examples:

```text
Requests per second
Messages per second
Transactions per minute
```

---

# Errors

Measure failures:

```text
HTTP 5xx
HTTP 4xx
Timeouts
Failed Jobs
Database Errors
```

---

# Saturation

How close the system is to its capacity.

Examples:

```text
CPU 90%
Memory 95%
Disk 85%
Connection Pool 98%
```

---

# RED Method

RED stands for:

```text
Rate
Errors
Duration
```

Primarily useful for request-driven services.

---

# Rate

Number of requests:

```text
requests/second
```

---

# Errors

Number or percentage of failed requests.

---

# Duration

How long requests take.

---

# USE Method

USE stands for:

```text
Utilization
Saturation
Errors
```

It is particularly useful for infrastructure resources.

---

# Utilization

Example:

```text
CPU = 75%
Memory = 60%
```

---

# Saturation

Example:

```text
CPU queue increasing
Disk I/O queue increasing
```

---

# Errors

Examples:

```text
Network packet errors
Disk errors
Hardware errors
```

---

# RED vs USE

| Method | Best For |
|---|---|
| RED | Services |
| USE | Infrastructure |
| Golden Signals | General service health |

---

# SLI

SLI means:

```text
Service Level Indicator
```

It is a measurable indicator of service behavior.

Example:

```text
Successful Requests / Total Requests
```

---

# SLO

SLO means:

```text
Service Level Objective
```

Example:

```text
99.9% successful requests
```

---

# SLA

SLA means:

```text
Service Level Agreement
```

It is a contractual or business commitment.

---

# SLI vs SLO vs SLA

```text
SLI
=
What we measure
```

```text
SLO
=
What target we want
```

```text
SLA
=
What we contractually promise
```

---

# Example

```text
SLI:
Availability

SLO:
99.9%

SLA:
99.5%
```

---

# Error Budget

If SLO is:

```text
99.9%
```

allowed unavailability is approximately:

```text
0.1%
```

The permitted failure amount is called the:

```text
Error Budget
```

---

# Monitoring Dashboards

A production dashboard may contain:

```text
Cluster Health
Node Health
Pod Health
CPU
Memory
Disk
Network
API Server
Application Metrics
Alerts
```

---

# Cluster Dashboard

Example:

```text
Nodes:             12
Healthy Nodes:     12
Pending Pods:       3
Failed Pods:        0
CPU Utilization:   61%
Memory Utilization:68%
Disk Utilization:  52%
```

---

# Node Dashboard

Track:

```text
CPU
Memory
Disk
Network
Pod Count
Container Count
Pressure Conditions
```

---

# Pod Dashboard

Track:

```text
Status
Restarts
CPU
Memory
Readiness
Network
```

---

# Application Dashboard

Track:

```text
Request Rate
Error Rate
Latency
Saturation
Database Health
Queue Length
```

---

# Alerting

Monitoring without alerting may require humans to constantly watch dashboards.

Alerting automates detection.

Example:

```text
CPU > 90%
   ↓
Alert
```

---

# Good Alerts

Good alerts are:

```text
Actionable
Relevant
Specific
Contextual
Stable
```

---

# Bad Alerts

Avoid alerts such as:

```text
CPU = 81%
```

if there is no meaningful action associated with that condition.

---

# Alert Fatigue

Too many alerts cause:

```text
Alert Fatigue
```

which can lead to:

```text
Ignored Alerts
Missed Incidents
Slow Response
```

---

# Alert Design

An alert should ideally provide:

```text
What happened?
Where?
When?
Severity?
Why it matters?
What should be checked?
```

---

# Example Alert

```text
CRITICAL

Pod:
payment-api-7d8f

Namespace:
production

Condition:
Error rate > 10%

Duration:
10 minutes

Impact:
Payment requests failing
```

---

# Thresholds

Threshold-based monitoring uses conditions such as:

```text
CPU > 90%
Memory > 85%
Disk > 80%
```

Thresholds are simple but can produce false positives if poorly chosen.

---

# Baselines

A baseline describes normal behavior.

Example:

```text
Normal CPU:
40–60%

Current:
95%
```

This may indicate an anomaly.

---

# Anomaly Detection

Anomaly detection attempts to identify behavior that differs from normal patterns.

Example:

```text
Normal:
100 requests/min

Current:
10,000 requests/min
```

Potentially:

```text
Traffic Spike
Attack
Misconfiguration
```

---

# Monitoring Kubernetes Events

Events provide useful operational information.

View:

```bash
kubectl get events
```

Sorted:

```bash
kubectl get events \
  --sort-by=.metadata.creationTimestamp
```

---

# Example Event

```text
FailedScheduling
```

Possible reason:

```text
Insufficient CPU
```

---

# Example Event

```text
FailedMount
```

Possible reason:

```text
Volume unavailable
```

---

# Example Event

```text
BackOff
```

Potentially indicates repeated container startup failures.

---

# Metrics Collection

Metrics can be collected from:

```text
Application
Kubelet
Node
API Server
Scheduler
Controller Manager
Exporters
```

---

# Metrics Aggregation

A monitoring platform can collect metrics from many sources:

```text
Node 1 ─┐
Node 2 ─┤
Node 3 ─┤
Pods ───┤
Apps ───┤
API ────┘
         ↓
     Metrics Store
```

---

# Monitoring Agents

Agents may run:

```text
Per Node
Per Pod
As Sidecars
As DaemonSets
```

---

# DaemonSet Monitoring Agent

A DaemonSet can run an agent on every node.

Example:

```text
Node 1 → Agent
Node 2 → Agent
Node 3 → Agent
```

Common use cases:

```text
Node Metrics
Logs
Security
Telemetry
```

---

# Node Exporter

Node Exporter exposes host-level metrics for Prometheus.

Examples:

```text
CPU
Memory
Disk
Filesystem
Network
```

Architecture:

```text
Node
 ↓
Node Exporter
 ↓
Prometheus
```

---

# Metrics Server

Metrics Server provides resource metrics for Kubernetes workloads and nodes.

Common metrics include:

```text
CPU
Memory
```

It is commonly used by:

```text
kubectl top
HPA
```

---

# Metrics Server vs Prometheus

| Feature | Metrics Server | Prometheus |
|---|---|---|
| CPU/Memory Resource Metrics | Yes | Yes, with appropriate sources |
| Long-Term Storage | No | Yes |
| General Monitoring | Limited | Extensive |
| PromQL | No | Yes |
| HPA Resource Metrics | Commonly | Via adapters/integrations depending on design |

---

# `kubectl top`

If Metrics Server is installed:

```bash
kubectl top nodes
```

Example:

```text
NAME       CPU(cores)   CPU%   MEMORY(bytes)   MEMORY%
worker-1   250m         12%    2Gi            25%
```

---

# Pod Metrics

```bash
kubectl top pods
```

Namespace:

```bash
kubectl top pods -n production
```

---

# Prometheus

Prometheus is a monitoring and time-series database platform widely used in Kubernetes environments.

It provides:

```text
Metrics Collection
Time-Series Storage
PromQL
Alerting Integration
```

---

# Prometheus Architecture

```text
Applications
    │
    ▼
Metrics Endpoints
    │
    ▼
Prometheus
    │
    ├── Storage
    ├── PromQL
    └── Alerting
          │
          ▼
      Alertmanager
```

---

# Pull-Based Monitoring

Prometheus commonly uses a pull model.

```text
Prometheus
    ↓
Scrape
    ↓
/metrics
```

---

# Metrics Endpoint

A service may expose:

```text
/metrics
```

Example:

```text
http_requests_total
http_request_duration_seconds
```

---

# Prometheus Service Discovery

Kubernetes can provide dynamic discovery of:

```text
Pods
Services
Nodes
Endpoints
```

This is important because Kubernetes workloads change frequently.

---

# Prometheus Labels

Example:

```text
http_requests_total{
  namespace="production",
  pod="backend-123",
  status="200"
}
```

Labels enable flexible querying.

---

# High Cardinality

Too many unique label combinations can cause large metric storage and query costs.

Bad example:

```text
request_id
user_id
session_id
```

as metric labels.

These values may create enormous cardinality.

---

# Monitoring Cardinality

Be careful with labels such as:

```text
User ID
Request ID
UUID
Timestamp
Unbounded URLs
```

Prefer bounded labels:

```text
method
status
service
namespace
```

---

# Monitoring and Capacity Planning

Monitoring historical metrics helps forecast:

```text
CPU Growth
Memory Growth
Storage Growth
Network Growth
Pod Growth
```

---

# Capacity Planning Example

Current:

```text
CPU = 50%
```

Growth:

```text
10% per month
```

Forecast:

```text
Future Capacity Requirement
```

---

# Horizontal Scaling

Monitoring can trigger:

```text
More Pods
```

using:

```text
HPA
```

---

# Vertical Scaling

Monitoring can indicate the need for:

```text
Larger CPU/Memory Requests
```

or:

```text
VPA
```

---

# Cluster Scaling

Monitoring can identify:

```text
Insufficient Nodes
```

which may trigger:

```text
Cluster Autoscaler
```

---

# Monitoring and Autoscaling

```text
Metrics
   ↓
HPA
   ↓
More Pods
```

and:

```text
Cluster Resource Demand
   ↓
Cluster Autoscaler
   ↓
More Nodes
```

---

# Monitoring and Troubleshooting

A common workflow:

```text
Alert
 ↓
Dashboard
 ↓
Metrics
 ↓
Logs
 ↓
Events
 ↓
Trace
 ↓
Root Cause
```

---

# Example Incident

Alert:

```text
HTTP 500 > 5%
```

Check metrics:

```text
Latency ↑
```

Check logs:

```text
Database timeout
```

Check database:

```text
Connection pool exhausted
```

Root cause:

```text
Database connection saturation
```

---

# Monitoring Security

Monitoring systems can contain sensitive information.

Protect:

```text
Metrics
Dashboards
Logs
Alerts
Credentials
```

---

# Monitoring RBAC

Restrict access to:

```text
Prometheus
Grafana
Alertmanager
Metrics APIs
```

---

# Monitoring Credentials

Avoid embedding credentials directly in:

```text
Dashboard
Configuration
Scripts
Source Code
```

Use appropriate Secret or identity mechanisms.

---

# Monitoring Availability

Monitoring should itself be highly available for production-critical systems.

Otherwise:

```text
Monitoring Failure
    ↓
No Visibility
```

---

# Monitoring the Monitoring System

Track:

```text
Scrape Failures
Missing Targets
Storage Health
Query Latency
Alert Delivery
Collector Health
```

---

# Monitoring Best Practices

### 1. Monitor the Four Golden Signals

```text
Latency
Traffic
Errors
Saturation
```

---

### 2. Monitor Infrastructure

Track:

```text
CPU
Memory
Disk
Network
```

---

### 3. Monitor Kubernetes Health

Track:

```text
Pods
Nodes
Events
Restarts
Scheduling
```

---

### 4. Monitor Applications

Track:

```text
Rate
Errors
Duration
Dependencies
```

---

### 5. Define SLOs

Do not monitor metrics without understanding service objectives.

---

### 6. Build Actionable Alerts

Every critical alert should have a response path.

---

### 7. Avoid Alert Fatigue

Tune:

```text
Thresholds
Duration
Severity
Aggregation
```

---

### 8. Monitor Capacity

Track long-term resource trends.

---

### 9. Avoid High Cardinality

Keep labels bounded.

---

### 10. Secure Monitoring

Use:

```text
RBAC
TLS
Authentication
Least Privilege
```

---

### 11. Integrate Metrics With Logs and Traces

Use the complete observability model.

---

### 12. Test Monitoring

Simulate:

```text
Pod Failure
Node Failure
High CPU
High Memory
Disk Pressure
Application Errors
```

Verify alerts.

---

# Production Monitoring Checklist

```text
☑ Cluster monitoring
☑ Node monitoring
☑ Pod monitoring
☑ Container monitoring
☑ Application monitoring
☑ Control plane monitoring
☑ CPU metrics
☑ Memory metrics
☑ Disk metrics
☑ Network metrics
☑ Restart monitoring
☑ OOM monitoring
☑ CPU throttling monitoring
☑ Kubernetes events
☑ Golden Signals
☑ RED metrics
☑ USE metrics
☑ SLI definitions
☑ SLO definitions
☑ Alerting
☑ Dashboarding
☑ Capacity planning
☑ Metrics retention
☑ Monitoring RBAC
☑ Monitoring security
☑ Monitoring health checks
```

---

# Hands-on Lab 1 – Node Metrics

If Metrics Server is installed:

```bash
kubectl top nodes
```

Record:

```text
CPU
Memory
```

for each node.

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

Investigate why they consume those resources.

---

# Hands-on Lab 3 – Generate CPU Load

Create a disposable workload that consumes CPU.

Monitor:

```bash
kubectl top pod
```

Observe the change in CPU utilization.

---

# Hands-on Lab 4 – Memory Consumption

Create a controlled test workload with increasing memory usage.

Observe:

```text
Memory Usage
Pod Status
OOMKilled
Restart Count
```

Use a disposable environment.

---

# Hands-on Lab 5 – Monitor Pod Restarts

Run:

```bash
kubectl get pods -A
```

Track:

```text
RESTARTS
```

Identify Pods with unusually high restart counts.

---

# Hands-on Lab 6 – Kubernetes Events

Run:

```bash
kubectl get events \
  --sort-by=.metadata.creationTimestamp
```

Create a scheduling or image-pull failure in a test environment.

Observe the resulting events.

---

# Hands-on Lab 7 – Node Exporter

Deploy Node Exporter in a disposable cluster.

Observe:

```text
CPU
Memory
Disk
Network
```

metrics.

---

# Hands-on Lab 8 – Prometheus

Deploy Prometheus.

Configure it to scrape a test application.

Query:

```text
up
```

Verify the target.

---

# Hands-on Lab 9 – PromQL

Practice queries such as:

```promql
up
```

and:

```promql
rate(http_requests_total[5m])
```

Then explore CPU and memory-related metrics available in your environment.

---

# Hands-on Lab 10 – Grafana Dashboard

Connect Grafana to Prometheus.

Create panels for:

```text
CPU
Memory
Pod Restarts
Request Rate
Error Rate
Latency
```

---

# Hands-on Lab 11 – Alerting

Create a test alert:

```text
CPU > 80%
```

Generate controlled CPU load.

Verify:

```text
Metric
 ↓
Rule
 ↓
Alert
```

---

# Hands-on Lab 12 – SLI and SLO

For a test application define:

```text
SLI:
Successful HTTP Requests
```

Define:

```text
SLO:
99.9%
```

Calculate the approximate error budget.

---

# Hands-on Lab 13 – RED Dashboard

Create panels for:

```text
Rate
Errors
Duration
```

for a test service.

---

# Hands-on Lab 14 – USE Dashboard

For a test node create:

```text
Utilization
Saturation
Errors
```

metrics.

---

# Hands-on Lab 15 – End-to-End Monitoring

Build:

```text
Application
 ↓
Metrics Endpoint
 ↓
Prometheus
 ↓
Grafana
 ↓
Alert
 ↓
Alertmanager
```

Then correlate the alert with:

```text
Logs
+
Events
```

---

# Common Mistakes

## 1. Monitoring Only CPU

CPU alone does not indicate complete system health.

Monitor:

```text
CPU
Memory
Disk
Network
Application
Errors
Latency
```

---

## 2. Monitoring Without Alerts

Dashboards are useful, but critical conditions should generate alerts.

---

## 3. Too Many Alerts

This creates alert fatigue.

---

## 4. No SLOs

Without objectives, it can be difficult to determine what actually matters.

---

## 5. Ignoring Application Metrics

Infrastructure can look healthy while the application is failing.

---

## 6. Ignoring Restarts

Frequent restarts are often an important failure signal.

---

## 7. Ignoring OOMKilled

Memory-related failures can remain hidden without monitoring.

---

## 8. Ignoring CPU Throttling

A Pod may show moderate CPU usage but still experience throttling depending on its workload and limits.

---

## 9. High-Cardinality Labels

Avoid unbounded labels in Prometheus.

---

## 10. No Capacity Planning

Current health does not guarantee future capacity.

---

## 11. Monitoring System Has No Monitoring

A broken monitoring platform can create a dangerous visibility gap.

---

## 12. No Security Controls

Monitoring systems can contain sensitive infrastructure information.

---

# Quick Revision

## Monitoring

```text
Continuous observation of system health and behavior
```

---

## Metrics

```text
Numerical measurements of system behavior
```

---

## Gauge

```text
Value that can increase or decrease
```

---

## Counter

```text
Monotonically increasing value that can reset
```

---

## Histogram

```text
Measures distributions across buckets
```

---

## Golden Signals

```text
Latency
Traffic
Errors
Saturation
```

---

## RED

```text
Rate
Errors
Duration
```

---

## USE

```text
Utilization
Saturation
Errors
```

---

## SLI

```text
Measured service indicator
```

---

## SLO

```text
Target for an SLI
```

---

## SLA

```text
Contractual/business commitment
```

---

## Error Budget

```text
Allowed failure within an SLO
```

---

## Metrics Server

```text
Provides resource metrics commonly used by kubectl top and HPA
```

---

## Prometheus

```text
Metrics collection, storage, querying, and alerting platform
```

---

## Grafana

```text
Visualization and dashboard platform
```

---

## Node Exporter

```text
Exposes host-level metrics for Prometheus
```

---

## Alert

```text
Notification generated when a monitored condition requires attention
```

---

# Essential Commands

View nodes:

```bash
kubectl get nodes
```

View Pods:

```bash
kubectl get pods -A
```

View resource metrics:

```bash
kubectl top nodes
```

View Pod metrics:

```bash
kubectl top pods -A
```

View events:

```bash
kubectl get events
```

Sort events:

```bash
kubectl get events \
  --sort-by=.metadata.creationTimestamp
```

Describe node:

```bash
kubectl describe node <node>
```

Describe Pod:

```bash
kubectl describe pod <pod>
```

View Pod logs:

```bash
kubectl logs <pod>
```

View previous logs:

```bash
kubectl logs <pod> --previous
```

Check Deployments:

```bash
kubectl get deployments -A
```

Check resource requests and limits:

```bash
kubectl get pod <pod> -o yaml
```

Check HPA:

```bash
kubectl get hpa -A
```

Check Metrics API:

```bash
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/nodes"
```

Check Metrics API for Pods:

```bash
kubectl get --raw "/apis/metrics.k8s.io/v1beta1/pods"
```

---

# Interview Questions

## Basic

- What is Kubernetes monitoring?
- What is the difference between monitoring and observability?
- What are the three pillars of observability?
- What are the Golden Signals?
- What is the RED method?
- What is the USE method?
- What is a metric?
- What is a Counter?
- What is a Gauge?
- What is a Histogram?
- What is Metrics Server?
- What is Prometheus?
- What is Grafana?
- What is Node Exporter?
- What is an SLI?
- What is an SLO?
- What is an SLA?

---

## Intermediate

- What should you monitor in a Kubernetes cluster?
- How do you monitor node CPU and memory?
- How do you monitor Pod resource usage?
- What is OOMKilled?
- What is CPU throttling?
- How do you identify frequently restarting Pods?
- How do you monitor Kubernetes events?
- Why is Metrics Server needed?
- What is the difference between Metrics Server and Prometheus?
- How does Prometheus collect metrics?
- What is PromQL?
- Why are Prometheus labels important?
- What is metric cardinality?
- Why can high cardinality be dangerous?
- How do you design Kubernetes monitoring dashboards?
- How do you prevent alert fatigue?

---

## Advanced

- Design a production Kubernetes monitoring architecture.
- How would you monitor a 500-node Kubernetes cluster?
- How would you monitor the Kubernetes control plane?
- How would you monitor etcd?
- How would you design SLOs for a Kubernetes application?
- How would you implement the RED method?
- How would you implement the USE method?
- How would you troubleshoot high API Server latency?
- How would you troubleshoot a Pod with high memory usage?
- How would you identify CPU throttling?
- How would you detect capacity exhaustion before it becomes an outage?
- How would you design high-availability monitoring?
- How would you control Prometheus cardinality?
- How would you integrate Prometheus with Grafana and Alertmanager?
- How would you secure a monitoring platform?
- How would you correlate metrics with logs and traces?

---

# Interview Scenario 1

### Question

> A Pod is running, but users are receiving errors. What would you check?

### Answer

Do not assume that:

```text
Pod Running
=
Application Healthy
```

Check:

```text
Application Metrics
 ↓
Error Rate
 ↓
Latency
 ↓
Logs
 ↓
Readiness
 ↓
Dependencies
 ↓
Network
```

A Pod can be Running while its application is unhealthy.

---

# Interview Scenario 2

### Question

> CPU usage is only 50%, but the application is slow. What else would you investigate?

### Answer

Check:

```text
CPU Throttling
Memory
Disk I/O
Network
Database Latency
Connection Pool
Application Latency
External Dependencies
```

CPU utilization alone is not enough.

---

# Interview Scenario 3

### Question

> A Pod is repeatedly restarting. How would you investigate?

### Answer

Check:

```bash
kubectl get pod <pod>
```

Then:

```bash
kubectl describe pod <pod>
```

Then:

```bash
kubectl logs <pod>
```

and:

```bash
kubectl logs <pod> --previous
```

Look for:

```text
OOMKilled
Probe Failure
Application Crash
Configuration Error
Missing Secret
Dependency Failure
```

---

# Interview Scenario 4

### Question

> What is the difference between Metrics Server and Prometheus?

### Answer

Metrics Server focuses primarily on Kubernetes resource metrics such as:

```text
CPU
Memory
```

and commonly supports:

```text
kubectl top
HPA
```

Prometheus is a broader monitoring platform providing:

```text
Metrics Collection
Time-Series Storage
PromQL
Service Discovery
Alerting Integration
```

Therefore:

```text
Metrics Server
=
Resource Metrics

Prometheus
=
General Monitoring Platform
```

---

# Interview Scenario 5

### Question

> What are the four Golden Signals?

### Answer

```text
Latency
Traffic
Errors
Saturation
```

They provide a practical high-level view of service health.

---

# Interview Scenario 6

### Question

> What is the difference between SLI, SLO, and SLA?

### Answer

```text
SLI
=
What we measure
```

```text
SLO
=
What target we aim for
```

```text
SLA
=
What we contractually promise
```

---

# Interview Scenario 7

### Question

> Prometheus memory usage keeps increasing. What might be wrong?

### Answer

One possibility is:

```text
High Metric Cardinality
```

For example, using unbounded values such as:

```text
request_id
user_id
UUID
```

as labels can generate enormous numbers of unique time series.

Investigate:

```text
Number of Time Series
Label Cardinality
Scrape Targets
Retention
Query Load
```

---

# Interview Scenario 8

### Question

> How would you monitor a Kubernetes cluster for production readiness?

### Answer

Monitor:

```text
Nodes
Pods
Containers
CPU
Memory
Disk
Network
Restarts
OOMKilled
CPU Throttling
Scheduling
API Server
Scheduler
Controller Manager
etcd
Application Metrics
Latency
Errors
Traffic
Saturation
```

Then implement:

```text
Dashboards
SLOs
Alerts
Capacity Planning
Logs
Tracing
```

---

# Production Monitoring Architecture

```text
                         Kubernetes Cluster
                                │
         ┌──────────────────────┼──────────────────────┐
         ▼                      ▼                      ▼
       Node A                 Node B                 Node C
         │                      │                      │
    Node Metrics           Node Metrics           Node Metrics
         │                      │                      │
         └──────────────────────┼──────────────────────┘
                                ▼
                         Metrics Collection
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
          Application       Kubelet          Exporters
            Metrics           Metrics             │
                │               │                 │
                └───────────────┼─────────────────┘
                                ▼
                            Prometheus
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
             PromQL          Grafana        Alert Rules
                                                │
                                                ▼
                                           Alertmanager
                                                │
                                                ▼
                                           SOC / SRE
```

---

# Chapter Summary

Monitoring provides continuous visibility into Kubernetes infrastructure and applications.

Important monitoring layers include:

```text
Application
Container
Pod
Node
Cluster
Control Plane
External Dependencies
```

Key resource signals are:

```text
CPU
Memory
Disk
Network
```

Important Kubernetes health signals include:

```text
Pod Status
Restarts
OOMKilled
CPU Throttling
Readiness
Liveness
Scheduling
Events
```

For application monitoring, use:

```text
Rate
Errors
Duration
```

through the:

```text
RED Method
```

For infrastructure monitoring, use:

```text
Utilization
Saturation
Errors
```

through the:

```text
USE Method
```

The four Golden Signals are:

```text
Latency
Traffic
Errors
Saturation
```

SLIs measure service behavior.

SLOs define targets.

SLAs define contractual commitments.

A common Kubernetes metrics stack is:

```text
Metrics Server
+
Prometheus
+
Grafana
+
Alertmanager
```

Metrics Server provides Kubernetes resource metrics commonly used by:

```text
kubectl top
HPA
```

Prometheus provides broader metrics collection and querying.

Grafana provides visualization.

Alertmanager handles alert routing and notification workflows.

A mature monitoring architecture is:

```text
Metrics
 ↓
Collection
 ↓
Storage
 ↓
Query
 ↓
Dashboard
 ↓
Alert
 ↓
Response
```

Monitoring should also be correlated with:

```text
Logs
+
Traces
+
Events
+
Runtime Security
```

The most important principle is:

> **Do not monitor infrastructure in isolation. Monitor the complete path from user request to application, dependency, container, Pod, node, and control plane.**

A production Kubernetes monitoring system should provide:

```text
Visibility
+
Actionable Alerts
+
Capacity Planning
+
SLO Tracking
+
Troubleshooting
+
Security
```

---

## Next Chapter

# Chapter 59 – Metrics Server

Topics will include:

- Metrics Server Fundamentals
- Why Metrics Server Exists
- Kubernetes Metrics API
- Resource Metrics
- CPU Metrics
- Memory Metrics
- Node Metrics
- Pod Metrics
- Metrics Server Architecture
- Metrics Server Components
- Metrics API
- API Aggregation Layer
- Kubelet Metrics
- Metrics Collection
- Metrics Scraping
- `kubectl top`
- `kubectl top nodes`
- `kubectl top pods`
- Metrics Server Installation
- Helm Installation
- Manifest Installation
- TLS
- Kubelet Certificates
- Kubelet Authentication
- Kubelet Authorization
- API Server Integration
- Metrics Server Configuration
- Resource Requests
- HPA Integration
- VPA Integration
- Metrics Server Limitations
- Metrics Server vs Prometheus
- Metrics Server vs Node Exporter
- Troubleshooting Metrics Server
- Metrics API Errors
- `Metrics API not available`
- `kubectl top` Errors
- Certificate Problems
- Network Problems
- RBAC Problems
- Resource Consumption
- Production Considerations
- Security
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---