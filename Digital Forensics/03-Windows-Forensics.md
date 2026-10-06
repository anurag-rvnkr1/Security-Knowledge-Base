# Windows Forensics

> **A practical enterprise guide to investigating Windows endpoints through Registry artifacts, Event Logs, PowerShell, Prefetch, Amcache, Shimcache, SRUM, LNK files, Jump Lists, browser artifacts, persistence mechanisms, NTFS metadata, authentication activity, and endpoint timelines.**

---

# Overview

Windows endpoints generate a large amount of forensic evidence.

A compromised Windows workstation may contain evidence of:

- User activity
- Authentication
- Process execution
- PowerShell activity
- File creation
- Program execution
- Persistence
- Network communication
- Browser activity
- Security-control activity
- Privilege changes
- Remote access

A useful Windows investigation correlates multiple artifact families rather than relying on a single artifact.

```text id="6x2lqz"
                    Windows Endpoint
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
      Event Logs        Registry          Files
        │                 │                 │
        ▼                 ▼                 ▼
    PowerShell         User Data         NTFS
        │                 │                 │
        └─────────────────┼─────────────────┘
                          ▼
                    Process Activity
                          │
                          ▼
                    Network Activity
                          │
                          ▼
                       Timeline
                          │
                          ▼
                      Findings
```

---

# Why Windows Forensics Matters

Windows remains one of the most common enterprise endpoint operating systems.

Organizations frequently rely on:

- Windows workstations
- Windows servers
- Active Directory
- PowerShell
- Microsoft Defender
- Microsoft 365
- Windows Event Forwarding
- Endpoint Detection and Response

Therefore, understanding Windows artifacts is essential for:

- SOC analysts
- Incident responders
- Threat hunters
- Digital forensic analysts
- Detection engineers
- Malware analysts

---

# Windows Forensic Investigation Model

```text id="f8zqps"
Alert
  │
  ▼
Identify Host
  │
  ▼
Identify User
  │
  ▼
Review Timeline
  │
  ▼
Analyze Processes
  │
  ▼
Analyze Files
  │
  ▼
Analyze Registry
  │
  ▼
Analyze Logs
  │
  ▼
Analyze Network
  │
  ▼
Correlate Evidence
```

---

# Important Windows Evidence Sources

| Evidence Source | What It Can Help Determine |
|---|---|
| Event Logs | Authentication, process, service, policy activity |
| Registry | Configuration, user activity, persistence |
| PowerShell Logs | Script execution |
| Prefetch | Program execution evidence |
| Amcache | Application execution/install-related evidence |
| Shimcache | Application compatibility/execution-related evidence |
| SRUM | Application and network usage |
| LNK | Files and paths accessed |
| Jump Lists | Application/file interaction |
| Browser | Web activity |
| Defender | Malware/security events |
| NTFS | File metadata |
| Scheduled Tasks | Persistence |
| Services | Persistence |
| User Profiles | User activity |
| EDR | Process and endpoint telemetry |

---

# Windows Event Logs

Windows Event Logs are among the most important sources of endpoint evidence.

Common logs include:

```text id="2xj8r4"
Security
System
Application
PowerShell
Windows Defender
Task Scheduler
Microsoft-Windows-Sysmon
```

---

# Security Event Log

The Security log can contain evidence related to:

- Logons
- Logoffs
- Account changes
- Privilege use
- Authentication failures
- Process creation when configured
- Object access when configured

---

# Authentication Investigation

A basic investigation may ask:

```text id="z3gk5h"
Who authenticated?
      │
      ▼
When?
      │
      ▼
From where?
      │
      ▼
To which system?
      │
      ▼
Using what authentication method?
```

---

# Useful Authentication Event Categories

Depending on audit configuration and Windows version, investigators commonly examine events such as:

```text id="z6t3yt"
4624 — Successful logon
4625 — Failed logon
4634 — Logoff
4647 — User-initiated logoff
4672 — Special privileges assigned
```

Event availability depends on audit policy and logging configuration.

---

# Successful Logon

Example:

```powershell id="f4l3iq"
Get-WinEvent -FilterHashtable @{
    LogName='Security'
    Id=4624
} -MaxEvents 20
```

