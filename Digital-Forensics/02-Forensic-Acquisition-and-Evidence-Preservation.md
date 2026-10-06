# Forensic Acquisition and Evidence Preservation

> **A practical guide to identifying, preserving, acquiring, validating, storing, and documenting digital evidence across endpoints, storage media, networks, cloud environments, and enterprise systems.**

---

# Overview

Forensic acquisition is the process of obtaining digital evidence in a manner that preserves its integrity and supports reliable examination.

Evidence preservation is equally important.

A technically excellent investigation can be weakened if:

- Evidence was modified during collection
- The original was not protected
- Hashes were not recorded
- Chain of custody was incomplete
- Acquisition methodology was undocumented
- Evidence was stored insecurely
- Volatile evidence was lost unnecessarily

The fundamental principle is:

> **Preserve the evidence before attempting to interpret it.**

---

# Acquisition and Preservation Lifecycle

```text id="x6j8m2"
Identify Evidence
       │
       ▼
Assess Volatility
       │
       ▼
Preserve
       │
       ▼
Acquire
       │
       ▼
Hash
       │
       ▼
Verify
       │
       ▼
Store
       │
       ▼
Create Working Copy
       │
       ▼
Analyze
```

---

# Why Acquisition Matters

Forensic analysis is only as reliable as the evidence being analyzed.

Consider:

```text id="w7y8v2"
Bad Acquisition
      │
      ▼
Incomplete Evidence
      │
      ▼
Incomplete Timeline
      │
      ▼
Incorrect Scope
      │
      ▼
Incorrect Conclusion
```

A controlled acquisition process attempts to prevent this chain.

---

# Acquisition Objectives

A good acquisition process should:

- Preserve evidence integrity
- Minimize evidence alteration
- Capture relevant data
- Document collection
- Support reproducibility
- Support independent verification
- Protect sensitive information
- Maintain chain of custody

---

# Evidence Identification

Before collecting evidence, determine what may be relevant.

Potential evidence sources include:

```text id="8t9i2v"
Endpoint
   │
   ├── Disk
   ├── Memory
   ├── Logs
   ├── Registry
   └── Applications

Network
   │
   ├── PCAP
   ├── DNS
   ├── Firewall
   └── Proxy

Identity
   │
   ├── Authentication
   ├── MFA
   └── Sessions

Cloud
   │
   ├── Audit Logs
   ├── API Activity
   ├── IAM
   └── Storage
```

---

# Evidence Prioritization

Not every source needs to be acquired immediately.

Prioritize according to:

```text
Volatility
Relevance
Business Impact
Evidence Value
Collection Risk
Availability
Retention
```

A useful conceptual model:

```text id="0q8qiw"
High Volatility
      +
High Relevance
      +
High Evidence Value
      ↓
Highest Priority
```

---

# Live vs Dead Acquisition

Two major acquisition models are:

### Live Acquisition

Collection occurs while the system is operating.

### Dead Acquisition

Collection occurs after the system has been shut down or storage has been detached.

---

# Live Acquisition

Live acquisition can provide access to:

- RAM
- Running processes
- Network connections
- Logged-in users
- Open files
- Active sessions
- Temporary state

Example:

```text id="8r4z7k"
Running System
      │
      ├── RAM
      ├── Processes
      ├── Network
      ├── Users
      └── Temporary State
```

---

# Risks of Live Acquisition

Live collection can alter the system.

For example:

```text id="0n2w8h"
Run Collection Tool
        │
        ▼
Process Created
        │
        ▼
Memory Changed
        │
        ▼
System State Modified
```

Therefore, live acquisition should be planned carefully.

---

# Dead Acquisition

Dead acquisition generally involves:

```text id="t0f6jp"
System
  │
  ▼
Shutdown / Controlled State
  │
  ▼
Storage Media
  │
  ▼
Forensic Acquisition
  │
  ▼
Image
```

Advantages may include:

- Reduced system-state changes
- Easier disk acquisition
- More predictable storage analysis

But volatile evidence may already be lost.

---

# Choosing the Acquisition Strategy

Ask:

```text id="r8uyhi"
Is RAM important?
      │
      ├── Yes → Consider live acquisition
      │
      └── No
           │
           ▼
Is immediate disk acquisition required?
           │
           ▼
Determine safest evidence-preserving approach
```

There is no universal acquisition order.

The correct approach depends on the incident.

---

# Forensic Imaging

Forensic imaging creates a controlled representation of storage media.

Conceptually:

```text id="5b9rjx"
Source Media
     │
     ▼
Acquisition Tool
     │
     ▼
Forensic Image
     │
     ▼
Hash
     │
     ▼
Verification
```

---

# Physical vs Logical Acquisition

## Physical Acquisition

Attempts to capture storage at the block level.

It can potentially include:

- Active files
- Deleted files
- File-system metadata
- Unallocated space
- Hidden structures

---

## Logical Acquisition

Collects selected files or directories.

Example:

```text id="8ckjso"
C:\Users\User\AppData\
C:\Windows\System32\winevt\Logs\
```

Logical acquisition may be faster but can omit evidence outside the selected scope.

---

# Physical vs Logical

| Characteristic | Physical | Logical |
|---|---|---|
| Scope | Broad | Selected |
| Deleted data | Potentially available | Usually limited |
| Speed | Slower | Faster |
| Storage | Larger | Smaller |
| Forensic depth | High | Lower |
| Operational impact | Potentially higher | Usually lower |

The choice should be based on investigation requirements.

---

# File-System-Level Acquisition

Another approach is collecting relevant file-system structures and artifacts.

Examples:

- Event logs
- Registry hives
- Browser databases
- User directories
- Application logs
- Persistence artifacts

This is often useful during rapid incident response.

---

# Write Blockers

A hardware or software write-blocking mechanism can help prevent unintended modification of storage media during acquisition.

Conceptually:

```text id="q7l3uw"
Evidence Drive
      │
      ▼
Write Blocker
      │
      ▼
Forensic Workstation
      │
      ▼
Acquisition
```

Write blockers are particularly important when working directly with removable storage or physical media.

---

# Why Write Protection Matters

Without write protection, a forensic workstation may unintentionally:

- Update file-system metadata
- Change access timestamps
- Create system files
- Modify journal state
- Alter metadata

Even unintended changes can complicate forensic interpretation.

---

# Forensic Image Formats

Common forensic image approaches include:

### Raw

A direct representation of acquired storage blocks.

### E01

A commonly used forensic evidence format supporting metadata and integrity information.

### AFF / AFF4

Open forensic acquisition formats with capabilities that can support evidence management.

Tool and format selection should follow organizational procedures and interoperability requirements.

---

# Acquisition Metadata

Record:

```text id="3t0mmb"
Case ID
Evidence ID
Source Device
Serial Number
Device Size
Acquisition Date
Acquisition Time
Time Zone
Acquisition Tool
Tool Version
Operator
Image Format
Hash
Destination
```

---

# Evidence Hashing

Hash the acquired evidence.

Example:

```bash id="y6x0qf"
sha256sum evidence.E01
```

or:

```bash id="2atj4e"
sha256sum disk-image.raw
```

Store the hash in the case record.

---

# Why SHA-256?

SHA-256 provides a strong modern integrity mechanism.

Example:

```text id="p8k3tq"
Evidence:
disk-image.raw

SHA-256:
a31c...8e92
```

If the same evidence is later hashed and produces a different value, investigate the discrepancy.

---

# Hash Verification

Verification should occur after acquisition and whenever evidence integrity must be demonstrated.

```text id="zj89h5"
Acquire
  │
  ▼
Hash Source / Image
  │
  ▼
Store Hash
  │
  ▼
Transfer
  │
  ▼
Recalculate
  │
  ▼
Compare
```

---

# Hash Limitations

Hashing proves that two inputs produce the same hash value under the selected algorithm.

It does not prove:

- That the evidence is genuine
- That acquisition captured everything required
- That the correct device was acquired
- That the investigator interpreted the evidence correctly

Integrity and authenticity are related but different concepts.

---

# Evidence Authenticity

To strengthen authenticity, correlate:

- Device identifiers
- Serial numbers
- Acquisition records
- Chain of custody
- Hashes
- System inventory
- Collection logs

---

# Chain of Custody

Chain of custody provides an auditable history of evidence handling.

Typical lifecycle:

```text id="d4qgqk"
Collected
   │
   ▼
Sealed / Stored
   │
   ▼
Transferred
   │
   ▼
Received
   │
   ▼
Analyzed
   │
   ▼
Returned / Archived
```

---

# Chain-of-Custody Record

Example:

```text id="g4n9la"
Evidence ID:
DF-2026-004

Description:
Laptop forensic image

Collected By:
Forensic Analyst

Date:
2026-10-06

Time:
10:45 UTC

Hash:
<recorded SHA-256>

Transferred To:
Evidence Repository

Purpose:
Forensic examination

Storage:
Restricted evidence storage
```

---

# Evidence Identification Labels

Every evidence item should have a unique identifier.

Example:

```text id="31e6at"
CASE-2026-014
   │
   ├── EV-001 Laptop
   ├── EV-002 Memory Image
   ├── EV-003 Disk Image
   ├── EV-004 PCAP
   └── EV-005 Cloud Logs
```

---

# Evidence Inventory

Maintain an evidence inventory.

| ID | Source | Type | Hash | Status |
|---|---|---|---|---|
| EV-001 | WS-104 | Disk Image | Recorded | Acquired |
| EV-002 | WS-104 | Memory | Recorded | Analyzed |
| EV-003 | Network | PCAP | Recorded | Analyzed |
| EV-004 | Cloud | Audit Logs | Recorded | Archived |

---

# Evidence Storage

Evidence repositories should provide:

- Encryption
- Access control
- Audit logging
- Integrity protection
- Backup
- Retention management
- Controlled deletion

---

# Evidence Access Model

```text id="1w9a1f"
Evidence Repository
       │
       ▼
Authentication
       │
       ▼
Authorization
       │
       ▼
Audit Logging
       │
       ▼
Evidence Access
```

Access should be restricted to authorized personnel.

---

# Working Copies

Do not perform routine analysis on the original evidence.

A common model is:

```text id="x1g8cg"
Original
   │
   ▼
Master Copy
   │
   ├──────────┐
   ▼          ▼
Working A   Working B
   │          │
   ▼          ▼
Analysis    Analysis
```

This allows independent analysis without repeatedly touching the source.

---

# Evidence Preservation vs Investigation Speed

Incident response often creates tension:

```text id="0x4i4p"
Evidence Preservation
        ↕
Operational Continuity
```

For example, keeping a compromised production server online may preserve volatile evidence but also allow an attacker to continue operating.

The decision should consider:

- Threat severity
- Business impact
- Evidence volatility
- Safety
- Legal requirements
- Incident-response procedures

---

# Volatile Evidence

Before shutdown, consider whether the investigation requires:

- RAM
- Processes
- Network connections
- Logged-in users
- Open files
- Active sessions
- Mounted storage

---

# Memory Acquisition

Memory acquisition methods vary by operating system.

### Windows

Tools may include:

- WinPmem
- Magnet RAM Capture
- Commercial forensic platforms

### Linux

Tools may include:

- LiME
- AVML
- Other validated acquisition tooling

The acquisition tool should be validated and appropriate for the investigation.

---

# Memory Acquisition Risks

Memory acquisition can:

- Change system state
- Consume resources
- Generate processes
- Alter memory
- Fail on certain systems

Document:

- Tool
- Version
- Time
- Operator
- Target
- Output
- Hash

---

# Disk Acquisition

A controlled disk acquisition workflow:

```text id="3qzylp"
Identify Disk
     │
     ▼
Record Device Information
     │
     ▼
Protect Evidence
     │
     ▼
Acquire
     │
     ▼
Calculate Hash
     │
     ▼
Verify
     │
     ▼
Store
```

---

# Example Device Documentation

```bash id="jlv1xp"
lsblk
```

Linux may also provide:

```bash id="5kv7g4"
sudo fdisk -l
```

These commands can help identify storage devices during authorized acquisition.

