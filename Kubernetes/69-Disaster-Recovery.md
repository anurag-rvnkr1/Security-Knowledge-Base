# Chapter 69 – Disaster Recovery

## Overview

Disaster Recovery (DR) is the process, architecture, and operational strategy used to restore Kubernetes workloads and services after a major failure.

High Availability focuses primarily on continuing service during component failures:

```text
Node Failure
    ↓
Another Node
    ↓
Service Continues
```

Disaster Recovery focuses on larger failures:

```text
Cluster Loss
    ↓
Recovery Environment
    ↓
Restore
    ↓
Service Recovery
```

A production DR strategy should protect against:

```text
Cluster Failure
Control Plane Failure
etcd Loss
Storage Failure
Region Failure
Cloud Failure
Human Error
Security Incidents
Ransomware
Accidental Deletion
```

A simplified DR architecture:

```text
                 Production Environment
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
        Kubernetes State       Application Data
              │                     │
              ▼                     ▼
             etcd                 PV / DB
              │                     │
              └──────────┬──────────┘
                         ▼
                    Backup System
                         │
             ┌───────────┴───────────┐
             ▼                       ▼
       Object Storage          Secondary Region
             │                       │
             └───────────┬───────────┘
                         ▼
                  Recovery Cluster
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Disaster Recovery fundamentals
- Disaster vs failure
- Business continuity
- Business impact analysis
- RPO
- RTO
- MTTR
- MTTD
- Disaster Recovery planning
- Kubernetes DR architecture
- Cluster disasters
- Control-plane disasters
- etcd disasters
- Worker-node disasters
- Storage disasters
- Network disasters
- Region failures
- Cloud-provider failures
- Data-center failures
- Security incidents
- Ransomware
- Accidental deletion
- Backup strategies
- etcd backups
- Persistent Volume backups
- Database backups
- Kubernetes resource backups
- Velero
- Volume snapshots
- Cross-cluster recovery
- Cross-region recovery
- Active-passive DR
- Active-active DR
- Warm standby
- Cold standby
- Recovery environments
- DNS failover
- Global load balancing
- Traffic failover
- Data replication
- Database replication
- Storage replication
- Secrets recovery
- Identity recovery
- Network recovery
- CNI recovery
- CSI recovery
- Control-plane recovery
- etcd restore
- Application recovery
- Dependency recovery
- Recovery runbooks
- DR testing
- Game days
- Chaos engineering
- Restore testing
- Failover testing
- Failback
- Recovery validation
- DR monitoring
- DR security
- Immutable backups
- Air-gapped backups
- Compliance
- Documentation
- Production DR architecture
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is Disaster Recovery?

Disaster Recovery is the capability to recover systems and data after a disruptive event.

The basic process is:

```text
Disaster
   ↓
Detect
   ↓
Assess
   ↓
Recover
   ↓
Validate
   ↓
Resume Operations
```

---

# Disaster vs Failure

A failure may affect one component:

```text
Worker Node
    X
```

A disaster can affect an entire environment:

```text
Region
   X
```

Examples:

```text
Failure:
Single Pod Failure

Disaster:
Complete Cluster Loss
```

---

# Business Continuity

Business Continuity is the broader strategy for keeping critical business operations functioning during disruptions.

It includes:

```text
Technology
People
Processes
Communication
Suppliers
Infrastructure
```

Disaster Recovery is one part of Business Continuity.

---

# Business Impact Analysis

Business Impact Analysis (BIA) identifies:

```text
Critical Services
Business Impact
Dependencies
Recovery Requirements
Acceptable Downtime
Acceptable Data Loss
```

Example:

```text
Payment Service
     ↓
Critical
     ↓
RTO = 30 minutes
RPO = 5 minutes
```

---

# RPO

Recovery Point Objective defines acceptable data loss.

Example:

```text
RPO = 15 minutes
```

The recovery strategy should aim to restore data to a point no older than approximately 15 minutes under the defined failure scenario.

---

# RTO

Recovery Time Objective defines the target time for restoring service.

Example:

```text
RTO = 1 hour
```

The recovery process should target restoration within approximately one hour.

---

# MTTR

MTTR means:

```text
Mean Time To Recovery
```

It measures the average time required to restore service after failures.

---

# MTTD

MTTD means:

```text
Mean Time To Detect
```

It measures how quickly a problem is detected.

---

# Recovery Metrics

A useful model is:

```text
MTTD
 ↓
Detection

MTTR
 ↓
