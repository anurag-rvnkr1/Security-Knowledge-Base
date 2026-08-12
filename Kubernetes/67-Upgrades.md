# Chapter 67 – Upgrades

## Overview

Kubernetes upgrades are the controlled process of moving a cluster, its control-plane components, worker nodes, and related ecosystem components from one supported version to another.

Regular upgrades are important because they provide:

```text
Security Fixes
Bug Fixes
Performance Improvements
New Features
API Improvements
Dependency Updates
```

A Kubernetes upgrade should never be treated as simply changing a version number.

A production upgrade involves:

```text
Planning
   ↓
Compatibility Review
   ↓
Backup
   ↓
Testing
   ↓
Control Plane Upgrade
   ↓
Worker Node Upgrade
   ↓
Validation
   ↓
Monitoring
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes upgrade fundamentals
- Why Kubernetes upgrades matter
- Kubernetes release lifecycle
- Version skew
- Control-plane upgrades
- Worker-node upgrades
- kubelet upgrades
- kubectl compatibility
- API version changes
- Deprecated APIs
- Removed APIs
- CRD compatibility
- CNI compatibility
- CSI compatibility
- Ingress compatibility
- Gateway API compatibility
- Operator compatibility
- Helm compatibility
- Admission webhook compatibility
- Monitoring-stack compatibility
- Backup before upgrade
- Upgrade planning
- Upgrade strategies
- Rolling upgrades
- Node-by-node upgrades
- Surge upgrades
- Cordon
- Drain
- Uncordon
- Pod Disruption Budgets
- Capacity planning
- Maintenance windows
- Preflight checks
- Cluster health checks
- Upgrade testing
- Staging clusters
- Canary nodes
- Control-plane upgrades
- Worker-node upgrades
- Managed Kubernetes upgrades
- kubeadm upgrades
- Cloud-provider upgrades
- Upgrade automation
- Rollback
- Upgrade failures
- API Server failures
- Scheduler failures
- Controller failures
- Node failures
- CNI failures
- CSI failures
- Admission failures
- Certificate issues
- etcd backups
- Disaster recovery
- Post-upgrade validation
- Monitoring
- Security
- Production upgrade checklist
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is a Kubernetes Upgrade?

A Kubernetes upgrade changes one or more cluster components to newer supported versions.

For example:

```text
Kubernetes 1.33
      ↓
Kubernetes 1.34
```

An upgrade may involve:

```text
Control Plane
Worker Nodes
kubelet
kubectl
CNI
CSI
Ingress
Operators
Monitoring
Security Tools
```

Not all components necessarily need to be upgraded at exactly the same time.

---

# Why Upgrade Kubernetes?

Upgrades provide:

```text
Security Patches
Bug Fixes
Performance Improvements
New APIs
Feature Improvements
Dependency Updates
```

Remaining on an old version can create:

```text
Security Risk
Unsupported Configuration
Compatibility Problems
Operational Risk
```

---

# Kubernetes Release Lifecycle

Kubernetes releases are versioned using:

```text
Major.Minor.Patch
```

Example:

```text
1.34.2
```

Where:

```text
1     → Major
34    → Minor
2     → Patch
```

Kubernetes follows a regular release process, and supported-version windows change over time.

Always verify the currently supported versions using the official Kubernetes documentation before planning a production upgrade.

---

# Patch Upgrade

Example:

```text
1.34.1
   ↓
1.34.2
```

Patch releases generally contain:

```text
Bug Fixes
Security Fixes
```

---

# Minor Upgrade

Example:

```text
1.33
 ↓
1.34
```

Minor upgrades can introduce:

```text
New Features
API Changes
Behavior Changes
Deprecations
```

Therefore, they require more planning.

---

# Major Upgrade

Kubernetes major-version changes are less frequent than minor and patch releases.

The upgrade process should always follow the version-specific documentation and compatibility requirements.

---

# Control Plane

The control plane contains:

```text
API Server
Scheduler
Controller Manager
etcd
Cloud Controller Manager
```

Depending on the cluster architecture.

---

# Worker Nodes

Worker nodes commonly contain:

```text
kubelet
Container Runtime
kube-proxy
CNI Components
CSI Components
```

---

# Upgrade Order

A common Kubernetes upgrade pattern is:

```text
Control Plane
      ↓
Worker Nodes
```

Worker nodes should generally not be upgraded beyond the supported version-skew constraints of the Kubernetes release.

---

# Version Skew

Version skew describes supported differences between Kubernetes component versions.

For example:

```text
API Server
    ↓
kubelet
    ↓
