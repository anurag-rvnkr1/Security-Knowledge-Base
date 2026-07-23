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

# 14 - Linux Storage Management

# Part 3 — Filesystem Management, Disk Usage Analysis, Storage Troubleshooting, Performance Optimization, and Enterprise Monitoring

---

# Introduction

Storage management does not end after creating partitions and mounting filesystems.

Enterprise Linux administrators must continuously:

- Monitor storage utilization
- Expand filesystems
- Analyze disk usage
- Detect storage failures
- Repair filesystems
- Optimize performance
- Monitor storage health
- Plan future capacity

Poor storage management can lead to:

- Application outages
- Database failures
- System crashes
- Lost log data
- Backup failures
- Security incidents

---

# Enterprise Storage Management Lifecycle

```text
Provision Storage

↓

Create Filesystem

↓

Mount

↓

Monitor Usage

↓

Optimize Performance

↓

Expand Capacity

↓

Backup

↓

Maintain

↓

Retire Storage
```

---

# Filesystem Administration

Administrators routinely perform:

- Create filesystems
- Check filesystem integrity
- Repair filesystems
- Resize filesystems
- Monitor usage
- Verify mounted storage

---

# Viewing Filesystem Information

Display mounted filesystems:

```bash
df -Th
```

Example output:

```text
Filesystem     Type   Size Used Avail Mounted on

/dev/sda2      ext4    50G  20G   28G /
```

Useful columns:

- Filesystem
- Type
- Size
- Used
- Available
- Mount Point

---

# Understanding `df`

```bash
df -h
```

Displays:

- Total size
- Used space
- Available space
- Percentage used

Example:

```text
Use%

72%
```

Administrators should monitor high utilization before it affects applications.

---

# Disk Usage Analysis with `du`

Determine directory size:

```bash
du -sh /var/log
```

Analyze subdirectories:

```bash
du -h --max-depth=1 /var
```

Example:

```text
3.5G    /var/log

5.1G    /var/lib
```

---

# `df` vs `du`

| Command | Purpose |
|----------|----------|
| `df` | Filesystem usage |
| `du` | Directory/file usage |

Both are important during storage investigations.

---

# Finding Large Files

Locate files larger than 500 MB:

```bash
find / -type f -size +500M
```

Locate files larger than 1 GB:

```bash
find / -type f -size +1G
```

Useful during emergency disk cleanup.

---

# Sorting Large Files

Example:

```bash
du -ah /var | sort -rh | head
```

Shows the largest files and directories first.

---

# Finding Large Directories

```bash
du -sh /*
```

Or:

```bash
du -h --max-depth=1 /
```

Helps identify where storage is being consumed.

---

# Filesystem Creation

Create an ext4 filesystem:

```bash
sudo mkfs.ext4 /dev/sdb1
```

Create an XFS filesystem:

```bash
sudo mkfs.xfs /dev/sdb1
```

> **Warning:** Formatting destroys existing data on the target device.

---

# Viewing Filesystem UUID

```bash
blkid
```

Example:

```text
UUID="1234-5678"
```

UUIDs are commonly referenced in `/etc/fstab`.

---

# Filesystem Labels

Assign an ext4 label:

```bash
sudo e2label /dev/sdb1 DATA
```

View label:

```bash
lsblk -f
```

Labels provide a human-readable identifier.

---

# Checking Filesystem Integrity

For ext2/3/4:

```bash
sudo fsck /dev/sdb1
```

For a filesystem that may be mounted:

```bash
sudo fsck -f /dev/sdb1
```

> Filesystem checks should generally be performed on **unmounted** filesystems or from rescue/maintenance environments unless the filesystem and tool explicitly support online checking.

---

# Filesystem Repair Workflow

```text
Filesystem Issue

↓

Unmount Filesystem

↓

Run fsck

↓

Repair Errors

↓

Mount Filesystem

↓

Verify
```

---

# XFS Repair

XFS uses a different utility:

```bash
sudo xfs_repair /dev/sdb1
```

Unlike ext filesystems, `fsck` is not the primary repair tool for XFS.

---

# Viewing Mounted Filesystems

Modern method:

```bash
findmnt
```

Example:

```text
TARGET

/

/home

/data
```

