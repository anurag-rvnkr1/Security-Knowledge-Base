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

