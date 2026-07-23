# 02 - Linux Installation

# Part 1 — Installation Overview, System Requirements, Installation Methods, Choosing a Distribution, BIOS vs UEFI, and Preparing Installation Media

---

# Introduction

Installing Linux is the first practical step toward becoming a Linux administrator, cybersecurity professional, cloud engineer, or DevOps engineer.

Linux can be installed in multiple ways depending on the intended use case. A cybersecurity student may prefer a virtual machine for safe experimentation, while an enterprise organization may deploy Linux on physical servers, cloud infrastructure, or containerized environments.

Understanding the different installation methods, firmware interfaces, and storage concepts ensures a reliable and secure deployment.

---

# Learning Objectives

After completing this section, you will be able to:

- Understand different Linux installation methods.
- Select an appropriate Linux distribution.
- Identify hardware requirements.
- Explain BIOS and UEFI firmware.
- Create bootable installation media.
- Plan storage and partitioning.
- Prepare systems for installation.

---

# Installation Workflow

A typical Linux installation follows these stages:

```text
Choose Distribution
        │
        ▼
Download ISO Image
        │
        ▼
Verify ISO Integrity
        │
        ▼
Create Bootable Media
        │
        ▼
Configure BIOS / UEFI
        │
        ▼
Boot Installer
        │
        ▼
Partition Storage
        │
        ▼
Install Linux
        │
        ▼
Configure System
        │
        ▼
Update Packages
```

Each stage contributes to a successful and secure deployment.

---

# What is an ISO Image?

An **ISO image** is a complete archive of an operating system installation disc.

It contains:

- Linux kernel
- Bootloader
- Installer
- Package repository
- Initial system utilities
- Installation scripts

Example filenames:

```text
ubuntu-24.04-live-server-amd64.iso

rocky-9.5-x86_64-dvd.iso

kali-linux-2026.2-installer-amd64.iso
```

---

# Why Verify ISO Integrity?

Before installing Linux, verify that the downloaded ISO image has not been corrupted or tampered with.

Verification helps ensure:

- Download integrity
- Protection against corruption
- Detection of unauthorized modifications
- Authentic installation media

Most Linux vendors publish SHA-256 or SHA-512 checksums alongside ISO downloads.

Example:

```bash
sha256sum ubuntu.iso
```

Compare the output with the checksum provided by the distribution's official website.

---

# Choosing the Right Linux Distribution

Different distributions are optimized for different purposes.

| Distribution | Best For |
|--------------|----------|
| Ubuntu LTS | Beginners, cloud, enterprise |
| Debian | Stable servers |
| Fedora | Developers, latest technologies |
| RHEL | Enterprise production environments |
| Rocky Linux | Enterprise server deployments |
| AlmaLinux | Community enterprise replacement |
| Kali Linux | Penetration testing |
| Parrot Security | Security assessments and forensics |
| Arch Linux | Advanced users |
| Linux Mint | Desktop users |

Choose a distribution that aligns with your learning goals or organizational requirements.

---

# Recommended Distributions by Role

| Role | Recommended Distribution |
|------|---------------------------|
| Beginner | Ubuntu LTS |
| Linux Administrator | Rocky Linux, Ubuntu Server |
| SOC Analyst | Ubuntu Server |
| DevOps Engineer | Ubuntu Server, Rocky Linux |
| Cloud Engineer | Ubuntu Server, RHEL |
| Cybersecurity Student | Ubuntu + Kali Linux (VM) |
| Penetration Tester | Kali Linux |
| Enterprise Administrator | RHEL, Rocky Linux, SUSE Linux Enterprise |

---

# Hardware Requirements

Hardware requirements vary depending on the distribution and intended workload.

Typical minimum requirements:

| Component | Minimum |
|-----------|---------|
| CPU | 64-bit dual-core |
| RAM | 2 GB |
| Storage | 25 GB |
| Network | Ethernet or Wi-Fi |
| Display | 1024 × 768 |

Recommended for learning in a virtual machine:

| Component | Recommended |
|-----------|-------------|
| CPU | 4 cores |
| RAM | 8 GB or more |
| Storage | 50–100 GB SSD |
| Virtualization | VT-x or AMD-V enabled |

---

# Installation Methods

Linux can be installed using several approaches.

## Physical Installation

Linux is installed directly onto a computer's internal storage.

Advantages:

- Full hardware performance
- No virtualization overhead
- Direct device access

Common use cases:

- Servers
- Workstations
- Dedicated appliances

---

## Virtual Machine Installation

Linux runs as a guest operating system within virtualization software.

Examples:

- Oracle VirtualBox
- VMware Workstation
- KVM
- Hyper-V

Advantages:

- Safe experimentation
- Easy snapshots
- Multiple operating systems
- Isolation from the host system

Widely used in cybersecurity training and labs.

---

## Dual Boot

Linux and another operating system (such as Windows) are installed on the same computer.

At startup, the bootloader allows the user to choose which operating system to boot.

Advantages:

- Native performance
- Access to both operating systems

Considerations:

- Requires disk partitioning
- Changes to one operating system can affect boot configuration

---

## Windows Subsystem for Linux (WSL)