---

# Windows Storage Identification

Examples:

```powershell id="qgibxa"
Get-Disk
```

and:

```powershell id="b8izdy"
Get-Volume
```

These are identification commands, not substitutes for a formal forensic acquisition process.

---

# Remote Acquisition

Remote evidence collection can be useful when:

- Endpoint is geographically distant
- Immediate physical access is impossible
- Large enterprise environments are involved
- Centralized EDR collection is available

But remote collection introduces additional considerations:

- Network availability
- Evidence transfer integrity
- Authentication
- Authorization
- Bandwidth
- Endpoint impact
- Chain of custody

---

# Remote Acquisition Architecture

```text id="4rvvgr"
Remote Endpoint
      │
      ▼
Collection Agent
      │
      ▼
Secure Channel
      │
      ▼
Forensic Collection Server
      │
      ▼
Evidence Repository
```

---

# Cloud Evidence Acquisition

Cloud evidence differs from traditional disk acquisition.

There may be no physical disk available to investigators.

Instead, evidence may come from:

```text id="4osb8k"
Identity Provider
      │
      ├── Authentication
      ├── MFA
      └── Sessions
             │
             ▼
         Cloud APIs
             │
      ┌──────┼──────┐
      ▼      ▼      ▼
   Storage Compute Network
      │      │      │
      └──────┼──────┘
             ▼
          Audit Logs
```

---

# Cloud Acquisition Challenges

Challenges include:

- Short log retention
- Distributed infrastructure
- Multi-tenant architecture
- Provider-controlled infrastructure
- Time synchronization
- API pagination
- Large data volumes
- Access permissions
- Legal jurisdiction

---

# Cloud Evidence Preservation

When an incident occurs:

```text
Identify
   │
   ▼
Determine Retention
   │
   ▼
Preserve Logs
   │
   ▼
Preserve Relevant Resources
   │
   ▼
Export Evidence
   │
   ▼
Hash
   │
   ▼
Store
```

---

# SaaS Evidence

SaaS applications may contain:

- Login events
- Administrative actions
- File access
- Sharing events
- OAuth activity
- Configuration changes
- API activity

Investigators should understand the provider's logging and retention model before relying on a SaaS artifact.

---

# Container Evidence

Containers are ephemeral by design.

Relevant evidence may include:

```text id="b2gn5f"
Container Logs
Image
Image Layers
Container Metadata
Runtime Events
Host Logs
Kubernetes Audit Logs
Network Telemetry
```

---

# Container Preservation Challenge

```text id="0brnq3"
Container Running
      │
      ▼
Container Removed
      │
      ▼
Runtime Evidence Lost
```

Therefore, incident response procedures should account for container volatility.

---

# Kubernetes Evidence

Potential evidence includes:

- Kubernetes audit logs
- Pod events
- Deployment configuration
- Service accounts
- Secrets access
- Node logs
- Container logs
- Network telemetry
- Cloud provider audit logs

---

# Mobile Evidence

Mobile devices contain:

- Application data
- Messages
- Call records
- Browser data
- Location information
- Authentication artifacts
- Photos
- Device configuration

Mobile acquisition is highly platform-dependent and should use appropriate authorized forensic procedures.

---

# Evidence Preservation Notice

A preservation request may be appropriate when evidence could expire or be deleted.

Potential targets:

```text id="h0v4f0"
Cloud Logs
Email
SaaS Data
Firewall Logs
Proxy Logs
DNS Logs
EDR Data
Application Logs
```

---

# Log Retention

A common forensic problem:

```text id="f7m8tr"
Incident
   │
   ▼
Investigation
   │
   ▼
Log Retention Expired
   │
   ▼
Evidence Missing
```

Forensic readiness therefore depends heavily on appropriate retention policies.

---

# Log Preservation Strategy

Organizations should define:

- Critical log sources
- Retention periods
- Immutable storage requirements
- Access controls
- Backup requirements
- Export procedures
- Legal holds where appropriate

---

# Time Synchronization

Evidence correlation depends on accurate time.

Use centralized time synchronization where practical.

Conceptually:

```text id="3d8d4f"
              Time Source
                  │
        ┌─────────┼─────────┐
        ▼         ▼         ▼
    Endpoint    Server     Cloud
        │         │         │
        └─────────┼─────────┘
                  ▼
            Consistent Timeline
```

---

# Acquisition Documentation

Every acquisition should record:

```text id="z5a8uh"
Who
What
When
Where
Why
How
Tool
Version
Hash
Result
```

This is the forensic equivalent of maintaining an engineering change record.

---

# Acquisition Failure

Acquisition can fail due to:

- Hardware problems
- Encryption
- Insufficient permissions
- Storage corruption
- Tool incompatibility
- Network failure
- Insufficient storage
- System instability

Failure should be documented rather than silently ignored.

---

# Acquisition Validation

After acquisition:

```text id="v6u2nq"
Was the correct source acquired?
        │
        ▼
Was the acquisition complete?
        │
        ▼
Was integrity verified?
        │
        ▼
Can the image be mounted/read?
        │
        ▼
Can artifacts be extracted?
```

---

# Evidence Integrity Checklist

```text id="9ukx0x"
[ ] Source identified
[ ] Device information recorded
[ ] Acquisition method documented
[ ] Tool documented
[ ] Tool version documented
[ ] Acquisition time recorded
[ ] Hash calculated
[ ] Hash recorded
[ ] Verification completed
[ ] Evidence stored securely
[ ] Working copy created
```

---

# Common Acquisition Mistakes

## Mistake 1 — No Documentation

An image without acquisition metadata is difficult to validate.

## Mistake 2 — No Hash

Integrity cannot be easily demonstrated.

## Mistake 3 — Modifying the Original

Analysis should generally occur on controlled working copies.

## Mistake 4 — Ignoring Volatile Evidence

Important state may disappear after shutdown.

## Mistake 5 — Incorrect Scope

Collecting the wrong system creates false confidence.

## Mistake 6 — Inadequate Storage

Large forensic images require appropriate capacity.

## Mistake 7 — Poor Access Control

Sensitive evidence should not be broadly accessible.

---

# Common Preservation Misconfigurations

### Short Retention

Important evidence disappears.

### Mutable Logs

Attackers or administrators can alter historical data.

### No Centralization

Evidence becomes fragmented.

### Unsynchronized Clocks

Timeline reconstruction becomes unreliable.

### No Audit Trail

Investigators cannot determine who accessed evidence.

### No Backup

A damaged evidence repository can destroy investigative capability.

---

# Practical Lab 01 — Disk Image Integrity

Create a test file:

```bash id="n4qjpa"
dd if=/dev/zero of=test-evidence.img bs=1M count=10
```

Calculate the hash:

```bash id="r9sqcm"
sha256sum test-evidence.img
```

Create a copy:

```bash id="z8p6a0"
cp test-evidence.img test-evidence-copy.img
```

Calculate again:

```bash id="x2w5ra"
sha256sum test-evidence-copy.img
```

Confirm that the hashes match.

This demonstrates the fundamental integrity-validation workflow.

---

# Practical Lab 02 — Evidence Modification

Create a file:

```bash id="l6s4ro"
echo "original evidence" > evidence.txt
```

Hash it:

```bash id="zv3s4w"
sha256sum evidence.txt
```

Modify it:

```bash id="qj5j5n"
echo "modified" >> evidence.txt
```

Hash it again:

```bash id="j9yd4v"
sha256sum evidence.txt
```

Observe the change.

The objective is to understand why integrity verification is important.

---

# Practical Lab 03 — Evidence Inventory

Create an evidence inventory containing:

```text id="w6lbyq"
EV-001 Disk
EV-002 Memory
EV-003 Network
EV-004 Identity
EV-005 Cloud
```

For each item document:

```text
Source
Type
Collection Time
Collector
Hash
Storage
Status
```

---

# Practical Lab 04 — Chain of Custody

Create a simulated chain-of-custody record.

Track:

```text id="cmmk4o"
Investigator A
      │
      ▼
Evidence Repository
      │
      ▼
Investigator B
      │
      ▼
Forensic Workstation
```

