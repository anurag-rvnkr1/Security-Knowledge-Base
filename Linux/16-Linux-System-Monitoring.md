# 16 - Linux System Monitoring

# Part 1 — System Monitoring Fundamentals, Performance Metrics, CPU Monitoring, Memory Monitoring, Load Average, and System Health

---

# Introduction

Linux systems continuously generate performance data that helps administrators understand the health of the operating system.

System monitoring is essential for:

- Linux Administration
- DevOps
- Cloud Engineering
- Site Reliability Engineering (SRE)
- Database Administration
- Cybersecurity
- Incident Response
- Capacity Planning

Without monitoring, organizations cannot proactively detect performance issues, security incidents, or hardware failures.

---

# Learning Objectives

After completing this chapter, you will understand:

- System monitoring fundamentals
- Performance metrics
- CPU utilization
- Memory utilization
- Load average
- System uptime
- Performance bottlenecks
- Enterprise monitoring concepts

---

# What is System Monitoring?

System monitoring is the continuous observation of operating system resources.

Resources include:

- CPU
- Memory
- Storage
- Network
- Processes
- Services
- Users
- Hardware

The goal is to maintain:

- Performance
- Availability
- Reliability
- Security

---

# Monitoring Lifecycle

```text
Collect Metrics

↓

Analyze

↓

Detect Issues

↓

Alert

↓

Investigate

↓

Resolve

↓

Verify

↓

Document
```

---

# Why Monitoring Matters

Monitoring helps organizations:

- Detect failures early
- Reduce downtime
- Improve performance
- Prevent outages
- Detect attacks
- Support compliance
- Plan future capacity
- Improve user experience

---

# Enterprise Monitoring Architecture

```text
Linux Servers

↓

Monitoring Agents

↓

Monitoring Server

↓

Time-Series Database

↓

Dashboards

↓

Alerts

↓

Administrators
```

---

# Types of Monitoring

| Type | Examples |
|--------|-----------|
| CPU | Utilization, idle time |
| Memory | RAM, cache, swap |
| Disk | Capacity, I/O |
| Network | Bandwidth, latency |
| Processes | Running services |
| Applications | Response time |
| Security | Authentication events |
| Hardware | Temperature, SMART, sensors |

---

# System Performance Metrics

Important metrics include:

- CPU utilization
- CPU load
- Memory utilization
- Swap usage
- Disk utilization
- I/O wait
- Network throughput
- Running processes
- System uptime

---

# Performance Workflow

```text
Applications

↓

Kernel

↓

System Resources

↓

Metrics

↓

Monitoring Tools

↓

Administrator
```

---

# System Uptime

Display uptime:

```bash
uptime
```

Example:

```text
10:35:22 up 18 days, 5 users, load average: 0.34, 0.42, 0.51
```

Information shown:

- Current time
- System uptime
- Logged-in users
- Load average

---

# Understanding Load Average

Example:

```text
0.80

1.15

0.95
```

These represent average system load over:

| Value | Time Period |
|---------|-------------|
| First | 1 minute |
| Second | 5 minutes |
| Third | 15 minutes |

---

# Interpreting Load Average

For a system with **4 CPU cores**:

| Load | Interpretation |
|--------|----------------|
| 1.0 | Light workload |
| 2.0 | Moderate workload |
| 4.0 | CPUs fully utilized |
| Greater than 4 | Processes waiting for CPU and/or uninterruptible resources |

Load average includes runnable tasks and tasks waiting in uninterruptible sleep (commonly I/O), so it is not solely a CPU metric.

---

# Viewing CPU Information

Display processor information:

```bash
lscpu
```

Example information:

- Architecture
- CPU model
- Core count
- Threads
- Cache sizes
- Virtualization support

---

# CPU Architecture Example

```text
CPU

├── Core 1

├── Core 2

├── Core 3

└── Core 4
```

---

# CPU Monitoring

Common metrics:

- User utilization
- System utilization
- Idle time
- I/O wait
- Interrupt handling
- Context switches

---

# The `top` Command

Launch:

```bash
top
```

Displays:

- CPU usage
- Memory usage
- Running processes
- Load average
- Uptime

Example header:

```text
Tasks

CPU

Memory

Load Average
```

---

# Understanding CPU States in `top`

| State | Meaning |
|---------|----------|
| us | User processes |
| sy | Kernel/system processes |
| ni | Nice (priority-adjusted) processes |
| id | Idle CPU time |
| wa | Waiting for I/O |
| hi | Hardware interrupts |
| si | Software interrupts |
| st | Steal time (virtualized environments) |

---

# CPU Utilization Example

