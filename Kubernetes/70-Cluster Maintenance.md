# Chapter 70 – Cluster Maintenance

## Overview

Kubernetes cluster maintenance is the collection of planned and controlled activities required to keep a cluster:

```text
Healthy
Secure
Stable
Performant
Supported
Available
```

Maintenance includes:

```text
Node Maintenance
Control Plane Maintenance
OS Updates
Kernel Updates
Container Runtime Updates
kubelet Updates
Certificate Management
Storage Maintenance
Network Maintenance
CNI Maintenance
CSI Maintenance
Resource Cleanup
Capacity Management
Monitoring
Security
```

A safe maintenance workflow is:

```text
Plan
  ↓
Backup
  ↓
Health Check
  ↓
Cordon
  ↓
Drain
  ↓
Maintain
  ↓
Validate
  ↓
Uncordon
  ↓
Monitor
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Cluster maintenance fundamentals
- Maintenance planning
- Maintenance windows
- Change management
- Cluster health checks
- Node maintenance
- Control-plane maintenance
- Worker-node maintenance
- Cordon
- Drain
- Uncordon
- Pod eviction
- Pod Disruption Budgets
- Node replacement
- Node reboot
- Operating-system updates
- Kernel updates
- Container-runtime updates
- kubelet maintenance
- Kubernetes component maintenance
- CNI maintenance
- CSI maintenance
- CoreDNS maintenance
- Ingress maintenance
- Gateway maintenance
- Certificate maintenance
- etcd maintenance
- etcd defragmentation
- Disk maintenance
- Storage maintenance
- Network maintenance
- Capacity management
- Resource cleanup
- Image cleanup
- Unused-resource cleanup
- Namespace cleanup
- Stale resources
- Failed Pods
- Completed Jobs
- Old ReplicaSets
- Orphaned resources
- Monitoring during maintenance
- Logging during maintenance
- Security during maintenance
- Backup before maintenance
- Maintenance automation
- Rolling maintenance
- Zero-downtime maintenance
- Planned maintenance
- Emergency maintenance
- Maintenance runbooks
- Maintenance validation
- Post-maintenance checks
- Troubleshooting
- Production maintenance strategy
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is Cluster Maintenance?

Cluster maintenance means performing operational tasks that keep Kubernetes infrastructure and workloads functioning correctly.

Examples:

```text
Upgrade OS
Restart Node
Replace Hardware
Update kubelet
Update Container Runtime
Repair Storage
Update CNI
Renew Certificates
Clean Resources
```

---

# Why Is Maintenance Important?

Without regular maintenance, a cluster may experience:

```text
Security Vulnerabilities
Disk Exhaustion
Certificate Expiration
Performance Degradation
Unsupported Components
Resource Waste
Unexpected Failures
```

---

# Planned vs Emergency Maintenance

## Planned Maintenance

Examples:

```text
OS Updates
Kernel Updates
Node Replacement
Kubernetes Upgrade
CNI Upgrade
Certificate Rotation
```

These should be scheduled.

---

## Emergency Maintenance

Examples:

```text
Critical Security Vulnerability
Disk Failure
Compromised Node
Network Failure
Hardware Failure
```

Emergency maintenance requires faster response.

---

# Maintenance Window

A maintenance window defines:

```text
Start Time
End Time
Scope
Owner
Expected Impact
Validation
Recovery Plan
```

Example:

```text
Maintenance:
01:00–03:00

Scope:
Worker Nodes

Impact:
Potential Pod Evictions
```

---

# Change Management

Production maintenance should follow a controlled change process.

Typical flow:

```text
Request
 ↓
Risk Assessment
 ↓
Approval
 ↓
Maintenance
 ↓
Validation
 ↓
Documentation
```

---

# Maintenance Risk Assessment

Before maintenance ask:

```text
What can fail?
What is the blast radius?
How much capacity remains?
Can workloads tolerate disruption?
Is backup available?
How do we recover?
```

---

# Maintenance Checklist

Before starting:

```text
☑ Cluster healthy
☑ Nodes Ready
☑ Applications healthy
☑ Backup verified
☑ Capacity available
☑ PDBs reviewed
☑ Maintenance window approved
☑ Monitoring active
☑ Recovery plan ready
☑ Dependencies identified
```

---

# Cluster Health Check

Start with:

```bash
kubectl get nodes
```

Expected:

```text
STATUS = Ready
```

---

# Check All Pods

```bash
kubectl get pods -A
```

Look for:

```text
CrashLoopBackOff
Pending
Error
ImagePullBackOff
Unknown
```

---

# Check Events

```bash
kubectl get events -A
```

Events can reveal:

```text
Scheduling Failures
Mount Errors
Network Problems
Probe Failures
Eviction
```

---

# Check Resources

If Metrics Server is available:

```bash
kubectl top nodes
```

and:

```bash
kubectl top pods -A
```

---

# Check Persistent Volumes

```bash
kubectl get pv
```

Check PVCs:

```bash
kubectl get pvc -A
```

---

# Check Services

```bash
kubectl get svc -A
```

---

# Check Ingress

```bash
kubectl get ingress -A
```

---

# Check Gateway API

If installed:

```bash
kubectl get gateway -A
```

---

# Check PDBs

```bash
kubectl get pdb -A
```

---

# Check Nodes Before Maintenance

```bash
kubectl get nodes -o wide
```

Record:

```text
Node Name
Status
Version
Internal IP
OS
Kernel
Container Runtime
```

---

# Node Maintenance

Node maintenance commonly follows:

```text
Cordon
 ↓
