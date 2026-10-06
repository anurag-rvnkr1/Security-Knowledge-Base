# Endpoint Detection & EDR Hunting

## Overview

Endpoint Detection and Response (EDR) is a core capability of modern security operations. EDR platforms continuously collect endpoint telemetry, correlate events, detect suspicious behavior, provide investigation context, and support response actions.

Threat hunters use EDR data to investigate activity that may not trigger a traditional signature-based alert.

A mature endpoint hunting capability combines:

- Process telemetry
- Command-line activity
- File activity
- Registry activity
- Network connections
- User and identity context
- Authentication events
- Persistence mechanisms
- Script execution
- Security-control changes
- Endpoint configuration
- Parent-child process relationships
- Behavioral detections
- Threat intelligence
- MITRE ATT&CK techniques
- Host and user baselines

The goal is not simply to search for malware.

The goal is to answer:

> **What happened on this endpoint, why did it happen, who initiated it, what did it touch, and what happened next?**

---

# Why It Matters

Traditional endpoint security often relies heavily on known signatures.

Modern attackers frequently use:

- Legitimate administrative tools
- PowerShell
- WMI
- Windows Management Instrumentation
- Scheduled tasks
- Remote services
- Scripting engines
- Trusted binaries
- Cloud administration tools
- Valid credentials
- Memory-resident techniques
- Fileless execution
- Living-off-the-Land techniques

Therefore, the following may not be inherently malicious:

```text
powershell.exe
cmd.exe
wscript.exe
cscript.exe
mshta.exe
rundll32.exe
regsvr32.exe
wmic.exe
schtasks.exe
sc.exe
net.exe
bitsadmin.exe
```

The important question is:

```text
WHO
 │
 ├── User
 ├── Account
 └── Parent Process
      │
      ▼
WHAT
 │
 ├── Process
 ├── Command Line
 ├── File
 └── Network Connection
      │
      ▼
WHY
 │
 ├── Expected Business Activity
 ├── Administrative Activity
 ├── Software Update
 └── Suspicious Behavior
      │
      ▼
WHAT NEXT?
 │
 ├── Persistence
 ├── Credential Access
 ├── Discovery
 ├── Lateral Movement
 └── Exfiltration
```

This context is the foundation of EDR threat hunting.

---

# EDR Architecture

A typical EDR architecture looks like:

```text
                    ENDPOINTS
        ┌────────────┬────────────┬────────────┐
        │            │            │            │
        ▼            ▼            ▼            ▼
     Windows       Linux        macOS       Servers
        │            │            │            │
        └────────────┴────────────┴────────────┘
                         │
                         ▼
                  EDR SENSOR / AGENT
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
    Processes         Files           Network
        │                │                │
        ▼                ▼                ▼
   Registry          Scripts        Authentication
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  Telemetry Pipeline
                         │
                         ▼
                  EDR Cloud / Server
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
         Detection    Search      Analytics
             │           │           │
             └───────────┼───────────┘
                         ▼
                       SOC
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
           Analyst     Hunter      IR Team
```

---

# EPP vs EDR vs XDR

## EPP

Endpoint Protection Platform primarily focuses on prevention.

Typical capabilities include:

- Malware prevention
- Antivirus
- Exploit prevention
- Web protection
- Application control
- Behavioral blocking

Conceptually:

```text
Threat
  │
  ▼
EPP
  │
  ├── Detect
  └── Block
```

---

## EDR

EDR emphasizes visibility, investigation, detection, and response.

```text
Endpoint
   │
   ▼
Telemetry
   │
   ▼
Detection
   │
   ▼
Investigation
   │
   ▼
Response
```

EDR allows analysts to reconstruct endpoint activity.

---

## XDR

XDR extends the detection and investigation model across multiple security domains.

```text
Endpoint ──────┐
Identity ──────┤
Email ─────────┤
Network ───────┼──► XDR ───► Correlation
Cloud ─────────┤
Applications ──┘
```

The exact capabilities vary between vendors.

---

# Endpoint Telemetry

A threat hunter should understand the telemetry available before designing a hunt.

Important telemetry categories include:

| Telemetry | Examples |
|---|---|
| Process | Creation, termination, parent-child relationships |
| Command line | Arguments passed to processes |
| File | Create, modify, rename, delete |
| Registry | Keys and values |
| Network | Connections, DNS, ports |
| Authentication | Logon, logout, failures |
| User | Account and session context |
| Script | PowerShell, JavaScript, VBScript |
| Service | Service installation/start |
| Scheduled task | Creation and execution |
| Driver | Driver loading |
| Security controls | EDR/AV changes |
| Browser | Downloads and execution context |
| USB | Removable device activity |

Telemetry quality determines hunting quality.

---

# Endpoint Investigation Model

