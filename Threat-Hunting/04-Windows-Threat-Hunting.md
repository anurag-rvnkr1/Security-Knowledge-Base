# Windows Threat Hunting

## Overview

Windows is one of the most widely deployed operating systems in enterprise environments and therefore one of the most important platforms for threat hunters.

Attackers frequently target Windows because enterprise environments often contain:

- User identities
- Privileged accounts
- Active Directory
- Business applications
- Sensitive documents
- Credentials
- Administrative tools
- Remote management interfaces

A Windows threat hunter must understand both **normal Windows administration** and **attacker behavior**.

The objective is not to treat every unusual Windows event as malicious.

Instead, the hunter should identify combinations of events that form a suspicious behavioral pattern.

```text
Windows Endpoint
       │
       ├── Processes
       ├── Users
       ├── Authentication
       ├── Files
       ├── Registry
       ├── Services
       ├── Scheduled Tasks
       ├── PowerShell
       ├── Network Connections
       └── Security Events
              │
              ▼
        Security Telemetry
              │
              ▼
         Threat Hunting
              │
              ▼
          Investigation
              │
              ▼
          Detection
```

---

# Why Windows Threat Hunting Matters

A compromised Windows workstation may become the starting point for a much larger attack.

A typical attack path could look like:

```text
Phishing
   ↓
User Execution
   ↓
Initial Compromise
   ↓
PowerShell
   ↓
Credential Access
   ↓
Discovery
   ↓
Lateral Movement
   ↓
Privilege Escalation
   ↓
Persistence
   ↓
Data Collection
   ↓
Exfiltration / Impact
```

A threat hunter may not observe the initial compromise.

However, evidence of later activity may still be available.

This makes Windows telemetry extremely valuable for reconstructing attacker behavior.

---

# Windows Threat Hunting Architecture

A typical enterprise Windows hunting environment looks like:

```text
                 Windows Endpoints
                 /      |       \
                /       |        \
               ▼        ▼         ▼
         Event Logs   Sysmon      EDR
               \        |         /
                \       |        /
                 ▼      ▼        ▼
                    Log Pipeline
                         │
                         ▼
                        SIEM
                         │
                ┌────────┴────────┐
                ▼                 ▼
          Detection            Hunting
                │                 │
                └────────┬────────┘
                         ▼
                    Investigation
                         │
                         ▼
                  Incident Response
```

---

# Windows Telemetry

Threat hunting depends on telemetry.

Important Windows telemetry includes:

- Windows Security Event Logs
- System Event Logs
- Application Event Logs
- PowerShell logs
- Sysmon
- Microsoft Defender
- EDR telemetry
- Task Scheduler
- Service creation
- Registry activity
- Authentication events
- Active Directory events
- DNS
- Network connections

---

# Windows Event Logging

Windows Event Logs provide structured information about system activity.

Common log categories include:

```text
Application
Security
System
Setup
Forwarded Events
```

Additional channels can include:

```text
Microsoft-Windows-PowerShell/Operational
Microsoft-Windows-Sysmon/Operational
Microsoft-Windows-TaskScheduler/Operational
Microsoft-Windows-WMI-Activity/Operational
```

The exact channels available depend on the operating system and logging configuration.

---

# Windows Event Viewer

Windows Event Viewer can be used to inspect local logs.

Open:

```text
eventvwr.msc
```

Common navigation:

```text
Event Viewer
   └── Windows Logs
       ├── Application
       ├── Security
       ├── Setup
       └── System
```

For operational hunting, centralized collection is generally more scalable than manually inspecting individual endpoints.

---

# Important Windows Security Events

Several Windows Security Event IDs are particularly useful to hunters.

| Event ID | Description | Hunting Value |
|---|---|---|
| 4624 | Successful logon | Authentication analysis |
| 4625 | Failed logon | Brute force / password attacks |
| 4634 | Logoff | Session analysis |
| 4647 | User initiated logoff | Session analysis |
| 4672 | Special privileges assigned | Privileged activity |
| 4688 | Process creation | Process hunting |
| 4697 | Service installed | Persistence |
| 4698 | Scheduled task created | Persistence |
| 4720 | User account created | Account manipulation |
| 4728 | Member added to security-enabled global group | Privilege changes |
| 4732 | Member added to security-enabled local group | Privilege changes |
| 4740 | User account locked out | Authentication investigation |
| 4768 | Kerberos TGT requested | AD authentication |
| 4769 | Kerberos service ticket requested | Kerberos activity |
| 4771 | Kerberos pre-authentication failed | Authentication investigation |
| 4776 | Credential validation | Authentication investigation |

