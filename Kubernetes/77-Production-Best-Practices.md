# Chapter 77 – Production Best Practices

## Overview

Running Kubernetes in production requires more than simply deploying applications successfully.

A production Kubernetes environment must be:

```text
Secure
Reliable
Observable
Scalable
Maintainable
Performant
Cost-Efficient
Recoverable
```

Production best practices combine everything learned throughout Kubernetes administration, networking, storage, security, observability, and operations.

A simplified production lifecycle is:

```text
Design
  ↓
Build
  ↓
Secure
  ↓
Deploy
  ↓
Observe
  ↓
Operate
  ↓
Optimize
  ↓
Recover
  ↓
Improve
```

A production-ready Kubernetes platform should follow:

```text
Least Privilege
+
High Availability
+
Defense in Depth
+
Automation
+
Observability
+
Infrastructure as Code
+
Continuous Improvement
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes production readiness
- Production architecture
- Cluster design
- Node design
- Workload design
- Namespace strategy
- Resource management
- Resource requests
- Resource limits
- Quality of Service
- Pod disruption budgets
- High availability
- Multi-zone deployments
- Scheduling
- Node affinity
- Pod affinity
- Pod anti-affinity
- Taints
- Tolerations
- Autoscaling
- Horizontal Pod Autoscaler
- Vertical Pod Autoscaler
- Cluster Autoscaler
- Deployment strategies
- Rolling updates
- Rollbacks
- Blue-green deployments
- Canary deployments
- Health checks
- Liveness probes
- Readiness probes
- Startup probes
- Graceful shutdown
- SecurityContext
- Pod Security
- RBAC
- ServiceAccounts
- Secrets
- NetworkPolicies
- Image security
- Supply-chain security
- Admission policies
- Runtime security
- Logging
- Monitoring
- Metrics
- Alerting
- Distributed tracing
- Backup
- Disaster recovery
- Cluster upgrades
- Maintenance
- Capacity planning
- Performance optimization
- Cost optimization
- Configuration management
- GitOps
- Infrastructure as Code
- CI/CD
- Reliability engineering
- SLOs
- SLIs
- SLAs
- Error budgets
- Production troubleshooting
- Incident response
- Runbooks
- Documentation
- Change management
- Security hardening
- Compliance
- Production checklists
- Common mistakes
- Hands-on labs
- Interview questions

---

# What Is Production-Ready Kubernetes?

A production-ready Kubernetes environment should be capable of:

```text
Handling Failures
+
Protecting Workloads
+
Scaling Applications
+
Providing Visibility
+
Recovering From Incidents
+
Supporting Safe Changes
```

---

# Production Readiness Model

```text
                 Production
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    Security      Reliability   Observability
       │             │             │
       └─────────────┼─────────────┘
                     ▼
                  Operations
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    Scaling       Recovery       Cost
```

---

# Production Architecture

A typical production platform may contain:

```text
Users
  ↓
DNS
  ↓
Load Balancer
  ↓
Gateway / Ingress
  ↓
Kubernetes Service
  ↓
Pods
  ↓
Application
  ↓
Database / External Services
```

Supporting systems:

```text
Monitoring
Logging
Security
Backup
CI/CD
Registry
Secrets
```

---

# Cluster Design

Production cluster design should consider:

```text
Availability
Capacity
Security
Network
Storage
Failure Domains
Compliance
Cost
```

---

# Availability Zones

Where supported, distribute workloads across multiple availability zones.

Example:

```text
Zone A
 ├── Node 1
 └── Node 2

Zone B
 ├── Node 3
 └── Node 4

Zone C
 ├── Node 5
 └── Node 6
```

This reduces dependence on a single zone.

---

# Failure Domains

Important failure domains include:

```text
Pod
Node
Rack
Availability Zone
Region
Cluster
Cloud Provider
```

Production architecture should understand which failures it can tolerate.

---

# Namespace Strategy

Namespaces can provide organizational and security boundaries.

Example:

```text
production
staging
development
monitoring
security
platform
```

Avoid creating namespaces without a clear ownership or isolation purpose.

---

# Namespace Ownership

Define:

```text
Owner
Purpose
Environment
Access
Resource Quota
Network Policy
```

---

# Resource Quotas

Use ResourceQuota to prevent one namespace from consuming unlimited cluster resources.

Example:

```yaml
apiVersion: v1
kind: ResourceQuota
metadata:
  name: production-quota
  namespace: production
spec:
  requests.cpu: "20"
  requests.memory: 40Gi
  limits.cpu: "40"
  limits.memory: 80Gi
```

---

# LimitRange

LimitRange can define default or allowed resource values within a namespace.

Example:

```yaml
apiVersion: v1
kind: LimitRange
metadata:
  name: default-limits
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

# Resource Requests

Requests tell Kubernetes how much resource a container expects to require.

Example:

```yaml
resources:
  requests:
    cpu: "250m"
    memory: "256Mi"
```

---

# Resource Limits

Limits place an upper bound on resource consumption.

Example:

```yaml
resources:
  limits:
    cpu: "1"
    memory: "1Gi"
```

---

# Why Requests Matter

Requests influence:

```text
Scheduling
Capacity Planning
Autoscaling
QoS
```

---

# Why Limits Matter

Limits can prevent workloads from consuming unlimited resources.

However, poorly chosen limits can cause:

```text
OOMKilled
CPU Throttling
Application Instability
```

---

# Quality of Service

Kubernetes QoS classes include:

```text
Guaranteed
Burstable
BestEffort
```

---

# Guaranteed

Generally achieved when containers have matching CPU and memory requests and limits for all applicable containers.

---

# Burstable

Used when resource requests and limits are defined but do not meet Guaranteed criteria.

---

# BestEffort

Used when containers have no CPU or memory requests or limits.

---

# Production Recommendation

Avoid leaving critical workloads without resource requests.

Define resources based on:

```text
Measured Usage
+
Expected Load
+
Safety Margin
```

---

# Pod Disruption Budget

PDB helps maintain application availability during voluntary disruptions.

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

# Why PDB Matters

During:

```text
Node Maintenance
Cluster Upgrades
Voluntary Evictions
```

PDB can help prevent excessive simultaneous disruption.

---

# High Availability

High availability means the application can continue operating despite expected failures.

Use:

```text
Multiple Replicas
+
Multiple Nodes
+
Multiple Zones
+
Health Checks
+
Load Balancing
```

---

# Replica Strategy

Avoid:

```yaml
replicas: 1
```

for critical stateless workloads unless there is a deliberate reason.

Prefer multiple replicas based on availability requirements.

---

# Pod Anti-Affinity

Pod anti-affinity can distribute replicas across nodes.

Example concept:

```yaml
affinity:
  podAntiAffinity:
    preferredDuringSchedulingIgnoredDuringExecution:
      - weight: 100
        podAffinityTerm:
          topologyKey: kubernetes.io/hostname
          labelSelector:
            matchLabels:
              app: api
```

---

# Topology Spread Constraints

Topology spread constraints provide another mechanism for distributing workloads across failure domains.

Example:

```yaml
topologySpreadConstraints:
  - maxSkew: 1
    topologyKey: topology.kubernetes.io/zone
    whenUnsatisfiable: DoNotSchedule
    labelSelector:
      matchLabels:
        app: api
```

---

# Node Affinity

Use node affinity when workloads should run on specific nodes or infrastructure.

Examples:

```text
GPU Nodes
SSD Nodes
High-Memory Nodes
Specific Zones
```

---

# Taints and Tolerations

Taints prevent workloads from being scheduled onto nodes unless they tolerate the taint.

Useful for:

```text
Dedicated Nodes
GPU Nodes
Security-Sensitive Nodes
Infrastructure Nodes
```

---

# Health Checks

Production workloads should generally use appropriate probes.

Three major probe types:

```text
Startup
Readiness
Liveness
```

---

# Startup Probe

Startup probes help applications that require significant initialization time.

Example:

```yaml
startupProbe:
  httpGet:
    path: /startup
    port: 8080
  failureThreshold: 30
  periodSeconds: 10
```

---

# Readiness Probe

Readiness determines whether a Pod should receive traffic.

Example:

```yaml
readinessProbe:
  httpGet:
    path: /ready
    port: 8080
```

---

# Liveness Probe

Liveness helps detect containers that are unhealthy and need restarting.

Example:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8080
```

---

# Probe Best Practice

Do not make liveness checks depend on external systems unnecessarily.

Bad example:

```text
Liveness
   ↓
Database
   ↓
Database Down
   ↓
Application Restarted
```

This can create restart storms.

---

# Graceful Shutdown

Applications should handle termination signals.

Conceptually:

```text
SIGTERM
  ↓
Stop Accepting New Requests
  ↓
Finish Existing Requests
  ↓
Cleanup
  ↓
Exit
```

---

# terminationGracePeriodSeconds

Example:

```yaml
spec:
  terminationGracePeriodSeconds: 30
```

Choose the value based on application behavior.

---

# Deployment Strategy

Common deployment strategies include:

```text
Rolling Update
Blue-Green
Canary
Recreate
```

---

# Rolling Update

The new version gradually replaces the old version.

Example:

```text
v1 v1 v1 v1
 ↓
v1 v1 v1 v2
 ↓
v1 v1 v2 v2
 ↓
v1 v2 v2 v2
 ↓
v2 v2 v2 v2
```

---

# Rolling Update Configuration

Example:

```yaml
strategy:
  type: RollingUpdate
  rollingUpdate:
    maxUnavailable: 1
    maxSurge: 1
```

---

# Blue-Green Deployment

Two environments:

```text
Blue = Current
Green = New
```

Traffic switches:

```text
Blue
 ↓
Green
```

Rollback:

```text
Green
 ↓
Blue
```

---

# Canary Deployment

A small percentage of traffic is sent to the new version.

Example:

```text
95% → v1
5%  → v2
```

If healthy:

```text
90% → v1
10% → v2
```

Eventually:

```text
0% → v1
100% → v2
```

---

# Rollbacks

Always have a rollback strategy.

Example:

```bash
kubectl rollout history deployment/api
```

Rollback:

```bash
kubectl rollout undo deployment/api
```

---

# Deployment Status

Check:

```bash
kubectl rollout status deployment/api
```

---

# Configuration Management

Separate:

```text
Application Code
Configuration
Secrets
Infrastructure
```

---

# ConfigMaps

Use ConfigMaps for non-sensitive configuration.

Example:

```yaml
envFrom:
  - configMapRef:
      name: app-config
