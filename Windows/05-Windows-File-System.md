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

# 05-Windows-File-System.md

# Part 3 — NTFS Security, Alternate Data Streams (ADS), Compression, Encryption (EFS), Hard Links, Symbolic Links, Quotas, and Advanced NTFS Features

---

# Introduction

Beyond storing files efficiently, **NTFS** provides powerful enterprise features that improve:

- Security
- Data protection
- Storage efficiency
- Access control
- Administrative flexibility

These capabilities distinguish NTFS from older file systems such as FAT32 and exFAT.

Understanding these advanced features is essential for:

- Windows Administrators
- Cybersecurity Engineers
- SOC Analysts
- Incident Responders
- Digital Forensic Investigators
- Enterprise IT Teams

---

# Advanced NTFS Features

Modern NTFS supports numerous enterprise capabilities.

```text
NTFS

├── Access Control Lists (ACLs)
├── Alternate Data Streams (ADS)
├── Encrypting File System (EFS)
├── NTFS Compression
├── Disk Quotas
├── Hard Links
├── Symbolic Links
├── Junction Points
├── Sparse Files
└── Reparse Points
```

---

# NTFS Security Model

NTFS secures files using **Access Control Lists (ACLs)**.

```text
User Requests File

↓

Security Token

↓

ACL Evaluation

↓

Access Granted?

↓

Yes → Open File

No → Access Denied
```

This access check is performed by Windows before a file is opened.

---

# Access Control Lists (ACLs)

Each NTFS object can contain an ACL that specifies who is allowed or denied access.

An ACL is composed of multiple **Access Control Entries (ACEs)**.

```text
ACL

├── ACE 1
├── ACE 2
├── ACE 3
└── ACE 4
```

Each ACE defines permissions for a user or group.

---

# Common NTFS Permissions

| Permission | Description |
|------------|-------------|
| Full Control | Complete management of the file or folder |
| Modify | Read, write, delete, and modify |
| Read & Execute | View and execute files |
| Read | View file contents |
| Write | Create or modify files |
| List Folder Contents | View directory contents (folders) |

These permissions can be inherited by child objects.

---

# Permission Inheritance

Inheritance simplifies administration.

```text
Parent Folder

↓

Permissions

↓

Child Folder

↓

Child Files
```

By default, new files and folders inherit permissions from their parent unless inheritance is disabled.

---

# Effective Permissions

A user's actual access depends on:

- Direct permissions
- Group memberships
- Inherited permissions
- Explicit deny entries

Administrators should evaluate **effective permissions** rather than only reviewing individual ACL entries.

---

# Alternate Data Streams (ADS)

NTFS supports **Alternate Data Streams (ADS)**.

An ADS allows additional data to be associated with a file without changing its primary contents.

Example:

```text
Report.docx

├── Main Data Stream
└── Hidden Stream
```

The main file appears unchanged in File Explorer.

---

# ADS Concept

```text
File

↓

Primary Stream

↓

Alternate Stream

↓

Additional Data
```

Applications typically access only the primary data stream unless explicitly instructed otherwise.

---

# Legitimate Uses of ADS

Microsoft uses ADS for several purposes.

Examples include:

- Zone.Identifier (Mark of the Web)
- Application metadata
- Compatibility information

Not every ADS indicates malicious activity.

---

# Cybersecurity Perspective: ADS

Attackers have historically abused ADS to:

- Hide scripts
- Conceal malicious payloads
- Store configuration data
- Evade casual inspection

Modern security products often inspect ADS, but analysts should still consider them during investigations.

---

# Encrypting File System (EFS)

EFS provides file-level encryption on NTFS volumes.

Workflow:

```text
User Saves File

↓

EFS Encrypts File

↓

Encrypted on Disk

↓

Authorized User Opens File

↓

Automatically Decrypted
```

Encryption and decryption are generally transparent to the authorized user.

---

# EFS Characteristics

Benefits:

- File-level encryption
- User-specific protection
- Integrated with Windows
- Transparent operation

Limitations:

- Requires NTFS
- Not available on all Windows editions
- Different from BitLocker (volume-level encryption)

---

# EFS vs BitLocker