kubectl
```

The versions cannot be mixed arbitrarily.

Always follow the official version-skew policy for the specific Kubernetes versions being used.

---

# Why Version Skew Matters

Unsupported combinations can cause:

```text
Unexpected Behavior
API Compatibility Issues
Feature Problems
Upgrade Failures
```

---

# kubectl Version

Check:

```bash
kubectl version
```

The client and server versions should comply with the Kubernetes version-skew policy.

---

# kubelet Version

The kubelet version is important because it directly participates in node operation.

Check the node's Kubernetes version:

```bash
kubectl get nodes
```

---

# Upgrade Planning

Before an upgrade:

```text
1. Identify Current Version
2. Select Target Version
3. Review Supported Upgrade Path
4. Check Deprecated APIs
5. Check Add-ons
6. Check Backups
7. Test
8. Schedule Maintenance
```

---

# Preflight Checklist

Before upgrading:

```text
☑ Cluster healthy
☑ All critical nodes Ready
☑ No major alerts
☑ etcd backup completed
☑ Application backup completed
☑ Resource capacity available
☑ PDBs reviewed
☑ Deprecated APIs checked
☑ CRDs reviewed
☑ CNI compatibility checked
☑ CSI compatibility checked
☑ Ingress/Gateway compatibility checked
☑ Operators checked
☑ Monitoring checked
☑ Logging checked
☑ Admission policies checked
☑ Recovery plan prepared
```

---

# Check Cluster Version

```bash
kubectl version
```

---

# Check Nodes

```bash
kubectl get nodes
```

---

# Check All Pods

```bash
kubectl get pods -A
```

Look for:

```text
CrashLoopBackOff
ImagePullBackOff
Pending
Error
Unknown
```

---

# Check Events

```bash
kubectl get events -A
```

---

# Check Node Resources

```bash
kubectl top nodes
```

if Metrics Server is available.

---

# Check Pod Resources

```bash
kubectl top pods -A
```

---

# Check API Resources

Before upgrading, review available APIs:

```bash
kubectl api-resources
```

---

# Deprecated APIs

Kubernetes periodically deprecates APIs.

Example:

```text
Old API
   ↓
Deprecated
   ↓
Removed
```

Applications using removed APIs may fail after an upgrade.

---

# API Version Migration

Example:

```yaml
apiVersion: old.example.io/v1beta1
```

may need to become:

```yaml
apiVersion: example.io/v1
```

The exact migration depends on the API.

---

# Why Deprecated APIs Matter

A workload may work today:

```text
Current Cluster
      ↓
Works
```

but fail after upgrade:

```text
New Cluster
      ↓
API Removed
      ↓
Failure
```

---

# CRDs

Custom Resource Definitions extend Kubernetes APIs.

Before upgrading:

```text
Review CRD Versions
Review Stored Versions
Review Conversion
Review Operator Compatibility
```

---

# Operators

Operators often depend on specific Kubernetes versions.

Check:

```text
Operator Version
Kubernetes Compatibility
CRD Compatibility
Webhook Compatibility
```

---

# CNI Compatibility

Networking plugins must support the target Kubernetes version.

Examples:

```text
Cilium
Calico
Flannel
```

Check:

```text
Supported Kubernetes Versions
Kernel Requirements
eBPF Requirements
Network Policy Compatibility
```

---

# CSI Compatibility

Storage drivers must also support the target Kubernetes version.

Check:

```text
CSI Driver
Kubernetes Version
Storage Backend
Snapshot Support
Sidecar Versions
```

---

# Ingress Compatibility

Before upgrading:

```text
Ingress Controller
Ingress API
Annotations
TLS
Load Balancer
```

must be reviewed.

---

# Gateway API Compatibility

If using Gateway API, check:

```text
Gateway API Version
Gateway Controller
GatewayClass
Routes
CRDs
```

---

# Admission Webhooks

Admission webhooks can block API operations.

Before upgrading, verify:

```text
Webhook Availability
TLS Certificates
Service Endpoints
CA Bundle
Timeouts
Failure Policy
```

---

# Monitoring Compatibility

Review:

```text
Prometheus
Grafana
Metrics Server
OpenTelemetry
Alertmanager
Exporters
```

---

# Logging Compatibility

Review:

```text
Fluent Bit
Fluentd
Vector
OpenTelemetry Collector
Log Backend
```

and ensure the logging stack supports the target environment.

---

# Helm Compatibility

Check:

```bash
helm version
```

Review:

```text
Helm Releases
Chart Versions
Kubernetes Compatibility
CRDs
Hooks
```

---

# Backup Before Upgrade

Always maintain a recovery plan before a production upgrade.

Important backups can include:

```text
etcd
Kubernetes Resources
Persistent Data
Application Configuration
Secrets
```

---

# Why Backup Before Upgrade?

If the upgrade causes a severe failure:

```text
Upgrade
 ↓
Failure
 ↓
Recovery
```

Without a valid backup:

```text
Failure
 ↓
Limited Recovery Options
```

---

# Upgrade Testing

Never test a major production upgrade for the first time directly in production.

Prefer:

```text
Development
 ↓