WSL allows Linux user-space environments to run directly on Windows without a traditional virtual machine.

Benefits:

- Quick setup
- Low resource usage
- Access to Linux tools from Windows
- Integration with development workflows

WSL is particularly useful for developers and students but is not a full replacement for a dedicated Linux installation in all scenarios.

---

## Cloud Installation

Linux instances can be launched in cloud environments.

Examples:

- Amazon EC2
- Azure Virtual Machines
- Google Compute Engine
- Oracle Cloud Infrastructure

Benefits:

- Rapid deployment
- Elastic scaling
- Pay-as-you-go pricing
- Remote access via SSH

Cloud deployments are common in enterprise environments.

---

# Comparing Installation Methods

| Method | Performance | Isolation | Typical Use |
|---------|-------------|-----------|-------------|
| Physical Installation | Excellent | Low | Servers, workstations |
| Virtual Machine | Very Good | High | Learning, labs, testing |
| Dual Boot | Excellent | Low | Desktop users |
| WSL | Good | Moderate | Development |
| Cloud Instance | Depends on instance type | High | Production, cloud labs |

---

# BIOS

The **Basic Input/Output System (BIOS)** is legacy firmware that initializes hardware during system startup.

Responsibilities include:

- Power-on self-test (POST)
- Hardware initialization
- Boot device selection
- Handing control to the bootloader

Characteristics:

- Legacy technology
- Uses MBR partitioning
- Limited feature set compared to UEFI

---

# UEFI

The **Unified Extensible Firmware Interface (UEFI)** is the modern replacement for BIOS.

Advantages:

- Faster startup
- Secure Boot support
- GPT partition support
- Larger disk support
- Improved firmware interface
- Better security features

Most modern systems ship with UEFI firmware enabled by default.

---

# BIOS vs UEFI

| Feature | BIOS | UEFI |
|----------|------|------|
| Release Era | Legacy | Modern |
| Boot Method | MBR | GPT |
| Maximum Disk Size | ~2 TB | Greater than 2 TB |
| Secure Boot | Not Supported | Supported |
| Startup Speed | Slower | Faster |
| Interface | Text-based | Graphical (vendor-dependent) |

---

# Secure Boot

Secure Boot is a UEFI feature that helps prevent unauthorized bootloaders and operating systems from loading during startup.

Benefits:

- Protects against bootkits
- Verifies trusted boot components
- Improves platform integrity

Some Linux distributions support Secure Boot out of the box, while others may require additional configuration.

---

# MBR vs GPT

Storage devices use partition tables to organize disk partitions.

| Feature | MBR | GPT |
|----------|-----|-----|
| Maximum Disk Size | ~2 TB | Greater than 2 TB |
| Maximum Primary Partitions | 4 | 128 (typical) |
| Redundancy | No | Yes |
| Firmware Compatibility | BIOS | UEFI |

GPT is recommended for modern systems.

---

# Downloading Linux

Always download installation images from official distribution websites.

General recommendations:

- Select the correct architecture (typically 64-bit x86_64/amd64).
- Choose Long-Term Support (LTS) releases when available for stability.
- Verify checksums before use.
- Avoid downloading ISOs from unofficial sources.

---

# Creating Bootable Installation Media

A bootable USB drive allows a system to start the Linux installer.

Common tools include:

| Operating System | Tool |
|------------------|------|
| Windows | Rufus, balenaEtcher |
| Linux | `dd`, GNOME Disks, Ventoy |
| macOS | balenaEtcher |

Typical USB size:

- 8 GB or larger

---

# Preparing for Installation

Before beginning installation:

- Back up important data.
- Verify hardware compatibility.
- Confirm firmware mode (BIOS or UEFI).
- Enable virtualization extensions if using virtual machines.
- Download the correct ISO image.
- Verify the ISO checksum.
- Prepare bootable media.
- Ensure stable power for laptops and workstations.

---

# Enterprise Deployment Considerations

Enterprise Linux deployments often involve:

- Standardized installation images
- Automated installation frameworks
- Centralized configuration management
- Secure boot policies
- Disk encryption
- Consistent partition layouts
- Configuration baselines
- Asset inventory integration

Automation tools help ensure consistency across large fleets of systems.

---

# Business Impact

A well-planned installation process helps organizations:

- Reduce deployment errors.
- Improve system reliability.
- Accelerate provisioning.
- Maintain security compliance.
- Standardize infrastructure.
- Simplify lifecycle management.

---

# Enterprise Best Practices

- Use supported Long-Term Support (LTS) or enterprise releases.
- Verify installation media before deployment.
- Prefer UEFI with GPT on modern hardware.
- Maintain documented installation procedures.
- Standardize partition layouts.
- Apply security updates immediately after installation.
- Record installed software versions and configuration baselines.

---

# Key Takeaways

- Linux can be installed on physical hardware, virtual machines, cloud platforms, WSL, or dual-boot systems.
- Choosing the right distribution depends on your use case and organizational requirements.
- Verify ISO integrity before installation.
- UEFI with GPT is recommended for modern systems.
- Proper preparation reduces deployment risk and improves security.

---


