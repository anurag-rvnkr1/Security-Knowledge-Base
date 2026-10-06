# Threat Hunting Playbooks and Labs

## Overview

Threat hunting becomes operationally valuable when analysts can repeatedly execute structured investigations against real security telemetry.

A threat-hunting playbook provides:

- A defined objective
- A threat hypothesis
- Required telemetry
- Query logic
- Investigation steps
- Evidence requirements
- Pivot points
- Validation criteria
- Escalation guidance
- Detection opportunities

This chapter converts the concepts covered throughout the Threat Hunting section into practical workflows.

The objective is not simply to find suspicious events.

The objective is to establish a repeatable process:

```text id="2s8s0g"
Threat Intelligence
        │
        ▼
Hunt Hypothesis
        │
        ▼
Telemetry
        │
        ▼
Query
        │
        ▼
Investigation
        │
        ▼
Evidence
        │
        ▼
Assessment
        │
        ├──────────────┐
        ▼              ▼
   True Positive    Benign
        │
        ▼
Detection / Response
```

---

# Why Hunting Playbooks Matter

Without structured procedures, threat hunting can become:

```text id="a2n7hz"
Random Searches
      ↓
Large Result Sets
      ↓
Inconsistent Analysis
      ↓
Missed Evidence
      ↓
Poor Documentation
```

A playbook creates consistency.

```text id="6m4t9u"
Hypothesis
    ↓
Required Data
    ↓
Query
    ↓
Pivot
    ↓
Validation
    ↓
Conclusion
```

---

# Playbook Design Principles

A good hunting playbook should be:

- Hypothesis driven
- Evidence based
- Repeatable
- Measurable
- Documented
- Adaptable
- Platform aware
- Safe
- Actionable

Avoid playbooks that simply provide a long list of commands.

The analyst should understand **why** each step exists.

---

# Standard Hunt Playbook Structure

```text id="qwmwqo"
1. Objective
2. Threat Scenario
3. Hypothesis
4. ATT&CK Mapping
5. Required Telemetry
6. Preconditions
7. Initial Query
8. Investigation
9. Pivots
10. Validation
11. Escalation
12. Detection Opportunity
13. Documentation
14. Lessons Learned
```

---

# Hunt Lifecycle

```text id="91u0y3"
             ┌───────────────────┐
             │ Threat Intelligence│
             └─────────┬─────────┘
                       │
                       ▼
                 Hunt Hypothesis
                       │
                       ▼
                 Data Collection
                       │
                       ▼
                  Initial Hunt
                       │
                       ▼
                    Pivot
                       │
                       ▼
                  Correlation
                       │
                       ▼
                  Validation
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          Benign              Suspicious
             │                   │
             ▼                   ▼
       Close / Record      Escalate / Detect
```

---

# Hunt Documentation Standard

Every hunt should produce a record.

```text id="8v0gkg"
Hunt ID:
Hunt Name:
Analyst:
Start Time:
End Time:

Hypothesis:

Threat Scenario:

MITRE ATT&CK:

Data Sources:

Queries:

Time Range:

Hosts Investigated:

Users Investigated:

Indicators:

Evidence:

Findings:

Conclusion:

Detection Candidate:

Response Required:

Lessons Learned:
```

---

# Playbook 01 — Password Spraying

## Objective

Identify authentication failures consistent with password spraying.

## Threat Scenario

An attacker attempts a small number of passwords against many accounts to avoid triggering individual account lockouts.

## ATT&CK

```text id="5w1k6r"
T1110 — Brute Force
T1110.003 — Password Spraying
```

---

## Hypothesis

> A source may be attempting authentication against multiple user accounts within a short period.

---

## Required Telemetry

```text id="n2x4hv"
Authentication Logs
Identity Provider
VPN
Windows Security
Cloud Identity
SSO
```

Required fields:

```text id="m4j3dx"
timestamp
user
source.ip
destination
authentication.result
authentication.method
```

---

## Initial Hunt

Conceptually:

```text id="9br4ko"
Authentication Failures
        │
        ▼
Group by Source IP
        │
        ▼
Count Unique Users
        │
        ▼
Count Attempts
        │
        ▼
Time Window
```

---

## Investigation

For suspicious sources investigate:

```text id="5r6e8h"
Source Reputation
Geography
ASN
VPN/Proxy
Target Users
Authentication Method
Successful Login
```

---

## Critical Pivot

Look for:

```text id="1m8xqv"
Failure
Failure
Failure
Success
```

A successful login following many failures can significantly increase investigation priority.

---

## Follow-Up

Investigate the account after successful authentication:

```text id="r4yq2e"
Process Activity
Cloud Actions
Mailbox Access
VPN Activity
Privilege Changes
Data Access
```

---

## Detection Opportunity

Create detection logic based on:

```text id="ypz3m5"
One Source
+
Many Users
+
Authentication Failures
+
Short Time Window
```

---

# Playbook 02 — Brute Force Against One Account

## Objective

Identify repeated authentication failures against one account.

## Hypothesis

> An attacker may repeatedly attempt credentials against a specific account.

---

## Query Logic

```text id="v0xg7j"
User
  │
  ▼
Authentication Failures
  │
  ▼
Count Attempts
  │
  ▼
Group by Source
```

---

## Investigate

```text id="yd8j9c"
Is the account privileged?

Is the source internal?

Is the source expected?

Did authentication eventually succeed?

Was MFA triggered?

Was a new device involved?
```

---

# Playbook 03 — Suspicious PowerShell

## Objective

Identify potentially malicious PowerShell execution.