```

---

# Secrets

Use Secrets for sensitive data, but understand that Kubernetes Secret objects alone do not automatically solve all secret-management requirements.

Consider:

```text
External Secret Managers
Encryption at Rest
Rotation
Short-Lived Credentials
Access Control
```

---

# Never Hardcode Secrets

Avoid:

```yaml
password: MyPassword123
```

inside source code or Git repositories.

---

# Image Best Practices

Use:

```text
Small Images
Minimal Packages
Pinned Versions
Image Digests
Approved Registries
Vulnerability Scanning
SBOM
Signing
```

---

# Avoid `latest`

Avoid:

```yaml
image: nginx:latest
```

for production workloads when deterministic deployments are required.

Prefer a controlled version and, where appropriate, an immutable digest.

---

# Image Pull Policy

Choose deliberately based on deployment strategy.

Avoid relying on implicit behavior when deterministic production behavior matters.

---

# Non-Root Containers

Where possible:

```yaml
securityContext:
  runAsNonRoot: true
```

---

# Read-Only Filesystem

Where supported:

```yaml
securityContext:
  readOnlyRootFilesystem: true
```

This can reduce the impact of certain attacks.

---

# Drop Capabilities

Example:

```yaml
securityContext:
  capabilities:
    drop:
      - ALL
```

Add only capabilities that are genuinely required.

---

# Privilege Escalation

Where appropriate:

```yaml
securityContext:
  allowPrivilegeEscalation: false
```

---

# Seccomp

Use an appropriate seccomp profile.

Example:

```yaml
securityContext:
  seccompProfile:
    type: RuntimeDefault
```

---

# Network Security

Production clusters should implement network segmentation.

Use:

```text
NetworkPolicy
Gateway
Ingress Controls
Egress Controls
Firewall
Cloud Network Controls
```

---

# Default-Deny Networking

A common strategy:

```text
Deny All
   ↓
Allow Required Traffic
```

This follows a least-privilege networking model.

---

# RBAC

Use least privilege.

Avoid:

```text
cluster-admin
```

unless absolutely necessary.

---

# ServiceAccounts

Create dedicated ServiceAccounts for workloads.

Avoid sharing one highly privileged ServiceAccount across many applications.

---

# ServiceAccount Example

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: api-service
  namespace: production
```

---

# Disable Unnecessary Token Mounting

If a Pod does not need Kubernetes API access:

```yaml
automountServiceAccountToken: false
```

---

# Admission Policies

Use admission controls to prevent unsafe configurations.

Examples:

```text
Privileged Containers
Unapproved Images
Missing Resources
Missing Labels
HostPath
Host Networking
```

---

# Policy as Code

Store policies in version control.

Example:

```text
Git
 ↓
Review
 ↓
Test
 ↓
Policy
 ↓
Cluster
```

---

# GitOps

Production changes should ideally be traceable.

Example:

```text
Developer
   ↓
Git Commit
   ↓
Review
   ↓
CI
   ↓
Policy Checks
   ↓
Deployment
```

---

# Infrastructure as Code

Use tools such as:

```text
Terraform
OpenTofu
Pulumi
CloudFormation
```

where appropriate.

Benefits:

```text
Repeatability
Version Control
Review
Automation
Drift Detection
```

---

# CI/CD Security

CI/CD should validate:

```text
Code
Dependencies
Secrets
Images
SBOM
Manifests
Policies
```

---

# Observability

Production systems require:

```text
Logs
Metrics
Traces
Alerts
```

---

# The Three Pillars

```text
Logs
Metrics
Traces
```

Together they provide broader system visibility.

---

# Metrics

Monitor:

```text
CPU
Memory
Network
Disk
Pod Restarts
Request Rate
Latency
Error Rate
```

---

# Golden Signals

Common service-level signals:

```text
Latency
Traffic
Errors
Saturation
```

---

# Logging

Centralize logs instead of relying exclusively on local node storage.

A typical pipeline:

```text
Pod
 ↓
Log Collector
 ↓
Central Storage
 ↓
Search / SIEM
```

---

# Distributed Tracing

Tracing helps follow a request across services.

Example:

```text
Client
 ↓
Gateway
 ↓
Frontend
 ↓
API
 ↓
Database
```

---

# Alerting

Alerts should be:

```text
Actionable
Specific
Prioritized
Context-Rich
```

Avoid alerting on every minor event.

---

# Service Level Objectives

SLOs define target reliability.

Example:

```text
Availability SLO = 99.9%
```

---

# Service Level Indicators

SLIs are measurements used to evaluate service performance.

Example:

```text
Successful Requests
-------------------
Total Requests
```

---

# Service Level Agreements

An SLA is typically an external or contractual commitment.

Do not confuse:

```text
SLI
SLO
SLA
```

---

# Error Budget

If the SLO is:

```text
99.9%
```

the remaining availability budget can be used to reason about acceptable unreliability and change risk.

---

# Monitoring Kubernetes

Monitor:

```text
Control Plane
Nodes
Pods
Containers
Services
Ingress/Gateway
Storage
Network
API Server
```

---

# Monitoring Nodes

Important metrics:

```text
CPU
Memory
Disk
Disk I/O
Network
Filesystem
Pressure
```

---

# Monitoring Pods

Monitor:

```text
Restarts
CPU
Memory
Ready Status
OOMKilled
CrashLoopBackOff
```

---

# Monitoring Deployments

Monitor:

```text
Desired Replicas
Available Replicas
Updated Replicas
Unavailable Replicas
```

---

# Storage Monitoring

Monitor:

```text
Capacity
Usage
IOPS
Latency
Errors
PVC Status
```

---

# Database Dependencies

Kubernetes may run the application while the real bottleneck is an external database.

