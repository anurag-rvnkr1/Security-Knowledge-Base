# SIEM Cheatsheet

> A compact, interview-focused and practical reference covering SIEM fundamentals, log management, detection engineering, correlation, threat intelligence, MITRE ATT&CK, investigation, incident response, SIEM engineering, cloud security, SOAR, UEBA, XDR, and modern SOC operations.

---

# 1. SIEM Fundamentals

## SIEM

**SIEM = Security Information and Event Management**

Core functions:

```text
Collect
 ↓
Normalize
 ↓
Store
 ↓
Search
 ↓
Correlate
 ↓
Detect
 ↓
Alert
 ↓
Investigate
 ↓
Respond
```

## Main SIEM Functions

```text
Log Collection
Log Management
Normalization
Enrichment
Search
Detection
Correlation
Alerting
Investigation
Threat Hunting
Reporting
Compliance
```

---

# 2. SIEM vs SOC vs SOAR vs XDR

| Technology | Primary Purpose |
|---|---|
| SIEM | Collect, correlate, detect, investigate |
| SOAR | Automate and orchestrate response |
| EDR | Endpoint detection and response |
| NDR | Network detection and response |
| XDR | Integrated detection and response across security domains |
| UEBA | User/entity behavioral analytics |
| TIP | Threat intelligence management |
| SOC | People + processes + technology |

Simplified:

```text
SIEM → Detect
SOAR → Automate
EDR  → Protect endpoints
NDR  → Analyze network
UEBA → Analyze behavior
XDR  → Integrate security controls
SOC  → Operate everything
```

---

# 3. SIEM Architecture

```text
Data Sources
     ↓
Collectors
     ↓
Transport / Queue
     ↓
Parsing
     ↓
Normalization
     ↓
Enrichment
     ↓
Storage
     ↓
Detection
     ↓
Correlation
     ↓
Risk
     ↓
Alert
     ↓
SOC
     ↓
Response
```

---

# 4. Common SIEM Data Sources

```text
Windows
Linux
Firewall
VPN
IDS/IPS
EDR
NDR
DNS
DHCP
Proxy
Web Server
Application
Database
Email
IAM
Cloud Audit
Cloud Network
Kubernetes
Containers
SaaS
```

---

# 5. High-Value Log Sources

Usually high-value:

```text
Identity
Endpoint
Firewall
DNS
VPN
Cloud
Email
EDR
```

Why?

```text
Identity → Account compromise
Endpoint → Execution
Firewall → Network behavior
DNS → C2 / malicious domains
VPN → Remote access
Cloud → API / IAM activity
Email → Phishing
EDR → Endpoint behavior
```

---

# 6. Log Lifecycle

```text
Generate
 ↓
Collect
 ↓
Transport
 ↓
Parse
 ↓
Normalize
 ↓
Enrich
 ↓
Store
 ↓
Search
 ↓
Detect
 ↓
Investigate
 ↓
Retain / Archive
```

---

# 7. Raw Log vs Parsed Log

Raw:

```text
2026-08-13 login failed user=alice src=10.0.0.5
```

Parsed:

```text
timestamp = 2026-08-13
event.action = login
event.outcome = failure
user.name = alice
source.ip = 10.0.0.5
```

---

# 8. Parsing

**Parsing = converting raw log data into structured fields.**

Common methods:

```text
Regex
JSON Parsing
CSV Parsing
Key-Value Parsing
Vendor Parsers
Grok-like Patterns
```

Parsing problems:

```text
Format Change
Malformed Logs
Encoding
Timestamp Change
Unexpected Fields
Vendor Update
```

---

# 9. Normalization

Different vendors:

```text
src_ip
sourceAddress
client_ip
```

Normalize:

```text
source.ip
```

Purpose:

```text
Reusable Queries
Reusable Detection
Correlation
Cross-Vendor Visibility
```

---

# 10. Common Normalized Fields

```text
@timestamp

event.action
event.category
event.type
event.outcome

user.name
user.id

source.ip
source.port

destination.ip
destination.port

host.name

process.name
process.pid
process.command_line

file.name
file.hash

url.domain
url.path

network.protocol
```

---

# 11. Event Categories

```text
Authentication
Process
Network
File
DNS
Web
Cloud
Email
Configuration
Privilege
```

---

# 12. Event Outcome

```text
success
failure
unknown
```

Example:

```text
event.action = login
event.outcome = failure
```

---

# 13. Enrichment

**Enrichment = adding useful context to an event.**

Example:

```text
IP
 ↓
GeoIP
 ↓
ASN
 ↓
Threat Intelligence
```

Another:

```text
Host
 ↓
Asset Criticality
 ↓
Business Owner
```

Common enrichment:

```text
Threat Intelligence
Asset Inventory
CMDB
GeoIP
ASN
User Directory
Vulnerability Data
Cloud Inventory
Business Criticality
```

---

# 14. SIEM Query Basics

Typical query workflow:

```text
Time Filter
 ↓
Event Filter
 ↓
Field Filter
 ↓
Aggregation
 ↓
Correlation
```

Always start with a reasonable time range.

---

# 15. Common Search Operations

```text
=
!=
AND
OR
NOT
IN
LIKE
COUNT
UNIQUE
GROUP BY
SORT
```

Exact syntax depends on the SIEM.

---