A useful investigation model is:

```text
HOST
 │
 ├── USER
 │
 ├── PROCESS
 │     │
 │     ├── Parent
 │     ├── Child
 │     ├── Command Line
 │     └── Integrity Level
 │
 ├── FILE
 │
 ├── REGISTRY
 │
 ├── NETWORK
 │
 ├── AUTHENTICATION
 │
 └── PERSISTENCE
```

A suspicious process should therefore never be investigated in isolation.

---

# Process Tree Hunting

Process trees are one of the most valuable EDR hunting capabilities.

Example:

```text
explorer.exe
    │
    └── winword.exe
          │
          └── powershell.exe
                │
                └── rundll32.exe
                      │
                      └── suspicious.dll
```

A hunter should ask:

1. Why did Word launch PowerShell?
2. What document caused the process?
3. What command line was used?
4. Where did the DLL originate?
5. What network connection followed?
6. Did the process create persistence?
7. Did the user normally perform this activity?

---

# Parent-Child Relationships

Commonly suspicious relationships include:

```text
winword.exe
    └── powershell.exe
```

```text
excel.exe
    └── cmd.exe
```

```text
outlook.exe
    └── mshta.exe
```

```text
browser.exe
    └── powershell.exe
```

```text
w3wp.exe
    └── cmd.exe
```

These are not automatically malicious.

Context determines severity.

For example:

```text
Word → PowerShell
```

may indicate malicious document execution.

But:

```text
Administrator Script
    → Word automation
    → PowerShell
```

could be legitimate.

---

# Command-Line Hunting

Command-line arguments frequently provide the missing context.

Example:

```text
powershell.exe
```

provides limited information.

Whereas:

```text
powershell.exe -NoProfile -ExecutionPolicy Bypass ...
```

provides significantly more context.

Potentially suspicious characteristics include:

- Encoded command usage
- Hidden execution
- Unusual parent process
- Download behavior
- Script execution from temporary directories
- Execution from user-writable paths
- Obfuscated arguments
- Unusual administrative tools
- Network retrieval followed by execution

Avoid treating one command-line switch as proof of compromise.

---

# PowerShell Hunting

PowerShell is widely used by administrators and attackers.

Useful telemetry can include:

- Process creation
- Command line
- Script block logging
- Module logging
- PowerShell operational logs
- EDR behavioral events

A useful hunting flow is:

```text
PowerShell
   │
   ▼
Who launched it?
   │
   ▼
What was the parent?
   │
   ▼
What arguments were used?
   │
   ▼
What files were touched?
   │
   ▼
What network connections occurred?
   │
   ▼
What happened afterward?
```

---

# Script Execution Hunting

Important script interpreters include:

```text
powershell.exe
cmd.exe
wscript.exe
cscript.exe
mshta.exe
python.exe
perl.exe
ruby.exe
bash.exe
```

Hunt based on combinations rather than simple process names.

For example:

```text
Office Application
      +
Script Interpreter
      +
External Network Connection
```

is more interesting than:

```text
PowerShell
```

alone.

---

# Living-off-the-Land Hunting

Living-off-the-Land (LotL) activity uses legitimate operating-system utilities.

Examples include:

```text
PowerShell
WMI
BITS
Rundll32
Regsvr32
Mshta
Schtasks
Sc
Certutil
Net
Whoami
Ipconfig
Nltest
```

The hunting challenge is distinguishing:

```text
Legitimate Administration
```

from:

```text
Abuse of Legitimate Functionality
```

A useful analytical model:

```text
Tool
 +
User
 +
Parent Process
 +
Command Line
 +
Target
 +
Time
 +
Network
 +
Frequency
```

---

# File Activity Hunting

EDR platforms can provide visibility into:

- File creation
- Modification
- Rename
- Deletion
- Execution
- Hashes
- File paths
- File reputation

Important locations may include:

```text
%TEMP%
%APPDATA%
%LOCALAPPDATA%
%PROGRAMDATA%
C:\Users\Public\
C:\Windows\Temp\
Downloads\
Startup\
```

Linux environments may require different path analysis.

A suspicious file should be investigated using:

```text
Path
Hash
Signer
Creation time
Modification time
Parent process
User
Execution history
Network activity
```

---

# Temporary Directory Hunting

Attackers may stage files in temporary or user-writable locations.

Examples:

```text
C:\Users\user\AppData\Local\Temp\
C:\Windows\Temp\
/tmp/
/var/tmp/
```

Potentially interesting sequence:

```text
Browser
   │
   ▼
Download
   │
   ▼
Temp Directory
   │
   ▼
Execution
   │
   ▼
PowerShell
   │
   ▼
Network Connection
```

The sequence is more important than the directory alone.

---

# Registry Hunting

