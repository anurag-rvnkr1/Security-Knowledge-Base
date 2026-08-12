# Chapter 82 – Operators

## Overview

A Kubernetes Operator is a software component that extends Kubernetes to automate the management of a specific application, service, or operational process.

The Operator pattern combines:

```text
Custom Resources
+
Controllers
+
Reconciliation Logic
```

The basic idea is:

```text
User
 ↓
Custom Resource
 ↓
Kubernetes API
 ↓
Operator Controller
 ↓
Reconciliation
 ↓
Application / Infrastructure
```

Instead of requiring an administrator to manually manage a complex application, an Operator can automate tasks such as:

```text
Installation
Configuration
Scaling
Backup
Recovery
Upgrades
Failover
Health Management
```

Examples of workloads commonly managed by Operators include:

```text
Databases
Message Queues
Monitoring Systems
Storage Systems
Backup Systems
Distributed Applications
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes Operators
- What is an Operator?
- Why Operators?
- Operator Pattern
- Kubernetes API Extensions
- Controllers
- Reconciliation
- Desired State
- Actual State
- Custom Resources
- Custom Resource Definitions
- CRDs
- Custom Controllers
- Operator Lifecycle
- Operator Architecture
- Operator SDK
- Kubebuilder
- Controller Runtime
- Watchers
- Events
- Reconciliation Loops
- Finalizers
- Owner References
- Status Conditions
- Spec vs Status
- API Design
- Versioning
- Conversion
- Webhooks
- Admission Webhooks
- Mutating Webhooks
- Validating Webhooks
- Leader Election
- RBAC
- Operator Security
- Operator Deployment
- Operator Lifecycle Manager
- OLM
- OperatorHub
- Helm-Based Operators
- Ansible-Based Operators
- Go-Based Operators
- Stateful Application Operators
- Database Operators
- Backup Operators
- Monitoring Operators
- Storage Operators
- Multi-Cluster Operators
- Operator Dependencies
- Operator Upgrades
- Operator Rollbacks
- Operator Testing
- Unit Testing
- Integration Testing
- End-to-End Testing
- Operator Observability
- Logging
- Metrics
- Events
- Failure Handling
- Reconciliation Failures
- Idempotency
- Production Best Practices
- Common Mistakes
- Troubleshooting
- Hands-on Labs
- Quick Revision
- Interview Questions

---

# What Is an Operator?

An Operator is a Kubernetes application that uses the Kubernetes API to automate operational knowledge.

A simplified model is:

```text
Custom Resource
      ↓
Operator
      ↓
Controller
      ↓
Reconciliation
      ↓
Managed Resources
```

---

# Why Operators?

Kubernetes already manages basic workloads well.

For example:

```text
Deployment
Service
ConfigMap
Secret
```

But complex applications often require domain-specific operations.

A database may require:

```text
Backup
Restore
Replication
Failover
Schema Management
Scaling
Version Upgrades
```

An Operator can automate these tasks.

---

# Human Knowledge vs Operator

Without an Operator:

```text
Database
 ↓
Administrator
 ↓
Manual Procedures
```

With an Operator:

```text
Database Custom Resource
 ↓
Operator
 ↓
Automated Procedures
```

---

# Operator Pattern

The Operator pattern extends Kubernetes with domain-specific automation.

Conceptually:

```text
Kubernetes API
      │
      ├── Built-in Resources
      │
      └── Custom Resources
               │
               ▼
            Operator
               │
               ▼
       Managed Application
```

---

# Controllers

A controller continuously observes Kubernetes resources and attempts to make actual state match desired state.

The basic loop is:

```text
Observe
  ↓
Compare
  ↓
Act
  ↓
Observe Again
```

---

# Reconciliation

Reconciliation is the process of making:

```text
Actual State
```

match:

```text
Desired State
```

Example:

```text
Desired:
3 Database Replicas

Actual:
2 Database Replicas

        ↓

Operator Reconciles

        ↓

3 Database Replicas
```

---

# Desired State

The desired state is commonly represented by the resource:

```yaml
spec:
```

Example:

```yaml
spec:
  replicas: 3
```

---

# Actual State

Actual state is represented by:

```text
Kubernetes Resources
+
Application State
+
Observed Conditions
```

---

# Spec vs Status

A common Kubernetes API pattern is:

```yaml
spec:
  replicas: 3

status:
  availableReplicas: 3
  phase: Ready
```

---

# `spec`

The `spec` describes:

```text
What the user wants
```

---

# `status`

The `status` describes:

```text
What the system observes
```

---

# Custom Resources

A Custom Resource is an extension of the Kubernetes API.

Example:

```yaml
apiVersion: databases.example.com/v1
kind: PostgreSQLCluster
metadata:
  name: production-db
spec:
  replicas: 3
```

Kubernetes can store this object just like other API resources.

---

# Custom Resource Definition

A Custom Resource Definition, or CRD, defines a new Kubernetes API resource.

Conceptually:

```text
CRD
 ↓
Defines API
 ↓
Custom Resource
 ↓
Operator Manages It
```

---

# CRD Example

A simplified CRD:

```yaml
apiVersion: apiextensions.k8s.io/v1
kind: CustomResourceDefinition
metadata:
  name: postgresclusters.databases.example.com