# 16. Query Optimization

Prefer:

```text
Time Filter
+
Structured Fields
+
Relevant Dataset
+
Aggregation
```

Avoid:

```text
Entire Historical Dataset
+
Complex Regex
+
High Cardinality
```

---

# 17. Detection Engineering

Detection engineering converts:

```text
Threat
 ↓
Behavior
 ↓
Telemetry
 ↓
Detection Logic
 ↓
Alert
```

A detection should define:

```text
Objective
Data Sources
Fields
Logic
Threshold
Time Window
Severity
Risk
MITRE Mapping
Exceptions
Response
Owner
Version
```

---

# 18. Detection-as-Code

Treat detections as software.

Store:

```text
Rules
Queries
Tests
Metadata
Documentation
Versions
```

Benefits:

```text
Version Control
Peer Review
Testing
Rollback
Auditability
Collaboration
```

---

# 19. Detection Lifecycle

```text
Threat
 ↓
Requirement
 ↓
Design
 ↓
Development
 ↓
Testing
 ↓
Review
 ↓
Deployment
 ↓
Monitoring
 ↓
Tuning
 ↓
Retirement
```

---

# 20. Positive vs Negative Testing

### Positive

Suspicious behavior:

```text
Expected → ALERT
```

### Negative

Legitimate behavior:

```text
Expected → NO ALERT
```

Also test:

```text
Boundary
Missing Fields
Duplicates
Delayed Events
High Volume
```

---

# 21. Detection Tuning

If noisy:

```text
Analyze False Positives
 ↓
Add Context
 ↓
Adjust Threshold
 ↓
Adjust Time Window
 ↓
Add Narrow Exception
 ↓
Retest
```

Never blindly disable a noisy detection.

---

# 22. False Positive

```text
Detection Triggered
+
Activity is Legitimate
```

Example:

```text
PowerShell
```

does not automatically mean:

```text
Malware
```

---

# 23. False Negative

```text
Malicious Activity
+
Detection Fails
```

False negatives are dangerous because the attacker may remain undetected.

---

# 24. Precision

```text
Precision =
True Positives
-------------------------
True Positives + False Positives
```

High precision:

```text
More triggered alerts are useful
```

---

# 25. Recall

```text
Recall =
True Positives
-------------------------
True Positives + False Negatives
```

High recall:

```text
More relevant malicious activity is detected
```

---

# 26. Precision vs Recall

```text
Precision
→ Reduce False Positives

Recall
→ Reduce False Negatives
```

The right balance depends on:

```text
Threat
Risk
SOC Capacity
Response Cost
```

---

# 27. Detection Latency

```text
Event Occurs
 ↓
Event Ingested
 ↓
Detection Executes
 ↓
Alert Generated
```

Important metric:

```text
Detection Latency
```

---

# 28. Ingestion Latency

```text
Event Generated
 ↓
Collected
 ↓
SIEM Receives
```

Difference:

```text
Ingestion Latency
```

---

# 29. EPS

**EPS = Events Per Second**

Example:

```text
Average = 5,000 EPS
Peak = 15,000 EPS
```

Design for peak traffic.

---

# 30. SIEM Capacity

Consider:

```text
EPS
GB/day
Peak Volume
Retention
Search Load
Detection Load
Replication
Growth
```

---

# 31. Storage Tiers

```text
HOT
 ↓
WARM
 ↓
COLD
 ↓
ARCHIVE
```

### Hot

```text
Fast Search
Recent Data
Real-Time Detection
```

### Warm

```text
Recent Historical Data
```

### Cold/Archive

```text
Long-Term Retention
Compliance
Forensics
```

---

# 32. Retention

Retention depends on:

```text
Security Requirements
Compliance
Legal Requirements
Investigation Needs
Storage Cost
```

---

# 33. Data Quality

Important dimensions:

```text
Completeness
Accuracy
Timeliness
Consistency
Validity
```

Poor telemetry:

```text
Poor Detection
```

---

# 34. Schema Drift

Example:

```text
Old:
source_ip

New:
client_ip
```

Detection expects:

```text
source.ip
```

Parser/detection may break.

Solution:

```text
Schema Monitoring
Parser Testing
Version Control
```

---

# 35. Ingestion Health

Monitor:

```text
Events Expected
Events Received
Events Parsed
Events Stored
Latency
Dropped Events
Errors
```

---

# 36. SIEM Health

Monitor:

```text
Collectors
Ingestion
Parsing
Storage
Queries
Detection Engine
Alerting
APIs
Connectors
```

---

# 37. Data Loss

Example:

```text
Generated = 100,000
Received = 80,000
```

Potential:

```text
20% Visibility Gap
```

---

# 38. Clock Synchronization

Use:

```text
NTP
Consistent Time
Normalized Timestamps
UTC where appropriate
```

Incorrect time causes:

```text
Broken Timelines
Broken Correlation
Incorrect Investigations
```

---

# 39. Correlation

Correlation combines multiple signals.

Example:

```text
Failed Login
+
Successful Login
+
MFA Change
+
Privilege Change
```

↓

```text
Possible Account Compromise
```

---

# 40. Correlation Types

```text
Time-Based
Entity-Based
Sequence-Based
Threshold-Based
Risk-Based
Cross-Source
```

---

# 41. Time-Based Correlation

