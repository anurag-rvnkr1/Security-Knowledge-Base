# 02-Windows-Installation.md

# Part 1 — Windows Installation Fundamentals, Hardware Requirements, BIOS/UEFI, GPT/MBR, and Installation Methods

---

# Introduction

Installing Windows correctly is the foundation of a stable, secure, and high-performing system. Whether deploying a personal laptop, an enterprise workstation, or a Windows Server, understanding the installation process is essential for IT administrators, cloud engineers, and cybersecurity professionals.

This chapter covers Windows installation from beginner to enterprise level.

---

# Learning Objectives

By the end of this chapter, you will understand:

- Windows installation workflow
- Hardware requirements
- BIOS vs UEFI
- Legacy Boot vs UEFI Boot
- MBR vs GPT partition styles
- Windows installation methods
- Installation media creation
- Secure Boot
- TPM
- Enterprise deployment overview
- Best practices
- Practical labs

---

# Windows Installation Overview

A typical Windows installation follows this sequence:

```text
Power On

↓

Firmware Initialization (BIOS/UEFI)

↓

Boot Device Selected

↓

Windows Installation Media

↓

Windows Setup

↓

Partition Selection

↓

File Copy

↓

Driver Installation

↓

Configuration

↓

User Setup

↓

Desktop Ready
```

---

# Why Proper Installation Matters

A properly installed Windows system provides:

- Better performance
- Improved stability
- Enhanced security
- Reliable updates
- Easier maintenance
- Enterprise compliance
- Reduced troubleshooting

Improper installations can lead to:

- Boot failures
- Driver incompatibility
- Data loss
- Performance issues
- Security risks

---

# Windows Hardware Requirements

Hardware requirements vary by Windows version. The table below reflects modern Windows 11 requirements and serves as a reference for current enterprise deployments.

| Component | Minimum Requirement |
|-----------|---------------------|
| Processor | 64-bit CPU, 2 or more cores, 1 GHz or faster |
| RAM | 4 GB |
| Storage | 64 GB or larger |
| Firmware | UEFI |
| TPM | TPM 2.0 |
| Graphics | DirectX 12 compatible |
| Display | HD (720p) or higher |
| Internet | Required for some editions and setup scenarios |

> Enterprise deployments often exceed these minimums to improve user experience and support business applications.

---

# Recommended Enterprise Hardware

| Component | Recommended |
|-----------|-------------|
| CPU | Quad-core or higher |
| RAM | 16 GB or more |
| Storage | NVMe SSD (512 GB or larger) |
| TPM | TPM 2.0 |
| Firmware | UEFI with Secure Boot |
| Network | Gigabit Ethernet and Wi-Fi 6/6E where available |

---

# Firmware Basics

Before Windows starts, the system firmware initializes hardware and prepares the computer to boot.

There are two primary firmware types:

```text
Firmware

├── Legacy BIOS
└── UEFI
```

---

# BIOS (Basic Input/Output System)

BIOS is the traditional firmware used by older computers.

Responsibilities:

- Perform Power-On Self-Test (POST)
- Detect hardware
- Locate a boot device
- Load the bootloader

Limitations:

- Supports only MBR boot
- Limited graphical interface
- No Secure Boot
- Limited disk size support

---

# UEFI (Unified Extensible Firmware Interface)

UEFI is the modern firmware standard.

Responsibilities:

- Hardware initialization
- Secure Boot support
- Faster startup
- GPT support
- Advanced firmware interface

Advantages:

- Faster boot time
- Better security
- Larger disk support
- Modern hardware compatibility
- Improved recovery features

---

# BIOS vs UEFI

| BIOS | UEFI |
|------|------|
| Older firmware | Modern firmware |
| Text-based interface | Graphical interface (vendor dependent) |
| Uses MBR | Uses GPT (recommended) |
| No Secure Boot | Secure Boot supported |
| Slower startup | Faster startup |
| Limited disk size support | Supports very large disks |

---

# Legacy Boot vs UEFI Boot

```text
Legacy Boot

Power

↓

BIOS

↓

MBR

↓

Bootloader

↓

Windows



UEFI Boot

Power

↓

UEFI

↓

EFI System Partition

↓

Windows Boot Manager

↓

Windows
```

---

# MBR (Master Boot Record)

MBR is the traditional partitioning scheme.

Characteristics:

- Supports up to 2 TB disks
- Maximum of four primary partitions
- Used with Legacy BIOS systems

Advantages:

- Broad compatibility with older hardware

Limitations:

- Limited partition count
- Disk size limitations

---

# GPT (GUID Partition Table)

GPT is the modern partitioning standard.

Characteristics:

- Supports disks larger than 2 TB
- Supports many partitions (Windows commonly supports up to 128)
- Required for modern UEFI installations

Advantages:

- Improved reliability
- Redundant partition information
- Better recovery
- Enterprise standard

---

# MBR vs GPT

| MBR | GPT |
|------|------|
| Legacy standard | Modern standard |
| Up to 2 TB | Supports much larger disks |
| Four primary partitions | Many partitions |
| BIOS boot | UEFI boot |
| Limited redundancy | Improved partition metadata resilience |

---

# Secure Boot

Secure Boot is a UEFI security feature.

Purpose:

```text
Power On

↓

UEFI

↓

Verify Boot Components

↓

Trusted Bootloader?

↓

Yes → Continue

No → Block Boot
```

Benefits:

- Prevents unauthorized bootloaders
- Helps mitigate bootkits
- Strengthens operating system startup security

---

# TPM (Trusted Platform Module)

TPM is a hardware security component.

Uses include:

- BitLocker key protection
- Secure Boot integration
- Device identity
- Credential protection
- Windows Hello support

Enterprise systems commonly enable TPM 2.0 by default.

---

# Installation Methods

Windows can be installed using multiple methods.

| Method | Typical Use Case |
|---------|------------------|
| USB Installation | Most common for desktops and laptops |
| DVD Installation | Legacy systems |
| Network (PXE) Boot | Enterprise deployments |
| Windows Deployment Services (WDS) | Centralized deployment |
| Microsoft Deployment Toolkit (MDT) | Automated imaging |
| Microsoft Configuration Manager | Large enterprise deployments |
| Cloud-based provisioning (e.g., Windows Autopilot) | Modern enterprise device onboarding |

---

# USB Installation

Most common approach.

Requirements:

- USB drive (typically 8 GB or larger)
- Windows installation media
- Supported computer

Advantages:

- Fast
- Portable
- Easy to update
- Widely supported

---

# ISO Image

An ISO file is a complete image of installation media.

Typical contents:

```text
Windows ISO

├── Boot Files
├── Setup Files
├── Recovery Environment
├── Drivers
└── Installation Images
```

ISO images are commonly used to:

- Create bootable USB drives
- Deploy virtual machines
- Archive installation media

---

# Bootable USB

A bootable USB contains:

- Bootloader
- Windows Setup files
- Installation environment

Benefits:

- Faster than DVD installation
- Convenient for field deployments
- Reusable after reimaging

---

# Enterprise Deployment Overview

Large organizations rarely install Windows manually on each device.

Typical deployment workflow:

```text
Golden Image

↓

Deployment Server

↓

Network Boot

↓

Automated Installation

↓

Domain Join

↓

Policies Applied

↓

Applications Installed

↓

Ready for Employee
```

Automation reduces deployment time and ensures consistent configurations.

---

# Cybersecurity Perspective

During installation, security decisions have long-term effects.

Recommendations:

- Enable Secure Boot.
- Enable TPM 2.0.
- Use GPT with UEFI.
- Install only trusted operating system images.
- Verify installation media integrity.
- Apply updates immediately after installation.
- Enable full-disk encryption where appropriate.

---

# Business Impact

A standardized installation process helps organizations:

- Reduce deployment time
- Improve endpoint security
- Simplify support
- Maintain compliance
- Ensure consistent configurations
- Lower operational costs

---

# Enterprise Best Practices

- Standardize on UEFI and GPT for new deployments.
- Maintain approved installation images.
- Verify firmware settings before deployment.
- Keep installation media up to date.
- Document deployment procedures.
- Test images before organization-wide rollout.
- Enable security features during installation rather than after deployment.

---

# Practical Labs

## Lab 1 — Check Firmware Mode

### Objective

Determine whether your system is using BIOS or UEFI.

Steps:

1. Press:

```text
Windows + R
```

2. Run:

```text
msinfo32
```

3. Locate:

```text
BIOS Mode
```

Record whether it displays:

- UEFI
- Legacy

---

## Lab 2 — Check Disk Partition Style

1. Open:

```text
Disk Management
```

2. Right-click the system disk.

3. Select:

```text
Properties

↓

Volumes
```

4. Record whether the partition style is:

- MBR
- GPT

---

# Key Takeaways

- UEFI and GPT are the modern standards for Windows installations.
- Secure Boot and TPM significantly improve startup security.
- USB media is the most common installation method.
- Enterprise environments rely on automated deployment tools rather than manual installations.
- Careful planning before installation reduces future operational issues.

---

# Interview Questions

1. What are the minimum hardware requirements for modern Windows installations?
2. Explain the difference between BIOS and UEFI.
3. Compare MBR and GPT.
4. What is Secure Boot?
5. What is TPM and why is it important?
6. Why is GPT recommended for modern systems?
7. What is an ISO image?
8. Why are USB installations preferred over DVDs?
9. Name three enterprise Windows deployment methods.
10. Why is installation standardization important in enterprises?