spec:
  group: databases.example.com
  names:
    kind: PostgreSQLCluster
    plural: postgresclusters
    singular: postgresqlcluster
  scope: Namespaced
  versions:
    - name: v1
      served: true
      storage: true
      schema:
        openAPIV3Schema:
          type: object
```

---

# Creating a Custom Resource

After the CRD exists:

```yaml
apiVersion: databases.example.com/v1
kind: PostgreSQLCluster
metadata:
  name: production-db
spec:
  replicas: 3
```

The Operator watches this resource.

---

# Custom Resource Lifecycle

```text
Create CR
   ↓
Operator Detects Event
   ↓
Reconcile
   ↓
Create / Update Resources
   ↓
Observe
   ↓
Update Status
```

---

# Operator Architecture

A simplified Operator architecture:

```text
                Kubernetes API
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Custom Resource        Other Resources
          │                     │
          └──────────┬──────────┘
                     ▼
                Controller
                     │
                Reconcile()
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
      Deployment   Service     Secret
          │          │          │
          └──────────┼──────────┘
                     ▼
                  Status
```

---

# Operator Components

A typical Operator contains:

```text
CRD
Controller
Reconciliation Logic
RBAC
Deployment
Optional Webhooks
Optional Metrics
```

---

# Watchers

A controller watches resources for changes.

Possible events:

```text
Create
Update
Delete
```

---

# Watch Relationship

Example:

```text
PostgreSQLCluster
       │
       ▼
Deployment
```

When the Custom Resource changes, the Operator reconciles the related Deployment.

---

# Event-Driven Reconciliation

A simplified flow:

```text
User Changes CR
      ↓
Kubernetes API
      ↓
Event
      ↓
Controller Queue
      ↓
Reconcile
```

---

# Reconciliation Loop

A good reconciliation loop is:

```text
Deterministic
Idempotent
Retryable
Observable
```

---

# Idempotency

Idempotency means running the reconciliation multiple times produces the same desired result.

Example:

```text
Reconcile
 ↓
Ensure Deployment Exists

Reconcile Again
 ↓
Deployment Already Correct
 ↓
No Unnecessary Change
```

---

# Why Idempotency Matters

Controllers can receive repeated events.

Therefore reconciliation should safely handle:

```text
Duplicate Events
Retries
Restarts
Temporary Failures
```

---

# Example Reconciliation Logic

Conceptually:

```text
Read Custom Resource
        ↓
Check Deployment
        ↓
Does it exist?
   ┌────┴────┐
   │         │
  No        Yes
   │         │
Create      Compare
   │         │
   └────┬────┘
        ▼
     Reconcile
        ↓
 Update Status
```

---

# Controller Runtime

Many Kubernetes Operators written in Go use:

```text
controller-runtime
```

It provides common controller functionality.

Conceptually:

```text
Controller
+
Client
+
Cache
+
Manager
+
Reconciler
```

---

# Operator SDK

Operator SDK is a framework/toolkit for building Operators.

It can help with:

```text
Project Scaffolding
Controller Development
CRD Generation
Testing
Packaging
```

---

# Kubebuilder

Kubebuilder is a framework for building Kubernetes APIs and controllers, especially in Go.

Typical architecture:

```text
Kubebuilder
 ↓
API Types
 ↓
CRD
 ↓
Controller
 ↓
Reconciliation
```

---

# Operator SDK vs Kubebuilder

Both can be used to develop Kubernetes Operators.

A simplified distinction:

| Operator SDK | Kubebuilder |
|---|---|
| Operator-focused toolkit | Kubernetes API/controller framework |
| Supports multiple development approaches | Strong Go/controller-runtime workflow |
| Packaging and lifecycle tooling | Strong API/controller scaffolding |
| Built around Kubernetes operator development | Built around Kubernetes controller development |

The best choice depends on the Operator architecture and ecosystem.

---

# Go-Based Operators

Go is widely used for Kubernetes controllers.

Typical project:

```text
api/
controllers/
config/
cmd/
```

---

# Ansible-Based Operators

Operator SDK has supported Ansible-based Operator development.

This can be useful when existing operational automation is already expressed through Ansible.

---

# Helm-Based Operators

Operators can also use Helm-based approaches.

Conceptually:

```text
Custom Resource
      ↓
Operator
      ↓
Helm Chart
      ↓
Kubernetes Resources
```

This can simplify some application packaging scenarios.

---

# Operator Lifecycle Manager

Operator Lifecycle Manager, commonly called OLM, provides mechanisms for managing the lifecycle of Operators in Kubernetes environments.

It can help with:

```text
Installation
Version Management
Dependency Management
Upgrade
```

---

# OperatorHub

OperatorHub provides a catalog of Operators.

When using third-party Operators:

```text
Review
 ↓
Security Assessment
 ↓
Version Selection
 ↓
Permissions Review
 ↓
Test
 ↓
Production Approval
```

Do not blindly install an Operator just because it is available in a catalog.

---

# Operator Deployment

An Operator usually runs as a Kubernetes workload.

Example:

```text
Deployment
   ↓
