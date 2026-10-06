# Memory Forensics

> **A practical enterprise guide to analyzing volatile memory for incident response, malware investigations, threat hunting, credential exposure, process analysis, network investigation, and advanced forensic reconstruction.**

---

# Overview

Memory forensics is the analysis of volatile system memory, commonly RAM, to identify evidence that may not exist—or may not be fully represented—on disk.

A running system can contain valuable evidence in memory:

```text
Processes
Threads
Command Lines
Network Connections
Loaded Modules
DLLs
Handles
Credentials
Tokens
Sockets
Injected Code
Malware
Encryption Keys
Clipboard Data
User Sessions
Kernel Objects
```

Unlike disk evidence, memory is highly volatile.

```text
System Running
     │
     ▼
RAM Changes Continuously
     │
     ├── Processes start/stop
     ├── Connections open/close
     ├── Credentials appear
     └── Malware executes
```

Therefore:

> **Memory acquisition should be considered time-sensitive evidence preservation.**

---

# Why Memory Forensics Matters

Disk forensics can answer:

> What was stored on the system?

Memory forensics can answer:

> What was happening in the system at a particular point in time?

This distinction is critical.

A malicious executable may be:

- Deleted from disk
- Renamed
- Unlinked
- Loaded only temporarily
- Injected into another process
- Executed from memory
- Partially represented by legitimate-looking files

Memory may still contain evidence of the activity.

---

# Memory Forensic Architecture

```text
                    System Memory
                         │
        ┌────────────────┼────────────────┐
        ▼                ▼                ▼
     User Space      Kernel Space      Network
        │                │                │
        ▼                ▼                ▼
    Processes        Drivers           Sockets
    Threads          Modules           Connections
    DLLs             Objects           Endpoints
    Handles          Kernel Data
        │
        └───────────────┬────────────────┘
                        ▼
                  Memory Image
                        │
                        ▼
                 Forensic Analysis
```

---

# Volatile Evidence

Examples include:

| Evidence | Volatility |
|---|---|
| Running processes | High |
| Network connections | High |
| Active sessions | High |
| Process memory | High |
| Credentials in memory | High |
| Clipboard | High |
| Temporary cryptographic material | High |
| Kernel state | High |
| Loaded modules | High |

The exact persistence characteristics depend on the operating system and system state.

---

# Order of Volatility

A simplified hierarchy:

```text
        Most Volatile
             │
             ▼
       CPU / Registers
             │
             ▼
            RAM
             │
             ▼
      Active Network State
             │
             ▼
     Temporary System State
             │
             ▼
          Disk
             │
             ▼
      Archived Evidence
             │
             ▼
        Least Volatile
```

The exact order can vary by environment and acquisition method.

---

# Memory Acquisition

Memory acquisition creates a forensic representation of volatile memory.

Conceptually:

```text
Running System
      │
      ▼
Memory Acquisition
      │
      ▼
Memory Image
      │
      ├── Hash
      ├── Preserve
      └── Analyze Copy
```

---

# Live Acquisition vs Dead Acquisition

## Live Acquisition

Memory is collected while the system is running.

Advantages:

- Captures volatile state
- Preserves active processes
- Captures current network state
- May reveal malware currently executing

Risks:

- Acquisition changes system state
- Some tools allocate memory
- Malware may detect acquisition
- Evidence can be altered

---

## Dead-System Acquisition

The system is powered down or otherwise unavailable for live collection.

Advantages:

- Avoids continued execution
- Allows controlled disk acquisition

Disadvantages:

- RAM contents are generally lost after shutdown
- Active sessions disappear
- Live network state disappears
- Running malware may no longer be observable

---

# Memory Acquisition Decision

```text
              Suspected Incident
                     │
                     ▼
             Is the system live?
                │          │
               Yes         No
                │           │
                ▼           ▼
        Evaluate live     Disk / other
        memory capture    evidence
                │
                ▼
        Risk vs Evidence
                │
        ┌───────┴───────┐
        ▼               ▼
     Acquire          Do Not
     Memory            Acquire
```

