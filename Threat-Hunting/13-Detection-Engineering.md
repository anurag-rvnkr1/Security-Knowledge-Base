# Detection Engineering

## Overview

Detection engineering is the discipline of designing, implementing, testing, deploying, tuning, and maintaining security detections that identify malicious or suspicious behavior from security telemetry.

Threat hunting asks:

> **What suspicious activity can we discover?**

Detection engineering asks:

> **How can we reliably identify this behavior again, at scale, with acceptable accuracy and operational cost?**

A mature security organization connects both disciplines:

```text
Threat Intelligence
        │
        ▼
Hunt Hypothesis
        │
        ▼
Threat Hunt
        │
        ▼
Behavior Identified
        │
        ▼
Detection Logic
        │
        ▼
Testing
        │
        ▼
Deployment
        │
        ▼
Alert
        │
        ▼
SOC Investigation
        │
        ▼
Feedback
        │
        └──────────────► Detection Improvement
```

Detection engineering is therefore not simply writing SIEM rules.

It is a continuous engineering lifecycle.

---

# Why Detection Engineering Matters

Modern enterprises generate enormous quantities of telemetry:

```text
Endpoints
Servers
Identity Systems
Cloud Platforms
Applications
Networks
Containers
Databases
SaaS
Email
DNS
```

Without detection engineering, this telemetry remains largely passive.

Detection engineering transforms:

```text
Raw Telemetry
      ↓
Security Logic
      ↓
Detection
      ↓
Alert
      ↓
Investigation
      ↓
Response
```

The objective is not to generate the maximum number of alerts.

The objective is to generate:

> **High-quality, actionable security signals.**

---

# Detection Engineering vs Threat Hunting

| Threat Hunting | Detection Engineering |
|---|---|
| Exploratory | Operational |
| Hypothesis driven | Behavior/rule driven |
| Often analyst initiated | Often continuously executed |
| May tolerate noise | Requires controlled noise |
| Finds unknown activity | Detects repeatable behavior |
| Temporary queries | Production detections |
| Investigation oriented | Alert/response oriented |

The two disciplines reinforce each other.

```text
Threat Hunt
    │
    ▼
Interesting Behavior
    │
    ▼
Detection Candidate
    │
    ▼
Detection Engineering
    │
    ▼
Production Detection
    │
    ▼
New Telemetry
    │
    ▼
Future Hunting
```

---

# Detection Engineering Lifecycle

```text
01. Identify Threat
        │
        ▼
02. Define Behavior
        │
        ▼
03. Identify Telemetry
        │
        ▼
04. Design Detection
        │
        ▼
05. Implement
        │
        ▼
06. Test
        │
        ▼
07. Validate
        │
        ▼
08. Deploy
        │
        ▼
09. Monitor
        │
        ▼
10. Tune
        │
        ▼
11. Measure
        │
        ▼
12. Retire / Improve
```

---

# Detection Objectives

Before writing a rule, define what it should accomplish.

Examples:

```text
Detect credential attacks
Detect privilege escalation
Detect lateral movement
Detect persistence
Detect data exfiltration
Detect malware execution
Detect cloud compromise
Detect identity abuse
```

A detection without a defined objective is difficult to evaluate.

---

# Detection Design Questions

Ask:

```text
What behavior am I detecting?

Which threat does it represent?

Which ATT&CK technique applies?

Which telemetry contains the evidence?

What does normal activity look like?

What makes the activity suspicious?

What context is required?

What should the SOC do when it triggers?
```

---

# Detection Types

Detection engineering commonly uses several approaches.

## Signature Detection

Matches known patterns.

Examples:

```text
Known malware hash
Known malicious domain
Known file path
Known command
```

Advantages:

- Simple
- Fast
- Easy to understand

Limitations:

- Easy to evade
- Poor coverage of unknown variants

---

# IOC Detection

Searches for known indicators.

```text
IP
Domain
URL
Hash
Email
Certificate
```

Useful for:

```text
Threat Intelligence
Retroactive Hunting
Known Campaigns
Incident Response
```

---

# Behavioral Detection

Detects activity patterns.

Example:

```text
PowerShell
+
Encoded Command
+
External Connection
```

Behavioral detection is generally more resilient to simple IOC changes.

---

# Threshold Detection

Example:

```text
More than 50 authentication failures
from one source within 10 minutes
```

Useful for:

```text
Brute Force
Password Spraying
Traffic Spikes
API Abuse
Scanning
```

---

# Anomaly Detection

Identifies deviations from expected behavior.

Example:

```text
User normally logs in from India.

Observed:
Login from a new geography
+
New device
+
Unusual time
```

Anomaly signals require context.

---

# Sequence Detection

Detects a sequence of events.

```text
Login
  ↓
Privilege Change
  ↓
Credential Access
  ↓
Lateral Movement
```

The individual events may be legitimate.

The sequence may be suspicious.

---

# Correlation Detection

Combines multiple data sources.

```text
Identity
   +
Endpoint
   +
Network
   +
Cloud
```

Example:

```text
Suspicious Login
      +
New Device
      +
PowerShell
      +
External Connection
```

---

# Risk-Based Detection

Instead of treating every signal independently:

```text
Signal A → +20
Signal B → +30
Signal C → +40

Total → 90
```

The SOC can prioritize higher-risk entities.

---

# Detection Pyramid

A useful conceptual model:

```text
                    Behavioral
                  /------------\
                 /   Anomaly    \
                /---------------\
               /   Correlation   \
              /-----------------\
             /     Threshold     \
            /---------------------\
           /      IOC / Hash       \
          /-------------------------\
         /      Basic Signature     \
        /---------------------------\
```

Lower layers are often easier to implement.

Higher layers can provide stronger contextual detection.

---

# Detection Coverage

Detection coverage should be mapped to threats and techniques.

Example:

```text
MITRE ATT&CK
      │
      ├── Initial Access
      ├── Execution
      ├── Persistence
      ├── Privilege Escalation
      ├── Defense Evasion
      ├── Credential Access
      ├── Discovery
      ├── Lateral Movement
      ├── Collection
      ├── Command & Control
      └── Exfiltration
```

Coverage should not be measured only by the number of rules.

---

# Detection Coverage Matrix

Example:

| Technique | Telemetry | Detection | Tested | Owner |
|---|---|---|---|---|
| PowerShell | EDR | Yes | Yes | SOC |
| Password Spray | Identity | Yes | Yes | SOC |
| DNS Tunneling | DNS | Yes | Partial | Network |
| Cloud Role Abuse | Cloud Audit | Yes | Yes | Cloud Sec |
| Process Injection | EDR | Partial | No | Endpoint |

This exposes gaps.

---

# Detection Gap

A detection gap occurs when:

```text
Threat
  ↓
Relevant Telemetry
  ↓
No Reliable Detection
```

Example:

```text
Cloud Privilege Escalation
        ↓
CloudTrail Available
        ↓
No Detection
```

This is an engineering priority.

---

# Detection Requirements

Every detection should have clearly defined requirements.

Example:

```yaml
name: Suspicious PowerShell Execution

objective: Detect potentially malicious PowerShell activity

telemetry:
  - endpoint_process
  - network

required_fields:
  - process.name
  - process.command_line
  - process.parent.name
  - user.name
  - host.name
```

---

# Detection Logic

The detection should explain:

```text
IF
    PowerShell executes
AND
    command contains suspicious behavior
AND
    parent process is unusual

THEN
    generate detection signal
```

Avoid opaque logic whenever possible.

---

# Detection Engineering Workflow

```text
Threat
 │
 ▼
Behavior
 │
 ▼
Telemetry
 │
 ▼
Query
 │
 ▼
Detection Logic
 │
 ▼
Test Dataset
 │
 ▼
Validation
 │
 ▼
Deployment
```

---

# Data Source Selection

Potential sources include:

```text
EDR
SIEM
Windows Event Logs
Sysmon
Linux Audit
DNS
Proxy
Firewall
Identity Provider
Cloud Audit Logs
Application Logs
Email Security
WAF
Kubernetes
```

Choose the source that provides the strongest evidence.

---

# Telemetry Requirements

A detection may fail because telemetry is incomplete.

Example:

```text
Detection requires:
Command Line

Telemetry provides:
Process Name only
```

The detection cannot reliably implement its intended logic.

---

# Telemetry Quality

Evaluate:

```text
Coverage
Completeness
Accuracy
Latency
Retention
Normalization
Timestamp Quality
Parsing
Availability
```

---

# Detection Data Pipeline

