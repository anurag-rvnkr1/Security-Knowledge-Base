# Chapter 73 – Incident Response

## Overview

Kubernetes Incident Response is the structured process of detecting, investigating, containing, eradicating, and recovering from security incidents affecting Kubernetes clusters, workloads, nodes, identities, applications, and supporting infrastructure.

A Kubernetes environment can be compromised at multiple layers:

```text
Application
    ↓
Container
    ↓
Pod
    ↓
Node
    ↓
Cluster
    ↓
Cloud / Infrastructure
```

A security incident may involve:

```text
Compromised Container
Compromised Pod
Compromised Node
Stolen Credentials
RBAC Abuse
Secret Exposure
Malicious Image
Container Escape
Cryptomining
Data Exfiltration
Lateral Movement
Supply Chain Compromise
```

A standard incident-response lifecycle is:

```text
Preparation
    ↓
Detection
    ↓
Triage
    ↓
Investigation
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Lessons Learned
```

The objective is:

```text
Detect Quickly
+
Contain Safely
+
Preserve Evidence
+
Remove Threat
+
Recover Reliably
+
Prevent Recurrence
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes incident response fundamentals
- Incident vs alert
- Security incident
- Incident lifecycle
- Preparation
- Detection
- Triage
- Containment
- Eradication
- Recovery
- Lessons learned
- Incident classification
- Severity levels
- Incident prioritization
- Kubernetes attack scenarios
- Compromised Pod
- Compromised container
- Compromised node
- Compromised ServiceAccount
- Credential theft
- Secret exposure
- Privilege escalation
- Container escape
- Cryptomining
- Malware
- Ransomware
- Data exfiltration
- Network intrusion
- API Server abuse
- kubelet abuse
- RBAC abuse
- Supply-chain compromise
- Malicious images
- Admission Controller abuse
- Persistence
- Lateral movement
- Discovery
- Collection
- Command and control
- Detection sources
- Kubernetes audit logs
- Container logs
- Node logs
- Cloud logs
- Network logs
- DNS logs
- Runtime security
- SIEM integration
- Alert triage
- Incident scoping
- Evidence preservation
- Forensic considerations
- Pod isolation
- Network isolation
- Node isolation
- Credential revocation
- Secret rotation
- Token revocation
- Image replacement
- Pod termination
- Node rebuild
- Cluster recovery
- Evidence collection
- Chain of custody
- Timeline creation
- IOC
- IOA
- Threat intelligence
- MITRE ATT&CK
- Kubernetes attack techniques
- Incident communication
- Escalation
- Incident documentation
- Recovery
- Post-incident review
- Root cause analysis
- Corrective actions
- Preventive controls
- Incident runbooks
- SOC integration
- SIEM integration
- SOAR automation
- Production incident response
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is Incident Response?

Incident Response is the organized process used to handle a security incident.

It includes:

```text
Detection
Investigation
Containment
Eradication
Recovery
```

---

# What Is a Security Incident?

A security incident is an event that may compromise:

```text
Confidentiality
Integrity
Availability
```

Examples:

```text
Stolen ServiceAccount Token
Unauthorized API Access
Malicious Container
Container Escape
Secret Exfiltration
Cryptominer
```

---

# Alert vs Incident

These are not the same.

## Alert

```text
Potentially Suspicious Event
```

## Incident

```text
Confirmed or Credible Security Impact
```

Example:

```text
Unexpected kubectl command
        ↓
Alert
        ↓
Investigation
        ↓
Confirmed Unauthorized Access
        ↓
Incident
```

---

# Incident Response Lifecycle

A common lifecycle:

```text
Preparation
     ↓
Detection
     ↓
Triage
     ↓
Investigation
     ↓
Containment
     ↓
Eradication
     ↓
Recovery
     ↓
Lessons Learned
```

---

# Phase 1 – Preparation

Preparation includes:

```text
Policies
Runbooks
Logging
Monitoring
Backups
Access Controls
Tools
Training
Communication
```

---

# Incident Response Preparation

Before an incident, establish:

```text
Who Responds?
Who Escalates?
Who Approves Isolation?
Who Communicates?
Who Handles Forensics?
Who Handles Recovery?
```

---

# Incident Response Team

Possible roles:

```text
SOC Analyst
Security Engineer
Kubernetes Administrator
Cloud Engineer
Incident Commander
Application Owner
Legal / Compliance
Management
```

---

# Incident Severity

Organizations can define severity levels.

Example:

```text
SEV-1 → Critical
SEV-2 → High
SEV-3 → Medium
SEV-4 → Low
```

---

# SEV-1 Example

Potential characteristics:

```text
Production Cluster Compromise
Data Exfiltration
Cluster-Wide Privilege Escalation
Active Ransomware
Critical Credential Compromise
```

---

# SEV-2 Example

```text
Compromised Application
Limited Credential Exposure
Single Namespace Compromise
Suspicious Privileged Container
```

Severity definitions should be organization-specific.

---

# Incident Preparation Checklist

```text
☑ Logging enabled
☑ Kubernetes audit logs available
☑ Runtime monitoring enabled
☑ Network visibility available
☑ SIEM integration configured
☑ Backups available
☑ Contact list maintained
☑ Runbooks documented
☑ Evidence storage prepared
☑ Access permissions tested
☑ Recovery procedures tested
```

---

# Phase 2 – Detection

Detection identifies potentially malicious activity.

Sources include:

```text
SIEM
EDR
Runtime Security
Kubernetes Audit Logs
Cloud Logs
Network Logs
DNS Logs
Application Logs
IDS / IPS
```

---

# Kubernetes Detection Sources

Important sources include:

```text
API Server Audit Logs
kubelet Logs
Container Logs
Runtime Events
Pod Events
Admission Logs
CNI Logs
Cloud Audit Logs
```

---

# Kubernetes Audit Logs

Audit logs record API activity.

They can help answer:

```text
Who?
What?
When?
From Where?
Which Resource?
Which Namespace?
```

---

# Example Suspicious Activity

```text
Unknown Identity
      ↓
