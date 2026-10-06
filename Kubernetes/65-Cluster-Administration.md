# Chapter 65 – Cluster Administration

## Overview

Kubernetes cluster administration is the practice of operating, securing, monitoring, maintaining, troubleshooting, and optimizing a Kubernetes cluster.

A Kubernetes administrator is responsible for ensuring that the cluster remains:

```text
Available
Secure
Healthy
Performant
Scalable
Maintainable
```

A production Kubernetes cluster contains multiple interconnected components:

```text
                    Kubernetes Cluster
                           │
              ┌────────────┴────────────┐
              │                         │
        Control Plane                Worker Nodes
              │                         │
     ┌────────┼────────┐          ┌─────┼─────┐
     ▼        ▼        ▼          ▼     ▼     ▼
  API Server  etcd  Controllers  kubelet Runtime kube-proxy
     │
     ▼
 Scheduler
```

Cluster administration covers the complete lifecycle:

```text
Provision
   ↓
Configure
   ↓
Secure
   ↓
Monitor
   ↓
Maintain
   ↓
Upgrade
   ↓
Troubleshoot
   ↓
Scale
   ↓
Backup / Restore
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes cluster administration
- Cluster architecture
- Control plane
- Worker nodes
- API Server
- etcd
- Scheduler
- Controller Manager
- Cloud Controller Manager
- kubelet
- kube-proxy
- Container Runtime
- Cluster configuration
- kubeconfig
- kubectl
- Contexts
- Namespaces
- Nodes
- Node labels
- Node conditions
- Node capacity
- Node allocatable resources
- Node management
- Node registration
- Node draining
- Node cordoning
- Node uncordoning
- Pod eviction
- Cluster networking
- CNI
- Cluster DNS
- CoreDNS
- Services
- Ingress
- Gateway API
- Storage
- CSI
- Persistent Volumes
- Persistent Volume Claims
- RBAC
- Service Accounts
- Authentication
- Authorization
- Admission
- Secrets
- ConfigMaps
- Resource Quotas
- Limit Ranges
- Scheduling
- Taints
- Tolerations
- Affinity
- Node Selectors
- Pod Disruption Budgets
- Cluster monitoring
- Cluster logging
- Events
- Metrics
- Audit logs
- Control plane monitoring
- etcd management
- Certificate management
- Kubernetes PKI
- Cluster health
- API Server health
- Scheduler health
- Controller Manager health
- Node health
- Resource utilization
- Capacity planning
- Cluster scaling
- Cluster Autoscaler
- Manual scaling
- Cluster upgrades
- Backup
- Restore
- Security administration
- Network Policies
- Pod Security
- Image Security
- Runtime Security
- High Availability
- Troubleshooting
- Production operations
- Best practices
- Hands-on Labs
- Common mistakes
- Quick revision
- Interview questions

---

# What Is Cluster Administration?

Cluster administration involves managing the Kubernetes infrastructure and its configuration throughout the cluster lifecycle.

It includes:

```text
Cluster Components
+
Nodes
+
Networking
+
Storage
+
Security
+
Scheduling
+
Monitoring
+
Upgrades
+
Backup
+
Troubleshooting
```

---

# Kubernetes Cluster Architecture

A typical Kubernetes cluster contains:

```text
                    Cluster
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
     Control Plane              Worker Nodes
          │                         │
   ┌──────┼──────┐           ┌──────┼──────┐
   ▼      ▼      ▼           ▼      ▼      ▼
 API    etcd  Scheduler    kubelet Runtime kube-proxy
Server
   │
   └── Controllers
```

---

# Control Plane

The control plane manages the overall state of the cluster.

Major components include:

```text
kube-apiserver
etcd
kube-scheduler
kube-controller-manager
cloud-controller-manager
```

---

# Worker Node

A worker node runs application workloads.

Important components include:

```text
kubelet
Container Runtime
kube-proxy
```

A node may also run:

```text
CNI Components
CSI Components
Monitoring Agents
Logging Agents
```

depending on the cluster design.

---

# API Server

The Kubernetes API Server is the primary entry point to the Kubernetes control plane.

Architecture:

```text
kubectl
   │
   ▼
API Server
   │
   ├── etcd
   ├── Scheduler
   └── Controllers
```

---

# API Server Responsibilities

The API Server handles:

```text
Authentication
Authorization
Admission
API Requests
Resource Validation
Object Persistence Coordination
```

---

# Example API Request

When you execute:

```bash
kubectl get pods
```

the request generally follows:

```text
kubectl
  ↓
API Server
  ↓
Authorization
  ↓
Resource Retrieval
  ↓
Response
```

---

# etcd

`etcd` is the distributed key-value store used by Kubernetes to persist cluster state.

Conceptually:

```text
Kubernetes State
       ↓
      etcd
```

It stores information such as:

```text
Pods
Deployments
Services
Secrets
ConfigMaps
Nodes
RBAC Objects
Cluster Configuration
```

---

# Why etcd Is Critical

If etcd becomes unavailable:

```text
Control Plane
     ↓
Unable to reliably persist/read cluster state
```

Therefore:

```text
etcd
=
Critical Control Plane Component
```

---

# etcd Best Practices

Protect etcd with:

```text
Backups
Encryption
Access Control
TLS
High Availability
Monitoring
```

Never expose etcd publicly.

---

# Scheduler

The scheduler determines which node should run a newly created Pod.

Example:

```text
Pending Pod
    ↓
Scheduler
    ↓
Select Suitable Node
    ↓
Pod Assigned
```

---

# Scheduler Factors

The scheduler considers factors such as:

```text
Resource Requests
Node Availability
Node Selectors
Affinity
Anti-Affinity
Taints
Tolerations
Topology Constraints
Priority
```

---

# Controller Manager

The Controller Manager runs controllers that continuously reconcile desired state with actual state.

Conceptually:

```text
Desired State
     │
     ▼
Controller
     │
     ▼
Actual State
```

Example:

```text
Deployment:
replicas = 3

