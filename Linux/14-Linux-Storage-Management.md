# 14 - Linux Storage Management

# Part 1 — Storage Fundamentals, Block Devices, Partitions, MBR vs GPT, Filesystems, and Storage Architecture

---

# Introduction

Storage is one of the most critical components of every Linux system.

Whether deploying:

- Web servers
- Database servers
- Kubernetes clusters
- Cloud virtual machines
- Security appliances
- SIEM platforms
- Enterprise file servers

administrators must understand how Linux discovers, organizes, formats, and manages storage.

Proper storage management improves:

- Performance
- Reliability
- Availability
- Scalability
- Data integrity
- Disaster recovery
- Security

---

# Learning Objectives

After completing this chapter, you will understand:

- Linux storage architecture
- Block devices
- Physical and virtual disks
- Partitions
- MBR and GPT partition tables
- Filesystems
- Mount points
- Enterprise storage concepts

---

# Linux Storage Architecture

```text
Application

↓

Filesystem

↓

Logical Volume (Optional)

↓

Partition

↓

Disk

↓

Storage Controller

↓

Physical Storage
```

---

# What is Storage?

Storage is where Linux permanently stores data.

Examples include:

- Operating system files
- User files
- Databases
- Logs
- Virtual machine disks
- Containers
- Backups
- Security audit logs

Unlike RAM, storage retains data after power loss.

---

# Types of Storage

| Storage Type | Example |
|--------------|----------|
| HDD | Magnetic hard disk |
| SSD | SATA Solid-State Drive |
| NVMe SSD | PCIe NVMe drive |
| USB Storage | Flash drive |
| SAN | Storage Area Network |
| NAS | Network Attached Storage |
| Cloud Storage | Block volumes, managed disks |

---

# HDD vs SSD vs NVMe

| Feature | HDD | SSD | NVMe SSD |
|----------|-----|-----|-----------|
| Speed | Low | High | Very High |
| Moving Parts | Yes | No | No |
| Latency | High | Low | Very Low |
| Reliability | Moderate | High | High |
| Cost per GB | Lowest | Moderate | Higher |

---

# Physical vs Virtual Storage

| Physical | Virtual |
|----------|----------|
| Actual hardware disk | Hypervisor-provided virtual disk |
| Installed in server | VMware VMDK, QCOW2, VHDX, etc. |
| Direct hardware access | Abstracted by virtualization platform |

Linux manages both similarly once presented as block devices.

---

# What is a Block Device?

A **block device** stores data in fixed-size blocks.

Examples:

```text
/dev/sda

/dev/sdb

/dev/nvme0n1
```

Applications do not write directly to raw disks in most cases; they interact through filesystems layered on block devices.

---

# Character Devices vs Block Devices

| Character Device | Block Device |
|------------------|--------------|
| Stream of bytes | Fixed-size blocks |
| Keyboard | Hard disk |
| Serial port | SSD |
| Mouse | NVMe |

---

# Linux Device Files

Linux represents hardware as files.

Storage devices appear under:

```text
/dev/
```

Examples:

```text
/dev/sda

/dev/sdb

/dev/nvme0n1

/dev/vda
```

---

# Common Storage Device Naming

| Device | Description |
|----------|-------------|
| `/dev/sda` | First SCSI/SATA disk |
| `/dev/sdb` | Second SCSI/SATA disk |
| `/dev/nvme0n1` | First NVMe disk |
| `/dev/vda` | First VirtIO disk |
| `/dev/loop0` | Loop device |

---

# Viewing Storage Devices

Display block devices:

```bash
lsblk
```

Example:

```text
NAME

sda

├── sda1

├── sda2

└── sda3
```

---

# Viewing Disk Information

```bash
sudo fdisk -l
```

Provides information such as:

- Disk size
- Partition layout
- Partition type
- Sector information

---

# Storage Hierarchy

```text
Disk

↓

Partition

↓

Filesystem

↓

Mount Point

↓

Files
```

---

# What is a Partition?

A partition divides a physical disk into logical sections.

Example:

```text
Disk

├── Partition 1

├── Partition 2

└── Partition 3
```

Each partition can contain:

- A filesystem
- Swap space
- LVM physical volume
- RAID member

---

# Why Partition a Disk?

Benefits include:

- Organizing data
- Separating operating system and user data
- Simplifying backups
- Improving recovery
- Supporting multiple operating systems
- Isolating workloads

---

# Enterprise Partition Example

```text
Disk

├── EFI

├── /boot

├── /

├── /var

├── /home

└── Swap
```

This layout can improve security, manageability, and resilience.

---

# Partition Table

A partition table describes how a disk is divided.

Two primary standards:

