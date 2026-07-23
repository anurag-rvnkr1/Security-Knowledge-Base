# 01 - Linux Fundamentals

# Part 1 — Introduction to Linux, History of Unix & Linux, GNU Project, Open Source, Linux Distributions, and Enterprise Linux

---

# Introduction

Linux is the world's most widely used open-source operating system. It powers everything from smartphones and laptops to cloud infrastructure, supercomputers, enterprise servers, IoT devices, embedded systems, and cybersecurity platforms.

Nearly every modern technology stack—including cloud computing, DevOps, cybersecurity, artificial intelligence, and enterprise networking—relies heavily on Linux.

For cybersecurity professionals, Linux is more than just an operating system. It is the primary platform for:

- Security Operations Centers (SOC)
- Penetration Testing
- Digital Forensics
- Threat Hunting
- Malware Analysis
- Incident Response
- Detection Engineering
- Cloud Infrastructure
- Container Platforms
- Web Servers
- Network Appliances

Understanding Linux is therefore a foundational skill for anyone pursuing a career in IT or cybersecurity.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the history and evolution of Unix and Linux.
- Explain the philosophy behind open-source software.
- Describe the GNU Project and its significance.
- Identify the components of a Linux operating system.
- Compare major Linux distributions.
- Understand enterprise Linux ecosystems.
- Recognize Linux's role in modern IT and cybersecurity.
- Appreciate the advantages and limitations of Linux.

---

# What is Linux?

Linux is an **open-source, Unix-like operating system** built around the Linux kernel. It provides a stable, secure, and highly customizable environment for running applications on a wide variety of hardware platforms.

Unlike proprietary operating systems, Linux allows users and organizations to inspect, modify, and distribute its source code under open-source licenses.

A complete Linux operating system typically consists of:

- Linux Kernel
- GNU utilities
- Shell
- System libraries
- System services
- Package manager
- File system
- User applications

---

# Why Linux Matters

Linux dominates many areas of computing because of its reliability, flexibility, and scalability.

Linux is widely used in:

| Industry | Linux Usage |
|-----------|-------------|
| Cloud Computing | Virtual machines, Kubernetes, containers |
| Enterprise IT | Servers, databases, web hosting |
| Cybersecurity | SOC, VAPT, DFIR, threat hunting |
| Networking | Routers, firewalls, appliances |
| Telecommunications | 5G infrastructure |
| Artificial Intelligence | GPU clusters, ML platforms |
| Supercomputing | High-performance computing (HPC) |
| IoT & Embedded Systems | Smart devices, automotive systems |
| Finance | Trading platforms, banking infrastructure |
| Government & Defense | Secure enterprise environments |

---

# What is Unix?

Unix is a multiuser, multitasking operating system developed at **Bell Labs** in the late 1960s and early 1970s. It introduced many concepts that continue to influence modern operating systems.

Key Unix principles include:

- Everything is treated as a file.
- Build small programs that perform one task well.
- Combine programs using pipes.
- Keep interfaces simple.
- Encourage scripting and automation.

Many modern operating systems, including Linux and macOS, are heavily influenced by Unix.

---

# Brief History of Unix

| Year | Milestone |
|------|-----------|
| 1969 | Unix development begins at Bell Labs |
| 1971 | First Unix Edition released |
| 1973 | Unix rewritten in the C programming language |
| 1980s | Commercial Unix variants become popular |
| 1990s | Linux emerges as a free Unix-like alternative |
| Today | Unix principles continue to influence modern systems |

Rewriting Unix in C greatly improved portability, enabling it to run on different hardware architectures.

---

# Birth of Linux

In 1991, **Linus Torvalds**, then a computer science student in Finland, began developing a free Unix-like kernel as a personal project.

His goals included:

- Learning operating system design.
- Creating a free alternative to proprietary Unix systems.
- Supporting Intel 80386 processors.

The first public announcement was made in August 1991, inviting developers to contribute to the project.

---

# Linux Timeline

| Year | Event |
|------|-------|
| 1991 | Initial Linux kernel released |
| 1992 | Linux licensed under the GNU General Public License (GPL) |
| 1993 | Early Linux distributions appear |
| 1994 | Linux Kernel 1.0 released |
| 2000s | Enterprise Linux adoption accelerates |
| 2013 | Linux becomes dominant in cloud computing |
| Today | Linux powers the majority of servers, cloud workloads, and supercomputers |

