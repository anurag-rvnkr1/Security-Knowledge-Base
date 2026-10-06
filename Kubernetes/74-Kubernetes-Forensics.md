# Chapter 74 – Kubernetes Forensics

## Overview

Kubernetes Forensics is the process of collecting, preserving, analyzing, and correlating digital evidence from Kubernetes clusters to understand a security incident.

Kubernetes forensics differs from traditional host forensics because workloads are often:

```text
Ephemeral
Dynamic
Short-Lived
Automatically Recreated
Distributed
```

A Pod may disappear before an investigator can inspect it.

Therefore, forensic readiness is critical.

A simplified Kubernetes forensic workflow is:

```text
Detect
   ↓
Preserve
   ↓
Collect
   ↓
Validate
   ↓
Analyze
   ↓
Correlate
   ↓
Reconstruct Timeline
   ↓
Determine Root Cause
   ↓
Report
```

The investigation may span:

```text
Pod
 ↓
Container
 ↓
Node
 ↓
Cluster
 ↓
Cloud
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes forensics fundamentals
- Digital forensics
- Kubernetes forensic challenges
- Evidence sources
- Evidence preservation
- Chain of custody
- Volatile evidence
- Non-volatile evidence
- Pod forensics
- Container forensics
- Node forensics
- Control plane forensics
- API Server forensics
- etcd forensics
- kubelet forensics
- Container runtime forensics
- Kubernetes audit logs
- Application logs
- System logs
- Network logs
- DNS logs
- Cloud logs
- Runtime security data
- Process analysis
- File-system analysis
- Memory forensics
- Network forensics
- Container image forensics
- Image digests
- SBOM
- Malware analysis
- Timeline analysis
- IOC collection
- IOA collection
- Attack reconstruction
- Initial access
- Execution
- Persistence
- Privilege escalation
- Credential access
- Discovery
- Lateral movement
- Collection
- Exfiltration
- Impact
- Kubernetes artifacts
- Pod YAML
- Events
- ReplicaSets
- Deployments
- DaemonSets
- StatefulSets
- Jobs
- CronJobs
- ServiceAccounts
- Roles
- RoleBindings
- Secrets
- ConfigMaps
- NetworkPolicies
- Ingress
- Gateway
- Admission Controllers
- CRDs
- Persistent Volumes
- Container runtime artifacts
- containerd
- CRI-O
- Node evidence
- kubelet evidence
- Linux logs
- systemd
- journald
- kernel logs
- authentication logs
- cloud forensics
- forensic readiness
- evidence collection procedures
- evidence integrity
- hashing
- secure evidence storage
- timeline construction
- hypothesis testing
- root cause analysis
- forensic tools
- kubectl
- crictl
- journalctl
- Linux tools
- runtime tools
- SIEM
- incident-response integration
- legal considerations
- compliance
- privacy
- production forensics
- best practices
- hands-on labs
- common mistakes
- quick revision
- interview questions

---

# What Is Digital Forensics?

Digital forensics is the systematic process of:

```text
Collecting
+
Preserving
+
Analyzing
+
Interpreting
+
Reporting
```

digital evidence.

The goal is to determine:

```text
What happened?
When?
How?
Who?
What was affected?
What evidence supports the conclusion?
```

---

# Kubernetes Forensics

Kubernetes forensics applies these principles to:

```text
Cluster
Control Plane
Nodes
Containers
Pods
Applications
Network
Storage
Cloud
```

---

# Why Kubernetes Forensics Is Difficult

Traditional servers often remain stable for long periods.

Kubernetes workloads can be:

```text
Created
 ↓
Run
 ↓
Deleted
 ↓
Recreated
```

within minutes.

---

# Ephemeral Workloads

Example:

```text
Malicious Pod
     ↓
Attacker Activity
     ↓
Pod Deleted
     ↓
Replacement Pod Created
```

If logging was not centralized, evidence may be lost.

---

# Forensic Readiness

Forensic readiness means designing the environment so useful evidence is available when an incident occurs.

Important controls:

```text
Audit Logging
Central Logging
Runtime Monitoring
Network Visibility
Cloud Logging
Time Synchronization
Evidence Storage
Backup
```

---

# Forensic Readiness Architecture

```text
Kubernetes
    │
    ├── Audit Logs
    ├── Pod Logs
    ├── Node Logs
    ├── Runtime Logs
    ├── Network Logs
    └── Events
           │
           ▼
      Central Storage
           │
           ▼
          SIEM
           │
           ▼
       Investigation
```

---

# Evidence Sources

Potential sources include:

```text
Kubernetes API
Audit Logs
Pod Specifications
Pod Logs
Events
Container Runtime
Node Filesystem
Node Logs
Process Information
Network Logs
DNS Logs
Cloud Logs
Container Images
Registry Logs
CI/CD Logs
Git History
SIEM
Runtime Security
```

---

# Evidence Categories

Evidence can be broadly classified as:

```text
Volatile
Non-Volatile
```

---

# Volatile Evidence

Volatile evidence can disappear quickly.

Examples:

```text
Running Processes
Memory
Network Connections
Active Sessions
Temporary Files
Current Container State
```

---

# Non-Volatile Evidence

Examples:

```text
Disk
Logs
Container Images
Audit Records
Backups
Configuration
Git History
```

---

# Evidence Priority

A simplified order is:

```text
Memory
 ↓