Event availability and field content depend on Windows auditing configuration.

---

# Event ID 4624 — Successful Logon

Event ID **4624** represents a successful account logon.

Useful fields may include:

- Account name
- Account domain
- Logon type
- Source network address
- Workstation name
- Authentication package
- Logon ID

---

# Windows Logon Types

Logon type provides important context.

Common types include:

| Logon Type | Meaning |
|---:|---|
| 2 | Interactive |
| 3 | Network |
| 4 | Batch |
| 5 | Service |
| 7 | Unlock |
| 8 | NetworkCleartext |
| 9 | NewCredentials |
| 10 | RemoteInteractive |
| 11 | CachedInteractive |

For threat hunting, combinations of:

```text
User
+
Logon Type
+
Source
+
Destination
+
Time
```

can be highly informative.

---

# Example: RDP Hunting

RDP commonly produces **Logon Type 10** events.

A basic hunting workflow:

```text
4624
  │
  ├── Logon Type = 10
  ├── User
  ├── Source IP
  ├── Destination Host
  └── Timestamp
          │
          ▼
     Investigation
```

Potential hunting leads:

- Unusual source host
- Rare administrator login
- Login outside normal hours
- Login followed by suspicious process execution
- Login from an unexpected network segment

RDP usage itself is not malicious.

Context matters.

---

# Event ID 4625 — Failed Logon

Event ID **4625** records a failed logon.

Repeated failures can indicate:

- Password spraying
- Brute force
- Credential guessing
- Misconfigured applications
- Expired credentials
- Legitimate user mistakes

A hunter should analyze:

```text
Account
Source
Destination
Time
Failure Reason
Frequency
```

---

# Password Spraying Hunt

A password spray often targets many accounts with relatively few attempts per account.

Conceptually:

```text
Attacker
   │
   ├── User A → Failed
   ├── User B → Failed
   ├── User C → Failed
   ├── User D → Failed
   └── User E → Failed
```

Compare this with brute force:

```text
Attacker
   │
   └── User A
        ├── Password 1
        ├── Password 2
        ├── Password 3
        └── Password 4
```

A hunter should look for patterns rather than simply counting failed logons.

---

# Event ID 4672 — Special Privileges

Event ID **4672** can indicate that special privileges were assigned to a new logon.

This can be useful for hunting privileged activity.

Investigate combinations such as:

```text
4624 Successful Logon
        +
4672 Special Privileges
        +
Unusual Source
```

The combination may deserve investigation.

---

# Event ID 4688 — Process Creation

Process creation is one of the most valuable Windows hunting events.

It can provide:

- New process
- Parent process
- Command line
- User
- Process ID
- Timestamp

Conceptually:

```text
Parent Process
      │
      ▼
Child Process
      │
      ▼
Command Line
      │
      ▼
Network / File Activity
```

This allows hunters to reconstruct process execution chains.

---

# Process Trees

A process tree shows parent-child relationships.

Example:

```text
explorer.exe
    │
    └── powershell.exe
          │
          └── cmd.exe
                │
                └── suspicious.exe
```

The individual processes may be legitimate.

The relationship may be suspicious.

This is why **process context** is more useful than simply searching for filenames.

---

# Parent-Child Process Analysis

Consider:

```text
winword.exe
    └── powershell.exe
```

This may deserve investigation because Office applications do not normally need to launch PowerShell in many user workflows.

Compare:

```text
services.exe
    └── svchost.exe
```

This is normal Windows behavior in many environments.

Threat hunting therefore requires understanding normal process relationships.

---

# Living Off the Land

Attackers frequently use legitimate Windows tools rather than dropping custom malware.

Examples include:

- PowerShell
- cmd.exe
- rundll32.exe
- regsvr32.exe
- mshta.exe
- wscript.exe
- cscript.exe
- certutil.exe
- bitsadmin.exe
- schtasks.exe
- sc.exe
- net.exe

These are often called **Living-off-the-Land** techniques.

Important:

> A legitimate tool is not inherently malicious.

The hunter should analyze:

```text
Tool
+
User
+
Parent
+
Arguments
+
Target
+
Time
+
Network
```

---

# PowerShell Threat Hunting

PowerShell is extremely important in Windows threat hunting.

It can be used for:

- Administration
- Automation
- Configuration
- Security management
- Software deployment
- Offensive operations

Useful telemetry may include:

- Process creation
- PowerShell Operational logs
- Script Block Logging
- Module Logging
- Transcription
- EDR telemetry

