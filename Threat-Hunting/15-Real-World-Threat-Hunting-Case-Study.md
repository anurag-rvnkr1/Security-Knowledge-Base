# Real-World Threat Hunting Case Study

## Overview

This chapter presents a complete, realistic enterprise threat-hunting case study.

The objective is to demonstrate how a security team can move from:

```text
Threat Intelligence
        ↓
Hunt Hypothesis
        ↓
Telemetry Validation
        ↓
Threat Hunting
        ↓
Entity Pivoting
        ↓
Correlation
        ↓
Timeline Reconstruction
        ↓
Threat Validation
        ↓
Incident Escalation
        ↓
Detection Engineering
        ↓
Lessons Learned
```

The case study is intentionally structured as a **defensive investigation**.

All infrastructure, identities, domains, IP addresses, timestamps, and organizations used in the scenario are fictional or sanitized.

---

# Case Study Scenario

## Organization

Consider a fictional enterprise:

```text
Organization: Northstar Financial Services

Industry: Financial Services

Employees: ~8,000

Endpoints: ~6,000

Servers: ~1,200

Cloud:
    Microsoft Azure
    AWS

Security Stack:
    SIEM
    EDR
    Identity Provider
    DNS Logging
    Proxy
    Firewall
    Cloud Audit Logs
    Email Security
```

---

# Security Team

The organization has:

```text
SOC Analysts
Threat Hunters
Detection Engineers
Incident Responders
Cloud Security Engineers
Identity Security Engineers
Threat Intelligence Analysts
```

---

# Existing Architecture

```text
                    INTERNET
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
        Email         VPN        Web Apps
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Identity Layer
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
         Endpoints   Servers    Cloud
             │         │         │
             └─────────┼─────────┘
                       ▼
                     SIEM
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Detection    Hunting      SOC
          │            │            │
          └────────────┼────────────┘
                       ▼
                    Response
```

---

# Threat Intelligence Trigger

The threat intelligence team receives information about an active campaign targeting organizations in the same industry.

The intelligence describes:

```text
Initial Access:
Phishing / Credential Theft

Follow-On Activity:
Valid Account Use

Potential Behavior:
PowerShell
Cloud Access
Credential Discovery
Lateral Movement
Data Collection
```

The intelligence team does not have a confirmed indicator matching Northstar.

This is important.

The team cannot simply search for a known malicious IP or hash.

Instead, the threat hunters must investigate the **behavior**.

---

# Hunt Objective

The threat-hunting team defines the objective:

> Determine whether Northstar has experienced suspicious identity activity followed by endpoint or cloud behavior consistent with the reported campaign.

---

# Hunt Hypothesis

The primary hypothesis becomes:

> **A compromised user account may have been used from an unusual source or device, followed by suspicious endpoint or cloud activity.**

---

# Secondary Hypotheses

The team creates additional hypotheses:

```text
H1:
A valid account may be compromised.

H2:
The compromised account may be used from an unusual device or location.

H3:
The account may execute suspicious PowerShell.

H4:
The attacker may access additional internal systems.

H5:
The attacker may access cloud resources.

H6:
The attacker may attempt persistence or privilege escalation.

H7:
The attacker may stage or exfiltrate information.
```

---

# MITRE ATT&CK Mapping

Potential techniques:

```text
T1078     Valid Accounts
T1059.001 PowerShell
T1021     Remote Services
T1087     Account Discovery
T1053     Scheduled Task/Job
T1550     Use Alternate Authentication Material
T1110     Brute Force
T1041     Exfiltration Over C2 Channel
```

The exact mapping should be validated against the observed behavior.

---

# Hunt Scope

The team defines:

```text
Time Range:
Previous 30 days

Identity:
All workforce accounts

Endpoints:
All managed endpoints

Cloud:
Production cloud accounts

Network:
DNS + Proxy + Firewall

Priority:
Privileged and sensitive users first
```

---

# Phase 1 — Telemetry Validation

Before hunting, the team validates available data.

Required sources:

```text
Identity
Endpoint
DNS
Proxy
Firewall
Cloud Audit
Email
```

---

# Telemetry Health

Example:

```text
Source             Status

Identity           Healthy
EDR                Healthy
DNS                Healthy
Proxy              Healthy
Firewall           Healthy
Cloud Audit        Healthy
Email              Healthy
```

The team confirms that the required data is available.

---

# Phase 2 — Identity Hunt

The first hypothesis is:

> A valid account may have been used unusually.

The team searches for:

```text
New Locations
New Devices
New Source IPs
Unusual User Agents
Impossible Travel
Authentication Failures
MFA Anomalies
Privileged Login
```

---

# Initial Identity Finding

One account stands out:

```text
User:
alex.morgan

Role:
Finance Operations

Normal Location:
Bengaluru

Normal Devices:
FIN-LT-221
FIN-LT-221-VPN
```

