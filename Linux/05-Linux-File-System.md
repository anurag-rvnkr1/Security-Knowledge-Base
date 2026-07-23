# 05 - Linux File System

# Part 1 — Linux Filesystem Overview, Filesystem Hierarchy Standard (FHS), Directory Structure, File Types, and Path Management

---

# Introduction

One of the most distinguishing characteristics of Linux is its **unified filesystem**. Unlike some operating systems that expose separate drive letters (for example, `C:` or `D:`), Linux organizes everything into a **single hierarchical directory tree** beginning at the **root directory (`/`)**.

In Linux, almost everything is represented as a file:

- Regular files
- Directories
- Storage devices
- Network sockets
- Pipes
- Processes (through virtual filesystems)
- Hardware interfaces

This design provides a consistent method for accessing system resources and simplifies administration.

Understanding the Linux filesystem is essential for:

- Linux Administration
- DevOps
- Cloud Engineering
- Cybersecurity
- Digital Forensics
- Incident Response
- Malware Analysis
- System Troubleshooting

---

# Learning Objectives

After completing this chapter, you will be able to:

- Explain Linux filesystem architecture.
- Understand the Filesystem Hierarchy Standard (FHS).
- Navigate the Linux directory structure.
- Identify different Linux file types.
- Understand absolute and relative paths.
- Explain mount points.
- Apply enterprise filesystem best practices.

---

# What is a Filesystem?

A **filesystem** is the method used by an operating system to organize, store, retrieve, and manage data on storage devices.

The filesystem determines:

- How files are stored
- How directories are organized
- How permissions are maintained
- How metadata is tracked
- How free space is managed

Without a filesystem, data stored on disks would be unusable.

---

# Responsibilities of a Filesystem

A filesystem manages:

- File creation
- File deletion
- Directory organization
- Metadata
- Access permissions
- Storage allocation
- File lookup
- Data integrity

---

# Linux Filesystem Architecture

```text
Applications

↓

Virtual File System (VFS)

↓

Filesystem Driver

↓

Storage Device

↓

SSD / HDD / NVMe
```

Applications interact with files through the Virtual File System (VFS), which abstracts the underlying filesystem implementation.

---

# Unified Directory Tree

Linux organizes all files under a single directory tree.

```text
               /

        Root Directory

       /     |      \

    home    etc    var

      |

   anurag

      |

Documents
```

Every mounted storage device becomes part of this unified hierarchy.

---

# Root Directory (/)

The **root directory (`/`)** is the highest level of the Linux filesystem.

Every file and directory ultimately resides beneath it.

Example:

```text
/

├── bin

├── etc

├── home

├── usr

└── var
```

The root directory should not be confused with the **root user**.

---

# Filesystem Hierarchy Standard (FHS)

The **Filesystem Hierarchy Standard (FHS)** defines the purpose and organization of directories in Linux.

Benefits:

- Consistency across distributions
- Simplified administration
- Improved software compatibility
- Easier automation
- Predictable directory locations

Most major Linux distributions generally follow the FHS.

---

# High-Level Directory Layout

```text
/

├── bin
├── boot
├── dev
├── etc
├── home
├── lib
├── media
├── mnt
├── opt
├── proc
├── root
├── run
├── sbin
├── srv
├── sys
├── tmp
├── usr
└── var
```

Each directory has a specific purpose.

---

# /bin

Contains essential user commands required for booting and basic system operation.

Examples:

```text
ls

cp

mv

cat

echo
```

On many modern distributions, `/bin` is implemented as a symbolic link to `/usr/bin`.

---

# /sbin

Contains essential system administration commands.

Examples:

```text
fsck

reboot

shutdown

mount
```

Modern distributions may link `/sbin` to `/usr/sbin`.

---

# /boot

Contains files required during the boot process.

Typical contents:

```text
vmlinuz

initramfs

grub/

System.map
```

Loss or corruption of this directory may prevent the system from booting.

---

# /dev

Contains **device files** representing hardware and virtual devices.

Examples:

```text
/dev/sda

/dev/null

/dev/random

/dev/tty

/dev/nvme0n1
```

These special files provide a uniform interface to devices.

---

# /etc

Stores system-wide configuration files.

Examples:

```text
passwd

shadow

fstab

hosts

ssh/
```

Applications typically read configuration from `/etc` during startup.

---

# /home

Contains personal directories for regular users.

Example:

```text
/home/

├── alice

├── bob

└── anurag
```

User documents, downloads, and personal configuration files are generally stored here.

---

# /root

Home directory of the **root** user.

Example:

```text
/root
```

This directory is separate from `/home` and is intended for the superuser.

---

# /lib and /lib64

Contain essential shared libraries and kernel modules required by programs in `/bin` and `/sbin`.

Examples:

```text
libc.so

libpthread.so
```

On many systems, these directories are merged into the `/usr` hierarchy.

---

# /usr

Contains the majority of user applications and read-only program resources.

Common subdirectories include:

```text
/usr/bin

/usr/lib

/usr/share

/usr/local
```

The `/usr` hierarchy is central to most Linux software installations.

