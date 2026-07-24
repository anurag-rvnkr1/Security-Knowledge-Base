# 28-Windows-Cheat-Sheet.md

# Windows Administrator & Cybersecurity Cheat Sheet

---

# Introduction

This cheat sheet is a quick-reference guide for Windows administrators, SOC analysts, cybersecurity professionals, desktop support engineers, and students preparing for interviews or certifications.

It summarizes the most important Windows concepts, commands, tools, troubleshooting techniques, and security practices covered throughout this handbook.

---

# Windows Boot Process

```text
Power On

↓

BIOS / UEFI

↓

Windows Boot Manager

↓

Boot Configuration Data (BCD)

↓

Winload

↓

Windows Kernel

↓

Hardware Abstraction Layer (HAL)

↓

Boot Drivers

↓

Session Manager

↓

Service Control Manager (SCM)

↓

Winlogon

↓

Logon Screen

↓

User Desktop
```

---

# Windows Architecture

```text
+------------------------------------------------+
|                User Applications               |
+------------------------------------------------+
|               User Mode Services               |
+------------------------------------------------+
|              Windows Executive                 |
+------------------------------------------------+
|               Windows Kernel                   |
+------------------------------------------------+
|      Hardware Abstraction Layer (HAL)          |
+------------------------------------------------+
|                  Hardware                      |
+------------------------------------------------+
```

---

# Windows Directory Structure

| Directory | Purpose |
|-----------|---------|
| `C:\Windows` | Operating system files |
| `C:\Windows\System32` | Core system files |
| `C:\Windows\SysWOW64` | 32-bit components on 64-bit Windows |
| `C:\Program Files` | 64-bit applications |
| `C:\Program Files (x86)` | 32-bit applications |
| `C:\Users` | User profiles |
| `C:\ProgramData` | Shared application data |
| `C:\Temp` (varies) | Temporary files |

---

# NTFS Permissions

| Permission | Description |
|------------|-------------|
| Full Control | Complete access including permissions and ownership |
| Modify | Read, write, delete |
| Read & Execute | Open and execute files |
| Read | View files and folders |
| Write | Create or modify content |

---

# Windows Startup Modes

| Mode | Purpose |
|------|----------|
| Normal | Standard startup |
| Safe Mode | Minimal drivers and services |
| Safe Mode with Networking | Safe Mode plus networking |
| Safe Mode with Command Prompt | Command-line diagnostics |

---

# Essential Keyboard Shortcuts

| Shortcut | Function |
|----------|----------|
| `Ctrl + Shift + Esc` | Task Manager |
| `Ctrl + Alt + Delete` | Security options |
| `Win + R` | Run dialog |
| `Win + E` | File Explorer |
| `Win + L` | Lock computer |
| `Win + I` | Settings |
| `Win + X` | Power User menu |
| `Win + D` | Show desktop |
| `Alt + Tab` | Switch applications |
| `Win + Tab` | Task View |

---

# Common Administrative Tools

| Tool | Run Command |
|------|-------------|
| Event Viewer | `eventvwr.msc` |
| Task Manager | `taskmgr` |
| Device Manager | `devmgmt.msc` |
| Services | `services.msc` |
| Registry Editor | `regedit` |
| System Configuration | `msconfig` |
| System Information | `msinfo32` |
| Resource Monitor | `resmon` |
| Performance Monitor | `perfmon` |
| Computer Management | `compmgmt.msc` |
| Local Users and Groups* | `lusrmgr.msc` |
| Disk Management | `diskmgmt.msc` |
| Local Security Policy** | `secpol.msc` |
| Group Policy Editor** | `gpedit.msc` |

\* Not available on Windows Home editions.  
\** Availability depends on Windows edition.

---

# Frequently Used CMD Commands

| Command | Purpose |
|----------|----------|
| `dir` | List files and folders |
| `cd` | Change directory |
| `mkdir` | Create directory |
| `rmdir` | Remove directory |
| `copy` | Copy files |
| `move` | Move files |
| `del` | Delete files |
| `ren` | Rename files |
| `tree` | Display directory structure |
| `cls` | Clear screen |
| `help` | Display command help |
| `exit` | Exit Command Prompt |

---

# Networking Commands

| Command | Purpose |
|----------|----------|
| `ipconfig` | Display IP configuration |
| `ipconfig /all` | Detailed network information |
| `ipconfig /release` | Release DHCP lease |
| `ipconfig /renew` | Renew DHCP lease |
| `ipconfig /flushdns` | Clear DNS cache |
| `ping` | Test connectivity |
| `tracert` | Trace network route |
| `pathping` | Combined route and packet-loss analysis |
| `nslookup` | Query DNS |
| `netstat` | Display active connections |
| `arp -a` | Display ARP cache |
| `route print` | Display routing table |