Provides a structured view of active mounts.

---

# Monitoring Disk I/O

Install the appropriate package for your distribution if necessary, then run:

```bash
iostat
```

Extended statistics:

```bash
iostat -x
```

Useful metrics include:

- Read operations
- Write operations
- Utilization
- Await time

---

# Monitoring Block Devices

Display block devices:

```bash
lsblk
```

Show filesystem details:

```bash
lsblk -f
```

---

# Monitoring Storage Health

For drives supporting SMART, install the appropriate package (commonly `smartmontools`) and run:

```bash
sudo smartctl -H /dev/sda
```

Display detailed information:

```bash
sudo smartctl -a /dev/sda
```

SMART can help identify signs of impending hardware failure.

---

# Storage Performance Factors

Performance depends on:

- Storage type
- Filesystem
- RAID level
- Queue depth
- Workload pattern
- Controller performance
- Available memory

---

# Sequential vs Random I/O

| Sequential I/O | Random I/O |
|----------------|------------|
| Large continuous reads/writes | Small scattered reads/writes |
| Efficient for backups | Common in databases |
| Higher throughput | Higher latency |

---

# Storage Performance Workflow

```text
Application

↓

Filesystem

↓

Storage Driver

↓

Disk Controller

↓

Physical Storage
```

Each layer can affect performance.

---

# Capacity Planning

Administrators should monitor:

- Used space
- Growth trends
- Backup requirements
- Application expansion
- Available free space

Capacity planning helps prevent unexpected outages.

---

# Storage Threshold Example

| Usage | Recommendation |
|--------|----------------|
| Below 70% | Normal monitoring |
| 70–85% | Review growth |
| Above 85% | Plan expansion |
| Above 95% | Immediate action |

Thresholds vary by organization and workload.

---

# Log File Growth

Large log files commonly consume storage.

Review:

```bash
du -sh /var/log
```

List log files:

```bash
find /var/log -type f
```

Ensure log rotation is configured appropriately.

---

# Storage Monitoring Workflow

```text
Filesystem

↓

Disk Usage

↓

Threshold Alert

↓

Investigation

↓

Cleanup or Expansion

↓

Verification
```

---

# Enterprise Storage Monitoring

Organizations commonly monitor:

- Disk usage
- Filesystem utilization
- Disk latency
- SMART status
- I/O performance
- RAID health
- LVM usage
- Capacity growth

Monitoring platforms generate alerts before critical thresholds are reached.

---

# Enterprise Case Study

## `/var` Filesystem Full

Symptoms:

- Services fail
- Logs stop writing
- Package installation errors
- Application instability

Investigation:

```text
Check df

↓

Check du

↓

Locate Large Files

↓

Review Logs

↓

Clean or Archive

↓

Verify Free Space
```

Resolution:

- Remove unnecessary files
- Archive old logs
- Confirm adequate free space
- Investigate the root cause of excessive growth

---

# Enterprise Case Study

## Storage Expansion

An application requires an additional 500 GB.

Workflow:

```text
Add New Disk

↓

Extend LVM (if used)

↓

Grow Filesystem

↓

Verify Capacity

↓

Update Documentation
```

Modern filesystems and LVM often support online expansion, depending on the filesystem and deployment.

---

# Cybersecurity Perspective

Storage monitoring supports security by helping detect:

- Unexpected log growth
- Malware creating large files
- Ransomware encrypting large numbers of files
- Unauthorized data collection
- Storage-based denial-of-service attempts

Security teams should monitor abnormal storage activity alongside traditional system metrics.

---

# Business Impact

Effective filesystem management provides:

- Higher availability
- Better application performance
- Reduced downtime
- Predictable storage growth
- Lower maintenance costs
- Faster incident response

---

# Enterprise Best Practices

- Monitor storage usage continuously.
- Configure alerts before filesystems become critically full.
- Use filesystem labels and UUIDs consistently.
- Verify filesystem integrity during scheduled maintenance.
- Rotate and archive logs appropriately.
- Monitor SMART health for physical disks.
- Plan capacity growth before storage exhaustion occurs.
- Document storage changes and expansion procedures.

---

# Key Takeaways