---

# /usr/local

Reserved for locally installed software that is not managed by the distribution's package manager.

Example:

```text
/usr/local/bin

/usr/local/lib
```

This separation helps preserve locally installed applications during system updates.

---

# /var

Contains variable data that changes during normal system operation.

Examples:

```text
Logs

Mail

Databases

Caches

Print Queues
```

Important subdirectories:

```text
/var/log

/var/cache

/var/lib

/var/tmp
```

---

# /tmp

Stores temporary files.

Characteristics:

- Readable by all users (with sticky bit protection on most systems)
- Often cleared automatically during reboot or cleanup routines
- Intended for short-lived data

Applications should not rely on files in `/tmp` for long-term storage.

---

# /proc

A virtual filesystem providing information about running processes and kernel state.

Examples:

```text
/proc/cpuinfo

/proc/meminfo

/proc/version

/proc/1
```

Files under `/proc` are generated dynamically and do not occupy traditional disk storage.

---

# /sys

Provides information about devices, drivers, and the Linux kernel through the **sysfs** virtual filesystem.

Examples:

```text
/sys/class

/sys/block

/sys/devices
```

It is widely used by system management tools.

---

# /run

Contains volatile runtime information created after boot.

Examples:

- Process IDs (PID files)
- Runtime sockets
- Lock files

The contents are typically stored in memory and recreated on every boot.

---

# /media

Automatically mounted removable media.

Examples:

```text
USB Drives

DVDs

External Hard Drives
```

Desktop environments commonly mount removable devices here.

---

# /mnt

Traditionally used for temporary manual mounts.

Example:

```bash
sudo mount /dev/sdb1 /mnt
```

Administrators often use `/mnt` during maintenance or recovery tasks.

---

# /srv

Intended for data served by network services.

Examples:

```text
Web Content

FTP Files

Application Data
```

Usage varies between distributions and deployments.

---

# Directory Purpose Summary

| Directory | Primary Purpose |
|-----------|-----------------|
| `/` | Root of the filesystem |
| `/bin` | Essential user commands |
| `/boot` | Bootloader and kernel files |
| `/dev` | Device files |
| `/etc` | Configuration files |
| `/home` | User home directories |
| `/root` | Root user's home |
| `/usr` | User applications and libraries |
| `/var` | Variable data |
| `/tmp` | Temporary files |
| `/proc` | Process and kernel information |
| `/sys` | Device and kernel interfaces |
| `/run` | Runtime system data |
| `/media` | Removable media |
| `/mnt` | Temporary mount points |
| `/srv` | Service data |

---

# Linux File Types

Linux supports multiple file types.

| Symbol | File Type |
|---------|-----------|
| `-` | Regular file |
| `d` | Directory |
| `l` | Symbolic link |
| `c` | Character device |
| `b` | Block device |
| `p` | Named pipe (FIFO) |
| `s` | Socket |

These symbols appear as the first character in `ls -l` output.

---

# Regular Files

Examples:

```text
notes.txt

report.pdf

script.sh

photo.jpg
```

Regular files store user or application data.

---

# Directories

Directories organize files into a hierarchical structure.

Example:

```text
Projects/

Assignments/

Downloads/
```

Directories can contain both files and other directories.

---

# Device Files

Examples:

```text
/dev/null

/dev/zero

/dev/sda
```

These special files provide interfaces to hardware or virtual devices.

---

# Symbolic Links

A symbolic link (soft link) references another file or directory.

Example:

```text
/bin → /usr/bin
```

Unlike hard links, symbolic links can reference directories and files on different filesystems.

---

# Absolute Paths

An **absolute path** begins at the root directory (`/`).

Examples:

```text
/etc/passwd

/home/anurag/Documents

/usr/bin/python3
```

Absolute paths always identify the same location regardless of the current working directory.

---

# Relative Paths

A **relative path** is interpreted relative to the current working directory.

Example:

```text
Documents/report.txt
```

Relative paths are shorter and convenient when working within a directory hierarchy.

---

# Path Symbols

| Symbol | Meaning |
|----------|---------|
| `.` | Current directory |
| `..` | Parent directory |
| `~` | Current user's home directory |
| `/` | Root directory |

Examples:

```bash
cd ..
cd ~
pwd
```

---

# Cybersecurity Perspective

A strong understanding of the filesystem hierarchy helps security professionals:

- Locate log files quickly.
- Investigate malware persistence.
- Analyze user activity.
- Identify unauthorized files.
- Understand application storage locations.
- Perform filesystem forensics.

Many attacks rely on modifying configuration files or placing malicious files in predictable directories.

---

# Business Impact

A standardized filesystem layout enables organizations to:

- Simplify system administration.
- Improve automation.
- Accelerate troubleshooting.
- Reduce configuration errors.
- Support consistent enterprise deployments.

---

# Enterprise Best Practices

- Follow the Filesystem Hierarchy Standard (FHS).
- Store configuration files in `/etc`.
- Keep application binaries under package-managed directories or `/usr/local` as appropriate.
- Separate user data from operating system files.
- Monitor critical directories such as `/boot`, `/etc`, and `/var/log`.
- Restrict permissions on sensitive configuration files.
- Document custom filesystem layouts.