Document every transfer.

---

# Practical Lab 05 — Live Acquisition Planning

Scenario:

> An endpoint is actively communicating with a suspicious external system.

Determine whether you should prioritize:

```text id="0nq7dv"
Memory
Network Connections
Processes
Logged-In Users
Disk
```

Document:

1. Why you selected the order.
2. What evidence may disappear.
3. What risks the acquisition introduces.
4. What should be documented.

---

# Practical Lab 06 — Cloud Evidence Preservation

Scenario:

> A cloud identity is suspected of compromise.

Identify evidence sources:

```text id="l4g6uc"
Authentication
MFA
Session Activity
API Calls
IAM Changes
Storage Access
Network Activity
```

Then create a preservation plan.

---

# Practical Lab 07 — Container Evidence Preservation

Scenario:

> A Kubernetes workload is suspected of compromise.

Identify:

```text id="9ukc4a"
Pod
Container
Node
Image
Logs
Kubernetes Audit
Service Account
Network
Cloud Provider
```

Determine which evidence should be preserved before the workload is terminated.

---

# Practical Lab 08 — Evidence Gap Analysis

Scenario:

A disk image is available, but memory was not captured.

Determine:

```text id="uv4ylt"
What can be investigated?
What cannot be confidently determined?
What additional evidence may compensate?
What confidence level should be assigned?
```

---

# Acquisition Decision Matrix

| Situation | Possible Priority |
|---|---|
| Active malware | Volatile state + endpoint |
| Ransomware | Containment + evidence preservation |
| Suspected credential theft | Identity + endpoint + memory |
| Data exfiltration | Network + endpoint + cloud |
| Cloud compromise | Identity + API + audit logs |
| Web compromise | Application + endpoint + network |
| Insider investigation | Identity + endpoint + application |
| Lost endpoint | Identity + device + cloud |

The matrix is illustrative; actual priorities should follow organizational procedures and incident context.

---

# Evidence Preservation Decision Tree

```text id="db4cxg"
                Evidence Identified
                       │
                       ▼
             Is it highly volatile?
                 │            │
                Yes           No
                 │             │
                 ▼             ▼
        Preserve rapidly    Assess scope
                 │             │
                 └──────┬──────┘
                        ▼
                   Acquire
                        │
                        ▼
                     Hash
                        │
                        ▼
                    Verify
                        │
                        ▼
                     Store
                        │
                        ▼
               Create Working Copy
```

---

# Forensic Acquisition Record

```text id="y70xla"
# Forensic Acquisition Record

## Case Information

Case ID:
Evidence ID:

## Source

Hostname:
Asset ID:
Serial Number:
Operating System:

## Acquisition

Acquisition Type:
Tool:
Tool Version:
Operator:
Start Time:
End Time:
Time Zone:

## Output

Image Format:
Output Location:
Size:

## Integrity

Hash Algorithm:
Hash:
Verification Result:

## Notes

## Chain of Custody

## Limitations
```

---

# Chain-of-Custody Template

```text id="s8xwvb"
# Chain of Custody

Evidence ID:

Description:

Collected By:

Collection Date:

Collection Time:

Initial Location:

Initial Hash:

---

Transfer #1

From:
To:
Date:
Time:
Purpose:
Integrity Verified:

---

Transfer #2

From:
To:
Date:
Time:
Purpose:
Integrity Verified:

---

Final Storage:

Final Hash:

Notes:
```

---

# Evidence Handling Checklist

```text id="j73n6p"
[ ] Authorization confirmed
[ ] Scope confirmed
[ ] Evidence identified
[ ] Volatility assessed
[ ] Preservation initiated
[ ] Collection method selected
[ ] Source documented
[ ] Acquisition performed
[ ] Hash calculated
[ ] Hash verified
[ ] Chain of custody recorded
[ ] Evidence encrypted
[ ] Evidence access restricted
[ ] Working copy created
[ ] Original protected
[ ] Acquisition report completed
```

---

# Forensic Readiness Requirements

An organization should prepare:

### People

- Trained forensic analysts
- Incident responders
- Legal contacts
- Evidence custodians