Monitor dependencies:

```text
Database
Cache
Message Queue
External API
Object Storage
```

---

# Backup Strategy

Back up:

```text
Application Data
Persistent Volumes
Kubernetes Configuration
Cluster State Where Applicable
```

---

# Backup Verification

A backup that cannot be restored is not a reliable backup strategy.

Test:

```text
Backup
 ↓
Restore
 ↓
Validation
```

---

# Disaster Recovery

Define:

```text
RPO
RTO
Recovery Procedures
Dependencies
Responsibilities
```

---

# RPO

Recovery Point Objective defines the maximum acceptable amount of data loss.

Example:

```text
RPO = 15 minutes
```

---

# RTO

Recovery Time Objective defines the target time to restore service.

Example:

```text
RTO = 1 hour
```

---

# Cluster Upgrades

Never treat Kubernetes upgrades as a casual package update.

Plan:

```text
Compatibility
Backup
Testing
Version Skew
Add-ons
Storage
Networking
Rollback
```

---

# Upgrade Process

```text
Review
 ↓
Test
 ↓
Backup
 ↓
Upgrade
 ↓
Validate
 ↓
Monitor
```

---

# Maintenance

Production maintenance should be:

```text
Planned
Automated
Documented
Observable
Reversible
```

---

# Node Maintenance

Use appropriate node lifecycle operations.

Example:

```bash
kubectl cordon <node>
```

Then drain when appropriate:

```bash
kubectl drain <node>
```

Understand workload disruption before draining production nodes.

---

# Change Management

Every important production change should have:

```text
Owner
Reason
Risk
Approval
Implementation Plan
Rollback Plan
Validation
```

---

# Deployment Windows

For sensitive changes, define:

```text
Maintenance Window
On-Call Coverage
Monitoring
Rollback Criteria
```

---

# Capacity Planning

Monitor:

```text
Current Usage
Growth
Peak Load
Seasonality
Failure Capacity
```

---

# Headroom

Do not operate the cluster permanently at near-maximum capacity.

Maintain enough headroom for:

```text
Traffic Spikes
Node Failures
Deployments
System Pods
Autoscaling
```

---

# Autoscaling

Use:

```text
HPA
VPA
Cluster Autoscaler
```

where appropriate.

---

# Horizontal Pod Autoscaler

Scales the number of Pod replicas.

Example:

```text
Low Traffic
 ↓
2 Pods

High Traffic
 ↓
8 Pods
```

---

# Vertical Pod Autoscaler

Adjusts resource requests and limits according to observed usage, depending on its configured mode.

---

# Cluster Autoscaler

Adjusts node capacity based on scheduling demand in supported environments.

---

# Cost Optimization

Optimize:

```text
Overprovisioning
Idle Resources
Storage
Network
Node Types
Autoscaling
```

---

# Cost vs Reliability

Do not optimize cost blindly.

Example:

```text
1 Node
 ↓
Cheap
 ↓
High Failure Risk
```

versus:

```text
3 Nodes
 ↓
Higher Cost
 ↓
Higher Availability
```

---

# Production Security

Use defense in depth:

```text
Identity
+
RBAC
+
Pod Security
+
Network Policy
+
Image Security
+
Runtime Security
+
Audit
```

---

# Zero Trust Principles

A production Kubernetes architecture should avoid assuming:

```text
Internal = Trusted
```

Instead:

```text
Verify
Authenticate
Authorize
Encrypt
Monitor
```

---

# Encryption

Use encryption where appropriate for:

```text
Network Traffic
Secrets
Storage
Backups
```

---

# TLS

Secure communication between services and external clients using appropriate TLS configurations.

---

# Certificate Management

Monitor:

```text
Expiration
Issuance
Rotation
Trust Chain
```

Automated certificate management can reduce manual errors.

---

# DNS Reliability

Production systems depend heavily on DNS.

Monitor:

```text
DNS Availability
Latency
Failures
Configuration
```

---

# Network Reliability

Monitor:

```text
Packet Loss
Latency
Connections
Load Balancers
Ingress/Gateway
```

---

# Pod Lifecycle

Understand:

```text
Pending
Running
Succeeded
Failed
Unknown
```

and container states such as:

```text
Waiting
Running
Terminated
```

---

# CrashLoopBackOff

A Pod repeatedly restarting may indicate:

```text
Application Failure
Configuration Error
Dependency Failure
Resource Problem
Probe Failure
```

Investigate:

```bash
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

---

# OOMKilled

An OOMKilled container may indicate:

```text
Insufficient Memory
Memory Leak
Incorrect Limit
Unexpected Load
```

Investigate resource configuration and actual usage.

---

# Production Troubleshooting

Use a systematic process:

```text
Detect
 ↓
Scope
 ↓
Collect Evidence
 ↓
Form Hypothesis
 ↓
Test
 ↓
Fix
 ↓
Validate
 ↓
Document
```

---

# Troubleshooting Golden Rule

Do not immediately change multiple variables.

Otherwise:

```text
Problem
 ↓
Five Changes
 ↓
Problem Disappears
 ↓
Unknown Root Cause
```

Make controlled changes where possible.

---

# Runbooks

A runbook documents how to respond to a known operational problem.

Example:

```text
Problem:
API Pods CrashLoopBackOff

