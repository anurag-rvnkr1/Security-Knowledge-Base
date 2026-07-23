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