## ATT&CK

```text id="9l8yqg"
T1059.001 — PowerShell
```

---

## Hypothesis

> PowerShell may be executing commands inconsistent with the user's normal activity.

---

## Required Telemetry

```text id="h0s2x8"
EDR
Sysmon
Windows Process Creation
PowerShell Logging
Network Telemetry
```

Fields:

```text id="x0u8j4"
process.name
process.command_line
process.parent.name
user.name
host.name
destination.ip
```

---

## Initial Search

Start with:

```text id="wy1z7g"
powershell.exe
```

Then inspect:

```text id="j5w7n4"
Command Line
Parent Process
User
Host
Network
Frequency
```

---

## Suspicious Context

Examples:

```text id="0n5m9w"
Office → PowerShell
Browser → PowerShell
Web Server → PowerShell
Unknown Executable → PowerShell
```

Context matters.

---

## Command-Line Indicators

Look for behaviors such as:

```text id="d7x1u8"
Encoded execution
Download operations
Remote commands
Script execution
Credential-related activity
Unusual URLs
Temporary directory execution
```

Avoid relying on one string alone.

---

## Pivot

From PowerShell:

```text id="j2z9eq"
Host
 │
 ├── User
 ├── Parent Process
 ├── Child Processes
 ├── Network Connections
 ├── DNS
 └── File Activity
```

---

# Playbook 04 — Suspicious Parent-Child Process Relationship

## Objective

Find unusual process trees.

## Hypothesis

> A legitimate process may have spawned an unexpected child process as part of malicious execution.

---

## Example Relationships

```text id="3t0qg2"
winword.exe
    └── powershell.exe

excel.exe
    └── cmd.exe

w3wp.exe
    └── cmd.exe

nginx
    └── sh
```

These are not automatically malicious.

They require context.

---

## Investigation

Capture:

```text id="f2s8y7"
Parent
Child
User
Command Line
Integrity Level
Signer
Hash
Network Activity
```

---

# Playbook 05 — Credential Access Hunting

## Objective

Identify suspicious activity associated with credential access.

## Hypothesis

> A process may be interacting with credential stores or authentication material unexpectedly.

---

## Telemetry

```text id="0c3s4p"
EDR
Windows Events
Linux Audit
Identity
File Access
Process Telemetry
```

---

## Windows Areas

Potential investigation areas:

```text id="9g1f7a"
/LSASS activity
Credential stores
Registry
Security events
Token activity
```

Do not interpret legitimate security software activity as malicious without context.

---

## Linux Areas

Investigate:

```text id="n7d8r4"
/etc/shadow
SSH keys
Credential files
Shell history
Environment variables
Process memory
```

Use appropriate authorization and evidence-handling controls.

---

# Playbook 06 — Privilege Escalation

## Objective

Identify unexpected privilege changes.

## Hypothesis

> An account or process may have gained privileges outside normal administrative workflows.

---

## Windows

Investigate:

```text id="w2k9p4"
Privileged Group Changes
New Services
Scheduled Tasks
Token Activity
UAC Events
Account Changes
```

---

## Linux

Investigate:

```text id="6p8x3s"
sudo
SUID
File Permissions
Cron
systemd
User Group Changes
```

---

## Cloud

Investigate:

```text id="7x2g0c"
IAM Policy Changes
Role Assignments
Trust Policy Changes
Service Accounts
New Credentials
```

---

# Playbook 07 — Persistence Hunting

## Objective

Identify mechanisms that survive reboot, logout, or process termination.

---

## Windows Persistence

Investigate:

```text id="h1v6l4"
Registry Run Keys
Scheduled Tasks
Services
Startup Folders
WMI
Logon Scripts
New Accounts
```

---

## Linux Persistence

Investigate:

```text id="4p7m8s"
cron
systemd
SSH Keys
Shell Profiles
Startup Scripts
Init Mechanisms
```

---

## Cloud Persistence

Investigate:

```text id="0x5j9k"
IAM Users
Access Keys
Roles
Trust Policies
Service Principals
OAuth Applications
Automation Accounts
```

---

# Playbook 08 — DNS Threat Hunting

## Objective

Identify suspicious DNS activity.

## Hypothesis

> A compromised endpoint may use DNS for command-and-control, tunneling, reconnaissance, or beaconing.

---

## Initial Query

Aggregate:

```text id="5x8v1p"
Host
Domain
Query Count
Unique Domains
NXDOMAIN
Query Type
```

---

## Investigate

Look for:

```text id="v3m8d1"
Rare Domains
Long Labels
High Entropy
TXT Activity
Regular Intervals
High Query Volume
```

---

## Pivot

```text id="x8q3l0"
Domain
  ↓
Host
  ↓
Process
  ↓
User
  ↓
Network
```

---

# Playbook 09 — DNS Beaconing

## Hypothesis

> A compromised endpoint may repeatedly contact a domain at regular intervals.

---

## Method

Collect timestamps:

```text id="8h0m4r"
10:00:01
10:05:02
10:10:00
10:15:03
10:20:01
```

Calculate approximate intervals.

---

## Investigate

```text id="8c4j1s"
Average Interval
Interval Variance
Jitter
Domain Age
Host Process
Network Destination
```

Regularity is a signal, not proof.

---

# Playbook 10 — Lateral Movement

## Objective

Identify suspicious movement between systems.

## Hypothesis

> A compromised identity or endpoint may be accessing systems outside its normal relationship graph.

---

## Required Telemetry

```text id="j5q8d1"
Authentication
SMB
RDP
WinRM
SSH
Remote Management
Network Flow
EDR
```

