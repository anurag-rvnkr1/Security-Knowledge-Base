# Chapter 66 – Backup & Restore

## Overview

Backup and restore are essential parts of Kubernetes production operations.

A Kubernetes cluster contains two broad categories of important data:

```text
Kubernetes State
+
Application Data
```

Kubernetes state includes:

```text
Deployments
Pods
Services
ConfigMaps
Secrets
RBAC
Namespaces
CRDs
Storage Configuration
```

Application data may include:

```text
Databases
Persistent Volumes
Uploaded Files
Application State
Object Storage
```

A backup strategy must account for both.

A simplified architecture is:

```text
                Kubernetes Cluster
                       │
          ┌────────────┴────────────┐
          ▼                         ▼
     Cluster State            Application Data
          │                         │
          ▼                         ▼
        etcd                  Persistent Volumes
          │                         │
          └────────────┬────────────┘
                       ▼
                    Backup
                       │
                       ▼
              Secure Backup Storage
                       │
                       ▼
                    Restore
                       │
                       ▼
             Recovered Environment
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes backup fundamentals
- Why backup matters
- Backup vs snapshot
- Recovery
- Disaster recovery
- RPO
- RTO
- Kubernetes state
- etcd backup
- etcd snapshots
- etcd restore
- Kubernetes resource backup
- Persistent Volume backup
- Application data backup
- Configuration backup
- Secret backup
- Namespace backup
- Cluster backup
- Volume snapshots
- CSI VolumeSnapshots
- Storage snapshots
- Velero
- Backup architecture
- Backup locations
- Object storage
- S3-compatible storage
- Backup encryption
- Backup compression
- Incremental backup
- Full backup
- Scheduled backup
- Retention
- Backup policies
- Backup verification
- Restore testing
- Namespace restore
- Application restore
- Cluster restore
- etcd disaster recovery
- Persistent data recovery
- Cross-cluster restore
- Cross-region recovery
- Disaster recovery architecture
- High availability vs backup
- Backup security
- RBAC
- Encryption
- Immutable backups
- Ransomware protection
- Air-gapped backups
- Backup monitoring
- Backup failures
- Restore failures
- Troubleshooting
- Production backup strategy
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is a Backup?

A backup is a recoverable copy of important data or configuration stored separately from the primary environment.

Example:

```text
Production Cluster
       │
       ▼
     Backup
       │
       ▼
External Storage
```

The goal is:

```text
Failure
  ↓
Recovery
  ↓
Restore Service
```

---

# Why Kubernetes Backups Matter

Kubernetes itself is not a backup system.

A cluster can fail because of:

```text
Human Error
Hardware Failure
etcd Corruption
Storage Failure
Cluster Misconfiguration
Security Incident
Ransomware
Cloud Outage
Region Failure
Accidental Deletion
```

Without backups:

```text
Failure
  ↓
Data Loss
```

With backups:

```text
Failure
  ↓
Restore
  ↓
Recovery
```

---

# What Should Be Backed Up?

A production backup strategy should consider:

```text
Cluster State
Application Configuration
Secrets
Persistent Data
Custom Resources
CRDs
Application-Specific Data
```

---

# Kubernetes State

Important Kubernetes objects may include:

```text
Namespaces
Deployments
StatefulSets
DaemonSets
Services
Ingress
Gateway API Resources
ConfigMaps
Secrets
RBAC
ServiceAccounts
NetworkPolicies
PDBs
CRDs
Custom Resources
```

---

# etcd

`etcd` contains Kubernetes control-plane state.

Conceptually:

```text
Kubernetes Objects
       ↓
API Server
       ↓
      etcd
```

Therefore, an etcd backup can be a critical component of Kubernetes control-plane recovery.

---

# etcd Backup

An etcd snapshot captures the etcd database state at a point in time.

Conceptually:

```text
etcd
 │
 ▼
Snapshot
 │
 ▼
Backup Storage
```

---

# etcd Snapshot

A common command using `etcdctl` is:

```bash
etcdctl snapshot save snapshot.db
```

The exact environment variables, certificates, endpoints, and command options depend on the cluster deployment.

Do not run restore commands against production without a tested recovery plan.

---

# Verify etcd Snapshot

Depending on your etcd version:

```bash
etcdctl snapshot status snapshot.db
```

This can provide information about the snapshot.

Always verify the snapshot using the version-appropriate tooling.

---

# etcd Restore

Conceptually:

```text
Backup Snapshot
      ↓
Restore etcd
      ↓