- `df` reports filesystem utilization, while `du` measures directory usage.
- `find` can identify unusually large files consuming storage.
- Filesystem integrity tools vary by filesystem type (`fsck` for ext filesystems, `xfs_repair` for XFS).
- Performance monitoring and capacity planning are essential in enterprise environments.
- Continuous storage monitoring improves reliability, security, and operational resilience.

---

# 14 - Linux Storage Management

# Part 4 — Practical Labs, Enterprise Case Studies, Chapter Summary, Interview Questions, and References

---

# Introduction

Linux storage management is a critical skill for:

- Linux System Administrators
- DevOps Engineers
- Cloud Engineers
- Database Administrators
- Storage Engineers
- SOC Analysts
- Security Engineers
- Incident Responders

Every enterprise relies on stable, scalable, and secure storage infrastructure to ensure application availability and data integrity.

---

# Enterprise Storage Lifecycle

```text
Storage Planning

↓

Provision Storage

↓

Partition Disk

↓

Create Filesystem

↓

Mount Filesystem

↓

Configure Persistence

↓

Monitor Usage

↓

Expand Capacity

↓

Backup

↓

Retire Storage
```

---

# Practical Lab 1 — Identify Storage Devices

Display all block devices:

```bash
lsblk
```

Display detailed partition information:

```bash
sudo fdisk -l
```

### Objectives

- Identify disks and partitions
- Observe mount points
- Review storage sizes

---

# Practical Lab 2 — View Filesystem Usage

Display filesystem utilization:

```bash
df -h
```

Display filesystem type:

```bash
df -Th
```

### Questions

- Which filesystem has the highest usage?
- Which mount point has the least free space?

---

# Practical Lab 3 — Analyze Directory Usage

Check the size of `/var`:

```bash
du -sh /var
```

Analyze first-level directories:

```bash
du -h --max-depth=1 /
```

### Objectives

- Locate large directories
- Understand storage distribution

---

# Practical Lab 4 — Locate Large Files

Find files larger than 1 GB:

```bash
find / -type f -size +1G
```

Sort large files:

```bash
du -ah / | sort -rh | head -20
```

### Objectives

- Identify storage-consuming files
- Practice emergency disk cleanup

---

# Practical Lab 5 — View Mounted Filesystems

Display mounted filesystems:

```bash
findmnt
```

Alternative:

```bash
mount
```

### Objectives

- Review mount points
- Verify active filesystems

---

# Practical Lab 6 — Create a Filesystem

Create an ext4 filesystem:

```bash
sudo mkfs.ext4 /dev/sdb1
```

Create an XFS filesystem:

```bash
sudo mkfs.xfs /dev/sdb1
```

> **Warning:** Perform this only on test disks. Formatting permanently erases existing data.

---

# Practical Lab 7 — Mount and Unmount a Filesystem

Create a mount point:

```bash
sudo mkdir /data
```

Mount:

```bash
sudo mount /dev/sdb1 /data
```

Verify:

```bash
findmnt
```

Unmount:

```bash
sudo umount /data
```

### Objectives

- Mount and unmount filesystems safely
- Verify successful operations

---

# Practical Lab 8 — View UUID Information

Display UUIDs:

```bash
blkid
```

Compare with:

```bash
cat /etc/fstab
```

### Objectives

- Understand persistent storage identifiers
- Review filesystem configuration

---

# Practical Lab 9 — Validate `/etc/fstab`

Edit carefully using your preferred editor, then test:

```bash
sudo mount -a
```

### Objectives

- Verify persistent mount configuration
- Detect syntax errors before reboot

---

# Practical Lab 10 — Explore LVM

Display Physical Volumes:

```bash
pvs
```

Display Volume Groups:

```bash
vgs
```

Display Logical Volumes:

```bash
lvs
```

### Objectives

- Understand LVM hierarchy
- Review available storage pools

---

# Practical Lab 11 — Review RAID

Display RAID details (if configured):

```bash
cat /proc/mdstat
```

Detailed information:

```bash
sudo mdadm --detail /dev/md0
```

### Objectives

- Identify RAID arrays
- Review synchronization status

---

# Practical Lab 12 — Monitor Swap

Display swap:

```bash
swapon --show
```

View memory and swap:

```bash
free -h
```

### Objectives

