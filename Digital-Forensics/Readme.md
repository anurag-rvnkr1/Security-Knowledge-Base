# Digital Forensics

> **A practical, enterprise-oriented digital forensics knowledge base covering evidence preservation, forensic acquisition, Windows and Linux investigations, memory analysis, disk forensics, network forensics, cloud investigations, malware forensics, timeline reconstruction, and end-to-end forensic case studies.**

---

## Overview

Digital forensics is the disciplined process of identifying, preserving, acquiring, examining, analyzing, and reporting digital evidence.

It is used across:

- Incident response
- Security operations
- Threat hunting
- Malware investigations
- Insider-threat investigations
- Data-breach investigations
- Account-compromise investigations
- Fraud investigations
- Legal and regulatory investigations
- Law-enforcement investigations
- Corporate investigations
- Security research

A strong forensic investigation is not simply:

> "Find suspicious files."

It is a structured process of answering:

```text
What happened?
     │
     ▼
When did it happen?
     │
     ▼
How did it happen?
     │
     ▼
What evidence supports it?
     │
     ▼
What systems were affected?
     │
     ▼
What identities were involved?
     │
     ▼
What data was accessed?
     │
     ▼
What did the attacker do?
     │
     ▼
What can be proven?
```

---

# Why Digital Forensics Matters

Modern attacks leave evidence across multiple layers.

```text
                    Digital Investigation
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
     Endpoint           Network            Identity
        │                  │                  │
        ▼                  ▼                  ▼
      Files              PCAP               Logs
      Memory             DNS                Auth
      Processes          Firewall           Tokens
      Registry           Proxy              Sessions
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                         Cloud
                           │
                           ▼
                    Application Data
```

No single evidence source is always sufficient.

A mature forensic investigation correlates multiple sources to construct a defensible understanding of an event.

---

# Objectives

This section is designed to teach you how to:

- Understand digital evidence
- Preserve evidence correctly
- Acquire forensic images
- Maintain chain of custody
- Analyze Windows systems
- Analyze Linux systems
- Investigate memory
- Analyze disks and file systems
- Investigate network traffic
- Investigate cloud environments
- Analyze containers
- Understand mobile forensic fundamentals
- Investigate malware
- Build forensic timelines
- Correlate artifacts
- Assess evidence confidence
- Produce professional forensic reports

---

# Digital Forensics Investigation Lifecycle

```text
                 IDENTIFICATION
                       │
                       ▼
                  PRESERVATION
                       │
                       ▼
                   ACQUISITION
                       │
                       ▼
                    EXAMINATION
                       │
                       ▼
                    ANALYSIS
                       │
                       ▼
                 INTERPRETATION
                       │
                       ▼
                   REPORTING
                       │
                       ▼
                 PRESENTATION
```

---

# Core Forensic Principles

## 1. Preserve the Original

Whenever practical, the original evidence should remain protected.

Work from verified copies.

```text
Original Evidence
       │
       ▼
Forensic Acquisition
       │
       ▼
Hash Verification
       │
       ▼
Working Copy
       │
       ▼
Analysis
```

---

## 2. Maintain Integrity

Evidence should be protected from unauthorized alteration.

Cryptographic hashes can help verify integrity.

Example:

```bash
sha256sum evidence.img
```

---

## 3. Maintain Chain of Custody

Every transfer of evidence should be documented.

```text
Evidence Identified
       │
       ▼
Collected
       │
       ▼
Transferred
       │
       ▼
Stored
       │
       ▼
Analyzed
       │
       ▼
Reported
```

---

## 4. Separate Fact From Interpretation

Example:

```text
FACT:
A process executed at 10:32.

INTERPRETATION:
The process may have been related to attacker activity.

CONCLUSION:
Additional evidence is required before attributing the process to the attacker.
```

This distinction is critical.

---

# Evidence Categories

## Volatile Evidence

Evidence that may disappear or change quickly.

Examples:

- RAM
- Running processes
- Network connections
- Logged-in users
- Temporary state

---

## Non-Volatile Evidence

Evidence that persists after shutdown.

Examples:

