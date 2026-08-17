# Chapter 09 – Detection Engineering for Endpoint, Network & Identity

> Endpoint, network, and identity telemetry form three of the most important pillars of modern security detection. Endpoint data reveals what processes and files are doing, network data reveals how systems communicate, and identity data reveals who is accessing what. Combining all three creates stronger, context-rich detections capable of identifying attacks across the full lifecycle.

---

# 1. Introduction

Modern attacks rarely remain inside a single security layer.

A typical attack may look like:

```text
Identity
   ↓
Endpoint
   ↓
Network
   ↓
Identity
   ↓
Another Endpoint
```

For example:

```text
Compromised Account
      ↓
Login from New Device
      ↓
Suspicious Process
      ↓
External C2
      ↓
Credential Access
      ↓
Lateral Movement
```

A mature detection program therefore needs visibility across:

```text
Endpoint
Network
Identity
```

---

# 2. The Three Detection Pillars

## Endpoint

Answers:

```text
What happened on the machine?
```

## Network

Answers:

```text
Where did the machine communicate?
```

## Identity

Answers:

```text
Who performed the activity?
```

Together:

```text
WHO
 +
WHAT
 +
WHERE
 +
WHEN
 +
WHY
```

---

# 3. Endpoint Detection Engineering

Endpoint detection focuses on activity occurring on:

```text
Workstations
Servers
Laptops
Virtual Machines
Cloud Instances
Containers
```

Common telemetry:

```text
Process Creation
Process Termination
Command Line
File Activity
Registry
Services
Scheduled Tasks
User Sessions
Network Connections
Security Events
```

---

# 4. Endpoint Detection Sources

Common sources include:

```text
EDR
Operating System Logs
Windows Event Logs
Linux Audit Logs
Sysmon
Endpoint Agents
File Monitoring
Application Logs
```

The exact data available depends on the platform.

---

# 5. Process Creation

Process creation is one of the most valuable endpoint signals.

Useful fields:

```text
Process Name
Process ID
Parent Process
Parent PID
Command Line
Executable Path
Hash
User
Integrity Level
Signer
Timestamp
```

---

# 6. Process Tree

Example:

```text
explorer.exe
   └── winword.exe
        └── powershell.exe
             └── unknown.exe
```

The process tree provides execution context.

A detection should often consider:

```text
Parent
Child
Grandparent
Arguments
User
Path
Network
```

---

# 7. Parent-Child Detection

Example:

```text
Office Application
        ↓
Script Interpreter
```

Potentially suspicious depending on context.

Additional context:

```text
Document
User
Command Line
Network Connection
File Creation
```

can increase confidence.

---

# 8. Command-Line Detection

Command lines may contain:

```text
URLs
Encoded Data
File Paths
Scripts
Administrative Commands
Download Locations
Execution Parameters
```

Example:

```text
powershell.exe
+
suspicious command
+
external destination
```

is stronger than process name alone.

---

# 9. Command-Line Normalization

Command lines may vary because of:

```text
Whitespace
Case
Quoting
Encoding
Argument Order
Aliases
```

Detection logic should avoid unnecessary dependence on superficial formatting.

---

# 10. File Activity

Important file events:

```text
Create
Modify
Rename
Delete
Execute
Read
Write
```

Useful context:

```text
Process
User
Path
Hash
Extension
Parent Process
```

---

# 11. Suspicious File Creation

Example:

```text
Document Reader
      ↓
Creates Executable
      ↓
Executes It
```

This may be suspicious depending on application behavior.

---

# 12. Persistence Detection

Endpoint persistence can involve:

```text
Scheduled Tasks
Services
Startup Items
Registry
Login Scripts
New Accounts
Configuration Changes
```

Detection should identify:

```text
Who
What
Where
When
Process
Context
```

---

# 13. Scheduled Task Detection

A useful detection can consider:

```text
Task Created
+
Unexpected User
+
Suspicious Command
+
Unusual Location
```

Avoid:

```text
Alert on every scheduled task
```

because legitimate administration generates many tasks.

---

# 14. Service Creation Detection

Potential signals:

```text
New Service
+
Unexpected Binary
+
Unsigned Executable
+
Suspicious Path
+
Remote Creation
```

---

# 15. Registry Detection

Useful for:

```text
Persistence
Security Configuration Changes
Execution
System Modification
```

Detection should focus on meaningful registry locations and behavior rather than generating alerts for all changes.

---

# 16. Credential Access Detection

Endpoint signals can include:

```text
Sensitive Process Access
Credential Store Access
Memory Access
Security Tool Interaction
Authentication Artifacts
```

Context is critical because legitimate security and administrative software may perform similar actions.

---

# 17. Defense Evasion Detection

Look for:

```text
Security Service Modification
Log Clearing
Security Tool Tampering
Process Termination
Configuration Changes
File Deletion
```

---

# 18. Discovery Detection

Endpoint discovery behaviors include:

```text
System Information
User Enumeration
Process Enumeration
Network Configuration
Service Enumeration
Installed Software
```

Single discovery commands may be normal.

A burst of discovery activity can be more meaningful.

---

# 19. Endpoint Discovery Sequence

Example:

```text
System Discovery
      ↓
User Discovery
      ↓
Network Discovery
      ↓
Service Discovery
```

Same:

```text
Host
User
Process
```

within a short period can increase suspicion.

---

# 20. Endpoint Network Connections

Process-level network telemetry can connect:

```text
Process
+
Destination
+
Port
+
Protocol
+
User
```

Example:

```text
Suspicious Process
      ↓
External Destination
```

This provides stronger context than a network event alone.

---

# 21. Endpoint Detection Example

```text
Office Application
      ↓
Script Interpreter
      ↓
Creates Executable
      ↓
External Connection
```

Potential:

```text
High-Confidence Suspicious Execution
```

---

# 22. Network Detection Engineering

Network detection focuses on:

```text
Connections
DNS
Protocols
Traffic
Destinations
Ports
Certificates
Network Flows
```

---

# 23. Network Telemetry Sources

Common sources:

```text
Firewall
Proxy
DNS
NetFlow
NDR
IDS/IPS
VPN
Load Balancer
Cloud Network Logs
TLS Metadata
```

---

# 24. Network Flow Data

Common fields:

```text
Source IP
Destination IP
Source Port
Destination Port
Protocol
Bytes
Packets
Start Time
End Time
Direction
```

Flow data provides metadata rather than full content.

---

# 25. DNS Detection

Useful signals:

```text
Rare Domain
New Domain
High Query Frequency
Unusual Query Length
Suspicious TLD
High Entropy
Large Number of Subdomains
Periodic Queries
```

None of these alone proves malicious activity.

---

# 26. Domain Rarity

Example:

```text
Corporate Environment:
1000 Hosts

Domain:
contacted by only 1 Host
```

This can be a useful signal.

Combine with:

```text
Process
User
Timing
Threat Intelligence
```

---

# 27. DNS Burst

Example:

```text
Host
 ↓
500 DNS Queries
 ↓
100 Unique Domains
 ↓
5 Minutes
```

Potential:

```text
Reconnaissance
Malware
Browser Activity
Software Update
```

Context determines interpretation.

---

# 28. DNS Beaconing

Potential pattern:

```text
Query
10:00

Query
10:05

Query
10:10

Query
10:15
```

Periodic behavior can indicate automation or C2.

---

# 29. Network Beaconing

Beaconing can be characterized by:

```text
Frequency
Periodicity
Destination
Bytes
Jitter
Protocol
Process
```

---

# 30. Beaconing Detection

A stronger signal:

```text
Periodic Connection
+
Rare Destination
+
Unusual Process
+
Small Repeated Payload
```

---

# 31. Network Scanning

Potential indicators:

```text
One Source
+
Many Destination Hosts
+
Many Ports
+
Short Time Window
```

Example:

```text
Host A
 ↓
Host B: 22
Host C: 22
Host D: 22
Host E: 22
```

---

# 32. Port Scanning

Possible behavior:

```text
Single Source
+
Many Destination Ports
```

But legitimate vulnerability scanners and monitoring systems can create similar patterns.