---

# The GNU Project

The **GNU Project**, launched by **Richard Stallman** in 1983, aimed to create a completely free Unix-compatible operating system.

Before the Linux kernel existed, GNU had already developed many essential components, including:

- GNU Compiler Collection (GCC)
- GNU Bash
- Core utilities
- Libraries
- Debugging tools

When the Linux kernel was combined with GNU software, a complete operating system became possible.

---

# GNU + Linux

A typical Linux system consists of:

```
Applications

↓

GNU Utilities

↓

Shell (Bash, Zsh, etc.)

↓

System Libraries

↓

Linux Kernel

↓

Hardware
```

The GNU Project supplies many user-space tools, while the Linux kernel manages hardware and system resources.

---

# What is Open Source?

Open-source software makes its source code publicly available, allowing anyone to:

- View the code.
- Modify it.
- Improve it.
- Redistribute it according to the license terms.

This collaborative development model encourages innovation, transparency, and rapid improvement.

---

# Benefits of Open Source

| Benefit | Description |
|----------|-------------|
| Transparency | Source code can be inspected |
| Security | Vulnerabilities are openly reviewed and patched |
| Flexibility | Software can be customized |
| Cost | Often available without licensing fees |
| Innovation | Global developer collaboration |
| Vendor Independence | Reduced reliance on proprietary vendors |

---

# Proprietary vs Open Source

| Proprietary Software | Open-Source Software |
|----------------------|----------------------|
| Closed source code | Publicly available source code |
| Vendor-controlled | Community and organization contributions |
| Licensing fees may apply | Often free to use |
| Limited customization | Highly customizable |
| Vendor support | Community and commercial support available |

---

# Linux Distributions

A **Linux distribution (distro)** combines the Linux kernel with system utilities, package management, desktop environments, and additional software into a complete operating system.

Different distributions target different use cases, such as:

- Desktop computing
- Enterprise servers
- Cloud infrastructure
- Security testing
- Embedded systems

---

# Major Linux Distribution Families

```
Linux

├── Debian Family
│   ├── Debian
│   ├── Ubuntu
│   ├── Kali Linux
│   └── Linux Mint
│
├── Red Hat Family
│   ├── Red Hat Enterprise Linux (RHEL)
│   ├── Rocky Linux
│   ├── AlmaLinux
│   └── Fedora
│
├── SUSE Family
│   ├── openSUSE
│   └── SUSE Linux Enterprise
│
└── Arch Family
    ├── Arch Linux
    └── Manjaro
```

Each family differs in package management, release cycle, and intended audience.

---

# Popular Linux Distributions

| Distribution | Primary Use |
|--------------|-------------|
| Ubuntu | Desktop, servers, cloud |
| Debian | Stable servers |
| Fedora | Development and testing |
| RHEL | Enterprise production systems |
| Rocky Linux | Community enterprise servers |
| AlmaLinux | Enterprise replacement for CentOS |
| Kali Linux | Penetration testing and security assessments |
| Parrot Security | Security testing and digital forensics |
| Arch Linux | Advanced users and customization |
| Linux Mint | Desktop computing |

---

# Enterprise Linux

Enterprise Linux distributions provide long-term stability, security updates, certification, and commercial support for business environments.

Common enterprise distributions include:

- Red Hat Enterprise Linux (RHEL)
- SUSE Linux Enterprise Server (SLES)
- Ubuntu LTS
- Oracle Linux
- Rocky Linux
- AlmaLinux

Organizations select enterprise distributions for their predictable release cycles and vendor support.

---

# Linux in Cybersecurity

Linux plays a central role across offensive and defensive security disciplines.

Examples include:

| Domain | Linux Usage |
|--------|-------------|
| SOC | Log analysis, SIEM collectors |
| VAPT | Security testing tools |
| Threat Hunting | Command-line investigations |
| DFIR | Forensic analysis |
| Detection Engineering | Log pipelines and automation |
| Cloud Security | Kubernetes and container security |
| Malware Analysis | Sandboxes and reverse engineering |
| Web Security | Secure server hosting |

---

# Enterprise Use Cases

Large organizations deploy Linux for:

- Web servers
- Database servers
- Application servers
- DNS servers
- Email infrastructure
- Virtualization hosts
- Kubernetes clusters
- CI/CD pipelines
- Security monitoring platforms
- Network appliances

Linux is often chosen for mission-critical workloads due to its stability and scalability.

---

# Business Impact

Adopting Linux enables organizations to:

- Reduce software licensing costs.
- Improve infrastructure scalability.
- Enhance system reliability.
- Strengthen security through transparency.
- Support cloud-native technologies.
- Accelerate automation and DevOps initiatives.

---

# Enterprise Best Practices

Organizations should:

- Standardize on approved Linux distributions.
- Apply security updates regularly.
- Follow vendor-supported release versions.
- Automate configuration management.
- Implement centralized logging and monitoring.
- Enforce least privilege for administrative access.
- Maintain accurate system documentation.

---

# Key Takeaways

- Linux is an open-source, Unix-like operating system built around the Linux kernel.
- Unix laid the foundation for many modern operating systems.
- The GNU Project provides many of the user-space tools used with Linux.
- Linux distributions package the kernel with utilities, package managers, and applications.
- Enterprise Linux is widely used for servers, cloud computing, and cybersecurity.
- Linux skills are essential for modern IT, DevOps, cloud, and cybersecurity careers.

---


# Part 2 — Linux Architecture, Kernel, Shell, Terminal, CLI vs GUI, Linux Components, and System Overview

---

# Introduction

To become proficient with Linux, it is essential to understand how the operating system is organized internally. Unlike many proprietary operating systems, Linux follows a modular architecture where each component has a well-defined responsibility.

Understanding Linux architecture helps administrators, developers, SOC analysts, and cybersecurity professionals troubleshoot systems, optimize performance, secure infrastructure, and understand how applications interact with hardware.

This section explains the major building blocks of Linux, from hardware to user applications.

---

# Linux Architecture Overview

A Linux system consists of multiple layers that work together to provide a complete operating system.

```
+------------------------------------------------------+
|                User Applications                     |
| (Firefox, Nginx, Python, Docker, VS Code, etc.)      |
+------------------------------------------------------+
|               Shell & Command Line                   |
| (Bash, Zsh, Fish, PowerShell Core)                   |
+------------------------------------------------------+
|              System Libraries (glibc)                |
+------------------------------------------------------+
|                Linux Kernel                          |
| Process | Memory | Filesystem | Network | Drivers    |
+------------------------------------------------------+
|                  Hardware                            |
| CPU | RAM | Storage | NIC | GPU | USB Devices        |
+------------------------------------------------------+
```

Each layer provides services to the layer above while relying on the layer below.

---

# Major Components of Linux

A complete Linux operating system includes:

| Component | Purpose |
|-----------|---------|
| Kernel | Manages hardware and system resources |
| Shell | User interface for executing commands |
| System Libraries | APIs used by applications |
| File System | Organizes files and directories |
| Init/System Manager | Starts services during boot |
| Package Manager | Installs and updates software |
| User Applications | Productivity and server software |

---

# What is the Linux Kernel?

The **Linux Kernel** is the core of the operating system.

It is responsible for:

- Managing CPU resources
- Managing memory
- Scheduling processes
- Device communication
- File system management
- Network communication
- Security enforcement
- Hardware abstraction

Without the kernel, applications cannot interact with hardware.

---

# Responsibilities of the Kernel

```
Applications

↓

System Calls

↓

Kernel

├── Process Management
├── Memory Management
├── Device Drivers
├── File Systems
├── Networking
├── Security Modules

↓

Hardware
```

The kernel acts as the intermediary between software and physical hardware.

---

# Kernel Features

Modern Linux kernels support:

- Preemptive multitasking
- Virtual memory
- Multi-user operation
- Multiprocessing (SMP)
- Loadable kernel modules
- Advanced networking
- Filesystem support
- Security frameworks
- Container technologies

These capabilities make Linux suitable for both embedded systems and large-scale enterprise deployments.

---

# Monolithic Kernel

Linux uses a **monolithic kernel** architecture.

This means core operating system services execute within kernel space.

Advantages include:

- High performance
- Efficient communication between subsystems
- Reduced overhead

Potential disadvantages:

