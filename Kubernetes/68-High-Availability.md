# Chapter 68 – High Availability

## Overview

High Availability (HA) is the ability of a Kubernetes platform and the applications running on it to continue operating when individual components fail.

The primary goal is:

```text
Failure
   ↓
Redundancy
   ↓
Automatic Recovery / Failover
   ↓
Minimal Service Interruption
```

A highly available Kubernetes environment avoids relying on a single component for critical functionality.

A simplified HA architecture:

```text
                         Users
                           │
                           ▼
                    Load Balancer
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
          API Server    API Server    API Server
              │            │            │
              └────────────┼────────────┘
                           │
                         etcd
                       ┌───┼───┐
                       ▼   ▼   ▼
                    etcd-1 etcd-2 etcd-3

                 Worker Node Pool
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          Worker-1   Worker-2   Worker-3
              │          │          │
             Pods       Pods       Pods
```

HA applies to both:

```text
Kubernetes Infrastructure
+
Applications
```

---

# Learning Objectives

After completing this chapter, you will understand:

- High Availability fundamentals
- Availability
- Reliability
- Fault tolerance
- Single points of failure
- Kubernetes HA architecture
- Control-plane HA
- API Server HA
- etcd HA
- Scheduler HA
- Controller Manager HA
- Cloud Controller Manager HA
- Worker-node HA
- Load balancers
- API Server load balancing
- etcd quorum
- etcd leader election
- Control-plane replicas
- Worker-node pools
- Multi-zone clusters
- Multi-region architecture
- Pod replicas
- Deployments
- StatefulSets
- DaemonSets
- Pod Disruption Budgets
- Topology spread constraints
- Pod anti-affinity
- Node affinity
- Taints and tolerations
- Failure domains
- Availability zones
- Node failure
- Control-plane failure
- API Server failure
- etcd failure
- Network failure
- Storage failure
- DNS failure
- CNI failure
- CSI failure
- Load balancer failure
- Application failure
- Health checks
- Liveness probes
- Readiness probes
- Startup probes
- Graceful shutdown
- Rolling updates
- Rolling restarts
- Zero-downtime deployments
- Capacity planning
- Spare capacity
- Cluster Autoscaler
- Horizontal Pod Autoscaler
- Backup vs HA
- HA vs Disaster Recovery
- Multi-cluster HA
- Active-passive architecture
- Active-active architecture
- Cross-region HA
- Database HA
- Stateful application HA
- Monitoring HA
- Logging HA
- Security HA
- HA testing
- Chaos testing
- Failure simulation
- Recovery
- Troubleshooting
- Production HA architecture
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is High Availability?

High Availability means designing a system so that failures do not cause unacceptable service interruption.

Instead of:

```text
Component
    ↓
Failure
    ↓
Service Down
```

HA aims for:

```text
Component A
    ↓
Failure
    ↓
Component B
    ↓
Service Continues
```

---

# Availability

Availability describes how often a service is operational and accessible.

A common representation is:

```text
Availability =
Uptime / Total Time
```

---

# Availability Example

Suppose a service is available:

```text
99% of the time
```

This means approximately:

```text
1% downtime
```

over the measurement period.

---

# Common Availability Targets

Examples:

```text
99%
99.9%
99.99%
99.999%
```

Each additional nine requires significantly more engineering effort.

---

# Reliability vs Availability

Reliability:

```text
Probability that a system performs correctly over time
```

Availability:

```text
Probability that a system is operational when needed
```

A system can be reliable but temporarily unavailable because of maintenance.

---

# Fault Tolerance

Fault tolerance means a system can continue operating despite certain component failures.

Example:

```text
Worker-1
   X
   ↓
Worker-2
   ✓
   ↓
Application Continues
```

---

# Single Point of Failure

A Single Point of Failure (SPOF) is a component whose failure can cause the entire service to fail.

Example:

```text
Users
  ↓
Single Load Balancer
  ↓
Application
```

If the load balancer fails:

```text
Application
     X
```

---

# Kubernetes HA Goal

Remove or reduce critical SPOFs.

Instead of:

```text
1 API Server
```

use:

```text
API-1
API-2
API-3
```

Instead of:

```text
1 Worker
```

use:

```text
Worker-1
Worker-2
Worker-3
```

---

# Kubernetes HA Layers

HA can be considered at several layers:

```text
Application
     ↓
Pods
     ↓
Nodes
     ↓
Networking
     ↓
Storage
     ↓
Control Plane
     ↓
Infrastructure
```

---

# Control Plane HA

A production Kubernetes control plane commonly uses multiple control-plane nodes.

Example:

```text
              Load Balancer
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      API-1       API-2       API-3
        │           │           │
        └───────────┼───────────┘
                    │
                 etcd
```

---

# API Server HA

The Kubernetes API Server is generally stateless relative to etcd.

Multiple API Servers can serve requests:

```text
                Load Balancer
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       API-1       API-2       API-3
```

If one API Server fails:

```text
API-1
  X

API-2
  ✓
```

the load balancer can route traffic to healthy servers.

---

# API Server Load Balancing

A load balancer provides a stable endpoint:

```text
https://kubernetes-api.example
```

and distributes requests across:

```text
API-1
API-2
API-3
```

---

# API Server Health Checks

The load balancer should detect unhealthy API Servers.

Conceptually:

```text
Load Balancer
     │
     ├── API-1 ✓
     ├── API-2 ✓
     └── API-3 X
```

Traffic is directed to healthy instances.

---

# etcd HA

etcd uses a distributed consensus model.

A production HA etcd cluster commonly uses an odd number of members:

```text
3
5
7
```

---

# Why Odd Number of etcd Members?

etcd requires quorum.

For:

```text
3 members
```

quorum is:

```text
2
```

For:

```text
5 members
```

quorum is:

```text
3
```

---

# etcd Quorum

The quorum formula is:

```text
Quorum = floor(N / 2) + 1
```

For example:

```text
3 → 2
5 → 3
7 → 4
```

---

# etcd Failure Tolerance

A 3-member etcd cluster can generally tolerate:

```text
1 member failure
```

A 5-member cluster can generally tolerate:

```text
2 member failures
```

as long as quorum remains available.

---

# etcd Leader

etcd uses leader election.

Conceptually:

```text
etcd-1
etcd-2
etcd-3

     ↓

Leader
```

If the leader fails:

```text
Leader
  X
  ↓
Election
  ↓
New Leader
```

---

# etcd Failure

If quorum is lost:

```text
etcd
 ↓
No Quorum
 ↓
Control Plane Problems
```

The API Server may no longer be able to reliably persist cluster state.

---

# Control Plane Components

HA control planes may run multiple instances of:

```text
API Server
Scheduler
Controller Manager
Cloud Controller Manager
```

The exact deployment model depends on the Kubernetes distribution.

---

# Scheduler HA

Multiple scheduler instances can participate in leader election.

Conceptually:

```text
Scheduler-1
Scheduler-2
Scheduler-3
```

One may act as the active leader while others are available to take over.

---

# Controller Manager HA

Similarly, multiple controller-manager instances can use leader election.

Example:

```text
Controller-1
Controller-2
Controller-3
```

This provides redundancy.

---

# Cloud Controller Manager HA

Cloud Controller Manager deployments can also use multiple instances depending on the cloud integration.

---

# Worker Node HA

Applications should not depend on a single worker node.

Instead:

```text
Worker-1
Worker-2
Worker-3
```

can provide workload redundancy.

---

# Pod Replicas

A Deployment can run multiple replicas.

Example:

```yaml
spec:

  replicas: 3
```

Architecture:

```text
Application
   │
   ├── Pod-1
   ├── Pod-2
   └── Pod-3
```

---

# Why Multiple Replicas?

If:

```text
Pod-1
  X
```

then:

```text
Pod-2
Pod-3
```

can continue serving requests.

---

# Pod Distribution

Simply running three replicas does not guarantee HA.

Bad placement:

```text
Node-1
 ├── Pod-1
 ├── Pod-2
 └── Pod-3

Node-1
   X
```

All replicas can fail together.

Better:

```text
Node-1 → Pod-1
Node-2 → Pod-2
Node-3 → Pod-3
```

---

# Pod Anti-Affinity

Pod anti-affinity can discourage or require separating replicas across nodes.

Conceptually:

```yaml
affinity:

  podAntiAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

      - labelSelector:

          matchLabels:
            app: backend

        topologyKey: kubernetes.io/hostname
```

---

# Topology Spread Constraints

Topology spread constraints provide another way to distribute workloads across failure domains.

Example:

```yaml
topologySpreadConstraints:

  - maxSkew: 1

    topologyKey: topology.kubernetes.io/zone

    whenUnsatisfiable: DoNotSchedule

    labelSelector:

      matchLabels:
        app: backend
```

---

# Availability Zones

Cloud platforms commonly provide multiple Availability Zones.

Example:

```text
Region
│
├── Zone A
│    └── Nodes
│
├── Zone B
│    └── Nodes
│
└── Zone C
     └── Nodes
```

---

# Multi-Zone Kubernetes

A resilient application should distribute replicas across zones.

```text
Zone A → Pod-1
Zone B → Pod-2
Zone C → Pod-3
```

If one zone fails:

```text
Zone A
  X
```

other zones remain available.

---

# Failure Domains

Failure domains can include:

```text
Node
Rack
Zone
Region
Data Center
Cloud Provider
```

HA architecture should place replicas across appropriate failure domains.

---

# Node Failure

If one node fails:

```text
Node-1
   X
```

Kubernetes can recreate eligible workload replicas on other nodes.

Example:

```text
Deployment replicas = 3

Before:
Node-1 → Pod-1
Node-2 → Pod-2
Node-3 → Pod-3

Node-1 fails

After:
Node-2 → Pod-2
Node-3 → Pod-3
Node-4 → Pod-1 replacement
```