---

# Key Takeaways

- Linux organizes all files under a single hierarchical directory tree.
- The root directory (`/`) is the starting point of the entire filesystem.
- The Filesystem Hierarchy Standard (FHS) defines the purpose of major directories.
- Linux supports multiple file types, including regular files, directories, device files, and symbolic links.
- Understanding directory structure is fundamental for Linux administration, security, and troubleshooting.

---


# Part 2 — Inodes, Superblocks, File Metadata, Hard Links, Symbolic Links, Directory Internals, and Filesystem Navigation

---

# Introduction

When users create a file, they usually think only about its name and contents.

Internally, however, Linux stores significantly more information:

- File metadata
- Storage block locations
- Ownership
- Permissions
- Timestamps
- File size
- Links
- Filesystem metadata

Understanding these internal structures is essential for:

- Linux Administration
- Performance Optimization
- Digital Forensics
- Incident Response
- Malware Analysis
- Filesystem Recovery

---

# How Linux Stores a File

Creating a file involves several steps.

```text
User Creates File
        │
        ▼
Allocate Inode
        │
        ▼
Allocate Data Blocks
        │
        ▼
Store Metadata
        │
        ▼
Create Directory Entry
```

Notice that the **filename is not stored inside the inode**—it is stored in the directory entry.

---

# What is an Inode?

An **inode (Index Node)** is a data structure that stores metadata about a file.

Every file and directory has a unique inode number **within a filesystem**.

An inode does **not** store:

- Filename
- Parent directory name

Instead, it stores everything required to locate and manage the file.

---

# Information Stored in an Inode

Typical inode information includes:

- File type
- Owner (UID)
- Group (GID)
- Permissions
- File size
- Number of hard links
- Access time (atime)
- Modification time (mtime)
- Change time (ctime)
- Block pointers
- Flags

---

# Inode Architecture

```text
                Inode

        ┌──────────────────┐

        │ File Type        │

        │ Owner            │

        │ Permissions      │

        │ Size             │

        │ Timestamps       │

        │ Block Pointers   │

        └──────────────────┘

                │

                ▼

         Actual Data Blocks
```

The inode acts as the metadata record for the file.

---

# Filename Storage

The directory stores mappings between filenames and inode numbers.

Example:

```text
Directory

report.txt  ─────► Inode 52418

notes.txt   ─────► Inode 52419

photo.jpg   ─────► Inode 52420
```

The directory knows the filename; the inode knows the file metadata.

---

# Viewing Inode Numbers

Display inode numbers:

```bash
ls -i
```

Example:

```text
52418 report.txt

52419 notes.txt
```

Display detailed inode information:

```bash
stat report.txt
```

---

# Example `stat` Output

```text
File: report.txt

Size: 2048

Blocks: 8

Inode: 52418

Owner: anurag

Permissions: -rw-r--r--
```

`stat` is a valuable tool for administrators and forensic analysts.

---

# Why Inodes Matter

Inodes enable Linux to:

- Locate file data efficiently.
- Separate metadata from filenames.
- Support hard links.
- Improve filesystem organization.
- Simplify file lookup.

---

# Data Blocks

The actual contents of a file are stored in **data blocks**, not in the inode.

```text
Directory

↓

Inode

↓

Data Blocks

↓

Actual File Content
```

Large files occupy multiple data blocks.

---

# Block Size

Filesystems divide storage into fixed-size blocks.

Common block sizes:

- 1 KB
- 2 KB
- 4 KB
- 8 KB

Example:

A 1 KB file stored on a 4 KB block consumes an entire 4 KB block on disk, though filesystems may employ optimizations depending on their design.

---

# Block Allocation

```text
Disk

┌────┬────┬────┬────┬────┐

│ B1 │ B2 │ B3 │ B4 │ B5 │

└────┴────┴────┴────┴────┘

       ▲

       │

    Inode Points Here
```

The filesystem tracks which blocks belong to each file.

---

# Superblock

The **superblock** stores metadata about the entire filesystem.

Information includes:

- Filesystem type
- Block size
- Total blocks
- Free blocks
- Total inodes
- Free inodes
- Mount status
- Filesystem state

Without a valid superblock, mounting the filesystem may fail.

---

# Superblock Architecture

```text
Filesystem

├── Superblock

├── Inode Table

├── Data Blocks

└── Free Space
```

The superblock is one of the most critical filesystem structures.

---

# Backup Superblocks

Many Linux filesystems maintain backup copies of the superblock.

Benefits:

- Filesystem recovery
- Corruption repair
- Disaster recovery

This improves resilience against metadata corruption.

---

# Viewing Filesystem Information

Display filesystem details:

```bash
df -T
```

Show block device information:

```bash
lsblk
```

Display filesystem metadata (ext-based filesystems):

```bash
sudo tune2fs -l /dev/sdX1
```

Replace `/dev/sdX1` with the appropriate device.

---

# File Metadata

Metadata describes a file without including its contents.

Metadata includes:

- Owner
- Group
- Size
- Permissions
- Timestamps
- Inode number
- File type

Metadata is essential for access control and auditing.

---

# Linux File Timestamps

Linux tracks several timestamps.

| Timestamp | Description |
|-----------|-------------|
| atime | Last access time |
| mtime | Last content modification |
| ctime | Last metadata change |

Some filesystems may also support **birth/creation time** depending on the filesystem and kernel version.

---

# Timestamp Example

```text
report.txt

Created

↓

Modified

↓

Accessed

↓

Permissions Changed
```

Different operations update different timestamps.

---

# Hard Links

A **hard link** creates another directory entry pointing to the **same inode**.

Example:

```text
report.txt

↓

Inode 52418

↑

report_backup.txt
```

Both names reference identical file data.

---

# Hard Link Characteristics

- Shares the same inode
- Shares file contents
- Shares metadata
- No distinction between "original" and "copy"
- Cannot span different filesystems
- Typically cannot reference directories

---

# Create Hard Link

```bash
ln report.txt report_backup.txt
```

Verify:

```bash
ls -li
```

Both files should display the same inode number.

---

# Symbolic (Soft) Links

A symbolic link is a special file that stores the **path** to another file or directory.

Example:

```text
shortcut

↓

/home/anurag/report.txt
```

Unlike hard links, symbolic links reference a pathname rather than an inode directly.

---

# Symbolic Link Characteristics

- Different inode from target
- Stores target path
- Can span filesystems
- Can reference directories
- May become broken if the target is removed

---

# Create Symbolic Link

```bash
ln -s report.txt shortcut.txt
```

List symbolic links:

```bash
ls -l
```

Example:

```text
shortcut.txt -> report.txt
```

---

# Hard Link vs Symbolic Link

| Feature | Hard Link | Symbolic Link |
|----------|-----------|---------------|
| Same Inode | Yes | No |
| Cross Filesystem | No | Yes |
| Points To | Inode | Path |
| Can Link Directories | Generally No | Yes |
| Broken if Target Deleted | No (data remains while links exist) | Yes |

---

# Directory Internals

Directories are special files that map filenames to inode numbers.

Example:

```text
Projects

↓

report.txt → Inode 4021

notes.txt → Inode 4022

image.jpg → Inode 4023
```

The filesystem consults these mappings during file lookup.

---

# File Lookup Process

```text
Open File

↓

Search Directory

↓

Find Inode Number

↓

Read Inode

↓

Locate Data Blocks

↓

Read File
```

Efficient directory structures contribute to fast file access.

---

# Navigating the Filesystem

Display current directory:

```bash
pwd
```

List files:

```bash
ls
```

Change directory:

```bash
cd /etc
```

Return to previous directory:

```bash
cd -
```

Go to home directory:

```bash
cd ~
```

---

# Useful Navigation Commands

| Command | Purpose |
|----------|----------|
| `pwd` | Print working directory |
| `ls` | List directory contents |
| `cd` | Change directory |
| `tree` | Display directory hierarchy (if installed) |
| `find` | Search for files |
| `locate` | Search using indexed database |

---

# Cybersecurity Perspective

Knowledge of inodes and metadata is valuable when investigating:

- Deleted files
- File tampering
- Malware persistence
- Unauthorized modifications
- Timestamp manipulation
- Log integrity
- Hidden files and links

Forensic analysts frequently examine inode information to reconstruct events.

---

# Business Impact

Understanding filesystem internals enables organizations to:

- Improve troubleshooting.
- Recover damaged filesystems.
- Detect unauthorized changes.
- Support forensic investigations.
- Optimize storage management.

---

# Enterprise Best Practices

- Monitor filesystem health regularly.
- Use appropriate filesystem checking tools during maintenance windows.
- Preserve file metadata during backups where required.
- Avoid unnecessary manual manipulation of filesystem structures.
- Audit critical files for unexpected ownership or timestamp changes.
- Train administrators on the differences between hard and symbolic links.

---

# Key Takeaways

- Inodes store file metadata, while directories map filenames to inode numbers.
- File contents reside in data blocks referenced by inodes.
- The superblock contains metadata describing the filesystem itself.
- Hard links share an inode; symbolic links reference a pathname.
- Understanding filesystem internals is fundamental for administration, recovery, and digital forensics.

---


# Part 3 — Mounting & Unmounting, Virtual Filesystems, ext4, XFS, Btrfs, Journaling, Filesystem Checks, and Enterprise Storage Management

---

# Introduction

A storage device is not immediately usable after it is connected to a Linux system.

Before users or applications can access files stored on a device, Linux must **mount** the filesystem into its unified directory hierarchy.

This chapter explains:

- Mounting and unmounting
- Mount points
- Virtual filesystems
- Common Linux filesystems
- Journaling
- Filesystem integrity checking
- Enterprise storage best practices

Understanding these concepts is essential for Linux administrators, DevOps engineers, cloud engineers, and cybersecurity professionals.

---

# What is Mounting?

**Mounting** is the process of attaching a filesystem to a directory within the Linux filesystem hierarchy.