---

# PowerShell Event Logging

Relevant PowerShell telemetry can include:

```text
Windows PowerShell Operational
```

and, where configured:

- Script Block Logging
- Module Logging
- Transcription

Security teams should configure logging according to their organization's requirements, privacy considerations, and performance constraints.

---

# Suspicious PowerShell Indicators

Potential hunting signals include:

```text
Encoded commands
     +
Unusual parent process
     +
Rare user
     +
External connection
     +
Unexpected privilege level
```

Other useful context:

- `-EncodedCommand`
- Hidden execution
- Unusual download behavior
- Unusual child processes
- Commands executed by service accounts
- PowerShell launched from unexpected applications

None of these alone proves malicious activity.

---

# Example PowerShell Process

```text
WINWORD.EXE
    │
    └── powershell.exe
          │
          ├── command execution
          └── outbound connection
```

Possible investigation:

```text
Office Document
      ↓
PowerShell
      ↓
Command
      ↓
Network Connection
      ↓
Downloaded File
      ↓
Execution
```

This sequence can provide stronger evidence than any single event.

---

# Sysmon

**Sysmon**, part of Microsoft's Sysinternals suite, provides detailed system telemetry useful for security monitoring and hunting.

Depending on configuration, Sysmon can provide information about:

- Process creation
- Network connections
- File creation
- Registry changes
- Process access
- DNS queries
- Image loading
- Driver activity

Sysmon configuration should be designed carefully to balance visibility, performance, storage, and noise.

---

# Useful Sysmon Events

Commonly useful event IDs include:

| Sysmon Event | Description |
|---:|---|
| 1 | Process Create |
| 3 | Network Connection |
| 7 | Image Loaded |
| 8 | CreateRemoteThread |
| 10 | Process Access |
| 11 | File Create |
| 12 | Registry Event |
| 13 | Registry Value Set |
| 22 | DNS Query |
| 23 | File Delete |
| 25 | Process Tampering |

Sysmon event availability depends on the Sysmon version and configuration.

---

# Sysmon Process Hunting

A useful process investigation includes:

```text
Image
Command Line
Parent Image
Parent Command Line
User
Integrity Level
Hashes
Timestamp
Host
```

Example:

```text
powershell.exe
     │
     ├── Parent: winword.exe
     ├── User: employee
     ├── Integrity: Medium
     ├── Command: suspicious parameters
     └── Network: external destination
```

This gives the hunter significantly more context.

---

# Process Injection

Process injection involves manipulating another process to execute code or alter behavior.

Potential telemetry may include:

- Process access
- Remote thread creation
- Memory-related behavior
- EDR detections
- Unusual process relationships

Example:

```text
Process A
    │
    └── accesses Process B
             │
             └── suspicious execution
```

This behavior can be mapped to relevant MITRE ATT&CK techniques.

---

# Registry Hunting

The Windows Registry contains configuration and operational information.

Attackers may abuse registry locations for:

- Persistence
- Configuration changes
- Execution
- Defense evasion

Common persistence locations include Run and RunOnce keys.

Example:

```text
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
```

and:

```text
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
```

A registry modification is not automatically malicious.

Investigate:

```text
Who changed it?
What changed?
When?
What executable was referenced?
Is the executable legitimate?
```

---

# Scheduled Task Hunting

Scheduled tasks can be used legitimately for automation and administration.

They can also provide persistence.

Useful events may include:

```text
4698
Scheduled task created
```

Potential hunting logic:

```text
New Scheduled Task
       ↓
Unusual User
       ↓
Unusual Command
       ↓
Unusual Trigger
       ↓
Suspicious Binary
```

---

# Service Creation Hunting

Windows services are another persistence and execution mechanism.

Relevant event:

```text
4697
A service was installed
```

Investigation:

```text
Service Created
      ↓
Service Name
      ↓
Image Path
      ↓
Account
      ↓
Creator
      ↓
Timestamp
```

Look for:

- Unusual service names
- Unexpected executable paths
- User-writable locations
- Recently created services
- Service creation followed by network activity

---

# WMI Threat Hunting

**Windows Management Instrumentation (WMI)** is widely used for legitimate administration.

It can also be abused for:

- Execution
- Discovery
- Persistence
- Remote administration

Potential telemetry includes:

- WMI operational logs
- Process creation
- EDR
- Network activity

Example:

```text
Remote Host
     ↓
WMI
     ↓
Process Creation
     ↓
Command Execution
```

WMI activity should be evaluated against normal administrative behavior.

---

# Windows Authentication Hunting