Actual:
2 Pods

Controller:
Create 1 Pod
```

---

# Cloud Controller Manager

The Cloud Controller Manager integrates Kubernetes with supported cloud-provider functionality.

Examples include managing cloud-specific resources such as:

```text
Load Balancers
Node Information
Routes
Volumes
```

The exact responsibilities depend on the cloud provider and integration architecture.

---

# kubelet

The kubelet runs on each worker node.

It ensures that Pods assigned to the node are running according to their specifications.

```text
API Server
    ↓
Pod Assignment
    ↓
kubelet
    ↓
Container Runtime
    ↓
Containers
```

---

# Container Runtime

The container runtime is responsible for running containers.

Kubernetes commonly uses runtimes compatible with the Container Runtime Interface (CRI).

Examples include:

```text
containerd
CRI-O
```

---

# kube-proxy

`kube-proxy` traditionally implements service networking behavior on nodes.

It helps implement:

```text
Service Virtual IP
Traffic Forwarding
Load Distribution
```

Modern Kubernetes networking implementations can use alternative mechanisms depending on the environment.

---

# CNI

CNI stands for:

```text
Container Network Interface
```

CNI plugins provide Pod networking.

Examples include:

```text
Calico
Cilium
Flannel
```

The selected CNI determines important networking behavior and capabilities.

---

# Cluster DNS

Kubernetes commonly uses CoreDNS for cluster DNS.

Example:

```text
service.namespace.svc.cluster.local
```

Applications can use DNS instead of hard-coded Pod IP addresses.

---

# CoreDNS

CoreDNS provides DNS resolution for Kubernetes services and other configured DNS records.

Example:

```text
payment-service.payments.svc.cluster.local
```

---

# Namespace Administration

Namespaces logically separate Kubernetes resources.

List namespaces:

```bash
kubectl get namespaces
```

Create namespace:

```bash
kubectl create namespace production
```

---

# Namespace Use Cases

Namespaces can separate:

```text
Development
Staging
Production
Security
Monitoring
Platform
```

They can also support:

```text
RBAC
Resource Quotas
Network Policies
Policy Management
```

---

# kubeconfig

`kubeconfig` contains configuration used by Kubernetes clients such as `kubectl`.

It can define:

```text
Clusters
Users
Contexts
```

---

# View kubeconfig

Run:

```bash
kubectl config view
```

Be careful when exposing kubeconfig because it may contain authentication credentials or references to credentials.

---

# Current Context

Check:

```bash
kubectl config current-context
```

---

# List Contexts

```bash
kubectl config get-contexts
```

---

# Switch Context

```bash
kubectl config use-context <context-name>
```

Always verify the active context before running destructive commands.

---

# Cluster Information

Run:

```bash
kubectl cluster-info
```

This can provide basic cluster endpoint information.

---

# Kubernetes Version

Check client and server versions:

```bash
kubectl version
```

The exact output depends on the kubectl version.

---

# Node Administration

List nodes:

```bash
kubectl get nodes
```

More details:

```bash
kubectl get nodes -o wide
```

---

# Describe Node

```bash
kubectl describe node <node-name>
```

Useful for investigating:

```text
Conditions
Capacity
Allocatable
Labels
Taints
Pods
Events
```

---

# Node Labels

Labels classify nodes.

Example:

```text
node-role.kubernetes.io/worker
```

Custom labels can represent:

```text
environment=production
disk=ssd
zone=us-east-1a
```

---

# Add a Label

Example:

```bash
kubectl label node <node-name> environment=production
```

---

# Node Conditions

Nodes can expose conditions such as:

```text
Ready
MemoryPressure
DiskPressure
PIDPressure
NetworkUnavailable
```

---

# Ready Condition

A healthy node commonly reports:

```text
Ready=True
```

Check:

```bash
kubectl get nodes
```

---

# Node Capacity

Capacity represents the total resources available on a node.

Examples:

```text
CPU
Memory
Ephemeral Storage
Pods
```

---

# Node Allocatable

Allocatable represents resources available for Kubernetes workloads after reserving resources for system components.

Conceptually:

```text
Node Capacity
      -
System Reservations
      -
Kubernetes Reservations
      =
Allocatable
```

---

# Node Resources

Inspect:

```bash
kubectl describe node <node-name>
```

Look for:

```text
Capacity
Allocatable
Allocated resources
```

---

# Node Cordon

Cordoning prevents new Pods from being scheduled onto a node.

```bash
kubectl cordon <node-name>
```

Existing Pods generally continue running.

---

# Node Drain

Draining prepares a node for maintenance by evicting or deleting eligible Pods according to Kubernetes disruption rules and command options.

Example:

```bash
kubectl drain <node-name> \
  --ignore-daemonsets
```

Use drain carefully in production.

---

# Node Uncordon

After maintenance:

```bash
kubectl uncordon <node-name>
```

The node can become eligible for new scheduling again.

---

# Cordon vs Drain

| Operation | Effect |
|---|---|
| Cordon | Prevents new scheduling |
| Drain | Evicts/deletes eligible workloads and marks node unschedulable |
| Uncordon | Allows scheduling again |

---

# Pod Eviction

Pod eviction can occur because of:

```text
Node Drain
Resource Pressure
Node Failure
Pod Disruption Budget
```

Eviction behavior depends on the workload and cluster configuration.

---

# Pod Disruption Budget

A Pod Disruption Budget (PDB) limits voluntary disruption.

Example:

```yaml
apiVersion: policy/v1
kind: PodDisruptionBudget

metadata:
  name: payment-pdb

spec:

  minAvailable: 2

  selector:

    matchLabels:
      app: payment
```

PDBs are useful during:

```text
Node Drain
Cluster Maintenance
Voluntary Disruptions
```

---

# Service Administration

List services:

```bash
kubectl get services
```

A Service provides stable networking for a group of Pods.

Common types:

```text
ClusterIP
NodePort
LoadBalancer
ExternalName
```

---

# Ingress

Ingress provides HTTP/HTTPS routing into Kubernetes services.

Architecture:

```text
Internet
   ↓
