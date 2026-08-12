# Chapter 87 – Real-World Case Studies

## Overview

This chapter applies Kubernetes concepts to realistic production scenarios.

The objective is not only to understand **how Kubernetes works**, but to develop the ability to:

- Design Kubernetes architectures
- Identify failure domains
- Troubleshoot production incidents
- Secure workloads
- Analyze performance problems
- Handle networking failures
- Recover from storage failures
- Respond to security incidents
- Perform controlled deployments
- Design highly available systems
- Make operational decisions under pressure

The case studies follow a consistent incident-analysis model:

```text
Scenario
   ↓
Architecture
   ↓
Problem
   ↓
Symptoms
   ↓
Investigation
   ↓
Root Cause
   ↓
Remediation
   ↓
Validation
   ↓
Prevention
```

---

# Case Study 1 – E-Commerce Platform

## Scenario

An e-commerce company runs its application on Kubernetes.

Architecture:

```text
                    Internet
                       │
                       ▼
                 Load Balancer
                       │
                       ▼
                    Ingress
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
        Frontend Service    API Service
             │                   │
             ▼                   ▼
       Frontend Pods         API Pods
                                 │
                ┌────────────────┼────────────────┐
                ▼                ▼                ▼
             Redis           Database          Payment API
```

---

## Requirements

The platform must support:

```text
High Availability
Horizontal Scaling
Secure Communication
Persistent Storage
Monitoring
Centralized Logging
Automated Deployment
```

---

## Kubernetes Design

Use:

```text
Deployment
Service
Ingress / Gateway
ConfigMap
Secret
HPA
PDB
NetworkPolicy
RBAC
PVC
```

---

## Failure Scenario

Customers report:

```text
Checkout requests are failing.
```

---

## Symptoms

```text
HTTP 500
High API latency
Payment failures
```

Check:

```bash
kubectl get pods
kubectl get svc
kubectl get endpointslices
kubectl get events
```

---

## Investigation

Check API logs:

```bash
kubectl logs deployment/api
```

Check database connectivity.

Check:

```text
NetworkPolicy
DNS
Service
Database
Secrets
```

---

## Root Cause

Suppose the API's NetworkPolicy was modified and database traffic was accidentally blocked.

Architecture became:

```text
API
 │
 X
 │
Database
```

---

## Remediation

Update the NetworkPolicy to explicitly allow:

```text
API → Database
```

Verify:

```bash
kubectl get networkpolicy
```

---

## Prevention

Implement:

```text
NetworkPolicy tests
GitOps
Policy review
Automated validation
Monitoring
```

---

# Case Study 2 – Banking Platform

## Scenario

A banking application handles:

```text
Accounts
Transactions
Payments
Authentication
Audit Logs
```

Security requirements are strict.

---

## Architecture

```text
Internet
   │
   ▼
API Gateway
   │
   ▼
Authentication
   │
   ▼
Application
   │
   ├── Accounts
   ├── Payments
   └── Transactions
          │
          ▼
       Database
```

---

## Security Requirements

```text
Least Privilege
Network Segmentation
Encryption
Audit Logging
Secret Management
Image Security
Runtime Security
```

---

## Kubernetes Security Design

Use:

```text
RBAC
ServiceAccounts
NetworkPolicy
Pod Security
Secrets
Admission Policies
Image Scanning
Audit Logs
```

---

## Incident

An application attempts to access Kubernetes Secrets belonging to another namespace.

---

## Investigation

Identify the workload:

```bash
kubectl get pods -A
```

Identify its ServiceAccount:

```bash
kubectl get pod <pod> -o jsonpath='{.spec.serviceAccountName}'
```

Check permissions:

```bash
kubectl auth can-i \
  get secrets \
  --as=system:serviceaccount:production:app-sa
```

---

## Root Cause

A ClusterRoleBinding granted excessive permissions.

Example:

```text
ServiceAccount
      ↓
ClusterRole
      ↓
get secrets
      ↓
all namespaces
```

---

## Remediation

Replace cluster-wide permissions with a namespace-scoped Role.

Follow:

```text
Least Privilege
```

---

## Prevention

Implement:

```text
RBAC Reviews
Automated Policy Checks
Admission Policies
Access Auditing
ServiceAccount Separation
```

---

# Case Study 3 – SaaS Platform

## Scenario

A SaaS company hosts thousands of customers.

Each customer requires logical isolation.

---

## Architecture

```text
                Kubernetes Cluster
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
    Tenant A        Tenant B        Tenant C
    Namespace       Namespace       Namespace
```

---

## Requirements

Each tenant should have:

```text
Resource Isolation
Network Isolation
RBAC Isolation
Storage Isolation
```

---

## Kubernetes Controls

Use:

```text
Namespaces
ResourceQuota
LimitRange
NetworkPolicy
RBAC
Dedicated ServiceAccounts
```

---

## Incident

Tenant A experiences a traffic spike.

CPU usage increases dramatically.

---

## Risk

Tenant A could consume resources required by Tenant B.

---

## Solution

Apply ResourceQuota:

```yaml
spec:
  hard:
    requests.cpu: "4"
    requests.memory: 8Gi
    pods: "50"
```

Apply LimitRange for per-container defaults and limits.

---

## Result

```text
Tenant A
   ↓
ResourceQuota
   ↓
Maximum Allowed Resources
```

Other tenants remain protected.

---

# Case Study 4 – High-Traffic Web Application

## Scenario

A website receives:

```text
10,000 requests/minute
```

During a marketing campaign:

```text
100,000 requests/minute
```

---

## Problem

Application becomes overloaded.

---

## Solution

Implement:

```text
HPA
Resource Requests
Resource Limits
Caching
Load Balancing
Multiple Replicas
```

---

## HPA

Example:

```yaml
minReplicas: 3
maxReplicas: 50
```

Target:

```text
CPU = 60%
```

---

## Cluster Autoscaler

If Pods cannot be scheduled because nodes lack capacity:

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
 ↓
Pods Scheduled
```

---

## Important Insight

HPA and Cluster Autoscaler solve different problems.

```text
HPA
→ More or fewer Pods

Cluster Autoscaler
→ More or fewer Nodes
```

---

# Case Study 5 – Microservices Platform

## Scenario

A company has:

```text
Frontend
Users
Orders
Payments
Inventory
Notifications
```

---

## Architecture

```text
Frontend
   │
   ▼
API Gateway
   │
   ├── Users
   ├── Orders
   ├── Payments
   ├── Inventory
   └── Notifications
```

---

## Problem

Orders become slow.

---

## Investigation

Application traces reveal:

```text
Orders
 ↓
Inventory
 ↓
Database
```

Inventory service takes:

```text
2.5 seconds
```

---

## Solution

Implement:

```text
Distributed Tracing
Timeouts
Retries
Caching
Circuit Breaking
```

A service mesh can provide some of these capabilities depending on the architecture.

---

# Case Study 6 – Kubernetes Node Failure

## Scenario

A worker node becomes unavailable.

```text
Node A → NotReady
```

---

## Symptoms

Pods disappear or become unavailable.

---

## Investigation

```bash
kubectl get nodes
```

Output:

```text
Node A   NotReady
```

Inspect:

```bash
kubectl describe node node-a
```

---

## Recovery

If workloads are managed by a Deployment:

```text
Node Failure
    ↓
Pods Lost
    ↓
Controller Detects Difference
    ↓
Replacement Pods
    ↓
Healthy Nodes
```

---

## Important Requirement

Applications must have multiple replicas.

Bad:

```text
Replica = 1
```

Better:

```text
Replica = 3
```

with suitable topology constraints.

---

# Case Study 7 – DNS Outage

## Scenario

Applications suddenly report:

```text
Temporary failure in name resolution
```

---

## Investigation

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Check logs:

```bash
kubectl logs -n kube-system \
  -l k8s-app=kube-dns
```

Test DNS:

```bash
kubectl run dns-test \
  --image=busybox:1.36 \
  -it --rm \
  --restart=Never -- sh
```

Inside:

```bash
nslookup kubernetes.default
```

---

## Potential Causes

```text
CoreDNS failure
CNI failure
NetworkPolicy
DNS configuration
Node networking
Upstream DNS
```

---

## Recovery

Restore the failed component.

Validate:

```bash
nslookup kubernetes.default
```

Then test application connectivity.

---

# Case Study 8 – NetworkPolicy Incident

## Scenario

A new NetworkPolicy is deployed.

Immediately afterward:

```text
Backend cannot reach Database.
```

---

## Investigation

List policies:

```bash
kubectl get networkpolicy -A
```

Describe:

```bash
kubectl describe networkpolicy <name>
```

Check labels:

```bash
kubectl get pods --show-labels
```

---

## Root Cause

The policy selector doesn't match the intended backend Pods.

---

## Fix

Correct:

```yaml
podSelector:
```

or:

```yaml
namespaceSelector:
```

---

## Lesson

NetworkPolicy is label-driven.

```text
Wrong Label
     ↓
Wrong Selection
     ↓