Authentication telemetry is essential.

Investigate:

```text
Successful Logons
Failed Logons
Remote Logons
Service Logons
Privileged Logons
Kerberos Activity
NTLM Activity
Account Changes
```

Correlate identity activity with endpoint behavior.

---

# Authentication Correlation

Example:

```text
4624 Successful Logon
       ↓
4624 Remote Logon
       ↓
4688 Process Creation
       ↓
Network Connection
       ↓
Sensitive File Access
```

The sequence provides more context than an isolated login.

---

# Active Directory Hunting

Active Directory is a major enterprise identity system.

Threat hunters should monitor:

- User creation
- Group membership changes
- Privileged group changes
- Kerberos activity
- Authentication failures
- Service accounts
- Domain controllers
- Trust relationships
- Replication-related activity

---

# Privileged Group Hunting

Monitor changes involving sensitive groups such as:

- Domain Admins
- Enterprise Admins
- Administrators
- Other organization-defined privileged groups

Example:

```text
User Added
    ↓
Privileged Group
    ↓
Unexpected Actor
    ↓
Unexpected Time
```

This may warrant investigation.

---

# Account Creation Hunting

Event ID **4720** represents a user account creation event.

Potential hunting signals:

```text
New Account
   +
Unexpected Creator
   +
Privileged Group
   +
Unusual Naming
```

However, service accounts and onboarding processes can generate legitimate account creation events.

Always validate against business context.

---

# Credential Access Hunting

Credential access may involve:

- Credential dumping
- Password stores
- Browser credentials
- Kerberos abuse
- LSASS-related activity
- Credential files
- Token manipulation

Potential telemetry:

```text
Process
+
Process Access
+
Authentication
+
Privilege
+
EDR
```

---

# LSASS Monitoring

The Local Security Authority Subsystem Service (**LSASS**) is a sensitive Windows process involved in authentication and security policy.

Hunters may investigate suspicious access to LSASS.

Potential telemetry includes:

- Sysmon Process Access
- EDR
- Windows security telemetry
- Process relationships

A suspicious process accessing LSASS should be investigated carefully.

---

# Discovery Hunting

After obtaining access, attackers often perform discovery.

Common targets:

```text
System
Users
Processes
Services
Network
Shares
Domain
Groups
Applications
Security Products
```

Examples of commands that may appear in legitimate administration include:

```text
whoami
hostname
ipconfig
systeminfo
tasklist
net user
net group
net use
```

These commands are not inherently malicious.

The surrounding context matters.

---

# Discovery Correlation

A stronger signal can emerge from sequence:

```text
whoami
   ↓
systeminfo
   ↓
ipconfig
   ↓
net user
   ↓
net group
   ↓
network enumeration
```

Rapid execution of multiple discovery commands by an unusual account may warrant investigation.

---

# Windows Network Hunting

Endpoint network telemetry can reveal:

- Outbound connections
- Internal connections
- Destination IPs
- Destination ports
- Processes responsible
- DNS queries
- Connection timing

Example:

```text
Process
   ↓
Destination
   ↓
Port
   ↓
DNS
   ↓
Firewall
```

Correlating process and network telemetry is particularly valuable.

---

# Process-to-Network Correlation

Suppose:

```text
powershell.exe
      ↓
External IP
      ↓
443
```

This is not automatically malicious.

Investigate:

```text
Who launched PowerShell?
What command executed?
What is the destination?
Was it expected?
What happened afterward?
```

Context determines the risk.

---

# Windows Persistence Hunting

Common persistence mechanisms include:

```text
Registry Run Keys
Scheduled Tasks
Services
Startup Items
WMI
User Accounts
Logon Scripts
```

Hunt for:

```text
New Persistence
     ↓
Unexpected User
     ↓
Unexpected Location
     ↓
Suspicious Binary
```

---

# Windows Defense Evasion

Attackers may attempt to reduce visibility.

Potential behaviors include:

- Clearing logs
- Disabling security tools
- Deleting files
- Tampering with processes
- Obfuscating commands
- Modifying security settings

For example:

```text
Suspicious Activity
       ↓
Security Control Modified
       ↓
Telemetry Gap
```

A sudden reduction in telemetry itself can be a hunting signal.

---

# Event Log Clearing

A suspicious event log clearing operation can be investigated through Windows Security logging.

Event ID **1102** can indicate that the Security audit log was cleared.

Investigation:

```text
1102
 ↓
User
 ↓
Host
 ↓
Time
 ↓
Events Before Clearing
 ↓
Events After Clearing
```

