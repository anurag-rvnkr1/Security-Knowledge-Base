# Disk and File-System Forensics

> **A practical enterprise guide to investigating persistent digital evidence through disk images, partitions, file systems, metadata, timestamps, deleted files, unallocated space, file carving, journaling, alternate data streams, and file-system timelines.**

---

# Overview

Disk and file-system forensics focuses on persistent evidence stored on physical or virtual storage.

Unlike memory forensics, which examines volatile runtime state, disk forensics examines information that can survive:

- Reboots
- Shutdowns
- Process termination
- Network disconnection

Typical evidence includes:

```text
Files
Directories
File Metadata
File-System Structures
Deleted Files
Unallocated Space
Partitions
Journals
Logs
Browser Data
User Documents
Application Data
Persistence Mechanisms
Operating-System Artifacts
```

A disk investigation attempts to reconstruct:

```text
What existed?
What changed?
When did it change?
Who owned it?
Where did it come from?
Was it deleted?
What other evidence is related?
```

---

# Why Disk Forensics Matters

Attackers frequently interact with persistent storage.

Examples include:

```text
Malware Files
Web Shells
Scripts
Credentials
Configuration Files
Logs
Persistence Mechanisms
Downloaded Tools
Staged Data
Archives
Deleted Evidence
```

Even when files are deleted, traces may remain within:

- File-system metadata
- Journals
- Unallocated space
- Application databases
- Backups
- Snapshots
- Endpoint telemetry

---

# Disk Forensic Architecture

```text
                     Storage Device
                           │
                           ▼
                     Partition Table
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      Partition 1      Partition 2      Partition 3
          │                │                │
          ▼                ▼                ▼
      File System      File System      File System
          │
          ▼
 ┌───────────────────────────────┐
 │ Files                         │
 │ Directories                   │
 │ Metadata                      │
 │ Journals                      │
 │ Deleted Entries               │
 │ Unallocated Space             │
 └───────────────────────────────┘
```

---

# Disk Investigation Questions

A forensic analyst should ask:

```text
What storage was present?
Which partitions existed?
Which file system was used?
Which files were created?
Which files changed?
Which files were deleted?
Which users owned them?
Which files were executed?
What persistence existed?
What artifacts support the timeline?
```

---

# Storage Evidence Types

| Evidence | Value |
|---|---|
| Full disk image | Complete storage representation |
| Partition image | Individual filesystem |
| Logical acquisition | Selected files |
| File-system metadata | File activity |
| Journals | File-system changes |
| Unallocated space | Deleted remnants |
| Slack space | Residual data |
| File contents | Direct evidence |
| Application databases | User activity |
| System files | OS activity |

---

# Physical vs Logical Evidence

## Physical Acquisition

Captures storage at the block level.

Conceptually:

```text
Physical Disk
      │
      ▼
Every Accessible Block
      │
      ▼
Forensic Image
```

Advantages:

- Deleted data
- Unallocated space
- File-system structures
- Complete storage context

---

## Logical Acquisition

Collects selected files or directories.

Example:

```text
/home/user/
```

Advantages:

- Faster
- Smaller
- Useful for targeted investigations

Limitations:

- Deleted data may be missed
- Unallocated space is generally unavailable
- File-system context may be incomplete

---

# Disk Imaging

A forensic disk image should preserve the original storage content as accurately as practical.

Common image approaches include:

```text
Raw / DD
E01
AFF / AFF4
```

Selection depends on tooling and forensic requirements.

---

# Imaging Workflow

```text
Original Storage
       │
       ▼
Write Protection
       │
       ▼
Acquisition
       │
       ▼
Forensic Image
       │
       ├── Hash
       ├── Verify
       └── Preserve
              │
              ▼
         Working Copy
              │
              ▼
           Analysis
```

---

# Write Protection

A hardware or software write blocker can help prevent accidental modification of evidence during acquisition.

Conceptually:

```text
Evidence Disk
     │
     ▼
Write Blocker
     │
     ▼
Forensic Workstation
```

The goal is to preserve evidence integrity.

---

# Hashing Disk Images

After acquisition:

```bash
sha256sum evidence.img
```

Record:

```text
Evidence ID
Image Name
Hash
Acquisition Time
Operator
Tool
Tool Version
```

---

# Hash Verification

Before analysis:

```bash
sha256sum evidence.img
```

Compare against the original recorded hash.

