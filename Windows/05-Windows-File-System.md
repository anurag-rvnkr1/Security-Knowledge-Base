# 05-Windows-File-System.md

# Part 1 — Windows File System Fundamentals, Storage Architecture, NTFS Introduction, FAT, exFAT, and File System Concepts

---

# Introduction

A **File System** is one of the most fundamental components of any operating system. It determines **how data is stored, organized, accessed, secured, and recovered** from storage devices.

Every document, image, executable, log file, database, registry hive, and system file stored in Windows resides within a file system.

Understanding Windows file systems is essential for:

- Windows Administration
- System Engineering
- Cybersecurity
- Digital Forensics
- Incident Response
- Malware Analysis
- Data Recovery
- Enterprise Storage Management

This chapter begins with the foundations of Windows file systems before moving into NTFS internals, permissions, metadata, journaling, forensic artifacts, and enterprise storage practices.

---

# Learning Objectives

By the end of this part, you will understand:

- What a file system is
- Why file systems are important
- Windows storage architecture
- Physical vs Logical storage
- File system terminology
- FAT
- FAT32
- exFAT
- NTFS overview
- Enterprise storage concepts

---

# What is a File System?

A **file system** is the method used by an operating system to organize and manage data stored on storage devices.

Without a file system, Windows would not know:

- Where files are located
- How folders are organized
- Which sectors belong to which file
- Who owns a file
- Which permissions apply
- Whether deleted space is reusable

---

# File System Responsibilities

A Windows file system is responsible for:

- Creating files
- Reading files
- Writing files
- Deleting files
- Organizing directories
- Managing free space
- Maintaining metadata
- Enforcing permissions
- Recovering from crashes

---

# High-Level Storage Architecture

```text
Application

↓

Windows API

↓

I/O Manager

↓

File System Driver (NTFS/FAT/exFAT)

↓

Storage Driver

↓

SSD / HDD / NVMe
```

Applications never communicate directly with disks. All storage requests pass through Windows storage components.

---

# Data Storage Journey

When a user saves a file:

```text
User Saves Document

↓

Application

↓

Windows API

↓

I/O Manager

↓

NTFS Driver

↓

Storage Driver

↓

Physical Disk

↓

Data Stored
```

---

# Physical Storage vs Logical Storage

## Physical Storage

Examples:

- SSD
- HDD
- NVMe SSD
- USB Drive
- SD Card

Physical storage refers to the actual hardware.

---

## Logical Storage

Examples:

```text
C:

D:

E:

Network Drive (Z:)
```

Logical storage represents partitions or volumes presented by the operating system.

---

# Storage Hierarchy

```text
Physical Disk

↓

Partition

↓

Volume

↓

File System

↓

Folders

↓

Files
```

---

# Important File System Terminology

| Term | Description |
|------|-------------|
| Disk | Physical storage device |
| Partition | Section of a disk |
| Volume | Formatted partition with a file system |
| Cluster | Smallest storage allocation unit |
| Sector | Smallest physical storage unit |
| File | Collection of stored data |
| Folder | Container for files and folders |
| Metadata | Information describing a file |

---

# What is a Sector?

A **sector** is the smallest physical storage unit on a disk.

Example:

```text
Disk

+-----+
|512B |
+-----+

+-----+
|512B |
+-----+

+-----+
|512B |
+-----+
```

Modern storage devices commonly use:

- 512 bytes
- 4096 bytes (4K sectors)

---

# What is a Cluster?

Windows allocates storage using **clusters** rather than individual sectors.

Example:

```text
Cluster

+-------+
|Sector |
+-------+
|Sector |
+-------+
|Sector |
+-------+
|Sector |
+-------+
```

A cluster contains one or more sectors.

---

# Cluster Allocation

Example:

```text
File Size = 3 KB

Cluster Size = 4 KB

Allocated = 4 KB

Unused = 1 KB
```

Unused space inside the allocated cluster is known as **slack space**.

---

# Slack Space

