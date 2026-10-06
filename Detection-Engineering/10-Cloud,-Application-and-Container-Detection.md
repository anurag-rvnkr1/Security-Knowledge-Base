# Chapter 10 – Cloud, Application & Container Detection

> Modern applications increasingly run across public cloud platforms, APIs, containers, Kubernetes clusters, serverless services, SaaS platforms, and distributed infrastructure. Detection engineering must therefore move beyond traditional endpoint and network telemetry and understand cloud control planes, application behavior, container runtime activity, identities, APIs, and workload relationships.

---

# 1. Introduction

Traditional security monitoring often focuses on:

```text
Endpoint
Network
Identity
```

Modern environments add:

```text
Cloud
Application
API
Container
Kubernetes
Serverless
SaaS
CI/CD
Infrastructure-as-Code
```

A modern attack may look like:

```text
Compromised Identity
        ↓
Cloud API Access
        ↓
Privilege Modification
        ↓
Container Deployment
        ↓
Application Access
        ↓
Data Access
        ↓
Exfiltration
```

Therefore, modern detection engineering must understand both:

```text
Infrastructure Behavior
```

and:

```text
Application Behavior
```

---

# 2. Cloud Detection Engineering

Cloud detection focuses on activity across:

```text
Identity
Control Plane
Compute
Storage
Network
Applications
Containers
Serverless
Secrets
Configuration
```

---

# 3. Cloud Shared Responsibility

Cloud security is divided between:

```text
Cloud Provider
        +
Customer
```

The provider typically manages parts of:

```text
Physical Infrastructure
Underlying Cloud Platform
```

The customer remains responsible for areas such as:

```text
Identity
Configuration
Data
Applications
Access Policies
Workloads
Secrets
```

The exact responsibility depends on the service model.

---

# 4. Cloud Control Plane

The cloud control plane records administrative operations such as:

```text
Create Resource
Delete Resource
Modify IAM
Create Access Key
Change Security Group
Modify Storage Policy
Create Snapshot
Change Network Configuration
```

Control-plane logs are therefore extremely valuable for detection.

---

# 5. Cloud Audit Logs

Common information:

```text
Actor
Action
Resource
Source IP
Timestamp
Region
Authentication Method
Result
User Agent
```

A useful detection question is:

```text
Who changed what?
From where?
When?
Using which identity?
```

---

# 6. Cloud Identity Detection

Cloud identities include:

```text
Human Users
Service Accounts
Roles
Workload Identities
Access Keys
Temporary Credentials
Federated Identities
```

---

# 7. Cloud Account Takeover

Possible sequence:

```text
Unusual Login
      ↓
New Device
      ↓
New Region
      ↓
Credential / Key Creation
      ↓
Privilege Change
      ↓
Sensitive API Calls
```

This should be treated as a behavioral chain rather than independent alerts.

---

# 8. Cloud Privilege Escalation

Potential signals:

```text
Role Assignment
Policy Modification
Permission Grant
Trust Relationship Change
Administrative Role Activation
```

Example:

```text
Normal User
      ↓
New Administrative Role
      ↓
Sensitive Resource Access
```

---

# 9. IAM Policy Changes

Monitor:

```text
Policy Created
Policy Modified
Policy Attached
Policy Detached
Trust Policy Changed
Privilege Expanded
```

Especially important:

```text
Privilege Expansion
```

that is unexpected or occurs outside normal change workflows.

---

# 10. Excessive Permissions

Detection can identify:

```text
New Broad Permission
+
Rare User
+
Sensitive Resource
```

Example:

```text
Action:
Allow *

Resource:
All Resources
```

Such broad permission changes require strong contextual review.

---

# 11. Access Key Detection

Monitor:

```text
Key Created
Key Deleted
Key Rotated
Key Used
Inactive Key Reactivated
```

Suspicious sequence:

```text
Login
 ↓
New Access Key
 ↓
Key Used from New Location
 ↓
Sensitive API Calls
```

---

# 12. Cloud Resource Creation

Monitor creation of:

```text
VM
Container
Function
Storage
Database
Network
Role
Key
Snapshot
Security Group
```

Unexpected resources may indicate:

```text
Persistence
Cryptomining
Data Collection
Staging
Command and Control
```

---

# 13. Cryptomining Detection

Potential signals:

```text
Unexpected Compute Resource
+
High CPU Usage
+
Unknown Process
+
Mining Pool Communication
```

Cloud resource creation may provide additional context:

```text
New VM
+
High CPU
+
Suspicious External Destination
```

---

# 14. Cloud Storage Detection

Monitor:

```text
Bucket Creation
Policy Changes
Public Access
Mass Downloads
Large Data Reads
External Sharing
```

---

# 15. Public Storage Exposure

Potential detection:

```text
Private Storage
      ↓
Public Access Enabled
      ↓
Sensitive Data Exists
```

This is both:

```text
Security Event
```

and potentially:

```text
Compliance Event
```

---

# 16. Mass Cloud Data Access

Potential sequence:

```text
Normal User
      ↓
Large Number of Objects Accessed
      ↓
Unusual Time
      ↓
New Location
      ↓
External Transfer
```

Potential:

```text
Data Theft
```

---

# 17. Cloud Network Detection

Monitor:

```text
Security Group
Network ACL
Route
Load Balancer
VPC Flow
Public Exposure
Unexpected Egress
```

---

# 18. Security Group Changes

Potentially suspicious:

```text
Restricted Port
      ↓
Internet Access Enabled
```

Example:

```text
Database
Port 5432
Source:
0.0.0.0/0
```

The exact risk depends on architecture and intended exposure.

---

# 19. Cloud Egress Detection

Monitor:

```text
Unexpected External Destination
Large Transfer
Rare Destination
New Destination
Sensitive Workload
```

---

# 20. Cloud Metadata Services

Cloud workloads may interact with metadata services.

Monitor unexpected access patterns involving:

```text
Metadata Endpoint
Credential Retrieval
Instance Identity
```

Such activity can be important during cloud compromise investigations.

---

# 21. Serverless Detection

Serverless environments include:

```text
Functions
Triggers
Events
API Gateways
Queues
Storage Events
```

Useful signals:

```text
Function Creation
Code Update
Permission Change
Unexpected Invocation
Unusual Invocation Volume
External Destination
```

---

# 22. Serverless Persistence

Potential sequence:

```text
Compromised Identity
      ↓
Function Created
      ↓
Trigger Configured
      ↓
Function Executes
```

This may provide a persistence mechanism.

---

# 23. Serverless Abuse

Potential signals:

```text
Function Invocations Spike
+
New Function Code
+
Unexpected Network Destination
```

Context is required because legitimate deployments can produce the same events.

---

# 24. Cloud API Detection

APIs are central to cloud operations.

Monitor:

```text
API Caller
API Action
Resource
Source
Result
Frequency
Sequence
```

---

# 25. API Enumeration

Potential pattern:

```text
Identity
 ↓
Many API Queries
 ↓
Many Resources
```

Potential:

```text
Discovery
```

---

# 26. API Abuse

Potential signals:

```text
High Request Rate
Unexpected Endpoint
Unusual User-Agent
Invalid Requests
Privilege-Sensitive Operations
```

---

# 27. Application Detection Engineering

Application detection focuses on:

```text
Authentication
Authorization
Sessions
Requests
Responses
APIs
Transactions
Data Access
Errors
```

---

# 28. Application Telemetry

Useful fields:

```text
Timestamp
User
Session
Source IP
HTTP Method
URL
Endpoint
Status Code
Response Size
User-Agent
Request ID
Trace ID
Resource
```

---

# 29. Application Logs

Application logs should answer:

```text
Who made the request?
What did they request?
When?
From where?
What happened?
What resource was affected?
```

---

# 30. Structured Logging

Prefer structured events:

```json
{
  "timestamp": "...",
  "user_id": "123",
  "request_id": "abc",
  "endpoint": "/api/resource",
  "action": "read",
  "status": 200
}
```

Structured logs simplify detection and correlation.

---

# 31. Authentication Detection

Monitor:

```text
Failed Login
Successful Login
Password Reset
MFA
Session Creation
Session Revocation
```

---

# 32. Application Account Takeover

Potential sequence:

```text
Failed Login Burst
      ↓
Successful Login
      ↓
New Device
      ↓
Session Creation
      ↓
Sensitive API Access
```

---

# 33. Session Anomalies

Monitor:

```text
Session Reuse
Session From Multiple Locations
Session From New Device
Long-Lived Session
Unexpected Token Use
```

---

# 34. Authorization Detection

Important events:

```text
Permission Denied
Permission Granted
Role Change
Privilege Escalation
Unauthorized Resource Access
```

---

# 35. Broken Access Control Detection

Potential pattern:

```text
User
 ↓
Repeated Access to Unauthorized Resource
 ↓
Sequential Resource IDs
```

This can indicate attempted authorization abuse.

---

# 36. API Enumeration

Example:

```text
/api/users/100
/api/users/101
/api/users/102
/api/users/103
```

A pattern of sequential access may indicate resource enumeration.

Legitimate applications can also generate predictable IDs, so context matters.

---

# 37. API Abuse Detection

Monitor:

```text
Request Rate
Endpoint Diversity
Status Codes
Authentication
Source
User
Response Size
```

---

# 38. HTTP Error Patterns

Potential indicators:

```text
Large Number of 401
Large Number of 403
Large Number of 404
Large Number of 500
```

Patterns can indicate:

```text
Brute Force
Enumeration
Scanning
Application Abuse
```

---

# 39. Status Code Sequences

Example:

```text
404
404
404
404
200
```

Potential:

```text
Endpoint Discovery
```

Another:

```text
401
401
401
200
```

Potential:

```text
Credential Guessing
```

---

# 40. Request Rate Detection

Example:

```text
1000 requests
within 1 minute
```

may indicate:

```text
Automation
Abuse
Scanning
DDoS
Legitimate Batch Job
```

Context determines the result.

---

# 41. User-Agent Detection

Potential signals:

```text
Rare User-Agent
Unexpected Automation
Known Offensive Tool Signature
Inconsistent Browser Identity
```

User-Agent alone should rarely be considered sufficient evidence.

---

# 42. Application Data Access

Monitor:

```text
Sensitive Record Reads
Mass Downloads
Bulk Export
Search Bursts
Administrative Queries
```

---

# 43. Data Exfiltration Through APIs

Potential sequence:

```text
Authentication
 ↓
Search
 ↓
Large Result Sets
 ↓
Repeated Requests
 ↓
Large Outbound Transfer
```

---

# 44. Application Abuse Correlation

Combine:

```text
Identity
+
API
+
Application
+
Network
```

Example:

```text
New Login
+
High API Rate
+
Sensitive Data Access
+
Large Egress
```

---

# 45. Application Error Correlation

A sequence such as:

```text
Many Errors
 ↓
Successful Request
 ↓
Sensitive Access
```

can sometimes indicate exploitation or discovery.

---

# 46. Exploit Detection

Detection can combine:

```text
Suspicious Request
+
Application Error
+
Unexpected Process
+
Network Connection
```

This provides stronger evidence than matching a single request pattern.

---

# 47. Container Detection Engineering

Containers introduce a different execution model:

```text
Image
 ↓
Container
 ↓
Process
 ↓
Network
 ↓
Volume
```

---

# 48. Container Telemetry

Useful fields:

```text
Container ID
Image
Image Digest
Pod
Namespace
Node
Process
User
Command
Network
Volume
Service Account
```

---

# 49. Container Image Detection

Monitor:

```text
Unknown Image
Untrusted Registry
Unsigned Image
Rare Image
Unexpected Image Tag
Image Digest Change
```

---

# 50. Image Tagging Risk

Avoid relying exclusively on:

```text
latest
```

because tags can change.

Prefer immutable identifiers such as:

```text
Image Digest
```

where supported.

---

# 51. Container Creation

Potentially suspicious:

```text
Unexpected Container
+
Privileged Mode
+
Host Mount
+
External Network
```

---

# 52. Privileged Containers

Monitor:

```text
Privileged Container
Host Namespace
Host Filesystem Mount
Sensitive Device Access
Root User
```

These configurations can provide significantly greater host access.

---

# 53. Container Escape Detection

Potential signals:

```text
Unexpected Host Access
+
Privileged Configuration
+
Sensitive Device Access
+
Host Process Interaction
```