Recovery
```

DR planning should minimize both.

---

# DR Requirements

Before designing DR, define:

```text
RPO
RTO
Critical Services
Dependencies
Recovery Order
Recovery Location
Backup Retention
```

---

# Kubernetes Disaster Scenarios

Possible scenarios include:

```text
Control Plane Loss
etcd Corruption
Cluster Deletion
Worker Node Loss
Storage Loss
Network Failure
Region Failure
Cloud Provider Failure
Credential Compromise
Ransomware
Human Error
```

---

# Cluster Disaster

A cluster may become unavailable due to:

```text
Control Plane Failure
Infrastructure Failure
etcd Failure
Network Failure
Storage Failure
```

Recovery may require:

```text
New Cluster
+
Restore
```

---

# Control Plane Disaster

Control-plane components include:

```text
API Server
etcd
Scheduler
Controller Manager
```

If the control plane is lost:

```text
Existing workloads
        ↓
May continue running temporarily
```

but cluster management and reconciliation can be severely affected.

---

# etcd Disaster

etcd stores critical Kubernetes state.

If etcd is lost:

```text
Cluster State
     ↓
Unavailable / Lost
```

A valid etcd backup can support recovery.

---

# etcd Recovery

Conceptually:

```text
Valid Snapshot
      ↓
Restore etcd
      ↓
Recover Control Plane
      ↓
Validate API Server
      ↓
Validate Controllers
      ↓
Validate Scheduler
```

Exact procedures depend on the cluster topology and Kubernetes distribution.

---

# Worker Node Disaster

If a worker node is permanently lost:

```text
Worker
  X
```

Workloads can be recreated on other nodes if:

```text
Replicas Exist
Capacity Exists
Storage Is Recoverable
```

---

# Storage Disaster

Storage failure is especially serious for:

```text
Databases
Stateful Applications
Persistent Files
```

Recovery may require:

```text
Volume Snapshot
Backup
Storage Replication
Database Restore
```

---

# Network Disaster

Networking failures can affect:

```text
Pod-to-Pod Communication
Service Traffic
DNS
Ingress
External Dependencies
```

Recovery should verify:

```text
CNI
Routes
DNS
Load Balancer
Network Policies
```

---

# Region Failure

A region may become unavailable due to:

```text
Cloud Outage
Networking
Power
Infrastructure
Natural Disaster
```

A cross-region architecture can provide recovery.

```text
Region A
   X

Region B
   ↓
Recovery
```

---

# Cloud Provider Failure

A major cloud outage may require:

```text
Secondary Region
Secondary Provider
On-Premises Environment
```

depending on business requirements.

---

# Data Center Failure

For organizations operating their own infrastructure:

```text
Data Center A
      X
```

a secondary data center can provide recovery:

```text
Data Center B
      ↓
Recovery
```

---

# Security Incident

A Kubernetes cluster can become compromised through:

```text
Compromised Credentials
Vulnerable Workload
Supply Chain Attack
Exposed API
Malicious Image
Privilege Escalation
```

DR must account for security recovery, not just infrastructure failure.

---

# Ransomware

Ransomware may encrypt or destroy:

```text
Application Data
Backups
Secrets
Configuration
```

A strong DR strategy should use:

```text
Immutable Backups
+
Separate Credentials
+
Offline Copies
+
Access Control
+
Encryption
```

---

# Accidental Deletion

Example:

```bash
kubectl delete namespace production
```

Accidental deletion can cause significant damage.

Recovery requires:

```text
Backup
+
Restore
```

if the resources and data were backed up.

---

# Backup Strategy

A production DR strategy should protect:

```text
Kubernetes State
+
Persistent Data
+
Database State
+
Configuration
+
Secrets
```

---

# Kubernetes Resource Backup

Back up important resources such as:

```text
Namespaces
Deployments
Services
ConfigMaps
Secrets
RBAC
NetworkPolicies
CRDs
Custom Resources
Ingress
Gateway API Resources
```

---

# etcd Backup

etcd snapshots provide a mechanism to preserve Kubernetes control-plane state.

Example:

```bash
etcdctl snapshot save snapshot.db
```

The endpoint and certificate options depend on the cluster environment.

---

# Persistent Volume Backup

Persistent application data must be backed up separately.

Example:

```text
PVC
 ↓
Volume Snapshot
 ↓
Backup Storage
```

---

# Database Backup

Databases should generally use database-aware backup mechanisms.

Example:

```text
PostgreSQL
    ↓
Database Backup
    ↓
Remote Storage
```

This can provide better application consistency than simply copying live database files.

---

# Velero

Velero is commonly used to back up and restore Kubernetes resources and, with the appropriate plugins/configuration, persistent volume data.

Architecture:

```text
Kubernetes
    │
    ▼
  Velero
    │
    ├── Resource Backup
    │
    └── Volume Data / Snapshots
             │
             ▼
        Backup Storage
