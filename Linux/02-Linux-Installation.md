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


