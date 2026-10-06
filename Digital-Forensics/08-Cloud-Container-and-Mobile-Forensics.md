# Cloud, Container, and Mobile Forensics

> **A practical enterprise guide to investigating modern distributed environments through cloud audit logs, identity telemetry, virtual machines, object storage, containers, Kubernetes, workload metadata, mobile artifacts, and cross-platform evidence correlation.**

---

# Overview

Traditional digital forensics often assumes that evidence exists on a physical endpoint or local disk.

Modern environments are different.

Enterprise workloads increasingly span:

```text
Cloud
 │
 ├── Virtual Machines
 ├── Object Storage
 ├── Databases
 ├── Serverless
 ├── Identity Platforms
 ├── APIs
 └── Managed Services

Containers
 │
 ├── Docker
 ├── Kubernetes
 ├── Pods
 ├── Images
 └── Runtime

Mobile
 │
 ├── Android
 ├── iOS
 ├── Applications
 ├── Cloud Synchronization
 └── Device Telemetry
```

Evidence is therefore:

> **Distributed across identities, APIs, workloads, platforms, devices, and cloud services.**

---

# Why Modern Platform Forensics Matters

An incident may begin on one platform and move across several others.

Example:

```text id="x2q1mt"
Compromised User
      │
      ▼
Cloud Login
      │
      ▼
API Access
      │
      ▼
Cloud VM
      │
      ▼
Container
      │
      ▼
Database
      │
      ▼
Data Access
```

A host-only investigation would miss significant portions of the attack.

---

# Modern Forensic Architecture

```text id="q1d8cm"
                         Investigation
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
        Cloud             Containers            Mobile
          │                   │                   │
    ┌─────┼─────┐        ┌────┼────┐        ┌────┼────┐
    ▼     ▼     ▼        ▼    ▼    ▼        ▼    ▼    ▼
 Identity VM  Storage   Image Pod Node    Apps  OS  Cloud
    │     │     │        │    │    │        │    │    │
    └─────┼─────┘        └────┼────┘        └────┼────┘
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                         Correlation
                              │
                              ▼
                           Timeline
```

---

# Core Challenges

Modern platform forensics introduces challenges such as:

- Evidence distributed across providers
- Short-lived workloads
- Ephemeral containers
- Managed services
- Encryption
- Multi-tenant infrastructure
- Provider-specific logging
- API-based activity
- Identity-centric attacks
- Data residency
- Privacy requirements
- Limited physical access

---

# Shared Responsibility Model

Cloud security is commonly divided between:

```text id="3b1s4m"
Cloud Provider
      │
      ├── Physical Infrastructure
      ├── Core Platform
      └── Managed Service Components

Customer
      │
      ├── Identity
      ├── Data
      ├── Configuration
      ├── Workloads
      └── Access Policies
```

The exact responsibilities vary by service model.

---

# Cloud Forensic Principles

A cloud investigation should establish:

```text id="5c7k4w"
Who
What
When
Where
How
Which Resource
Which Identity
Which API
Which Data
```

The identity is often as important as the IP address.

---

# Cloud Evidence Categories

| Evidence | Examples |
|---|---|
| Identity | Users, roles, tokens |
| API | Administrative actions |
| Network | Flow logs, firewall |
| Compute | VM activity |
| Storage | Object access |
| Database | Queries and access |
| Application | Service logs |
| Configuration | Resource changes |
| Security | Alerts and findings |
| Orchestration | Kubernetes events |

---

# Cloud Identity Forensics

Identity is central to cloud investigations.

Investigate:

```text id="atf1v0"
User
Role
Service Account
Application Identity
Authentication
MFA
Token
Source IP
Device
API Activity
```

---

# Identity Investigation Model

```text id="2c0q8j"
Identity
   │
   ▼
Authentication
   │
   ▼
Token / Session
   │
   ▼
API Call
   │
   ▼
Resource
   │
   ▼
Data
```

---

# Cloud Authentication

Investigate:

- Login time
- Source IP
- Authentication method
- MFA
- Device
- Location metadata
- Session
- Failed attempts

An unusual login does not automatically prove compromise.

---

# API Forensics

Cloud environments are heavily API-driven.

Examples of actions include:

```text id="8r7k9y"
Create Resource
Modify Resource
Delete Resource
Change Policy
Read Data
Generate Credential
Change Network
Create User
Assume Role
```