Recover Cluster State
```

Example command syntax varies by etcd version.

A restore normally requires:

```text
Correct etcd Version
Correct Certificates
Correct Data Directory
Correct Cluster Configuration
```

---

# Important etcd Restore Principle

An etcd restore is not simply:

```text
Copy File
```

It can involve reconstructing the control-plane datastore and ensuring that the control-plane components use the restored data correctly.

---

# Kubernetes Resource Backup

Another approach is backing up Kubernetes API resources.

Example:

```bash
kubectl get deployments -A -o yaml
```

However, manually exporting every resource is not a complete production backup strategy.

You must account for:

```text
Dependencies
Secrets
CRDs
Persistent Data
Cluster-Scoped Resources
Storage
```

---

# Resource Backup vs etcd Backup

| Feature | Resource Backup | etcd Backup |
|---|---|---|
| Kubernetes Objects | Yes | Yes |
| Direct Cluster State | Partial/Logical | Yes |
| Easy Selective Restore | Strong | More Complex |
| Application-Level Portability | Strong | Lower |
| Control Plane Recovery | Limited | Strong |
| PV Data | Not automatically | Not application data |

Both approaches can be useful depending on recovery requirements.

---

# Persistent Volume Backup

Persistent Volumes contain application data.

Examples:

```text
Database Files
User Uploads
Application State
```

Backing up Kubernetes YAML does not automatically back up the contents of the volume.

Therefore:

```text
PV Configuration
+
PV Data
```

must be considered separately.

---

# Volume Snapshot

A volume snapshot captures storage at a point in time.

Architecture:

```text
Persistent Volume
       │
       ▼
Volume Snapshot
       │
       ▼
Snapshot Storage
```

---

# CSI VolumeSnapshot

Kubernetes supports VolumeSnapshot resources through the CSI ecosystem.

Conceptually:

```yaml
apiVersion: snapshot.storage.k8s.io/v1
kind: VolumeSnapshot

metadata:
  name: database-snapshot

spec:

  source:

    persistentVolumeClaimName: database-pvc
```

The actual snapshot capability depends on the installed CSI driver.

---

# VolumeSnapshotClass

A VolumeSnapshotClass defines snapshot behavior for a CSI driver.

Conceptually:

```text
VolumeSnapshotClass
        ↓
VolumeSnapshot
        ↓
CSI Driver
        ↓
Storage Backend
```

---

# Snapshot vs Backup

A snapshot is usually:

```text
Point-in-Time Copy
```

A backup is generally:

```text
Recoverable Copy Stored Separately
```

A snapshot may still depend on the original storage platform.

Therefore:

```text
Snapshot ≠ Complete Disaster Recovery
```

---

# Backup vs High Availability

High availability:

```text
Reduce Downtime
```

Backup:

```text
Recover Data
```

Example:

```text
HA:
Node A fails
 ↓
Node B continues
```

Backup:

```text
Cluster destroyed
 ↓
Restore from backup
```

You need both for strong resilience.

---

# Recovery

Recovery is the process of returning systems and data to an operational state after failure.

Example:

```text
Failure
 ↓
Identify Scope
 ↓
Select Recovery Point
 ↓
Restore
 ↓
Validate
 ↓
Resume Operations
```

---

# Disaster Recovery

Disaster Recovery (DR) is the broader strategy for recovering from major failures.

Potential disasters:

```text
Cluster Loss
Region Failure
Storage Loss
Security Incident
Ransomware
Control Plane Failure
```

---

# RPO

RPO means:

```text
Recovery Point Objective
```

It answers:

> How much data loss can the organization tolerate?

Example:

```text
RPO = 15 minutes
```

means the recovery strategy should aim to lose no more than approximately 15 minutes of acceptable data under the defined scenario.

---

# RTO

RTO means:

```text
Recovery Time Objective
```

It answers:

> How quickly must the service be restored?

Example:

```text
RTO = 1 hour
```

means the recovery plan should aim to restore the service within approximately one hour.

---

# RPO vs RTO

| Concept | Question |
|---|---|
| RPO | How much data can we lose? |
| RTO | How much downtime can we tolerate? |

---

# Example

Suppose:

```text
RPO = 15 minutes
RTO = 1 hour
```

The organization expects:

```text
Maximum acceptable data loss ≈ 15 minutes
Maximum target recovery time ≈ 1 hour
```

---

# Backup Frequency

Backup frequency should match the RPO.

Example:

```text
RPO = 24 hours
```

A daily backup may be appropriate.

For:

```text
RPO = 15 minutes
```

you may require much more frequent backups or replication.

---

# Full Backup

A full backup contains the selected complete dataset.

Example:

```text
Full Cluster Backup
```

Advantages:

```text
Simple Restore
Self-Contained
```

Disadvantages:

```text
Large Storage
Longer Backup Time
Higher Network Usage
```

---

# Incremental Backup

An incremental backup stores changes since a previous backup according to the backup system's model.

Conceptually:

```text
Full Backup
     ↓
Changes
     ↓
Incremental
     ↓
More Changes
     ↓
Incremental
```

Advantages:

```text
Less Storage
Lower Transfer
Faster Frequent Backups
```

---

# Differential Backup

A differential backup stores changes since a selected full backup.

Conceptually:

```text
Full
 ↓
Diff 1
 ↓
Diff 2
 ↓
Diff 3
```

The exact backup capabilities depend on the backup system being used.

---

# Backup Retention

Retention defines how long backups are kept.

Example:

```text
Hourly → 24 hours
Daily → 30 days
Weekly → 12 weeks
Monthly → 12 months
```

Retention should be aligned with:

```text
Business Requirements
Compliance
Storage Cost
Recovery Requirements
```

---

# Backup Storage

Backups should ideally be stored separately from the production cluster.

Possible destinations:

```text
Object Storage
Remote Storage
Secondary Region
Secondary Cluster
Air-Gapped Storage
```

---

# Object Storage

Common object storage patterns include:

```text
S3-Compatible Storage
Cloud Object Storage
Private Object Storage
```

Architecture:

```text
Kubernetes
    ↓
