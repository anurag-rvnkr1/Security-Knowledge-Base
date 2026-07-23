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

# 16 - Linux System Monitoring

# Part 3 — Advanced Monitoring, Log Correlation, Performance Tuning, Capacity Planning, Enterprise Monitoring Platforms, and Incident Analysis

---

# Introduction

Modern enterprise environments rarely consist of a single Linux server.

Organizations monitor:

- Hundreds of Linux servers
- Virtual machines
- Containers
- Kubernetes clusters
- Cloud instances
- Databases
- Applications
- Storage systems
- Network devices

Advanced monitoring focuses on:

- Trend analysis
- Predictive maintenance
- Capacity planning
- Alert correlation
- Root cause analysis
- Performance optimization

---

# Enterprise Monitoring Evolution

```text
Single Server

↓

Multiple Servers

↓

Centralized Monitoring

↓

Dashboards

↓

Alerting

↓

Automation

↓

Predictive Analytics
```

---

# From Reactive to Proactive Monitoring

| Reactive Monitoring | Proactive Monitoring |
|----------------------|----------------------|
| Respond after failure | Detect issues before failure |
| Manual investigation | Automated alerts |
| Downtime likely | Downtime minimized |
| Limited visibility | Continuous visibility |

---

# Performance Baselines

A **baseline** represents normal system behavior under expected workloads.

Typical baseline metrics:

- CPU utilization
- Memory usage
- Load average
- Disk latency
- Disk throughput
- Network throughput
- Process count
- Application response time

Without a baseline, it is difficult to determine whether current behavior is abnormal.

---

# Baseline Example

| Metric | Normal Range |
|----------|--------------|
| CPU | 20–40% |
| Memory | 55–70% |
| Load Average | 0.8–1.5 |
| Disk Usage | Below 75% |
| Network Throughput | 80–120 Mbps |
| Response Time | Below 150 ms |

These values vary depending on workload and hardware.

---

# Trend Analysis

Instead of looking at one measurement:

```text
40%

↓

42%

↓

45%

↓

55%

↓

70%
```

Trend analysis identifies gradual degradation before it becomes an outage.

---

# Capacity Planning

Capacity planning predicts future infrastructure requirements.

Inputs include:

- Historical metrics
- Business growth
- Seasonal demand
- Resource utilization
- Application expansion

---

# Capacity Planning Workflow

```text
Collect Metrics

↓

Analyze Growth

↓

Forecast Capacity

↓

Expand Infrastructure

↓

Continue Monitoring
```

---

# Capacity Planning Example

Current usage:

```text
Disk

75%
```

Growth:

```text
5% per month
```

Prediction:

```text
100%

↓

5 months
```

Action:

Provision additional storage before reaching critical utilization.

---

# Performance Bottlenecks

A bottleneck is the resource limiting overall system performance.

Possible bottlenecks:

- CPU
- Memory
- Storage
- Network
- Database
- Application
- External dependency

---

# Bottleneck Identification

```text
Slow Application

↓

CPU?

↓

Memory?

↓

Disk?

↓

Network?

↓

Application?

↓

Root Cause
```

---

# CPU Bottleneck Indicators

Symptoms:

- High CPU utilization
- High load average
- Long process queues
- Reduced responsiveness

Possible causes:

- Infinite loops
- Inefficient code
- Cryptomining malware
- Large batch processing
- Excessive concurrency

---

# Memory Bottleneck Indicators

Symptoms:

- Heavy swap usage
- Out-of-memory events
- Slow application startup
- Increased disk activity

Possible causes:

- Memory leaks
- Large caches
- Insufficient RAM
- Excessive workloads

---

# Disk Bottleneck Indicators

Symptoms:

- High `%util`
- High `await`
- Slow file access
- Delayed database operations

Possible causes:

- Slow storage
- Heavy write workloads
- Fragmented workloads (filesystem dependent)
- Backup operations
- Log growth