```text
Event A
+
Event B
within 10 minutes
```

---

# 42. Entity-Based Correlation

Group by:

```text
User
Host
IP
Account
Cloud Resource
```

---

# 43. Sequence-Based Correlation

```text
Phishing
 ↓
Execution
 ↓
Credential Access
 ↓
C2
```

---

# 44. Threshold-Based Detection

Example:

```text
Failed Logins > 20
within 10 minutes
```

---

# 45. Risk-Based Correlation

Example:

```text
Suspicious Login      +20
MFA Change            +30
Privilege Change      +40
Malicious IP          +50
Critical Asset        +30
```

Total:

```text
170
```

---

# 46. Risk Scoring

Risk can consider:

```text
User
Host
IP
Asset Criticality
Threat Intelligence
Behavior
Technique
Historical Risk
```

---

# 47. Risk Decay

Old activity can gradually lose weight:

```text
Risk = 100
 ↓
70
 ↓
40
 ↓
10
```

This prevents stale events from permanently increasing risk.

---

# 48. Alert

An alert is:

```text
A security signal requiring attention.
```

A useful alert should contain:

```text
What happened?
Who?
What host?
When?
Source?
Destination?
Why suspicious?
Risk?
Evidence?
Recommended next step?
```

---

# 49. Alert vs Incident

```text
Alert
→ Signal

Incident
→ Confirmed/suspected security event requiring coordinated response
```

Not every alert becomes an incident.

---

# 50. Alert Fatigue

Caused by:

```text
Too Many Alerts
Low Precision
Duplicate Alerts
Poor Correlation
Insufficient Context
```

Reduce through:

```text
Tuning
Grouping
Deduplication
Risk Scoring
Correlation
Enrichment
```

---

# 51. Alert Grouping

Instead of:

```text
100 related alerts
```

create:

```text
1 Incident
+
100 Related Events
```

---

# 52. Alert Deduplication

Group repeated alerts using:

```text
Same Rule
+
Same User
+
Same Host
+
Short Time Window
```

---

# 53. Authentication Use Cases

Important:

```text
Brute Force
Password Spraying
Credential Stuffing
Impossible Travel
Unusual Login
Privileged Login
MFA Manipulation
Account Lockout
New Device
```

---

# 54. Brute Force

```text
One Account
+
Many Failed Attempts
```

Example:

```text
Alice
 ↓
50 Failed Logins
```

---

# 55. Password Spraying

```text
One Source
+
Many Users
+
Authentication Failures
```

Difference:

```text
Brute Force
→ One/Few Users + Many Attempts

Password Spray
→ Many Users + Few Attempts Per User
```

---

# 56. Credential Stuffing

```text
Compromised Credential Lists
+
Login Attempts
```

Usually involves reuse of previously exposed credentials.

---

# 57. Successful Login After Failures

```text
Failure
 ↓
Failure
 ↓
Failure
 ↓
Success
```

Potential:

```text
Account Compromise
```

Add context:

```text
IP
Device
Location
MFA
User
```

---

# 58. Impossible Travel

```text
Login A
→ Location A

Shortly after

Login B
→ Distant Location
```

Investigate:

```text
VPN
Proxy
Cloud Access
Mobile Network
Geolocation Accuracy
```

---

# 59. Privileged Account Monitoring

Monitor:

```text
Administrator
Root
Domain Admin
Cloud Admin
Security Admin
```

Look for:

```text
Unusual Time
Unusual Device
Unusual Location
Privilege Change
Sensitive Action
```

---

# 60. Endpoint Use Cases

```text
Malware
PowerShell
Command Shell
Suspicious Process
Persistence
Credential Access
Lateral Movement
Unsigned Binary
Rare Process
```

---

# 61. Suspicious PowerShell

Weak:

```text
PowerShell executed
```

Better:

```text
PowerShell
+
Encoded Command
+
Unusual Parent
+
External Network
```

---

# 62. Suspicious Process Chain

Example:

```text
winword.exe
 ↓
powershell.exe
 ↓
unknown.exe
 ↓
external connection
```

Potential:

```text
Malware Execution
```

---

# 63. Persistence

Monitor:

```text
Scheduled Tasks
Services
Startup Items
Registry
New Accounts
Cloud Credentials
```

---

# 64. Credential Access

Monitor:

```text
Credential Store
Sensitive Process Access
Browser Credentials
Memory Access
Credential Dumping Indicators
```

---

# 65. Lateral Movement

Monitor:

```text
RDP
SSH
SMB
Remote Authentication
Remote Execution
Administrative Shares
```

---

# 66. Network Use Cases

```text
Port Scan
Malicious IP
Malicious Domain
DNS Tunneling
Beaconing
C2
Data Exfiltration
Rare Destination
```

---

# 67. Port Scan

Potential pattern:

```text
One Source
+
Many Ports
```

or:

```text
One Source
+
Many Hosts
```

within a short window.

---

# 68. DNS Tunneling

Potential signals:

```text
Long Queries
High Volume
High Entropy
Rare Domain
Repeated Queries
Unusual Record Types
```

---

# 69. Beaconing

Potential:

```text
Repeated Connections
+
Regular Intervals
+
Same Destination
```

Example:

```text
10:00
10:05
10:10
10:15
```

Periodic behavior alone is not proof of C2.

---

# 70. C2

Potential combination:

```text
Suspicious Process
+
Periodic Network Connection
+
Rare Destination
+
Threat Intelligence
```

---

# 71. Data Exfiltration

Potential sequence:

```text
Sensitive Access
 ↓
Archive
 ↓
Large Transfer
 ↓
External Destination
```

---

# 72. Web Use Cases

```text
SQL Injection
XSS
Path Traversal
Authentication Abuse
Web Shell
API Abuse
Suspicious User Agent
```

---

# 73. Email Use Cases

```text
Phishing
Malicious Attachment
Malicious URL
BEC
Spoofing
Credential Harvesting
```

---

# 74. Phishing Attack Chain

```text
Email
 ↓
User Click
 ↓
Malicious Domain
 ↓
Download
 ↓
Execution
```

Cross-source correlation is stronger than email-only detection.

---

# 75. Cloud Use Cases

```text
Unusual Cloud Login
IAM Change
Privilege Escalation
Access Key Creation
Storage Access
Security Group Change
New Resource
API Abuse
Cryptomining
```

---

# 76. Cloud Account Compromise

```text
Unusual Login
 ↓
MFA Change
 ↓
Privilege Escalation
 ↓
New Key
 ↓
Sensitive API Calls
```

---

# 77. Cloud Storage Exfiltration

```text
Sensitive Object
+
New Principal
+
Large Download
+
External Source
```

---

# 78. Ransomware

Behavioral signals:

```text
Mass File Changes
File Rename
Encryption-Like Activity
Shadow Copy Changes
Backup Tampering
Security Tool Changes
Multiple Hosts
```

---

# 79. Ransomware Correlation

```text
Mass File Modification
+
Suspicious Process
+
Backup Tampering
+
Multiple Hosts
```

↓

```text
High-Risk Ransomware Candidate
```

---

# 80. Insider Risk

Potential:

```text
Sensitive Access
+
Large Download
+
Unusual Time
+
External Transfer
```

Do not automatically infer malicious intent from anomalous employee behavior.

---

# 81. Threat Intelligence

Threat Intelligence enriches:

```text
IP
Domain
URL
Hash
Actor
Campaign
```

Important attributes:

```text
Confidence
Age
Source
Relevance
Context
```

---

# 82. IOC

IOC = Indicator of Compromise

Examples:

```text
Malicious IP
Malicious Domain
File Hash
URL
Email Address
```

---

# 83. IOC Lifecycle

```text
Collect
 ↓
Validate
 ↓
Enrich
 ↓
Store
 ↓
Match
 ↓
Detect
 ↓
Expire / Review
```

---

# 84. IOC Limitations

IOC matches can become:

```text
Stale
False Positive
Too Broad
Already Blocked
```

Behavior-based detection should complement IOCs.

---

# 85. MITRE ATT&CK

ATT&CK provides a knowledge base of adversary tactics and techniques.

Typical structure:

```text
Tactic
 ↓
Technique
 ↓
Sub-technique
```

---

# 86. Common ATT&CK Tactics

```text
Reconnaissance
Resource Development
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

# 87. Common Techniques

Examples:

```text
Phishing
PowerShell
Valid Accounts
Scheduled Task
Remote Services
Credential Dumping
Command and Scripting Interpreter
Data from Local System
Exfiltration Over C2 Channel
```

---

# 88. ATT&CK Detection Mapping

```text
Technique
 ↓
Telemetry
 ↓
Detection
 ↓
Test
 ↓
Coverage
```

---

# 89. Detection Coverage

Ask:

```text
Which techniques can we detect?

Which techniques have weak visibility?

Which data sources are missing?

Which detections are high confidence?
```

---

# 90. Threat Hunting

Threat hunting is:

```text
Proactive
Hypothesis-Driven
Investigation
```

Workflow:

```text
Hypothesis
 ↓
Data
 ↓
Search
 ↓
Analysis
 ↓
Validation
 ↓
Detection
```

---

# 91. Hunt Example

Hypothesis:

```text
An attacker may be using
rare remote administration tools.
```

Search:

```text
Process
User
Host
Network
Time
```

---

# 92. Hunt → Detection

```text
Hunt Finding
 ↓
Pattern
 ↓
Detection Rule
 ↓
Production
```

---

# 93. Detection → Hunt

```text
Interesting Alert
 ↓
Broader Search
 ↓
Find Related Activity
 ↓
Threat Hunt
```

---

# 94. Investigation

Basic workflow:

```text
Alert
 ↓
Validate
 ↓
Enrich
 ↓
Scope
 ↓
Timeline
 ↓
Root Cause
 ↓
Contain
 ↓
Recover
```

---

# 95. Investigation Questions

```text
What happened?

When?

Who?

Which host?

Which account?

Which process?

Which IP?

Which domain?

What changed?

How did it start?

How far did it spread?

What data was accessed?
```

---

# 96. Timeline

Example:

```text
10:01 Login
10:03 MFA Change
10:05 PowerShell
10:07 C2
10:12 Credential Access
10:20 Lateral Movement
```

Timeline reconstruction is central to investigation.

---

# 97. Incident Response

```text
Preparation
 ↓
Detection
 ↓
Analysis
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

# 98. Triage

Triage asks:

```text
Is this real?

How severe?

What is affected?

Who is affected?

Is it ongoing?

What should happen next?
```