```text
Source
  │
  ▼
Collection
  │
  ▼
Transport
  │
  ▼
Parsing
  │
  ▼
Normalization
  │
  ▼
Enrichment
  │
  ▼
Detection
  │
  ▼
Alert
```

Failures anywhere can affect detection quality.

---

# Detection Schema

Normalized schemas improve portability.

Common concepts:

```text
user.name
host.name
source.ip
destination.ip
process.name
process.command_line
file.hash.sha256
network.protocol
event.action
event.outcome
```

Examples include:

- ECS
- CIM
- OCSF

---

# Sigma

Sigma provides a vendor-neutral way of describing detection logic.

Conceptually:

```text
Sigma Rule
    │
    ├── Splunk
    ├── Elastic
    ├── Sentinel
    └── Other Platforms
```

This enables detection logic to be separated from a specific backend.

---

# Example Sigma Structure

```yaml
title: Suspicious PowerShell Execution

id: example-detection-id

status: experimental

description: Detects potentially suspicious PowerShell behavior.

logsource:
  category: process_creation

detection:
  selection:
    Image|endswith:
      - '\powershell.exe'

  condition: selection

level: medium
```

Production rules should be significantly more context-aware and tested.

---

# Detection Metadata

Recommended metadata:

```yaml
id:
name:
description:
status:
severity:
confidence:
author:
owner:
version:
created:
modified:
references:
tags:
mitre_attack:
data_sources:
false_positives:
response:
```

---

# Severity vs Confidence

These are different.

## Severity

Potential impact.

```text
Low
Medium
High
Critical
```

## Confidence

Confidence that the activity is malicious.

```text
Low
Medium
High
```

Example:

```text
High Severity
+
Low Confidence
```

may require analyst validation before escalation.

---

# Detection Priority

A useful conceptual model:

```text
Priority =
Severity
×
Confidence
×
Asset Criticality
×
Threat Context
```

Exact implementation should be adapted to the organization.

---

# Alert Design

A detection should produce enough context for investigation.

Bad alert:

```text
Suspicious activity detected.
```

Better:

```text
Suspicious PowerShell Execution

Host: WS-102
User: alice
Parent: winword.exe
Process: powershell.exe
Command: ...
Destination: 198.51.100.20
Time: ...
Reason: Unusual parent + external connection
```

---

# Detection Context

Useful context:

```text
Asset
User
Process
Parent Process
Command Line
Source IP
Destination IP
Domain
Authentication
Cloud Account
Geo
Threat Intelligence
Historical Baseline
```

---

# Alert Enrichment

Enrichment can include:

```text
Asset Criticality
User Role
VIP Status
Threat Intelligence
GeoIP
WHOIS
Domain Age
Known Scanner
Known Service
Cloud Resource
Vulnerability Context
```

Enrichment should improve decisions, not simply increase alert size.

---

# Entity Context

Example:

```text
Alert
 │
 ├── User Profile
 ├── Host Profile
 ├── Historical Activity
 ├── Network Relationships
 └── Threat Intelligence
```

---

# Detection Correlation

A detection becomes stronger when multiple signals align.

```text
Identity Alert
      │
      ▼
Endpoint Alert
      │
      ▼
Network Alert
      │
      ▼
High-Confidence Incident
```

---

# Detection Chaining

Example:

```text
01 Login Anomaly
       ↓
02 Suspicious Process
       ↓
03 Credential Access
       ↓
04 Lateral Movement
```

This can represent an attack progression.

---

# Detection Dependencies

Document dependencies:

```text
Detection
  │
  ├── EDR
  ├── DNS
  ├── Identity
  └── Threat Intelligence
```

If one dependency fails, detection quality may degrade.

---

# Detection Testing

A production detection should be tested.

Testing should include:

```text
Positive Case
Negative Case
Boundary Case
Missing Data
Malformed Data
Case Variation
Legitimate Administrative Activity
Known Attack Simulation
```

---

# Positive Test

Expected malicious behavior:

```text
Test
 ↓
Detection triggers
```

---

# Negative Test

Expected benign behavior:

```text
Normal activity
 ↓
Detection does not trigger
```

---

# Boundary Test

Example:

```text
Threshold = 20

19 → No alert
20 → Defined behavior
21 → Alert
```

The exact expected result must be documented.

---

# Detection Testing Framework

```text
Test Data
    │
    ▼
Detection
    │
    ├── Expected Match
    └── Expected Non-Match
```

Automate this where practical.

---