Steps:
1. Check Pod status
2. Check events
3. Check current logs
4. Check previous logs
5. Check configuration
6. Check resources
7. Check dependencies
8. Apply approved remediation
9. Validate
```

---

# Incident Response

Production incidents should have:

```text
Detection
Severity
Owner
Communication
Containment
Recovery
Root Cause
Postmortem
```

---

# On-Call

Define:

```text
Primary On-Call
Secondary On-Call
Escalation
Contact Method
Severity Criteria
```

---

# Documentation

Document:

```text
Architecture
Dependencies
Runbooks
Recovery
Security Controls
Ownership
Configuration
Known Issues
```

---

# Production Readiness Review

Before production deployment, review:

```text
Security
Availability
Performance
Observability
Backup
Recovery
Scaling
Cost
Documentation
```

---

# Production Readiness Checklist

```text
☑ Multiple replicas configured where required
☑ Resource requests defined
☑ Resource limits reviewed
☑ Health probes configured
☑ Graceful shutdown implemented
☑ PDB configured where appropriate
☑ Topology distribution reviewed
☑ NetworkPolicies implemented
☑ RBAC least privilege
☑ Dedicated ServiceAccount
☑ Secrets protected
☑ Images scanned
☑ Image versions controlled
☑ SecurityContext configured
☑ Non-root where possible
☑ Capabilities minimized
☑ seccomp configured
☑ Admission policies implemented
☑ Runtime monitoring enabled
☑ Centralized logging enabled
☑ Metrics available
☑ Alerts configured
☑ Tracing available where needed
☑ Backup configured
☑ Restore tested
☑ Disaster recovery documented
☑ RPO defined
☑ RTO defined
☑ Upgrade plan documented
☑ Rollback plan tested
☑ Capacity reviewed
☑ Autoscaling configured where required
☑ Cost reviewed
☑ Runbooks available
☑ Ownership defined
☑ On-call configured
☑ Security review completed
```

---

# Common Mistakes

## 1. Running Critical Applications With One Replica

This creates a single point of failure.

---

## 2. No Resource Requests

Scheduling and capacity planning become unreliable.

---

## 3. Arbitrary Resource Limits

Incorrect limits can cause unnecessary:

```text
OOMKilled
CPU Throttling
```

---

## 4. Incorrect Probes

Bad probes can cause:

```text
Restart Loops
Traffic Loss
Deployment Failures
```

---

## 5. No Pod Disruption Budget

Maintenance can cause unnecessary downtime.

---

## 6. All Replicas on One Node

A node failure can take down the entire application.

---

## 7. Using `latest`

Mutable tags make deployments less deterministic.

---

## 8. Running Containers as Root

This increases the potential impact of application compromise.

---

## 9. Excessive RBAC

Avoid unnecessary:

```text
cluster-admin
```

access.

---

## 10. No Network Policies

A compromised Pod may have excessive network reachability.

---

## 11. No Centralized Logging

Local logs can disappear when Pods or nodes are replaced.

---

## 12. No Monitoring

You cannot reliably operate what you cannot observe.

---

## 13. No Tested Backups

Untested backups create false confidence.

---

## 14. No Rollback Plan

Every production deployment should have a recovery strategy.

---

## 15. Manual Production Changes

Manual changes are difficult to:

```text
Review
Repeat
Audit
Rollback
```

---

## 16. No Capacity Headroom

Clusters operating near maximum capacity are vulnerable to:

```text
Traffic Spikes
Node Failures
Scheduling Failures
```

---

## 17. Ignoring Dependencies

Application health may depend on:

```text
Database
Cache
Queue
External API
```

---

## 18. Over-Automating Destructive Actions

Automation should be safe, tested, and appropriately controlled.

---

# Best Practices

### 1. Design for Failure

Assume:

```text
Pods Fail
Nodes Fail
Zones Fail
Dependencies Fail
```

---

### 2. Use Least Privilege

Apply it to:

```text
Users
ServiceAccounts
Containers
Networks
```

---

### 3. Automate Deployments

Use:

```text
CI/CD
GitOps
Infrastructure as Code
```

---

### 4. Monitor Everything Important

At minimum:

```text
Logs
Metrics
Alerts
```

Add tracing where distributed request visibility is needed.

---

### 5. Test Recovery

Regularly test:

```text
Restore
Failover
Rollback
Disaster Recovery
```

---

### 6. Keep Images Minimal

Reduce:

```text
Attack Surface
Image Size
Unnecessary Packages
```

---

### 7. Make Deployments Reversible

Always know:

```text
What Changed?
How To Roll Back?
```

---

### 8. Define SLOs

Reliability should be measurable.

---

### 9. Maintain Capacity Headroom

Plan for:

```text
Growth
Failures
Spikes
Maintenance
```

---

### 10. Document Operational Knowledge

Runbooks reduce dependence on individual engineers.

---

# Hands-on Lab 1 – Production-Ready Deployment

Create a Deployment with:

```text
3 Replicas
Resource Requests
Resource Limits
Readiness Probe
Liveness Probe
Startup Probe
SecurityContext
Rolling Update
```

Validate:

```bash
kubectl get deployment
kubectl rollout status deployment/<name>
```

---

# Hands-on Lab 2 – High Availability

Deploy multiple replicas across nodes.

Use:

```text
Pod Anti-Affinity
```

or:

```text
Topology Spread Constraints
```

Verify placement:

```bash
kubectl get pods -o wide
```

---

# Hands-on Lab 3 – Resource Management

Configure:

```text
Requests
Limits
ResourceQuota
LimitRange
```

Observe scheduling behavior.

---

# Hands-on Lab 4 – Pod Disruption Budget

Create a PDB.

Simulate controlled node maintenance.

Observe how Kubernetes protects available replicas.

---

# Hands-on Lab 5 – Health Probes

Create an application with:

```text
Startup
Readiness
Liveness
```

Simulate:

```text
Slow Startup
Temporary Failure
Permanent Failure
```

Observe Kubernetes behavior.

---

# Hands-on Lab 6 – Rolling Deployment

Deploy:

```text
v1
```

Then update to:

```text
v2
```

Observe:

```bash
kubectl rollout status deployment/<name>
```

---

# Hands-on Lab 7 – Rollback

Deploy a broken version.

Observe the failure.

Rollback:

```bash
kubectl rollout undo deployment/<name>
```

Verify:

```bash
kubectl rollout status deployment/<name>
```

---

# Hands-on Lab 8 – Network Security

Create:

```text
Frontend
Backend
Database
```

Implement NetworkPolicies allowing only:

```text
Frontend → Backend
Backend → Database
```

---

# Hands-on Lab 9 – RBAC Hardening

Create a dedicated ServiceAccount.

Grant only the required permissions.

Verify:

```text
Allowed Actions
Denied Actions
```

---

# Hands-on Lab 10 – Container Hardening

Configure:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
  readOnlyRootFilesystem: true
  seccompProfile:
    type: RuntimeDefault
```

