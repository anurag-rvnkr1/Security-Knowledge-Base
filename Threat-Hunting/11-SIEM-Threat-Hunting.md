# SIEM Threat Hunting

## Overview

A Security Information and Event Management (SIEM) platform is one of the primary analytical systems used by modern Security Operations Centers.

A SIEM centralizes security telemetry from multiple sources and enables security teams to:

- Search events
- Correlate activity
- Detect threats
- Investigate incidents
- Hunt for adversary behavior
- Build dashboards
- Generate alerts
- Support incident response
- Maintain security visibility

A SIEM is not automatically a threat-hunting platform simply because it stores logs.

The value comes from how effectively analysts transform raw telemetry into:

```text
Raw Events
    │
    ▼
Normalized Data
    │
    ▼
Context
    │
    ▼
Hypotheses
    │
    ▼
Queries
    │
    ▼
Correlation
    │
    ▼
Investigation
    │
    ▼
Detection
```

The core principle is:

> **A SIEM should help the hunter connect seemingly unrelated events into a coherent security story.**

---

# Why SIEM Threat Hunting Matters

Enterprise environments generate enormous amounts of telemetry.

Examples include:

```text
Endpoints
Servers
Firewalls
DNS
VPN
Identity
Cloud
Applications
Databases
Email
Web Proxies
EDR
Network Sensors
Containers
Kubernetes
```

Without centralized analysis:

```text
Endpoint Logs ──────┐
DNS Logs ───────────┤
Firewall Logs ──────┤
Identity Logs ──────┼──► Analyst
Cloud Logs ─────────┤
EDR Logs ───────────┘
```

The analyst must manually correlate everything.

A SIEM provides:

```text
Multiple Sources
      │
      ▼
Central Collection
      │
      ▼
Normalization
      │
      ▼
Search
      │
      ▼
Correlation
      │
      ▼
Detection
```

---

# SIEM Architecture

A typical enterprise SIEM architecture looks like:

```text
                     DATA SOURCES
                         │
       ┌─────────────────┼─────────────────┐
       │                 │                 │
       ▼                 ▼                 ▼
    Endpoint           Network           Identity
       │                 │                 │
       ├───────┐   ┌─────┴─────┐   ┌──────┘
       │       │   │           │   │
       ▼       ▼   ▼           ▼   ▼
      EDR     DNS Firewall    VPN  IAM
       │       │     │         │    │
       └───────┴─────┴─────────┴────┘
                         │
                         ▼
                   Log Collection
                         │
                         ▼
                  Parsing / Parsing
                         │
                         ▼
                    Normalization
                         │
                         ▼
                   Enrichment
                         │
                         ▼
                      SIEM
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Search      Detection    Dashboard
             │           │           │
             └───────────┼───────────┘
                         ▼
                       SOC
```

---

# SIEM Core Functions

A SIEM typically provides:

## Collection

Gather telemetry from multiple systems.

## Parsing

Extract fields from raw events.

## Normalization

Map different vendor formats into consistent fields.

## Enrichment

Add:

- Asset information
- User information
- Threat intelligence
- GeoIP
- Business criticality
- Identity context

## Search

Allow analysts to investigate historical and real-time data.

## Correlation

Connect related events.

## Detection

Generate alerts from suspicious patterns.

## Visualization

Provide dashboards and investigation views.

---

# SIEM vs Threat Hunting

These concepts should not be confused.

```text
SIEM
 │
 ├── Collection
 ├── Search
 ├── Correlation
 ├── Detection
 └── Visualization
```

Threat hunting is an analytical process:

```text
Question
   │
   ▼
Hypothesis
   │
   ▼
Data
   │
   ▼
Query
   │
   ▼
Analysis
   │
   ▼
Conclusion
```

The SIEM is one of the primary tools used to execute that process.

---

# SIEM Data Pipeline