Ingress
   ↓
Service
   ↓
Pods
```

---

# Gateway API

Gateway API provides Kubernetes-native APIs for expressing more advanced traffic routing.

Conceptually:

```text
Gateway
   ↓
HTTPRoute
   ↓
Service
   ↓
Pods
```

---

# Storage Administration

Kubernetes storage administration includes:

```text
Persistent Volumes
Persistent Volume Claims
Storage Classes
CSI Drivers
```

---

# CSI

CSI stands for:

```text
Container Storage Interface
```

CSI drivers integrate Kubernetes with storage systems.

Architecture:

```text
Pod
 ↓
PVC
 ↓
PV
 ↓
CSI Driver
 ↓
Storage System
```

---

# Persistent Volume

A PersistentVolume represents storage available to the cluster.

```bash
kubectl get pv
```

---

# Persistent Volume Claim

A PVC requests storage.

```bash
kubectl get pvc -A
```

---

# Storage Class

StorageClasses define classes of storage and can enable dynamic provisioning.

```bash
kubectl get storageclass
```

---

# RBAC

Role-Based Access Control controls what authenticated identities can do.

Objects include:

```text
Role
ClusterRole
RoleBinding
ClusterRoleBinding
```

---

# Role

A Role defines permissions within a namespace.

Example:

```yaml
rules:

  - apiGroups:
      - ""

    resources:
      - pods

    verbs:
      - get
      - list
```

---

# ClusterRole

A ClusterRole can define permissions applicable across the cluster or reusable with namespace-scoped bindings.

---

# RoleBinding

RoleBinding associates a Role or ClusterRole with subjects within a namespace.

---

# ClusterRoleBinding

ClusterRoleBinding grants a ClusterRole to subjects at cluster scope.

Use cluster-wide permissions carefully.

---

# Service Accounts

Service Accounts provide identities for workloads running in Kubernetes.

Example:

```bash
kubectl get serviceaccounts -A
```

Applications can use Service Accounts when accessing the Kubernetes API or other integrated systems.

---

# Authentication

Authentication answers:

```text
Who are you?
```

Possible identity sources include:

```text
Certificates
OIDC
Cloud IAM
Service Accounts
External Identity Systems
```

---

# Authorization

Authorization answers:

```text
What are you allowed to do?
```

Kubernetes commonly uses:

```text
RBAC
```

for authorization.

---

# Admission

Admission happens after authentication and authorization but before an object is persisted.

Conceptually:

```text
Request
 ↓
Authentication
 ↓
Authorization
 ↓
Admission
 ↓
Persistence
```

Admission can:

```text
Validate
Mutate
Reject
```

requests.

---

# ConfigMaps

ConfigMaps store non-sensitive configuration.

```bash
kubectl get configmaps -A
```

Examples:

```text
Application Settings
Feature Flags
Configuration Files
```

---

# Secrets

Secrets are intended for sensitive configuration data.

Examples:

```text
Passwords
Tokens
Certificates
Keys
```

Protect Secrets with:

```text
RBAC
Encryption at Rest
External Secret Management
Least Privilege
```

---

# Resource Quotas

ResourceQuota limits resource consumption within a namespace.

Example:

```yaml
apiVersion: v1
kind: ResourceQuota

metadata:
  name: production-quota

spec:

  requests.cpu: "10"

  requests.memory: 20Gi

  limits.cpu: "20"

  limits.memory: 40Gi
```

---

# LimitRange

LimitRange can define default and allowed resource requests/limits within a namespace.

Example:

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

---

# Scheduling Administration

Administrators manage scheduling through:

```text
Node Selectors
Node Affinity
Pod Affinity
Pod Anti-Affinity
Taints
Tolerations
Topology Constraints
Priority Classes
Resource Requests
```

---

# Node Selector

Example:

```yaml
nodeSelector:

  disk: ssd
```

The Pod can only be scheduled onto nodes matching the label.

---

# Node Affinity

Node affinity provides more expressive node selection.

Example:

```yaml
affinity:

  nodeAffinity:

    requiredDuringSchedulingIgnoredDuringExecution:

      nodeSelectorTerms:

        - matchExpressions:

            - key: disk

              operator: In

              values:
                - ssd
```

---

# Taints

Taints repel Pods from nodes unless the Pods tolerate them.

Example:

```bash
kubectl taint nodes <node-name> dedicated=security:NoSchedule
```

---

# Tolerations

A matching Pod can tolerate the taint.

Example:

```yaml
tolerations:

  - key: dedicated

    operator: Equal

    value: security

    effect: NoSchedule
```

---

# Cluster Monitoring

Cluster administrators should monitor:

```text
Control Plane
Nodes
Pods
API Server
Scheduler
Controllers
etcd
Networking
Storage
Resource Usage
```

---

# Cluster Metrics

Important metrics include:

```text
CPU
Memory
Disk
Network
Pod Count
API Request Rate
API Latency
Scheduler Latency
Controller Errors
etcd Health
```

---

# Metrics Server

Metrics Server provides resource usage metrics commonly used by:

```text
kubectl top
Horizontal Pod Autoscaler
```

Check:

```bash
kubectl top nodes
```

and:

```bash
kubectl top pods -A
```

---

# Cluster Events

Events provide information about important cluster activity.

Run:

```bash
kubectl get events -A
```

Sort events by creation time:

```bash
kubectl get events -A \
  --sort-by=.lastTimestamp
```

Events are useful for troubleshooting but should not be treated as a long-term audit log.

---

# Cluster Logging

Cluster logging collects:

```text
Application Logs
Node Logs
Control Plane Logs
Container Runtime Logs
```

A logging architecture might be:

```text
Pods
 ↓
Logging Agent
 ↓
Log Backend
 ↓
Dashboard
```

---

# Audit Logging

Kubernetes Audit Logs record API activity.

They can answer:

```text
Who performed the action?
What resource?
What operation?
When?
From where?
```

Example:

```text
User
 ↓