Detection requires environment-specific telemetry.

---

# 54. Container Process Detection

Monitor:

```text
Unexpected Process
Unexpected Parent
Shell Spawn
Network Tool
Privilege Change
Package Installation
```

---

# 55. Container Shell Detection

Example:

```text
Web Application Container
      ↓
Shell
      ↓
Network Utility
      ↓
External Connection
```

This may indicate post-exploitation.

---

# 56. Container Network Detection

Monitor:

```text
Unexpected Egress
Container-to-Container Communication
External Destination
Unexpected Port
DNS
```

---

# 57. Container-to-Container Communication

A compromised container may attempt:

```text
Container A
      ↓
Database
Container B
      ↓
Internal Service
```

Unexpected relationships can be detected through network telemetry.

---

# 58. Kubernetes Detection

Kubernetes introduces:

```text
Cluster
Node
Pod
Namespace
Service Account
Role
RoleBinding
API Server
```

---

# 59. Kubernetes Audit Logs

Important events:

```text
Pod Creation
Deployment Change
Role Creation
RoleBinding
Secret Access
Service Account
Exec
Port Forward
API Requests
```

---

# 60. Kubernetes RBAC Detection

Monitor:

```text
Role Created
Role Modified
RoleBinding Created
ClusterRoleBinding
Privilege Expansion
```

---

# 61. Kubernetes Secret Access

Secrets may contain:

```text
Credentials
Tokens
API Keys
Certificates
```

Monitor unexpected:

```text
Secret Reads
```

especially from unusual identities or workloads.

---

# 62. Kubernetes Exec Detection

A potentially important signal:

```text
kubectl exec
```

or equivalent API behavior.

Context:

```text
Who
Into Which Pod
From Where
Why
What Process
```

matters.

---

# 63. Kubernetes Service Account Abuse

Potential sequence:

```text
Service Account
      ↓
Token Access
      ↓
API Enumeration
      ↓
Privilege Change
      ↓
Sensitive Resource
```

---

# 64. Kubernetes Persistence

Potential methods may involve:

```text
Deployment Modification
DaemonSet
CronJob
Service Account
Admission Configuration
```

Detection should focus on unexpected administrative changes.

---

# 65. Kubernetes Discovery

Potential behavior:

```text
List Pods
List Secrets
List Services
List Nodes
List Roles
```

A burst of enumeration by an unusual identity can be significant.

---

# 66. Container + Kubernetes Correlation

Example:

```text
Unusual API Access
      ↓
Pod Creation
      ↓
Privileged Container
      ↓
External Connection
```

This is stronger than any one event.

---

# 67. CI/CD Detection

Modern workloads often originate from:

```text
Source Repository
 ↓
Build
 ↓
Artifact
 ↓
Container Image
 ↓
Deployment
```

Monitor:

```text
Pipeline Changes
Credential Changes
Unexpected Builds
Artifact Changes
Deployment Changes
```

---

# 68. Pipeline Credential Abuse

Potential:

```text
Compromised Developer
      ↓
Pipeline Access
      ↓
Secret Access
      ↓
Build Modification
      ↓
Malicious Artifact
```

---

# 69. Supply Chain Detection

Monitor:

```text
Dependency Change
Base Image Change
Build Script Change
Artifact Hash Change
Unexpected Publisher
Registry Activity
```

---

# 70. Infrastructure-as-Code Detection

Monitor:

```text
Terraform
CloudFormation
Kubernetes Manifests
Deployment Configuration
IAM Configuration
Network Configuration
```

Unexpected infrastructure changes can be highly valuable detection signals.

---

# 71. Configuration Drift

Example:

```text
Expected:
Private Database

Observed:
Public Database
```

Configuration drift can indicate:

```text
Misconfiguration
Unauthorized Change
Attack
```

---

# 72. Cloud + Application Correlation

Example:

```text
Cloud Login
 ↓
Application Deployment
 ↓
New API Endpoint
 ↓
Sensitive Data Access
```

---

# 73. Cloud + Container Correlation

Example:

```text
Cloud IAM Change
 ↓
Container Deployment
 ↓
Privileged Container
 ↓
External Network
```