The account shows:

```text
Normal:
Bengaluru
Corporate Laptop

Observed:
New Source
New Device
Unusual Time
```

---

# Authentication Timeline

```text
01:42:13
Authentication Failure

01:42:25
Authentication Failure

01:42:39
Successful Authentication

01:43:01
MFA Approval

01:45:12
Cloud Session Created
```

This pattern is suspicious.

It is not yet proof of compromise.

---

# Investigation Question

The analyst asks:

> Was this simply a legitimate user traveling or using a new device?

The team investigates:

```text
Travel Records
VPN
Device Inventory
User Activity
MFA History
```

No corresponding approved travel or device registration is found.

---

# Initial Assessment

Confidence:

```text
Medium
```

Reason:

```text
Unusual Source
+
New Device
+
Authentication Failures
+
Successful Login
```

The team does not yet declare compromise.

---

# Phase 3 — Entity Pivot

The analyst pivots from:

```text
User
```

to:

```text
Source IP
Device
Cloud Session
Authentication
Endpoint
DNS
```

Graph:

```text
                    alex.morgan
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
     Source IP       New Device     Cloud Session
          │              │              │
          ▼              ▼              ▼
       DNS          Processes       API Calls
```

---

# Source IP Investigation

The source IP is:

```text
198.51.100.42
```

This is a documentation-only example address.

The analyst checks:

```text
Threat Intelligence
ASN
Geolocation
Historical Usage
Other Users
```

The IP is not previously associated with Northstar.

---

# IP Reuse Analysis

The analyst asks:

> Has any other employee used this source?

Results:

```text
User                  Attempts

alex.morgan            4
other-user-1           0
other-user-2           0
```

This increases suspicion.

---

# Phase 4 — Device Investigation

The new device identifier is:

```text
Device:
UNKNOWN-DEVICE-442
```

It is not present in the organization's managed-device inventory.

The analyst checks:

```text
EDR
MDM
Identity Provider
VPN
Asset Inventory
```

No managed endpoint exists with this identity.

---

# Investigation Finding

The identity appears to have been used from:

```text
Unknown Device
+
Unknown Source
+
Unusual Time
```

Confidence increases.

```text
Medium → Medium/High
```

---

# Phase 5 — Endpoint Correlation

The analyst now searches for activity associated with the user around the authentication event.

Search:

```text
User
+
Host
+
Process
+
Network
```

A related endpoint is identified:

```text
FIN-LT-221
```

---

# Process Investigation

The timeline contains:

```text
01:51
winword.exe

01:51
powershell.exe

01:52
powershell.exe

01:53
network connection
```

---

# Process Tree

```text
WINWORD.EXE
    │
    └── powershell.exe
            │
            ├── child process
            └── network connection
```

This parent-child relationship is unusual for the user's normal activity.

---

# Command-Line Investigation

The command line contains suspicious scripting behavior.

The analyst records:

```text
Process:
powershell.exe

Parent:
winword.exe

User:
alex.morgan

Host:
FIN-LT-221
```

The full command line is preserved in the investigation record according to evidence-handling procedures.

---

# Endpoint Baseline

Historical activity for `alex.morgan` shows:

```text
PowerShell:
Rare

Office → PowerShell:
Never observed

External PowerShell Network:
Never observed
```

This is significant.

---

# Phase 6 — Network Investigation

The analyst pivots from the endpoint to network activity.

Search:

```text
Host
+
Destination
+
DNS
+
Proxy
```

---

# DNS Finding

The endpoint queried:

```text
update-example.invalid
```

This is a fictional documentation domain.

The domain was:

```text
Rare
Recently observed
Only associated with one endpoint
```

---

# DNS Timeline

```text
01:52:03
DNS Query

01:52:13
DNS Query

01:52:23
DNS Query

01:52:33
DNS Query
```

The interval is approximately:

```text
10 seconds
```

---

# Beaconing Hypothesis

The team now considers:

> The endpoint may be periodically communicating with external infrastructure.

However:

> Regular DNS intervals alone do not prove command and control.

---

# DNS Correlation

The analyst correlates:

```text
DNS
+
Process
+
Endpoint
+
User
```

The DNS activity occurs shortly after the suspicious PowerShell process starts.

---

# Combined Evidence

```text
Unusual Authentication
        │
        ▼
Unknown Device
        │
        ▼
Known Corporate User
        │
        ▼
Office → PowerShell
        │
        ▼
External Network Activity
        │
        ▼
Repeated DNS Queries
```

This is significantly more concerning than any individual event.

---

# Phase 7 — User Behavior Analysis

The analyst reviews the previous 30 days.

Normal:

```text
Login:
08:30–18:30

Devices:
Corporate Laptop

PowerShell:
Rare

Cloud:
Finance applications
```

Observed:

```text
01:42 Login
Unknown Source
Unknown Device
PowerShell
External DNS
Cloud Session
```

The deviation is substantial.

---

# Phase 8 — Cloud Investigation

The cloud security team investigates the cloud session.

Events include:

```text
Login
Session Creation
Storage Enumeration
Resource Discovery
```

The user normally does not perform these actions at that time.

---

# Cloud API Timeline

```text
01:45
Session Created

01:46
Resource Discovery

01:48
Storage Enumeration

01:50
Sensitive Resource Query
```

---

# Identity + Endpoint + Cloud Correlation

The investigation now shows:

```text
Authentication
       │
       ▼
Endpoint Execution
       │
       ▼
Network Activity
       │
       ▼
Cloud Session
       │
       ▼
Cloud Discovery
```

---

# Phase 9 — Lateral Movement Hunt

The team investigates whether the compromised identity accessed other systems.

Search:

```text
User
+
Source Host
+
Destination Host
+
Authentication
```

---

# Lateral Movement Finding

The account accessed:

```text
FIN-SRV-14
FIN-SRV-19
```

These systems are outside the user's normal access pattern.

---

# Relationship Baseline

Historical relationship:

```text
alex.morgan
     ↓
FIN-LT-221
```

Observed:

```text
alex.morgan
     ├── FIN-LT-221
     ├── FIN-SRV-14
     └── FIN-SRV-19
```

This is suspicious.

---

# Phase 10 — Privilege Investigation

The team checks whether privileges changed.

Search:

```text
Group Changes
Role Changes
Account Changes
Privilege Events
Cloud IAM
```

No permanent privilege escalation is found.

This is an important negative finding.

---

# Negative Evidence

The investigation records:

```text
No confirmed new privileged group membership.
No confirmed permanent cloud role escalation.
```

Negative evidence is still useful.

---

# Phase 11 — Persistence Hunt

The team searches for persistence.

Windows:

```text
Scheduled Tasks
Services
Registry Run Keys
WMI
Startup
```

Cloud:

```text
New Access Keys
New Service Principals
OAuth Applications
Role Changes
```

---

# Persistence Result

No confirmed persistence mechanism is identified.

However:

```text
Temporary Cloud Session
```

was observed.

The investigation continues.

---

# Phase 12 — Data Access

The team investigates sensitive data access.

Search:

```text
Finance Data
Cloud Storage
File Servers
Database Access
```

---

# Data Access Finding

The account accessed several finance-related files.

The access was unusual for the user's historical behavior.

---

# Data Staging Investigation

The endpoint shows:

```text
File Access
     ↓
Archive Creation
```

An archive is created in a temporary directory.

---

# Staging Hypothesis

The team considers:

> The attacker may be preparing data for exfiltration.

---

# Exfiltration Investigation

Network telemetry is reviewed.

The endpoint establishes an outbound connection shortly after archive creation.

The team correlates:

```text
Archive Creation
+
DNS
+
Network Connection
```

---

# Important Limitation

The available telemetry does not conclusively establish that sensitive data was successfully exfiltrated.

Therefore the investigation records:

```text
Potential Exfiltration
```

rather than:

```text
Confirmed Exfiltration
```

This distinction is essential.

---

# Phase 13 — Attack Timeline

The team reconstructs the complete sequence.

```text
01:42
Authentication Failures
        │
        ▼
01:42
Successful Login
        │
        ▼
01:43
MFA Approval
        │
        ▼
01:45
Cloud Session
        │
        ▼
01:51
Office Process
        │
        ▼
01:51
PowerShell
        │
        ▼
01:52
DNS Activity
        │
        ▼
01:55
Lateral Movement
        │
        ▼
02:03
Sensitive Data Access
        │
        ▼
02:07
Archive Creation
        │
        ▼
02:09
Outbound Connection
```

---

# Attack Chain

Conceptually:

```text
Credential Compromise
        │
        ▼
Valid Account Use
        │
        ▼
Endpoint Execution
        │
        ▼
Command Execution
        │
        ▼
Network Communication
        │
        ▼
Lateral Movement
        │
        ▼
Collection
        │
        ▼
Potential Exfiltration
```

---

# Phase 14 — Threat Assessment

The investigation now has multiple correlated signals.

Evidence:

```text
✓ Unusual authentication
✓ Unknown device
✓ Unknown source
✓ Suspicious process tree
✓ Rare PowerShell
✓ External DNS activity
✓ Unusual cloud activity
✓ Unusual lateral movement
✓ Sensitive data access
✓ Archive creation
✓ Outbound connection
```

---

# Confidence Assessment

The team assesses:

```text
Confidence:
High
```

Reason:

Multiple independent telemetry sources support the same attack narrative.

---

# Incident Escalation

The hunt is converted into an incident.

```text
Threat Hunt
    ↓
High-Confidence Finding
    ↓
Incident Record
    ↓
Incident Response
```