DELETE Pod
 ↓
API Server
 ↓
Audit Event
```

---

# Why Audit Logs Matter

Audit logs are useful for:

```text
Security
Compliance
Forensics
Incident Response
Troubleshooting
```

---

# Control Plane Health

Administrators should monitor:

```text
API Server
etcd
Scheduler
Controller Manager
```

---

# API Server Health

The API Server should be monitored for:

```text
Availability
Latency
Error Rate
Request Rate
Resource Usage
```

---

# Scheduler Health

Monitor:

```text
Scheduling Latency
Scheduling Errors
Pending Pods
```

---

# Controller Manager Health

Monitor:

```text
Controller Errors
Reconciliation Delays
Queue Depth
```

depending on the metrics exposed by the deployment/version.

---

# etcd Health

Monitor:

```text
Availability
Disk Usage
Latency
Leader Changes
Database Size
Defragmentation Requirements
```

---

# etcd Backup

Because etcd contains critical cluster state, backups are essential.

A conceptual workflow:

```text
etcd
 ↓
Snapshot
 ↓
Secure Backup Storage
```

---

# etcd Restore

A restore operation can recover Kubernetes control-plane state after a disaster.

Restoration should be tested regularly.

Do not treat an untested backup as a reliable recovery plan.

---

# Kubernetes PKI

Kubernetes uses certificates for secure communication between components.

Important communication paths can include:

```text
kubectl → API Server
kubelet → API Server
API Server → kubelet
API Server → etcd
Control Plane Components
```

---

# Certificate Management

Administrators should monitor:

```text
Certificate Expiration
Certificate Rotation
Trust Configuration
CA Management
```

---

# Certificate Expiration

An expired certificate can cause:

```text
Authentication Failures
Component Communication Failures
Cluster Availability Issues
```

---

# Cluster Health Check

A basic workflow:

```text
1. Check Nodes
2. Check Pods
3. Check Events
4. Check API Server
5. Check Control Plane
6. Check etcd
7. Check Networking
8. Check Storage
9. Check Resource Usage
```

---

# Check Nodes

```bash
kubectl get nodes
```

Look for:

```text
Ready
NotReady
Unknown
```

---

# Check System Pods

```bash
kubectl get pods -A
```

Pay particular attention to:

```text
kube-system
```

and other infrastructure namespaces.

---

# Check Events

```bash
kubectl get events -A
```

Look for:

```text
FailedScheduling
FailedMount
BackOff
Unhealthy
Failed
```

---

# Check Resources

```bash
kubectl top nodes
```

and:

```bash
kubectl top pods -A
```

if Metrics Server is available.

---

# Resource Utilization

Monitor:

```text
CPU
Memory
Disk
Network
Pods
```

High utilization can result in:

```text
Scheduling Failures
Evictions
Performance Problems
Node Pressure
```

---

# Capacity Planning

Capacity planning estimates future resource requirements.

Consider:

```text
Current Usage
Growth Rate
Peak Traffic
Reserved Capacity
Failure Scenarios
```

---

# Cluster Scaling

Scaling can occur at multiple levels:

```text
Application Pods
Worker Nodes
Control Plane
Storage
Network
```

---

# Horizontal Pod Scaling

HPA increases or decreases the number of Pods.

```text
Load
 ↓
HPA
 ↓
More / Fewer Pods
```

---

# Cluster Autoscaler

Cluster Autoscaler adjusts worker node count based on scheduling requirements and configured policies.

Example:

```text
Pending Pods
     ↓
Insufficient Node Capacity
     ↓
Cluster Autoscaler
     ↓
New Node
```

---

# Manual Node Scaling

Administrators can add or remove nodes according to the platform or infrastructure tooling.

After adding a node:

```text
Node Joins
 ↓
kubelet Registers
 ↓
Node Ready
 ↓
Scheduler Can Use Node
```

---

# Cluster Upgrade

Cluster upgrades should follow a controlled process:

```text
Review Compatibility
       ↓
Backup
       ↓
Test
       ↓
Upgrade Control Plane
       ↓
Upgrade Nodes
       ↓
Validate
```

---

# Upgrade Preparation

Before upgrading:

```text
Check Kubernetes Version
Check API Deprecations
Check Add-ons
Check CNI
Check CSI
Check Ingress / Gateway
Check Operators
Check Helm Releases
Check Backups
```

---

# Node Upgrade

A typical node maintenance sequence is:

```text
Cordon
 ↓
Drain
 ↓
Upgrade
 ↓
Reboot if required
 ↓
Uncordon
 ↓
Validate
```

---

# Backup Strategy

Back up important components such as:

```text
etcd
Cluster Configuration
Persistent Application Data
Important Secrets
Infrastructure Configuration
```

The exact backup scope depends on the architecture.

---

# Restore Strategy

A recovery process should define:

```text
What to Restore
Order of Restoration
Recovery Time Objective
Recovery Point Objective
Validation
```

---

# Disaster Recovery

Disaster recovery planning should account for:

```text
Control Plane Failure
Node Failure
etcd Loss
Storage Failure
Network Failure
Region Failure
Credential Loss
```

---

# High Availability

A production control plane may use multiple control-plane nodes.

Example:

```text
              Load Balancer
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       API-1      API-2      API-3
          │         │         │
          └─────────┼─────────┘
                    ▼
                  etcd
```

The exact etcd topology depends on the Kubernetes distribution and deployment architecture.

---

# HA Requirements

High availability requires considering:

```text
API Server
etcd
Scheduler
Controller Manager
Networking
Load Balancing
Storage
DNS
```

---

# Security Administration

Cluster administrators must secure:

```text
API Server
etcd
Nodes
RBAC
Service Accounts
Secrets
Network
Images
Runtime
Audit Logs
```

---

# Least Privilege

Grant only the permissions required.

Avoid:

```text
cluster-admin
```

for ordinary workloads or users unless genuinely necessary.

---

# Network Policies

NetworkPolicies control allowed network communication.

Example:

```text
Frontend
   ↓
