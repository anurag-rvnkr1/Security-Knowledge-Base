# 10 - Linux Processes

# Part 1 — Process Fundamentals, Process Lifecycle, Parent & Child Processes, Process States, PID, PPID, Process Management Basics

---

# Introduction

A **process** is a running instance of a program.

Every action performed on a Linux system involves one or more processes.

Examples:

- Opening a terminal
- Running Python
- Starting Apache
- Connecting through SSH
- Browsing a website
- Executing a shell script
- Running Docker containers

Everything executed by Linux eventually becomes a process managed by the Linux kernel.

Understanding processes is fundamental for:

- Linux Administration
- DevOps
- Cloud Engineering
- Site Reliability Engineering (SRE)
- SOC Operations
- Digital Forensics (DFIR)
- Malware Analysis
- Performance Tuning

---

# Learning Objectives

After completing this chapter, you will understand:

- What a process is
- Process lifecycle
- Parent and child processes
- Process identifiers
- Process states
- Foreground and background execution
- Kernel process management
- Enterprise monitoring concepts

---

# What is a Process?

A **program** is a static file stored on disk.

Example:

```text
/bin/bash
```

When executed:

```bash
bash
```

Linux loads it into memory.

The running instance becomes a **process**.

---

# Program vs Process

| Program | Process |
|----------|----------|
| Stored on disk | Running in memory |
| Passive | Active |
| Static executable | Dynamic execution |
| Does not consume CPU | Uses CPU, RAM and other resources |
| Example: `/usr/bin/python3` | Example: Running Python interpreter |

---

# Process Architecture

```text
           Executable File

                  │

                  ▼

         Linux Loader (exec)

                  │

                  ▼

         Process Created

                  │

      ┌───────────┼───────────┐

      │           │           │

    Memory       CPU       Resources

      │           │           │

      └───────────┼───────────┘

                  │

                  ▼

          Running Process
```

---

# Process Components

Every process contains:

- Executable code
- Process ID (PID)
- Parent Process ID (PPID)
- Memory space
- Open files
- Environment variables
- Current working directory
- Security credentials
- Threads
- Scheduling information

---

# Process Lifecycle

Every process follows a lifecycle.

```text
Program

↓

Created

↓

Ready

↓

Running

↓

Waiting

↓

Running

↓

Terminated
```

Not every process enters every state for the same duration, but all eventually terminate or are replaced.

---

# Process Creation

Processes are typically created when:

- A user runs a command.
- A service starts.
- A script launches another program.
- A scheduled task executes.
- Another process creates a child process.

---

# Simplified Process Creation

```text
Shell

↓

fork()

↓

Child Process

↓

exec()

↓

Requested Program
```

In Unix-like systems, a shell commonly:

1. Creates a child process (`fork()`).
2. Replaces the child with the requested program (`exec()`).

---

# Parent and Child Processes

Most processes are created by existing processes.

Example:

```text
bash

↓

python

↓

script.py
```

Relationship:

```text
bash

Parent

↓

python

Child
```

---

# Process Tree

```text
systemd (PID 1)

│

├── sshd

│     │

│     └── bash

│            │

│            └── python

│

├── nginx

│

├── cron

│

└── docker
```

Processes form a hierarchical tree.

---

# Parent Process

A parent process:

- Starts another process.
- Receives its PID information.
- May wait for its completion.
- Can manage child processes.

Example:

```text
bash

↓

vim
```

Bash is the parent.

---

# Child Process

The launched program becomes the child.

Example:

```text
bash

↓

vim
```

`vim` is the child process.

---

# Process Identifier (PID)

Every process has a unique numeric identifier.

Example:

```text
PID

↓

4281
```

The kernel uses the PID to identify and manage processes.

---

# Parent Process ID (PPID)

Every child stores its parent's PID.

Example:

```text
PID

↓

4250

PPID

↓

4000
```

This relationship defines the process hierarchy.

---

# Viewing Current Shell PID

Display the current shell's PID:

```bash
echo $$
```

Example:

```text
3241
```

---

# Viewing Parent PID

Display the parent process:

```bash
echo $PPID
```

Example:

```text
2200
```

---

# Display Running Processes

The most common command:

```bash
ps
```

Example:

```text
PID TTY TIME CMD

3214 pts/0 00:00 bash

3260 pts/0 00:00 ps
```

---

# Display Detailed Processes

```bash
ps -ef
```

Typical columns:

| Column | Description |
|----------|-------------|
| UID | Process owner |
| PID | Process ID |
| PPID | Parent PID |
| C | CPU usage indicator |
| STIME | Start time |
| TTY | Terminal |
| TIME | CPU time used |
| CMD | Executed command |

---

# BSD Style Process Listing

```bash
ps aux
```