```

---

# Velero Backup

Example:

```bash
velero backup create production-backup
```

Check:

```bash
velero backup get
```

---

# Velero Restore

Example:

```bash
velero restore create \
  --from-backup production-backup
```

Always test restore workflows in a controlled environment.

---

# Volume Snapshots

CSI-based VolumeSnapshots can provide point-in-time storage recovery.

Conceptually:

```text
PVC
 ↓
VolumeSnapshot
 ↓
Snapshot Storage
```

---

# Snapshot vs Backup

A snapshot:

```text
Point-in-Time Storage State
```

A backup:

```text
Recoverable Copy Stored Independently
```

A snapshot alone should not be assumed to provide complete disaster recovery.

---

# Cross-Cluster Recovery

A backup can sometimes be restored to another cluster:

```text
Cluster A
    ↓
Backup
    ↓
Cluster B
    ↓
Restore
```

This is useful for:

```text
Disaster Recovery
Migration
Testing
```

---

# Cross-Region Recovery

For regional disasters:

```text
Primary Region
      │
      ▼
Backup Replication
      │
      ▼
Secondary Region
      │
      ▼
Recovery Cluster
```

---

# Active-Passive DR

Architecture:

```text
Region A
   │
   ▼
Active Cluster

Region B
   │
   ▼
Standby Cluster
```

When Region A fails:

```text
Region A
   X

Region B
   ↓
Active
```

---

# Active-Active DR

Both environments serve traffic:

```text
Global Traffic Manager
       │
   ┌───┴───┐
   ▼       ▼
Region A Region B
   │       │
Cluster A Cluster B
```

Active-active is more complex because data consistency and traffic management must be carefully designed.

---

# Warm Standby

A warm standby environment is partially prepared for recovery.

Example:

```text
Secondary Cluster
   ↓
Infrastructure Ready
   ↓
Applications Partially Ready
```

Recovery is faster than building everything from scratch.

---

# Cold Standby

A cold standby environment may require significant setup during recovery.

```text
Disaster
   ↓
Provision Infrastructure
   ↓
Create Cluster
   ↓
Restore
   ↓
Validate
```

This can be cheaper but typically has a longer RTO.

---

# DR Environment Comparison

| Strategy | Recovery Speed | Cost | Complexity |
|---|---|---|---|
| Cold Standby | Slow | Lower | Lower |
| Warm Standby | Medium | Medium | Medium |
| Active-Passive | Fast | Higher | Higher |
| Active-Active | Very Fast | High | Very High |

---

# Recovery Environment

A recovery environment may require:

```text
Kubernetes Cluster
Networking
DNS
Load Balancer
Storage
Identity
Secrets
Monitoring
Logging
Security
```

---

# DNS Failover

DNS can direct users to the recovery environment.

Example:

```text
app.example.com
      │
      ▼
Global DNS
   ┌──┴──┐
   ▼     ▼
Region A Region B
```

---

# Global Load Balancing

A global load balancer can route traffic based on:

```text
Health
Location
Latency
Availability
Policy
```

---

# Traffic Failover

Normal:

```text
Users
  ↓
Region A
```

After failure:

```text
Users
  ↓
Region B
```

---

# Data Replication

DR often requires replication of application data.

Possible approaches:

```text
Database Replication
Storage Replication
Object Storage Replication
Application-Level Replication
```

---

# Database Replication

Example:

```text
Primary DB
    │
    ▼
Replica DB
```

If the primary region fails:

```text
Replica
   ↓
Promoted
```

The exact process depends on the database.

---

# Storage Replication

Storage platforms may support:

```text
Synchronous Replication
Asynchronous Replication
Cross-Region Replication
```

Choose based on:

```text
RPO
Latency
Cost
Consistency
```

---

# Synchronous Replication

Writes are replicated before being acknowledged according to the storage/database protocol.

Benefits:

```text
Lower Data Loss
```

Trade-offs:

```text
Latency
Distance Constraints
Complexity
```

---

# Asynchronous Replication

Changes are replicated after the primary operation.

Benefits:

```text
Lower Latency
Longer Distances
```

Trade-off:

```text
Potential Data Loss
```

---

# Secrets Recovery

Secrets may be required for:

```text
Database
APIs
TLS
Authentication
Cloud Services
```

Protect backup copies with:

```text
Encryption
RBAC
Separate Credentials
```

---

# Identity Recovery

Recovery environments may depend on:

```text
Identity Provider
OIDC
Cloud IAM
Certificates
Service Accounts
```

Ensure identity dependencies are available during DR.

---

# Network Recovery

Recovery requires:

```text
CNI
DNS
Routes
Load Balancer
Firewall
Network Policies
```

---

# CNI Recovery

Ensure the recovery cluster has:

```text
Compatible CNI
Correct Configuration
Required Network Permissions
```

---

# CSI Recovery

Persistent storage recovery may require:

```text
CSI Driver
StorageClass
Storage Backend
Snapshot Support
```

---

# Control Plane Recovery

A control-plane recovery workflow may look like:

```text
Provision Control Plane
        ↓
