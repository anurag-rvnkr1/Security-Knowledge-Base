# Cloud Threat Hunting

## Overview

Cloud environments have fundamentally changed the way organizations build, operate, and secure infrastructure.

Traditional security models focused heavily on:

```text
Endpoint
   │
   ▼
Network
   │
   ▼
Server
```

Modern cloud environments introduce additional security boundaries:

```text
Identity
   │
   ├──► Cloud Control Plane
   │
   ├──► API
   │
   ├──► Compute
   │
   ├──► Storage
   │
   ├──► Database
   │
   ├──► Serverless
   │
   ├──► Containers
   │
   └──► Kubernetes
```

Cloud threat hunting therefore requires visibility into both:

- **Data plane activity** — interaction with cloud resources
- **Control plane activity** — changes to cloud configuration and management

A mature cloud-hunting program combines:

```text
Cloud Audit Logs
+
IAM
+
Network Telemetry
+
Endpoint Telemetry
+
Application Logs
+
Identity Provider
+
Container/Kubernetes Logs
+
Threat Intelligence
```

The central question is:

> **Who performed this cloud action, from where, using which identity, against which resource, and what changed afterward?**

---

# Why Cloud Threat Hunting Matters

Cloud attacks often abuse legitimate functionality.

An attacker may not need to deploy traditional malware.

Instead, they may:

```text
Steal Credentials
      │
      ▼
Authenticate to Cloud
      │
      ▼
Discover Resources
      │
      ▼
Escalate Privileges
      │
      ▼
Create Persistence
      │
      ▼
Access Sensitive Data
      │
      ▼
Exfiltrate
```

The attacker may use:

- Cloud APIs
- IAM roles
- Access keys
- Service principals
- OAuth applications
- Management consoles
- CLI tools
- Serverless functions
- Storage services
- Compute instances

This makes identity and control-plane telemetry extremely important.

---

# Shared Responsibility Model

Cloud security is based on a shared responsibility model.

Conceptually:

```text
             CLOUD SECURITY
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
   Provider              Customer
        │                     │
        │                     ├── Identity
        │                     ├── Data
        │                     ├── Configuration
        │                     ├── Applications
        │                     └── Access
        │
        ├── Physical Infrastructure
        ├── Core Platform
        └── Provider Services
```

The exact responsibility boundary depends on the service model.

Threat hunters must understand which telemetry is controlled by the organization.

---

# Cloud Threat-Hunting Architecture

```text
                         CLOUD ENVIRONMENT
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
        AWS                   Azure                  GCP
          │                     │                     │
          ▼                     ▼                     ▼
      Audit Logs            Activity Logs          Audit Logs
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                         Central Log Platform
                                │
             ┌──────────────────┼──────────────────┐
             ▼                  ▼                  ▼
           SIEM               XDR                Data Lake
             │                  │                  │
             └──────────────────┼──────────────────┘
                                ▼
                           Threat Hunting
                                │
                ┌───────────────┼───────────────┐
                ▼               ▼               ▼
              IAM            Network          Workload
```

---

# Cloud Telemetry Categories

| Category | Examples |
|---|---|
| Control Plane | IAM changes, resource creation |
| Data Plane | Object access, database queries |
| Identity | Login, token, role assumption |
| Network | Flow logs, load balancers |
| Compute | VM process and system activity |
| Storage | Object access |
| Serverless | Function invocation |
| Containers | Runtime events |
| Kubernetes | API audit logs |
| Application | API/application logs |

---

# Control Plane vs Data Plane

## Control Plane

Management actions:

```text
CreateUser
CreateRole
ModifyFirewall
CreateInstance
DeleteBucket
ChangePolicy
```

## Data Plane

Resource usage:

```text
ReadObject
WriteObject
QueryDatabase
InvokeFunction
AccessSecret
```

A compromise may involve both.

Example:

```text
Control Plane
     │
     ▼
New Access Policy
     │
     ▼
Data Plane
     │
     ▼
Sensitive Object Access
```

---

# Cloud Threat-Hunting Workflow

```text
Cloud Event
    │
    ▼
Identify Principal
    │
    ▼
Identify Source
    │
    ▼
Identify Action
    │
    ▼
Identify Resource
    │
    ▼
Compare Baseline
    │
    ▼
Correlate Related Events
    │
    ▼
Assess Risk
    │
    ▼
Scope
    │
    ▼
Respond
```

---

# AWS Threat Hunting

AWS provides extensive telemetry through services such as:

- CloudTrail
- VPC Flow Logs
- CloudWatch
- GuardDuty
- IAM
- S3 access logging / CloudTrail data events
- Load balancer logs
- EKS audit and workload telemetry

The exact telemetry depends on the services deployed.

---

# AWS CloudTrail