Drain
 ↓
Perform Maintenance
 ↓
Reboot
 ↓
Validate
 ↓
Uncordon
```

---

# Cordon

Cordon prevents new Pods from being scheduled on the node.

```bash
kubectl cordon <node>
```

Existing Pods continue running unless another operation affects them.

---

# Verify Cordon

```bash
kubectl get nodes
```

The node should show:

```text
SchedulingDisabled
```

---

# Drain

Drain prepares a node for maintenance by evicting or removing eligible workloads.

Example:

```bash
kubectl drain <node> \
  --ignore-daemonsets
```

The exact flags should be chosen based on the workloads on the node.

---

# Why Drain?

Without draining:

```text
Node
 ↓
Maintenance / Reboot
 ↓
Running Pods
 ↓
Service Disruption
```

With controlled draining:

```text
Node
 ↓
Pods Evicted
 ↓
Pods Rescheduled
 ↓
Maintenance
```

---

# Pod Eviction

Kubernetes uses eviction mechanisms to move workloads away from a node during voluntary maintenance.

PDBs can limit voluntary disruption.

---

# Pod Disruption Budget

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

# PDB and Drain

Suppose:

```text
3 replicas
minAvailable = 2
```

The system should avoid voluntarily disrupting too many replicas simultaneously.

However:

```text
PDB ≠ Guaranteed Availability
```

A PDB does not prevent unexpected node failures.

---

# Check Workloads Before Drain

Identify Pods:

```bash
kubectl get pods -A -o wide
```

Determine:

```text
Which Pods run on the node?
Which are replicated?
Which are Stateful?
Which are DaemonSets?
Which have PDBs?
```

---

# DaemonSets

DaemonSet Pods are managed differently during drain.

For example:

```text
CNI
Logging Agent
Security Agent
```

may run as DaemonSets.

The `--ignore-daemonsets` option is commonly required when draining such nodes.

---

# Static Pods

Control-plane components may be deployed as static Pods depending on cluster architecture.

These are not handled like normal Deployment Pods.

---

# Node Reboot

A controlled reboot can follow:

```text
Cordon
 ↓
Drain
 ↓
Reboot
 ↓
Check Node
 ↓
Check kubelet
 ↓
Check Runtime
 ↓
Check CNI
 ↓
Uncordon
```

---

# Verify Node After Reboot

```bash
kubectl get node <node>
```

Expected:

```text
Ready
```

---

# Verify kubelet

On the node:

```bash
systemctl status kubelet
```

---

# Restart kubelet

If required:

```bash
sudo systemctl restart kubelet
```

---

# Check kubelet Logs

```bash
journalctl -u kubelet
```

For recent logs:

```bash
journalctl -u kubelet -n 100
```

---

# Container Runtime Maintenance

Kubernetes nodes use a container runtime.

Common runtime:

```text
containerd
```

Maintenance may include:

```text
Version Updates
Configuration
Restart
Troubleshooting
```

---

# Check Container Runtime

```bash
kubectl get nodes -o wide
```

For node-level details:

```bash
kubectl describe node <node>
```

---

# Container Runtime Restart

A runtime restart can affect workloads on that node.

Therefore:

```text
Drain
 ↓
Restart Runtime
 ↓
Validate
```

is safer than restarting it blindly on a busy production node.

---

# Operating System Updates

Node operating systems require regular updates.

Examples:

```text
Security Patches
Kernel Updates
Package Updates
Runtime Libraries
```

---

# Kernel Updates

Kernel updates may require a reboot.

Workflow:

```text
Cordon
 ↓
Drain
 ↓
Kernel Update
 ↓
Reboot
 ↓
Validate
 ↓
Uncordon
```

---

# OS Patch Management

Use:

```text
Automation
Configuration Management
Golden Images
Managed Node Pools
```

where appropriate.

---

# Immutable Node Strategy

Some organizations replace nodes rather than modifying them in place.

Example:

```text
Old Node
   ↓
Drain
   ↓
Delete

New Node
   ↓
Join Cluster
```

This can provide consistent environments.

---

# Node Replacement

Typical workflow:

```text
Create New Node
      ↓
Validate
      ↓
Cordon Old Node
      ↓