# Part 2 — Virtual Machines, VirtualBox, VMware, Hyper-V, KVM, Windows Subsystem for Linux (WSL), Cloud Instances, and Enterprise Deployment Methods

---

# Introduction

Most Linux professionals do **not** begin by installing Linux directly on their primary computer. Instead, they use **virtualization** to safely create isolated Linux environments.

Virtual machines allow multiple operating systems to run simultaneously on the same physical computer without affecting one another. This makes virtualization the preferred method for:

- Learning Linux
- Cybersecurity Labs
- SOC Training
- Penetration Testing
- Malware Analysis
- Software Development
- DevOps
- Cloud Testing

Enterprise organizations also rely heavily on virtualization to maximize hardware utilization, improve scalability, simplify disaster recovery, and reduce infrastructure costs.

---

# What is Virtualization?

Virtualization is the process of creating a **virtual version of a physical computer**.

Instead of installing Linux directly on hardware, a virtualization platform creates virtual hardware such as:

- CPU
- RAM
- Hard Disk
- Network Adapter
- USB Controller
- Graphics Adapter

The guest operating system (Linux) believes it is running on a real computer.

---

# Virtualization Architecture

```text
+----------------------------------------------------+
|               Guest Operating System               |
|               Ubuntu / Rocky / Kali               |
+----------------------------------------------------+
|              Virtual Hardware Layer                |
| CPU | RAM | Disk | NIC | USB | Graphics           |
+----------------------------------------------------+
|                 Hypervisor                         |
| VirtualBox / VMware / Hyper-V / KVM               |
+----------------------------------------------------+
|                 Host Operating System              |
| Windows / Linux / macOS                           |
+----------------------------------------------------+
|                Physical Hardware                   |
+----------------------------------------------------+
```

---

# Advantages of Virtual Machines

Virtual machines provide several benefits.

- Safe testing environment
- Easy rollback using snapshots
- Multiple operating systems on one computer
- Hardware isolation
- Malware containment
- Resource flexibility
- Simple backup and migration

---

# Virtual Machine Terminology

| Term | Description |
|------|-------------|
| Host | Physical computer running virtualization software |
| Guest | Virtual operating system |
| Hypervisor | Software that manages virtual machines |
| Snapshot | Saved state of a VM |
| Clone | Copy of an existing VM |
| Virtual Disk | Disk image used by the VM |

---

# What is a Hypervisor?

A **hypervisor** manages virtual machines by allocating hardware resources such as CPU, memory, storage, and networking.

There are two main categories of hypervisors.

---

# Type 1 Hypervisor (Bare Metal)

Runs directly on physical hardware.

Examples:

- VMware ESXi
- Microsoft Hyper-V Server
- Xen
- KVM (Linux Kernel-based)

Advantages:

- High performance
- Better security
- Enterprise scalability
- Used in production data centers

---

# Type 2 Hypervisor (Hosted)

Runs as an application on top of an existing operating system.

Examples:

- Oracle VirtualBox
- VMware Workstation
- VMware Fusion
- Parallels Desktop

Advantages:

- Easy installation
- Ideal for learning
- Suitable for development and testing

---

# Type 1 vs Type 2 Hypervisors

| Feature | Type 1 | Type 2 |
|----------|--------|--------|
| Runs On | Hardware | Existing OS |
| Performance | Higher | Slightly Lower |
| Enterprise Usage | Common | Less Common |
| Learning | Moderate | Excellent |
| Examples | ESXi, KVM | VirtualBox, VMware Workstation |

---

# Oracle VirtualBox

VirtualBox is a free and open-source Type 2 hypervisor developed by Oracle.

Supported host operating systems:

- Windows
- Linux
- macOS

Features:

- Snapshots
- Shared folders
- USB passthrough
- Multiple virtual networks
- Guest additions
- Full-screen mode

VirtualBox is one of the most popular tools for students and cybersecurity labs.

---

# Creating a Virtual Machine in VirtualBox

Typical workflow:

```text
Install VirtualBox
        │
        ▼
Create New VM
        │
        ▼
Select Linux ISO
        │
        ▼
Allocate RAM
        │
        ▼
Create Virtual Disk
        │
        ▼
Configure Network
        │
        ▼
Start Installation
```

---

# Recommended VirtualBox Resources

| Resource | Recommended |
|----------|-------------|
| CPU | 2–4 Cores |
| RAM | 4–8 GB |
| Disk | 40–80 GB |
| Video Memory | 128 MB |
| Network | NAT or Bridged |

---

# VMware Workstation

VMware Workstation is a commercial Type 2 hypervisor widely used by professionals.

Key features:

- High performance
- Advanced networking
- Snapshots
- Cloning
- Virtual TPM support
- Better hardware compatibility
- Enterprise integrations

It is commonly used in enterprise development and cybersecurity environments.

---

# VirtualBox vs VMware

| Feature | VirtualBox | VMware Workstation |
|----------|------------|-------------------|
| License | Free | Commercial (some editions free for personal use) |
| Performance | Very Good | Excellent |
| Snapshots | Yes | Yes |
| USB Support | Yes | Yes |
| Enterprise Adoption | Moderate | High |
| Ease of Use | Excellent | Excellent |

---

# Microsoft Hyper-V

