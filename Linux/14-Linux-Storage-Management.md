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


# 14 - Linux Storage Management

# Part 2 — Mounting, Unmounting, `/etc/fstab`, LVM, RAID, Swap Space, and Storage Configuration

---

# Introduction

After creating partitions and filesystems, Linux must make them accessible through the directory hierarchy.

This is accomplished by:

- Mounting filesystems
- Managing persistent mounts
- Configuring Logical Volume Manager (LVM)
- Implementing RAID
- Managing swap space
- Monitoring storage utilization

These concepts are fundamental in enterprise Linux deployments.

---

# Storage Configuration Workflow

```text
Physical Disk

↓

Partition

↓

Filesystem

↓

Mount

↓

Persistent Configuration

↓

Applications
```

---

# What is Mounting?

Mounting is the process of attaching a filesystem to a directory so that users and applications can access its contents.

Without mounting, a filesystem exists on disk but is not part of the active directory tree.

---

# Mount Point

A **mount point** is an existing directory where a filesystem is attached.

Example:

```text
/

├── home

├── var

├── boot

├── data
```

If a new disk is mounted at:

```text
/data
```

its contents become accessible through:

```text
/data
```

---

# Mounting Workflow

```text
Filesystem

↓

Mount Point

↓

Mounted

↓

Accessible to Users
```

---

# Viewing Mounted Filesystems

Display mounted filesystems:

```bash
mount
```

A more modern alternative:

```bash
findmnt
```

Example output:

```text
TARGET     SOURCE

/          /dev/sda2

/home      /dev/sda3
```

---

# Viewing Block Devices

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

Useful columns include:

- NAME
- SIZE
- TYPE
- MOUNTPOINT

---

# Manually Mounting a Filesystem

Create a mount point:

```bash
sudo mkdir /data
```

Mount the filesystem:

```bash
sudo mount /dev/sdb1 /data
```

Verify:

```bash
findmnt
```

or

```bash
mount | grep /data
```

---

# Accessing Mounted Storage

After mounting:

```text
/dev/sdb1

↓

/data

↓

Files Available
```

Applications interact with `/data` rather than the underlying block device.

---

# Unmounting a Filesystem

Detach a mounted filesystem:

```bash
sudo umount /data
```

Or:

```bash
sudo umount /dev/sdb1
```

> The command is `umount` (without the first "n").

---

# Why Unmount?

Unmounting helps ensure:

- Buffered writes are flushed
- Filesystem consistency
- Safe device removal

Unmount removable storage before disconnecting it.

---

# Busy Filesystem

If unmounting fails:

```text
target is busy
```

Possible causes:

- Open files
- Current working directory inside the mount
- Running applications using the filesystem

Identify processes:

```bash
lsof +D /data
```

or

```bash
fuser -vm /data
```

Resolve the issue before retrying the unmount.

---

# Persistent Mounts

Manual mounts are generally temporary.

To mount automatically during boot, configure:

```text
/etc/fstab
```

---

# `/etc/fstab`

The `/etc/fstab` file defines filesystems that should be mounted automatically.

View it:

```bash
cat /etc/fstab
```

---

# Example `/etc/fstab` Entry

```text
UUID=1234-5678

/data

ext4

defaults

0

2
```

Each field has a specific meaning.

---

# `/etc/fstab` Fields

| Field | Description |
|--------|-------------|
| Device or UUID | Storage device identifier |
| Mount Point | Directory where filesystem is mounted |
| Filesystem | Filesystem type |
| Mount Options | Mount behavior |
| Dump | Backup utility field (usually `0`) |
| Pass | Filesystem check order during boot |

---

# Why Use UUID?

Device names may change after:

- Hardware replacement
- Virtual machine migration
- Storage controller changes

UUIDs uniquely identify filesystems and are generally preferred.

View UUIDs:

```bash
blkid
```

---

# Testing `/etc/fstab`

After editing:

```bash
sudo mount -a
```

If no errors occur, the configuration is likely valid.

Always test before rebooting.

---

# Common Mount Options

| Option | Purpose |
|---------|----------|
| `defaults` | Standard mount options |
| `ro` | Read-only |
| `rw` | Read-write |
| `noexec` | Prevent execution of binaries |
| `nosuid` | Ignore SUID/SGID bits |
| `nodev` | Do not interpret device files |

Security-sensitive filesystems often use additional restrictive mount options.

---

# Logical Volume Manager (LVM)

LVM provides flexible storage management beyond traditional partitions.

Benefits include:

- Easier resizing
- Storage pooling
- Flexible allocation
- Simplified expansion

---

# LVM Architecture

```text
Physical Disk

↓

Physical Volume (PV)

↓

Volume Group (VG)

↓

Logical Volume (LV)

↓

Filesystem

↓

Mount Point
```