# Atomic Red Team / Adversary Simulation

Authorized adversary simulation can validate detection coverage.

Conceptually:

```text
Technique Simulation
        ↓
Telemetry
        ↓
Detection
        ↓
Alert
        ↓
SOC Validation
```

Use only within authorized environments.

---

# Purple Teaming

Purple teaming combines:

```text
Red Team
+
Blue Team
```

to validate:

```text
Attack
→ Telemetry
→ Detection
→ Investigation
→ Response
```

---

# Detection Validation Questions

After testing:

```text
Did the event occur?

Was telemetry generated?

Was telemetry ingested?

Was it parsed?

Did the query match?

Was an alert generated?

Was context included?

Could the SOC investigate it?

Was the response actionable?
```

---

# False Positives

False positives occur when benign activity triggers a detection.

Examples:

```text
IT Administration
Security Testing
Vulnerability Scanning
Automation
Backup Systems
Monitoring
Software Deployment
```

False positives are not always a failure.

The objective is:

> **Understand and control them.**

---

# False Positive Analysis

For each false positive:

```text
Why did it trigger?

Is the behavior actually expected?

Can context distinguish it?

Can the rule be improved?

Should the activity be suppressed?

Is the telemetry misleading?
```

---

# Tuning

Tuning may involve:

```text
Thresholds
Time Windows
Entity Context
Allowlisting
Suppression
Correlation
Scoring
Field Conditions
```

---

# Dangerous Tuning

Avoid:

```text
Disable Detection
```

simply because:

```text
Too Many Alerts
```

Instead determine why the alerts occur.

---

# Tuning Lifecycle

```text
Alert
 │
 ▼
Investigate
 │
 ▼
Classify
 │
 ├── True Positive
 ├── Benign
 └── False Positive
       │
       ▼
    Improve
       │
       ▼
   Retest
```

---

# Alert Fatigue

Excessive alerts cause:

```text
Analyst Overload
       ↓
Delayed Investigations
       ↓
Missed Threats
       ↓
Reduced SOC Effectiveness
```

Detection engineering must therefore consider analyst capacity.

---

# Detection Quality Metrics

Useful metrics include:

```text
True Positives
False Positives
True Negatives
False Negatives
Alert Volume
Mean Time to Triage
Mean Time to Respond
Escalation Rate
Detection Coverage
```

---

# Precision

```text
Precision =
True Positives
-------------------------
True Positives + False Positives
```

High precision means alerts are generally useful.

---

# Recall

```text
Recall =
True Positives
-------------------------
True Positives + False Negatives
```

High recall means more relevant malicious activity is detected.

---

# F1 Score

A conceptual combined metric:

```text
F1 =
2 × Precision × Recall
----------------------
Precision + Recall
```

Security operations should not rely on F1 alone.

Business risk and analyst workflow matter.

---

# Detection Latency

Important timestamps:

```text
Attack Occurs
      ↓
Telemetry Generated
      ↓
Telemetry Ingested
      ↓
Detection Evaluated
      ↓
Alert Created
      ↓
Analyst Sees Alert
```

The difference between these points affects response time.

---

# Detection Freshness

A detection should operate on sufficiently recent telemetry.

Monitor:

```text
Event Timestamp
Ingestion Timestamp
Detection Timestamp
```

Large gaps may indicate pipeline problems.

---

# Detection Reliability

Track:

```text
Execution Success
Data Availability
Query Errors
Alert Generation
Latency
```

A theoretically excellent detection is useless if it repeatedly fails operationally.

---

# Detection Performance

Performance factors include:

```text
Data Volume
Search Range
Query Complexity
Joins
Regex
Aggregation
Cardinality
Correlation
Storage
```

Optimize production detections for predictable execution.

---

# Detection Optimization

General pattern:

```text
Reduce Dataset
      ↓
Filter Early
      ↓
Use Structured Fields
      ↓
Avoid Expensive Operations
      ↓
Aggregate Carefully
      ↓
Correlate Relevant Events
```

---

# High-Cardinality Problems

Examples:

```text
User IDs
URLs
Process IDs
Cloud Request IDs
Session IDs
```

High-cardinality fields can make aggregation expensive.

Use them deliberately.

---

# Joins

Joins can be useful:

```text
Identity
+
Endpoint
```

But large unrestricted joins can become expensive.

Prefer correlation strategies appropriate to the SIEM/data platform.