Investigate:

- Account
- Logon type
- Source address
- Workstation
- Timestamp
- Authentication context

---

# Failed Authentication

```powershell id="y7z8ga"
Get-WinEvent -FilterHashtable @{
    LogName='Security'
    Id=4625
} -MaxEvents 20
```

Repeated failures may indicate:

- User error
- Misconfigured services
- Password spraying
- Brute-force activity
- Stale credentials

Do not automatically classify repeated failures as malicious.

---

# Logon Types

Common Windows logon types include:

| Type | General Meaning |
|---|---|
| 2 | Interactive |
| 3 | Network |
| 4 | Batch |
| 5 | Service |
| 7 | Unlock |
| 8 | Network cleartext credentials |
| 9 | New credentials |
| 10 | Remote Interactive |
| 11 | Cached Interactive |

Interpretation requires context.

---

# Process Creation

Process execution is central to endpoint forensics.

Useful telemetry may come from:

- Security auditing
- Sysmon
- EDR
- PowerShell logs
- Prefetch

A process investigation should consider:

```text id="v2v1xx"
Process
  │
  ├── Parent
  ├── User
  ├── Command Line
  ├── Path
  ├── Hash
  ├── Start Time
  └── Network Connections
```

---

# Sysmon

Sysmon can provide enhanced endpoint telemetry when appropriately configured.

Commonly useful event categories include:

```text id="13ezxh"
Process Creation
Network Connections
File Creation
Registry Activity
DNS Activity
Process Access
Image Loading
```

Configuration determines what is logged.

---

# PowerShell Forensics

PowerShell is a legitimate administrative tool and therefore requires behavioral analysis rather than simply treating PowerShell as malicious.

Important evidence sources may include:

- PowerShell operational logs
- Script Block Logging
- Module Logging
- Transcription
- EDR telemetry
- Process command lines

---

# PowerShell Script Block Logging

Where enabled, script-block telemetry can provide visibility into executed PowerShell content.

Investigators should correlate:

```text id="p0h55m"
PowerShell Event
      │
      ▼
Process Parent
      │
      ▼
User
      │
      ▼
Network
      │
      ▼
File Activity
```

---

# PowerShell Investigation

Example:

```powershell id="b8m8sx"
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -MaxEvents 50
```

Look for:

- Suspicious execution
- Encoded commands
- Unusual parent processes
- Downloads
- Network activity
- Script locations
- User context

Encoded PowerShell alone is not proof of malicious activity.

Context is required.

---

# Windows Registry

The Registry is a major forensic evidence source.

Conceptually:

```text id="8p6v0r"
Registry
   │
   ├── System Configuration
   ├── User Configuration
   ├── Software
   ├── Network
   ├── Services
   └── Persistence
```

---

# Major Registry Hives

Common hives include:

```text id="b4j8z3"
SYSTEM
SOFTWARE
SAM
SECURITY
NTUSER.DAT
USRCLASS.DAT
```

Each contains different categories of information.

---

# SYSTEM Hive

May contain evidence related to:

- Services
- Drivers
- Hardware
- Network configuration
- System configuration

---

# SOFTWARE Hive

May contain:

- Installed software
- Application configuration
- Windows configuration

---

# SAM Hive

Contains Windows account-related information.

Access to sensitive account databases must be handled carefully and only for authorized investigations.

---

# NTUSER.DAT

Per-user Registry hive.

It may contain evidence related to:

- User preferences
- Application activity
- Recent activity
- User-specific configuration

---

# USRCLASS.DAT

May contain additional per-user shell and application activity.

---

# Registry Persistence

Common persistence locations include areas associated with:

- Run keys
- Services
- Startup configuration
- Scheduled Tasks
- Application configuration

Investigators should correlate Registry findings with actual process and execution evidence.

---

# Registry Investigation Principle

A Registry key showing a program path does not automatically prove execution.

Use:

```text id="wj1w72"
Registry
   +
Execution Artifact
   +
Timeline
   +
Process Telemetry
```

to establish stronger conclusions.

---

# Prefetch

Windows Prefetch can provide useful execution-related evidence on systems where it is enabled and applicable.

It can help investigators determine:

- Program name
- Execution-related information
- Referenced files
- Timing information

---

# Prefetch Limitations

Prefetch is not a universal execution log.

Limitations can include:

- OS-specific behavior
- Configuration differences
- File-system behavior
- Retention limits
- Artifact modification

Therefore:

> Prefetch evidence should be correlated with other artifacts.

---

# Amcache

Amcache is a Windows forensic artifact that can provide information about applications and executable files.

It may assist with:

- Program inventory
- File paths
- Hash-related information
- Application execution/install context

Its exact forensic interpretation depends on Windows version and artifact state.

---

# Shimcache

Shimcache is associated with Windows application compatibility mechanisms.

It can provide useful historical evidence about executable paths and related compatibility data.

Important:

> Shimcache presence should not automatically be interpreted as proof that a program executed.

Correlate with other execution artifacts.

---

# SRUM

System Resource Usage Monitor provides historical information related to application and system resource usage.

It may assist investigations involving:

- Application usage
- Network activity
- User context
- Resource consumption

SRUM is particularly useful when reconstructing historical endpoint activity.

---

# LNK Files

Windows shortcut files can contain information about files and paths accessed through shortcuts.

Potential evidence includes:

- Target path
- Volume information
- Timestamps
- Machine-related information

LNK artifacts can help reconstruct user activity.

---

# Jump Lists

Jump Lists can provide evidence about files and resources associated with applications.

They can help answer:

> Which files were recently associated with a particular application?

They should be interpreted together with:

- File-system metadata
- User activity
- Application logs
- Other shell artifacts

---

# Browser Forensics

Browsers can contain highly valuable evidence.

Potential artifacts:

```text id="6o2jme"
History
Downloads
Cookies
Cache
Bookmarks
Sessions
Form Data
Saved Credentials
Extensions
```

---

# Browser Investigation Questions

```text id="v9g1yb"
Which site was accessed?
When?
From which user profile?
Was a file downloaded?
Where was it saved?
Was a suspicious URL visited?
Was authentication performed?
```

---

# Browser Download Investigation

Correlate:

```text id="p4f1du"
Browser History
      │
      ▼
Download Record
      │
      ▼
Downloaded File
      │
      ▼
File Metadata
      │
      ▼
Execution Evidence
```

This can reveal the relationship between browsing and endpoint activity.

---

# Windows Defender

Microsoft Defender telemetry can provide evidence related to:

- Malware detections
- Quarantine
- Remediation
- Threat names
- Detection times

Defender evidence should be correlated with endpoint telemetry.

---

# Windows Defender Investigation

Potential questions:

```text id="l0w3wv"
What was detected?
When?
Where?
Was it quarantined?
Was remediation successful?
Did the file execute?
Were other endpoints affected?
```

---

# Scheduled Tasks

Scheduled Tasks are legitimate Windows functionality but can also be abused for persistence.

Investigate:

- Task name
- Author
- Trigger
- Program
- Arguments
- User
- Creation/update time

Example:

```powershell id="3m6x5k"
Get-ScheduledTask
```

---

# Scheduled Task Investigation

```text id="6t0v7n"
Task
 │
 ├── Trigger
 ├── User
 ├── Program
 ├── Arguments
 ├── Creation
 └── Modification
```

Correlate task creation with:

- Registry
- File creation
- Process execution
- Authentication

---

# Windows Services

Services are another important persistence and execution mechanism.

Investigate:

```powershell id="v5b8h7"
Get-Service
```

For detailed service configuration:

```powershell id="l2f5p7"
Get-CimInstance Win32_Service
```

Look for:

- Service name
- Display name
- Binary path
- Start mode
- Account
- Creation/change evidence

---

# Startup Persistence

Investigate locations associated with:

- User startup
- System startup
- Run keys
- Startup folders
- Services
- Scheduled Tasks

A persistence finding should ideally be correlated with execution evidence.

---

# Windows File-System Forensics

Windows commonly uses NTFS.

Useful evidence can include:

- File names
- Paths
- Size
- Timestamps
- Permissions
- Alternate Data Streams
- File references
- Deleted-file metadata

---

# NTFS Metadata

Important concepts include:

```text id="d0w6jo"
MFT
File Records
Timestamps
Attributes
Security Descriptors
Alternate Data Streams
USN Journal
```

---

# Master File Table

The MFT contains records associated with files and directories.

Forensic analysis may provide:

- File names
- Paths
- Metadata
- Timestamps
- File references

The MFT is not simply a perfect historical record.

---

# USN Journal

The NTFS USN Journal can provide information about file-system changes.

It can assist with questions such as:

- Was a file created?
- Was a file renamed?
- Was a file deleted?
- Was a directory changed?

Retention and configuration affect what is available.

---

# Alternate Data Streams

NTFS supports alternate data streams.

Example conceptual structure:

```text id="h4e8sf"
file.txt
   │
   ├── Main Data Stream
   │
   └── Alternate Data Stream
```

Investigators may examine ADS when suspicious files or unusual file behavior are involved.

---

# Windows User Activity

Potential user-activity evidence includes:

- Logon/logoff
- Browser activity
- File access
- LNK files
- Jump Lists
- Recent files
- Application usage
- Shell activity

---

# User Investigation Model

```text id="xv2m1p"
User
 │
 ├── Authentication
 │
 ├── Interactive Session
 │
 ├── Application
 │
 ├── File
 │
 ├── Network
 │
 └── Cloud
```

---

# Remote Access Investigation

Windows systems may be accessed remotely using mechanisms such as:

- RDP
- SMB
- WinRM
- Remote management tools
- Administrative software

Investigate:

```text id="49l1zj"
Source
   │
   ▼
Authentication
   │
   ▼
Remote Session
   │
   ▼
Process Activity
   │
   ▼
Network Activity
```

---

# RDP Investigation

Potential evidence includes:

- Successful authentication
- Failed authentication
- Session events
- Source addresses
- User identity
- Session timing

RDP activity should be correlated with endpoint and network evidence.

---

# Windows Network Evidence

Investigate:

```text id="6d1u0x"
DNS
Connections
Firewall
Proxy
EDR
Browser
Application
```

Example:

```powershell id="9cl3iv"
Get-NetTCPConnection
```

---

# Suspicious Network Connection

A connection becomes more meaningful when correlated with:

```text id="p9v9ec"
Process
+
User
+
Destination
+
DNS
+
Timestamp
```

---

# Process Tree Analysis

One of the most important Windows forensic techniques is process-tree analysis.

Example:

```text id="8u0fzu"
winword.exe
    │
    └── powershell.exe
          │
          └── suspicious.exe
                 │
                 └── outbound connection
```

This does not automatically prove compromise, but it provides important behavioral context.

---

# Parent-Child Relationships

Investigate:

- Parent process
- Child process
- User
- Command line
- Execution path
- Integrity level
- Start time
- Network activity

---

# Command-Line Evidence

Command lines can reveal:

- Arguments
- Script paths
- Remote resources
- Execution context
- Administrative actions

Example:

```text id="09kz6r"
powershell.exe
    │
    └── Script / Command
             │
             ├── User
             ├── Parent
             └── Network
```

---

# Windows Persistence Investigation

A practical persistence review may include:

```text id="pjc3yi"
Registry
Scheduled Tasks
Services
Startup Folders
WMI
Browser Extensions
User Profile
Application Configuration
```

---

# WMI

Windows Management Instrumentation is widely used for administration and automation.

It can also be abused for persistence or execution.

Investigate suspicious:

- WMI event subscriptions
- Consumers
- Filters
- Providers
- Related processes

Because WMI is legitimate infrastructure, context is essential.

---

# WMI Investigation Principle

Do not assume:

> WMI = malicious.

Instead determine:

```text id="l1v0a7"
Who created it?
When?
What does it execute?
Under which account?
Was it expected?
Does telemetry show execution?
```

---

# Windows Evidence Correlation

A strong investigation may look like:

```text id="n7p7m2"
10:01
Suspicious Authentication
      │
      ▼
10:03
PowerShell Execution
      │
      ▼
10:04
File Created
      │
      ▼
10:05
Scheduled Task Created
      │
      ▼
10:07
External DNS Query
      │
      ▼
10:08
Outbound Connection
```

This produces a significantly stronger narrative than any individual artifact.

