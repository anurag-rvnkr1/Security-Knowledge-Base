# Chapter 76 – Compliance & Auditing

## Overview

Kubernetes Compliance and Auditing is the process of ensuring that Kubernetes clusters, workloads, identities, configurations, infrastructure, and operational practices satisfy defined security, regulatory, organizational, and industry requirements.

Security asks:

```text
"How do we protect the environment?"
```

Compliance asks:

```text
"Can we demonstrate that required controls are implemented and working?"
```

Auditing provides the evidence.

A simplified compliance lifecycle is:

```text
Requirements
     ↓
Controls
     ↓
Implementation
     ↓
Monitoring
     ↓
Evidence
     ↓
Audit
     ↓
Findings
     ↓
Remediation
     ↓
Continuous Improvement
```

Kubernetes compliance can involve:

```text
Identity
RBAC
Authentication
Authorization
Secrets
Network Security
Pod Security
Image Security
Supply Chain
Logging
Monitoring
Vulnerability Management
Backup
Data Protection
Configuration
Cloud Infrastructure
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes compliance fundamentals
- Security auditing
- Compliance vs security
- Governance
- Risk management
- Regulatory requirements
- Security policies
- Kubernetes audit logs
- Audit policy
- Audit levels
- Audit backends
- Log retention
- Evidence collection
- Evidence integrity
- Access control
- RBAC auditing
- ServiceAccount auditing
- Authentication auditing
- Authorization auditing
- Admission auditing
- Network Policy auditing
- Pod Security auditing
- Secret access auditing
- Container image compliance
- Image provenance
- SBOM compliance
- Supply-chain compliance
- Vulnerability management compliance
- Patch management
- Configuration compliance
- CIS Kubernetes Benchmark
- NIST
- ISO 27001
- SOC 2
- PCI DSS
- HIPAA
- GDPR
- Data protection
- Cloud compliance
- Multi-cluster compliance
- Policy as Code
- OPA
- Gatekeeper
- Kyverno
- Admission Policies
- Continuous Compliance
- Compliance Monitoring
- Compliance Dashboards
- Audit Evidence
- Audit Trails
- Control Mapping
- Security Controls
- Control Validation
- Compliance Exceptions
- Risk Acceptance
- Remediation
- Compliance Reporting
- Internal Audits
- External Audits
- Third-Party Audits
- Audit Preparation
- Audit Findings
- Corrective Actions
- Preventive Actions
- Continuous Improvement
- Security Governance
- Production Compliance
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is Compliance?

Compliance means meeting defined requirements.

Requirements may come from:

```text
Law
Regulation
Industry Standard
Contract
Customer Requirement
Internal Policy
Security Framework
```

---

# What Is Auditing?

Auditing is the systematic examination of:

```text
Controls
Configurations
Activities
Evidence
Processes
```

to determine whether requirements are being satisfied.

---

# Compliance vs Security

These concepts are related but different.

| Security | Compliance |
|---|---|
| Protect systems | Demonstrate required controls |
| Focuses on risk | Focuses on requirements |
| Prevents/detects threats | Measures control adherence |
| Technical + operational | Technical + procedural + governance |

A system can be:

```text
Compliant but insecure
```

if controls exist on paper but do not adequately address real-world threats.

---

# Governance

Governance defines:

```text
Who Is Responsible?
What Is Required?
Who Approves?
How Is Risk Managed?
How Is Compliance Demonstrated?
```

---

# Risk Management

Compliance does not eliminate risk.

A practical model is:

```text
Identify Risk
     ↓
Assess Risk
     ↓
Implement Controls
     ↓
Monitor
     ↓
Remediate
     ↓
Accept / Transfer / Avoid / Reduce
```

---

# Security Policy

A Kubernetes security policy may define:

```text
Authentication
RBAC
Pod Security
Network Security
Image Security
Logging
Secrets
Backups
Incident Response
```

---

# Control

A control is a mechanism designed to reduce risk or satisfy a requirement.

Examples:

```text
RBAC
NetworkPolicy
Audit Logging
Image Scanning
Admission Policy
Encryption
Backup
```

---

# Control Objective

A control objective describes what should be achieved.

Example:

```text
Only authorized users should access production workloads.
```

Possible controls:

```text
RBAC
MFA
Least Privilege
Audit Logging
```

---

# Control Mapping

A single Kubernetes control may support multiple requirements.

Example:

```text
Centralized Audit Logging
        │
        ├── Security Monitoring
        ├── Incident Response
        ├── Accountability
        └── Audit Evidence
```

---

# Kubernetes Compliance Architecture

```text
                 Requirements
                       │
                       ▼
                    Policies
                       │
                       ▼
                Kubernetes Controls
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
      RBAC        Pod Security     Network
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Monitoring
                       │
                       ▼
                     Audit
                       │
                       ▼
                    Evidence
                       │
                       ▼
                    Reports
```

---

# Kubernetes Audit Logging

Kubernetes Audit Logging records security-relevant API activity.

It can help answer:

```text
Who?
What?
When?
Where?
Which Resource?
Which Namespace?
```

---

# Why Audit Logs Matter

Audit logs provide evidence of API activity.

Examples:

```text
Pod Created
Secret Accessed
Role Changed
ServiceAccount Modified
Deployment Deleted
```

---

# Kubernetes Audit Policy

The audit policy determines which events are recorded and at what level.

Example structure:

```yaml
apiVersion: audit.k8s.io/v1
kind: Policy