```text
Source
  │
  ▼
Collector
  │
  ▼
Parser
  │
  ▼
Normalizer
  │
  ▼
Enrichment
  │
  ▼
Storage
  │
  ▼
Search
  │
  ▼
Detection
```

Each stage can introduce problems.

---

# Log Collection

Sources may send logs using:

- Syslog
- Agents
- APIs
- Message queues
- Cloud connectors
- Webhooks
- Forwarders
- Event streaming

Common protocols and mechanisms include:

```text
Syslog
Windows Event Forwarding
Beats
Fluent Bit
Kafka
Cloud APIs
REST APIs
Agent-based collection
```

---

# Collection Reliability

A security team should know:

```text
Are logs arriving?

Are they complete?

Are timestamps correct?

Are fields parsed?

Are events delayed?

Are events duplicated?

Are sources offline?
```

A missing log source can create a major blind spot.

---

# Telemetry Health

Monitor:

```text
Event Volume
Source Availability
Event Delay
Parsing Errors
Field Population
Dropped Events
Duplicate Events
```

Example:

```text
Firewall Logs
Yesterday: 5M events
Today:     0 events
```

This may indicate:

- Network issue
- Collector failure
- Firewall change
- Logging configuration change
- Attacker interference

---

# Log Parsing

Raw log:

```text
Oct 06 12:01:22 server sshd[1234]: Failed password for admin from 10.10.10.5 port 42122 ssh2
```

Parsed fields:

```text
timestamp = 2026-10-06T12:01:22
process = sshd
user = admin
source.ip = 10.10.10.5
source.port = 42122
action = authentication_failure
protocol = ssh
```

Structured data is easier to hunt.

---

# Normalization

Different systems may represent the same concept differently.

Example:

```text
Windows:
TargetUserName

Linux:
user

Firewall:
username

Cloud:
principal
```

A normalized schema might use:

```text
user.name
```

This allows cross-source hunting.

---

# Common Normalized Fields

A useful schema may include:

```text
@timestamp
event.action
event.category
event.outcome
user.name
user.id
source.ip
source.port
destination.ip
destination.port
host.name
process.name
process.command_line
file.name
network.protocol
cloud.account.id
```

Field names vary by platform.

---

# ECS

Elastic Common Schema (ECS) provides a standardized field model for many security and observability events.

Example:

```text
source.ip
destination.ip
user.name
process.name
process.command_line
host.name
event.category
```

Standardized schemas improve cross-source analytics.

---

# CIM

Splunk's Common Information Model (CIM) provides normalized data models for Splunk environments.

Examples include:

```text
Authentication
Endpoint
Network Traffic
Web
DNS
Malware
Change
```

Normalization allows searches to work across multiple data sources.

---

# OCSF

The Open Cybersecurity Schema Framework provides a vendor-agnostic approach to cybersecurity event normalization.

Conceptually:

```text
Vendor Event
     │
     ▼
OCSF Schema
     │
     ▼
Common Security Analytics
```

The exact schema implementation depends on the organization's architecture.

---

# Sigma

Sigma is a generic detection-rule format designed to describe log-based detections in a vendor-neutral manner.

Conceptually:

```text
Sigma Rule
    │
    ├──► Splunk
    ├──► Elastic
    ├──► Sentinel
    └──► Other Platforms
```

This improves portability.

---

# SIEM Threat-Hunting Workflow

```text
Hunt Question
     │
     ▼
Hypothesis
     │
     ▼
Identify Data Sources
     │
     ▼
Validate Telemetry
     │
     ▼
Build Query
     │
     ▼
Baseline
     │
     ▼
Find Anomalies
     │
     ▼
Correlate
     │
     ▼
Investigate
     │
     ▼
Document
     │
     ▼
Detection / Control
```

---

# Hunt Questions

Good hunt questions are specific.

Weak:

```text
"Is the network secure?"
```

Better:

```text
"Are endpoints generating unusual outbound connections?"
```

Better:

```text
"Which endpoints initiated outbound connections to destinations they have never contacted before during the last seven days?"
```