---

# 33. Network Service Discovery

Example:

```text
Host
 ↓
Multiple Internal Hosts
 ↓
Common Administrative Ports
```

Potential:

```text
Lateral Movement Preparation
```

---

# 34. Lateral Movement Detection

Useful network signals:

```text
New Internal Connection
Remote Service
Administrative Protocol
New Source-Destination Relationship
Privileged Account
```

---

# 35. Internal Relationship Modeling

Build expected relationships:

```text
Admin Workstation
→
Server Cluster
```

Then identify:

```text
Developer Laptop
→
Domain Controller
```

as potentially unusual.

---

# 36. Network Segmentation Detection

A connection that crosses unexpected security boundaries may deserve attention.

Example:

```text
User VLAN
      ↓
Database VLAN
```

when the user normally has no direct access.

---

# 37. Egress Detection

Monitor:

```text
Internal Host
      ↓
External Destination
```

especially when:

```text
Destination is Rare
Process is Suspicious
Data Volume is Unusual
```

---

# 38. Data Exfiltration Detection

Potential signals:

```text
Large Outbound Transfer
+
Sensitive Resource
+
Rare Destination
+
Unusual Time
```

---

# 39. Exfiltration Baseline

A server may normally transfer:

```text
100 GB/day
```

while a workstation normally transfers:

```text
500 MB/day
```

Therefore thresholds should be entity-aware.

---

# 40. Network Protocol Detection

Monitor unusual protocol behavior:

```text
Unexpected Protocol
Unexpected Port
Protocol Mismatch
Encrypted Traffic Anomaly
Unexpected Remote Service
```

Avoid assuming:

```text
Port = Protocol
```

because applications can use non-standard ports.

---

# 41. TLS Detection

Useful metadata may include:

```text
Certificate
Server Name
TLS Version
Handshake Metadata
Connection Timing
Destination
```

Encrypted traffic limits content inspection but does not eliminate metadata-based detection.

---

# 42. Certificate Detection

Potential signals:

```text
Rare Certificate
Recently Seen Certificate
Unexpected Issuer
Certificate Reuse
Suspicious Domain Association
```

Certificate data should be interpreted in context.

---

# 43. Identity Detection Engineering

Identity detection focuses on:

```text
Authentication
Authorization
Accounts
Sessions
MFA
Privileges
Roles
Access
```

---

# 44. Identity Telemetry

Useful sources:

```text
Identity Provider
Directory Services
SSO
MFA
VPN
Cloud IAM
Application Authentication
Privileged Access Management
```

---

# 45. Authentication Events

Important fields:

```text
User
Source IP
Device
Location
Authentication Method
MFA Result
Application
Timestamp
Result
Session
```

---

# 46. Failed Authentication

One failed login:

```text
Usually Low Signal
```

Many failures:

```text
Potentially More Significant
```

Example:

```text
20 Failures
+
1 Success
```

requires investigation depending on context.

---

# 47. Password Spraying

Conceptual pattern:

```text
One Source
 ↓
Many Users
 ↓
Few Password Attempts per User
```

This differs from:

```text
Brute Force
```

which commonly focuses many attempts against one account.

---

# 48. Brute Force

Conceptually:

```text
One Account
+
Many Authentication Attempts
```

Potential detection:

```text
Count
+
Time Window
+
Source
```

---

# 49. Credential Stuffing

Potential pattern:

```text
Many Accounts
+
Known Credential Attempts
+
External Source
```

Identity detection should consider:

```text
Source Reputation
Device
Location
Application
Success Rate
```

---

# 50. Successful Login After Failures

A useful sequence:

```text
Multiple Failed Attempts
      ↓
Successful Authentication
```

Risk can increase if followed by:

```text
New Device
MFA Change
Sensitive Access
```

---

# 51. Impossible Travel

Conceptually:

```text
Login A:
Location X

Shortly After:

Login B:
Location Y

Physical travel impossible
```

This can be a signal.

But VPNs, proxies, mobile networks, and cloud infrastructure can create misleading location information.

---

# 52. New Device Detection