---

# Node Auto-Recovery

Depending on the environment, failed nodes may be:

```text
Detected
Replaced
Repaired
```

through infrastructure automation or Cluster Autoscaler mechanisms.

---

# Pod Readiness

Readiness probes indicate whether a container is ready to receive traffic.

Example:

```yaml
readinessProbe:

  httpGet:
    path: /ready
    port: 8080
```

---

# Why Readiness Matters

Without readiness:

```text
Pod Starting
   ↓
Traffic Sent
   ↓
Requests Fail
```

With readiness:

```text
Pod Starting
   ↓
Not Ready
   ↓
No Traffic
   ↓
Ready
   ↓
Traffic
```

---

# Liveness Probe

A liveness probe helps determine whether a container should be restarted.

Example:

```yaml
livenessProbe:

  httpGet:
    path: /health
    port: 8080
```

---

# Startup Probe

Startup probes protect slow-starting applications from premature liveness failures.

Example:

```yaml
startupProbe:

  httpGet:
    path: /startup
    port: 8080
```

---

# Probe Comparison

| Probe | Purpose |
|---|---|
| Startup | Determine whether application has started |
| Readiness | Determine whether traffic should be sent |
| Liveness | Determine whether container should be restarted |

---

# Graceful Shutdown

When a Pod is terminated:

```text
SIGTERM
   ↓
Application Cleanup
   ↓
Connections Finish
   ↓
Container Stops
```

Graceful shutdown reduces dropped requests.

---

# terminationGracePeriodSeconds

Example:

```yaml
spec:

  terminationGracePeriodSeconds: 30
```

This gives the workload time to shut down gracefully.

---

# Service HA

Services distribute traffic across healthy backend Pods.

Architecture:

```text
Client
  ↓
Service
  ↓
┌───┼───┐
▼   ▼   ▼
Pod Pod Pod
```

---

# Service and Readiness

Services normally avoid routing traffic to Pods that are not considered ready for normal service endpoints.

Therefore:

```text
Readiness
+
Service
```

helps maintain availability during deployments and failures.

---

# Load Balancer HA

External traffic may use:

```text
Cloud Load Balancer
```

or another highly available ingress/load-balancing architecture.

Avoid introducing a single externally reachable load balancer as an unmanaged SPOF.

---

# Ingress HA

Run multiple replicas of the Ingress controller where supported.

Example:

```text
Ingress Controller
 ├── Replica-1
 ├── Replica-2
 └── Replica-3
```

---

# Gateway HA

Gateway implementations should also be deployed according to their controller's HA capabilities.

Ensure:

```text
Gateway Controller
Load Balancer
Network
```

are resilient.

---

# Stateful Application HA

Stateful applications require additional planning.

Examples:

```text
PostgreSQL
MySQL
MongoDB
Redis
Kafka
```

Running multiple Pods does not automatically make a database highly available.

---

# Database HA

Database HA may require:

```text
Replication
Leader Election
Failover
Quorum
Consistent Storage
Backup
```

---

# StatefulSet

StatefulSet provides:

```text
Stable Identity
Stable Network Identity
Ordered Operations
Persistent Storage Association
```

It does not automatically provide database-level HA.

---

# StatefulSet HA

A typical architecture:

```text
Database
 ├── Primary
 ├── Replica
 └── Replica
```

The database itself must support:

```text
Replication
Failover
Consistency
```

---

# DaemonSet HA

DaemonSets run workloads on nodes.

Common use cases:

```text
Logging Agent
Monitoring Agent
Security Agent
CNI Components
```

Node failures reduce the number of DaemonSet instances automatically because the failed node is unavailable.

---

# Pod Disruption Budget

PDBs protect replicated applications from excessive voluntary disruption.

Example:

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget

metadata:
  name: api-pdb

spec:

  minAvailable: 2

  selector:

    matchLabels:
      app: api
```

---

# PDB and HA

PDB helps during:

```text
Node Drain
Cluster Maintenance
Voluntary Disruptions
```

It does not protect against every involuntary failure.

---

# Horizontal Pod Autoscaler

HPA adjusts replicas based on metrics.

Conceptually:

```text
Traffic
  ↓
CPU / Custom Metrics
  ↓
HPA
  ↓
More Pods
```

---

# Cluster Autoscaler

Cluster Autoscaler adjusts node capacity when scheduling requirements change.

Example:

```text
HPA
 ↓
More Pods
 ↓
Insufficient Nodes
 ↓
Cluster Autoscaler
 ↓
New Nodes
```

---

# Spare Capacity

HA requires sufficient spare capacity.

Example:

```text
Cluster Capacity = 100 CPU
Current Usage = 85 CPU
```

If a node fails, the remaining capacity may be insufficient.

Therefore, HA requires:

```text
Capacity Planning
```

---

# N+1 Capacity

A common planning principle is:

```text
N = Required Capacity
N+1 = Required Capacity + One Failure
```

For example:

```text
Required:
3 Nodes