If the values differ:

```text
STOP
 │
 ▼
Investigate Integrity Failure
```

Do not silently continue.

---

# Hash Limitations

A matching hash demonstrates that the analyzed file matches the hashed image.

It does not automatically establish:

- Source authenticity
- Correct acquisition
- Complete acquisition
- Interpretation accuracy

---

# Partition Tables

Storage can contain partition structures.

Common partitioning concepts include:

```text
MBR
GPT
```

A forensic analyst should identify:

- Partition type
- Start sector
- End sector
- Size
- File system
- Boot information

---

# MBR

Master Boot Record is an older partitioning mechanism.

It has historical importance and remains relevant for forensic analysis of legacy systems.

---

# GPT

GUID Partition Table is widely used on modern systems.

It supports:

- Large disks
- Many partitions
- Redundant partition metadata

---

# File Systems

Important file systems include:

```text
Windows
 ├── NTFS
 └── FAT32 / exFAT

Linux
 ├── ext4
 ├── XFS
 └── Btrfs

macOS
 └── APFS
```

The exact forensic artifacts depend on the file system.

---

# NTFS

NTFS is a major Windows file system.

Important forensic structures include:

```text
MFT
USN Journal
File Attributes
Security Descriptors
Alternate Data Streams
Directory Entries
```

---

# Master File Table

The NTFS Master File Table (MFT) contains records describing files and directories.

Conceptually:

```text
MFT Record
 ├── File Name
 ├── Metadata
 ├── Attributes
 ├── Timestamps
 └── Data References
```

MFT analysis can provide important historical context.

---

# NTFS File Attributes

NTFS files can contain multiple attributes.

Examples include:

```text
$STANDARD_INFORMATION
$FILE_NAME
$DATA
```

Different metadata structures may contain different timestamp information.

---

# NTFS Timestamps

Windows forensic analysis commonly considers:

```text
Created
Modified
Accessed
Changed
```

The interpretation of timestamps depends on the artifact and Windows behavior.

---

# Important Timestamp Principle

A timestamp should never be interpreted in isolation.

Consider:

```text
File Timestamp
+
System Time
+
Time Zone
+
Application Activity
+
User Activity
+
Network Evidence
```

---

# Linux File Systems

Linux systems may use:

```text
ext4
XFS
Btrfs
```

The forensic structures differ.

For ext-family file systems, important concepts include:

- Inodes
- Directory entries
- Journaling
- Block groups
- Extended attributes

---

# Inodes

An inode stores metadata about a file.

Conceptually:

```text
Inode
 ├── Owner
 ├── Group
 ├── Permissions
 ├── Size
 ├── Timestamps
 └── Data References
```

The file name is associated through directory structures rather than being the core identity of the inode itself.

---

# File-System Metadata

Useful metadata includes:

```text
File Name
Path
Size
Owner
Group
Permissions
Timestamps
Inode / File Record
Attributes
```

---

# File Metadata Investigation

Example:

```bash
stat suspicious-file
```

Investigate:

```text
Size
Owner
Permissions
mtime
ctime
atime
```

---

# Linux Timestamps

Linux commonly exposes:

```text
atime
mtime
ctime
```

Remember:

```text
ctime ≠ ordinary file creation time
```

The meaning is generally related to inode metadata/status changes.

---

# File Creation Time

Some modern file systems may expose additional creation/birth-time information.

Availability depends on:

- File system
- Kernel
- Tool
- Mount configuration
- Acquisition method

Never assume every Linux file has a reliable creation timestamp.

---

# MACB Timeline

A common forensic timeline representation is:

```text
M — Modified
A — Accessed
C — Changed
B — Birth / Creation
```

Availability depends on the artifact and file system.

---

# Timeline Example

```text
10:01 — File created
10:02 — File modified
10:03 — File executed
10:05 — Persistence configured
10:08 — File deleted
```

The timeline becomes stronger when supported by independent artifacts.

---

# Deleted Files

Deleting a file does not always immediately destroy every trace of it.

Potential evidence may remain in:

```text
Directory Entries
File-System Metadata
Journals
Unallocated Space
Slack Space
Application Databases
Backups
Snapshots
```

---

# What Happens When a File Is Deleted?

Simplified:

```text
File
 │
 ▼
Directory Reference Removed
 │
 ▼
Blocks May Become Available
 │
 ▼
Data May Remain
 │
 ▼
Later Reused / Overwritten
```