---

## Query Model

```text id="y4c8z2"
Source Host
     │
     ▼
User
     │
     ▼
Destination Host
     │
     ▼
Authentication Method
```

---

## Baseline

Determine:

```text id="3f0m7n"
Normal Source → Destination Relationships
```

Then identify new relationships.

---

# Playbook 11 — RDP Hunting

## Objective

Identify suspicious Remote Desktop activity.

## Hypothesis

> An account may be using RDP from an unusual source or at an unusual time.

---

## Investigate

```text id="g9s2y1"
Source Host
Target Host
User
Logon Type
Timestamp
Geography
Device
```

---

## Correlate

```text id="1w8k3p"
RDP Login
   +
New Device
   +
Privileged Account
   +
Unusual Time
```

---

# Playbook 12 — SSH Threat Hunting

## Objective

Identify suspicious SSH activity.

## Linux Telemetry

```text id="z5m7k2"
/var/log/auth.log
/var/log/secure
journald
auditd
EDR
```

---

## Investigate

```text id="s1k8c6"
Failed Logins
Successful Logins
Root Access
New Keys
New Users
Source IPs
```

---

## Pivot

```text id="m8d2v9"
SSH Login
   ↓
User
   ↓
Process
   ↓
Command
   ↓
Network
```

---

# Playbook 13 — Web Shell Hunting

## Objective

Identify command execution through a compromised web application.

## Hypothesis

> A web server process may be spawning a shell or interpreter unexpectedly.

---

## Suspicious Process Chains

```text id="1p5v8k"
nginx
 └── sh

apache
 └── bash

w3wp.exe
 └── cmd.exe

java
 └── powershell.exe
```

These require validation.

---

## Required Evidence

```text id="5h0y9d"
Web Request
Source IP
URL
Web Process
Child Process
Command Line
File Modification
Network Connection
```

---

## Timeline

```text id="v5f7x2"
HTTP Request
     ↓
Web Process
     ↓
Shell
     ↓
Command
     ↓
Outbound Connection
```

---

# Playbook 14 — Account Takeover

## Objective

Identify potentially compromised user accounts.

## Hypothesis

> A valid account may have been taken over.

---

## Signals

```text id="g1w8q4"
New Location
New Device
New ASN
Unusual User-Agent
Impossible Travel
MFA Anomaly
Unusual Login Time
Sensitive Action
```

---

## Correlation

```text id="m4r7c9"
Authentication Anomaly
       +
Device Anomaly
       +
Behavior Anomaly
```

---

## Investigation

Review:

```text id="k9p2x1"
Recent Password Changes
MFA Events
OAuth Grants
Mailbox Activity
Cloud Actions
File Access
Privilege Changes
```

---

# Playbook 15 — MFA Fatigue / Authentication Abuse

## Objective

Identify repeated authentication prompts or suspicious MFA activity.

## Hypothesis

> An attacker may be attempting to cause a user to approve an authentication request.

---

## Signals

```text id="5b3n8j"
Many MFA Requests
Repeated Denials
One Approval
New Device
Unusual Location
```

---

## Investigation

```text id="j8k2v4"
User
Device
Source IP
MFA Method
Request Count
Approval Time
Post-Approval Activity
```

---

# Playbook 16 — Cloud IAM Abuse

## Objective

Identify suspicious cloud identity changes.

## Hypothesis

> An attacker may modify cloud permissions to maintain or expand access.

---

## Investigate

```text id="s6h1q8"
Role Assignment
Policy Change
Trust Policy
Access Key
Service Principal
Credential
```

---

## Correlate

```text id="9w2x6r"
Login
   ↓
IAM Change
   ↓
Sensitive API
   ↓
Data Access
```

---

# Playbook 17 — Cloud Storage Exposure

## Objective

Identify suspicious access to sensitive storage.

## Investigate

```text id="4d7m1y"
Storage Object Access
Source IP
Identity
User-Agent
Volume
Geography
```

---

## High-Risk Pattern

```text id="0r5x9k"
Rare Identity
    +
Large Download
    +
Sensitive Bucket
    +
New Source
```

---

# Playbook 18 — Suspicious API Activity

## Objective

Identify API abuse.

## Hypothesis

> An identity may be using APIs in a way inconsistent with normal behavior.

---

## Signals

```text id="c2f8m7"
High Request Rate
Rare API
New Endpoint
New User-Agent
Unusual Authentication
Error Spike
```

---

# Playbook 19 — Data Exfiltration

## Objective

Identify suspicious outbound transfer.

## Hypothesis

> A compromised system may be transferring sensitive information externally.

---

## Required Telemetry

```text id="m7y4q1"
Proxy
Firewall
DNS
DLP
Cloud
Endpoint
Network Flow
```

---

## Investigate

```text id="v8c2k5"
Destination
Volume
Protocol
User
Host
Time
Application
Data Classification
```

---

## Important Principle

Large transfers are not automatically malicious.

Examples of legitimate large transfers:

```text id="r7p3n9"
Backup
Cloud Sync
Software Distribution
Video Processing
Database Replication
```

Context is essential.

---

# Playbook 20 — Data Staging

## Objective

Identify suspicious local collection before exfiltration.

## Hypothesis

> An attacker may aggregate sensitive data before transferring it.

---

## Investigate

```text id="9h4x2s"
Archive Creation
Temporary Directories
Large File Creation
Sensitive File Access
Compression Tools
Unusual User Activity
```

---

## Process Correlation