Hyper-V is Microsoft's built-in virtualization platform available on supported Windows editions.

Advantages:

- Native Windows integration
- Good performance
- Virtual networking
- Secure Boot support
- Dynamic memory allocation

Hyper-V is frequently used in Windows-based enterprise environments.

---

# KVM (Kernel-based Virtual Machine)

KVM is a Type 1 hypervisor built directly into the Linux kernel.

Advantages:

- Excellent performance
- Open source
- Enterprise-ready
- Integrated with Linux
- Supports virtualization extensions

Many cloud providers and enterprise data centers use KVM.

---

# Comparing Popular Virtualization Platforms

| Platform | Host OS | Type | Enterprise Use |
|----------|----------|------|----------------|
| VirtualBox | Windows, Linux, macOS | Type 2 | Moderate |
| VMware Workstation | Windows, Linux | Type 2 | High |
| Hyper-V | Windows | Type 1 | High |
| KVM | Linux | Type 1 | Very High |

---

# Snapshots

A snapshot captures the current state of a virtual machine.

It stores:

- Disk state
- Memory state (optional)
- Device configuration

Benefits:

- Roll back after failed updates
- Restore malware lab environments
- Test software safely
- Experiment without permanent changes

Snapshots are heavily used in cybersecurity training.

---

# Cloning

A clone is a copy of an existing virtual machine.

Two common types:

- Full Clone
- Linked Clone

Advantages:

- Rapid lab deployment
- Standardized environments
- Easy distribution to students or teams

---

# Virtual Networking

Virtual machines support multiple network configurations.

Common modes include:

| Mode | Description |
|------|-------------|
| NAT | Shares the host's internet connection; guest is hidden behind the host |
| Bridged | Guest appears as a separate device on the physical network |
| Host-Only | Communication only between host and guest(s) |
| Internal Network | Communication only among VMs on the same internal network |

Choose the mode based on the lab or production requirements.

---

# Windows Subsystem for Linux (WSL)

WSL allows Linux user-space environments to run directly on Windows.

Benefits:

- Fast startup
- Minimal overhead
- Integration with Windows tools
- Access to Linux command-line utilities
- Suitable for development and scripting

WSL is convenient for learning basic Linux commands and development workflows.

---

# WSL 1 vs WSL 2

| Feature | WSL 1 | WSL 2 |
|----------|-------|-------|
| Kernel | Translation layer | Real Linux kernel |
| Performance | Good | Better for filesystem-intensive tasks |
| Docker Support | Limited | Excellent |
| Compatibility | Moderate | High |

WSL 2 is recommended for most modern development use cases.

---

# Cloud Linux Instances

Cloud providers make it possible to launch Linux servers in minutes.

Typical workflow:

```text
Create Cloud Account
        │
        ▼
Choose Region
        │
        ▼
Select Linux Image
        │
        ▼
Choose Instance Size
        │
        ▼
Configure Networking
        │
        ▼
Generate SSH Keys
        │
        ▼
Launch Instance
        │
        ▼
Connect via SSH
```

Cloud instances are ideal for learning cloud administration and practicing remote Linux management.

---

# Common Enterprise Deployment Methods

Organizations deploy Linux using several approaches.

- Manual installation
- Automated installation (Kickstart, AutoYaST, Preseed, Autoinstall)
- Virtual machine templates
- Golden images
- Infrastructure as Code (IaC)
- Cloud images
- Container images

Automation improves consistency and reduces deployment time.

---

# Golden Images

A **golden image** is a preconfigured operating system image that includes:

- Approved packages
- Security settings
- Baseline configurations
- Monitoring agents
- Compliance policies

Benefits:

- Consistent deployments
- Faster provisioning
- Reduced configuration drift
- Simplified patch management

---

# Infrastructure as Code (IaC)

Infrastructure as Code automates the provisioning of servers and infrastructure.

Common tools include:

- Terraform
- Ansible
- Puppet
- Chef

These tools help deploy Linux systems consistently across on-premises and cloud environments.

---

# Enterprise Deployment Workflow

```text
Standard Image
        │
        ▼
Automated Provisioning
        │
        ▼
Configuration Management
        │
        ▼
Security Hardening
        │
        ▼
Monitoring & Logging
        │
        ▼
Production Deployment
```

---

# Business Impact

Virtualization and automated deployment provide organizations with:

- Faster provisioning
- Lower hardware costs
- Improved resource utilization
- Rapid disaster recovery
- Easier testing
- Scalable infrastructure
- Standardized environments

---

# Enterprise Best Practices

- Use virtualization for learning and testing.
- Allocate adequate CPU, memory, and storage to VMs.
- Take snapshots before major changes.
- Use bridged networking only when necessary.
- Prefer WSL 2 for Windows-based development.
- Standardize on approved VM templates and golden images.
- Automate deployments whenever possible.
- Secure cloud instances with SSH keys and least-privilege access.

---

# Key Takeaways

- Virtualization allows Linux to run safely alongside other operating systems.
- Hypervisors manage virtual hardware and guest operating systems.
- VirtualBox, VMware, Hyper-V, and KVM each serve different use cases.
- WSL provides a lightweight Linux environment on Windows.
- Cloud instances enable rapid Linux deployment for development and production.
- Enterprise organizations rely on automation, golden images, and Infrastructure as Code to deploy Linux consistently.