---

# 74. Application + Container Correlation

Example:

```text
Web Request
 ↓
Application Process
 ↓
Shell Spawn
 ↓
Network Connection
```

This can indicate application compromise.

---

# 75. Application + Identity Correlation

Example:

```text
New Login
 ↓
Sensitive API Access
 ↓
Large Data Export
```

---

# 76. Cloud + Identity + Application

Example:

```text
New Cloud Login
 ↓
New Role
 ↓
Application Admin Access
 ↓
Sensitive Data Export
```

---

# 77. Cloud + Identity + Endpoint

Example:

```text
Identity Compromise
 ↓
Cloud Credential Use
 ↓
Endpoint Activity
 ↓
Cloud API Access
```

---

# 78. Container + Network + Identity

Example:

```text
Service Account
 ↓
Container Exec
 ↓
Internal Network Scan
```

Potential cluster compromise.

---

# 79. Modern Attack Chain

A realistic cloud-native attack may look like:

```text
Phishing
   ↓
Identity Compromise
   ↓
Cloud Login
   ↓
Privilege Escalation
   ↓
Secret Access
   ↓
Container Deployment
   ↓
Application Access
   ↓
Data Collection
   ↓
Exfiltration
```

Detection engineering must therefore cross multiple domains.

---

# 80. Cloud Detection Architecture

```text
Cloud Audit Logs
        ↓
Identity Logs
        ↓
Network Logs
        ↓
Workload Logs
        ↓
Container Logs
        ↓
Application Logs
        ↓
Normalization
        ↓
Detection
        ↓
Correlation
        ↓
Risk
        ↓
Alert
```

---

# 81. Application Detection Architecture

```text
HTTP/API
   ↓
Application Logs
   ↓
Authentication
   ↓
Authorization
   ↓
Database
   ↓
Network
   ↓
Correlation
   ↓
Detection
```

---

# 82. Container Detection Architecture

```text
Image
 ↓
Container
 ↓
Process
 ↓
Network
 ↓
Kubernetes
 ↓
Cloud
 ↓
Correlation
```

---

# 83. Cloud Identity Resolution

A cloud user may appear as:

```text
User
Role
Session
Temporary Credential
Service Account
Federated Identity
```

Detection systems need to preserve the original identity context.

---

# 84. Cloud Session Context

Useful fields:

```text
Principal
Session Name
Role
Source IP
User Agent
MFA
Region
Credential Type
```

---

# 85. Application Request Correlation

Use:

```text
Request ID
Trace ID
Session ID
User ID
```

to connect:

```text
API Request
Application Event
Database Event
Network Event
```

---

# 86. Distributed Tracing

Modern applications often use:

```text
Trace ID
Span ID
Parent Span
```

This can help connect activity across microservices.

---

# 87. Microservice Detection

Example:

```text
API Gateway
 ↓
Service A
 ↓
Service B
 ↓
Database
```

Suspicious behavior can propagate across services.

---

# 88. Microservice Anomaly

Example:

```text
Service A
normally calls:
Service B

Observed:
Service A
calls:
External Service
```

This may indicate:

```text
Compromise
Configuration Change
Supply Chain Issue
```

---

# 89. Database Detection

Monitor:

```text
Authentication
Privilege Changes
Schema Changes
Large Queries
Mass Reads
Exports
Administrative Commands
```

---

# 90. Database + Application Correlation

Example:

```text
Web User
 ↓
Unusual API Request
 ↓
Large Database Query
 ↓
Large Response
 ↓
External Transfer
```

Potential data exfiltration.

---

# 91. Secrets Detection

Sensitive secrets include:

```text
API Keys
Tokens
Passwords
Certificates
Private Keys
Cloud Credentials
```

Monitor:

```text
Secret Creation
Secret Access
Secret Rotation
Secret Export
```

---

# 92. Secret Access Detection

Potential sequence:

```text
Unusual Identity
 ↓
Secret Store Access
 ↓
New Compute Resource
 ↓
External Connection
```

This can indicate credential theft or abuse.

---

# 93. Cloud Resource Relationship Graph

Example:

```text
User
 │
 └── Role
      │
      └── VM
           │
           └── Container
                │
                └── Service
                     │
                     └── Database
```