Drain Old Node
      ↓
Remove Old Node
```

---

# Why Replace Nodes?

Benefits:

```text
Consistency
Reduced Configuration Drift
Repeatability
Automation
Simpler Rollback
```

---

# Node Labels

Before replacing nodes, preserve required labels.

Check:

```bash
kubectl get nodes --show-labels
```

Important labels may control:

```text
Scheduling
Affinity
Topology
Workload Placement
```

---

# Node Taints

Check:

```bash
kubectl describe node <node>
```

Review:

```text
Taints
```

When replacing nodes, ensure required taints are recreated.

---

# Node Maintenance and Affinity

Node affinity may require Pods to run on specific nodes or labels.

Before draining:

```text
Check Node Affinity
Check Pod Affinity
Check Anti-Affinity
```

---

# Node Maintenance and Topology

Topology constraints can affect rescheduling.

Example:

```text
Zone A
Zone B
Zone C
```

A Pod may not be allowed to move if topology constraints cannot be satisfied.

---

# Capacity During Maintenance

Suppose:

```text
5 Nodes
```

and one node is drained.

Remaining:

```text
4 Nodes
```

Can they handle all workloads?

Check:

```text
CPU
Memory
Pod Count
Storage
```

---

# N+1 Capacity

A production cluster should often have enough spare capacity to tolerate at least one expected node failure.

Example:

```text
Required Capacity = 3 Nodes
Provisioned = 4 Nodes
```

This is one form of N+1 planning.

---

# Resource Requests

Scheduling depends heavily on resource requests.

Example:

```yaml
resources:

  requests:
    cpu: "500m"
    memory: "512Mi"
```

---

# Resource Limits

Example:

```yaml
resources:

  limits:
    cpu: "1"
    memory: "1Gi"
```

Poorly configured requests can make maintenance and rescheduling harder.

---

# Disk Maintenance

Node disk pressure can cause problems.

Check:

```bash
df -h
```

and:

```bash
df -i
```

Monitor:

```text
Disk Usage
Inodes
Container Logs
Image Storage
Temporary Files
```

---

# Disk Pressure

Kubernetes can report:

```text
DiskPressure
```

when node storage becomes constrained.

Check:

```bash
kubectl describe node <node>
```

---

# Image Cleanup

Unused container images can consume disk.

Container-runtime-specific cleanup should be performed carefully.

Avoid deleting images blindly on active production nodes.

---

# Container Logs

Large container logs can consume disk.

Use:

```text
Log Rotation
Centralized Logging
Retention Policies
```

---

# Resource Cleanup

Regularly review:

```text
Completed Jobs
Failed Jobs
Unused ConfigMaps
Unused Secrets
Old ReplicaSets
Unused PVCs
Unused Namespaces
```

Be careful with automated deletion.

---

# Completed Jobs

List:

```bash
kubectl get jobs -A
```

Old completed Jobs can accumulate.

Use controlled retention policies or cleanup automation.

---

# CronJobs

Review:

```bash
kubectl get cronjobs -A
```

Ensure:

```text
History Limits
Schedule
Concurrency Policy
```

are appropriate.

---

# Old ReplicaSets

Deployments can leave historical ReplicaSets.

Check:

```bash
kubectl get rs -A
```

Deployment history limits can control retained revisions.

---

# Namespace Cleanup

List:

```bash
kubectl get namespaces
```

Review unused namespaces before removing them.

Never delete production namespaces without explicit verification.

---

# Orphaned Resources

Examples:

```text
Unused Load Balancer
Unused PVC
Unused Service
Unused CRD
Unused ConfigMap
```

Identify dependencies before deleting.

---

# Certificate Maintenance

Kubernetes environments depend on certificates for:

```text
API Server
kubelet
etcd
Admission Webhooks
Ingress
Service Mesh
```

---

# Certificate Expiration

Expired certificates can cause:

```text
API Failures
Node Failures
Webhook Failures
TLS Errors
```

---

# Check Certificates

For kubeadm clusters:

```bash
kubeadm certs check-expiration
```

The exact command depends on the Kubernetes distribution.

---

# Certificate Rotation

Certificate rotation should be:

```text
Planned
Monitored
Tested
Documented
```

---

# etcd Maintenance

etcd maintenance can include:

```text
Health Checks
Backup
Defragmentation
Disk Monitoring
Certificate Management
Member Management
```

---

# etcd Backup

Before high-risk control-plane maintenance:

```bash
etcdctl snapshot save snapshot.db
```

Store the snapshot securely outside the active etcd environment.

---

# etcd Defragmentation

etcd databases can accumulate fragmented storage.

Defragmentation can reclaim space.

It must be performed carefully and according to the cluster's operational requirements.

---

# etcd Disk Monitoring

Monitor:

```text
Disk Space
Latency
IOPS
Database Size
Defragmentation
```

---

# Network Maintenance

Network maintenance can involve:

```text
CNI
Routes
Firewall
Load Balancer
DNS
Network Policies
```

---

# CNI Maintenance

Before changing a CNI:

```text
Check Version
Check Compatibility
Backup Configuration
Test in Staging
Plan Rollback
```

Networking changes have high blast radius.

---

# CoreDNS Maintenance

Check:

```bash
kubectl get pods -n kube-system
```

Look for CoreDNS Pods.

---

# CoreDNS Health

DNS failures can affect:

```text
Service Discovery
External Name Resolution
Application Connectivity
```

---

# Ingress Maintenance

Check:

```bash
kubectl get ingress -A
```

Also review:

```text
Ingress Controller
TLS
Load Balancer
Annotations
Controller Logs
```

---

# Gateway Maintenance

If Gateway API is used, verify:

```text
GatewayClass
Gateway
Routes
Controller
Load Balancer
```

---

# Storage Maintenance

Review:

```text
PV
PVC
StorageClass
CSI
VolumeSnapshots
Storage Backend
```

Commands:

```bash
kubectl get pv
kubectl get pvc -A
kubectl get storageclass
```

---

# CSI Maintenance

Before upgrading or changing CSI components:

```text
Check Driver Compatibility
Check Existing Volumes
Check Snapshots
Check Attachments
Check Recovery
```

---

# Storage Maintenance Risk

Storage failures can affect:

```text
Databases
StatefulSets
Persistent Applications
```

Always validate storage after maintenance.

---

# Control Plane Maintenance

Control-plane maintenance may involve:

```text
API Server
Scheduler
Controller Manager
etcd
Cloud Controller Manager
Certificates
Operating System
```

Use the Kubernetes distribution's official maintenance procedure.

---

# API Server Maintenance

Multiple API Servers can reduce disruption.

Before maintenance:

```text
Verify Other API Servers Healthy
```

---

# Scheduler Maintenance

Leader election allows another scheduler instance to take over in HA configurations.

---

# Controller Manager Maintenance

Similarly, leader election can provide redundancy.

---

# etcd Maintenance Risk

etcd is highly sensitive to quorum loss.

Never casually stop enough etcd members to lose quorum.

---

# Maintenance and Monitoring

Monitoring should remain active throughout maintenance.

Watch:

```text
Node Status
Pod Status
API Errors
Application Errors
Latency
Resource Usage
```

---

# Maintenance and Logging

Logs should remain available during maintenance.

Monitor:

```text
Application Logs
Node Logs
kubelet Logs
Control Plane Logs
CNI Logs
CSI Logs
```

---

# Maintenance and Security

Never treat maintenance as a reason to disable security controls unnecessarily.

Maintain:

```text
RBAC
TLS
Network Policies
Pod Security
Audit Logging
```

---

# Backup Before Maintenance

High-risk maintenance should have a recovery mechanism.

Examples:

```text
etcd Snapshot
Database Backup
Volume Snapshot
Configuration Backup
```

---

# Rolling Maintenance

Rolling maintenance updates infrastructure gradually.

Example:

```text
Node-1
 ↓