```text
User

35%

System

10%

Idle

55%
```

Interpretation:

The CPU has spare capacity because more than half the time is idle.

---

# Viewing Processor Statistics

```bash
mpstat
```

All processors:

```bash
mpstat -P ALL
```

Provides per-CPU utilization statistics.

---

# Monitoring CPU Continuously

```bash
vmstat 2
```

Updates every:

```text
2 seconds
```

Useful metrics include:

- Runnable processes
- Memory
- Swap
- I/O
- CPU usage

---

# Memory Fundamentals

Memory stores:

- Running programs
- Kernel data
- Buffers
- Cache
- Temporary application data

Unlike storage, RAM is volatile.

---

# Memory Layout

```text
Applications

↓

RAM

├── Used

├── Free

├── Buffers

└── Cache
```

---

# Viewing Memory

Display memory:

```bash
free -h
```

Example:

```text
Total

Used

Free

Shared

Buffers/Cache

Available
```

---

# Understanding `free`

Important columns:

| Column | Meaning |
|----------|----------|
| Total | Installed RAM |
| Used | Memory currently in use (includes cache/buffers) |
| Free | Completely unused memory |
| Available | Estimated memory available for new applications without swapping |
| Swap | Swap usage |

On modern Linux systems, the **Available** column is often the most useful indicator of usable memory.

---

# Linux Memory Management

Linux intentionally uses free memory for:

- Filesystem cache
- Buffers
- Performance optimization

This cached memory can generally be reclaimed when applications require more RAM.

---

# Buffers vs Cache

| Buffers | Cache |
|----------|--------|
| Block device metadata | Cached file contents |
| Improve I/O efficiency | Improve file access performance |

---

# Swap Memory

Swap is disk space used when RAM becomes constrained.

Display swap:

```bash
swapon --show
```

Or:

```bash
free -h
```

---

# Swap Workflow

```text
RAM Full

↓

Inactive Pages

↓

Swap

↓

RAM Available
```

Swap is significantly slower than RAM and excessive swap activity may indicate memory pressure.

---

# Virtual Memory

Linux presents applications with virtual memory.

```text
Application

↓

Virtual Memory

↓

Physical Memory

↓

Swap (if needed)
```

Virtual memory simplifies memory management and process isolation.

---

# Memory Pressure Symptoms

Common signs include:

- Heavy swap usage
- Slow application response
- Increased I/O wait
- Out-of-memory (OOM) events
- Frequent page reclamation

---

# Out-of-Memory (OOM)

If memory is exhausted, the Linux kernel may invoke the **OOM Killer** to terminate one or more processes and recover memory.

Administrators should investigate:

- Memory leaks
- Runaway processes
- Insufficient RAM
- Unexpected workload increases

---

# Enterprise Monitoring Dashboard

Typical dashboard includes:

```text
CPU Usage

Memory Usage

Swap Usage

Load Average

Disk Usage

Network Usage

Running Processes

Alerts
```

---

# Cybersecurity Perspective

Performance anomalies can indicate security incidents.

Examples include:

- Sudden CPU spikes caused by malware or cryptominers
- Unexpected memory growth due to malicious or unstable processes
- Persistent high load from denial-of-service conditions
- Unauthorized background services
- Excessive resource consumption after compromise

Security Operations Centers (SOCs) routinely correlate performance metrics with logs and network events during investigations.

---

# Business Impact

Continuous monitoring enables organizations to:

- Improve availability
- Reduce downtime
- Detect failures earlier
- Meet SLA requirements
- Improve customer experience
- Optimize infrastructure costs
- Support capacity planning

Without monitoring, performance degradation may remain unnoticed until business services are affected.

---

# Enterprise Best Practices

- Establish performance baselines.
- Monitor trends instead of isolated measurements.
- Configure alerts for sustained abnormal utilization.
- Correlate CPU, memory, disk, and network metrics.
- Investigate repeated OOM events promptly.
- Regularly review capacity planning reports.
- Retain historical monitoring data for trend analysis.
- Integrate monitoring with centralized alerting systems.

---

# Key Takeaways

- System monitoring provides continuous visibility into Linux performance.
- CPU utilization, memory usage, and load average are foundational metrics.
- Load average measures runnable and uninterruptible tasks over time.
- Linux uses available memory for caching to improve performance.
- Monitoring trends is more valuable than reacting to single data points.
- Effective monitoring improves reliability, performance, and security.

---


# 16 - Linux System Monitoring

# Part 2 — Process Monitoring, Disk Monitoring, Network Monitoring, Monitoring Tools, and Performance Analysis

---

# Introduction