Signals:

```text
User
+
Previously Unknown Device
+
Sensitive Application
```

This is not inherently malicious.

Add:

```text
Unusual Location
+
Risky Authentication
+
Privilege
```

for stronger detection.

---

# 53. MFA Detection

Monitor:

```text
MFA Disabled
MFA Reset
New Factor
New Device
Recovery Method Change
MFA Failure Burst
```

---

# 54. MFA Fatigue

Potential pattern:

```text
Many MFA Requests
      ↓
User Approves
      ↓
Successful Login
```

This can indicate an attempted authentication attack.

---

# 55. Privilege Change Detection

Monitor:

```text
Role Change
Group Membership
Admin Assignment
IAM Policy Change
Permission Grant
Delegation
```

---

# 56. Privilege Escalation Sequence

Example:

```text
Normal User
      ↓
Role Change
      ↓
Administrative Login
      ↓
Sensitive Resource Access
```

---

# 57. Account Creation Detection

Monitor:

```text
New Account
+
Privileged Role
+
Unusual Creator
```

Potential persistence.

---

# 58. Service Account Detection

Service accounts may behave differently from human users.

Baseline:

```text
Expected Applications
Expected Hosts
Expected Times
Expected APIs
```

A service account suddenly performing interactive authentication may be suspicious.

---

# 59. Dormant Account Detection

Potential:

```text
Dormant Account
      ↓
Sudden Login
      ↓
Sensitive Access
```

This is a useful identity signal.

---

# 60. Privileged Account Detection

High-value accounts include:

```text
Domain Admin
Cloud Admin
Root
Security Admin
Database Admin
```

Behavior involving these identities should receive stronger contextual weighting.

---

# 61. Identity + Endpoint Correlation

Example:

```text
User Login
      ↓
New Device
      ↓
Suspicious Process
```

This is stronger than any single signal.

---

# 62. Identity + Network Correlation

Example:

```text
Privileged Login
      ↓
New Internal Host
      ↓
Remote Service
```

Potential lateral movement.

---

# 63. Identity + Cloud Correlation

Example:

```text
New Device
      ↓
Cloud Login
      ↓
Access Key Creation
      ↓
Privilege Change
```

Potential account takeover.

---

# 64. Endpoint + Network Correlation

Example:

```text
Suspicious Process
      ↓
Rare External Destination
      ↓
Periodic Connection
```

Potential C2.

---

# 65. Endpoint + Identity + Network

A powerful detection:

```text
User:
Alice

↓ Login from New Device

Endpoint:
Suspicious Process

↓ Network

Rare External Domain

↓ Identity

Sensitive Resource Access
```

Potential:

```text
High-Confidence Account + Endpoint Compromise
```

---

# 66. Detection Across Attack Stages

A mature detection program covers:

```text
Initial Access
Execution
Persistence
Credential Access
Discovery
Lateral Movement
Collection
C2
Exfiltration
Impact
```

---

# 67. Endpoint Detection by ATT&CK Stage

Example:

```text
Execution
→ Process / Command Line

Persistence
→ Services / Scheduled Tasks

Credential Access
→ Credential Access Behavior

Discovery
→ Enumeration

Lateral Movement
→ Remote Execution
```

---

# 68. Network Detection by ATT&CK Stage

Example:

```text
Recon
→ Scanning

C2
→ Beaconing

Lateral Movement
→ Remote Connections

Exfiltration
→ Unusual Outbound Transfer
```

---

# 69. Identity Detection by ATT&CK Stage

Example:

```text
Initial Access
→ Suspicious Authentication

Credential Access
→ Authentication Abuse

Privilege Escalation
→ Role Change

Lateral Movement
→ New Remote Authentication
```

---

# 70. Detection Data Quality

Detection quality depends on:

```text
Completeness
Accuracy
Consistency
Timestamp Quality
Entity Resolution
Field Normalization
Retention
```

---

# 71. Missing Endpoint Telemetry

If process creation is missing:

```text
Endpoint Detection
```

may be severely limited.

Possible action:

```text
Improve EDR
Improve Logging
Deploy Additional Telemetry
```