### Process

- Acquisition procedures
- Preservation procedures
- Chain-of-custody procedures
- Evidence retention policies

### Technology

- EDR
- SIEM
- Cloud logging
- Network telemetry
- Evidence storage
- Acquisition tools

### Governance

- Authorization
- Privacy
- Retention
- Legal requirements
- Access control

---

# Enterprise Evidence Architecture

```text id="x8gk3p"
                     Enterprise
                         │
      ┌──────────────────┼──────────────────┐
      ▼                  ▼                  ▼
   Endpoint            Network             Cloud
      │                  │                  │
      ▼                  ▼                  ▼
     EDR                PCAP             Audit Logs
     Logs               DNS              IAM
     Disk               Proxy            API
     Memory             Firewall         Storage
      │                  │                  │
      └──────────────────┼──────────────────┘
                         ▼
                 Collection Layer
                         │
                         ▼
                Integrity Validation
                         │
                         ▼
                 Evidence Repository
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          Forensics   IR Team   Legal/Compliance
```

---

# Evidence Retention

Retention should account for:

- Investigation duration
- Regulatory requirements
- Legal holds
- Business requirements
- Storage costs
- Privacy
- Data sensitivity

Longer retention is not automatically better.

Retention should be risk-based and governed.

---

# Evidence Destruction

Evidence should never be casually deleted.

Where destruction is authorized, document:

```text id="3s3m0m"
Evidence ID
Authorization
Reason
Date
Method
Operator
Verification
```

Legal holds may override normal retention schedules.

---

# Privacy Considerations

Forensic evidence can contain:

- Personal information
- Credentials
- Emails
- Financial information
- Health information
- Private communications
- Customer data

Investigators should follow:

- Least privilege
- Data minimization
- Access controls
- Encryption
- Retention policies
- Legal guidance

---

# Professional Acquisition Principles

## Principle 1

> **Collect what is necessary to answer the investigative question.**

## Principle 2

> **Preserve original evidence whenever practical.**

## Principle 3

> **Document every important acquisition decision.**

## Principle 4

> **Verify evidence integrity.**

## Principle 5

> **Minimize unnecessary modification.**

## Principle 6

> **Maintain chain of custody.**

## Principle 7

> **Document limitations honestly.**

---

# Interview Questions

## 1. What is forensic acquisition?

The controlled collection of digital evidence for examination while preserving its integrity and documenting the collection process.

---

## 2. What is the difference between physical and logical acquisition?

Physical acquisition generally captures storage at a lower/block level and may include deleted or unallocated data.

Logical acquisition collects selected files, directories, or application data.

---

## 3. What is a write blocker?

A mechanism designed to prevent unintended writes to evidence media during forensic access or acquisition.

---

## 4. Why should evidence be hashed?

To provide a cryptographic integrity value that can be compared later to detect changes.

---

## 5. Does hashing prove evidence authenticity?

No.

Hashing helps verify integrity. Authenticity requires additional evidence such as acquisition records, device identification, chain of custody, and trusted collection procedures.

---

## 6. When would live acquisition be appropriate?

When volatile information such as memory, active processes, sessions, or network connections may be important to the investigation.

---

## 7. What is the primary disadvantage of live acquisition?

The collection process itself can modify system state.

---

## 8. What information belongs in a chain-of-custody record?

At minimum:

```text
Who
What
When
Where
Why
Transfer
Storage
Integrity
```

---

## 9. What is forensic imaging?

Creating a controlled representation of storage media for forensic analysis.

---

## 10. Why should analysts use working copies?

To protect original or master evidence from unnecessary modification during analysis.

---

## 11. What is forensic readiness?

The ability of an organization to efficiently preserve and collect evidence when an incident occurs.

---

## 12. Why are cloud investigations different?

Cloud environments may not expose physical infrastructure directly. Evidence is often distributed across provider APIs, identity systems, audit logs, storage, compute, and network services.

---

## 13. What is an evidence gap?

A missing or unavailable evidence source that limits what can be confidently determined.

---

## 14. What would you do if a forensic hash does not match?

Do not ignore it.