The decision should consider:

- Incident severity
- Legal authority
- Business impact
- System criticality
- Available tooling
- Evidence requirements

---

# Memory Acquisition Documentation

Record:

```text
Case ID
Host
Hostname
IP
Operating System
Time
Timezone
Acquisition Tool
Tool Version
Operator
Acquisition Method
Output Format
Hash
Storage Location
```

---

# Memory Integrity

After acquisition, calculate a cryptographic hash.

Example:

```bash
sha256sum memory.raw
```

Record the result in the evidence log.

Example:

```text
Evidence ID: MEM-001
File: host01-memory.raw
SHA-256: <recorded hash>
```

---

# Important Principle

Hashing demonstrates that the analyzed file matches the hashed evidence.

It does not prove:

- The source system was uncompromised
- The acquisition process was perfect
- The evidence is authentic by itself
- The interpretation is correct

Integrity is one component of forensic trust.

---

# Memory Analysis Workflow

```text
Memory Image
     │
     ▼
Validate Evidence
     │
     ▼
Identify OS / Profile
     │
     ▼
Process Analysis
     │
     ▼
Network Analysis
     │
     ▼
Modules / DLLs
     │
     ▼
Handles
     │
     ▼
Command Lines
     │
     ▼
Injection Indicators
     │
     ▼
Credentials / Tokens
     │
     ▼
Malware Analysis
     │
     ▼
Timeline / Correlation
```

---

# Volatility

**Volatility** is one of the most widely used frameworks for memory analysis.

The modern Volatility project is commonly referred to as:

```text
Volatility 3
```

It supports memory analysis across several operating-system families.

Official project:

https://volatility3.readthedocs.io/

---

# Volatility Concepts

Volatility uses plugins to analyze specific memory structures.

Conceptually:

```text
Memory Image
     │
     ▼
Volatility
     │
 ┌───┼───────────────┐
 ▼   ▼               ▼
PS   Network       Modules
 │     │               │
 ▼     ▼               ▼
Processes Connections DLLs
```

---

# Initial Memory Triage

The first objective is usually to establish:

```text
What OS is this?
What processes existed?
What network connections existed?
Which processes look unusual?
```

Do not immediately assume that the most unusual-looking process is malicious.

---

# Process Enumeration

A memory image can contain information about active or recently existing processes depending on the operating system and available artifacts.

Typical analysis questions:

```text
PID
PPID
Process Name
Executable Path
Command Line
User
Creation Time
Parent
Children
```

---

# Process Tree

Process relationships can be represented as:

```text
explorer.exe
      │
      └── powershell.exe
              │
              └── suspicious.exe
                     │
                     └── network connection
```

A process tree can reveal:

- Unusual parent-child relationships
- Office applications spawning shells
- Browsers spawning unexpected tools
- Scripts launching executables
- Service processes creating interactive shells

---

# Process Anomalies

Potential indicators include:

```text
Unexpected Parent
Unexpected Path
Suspicious Command Line
Unsigned Module
Executable Deleted From Disk
Unusual Network Activity
Injected Memory
Abnormal Process Name
```

These are indicators, not automatic proof of compromise.

---

# Process Name Masquerading

Attackers may use names resembling legitimate processes.

Example:

```text
svchost.exe
svhost.exe
scvhost.exe
```

Name alone is insufficient.

Correlate:

```text
Name
Path
Parent
User
Modules
Command Line
Network
Signature
```

---

# Process Paths

A legitimate process name running from an unusual location may require investigation.

Example reasoning:

```text
Expected:
C:\Windows\System32\svchost.exe

Unexpected:
C:\Users\Public\svchost.exe
```

Context and system configuration still matter.

---

# Command-Line Analysis