Backup Tool
    ↓
Object Storage
```

---

# Why External Backup Storage?

If the cluster is destroyed:

```text
Cluster
  X
```

the backup should still exist:

```text
External Storage
  ✓
```

---

# Cross-Region Backup

For regional disaster recovery:

```text
Primary Region
      │
      ▼
Backup
      │
      ▼
Secondary Region
```

This protects against:

```text
Regional Outage
```

---

# Cross-Cluster Restore

Backups can sometimes be restored into another Kubernetes cluster.

Example:

```text
Cluster A
   ↓
Backup
   ↓
Cluster B
```

This is useful for:

```text
Disaster Recovery
Migration
Testing
Development
```

---

# Velero

Velero is a popular open-source tool for backing up and restoring Kubernetes resources and, depending on configuration and plugins, persistent volume data.

A typical architecture:

```text
Kubernetes
    │
    ▼
  Velero
    │
 ┌──┴────────────┐
 ▼               ▼
Object Storage   Volume Backup
```

---

# Velero Components

A Velero deployment commonly includes:

```text
Velero Server
Backup Resources
Restore Resources
Storage Location
Volume Snapshot / Data Movement Components
```

Exact capabilities depend on the Velero version, plugins, and configuration.

---

# Velero Backup

A simplified example:

```bash
velero backup create production-backup
```

This creates a backup according to the configured Velero policies and storage locations.

---

# List Backups

```bash
velero backup get
```

---

# Describe Backup

```bash
velero backup describe production-backup
```

---

# Backup Logs

```bash
velero backup logs production-backup
```

Useful for identifying:

```text
Failed Resources
Plugin Errors
Storage Errors
Permission Problems
```

---

# Restore

A simplified restore command:

```bash
velero restore create \
  --from-backup production-backup
```

Always test restore procedures in a controlled environment first.

---

# List Restores

```bash
velero restore get
```

---

# Describe Restore

```bash
velero restore describe <restore-name>
```

---

# Restore Logs

```bash
velero restore logs <restore-name>
```

---

# Scheduled Backups

Automated backups reduce reliance on manual operations.

Conceptually:

```text
Schedule
   ↓
Backup
   ↓
Storage
```

Example:

```bash
velero schedule create daily-backup \
  --schedule="0 2 * * *"
```

Verify the syntax supported by your installed Velero version.

---

# Backup Schedule

A production schedule could be:

```text
Frequent Backup
      +
Daily Backup
      +
Weekly Retention
      +
Monthly Retention
```

The exact policy depends on RPO, compliance, and cost requirements.

---

# Backup Encryption

Backups should be encrypted.

Possible layers:

```text
Encryption in Transit
+
Encryption at Rest
```

---

# Encryption in Transit

Use:

```text
TLS
```

for communication between:

```text
Backup Tool
      ↓
Backup Storage
```

where supported.

---

# Encryption at Rest

Backup storage should use encryption such as:

```text
Server-Side Encryption
Customer-Managed Keys
Application-Level Encryption
```

depending on the platform.

---

# Immutable Backups

An immutable backup cannot be modified or deleted during a defined retention period.

This is useful against:

```text
Ransomware
Malicious Deletion
Compromised Credentials
```

---

# Ransomware Protection

A strong strategy can include:

```text
Immutable Storage
+
Separate Credentials
+
Restricted Access
+
Versioning
+
Encryption
+
Offline / Air-Gapped Copies
```

---

# Air-Gapped Backup

An air-gapped backup is isolated from the primary production environment.

Conceptually:

```text
Production
    X
     \
      Backup
       │
       ▼
Isolated Storage
```

This can reduce the risk of an attacker compromising both production and backups.

---

# Backup Security

Protect:

```text
Backup Storage
Backup Credentials
Encryption Keys
Restore Permissions
Backup APIs
```

---

# Backup RBAC

Only authorized identities should be able to:

```text
Create Backup
Delete Backup
Restore Backup
Modify Retention
Access Backup Data
```

---

# Backup Credentials

Use dedicated identities.

Avoid:

```text
Administrator Credentials
```

for routine backup operations.

---

# Backup Monitoring

Monitor:

```text
Backup Success
Backup Failure
Backup Duration
Backup Size
Storage Capacity
Restore Tests
Snapshot Failures
```

---

# Backup Alerts

Useful alerts include:

```text
Backup Failed
Backup Older Than RPO
Storage Near Capacity
Restore Failed
Snapshot Failed
Backup Job Stuck
```

---

# Backup Verification

A backup should not be considered reliable merely because the backup command succeeded.

Verification can include:

```text
Backup Integrity Check
Metadata Validation
Test Restore
Application Validation
```

---

# Restore Testing

The most important backup practice is:

```text
Test Restore
```

A reliable cycle is:

```text
Backup
 ↓
Verify
 ↓
