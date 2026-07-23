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