rules:
  - level: Metadata
```

A real production policy should be designed according to security, privacy, storage, and performance requirements.

---

# Audit Levels

Kubernetes commonly supports levels such as:

```text
None
Metadata
Request
RequestResponse
```

---

# None

```text
No Event Logged
```

Useful when a particular activity does not need auditing.

---

# Metadata

Records metadata such as:

```text
User
Timestamp
Resource
Verb
Namespace
```

It does not record full request and response bodies.

---

# Request

Records metadata plus the request information where supported.

This can provide more investigative context.

---

# RequestResponse

Records metadata, request information, and response information.

This can produce significantly more sensitive data and storage overhead.

Use carefully.

---

# Audit Policy Design

A good audit policy balances:

```text
Security Visibility
+
Privacy
+
Storage
+
Performance
```

---

# Audit Backends

Audit events can be sent to supported backends such as:

```text
Log
Webhook
```

A centralized architecture can forward audit information into security infrastructure.

---

# Audit Log Retention

Retention should be based on:

```text
Security Requirements
Compliance Requirements
Incident Response Requirements
Storage Capacity
Privacy Requirements
```

---

# Long-Term Audit Storage

For important environments:

```text
Kubernetes
   ↓
Audit Logs
   ↓
Central Logging
   ↓
Immutable / Protected Storage
   ↓
SIEM
```

---

# Evidence Collection

Compliance evidence can include:

```text
Configuration
Logs
Policies
Screenshots
Reports
Access Reviews
Vulnerability Reports
Change Records
Incident Records
```

---

# Evidence Integrity

Evidence should be protected against unauthorized modification.

Controls include:

```text
Access Control
Hashing
Encryption
Immutable Storage
Audit Trails
Retention Policies
```

---

# Evidence Access

Use least privilege.

Only authorized personnel should access sensitive compliance evidence.

---

# RBAC Auditing

Review:

```text
Users
Groups
ServiceAccounts
Roles
RoleBindings
ClusterRoles
ClusterRoleBindings
```

---

# RBAC Compliance Questions

Ask:

```text
Who Has Access?
Why?
What Permissions?
Which Namespace?
Is Access Still Required?
Was Access Reviewed?
```

---

# ServiceAccount Auditing

Review:

```text
ServiceAccount Creation
ServiceAccount Changes
RoleBindings
ClusterRoleBindings
Token Usage
```

---

# Authentication Auditing

Monitor:

```text
Successful Authentication
Failed Authentication
Unknown Identities
Credential Changes
Authentication Method
Source IP
```

---

# Authorization Auditing

Determine:

```text
Who Attempted Access?
What Resource?
Which Verb?
Was Access Allowed?
```

---

# Admission Auditing

Admission controls can enforce policies before resources are persisted.

Audit:

```text
Allowed Requests
Rejected Requests
Policy Violations
Policy Changes
```

---

# Pod Security Auditing

Review workloads for:

```text
Privileged Containers
Host Network
Host PID
Host IPC
HostPath
Capabilities
Root User
Privilege Escalation
```

---

# Pod Security Standards

Kubernetes Pod Security Standards commonly define:

```text
Privileged
Baseline
Restricted
```

---

# Privileged

Provides broad flexibility with minimal restrictions.

It is generally unsuitable for workloads that do not require elevated privileges.

---

# Baseline

Blocks many known privilege-escalation configurations while permitting common workloads.

---

# Restricted

Provides stronger restrictions intended for security-sensitive workloads.

---

# Network Policy Auditing

Check:

```bash
kubectl get networkpolicy -A
```

Ask:

```text
Which Namespaces Are Isolated?
Which Traffic Is Allowed?
Which Traffic Is Denied?
Are Production Workloads Protected?
```

---

# Default-Deny

A common security architecture is:

```text
Default Deny
      ↓
Explicitly Allow Required Traffic
```

This supports network segmentation.

---

# Secret Access Auditing

Sensitive resources include:

```text
Kubernetes Secrets
Cloud Credentials
Database Credentials
TLS Keys
API Tokens
```

Audit:

```text
Who
Accessed
Which Secret
When
From Where
```

---

# Secret Management Compliance

Controls may include:

```text
Encryption at Rest
Access Control
Rotation
Short-Lived Credentials
External Secret Management
Audit Logging
```

---

# Container Image Compliance

Organizations may require:

```text
Approved Registry
Vulnerability Scanning
Image Signing
SBOM
Provenance
Known Source
Approved Base Image
```

---

# Image Provenance

Provenance helps establish:

```text
Where Was Image Built?
From Which Source?
Which Pipeline?
Which Commit?
Who Built It?
```

---

# SBOM

SBOM means:

```text
Software Bill of Materials
```

It provides a machine-readable inventory of software components.

Example:

```text
Application
 ├── Library A
 ├── Library B
 └── Library C