Restore etcd / State
        ↓
Validate API Server
        ↓
Validate Scheduler
        ↓
Validate Controllers
        ↓
Join Worker Nodes
        ↓
Restore Applications
```

---

# Application Recovery

Applications may require:

```text
Deployments
Services
ConfigMaps
Secrets
PVCs
NetworkPolicies
Ingress
Gateway
```

---

# Dependency Recovery

Applications often depend on:

```text
Database
Cache
Message Queue
Object Storage
External API
Identity Provider
DNS
```

Recover dependencies in the correct order.

---

# Recovery Order

A common conceptual order is:

```text
Infrastructure
   ↓
Network
   ↓
Identity
   ↓
Kubernetes
   ↓
Storage
   ↓
Databases
   ↓
Applications
   ↓
Ingress / Traffic
   ↓
Monitoring
```

The exact order depends on the environment.

---

# Recovery Runbook

A DR runbook should include:

```text
Trigger
Contacts
Prerequisites
Backup Locations
Credentials
Recovery Steps
Validation
Failover
Failback
Escalation
```

---

# DR Runbook Example

```text
1. Declare Incident
2. Assess Scope
3. Identify Recovery Region
4. Verify Latest Backup
5. Provision / Activate Cluster
6. Restore Cluster State
7. Restore Storage
8. Restore Databases
9. Restore Applications
10. Validate Services
11. Switch Traffic
12. Monitor
```

---

# DR Testing

A DR strategy should be tested regularly.

Testing can include:

```text
Restore Test
Failover Test
Game Day
Chaos Experiment
Cross-Region Recovery
Backup Validation
```

---

# Restore Testing

Verify:

```text
Backup Exists
 ↓
Restore
 ↓
Application Starts
 ↓
Data Exists
 ↓
Traffic Works
```

---

# Failover Testing

Simulate:

```text
Primary Region Failure
```

Then:

```text
Secondary Region
 ↓
Traffic
 ↓
Applications
```

---

# Game Day

A game day is a planned exercise where teams simulate a disaster.

Participants may include:

```text
Platform Team
Security Team
Application Team
Database Team
Network Team
Operations
Management
```

---

# Chaos Engineering

Chaos engineering intentionally introduces controlled failures to validate system resilience.

Example:

```text
Kill Pod
 ↓
Observe
 ↓
Measure Recovery
```

---

# DR Testing Metrics

Measure:

```text
Actual RTO
Actual RPO
MTTD
MTTR
Data Integrity
Service Availability
```

---

# Failback

Failback is returning operations to the original or preferred environment after recovery.

Example:

```text
Region A
   X
   ↓
Region B
   ↓
Recovery
   ↓
Region A Recovered
   ↓
Failback
```

---

# Failback Planning

Before failback:

```text
Data Synchronization
Application Validation
Traffic Testing
Capacity
DNS
Monitoring
```

---

# Recovery Validation

After recovery, verify:

```text
API Server
Nodes
DNS
CNI
CSI
Storage
Databases
Services
Ingress
Gateway
Applications
Monitoring
Logging
Security
```

---

# Application Validation

Do not only check:

```text
Pod Running
```

Test:

```text
User Login
API Request
Database Read
Database Write
Payment
Messaging
External Integration
```

according to the application.

---

# Data Validation

Verify:

```text
Record Counts
Checksums
Application Queries
Transactions
Files
Object Storage
```

where applicable.

---

# DR Monitoring

During recovery, monitor:

```text
Cluster Health
Node Health
Pod Restarts
API Latency
Database Health
Storage
Network
Application Errors
Traffic
```

---

# DR Security

During disaster recovery:

```text
Security Must Not Be Disabled
```

Maintain:

```text
RBAC
TLS
Secrets
Network Policies
Audit Logging
Image Security
```

---

# Immutable Backups

Immutable backups protect against:

```text
Modification
Deletion
Ransomware
```

during a defined retention period.

---

# Air-Gapped Backups

Air-gapped backups are isolated from the production environment.

This provides additional protection against:

```text
Credential Compromise
Ransomware
Malicious Deletion
```

---

# Backup Separation

A strong strategy separates:

```text
Production Credentials
      X