Unexpected Network Behavior
```

---

# Case Study 9 – Storage Failure

## Scenario

A database Pod is stuck:

```text
Pending
```

---

## Investigation

```bash
kubectl get pvc
```

Output:

```text
Pending
```

Describe:

```bash
kubectl describe pvc database-data
```

---

## Check

```bash
kubectl get storageclass
kubectl get pv
kubectl get csidrivers
kubectl get events
```

---

## Possible Causes

```text
Missing StorageClass
CSI Driver Failure
Capacity
Access Mode
Topology
Provisioning Failure
```

---

## Remediation

Fix the underlying storage configuration.

Then:

```bash
kubectl get pvc
```

Expected:

```text
Bound
```

---

# Case Study 10 – ImagePullBackOff

## Scenario

A Deployment update causes all new Pods to fail.

Status:

```text
ImagePullBackOff
```

---

## Investigation

```bash
kubectl describe pod <pod>
```

Look at:

```text
Events
```

---

## Potential Causes

```text
Wrong image name
Wrong tag
Private registry authentication
Registry unavailable
Image deleted
Network failure
```

---

## Solution

Verify image:

```text
registry/image:tag
```

For private registries, verify:

```text
imagePullSecrets
```

---

# Case Study 11 – CrashLoopBackOff

## Scenario

A new application deployment never becomes Ready.

Status:

```text
CrashLoopBackOff
```

---

## Investigation

```bash
kubectl logs <pod>
```

Then:

```bash
kubectl logs <pod> --previous
```

Describe:

```bash
kubectl describe pod <pod>
```

---

## Possible Causes

```text
Application Error
Bad Configuration
Missing Secret
Missing ConfigMap
Database Failure
Incorrect Command
Permission Problem
OOMKilled
```

---

# Case Study 12 – OOMKilled

## Scenario

An application works initially but periodically restarts.

---

## Investigation

```bash
kubectl describe pod <pod>
```

Look for:

```text
Reason: OOMKilled
```

---

## Root Cause

Memory usage exceeds the configured limit.

---

## Remediation

Analyze:

```text
Actual Memory Usage
Memory Leak
Application Configuration
Resource Requests
Resource Limits
```

Increase limits only when justified.

Do not use large limits as a substitute for diagnosing a memory leak.

---

# Case Study 13 – Readiness Probe Failure

## Scenario

Pods are Running but receive no traffic.

---

## Observation

```bash
kubectl get pods
```

Output:

```text
1/1 Running
```

but the Service has fewer or no endpoints.

---

## Investigation

```bash
kubectl describe pod <pod>
kubectl get endpointslices
```

---

## Root Cause

Readiness endpoint returns failure.

---

## Important Lesson

```text
Running ≠ Ready
```

A Pod can be running but intentionally excluded from Service traffic.

---

# Case Study 14 – Liveness Probe Failure

## Scenario

Application repeatedly restarts.

---

## Investigation

```bash
kubectl describe pod <pod>
```

Look for:

```text
Liveness probe failed
```

---

## Root Cause

The liveness probe is incorrectly configured or the application is unhealthy.

---

## Remediation

Check:

```text
Path
Port
Initial Delay
Timeout
Period
Failure Threshold
```

Do not make liveness probes excessively aggressive.

---

# Case Study 15 – Kubernetes API Server Overload

## Scenario

`kubectl` commands become slow.

Applications using the Kubernetes API also experience delays.

---

## Investigation

Check:

```text
API Server Metrics
API Server Logs
Request Rate
Latency
etcd Health
Control Plane Resources
```

---

## Possible Causes

```text
Excessive API Requests
Large List Operations
Controller Loops
etcd Performance
Resource Exhaustion
```

---

## Prevention

Use:

```text
Efficient Controllers
Caching
Watch APIs
Reasonable Polling
API Monitoring
```

---

# Case Study 16 – etcd Failure

## Scenario

The Kubernetes control plane becomes unstable.

---

## Symptoms

```text
API errors
Slow API requests
Controller failures
Scheduler problems
```

---

## Investigation

Check:

```text
etcd health
etcd latency
etcd member status
Control Plane Logs
```

---

## Recovery

For HA clusters:

```text
Healthy etcd Members
        ↓
Quorum
        ↓
Cluster State
```

Always maintain tested etcd backups.

---

# Case Study 17 – Control Plane Failure

## Scenario

One control-plane node fails.

In an HA cluster:

```text
Control Plane A → Failed
Control Plane B → Healthy
Control Plane C → Healthy
```

---

## Result

The cluster should continue operating if quorum and API availability are maintained.

---

## Lesson

High availability requires:

```text
Multiple Control Plane Nodes
Multiple etcd Members
API Load Balancing
Failure-Domain Planning
```

---

# Case Study 18 – Zero-Downtime Deployment

## Scenario

A company must deploy a new application version without service interruption.

---

## Configuration

```text
Replicas = 5
RollingUpdate
Readiness Probe
PodDisruptionBudget
```

---

## Deployment

```bash
kubectl set image deployment/web \
  web=web:v2