```

---

# SBOM and Compliance

SBOMs can help with:

```text
Vulnerability Management
Supply-Chain Visibility
License Tracking
Incident Response
Software Inventory
```

---

# Supply Chain Compliance

Important controls include:

```text
Source Control
CI/CD Security
Dependency Management
Image Scanning
Image Signing
Provenance
Registry Security
Admission Policy
```

---

# Vulnerability Management Compliance

A mature program should track:

```text
Vulnerability
Severity
Affected Asset
Owner
Due Date
Remediation
Exception
Status
```

---

# Patch Management

Track:

```text
Node OS
Container Images
Kubernetes Version
Dependencies
Runtime
Applications
```

---

# Configuration Compliance

Check:

```text
RBAC
Pod Security
Network Policies
Encryption
Audit Logging
Admission
Storage
```

---

# Configuration Drift

Drift occurs when actual configuration differs from the approved baseline.

Example:

```text
Approved:
privileged = false

Actual:
privileged = true
```

This should generate a compliance finding.

---

# CIS Kubernetes Benchmark

The CIS Kubernetes Benchmark provides security configuration guidance for Kubernetes.

It can help organizations evaluate areas such as:

```text
Control Plane
Worker Nodes
Policies
Authentication
Authorization
Logging
```

---

# Important Note About Benchmarks

A benchmark is guidance.

It should be interpreted according to:

```text
Environment
Threat Model
Business Requirements
Platform
Version
```

Do not blindly apply every recommendation without understanding operational impact.

---

# NIST

NIST publishes cybersecurity frameworks and guidance that organizations may use for:

```text
Risk Management
Security Controls
Incident Response
Identity
Monitoring
Governance
```

---

# ISO 27001

ISO/IEC 27001 provides requirements for an Information Security Management System (ISMS).

Kubernetes controls may support broader organizational controls under an ISMS.

---

# SOC 2

SOC 2 evaluates organizational controls around trust service criteria.

Kubernetes evidence may support controls involving:

```text
Security
Availability
Confidentiality
Processing Integrity
Privacy
```

depending on the scope and applicable criteria.

---

# PCI DSS

PCI DSS applies to organizations handling payment card data.

Kubernetes environments within the relevant cardholder-data environment may require controls around:

```text
Access
Logging
Vulnerability Management
Network Security
Configuration
Monitoring
```

---

# HIPAA

HIPAA applies to covered entities and business associates handling protected health information in applicable contexts.

Kubernetes workloads handling sensitive healthcare data may require:

```text
Access Controls
Audit Controls
Data Protection
Risk Management
```

---

# GDPR

GDPR applies to organizations and processing activities within its scope.

Kubernetes infrastructure handling personal data may need controls around:

```text
Access
Data Protection
Logging
Retention
Privacy
Incident Management
```

---

# Compliance Does Not Equal Certification

Implementing technical controls does not automatically mean an organization is certified.

Certification or formal attestation depends on:

```text
Scope
Applicable Standard
Assessment
Evidence
Auditor
Organization
```

---

# Cloud Compliance

Managed Kubernetes requires attention to both:

```text
Kubernetes
+
Cloud Provider
```

Review:

```text
IAM
Networking
Storage
Encryption
Logging
Control Plane
Worker Nodes
Cloud Audit Logs
```

---

# Multi-Cluster Compliance

Organizations may have:

```text
Development
Staging
Production
DR
Regional Clusters
```

Compliance should be consistently evaluated across all relevant clusters.

---

# Compliance Architecture

```text
             Multiple Clusters
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
      Dev         Stage       Prod
        │           │           │
        └───────────┼───────────┘
                    ▼
             Policy Engine
                    │
                    ▼
            Compliance Checks
                    │
             ┌──────┴──────┐
             ▼             ▼
          Findings       Passed
             │
             ▼
         Remediation
             │
             ▼
          Evidence
             │
             ▼
           Report
```

---

# Policy as Code

Policy as Code represents security and compliance rules in machine-readable form.

Example concept:

```text
IF privileged container
THEN reject
```

---

# Benefits of Policy as Code

```text
Consistency
Automation
Version Control
Repeatability
Auditability
```

---

# Open Policy Agent

OPA is a general-purpose policy engine commonly used for policy decisions.

Conceptually:

```text
Request
   ↓
OPA
   ↓
Policy Evaluation
   ↓
Allow / Deny
```

---

# Gatekeeper

Gatekeeper integrates OPA-based policy enforcement into Kubernetes admission workflows.

It can help enforce policies such as:

```text
Approved Registries
Required Labels
Restricted Configurations
Resource Requirements
```

---

# Kyverno

Kyverno is a Kubernetes-native policy engine.

Policies can validate or mutate Kubernetes resources.

---

# OPA vs Kyverno

| OPA/Gatekeeper | Kyverno |
|---|---|
| General policy engine | Kubernetes-native |
| Rego-based | YAML-oriented policies |
| Broad policy use cases | Kubernetes-focused |
| Strong policy flexibility | Familiar Kubernetes-style experience |

The right choice depends on the organization's requirements.

---

# Admission Policies

Admission policies can enforce:

```text
No Privileged Containers
Approved Images
Required Labels
Required SecurityContext
Resource Limits
```

---

# Compliance Enforcement Flow

```text
Developer
   ↓
Manifest
   ↓
Admission
   ↓
Policy Evaluation
   ↓
Allow / Reject
```

---

# Continuous Compliance

Traditional compliance may be periodic:

```text
Audit
 ↓
Finding
 ↓
Fix
```

Continuous compliance is:

```text
Monitor
 ↓
Detect Drift
 ↓
Alert
 ↓