---

# 72. Missing Network Telemetry

Without DNS or flow visibility:

```text
C2 Detection
```

may become difficult.

---

# 73. Missing Identity Telemetry

Without authentication and privilege logs:

```text
Account Takeover
Privilege Abuse
Lateral Movement
```

detections become weaker.

---

# 74. Telemetry Normalization

Different sources may use different fields.

Example:

```text
user
username
account
principal
```

Normalize them to a common representation.

---

# 75. Endpoint Normalization

Normalize:

```text
Process Name
Path
Hash
User
Host
Timestamp
Network Destination
```

---

# 76. Network Normalization

Normalize:

```text
Source IP
Destination IP
Port
Protocol
DNS Name
Bytes
Direction
Timestamp
```

---

# 77. Identity Normalization

Normalize:

```text
User ID
Account Name
Role
Device ID
Source IP
Application
Authentication Method
```

---

# 78. Entity Resolution

Map:

```text
Alice
alice@example.com
CORP\alice
```

to:

```text
Canonical User:
alice
```

Similarly:

```text
server01
server01.example.com
10.0.0.10
```

may map to one asset.

---

# 79. Detection Logic Should Be Context-Aware

Avoid:

```text
Alert on any admin login.
```

Prefer:

```text
Admin login
+
New Device
+
Unusual Location
+
Sensitive Resource Access
```

---

# 80. Threshold Detection

Examples:

```text
10 failed logins / 5 minutes
```

```text
50 unique destinations / 1 minute
```

```text
1000 file modifications / 5 minutes
```

Thresholds should be validated against baseline behavior.

---

# 81. Dynamic Thresholds

Static:

```text
> 100 events
```

Dynamic:

```text
> 5 × normal baseline
```

Dynamic thresholds can adapt to different entities.

---

# 82. Peer-Based Thresholds

Compare:

```text
User A
```

with:

```text
Users in Same Role
```

or:

```text
Server A
```

with:

```text
Servers of Same Type
```

---

# 83. Endpoint Detection Example

```text
IF

process.parent = office_application

AND

process.name = script_interpreter

AND

network.destination = external

AND

destination_rarity = high

THEN

generate_detection
```

Exact implementation should use normalized telemetry and environment-specific tuning.

---

# 84. Network Detection Example

```text
IF

source.host

connects_to

many_unique_destinations

WITHIN

5_minutes

AND

destination_ports

are_restricted

THEN

potential_scanning
```

Exclude authorized scanners.

---

# 85. Identity Detection Example

```text
IF

failed_logins >= threshold

AND

successful_login = true

AND

new_device = true

WITHIN

15_minutes

THEN

increase_user_risk
```

---

# 86. Cross-Domain Detection Example

```text
IF

new_device_login

AND

suspicious_process

AND

rare_external_connection

THEN

high_confidence_compromise
```

---

# 87. Detection Exceptions

Exceptions should be:

```text
Specific
Documented
Reviewed
Time-Bounded
Auditable
```

Avoid:

```text
Ignore Entire Host
```

when a narrower exception is possible.

---

# 88. Authorized Scanners

Security scanners may generate:

```text
Port Scans
Vulnerability Probes
Authentication Attempts
```

Detection should identify known scanner context rather than disabling scanning detections globally.

---

# 89. Administrative Activity

Administrators may generate:

```text
Remote Logins
PowerShell
Service Creation
Privilege Changes
```

Use:

```text
User Role
Host
Time
Change Ticket
Tool
```

to distinguish expected activity.

---

# 90. Endpoint Detection Performance

Consider:

```text
Event Volume
CPU
Memory
Query Cost
Storage
Latency
```

High-volume telemetry requires efficient filtering.

---

# 91. Network Detection Performance

Expensive operations include:

```text
Large Joins
High-Cardinality Aggregations
Long Time Windows
Deep Packet Analysis
Complex Regex
```

Optimize carefully.

---

# 92. Identity Detection Performance

High-cardinality fields:

```text
User
Device
Application
IP
Session
```

can create large state spaces.

Use:

```text
Pre-Aggregation
Filtering
Reasonable Windows
```

---

# 93. Detection Testing

Test:

```text
Positive Case
Negative Case
Edge Case
Boundary
Missing Data
Duplicate Data
Delayed Data
Alternative Procedure
```

---

# 94. Endpoint Positive Test

Example:

```text
Suspicious Process Chain
```

Expected:

```text
Detection Fires
```

---

# 95. Network Positive Test

Example:

```text
Controlled Scan Simulation
```

Expected:

```text
Scanning Detection
```

---

# 96. Identity Positive Test

Example:

```text
Controlled Authentication Anomaly
```

Expected:

```text
Identity Detection
```

---

# 97. Negative Testing

Ensure:

```text
Normal Admin Activity
Normal Backup
Normal Software Update
Normal Monitoring
Normal Scanner
```

does not create unacceptable alert noise.

---

# 98. Detection Validation

Measure:

```text
Did the telemetry arrive?
Did the detection trigger?
How quickly?
Was the alert accurate?
Was the context useful?
```

---

# 99. Detection Latency

Measure:

```text
Event Time
   ↓
Telemetry Arrival
   ↓
Detection
   ↓
Alert
```

Track each stage separately.

---

# 100. Endpoint Detection Latency

Important for:

```text
Ransomware
Malware Execution
Credential Theft
Persistence
```

---

# 101. Network Detection Latency

Important for:

```text
C2
Exfiltration
Scanning
Lateral Movement
```

---

# 102. Identity Detection Latency

Important for:

```text
Account Takeover
MFA Abuse
Privilege Escalation
Suspicious Authentication
```

---

# 103. Detection Quality Metrics

Track:

```text
True Positives
False Positives
False Negatives
Precision
Recall
Alert Volume
Detection Latency
Analyst Acceptance
```

---

# 104. Detection Coverage Matrix

| Domain | Telemetry | Detection | Testing | Coverage |
|---|---|---|---|---|
| Endpoint | Yes | Yes | Yes | High |
| Network | Yes | Partial | Yes | Medium |
| Identity | Yes | Yes | No | Medium |

---

# 105. Cross-Domain Coverage

A mature program should evaluate:

```text
Endpoint
Network
Identity
```

individually and together.

Example:

```text
Endpoint Coverage: High
Network Coverage: High
Identity Coverage: High

Cross-Domain Correlation: Low
```

This is still a detection gap.

---

# 106. Detection Maturity

### Level 1

Basic logs:

```text
Endpoint
Network
Identity
```

### Level 2

Individual detections.

### Level 3

Contextual detections.

### Level 4

Cross-domain correlation.

### Level 5

Risk-based detection.

### Level 6

Threat-informed adaptive detection.

---

# 107. Common Endpoint Mistakes

```text
Alerting on every script execution
Ignoring process ancestry
Ignoring command line
Ignoring user context
Ignoring signed software
Ignoring legitimate administration
```

---

# 108. Common Network Mistakes

```text
Treating every rare domain as malicious
Ignoring authorized scanners
Using only IP reputation
Ignoring encrypted traffic metadata
Using static thresholds everywhere
```

---

# 109. Common Identity Mistakes

```text
Alerting on every failed login
Ignoring service accounts
Ignoring VPNs
Ignoring MFA workflows
Ignoring role context
Ignoring device context
```

---

# 110. Cross-Domain Mistakes

```text
Not resolving identities
Not resolving assets
Using inconsistent timestamps
Ignoring data source delays
Correlating unrelated events
Counting duplicate evidence
```

---

# 111. Practical Exercise – Endpoint

Build a detection hypothesis:

```text
Office Application
→ Script Interpreter
→ External Connection
```

Document:

```text
Telemetry
Fields
False Positives
Positive Test
Negative Test
ATT&CK Mapping
```

---

# 112. Practical Exercise – Network

Build:

```text
Single Host
→ Many Destinations
→ Short Time Window
```

Document:

```text
Expected Scanner Activity
Threshold
Exception Strategy
Positive Test
Negative Test
```

---

# 113. Practical Exercise – Identity

Build:

```text
Failed Authentication Burst
→ Successful Login
→ New Device
→ Sensitive Access
```

Document:

```text
Correlation Key
Time Window
Risk
Severity
False Positives
```

---

# 114. Practical Exercise – Cross-Domain

Build:

```text
New Device Login
      ↓
Suspicious Process
      ↓
Rare External Destination
      ↓
Sensitive Resource Access
```

Map:

```text
Identity
Endpoint
Network
Application
```

---

# 115. Detection Design Template

```yaml
id: DET-ENDPOINT-001

name: Suspicious Process and Network Activity

description: >
  Detects suspicious process behavior followed by
  an unusual external network connection.

domains:
  - endpoint
  - network

entities:
  - user
  - host
  - process

telemetry:
  - process_creation
  - network_connection

conditions:
  - suspicious_parent
  - unusual_command_line
  - rare_external_destination

window:
  minutes: 10

severity: high

confidence: medium

tests:
  - positive_case
  - negative_case
  - evasion_case

status: production
```

---

# 116. Detection Checklist

```text
[ ] Endpoint telemetry available
[ ] Network telemetry available
[ ] Identity telemetry available
[ ] Fields normalized
[ ] Users resolved
[ ] Hosts resolved
[ ] Process relationships available
[ ] Network relationships available
[ ] Authentication context available
[ ] Detection hypothesis documented
[ ] Correlation key defined
[ ] Time window defined
[ ] Threshold validated
[ ] False positives identified
[ ] Exceptions documented
[ ] Positive test created
[ ] Negative test created
[ ] Evasion test created
[ ] Performance tested
[ ] Detection latency measured
[ ] ATT&CK mapping completed
[ ] Owner assigned
```

---

# 117. Interview Questions

### What are the three major detection domains covered in this chapter?

> Endpoint, network, and identity.

### Why is endpoint telemetry important?

> It reveals process, file, execution, persistence, and host-level activity.

### Why is network telemetry important?

> It reveals communication patterns, destinations, protocols, scanning, C2, lateral movement, and potential exfiltration.

### Why is identity telemetry important?

> It provides information about who authenticated, from where, using what device or method, and what privileges or resources were involved.

### What is a process tree?

> A representation of parent-child process relationships that provides execution context.

### Why is PowerShell execution alone usually insufficient for a high-confidence detection?

> PowerShell is a legitimate administrative and automation tool, so additional context such as parent process, command line, user, host, and network behavior is needed.

### What is password spraying?

> Attempting a small number of passwords across many accounts rather than repeatedly targeting one account.

### What is the difference between brute force and password spraying?

> Brute force commonly targets one account with many guesses, while password spraying distributes a small number of guesses across many accounts.

### What is impossible travel?

> A detection signal where authentication events appear to originate from geographically distant locations within an unrealistically short period.

### Why can impossible-travel detections generate false positives?

> VPNs, proxies, mobile networks, cloud services, and inaccurate geolocation can make legitimate activity appear geographically impossible.

### How do you detect lateral movement?

> Correlate unusual internal authentication, remote service activity, source-destination relationships, privileged accounts, and endpoint/network behavior.

### How do you improve endpoint detection?

> Use process ancestry, command-line context, file behavior, user identity, network activity, baselines, and behavioral correlation.

### How do you improve network detection?

> Combine flow, DNS, destination rarity, timing, protocol, process context, threat intelligence, and behavioral patterns.

### How do you improve identity detection?

> Combine authentication, device, location, MFA, privilege, application, historical behavior, and resource-access context.

---

# 118. Quick Revision

```text
Endpoint Detection
→ Detect host and process behavior

Network Detection
→ Detect communication behavior

Identity Detection
→ Detect authentication and access behavior

Process Tree
→ Parent-child execution relationship

Command Line
→ Process execution arguments

Network Flow
→ Connection metadata

DNS Detection
→ Domain resolution behavior

Beaconing
→ Repeated periodic communication

Scanning
→ Many destinations/ports in a short period

Password Spraying
→ Few attempts across many accounts

Brute Force
→ Many attempts against one account

Credential Stuffing
→ Reused credentials across many accounts

MFA Fatigue
→ Repeated MFA requests intended to induce approval

Privilege Change
→ Modification of account permissions/roles

Entity Resolution
→ Mapping different identifiers to the same entity

Cross-Domain Detection
→ Correlating identity + endpoint + network

Dynamic Threshold
→ Threshold based on behavioral baseline

Detection Latency
→ Time from activity to actionable detection
```