The exact behavior depends on the file system and storage technology.

---

# Deleted File Recovery

Recovery depends on:

- File system
- Whether blocks were reused
- SSD behavior
- TRIM
- Encryption
- File fragmentation
- File-system journaling
- Available metadata

Therefore:

> Deleted does not always mean recoverable.

---

# SSD Considerations

Solid-state storage introduces additional complexity.

TRIM can make deleted blocks unavailable for traditional recovery.

Therefore:

```text
HDD
  │
  └── Deleted data may remain

SSD + TRIM
  │
  └── Recovery may be significantly reduced
```

The exact result depends on hardware, firmware, OS, and configuration.

---

# Unallocated Space

Unallocated space consists of storage not currently assigned to an active file.

It may contain remnants of:

- Deleted files
- Previous file content
- Temporary data

However, available evidence can be fragmented or overwritten.

---

# Slack Space

File slack refers broadly to unused space associated with allocated storage structures.

Historically, slack could contain remnants of previous data.

Modern storage behavior and file-system characteristics must be considered.

---

# File Carving

File carving attempts to recover files based on recognizable content structures rather than normal file-system metadata.

Conceptually:

```text
Raw Storage
    │
    ▼
Identify File Signatures
    │
    ▼
Extract Candidate Data
    │
    ▼
Validate
    │
    ▼
Recovered File
```

---

# File Carving Limitations

Carving can produce:

- Fragmented files
- False positives
- Partial files
- Duplicate content
- Files without original names

Recovered data should therefore be validated.

---

# File Signatures

Some file formats contain recognizable headers or structures.

Examples:

```text
JPEG
PDF
ZIP
PNG
Office Documents
Executable Formats
```

File carving tools use such structures to identify candidate files.

---

# Journaling

File systems may maintain journals recording changes.

Journaling can help investigators understand:

- File operations
- Metadata changes
- File-system activity

Examples include:

```text
NTFS USN Journal
ext4 Journal
```

---

# NTFS USN Journal

The Update Sequence Number Journal can contain information about changes to files and directories.

It can assist with:

```text
Creation
Deletion
Renaming
Modification
```

It is particularly valuable for reconstructing file-system activity.

---

# Journal Limitations

Journals are not complete event logs.

Consider:

- Retention
- Rotation
- Configuration
- Overwriting
- File-system behavior
- Available records

---

# Alternate Data Streams

NTFS supports Alternate Data Streams (ADS).

Conceptually:

```text
file.txt
 ├── Main Data
 └── Alternate Data Stream
```

ADS can have legitimate uses but may also require investigation when unexpected.

---

# Investigating ADS

On Windows systems, forensic tools can identify alternate streams.

A simple conceptual example:

```text
Document.txt
Document.txt:Zone.Identifier
```

The presence of an ADS is not inherently malicious.

---

# Hidden Files

Hidden attributes and unusual locations should be investigated carefully.

Examples:

```text
Hidden
System
Obfuscated Names
Unexpected Directories
Unexpected Extensions
```

Attackers may hide artifacts, but legitimate software also creates hidden files.

---

# File Extension Mismatch

A file named:

```text
report.pdf
```

may not actually be a PDF.

Investigators should consider:

```text
Filename
Extension
Magic Bytes
File Structure
Hash
Origin
```

---

# File Hashing

Hash suspicious files:

```bash
sha256sum suspicious-file
```

For Windows environments, approved forensic tools can calculate equivalent hashes.

Use hashes for:

- Evidence integrity
- Malware identification
- Duplicate detection
- IOC correlation

---

# Known-File Matching

Investigators can compare hashes against:

- Trusted software databases
- Enterprise software inventories
- Malware repositories
- Internal threat intelligence

A hash match should still be interpreted in context.

---

# File Ownership

Ownership may help determine:

```text
Who created it?
Which service owns it?
Was the location expected?
```

But ownership does not prove authorship.

---

# Permissions

Linux example:

```bash
ls -la suspicious-file
```

Windows investigations should consider:

- ACLs
- Owner
- Inheritance
- Security descriptors

---

# NTFS Security Descriptors

Security descriptors can provide:

```text
Owner
Permissions
Access Control Entries
Inheritance
```

These can be useful during insider-threat and unauthorized-access investigations.

---

# Windows File-System Investigation