- Disk
- File system
- Registry
- Logs
- Browser history
- Configuration files

---

# Order of Volatility

A simplified model:

```text
Most Volatile
     │
     ▼
CPU / Registers
     │
RAM
     │
Network Connections
     │
Running Processes
     │
Temporary Files
     │
Disk
     │
Remote Logs
     │
Backups
     ▼
Least Volatile
```

The exact acquisition order depends on the investigation and operational environment.

---

# Major Evidence Sources

| Source | Examples |
|---|---|
| Memory | Processes, modules, network state |
| Disk | Files, deleted files, metadata |
| Windows | Registry, Event Logs, Prefetch |
| Linux | auth logs, shell history, system logs |
| Network | PCAP, DNS, firewall |
| Identity | Authentication, sessions |
| Cloud | API activity, audit logs |
| Browser | History, cookies, downloads |
| Email | Headers, attachments, metadata |
| Applications | Application logs, databases |
| Containers | Images, layers, logs |
| Mobile | Device data, application artifacts |

---

# Major Forensic Domains

This section covers ten major areas.

```text
01 Fundamentals
02 Acquisition & Evidence
03 Windows
04 Linux
05 Memory
06 Disk & File Systems
07 Network
08 Cloud / Containers / Mobile
09 Malware
10 Timelines & Case Studies
```

---

# Chapter Roadmap

## 01 — Digital Forensics Fundamentals

**File:**

```text
01-Digital-Forensics-Fundamentals.md
```

Covers:

- Digital forensics definition
- Forensic methodology
- Evidence concepts
- Evidence types
- Volatile evidence
- Non-volatile evidence
- Forensic principles
- Evidence integrity
- Chain of custody
- Evidence handling
- Forensic roles
- Investigation workflow
- Legal and ethical considerations
- Forensic reporting
- Interview questions

---

## 02 — Forensic Acquisition and Evidence Preservation

**File:**

```text
02-Forensic-Acquisition-and-Evidence-Preservation.md
```

Covers:

- Evidence identification
- Evidence preservation
- Forensic imaging
- Bit-stream acquisition
- Live acquisition
- Dead-box acquisition
- Write blockers
- Hashing
- Evidence verification
- Chain of custody
- Evidence storage
- Acquisition tools
- Remote acquisition
- Cloud evidence acquisition
- Practical acquisition labs

---

## 03 — Windows Forensics

**File:**

```text
03-Windows-Forensics.md
```

Covers:

- Windows forensic architecture
- Windows Registry
- Event Logs
- PowerShell
- Prefetch
- Amcache
- Shimcache
- UserAssist
- LNK files
- Jump Lists
- SRUM
- Browser artifacts
- Windows Defender artifacts
- Scheduled Tasks
- Services
- Startup persistence
- NTFS artifacts
- Windows account investigation
- Windows incident case study

---

## 04 — Linux Forensics

**File:**

```text
04-Linux-Forensics.md
```

Covers:

- Linux forensic architecture
- File systems
- Authentication logs
- systemd journals
- Bash history
- SSH artifacts
- User accounts
- sudo activity
- Cron
- Services
- Processes
- Network connections
- File timestamps
- Deleted files
- Persistence
- Linux compromise investigation
- Linux forensic commands
- Practical investigation lab

---

## 05 — Memory Forensics

**File:**

```text
05-Memory-Forensics.md
```

Covers:

- RAM fundamentals
- Memory acquisition
- Volatile evidence
- Process analysis
- Process trees
- Network connections
- DLL/module analysis
- Handles
- Command lines
- Injection indicators
- Credential artifacts
- Malware in memory
- Windows memory analysis
- Linux memory analysis
- Volatility
- Memory investigation workflow
- Practical memory forensic lab

---

## 06 — Disk and File-System Forensics

**File:**

```text
06-Disk-and-File-System-Forensics.md
```

Covers:

- Disk architecture
- Partitions
- File systems
- NTFS
- FAT
- EXT4
- Inodes
- Metadata
- File timestamps
- Deleted files
- File carving
- Slack space
- Unallocated space
- Journaling
- Alternate data streams
- Hidden files
- Disk imaging
- File-system analysis
- Practical disk forensic investigation

