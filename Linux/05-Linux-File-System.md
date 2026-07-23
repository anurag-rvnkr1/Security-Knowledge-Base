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