Remediate
 ↓
Verify
```

---

# Compliance Monitoring

Monitor continuously for:

```text
Configuration Drift
New Vulnerabilities
RBAC Changes
Policy Changes
Image Changes
Unauthorized Access
Logging Failures
```

---

# Compliance Dashboard

A dashboard may show:

```text
Overall Compliance
Critical Findings
Open Findings
Policy Violations
Vulnerabilities
RBAC Violations
Image Violations
Configuration Drift
```

---

# Compliance Score

Organizations may calculate an internal score such as:

```text
Compliant Controls
------------------ × 100
Total Controls
```

This is an internal metric and should not automatically be interpreted as regulatory compliance.

---

# Audit Trail

An audit trail records activities over time.

Examples:

```text
Login
API Request
Configuration Change
Deployment
Policy Change
Credential Change
```

---

# Change Management

Security-sensitive Kubernetes changes should be traceable.

Examples:

```text
RBAC Change
NetworkPolicy Change
Deployment Change
Admission Policy Change
Cluster Configuration Change
```

---

# GitOps and Compliance

GitOps can improve auditability:

```text
Git Commit
   ↓
Review
   ↓
CI Checks
   ↓
Policy Validation
   ↓
Deployment
```

This creates a traceable change history.

---

# Compliance Exceptions

Sometimes a requirement cannot immediately be met.

An exception should document:

```text
Requirement
Reason
Risk
Compensating Control
Owner
Approval
Expiration
```

---

# Risk Acceptance

Risk acceptance should be:

```text
Documented
Approved
Time-Bounded
Reviewed
```

Avoid permanent undocumented exceptions.

---

# Remediation

A compliance finding should have:

```text
Finding
Severity
Owner
Action
Due Date
Status
Evidence
```

---

# Corrective Action

Corrective action fixes an identified issue.

Example:

```text
Finding:
Privileged container

Correction:
Remove privileged access
```

---

# Preventive Action

Preventive action prevents recurrence.

Example:

```text
Admission Policy
+
CI Validation
```

to prevent future privileged workloads.

---

# Audit Findings

Typical findings may include:

```text
Excessive RBAC
Missing Audit Logging
Privileged Pod
Unapproved Image
Missing NetworkPolicy
Unencrypted Data
Unsupported Kubernetes Version
Critical Vulnerability
```

---

# Finding Severity

A simple classification:

```text
Critical
High
Medium
Low
Informational
```

Severity should consider:

```text
Risk
Impact
Exploitability
Asset Criticality
Exposure
```

---

# Audit Process

A typical audit:

```text
Define Scope
    ↓
Identify Requirements
    ↓
Map Controls
    ↓
Collect Evidence
    ↓
Test Controls
    ↓
Identify Findings
    ↓
Remediate
    ↓
Retest
    ↓
Report
```

---

# Internal Audit

Performed by:

```text
Internal Security Team
Internal Audit
Compliance Team
```

Purpose:

```text
Find Problems Before External Assessment
```

---

# External Audit

Performed by an independent assessor or auditor according to the applicable framework or engagement.

---

# Third-Party Audit

Third parties may assess:

```text
Cloud Provider
SaaS Provider
Managed Kubernetes
Vendor
Supplier
```

---

# Audit Preparation

Before an audit:

```text
Define Scope
 ↓
Collect Policies
 ↓
Collect Evidence
 ↓
Review Configurations
 ↓
Validate Controls
 ↓
Resolve Known Findings
```

---

# Evidence Package

A compliance evidence package may include:

```text
Policies
Architecture
Access Reviews
Audit Logs
Vulnerability Reports
Configuration Reports
Backup Evidence
Incident Records
Change Records
Training Records
```

---

# Audit Evidence Retention

Retention should follow:

```text
Legal Requirements
Regulatory Requirements
Contractual Requirements
Internal Policy
Incident Requirements
```

---

# Security Governance

Governance connects:

```text
Business
+
Risk
+
Security
+
Compliance
+
Operations
```

---

# Compliance and DevSecOps

Integrate compliance into the development lifecycle:

```text
Code
 ↓
Build
 ↓
Scan
 ↓
Policy
 ↓
Deploy
 ↓
Monitor
 ↓
Audit
```

---

# Compliance in CI/CD

Pipeline checks can validate:

```text
Image Vulnerabilities
Secrets
Manifest Security
SBOM
Image Signature
Policy Violations
```

---

# Example CI Compliance Flow

```text
Pull Request
      ↓
Security Scan
      ↓
SBOM
      ↓
Policy Check
      ↓
Image Scan
      ↓
Approval
      ↓
Deploy
```

---

# Kubernetes Compliance Control Matrix

| Control Area | Example Control | Evidence |
|---|---|---|
| Identity | RBAC | Role/Binding Reports |
| Authentication | Strong Authentication | Identity Logs |
| Audit | API Audit Logging | Audit Logs |
| Pod Security | Restricted Workloads | Policy Reports |
| Network | NetworkPolicy | Policy Inventory |
| Images | Approved Registry | Image Reports |
| Vulnerabilities | Scanning | Scan Reports |
| Secrets | Controlled Access | Audit Logs |
| Runtime | Threat Detection | Runtime Alerts |
| Backup | Tested Backup | Backup Reports |
| Change | GitOps | Git History |

---

# Compliance Monitoring Architecture

```text
Kubernetes
    │
    ├── Configuration
    ├── Audit Logs
    ├── Policies
    ├── Vulnerabilities
    └── Runtime
           │
           ▼
      Compliance Engine
           │
      ┌────┴────┐
      ▼         ▼
   Compliant  Violation
                 │
                 ▼
             Remediation
                 │
                 ▼
               Evidence
                 │
                 ▼
               Report