| EFS | BitLocker |
|------|-----------|
| File-level encryption | Volume-level encryption |
| Protects selected files | Protects entire drive |
| User-based access | Device-based protection |
| Requires NTFS | Works with supported Windows volumes |

Organizations often deploy BitLocker for full-disk protection and EFS only where file-level encryption is specifically required.

---

# NTFS Compression

NTFS can compress files and folders to reduce storage consumption.

```text
Original File

↓

NTFS Compression

↓

Compressed on Disk

↓

Automatic Decompression During Access
```

Compression occurs transparently.

---

# Compression Benefits

Advantages:

- Reduced disk usage
- Transparent operation
- Easy management

Potential trade-offs:

- Additional CPU usage during compression/decompression
- May not significantly reduce already compressed files (e.g., ZIP, JPEG, MP4)

---

# Sparse Files

A **sparse file** reserves logical space without physically allocating every byte.

Example:

```text
Logical File

100 GB

↓

Actual Disk Usage

5 GB
```

Sparse files are commonly used by:

- Virtual machines
- Databases
- Backup applications

---

# Hard Links

A **hard link** creates another directory entry pointing to the same file data.

```text
File A

↓

Shared Data

↑

File B
```

Characteristics:

- Same data
- Same NTFS volume
- Multiple names
- Data remains until the last hard link is removed

---

# Symbolic Links

A **symbolic link** is a special file that references another file or directory.

```text
Shortcut

↓

Target File
```

Unlike hard links, symbolic links can point to objects on different volumes.

---

# Hard Links vs Symbolic Links

| Hard Link | Symbolic Link |
|------------|---------------|
| Points directly to file data | Points to another path |
| Same volume only | Can span volumes |
| File remains while links exist | Target may become unavailable |
| More transparent to applications | Behaves like a reference |

---

# Junction Points

A **junction point** links one directory to another directory.

Example:

```text
Folder A

↓

Junction

↓

Folder B
```

Administrators use junctions to maintain compatibility with legacy software and directory layouts.

---

# Reparse Points

A **reparse point** stores special information used by the file system to redirect processing.

Used by:

- Symbolic links
- Junctions
- Mount points
- Cloud storage integrations

---

# Disk Quotas

NTFS supports disk quotas for user storage management.

Example:

```text
User Storage

↓

Quota Limit

↓

Warning Threshold

↓

Limit Reached
```

Administrators can prevent excessive disk consumption.

---

# Quota Example

| User | Quota | Used |
|------|--------|------|
| Alice | 20 GB | 12 GB |
| Bob | 20 GB | 19 GB |
| Charlie | 50 GB | 34 GB |

Quotas are especially useful on shared file servers.

---

# File Attributes

Common NTFS attributes include:

| Attribute | Purpose |
|-----------|----------|
| Read-only | Prevent accidental modification |
| Hidden | Hide from normal directory listings |
| System | Identify system files |
| Archive | Backup indicator |
| Compressed | NTFS compression enabled |
| Encrypted | EFS enabled |

---

# Enterprise Example

A finance department stores confidential payroll files.

```text
Payroll Folder

↓

NTFS ACL

↓

Only HR Group

↓

EFS Encryption

↓

Daily Backup

↓

Audit Logging
```

This layered approach provides confidentiality and accountability.

---

# Cybersecurity Perspective

Security analysts frequently investigate:

- Unauthorized ACL changes
- Suspicious ADS usage
- Symbolic link abuse
- Junction manipulation
- Quota abuse
- Unexpected encryption
- Hidden files

Threat actors may leverage advanced NTFS features to evade detection or establish persistence.

---

# Business Impact

Advanced NTFS capabilities help organizations:

- Protect sensitive data
- Reduce storage costs
- Improve regulatory compliance
- Simplify storage management
- Enhance operational security
- Support enterprise-scale file sharing

---

# Enterprise Best Practices

- Apply the principle of least privilege using NTFS permissions.
- Review ACLs regularly.
- Limit the use of EFS to approved scenarios.
- Use BitLocker for endpoint disk protection.
- Enable quotas on shared file servers where appropriate.
- Monitor for suspicious ADS and reparse point activity.
- Document and audit symbolic links and junctions on critical systems.