Graph relationships provide useful investigation context.

---

# 94. Cloud Asset Criticality

Not every cloud resource has equal importance.

Examples:

```text
Development VM
Production API
Identity Provider
Database
Payment Service
```

Risk scoring should account for business importance.

---

# 95. Cloud Baselines

Baseline:

```text
Normal Regions
Normal APIs
Normal Users
Normal Resources
Normal Network Destinations
Normal Deployment Patterns
```

Then detect meaningful deviations.

---

# 96. Application Baselines

Baseline:

```text
Requests/User
Endpoints/User
Response Size
Normal Error Rate
Normal Access Pattern
```

---

# 97. Container Baselines

Baseline:

```text
Images
Processes
Network Destinations
Privileges
Namespaces
Service Accounts
```

---

# 98. Kubernetes Baselines

Baseline:

```text
Pods
Deployments
RBAC
Namespaces
API Requests
Service Accounts
```

---

# 99. Behavioral Detection

Behavioral detection can identify:

```text
New
Rare
Unexpected
Excessive
Sequential
Periodic
Privilege-changing
```

activity.

---

# 100. Static vs Behavioral Detection

### Static

```text
Known Malicious IP
Known Hash
Known Domain
```

### Behavioral

```text
Unusual API Access
Unexpected Privilege Change
Rare Container Behavior
Abnormal Data Access
```

Behavioral detection is often more resilient to changing infrastructure.

---

# 101. Cloud Detection Exceptions

Examples:

```text
Approved Deployment Pipeline
Authorized Security Scanner
Known Backup System
Approved Administrative Account
```

Exceptions should remain:

```text
Specific
Documented
Auditable
```

---

# 102. Application Detection Exceptions

Examples:

```text
Known Health Checks
Monitoring Bots
Load Testing
Internal Automation
```

---

# 103. Container Detection Exceptions

Examples:

```text
Approved CI/CD Runner
Security Scanner
Known Platform Agent
```

---

# 104. Kubernetes Detection Exceptions

Examples:

```text
Platform Controller
Cluster Operator
Deployment Controller
Monitoring Agent
```

---

# 105. Detection Testing

Test:

```text
Cloud API Abuse
IAM Change
Container Creation
Kubernetes Privilege Change
Application Enumeration
Secret Access
Data Export
```

---

# 106. Positive Cloud Test

Example:

```text
Controlled IAM Privilege Change
```

Expected:

```text
Detection Trigger
```

---

# 107. Positive Application Test

Example:

```text
Controlled API Enumeration
```

Expected:

```text
Application Detection
```

---

# 108. Positive Container Test

Example:

```text
Controlled Unexpected Shell
```

Expected:

```text
Container Detection
```

---

# 109. Positive Kubernetes Test

Example:

```text
Controlled Privileged Role Assignment
```

Expected:

```text
Kubernetes Detection
```

---

# 110. Negative Testing

Validate that normal:

```text
Deployments
Autoscaling
Health Checks
Backups
Monitoring
CI/CD
```

do not create excessive alerts.

---

# 111. Detection Latency

Measure:

```text
Cloud Event
 ↓
Log Ingestion
 ↓
Normalization
 ↓
Detection
 ↓
Alert
```

---

# 112. Cloud Detection Challenges

Common challenges:

```text
Huge API Volume
Dynamic Infrastructure
Short-Lived Workloads
Multiple Accounts
Multiple Regions
Multiple Services
Identity Complexity
```

---

# 113. Application Detection Challenges

```text
High Request Volume
Distributed Architecture
Encrypted Traffic
Dynamic APIs
User-Generated Content
Legitimate Automation
```

---

# 114. Container Detection Challenges

```text
Ephemeral Containers
Dynamic IPs
Short Lifetimes
Shared Nodes
Image Changes
High Deployment Frequency
```

---

# 115. Kubernetes Detection Challenges

```text
High API Volume
Controller Activity
Service Accounts
Dynamic Workloads
Complex RBAC
Large Cluster State
```

---

# 116. Detection Performance

Optimize:

```text
Filtering
Normalization
Aggregation
Correlation
State
Queries
Retention
```

Avoid unnecessary:

```text
Full-Table Searches
Long Windows
High-Cardinality Joins
Complex Regex
```

---

# 117. Detection-as-Code Metadata

Example:

```yaml
id: DET-CLOUD-001

name: Suspicious Cloud Privilege Change

domain:
  - cloud
  - identity

entities:
  - user
  - role
  - resource

severity: high

confidence: medium

tests:
  - positive
  - negative

status: production
```

---

# 118. Cloud Detection Checklist

```text
[ ] Cloud audit logs enabled
[ ] Identity logs enabled
[ ] Network logs available
[ ] Workload logs available
[ ] Container telemetry available
[ ] Kubernetes audit logs available
[ ] Application logs structured
[ ] API requests traceable
[ ] Users resolved
[ ] Cloud roles resolved
[ ] Resources resolved
[ ] Sensitive resources identified
[ ] Baselines defined
[ ] Detection hypotheses documented
[ ] Positive tests created
[ ] Negative tests created
[ ] Exceptions documented
[ ] Detection latency measured
[ ] ATT&CK mappings validated
```

---

# 119. Interview Questions

### Why are cloud audit logs important?

> They record control-plane operations such as identity changes, resource creation, policy modification, and sensitive API activity.

### What is cloud control-plane activity?

> Administrative operations used to create, modify, delete, or configure cloud resources and services.

### How would you detect cloud account takeover?

> Correlate unusual authentication, new device or location, credential or access-key changes, privilege changes, and sensitive API activity.

### How would you detect suspicious container activity?

> Monitor image provenance, container creation, privilege configuration, process execution, network behavior, and unexpected access to host resources.

### What is Kubernetes audit logging?

> Logging of API-server operations such as resource creation, RBAC changes, secret access, exec operations, and other cluster management activity.

### Why are privileged containers important?

> They may have significantly greater access to the host or underlying infrastructure and therefore increase the impact of a compromise.

### How would you detect API abuse?

> Combine request rate, endpoint diversity, authentication context, response patterns, source, user, and resource sensitivity.

### How would you detect data exfiltration through an API?

> Correlate unusual authentication, sensitive resource access, high-volume API requests, large responses, and unusual outbound network activity.

### What is configuration drift?

> A deviation between the intended configuration and the observed configuration.

### Why are cloud identities difficult to correlate?

> Cloud environments can involve users, roles, temporary credentials, service accounts, federated identities, and sessions representing the same logical actor.

### How can containers complicate detection?

> Containers are often short-lived, dynamically created, and share infrastructure, making traditional host-based assumptions less reliable.

### What is the importance of request IDs and trace IDs?

> They allow events across distributed application components and services to be connected into a single transaction or activity chain.

---

# 120. Quick Revision

```text
Cloud Detection
→ Detect cloud control-plane and workload behavior

Control Plane
→ Administrative cloud operations

Cloud Audit Log
→ Record of cloud API activity

IAM
→ Identity and access management

Access Key
→ Credential used for cloud access

Serverless
→ Event-driven function execution

Application Detection
→ Detect application and API behavior

Request ID
→ Identifier for an application request

Trace ID
→ Identifier connecting distributed service activity

Container
→ Isolated application workload

Image
→ Template used to create a container

Container Digest
→ Immutable image identifier

Privileged Container
→ Container with elevated host/infrastructure access

Kubernetes
→ Container orchestration platform

Kubernetes Audit Log
→ Record of API-server activity

RBAC
→ Role-based access control

Service Account
→ Identity used by workloads

Secret
→ Sensitive credential or token

Configuration Drift
→ Difference between expected and observed configuration

Cloud Egress
→ Outbound cloud network activity

API Abuse
→ Suspicious or excessive API usage

Workload Identity
→ Identity associated with an application workload
```

---

# 121. Golden Rules