```

---

# Common Compliance Controls

## Identity

```text
Least Privilege
MFA
RBAC
Access Reviews
```

---

## Workload Security

```text
Pod Security
Non-Root
Read-Only Filesystem
Dropped Capabilities
seccomp
```

---

## Network

```text
NetworkPolicy
Segmentation
Ingress Controls
Egress Controls
```

---

## Images

```text
Approved Registry
Scanning
Signing
SBOM
Provenance
```

---

## Secrets

```text
Encryption
Access Control
Rotation
External Secret Management
```

---

## Logging

```text
Audit Logs
Centralized Logging
Retention
Integrity
```

---

# Compliance and Encryption

Potential requirements may include encryption:

```text
In Transit
At Rest
```

Examples:

```text
TLS
Storage Encryption
Secret Encryption
Database Encryption
```

---

# Encryption of Kubernetes Secrets

Kubernetes Secrets are not automatically equivalent to secure encrypted storage merely because they are represented as Secret objects.

Organizations should evaluate:

```text
Encryption at Rest
KMS Integration
Access Control
Secret Rotation
```

---

# Compliance and Backup

Backups should be:

```text
Secure
Encrypted
Access Controlled
Tested
Monitored
```

Regular restoration testing is essential.

---

# Compliance and Disaster Recovery

Organizations may define:

```text
RPO
RTO
Backup Frequency
Recovery Procedures
Testing Requirements
```

---

# Compliance and Incident Response

Incident records can become audit evidence.

Document:

```text
Detection
Investigation
Containment
Eradication
Recovery
RCA
Corrective Actions
```

---

# Compliance and Forensics

Forensic evidence should maintain:

```text
Integrity
Access Control
Retention
Chain of Custody
```

---

# Production Compliance Checklist

```text
☑ Security policy documented
☑ Kubernetes scope defined
☑ RBAC reviewed
☑ Authentication monitored
☑ Audit logging enabled
☑ Audit policy reviewed
☑ Log retention defined
☑ Pod Security enforced
☑ Network policies reviewed
☑ Secrets protected
☑ Images scanned
☑ Image provenance validated
☑ SBOM available where required
☑ Vulnerabilities tracked
☑ Patch management implemented
☑ Configuration baseline defined
☑ Configuration drift monitored
☑ Admission policies enabled
☑ Compliance policies version-controlled
☑ Evidence collection automated
☑ Evidence integrity protected
☑ Backup controls validated
☑ Disaster recovery tested
☑ Incident response documented
☑ Compliance exceptions documented
☑ Risk acceptance documented
☑ Findings tracked
☑ Remediation tracked
☑ Audit readiness reviewed
```

---

# Common Mistakes

## 1. Treating Compliance as a Checkbox Exercise

Compliance should support actual security outcomes.

---

## 2. No Evidence

A control that cannot be demonstrated may be difficult to validate during an audit.

---

## 3. Manual Compliance Only

Manual checks do not scale well across large clusters.

---

## 4. Ignoring Configuration Drift

A compliant cluster can become non-compliant after a configuration change.

---

## 5. No Ownership

Every finding should have:

```text
Owner
Due Date
Status
```

---

## 6. Permanent Exceptions

Exceptions should be:

```text
Approved
Documented
Time-Bounded
```

---

## 7. Ignoring Cloud Infrastructure

Kubernetes compliance often depends on cloud controls.

---

## 8. Overly Broad RBAC

Excessive permissions increase security and compliance risk.

---

## 9. Poor Audit Retention

Insufficient retention can make historical investigations difficult.

---

## 10. Logging Sensitive Data

Audit and application logs can contain sensitive information.

Use:

```text
Redaction
Access Control
Retention
```

---

## 11. Blindly Applying Benchmarks

Every benchmark recommendation should be evaluated against the actual environment.

---

## 12. No Continuous Monitoring

Periodic audits can miss problems between assessments.

---

# Best Practices

### 1. Define Requirements First

Know:

```text
Which Standard?
Which Scope?
Which Controls?
Which Evidence?
```

---

### 2. Automate Compliance

Use:

```text
Policy as Code
CI/CD
Continuous Scanning
```

---

### 3. Centralize Evidence

Maintain controlled evidence repositories.

---

### 4. Protect Evidence

Use:

```text
Encryption
Access Control
Immutable Storage
Hashing
```

---

### 5. Monitor Drift

Continuously compare:

```text
Expected
vs
Actual
```

---

### 6. Use Least Privilege

Review RBAC regularly.

---

### 7. Integrate Security Into CI/CD

Catch problems before production.

---

### 8. Maintain Audit Trails

Track:

```text
Who
What
When
Why
```

---

### 9. Test Controls

A control should not merely exist.

Verify that it actually works.

---

### 10. Treat Compliance as Continuous

Use:

```text
Monitor
 ↓
Detect
 ↓
Remediate
 ↓