---

# Detection Scheduling

A detection may execute:

```text
Real Time
Every Minute
Every 5 Minutes
Every 15 Minutes
Hourly
Daily
```

The correct schedule depends on the threat.

---

# Real-Time Detection

Useful for:

```text
Credential Theft
Active Lateral Movement
Malware Execution
Account Takeover
Critical Cloud Changes
```

---

# Batch Detection

Useful for:

```text
Daily Anomalies
Long-Term Trends
Rare Behavior
Historical Correlation
```

---

# Detection Window

Example:

```text
Run every 5 minutes
Search previous 10 minutes
```

Overlap can help avoid missing events near evaluation boundaries.

But excessive overlap may duplicate alerts.

---

# Alert Deduplication

Multiple events may represent one incident.

Example:

```text
100 failed logins
```

should not necessarily create:

```text
100 separate alerts
```

Instead aggregate:

```text
Password Spray Alert
Source: X
Users: 70
Attempts: 100
```

---

# Alert Grouping

Group by entities such as:

```text
User
Host
Source IP
Incident
Campaign
Session
```

---

# Detection Suppression

Suppression can prevent repeated alerts.

Example:

```text
Same Host
Same Detection
Within 30 Minutes
```

→ one alert.

Suppression must preserve enough evidence for investigation.

---

# Detection Deduplication Risks

Over-aggressive deduplication can hide:

```text
Multiple Attackers
Multiple Victims
Multiple Campaigns
Escalation
Repeated Persistence
```

Use meaningful grouping keys.

---

# Detection-as-Code Repository

Example:

```text
detections/
│
├── sigma/
│   ├── windows/
│   ├── linux/
│   ├── cloud/
│   └── network/
│
├── splunk/
├── sentinel/
├── elastic/
│
├── tests/
│
├── schemas/
│
└── documentation/
```

---

# Detection Pull Request

A mature workflow:

```text
Developer
   │
   ▼
Detection Code
   │
   ▼
Automated Tests
   │
   ▼
Peer Review
   │
   ▼
Security Review
   │
   ▼
Performance Validation
   │
   ▼
Deployment
```

---

# Detection CI/CD

Possible pipeline:

```text
Git Push
   │
   ▼
Lint
   │
   ▼
Schema Validation
   │
   ▼
Unit Tests
   │
   ▼
Detection Tests
   │
   ▼
Build
   │
   ▼
Deploy
```

---

# Detection Regression Testing

A previously working detection can break because of:

```text
Schema Changes
Telemetry Changes
SIEM Changes
Query Changes
Parser Changes
Threshold Changes
```

Regression testing protects against silent failures.

---

# Detection Test Dataset

Maintain representative events:

```text
tests/
│
├── positive/
├── negative/
├── edge/
└── regression/
```

Each test should have an expected outcome.

---

# Detection Documentation

Each production detection should document:

```text
Name
Purpose
Threat
Technique
Data Sources
Required Fields
Logic
Severity
Confidence
False Positives
Response
Testing
Performance
Owner
Version
Review Date
```

---

# Detection Runbook

A detection should connect to an investigation procedure.

Example:

```text
Detection
    ↓
Validate Alert
    ↓
Identify User
    ↓
Identify Host
    ↓
Review Process Tree
    ↓
Review Network Activity
    ↓
Review Authentication
    ↓
Check Threat Intelligence
    ↓
Contain if Necessary
```

---

# Detection-to-Response Mapping

```text
Detection
   │
   ├── Triage
   ├── Enrichment
   ├── Investigation
   ├── Containment
   ├── Eradication
   └── Recovery
```

---

# Detection Ownership

Assign ownership.

Example:

```text
Detection:
Cloud IAM Privilege Change

Owner:
Cloud Security

Reviewer:
SOC Engineering

Escalation:
Incident Response
```

Ownership prevents abandoned detections.

---

# Detection Review Cycle

Review:

```text
Monthly
Quarterly
After Major Incident
After Schema Change
After Platform Migration
```

The exact cadence should match risk and organizational change.

---

# Detection Retirement

A detection should eventually be retired when:

```text
Threat No Longer Relevant
Telemetry Removed
Replacement Detection Exists
Duplicate Detection
Unacceptable Cost
Technology Deprecated
```

Retirement should be documented.

---

# Detection Debt

Detection debt is similar to technical debt.

Examples:

```text
Old Rules
Unowned Rules
Untested Rules
Broken Rules
Duplicate Rules
Excessive Exceptions
Missing Documentation
```

Detection debt reduces SOC effectiveness.

---

# Detection Inventory

Maintain a central inventory:

| ID | Name | Source | Technique | Owner | Status |
|---|---|---|---|---|---|
| DET-001 | Password Spray | Identity | T1110.003 | SOC | Active |
| DET-002 | Suspicious PowerShell | EDR | T1059.001 | Endpoint | Active |
| DET-003 | DNS Tunneling | DNS | T1071.004 | Network | Testing |
| DET-004 | Cloud IAM Abuse | Cloud | T1098 | Cloud Sec | Active |

---

# Detection Coverage Mapping

```text
Threat
  │
  ▼
ATT&CK Technique
  │
  ▼
Telemetry
  │
  ▼
Detection
  │
  ▼
Test
  │
  ▼
Runbook
```

Every important threat should ideally have this chain.

---

# Detection Engineering Example

## Scenario

A SOC wants to detect suspicious remote PowerShell execution.

### Threat

Remote execution following credential compromise.

### Hypothesis

A compromised account may remotely execute PowerShell on another Windows host.

### Evidence

```text
Remote Authentication
+
PowerShell Process
+
Remote Source
+
Unusual User/Host Relationship
```

### Correlation

```text
Authentication
      │
      ▼
Target Host
      │
      ▼
PowerShell
      │
      ▼
Command Line
```

### Enrichment

```text
User Role
Host Criticality
Source Reputation
Historical Relationship
```

### Alert

```text
Suspicious Remote PowerShell

User: user01
Source: workstation-17
Target: server-23
Process: powershell.exe
Parent: wsmprovhost.exe
Reason:
Unusual remote execution relationship
```

---

# Detection Engineering Example — Password Spray

## Logic

```text
IF

authentication failures

FROM

one source

AGAINST

many unique accounts

WITHIN

defined time window

THEN

generate detection
```

Additional context:

```text
Source Reputation
Geography
Authentication Protocol
Successful Login After Failures
Target Privilege
```

---

# Detection Engineering Example — DNS Tunneling

## Logic

```text
IF

DNS query volume is unusual

AND

labels are unusually long/high entropy

AND

domain is rare

AND

query intervals are regular

THEN

raise suspicious DNS behavior
```

Do not rely on one feature alone.

---

# Detection Engineering Example — Cloud Credential Abuse

```text
New Credential
      +
New Geography
      +
Unusual User-Agent
      +
Sensitive API Calls
```

This combined signal can be more useful than any individual event.

---

# Detection Engineering Example — Account Takeover

```text
New Login Location
        +
New Device
        +
MFA Anomaly
        +
Sensitive Action
```

This represents a behavioral chain.

---

# Threat-Informed Detection Engineering

Detection priorities should be influenced by:

```text
Threat Intelligence
+
Organization Assets
+
Business Risk
+
Known Attack Paths
+
Historical Incidents
```

Do not attempt to detect everything equally.

---

# Crown Jewel Detection

Critical assets deserve stronger detection coverage.

Examples:

```text
Domain Controllers
Identity Providers
Payment Systems
Production Databases
Source Code Platforms
Cloud Control Plane
Security Infrastructure
```

---

# Attack Path Detection

Think beyond individual events.

```text
Initial Access
      ↓
Execution
      ↓
Privilege Escalation
      ↓
Credential Access
      ↓
Lateral Movement
      ↓
Collection
      ↓
Exfiltration
```

Detection coverage should address meaningful portions of the attack path.

---

# Detection Engineering and MITRE ATT&CK

ATT&CK can provide:

```text
Technique
Sub-Technique
Data Sources
Detection Ideas
Procedure Examples
```

Use ATT&CK as a framework, not as proof that an environment is fully protected.

---

# Detection Coverage Limitations

A technique may be:

```text
Mapped
```

but not necessarily:

```text
Well Detected
```

Coverage should consider:

```text
Telemetry
Detection
Testing
Precision
Recall
Response
```

---

# Detection Maturity Model

## Level 1 — Reactive

Rules are created after incidents.

## Level 2 — Signature Driven

IOC and known-pattern detection.

## Level 3 — Behavioral

Behavior-based detection introduced.

## Level 4 — Threat-Informed

Detection priorities based on intelligence and risk.