Backup Credentials
```

Compromise of one should not automatically compromise the other.

---

# Compliance

Some environments require:

```text
Retention
Encryption
Audit Logs
Access Controls
Recovery Testing
Geographic Requirements
```

Always follow applicable organizational and regulatory requirements.

---

# DR Documentation

Document:

```text
Architecture
Dependencies
RPO
RTO
Backup Locations
Recovery Procedures
Contacts
Escalation
Testing Results
```

---

# DR Architecture Example

```text
                       Global DNS
                           │
                    Global Load Balancer
                       /          \
                      /            \
                     ▼              ▼
              Region A          Region B
             Primary           Recovery
                 │                 │
          ┌──────┴──────┐          │
          ▼             ▼          ▼
       Kubernetes    Database   Kubernetes
        Cluster       Primary    Cluster
          │             │          │
          └──────┬──────┘          │
                 ▼                 │
             Replication ──────────┘
                 │
                 ▼
          Backup Storage
                 │
          ┌──────┴──────┐
          ▼             ▼
     Immutable       Archive
       Copy
```

---

# Common Mistakes

## 1. Assuming HA Is DR

HA does not protect against every disaster.

---

## 2. Keeping Backups in the Same Cluster

Cluster loss can also destroy backups.

---

## 3. Never Testing Recovery

An untested DR plan may fail when needed.

---

## 4. Ignoring Application Data

Kubernetes resources alone do not restore database contents.

---

## 5. Ignoring Dependencies

Applications may depend on:

```text
DNS
Identity
Database
Storage
External APIs
```

---

## 6. No RPO/RTO

Without measurable targets, DR cannot be properly designed.

---

## 7. No Failback Plan

Recovery is incomplete if returning to the primary environment is not planned.

---

## 8. Ignoring Security During DR

Do not bypass security controls simply to recover faster without a controlled emergency procedure.

---

## 9. No Immutable Backup

Attackers may destroy ordinary backups.

---

## 10. No Cross-Region Copy

A regional disaster can affect locally stored backups.

---

# Best Practices

### 1. Define RPO and RTO

Start with business requirements.

---

### 2. Protect Both State and Data

Use:

```text
etcd
+
Resource Backup
+
PV / Database Backup
```

---

### 3. Store Backups Externally

Prefer:

```text
Separate Account
Separate Project
Separate Region
```

where appropriate.

---

### 4. Use Immutable Backups

Protect critical recovery points from deletion.

---

### 5. Test Recovery

Regularly perform:

```text
Restore
Failover
Failback
```

---

### 6. Document Dependencies

Map:

```text
Application
 ↓
Database
 ↓
Identity
 ↓
Network
 ↓
Storage
```

---

### 7. Automate Recovery

Use:

```text
Infrastructure as Code
GitOps
Automation
Backup Tools
```

---

### 8. Monitor Backup Health

Alert on:

```text
Backup Failure
Old Backup
Storage Failure
Restore Failure
```

---

### 9. Maintain Recovery Runbooks

Ensure operators know:

```text
What
When
How
Who
```

---

### 10. Conduct DR Exercises

Practice before a real disaster occurs.

---

# Hands-on Lab 1 – Define RPO and RTO

Choose a test application.

Define:

```text
RPO = 15 minutes
RTO = 1 hour
```

Design a backup and recovery strategy that meets those targets.

---

# Hands-on Lab 2 – etcd Disaster Recovery

In a disposable cluster:

```text
Create etcd Backup
 ↓
Simulate Failure
 ↓
Restore
 ↓
Validate Control Plane
```

Document the exact version-specific recovery procedure.

---

# Hands-on Lab 3 – Namespace Recovery

Create:

```text
Namespace
Deployment
Service
ConfigMap
Secret
```

Back up the namespace.

Delete it.

Restore it.

Validate all resources.

---

# Hands-on Lab 4 – Persistent Data Recovery

Create a PVC containing test data.

Create a supported snapshot or backup.

Delete the workload.

Restore:

```text
PVC
+
Pod
```

Verify the data.

---

# Hands-on Lab 5 – Velero Disaster Recovery

Use Velero to:

```text
Backup
 ↓
Delete Test Namespace
 ↓
Restore
 ↓