Operator Pod
   ↓
Kubernetes API
```

---

# Operator Namespace

An Operator may be:

```text
Namespace-Scoped
```

or:

```text
Cluster-Wide
```

depending on what it needs to manage.

---

# Namespace-Scoped Operator

Manages resources in one or selected namespaces.

Advantages:

```text
Smaller Blast Radius
Simpler Permissions
```

---

# Cluster-Wide Operator

May watch or manage resources across the cluster.

This can be necessary for platform-level Operators.

However, it increases:

```text
Permissions
Blast Radius
Security Responsibility
```

---

# Operator RBAC

An Operator needs permissions to manage resources.

Example:

```text
get
list
watch
create
update
patch
delete
```

Only grant what is required.

---

# Operator Security

An Operator is highly privileged software.

If compromised, it may be able to modify many Kubernetes resources.

Therefore secure:

```text
Operator Image
Operator RBAC
Operator Dependencies
Operator Configuration
Operator Network Access
Operator Credentials
```

---

# Least Privilege

Avoid:

```yaml
kind: ClusterRole
rules:
  - apiGroups: ["*"]
    resources: ["*"]
    verbs: ["*"]
```

unless there is a compelling, documented reason.

Prefer narrowly scoped permissions.

---

# Operator ServiceAccount

The Operator should run with a dedicated ServiceAccount.

Example:

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: database-operator
```

---

# Operator RBAC Flow

```text
Operator Pod
    ↓
ServiceAccount
    ↓
Role / ClusterRole
    ↓
RoleBinding / ClusterRoleBinding
    ↓
Kubernetes API
```

---

# Leader Election

When multiple Operator replicas run, they may use leader election.

Conceptually:

```text
Operator A ─┐
Operator B ─┼─→ Leader Election
Operator C ─┘
                ↓
             Leader
                ↓
          Reconciliation
```

This helps prevent multiple replicas from performing conflicting active reconciliation.

---

# Operator High Availability

Production Operators may run multiple replicas.

Example:

```yaml
spec:
  replicas: 2
```

But simply running multiple replicas does not automatically guarantee safe active reconciliation; leader election and controller design matter.

---

# Operator Events

Operators can publish Kubernetes Events.

Example:

```text
PostgreSQLCluster
      ↓
Backup Started
      ↓
Kubernetes Event
```

Events can help operators understand what the controller is doing.

---

# Status Conditions

Modern Kubernetes APIs commonly expose structured conditions.

Example:

```yaml
status:
  conditions:
    - type: Ready
      status: "True"
      reason: ClusterReady
      message: Cluster is operational
```

---

# Condition Types

Examples:

```text
Ready
Progressing
Degraded
Available
```

The exact conditions depend on the API.

---

# Status Updates

The Operator should update status when important state changes.

Example:

```text
Desired:
3 replicas

Observed:
2 replicas

Status:
Progressing
```

---

# Finalizers

Finalizers allow controllers to perform cleanup before a resource is fully deleted.

Conceptually:

```text
Delete Request
      ↓
Finalizer Present
      ↓
Cleanup
      ↓
Remove Finalizer
      ↓
Resource Deleted
```

---

# Why Finalizers?

Suppose an Operator creates an external database.

Deleting the Custom Resource may need to trigger:

```text
External Resource Cleanup
```

before the Kubernetes object disappears.

---

# Finalizer Example

Conceptually:

```yaml
metadata:
  finalizers:
    - database.example.com/cleanup
```

---

# Owner References

Owner references connect managed resources to their parent resource.

Example:

```text
PostgreSQLCluster
       │
       ├── Deployment
       ├── Service
       └── ConfigMap
```

The child resources can reference the parent as an owner.

---

# Garbage Collection

Kubernetes can use owner references for garbage collection.

This can help automatically remove dependent resources when their owner is deleted, subject to Kubernetes ownership rules.

---

# Owner Reference vs Finalizer

| Owner Reference | Finalizer |
|---|---|
| Represents ownership | Blocks deletion until cleanup |
| Supports garbage collection | Allows custom cleanup |
| Declarative relationship | Controller-controlled deletion workflow |

They solve different problems.

---

# API Design

A good Custom Resource API should be:

```text
Clear
Predictable
Versioned
Validated
Backward-Compatible
```

---

# API Group

Example:

```text
databases.example.com
```

---

# API Version

Example:

```text
v1
```

Full API:

```text
databases.example.com/v1
```

---

# Kind

Example:

```text
PostgreSQLCluster
```

---

# Resource Naming

Plural resource:

```text
postgresqlclusters
```

Kind:

```text
PostgreSQLCluster
```

---

# API Versioning

An Operator may evolve:

```text
v1alpha1
 ↓
v1beta1
 ↓
v1
```

Production APIs should have a carefully planned compatibility strategy.

---

# Conversion

When multiple versions of a CRD exist, conversion mechanisms can translate between versions.

Conceptually:

```text
v1alpha1
    ↓
Conversion
    ↓
v1
```

---

# Storage Version

A CRD identifies one version as the storage version.

The Operator and API server must handle version compatibility correctly.

---