Restore
 ↓
Validate
```

---

# Restore Testing Frequency

Testing frequency should match:

```text
Business Criticality
RPO
RTO
Compliance
Change Frequency
```

Critical systems should be tested regularly.

---

# Namespace Restore

A namespace can sometimes be restored selectively.

Example:

```text
Production
 ├── frontend
 ├── backend
 └── payments
```

Restore only:

```text
payments
```

when required.

---

# Application Restore

Application recovery may require:

```text
Kubernetes Objects
+
Persistent Data
+
Secrets
+
Configuration
```

All dependencies must be considered.

---

# Cluster Restore

A full cluster restore may involve:

```text
Control Plane
etcd
Cluster Resources
Networking
Storage
Applications
```

The exact procedure depends on how the cluster was provisioned and managed.

---

# etcd Disaster Recovery

Conceptual process:

```text
etcd Failure
   ↓
Stop / Isolate Affected Control Plane
   ↓
Restore Valid Snapshot
   ↓
Rebuild / Reconfigure etcd
   ↓
Validate API Server
   ↓
Validate Controllers
   ↓
Validate Nodes
   ↓
Validate Applications
```

This must be adapted to the cluster topology and Kubernetes distribution.

---

# Persistent Data Recovery

Restoring Kubernetes objects does not automatically restore application data.

For example:

```text
Deployment
✓ Restored

PVC
✓ Restored

Database Files
?
```

Therefore, application data backups must be handled separately.

---

# Database Backups

Stateful applications such as databases should generally use database-aware backup strategies.

Examples:

```text
PostgreSQL
MySQL
MongoDB
```

A database-aware backup can provide better consistency than simply copying live database files.

---

# Application-Consistent Backup

For stateful systems:

```text
Application
     ↓
Consistent Backup
     ↓
Storage
```

may require:

```text
Quiescing
Database Dump
Transaction Coordination
Snapshots
Application Hooks
```

depending on the application.

---

# Crash-Consistent Backup

A crash-consistent snapshot represents storage as it might appear after a sudden system failure.

This can be useful, but it does not necessarily guarantee application-level consistency.

---

# Backup Consistency

Always ask:

```text
Is this backup:

Crash-consistent?
Application-consistent?
Database-consistent?
```

---

# Backup Architecture

A mature architecture may look like:

```text
                       Production
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
        Kubernetes State          Application Data
              │                         │
              ▼                         ▼
             etcd                    PVC / DB
              │                         │
              └────────────┬────────────┘
                           ▼
                       Backup Tool
                           │
                 ┌─────────┴─────────┐
                 ▼                   ▼
            Object Storage      Snapshot System
                 │                   │
                 └─────────┬─────────┘
                           ▼
                    Secondary Region
```

---

# Backup Lifecycle

```text
Create
  ↓
Validate
  ↓
Encrypt
  ↓
Store
  ↓
Replicate
  ↓
Retain
  ↓
Test Restore
  ↓
Expire
```

---

# Backup Policy

A policy should define:

```text
What
When
Where
How Often
Retention
Encryption
Ownership
Recovery Process
```

---

# Example Backup Policy

```text
Production:

Cluster State:
Every 6 hours

Application Data:
Every 15 minutes

Daily Backup:
30 days

Weekly Backup:
12 weeks

Monthly Backup:
12 months

Off-Site Copy:
Enabled

Encryption:
Enabled

Restore Test:
Monthly
```

This is only an example; actual intervals should be determined from RPO/RTO requirements.

---

# Backup Dependencies

A backup system can depend on:

```text
DNS
Network
Object Storage
CSI
Credentials
Encryption Keys
API Server
Storage
```

Therefore, backup infrastructure itself must be monitored.

---

# Backup Failure Scenarios

## Object Storage Unavailable

```text
Backup
 ↓
Storage Failure
 ↓
Backup Failed
```

Mitigation:

```text
Retry
Secondary Location
Alerting
```

---

# Credential Failure

```text
Backup Tool
 ↓
Authentication Failure
```

Check:

```text
Credentials
Permissions
Token Expiration
Secret
```

---

# Storage Full

```text
Backup
 ↓
Insufficient Storage
```

Mitigation:

```text
Retention
Capacity Expansion
Archive
```

---

# Snapshot Failure

Possible causes:

```text
CSI Driver
Storage Backend
Volume State
Permissions
Capacity
```

---

# Restore Failure

Possible causes:

```text
Corrupted Backup
Missing Dependencies
Version Incompatibility
Storage Failure
RBAC
CRD Missing
Networking
Secrets
```

---

# Version Compatibility

Restoring backups across Kubernetes versions requires careful compatibility testing.

Consider:

```text
Kubernetes Version
CRD Version
API Version
CSI Driver
CNI
Operators
Backup Tool
```

---

# Backup and CRDs

Custom Resources may depend on their CRDs.

Restore ordering can matter:

```text
CRD
 ↓
Custom Resource
```

rather than:

```text
Custom Resource
 ↓