Command lines can reveal:

- Scripts
- Parameters
- Network destinations
- Administrative actions
- Tool execution
- Suspicious file paths

A useful relationship:

```text
Process
   │
   └── Command Line
           │
           ├── File
           ├── User
           └── Network
```

---

# Network Connections in Memory

Memory may contain evidence of network activity.

Investigate:

```text
Local IP
Local Port
Remote IP
Remote Port
Protocol
Owning Process
```

Conceptual example:

```text
Process
   │
   └── TCP Connection
          │
          ├── Local: 10.0.0.15:51522
          └── Remote: 203.0.113.10:443
```

Use reserved/example addresses in documentation and labs.

---

# Network Correlation

Do not treat an external connection as malicious simply because it is unfamiliar.

Correlate:

```text
Process
+
Destination
+
DNS
+
User
+
Time
+
Application Role
+
Threat Intelligence
```

---

# DLL and Module Analysis

Processes load modules such as:

- DLLs
- Shared libraries
- Drivers
- Runtime components

Investigate:

```text
Module Name
Path
Process
Load Address
Signature
Expected / Unexpected
```

---

# Suspicious Module Indicators

Potential indicators include:

- Unusual path
- Deleted module
- Unsigned module
- Unexpected module for process
- Recently introduced module
- Module associated with suspicious process

Again:

> An anomaly is a lead, not a conclusion.

---

# Handles

Processes maintain handles to operating-system objects.

Examples:

```text
Files
Registry Keys
Processes
Threads
Events
Mutants
Named Pipes
Sockets
```

Handle analysis can help answer:

> What resources was a process interacting with?

---

# Credential Evidence

Memory can contain sensitive authentication material.

Depending on OS and configuration, this may include:

- Authentication tokens
- Session information
- Credential material
- Security packages
- Application secrets

Credential extraction should only be performed under explicit authorization and appropriate evidence-handling procedures.

---

# Credential Forensics Principle

The objective is not:

> Extract everything possible.

The objective is:

> Determine whether credential exposure occurred and establish its forensic significance.

---

# Windows Memory Forensics

Windows memory can provide evidence about:

```text
Processes
Threads
DLLs
Handles
Registry Structures
Network
Tokens
Services
Drivers
Kernel Objects
```

Memory analysis can complement:

```text
Event Logs
Registry
Prefetch
Amcache
SRUM
EDR
```

---

# Windows Process Investigation

Investigate relationships such as:

```text
winword.exe
     │
     ▼
powershell.exe
     │
     ▼
suspicious process
```

Such a chain may deserve investigation depending on the context.

---

# Windows Injection Indicators

Process injection may leave memory artifacts.

Potential indicators include:

```text
Executable memory regions
Unusual memory permissions
Unbacked executable regions
Unexpected threads
Memory regions inconsistent with loaded modules
```

These indicators should be interpreted carefully.

---

# Common Process Injection Concepts

High-level categories include:

- Remote thread execution
- Process hollowing
- DLL injection
- Reflective loading
- APC-based execution

The forensic objective is to identify anomalous memory execution rather than blindly classify every unusual region as malicious.

---

# Memory Permissions

Executable memory can be described using permissions such as:

```text
Read
Write
Execute
```

A region combining write and execute permissions can deserve investigation, especially when inconsistent with normal application behavior.

However, legitimate software can also use unusual memory protections.

---

# Malware in Memory

Malware may appear through:

```text
Process
Memory Region
Module
Thread
Network Connection
Command Line
Persistence
```

The investigation should correlate multiple artifacts.

---

# Fileless Activity

Some malicious activity may leave limited conventional file evidence.

Examples include:

```text
Memory-resident code
Script execution
Abused administrative tools
In-memory modules
Temporary execution
```

Memory can therefore become particularly valuable.

---

# Deleted Executables

A process may remain active even after its backing file has been deleted.

This can create an important forensic clue:

```text
Disk:
Executable Missing

Memory:
Process Still Present
```

Investigators should preserve and analyze both sources.

---

# Linux Memory Forensics

Linux memory may provide evidence related to:

```text
Processes
Kernel State
Modules
Sockets
Credentials
Command Lines
Memory Regions
```

Memory should be interpreted alongside:

```text
journalctl
auth logs
audit logs
/proc
disk evidence
network telemetry
```

---

# Linux `/proc` vs Memory Image

`/proc` represents current system state.

A memory image represents a captured point in time.

Conceptually:

```text
Live /proc
     │
     └── Current State

Memory Image
     │
     └── Captured State
```

These sources can complement each other.

---

# Memory and Malware Timelines

Suppose:

```text
09:01 — Suspicious login
09:03 — Shell created
09:04 — Process launched
09:05 — Network connection
09:06 — File deleted
```

Memory may preserve process/network evidence that helps connect the events.

---

# Memory Evidence Correlation

A strong investigation correlates:

```text
Memory
  │
  ├── Process
  ├── Network
  ├── Module
  └── Command Line
        │
        ▼
Disk
  │
  ├── File
  ├── Timestamp
  └── Persistence
        │
        ▼
Logs
  │
  ├── Authentication
  ├── Execution
  └── Network
```

---

# Memory Forensic Decision Matrix

| Question | Useful Evidence |
|---|---|
| What was running? | Process analysis |
| What was connected? | Network analysis |
| What modules were loaded? | Module analysis |
| Was code injected? | Memory-region analysis |
| What launched the process? | Parent/child analysis |
| What resources were accessed? | Handle analysis |
| Were credentials exposed? | Authentication/security artifacts |
| Was malware resident? | Process + memory + network |
| What happened first? | Timeline correlation |

---

# Common Memory Forensic Mistakes

## Acquiring Memory Too Late

Volatile evidence may disappear.

## Performing Excessive Actions First

Every action can change system state.

## No Hashing

Evidence integrity becomes harder to demonstrate.

## Analyzing Only One Artifact

A suspicious process alone is insufficient.

## Treating Tool Output as Truth

Tools can misinterpret corrupted or unusual memory.

## Ignoring Time

Memory is a snapshot, not a complete historical record.

## Ignoring Disk Evidence

Memory and disk should complement each other.

---

# Memory Acquisition Risks

Live acquisition may:

- Modify memory
- Create processes
- Open files
- Generate network activity
- Alter system state

Document acquisition actions.

---

# Memory Analysis Validation

Forensic findings should be reproducible.

Record:

```text
Tool
Version
Plugin
Arguments
Memory Image Hash
Analysis Date
Analyst
Output
```

---

# Evidence Handling

Store memory images securely.

Recommended structure:

```text
Evidence/
│
├── Original/
│   └── memory.raw
│
├── Hashes/
│   └── memory.sha256
│
├── Working/
│   └── analysis-copy.raw
│
└── Reports/
    └── memory-analysis.md
```

---

# Chain of Custody

Example:

```text
Evidence ID: MEM-001

Collected:
2026-10-06 10:15 UTC

Host:
LINUX-SRV-01

Acquired By:
Analyst A

Method:
Approved memory acquisition procedure

SHA-256:
<recorded hash>

Transferred To:
Forensic Storage

Access:
Restricted
```

---

# Practical Lab 01 — Memory Triage

## Objective

Analyze an authorized memory image and establish:

```text
OS
Processes
Network
Users
Modules
Suspicious Activity
```

---

## Investigation Questions

```text
1. What operating system is represented?
2. What processes were running?
3. Which process is unusual?
4. What is its parent?
5. What command line was used?
6. What network connections existed?
7. Which modules were loaded?
```

---

# Practical Lab 02 — Process Tree Investigation

Construct:

```text
Parent
  │
  └── Child
        │
        └── Grandchild
```