# Webhooks

Operators may use webhooks for:

```text
Validation
Mutation
Conversion
```

---

# Validating Webhook

A validating webhook checks whether a request is acceptable.

Example:

```text
replicas = -1
```

The webhook can reject it.

---

# Mutating Webhook

A mutating webhook modifies an incoming resource.

Example:

```text
User Creates Pod
       ↓
Webhook
       ↓
Adds Security Configuration
       ↓
Kubernetes
```

---

# Admission Webhooks

Admission webhooks operate during Kubernetes API admission.

They can enforce or modify policy.

---

# Operator Webhook Architecture

```text
User
 ↓
Kubernetes API
 ↓
Admission Webhook
 ↓
Validation / Mutation
 ↓
API Server
 ↓
Operator
```

---

# Operator Reconciliation

A controller typically:

```text
1. Read Resource
2. Read Current State
3. Calculate Desired State
4. Create/Update Resources
5. Update Status
6. Requeue if Necessary
```

---

# Requeue

A controller may request another reconciliation when:

```text
External State May Change
Waiting for Resource
Retry Needed
```

---

# Reconciliation Failure

If reconciliation fails:

```text
Error
 ↓
Log
 ↓
Return Error
 ↓
Controller Retries
```

A controller should implement safe retry behavior.

---

# Exponential Backoff

Repeated failures should not cause uncontrolled API traffic.

Controllers can use retry/backoff mechanisms.

---

# External Systems

Operators may manage external systems:

```text
Cloud Resources
Databases
DNS
Storage
Message Queues
```

---

# External Resource Management

Example:

```text
Custom Resource
      ↓
Operator
      ↓
Cloud API
      ↓
Load Balancer
```

The Operator then reports the external state back into:

```text
status:
```

---

# External Dependencies

Operators managing external systems need to handle:

```text
Network Failure
Authentication Failure
API Rate Limits
Partial Failure
Timeouts
Retries
```

---

# Idempotent External Operations

If an Operator creates a cloud resource, it should first determine whether the resource already exists.

Avoid:

```text
Reconcile
 ↓
Create
 ↓
Reconcile
 ↓
Create Again
```

Prefer:

```text
Reconcile
 ↓
Observe
 ↓
Create if Missing
 ↓
Otherwise Update / No-op
```

---

# Stateful Application Operator

A database Operator may automate:

```text
Database Creation
Replication
Backup
Restore
Failover
Scaling
Upgrade
```

---

# Database Operator Architecture

```text
PostgreSQLCluster
       ↓
Database Operator
       │
 ┌─────┼─────────┐
 ▼     ▼         ▼
Pods  Services  PVCs
       │
       ▼
   PostgreSQL
```

---

# Backup Operator

A backup Operator may manage:

```text
Scheduled Backups
Retention
Storage
Restore
Verification
```

---

# Monitoring Operator

A monitoring Operator may create:

```text
ServiceMonitors
PrometheusRules
Dashboards
Alerts
```

---

# Storage Operator

Storage Operators may automate:

```text
Volumes
Storage Systems
Replication
Snapshots
```

---

# Multi-Cluster Operator

A platform Operator may manage resources across clusters.

Example:

```text
Central Controller
      │
 ┌────┼────┐
 ▼    ▼    ▼
C1   C2   C3
```

Multi-cluster systems require careful:

```text
Authentication
Authorization
Failure Handling
Network Security
```

---

# Operator Dependencies

An Operator may depend on:

```text
CRDs
Other Operators
External Services
RBAC
Secrets
Webhooks
```

Dependencies must be installed and upgraded in a controlled order.

---

# Operator Upgrades

A production Operator upgrade should follow:

```text
Review
 ↓
Compatibility Check
 ↓
Backup
 ↓
Test
 ↓
Upgrade
 ↓
Observe
 ↓
Rollback if Required
```

---

# CRD Upgrade

CRDs are APIs and should be treated as important production infrastructure.

Before changing a CRD:

```text
Check Existing Objects
Check Versions
Check Conversion
Check Compatibility
Check Stored Data
```

---

# Operator Rollback

Rolling back the Operator image may not automatically roll back:

```text
CRD Changes
Application Changes
Database Schema
External Resources
```

Therefore Operator rollback requires planning.

---

# Operator Testing

Operators should be tested at multiple levels:

```text
Unit
Integration
End-to-End
```

---

# Unit Testing

Test individual reconciliation logic.

Examples:

```text
Missing Deployment
Existing Deployment
Incorrect Configuration
Invalid Spec
```

---

# Integration Testing

Test interaction with:

```text
Kubernetes API
CRDs
Controllers
Webhooks
```

---

# End-to-End Testing

Run the Operator against a real Kubernetes environment.

Validate:

```text
Create
Update
Delete
Upgrade
Failure Recovery
```

---

# Failure Testing

Test:

```text
Pod Failure
Network Failure
API Failure
Resource Deletion
External Service Failure
```

---

# Operator Observability

Operators should expose:

```text
Logs
Metrics
Events
Status Conditions
```

---

# Operator Logs

Logs should help answer:

```text
Which resource?
What action?
Why?
What failed?
What will happen next?
```