Unlike operating systems that assign drive letters, Linux integrates every mounted filesystem into a single directory tree.

Example:

```text
Before Mount

/

├── home

├── var

└── mnt


After Mount

/

├── home

├── var

└── mnt

      │

      ▼

 SSD Filesystem
```

---

# Why Mounting is Required

Linux cannot access data on a storage device until:

- The device is detected.
- The filesystem is recognized.
- The filesystem is mounted.

Without mounting, the operating system knows the device exists but cannot use its files.

---

# Mount Point

A **mount point** is an existing directory where another filesystem becomes accessible.

Example:

```text
/

└── media

      │

      ▼

USB Drive
```

Everything inside the mounted filesystem appears beneath the mount point.

---

# Mount Workflow

```text
Storage Device

↓

Filesystem Detected

↓

Mount Command

↓

Mount Point

↓

Filesystem Available
```

---

# Viewing Mounted Filesystems

Display mounted filesystems:

```bash
mount
```

Show disk usage:

```bash
df -h
```

Display filesystem types:

```bash
df -T
```

---

# Mounting a Filesystem

Example:

```bash
sudo mount /dev/sdb1 /mnt
```

Explanation:

| Component | Purpose |
|-----------|----------|
| `/dev/sdb1` | Storage device |
| `/mnt` | Mount point |

After mounting, files become accessible under `/mnt`.

---

# Unmounting a Filesystem

Unmount:

```bash
sudo umount /mnt
```

or

```bash
sudo umount /dev/sdb1
```

A filesystem should generally be unmounted before removing the storage device to help prevent data loss.

---

# Busy Filesystem

If a filesystem is in use:

```text
umount: target is busy
```

Possible reasons:

- Open files
- Running applications
- Current working directory inside mount point

Identify open files:

```bash
lsof +D /mnt
```

or

```bash
fuser -vm /mnt
```

---

# Persistent Mounts

Filesystems that should be mounted automatically at boot are defined in:

```text
/etc/fstab
```

Example:

```text
UUID=xxxx-xxxx  /data  ext4  defaults  0  2
```

Using UUIDs instead of device names is generally recommended because device names can change between boots.

---

# Understanding `/etc/fstab`

Typical fields:

| Field | Description |
|--------|-------------|
| Device | Disk, partition, or UUID |
| Mount Point | Directory where the filesystem is mounted |
| Filesystem Type | ext4, xfs, btrfs, etc. |
| Mount Options | defaults, ro, noexec, etc. |
| Dump | Backup utility flag |
| fsck Order | Filesystem check order during boot |

Incorrect entries in `/etc/fstab` can prevent successful boot, so changes should be validated carefully.

---

# Virtual Filesystems

Some Linux filesystems do **not** store persistent data on disk.

Instead, they expose kernel and runtime information.

Examples include:

| Filesystem | Purpose |
|------------|----------|
| procfs | Process information |
| sysfs | Device and kernel information |
| tmpfs | Memory-backed temporary storage |
| devtmpfs | Device nodes |

---

# proc Filesystem

Mounted at:

```text
/proc
```

Provides runtime information such as:

```text
/proc/cpuinfo

/proc/meminfo

/proc/uptime

/proc/version
```

These files are generated dynamically by the kernel.

---

# sysfs

Mounted at:

```text
/sys
```

Provides information about:

- Hardware
- Drivers
- Kernel objects
- Devices

Common directories:

```text
/sys/class

/sys/block

/sys/devices
```

---

# tmpfs

A **tmpfs** filesystem stores data in memory (RAM) rather than on persistent storage.

Common uses:

- Temporary runtime files
- Shared memory
- Fast temporary storage

Typical mount points:

```text
/run

/dev/shm
```

Data stored in `tmpfs` is lost after reboot.

---

# Common Linux Filesystems

Linux supports numerous filesystems.

Some of the most common include:

- ext4
- XFS
- Btrfs
- FAT32
- exFAT
- NTFS
- ISO9660

Each filesystem has different characteristics and use cases.

---

# ext4

**Fourth Extended Filesystem (ext4)** is one of the most widely deployed Linux filesystems.

Features:

- Journaling
- Large filesystem support
- Extents
- Delayed allocation
- Backward compatibility with ext3

Common use cases:

- General-purpose servers
- Workstations
- Virtual machines

---

# XFS

XFS is a high-performance filesystem designed for scalability.

Features:

- Excellent performance with large files
- Online filesystem growth
- Metadata journaling
- Parallel I/O optimization

Common use cases:

- Enterprise servers
- Database systems
- Large storage arrays

---

# Btrfs

**B-tree Filesystem (Btrfs)** is a modern filesystem with advanced management capabilities.

Features include:

- Copy-on-write (CoW)
- Snapshots
- Checksums
- Compression
- Integrated RAID features
- Subvolumes

Btrfs is often used where snapshotting and data integrity are priorities.

---

# FAT32

Characteristics:

- High compatibility
- No Linux permissions
- Limited maximum file size (approximately 4 GB)
- Commonly used on USB drives

---

# NTFS