---


# Part 3 — Installing Linux in VirtualBox & VMware, Disk Partitioning, Filesystem Selection, LVM, Swap, and Step-by-Step Installation Walkthrough

---

# Introduction

After selecting a Linux distribution and understanding virtualization platforms, the next step is installing Linux.

Although installers differ slightly between distributions such as Ubuntu, Rocky Linux, Debian, Fedora, and Kali Linux, the overall installation workflow is remarkably similar.

Understanding what happens during installation helps administrators:

- Build secure systems
- Design proper storage layouts
- Improve disaster recovery
- Simplify future upgrades
- Standardize enterprise deployments

---

# Linux Installation Workflow

```text
Download ISO
      │
      ▼
Create Virtual Machine
      │
      ▼
Attach ISO
      │
      ▼
Boot Installer
      │
      ▼
Choose Language
      │
      ▼
Configure Keyboard
      │
      ▼
Configure Network
      │
      ▼
Partition Disk
      │
      ▼
Install Packages
      │
      ▼
Create User
      │
      ▼
Install Bootloader
      │
      ▼
Reboot
```

---

# Installing Linux in VirtualBox

## Step 1 — Create a New Virtual Machine

Open VirtualBox and select:

```
New
```

Provide:

| Setting | Example |
|----------|----------|
| Name | Ubuntu Server |
| Type | Linux |
| Version | Ubuntu (64-bit) |

---

## Step 2 — Allocate Memory

Recommended RAM:

| Purpose | RAM |
|----------|-----|
| CLI Practice | 2 GB |
| Desktop | 4 GB |
| Development | 8 GB |
| Kubernetes | 8–16 GB |

Never allocate all available RAM to the VM.

---

## Step 3 — Configure CPU

Recommended allocation:

| Host CPU | Guest CPU |
|-----------|-----------|
| 4 Cores | 2 |
| 8 Cores | 4 |
| 16 Cores | 6–8 |

Avoid assigning every CPU core to a single VM.

---

## Step 4 — Create Virtual Hard Disk

Choose:

```
VDI (VirtualBox Disk Image)
```

Storage type:

```
Dynamically Allocated
```

Recommended sizes:

| Usage | Disk Size |
|---------|-----------|
| Learning | 30 GB |
| Development | 60 GB |
| Server Lab | 80 GB |
| Kubernetes | 100 GB |

---

## Step 5 — Attach Linux ISO

Navigate to:

```
Settings

↓

Storage

↓

Optical Drive

↓

Choose ISO
```

Select the downloaded Linux ISO.

---

## Step 6 — Configure Networking

Default:

```
NAT
```

Alternative:

```
Bridged Adapter
```

Choose based on whether the VM needs to appear directly on the physical network.

---

# Installing Linux in VMware

VMware installation is very similar.

Typical workflow:

```
Create VM

↓

Select ISO

↓

Allocate CPU

↓

Allocate RAM

↓

Create Disk

↓

Configure Network

↓

Power On

↓

Install Linux
```

VMware often detects Linux distributions automatically and suggests optimized settings.

---

# Booting the Installer

After powering on the VM:

```
GRUB Menu

↓

Try or Install Linux

↓

Start Installer
```

Some distributions provide:

- Live Environment
- Memory Test
- Rescue Mode
- OEM Installation

---

# Language Selection

Choose the preferred installation language.

Example:

```
English (US)
```

The selected language determines:

- Installer interface
- System locale
- Default language settings

---

# Keyboard Layout

Examples:

```
US

UK

German

French

Japanese
```

Test the layout before continuing to avoid password entry issues later.

---

# Time Zone

Choose:

```
Asia/Kolkata
```

or

```
UTC
```

Servers often use **UTC** to simplify log correlation across multiple regions.

---

# Network Configuration

Options include:

```
Automatic (DHCP)

Static IP
```

Enterprise servers commonly use static IP addresses, while desktop systems typically rely on DHCP.

---

# Hostname

The hostname identifies the machine on a network.

Example:

```
ubuntu-server

soc-lab

web01

db01

kali-lab
```

Enterprise naming conventions usually reflect the server's role or location.

---

# Creating Users

Most installers create:

- Root account (or disable direct root login)
- Standard administrative user

Example:

```
Username:

anurag

Password:

********
```

Use strong, unique passwords for all accounts.

---

# Disk Partitioning

Disk partitioning divides a storage device into logical sections.

Example:

```
Disk

↓

Partition 1

↓

Partition 2

↓

Partition 3
```

Each partition serves a specific purpose.

---

# Automatic Partitioning

Recommended for beginners.

The installer automatically creates the required partitions.

Advantages:

- Fast
- Simple
- Minimal configuration

---

# Manual Partitioning

Recommended for:

- Servers
- Enterprise systems
- Advanced users

Advantages:

- Better organization
- Improved security
- Easier backups
- Separate growth management

---

# Typical Linux Partition Layout

```text
Disk

├── EFI System Partition
├── /
├── /home
├── swap
└── /var (optional)
```

