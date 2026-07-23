# 24 - Linux Troubleshooting

# Part 1 — Linux Troubleshooting Fundamentals, Methodology, Boot Problems, and Recovery

---

# Introduction

Linux systems are designed to be reliable, but failures can still occur due to:

- Hardware issues
- Software bugs
- Misconfigurations
- Network failures
- Storage problems
- Resource exhaustion
- Human error
- Security incidents

A good Linux administrator or cybersecurity professional must be able to troubleshoot systems quickly, methodically, and with minimal business impact.

---

# Learning Objectives

By the end of this chapter, you will understand:

- Enterprise troubleshooting methodology
- Root cause analysis
- Boot troubleshooting
- System recovery
- Log-based troubleshooting
- Service diagnosis
- Enterprise troubleshooting workflows
- Best practices for incident resolution

---

# What is Troubleshooting?

Troubleshooting is the systematic process of identifying, isolating, diagnosing, and resolving problems affecting a Linux system.

The primary goals are to:

- Restore service
- Minimize downtime
- Preserve data
- Identify root cause
- Prevent recurrence

---

# Enterprise Troubleshooting Workflow

```text
Problem Report

↓

Collect Information

↓

Identify Symptoms

↓

Analyze

↓

Identify Root Cause

↓

Implement Fix

↓

Validate

↓

Document

↓

Prevent Future Issues
```

---

# Reactive vs Proactive Troubleshooting

| Reactive | Proactive |
|-----------|-----------|
| Respond after failure | Prevent future failures |
| Restore service | Reduce future incidents |
| Incident-driven | Monitoring-driven |
| Immediate resolution | Continuous improvement |

Enterprise IT teams combine both approaches.

---

# Troubleshooting Principles

Always:

- Understand the problem
- Gather evidence
- Avoid assumptions
- Make one change at a time
- Validate every change
- Document findings

---

# Root Cause Analysis (RCA)

Fixing symptoms is not enough.

Example:

```text
Server Down

↓

Restart Server

↓

Service Restored

↓

WHY did it fail?

↓

Root Cause

↓

Permanent Fix
```

Without RCA, the issue is likely to return.

---

# Information Gathering

Before making changes, collect:

- Error messages
- Log entries
- System uptime
- Resource utilization
- Recent configuration changes
- Software updates
- User reports
- Incident timeline

---

# Essential Diagnostic Commands

Hostname:

```bash
hostnamectl
```

Kernel:

```bash
uname -r
```

System uptime:

```bash
uptime
```

Current users:

```bash
who
```

Current date:

```bash
date
```

---

# System Health Overview

CPU:

```bash
top
```

Memory:

```bash
free -h
```

Storage:

```bash
df -h
```

Processes:

```bash
ps aux
```

These commands provide a quick snapshot of system health.

---

# Enterprise Incident Prioritization

| Priority | Example |
|----------|----------|
| Critical | Production outage |
| High | Major service unavailable |
| Medium | Partial degradation |
| Low | Minor configuration issue |

Prioritization helps allocate resources effectively.

---

# Troubleshooting Methodology

```text
Observe

↓

Collect Data

↓

Analyze

↓

Hypothesize

↓

Test

↓

Validate

↓

Document
```

---

# Boot Problems

Boot failures can occur because of:

- Corrupted bootloader
- Missing kernel
- Damaged initramfs
- Filesystem corruption
- Incorrect `/etc/fstab`
- Disk failures
- Kernel panic
- Misconfigured services

---

# Linux Boot Sequence

```text
BIOS / UEFI

↓

Bootloader

↓

Kernel

↓

initramfs

↓

systemd

↓

Services

↓

Login
```

Failures can occur at any stage.

---

# Boot Failure Categories

| Stage | Possible Issue |
|--------|----------------|
| Firmware | Hardware detection |
| Bootloader | Missing GRUB entries |
| Kernel | Kernel panic |
| initramfs | Missing drivers |
| systemd | Failed units |
| Login | Authentication problems |

---

# Viewing Previous Boot Logs

Current boot:

```bash
journalctl -b
```

Previous boot:

```bash
journalctl -b -1
```

These logs are often the first place to investigate startup issues.

---

# Failed Services During Boot

List failed units:

```bash
systemctl --failed
```

Inspect a specific service:

```bash
systemctl status service-name
```

---

# Kernel Messages

Display kernel ring buffer:

```bash
dmesg
```

Recent kernel messages can reveal:

- Driver issues
- Hardware errors
- Filesystem problems
- Memory issues

---

# Bootloader (GRUB)

GRUB is commonly used as the Linux bootloader.

Responsibilities:

- Load kernel
- Load initramfs
- Pass boot parameters
- Present boot menu

---

# Common GRUB Problems

Examples:

- Missing configuration
- Corrupted bootloader
- Incorrect kernel entry
- Damaged boot partition

Symptoms:

- Boot menu missing
- Rescue prompt
- System fails before kernel loads

---

# initramfs

The initial RAM filesystem (initramfs):

- Loads required drivers
- Mounts the root filesystem
- Prepares the system before handing control to `systemd`

If required drivers are missing, the system may fail to boot.

---

# Kernel Panic

A kernel panic occurs when the kernel encounters a fatal condition from which it cannot safely recover.

Possible causes:

- Faulty hardware
- Unsupported drivers
- Corrupted kernel
- Filesystem corruption
- Severe kernel bugs

Kernel panics require investigation rather than repeated reboots.

---

# Filesystem Issues During Boot

Common causes:

- Corrupted filesystem
- Incorrect UUID in `/etc/fstab`
- Missing storage device
- Disk failure

Symptoms may include:

- Emergency mode
- Read-only filesystem
- Mount failures

---

# Emergency Mode

Linux may enter emergency mode when critical filesystems cannot be mounted or essential services fail to start.

Typical workflow:

```text
Boot Failure

↓

Emergency Mode

↓

Review Logs

↓

Repair Configuration

↓

Reboot

↓

Validate
```

---

# Rescue Mode

Rescue mode provides a minimal environment for system recovery.

Typical tasks:

- Repair filesystems
- Correct configuration files
- Reset passwords
- Restore backups
- Disable problematic services

---

# Viewing Boot Time

Display startup timing:

```bash
systemd-analyze
```

Detailed service timing:

```bash
systemd-analyze blame
```

Useful for identifying slow boot services.

---

# Boot Performance Workflow

```text
Boot

↓

Measure

↓

Identify Slow Services

↓

Optimize

↓

Validate
```

---

# Enterprise Recovery Strategy

A typical recovery process:

```text
Failure

↓

Detection

↓

Diagnosis

↓

Recovery

↓

Validation

↓

Root Cause Analysis

↓

Documentation
```

---

# Documentation During Troubleshooting

Record:

- Symptoms
- Timeline
- Commands executed
- Configuration changes
- Root cause
- Resolution
- Preventive actions

Good documentation accelerates future troubleshooting efforts.

---

# Cybersecurity Perspective

Attackers may intentionally cause:

- Service failures
- Bootloader tampering
- Configuration corruption
- Resource exhaustion
- Log deletion

Troubleshooting should therefore consider both operational failures and potential security incidents.

---

# Business Impact

Effective troubleshooting helps organizations:

- Minimize downtime
- Protect critical services
- Reduce financial losses
- Improve customer satisfaction
- Strengthen operational resilience
- Accelerate incident recovery

---

# Enterprise Best Practices

- Follow a structured troubleshooting methodology.
- Preserve evidence before making changes.
- Review logs before restarting services.
- Validate every corrective action.
- Perform root cause analysis after restoration.
- Document incidents thoroughly.
- Test recovery procedures regularly.
- Maintain verified backups and recovery plans.

---

# Key Takeaways

- Troubleshooting is a structured, evidence-based process.
- Root cause analysis is essential to prevent recurring issues.
- Boot problems can occur at multiple stages of the startup process.
- Logs, system status, and diagnostics are critical for identifying failures.
- Documentation and validation are integral parts of enterprise troubleshooting.

---

# 24 - Linux Troubleshooting

# Part 2 — Service Troubleshooting, Process Troubleshooting, Performance Analysis, Network Troubleshooting, and DNS Troubleshooting

---

# Introduction

Most production Linux incidents involve one or more of the following:

- Failed services
- High CPU utilization
- Memory exhaustion
- Disk space shortages
- Network failures
- DNS issues
- Resource contention
- Configuration errors

A systematic troubleshooting approach minimizes downtime and helps identify the true root cause.

---

# Service Troubleshooting

Linux services provide essential functionality such as:

- SSH
- Web servers
- Databases
- DNS
- Email
- Monitoring agents

When a service fails, investigate before restarting it.

---

# Service Troubleshooting Workflow

```text
Service Failure

↓

Check Status

↓

Review Logs

↓

Identify Cause

↓

Apply Fix

↓

Restart Service

↓

Validate
```

