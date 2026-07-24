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