---

# 99. Severity

A typical model:

```text
Critical
High
Medium
Low
Informational
```

Severity should consider:

```text
Impact
Confidence
Asset Criticality
User Privilege
Threat Intelligence
Scope
```

---

# 100. Containment

Possible actions:

```text
Isolate Endpoint
Disable Account
Revoke Session
Block IP
Block Domain
Remove Malicious Access
```

Actions should be authorized and appropriately controlled.

---

# 101. Eradication

Remove:

```text
Malware
Persistence
Compromised Credentials
Unauthorized Accounts
Malicious Configuration
```

---

# 102. Recovery

```text
Restore
Validate
Monitor
Return to Production
```

---

# 103. SIEM Engineering

Core areas:

```text
Parsing
Normalization
Enrichment
Detection-as-Code
Performance
Scaling
Storage
Retention
Monitoring
Testing
Reliability
```

---

# 104. Query Optimization

```text
Filter Early
 ↓
Use Structured Fields
 ↓
Limit Time
 ↓
Aggregate
 ↓
Avoid Unnecessary Regex
 ↓
Avoid High Cardinality
```

---

# 105. High Cardinality

Examples:

```text
UUID
Request ID
Session ID
Full URL
```

Grouping by many unique values can be expensive.

---

# 106. Log Bursts

Possible causes:

```text
Attack
Incident
Outage
Deployment
Authentication Failure
Scanning
```

Architecture should tolerate bursts.

---

# 107. Backpressure

```text
Producer
 ↓
Queue
 ↓
Processor
```

If processing slows:

```text
Queue Buffers Events
```

---

# 108. Queue Benefits

```text
Buffering
Burst Handling
Decoupling
Resilience
Replay
```

---

# 109. High Availability

Avoid unnecessary:

```text
Single Collector
Single Storage Node
Single Network Path
Single Critical Dependency
```

---

# 110. Disaster Recovery

Plan for:

```text
SIEM Failure
Storage Failure
Network Failure
Region Failure
Configuration Loss
Credential Failure
```

---

# 111. RTO

```text
Recovery Time Objective
```

How quickly service should be restored.

---

# 112. RPO

```text
Recovery Point Objective
```

Maximum acceptable data-loss window.

---

# 113. Detection-as-Code Pipeline

```text
Commit
 ↓
Lint
 ↓
Unit Test
 ↓
Review
 ↓
Staging
 ↓
Validation
 ↓
Production
```

---

# 114. Shadow Mode

New rule:

```text
Runs
 ↓
Does Not Alert Analysts
 ↓
Measure Results
 ↓
Tune
 ↓
Enable
```

Useful for noisy detections.

---

# 115. Canary Deployment

```text
Deploy to Small Scope
 ↓
Monitor
 ↓
Validate
 ↓
Expand
```

---

# 116. Rollback

Always have:

```text
Previous Version
+
Rollback Procedure
```

---

# 117. SIEM Security

Protect:

```text
Admin Accounts
API Keys
Connectors
Rules
Storage
Dashboards
Service Accounts
```

---

# 118. Least Privilege

Example:

```text
Collector
```

should receive only required permissions.

Avoid:

```text
Collector
→ Full Administrator
```

unless genuinely necessary and appropriately controlled.

---

# 119. SIEM Audit Logging

Monitor:

```text
Rule Changes
Admin Login
Configuration Changes
Data Source Changes
API Access
Privilege Changes
```

---

# 120. SIEM Should Monitor Itself

Monitor:

```text
Collector Failure
Parser Failure
Rule Failure
Connector Failure
Storage
Authentication
Configuration Changes
```

---

# 121. Cloud SIEM

Important cloud telemetry:

```text
Identity
Control Plane
API
Network
Storage
Application
Container
Kubernetes
SaaS
```

---

# 122. Cloud Control Plane

Examples:

```text
Create Resource
Delete Resource
Change IAM
Change Network
Create Key
Modify Storage
```

---

# 123. Cloud IAM

Monitor:

```text
Role Change
Policy Change
Permission Grant
New User
New Key
MFA Change
```

---

# 124. Cloud API

Monitor:

```text
Caller
Action
Resource
Source IP
User Agent
Timestamp
Outcome
```

---

# 125. Cloud Network

Useful telemetry:

```text
Flow Logs
Firewall
Load Balancer
DNS
Proxy
```

---

# 126. Kubernetes

Monitor:

```text
Audit Logs
Pod Creation
Role Changes
Secret Access
Service Accounts
Exec
Cluster Changes
```

---

# 127. Multi-Cloud

Challenges:

```text
Different APIs
Different Schemas
Different IAM
Different Logging
Different Regions
Different Costs
```

Solution:

```text
Normalization
+
Common Data Model
```

---

# 128. Zero Trust + SIEM

Zero Trust:

```text
Verify Explicitly
Least Privilege
Assume Breach
```

SIEM provides visibility into:

```text
Identity
Device
Resource
Network
Behavior
```

---

# 129. SOAR

SOAR:

```text
Security Orchestration
Automation and Response
```

Workflow:

```text
Alert
 ↓
Enrichment
 ↓
Decision
 ↓
Action
 ↓
Verification
 ↓
Case Update
```

---

# 130. SOAR Example