Windows persistence and configuration changes can involve registry activity.

Areas worth monitoring include:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

```text
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```

Other registry areas may contain:

- Services
- Policies
- Startup configuration
- Security settings
- Application configuration

Hunting should focus on:

```text
Who changed it?
What changed?
When?
What process performed the change?
What value was introduced?
Was the process expected?
```

---

# Network Hunting

Endpoint network telemetry can reveal:

```text
Process
   │
   ▼
Destination IP
   │
   ▼
Destination Port
   │
   ▼
Domain
   │
   ▼
DNS Query
   │
   ▼
TLS / HTTP
```

Useful investigation questions:

- Which process made the connection?
- Was the process expected to communicate externally?
- Is the destination new for the host?
- Is the destination rare across the organization?
- Was DNS resolution involved?
- Did the connection occur immediately after process creation?
- Did the process transmit unusual amounts of data?

---

# Process-to-Network Correlation

Consider:

```text
winword.exe
    │
    └── powershell.exe
            │
            └── outbound connection
                    │
                    └── rare external domain
```

This is significantly more useful than simply searching for a suspicious domain.

The endpoint provides behavioral context.

---

# Authentication Context

Endpoint telemetry should be correlated with identity.

For every suspicious process ask:

```text
USER
 │
 ├── Username
 ├── Domain
 ├── Privilege
 ├── Logon Type
 └── Session
```

Then correlate:

```text
User
  │
  ▼
Authentication
  │
  ▼
Process
  │
  ▼
Network
```

This helps identify:

- Compromised accounts
- Privilege escalation
- Lateral movement
- Service account abuse
- Remote execution

---

# Privilege Context

Important process attributes may include:

- User
- Integrity level
- Elevated status
- Token information
- Session
- Parent process
- Administrative group membership

A suspicious sequence could be:

```text
Standard User
      │
      ▼
Suspicious Process
      │
      ▼
Privilege Escalation
      │
      ▼
Administrative Process
```

This should trigger deeper investigation.

---

# Endpoint Baselines

Threat hunting becomes more effective when normal behavior is understood.

Examples:

```text
Normal:
Developer → VS Code → Git → Python

Normal:
Administrator → PowerShell → Server Management

Normal:
Browser → Browser Helper Processes
```

Potential anomaly:

```text
Developer Laptop
    │
    └── Excel
          │
          └── PowerShell
                │
                └── Network Connection
```

Baselines should consider:

- User
- Host
- Department
- Role
- Application
- Time
- Location
- Process frequency

---

# Rarity-Based Hunting

Rare activity can be useful as a hunting signal.

Examples:

```text
Rare Process
Rare Parent-Child Relationship
Rare Command Line
Rare Destination
Rare User/Host Combination
Rare Persistence Mechanism
```

Example:

```text
PowerShell launched by Word
```

may occur:

```text
1 time / 10,000 endpoints
```

This deserves investigation.

However:

> **Rare does not automatically mean malicious.**

---

# Behavioral Detection

Behavioral detection combines multiple signals.

Example:

```text
Office Process
      │
      ▼
PowerShell
      │
      ▼
Temporary File
      │
      ▼
External Network
      │
      ▼
Persistence
```

Each event may be benign independently.

The combined chain is much more suspicious.

---

# Detection Engineering

A mature SOC converts successful hunts into detections.

Pipeline:

```text
Threat Hunt
    │
    ▼
Interesting Behavior
    │
    ▼
Validated Pattern
    │
    ▼
Detection Rule
    │
    ▼
Testing
    │
    ▼
Deployment
    │
    ▼
Monitoring
    │
    ▼
Tuning
```

A detection should have:

- Detection logic
- Data source
- Required fields
- Severity
- ATT&CK mapping
- Investigation guidance
- False-positive guidance
- Response recommendation

---

# Example Detection Concept

Detection objective:

> Identify suspicious scripting activity originating from Office applications.

Conceptual logic:

```text
IF
    Parent Process IN (
        winword.exe,
        excel.exe,
        powerpnt.exe
    )

AND

    Child Process IN (
        powershell.exe,
        cmd.exe,
        wscript.exe,
        cscript.exe,
        mshta.exe
    )

THEN

    Generate Investigation Signal
```

Improve the detection by adding:

```text
+
Rare User/Host Relationship
+
Suspicious Command Line
+
External Network Connection
+
File From Internet Zone
```

---

# Microsoft Defender Hunting Concepts

Microsoft Defender environments commonly expose endpoint telemetry suitable for advanced hunting.

Typical conceptual datasets include:

```text
DeviceProcessEvents
DeviceFileEvents
DeviceNetworkEvents
DeviceRegistryEvents
DeviceLogonEvents
DeviceEvents
```

Example conceptual query:

```kusto
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| project Timestamp,
          DeviceName,
          AccountName,
          InitiatingProcessFileName,
          ProcessCommandLine
| order by Timestamp desc
```

This is useful for finding PowerShell execution and its initiating process.

---

# PowerShell Parent-Process Hunt

```kusto
DeviceProcessEvents
| where FileName =~ "powershell.exe"
| where InitiatingProcessFileName in~ (
    "winword.exe",
    "excel.exe",
    "outlook.exe",
    "powerpnt.exe"
)
| project Timestamp,
          DeviceName,
          AccountName,
          InitiatingProcessFileName,
          ProcessCommandLine
```

This is a starting point, not a complete production detection.

---

# Network Correlation

A useful workflow is:

```text
Process Event
     │
     ▼
Identify Device
     │
     ▼
Identify Process
     │
     ▼
Search Network Events
     │
     ▼
Identify Destination
     │
     ▼
Enrich Domain/IP
```

The objective is to reconstruct the execution chain.

---

# CrowdStrike-Style Investigation Concepts

EDR platforms such as CrowdStrike provide endpoint telemetry and process-centric investigation capabilities.

Conceptually, hunters may investigate:

```text
Host
 │
 ├── Process
 ├── User
 ├── File
 ├── Network
 └── Detection
```

A strong investigation focuses on:

```text
Process Tree
+
Command Line
+
User
+
Hash
+
Network
+
Timeline
```

Vendor terminology and query syntax vary by product version and deployment.

---

# SentinelOne Investigation Concepts

SentinelOne-style endpoint investigations commonly emphasize:

- Storyline relationships
- Process activity
- File activity
- Network activity
- Behavioral detections
- Endpoint response

Conceptually:

```text
Initial Process
      │
      ├── Child
      │    ├── File
      │    └── Network
      │
      └── Persistence
```

The important principle is to understand the complete behavioral chain rather than focusing on a single alert.

---

# osquery

osquery exposes operating-system state through SQL-like queries.

Example:

```sql
SELECT
    name,
    path,
    pid
FROM processes;
```

Network connections:

```sql
SELECT
    pid,
    local_address,
    local_port,
    remote_address,
    remote_port,
    state
FROM process_open_sockets;
```

Listening ports:

```sql
SELECT
    pid,
    address,
    port,
    protocol
FROM listening_ports;
```

Users:

```sql
SELECT
    username,
    uid,
    gid,
    directory
FROM users;
```

Scheduled tasks and persistence can also be investigated depending on operating system and available tables.

---

# Velociraptor

Velociraptor is an open-source digital forensics and endpoint visibility platform.

It can be used for:

- Endpoint collection
- Artifact collection
- Threat hunting
- Incident response
- Remote investigation
- File analysis
- Process analysis
- Timeline generation

Conceptually:

```text
Hunt Query
    │
    ▼
Endpoint Collection
    │
    ▼
Artifacts
    │
    ▼
Analysis
    │
    ▼
Investigation
```

It is particularly useful when a SOC needs deeper endpoint visibility beyond traditional SIEM logs.

---

# EDR Evasion Concepts

Threat hunters should understand how attackers attempt to reduce visibility.

Examples include:

- Disabling security tools
- Tampering with logging
- Process injection
- Masquerading
- Living-off-the-Land
- Obfuscation
- Memory-only execution
- Security-control exclusion abuse
- Driver abuse

Hunting principle:

> **When telemetry suddenly disappears, investigate why.**

For example:

```text
Normal Endpoint
      │
      ▼
High Telemetry
      │
      ▼
Security Control Change
      │
      ▼
Telemetry Drop
      │
      ▼
Suspicious Activity
```

A telemetry gap can itself become a detection signal.

---

# Security Tool Tampering

Monitor changes involving:

```text
EDR services
AV configuration
Security exclusions
Security agents
Logging configuration
Event collection
Endpoint protection settings
```

Investigate:

```text
Who made the change?
Which process made it?
Was the account authorized?
Was the change approved?
What happened afterward?
```

---

# Process Injection Hunting

Process injection attempts to execute code within another process context.

Potential signals include:

```text
Unexpected process access
Cross-process memory operations
Remote thread creation
Unusual module loading
Suspicious process relationships
```

Detection should avoid relying on one low-level signal.

A better model is:

```text
Process A
   │
   ├── Unusual access to Process B
   │
   ├── Memory manipulation
   │
   └── Suspicious execution
          │
          ▼
       Investigate
```

---

# Masquerading

Attackers may name malicious files after legitimate programs.

Example:

```text
svchost.exe
explorer.exe
chrome.exe
lsass.exe
```

A file name alone is insufficient.

Investigate:

```text
Name
Path
Digital Signature
Hash
Parent Process
User
Command Line
Network Activity
```