Test the application and adjust only where required.

---

# Hands-on Lab 11 – Admission Policy

Implement a policy that rejects:

```text
Privileged Containers
```

Test:

```text
Compliant Deployment
Non-Compliant Deployment
```

---

# Hands-on Lab 12 – Monitoring

Deploy a monitoring stack.

Create dashboards for:

```text
CPU
Memory
Pod Restarts
Node Health
Request Rate
Error Rate
Latency
```

---

# Hands-on Lab 13 – Logging

Create centralized application logging.

Verify that logs remain available even after a Pod is replaced.

---

# Hands-on Lab 14 – Autoscaling

Configure an HPA.

Generate controlled load.

Observe:

```text
Replica Count
CPU
Memory
```

---

# Hands-on Lab 15 – Backup and Restore

Create application data.

Perform a backup.

Delete the test environment.

Restore.

Verify application functionality.

---

# Hands-on Lab 16 – Disaster Recovery

Simulate a cluster failure scenario.

Execute:

```text
Recovery Plan
 ↓
Restore
 ↓
Validate
 ↓
Measure RTO
```

---

# Hands-on Lab 17 – Capacity Planning

Generate increasing workload.

Measure:

```text
CPU
Memory
Pod Count
Node Count
Latency
```

Determine when scaling is required.

---

# Hands-on Lab 18 – Cost Optimization

Identify:

```text
Idle Pods
Over-Provisioned Requests
Unused Storage
Unused Nodes
```

Optimize without violating reliability requirements.

---

# Hands-on Lab 19 – Production Incident

Simulate:

```text
API Failure
 ↓
Pods Restart
 ↓
Traffic Drops
```

Use:

```text
Logs
Metrics
Events
Probes
```

to identify the root cause.

---

# Hands-on Lab 20 – Complete Production Readiness Exercise

Build a production-style application with:

```text
High Availability
Resource Management
Health Checks
SecurityContext
RBAC
NetworkPolicies
Image Security
Admission Policy
Monitoring
Logging
Alerting
Backup
Autoscaling
CI/CD
Rollback
Runbooks
```

Perform a complete production readiness review.

---

# Quick Revision

## Production Readiness

```text
Security
+
Reliability
+
Observability
+
Scalability
+
Recoverability
```

---

## Resource Requests

```text
Resources needed for scheduling
```

---

## Resource Limits

```text
Maximum configured resource consumption
```

---

## PDB

```text
Protects availability during voluntary disruptions
```

---

## Readiness Probe

```text
Determines whether a Pod should receive traffic
```

---

## Liveness Probe

```text
Helps determine whether a container needs restarting
```

---

## Startup Probe

```text
Protects slow-starting applications from premature liveness failures
```

---

## HPA

```text
Scales Pod replicas
```

---

## VPA

```text
Adjusts workload resource sizing according to observed usage and configuration
```

---

## Cluster Autoscaler

```text
Adjusts node capacity according to scheduling demand
```

---

## RPO

```text
Maximum acceptable data loss
```

---

## RTO

```text
Target recovery time
```

---

## SLI

```text
Measured reliability indicator
```

---

## SLO

```text
Target reliability level
```

---

## SLA

```text
Service commitment, often contractual
```

---

# Essential Commands

Check cluster:

```bash
kubectl cluster-info
```

Check nodes:

```bash
kubectl get nodes
```

Node details:

```bash
kubectl describe node <node>
```

Check Pods:

```bash
kubectl get pods -A -o wide
```

Deployment:

```bash
kubectl get deployments -A
```

Deployment details:

```bash
kubectl describe deployment <deployment>
```

Rollout status:

```bash
kubectl rollout status deployment/<deployment>
```

Rollout history:

```bash
kubectl rollout history deployment/<deployment>
```

Rollback:

```bash
kubectl rollout undo deployment/<deployment>
```

Check events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Check resources:

```bash
kubectl top nodes
```

```bash
kubectl top pods -A
```

Check HPA:

```bash
kubectl get hpa -A
```

Check PDB:

```bash
kubectl get pdb -A
```