Avoid logging:

```text
Passwords
Tokens
Private Keys
Sensitive Data
```

---

# Operator Metrics

Useful metrics can include:

```text
Reconciliation Count
Reconciliation Errors
Reconciliation Duration
Queue Depth
API Requests
Work Queue Failures
```

Exact metrics depend on the framework.

---

# Operator Events

Events can show:

```text
Created
Updated
Failed
Ready
Degraded
```

---

# Operator Health

A production Operator should have appropriate:

```text
Liveness
Readiness
Startup
```

probes when applicable.

---

# Operator Resource Management

Operators themselves require:

```text
CPU Requests
Memory Requests
CPU Limits
Memory Limits
```

where appropriate.

---

# Operator SecurityContext

Use hardened container configuration where compatible:

```yaml
securityContext:
  runAsNonRoot: true
  allowPrivilegeEscalation: false
```

The exact configuration must match the Operator's requirements.

---

# Operator Network Security

Use NetworkPolicies where appropriate.

Restrict:

```text
Operator → Kubernetes API
Operator → External APIs
```

to required communication paths.

---

# Operator Supply Chain Security

Secure:

```text
Operator Source
Dependencies
Container Image
CRDs
Helm Packages
Build Pipeline
Registry
```

---

# Operator Image Security

Use:

```text
Trusted Base Image
Minimal Image
Vulnerability Scanning
SBOM
Image Signing
Immutable Digest
```

where appropriate.

---

# Operator RBAC Review

Review:

```bash
kubectl get clusterrole
kubectl get role -A
kubectl get clusterrolebinding
kubectl get rolebinding -A
```

Identify excessive permissions.

---

# Operator Security Architecture

```text
              Git
               │
               ▼
          Operator Source
               │
               ▼
              CI
       ┌───────┼───────┐
       ▼       ▼       ▼
     Test    Scan     SBOM
       │       │       │
       └───────┼───────┘
               ▼
          Signed Image
               │
               ▼
            Registry
               │
               ▼
          Kubernetes
               │
               ▼
       Operator Deployment
               │
        ServiceAccount
               │
               ▼
              RBAC
               │
               ▼
         Kubernetes API
```

---

# Production Operator Architecture

```text
                  User
                   │
                   ▼
             Custom Resource
                   │
                   ▼
              Kubernetes API
                   │
                   ▼
              Operator
                   │
           ┌───────┴───────┐
           ▼               ▼
       Reconcile        Status
           │
      ┌────┼────┬────┐
      ▼    ▼    ▼    ▼
    Pods  PVC  Svc  Secret
      │
      ▼
 Application
```

---

# Operator Design Principles

### 1. Reconciliation Must Be Idempotent

Repeated reconciliation should be safe.

---

### 2. Minimize Permissions

Use least-privilege RBAC.

---

### 3. Make APIs Clear

Users should understand:

```text
spec
status
conditions
```

---

### 4. Handle Failure

Expect:

```text
Retries
Restarts
API Errors
Network Errors
Partial State
```

---

### 5. Update Status

Expose useful operational information.

---

### 6. Use Owner References

Where appropriate, establish resource ownership.

---

### 7. Use Finalizers Carefully

Ensure cleanup logic cannot permanently block deletion.

---

### 8. Test Upgrade Paths

Operators manage long-lived production state.

---

### 9. Observe the Operator

Monitor:

```text
Errors
Latency
Queue
Events
Status
```

---

### 10. Secure the Supply Chain

Treat Operators as privileged infrastructure software.

---

# Common Mistakes

## 1. Overly Broad RBAC

Giving the Operator unrestricted access creates a large blast radius.

---

## 2. Non-Idempotent Reconciliation

Repeated events may create duplicate resources or unwanted changes.

---

## 3. Ignoring Status

Users need visibility into whether the desired state has been achieved.

---

## 4. Bad Finalizer Logic

A broken finalizer can leave resources stuck in:

```text
Terminating
```

---

## 5. Ignoring API Compatibility

CRD changes can break existing resources.

---

## 6. No Upgrade Testing

An Operator upgrade can affect every managed workload.

---

## 7. Poor Error Handling

Transient failures should be retried safely.

---

## 8. Logging Secrets

Never expose credentials in Operator logs.

---

## 9. Excessive External API Calls

Uncontrolled reconciliation can hit rate limits.

---

## 10. No Leader Election

Multiple replicas can cause conflicting operations if the controller is not designed for concurrent active reconciliation.

---

## 11. No Observability

Without metrics and logs, diagnosing Operator failures becomes difficult.

---

## 12. Treating the Operator as Ordinary Application Software

Operators have direct control over Kubernetes resources and therefore require strong security and reliability practices.

---

# Hands-on Lab 1 – Inspect Existing CRDs

List CRDs:

```bash
kubectl get crd
```

Inspect one:

```bash
kubectl describe crd <crd-name>
```

---

# Hands-on Lab 2 – Create a Simple CRD

Create a CRD representing:

```text
WebApplication
```

with fields:

```text
replicas
image
port
```

---

# Hands-on Lab 3 – Create a Custom Resource

Create:

```yaml
apiVersion: apps.example.com/v1
kind: WebApplication
metadata:
  name: example
spec:
  replicas: 2
  image: nginx:1.27
  port: 80
```

Verify:

```bash
kubectl get webapplications
```

---

# Hands-on Lab 4 – Build a Simple Controller

Using Kubebuilder or Operator SDK, create a controller that watches:

```text
WebApplication
```

and creates:

```text
Deployment
Service
```

---

# Hands-on Lab 5 – Reconciliation

Implement logic:

```text
If Deployment Missing
    ↓
Create Deployment

If Deployment Exists
    ↓
Compare Desired State
    ↓
Update if Required
```

---

# Hands-on Lab 6 – Status Conditions

Add:

```text
Ready
Progressing
Degraded
```

conditions.

Update status after reconciliation.

---

# Hands-on Lab 7 – Owner References

Make the Deployment owned by the Custom Resource.

Delete the Custom Resource.

Observe the behavior of dependent resources.

---

# Hands-on Lab 8 – Finalizer

Add a finalizer.

Before deletion:

```text
Cleanup External Resource
```

Then remove the finalizer.

---

# Hands-on Lab 9 – RBAC

Create only the permissions required to manage:

```text
Deployments
Services
ConfigMaps
```

Test the Operator with restricted permissions.

---

# Hands-on Lab 10 – Leader Election

Run multiple Operator replicas.

Enable leader election.

Observe which instance actively reconciles.

---

# Hands-on Lab 11 – Failure Recovery

Delete a managed Deployment:

```bash
kubectl delete deployment <name>
```

Observe the Operator recreate it.

---

# Hands-on Lab 12 – Configuration Change

Modify:

```yaml
spec:
  replicas: 5
```

Observe reconciliation.

---

# Hands-on Lab 13 – Invalid Configuration

Submit an invalid Custom Resource.

Use validation to reject it.

---

# Hands-on Lab 14 – Webhook

Create a validating webhook that rejects:

```text
replicas < 1
```

---

# Hands-on Lab 15 – Operator Metrics

Expose reconciliation metrics.

Monitor:

```text
Reconciliation Count
Errors
Duration
```

---

# Hands-on Lab 16 – Operator Logging

Generate structured logs showing:

```text
Resource
Namespace
Name
Action
Result
```

Ensure secrets are never logged.

---

# Hands-on Lab 17 – Operator Testing

Write:

```text
Unit Tests
Integration Tests
End-to-End Tests
```

for:

```text
Create
Update
Delete
Failure
Recovery
```

---

# Hands-on Lab 18 – Operator Upgrade

Deploy:

```text
Operator v1
```

Upgrade to:

```text
Operator v2
```

Verify existing Custom Resources continue working.

---

# Hands-on Lab 19 – Multi-Resource Operator

Create an Operator that manages:

```text
Deployment
Service
ConfigMap
HorizontalPodAutoscaler
```

from a single Custom Resource.

---

# Hands-on Lab 20 – Production Operator Project

Build a production-style Operator:

```text
Custom Resource
      ↓
CRD
      ↓
Controller
      ↓
Reconciliation
      ↓
Deployment
Service
ConfigMap
HPA
PDB
NetworkPolicy
      ↓
Status Conditions
      ↓
Metrics
Logs
Events
```

Include:

```text
RBAC
Finalizers
Owner References
Leader Election
Webhooks
Testing
Security
```

---

# Quick Revision

## Operator

```text
Software that automates management of a Kubernetes application or resource
```

---

## Controller

```text
Component that continuously reconciles desired and actual state
```

---

## CRD

```text
Defines a new Kubernetes API resource
```

---

## Custom Resource

```text
An instance of a CRD
```

---

## Reconciliation

```text
Process of aligning actual state with desired state
```

---

## Spec

```text
Desired State
```

---

## Status

```text
Observed State
```

---

## Finalizer

```text
Blocks deletion until cleanup is completed
```

---

## Owner Reference

```text
Represents resource ownership and supports garbage collection
```

---

## Leader Election

```text
Coordinates active controller leadership among replicas
```

---

## Idempotency

```text
Repeated reconciliation produces the same correct result
```

---

# Essential Commands

List CRDs:

```bash
kubectl get crd
```

Describe CRD:

```bash
kubectl describe crd <name>
```

List Custom Resources:

```bash
kubectl get <resource>
```

List all API resources:

```bash
kubectl api-resources
```

Inspect API versions:

```bash
kubectl api-versions
```

Describe Custom Resource:

```bash
kubectl describe <resource> <name>
```

View YAML:

```bash
kubectl get <resource> <name> -o yaml
```

Check Operator Pods:

```bash
kubectl get pods -n <operator-namespace>
```

View Operator logs:

```bash
kubectl logs deployment/<operator> -n <namespace>
```

Check events:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Check RBAC:

```bash
kubectl get clusterrole
```

Check bindings:

```bash
kubectl get clusterrolebinding
```

Check Services:

```bash
kubectl get svc -A
```

Check Deployments:

```bash
kubectl get deployment -A
```

Check Custom Resource status:

```bash
kubectl get <resource> <name> -o jsonpath='{.status}'
```