---

# Incident Scope

The team identifies:

```text
Primary User:
alex.morgan

Primary Endpoint:
FIN-LT-221

Potentially Accessed:
FIN-SRV-14
FIN-SRV-19

Cloud Session:
Associated with user

Potential Data:
Finance documents
```

---

# Phase 15 — Containment

Containment should follow organizational incident-response procedures.

Potential actions may include:

```text
Account Session Revocation
Credential Reset
Endpoint Isolation
Token Revocation
Cloud Session Termination
Blocking Confirmed Malicious Infrastructure
```

Actions must be authorized and carefully logged.

---

# Important Principle

Do not immediately destroy evidence.

For example:

```text
Do not:
Delete suspicious files
Wipe systems
Destroy logs
```

before appropriate evidence preservation and incident-response procedures.

---

# Phase 16 — Evidence Preservation

Preserve relevant:

```text
Identity Logs
EDR Events
Process Trees
DNS Logs
Proxy Logs
Firewall Logs
Cloud Audit Logs
Email Logs
File Access Logs
```

Maintain:

```text
Timestamp
Source
Query
Analyst
Action
```

---

# Phase 17 — Root Cause Investigation

The team investigates how the attacker obtained access.

Potential paths:

```text
Phishing
Credential Theft
Password Reuse
Session Theft
MFA Abuse
Compromised Device
```

---

# Email Investigation

Search the user's mailbox around the preceding days.

Potential indicators:

```text
Unexpected Login Link
Credential Request
Malicious Attachment
Fake Document
OAuth Consent
Suspicious Sender
```

---

# Example Finding

The user received an unexpected document shortly before the compromise.

The document contained a link to a fake authentication page.

This provides a plausible initial-access path.

---

# Attack Narrative

The investigation develops the following hypothesis:

```text
Phishing
   ↓
Credential Theft
   ↓
Valid Account
   ↓
Unusual Login
   ↓
Endpoint Execution
   ↓
Lateral Movement
   ↓
Data Collection
   ↓
Potential Exfiltration
```

---

# Confidence Boundaries

The team distinguishes between:

## Confirmed

```text
Valid account was used unusually.
Suspicious endpoint activity occurred.
Lateral movement occurred.
Sensitive data was accessed.
```

## Likely

```text
Credential theft occurred.
PowerShell was attacker-controlled.
```

## Possible

```text
Sensitive data was exfiltrated.
```

This prevents overclaiming.

---

# Phase 18 — Detection Gap Analysis

The organization asks:

> Why did existing detections not stop or alert on this activity earlier?

---

# Existing Detections

The environment already had:

```text
Password Spray Detection
PowerShell Detection
Cloud Login Detection
```

But none produced a high-priority incident.

---

# Gap 1 — Identity Detection

Existing detection required:

```text
Large Authentication Failure Volume
```

The attacker used only a few attempts.

Therefore:

```text
Password Spray Detection
       ↓
Not Triggered
```

---

# Gap 2 — PowerShell Detection

The existing rule detected known suspicious command patterns.

The observed command did not match those patterns.

Therefore:

```text
PowerShell Execution
       ↓
Detection
       ↓
No Alert
```

---

# Gap 3 — Identity + Endpoint Correlation

No rule correlated:

```text
New Device
+
Unusual Login
+
PowerShell
```

This became a major detection gap.

---

# Gap 4 — Cloud Correlation

Cloud activity was analyzed separately.

No cross-domain correlation existed between:

```text
Identity
+
Endpoint
+
Cloud
```

---

# Detection Engineering Opportunity

Create a new detection:

> **Suspicious Valid Account Activity Across Identity, Endpoint, and Cloud**

---

# Detection Logic

Conceptually:

```text
New / Unusual Authentication
        +
New Device or Source
        +
Suspicious Endpoint Behavior
        +
Unusual Cloud Activity
```

The combined score should exceed a defined risk threshold.

---

# Detection Model

```text
Identity Anomaly
      │
      ├── +20
      │
      ▼
Endpoint Anomaly
      │
      ├── +30
      │
      ▼
Cloud Anomaly
      │
      ├── +30
      │
      ▼
Sensitive Resource Access
      │
      ├── +20
      │
      ▼
Risk = 100
```

The exact scoring system must be tuned for the environment.

---

# Detection Testing

The detection is tested against:

```text
Normal User
Traveling User
New Device
Compromised Account Simulation
Administrative Activity
Service Account
```

---

# False Positive Testing

A legitimate user may:

```text
Travel
Use VPN
Change Device
Access Cloud
Run PowerShell
```

Therefore the detection should not trigger solely on one anomaly.

---

# Detection Correlation

The improved model uses:

```text
Identity
   +
Endpoint
   +
Cloud
   +
Asset Criticality
```

---

# Detection Output

Example:

```text
Detection:
Suspicious Valid Account Activity

User:
alex.morgan

Risk:
High

Signals:
- New Device
- Unusual Login
- Suspicious PowerShell
- Rare Cloud Activity
- Sensitive Data Access

Recommended Action:
Investigate identity and endpoint immediately.
```

---

# Phase 19 — Threat Intelligence Update

The incident produces new intelligence.

Potential intelligence:

```text
Infrastructure
Domains
IP Addresses
Attack Behavior
Initial Access Method
TTPs
```

Only validated indicators should be shared as confirmed intelligence.

---

# Intelligence Confidence

Example:

```text
Observed Behavior:
High Confidence

Malicious Domain:
High Confidence

Phishing Infrastructure:
Medium Confidence

Attribution:
Unknown
```

Do not infer attribution without sufficient evidence.

---

# Phase 20 — Detection Improvement

The organization creates:

```text
New Detection
+
New Hunt Playbook
+
New Dashboard
+
New Intelligence
```

---

# New Hunt Playbook

Future hunts will search for:

```text
Unusual Identity
+
New Device
+
Suspicious Endpoint
+
Cloud Activity
```

---

# Phase 21 — Lessons Learned

The team identifies:

### Lesson 1

Single-event detection was insufficient.

### Lesson 2

Identity telemetry was critical.

### Lesson 3

Cross-domain correlation increased confidence.

### Lesson 4

Behavior-based hunting found activity that IOC-based detection missed.

### Lesson 5

Telemetry quality enabled investigation.

### Lesson 6

Detection gaps should be converted into engineering tasks.

---

# Phase 22 — Control Improvements

Potential improvements:

```text
MFA Hardening
Conditional Access
Device Trust
Endpoint Detection
Identity Risk Detection
Cloud Monitoring
Network Visibility
Detection Correlation
User Awareness
```

---

# Phase 23 — Metrics

The team records:

```text
Initial Detection:
Threat Hunt

Time to Identify:
Example metric

Time to Scope:
Example metric

Affected Users:
1

Affected Endpoints:
1 primary

Potentially Accessed Servers:
2

Potential Data:
Finance-related

Detection Gaps:
4
```

Real organizations should populate these values from actual incident data.

---

# Full Investigation Architecture

```text
                    THREAT INTELLIGENCE
                            │
                            ▼
                      HUNT HYPOTHESIS
                            │
                            ▼
                     TELEMETRY CHECK
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
       Identity          Endpoint           Cloud
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                        CORRELATION
                            │
                            ▼
                      ENTITY PIVOTS
                            │
                            ▼
                    TIMELINE REBUILD
                            │
                            ▼
                     THREAT ASSESSMENT
                            │
                  ┌─────────┴─────────┐
                  ▼                   ▼
                Benign             Malicious
                                      │
                                      ▼
                                  INCIDENT
                                      │
                     ┌────────────────┼────────────────┐
                     ▼                ▼                ▼
                 Response         Detection         Intel
                     │                │                │
                     └────────────────┼────────────────┘
                                      ▼
                               LESSONS LEARNED
```

---

# End-to-End Hunt Record

```text
Hunt ID:
TH-CASE-001

Title:
Compromised Valid Account Investigation

Objective:
Identify suspicious identity activity followed by
endpoint and cloud behavior.

Primary Hypothesis:
A valid account may have been compromised.

Data Sources:
Identity
EDR
DNS
Proxy
Cloud Audit
Email
Firewall

Initial Signal:
Unusual authentication

Key Findings:
New device
Unusual source
PowerShell
DNS activity
Lateral movement
Cloud activity
Data access

Assessment:
High confidence suspicious activity

Escalation:
Incident response

Detection Gap:
Cross-domain identity + endpoint + cloud correlation

Detection Created:
Suspicious Valid Account Activity

Outcome:
Detection and hunting workflow improved
```

---

# Practical Lab — Reproduce the Case Study

This scenario can be reproduced safely in an isolated lab.

## Objective

Build a complete investigation pipeline.

---

## Lab Architecture

```text
                    Analyst
                       │
                       ▼
                      SIEM
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
    Windows           Linux         Cloud
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                    Telemetry
                       │
                       ▼
                   Hunt Queries
                       │
                       ▼
                    Findings
```

---

# Lab Requirements

Potential components:

```text
Windows VM
Linux VM
SIEM
EDR or endpoint telemetry
DNS logging
Authentication logs
Cloud sandbox
```

Use only systems and accounts you are authorized to test.

---

# Lab Phase 1 — Generate Telemetry

Generate benign, authorized activity such as:

```text
Authentication
Process Creation
DNS Queries
Cloud API Activity
File Access
```

---

# Lab Phase 2 — Establish Baseline

Record:

```text
Normal Users
Normal Hosts
Normal Processes
Normal Domains
Normal Cloud Activity
```