```

Monitor:

```bash
kubectl rollout status deployment/web
```

---

## Validation

Check:

```text
Error Rate
Latency
Availability
Pod Readiness
```

---

# Case Study 19 – Failed Deployment Rollback

## Scenario

Version 2 causes:

```text
HTTP 500
```

---

## Investigation

```bash
kubectl rollout history deployment/web
```

Rollback:

```bash
kubectl rollout undo deployment/web
```

Verify:

```bash
kubectl rollout status deployment/web
```

---

## Lesson

Every production deployment should have a tested rollback strategy.

---

# Case Study 20 – Blue/Green Deployment

## Architecture

```text
             Service
                │
       ┌────────┴────────┐
       ▼                 ▼
    Version 1         Version 2
```

Initially:

```text
Service → v1
```

After validation:

```text
Service → v2
```

---

## Advantages

```text
Fast Rollback
Full Environment Testing
Clear Version Separation
```

---

## Disadvantages

```text
Higher Resource Usage
More Infrastructure
Database Compatibility Complexity
```

---

# Case Study 21 – Canary Deployment

## Scenario

A company wants to release a new version to only a small percentage of users.

---

## Strategy

```text
v1 → 90%
v2 → 10%
```

Monitor:

```text
Latency
Errors
Conversion
Resource Usage
```

Then:

```text
10%
 ↓
25%
 ↓
50%
 ↓
100%
```

---

## Stop Condition

Rollback if:

```text
Error Rate ↑
Latency ↑
Availability ↓
Business Metrics ↓
```

---

# Case Study 22 – GitOps Drift

## Scenario

Production is managed through GitOps.

An engineer manually changes:

```bash
kubectl scale deployment web --replicas=1
```

Git declares:

```text
replicas = 5
```

---

## Result

The GitOps controller detects drift and restores:

```text
replicas = 5
```

---

## Lesson

Git becomes the source of truth.

Manual production changes should be controlled and exceptional.

---

# Case Study 23 – Secret Exposure

## Scenario

A developer accidentally commits a Kubernetes Secret manifest containing credentials into Git.

---

## Immediate Actions

```text
1. Revoke credential
2. Rotate credential
3. Identify exposure
4. Remove secret from active repository history where appropriate
5. Audit access
6. Deploy replacement secret
```

---

## Important

Deleting the file from the latest Git commit does not necessarily remove historical copies.

Treat exposed credentials as compromised.

---

# Case Study 24 – Kubernetes Supply Chain Attack

## Scenario

A compromised container image is introduced into a cluster.

---

## Potential Attack Path

```text
Compromised Dependency
        ↓
Malicious Image
        ↓
Container Registry
        ↓
Kubernetes Deployment
        ↓
Production Pod
```

---

## Controls

```text
Trusted Registries
Image Scanning
SBOM
Image Signing
Digest Pinning
Admission Policies
Minimal Images
Runtime Monitoring
```

---

# Case Study 25 – Container Escape Scenario

## Scenario

A workload is compromised and attempts to escape its container boundary.

---

## Risk Factors

```text
Privileged Container
HostPID
HostNetwork
HostPath
Excessive Capabilities
Root User
Weak Runtime Configuration
```

---

## Defensive Controls

Use:

```text
runAsNonRoot
allowPrivilegeEscalation: false
Drop Capabilities
seccomp
AppArmor / SELinux where supported
Pod Security
Runtime Detection
Least Privilege
```

---

# Case Study 26 – Runtime Threat Detection

## Scenario

A container unexpectedly launches:

```text
/bin/sh
```

and accesses sensitive filesystem paths.

---

## Detection

Runtime security tooling can detect suspicious behavior such as:

```text
Unexpected Process Execution
Privilege Escalation
Suspicious File Access
Unexpected Network Connections
```

---

## Response

```text
Detect
 ↓
Validate
 ↓
Isolate
 ↓
Collect Evidence
 ↓
Rotate Credentials
 ↓
Investigate
 ↓
Rebuild Workload
 ↓