---

# Check Service Status

Display service status:

```bash
systemctl status service-name
```

Example:

```bash
systemctl status ssh
```

Look for:

- Active state
- Exit codes
- Error messages
- Recent log entries

---

# Review Failed Services

```bash
systemctl --failed
```

This lists all units currently in a failed state.

---

# Restart a Service

```bash
sudo systemctl restart service-name
```

Restarting may restore service temporarily, but always investigate the underlying cause.

---

# Reload Configuration

Some services support configuration reloads without a full restart:

```bash
sudo systemctl reload service-name
```

Use reload when supported to minimize service disruption.

---

# View Service Logs

```bash
journalctl -u service-name
```

Recent entries:

```bash
journalctl -u service-name -n 50
```

Logs often provide the most direct explanation for service failures.

---

# Validate Configuration

Many services provide syntax validation commands.

Example (SSH):

```bash
sudo sshd -t
```

Always validate configuration files before restarting services after changes.

---

# Process Troubleshooting

Processes consume:

- CPU
- Memory
- Disk I/O
- Network resources

Unexpected process behavior can affect overall system performance.

---

# View Running Processes

```bash
ps aux
```

Display process tree:

```bash
ps -ef --forest
```

---

# Interactive Process Monitoring

```bash
top
```

or

```bash
htop
```

(if installed)

Monitor:

- CPU usage
- Memory usage
- Process state
- Load averages

---

# Process States

| State | Meaning |
|--------|---------|
| R | Running |
| S | Sleeping |
| D | Uninterruptible sleep (often I/O) |
| T | Stopped |
| Z | Zombie |

Persistent zombie or uninterruptible processes warrant investigation.

---

# Identify Resource-Intensive Processes

Sort by CPU:

```bash
ps aux --sort=-%cpu | head
```

Sort by memory:

```bash
ps aux --sort=-%mem | head
```

---

# Terminate a Process

Graceful termination:

```bash
kill PID
```

Force termination:

```bash
kill -9 PID
```

Prefer graceful termination whenever possible to avoid data loss or corruption.

---

# Performance Troubleshooting

Performance issues may be caused by:

- CPU saturation
- Memory pressure
- Disk bottlenecks
- Network latency
- Misconfigured applications
- Resource leaks

---

# Performance Analysis Workflow

```text
Identify Symptoms

↓

Measure Resources

↓

Locate Bottleneck

↓

Implement Fix

↓

Validate

↓

Monitor
```

---

# CPU Analysis

Current CPU load:

```bash
uptime
```

Interactive view:

```bash
top
```

Review:

- Load average
- CPU utilization
- High-CPU processes

---

# Memory Analysis

Display memory usage:

```bash
free -h
```

Review:

- Total memory
- Used memory
- Available memory
- Swap utilization

High swap usage may indicate memory pressure.

---

# Storage Analysis

Filesystem utilization:

```bash
df -h
```

Directory usage:

```bash
du -sh *
```

Look for:

- Nearly full filesystems
- Rapid storage growth
- Large log files

---

# Open Files

Display open files:

```bash
lsof
```

Useful for:

- Deleted-but-open files
- Port ownership
- File lock investigations

---

# Disk I/O Considerations

Symptoms of disk-related issues:

- Slow application response
- High I/O wait
- Delayed service startup
- Slow database operations

Correlate storage observations with application and system logs.

---

# Network Troubleshooting

Common network issues include:

- Connectivity failures
- Routing problems
- Firewall restrictions
- Interface failures
- MTU mismatches
- DNS failures

---

# Network Troubleshooting Workflow

```text
Verify Interface

↓

Check Address

↓

Check Route

↓

Test Connectivity

↓

Review Firewall

↓

Validate
```

---

# Review Network Interfaces

```bash
ip addr
```

Verify:

- Interface state
- IP address
- Expected configuration

---

# Review Routing Table

```bash
ip route
```

Look for:

- Default route
- Incorrect routes
- Missing gateways

---

# Connectivity Testing

Test basic connectivity:

```bash
ping hostname
```

or

```bash
ping IP_ADDRESS
```

A failed ping does not always indicate failure because ICMP may be intentionally blocked.

---

# Trace Network Path

```bash
traceroute hostname
```

or

```bash
tracepath hostname
```

(if available)

Useful for identifying routing issues.

---

# Display Listening Ports

```bash
ss -tulpn
```

Verify that expected services are listening on the correct interfaces and ports.