Staging
 ↓
Canary
 ↓
Production
```

---

# Staging Cluster

A staging cluster should resemble production where practical:

```text
Kubernetes Version
CNI
CSI
Ingress
Operators
Monitoring
Applications
```

---

# Canary Testing

Upgrade a small subset first.

Example:

```text
Worker Nodes

Node 1 → Upgrade
Node 2 → Upgrade
Node 3 → Upgrade later
Node 4 → Upgrade later
```

Observe:

```text
Application Health
Errors
Latency
Scheduling
Networking
Storage
```

---

# Rolling Upgrade

A rolling upgrade updates nodes gradually.

```text
Node 1
 ↓
Validate

Node 2
 ↓
Validate

Node 3
 ↓
Validate
```

This reduces blast radius.

---

# Node-by-Node Upgrade

A typical workflow:

```text
Cordon
 ↓
Drain
 ↓
Upgrade
 ↓
Reboot if Required
 ↓
Validate
 ↓
Uncordon
```

---

# Cordon

```bash
kubectl cordon <node-name>
```

This prevents new Pods from being scheduled onto the node.

---

# Drain

Example:

```bash
kubectl drain <node-name> \
  --ignore-daemonsets
```

The exact flags depend on workload characteristics and the Kubernetes version.

---

# Uncordon

After successful validation:

```bash
kubectl uncordon <node-name>
```

---

# Pod Disruption Budgets

PDBs help limit voluntary disruptions during maintenance.

Example:

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget

metadata:
  name: backend-pdb

spec:
  minAvailable: 2

  selector:
    matchLabels:
      app: backend
```

---

# Capacity Planning Before Upgrade

Suppose:

```text
3 worker nodes
```

You drain one node.

Remaining:

```text
2 nodes
```

Can the remaining nodes handle the workload?

Always check:

```text
CPU
Memory
Pod Count
Storage
Network
```

---

# Surge Capacity

If your infrastructure supports it, temporarily adding capacity can make upgrades safer.

Example:

```text
Normal:
3 Nodes

Upgrade:
4 Nodes

After Upgrade:
3 Nodes
```

This can reduce scheduling pressure.

---

# Managed Kubernetes Upgrades

Cloud-managed Kubernetes platforms may provide automated control-plane upgrades and node-pool upgrade mechanisms.

Examples include:

```text
Amazon EKS
Azure Kubernetes Service
Google Kubernetes Engine
```

The exact workflow differs between providers.

---

# Managed Upgrade Responsibilities

The cloud provider may manage:

```text
Control Plane
```

while you remain responsible for:

```text
Node Pools
Applications
Add-ons
CNI
CSI
Ingress
Policies
```

depending on the platform.

---

# kubeadm Upgrades

Clusters created using kubeadm follow a specific upgrade process.

Typical flow:

```text
Check Version
 ↓
Backup
 ↓
kubeadm Upgrade Plan
 ↓
Control Plane Upgrade
 ↓
kubelet / kubectl
 ↓
Worker Nodes
```

---

# kubeadm Preflight

Run:

```bash
kubeadm upgrade plan
```

This helps inspect available upgrade paths in supported kubeadm environments.

---

# kubeadm Upgrade

The exact commands depend on the source and target versions.

Follow the official kubeadm upgrade instructions rather than blindly applying commands from an older tutorial.

---

# Worker Node Upgrade With kubeadm

Typical conceptual workflow:

```text
Drain Node
 ↓
Upgrade kubeadm
 ↓
kubeadm upgrade node
 ↓
Upgrade kubelet
 ↓
Upgrade kubectl if needed
 ↓
Restart kubelet
 ↓
Uncordon
```

---

# Upgrade Automation

Large environments should automate repetitive tasks.

Possible tools:

```text
Terraform
Ansible
Cluster API
GitOps
Cloud Provider Automation
```

---

# GitOps and Upgrades

Infrastructure configuration can be version controlled.

```text
Git
 ↓
Review
 ↓
Test
 ↓
Deploy
 ↓
Validate
```

This provides:

```text
Auditability
Repeatability
Rollback
Change Review
```

---

# Upgrade Rollback

Rollback strategy depends on:

```text
Control Plane
Worker Nodes
Applications
CRDs
Data
```

Kubernetes does not provide a universal one-command rollback for every cluster upgrade.

---

# Why Rollback Is Difficult

Consider:

```text
Old Version
   ↓
Upgrade
   ↓
API Changes
   ↓
Data / Configuration Changes
```

Reverting may not be safe if:

```text
API Removed
State Changed
CRD Migrated
Data Format Changed
```

Therefore:

```text
Recovery Plan
>
Assumed Rollback
```

---

# Upgrade Failure

Potential failures:

```text
API Server
etcd
Scheduler
Controller Manager
kubelet
CNI
CSI
Admission
Certificates
Applications
```