---

# Interview Questions

## Basic

- What is a Kubernetes Operator?
- What is the Operator pattern?
- What is a controller?
- What is reconciliation?
- What is a CRD?
- What is a Custom Resource?
- What is the difference between a CRD and a Custom Resource?
- What is `spec`?
- What is `status`?
- What is a finalizer?
- What is an owner reference?
- What is leader election?
- Why is idempotency important?

---

## Intermediate

- How does an Operator work?
- How does a reconciliation loop work?
- What happens when a Custom Resource changes?
- How does a controller watch resources?
- What is controller-runtime?
- What is Operator SDK?
- What is Kubebuilder?
- How do Operators use RBAC?
- How do Operators update status?
- What are status conditions?
- What are admission webhooks?
- What is the difference between mutating and validating webhooks?
- How do Operators manage external resources?
- How do Operators handle failures?
- How do Operators use finalizers?
- How do Operators use owner references?

---

## Advanced

- Design a production Operator architecture.
- How would you build a database Operator?
- How would you design an idempotent reconciliation loop?
- How would you secure a cluster-wide Operator?
- How would you minimize Operator RBAC?
- How would you handle CRD version migrations?
- How would you implement conversion between API versions?
- How would you design Operator high availability?
- How would you handle external API failures?
- How would you test an Operator?
- How would you safely upgrade an Operator?
- How would you design a multi-cluster Operator?
- How would you prevent an Operator from becoming a single point of failure?
- How would you monitor Operator performance?
- How would you troubleshoot resources stuck in `Terminating`?

---

# Interview Scenario 1

### Question

> What is the difference between a Kubernetes Controller and an Operator?

### Answer

A **Controller** is a Kubernetes control-loop component that reconciles resources.

An **Operator** is an application-specific controller pattern that combines:

```text
Custom Resources
+
Controllers
+
Domain-Specific Operational Knowledge
```

An Operator is therefore a specialized form of controller-based automation.

---

# Interview Scenario 2

### Question

> What happens when a Custom Resource is created?

### Answer

Conceptually:

```text
Custom Resource
 ↓
Kubernetes API
 ↓
Watch Event
 ↓
Controller Queue
 ↓
Reconcile
 ↓
Create / Update Managed Resources
 ↓
Update Status
```

---

# Interview Scenario 3

### Question

> Why must reconciliation be idempotent?

### Answer

Controllers can reconcile the same resource multiple times due to:

```text
Events
Retries
Restarts
Dependent Resource Changes
```

If reconciliation is idempotent, repeated execution safely converges to the desired state instead of creating duplicate or conflicting resources.

---

# Interview Scenario 4

### Question

> What is a finalizer?

### Answer

A finalizer allows an Operator to perform cleanup before Kubernetes completes deletion.

Example:

```text
Delete CR
 ↓
Finalizer
 ↓
Cleanup External Resource
 ↓
Remove Finalizer
 ↓
Object Deleted
```

---

# Interview Scenario 5

### Question

> What happens if a finalizer is broken?

### Answer

The resource can remain stuck in:

```text
Terminating
```

Therefore finalizer code must be:

```text
Reliable
Idempotent
Timeout-Aware
Observable
```

Operators should also provide an operational procedure for safely recovering from stuck finalizers.

---

# Interview Scenario 6

### Question

> Why use owner references?

### Answer

Owner references establish relationships between resources.

Example:

```text
WebApplication
      ↓
Deployment
      ↓
Pods
```

They allow Kubernetes garbage collection mechanisms to manage dependent resources appropriately.

---

# Interview Scenario 7

### Question

> Why should an Operator not use unrestricted ClusterRole permissions?

### Answer

Because Operators are privileged control-plane applications.

If compromised:

```text
Operator
 ↓
Broad RBAC
 ↓
Cluster Compromise
```

Least privilege reduces the blast radius.

---

# Interview Scenario 8

### Question

> How would you design a database Operator?

### Answer

I would expose a Custom Resource:

```yaml
kind: PostgreSQLCluster
spec:
  replicas: 3
  version: "16"
  storage: 100Gi
```

The Operator would reconcile:

```text
Stateful Workloads
Services
Storage
Backups
Replication
Health
```

and update:

```text
status:
```

with:

```text
Ready
Progressing
Degraded
```

I would also implement:

```text
RBAC
Finalizers
Owner References
Metrics
Logging
Testing
Upgrade Strategy
```

---

# Interview Scenario 9

### Question

> How would you troubleshoot an Operator that is not reconciling?

### Answer

I would check:

```text
1. Operator Pod
2. Operator Logs
3. CRD
4. Custom Resource
5. RBAC
6. Watch Configuration
7. Events
8. Controller Metrics
9. Webhooks
10. API Server Connectivity
```

Then verify whether reconciliation requests are being generated and whether the controller is failing during processing.

---

# Interview Scenario 10

### Question

> Design a production-grade Operator architecture.

### Answer