---

# Lab Phase 3 — Execute Authorized Simulation

Use controlled security-testing techniques.

Examples:

```text
Authentication Testing
PowerShell Simulation
DNS Activity
Remote Access Simulation
Cloud API Testing
```

Do not use uncontrolled malware or unauthorized infrastructure.

---

# Lab Phase 4 — Hunt

Run:

```text
Identity Hunt
Endpoint Hunt
DNS Hunt
Cloud Hunt
Lateral Movement Hunt
```

---

# Lab Phase 5 — Correlate

Connect:

```text
User
+
Host
+
Process
+
IP
+
Domain
+
Cloud Session
```

---

# Lab Phase 6 — Build Timeline

Create:

```text
Timestamp
Event
Entity
Source
Interpretation
```

---

# Lab Phase 7 — Detection

Create a detection based on the discovered behavior.

---

# Lab Phase 8 — Validate

Run:

```text
Positive Test
Negative Test
False Positive Test
Regression Test
```

---

# Lab Phase 9 — Document

Produce:

```text
Investigation Report
Detection
Playbook
Lessons Learned
```

---

# Case Study Decision Tree

```text
Unusual Authentication
        │
        ▼
Is source expected?
   │            │
  Yes           No
   │            │
   ▼            ▼
Review      Investigate
normality       │
                ▼
         Is device trusted?
            │         │
           Yes        No
            │         │
            ▼         ▼
       Continue     Escalate
                      │
                      ▼
              Check endpoint
                      │
                      ▼
            Suspicious behavior?
                 │         │
                No        Yes
                 │         │
                 ▼         ▼
               Close    Correlate
                           │
                           ▼
                       Cloud / Network
                           │
                           ▼
                       Build Timeline
```

---

# Analyst Decision Framework

When an anomaly appears, ask:

```text
1. Is it unusual?
2. Is it explainable?
3. Is it risky?
4. Is there corroborating evidence?
5. Is there an affected asset?
6. Is there evidence of attacker intent?
7. Is the activity part of a larger sequence?
```

---

# Evidence Confidence Model

A useful conceptual model:

```text
Single Weak Signal
       ↓
Low Confidence

Multiple Correlated Signals
       ↓
Medium Confidence

Strong Multi-Source Evidence
       ↓
High Confidence

Validated Incident Evidence
       ↓
Confirmed
```

---

# Avoiding Confirmation Bias

Threat hunters must avoid forcing evidence into an expected narrative.

For every hypothesis, ask:

```text
What evidence supports it?

What evidence contradicts it?

What benign explanation exists?

What telemetry is missing?

What additional evidence would prove or disprove it?
```

---

# Alternative Explanation Analysis

For example:

```text
New Login
```

Possible explanations:

```text
Compromise
Travel
VPN
New Device
Administrative Work
Automated Application
```

The hunter should test alternatives.

---

# Competing Hypotheses

Example:

```text
H1: Account compromise

H2: Legitimate user travel

H3: VPN routing anomaly

H4: Service automation

H5: Device registration problem
```

Evidence should determine which explanation is best supported.

---

# Hypothesis Scoring

Conceptually:

```text
Hypothesis
   │
   ├── Supporting Evidence
   ├── Contradicting Evidence
   ├── Missing Evidence
   └── Alternative Explanation
```

Do not treat a numerical score as proof.

---

# Threat Hunting and Incident Response

Threat hunting may discover an incident before automated detection does.

```text
Automated Detection
        │
        └── No Alert

Threat Hunt
        │
        ▼
Suspicious Behavior
        │
        ▼
Investigation
        │
        ▼
Incident
```

This is one of the most valuable outcomes of proactive hunting.

---

# Threat Hunting and Detection Engineering

The case study demonstrates:

```text
Hunt
 ↓
Finding
 ↓
Behavior
 ↓
Detection
 ↓
Test
 ↓
Deploy
 ↓
Monitor
```

---

# Threat Hunting and Threat Intelligence

The relationship is bidirectional.

```text
Threat Intelligence
        ↓
Hunt
        ↓
New Findings
        ↓
Validated Intelligence
        ↓
Threat Intelligence
```

---

# Threat Hunting and SOC Operations

The SOC provides:

```text
Alert Patterns
False Positives
Incident Trends
User Context
Detection Feedback
```

Threat hunters convert these into deeper investigations.

---

# Threat Hunting and Security Architecture

Hunting can reveal:

```text
Telemetry Gaps
Identity Gaps
Endpoint Gaps
Cloud Gaps
Network Gaps
Detection Gaps
```

These become architecture improvement opportunities.

---

# Enterprise Threat Hunting Feedback Loop