Backend
   ↓
Database
```

rather than:

```text
Everything
   ↓
Everything
```

---

# Pod Security

Apply appropriate Pod Security Standards and organizational policies.

Avoid unnecessarily privileged workloads.

---

# Image Security

Use:

```text
Trusted Registries
Image Scanning
Minimal Images
Pinned Versions
Signature Verification
```

where appropriate.

---

# Runtime Security

Monitor:

```text
Unexpected Processes
Privilege Escalation
Suspicious Network Activity
Container Behavior
```

---

# Cluster Administration Workflow

A useful daily workflow:

```text
Check Cluster
   ↓
Check Nodes
   ↓
Check System Pods
   ↓
Check Events
   ↓
Check Alerts
   ↓
Review Capacity
   ↓
Review Security
   ↓
Review Backups
```

---

# Daily Health Checklist

```text
☑ All nodes healthy
☑ System Pods healthy
☑ No critical events
☑ API Server healthy
☑ etcd healthy
☑ Scheduler healthy
☑ Controllers healthy
☑ DNS healthy
☑ CNI healthy
☑ CSI healthy
☑ Resource utilization normal
☑ No unexpected evictions
☑ No certificate warnings
☑ Monitoring healthy
☑ Logging healthy
```

---

# Weekly Administration Checklist

```text
☑ Review alerts
☑ Review resource usage
☑ Review capacity
☑ Review failed Pods
☑ Review node conditions
☑ Review audit logs
☑ Review RBAC
☑ Review image vulnerabilities
☑ Verify backups
☑ Review expiring certificates
☑ Review cluster add-ons
```

---

# Monthly Administration Checklist

```text
☑ Test restore process
☑ Review upgrade availability
☑ Review deprecated APIs
☑ Review capacity forecasts
☑ Review security policies
☑ Review network policies
☑ Review storage
☑ Review HA
☑ Review disaster recovery
☑ Review operational documentation
```

---

# Troubleshooting Framework

When something fails:

```text
Identify
   ↓
Scope
   ↓
Collect Evidence
   ↓
Check Events
   ↓
Check Logs
   ↓
Check Metrics
   ↓
Check Dependencies
   ↓
Apply Fix
   ↓
Validate
   ↓
Document
```

---

# Troubleshooting Pod Scheduling

Check:

```bash
kubectl describe pod <pod-name>
```

Look for:

```text
Events
FailedScheduling
Node Selector
Affinity
Taints
Resource Requests
```

---

# Troubleshooting Node NotReady

Run:

```bash
kubectl describe node <node-name>
```

Check:

```text
Conditions
Events
Kubelet
Network
Disk
Memory
Container Runtime
```

---

# Troubleshooting DNS

Check CoreDNS:

```bash
kubectl get pods -n kube-system
```

Check service:

```bash
kubectl get svc -n kube-system
```

Run a test Pod and perform DNS lookup.

---

# Troubleshooting Networking

Check:

```text
CNI Pods
NetworkPolicy
Service
Endpoints
DNS
Routes
Firewall
```

---

# Troubleshooting Storage

Check:

```bash
kubectl get pv
kubectl get pvc -A
kubectl get storageclass
```

Then inspect:

```bash
kubectl describe pvc <pvc-name>
```

---

# Troubleshooting API Access

Check:

```text
kubeconfig
Context
Credentials
RBAC
API Server
Network
```

Verify:

```bash
kubectl auth can-i get pods
```

---

# Troubleshooting RBAC

Use:

```bash
kubectl auth can-i get pods
```

For a specific identity:

```bash
kubectl auth can-i get pods \
  --as=<user>
```

Use impersonation only where authorized.

---

# Troubleshooting Admission

If an API request is rejected:

```text
Check Error
 ↓
Identify Admission Policy
 ↓
Inspect Configuration
 ↓
Check Validation / Mutation
```

Possible sources include:

```text
Validating Admission Policy
Admission Webhook
Pod Security
Other Policy Engines
```

---

# Troubleshooting Control Plane

Check:

```text
API Server
etcd
Scheduler
Controller Manager
```

Also inspect:

```text
System Logs
Events
Metrics
Certificates
Network
```

---

# Common Mistakes

## 1. Running Everything as cluster-admin

This violates least privilege.

---

## 2. Skipping Backups

Cluster state and application data require recovery planning.

---

## 3. Never Testing Restores

A backup is not useful if it cannot be restored.

---

## 4. Draining Nodes Without Planning

This can disrupt workloads.

Use:

```text
PDB
Replication
Capacity Planning
```

---

## 5. Ignoring Events

Events can provide immediate clues during troubleshooting.

---

## 6. Ignoring Node Pressure

Monitor:

```text
MemoryPressure
DiskPressure
PIDPressure
```

---

## 7. Exposing API Server or etcd

Restrict access.

---

## 8. Hard-Coding Secrets

Use proper secret management.

---

## 9. Ignoring Certificates

Expired certificates can cause severe failures.

---

## 10. Upgrading Without Testing

Validate compatibility first.

---

## 11. No Capacity Planning

A cluster can become saturated unexpectedly.

---

## 12. No Disaster Recovery Testing

Recovery must be practiced.

---

# Best Practices

### 1. Automate Cluster Administration

Use infrastructure-as-code and configuration management where appropriate.

---

### 2. Use Least Privilege

Keep administrative permissions tightly controlled.

---

### 3. Monitor Everything Important

Monitor:

```text
Control Plane
Nodes
Networking
Storage
Applications
```

---

### 4. Back Up Critical State

Especially:

```text
etcd
Application Data
Configuration
```

---

### 5. Test Restores

Regularly validate:

```text
Backup
Restore
Application Recovery
```

---

### 6. Plan Upgrades

Maintain:

```text
Version Matrix
Compatibility Checks
Rollback Plan
Backup
Testing
```

---

### 7. Use Pod Disruption Budgets

Protect critical replicated workloads during maintenance.

---

### 8. Secure the API

Use:

```text
Authentication
Authorization
Admission
TLS
Network Restrictions
```

---

### 9. Monitor Certificates

Automate expiry detection and rotation where possible.

---

### 10. Document Runbooks

Create procedures for:

```text
Node Failure
API Failure
etcd Failure
DNS Failure
Network Failure
Storage Failure
Upgrade
Restore
```

---

# Hands-on Lab 1 – Cluster Inspection

Run:

```bash
kubectl cluster-info
kubectl get nodes
kubectl get pods -A
kubectl get namespaces
```

Document the cluster architecture.

---

# Hands-on Lab 2 – Node Administration

Select a disposable worker node.

Run:

```bash
kubectl cordon <node-name>
```

Verify scheduling behavior.

Then:

```bash
kubectl uncordon <node-name>
```

---

# Hands-on Lab 3 – Node Drain

On a disposable environment:

```bash
kubectl drain <node-name> \
  --ignore-daemonsets
