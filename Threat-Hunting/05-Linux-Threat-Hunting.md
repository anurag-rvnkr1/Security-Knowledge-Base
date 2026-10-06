# Linux Threat Hunting

## Overview

Linux is widely used across:

- Enterprise servers
- Cloud infrastructure
- Web applications
- Databases
- Containers
- Kubernetes nodes
- DevOps environments
- Security infrastructure
- Network appliances

Because Linux systems frequently host critical services and infrastructure, they are attractive targets for attackers.

A Linux compromise may involve:

```text id="c9b3q1"
Initial Access
      ↓
Shell Access
      ↓
Execution
      ↓
Privilege Escalation
      ↓
Credential Access
      ↓
Discovery
      ↓
Persistence
      ↓
Lateral Movement
      ↓
Collection
      ↓
Command & Control
      ↓
Impact
```

Linux threat hunting focuses on identifying the evidence left behind by these behaviors.

---

# Why Linux Threat Hunting Matters

Linux systems are frequently assumed to be secure because they may have fewer traditional malware infections than desktop environments.

This assumption is dangerous.

Attackers can abuse:

- SSH
- sudo
- cron
- systemd
- shell interpreters
- cloud credentials
- exposed services
- web applications
- containers
- scheduled jobs
- legitimate administration tools

A compromised Linux server may also be used as:

```text id="h8f4b9"
Initial Foothold
      ↓
Persistence
      ↓
Credential Theft
      ↓
Internal Reconnaissance
      ↓
Lateral Movement
      ↓
Command & Control
```

---

# Linux Threat Hunting Architecture

A typical Linux hunting environment can be represented as:

```text id="j8v2u5"
                  Linux Hosts
                      │
        ┌─────────────┼─────────────┐
        ▼             ▼             ▼
      Logs          auditd        EDR
        │             │             │
        └─────────────┼─────────────┘
                      ▼
                Log Collection
                      │
                      ▼
               SIEM / Data Lake
                      │
              ┌───────┴───────┐
              ▼               ▼
           Detection        Hunting
              │               │
              └───────┬───────┘
                      ▼
                 Investigation
                      │
                      ▼
                Incident Response
```

---

# Linux Security Telemetry

Important telemetry sources include:

- `/var/log/auth.log`
- `/var/log/secure`
- `/var/log/syslog`
- `/var/log/messages`
- `journald`
- `auditd`
- SSH logs
- sudo logs
- shell history
- process telemetry
- EDR
- DNS
- firewall
- network connections
- application logs
- web server logs
- container logs

The exact files vary by distribution.

For example:

```text id="6w9xps"
Debian / Ubuntu

/var/log/auth.log
/var/log/syslog

RHEL / CentOS / Fedora

/var/log/secure
/var/log/messages
```

Modern systems may rely heavily on `systemd-journald`.

---

# Linux Logging Architecture

```text id="w0j4y7"
Application
     │
     ▼
System Service
     │
     ▼
journald / syslog
     │
     ├── Local Storage
     │
     └── Forwarding
             │
             ▼
            SIEM
```

Centralized collection is preferred for enterprise hunting because local logs can be deleted or modified after compromise.

---

# Journald

`systemd-journald` collects and manages system logs on systems using systemd.

Basic command:

```bash
journalctl
```

Useful examples:

```bash
journalctl -b
```

View logs from the current boot.

```bash
journalctl -u ssh
```

Review logs for a specific service.

```bash
journalctl --since "1 hour ago"
```

Review recent events.

```bash
journalctl -p warning
```

Review warning-level events.

The exact service name may vary by distribution, for example `ssh` or `sshd`.

---

# Authentication Logs

Authentication logs are among the most valuable Linux hunting sources.

They can reveal:

- Successful SSH authentication
- Failed authentication
- sudo activity
- Account changes
- Authentication methods
- Source IP addresses
- Usernames
- Session activity

Typical workflow:

```text id="6sj0xu"
Authentication Event
        ↓
User
        ↓
Source IP
        ↓
Destination Host
        ↓
Time
        ↓
Post-Authentication Activity
```

---

# SSH Threat Hunting

SSH is one of the most important Linux remote-access mechanisms.

It is also frequently targeted.

Threat hunters should investigate:

- Repeated failed logins
- Successful login after many failures
- New source IPs
- Unusual login times
- Root login
- New SSH keys
- Unexpected users
- Authentication from unusual countries or networks
- Rapid access across multiple servers

---

# SSH Authentication Flow

```text id="n2r6cn"
Remote Host
     │
     ▼
SSH
     │
     ▼
Authentication
     │
     ├── Password
     ├── Public Key
     └── Other configured mechanisms
     │
     ▼
Shell / Session
     │
     ▼
Command Execution
```

A successful SSH login should therefore be correlated with subsequent activity.

---

# SSH Brute Force Hunting

A simple pattern:

```text id="d6w7a2"
Many Failed Logins
        ↓
Same Source
        ↓
Many Attempts
        ↓
Potential Brute Force
```

But consider legitimate causes:

- Misconfigured automation
- Monitoring systems
- Expired credentials
- Backup jobs
- Internal scanning

Always investigate context.

---

# Password Spraying on Linux

Password spraying differs from traditional brute force.

Example:

```text id="u5u7r3"
Source IP
   │
   ├── user01 → failed
   ├── user02 → failed
   ├── user03 → failed
   ├── user04 → failed
   └── user05 → failed
```

Look for:

- Many accounts
- Similar timestamps
- Common source
- Low attempt count per account
- Subsequent successful authentication

---

# SSH Successful Login

A successful login is not automatically suspicious.

Investigate:

```text id="gl6g2w"
User
Source
Destination
Time
Authentication Method
```

Then correlate:

```text id="j8d3m7"
SSH Login
   ↓
sudo
   ↓
Process Creation
   ↓
Network Connection
   ↓
Persistence
```

This can expose post-compromise activity.

---

# Root Login Hunting

Direct root SSH access may be disabled in many environments, but where it is permitted it deserves appropriate monitoring.

Investigate:

```text id="8h5v7f"
Root Login
    +
Unexpected Source
    +
Unexpected Time
```

Do not automatically classify every root login as malicious because legitimate administrative environments may use controlled privileged access.

---

# SSH Key Persistence

Attackers may add unauthorized public keys to maintain access.

Common location:

```bash
~/.ssh/authorized_keys
```

Potential hunting approach:

```text id="m6j5m0"
Authorized Keys
      ↓
Recent Modification
      ↓
Unexpected User
      ↓
Unknown Key
      ↓
Persistence Investigation
```

Monitor changes to sensitive SSH configuration and authorized key files where feasible.

---

# SSH Configuration Hunting

Important configuration areas can include:

```text id="v2p3nq"
/etc/ssh/sshd_config
/etc/ssh/ssh_config
~/.ssh/
```

Potential investigation targets:

- Authentication settings
- Root login configuration
- Authorized keys
- New users
- Unexpected configuration changes

Configuration changes should be correlated with administrative change windows.

---

# Linux Process Hunting

Process telemetry is essential.

Useful commands include:

```bash
ps aux
```

```bash
ps -ef
```

```bash
top
```

```bash
htop
```

```bash
pgrep -a <process>
```

For threat hunting, process information should ideally be collected centrally rather than relying only on live manual inspection.

---

# Process Investigation

For a suspicious process, investigate:

```text id="0g1y2s"
PID
PPID
User
Executable
Arguments
Working Directory
Open Files
Network Connections
Start Time
Parent Process
Children
```

Conceptually:

```text id="1c0p9e"
Parent Process
       ↓
Child Process
       ↓
Command Line
       ↓
File Activity
       ↓
Network Activity
```

---

# Parent-Child Process Analysis

Example:

```text id="r3l5sn"
sshd
 └── bash
      └── sudo
           └── suspicious_binary
```

This does not automatically prove compromise.

But if:

```text id="jq9f0n"
Unexpected SSH
      ↓
bash
      ↓
sudo
      ↓
Unknown Binary
      ↓
External Connection
```

the complete chain becomes a stronger hunting lead.

---

# Shell Hunting

Common Linux shells include:

- Bash
- Zsh
- Sh
- Fish
- Dash

Attackers frequently use shells because they are already available.

Potential hunting signals include:

- Shell launched by unexpected processes
- Shell executed by service accounts
- Interactive shell on servers where interactive access is unusual
- Shell activity after suspicious web requests
- Shell spawned by application processes

---

# Web Shell Hunting

Web servers are frequent Linux attack targets.

A common attack path can look like:

```text id="7e0w8h"
Internet
   ↓
Web Application
   ↓
Exploitation
   ↓
Web Shell
   ↓
Shell
   ↓
Server
```

Potential evidence:

```text id="u2qf4x"
Web Access Log
      +
Unexpected Process
      +
Web Server User
      +
Shell Execution
```

A web server process launching a shell may deserve investigation depending on the application's architecture.

---

# Web Server Process Correlation

Example:

```text id="3m8o0y"
nginx/apache
      ↓
Application Runtime
      ↓
Unexpected Shell
      ↓
Command Execution
```

Potential data sources:

- Web server logs
- Application logs
- Process telemetry
- EDR
- Network telemetry
- File creation events

---

# Sudo Hunting

`sudo` allows authorized users to execute commands with elevated privileges.

It is extremely useful for administration and can also be abused.

Hunt for:

- Unexpected sudo usage
- Unusual users
- Rare commands
- Sudo from unusual source sessions
- Privilege escalation sequences

Conceptually:

```text id="7n5x6w"
User Session
    ↓
sudo
    ↓
Root Command
    ↓
Persistence / Discovery / Credential Access
```

---

# Sudo Investigation

Ask:

```text id="j3t9k6"
Who used sudo?

What command was executed?

When?

From which session?

Was the user authorized?

Was the command expected?

What happened afterward?
```

---

# Privilege Escalation Hunting

Linux privilege escalation may involve:

- Misconfigured sudo
- SUID binaries
- Writable privileged files
- Weak service permissions
- Kernel vulnerabilities
- Credential abuse
- Container escape
- Misconfigured scheduled tasks

Threat hunters should focus on observable behavior rather than simply scanning for every possible privilege escalation vulnerability.

---

# SUID Hunting

SUID programs execute with the privileges of their owner.

A common administrative discovery command is:

```bash
find / -perm -4000 -type f 2>/dev/null
```

For hunting, focus on:

- Newly introduced SUID binaries
- Unusual locations
- Unexpected ownership
- Recently modified binaries

Example:

```text id="x42l9j"
New SUID Binary
      ↓
Unexpected Path
      ↓
Unknown Owner
      ↓
Recent Modification
```

This may warrant investigation.

---

# File Permission Hunting

Linux permissions are fundamental to security.

Investigate:

- World-writable sensitive files
- Unexpected ownership
- Modified system binaries
- New executable files
- Suspicious files in temporary directories

Potential locations:

```text id="t2j6eg"
/tmp
/var/tmp
/dev/shm
/home
/opt
/usr/local/bin
```

Temporary directories can contain legitimate software and application artifacts, so context is required.

---

# Temporary Directory Hunting

Attackers may use temporary locations for staging or execution.

Potential hunting signal:

```text id="r3j4de"
New Executable
      +
Temporary Directory
      +
Unexpected User
      +
Network Connection
```

This combination is more meaningful than the directory alone.

---

# Linux Persistence

Common persistence mechanisms include:

```text id="br5l5e"
SSH Keys
Cron
Systemd
Init Scripts
Shell Profiles
SUID
Services
User Accounts
Application Configuration
```

---

# Cron Hunting

Cron schedules recurring tasks.

Common locations include:

```text id="o8i1tq"
/etc/crontab
/etc/cron.d/
/etc/cron.daily/
/etc/cron.hourly/
/var/spool/cron/
```

User crontabs can be inspected with:

```bash
crontab -l
```

Potential hunting signal:

```text id="z4h2z0"
New Cron Entry
      ↓
Unexpected User
      ↓
Suspicious Command
      ↓
External Network Connection
```

---

# Cron Persistence Example

Conceptually:

```text id="p0o6sn"
Compromise
   ↓
Modify Cron
   ↓
Wait
   ↓
Cron Executes
   ↓
Payload
```

Hunt for:

- Newly created jobs
- Jobs invoking unusual scripts
- Downloads
- Encoded commands
- Commands executed from writable directories

---

# Systemd Hunting

Modern Linux systems frequently use systemd.

Services can be examined with:

```bash
systemctl list-units
```

```bash
systemctl list-unit-files
```

Investigate:

```text id="q7b8m4"
New Service
     ↓
Unknown Unit
     ↓
Unexpected ExecStart
     ↓
Unexpected User
```

---

# Systemd Persistence

A conceptual attack chain:

```text id="7j3m5h"
Attacker
   ↓
Create Service
   ↓
Enable Service
   ↓
System Reboot
   ↓
Service Starts
   ↓
Persistence
```

Hunting should correlate:

- Service creation
- File modification
- Service activation
- User
- Process
- Network activity

---

# Shell Profile Persistence

Attackers may modify shell startup files.

Examples include:

```text id="x0q8cr"
~/.bashrc
~/.bash_profile
~/.profile
/etc/profile
```

Potential hunting signal:

```text id="6j5pmm"
Profile Modified
      ↓
Unexpected User
      ↓
Command Added
      ↓
External Connection
```

---

# Account Hunting

Monitor changes to:

- User accounts
- Groups
- Sudo configuration
- SSH keys
- Passwords
- Privileged memberships

Useful commands for authorized investigation include:

```bash
getent passwd
```

```bash
getent group
```

```bash
id <username>
```

Account changes should ideally be correlated with centralized identity and configuration-management records.

---

# Suspicious Account Creation

Potential hunting signals:

```text id="d6f8w1"
New User
   +
Unexpected Creator
   +
Privileged Group
   +
SSH Key
```

A newly created account is not inherently malicious.

Examples of legitimate creation:

- New employee
- Application deployment
- Service account
- Automation

---

# Linux Credential Hunting

Potential credential-related targets include:

- SSH keys
- Password files
- Application configuration
- Cloud credentials
- Environment variables
- Browser/application credentials
- Shell history
- Secrets files

Examples of sensitive locations can include:

```text id="m0h2b8"
/etc/shadow
~/.ssh/
/etc/ssh/
Application configuration
Cloud credential stores
```

Access to sensitive files should be investigated based on the user, process, permissions, and expected administrative behavior.

---

