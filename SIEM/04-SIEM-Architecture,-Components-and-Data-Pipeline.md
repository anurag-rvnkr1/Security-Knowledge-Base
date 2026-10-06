# Chapter 04 – SIEM Architecture, Components & Data Pipeline

> A SIEM is not a single application. It is a collection of interconnected components responsible for collecting, transporting, processing, storing, searching, detecting, correlating, and presenting security telemetry.

---

# 1. Introduction

A basic SIEM architecture can be represented as:

```text
DATA SOURCES
     ↓
COLLECTORS / AGENTS
     ↓
INGESTION
     ↓
PROCESSING
     ↓
NORMALIZATION
     ↓
ENRICHMENT
     ↓
STORAGE / INDEXING
     ↓
SEARCH / ANALYTICS
     ↓
DETECTION / CORRELATION
     ↓
ALERTING
     ↓
INVESTIGATION
     ↓
RESPONSE
```

The architecture must support four fundamental requirements:

```text
Visibility
Scalability
Reliability
Security
```

---

# 2. SIEM as a System

A SIEM can be viewed as several logical layers:

```text
┌───────────────────────────────────────┐
│           Analyst / SOC Layer         │
│ Dashboards • Search • Cases • Alerts  │
├───────────────────────────────────────┤
│       Detection & Analytics Layer     │
│ Rules • Correlation • Risk • Hunting  │
├───────────────────────────────────────┤
│          Search / Query Layer         │
├───────────────────────────────────────┤
│         Storage / Index Layer         │
├───────────────────────────────────────┤
│        Processing / Enrichment         │
├───────────────────────────────────────┤
│       Collection / Ingestion Layer    │
├───────────────────────────────────────┤
│             Data Sources              │
└───────────────────────────────────────┘
```

---

# 3. Core SIEM Components

A typical SIEM may contain:

```text
1. Data Sources
2. Agents
3. Collectors
4. Forwarders
5. Ingestion Layer
6. Message Queue
7. Processing Engine
8. Parser
9. Normalizer
10. Enrichment Engine
11. Storage
12. Index
13. Search Engine
14. Detection Engine
15. Correlation Engine
16. Alert Manager
17. Dashboard
18. Case Management
19. API
20. Administration Layer
```

Not every SIEM exposes these as separate services.

---

# 4. Data Sources

The architecture begins with telemetry sources.

```text
Windows
Linux
Firewall
DNS
VPN
EDR
IDS/IPS
Identity
Cloud
Applications
Databases
Containers
SaaS
```

Each produces different data formats and volumes.

---

# 5. Collection Layer

The collection layer obtains telemetry.

```text
Endpoint
   ↓
Agent
   ↓
Collector
```

or:

```text
Firewall
   ↓
Syslog
   ↓
Collector
```

or:

```text
Cloud
   ↓
API
   ↓
Collector
```

---

# 6. Collector

A collector is responsible for receiving or retrieving telemetry.

It may handle:

```text
Connection Management
Authentication
Buffering
Filtering
Compression
Encryption
Routing
Basic Parsing
```

---

# 7. Collector Architecture

Small environment:

```text
Sources
   ↓
Single Collector
   ↓
SIEM
```

Large environment:

```text
Sources
   ↓
Regional Collectors
   ↓
Load Balancers
   ↓
Central Processing
```

---

# 8. Regional Collectors

Global organizations may deploy collectors close to data sources.

```text
USA Sources
    ↓
USA Collector
    │
    ├─────────────┐
                  │
Europe Sources    │
    ↓             │
EU Collector      │
    │             │
    └──────┬──────┘
           ▼
       Central SIEM
```

Benefits:

```text
Reduced Latency
Bandwidth Optimization
Regional Resilience
Data Residency Support
```

---

# 9. Forwarders

A forwarder transfers telemetry from one component to another.

```text
Endpoint
   ↓
Forwarder
   ↓
Collector
   ↓
SIEM
```

A forwarder may provide:

```text
Filtering
Buffering
Encryption
Compression
Routing
```

---

# 10. Ingestion Layer

The ingestion layer receives telemetry into the SIEM pipeline.

```text
Collectors
    ↓
Ingestion
    ↓
Processing
```

It should be able to handle:

```text
High Throughput
Burst Traffic
Retries
Authentication
Validation
Backpressure
```

---

# 11. Message Queue

Large environments often use a message queue.