---

# Network Bottleneck Indicators

Symptoms:

- High latency
- Packet loss
- Connection timeouts
- Slow application responses

Possible causes:

- Congestion
- Faulty interfaces
- Routing problems
- Bandwidth saturation

---

# Root Cause Analysis (RCA)

A structured investigation should avoid assumptions.

```text
Alert

↓

Collect Metrics

↓

Review Logs

↓

Correlate Events

↓

Identify Root Cause

↓

Implement Fix

↓

Verify

↓

Document
```

---

# Log Correlation

Performance metrics become significantly more valuable when combined with logs.

Example:

```text
CPU Spike

↓

Authentication Logs

↓

Application Logs

↓

Kernel Logs

↓

Network Events

↓

Incident Timeline
```

This approach helps distinguish legitimate workload increases from operational or security issues.

---

# Time Synchronization

Accurate timestamps are essential.

All monitored systems should synchronize time using services such as:

- NTP
- Chrony

Benefits:

- Reliable event ordering
- Easier forensic analysis
- Accurate alert correlation

---

# Enterprise Alerting

Alerts should be:

- Actionable
- Prioritized
- Accurate
- Timely

---

# Alert Severity

| Severity | Meaning |
|-----------|----------|
| Critical | Immediate service impact |
| High | Significant degradation |
| Medium | Potential issue |
| Low | Informational |

---

# Alert Lifecycle

```text
Metric

↓

Threshold

↓

Alert

↓

Notification

↓

Investigation

↓

Resolution

↓

Closure
```

---

# Avoiding Alert Fatigue

Poor alerting can overwhelm administrators.

Best practices:

- Remove duplicate alerts
- Suppress known maintenance events
- Alert on sustained conditions
- Use escalation policies
- Regularly review thresholds

---

# Enterprise Monitoring Platforms

Common monitoring platforms include:

| Platform | Primary Use |
|-----------|-------------|
| Prometheus | Metrics collection and alerting |
| Grafana | Dashboards and visualization |
| Zabbix | Infrastructure monitoring |
| Nagios | Host and service monitoring |
| Icinga | Enterprise monitoring |
| Datadog | Cloud observability |
| New Relic | Application performance monitoring |
| Elastic Stack | Metrics and log analysis |

---

# Centralized Monitoring Architecture

```text
Linux Servers

↓

Monitoring Agents

↓

Metrics Database

↓

Dashboards

↓

Alert Manager

↓

Operations Team
```

---

# Key Performance Indicators (KPIs)

Organizations commonly track:

| KPI | Purpose |
|------|----------|
| CPU Utilization | Resource efficiency |
| Memory Utilization | Capacity planning |
| Disk Usage | Storage planning |
| Disk Latency | Storage performance |
| Network Throughput | Connectivity health |
| Application Response Time | User experience |
| Error Rate | Service quality |
| Uptime | Availability |

---

# Service Level Indicators (SLIs)

Examples:

- Request latency
- Successful request percentage
- Error rate
- Availability
- Throughput

These metrics are often used to evaluate service health.

---

# Service Level Objectives (SLOs)

Example:

```text
Availability

99.9%
```

Latency objective:

```text
95% of requests

↓

Below 200 ms
```

SLOs define measurable operational targets.

---

# Enterprise Dashboard

```text
System Health

├── CPU

├── Memory

├── Disk

├── Network

├── Processes

├── Services

├── Logs

└── Alerts
```

---

# Performance Tuning Strategy

```text
Measure

↓

Identify Bottleneck

↓

Optimize

↓

Test

↓

Monitor Again
```

Avoid making multiple major changes simultaneously, as this complicates root cause analysis.

---

# Monitoring Containers

Common metrics:

- CPU usage
- Memory usage
- Container restarts
- Disk usage
- Network traffic
- Resource limits

Container orchestration platforms often expose these metrics through integrated monitoring solutions.