---

# API Server Failure

Symptoms:

```text
kubectl commands fail
Applications cannot access API
Controllers fail
```

Investigate:

```text
API Server Logs
Certificates
etcd
Network
Resource Usage
```

---

# etcd Failure

Symptoms may include:

```text
API Server Errors
Cluster State Problems
Control Plane Instability
```

Check:

```text
etcd Health
Disk
Network
Certificates
Quorum
```

---

# Scheduler Failure

Symptoms:

```text
New Pods remain Pending
```

Check:

```text
Scheduler Logs
API Server
Resource Constraints
Events
```

---

# Controller Manager Failure

Symptoms:

```text
Desired State Not Reconciled
```

Examples:

```text
Replica Count Not Correct
Nodes Not Properly Reconciled
```

---

# kubelet Failure

Symptoms:

```text
Node NotReady
Pods Not Running
Container Management Problems
```

Check:

```text
kubelet
Container Runtime
CNI
Disk
Memory
Certificates
```

---

# CNI Failure

Symptoms:

```text
Pods Cannot Reach Network
DNS Problems
Service Communication Failures
```

Check:

```text
CNI Pods
Routes
Network Policies
Node Network
CNI Compatibility
```

---

# CSI Failure

Symptoms:

```text
PVC Pending
Mount Failures
Volume Attach Errors
```

Check:

```text
CSI Controller
CSI Node
Storage Backend
Permissions
Driver Compatibility
```

---

# Admission Failure

Symptoms:

```text
kubectl apply
 ↓
Request Rejected
```

Check:

```text
Admission Webhook
Certificate
Service
Endpoint
Policy
```

---

# Certificate Problems

Upgrades can expose certificate issues.

Check:

```text
Expiration
CA
SAN
Trust
Rotation
```

---

# Post-Upgrade Validation

After upgrading:

```text
1. Check Control Plane
2. Check Nodes
3. Check System Pods
4. Check Networking
5. Check Storage
6. Check DNS
7. Check Applications
8. Check Monitoring
9. Check Logging
10. Check Security
```

---

# Check Nodes

```bash
kubectl get nodes
```

Verify:

```text
Ready
Version
```

---

# Check Pods

```bash
kubectl get pods -A
```

Look for:

```text
CrashLoopBackOff
Pending
Error
ImagePullBackOff
```

---

# Check Events

```bash
kubectl get events -A
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

# Check Gateway

```bash
kubectl get gateway -A
```

if Gateway API is installed.

---

# Check Storage

```bash
kubectl get pv
kubectl get pvc -A
```

---

# Check DNS

Deploy a test Pod and verify:

```text
Service DNS
External DNS
Cluster DNS
```

---

# Application Validation

Test:

```text
Authentication
API Requests
Database Access
Message Queues
External APIs
Background Jobs
```

Do not rely only on:

```text
Pod = Running
```

---

# Monitoring After Upgrade

Monitor:

```text
CPU
Memory
API Latency
Error Rate
Pod Restarts
Node Health
Network Errors
Storage Errors
Application Latency
```

---

# Upgrade Observability

A useful dashboard can contain:

```text
Node Status
Pod Restarts
API Server Errors
API Latency
Scheduler Metrics
Controller Metrics
etcd Metrics
CNI Metrics
CSI Metrics
Application SLOs
```

---

# Security Validation

After upgrading, verify:

```text
RBAC
Network Policies
Pod Security
Admission Policies
Secrets
Certificates
Audit Logging
Image Policies
```

---

# Upgrade Communication

Production upgrades should have:

```text
Change Ticket
Maintenance Window
Owner
Approvers
Rollback / Recovery Plan
Monitoring Plan
Communication Plan
```

---

# Upgrade Runbook

A runbook can follow:

```text
Pre-Checks
 ↓
Backup
 ↓
Upgrade Control Plane
 ↓
Validate
 ↓
Upgrade Workers
 ↓
Validate
 ↓
Application Testing
 ↓
Monitoring
 ↓
Close Change
```

---

# Upgrade Strategy Example

Suppose:

```text
10 Worker Nodes
```

Use:

```text
1 Canary Node
 ↓
Validate
 ↓
2 Nodes
 ↓
Validate
 ↓
3 Nodes
 ↓
Validate
 ↓