---

# Hypothesis-Driven Hunting

Example:

> A compromised endpoint may be communicating with previously unseen external infrastructure.

Required data:

```text
DNS
Network
Endpoint
Threat Intelligence
```

Query:

```text
Rare Destination
+
New Domain
+
Suspicious Process
```

---

# Query Development

Start broad.

```text
All authentication events
```

Then narrow:

```text
Failed authentication
```

Then:

```text
High failure volume
```

Then:

```text
Many users from one source
```

Then:

```text
Successful authentication after failures
```

This iterative process reduces blind spots.

---

# Broad-to-Narrow Hunting

```text
All Events
   │
   ▼
Relevant Category
   │
   ▼
Relevant Host/User
   │
   ▼
Anomalous Behavior
   │
   ▼
High-Confidence Activity
```

---

# Narrow-to-Broad Hunting

Sometimes the investigation starts with a known indicator.

```text
Known Malicious IP
      │
      ▼
Hosts Communicating
      │
      ▼
Users
      │
      ▼
Processes
      │
      ▼
Related Domains
      │
      ▼
Enterprise Scope
```

Both approaches are useful.

---

# SIEM Search Strategy

A professional hunt should consider:

```text
Time Range
Data Source
Fields
Filtering
Aggregation
Baseline
Correlation
Enrichment
```

Avoid immediately running extremely expensive queries across years of data.

---

# Time Windows

Time range should match the hypothesis.

Examples:

```text
Brute Force:
5–60 minutes

Beaconing:
Hours–Days

Persistence:
Days–Weeks

Long-Term Account Abuse:
Weeks–Months
```

---

# Time Bucketing

Instead of viewing thousands of events individually:

```text
12:00
12:01
12:02
...
```

aggregate them:

```text
5-minute window
10-minute window
1-hour window
```

Example:

```text
Source IP
Unique Users
Failures
Successes
```

---

# Statistical Baselines

A baseline can include:

```text
Mean
Median
Percentile
Standard Deviation
Frequency
Unique Count
Historical Range
```

Example:

```text
Typical API calls:
100–300/hour

Observed:
2,900/hour
```

The anomaly is worth investigating.

---

# Baseline Challenges

Baselines can be distorted by:

- Business growth
- Software deployments
- Holidays
- Incident response
- Cloud migration
- New applications
- Seasonal workloads

Baselines should therefore evolve.

---

# SIEM Enrichment

Useful enrichment includes:

```text
Asset Owner
Department
Criticality
User Role
GeoIP
ASN
Threat Intelligence
Domain Age
Cloud Account
Application
Vulnerability Data
```

Example:

```text
Source IP
   │
   ▼
Asset Lookup
   │
   ▼
Host Owner
   │
   ▼
Business Criticality
```

---

# Asset Context

Suppose two systems contact the same suspicious domain:

```text
Host A:
Developer Laptop

Host B:
Domain Controller
```

The second event should receive higher priority.

Asset criticality changes investigation priority.

---

# User Context

Likewise:

```text
User A:
Standard Employee

User B:
Domain Administrator
```

The same authentication anomaly may have very different risk.

---

# Correlation

Correlation connects events across time and systems.

Example:

```text
Email
  │
  ▼
Phishing Link
  │
  ▼
Authentication
  │
  ▼
Endpoint Process
  │
  ▼
DNS
  │
  ▼
Network Connection
  │
  ▼
Cloud Access
```

A SIEM can help reconstruct this chain.

---

# Correlation Example

```text
08:10 Email Received
08:13 Link Clicked
08:14 Browser Process
08:15 DNS Query
08:16 HTTPS Connection
08:18 PowerShell
08:20 Credential Access
08:25 Cloud Login
```

Each event individually may appear low-risk.

Together they may represent a compromise.

---

# Entity-Based Hunting

Instead of focusing only on events, investigate entities:

```text
User
Host
IP
Domain
Process
Application
Cloud Account
```