---

# System Repair Commands

| Command | Purpose |
|----------|----------|
| `sfc /scannow` | Repair protected system files |
| `DISM /Online /Cleanup-Image /RestoreHealth` | Repair Windows image |
| `chkdsk C: /f` | Repair file system errors |
| `chkdsk C: /r` | Locate bad sectors and recover readable data |

---

# PowerShell Essentials

| Command | Purpose |
|----------|----------|
| `Get-Process` | List processes |
| `Get-Service` | List services |
| `Get-EventLog`* | Read classic logs |
| `Get-WinEvent` | Read event logs |
| `Get-ComputerInfo` | System information |
| `Get-Help` | Help documentation |
| `Get-ChildItem` | List files and folders |
| `Get-Command` | List available commands |
| `Restart-Service` | Restart a service |

\* `Get-WinEvent` is generally preferred for newer event logs.

---

# Event Viewer Logs

| Log | Purpose |
|------|----------|
| Application | Application events |
| Security | Authentication and audit events |
| System | Operating system events |
| Setup | Installation events |
| Forwarded Events | Collected remote events |

---

# Common Windows Services

| Service | Purpose |
|----------|----------|
| Service Control Manager | Manages services |
| Windows Update | Updates Windows |
| Print Spooler | Printing |
| DHCP Client | DHCP configuration |
| DNS Client | DNS resolution |
| Windows Time | Time synchronization |
| Task Scheduler | Scheduled tasks |
| Windows Defender | Endpoint protection |

---

# Active Directory Components

| Component | Purpose |
|-----------|---------|
| Forest | Highest logical boundary |
| Tree | Collection of domains |
| Domain | Administrative boundary |
| Organizational Unit (OU) | Logical organization |
| Domain Controller | Authentication server |
| Security Group | Permission management |
| Group Policy | Centralized configuration |

---

# Group Policy Processing Order

```text
Local

↓

Site

↓

Domain

↓

Organizational Unit (OU)
```

Remember:

**LSDOU**

---

# Common File Systems

| File System | Typical Use |
|-------------|-------------|
| NTFS | Windows system drives |
| FAT32 | Legacy and removable devices |
| exFAT | Large removable storage |

---

# Registry Root Keys

| Hive | Description |
|------|-------------|
| HKLM | Local machine settings |
| HKCU | Current user settings |
| HKCR | File associations |
| HKU | User profiles |
| HKCC | Current hardware profile |

---

# Windows Security Features

| Feature | Purpose |
|----------|----------|
| Microsoft Defender | Endpoint protection |
| Windows Firewall | Network traffic filtering |
| BitLocker | Disk encryption |
| Secure Boot | Trusted startup |
| Credential Guard | Credential protection |
| Windows Hello | Modern authentication |
| UAC | Privilege elevation control |

---

# Troubleshooting Workflow

```text
Identify

↓

Gather Information

↓

Analyze

↓

Develop Hypothesis

↓

Test

↓

Implement

↓

Validate

↓

Document
```

---

# Performance Investigation Workflow

```text
Slow Computer

↓

Task Manager

↓

Resource Monitor

↓

Performance Monitor

↓

Event Viewer

↓

Identify Root Cause

↓

Fix

↓

Validate
```

---

# Blue Screen (BSOD) Checklist

- Record stop code.
- Review recent hardware or software changes.
- Examine Event Viewer.
- Check memory health.
- Verify drivers.
- Analyze crash dumps if available.
- Validate after remediation.

---

# Interview Quick Facts

| Question | Quick Answer |
|----------|--------------|
| Default file system | NTFS |
| AD authentication | Kerberos |
| Registry editor | `regedit` |
| Safe startup | Safe Mode |
| Repair Windows files | `sfc /scannow` |
| Repair Windows image | `DISM /Online /Cleanup-Image /RestoreHealth` |
| View applied GPOs | `gpresult /r` |
| Display IP | `ipconfig` |
| Advanced process tool | Process Explorer |
| Startup analysis | Autoruns |

---

# Security Best Practices

- Apply the principle of least privilege.
- Keep systems patched.
- Use strong authentication.
- Enable BitLocker where appropriate.
- Review logs regularly.
- Restrict administrative access.
- Maintain tested backups.
- Use centralized monitoring.
- Follow change management procedures.
- Document security incidents.

---

# Key Takeaways

- Keep this cheat sheet accessible during labs and revision.
- Use built-in tools before introducing third-party utilities.
- Follow structured troubleshooting rather than guessing.
- Practice PowerShell alongside graphical tools.
- Reinforce security in every administrative task.

---