HA:
4 Nodes
```

This allows one node to fail while maintaining capacity.

---

# Multi-Region Architecture

For major regional failures:

```text
Region A
   │
   ├── Cluster A
   │
   ▼
Global Traffic
   ▲
   │
   └── Cluster B
          │
       Region B
```

---

# Active-Passive

One region serves production.

```text
Region A
  ↓
Active

Region B
  ↓
Standby
```

On failure:

```text
Region A
  X

Region B
  ↓
Active
```

---

# Active-Active

Both regions serve traffic.

```text
           Global Load Balancer
              /          \
             ▼            ▼
         Region A      Region B
           │              │
        Cluster A      Cluster B
```

This is more complex, especially for stateful applications.

---

# Multi-Cluster HA

Multiple Kubernetes clusters can provide additional failure isolation.

Example:

```text
Cluster A
   │
   ├── Region A
   │
Cluster B
   │
   └── Region B
```

---

# Multi-Cluster Challenges

Challenges include:

```text
Data Synchronization
Traffic Management
Identity
Secrets
Configuration
Observability
Deployment
Cost
```

---

# Backup vs High Availability

HA:

```text
Prevents / Reduces Downtime
```

Backup:

```text
Recovers Data
```

Example:

```text
HA:
Node failure → Service continues

Backup:
Cluster destruction → Restore
```

Both are required.

---

# HA vs Disaster Recovery

HA handles:

```text
Component Failures
```

DR handles:

```text
Large-Scale Failures
```

Example:

```text
HA:
Node Failure

DR:
Region Failure
```

---

# Monitoring HA

Monitoring itself should be highly available.

Avoid:

```text
One Monitoring Server
```

as the only source of observability.

Consider:

```text
Redundant Collectors
Replicated Storage
External Alerting
```

---

# Logging HA

Logs should survive:

```text
Node Failure
Pod Failure
Cluster Failure
```

Use external or replicated log storage where required.

---

# Security HA

Security systems should also avoid becoming SPOFs.

Examples:

```text
Identity Provider
Secret Management
Admission Webhooks
Security Monitoring
```

---

# Admission Webhook HA

If an admission webhook is critical:

```text
Webhook
 ├── Replica-1
 ├── Replica-2
 └── Replica-3
```

Ensure:

```text
Service
DNS
TLS
Endpoints
```

are resilient.

---

# DNS HA

Cluster DNS should have multiple replicas.

Example:

```text
CoreDNS
 ├── Pod-1
 ├── Pod-2
 └── Pod-3
```

---

# CNI HA

Networking components should be deployed according to the CNI's supported HA architecture.

Monitor:

```text
CNI Pods
Node Networking
Routes
Network Policies
```

---

# CSI HA

Storage components may include:

```text
CSI Controller
CSI Node
External Provisioner
Snapshotter
```

depending on the driver.

Ensure critical control components are deployed according to supported HA guidance.

---

# Health Checks

HA systems require health checks.

Monitor:

```text
Availability
Latency
Errors
Readiness
Resource Usage
```

---

# Failure Detection

The system should detect:

```text
Node Failure
Pod Failure
API Failure
Network Failure
Storage Failure
```

quickly.

---

# Automatic Recovery

Examples:

```text
Pod Failure
 ↓
ReplicaSet
 ↓
New Pod
```

and:

```text
Node Failure
 ↓
Scheduler
 ↓
Replacement Pod
```

provided the workload and cluster state permit it.

---

# Rolling Updates

Deployments can update Pods gradually.

Example:

```text
Version 1
 ↓
Version 2
 ↓
Version 2
```

This helps reduce downtime.

---

# Rolling Restart

A controlled restart can be performed with:

```bash
kubectl rollout restart deployment <deployment-name>
```

Monitor the rollout afterward.

---

# Check Rollout

```bash
kubectl rollout status deployment <deployment-name>
```

---

# Rollout History

```bash
kubectl rollout history deployment <deployment-name>
```

---

# Rollback Application Deployment

For a Deployment:

```bash
kubectl rollout undo deployment <deployment-name>
```

This is an application rollout rollback, not a Kubernetes cluster-version rollback.

---

# Zero-Downtime Deployment

A typical pattern:

```text
Old Pods
   │
   ├── Receive Traffic
   │
New Pods
   │
   ├── Start
   ├── Become Ready
   └── Receive Traffic
```

This requires:

```text
Readiness
Replication
Capacity
RollingUpdate Strategy
```

---

# Deployment Strategy

Example:

```yaml
strategy:

  type: RollingUpdate

  rollingUpdate:

    maxUnavailable: 0

    maxSurge: 1
```

This can help maintain availability during rollout, assuming enough capacity exists.

---

# Failure Simulation

HA should be tested.

Examples:

```text
Kill Pod
Stop Node
Break Network
Restart API Server
Simulate Storage Failure
```

Use controlled environments and approved procedures.

---

# Chaos Testing

Chaos testing deliberately introduces failures to validate resilience.

Conceptually:

```text
Inject Failure
      ↓