```text id="q6m8w1"
File Access
   ↓
Archive
   ↓
Compression
   ↓
Outbound Connection
```

---

# Playbook 21 — Malware Execution

## Objective

Identify potentially malicious file execution.

## Signals

```text id="7c3n9x"
Unknown Hash
Unsigned Binary
Unusual Path
Rare Process
Suspicious Parent
Network Connection
Persistence
```

---

## Investigate

```text id="m8k1s5"
File Hash
Signer
First Seen
Prevalence
Parent
Child Processes
Network
Persistence
```

---

# Playbook 22 — Living-off-the-Land

## Objective

Identify legitimate system tools being used suspiciously.

Potential tools include:

```text id="r3w9h6"
PowerShell
cmd
rundll32
regsvr32
mshta
wscript
cscript
certutil
bitsadmin
```

---

## Detection Strategy

Do not simply alert on execution.

Correlate:

```text id="j7x4m2"
Tool
+
Parent
+
Command Line
+
User
+
Destination
+
Frequency
```

---

# Playbook 23 — Scheduled Task Persistence

## Windows

Investigate:

```text id="5n8q2v"
Task Creation
Task Modification
Task Execution
Task Author
Task Action
```

---

## Suspicious Characteristics

```text id="k1s7m4"
Temporary Path
Script Interpreter
Unusual User
Unexpected Trigger
Remote Creation
```

---

# Playbook 24 — Linux Cron Persistence

Investigate:

```text id="c8v2p6"
User Crontab
System Crontab
Cron Directories
Cron Execution
```

Potential indicators:

```text id="m3x9r1"
Unexpected Script
Temporary Directory
Encoded Command
Network Activity
```

---

# Playbook 25 — Service Persistence

## Windows

Investigate:

```text id="w6k1q4"
New Service
Service Binary
Service Account
Start Type
Creation Time
```

## Linux

Investigate:

```text id="p9s3y8"
systemd Units
Service Files
ExecStart
User
Environment
```

---

# Playbook 26 — Identity Privilege Abuse

## Objective

Identify unusual administrative behavior.

Investigate:

```text id="f2m8x5"
Privileged Login
Group Change
Role Assignment
Credential Creation
Sensitive Action
```

---

# Playbook 27 — Kerberos Threat Hunting

## Objective

Identify suspicious Kerberos activity.

Investigate:

```text id="v3j7q1"
TGT Requests
Service Tickets
Pre-authentication Failures
Service Account Activity
Unusual Ticket Patterns
```

Potential techniques:

```text id="k8m4s2"
Kerberoasting
AS-REP Roasting
Pass-the-Ticket
```

Interpret events in organizational context.

---

# Playbook 28 — OAuth Abuse

## Objective

Identify suspicious OAuth application activity.

Investigate:

```text id="x5r8n3"
New Application
Consent Grant
High Privileges
Rare Application
User Grant
Service Principal
```

---

# Playbook 29 — Container Threat Hunting

## Objective

Identify suspicious activity within container environments.

Investigate:

```text id="6y2m9p"
Container Creation
Image Source
Exec
Privilege
Network
Mounts
Secrets
```

---

## Suspicious Pattern

```text id="z7c1w4"
Unexpected Container
       +
Privileged Mode
       +
Host Mount
       +
Interactive Shell
```

---

# Playbook 30 — Kubernetes Threat Hunting

## Objective

Identify suspicious Kubernetes activity.

Investigate:

```text id="q8v4m2"
API Requests
Exec
Secrets
RoleBindings
Service Accounts
Pods
Namespaces
Network Policies
```

---

# Kubernetes Attack Path

```text id="u1r6k9"
Compromised Credential
       ↓
Kubernetes API
       ↓
RBAC Abuse
       ↓
Pod Exec
       ↓
Secret Access
       ↓
Container / Host Impact
```

---

# Playbook 31 — CI/CD Threat Hunting

## Objective

Identify abuse of software delivery pipelines.

Investigate:

```text id="s4k8n1"
Pipeline Changes
Secrets
Tokens
Build Agents
Repository Permissions
Artifacts
Deployments
```

---

# Suspicious CI/CD Pattern

```text id="f9q3x7"
Compromised Developer
       ↓
Pipeline Modification
       ↓
Secret Access
       ↓
Build
       ↓
Malicious Artifact
       ↓
Deployment
```

---

# Playbook 32 — Security Control Tampering

## Objective

Identify attempts to disable or bypass security controls.

Investigate:

```text id="m5w2j8"
EDR Service Changes
Logging Changes
Audit Configuration
Firewall Changes
SIEM Agent Status
CloudTrail Changes
```

---

## High-Risk Pattern

```text id="4x7p2n"
Privileged Login
       ↓
Security Control Modification
       ↓
Suspicious Activity
```

This sequence deserves immediate investigation.

---

# Playbook 33 — Log Tampering

## Objective

Identify attempts to remove evidence.

Investigate:

```text id="q2k7v8"
Log Clearing
Audit Configuration Changes
Logging Service Stop
Retention Changes
Cloud Logging Changes
```

---

# Playbook 34 — Newly Created Account

## Objective

Identify suspicious account creation.

Investigate:

```text id="9v4m1x"
Account Creation
Creator
Privileges
Group Membership
Login Activity
Source
```

---

# High-Risk Pattern

```text id="j8s3p6"
Privileged User
      ↓
Creates Account
      ↓
Adds Privileges
      ↓
New Account Logs In
```

---

# Playbook 35 — Rare Process Hunting

## Objective

Identify processes with low environmental prevalence.

---

## Method

Calculate:

```text id="g1x6q4"
Process Frequency
Host Frequency
User Frequency
First Seen
Last Seen
```

---

## Example

```text id="v3k8m2"
powershell.exe → common
chrome.exe     → common
unknown.exe    → rare
```

Rare does not mean malicious.

Investigate context.

---

# Playbook 36 — Rare Domain Hunting

Investigate:

```text id="c7n2w9"
First Seen
Unique Hosts
Query Count
Domain Age
TLD
Entropy
DNS Record
Threat Intelligence
```

---

# Playbook 37 — Newly Registered Domain Hunting

Potential signals:

```text id="m1s8x5"
New Registration
Rare Internal Host
High Query Frequency
Suspicious Content
Recent Infrastructure
```

New domains are not inherently malicious.

---

# Playbook 38 — Threat Intelligence Retro-Hunt

## Objective

Search historical telemetry for newly identified indicators.

---

## Workflow

```text id="r6q3y8"
New IOC
   ↓
Normalize
   ↓
Search Historical Data
   ↓
Find Matches
   ↓
Identify Hosts
   ↓
Identify Users
   ↓
Investigate Timeline
```

---

# Playbook 39 — IOC Pivot

Given an indicator:

```text id="k4w8m1"
IP
Domain
Hash
URL
```

Pivot through:

```text id="j7p3x9"
Endpoint
DNS
Proxy
Firewall
Identity
Cloud
Email
```

---

# Playbook 40 — Incident Timeline Reconstruction

## Objective

Build a chronological attack narrative.

---

## Timeline

```text id="x9m2c6"
08:42 Login Failure
08:43 Successful Login
08:45 PowerShell
08:47 DNS Query
08:49 Credential Access
08:53 Lateral Movement
08:58 Data Staging
09:02 External Connection
```

---

# Timeline Sources

Combine:

```text id="h5q8s1"
Authentication
Endpoint
Network
DNS
Cloud
Application
Email
```

---

# Timeline Accuracy

Always consider:

```text id="3n7x2v"
Event Time
Ingestion Time
Timezone
Clock Drift
Log Delay
```

Do not assume timestamps are perfectly synchronized.

---

# Playbook 41 — Entity Pivoting

Start with:

```text id="r2v8m4"
User
```

Pivot:

```text id="9f1x7q"
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
Cloud Sessions
```

---

# Playbook 42 — Host-Centric Investigation

Start with:

```text id="7c4m9p"
Host
```

Pivot:

```text id="n6x2k8"
Host
 ├── Users
 ├── Processes
 ├── Files
 ├── Network
 ├── DNS
 ├── Persistence
 └── Authentication
```

---

# Playbook 43 — User-Centric Investigation

```text id="p3m7v1"
User
 ├── Logins
 ├── Devices
 ├── Locations
 ├── Applications
 ├── Privileges
 ├── Cloud Activity
 └── Data Access
```

---

# Playbook 44 — Network-Centric Investigation

```text id="x8k3q5"
Source
   ↓
Destination
   ↓
Protocol
   ↓
Domain
   ↓
Process
   ↓
User
```

---

# Playbook 45 — Cloud-Centric Investigation

```text id="m7q2c9"
Identity
   ↓
Session
   ↓
API Calls
   ↓
Resources
   ↓
Data Access
   ↓
Network
```

---

# Playbook 46 — Multi-Stage Attack Hunt

## Objective

Identify an attack spanning multiple ATT&CK tactics.

---

## Example

```text id="g4n8x2"
Initial Access
      ↓
Execution
      ↓
Credential Access
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Exfiltration
```

---

## Investigation Model

Do not search each stage independently.

Build an entity timeline.

```text id="v1c7m9"
User
Host
Time
Process
Network
Resource
```

---

# Playbook 47 — Detection Validation Hunt

## Objective

Validate an existing detection.

Process:

```text id="n5w2r8"
Detection
   ↓
Expected Behavior
   ↓
Authorized Simulation
   ↓
Telemetry
   ↓
Rule
   ↓
Alert
```

---

# Playbook 48 — Detection Gap Hunt

## Objective

Find threats that existing controls may not detect.

---

## Method

```text id="q8m3x1"
Threat
 ↓
ATT&CK Technique
 ↓
Telemetry
 ↓
Existing Detection?
 ↓
Test
```

If no detection exists:

```text id="w7c4n2"
Detection Gap
```

---

# Playbook 49 — Telemetry Health Hunt

## Objective

Identify missing or degraded security telemetry.

Investigate:

```text id="r4m9x6"
Expected Hosts
Reporting Hosts
Expected Logs
Received Logs
Agent Health
Ingestion Delay
```

---

# Telemetry Gap Example

```text id="h1x7q3"
Expected:
500 Endpoints

Reporting:
487

Gap:
13
```

Investigate immediately.

---

# Playbook 50 — Crown Jewel Hunt

## Objective

Focus hunting on the most critical systems.

Examples:

```text id="v8n2k5"
Domain Controllers
Identity Providers
Payment Systems
Production Databases
Source Code
Cloud Control Plane
Security Infrastructure
```

Increase detection and hunting depth around these assets.

---

# Practical Lab Environment

A useful threat-hunting lab can contain:

```text id="l7m3x9"
                ┌───────────────┐
                │    Analyst    │
                └───────┬───────┘
                        │
                        ▼
                 ┌─────────────┐
                 │     SIEM    │
                 └──────┬──────┘
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
      Windows         Linux         Network
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                  Detection Layer
```

Optional additions:

```text id="c9v4k1"
AD
EDR
DNS
Cloud Sandbox
Kubernetes
Threat Intelligence
```

---

# Lab 1 — Windows Authentication Hunt

## Objective

Detect suspicious authentication activity.

## Data

Use authorized lab-generated authentication events.

## Steps

1. Collect authentication events.
2. Filter failures.
3. Group by source.
4. Count unique users.
5. Identify successful logins.
6. Investigate post-login behavior.
7. Document findings.

---

# Lab 2 — PowerShell Hunt

## Objective

Investigate PowerShell execution.

### Collect

```text id="n8q3w6"
Process Name
Command Line
Parent
User
Host
Network
```

### Investigate

```text id="v4m7x2"
Rare Parent
Suspicious Command
Encoded Content
External Connection
```

---

# Lab 3 — Linux SSH Hunt

## Objective

Identify suspicious SSH activity.

### Collect

```text id="y2k8p4"
Source IP
User
Result
Timestamp
Privilege
```

### Investigate

```text id="x6m1r9"
Failed Attempts
Successful Login
Root Access
New Key
Post-Login Commands
```

---

# Lab 4 — DNS Hunt

## Objective

Investigate potentially suspicious DNS behavior.

Calculate:

```text id="p5x9m3"
Query Frequency
Label Length
Entropy
Unique Domains
NXDOMAIN Rate
```

Then pivot to endpoint telemetry.

---

# Lab 5 — Lateral Movement Hunt

## Objective

Identify unusual host-to-host relationships.

### Build Graph

```text id="k3v8q2"
Host A
 ├── Host B
 ├── Host C
 └── Host D
```

Compare with baseline.

---

# Lab 6 — Cloud IAM Hunt

## Objective

Investigate suspicious privilege changes.

Look for:

```text id="n7x4m1"
Role Assignment
Policy Change
New Credential
New Region
Sensitive API
```

Correlate events by principal.

---

# Lab 7 — Account Takeover

## Objective

Investigate suspicious identity activity.

Signals:

```text id="q9m3v6"
New Device
New Location
MFA Anomaly
Unusual Time
Sensitive Action
```

Build a user timeline.

---

# Lab 8 — Web Shell Investigation

## Objective

Investigate suspicious web server execution.

Build:

```text id="z5c8n2"
HTTP Request
      ↓
Web Process
      ↓
Child Process
      ↓
Network Connection
```

Determine whether the process chain is expected.

---

# Lab 9 — Detection Engineering

Create one production-quality detection from a completed hunt.

Required:

```text id="x2m7v9"
Hypothesis
Query
Detection
Test
Documentation
Runbook
```

---

# Lab 10 — Purple Team Detection Validation

Choose an authorized technique.

Document:

```text id="j4p8q1"
Technique
Simulation
Expected Telemetry
Actual Telemetry
Detection
Alert
Gap
Improvement
Retest
```

---

# Lab Investigation Methodology

Every practical lab should follow:

```text id="7m3x9q"
1. Establish Scope
2. Define Time Range
3. Validate Data
4. Execute Initial Query
5. Inspect Results
6. Identify Interesting Entity
7. Pivot
8. Correlate
9. Build Timeline
10. Assess
11. Document
```

---

# Investigation Scoping

Before searching, define:

```text id="x5q2m8"
Time
Users
Hosts
Networks
Cloud Accounts
Data Sources
```

Poor scope produces unnecessary noise.

---

# Evidence Collection

Record:

```text id="n8m4v1"
Timestamp
Source
Event
Entity
Query
Result
Interpretation
```

---

# Evidence Preservation

During real incidents:

- Preserve relevant logs.
- Avoid modifying evidence unnecessarily.
- Record timestamps.
- Record query versions.
- Document analyst actions.
- Follow organizational evidence-handling procedures.

---

# Hunt Result Classification

A hunt can conclude:

```text id="c4x7m2"
Benign
Suspicious
Likely Malicious
Confirmed Malicious
Inconclusive
Telemetry Gap
```

Avoid overstating certainty.

---

# Confidence Assessment

Example:

```text id="m8q3v6"
Low Confidence
One Weak Signal

Medium Confidence
Multiple Correlated Signals

High Confidence
Strong Evidence + Validation

Confirmed
Evidence / Incident Process Establishes Malicious Activity
```

---

# Hunt-to-Incident Handoff

When escalation is required:

```text id="p7x2k9"
Hunt Finding
     ↓
Incident Record
     ↓
Scope
     ↓
Containment
     ↓
Eradication
     ↓
Recovery
```

Provide the incident responder with:

```text id="v4m8n1"
Affected Hosts
Affected Users
Indicators
Timeline
Evidence
Queries
Initial Assessment
```

---

# Hunt-to-Detection Handoff

A successful hunt may produce a detection.

```text id="z2c6m9"
Hunt Finding
      ↓
Behavior Definition
      ↓
Detection Logic
      ↓
Test
      ↓
Deploy
```

---

# Hunt-to-Threat-Intelligence Handoff

A hunt may discover:

```text id="k8m1q4"
New Domain
New IP
New Hash
New Infrastructure
New TTP
```

Feed validated intelligence into the appropriate intelligence workflow.

---

# Hunt Metrics

Track:

```text id="q5x9n2"
Hunts Completed
True Positives
New Detections
Detection Gaps
Telemetry Gaps
Time to Investigate
Useful Findings
False Positives
```

---

# Hunt Effectiveness

A hunt is valuable if it produces one or more of:

```text id="j7m3v8"
Threat Discovery
Detection Improvement
Telemetry Improvement
Risk Reduction
Intelligence
Better Baseline
New Investigation Knowledge
```

---

# Hunt Backlog

Maintain a prioritized backlog.

```text
HUNT-001 Password Spray
HUNT-002 Suspicious PowerShell
HUNT-003 DNS Tunneling
HUNT-004 Cloud IAM Abuse
HUNT-005 Lateral Movement
```

Prioritize using:

```text id="w4q8m1"
Threat Relevance
Business Impact
Exposure
Telemetry Availability
Detection Gaps
Recent Intelligence
```

---

# Hunt Prioritization Matrix

| Priority | Threat | Business Impact | Telemetry | Detection Gap |
|---|---|---|---|---|
| Critical | Identity compromise | Critical | Strong | Yes |
| High | Lateral movement | High | Strong | Partial |
| Medium | DNS anomaly | Medium | Strong | Yes |
| Low | Rare process | Medium | Partial | Partial |

---

# Playbook Automation

Some repetitive steps can be automated.

```text id="v9m2x6"
IOC
 ↓
Enrichment
 ↓
SIEM Search
 ↓
Host Lookup
 ↓
User Lookup
 ↓
Threat Intelligence
```

Automation should support analysts rather than blindly automate conclusions.

---

# Safe Automation Principles

Automation should:

- Preserve evidence
- Log actions
- Use least privilege
- Avoid destructive operations
- Require approval for high-impact actions
- Maintain auditability

---

# Hunt Query Library

Organize reusable queries:

```text id="c7n4x2"
queries/
│
├── authentication/
├── endpoint/
├── windows/
├── linux/
├── dns/
├── network/
├── cloud/
├── identity/
└── containers/
```

---

# Playbook Repository

A professional hunting repository can use:

```text id="m8q3v7"
playbooks/
│
├── authentication/
├── endpoint/
├── identity/
├── network/
├── cloud/
├── dns/
└── incident/
```

Each playbook may contain:

```text id="x2k6p9"
README.md
queries/
tests/
references/
```

---

# Example Playbook Metadata

```yaml id="h7m3q1"
id: TH-PB-001
name: Password Spraying
category: identity
status: active
severity: high

hypothesis: >
  A source may be attempting authentication
  against multiple accounts.

telemetry:
  - authentication
  - identity
  - vpn

mitre:
  - T1110.003

owner: SOC
```

---

# Hunt Review

After completing a hunt, ask:

```text id="w8x2m5"
What did we learn?

What did we miss?

Was telemetry sufficient?

Was the query efficient?

Did we discover a detection gap?

Should a new detection be created?

Should an existing detection be tuned?

Did threat intelligence improve?

Should this hunt become recurring?
```

---

# Hunt Retrospective

Document:

```text id="p3m7x9"
Finding
Root Cause
Detection Gap
Telemetry Gap
Query Improvement
Process Improvement
Automation Opportunity
```

---

# Real-World Investigation Model

A mature hunt often follows this progression:

```text id="4c8m2x"
Hypothesis
    ↓
Broad Search
    ↓
Candidate Entity
    ↓
Entity Pivot
    ↓
Behavior Correlation
    ↓
Timeline
    ↓
Threat Validation
    ↓
Risk Assessment
    ↓
Detection / Response
```

---

# Practical Investigation Example

## Scenario

An analyst notices a rare PowerShell execution on a production server.

### Step 1 — Initial Observation

```text id="z7m2q4"
Host: PROD-WEB-01
Process: powershell.exe
User: service-account
```

### Step 2 — Parent Process

```text id="v4x8n1"
Parent: w3wp.exe
```

This is unusual and deserves investigation.

### Step 3 — Command Line

```text id="j9m3k6"
Review command line
```

### Step 4 — Network

```text id="p2q7x5"
Check outbound connections
```

### Step 5 — Web Logs

```text id="n6m1v8"
Search HTTP requests immediately preceding execution.
```

### Step 6 — Timeline

```text id="x3c8q2"
HTTP Request
    ↓
Web Process
    ↓
PowerShell
    ↓
Network Connection
```

### Step 7 — Assessment

The process chain may indicate possible web application compromise.

Escalate according to organizational incident procedures if supporting evidence exists.

---

# Hunt Playbook Quality Checklist

## Preparation

- [ ] Objective defined
- [ ] Hypothesis defined
- [ ] Scope defined
- [ ] ATT&CK mapping considered

## Telemetry

- [ ] Data sources identified
- [ ] Fields validated
- [ ] Coverage checked
- [ ] Time synchronization considered

## Investigation

- [ ] Initial query executed
- [ ] Results reviewed
- [ ] Entity pivot performed
- [ ] Correlation performed
- [ ] Timeline created

## Assessment

- [ ] Evidence documented
- [ ] Confidence assigned
- [ ] False positives considered
- [ ] Threat intelligence checked

## Outcome

- [ ] Detection candidate identified
- [ ] Detection gap recorded
- [ ] Telemetry gap recorded
- [ ] Escalation completed if required
- [ ] Lessons learned documented

---

# Enterprise Threat Hunting Architecture

```text id="q8v3m1"
                    THREAT INTELLIGENCE
                            │
                            ▼
                       HUNT BACKLOG
                            │
                            ▼
                       HYPOTHESIS
                            │
                            ▼
                    HUNT PLAYBOOK
                            │
                            ▼
                     QUERY LIBRARY
                            │
                            ▼
                 ┌──────────┼──────────┐
                 ▼          ▼          ▼
              SIEM        EDR       Cloud
                 │          │          │
                 └──────────┼──────────┘
                            ▼
                         FINDINGS
                            │
              ┌─────────────┼─────────────┐
              ▼             ▼             ▼
          Detection      Incident       Intel
              │             │             │
              └─────────────┼─────────────┘
                            ▼
                       FEEDBACK LOOP
```