Verify
```

---

# Hands-on Lab 1 – Kubernetes Audit Logging

Configure a test Kubernetes environment with an audit policy.

Generate API activity.

Review:

```text
User
Verb
Resource
Namespace
Timestamp
```

---

# Hands-on Lab 2 – Audit Levels

Experiment with:

```text
Metadata
Request
RequestResponse
```

Compare:

```text
Information Captured
Storage Volume
Sensitive Data Exposure
```

---

# Hands-on Lab 3 – RBAC Compliance

Create intentionally excessive RBAC permissions in a test environment.

Identify:

```text
Excessive Access
Sensitive Permissions
Cluster-Wide Access
```

Remediate them.

---

# Hands-on Lab 4 – Pod Security Compliance

Create test Pods with:

```text
Privileged
Root User
Host Network
HostPath
Additional Capabilities
```

Evaluate them against your chosen Pod Security requirements.

---

# Hands-on Lab 5 – Network Compliance

Deploy:

```text
Frontend
Backend
Database
```

Implement:

```text
Default Deny
Explicit Allow
```

Validate the resulting traffic paths.

---

# Hands-on Lab 6 – Image Compliance

Create an image compliance policy requiring:

```text
Approved Registry
Non-Latest Tag
Image Digest
```

Test compliant and non-compliant images.

---

# Hands-on Lab 7 – Policy as Code

Use Gatekeeper or Kyverno in a disposable cluster.

Create a policy:

```text
Reject privileged containers
```

Attempt deployment.

Observe:

```text
Allow
vs
Reject
```

---

# Hands-on Lab 8 – Configuration Drift

Deploy a compliant resource.

Modify it manually.

Detect:

```text
Expected Configuration
vs
Actual Configuration
```

---

# Hands-on Lab 9 – Vulnerability Compliance

Generate a test vulnerability report.

Create a tracking table:

```text
Vulnerability
Severity
Asset
Owner
Due Date
Status
```

---

# Hands-on Lab 10 – SBOM Compliance

Generate an SBOM for a test image.

Identify:

```text
Packages
Versions
Dependencies
Licenses
```

---

# Hands-on Lab 11 – Evidence Collection

Collect:

```text
RBAC
NetworkPolicies
Pod Security
Audit Logs
Image Reports
Vulnerability Reports
```

Organize them into an audit evidence package.

---

# Hands-on Lab 12 – Evidence Integrity

Hash evidence:

```bash
sha256sum evidence/*
```

Record the hashes.

Verify the hashes later.

---

# Hands-on Lab 13 – Compliance Dashboard

Create a dashboard showing:

```text
Compliance Score
Critical Findings
RBAC Violations
Image Violations
Policy Violations
Vulnerabilities
Configuration Drift
```

---

# Hands-on Lab 14 – Continuous Compliance

Build a workflow:

```text
Configuration Change
 ↓
Policy Evaluation
 ↓
Violation
 ↓
Alert
 ↓
Ticket
 ↓
Remediation
 ↓
Verification
```

---

# Hands-on Lab 15 – Audit Simulation

Simulate an external audit.

Prepare evidence for:

```text
Access Control
Logging
Network Security
Image Security
Vulnerability Management
Incident Response
Backup
```

---

# Hands-on Lab 16 – Full Compliance Exercise

Build a test Kubernetes environment.

Implement:

```text
RBAC
Pod Security
NetworkPolicy
Audit Logging
Image Scanning
Admission Policy
Runtime Detection
Backup
```

Then conduct:

```text
Internal Audit
 ↓
Findings
 ↓
Risk Assessment
 ↓
Remediation
 ↓
Retest
 ↓
Final Report
```

---

# Quick Revision

## Compliance

```text
Meeting defined requirements
```

---

## Auditing

```text
Evaluating controls and evidence
```

---

## Governance

```text
Management of security, risk, policies, and responsibilities
```

---

## Control

```text
Mechanism used to reduce risk or satisfy a requirement
```

---

## Audit Trail

```text
Record of activities over time
```

---

## Policy as Code

```text
Machine-readable security and compliance rules
```

---

## OPA

```text
General-purpose policy engine
```

---

## Gatekeeper

```text
Kubernetes admission policy enforcement using OPA
```

---

## Kyverno

```text
Kubernetes-native policy engine
```

---

## Configuration Drift

```text
Difference between approved and actual configuration
```

---

## Evidence

```text
Information used to demonstrate control implementation or activity
```

---

## Risk Acceptance

```text
Formal decision to accept a defined risk
```

---

# Essential Commands

List all Pods:

```bash
kubectl get pods -A
```

List Nodes:

```bash
kubectl get nodes
```

List Services:

```bash
kubectl get svc -A
```

List NetworkPolicies:

```bash
kubectl get networkpolicy -A
```

List ServiceAccounts:

```bash
kubectl get serviceaccounts -A
```

List Roles:

```bash
kubectl get roles -A
```

List RoleBindings:

```bash
kubectl get rolebindings -A
```

List ClusterRoles:

```bash
kubectl get clusterroles
```

List ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

List Deployments:

```bash
kubectl get deployments -A
```

List DaemonSets:

```bash
kubectl get daemonsets -A
```

List StatefulSets:

```bash
kubectl get statefulsets -A
```

List CronJobs:

```bash
kubectl get cronjobs -A
```

List Secrets:

```bash
kubectl get secrets -A
```

List ConfigMaps:

```bash
kubectl get configmaps -A
```

List Pod Security labels:

```bash
kubectl get namespaces --show-labels
```

Inspect a Pod:

```bash
kubectl get pod <pod> -o yaml
```

Inspect a Deployment:

```bash
kubectl get deployment <deployment> -o yaml
```

View Events:

```bash
kubectl get events -A
```

View current context:

```bash
kubectl config current-context
```

View contexts:

```bash
kubectl config get-contexts
```

Hash evidence:

```bash
sha256sum <file>
```

---

# Interview Questions

## Basic

- What is Kubernetes compliance?
- What is Kubernetes auditing?
- What is the difference between security and compliance?
- What is governance?
- What is a security control?
- What is an audit trail?
- What is configuration drift?
- What is policy as code?
- What is OPA?
- What is Gatekeeper?
- What is Kyverno?
- What is the CIS Kubernetes Benchmark?
- What is an SBOM?
- Why are Kubernetes audit logs important?

---

## Intermediate

- How do you audit Kubernetes RBAC?
- How do you audit ServiceAccounts?
- How do you audit Kubernetes API activity?
- What are Kubernetes audit levels?
- What is the difference between Metadata and RequestResponse audit levels?
- How do you implement continuous compliance?
- How do you detect configuration drift?
- How can admission controllers support compliance?
- How can Kyverno enforce security policies?
- How can Gatekeeper enforce Kubernetes policies?
- How do you manage compliance exceptions?
- How do you collect Kubernetes audit evidence?
- How do you protect audit evidence?

---

## Advanced

- Design a continuous Kubernetes compliance architecture.
- How would you map Kubernetes controls to an enterprise compliance framework?
- How would you implement policy as code across multiple clusters?
- How would you design a compliance system for 100+ Kubernetes clusters?
- How would you prevent configuration drift?
- How would you automate compliance evidence collection?
- How would you integrate Kubernetes compliance with CI/CD?
- How would you combine vulnerability management and compliance?
- How would you design Kubernetes audit logging for a regulated environment?
- How would you handle a conflict between a security benchmark and application availability?
- How would you design exception and risk-acceptance workflows?
- How would you prove that a Kubernetes security control is operating effectively?

---

# Interview Scenario 1

### Question

> Your Kubernetes cluster is compliant during an audit, but a week later someone deploys a privileged Pod. How do you prevent this?

### Answer

Use continuous enforcement:

```text
Admission Policy
       +
CI/CD Policy Checks
       +
Runtime Monitoring
       +
Configuration Drift Detection
```

For example:

```text
Developer
   ↓
Manifest
   ↓
CI Policy
   ↓
Admission Policy
   ↓
Deploy
   ↓
Runtime Monitoring
```

This prevents or detects violations after the initial audit.

---

# Interview Scenario 2

### Question

> How would you audit Kubernetes RBAC?

### Answer

Review:

```text
Users
Groups
ServiceAccounts
Roles
RoleBindings
ClusterRoles
ClusterRoleBindings
```

Then identify:

```text
Wildcard Permissions
Cluster-Wide Access
Sensitive Resource Access
Unused Access
Privilege Escalation Paths
```

Finally:

```text
Document
 ↓
Remediate
 ↓
Retest
```

---

# Interview Scenario 3

### Question

> What Kubernetes audit level would you use?

### Answer

There is no universal answer.

I would choose based on:

```text
Security Requirements
Privacy
Storage
Performance
Incident Response
```

For many events, `Metadata` can provide useful visibility with lower data exposure.

More detailed levels may be appropriate for selected sensitive operations, but they can capture sensitive request or response data and increase storage requirements.

---

# Interview Scenario 4

### Question

> How would you implement compliance across 100 Kubernetes clusters?

### Answer

Use centralized automation:

```text
Clusters
   ↓
Policy as Code
   ↓
Central Compliance Engine
   ↓
Continuous Evaluation
   ↓
Findings
   ↓
Central Dashboard
   ↓
Remediation
```

Use:

```text
GitOps
Policy as Code
Central Logging
Central SIEM
Automated Evidence Collection
```

---

# Interview Scenario 5

### Question

> How do you prevent developers from deploying unapproved images?

### Answer

Use multiple layers:

```text
CI/CD
 ↓
Image Scan
 ↓
Signature Verification
 ↓
Admission Policy
 ↓
Kubernetes
```

The admission layer should reject images that violate the organization's policy.

---

# Interview Scenario 6

### Question

> How would you prove that an RBAC control is working?

### Answer

Do not simply show that a Role exists.

Test the control:

```text
Authorized Request → Allowed
Unauthorized Request → Denied
```

Then retain:

```text
Configuration
+
Test Evidence
+
Audit Logs
```

This demonstrates both implementation and operation.

---

# Interview Scenario 7

### Question

> What is the difference between a benchmark and a compliance requirement?

### Answer

A benchmark provides recommended security configurations.

A compliance requirement comes from:

```text
Law
Regulation
Contract
Standard
Internal Policy
```

A benchmark can support compliance but is not automatically equivalent to a legal or regulatory requirement.

---

# Interview Scenario 8

### Question

> How would you handle a compliance exception?

### Answer

Document:

```text
Requirement
 ↓
Reason for Exception
 ↓
Risk
 ↓
Compensating Control
 ↓
Owner
 ↓
Approval
 ↓
Expiration Date
```

Then review it periodically.

---

# Interview Scenario 9

### Question

> Why is continuous compliance important?

### Answer

Kubernetes is dynamic.

Resources can change:

```text
Every Minute
Every Deployment
Every Configuration Change
```

Therefore:

```text
Annual Audit
```

alone cannot guarantee ongoing compliance.

Continuous compliance detects:

```text
Drift
Policy Violations
New Vulnerabilities
Unauthorized Changes
```

---

# Interview Scenario 10

### Question

> Design a production Kubernetes compliance platform.

### Answer

```text
                  Kubernetes Clusters
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
          Cluster A    Cluster B    Cluster C
             │            │            │
             └────────────┼────────────┘
                          ▼
                    Policy as Code
                          │
              ┌───────────┼───────────┐
              ▼           ▼           ▼
            RBAC      Pod Security   Network
              │           │           │
              └───────────┼───────────┘
                          ▼
                  Compliance Engine
                          │
             ┌────────────┼────────────┐
             ▼            ▼            ▼
         Findings      Evidence       Logs
             │            │            │
             └────────────┼────────────┘
                          ▼
                    SIEM / Dashboard
                          │
                          ▼
                     SOC / GRC
                          │
                          ▼
                      Remediation
```

Important capabilities:

```text
Policy Enforcement
Continuous Scanning
Evidence Collection
Audit Logging
Configuration Drift Detection
Vulnerability Management
Reporting
Exception Management
```

---

# Production Compliance Checklist

```text
☑ Compliance scope documented
☑ Applicable requirements identified
☑ Security controls mapped
☑ RBAC reviewed
☑ Authentication controls reviewed
☑ Audit logging enabled
☑ Audit policy reviewed
☑ Audit retention defined
☑ Evidence storage protected
☑ Pod Security configured
☑ NetworkPolicies reviewed
☑ Secrets protected
☑ Images scanned
☑ Image provenance verified
☑ SBOM process implemented
☑ Vulnerability management implemented
☑ Patch management documented
☑ Configuration baseline established
☑ Configuration drift monitored
☑ Admission controls implemented
☑ Policy as Code version-controlled
☑ Continuous compliance enabled
☑ Compliance dashboard available
☑ Findings assigned
☑ Exceptions documented
☑ Risk acceptance documented
☑ Remediation tracked
☑ Backup controls validated
☑ Incident response tested
☑ Audit evidence retained
☑ Internal audits performed
☑ External audit readiness maintained
```

---

# Chapter Summary

Kubernetes compliance and auditing provide the governance and evidence layer around Kubernetes security.

The core lifecycle is:

```text
Requirements
 ↓
Controls
 ↓
Implementation
 ↓
Monitoring
 ↓
Evidence
 ↓
Audit
 ↓
Findings
 ↓
Remediation
 ↓
Continuous Improvement
```

Important Kubernetes compliance controls include:

```text
RBAC
+
Authentication
+
Audit Logging
+
Pod Security
+
Network Policies
+
Secret Management
+
Image Security
+
Vulnerability Management
+
Policy as Code
+
Continuous Monitoring
```

Important policy technologies include:

```text
OPA
Gatekeeper
Kyverno
```

Important security guidance can include:

```text
CIS Kubernetes Benchmark
NIST
ISO/IEC 27001
SOC 2
PCI DSS
HIPAA
GDPR
```

The exact requirements depend on the organization's scope, geography, industry, contracts, data, and applicable regulations.

The most important principle is:

> **Compliance is not a one-time checklist; build controls into Kubernetes, continuously monitor them, preserve trustworthy evidence, detect configuration drift, remediate findings, and continuously demonstrate that security controls are operating effectively.**

---

## Module 7 Complete

The following chapters covered:

```text
Chapter 46 – Kubernetes Security Fundamentals
Chapter 47 – Authentication
Chapter 48 – Authorization (RBAC)
Chapter 49 – Service Accounts
Chapter 50 – Admission Controllers
Chapter 51 – Pod Security Standards
Chapter 52 – Network Security
Chapter 53 – Secret Management
Chapter 54 – Image Security
Chapter 55 – Runtime Security
Chapter 56 – Supply Chain Security
```

---

## Next Module

# Module 8 — Kubernetes Observability

### Chapter 57 – Logging

Topics will include:

- Kubernetes Logging Fundamentals
- Why Logging Matters
- Container Logs
- Pod Logs
- Node Logs
- Application Logs
- System Logs
- Kubernetes Component Logs
- kubelet Logs
- API Server Logs
- Scheduler Logs
- Controller Manager Logs
- Container Runtime Logs
- Structured Logging
- JSON Logs
- Log Levels
- Log Rotation
- Log Retention
- Centralized Logging
- Log Aggregation
- Fluent Bit
- Fluentd
- Logstash
- Elasticsearch
- OpenSearch
- Loki
- Cloud Logging
- SIEM Integration
- Log Pipelines
- Log Parsing
- Log Enrichment
- Log Filtering
- Log Correlation
- Multiline Logs
- Sensitive Data
- Log Redaction
- Security Logging
- Audit Logging
- Compliance Logging
- Troubleshooting with Logs
- Production Logging Architecture
- Logging Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---