Monitor
```

---

# Case Study 27 – Kubernetes Forensics

## Scenario

A Pod is suspected of compromise.

---

## Evidence

Collect:

```text
Pod YAML
Deployment YAML
Events
Logs
ServiceAccount
RBAC
NetworkPolicy
Network Connections
Image Information
Audit Logs
Node Evidence
```

---

## Timeline

Build:

```text
T0 → Initial deployment
T1 → Suspicious process
T2 → Network connection
T3 → Detection
T4 → Containment
T5 → Recovery
```

---

# Case Study 28 – RBAC Privilege Escalation

## Scenario

A compromised application attempts to create privileged resources.

---

## Investigation

Check:

```bash
kubectl auth can-i \
  create pods \
  --as=system:serviceaccount:production:app-sa
```

Review:

```text
Roles
ClusterRoles
RoleBindings
ClusterRoleBindings
```

---

## Root Cause

Excessive permissions:

```text
create
update
patch
```

on sensitive resources.

---

## Prevention

Use:

```text
Least Privilege
Namespace Scope
Separate ServiceAccounts
RBAC Auditing
```

---

# Case Study 29 – Database Failure

## Scenario

Database Pods are unavailable.

---

## Investigation

```bash
kubectl get statefulset
kubectl get pods
kubectl get pvc
kubectl get pv
```

Check:

```text
Database Logs
Storage
Replication
Readiness
Resource Usage
```

---

## Recovery

Depending on the architecture:

```text
Restart
Failover
Restore
Replica Promotion
Backup Recovery
```

Never assume that deleting a database Pod is a safe recovery action.

---

# Case Study 30 – Database Storage Failure

## Scenario

Database Pod cannot mount its volume.

---

## Investigation

```bash
kubectl describe pod <pod>
kubectl describe pvc <pvc>
kubectl describe pv <pv>
```

Check:

```text
CSI
StorageClass
Volume Attachment
Node
Access Mode
```

---

# Case Study 31 – Network Partition

## Scenario

Two nodes cannot communicate.

---

## Symptoms

```text
Pod connectivity failures
Node conditions
Service failures
Timeouts
```

---

## Investigation

Check:

```text
Node Network
CNI
Routes
Firewall
NetworkPolicy
DNS
```

---

## Lesson

Kubernetes networking depends on several layers:

```text
Application
 ↓
Service
 ↓
Cluster Network
 ↓
CNI
 ↓
Node Network
 ↓
Physical / Cloud Network
```

---

# Case Study 32 – Resource Exhaustion

## Scenario

Nodes run out of memory.

---

## Symptoms

```text
Pod Evictions
OOMKilled
Scheduling Failures
Node Pressure
```

---

## Investigation

```bash
kubectl top nodes
kubectl top pods -A
kubectl describe node <node>
```

Look for:

```text
MemoryPressure
DiskPressure
PIDPressure
```

---

## Prevention

```text
Requests
Limits
ResourceQuota
HPA
Cluster Autoscaler
Capacity Planning
```

---

# Case Study 33 – Disk Pressure

## Scenario

A node reports:

```text
DiskPressure=True
```

---

## Potential Causes

```text
Container Logs
Image Layers
Temporary Files
Container Runtime Data
Ephemeral Storage
```

---

## Investigation

Check node storage at the operating-system level where authorized.

Also inspect:

```bash
kubectl describe node <node>
```

---

## Prevention

```text
Log Rotation
Ephemeral Storage Limits
Image Cleanup
Capacity Monitoring
```

---

# Case Study 34 – Certificate Expiration

## Scenario

Kubernetes components begin reporting TLS errors.

---

## Symptoms

```text
API connection failures
Component communication errors
Authentication failures
```

---

## Investigation

Review:

```text
Certificate Expiration
Kubeconfig
Control Plane Certificates
Component Certificates
```

---

## Prevention

```text
Certificate Monitoring
Automated Rotation
Expiration Alerts
Documented Renewal Procedures
```

---

# Case Study 35 – Cluster Upgrade Failure

## Scenario

A Kubernetes upgrade causes workloads to behave unexpectedly.

---

## Potential Causes

```text
API Deprecation
Version Skew
Admission Changes
CNI Compatibility
CSI Compatibility
Ingress Controller Compatibility
CRD Compatibility
```

---

## Prevention

Before upgrading:

```text
Backup
Read Release Notes
Check Deprecated APIs
Test in Staging
Validate Add-ons
Plan Rollback
```

---

# Case Study 36 – Admission Policy Blocks Deployment

## Scenario

A Deployment fails during creation.

Error indicates:

```text
Admission webhook denied request.
```

---

## Investigation

Check:

```text
Admission Configuration
Policy
Webhook
Namespace Labels
Pod Security
```

---

## Common Causes

```text
Privileged Container
Missing SecurityContext
Untrusted Image
Missing Labels
Policy Violation
```

---

# Case Study 37 – Multi-Cluster Architecture

## Scenario

A global SaaS platform needs:

```text
India Cluster
Europe Cluster
US Cluster
```

---

## Architecture

```text
Global Traffic Management
        │
   ┌────┼────┐
   ▼    ▼    ▼
 India EU    US
