# Incident Analysis and Scoping

> **A practical enterprise guide to reconstructing attacks, determining root cause, identifying affected assets and identities, mapping attacker activity, establishing incident scope, and building evidence-based incident timelines.**

---

## Overview

Once an alert has been validated and an incident has been declared, the next critical question is:

> **How far did the attacker get?**

Initial triage may identify one compromised endpoint, account, application, or cloud resource.

That does **not** mean the incident is limited to that asset.

A compromised workstation may be:

```text
Initial Endpoint
      │
      ├── Credential Theft
      │
      ├── Lateral Movement
      │
      ├── Persistence
      │
      └── Command and Control
              │
              ▼
          Other Systems
```

Incident analysis determines what actually happened.

Incident scoping determines **how much of the environment was affected**.

Together, they answer:

```text
How did the attacker enter?

When did the compromise begin?

What did the attacker do?

Which accounts were involved?

Which systems were accessed?

Which privileges were obtained?

Did the attacker move laterally?

Did they establish persistence?

What data was accessed?

Was data exfiltrated?

What remains unknown?
```

The goal is to transform fragmented telemetry into an evidence-backed incident narrative.

---

# Why It Matters

Poor scoping is one of the most dangerous incident response failures.

Consider:

```text
EDR Alert
    │
    ▼
Compromised Laptop
    │
    ▼
Analyst isolates laptop
    │
    ▼
Incident marked contained
```

But investigation later reveals:

```text
Laptop
  │
  ├── Credential Theft
  │
  ▼
Domain Account
  │
  ├── Authentication
  ▼
File Server
  │
  ├── Sensitive Data Access
  ▼
Cloud Account
  │
  └── Data Download
```

The original endpoint was only the **entry point into the investigation**, not the full incident.

---

# Analysis vs Scoping

These concepts are closely related but different.

## Incident Analysis

Determines:

> **What happened?**

It focuses on:

- Attack sequence
- Techniques
- Commands
- Processes
- Authentication
- Persistence
- Network activity

## Incident Scoping

Determines:

> **How much was affected?**

It focuses on:

- Hosts
- Users
- Accounts
- Applications
- Networks
- Cloud resources
- Data
- Business units

A useful model:

```text
                INCIDENT
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
     Analysis                 Scope
        │                       │
   What happened?          What is affected?
        │                       │
        └───────────┬───────────┘
                    ▼
              Attack Narrative
```

---

# Investigation Objectives

A mature investigation should establish:

### Initial Access

How did the attacker enter?

### Execution

What code or commands were executed?

### Persistence

How did the attacker maintain access?

### Privilege Escalation

Did the attacker obtain higher privileges?

### Credential Access

Were credentials or tokens stolen?

### Discovery

What did the attacker learn about the environment?

### Lateral Movement

Did the attacker move to other systems?

### Command and Control

How did the attacker communicate externally?

### Collection

What information was gathered?

### Exfiltration

Was information transferred outside the environment?

### Impact

What damage or business disruption occurred?

---

# Investigation Model

```text
                     INCIDENT
                         │
                         ▼
                 Initial Evidence
                         │
                         ▼
                  Build Timeline
                         │
                         ▼
                  Identify Entry
                         │
                         ▼
                  Track Activity
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Identity        Endpoint        Network
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                  Expand Scope
                         │
                         ▼
                  Determine Impact
                         │
                         ▼
                  Root Cause
```

---

# Attack Timeline

The timeline is one of the most important investigative artifacts.

A timeline should combine evidence from multiple sources.

Example:

```text
08:12  Phishing email delivered
   │
08:19  User opened attachment
   │
08:20  Office process spawned PowerShell
   │
08:21  Script downloaded payload
   │
08:23  Credential access activity
   │
08:31  Suspicious authentication
   │
08:35  Remote connection to FILE-02
   │
08:42  Archive created
   │
08:51  External network connection
   │
09:05  EDR detection
   │
09:12  Host isolated
```

This provides a much stronger understanding than examining individual alerts.

---

# Timeline Data Sources

Potential sources include:

```text
Windows Events
Sysmon
EDR
Firewall
DNS
Proxy
VPN
Identity
Cloud Audit Logs
Email
Application Logs
Database Logs
File Metadata
Memory
Network Captures
```

---

# Timeline Construction

A practical timeline table:

| Timestamp | Source | Host | User | Activity | Confidence |
|---|---|---|---|---|---|
| 08:12 | Email | Mailbox | user01 | Email delivered | High |
| 08:19 | Endpoint | WS-01 | user01 | Document opened | High |
| 08:20 | Sysmon | WS-01 | user01 | PowerShell launched | High |
| 08:31 | Identity | DC | user01 | Authentication | High |
| 08:35 | Network | WS-01 | user01 | SMB connection | Medium |
| 08:42 | Endpoint | WS-01 | user01 | Archive created | High |

Confidence should reflect the strength of the evidence.

---

# Evidence Confidence

Investigators should distinguish between:

### Confirmed

Direct evidence establishes the activity.

### Highly Likely

Multiple independent indicators support the conclusion.

### Possible

Evidence suggests the activity but does not prove it.

### Unknown

Available evidence is insufficient.

Example:

```text
Confirmed:
PowerShell executed.

Confirmed:
Account authenticated to SERVER-02.

Likely:
The same attacker controlled both actions.

Possible:
Credentials were stolen from WS-01.

Unknown:
Whether files were successfully exfiltrated.
```

This prevents overstatement.

---

# Initial Access

Determining the initial access vector is one of the most important investigative objectives.

Common vectors include:

```text
Phishing
Stolen Credentials
Password Spraying
Exposed Service
Vulnerability Exploitation
Supply Chain
Remote Access
Cloud Credential Theft
Malicious Insider
Drive-by Compromise
```

---

# Initial Access Investigation

Ask:

```text
What was the first suspicious activity?

What asset was first compromised?

What account was involved?

Was there a preceding email?

Was there an external connection?

Was a vulnerability exploited?

Was a credential used?

Was the service internet-facing?
```

---

# Example: Phishing Initial Access

```text
External Email
      │
      ▼
User Mailbox
      │
      ▼
Malicious Link
      │
      ▼
Credential Harvesting
      │
      ▼
Attacker Login
      │
      ▼
Cloud Access
```

Evidence might include:

- Email headers
- Message ID
- URL
- Authentication logs
- Browser telemetry
- Identity logs
- Cloud activity

---

# Example: Exploitation Initial Access

```text
Internet
   │
   ▼
Public Service
   │
   ▼
Vulnerability
   │
   ▼
Code Execution
   │
   ▼
Web Shell
   │
   ▼
Server Compromise
```

Investigators should determine:

- Vulnerable service
- Exposure
- Exploit timestamp
- Process execution
- File creation
- Outbound connections
- Persistence

---

# Execution Analysis

After initial access, determine what the attacker executed.

Potential execution mechanisms include:

- PowerShell
- Command shell
- Python
- Bash
- WMI
- Scheduled task
- Service
- Macro
- Web shell
- Cloud API
- Container command

---

# Process Tree Analysis

A process tree provides valuable context.

Example:

```text
WINWORD.EXE
    │
    └── powershell.exe
            │
            └── mshta.exe
                    │
                    └── payload.exe
```

This may indicate a suspicious execution chain.

Compare with a normal example:

```text
WINWORD.EXE
    │
    └── winword-helper.exe
```

Context matters.

---

# Parent-Child Relationships

Investigators should examine:

- Parent process
- Child process
- User
- Command line
- Integrity level
- Execution path
- Hash
- Start time
- Network activity

Example:

```powershell
Get-CimInstance Win32_Process |
Select-Object ProcessId, ParentProcessId, Name, CommandLine
```

---

# Command-Line Analysis

Command lines can reveal:

- Scripts
- URLs
- Encoded commands
- Download locations
- Credentials
- Execution parameters
- Tools

Example suspicious pattern:

```text
powershell.exe -enc <encoded-content>
```

The presence of encoding alone does not prove maliciousness.

It should trigger contextual investigation.

---

# Credential Access

Credential theft may be central to the attack.

Potential targets include:

- Passwords
- Password hashes
- Kerberos tickets
- Browser credentials
- Tokens
- API keys
- Cloud credentials
- SSH keys
- Service account credentials

Investigators should ask:

```text
Was credential access attempted?

Which account was targeted?

Was credential material obtained?

Where could the stolen credentials be used?

Were they subsequently used elsewhere?
```

---

# Identity Pivoting

A compromised endpoint can be used to investigate identity activity.

```text
Compromised Host
      │
      ▼
User Account
      │
      ▼
Authentication Logs
      │
      ▼
Other Hosts
      │
      ▼
Additional Accounts
```

This technique can reveal lateral movement.

---

# Lateral Movement

Lateral movement occurs when an attacker moves from one compromised system to another.

Common mechanisms include:

- RDP
- SMB
- WinRM
- SSH
- Remote services
- PsExec-like mechanisms
- WMI
- Remote management tools
- Cloud administration APIs

---

# Lateral Movement Investigation

Look for:

```text
Source Host
Destination Host
Account
Protocol
Timestamp
Authentication
Process
Command
```

Example:

```text
WS-01
  │
  │ SMB
  ▼
FILE-02
  │
  │ RDP
  ▼
ADMIN-03
```

---

# Privilege Escalation

Determine whether the attacker increased privileges.

Possible paths:

```text
Standard User
     │
     ▼
Local Admin
     │
     ▼
Domain Privileges
     │
     ▼
Enterprise-Level Privileges
```

Investigate:

- New group membership
- Privileged authentication
- Token manipulation
- Exploited vulnerabilities
- Service abuse
- Credential theft

---

# Persistence

Persistence allows an attacker to maintain access.

Common mechanisms include:

```text
Scheduled Tasks
Services
Startup Items
Registry Run Keys
WMI
Web Shells
Cloud Access Keys
OAuth Applications
SSH Keys
Cron Jobs
New Accounts
```

---

# Persistence Investigation

Ask:

```text
What changed?

When did it change?

Who created the change?

Which account performed it?

What process created it?

Is it still active?

Does removing it affect legitimate operations?
```

---

# Scheduled Task Example

Windows:

```powershell
Get-ScheduledTask
```

Investigators should examine:

- Task name
- Author
- Trigger
- Action
- Executable
- Arguments
- Creation time

Linux:

```bash
crontab -l
```

and appropriate system-wide cron locations.

---

# Service Investigation

Windows:

```powershell
Get-Service
```

Further investigation may identify:

- Service executable
- Startup type
- Account
- Creation time

Linux:

```bash
systemctl list-units --type=service
```

---

# Discovery Activity

Attackers often perform discovery before moving further.

Examples:

```text
User Discovery
System Discovery
Network Discovery
Domain Discovery
Cloud Resource Discovery
Security Tool Discovery
```

Investigators may search for commands and telemetry associated with:

- Host discovery
- User enumeration
- Domain enumeration
- Network enumeration
- Process enumeration

---

# Command and Control

Determine whether compromised systems communicated with attacker infrastructure.

Potential evidence:

```text
DNS
HTTP
HTTPS
TLS
VPN
Custom Protocol
Cloud Services
```

Look for:

- Rare destinations
- Newly registered domains
- Beacon-like intervals
- Suspicious user agents
- Unusual ports
- Rare processes communicating externally

---

# DNS Investigation

Example:

```text
Host
 │
 ▼
DNS Query
 │
 ▼
Suspicious Domain
 │
 ▼
Resolved IP
 │
 ▼
Outbound Connection
```

Useful evidence:

- Query timestamp
- Domain
- Host
- User
- Process
- Destination IP
- Frequency

---

# Network Connection Analysis

Windows:

```powershell
Get-NetTCPConnection
```

Linux:

```bash
ss -tunap
```

Questions:

```text
Which process owns the connection?

Which user owns the process?

Where is the connection going?

Is the destination known?

Has this host contacted it before?
```

---

# Data Collection

Attackers may gather data before exfiltration.

Examples:

- Archive creation
- Database queries
- File copying
- Cloud storage downloads
- Email collection
- Credential collection

Potential signs:

```text
Large Archive
      │
      ▼
Temporary Directory
      │
      ▼
Network Transfer
      │
      ▼
External Destination
```

---

# Data Staging

Data staging occurs when information is gathered into a location before transfer.

Example:

```text
Multiple Files
     │
     ▼
Temporary Directory
     │
     ▼
Archive
     │
     ▼
Staging Server
     │
     ▼
External Transfer
```

Investigate:

- File creation
- Archive tools
- File sizes
- Access times
- User
- Process
- Network activity

---

# Exfiltration Investigation

Possible channels include:

- HTTPS
- DNS
- Cloud storage
- Email
- FTP
- SSH
- API
- Custom protocols

Important questions:

```text
Was data transferred?

What data?

How much?

When?

From which host?

Using which account?

To where?

Was encryption used?
```

If evidence is insufficient, report:

> **Exfiltration status: Unknown**

rather than assuming either success or failure.

---

# Cloud Investigation

Cloud incidents require a separate investigation dimension.

Potential evidence:

```text
Identity
   │
   ▼
Cloud Login
   │
   ▼
API Activity
   │
   ▼
Permission Change
   │
   ▼
Resource Access
   │
   ▼
Data Access
```

Investigate:

- Authentication
- API calls
- Role changes
- Access key creation
- Resource creation
- Security group changes
- Storage access
- Object downloads
- Persistence

---

# Cloud Scope

Determine:

```text
Affected Identity
Affected Account
Affected Subscription / Project
Affected Region
Affected Resources
Affected Data
```

A compromised cloud administrator account can potentially affect a large number of resources.

---

# Identity Scope

Identity scope should include:

```text
Users
Service Accounts
Privileged Accounts
Machine Accounts
API Keys
Access Keys
OAuth Applications
Tokens
Sessions
```

---

# Endpoint Scope

For a compromised endpoint, determine:

```text
Hostname
IP
User
OS
Processes
Files
Persistence
Network Connections
Security Controls
Other Users
```

Then pivot to similar activity across the environment.

---

# Enterprise Scope Expansion

A useful method is:

```text
Known IOC
   │
   ├── Host Search
   │
   ├── User Search
   │
   ├── Process Search
   │
   ├── Network Search
   │
   ├── DNS Search
   │
   └── Cloud Search
         │
         ▼
   Related Activity
         │
         ▼
   New IOCs
         │
         └──────────► Repeat
```

This creates an iterative investigation.

---

# IOC Pivoting

Suppose investigators identify:

```text
IP: 203.0.113.50
```

Pivot into:

```text
IP
 │
 ├── Hosts
 ├── Users
 ├── DNS
 ├── Firewall
 ├── Proxy
 ├── EDR
 └── Cloud
```

If a suspicious domain is discovered:

```text
Domain
 │
 ├── DNS Queries
 ├── Resolved IPs
 ├── Hosts
 ├── Processes
 └── Network Connections
```

Each pivot may reveal new evidence.

---

# Entity Relationship Model

Incident investigations can be represented as relationships.

```text
             User
              │
              ▼
            Host
          ┌───┴───┐
          ▼       ▼
       Process    File
          │
          ▼
       Network
          │
          ▼
        Domain
          │
          ▼
          IP
```

This graph-based thinking is particularly useful in SIEM and EDR investigations.

---

# Attack Graph

A larger incident may resemble:

```text
Phishing Email
      │
      ▼
User Credential
      │
      ▼
Cloud Account
      │
      ▼
OAuth Application
      │
      ▼
Mailbox Access
      │
      ▼
Sensitive Data
      │
      ▼
Cloud Storage
      │
      ▼
External Destination
```

This provides a high-level representation of the attack path.

---

# Root Cause Analysis

Root cause analysis asks:

> **What underlying weakness allowed the incident to occur or succeed?**

Possible root causes:

- Missing MFA
- Vulnerable application
- Excessive privileges
- Stolen credentials
- Weak segmentation
- Misconfigured cloud storage
- Missing patch
- Poor logging
- Inadequate monitoring
- User compromise

---

# Root Cause vs Trigger

These should not be confused.

### Trigger

The immediate event that started the incident.