---

## 07 — Network and Network Traffic Forensics

**File:**

```text
07-Network-and-Network-Traffic-Forensics.md
```

Covers:

- Network forensic methodology
- PCAP
- TCP/IP investigation
- DNS
- HTTP/HTTPS
- TLS metadata
- DHCP
- ARP
- Firewall logs
- Proxy logs
- VPN logs
- Beaconing
- Lateral movement
- Data exfiltration
- Network reconstruction
- Wireshark
- Zeek
- NetworkMiner
- Practical PCAP investigation

---

## 08 — Cloud, Container and Mobile Forensics

**File:**

```text
08-Cloud-Container-and-Mobile-Forensics.md
```

Covers:

- Cloud forensic challenges
- Cloud evidence sources
- AWS investigation
- Azure investigation
- Google Cloud investigation
- Cloud identity artifacts
- API activity
- Object storage
- Container evidence
- Docker investigation
- Kubernetes investigation
- Container logs
- Image layers
- Mobile forensic fundamentals
- Android artifacts
- iOS forensic concepts
- Cloud/container/mobile case studies

---

## 09 — Malware Forensics and Reverse Engineering

**File:**

```text
09-Malware-Forensics-and-Reverse-Engineering.md
```

Covers:

- Malware investigation methodology
- Static analysis
- Dynamic analysis
- Hashing
- Strings
- PE files
- ELF files
- Imports and exports
- Persistence
- C2 indicators
- Network behavior
- Sandboxing
- YARA
- Ghidra
- Debugging concepts
- Reverse engineering fundamentals
- Malware evidence handling
- Practical malware analysis lab

---

## 10 — Forensic Timelines, Investigation and Case Studies

**File:**

```text
10-Forensic-Timelines-Investigation-and-Case-Studies.md
```

Covers:

- Timeline construction
- Super timelines
- Timestamp normalization
- Time zones
- MACB concepts
- Event correlation
- Evidence correlation
- Attack reconstruction
- IOC pivoting
- Entity relationships
- Confidence assessment
- Negative evidence
- Root cause analysis
- Forensic reporting
- End-to-end investigations
- Case studies
- Practical investigation labs

---

# Forensic Investigation Methodology

A practical investigation can follow:

```text
1. Define Investigation Scope
          │
          ▼
2. Identify Evidence Sources
          │
          ▼
3. Preserve Evidence
          │
          ▼
4. Acquire Evidence
          │
          ▼
5. Verify Integrity
          │
          ▼
6. Extract Artifacts
          │
          ▼
7. Build Timeline
          │
          ▼
8. Correlate Evidence
          │
          ▼
9. Develop Findings
          │
          ▼
10. Assess Confidence
          │
          ▼
11. Document Results
          │
          ▼
12. Report
```

---

# Evidence Correlation

The strongest investigations rarely rely on a single artifact.

Example:

```text
Windows Event Log
       │
       ├──────────────┐
       ▼              ▼
PowerShell         Registry
       │              │
       └──────┬───────┘
              ▼
            Process
              │
              ▼
          Network
              │
              ▼
             DNS
              │
              ▼
        External Host
```

Each artifact increases or decreases confidence in the investigation hypothesis.

---

# Evidence Confidence

Use explicit confidence levels.

### High Confidence

Multiple independent evidence sources agree.

### Medium Confidence

Evidence strongly supports the conclusion but some gaps remain.

### Low Confidence

The evidence is suggestive but insufficient for a strong conclusion.

Example:

```text
Finding:
Credential compromise occurred.

Evidence:
Authentication logs
Endpoint telemetry
Identity provider events
Network activity

Confidence:
High
```

---

# Forensic Tools

Common tools include:

### Disk

- Autopsy
- The Sleuth Kit
- FTK
- EnCase
- X-Ways

### Memory

- Volatility
- WinPmem
- LiME

### Network

- Wireshark
- Zeek
- NetworkMiner
- tcpdump

### Malware

- Ghidra
- IDA
- YARA
- capa
- FLOSS

### Acquisition