Processes
 ↓
Network Connections
 ↓
Runtime State
 ↓
Logs
 ↓
Filesystem
 ↓
Backups
```

The exact order depends on the incident and operational constraints.

---

# Chain of Custody

Chain of custody documents:

```text
Evidence
 ↓
Collected By
 ↓
Date / Time
 ↓
Method
 ↓
Storage
 ↓
Access History
```

---

# Why Chain of Custody Matters

It establishes:

```text
Evidence Authenticity
+
Evidence Integrity
+
Handling Accountability
```

This becomes especially important for legal, regulatory, or disciplinary investigations.

---

# Evidence Integrity

Use:

```text
Hashing
Access Control
Immutable Storage
Metadata
Audit Trails
```

---

# Hashing Evidence

A cryptographic hash can help verify that evidence has not changed.

Example:

```bash
sha256sum evidence.tar
```

Result:

```text
<hash>  evidence.tar
```

Record the hash with the evidence metadata.

---

# Time Synchronization

Accurate timestamps are critical for timeline analysis.

Use consistent time synchronization across:

```text
Nodes
Applications
Cloud
Logging Systems
SIEM
```

---

# Kubernetes Artifact

A Kubernetes artifact is information that helps reconstruct cluster state or activity.

Examples:

```text
Pod
Deployment
ReplicaSet
ServiceAccount
Role
RoleBinding
Secret
ConfigMap
Event
NetworkPolicy
```

---

# Pod Forensics

Investigate:

```text
Pod Name
Namespace
UID
Node
Image
Image Digest
Command
Arguments
Environment
Volumes
ServiceAccount
SecurityContext
Network
```

---

# Collect Pod YAML

```bash
kubectl get pod <pod-name> -o yaml
```

Save the output as evidence.

---

# Collect Pod Description

```bash
kubectl describe pod <pod-name>
```

This may provide:

```text
Events
Mounts
Image
Node
Conditions
Container State
Restart Count
```

---

# Pod UID

Pod names may be reused or replaced.

The Pod UID provides a more specific identity for a particular Pod instance.

Retrieve:

```bash
kubectl get pod <pod-name> \
  -o jsonpath='{.metadata.uid}'