Example:

> Employee clicked a phishing link.

### Root Cause

The underlying condition that enabled the attack.

Example:

> Credentials were not protected by phishing-resistant authentication.

The trigger explains **what happened immediately**.

The root cause explains **why the attack was able to succeed**.

---

# Five Whys

A simple root-cause technique:

```text
Why was the account compromised?
        ↓
Credentials were stolen.

Why were stolen credentials usable?
        ↓
Authentication relied on a password.

Why was password-only authentication allowed?
        ↓
MFA coverage was incomplete.

Why was MFA coverage incomplete?
        ↓
Legacy applications were exempted.

Why were legacy applications not modernized?
        ↓
Migration had not been completed.
```

This reveals a deeper remediation opportunity.

---

# Scope Categories

An incident can be scoped across multiple dimensions.

```text
                 INCIDENT SCOPE
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
    Identity        Endpoint       Network
       │              │              │
       ▼              ▼              ▼
    Users           Hosts           IPs
    Accounts        Servers         Domains
    Tokens          Processes       Connections
       │              │              │
       └──────────────┼──────────────┘
                      ▼
                    Cloud
                      │
                      ▼
                  Applications
                      │
                      ▼
                     Data
```

---

# Scope Confidence

Not every scope determination is equally certain.

Example:

```text
Confirmed affected:
WS-01
WS-02

Likely affected:
User01 account

Potentially affected:
FILE-01

No evidence currently found:
DB-01

Unknown:
Cloud storage exposure
```

This is much more useful than declaring the environment simply "compromised."

---

# Negative Evidence

Negative findings can be valuable.

For example:

```text
No evidence of:
- Lateral movement to production servers
- Persistence on WS-02
- Privilege escalation
- External data transfer
```

However:

> Absence of evidence is not always evidence of absence.

If telemetry was unavailable, the correct conclusion may be:

> **Unable to determine due to insufficient telemetry.**

---

# Evidence Gaps

An investigation should explicitly document missing evidence.

Examples:

```text
EDR not installed on server
DNS logs retained for only 24 hours
Cloud audit logs disabled
Firewall logs unavailable
Memory capture not performed
```

These gaps affect confidence in the final conclusions.

---

# Common Investigation Mistakes

## 1. Stopping at the First Compromised Host

The first host may only be the initial foothold.

## 2. Focusing Only on Malware

The real issue may be identity compromise.

## 3. Ignoring Authentication

Attackers frequently use legitimate credentials.

## 4. Assuming IOC = Full Scope

Finding one malicious IP does not reveal every attacker-controlled resource.

## 5. Ignoring Cloud

Cloud environments may contain the highest-value data.

## 6. Ignoring Service Accounts

Attackers may abuse non-human identities.

## 7. Failing to Build a Timeline

Individual alerts rarely tell the whole story.

## 8. Confusing Correlation With Causation

Two events occurring close together does not automatically prove that one caused the other.

## 9. Ignoring Unknowns

Investigations should explicitly identify what cannot be determined.

## 10. Modifying Evidence Too Early

Containment and investigation actions should consider forensic impact.

---

# Common Scoping Misconfigurations

### Incomplete EDR Coverage

Some hosts cannot be investigated.

### Short Log Retention

Historical activity disappears.

### Missing Cloud Audit Logs

Cloud actions cannot be reconstructed.

### Poor Asset Inventory

Affected systems cannot be identified reliably.

### No Centralized Identity Logging

Account activity cannot be correlated.

### Unsynchronized Clocks

Timelines become unreliable.

### Incomplete DNS Visibility

C2 and infrastructure relationships become harder to identify.

---

# Practical Commands

These commands support authorized investigation.

---

## Windows

### Processes

```powershell
Get-CimInstance Win32_Process |
Select-Object ProcessId,ParentProcessId,Name,CommandLine
```

### Network Connections

```powershell
Get-NetTCPConnection |
Select-Object LocalAddress,LocalPort,RemoteAddress,RemotePort,State,OwningProcess
```

### Scheduled Tasks

```powershell
Get-ScheduledTask
```

### Services