---

# Monitoring Virtual Machines

Monitor both:

- Guest operating system
- Hypervisor resources

Potential virtualization-specific issues include:

- CPU steal time
- Storage contention
- Memory overcommitment
- Noisy neighbors

---

# Enterprise Incident Example

## Database Performance Degradation

Timeline:

```text
09:00

↓

CPU Stable

↓

09:10

Disk Latency Increased

↓

09:12

Database Response Time Increased

↓

09:15

Application Timeout

↓

Investigation
```

Root Cause:

Storage array latency caused delayed database I/O.

Resolution:

- Reduce storage contention
- Optimize workload scheduling
- Verify storage performance

---

# Enterprise Incident Example

## Unexpected CPU Spike

Investigation:

```text
Alert

↓

top

↓

ps

↓

Logs

↓

Network

↓

Root Cause
```

Possible findings:

- Scheduled batch job
- Infinite loop
- Cryptomining malware
- Application defect

---

# Enterprise Incident Example

## Memory Exhaustion

Workflow:

```text
Alert

↓

free

↓

vmstat

↓

Process Analysis

↓

Application Logs

↓

Memory Leak Identified
```

Resolution:

- Restart affected service
- Apply software fix
- Increase monitoring frequency

---

# Cybersecurity Perspective

Advanced monitoring is an important component of security operations.

Indicators of compromise may include:

- Persistent abnormal CPU utilization
- Unexpected long-running processes
- Unusual outbound network traffic
- Rapid log growth
- Unauthorized service creation
- Repeated authentication failures
- Sudden resource exhaustion

Monitoring data should be correlated with:

- Authentication logs
- System logs
- Network telemetry
- Endpoint security events
- Threat intelligence

---

# Business Impact

Advanced monitoring enables organizations to:

- Reduce Mean Time to Detect (MTTD)
- Reduce Mean Time to Resolve (MTTR)
- Improve service availability
- Meet SLA commitments
- Improve customer satisfaction
- Optimize infrastructure spending
- Support business continuity

---

# Enterprise Best Practices

- Establish and regularly update performance baselines.
- Monitor historical trends, not just current values.
- Correlate metrics with logs and application events.
- Synchronize system time across all infrastructure.
- Review alert thresholds periodically.
- Perform root cause analysis after major incidents.
- Automate repetitive monitoring tasks where appropriate.
- Document monitoring procedures and escalation paths.
- Test alerting systems during maintenance exercises.
- Continuously refine dashboards based on operational needs.

---

# Key Takeaways

- Effective monitoring requires both real-time visibility and historical analysis.
- Performance baselines enable accurate anomaly detection.
- Capacity planning prevents resource exhaustion.
- Metrics, logs, and alerts should be correlated during investigations.
- Enterprise monitoring platforms provide centralized visibility across infrastructure.
- Continuous monitoring improves reliability, security, and operational efficiency.

---


# 16 - Linux System Monitoring

# Part 4 — Practical Labs, Enterprise Case Studies, Chapter Summary, Interview Questions, and References

---

# Introduction

Monitoring is one of the most important responsibilities of a Linux administrator.

In enterprise environments, monitoring enables teams to:

- Detect problems before users notice
- Prevent outages
- Investigate incidents
- Optimize performance
- Meet Service Level Agreements (SLAs)
- Improve infrastructure reliability

This section focuses on practical monitoring exercises and real-world enterprise scenarios.

---

# Enterprise Monitoring Lifecycle

```text
Collect Metrics

↓

Visualize

↓

Analyze

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

↓

Improve
```

---

# Practical Lab 1 — System Overview

Display system uptime:

```bash
uptime
```

Display kernel information:

```bash
uname -a
```

Display hostname:

```bash
hostnamectl
```

### Objectives

- Review basic system health
- Verify uptime and kernel version

---

# Practical Lab 2 — CPU Monitoring