CRD
```

---

# Backup and Operators

Operators may recreate resources automatically.

During restore, consider:

```text
Operator State
CRDs
Custom Resources
Controller Reconciliation
```

---

# Backup and Secrets

Secrets are sensitive.

Backup them only when required and protect them with:

```text
Encryption
Access Control
Secure Storage
Retention
```

---

# Backup and ConfigMaps

ConfigMaps are generally less sensitive than Secrets, but still important for application recovery.

---

# Backup and RBAC

Restore:

```text
Roles
ClusterRoles
RoleBindings
ClusterRoleBindings
ServiceAccounts
```

when required.

Be careful with restoring broad permissions.

---

# Backup and Network Policies

NetworkPolicies can be essential to application functionality.

A restore strategy should include them where required.

---

# Backup and Ingress

If applications rely on Ingress resources, include:

```text
Ingress
IngressClass
TLS Secrets
Controller Configuration
```

where applicable.

---

# Backup and Gateway API

For Gateway API deployments, consider:

```text
GatewayClass
Gateway
HTTPRoute
GRPCRoute
TLSRoute
ReferenceGrants
```

as applicable.

---

# Backup and StorageClasses

StorageClasses may be required for PVC recreation.

However, they may be cluster-specific and should be reviewed before restoring into another cluster.

---

# Backup and CSI

CSI drivers are infrastructure dependencies.

A restored PVC may fail if the required CSI driver is not available.

---

# Backup and CNI

Network restoration may depend on:

```text
CNI
Network Policies
Load Balancers
Routes
DNS
```

---

# Disaster Recovery Architecture

A strong DR architecture may use:

```text
Primary Cluster
       │
       ├── Backup
       │
       ▼
Secondary Region
       │
       ▼
Secondary Cluster
```

---

# Active-Passive DR

```text
Primary
  │
  ▼
Backup
  │
  ▼
Standby Cluster
```

The secondary environment is not actively serving all production traffic.

---

# Active-Active DR

```text
Region A
   │
   ├──────────┐
   │          │
   ▼          ▼
Region B    Shared Systems
```

Both environments may serve traffic.

This is more complex and requires careful data consistency design.

---

# Backup vs Replication

Replication:

```text
Copies current changes continuously
```

Backup:

```text
Preserves recoverable historical states
```

Replication alone may replicate:

```text
Accidental Deletion
Corruption
Ransomware
```

Therefore:

```text
Replication ≠ Backup
```

---

# Immutable Backup Strategy

A strong production strategy can be:

```text
Primary Backup
      ↓
Object Storage
      ↓
Immutable Retention
      ↓
Secondary Region
      ↓
Offline / Air-Gapped Copy
```

---

# Recovery Workflow

During an incident:

```text
Detect Failure
      ↓
Declare Recovery Event
      ↓
Identify RPO / RTO
      ↓
Select Recovery Point
      ↓
Validate Backup
      ↓
Restore Infrastructure
      ↓
Restore Kubernetes State
      ↓
Restore Application Data
      ↓
Validate Applications
      ↓
Restore Traffic
      ↓
Monitor
```

---

# Recovery Validation

After restore, verify:

```text
API Server
Nodes
DNS
CNI
CSI
Applications
Services
Ingress / Gateway
Databases
Secrets
Monitoring
Logging
Security Policies
```

---

# Application Validation

Do not stop at:

```text
Pod = Running
```

Also test:

```text
HTTP Request
Database Query
Authentication
Application Workflow
External Dependencies
```

---

# Recovery Runbook

A recovery runbook should contain:

```text
Prerequisites
Contacts
Backup Location
Credentials
Restore Steps
Validation Steps
Rollback
Escalation
```

---

# Recovery Documentation

Document:

```text
RPO
RTO
Backup Frequency
Retention
Storage Location
Encryption
Restore Procedure
Last Restore Test
Owner
```

---

# Common Mistakes

## 1. Backing Up Only YAML

Kubernetes manifests do not contain all application data.

---

## 2. No etcd Backup

Control-plane recovery becomes much harder.

---

## 3. No Persistent Data Backup

A restored Deployment does not restore database contents.

---

## 4. Backups Stored in the Same Cluster

Cluster destruction could destroy the backups too.

---

## 5. No Restore Testing

Untested backups may be unusable.

---

## 6. No Encryption

Backup data can contain sensitive information.

---

## 7. No Retention Policy

Storage can grow uncontrollably.

---

## 8. No Immutable Copy

Attackers who compromise backup credentials may delete backups.

---

## 9. Ignoring CRDs

Custom Resources may fail to restore without their CRDs.

---

## 10. Ignoring CSI

Persistent volumes may not recover without the correct storage driver.

---

## 11. Ignoring Secrets

Applications may start but fail to authenticate to dependencies.

---

## 12. Ignoring DNS and Networking

Restored Pods may be running but unreachable.

---

# Best Practices

### 1. Define RPO and RTO

Backup design should start with:

```text
How much data can we lose?
How quickly must we recover?
```

---

### 2. Back Up Both State and Data

Use:

```text
Cluster State Backup
+
Application Data Backup
```

---

### 3. Store Backups Outside the Cluster

Prefer:

```text
Remote Object Storage
Secondary Region
```

---

### 4. Encrypt Backups

Use encryption:

```text
In Transit
At Rest
```

---

### 5. Use Immutable Backups

Protect against:

```text
Ransomware
Malicious Deletion
```

---

### 6. Automate Backups

Use scheduled backup jobs.

---

### 7. Monitor Backups

Alert when:

```text
Backup Fails
Backup Is Too Old
Storage Is Full
```

---

### 8. Test Restores

A good cycle is:

```text
Backup
 ↓