Validate

Node-2
 ↓
Validate

Node-3
 ↓
Validate
```

---

# Zero-Downtime Maintenance

The objective is:

```text
Maintenance
     ↓
No User-Visible Downtime
```

This requires:

```text
Multiple Replicas
+
Capacity
+
PDB
+
Readiness
+
Controlled Drain
```

---

# Maintenance Automation

Automation can reduce human error.

Possible tools:

```text
Ansible
Terraform
Cluster API
GitOps
Cloud Provider Automation
```

---

# Automated Node Maintenance

A typical automation flow:

```text
Select Node
 ↓
Cordon
 ↓
Drain
 ↓
Patch
 ↓
Reboot
 ↓
Validate
 ↓
Uncordon
 ↓
Continue
```

---

# Maintenance Guardrails

Automation should include:

```text
Health Check
Capacity Check
PDB Check
Approval
Timeout
Failure Detection
Rollback / Recovery
```

---

# Maintenance Runbook

A runbook should document:

```text
Purpose
Scope
Prerequisites
Commands
Expected Output
Validation
Failure Handling
Rollback / Recovery
Contacts
```

---

# Example Node Maintenance Runbook

```text
1. Verify Cluster Health
2. Check Node Workloads
3. Check PDBs
4. Check Capacity
5. Cordon Node
6. Drain Node
7. Perform Maintenance
8. Reboot if Required
9. Validate kubelet
10. Validate Runtime
11. Validate CNI
12. Validate Node
13. Uncordon
14. Validate Workloads
15. Monitor
```

---

# Emergency Maintenance

For urgent security issues:

```text
Identify Vulnerability
 ↓
Assess Exposure
 ↓
Determine Urgency
 ↓
Isolate if Necessary
 ↓
Patch
 ↓
Validate
 ↓