---

# Windows Timeline

A practical timeline might include:

| Time | Evidence | Interpretation |
|---|---|---|
| 10:01 | 4624 | Successful authentication |
| 10:03 | Process event | PowerShell execution |
| 10:04 | File artifact | New executable |
| 10:05 | Task artifact | Scheduled task created |
| 10:07 | DNS | External lookup |
| 10:08 | Network | Outbound connection |

---

# Timeline Caveats

A timestamp does not automatically prove causality.

For example:

```text id="vmm3h6"
Event A
10:01

Event B
10:02
```

does not necessarily mean Event A caused Event B.

Use multiple evidence sources and contextual analysis.

---

# Windows Forensic Workflow

```text id="xg50q6"
Identify Host
    │
    ▼
Identify User
    │
    ▼
Preserve Evidence
    │
    ▼
Collect Logs
    │
    ▼
Collect Registry
    │
    ▼
Analyze Processes
    │
    ▼
Analyze Persistence
    │
    ▼
Analyze Files
    │
    ▼
Analyze Network
    │
    ▼
Build Timeline
    │
    ▼
Correlate
    │
    ▼
Report
```

---

# Common Windows Forensic Misconfigurations

## Insufficient Security Logging

Important authentication events may be unavailable.

## No PowerShell Logging

Script execution visibility becomes limited.

## No Sysmon / Endpoint Telemetry

Process and network investigations become harder.

## Short Event Log Retention

Historical evidence disappears.

## Poor Time Synchronization

Timeline reconstruction becomes unreliable.

## No Centralized Logging

Evidence remains isolated on endpoints.

---

# Detection and Forensic Readiness

Windows forensic capability depends heavily on endpoint visibility.

Recommended telemetry may include:

```text id="x20v0r"
Security Logs
PowerShell Logs
Sysmon
EDR
Defender
DNS
Firewall
Proxy
Identity
```

Organizations should balance visibility with:

- Performance
- Privacy
- Storage
- Retention
- Detection quality

---

# Practical Lab 01 — Windows Event Investigation

## Scenario

A workstation generated a suspicious authentication alert.

Investigate:

```text id="o0s4x2"
4624
4625
4672
```

Questions:

1. Which account authenticated?
2. Was the authentication successful?
3. What was the logon type?
4. What was the source?
5. Was privileged access involved?

---

# Practical Lab 02 — PowerShell Investigation

Search the PowerShell operational log:

```powershell id="y3z6h1"
Get-WinEvent -LogName "Microsoft-Windows-PowerShell/Operational" -MaxEvents 100
```

Identify:

- Suspicious commands
- User
- Time
- Parent process if available elsewhere
- Related file activity
- Network activity

Then correlate with EDR or Sysmon if available.

---

# Practical Lab 03 — Process Tree Investigation

Given:

```text id="y3o8r1"
explorer.exe
    │
    └── winword.exe
          │
          └── powershell.exe
                │
                └── suspicious.exe
```

Determine:

- Which process started the chain?
- Which user owned it?
- What command line was used?
- What network connections followed?
- Which files were created?

---

# Practical Lab 04 — Persistence Investigation

Review:

```text id="b5b3qy"
Scheduled Tasks
Services
Run Keys
Startup Folders
WMI
```

For every suspicious item document:

```text id="h8y6ot"
Name
Path
User
Creation Time
Modification Time
Execution
Network
Expected / Unexpected
Confidence
```

---

# Practical Lab 05 — Browser-to-Execution Investigation

Scenario:

```text id="c6y4oe"
Browser
  │
  ▼
Suspicious URL
  │
  ▼
Download
  │
  ▼
File Creation
  │
  ▼
Execution
  │
  ▼
Network Connection
```

Determine:

- URL
- User
- Browser profile
- Downloaded file
- File hash
- Execution evidence
- Network destination

---

# Practical Lab 06 — Complete Windows Investigation

Investigate a simulated compromised workstation using:

```text id="v1w7r3"
Security Logs
PowerShell
Sysmon
Registry
Prefetch
Amcache
Browser
Scheduled Tasks
Services
Network
```

Construct:

```text id="r0y8m1"
Initial Access
     ↓
Execution
     ↓
Persistence
     ↓
Network
     ↓
Detection
```

Then document evidence confidence.

---

# Windows Forensic Collection Checklist

```text id="axm7yt"
[ ] Host identified
[ ] User identified
[ ] System time recorded
[ ] Security logs preserved
[ ] PowerShell logs preserved
[ ] Sysmon logs preserved
[ ] Defender logs preserved
[ ] Registry acquired
[ ] User profiles identified
[ ] Browser artifacts preserved
[ ] Prefetch collected
[ ] Amcache collected
[ ] Shimcache collected
[ ] SRUM considered
[ ] Scheduled Tasks reviewed
[ ] Services reviewed
[ ] Persistence reviewed
[ ] Network telemetry preserved
[ ] Evidence hashed
[ ] Timeline constructed
```

---

# Windows Investigation Report Template

```text id="g4d4kv"
# Windows Forensic Investigation

## Case Information

Case ID:
Host:
User:
Investigator:
Date:

## Scope

## Evidence Sources

## Acquisition

## Integrity

## Authentication Analysis

## Process Analysis

## PowerShell Analysis

## Registry Analysis

## Persistence Analysis

## File-System Analysis

## Browser Analysis

## Network Analysis

## Timeline

## Findings

## Evidence Correlation

## Evidence Gaps

## Confidence

## Conclusions

## Recommendations
```

---

# Example Finding

```text id="6z0c84"
Finding ID:
WIN-001

Title:
Suspicious PowerShell Execution

Observation:
PowerShell executed under USER01 shortly after an unusual interactive authentication event.

Evidence:
Security log
PowerShell telemetry
Process telemetry
DNS telemetry

Timeline:
10:31 — Authentication
10:33 — PowerShell
10:34 — DNS query
10:35 — External connection

Assessment:
The activity is consistent with possible post-authentication execution and requires further investigation.

Confidence:
High
```

---

# Windows Evidence Confidence

### High

Multiple independent artifacts correlate.

### Medium

Evidence supports the hypothesis but gaps remain.

### Low

Single artifact or ambiguous evidence.

Example:

```text id="m3x5u9"
Registry Run Key
      │
      ▼
Possible Persistence

Registry
+
Process Execution
+
Timeline
      │
      ▼
Stronger Persistence Finding
```

---

# Interview Questions

## 1. What Windows artifacts are important during forensic investigation?

Common examples include:

- Event Logs
- Registry
- PowerShell logs
- Prefetch
- Amcache
- Shimcache
- SRUM
- LNK files
- Jump Lists
- Browser artifacts
- NTFS metadata
- Scheduled Tasks
- Services
- Defender telemetry
- EDR telemetry

---

## 2. Does Prefetch prove execution?

Not by itself.

It can provide useful execution-related evidence, but it should be correlated with other artifacts.

---

## 3. Does Shimcache prove execution?

Not necessarily.

Shimcache is related to application compatibility information and should be interpreted carefully.

---

## 4. What is the Windows Registry useful for?

It can provide information about:

- System configuration
- User activity
- Installed software
- Services
- Persistence
- Network configuration
- Application settings

---

## 5. What is Amcache?

A Windows artifact that can provide application and executable-related information useful during forensic investigation.

---

## 6. What is SRUM?

System Resource Usage Monitor data that can provide historical information about application and resource usage.

---

## 7. Why is PowerShell important in Windows forensics?

PowerShell is widely used for legitimate administration but can also be used during attacks. Its telemetry can reveal scripts, commands, execution context, and associated activity.

---

## 8. What is Sysmon?

A Windows system-monitoring utility that can provide detailed telemetry about processes, network connections, files, Registry activity, DNS, and other system events depending on its configuration.

---

## 9. Why is process-tree analysis important?

Because parent-child relationships can reveal how a process was launched and provide behavioral context.

---

## 10. How would you investigate suspicious PowerShell?

Correlate:

```text id="u9n2zw"
PowerShell Logs
+
Parent Process
+
User
+
Command Line
+
Files
+
Network
+
Timeline
```

---

## 11. How would you investigate persistence?

Review:

```text id="z4v7p0"
Registry
Scheduled Tasks
Services
Startup
WMI
Applications
```

Then correlate persistence configuration with execution evidence.

---

## 12. How would you investigate suspicious RDP activity?

Review:

```text id="3l0h3j"
Authentication
Session Events
Source Address
User
Process Activity
Network
Timeline
```

---

## 13. What is an important limitation of Windows event logs?

Logging depends on audit configuration, retention, forwarding, system state, and available storage.

---

## 14. Why should Windows artifacts be correlated?

Because individual artifacts can be incomplete or ambiguous.

Correlation provides stronger evidence.

---

# Scenario Interview Question

### Scenario

> You find a suspicious executable in `C:\Users\User\Downloads`. What do you investigate?

A structured approach:

```text id="3s3o3n"
File
 │
 ├── Hash
 ├── Metadata
 ├── Creation Time
 ├── Origin
 ├── Browser Download
 ├── Execution
 ├── Parent Process
 ├── Persistence
 ├── User
 ├── Network
 └── Related Hosts
```

---

# Scenario Interview Question

### Scenario

> A scheduled task points to an unfamiliar executable. Does that prove persistence?

Not by itself.

Investigate:

- Task creation
- Task modification
- Executable existence
- File metadata
- Execution evidence
- User context
- Parent process
- Network activity
- Whether the task is legitimate

---

# Windows Forensic Maturity Model

## Level 1

Basic Event Logs.

## Level 2

Registry and endpoint artifacts.

## Level 3

Centralized logs + PowerShell + EDR.

## Level 4

Sysmon + EDR + SIEM + forensic workflows.

## Level 5

Enterprise endpoint telemetry + automated collection + integrated threat hunting and detection engineering.

---

# Chapter Completion Checklist

```text id="2v5m1p"
[ ] Understand Windows forensic architecture
[ ] Understand Event Logs
[ ] Understand authentication events
[ ] Understand process creation
[ ] Understand PowerShell
[ ] Understand Sysmon
[ ] Understand Registry hives
[ ] Understand Prefetch
[ ] Understand Amcache
[ ] Understand Shimcache
[ ] Understand SRUM
[ ] Understand LNK files
[ ] Understand Jump Lists
[ ] Understand browser artifacts
[ ] Understand Defender telemetry
[ ] Understand Scheduled Tasks
[ ] Understand Services
[ ] Understand WMI
[ ] Understand NTFS evidence
[ ] Understand USN Journal
[ ] Understand process trees
[ ] Understand Windows timelines
[ ] Complete Windows forensic labs
```

---

# Key Takeaways

Windows forensics is strongest when multiple artifact families are correlated.

A useful investigation model is:

```text id="4e5c8g"
Identity
   │
   ▼
Authentication
   │
   ▼
Process
   │
   ▼
File
   │
   ▼
Persistence
   │
   ▼
Network
   │
   ▼
Timeline
   │
   ▼
Finding
```

The investigator should avoid treating any single artifact as absolute proof.

Instead:

> **Correlate execution, identity, file-system, Registry, network, and timeline evidence to construct a defensible narrative.**

Windows forensics is therefore not simply about knowing where artifacts are stored.

It is about understanding **what each artifact can prove, what it cannot prove, how long it persists, what can modify it, and how it fits into the broader investigation**.

---

# References

### Microsoft — Windows Security Auditing

https://learn.microsoft.com/windows/security/threat-protection/auditing/

### Microsoft — Windows Event Logs

https://learn.microsoft.com/windows/win32/eventlog/event-logging

### Microsoft — Sysmon

https://learn.microsoft.com/sysinternals/downloads/sysmon

### Microsoft — PowerShell Logging

https://learn.microsoft.com/powershell/

### Microsoft — Windows Registry

https://learn.microsoft.com/windows/win32/sysinfo/registry

### Eric Zimmerman Tools

https://ericzimmerman.github.io/

### SANS Digital Forensics

https://www.sans.org/digital-forensics/

### NIST SP 800-86

https://csrc.nist.gov/publications/detail/sp/800-86/final

### MITRE ATT&CK

https://attack.mitre.org/

---

> **Windows forensics is the practice of turning endpoint artifacts into a defensible reconstruction of user activity, system activity, and potential attacker behavior.**