# `/etc/shadow` Monitoring

`/etc/shadow` contains password hash information on many Linux systems.

Direct access is normally restricted.

A suspicious process accessing it can be a hunting lead.

```text id="z3d9h5"
Process
   ↓
Sensitive File Access
   ↓
User Context
   ↓
Privilege
   ↓
Follow-up Activity
```

Do not treat legitimate privileged administration as automatically malicious.

---

# Environment Variable Hunting

Applications may expose secrets through environment variables.

Potential targets include:

```text id="f1e6u8"
API Keys
Tokens
Cloud Credentials
Database Credentials
Application Secrets
```

Threat hunters may investigate suspicious processes that access environments belonging to other processes.

---

# Bash History

Shell history can sometimes provide investigative clues.

Examples:

```text id="q2q4js"
~/.bash_history
```

Potential commands may reveal:

- Reconnaissance
- Configuration changes
- Download activity
- Privilege escalation attempts
- Persistence

However:

> Shell history is not a complete or reliable forensic record.

Attackers can disable, clear, or avoid shell history.

---

# Network Threat Hunting on Linux

Linux hosts frequently act as:

- Web servers
- DNS servers
- Databases
- Application servers
- Proxies
- Kubernetes nodes

Network hunting should correlate:

```text id="x9d8qu"
Process
   ↓
Socket
   ↓
Destination
   ↓
Port
   ↓
DNS
   ↓
Firewall
```

---

# Useful Network Commands

For authorized troubleshooting and investigation:

```bash
ss -tulpn
```

View listening sockets.

```bash
ss -tp
```

View TCP connections with process information where permitted.

```bash
ip addr
```

View network interfaces.

```bash
ip route
```

View routing information.

```bash
lsof -i
```

View network-related open files where available.

---

# Listening Port Hunting

Unexpected services may expose new attack surfaces.

Example:

```text id="9y0r5v"
New Listening Port
       ↓
Unknown Process
       ↓
Unexpected User
       ↓
External Exposure
```

Investigate:

- Process
- Binary
- Configuration
- User
- Parent process
- Service definition
- Firewall exposure

---

# Outbound Connection Hunting

A Linux endpoint making an unexpected external connection can be a hunting lead.

Consider:

```text id="9pl2h1"
Process
+
Destination
+
Port
+
Frequency
+
DNS
+
User
```

Periodic communication may indicate beaconing, but legitimate applications can also communicate periodically.

---

# DNS Hunting

Investigate:

- Rare domains
- High-frequency queries
- Long subdomains
- Unusual query patterns
- New destinations
- Unexpected DNS clients

Conceptually:

```text id="8v3x9y"
Linux Host
    ↓
DNS Query
    ↓
Rare Domain
    ↓
Periodic Requests
    ↓
External Connection
```

Additional evidence is required before concluding malicious C2.

---

# Linux Malware Hunting

Linux malware may exhibit:

- Unexpected processes
- Persistence
- Network connections
- Modified binaries
- New users
- Suspicious files
- Resource consumption
- Hidden processes
- Unusual services

A useful workflow:

```text id="4m0wzq"
Suspicious Process
      ↓
Binary Path
      ↓
Hash
      ↓
Parent
      ↓
User
      ↓
Network
      ↓
Persistence
      ↓
Timeline
```

---

# File Integrity Hunting

Important system files may be monitored for unexpected changes.

Examples:

```text id="u6q3se"
/etc/passwd
/etc/shadow
/etc/sudoers
/etc/ssh/
/etc/systemd/
/etc/crontab
```

File integrity monitoring can help detect unauthorized modifications.

---

# Rootkit Hunting

Rootkits attempt to hide malicious activity.

Potential indicators can include inconsistencies between:

```text id="f4z5z7"
Process Listing
      vs
Kernel / EDR Telemetry
```

or:

```text id="7f4n6r"
Network Connections
      vs
Process Visibility
```

Rootkit investigation is advanced and may require:

- EDR
- Kernel-level telemetry
- Offline analysis
- Memory forensics
- Trusted boot environments

A normal process listing should not be treated as proof that the system is clean.

---

# Linux Container Hunting

Modern Linux environments frequently run containers.

A suspicious container may be investigated through:

```text id="6c8h8d"
Container
   ↓
Image
   ↓
Process
   ↓
Network
   ↓
Filesystem
   ↓
Privileges
```

Potential hunting signals include:

- Unexpected privileged containers
- Unknown images
- Unexpected outbound connections
- Host filesystem access
- Suspicious processes
- Container creation outside normal deployment workflows

Container hunting will be covered more deeply in the repository's Containers and Kubernetes sections.

---

# Cloud Linux Hunting

Linux instances in cloud environments should be correlated with cloud telemetry.

```text id="5u8r1x"
Cloud Identity
      +
Instance
      +
SSH
      +
Process
      +
Network
```

Example:

```text id="h2m5v8"
New Cloud Instance
      ↓
SSH Login
      ↓
Privilege Escalation
      ↓
Credential Access
      ↓
Outbound Connection
```

Cloud audit logs can provide valuable context.

---

# Linux Attack Timeline

A possible compromise timeline:

```text id="6r7j1p"
10:14
SSH Authentication
      ↓
10:15
Shell Started
      ↓
10:17
System Discovery
      ↓
10:19
Privilege Escalation
      ↓
10:22
Credential Access
      ↓
10:25
Cron Modified
      ↓
10:28
Outbound Connection
      ↓
10:35
Lateral Movement
```

The timeline is more useful than isolated events.

---

# Linux Threat Hunting Methodology

```text id="q0p9kx"
1. Define Threat Scenario
          ↓
2. Create Hypothesis
          ↓
3. Identify Linux Telemetry
          ↓
4. Search Authentication
          ↓
5. Analyze Processes
          ↓
6. Analyze Persistence
          ↓
7. Analyze Network
          ↓
8. Correlate Events
          ↓
9. Build Timeline
          ↓
10. Validate Finding
          ↓
11. Map ATT&CK
          ↓
12. Create Detection
```

---

# Example Hunt — SSH Compromise

## Hypothesis

> An attacker may have obtained valid SSH credentials and established persistence on a Linux server.

## Telemetry

```text id="v5l6i7"
SSH Logs
Authentication
Process
Sudo
File Activity
Network
EDR
```

## Hunt

```text id="r2m6n4"
SSH Login
   ↓
Source IP
   ↓
User
   ↓
Shell
   ↓
sudo
   ↓
Persistence
   ↓
Network
```

## Investigate

Ask:

- Is the source expected?
- Is the user expected?
- Was the login during normal hours?
- Was a new SSH key added?
- Was sudo used?
- Were unusual processes started?
- Was outbound communication established?

---

# Example Hunt — Cron Persistence

## Hypothesis

> An attacker who compromised a Linux host may create a scheduled task to maintain persistence.

## Telemetry

- File integrity
- Auditd
- EDR
- Process execution
- Cron logs

## Investigation

```text id="s4c5n1"
Cron File Modified
       ↓
User
       ↓
Command
       ↓
Execution
       ↓
Network
```

---

# Example Hunt — Web Server Compromise

## Hypothesis

> An attacker may exploit a public-facing web application and execute commands through the web server process.

## Telemetry

```text id="7m6m9y"
Web Logs
Application Logs
Process Telemetry
File Activity
Network
EDR
```

## Hunt

```text id="3d0n5w"
Suspicious Web Request
       ↓
Application Error / Exploit
       ↓
Web Process
       ↓
Shell Spawned
       ↓
Command Execution
       ↓
Outbound Connection
```

---

# Example Hunt — Privilege Escalation

## Hypothesis

> A compromised user may attempt to obtain root privileges using an unexpected sudo action or privileged binary.

## Telemetry

```text id="p2x9j6"
Authentication
+
sudo
+
Process
+
File
+
Privilege Context
```

## Investigation

```text id="0s4w9x"
User
 ↓
sudo
 ↓
Root Process
 ↓
Persistence
 ↓
Network
```

---

# Auditd

`auditd` provides Linux auditing capabilities and can capture security-relevant events.

Depending on configuration, it can provide visibility into:

- Process execution
- File access
- Permission changes
- User activity
- Configuration changes
- System calls

Example:

```bash
ausearch -m EXECVE
```

where supported and configured.

Audit rules should be designed carefully because excessive auditing can create significant volume.

---

# Auditd Hunting

A useful conceptual model:

```text id="q4j6yu"
Audit Event
     ↓
User
     ↓
Process
     ↓
Executable
     ↓
Arguments
     ↓
File / Resource
```

This can provide valuable evidence for endpoint investigations.

---

# Linux EDR

EDR can provide telemetry beyond traditional system logs.

Possible capabilities include:

- Process trees
- File activity
- Network connections
- Persistence
- Detection logic
- Behavioral analytics
- Response actions

Conceptually:

```text id="u7x9x3"
EDR
 │
 ├── Process
 ├── File
 ├── Network
 ├── User
 └── Persistence
       │
       ▼
      SIEM
```

---

# Linux Threat Hunting With SIEM

A SIEM can normalize:

```text id="y5o8q7"
auth.log
syslog
journald
auditd
EDR
DNS
Firewall
Application Logs
```

into a common investigation layer.

```text id="7n6s3p"
Linux Telemetry
       ↓
Normalization
       ↓
Enrichment
       ↓
Correlation
       ↓
Hunting
```

---

# Generic Linux Hunting Query

Conceptually:

```text id="1k7x3j"
SELECT
    user,
    source_ip,
    host,
    timestamp,
    event_type
FROM authentication_events
WHERE event_type IN (
    'failed_login',
    'successful_login'
)
ORDER BY timestamp DESC;
```

Actual syntax varies by SIEM.

---

# Generic SSH Hunting Query

Conceptually:

```text id="5z4v1n"
Find SSH authentication events
GROUP BY source_ip
AND username
OVER a defined time window
WHERE failures exceed baseline
OR
successful login follows repeated failures
```

---

# Generic Persistence Hunt

Conceptually:

```text id="7n3h4w"
Find modifications to:

cron
systemd services
authorized_keys
shell profiles

WHERE

user is unusual
OR
modification is outside change window
OR
referenced executable is unusual
```

---

# Detection Engineering

A successful Linux hunt can produce detection logic.

Example:

```text id="8j6n0m"
Behavior
   ↓
Evidence
   ↓
Stable Pattern
   ↓
Detection Rule
   ↓
Test
   ↓
Tune
   ↓
Deploy
```

Possible detection targets:

- Suspicious SSH behavior
- Unexpected privileged activity
- Persistence creation
- Web server spawning shell
- Unusual process execution
- Suspicious outbound connections

---

# Linux Telemetry Gaps

Common gaps include:

- No centralized authentication logs
- Missing auditd
- Limited process visibility
- No EDR
- Short log retention
- Unmonitored cloud instances
- Missing DNS telemetry
- Missing container telemetry
- Poor time synchronization
- Logs stored only locally

A hunting result should distinguish:

```text id="5d0l4e"
No Evidence Found
```

from:

```text id="n7w2k6"
No Evidence Available
```

These are not equivalent.

---

# Linux Threat Hunting Checklist

## Authentication

```text id="q6v7n2"
[ ] SSH failures
[ ] SSH successes
[ ] Source IP
[ ] User
[ ] Root login
[ ] Authentication method
[ ] Login timing
```

## Processes

```text id="j4p9s0"
[ ] Process
[ ] Parent
[ ] Child
[ ] User
[ ] Arguments
[ ] Path
[ ] Start time
```

## Persistence

```text id="z7s5r1"
[ ] Cron
[ ] Systemd
[ ] SSH keys
[ ] Shell profiles
[ ] Services
[ ] SUID
[ ] Accounts
```

## Privilege

```text id="b8c4v2"
[ ] sudo
[ ] Root
[ ] SUID
[ ] Privileged groups
[ ] Permission changes
```

## Network

```text id="h1n5x7"
[ ] Listening ports
[ ] Outbound connections
[ ] DNS
[ ] Destination
[ ] Port
[ ] Process
```

## Files

```text id="m2q9w6"
[ ] New executables
[ ] Sensitive file access
[ ] System file changes
[ ] Temporary files
[ ] Configuration changes
```

---

# Practical Lab 1 — SSH Threat Hunt

## Scenario

A Linux production server may have experienced unauthorized SSH access.

### Available Data

```text
auth.log / secure
journald
EDR
Firewall Logs
```

### Hypothesis

> An attacker may have authenticated using valid credentials and subsequently established persistence.

### Investigation

```text id="g4f7m9"
SSH Authentication
      ↓
Source IP
      ↓
User
      ↓
Shell
      ↓
sudo
      ↓
SSH Keys
      ↓
Cron / Systemd
      ↓
Network
```

### Deliverable

Create:

- Authentication timeline
- Suspicious events
- ATT&CK mapping
- Evidence
- Conclusion
- Detection recommendation

---

# Practical Lab 2 — Web Shell Hunt

## Scenario

A Linux web server may have been compromised.

### Hypothesis

> An attacker may have exploited the web application and caused the web service to spawn a shell.

### Investigate

```text id="y3j5m8"
Web Logs
     ↓
Suspicious Request
     ↓
Web Process
     ↓
Shell
     ↓
Command
     ↓
Network
```

### Questions

1. What request triggered the suspicious behavior?
2. Which process executed?
3. Which user owned the process?
4. Was a shell spawned?
5. What commands followed?
6. Was there outbound communication?
7. Was persistence established?

---

# Practical Lab 3 — Linux Persistence Hunt

Search for:

```text id="k5m7q2"
Cron
Systemd
SSH Keys
Shell Profiles
SUID
Services
New Users
```

Build a timeline:

```text id="s2x6h9"
Initial Access
 ↓
Persistence Modification
 ↓
Execution
 ↓
Network
```

---

# Practical Lab 4 — Privilege Escalation Hunt

## Scenario

A low-privileged account may have obtained root privileges.

Investigate:

```text id="r8j1m4"
Login
 ↓
Process
 ↓
sudo
 ↓
SUID / Permission
 ↓
Root Process
 ↓
Persistence
```

Document the evidence chain.

---

# Practical Lab 5 — Full Linux Attack Timeline

Build a complete timeline:

```text id="z3n7p5"
Initial Access
      ↓
SSH
      ↓
Shell
      ↓
Discovery
      ↓
Privilege Escalation
      ↓
Credential Access
      ↓
Persistence
      ↓
Network
      ↓
Lateral Movement
```

For every event record:

```text
Timestamp
Host
User
Process
Command
Source
Destination
ATT&CK Technique
Analyst Interpretation
```

---

# Linux Hunt Report Template

```markdown id="z0r7x5"
# Linux Threat Hunt Report

## Hunt Name

## Analyst

## Date

## Threat Scenario

## Hunt Hypothesis

## MITRE ATT&CK Mapping

## Data Sources

## Telemetry Coverage

## Authentication Analysis

## Process Analysis

## Privilege Analysis

## Persistence Analysis

## Network Analysis

## File Analysis

## Investigation Timeline

## Findings

## Evidence

## False Positives

## Telemetry Gaps

## Conclusion

## Detection Opportunity

## Recommendations

## Lessons Learned

## References
```

---

# MITRE ATT&CK Mapping

Linux threat hunting commonly intersects with techniques involving:

```text id="p7w4q2"
Execution
├── Command and Scripting Interpreter
│   └── Unix Shell
│
├── Python / Other Interpreters
└── User Execution

Persistence
├── Cron
├── Systemd Services
├── SSH Authorized Keys
└── Shell Profiles

Privilege Escalation
├── Sudo
├── SUID / SGID-related abuse
└── Exploitation

Credential Access
├── Credentials from Files
├── SSH Keys
└── Password Stores

Discovery
├── System Information Discovery
├── Process Discovery
├── Account Discovery
├── File and Directory Discovery
└── Network Service Scanning

Lateral Movement
├── Remote Services
└── SSH

Command and Control
├── Application Layer Protocol
├── DNS
└── Encrypted Channels
```

Always verify the current ATT&CK technique and sub-technique mapping when creating a production detection.

---

# Common Linux Hunting Mistakes

## Assuming Linux Is Secure by Default

Security depends on:

- Configuration
- Patch status
- Identity controls
- Network exposure
- Monitoring
- Application security

---

## Treating SSH Failures as Automatically Malicious

Automated systems and legitimate users can generate many failures.

Look for patterns.

---

## Treating Shell Usage as Malicious

Shells are fundamental administration tools.

Context matters.

---

## Ignoring Legitimate Automation

Cron, systemd, service accounts, and scripts are heavily used in production.

---

## Searching Only Local Logs

An attacker with sufficient privileges may alter local evidence.

Centralized telemetry is more resilient.

---

## Ignoring Cloud and Containers

Modern Linux environments often exist inside cloud and container infrastructure.

Host-level hunting alone may be insufficient.

---

# Best Practices

- Centralize Linux security logs.
- Collect authentication telemetry.
- Monitor SSH.
- Monitor privileged activity.
- Collect process telemetry.
- Deploy auditd where appropriate.
- Use EDR where supported.
- Monitor persistence mechanisms.
- Track system configuration changes.
- Monitor sensitive file access.
- Monitor unexpected network connections.
- Establish baselines for administrative activity.
- Monitor cloud and container context.
- Maintain sufficient retention.
- Synchronize system clocks.
- Protect centralized logs from tampering.
- Correlate multiple telemetry sources.
- Map hunts to ATT&CK.
- Convert validated findings into detections.

---

# Linux Threat Hunting Maturity

```text id="q8m2s5"
Level 1
Manual Log Review
       ↓
Level 2
Centralized Authentication Logging
       ↓
Level 3
Auditd + Process Telemetry
       ↓
Level 4
EDR + Behavioral Hunting
       ↓
Level 5
ATT&CK-Mapped Detection Engineering
       ↓
Level 6
Cloud / Container-Aware Hunting
```

---

# Interview Questions

## Beginner

### What is Linux threat hunting?

It is the proactive analysis of Linux telemetry to identify suspicious or malicious activity that may not have triggered existing detections.

---

### Where are Linux authentication logs stored?

This depends on the distribution and logging configuration. Common locations include:

```text
/var/log/auth.log
/var/log/secure
```

Modern systems may also use `journald`.

---

### What is journald?

`systemd-journald` is a system service that collects and manages logs on systems using systemd.

---

### What is auditd?

`auditd` provides Linux auditing capabilities and can record security-relevant activity according to configured audit rules.

---

### Why is SSH important for threat hunting?

SSH is a common remote administration mechanism and can be abused for unauthorized access, credential attacks, persistence, and lateral movement.

---

## Intermediate

### How would you investigate a suspicious SSH login?

I would examine:

```text id="p6r4x9"
Source IP
User
Authentication Method
Time
Destination Host
Session Activity
sudo
Processes
Persistence
Network Connections
```

Then correlate the activity into a timeline.

---

### How would you hunt Linux persistence?

I would investigate:

```text id="c2v7j8"
Cron
Systemd
SSH Authorized Keys
Shell Profiles
Services
SUID
Accounts
```

and correlate modifications with the responsible user and process.

---

### How would you investigate a suspicious Linux process?

I would examine:

```text id="f4n6z1"
PID
PPID
User
Executable
Arguments
Parent
Children
Files
Network
Start Time
Persistence
```

---

### Why is centralized logging important?

Because an attacker with sufficient privileges may alter or delete local logs. Centralized collection provides a more resilient source of evidence.

---

## Advanced

### How would you hunt a compromised Linux web server?

```text id="v6j3s8"
Web Request
    ↓
Application
    ↓
Process
    ↓
Shell
    ↓
Command
    ↓
File
    ↓
Network
    ↓
Persistence
```

I would correlate web logs, application logs, process telemetry, filesystem activity, network connections, and authentication events.

---

### How would you distinguish legitimate cron activity from malicious persistence?

Consider:

- Who created it?
- When was it created?
- What command executes?
- Where is the referenced binary?
- Is it part of a known deployment?
- Does the command access external infrastructure?
- Is the account expected to manage scheduled tasks?

---

### How would you investigate possible Linux credential theft?

I would look for unusual access to sensitive credential locations and correlate:

```text id="z9t2c4"
Process
+
User
+
Privilege
+
Sensitive File
+
Command Line
+
Network
```

---

### What is the difference between "no malicious activity" and "no evidence"?

```text id="y5r8p3"
No Malicious Activity
=
Evidence was available and the hypothesis
was investigated without finding malicious behavior.

No Evidence
=
Required telemetry was missing or insufficient.
```

This distinction is critical in professional threat hunting.

---

# Professional Linux Threat Hunting Workflow

```text id="q3c7n8"
                  Threat Intelligence
                         │
                         ▼
                   Hunt Hypothesis
                         │
                         ▼
                    Linux Host
                         │
          ┌──────────────┼──────────────┐
          ▼              ▼              ▼
       Auth Logs       auditd          EDR
          │              │              │
          └──────────────┼──────────────┘
                         ▼
                 SIEM / Data Lake
                         │
                         ▼
                    Hunt Query
                         │
                         ▼
                    Correlation
                         │
                         ▼
                     Timeline
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
           Benign                Suspicious
                                    │
                                    ▼
                               Investigation
                                    │
                           ┌────────┴────────┐
                           ▼                 ▼
                      Incident           Detection
                      Response           Engineering
```

---

# Chapter Summary

Linux threat hunting requires understanding the relationship between:

```text id="v2x8m4"
Identity
+
Authentication
+
Processes
+
Files
+
Permissions
+
Persistence
+
Network
+
Timeline
```

The most important principle is:

> **A Linux threat hunt should investigate behavior in context rather than treating individual commands, processes, or log events as automatically malicious.**

A suspicious SSH login becomes more meaningful when followed by:

```text id="4m6q9w"
SSH Login
   ↓
Shell
   ↓
sudo
   ↓
Discovery
   ↓
Persistence
   ↓
External Connection
```

Likewise:

```text id="b1r5x7"
Web Request
   ↓
Web Process
   ↓
Shell
   ↓
Command Execution
   ↓
Network Connection
```

can provide evidence of a possible web-server compromise.

The strongest Linux hunting capability combines:

```text id="s6h2k8"
Linux Logs
    +
auditd
    +
EDR
    +
Authentication
    +
Network Telemetry
    +
Cloud Context
    +
ATT&CK
```

into a unified investigation.

---

# Key Takeaways

```text id="m8q1v6"
01. Linux is a critical enterprise and cloud hunting environment.

02. Authentication telemetry is foundational for Linux investigations.

03. SSH activity should be correlated with post-login behavior.

04. Process trees provide important execution context.

05. sudo and privilege changes require contextual investigation.

06. Cron and systemd are important persistence surfaces.

07. SSH authorized keys can provide persistence opportunities.

08. Sensitive file access should be correlated with process and user context.

09. Web-server process behavior can reveal application compromise.

10. auditd can provide valuable security telemetry when appropriately configured.

11. Centralized logging protects investigations against local evidence tampering.

12. Cloud and container context is increasingly important for Linux hunting.

13. A timeline is more useful than isolated events.

14. Telemetry gaps must be distinguished from clean results.

15. Validated hunting findings should feed detection engineering.
```

---

# References

## Linux

- Linux Documentation — https://www.kernel.org/doc/
- systemd Documentation — https://www.freedesktop.org/wiki/Software/systemd/
- `journalctl` Manual — https://www.freedesktop.org/software/systemd/man/latest/journalctl.html
- OpenSSH — https://www.openssh.com/
- Linux Audit — https://linux-audit.com/

## Security

- MITRE ATT&CK — https://attack.mitre.org/
- CISA — https://www.cisa.gov/
- NIST Cybersecurity Framework — https://www.nist.gov/cyberframework

## Detection and Monitoring

- Wazuh — https://documentation.wazuh.com/
- Elastic Security — https://www.elastic.co/security
- Microsoft Defender for Endpoint — https://learn.microsoft.com/defender-endpoint/

---