```text
Collectors
     ↓
Message Queue
     ↓
Processing Workers
```

Examples of technologies used in broader data platforms include:

```text
Apache Kafka
RabbitMQ
Cloud Messaging Services
```

The specific technology depends on architecture.

---

# 12. Why Use a Queue?

Without a queue:

```text
Collector
   ↓
Processor
```

If the processor fails:

```text
Data Flow
   ↓
Interrupted
```

With a queue:

```text
Collector
   ↓
Queue
   ↓
Processor
```

The queue can temporarily retain events while consumers recover.

---

# 13. Queue Benefits

A queue can provide:

```text
Buffering
Scalability
Decoupling
Retry
Fault Isolation
Load Distribution
```

---

# 14. Queue Partitioning

Large systems may partition events.

Example:

```text
Queue
 ├── Partition 1
 ├── Partition 2
 ├── Partition 3
 └── Partition 4
```

Consumers can process partitions in parallel.

---

# 15. Processing Layer

The processing layer transforms incoming data.

Typical operations:

```text
Decode
Parse
Normalize
Validate
Enrich
Filter
Deduplicate
Route
```

Example:

```text
Raw Event
   ↓
Parse
   ↓
Normalize
   ↓
Enrich
   ↓
Validate
```

---

# 16. Parsing Engine

The parser understands source-specific formats.

Example:

```text
Firewall:
src=10.0.0.1 dst=10.0.0.2 action=ALLOW
```

Parser extracts:

```text
source.ip
destination.ip
event.action
```

---

# 17. Normalization Engine

The normalization layer maps source-specific fields to common fields.

```text
src
src_ip
sourceAddress
client_ip
rhost
```

↓

```text
source.ip
```

This enables cross-source detection.

---

# 18. Enrichment Engine

The enrichment layer adds context.

```text
source.ip
   ↓
Threat Intelligence
   ↓
Malicious = True
```

or:

```text
destination.ip
   ↓
Asset Inventory
   ↓
Critical Server
```

---

# 19. Processing Pipeline Example

```text
RAW EVENT
    ↓
Decode
    ↓
Parse
    ↓
Normalize
    ↓
GeoIP
    ↓
Threat Intelligence
    ↓
Asset Enrichment
    ↓
Validation
    ↓
Index
```

---

# 20. Storage Layer

The SIEM must store security data.

Storage may contain:

```text
Raw Events
Normalized Events
Alerts
Cases
Threat Intelligence
Metadata
Audit Logs
```

---

# 21. Why Storage Matters

Stored telemetry supports:

```text
Historical Investigation
Threat Hunting
Compliance
Forensics
Detection Testing
Incident Review
Trend Analysis
```

---

# 22. Indexing

An index makes large volumes of data searchable.

Conceptually:

```text
Billions of Events
       ↓
Index
       ↓
Fast Search
```

Without efficient indexing:

```text
Query
 ↓
Scan Huge Dataset
 ↓
Slow
```

With indexing:

```text
Query
 ↓
Relevant Index
 ↓
Fast Retrieval
```

---

# 23. Search Engine

The search layer allows analysts to query telemetry.

Example:

```text
source.ip = 10.10.10.20
AND
event.outcome = failure
```

Search engines may support:

```text
Filtering
Aggregation
Sorting
Time Ranges
Full-Text Search
Structured Queries
Statistical Analysis
```

---

# 24. Search vs Detection

Search:

> Analyst asks a question.

Detection:

> SIEM automatically asks a security question repeatedly.

Example:

```text
SEARCH:
Find failed logins from IP X.

DETECTION:
Alert when an IP generates
more than 20 failed logins
within 5 minutes.
```

---

# 25. Detection Engine

The detection engine evaluates telemetry against security logic.

```text
Events
  ↓
Detection Rule
  ↓
Condition Match
  ↓
Alert
```

---

# 26. Detection Rule

Example:

```text
IF
failed_login_count > 20

AND

unique_users > 5

WITHIN
5 minutes

THEN
generate alert
```

This may identify password spraying behavior.

---

# 27. Correlation Engine

Correlation combines related events.

Example:

```text
Failed Login
      +
Successful Login
      +
Privilege Change
      +
Suspicious Process
```

↓

```text
Potential Account Compromise
```

---

# 28. Correlation vs Detection

Detection:

```text
"This event matches a suspicious condition."
```

Correlation:

```text
"These events are related and together indicate suspicious behavior."
```