- Understand swap utilization
- Compare RAM and swap usage

---

# Practical Lab 13 — Check Filesystem Integrity

For ext filesystems:

```bash
sudo fsck /dev/sdb1
```

For XFS:

```bash
sudo xfs_repair /dev/sdb1
```

> **Note:** Perform integrity checks on unmounted filesystems or during maintenance windows unless the filesystem supports online operations.

---

# Practical Lab 14 — Monitor Disk Health

Display SMART health:

```bash
sudo smartctl -H /dev/sda
```

Detailed information:

```bash
sudo smartctl -a /dev/sda
```

### Objectives

- Detect potential hardware failures
- Review disk health indicators

---

# Practical Lab 15 — Storage Performance

Display I/O statistics:

```bash
iostat
```

Extended statistics:

```bash
iostat -x
```

### Objectives

- Review disk utilization
- Identify storage bottlenecks

---

# Storage Troubleshooting Checklist

| Check | Command |
|--------|---------|
| View disks | `lsblk` |
| View partitions | `fdisk -l` |
| Filesystem usage | `df -h` |
| Directory usage | `du -sh` |
| Mounted filesystems | `findmnt` |
| UUIDs | `blkid` |
| LVM status | `pvs`, `vgs`, `lvs` |
| RAID status | `cat /proc/mdstat` |
| SMART health | `smartctl` |
| Swap | `swapon --show` |

---

# Enterprise Case Study 1

# Filesystem Reaches 100%

### Symptoms

- Applications stop writing data
- Package installation fails
- Logging stops
- Services become unstable

### Investigation

```text
Run df

↓

Run du

↓

Locate Large Files

↓

Review Log Growth

↓

Archive or Remove Data

↓

Verify Free Space
```

### Root Cause

Uncontrolled application log growth.

### Resolution

- Rotate logs
- Archive old files
- Monitor filesystem usage
- Configure storage alerts

---

# Enterprise Case Study 2

# Disk Failure in RAID

### Investigation

```text
Alert

↓

Review RAID Status

↓

Identify Failed Disk

↓

Replace Disk

↓

Rebuild Array

↓

Verify Health
```

### Business Benefit

RAID redundancy maintains service availability while replacing failed hardware.

---

# Enterprise Case Study 3

# Production Storage Expansion

### Scenario

A database server approaches storage limits.

### Workflow

```text
Provision New Disk

↓

Extend Volume Group

↓

Extend Logical Volume

↓

Grow Filesystem

↓

Verify Capacity

↓

Update Documentation
```

### Outcome

- Minimal downtime
- Increased storage capacity
- Continued application availability

---

# Enterprise Case Study 4

# Unexpected Storage Consumption

### Investigation

```text
Alert

↓

Review df

↓

Review du

↓

Find Large Files

↓

Review Running Processes

↓

Identify Root Cause

↓

Resolve
```

### Findings

- Debug logs left enabled
- Temporary files not cleaned
- Backup retention exceeded policy

---

# Common Storage Problems

| Problem | Possible Cause |
|----------|----------------|
| Filesystem full | Large files or uncontrolled log growth |
| Cannot mount filesystem | Incorrect filesystem, damaged metadata, or configuration issue |
| Device busy during unmount | Open files or active processes |
| Slow disk performance | High I/O load or hardware limitations |
| RAID degraded | Disk failure |
| LVM volume full | Insufficient free space in the Volume Group |
| Filesystem corruption | Improper shutdown or hardware issues |
| Swap heavily used | Memory pressure or insufficient RAM |

---

# Enterprise Monitoring Metrics

| Metric | Importance |
|----------|------------|
| Disk utilization | Capacity planning |
| Free space | Prevent outages |
| I/O latency | Performance monitoring |
| RAID health | High availability |
| SMART status | Hardware reliability |
| Filesystem growth | Trend analysis |
| Swap usage | Memory health |
| Mount status | Operational readiness |

---

# Cybersecurity Perspective

Storage monitoring is an important security capability.

Security teams monitor:

- Unexpected filesystem growth
- Unauthorized storage devices
- Log tampering
- Sensitive data exposure
- Malware creating large files
- Ransomware activity
- Audit log availability

Full filesystems can also disrupt security controls by preventing logs from being written.