Common columns:

| Column | Meaning |
|----------|----------|
| USER | Process owner |
| PID | Process ID |
| %CPU | CPU utilization |
| %MEM | Memory utilization |
| VSZ | Virtual memory |
| RSS | Resident memory |
| STAT | Process state |
| COMMAND | Command line |

---

# Viewing Process Tree

Display hierarchy:

```bash
pstree
```

Example:

```text
systemd

├── NetworkManager

├── sshd

│     └── bash

│           └── python

└── nginx
```

`pstree -p` also displays PIDs.

---

# PID 1

On most modern Linux distributions:

```text
systemd
```

runs as:

```text
PID 1
```

Responsibilities include:

- System initialization
- Service management
- Process adoption
- Shutdown handling

---

# Orphan Processes

If a parent exits before its child:

```text
Parent

↓

Terminates

↓

Child

↓

Adopted by PID 1
```

Modern systems typically have `systemd` adopt orphaned processes.

---

# Zombie Processes

A zombie process has:

- Finished execution
- Released most resources
- Retained its process table entry until the parent collects its exit status

```text
Child

↓

Terminates

↓

Parent Has Not Waited

↓

Zombie
```

Zombie processes consume very little memory but occupy entries in the process table.

---

# Process States

Linux processes transition through several states.

| State | Description |
|----------|-------------|
| Running | Currently executing or ready to execute |
| Sleeping | Waiting for an event |
| Interruptible Sleep | Can wake on signals or events |
| Uninterruptible Sleep | Waiting on certain kernel operations (commonly I/O) |
| Stopped | Suspended |
| Zombie | Finished, awaiting parent cleanup |

---

# View Process State

Example:

```bash
ps -eo pid,state,cmd
```

Output:

```text
PID S CMD

101 S sshd

205 R top

310 Z defunct
```

---

# State Codes

| Code | Meaning |
|--------|----------|
| R | Running or runnable |
| S | Interruptible sleep |
| D | Uninterruptible sleep |
| T | Stopped or traced |
| Z | Zombie |
| I | Idle kernel thread (commonly seen on modern kernels) |

---

# Process Scheduling Overview

The Linux scheduler decides:

- Which process runs next
- CPU allocation
- Fairness
- Response time
- Priority handling

Simplified view:

```text
CPU

↓

Scheduler

↓

Process Queue

↓

Selected Process

↓

Execution
```

---

# Process Memory Layout

A simplified process memory layout:

```text
+----------------------+
| Command-line Args    |
+----------------------+
| Environment          |
+----------------------+
| Stack                |
+----------------------+
| Heap                 |
+----------------------+
| Data Segment         |
+----------------------+
| Text (Code)          |
+----------------------+
```

Each process has its own virtual address space, isolated by the operating system.

---

# Viewing Process Information

Inspect a specific process:

```bash
ps -p 1234 -f
```

Replace `1234` with an actual PID.

Useful fields include:

- Parent PID
- Owner
- Start time
- Command

---

# The `/proc` Filesystem

Linux exposes process information through:

```text
/proc
```

Each running process has a directory named after its PID.

Example:

```text
/proc/2451
```

Common files:

| File | Purpose |
|------|----------|
| `status` | Process status |
| `cmdline` | Command-line arguments |
| `environ` | Environment variables |
| `maps` | Memory mappings |
| `fd/` | Open file descriptors |

---

# Viewing Process Status

Example:

```bash
cat /proc/$$/status
```

This displays detailed information about the current shell process.

---

# Enterprise Example

A production application starts:

```text
systemd

↓

nginx

↓

gunicorn

↓

Python Worker

↓

Database Connections
```

Each component is a separate process with its own PID, permissions, memory usage, and lifecycle.

Monitoring this hierarchy simplifies troubleshooting and incident response.

---

# Cybersecurity Perspective

Attackers often:

- Spawn unauthorized processes.
- Launch reverse shells.
- Inject malicious child processes.
- Create long-running persistence mechanisms.
- Hide malicious executables behind legitimate process names.

SOC analysts routinely investigate:

- Unexpected parent-child relationships.
- Suspicious process trees.
- Orphaned processes.
- Long-running unauthorized processes.
- Unusual command-line arguments.

Process analysis is a core component of endpoint detection and response (EDR).

---

# Business Impact

Effective process management helps organizations:

- Improve application reliability.
- Reduce downtime.
- Detect abnormal behavior.
- Troubleshoot performance issues.
- Support incident response.
- Increase infrastructure stability.

---

# Enterprise Best Practices

- Understand normal process hierarchies for critical applications.
- Monitor unexpected parent-child relationships.
- Investigate zombie processes if they accumulate.
- Regularly review long-running privileged processes.
- Use process monitoring as part of security operations.
- Correlate process activity with system logs and audit events.