```powershell
Get-CimInstance Win32_Service |
Select-Object Name,State,StartMode,StartName,PathName
```

### Local Administrators

```powershell
Get-LocalGroupMember -Group "Administrators"
```

### Recent Security Events

```powershell
Get-WinEvent -LogName Security -MaxEvents 200
```

---

# Linux

### Processes

```bash
ps aux --forest
```

### Network Connections

```bash
ss -tunap
```

### Listening Services

```bash
ss -lntup
```

### Logged-In Users

```bash
w
```

### Recent Login Activity

```bash
last
```

### Authentication Logs

```bash
grep -i "authentication" /var/log/auth.log
```

### Cron

```bash
crontab -l
```

---

# File Investigation

### Linux

```bash
find /tmp -type f -mtime -1 -ls
```

### Windows

```powershell
Get-ChildItem $env:TEMP -File |
Sort-Object LastWriteTime -Descending
```

These searches should be adapted to the specific investigation and environment.

---

# Hash Collection

Windows:

```powershell
Get-FileHash .\suspicious.exe -Algorithm SHA256
```

Linux:

```bash
sha256sum suspicious
```

Hashes should be recorded as investigation artifacts.

---

# Practical Lab

# Lab — Reconstructing a Multi-Stage Attack

## Scenario

A fictional enterprise detects suspicious PowerShell activity on:

```text
Host: WS-104
User: analyst01
Time: 10:42 UTC
```

The initial alert shows:

```text
WINWORD.EXE
      │
      └── powershell.exe
              │
              └── script.ps1
```

The script contacted:

```text
updates-example.example
```

---

# Evidence Provided

### Endpoint

```text
10:42
WINWORD.EXE launched PowerShell

10:43
PowerShell executed script.ps1

10:44
Network connection established
```

### Identity

```text
10:51
analyst01 authenticated to FILE-02
```

### Network

```text
10:52
WS-104 → FILE-02 SMB
```

### File Server

```text
11:02
Large archive created
```

### Firewall

```text
11:15
FILE-02 → external destination
```

---

# Task 1 — Build Timeline

Construct:

```text
10:42  Initial execution
10:43  Script execution
10:44  External connection
10:51  Authentication
10:52  Lateral movement
11:02  Data staging
11:15  Possible exfiltration
```

---

# Task 2 — Identify Attack Stages

Map the activity to:

```text
Initial Access
Execution
Credential Access
Lateral Movement
Collection
Staging
Exfiltration
```

Only mark stages supported by evidence.

---

# Task 3 — Determine Scope

Investigate:

```text
WS-104
analyst01
FILE-02
Related accounts
Related hosts
External destination
```

---

# Task 4 — Determine Unknowns

For example:

```text
Was the credential stolen?

Was the archive sensitive?

Was the external transfer successful?

Were additional systems compromised?
```

---

# Task 5 — Determine Containment Requirements

Possible actions:

```text
Isolate WS-104
Disable / reset analyst01
Restrict FILE-02
Preserve evidence
Block malicious infrastructure
Search environment for related activity
```

---

# Task 6 — Root Cause

Determine whether the underlying cause was:

- Phishing
- Credential theft
- Vulnerability
- Misconfiguration
- Excessive privileges

Do not select a root cause without supporting evidence.

---

# Expected Investigation Report

```text
Incident:
Multi-Stage Endpoint Compromise

Initial Access:
Malicious Office document

Execution:
PowerShell

Initial Host:
WS-104

User:
analyst01

Lateral Movement:
WS-104 → FILE-02

Collection:
Archive created on FILE-02

Exfiltration:
Potential external transfer

Confirmed Scope:
WS-104
analyst01
FILE-02

Unknown:
Exact data transferred

Containment:
Endpoint isolated
Identity secured
FILE-02 restricted

Further Actions:
Enterprise-wide IOC hunt
Credential investigation
Forensic analysis
Detection improvements
```

---

# Advanced Lab — Scope Expansion

Start with one known IOC:

```text
Domain:
updates-example.example
```

Perform pivots:

```text
Domain
 │
 ├── DNS
 │
 ├── Hosts
 │
 ├── Processes
 │
 ├── Users
 │
 └── Network Connections
```