Monitoring CPU and memory provides only part of the overall system health.

Enterprise administrators must also monitor:

- Running processes
- Storage utilization
- Disk I/O
- Network performance
- System bottlenecks
- Resource contention
- Application behavior

A holistic monitoring approach enables proactive detection and resolution of operational issues.

---

# Enterprise Monitoring Workflow

```text
Collect Metrics

↓

Analyze Performance

↓

Identify Bottleneck

↓

Determine Root Cause

↓

Apply Fix

↓

Verify Improvement

↓

Continue Monitoring
```

---

# Process Monitoring

A **process** is a running instance of a program.

Monitoring processes helps administrators:

- Detect runaway applications
- Investigate high CPU usage
- Identify memory leaks
- Verify service availability
- Detect suspicious processes

---

# Process States

| State | Meaning |
|--------|----------|
| R | Running or runnable |
| S | Interruptible sleep |
| D | Uninterruptible sleep (usually I/O) |
| T | Stopped or traced |
| Z | Zombie |
| I | Idle kernel thread (Linux-specific) |

---

# Viewing Processes

Display running processes:

```bash
ps -ef
```

BSD-style format:

```bash
ps aux
```

Both commands provide:

- PID
- User
- CPU usage
- Memory usage
- Start time
- Command

---

# Process Monitoring Workflow

```text
Application

↓

Process

↓

CPU

↓

Memory

↓

I/O

↓

Administrator
```

---

# Finding Specific Processes

Example:

```bash
ps -ef | grep nginx
```

Or:

```bash
pgrep nginx
```

View detailed information:

```bash
ps -fp <PID>
```

---

# Interactive Process Monitoring

Launch:

```bash
top
```

Common interactive commands:

| Key | Action |
|------|--------|
| `P` | Sort by CPU usage |
| `M` | Sort by memory usage |
| `T` | Sort by cumulative CPU time |
| `k` | Kill a process |
| `r` | Change process priority (renice) |
| `h` | Help |
| `q` | Quit |

---

# Using `htop`

`htop` provides an enhanced interactive interface.

Start:

```bash
htop
```

Features include:

- Colorized display
- Tree view
- Mouse support
- Easier process management
- Search and filtering

If unavailable, install it using your distribution's package manager.

---

# Understanding Zombie Processes

Zombie processes have completed execution but still retain an entry in the process table until the parent process collects their exit status.

Example:

```text
Parent

↓

Child exits

↓

Zombie

↓

Parent reaps child

↓

Removed
```

A small number of transient zombies is normal. Persistent zombies may indicate issues with the parent process.

---

# Disk Monitoring

Disk monitoring includes:

- Capacity
- Read/write activity
- Latency
- Utilization
- Error rates

---

# Filesystem Capacity

Display usage:

```bash
df -h
```

Example:

```text
Filesystem

Size

Used

Avail

Use%
```

---

# Directory Usage

Display directory size:

```bash
du -sh /var
```

Analyze subdirectories:

```bash
du -h --max-depth=1 /var
```

---

# Block Devices

Display devices:

```bash
lsblk
```

Show filesystem information:

```bash
lsblk -f
```

---

# Disk I/O Monitoring

View statistics:

```bash
iostat
```

Extended statistics:

```bash
iostat -x
```

Common metrics:

| Metric | Meaning |
|---------|----------|
| r/s | Read operations per second |
| w/s | Write operations per second |
| rkB/s or kB_read/s | Read throughput |
| wkB/s or kB_wrtn/s | Write throughput |
| await | Average request wait time |
| %util | Approximate device utilization |

Metric names can vary slightly depending on the `sysstat` version.

---

# Interpreting `iostat`

Example:

```text
%util

95%
```

Interpretation:

The storage device is heavily utilized and may be a performance bottleneck.

A high `%util` should be evaluated together with latency (`await`) and workload characteristics.

---

# Monitoring I/O with `vmstat`

Run:

```bash
vmstat 2
```

Relevant fields:

| Field | Meaning |
|--------|----------|
| bi | Blocks received from block devices |
| bo | Blocks sent to block devices |
| wa | CPU waiting for I/O |
| r | Runnable processes |
| b | Processes in uninterruptible sleep |

---

# Network Monitoring

Network monitoring includes:

- Bandwidth
- Connections
- Latency
- Errors
- Packet loss
- Interface statistics

---

# Interface Statistics

Display interface statistics:

```bash
ip -s link
```

View network interfaces:

```bash
ip addr
```

---

# Active Connections

Display listening sockets:

```bash
ss -tuln
```

Established connections:

```bash
ss -tan
```

---

# Network Statistics