Verify:

1. The correct evidence was used.
2. The correct hash algorithm was used.
3. The storage process did not alter the evidence.
4. The original hash was recorded correctly.
5. The evidence transfer history is intact.

Then document and investigate the discrepancy.

---

# Scenario Interview Question

### Scenario

> You are investigating a compromised workstation. The system is still running. What evidence would you consider before shutting it down?

A strong answer would consider:

```text id="3x7m6y"
RAM
Running Processes
Network Connections
Logged-In Users
Open Files
Active Sessions
Temporary State
```

Then evaluate:

```text id="k8osps"
Evidence Value
      +
Threat Severity
      +
Business Impact
      +
Collection Risk
```

The goal is to make an evidence-preserving decision rather than blindly choosing "shutdown" or "keep running."

---

# Scenario Interview Question

### Scenario

> A disk image has been provided to you without a hash or acquisition record. Can you use it?

It may still contain useful information, but the evidence has a significant integrity and provenance limitation.

The investigator should:

- Document the limitation.
- Determine where the image came from.
- Identify acquisition details if available.
- Calculate a current hash.
- Avoid claiming stronger provenance than the evidence supports.
- Report the limitation.

---

# Maturity Model

## Level 1 — Ad Hoc

- Manual collection
- No standardized acquisition
- Limited documentation

## Level 2 — Repeatable

- Standard acquisition procedures
- Basic chain of custody
- Hash verification

## Level 3 — Managed

- Central evidence repository
- Formal procedures
- Dedicated forensic tooling
- Regular training

## Level 4 — Integrated

- Enterprise forensic readiness
- Automated evidence collection
- IR integration
- Cloud evidence preservation

## Level 5 — Advanced

- Rapid enterprise acquisition
- Automated preservation workflows
- Cross-domain evidence correlation
- Continuous forensic readiness validation

---

# Chapter Completion Checklist

```text id="s6d3h4"
[ ] Understand forensic acquisition
[ ] Understand evidence preservation
[ ] Understand live acquisition
[ ] Understand dead acquisition
[ ] Understand physical acquisition
[ ] Understand logical acquisition
[ ] Understand forensic imaging
[ ] Understand write blockers
[ ] Understand hashing
[ ] Understand hash verification
[ ] Understand chain of custody
[ ] Understand evidence storage
[ ] Understand working copies
[ ] Understand remote acquisition
[ ] Understand cloud evidence
[ ] Understand container evidence
[ ] Understand mobile evidence
[ ] Understand evidence retention
[ ] Understand forensic readiness
[ ] Complete disk integrity lab
[ ] Complete chain-of-custody lab
[ ] Complete evidence preservation lab
```

---

# Key Takeaways

Forensic acquisition is the foundation upon which the rest of an investigation depends.

A strong acquisition process follows:

```text id="x8k7q1"
Identify
   ↓
Prioritize
   ↓
Preserve
   ↓
Acquire
   ↓
Hash
   ↓
Verify
   ↓
Document
   ↓
Store
   ↓
Analyze Working Copy
```

The most important principles are:

- Protect the original.
- Consider volatile evidence.
- Choose acquisition methods deliberately.
- Verify integrity.
- Maintain chain of custody.
- Secure evidence.
- Document every important decision.
- Record limitations.
- Preserve enough context to make the evidence meaningful.

> **Good forensic analysis begins long before the first artifact is examined. It begins with disciplined evidence preservation and acquisition.**

---

# References

### NIST SP 800-86

Guide to Integrating Forensic Techniques into Incident Response:

https://csrc.nist.gov/publications/detail/sp/800-86/final

### NIST SP 800-61

Computer Security Incident Handling Guide:

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### SWGDE

Scientific Working Group on Digital Evidence:

https://www.swgde.org/

### The Sleuth Kit

https://www.sleuthkit.org/

### Autopsy

https://www.autopsy.com/

### Volatility Foundation

https://volatilityfoundation.org/

### CISA

https://www.cisa.gov/

### ISO/IEC 27037

Guidelines for identification, collection, acquisition, and preservation of digital evidence.

https://www.iso.org/
