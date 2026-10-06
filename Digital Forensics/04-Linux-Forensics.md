# Linux Forensics

> **A practical enterprise guide to investigating Linux systems through authentication logs, systemd journals, shell history, SSH activity, user accounts, sudo, processes, networking, file-system metadata, cron, services, persistence, and forensic timelines.**

---

# Overview

Linux systems are widely used in:

- Enterprise servers
- Web applications
- Databases
- Cloud infrastructure
- Containers
- Kubernetes
- Network appliances
- Security infrastructure
- DevOps environments

A compromised Linux host can contain evidence across:

```text id="1s9t1m"
Files
Logs
Processes
Memory
Users
SSH
Sudo
Cron
systemd
Network
Shell History
File-System Metadata
Applications
Containers
```

Linux forensics therefore requires both **host-level investigation** and **environmental context**.

---

# Why Linux Forensics Matters

Attackers may use Linux systems for:

- Initial access
- Web application compromise
- Command execution
- Credential access
- Persistence
- Privilege escalation
- Lateral movement
- Data staging
- Command and control
- Cryptomining
- Data exfiltration

A forensic investigation should reconstruct:

```text id="8xv0r1"
Initial Access
      │
      ▼
Execution
      │
      ▼
Privilege Escalation
      │
      ▼
Persistence
      │
      ▼
Discovery
      │
      ▼
Network Activity
      │
      ▼
Data Access
```

---

# Linux Forensic Architecture

```text id="h5m5e7"
                    Linux Host
                       │
       ┌───────────────┼────────────────┐
       ▼               ▼                ▼
      Users           Files            Logs
       │               │                │
       ▼               ▼                ▼
      SSH             /etc           journald
      sudo            /home          auth logs
      shell           /var           app logs
       │               │                │
       └───────────────┼────────────────┘
                       ▼
                    Processes
                       │
                       ▼
                    Network
                       │
                       ▼
                    Timeline
```

---

# Linux Investigation Questions

A typical investigation should answer:

```text id="7c7o2d"
Who accessed the system?
When?
From where?
How did they authenticate?
What commands were executed?
Which processes ran?
Which files changed?
Was persistence established?
Which systems were contacted?
Was privilege escalated?
Was data accessed?
```

---

# Major Linux Evidence Sources

| Evidence Source | Investigation Value |
|---|---|
| `/var/log/auth.log` | Authentication |
| `/var/log/secure` | Authentication on some distributions |
| `journalctl` | systemd logs |
| Bash history | Shell commands |
| SSH logs | Remote access |
| `/etc/passwd` | Account inventory |
| `/etc/shadow` | Account credential metadata |
| `/etc/sudoers` | Privilege configuration |
| Cron | Scheduled execution |
| systemd | Services |
| Process state | Running activity |
| Network sockets | Connections |
| File metadata | File activity |
| `/tmp` | Temporary activity |
| `/var/tmp` | Temporary activity |
| `/dev/shm` | Temporary in-memory filesystem |
| Web logs | Application activity |
| Shell configuration | Persistence |
| SSH keys | Authentication/persistence |

---

# Linux Distribution Differences

Linux forensics varies across distributions.

For example:

```text id="8ozh1g"
Debian / Ubuntu
      │
      └── /var/log/auth.log

RHEL / CentOS / Fedora
      │
      └── /var/log/secure
```

Modern distributions may rely heavily on:

```text
systemd
   │
   ▼
journald
```

Always identify:

- Distribution
- Version
- Logging configuration
- Init system
- Installed software

before interpreting artifacts.

---

# Identify the Linux System

Useful commands:

```bash id="l4q4k5"
hostname
uname -a
cat /etc/os-release
```

For kernel information:

```bash id="p1x6xw"
uname -r
```

---

# System Identity

Record:

```text id="b3d6iq"
Hostname
IP Address
OS
Kernel
Architecture
Uptime
Cloud Instance ID
Asset ID
```

This creates the initial forensic context.

---

# Uptime

```bash id="a9p8tr"
uptime
```

Uptime helps determine:

- Whether a system recently rebooted
- Whether volatile evidence may still exist
- Whether timestamps need contextual interpretation

---

# User Accounts

Linux account information may be found in:

```text id="w7x4q9"
/etc/passwd
/etc/shadow
/etc/group
```

---

# `/etc/passwd`

The file can provide:

- Username
- UID
- GID
- Home directory
- Login shell

Example:

```bash id="m7u3u4"
cat /etc/passwd
```

---

# Account Investigation

Look for:

- Unexpected users
- Recently created accounts
- UID anomalies
- Unexpected shells
- Unusual home directories
- Service accounts with interactive shells

Do not assume every unfamiliar account is malicious.

Some may be legitimate service accounts.

---

# `/etc/shadow`

The shadow database contains password-related information.

Access should be handled carefully because it is highly sensitive.

Investigators may examine:

- Account state
- Password-aging metadata
- Credential configuration

Avoid unnecessarily exposing password hashes in reports.

---

# Group Membership

Review:

```bash id="8y7h6q"
cat /etc/group
```

Look for unexpected membership in privileged groups.

Examples may include:

- `sudo`
- `wheel`
- Administrative groups

---

# Sudo Configuration

Investigate:

```bash id="5l9r6y"
sudo -l
```

and authorized configuration files where appropriate.

Review:

```text id="2v1l0n"
/etc/sudoers
/etc/sudoers.d/
```

Questions:

- Who can execute privileged commands?
- Were permissions recently changed?
- Are there unexpected entries?

---

# Authentication Logs

Authentication evidence is central to Linux investigations.

Common sources:

```text id="m4g0ra"
/var/log/auth.log
/var/log/secure
journald
SSH logs
```

---

# SSH Investigation

SSH is one of the most important Linux remote-access mechanisms.

Investigate:

```text id="4q6s1u"
Source IP
User
Authentication Method
Timestamp
Success / Failure
Session Duration
Commands
```

---

# SSH Logs

Example:

```bash id="n8m2j7"
grep -i "sshd" /var/log/auth.log
```

On systems using journald:

```bash id="8z0jcn"
journalctl -u ssh
```

The exact service name may differ by distribution.

---

# Successful SSH Authentication

Search for successful sessions:

```bash id="c0m8zv"
grep -i "accepted" /var/log/auth.log
```

Investigate:

```text id="l4j2j8"
User
Source IP
Authentication Method
Time
```

---

# Failed SSH Authentication

Search for:

```bash id="x8w5f3"
grep -i "failed" /var/log/auth.log
```

Repeated failures may indicate:

- Password guessing
- Brute force
- Misconfiguration
- Automated scanning
- Legitimate authentication problems

Context is required.

---

# SSH Keys

SSH key-based authentication can create persistent access.

Review authorized keys:

```bash id="v4w6p8"
cat ~/.ssh/authorized_keys
```

Forensic questions:

```text id="p7y3s8"
When was the key added?
Who added it?
Does the key belong to a legitimate user?
Was the account compromised?
Was the key used?
```

---

# SSH Configuration

Review:

```text id="x4v5r2"
/etc/ssh/sshd_config
/etc/ssh/sshd_config.d/
```

Potentially relevant settings include:

- Authentication methods
- Root login
- Password authentication
- Authorized key configuration
- Port configuration

Configuration changes should be correlated with logs.

---

# Shell History

Shell history can provide useful evidence.

Common locations include:

```text id="q2j6u1"
~/.bash_history
~/.zsh_history
```

Example:

```bash id="1l7w9x"
cat ~/.bash_history
```

---

# Shell History Limitations

Shell history is not a perfect command log.

It may be:

- Disabled
- Deleted
- Incomplete
- Truncated
- Different between shells
- Missing commands executed through other mechanisms

Therefore:

> Shell history should be treated as one evidence source, not absolute truth.

---

# Shell History Investigation

Look for:

- Downloads
- Administrative commands
- Credential-related activity
- Network tools
- File manipulation
- Persistence changes
- Privilege escalation attempts

Then correlate with:

```text id="y1j9k7"
Process
Logs
File Metadata
Network
User
```

---

# systemd and journald

Modern Linux systems frequently use systemd.

Logs can be accessed using:

```bash id="g3w2w4"
journalctl
```

---

# Query Recent Logs

```bash id="3l8k8x"
journalctl -n 100
```

---

# Query by Time

```bash id="2t0k4p"
journalctl --since "2026-10-06 09:00:00"
```

---

# Query a Service

```bash id="0v4t5s"
journalctl -u ssh
```

Service names differ across distributions.

---

# Kernel Logs

Investigate:

```bash id="f9p5sl"
journalctl -k
```

or:

```bash id="6h6d9b"
dmesg
```

Depending on permissions and system configuration.

---

# systemd Services

List services:

```bash id="3c9j2k"
systemctl list-units --type=service
```

Review enabled services:

```bash id="z5v0j9"
systemctl list-unit-files --type=service
```

Investigate suspicious services:

```text id="r8m6l4"
Name
Path
User
Start Mode
Creation
Modification
Execution
```

---

# Linux Persistence

Common persistence mechanisms include:

```text id="c3v6h8"
Cron
systemd
SSH Keys
Shell Profiles
Startup Scripts
Services
Web Applications
User Accounts
SUID/SGID
Kernel Modules
Containers
```

---

# Cron

Cron provides legitimate scheduled task functionality.

Review:

```bash id="f5m3t7"
crontab -l
```

System-level schedules may exist in:

```text id="5d4x0q"
/etc/crontab
/etc/cron.d/
/etc/cron.daily/
/etc/cron.hourly/
/etc/cron.weekly/
/etc/cron.monthly/
```

---

# Cron Investigation

For suspicious entries determine:

```text id="n2k6y1"
Who owns it?
What executes?
When does it run?
Where is the script?
When was it created?
Was the change authorized?
```

---

# Shell Profile Persistence

Review files such as:

```text id="g1p4x8"
~/.bashrc
~/.profile
~/.bash_profile
/etc/profile
/etc/profile.d/
```

Investigate unexpected commands or scripts.

---

# Process Investigation

Running processes provide important volatile evidence.

```bash id="r4c9z0"
ps aux
```

or:

```bash id="p2g8x1"
ps -ef
```

---

# Process Investigation Questions

```text id="o1u3n6"
What is running?
Who owns it?
Where is the executable?
Who started it?
When did it start?
What files does it access?
What network connections exist?
```

---

# Process Tree

Use tools such as:

```bash id="u0d6h8"
pstree
```

Conceptually:

```text id="k8f0v5"
sshd
  │
  └── bash
       │
       └── suspicious process
             │
             └── network connection
```

Parent-child relationships provide useful behavioral context.

---

# Process Executable Paths

Linux exposes process information through `/proc`.

Example:

```bash id="7m2w5g"
readlink /proc/<PID>/exe
```

Command-line information:

```bash id="w7s8f4"
cat /proc/<PID>/cmdline
```

Use only on authorized systems.

---

# Open Files

A process may have open files.

```bash id="1h5j9v"
lsof -p <PID>
```

This can help correlate:

```text id="0g1v3z"
Process
   │
   ├── Files
   ├── Libraries
   ├── Sockets
   └── Pipes
```

---

# Network Investigation

Linux network state can provide important evidence.

```bash id="6f3v2x"
ss -tulpn
```

For established connections:

```bash id="d4w7x0"
ss -tp
```

---

# Network Questions

Determine:

```text id="8x5l1z"
Which process owns the connection?
Which user owns the process?
What destination is contacted?
What port is used?
When did the connection begin?
Is DNS involved?
```

---

# Network Interfaces

```bash id="7c4m9b"
ip addr
```

Routes:

```bash id="3y8n0k"
ip route
```

These help establish the system's network context.

---

# DNS Investigation

Depending on the environment, DNS evidence may exist in:

- Resolver logs
- systemd-resolved
- DNS server logs
- Network monitoring
- EDR
- PCAP

DNS should be correlated with process and network activity.

---

# File-System Investigation

Important directories include:

```text id="f6g4s2"
/etc
/home
/root
/tmp
/var/tmp
/dev/shm
/var/log
/var/www
/opt
/usr/local
```

Their relevance depends on the system's role.

---

# Temporary Directories

Investigate:

```text id="2w0h7k"
/tmp
/var/tmp
/dev/shm
```

Attackers may use temporary locations for:

- Staging
- Downloaded tools
- Scripts
- Temporary payloads

But legitimate applications also use these directories.

---

# File Metadata

Useful commands include:

```bash id="v6y9z1"
stat suspicious-file
```

Review:

- Size
- Permissions
- Ownership
- Modification time
- Access time
- Change time

---

# Linux Timestamps

Linux commonly provides:

```text id="w7m5l2"
atime — Access
mtime — Modification
ctime — Metadata/status change
```

`ctime` does not mean "creation time" in the usual Linux file-system interpretation.

---

# Find Recently Modified Files

Example:

```bash id="x3j4p8"
find /var/www -type f -mtime -1
```

This can be useful for application investigations.

Use targeted paths to avoid excessive noise.

---

# File Hashing

```bash id="k6x4v1"
sha256sum suspicious-file
```

Record hashes for relevant evidence.

---

# File Ownership

Investigate:

```bash id="r8c7p5"
ls -la suspicious-file
```

Questions:

```text id="z1s8h4"
Who owns it?
What permissions exist?
Is it executable?
When was it modified?
```

---

# Linux Permissions

Review:

```text id="b8m4t0"
-rwxr-xr-x
```

Understand:

```text id="u4r3y1"
Owner
Group
Others
Read
Write
Execute
```

---

# SUID and SGID

SUID/SGID binaries can be legitimate but require careful review during privilege-escalation investigations.

Search examples:

```bash id="3c6j9r"
find / -perm -4000 -type f 2>/dev/null
```

and:

```bash id="5q0h2n"
find / -perm -2000 -type f 2>/dev/null
```

Investigate unusual binaries rather than assuming every SUID file is malicious.

---

# Linux Capabilities

Capabilities provide fine-grained privileges.

Investigate with:

```bash id="x4p6d9"
getcap -r / 2>/dev/null
```

Unexpected capabilities may be relevant during privilege-escalation investigations.

---

# Root Investigation

Root-level activity deserves particular attention.

Review:

- Authentication
- sudo
- Process activity
- File changes
- Persistence
- Network activity
- Privileged commands

---

# Sudo Logs

Depending on distribution and configuration, sudo activity may appear in authentication logs or journald.

Example:

```bash id="h5q7k2"
grep -i "sudo" /var/log/auth.log
```

---

# Privilege Escalation Investigation

A useful model:

```text id="e8p0z2"
User
 │
 ▼
Initial Access
 │
 ▼
Command Execution
 │
 ▼
Privilege Escalation
 │
 ▼
Root
 │
 ▼
Persistence
```

Investigate evidence at every stage.

---

# Web Server Forensics

Linux systems frequently host:

- Apache
- Nginx
- Application servers
- APIs

Application logs may provide:

```text id="m8w4x3"
Request
IP
User Agent
URI
Status
Timestamp
```

---

# Web Application Compromise

Correlate:

```text id="z7c6a4"
Web Request
   │
   ▼
Application Process
   │
   ▼
File Creation
   │
   ▼
Shell / Command
   │
   ▼
Outbound Connection
```

This is especially useful during web-shell investigations.

---

# Web Shell Investigation

Look for suspicious files in application directories.

Example:

```bash id="q9m4s2"
find /var/www -type f -mtime -3
```

Then investigate:

- File metadata
- File contents
- Web logs
- Process execution
- Network activity

---

# SSH Persistence

Potential mechanisms include:

```text id="x4l8v6"
Authorized Keys
SSH Configuration
New Accounts
Shell Profiles
Services
```

Investigate modifications carefully.

---

# Linux Malware Investigation

Potential evidence sources:

```text id="s3q9h5"
Process
File
Memory
Network
Persistence
Logs
```

Malware analysis is covered in greater depth in Chapter 09.

---

# Linux File-System Timeline

Example:

```text id="j4r6n8"
09:01
SSH Authentication

09:03
Shell Started

09:04
Suspicious File Created

09:05
File Executed

09:06
Cron Entry Modified

09:08
Outbound Connection

09:12
Security Alert
```

---

# Timeline Correlation

Correlate:

```text id="c5x9w1"
Authentication
      +
Process
      +
File
      +
Persistence
      +
Network
```

The combined sequence can reveal the attack path.

---

# Linux Forensic Workflow

```text id="p7v4y0"
Identify Host
    │
    ▼
Identify Users
    │
    ▼
Preserve Volatile Evidence
    │
    ▼
Review Authentication
    │
    ▼
Review Processes
    │
    ▼
Review Network
    │
    ▼
Review Files
    │
    ▼
Review Persistence
    │
    ▼
Review Applications
    │
    ▼
Build Timeline
    │
    ▼
Correlate
    │
    ▼
Report
```

---

# Common Linux Forensic Misconfigurations

## Short Log Retention

Historical authentication evidence disappears.

## No Centralized Logging

Evidence remains only on the compromised host.

## Weak Time Synchronization

Timeline reconstruction becomes unreliable.

## No Audit Framework

Important system activity may be unavailable.

## Inconsistent SSH Logging

Remote access investigations become difficult.

## Shell History Not Preserved

Command-level context may be lost.

---

# Linux Audit Framework

Linux Audit (`auditd`) can provide detailed security-relevant telemetry when properly configured.

Example:

```bash id="m7k8r5"
systemctl status auditd
```

Audit logs are commonly stored under:

```text id="7v9d2f"
/var/log/audit/
```

---

# Audit Investigation

Depending on configuration, audit telemetry may help answer:

- Which user executed an action?
- Which process performed it?
- Which file was accessed?
- When did the event occur?

Audit configuration determines the available evidence.

---

# Journald Retention

Investigators should understand whether journald logs are:

- Persistent
- Volatile
- Rotated
- Forwarded
- Restricted

A forensic investigation should not assume historical journal data exists indefinitely.

---

# Linux Evidence Collection Checklist

```text id="f5k8m3"
[ ] Hostname recorded
[ ] OS recorded
[ ] Kernel recorded
[ ] IP configuration recorded
[ ] Time source checked
[ ] Logged-in users identified
[ ] Authentication logs preserved
[ ] SSH evidence preserved
[ ] Shell history preserved
[ ] Processes recorded
[ ] Network connections recorded
[ ] File-system evidence collected
[ ] Cron reviewed
[ ] systemd reviewed
[ ] SSH keys reviewed
[ ] Sudo reviewed
[ ] SUID/SGID reviewed
[ ] Capabilities reviewed
[ ] Web/application logs reviewed
[ ] Temporary directories reviewed
[ ] Evidence hashed
[ ] Timeline constructed
```

---

# Practical Lab 01 — Linux Authentication Investigation

## Scenario

A Linux server shows suspicious SSH activity.

Investigate:

```bash id="q5m3r1"
grep -i "sshd" /var/log/auth.log
```

or:

```bash id="y4c8p2"
journalctl -u ssh
```

Determine:

- Source IPs
- Usernames
- Successful authentications
- Failed authentications
- Authentication methods
- Timeline

---

# Practical Lab 02 — SSH Persistence Investigation

Inspect:

```text id="x8f2k0"
~/.ssh/authorized_keys
/etc/ssh/
/etc/ssh/sshd_config
```

Determine:

```text id="t1n7m6"
Which keys exist?
Which users have them?
When were files modified?
Are unexpected keys present?
```

Correlate with authentication logs.

---

# Practical Lab 03 — Process Investigation

Run:

```bash id="s5j7q9"
ps aux
```

and:

```bash id="b2r4v8"
pstree
```

Identify:

- Suspicious processes
- Parent processes
- User
- Executable path

Then inspect:

```bash id="a4w5p7"
readlink /proc/<PID>/exe
```

---

# Practical Lab 04 — Network Investigation

Run:

```bash id="n9x2q3"
ss -tp
```

Determine:

```text id="4h8r5w"
Process
User
Destination
Port
Connection State
```

Then compare the network destination with:

- DNS
- Firewall
- Proxy
- EDR
- Threat intelligence

---

# Practical Lab 05 — Persistence Investigation

Review:

```text id="6z1m3c"
/etc/crontab
/etc/cron.d/
/etc/systemd/system/
/etc/systemd/user/
~/.bashrc
~/.profile
~/.ssh/authorized_keys
```

Identify unexpected entries.

Document:

```text id="7c3s8y"
Persistence Type
Path
Owner
Timestamp
Execution
Network
Expected / Unexpected
Confidence
```

---

# Practical Lab 06 — Web Server Investigation

Scenario:

> An Nginx server may have been compromised.

Review:

```text id="1p6h9d"
Web Access Logs
Web Error Logs
Application Logs
Processes
Recently Modified Files
Network Connections
Persistence
```

Construct:

```text id="s2m8k4"
Request
  ↓
Application
  ↓
File
  ↓
Process
  ↓
Network
```

---

# Practical Lab 07 — Complete Linux Compromise Investigation

Scenario:

```text id="5q6w8z"
Suspicious SSH Login
        │
        ▼
Shell Activity
        │
        ▼
Suspicious File
        │
        ▼
Privilege Escalation
        │
        ▼
Persistence
        │
        ▼
Outbound Connection
```

Your investigation should determine:

1. Initial access
2. User
3. Commands
4. Process
5. Privilege escalation
6. Persistence
7. Network activity
8. Scope
9. Evidence gaps

---

# Linux Investigation Report Template

```text id="c3j9s6"
# Linux Forensic Investigation

## Case Information

Case ID:
Hostname:
IP:
Operating System:
Kernel:
Investigator:

## Scope

## Evidence Sources

## Acquisition

## Authentication Analysis

## SSH Analysis

## User Analysis

## Process Analysis

## Network Analysis

## File-System Analysis

## Persistence Analysis

## Application Analysis

## Timeline

## Findings

## Evidence Correlation

## Evidence Gaps

## Confidence

## Conclusions

## Recommendations
```

---

# Example Finding

```text id="e8k3m4"
Finding ID:
LIN-001

Title:
Suspicious SSH Access

Observation:
An interactive SSH session for USER01 originated from an unfamiliar external address.

Evidence:
SSH authentication logs
Shell history
Process telemetry
Network telemetry

Timeline:
09:01 — Successful SSH authentication
09:02 — Interactive shell
09:04 — Suspicious process execution
09:06 — Outbound network connection

Assessment:
The activity is consistent with possible unauthorized access.

Confidence:
High

Limitations:
Historical network telemetry was incomplete.
```

---

# Linux Forensic Decision Tree

```text id="k7p1r0"
              Suspicious Host
                    │
                    ▼
              Is it running?
               │          │
              Yes         No
               │           │
               ▼           ▼
       Preserve volatile   Disk
          evidence       acquisition
               │           │
               └─────┬─────┘
                     ▼
              Authentication
                     │
                     ▼
                 Processes
                     │
                     ▼
                  Network
                     │
                     ▼
                    Files
                     │
                     ▼
                Persistence
                     │
                     ▼
                  Timeline
                     │
                     ▼
                 Correlation
```

---

# Interview Questions

## 1. What Linux artifacts are important during forensic investigation?

Common sources include:

- Authentication logs
- journald
- Bash history
- SSH configuration
- Authorized keys
- User accounts
- Sudo
- Cron
- systemd
- Processes
- Network connections
- File metadata
- Application logs
- Audit logs

---

## 2. Where are SSH authentication events commonly found?

Depending on distribution:

```text id="4j6s8k"
/var/log/auth.log
/var/log/secure
journald
```

---

## 3. Does Bash history prove all commands executed by a user?

No.

History can be incomplete, disabled, deleted, or bypassed.

---

## 4. How would you investigate suspicious SSH activity?

Review:

```text id="p6x2c9"
Authentication
Source IP
User
Authentication Method
Session
Commands
Processes
Network
Timeline
```

---

## 5. What is journald?

The systemd journal is a centralized logging mechanism used by many modern Linux systems.

---

## 6. What is auditd?

The Linux Audit framework can provide detailed security-relevant event telemetry depending on its configuration.

---

## 7. How do you investigate Linux persistence?

Review:

```text id="7w5c9m"
Cron
systemd
SSH Keys
Shell Profiles
Services
Startup Scripts
User Accounts
SUID/SGID
Capabilities
Applications
```

---

## 8. What is the difference between `mtime` and `ctime`?

`mtime` represents modification time.

`ctime` represents inode metadata/status change time.

It should not be interpreted as ordinary file creation time.

---

## 9. Why is `/proc` useful during forensics?

It exposes information about running processes and kernel/system state.

---

## 10. What does `ss` help investigators understand?

It can show network sockets and connections, helping correlate network activity with processes.

---

## 11. What is a Linux SUID binary?

A binary configured to execute with the permissions of its owner, commonly root. SUID is legitimate functionality but can be relevant to privilege-escalation investigations.

---

## 12. Does an unfamiliar cron job prove compromise?

No.

Determine:

- Owner
- Purpose
- Creation/modification
- Script
- Execution
- Network behavior
- Expected business function

---

## 13. What evidence would you collect from a compromised web server?

At minimum:

```text id="m8q0v7"
Web Logs
Application Logs
Processes
Files
Network
Authentication
Persistence
Memory if appropriate
```

---

## 14. How do Linux and Windows forensics differ?

The artifacts and operating-system architecture differ.

Linux investigations commonly emphasize:

- journald
- auth logs
- SSH
- shell history
- systemd
- cron
- `/proc`
- Linux file systems

Windows investigations commonly emphasize:

- Event Logs
- Registry
- PowerShell
- Prefetch
- Amcache
- SRUM
- Windows-specific persistence

The underlying forensic principles remain similar.

---

# Scenario Interview Question

### Scenario

> You discover a new user account on a Linux server. What do you investigate?

```text id="p2k9v4"
Account
 │
 ├── UID
 ├── GID
 ├── Home Directory
 ├── Shell
 ├── Groups
 ├── SSH Keys
 ├── Creation Evidence
 ├── Authentication
 ├── Sudo
 └── Process Activity
```

Then determine whether the account is legitimate.

---

# Scenario Interview Question

### Scenario

> You find a suspicious binary in `/tmp`. What do you do?

A structured approach:

```text id="w4g7x8"
Preserve
   │
   ▼
Hash
   │
   ▼
Metadata
   │
   ▼
Owner / Permissions
   │
   ▼
Execution Evidence
   │
   ▼
Process
   │
   ▼
Network
   │
   ▼
Persistence
   │
   ▼
Related Hosts
```

Do not execute the suspicious file merely to determine what it does on a production system.

---

# Scenario Interview Question

### Scenario

> You find an SSH key that does not belong to the user.

Investigate:

1. File metadata
2. Key contents and fingerprint
3. User ownership
4. Authentication logs
5. Source addresses
6. Session activity
7. Related account changes
8. Persistence mechanisms

Then assess whether the key is unauthorized.

---

# Linux Forensic Maturity Model

## Level 1 — Basic

- Authentication logs
- Manual investigation

## Level 2 — Repeatable

- Standard collection
- journald
- SSH analysis
- File investigation

## Level 3 — Managed

- Centralized logging
- auditd
- EDR
- Formal procedures

## Level 4 — Integrated

- SIEM
- EDR
- Threat hunting
- Forensic collection

## Level 5 — Advanced

- Enterprise Linux telemetry
- Automated evidence preservation
- Cross-host correlation
- Cloud/container integration
- Continuous forensic readiness

---

# Chapter Completion Checklist

```text id="s4j8v2"
[ ] Understand Linux forensic architecture
[ ] Identify Linux distribution
[ ] Understand authentication logs
[ ] Understand SSH forensics
[ ] Understand shell history
[ ] Understand journald
[ ] Understand auditd
[ ] Understand Linux users
[ ] Understand sudo
[ ] Understand processes
[ ] Understand /proc
[ ] Understand network sockets
[ ] Understand file metadata
[ ] Understand Linux timestamps
[ ] Understand cron
[ ] Understand systemd
[ ] Understand SSH persistence
[ ] Understand SUID/SGID
[ ] Understand capabilities
[ ] Understand web-server forensics
[ ] Understand Linux timelines
[ ] Complete authentication lab
[ ] Complete persistence lab
[ ] Complete network lab
[ ] Complete full Linux investigation
```

---

# Key Takeaways

Linux forensics is fundamentally about correlating system state, user activity, authentication, files, processes, persistence, and network behavior.

A practical investigation model is:

```text id="x3v5n8"
Authentication
      │
      ▼
User
      │
      ▼
Process
      │
      ▼
File
      │
      ▼
Persistence
      │
      ▼
Network
      │
      ▼
Timeline
      │
      ▼
Finding
```

The investigator should remember:

- Shell history is not complete.
- Authentication logs depend on configuration.
- `ctime` is not ordinary creation time.
- Cron and systemd are legitimate administration mechanisms.
- SUID is not inherently malicious.
- SSH keys require context.
- `/proc` provides valuable volatile evidence.
- File timestamps require careful interpretation.
- Network connections should be correlated with owning processes.
- No single Linux artifact should normally be treated as conclusive proof.

> **Linux forensics is the disciplined reconstruction of system, user, process, file, authentication, persistence, and network activity from evidence distributed across the operating system.**

---

# References

### Linux Manual Pages

https://man7.org/linux/man-pages/

### systemd / journalctl

https://www.freedesktop.org/wiki/Software/systemd/

### Linux Audit

https://linux-audit.com/

### Red Hat Security

https://access.redhat.com/security/

### Ubuntu Security

https://ubuntu.com/security

### NIST SP 800-86

https://csrc.nist.gov/publications/detail/sp/800-86/final

### MITRE ATT&CK

https://attack.mitre.org/

### SANS Digital Forensics

https://www.sans.org/digital-forensics/

### The Sleuth Kit

https://www.sleuthkit.org/

---

> **Investigate the user, process, file, persistence, and network together. The timeline connects them.**