Modern SIEMs often combine both concepts.

---

# 29. Alert Manager

The alert manager handles generated alerts.

It may perform:

```text
Deduplication
Grouping
Prioritization
Severity Assignment
Routing
Notification
Suppression
Escalation
```

---

# 30. Alert Grouping

Suppose:

```text
100 identical alerts
```

Instead of displaying:

```text
Alert 1
Alert 2
Alert 3
...
Alert 100
```

the SIEM may group them:

```text
Password Spray
100 Events
18 Users
4 Hosts
```

This reduces analyst workload.

---

# 31. Alert Deduplication

If the same detection fires repeatedly:

```text
Alert A
Alert A
Alert A
```

the SIEM can suppress duplicate alerts for a defined period.

This helps reduce:

```text
Alert Fatigue
```

---

# 32. Risk Scoring

Some architectures calculate risk.

Example:

```text
Suspicious Login       +20
Malicious IP           +40
Privilege Escalation   +50
Critical Server        +30
```

Total:

```text
140
```

Higher score:

```text
Higher Priority
```

---

# 33. Entity Risk

Risk can be associated with entities:

```text
User Risk
Host Risk
IP Risk
Cloud Account Risk
Application Risk
```

Example:

```text
User Alice
Risk Score = 85
```

because of:

```text
Impossible Travel
+
Failed MFA
+
Suspicious Login
```

---

# 34. Dashboard Layer

Dashboards provide visual summaries.

Examples:

```text
Alert Volume
Critical Alerts
Top Source IPs
Failed Logins
Malware Detections
Incident Status
Log Source Health
Detection Coverage
```

---

# 35. SOC Dashboard

A SOC dashboard might contain:

```text
┌──────────────────────────────────┐
│ Critical Alerts       12         │
│ High Alerts           38         │
│ Open Incidents        7          │
│ EPS                   85K        │
│ Log Sources Healthy   97%        │
└──────────────────────────────────┘

Top Threats
────────────────────
Brute Force
Malware
Phishing
Suspicious PowerShell

Top Sources
────────────────────
Firewall
EDR
Identity
Cloud
```

---

# 36. Case Management

Alerts often become investigations.

```text
Alert
 ↓
Case
 ↓
Investigation
 ↓
Evidence
 ↓
Actions
 ↓
Resolution
```

A case may contain:

```text
Description
Severity
Owner
Timeline
Alerts
Entities
Notes
Evidence
Tasks
Response Actions
Resolution
```

---

# 37. SIEM APIs

Modern SIEM platforms often expose APIs.

Use cases:

```text
Alert Retrieval
Case Management
Automation
Threat Intelligence
Custom Integrations
Data Ingestion
Reporting
```

Example:

```text
SOAR
   ↓
SIEM API
   ↓
Retrieve Alert
```

---

# 38. SIEM and SOAR Architecture

```text
                  SIEM
                   │
                Alert
                   │
                   ▼
                  SOAR
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       Firewall    EDR      IAM
       Block IP   Isolate   Disable
                   │
                   ▼
               Response
```

---

# 39. Administration Layer

Administrative functions include:

```text
User Management
Role Management
Data Source Configuration
Detection Management
Retention
Integration
API Keys
Certificates
System Health
```

This layer must be strongly protected.

---

# 40. RBAC

**Role-Based Access Control**

Example:

```text
Analyst
 ↓
Search + Investigate

Detection Engineer
 ↓
Search + Create Rules

Administrator
 ↓
System Configuration
```

Apply:

```text
Least Privilege
```

---

# 41. Multi-Tenancy

Managed security providers may monitor multiple customers.

Architecture:

```text
Customer A ──┐
Customer B ──┤
Customer C ──┤
              ▼
          Shared SIEM
```

Strong logical isolation is required.

---

# 42. Data Isolation

Different customers or business units may require:

```text
Separate Indexes
Separate Tenants
Separate Access Policies
Separate Encryption Keys
```

The exact design depends on requirements.

---

# 43. SIEM Deployment Models

Common models:

```text
On-Premises
Cloud
Hybrid
Managed SIEM
```

---

# 44. On-Premises Architecture

```text
                    Enterprise
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
    Servers          Network          Endpoints
       │                │                │
       └────────────────┼────────────────┘
                        ▼
                   Collectors
                        │
                        ▼
                  SIEM Cluster
              ┌─────────┼─────────┐
              ▼         ▼         ▼
           Search    Detection   Storage
```