Cluster Cluster Cluster
```

---

## Benefits

```text
Regional Availability
Latency Reduction
Failure Isolation
Compliance
```

---

## Challenges

```text
Data Replication
Global Identity
Deployment Coordination
Observability
Cost
```

---

# Case Study 38 – Disaster Recovery

## Scenario

A production cluster is lost.

---

## Recovery Architecture

```text
Primary Cluster
       │
       │ Backups
       ▼
 Backup Storage
       │
       ▼
DR Cluster
```

---

## Recovery Steps

```text
1. Provision cluster
2. Configure networking
3. Restore cluster resources
4. Restore secrets
5. Restore storage
6. Deploy applications
7. Validate services
8. Redirect traffic
9. Monitor
```

---

# Case Study 39 – Ransomware Scenario

## Scenario

A compromised workload attempts to encrypt application data.

---

## Response

```text
Detect
 ↓
Isolate Workload
 ↓
Block Network
 ↓
Preserve Evidence
 ↓
Rotate Credentials
 ↓
Identify Scope
 ↓
Restore From Clean Backup
 ↓
Validate
 ↓
Harden
```

---

## Key Requirement

Backups must be:

```text
Regular
Protected
Tested
Recoverable
Separated From Primary Failure Domain
```

---

# Case Study 40 – Production Incident Management

## Scenario

Production API availability drops to 80%.

---

## Incident Process

```text
Detection
 ↓
Incident Declaration
 ↓
Impact Assessment
 ↓
Mitigation
 ↓
Root Cause Investigation
 ↓
Recovery
 ↓
Monitoring
 ↓
Postmortem
```

---

## Incident Questions

Ask:

```text
What changed?
When did it change?
What is affected?
What is not affected?
Can we roll back?
Can we isolate the failure?
What is the safest mitigation?
```

---

# Case Study 41 – Observability Failure

## Scenario

Application is failing but dashboards show no metrics.

---

## Investigation

Check:

```text
Metrics Agent
Prometheus
ServiceMonitor
Network
Scrape Configuration
RBAC
```

---

## Lesson

Observability itself is a production dependency.

You need monitoring for:

```text
Applications
Kubernetes
Monitoring Stack
Alerting Pipeline
```

---

# Case Study 42 – Alert Fatigue

## Scenario

The operations team receives thousands of alerts every day.

---

## Problem

Important alerts are ignored.

---

## Solution

Design alerts around:

```text
User Impact
SLOs
Error Budget
Actionability
Severity
```

Avoid alerting on every small fluctuation.

---

# Case Study 43 – SLO-Based Kubernetes Monitoring

Define:

```text
Availability SLO = 99.9%
Latency SLO = 95% < 300ms
```

Monitor:

```text
Availability
Latency
Error Rate
Traffic
```

---

## Error Budget

If SLO:

```text
99.9%
```

then allowed unavailability is approximately:

```text
0.1%
```

Use error budgets to guide:

```text
Release Risk
Reliability Work
Incident Response
```

---

# Case Study 44 – CI/CD Pipeline

## Architecture

```text
Developer
   ↓
Git
   ↓
CI
   ↓
Tests
   ↓
Security Scan
   ↓
Build Image
   ↓
Registry
   ↓
Deployment
   ↓
Kubernetes
```

---

## Security Gates

Include:

```text
SAST
Dependency Scanning
Container Scanning
Secret Scanning
SBOM
Image Signing
Policy Validation
```

---

# Case Study 45 – Secure Software Supply Chain

## Goal

Prevent untrusted artifacts from reaching production.

---

## Pipeline

```text
Source
 ↓
Build
 ↓
Test
 ↓
Scan
 ↓
Generate SBOM
 ↓
Sign Image
 ↓
Verify Signature
 ↓