CloudTrail records AWS API activity.

A simplified event contains:

```text
Timestamp
User Identity
Event Name
Source IP
User Agent
AWS Region
Resource
Result
```

Example conceptual event:

```json
{
  "eventName": "CreateUser",
  "sourceIPAddress": "203.0.113.10",
  "awsRegion": "ap-south-1"
}
```

The actual event structure is richer and should be analyzed according to the deployed CloudTrail configuration.

---

# AWS Identity Types

CloudTrail may contain identities such as:

```text
IAM User
IAM Role
Assumed Role
Federated User
AWS Service
Root Account
```

Understanding the principal is critical.

---

# AWS Root Account Hunting

Root account activity should receive special attention because the root identity has exceptional privileges.

Monitor:

```text
Root Authentication
Root API Activity
Credential Changes
MFA Changes
Billing Changes
Security Configuration Changes
```

Unexpected root activity should be investigated immediately.

---

# AWS ConsoleLogin

Console authentication events can reveal:

```text
Identity
Source IP
User Agent
MFA
Time
```

Hunt for:

```text
New Location
New Device
Unusual Time
Unexpected User Agent
```

---

# AWS Access Key Hunting

Access keys may provide programmatic access.

Potentially suspicious sequence:

```text
CreateAccessKey
      │
      ▼
Unusual Source IP
      │
      ▼
API Calls
      │
      ▼
Privilege Escalation
      │
      ▼
Data Access
```

Investigate:

```text
Who created the key?
Which identity owns it?
Why was it created?
Where was it used?
What APIs were called?
```

---

# AWS AssumeRole Hunting

Role assumption is normal in many cloud architectures.

A suspicious pattern may involve:

```text
Identity A
   │
   ▼
AssumeRole
   │
   ▼
High-Privilege Role
   │
   ▼
Sensitive API Calls
```

Important context includes:

- Source identity
- Target role
- Source IP
- Session name
- Time
- Historical behavior

---

# AWS IAM Policy Changes

Monitor:

```text
AttachUserPolicy
AttachRolePolicy
PutUserPolicy
PutRolePolicy
CreatePolicy
CreatePolicyVersion
SetDefaultPolicyVersion
```

Potentially suspicious sequence:

```text
Low-Privilege Identity
       │
       ▼
Policy Modification
       │
       ▼
Administrative Permission
       │
       ▼
Sensitive Resource Access
```

---

# AWS IAM Persistence

Attackers may create persistence through:

- New users
- Access keys
- Roles
- Policy modifications
- Trust-policy changes
- Federation configuration

A useful hunting model:

```text
IAM Change
    │
    ├── Identity
    ├── Permission
    ├── Credential
    └── Trust Relationship
```

---

# IAM Trust Policy Hunting

Role trust policies determine who or what can assume a role.

Unexpected trust relationships can create persistence.

Investigate:

```text
Role
 │
 ▼
Trust Policy Change
 │
 ▼
New Principal
 │
 ▼
AssumeRole
```

---

# AWS S3 Hunting

S3 is frequently used to store sensitive information.

Important events can include:

```text
GetObject
PutObject
DeleteObject
ListBucket
GetBucketPolicy
PutBucketPolicy
```

Potential anomalies:

```text
User
 │
 ▼
Rare Bucket
 │
 ▼
Large GetObject Activity
 │
 ▼
External Source
```

---

# S3 Data Access

Data-plane monitoring can help identify unusual access.

Example:

```text
Normal:
Application Role → Application Bucket

Observed:
Developer Identity → Production Data Bucket
```

The behavior requires investigation.

---

# S3 Public Exposure

Monitor configuration changes involving:

- Bucket policies
- Access controls
- Public access settings
- Cross-account access

Potential sequence:

```text
Bucket Configuration Change
          │
          ▼
Public / External Access
          │
          ▼
Object Retrieval
```

---

# AWS EC2 Hunting

EC2 investigations may combine:

```text
CloudTrail
+
VPC Flow Logs
+
Instance Metadata
+
EDR
+
OS Logs
```

Example:

```text
New Instance
    │
    ▼
New IAM Role
    │
    ▼
Outbound Connection
    │
    ▼
Suspicious Process
```

---

# EC2 Metadata Service

Cloud workloads may access instance metadata.

A commonly known metadata endpoint is:

```text
http://169.254.169.254/
```

Modern AWS deployments can require IMDSv2, which uses session-oriented requests.

From a hunting perspective, investigate unexpected metadata access.

Potential signal:

```text
Application
    │
    ▼
Metadata Service
    │
    ▼
Credential Retrieval
    │
    ▼
AWS API Activity
```

---

# Metadata Hunting

Correlate:

```text
Metadata Access
+
Process
+
User
+
IAM Role
+
Subsequent API Calls
```

Do not treat every metadata request as malicious.

Cloud agents and legitimate software may access metadata.

---

# AWS Lambda Hunting

Serverless workloads introduce a different security model.

Monitor:

- Function invocation
- Function configuration
- Environment variables
- IAM role changes
- Function code changes
- Unexpected network communication

Potential attack path:

```text
Compromised Identity
      │
      ▼
Modify Lambda
      │
      ▼
Execution
      │
      ▼
Sensitive Resource Access
```

---

# AWS Secrets Hunting

Monitor access to:

- Secrets Manager
- Parameter Store
- KMS
- Application credentials

Potentially suspicious:

```text
Rare Identity
     │
     ▼
Secret Access
     │
     ▼
API Calls
     │
     ▼
External Network
```

---

# Azure Threat Hunting

Azure environments provide telemetry through services such as:

- Microsoft Entra sign-in logs
- Entra audit logs
- Azure Activity Logs
- Resource logs
- Azure Monitor
- Microsoft Defender for Cloud
- Microsoft Defender XDR
- Storage logs
- Key Vault logs

---

# Azure Activity Log

Activity logs can provide visibility into management-plane operations.

Examples include:

```text
Resource Creation
Role Assignment
Policy Changes
Network Changes
VM Operations
Key Vault Configuration
```

---

# Azure Role Assignment Hunting

Potentially suspicious:

```text
User
 │
 ▼
Role Assignment
 │
 ▼
High Privilege
 │
 ▼
Resource Access
```

Investigate:

```text
Who assigned it?
To whom?
Which role?
At what time?
Why?
What happened afterward?
```

---

# Azure Service Principal Hunting

Service principals may be used for automation.

Monitor:

```text
Application Registration
Credential Addition
Permission Grant
Role Assignment
Authentication
```

Potential persistence:

```text
Application
    │
    ▼
New Credential
    │
    ▼
Service Principal Login
    │
    ▼
Cloud API Access
```

---

# Azure Key Vault Hunting

Key Vault access can be highly sensitive.

Investigate:

```text
Identity
   │
   ▼
Secret Access
   │
   ▼
Rare Application
   │
   ▼
External Activity
```

---

# Azure Storage Hunting

Monitor:

- Blob access
- Container configuration
- Public access
- SAS token usage
- Unusual download activity

Potential sequence:

```text
Storage Configuration Change
        │
        ▼
External Access
        │
        ▼
Large Data Download
```

---

# Azure VM Hunting

Combine:

```text
Azure Activity
+
VM Logs
+
EDR
+
Network Flow
```

This allows:

```text
Cloud Identity
   │
   ▼
VM
   │
   ▼
Process
   │
   ▼
Network
```

---

# GCP Threat Hunting

Google Cloud provides telemetry through:

- Cloud Audit Logs
- IAM
- VPC Flow Logs
- Firewall Logs
- Cloud Storage logs
- GKE audit logs
- Cloud Run telemetry
- Compute Engine logs

---

# GCP Audit Logs

Audit logs can reveal:

```text
Identity
Method
Resource
Source
Timestamp
Result
```

Example conceptual activity:

```text
Principal
   │
   ▼
SetIamPolicy
   │
   ▼
Project
```

IAM policy changes deserve close monitoring.

---

# GCP IAM Hunting

Monitor:

```text
Grant Role
Remove Role
Create Service Account
Create Key
Set IAM Policy
```

Potential sequence:

```text
Compromised Identity
      │
      ▼
IAM Modification
      │
      ▼
Service Account
      │
      ▼
Long-Term Access
```

---

# GCP Service Account Keys

Service account keys can provide programmatic access.

Investigate:

```text
New Key
   │
   ▼
Unexpected Source
   │
   ▼
API Calls
```

Determine:

```text
Who created it?
Why?
Who used it?
Where?
What resources were accessed?
```

---

# Cloud Credential Hunting

Cloud credentials can exist as:

```text
Passwords
Access Keys
Service Account Keys
OAuth Tokens
Session Tokens
API Keys
Workload Identity
Managed Identity
```

Threat hunting must account for each.

---

# Credential Lifecycle

```text
Credential Created
      │
      ▼
Credential Used
      │
      ▼
Credential Rotated
      │
      ▼
Credential Revoked
```

Hunt for credentials that:

- Were created unexpectedly
- Have unusual usage
- Are used from unusual locations
- Remain active after expected expiration

---

# Cloud Privilege Escalation

Cloud privilege escalation can occur through:

```text
Identity
   │
   ├──► IAM Policy
   ├──► Role
   ├──► Trust Policy
   ├──► Service Account
   ├──► Function
   └──► Resource Policy
```

Example:

```text
User
 │
 ▼
Modify IAM
 │
 ▼
Assume Admin Role
 │
 ▼
Access Secrets
```

---

# Cloud Persistence

Cloud persistence can involve:

- New IAM users
- New access keys
- Service accounts
- Role trust changes
- OAuth applications
- API keys
- Lambda/function modifications
- Scheduled cloud jobs
- CI/CD credentials
- Resource policies

A useful hunt:

```text
Configuration Change
       │
       ▼
New Identity / Credential
       │
       ▼
Authentication
       │
       ▼
Resource Access
```

---

# Cloud Discovery

Attackers may enumerate:

```text
Accounts
Roles
Policies
Buckets
Instances
Networks
Security Groups
Functions
Secrets
Projects
Subscriptions
```

A sudden spike in API enumeration from an identity can be suspicious.

---

# API Enumeration Hunting

Example:

```text
Identity
 │
 ├── ListBuckets
 ├── DescribeInstances
 ├── ListRoles
 ├── ListUsers
 ├── DescribeNetworks
 └── ListFunctions
```

This may represent cloud reconnaissance.

But infrastructure automation can produce similar behavior.

---

# Cloud Network Hunting

Important sources include:

- VPC Flow Logs
- NSG flow logs
- Firewall logs
- Load balancer logs
- NAT logs

Investigate:

```text
Workload
   │
   ▼
Destination
   │
   ▼
Port
   │
   ▼
Protocol
   │
   ▼
Frequency
```

---

# Cloud Egress Hunting

A compromised workload may communicate with unusual external infrastructure.

Potential signals:

```text
New Workload
+
New External Destination
+
Rare Port
+
High Outbound Volume
```

Correlate with workload identity and process telemetry.

---

# Cloud Storage Exfiltration

A possible sequence:

```text
Identity Compromise
      │
      ▼
Storage Discovery
      │
      ▼
Sensitive Object Access
      │
      ▼
Large Data Retrieval
      │
      ▼
External Transfer
```

This should be reconstructed through control-plane and data-plane telemetry.

---

# Cloud-Native Attack Chain

Example:

```text
Phished User
     │
     ▼
Cloud Login
     │
     ▼
OAuth Consent
     │
     ▼
API Enumeration
     │
     ▼
IAM Change
     │
     ▼
Sensitive Storage
     │
     ▼
Data Access
```

No traditional endpoint malware is necessarily required.

---

# Serverless Threat Hunting

Serverless platforms include:

- AWS Lambda
- Azure Functions
- Google Cloud Functions
- Cloud Run-style workloads

Hunt for:

```text
Function Created
Function Modified
Permission Changed
Credential Changed
Unexpected Invocation
Unexpected Destination
```

---

# Serverless Persistence

An attacker may modify:

```text
Function Code
Environment Variables
IAM Role
Trigger
Event Source
```

Conceptually:

```text
Function
   │
   ├── Code
   ├── Role
   ├── Trigger
   └── Environment
```

Changes to any of these may alter security behavior.

---

# Container Threat Hunting

Cloud workloads increasingly run in containers.

Useful telemetry:

```text
Container
Image
Registry
Process
Network
Identity
Kubernetes
Runtime
```

Potential sequence:

```text
Container
   │
   ▼
Unexpected Process
   │
   ▼
Metadata Access
   │
   ▼
Cloud Credential
   │
   ▼
Cloud API
```

---

# Container Image Hunting

Monitor:

- Image source
- Registry
- Digest
- First seen
- Deployment
- Vulnerability state

Unexpected image deployments can be investigated through:

```text
Image
 ↓
Deployment
 ↓
Identity
 ↓
Workload
 ↓
Network
```

---

# Kubernetes Threat Hunting

Kubernetes introduces additional identity and control-plane telemetry.

Important sources include:

- Kubernetes API audit logs
- Admission logs
- Container runtime logs
- Kubernetes events
- Network telemetry
- Cloud IAM
- Container security telemetry

---

# Kubernetes API Hunting

Monitor actions such as:

```text
Create Pod
Exec
Create Secret
Create ServiceAccount
Create Role
Create RoleBinding
Create ClusterRoleBinding
```

A potentially suspicious sequence:

```text
User
 │
 ▼
Create ServiceAccount
 │
 ▼
Create RoleBinding
 │
 ▼
Create Pod
 │
 ▼
Privileged Access
```

---

# Kubernetes Exec Hunting

`exec` operations allow users or automation to execute commands within containers.

Investigate:

```text
Who
Which Pod
Which Namespace
Which Container
What Time
What Followed
```

An unexpected interactive container session deserves review.

---

# Kubernetes Secrets

Secrets can contain:

- Credentials
- API keys
- Certificates
- Tokens

Monitor:

```text
Secret Created
Secret Modified
Secret Access
Unexpected Identity
```

---

# Cloud CI/CD Hunting

CI/CD pipelines can hold powerful credentials.

Monitor:

```text
Pipeline
 │
 ▼
Credential
 │
 ▼
Build
 │
 ▼
Cloud API
 │
 ▼
Deployment
```

Suspicious signals include:

- New pipeline
- Changed build configuration
- New deployment identity
- Unusual repository
- Unusual deployment time
- Unexpected production deployment

---

# Cloud Supply Chain

Cloud environments depend on:

```text
Source Code
   │
   ▼
Build System
   │
   ▼
Container / Artifact
   │
   ▼
Registry
   │
   ▼
Deployment
   │
   ▼
Production
```

A compromise anywhere in this chain can affect cloud infrastructure.

---

# Cloud Control Plane Hunting

Control-plane actions can often be categorized:

```text
Identity Changes
Resource Changes
Network Changes
Security Changes
Storage Changes
Compute Changes
Application Changes
```

A good hunt focuses on high-impact administrative actions.

---

# Cloud Configuration Drift

Compare:

```text
Expected Configuration
        │
        ▼
Actual Configuration
        │
        ▼
Difference
        │
        ▼
Investigation
```

Examples:

```text
Firewall Rule
IAM Policy
Storage Exposure
Security Group
Role Assignment
Logging
```

---

# Cloud Logging Tampering

Attackers may attempt to reduce visibility.

Monitor changes involving:

```text
Audit Logging
Log Destinations
Retention
Monitoring
Alerting
Security Services
```

Potential sequence:

```text
Attacker
   │
   ▼
Disable / Modify Logging
   │
   ▼
Sensitive Activity
```

---

# Cloud Detection Evasion

Possible attacker behaviors include:

- Using legitimate APIs
- Rotating credentials
- Using temporary credentials
- Using compromised service accounts
- Using trusted cloud infrastructure
- Operating through automation systems

Therefore cloud hunting must focus heavily on behavior and identity context.

---

# Cloud Threat Intelligence

Cloud infrastructure can be enriched using:

```text
IP Reputation
Domain Reputation
ASN
Cloud Provider
Account
Resource
Certificate
Threat Intelligence
```

But cloud provider IP ranges are shared and dynamic.

Infrastructure reputation must therefore be interpreted carefully.

---

# Cloud Asset Context

Every cloud event should ideally map to:

```text
Account / Subscription / Project
        │
        ▼
Resource
        │
        ▼
Owner
        │
        ▼
Environment
        │
        ▼
Business Criticality
```

A production database and a development VM should not have identical risk priorities.

---

# Production vs Development

A useful classification:

```text
Production
   │
   ├── Critical
   ├── Sensitive
   └── High Monitoring

Development
   │
   ├── Lower Criticality
   └── Different Baseline
```

Threat hunters should understand environment context before prioritizing events.

---

# Cloud Risk-Based Hunting

Prioritize:

```text
High-Privilege Identity
        +
Sensitive Resource
        +
Unusual Behavior
```

Example:

```text
Administrator
+
New Location
+
Production Database
```

is significantly more concerning than:

```text
Developer
+
Known Development Resource
+
Expected Location
```

---

# Cloud Query Engineering

A normalized cloud event should support queries such as:

```text
Principal
Action
Resource
Source
Timestamp
Result
Environment
```

Then hunters can ask:

```text
Which identities performed unusual actions?

Which resources experienced unusual access?

Which source IPs performed high-risk actions?

Which identities changed their own permissions?
```

---

# Example CloudTrail Hunt

Conceptual Splunk-style query:

```spl id="m1b8y6"
index=aws_cloudtrail
| stats
    count as events
    dc(eventName) as unique_actions
    by userIdentity.arn, sourceIPAddress
| sort -events
```

Use environment-specific field mappings.

---

# IAM Change Hunt

```spl id="i6r2r5"
index=aws_cloudtrail
eventName IN (
    "AttachUserPolicy",
    "AttachRolePolicy",
    "PutUserPolicy",
    "PutRolePolicy",
    "CreateAccessKey",
    "CreateUser",
    "CreateRole"
)
| table _time,
        userIdentity.arn,
        eventName,
        sourceIPAddress,
        awsRegion
```

---

# Azure Identity Hunt

Conceptually:

```kusto id="c4cdb9"
SigninLogs
| summarize
    Attempts = count(),
    Locations = dcount(Location),
    IPs = dcount(IPAddress)
    by UserPrincipalName
| order by Attempts desc
```

The exact schema depends on the tenant and telemetry configuration.

---

# GCP IAM Hunt

Conceptually:

```text
Audit Log
    │
    ▼
IAM Policy Change
    │
    ├── Principal
    ├── Resource
    ├── Role
    └── Source
```

Prioritize unexpected high-privilege changes.

---

# Practical Lab 1 — AWS IAM Persistence

## Objective

Identify suspicious cloud persistence.

Search for:

```text
CreateUser
CreateAccessKey
CreateRole
AttachPolicy
PutPolicy
TrustPolicy Change
```

Build:

```text
Identity
   │
   ▼
IAM Change
   │
   ▼
New Credential
   │
   ▼
API Activity
```

---

# Practical Lab 2 — AWS Sensitive Storage Access

## Objective

Identify unusual S3 access.

Investigate:

```text
Identity
Bucket
Object
Source IP
Operation
Volume
Time
```

Compare with historical behavior.

---

# Practical Lab 3 — Cloud Credential Anomaly

Hypothesis:

> A credential is being used outside its expected environment.

Search:

```text
Credential
+
New IP
+
New Location
+
New API Pattern
```

Then identify whether the credential should be rotated or revoked according to incident-response procedures.

---

# Practical Lab 4 — Azure Privilege Escalation

Search for:

```text
Role Assignment
+
New Principal
+
High Privilege
```

Then correlate:

```text
Identity
Source
Resource
Subsequent API Calls
```

---

# Practical Lab 5 — GCP IAM Abuse

Search for:

```text
SetIamPolicy
CreateServiceAccount
CreateServiceAccountKey
```

Investigate:

```text
Actor
Source
Target
Role
Time
Subsequent API Activity
```

---

# Practical Lab 6 — Cloud Storage Exfiltration

Hypothesis:

> A compromised identity is accessing unusually large amounts of cloud storage.

Workflow:

```text
Identity
 │
 ▼
Object Enumeration
 │
 ▼
Object Retrieval
 │
 ▼
Large Volume
 │
 ▼
External Destination
```

Correlate data-plane and network telemetry.

---

# Practical Lab 7 — Kubernetes Privilege Escalation

Search for:

```text
CreateRole
CreateRoleBinding
CreateClusterRoleBinding
CreateServiceAccount
Exec
```

Investigate the identity and namespace.

---

# Practical Lab 8 — Cloud Logging Tampering

Search for:

```text
Logging Configuration Change
+
High-Privilege Identity
```

Then examine activity immediately before and after the change.

---

# Practical Lab 9 — Cloud API Enumeration

Identify identities generating unusually broad discovery activity:

```text
List*
Describe*
Get*
Enumerate*
```

Then compare against:

```text
Historical Behavior
Role
Application
Automation
```

---

# Practical Lab 10 — Multi-Cloud Identity Correlation

A user may access:

```text
Entra ID
   │
   ├──► Azure
   │
   ├──► AWS
   │
   └──► SaaS
```

Build a unified identity timeline across platforms.

---

# Cloud Incident Timeline

Example:

```text
08:12
User authenticates

08:14
New cloud API source observed

08:15
IAM enumeration

08:17
New access key created

08:18
Administrative role assumed

08:21
Storage enumeration

08:25
Large object downloads

08:29
Logging configuration modified
```

This sequence is highly valuable during investigation.

---

# Cloud Detection Engineering

A mature pipeline:

```text
Cloud Telemetry
      │
      ▼
Normalization
      │
      ▼
Identity Resolution
      │
      ▼
Asset Context
      │
      ▼
Baseline
      │
      ▼
Behavioral Detection
      │
      ▼
Risk Scoring
      │
      ▼
SIEM / XDR
      │
      ▼
SOC
```

---

# Example Detection — IAM Privilege Escalation

```text
IF

Identity modifies its own permissions

AND

New permission grants administrative access

AND

Activity is outside normal administrative workflow

THEN

Generate high-priority investigation
```

---

# Example Detection — New Credential

```text
IF

New cloud credential created

AND

Creator is not normally responsible for credential management

AND

Credential is used shortly afterward

AND

Source is unusual

THEN

Generate credential-abuse signal
```

---

# Example Detection — Sensitive Storage Access

```text
IF

Identity has no historical access to sensitive storage

AND

Begins high-volume object retrieval

AND

Source is unusual

THEN

Generate data-access investigation
```

---

# Example Detection — Logging Tampering

```text
IF

Audit logging configuration changes

AND

Actor is not an approved logging administrator

OR

Change occurs immediately before high-risk API activity

THEN

Generate high-priority alert
```

---

# Cloud False Positives

Common legitimate causes include:

- Infrastructure-as-Code
- CI/CD
- Auto-scaling
- Cloud migrations
- Security scanners
- Backup systems
- Monitoring
- Deployment automation
- Managed services

Therefore, establish automation identities and expected behavior.

---