Monitor
```

---

# Emergency Node Isolation

If a node is compromised:

```bash
kubectl cordon <node>
```

Then carefully remove workloads according to the incident-response procedure.

Do not destroy forensic evidence without authorization and an established response plan.

---

# Maintenance Validation

After maintenance:

```text
Node Ready
Pods Healthy
DNS Healthy
Network Healthy
Storage Healthy
Ingress Healthy
Applications Healthy
Monitoring Healthy
```

---

# Node Validation

```bash
kubectl get node <node>
```

Check:

```text
Ready
Conditions
Taints
Labels
Capacity
Allocatable
```

---

# Pod Validation

```bash
kubectl get pods -A -o wide
```

Look for:

```text
CrashLoopBackOff
Pending
Error
```

---

# Application Validation

Test:

```text
Frontend
API
Database
Authentication
Background Jobs
External Integrations
```

---

# Post-Maintenance Monitoring

Monitor for an appropriate period:

```text
CPU
Memory
Restarts
Errors
Latency
Network
Storage
```

---

# Maintenance Documentation

Record:

```text
What Changed
When
Who
Why
Result
Problems
Recovery Actions
```

This creates an operational history.

---

# Maintenance Metrics

Useful metrics include:

```text
Maintenance Duration
Failed Maintenance Events
Node Recovery Time
Pod Eviction Time
Application Error Rate
Downtime
Change Failure Rate
```

---

# Change Failure Rate

A useful operational metric is:

```text
Failed Changes / Total Changes
```

Lower failure rates indicate better maintenance processes.

---

# Common Maintenance Mistakes

## 1. Draining Without Checking Capacity

This can leave Pods Pending.

---

## 2. Ignoring PDBs

Drain may block or cause unexpected disruption.

---

## 3. Restarting Nodes Without Draining

Can cause unnecessary application disruption.

---

## 4. Updating All Nodes at Once

This increases blast radius.

---

## 5. Ignoring Stateful Workloads

Databases require additional care.

---

## 6. Ignoring Certificates

Expired certificates can break cluster components.

---

## 7. No Backup

High-risk maintenance without recovery is dangerous.

---

## 8. Cleaning Resources Blindly

Deleting an apparently unused resource may break dependencies.

---

## 9. Ignoring Disk Pressure

Full disks can destabilize nodes.

---

## 10. No Post-Maintenance Validation

A node being Ready does not guarantee application health.

---

## 11. Ignoring CNI / CSI

Networking and storage are critical dependencies.

---

## 12. No Monitoring

Problems may remain unnoticed.

---

# Best Practices

### 1. Plan Maintenance

Define:

```text
Scope
Risk
Impact
Recovery
```

---

### 2. Backup First

For high-risk changes:

```text
Backup
+
Verify Recovery
```

---

### 3. Use Cordon and Drain

For planned node maintenance:

```text
Cordon
 ↓
Drain
 ↓
Maintain
```

---

### 4. Maintain Spare Capacity

Ensure workloads can move.

---

### 5. Use PDBs

Protect replicated workloads during voluntary disruption.

---

### 6. Maintain Multiple Replicas

Use:

```text
Deployment
+
Topology Distribution
```

for resilient workloads.

---

### 7. Automate Repetitive Work

Automation improves:

```text
Consistency
Repeatability
Safety
```

---

### 8. Monitor During Maintenance

Watch both:

```text
Infrastructure
+
Applications
```

---

### 9. Validate After Every Step

Do not wait until the end.

---

### 10. Document Everything

Maintain:

```text
Runbooks
Change Records
Recovery Procedures
```

---

# Hands-on Lab 1 – Basic Node Maintenance

Use a test cluster.

Perform:

```text
Check
 ↓
Cordon
 ↓
Drain
 ↓
Maintenance
 ↓
Uncordon
```

---

# Hands-on Lab 2 – Node Reboot

On a disposable cluster:

```text
Cordon
Drain
Reboot
Validate
Uncordon
```

Check application availability.

---

# Hands-on Lab 3 – PDB and Drain

Create:

```text
3 replicas
```

and:

```text
PDB
```

Drain one node.

Observe:

```text
Pod Eviction
Scheduling
Availability
```

---

# Hands-on Lab 4 – Capacity Testing

Create workloads that consume most available resources.

Drain one node.

Observe:

```text
Pending Pods
Scheduling Failures
Resource Pressure
```

---

# Hands-on Lab 5 – Node Replacement

Create a new node.

Then:

```text
Cordon Old Node
 ↓
Drain
 ↓