Example:

```text
User Alice
   │
   ├── Host A
   ├── Host B
   ├── IP C
   └── Cloud Account D
```

This supports relationship-based investigations.

---

# Entity Resolution

Different logs may represent the same entity differently.

Example:

```text
alice
alice@example.com
CORP\alice
A12345
```

Identity resolution should map these where appropriate.

---

# SIEM Investigation Graph

```text
             User
              │
       ┌──────┼──────┐
       ▼      ▼      ▼
      Host    IP    Cloud
       │      │      │
       ▼      ▼      ▼
    Process Domain Resource
```

Graph thinking helps analysts understand attack paths.

---

# Splunk Threat Hunting

Splunk Search Processing Language (SPL) can be used for investigation.

Basic:

```spl
index=auth
| stats count by user
| sort -count
```

---

# Splunk Authentication Hunt

```spl
index=auth action=failure
| stats
    count as failures
    dc(user) as users
    by src_ip
| sort -failures
```

---

# Splunk Rare Destination Hunt

```spl
index=network
| stats
    dc(src_ip) as hosts
    count as connections
    by dest_ip
| where hosts <= 2
| sort -connections
```

This is only a starting point.

---

# Splunk Process Hunting

```spl
index=endpoint
| stats count by host, process_name
| sort -count
```

Add command-line analysis when available.

---

# Splunk Correlation

Conceptually:

```spl
index=dns
| join host
    [ search index=endpoint process_name=powershell.exe ]
```

However, joins can be expensive at scale.

Prefer efficient correlation approaches such as:

- Stats
- Eventstats
- Transaction where appropriate
- Data models
- Accelerated searches

---

# Microsoft Sentinel

Microsoft Sentinel provides SIEM and security analytics capabilities integrated with Azure and Microsoft security telemetry.

Common hunting data sources include:

```text
SigninLogs
AuditLogs
SecurityEvent
DeviceProcessEvents
DeviceNetworkEvents
DnsEvents
CloudAppEvents
```

Exact tables depend on the connected data sources and deployment.

---

# Sentinel Hunting Example

```kusto
SigninLogs
| summarize
    Attempts = count(),
    Users = dcount(UserPrincipalName)
    by IPAddress
| order by Users desc
```

---

# Sentinel Authentication Hunt

```kusto
SigninLogs
| where ResultType != 0
| summarize
    Failures = count(),
    Users = dcount(UserPrincipalName)
    by IPAddress
| where Users >= 10
```

Tune thresholds according to organizational behavior.

---

# Sentinel Endpoint Correlation

Conceptually:

```kusto
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| project Timestamp, DeviceName, AccountName, ProcessCommandLine
```

Then correlate with network and identity telemetry.

---

# Elastic Security

Elastic can provide:

- Search
- Detection
- Endpoint telemetry
- Network telemetry
- Dashboards
- Threat intelligence
- Timeline investigation

ECS makes normalized security analysis easier.

---

# Elastic Query Example

Conceptually:

```text
event.category:authentication
and event.outcome:failure
```

Then aggregate by:

```text
source.ip
user.name
```

---

# SIEM Detection vs Hunt

A detection asks:

```text
"Did a known suspicious pattern occur?"
```

A hunt asks:

```text
"What suspicious or unknown behavior might exist?"
```

Detection:

```text
Specific Pattern
     │
     ▼
Alert
```

Hunt:

```text
Hypothesis
     │
     ▼
Search
     │
     ▼
Unknown Findings
```

---

# Detection Engineering Lifecycle

```text
Hunt Finding
     │
     ▼
Validate
     │
     ▼
Define Behavior
     │
     ▼
Write Detection
     │
     ▼
Test
     │
     ▼
Deploy
     │
     ▼
Monitor
     │
     ▼
Tune
```

This is one of the most important outputs of mature threat hunting.

---

# Detection Quality

A good SIEM detection should provide:

```text
High Signal
Useful Context
Low Noise
Clear Severity
Actionable Evidence
Stable Logic
```

---

# Detection Metadata

A professional detection should include:

```text
Detection Name
Description
Data Sources
Logic
Severity
MITRE ATT&CK
Owner
Version
False Positives
Response
Testing
Last Review
```

---

# Sigma Detection

A simplified Sigma rule structure:

```yaml
title: Suspicious Authentication Pattern
status: experimental

logsource:
  category: authentication

detection:
  selection:
    action: failure

  condition: selection

level: medium
```

Real-world rules should include stronger conditions and environment-specific fields.

---

# Detection Testing

Before production:

```text
Rule
 │
 ▼
Historical Replay
 │
 ▼
Known Benign Data
 │
 ▼
Known Malicious Data
 │
 ▼
False Positive Analysis
 │
 ▼
Production
```

---

# SIEM Alert Fatigue

Too many alerts can overwhelm analysts.

Example:

```text
100,000 Events
      │
      ▼
10,000 Alerts
      │
      ▼
500 Investigations
      │
      ▼
10 Real Incidents
```

A detection program must reduce unnecessary alert volume.

---

# Alert Prioritization

Prioritize using:

```text
Severity
+
Confidence
+
Asset Criticality
+
Identity Privilege
+
Threat Intelligence
+
Behavioral Context
```

---

# Risk-Based Alerting

A conceptual model:

```text
Risk Score =
Behavior
+
Identity
+
Asset
+
Threat Intelligence
+
Historical Anomaly
```

Example:

```text
Low-Risk DNS Anomaly
        +
Privileged Account
        +
Critical Server
        +
Known Malicious IP
```

should receive significantly higher priority.

---

# SIEM Data Quality

A SIEM is only as effective as its telemetry.

Ask:

```text
Are all critical systems connected?

Are logs complete?

Are timestamps synchronized?

Are fields normalized?

Are important events retained?

Are logs searchable within required timeframes?
```

---

# Time Synchronization

Accurate timestamps are critical for incident reconstruction.

Use synchronized time sources such as enterprise NTP infrastructure.

Without synchronization:

```text
Event A: 10:01
Event B: 09:58
Event C: 10:03
```

may be incorrectly ordered.

---

# Log Retention

Retention should reflect:

- Compliance
- Threat-hunting requirements
- Incident-response needs
- Storage costs
- Investigation timelines

Different data may require different retention periods.

---

# Hot vs Cold Data

Conceptually:

```text
Recent Data
   │
   ▼
Hot Storage
Fast Search
   │
   ▼
Warm Storage
   │
   ▼
Cold Archive
Lower Cost
```

Hunters should know where historical data resides.

---

# SIEM Performance

Poor queries can consume substantial resources.

Avoid unnecessary:

```text
Full historical scans
Large joins
Unbounded regex
High-cardinality aggregations
Repeated subsearches
```

Use:

```text
Narrow time ranges
Indexed fields
Data models
Pre-aggregation
Efficient filters
```

---

# Query Optimization

Bad:

```text
Search entire dataset
   │
   ▼
Filter later
```

Better:

```text
Restrict time
   │
   ▼
Restrict index/source
   │
   ▼
Filter early
   │
   ▼
Aggregate
```

---

# High-Cardinality Fields

Fields such as:

```text
URL
Command Line
Unique ID
Session ID
```

can generate enormous cardinality.

Use aggregation carefully.

---

# SIEM Hunting With Threat Intelligence

A threat-intelligence workflow:

```text
IOC
 │
 ▼
SIEM Search
 │
 ├── Historical DNS
 ├── Network
 ├── Endpoint
 ├── Email
 └── Authentication
```

The goal is not just to find current matches.

Determine:

```text
First Seen
Last Seen
Affected Hosts
Affected Users
Related Indicators
```

---

# IOC Retro-Hunting

Given:

```text
Malicious IP
```

search historical logs:

```text
IP
 │
 ├── DNS
 ├── Firewall
 ├── Proxy
 ├── EDR
 └── Cloud
```

Then scope the environment.

---

# IOC Limitations

Indicators can become:

- Stale
- Reused
- Shared
- False positive
- Infrastructure-dependent

Therefore combine:

```text
IOC
+
Behavior
+
Context
```

---

# SIEM Investigation Timeline

A good investigation should produce:

```text
Initial Event
      │
      ▼
First Suspicious Activity
      │
      ▼
Privilege Change
      │
      ▼
Lateral Movement
      │
      ▼
Persistence
      │
      ▼
Data Access
      │
      ▼
Exfiltration
```

The SIEM should help construct this timeline.

---

# Practical Lab 1 — Password Spray

## Objective

Identify a possible password-spraying source.

Search:

```text
Authentication Failures
        │
        ▼
Group by Source
        │
        ▼
Count Unique Users
        │
        ▼
Find Successful Authentication
```

Investigate the successful account.

---

# Practical Lab 2 — Suspicious PowerShell

## Objective

Identify unusual PowerShell execution.

Search:

```text
PowerShell
    │
    ▼
Command Line
    │
    ▼
Parent Process
    │
    ▼
User
    │
    ▼
Network Activity
```

Prioritize unusual parent-child relationships.

---

# Practical Lab 3 — DNS Beaconing

Search:

```text
Host
 │
 ▼
Domain
 │
 ▼
Repeated Queries
 │
 ▼
Interval Analysis
```

Correlate with network connections.

---

# Practical Lab 4 — Suspicious Privilege Change

Search:

```text
Privilege Event
      │
      ▼
User
      │
      ▼
Source Host
      │
      ▼
Subsequent Activity
```

Determine whether the change was authorized.

---

# Practical Lab 5 — IOC Retro-Hunt

Given:

```text
Suspicious Domain
Suspicious IP
Suspicious Hash
```

search:

```text
DNS
Network
Endpoint
Email
Cloud
```

Document:

```text
First Seen
Last Seen
Hosts
Users
Processes
```

---

# Practical Lab 6 — Multi-Source Correlation

Hypothesis:

> A compromised endpoint may have resulted in cloud account abuse.

Search:

```text
Endpoint
   │
   ▼
Authentication
   │
   ▼
Cloud Login
   │
   ▼
API Activity
```

Build one unified timeline.

---

# Practical Lab 7 — Logging Blind Spot

Find a source that suddenly stops sending telemetry.

Example:

```text
Firewall A
10:00 → 20,000 events

11:00 → 19,500 events

12:00 → 0 events
```

Investigate:

- Collector
- Network
- Configuration
- Device
- Logging service

---

# Practical Lab 8 — Rare Administrative Activity

Identify:

```text
Rare User
+
Administrative Action
+
Critical Resource
```

Then correlate with:

```text
Authentication
Endpoint
Cloud
Network
```

---

# Practical Lab 9 — Detection Validation

Take a known detection.

Perform:

```text
Historical Search
      │
      ▼
Known Benign Activity
      │
      ▼
Known Malicious Simulation
      │
      ▼
Measure Results
```

Document:

```text
True Positives
False Positives
Missed Events
Latency
```

---

# Practical Lab 10 — Hunt-to-Detection

Start with a hunt finding:

```text
Rare privileged login
```

Build:

```text
Hypothesis
   │
   ▼
Query
   │
   ▼
Validation
   │
   ▼
Detection
   │
   ▼
Testing
   │
   ▼
Production
```

This demonstrates the full threat-hunting lifecycle.

---

# SIEM Investigation Methodology

Use the following workflow:

```text
1. Define Question
2. Define Hypothesis
3. Identify Data
4. Validate Data Quality
5. Establish Baseline
6. Query
7. Investigate Outliers
8. Correlate
9. Enrich
10. Scope
11. Document
12. Detect
13. Tune
```

---

# SIEM Threat-Hunting Maturity