Observe
      ↓
Recover
      ↓
Measure
```

---

# HA Metrics

Important metrics include:

```text
Availability
Error Rate
Latency
Pod Restarts
Node Failures
API Server Availability
etcd Health
Network Errors
Storage Errors
```

---

# SLA

Service Level Agreement defines a contractual availability or performance commitment.

Example:

```text
99.9% Availability
```

---

# SLO

Service Level Objective is the internal target.

Example:

```text
SLO = 99.95%
```

---

# SLI

Service Level Indicator is the measured metric.

Example:

```text
Successful Requests / Total Requests
```

---

# SLI → SLO → SLA

```text
SLI
 ↓
Measurement

SLO
 ↓
Target

SLA
 ↓
Contractual Commitment
```

---

# HA Design Process

Start with:

```text
1. Identify Critical Services
2. Identify Failure Domains
3. Identify SPOFs
4. Define Availability Target
5. Define RTO
6. Define RPO
7. Add Redundancy
8. Add Monitoring
9. Test Failure
10. Document Recovery
```

---

# HA Example

Suppose an API requires:

```text
99.99% Availability
```

Design:

```text
3 API Pods
3 Worker Nodes
3 Availability Zones
Multiple API Servers
HA etcd
Load Balancer
Readiness Probes
PDB
Monitoring
Backup
```

---

# Common HA Mistakes

## 1. Three Pods on One Node

```text
Node-1
 ├── Pod-1
 ├── Pod-2
 └── Pod-3
```

Node failure destroys all replicas.

---

## 2. One Worker Node

This creates a major SPOF.

---

## 3. No Spare Capacity

A node failure may leave nowhere to schedule replacements.

---

## 4. No Readiness Probes

Traffic can reach unhealthy or initializing applications.

---

## 5. No PDB

Maintenance may disrupt too many replicas.

---

## 6. Treating StatefulSets as Automatically HA

StatefulSet does not provide database replication by itself.

---

## 7. No Multi-Zone Distribution

A zone outage can affect all replicas.

---

## 8. Single Monitoring System

If monitoring fails, operators may lose visibility.

---

## 9. No Backup

HA does not protect against all data-loss scenarios.

---

## 10. No Failure Testing

An HA architecture that has never been tested is an assumption.

---

# Best Practices

### 1. Eliminate SPOFs

Identify:

```text
Network
Load Balancer
Control Plane
Storage
Application
```

---

### 2. Spread Workloads

Use:

```text
Anti-Affinity
Topology Spread
Multiple Zones
```

---

### 3. Use Multiple Replicas

For stateless workloads:

```text
replicas > 1
```

---

### 4. Maintain Spare Capacity

Allow the cluster to tolerate expected failures.

---

### 5. Use Readiness Probes

Only send traffic to ready applications.

---

### 6. Use PDBs

Protect workloads during voluntary disruption.

---

### 7. Protect Stateful Systems

Use application-native replication and tested recovery.

---

### 8. Monitor Everything

Track:

```text
Availability
Latency
Errors
Saturation
```

---

### 9. Test Failures

Practice:

```text
Node Failure
Pod Failure
Zone Failure
Network Failure
```

---

### 10. Combine HA With Backup

HA reduces downtime.

Backup enables recovery.

---

# Hands-on Lab 1 – Multiple Pod Replicas

Create a Deployment:

```yaml
apiVersion: apps/v1
kind: Deployment

metadata:
  name: web

spec:

  replicas: 3

  selector:
    matchLabels:
      app: web

  template:

    metadata:
      labels:
        app: web

    spec:

      containers:

        - name: web
          image: nginx
```

Verify:

```bash
kubectl get pods -o wide
```

---

# Hands-on Lab 2 – Pod Failure

Delete one Pod:

```bash
kubectl delete pod <pod-name>
```

Observe:

```text
ReplicaSet
 ↓
Replacement Pod
```

---

# Hands-on Lab 3 – Pod Anti-Affinity

Configure anti-affinity so replicas prefer or require separate nodes.

Observe:

```bash
kubectl get pods -o wide
```

---

# Hands-on Lab 4 – Topology Spread

Deploy replicas across multiple zones or node labels in a suitable test environment.

Verify distribution.

---

# Hands-on Lab 5 – Readiness Probe

Create a Deployment with:

```yaml
readinessProbe:
  httpGet:
    path: /
    port: 80
```

Observe Pod readiness.

---

# Hands-on Lab 6 – Liveness Probe

Configure:

```yaml
livenessProbe:
  httpGet:
    path: /
    port: 80
