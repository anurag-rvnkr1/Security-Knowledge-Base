# Hunting Query Engineering

## Overview

Threat hunting depends heavily on the quality of the queries used to analyze security telemetry.

A threat hunter may have:

- Excellent threat intelligence
- Strong knowledge of MITRE ATT&CK
- High-quality telemetry
- A well-defined hypothesis

but still fail to identify malicious activity if the query is:

- Too broad
- Too narrow
- Inefficient
- Based on unreliable fields
- Missing relevant data sources
- Vulnerable to false positives
- Unable to correlate related activity

Hunting query engineering is therefore the discipline of designing queries that are:

```text
Accurate
Efficient
Repeatable
Explainable
Scalable
Maintainable
Portable
```

The fundamental objective is:

> **Transform a security hypothesis into an efficient query that produces useful investigative evidence.**

---

# Hunting Query Engineering Lifecycle

```text
Threat Intelligence
       │
       ▼
Hunt Hypothesis
       │
       ▼
Required Evidence
       │
       ▼
Data Sources
       │
       ▼
Field Mapping
       │
       ▼
Query Design
       │
       ▼
Optimization
       │
       ▼
Validation
       │
       ▼
Hunt
       │
       ▼
Finding
       │
       ▼
Detection
```

---

# Why Query Engineering Matters

Enterprise SIEM environments may contain:

```text
Millions
    ↓
Billions
    ↓
Potentially Trillions
```

of events.

A poorly designed query can:

- Consume excessive compute
- Produce huge result sets
- Increase investigation time
- Create false positives
- Miss relevant activity
- Affect other SOC operations

A good query reduces the search space while preserving meaningful evidence.

---

# Query Engineering Principles

A strong hunting query should answer:

```text
What am I looking for?

Why am I looking for it?

Which data source contains the evidence?

Which fields represent the behavior?

What is normal?

What makes the event suspicious?

How can I validate the result?
```

---

# Query Anatomy

Most security queries contain several logical stages:

```text
Data Source
    │
    ▼
Time Range
    │
    ▼
Initial Filtering
    │
    ▼
Field Extraction
    │
    ▼
Aggregation
    │
    ▼
Correlation
    │
    ▼
Enrichment
    │
    ▼
Scoring
    │
    ▼
Investigation Output
```

---

# Example

Suppose the hypothesis is:

> An attacker may be performing password spraying against multiple users from a single source.

Required evidence:

```text
Authentication failures
+
Multiple target users
+
Common source
+
Short time window
```

Query logic:

```text
Authentication Failures
        │
        ▼
Group by Source IP
        │
        ▼
Count Unique Users
        │
        ▼
Count Failures
        │
        ▼
Apply Threshold
```

---

# Query Development Methodology

Use the following process:

```text
1. Define hypothesis
2. Identify required evidence
3. Identify telemetry
4. Map fields
5. Start broad
6. Validate fields
7. Narrow the search
8. Aggregate
9. Correlate
10. Enrich
11. Test false positives
12. Optimize
13. Document
```

---

# Step 1 — Define the Hypothesis

Bad:

```text
Find hackers.
```

Better:

```text
Find endpoints executing suspicious PowerShell.
```

Better:

```text
Identify PowerShell executions from unusual parent processes on endpoints where the command line contains suspicious network or encoded execution behavior.
```

The stronger hypothesis produces a better query.

---

# Step 2 — Define Required Evidence

For the PowerShell hypothesis:

```text
Process Name
Command Line
Parent Process
User
Host
Timestamp
Network Connection
```

Required fields:

```text
process.name
process.command_line
process.parent.name
user.name
host.name
@timestamp
destination.ip
```

---

# Step 3 — Identify Data Sources

Potential sources:

```text
EDR
Windows Event Logs
Sysmon
SIEM
Network
DNS
Proxy
```

Do not assume one data source contains the entire attack story.

---

# Step 4 — Map Fields

Example:

```text
Concept            Field

User               user.name
Host               host.name
Source IP           source.ip
Destination IP      destination.ip
Process             process.name
Command Line       process.command_line
Parent Process      process.parent.name
Timestamp           @timestamp
```

Field names differ by platform.

---

# Field Mapping

A field mapping table helps maintain query portability.

```text
Concept
  │
  ├── Splunk
  ├── ECS
  ├── Sentinel
  ├── Windows
  └── OCSF
```

Maintain a documented mapping layer where possible.

---

# Query Reliability

Not all fields are equally trustworthy.

Example:

```text
process.name
```

may be reliably populated.

While:

```text
process.command_line
```

may be missing due to telemetry configuration.

Therefore query engineering must consider field coverage.

---

# Field Coverage

Calculate:

```text
Field Coverage =
Events Containing Field
-----------------------
Total Relevant Events
```

Example:

```text
Command Line Coverage = 96%
Parent Process Coverage = 71%
```

The second field should be treated carefully.

---

# Query Testing

Before using a field:

```text
Search sample events
        │
        ▼
Check field exists
        │
        ▼
Check field format
        │
        ▼
Check value consistency
        │
        ▼
Check null rate
```

---

# Start Broad

Example:

```text
process.name = powershell.exe
```

Then inspect:

```text
Users
Hosts
Parents
Commands
Frequency
```

Do not immediately build a complex query without validating the underlying data.

---

# Narrow Gradually

```text
PowerShell
   │
   ▼
PowerShell + Encoded Command
   │
   ▼
PowerShell + Suspicious Parent
   │
   ▼
PowerShell + External Network Activity
   │
   ▼
PowerShell + Rare Host Behavior
```

Each step increases specificity.

---

# Query Precision vs Recall

Two important concepts:

## Precision

Percentage of returned results that are actually relevant.

```text
Precision =
Relevant Results
---------------
All Results
```

## Recall

Percentage of relevant activity that the query successfully finds.

```text
Recall =
Relevant Results Found
----------------------
All Relevant Activity
```

---

# Example

Query A:

```text
powershell.exe
```

High recall.

But potentially low precision.

Query B:

```text
powershell.exe
+
encoded command
+
unusual parent
+
external connection
```

Higher precision.

But it may miss other attacks.

---

# Hunting Requires Balance

```text
Broad Query
   │
   ├── High Recall
   └── More Noise

Narrow Query
   │
   ├── High Precision
   └── Possible Misses
```

Experienced hunters often begin broad and progressively narrow.

---

# Time Range Engineering

Time range is one of the most important query parameters.

Examples:

```text
Brute Force       → Minutes / Hours
Beaconing         → Hours / Days
Persistence       → Days / Weeks
Account Abuse     → Weeks / Months
Insider Activity  → Longer historical windows
```

---

# Search Recent Data First

For initial investigation:

```text
Last 1 hour
Last 24 hours
Last 7 days
```

Expand only when required.

This improves both performance and analyst focus.

---

# Time Window Selection

Example:

```text
Password Spray
```

A useful starting window may be:

```text
5–30 minutes
```

because password spraying often attempts many accounts within a relatively short period.

However, attackers may deliberately spread activity across longer periods.

Therefore test multiple windows when appropriate.

---

# Time Bucketing

Instead of:

```text
1,000 individual events
```

aggregate into:

```text
5-minute buckets
```

Example:

```text
Time        Failures

10:00       5
10:05       7
10:10       92
10:15       103
```

The spike becomes obvious.

---

# Sliding Windows

A sliding window evaluates activity across overlapping intervals.

Conceptually:

```text
10:00 ───── 10:10
      10:01 ───── 10:11
            10:02 ───── 10:12
```

This can identify activity that does not align with fixed buckets.

---

# Threshold Engineering

A threshold should be based on evidence.

Bad:

```text
Failures > 10
```

Better:

```text
Failures > historical baseline
```

Better:

```text
Failures significantly above expected behavior
AND
multiple unique users
```

---

# Static Thresholds

Example:

```text
More than 20 failures
```

Advantages:

- Simple
- Fast
- Easy to understand

Disadvantages:

- Environment-specific
- Can create false positives
- May miss slow attacks

---

# Dynamic Thresholds

Dynamic thresholds use historical behavior.

Example:

```text
Normal:
5–20 authentication failures/hour

Observed:
250/hour
```

The deviation becomes suspicious.

---

# Statistical Thresholds

Possible methods include:

```text
Mean
Median
Percentiles
Standard Deviation
MAD
Historical Maximum
```

Robust methods are often preferable when data contains outliers.

---

# Cardinality

Cardinality refers to the number of unique values.

Examples:

```text
Unique Users
Unique Hosts
Unique IPs
Unique Domains
```

Example:

```text
Source IP: 10.10.10.10

Failures: 150
Unique Users: 42
```

This is more suspicious than:

```text
Failures: 150
Unique Users: 1
```

because the first pattern may indicate spraying.

---

# Distinct Counts

Security queries frequently use distinct counts.

Conceptually:

```text
count(events)
```

measures volume.

While:

```text
distinct_count(users)
```

measures breadth.

Both can be important.

---

# Aggregation

Aggregation converts many events into useful summaries.

Example:

```text
Source IP
Failures
Unique Users
Unique Hosts
First Seen
Last Seen
```

This produces analyst-friendly output.

---

# Example Aggregation

```text
Source IP       Failures    Users    Hosts

10.10.10.10     532         71       32
10.10.10.20     28          2        1
10.10.10.30     9           1        1
```

The first source deserves investigation.

---

# Grouping Strategy

Choose grouping fields based on the hypothesis.

For password spraying:

```text
source.ip
```

For account abuse:

```text
user.name
```

For lateral movement:

```text
source.host
destination.host
```

For beaconing:

```text
host
destination
```

---

# Query Cost

Query cost can be influenced by:

```text
Data Volume
Time Range
Field Cardinality
Regex
Joins
Subqueries
Sorting
Aggregations
Data Model
Storage Architecture
```

---

# Query Optimization

General strategy:

```text
Reduce Data
     │
     ▼
Filter Early
     │
     ▼
Select Required Fields
     │
     ▼
Aggregate
     │
     ▼
Correlate
```

---

# Filter Early

Less efficient:

```text
Retrieve millions of events
        │
        ▼
Process everything
        │
        ▼
Filter
```

More efficient:

```text
Time Filter
     │
     ▼
Source Filter
     │
     ▼
Event Filter
     │
     ▼
Analysis
```

---

# Indexed Fields

Use fields supported efficiently by the SIEM's storage/search architecture.

Examples may include:

```text
Index
Source
Event Type
Timestamp
Tenant
Host
```

Exact optimization mechanisms vary between platforms.

---

# Avoid Unnecessary Regex

Regex can be computationally expensive.

Instead of:

```text
.*powershell.*
```

use structured fields when available:

```text
process.name = powershell.exe
```

Then apply regex only when necessary.

---

# Regex Safety

Avoid unnecessarily complex expressions.

Bad:

```text
Highly nested regex
```

Better:

```text
Structured parsing
+
Simple pattern matching
```

---

# Case Normalization

Different systems may record:

```text
PowerShell
powershell
POWERSHELL
```

Normalize values where appropriate.

Conceptually:

```text
lower(process.name)
```

Then compare against normalized values.

---

# String Matching

Prefer exact matching where possible.

Example:

```text
process.name = "powershell.exe"
```

instead of broad substring matching:

```text
process contains "shell"
```

The second can create noise.

---

# Wildcards

Wildcards are useful but can increase search cost.

Use them carefully.

Instead of:

```text
*admin*
```

consider identifying the exact field and normalized values.

---

# Query Layering

Complex hunts should often be divided into stages:

```text
Stage 1
Data Discovery

Stage 2
Filtering

Stage 3
Aggregation

Stage 4
Correlation

Stage 5
Enrichment

Stage 6
Scoring
```

This makes troubleshooting easier.

---

# Reusable Query Components

Create reusable building blocks:

```text
Authentication Filter
Endpoint Filter
DNS Filter
Privileged User Filter
Critical Asset Filter
Known Bad Indicator Filter
```

Then combine them.

---

# Query Templates

Example:

```text
<DATA_SOURCE>
| <TIME_FILTER>
| <BEHAVIOR_FILTER>
| <GROUPING>
| <THRESHOLD>
| <ENRICHMENT>
```

Templates improve consistency across analysts.

---

# IOC Query Engineering

Given:

```text
Malicious IP
```

Do not search only:

```text
destination.ip = IOC
```

Also consider:

```text
source.ip
dns.answers
url.domain
proxy.destination
firewall.destination
cloud.network
```

depending on telemetry.

---

# IOC Normalization

Indicators may appear as:

```text
IP
IPv6
Domain
FQDN
URL
Hash
Email
Certificate
```

Normalize before searching.

---

# Domain Matching

Searching:

```text
example.com
```

may miss:

```text
www.example.com
cdn.example.com
login.example.com
```

Depending on the use case, consider parent-domain relationships.

But avoid matching unrelated domains accidentally.

---

# Hash Hunting

Common hashes:

```text
MD5
SHA-1
SHA-256
```

Search endpoint telemetry:

```text
file.hash
process.hash
attachment.hash
```

depending on available data.

---

# TTP Hunting

IOC hunting:

```text
Known Indicator
     │
     ▼
Search
```

TTP hunting:

```text
Behavior
     │
     ▼
Search Multiple Indicators
     │
     ▼
Identify Technique
```

TTP hunting is generally more resilient to infrastructure changes.

---

# Process Tree Queries

A process alone may not be suspicious.

Example:

```text
winword.exe
   │
   └── powershell.exe
```

is more interesting than:

```text
powershell.exe
```

alone.

Query:

```text
Parent
+
Child
+
User
+
Command Line
```

---

# Parent-Child Hunting

Common suspicious relationships may include:

```text
Office
  └── PowerShell

Browser
  └── Command Shell

Web Server
  └── Shell

Database
  └── Command Interpreter
```

Context is essential.

---

# Living-off-the-Land Hunting

Attackers may use legitimate tools.

Examples:

```text
PowerShell
cmd
wscript
cscript
rundll32
regsvr32
mshta
certutil
bitsadmin
```

Do not treat execution alone as malicious.

Instead correlate:

```text
Tool
+
User
+
Parent
+
Arguments
+
Destination
+
Frequency
```

---

# Command-Line Query Engineering

Command lines can be high-value telemetry.

Search for:

```text
Encoded commands
Download operations
Credential-related parameters
Remote execution
Unusual URLs
Temporary directories
Suspicious scripting
```

Use environment-specific tuning.

---

# DNS Query Engineering

Example hypothesis:

> A compromised endpoint may be performing automated DNS beaconing.

Required fields:

```text
host
query
response
timestamp
query_type
```

Aggregate:

```text
Host
Domain
Query Count
Intervals
Unique Domains
```

---

# Beacon Query Logic

```text
Repeated Domain
+
Regular Intervals
+
Same Host
+
Long Duration
```

Potentially suspicious.

Add:

```text
Rare Destination
+
Suspicious Process
```

for stronger evidence.

---

# Authentication Query Engineering

Important fields:

```text
user
source.ip
destination
authentication_method
result
timestamp
```

Useful analytics:

```text
Failure Count
Unique Users
Unique Hosts
Success After Failure
Geographic Spread
Device Spread
```

---

# Lateral Movement Query

Hypothesis:

> A compromised account may be moving between systems.

Query dimensions:

```text
Source Host
Destination Host
User
Authentication Type
Timestamp
```

Then build a graph:

```text
Host A
  │
  ├── Host B
  ├── Host C
  └── Host D
```

---

# Identity Graph Hunting

Example:

```text
User
 │
 ├── Host A
 │
 ├── Host B
 │
 ├── IP C
 │
 └── Cloud Session
```

Unexpected relationships deserve investigation.

---

# Cloud Query Engineering

Cloud telemetry often contains:

```text
Principal
Source IP
Action
Resource
Region
User Agent
Session
```

Useful query dimensions:

```text
Rare API Calls
New Regions
New User Agents
Privilege Changes
Access Key Usage
Role Assumption
Resource Exposure
```

---

# Cloud API Sequence Hunting

Example:

```text
Console Login
      │
      ▼
Create Access Key
      │
      ▼
Modify IAM Policy
      │
      ▼
Access Storage
```

Each action may be legitimate.

The sequence is what creates concern.

---

# Sequence Detection

Some attacks are better represented as sequences:

```text
A → B → C
```

rather than individual events.

Examples:

```text
Login Failure
    →
Successful Login
    →
Privilege Change
```

or:

```text
Process Creation
    →
Network Connection
    →
Credential Access
```

---

# Sequence Windows

Define a reasonable time window:

```text
A
│
├──── 5 min ────► B
│
├──── 20 min ───► C
```

The window should reflect the behavior being investigated.

---

# Correlation Keys

Common correlation keys:

```text
User
Host
Source IP
Destination IP
Session ID
Process ID
Cloud Account
Request ID
```

Choose keys carefully.

---

# Correlation Pitfall

Correlating only on:

```text
user.name
```

can generate noise because a user may legitimately operate multiple systems.

Better:

```text
user
+
host
+
time
```

or:

```text
user
+
source.ip
+
session
```

depending on the use case.

---

# Sessionization

Sessionization groups related events into logical sessions.

Example:

```text
User Login
    │
    ├── Command
    ├── Network Request
    ├── File Access
    └── Logout
```

This makes investigations easier.

---

# Sequence-Based Hunting

Conceptual sequence:

```text
Authentication
      ↓
Privilege Escalation
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Data Access
```

Query each stage and connect them.

---

# Rare Event Hunting

A rare event may be valuable.

Examples:

```text
Rare Process
Rare Parent-Child Relationship
Rare Domain
Rare User-Agent
Rare Administrative Action
Rare Cloud API
```

But:

> Rare does not automatically mean malicious.

---

# Frequency Analysis

Example:

```text
Event                     Frequency

PowerShell                20,000
cmd.exe                   12,000
rundll32.exe              400
mshta.exe                 12
```

The rare `mshta.exe` activity deserves contextual review.

---

# Peer Group Analysis

Compare an entity with similar entities.

Example:

```text
Finance Users
Engineering Users
Domain Controllers
Developer Servers
```

A behavior may be normal for one peer group but abnormal for another.

---

# User Peer Baselines

Example:

```text
Typical User:
10 logins/day

Observed:
80 logins/day
```

This may indicate:

- Account compromise
- Automation
- New workflow
- Shared account
- Service behavior

Context is required.

---

# Host Peer Baselines

Compare:

```text
Workstation
Server
Domain Controller
Database Server
Cloud VM
```

Different systems have different normal behaviors.

---

# Negative Hunting

Sometimes search for absence.

Examples:

```text
Critical host not sending logs
Endpoint without EDR heartbeat
Cloud account without MFA
Expected backup events missing
```

Absence can be a security signal.

---

# Telemetry Gap Hunting

Example:

```text
100 endpoints expected
97 reporting
```

Investigate the missing three.

Telemetry gaps may occur because of:

- Agent failure
- Network failure
- Configuration
- New assets
- Decommissioned assets
- Tampering

---

# Query Validation With Known Benign Data

Run the query against normal activity.

Questions:

```text
How many results?

Which users?

Which hosts?

What applications?

What normal workflows trigger it?
```

This identifies false positives.

---

# Query Validation With Known Malicious Data

Use:

- Authorized lab simulations
- Detection test datasets
- Historical incidents
- Purple-team exercises

Confirm the query detects the intended behavior.

---

# Purple-Team Validation

```text
Adversary Simulation
       │
       ▼
Telemetry
       │
       ▼
SIEM
       │
       ▼
Hunting Query
       │
       ▼
Detection
       │
       ▼
SOC Investigation
```

This validates the complete detection chain.

---

# Query Unit Testing

Treat important queries like software.

Test:

```text
Expected Match
Expected Non-Match
Edge Case
Missing Field
Malformed Data
Case Variation
Time Boundary
```

---

# Example Test Matrix

| Test | Expected Result |
|---|---|
| Known malicious event | Match |
| Normal PowerShell | No match |
| Missing command line | Graceful handling |
| Uppercase process | Match if normalized |
| Old event outside window | No match |
| Similar benign command | No match |

---

# Query Documentation

Every production hunting query should explain:

```text
Purpose
Hypothesis
Data Sources
Required Fields
Logic
Threshold
Expected Output
Known False Positives
Performance Notes
MITRE Mapping
Owner
Last Review
```

---

# Query Versioning

Use version control.

Example:

```text
query-v1
query-v2
query-v3
```

Document changes.

Example:

```text
v1:
Initial detection

v2:
Added parent process

v3:
Added critical asset context
```

---

# Query Portability

Different platforms have different query languages.

```text
Splunk → SPL
Sentinel → KQL
Elastic → KQL / EQL / DSL
QRadar → AQL
OpenSearch → Query DSL / SQL / PPL
```

Do not assume syntactic portability.

The logic should be portable even when syntax is not.

---

# Portable Hunt Logic

Example:

```text
Hypothesis:
One source IP is authenticating against many accounts.

Logic:

Authentication failures
+
Group by source
+
Count unique users
+
Apply threshold
```

The implementation changes by SIEM.

---

# Sigma as an Abstraction Layer

Sigma can describe detection logic:

```text
Behavior
   │
   ▼
Sigma
   │
   ├── SPL
   ├── KQL
   ├── Elastic
   └── Other Backend
```

This supports detection-as-code workflows.

---

# Detection-as-Code

Treat detections as software artifacts.

Repository:

```text
detections/
│
├── windows/
├── linux/
├── cloud/
├── network/
├── identity/
└── sigma/
```

Include:

```text
Rules
Tests
Documentation
Metadata
Version History
```

---

# Query-as-Code

A mature organization can maintain:

```text
queries/
│
├── authentication/
├── endpoint/
├── dns/
├── network/
├── cloud/
└── identity/
```

Benefits:

- Review
- Collaboration
- Version control
- Reproducibility
- Auditability

---

# Pull Request Workflow

```text
Analyst
   │
   ▼
Create Query
   │
   ▼
Unit Tests
   │
   ▼
Peer Review
   │
   ▼
Performance Review
   │
   ▼
Deploy
```

---

# Query Naming Convention

Example:

```text
TH-AUTH-001-Password-Spray
TH-ENDPOINT-002-Suspicious-PowerShell
TH-DNS-003-DGA-Lookup
TH-CLOUD-004-IAM-Privilege-Change
```

Naming should be consistent across the organization.

---

# Query Metadata

Recommended:

```yaml
id: TH-AUTH-001
name: Password Spray Hunt
category: authentication
author: security-team
version: 1.2
severity: medium
confidence: medium
mitre:
  - T1110.003
data_sources:
  - authentication
  - identity
```

---

# False Positive Engineering

Every query should identify expected benign behavior.

Examples:

```text
Vulnerability Scanners
Monitoring Systems
Backup Services
IT Administration
Penetration Testing
Automated Applications
```

Do not blindly exclude them.

Instead use:

```text
Known Source
+
Expected Behavior
+
Expected Schedule
```

---

# Suppression vs Exclusion

Exclusion:

```text
Never investigate this entity.
```

Suppression:

```text
Reduce repeated notifications while retaining evidence.
```

Suppression is often safer than permanently excluding activity.

---

# Allowlist Risk

An allowlist can become dangerous.

Example:

```text
Trusted IP
```

may later become compromised.

Review allowlists regularly.

---

# Query Drift

Environment changes can break queries.

Examples:

```text
New EDR
New Cloud Platform
New Identity Provider
New Log Schema
New Host Naming
```

Queries must be periodically reviewed.

---

# Schema Drift

Example:

```text
Old:
user

New:
user.name
```

A query may silently stop working.

Monitor query health.

---

# Query Health Monitoring

Track:

```text
Execution Success
Result Volume
Runtime
Field Coverage
False Positive Rate
Detection Coverage
```

A query returning zero results forever may not mean "no threats."

It may mean "broken telemetry."

---

# Hunting Query Performance Metrics

Useful metrics:

```text
Execution Time
Data Scanned
Events Processed
Results Returned
Resource Consumption
Failure Rate
```

---

# Query Result Quality

A good result should be:

```text
Relevant
Understandable
Actionable
Traceable
```

Include evidence fields.

Example:

```text
Timestamp
Host
User
Source IP
Destination
Process
Command Line
Reason
```

---

# Explainability

Avoid black-box hunting queries where analysts cannot explain why an event was selected.

A hunter should be able to answer:

> Why did this event appear?

---

# Risk Scoring

Multiple weak signals can be combined.

Conceptually:

```text
Risk =
Rare Behavior
+
Privileged Identity
+
Critical Asset
+
Threat Intelligence
+
Unusual Network Activity
```

Example:

```text
Rare PowerShell
   + 
Admin User
   +
Domain Controller
   +
External Connection
```

This should rank highly.

---

# Multi-Signal Hunting

Instead of:

```text
PowerShell = suspicious
```

use:

```text
PowerShell
+
Rare Parent
+
Encoded Command
+
External Connection
+
Privileged User
```

The combined evidence is stronger.

---

# Query Chaining

One query can produce candidates for another.

```text
Query A
Rare Hosts
   │
   ▼
Query B
Processes on Hosts
   │
   ▼
Query C
Network Activity
   │
   ▼
Query D
Identity Activity
```

This reduces unnecessary global searches.

---

# Pivoting

Threat hunting is iterative.

```text
IP
 │
 ▼
Host
 │
 ▼
User
 │
 ▼
Process
 │
 ▼
Domain
 │
 ▼
Cloud Account
```

Each pivot produces new investigative context.

---

# Example Hunt — Suspicious PowerShell

## Hypothesis

An attacker may be using PowerShell to execute commands on an endpoint.

## Query stages

### Stage 1

```text
process.name = powershell.exe
```

### Stage 2

Add:

```text
process.command_line
```

### Stage 3

Add:

```text
parent process
```

### Stage 4

Add:

```text
network activity
```

### Stage 5

Add:

```text
user privilege
```

Final analytical model:

```text
PowerShell
+
Unusual Parent
+
Suspicious Command
+
Network Connection
+
Privileged User
```

---

# Example Hunt — Password Spraying

## Hypothesis

An external source may be attempting credentials against many accounts.

Required logic:

```text
Authentication Failure
        │
        ▼
Group by Source
        │
        ▼
Unique Users
        │
        ▼
Short Time Window
        │
        ▼
Successful Login?
```

Then investigate:

```text
Source Reputation
Target Accounts
Authentication Method
Location
Device
Post-Login Activity
```

---

# Example Hunt — DNS Tunneling

## Hypothesis

A compromised endpoint may be transferring information through DNS.

Look for:

```text
High Query Volume
+
Long Labels
+
High Entropy
+
TXT Usage
+
Rare Domains
+
Regular Intervals
```

Correlate with:

```text
Process
Network
User
Host
```

---

# Example Hunt — Cloud Privilege Escalation

## Hypothesis

A cloud identity may be escalating permissions.

Search:

```text
Role Changes
+
Policy Changes
+
New Credentials
+
New Region
+
Sensitive API Calls
```

Then correlate:

```text
Principal
Source IP
User Agent
Session
Resource
```

---

# Example Hunt — Lateral Movement

## Hypothesis

A compromised account may be accessing multiple internal hosts.

Search:

```text
User
+
Source Host
+
Destination Host
+
Authentication Type
```

Aggregate:

```text
Unique Destinations
```

Then compare against historical behavior.

---

# Query Engineering Checklist

## Hypothesis

- [ ] Is the hypothesis explicit?
- [ ] Is it testable?
- [ ] Is the expected behavior defined?

## Data

- [ ] Correct data source?
- [ ] Required fields available?
- [ ] Telemetry coverage validated?

## Logic

- [ ] Correct filters?
- [ ] Correct aggregation?
- [ ] Correct time window?
- [ ] Correct correlation key?

## Performance

- [ ] Narrow time range?
- [ ] Filters applied early?
- [ ] Expensive regex minimized?
- [ ] Aggregations reasonable?

## Quality

- [ ] False positives tested?
- [ ] Known malicious activity tested?
- [ ] Edge cases tested?
- [ ] Output actionable?

## Maintenance

- [ ] Documented?
- [ ] Versioned?
- [ ] Owner assigned?
- [ ] MITRE mapped?
- [ ] Review date defined?

---

# Common Query Engineering Mistakes

## 1. Searching Everything

Massive searches are rarely the best first step.

---

## 2. Overfitting

A query designed around one exact incident may fail against similar attacks.

---

## 3. Overly Broad Matching

Broad patterns create noise.

---

## 4. Ignoring Field Coverage

A query cannot reliably detect what telemetry does not capture.

---

## 5. Hard-Coded Thresholds

Static thresholds can fail as environments change.

---

## 6. Excessive Regex

Structured fields should be preferred.

---

## 7. Expensive Joins

Large joins can severely impact performance.

---

## 8. No Testing

Queries should be validated before operational use.

---

## 9. No Documentation

Another analyst should be able to understand the query.

---

## 10. No Version Control

Security logic should be auditable.

---

# Professional Hunt Query Template

```text
Hunt ID:

Hunt Name:

Objective:

Hypothesis:

Threat:

MITRE ATT&CK:

Data Sources:

Required Fields:

Time Range:

Query:

Aggregation:

Threshold:

Correlation:

Enrichment:

Expected Results:

Known Benign Behavior:

False Positives:

Performance Notes:

Validation Dataset:

Detection Candidate:

Owner:

Version:

Last Review:
```

---

# Query Engineering Maturity

## Level 1 — Ad Hoc

Analysts manually search logs.

## Level 2 — Repeatable

Common hunting queries are documented.

## Level 3 — Standardized

Queries use common schemas and naming conventions.

## Level 4 — Version Controlled

Queries are maintained as code.

## Level 5 — Automated

Queries are tested, deployed, monitored, and continuously improved.

---

# Enterprise Query Architecture

```text
                    THREAT INTELLIGENCE
                            │
                            ▼
                       HYPOTHESIS
                            │
                            ▼
                     QUERY LIBRARY
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
         Endpoint         Network       Identity
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                       SIEM / Data Lake
                            │
                            ▼
                         Results
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
        Investigation   Detection       Hunting
             │              │              │
             └──────────────┼──────────────┘
                            ▼
                       Feedback Loop
```

---

# Detection Engineering Handoff

A successful hunt should produce reusable security knowledge.

```text
Hunt
 │
 ▼
Finding
 │
 ▼
Behavior Characterization
 │
 ▼
Detection Logic
 │
 ▼
Test
 │
 ▼
Deploy
 │
 ▼
Monitor
```

---

# Final Takeaways

1. **A hunting query is an implementation of a security hypothesis.**
2. **Start with the behavior you want to understand, not the query language.**
3. **Validate telemetry before building complex logic.**
4. **Use normalized fields whenever possible.**
5. **Balance precision and recall.**
6. **Use aggregation to transform event volume into behavioral evidence.**
7. **Use time windows appropriate to the attack behavior.**
8. **Use entity and peer-group baselines to identify anomalies.**
9. **Correlate multiple weak signals instead of relying on one simplistic indicator.**
10. **Optimize queries for enterprise-scale data volumes.**
11. **Treat queries as code when they become operationally important.**
12. **Version, test, document, and review important hunting queries.**
13. **Monitor query health and schema drift.**
14. **Successful hunts should feed detection engineering.**
15. **The best query is not the most complicated query; it is the query that efficiently produces reliable investigative evidence.**

The core principle is:

> **Engineer the query around the behavior, validate the data, control the cost, measure the results, and preserve the logic so another analyst can reproduce the hunt.**

---

# References

- MITRE ATT&CK  
  https://attack.mitre.org/

- Sigma  
  https://sigmahq.io/

- SigmaHQ GitHub  
  https://github.com/SigmaHQ/sigma

- NIST SP 800-92 — Guide to Computer Security Log Management  
  https://csrc.nist.gov/publications/detail/sp/800-92/final

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

- Splunk Documentation  
  https://docs.splunk.com/

- Splunk Search Reference  
  https://docs.splunk.com/Documentation/Splunk/latest/SearchReference/

- Splunk Common Information Model  
  https://docs.splunk.com/Documentation/CIM/

- Microsoft Sentinel Documentation  
  https://learn.microsoft.com/azure/sentinel/

- Kusto Query Language  
  https://learn.microsoft.com/kusto/query/

- Elastic Security  
  https://www.elastic.co/security

- Elastic Common Schema  
  https://www.elastic.co/guide/en/ecs/current/index.html

- Open Cybersecurity Schema Framework  
  https://ocsf.io/

- MITRE CAR — Cyber Analytics Repository  
  https://car.mitre.org/

- CISA Cybersecurity Resources  
  https://www.cisa.gov/topics/cybersecurity