```

---

# Pod Logs

Collect:

```bash
kubectl logs <pod-name>
```

For a specific container:

```bash
kubectl logs <pod-name> -c <container-name>
```

---

# Previous Container Logs

If a container restarted:

```bash
kubectl logs <pod-name> --previous
```

This can be valuable when investigating crashes or short-lived malicious activity.

---

# Container Forensics

Investigate:

```text
Image
Process
Filesystem
Environment
Capabilities
Mounts
Network
ServiceAccount
Runtime
```

---

# Container Image Evidence

Record:

```text
Registry
Repository
Tag
Digest
Creation Time
Build Information
SBOM
Scan Results
```

---

# Image Digest

Prefer investigating an exact image digest:

```text
registry.example/app@sha256:<digest>
```

instead of relying only on:

```text
app:latest
```

Tags can be mutable.

---

# Image Provenance

Investigate:

```text
Where was the image built?
Which CI/CD job?
Which source commit?
Which builder?
Which registry?
Who pushed it?
```

---

# Registry Logs

Registry logs can help determine:

```text
Who Pulled?
Who Pushed?
When?
Which Image?
From Where?
```

---

# Container Runtime Forensics

Common runtimes include:

```text
containerd
CRI-O
```

Runtime evidence may include:

```text
Container Metadata
Container Lifecycle
Image Information
Process Information
Runtime Logs
```

---

# crictl

`crictl` can interact with CRI-compatible container runtimes.

Example:

```bash
crictl ps
```

List all containers:

```bash
crictl ps -a
```

List images:

```bash
crictl images
```

Inspect a container:

```bash
crictl inspect <container-id>
```

---

# Runtime Evidence

Useful information includes:

```text
Container ID
Image
Created Time
Started Time
Stopped Time
Command
Environment
Mounts
```

---

# Node Forensics

If a node may be compromised, investigate:

```text
Processes
Memory
Filesystem
Network
Users
Authentication
kubelet
Runtime
Kernel
Logs
```

---

# Node Identification

Find Pod placement:

```bash
kubectl get pods -A -o wide
```

Then identify the corresponding node.

---

# Node Details

```bash
kubectl describe node <node-name>
```

Review:

```text
Conditions
Addresses
Labels
Taints
Pods
Events
```

---

# kubelet Forensics

kubelet is a key node-level component.

Investigate:

```text
kubelet Logs
Configuration
Authentication
Authorization
Version
API Connections
```

---

# kubelet Logs

On a Linux node:

```bash
journalctl -u kubelet
```

For recent entries:

```bash
journalctl -u kubelet --since "1 hour ago"
```

---

# Linux Forensics

Node investigation may include:

```text
Processes
Users
Cron
Systemd
SSH
Network
Filesystem
Kernel
```

---

# Process Analysis

Look for:

```bash
ps aux
```

or:

```bash
ps -ef
```

Suspicious characteristics:

```text
Unknown Process
Unexpected Binary
Unexpected Parent
High CPU
Network Connection
Root Process
```

---

# Network Connections

Useful Linux commands include:

```bash
ss -tulpn
```

or:

```bash
ss -antp
```

Look for:

```text
Unexpected Remote IP
Unexpected Port
Unexpected Process
```

---

# Authentication Logs

Depending on the Linux distribution:

```text
/var/log/auth.log
```

or:

```text
/var/log/secure
```

Investigate:

```text
Successful Login
Failed Login
SSH Access
Privilege Escalation
```

---

# systemd

Systemd can reveal:

```text
Service Creation
Service Changes
Service Failures
```

Review:

```bash
systemctl list-units
```

---

# journald

Query system logs:

```bash
journalctl
```

Time-limited:

```bash
journalctl --since "2 hours ago"
```

---

# Kernel Logs

Kernel logs may contain evidence of:

```text
Kernel Exploitation
Container Runtime Problems
Network Events
Filesystem Events
```

Check:

```bash
dmesg
```

or:

```bash
journalctl -k
```

---

# Filesystem Forensics

Look for:

```text
Unexpected Files
Modified Binaries
Temporary Files
Persistence
Malware
Credentials
Configuration Changes
```

---

# File Metadata

Useful information:

```text
Created
Modified
Accessed
Permissions
Owner
Hash
```

---

# Persistence Artifacts

Investigate:

```text
Cron
Systemd Services
SSH Keys
Shell Profiles
Startup Scripts
Kubernetes Jobs
CronJobs
DaemonSets
Deployments
Admission Components
```

---

# Kubernetes Persistence

Attackers may create:

```text
Deployment
DaemonSet
CronJob
Job
ServiceAccount
Secret
ConfigMap
```

Investigate recently created resources.

---

# ReplicaSet Investigation

A ReplicaSet may preserve evidence about a previous Deployment revision.

Check:

```bash
kubectl get replicasets -A
```

---

# Deployment Investigation

Check:

```bash
kubectl get deployments -A
```

Then:

```bash
kubectl describe deployment <deployment-name>
```

Review:

```text
Image
Revision
Replicas
Pod Template
ServiceAccount
```

---

# DaemonSet Investigation

DaemonSets run Pods across nodes.

Check:

```bash
kubectl get daemonsets -A
```

An unexpected DaemonSet can be a persistence mechanism.

---

# StatefulSet Investigation

Check:

```bash
kubectl get statefulsets -A
```

Investigate:

```text
Images
Volumes
ServiceAccounts
Recent Changes
```

---

# Job Investigation

Check:

```bash
kubectl get jobs -A
```

Investigate unexpected Jobs.

---

# CronJob Investigation

Check:

```bash
kubectl get cronjobs -A
```

CronJobs can provide recurring execution.

---

# ServiceAccount Forensics

Investigate:

```bash
kubectl get serviceaccounts -A
```

Determine:

```text
Creation
Usage
Permissions
Bindings
Token Exposure
```

---

# Role Forensics

Check:

```bash
kubectl get roles -A
```

Review suspicious permissions:

```text
Secrets
Pods
Exec
Nodes
RBAC
```

---

# RoleBinding Forensics

Check:

```bash
kubectl get rolebindings -A
```

Determine:

```text
Subject
Role
Namespace
```

---

# ClusterRole Forensics

Check:

```bash
kubectl get clusterroles
```

Look for:

```text
Wildcard Permissions
Sensitive Resources
Unexpected Custom Roles
```

---

# ClusterRoleBinding Forensics

Check:

```bash
kubectl get clusterrolebindings
```

Identify:

```text
Unexpected Users
Unexpected Groups
Unexpected ServiceAccounts
```

---

# Secret Forensics

Secrets may contain:

```text
Passwords
Tokens
Certificates
API Keys
Cloud Credentials
```

Do not casually print Secret values into terminals, tickets, or logs.

Investigate access patterns through audit logs and controlled evidence handling.

---

# Secret Metadata

Collect metadata without unnecessarily exposing values:

```bash
kubectl get secret <secret-name> -o yaml
```

Use appropriate redaction before sharing evidence.

---

# ConfigMap Forensics

Check:

```bash
kubectl get configmaps -A
```

Investigate unexpected changes.

ConfigMaps may contain:

```text
Application Configuration
Endpoints
Feature Flags
Scripts
```

---

# NetworkPolicy Forensics

Check:

```bash
kubectl get networkpolicy -A
```

Determine:

```text
What Traffic Was Allowed?
What Traffic Was Blocked?
Was Policy Recently Changed?
```

---

# Ingress Forensics

Check:

```bash
kubectl get ingress -A
```

Investigate:

```text
Host
TLS
Backend
Recent Changes
External Exposure
```

---

# Gateway Forensics

Check:

```bash
kubectl get gateway -A
```

and:

```bash
kubectl get httproute -A
```

Investigate:

```text
Routes
Listeners
TLS
Backend Targets
Recent Changes
```

---

# Admission Controller Forensics

Investigate:

```text
Mutating Webhooks
Validating Webhooks
Admission Policies
Policy Changes
```

An attacker who compromises admission infrastructure may affect future workloads.

---

# CRD Forensics

Custom Resources can contain application-specific control logic.

Check:

```bash
kubectl get crd
```

Then identify suspicious custom resources.

---

# Kubernetes Audit Logs

Audit logs are among the most valuable Kubernetes forensic sources.

They can reveal:

```text
Identity
Timestamp
Source IP
Verb
Resource
Namespace
Object
Response
```

---

# Audit Event Example

Conceptually:

```text
User
 ↓