## Level 5 — Detection-as-Code

Automated testing and version control.

## Level 6 — Continuous Validation

Purple-team validation, telemetry health, and continuous improvement.

---

# Practical Lab 1 — Build a PowerShell Detection

## Objective

Create a detection for suspicious PowerShell execution.

## Steps

1. Identify PowerShell telemetry.
2. Identify process fields.
3. Build broad query.
4. Add command-line context.
5. Add parent process.
6. Add network context.
7. Test benign activity.
8. Test authorized simulation.
9. Tune.
10. Document.

---

# Practical Lab 2 — Password Spray Detection

## Objective

Detect one source authenticating against multiple accounts.

### Required fields

```text
timestamp
source.ip
user.name
event.outcome
```

### Logic

```text
Filter failures
      ↓
Group by source
      ↓
Count unique users
      ↓
Count attempts
      ↓
Apply threshold
```

### Validation

Generate authorized authentication failures in a lab environment and confirm:

```text
Telemetry
   ↓
Query
   ↓
Detection
   ↓
Alert
```

---

# Practical Lab 3 — DNS Detection

## Objective

Identify suspicious DNS behavior.

Analyze:

```text
Query Volume
Unique Domains
Label Length
Entropy
NXDOMAIN
TXT
Query Intervals
```

Create a combined detection candidate.

---

# Practical Lab 4 — Detection-as-Code

Create:

```text
detections/
├── rules/
├── tests/
├── schemas/
└── docs/
```

Implement:

```text
Rule
+
Positive Test
+
Negative Test
+
Documentation
```

Commit everything to version control.

---

# Practical Lab 5 — Purple Team Validation

Choose an authorized technique.

Process:

```text
Attack Simulation
       ↓
Telemetry Validation
       ↓
Detection Validation
       ↓
Alert Review
       ↓
SOC Investigation
       ↓
Tuning
       ↓
Retest
```

Document:

```text
Expected
Observed
Gap
Improvement
Result
```

---

# Detection Engineering Checklist

## Threat Modeling

- [ ] Threat identified
- [ ] Behavior defined
- [ ] ATT&CK mapping considered
- [ ] Business impact understood

## Telemetry

- [ ] Data source identified
- [ ] Required fields available
- [ ] Coverage measured
- [ ] Parsing validated
- [ ] Timestamp quality checked

## Detection

- [ ] Logic documented
- [ ] Severity defined
- [ ] Confidence defined
- [ ] Context included
- [ ] Correlation considered

## Testing

- [ ] Positive test
- [ ] Negative test
- [ ] Edge test
- [ ] Regression test
- [ ] Authorized simulation

## Operations

- [ ] Owner assigned
- [ ] Runbook created
- [ ] Alert grouping defined
- [ ] Suppression reviewed
- [ ] Performance evaluated

## Maintenance

- [ ] Version controlled
- [ ] Review date assigned
- [ ] Schema drift monitored
- [ ] False positives reviewed
- [ ] Detection debt tracked

---

# Common Detection Engineering Mistakes

## 1. Alert Everything

More alerts do not equal better security.

---

## 2. Detect Only IOCs

Attackers can change infrastructure.

---

## 3. Ignore Context

A suspicious event without context may be meaningless.

---

## 4. No Testing

Untested detections create false confidence.

---

## 5. Hard-Coded Assumptions

Enterprise environments change.

---

## 6. Excessive Allowlisting

Attackers can abuse trusted entities.

---

## 7. No Ownership

Unowned detections eventually decay.

---

## 8. No Performance Testing

Expensive rules can affect SIEM operations.

---

## 9. No Runbook

The SOC may receive an alert without knowing what to do.

---

## 10. No Feedback Loop

Detection quality must improve from investigation results.

---

# Professional Detection Record

```text
Detection ID:
Detection Name:

Objective:

Threat Scenario:

MITRE ATT&CK:

Severity:

Confidence:

Data Sources:

Required Fields:

Detection Logic:

Time Window:

Schedule:

Aggregation:

Correlation:

Enrichment:

Known False Positives:

Suppression:

Test Cases:

Performance Notes:

Response Procedure:

Owner:

Reviewer:

Version:

Created:

Last Modified:

Next Review:
```

---

# Enterprise Detection Architecture