```

Test the application's response to an unhealthy state in a disposable environment.

---

# Hands-on Lab 7 – Startup Probe

Deploy a slow-starting test application.

Configure:

```yaml
startupProbe:
```

Observe how startup and liveness behavior interact.

---

# Hands-on Lab 8 – Pod Disruption Budget

Create:

```text
3 replicas
+
PDB
```

Drain a node.

Observe disruption behavior.

---

# Hands-on Lab 9 – Rolling Deployment

Update an image:

```bash
kubectl set image deployment/web \
  web=nginx:latest
```

Then:

```bash
kubectl rollout status deployment/web
```

Observe:

```text
Old Pods
 ↓
New Pods
```

Use a controlled, immutable image tag in production rather than relying on a moving tag.

---

# Hands-on Lab 10 – Rollback Application Deployment

Perform a Deployment update.

Check:

```bash
kubectl rollout history deployment/web
```

Then:

```bash
kubectl rollout undo deployment/web
```

---

# Hands-on Lab 11 – Node Failure Simulation

In a disposable environment:

```text
Stop Worker Node
```

Observe:

```text
Node Condition
Pod Scheduling
Replica Recovery
```

---

# Hands-on Lab 12 – Multi-Zone HA

Create or use a cluster spanning multiple zones.

Deploy:

```text
3 replicas
```

Use topology constraints.

Verify:

```text
Zone A
Zone B
Zone C
```

distribution.

---

# Hands-on Lab 13 – Control Plane HA

Create a test HA control plane.

Verify:

```text
API Server-1
API Server-2
API Server-3
```

and test failure of one API Server.

---

# Hands-on Lab 14 – etcd Quorum

Use a disposable etcd/Kubernetes environment.

Observe:

```text
3 members
1 failure
Quorum maintained
```

Do not intentionally destroy production quorum.

---

# Hands-on Lab 15 – API Server Load Balancing

Configure a test load balancer in front of multiple API Servers.

Stop one API Server.

Verify:

```text
kubectl
```

continues working.

---

# Hands-on Lab 16 – HA Monitoring

Deploy monitoring with redundant components where supported.

Simulate one monitoring component failure.

Verify continued observability.

---

# Hands-on Lab 17 – Stateful Application HA

Deploy a test database with its supported replication mechanism.

Simulate primary failure.

Observe:

```text
Replica
 ↓
Failover
```

---

# Hands-on Lab 18 – Backup + HA

Combine:

```text
Multiple Replicas
+
Multi-Node
+
Backup
```

Simulate:

```text
Node Failure
```

then:

```text
Cluster Failure
```

Compare HA and backup behavior.

---

# Hands-on Lab 19 – Chaos Experiment

Create a controlled failure:

```text
Pod Kill
```

Measure:

```text
Detection Time
Recovery Time
Availability
```

---

# Hands-on Lab 20 – Full HA Exercise

Design:

```text
3 Control Plane Nodes
3+ Worker Nodes
Multiple Zones
HA API Server
HA etcd
Load Balancer
3+ Application Replicas
PDB
Readiness Probes
Topology Spread
Monitoring
Backup
```

Then simulate:

```text
Pod Failure
Node Failure
API Server Failure
Zone Failure
```

Document recovery behavior.

---

# Quick Revision

## High Availability

```text
Ability to continue service despite expected failures
```

---

## SPOF

```text
Single Point of Failure
```

---

## Fault Tolerance

```text
Ability to continue operating despite component failure
```

---

## API Server HA

```text
Multiple API Servers behind a stable endpoint/load balancer
```

---

## etcd HA

```text
Multiple etcd members maintaining quorum
```

---

## Quorum

```text
Majority required for consensus
```

---

## Pod Replicas

```text
Multiple instances of an application
```

---

## Pod Anti-Affinity

```text
Separates workloads based on topology rules
```

---

## Topology Spread

```text
Distributes Pods across failure domains
```

---

## PDB

```text
Limits voluntary disruption
```

---

## Readiness Probe

```text
Determines whether a Pod should receive traffic
```

---

## Liveness Probe

```text
Helps determine whether a container should be restarted
```

---

## Startup Probe

```text
Protects slow-starting applications during initialization
```

---

## RPO

```text
Acceptable data loss
```

---

## RTO

```text
Target recovery time
```

---

## HA vs Backup

```text
HA → Continue operating
Backup → Recover data
```

---

## Active-Passive

```text
One active environment + standby
```

---

## Active-Active

```text
Multiple environments actively serving traffic
```

---

# Essential Commands

Check nodes:

```bash
kubectl get nodes
```

Check Pods:

```bash
kubectl get pods -o wide
```

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

Check PDB:

```bash
kubectl get pdb -A
```

Describe PDB:

```bash
kubectl describe pdb <pdb-name>
```

Check deployments:

```bash
kubectl get deployments -A
```

Check rollout:

```bash
kubectl rollout status deployment/<deployment>
```

Restart deployment:

```bash
kubectl rollout restart deployment/<deployment>
```

View rollout history:

```bash
kubectl rollout history deployment/<deployment>
```

Rollback application:

```bash
kubectl rollout undo deployment/<deployment>
```

Cordon:

```bash
kubectl cordon <node>
```

Drain:

```bash
kubectl drain <node> --ignore-daemonsets
```

Uncordon:

```bash
kubectl uncordon <node>
```

Check Services:

```bash
kubectl get svc -A
```

Check endpoints:

```bash
kubectl get endpoints -A
```

Check EndpointSlices:

```bash
kubectl get endpointslices -A
```

Check topology:

```bash
kubectl get nodes \
  --show-labels