---

# Professional Threat Hunting Workflow

```text id="j5x8q2"
01. Understand Threat
02. Define Hypothesis
03. Identify Evidence
04. Validate Telemetry
05. Execute Hunt
06. Analyze Results
07. Pivot
08. Correlate
09. Reconstruct Timeline
10. Assess Confidence
11. Escalate if Required
12. Create Detection
13. Record Intelligence
14. Document Lessons
15. Improve Playbook
```

---

# Common Hunting Mistakes

## 1. Searching Without a Hypothesis

Large result sets rarely produce efficient investigations.

---

## 2. Ignoring Baselines

Unusual does not automatically mean malicious.

---

## 3. Trusting One Signal

Strong investigations combine multiple evidence sources.

---

## 4. Ignoring Identity

Users and service accounts often provide essential context.

---

## 5. Ignoring Time

Attack chains are temporal.

---

## 6. Ignoring Telemetry Gaps

Missing evidence can itself be meaningful.

---

## 7. Treating Every IOC as Proof

Indicators require contextual validation.

---

## 8. Failing to Document

Undocumented investigations cannot be reliably reproduced.

---

## 9. Not Feeding Results Back

Hunts should improve detections and intelligence.

---

# Threat Hunting Maturity

## Level 1 — Reactive

Hunting happens only after alerts or incidents.

## Level 2 — Structured

Repeatable playbooks exist.

## Level 3 — Threat-Informed

Threat intelligence drives hunt priorities.

## Level 4 — Detection-Integrated

Hunts continuously produce detection improvements.

## Level 5 — Continuous Validation

Purple teaming, telemetry validation, and automated testing continuously measure detection effectiveness.

---

# Interview Questions

## Fundamentals

### 1. What is a threat-hunting playbook?

A documented, repeatable workflow that guides analysts through a specific security investigation from hypothesis through evidence collection, validation, and outcome.

### 2. Why are playbooks useful?

They improve consistency, repeatability, analyst efficiency, documentation, and knowledge transfer.

### 3. What should a hunting playbook contain?

At minimum:

- Objective
- Hypothesis
- Telemetry
- Queries
- Investigation steps
- Pivots
- Validation
- Escalation
- Detection opportunities

---

## Investigation

### 4. How would you investigate password spraying?

Look for authentication failures from one source against many unique accounts within a defined time window, then investigate successful logins and post-authentication behavior.

### 5. How would you investigate suspicious PowerShell?

Review the process tree, command line, user, host, execution frequency, network connections, parent process, and historical behavior.

### 6. How would you investigate lateral movement?

Correlate source host, destination host, user, authentication method, time, and historical source-to-destination relationships.

### 7. Why is a timeline important?

It allows analysts to understand event order and reconstruct the attack chain.

---

## Detection

### 8. When should a hunt become a detection?

When the behavior is sufficiently understood, repeatable, supported by reliable telemetry, and valuable enough to monitor continuously.

### 9. What is detection validation?

Testing whether the telemetry, query, rule, alert, and SOC workflow actually identify the intended behavior.

### 10. What is a detection gap?

A situation where relevant threat activity can occur and telemetry exists, but no reliable detection identifies it.

---

## Advanced

### 11. How do you prioritize hunts?

Consider threat intelligence, business impact, asset criticality, exposure, recent incidents, telemetry availability, and existing detection gaps.

### 12. Why should threat hunters perform entity pivots?

Because a single event rarely contains enough context. Pivoting connects users, hosts, processes, IPs, domains, and cloud activity.

### 13. What is telemetry-gap hunting?

Searching for systems or events that should be reporting security telemetry but are not.

### 14. How does threat hunting improve detection engineering?

Hunting identifies real environmental behavior and attack patterns that can be converted into tested, production detections.

### 15. What is purple-team validation?

Collaborative validation where authorized adversary simulations are used to test telemetry, detections, investigations, and response processes.

---

# Final Takeaways

1. **A threat-hunting playbook converts analytical knowledge into repeatable operational procedures.**
2. **Every hunt should begin with a clear hypothesis.**
3. **Telemetry validation should happen before complex investigation.**
4. **Entity pivots connect isolated events into behavioral evidence.**
5. **Timelines are essential for understanding attack progression.**
6. **Baselines distinguish unusual behavior from genuinely suspicious behavior.**
7. **Multiple weak signals can become a strong investigative case when correlated.**
8. **Hunt findings should feed detection engineering.**
9. **Hunts should identify telemetry and detection gaps.**
10. **Documentation makes hunts reproducible and auditable.**
11. **Playbooks should be regularly reviewed and improved.**
12. **Authorized simulations provide practical validation of hunting and detection capabilities.**
13. **Automation should accelerate evidence collection without replacing analyst judgment.**
14. **Hunting maturity comes from integrating intelligence, telemetry, detection, investigation, and response.**
15. **The ultimate objective is continuous reduction of organizational risk.**

The core principle is:

> **A mature threat hunt does not end when the analyst finds an interesting event. It ends when the organization understands the behavior, validates the risk, improves its defenses, and captures the knowledge for future investigations.**

---

# References

- MITRE ATT&CK  
  https://attack.mitre.org/

- MITRE Cyber Analytics Repository  
  https://car.mitre.org/

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