---

# DNS Troubleshooting

DNS problems often appear as application connectivity failures.

Typical symptoms:

- Hostnames cannot be resolved
- Slow connections
- Intermittent failures
- Service discovery issues

---

# DNS Resolution Workflow

```text
Application

↓

DNS Query

↓

Resolver

↓

DNS Server

↓

Response

↓

Connection
```

---

# Check DNS Configuration

View configured resolvers:

```bash
cat /etc/resolv.conf
```

Verify:

- Nameserver entries
- Search domains
- Resolver configuration

---

# Query DNS

Using `dig` (if installed):

```bash
dig example.com
```

Using `host`:

```bash
host example.com
```

Using `nslookup`:

```bash
nslookup example.com
```

Compare results if troubleshooting inconsistent resolution.

---

# Verify Hostname Resolution

Display hostname:

```bash
hostname
```

Verify local hostname mappings:

```bash
cat /etc/hosts
```

Ensure local overrides are intentional and up to date.

---

# Firewall Considerations

A correctly configured firewall may intentionally block traffic.

Before assuming a network failure:

- Verify firewall policy
- Confirm allowed ports
- Check recent rule changes

---

# Network Troubleshooting Checklist

| Check | Status |
|--------|--------|
| Interface up | ✓ |
| IP address assigned | ✓ |
| Default route present | ✓ |
| DNS configured | ✓ |
| Firewall reviewed | ✓ |
| Service listening | ✓ |
| Logs reviewed | ✓ |

---

# Enterprise Scenario 1

## Web Server Unreachable

Symptoms:

- Users cannot access HTTPS service.
- SSH access remains available.

Investigation:

1. Verify web service status.
2. Review service logs.
3. Confirm listening port.
4. Check firewall configuration.
5. Validate TLS configuration.
6. Test locally before external testing.

---

# Enterprise Scenario 2

## High CPU Usage

Symptoms:

- Slow application response.
- Elevated system load.

Investigation:

- Review running processes.
- Identify CPU-intensive workloads.
- Examine recent deployments.
- Correlate with application logs.
- Validate after corrective actions.

---

# Enterprise Scenario 3

## DNS Resolution Failure

Symptoms:

- Hostnames fail to resolve.
- IP-based connections succeed.

Investigation:

- Verify `/etc/resolv.conf`.
- Test configured DNS servers.
- Check local `/etc/hosts`.
- Review resolver service status.
- Confirm network connectivity.

---

# Cybersecurity Perspective

Performance degradation and service failures can also indicate security events such as:

- Denial-of-service attacks
- Unauthorized processes
- Resource abuse
- Cryptomining malware
- Configuration tampering

Always consider security as a potential contributing factor during investigations.

---

# Business Impact

Rapid troubleshooting of services and networks helps organizations:

- Reduce downtime
- Improve customer experience
- Maintain service-level agreements (SLAs)
- Minimize operational costs
- Improve incident response efficiency

---

# Enterprise Best Practices

- Review logs before restarting services.
- Validate configuration changes before deployment.
- Monitor CPU, memory, storage, and network resources continuously.
- Investigate recurring failures using root cause analysis.
- Document all troubleshooting steps and outcomes.
- Correlate system metrics with application logs.
- Test changes in staging when practical.
- Preserve evidence if a security incident is suspected.

---

# Key Takeaways

- Service troubleshooting begins with status checks and log analysis.
- Resource monitoring is essential for diagnosing performance issues.
- Network troubleshooting follows a structured, layered approach.
- DNS issues often present as application connectivity problems.
- Effective troubleshooting combines technical analysis, documentation, and validation.

---

# 24 - Linux Troubleshooting

# Part 3 — Storage Troubleshooting, Filesystem Recovery, Log Analysis, Security Incident Troubleshooting, Practical Labs, and Enterprise Case Studies

---

# Introduction

Storage failures and filesystem corruption can cause severe service disruptions.

Common symptoms include:

- Systems becoming read-only
- Applications failing to write data
- Boot failures
- Missing files
- Disk space exhaustion
- High disk latency

Administrators must diagnose these problems carefully to prevent data loss.

---

# Storage Troubleshooting Workflow

```text
Identify Symptoms

↓

Collect Information

↓

Verify Storage

↓

Review Filesystems

↓

Analyze Logs

↓

Repair

↓

Validate

↓

Document
```

---

# Storage Inventory

Display block devices:

```bash
lsblk
```

Display filesystem usage:

```bash
df -h
```

Display mounted filesystems:

```bash
mount
```

These commands provide an overview of the storage layout.

---

# Filesystem Utilization

Check available storage:

```bash
df -h
```

Example output:

```text
Filesystem      Size  Used Avail Use%

/dev/sda2        80G   72G    8G  90%
```

High utilization may affect application performance and updates.

---

# Directory Usage

Determine which directories consume space:

```bash
du -sh /*
```

Review large directories individually for more detail.

---

# Inode Exhaustion

A filesystem can run out of inodes even when free space remains.

Check inode usage:

```bash
df -i
```

High inode usage is common when many small files exist.

---

# Deleted but Open Files

A deleted file may continue consuming disk space while a process keeps it open.

Display open files:

```bash
lsof
```

Look for deleted files still referenced by running processes.

---

# Filesystem Integrity

Filesystem corruption may result from:

- Power loss
- Hardware failure
- Kernel issues
- Improper shutdowns

Symptoms include:

- Read-only mounts
- Mount failures
- Missing files
- Input/output errors

---

# Filesystem Recovery

General recovery workflow:

```text
Identify Problem

↓

Unmount Filesystem (if appropriate)

↓

Run Filesystem Check

↓

Review Results

↓

Mount

↓

Validate
```

Always ensure backups are available before performing repair operations.

---

# Review Filesystem UUIDs

```bash
blkid
```

Useful when troubleshooting:

- `/etc/fstab`
- Mount failures
- Incorrect UUID references

---

# Verify Mount Configuration

Display configuration:

```bash
cat /etc/fstab
```

Common issues:

- Incorrect UUID
- Incorrect filesystem type
- Invalid mount options
- Missing storage devices

---

# Read-Only Filesystem

Symptoms:

- Applications cannot write files
- Package updates fail
- Configuration changes cannot be saved

Investigate:

- Disk health
- Filesystem state
- Kernel logs
- Mount options

---

# Storage Performance

Storage bottlenecks may cause:

- Slow applications
- Delayed database queries
- Long boot times
- High I/O wait

Correlate observations with system metrics and logs.

---

# Log Analysis

Logs are one of the most valuable troubleshooting resources.

Common log categories:

- Authentication
- Kernel
- System services
- Applications
- Package management
- Security events

---

# System Journal

View recent entries:

```bash
journalctl
```

Current boot:

```bash
journalctl -b
```

Previous boot:

```bash
journalctl -b -1
```

---

# Follow Logs

View new log entries in real time:

```bash
journalctl -f
```

Useful during troubleshooting after applying configuration changes.

---

# Kernel Messages

Display kernel messages:

```bash
dmesg
```

Common items include:

- Driver initialization
- Hardware detection
- Filesystem errors
- Network initialization

---

# Search Logs

Example:

```bash
journalctl | grep error
```

or

```bash
grep "error" logfile
```

Searching logs helps isolate relevant events.

---

# Log Analysis Workflow

```text
Collect Logs

↓

Filter

↓

Correlate

↓

Identify Pattern

↓

Determine Root Cause

↓

Implement Fix
```

---

# Security Incident Troubleshooting

Not every outage is purely operational.

Consider security-related causes such as:

- Unauthorized access
- Malware
- Configuration tampering
- Credential misuse
- Resource abuse

---

# Security Investigation Workflow

```text
Detect

↓

Collect Evidence

↓

Analyze

↓

Contain (if required)

↓

Recover

↓

Lessons Learned
```

---

# Authentication Investigation

Review authentication events:

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

Look for:

- Repeated failures
- Unusual login times
- Unexpected accounts
- Privileged activity

---

# Service Investigation

Review service state:

```bash
systemctl status service-name
```

Review logs:

```bash
journalctl -u service-name
```

Correlate timestamps with reported issues.

---

# Configuration Drift

Unexpected configuration changes may explain recurring issues.

Review:

- Recent deployments
- Change management records
- Version-controlled configuration
- Audit logs

---

# Enterprise Troubleshooting Checklist

| Area | Verify |
|------|--------|
| CPU | Utilization within expected range |
| Memory | No excessive pressure or swapping |
| Storage | Sufficient free space and healthy filesystems |
| Network | Interfaces, routes, DNS, firewall |
| Services | Running and healthy |
| Logs | Reviewed for errors |
| Security | No signs of unauthorized activity |
| Documentation | Updated with findings |

---

# Practical Lab 1 — Storage Inventory

```bash
lsblk
```