```

Check resources:

```bash
kubectl top nodes
```

---

# Interview Questions

## Basic

- What is High Availability?
- Why is HA important in Kubernetes?
- What is a Single Point of Failure?
- What is fault tolerance?
- What is the difference between reliability and availability?
- How does Kubernetes support HA?
- How many control-plane nodes are commonly used for HA?
- What is etcd quorum?
- Why are odd numbers commonly used for etcd?
- What is API Server HA?
- What is worker-node HA?
- What is a Pod replica?
- What is a PDB?
- What is a readiness probe?
- What is a liveness probe?
- What is a startup probe?
- What is topology spread?

---

## Intermediate

- How does Kubernetes recover from a failed Pod?
- How does Kubernetes handle node failure?
- Why should Pods be distributed across nodes?
- Why should replicas be distributed across zones?
- How does Pod anti-affinity improve HA?
- How does a PDB help during node maintenance?
- Why is spare capacity important?
- What is N+1 capacity?
- How does a load balancer improve API Server availability?
- How does etcd maintain quorum?
- What happens if an etcd leader fails?
- What happens if etcd loses quorum?
- How do readiness probes improve availability?
- How do rolling updates reduce downtime?
- Does StatefulSet automatically provide database HA?

---

## Advanced

- Design a highly available Kubernetes cluster.
- Design an HA control plane across three availability zones.
- How would you make a Kubernetes application resilient to node failure?
- How would you design HA for a stateful database?
- How would you design multi-region Kubernetes HA?
- Explain active-active vs active-passive Kubernetes architectures.
- How would you eliminate SPOFs in a production cluster?
- How would you calculate required capacity for N+1 resilience?
- How would you test Kubernetes HA?
- How would you perform chaos testing?
- How would you design HA monitoring?
- How would you design HA for CNI and CSI?
- What happens when etcd loses quorum?
- How would you recover from a control-plane failure?
- How would you design zero-downtime application deployments?
- What is the difference between HA and disaster recovery?

---

# Interview Scenario 1

### Question

> How does Kubernetes provide high availability?

### Answer

Kubernetes provides HA through multiple mechanisms:

```text
Multiple Control Plane Nodes
+
Multiple etcd Members
+
Multiple Worker Nodes
+
ReplicaSets / Deployments
+
Load Balancing
+
Readiness Probes
+
PDBs
+
Topology Distribution
+
Autoscaling
```

These mechanisms address different failure scenarios.

---

# Interview Scenario 2

### Question

> Why should you run multiple API Servers?

### Answer

The API Server is a critical control-plane component.

Multiple API Servers allow:

```text
API-1
API-2
API-3
```

to serve requests.

If one fails:

```text
API-1
  X

API-2
  ✓
API-3
  ✓
```

the cluster can continue serving API requests, assuming the rest of the control plane remains healthy.

---

# Interview Scenario 3

### Question

> Why does etcd require quorum?

### Answer

etcd uses distributed consensus.

A majority is required to safely make progress.

For:

```text
3 members → quorum = 2
```

For:

```text
5 members → quorum = 3
```

If quorum is lost:

```text
Cluster State
     ↓
Cannot safely commit updates
```

which can significantly affect Kubernetes control-plane operation.

---

# Interview Scenario 4

### Question

> You have three application replicas. Are you highly available?

### Answer

Not necessarily.

If all replicas run on one node:

```text
Node-1
 ├── Pod-1
 ├── Pod-2
 └── Pod-3
```

then:

```text
Node Failure
     ↓
All replicas fail
```

HA requires distributing replicas across appropriate failure domains.

---

# Interview Scenario 5

### Question

> How do you distribute Pods across zones?

### Answer

Use:

```text
Topology Spread Constraints
```

or:

```text
Pod Anti-Affinity
```

For example:

```text
Zone A → Pod-1
Zone B → Pod-2
Zone C → Pod-3
```

This reduces correlated failure.

---

# Interview Scenario 6

### Question

> What is the purpose of a readiness probe?

### Answer

It tells Kubernetes whether the application is ready to receive traffic.

During startup:

```text
Pod
 ↓
Not Ready
 ↓
No Normal Service Traffic
```

After initialization:

```text
Ready
 ↓
Traffic
```

This helps prevent requests from reaching unready applications.

---

# Interview Scenario 7

### Question

> Does a PDB guarantee zero downtime?

### Answer

No.

A PDB limits voluntary disruption but does not protect against all failures.

For example:

```text
Node suddenly crashes
```

A PDB cannot prevent the crash.

It mainly helps during operations such as:

```text
Drain
Maintenance
Voluntary Disruption
```

---

# Interview Scenario 8

### Question

> What happens when an application Pod fails?

### Answer

If it is managed by a controller such as a Deployment:

```text
Pod Failure
    ↓