- FTK Imager
- Guymager
- dd
- dc3dd

### Timeline

- Plaso
- log2timeline
- Timesketch

Tool selection should depend on evidence type, environment, legal requirements, and organizational procedures.

---

# Forensic Tooling Architecture

```text
                    Evidence
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
      Disk           Memory          Network
       │               │               │
       ▼               ▼               ▼
     Autopsy       Volatility       Wireshark
       │               │               │
       └───────────────┼───────────────┘
                       ▼
                   Timeline
                       │
                       ▼
                  Correlation
                       │
                       ▼
                    Report
```

---

# Forensic Reporting

A professional report should contain:

```text
Executive Summary
Investigation Scope
Evidence Sources
Acquisition Method
Evidence Integrity
Methodology
Timeline
Findings
Analysis
Indicators
Affected Systems
Affected Identities
Evidence Limitations
Confidence
Conclusions
Recommendations
Appendices
```

---

# Example Finding

```text
Finding ID:
DF-001

Finding:
Suspicious PowerShell execution was observed on WS-104.

Evidence:
Windows PowerShell event logs
EDR process telemetry
Prefetch artifact
Network connection telemetry

Timeline:
2026-10-05 10:32 UTC

Assessment:
The process executed under the compromised user context and established an outbound connection shortly afterward.

Confidence:
High

Recommendation:
Investigate the associated account and destination infrastructure.
```

---

# Evidence Limitations

Every professional forensic report should explicitly state limitations.

Examples:

- Disk image unavailable
- Memory not captured
- Logs expired
- Endpoint telemetry incomplete
- Cloud retention expired
- Clock synchronization uncertain
- Encrypted storage unavailable
- Deleted evidence unrecoverable

A limitation is not a failure.

Failing to document the limitation is the problem.

---

# Legal and Ethical Considerations

Digital forensic analysis must be performed within authorized boundaries.

Important considerations include:

- Scope of authorization
- Privacy
- Data minimization
- Evidence integrity
- Chain of custody
- Legal requirements
- Regulatory requirements
- Organizational policy
- Jurisdiction
- Sensitive information handling

Never collect or analyze systems without appropriate authorization.

---

# Digital Forensics and Incident Response

Digital forensics is closely integrated with incident response.

```text
Incident Response
       │
       ▼
Detection
       │
       ▼
Investigation
       │
       ├───────────────┐
       ▼               ▼
 Threat Hunting    Forensics
       │               │
       └───────┬───────┘
               ▼
             Scope
               │
               ▼
            Recovery
```

---

# Digital Forensics and Threat Hunting

Threat hunters can use forensic artifacts to search historical activity.

Example:

```text
Forensic Finding
       │
       ▼
IOC / TTP
       │
       ▼
Historical Search
       │
       ▼
Additional Hosts
       │
       ▼
Expanded Scope
```

---

# Digital Forensics and Detection Engineering

Forensic findings frequently become detection requirements.

```text
Forensic Artifact
       │
       ▼
Observed Behavior
       │
       ▼
Detection Hypothesis
       │
       ▼
Detection Rule
       │
       ▼
Validation
```

---

# Enterprise Forensic Readiness

Forensic capability should be designed before an incident occurs.

Organizations should prepare:

```text
Asset Inventory
Logging
Time Synchronization
Endpoint Telemetry
Network Telemetry
Cloud Audit Logs
Evidence Storage
Acquisition Procedures
Chain of Custody
Trained Personnel
Forensic Tools
Legal Procedures
```

---

# Forensic Readiness Architecture

```text
                    Enterprise
                        │
        ┌───────────────┼────────────────┐
        ▼               ▼                ▼
     Endpoint         Network           Cloud
        │               │                │
        ▼               ▼                ▼
      EDR              PCAP          Audit Logs
        │               │                │
        └───────────────┼────────────────┘
                        ▼
                     SIEM
                        │
                        ▼
                Forensic Collection
                        │
                        ▼
                 Evidence Repository
                        │
                        ▼
                 Forensic Analysts
                        │
                        ▼
                     Report
```

---

# Practical Labs

This section will include hands-on investigations such as:

### Lab 01 — Windows Artifact Investigation

Investigate:

- Event Logs
- Registry
- Prefetch
- PowerShell
- User activity

### Lab 02 — Linux Compromise Investigation

Investigate:

- SSH
- Authentication
- Bash history
- Processes
- Persistence

### Lab 03 — Memory Investigation

Analyze:

- Processes
- Network connections
- Suspicious modules
- Command lines

### Lab 04 — Disk Investigation

Investigate:

- Deleted files
- File metadata
- Persistence
- User activity

### Lab 05 — PCAP Investigation

Analyze:

- DNS
- HTTP
- TCP
- Beaconing
- Suspicious traffic

### Lab 06 — Cloud Investigation

Analyze:

- Authentication
- API activity
- IAM
- Storage access

### Lab 07 — Malware Investigation

Perform:

- Static analysis
- Dynamic analysis
- IOC extraction
- Behavioral analysis

### Lab 08 — Full Timeline Investigation

Correlate:

```text
Endpoint
+
Identity
+
Network
+
Cloud
```

to reconstruct a complete attack.

---

# Interview Preparation

Each chapter includes interview questions covering:

- Evidence handling
- Chain of custody
- Windows artifacts
- Linux artifacts
- Memory analysis
- Disk forensics
- Network forensics
- Cloud forensics
- Malware analysis
- Timeline analysis
- Investigation methodology
- Reporting

---

# Recommended Learning Path

```text
Phase 1
Forensic Fundamentals
        │
        ▼
Phase 2
Evidence Acquisition
        │
        ▼
Phase 3
Windows + Linux
        │
        ▼
Phase 4
Disk + Memory
        │
        ▼
Phase 5
Network
        │
        ▼
Phase 6
Cloud + Containers + Mobile
        │
        ▼
Phase 7
Malware
        │
        ▼
Phase 8
Timeline Reconstruction
        │
        ▼
Phase 9
End-to-End Investigations
```

---

# Skills Developed

After completing this section, you should be able to demonstrate knowledge of:

### Evidence

- Evidence preservation
- Acquisition
- Integrity
- Chain of custody

### Endpoint

- Windows forensics
- Linux forensics
- Registry
- Logs
- File systems

### Memory

- Process analysis
- Network analysis
- Memory artifacts
- Malware in memory

### Network

- PCAP analysis
- DNS investigation
- Protocol analysis
- Network reconstruction

### Cloud

- Cloud audit logs
- Identity investigation
- API activity
- Storage access

### Malware

- Static analysis
- Dynamic analysis
- IOC extraction
- Behavioral analysis

### Investigation

- Timeline reconstruction
- Evidence correlation
- Hypothesis testing
- Reporting

---

# Forensic Investigation Checklist

```text
[ ] Scope defined
[ ] Authorization verified
[ ] Evidence identified
[ ] Volatile evidence considered
[ ] Evidence preserved
[ ] Acquisition performed
[ ] Hashes calculated
[ ] Chain of custody documented
[ ] Working copy created
[ ] Artifacts extracted
[ ] Timeline constructed
[ ] Evidence correlated
[ ] Findings documented
[ ] Confidence assessed
[ ] Limitations documented
[ ] Report completed
```

---

# Professional Principles

## Preserve First

Do not unnecessarily alter evidence.

## Verify Everything

Use hashes and independent evidence where appropriate.

## Document Everything

If an action matters, record it.

## Separate Facts From Conclusions

Do not overstate evidence.

## Maintain Reproducibility

Another qualified investigator should be able to understand how the conclusion was reached.

## Minimize Assumptions

Prefer evidence over speculation.

## Protect Sensitive Data

Forensic evidence can contain highly sensitive information.

---

# Repository Structure

```text
Digital-Forensics/
│
├── README.md
│
├── 01-Digital-Forensics-Fundamentals.md
├── 02-Forensic-Acquisition-and-Evidence-Preservation.md
├── 03-Windows-Forensics.md
├── 04-Linux-Forensics.md
├── 05-Memory-Forensics.md
├── 06-Disk-and-File-System-Forensics.md
├── 07-Network-and-Network-Traffic-Forensics.md
├── 08-Cloud-Container-and-Mobile-Forensics.md
├── 09-Malware-Forensics-and-Reverse-Engineering.md
└── 10-Forensic-Timelines-Investigation-and-Case-Studies.md
```