---

# References

- Microsoft Learn
- Windows Installation Documentation
- Windows Deployment Documentation
- Microsoft Security Documentation
- Windows Hardware Compatibility Documentation

---

# 02-Windows-Installation.md

# Part 2 — Creating Installation Media, Boot Process, Windows Setup, Disk Partitioning, and Installation Walkthrough

---

# Introduction

After understanding the hardware requirements and firmware concepts, the next step is preparing installation media and performing a Windows installation.

This section covers:

- Downloading Windows
- Creating bootable installation media
- Boot sequence
- Windows Setup
- Disk partitioning
- Installation options
- Enterprise deployment considerations

---

# Windows Installation Workflow

```text
Download Windows

↓

Create Bootable USB

↓

Configure BIOS/UEFI

↓

Boot from USB

↓

Windows Setup

↓

Partition Disk

↓

Install Windows

↓

First Boot (OOBE)

↓

User Configuration

↓

Desktop Ready
```

---

# Obtaining Windows Installation Media

Microsoft provides official installation media through:

- Windows ISO images
- Media Creation Tool (supported Windows editions)
- Volume Licensing Service Center (for eligible organizations)
- Visual Studio Subscriptions (where applicable)

Always use official Microsoft sources for installation media.

---

# Creating a Bootable USB

Requirements:

| Requirement | Description |
|------------|-------------|
| USB Drive | 8 GB or larger |
| Windows ISO | Official Microsoft image |
| Stable Internet | For downloading installation files |
| Administrative Access | Required for media creation |

---

# Media Creation Tool

The Media Creation Tool automates:

- Downloading Windows
- Verifying installation files
- Creating a bootable USB
- Preparing installation media

Benefits:

- Simple workflow
- Official files
- Automatic compatibility checks
- Supports the latest releases

---

# Alternative USB Creation Tools

Common tools include:

| Tool | Typical Use |
|------|-------------|
| Rufus | Advanced bootable USB creation |
| Ventoy | Multi-ISO boot USB |
| balenaEtcher | Cross-platform flashing |
| DiskPart (Windows) | Manual preparation (advanced) |

---

# Choosing the Correct Architecture

Modern Windows installations are generally:

```text
64-bit (x64)
```

Older systems may use:

```text
32-bit (x86)
```

Enterprise deployments should standardize on 64-bit unless a legacy application specifically requires otherwise.

---

# Configuring Boot Order

The system firmware determines which device boots first.

Example order:

```text
1. USB Drive

↓

2. Internal SSD

↓

3. Network (PXE)

↓

4. DVD
```

Temporary boot menus are often available through vendor-specific keys during startup.

---

# Windows Setup Environment

After booting from the installation media:

```text
Windows Setup

↓

Language Selection

↓

Keyboard Layout

↓

Install Now

↓

License Agreement

↓

Installation Type

↓

Disk Selection

↓

File Copy

↓

Restart

↓

Out-of-Box Experience (OOBE)
```

---

# Language Selection

Choose:

- Language
- Time and currency format
- Keyboard layout

These settings can typically be modified after installation if needed.

---

# Install Now

Selecting **Install Now** starts the installation process.

Setup performs:

- Hardware detection
- Storage detection
- Compatibility checks
- Preparation for installation

---

# Product Key

Windows Setup may prompt for:

```text
Product Key
```

Options include:

- Enter a valid key
- Skip (if digital entitlement or later activation is planned)

Enterprise environments often activate Windows automatically through centralized licensing.

---

# Windows Edition Selection

Choose the edition matching your license.

Example:

```text
Windows Home

Windows Pro

Windows Enterprise

Windows Education
```

Installing the incorrect edition may prevent successful activation.

---

# License Agreement

Read and accept the Microsoft Software License Terms before proceeding.

---

# Installation Types

Windows offers two primary installation types.

---

## Upgrade Installation

```text
Existing Windows

↓

Upgrade

↓

Applications Retained

↓

Personal Files Retained

↓

Settings Retained
```

Advantages:

- Faster migration
- Preserves applications
- Retains user data

Limitations:

- Existing issues may carry over
- Less suitable for major environment rebuilds

---

## Custom Installation (Clean Install)

```text
Empty Disk

↓

Partition Creation

↓

Fresh Windows Installation

↓

Clean System
```

Advantages:

- Better performance
- Removes previous configuration issues
- Preferred for enterprise imaging
- Cleaner environment

---

# Upgrade vs Clean Installation

| Upgrade | Clean Install |
|----------|---------------|
| Retains applications | Removes existing applications |
| Keeps user files | Starts fresh |
| Faster migration | Best long-term stability |
| Suitable for supported upgrades | Preferred for new deployments |

---

# Disk Selection

Windows displays available storage devices.

Example:

```text
Disk 0

↓

Partition 1

Partition 2

Unallocated Space
```

Select the appropriate destination for installation.

---

# Partition Concepts

A partition divides physical storage into logical sections.

Common partitions include:

```text
EFI System Partition

↓

Microsoft Reserved (MSR)

↓

Windows Partition (C:)

↓

Recovery Partition
```

Modern Windows installations automatically create required partitions on unallocated GPT disks.

---

# Typical GPT Layout

```text
Disk

├── EFI System Partition
├── Microsoft Reserved (MSR)
├── Windows (C:)
└── Recovery Partition
```

Each partition serves a specific purpose during boot, operation, and recovery.

---

# Formatting Partitions

During a clean installation, Setup allows formatting of existing partitions.

Formatting:

- Removes existing file system structures
- Deletes stored data
- Prepares the partition for a new installation

> **Warning:** Formatting permanently removes data from the selected partition.

---

# File Copy Phase

Windows Setup copies:

- Operating system files
- Boot files
- Drivers
- Recovery environment
- Default applications

Progress includes:

```text
Copy Files

↓

Install Features

↓

Install Updates (if applicable)

↓

Finalize Installation
```

---

# Automatic Restart

After installation files are copied:

```text
Windows Restarts

↓

Boots from Internal Drive

↓

Continues Installation
```

Avoid booting from the USB again unless reinstalling.

---

# Out-of-Box Experience (OOBE)

OOBE completes the initial configuration.

Typical tasks:

- Region selection
- Keyboard layout
- Network connection
- Microsoft account or local account setup
- Device naming (in some scenarios)
- Privacy preferences

---

# Creating User Accounts

Options may include:

- Microsoft account
- Local account (availability depends on edition and setup scenario)
- Organizational account (enterprise-managed devices)

Enterprise devices are commonly joined to organizational identity services after or during provisioning.

---

# Device Naming

Meaningful naming conventions improve management.

Example:

```text
HR-LAP-001

FIN-WS-015

ENG-DESKTOP-022
```

Benefits:

- Easier inventory
- Faster troubleshooting
- Simplified asset management

---

# Enterprise Deployment Considerations

Large organizations automate installation using:

```text
Reference Image

↓

Deployment Server

↓

Network Deployment

↓

Automated Configuration

↓

Domain or Cloud Join

↓

Policies Applied

↓

Applications Installed
```

Automation reduces manual effort and improves consistency.

---

# Cybersecurity Perspective

Installation decisions directly affect security.

Recommendations:

- Install from trusted media only.
- Delete unknown partitions before reimaging managed devices (after verifying backups).
- Use Secure Boot and TPM.
- Apply the latest updates immediately after installation.
- Enable BitLocker where organizational policy requires it.
- Avoid unnecessary administrator accounts.

---

# Business Impact

A standardized installation process provides:

- Faster onboarding
- Reduced configuration errors
- Improved compliance
- Consistent security posture
- Lower support costs
- Better asset management

---

# Enterprise Best Practices

- Maintain standardized installation images.
- Validate hardware compatibility before deployment.
- Use consistent partitioning schemes.
- Record device asset information during provisioning.
- Verify activation and update status after installation.
- Document deployment procedures and recovery steps.

---

# Practical Labs

## Lab 1 — Identify Existing Partitions

### Objective

Examine the partition structure of a Windows system.

Steps:

1. Open:

```text
Disk Management
```

2. Identify:

- EFI System Partition
- Recovery Partition
- Windows (C:)
- Any additional data partitions

3. Record the partition sizes and purposes.

---

## Lab 2 — Observe Windows Setup (Virtual Machine)

Create a virtual machine and boot from a Windows ISO.

During Setup, identify:

- Language selection
- Edition selection
- Installation type
- Partition selection
- OOBE screens

> Use a virtual machine to practice safely without affecting your primary computer.

---

# Key Takeaways

- Bootable USB media is the standard installation method for most systems.
- Clean installations provide the most consistent deployment experience.
- GPT-based installations automatically create required system partitions.
- OOBE completes device and user configuration after installation.
- Enterprise deployments rely heavily on automation and standardized images.

---

# Interview Questions

1. What is the purpose of the Media Creation Tool?
2. Compare upgrade and clean installations.
3. What partitions are typically created on a GPT Windows installation?
4. What happens during the Out-of-Box Experience (OOBE)?
5. Why should organizations standardize device names?
6. Why is a clean installation often preferred for enterprise deployments?
7. What precautions should be taken before formatting a partition?
8. Why is activation important after installation?
9. What are the benefits of automated Windows deployments?
10. Why should installation media come only from trusted sources?

---

# References

- Microsoft Learn
- Windows Setup Documentation
- Windows Deployment Documentation
- Microsoft Security Guidance
- Windows Hardware Compatibility Documentation

---