---

# Business Impact

Well-managed storage provides:

- Reliable application performance
- Predictable capacity growth
- Faster recovery from failures
- Better regulatory compliance
- Reduced operational risk
- Improved business continuity

Poor storage management can result in:

- Service outages
- Data loss
- Failed backups
- Increased recovery time
- Customer impact

---

# Enterprise Best Practices

- Standardize partition and filesystem layouts.
- Prefer GPT for modern systems.
- Use UUIDs for persistent mounts.
- Monitor disk usage continuously.
- Configure proactive storage alerts.
- Rotate and archive logs according to policy.
- Test backup and recovery procedures regularly.
- Document all storage changes.
- Validate RAID health during routine maintenance.
- Review SMART data periodically for early hardware failure detection.

---

# Chapter Summary

In this chapter, you learned:

- Linux storage architecture
- Block devices
- Partitions
- MBR vs GPT
- Filesystems
- Mounting and unmounting
- `/etc/fstab`
- LVM fundamentals
- RAID concepts
- Swap management
- Disk usage analysis
- Filesystem integrity
- Storage monitoring
- Enterprise storage best practices
- Cybersecurity considerations

---

# Interview Questions

## Beginner

1. What is a block device?
2. What is a partition?
3. What is the difference between MBR and GPT?
4. What is a filesystem?
5. What does the `mount` command do?
6. What is `/etc/fstab` used for?
7. What is swap space?
8. What is the purpose of `df`?
9. What is the purpose of `du`?
10. What is the difference between HDD, SSD, and NVMe?

---

## Intermediate

1. Explain the Linux storage hierarchy.
2. Compare ext4, XFS, and Btrfs.
3. What are the advantages of LVM?
4. Explain the purpose of UUIDs.
5. How does RAID 1 differ from RAID 5?
6. How would you troubleshoot a full filesystem?
7. What does `fsck` do?
8. How do you identify large files consuming storage?
9. What information does `lsblk` provide?
10. Explain persistent filesystem mounting.

---

## Advanced

1. Design an enterprise storage layout for a database server.
2. Describe the steps to safely expand an LVM-backed filesystem.
3. Explain the role of RAID in high availability.
4. How would you investigate filesystem corruption?
5. Design a storage monitoring strategy for Linux servers.
6. Explain the importance of separating application, log, and user data.
7. How would you respond to repeated storage exhaustion alerts?
8. Discuss the security implications of filesystem mount options.
9. Explain how SMART monitoring contributes to preventive maintenance.
10. Describe best practices for enterprise backup and recovery integration.

---

# Key Takeaways

- Linux storage is organized through block devices, partitions, filesystems, and mount points.
- GPT is the preferred partitioning scheme for modern systems.
- LVM provides flexible storage allocation and expansion.
- RAID improves availability and/or performance depending on the chosen level.
- Continuous monitoring of capacity, performance, and disk health is essential.
- Storage management is a foundational operational and security responsibility.

---

# References

## Official Documentation

- `man lsblk`
- `man mount`
- `man umount`
- `man fstab`
- `man blkid`
- `man mkfs`
- `man fsck`
- `man xfs_repair`
- `man pvcreate`
- `man vgcreate`
- `man lvcreate`
- `man mdadm`
- `man swapon`
- `man smartctl`
- `man iostat`

## Standards & Best Practices

- Red Hat Enterprise Linux Storage Administration Guide
- Ubuntu Server Storage Documentation
- Arch Linux Wiki – Storage
- Linux Foundation Documentation
- NIST SP 800-88 (Media Sanitization)
- NIST SP 800-209 (Storage Security Guidance)
- CIS Linux Benchmarks
- Vendor documentation for enterprise storage arrays and RAID controllers

---

# Next Chapter

➡️ **15-Linux-Shell-and-Bash-Scripting.md**

## Topics Covered

- Shell Fundamentals
- Types of Shells
- Bash Basics
- Environment Variables
- Shell Expansion
- Input and Output Redirection
- Pipes
- Command Substitution
- Bash Scripting
- Variables and Data Types
- Conditional Statements
- Loops
- Functions
- Error Handling
- Practical Automation
- Enterprise Scripting Best Practices
- Practical Labs
- Interview Questions
- References