Large enterprise deployments may also use dedicated partitions for `/tmp`, `/opt`, or application data.

---

# EFI System Partition (ESP)

Purpose:

- Stores UEFI boot files
- Required for UEFI systems

Typical size:

```
512 MB
```

Filesystem:

```
FAT32
```

Mount point:

```
/boot/efi
```

---

# Root Partition

Mount point:

```
/
```

Contains:

- Operating system
- Applications
- Libraries
- Configuration
- Kernel

Recommended sizes:

| Environment | Size |
|--------------|------|
| Desktop | 30–50 GB |
| Server | 40–80 GB |
| Enterprise | Depends on workload |

---

# Home Partition

Mount point:

```
/home
```

Stores:

- User files
- Documents
- Downloads
- Desktop settings
- SSH keys

Separating `/home` simplifies OS reinstalls while preserving user data.

---

# Swap Partition

Swap extends virtual memory by using disk space when RAM is exhausted.

Benefits:

- Prevents crashes due to memory exhaustion
- Supports hibernation (if configured)
- Handles temporary memory spikes

General guidance:

| RAM | Suggested Swap |
|------|----------------|
| 2 GB | 2 GB |
| 4 GB | 2–4 GB |
| 8 GB | 4 GB |
| 16 GB+ | 4–8 GB (workload dependent) |

Modern systems with ample RAM often require only modest swap space.

---

# What is LVM?

**Logical Volume Manager (LVM)** provides flexible storage management by abstracting physical storage into logical volumes.

Advantages:

- Resize partitions without reinstalling
- Add new storage easily
- Create snapshots
- Simplify storage administration

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
```

---

# Benefits of LVM

- Online volume expansion
- Flexible storage allocation
- Easier migration
- Snapshot support
- Better storage utilization

LVM is widely used in enterprise Linux environments.

---

# Choosing a Filesystem

The filesystem determines how data is stored and retrieved.

Common options:

| Filesystem | Common Use |
|------------|------------|
| ext4 | General purpose |
| XFS | Enterprise servers |
| Btrfs | Snapshots and advanced features |
| FAT32 | EFI partition |
| exFAT | Removable media |

---

# ext4

Features:

- Stable
- Journaling
- Excellent compatibility
- Low maintenance

Best suited for:

- Desktop
- Servers
- General-purpose systems

---

# XFS

Features:

- High performance
- Excellent scalability
- Supports very large filesystems
- Online filesystem expansion

Often the default filesystem for enterprise distributions such as Red Hat Enterprise Linux and Rocky Linux.

---

# Btrfs

Features:

- Snapshots
- Checksums
- Compression
- Copy-on-write
- Advanced volume management

Suitable for systems requiring advanced storage features.

---

# Installation Summary

Before installation begins, the installer typically displays a summary of:

- Language
- Keyboard
- Time zone
- User account
- Storage layout
- Filesystem
- Bootloader location

Review this information carefully before proceeding.

---

# Installing the Operating System

The installer then:

- Formats partitions
- Copies system files
- Installs packages
- Configures services
- Installs the bootloader
- Generates initial configuration

Installation time varies based on hardware performance and the selected software.

---

# Reboot

After installation:

```text
Installation Complete

↓

Restart System
```

Remove the installation ISO if prompted to prevent booting back into the installer.

---

# First Boot

On the first boot, you should see:

```text
GRUB

↓

Linux Kernel

↓

Login Screen

↓