---

# 45. Cloud SIEM Architecture

```text
Cloud Sources
     │
     ▼
Connectors
     │
     ▼
Ingestion
     │
     ▼
Processing
     │
     ▼
Cloud Storage
     │
     ▼
Analytics
     │
     ▼
Alerts
```

Advantages:

```text
Elastic Scaling
Managed Infrastructure
Cloud Integrations
```

---

# 46. Hybrid Architecture

```text
On-Prem
   │
   ▼
Collectors
   │
   ├──────────────┐
                  │
Cloud             │
   │              │
   ▼              │
Cloud Connectors  │
   │              │
   └──────┬───────┘
          ▼
         SIEM
```

---

# 47. High Availability

A production SIEM should avoid single points of failure.

Bad:

```text
Source
 ↓
Single Collector
 ↓
Single SIEM
```

If the SIEM fails:

```text
Visibility = 0
```

---

# 48. High Availability Architecture

Better:

```text
          Load Balancer
             │
      ┌──────┼──────┐
      ▼      ▼      ▼
     SIEM1  SIEM2  SIEM3
      │      │      │
      └──────┼──────┘
             ▼
        Distributed
          Storage
```

---

# 49. Failover

If:

```text
Collector 1
```

fails:

```text
Sources
   ↓
Collector 2
```

If:

```text
Processing Node 1
```

fails:

```text
Queue
 ↓
Processing Node 2
```

---

# 50. Disaster Recovery

A SIEM should have a recovery strategy.

Consider:

```text
Backup
Replication
Secondary Region
Configuration Backup
Detection Backup
Case Backup
Threat Intelligence Backup
```

---

# 51. Recovery Point Objective

**RPO** answers:

> How much data can the organization afford to lose?

Example:

```text
RPO = 15 minutes
```

Means the architecture aims to limit recoverable data loss to approximately that window.

---

# 52. Recovery Time Objective

**RTO** answers:

> How quickly must the system be restored?

Example:

```text
RTO = 1 hour
```

The organization aims to restore service within that target.

---

# 53. SIEM Scalability

A SIEM must scale across:

```text
Events Per Second
Data Volume
Users
Queries
Detections
Retention
Log Sources
```

---

# 54. EPS

**Events Per Second**

Example:

```text
10,000 EPS
```

means:

```text
10,000 events/sec
```

EPS is useful for understanding ingestion capacity.

But:

> EPS alone does not determine total SIEM resource requirements.

Event size, indexing, retention, query load, enrichment, and detection complexity also matter.

---

# 55. Query Load

Two environments may ingest:

```text
100,000 EPS
```

but have very different query workloads.

Environment A:

```text
20 analysts
```

Environment B:

```text
500 analysts
+
thousands of scheduled searches
```

The second may require substantially more analytics capacity.

---

# 56. Storage Capacity

Storage requirements depend on:

```text
Ingestion Rate
Average Event Size
Compression
Index Overhead
Retention
Replication
Hot/Warm/Cold Strategy
```

---

# 57. Retention

Retention defines how long data is kept.

Example:

```text
Hot:
7 days

Warm:
30 days

Cold:
180 days

Archive:
1 year
```

Exact periods depend on:

```text
Security Requirements
Compliance
Business Needs
Cost
Risk
```

---

# 58. Cost Optimization

SIEM cost can be controlled through:

```text
Filtering
Tiered Storage
Compression
Retention Policies
Data Routing
Sampling where appropriate
Reducing Duplicate Data
Efficient Queries
```

But cost optimization must not destroy critical security visibility.

---

# 59. Data Pipeline Bottlenecks

Common bottlenecks:

```text
Collection
Network
Queue
Parser
Enrichment
Storage
Indexing
Search
Detection
```

---

# 60. Bottleneck Example

Suppose:

```text
Input:
100K EPS

Parsing:
100K EPS

Enrichment:
40K EPS
```

Then:

```text
Enrichment
   ↓
Bottleneck
```

Possible solutions:

```text
Scale Enrichment Workers
Optimize Lookups
Cache Results
Reduce Expensive Enrichment
```

---

# 61. Caching

Repeated enrichment requests can be expensive.

Example:

```text
IP → Threat Intelligence
```

Instead of querying the external service for every event:

```text
First lookup
 ↓
Cache result
 ↓
Reuse temporarily
```

This reduces:

```text
Latency
API Usage
Cost
```

Cache freshness requirements must be considered.

---

# 62. Distributed Processing

Large SIEM platforms may distribute work:

```text
Events
  ↓
Worker 1
Worker 2
Worker 3
Worker 4
  ↓
Storage
```

Advantages:

```text
Parallel Processing
Scalability
Fault Tolerance
```

---

# 63. Detection Scheduling

Detections may execute:

```text
Real-Time
Near Real-Time
Scheduled
```

Example:

```text
Every Event
 ↓
Real-Time Rule
```

or:

```text
Every 5 minutes
 ↓
Search Last 10 Minutes
```

---

# 64. Real-Time Detection

```text
Event
 ↓
Pipeline
 ↓
Detection
 ↓
Alert
```

Advantages:

```text
Low Latency
Fast Response
```

Potential challenge:

```text
Higher Processing Cost
```

---

# 65. Scheduled Detection

```text
Events
 ↓
Storage
 ↓
Scheduled Query
 ↓
Detection
 ↓
Alert
```

Useful for:

```text
Complex Queries
Historical Patterns
Aggregation
Periodic Threat Hunting
```

---

# 66. Correlation Windows

A detection may look across a time window.

Example:

```text
10:00 → Failed Login
10:01 → Failed Login
10:02 → Failed Login
10:03 → Successful Login
```

Rule:

```text
Within 5 minutes
```

↓

```text
Potential Brute Force
```

---

# 67. Sliding Windows

A sliding window continuously evaluates recent events.

```text
Current Time
     │
     ▼
───────────────
Last 5 Minutes
───────────────
```

As time moves:

```text
Old events leave
New events enter
```

Useful for:

```text
Rate Detection
Brute Force
Scanning
Flooding
```

---

# 68. Stateful Detection

Some detections maintain state.

Example:

```text
User:
alice

Failed Login:
5

Successful Login:
1

Privilege Change:
1
```

The detection tracks the sequence over time.

---

# 69. Stateless vs Stateful Detection

### Stateless

Each event evaluated independently.

```text
IF event.action = malware_detection
THEN alert
```

### Stateful

Multiple events and historical state are considered.

```text
5 failures
+
success
+
privilege change
```

Stateful detection can identify more complex behaviors.

---

# 70. Event Correlation Architecture

```text
                 EVENTS
                   │
          ┌────────┼────────┐
          ▼        ▼        ▼
       Identity  Network  Endpoint
          │        │        │
          └────────┼────────┘
                   ▼
              Correlation
                   │
                   ▼
              Risk Engine
                   │
                   ▼
                 Alert
```

---

# 71. Investigation Layer

Analysts need:

```text
Search
Timeline
Entity View
Related Events
Threat Intelligence
Alert Details
Case Management
```

A SIEM architecture should optimize not only data ingestion but also analyst investigation.

---

# 72. Timeline View

Example:

```text
09:00:01  Failed Login
09:00:05  Failed Login
09:00:10  Successful Login
09:01:15  MFA Disabled
09:03:20  Admin Role Added
09:05:44  Data Access
```

This helps analysts understand the attack sequence.

---

# 73. Entity-Centric Investigation

Instead of searching only by event:

```text
User: alice
```

Analyst can pivot through:

```text
User
 ↓
Hosts
 ↓
IPs
 ↓
Processes
 ↓
Domains
 ↓
Alerts
 ↓
Cases
```

---

# 74. SIEM Data Pipeline Summary

```text
                 SOURCES
                    │
                    ▼
              COLLECTION
                    │
                    ▼
               FORWARDING
                    │
                    ▼
                INGESTION
                    │
                    ▼
                 QUEUE
                    │
                    ▼
               PROCESSING
                    │
          ┌─────────┼─────────┐
          ▼         ▼         ▼
        PARSE    NORMALIZE  ENRICH
          │         │         │
          └─────────┼─────────┘
                    ▼
                 VALIDATE
                    │
                    ▼
               INDEX / STORE
                    │
             ┌──────┴──────┐
             ▼             ▼
          SEARCH        DETECTION
             │             │
             └──────┬──────┘
                    ▼
                 ALERT
                    │
                    ▼
              INVESTIGATION
                    │
                    ▼
                 RESPONSE
```

---

# 75. Security of the SIEM Architecture

Protect every layer.

## Source

```text
Secure Logging
```

## Collector

```text
Authentication
Encryption
Hardening
```