Remove
```

Verify workloads move successfully.

---

# Hands-on Lab 6 – Disk Monitoring

Check:

```bash
df -h
df -i
```

Create controlled disk pressure in a disposable environment.

Observe:

```text
DiskPressure
Eviction
```

---

# Hands-on Lab 7 – Resource Cleanup

Identify:

```text
Completed Jobs
Old ReplicaSets
Unused Resources
```

Clean them carefully.

---

# Hands-on Lab 8 – Certificate Maintenance

In a test kubeadm environment:

```bash
kubeadm certs check-expiration
```

Review certificate lifecycle and renewal procedures.

---

# Hands-on Lab 9 – etcd Backup

Create an etcd snapshot.

Verify:

```text
Backup Exists
Backup Size
Snapshot Integrity
Storage Location
```

---

# Hands-on Lab 10 – etcd Maintenance

In a disposable environment:

```text
Monitor Database Size
 ↓
Perform Defragmentation
 ↓
Validate
```

---

# Hands-on Lab 11 – CNI Maintenance

Upgrade or modify CNI components in a test environment.

Validate:

```text
Pod-to-Pod
Pod-to-Service
DNS
NetworkPolicy
```

---

# Hands-on Lab 12 – CSI Maintenance

Perform controlled CSI maintenance.

Test:

```text
PVC
Mount
Read
Write
Unmount
```

---

# Hands-on Lab 13 – CoreDNS Maintenance

Restart or update CoreDNS in a test cluster.

Verify:

```text
Service DNS
External DNS
```

---

# Hands-on Lab 14 – Ingress Maintenance

Perform controlled Ingress controller maintenance.

Verify:

```text
HTTP
HTTPS
TLS
Routing
```

---

# Hands-on Lab 15 – Gateway Maintenance

If Gateway API is available:

```text
Gateway
Routes
Controller
```

Perform maintenance and verify traffic.

---

# Hands-on Lab 16 – Rolling Node Maintenance

Use multiple worker nodes.

Perform:

```text
Node 1
 ↓
Node 2
 ↓
Node 3
```

with validation after every node.

---

# Hands-on Lab 17 – Automated Node Maintenance

Create an automation workflow:

```text
Select
 ↓
Cordon
 ↓
Drain
 ↓
Patch
 ↓
Reboot
 ↓
Validate
 ↓
Uncordon
```

Add failure handling.

---

# Hands-on Lab 18 – Maintenance Monitoring

Create a dashboard showing:

```text
Nodes
Pods
CPU
Memory
Restarts
API Errors
Application Errors
```

Run maintenance and observe the dashboard.

---

# Hands-on Lab 19 – Emergency Patch

Simulate a critical node vulnerability in a test environment.

Practice:

```text
Assess
 ↓
Isolate
 ↓
Patch
 ↓
Validate
 ↓
Monitor
```

---

# Hands-on Lab 20 – Full Maintenance Exercise

Design and execute:

```text
Health Check
 ↓
Backup
 ↓
Capacity Check
 ↓
PDB Review
 ↓
Cordon
 ↓
Drain
 ↓
Node Maintenance
 ↓
Reboot
 ↓
Validation
 ↓
Uncordon
 ↓
Application Testing
 ↓
Monitoring
```

Document:

```text
Duration
Issues
Downtime
Recovery
Lessons Learned
```

---

# Quick Revision

## Cordon

```text
Prevents new Pods from being scheduled on a node
```

---

## Drain

```text
Evicts/removes eligible workloads for maintenance
```

---

## Uncordon

```text
Allows scheduling on the node again
```

---

## PDB

```text
Limits voluntary disruption
```

---

## Node Replacement

```text
Replace an old node with a new node
```

---

## Disk Pressure

```text
Node condition caused by insufficient disk resources
```

---

## Cluster Maintenance

```text
Operational work required to keep Kubernetes healthy and supported
```

---

## Rolling Maintenance

```text
Maintain infrastructure gradually instead of all at once
```

---

## Planned Maintenance

```text
Scheduled operational change
```

---

## Emergency Maintenance

```text
Urgent change required to reduce immediate risk
```

---

## Maintenance Runbook

```text
Documented procedure for executing and validating maintenance
```

---

# Essential Commands

Check nodes:

```bash
kubectl get nodes
```

Check detailed node information:

```bash
kubectl describe node <node>
```

Check all Pods:

```bash
kubectl get pods -A
```

Check Pods on a node:

```bash
kubectl get pods -A -o wide \
  --field-selector spec.nodeName=<node>
```

Cordon:

```bash
kubectl cordon <node>
```

Drain:

```bash
kubectl drain <node> \
  --ignore-daemonsets