Desktop or Terminal
```

The system is now ready for post-installation configuration.

---

# Business Impact

Proper partitioning and filesystem selection improve:

- Performance
- Reliability
- Backup strategies
- Disaster recovery
- Security
- Storage scalability

---

# Enterprise Best Practices

- Use GPT with UEFI on modern hardware.
- Allocate separate partitions for critical data where appropriate (for example, `/home`, `/var`, or application data).
- Use LVM for servers that require flexible storage management.
- Choose a filesystem appropriate for the workload (`ext4` for general use, `XFS` for many enterprise servers).
- Review installation settings carefully before formatting disks.
- Remove installation media after the first successful boot.
- Document partition layouts and storage configurations.

---

# Key Takeaways

- Installing Linux in VirtualBox and VMware follows a similar workflow.
- Automatic partitioning is suitable for beginners, while manual partitioning offers greater control.
- GPT and UEFI are the preferred standards for modern systems.
- LVM provides flexible, enterprise-grade storage management.
- Selecting the right filesystem and partition layout is critical for performance, maintainability, and scalability.

---

# Part 4 — Post-Installation Configuration, Package Updates, User Management, SSH Setup, Essential Software, Enterprise Hardening, Practical Labs, Summary, Interview Questions, and References

---

# Introduction

Installing Linux is only the beginning. A freshly installed system should **never** be considered production-ready.

Before the system is used for development, enterprise workloads, or cybersecurity labs, administrators should perform a series of post-installation tasks to:

- Apply security updates
- Configure users
- Enable secure remote administration
- Install essential tools
- Configure networking
- Harden the operating system
- Enable monitoring and logging

These steps help create a secure, stable, and maintainable Linux environment.

---

# First Login

After rebooting, log in using the account created during installation.

Example:

```text
Username: anurag
Password: ********
```

Verify the system is functioning correctly before making additional changes.

---

# Verify System Information

Check the currently running kernel:

```bash
uname -r
```

Example output:

```text
6.8.0-31-generic
```

Display detailed kernel information:

```bash
uname -a
```

---

# Check Linux Distribution

Display distribution details:

Ubuntu/Debian:

```bash
cat /etc/os-release
```

Example:

```text
NAME="Ubuntu"
VERSION="24.04 LTS"
```

---

# Verify Hostname

Display hostname:

```bash
hostname
```

Change hostname temporarily:

```bash
hostname new-server
```

Modern systems should use:

```bash
hostnamectl set-hostname web01
```

Verify:

```bash
hostnamectl
```

---

# Verify Date and Time

Check current time:

```bash
date
```

View detailed status:

```bash
timedatectl
```

Synchronize time using NTP if required.

Accurate time is critical for:

- Authentication
- Kerberos
- SIEM
- Log correlation
- Incident response

---

# Update Package Repository

Ubuntu/Debian:

```bash
sudo apt update
```

Rocky Linux / AlmaLinux:

```bash
sudo dnf check-update
```

Updating package metadata ensures the system knows about the latest available software.

---

# Upgrade Installed Packages

Ubuntu:

```bash
sudo apt upgrade
```

Rocky Linux:

```bash
sudo dnf upgrade
```

Benefits:

- Security patches
- Bug fixes
- Performance improvements
- Stability updates

Always update a newly installed system before using it.

---

# Install Essential Packages

Examples:

Ubuntu:

```bash
sudo apt install \
curl \
wget \
git \
vim \
htop \
net-tools \
openssh-server
```

Rocky:

```bash
sudo dnf install \
curl \
wget \
git \
vim \
htop \
net-tools \
openssh-server
```

These utilities are commonly required for administration and troubleshooting.

---

# Verify Network Connectivity

Test internet connectivity:

```bash
ping google.com
```

Or test a specific IP:

```bash
ping 8.8.8.8
```

Successful replies confirm basic network connectivity.

---

# Check IP Address

Modern command:

```bash
ip addr
```

Short form:

```bash
ip a
```

Example output:

```text
192.168.1.50/24
```

---

# Check Default Gateway

```bash
ip route
```

Example:

```text
default via 192.168.1.1
```

---

# Verify DNS Resolution

```bash
dig openai.com
```

or

```bash
nslookup openai.com
```

Proper DNS resolution is essential for package updates, cloud services, and internet access.

---

# Create Additional Users

Example:

```bash
sudo useradd analyst
```

Create a home directory:

```bash
sudo useradd -m analyst
```

Assign password:

```bash
sudo passwd analyst
```

---

# Grant Administrative Privileges

Ubuntu:

```bash
sudo usermod -aG sudo analyst
```

Rocky Linux:

```bash
sudo usermod -aG wheel analyst
```

Always follow the principle of least privilege.

---

# Verify Groups

```bash
groups analyst
```

Example:

```text
analyst sudo
```

---

# Configure SSH

Install OpenSSH Server (if not already installed):

Ubuntu:

```bash
sudo apt install openssh-server
```

Enable service:

```bash
sudo systemctl enable ssh
```

Start service:

```bash
sudo systemctl start ssh
```

Verify:

```bash
sudo systemctl status ssh
```

---

# Test Remote Access

From another Linux system:

```bash
ssh username@server-ip
```

Example:

```bash
ssh anurag@192.168.1.50
```

---

# Generate SSH Keys

Generate a modern ED25519 key pair:

```bash
ssh-keygen -t ed25519
```

Default files:

```text
~/.ssh/id_ed25519
~/.ssh/id_ed25519.pub
```

Public keys can be added to `~/.ssh/authorized_keys` on remote systems for passwordless authentication.

---

# Configure Firewall

Ubuntu (UFW):

```bash
sudo ufw enable
```

Allow SSH:

```bash
sudo ufw allow ssh
```

View rules:

```bash
sudo ufw status
```

Rocky Linux (firewalld):

```bash
sudo systemctl enable firewalld
sudo systemctl start firewalld
```

Allow SSH:

```bash
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --reload
```

---

# Enable Automatic Security Updates

Ubuntu:

```bash
sudo apt install unattended-upgrades
```

Automatic updates reduce the window of exposure to known vulnerabilities.

In enterprise environments, updates should follow established testing and change-management procedures.

---

# Configure Swap (If Required)

Display swap usage:

```bash
swapon --show
```

Memory statistics:

```bash
free -h
```

If no swap is configured and workloads require it, create a swap file following your distribution's documentation.

---

# Install Development Tools

Common packages:

```bash
git
python3
pip
gcc
make
cmake
```

Useful for:

- Programming
- DevOps
- Security tools
- Automation

---

# Install Monitoring Tools

Examples:

```bash
htop
iotop
iftop
btop
sysstat
```

These utilities help analyze:

- CPU
- Memory
- Storage
- Network
- Processes

---

# Configure Log Rotation

Most distributions include `logrotate` by default.

Verify:

```bash
logrotate --version
```

Log rotation helps:

- Prevent disks from filling
- Archive historical logs
- Improve log management

---

# Backup Important Configuration Files

Examples:

```bash
/etc/
/home/
/var/log/
/etc/ssh/
```

Configuration backups simplify disaster recovery and change rollback.

---

# Enterprise Hardening Checklist

Recommended actions after installation:

- Apply all security updates.
- Disable unused services.
- Remove unnecessary packages.
- Configure a firewall.
- Enable SSH key authentication.
- Disable direct root login over SSH.
- Use strong password policies.
- Synchronize time with NTP.
- Enable centralized logging.
- Monitor system resources.
- Configure automatic backups.
- Document system configuration.

---

# Enterprise Deployment Workflow

```text
Install Linux
        │
        ▼