## Level 1 — Centralized Logs

Logs are collected but mainly searched manually.

## Level 2 — Structured Search

Analysts use normalized fields and repeatable queries.

## Level 3 — Hypothesis-Driven Hunting

Threat hunters proactively investigate behaviors.

## Level 4 — Detection Engineering

Hunt findings become repeatable detections.

## Level 5 — Continuous Detection Improvement

Detections, hunts, intelligence, and incident response continuously improve one another.

```text
Threat Intel
     ↓
Hunt
     ↓
Detection
     ↓
Incident
     ↓
Lessons Learned
     ↓
Improved Hunt
```

---

# SIEM Operating Model

A mature SOC may divide responsibilities across:

```text
Detection Engineering
Threat Hunting
SOC Operations
Incident Response
Threat Intelligence
Security Engineering
```

But these teams should share findings.

---

# Threat Hunter's SIEM Checklist

## Data

- [ ] Critical sources connected
- [ ] Logs arriving
- [ ] Timestamps synchronized
- [ ] Fields normalized
- [ ] Retention sufficient
- [ ] Data quality monitored

## Hunting

- [ ] Hypothesis defined
- [ ] Data sources identified
- [ ] Baseline established
- [ ] Query optimized
- [ ] Results validated
- [ ] Correlation performed

## Investigation

- [ ] User
- [ ] Host
- [ ] IP
- [ ] Process
- [ ] Domain
- [ ] Cloud identity
- [ ] Resource
- [ ] Timeline

## Detection

- [ ] Finding validated
- [ ] Rule documented
- [ ] MITRE mapped
- [ ] False positives tested
- [ ] Severity assigned
- [ ] Response documented

---

# Common SIEM Hunting Mistakes

## 1. Searching Without a Hypothesis

Large searches generate noise.

---

## 2. Ignoring Data Quality

Missing telemetry can produce false confidence.

---

## 3. Searching Too Much Data

Large unbounded queries waste resources.

---

## 4. Treating Every Anomaly as Malicious

Anomalies are investigation candidates.

---

## 5. Ignoring Asset Context

A critical server deserves different priority than a test workstation.

---

## 6. Ignoring Identity Context

User privilege and role matter.

---

## 7. Failing to Document Hunts

A hunt that exists only in an analyst's head cannot become organizational knowledge.

---

## 8. Not Converting Findings Into Detections

Repeated successful hunts should often become automated detections.

---

# Professional SIEM Hunt Record

```text
Hunt ID:

Hunt Name:

Analyst:

Date:

Hypothesis:

Threat Actor / Technique:

Data Sources:

Time Range:

Query:

Baseline:

Observed Behavior:

Anomalies:

Related Users:

Related Hosts:

Related IPs:

Related Domains:

Threat Intelligence:

Asset Criticality:

MITRE ATT&CK:

Evidence:

Assessment:

True Positive / False Positive:

Detection Candidate:

Recommended Controls:

Follow-Up:

Lessons Learned:
```

---

# SIEM Detection Record

```text
Detection ID:

Detection Name:

Description:

Objective:

Data Sources:

Required Fields:

Logic:

Severity:

Confidence:

MITRE ATT&CK:

Expected False Positives:

Exclusions:

Testing Method:

Response:

Owner:

Version:

Last Review:

Performance:

Status:
```

---

# Interview Questions

## 1. What is a SIEM?

A SIEM is a security platform that collects, normalizes, analyzes, searches, correlates, and presents security telemetry to support detection and investigation.

---

## 2. Is a SIEM the same as a threat-hunting platform?

No.

A SIEM is a primary source of centralized security telemetry and analytical capability. Threat hunting is a proactive investigative methodology.

---

## 3. What is log normalization?

Normalization maps different vendor-specific event formats into common fields and structures.

---

## 4. Why is normalization important?

It allows analysts and detection rules to query similar security concepts consistently across multiple data sources.

---

## 5. What is Sigma?