Deploy
```

---

# Case Study 46 – Production Resource Optimization

## Scenario

Cluster cost is increasing.

---

## Investigation

Check:

```bash
kubectl top nodes
kubectl top pods -A
```

Compare:

```text
Requested CPU
Actual CPU
Requested Memory
Actual Memory
```

---

## Optimization

Adjust:

```text
Requests
Limits
Replica Counts
HPA
Node Sizes
Workload Placement
```

---

# Case Study 47 – Overprovisioned Workloads

## Scenario

A service requests:

```text
CPU = 4 cores
Memory = 8Gi
```

but normally consumes:

```text
CPU = 200m
Memory = 500Mi
```

---

## Problem

Scheduling capacity is wasted.

---

## Solution

Use observed usage to establish appropriate requests while maintaining sufficient headroom.

---

# Case Study 48 – Underprovisioned Workloads

## Scenario

A service requests:

```text
CPU = 100m
Memory = 128Mi
```

but regularly requires:

```text
CPU = 1 core
Memory = 1Gi
```

---

## Symptoms

```text
Throttling
OOMKilled
Poor Performance
```

---

## Solution

Tune requests and limits based on measured workload behavior.

---

# Case Study 49 – Pod Topology Failure

## Scenario

Three replicas are accidentally scheduled onto the same node.

---

## Risk

```text
Node Failure
   ↓
All Replicas Lost
```

---

## Solution

Use:

```text
Pod Anti-Affinity
Topology Spread Constraints
```

---

# Case Study 50 – Complete Production Architecture

## Scenario

Design a highly available enterprise Kubernetes platform.

---

## Architecture

```text
                         Internet
                            │
                            ▼
                     Global Load Balancer
                            │
                    ┌───────┴───────┐
                    ▼               ▼
               Cluster A       Cluster B
                    │               │
              ┌─────┴─────┐   ┌─────┴─────┐
              ▼           ▼   ▼           ▼
           Ingress     Gateway Ingress   Gateway
              │           │      │          │
              └─────┬─────┘      └────┬─────┘
                    ▼                  ▼
                Services           Services
                    │                  │
              Deployments          Deployments
                    │                  │
                StatefulSets       StatefulSets
                    │                  │
                 Storage             Storage
```

---

## Platform Layer

```text
Kubernetes
CNI
CSI
CoreDNS
Ingress / Gateway
```

---

## Security Layer

```text
RBAC
Pod Security
NetworkPolicy
Secrets
Admission Policies
Image Security
Runtime Security
Audit
```

---

## Observability Layer

```text
Prometheus
Grafana
Alertmanager
OpenTelemetry
Logging
Tracing
```

---

## Operations Layer

```text
GitOps
CI/CD
Helm
Kustomize
Backup
DR
Upgrade Automation
Incident Response
```

---

# Case Study Analysis Framework

For every production incident, use this framework:

## 1. Identify

```text
What is broken?
```

## 2. Scope

```text
Which users?
Which namespaces?
Which workloads?
Which nodes?
```

## 3. Timeline

```text
When did it start?
What changed immediately before it?
```

## 4. Evidence

Collect:

```text
Events
Logs
Metrics
Traces
Resource Definitions
Audit Logs
```

## 5. Hypothesis

Form a testable theory.

Example:

```text
"The API cannot reach the database because the
new NetworkPolicy blocks egress."
```

## 6. Test

Use targeted commands.

```bash
kubectl describe
kubectl logs
kubectl get
kubectl auth can-i
```

## 7. Root Cause

Identify the actual failure.

## 8. Remediation

Apply the smallest safe fix.

## 9. Validation

Confirm:

```text
Availability
Performance
Security
Data Integrity
```

## 10. Prevention

Implement:

```text
Automation
Monitoring
Testing
Policy
Documentation
```

---

# Production Incident Severity

## SEV-1

```text
Major production outage
Critical security incident
Large-scale data loss
```

Immediate response.

---

## SEV-2

```text
Major degradation
Important functionality unavailable
Significant customer impact
```

Urgent response.

---

## SEV-3

```text
Limited impact
Workaround available
```

Normal incident response.

---

# Golden Signals

Monitor:

```text
Latency
Traffic
Errors
Saturation
```

These provide a useful high-level view of application health.

---

# Kubernetes Golden Signals

Add:

```text
Pod Restarts
Pending Pods
Node Pressure
API Server Latency
DNS Health
Storage Health
```

---

# Production Debugging Priority

When an incident occurs:

```text
1. Is the application reachable?
2. Are Pods healthy?
3. Are Pods Ready?
4. Are Services configured correctly?
5. Are endpoints present?
6. Is DNS working?
7. Is networking working?
8. Is storage healthy?
9. Are resources sufficient?
10. Are security policies blocking traffic?
11. Did a recent change cause the issue?
```

---

# Security Incident Priority

For a suspected compromise:

```text
1. Confirm
2. Scope
3. Contain
4. Preserve Evidence
5. Revoke Credentials
6. Investigate
7. Eradicate
8. Recover
9. Monitor
10. Postmortem
```

---

# Common Production Mistakes

Avoid:

```text
❌ Running everything as root
❌ Using default ServiceAccounts unnecessarily
❌ Excessive ClusterRole permissions
❌ No NetworkPolicies
❌ Hard-coded credentials
❌ Mutable production image tags without controls
❌ No resource requests
❌ No health probes
❌ Single application replica
❌ No backup
❌ Untested restore process
❌ No monitoring
❌ No alerting
❌ Manual production changes
❌ Uncontrolled force deletion
❌ Untested upgrades
```

---

# Production Design Principles

## Principle 1 – Least Privilege

```text
Give workloads only what they need.
```

## Principle 2 – Defense in Depth

```text
Identity
+
Network
+
Runtime
+
Image
+
Admission
+
Monitoring
```

## Principle 3 – Assume Failure

Design for:

```text
Pod Failure
Node Failure
Zone Failure
Network Failure
Storage Failure
Control Plane Failure
```

## Principle 4 – Automate

Automate:

```text
Deployment
Testing
Security
Monitoring
Backup
Recovery
```

## Principle 5 – Observe Everything Important

You cannot reliably operate what you cannot observe.

---

# Final Case Study Challenge

Design a Kubernetes platform for an online banking application.

Requirements:

```text
10 million users
99.99% availability
Multi-region
Encrypted traffic
Strict RBAC
Network segmentation
Automated deployment
Real-time monitoring
Centralized logging
Distributed tracing
Disaster recovery
Security monitoring
```

You must design:

```text
Cluster Architecture
Networking
Storage
Security
Identity
RBAC
Observability
CI/CD
GitOps
Backup
DR
Incident Response
```

---

# Expected Architecture

```text
                         Global Traffic
                               │
                ┌──────────────┴──────────────┐
                ▼                             ▼
           Region A                       Region B
                │                             │
        ┌───────┴───────┐             ┌───────┴───────┐
        ▼               ▼             ▼               ▼
     Gateway         Gateway       Gateway         Gateway
        │               │             │               │
        ▼               ▼             ▼               ▼
    Services        Services      Services        Services
        │               │             │               │
        ▼               ▼             ▼               ▼
   Applications     Applications   Applications     Applications
        │               │             │               │
        ▼               ▼             ▼               ▼
     Storage          Storage       Storage          Storage