```

Observe:

```text
Pod Eviction
Scheduling
PDB Behavior
```

---

# Hands-on Lab 4 – Node Labels

Add:

```bash
kubectl label node <node-name> disk=ssd
```

Create a Pod using:

```yaml
nodeSelector:
  disk: ssd
```

Verify placement.

---

# Hands-on Lab 5 – Taints and Tolerations

Taint a test node:

```bash
kubectl taint nodes \
  <node-name> \
  dedicated=testing:NoSchedule
```

Create:

```text
Pod without toleration
```

and:

```text
Pod with toleration
```

Compare scheduling behavior.

---

# Hands-on Lab 6 – Resource Quota

Create a namespace.

Apply a ResourceQuota.

Deploy workloads exceeding the quota.

Observe:

```text
Admission
Resource Accounting
Pod Creation Failure
```

---

# Hands-on Lab 7 – LimitRange

Create a LimitRange.

Deploy a container without explicit resources.

Observe the default requests and limits.

---

# Hands-on Lab 8 – RBAC

Create:

```text
ServiceAccount
Role
RoleBinding
```

Allow:

```text
get/list pods
```

Test:

```bash
kubectl auth can-i get pods
```

---

# Hands-on Lab 9 – Audit Investigation

Perform an authorized Kubernetes API action.

Inspect audit records.

Identify:

```text
User
Operation
Resource
Timestamp
```

---

# Hands-on Lab 10 – Cluster DNS

Deploy a test Pod.

Resolve:

```text
kubernetes.default.svc.cluster.local
```

Verify CoreDNS functionality.

---

# Hands-on Lab 11 – Service Networking

Create:

```text
Deployment
Service
```

Access the Service from another Pod.

Verify:

```text
DNS
Service IP
Endpoint
Pod
```

---

# Hands-on Lab 12 – Persistent Storage

Create:

```text
StorageClass
PVC
Pod
```

Verify that the Pod can use persistent storage.

---

# Hands-on Lab 13 – Node Failure Simulation

In a disposable environment, simulate a node outage.

Observe:

```text
Node Condition
Pod Behavior
Replica Replacement
Scheduling
Events
```

---

# Hands-on Lab 14 – Cluster Monitoring

Install or use an existing monitoring stack.

Monitor:

```text
CPU
Memory
Disk
Pods
Nodes
API Server
```

---

# Hands-on Lab 15 – Cluster Events

Generate a controlled scheduling failure.

Run:

```bash
kubectl get events -A
```

Identify the failure reason.

---

# Hands-on Lab 16 – Certificate Inspection

Inspect the cluster's certificate configuration using the administration tools appropriate for your Kubernetes distribution.

Identify:

```text
Certificate Authority
Component Certificates
Expiration
```

---

# Hands-on Lab 17 – etcd Backup

In a test cluster where you have appropriate administrative access:

```text
Create etcd snapshot
```

Store it securely.

Document the procedure.

---

# Hands-on Lab 18 – etcd Restore

Use a disposable test cluster.

Practice:

```text
Backup
 ↓
Restore
 ↓
Control Plane Validation
```

Never experiment with restore procedures on production without an approved recovery plan.

---

# Hands-on Lab 19 – Upgrade Simulation

Create a test cluster.

Document:

```text
Current Version
Target Version
Compatibility
Backup
Upgrade
Validation
```

---

# Hands-on Lab 20 – Full Administration Exercise

Build a Kubernetes environment containing:

```text
Multiple Nodes
Namespaces
RBAC
Resource Quotas
Network Policies
Storage
Monitoring
Logging
Ingress / Gateway
```

Then perform:

```text
Node Cordon
Node Drain
Node Recovery
Application Scaling
Backup
Health Check
Troubleshooting
```

---

# Quick Revision

## Cluster Administration

```text
Operating and maintaining a Kubernetes cluster
```

---

## Control Plane

```text
Manages cluster state
```

---

## API Server

```text
Primary Kubernetes API endpoint
```

---

## etcd

```text
Persistent distributed key-value store for cluster state
```

---

## Scheduler

```text
Assigns Pods to suitable nodes
```

---

## Controller Manager

```text
Runs reconciliation controllers
```

---

## kubelet

```text
Manages Pods on a node
```

---

## Container Runtime

```text
Runs containers
```

---

## kube-proxy

```text
Implements service networking behavior on nodes in applicable configurations
```

---

## CNI

```text
Provides container networking
```

---

## CoreDNS

```text
Provides Kubernetes DNS
```

---

## Cordon

```text
Prevents new Pods from scheduling on a node
```

---

## Drain

```text
Evicts/deletes eligible workloads from a node for maintenance
```

---

## Uncordon

```text
Allows scheduling on the node again
```

---

## RBAC

```text
Controls authorization
```

---

## ResourceQuota

```text
Limits namespace resource consumption
```

---

## LimitRange

```text
Defines resource defaults and constraints
```

---

## PDB

```text
Limits voluntary disruption of replicated workloads
```

---

## Audit Log

```text
Records Kubernetes API activity
```

---

## kubeconfig

```text
Client configuration containing clusters, users, and contexts
```

---

# Essential Commands

Cluster information:

```bash
kubectl cluster-info
```

Cluster version:

```bash
kubectl version
```

Current context:

```bash
kubectl config current-context
```

List contexts:

```bash
kubectl config get-contexts
```

Switch context:

```bash
kubectl config use-context <context>
```

List nodes:

```bash
kubectl get nodes
```

Detailed nodes:

```bash
kubectl get nodes -o wide
```

Describe node:

```bash
kubectl describe node <node>
```

Node resource usage:

```bash
kubectl top nodes
```

Pod resource usage:

```bash
kubectl top pods -A
```

All Pods:

```bash
kubectl get pods -A
```

System Pods:

```bash
kubectl get pods -n kube-system
```

Events:

```bash
kubectl get events -A
```

Namespaces:

```bash
kubectl get namespaces
```

Services:

```bash
kubectl get svc -A
```

Ingress:

```bash
kubectl get ingress -A
```

Gateway resources:

```bash
kubectl get gateway -A
```

Persistent Volumes:

```bash
kubectl get pv
```

Persistent Volume Claims:

```bash
kubectl get pvc -A
```

StorageClasses:

```bash
kubectl get storageclass
```

Service Accounts:

```bash
kubectl get serviceaccounts -A
```

Roles:

```bash
kubectl get roles -A
```

ClusterRoles:

```bash
kubectl get clusterroles
```

RoleBindings:

```bash
kubectl get rolebindings -A
```

ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

Check authorization:

```bash
kubectl auth can-i get pods
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