kubectl exec
      ↓
Production Pod
      ↓
Sensitive Namespace
```

This may warrant investigation.

---

# Pod Events

Check:

```bash
kubectl get events -A
```

Events can reveal:

```text
Scheduling
Mounting
Image Pulling
Evictions
Container Failures
```

Events are useful but should not be treated as a complete forensic record.

---

# Container Logs

Check:

```bash
kubectl logs <pod>
```

Previous container:

```bash
kubectl logs <pod> --previous
```

Useful for:

```text
Application Errors
Suspicious Commands
Malware Indicators
Unexpected Connections
```

---

# Node Logs

On the node:

```bash
journalctl -u kubelet
```

Also review:

```text
Container Runtime Logs
System Logs
Authentication Logs
Kernel Logs
```

---

# Cloud Logs

Cloud environments may provide:

```text
IAM Logs
API Logs
Load Balancer Logs
VPC Flow Logs
Instance Logs
Firewall Logs
```

These can be critical when investigating cloud-hosted Kubernetes.

---

# Network Logs

Useful sources include:

```text
Flow Logs
Firewall Logs
CNI Logs
IDS
Service Mesh Telemetry
```

---

# DNS Logs

DNS activity can reveal:

```text
Unexpected External Domains
Command-and-Control Domains
Data Exfiltration
Malware Infrastructure
```

---

# Runtime Security

Runtime security can detect:

```text
Unexpected Process
Shell Execution
Privilege Escalation
Sensitive File Access
Suspicious Network Connection
```

---

# SIEM Integration

Security data can be centralized into a SIEM.

Conceptually:

```text
Kubernetes
Cloud
Nodes
Applications
Network
Runtime
   ↓
  SIEM
   ↓
Correlation
   ↓
Alert
```

---

# Phase 3 – Triage

Triage determines:

```text
Is This Real?
How Serious?
What Is Affected?
What Should Happen Next?
```

---

# Triage Questions

Ask:

```text
What happened?
When did it start?
Which cluster?
Which namespace?
Which Pod?
Which node?
Which identity?
Which credentials?
Is the attacker still active?
Is data affected?
```

---

# Incident Scoping

Determine the blast radius:

```text
Single Container
      ↓
Single Pod
      ↓
Namespace
      ↓
Node
      ↓
Cluster
      ↓
Cloud Account
```

---

# Example Scope

```text
Compromised Pod
      ↓
ServiceAccount Token
      ↓
API Access
      ↓
Other Namespace
```

The incident may therefore be larger than the original Pod.

---

# Indicators of Compromise

IOC means:

```text
Indicator of Compromise
```

Examples:

```text
Malicious IP
Domain
Hash
File
Process
Credential
Container Image
```

---

# Indicators of Attack

IOA means:

```text
Indicator of Attack
```

Examples:

```text
Unexpected kubectl exec
Privilege Escalation
Credential Dumping
Suspicious API Calls
```

IOAs focus more on suspicious behavior than static artifacts.

---

# Threat Intelligence

Threat intelligence can help determine:

```text
Known Malware
Known IP
Known Domain
Known CVE Exploitation
Known Attacker Behavior
```

---

# Phase 4 – Investigation

Investigation aims to reconstruct:

```text
What Happened?
How?
Who?
When?
What Was Accessed?
What Changed?
```

---

# Investigation Timeline

Create a timeline:

```text
10:00 → Initial Login
10:03 → Pod Created
10:05 → kubectl exec
10:08 → Secret Read
10:10 → External Connection
10:15 → New Pod Created
```

---

# Why Timeline Matters

A timeline helps identify:

```text
Initial Access
Execution
Persistence
Privilege Escalation
Discovery
Lateral Movement
Collection
Exfiltration
```

---

# Kubernetes Discovery

An attacker may attempt to discover:

```text
Pods
Services
Namespaces
Secrets
ConfigMaps
ServiceAccounts
Roles
Nodes
```

Suspicious API activity can be investigated through audit logs.

---

# ServiceAccount Compromise

A compromised ServiceAccount can be dangerous if it has excessive permissions.

Investigate:

```text
Token
Roles
RoleBindings
ClusterRoles
ClusterRoleBindings
```

---

# Check ServiceAccounts

```bash
kubectl get serviceaccounts -A
```

---

# Check RoleBindings

```bash
kubectl get rolebindings -A
```

---

# Check ClusterRoleBindings

```bash
kubectl get clusterrolebindings
```

---

# RBAC Investigation

Determine:

```text
Who has access?
What can they do?
Where can they do it?
```

---

# Privilege Escalation

Potential paths include:

```text
Low-Privilege Identity
      ↓