For example:

```text
svchost.exe
```

running from an unexpected user-writable directory should receive additional scrutiny.

---

# Hash Hunting

Hashes can be used for:

- Malware identification
- Threat intelligence matching
- Prevalence analysis
- File tracking
- Incident scoping

Useful fields:

```text
MD5
SHA-1
SHA-256
```

Prefer stronger hashes such as SHA-256 when available.

Example hunting concept:

```text
Hash
 │
 ├── Known malicious?
 ├── Seen on other endpoints?
 ├── First seen?
 ├── Last seen?
 └── Associated process?
```

---

# Prevalence Hunting

One of the most useful questions in EDR is:

> **How many systems have this artifact?**

Example:

```text
Suspicious Hash
      │
      ▼
Search Enterprise
      │
      ├── 1 Host
      ├── 2 Users
      └── 3 Executions
```

A rare artifact may be more interesting than a widely deployed corporate application.

---

# First-Seen / Last-Seen Analysis

Important questions:

```text
When was this first observed?
When was it last observed?
Where was it observed?
Who executed it?
```

Timeline:

```text
Day 1 ───── File First Seen
Day 2 ───── Process Execution
Day 3 ───── Network Activity
Day 4 ───── Persistence
Day 5 ───── Detection
```

This helps determine the probable intrusion window.

---

# Endpoint Timeline Reconstruction

A typical timeline may look like:

```text
09:01:22
User Login
     │
09:02:10
Browser Started
     │
09:04:55
Document Downloaded
     │
09:05:02
Office Application Started
     │
09:05:04
PowerShell Started
     │
09:05:08
File Created
     │
09:05:11
External Connection
     │
09:06:30
Scheduled Task Created
```

This is significantly more useful than examining alerts independently.

---

# Investigation Workflow

## Step 1 — Validate the Alert

Determine:

```text
What triggered?
When?
Which endpoint?
Which user?
Which process?
```

---

## Step 2 — Build the Process Tree

```text
Root Process
    │
    ├── Parent
    ├── Current Process
    └── Children
```

---

## Step 3 — Analyze Command Line

Look for:

- Obfuscation
- Unusual arguments
- Download behavior
- Execution from unusual paths
- Encoded data

---

## Step 4 — Analyze Files

Check:

```text
Path
Hash
Signer
Creation time
Modification time
Prevalence
```

---

## Step 5 — Analyze Network

Check:

```text
Destination
Port
Domain
DNS
Process
Frequency
Reputation
```

---

## Step 6 — Analyze User

Determine:

```text
Who executed it?
Was the user active?
Was the account privileged?
Was there unusual authentication?
```

---

## Step 7 — Search for Persistence

Investigate:

```text
Services
Scheduled Tasks
Registry Run Keys
Startup Locations
WMI
Accounts
SSH Keys
```

---

## Step 8 — Scope the Incident

Search across:

```text
Host
User
Hash
Domain
IP
Process
Command Line
File Name
```

---

## Step 9 — Determine ATT&CK Mapping

Example:

```text
PowerShell
   → T1059.001

Scheduled Task
   → T1053.005

Command Shell
   → T1059.003
```

---

## Step 10 — Contain and Respond

Depending on incident severity:

```text
Isolate Host
Disable Account
Terminate Process
Remove Persistence
Block IOC
Collect Evidence
Reset Credentials
```

Actions should follow organizational incident-response procedures.

---

# False Positives

EDR generates large amounts of telemetry.

Common false positives include:

- IT administration
- Software deployment
- Patch management
- Developer tooling
- Monitoring software
- Backup software
- Security scanners
- Automated scripts

Do not immediately suppress a detection.

Instead:

```text
Alert
 │
 ▼
Investigate
 │
 ▼
Understand Legitimate Cause
 │
 ▼
Identify Stable Context
 │
 ▼
Tune Detection
```

---

# Detection Tuning

Bad detection:

```text
PowerShell Execution
```

Better:

```text
Office
 +
PowerShell
 +
Rare Host/User Combination
 +
External Network
```

Better detections generally combine:

- Process
- Parent
- User
- Command line
- File
- Network
- Frequency
- Baseline

---

# Practical Lab 1 — PowerShell Parent-Child Hunting

## Objective

Identify unusual PowerShell execution originating from user-facing applications.

## Query Concept

```text
Process = powershell.exe
AND
Parent IN (
    winword.exe,
    excel.exe,
    outlook.exe
)
```

## Investigation

For every result collect:

```text
Timestamp
Host
User
Parent
Command Line
Hash
Network Connections
```

## Expected Outcome

Build a process tree:

```text
Application
    │
    ▼
PowerShell
    │
    ├── File
    ├── Network
    └── Persistence
```

---

# Practical Lab 2 — Rare Process Hunting