```text
             ┌─────────────────────┐
             │ Threat Intelligence │
             └──────────┬──────────┘
                        ▼
                 Hunt Hypothesis
                        │
                        ▼
                     Hunting
                        │
                        ▼
                    Findings
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
       Detection     Incident      Intel
            │           │           │
            └───────────┼───────────┘
                        ▼
                  Lessons Learned
                        │
                        ▼
                 Security Controls
                        │
                        ▼
                 Improved Hunting
```

---

# What Makes This a Realistic Investigation?

Real investigations rarely look like:

```text
IOC
↓
Alert
↓
Attack
```

They more often look like:

```text
Weak Signal
   ↓
Anomaly
   ↓
Investigation
   ↓
Another Weak Signal
   ↓
Correlation
   ↓
Timeline
   ↓
Confidence Increase
   ↓
Incident
```

Threat hunting is therefore fundamentally an **evidence-correlation discipline**.

---

# Professional Threat Hunting Checklist

## Intelligence

- [ ] Threat intelligence reviewed
- [ ] Threat relevance assessed
- [ ] TTPs identified
- [ ] Indicators normalized

## Hypothesis

- [ ] Hypothesis written
- [ ] Alternative explanations considered
- [ ] Required evidence identified

## Telemetry

- [ ] Identity available
- [ ] Endpoint available
- [ ] Network available
- [ ] DNS available
- [ ] Cloud available
- [ ] Email available where relevant

## Investigation

- [ ] Initial query
- [ ] Entity pivot
- [ ] Correlation
- [ ] Baseline comparison
- [ ] Timeline

## Validation

- [ ] Supporting evidence
- [ ] Contradicting evidence
- [ ] False positives
- [ ] Confidence assessed

## Outcome

- [ ] Incident escalated if required
- [ ] Detection gap documented
- [ ] New detection created where appropriate
- [ ] Intelligence updated
- [ ] Lessons learned recorded

---

# Threat Hunting Report Template

```text
# Threat Hunting Report

## Hunt Metadata

Hunt ID:
Analyst:
Date:
Duration:

## Objective

## Threat Scenario

## Hypothesis

## Alternative Hypotheses

## ATT&CK Mapping

## Scope

## Data Sources

## Queries

## Findings

## Evidence

## Timeline

## Entity Relationships

## Threat Assessment

## Confidence

## Detection Gaps

## Telemetry Gaps

## Incident Escalation

## Detection Improvements

## Intelligence Improvements

## Lessons Learned

## Recommendations
```

---

# Executive Summary Template

A senior-level summary should answer:

```text
What happened?

How was it discovered?

What systems were affected?

What evidence supports the conclusion?

What is the current risk?

What actions were taken?

What improvements are required?
```

Avoid overwhelming executives with raw technical events.

---

# Technical Summary Template

```text
Initial Signal
      ↓
Authentication
      ↓
Endpoint
      ↓
Network
      ↓
Cloud
      ↓
Data Access
      ↓
Assessment
```

Include evidence and timestamps.

---

# Lessons for Security Engineers

This case demonstrates several important principles.

### Identity is a Security Boundary

Valid credentials can bypass many perimeter controls.

### Endpoint Context Matters

A login alone may be ambiguous.

### Network Context Matters

External communication can strengthen or weaken a hypothesis.

### Cloud Context Matters

Modern attacks often cross traditional security boundaries.

### Correlation Matters

Multiple weak signals can become a strong investigation.

### Baselines Matter

Normal behavior provides essential context.

### Detection Engineering Matters

Hunts should improve future automated detection.

---

# Interview Questions

## 1. Walk me through a complete threat hunt.

A strong answer should cover:

```text
Threat intelligence
→ hypothesis
→ telemetry
→ initial query
→ entity pivot
→ correlation
→ timeline
→ validation
→ assessment
→ detection improvement
```

---

## 2. What would make you escalate a hunt to incident response?

When multiple independent signals provide sufficient evidence that malicious activity may have occurred, particularly when critical assets, identities, persistence, lateral movement, or data access are involved.

---

## 3. How do you avoid false positives?

Use:

- Baselines
- Peer groups
- Context
- Correlation
- Historical behavior
- Asset criticality
- Known legitimate workflows

---

## 4. What if your hypothesis is wrong?

Document the contradictory evidence, test alternative explanations, revise the hypothesis, and continue the investigation based on the strongest available evidence.

---

## 5. How do you prove an account is compromised?

You generally cannot prove compromise from one anomaly alone. Build evidence across authentication, device, endpoint, network, identity, and post-authentication behavior.

---

## 6. Why is cross-domain correlation important?

Attackers operate across identity, endpoints, networks, applications, and cloud environments. Correlation allows analysts to reconstruct the broader attack chain.

---

## 7. What is the difference between suspicious and confirmed malicious activity?

Suspicious activity indicates that behavior is unusual or concerning. Confirmed malicious activity requires stronger evidence established through investigation or an appropriate incident-response process.

---

## 8. What should happen after a successful hunt?