Misconfigured RBAC
      ↓
High-Privilege Permission
```

or:

```text
Container
 ↓
Host Access
 ↓
Node
```

---

# Secret Access Investigation

Determine:

```text
Which Secret?
Which Identity?
Which Pod?
Which Time?
Was It Exfiltrated?
```

---

# Secret Rotation

If a credential is compromised:

```text
Identify
 ↓
Revoke / Rotate
 ↓
Update Applications
 ↓
Validate
```

---

# Do Not Assume Deleting a Pod Revokes Credentials

Deleting a Pod does not necessarily revoke credentials that were already copied or exposed.

Rotate affected credentials.

---

# Container Compromise

Indicators may include:

```text
Unexpected Process
Unexpected Shell
Unexpected Package
Unexpected Network Connection
Unexpected File
```

---

# Compromised Pod

A suspicious Pod should be evaluated for:

```text
Image
Container
Command
Arguments
SecurityContext
ServiceAccount
Volumes
Network
Node
```

---

# Pod Investigation

```bash
kubectl describe pod <pod-name>
```

Inspect:

```text
Image
Command
Environment
Volumes
ServiceAccount
SecurityContext
Node
Events
```

---

# Image Investigation

Check:

```bash
kubectl get pod <pod-name> \
  -o jsonpath='{.spec.containers[*].image}'
```

Determine:

```text
Registry
Tag
Digest
Image Age
Image Provenance
Scan Results
```

---

# Malicious Image

Possible sources:

```text
Compromised Registry
Compromised Build Pipeline
Typosquatting
Malicious Dependency
Developer Credential Theft
```

---

# Supply Chain Incident

Example:

```text
Developer
 ↓
CI/CD
 ↓
Build System Compromise
 ↓
Malicious Image
 ↓
Registry
 ↓
Kubernetes
```

---

# Container Escape

A container escape occurs when an attacker breaks container isolation and gains access to the host environment.

Potential contributing factors include:

```text
Kernel Vulnerability
Privileged Container
Dangerous Capability
Host Mount
Runtime Vulnerability
```

---

# Container Escape Response

Treat suspected container escape as a potentially serious node-level incident.

Do not assume deleting the container is sufficient.

---

# Compromised Node

If a node may be compromised:

```text
Isolate
 ↓
Preserve Evidence
 ↓
Investigate
 ↓
Rebuild / Recover
```

---

# Node Isolation

A node may need:

```text
Network Isolation
Workload Isolation
Access Restriction
```

The exact method depends on the environment and incident-response plan.

---

# Why Not Immediately Destroy a Node?

Immediate destruction can eliminate:

```text
Memory Evidence
Filesystem Evidence
Process Evidence
Logs
Timeline Information
```

If forensic preservation is required, coordinate with the incident-response team before rebuilding.

---

# Evidence Preservation

Potential evidence:

```text
Container Logs
Node Logs
Audit Logs
Runtime Events
Process Information
Filesystem
Network Data
Cloud Logs
Images
Manifests
```

---

# Chain of Custody

Chain of custody documents:

```text
Who Collected Evidence
When
How
Where Stored
Who Accessed It
```

This is especially important when evidence may be used for legal or regulatory purposes.

---

# Evidence Integrity

Use appropriate integrity mechanisms such as:

```text
Hashes
Access Controls
Immutable Storage
Timestamps
```

---

# Phase 5 – Containment

Containment prevents further damage.

Possible actions:

```text
Isolate Pod
Isolate Node
Block Network
Revoke Credentials
Disable Account
Remove Exposure
Block Image
```

---

# Short-Term Containment

Example:

```text
Compromised Pod
      ↓
Network Isolation
      ↓
Stop Lateral Movement
```

---

# Long-Term Containment

May include:

```text
Patch
Reconfigure
Rotate Credentials
Replace Nodes
Update Policies
```

---

# Pod Isolation

NetworkPolicy may help isolate a workload.

Example:

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy

metadata:
  name: quarantine

spec:

  podSelector:
    matchLabels:
      incident: quarantine

  policyTypes:
    - Ingress
    - Egress
```

A real incident policy must be carefully designed because an overly restrictive policy can interfere with evidence collection or recovery.

---

# Labeling for Isolation

A response process may label a Pod:

```text
incident=quarantine
```

and apply a corresponding policy.

---

# Network Isolation

At broader levels, use:

```text
Firewall
Security Groups
Network ACL
CNI Policy
Service Mesh Policy
```

depending on the environment.

---

# Credential Revocation

Compromised credentials may include:

```text
ServiceAccount Token
Cloud Credential
Database Password
API Key
SSH Key
Registry Credential
```

Rotate or revoke them according to the incident plan.

---

# Image Blocking

If an image is confirmed malicious:

```text
Block Registry Access
Block Image Digest
Remove Deployment
Replace Image
```