---

# Practical Labs

## Lab 1 — Review NTFS Permissions

1. Create a test folder.
2. Right-click → **Properties** → **Security**.
3. Observe:

- Users
- Groups
- Assigned permissions
- Inheritance status

Do not modify permissions on production folders.

---

## Lab 2 — Enable NTFS Compression

1. Create a test folder.
2. Open **Properties**.
3. Select **Advanced**.
4. Observe the **Compress contents to save disk space** option.

Do not enable compression on production data without evaluating performance implications.

---

## Lab 3 — Review Disk Quota Settings

1. Open the **Properties** of an NTFS volume.
2. Navigate to the **Quota** tab (if available).
3. Review:

- Quota status
- Default limits
- Warning thresholds

Discuss enterprise use cases for quotas.

---

# Key Takeaways

- NTFS provides advanced enterprise security and storage features.
- ACLs control access to files and folders.
- EFS encrypts individual files, while BitLocker protects entire volumes.
- Alternate Data Streams store additional information associated with files.
- Hard links, symbolic links, and junctions provide flexible file system references.
- Disk quotas help administrators manage storage usage.

---

# Interview Questions

1. What is an Access Control List (ACL)?
2. What is the difference between an ACL and an ACE?
3. What are Alternate Data Streams (ADS)?
4. How does EFS differ from BitLocker?
5. What are the advantages of NTFS compression?
6. What is a sparse file?
7. Compare hard links and symbolic links.
8. What are junction points?
9. What are reparse points?
10. Why are NTFS quotas useful in enterprise environments?

---

# References

- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- Microsoft Learn
- Microsoft NTFS Documentation
- Microsoft EFS Documentation
- Microsoft BitLocker Documentation
- Microsoft Sysinternals Documentation

---

# 05-Windows-File-System.md

# Part 4 — File System Forensics, NTFS Timestamps, File Recovery, ReFS, Enterprise Storage Best Practices, Chapter Summary, and Review

---

# Introduction

Modern Windows file systems are not only designed to store data efficiently—they also preserve valuable metadata that can be used for:

- Digital Forensics
- Incident Response
- Malware Analysis
- Insider Threat Investigations
- Compliance Auditing
- Data Recovery

Understanding how Windows records file activity helps administrators and security professionals reconstruct events after an incident.

---

# File System Forensics

**File system forensics** is the process of analyzing storage devices to determine:

- What files existed
- When files were created
- Who accessed them
- Whether they were modified
- Whether they were deleted
- Whether hidden artifacts remain

Forensic investigators rely heavily on NTFS metadata because it often survives long after normal file deletion.

---

# Digital Evidence Sources

```text
NTFS Volume

├── Master File Table (MFT)
├── $LogFile
├── $Bitmap
├── USN Change Journal
├── File Metadata
├── Security Descriptors
├── Slack Space
├── Unallocated Space
└── Windows Event Logs
```

Each source provides different pieces of evidence.

---

# NTFS Timestamps

Every NTFS file contains multiple timestamps.

The four primary timestamps are commonly referred to as **MACB**:

| Timestamp | Description |
|-----------|-------------|
| Modified (M) | File contents last changed |
| Accessed (A) | File last accessed |
| Changed (C) | Metadata last changed |
| Birth/Created (B) | File created |

These timestamps help investigators build timelines.

---

# MACB Timeline

```text
File Created

↓

Modified

↓

Metadata Updated

↓

Accessed
```

Investigators compare these values to reconstruct user activity.

---

# Timestamp Analysis Example

| Event | Time |
|--------|------|
| Created | 09:00 |
| Modified | 09:20 |
| Metadata Changed | 09:22 |
| Accessed | 10:10 |

Possible interpretation:

- File created at 09:00
- Contents edited at 09:20
- Permissions or attributes changed shortly afterward
- File opened again later

---

# Security Information in NTFS

NTFS stores security metadata such as:

- Owner SID
- Primary Group
- Discretionary ACL (DACL)
- System ACL (SACL)

This information helps determine:

- Who owned a file
- Who could access it
- Whether auditing was configured

---

# Deleted Files

Deleting a file does **not** immediately erase its contents.

Typical process:

```text
Delete File

↓

Directory Entry Removed

↓

MFT Record Marked Available

↓

Clusters Marked Free

↓

Data Remains Until Overwritten
```

This behavior allows recovery tools to restore deleted files if the data has not been overwritten.

---

# File Recovery

Successful recovery depends on factors such as:

- Time since deletion
- Disk activity
- Overwritten clusters
- File fragmentation

The longer a system continues to write data after deletion, the lower the probability of successful recovery.

---

# Unallocated Space

When a file is deleted, its clusters often become **unallocated**.

```text
Disk

+----------------------+

Allocated Data

###########

Unallocated

...........

+----------------------+
```

Unallocated space may contain:

- Deleted documents
- Images
- Executables
- Fragments of previous files

---

# Slack Space Review

Slack space exists because Windows allocates storage in clusters.

```text
Cluster

################

Unused Area

............
```

Slack space may contain remnants of previously stored information and is therefore valuable during forensic investigations.

---

# USN Change Journal

The **Update Sequence Number (USN) Change Journal** records changes to files on NTFS volumes.

It can record events such as:

- File creation
- File deletion
- Rename operations
- Security changes
- Data modification

The journal assists administrators and forensic analysts in identifying file activity.

---

# NTFS Log File

Previously introduced as:

```text
$LogFile
```

It records metadata transactions that help NTFS recover after unexpected shutdowns.

From a forensic perspective, it may also provide insight into recent file system operations.

---

# Alternate Data Streams Review

Investigators should verify whether files contain:

```text
Main File

↓

Alternate Data Stream

↓

Hidden Information
```

Although ADS has legitimate uses, unexpected streams warrant investigation.

---

# File Integrity

Organizations verify file integrity using cryptographic hashes.

Common algorithms:

| Algorithm | Typical Use |
|-----------|-------------|
| SHA-256 | Integrity verification |
| SHA-384 | High-security integrity checks |
| SHA-512 | Long-term integrity validation |

Hash values change whenever file contents change.

---

# Integrity Verification Workflow

```text
Original File

↓

SHA-256 Hash

↓

Store Hash

↓

Later Verification

↓

Match?

↓

Yes → File Unchanged

No → File Modified
```

---

# ReFS (Resilient File System)

**ReFS** was introduced for high-availability enterprise workloads.

Primary goals:

- Data integrity
- Scalability
- Fault resilience
- Automatic corruption detection

ReFS is commonly used in certain Windows Server and enterprise storage scenarios rather than as the default client operating system volume.

---

# ReFS Features

Advantages include:

- Integrity streams
- Metadata resilience
- Large volume support
- Automatic corruption detection
- Improved resiliency with supported storage technologies

---

# NTFS vs ReFS

| Feature | NTFS | ReFS |
|----------|------|------|
| Default Windows client file system | Yes | No |
| ACL support | Yes | Yes |
| EFS | Yes | No |
| Bootable client system volume | Yes | Limited/Scenario dependent |
| Integrity streams | Limited | Yes |
| Enterprise storage focus | Good | Excellent |

The exact capabilities of ReFS depend on the Windows edition and version.

---

# Enterprise Storage Architecture

Example:

```text
Windows Workstation

↓

NTFS System Drive

↓

BitLocker

↓

Network Storage

↓

Windows Server

↓

ReFS Storage Pool

↓

Enterprise Backup
```

Organizations often combine NTFS endpoints with resilient centralized storage.

---

# Backup Strategy

A common enterprise backup approach follows the **3-2-1 principle**:

- **3** copies of important data
- **2** different storage media
- **1** copy stored offsite or offline

This improves resilience against hardware failures, ransomware, and accidental deletion.

---

# File System Monitoring

Administrators commonly monitor:

- Disk utilization
- File integrity
- Permission changes
- File creation
- File deletion
- Storage health
- Unexpected encryption
- Access failures

Monitoring tools may include:

- Event Viewer
- Microsoft Defender for Endpoint
- Microsoft Sentinel
- SIEM platforms
- Enterprise endpoint monitoring tools

---

# Enterprise Example

A ransomware attack begins encrypting user documents.