- Kernel bugs may affect the entire system.
- Debugging kernel code is more complex.

---

# Kernel Space vs User Space

```
+------------------------------+
|          User Space          |
| Applications                 |
| Shell                        |
| Browsers                     |
| Databases                    |
+--------------↑---------------+
               |
         System Calls
               |
+--------------↓---------------+
|         Kernel Space         |
| Scheduler                    |
| Memory Manager               |
| Drivers                      |
| Networking                   |
| File Systems                 |
+------------------------------+
```

**User Space**

- Runs normal applications.
- Limited privileges.
- Cannot directly access hardware.

**Kernel Space**

- Full system privileges.
- Direct hardware access.
- Executes trusted operating system code.

This separation improves system stability and security.

---

# System Calls

Applications communicate with the kernel through **system calls**.

Examples include:

- Opening files
- Reading data
- Writing files
- Creating processes
- Sending network packets
- Allocating memory

```
Application

↓

System Call

↓

Kernel

↓

Hardware
```

System calls provide a controlled interface to kernel functionality.

---

# Process Management

The kernel manages all running processes.

Responsibilities include:

- Process creation
- Scheduling
- Context switching
- Process termination
- Resource allocation

Each process receives:

- Process ID (PID)
- Memory allocation
- CPU scheduling
- Security context

---

# Memory Management

The kernel manages system memory efficiently by:

- Allocating RAM
- Reclaiming unused memory
- Managing virtual memory
- Swapping pages when necessary
- Preventing unauthorized memory access

Efficient memory management ensures stable system performance.

---

# Device Drivers

Device drivers allow the kernel to communicate with hardware devices.

Examples:

- Network adapters
- Graphics cards
- Storage devices
- USB peripherals
- Audio devices

Linux supports thousands of hardware drivers, many of which are built directly into the kernel or loaded as modules.

---

# Loadable Kernel Modules (LKMs)

Kernel functionality can be extended using **Loadable Kernel Modules** without recompiling or rebooting the kernel.

Examples include:

- Filesystem modules
- Network drivers
- USB drivers
- Virtualization support

Benefits:

- Reduced kernel size
- Dynamic hardware support
- Easier maintenance

---

# File System Management

The kernel provides a unified interface for accessing different file systems.

Supported file systems include:

- ext4
- XFS
- Btrfs
- FAT32
- exFAT
- NTFS (via appropriate drivers)
- NFS
- SMB/CIFS

Applications access files through standard system calls regardless of the underlying filesystem.

---

# Networking Stack

Linux includes a mature networking stack capable of supporting:

- IPv4
- IPv6
- TCP
- UDP
- ICMP
- Routing
- Firewalling
- VPNs
- Network namespaces
- Packet filtering

The networking stack is widely used in enterprise infrastructure and cloud platforms.

---

# Linux Security Modules (LSM)

Linux Security Modules provide additional access control mechanisms.

Common frameworks include:

- SELinux
- AppArmor
- Smack
- TOMOYO

These frameworks enforce security policies beyond standard UNIX permissions.

---

# What is a Shell?

A **shell** is a command interpreter that allows users to interact with the operating system.

It:

- Accepts user commands.
- Executes programs.
- Supports scripting.
- Automates administrative tasks.

The shell serves as the interface between users and the kernel.

---

# Shell Workflow

```
User

↓

Shell

↓

System Call

↓

Kernel

↓

Hardware
```

The shell interprets commands but does not directly control hardware.

---

# Popular Linux Shells

| Shell | Description |
|--------|-------------|
| Bash | Default shell for many Linux distributions |
| Zsh | Advanced interactive shell with extensibility |
| Fish | User-friendly shell with modern features |
| Dash | Lightweight POSIX-compliant shell |
| Ksh | KornShell, commonly used in enterprise UNIX environments |

---

# What is a Terminal?

A **terminal** is the application used to access a shell.

Examples:

- GNOME Terminal
- Konsole
- Xfce Terminal
- Alacritty
- Windows Terminal (for WSL)

The terminal displays command output and accepts keyboard input.

---

# Terminal vs Shell

| Terminal | Shell |
|-----------|-------|
| User interface application | Command interpreter |
| Displays text | Executes commands |
| Hosts a shell session | Processes user input |
| Examples: GNOME Terminal, Konsole | Examples: Bash, Zsh, Fish |