The surrounding timeline is often more valuable than the clearing event alone.

---

# Windows Timeline Reconstruction

One of the most important threat-hunting skills is building timelines.

Example:

```text
08:41
User Login
   ↓
08:43
Office Application Started
   ↓
08:44
PowerShell Spawned
   ↓
08:45
External Network Connection
   ↓
08:47
Credential Access Activity
   ↓
08:50
Remote Authentication
   ↓
08:52
New Scheduled Task
```

Individually:

```text
Normal / Ambiguous
```

Together:

```text
Potential Attack Chain
```

---

# Process Investigation Methodology

For a suspicious process:

```text
1. Identify Process
        ↓
2. Identify User
        ↓
3. Identify Parent
        ↓
4. Inspect Command Line
        ↓
5. Inspect File Path
        ↓
6. Check Hash / Reputation
        ↓
7. Check Network Activity
        ↓
8. Check Child Processes
        ↓
9. Check Persistence
        ↓
10. Build Timeline
```

---

# Windows Hunt Hypothesis

## Hypothesis

> An attacker who gains access to a Windows endpoint may use PowerShell to execute commands and then perform discovery before attempting lateral movement.

### ATT&CK Context

Potential techniques may include:

```text
Command and Scripting Interpreter
        ↓
PowerShell

System Information Discovery

Account Discovery

Network Service Scanning

Remote Services
```

### Required Telemetry

```text
Windows Security Logs
Sysmon
PowerShell Logs
EDR
DNS
Authentication
Network Logs
```

---

# Hunt Workflow

```text
PowerShell Events
       ↓
Identify Users
       ↓
Identify Hosts
       ↓
Analyze Parent Processes
       ↓
Inspect Commands
       ↓
Correlate Network Activity
       ↓
Check Authentication
       ↓
Check Discovery Commands
       ↓
Check Lateral Movement
       ↓
Build Timeline
```

---

# Example Hunting Logic

Conceptually:

```text
IF

PowerShell execution

AND

unusual parent process

AND

unusual command line

AND

external network connection

THEN

Investigate
```

The exact implementation depends on the SIEM, EDR, logging schema, and environment.

---

# Windows Hunt Data Model

A useful normalized event model:

```text
Timestamp
Host
User
Process
Parent Process
Command Line
Event ID
Source IP
Destination IP
Destination Port
File
Registry Key
Authentication Type
Integrity Level
Logon ID
```

Normalization makes cross-source correlation easier.

---

# Windows Threat Hunting with SIEM

A SIEM can correlate Windows telemetry.

Conceptually:

```text
Windows Events
      +
Sysmon
      +
EDR
      +
AD
      +
DNS
      ↓
     SIEM
      ↓
Correlation
      ↓
Threat Hunt
```

---

# Generic Hunting Query

A conceptual query:

```text
SELECT
    user,
    host,
    process,
    parent_process,
    command_line,
    timestamp
FROM process_events
WHERE process = 'powershell.exe'
ORDER BY timestamp DESC;
```

The actual syntax varies by platform.

---

# Example: Suspicious Parent Process

Conceptual query:

```text
Find PowerShell events
WHERE parent process is unusual
AND command line is suspicious
AND external network activity exists
```

This illustrates the logic rather than prescribing a universal production rule.

---

# Example: Failed Authentication

Conceptual query:

```text
Find authentication failures
GROUP BY source IP, username
OVER a defined time window
WHERE failure volume or account spread
exceeds the organization's baseline
```

This can help identify:

- Password spraying
- Brute force
- Misconfiguration
- User error

Further investigation is required.

---

# Windows Threat Hunting With EDR

EDR platforms provide rich endpoint telemetry.

A typical investigation:

```text
Alert / Hunt Lead
       ↓
Host
       ↓
Process Tree
       ↓
User
       ↓
Command Line
       ↓
File
       ↓
Network
       ↓
Timeline
```

EDR is particularly useful for endpoint behavior that traditional Windows logs may not capture in sufficient detail.

---

# Endpoint Investigation Questions

For every suspicious Windows event, ask:

### Identity

- Which user?
- Is the user privileged?
- Is the account expected?

### Process

- Which process?
- Which parent?
- Which child processes?
- What command line?

### File

- Where is the executable?
- Is the path expected?
- Is the file signed?
- Is the hash known?

### Network

- What destination?
- Which port?
- Is the destination expected?
- Was DNS involved?

### Persistence

- Was a task created?
- Was a service installed?
- Was the registry modified?

### Timeline

- What happened before?
- What happened afterward?