Suppose the investigation identifies:

```text
WS-104
WS-108
WS-212
```

Now pivot from each host:

```text
Host
 │
 ├── User
 ├── Process
 ├── Network
 ├── Authentication
 └── Persistence
```

Continue until new evidence stops expanding the scope.

This demonstrates an important IR principle:

> **Scope should be evidence-driven and iterative.**

---

# Investigation Checklist

## Initial Analysis

```text
[ ] Incident validated
[ ] Initial alert reviewed
[ ] Evidence preserved
[ ] Initial host identified
[ ] Initial user identified
[ ] Initial timestamp identified
```

## Timeline

```text
[ ] Initial access identified
[ ] Execution identified
[ ] Persistence investigated
[ ] Privilege escalation investigated
[ ] Credential access investigated
[ ] Lateral movement investigated
[ ] Collection investigated
[ ] Exfiltration investigated
```

## Scope

```text
[ ] Hosts identified
[ ] Users identified
[ ] Accounts identified
[ ] Network indicators identified
[ ] Cloud resources identified
[ ] Applications identified
[ ] Data affected identified
```

## Confidence

```text
[ ] Confirmed findings documented
[ ] Likely findings documented
[ ] Possible findings documented
[ ] Unknowns documented
[ ] Evidence gaps documented
```

---

# Interview Questions

## 1. What is incident scoping?

Incident scoping determines the breadth of a compromise, including affected hosts, users, identities, applications, cloud resources, networks, and data.

---

## 2. Why is scoping important?

Because the initially detected system may only represent one part of a larger attack.

---

## 3. What is an attack timeline?

An attack timeline is a chronological reconstruction of relevant events used to understand how an incident progressed.

---

## 4. What evidence can be used to build an incident timeline?

Examples include:

- EDR
- Sysmon
- Windows Event Logs
- Linux logs
- Authentication
- DNS
- Firewall
- Proxy
- Cloud audit logs
- Email
- Application logs
- Network captures

---

## 5. How do you identify initial access?

Investigate the earliest known suspicious activity and determine how the attacker obtained their first foothold.

---

## 6. What is lateral movement?

Lateral movement is the process of an attacker moving from one compromised system or identity to another.

---

## 7. How do you investigate lateral movement?

Correlate:

- Authentication
- Remote services
- Network connections
- Process execution
- User accounts
- Source and destination systems

---

## 8. What is persistence?

Persistence refers to mechanisms that allow an attacker to maintain access after initial compromise or system restart.

---

## 9. Why are service accounts important during scoping?

Service accounts may have broad permissions and can provide attackers with access to multiple systems.

---

## 10. What is root cause analysis?

Root cause analysis identifies the underlying weakness that enabled or facilitated the incident.

---

## 11. What is the difference between a trigger and a root cause?

The trigger is the immediate event that initiated the incident.

The root cause is the deeper condition that allowed the incident to occur or succeed.

---

## 12. What should you do when evidence is incomplete?

Document the limitation and clearly classify the finding as unknown or unconfirmed rather than making unsupported assumptions.

---

## 13. Why should investigators search beyond the initial host?

Attackers commonly use compromised systems for credential theft, lateral movement, persistence, and access to additional systems.

---

## 14. How can you scope a compromise using an IOC?

Pivot from the IOC into:

```text
Hosts
Users
Processes
Network
DNS
Authentication
Cloud
```

Then identify related activity and newly discovered indicators.

---

## 15. What is the difference between evidence and inference?

Evidence is directly observable information.

Inference is a conclusion derived from available evidence.

Professional incident reports should clearly distinguish them.

---

# Professional Incident Analysis Template

```text
Incident ID:
Incident Name:
Severity:
Incident Commander:

## Executive Summary

## Initial Detection

## Initial Access

## Timeline

## Affected Users

## Affected Hosts

## Affected Applications

## Affected Cloud Resources

## Attack Techniques

## Credential Activity

## Persistence

## Lateral Movement

## Command and Control

## Collection

## Exfiltration

## Business Impact

## Root Cause

## Confirmed Findings

## Likely Findings

## Unknowns

## Evidence Gaps

## Containment

## Eradication

## Recovery

## Recommendations

## Detection Improvements
```