Restore
 ↓
Validate
```

---

### 9. Use Application-Aware Backups

For databases, use appropriate database-consistent methods.

---

### 10. Document Recovery

Maintain a tested recovery runbook.

---

# Hands-on Lab 1 – Kubernetes Resource Backup

Create test resources:

```text
Namespace
Deployment
Service
ConfigMap
Secret
```

Export and document their configuration.

---

# Hands-on Lab 2 – etcd Snapshot

In a disposable cluster:

```text
Create etcd Snapshot
 ↓
Verify Snapshot
 ↓
Copy to Secure Storage
```

Document the exact commands for your cluster version.

---

# Hands-on Lab 3 – PVC Snapshot

Create:

```text
PVC
Pod
Test Data
```

Create a CSI VolumeSnapshot.

Verify:

```text
Snapshot
```

is ready.

---

# Hands-on Lab 4 – Restore PVC From Snapshot

Create a new PVC from the snapshot.

Mount it into a test Pod.

Verify the test data.

---

# Hands-on Lab 5 – Install Velero

Install Velero in a test cluster.

Configure:

```text
Backup Storage Location
```

using an appropriate object-storage backend.

---

# Hands-on Lab 6 – Velero Backup

Create:

```bash
velero backup create test-backup
```

Check:

```bash
velero backup get
```

---

# Hands-on Lab 7 – Inspect Backup

Run:

```bash
velero backup describe test-backup
```

and:

```bash
velero backup logs test-backup
```

Identify:

```text
Successful Resources
Failed Resources
Warnings
```

---

# Hands-on Lab 8 – Velero Restore

Create a restore:

```bash
velero restore create \
  --from-backup test-backup
```

Verify:

```bash
velero restore get
```

---

# Hands-on Lab 9 – Namespace Restore

Back up a test namespace.

Delete it.

Restore only that namespace.

Verify:

```text
Pods
Services
ConfigMaps
Secrets
```

---

# Hands-on Lab 10 – Persistent Data Backup

Create a test application with a PVC.

Store:

```text
test-file.txt
```

Back up the application and volume data using your chosen backup mechanism.

Restore it.

Verify the file.

---

# Hands-on Lab 11 – Scheduled Backup

Create an automated backup schedule.

Verify that:

```text
Backup 1
Backup 2
Backup 3
```

are created according to the schedule.

---

# Hands-on Lab 12 – Backup Failure

Intentionally make the backup storage unavailable in a disposable environment.

Observe:

```text
Backup Failure
Logs
Alerts
Retry
```

---

# Hands-on Lab 13 – Restore Failure

Create a controlled restore failure.

Investigate:

```text
Restore Logs
Missing Dependencies
RBAC
Storage
CRDs
```

---

# Hands-on Lab 14 – Cross-Cluster Restore

Create:

```text
Cluster A
```

Back up resources.

Restore into:

```text
Cluster B
```

Validate application behavior.

---

# Hands-on Lab 15 – Backup Encryption

Configure encrypted backup storage.

Verify:

```text
Encryption at Rest
TLS
Access Control
```

---

# Hands-on Lab 16 – Immutable Backup

Configure a test object-storage bucket with an appropriate immutability/retention mechanism.

Verify that a retained backup cannot be deleted before its retention period expires.

---

# Hands-on Lab 17 – Disaster Recovery Exercise

Simulate:

```text
Primary Cluster Loss
```

Perform:

```text
Backup Selection
 ↓
Recovery Cluster
 ↓
Restore
 ↓
Application Validation
 ↓
Traffic Recovery
```

Measure:

```text
Actual RTO
Actual Data Loss
```

---

# Hands-on Lab 18 – RPO Exercise

Create backups every:

```text
15 minutes
```

Simulate data loss.

Determine:

```text
Actual Recovery Point
```

---

# Hands-on Lab 19 – RTO Exercise

Document the complete restore procedure.

Measure:

```text
Time to Recovery
```

Compare it with the required RTO.

---

# Hands-on Lab 20 – Production Backup Architecture

Build:

```text
Kubernetes
    │
 ┌──┴─────────┐
 ▼            ▼
etcd         PVC
 │            │
 └─────┬──────┘
       ▼
  Backup System
       │
 ┌─────┴─────────────┐
 ▼                   ▼
Object Storage    Volume Backup
 │
 ▼