Check ResourceQuota:

```bash
kubectl get resourcequota -A
```

Check LimitRange:

```bash
kubectl get limitrange -A
```

Check NetworkPolicies:

```bash
kubectl get networkpolicy -A
```

Check ServiceAccounts:

```bash
kubectl get serviceaccounts -A
```

Check RBAC:

```bash
kubectl get roles,rolebindings -A
```

Check Cluster RBAC:

```bash
kubectl get clusterroles,clusterrolebindings
```

Cordon node:

```bash
kubectl cordon <node>
```

Drain node:

```bash
kubectl drain <node>
```

Uncordon node:

```bash
kubectl uncordon <node>
```

Check Pod logs:

```bash
kubectl logs <pod>
```

Previous container logs:

```bash
kubectl logs <pod> --previous
```

Pod details:

```bash
kubectl describe pod <pod>
```

Pod YAML:

```bash
kubectl get pod <pod> -o yaml
```

---

# Interview Questions

## Basic

- What makes a Kubernetes cluster production-ready?
- Why are resource requests important?
- What are resource limits?
- What are Kubernetes QoS classes?
- What is a PodDisruptionBudget?
- What is a readiness probe?
- What is a liveness probe?
- What is a startup probe?
- What is graceful shutdown?
- What is a rolling update?
- What is blue-green deployment?
- What is canary deployment?
- What is HPA?
- What is VPA?
- What is Cluster Autoscaler?
- What are SLI, SLO, and SLA?
- What are RPO and RTO?

---

## Intermediate

- How would you design a highly available Kubernetes application?
- How do you distribute Pods across availability zones?
- How do topology spread constraints work?
- How do you prevent a single namespace from consuming all cluster resources?
- How do you secure production Pods?
- How do you implement least-privilege RBAC?
- How do you secure container images?
- How do you design Kubernetes network security?
- How do you implement centralized logging?
- How do you design Kubernetes monitoring?
- How do you perform a safe Kubernetes upgrade?
- How do you implement rollback?
- How do you design backup and disaster recovery?
- How do you optimize Kubernetes costs?

---

## Advanced

- Design a production Kubernetes architecture for a highly available application.
- How would you design Kubernetes across multiple availability zones?
- How would you design a multi-region Kubernetes architecture?
- How would you handle a complete node failure?
- How would you handle an availability-zone failure?
- How would you design zero-downtime deployments?
- How would you combine HPA, VPA, and Cluster Autoscaler?
- How would you design production-grade observability?
- How would you design Kubernetes disaster recovery?
- How would you secure a production cluster against container escape?
- How would you design Kubernetes for a regulated environment?
- How would you reduce Kubernetes costs without reducing reliability?
- How would you design a complete production readiness review?

---

# Interview Scenario 1

### Question

> How would you make a Kubernetes application highly available?

### Answer

I would use:

```text
Multiple Replicas
+
Multiple Nodes
+
Multiple Availability Zones
+
Pod Anti-Affinity / Topology Spread
+
Readiness Probes
+
PDB
+
Load Balancing
+
Autoscaling
```

I would also ensure that dependencies such as databases and caches have appropriate availability characteristics.

---

# Interview Scenario 2

### Question

> What happens if all replicas of an application are scheduled on one node?

### Answer

A node failure can remove all application replicas simultaneously.

I would use:

```text
Pod Anti-Affinity
```

or:

```text
Topology Spread Constraints
```

to distribute replicas across nodes and, where appropriate, availability zones.

---

# Interview Scenario 3

### Question

> How do you perform zero-downtime deployment?

### Answer

Use:

```text
Multiple Replicas
+
Readiness Probe
+
Rolling Update
+
PDB
+
Graceful Shutdown
```

For higher-risk changes, use:

```text
Canary
```

or:

```text
Blue-Green
```

---

# Interview Scenario 4

### Question

> Why should you not use the same ServiceAccount for every application?

### Answer

Because compromise of one application could provide unnecessary permissions to other workloads.

Instead:

```text
Application A
 ↓
ServiceAccount A

Application B
 ↓
ServiceAccount B
```

Each receives only the permissions it requires.

---

# Interview Scenario 5

### Question

> How would you secure a production container?

### Answer

I would use:

```text
Non-Root
+
Read-Only Filesystem
+
Drop Capabilities
+
No Privilege Escalation
+
seccomp
+
Minimal Image
+
Image Scanning
+
Resource Limits
+
NetworkPolicy
```

I would add only the privileges and capabilities genuinely required by the application.

---

# Interview Scenario 6

### Question

> How would you handle a Kubernetes node maintenance operation?

### Answer

I would:

```text
Review Workloads
 ↓
Check PDB
 ↓
Cordon Node
 ↓
Drain Safely
 ↓
Perform Maintenance
 ↓
Validate Node
 ↓
Uncordon
 ↓
Monitor Workloads
```

I would verify that the maintenance does not violate availability requirements.

---

# Interview Scenario 7

### Question

> How do you prepare Kubernetes for disaster recovery?

### Answer

Define:

```text
RPO
RTO
```

Then implement:

```text
Backups
+
Secure Storage
+
Recovery Procedures
+
Dependency Recovery
+
Regular Restore Testing
```

The recovery process should be tested rather than assumed to work.

---

# Interview Scenario 8

### Question

> How do you prevent one application from consuming all cluster resources?

### Answer

Use:

```text
Resource Requests
+
Resource Limits
+
ResourceQuota
+
LimitRange
+
Autoscaling
+
Capacity Planning
```

This provides workload-level and namespace-level resource governance.

---

# Interview Scenario 9

### Question

> How would you troubleshoot CrashLoopBackOff in production?

### Answer

I would inspect:

```bash
kubectl get pod <pod>
kubectl describe pod <pod>
kubectl logs <pod>
kubectl logs <pod> --previous
```

Then investigate:

```text
Application Error
Configuration
Secrets
Dependencies
Resources
Probes
Recent Deployment
```

I would avoid restarting repeatedly without identifying the underlying cause.

---

# Interview Scenario 10

### Question

> Design a complete production Kubernetes platform.

### Answer

A high-level architecture:

```text
                         Users
                           │
                           ▼
                          DNS
                           │
                           ▼
                    Load Balancer
                           │
                           ▼
                    Gateway / Ingress
                           │
                           ▼
                     Kubernetes
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
    Application A      Application B      Application C
        │                  │                  │
        ▼                  ▼                  ▼
    Services           Services           Services
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                    Data / Dependencies

Supporting Platform:
──────────────────────────────────────────────
RBAC          NetworkPolicy       Pod Security
Images        Admission           Runtime Security
Logging       Metrics             Tracing
Alerts        Backup              DR
CI/CD         GitOps              IaC
Autoscaling   Capacity            Cost Management
```

The platform should additionally have:

```text
High Availability
+
Multi-Zone Distribution
+
Secure Defaults
+
Automated Deployments
+
Continuous Compliance
+
Incident Response
+
Operational Runbooks
```

---

# Production Operations Checklist

```text
☑ Architecture documented
☑ Dependencies documented
☑ Ownership defined
☑ Multiple replicas configured
☑ Failure domains considered
☑ Resource requests configured
☑ Resource limits reviewed
☑ ResourceQuota configured
☑ LimitRange configured where useful
☑ PDB reviewed
☑ Topology distribution configured
☑ Health probes configured
☑ Graceful shutdown implemented
☑ Rolling deployment configured
☑ Rollback tested
☑ Image security implemented
☑ Containers hardened
☑ RBAC least privilege
☑ ServiceAccounts separated
☑ NetworkPolicies implemented
☑ Secrets protected
☑ Admission controls enabled
☑ Runtime detection enabled
☑ Audit logging enabled
☑ Centralized logging enabled
☑ Metrics enabled
☑ Alerting configured
☑ Tracing implemented where required
☑ Backup configured
☑ Restore tested
☑ Disaster recovery tested
☑ RPO defined
☑ RTO defined
☑ Upgrade strategy documented
☑ Maintenance procedure documented
☑ Capacity planning performed
☑ Autoscaling configured
☑ Cost reviewed
☑ Runbooks created
☑ On-call process defined
☑ Incident response tested
☑ Compliance requirements mapped
☑ Security review completed
```

---

# Chapter Summary

Production Kubernetes is not simply about keeping Pods running.

A production platform must provide:

```text
Availability
+
Security
+
Observability
+
Scalability
+
Recoverability
+
Operational Control
```

The most important production practices are:

```text
Use Multiple Replicas
+
Distribute Across Failure Domains
+
Define Resource Requests
+
Use Appropriate Limits
+
Configure Health Probes
+
Use PDBs
+
Implement Least Privilege
+
Secure Images
+
Use Network Policies
+
Centralize Logs
+
Monitor Metrics
+
Configure Alerts
+
Automate Deployments
+
Test Rollbacks
+
Back Up Data
+
Test Recovery
+
Plan Capacity
+
Monitor Costs
```

Production reliability is achieved through engineering discipline rather than a single Kubernetes feature.

The most important principle is:

> **Design Kubernetes workloads and infrastructure to expect failure, enforce secure defaults, automate repeatable operations, continuously observe system health, and regularly test deployment, rollback, backup, and recovery procedures.**

---

## Next Chapter

# Chapter 78 – GitOps

Topics will include:

- GitOps Fundamentals
- What Is GitOps?
- GitOps Principles
- Git as the Source of Truth
- Declarative Infrastructure
- Desired State
- Actual State
- Reconciliation
- Continuous Delivery
- GitOps vs Traditional CI/CD
- GitOps Architecture
- GitOps Workflow
- Kubernetes and GitOps
- Git Repository Structure
- Environment Management
- Development
- Staging
- Production
- Configuration Management
- Secrets with GitOps
- Sealed Secrets
- External Secrets
- Helm with GitOps
- Kustomize with GitOps
- Argo CD
- Flux
- Argo CD Architecture
- Flux Architecture
- Applications
- ApplicationSets
- Sync
- Auto-Sync
- Manual Sync
- Health Status
- Drift Detection
- Self-Healing
- Rollback
- Progressive Delivery
- Canary Deployments
- Blue-Green Deployments
- GitOps Security
- RBAC
- Repository Security
- Commit Signing
- Image Verification
- Supply Chain Security
- Policy as Code
- CI Integration
- Pull Requests
- Change Management
- Auditability
- Compliance
- Multi-Cluster GitOps
- Multi-Environment GitOps
- Monorepo vs Multi-Repo
- Branching Strategies
- Repository Layout
- Deployment Promotion
- Disaster Recovery
- GitOps Observability
- Notifications
- Troubleshooting
- Production Best Practices
- Common Mistakes
- Hands-on Labs
- Quick Revision
- Interview Questions
- References

---