Look for unusual relationships.

Document:

```text
PID
PPID
Process
Path
Command Line
User
Timestamp
Assessment
```

---

# Practical Lab 03 — Network Investigation

Identify active connections.

Create a table:

| Process | Local | Remote | Port | Assessment |
|---|---|---|---|---|
| Process A | Example | Example | 443 | Review |
| Process B | Example | Example | 53 | Expected |

Then correlate with:

- DNS
- Proxy
- Firewall
- EDR
- Threat intelligence

---

# Practical Lab 04 — Suspicious Process Investigation

Scenario:

> An endpoint security platform reports an unusual process.

Investigate:

```text
Process
   │
   ├── Parent
   ├── Command Line
   ├── Path
   ├── Modules
   ├── Network
   └── Memory
```

Determine whether the process is:

```text
Expected
Suspicious
Malicious
Unknown
```

Do not force a conclusion when evidence is insufficient.

---

# Practical Lab 05 — Memory-Resident Malware Investigation

Scenario:

> A suspicious process is active, but its executable is no longer present on disk.

Investigate:

```text
Process
   │
   ▼
Memory
   │
   ├── Modules
   ├── Memory Regions
   ├── Threads
   └── Network
```

Correlate with disk evidence.

---

# Practical Lab 06 — Complete Memory Investigation

Scenario:

```text
Security Alert
     │
     ▼
Memory Capture
     │
     ▼
Suspicious Process
     │
     ├── Unusual Parent
     ├── Suspicious Command Line
     ├── External Connection
     └── Abnormal Memory
```

Your report should establish:

1. What happened?
2. Which process was involved?
3. What launched it?
4. What network activity occurred?
5. Was code execution anomalous?
6. What evidence supports the finding?
7. What evidence is missing?
8. What is the confidence level?

---

# Memory Forensic Investigation Report

```text
# Memory Forensic Report

## Case Information

Case ID:
Host:
Hostname:
OS:
Acquisition Time:
Analyst:

## Evidence

Memory Image:
Hash:
Acquisition Method:

## Executive Summary

## System Identification

## Process Analysis

## Process Tree

## Command-Line Analysis

## Network Analysis

## Module Analysis

## Memory Anomalies

## Credential Exposure Assessment

## Malware Assessment

## Timeline

## Evidence Correlation

## Findings

## Evidence Gaps

## Confidence

## Recommendations

## Conclusion
```

---

# Example Finding

```text
Finding ID:
MEM-001

Title:
Suspicious Process with External Network Connection

Observation:
A process with an unusual parent-child relationship was identified in memory. The process also maintained an outbound connection to an external destination.

Evidence:
Memory process analysis
Process tree
Network connection data
Disk artifacts

Assessment:
The activity is suspicious and requires correlation with endpoint and network telemetry.

Confidence:
Medium

Limitation:
Historical network telemetry was incomplete.
```

---

# Memory Forensics and Detection Engineering

Memory findings can improve detection rules.

Example:

```text
Forensic Finding
      │
      ▼
Suspicious Parent/Child Relationship
      │
      ▼
Detection Hypothesis
      │
      ▼
EDR / SIEM Rule
      │
      ▼
Future Alert
```

---

# Memory Forensics and Threat Hunting

A memory finding can become a hunt hypothesis.

Example:

```text
Memory Finding:
Unusual executable memory

        ↓

Hunt:
Search endpoints for similar memory indicators

        ↓

Scope:
Identify affected hosts

        ↓

Detection:
Create behavioral analytic
```

---

# Memory Forensics and Incident Response

Memory analysis can support:

```text
Detection
   ↓
Triage
   ↓
Containment
   ↓
Memory Acquisition
   ↓
Analysis
   ↓
Scope
   ↓
Eradication
   ↓
Recovery
```

Memory should be collected at the appropriate point based on evidence preservation requirements.

---