# Infrastructure-as-Code Considerations

Tools such as Terraform and CloudFormation-style systems may produce large numbers of changes.

A detection must distinguish:

```text
Approved Automation
```

from:

```text
Unexpected Manual Change
```

Useful context:

```text
Pipeline
Repository
Commit
Identity
Change Window
Resource
```

---

# Cloud Asset Inventory

A hunting program should maintain visibility into:

```text
Accounts
Projects
Subscriptions
Regions
Resources
Owners
Tags
Environment
Criticality
```

Without asset context, cloud hunting becomes significantly harder.

---

# Cloud Threat-Hunting Checklist

## Identity

- [ ] User logins
- [ ] Service identities
- [ ] Access keys
- [ ] API tokens
- [ ] OAuth applications
- [ ] Role assumptions
- [ ] Privilege changes

## Control Plane

- [ ] IAM changes
- [ ] Resource creation
- [ ] Network changes
- [ ] Security changes
- [ ] Logging changes
- [ ] Policy changes

## Data Plane

- [ ] Storage access
- [ ] Database access
- [ ] Secret access
- [ ] Function invocation
- [ ] API calls

## Network

- [ ] Flow logs
- [ ] External destinations
- [ ] Egress
- [ ] Unusual ports
- [ ] C2 behavior

## Workloads

- [ ] VM
- [ ] Container
- [ ] Kubernetes
- [ ] Serverless
- [ ] Application

## Response

- [ ] Revoke credentials
- [ ] Disable compromised identity
- [ ] Revoke sessions
- [ ] Remove unauthorized roles
- [ ] Remove persistence
- [ ] Isolate workloads
- [ ] Preserve evidence

---

# Common Cloud Hunting Mistakes

## 1. Monitoring Only Login Events

API activity after login can be much more informative.

---

## 2. Ignoring Service Identities

Service accounts and roles can have extremely broad permissions.

---

## 3. Ignoring Data-Plane Events

Control-plane logs alone may not reveal data theft.

---

## 4. Ignoring Logging Configuration

Attackers may attempt to reduce visibility.

---

## 5. Treating Cloud Provider IPs as Automatically Trusted

Cloud infrastructure is shared and dynamic.

---

## 6. Ignoring Automation

CI/CD and Infrastructure-as-Code can produce large amounts of legitimate activity.

---

## 7. Ignoring Cross-Cloud Activity

Attackers may move between:

```text
Identity Provider
→ SaaS
→ AWS
→ Azure
→ GCP
```

---

# Professional Cloud Investigation Template

```text
Incident ID:

Date/Time:

Cloud Provider:

Account / Subscription / Project:

Identity:

Identity Type:

Source IP:

Source Location:

Device:

Authentication Method:

MFA:

Action:

Resource:

Region:

Environment:

Privilege:

API Calls:

Network Activity:

Data Access:

Credential Changes:

IAM Changes:

Logging Changes:

Related Identities:

Related Resources:

First Seen:

Last Seen:

MITRE ATT&CK:

Timeline:

Assessment:

Containment:

Credential Revocation:

Persistence Removal:

Remediation:

Detection Improvement:

Lessons Learned:
```

---

# Cloud MITRE ATT&CK Mapping

Relevant techniques include:

| Technique | Description |
|---|---|
| T1078.004 | Valid Accounts: Cloud Accounts |
| T1098.001 | Additional Cloud Roles |
| T1136.003 | Create Account: Cloud Account |
| T1528 | Steal Application Access Token |
| T1552.001 | Credentials In Files |
| T1530 | Data from Cloud Storage |
| T1613 | Container Service |
| T1609 | Container Administration Command |
| T1610 | Deploy Container |
| T1526 | Cloud Service Dashboard |
| T1580 | Cloud Infrastructure Discovery |
| T1619 | Cloud Storage Object Discovery |
| T1538 | Cloud Service Dashboard |
| T1562.007 | Disable or Modify Cloud Firewall |
| T1562.008 | Disable or Modify Cloud Logs |
| T1537 | Transfer Data to Cloud Account |

ATT&CK mappings should be validated against the current ATT&CK knowledge base when converting this material into production detections.

---

# Interview Questions

## 1. What makes cloud threat hunting different from traditional threat hunting?

Cloud hunting requires visibility into identities, control-plane APIs, data-plane activity, cloud resources, workloads, and dynamically changing infrastructure.

---

## 2. What is the cloud control plane?

The control plane manages cloud resources and configuration through management APIs.

---

## 3. What is the data plane?

The data plane represents interaction with the actual cloud resources and their data.

---

## 4. Why is CloudTrail important?

CloudTrail provides AWS API activity that can help investigate identities, actions, resources, source IPs, and control-plane behavior.

---