- MBR
- GPT

---

# MBR (Master Boot Record)

MBR is the traditional partitioning scheme.

Characteristics:

- Supports disks up to approximately 2 TB.
- Supports up to four primary partitions.
- One primary partition can be extended to host multiple logical partitions.

---

# MBR Layout

```text
Disk

↓

MBR

↓

Partition Table

↓

Partitions
```

---

# GPT (GUID Partition Table)

GPT is the modern partitioning standard.

Characteristics:

- Supports disks larger than 2 TB.
- Supports many partitions (commonly up to 128 by default).
- Includes redundant metadata for improved resilience.
- Works with UEFI systems.

---

# GPT Layout

```text
Primary GPT Header

↓

Partition Entries

↓

Data

↓

Backup GPT Header
```

---

# MBR vs GPT

| Feature | MBR | GPT |
|----------|-----|-----|
| Maximum Disk Size | ~2 TB | Very large (supports modern large disks) |
| Primary Partitions | 4 | Typically 128 |
| Redundant Metadata | No | Yes |
| UEFI Support | Limited | Native |
| Legacy BIOS Support | Yes | With compatibility considerations |

---

# Choosing Between MBR and GPT

| Use Case | Recommended |
|----------|-------------|
| Modern server | GPT |
| Large disks | GPT |
| UEFI boot | GPT |
| Legacy BIOS-only system | MBR (if required) |

Most modern enterprise deployments use GPT.

---

# What is a Filesystem?

A filesystem organizes data on storage.

Without a filesystem, the operating system cannot efficiently store or retrieve files.

---

# Filesystem Responsibilities

A filesystem manages:

- File names
- Directories
- Permissions
- Metadata
- Space allocation
- Timestamps
- Journaling (where supported)

---

# Common Linux Filesystems

| Filesystem | Typical Use |
|------------|-------------|
| ext4 | General-purpose Linux |
| XFS | Enterprise servers, large filesystems |
| Btrfs | Snapshots and advanced features |
| FAT32 | Cross-platform removable media |
| exFAT | Large removable storage |
| NTFS | Windows interoperability |

---

# ext4 Filesystem

Features:

- Journaling
- Stable and mature
- Good performance
- Broad distribution support

Suitable for:

- Desktops
- Servers
- Virtual machines

---

# XFS Filesystem

Features:

- High scalability
- Efficient handling of large files
- Online filesystem growth
- Common default on many enterprise distributions

Suitable for:

- Enterprise storage
- Database servers
- Large file workloads

---

# Btrfs Filesystem

Features:

- Snapshots
- Checksums
- Compression
- Subvolumes

Common use cases:

- Development environments
- Snapshot-based recovery
- Advanced storage management

---

# Journaling Filesystems

A journaling filesystem records metadata changes before committing them.

Workflow:

```text
Write Request

↓

Journal

↓

Filesystem

↓

Completed
```

Benefits:

- Faster crash recovery
- Improved consistency after unexpected shutdowns

---

# Filesystem Comparison

| Feature | ext4 | XFS | Btrfs |
|----------|------|-----|--------|
| Journaling | ✓ | ✓ | ✓ |
| Snapshots | Limited | No (filesystem-native) | ✓ |
| Compression | No | No | ✓ |
| Online Growth | ✓ | ✓ | ✓ |

---

# Enterprise Storage Layout

```text
Physical Disk

↓

GPT

↓

Partition

↓

Filesystem

↓

Mount Point

↓

Applications
```

---

# Cybersecurity Perspective

Storage architecture has direct security implications.

Security teams consider:

- Disk encryption
- Separate partitions for logs
- Protecting audit trails
- Filesystem permissions
- Secure deletion of sensitive data
- Storage monitoring

Dedicated partitions for areas such as `/var` can help contain excessive log growth and reduce operational risk.

---

# Business Impact

Proper storage planning provides:

- Better performance
- Easier backups
- Improved disaster recovery
- Increased scalability
- Better compliance
- Simplified maintenance

Poor storage design can result in:

- Downtime
- Data loss
- Performance bottlenecks
- Operational complexity

---

# Enterprise Best Practices

- Use GPT for new deployments.
- Select filesystems based on workload requirements.
- Separate operating system, logs, and application data where appropriate.
- Monitor storage capacity regularly.
- Document partition layouts.
- Plan for future storage growth.
- Align storage design with backup and recovery objectives.

---

# Key Takeaways

- Linux represents storage devices as block devices under `/dev`.
- Partitions divide disks into logical sections.
- GPT is the preferred partition table for modern systems.
- Filesystems organize and manage stored data.
- Storage architecture directly influences performance, reliability, and security.

---