A Windows disk investigation may correlate:

```text
MFT
+
USN Journal
+
Registry
+
Event Logs
+
Prefetch
+
Amcache
+
Browser Artifacts
+
User Files
```

---

# Linux File-System Investigation

A Linux disk investigation may correlate:

```text
Inodes
+
Directory Entries
+
journald
+
Auth Logs
+
Shell History
+
Cron
+
systemd
+
Application Logs
```

---

# File-System Investigation Workflow

```text
Disk Image
    │
    ▼
Validate Hash
    │
    ▼
Identify Partitions
    │
    ▼
Identify File Systems
    │
    ▼
Mount / Parse Safely
    │
    ▼
Enumerate Files
    │
    ▼
Analyze Metadata
    │
    ▼
Analyze Deleted Data
    │
    ▼
Analyze Journals
    │
    ▼
Analyze Applications
    │
    ▼
Build Timeline
    │
    ▼
Correlate
```

---

# Safe Mounting

Forensic images should be mounted in a way that prevents modification.

The investigator should:

- Use read-only access
- Preserve the original image
- Work from a verified copy
- Record mount configuration
- Avoid accidental writes

---

# Forensic File-System Tools

Common tools include:

| Tool | Purpose |
|---|---|
| Autopsy | Forensic case analysis |
| The Sleuth Kit | File-system investigation |
| FTK | Commercial forensic platform |
| EnCase | Commercial forensic platform |
| Magnet AXIOM | Commercial forensic platform |
| `fls` | File listing |
| `istat` | Metadata analysis |
| `icat` | File extraction |
| `mmls` | Partition analysis |
| `fsstat` | File-system information |
| `sha256sum` | Hashing |

Tool availability varies by environment.

---

# The Sleuth Kit

The Sleuth Kit provides command-line tools for examining disk images and file systems.

Examples include:

```bash
mmls evidence.img
```

to inspect partition structures.

And:

```bash
fsstat evidence.img
```

to examine file-system information when supported by the image and tool version.

---

# File Listing

For supported file systems, tools such as:

```bash
fls
```

can help enumerate files and directories.

Deleted entries may also be identifiable depending on file system and evidence state.

---

# Metadata Analysis

Tools such as:

```bash
istat
```

can help inspect file-system metadata.

Use the appropriate metadata identifier for the file system under investigation.

---

# File Extraction

Tools such as:

```bash
icat
```

can extract file content from supported forensic images.

Always document:

```text
Image
File-System
Metadata Identifier
Output
Hash
```

---

# Disk Forensics and Timeline Analysis

A useful model is:

```text
File-System Metadata
        +
Journal
        +
Application Logs
        +
Operating-System Logs
        +
User Activity
        ↓
     Timeline
```

---

# Evidence Correlation Example

Suppose a suspicious executable is identified.

```text
MFT:
File Created

USN:
File Modified

Event Log:
Process Executed

Network:
External Connection

EDR:
Detection

```

The combined evidence is significantly stronger than any single artifact.

---

# Common Disk Forensic Mistakes

## Modifying the Original

Never perform analysis directly against original evidence when avoidable.

## Ignoring Hashes

Integrity cannot be easily demonstrated.

## Treating Timestamps as Absolute

Clock drift and artifact semantics matter.

## Assuming Deleted Means Gone

Evidence may survive elsewhere.

## Assuming Recovery Is Guaranteed

SSD/TRIM and overwriting may prevent recovery.

## Ignoring Journals

Journals can provide important file-system context.

## Trusting File Names

Names can be misleading.

## Ignoring Time Zones

Cross-system timelines can become incorrect.

---

# Time Normalization

Record:

```text
Timestamp
Timezone
UTC Equivalent
System Time Source
```

Example:

```text
Local:
10:30 IST

UTC:
05:00 UTC
```

Use the correct timezone for the actual evidence rather than assuming.

---

# File-System Timeline Model

```text
                    Timeline
                        │
       ┌────────────────┼────────────────┐
       ▼                ▼                ▼
    File-System       Logs             Network
       │                │                │
       ▼                ▼                ▼
    Creation         Login             Connection
    Modification     Execution         Destination
    Deletion         Service           Transfer
       │                │                │
       └────────────────┼────────────────┘
                        ▼
                  Attack Narrative
```

---

# Practical Lab 01 — Disk Image Identification

## Objective

Given an authorized forensic image:

Determine:

```text
Image Format
Partition Scheme
Partitions
File Systems
Partition Sizes
```

Document:

```text
Evidence ID
Image Hash
Partition Table
File Systems
```

---

# Practical Lab 02 — File-System Investigation

Identify:

```text
User Directories
System Directories
Application Data
Temporary Directories
Logs
Persistence Locations
```

Create an evidence inventory.

---

# Practical Lab 03 — Deleted File Investigation

Identify deleted entries.

Determine:

```text
File Name
Path
Metadata
Size
Deletion Evidence
Recoverability
```

Do not assume every deleted entry can be recovered.

---

# Practical Lab 04 — Timeline Investigation

Construct:

```text
09:01 — User Login
09:03 — File Created
09:04 — File Executed
09:05 — Persistence Added
09:07 — Network Connection
09:10 — File Deleted
```

Then identify supporting artifacts for every event.

---

# Practical Lab 05 — Suspicious File Investigation

Scenario:

> A suspicious executable was discovered on an endpoint.

Investigate:

```text
File Name
Hash
Metadata
Owner
Permissions
Path
Origin
Execution Evidence
Network
Persistence
```

Then determine:

```text
Benign
Suspicious
Malicious
Unknown
```

---

# Practical Lab 06 — NTFS Investigation

Investigate:

```text
MFT
USN Journal
Prefetch
Event Logs
Registry
Browser Artifacts
```

Correlate file creation and execution.

---

# Practical Lab 07 — Linux File-System Investigation

Investigate:

```text
Inodes
File Metadata
Authentication Logs
Shell History
Cron
systemd
Temporary Files
Application Logs
```

Construct a timeline.

---

# Practical Lab 08 — Complete Disk Forensic Investigation

Scenario:

```text
Security Alert
     │
     ▼
Disk Acquisition
     │
     ▼
Suspicious File
     │
     ├── Metadata
     ├── Execution
     ├── Persistence
     ├── Network
     └── Deletion
           │
           ▼
       Timeline
           │
           ▼
        Findings
```

Answer:

1. What happened?
2. Which files were involved?
3. When were they created?
4. Were they executed?
5. Were they deleted?
6. Was persistence established?
7. Was data staged?
8. What evidence supports the conclusion?
9. What evidence is missing?

---

# Disk Forensic Investigation Report

```text
# Disk and File-System Forensic Report

## Case Information

Case ID:
Host:
Evidence ID:
Image:
Hash:
Investigator:

## Acquisition

## Storage Architecture

## Partition Analysis

## File-System Analysis

## File Metadata

## Deleted File Analysis

## Journal Analysis

## Suspicious Files

## Persistence Analysis

## Application Artifacts

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
DISK-001

Title:
Suspicious Executable Created and Later Removed

Observation:
A suspicious executable was identified through file-system artifacts. Timeline evidence indicates that the file was created, modified, and subsequently removed.

Supporting Evidence:
File-system metadata
Journal records
Endpoint telemetry
Network telemetry

Assessment:
The file lifecycle is consistent with potentially unauthorized activity.

Confidence:
Medium-High

Limitation:
The executable's complete content was not recoverable.
```

---

# Disk Forensics and Incident Response

Disk forensics supports:

```text
Detection
   ↓
Triage
   ↓
Acquisition
   ↓
Analysis
   ↓
Scope
   ↓
Eradication
   ↓
Recovery
```

Disk evidence can help determine:

- Root cause
- Persistence
- Affected files
- Malware
- User activity
- Attack timeline

---

# Disk Forensics and Threat Hunting

Forensic discoveries can become hunt hypotheses.

Example:

```text
Forensic Finding
      │
      ▼
Suspicious File Location
      │
      ▼
Search Enterprise
      │
      ▼
Identify Similar Files
      │
      ▼
Hash / Metadata Correlation
      │
      ▼
Scope Incident
```

---

# Disk Forensics and Detection Engineering

Example:

```text
Forensic Finding:
Unexpected executable in application directory

        ↓

Detection Hypothesis:
Monitor executable creation in protected directories

        ↓

Telemetry:
EDR + File Events

        ↓

Detection:
Alert on anomalous creation
```

---

# Enterprise Disk Forensics Architecture