Admission policies can prevent redeployment.

---

# Phase 6 – Eradication

Eradication removes the root cause.

Examples:

```text
Remove Malware
Patch Vulnerability
Remove Persistence
Rotate Credentials
Replace Image
Rebuild Node
Fix RBAC
Fix Network Policy
```

---

# Persistence

Attackers may attempt persistence through:

```text
Malicious Deployment
CronJob
DaemonSet
Backdoor Account
ServiceAccount
Secret
Admission Controller
CI/CD Pipeline
```

---

# Persistence Investigation

Review:

```bash
kubectl get deployments -A
kubectl get daemonsets -A
kubectl get statefulsets -A
kubectl get jobs -A
kubectl get cronjobs -A
```

Also review:

```text
RBAC
ServiceAccounts
Admission Configuration
Custom Resources
```

---

# Phase 7 – Recovery

Recovery returns the environment to a trusted operational state.

Possible actions:

```text
Redeploy Clean Images
Restore Data
Rebuild Nodes
Rotate Credentials
Restore Policies
Validate Workloads
Monitor Closely
```

---

# Recovery Principles

Do not simply:

```text
Restart Everything
```

Instead:

```text
Establish Trust
 ↓
Recover Clean Components
 ↓
Validate
 ↓
Restore Service
```

---

# Node Rebuild

For a confirmed node compromise, rebuilding the node from a known-good image can be safer than attempting to clean every artifact.

Typical approach:

```text
Drain / Isolate
 ↓
Preserve Evidence
 ↓
Remove Node
 ↓
Provision Clean Node
 ↓
Apply Hardened Configuration
 ↓
Join Cluster
 ↓
Validate
```

---

# Cluster Recovery

A major cluster compromise may require:

```text
Credential Rotation
Node Rebuild
Control Plane Validation
etcd Recovery
Image Replacement
RBAC Review
Network Review
Application Recovery
```

---

# etcd Recovery

If etcd integrity is compromised, follow the organization's tested etcd recovery procedure.

Do not experiment with production etcd during an active incident.

---

# Phase 8 – Lessons Learned

After recovery:

```text
What Happened?
Why?
What Failed?
What Worked?
What Should Change?
```

---

# Root Cause Analysis

RCA identifies the underlying cause.

Example:

```text
Incident
 ↓
Compromised Pod
 ↓
Privileged Container
 ↓
Insecure Deployment
 ↓
Missing Admission Policy
```

Root cause:

```text
Insufficient workload security controls
```

---

# Corrective Actions

Examples:

```text
Patch
RBAC Changes
Network Policies
Admission Policies
Image Signing
Runtime Detection
Logging
Training
```

---

# Preventive Controls

Prevent recurrence with:

```text
Least Privilege
+
Pod Security
+
Network Policies
+
Image Scanning
+
Admission Controls
+
Runtime Detection
```

---

# Common Kubernetes Incident Scenarios

## Scenario 1 – Cryptomining

```text
Vulnerable Application
 ↓
Container Compromise
 ↓
Cryptominer
 ↓
High CPU
```

Indicators:

```text
High CPU
Unexpected Process
Unexpected External Connection
```

---

# Cryptomining Response

```text
Detect
 ↓
Identify Pod
 ↓
Isolate
 ↓
Preserve Evidence
 ↓
Investigate Entry Point
 ↓
Remove Malicious Workload
 ↓
Patch Root Cause
 ↓
Monitor
```

---

# Scenario 2 – Secret Theft

```text
Compromised Identity
 ↓
Secret Access
 ↓
Credential Theft
 ↓
External Access
```

Response:

```text
Identify Secret
 ↓
Identify Access
 ↓
Rotate
 ↓
Investigate Usage
 ↓
Monitor
```

---

# Scenario 3 – Malicious Image

```text
Compromised Build
 ↓
Malicious Image
 ↓
Registry
 ↓
Kubernetes
```

Response:

```text
Block Image
 ↓
Stop Deployment
 ↓
Identify Affected Workloads
 ↓
Replace Image
 ↓
Investigate CI/CD
```

---

# Scenario 4 – Compromised ServiceAccount

```text
Token Theft
 ↓
API Access
 ↓
RBAC Abuse
```

Response:

```text
Identify Token
 ↓
Identify Permissions
 ↓
Revoke / Rotate
 ↓
Review Audit Logs
 ↓
Investigate Actions
```

---

# Scenario 5 – Container Escape

```text
Compromised Container
 ↓
Escape
 ↓
Host Access
```

Response:

```text
Treat Node as Potentially Compromised
 ↓
Isolate
 ↓
Preserve Evidence
 ↓
Investigate
 ↓
Rebuild
```

---

# Scenario 6 – Ransomware

Potential signs:

```text
Mass File Encryption
Unavailable Applications
Unexpected Processes
Storage Changes
```

Response requires coordinated:

```text
Containment
Credential Revocation
Evidence Preservation
Backup Protection
Recovery
```

---

# Scenario 7 – API Server Abuse

Indicators:

```text
Unexpected API Calls
Unusual Identity
Mass Resource Enumeration
Secret Access
Privilege Changes
```

Investigate audit logs.

---