## 5. How would you hunt for AWS IAM abuse?

I would monitor:

```text
Users
Roles
Policies
Access Keys
Trust Policies
Role Assumption
```

and correlate them with source, identity, and subsequent API activity.

---

## 6. What is cloud persistence?

Cloud persistence is maintaining unauthorized access through mechanisms such as accounts, credentials, roles, OAuth applications, service identities, policies, or workload modifications.

---

## 7. How would you investigate an unexpected access key?

I would identify:

```text
Creator
Owner
Creation Time
Source
Usage
API Calls
Resources Accessed
```

and determine whether the credential is legitimate.

---

## 8. How would you hunt for cloud data exfiltration?

I would correlate:

```text
Identity
+
Storage Enumeration
+
Object Access
+
Volume
+
Destination
+
Network
```

---

## 9. Why are service accounts dangerous?

They can have broad permissions, long-lived credentials, and automated access that may be less visible than human activity.

---

## 10. How would you detect cloud privilege escalation?

Monitor changes to:

```text
IAM Policies
Roles
Role Bindings
Trust Policies
Service Accounts
Application Permissions
```

and correlate those changes with subsequent privileged activity.

---

## 11. What is cloud control-plane logging?

It is telemetry describing management operations such as creating resources, modifying IAM, changing security settings, and altering infrastructure configuration.

---

## 12. Why should cloud logging changes be monitored?

Attackers may attempt to disable or modify logging to reduce visibility into subsequent activity.

---

## 13. How would you hunt Kubernetes privilege escalation?

I would investigate:

```text
Role
RoleBinding
ClusterRole
ClusterRoleBinding
ServiceAccount
Pod
Exec
```

changes and correlate them with the responsible identity.

---

## 14. What is the importance of cloud asset context?

It tells the hunter what the affected resource is, who owns it, how critical it is, and whether the observed activity is normal.

---

## 15. What is the most important principle of cloud threat hunting?

> **Treat cloud APIs and identities as security telemetry, not merely infrastructure operations.**

---

# Key Takeaways

1. **Cloud security is heavily identity-centric.**
2. **Control-plane activity can reveal attacker persistence and privilege escalation.**
3. **Data-plane activity is essential for detecting data access and exfiltration.**
4. **AWS CloudTrail, Azure activity/audit telemetry, and GCP audit logs are foundational hunting sources.**
5. **IAM changes deserve close monitoring.**
6. **Access keys, service accounts, roles, and tokens can provide attacker persistence.**
7. **Cloud metadata services can become credential-access paths and should be monitored appropriately.**
8. **Serverless, containers, and Kubernetes introduce additional hunting surfaces.**
9. **Cloud logging tampering is itself a high-value hunting signal.**
10. **Infrastructure-as-Code and CI/CD must be incorporated into behavioral baselines.**
11. **Cloud storage access should be correlated with identity and network activity.**
12. **Cross-cloud identity activity should be investigated as one identity story.**
13. **Cloud provider infrastructure should not automatically be considered trusted.**
14. **Asset criticality is essential for prioritizing cloud investigations.**
15. **Cloud threat hunting should continuously feed cloud-native detection engineering.**

The core mindset is:

> **Don't ask only "Who logged into the cloud?" Ask "Which identity performed which action against which resource, from where, using what credentials, what changed afterward, and what data or privileges became accessible?"**

---

# References

- MITRE ATT&CK — Cloud Matrix  
  https://attack.mitre.org/matrices/enterprise/cloud/

- AWS CloudTrail Documentation  
  https://docs.aws.amazon.com/awscloudtrail/

- AWS IAM Documentation  
  https://docs.aws.amazon.com/iam/

- AWS VPC Flow Logs  
  https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html

- AWS S3 Security Documentation  
  https://docs.aws.amazon.com/AmazonS3/latest/userguide/security.html

- AWS EC2 Instance Metadata Documentation  
  https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-metadata.html

- Microsoft Azure Activity Log  
  https://learn.microsoft.com/azure/azure-monitor/essentials/activity-log

- Microsoft Entra Documentation  
  https://learn.microsoft.com/entra/

- Microsoft Defender for Cloud  
  https://learn.microsoft.com/azure/defender-for-cloud/

- Google Cloud Audit Logs  
  https://cloud.google.com/logging/docs/audit

- Google Cloud IAM  
  https://cloud.google.com/iam/docs

- Google Cloud VPC Flow Logs  
  https://cloud.google.com/vpc/docs/flow-logs

- Kubernetes Auditing  
  https://kubernetes.io/docs/tasks/debug/debug-cluster/audit/

- Kubernetes Security  
  https://kubernetes.io/docs/concepts/security/

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

- CISA Cloud Security Resources  
  https://www.cisa.gov/topics/cloud-security