```text
                         Git
                          │
                          ▼
                       CI/CD
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            Tests       Scan         SBOM
              │           │           │
              └───────────┼───────────┘
                          ▼
                     Signed Image
                          │
                          ▼
                       Registry
                          │
                          ▼
                     Kubernetes
                          │
                 ┌────────┴────────┐
                 ▼                 ▼
                CRD          Operator Deployment
                                  │
                             ServiceAccount
                                  │
                                  ▼
                                 RBAC
                                  │
                                  ▼
                           Kubernetes API
                                  │
                              Controller
                                  │
                           Reconciliation
                                  │
              ┌───────────────────┼───────────────────┐
              ▼                   ▼                   ▼
          Deployment           Service              PVC
              │                   │                   │
              └───────────────────┼───────────────────┘
                                  ▼
                              Application
                                  │
                                  ▼
                             Status / Events
                                  │
                                  ▼
                         Metrics / Monitoring
```

The Operator should use:

```text
Idempotent Reconciliation
Least-Privilege RBAC
Leader Election
Finalizers
Owner References
Status Conditions
Webhooks Where Required
Strong Testing
Secure Supply Chain
```

---

# Production Operator Checklist

```text
☑ CRD API designed
☑ API versions documented
☑ OpenAPI validation configured
☑ Spec/status separation defined
☑ Status conditions implemented
☑ Reconciliation idempotent
☑ Error handling implemented
☑ Retry behavior controlled
☑ Finalizers implemented only when needed
☑ Finalizers tested for failure
☑ Owner references configured where appropriate
☑ RBAC minimized
☑ Dedicated ServiceAccount configured
☑ Leader election configured where required
☑ Webhooks secured
☑ Operator image scanned
☑ SBOM generated
☑ Image signing considered
☑ Immutable image reference considered
☑ Secrets protected
☑ Network access restricted
☑ Resource requests configured
☑ Health probes configured
☑ Logging implemented
☑ Metrics implemented
☑ Events implemented
☑ Unit tests implemented
☑ Integration tests implemented
☑ End-to-end tests implemented
☑ Upgrade path tested
☑ CRD migration strategy documented
☑ Disaster recovery considered
☑ External dependencies documented
☑ Production troubleshooting procedure documented
```

---

# Chapter Summary

Kubernetes Operators extend Kubernetes with application-specific automation.

The fundamental architecture is:

```text
Custom Resource
      ↓
Kubernetes API
      ↓
Controller
      ↓
Reconciliation
      ↓
Managed Resources
      ↓
Status
```

The most important concepts are:

```text
CRD
Custom Resource
Controller
Reconciliation
Idempotency
Finalizers
Owner References
Status Conditions
RBAC
Leader Election
Webhooks
```

Operators are especially useful when applications require complex operational knowledge such as:

```text
Backup
Restore
Failover
Replication
Scaling
Upgrades
External Resource Management
```

However, Operators are also highly privileged components. A production Operator must therefore be treated as critical infrastructure.

The most important security principles are:

```text
Least Privilege
+
Secure Supply Chain
+
Minimal Network Access
+
Protected Secrets
+
Strong API Validation
+
Observable Reconciliation
```

The most important reliability principle is:

> **An Operator should continuously and safely reconcile the desired state expressed by its Custom Resources with the actual state of the system, using idempotent logic, clear status reporting, controlled retries, and strong observability.**

---

## Next Chapter

# Chapter 83 – Service Mesh (Istio & Linkerd)

Topics will include:

- Service Mesh Fundamentals
- What Is a Service Mesh?
- Why Service Mesh?
- Microservices Networking
- East-West Traffic
- North-South Traffic
- Data Plane
- Control Plane
- Sidecar Proxy
- Ambient Mesh
- Service Discovery
- Traffic Management
- Load Balancing
- Retries
- Timeouts
- Circuit Breaking
- Fault Injection
- Traffic Splitting
- Canary Deployments
- Blue-Green Deployments
- Request Routing
- HTTP Routing
- gRPC Routing
- TCP Routing
- Mutual TLS
- mTLS
- Identity
- Certificate Management
- Zero Trust Networking
- Authorization Policies
- Authentication
- Encryption
- Observability
- Metrics
- Logging
- Distributed Tracing
- Access Logs
- OpenTelemetry
- Istio
- Istio Architecture
- Istiod
- Envoy
- Istio Ingress Gateway
- Istio Egress Gateway
- VirtualService
- DestinationRule
- Gateway
- ServiceEntry
- PeerAuthentication
- RequestAuthentication
- AuthorizationPolicy
- Sidecar Configuration
- Istio Ambient Mode
- ztunnel
- Waypoint Proxies
- Linkerd
- Linkerd Architecture
- Linkerd Proxy
- Linkerd Control Plane
- Linkerd Data Plane
- Linkerd Viz
- Service Profiles
- Traffic Policies
- mTLS in Linkerd
- Retries
- Timeouts
- Traffic Splitting
- Service Mesh Security
- Service Mesh Performance
- Resource Overhead
- Multi-Cluster Mesh
- Kubernetes Integration
- Ingress Integration
- Gateway API Integration
- Service Mesh with GitOps
- Service Mesh with CI/CD
- Service Mesh Troubleshooting
- Production Best Practices
- Common Mistakes
- Hands-on Labs
- Quick Revision
- Interview Questions
- References

---