Primarily associated with Windows systems.

Linux can access NTFS volumes using appropriate kernel support or user-space drivers, depending on the distribution and configuration.

Typical use cases:

- Dual-boot systems
- External drives
- Data exchange with Windows

---

# Filesystem Comparison

| Feature | ext4 | XFS | Btrfs |
|----------|------|-----|--------|
| Journaling | Yes | Yes | Metadata with CoW architecture |
| Snapshots | No | No (native) | Yes |
| Copy-on-Write | No | No | Yes |
| Scalability | High | Very High | High |
| Checksums | Limited | Metadata-focused | Extensive |
| Enterprise Adoption | Very High | Very High | Growing |

The best filesystem depends on workload requirements, recovery objectives, and operational needs.

---

# Journaling

A journal records pending filesystem operations before they are committed.

Simplified workflow:

```text
Write Request

↓

Journal

↓

Filesystem Update

↓

Journal Cleared
```

This reduces the likelihood of metadata corruption after unexpected shutdowns.

---

# Benefits of Journaling

- Faster recovery
- Reduced filesystem corruption
- Improved consistency
- Better resilience against power failures
- Reduced recovery time after crashes

---

# Filesystem Consistency Checks

Linux provides tools to verify filesystem integrity.

Example:

```bash
sudo fsck /dev/sdb1
```

`fsck` checks for inconsistencies and, when appropriate, repairs supported filesystems.

**Important:** Run filesystem checks according to vendor and distribution guidance, typically on unmounted filesystems or from recovery environments.

---

# Checking Disk Usage

Filesystem usage:

```bash
df -h
```

Directory usage:

```bash
du -sh /var/log
```

These commands help identify storage consumption and capacity issues.

---

# Block Device Information

List storage devices:

```bash
lsblk
```

Example:

```text
NAME

sda

├── sda1

├── sda2

nvme0n1

└── nvme0n1p1
```

This provides a hierarchical view of disks and partitions.

---

# Storage Layout Example

```text
NVMe SSD

├── EFI Partition

├── Root Filesystem

├── Home

└── Swap
```

Enterprise systems may include additional partitions or logical volumes for applications, databases, and logs.

---

# Enterprise Storage Design

Large environments often separate data into dedicated filesystems such as:

```text
/

/boot

/home

/var

/var/log

/tmp

/opt

/data

/backup
```

Benefits include:

- Easier maintenance
- Better isolation
- Improved capacity planning
- Simplified backups
- Reduced impact of disk exhaustion

---

# Cybersecurity Perspective

Understanding filesystems assists in:

- Malware investigations
- Log analysis
- Persistence detection
- Filesystem integrity monitoring
- Incident response
- Digital forensics

Attackers may abuse writable locations, temporary directories, or misconfigured mount options to gain persistence or execute malicious code.

---

# Business Impact

Well-designed storage architecture helps organizations:

- Improve reliability.
- Reduce downtime.
- Simplify backups.
- Support disaster recovery.
- Scale storage efficiently.
- Meet compliance requirements for data management.

---

# Enterprise Best Practices

- Use UUIDs in `/etc/fstab` instead of device names where practical.
- Choose the filesystem that aligns with workload requirements.
- Separate operating system, application, and data partitions where appropriate.
- Monitor filesystem utilization proactively.
- Validate mount configurations before deployment.
- Schedule filesystem integrity checks as part of maintenance procedures.
- Keep adequate free space to maintain performance and stability.

---

# Key Takeaways

- Mounting integrates a filesystem into Linux's unified directory hierarchy.
- `/etc/fstab` defines persistent filesystem mounts.
- Virtual filesystems expose kernel and runtime information rather than persistent data.
- ext4, XFS, and Btrfs each provide different capabilities and trade-offs.
- Journaling improves filesystem consistency and accelerates recovery after unexpected failures.

---


# Part 4 — Filesystem Security, Mount Options, Filesystem Forensics, Practical Labs, Chapter Summary, Interview Questions, and References

---

# Introduction

The Linux filesystem is one of the primary targets for attackers because it contains:

- Operating system binaries
- Configuration files
- User data
- Authentication databases
- Logs
- SSH keys
- Application data
- Security policies

A secure filesystem architecture is fundamental to maintaining the confidentiality, integrity, and availability of Linux systems.

This section focuses on filesystem security, secure mount options, forensic techniques, enterprise best practices, and practical administration.

---

# Filesystem Security Principles

The security of a Linux filesystem is based on several core principles:

- Least Privilege
- Defense in Depth
- Integrity
- Availability
- Accountability
- Confidentiality

Every file should be accessible only to users and processes that require it.

---

# Critical Directories

Certain directories are especially important from a security perspective.

| Directory | Security Importance |
|------------|---------------------|
| `/etc` | System configuration |
| `/boot` | Kernel and bootloader |
| `/home` | User data |
| `/root` | Root user's files |
| `/var/log` | Security logs |
| `/var/lib` | Application data |
| `/tmp` | Temporary files |
| `/usr/bin` | Executable programs |

Unauthorized modifications to these locations may indicate compromise or misconfiguration.