```text
4 KB Cluster

+-----------------------+

File Data

###############

Unused Space

......

+-----------------------+
```

Slack space can contain remnants of previously stored data, making it important in digital forensics.

---

# Windows File System Evolution

```text
FAT

↓

FAT16

↓

FAT32

↓

NTFS

↓

ReFS (Windows Server & Enterprise Scenarios)
```

Each generation introduced improvements in scalability, reliability, and security.

---

# FAT (File Allocation Table)

FAT was one of Microsoft's earliest file systems.

Characteristics:

- Simple design
- Minimal metadata
- Broad compatibility
- Low overhead

Limitations:

- No permissions
- No encryption
- No journaling
- Limited file size

---

# FAT32

FAT32 improved upon earlier FAT versions.

Advantages:

- Compatible with many devices
- Lightweight
- Easy implementation

Limitations:

| Limitation | Value |
|------------|-------|
| Maximum file size | 4 GB |
| Limited security | Yes |
| Journaling | No |
| Encryption | No |

FAT32 is commonly used on removable media and embedded devices.

---

# exFAT

exFAT (Extended File Allocation Table) was designed for modern flash storage.

Advantages:

- Supports large files
- Supports large volumes
- Lightweight
- Compatible across many operating systems

Common uses:

- USB flash drives
- SDXC cards
- External SSDs
- Cameras
- Multimedia devices

---

# FAT32 vs exFAT

| Feature | FAT32 | exFAT |
|----------|--------|--------|
| Max File Size | 4 GB | Very Large |
| Flash Storage Optimized | Limited | Yes |
| Journaling | No | No |
| Security Permissions | No | No |
| Cross-Platform Support | Excellent | Excellent |

---

# NTFS (New Technology File System)

NTFS is the default Windows file system for modern desktop and server installations.

It was designed for:

- Reliability
- Security
- Scalability
- Performance
- Enterprise environments

---

# NTFS Capabilities

NTFS supports:

- File permissions
- Encryption
- Compression
- Journaling
- Large volumes
- Large files
- Security descriptors
- Alternate Data Streams
- Disk quotas
- Symbolic links
- Hard links

These capabilities make NTFS suitable for enterprise workloads.

---

# Why NTFS Became the Standard

Compared to FAT-based systems, NTFS provides:

- Better crash recovery
- Strong access control
- Improved storage efficiency
- Advanced metadata management
- Enterprise-grade reliability

---

# Windows Supported File Systems

| File System | Typical Usage |
|-------------|---------------|
| FAT32 | Legacy devices, USB drives |
| exFAT | Flash drives, SD cards |
| NTFS | Windows system drives |
| ReFS | Enterprise storage and virtualization scenarios |

---

# Choosing the Right File System

| Scenario | Recommended File System |
|----------|--------------------------|
| Windows System Drive | NTFS |
| External USB (cross-platform) | exFAT |
| Legacy USB Compatibility | FAT32 |
| Enterprise Storage Spaces | ReFS (where supported) |

---

# Enterprise Example

A corporate laptop may use:

```text
Disk

↓

EFI Partition

↓

Recovery Partition

↓

NTFS (C:)

↓

User Files

↓

Applications

↓

Windows OS
```

An external drive used for collaboration across Windows and macOS systems may use exFAT for broader compatibility.

---

# Cybersecurity Perspective

The choice of file system affects security.

Examples:

| File System | Security Features |
|--------------|------------------|
| FAT32 | Minimal |
| exFAT | Minimal |
| NTFS | ACLs, EFS, auditing, ADS, quotas |
| ReFS | Integrity streams (supported scenarios), resiliency |

Security analysts often examine:

- File metadata
- Deleted files
- Slack space
- Alternate Data Streams
- File timestamps
- Access permissions

---

# Business Impact

Selecting the correct file system improves:

- Data reliability
- Storage performance
- Security
- Compliance
- Disaster recovery
- Administrative efficiency

Using an inappropriate file system can lead to reduced functionality, compatibility issues, or weakened security.

---

# Enterprise Best Practices