```

Uncordon:

```bash
kubectl uncordon <node>
```

Check PDB:

```bash
kubectl get pdb -A
```

Check PV:

```bash
kubectl get pv
```

Check PVC:

```bash
kubectl get pvc -A
```

Check StorageClasses:

```bash
kubectl get storageclass
```

Check Services:

```bash
kubectl get svc -A
```

Check Ingress:

```bash
kubectl get ingress -A
```

Check Gateway:

```bash
kubectl get gateway -A
```

Check Jobs:

```bash
kubectl get jobs -A
```

Check CronJobs:

```bash
kubectl get cronjobs -A
```

Check ReplicaSets:

```bash
kubectl get rs -A
```

Check resource usage:

```bash
kubectl top nodes
```

Check Pod resource usage:

```bash
kubectl top pods -A
```

Check events:

```bash
kubectl get events -A
```

Check kubelet:

```bash
systemctl status kubelet
```

Restart kubelet:

```bash
sudo systemctl restart kubelet
```

Check kubelet logs:

```bash
journalctl -u kubelet -n 100
```

Check disk:

```bash
df -h
```

Check inodes:

```bash
df -i
```

Check kubeadm certificates:

```bash
kubeadm certs check-expiration
```

---

# Interview Questions

## Basic

- What is Kubernetes cluster maintenance?
- Why is cluster maintenance important?
- What is cordon?
- What is drain?
- What is uncordon?
- What is a Pod Disruption Budget?
- Why should nodes be drained before maintenance?
- What is node replacement?
- What is planned maintenance?
- What is emergency maintenance?
- What is disk pressure?
- Why are backups important before maintenance?
- What is a maintenance window?
- What is a maintenance runbook?

---

## Intermediate

- How do you safely reboot a Kubernetes node?
- What happens when you cordon a node?
- What happens when you drain a node?
- How do PDBs affect drain?
- Why might `kubectl drain` fail?
- What happens to DaemonSet Pods during drain?
- How do you check whether a node has enough capacity?
- How do you troubleshoot a node after reboot?
- How do you maintain CNI components?
- How do you maintain CSI components?
- How do you maintain CoreDNS?
- How do you perform certificate maintenance?
- How do you identify disk pressure?
- How do you safely clean unused resources?
- How do you maintain stateful workloads?

---

## Advanced

- Design a zero-downtime node maintenance strategy.
- How would you maintain a 500-node Kubernetes cluster?
- How would you automate node patching?
- How would you safely replace nodes?
- How would you maintain a cluster across multiple availability zones?
- How would you perform emergency patching for a critical kernel vulnerability?
- How would you maintain etcd safely?
- How would you handle maintenance when PDBs prevent draining?
- How would you handle a node that remains NotReady after maintenance?
- How would you design a production maintenance runbook?
- How would you maintain Kubernetes without affecting critical applications?
- How would you combine Cluster Autoscaler with node maintenance?
- How would you validate networking and storage after maintenance?

---

# Interview Scenario 1

### Question

> How would you safely reboot a production Kubernetes node?

### Answer

Use:

```text
Check Cluster Health
 ↓
Check Capacity
 ↓
Review PDBs
 ↓
Cordon
 ↓
Drain
 ↓
Reboot
 ↓
Validate Node
 ↓
Validate Pods
 ↓
Validate Applications
 ↓
Uncordon
 ↓
Monitor
```

---

# Interview Scenario 2

### Question

> What is the difference between cordon and drain?

### Answer

`cordon`:

```text
Prevents new Pods from scheduling
```

`drain`:

```text
Moves/evicts eligible workloads so the node can be safely maintained
```

Typical sequence:

```text
Cordon
 ↓
Drain
```

---

# Interview Scenario 3

### Question

> Why might `kubectl drain` fail?

### Answer

Possible reasons include:

```text
PDB Restrictions
Unmanaged Pods
Local Storage
DaemonSets
Insufficient Capacity
Pod Eviction Issues
```

The correct response is to understand the workload rather than blindly bypassing safety checks.

---

# Interview Scenario 4

### Question

> What happens if you drain a node without enough cluster capacity?

### Answer

Some workloads may remain Pending:

```text
Node Drained
 ↓
Pods Rescheduled
 ↓
Insufficient Capacity
 ↓
Pods Pending
```

Therefore, capacity must be checked before maintenance.

---

# Interview Scenario 5

### Question

> How do you safely patch 100 Kubernetes nodes?

### Answer

Use a rolling strategy:

```text
Health Check
 ↓
Select Batch
 ↓
Cordon
 ↓
Drain
 ↓
Patch
 ↓
Reboot
 ↓
Validate
 ↓
Uncordon
 ↓
Next Batch
```

Use small batches initially and monitor continuously.

---

# Interview Scenario 6

### Question

> Why might replacing nodes be better than patching them in place?

### Answer

Node replacement can provide:

```text
Consistent Images
Less Configuration Drift
Repeatability
Automation
Simpler Recovery
```

This is especially useful with immutable or managed node-pool approaches.

---

# Interview Scenario 7

### Question

> How do you maintain a stateful application?

### Answer

First understand:

```text
Replication
Storage
Failover
PDB
Backup
Recovery
```

Do not assume that draining a node is harmless simply because multiple Pods exist.

---

# Interview Scenario 8

### Question

> How do you maintain a Kubernetes cluster during a critical security patch?

### Answer

Use an accelerated but controlled process:

```text
Identify Vulnerability
 ↓