Potential outcomes include:

```text
Detection
Incident
Threat Intelligence
Telemetry Improvement
Security Control Improvement
New Playbook
```

---

## 9. How would you measure threat-hunting effectiveness?

Possible metrics include:

```text
Threats Discovered
Detection Gaps Found
New Detections
Telemetry Gaps
Validated Intelligence
Time to Investigate
Detection Improvements
```

---

## 10. How would you explain this investigation to management?

Focus on:

```text
Impact
Risk
Affected Assets
Evidence
Actions Taken
Current Status
Recommended Improvements
```

Avoid unnecessary technical detail.

---

# Final Threat Hunting Section Takeaways

The complete Threat Hunting section can now be viewed as:

```text
01 Fundamentals
       ↓
02 MITRE ATT&CK
       ↓
03 Threat Intelligence
       ↓
04 Windows
       ↓
05 Linux
       ↓
06 EDR
       ↓
07 Network
       ↓
08 DNS
       ↓
09 Identity
       ↓
10 Cloud
       ↓
11 SIEM
       ↓
12 Query Engineering
       ↓
13 Detection Engineering
       ↓
14 Playbooks & Labs
       ↓
15 Real-World Case Study
```

This progression moves from foundational knowledge to practical enterprise execution.

---

# Threat Hunting Operating Model

```text
                    THREAT INTELLIGENCE
                            │
                            ▼
                    PRIORITY / RISK
                            │
                            ▼
                       HYPOTHESIS
                            │
                            ▼
                      DATA / TELEMETRY
                            │
                            ▼
                       HUNT QUERY
                            │
                            ▼
                     ENTITY ANALYSIS
                            │
                            ▼
                      CORRELATION
                            │
                            ▼
                       TIMELINE
                            │
                            ▼
                     THREAT ASSESSMENT
                            │
             ┌──────────────┼──────────────┐
             ▼              ▼              ▼
           BENIGN       SUSPICIOUS      MALICIOUS
             │              │              │
             ▼              ▼              ▼
           CLOSE        CONTINUE        INCIDENT
                            │              │
                            └──────┬───────┘
                                   ▼
                          DETECTION ENGINEERING
                                   │
                                   ▼
                             IMPROVED DEFENSE
                                   │
                                   ▼
                            FUTURE HUNTING
```

---

# Final Takeaways

1. **Threat hunting is an evidence-driven investigative process.**
2. **A good hunt starts with a clear and testable hypothesis.**
3. **Threat intelligence provides direction but does not replace investigation.**
4. **Identity, endpoint, network, DNS, and cloud telemetry should be correlated whenever relevant.**
5. **Single anomalies rarely establish compromise on their own.**
6. **Entity pivoting transforms isolated events into relationships.**
7. **Timeline reconstruction is fundamental to understanding attack progression.**
8. **Alternative explanations should be actively tested to reduce confirmation bias.**
9. **Confidence should reflect the quality and quantity of supporting evidence.**
10. **Negative findings are valuable and should be documented.**
11. **Threat hunting can identify attacks that automated detections miss.**
12. **Successful hunts should create new detections or improve existing ones.**
13. **Detection gaps and telemetry gaps are important security findings.**
14. **Incident-response escalation should be based on evidence and organizational procedures.**
15. **Threat intelligence should be updated with validated findings.**
16. **Playbooks turn individual analyst knowledge into repeatable organizational capability.**
17. **Purple-team exercises can validate whether hunting and detection actually work.**
18. **A mature threat-hunting program continuously feeds intelligence, detection engineering, SOC operations, and security architecture.**

The central principle of this entire section is:

> **Threat hunting is not simply searching for attackers. It is the disciplined process of forming hypotheses, analyzing telemetry, correlating evidence, challenging assumptions, validating threats, and continuously improving the organization's ability to detect and respond to them.**

---

# References

- MITRE ATT&CK  
  https://attack.mitre.org/

- MITRE Cyber Analytics Repository  
  https://car.mitre.org/

- MITRE D3FEND  
  https://d3fend.mitre.org/

- SigmaHQ  
  https://sigmahq.io/

- Atomic Red Team  
  https://atomicredteam.io/

- MITRE Caldera  
  https://caldera.mitre.org/

- NIST Cybersecurity Framework  
  https://www.nist.gov/cyberframework

- NIST SP 800-61 — Computer Security Incident Handling Guide  
  https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

- NIST SP 800-92 — Guide to Computer Security Log Management  
  https://csrc.nist.gov/publications/detail/sp/800-92/final

- CISA Cybersecurity Resources  
  https://www.cisa.gov/topics/cybersecurity

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

- CIS Critical Security Controls  
  https://www.cisecurity.org/controls

- CISA Known Exploited Vulnerabilities Catalog  
  https://www.cisa.gov/known-exploited-vulnerabilities-catalog