---

# Detection Engineering Feedback

Incident analysis should improve future detection.

Example:

```text
Investigation
     │
     ▼
Attacker Behavior Identified
     │
     ▼
Detection Gap
     │
     ▼
New Detection
     │
     ▼
Test Against Historical Data
     │
     ▼
Deploy
     │
     ▼
Monitor
```

Potential improvements:

- New SIEM rule
- EDR detection
- Identity alert
- Network detection
- Cloud detection
- Logging enhancement
- Asset coverage improvement

---

# Threat Hunting Feedback

Incident scoping can also create new hunting hypotheses.

Example:

```text
Compromised Host
      │
      ▼
Suspicious PowerShell
      │
      ▼
Hunt Hypothesis
      │
      ▼
Search Environment
      │
      ▼
Additional Hosts
      │
      ▼
Expanded Incident
```

This is why incident response and threat hunting should operate as complementary capabilities.

---

# Incident Analysis Maturity

## Level 1 — Basic

- Single-host investigation
- Limited timeline
- Manual log review

## Level 2 — Repeatable

- Standard timeline
- IOC pivots
- Basic scoping

## Level 3 — Defined

- Cross-source correlation
- Identity investigation
- Network and endpoint integration

## Level 4 — Measured

- Investigation metrics
- Evidence confidence
- Automated enrichment
- Scope validation

## Level 5 — Optimized

- Graph-based investigation
- Automated pivoting
- Threat-informed analysis
- Continuous detection feedback

---

# Key Metrics

Useful investigation metrics include:

### Time to Scope

How long it takes to establish the likely incident boundary.

### Time to Root Cause

How long it takes to determine the underlying cause.

### Investigation Coverage

Percentage of relevant telemetry sources examined.

### Evidence Completeness

Percentage of required evidence successfully collected.

### Scope Accuracy

How often initial scope estimates match later findings.

### Unknown Rate

Number of major questions that remain unanswered because of evidence limitations.

Metrics should improve investigation quality rather than encourage premature closure.

---

# Key Takeaways

Incident analysis transforms raw evidence into an understanding of what happened.

Incident scoping determines how far the compromise reached.

The core workflow is:

```text
Incident
   ↓
Preserve Evidence
   ↓
Build Timeline
   ↓
Identify Initial Access
   ↓
Analyze Attacker Activity
   ↓
Pivot Across Identity / Endpoint / Network / Cloud
   ↓
Expand Scope
   ↓
Determine Impact
   ↓
Identify Root Cause
   ↓
Document Confirmed Findings
   ↓
Document Unknowns
```

The most important principles are:

- Do not stop at the first compromised host
- Build timelines from multiple evidence sources
- Follow identities as well as machines
- Investigate lateral movement
- Search for persistence
- Track attacker infrastructure
- Treat scope as iterative
- Separate facts from inference
- Explicitly document unknowns
- Record evidence gaps
- Feed findings into threat hunting and detection engineering

> **The objective of incident analysis is not merely to explain the alert. It is to reconstruct the attack and understand its true impact.**

---

# References

### NIST

**Computer Security Incident Handling Guide — SP 800-61**

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### MITRE ATT&CK

https://attack.mitre.org/

### CISA

https://www.cisa.gov/

### FIRST

https://www.first.org/

### SANS

https://www.sans.org/

### CIS Controls

https://www.cisecurity.org/controls

### Sigma

https://sigmahq.io/

---

# Chapter Summary

A security incident rarely presents itself as a complete story.

Investigators receive fragments:

```text
Alert
Log
Process
Authentication
DNS Query
Network Connection
File
Cloud Event
```

The investigator's responsibility is to connect those fragments into an evidence-backed narrative:

```text
Initial Access
      ↓
Execution
      ↓
Persistence
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
      ↓
Impact
```

while continuously determining:

```text
What is confirmed?
What is likely?
What is possible?
What remains unknown?
```

> **Good incident analysis explains the attack. Good scoping explains its boundaries. Together, they provide the foundation for effective containment and eradication.**