# Enterprise Memory Forensics Architecture

```text
                    SOC / IR
                       │
                       ▼
                  Security Alert
                       │
                       ▼
                 Endpoint Triage
                       │
             ┌─────────┴─────────┐
             ▼                   ▼
          Memory              Disk
         Capture             Evidence
             │                   │
             └─────────┬─────────┘
                       ▼
                Forensic Platform
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Process         Network        Malware
     Analysis        Analysis       Analysis
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                  Correlation
                       │
                       ▼
                    Report
```

---

# Forensic Readiness for Memory

Organizations should establish:

```text
Approved acquisition tools
Acquisition procedures
Evidence storage
Access controls
Legal authority
Incident severity criteria
Analyst training
Hashing procedures
Chain of custody
```

---

# Memory Evidence Retention

Memory images can be large.

Organizations should define:

- What incidents require memory acquisition
- How images are stored
- Retention period
- Encryption
- Access controls
- Chain of custody
- Destruction procedures

Sensitive memory may contain credentials and personal information.

---

# Privacy Considerations

Memory can contain:

```text
Passwords
Tokens
Messages
Documents
Personal Data
Session Information
Application Secrets
```

Therefore:

> Memory analysis should follow data-minimization, authorization, access-control, and evidence-handling requirements.

---

# Analyst Safety

When analyzing potentially malicious memory:

- Use isolated forensic environments.
- Work from verified copies.
- Do not execute extracted binaries casually.
- Avoid connecting analysis systems to production networks.
- Preserve original evidence.
- Record tooling and methodology.

---

# Memory Analysis Confidence Model

## High Confidence

Multiple independent artifacts agree.

```text
Memory
+
EDR
+
Network
+
Disk
```

## Medium Confidence

Multiple related artifacts support the conclusion.

## Low Confidence

Single ambiguous memory artifact.

## Unknown

Insufficient evidence.

---

# Interview Questions

## 1. What is memory forensics?

The forensic examination of volatile memory to identify processes, network activity, loaded modules, credentials, malware, and other runtime evidence.

---

## 2. Why is memory important?

Because some evidence exists only temporarily while the system is running.

---

## 3. What is volatile evidence?

Evidence that can disappear or change rapidly when system state changes.

---

## 4. Why acquire memory before shutting down a system?

Because shutting down generally destroys active RAM contents.

---

## 5. What can memory reveal?

Potentially:

- Processes
- Threads
- Network connections
- Loaded modules
- Command lines
- Handles
- Tokens
- Malware
- Memory-resident code

---

## 6. What is Volatility?

A memory-forensics framework used to analyze operating-system memory images.

---

## 7. What is process injection?

A technique in which code executes within another process's address space.

From a forensic perspective, investigators may look for anomalous memory regions, threads, modules, and execution relationships.

---

## 8. Why is a suspicious process name insufficient?

Because attackers can imitate legitimate names, and legitimate software may also use unusual names.

Investigate:

```text
Path
Parent
Command Line
Modules
User
Network
Memory
```

---

## 9. What is a memory image?

A forensic representation of system memory captured at a particular point in time.

---

## 10. What is the difference between memory and disk forensics?

Disk forensics primarily examines persistent evidence.

Memory forensics examines volatile runtime state.

They complement one another.

---

## 11. Can memory prove that a system was compromised?

Memory can provide strong evidence, but conclusions should normally be based on correlated evidence and documented methodology.

---

## 12. What is process injection from a forensic perspective?

It is an execution pattern where code operates inside another process, potentially creating anomalous memory, thread, or module artifacts.

---

# Scenario Interview Question

### Scenario

> A process named `svchost.exe` is communicating with an unfamiliar external IP.

Do not immediately classify it as malicious.

Investigate:

```text
Process Path
Parent Process
Command Line
User
Loaded Modules
Network Destination
DNS
EDR
Expected Windows Services
Timeline
```