---

# 119. Golden Rules

```text
1. Endpoint tells you what happened.

2. Network tells you where communication occurred.

3. Identity tells you who performed the activity.

4. Use all three together whenever useful.

5. Process ancestry is often more informative than process name alone.

6. Command-line context matters.

7. Legitimate tools can be abused.

8. Rare does not automatically mean malicious.

9. New does not automatically mean malicious.

10. Baselines should be entity-aware.

11. Service accounts need separate behavioral expectations.

12. Privileged identities deserve stronger contextual weighting.

13. Network detections should account for legitimate scanners.

14. DNS detections should account for legitimate automation.

15. Identity detections should account for VPN and proxy behavior.

16. Do not assume ports uniquely identify protocols.

17. Normalize telemetry before cross-source correlation.

18. Resolve identities consistently.

19. Resolve hosts consistently.

20. Account for event and ingestion timestamps.

21. Test positive and negative cases.

22. Test delayed and missing telemetry.

23. Test alternative attacker procedures.

24. Measure detection latency.

25. Measure precision and recall where possible.

26. Avoid broad exceptions.

27. Keep exceptions documented and auditable.

28. Use threat intelligence as context rather than absolute truth.

29. Cross-domain correlation can produce significantly stronger detections.

30. The strongest detection answers:
    WHO + WHAT + WHERE + WHEN + CONTEXT.
```

---

# 120. Final Mental Model

A mature detection should connect:

```text
IDENTITY
   │
   │ Who?
   ↓
ENDPOINT
   │
   │ What happened?
   ↓
NETWORK
   │
   │ Where did it communicate?
   ↓
APPLICATION / CLOUD
   │
   │ What resource was accessed?
   ↓
CORRELATION
   │
   ↓
RISK
   │
   ↓
ACTIONABLE ALERT
```

For example:

```text
User
 ↓
New Device Login
 ↓
Suspicious Process
 ↓
Rare External Connection
 ↓
Sensitive Resource Access
 ↓
Elevated Risk
 ↓
SOC Investigation
```

The complete detection model is:

```text
WHO
 +
WHAT
 +
WHERE
 +
WHEN
 +
HOW
 +
CONTEXT
      ↓
CORRELATION
      ↓
RISK
      ↓
DETECTION
      ↓
RESPONSE
```

---

# 121. Chapter Summary

This chapter covered:

```text
Endpoint Detection Engineering
Network Detection Engineering
Identity Detection Engineering
Process Creation
Process Trees
Command Lines
File Activity
Persistence
Credential Access
Defense Evasion
Discovery
Endpoint Network Connections
DNS Detection
Domain Rarity
DNS Beaconing
Network Beaconing
Scanning
Port Scanning
Lateral Movement
Network Segmentation
Egress Detection
Exfiltration
TLS Metadata
Authentication
Password Spraying
Brute Force
Credential Stuffing
Impossible Travel
New Device Detection
MFA Abuse
Privilege Changes
Account Creation
Service Accounts
Dormant Accounts
Cross-Domain Correlation
Entity Resolution
Telemetry Normalization
Dynamic Thresholds
Peer Baselines
Detection Testing
Detection Latency
Detection Quality
Coverage
Detection Maturity
```

The central principle is:

> **Endpoint, network, and identity telemetry provide different perspectives of the same attack. Endpoint data shows what happened, network data shows where communication occurred, and identity data shows who performed the activity. The strongest detections combine these perspectives to transform isolated events into a coherent security story.**

The next chapter moves into **Cloud, Application & Container Detection**, extending detection engineering beyond traditional endpoints and networks into modern infrastructure, APIs, Kubernetes, containers, SaaS, and cloud-native environments.