```text
1. Cloud detection starts with control-plane visibility.

2. Identity is central to cloud security.

3. Monitor privilege changes.

4. Monitor access-key creation and usage.

5. Monitor sensitive resource access.

6. Treat cloud API activity as first-class security telemetry.

7. Baseline cloud behavior by identity, resource, and service.

8. Do not treat every new cloud resource as malicious.

9. Context matters for cloud administrative activity.

10. Monitor public exposure changes.

11. Monitor unexpected cloud egress.

12. Treat application APIs as security telemetry.

13. Use structured application logs.

14. Preserve request IDs and trace IDs.

15. Correlate authentication with application behavior.

16. Monitor sensitive data access.

17. Monitor abnormal API rates.

18. Do not rely on User-Agent alone.

19. Containers require workload-aware detection.

20. Monitor image provenance.

21. Monitor privileged containers.

22. Monitor unexpected container processes.

23. Monitor container network activity.

24. Kubernetes API activity is highly valuable telemetry.

25. Monitor RBAC changes.

26. Monitor service-account behavior.

27. Monitor secret access.

28. Treat CI/CD as part of the security boundary.

29. Monitor deployment and infrastructure changes.

30. Detect configuration drift.

31. Resolve cloud identities carefully.

32. Resolve workload identities carefully.

33. Account for ephemeral infrastructure.

34. Test detections against legitimate automation.

35. Test positive and negative cases.

36. Measure detection latency.

37. Keep exceptions narrow and auditable.

38. Use business criticality in risk scoring.

39. Correlate cloud, identity, application, container, and network signals.

40. Modern detection engineering must protect workloads, identities, APIs, and infrastructure together.
```

---

# 122. Final Mental Model

Modern environments can be understood as:

```text
IDENTITY
    ↓
CLOUD CONTROL PLANE
    ↓
WORKLOAD
    ↓
CONTAINER
    ↓
APPLICATION
    ↓
DATABASE
    ↓
NETWORK
```

An attacker may move through:

```text
Identity
   ↓
Cloud API
   ↓
Privilege
   ↓
Container
   ↓
Application
   ↓
Data
   ↓
Exfiltration
```

A mature detection architecture therefore observes:

```text
WHO?
 ↓
WHAT CLOUD ACTION?
 ↓
WHAT WORKLOAD?
 ↓
WHAT APPLICATION?
 ↓
WHAT DATA?
 ↓
WHERE DID IT GO?
```

Then:

```text
Telemetry
    ↓
Normalization
    ↓
Entity Resolution
    ↓
Behavior Detection
    ↓
Cross-Domain Correlation
    ↓
Risk
    ↓
Alert
    ↓
Investigation
```

---

# 123. Chapter Summary

This chapter covered:

```text
Cloud Detection Engineering
Cloud Control Plane
Cloud Audit Logs
Cloud IAM
Cloud Account Takeover
Cloud Privilege Escalation
IAM Policy Changes
Access Keys
Cloud Resource Creation
Cryptomining Detection
Cloud Storage
Public Exposure
Mass Data Access
Cloud Network Detection
Security Groups
Cloud Egress
Metadata Services
Serverless Detection
Cloud APIs
API Enumeration
API Abuse
Application Detection
Structured Logging
Authentication
Authorization
Session Detection
API Enumeration
HTTP Error Detection
Request Rate
User-Agent Context
Data Access
API Exfiltration
Container Detection
Container Images
Image Digests
Privileged Containers
Container Processes
Container Networking
Kubernetes
Kubernetes Audit Logs
RBAC
Secrets
Service Accounts
Kubernetes Exec
Kubernetes Persistence
CI/CD Detection
Supply Chain Detection
Infrastructure-as-Code
Configuration Drift
Microservices
Distributed Tracing
Database Detection
Secrets Detection
Cloud/Application/Container Correlation
Baselines
Behavioral Detection
Detection Testing
Detection Performance
```

The central principle is:

> **Modern applications are distributed across identities, cloud services, containers, APIs, workloads, and networks. Effective detection engineering must therefore follow the activity across these boundaries rather than treating each platform as an isolated security domain.**

The modern detection model is:

```text
IDENTITY
    +
CLOUD
    +
APPLICATION
    +
CONTAINER
    +
KUBERNETES
    +
NETWORK
       ↓
CORRELATION
       ↓
RISK
       ↓
ACTIONABLE DETECTION
```

The objective is not simply to monitor cloud logs or container events. The objective is to understand **how identities, infrastructure, workloads, applications, and data interact—and detect when those relationships deviate from legitimate behavior.**

---