Label node:

```bash
kubectl label node <node> key=value
```

Taint node:

```bash
kubectl taint node <node> key=value:NoSchedule
```

---

# Interview Questions

## Basic

- What is Kubernetes cluster administration?
- What are the major Kubernetes control-plane components?
- What is the role of the API Server?
- What is etcd?
- What does the scheduler do?
- What does the Controller Manager do?
- What is the kubelet?
- What is a container runtime?
- What is kube-proxy?
- What is CNI?
- What is CoreDNS?
- What is kubeconfig?
- What is a Kubernetes context?
- What is a namespace?
- What is node capacity?
- What is node allocatable?
- What is cordon?
- What is drain?
- What is uncordon?
- What is a Pod Disruption Budget?
- What is RBAC?
- What is a ResourceQuota?
- What is a LimitRange?
- What are Kubernetes audit logs?

---

## Intermediate

- Explain the complete Kubernetes control-plane architecture.
- How does `kubectl` communicate with the cluster?
- What happens when you create a Deployment?
- How does the scheduler select a node?
- What happens when a node becomes NotReady?
- What is the difference between cordon and drain?
- Why are PDBs important?
- How do you troubleshoot a node?
- How do you troubleshoot a Pending Pod?
- How do you troubleshoot DNS?
- How do you troubleshoot a Service?
- How do you troubleshoot a PVC?
- How do you troubleshoot RBAC?
- How do you check cluster resource utilization?
- How do you monitor etcd?
- How do you back up etcd?
- How do you perform a Kubernetes upgrade?
- What should be checked before upgrading Kubernetes?
- How do you manage Kubernetes certificates?
- How do you secure the Kubernetes API Server?

---

## Advanced

- Design a highly available Kubernetes control plane.
- Explain how etcd contributes to cluster availability.
- How would you recover a Kubernetes cluster after etcd corruption?
- How would you perform a zero/minimal-downtime node maintenance operation?
- How would you design cluster capacity planning?
- How would you troubleshoot a cluster where Pods are Pending?
- How would you troubleshoot a cluster where all Nodes are NotReady?
- How would you investigate API Server latency?
- How would you investigate etcd latency?
- How would you design Kubernetes audit logging?
- How would you secure a production Kubernetes cluster?
- How would you implement least-privilege administration?
- How would you plan a Kubernetes version upgrade?
- How would you design disaster recovery for a production cluster?
- How would you manage multiple Kubernetes clusters?
- How would you investigate a suspected Kubernetes security incident?

---

# Interview Scenario 1

### Question

> What happens when you run `kubectl apply -f deployment.yaml`?

### Answer

Conceptually:

```text
kubectl
   ↓
API Server
   ↓
Authentication
   ↓
Authorization
   ↓
Admission
   ↓
Object Stored
   ↓
Controller
   ↓
ReplicaSet
   ↓
Pods
   ↓
Scheduler
   ↓
Node
   ↓
kubelet
   ↓
Container Runtime
```

The API Server accepts and persists the desired state, controllers reconcile it, the scheduler assigns Pods to nodes, and kubelets ensure the assigned Pods run.

---

# Interview Scenario 2

### Question

> A Pod is stuck in Pending. How do you troubleshoot it?

### Answer

Run:

```bash
kubectl describe pod <pod-name>
```

Inspect:

```text
Events
FailedScheduling
Resource Requests
Node Selector
Affinity
Taints
Tolerations
Topology Constraints
```

Then check:

```bash
kubectl get nodes
kubectl describe nodes
```

The most important first clue is usually the Pod's scheduling events.

---

# Interview Scenario 3

### Question

> A Kubernetes node is NotReady. What do you check?

### Answer

Start with:

```bash
kubectl describe node <node-name>
```

Check:

```text
Node Conditions
Events
MemoryPressure
DiskPressure
PIDPressure
Network
Kubelet
Container Runtime
```

Then inspect node-level logs and system services using the appropriate access method for the cluster.

---

# Interview Scenario 4

### Question

> What is the difference between cordon and drain?

### Answer

Cordon:

```text
Prevents new Pods from being scheduled
```

Drain:

```text
Makes the node unschedulable
+
Evicts/deletes eligible workloads
```

Typical maintenance:

```text
Cordon
 ↓
Drain
 ↓
Maintenance
 ↓
Uncordon
```

---

# Interview Scenario 5