- Use NTFS for Windows operating system volumes.
- Use exFAT for removable media requiring cross-platform compatibility.
- Enable encryption for sensitive data.
- Monitor disk health and storage utilization.
- Back up important data regularly.
- Avoid FAT32 for enterprise system drives.
- Standardize storage configurations across managed devices.

---

# Practical Labs

## Lab 1 — Identify the File System

1. Open **File Explorer**.
2. Right-click the **C:** drive.
3. Select **Properties**.
4. Record:
   - File system
   - Capacity
   - Used space
   - Free space

---

## Lab 2 — View Disk Layout

1. Press:

```text
Windows + R
```

2. Run:

```text
diskmgmt.msc
```

Identify:

- EFI partition
- Recovery partition
- Primary NTFS partition

Observe the storage layout without making changes.

---

## Lab 3 — Examine a USB Drive

Insert a USB drive and:

1. Open **Properties**.
2. Record:
   - File system
   - Capacity
   - Allocation unit size (if available)

Discuss why FAT32, exFAT, or NTFS might have been chosen.

---

# Key Takeaways

- A file system organizes and manages stored data.
- Windows supports FAT32, exFAT, NTFS, and ReFS for different scenarios.
- NTFS is the default file system for modern Windows installations.
- Clusters are the smallest allocation units used by the file system.
- Slack space can contain remnants of previous data and is relevant to digital forensics.
- Choosing the appropriate file system improves reliability, security, and performance.

---

# Interview Questions

1. What is a file system?
2. What is the difference between a sector and a cluster?
3. What is slack space?
4. Compare FAT32, exFAT, and NTFS.
5. Why is NTFS the default Windows file system?
6. What is metadata?
7. When would you choose exFAT over NTFS?
8. Why is FAT32 still used today?
9. What are the benefits of NTFS in enterprise environments?
10. How does the file system contribute to cybersecurity?

---

# References

- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- Microsoft Learn
- Microsoft NTFS Documentation
- Microsoft ReFS Documentation
- Microsoft Storage Documentation
- Microsoft Sysinternals Documentation

---

# 05-Windows-File-System.md

# Part 2 — NTFS Architecture, Master File Table (MFT), Metadata, File Records, Directories, Journaling, and NTFS Internals

---

# Introduction

The **New Technology File System (NTFS)** is the default file system for modern Windows operating systems because it provides:

- Reliability
- Security
- High performance
- Fault tolerance
- Scalability
- Advanced metadata management

Unlike older file systems such as FAT32, NTFS treats **almost everything as a file**, including metadata describing the file system itself.

Understanding NTFS internals is essential for:

- Windows Administration
- Digital Forensics
- Incident Response
- Malware Analysis
- Storage Management
- Cybersecurity

---

# NTFS High-Level Architecture

```text
Application

↓

Windows API

↓

I/O Manager

↓

NTFS Driver

↓

NTFS Metadata

↓

Storage Driver

↓

Physical Disk
```

The NTFS driver translates file operations into disk operations while maintaining consistency and security.

---

# NTFS Internal Components

```text
NTFS Volume

├── Boot Sector
├── Master File Table (MFT)
├── MFT Mirror
├── Log File
├── Bitmap
├── Directory Indexes
├── Security Descriptors
└── User Data
```

Each component contributes to reliable storage and fast file access.

---

# NTFS Boot Sector

Every NTFS volume begins with a **boot sector**.

Responsibilities:

- Identify the partition as NTFS
- Store boot code
- Store BIOS Parameter Block (BPB)
- Record volume information
- Locate critical NTFS structures

---

# Simplified NTFS Layout

```text
+--------------------------------------+

Boot Sector

+--------------------------------------+

Master File Table (MFT)

+--------------------------------------+

MFT Mirror

+--------------------------------------+

Metadata Files

+--------------------------------------+

User Files

+--------------------------------------+

Free Space

+--------------------------------------+
```

The exact layout varies depending on volume size and usage.

---

# Master File Table (MFT)