---

# How to Use This Section

For learning:

1. Read the chapter.
2. Understand the forensic concepts.
3. Study the diagrams.
4. Practice the commands.
5. Complete the practical lab.
6. Answer the interview questions.
7. Review the references.
8. Connect the chapter with Incident Response and Threat Hunting.

For portfolio development:

```text
Learn
  ↓
Practice
  ↓
Investigate
  ↓
Document
  ↓
Publish
```

---

# Relationship With Other Knowledge Base Sections

Digital Forensics connects directly with several other domains.

```text
                    Digital Forensics
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
Incident Response     Threat Hunting      Detection
        │                  │                  │
        ▼                  ▼                  ▼
Investigation          Hypotheses          Artifacts
        │                  │                  │
        └──────────────────┼──────────────────┘
                           ▼
                       Evidence
                           │
                           ▼
                       Findings
```

It also connects to:

- Malware Analysis
- Reverse Engineering
- SIEM
- SOC
- Active Directory
- Windows
- Linux
- Cloud Security
- Network Security
- Threat Intelligence
- MITRE ATT&CK

---

# Maturity Model

## Level 1 — Basic

- Manual artifact collection
- Limited evidence handling
- Basic investigation knowledge

## Level 2 — Repeatable

- Documented acquisition
- Standard procedures
- Basic forensic tooling

## Level 3 — Managed

- Formal evidence processes
- Centralized logging
- Dedicated forensic capability

## Level 4 — Integrated

- IR + forensics + hunting
- Automated evidence collection
- Centralized investigation workflows

## Level 5 — Advanced

- Enterprise forensic readiness
- Rapid acquisition
- Cross-domain correlation
- Advanced memory and malware analysis
- Continuous forensic capability improvement

---

# Completion Checklist

```text
[ ] 01 Fundamentals
[ ] 02 Acquisition & Preservation
[ ] 03 Windows Forensics
[ ] 04 Linux Forensics
[ ] 05 Memory Forensics
[ ] 06 Disk & File-System Forensics
[ ] 07 Network Forensics
[ ] 08 Cloud / Container / Mobile Forensics
[ ] 09 Malware Forensics
[ ] 10 Timelines & Case Studies
```

---

# References

### NIST

Guide to Integrating Forensic Techniques into Incident Response — NIST SP 800-86:

https://csrc.nist.gov/publications/detail/sp/800-86/final

### NIST

Computer Security Incident Handling Guide:

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### SWGDE

Scientific Working Group on Digital Evidence:

https://www.swgde.org/

### CISA

Cybersecurity and forensic resources:

https://www.cisa.gov/

### MITRE ATT&CK

https://attack.mitre.org/

### The Sleuth Kit

https://www.sleuthkit.org/

### Autopsy

https://www.autopsy.com/

### Volatility

https://volatilityfoundation.org/

### Wireshark

https://www.wireshark.org/

### Zeek

https://zeek.org/

### Ghidra

https://ghidra-sre.org/

### YARA

https://virustotal.github.io/yara/

### Plaso

https://plaso.readthedocs.io/

---

# Final Objective

The objective of this section is not simply to learn forensic tools.

It is to develop the ability to reason from evidence.

```text
Evidence
   │
   ▼
Artifact
   │
   ▼
Event
   │
   ▼
Timeline
   │
   ▼
Correlation
   │
   ▼
Hypothesis
   │
   ▼
Validation
   │
   ▼
Finding
   │
   ▼
Conclusion
```

A strong forensic investigator does not begin with:

> **"What tool should I run?"**

They begin with:

> **"What question am I trying to answer, what evidence can answer it, and how can I preserve and validate that evidence?"**

That mindset is the foundation of professional digital forensics.

---

> **Preserve the evidence. Validate the artifact. Reconstruct the timeline. Correlate the facts. Document the conclusion.**