Remaining Nodes
```

This limits the blast radius.

---

# Upgrade and PDBs

PDBs can prevent too many replicas from being voluntarily disrupted.

However:

```text
PDB
≠
Infinite Capacity
```

If there is insufficient capacity, drain may block.

---

# Upgrade and StatefulSets

Stateful workloads require extra care because:

```text
Persistent Storage
Stable Identity
Ordering
```

may matter.

Examples:

```text
Databases
Queues
Stateful Services
```

---

# Upgrade and DaemonSets

DaemonSets run Pods across nodes.

During node draining:

```text
DaemonSet Pods
```

are handled differently from ordinary replicated workloads.

Do not blindly use drain flags without understanding their effect.

---

# Upgrade and Static Pods

Some control-plane components may be deployed as static Pods, depending on the cluster architecture.

These require different upgrade procedures than ordinary application Pods.

---

# Upgrade and CRDs

Before upgrading:

```text
List CRDs
Review Versions
Check Operators
Check Conversion
```

Run:

```bash
kubectl get crd
```

---

# Upgrade and Webhooks

Check:

```bash
kubectl get validatingwebhookconfigurations
```

and:

```bash
kubectl get mutatingwebhookconfigurations
```

Verify webhook dependencies.

---

# Upgrade and API Discovery

Inspect:

```bash
kubectl api-resources
```

Review APIs used by applications and operators.

---

# Upgrade and Helm

List releases:

```bash
helm list -A
```

Review chart compatibility before upgrading the Kubernetes cluster.

---

# Upgrade and Monitoring

Before upgrading:

```text
Monitoring Healthy
```

During upgrade:

```text
Monitor
```

After upgrade:

```text
Compare Metrics
```

---

# Upgrade and Logging

Ensure:

```text
Logs Continue
```

after each infrastructure component is upgraded.

---

# Upgrade and Backups

The safest sequence is:

```text
Validate Backup
      ↓
Test Restore
      ↓
Upgrade
```

---

# Disaster Recovery During Upgrade

If a serious issue occurs:

```text
Stop Further Upgrade
      ↓
Assess Failure
      ↓
Use Recovery Plan
      ↓
Restore if Required
      ↓
Validate
```

---

# Common Mistakes

## 1. Upgrading Directly in Production

Always test first.

---

## 2. Ignoring Deprecated APIs

Removed APIs can break applications.

---

## 3. Ignoring Add-ons

CNI, CSI, Ingress, and operators must support the target version.

---

## 4. No Backup

An upgrade without recovery planning is dangerous.

---

## 5. No Capacity

Draining nodes may leave insufficient capacity.

---

## 6. Ignoring PDBs

PDBs can block maintenance.

---

## 7. Upgrading Too Many Nodes at Once

This increases blast radius.

---

## 8. Assuming Rollback Is Easy

Cluster upgrades are not universally reversible.

---

## 9. No Post-Upgrade Validation

A successful command does not guarantee a healthy cluster.

---

## 10. Ignoring Monitoring

Problems can remain undetected.

---

## 11. Ignoring Certificates

Certificate failures can appear after component changes.

---

## 12. Forgetting CRDs

Custom workloads may break.

---

# Best Practices

### 1. Plan Before Upgrading

Document:

```text
Source
Target
Dependencies
Risks
Recovery
```

---

### 2. Back Up First

Maintain:

```text
etcd
Application Data
Cluster Resources
```

where applicable.

---

### 3. Test in Staging

Use production-like configuration.

---

### 4. Upgrade Gradually

Use:

```text
Canary
Rolling Upgrade
Node-by-Node
```

---

### 5. Maintain Capacity

Ensure workloads can tolerate node maintenance.

---

### 6. Review API Deprecations

Identify removed APIs before the upgrade.

---

### 7. Validate Add-ons

Check:

```text
CNI
CSI
Ingress
Gateway
Operators
Monitoring
Logging
```

---

### 8. Monitor During the Upgrade

Watch:

```text
Nodes
Pods
API
Applications
```

---

### 9. Validate After Every Stage

Do not wait until the entire upgrade is finished.

---

### 10. Maintain a Recovery Plan

Document:

```text
Backup
Restore
Escalation
Recovery
```

---

# Hands-on Lab 1 – Kubernetes Version Inspection

Run:

```bash
kubectl version
kubectl get nodes
```

Document:

```text
Client Version
Server Version
Node Versions
```

---

# Hands-on Lab 2 – API Deprecation Review

List APIs:

```bash
kubectl api-resources
```

Review workloads and identify old API versions.

---

# Hands-on Lab 3 – Upgrade a Test Cluster

Create a disposable Kubernetes cluster.

Perform:

```text
Backup
Upgrade
Validation
```

Document every step.

---

# Hands-on Lab 4 – Node-by-Node Upgrade

Use a test cluster.

Perform:

```text
Cordon
Drain
Upgrade
Validate
Uncordon
```

one node at a time.

---

# Hands-on Lab 5 – PDB During Upgrade

Deploy:

```text
3 Replica Application
```

Create:

```text
PDB
```

Drain a node.

Observe the disruption behavior.

---

# Hands-on Lab 6 – Capacity Testing

Deploy enough workloads to consume most node resources.

Drain a node.

Observe:

```text
Pending Pods
Scheduling
Capacity
```

---

# Hands-on Lab 7 – Canary Upgrade

Upgrade:

```text
1 Node
```

Monitor:

```text
Applications
Network
Storage
Logs
Metrics
```

Then upgrade the remaining nodes.

---

# Hands-on Lab 8 – CNI Compatibility

Check the installed CNI version.

Review its compatibility with the target Kubernetes version.

Perform the upgrade in a test environment.

---

# Hands-on Lab 9 – CSI Compatibility

Check:

```bash
kubectl get pods -A
```

Identify CSI components.

Test:

```text
PVC Creation
Mount
Read
Write
Unmount
```

after upgrade.

---

# Hands-on Lab 10 – Admission Webhook Validation

Create a test admission webhook.

Upgrade the cluster.

Verify that:

```text
Validation
Mutation
TLS
```

continue working.

---

# Hands-on Lab 11 – Application Validation

After an upgrade, test:

```text
Frontend
API
Database
Ingress
Background Worker
```

Create an automated smoke test.

---

# Hands-on Lab 12 – Monitoring Validation

Verify:

```text
Prometheus
Grafana
Metrics Server
OpenTelemetry
Alertmanager
```

after upgrade.

---

# Hands-on Lab 13 – Logging Validation

Verify logs continue flowing from:

```text
Application
Node
Control Plane
```

as applicable.

---

# Hands-on Lab 14 – Upgrade Failure Simulation

In a disposable environment, introduce a controlled failure during node maintenance.

Practice:

```text
Stop
Investigate
Recover
Resume
```

---

# Hands-on Lab 15 – Recovery Test

Take a backup before upgrade.

Simulate an unrecoverable upgrade problem.

Practice the documented recovery process.

---

# Hands-on Lab 16 – Managed Kubernetes Upgrade

Using a supported cloud sandbox, perform a test upgrade.

Observe:

```text
Control Plane
Node Pool
Add-ons
Applications
```

---

# Hands-on Lab 17 – kubeadm Upgrade

Create a test kubeadm cluster.

Practice:

```bash
kubeadm upgrade plan
```

Then perform the version-appropriate upgrade procedure.

---

# Hands-on Lab 18 – Post-Upgrade Checklist

Create a script or checklist that validates:

```text
Nodes
Pods
Services
PVCs
DNS
Ingress
Applications
Monitoring
```

---

# Hands-on Lab 19 – Upgrade Metrics

Record before and after:

```text
API Latency
Pod Restart Rate
Node CPU
Node Memory
Application Latency
Error Rate
```

Compare the results.

---

# Hands-on Lab 20 – Full Production Upgrade Simulation

Design a complete upgrade exercise:

```text
Current Cluster
      ↓
