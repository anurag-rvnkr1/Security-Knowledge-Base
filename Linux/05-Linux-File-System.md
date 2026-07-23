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