### Question

> Why is etcd so important?

### Answer

etcd stores Kubernetes cluster state.

For example:

```text
Pods
Deployments
Services
Secrets
ConfigMaps
Nodes
RBAC
```

Therefore, protecting etcd with:

```text
HA
Backups
TLS
Access Control
Monitoring
```

is critical.

---

# Interview Scenario 6

### Question

> How would you safely maintain a production node?

### Answer

First ensure sufficient workload redundancy.

Then:

```text
Check PDB
 ↓
Check Capacity
 ↓
Cordon
 ↓
Drain
 ↓
Perform Maintenance
 ↓
Validate Node
 ↓
Uncordon
```

Finally verify:

```text
Pods
Services
Application Health
Alerts
```

---

# Interview Scenario 7

### Question

> How would you secure Kubernetes administration?

### Answer

Use:

```text
Strong Authentication
RBAC
Least Privilege
TLS
Audit Logging
Network Restrictions
Secure kubeconfig
Secret Management
Admission Policies
Pod Security
Image Security
```

Avoid distributing:

```text
cluster-admin
```

credentials unnecessarily.

---

# Interview Scenario 8

### Question

> What would you monitor on a Kubernetes cluster?

### Answer

Monitor:

```text
Control Plane
Nodes
Pods
CPU
Memory
Disk
Network
API Server
etcd
Scheduler
Controllers
DNS
CNI
CSI
Events
Audit Logs
```

Also monitor application-level:

```text
Latency
Errors
Traffic
Saturation
```

---

# Interview Scenario 9

### Question

> How would you prepare for a Kubernetes upgrade?

### Answer

Use:

```text
Version Compatibility Review
 ↓
API Deprecation Review
 ↓
Backup
 ↓
Test Environment
 ↓
Upgrade Plan
 ↓
Control Plane Upgrade
 ↓
Node Upgrade
 ↓
Validation
 ↓
Rollback / Recovery Plan
```

Also validate:

```text
CNI
CSI
Ingress / Gateway
Operators
Monitoring
Logging
Security Policies
```

---

# Interview Scenario 10

### Question

> How would you design a production Kubernetes administration strategy?

### Answer

Build around:

```text
High Availability
+
Security
+
Monitoring
+
Backup
+
Disaster Recovery
+
Automation
+
Capacity Planning
+
Controlled Upgrades
```

A simplified architecture:

```text
                    Load Balancer
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Control-1   Control-2   Control-3
             │           │           │
             └───────────┼───────────┘
                         ▼
                        etcd
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
     Worker-1         Worker-2         Worker-3
        │                │                │
     kubelet          kubelet          kubelet
        │                │                │
     Runtime          Runtime          Runtime
```

Add:

```text
Monitoring
Logging
Audit
Backup
RBAC
Network Policies
Security Controls
```

---

# Production Cluster Administration Checklist

```text
☑ Control plane HA
☑ etcd HA
☑ etcd backups
☑ Restore testing
☑ API Server monitoring
☑ Scheduler monitoring
☑ Controller monitoring
☑ Node monitoring
☑ CNI health
☑ CoreDNS health
☑ CSI health
☑ Resource monitoring
☑ Capacity planning
☑ RBAC
☑ Least privilege
☑ Audit logging
☑ Network policies
☑ Pod security
☑ Image security
☑ Certificate monitoring
☑ Secret management
☑ Upgrade strategy
☑ Disaster recovery
☑ Maintenance runbooks
☑ Incident response procedures
```

---

# Chapter Summary

Cluster administration is responsible for maintaining the health, security, availability, and performance of Kubernetes infrastructure.

The core control-plane architecture is:

```text
API Server
    │
    ├── etcd
    ├── Scheduler
    ├── Controller Manager
    └── Cloud Controller Manager
```

Worker nodes contain:

```text
kubelet
Container Runtime
kube-proxy
```

Cluster administration covers:

```text
Nodes
Networking
Storage
Scheduling
Security
Monitoring
Logging
Backups
Upgrades
High Availability
Disaster Recovery
```

Important operational commands include:

```bash
kubectl get nodes
kubectl describe node
kubectl cordon
kubectl drain
kubectl uncordon
kubectl top
kubectl get events
kubectl auth can-i
```

A safe maintenance workflow is:

```text
Plan
 ↓
Check Capacity
 ↓
Check PDB
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

A production administrator should treat the Kubernetes cluster itself as a critical production system.

The most important principle is:

> **Kubernetes cluster administration is not simply running `kubectl` commands; it is the disciplined management of cluster availability, security, capacity, networking, storage, upgrades, backups, and operational recovery.**

---

## Next Chapter

# Chapter 66 – Backup & Restore

Topics will include:

- Kubernetes Backup Fundamentals
- Why Backup Matters
- Backup vs Snapshot
- Recovery
- Disaster Recovery
- RPO
- RTO
- Kubernetes State
- etcd Backup
- etcd Snapshots
- etcd Restore
- Kubernetes Resource Backup
- Persistent Volume Backup
- Application Data Backup
- Configuration Backup
- Secret Backup
- Namespace Backup
- Cluster Backup
- Volume Snapshots
- CSI Volume Snapshots
- Storage Snapshots
- Velero
- Backup Architecture
- Backup Locations
- Object Storage
- S3-Compatible Storage
- Backup Encryption
- Backup Compression
- Incremental Backup
- Full Backup
- Scheduled Backup
- Retention
- Backup Policies
- Backup Verification
- Restore Testing
- Namespace Restore
- Application Restore
- Cluster Restore
- etcd Disaster Recovery
- Persistent Data Recovery
- Cross-Cluster Restore
- Cross-Region Recovery
- Disaster Recovery Architecture
- High Availability vs Backup
- Backup Security
- RBAC
- Encryption
- Immutable Backups
- Ransomware Protection
- Air-Gapped Backups
- Backup Monitoring
- Backup Failures
- Restore Failures
- Troubleshooting
- Production Backup Strategy
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---