Then determine whether the behavior is expected.

---

# Scenario Interview Question

### Scenario

> A suspicious executable was deleted, but the process is still running.

Possible explanation:

```text
Disk
  │
  └── File Deleted

Memory
  │
  └── Process Still Running
```

Preserve memory and correlate:

- Process
- Path
- Command line
- Network
- Loaded modules
- File-system metadata

---

# Scenario Interview Question

### Scenario

> A server is suspected of running malware, but there is no obvious malicious file.

Investigate:

```text
Memory
Processes
Network
Modules
Command Lines
Persistence
Logs
```

Do not conclude that the absence of a suspicious file means the host is clean.

---

# Memory Forensics Maturity Model

## Level 1 — Basic

- Understand volatile evidence
- Understand RAM acquisition
- Perform basic process analysis

## Level 2 — Repeatable

- Standard acquisition procedure
- Hashing
- Process and network analysis
- Formal documentation

## Level 3 — Managed

- Enterprise forensic tooling
- Centralized evidence storage
- IR integration
- Analyst procedures

## Level 4 — Integrated

- EDR + SIEM + memory forensics
- Automated triage
- Threat hunting integration
- Detection engineering feedback

## Level 5 — Advanced

- Enterprise memory acquisition strategy
- Large-scale forensic workflows
- Advanced malware analysis
- Cross-host correlation
- Automated evidence preservation

---

# Chapter Completion Checklist

```text
[ ] Understand volatile evidence
[ ] Understand memory acquisition
[ ] Understand live vs dead acquisition
[ ] Understand evidence integrity
[ ] Understand Volatility
[ ] Understand process analysis
[ ] Understand process trees
[ ] Understand command-line analysis
[ ] Understand network analysis
[ ] Understand modules
[ ] Understand handles
[ ] Understand memory anomalies
[ ] Understand injection indicators
[ ] Understand malware in memory
[ ] Understand Windows memory forensics
[ ] Understand Linux memory forensics
[ ] Understand credential exposure considerations
[ ] Understand memory timelines
[ ] Understand evidence correlation
[ ] Complete process lab
[ ] Complete network lab
[ ] Complete malware-memory lab
[ ] Complete full memory investigation
```

---

# Key Takeaways

Memory forensics provides a view of **what a system was doing at a particular point in time**.

A strong investigation correlates:

```text
Process
   +
Parent / Child
   +
Command Line
   +
Modules
   +
Memory
   +
Network
   +
Disk
   +
Logs
```

Remember:

- RAM is volatile.
- Acquisition can change system state.
- Memory should be preserved early when appropriate.
- Hash forensic images.
- Work from verified copies.
- Process names alone are not sufficient.
- Network connections require context.
- Memory anomalies require validation.
- Memory and disk evidence complement one another.
- Sensitive credentials may exist in memory.
- Tool output should be independently interpreted.
- Strong forensic conclusions come from evidence correlation.

> **Memory forensics turns volatile runtime state into investigative evidence, helping investigators reconstruct processes, connections, execution, malware behavior, and other activity that may not be recoverable from disk alone.**

---

# References

### Volatility 3 Documentation

https://volatility3.readthedocs.io/

### Volatility Foundation

https://volatilityfoundation.org/

### NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response

https://csrc.nist.gov/publications/detail/sp/800-86/final

### NIST SP 800-61 — Incident Response

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### MITRE ATT&CK

https://attack.mitre.org/

### Microsoft Sysinternals

https://learn.microsoft.com/sysinternals/

### Microsoft Security

https://learn.microsoft.com/security/

### Linux Kernel Documentation

https://docs.kernel.org/

### SANS Digital Forensics

https://www.sans.org/digital-forensics/

### The Sleuth Kit

https://www.sleuthkit.org/

---

> **Preserve early. Validate carefully. Correlate broadly. Treat memory as a snapshot of system state, not the entire history of the system.**