## Objective

Find uncommon processes across endpoints.

Conceptual workflow:

```text
Collect Process Events
        │
        ▼
Group By Process
        │
        ▼
Count Unique Hosts
        │
        ▼
Sort Ascending
        │
        ▼
Investigate Rare Processes
```

Example logic:

```text
Process
Host Count
Execution Count
User Count
First Seen
Last Seen
```

Investigate processes with unusually low prevalence.

---

# Practical Lab 3 — Suspicious Temporary File

## Objective

Investigate executable files created in temporary directories.

Search concept:

```text
File Created
AND
Path contains Temp
AND
Extension executable/script
```

Then correlate:

```text
File
  │
  ▼
Creating Process
  │
  ▼
User
  │
  ▼
Network
  │
  ▼
Persistence
```

---

# Practical Lab 4 — Security Control Tampering

## Objective

Detect suspicious modification of endpoint security controls.

Investigate:

```text
Security configuration change
        │
        ▼
Process responsible
        │
        ▼
User responsible
        │
        ▼
Authorization
        │
        ▼
Activity afterward
```

A security-control modification followed by suspicious execution deserves priority investigation.

---

# Practical Lab 5 — Cross-Host IOC Hunt

Given:

```text
SHA256 = <known-hash>
```

Search:

```text
All endpoints
All process events
All file events
All network events
```

Determine:

```text
First Seen
Last Seen
Affected Hosts
Affected Users
Execution Count
Associated Network
```

Then build the incident scope.

---

# Practical Lab 6 — Process-to-Network Hunt

Identify processes that establish unusual outbound connections.

Workflow:

```text
Process
   │
   ▼
Network Connection
   │
   ▼
Destination
   │
   ▼
Domain/IP Enrichment
   │
   ▼
Host Prevalence
   │
   ▼
User Context
```

Investigate uncommon combinations.

---

# ATT&CK Mapping

Useful endpoint hunting techniques include:

| Technique | Description |
|---|---|
| T1059 | Command and Scripting Interpreter |
| T1059.001 | PowerShell |
| T1059.003 | Windows Command Shell |
| T1053 | Scheduled Task/Job |
| T1053.005 | Scheduled Task |
| T1547 | Boot or Logon Autostart |
| T1547.001 | Registry Run Keys / Startup Folder |
| T1562.001 | Impair Defenses |
| T1055 | Process Injection |
| T1036 | Masquerading |
| T1105 | Ingress Tool Transfer |
| T1218 | System Binary Proxy Execution |
| T1082 | System Information Discovery |
| T1083 | File and Directory Discovery |
| T1057 | Process Discovery |
| T1049 | System Network Connections Discovery |

Always verify the appropriate ATT&CK technique and sub-technique when creating production documentation.

---

# EDR Hunting Checklist

## Process

- [ ] Process identified
- [ ] Parent identified
- [ ] Child processes reviewed
- [ ] Command line reviewed
- [ ] User identified
- [ ] Integrity/privilege reviewed
- [ ] Process path validated

## Files

- [ ] File path checked
- [ ] Hash collected
- [ ] Signature checked
- [ ] Prevalence checked
- [ ] Creation time checked
- [ ] Modification time checked

## Network

- [ ] Destination identified
- [ ] Domain checked
- [ ] IP checked
- [ ] Port checked
- [ ] DNS activity reviewed
- [ ] Process-to-network relationship established

## Identity

- [ ] User identified
- [ ] Logon reviewed
- [ ] Privileges checked
- [ ] Account legitimacy confirmed

## Persistence

- [ ] Scheduled tasks checked
- [ ] Services checked
- [ ] Registry checked
- [ ] Startup locations checked
- [ ] WMI checked
- [ ] Accounts checked

## Defense Evasion

- [ ] Security-control changes checked
- [ ] Logging changes checked
- [ ] Process injection considered
- [ ] Masquerading considered
- [ ] Telemetry gaps investigated

---

# Common EDR Hunting Mistakes

## 1. Searching Only for Malware Names

Attackers may use:

```text
legitimate tools
```

rather than malware with recognizable names.

---

## 2. Treating Every PowerShell Event as Malicious

PowerShell is a legitimate administration platform.

Context matters.

---

## 3. Ignoring Parent Processes

The parent process can reveal the execution origin.

---

## 4. Ignoring User Context

A process may be normal for one user and highly unusual for another.

---

## 5. Ignoring Network Activity

Endpoint process activity becomes significantly more useful when correlated with network telemetry.

---

## 6. Hunting Only IOCs

IOC hunting is useful but limited.

Modern hunting should include:

```text
IOC
+
Behavior
+
Identity
+
Process
+
Network
+
Timeline
```

---

# EDR Data Quality

A mature EDR deployment should answer:

```text
What executed?
Who executed it?
Where did it execute?
What launched it?
What did it access?
Where did it connect?
What happened afterward?
```

If the answer is:

```text
Unknown
```

for many events, the organization has a telemetry gap.

---

# Telemetry Gap Analysis

Example:

```text
Endpoint
   │
   ├── Process Telemetry      ✓
   ├── File Telemetry         ✓
   ├── Network Telemetry      ✓
   ├── User Context           ✓
   ├── Registry Telemetry     ✗
   └── Script Telemetry       ✗
```

This should become a security improvement item.

---

# EDR + SIEM Architecture

```text
                  ENDPOINTS
                     │
                     ▼
                    EDR
                     │
          ┌──────────┴──────────┐
          │                     │
          ▼                     ▼
      Detection             Telemetry
          │                     │
          └──────────┬──────────┘
                     ▼
                    SIEM
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
    Correlation   Hunting      Alerting
        │            │            │
        └────────────┼────────────┘
                     ▼
                    SOC
```

EDR provides endpoint depth.

SIEM provides broader organizational correlation.

---

# EDR + Identity Correlation

```text
Identity
   │
   ▼
Authentication
   │
   ▼
Endpoint
   │
   ▼
Process
   │
   ▼
Network
   │
   ▼
Cloud / Application
```

This allows detection of attacks that span multiple security layers.

---

# EDR + Threat Intelligence

Threat intelligence can enrich endpoint observations.

Example:

```text
Endpoint Domain
       │
       ▼
Threat Intelligence
       │
       ├── Reputation
       ├── Malware Family
       ├── Threat Actor
       ├── ATT&CK
       └── Historical Activity
```

But reputation should not replace investigation.

---

# EDR Hunt Maturity Model

## Level 1 — Reactive

```text
Alert
 ↓
Investigate
```

---

## Level 2 — IOC Hunting

```text
Hash
IP
Domain
 ↓
Search
```

---

## Level 3 — Behavioral Hunting

```text
Process
+
User
+
Network
+
Persistence
```

---

## Level 4 — Hypothesis-Driven Hunting

```text
Threat Intelligence
       ↓
Hypothesis
       ↓
Telemetry
       ↓
Hunt
       ↓
Detection
```

---

## Level 5 — Continuous Detection Engineering

```text
Threat Research
      ↓
Hunting
      ↓
Detection
      ↓
Automation
      ↓
Measurement
      ↓
Tuning
      ↓
New Hunt
```

---

# Professional EDR Investigation Template

```text
Incident ID:
Date/Time:

Host:
User:
IP Address:

Initial Detection:

Process:
Parent Process:
Command Line:

File:
Path:
SHA256:
Signer:

Network:
Destination:
Port:
Domain:

Authentication Context:

Persistence:

MITRE ATT&CK:

Affected Hosts:

Affected Users:

Timeline:

Evidence:

Assessment:

Containment:

Remediation:

Lessons Learned:

Detection Improvement:
```

---

# Interview Questions

## 1. What is EDR?

EDR is an endpoint security capability that collects endpoint telemetry and provides detection, investigation, threat hunting, and response functionality.

---

## 2. What is the difference between EPP and EDR?

EPP focuses primarily on prevention and protection.

EDR focuses on visibility, behavioral detection, investigation, hunting, and response.

---

## 3. Why is process-tree analysis important?

It establishes execution relationships and provides context about how a process started and what it subsequently launched.

---

## 4. Is PowerShell execution malicious?

No.

PowerShell is a legitimate administrative technology. Suspicion depends on context such as parent process, command line, user, destination, frequency, and subsequent behavior.

---

## 5. What is Living-off-the-Land?

It is the use or abuse of legitimate tools already present within an environment to perform malicious activity.

---

## 6. How would you investigate a suspicious process?

I would examine:

```text
Process
Parent
Children
Command Line
User
Path
Hash
Signature
Network
Files
Persistence
Timeline
```

---

## 7. How would you hunt for a compromised endpoint?

I would correlate:

```text
Authentication
+
Process
+
File
+
Network
+
Persistence
+
Threat Intelligence
```

and establish a timeline.

---

## 8. How do you distinguish legitimate administration from attacker activity?

I would evaluate:

- User
- Host
- Parent process
- Command line
- Timing
- Destination
- Frequency
- Baseline
- Authorization
- Change-management context

---

## 9. What is process injection?

Process injection is a class of techniques where code execution is introduced into the context of another process.

---

## 10. What is telemetry gap analysis?

It is the process of identifying missing or insufficient endpoint telemetry that prevents reliable investigation or detection.

---

## 11. Why is command-line telemetry important?

It provides execution context that a process name alone cannot provide.

---

## 12. What is behavioral detection?