Health Check
      ↓
Backup
      ↓
Staging Test
      ↓
Canary
      ↓
Control Plane Upgrade
      ↓
Worker Upgrade
      ↓
Application Validation
      ↓
Monitoring
      ↓
Completion
```

Document:

```text
Risks
Owners
Commands
Validation
Recovery
```

---

# Quick Revision

## Kubernetes Upgrade

```text
Moving cluster components to a newer supported version
```

---

## Patch Upgrade

```text
Bug/security fix release
```

---

## Minor Upgrade

```text
Upgrade between Kubernetes minor versions
```

---

## Version Skew

```text
Supported version differences between Kubernetes components
```

---

## Cordon

```text
Prevents new scheduling on a node
```

---

## Drain

```text
Evicts/deletes eligible workloads for maintenance
```

---

## Uncordon

```text
Allows scheduling on the node again
```

---

## PDB

```text
Controls voluntary disruption of replicated workloads
```

---

## Canary Upgrade

```text
Upgrade a small subset before broader rollout
```

---

## Rolling Upgrade

```text
Upgrade infrastructure gradually
```

---

## Deprecated API

```text
API still available but scheduled for removal
```

---

## Removed API

```text
API no longer available
```

---

## Upgrade Validation

```text
Confirm cluster and applications remain healthy after upgrade
```

---

# Essential Commands

Check Kubernetes version:

```bash
kubectl version
```

Check nodes:

```bash
kubectl get nodes
```

Check node details:

```bash
kubectl describe node <node-name>
```

Check Pods:

```bash
kubectl get pods -A
```

Check events:

```bash
kubectl get events -A
```

Check resources:

```bash
kubectl top nodes
```

Check API resources:

```bash
kubectl api-resources
```

Check CRDs:

```bash
kubectl get crd
```

Check validating webhooks:

```bash
kubectl get validatingwebhookconfigurations
```

Check mutating webhooks:

```bash
kubectl get mutatingwebhookconfigurations
```

Check Helm releases:

```bash
helm list -A
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

For kubeadm:

```bash
kubeadm upgrade plan
```

---

# Interview Questions

## Basic