GET
 ↓
Secret
 ↓
Production Namespace
```

This can help establish:

```text
Who accessed what?
```

---

# Audit Log Investigation

Look for suspicious:

```text
create
delete
patch
update
get
list
watch
exec
```

The relevance of each verb depends on the resource and context.

---

# Sensitive API Activity

Pay particular attention to access involving:

```text
Secrets
ServiceAccounts
Roles
ClusterRoles
RoleBindings
Pods
Nodes
Deployments
Admission Resources
```

---

# kubectl exec Forensics

`kubectl exec` can provide interactive access into a container.

Investigate unexpected exec activity through:

```text
Audit Logs
Runtime Logs
Container Logs
User Identity
Source IP
```

---

# Cloud Forensics

Cloud-hosted Kubernetes requires investigation beyond Kubernetes itself.

Review:

```text
IAM
VPC
Security Groups
Firewall
Load Balancers
Object Storage
Cloud Audit Logs
Compute Instances
Managed Kubernetes Control Plane Logs
```

---

# Cloud Credential Compromise

If Kubernetes credentials can access cloud APIs:

```text
Kubernetes Compromise
       ↓
Cloud Credential
       ↓
Cloud API
       ↓
Cloud Resources
```

The investigation must expand to the cloud environment.

---

# Network Forensics

Network evidence can help establish:

```text
Source
Destination
Port
Protocol
Time
Volume
```

---

# DNS Forensics

DNS can reveal:

```text
Malicious Domains
C2 Infrastructure
Data Exfiltration
Unexpected External Services
```

---

# Network Flow Analysis

Look for:

```text
Unexpected External IP
Unexpected Port
Unexpected Protocol
Unexpected Data Volume
Unexpected DNS Domain
```

---

# Container Image Forensics

Preserve the exact image where possible.

Record:

```text
Registry
Repository
Tag
Digest
SBOM
Build Metadata
Signature
```

---

# Image Hash

Use the digest or a cryptographic hash to identify exact content.

Example:

```text
sha256:<digest>
```

---

# Malware Analysis

If malware is discovered:

```text
Preserve Sample
 ↓
Hash Sample
 ↓
Identify
 ↓
Analyze Safely
 ↓
Extract IOCs
```

Do not execute unknown malware on production systems.

---

# IOC Collection

Collect:

```text
IP
Domain
URL
Hash
Filename
Process
Image Digest
Credential
```

---

# IOA Collection

Collect behavioral indicators:

```text
Unexpected Exec
Privilege Escalation
Secret Enumeration
Mass Resource Listing
Unexpected Pod Creation
Suspicious Network Activity
```

---

# Timeline Analysis

A timeline combines evidence from multiple sources.

Example:

```text
10:01 API Login
10:02 Pod Created
10:03 Exec
10:05 Secret Read
10:06 External DNS Request
10:07 New ServiceAccount Created
10:10 Data Transfer
```

---

# Timeline Sources

Correlate:

```text
Kubernetes Audit
Pod Logs
Node Logs
Cloud Logs
Network Logs
DNS Logs
Registry Logs
CI/CD Logs
```

---

# Timeline Correlation

Suppose:

```text
Audit Log
10:02 → Pod Created
```

and:

```text
Runtime Log
10:03 → Container Started
```

and:

```text
DNS
10:05 → Suspicious Domain
```

Correlation can establish a probable sequence.

---

# Hypothesis Testing

Forensics should not rely on assumptions.

Example hypothesis:

```text
Attacker entered through vulnerable application.
```

Test against:

```text
Application Logs
Network Logs
Audit Logs
Image History
```

---

# Evidence-Based Conclusion

A strong conclusion is:

```text
Supported by Evidence
```

rather than:

```text
Likely because it seems suspicious
```

---

# Initial Access Investigation

Potential entry points:

```text
Internet-Facing Application
Stolen Credentials
Vulnerable Image
Compromised CI/CD
Exposed API
Misconfigured Service
```

---

# Execution Investigation

Look for:

```text
Container Start
kubectl exec
Unexpected Process
Script Execution
Job Creation
CronJob
```

---

# Persistence Investigation

Look for:

```text
Deployment
DaemonSet
CronJob
ServiceAccount
Secret
Admission Component
CI/CD Change
```

---

# Privilege Escalation Investigation

Review:

```text
RBAC Changes
ServiceAccounts
Capabilities
Privileged Pods
Host Mounts
Host Namespaces
```

---

# Credential Access Investigation

Look for:

```text
Secret Access
Token Exposure
Cloud Credential Access
Registry Credentials
Application Credentials
```

---

# Discovery Investigation

Attackers may enumerate:

```text
Namespaces
Pods
Services
Secrets
Roles
Nodes
Cloud Resources
```

---

# Lateral Movement Investigation

Trace:

```text
Identity
 ↓
Pod
 ↓
Service
 ↓
Credential
 ↓