---

# Key Takeaways

- A process is a running instance of a program.
- Every process has a unique PID and an associated PPID.
- Linux organizes processes into hierarchical trees.
- Processes move through defined lifecycle states.
- The `/proc` filesystem exposes detailed runtime information.
- Process analysis is essential for administration, troubleshooting, and cybersecurity.

---

# Part 2 — Foreground & Background Processes, Job Control, Signals, Process Priorities, `kill`, `nice`, `renice`, and Process Management Commands

---

# Introduction

Linux systems often run hundreds or even thousands of processes simultaneously.

A system administrator must be able to:

- Start processes
- Stop processes
- Pause processes
- Resume processes
- Change priorities
- Terminate unresponsive applications
- Monitor resource consumption

Linux provides numerous tools to manage processes efficiently without rebooting the system.

---

# Foreground Process

A **foreground process** runs interactively and occupies the current terminal.

Example:

```bash
nano notes.txt
```

While `nano` is running:

- The terminal is dedicated to it.
- Other commands cannot be entered until the process exits or is suspended.

---

# Foreground Process Flow

```text
User

↓

Terminal

↓

Foreground Process

↓

Output

↓

Terminal Returned
```

---

# Background Process

A **background process** runs independently of the terminal prompt.

The shell immediately returns control so additional commands can be executed.

Example:

```bash
sleep 300 &
```

Output:

```text
[1] 4258
```

Where:

- `1` → Job number
- `4258` → Process ID (PID)

---

# Background Process Flow

```text
Terminal

↓

Start Command

↓

Background Process

↓

Prompt Immediately Returns
```

---

# Running a Command in Background

Example:

```bash
python backup.py &
```

or

```bash
tar -czf backup.tar.gz /home &
```

These commands continue running while the shell remains usable.

---

# Viewing Background Jobs

Display shell-managed jobs:

```bash
jobs
```

Example:

```text
[1]+ Running sleep 300 &
```

---

# Job Numbers vs Process IDs

| Job Number | Process ID |
|------------|------------|
| Managed by the shell | Managed by the kernel |
| Starts at 1 for each shell session | Unique system-wide |
| Used with `fg` and `bg` | Used with `kill`, `ps`, etc. |

Example:

```text
[2] 5321
```

Job:

```text
2
```

PID:

```text
5321
```

---

# Bringing a Job to the Foreground

Syntax:

```bash
fg %1
```

Example:

```bash
fg %2
```

The selected background job becomes the foreground process.

---

# Sending a Process to the Background

If a foreground process is running:

Suspend it:

```text
Ctrl + Z
```

Example output:

```text
[1]+ Stopped
```

Resume in background:

```bash
bg
```

or

```bash
bg %1
```

---

# Job Control Workflow

```text
Foreground Process

↓

Ctrl + Z

↓

Stopped

↓

bg

↓

Running in Background

↓

fg

↓

Foreground Again
```

---

# Listing Jobs with Details

```bash
jobs -l
```

Example:

```text
[1]+ 4258 Running sleep 300 &
```

This displays both the job number and the PID.

---

# Process Monitoring with `ps`

Display current shell processes:

```bash
ps
```

Display all processes:

```bash
ps -ef
```

Display BSD-style output:

```bash
ps aux
```

---

# Searching for a Process

Use `ps` with `grep`:

```bash
ps -ef | grep nginx
```

Example:

```text
root  1423 ... nginx
```

> **Tip:** `grep` itself may appear in the results. Alternatives such as `pgrep` avoid this.

---

# Using `pgrep`

Search by process name:

```bash
pgrep nginx
```

Display names:

```bash
pgrep -l nginx
```

Example:

```text
1423 nginx

1424 nginx
```

---

# Using `pidof`

Find the PID of a program:

```bash
pidof sshd
```

Example:

```text
1021
```

---

# Real-Time Process Monitoring

The classic monitoring tool:

```bash
top
```

Typical display:

```text
PID

USER

CPU

MEM

TIME

COMMAND
```

Refreshes continuously until exited with:

```text
q
```

---

# Interactive Controls in `top`

| Key | Function |
|------|----------|
| `P` | Sort by CPU usage |
| `M` | Sort by memory usage |
| `k` | Kill a process |
| `r` | Renice a process |
| `h` | Help |
| `q` | Quit |

---

# Using `htop`

Many distributions also provide:

```bash
htop
```

Features include:

- Colorized interface
- Tree view
- Mouse support
- Easier navigation
- Interactive process management

Install if necessary using your distribution's package manager.

---

# Process Signals

Linux communicates with processes using **signals**.

Signals notify a process that an event has occurred.

Examples:

- Termination request
- Interrupt from keyboard
- Pause execution
- Continue execution
- Reload configuration

---

# Signal Flow

```text
Administrator

↓

Signal

↓

Kernel

↓

Target Process

↓

Action Performed
```

---

# Common Signals

| Signal | Number | Purpose |
|----------|--------|----------|
| SIGTERM | 15 | Graceful termination request |
| SIGKILL | 9 | Immediate termination (cannot be caught or ignored) |
| SIGINT | 2 | Interrupt (Ctrl + C) |
| SIGSTOP | 19* | Stop execution |
| SIGCONT | 18* | Continue execution |
| SIGHUP | 1 | Hangup / often used to reload configuration |

> *Signal numbers may vary slightly between Unix-like systems. Signal names are portable.

---

# Viewing Signals

Display available signals:

```bash
kill -l
```

---

# Gracefully Terminating a Process

Syntax:

```bash
kill PID
```

Example:

```bash
kill 4258
```

This sends **SIGTERM (15)** by default.

---

# Forcefully Killing a Process

If the process does not respond:

```bash
kill -9 4258
```

Equivalent:

```bash
kill -SIGKILL 4258
```

Use only when graceful termination fails.

---

# Killing Multiple Processes

```bash
kill PID1 PID2 PID3
```

Example:

```bash
kill 1200 1201 1202
```

---

# Killing by Process Name

Use:

```bash
pkill nginx
```

Specific signal:

```bash
pkill -TERM nginx
```

---

# Using `killall`

Terminate all matching processes:

```bash
killall firefox
```

This targets processes by name rather than PID.

---

# Stopping a Process

Suspend execution:

```bash
kill -STOP PID
```

Resume:

```bash
kill -CONT PID
```

The process remains in memory while stopped.

---

# Keyboard Shortcuts

| Shortcut | Function |
|-----------|----------|
| Ctrl + C | Send SIGINT to the foreground process |
| Ctrl + Z | Suspend the foreground process |
| Ctrl + D | End input (EOF); may exit the shell or program depending on context |

---

# Process Priorities

Linux assigns each process a scheduling priority.

Higher-priority processes generally receive CPU time sooner than lower-priority processes, according to the scheduler's policy.

---

# Nice Value

Range:

```text
-20

↓

0

↓

19
```

| Nice Value | Priority |
|------------|----------|
| -20 | Highest priority |
| 0 | Default |
| 19 | Lowest priority |

Lower nice values correspond to higher scheduling priority.

---

# Starting with a Nice Value

Example:

```bash
nice -n 10 tar -czf backup.tar.gz /home
```

The process starts with a lower CPU scheduling priority than the default.

---

# Viewing Nice Values

```bash
ps -eo pid,ni,cmd
```

Example:

```text
PID NI CMD

1500 0 sshd

2200 10 tar
```

---

# Changing Priority of a Running Process

Syntax:

```bash
renice 5 -p 2200
```

Example output:

```text
2200 (process ID) old priority 0, new priority 5
```

Lowering the nice value (raising priority) generally requires elevated privileges.

---

# Enterprise Example

Backup jobs should not significantly impact production services.

Configuration:

```text
Web Server

↓

Default Priority

Database

↓

High Priority

Nightly Backup

↓

Lower Priority (Higher Nice Value)
```

This helps maintain application responsiveness during backup operations.

---

# Cybersecurity Perspective

Attackers frequently create:

- Hidden background processes
- Reverse shells
- Cryptocurrency miners
- Persistence services
- Long-running unauthorized scripts

SOC analysts investigate:

- Unexpected background jobs
- High CPU usage
- Suspicious command lines
- Unknown parent-child relationships
- Processes with unusual priorities
- Repeatedly respawning processes

Process monitoring is a fundamental endpoint detection capability.

---

# Business Impact

Effective process management enables organizations to:

- Reduce downtime
- Improve system responsiveness
- Optimize resource utilization
- Detect malicious activity
- Improve operational stability
- Troubleshoot production incidents efficiently

---

# Enterprise Best Practices

- Prefer graceful termination (`SIGTERM`) before using `SIGKILL`.
- Avoid unnecessarily increasing process priority.
- Monitor CPU-intensive processes during business hours.
- Use `nice` for long-running batch jobs.
- Investigate unknown background processes promptly.
- Review process trees during incident response.
- Automate monitoring for abnormal process behavior.

---

# Key Takeaways

- Foreground processes occupy the current terminal.
- Background processes allow continued use of the shell.
- Job control uses `jobs`, `fg`, and `bg`.
- Signals control process behavior without restarting the system.
- `kill`, `pkill`, and `killall` terminate processes in different ways.
- `nice` and `renice` influence CPU scheduling priority.
- Process monitoring is essential for both system administration and cybersecurity.

---