Secondary Region
```

Include:

```text
Encryption
Immutable Storage
Retention
Monitoring
Restore Testing
DR Runbook
```

---

# Quick Revision

## Backup

```text
Recoverable copy of important data/state
```

---

## Restore

```text
Recovering data/state from backup
```

---

## RPO

```text
Maximum acceptable data loss
```

---

## RTO

```text
Target maximum recovery time
```

---

## etcd Snapshot

```text
Point-in-time copy of etcd database state
```

---

## Volume Snapshot

```text
Point-in-time copy of storage volume
```

---

## Velero

```text
Kubernetes backup and restore tool
```

---

## Full Backup

```text
Complete selected dataset
```

---

## Incremental Backup

```text
Changes since a previous backup according to the backup model
```

---

## Retention

```text
How long backups are preserved
```

---

## Immutable Backup

```text
Backup protected from modification/deletion during retention
```

---

## Air-Gapped Backup

```text
Backup isolated from production environment
```

---

## Application-Consistent Backup

```text
Backup coordinated with application state
```

---

## Crash-Consistent Backup

```text
Storage state suitable for recovery after an unexpected interruption
```

---

## Disaster Recovery

```text
Strategy for recovering from major failures
```

---

# Essential Commands

Check etcd snapshot:

```bash
etcdctl snapshot status snapshot.db
```

Create an etcd snapshot:

```bash
etcdctl snapshot save snapshot.db
```

List Velero backups:

```bash
velero backup get
```

Create Velero backup:

```bash
velero backup create test-backup
```

Describe backup:

```bash
velero backup describe test-backup
```

View backup logs:

```bash
velero backup logs test-backup
```

List restores:

```bash
velero restore get
```

Create restore:

```bash
velero restore create \
  --from-backup test-backup
```

Describe restore:

```bash
velero restore describe <restore-name>
```

View restore logs:

```bash
velero restore logs <restore-name>
```

List VolumeSnapshots:

```bash
kubectl get volumesnapshot -A
```

List VolumeSnapshotClasses:

```bash
kubectl get volumesnapshotclass
```

List PVCs:

```bash
kubectl get pvc -A
```

List PVs:

```bash
kubectl get pv
```

List StorageClasses:

```bash
kubectl get storageclass
```

---

# Interview Questions

## Basic

- What is Kubernetes backup?
- Why do Kubernetes clusters need backups?
- What is etcd?
- Why is etcd backup important?
- What is an etcd snapshot?
- What is a Persistent Volume backup?
- What is a VolumeSnapshot?
- What is CSI?
- What is Velero?
- What is RPO?
- What is RTO?
- What is the difference between backup and snapshot?
- What is the difference between backup and replication?
- What is an immutable backup?
- What is an air-gapped backup?
- What is backup retention?

---

## Intermediate

- What should be backed up in Kubernetes?
- Does backing up Kubernetes YAML also back up Persistent Volume data?
- How do you back up etcd?
- How do you restore etcd?
- How do you back up a PVC?
- What is a CSI VolumeSnapshot?
- How does Velero work?
- How do you create a Velero backup?
- How do you restore a Velero backup?
- How do you schedule backups?
- Where should Kubernetes backups be stored?
- Why should backups be stored outside the cluster?
- How do you protect backups from ransomware?
- How do you verify backups?
- Why is restore testing important?
- What happens if the CSI driver is missing during restore?

---

## Advanced

- Design a Kubernetes backup strategy for production.
- Design a disaster recovery architecture across two regions.
- How would you achieve an RPO of 15 minutes?
- How would you achieve an RTO of 1 hour?
- How would you restore a Kubernetes cluster after complete control-plane loss?
- How would you restore etcd after corruption?
- How would you recover Persistent Volume data?
- How would you perform a cross-cluster restore?
- How would you protect backups from a compromised Kubernetes cluster?
- How would you implement immutable backups?
- How would you design backup retention?
- How would you validate backup integrity?
- How would you test disaster recovery?
- What is the difference between crash-consistent and application-consistent backups?
- How would you back up a production PostgreSQL workload running in Kubernetes?
- How would you design backup monitoring and alerting?

---

# Interview Scenario 1

### Question

> What should be backed up in Kubernetes?

### Answer

A complete strategy should consider:

```text
Cluster State
+
Kubernetes Resources
+
CRDs
+
Secrets
+
Configuration
+
Persistent Data
+
Application-Specific Data
```

Backing up only YAML files is not enough for stateful workloads.

---

# Interview Scenario 2

### Question

> What is the difference between an etcd backup and a PVC backup?

### Answer

An etcd backup protects Kubernetes control-plane state:

```text
Deployments
Services
Secrets
RBAC
Namespaces
```

A PVC backup protects application data:

```text
Database Files
Uploaded Files
Application State
```

They solve different recovery problems.

---

# Interview Scenario 3

### Question

> What is RPO?

### Answer

RPO means Recovery Point Objective.

It defines how much data loss is acceptable.

For example:

```text
RPO = 15 minutes
```

means the recovery design should aim to limit data loss to approximately 15 minutes under the defined failure scenario.

---

# Interview Scenario 4

### Question

> What is RTO?

### Answer

RTO means Recovery Time Objective.

It defines how quickly the system should be restored.

Example:

```text
RTO = 1 hour
```

means the recovery process should target restoration within approximately one hour.

---

# Interview Scenario 5

### Question

> Are snapshots a replacement for backups?

### Answer

No.

A snapshot is a point-in-time representation of storage.

A backup should generally be stored separately and be independently recoverable.

If the storage platform fails:

```text
Snapshot
   ↓