## Queue

```text
Access Control
Encryption
```

## Processing

```text
Least Privilege
```

## Storage

```text
Encryption
RBAC
Integrity
```

## Search

```text
Authentication
Authorization
```

## Detection

```text
Change Control
```

## Administration

```text
MFA
Privileged Access
Audit Logs
```

---

# 76. SIEM as a High-Value Target

A SIEM may contain:

```text
Credentials
Network Information
User Activity
Security Events
Attack Evidence
Threat Intelligence
Incident Data
```

An attacker compromising the SIEM could potentially:

```text
Hide Activity
Disable Detections
Modify Rules
Delete Evidence
Steal Sensitive Information
```

Therefore:

> **Protecting the SIEM is itself a security requirement.**

---

# 77. SIEM Monitoring Itself

The SIEM should monitor:

```text
Collectors
Ingestion
Queues
Parsing
Storage
Detection
Authentication
Administrative Changes
```

This creates:

```text
Security Monitoring
        +
SIEM Platform Monitoring
```

---

# 78. Detection Engineering Pipeline

A mature architecture supports:

```text
Threat Research
      ↓
Detection Development
      ↓
Testing
      ↓
Deployment
      ↓
Monitoring
      ↓
Tuning
      ↓
Versioning
```

---

# 79. Detection-as-Code Concept

Detection rules can be managed like software:

```text
Rule
 ↓
Version Control
 ↓
Testing
 ↓
Review
 ↓
Deployment
```

Benefits:

```text
Change Tracking
Peer Review
Rollback
Consistency
Automation
```

---

# 80. Configuration Management

Important SIEM configurations include:

```text
Collectors
Parsers
Schemas
Rules
Dashboards
Retention
Users
Roles
Integrations
```

Configuration changes should be controlled and audited.

---

# 81. Change Management

Example:

```text
Parser Update
   ↓
Test
   ↓
Peer Review
   ↓
Deploy
   ↓
Monitor
```

Avoid uncontrolled production changes.

---

# 82. SIEM Architecture Best Practices

```text
1. Design for failure.

2. Avoid single points of failure.

3. Separate collection from processing where scale requires it.

4. Use buffering for resilience.

5. Monitor ingestion latency.

6. Monitor event loss.

7. Normalize important fields.

8. Protect ingestion endpoints.

9. Use least privilege.

10. Encrypt sensitive data.

11. Monitor the SIEM itself.

12. Design storage around retention requirements.

13. Separate hot, warm, and cold data where appropriate.

14. Test parsers after vendor changes.

15. Version detection rules.

16. Build for horizontal scaling where necessary.

17. Maintain disaster recovery.

18. Document data flows.

19. Protect administrative interfaces.

20. Treat the SIEM as a critical security asset.
```

---

# 83. Practical Architecture Exercise

Design a SIEM for:

```text
500 Employees
50 Servers
200 Endpoints
2 Firewalls
1 VPN
1 Identity Platform
Cloud Infrastructure
```

Identify:

```text
Data Sources
 ↓
Collection Method
 ↓
Collectors
 ↓
Ingestion
 ↓
Processing
 ↓
Storage
 ↓
Detection
 ↓
Alerting
```

---

# 84. Example Architecture

```text
Windows ───────┐
Linux ─────────┤
EDR ───────────┤
Firewall ──────┤
VPN ───────────┤
DNS ───────────┤
Identity ──────┤
Cloud ─────────┤
                ▼
          Collection Layer
                │
                ▼
           Ingestion Layer
                │
                ▼
              Queue
                │
                ▼
          Processing Layer
                │
       ┌────────┼────────┐
       ▼        ▼        ▼
     Parse   Normalize  Enrich
       │        │        │
       └────────┼────────┘
                ▼
            Storage
                │
       ┌────────┴────────┐
       ▼                 ▼
    Search            Detection
                         │
                         ▼
                       Alert
                         │
                         ▼
                       Case
                         │
                         ▼
                      Response
```

---

# 85. Interview Questions

### What are the main components of a SIEM?

> Data sources, collection, ingestion, processing, parsing, normalization, enrichment, storage, indexing, search, detection, correlation, alerting, investigation, and administration.

### Why use a message queue?

> To buffer events, decouple producers and consumers, handle bursts, improve resilience, and enable scalable processing.

### What is a collector?

> A component that receives or retrieves telemetry from one or more data sources and forwards it into the SIEM pipeline.