---

# Common Windows Hunting Misconfigurations

Threat hunting becomes difficult when telemetry is incomplete.

Common issues include:

- Process creation auditing disabled
- Command-line logging unavailable
- PowerShell logging incomplete
- Sysmon absent
- EDR coverage gaps
- Security logs not centralized
- Insufficient retention
- Poor clock synchronization
- Missing DNS telemetry
- Inconsistent audit policies
- Excessive log filtering

---

# Telemetry Gap Example

Suppose the hunter wants to investigate:

```text
Suspicious PowerShell
```

But only has:

```text
4624 Authentication
```

The investigation may be severely limited.

Required telemetry could include:

```text
Process Creation
+
Command Line
+
PowerShell Logs
+
Network
```

Therefore:

> **A failed hunt does not always mean the threat was absent. It may mean the organization could not observe the behavior.**

---

# Windows Hunting Best Practices

- Centralize security logs.
- Enable appropriate auditing.
- Collect process creation telemetry.
- Collect command-line information where appropriate.
- Deploy endpoint telemetry strategically.
- Monitor PowerShell activity.
- Monitor privileged authentication.
- Correlate identity and endpoint activity.
- Track scheduled task and service creation.
- Monitor persistence locations.
- Maintain adequate retention.
- Synchronize system time.
- Establish normal behavioral baselines.
- Avoid treating legitimate tools as inherently malicious.
- Investigate behavior in context.
- Document telemetry gaps.

---

# Practical Lab 1 — Windows Authentication Hunting

## Scenario

An organization suspects password spraying against employee accounts.

### Data

```text
Windows Security Events
VPN Logs
Active Directory
```

### Objective

Identify suspicious authentication patterns.

### Investigate

```text
4625
 ↓
Source IP
 ↓
Number of Users
 ↓
Failure Frequency
 ↓
Successful Logons
```

### Questions

1. How many accounts were targeted?
2. Did one source target multiple users?
3. Were any successful logons observed?
4. Were privileged accounts targeted?
5. Did successful authentication lead to additional activity?

---

# Practical Lab 2 — PowerShell Hunting

## Scenario

A workstation may have been compromised.

### Data

```text
4688
PowerShell Logs
Sysmon
EDR
DNS
```

### Hypothesis

> An attacker may have used PowerShell to execute commands and establish external communication.

### Investigate

```text
PowerShell
 ↓
Parent Process
 ↓
Command Line
 ↓
User
 ↓
Network
 ↓
DNS
 ↓
Child Processes
```

### Deliverable

Produce:

```text
Timeline
Evidence
ATT&CK Mapping
Conclusion
Detection Recommendation
```

---

# Practical Lab 3 — Persistence Hunting

## Scenario

A compromised endpoint may contain attacker persistence.

### Investigate

```text
Registry
Scheduled Tasks
Services
WMI
Startup Locations
Accounts
```

### Hunt

Look for:

```text
Recently Created
+
Unexpected User
+
Unexpected Binary
+
Suspicious Path
```

---

# Practical Lab 4 — Lateral Movement Hunting

## Scenario

An employee workstation may have been used to access other systems.

### Data

```text
Authentication Logs
EDR
Active Directory
Network Logs
```

### Investigation

```text
Source Host
    ↓
User
    ↓
Destination Host
    ↓
Authentication
    ↓
Process
    ↓
Network
```

### Goal

Determine whether the activity represents normal administration or possible lateral movement.

---

# Practical Lab 5 — Full Windows Attack Timeline

Build a timeline from:

```text
Authentication
      ↓
Process Creation
      ↓
PowerShell
      ↓
Discovery
      ↓
Credential Access
      ↓
Lateral Movement
      ↓
Persistence
```

Document:

- Timestamp
- User
- Host
- Event
- Evidence
- ATT&CK technique
- Analyst interpretation

---

# Windows Hunt Report Template

```markdown
# Windows Threat Hunt Report

## Hunt Name

## Analyst

## Date

## Threat Scenario

## Hunt Hypothesis

## MITRE ATT&CK Mapping

## Data Sources

## Telemetry Coverage

## Hunt Methodology

## Queries

## Findings

## Investigation Timeline

## Process Analysis

## Authentication Analysis

## Network Analysis

## Persistence Analysis

## Evidence

## False Positives

## Conclusion

## Detection Opportunity

## Telemetry Gaps

## Recommendations

## Lessons Learned

## References
```

---

# MITRE ATT&CK Mapping

Windows threat hunting commonly intersects with techniques such as:

```text
Execution
├── Command and Scripting Interpreter
│   └── PowerShell
│
├── Windows Command Shell
│
└── Windows Management Instrumentation

Persistence
├── Scheduled Task/Job
├── Windows Service
└── Registry Run Keys / Startup Folder

Privilege Escalation
├── Exploitation
├── Token-related abuse
└── Valid Accounts

Credential Access
├── OS Credential Dumping
├── Credentials from Password Stores
└── Input Capture

Discovery
├── System Information Discovery
├── Account Discovery
├── Process Discovery
└── Network Service Scanning

Lateral Movement
├── Remote Services
├── SMB/Windows Admin Shares
└── Remote Desktop Protocol
```

The exact ATT&CK technique and sub-technique should always be verified against the current ATT&CK knowledge base when documenting a specific detection.

---

# Windows Hunting Checklist

## Telemetry

```text
[ ] Security Logs
[ ] Sysmon
[ ] PowerShell
[ ] EDR
[ ] DNS
[ ] Authentication
[ ] Active Directory
[ ] Network
```

## Process

```text
[ ] Process
[ ] Parent
[ ] Child
[ ] Command Line
[ ] User
[ ] Integrity
[ ] Path
```

## Identity

```text
[ ] Account
[ ] Privilege
[ ] Logon Type
[ ] Source
[ ] Destination
[ ] Authentication
```

## Persistence

```text
[ ] Services
[ ] Scheduled Tasks
[ ] Registry
[ ] Startup
[ ] WMI
[ ] Accounts
```

## Network

```text
[ ] DNS
[ ] Destination
[ ] Port
[ ] Process
[ ] Frequency
```

## Investigation

```text
[ ] Timeline
[ ] Correlation
[ ] Baseline
[ ] Evidence
[ ] False Positives
[ ] ATT&CK Mapping
```

---

# Common Windows Hunting Mistakes

## Searching Only for Malware

Attackers can use legitimate tools.

Better:

```text
Behavior
+
Context
+
Correlation
```

---

## Treating PowerShell as Malicious

PowerShell is a legitimate administrative technology.

Focus on:

```text
Parent
Command
User
Destination
Timing
Context
```

---

## Looking at Individual Events

A single event may be meaningless.

Correlate:

```text
Authentication
+
Process
+
Network
+
File
+
Persistence
```

---

## Ignoring Normal Administrative Activity

Administrators routinely perform actions that resemble attacker behavior.

Build baselines for:

- Admin accounts
- Service accounts
- Management servers
- Deployment systems
- Backup infrastructure

---

## Ignoring Telemetry Gaps

If the necessary logs do not exist, document the limitation rather than assuming nothing happened.

---

# Windows Threat Hunting Maturity

A useful progression:

```text
Level 1
Basic Event Review
        ↓
Level 2
Centralized Windows Logging
        ↓
Level 3
Sysmon / EDR Telemetry
        ↓
Level 4
Behavior-Based Hunting
        ↓
Level 5
ATT&CK-Mapped Detection Engineering
        ↓
Level 6
Continuous Threat-Informed Hunting
```

---

# Interview Questions

## Beginner

### What is Windows threat hunting?

Windows threat hunting is the proactive investigation of Windows telemetry to identify suspicious or malicious activity that may not have generated an existing security alert.

---

### What is Windows Event Viewer?

Event Viewer is a Windows administrative tool used to view event logs generated by the operating system and applications.

---

### What is Event ID 4624?

It represents a successful logon.

---

### What is Event ID 4625?

It represents a failed logon.

---

### What is Event ID 4688?

It represents a process creation event when appropriate auditing is configured.

---

### What is Sysmon?

Sysmon is a Microsoft Sysinternals system monitoring tool that provides detailed telemetry useful for security monitoring and threat hunting.

---

## Intermediate

### Why is process-tree analysis important?

It provides parent-child context that helps distinguish expected administrative activity from suspicious process execution.

---

### How would you investigate suspicious PowerShell?

I would examine:

```text
User
Host
Parent Process
Command Line
PowerShell Telemetry
Network Connections
Child Processes
Timeline
```

Then correlate the behavior with authentication and other endpoint events.

---

### How would you hunt password spraying?

I would analyze failed authentication events across multiple accounts and identify common source infrastructure, timing patterns, account spread, and any successful authentication that follows.

---

### Why is Event ID 4624 alone insufficient?

A successful logon is normal in most environments. The source, destination, user, logon type, timing, and subsequent activity provide the context needed to determine whether it is suspicious.

---

## Advanced

### How would you reconstruct a Windows attack?

```text
Authentication
      ↓
Process Creation
      ↓
Execution
      ↓
Credential Access
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Persistence
      ↓
Collection / Impact
```

I would correlate Windows Security events, Sysmon, EDR, authentication, DNS, network telemetry, and Active Directory events into a unified timeline.

---

### How can you identify a compromised account?

Look for combinations such as:

```text
Unusual Source
+
Unusual Device
+
Unusual Login Time
+
Privileged Access
+
New Destination
+
Suspicious Post-Login Activity
```

No single indicator should automatically prove compromise.

---

### How would you hunt Living-off-the-Land activity?

I would focus on legitimate administrative binaries being used in unusual contexts.

For example:

```text
Tool
+
Rare Parent
+
Unusual User
+
Suspicious Arguments
+
Unexpected Network Activity
```

---

### How would you detect telemetry gaps?

Map hunting requirements to available data sources:

```text
Threat Behavior
      ↓
Required Telemetry
      ↓
Telemetry Available?
      │
   ┌──┴──┐
  Yes    No
   │      │
   ▼      ▼
 Hunt   Visibility Gap
```

---

# Professional Windows Threat Hunting Workflow

```text
                   Threat Intelligence
                           │
                           ▼
                    Hunt Hypothesis
                           │
                           ▼
                   Windows Telemetry
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
   Event Logs            Sysmon              EDR
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                      SIEM / Data Lake
                           │
                           ▼
                    Behavioral Hunt
                           │
                           ▼
                     Correlation
                           │
                           ▼
                       Timeline
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                  Benign       Suspicious
                                  │
                                  ▼
                             Investigation
                                  │
                         ┌────────┴────────┐
                         ▼                 ▼
                    Incident           Detection
                    Response           Engineering
```

---

# Chapter Summary

Windows threat hunting requires more than memorizing Event IDs.

The core skill is understanding how different telemetry sources combine to tell an attack story.

The most important relationship is:

```text
Identity
   +
Process
   +
Command Line
   +
File
   +
Registry
   +
Network
   +
Persistence
   +
Timeline
```

A single event may be harmless.

A sequence of related events can reveal an attack.

```text
Login
  ↓
PowerShell
  ↓
Discovery
  ↓
Credential Access
  ↓
Remote Authentication
  ↓
Persistence
```

This is the fundamental mindset of endpoint threat hunting.

The strongest Windows hunters therefore ask:

> **What happened?**

Then:

> **Who performed it?**

Then:

> **What process caused it?**

Then:

> **What did that process do?**

Then:

> **What happened before and after it?**

Finally:

> **Does the complete timeline represent legitimate activity or adversary behavior?**

---

# Key Takeaways

```text
01. Windows telemetry is foundational for enterprise threat hunting.

02. Security Event Logs provide identity and authentication context.

03. Event ID 4688 is highly valuable for process hunting when configured.

04. Sysmon can significantly increase endpoint visibility.

05. Process trees are more useful than isolated process names.

06. PowerShell should be hunted based on context, not treated as inherently malicious.

07. Authentication, process, network, and persistence telemetry should be correlated.

08. Active Directory telemetry is critical for identity and lateral-movement hunting.

09. Attack timelines are often more informative than individual events.

10. Telemetry gaps must be treated as security visibility gaps.

11. ATT&CK mapping helps organize Windows hunting and detection coverage.

12. Successful hunts should feed detection engineering and incident response.
```

---

# References

## Microsoft

- Microsoft Windows Security Auditing — https://learn.microsoft.com/windows/security/threat-protection/auditing/
- Windows Security Event Auditing — https://learn.microsoft.com/windows/security/threat-protection/auditing/basic-audit-logon-events
- Microsoft Sysinternals — https://learn.microsoft.com/sysinternals/
- Sysmon — https://learn.microsoft.com/sysinternals/downloads/sysmon
- PowerShell Logging — https://learn.microsoft.com/powershell/
- Windows Event Logs — https://learn.microsoft.com/windows/win32/eventlog/event-logging

## MITRE ATT&CK

- MITRE ATT&CK — https://attack.mitre.org/
- Enterprise ATT&CK — https://attack.mitre.org/matrices/enterprise/
- Command and Scripting Interpreter — https://attack.mitre.org/techniques/T1059/
- PowerShell — https://attack.mitre.org/techniques/T1059/001/

## Defensive Security

- CISA — https://www.cisa.gov/
- NIST — https://www.nist.gov/cyberframework
- Microsoft Security — https://www.microsoft.com/security/

---