Update Packages
        │
        ▼
Configure Users
        │
        ▼
Configure SSH
        │
        ▼
Enable Firewall
        │
        ▼
Install Monitoring
        │
        ▼
Apply Hardening
        │
        ▼
Backup Configuration
        │
        ▼
Production Ready
```

---

# Practical Lab 1 — Update the System

Commands:

```bash
sudo apt update
sudo apt upgrade
```

Objective:

- Refresh package metadata.
- Install available updates.

---

# Practical Lab 2 — Create a User

Commands:

```bash
sudo useradd -m analyst
sudo passwd analyst
groups analyst
```

Objective:

- Create and verify a standard user account.

---

# Practical Lab 3 — Enable SSH

Commands:

```bash
sudo systemctl enable ssh
sudo systemctl start ssh
sudo systemctl status ssh
```

Objective:

- Configure secure remote administration.

---

# Practical Lab 4 — Verify Networking

Commands:

```bash
ip a
ip route
ping 8.8.8.8
```

Objective:

- Confirm IP configuration, routing, and connectivity.

---

# Practical Lab 5 — Configure the Firewall

Ubuntu:

```bash
sudo ufw enable
sudo ufw allow ssh
sudo ufw status
```

Objective:

- Enable basic host firewall protection.

---

# Chapter Summary

In this chapter, you learned:

- Different Linux installation methods.
- Choosing the right Linux distribution.
- BIOS, UEFI, MBR, and GPT concepts.
- VirtualBox, VMware, Hyper-V, and KVM.
- Installing Linux in a virtual machine.
- Disk partitioning strategies.
- Filesystem selection.
- Logical Volume Manager (LVM).
- Post-installation configuration.
- User management.
- SSH setup.
- Firewall configuration.
- Initial enterprise hardening practices.

---

# Interview Questions

## Beginner

1. What is an ISO image?
2. What is the purpose of UEFI?
3. What is the difference between GPT and MBR?
4. What is a virtual machine?
5. Why would you use VirtualBox?
6. What is LVM?
7. What is swap memory?
8. How do you update packages on Ubuntu?
9. How do you display your IP address?
10. What is SSH used for?

---

## Intermediate

1. Compare VirtualBox and VMware Workstation.
2. Explain NAT and Bridged networking.
3. Why is GPT preferred over MBR?
4. What are the benefits of LVM?
5. Why separate `/home` from `/`?
6. How do you secure SSH access?
7. Why is NTP important?
8. What is a golden image?
9. What are Infrastructure as Code (IaC) tools?
10. Describe a typical enterprise post-installation checklist.

---

## Advanced

1. How would you standardize Linux deployments across hundreds of servers?
2. When would you choose XFS over ext4?
3. How would you automate Linux installations?
4. What security controls should be applied before placing a server into production?
5. How would you troubleshoot a Linux VM that cannot access the network?
6. How would you securely manage administrator access across an enterprise?
7. How do snapshots differ from backups?
8. How would you prepare a hardened base image for cloud deployments?
9. What are the risks of enabling password-based SSH authentication?
10. How would you integrate a newly installed Linux server into enterprise monitoring and logging?

---

# Key Takeaways

- Installation is only the first stage of the Linux lifecycle.
- Updating packages and configuring secure access are essential post-installation tasks.
- SSH, firewalls, monitoring, and backups form the foundation of a secure Linux deployment.
- Standardized deployment and hardening practices improve security, reliability, and maintainability.
- Proper post-installation configuration prepares Linux systems for enterprise, cloud, and cybersecurity workloads.

---

# References

## Official Documentation

- Ubuntu Documentation
- Debian Documentation
- Red Hat Enterprise Linux Documentation
- Rocky Linux Documentation
- AlmaLinux Documentation
- Fedora Documentation
- Linux Foundation Documentation

## Standards & Best Practices

- NIST SP 800 Series
- CIS Linux Benchmarks
- POSIX (IEEE 1003.1)
- Linux Standard Base (LSB)
- Filesystem Hierarchy Standard (FHS)

---

# Next Chapter

➡️ **03-Linux-Architecture.md**

Topics covered:

- Linux Architecture Overview
- Kernel Internals
- User Space vs Kernel Space
- System Calls
- Process Management
- Memory Management
- Device Drivers
- Linux Security Modules (LSM)
- Kernel Modules
- Boot Architecture
- Enterprise Linux Architecture
- Performance Considerations
- Cybersecurity Relevance