API logs can therefore provide highly valuable forensic evidence.

---

# Cloud Audit Logs

Major providers offer activity/audit logging.

Examples:

```text id="3n8k5j"
AWS
 └── CloudTrail

Azure
 └── Activity Log / Entra audit logs

Google Cloud
 └── Cloud Audit Logs
```

Exact services and retention depend on configuration.

---

# AWS CloudTrail

CloudTrail can provide evidence about AWS API activity.

Useful investigation fields include:

```text id="5j2w0d"
Identity
Event
Timestamp
Source IP
Region
Resource
User Agent
Request Metadata
```

---

# Azure Forensics

Relevant evidence can include:

```text id="k3m7s8"
Entra ID
Activity Logs
Sign-in Logs
Audit Logs
Resource Logs
Defender Alerts
Network Logs
```

---

# Google Cloud Forensics

Relevant evidence can include:

```text id="x6r1c4"
Cloud Audit Logs
IAM
VPC Flow Logs
Cloud Logging
Security Command Center
Compute Logs
Storage Logs
```

---

# Cloud Storage Forensics

Cloud object storage may contain:

- Sensitive data
- Backups
- Logs
- Application files
- Staged data

Investigate:

```text id="4m8q6r"
Object
Identity
Action
Timestamp
Source
Version
Access Method
```

---

# Object Storage Access

Examples of investigative questions:

```text id="7v0f3x"
Who accessed the object?
Was access authorized?
Which identity performed it?
From where?
Was the object downloaded?
Was it modified?
Was it deleted?
```

---

# Cloud Data Exfiltration

Potential evidence:

```text id="9y4j1w"
Object Access
+
API Activity
+
Network Flow
+
Identity
+
Destination
```

Example:

```text id="b1q3s6"
Compromised Identity
      │
      ▼
Object Read
      │
      ▼
Data Staging
      │
      ▼
External Transfer
```

---

# Cloud VM Forensics

Cloud VMs can provide:

```text id="h7f2d5"
Disk
Memory
Processes
Network
Logs
Identity
Cloud Metadata
Snapshots
```

The investigation should correlate guest-level and cloud-level evidence.

---

# Cloud VM Evidence Model

```text id="z3r5n8"
Cloud Control Plane
        │
        ▼
     VM Resource
        │
 ┌──────┼──────┐
 ▼      ▼      ▼
Disk  Memory  Network
 │      │       │
 └──────┼───────┘
        ▼
    Correlation
```

---

# Cloud Snapshots

Snapshots can preserve a point-in-time representation of storage.

Investigate:

```text id="5x1p7d"
Who created it?
When?
Why?
Who accessed it?
Was it copied?
Was it shared?
```

Unexpected snapshots may deserve investigation.

---

# Cloud Configuration Forensics

Configuration changes may be as important as file changes.

Examples:

```text id="u8k4v1"
Firewall Rule
IAM Policy
Security Group
Storage Permission
Access Key
Network Route
Logging Configuration
```

---

# Logging Tampering

Attackers may attempt to reduce visibility by modifying:

- Logging
- Retention
- Access policies
- Security controls

Therefore investigate:

```text id="d2c7q0"
Security Configuration Changes
+
Audit Logs
+
Identity Activity
```

---

# Cloud Evidence Retention

Organizations should define retention for:

```text id="4x8m2c"
Identity Logs
API Logs
Network Logs
Storage Logs
Security Alerts
Configuration History
```

Short retention can create major forensic gaps.

---

# Cloud Evidence Gaps

Examples:

```text id="g0w5y8"
Audit Logging Disabled
Short Retention
Missing Region
Missing Account
Missing Identity Context
Encrypted Payload
Deleted Resource
Provider Limitation
```

Document gaps explicitly.

---

# Container Forensics

Containers are designed to be:

- Portable
- Ephemeral
- Lightweight
- Automated

This creates forensic challenges.

A container may disappear before investigators collect evidence.

---

# Container Evidence Model

```text id="c9h4w6"
Container
   │
   ├── Image
   ├── Filesystem
   ├── Processes
   ├── Network
   ├── Environment
   └── Logs
        │
        ▼
      Host
        │
        ├── Runtime
        ├── Kernel
        └── Storage
```

---

# Docker Evidence

Relevant artifacts may include:

```text id="6v2n7x"
Images
Containers
Container Metadata
Logs
Volumes
Networks
Runtime Configuration
Host Logs
```

---

# Docker Container Metadata

Investigate:

```text id="j7q5w0"
Image
Container ID
Creation Time
Start Time
Command
Environment
Volumes
Network
User
```

---

# Container Images

Images can contain:

```text id="x4m9v3"
Application Code
Libraries
Configuration
Secrets
OS Packages
Scripts
```

Investigate image provenance.

Questions:

```text id="m8c3q2"
Where did the image come from?
Who built it?
When?
Was it modified?
Which registry?
Which digest?
```

---

# Image Digests

Container images can be identified using cryptographic digests.

Conceptually:

```text id="7w2d9p"
Image
  │
  ▼
Digest
  │
  ▼
Exact Image Identity
```

This is useful for forensic correlation.

---

# Container Logs

Container logs may contain:

```text id="1x5q8s"
Application Events
Errors
Requests
Authentication
Network Activity
Execution
```

Retention depends on runtime and logging architecture.

---

# Container Volumes

Persistent volumes may contain:

- Application data
- Database files
- Configuration
- Secrets
- User-generated content

Investigate volume ownership and lifecycle.

---

# Container Network Forensics

Investigate:

```text id="6c4h9z"
Container IP
Pod IP
Node IP
Destination
Port
Service
Identity
```

Container networking can make attribution more complicated than traditional hosts.

---

# Kubernetes Forensics

Kubernetes adds another layer.

Evidence may include:

```text id="b8n3r7"
Cluster
Node
Namespace
Pod
Container
Service
Ingress
ConfigMap
Secret
API Request
Audit Event
```

---

# Kubernetes Investigation Model

```text id="w0y6j1"
Cluster
  │
  ├── Node
  │    │
  │    └── Pod
  │          │
  │          └── Container
  │
  └── API Server
         │
         ▼
       Identity
         │
         ▼
       Action
```

---

# Kubernetes API Audit

API audit evidence can help identify:

- Who performed an action
- What resource was targeted
- What operation occurred
- When it occurred

Examples:

```text id="z4s2m6"
Create Pod
Modify Deployment
Read Secret
Change Role
Create Service
```

---

# Kubernetes Secrets

Secrets require careful investigation.

Determine:

```text id="n7k1p4"
Who accessed it?
When?
Which workload?
Which identity?
Was it exposed?
```

Do not unnecessarily reproduce sensitive secret values in reports.

---

# Kubernetes Persistence

Potential mechanisms include:

```text id="2v9c6x"
Unexpected Pod
Modified Deployment
CronJob
ServiceAccount
RBAC Change
Container Image
Admission Configuration
```

Investigate against known-good configuration.

---

# Ephemeral Workloads

A major forensic challenge:

```text id="e0m8h5"
Alert
  │
  ▼
Pod Running
  │
  ▼
Pod Deleted
  │
  ▼
Evidence Missing
```

Organizations should therefore implement:

- Centralized logs
- Audit logging
- Runtime telemetry
- Image retention
- Node-level monitoring

---

# Kubernetes Node Forensics

The node may contain evidence from workloads.

Investigate:

```text id="r4k6z2"
Runtime
Processes
Network
Filesystem
Logs
Kernel
```

This should be done using approved procedures.

---

# Container Forensic Workflow

```text id="3u8w1k"
Alert
 │
 ▼
Identify Cluster
 │
 ▼
Identify Namespace
 │
 ▼
Identify Pod
 │
 ▼
Identify Container
 │
 ▼
Preserve Logs
 │
 ▼
Preserve Metadata
 │
 ▼
Identify Image
 │
 ▼
Review Network
 │
 ▼
Review Identity
 │
 ▼
Review Node
 │
 ▼
Build Timeline
```

---

# Mobile Forensics

Mobile devices contain highly personal and security-sensitive evidence.

Potential evidence includes:

```text id="7h4x0v"
Device Metadata
Applications
Messages
Calls
Contacts
Browser Data
Photos
Location
Authentication
Notifications
Cloud Sync
Network
```

---

# Mobile Forensic Principles

Mobile evidence must be collected according to:

- Legal authority
- Organizational policy
- Device ownership
- Privacy requirements
- Acquisition capability

---

# Android Forensics

Android investigations may involve:

```text id="v9x2m6"
Device Storage
Application Data
Logs
Accounts
Browser Data
Messages
Notifications
System Configuration
Cloud Synchronization
```

The exact available artifacts depend on:

- Android version
- Device manufacturer
- Encryption
- Application
- Acquisition method

---

# iOS Forensics

iOS evidence may involve:

```text id="j6c1r8"
Device Data
Application Data
System Artifacts
Cloud Backups
Messages
Browser Data
Location
Accounts
```

Modern iOS security architecture significantly affects acquisition.

---

# Mobile Application Forensics

Investigate application artifacts such as:

```text id="5q8y1m"
Databases
Caches
Logs
Preferences
Tokens
Attachments
Local Storage
```

The exact artifacts vary by application and operating system.

---

# Mobile Cloud Synchronization

Mobile evidence may exist outside the physical device.

Examples:

```text id="0d6p4x"
Cloud Backup
Application Cloud
Photo Sync
Messaging Platform
Account Data
```

Therefore:

```text id="j2w7q3"
Device
 +
Cloud
 =
Complete Investigation
```

---

# Mobile Network Evidence

Correlate:

```text id="g5s8v1"
Device
 │
 ▼
Application
 │
 ▼
Network
 │
 ▼
Destination
 │
 ▼
Cloud Service
```

This can identify suspicious application communications.

---

# Mobile Evidence Challenges

Challenges include:

- Device encryption
- Locked devices
- Application encryption
- Secure hardware
- Cloud dependency
- Rapid OS changes
- Privacy
- Legal restrictions
- Deleted data

---

# Cloud + Container + Mobile Correlation

Modern incidents can cross all three environments.

Example:

```text id="2y4k7q"
Mobile Device
     │
     ▼
Compromised Identity
     │
     ▼
Cloud Login
     │
     ▼
Cloud API
     │
     ▼
Kubernetes Workload
     │
     ▼
Sensitive Database
```

Investigating only one environment would produce an incomplete picture.

---

# Cross-Platform Timeline

```text id="7m1z4s"
08:55 — Mobile authentication
09:00 — Cloud login
09:02 — API token used
09:04 — Kubernetes API action
09:06 — Pod created
09:10 — Database accessed
09:15 — External transfer
```

This timeline should be validated with independent evidence.

---

# Identity-Centric Investigation

Modern investigations increasingly begin with identity.

```text id="3n7b2q"
Identity
   │
   ├── Mobile
   ├── Cloud
   ├── API
   ├── VM
   └── Kubernetes
```

Investigate:

```text id="k5c8y1"
Identity
Authentication
Session
Token
Resource
Action
Data
```

---

# API Token Forensics

Investigate:

- Token creation
- Token use
- Source
- Scope
- Expiration
- Revocation
- Associated identity

Never expose live tokens in forensic reports.

---

# Cloud Credential Exposure

Potential evidence includes:

```text id="0y7p2x"
Unexpected API Calls
New Credentials
Token Use
Role Changes
Access Policy Changes
```

A credential may be compromised even if the associated user account appears legitimate.

---

# Cloud-to-Container Investigation

Example:

```text id="q8p3d1"
Cloud Identity
     │
     ▼
Cluster API
     │
     ▼
Deployment Change
     │
     ▼
Container Image
     │
     ▼
Pod
     │
     ▼
Network
```

Investigate every transition.

---

# Container-to-Cloud Investigation

A compromised workload may access cloud resources using:

- Workload identities
- Instance roles
- Service accounts
- Environment configuration

Investigate:

```text id="n3r5v7"
Workload
   │
   ▼
Identity
   │
   ▼
API
   │
   ▼
Cloud Resource
```

---

# Common Modern Forensic Mistakes

## Treating Cloud as a Single System

Cloud consists of many services and evidence sources.

## Ignoring Identity

IP-based investigation alone is insufficient.

## Assuming Containers Are Ephemeral and Therefore Unimportant

Centralized telemetry may preserve critical evidence.

## Collecting Only the Container

The node and orchestration platform may contain essential evidence.

## Ignoring Cloud Control Plane

Resource changes can reveal attacker actions.

## Ignoring Mobile Cloud Data

Important evidence may be synchronized externally.

## Exposing Secrets in Reports

Secrets should be protected and redacted.

---

# Cloud and Container Forensic Readiness

Organizations should enable:

```text id="6t9w2c"
Cloud Audit Logs
Identity Logs
MFA
Network Flow Logs
Storage Access Logs
Kubernetes Audit
Container Logs
Image Registry Logs
Endpoint Telemetry
Time Synchronization
```

---

# Evidence Preservation Priority

When a workload is ephemeral:

```text id="x4c8v2"
1. Record Identity
2. Record Resource Metadata
3. Preserve Logs
4. Preserve Audit Events
5. Preserve Network Data
6. Preserve Image Digest
7. Preserve Configuration
8. Preserve Relevant Storage
9. Preserve Node Evidence
10. Build Timeline
```

The exact order depends on incident conditions.

---

# Practical Lab 01 — Cloud Identity Investigation

## Scenario

A cloud identity generated unusual API activity.

Investigate:

```text id="4y7k1m"
User
Source IP
Authentication
MFA
API Calls
Resources
Time
```

Determine whether the activity is:

```text id="q8d5x2"
Expected
Suspicious
Unauthorized
Unknown
```

---

# Practical Lab 02 — Cloud Resource Investigation

Scenario:

> A new virtual machine appears in an account.

Investigate:

```text id="9x1r4v"
Creator
Creation Time
Image
Network
Security Group
Identity
Tags
Logs
```

Determine whether the resource was legitimate.

---

# Practical Lab 03 — Cloud Storage Investigation

Investigate an unexpected object access event.

Determine:

```text id="g2h8m6"
Identity
Object
Action
Source
Timestamp
Download
Authorization
```

---

# Practical Lab 04 — Container Investigation

Scenario:

> A container unexpectedly communicated with an external destination.

Investigate:

```text id="m7c1q5"
Container
Image
Digest
Process
Network
Logs
Identity
Host
```

---

# Practical Lab 05 — Kubernetes Investigation

Scenario:

> An unexpected pod appeared in a production namespace.

Investigate:

```text id="p4w9z2"
Namespace
Pod
ServiceAccount
Creator
Image
Deployment
Network
API Audit
Node
```

---

# Practical Lab 06 — Mobile Evidence Investigation

Using an authorized forensic dataset:

Investigate:

```text id="6v2k8r"
Device
User
Application
Timestamp
Network
Cloud Account
```

Construct a timeline without exposing unnecessary personal information.

---

# Practical Lab 07 — Cross-Platform Investigation

Scenario:

```text id="w3x7n1"
Mobile Login
     │
     ▼
Cloud Authentication
     │
     ▼
API Activity
     │
     ▼
Kubernetes Change
     │
     ▼
Container Network Activity
```

Determine:

1. Which identity was involved?
2. Which resources changed?
3. Which workload was affected?
4. What network activity occurred?
5. What evidence exists on each platform?
6. What evidence is missing?

---

# Modern Platform Forensic Report

```text id="8h5q2v"
# Cloud / Container / Mobile Forensic Report

## Case Information

Case ID:
Investigator:
Time Window:

## Scope

## Cloud Evidence

### Identity

### Authentication

### API Activity

### Resources

### Storage

### Network

## Container Evidence

### Cluster

### Namespace

### Pod

### Container

### Image

### Runtime

### Network

## Mobile Evidence

### Device

### Application

### Account

### Network

### Cloud Synchronization

## Cross-Platform Timeline

## Evidence Correlation

## Findings

## Evidence Gaps

## Privacy Considerations

## Confidence

## Recommendations

## Conclusion
```

---

# Example Finding

```text id="k1w7c3"
Finding ID:
CLOUD-001

Title:
Unexpected Cloud API Activity

Observation:
A cloud identity performed resource-management actions from an unfamiliar source during a period in which no corresponding administrative activity was expected.

Supporting Evidence:
Cloud audit logs
Identity telemetry
Network records
Resource configuration history

Assessment:
The activity is suspicious and requires validation against the account owner and approved administrative activity.

Confidence:
High

Limitation:
Device-level attribution was unavailable.
```

---

# Cloud Forensics and Incident Response

```text id="3z8x5m"
Cloud Alert
     │
     ▼
Identity Triage
     │
     ▼
API Investigation
     │
     ▼
Resource Scoping
     │
     ▼
Credential Containment
     │
     ▼
Workload Investigation
     │
     ▼
Data Exposure Assessment
     │
     ▼
Recovery
```

---