Validate
```

Measure:

```text
Recovery Time
```

---

# Hands-on Lab 6 – Cross-Cluster Recovery

Use:

```text
Cluster A
```

Create a backup.

Restore into:

```text
Cluster B
```

Validate:

```text
Applications
Services
Configuration
Storage
```

---

# Hands-on Lab 7 – Cross-Region Simulation

Use two test environments representing:

```text
Region A
Region B
```

Store backups in a location independent of Region A.

Simulate Region A failure.

Recover in Region B.

---

# Hands-on Lab 8 – DNS Failover

Create two test environments.

Configure a DNS failover mechanism.

Simulate:

```text
Primary Failure
```

Verify traffic moves to the recovery environment.

---

# Hands-on Lab 9 – Database Recovery

Create a test database.

Perform:

```text
Database Backup
 ↓
Data Change
 ↓
Simulated Failure
 ↓
Restore
```

Validate data integrity.

---

# Hands-on Lab 10 – Immutable Backup

Configure an object-storage retention policy in a test environment.

Attempt to delete a retained backup.

Verify the protection behavior.

---

# Hands-on Lab 11 – DR Game Day

Create a scenario:

```text
Primary Cluster Unavailable
```

Teams must:

```text
Detect
Assess
Recover
Validate
Communicate
```

Record:

```text
MTTD
MTTR
RPO
RTO
```

---

# Hands-on Lab 12 – Failover Test

Run:

```text
Primary
   ↓
Failure
   ↓
Secondary
```

Measure traffic recovery time.

---

# Hands-on Lab 13 – Failback Test

After recovering the primary:

```text
Secondary
   ↓
Synchronize
   ↓
Primary
   ↓
Failback
```

Verify data consistency.

---

# Hands-on Lab 14 – Dependency Recovery

Create an application dependent on:

```text
Database
Redis
DNS
Secret
```

Recover dependencies in the correct order.

---

# Hands-on Lab 15 – Security Incident Recovery

In a disposable environment, simulate compromised application credentials.

Practice:

```text
Credential Revocation
 ↓
Cluster Isolation
 ↓
Backup Verification
 ↓
Recovery
 ↓
Credential Rotation
 ↓
Validation
```

---

# Hands-on Lab 16 – Recovery Validation

Create automated tests that verify:

```text
HTTP
DNS
Database
Authentication
Storage
```

after recovery.

---

# Hands-on Lab 17 – Measure RTO

Document the exact recovery procedure.

Start a timer.

Recover the application.

Record:

```text
Actual RTO
```

Compare with the target.

---

# Hands-on Lab 18 – Measure RPO

Create data at known timestamps.

Perform scheduled backups.

Simulate failure.

Determine the latest recoverable data point.

---

# Hands-on Lab 19 – Full DR Simulation

Simulate:

```text
Complete Cluster Loss
```

Recover:

```text
Infrastructure
 ↓
Kubernetes
 ↓
Storage
 ↓
Database
 ↓
Applications
 ↓
Traffic
```

---

# Hands-on Lab 20 – Production DR Architecture

Design:

```text
Primary Region
      │
      ├── Kubernetes
      ├── Database
      └── Applications
             │
             ▼
        Backup System
             │
      ┌──────┴──────┐
      ▼             ▼
Immutable      Secondary Region
Backup               │
                     ▼
                Recovery Cluster
```

Document:

```text
RPO
RTO
Backup
Failover
Failback
Security
Monitoring
```

---

# Quick Revision

## Disaster Recovery

```text
Strategy for recovering from major failures
```

---

## Business Continuity

```text
Keeping business operations functioning during disruption
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

## MTTD

```text
Mean Time To Detect
```

---

## MTTR

```text
Mean Time To Recovery
```

---

## Warm Standby

```text
Partially prepared recovery environment
```

---

## Cold Standby

```text
Environment requiring significant provisioning during recovery
```

---

## Active-Passive

```text
Primary environment + standby environment
```

---

## Active-Active

```text
Multiple environments actively serving traffic
```

---

## Failover

```text
Move service from failed environment to recovery environment
```

---

## Failback

```text
Return service to the primary/preferred environment
```

---

## Immutable Backup

```text
Backup protected against modification/deletion during retention
```

---

## Air-Gapped Backup

```text
Backup isolated from production
```

---

## DR Test

```text
Controlled exercise proving recovery capability
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

Check Pods:

```bash
kubectl get pods -A
```

Check Services:

```bash
kubectl get svc -A
```

Check PVCs:

```bash
kubectl get pvc -A
```

Check PVs:

```bash
kubectl get pv
```

Check CRDs:

```bash
kubectl get crd
```

Check events:

```bash
kubectl get events -A
```

Check PDBs:

```bash
kubectl get pdb -A
```

Create Velero backup:

```bash
velero backup create production-backup
```

List backups:

```bash
velero backup get
```

Describe backup:

```bash
velero backup describe production-backup
```

Create restore:

```bash
velero restore create \
  --from-backup production-backup