The **Master File Table (MFT)** is the heart of NTFS.

Every file and directory on an NTFS volume has at least one corresponding MFT record.

Think of the MFT as a database containing information about everything stored on the volume.

---

# MFT Architecture

```text
Master File Table

├── File 1
├── File 2
├── File 3
├── Directory
├── System Metadata
└── ...
```

Even the MFT itself is represented as a file.

---

# Why the MFT is Important

The MFT stores information such as:

- File name
- File size
- Security information
- Timestamps
- Attributes
- Data location
- Directory relationships

Without the MFT, Windows would not know how files are organized on the disk.

---

# MFT Record Structure (Simplified)

```text
MFT Record

+---------------------------+
| Record Header             |
+---------------------------+
| Standard Information      |
+---------------------------+
| File Name                 |
+---------------------------+
| Security Descriptor       |
+---------------------------+
| Data Attribute            |
+---------------------------+
| Other Attributes          |
+---------------------------+
```

A standard MFT record is typically **1024 bytes**, although this may vary depending on formatting options.

---

# File Records

Each file receives a unique MFT record.

Example:

```text
resume.docx

↓

MFT Entry #3251

↓

Attributes

↓

Actual File Data
```

Deleting a file generally marks its MFT entry as reusable rather than immediately erasing the underlying data.

---

# Metadata

**Metadata** is "data about data."

Examples include:

| Metadata | Example |
|-----------|----------|
| File name | `report.pdf` |
| Size | 3 MB |
| Owner | User SID |
| Created | Timestamp |
| Modified | Timestamp |
| Permissions | ACL |
| Attributes | Read-only, Hidden |

Metadata enables Windows to manage files efficiently.

---

# File Attributes

NTFS stores file properties as **attributes**.

Common attributes include:

| Attribute | Purpose |
|------------|----------|
| Standard Information | Basic metadata |
| File Name | File naming information |
| Data | Actual file contents |
| Security Descriptor | Permissions |
| Index Root | Directory indexing |
| Bitmap | Allocation tracking |
| Object ID | Unique file identifier (optional) |

---

# Resident vs Non-Resident Data

Small files may be stored directly within the MFT record.

```text
MFT Entry

↓

Small File Data

↓

Stored Inside Record
```

This is known as **resident data**.

---

Large files store their contents outside the MFT.

```text
MFT Record

↓

Pointer

↓

Disk Clusters

↓

Actual File Contents
```

This is called **non-resident data**.

---

# Directories in NTFS

Directories are specialized files that maintain indexes of other files and folders.

Example:

```text
Documents

├── Resume.docx
├── Notes.txt
├── Photos
└── Projects
```

Internally, directory structures use indexed data for efficient lookups.

---

# Directory Indexing

NTFS indexes directories to improve search performance.

```text
Directory

↓

Index

↓

Locate File

↓

Open File
```

Large directories remain performant because Windows does not perform a simple sequential search for every lookup.

---

# NTFS Metadata Files

NTFS reserves several hidden metadata files.

Examples:

| Metadata File | Purpose |
|---------------|---------|
| `$MFT` | Master File Table |
| `$MFTMirr` | Backup of critical MFT records |
| `$LogFile` | Transaction journal |
| `$Bitmap` | Cluster allocation map |
| `$Boot` | Boot information |
| `$Volume` | Volume metadata |
| `$BadClus` | Bad cluster tracking |
| `$Secure` | Security descriptors |

These files are essential to NTFS operation.

---

# MFT Mirror

The **MFT Mirror** stores a copy of critical MFT records.

Purpose:

- Improve recoverability
- Support recovery from partial corruption
- Increase resilience against metadata damage

---

# NTFS Bitmap

The Bitmap tracks cluster allocation.

```text
Bitmap

1 = Used

0 = Free
```

When creating a file, NTFS consults the bitmap to locate available clusters.

---

# Journaling

NTFS is a **journaling file system**.

Before modifying critical metadata, NTFS records intended changes in the journal.