---

# LVM Components

| Component | Description |
|-----------|-------------|
| PV | Physical Volume |
| VG | Volume Group |
| LV | Logical Volume |

---

# Physical Volume (PV)

A Physical Volume is a disk or partition initialized for LVM.

Create:

```bash
sudo pvcreate /dev/sdb1
```

View:

```bash
pvs
```

---

# Volume Group (VG)

A Volume Group combines one or more Physical Volumes into a storage pool.

Create:

```bash
sudo vgcreate data_vg /dev/sdb1
```

View:

```bash
vgs
```

---

# Logical Volume (LV)

Logical Volumes are allocated from a Volume Group.

Create:

```bash
sudo lvcreate -L 20G -n data_lv data_vg
```

View:

```bash
lvs
```

---

# LVM Workflow

```text
Disk

↓

PV

↓

VG

↓

LV

↓

Filesystem

↓

Mount
```

---

# Advantages of LVM

- Online expansion (supported by many filesystems)
- Flexible storage allocation
- Multiple disks in one pool
- Easier capacity management
- Better support for changing storage requirements

---

# RAID (Redundant Array of Independent Disks)

RAID combines multiple disks for one or more goals:

- Redundancy
- Performance
- Capacity

---

# RAID Goals

```text
Multiple Disks

↓

Redundancy

↓

Performance

↓

Availability
```

---

# Common RAID Levels

| RAID | Purpose |
|-------|----------|
| RAID 0 | Performance |
| RAID 1 | Mirroring |
| RAID 5 | Distributed parity |
| RAID 6 | Double parity |
| RAID 10 | Performance + redundancy |

---

# RAID 0

```text
Disk A

Disk B

↓

Striping
```

Benefits:

- High performance
- Full combined capacity

Disadvantages:

- No redundancy
- Failure of one disk results in data loss

---

# RAID 1

```text
Disk A

↓

Mirror

↓

Disk B
```

Benefits:

- Redundancy
- Improved read availability

Trade-off:

- Approximately 50% usable capacity

---

# RAID 5

```text
Disk A

Disk B

Disk C

↓

Striping + Parity
```

Benefits:

- Fault tolerance
- Efficient capacity utilization

Requires at least three disks.

---

# RAID 10

```text
Mirror

↓

Stripe
```

Combines:

- High performance
- High availability

Often used for enterprise databases and virtualization platforms.

---

# Software RAID

Linux commonly manages software RAID using:

```text
mdadm
```

Example:

```bash
sudo mdadm --detail /dev/md0
```

---

# Swap Space

Swap extends available virtual memory by using disk space when RAM becomes constrained.

It is slower than RAM and should not be considered a substitute for sufficient physical memory.

---

# Swap Workflow

```text
RAM Full

↓

Inactive Memory Pages

↓

Swap

↓

RAM Available
```

---

# Viewing Swap

Display active swap:

```bash
swapon --show
```

or

```bash
free -h
```

---

# Enabling Swap

Example:

```bash
sudo swapon /swapfile
```

Disable:

```bash
sudo swapoff /swapfile
```

---

# Monitoring Disk Usage

Filesystem usage:

```bash
df -h
```

Directory usage:

```bash
du -sh /var/log
```

These commands help identify storage consumption.

---

# Enterprise Storage Layout

```text
OS Disk

├── /

├── /boot

Data Disk

├── /var

├── /home

├── /data

Backup Disk

└── /backup
```

Separating workloads simplifies administration and improves resilience.

---

# Cybersecurity Perspective

Storage configuration can strengthen security.

Examples include:

- Mounting removable media with restrictive options.
- Isolating log directories.
- Protecting sensitive data with encryption.
- Monitoring available disk space to prevent denial-of-service conditions.
- Restricting execution on data partitions using `noexec` where appropriate.

---

# Business Impact

Well-managed storage provides:

- Improved uptime
- Easier maintenance
- Better scalability
- Faster recovery
- Reduced operational risk
- Predictable capacity planning

---

# Enterprise Best Practices

- Use UUIDs in `/etc/fstab`.
- Test `/etc/fstab` changes with `mount -a`.
- Prefer LVM for enterprise servers requiring flexible storage.
- Select RAID levels based on workload and availability requirements.
- Monitor disk and filesystem usage regularly.
- Separate application, log, and user data where appropriate.
- Document storage layouts and recovery procedures.

---

# Key Takeaways

- Mounting connects filesystems to the Linux directory hierarchy.
- `/etc/fstab` enables persistent mounts across reboots.
- LVM provides flexible storage management.
- RAID improves availability and/or performance depending on the level used.
- Swap supplements physical memory under memory pressure.
- Continuous storage monitoring is essential for reliable operations.

---