```bash
df -h
```

Objectives:

- Identify storage devices
- Review filesystem utilization

---

# Practical Lab 2 — Directory Usage

```bash
du -sh /var/*
```

Objectives:

- Identify directories consuming the most space
- Investigate abnormal growth

---

# Practical Lab 3 — Open Files

```bash
lsof
```

Objectives:

- Review open files
- Identify deleted-but-open files

---

# Practical Lab 4 — Review Mount Configuration

```bash
cat /etc/fstab
```

Objectives:

- Verify filesystem configuration
- Compare UUIDs with `blkid`

---

# Practical Lab 5 — System Journal

```bash
journalctl -b
```

Objectives:

- Review boot messages
- Identify startup warnings or errors

---

# Practical Lab 6 — Kernel Messages

```bash
dmesg
```

Objectives:

- Review hardware initialization
- Identify storage or driver issues

---

# Practical Lab 7 — Service Logs

```bash
journalctl -u ssh
```

Replace `ssh` with another service as appropriate.

Objectives:

- Review service-specific events
- Correlate failures with system activity

---

# Practical Lab 8 — Authentication Logs

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

Objectives:

- Review authentication failures
- Identify suspicious patterns

---

# Enterprise Case Study 1

## Disk Full on Production Server

Symptoms:

- Application errors
- Failed package updates
- Logging failures

Investigation:

1. Check filesystem usage.
2. Identify large directories.
3. Review log growth.
4. Archive or remove unnecessary data.
5. Validate free space after remediation.

---

# Enterprise Case Study 2

## Service Failure After Configuration Change

Symptoms:

- Service does not start.
- Users report outage.

Investigation:

- Validate configuration syntax.
- Review service logs.
- Restore previous known-good configuration if required.
- Test before returning to production.

---

# Enterprise Case Study 3

## Unexpected Authentication Failures

Symptoms:

- Repeated failed logins
- User unable to authenticate

Investigation:

- Review authentication logs.
- Verify account status.
- Confirm password policy.
- Check recent identity or configuration changes.

---

# Enterprise Case Study 4

## Boot Delay

Symptoms:

- Slow startup after maintenance

Investigation:

- Review `systemd-analyze blame`.
- Identify slow services.
- Validate dependencies.
- Optimize startup configuration where appropriate.

---

# Cybersecurity Perspective

Troubleshooting and security investigations often overlap.

For example:

- High CPU usage may indicate resource abuse.
- Unexpected network traffic may indicate compromise.
- Service failures may result from unauthorized changes.
- Log anomalies may reveal malicious activity.

Maintain evidence integrity if a security incident is suspected.

---

# Business Impact

Effective troubleshooting of storage, logs, and security events helps organizations:

- Reduce downtime
- Protect critical data
- Improve operational resilience
- Meet compliance requirements
- Accelerate incident resolution

---

# Enterprise Best Practices

- Monitor storage utilization proactively.
- Review logs regularly, not only during incidents.
- Preserve evidence before making significant changes.
- Validate filesystem and configuration integrity.
- Correlate logs with monitoring data and change records.
- Document findings and root causes.
- Test recovery procedures periodically.
- Incorporate lessons learned into operational processes.

---

# Key Takeaways

- Storage and filesystem issues are common causes of Linux outages.
- Log analysis is central to effective troubleshooting.
- Security events should be considered during operational investigations.
- Practical diagnostics, documentation, and validation improve incident resolution.
- A structured approach reduces downtime and supports long-term system reliability.

---

# 24 - Linux Troubleshooting

# Part 4 — Advanced Practical Labs, Enterprise Scenarios, Chapter Summary, Interview Questions, Linux Troubleshooting Cheat Sheet, and References

---

# Introduction

Enterprise Linux troubleshooting requires more than technical knowledge.

Successful administrators and cybersecurity professionals must:

- Follow structured methodologies
- Minimize downtime
- Preserve evidence
- Perform root cause analysis
- Document findings
- Prevent recurrence

This final section combines practical exercises with real-world enterprise scenarios and interview preparation.

---

# Enterprise Troubleshooting Lifecycle

```text
Incident Report

↓

Initial Assessment

↓

Evidence Collection

↓

Diagnosis

↓

Root Cause Analysis

↓

Resolution

↓

Validation

↓

Documentation

↓

Preventive Actions
```

---

# Practical Lab 1 — Complete System Health Check

Review system information:

```bash
hostnamectl
```

```bash
uptime
```

```bash
free -h
```

```bash
df -h
```

```bash
ps aux
```

Objectives:

- Assess overall system health
- Record baseline metrics
- Identify obvious issues

---

# Practical Lab 2 — Investigate Failed Services

Display failed services:

```bash
systemctl --failed
```

Review a specific service:

```bash
systemctl status service-name
```

View logs:

```bash
journalctl -u service-name
```

Objectives:

- Identify failure causes
- Correlate service logs with system events

---

# Practical Lab 3 — Network Connectivity Validation

Review interfaces:

```bash
ip addr
```

Review routing:

```bash
ip route
```

Display listening ports:

```bash
ss -tulpn
```

Objectives:

- Verify network configuration
- Confirm required services are reachable

---

# Practical Lab 4 — DNS Investigation

View resolver configuration:

```bash
cat /etc/resolv.conf
```

Query DNS:

```bash
dig example.com
```

or

```bash
host example.com
```

Objectives:

- Validate DNS configuration
- Compare hostname resolution results

---

# Practical Lab 5 — Filesystem Investigation

Review mounted filesystems:

```bash
mount
```

Filesystem usage:

```bash
df -h
```

Directory usage:

```bash
du -sh /var/*
```

Objectives:

- Detect storage bottlenecks
- Identify abnormal disk consumption

---

# Practical Lab 6 — Log Correlation

Review current boot logs:

```bash
journalctl -b
```

Follow logs:

```bash
journalctl -f
```

Objectives:

- Correlate events with reported issues
- Identify recurring errors

---

# Practical Lab 7 — Authentication Investigation

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

Objectives:

- Review failed login attempts
- Identify unusual authentication activity

---

# Practical Lab 8 — Performance Investigation

Display top resource consumers:

```bash
top
```

Sort by CPU:

```bash
ps aux --sort=-%cpu | head
```

Sort by memory:

```bash
ps aux --sort=-%mem | head
```

Objectives:

- Identify resource-intensive processes
- Correlate with application behavior

---

# Practical Lab 9 — Storage Investigation

Review block devices:

```bash
lsblk
```

Review UUIDs:

```bash
blkid
```

Objectives:

- Validate storage configuration
- Compare with `/etc/fstab`

---

# Practical Lab 10 — Comprehensive Troubleshooting Report

Prepare a report including:

- Incident summary
- Timeline
- Symptoms
- Investigation steps
- Commands executed
- Root cause
- Resolution
- Validation
- Preventive recommendations

This mirrors documentation expected in enterprise environments.

---

# Enterprise Scenario 1

## Production Web Server Outage

Symptoms:

- HTTPS unavailable
- SSH functioning normally

Investigation:

```text
Service Status

↓

Service Logs

↓

Network Ports

↓

Firewall Rules

↓

Configuration Validation

↓

Recovery

↓

Validation
```

Root Cause (example):

- Invalid web server configuration introduced during deployment

---

# Enterprise Scenario 2

## Storage Exhaustion

Symptoms:

- Package updates fail
- Applications cannot write files

Investigation:

- Review filesystem usage
- Identify large directories
- Check deleted-but-open files
- Archive or remove unnecessary data
- Verify normal application behavior

---

# Enterprise Scenario 3

## Memory Pressure

Symptoms:

- Slow response times
- Frequent swapping

Investigation:

```text
Memory Usage

↓

Top Processes

↓

Application Logs

↓

Recent Changes

↓

Resolution
```

Possible causes include:

- Memory leaks
- Unexpected workloads
- Misconfigured applications

---

# Enterprise Scenario 4

## Network Connectivity Failure

Symptoms:

- Internal communication interrupted

Investigation:

- Verify interfaces
- Review routes
- Test connectivity
- Check DNS
- Review firewall policy
- Validate service listeners

---

# Enterprise Scenario 5

## Suspected Security Incident

Observed:

- Multiple failed logins
- New administrative account
- Configuration changes outside maintenance window

Response:

```text
Collect Evidence

↓

Preserve Logs

↓

Contain (if required)

↓

Investigate

↓

Recover

↓

Lessons Learned
```

---

# Enterprise Troubleshooting Checklist

| Area | Verification |
|------|--------------|
| Boot completed successfully | ✓ |
| Services healthy | ✓ |
| CPU utilization acceptable | ✓ |
| Memory available | ✓ |
| Storage sufficient | ✓ |
| Network operational | ✓ |
| DNS functioning | ✓ |
| Firewall verified | ✓ |
| Logs reviewed | ✓ |
| Security events assessed | ✓ |
| Documentation updated | ✓ |

---

# Linux Troubleshooting Cheat Sheet

## System Information

```bash
hostnamectl
```

```bash
uname -a
```

```bash
uptime
```

---

## CPU & Memory

```bash
top
```

```bash
free -h
```

```bash
ps aux
```

---

## Storage

```bash
df -h
```

```bash
du -sh *
```

```bash
lsblk
```

---

## Filesystems

```bash
mount
```

```bash
blkid
```

---

## Networking

```bash
ip addr
```

```bash
ip route
```

```bash
ss -tulpn
```

---

## DNS

```bash
cat /etc/resolv.conf
```

```bash
dig example.com
```

---

## Services

```bash
systemctl status service
```

```bash
systemctl --failed
```

---

## Logs

```bash
journalctl -b
```

```bash
journalctl -xe
```

```bash
dmesg
```

---

## Authentication

Ubuntu/Debian:

```bash
grep "Failed password" /var/log/auth.log
```

RHEL-family:

```bash
grep "Failed password" /var/log/secure
```

---

## Open Files

```bash
lsof
```

---

# Chapter Summary

In this chapter, you learned:

- Enterprise troubleshooting methodology
- Root cause analysis
- Boot troubleshooting
- Service diagnosis
- Process troubleshooting
- Performance analysis
- Storage and filesystem troubleshooting
- Network troubleshooting
- DNS troubleshooting
- Log analysis
- Security incident troubleshooting
- Practical investigation workflows
- Enterprise troubleshooting scenarios

---

# Interview Questions

## Beginner

1. What is the purpose of Linux troubleshooting?
2. Why is root cause analysis important?
3. Which command shows running services?
4. How do you check available disk space?
5. What command displays running processes?
6. How do you view system logs?
7. What is `journalctl` used for?
8. How do you check memory usage?
9. Which file contains DNS resolver configuration?
10. Why should logs be reviewed before restarting a service?

---

## Intermediate

1. Explain an enterprise troubleshooting methodology.
2. How would you troubleshoot a service that fails to start?
3. Describe how to investigate high CPU utilization.
4. How would you troubleshoot DNS failures?
5. Explain the purpose of `systemd-analyze`.
6. How do you identify storage bottlenecks?
7. Describe a structured approach to network troubleshooting.
8. How would you investigate repeated authentication failures?
9. Why is documentation important during incident resolution?
10. How do you differentiate symptoms from root causes?

---

## Advanced

1. Design a troubleshooting workflow for a production outage.
2. Explain how you would diagnose intermittent performance issues.
3. Describe a process for recovering from filesystem corruption.
4. How would you investigate a suspected Linux security incident?
5. Explain how centralized logging improves troubleshooting.
6. Design an enterprise troubleshooting playbook.
7. How would you correlate logs from multiple systems during an outage?
8. Explain how configuration drift contributes to recurring issues.
9. Describe methods for reducing mean time to resolution (MTTR).
10. How would you validate that an incident has been fully resolved?

---

# Key Takeaways

- Effective troubleshooting is structured, evidence-based, and repeatable.
- Root cause analysis prevents recurring incidents.
- Logs are often the most valuable diagnostic resource.
- Storage, network, service, and performance issues should be investigated systematically.
- Documentation, validation, and preventive improvements are essential parts of enterprise operations.

---

# References

## Official Documentation

- `man journalctl`
- `man systemctl`
- `man ps`
- `man top`
- `man free`
- `man df`
- `man mount`
- `man lsblk`
- `man ip`
- `man ss`
- `man dmesg`
- `man lsof`

## Standards & Best Practices

- Linux Foundation Documentation
- Red Hat Enterprise Linux Documentation
- Ubuntu Server Guide
- NIST SP 800-61 (Computer Security Incident Handling Guide)
- NIST Cybersecurity Framework (CSF)
- CIS Benchmarks
- ISO/IEC 27001
- SRE Principles (Site Reliability Engineering)

---

# Next Chapter

➡️ **25-Linux-Interview-Questions.md**

## Topics Covered

- Linux Fundamentals Interview Questions
- File System & Permissions Questions
- Process & Service Questions
- Networking Questions
- Shell Scripting Questions
- Security Questions
- Storage Questions
- Troubleshooting Scenarios
- HR + Technical Interview Questions
- Hands-on Practical Questions
- Scenario-Based Enterprise Questions
- Fresher to Advanced Interview Preparation