- What is a Kubernetes upgrade?
- Why should Kubernetes clusters be upgraded?
- What is the difference between a patch and minor release?
- What is version skew?
- What is a control-plane upgrade?
- What is a worker-node upgrade?
- What is kubelet?
- What is the role of kubeadm?
- What is cordon?
- What is drain?
- What is uncordon?
- What is a Pod Disruption Budget?
- What is a deprecated API?
- What is a removed API?
- Why should you back up before upgrading?

---

## Intermediate

- What is the recommended order for Kubernetes upgrades?
- How do you prepare a production cluster for an upgrade?
- How do you check for deprecated APIs?
- How do you upgrade worker nodes safely?
- Why is capacity planning important during upgrades?
- How do PDBs affect node draining?
- How do you handle StatefulSets during upgrades?
- How do you validate an upgrade?
- How do you check CNI compatibility?
- How do you check CSI compatibility?
- How do you verify admission webhooks?
- How do you troubleshoot a node that becomes NotReady after an upgrade?
- How do you troubleshoot Pods stuck in Pending after an upgrade?
- How do you handle a failed Kubernetes upgrade?

---

## Advanced

- Design a zero/minimal-downtime Kubernetes upgrade strategy.
- How would you upgrade a 100-node production cluster?
- How would you perform a canary upgrade?
- How would you handle API removals?
- How would you upgrade a cluster with stateful workloads?
- How would you upgrade a highly available control plane?
- How would you upgrade a kubeadm cluster?
- How would you upgrade a managed Kubernetes cluster?
- How would you recover from a failed control-plane upgrade?
- Why is rollback difficult after a Kubernetes upgrade?
- How would you design upgrade automation?
- How would you validate CNI, CSI, and admission webhooks after an upgrade?
- How would you design an upgrade strategy across multiple Kubernetes clusters?
- How would you minimize application downtime during worker-node upgrades?

---

# Interview Scenario 1

### Question

> What is the general order of a Kubernetes upgrade?

### Answer

A common approach is:

```text
Backup
 ↓
Health Check
 ↓
Compatibility Review
 ↓
Control Plane Upgrade
 ↓
Validation
 ↓
Worker Node Upgrade
 ↓
Application Validation
 ↓
Monitoring
```

The exact process depends on the Kubernetes distribution and upgrade mechanism.

---

# Interview Scenario 2

### Question

> Why should you check deprecated APIs before upgrading?

### Answer

Because an API available in the current version may be removed in the target version.

Example:

```text
Current Version
      ↓
Old API Works
      ↓
Upgrade
      ↓
API Removed
      ↓
Application Failure
```

Therefore, API usage should be reviewed before upgrading.

---

# Interview Scenario 3

### Question

> How would you upgrade worker nodes with minimal disruption?

### Answer

Use a controlled rolling strategy:

```text
Check Capacity
 ↓
Check PDB
 ↓
Cordon Node
 ↓
Drain Node
 ↓
Upgrade Node
 ↓
Validate
 ↓
Uncordon
```

Then repeat for the next node.

---

# Interview Scenario 4

### Question

> What happens if there is not enough capacity while draining a node?

### Answer

Some Pods may remain Pending because the remaining nodes cannot satisfy their resource requests or scheduling constraints.

Check:

```text
CPU
Memory
Taints
Affinity
Pod Requests
PDB
Topology Constraints
```

Add capacity if necessary.

---

# Interview Scenario 5

### Question

> Why is rollback not always straightforward?

### Answer

An upgrade can involve:

```text
API Changes
CRD Changes
State Changes
Component Changes
```

After moving forward, simply reinstalling the old binaries may not safely restore the previous state.

Therefore:

```text
Backup
+
Tested Recovery Plan
```

is more reliable than assuming rollback will always work.

---

# Interview Scenario 6

### Question

> How would you handle a CNI failure after a Kubernetes upgrade?

### Answer

Check:

```text
CNI Version
CNI Compatibility
CNI Pods
Node Networking
Routes
Network Policies
Kernel Requirements
```

Then inspect CNI logs and node-level networking.

Do not immediately change production networking without understanding the failure mode.

---

# Interview Scenario 7

### Question

> How would you handle CSI failures after an upgrade?

### Answer

Check:

```text
CSI Controller
CSI Node
StorageClass
PVC
PV
Storage Backend
Driver Compatibility
```

Then inspect:

```bash
kubectl describe pvc <pvc-name>
```

and relevant CSI logs.

---

# Interview Scenario 8

### Question

> How would you validate a Kubernetes upgrade?

### Answer

Validate:

```text
Control Plane
 ↓
Nodes
 ↓
System Pods
 ↓
DNS
 ↓
Networking
 ↓
Storage
 ↓
Ingress / Gateway
 ↓
Applications
 ↓
Monitoring
 ↓
Logging
 ↓
Security
```

Then compare key metrics before and after the upgrade.