```

List restores:

```bash
velero restore get
```

Create etcd snapshot:

```bash
etcdctl snapshot save snapshot.db
```

Check snapshot:

```bash
etcdctl snapshot status snapshot.db
```

---

# Interview Questions

## Basic

- What is Disaster Recovery?
- What is the difference between HA and DR?
- What is RPO?
- What is RTO?
- What is MTTR?
- What is MTTD?
- What is a disaster?
- What is Business Continuity?
- What is Business Impact Analysis?
- What is failover?
- What is failback?
- What is a warm standby?
- What is a cold standby?
- What is active-passive DR?
- What is active-active DR?
- Why are backups important for DR?

---

## Intermediate

- How would you recover a Kubernetes cluster?
- How would you recover etcd?
- How would you recover Persistent Volumes?
- How would you recover a database running in Kubernetes?
- How does Velero help with DR?
- How would you perform a cross-cluster restore?
- How would you perform cross-region recovery?
- How do you protect backups from ransomware?
- How do immutable backups help?
- Why should backups be stored outside the cluster?
- What dependencies must be recovered before an application?
- How do you test disaster recovery?
- What is the difference between snapshot and backup?
- How do you measure RPO and RTO?

---

## Advanced

- Design a multi-region Kubernetes DR architecture.
- Design an active-active Kubernetes DR strategy.
- Design an active-passive DR strategy.
- How would you recover after complete etcd loss?
- How would you recover after accidental production namespace deletion?
- How would you recover from ransomware?
- How would you recover a stateful application?
- How would you design cross-region database replication?
- How would you design an immutable backup architecture?
- How would you test a production DR plan without causing downtime?
- How would you design a DR runbook?
- How would you calculate whether an architecture meets its RPO and RTO?
- How would you perform failback after disaster recovery?
- How would you recover when both the cluster and its cloud region are unavailable?

---

# Interview Scenario 1

### Question

> What is the difference between High Availability and Disaster Recovery?

### Answer

HA focuses on continuing service when individual components fail:

```text
Node Failure
 ↓
Another Node
 ↓
Service Continues
```

DR focuses on recovering from major disasters:

```text
Cluster / Region Loss
 ↓
Recovery Environment
 ↓
Restore
```

HA minimizes downtime.

DR enables recovery.

---

# Interview Scenario 2

### Question

> What is RPO?

### Answer

RPO defines acceptable data loss.

Example:

```text
RPO = 15 minutes
```

means the recovery strategy should target a recovery point no older than approximately 15 minutes under the defined failure scenario.

---

# Interview Scenario 3

### Question

> What is RTO?

### Answer

RTO defines the target recovery time.

Example:

```text
RTO = 1 hour
```

means the service should target restoration within approximately one hour.

---

# Interview Scenario 4

### Question

> How would you recover a Kubernetes cluster after complete control-plane loss?

### Answer

Conceptually:

```text
Identify Disaster
 ↓
Provision Recovery Infrastructure
 ↓
Restore etcd / Cluster State
 ↓
Recover Control Plane
 ↓
Validate API Server
 ↓
Recover Worker Connectivity
 ↓
Restore Storage
 ↓
Restore Applications
 ↓
Validate
 ↓
Restore Traffic
```

The exact procedure depends on the Kubernetes distribution and architecture.

---

# Interview Scenario 5

### Question

> How would you protect Kubernetes backups from ransomware?

### Answer

Use:

```text
Immutable Backups
+
Separate Credentials
+
Encryption
+
Off-Site Storage
+
Cross-Region Copies
+
Air-Gapped Copies
+
Least Privilege
```

The attacker should not be able to destroy every recovery copy using compromised production credentials.

---

# Interview Scenario 6

### Question

> Why isn't a VolumeSnapshot enough for disaster recovery?

### Answer

A VolumeSnapshot may remain tied to the underlying storage system.

If the storage system or region is lost:

```text
Snapshot
   X
```

may also become unavailable.

Therefore use:

```text
Snapshots
+
Independent Backups
+
Off-Site Copies
```

where required.

---

# Interview Scenario 7

### Question

> What should be recovered first?

### Answer

A common dependency order is:

```text
Infrastructure
 ↓
Network
 ↓
Identity
 ↓
Kubernetes
 ↓
Storage
 ↓
Database
 ↓
Applications
 ↓