View interface counters:

```bash
cat /proc/net/dev
```

Example information:

- RX bytes
- TX bytes
- Errors
- Dropped packets

---

# Bandwidth Monitoring

Examples of tools:

- `sar`
- `iftop`
- `nload`
- `bmon`

Availability depends on installed packages and distribution.

---

# System Activity Reporter (`sar`)

Collect CPU statistics:

```bash
sar -u 5 5
```

Memory statistics:

```bash
sar -r 5 5
```

Disk activity:

```bash
sar -d 5 5
```

Network activity:

```bash
sar -n DEV 5 5
```

The `sysstat` package and data collection service may need to be enabled.

---

# Process Statistics (`pidstat`)

Monitor CPU:

```bash
pidstat 2
```

Memory:

```bash
pidstat -r
```

Disk I/O:

```bash
pidstat -d
```

Useful for identifying resource-intensive processes.

---

# `dstat`

`dstat` combines multiple system metrics.

Example:

```bash
dstat
```

Displays:

- CPU
- Disk
- Network
- Memory
- System

Note that `dstat` may not be installed by default on modern distributions.

---

# Monitoring Overview

```text
CPU

↓

Memory

↓

Processes

↓

Disk

↓

Network

↓

Applications

↓

Administrator
```

---

# Identifying Bottlenecks

| Symptom | Likely Cause |
|----------|--------------|
| High CPU | Compute-intensive processes |
| High load with high I/O wait | Slow storage or blocked I/O |
| Heavy swap usage | Memory pressure |
| High disk utilization | Intensive storage workload |
| High latency | Network congestion or remote issues |
| Packet drops | Interface errors or congestion |

---

# Performance Troubleshooting Workflow

```text
User Reports Issue

↓

Review CPU

↓

Review Memory

↓

Review Disk I/O

↓

Review Network

↓

Review Processes

↓

Identify Root Cause

↓

Implement Fix

↓

Verify
```

---

# Enterprise Monitoring Example

## Slow Database Server

Investigation:

```text
CPU

↓

Memory

↓

Disk Latency

↓

Database Processes

↓

Storage Performance

↓

Root Cause
```

Potential findings:

- High storage latency
- Insufficient memory
- Excessive concurrent queries
- Saturated disks

---

# Enterprise Monitoring Example

## Slow Web Server

Workflow:

```text
Application

↓

CPU

↓

Memory

↓

Network

↓

Logs

↓

Resolution
```

Possible causes:

- Traffic spikes
- Application bugs
- Backend dependency delays
- Resource exhaustion

---

# Enterprise Monitoring Example

## High Load Average

Workflow:

```text
Load Average

↓

CPU Usage

↓

I/O Wait

↓

Processes

↓

Storage

↓

Resolution
```

Remember that high load is not always caused by CPU saturation; blocked I/O can also increase load average.

---

# Enterprise Dashboard Example

```text
CPU Usage

Memory Usage

Swap Usage

Disk Usage

Disk I/O

Network Throughput

Running Processes

System Load

Alerts

Service Status
```

---

# Cybersecurity Perspective

Performance monitoring often reveals security incidents.

Indicators include:

- Sudden CPU spikes from cryptomining malware
- Unexpected network traffic
- New long-running processes
- High disk activity from ransomware
- Abnormal memory consumption
- Numerous outbound connections

Security analysts correlate monitoring metrics with:

- System logs
- Authentication logs
- Network telemetry
- Endpoint detection alerts

---

# Business Impact

Effective monitoring enables organizations to:

- Reduce downtime
- Detect issues before users notice
- Improve SLA compliance
- Optimize infrastructure costs
- Increase service reliability
- Support informed capacity planning

Poor monitoring can lead to prolonged outages, degraded customer experience, and delayed incident response.

---

# Enterprise Best Practices

- Monitor CPU, memory, storage, network, and processes together.
- Establish normal performance baselines.
- Alert on sustained abnormal behavior instead of short-lived spikes.
- Retain historical metrics for trend analysis.
- Correlate infrastructure metrics with application logs.
- Regularly review storage latency and network errors.
- Validate monitoring after infrastructure changes.
- Document recurring performance issues and resolutions.

---

# Key Takeaways

- Process, disk, and network monitoring are essential for complete system visibility.
- Tools such as `top`, `htop`, `ps`, `vmstat`, `iostat`, `sar`, and `pidstat` provide complementary insights.
- Performance bottlenecks should be diagnosed by correlating multiple metrics.
- Historical monitoring data improves troubleshooting and capacity planning.
- Continuous monitoring enhances both operational reliability and cybersecurity.

---