A terminal runs a shell, but they are not the same component.

---

# Command-Line Interface (CLI)

The CLI allows users to manage Linux systems by typing commands.

Advantages include:

- Automation
- Speed
- Low resource usage
- Remote administration
- Scriptability
- Fine-grained control

The CLI is the preferred interface for servers and cybersecurity operations.

---

# Graphical User Interface (GUI)

A GUI provides visual interaction through windows, icons, menus, and pointers.

Common desktop environments include:

- GNOME
- KDE Plasma
- XFCE
- Cinnamon
- MATE

GUIs are well suited for desktop users and graphical applications.

---

# CLI vs GUI

| CLI | GUI |
|-----|-----|
| Keyboard-driven | Mouse and keyboard |
| Fast for repetitive tasks | Easier for beginners |
| Excellent for automation | Better for visual workflows |
| Minimal resource usage | Higher resource usage |
| Preferred for servers | Preferred for desktops |

Most enterprise Linux servers operate without a graphical interface.

---

# Why Linux Servers Often Use the CLI

Organizations prefer command-line administration because it:

- Conserves system resources.
- Simplifies remote management over SSH.
- Enables scripting and automation.
- Integrates with configuration management tools.
- Supports large-scale infrastructure management.

---

# Environment Variables

Environment variables store information used by the shell and applications.

Common examples:

| Variable | Purpose |
|-----------|---------|
| `PATH` | Directories searched for executable commands |
| `HOME` | User's home directory |
| `USER` | Current username |
| `HOSTNAME` | System hostname |
| `SHELL` | Current shell |

These variables influence application behavior and user sessions.

---

# Linux Philosophy

Linux follows several enduring design principles:

- Everything is a file.
- Keep programs small and focused.
- Build reusable tools.
- Automate repetitive tasks.
- Prefer text-based configuration.
- Enable interoperability through standard interfaces.

These principles contribute to Linux's flexibility and longevity.

---

# Business Impact

Understanding Linux architecture enables organizations to:

- Improve troubleshooting efficiency.
- Optimize resource utilization.
- Build scalable infrastructure.
- Strengthen system security.
- Reduce operational complexity.
- Automate administrative tasks.

---

# Enterprise Best Practices

Organizations should:

- Use supported kernel versions.
- Keep kernels and system libraries updated.
- Restrict direct root access.
- Prefer CLI-based administration for servers.
- Monitor kernel logs and system performance.
- Apply security frameworks such as SELinux or AppArmor where appropriate.
- Document system architecture and standard configurations.

---

# Key Takeaways

- The Linux kernel is the core component of the operating system.
- User space and kernel space are separated for security and stability.
- Applications communicate with the kernel through system calls.
- The shell interprets user commands, while the terminal provides the interface to the shell.
- Linux follows a modular architecture that supports scalability, performance, and security.
- Understanding Linux architecture is fundamental for system administration and cybersecurity.

---


# Part 3 — Linux Features, Linux Directory Structure, Filesystem Hierarchy Standard (FHS), Essential Directories, and Enterprise File Organization

---

# Introduction

One of the most powerful aspects of Linux is its well-organized filesystem. Unlike Windows, where drives such as `C:\`, `D:\`, and `E:\` exist independently, Linux presents everything under a **single hierarchical directory tree** starting from the **root directory (`/`)**.

Linux follows the **Filesystem Hierarchy Standard (FHS)**, which defines where system files, user data, applications, configuration files, logs, libraries, and temporary files should reside. This consistency allows administrators to work across different Linux distributions with minimal changes.

Understanding the Linux directory structure is fundamental for:

- Linux Administration
- Cybersecurity
- Digital Forensics
- Incident Response
- DevOps
- Cloud Engineering
- System Troubleshooting

---

# Learning Objectives

After completing this section, you will be able to:

- Understand the Linux filesystem hierarchy.
- Explain the purpose of important directories.
- Navigate Linux directories confidently.
- Identify where configuration files, logs, binaries, and user data are stored.
- Apply FHS concepts in enterprise environments.

---

# Linux File System Overview

Linux stores all files and directories beneath a single root directory.

```
                /
                │
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

Every file, directory, storage device, and process is represented somewhere within this hierarchy.