Sigma is a vendor-neutral format for describing log-based detection rules.

---

## 6. What is the difference between detection and hunting?

Detection looks for known or defined suspicious patterns.

Hunting proactively searches for suspicious or previously unknown behavior based on hypotheses.

---

## 7. What is correlation?

Correlation connects events based on relationships such as:

```text
Time
User
Host
IP
Process
Domain
Resource
```

to reconstruct activity.

---

## 8. Why is asset context important?

It helps determine the business significance and risk of an event.

---

## 9. How would you investigate a suspicious IP in a SIEM?

I would search historical:

```text
DNS
Firewall
Proxy
Endpoint
Email
Authentication
Cloud
```

activity and determine affected users, hosts, processes, and timeline.

---

## 10. How do you avoid SIEM performance problems?

Use:

```text
Narrow Time Windows
Indexed Fields
Early Filtering
Efficient Aggregations
Data Models
Pre-Aggregation
```

and avoid unnecessarily expensive searches.

---

## 11. What is alert fatigue?

Alert fatigue occurs when analysts receive excessive low-value alerts, reducing their ability to identify genuinely important incidents.

---

## 12. How do you improve detection quality?

Use:

```text
Baselines
Context
Correlation
Threat Intelligence
Testing
False-Positive Analysis
Continuous Tuning
```

---

## 13. What should happen after a successful hunt?

The finding should be validated, documented, shared with relevant teams, and considered for detection engineering or control improvement.

---

## 14. What is a SIEM data-quality problem?

Examples include:

- Missing logs
- Parsing failures
- Incorrect timestamps
- Dropped events
- Duplicate events
- Missing fields

---

## 15. What is the most important SIEM hunting principle?

> **The SIEM is not valuable merely because it contains massive amounts of data; it is valuable when analysts can transform that data into reliable security decisions.**

---

# Key Takeaways

1. **A SIEM is a foundational platform for security visibility.**
2. **Threat hunting is a methodology, not merely a search operation.**
3. **Collection quality directly affects hunting quality.**
4. **Normalization enables scalable cross-source hunting.**
5. **Enrichment adds identity, asset, business, and threat context.**
6. **Hypothesis-driven hunting reduces unstructured investigation.**
7. **Correlation connects individual events into attack narratives.**
8. **Time range selection is critical for efficient hunting.**
9. **Baselines help distinguish unusual behavior from normal operations.**
10. **Asset and identity context should influence investigation priority.**
11. **Threat intelligence is more useful when combined with behavioral evidence.**
12. **SIEM detections require testing and continuous tuning.**
13. **Detection engineering should consume successful hunting findings.**
14. **Telemetry health is itself a security concern.**
15. **A mature SIEM program continuously connects telemetry, hunting, detection, and incident response.**

The core mindset is:

> **Don't ask only "Can I search this log?" Ask "Do I have the right telemetry, can I reliably connect it to other entities, and can I turn the result into a repeatable security capability?"**

---

# References

- NIST SP 800-92 — Guide to Computer Security Log Management  
  https://csrc.nist.gov/publications/detail/sp/800-92/final

- MITRE ATT&CK  
  https://attack.mitre.org/

- Sigma HQ  
  https://sigmahq.io/

- Sigma Specification  
  https://github.com/SigmaHQ/sigma-specification

- Splunk Documentation  
  https://docs.splunk.com/

- Splunk Common Information Model  
  https://docs.splunk.com/Documentation/CIM/

- Microsoft Sentinel Documentation  
  https://learn.microsoft.com/azure/sentinel/

- Microsoft Kusto Query Language  
  https://learn.microsoft.com/kusto/query/

- Elastic Security  
  https://www.elastic.co/security

- Elastic Common Schema  
  https://www.elastic.co/guide/en/ecs/current/index.html

- Open Cybersecurity Schema Framework  
  https://ocsf.io/

- CISA Cybersecurity Resources  
  https://www.cisa.gov/topics/cybersecurity

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework
