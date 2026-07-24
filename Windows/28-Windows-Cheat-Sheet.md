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


# 28-Windows-Cheat-Sheet.md

# Part 2 — Advanced Commands, PowerShell, Active Directory, Networking, Troubleshooting, Sysinternals, Interview Revision, and Final Handbook Summary

---

# Advanced CMD Commands

| Command | Purpose | Example |
|----------|---------|---------|
| `whoami` | Display current user | `whoami` |
| `whoami /groups` | Display group memberships | `whoami /groups` |
| `whoami /priv` | Display privileges | `whoami /priv` |
| `hostname` | Show computer name | `hostname` |
| `systeminfo` | Display system information | `systeminfo` |
| `tasklist` | List running processes | `tasklist` |
| `taskkill` | Terminate a process | `taskkill /PID 1234 /F` |
| `shutdown` | Shut down or restart | `shutdown /r /t 0` |
| `driverquery` | List installed drivers | `driverquery` |
| `gpresult` | Display applied Group Policy | `gpresult /r` |
| `net user` | Manage user accounts | `net user username` |
| `net localgroup` | Manage local groups | `net localgroup Administrators` |
| `sc query` | Query Windows services | `sc query` |
| `schtasks` | Manage scheduled tasks | `schtasks /query` |

---

# Essential PowerShell Cmdlets

## Process Management

| Cmdlet | Purpose |
|---------|---------|
| `Get-Process` | List processes |
| `Stop-Process` | Stop a process |
| `Start-Process` | Start a process |

---

## Service Management

| Cmdlet | Purpose |
|---------|---------|
| `Get-Service` | List services |
| `Start-Service` | Start service |
| `Stop-Service` | Stop service |
| `Restart-Service` | Restart service |
| `Set-Service` | Configure startup type |

---

## File Management

| Cmdlet | Purpose |
|---------|---------|
| `Get-ChildItem` | List files |
| `Copy-Item` | Copy files |
| `Move-Item` | Move files |
| `Remove-Item` | Delete files |
| `New-Item` | Create files/folders |

---

## Event Logs

| Cmdlet | Purpose |
|---------|---------|
| `Get-WinEvent` | Read event logs |
| `Clear-EventLog`* | Clear classic logs |
| `Limit-EventLog`* | Configure classic logs |

\* Applies to classic event logs; verify applicability before use.

---

## System Information

| Cmdlet | Purpose |
|---------|---------|
| `Get-ComputerInfo` | System information |
| `Get-Date` | Current date and time |
| `Get-HotFix` | Installed updates |
| `Get-CimInstance` | Query WMI/CIM objects |

---

# Active Directory Quick Reference

| Task | Command/Tool |
|------|--------------|
| View applied GPOs | `gpresult /r` |
| Group Policy report | `gpresult /h report.html` |
| Group Policy editor | `gpedit.msc`* |
| Active Directory Users and Computers | `dsa.msc`** |
| Active Directory Sites and Services | `dssite.msc`** |
| Active Directory Domains and Trusts | `domain.msc`** |

\* Local Group Policy Editor (availability depends on edition).  
\** Typically available on Windows Server or systems with Remote Server Administration Tools (RSAT).

---

# Networking Quick Reference

## Connectivity

```cmd
ping hostname
```

---

## DNS

```cmd
nslookup example.com
```

---

## Route

```cmd
tracert example.com
```

---

## Network Configuration

```cmd
ipconfig /all
```

---

## Active Connections

```cmd
netstat -ano
```

---

## Routing Table

```cmd
route print
```

---

## ARP Cache

```cmd
arp -a
```

---

# Windows Recovery Commands

| Command | Purpose |
|----------|----------|
| `sfc /scannow` | Repair protected system files |
| `DISM /Online /Cleanup-Image /RestoreHealth` | Repair component store |
| `chkdsk C: /f` | Repair file system |
| `chkdsk C: /r` | Scan for bad sectors |

---

# Windows Troubleshooting Toolkit

| Tool | Primary Use |
|------|-------------|
| Task Manager | Resource usage |
| Event Viewer | Logs |
| Resource Monitor | Detailed resource analysis |
| Performance Monitor | Performance counters |
| Reliability Monitor | Stability timeline |
| Device Manager | Drivers |
| WinRE | Recovery |
| Safe Mode | Minimal troubleshooting |
| System Restore | Configuration rollback |

---

# Sysinternals Toolkit

| Tool | Primary Use |
|------|-------------|
| Process Explorer | Advanced process analysis |
| Process Monitor | Registry and file monitoring |
| Autoruns | Startup entries |
| TCPView | TCP/UDP connections |
| RAMMap | Memory analysis |
| Handle | Open file handles |
| PsExec | Remote process execution |
| PsList | Process information |

---

# Windows Ports to Remember

| Port | Protocol | Typical Service |
|------|----------|-----------------|
| 20/21 | TCP | FTP |
| 22 | TCP | SSH |
| 23 | TCP | Telnet |
| 25 | TCP | SMTP |
| 53 | TCP/UDP | DNS |
| 67/68 | UDP | DHCP |
| 80 | TCP | HTTP |
| 110 | TCP | POP3 |
| 123 | UDP | NTP |
| 135 | TCP | RPC |
| 137-139 | TCP/UDP | NetBIOS |
| 143 | TCP | IMAP |
| 389 | TCP/UDP | LDAP |
| 443 | TCP | HTTPS |
| 445 | TCP | SMB |
| 3389 | TCP | Remote Desktop (RDP) |

---

# Windows Logs

| Log | Common Use |
|------|------------|
| Application | Application issues |
| System | Operating system events |
| Security | Authentication and auditing |
| Setup | Installation events |
| GroupPolicy Operational | GPO troubleshooting |
| Windows Update | Update troubleshooting |

---

# Active Directory Troubleshooting

```text
Cannot Log In

↓

Check DNS

↓

Check Domain Controller

↓

Verify Time

↓

Verify Network

↓

Review Event Viewer

↓

Run gpresult

↓

Resolve
```

---

# Performance Troubleshooting

```text
Slow Computer

↓

Task Manager

↓

CPU

↓

Memory

↓

Disk

↓

Network

↓

Event Viewer

↓

Fix
```

---

# BSOD Investigation

```text
Record Stop Code

↓

Review Drivers

↓

Check Event Logs

↓

Analyze Crash Dump

↓

Test Memory

↓

Validate
```

---

# Security Investigation

```text
Alert

↓

Review Logs

↓

Verify User

↓

Review Processes

↓

Review Network

↓

Contain

↓

Recover

↓

Document
```

---

# Common Windows Interview Commands

| Task | Command |
|------|----------|
| Current user | `whoami` |
| Computer information | `systeminfo` |
| Running processes | `tasklist` |
| IP address | `ipconfig` |
| Test connectivity | `ping` |
| DNS lookup | `nslookup` |
| Routing | `tracert` |
| Active connections | `netstat` |
| Repair files | `sfc /scannow` |
| Repair image | `DISM /Online /Cleanup-Image /RestoreHealth` |

---

# 50 Rapid-Fire Revision Points

1. Windows uses NTFS by default.
2. UEFI replaces legacy BIOS on modern systems.
3. BCD stores boot configuration.
4. Winload loads the Windows kernel.
5. HAL abstracts hardware differences.
6. User Mode has restricted privileges.
7. Kernel Mode has full system access.
8. The Registry stores configuration settings.
9. HKLM stores machine-wide settings.
10. HKCU stores current user settings.
11. Active Directory provides centralized identity management.
12. Domain Controllers authenticate users.
13. Kerberos is the default AD authentication protocol.
14. DNS is required for Active Directory.
15. Group Policy centralizes configuration.
16. Group Policy processing follows LSDOU.
17. OU stands for Organizational Unit.
18. NTFS supports ACLs.
19. BitLocker provides full-disk encryption.
20. UAC reduces unauthorized privilege elevation.
21. Windows Defender provides endpoint protection.
22. Windows Firewall filters network traffic.
23. Event Viewer records system events.
24. Task Manager monitors running processes.
25. Resource Monitor provides detailed resource usage.
26. Performance Monitor collects performance counters.
27. Reliability Monitor tracks system stability.
28. Device Manager manages hardware.
29. WinRE provides recovery tools.
30. Safe Mode loads minimal drivers.
31. Startup Repair addresses some boot problems.
32. SFC repairs protected system files.
33. DISM repairs the Windows component store.
34. CHKDSK repairs logical file system issues.
35. PowerShell uses object-based output.
36. `Get-Process` lists running processes.
37. `Get-Service` lists Windows services.
38. Process Explorer extends Task Manager capabilities.
39. Process Monitor captures file and Registry activity.
40. Autoruns displays startup entries.
41. TCPView shows active network connections.
42. Root Cause Analysis prevents recurring issues.
43. Performance baselines simplify troubleshooting.
44. Least privilege reduces security risk.
45. Patch management improves security.
46. Backups should be tested regularly.
47. Documentation improves operational efficiency.
48. Automation reduces repetitive work.
49. Monitoring enables proactive maintenance.
50. Always validate changes after implementation.

---

# Final Revision Checklist

Before an interview, ensure you can confidently explain:

- Windows architecture
- Boot process
- NTFS permissions
- Registry structure
- Active Directory
- Group Policy
- DNS and networking basics
- PowerShell fundamentals
- Event Viewer usage
- Performance troubleshooting
- Windows services
- Driver troubleshooting
- Windows Update
- BitLocker
- Microsoft Defender
- Windows Firewall
- Sysinternals tools
- Disaster recovery concepts
- Root Cause Analysis
- Enterprise troubleshooting methodology
- Security best practices

---

# Final Handbook Summary

Throughout this Windows Handbook, you have covered:

- Windows fundamentals
- Installation and deployment
- Operating system architecture
- Boot process
- File systems
- File management
- Command Prompt
- PowerShell
- Users and groups
- NTFS permissions
- Processes and threads
- Services
- Registry
- Networking
- Storage management
- System monitoring
- Event logging
- Windows security
- Windows Firewall
- Remote management
- Automation
- System hardening
- Active Directory
- Group Policy
- Windows for cybersecurity
- Troubleshooting
- Interview preparation
- Rapid revision

This progression provides a comprehensive foundation for Windows administration, enterprise IT operations, and cybersecurity.

---

# Recommended Next Learning Path

After mastering Windows administration, consider expanding into:

1. Windows Server Administration
2. Microsoft Entra ID (Azure AD)
3. Microsoft Intune
4. Hyper-V Virtualization
5. Microsoft Defender for Endpoint
6. Microsoft Sentinel (SIEM)
7. PowerShell Advanced Scripting
8. Active Directory Security
9. Incident Response & Digital Forensics
10. Cloud Security (Azure)

---

# Final Best Practices

- Practice in a virtual lab before making production changes.
- Automate repetitive tasks using PowerShell.
- Follow the principle of least privilege.
- Keep systems patched and monitored.
- Test backups and recovery procedures regularly.
- Document configurations and troubleshooting steps.
- Use structured methodologies for incident response.
- Continue learning through hands-on experience and official documentation.

---

# Congratulations!

You have successfully completed the **Windows Handbook**.

You now have a structured reference covering Windows fundamentals, enterprise administration, security, troubleshooting, Active Directory, PowerShell, networking, interview preparation, and operational best practices suitable for study, revision, and day-to-day administration.

---