```text
Malicious IP
 ↓
Threat Intel
 ↓
Find Related Hosts
 ↓
Check EDR
 ↓
Risk
 ↓
Block / Isolate if authorized
 ↓
Verify
 ↓
Create Case
```

---

# 131. Human-in-the-Loop

```text
Low Risk
→ Automatic

Medium Risk
→ Analyst Approval

High-Impact Action
→ Strong Approval / Controlled Automation
```

---

# 132. SOAR Safety

Consider:

```text
Confidence
Scope
Approval
Rollback
Verification
Audit
```

---

# 133. Idempotency

Repeated execution should remain safe.

Example:

```text
Block IP
```

If already blocked:

```text
No destructive duplicate effect
```

---

# 134. UEBA

UEBA:

```text
User and Entity Behavior Analytics
```

Analyzes:

```text
Users
Hosts
Applications
Service Accounts
Cloud Resources
```

---

# 135. UEBA Baseline

Learn:

```text
Normal Time
Normal Location
Normal Device
Normal Application
Normal Data Volume
Normal Destination
```

Then detect:

```text
Deviation
```

---

# 136. UEBA Example

Normal:

```text
09:00
India
Laptop-A
CRM
```

New:

```text
03:00
New Country
New Device
Admin Tool
```

↓

```text
Behavioral Anomaly
```

---

# 137. UEBA + SIEM

```text
SIEM Event
+
UEBA Score
+
Asset Risk
+
Threat Intelligence
```

↓

```text
Higher Confidence
```

---

# 138. UEBA Challenges

```text
Cold Start
Model Drift
False Positives
Changing Behavior
Seasonality
Privacy
Data Quality
```

---

# 139. XDR

XDR integrates:

```text
Endpoint
Network
Email
Identity
Cloud
```

with:

```text
Detection
Investigation
Response
```

---

# 140. SIEM + XDR

```text
XDR
 ↓
Integrated Security Detection
 ↓
SIEM
 ↓
Enterprise Correlation
 ↓
SOC
```

---

# 141. AI in SOC

AI can assist with:

```text
Alert Summarization
Timeline Generation
Query Generation
Threat Intelligence Summaries
Investigation
Case Summaries
Prioritization
```

---

# 142. AI Investigation

```text
Alert
 ↓
AI Analyzes Events
 ↓
Builds Timeline
 ↓
Identifies Entities
 ↓
Summarizes Evidence
 ↓
Suggests Next Steps
```

Always validate AI conclusions.

---

# 143. AI Risks

```text
Hallucination
Incorrect Reasoning
Missing Context
Overconfidence
Unsafe Actions
Excessive Permissions
```

---

# 144. AI Guardrails

```text
Least Privilege
Read/Write Separation
Approval Gates
Tool Restrictions
Evidence Requirements
Audit Logs
Rollback
```

---

# 145. Agentic SOC

Conceptually:

```text
Observe
 ↓
Reason
 ↓
Query
 ↓
Enrich
 ↓
Recommend
 ↓
Act
```

Important:

```text
AI Agent ≠ Unlimited Access
```

---

# 146. Attack Graph

```text
User
 ↓
Host
 ↓
Process
 ↓
IP
 ↓
Domain
 ↓
Other Host
```

Useful for:

```text
Scope
Lateral Movement
Attack Path
Investigation
```

---

# 147. Modern Correlation

Traditional:

```text
Event A + Event B
```

Modern:

```text
Identity
+
Endpoint
+
Network
+
Cloud
+
Threat Intelligence
+
Behavior
```

---

# 148. Modern SOC Feedback Loop

```text
Threat
 ↓
Detection
 ↓
Investigation
 ↓
Response
 ↓
Lessons Learned
 ↓
Detection Improvement
 ↓
Automation
 ↓
Better Detection
```

---

# 149. SOC Maturity

Conceptual model:

```text
Level 1 → Reactive
Level 2 → Centralized Monitoring
Level 3 → Detection Engineering
Level 4 → Threat-Informed SOC
Level 5 → AI-Assisted / Automated SOC
```

---

# 150. SOC Metrics

Important:

```text
MTTD
MTTR
Alert Volume
False Positive Rate
Detection Coverage
Investigation Time
Automation Rate
Data Coverage
Incident Rate
```

---

# 151. MTTD

```text
Mean Time to Detect
```

```text
Attack
 ↓
Detection
```

---

# 152. MTTR

Depending on organizational definition:

```text
Mean Time to Respond
```

or:

```text
Mean Time to Resolve
```

Always define the metric before comparing it.

---

# 153. Detection Coverage

Measure coverage across:

```text
Threats
Techniques
Assets
Data Sources
Attack Stages
```

---

# 154. Modern SOC Stack

```text
SIEM
SOAR
EDR
NDR
XDR
UEBA
TIP
Vulnerability Management
Cloud Security
Identity Security
Case Management
Threat Hunting
AI
```

---

# 155. Common Attack Chains

## Account Takeover

```text
Password Spray
 ↓
Successful Login
 ↓
MFA Change
 ↓
Privilege Change
 ↓
Sensitive Access
```

## Malware

```text
Phishing
 ↓
Office
 ↓
PowerShell
 ↓
Payload
 ↓
C2
```

## Lateral Movement

```text
Credential Access
 ↓
Remote Login
 ↓
New Host
 ↓
Remote Execution
```