---

# Everything is a File

One of Linux's core philosophies is:

> **Everything is a file.**

This includes:

- Regular files
- Directories
- Hard disks
- USB devices
- Network sockets
- Processes
- Printers
- Terminals

This design provides a consistent interface for interacting with system resources.

---

# Root Directory (`/`)

The root directory is the top-most directory of the Linux filesystem.

```
/
```

It contains every other directory.

Do not confuse:

| Symbol | Meaning |
|----------|---------|
| `/` | Root directory |
| `/root` | Home directory of the root user |

---

# Filesystem Hierarchy Standard (FHS)

The **Filesystem Hierarchy Standard (FHS)** defines the standard directory layout used by most Linux distributions.

Benefits include:

- Consistency across distributions.
- Easier system administration.
- Simplified application deployment.
- Improved interoperability.
- Predictable file locations.

Most enterprise Linux distributions adhere closely to the FHS.

---

# `/bin` — Essential User Commands

The `/bin` directory contains essential command-line utilities required for booting and single-user mode.

Examples:

```
ls
cp
mv
rm
cat
echo
pwd
chmod
```

These commands are available even when other filesystems are not mounted.

> **Note:** On many modern distributions, `/bin` is a symbolic link to `/usr/bin`.

---

# `/sbin` — System Administration Commands

The `/sbin` directory contains essential system administration utilities.

Examples:

```
fsck
reboot
shutdown
ip
mount
mkfs
```

These commands are primarily intended for administrative tasks.

> **Note:** On many modern systems, `/sbin` is a symbolic link to `/usr/sbin`.

---

# `/boot` — Boot Files

The `/boot` directory contains files required during the boot process.

Typical contents:

- Linux kernel
- Initial RAM filesystem (initramfs)
- GRUB configuration
- Bootloader files

Example:

```
/boot/vmlinuz
/boot/initrd.img
```

Deleting or modifying these files incorrectly may prevent the system from booting.

---

# `/dev` — Device Files

Linux represents hardware devices as files inside `/dev`.

Examples:

```
/dev/sda
/dev/sda1
/dev/tty
/dev/null
/dev/random
/dev/urandom
```

Examples of special devices:

| Device | Purpose |
|----------|---------|
| `/dev/null` | Discards all data written to it |
| `/dev/zero` | Produces continuous zero bytes |
| `/dev/random` | Generates high-quality random data |
| `/dev/urandom` | Generates pseudo-random data |

---

# `/etc` — Configuration Files

The `/etc` directory stores system-wide configuration files.

Common examples:

```
/etc/passwd
/etc/shadow
/etc/group
/etc/hosts
/etc/fstab
/etc/ssh/
/etc/systemd/
```

Most administrative configuration changes occur within this directory.

---

# `/home` — User Home Directories

Each regular user receives a personal directory inside `/home`.

Example:

```
/home/alice
/home/bob
/home/anurag
```

User-specific data includes:

- Documents
- Downloads
- SSH keys
- Desktop files
- Configuration files

Users typically have write access only to their own home directories.

---

# `/root` — Root User Home

The root user's home directory is:

```
/root
```

It is separate from `/home` to ensure administrative access remains available even if `/home` is unavailable.

---

# `/lib` and `/lib64`

These directories contain essential shared libraries required by system programs.

Examples include:

- C standard library
- Dynamic linker
- Runtime libraries

Applications depend on these libraries for execution.

---

# `/media`

The `/media` directory is used for automatically mounted removable devices.

Examples:

```
USB Drives
DVDs
External Hard Drives
SD Cards
```

---

# `/mnt`

The `/mnt` directory is intended for temporary manual mounts.

Example:

```
sudo mount /dev/sdb1 /mnt
```

System administrators frequently use `/mnt` during maintenance or recovery operations.

---

# `/opt`

The `/opt` directory contains optional third-party software packages.

Example:

```
/opt/google
/opt/VMware
/opt/custom-application
```

Enterprise software vendors often install applications under `/opt`.

---

# `/proc`

The `/proc` directory is a virtual filesystem generated by the kernel.

It provides real-time information about:

- Running processes
- CPU information
- Memory usage
- Kernel parameters
- System uptime

Example files:

```
/proc/cpuinfo
/proc/meminfo
/proc/uptime
/proc/version
```

These files do not exist on disk; they are generated dynamically.

---

# `/sys`

The `/sys` directory is another virtual filesystem that exposes kernel objects and hardware information.

Administrators can inspect:

- Devices
- Drivers
- Kernel modules
- Power management
- Hardware attributes

Many hardware-related settings can be viewed or modified through `/sys`.

---

# `/run`

The `/run` directory stores runtime information created after system boot.

Examples include:

- PID files
- Runtime sockets
- Lock files
- Service state information

Its contents are typically cleared during each reboot.

---

# `/srv`

The `/srv` directory stores data served by system services.

Examples:

```
/srv/www
/srv/ftp
/srv/git
```

This directory helps organize application-specific service data.

---

# `/tmp`

The `/tmp` directory stores temporary files.

Characteristics:

- Writable by all users.
- Frequently cleaned automatically.
- Used by applications during execution.

Applications should not rely on files in `/tmp` for long-term storage.

---

# `/usr`

The `/usr` directory contains the majority of user-space applications and resources.

Common subdirectories include:

```
/usr/bin
/usr/sbin
/usr/lib
/usr/share
/usr/local
```

Most installed software resides under `/usr`.

---

# `/usr/local`

This directory is reserved for software installed manually by administrators rather than through the system package manager.

Example:

```
/usr/local/bin
/usr/local/lib
/usr/local/share
```

This separation prevents conflicts with distribution-managed packages.

---

# `/var`

The `/var` directory stores data that changes frequently.

Examples include:

```
Logs
Mail queues
Databases
Web caches
Package metadata
Spool files
```

Important subdirectories:

```
/var/log
/var/cache
/var/lib
/var/tmp
```

---

# Important Enterprise Directories

| Directory | Enterprise Usage |
|------------|------------------|
| `/etc` | Configuration management |
| `/var/log` | Security monitoring and log analysis |
| `/home` | User data |
| `/usr` | Installed software |
| `/opt` | Third-party enterprise applications |
| `/boot` | Bootloader and kernel management |
| `/srv` | Hosted services |
| `/var/lib` | Databases and application state |

---

# Hidden Files

Files beginning with a period (`.`) are hidden.

Examples:

```
.bashrc
.profile
.gitconfig
.ssh
```

Hidden files typically contain user-specific configuration.

---

# Absolute vs Relative Paths

### Absolute Path

Begins from the root directory.

Example:

```
/home/alice/Documents/report.txt
```

### Relative Path

Begins from the current working directory.

Example:

```
Documents/report.txt
```

---

# Path Navigation Symbols

| Symbol | Meaning |
|----------|---------|
| `.` | Current directory |
| `..` | Parent directory |
| `~` | Current user's home directory |
| `/` | Root directory |

Example:

```
cd ..
cd ~
cd /
```

---

# Enterprise File Organization

A typical enterprise Linux server might organize files as follows:

```
/

├── boot
├── etc
├── home
├── opt
│   └── CompanyApp
├── srv
│   └── nginx
├── usr
├── var
│   ├── log
│   ├── lib
│   └── cache
└── tmp
```

Following standardized layouts simplifies automation, backups, monitoring, and incident response.

---

# Business Impact

A standardized filesystem hierarchy helps organizations:

- Simplify administration across servers.
- Reduce configuration errors.
- Improve automation.
- Accelerate troubleshooting.
- Support compliance requirements.
- Enable faster disaster recovery.

---

# Enterprise Best Practices

Organizations should:

- Avoid storing application data in system directories unless appropriate.
- Keep configuration files under `/etc`.
- Store logs under `/var/log`.
- Use `/opt` for third-party software.
- Regularly monitor filesystem usage.
- Protect sensitive configuration files with proper permissions.
- Maintain consistent directory structures across servers.

---

# Key Takeaways

- Linux organizes all files under a single root directory (`/`).
- The Filesystem Hierarchy Standard (FHS) defines consistent directory usage.
- Directories such as `/etc`, `/var`, `/home`, and `/usr` have specific administrative purposes.
- Virtual filesystems like `/proc` and `/sys` provide real-time system information.
- Understanding the filesystem hierarchy is essential for administration, troubleshooting, automation, and cybersecurity.

---