Ingress / Traffic
```

The exact order depends on the environment.

---

# Interview Scenario 8

### Question

> How do you test disaster recovery?

### Answer

Use controlled exercises:

```text
Backup Restore
Failover
Cross-Cluster Restore
Cross-Region Restore
Game Day
Chaos Testing
Failback
```

Measure:

```text
RPO
RTO
MTTD
MTTR
Data Integrity
```

---

# Interview Scenario 9

### Question

> What is the difference between active-active and active-passive DR?

### Answer

Active-passive:

```text
Primary → Serves Traffic
Secondary → Standby
```

Active-active:

```text
Primary → Serves Traffic
Secondary → Also Serves Traffic
```

Active-active can provide faster failover but introduces significantly more complexity, especially around stateful data.

---

# Interview Scenario 10

### Question

> Design a production Kubernetes DR architecture.

### Answer

Use:

```text
Primary Region
      │
      ├── HA Kubernetes
      ├── HA Database
      └── Applications
             │
             ▼
        Backup System
             │
      ┌──────┴───────┐
      ▼              ▼
Immutable        Secondary
Backup            Region
                      │
                      ▼
                Recovery Cluster
```

Add:

```text
Global Traffic Management
+
Data Replication
+
Encryption
+
Immutable Backups
+
Monitoring
+
DR Runbooks
+
Regular Testing
```

---

# Production DR Checklist

```text
☑ Business-critical services identified
☑ RPO defined
☑ RTO defined
☑ Dependencies documented
☑ etcd backup configured
☑ Kubernetes resource backup configured
☑ Persistent data backup configured
☑ Database backup configured
☑ Backup stored outside primary cluster
☑ Cross-region copy available
☑ Immutable backup available
☑ Encryption enabled
☑ Backup credentials isolated
☑ Recovery cluster strategy defined
☑ DNS failover strategy defined
☑ Traffic failover tested
☑ Identity recovery tested
☑ Network recovery tested
☑ Storage recovery tested
☑ Application recovery tested
☑ Failover tested
☑ Failback tested
☑ RTO measured
☑ RPO measured
☑ DR runbook documented
☑ Recovery contacts documented
☑ Regular DR exercises scheduled
```

---

# Chapter Summary

Disaster Recovery protects Kubernetes environments against failures larger than normal HA scenarios.

A mature DR strategy includes:

```text
Business Requirements
+
RPO
+
RTO
+
Backup
+
Recovery Environment
+
Failover
+
Failback
+
Testing
```

Kubernetes DR must consider:

```text
Control Plane
etcd
Worker Nodes
Networking
Storage
Databases
Applications
DNS
Identity
Security
```

A strong architecture is:

```text
Primary Cluster
       │
       ▼
Backup
       │
       ├───────────────┐
       ▼               ▼
Immutable Copy    Secondary Region
                       │
                       ▼
                 Recovery Cluster
```

The most important principle is:

> **Disaster Recovery is not a backup file or a secondary Kubernetes cluster by itself. It is a tested end-to-end capability that combines protected backups, recovery infrastructure, application dependencies, traffic failover, security, measurable RPO/RTO targets, and a validated recovery procedure.**

---

## Next Chapter

# Chapter 70 – Cluster Maintenance

Topics will include:

- Cluster Maintenance Fundamentals
- Maintenance Planning
- Maintenance Windows
- Change Management
- Cluster Health Checks
- Node Maintenance
- Control Plane Maintenance
- Worker Node Maintenance
- Cordon
- Drain
- Uncordon
- Pod Eviction
- Pod Disruption Budgets
- Node Replacement
- Node Reboot
- Operating System Updates
- Kernel Updates
- Container Runtime Updates
- kubelet Maintenance
- Kubernetes Component Maintenance
- CNI Maintenance
- CSI Maintenance
- CoreDNS Maintenance
- Ingress Maintenance
- Gateway Maintenance
- Certificate Maintenance
- etcd Maintenance
- etcd Defragmentation
- Disk Maintenance
- Storage Maintenance
- Network Maintenance
- Capacity Management
- Resource Cleanup
- Image Cleanup
- Unused Resource Cleanup
- Namespace Cleanup
- Stale Resources
- Failed Pods
- Completed Jobs
- Old ReplicaSets
- Orphaned Resources
- Monitoring During Maintenance
- Logging During Maintenance
- Security During Maintenance
- Backup Before Maintenance
- Maintenance Automation
- Rolling Maintenance
- Zero-Downtime Maintenance
- Planned Maintenance
- Emergency Maintenance
- Maintenance Runbooks
- Maintenance Validation
- Post-Maintenance Checks
- Troubleshooting
- Production Maintenance Strategy
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---