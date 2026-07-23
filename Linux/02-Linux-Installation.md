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