# Container Forensics and Incident Response

```text id="5p2n8c"
Container Alert
      │
      ▼
Identify Pod
      │
      ▼
Preserve Metadata
      │
      ▼
Preserve Logs
      │
      ▼
Identify Image
      │
      ▼
Investigate Node
      │
      ▼
Network Scope
      │
      ▼
Contain
```

---

# Mobile Forensics and Incident Response

```text id="4h9s6w"
Mobile Alert
    │
    ▼
Device / Account
    │
    ▼
Authentication
    │
    ▼
Application
    │
    ▼
Cloud
    │
    ▼
Network
    │
    ▼
Scope
```

---

# Enterprise Modern Forensics Architecture

```text id="e4c7z2"
                         Security Operations
                                │
                                ▼
                         Detection / Alert
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
              Cloud         Containers        Mobile
                │               │               │
        ┌───────┼───────┐       │        ┌──────┼──────┐
        ▼       ▼       ▼       ▼        ▼      ▼      ▼
     Identity  API    Network  K8s     Device  App    Cloud
        │       │       │       │        │      │      │
        └───────┼───────┴───────┼────────┴──────┼──────┘
                │               │               │
                └───────────────┼───────────────┘
                                ▼
                           SIEM / SOAR
                                │
                                ▼
                         Forensic Analysis
                                │
                                ▼
                             Timeline
                                │
                                ▼
                             Findings
```

---

# Evidence Confidence

## High Confidence

Independent evidence agrees across platforms.

```text id="4j7m2v"
Identity
+
Cloud Audit
+
Network
+
Workload
```

## Medium Confidence

Multiple related sources support the conclusion.

## Low Confidence

Single provider artifact or unexplained anomaly.

## Unknown

Evidence is insufficient.

---

# Interview Questions

## 1. Why is cloud forensics different from traditional disk forensics?

Because evidence is distributed across provider services, identities, APIs, workloads, and infrastructure rather than a single physical device.

---

## 2. Why is identity especially important in cloud investigations?

Cloud actions are often API-driven and strongly associated with identities, roles, tokens, and service accounts.

---

## 3. What is CloudTrail?

An AWS service that records supported account activity and API events.

---

## 4. What is the Azure equivalent of cloud activity logging?

Azure provides Activity Logs and Microsoft Entra audit/sign-in logging among other telemetry sources.

---

## 5. What are Google Cloud Audit Logs?

Provider logging mechanisms that record supported activity involving Google Cloud resources and services.

---

## 6. Why are containers difficult to investigate?

They can be short-lived and may disappear before local evidence is collected.

---

## 7. What evidence should be preserved when a Kubernetes pod is suspicious?

At minimum:

```text id="1z5m8r"
Pod Metadata
Image
Digest
Logs
Service Account
API Audit
Network
Node
Configuration
```

---

## 8. Why is the container image important?

It can establish the software and configuration baseline from which the workload originated.

---

## 9. What is a Kubernetes ServiceAccount?

An identity used by workloads to interact with the Kubernetes API and, depending on configuration, other services.

---

## 10. Why can mobile investigations require cloud evidence?

Applications frequently synchronize information to cloud services, and some important artifacts may exist outside the device.

---

## 11. What is the shared responsibility model?

A security model dividing responsibilities between the cloud provider and customer depending on the service.

---

## 12. What is a cloud forensic evidence gap?

A situation where required evidence is unavailable because of logging, retention, encryption, provider limitations, deletion, or other factors.

---

# Scenario Interview Question

### Scenario

> A cloud administrator account appears to have been compromised.

Investigate:

```text id="v8m2k4"
Authentication
   │
   ▼
MFA
   │
   ▼
Session
   │
   ▼
API Calls
   │
   ▼
Resources
   │
   ▼
Data
```

Then determine scope.

---

# Scenario Interview Question

### Scenario

> A suspicious Kubernetes pod disappeared before investigators could inspect it.

Investigate remaining evidence:

```text id="n3c7q1"
Kubernetes Audit
Pod Events
Deployment
Image Registry
Node Logs
Network Telemetry
Centralized Application Logs
Cloud Logs
```

The absence of the pod does not necessarily mean the absence of evidence.

---

# Scenario Interview Question

### Scenario

> A mobile device shows an unusual cloud login.

Investigate:

```text id="f6h1z8"
Device
+
Application
+
Authentication
+
MFA
+
Cloud Identity
+
Network
```

Do not assume the mobile device itself was compromised.

---

# Modern Forensics Maturity Model

## Level 1 — Basic

- Cloud audit logs
- Container logs
- Mobile evidence awareness

## Level 2 — Repeatable

- Identity investigation
- Cloud API analysis
- Container metadata collection

## Level 3 — Managed

- Centralized cloud logging
- Kubernetes audit
- Mobile forensic procedures

## Level 4 — Integrated

- Cloud + SIEM + EDR
- Identity threat detection
- Container runtime telemetry
- Cross-platform investigation

## Level 5 — Advanced

- Enterprise cloud forensics
- Automated evidence preservation
- Kubernetes-scale investigations
- Identity-centric correlation
- Cross-cloud investigations
- Continuous forensic readiness

---

# Chapter Completion Checklist

```text id="w6f9x2"
[ ] Understand cloud forensics
[ ] Understand shared responsibility
[ ] Understand cloud identity
[ ] Understand cloud authentication
[ ] Understand API forensics
[ ] Understand AWS CloudTrail
[ ] Understand Azure activity/audit logs
[ ] Understand Google Cloud Audit Logs
[ ] Understand cloud storage forensics
[ ] Understand cloud VM forensics
[ ] Understand snapshots
[ ] Understand configuration forensics
[ ] Understand cloud evidence gaps
[ ] Understand container forensics
[ ] Understand Docker evidence
[ ] Understand image digests
[ ] Understand container networking
[ ] Understand Kubernetes forensics
[ ] Understand Kubernetes audit
[ ] Understand ServiceAccounts
[ ] Understand ephemeral workloads
[ ] Understand node forensics
[ ] Understand Android forensics
[ ] Understand iOS forensics
[ ] Understand mobile application evidence
[ ] Understand mobile cloud synchronization
[ ] Understand cross-platform timelines
[ ] Complete cloud identity lab
[ ] Complete cloud resource lab
[ ] Complete container lab
[ ] Complete Kubernetes lab
[ ] Complete mobile lab
[ ] Complete cross-platform investigation
```

---

# Key Takeaways

Modern digital forensics is no longer limited to physical disks and endpoints.

A complete investigation may span:

```text id="q7x5m3"
Identity
   +
Cloud
   +
API
   +
VM
   +
Container
   +
Kubernetes
   +
Mobile
   +
Network
```

Remember:

- Cloud evidence is distributed.
- Identity is often more important than IP address.
- API logs can reconstruct administrative activity.
- Cloud configuration changes are forensic evidence.
- Containers may disappear quickly.
- Image digests help establish workload identity.
- Kubernetes audit logs can preserve actions after pods disappear.
- Node-level evidence can be critical.
- Mobile evidence may extend into cloud services.
- Secrets and tokens must be protected during investigations.
- Privacy and legal requirements are especially important for mobile evidence.
- Evidence gaps should be documented explicitly.
- Cross-platform correlation produces stronger conclusions.

> **Modern forensic investigations follow identities, APIs, workloads, devices, and data across infrastructure boundaries rather than treating each platform as an isolated system.**

---

# References

### AWS CloudTrail

https://docs.aws.amazon.com/awscloudtrail/

### AWS Security Documentation

https://docs.aws.amazon.com/security/

### Microsoft Entra Documentation

https://learn.microsoft.com/entra/

### Azure Activity Log

https://learn.microsoft.com/azure/azure-monitor/essentials/activity-log

### Microsoft Defender for Cloud

https://learn.microsoft.com/azure/defender-for-cloud/

### Google Cloud Audit Logs

https://cloud.google.com/logging/docs/audit

### Google Cloud Security

https://cloud.google.com/security

### Docker Documentation

https://docs.docker.com/

### Kubernetes Documentation

https://kubernetes.io/docs/

### Kubernetes Auditing

https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/

### NIST SP 800-86

https://csrc.nist.gov/publications/detail/sp/800-86/final

### NIST SP 800-61

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### MITRE ATT&CK

https://attack.mitre.org/

### Android Security

https://source.android.com/docs/security

### Apple Platform Security

https://support.apple.com/guide/security/welcome/web

---

> **Follow the identity. Preserve the cloud trail. Capture ephemeral workloads. Correlate device, workload, API, and network evidence into one timeline.**