```

Supporting platform:

```text
RBAC
NetworkPolicy
Pod Security
Secrets
Admission
Image Security
Runtime Security
Prometheus
Grafana
Alertmanager
OpenTelemetry
Logging
GitOps
Backup
DR
```

---

# Final Takeaways

Real-world Kubernetes expertise comes from understanding the relationship between:

```text
Application
     ↓
Pod
     ↓
Deployment
     ↓
Service
     ↓
Networking
     ↓
Storage
     ↓
Scheduling
     ↓
Security
     ↓
Observability
     ↓
Operations
```

A production incident rarely belongs to a single Kubernetes object.

For example:

```text
Service Failure
```

may actually involve:

```text
Service
 ↓
EndpointSlice
 ↓
Pod Labels
 ↓
Readiness
 ↓
NetworkPolicy
 ↓
CNI
 ↓
DNS
```

Similarly:

```text
Pod Pending
```

may involve:

```text
Scheduler
 ↓
Requests
 ↓
Node Capacity
 ↓
Affinity
 ↓
Taints
 ↓
Topology
 ↓
Storage
```

The goal of production troubleshooting is therefore not to memorize commands.

It is to understand the **dependency chain**.

---

# Core Production Mindset

```text
Observe
  ↓
Hypothesize
  ↓
Test
  ↓
Confirm
  ↓
Mitigate
  ↓
Recover
  ↓
Prevent
```

> **The best Kubernetes engineers are not those who never experience failures. They are the engineers who can systematically detect, isolate, explain, recover from, and prevent failures.**

---

# Next Chapter

## Chapter 88 – Troubleshooting Playbook

The next chapter converts the case studies into a practical troubleshooting reference covering:

```text
Pod Troubleshooting
Deployment Troubleshooting
Service Troubleshooting
DNS Troubleshooting
Ingress Troubleshooting
NetworkPolicy Troubleshooting
Storage Troubleshooting
Scheduling Troubleshooting
RBAC Troubleshooting
Node Troubleshooting
Resource Troubleshooting
HPA Troubleshooting
StatefulSet Troubleshooting
DaemonSet Troubleshooting
Control Plane Troubleshooting
etcd Troubleshooting
CNI Troubleshooting
CSI Troubleshooting
Security Incident Troubleshooting
Performance Troubleshooting
Production Incident Response
Root Cause Analysis
```
```