```text
                    Security Operations
                           │
                           ▼
                      Incident Alert
                           │
                           ▼
                    Endpoint Triage
                           │
                           ▼
                    Evidence Decision
                           │
              ┌────────────┴────────────┐
              ▼                         ▼
         Disk Image                  Logical
         Acquisition                Collection
              │                         │
              └────────────┬────────────┘
                           ▼
                    Forensic Platform
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
      File System       Timeline         Artifacts
       Analysis        Analysis          Analysis
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                      Correlation
                           │
                           ▼
                        Report
```

---

# Forensic Readiness

Organizations should prepare:

```text
Approved Imaging Procedures
Write Blockers
Forensic Storage
Evidence Hashing
Case Management
Retention Policies
Logging
Time Synchronization
Endpoint Collection
Backup / Snapshot Strategy
```

---

# Evidence Retention

Retention should account for:

- Legal requirements
- Regulatory requirements
- Incident severity
- Privacy
- Storage capacity
- Business requirements

Evidence should not be retained indefinitely without a documented reason.

---

# Encryption Considerations

Disk encryption can affect acquisition and analysis.

Investigators may need:

- Live acquisition
- Recovery keys
- Enterprise key-management records
- Authorized credentials
- Cloud recovery mechanisms

Do not assume a powered-off encrypted system can be analyzed like an unencrypted disk.

---

# Cloud Storage Considerations

Modern systems may use:

```text
Cloud Disks
Snapshots
Object Storage
Virtual Machine Images
Backup Systems
```

Cloud evidence should be acquired through approved provider mechanisms where possible.

---

# Virtual Machines

Virtual machines introduce additional evidence sources:

```text
Guest Disk
Guest Memory
Hypervisor Logs
Virtual Disk Metadata
Snapshots
Host Logs
Cloud Telemetry
```

A VM investigation may therefore require both guest and infrastructure evidence.

---

# Containers

Containerized environments may have:

```text
Container Filesystem
Image Layers
Container Logs
Runtime Metadata
Host Filesystem
Orchestrator Logs
```

Container forensics is covered further in:

`08-Cloud-Container-and-Mobile-Forensics.md`

---

# File-System Evidence Confidence

## High Confidence

Multiple independent artifacts agree.

```text
MFT
+
USN
+
Event Log
+
EDR
```

## Medium Confidence

Multiple related artifacts support the finding.

## Low Confidence

A single ambiguous metadata artifact.

## Unknown

Evidence is insufficient.

---

# Interview Questions

## 1. What is disk forensics?

The forensic examination of persistent storage and its file-system structures to identify evidence of activity.

---

## 2. What is a forensic image?

A forensic representation of storage acquired for investigation while preserving evidentiary integrity.

---

## 3. What is the difference between physical and logical acquisition?

Physical acquisition captures storage at a lower/block level and may include deleted/unallocated data.

Logical acquisition collects selected files or logical objects.

---

## 4. What is NTFS?

A Windows file system with forensic artifacts such as MFT records, USN Journal, attributes, and security metadata.

---

## 5. What is an inode?

A Linux/Unix file-system structure containing metadata and references associated with a file.

---

## 6. What is unallocated space?

Storage space not currently assigned to active file-system objects.

It may contain remnants of deleted data.

---

## 7. Can deleted files always be recovered?

No.

Recovery depends on:

- Overwriting
- File-system behavior
- Fragmentation
- SSD/TRIM
- Encryption
- Storage technology

---

## 8. What is file carving?

Recovering candidate files from raw storage based on file structures rather than relying entirely on file-system metadata.

---

## 9. What is the NTFS USN Journal?

A journal that records file-system changes and can help reconstruct activity involving files and directories.

---

## 10. What is file slack?

Unused space associated with allocated storage structures that may historically contain residual data.

---

## 11. Why are timestamps dangerous to interpret?

Because they can be affected by:

- Time zones
- Clock drift
- System behavior
- Application behavior
- Metadata semantics
- Manipulation

---

## 12. What is the purpose of hashing?

To provide an integrity reference for evidence and enable comparison/correlation.

---

## 13. What is the difference between `mtime` and `ctime` on Linux?

`mtime` represents file-content modification.

`ctime` represents inode metadata/status change.

---

## 14. Why should investigators use working copies?

To preserve the original evidence and allow repeatable analysis.

---

# Scenario Interview Question

### Scenario

> A suspicious file was deleted immediately after an alert.

What evidence might remain?