---

# Interview Scenario 9

### Question

> How would you upgrade a 100-node cluster?

### Answer

Use a staged strategy:

```text
Backup
 ↓
Staging Test
 ↓
Canary Node
 ↓
Small Batch
 ↓
Observe
 ↓
Larger Batches
 ↓
Complete
```

Maintain enough capacity to keep applications healthy while nodes are being drained.

---

# Interview Scenario 10

### Question

> Design a production Kubernetes upgrade strategy.

### Answer

Use:

```text
Version Planning
+
Compatibility Review
+
Backup
+
Staging
+
Canary
+
Rolling Upgrade
+
Capacity Planning
+
PDB
+
Monitoring
+
Validation
+
Recovery Plan
```

Architecture:

```text
                    Production
                        │
                  Health Check
                        │
                     Backup
                        │
                  Compatibility
                        │
                    Canary
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
        Control Plane          Workers
              │                   │
              └─────────┬─────────┘
                        ▼
                    Validation
                        │
                        ▼
                     Monitor
```

---

# Production Upgrade Checklist

```text
☑ Source version identified
☑ Target version identified
☑ Supported upgrade path verified
☑ Version skew reviewed
☑ Deprecated APIs checked
☑ CRDs reviewed
☑ Operators reviewed
☑ CNI compatibility checked
☑ CSI compatibility checked
☑ Ingress compatibility checked
☑ Gateway compatibility checked
☑ Admission webhooks checked
☑ Monitoring checked
☑ Logging checked
☑ Backup completed
☑ Restore capability verified
☑ Capacity verified
☑ PDBs reviewed
☑ Maintenance window approved
☑ Canary strategy defined
☑ Control plane upgraded
☑ Worker nodes upgraded
☑ Applications validated
☑ Security validated
☑ Monitoring validated
☑ Recovery plan available
☑ Upgrade documented
```

---

# Chapter Summary

Kubernetes upgrades are controlled infrastructure changes that require planning, compatibility analysis, testing, backup, gradual rollout, and validation.

A safe upgrade workflow is:

```text
Plan
 ↓
Backup
 ↓
Compatibility Check
 ↓
Test
 ↓
Control Plane Upgrade
 ↓
Validate
 ↓
Worker Upgrade
 ↓
Validate
 ↓
Monitor
```

The most important areas to review before an upgrade are:

```text
Deprecated APIs
CRDs
Operators
CNI
CSI
Ingress
Gateway API
Admission Webhooks
Monitoring
Logging
```

Worker-node maintenance commonly follows:

```text
Cordon
 ↓
Drain
 ↓
Upgrade
 ↓
Validate
 ↓
Uncordon
```

A production upgrade should also account for:

```text
Capacity
PDBs
Stateful Workloads
Backup
Disaster Recovery
Security
Observability
```

The most important principle is:

> **A Kubernetes upgrade should be treated as a controlled production change, not a simple version replacement. The safest approach combines compatibility testing, reliable backups, gradual rollout, sufficient capacity, continuous monitoring, and a tested recovery plan.**

---

## Next Chapter

# Chapter 68 – High Availability

Topics will include:

- High Availability Fundamentals
- Availability
- Reliability
- Fault Tolerance
- Single Point of Failure
- Kubernetes HA Architecture
- Control Plane HA
- API Server HA
- etcd HA
- Scheduler HA
- Controller Manager HA
- Cloud Controller Manager HA
- Worker Node HA
- Load Balancer
- API Server Load Balancing
- etcd Quorum
- etcd Leader Election
- Control Plane Replicas
- Worker Node Pools
- Multi-Zone Clusters
- Multi-Region Architecture
- Pod Replicas
- Deployments
- StatefulSets
- DaemonSets
- Pod Disruption Budgets
- Topology Spread Constraints
- Pod Anti-Affinity
- Node Affinity
- Taints and Tolerations
- Failure Domains
- Availability Zones
- Node Failure
- Control Plane Failure
- API Server Failure
- etcd Failure
- Network Failure
- Storage Failure
- DNS Failure
- CNI Failure
- CSI Failure
- Load Balancer Failure
- Application Failure
- Health Checks
- Liveness Probes
- Readiness Probes
- Startup Probes
- Graceful Shutdown
- Rolling Updates
- Rolling Restarts
- Zero-Downtime Deployments
- Capacity Planning
- Spare Capacity
- Cluster Autoscaler
- Horizontal Pod Autoscaler
- Backup vs HA
- HA vs Disaster Recovery
- Multi-Cluster HA
- Active-Passive
- Active-Active
- Cross-Region HA
- Database HA
- Stateful Application HA
- Monitoring HA
- Logging HA
- Security HA
- HA Testing
- Chaos Testing
- Failure Simulation
- Recovery
- Troubleshooting
- Production HA Architecture
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---