# Scenario 8 – Lateral Movement

Example:

```text
Pod A
 ↓
Service Credential
 ↓
Pod B
 ↓
Database
```

Use:

```text
Network Policies
Least Privilege
Segmentation
Monitoring
```

---

# MITRE ATT&CK

MITRE ATT&CK provides a framework for describing adversary behavior.

Relevant concepts can include:

```text
Initial Access
Execution
Persistence
Privilege Escalation
Defense Evasion
Credential Access
Discovery
Lateral Movement
Collection
Command and Control
Exfiltration
Impact
```

---

# Kubernetes Attack Chain

A simplified attack chain:

```text
Initial Access
      ↓
Execution
      ↓
Discovery
      ↓
Credential Access
      ↓
Privilege Escalation
      ↓
Lateral Movement
      ↓
Collection
      ↓
Exfiltration
```

Incident responders should determine where the attacker entered and how far they progressed.

---

# Incident Communication

Communication should be:

```text
Accurate
Timely
Controlled
Documented
```

---

# Incident Commander

The Incident Commander coordinates:

```text
Investigation
Containment
Communication
Decision Making
Recovery
```

---

# Escalation

Escalate when:

```text
Scope Expands
Critical Data Is Affected
Production Is Down
Credentials Are Compromised
Cloud Account Is Affected
Legal / Compliance Impact Exists
```

---

# Incident Documentation

Document:

```text
Timeline
Evidence
Actions
Decisions
Findings
Affected Assets
Recovery
Root Cause
```

---

# Incident Ticket

A useful incident record contains:

```text
Incident ID
Severity
Start Time
Detection Time
Affected Cluster
Affected Namespace
Affected Workloads
Indicators
Actions
Current Status
Owner
```

---

# Evidence Collection

Collect only what is necessary and authorized.

Examples:

```text
kubectl describe
kubectl get -o yaml
kubectl logs
Audit Logs
Node Logs
Runtime Logs
Cloud Logs
Network Logs
```

---

# Kubernetes Evidence

Useful commands:

```bash
kubectl get pod <pod> -o yaml
```

```bash
kubectl describe pod <pod>
```

```bash
kubectl logs <pod>
```

```bash
kubectl logs <pod> --previous
```

```bash
kubectl get events -A
```

---

# Resource Inventory During Incident

Collect:

```bash
kubectl get pods -A -o wide
```

```bash
kubectl get nodes -o wide
```

```bash
kubectl get svc -A
```

```bash
kubectl get ingress -A
```

```bash
kubectl get serviceaccounts -A
```

```bash
kubectl get roles -A
```

```bash
kubectl get rolebindings -A
```

```bash
kubectl get clusterrolebindings
```

---

# Preserve Before Destroy

Important principle:

```text
Evidence
 ↓
Preserve
 ↓
Contain
 ↓
Destroy / Rebuild
```

Do not automatically delete suspicious workloads before determining whether evidence needs to be preserved.

---

# However: Safety Comes First

If a workload is actively causing severe damage:

```text
Containment
```

may take priority.

The response team should balance:

```text
Evidence Preservation
+
Business Protection
+
Threat Containment
```

---

# SOAR Integration

SOAR can automate repetitive response actions.

Example:

```text
SIEM Alert
 ↓
SOAR
 ↓
Validate
 ↓
Quarantine Pod
 ↓
Disable Credential
 ↓
Create Incident
 ↓
Notify Team
```

Automation should include safeguards and approval for high-impact actions.

---

# SOC Integration

Kubernetes security events can flow into a SOC:

```text
Kubernetes
   ↓
Logs / Events
   ↓
SIEM
   ↓
Detection
   ↓
SOC Analyst
   ↓
Incident Response
```

---

# Incident Response Automation

Potential automated actions:

```text
Create Ticket
Block IP
Quarantine Pod
Disable Credential
Notify Analyst
Collect Logs
```

High-risk actions should be carefully controlled.

---

# Production Incident Runbook

Example:

```text
1. Detect
2. Validate Alert
3. Assign Severity
4. Identify Scope
5. Preserve Evidence
6. Contain
7. Investigate
8. Eradicate
9. Recover
10. Validate
11. Monitor
12. Document
13. Conduct RCA
```

---

# Incident Response Decision Tree

```text
Suspicious Event
      ↓
Is It Real?
 ┌────┴────┐
No         Yes
 ↓          ↓
Close     Scope
            ↓
       Active Threat?
        ┌───┴───┐
       No      Yes
       ↓        ↓
   Investigate Contain
       ↓        ↓
       └───┬────┘
           ↓
       Eradicate
           ↓
        Recover
           ↓
     Lessons Learned
```

---

# Common Mistakes

## 1. Immediately Deleting Evidence

This can destroy valuable forensic information.

---

## 2. Ignoring Scope

A compromised Pod may indicate:

```text
Node Compromise
Credential Compromise
Cluster Compromise
```

---

## 3. Rotating One Credential Only

Investigate related credentials and access paths.

---

## 4. Restarting the Entire Cluster

This may destroy evidence and increase downtime.

---

## 5. Ignoring Cloud Credentials

Kubernetes compromise can lead to cloud compromise.

---