Another Workload
```

---

# Collection Investigation

Potential targets:

```text
Database
Secrets
ConfigMaps
Object Storage
Application Data
Logs
```

---

# Exfiltration Investigation

Look for:

```text
Large Outbound Traffic
Unexpected External IPs
Suspicious DNS
Cloud Storage Uploads
Encrypted Channels
```

---

# Impact Investigation

Potential impact:

```text
Data Loss
Data Encryption
Service Disruption
Cryptomining
Resource Exhaustion
Application Destruction
```

---

# Forensic Collection Workflow

```text
Identify
 ↓
Preserve
 ↓
Collect
 ↓
Hash
 ↓
Store
 ↓
Analyze
 ↓
Correlate
 ↓
Report
```

---

# Evidence Collection Example

Create an evidence directory:

```bash
mkdir incident-evidence
```

Collect Pod YAML:

```bash
kubectl get pod <pod-name> -o yaml \
  > incident-evidence/pod.yaml
```

Collect description:

```bash
kubectl describe pod <pod-name> \
  > incident-evidence/pod-describe.txt
```

Collect logs:

```bash
kubectl logs <pod-name> \
  > incident-evidence/pod.log
```

---

# Collect Events

```bash
kubectl get events -A \
  --sort-by=.lastTimestamp \
  > incident-evidence/events.txt
```

---

# Collect Workload Inventory

```bash
kubectl get pods -A -o wide \
  > incident-evidence/pods.txt
```

---

# Collect Node Inventory

```bash
kubectl get nodes -o wide \
  > incident-evidence/nodes.txt
```

---

# Collect RBAC Information

```bash
kubectl get roles -A \
  > incident-evidence/roles.txt
```

```bash
kubectl get rolebindings -A \
  > incident-evidence/rolebindings.txt
```

```bash
kubectl get clusterrolebindings \
  > incident-evidence/clusterrolebindings.txt