Replica Count Below Desired
    ↓
Controller Reconciliation
    ↓
Replacement Pod
```

The Service can continue routing to healthy ready replicas.

---

# Interview Scenario 9

### Question

> What is the difference between HA and disaster recovery?

### Answer

HA focuses on continuing service despite component failures:

```text
Node Failure
 ↓
Another Node
```

DR focuses on recovery from larger disasters:

```text
Cluster / Region Loss
 ↓
Recovery Environment
 ↓
Restore
```

---

# Interview Scenario 10

### Question

> Design a highly available Kubernetes architecture.

### Answer

A strong design could use:

```text
                    Global / External LB
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
             Region A              Region B
                 │                     │
           ┌─────┴─────┐         ┌─────┴─────┐
           ▼     ▼     ▼         ▼     ▼     ▼
          Zone A Zone B Zone C   Zone A Zone B Zone C
             │      │      │       │      │      │
           Nodes  Nodes  Nodes   Nodes  Nodes  Nodes
             │      │      │       │      │      │
          App replicas distributed across failure domains
```

Control plane:

```text
Multiple API Servers
+
HA etcd
+
Scheduler HA
+
Controller Manager HA
```

Application layer:

```text
Multiple Replicas
+
PDB
+
Readiness
+
Topology Spread
```

Infrastructure:

```text
Load Balancing
+
Monitoring
+
Backup
+
Disaster Recovery
```

---

# Production HA Checklist

```text
☑ No critical SPOFs
☑ Multiple control-plane nodes
☑ HA etcd
☑ API Server load balancing
☑ Multiple worker nodes
☑ Multiple application replicas
☑ Pod distribution
☑ Multiple availability zones
☑ Topology spread
☑ Pod anti-affinity where appropriate
☑ PDBs
☑ Readiness probes
☑ Liveness probes
☑ Startup probes
☑ Graceful shutdown
☑ Spare capacity
☑ Autoscaling
☑ HA networking
☑ HA storage
☑ HA monitoring
☑ HA logging
☑ Backup
☑ Disaster recovery
☑ Failure testing
☑ Recovery runbooks
```

---

# Chapter Summary

High Availability is a combination of:

```text
Redundancy
+
Failure Isolation
+
Automatic Recovery
+
Monitoring
+
Capacity
+
Testing
```

Kubernetes HA can be designed across multiple layers:

```text
Application
 ↓
Pods
 ↓
Nodes
 ↓
Zones
 ↓
Control Plane
 ↓
Storage
 ↓
Network
```

A highly available application should use:

```text
Multiple Replicas
+
Readiness Probes
+
PDB
+
Topology Distribution
+
Spare Capacity
```

A highly available control plane should consider:

```text
Multiple API Servers
+
HA etcd
+
Scheduler HA
+
Controller Manager HA
+
API Load Balancing
```

The most important principle is:

> **High Availability is not achieved by simply running multiple Pods. True HA requires eliminating critical single points of failure, distributing workloads across failure domains, maintaining sufficient capacity, detecting failures quickly, recovering automatically where possible, and continuously testing the architecture.**

---

## Next Chapter

# Chapter 69 – Disaster Recovery

Topics will include:

- Disaster Recovery Fundamentals
- Disaster vs Failure
- Business Continuity
- Business Impact Analysis
- RPO
- RTO
- MTTR
- MTTD
- Disaster Recovery Planning
- Kubernetes DR Architecture
- Cluster Disaster
- Control Plane Disaster
- etcd Disaster
- Worker Node Disaster
- Storage Disaster
- Network Disaster
- Region Failure
- Cloud Provider Failure
- Data Center Failure
- Security Incident
- Ransomware
- Accidental Deletion
- Backup Strategy
- etcd Backup
- Persistent Volume Backup
- Database Backup
- Kubernetes Resource Backup
- Velero
- Volume Snapshots
- Cross-Cluster Recovery
- Cross-Region Recovery
- Active-Passive DR
- Active-Active DR
- Warm Standby
- Cold Standby
- Recovery Environment
- DNS Failover
- Global Load Balancing
- Traffic Failover
- Data Replication
- Database Replication
- Storage Replication
- Secrets Recovery
- Identity Recovery
- Network Recovery
- CNI Recovery
- CSI Recovery
- Control Plane Recovery
- etcd Restore
- Application Recovery
- Dependency Recovery
- Recovery Runbooks
- DR Testing
- Game Days
- Chaos Engineering
- Restore Testing
- Failover Testing
- Failback
- Recovery Validation
- DR Monitoring
- DR Security
- Immutable Backups
- Air-Gapped Backups
- Compliance
- Documentation
- Production DR Architecture
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---