```text
File-System Metadata
USN / Journal
Unallocated Space
Application Logs
EDR
Process Evidence
Network Logs
Backups
Snapshots
```

---

# Scenario Interview Question

### Scenario

> A file is named `invoice.pdf`, but the investigation suggests it may be executable.

Validate:

```text
Filename
Extension
Magic Bytes
File Structure
Hash
Execution Evidence
Origin
Network Activity
```

Never trust the extension alone.

---

# Scenario Interview Question

### Scenario

> A file's timestamp indicates suspicious activity, but the endpoint clock was incorrect.

Do not use the timestamp as absolute truth.

Correlate with:

```text
Authentication
EDR
Network
Server Logs
Domain Logs
Cloud Logs
Other Hosts
```

---

# Disk Forensics Maturity Model

## Level 1 — Basic

- Understand disk images
- Understand filesystems
- Analyze metadata

## Level 2 — Repeatable

- Standard acquisition
- Hash verification
- Timeline creation
- Deleted-file analysis

## Level 3 — Managed

- Enterprise forensic tooling
- Central evidence storage
- Standard procedures
- Case management

## Level 4 — Integrated

- Disk + memory + EDR
- SIEM correlation
- Threat hunting
- Automated artifact collection

## Level 5 — Advanced

- Enterprise forensic readiness
- Large-scale endpoint collection
- Cloud and VM integration
- Automated timeline generation
- Cross-host forensic correlation

---

# Chapter Completion Checklist

```text
[ ] Understand disk forensics
[ ] Understand physical acquisition
[ ] Understand logical acquisition
[ ] Understand forensic imaging
[ ] Understand hashing
[ ] Understand MBR
[ ] Understand GPT
[ ] Understand NTFS
[ ] Understand ext4 concepts
[ ] Understand MFT
[ ] Understand inodes
[ ] Understand file metadata
[ ] Understand timestamps
[ ] Understand MACB
[ ] Understand deleted files
[ ] Understand unallocated space
[ ] Understand slack space
[ ] Understand file carving
[ ] Understand journaling
[ ] Understand USN Journal
[ ] Understand ADS
[ ] Understand file-system timelines
[ ] Understand forensic tools
[ ] Complete disk-image lab
[ ] Complete deleted-file lab
[ ] Complete timeline lab
[ ] Complete NTFS lab
[ ] Complete Linux filesystem lab
[ ] Complete full disk investigation
```

---

# Key Takeaways

Disk forensics provides the persistent evidence necessary to reconstruct what happened on a system.

A strong investigation combines:

```text
Disk
 +
File System
 +
Metadata
 +
Journals
 +
Logs
 +
Memory
 +
Network
```

Remember:

- Preserve original evidence.
- Hash forensic images.
- Use write protection where appropriate.
- Work from verified copies.
- Understand the file system before interpreting artifacts.
- Deleted data may survive, but recovery is never guaranteed.
- SSD/TRIM can significantly affect recovery.
- File names and extensions can be misleading.
- Timestamps require context.
- Journals are valuable but incomplete.
- File metadata does not automatically prove user intent.
- Correlation produces stronger conclusions than isolated artifacts.

> **Disk forensics transforms persistent storage structures into a timeline of files, metadata, user activity, persistence, deletion, and system behavior.**

---

# References

### NIST SP 800-86 — Guide to Integrating Forensic Techniques into Incident Response

https://csrc.nist.gov/publications/detail/sp/800-86/final

### The Sleuth Kit

https://www.sleuthkit.org/

### Autopsy

https://www.autopsy.com/

### Microsoft NTFS Documentation

https://learn.microsoft.com/windows-server/storage/file-server/ntfs-overview

### Microsoft File Systems

https://learn.microsoft.com/windows/win32/fileio/file-systems

### Linux Kernel Documentation

https://docs.kernel.org/

### Linux `stat` Manual

https://man7.org/linux/man-pages/man1/stat.1.html

### Linux `find` Manual

https://man7.org/linux/man-pages/man1/find.1.html

### NIST Computer Forensics

https://www.nist.gov/itl/ssd/software-quality-group/computer-forensics-tool-testing-program-cftt

### SANS Digital Forensics

https://www.sans.org/digital-forensics/

### MITRE ATT&CK

https://attack.mitre.org/

---

> **Preserve the image. Understand the file system. Validate the metadata. Correlate the timeline. Never let a single artifact become the entire investigation.**