## 6. Ignoring ServiceAccounts

ServiceAccounts may have significant permissions.

---

## 7. Ignoring RBAC

Investigate:

```text
Role
RoleBinding
ClusterRole
ClusterRoleBinding
```

---

## 8. Focusing Only on the Malware

Find the initial access vector.

---

## 9. No Timeline

Without a timeline, determining attacker progression becomes difficult.

---

## 10. No Root Cause Analysis

Removing malware without fixing the entry point allows reinfection.

---

## 11. No Credential Rotation

Deleting a compromised Pod does not invalidate stolen credentials.

---

## 12. No Post-Incident Monitoring

Attackers may attempt to return.

---

# Best Practices

### 1. Prepare Before an Incident

Maintain:

```text
Runbooks
Logs
Backups
Contacts
Tools
```

---

### 2. Centralize Security Logs

Use:

```text
SIEM
Central Logging
Cloud Logging
```

---

### 3. Preserve Evidence

Especially for serious incidents.

---

### 4. Contain Quickly

Stop:

```text
Lateral Movement
Exfiltration
Further Compromise
```

---

### 5. Rotate Compromised Credentials

Do not rely only on Pod deletion.

---

### 6. Rebuild Compromised Nodes

For confirmed host compromise, rebuilding from trusted sources is often safer than attempting to clean every artifact.

---

### 7. Use Least Privilege

Reduce attacker capabilities.

---

### 8. Segment Networks

Use:

```text
NetworkPolicies
Firewall
Security Groups
```

---

### 9. Secure the Supply Chain

Use:

```text
Trusted Registry
SBOM
Image Scanning
Signing
Admission
```

---

### 10. Perform RCA

Fix the underlying cause.

---

# Hands-on Lab 1 – Incident Detection

Create a test workload that generates a known suspicious event.

Detect it using:

```text
Logs
Events
Monitoring
```

---

# Hands-on Lab 2 – Pod Investigation

Deploy a test Pod.

Investigate:

```bash
kubectl describe pod <pod>
```

and:

```bash
kubectl get pod <pod> -o yaml
```

Identify:

```text
Image
ServiceAccount
SecurityContext
Volumes
Node
```

---

# Hands-on Lab 3 – Log Investigation

Generate test application events.

Use:

```bash
kubectl logs <pod>
```

and:

```bash
kubectl logs <pod> --previous
```

Create a timeline.

---

# Hands-on Lab 4 – RBAC Investigation

Create a test ServiceAccount and Role.

Investigate:

```bash
kubectl get role -A
kubectl get rolebinding -A
```

Determine:

```text
Who
Can Do What
Where
```

---

# Hands-on Lab 5 – Suspicious ServiceAccount

Create a controlled test scenario involving unexpected API activity.

Review Kubernetes audit logs.

Determine:

```text
Identity
Time
API Resource
Verb
Namespace
```

---

# Hands-on Lab 6 – Network Isolation

Create a test NetworkPolicy that isolates a labeled workload.

Example:

```text
incident=quarantine
```

Validate:

```text
Ingress
Egress
```

---

# Hands-on Lab 7 – Credential Rotation

Create a disposable test credential.

Simulate compromise.

Practice:

```text
Identify
 ↓
Rotate
 ↓
Update Workload
 ↓
Validate
```

---

# Hands-on Lab 8 – Malicious Image Simulation

Create a harmless test image that produces an obvious indicator.

Deploy it.

Practice:

```text
Detect
 ↓
Identify
 ↓
Quarantine
 ↓
Remove
 ↓
Replace
```

---

# Hands-on Lab 9 – Cryptomining Simulation

In a disposable environment, run a harmless CPU-intensive process.

Observe:

```text
CPU
Process
Pod
Node
```

Create a detection rule.

---

# Hands-on Lab 10 – Incident Timeline

Create a simulated incident with multiple events.

Build:

```text
Initial Access
 ↓
Execution
 ↓
Discovery
 ↓
Credential Access
 ↓
Lateral Movement
```

Document timestamps.

---

# Hands-on Lab 11 – Evidence Collection

Collect:

```text
Pod YAML
Pod Description
Container Logs
Events
Node Information
RBAC
ServiceAccounts
```

Store evidence with appropriate integrity controls.

---

# Hands-on Lab 12 – Compromised Node Exercise

Use a disposable node.

Simulate suspicious behavior.

Practice:

```text
Detect
 ↓
Isolate
 ↓
Preserve
 ↓
Rebuild
 ↓
Validate
```

---

# Hands-on Lab 13 – SIEM Integration

Send test Kubernetes logs into a SIEM.

Create detection rules for:

```text
Unexpected Pod Creation
Unexpected Exec
Privilege Changes
Secret Access
```

---

# Hands-on Lab 14 – SOAR Automation

Create a safe test workflow:

```text
Alert
 ↓
Ticket
 ↓
Notification
 ↓
Analyst Approval
 ↓
Quarantine
```

---

# Hands-on Lab 15 – Full Incident Exercise

Simulate:

```text
Compromised Application
 ↓
Pod Access
 ↓
ServiceAccount Abuse
 ↓
Secret Access
 ↓
External Connection
```

Respond using:

```text
Detection
Triage
Investigation
Containment
Eradication
Recovery
RCA
```

---

# Quick Revision

## Incident

```text
Security event with confirmed or credible impact
```

---

## Triage

```text
Determine validity, severity, and scope
```

---

## Containment

```text
Prevent further damage
```

---

## Eradication

```text
Remove attacker presence and root cause
```

---

## Recovery

```text
Return systems to trusted operation
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

## SIEM

```text
Centralized security monitoring and correlation platform
```

---

## SOAR

```text
Security orchestration and automated response
```

---

## Root Cause Analysis

```text
Determine why the incident occurred
```

---

## Chain of Custody

```text
Documentation of evidence handling
```

---

# Essential Commands

List all Pods:

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

Pod logs:

```bash
kubectl logs <pod>
```

Previous container logs:

```bash
kubectl logs <pod> --previous
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

Events:

```bash
kubectl get events -A
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

Node details:

```bash
kubectl describe node <node>
```

kubelet logs:

```bash
journalctl -u kubelet
```

---

# Interview Questions

## Basic

- What is incident response?
- What is a security incident?
- What is the difference between an alert and an incident?
- What are the phases of incident response?
- What is triage?
- What is containment?
- What is eradication?
- What is recovery?
- What is an IOC?
- What is an IOA?
- What is a SIEM?
- What is SOAR?
- What is root cause analysis?
- What is chain of custody?

---

## Intermediate

- How do you investigate a compromised Pod?
- What logs are important during a Kubernetes incident?
- How do Kubernetes audit logs help incident response?
- How do you investigate ServiceAccount abuse?
- How do you investigate RBAC abuse?
- How do you isolate a compromised Pod?
- How do you isolate a compromised node?
- When should you rebuild a node?
- How do you rotate compromised credentials?
- How do you investigate a malicious container image?
- How do you investigate suspicious API activity?
- What is the difference between containment and eradication?
- Why should evidence be preserved before rebuilding a node?

---

## Advanced

- How would you respond to a suspected Kubernetes cluster compromise?
- How would you investigate a container escape?
- How would you investigate a compromised ServiceAccount?
- How would you determine the blast radius of an incident?
- How would you build a Kubernetes incident-response runbook?
- How would you integrate Kubernetes with a SOC?
- How would you detect lateral movement?
- How would you respond to a cryptomining attack?
- How would you respond to ransomware affecting Kubernetes storage?
- How would you handle a malicious image in a production registry?
- How would you respond to a Kubernetes zero-day?
- How would you preserve forensic evidence from a compromised node?
- How would you combine SIEM, runtime security, and Kubernetes audit logs?

---

# Interview Scenario 1

### Question

> A Pod suddenly starts consuming 100% CPU. How would you investigate?

### Answer

First determine whether the behavior is expected.

```text
Check Metrics
 ↓
Identify Pod
 ↓
Inspect Logs
 ↓
Inspect Processes / Runtime Signals
 ↓
Check Image
 ↓
Check Recent Changes
 ↓
Check Network Connections
 ↓
Check ServiceAccount
 ↓
Determine Security Impact
```

If malicious activity is suspected:

```text
Preserve Evidence
 ↓
Contain
 ↓
Investigate
```

---

# Interview Scenario 2

### Question

> You discover that a ServiceAccount token may have been stolen. What do you do?

### Answer

```text
1. Identify the ServiceAccount
2. Determine its permissions
3. Review audit logs
4. Identify suspicious activity
5. Rotate/revoke affected credentials
6. Investigate related secrets
7. Check for persistence
8. Monitor for additional activity
```

---

# Interview Scenario 3

### Question

> A container escape is suspected. What is your response?

### Answer

Treat the node as potentially compromised.

```text
Detect
 ↓
Preserve Evidence
 ↓
Isolate Node
 ↓
Investigate
 ↓
Identify Root Cause
 ↓
Rebuild Node
 ↓
Rotate Credentials
 ↓
Validate Cluster
 ↓
Monitor
```

---

# Interview Scenario 4

### Question

> Why shouldn't you immediately delete a compromised Pod?

### Answer

Deleting it may destroy:

```text
Process Evidence
Filesystem Evidence
Logs
Network Context
Runtime State
```

If immediate containment is not urgent, preserve evidence first.

If the workload is actively causing severe damage, containment may take priority.

---

# Interview Scenario 5

### Question

> How do you investigate an attacker who used kubectl?

### Answer

Review Kubernetes audit logs for:

```text
Identity
Source IP
Timestamp
Verb
Resource
Namespace
Object
Response
```

Then correlate with:

```text
Cloud Logs
Node Logs
Application Logs
Network Logs
```

---

# Interview Scenario 6

### Question

> How would you investigate a malicious image?

### Answer

Determine:

```text
Image
 ↓
Digest
 ↓
Registry
 ↓
Build Pipeline
 ↓
SBOM
 ↓
Scan Results
 ↓
Deployment History
```

Then:

```text
Block
 ↓
Replace
 ↓