### What is the difference between collector and forwarder?

> A collector generally receives or gathers telemetry, while a forwarder primarily transfers telemetry between components. In some products their responsibilities overlap.

### Why is indexing important?

> It enables efficient searching across large volumes of security data.

### What is high availability?

> Designing the system so that failure of one component does not cause unacceptable service interruption.

### What is horizontal scaling?

> Adding additional processing or storage nodes to increase capacity.

### What is vertical scaling?

> Increasing CPU, memory, storage, or other resources of an existing node.

### What is EPS?

> Events Per Second, a measure of telemetry ingestion volume.

### What is RPO?

> Recovery Point Objective, representing the maximum acceptable amount of data loss measured in time.

### What is RTO?

> Recovery Time Objective, representing the target time for restoring a service after disruption.

### Why is a SIEM a high-value target?

> Because it contains security telemetry, investigation evidence, detection logic, and potentially sensitive organizational information.

### What is the role of a detection engine?

> It evaluates telemetry against defined security logic and generates alerts when suspicious conditions are identified.

### What is correlation?

> Combining multiple events or signals to identify relationships and higher-level security behavior.

### What is case management?

> The process of organizing alerts, evidence, investigation notes, tasks, and response actions into an incident or investigation record.

---

# 86. Quick Revision

```text
SOURCE
→ Generates telemetry

COLLECTOR
→ Receives telemetry

FORWARDER
→ Transfers telemetry

INGESTION
→ Brings data into processing

QUEUE
→ Buffers and distributes data

PROCESSING
→ Transforms data

PARSER
→ Extracts fields

NORMALIZER
→ Standardizes fields

ENRICHER
→ Adds context

STORAGE
→ Retains data

INDEX
→ Enables efficient search

SEARCH
→ Analyst queries data

DETECTION
→ Identifies suspicious conditions

CORRELATION
→ Connects related events

ALERT
→ Notifies analysts

CASE
→ Organizes investigation

SOAR
→ Automates response
```

---

# 87. Golden Rules

```text
1. A SIEM is a system of components, not simply a database.

2. Collection and processing can be separated for scalability.

3. Queues improve resilience and decouple components.

4. Processing pipelines should be observable.

5. Storage and indexing are different concerns.

6. Search performance matters to analysts.

7. Detection can be real-time or scheduled.

8. Stateful correlation can identify multi-event attacks.

9. Alert management should reduce duplicate noise.

10. High availability prevents single points of failure.

11. Disaster recovery is part of SIEM architecture.

12. EPS is important but does not tell the whole capacity story.

13. Retention directly affects storage requirements and cost.

14. Enrichment can become a pipeline bottleneck.

15. SIEM infrastructure must monitor itself.

16. Administrative access should follow least privilege.

17. Detection rules should be version-controlled where practical.

18. Configuration changes should be controlled.

19. Protect the SIEM like any other critical security system.

20. Architecture should be designed around security visibility, reliability, scale, and investigation speed.
```

---

# 88. Chapter Summary

The most important architectural model is:

```text
                DATA SOURCES
                     │
                     ▼
               COLLECTION
                     │
                     ▼
                INGESTION
                     │
                     ▼
                  QUEUE
                     │
                     ▼
                PROCESSING
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     PARSE       NORMALIZE      ENRICH
       │             │             │
       └─────────────┼─────────────┘
                     ▼
                VALIDATION
                     │
                     ▼
              STORAGE / INDEX
                     │
            ┌────────┴────────┐
            ▼                 ▼
         SEARCH           DETECTION
            │                 │
            └────────┬────────┘
                     ▼
                   ALERT
                     │
                     ▼
              INVESTIGATION
                     │
                     ▼
                  RESPONSE
```

A production SIEM must additionally provide:

```text
High Availability
Scalability
Monitoring
Access Control
Encryption
Backup
Disaster Recovery
Configuration Management
Detection Management
```

The key mental model is:

> **The SIEM architecture transforms distributed telemetry into centralized, searchable, correlated, and actionable security intelligence.**

The next chapter moves into the heart of SIEM analytics:

```text
Chapter 05
    ↓
Detection Engineering, Rules & Correlation
```

There we will cover how SOC teams actually turn telemetry into detections, including rule logic, thresholds, correlation, sequences, behavioral detections, risk scoring, MITRE ATT&CK mapping, false-positive tuning, testing, and production detection lifecycle.