## Exfiltration

```text
Sensitive Access
 ↓
Archive
 ↓
Large Transfer
 ↓
External Destination
```

## Ransomware

```text
Initial Access
 ↓
Execution
 ↓
Credential Access
 ↓
Lateral Movement
 ↓
Mass File Modification
 ↓
Impact
```

---

# 156. Most Important SOC Correlations

```text
Failed Login
+
Successful Login
```

```text
New Device
+
Unusual Location
```

```text
Privilege Change
+
Sensitive Action
```

```text
PowerShell
+
Suspicious Parent
+
Network Connection
```

```text
Process
+
Rare Destination
+
Threat Intelligence
```

```text
Sensitive Data Access
+
Large Transfer
+
External Destination
```

```text
Cloud Login
+
MFA Change
+
Privilege Escalation
```

---

# 157. SIEM Troubleshooting Framework

If a detection is not firing:

```text
1. Did the source generate the event?
        ↓
2. Did collector receive it?
        ↓
3. Did transport succeed?
        ↓
4. Did parsing work?
        ↓
5. Are fields normalized?
        ↓
6. Is required data present?
        ↓
7. Did enrichment work?
        ↓
8. Did detection execute?
        ↓
9. Did correlation execute?
        ↓
10. Was alert generated?
```

---

# 158. If Logs Stop

Check:

```text
Source
 ↓
Network
 ↓
Collector
 ↓
Authentication
 ↓
Transport
 ↓
Parser
 ↓
SIEM
```

---

# 159. If Rule Suddenly Becomes Noisy

Check:

```text
Environment Change
Data Change
Parser Change
Threshold
Time Window
New Application
New Automation
```

Then:

```text
Tune
Test
Deploy
Monitor
```

---

# 160. If SIEM Performance Drops

Check:

```text
EPS
Storage
CPU
Memory
Queue
Search Volume
Detection Load
High Cardinality
Large Queries
```

---

# 161. If Alerts Suddenly Increase

Check:

```text
Attack?
Data Duplication?
Parser Problem?
Rule Change?
Threshold?
Log Burst?
Connector Issue?
```

---

# 162. Interview One-Liners

### What is SIEM?

> A platform that collects, normalizes, correlates, analyzes, and detects security events to support monitoring and incident response.

### What is correlation?

> Combining multiple events or signals to identify a higher-confidence security pattern.

### What is normalization?

> Converting vendor-specific fields into a common structure.

### What is enrichment?

> Adding contextual information such as threat intelligence, asset criticality, GeoIP, or user information.

### What is a detection rule?

> Logic that identifies suspicious or security-relevant behavior from telemetry.

### What is a use case?

> A defined security monitoring objective implemented through telemetry, detection, alerting, investigation, and response.

### What is alert fatigue?

> Excessive low-value alerts that reduce analyst effectiveness.

### How do you reduce false positives?

> Improve context, thresholds, correlation, exceptions, enrichment, and behavioral analysis.

### What is threat hunting?

> Proactive, hypothesis-driven investigation for previously undetected threats.

### What is MITRE ATT&CK?

> A knowledge base describing adversary tactics and techniques used to model and improve threat-informed detection.

### What is SOAR?

> A platform for security orchestration, automation, and response.

### What is UEBA?

> Behavioral analytics for identifying anomalous activity involving users and entities.

### What is XDR?

> An integrated detection and response approach spanning multiple security domains.

### What is detection-as-code?

> Managing detection rules as version-controlled, testable software artifacts.

### What is RTO?

> Target time for restoring a service after disruption.

### What is RPO?

> Maximum acceptable data-loss window.

### What is EPS?

> Events Per Second.

### What is MTTD?

> Mean Time to Detect.

### What is MTTR?

> Mean Time to Respond or Resolve, depending on the organization's definition.

---

# 163. Top 20 SIEM Interview Questions

```text
1. What is SIEM?

2. What are the major components of a SIEM?

3. What is log normalization?

4. What is log parsing?

5. What is correlation?

6. How do you detect brute force?

7. How is password spraying different from brute force?

8. How do you detect compromised accounts?

9. How do you detect lateral movement?

10. How do you detect C2?

11. How do you reduce false positives?

12. What is MITRE ATT&CK?

13. What is threat hunting?

14. What is SOAR?

15. What is UEBA?

16. What is XDR?

17. How do you troubleshoot a detection that is not firing?

18. How do you optimize SIEM performance?

19. How do you monitor SIEM health?

20. How would you design a SIEM for a hybrid cloud environment?
```

---

# 164. Rapid Interview Answers

### Brute Force

```text
Many failed attempts
against one account
within a short time.
```

### Password Spraying

```text
Attempts against many
accounts from a common source.
```

### Lateral Movement

```text
Movement from one compromised
system/account to another.
```

### C2

```text
Communication between compromised
systems and attacker infrastructure.
```

### Exfiltration

```text
Unauthorized transfer of data
outside the environment.
```

### Persistence

```text
Techniques used to maintain
access after compromise.
```

### Privilege Escalation

```text
Obtaining higher privileges
than originally authorized.
```

### UEBA

```text
Detect deviations from
normal user/entity behavior.
```

### SOAR

```text
Automate security workflows
and response actions.
```

### Detection Engineering

```text
Design, test, deploy, tune,
and maintain security detections.
```