```text
Change Requested

↓

Write Journal Entry

↓

Modify Metadata

↓

Operation Complete
```

This improves recovery after unexpected shutdowns.

---

# Why Journaling Matters

Without journaling:

```text
Power Loss

↓

Incomplete Write

↓

Corrupted File System
```

With journaling:

```text
Power Loss

↓

Journal Replay

↓

Metadata Recovered
```

Journaling primarily protects **file system metadata**, not necessarily the contents of every user file.

---

# NTFS Transaction Log

The journal is stored in:

```text
$LogFile
```

It records metadata transactions such as:

- File creation
- File deletion
- File rename
- Directory updates
- Allocation changes

---

# NTFS Consistency

NTFS maintains consistency through:

- Journaling
- Metadata validation
- Recovery procedures
- Transaction logging
- Allocation tracking

These mechanisms reduce the likelihood of corruption after crashes or power failures.

---

# Enterprise Example

An employee saves a spreadsheet.

```text
Excel

↓

Windows API

↓

NTFS Driver

↓

Update MFT

↓

Journal Transaction

↓

Allocate Clusters

↓

Write Data

↓

Update Metadata

↓

Complete
```

This process ensures the file system remains consistent even if an interruption occurs during the operation.

---

# Cybersecurity Perspective

NTFS metadata is valuable during investigations.

Analysts examine:

- MFT entries
- File timestamps
- Deleted file records
- Security descriptors
- Journal information
- Directory indexes

Malware may attempt to:

- Modify timestamps
- Hide files
- Abuse Alternate Data Streams
- Manipulate metadata

Understanding NTFS internals helps detect these activities.

---

# Business Impact

NTFS internals provide:

- Faster file access
- Reliable crash recovery
- Efficient storage management
- Improved scalability
- Enhanced security
- Better forensic capabilities

These features are critical for enterprise desktops, servers, and storage systems.

---

# Enterprise Best Practices

- Use NTFS for Windows operating system volumes.
- Monitor disk health and event logs.
- Maintain adequate free disk space.
- Back up critical systems regularly.
- Protect storage devices with encryption.
- Validate storage after unexpected shutdowns.
- Avoid forcing shutdowns whenever possible.

---

# Practical Labs

## Lab 1 — Identify NTFS Metadata

1. Open **Command Prompt**.
2. Run:

```cmd
fsutil fsinfo ntfsinfo C:
```

Observe information such as:

- Bytes per sector
- Bytes per cluster
- MFT record size
- MFT start location

> Administrative privileges may be required.

---

## Lab 2 — Examine File Properties

1. Create a text file.
2. Right-click → **Properties**.
3. Record:

- Size
- Size on disk
- Created timestamp
- Modified timestamp
- Attributes

Discuss why "Size" and "Size on disk" may differ.

---

## Lab 3 — Observe Directory Growth

1. Create a new folder.
2. Add several files.
3. Observe:

- Folder size
- Number of files
- Organization

Discuss how NTFS indexes directories for efficient access.

---

# Key Takeaways

- The Master File Table (MFT) is the core database of NTFS.
- Every file and directory has at least one MFT record.
- Metadata describes files and their properties.
- NTFS stores both resident and non-resident data.
- Journaling improves file system reliability by protecting metadata.
- Hidden metadata files such as `$MFT`, `$LogFile`, and `$Bitmap` are essential to NTFS operation.

---

# Interview Questions

1. What is the Master File Table (MFT)?
2. Why is the MFT important?
3. What is metadata?
4. What is the difference between resident and non-resident data?
5. What is the purpose of `$LogFile`?
6. Why is NTFS considered a journaling file system?
7. What information is stored in a typical MFT record?
8. What is the purpose of the NTFS bitmap?
9. How does the MFT Mirror improve reliability?
10. Why is NTFS metadata valuable during forensic investigations?

---

# References

- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- Microsoft Learn
- Microsoft NTFS Technical Documentation
- Microsoft Sysinternals Documentation
- Carrier, B. *File System Forensic Analysis*

---