Display processor information:

```bash
lscpu
```

Interactive monitoring:

```bash
top
```

Per-CPU statistics:

```bash
mpstat -P ALL
```

### Objectives

- Observe CPU utilization
- Identify heavily loaded CPUs

---

# Practical Lab 3 — Memory Monitoring

Display memory usage:

```bash
free -h
```

Continuous monitoring:

```bash
vmstat 2
```

### Questions

- How much memory is available?
- Is swap being used?
- Are there signs of memory pressure?

---

# Practical Lab 4 — Process Investigation

Display all processes:

```bash
ps -ef
```

Sort by CPU usage:

```bash
ps -eo pid,comm,%cpu,%mem --sort=-%cpu | head
```

Sort by memory usage:

```bash
ps -eo pid,comm,%mem,%cpu --sort=-%mem | head
```

### Objectives

- Identify resource-intensive processes
- Compare CPU and memory consumption

---

# Practical Lab 5 — Interactive Process Management

Launch:

```bash
htop
```

Tasks:

- Sort by CPU
- Sort by memory
- Search for a process
- View process tree

> If `htop` is unavailable, perform equivalent observations using `top`.

---

# Practical Lab 6 — Filesystem Monitoring

Display filesystem usage:

```bash
df -h
```

Display filesystem types:

```bash
df -Th
```

### Objectives

- Identify highly utilized filesystems
- Review available storage

---

# Practical Lab 7 — Directory Analysis

Display directory sizes:

```bash
du -h --max-depth=1 /var
```

Largest directories:

```bash
du -ah /var | sort -rh | head -20
```

### Objectives

- Locate storage hotspots
- Identify cleanup opportunities

---

# Practical Lab 8 — Disk I/O Monitoring

Display statistics:

```bash
iostat
```

Extended statistics:

```bash
iostat -x 2
```

### Observe

- Read/write activity
- Device utilization
- Average wait time

---

# Practical Lab 9 — Network Monitoring

Display interfaces:

```bash
ip addr
```

Display interface statistics:

```bash
ip -s link
```

Display connections:

```bash
ss -tuln
```

### Objectives

- Review interface health
- Identify listening services

---

# Practical Lab 10 — Continuous System Monitoring

Run:

```bash
vmstat 2
```

Observe:

- Runnable processes
- Memory
- Swap
- I/O
- CPU

---

# Practical Lab 11 — Historical Statistics

CPU:

```bash
sar -u 5 5
```

Memory:

```bash
sar -r 5 5
```

Disk:

```bash
sar -d 5 5
```

Network:

```bash
sar -n DEV 5 5
```

> Historical reporting requires the `sysstat` package and, on many distributions, an enabled data collection service.

---

# Practical Lab 12 — Process Statistics

Display process statistics:

```bash
pidstat
```

Memory:

```bash
pidstat -r
```

Disk:

```bash
pidstat -d
```

### Objectives

- Monitor process-level resource usage
- Compare workloads

---

# Practical Lab 13 — Monitoring Script

Example:

```bash
#!/usr/bin/env bash

echo "===== System Report ====="

echo "Hostname: $(hostname)"

echo "Uptime:"

uptime

echo

echo "Memory:"

free -h

echo

echo "Disk:"

df -h
```

### Skills Learned

- Automation
- Command substitution
- Reporting

---

# Practical Lab 14 — Resource Alert Script

Example:

```bash
#!/usr/bin/env bash

USAGE=$(df / | awk 'NR==2 {gsub("%","",$5); print $5}')

if [ "$USAGE" -gt 80 ]
then
    echo "Warning: Root filesystem usage is ${USAGE}%"
fi
```

### Enhancement Ideas

- Log alerts
- Send email notifications
- Integrate with monitoring systems

---

# Practical Lab 15 — Performance Investigation

Scenario:

```text
Users report slowness
```

Investigation:

```text
Check uptime

↓

Review load average

↓

Run top

↓

Run vmstat

↓

Run iostat

↓

Review logs

↓

Identify root cause
```

---

# Monitoring Checklist

| Check | Command |
|---------|----------|
| CPU | `top`, `mpstat` |
| Memory | `free`, `vmstat` |
| Processes | `ps`, `top`, `htop` |
| Disk usage | `df`, `du` |
| Disk I/O | `iostat` |
| Network | `ip`, `ss` |
| Historical metrics | `sar` |
| Process statistics | `pidstat` |
| System overview | `uptime` |

---

# Enterprise Case Study 1

# High CPU Utilization

### Symptoms

- Slow applications
- High load average
- Increased response time

### Investigation

```text
top

↓

Identify Process

↓

Review Logs

↓

Verify Workload

↓

Optimize or Restart
```

### Root Cause

A scheduled reporting job consumed excessive CPU resources during peak business hours.

### Resolution

- Reschedule the workload
- Optimize processing
- Monitor future executions

---

# Enterprise Case Study 2

# Memory Leak

### Symptoms

- Growing memory usage
- Increasing swap
- Eventual application failure

### Investigation

```text
free

↓

vmstat

↓

pidstat

↓

Application Logs

↓

Developer Review
```

### Resolution

- Restart affected application
- Deploy updated version
- Increase monitoring frequency

---

# Enterprise Case Study 3

# Disk Bottleneck

### Symptoms

- Slow database
- High `await`
- High `%util`

### Investigation

```text
iostat

↓

Storage Metrics

↓

Application Logs

↓

Storage Team

↓

Resolution
```

### Root Cause

Heavy backup operations overlapped with production database traffic.

### Resolution

- Reschedule backups
- Optimize storage usage
- Validate performance improvements

---

# Enterprise Case Study 4

# Network Congestion

### Symptoms

- Slow remote access
- Packet loss
- High latency

### Investigation

```text
ip -s link

↓

ss

↓

Network Monitoring

↓

Switch Review

↓

Resolution
```

### Possible Causes

- Bandwidth saturation
- Faulty network interface
- Misconfigured switch
- External network issues

---

# Enterprise Dashboard Example

```text
Infrastructure

├── CPU

├── Memory

├── Disk

├── Network

├── Processes

├── Services

├── Alerts

└── Logs
```

---

# Common Monitoring Mistakes

| Mistake | Impact | Better Practice |
|----------|--------|-----------------|
| Monitoring only CPU | Missed bottlenecks | Monitor all major resources |
| Ignoring trends | Late detection | Review historical metrics |
| No alert thresholds | Delayed response | Configure actionable alerts |
| Excessive alerts | Alert fatigue | Tune thresholds and priorities |
| Ignoring disk usage | Filesystem outages | Monitor capacity continuously |
| No baseline | Difficult analysis | Establish normal operating ranges |
| No documentation | Repeated investigations | Document incidents and resolutions |

---

# Enterprise Monitoring Checklist

| Task | Status |
|------|--------|
| CPU monitored | ✓ |
| Memory monitored | ✓ |
| Disk monitored | ✓ |
| Network monitored | ✓ |
| Processes monitored | ✓ |
| Alerts configured | ✓ |
| Baselines established | ✓ |
| Dashboards available | ✓ |
| Historical metrics retained | ✓ |
| Incident procedures documented | ✓ |

---

# Cybersecurity Perspective

Monitoring is a critical component of security operations.

Indicators that warrant investigation include:

- Unexpected CPU spikes
- New long-running processes
- Excessive outbound connections
- Rapid disk growth
- Repeated authentication failures
- Persistent high memory usage
- Sudden service creation or termination

Security teams correlate monitoring data with:

- System logs
- Authentication events
- Network telemetry
- Endpoint detection alerts
- Threat intelligence

This correlation improves the accuracy of incident detection and response.

---

# Business Impact