May Also Become Unavailable
```

Therefore:

```text
Snapshot ≠ Complete Backup Strategy
```

---

# Interview Scenario 6

### Question

> Why should backups be stored outside the Kubernetes cluster?

### Answer

If the cluster is destroyed:

```text
Cluster
  X
```

backups stored inside the same cluster may also be lost.

External storage provides separation:

```text
Cluster
   ↓
External Backup Storage
```

---

# Interview Scenario 7

### Question

> What happens if you restore Kubernetes YAML but not the database data?

### Answer

The Pods may start successfully:

```text
Deployment
✓

Pod
✓

Service
✓
```

but the application may still be missing:

```text
Database Data
```

Therefore, application state and persistent data must be backed up separately.

---

# Interview Scenario 8

### Question

> How do you protect backups from ransomware?

### Answer

Use multiple layers:

```text
Encryption
+
Immutable Storage
+
Separate Credentials
+
Least Privilege
+
Off-Site Copies
+
Air-Gapped Copies
+
Retention Policies
```

Do not rely on a single backup copy.

---

# Interview Scenario 9

### Question

> How do you know whether a backup actually works?

### Answer

Perform restore testing.

The process is:

```text
Backup
 ↓
Verify
 ↓
Restore
 ↓
Application Validation
```

A successful backup command alone does not prove recoverability.

---

# Interview Scenario 10

### Question

> Design a production Kubernetes backup strategy.

### Answer

Use:

```text
Kubernetes State
      │
      ▼
etcd Backup
      │
      ├─────────────┐
      ▼             ▼
Resource Backup   PV Backup
      │             │
      └──────┬──────┘
             ▼
       External Object Storage
             │
       ┌─────┴─────┐
       ▼           ▼
   Immutable    Secondary
     Copy        Region
```

Add:

```text
Encryption
Retention
Monitoring
RPO/RTO
Restore Testing
DR Runbooks
```

---

# Production Backup Checklist

```text
☑ RPO defined
☑ RTO defined
☑ etcd backup configured
☑ Kubernetes resource backup configured
☑ CRDs included
☑ Secrets protected
☑ Persistent data backup configured
☑ Database-aware backups configured
☑ Volume snapshots configured where appropriate
☑ External backup storage
☑ Cross-region copy
☑ Encryption at rest
☑ TLS
☑ Immutable retention
☑ Backup credentials protected
☑ RBAC
☑ Backup monitoring
☑ Failure alerts
☑ Restore tests
☑ Disaster recovery tests
☑ Recovery runbook
☑ Backup retention policy
```

---

# Chapter Summary

Kubernetes backup and restore should protect both:

```text
Cluster State
+
Application Data
```

Important components include:

```text
etcd
Persistent Volumes
CSI VolumeSnapshots
Velero
Object Storage
```

The key recovery concepts are:

```text
RPO
RTO
Backup
Snapshot
Restore
Disaster Recovery
```

A strong production architecture is:

```text
Production Cluster
       │
       ├── etcd Backup
       │
       ├── Resource Backup
       │
       └── Application Data Backup
                    │
                    ▼
             External Storage
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
     Immutable Copy      Secondary Region
```

Backups should be:

```text
Encrypted
Automated
Monitored
Externally Stored
Protected
Tested
```

The most important principle is:

> **A backup is only valuable when it can be successfully restored. Production Kubernetes environments therefore require not just backup automation, but regular restore validation and a tested disaster-recovery process.**

---

## Next Chapter

# Chapter 67 – Upgrades

Topics will include:

- Kubernetes Upgrade Fundamentals
- Why Kubernetes Upgrades Matter
- Kubernetes Release Cycle
- Version Skew
- Control Plane Upgrade
- Worker Node Upgrade
- kubelet Upgrade
- kubectl Compatibility
- API Version Changes
- Deprecated APIs
- Removed APIs
- CRD Compatibility
- CNI Compatibility
- CSI Compatibility
- Ingress Compatibility
- Gateway API Compatibility
- Operator Compatibility
- Helm Compatibility
- Admission Webhooks
- Monitoring Stack Compatibility
- Backup Before Upgrade
- Upgrade Planning
- Upgrade Strategy
- Rolling Upgrade
- Node-by-Node Upgrade
- Surge Upgrades
- Cordon
- Drain
- Uncordon
- Pod Disruption Budgets
- Capacity Planning
- Maintenance Windows
- Preflight Checks
- Cluster Health Checks
- Upgrade Testing
- Staging Clusters
- Canary Nodes
- Control Plane Upgrade
- Worker Node Upgrade
- Managed Kubernetes Upgrades
- kubeadm Upgrades
- Cloud Provider Upgrades
- Upgrade Automation
- Rollback
- Upgrade Failure
- API Server Failure
- Scheduler Failure
- Controller Failure
- Node Failure
- CNI Failure
- CSI Failure
- Admission Failure
- Certificate Issues
- etcd Backup
- Disaster Recovery
- Post-Upgrade Validation
- Monitoring
- Security
- Production Upgrade Checklist
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---