---

# Protecting Configuration Files

Examples of sensitive configuration files include:

```text
/etc/passwd

/etc/shadow

/etc/group

/etc/fstab

/etc/ssh/sshd_config

/etc/sudoers
```

Recommended practices:

- Restrict write permissions.
- Monitor for unauthorized changes.
- Include configuration files in backups.
- Review changes through change-management processes.

---

# Sensitive User Files

Common sensitive user files include:

```text
~/.ssh/

~/.bash_history

~/.profile

~/.bashrc

~/.config/
```

These may contain credentials, command history, or application settings and should be protected appropriately.

---

# Mount Options

Linux allows administrators to define mount options that influence filesystem behavior and security.

Common options:

| Option | Purpose |
|----------|----------|
| `ro` | Mount read-only |
| `rw` | Mount read-write |
| `noexec` | Prevent execution of binaries |
| `nosuid` | Ignore SUID/SGID bits |
| `nodev` | Ignore device files |
| `relatime` | Optimize access time updates |
| `defaults` | Standard mount options |

Selecting appropriate options depends on the filesystem's intended use.

---

# Read-Only Filesystems

Example:

```text
ro
```

Benefits:

- Prevents accidental modification.
- Protects static data.
- Reduces risk of unauthorized changes.

Typical use cases include installation media and certain recovery environments.

---

# noexec

Example:

```text
noexec
```

Purpose:

Prevent execution of binaries from the mounted filesystem.

Common candidates:

- Temporary storage
- Shared file repositories
- Removable media (where appropriate)

This can reduce the risk of executing malicious binaries from those locations.

---

# nosuid

Purpose:

```text
nosuid
```

Disables the effect of **SUID** and **SGID** permission bits on the mounted filesystem.

Benefits:

- Reduces privilege escalation opportunities.
- Limits abuse of privileged executables.

---

# nodev

Purpose:

```text
nodev
```

Prevents interpretation of device files on the mounted filesystem.

Useful for:

- User home partitions
- Removable media
- Shared storage

---

# Secure Mount Example

```text
UUID=xxxx

↓

/tmp

↓

ext4

↓

rw,nosuid,nodev,noexec
```

Combining multiple mount options strengthens security for filesystems that should not contain executable or privileged content.

---

# Temporary Directory Security

`/tmp` is writable by many users and applications.

Recommendations:

- Apply `noexec`, `nosuid`, and `nodev` where compatible with workloads.
- Monitor for unexpected executable files.
- Clean temporary files periodically.
- Review application compatibility before enforcing restrictive options.

---

# File Integrity Monitoring

Organizations often monitor critical filesystem locations for unauthorized changes.

Typical targets include:

- `/etc`
- `/boot`
- `/usr/bin`
- `/usr/sbin`
- `/var/log`
- Application configuration directories

Unexpected modifications should be investigated promptly.

---

# Filesystem Auditing

Routine filesystem audits may include:

- Permission reviews
- Ownership verification
- Unexpected executable detection
- Integrity validation
- Configuration comparison
- Storage utilization analysis

Regular audits help maintain security and operational consistency.

---

# Filesystem Forensics

Filesystem forensics involves examining storage to determine:

- What happened
- When it happened
- Who performed an action
- Which files were affected
- Whether evidence of compromise exists

This discipline is central to digital investigations.

---

# Forensic Artifacts

Investigators commonly examine:

```text
File Metadata

Timestamps

Permissions

Ownership

Directory Structure

Logs

Hidden Files

Links

Configuration Files
```

Correlating these artifacts helps reconstruct system activity.

---

# Timeline Analysis

File timestamps can help establish an event sequence.

Typical workflow:

```text
File Created

↓

File Modified

↓

Permission Changed

↓

File Accessed
```

Investigators should be aware that timestamps can be altered under certain circumstances, so they should be corroborated with additional evidence.

---

# Hidden Files

Hidden files begin with a period (`.`).

Examples:

```text
.bash_history

.profile

.ssh

.config
```

Hidden files are not inherently malicious but often contain important configuration or user information.

---

# Finding Large Files

Example:

```bash
find / -type f -size +100M
```

Use cases:

- Storage management
- Incident response
- Malware investigations
- Capacity planning

Exercise caution when searching the entire filesystem on production systems.

---

# Finding Recently Modified Files

Example:

```bash
find /var/log -type f -mtime -7
```

This searches for files modified within the last seven days.

---

# Finding SUID Files

Example:

```bash
find / -perm -4000 -type f
```

SUID binaries deserve periodic review because they execute with elevated privileges.

---

# Checking Filesystem Usage

Filesystem capacity:

```bash
df -h
```

Directory usage:

```bash
du -sh /home/*
```

Monitoring storage usage helps prevent service disruptions due to exhausted disk space.

---

# Detecting Open Files

Display open files:

```bash
lsof
```

Typical uses:

- Troubleshooting
- Security investigations
- Identifying locked files
- Diagnosing unmount issues

---

# Enterprise Filesystem Monitoring

Organizations frequently monitor:

- Disk usage
- Filesystem errors
- Permission changes
- Unexpected executable files
- Integrity violations
- Configuration drift
- Storage growth trends

These metrics support operational reliability and security.

---

# Cybersecurity Perspective

Attackers may attempt to:

- Modify configuration files.
- Replace legitimate executables.
- Hide malware in temporary directories.
- Abuse writable locations.
- Manipulate permissions.
- Establish persistence through startup files.

Defenders should monitor critical directories, review filesystem changes, and correlate filesystem events with authentication and process logs.

---

# Practical Lab 1 — Explore the Filesystem

Commands:

```bash
pwd
ls -la
tree
```

Objective:

- Navigate the filesystem hierarchy and identify major directories.

> **Note:** The `tree` command may require installation on some distributions.

---

# Practical Lab 2 — Examine File Metadata

Commands:

```bash
stat /etc/passwd
ls -li
```

Objective:

- Inspect inode numbers, timestamps, ownership, and permissions.

---

# Practical Lab 3 — Create Hard and Symbolic Links

Commands:

```bash
touch demo.txt

ln demo.txt hardlink.txt

ln -s demo.txt symlink.txt

ls -li
```

Objective:

- Compare inode numbers and observe the differences between hard and symbolic links.

---

# Practical Lab 4 — Review Mounted Filesystems

Commands:

```bash
mount

df -T

lsblk
```

Objective:

- Identify mounted filesystems, filesystem types, and block devices.

---

# Practical Lab 5 — Search for SUID Files

Command:

```bash
find / -perm -4000 -type f
```

Objective:

- Identify privileged executables and understand why they require careful monitoring.

---

# Practical Lab 6 — Review Disk Usage

Commands:

```bash
df -h

du -sh /var/log
```

Objective:

- Analyze filesystem utilization and identify directories consuming significant storage.

---

# Chapter Summary

In this chapter, you learned:

- Linux filesystem architecture.
- The Filesystem Hierarchy Standard (FHS).
- Directory structure and file types.
- Inodes, superblocks, and metadata.
- Hard links and symbolic links.
- Mounting and unmounting filesystems.
- Virtual filesystems (`proc`, `sys`, `tmpfs`).
- Common filesystems including ext4, XFS, and Btrfs.
- Journaling concepts.
- Filesystem integrity checks.
- Secure mount options.
- Filesystem monitoring and forensics.
- Enterprise storage and security best practices.

---

# Interview Questions

## Beginner

1. What is a filesystem?
2. What is the root directory?
3. What is the purpose of `/etc`?
4. What is an inode?
5. What is a mount point?
6. What is the difference between a hard link and a symbolic link?
7. What is journaling?
8. What is `/proc` used for?
9. What is the purpose of `/etc/fstab`?
10. How do you display mounted filesystems?

---

## Intermediate

1. Explain the Filesystem Hierarchy Standard (FHS).
2. What information is stored in an inode?
3. Compare ext4, XFS, and Btrfs.
4. What are the advantages of journaling?
5. How do `noexec`, `nosuid`, and `nodev` improve security?
6. Explain the relationship between directories and inodes.
7. What is the role of the superblock?
8. How would you troubleshoot a filesystem that fails to mount?
9. What information can be obtained from `stat`?
10. How does Linux use virtual filesystems?

---

## Advanced

1. Describe the complete path resolution process from filename to data blocks.
2. How would you recover from superblock corruption on a supported filesystem?
3. Explain the security implications of writable temporary directories.
4. How would you design an enterprise filesystem layout for a critical application server?
5. Compare copy-on-write filesystems with traditional journaling filesystems.
6. What filesystem artifacts are most valuable during a forensic investigation?
7. How would you detect unauthorized modifications to critical system files?
8. Explain how mount options reduce attack surface.
9. How would you monitor filesystem integrity across thousands of Linux systems?
10. Describe the role of metadata in incident response and digital forensics.

---

# Key Takeaways

- Linux stores all files within a single hierarchical directory tree rooted at `/`.
- Inodes contain metadata, while directories map filenames to inode numbers.
- Mounting integrates storage devices into the filesystem hierarchy.
- Virtual filesystems expose kernel and runtime information without storing persistent data.
- Secure mount options, integrity monitoring, and regular auditing strengthen filesystem security in enterprise environments.

---

# References

## Official Documentation

- Linux Kernel Documentation
- Filesystem Hierarchy Standard (FHS)
- ext4 Documentation
- XFS Documentation
- Btrfs Documentation
- GNU Core Utilities Manual

## Standards & Best Practices

- Linux Foundation Documentation
- CIS Benchmarks for Linux
- NIST SP 800 Series
- MITRE ATT&CK (Linux Techniques)

---

# Next Chapter

➡️ **06-Linux-File-Management.md**

Topics Covered:

- File Creation and Deletion
- Copying, Moving, and Renaming Files
- Viewing and Editing Files
- Searching Files and Directories
- Wildcards and Globbing
- Compression and Archiving
- Checksums and File Integrity
- File Permissions in Daily Operations
- Enterprise File Management Best Practices
- Practical Labs
- Interview Questions
- References