Comprehensive monitoring provides:

- Higher availability
- Faster incident detection
- Reduced Mean Time to Detect (MTTD)
- Reduced Mean Time to Resolve (MTTR)
- Better customer experience
- Improved SLA compliance
- More effective capacity planning
- Lower operational costs

---

# Enterprise Best Practices

- Define clear monitoring objectives.
- Monitor infrastructure and applications together.
- Establish and regularly review performance baselines.
- Configure alerts based on sustained conditions.
- Retain metrics long enough for trend analysis.
- Correlate metrics, logs, and events during investigations.
- Test monitoring and alerting after major infrastructure changes.
- Review dashboards regularly with operations and security teams.
- Automate repetitive health checks where appropriate.
- Document recurring incidents and lessons learned.

---

# Chapter Summary

In this chapter, you learned:

- System monitoring fundamentals
- CPU monitoring
- Memory monitoring
- Load average
- Process monitoring
- Disk monitoring
- Network monitoring
- Performance analysis
- Capacity planning
- Enterprise monitoring platforms
- Alerting concepts
- Practical monitoring techniques
- Enterprise best practices

---

# Interview Questions

## Beginner

1. What is system monitoring?
2. What information does the `uptime` command provide?
3. What is load average?
4. What does `top` display?
5. What is the purpose of `free -h`?
6. What is the difference between `df` and `du`?
7. What does `ps` display?
8. What does `iostat` monitor?
9. What is swap memory?
10. Why is monitoring important?

---

## Intermediate

1. Explain how to investigate high CPU utilization.
2. What does `%util` represent in `iostat`?
3. Compare `top` and `htop`.
4. How do you identify memory pressure?
5. Explain the role of `sar`.
6. What is a performance baseline?
7. How do you identify a storage bottleneck?
8. Explain process state `Z` (Zombie).
9. Why should historical metrics be retained?
10. How would you investigate a slow Linux server?

---

## Advanced

1. Design an enterprise monitoring architecture for 500 Linux servers.
2. Explain the relationship between MTTD and MTTR.
3. Describe a strategy for preventing alert fatigue.
4. How would you correlate monitoring metrics with security events?
5. Design a capacity planning process for rapidly growing infrastructure.
6. Explain how monitoring supports SRE objectives.
7. How would you investigate intermittent performance degradation?
8. Discuss monitoring considerations for virtualized environments.
9. Design a dashboard for a production Linux environment.
10. Explain how monitoring data supports incident response and post-incident reviews.

---

# Key Takeaways

- Effective monitoring combines CPU, memory, storage, network, and process metrics.
- Historical trends provide more insight than isolated measurements.
- Monitoring and alerting should be actionable and aligned with operational goals.
- Correlating metrics with logs accelerates root cause analysis.
- Enterprise monitoring improves reliability, scalability, and security.

---

# References

## Official Documentation

- `man top`
- `man htop`
- `man ps`
- `man vmstat`
- `man iostat`
- `man sar`
- `man pidstat`
- `man free`
- `man uptime`
- `man ss`

## Standards & Best Practices

- Linux Foundation Documentation
- Red Hat Enterprise Linux Performance Tuning Guide
- Ubuntu Server Guide
- Prometheus Documentation
- Grafana Documentation
- Zabbix Documentation
- Nagios Documentation
- CIS Linux Benchmarks
- NIST SP 800-61 (Computer Security Incident Handling Guide)
- Google Site Reliability Engineering (SRE) Book

---

# Next Chapter

➡️ **17-Linux-Logging.md**

## Topics Covered

- Linux Logging Fundamentals
- Syslog Architecture
- `systemd-journald`
- Log Files and Directories
- Log Rotation (`logrotate`)
- Logging Tools (`journalctl`, `logger`)
- Centralized Logging
- Log Analysis
- Security Logging
- Enterprise Logging Best Practices
- Practical Labs
- Interview Questions
- References