```text
User Files

↓

Rapid File Modifications

↓

EDR Detects Behavior

↓

SOC Alert

↓

Endpoint Isolated

↓

Backup Restored

↓

Business Operations Resume
```

The file system plays a central role in both detection and recovery.

---

# Cybersecurity Perspective

File systems are common targets for attackers.

Threats include:

- Ransomware
- Data theft
- Timestamp manipulation
- Hidden data in ADS
- Unauthorized permission changes
- File wiping
- Metadata tampering

Defensive measures include:

- Least privilege
- File integrity monitoring
- Endpoint detection and response (EDR)
- Centralized logging
- Frequent backups
- Encryption

---

# Business Impact

A secure and well-managed file system provides:

- Reliable data storage
- Regulatory compliance
- Faster investigations
- Reduced downtime
- Improved disaster recovery
- Better operational resilience

Poor file system management can result in data loss, security breaches, and costly outages.

---

# Enterprise Best Practices

- Use NTFS for Windows operating system volumes.
- Enable BitLocker for endpoint protection.
- Monitor changes to critical files.
- Regularly review NTFS permissions.
- Maintain tested backup and recovery procedures.
- Validate storage integrity after unexpected shutdowns.
- Use cryptographic hashes to verify important files.
- Monitor for unauthorized Alternate Data Streams and suspicious file activity.

---

# Practical Labs

## Lab 1 — View File Hash

Open **PowerShell** and run:

```powershell
Get-FileHash "C:\Path\To\File.txt" -Algorithm SHA256
```

Record:

- File name
- SHA-256 hash
- Algorithm used

---

## Lab 2 — Compare File Timestamps

1. Create a new text file.
2. Edit it several times.
3. View **Properties**.

Record:

- Created
- Modified
- Accessed

Discuss how the timestamps changed.

---

## Lab 3 — Review NTFS Permissions

Select a sensitive folder.

Review:

- Owner
- Security entries
- Inheritance
- Effective access

Discuss how these permissions support enterprise security.

---

# Chapter Summary

In this chapter, you learned:

- Windows file system fundamentals
- Physical and logical storage
- Sectors and clusters
- FAT32
- exFAT
- NTFS architecture
- Master File Table (MFT)
- Metadata
- Resident and non-resident data
- Journaling
- Access Control Lists (ACLs)
- Alternate Data Streams (ADS)
- Encrypting File System (EFS)
- NTFS Compression
- Hard links
- Symbolic links
- Junction points
- Reparse points
- Disk quotas
- NTFS timestamps
- File recovery concepts
- USN Change Journal
- ReFS
- Enterprise storage best practices

These concepts provide the foundation for Windows storage management, digital forensics, cybersecurity, and enterprise administration.

---

# Key Takeaways

- NTFS is the primary Windows file system because of its security, reliability, and scalability.
- The Master File Table (MFT) stores metadata for every file and directory.
- NTFS security relies on ACLs, security descriptors, and Windows access tokens.
- Journaling helps maintain metadata consistency after unexpected failures.
- Deleted files often remain recoverable until overwritten.
- File system metadata is invaluable for forensic investigations.
- ReFS is designed for resilient enterprise storage workloads.

---

# Interview Questions

1. What information does the Master File Table (MFT) store?
2. What are the four primary NTFS timestamps (MACB)?
3. What is the purpose of the USN Change Journal?
4. Why are deleted files often recoverable?
5. What is slack space?
6. How does ReFS differ from NTFS?
7. What is the purpose of file integrity monitoring?
8. Why are cryptographic hashes important in digital forensics?
9. What are common indicators of ransomware activity at the file system level?
10. Why is NTFS preferred over FAT32 for enterprise systems?

---

# References

- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)
- Carrier, B. *File System Forensic Analysis*
- Microsoft Learn
- Microsoft NTFS Documentation
- Microsoft ReFS Documentation
- Microsoft Defender Documentation
- Microsoft Sysinternals Documentation

---

# Congratulations!

You have successfully completed **Chapter 5 – Windows File System**.

You now understand how Windows organizes, secures, stores, protects, and recovers data using NTFS and related technologies. These concepts form the foundation for Windows administration, storage management, digital forensics, and cybersecurity.

---