Assess Exposure
 ↓
Backup
 ↓
Prepare Patch
 ↓
Test
 ↓
Cordon / Drain
 ↓
Patch
 ↓
Validate
 ↓
Roll Through Remaining Nodes
 ↓
Monitor
```

If the vulnerability is actively exploited, the change window may need to be shortened.

---

# Interview Scenario 9

### Question

> What should you monitor during maintenance?

### Answer

Monitor:

```text
Node Status
Pod Status
CPU
Memory
API Errors
Application Errors
Latency
Network
Storage
DNS
```

---

# Interview Scenario 10

### Question

> Design a production cluster maintenance strategy.

### Answer

Use:

```text
Maintenance Planning
+
Change Management
+
Backup
+
Capacity Planning
+
PDB
+
Rolling Maintenance
+
Automation
+
Monitoring
+
Validation
+
Recovery
```

Architecture:

```text
Maintenance Request
       │
       ▼
Risk Assessment
       │
       ▼
Backup + Health Check
       │
       ▼
Capacity / PDB Check
       │
       ▼
Cordon
       │
       ▼
Drain
       │
       ▼
Maintenance
       │
       ▼
Validation
       │
       ▼
Uncordon
       │
       ▼
Monitor
       │
       ▼
Document
```

---

# Production Maintenance Checklist

```text
☑ Maintenance scope defined
☑ Maintenance window defined
☑ Risk assessment completed
☑ Backup verified
☑ Cluster health verified
☑ Node health verified
☑ Application health verified
☑ Capacity checked
☑ PDBs checked
☑ Stateful workloads identified
☑ DaemonSets identified
☑ Static Pods identified
☑ Node labels checked
☑ Node taints checked
☑ Affinity rules reviewed
☑ Monitoring active
☑ Logging active
☑ CNI checked
☑ CSI checked
☑ Certificates checked
☑ Cordon completed
☑ Drain completed
☑ Maintenance completed
☑ Node validated
☑ Pods validated
☑ Applications validated
☑ Uncordon completed
☑ Post-maintenance monitoring completed
☑ Change documented
```

---

# Chapter Summary

Kubernetes cluster maintenance is an ongoing operational discipline.

A safe node-maintenance workflow is:

```text
Health Check
 ↓
Capacity Check
 ↓
PDB Review
 ↓
Cordon
 ↓
Drain
 ↓
Maintenance
 ↓
Reboot if Required
 ↓
Validate
 ↓
Uncordon
 ↓
Monitor
```

Important maintenance areas include:

```text
Nodes
Control Plane
kubelet
Container Runtime
OS
Kernel
CNI
CSI
CoreDNS
Ingress
Gateway
Certificates
etcd
Storage
Networking
Disk
Resources
```

Production maintenance should combine:

```text
Planning
+
Automation
+
Redundancy
+
Monitoring
+
Backup
+
Validation
+
Recovery
```

The most important principle is:

> **Kubernetes maintenance should be performed as a controlled change: understand the workloads, preserve sufficient capacity, protect against disruption, maintain observability, validate every stage, and never assume that a healthy node automatically means a healthy application.**

---

## Next Chapter

# Chapter 71 – Resource Optimization

Topics will include:

- Resource Optimization Fundamentals
- Kubernetes Resource Management
- CPU Optimization
- Memory Optimization
- Storage Optimization
- Network Optimization
- Pod Resource Requests
- Pod Resource Limits
- Quality of Service Classes
- Guaranteed QoS
- Burstable QoS
- BestEffort QoS
- CPU Requests
- CPU Limits
- Memory Requests
- Memory Limits
- ResourceQuota
- LimitRange
- Namespace Resource Management
- Resource Utilization
- Overprovisioning
- Underprovisioning
- Bin Packing
- Scheduling Efficiency
- Node Utilization
- Pod Density
- Vertical Pod Autoscaler
- Horizontal Pod Autoscaler
- Cluster Autoscaler
- Node Autoscaling
- Cost Optimization
- Right-Sizing
- Workload Profiling
- Capacity Planning
- Headroom
- Requests vs Actual Usage
- CPU Throttling
- Memory Pressure
- OOMKilled
- Evictions
- Disk Pressure
- Ephemeral Storage
- Storage Optimization
- Image Optimization
- Network Efficiency
- DNS Optimization
- Logging Cost Optimization
- Monitoring Cost Optimization
- Idle Resources
- Unused Resources
- Resource Cleanup
- Scheduling Optimization
- Node Affinity
- Taints and Tolerations
- Topology Spread
- Priority Classes
- Preemption
- Autoscaling Strategies
- HPA Optimization
- VPA Optimization
- Cluster Autoscaler Optimization
- Cost Allocation
- Namespace Cost Management
- Multi-Tenant Optimization
- Production Optimization
- Resource Efficiency Metrics
- Optimization Runbooks
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---