Investigate Supply Chain
```

---

# Interview Scenario 7

### Question

> How would you contain a compromised Pod?

### Answer

Depending on the situation:

```text
Network Isolation
+
Credential Revocation
+
Workload Isolation
```

Preserve evidence when practical.

Then remove the malicious workload after investigation requirements are satisfied.

---

# Interview Scenario 8

### Question

> What is the difference between containment and eradication?

### Answer

Containment:

```text
Stop Further Damage
```

Eradication:

```text
Remove Threat and Root Cause
```

Example:

```text
Containment:
Isolate Pod

Eradication:
Remove Malware + Patch Vulnerability
```

---

# Interview Scenario 9

### Question

> How would you determine the blast radius?

### Answer

Trace:

```text
Compromised Identity
 ↓
Permissions
 ↓
Resources Accessed
 ↓
Namespaces
 ↓
Nodes
 ↓
Secrets
 ↓
External Systems
```

Correlate Kubernetes audit, network, cloud, and application logs.

---

# Interview Scenario 10

### Question

> Design a production Kubernetes incident-response architecture.

### Answer

```text
                Kubernetes
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   Audit Logs   Runtime      Network
                   │           │
        └──────────┼───────────┘
                   ▼
                  SIEM
                   │
                   ▼
               Detection
                   │
                   ▼
               SOC Analyst
                   │
                   ▼
             Incident Response
                   │
       ┌───────────┼───────────┐
       ▼           ▼           ▼
   Containment  Eradication  Recovery
       │           │           │
       └───────────┼───────────┘
                   ▼
              RCA / Lessons
```

The architecture should include:

```text
Central Logging
+
Audit Logging
+
Runtime Security
+
Network Visibility
+
Identity Monitoring
+
Backups
+
Incident Runbooks
+
Credential Rotation
+
Recovery Procedures
```

---

# Production Incident Response Checklist

```text
☑ Incident response plan documented
☑ Roles assigned
☑ Escalation process defined
☑ Contact information maintained
☑ Kubernetes audit logging enabled
☑ Central logging enabled
☑ Runtime monitoring enabled
☑ Network visibility enabled
☑ SIEM integration configured
☑ Backups tested
☑ Evidence storage prepared
☑ Incident severity model defined
☑ Triage process defined
☑ Containment procedures defined
☑ Credential rotation procedure defined
☑ Node isolation procedure defined
☑ Node rebuild procedure defined
☑ Cluster recovery procedure defined
☑ Communication procedure defined
☑ RCA process defined
☑ Lessons-learned process defined
```

---

# Chapter Summary

Kubernetes incident response is a structured process for handling security incidents across:

```text
Applications
Containers
Pods
Nodes
Control Plane
Identities
Cloud Infrastructure
Supply Chain
```

The core lifecycle is:

```text
Preparation
 ↓
Detection
 ↓
Triage
 ↓
Investigation
 ↓
Containment
 ↓
Eradication
 ↓
Recovery
 ↓
Lessons Learned
```

The most important principles are:

```text
Know Your Environment
+
Collect Good Telemetry
+
Preserve Evidence
+
Contain Quickly
+
Rotate Compromised Credentials
+
Remove Root Cause
+
Recover From Trusted Sources
+
Monitor After Recovery
```

A compromised Pod does not necessarily mean the entire cluster is compromised, but responders must determine the actual blast radius rather than assuming the incident is isolated.

The most important operational principle is:

> **Contain the threat without unnecessarily destroying evidence, determine the full blast radius, eradicate the root cause, recover from trusted components, and continuously improve the controls that failed.**

---

## Next Chapter

# Chapter 74 – Kubernetes Forensics

Topics will include:

- Kubernetes Forensics Fundamentals
- Digital Forensics
- Kubernetes Forensic Challenges
- Evidence Sources
- Evidence Preservation
- Chain of Custody
- Volatile Evidence
- Non-Volatile Evidence
- Pod Forensics
- Container Forensics
- Node Forensics
- Control Plane Forensics
- API Server Forensics
- etcd Forensics
- kubelet Forensics
- Container Runtime Forensics
- Kubernetes Audit Logs
- Application Logs
- System Logs
- Network Logs
- DNS Logs
- Cloud Logs
- Runtime Security Data
- Process Analysis
- File System Analysis
- Memory Forensics
- Network Forensics
- Container Image Forensics
- Image Digests
- SBOM
- Malware Analysis
- Timeline Analysis
- IOC Collection
- IOA Collection
- Attack Reconstruction
- Initial Access
- Execution
- Persistence
- Privilege Escalation
- Credential Access
- Discovery
- Lateral Movement
- Collection
- Exfiltration
- Impact
- Kubernetes Artifacts
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
- Container Runtime Artifacts
- containerd
- CRI-O
- Node Evidence
- kubelet Evidence
- Linux Logs
- systemd
- Journald
- Kernel Logs
- Authentication Logs
- Cloud Forensics
- Forensic Readiness
- Evidence Collection Procedures
- Evidence Integrity
- Hashing
- Secure Evidence Storage
- Timeline Construction
- Hypothesis Testing
- Root Cause Analysis
- Forensic Tools
- kubectl
- crictl
- journalctl
- Linux Tools
- Runtime Tools
- SIEM
- Incident Response Integration
- Legal Considerations
- Compliance
- Privacy
- Production Forensics
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---