---

# 165. SIEM Architecture in One Diagram

```text
┌──────────────────────────────────────────────┐
│                 DATA SOURCES                 │
│ Windows │ Linux │ EDR │ DNS │ Firewall      │
│ Cloud   │ IAM   │ VPN │ Email │ Applications │
└───────────────────────┬──────────────────────┘
                        ↓
                 ┌──────────────┐
                 │  COLLECTORS  │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ TRANSPORT /  │
                 │    QUEUE     │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │   PARSING    │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ NORMALIZATION│
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │ ENRICHMENT   │
                 └──────┬───────┘
                        ↓
                 ┌──────────────┐
                 │   STORAGE    │
                 └──────┬───────┘
                        ↓
          ┌─────────────┼─────────────┐
          ↓             ↓             ↓
      DETECTION       UEBA            TI
          │             │             │
          └─────────────┼─────────────┘
                        ↓
                  CORRELATION
                        ↓
                      RISK
                        ↓
                     ALERT
                        ↓
                      SOC
                        ↓
                     SOAR
                        ↓
                    RESPONSE
```

---

# 166. Ultimate SIEM Mental Model

Remember:

```text
LOG
 ↓
FIELD
 ↓
NORMALIZE
 ↓
ENRICH
 ↓
SEARCH
 ↓
DETECT
 ↓
CORRELATE
 ↓
RISK
 ↓
ALERT
 ↓
TRIAGE
 ↓
INVESTIGATE
 ↓
RESPOND
 ↓
LEARN
 ↓
IMPROVE
```

---

# 167. SIEM Golden Rules

```text
1. A SIEM is only as good as its telemetry.

2. Missing logs create security blind spots.

3. Normalize data for reusable detections.

4. Enrich events with meaningful context.

5. Do not treat a single anomaly as proof of compromise.

6. Correlate multiple signals.

7. Use risk to prioritize.

8. Reduce alert fatigue aggressively but carefully.

9. Never disable noisy rules without investigation.

10. Treat detections as code.

11. Version-control detection logic.

12. Test positive and negative cases.

13. Monitor detection health.

14. Monitor ingestion health.

15. Design for peak EPS.

16. Plan for attack-driven log spikes.

17. Protect the SIEM itself.

18. Use least privilege.

19. Secure credentials and API keys.

20. Monitor cloud identity and API activity.

21. Map detections to relevant ATT&CK techniques.

22. Use threat intelligence as context.

23. Threat hunting should feed detection engineering.

24. SOAR should automate repeatable workflows.

25. High-impact automation needs safeguards.

26. AI should assist analysts, not replace evidence.

27. Validate AI-generated conclusions.

28. Keep humans involved in high-impact decisions.

29. Test disaster recovery.

30. Measure MTTD and MTTR.

31. Measure precision and recall where possible.

32. Measure detection coverage.

33. Continuously tune and improve.

34. The goal is actionable security intelligence—not maximum alert volume.
```

---

# 168. Final SIEM Cheat Code

When you see any SIEM problem, think:

```text
SOURCE
 ↓
DATA
 ↓
FIELD
 ↓
CONTEXT
 ↓
BEHAVIOR
 ↓
CORRELATION
 ↓
RISK
 ↓
ALERT
 ↓
INVESTIGATION
 ↓
RESPONSE
```

For any suspicious event, ask:

```text
WHO?
WHAT?
WHEN?
WHERE?
HOW?
WHY?
SCOPE?
RISK?
EVIDENCE?
NEXT ACTION?
```

For any detection failure, ask:

```text
DATA?
PARSER?
SCHEMA?
FIELD?
QUERY?
THRESHOLD?
CORRELATION?
ENGINE?
ALERT?
```

For any SOC improvement:

```text
DETECT BETTER
+
INVESTIGATE FASTER
+
AUTOMATE SAFELY
+
LEARN CONTINUOUSLY
```

---

# 169. Final Revision Map

```text
SIEM FUNDAMENTALS
        ↓
LOGGING
        ↓
PARSING
        ↓
NORMALIZATION
        ↓
ENRICHMENT
        ↓
SEARCH
        ↓
DETECTION ENGINEERING
        ↓
CORRELATION
        ↓
RISK
        ↓
THREAT INTELLIGENCE
        ↓
MITRE ATT&CK
        ↓
THREAT HUNTING
        ↓
INVESTIGATION
        ↓
INCIDENT RESPONSE
        ↓
SIEM ENGINEERING
        ↓
CLOUD SECURITY
        ↓
SOAR
        ↓
UEBA
        ↓
XDR
        ↓
AI-ASSISTED SOC
```

---

# 170. Final Takeaway

The entire SIEM domain can be reduced to five questions:

```text
1. Are we collecting the right data?

2. Can we understand and normalize that data?

3. Can we detect meaningful malicious behavior?

4. Can analysts investigate and respond efficiently?

5. Can the SOC continuously improve?
```

The ultimate SIEM objective is:

```text
Reliable Telemetry
        +
High-Quality Detection
        +
Useful Context
        +
Fast Investigation
        +
Controlled Automation
        +
Continuous Improvement
        =
Effective Security Operations
```

> **A mature SIEM does not simply tell the SOC that something happened. It helps the SOC understand what happened, why it matters, what is affected, how confident the organization should be, and what should happen next.**