```text
                       THREAT INTELLIGENCE
                               │
                               ▼
                         THREAT MODEL
                               │
                               ▼
                          HYPOTHESIS
                               │
                               ▼
                      DETECTION ENGINEERING
                               │
             ┌─────────────────┼─────────────────┐
             ▼                 ▼                 ▼
         Endpoint           Identity           Network
             │                 │                 │
             └─────────────────┼─────────────────┘
                               ▼
                         DATA PLATFORM
                       / SIEM / Data Lake
                               │
                               ▼
                         DETECTION LAYER
                               │
                               ▼
                           ALERTING
                               │
                               ▼
                              SOC
                               │
                 ┌─────────────┼─────────────┐
                 ▼             ▼             ▼
             Triage       Investigation    Response
                 │             │             │
                 └─────────────┼─────────────┘
                               ▼
                         FEEDBACK LOOP
                               │
                               └──────────► Detection Improvement
```

---

# Detection Engineering Operating Model

A mature team may include:

```text
Threat Hunter
Detection Engineer
SOC Analyst
Incident Responder
Threat Intelligence Analyst
Cloud Security Engineer
Endpoint Engineer
Network Security Engineer
```

Responsibilities should overlap enough to create feedback but remain clearly owned.

---

# Detection Engineer Responsibilities

Typical responsibilities include:

- Develop detections
- Maintain detection content
- Validate telemetry
- Build tests
- Tune rules
- Analyze false positives
- Optimize queries
- Map detections to threats
- Maintain detection documentation
- Support SOC investigations
- Perform detection gap analysis
- Conduct purple-team validation
- Monitor detection health

---

# SOC Feedback Loop

```text
Detection
   ↓
Alert
   ↓
Analyst Investigation
   ↓
True Positive / False Positive
   ↓
Feedback
   ↓
Detection Engineering
   ↓
Improved Detection
```

The SOC is one of the most important sources of detection-quality feedback.

---

# Detection Engineering KPIs

Possible metrics:

```text
Detection Coverage
True Positive Rate
False Positive Rate
Mean Time to Detect
Mean Time to Triage
Mean Time to Respond
Detection Availability
Detection Test Coverage
Detection Review Compliance
Alert Volume
Alert-to-Incident Conversion
```

Metrics should be interpreted together.

---

# Important Principle

A detection that generates 10,000 alerts with no useful signal is not necessarily better than a detection generating 50 high-quality alerts.

Measure:

```text
Security Value
+
Operational Cost
```

---

# Final Takeaways

1. **Detection engineering turns threat knowledge into repeatable security controls.**
2. **Good detections begin with clearly defined threat behavior.**
3. **Telemetry quality determines detection quality.**
4. **Behavioral and contextual detections can provide resilience against changing indicators.**
5. **Detection logic should be explainable and testable.**
6. **Every production detection should have an owner and documentation.**
7. **Positive, negative, boundary, and regression testing are essential.**
8. **False-positive management is an engineering problem, not simply an analyst problem.**
9. **Detection performance matters at enterprise scale.**
10. **Alert grouping and suppression should reduce noise without hiding meaningful activity.**
11. **Detection-as-code enables version control, review, automation, and reproducibility.**
12. **Purple-team exercises provide valuable validation of real detection coverage.**
13. **Detection coverage should be mapped to threats, telemetry, tests, and response—not merely ATT&CK techniques.**
14. **Detection debt must be actively managed.**
15. **The strongest detection programs continuously learn from threat hunting, incidents, intelligence, and SOC feedback.**

The central principle is:

> **A detection is not complete when the query works. It is complete when the organization can reliably detect the behavior, validate the signal, investigate the alert, respond to it, measure its quality, and continuously improve it.**

---

# References

- MITRE ATT&CK  
  https://attack.mitre.org/

- MITRE Cyber Analytics Repository  
  https://car.mitre.org/

- SigmaHQ  
  https://sigmahq.io/

- Sigma GitHub  
  https://github.com/SigmaHQ/sigma

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

- NIST SP 800-61 — Computer Security Incident Handling Guide  
  https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

- NIST SP 800-92 — Guide to Computer Security Log Management  
  https://csrc.nist.gov/publications/detail/sp/800-92/final

- Splunk Security Content  
  https://research.splunk.com/

- Splunk Documentation  
  https://docs.splunk.com/

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

- Atomic Red Team  
  https://atomicredteam.io/

- MITRE Caldera  
  https://caldera.mitre.org/