Behavioral detection identifies suspicious combinations or sequences of activity rather than relying solely on known malware signatures or static indicators.

---

## 13. What is EDR telemetry?

It is endpoint-generated security data describing activity such as process creation, file operations, network connections, authentication, registry changes, and other security-relevant behavior.

---

## 14. How would you investigate a suspicious PowerShell process?

I would identify:

```text
Parent
User
Command Line
Host
Files
Network
Persistence
Prevalence
Timeline
```

Then correlate the activity with identity and other security telemetry.

---

## 15. How can a threat hunter improve an EDR detection?

A typical workflow is:

```text
Hunt
 ↓
Validate Behavior
 ↓
Identify Stable Pattern
 ↓
Write Detection
 ↓
Test
 ↓
Tune
 ↓
Deploy
 ↓
Measure
```

---

# Enterprise Best Practices

## 1. Collect High-Value Telemetry

Prioritize:

```text
Process
Command Line
Network
File
Authentication
Persistence
Security Control Changes
```

---

## 2. Correlate Multiple Signals

Avoid relying on one event.

Use:

```text
Process + User + Network + File + Timeline
```

---

## 3. Maintain Baselines

Know:

```text
Normal users
Normal hosts
Normal processes
Normal destinations
Normal administration
```

---

## 4. Track Telemetry Gaps

Document:

```text
Missing Logs
Missing Sensors
Unsupported Platforms
Disabled Logging
Coverage Gaps
```

---

## 5. Convert Successful Hunts into Detections

Repeated manual investigations should become repeatable detections where appropriate.

---

## 6. Measure Detection Quality

Useful metrics include:

```text
True Positive Rate
False Positive Rate
Mean Time to Detect
Mean Time to Investigate
Mean Time to Respond
Endpoint Coverage
Telemetry Coverage
Detection Coverage
```

---

## 7. Integrate EDR With the SOC

A mature architecture connects:

```text
EDR
SIEM
SOAR
Identity
Threat Intelligence
Network Security
Cloud Security
Email Security
```

---

# Final Threat-Hunting Workflow

A professional endpoint hunter should think like this:

```text
             THREAT INTELLIGENCE
                     │
                     ▼
                HYPOTHESIS
                     │
                     ▼
              ENDPOINT TELEMETRY
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
      Process       File        Network
        │            │            │
        └────────────┼────────────┘
                     ▼
                  Identity
                     │
                     ▼
                 Timeline
                     │
                     ▼
                 Correlation
                     │
                     ▼
                ATT&CK Mapping
                     │
                     ▼
                 Assessment
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Benign                Suspicious
          │                     │
          ▼                     ▼
       Close                Scope
                                │
                                ▼
                            Containment
                                │
                                ▼
                            Remediation
                                │
                                ▼
                           Detection
                           Engineering
                                │
                                ▼
                         Continuous Hunt
```

---

# Key Takeaways

The most important principles of EDR threat hunting are:

1. **Process names are not enough.**
2. **Parent-child relationships provide critical context.**
3. **Command lines can reveal attacker intent.**
4. **User identity must be correlated with endpoint activity.**
5. **Network connections should be tied back to processes.**
6. **Rare behavior is useful for prioritization but is not proof of compromise.**
7. **PowerShell and other administrative tools require contextual analysis.**
8. **EDR telemetry should be correlated with SIEM, identity, and threat intelligence data.**
9. **Telemetry gaps are security findings.**
10. **Successful hunts should feed detection engineering.**
11. **Attack timelines are more valuable than isolated alerts.**
12. **Behavioral correlation is generally stronger than IOC-only hunting.**

The fundamental mindset is:

> **Don't hunt for a malicious file. Hunt for suspicious behavior and reconstruct the story around it.**

---

# References

- MITRE ATT&CK — Enterprise Techniques  
  https://attack.mitre.org/

- Microsoft Defender XDR Documentation  
  https://learn.microsoft.com/en-us/defender-xdr/

- Microsoft Defender Advanced Hunting Documentation  
  https://learn.microsoft.com/en-us/defender-xdr/advanced-hunting-overview

- Microsoft Sysinternals  
  https://learn.microsoft.com/en-us/sysinternals/

- Microsoft Windows Security Auditing  
  https://learn.microsoft.com/en-us/windows/security/threat-protection/auditing/

- osquery Documentation  
  https://osquery.readthedocs.io/

- Velociraptor Documentation  
  https://docs.velociraptor.app/

- CrowdStrike Documentation  
  https://www.crowdstrike.com/

- SentinelOne Documentation  
  https://www.sentinelone.com/

- MITRE ATT&CK Data Sources  
  https://attack.mitre.org/datasources/

- CISA Cybersecurity Resources  
  https://www.cisa.gov/topics/cybersecurity