```

---

# Hash Evidence

```bash
sha256sum incident-evidence/*
```

Store hashes separately from the working evidence set where appropriate.

---

# Secure Evidence Storage

Use:

```text
Restricted Access
Encryption
Immutable Storage
Audit Logging
Retention Policy
```

---

# Evidence Redaction

Sensitive evidence may contain:

```text
Passwords
Tokens
API Keys
Personal Data
Customer Data
```

Redact before sharing outside the authorized investigation team.

---

# Privacy Considerations

Forensic collection should follow:

```text
Authorization
Data Minimization
Access Control
Retention Requirements
Applicable Laws
Organizational Policy
```

Do not collect unrelated personal data unnecessarily.

---

# Legal Considerations

Depending on the incident, evidence may have legal implications.

Coordinate with appropriate:

```text
Legal
Compliance
Privacy
HR
Law Enforcement
```

when required.

---

# Forensics and Incident Response

Forensics supports incident response:

```text
Incident
 ↓
Containment
 ↓
Forensic Investigation
 ↓
Root Cause
 ↓
Eradication
 ↓
Recovery
```

---

# Forensics and SIEM

SIEM provides centralized correlation:

```text
Kubernetes
+
Cloud
+
Network
+
Node
+
Application
```

This makes timeline reconstruction easier.

---

# Production Forensic Architecture

```text
                     Kubernetes
                         │
        ┌────────────────┼─────────────────┐
        ▼                ▼                 ▼
   Audit Logs       Runtime Logs       Pod Logs
        │                │                 │
        └────────────────┼─────────────────┘
                         ▼
                    Log Platform
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Network       Cloud       SIEM
             │           │           │
             └───────────┼───────────┘
                         ▼
                   Investigation
                         │
                ┌────────┴────────┐
                ▼                 ▼
             Evidence          Timeline
                │                 │
                └────────┬────────┘
                         ▼
                    Root Cause
```

---

# Common Mistakes

## 1. No Centralized Logs

Ephemeral workloads can disappear before investigation.

---

## 2. Deleting Evidence Too Quickly

Pod deletion may destroy useful runtime evidence.

---

## 3. Ignoring Node Evidence

A compromised Pod may indicate a node compromise.

---

## 4. Ignoring Cloud Logs

Managed Kubernetes often depends heavily on cloud infrastructure.

---

## 5. Trusting Pod Names

Pod names can change.

Use:

```text
UID
Image Digest
Node
Timestamp
```

for precise identification.

---

## 6. Using Mutable Image Tags

Always record the exact image digest where possible.

---

## 7. Exposing Secrets During Investigation

Do not unnecessarily print credentials.

---

## 8. No Time Synchronization

Incorrect timestamps make correlation difficult.

---

## 9. No Evidence Hashing

Evidence integrity becomes harder to demonstrate.

---

## 10. No Chain of Custody

This can weaken evidence handling for formal investigations.

---

## 11. Investigating Without Scope

Always determine:

```text
Pod
Node
Namespace
Cluster
Cloud
```

impact.

---

## 12. Assuming the First Finding Is the Root Cause

The first suspicious artifact may only be a symptom.

---

# Best Practices

### 1. Enable Audit Logging

Maintain sufficient retention.

---

### 2. Centralize Logs

Do not rely solely on local container logs.

---

### 3. Maintain Forensic Readiness

Prepare before an incident.

---

### 4. Preserve Evidence

Especially for serious incidents.

---

### 5. Record Image Digests

Avoid relying solely on tags.

---

### 6. Maintain Accurate Time

Use reliable time synchronization.

---

### 7. Protect Evidence

Use:

```text
Encryption
Access Control
Immutable Storage
Hashing
```

---

### 8. Integrate Cloud Evidence

Investigate:

```text
IAM
Network
Compute
Storage
```

alongside Kubernetes.

---

### 9. Minimize Sensitive Data Exposure

Redact credentials and unnecessary personal data.

---

### 10. Build Investigation Runbooks

Document:

```text
What to Collect
Where to Collect
How to Store
Who Can Access
```

---

# Hands-on Lab 1 – Pod Evidence Collection

Create a test Pod.

Collect:

```bash
kubectl get pod <pod> -o yaml
kubectl describe pod <pod>
kubectl logs <pod>
```

Store each output as evidence.

---

# Hands-on Lab 2 – Kubernetes Timeline

Collect:

```bash
kubectl get events -A --sort-by=.lastTimestamp
```

Combine with:

```text
Pod Logs
Audit Logs
```

Build a timeline.

---

# Hands-on Lab 3 – Image Forensics

Deploy an image.

Record:

```text
Tag
Digest
Registry
```

Inspect:

```bash
kubectl get pod <pod> -o yaml
```

Determine the exact image being executed.

---

# Hands-on Lab 4 – Runtime Forensics

On a disposable node:

```bash
crictl ps -a
```

Inspect a container:

```bash
crictl inspect <container-id>
```

Record:

```text
Container ID
Image
Start Time
Command
Mounts
```

---

# Hands-on Lab 5 – Node Forensics

On a test node collect:

```bash
ps aux
```

```bash
ss -antp
```

```bash
journalctl -u kubelet
```

```bash
journalctl -k
```

Analyze suspicious activity.

---

# Hands-on Lab 6 – ServiceAccount Investigation

Create a test ServiceAccount.

Review:

```bash
kubectl get serviceaccount <name> -o yaml
```

Then inspect:

```text
RoleBindings
ClusterRoleBindings
```

Determine the account's permissions.

---

# Hands-on Lab 7 – RBAC Forensics

Create a controlled RBAC change.

Record:

```text
Before
Change
After
```

Use audit logs to determine:

```text
Who
Changed What
When
```

---

# Hands-on Lab 8 – Network Forensics

Generate controlled Pod-to-Pod traffic.

Review:

```text
Network Policy
Flow Logs
DNS
Application Logs
```

Determine:

```text
Source
Destination
Port
Time
```

---

# Hands-on Lab 9 – Evidence Hashing

Collect evidence files.

Run:

```bash
sha256sum incident-evidence/*
```

Store the hashes.

Modify a file and calculate its hash again.

Observe the difference.

---

# Hands-on Lab 10 – Malicious Image Investigation

Use a harmless simulated malicious image.

Investigate:

```text
Image
Digest
Registry
Deployment
Runtime
Network
```

Extract:

```text
IOC
IOA
```

---

# Hands-on Lab 11 – Persistence Investigation

Create controlled test resources:

```text
Deployment
DaemonSet
CronJob
ServiceAccount
```

Practice identifying unexpected resources.

---

# Hands-on Lab 12 – Full Kubernetes Forensic Exercise

Simulate:

```text
Initial Access
 ↓
Compromised Pod
 ↓
ServiceAccount Abuse
 ↓
Secret Access
 ↓
External Connection
```

Collect evidence from:

```text
Kubernetes
Node
Network
Cloud
```

Build:

```text
Timeline
IOCs
IOAs
Root Cause
Impact
```

---

# Quick Revision

## Kubernetes Forensics

```text
Collection and analysis of Kubernetes-related digital evidence
```

---

## Volatile Evidence

```text
Evidence that can disappear quickly
```

---

## Non-Volatile Evidence

```text
Persistent evidence such as logs and storage
```

---

## Chain of Custody

```text
Record of evidence handling
```

---

## IOC

```text
Indicator of Compromise
```

---

## IOA

```text
Indicator of Attack
```

---

## Forensic Readiness

```text
Preparing systems to preserve useful evidence
```

---

## Image Digest

```text
Immutable identifier for image content
```

---

## Timeline

```text
Chronological reconstruction of events
```

---

## Root Cause

```text
Underlying reason the incident occurred
```

---

# Essential Commands

List Pods:

```bash
kubectl get pods -A
```

Detailed Pod:

```bash
kubectl describe pod <pod>
```

Pod YAML:

```bash
kubectl get pod <pod> -o yaml
```

Pod UID:

```bash
kubectl get pod <pod> \
  -o jsonpath='{.metadata.uid}'
```

Pod logs:

```bash
kubectl logs <pod>
```

Previous logs:

```bash
kubectl logs <pod> --previous
```

All events:

```bash
kubectl get events -A
```

Chronological events:

```bash
kubectl get events -A \
  --sort-by=.lastTimestamp
```

Pod placement:

```bash
kubectl get pods -A -o wide
```

Nodes:

```bash
kubectl get nodes -o wide
```

Services:

```bash
kubectl get svc -A
```

Ingress:

```bash
kubectl get ingress -A
```

Gateway:

```bash
kubectl get gateway -A
```

ServiceAccounts:

```bash
kubectl get serviceaccounts -A
```

Roles:

```bash
kubectl get roles -A
```

RoleBindings:

```bash
kubectl get rolebindings -A
```

ClusterRoles:

```bash
kubectl get clusterroles
```

ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

NetworkPolicies:

```bash
kubectl get networkpolicy -A
```

Deployments:

```bash
kubectl get deployments -A
```

DaemonSets:

```bash
kubectl get daemonsets -A
```

StatefulSets:

```bash
kubectl get statefulsets -A
```

Jobs:

```bash
kubectl get jobs -A
```

CronJobs:

```bash
kubectl get cronjobs -A
```

CRDs:

```bash
kubectl get crd
```

Container runtime:

```bash
crictl ps -a
```

Runtime images:

```bash
crictl images
```

Runtime inspection:

```bash
crictl inspect <container-id>
```

kubelet logs:

```bash
journalctl -u kubelet
```

Kernel logs:

```bash
journalctl -k
```

System logs:

```bash
journalctl
```

Processes:

```bash
ps aux
```

Network connections:

```bash
ss -antp
```

Evidence hashing:

```bash
sha256sum <file>
```

---

# Interview Questions

## Basic

- What is Kubernetes forensics?
- Why is Kubernetes forensics different from traditional server forensics?
- What is forensic readiness?
- What is volatile evidence?
- What is non-volatile evidence?
- What is chain of custody?
- What is an IOC?
- What is an IOA?
- What is a forensic timeline?
- Why are Kubernetes audit logs important?
- What is an image digest?
- What is `crictl`?

---

## Intermediate

- How would you investigate a compromised Pod?
- How would you collect Pod evidence?
- How would you investigate a compromised node?
- What Kubernetes artifacts are useful during an investigation?
- How do you investigate ServiceAccount abuse?
- How do you investigate RBAC changes?
- How do you investigate a malicious image?
- How do you investigate suspicious `kubectl exec` activity?
- How do you preserve evidence from ephemeral workloads?
- How do you investigate container runtime activity?
- How do you construct an incident timeline?
- How do you preserve evidence integrity?

---

## Advanced

- How would you perform forensic analysis of a Kubernetes cluster?
- How would you investigate a suspected container escape?
- How would you reconstruct an attack across Kubernetes and cloud infrastructure?
- How would you investigate a compromised ServiceAccount?
- How would you determine whether a node was compromised?
- How would you investigate supply-chain compromise?
- How would you preserve evidence without disrupting production?
- How would you design forensic readiness for a multi-cluster Kubernetes environment?
- How would you correlate Kubernetes audit logs with cloud and network logs?
- How would you perform forensic analysis when the malicious Pod has already been deleted?
- How would you investigate a compromised etcd environment?
- How would you build a Kubernetes forensic investigation platform?

---

# Interview Scenario 1

### Question

> A suspicious Pod was deleted before the security team started investigating. What evidence would you look for?

### Answer

I would investigate:

```text
Kubernetes Audit Logs
Pod Events
Deployment / ReplicaSet History
Container Logs
Centralized Logging
Runtime Logs
Node Logs
Image Registry Logs
Network Logs
DNS Logs
Cloud Logs
```

I would also identify the Pod's:

```text
UID
Node
Image
ServiceAccount
Namespace
```

and reconstruct the timeline from surviving evidence.

---

# Interview Scenario 2

### Question

> How would you investigate a suspected compromised node?

### Answer

I would:

```text
1. Isolate the node if required
2. Preserve volatile evidence when practical
3. Collect processes
4. Collect network connections
5. Collect filesystem evidence
6. Review kubelet logs
7. Review runtime logs
8. Review authentication logs
9. Review kernel logs
10. Correlate with Kubernetes audit logs
11. Determine root cause
12. Rebuild the node if compromise is confirmed
```

---

# Interview Scenario 3

### Question

> Why is the image digest important during forensics?

### Answer

Image tags can be mutable.

For example:

```text
app:latest
```

may point to different image contents over time.

The digest:

```text
sha256:<digest>
```

identifies a specific image content, making it much more reliable for investigation and evidence correlation.

---

# Interview Scenario 4

### Question

> What information can Kubernetes audit logs provide?

### Answer

Depending on audit policy and configured fields, they can help identify:

```text
Identity
Timestamp
Source IP
API Verb
Resource
Namespace
Object
Request / Response Metadata
```

This can establish who performed an action and when.

---

# Interview Scenario 5

### Question

> How would you investigate a compromised ServiceAccount?

### Answer

I would:

```text
Identify ServiceAccount
 ↓
Review RoleBindings
 ↓
Review ClusterRoleBindings
 ↓
Determine Permissions
 ↓
Review Audit Logs
 ↓
Identify Actions
 ↓
Rotate / Revoke Credentials
 ↓
Investigate Affected Resources
 ↓
Search for Persistence
```

---

# Interview Scenario 6

### Question

> What evidence would you collect from a compromised container?

### Answer

I would collect:

```text
Container Metadata
Image Digest
Process Information
Filesystem Evidence
Logs
Environment Metadata
Mounts
Security Context
Network Connections
ServiceAccount
Runtime Information
```

Collection should be performed using approved forensic procedures.

---

# Interview Scenario 7

### Question

> How do you determine whether an attacker moved laterally?

### Answer

Correlate:

```text
Identity
 ↓
API Activity
 ↓
Network Connections
 ↓
Service Access
 ↓
Credential Usage
 ↓
Other Workloads
```

Look for evidence showing movement from the initially compromised workload to additional resources.

---

# Interview Scenario 8

### Question

> How would you investigate a supply-chain compromise?

### Answer

Trace:

```text
Source Code
 ↓
Commit
 ↓
CI/CD Job
 ↓
Build Artifact
 ↓
Image
 ↓
Registry
 ↓
Deployment
 ↓
Runtime
```

Compare:

```text
Expected Artifact
vs
Deployed Artifact
```

using image digests, SBOMs, registry logs, and CI/CD records.

---

# Interview Scenario 9

### Question

> What is forensic readiness in Kubernetes?

### Answer

Forensic readiness means designing the cluster and surrounding infrastructure so that useful evidence is available during an incident.

Examples:

```text
Audit Logging
+
Centralized Logs
+
Runtime Monitoring
+
Network Visibility
+
Time Synchronization
+
Evidence Storage
+
Retention
```

---

# Interview Scenario 10

### Question

> Design a Kubernetes forensic architecture.

### Answer

A practical architecture is:

```text
                 Kubernetes
                      │
      ┌───────────────┼────────────────┐
      ▼               ▼                ▼
 Audit Logs        Runtime           Node
      │             Logs             Logs
      │               │                │
      └───────────────┼────────────────┘
                      ▼
                Central Logging
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      SIEM          Network        Cloud
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                 Investigation
                      │
             ┌────────┴────────┐
             ▼                 ▼
          Evidence          Timeline
             │                 │
             └────────┬────────┘
                      ▼
                 Root Cause
                      │
                      ▼
                  Reporting
```

The system should include:

```text
Evidence Integrity
+
Access Control
+
Retention
+
Privacy Protection
+
Incident Runbooks
```

---

# Production Forensics Checklist

```text
☑ Kubernetes audit logging enabled
☑ Centralized logging enabled
☑ Node logs retained
☑ Container runtime logs retained
☑ Network visibility available
☑ DNS visibility available
☑ Cloud audit logs enabled
☑ Time synchronization configured
☑ Evidence storage prepared
☑ Evidence access controlled
☑ Evidence hashing procedure documented
☑ Chain of custody procedure documented
☑ Image digests recorded
☑ Registry logs retained
☑ CI/CD logs retained
☑ SBOMs available
☑ Runtime telemetry available
☑ Incident runbooks documented
☑ Privacy requirements documented
☑ Retention policies defined
☑ Recovery procedures tested
```

---

# Chapter Summary

Kubernetes forensics focuses on reconstructing security incidents across dynamic and ephemeral infrastructure.

The core process is:

```text
Detect
 ↓
Preserve
 ↓
Collect
 ↓
Validate
 ↓
Analyze
 ↓
Correlate
 ↓
Reconstruct
 ↓
Report
```

Important evidence sources include:

```text
Kubernetes Audit Logs
Pod Logs
Events
Container Runtime
Node Logs
Network Logs
DNS Logs
Cloud Logs
Registry Logs
CI/CD Logs
```

Because Kubernetes workloads are ephemeral, forensic readiness must be designed before incidents occur.

The most important principle is:

> **Collect reliable evidence before it disappears, preserve its integrity, correlate evidence across Kubernetes, nodes, network, cloud, and supply-chain systems, and use the resulting timeline to determine the attack path and root cause.**

---

## Next Chapter

# Chapter 75 – Runtime Threat Detection

Topics will include:

- Runtime Threat Detection Fundamentals
- Runtime Security
- Runtime vs Image Security
- Runtime vs Vulnerability Scanning
- Runtime Attack Surface
- Process Monitoring
- File Monitoring
- Network Monitoring
- System Call Monitoring
- Container Monitoring
- Pod Monitoring
- Node Monitoring
- Kubernetes API Monitoring
- Behavioral Detection
- Anomaly Detection
- Rule-Based Detection
- Signature-Based Detection
- eBPF
- Linux Security Modules
- seccomp
- AppArmor
- SELinux
- Falco
- Tetragon
- Tracee
- Runtime Security Architecture
- Container Escape Detection
- Privilege Escalation Detection
- Suspicious Shell Detection
- Unexpected Process Detection
- Sensitive File Access
- Credential Access
- Secret Access
- Network Connection Detection
- DNS Detection
- Reverse Shell Detection
- Cryptocurrency Mining Detection
- Malware Detection
- Persistence Detection
- Kubernetes API Abuse
- kubectl exec Detection
- ServiceAccount Abuse
- RBAC Abuse
- Host Namespace Abuse
- Privileged Container Detection
- HostPath Detection
- Capability Abuse
- Namespace Monitoring
- Runtime Policies
- Detection Rules
- Alert Severity
- Alert Triage
- False Positives
- Detection Engineering
- Threat Intelligence
- MITRE ATT&CK
- Kubernetes Threat Matrix
- SIEM Integration
- SOAR Integration
- Incident Response Integration
- Runtime Telemetry
- eBPF-Based Security
- Production Runtime Security
- Performance Considerations
- Detection Coverage
- Security Monitoring
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---