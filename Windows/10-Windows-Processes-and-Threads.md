# 10-Windows-Processes-and-Threads.md

# Part 1 — Windows Process Fundamentals, Threads, Process Architecture, Scheduling Basics, and Process Lifecycle

---

# Introduction

Every application running on Windows is built upon one or more **processes**.

When you:

- Open Microsoft Word
- Launch Google Chrome
- Start Notepad
- Run PowerShell
- Execute a Python script

Windows creates one or more **processes** that contain the resources needed for execution.

Inside every process are one or more **threads**, which perform the actual work.

Understanding processes and threads is fundamental for:

- Windows System Administration
- Cybersecurity
- Malware Analysis
- Digital Forensics
- Incident Response
- Performance Engineering
- Software Development

Nearly every Windows security investigation begins by examining running processes.

---

# Learning Objectives

By the end of this section, you will understand:

- What a process is
- What a thread is
- Process architecture
- Process lifecycle
- Parent-child relationships
- Process identifiers (PIDs)
- Thread identifiers (TIDs)
- Process scheduling basics
- Windows process management fundamentals

---

# What is a Process?

A **process** is an executing instance of a program.

A program stored on disk becomes a process when Windows loads it into memory and begins execution.

Example:

```text
Program on Disk

↓

User Opens Application

↓

Windows Loads Program

↓

Running Process
```

Examples of processes:

- `notepad.exe`
- `explorer.exe`
- `powershell.exe`
- `cmd.exe`
- `chrome.exe`

---

# Program vs Process

These terms are often confused.

| Program | Process |
|----------|----------|
| Static file | Running instance |
| Stored on disk | Loaded into memory |
| Passive | Active |
| Executable | Executing |

Example:

```text
notepad.exe

↓

Double Click

↓

Running Notepad Process
```

---

# What Does a Process Contain?

Every process includes multiple components.

```text
Process

├── Virtual Memory
├── Threads
├── Handles
├── Security Token
├── Environment Variables
├── Loaded DLLs
├── Heap
├── Stack(s)
└── Process Metadata
```

Together, these components allow the process to execute independently from other processes.

---

# Process Isolation

Windows isolates processes from one another.

```text
Process A

↓

Own Memory

-------------------

Process B

↓

Own Memory
```

By default, one process cannot directly access another process's memory without appropriate permissions and operating system support.

This isolation improves:

- Stability
- Reliability
- Security

---

# Why Process Isolation Matters

Without isolation:

```text
Application A

↓

Overwrite

↓

Application B Memory

↓

System Instability
```

With isolation:

```text
Application A

↓

Own Address Space

-------------------

Application B

↓

Own Address Space
```

Crashes and errors are less likely to affect unrelated applications.

---

# What is a Thread?

A **thread** is the smallest unit of execution managed by the operating system.

A process contains at least one thread.

Example:

```text
Process

↓

Main Thread
```

Without a thread, a process cannot execute instructions.

---

# Process vs Thread

| Process | Thread |
|----------|---------|
| Resource container | Execution unit |
| Own virtual memory | Shares process memory |
| Higher overhead | Lower overhead |
| Own security context | Uses process security context |

Processes provide isolation, while threads perform work.

---

# Multiple Threads

Many applications use multiple threads simultaneously.

Example:

```text
Web Browser

├── UI Thread
├── Network Thread
├── Rendering Thread
├── Audio Thread
└── GPU Thread
```

Multiple threads improve responsiveness and performance.

---

# Single-Threaded Example

```text
Calculator

↓

One Thread

↓

Sequential Execution
```

Simple applications may require only a single thread.

---

# Multi-Threaded Example

```text
Browser

├── Display Webpage
├── Download Images
├── Play Audio
├── Execute JavaScript
└── User Input
```

Each task can run concurrently using different threads.

---

# Benefits of Multi-Threading

Advantages include:

- Better responsiveness
- Improved CPU utilization
- Parallel task execution
- Better user experience
- Improved scalability

Improper synchronization, however, can introduce bugs such as race conditions and deadlocks.

---

# Process Creation

The simplified process creation workflow:

```text
User Starts Application

↓

Windows Loader

↓

Allocate Memory

↓

Load Executable

↓

Load DLLs

↓

Create Primary Thread

↓

Process Begins Execution
```

Windows performs many additional initialization steps internally.

---

# Process Lifecycle

A process typically moves through the following stages:

```text
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

The scheduler determines when a process's threads execute.

---

# Process States

Common execution states include:

| State | Description |
|---------|-------------|
| New | Being created |
| Ready | Waiting for CPU |
| Running | Executing instructions |
| Waiting | Waiting for an event or resource |
| Terminated | Execution completed |

The exact internal state model is more detailed, but these states are useful conceptually.

---

# Process Identifier (PID)

Every process receives a unique **Process Identifier (PID)**.

Example:

```text
Explorer.exe

↓

PID 4120
```

The PID uniquely identifies the process while it exists.

---

# Why PIDs Matter

Administrators use PIDs to:

- Identify processes
- Troubleshoot applications
- Terminate processes
- Analyze malware
- Correlate security events

Many Windows administration tools display PIDs.

---

# Thread Identifier (TID)

Each thread also receives a unique identifier.

```text
Process

↓

Thread

↓

Thread ID (TID)
```

A process may contain dozens—or even hundreds—of threads.

---

# Parent and Child Processes

Many processes create additional processes.

Example:

```text
Explorer.exe

↓

cmd.exe

↓

python.exe
```

This relationship is called a **parent-child process relationship**.

---

# Parent Process Example

```text
Explorer.exe

↓

notepad.exe
```

Explorer starts Notepad, making Explorer the parent process.

---

# Child Process Example

```text
cmd.exe

↓

powershell.exe
```

PowerShell becomes the child process of Command Prompt.

---

# Process Tree

Example:

```text
Explorer.exe

├── Chrome.exe
├── Notepad.exe
├── cmd.exe
│   ├── Python.exe
│   └── Ping.exe
└── Word.exe
```

Process trees are extremely valuable during incident response and malware analysis.

---

# Process Memory Layout (Simplified)

A process typically contains:

```text
High Memory

↓

Stack

↓

Heap

↓

DLLs

↓

Program Code

↓

Low Memory
```

Modern Windows uses virtual memory, and the actual layout is more complex than this simplified representation.

---

# User Mode vs Kernel Mode

Windows separates execution into two protection levels.

```text
Applications

↓

User Mode

------------------------

Operating System

↓

Kernel Mode
```

Applications normally execute in User Mode.

The operating system kernel executes in Kernel Mode with higher privileges.

---

# Why User Mode Matters

If an application crashes:

```text
Application

↓

Crash

↓

Application Ends

↓

Operating System Continues
```

Process isolation and User Mode execution help prevent application failures from crashing the entire operating system.

---

# Process Priority

Windows assigns scheduling priorities to processes and threads.

Common priority classes include:

| Priority | Typical Usage |
|-----------|---------------|
| Idle | Background work |
| Below Normal | Low-priority tasks |
| Normal | Default applications |
| Above Normal | Responsive applications |
| High | Time-sensitive tasks |
| Realtime | Specialized scenarios (use with caution) |

The scheduler considers these priorities when allocating CPU time.

---

# Windows Scheduler Overview

The Windows scheduler determines which thread executes on the CPU.

Simplified workflow:

```text
Ready Threads

↓

Scheduler

↓

CPU

↓

Execution

↓

Next Thread
```

The scheduler aims to balance responsiveness, fairness, and performance.

---

# Context Switching

A **context switch** occurs when the CPU changes from executing one thread to another.

```text
Thread A

↓

Save State

↓

Load Thread B

↓

Continue Execution
```

Context switching enables multitasking but also introduces processing overhead.

---

# Enterprise Example

A user opens Microsoft Outlook.

Windows performs:

```text
Start Outlook

↓

Create Process

↓

Allocate Memory

↓

Load Required DLLs

↓

Create Main Thread

↓

Initialize User Interface

↓

Application Ready
```

Background threads then handle tasks such as email synchronization, notifications, and search indexing.

---

# Cybersecurity Perspective

Processes are one of the primary indicators analyzed during security investigations.

Security analysts examine:

- Unexpected processes
- Parent-child relationships
- Suspicious command-line arguments
- Process injection attempts
- Unsigned executables
- Unusual execution paths
- High-risk child processes

Malware frequently disguises itself as legitimate processes or launches from trusted parent processes.

---

# Business Impact

Understanding process architecture helps organizations:

- Troubleshoot application issues
- Detect malicious software
- Improve performance
- Reduce downtime
- Support incident response
- Improve endpoint security

Reliable process management contributes to overall system stability and security.

---

# Enterprise Best Practices

- Monitor running processes using approved administrative tools.
- Investigate unexpected parent-child relationships.
- Keep operating systems and applications updated.
- Limit execution from untrusted locations.
- Use endpoint protection to monitor process behavior.
- Review high-privilege processes regularly.
- Correlate process activity with authentication and network events.

---

# Practical Labs

## Lab 1 — View Running Processes

Open **Task Manager**.

Navigate to:

```text
Processes
```

Observe:

- Process names
- CPU usage
- Memory usage
- Background processes

---

## Lab 2 — View Process IDs

Open **Command Prompt**.

Run:

```cmd
tasklist
```

Identify:

- Process Name
- PID
- Session Name
- Memory Usage

---

## Lab 3 — View Process Tree (Optional)

Open **Resource Monitor** or **Process Explorer** (Microsoft Sysinternals, if available).

Observe:

- Parent processes
- Child processes
- Process hierarchy

Document the relationships you observe.

---

# Key Takeaways

- A process is a running instance of a program.
- Every process contains one or more threads.
- Threads are the smallest units of execution.
- Windows isolates processes to improve stability and security.
- Every process has a unique PID, and every thread has a unique TID.
- Parent-child process relationships are important during troubleshooting and security investigations.
- The Windows scheduler manages thread execution and CPU allocation.

---

# Interview Questions

1. What is the difference between a program and a process?
2. What is a thread?
3. Why does every process require at least one thread?
4. What is a PID?
5. What is a TID?
6. What is process isolation?
7. What is the difference between User Mode and Kernel Mode?
8. What is a context switch?
9. Why are process trees important in cybersecurity?
10. What is the role of the Windows scheduler?

---

# References

- Microsoft Learn
- Microsoft Windows Process Documentation
- Microsoft Windows Scheduling Documentation
- Microsoft Sysinternals Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

# 10-Windows-Processes-and-Threads.md

# Part 2 — Windows Process Internals, Memory Architecture, Handles, DLLs, Inter-Process Communication (IPC), and Scheduling

---

# Introduction

In the previous section, you learned that a process is a running instance of a program and that threads perform the actual execution.

In this section, we will examine what happens **inside** a process.

Understanding process internals is essential for:

- Windows Administrators
- SOC Analysts
- Malware Analysts
- Incident Responders
- Performance Engineers
- Software Developers
- Reverse Engineers

Many advanced security techniques—including process injection, DLL hijacking, and memory analysis—require a solid understanding of Windows process architecture.

---

# Internal Process Architecture

A simplified Windows process contains several important components.

```text
Process

├── Executable Image
├── Virtual Address Space
├── Threads
├── Stack(s)
├── Heap(s)
├── Loaded DLLs
├── Handles
├── Environment Variables
├── Security Token
└── Process Metadata
```

Each component plays a specific role during execution.

---

# Executable Image

Every process begins with an executable image.

Example:

```text
notepad.exe

↓

Windows Loader

↓

Executable Image

↓

Running Process
```

The executable image contains:

- Machine instructions
- Program resources
- Metadata
- References to required DLLs

---

# Windows Loader

The Windows Loader prepares a process for execution.

Responsibilities include:

- Loading the executable
- Mapping memory
- Loading required DLLs
- Resolving imports
- Creating the primary thread
- Starting execution

Simplified workflow:

```text
Executable

↓

Windows Loader

↓

Memory Allocation

↓

Load DLLs

↓

Primary Thread

↓

Execution Begins
```

---

# Virtual Address Space

Every process receives its own **virtual address space**.

```text
Process A

↓

Virtual Memory A

---------------------

Process B

↓

Virtual Memory B
```

Virtual memory isolates processes and allows each process to believe it owns a continuous memory space.

---

# Why Virtual Memory Exists

Without virtual memory:

```text
Application A

↓

Overwrite

↓

Application B
```

With virtual memory:

```text
Application A

↓

Private Address Space

---------------------

Application B

↓

Private Address Space
```

Benefits include:

- Isolation
- Security
- Efficient memory management
- Simplified programming

---

# Simplified Memory Layout

A typical process memory layout:

```text
High Addresses

↓

Thread Stack

↓

Dynamic Libraries (DLLs)

↓

Heap

↓

Program Data

↓

Program Code (.text)

↓

Low Addresses
```

Actual layouts vary depending on the Windows version, architecture, and security features.

---

# Code Segment

The code segment contains executable instructions.

```text
Program Code

↓

CPU Executes Instructions
```

Normally, application code is not modified during execution.

---

# Data Segment

The data segment stores:

- Global variables
- Static variables
- Initialized data

Example:

```text
Application

↓

Global Configuration

↓

Data Segment
```

---

# Heap

The heap stores dynamically allocated memory.

Example:

```text
Program

↓

Allocate Memory

↓

Heap
```

Applications frequently use the heap for:

- Objects
- Buffers
- Dynamic arrays
- User-generated data

---

# Stack

Every thread has its own stack.

The stack stores:

- Function parameters
- Local variables
- Return addresses
- Temporary data

Example:

```text
Thread

↓

Function Call

↓

Stack
```

---

# Stack vs Heap

| Stack | Heap |
|--------|------|
| Per-thread | Shared within a process |
| Automatic allocation | Dynamic allocation |
| Fast access | More flexible |
| Smaller | Larger |
| Stores local variables | Stores dynamically allocated objects |

---

# Thread Stack Example

```text
main()

↓

login()

↓

validate()

↓

hashPassword()
```

Each function call creates a new stack frame.

When a function returns, its stack frame is removed.

---

# Dynamic Link Libraries (DLLs)

Windows applications rarely contain all required functionality internally.

Instead, they load **Dynamic Link Libraries (DLLs).**

Example:

```text
Application

↓

user32.dll

↓

kernel32.dll

↓

advapi32.dll

↓

ntdll.dll
```

DLLs allow code sharing between multiple applications.

---

# Benefits of DLLs

Advantages include:

- Code reuse
- Smaller executable files
- Easier updates
- Shared functionality
- Reduced memory usage

Many system functions are provided through DLLs rather than individual executables.

---

# DLL Loading

Workflow:

```text
Executable

↓

Windows Loader

↓

Locate DLL

↓

Load DLL

↓

Resolve Functions

↓

Execution Continues
```

---

# DLL Search Order

When loading a DLL, Windows searches multiple locations.

A simplified search order may include:

```text
Application Directory

↓

System Directory

↓

Windows Directory

↓

Directories in PATH
```

The actual search order depends on configuration and security features such as Safe DLL Search Mode.

Improper DLL loading can create security vulnerabilities.

---

# DLL Hijacking

**DLL Hijacking** occurs when an application loads a malicious DLL instead of the intended legitimate DLL.

Example:

```text
Application

↓

Search for DLL

↓

Malicious DLL Found First

↓

Attacker Code Executes
```

Mitigations include:

- Using secure DLL search paths
- Digitally signing software
- Keeping applications updated
- Following secure development practices

---

# Process Handles

A **handle** is a reference to an operating system object.

Processes use handles to interact with resources.

Examples:

- Files
- Registry keys
- Events
- Mutexes
- Processes
- Threads
- Network sockets

---

# Handle Example

```text
Application

↓

Open File

↓

Handle Created

↓

Read File

↓

Close Handle
```

Closing handles when they are no longer needed helps prevent resource leaks.

---

# Common Handle Types

| Handle Type | Example |
|--------------|----------|
| File | Text document |
| Process | Another process |
| Thread | Worker thread |
| Registry | Registry key |
| Event | Synchronization object |
| Mutex | Mutual exclusion |
| Semaphore | Resource coordination |
| Pipe | Inter-process communication |

---

# Handle Lifecycle

```text
Request Resource

↓

Kernel Creates Handle

↓

Application Uses Resource

↓

Handle Closed

↓

Resource Released
```

Applications that fail to close handles may experience resource exhaustion.

---

# Environment Variables

Processes inherit environment variables from their parent process.

Examples:

```text
PATH

TEMP

USERNAME

COMPUTERNAME

SystemRoot
```

Applications use these variables to locate files and configure runtime behavior.

---

# Parent-Child Environment

```text
Explorer.exe

↓

cmd.exe

↓

Python.exe
```

Child processes typically inherit the parent's environment unless it is modified during process creation.

---

# Security Token

Each process has an associated security token.

It contains:

- User SID
- Group SIDs
- Privileges
- Integrity level

Whenever a process accesses a protected resource, Windows consults the security token during authorization.

---

# Inter-Process Communication (IPC)

Processes often need to exchange information.

Windows supports several IPC mechanisms.

```text
Process A

↓

IPC Mechanism

↓

Process B
```

IPC enables applications to cooperate while remaining isolated.

---

# Common IPC Mechanisms

| IPC Method | Typical Usage |
|-------------|---------------|
| Named Pipes | Client-server communication |
| Anonymous Pipes | Parent-child communication |
| Shared Memory | High-speed data exchange |
| Sockets | Network communication |
| RPC | Remote procedure calls |
| COM/DCOM | Component communication |
| Clipboard | User-level data transfer |
| Windows Messages | GUI communication |

---

# Named Pipes

Named Pipes allow processes to communicate using a named communication channel.

Example:

```text
Application A

↓

Named Pipe

↓

Application B
```

They are commonly used by Windows services and client-server applications.

---

# Shared Memory

Shared memory provides high-performance communication.

```text
Process A

↓

Shared Memory

↓

Process B
```

Both processes access the same memory region under controlled conditions.

Synchronization mechanisms are required to prevent data corruption.

---

# Windows Messages

Graphical applications communicate using messages.

Example:

```text
Mouse Click

↓

Window Message

↓

Application

↓

Event Handler
```

This event-driven architecture underpins the Windows graphical user interface.

---

# Process Scheduling

The Windows scheduler determines which thread executes next.

Factors considered include:

- Priority
- CPU availability
- Waiting state
- Processor affinity
- Scheduling policy

Scheduling is performed at the **thread** level rather than the process level.

---

# Ready Queue

Threads ready to execute are placed in a queue.

```text
Ready Thread A

↓

Ready Queue

↓

Scheduler

↓

CPU
```

When CPU time becomes available, the scheduler selects an appropriate thread.

---

# Time Slice (Quantum)

Each runnable thread receives a limited amount of CPU time.

```text
Thread Executes

↓

Quantum Expires

↓

Scheduler Chooses Next Thread
```

This allows multiple applications to appear to run simultaneously.

---

# Thread Priority

Threads inherit a base priority from their process, but Windows may adjust priorities dynamically.

Higher-priority threads generally receive CPU time before lower-priority threads.

Administrators should avoid assigning unnecessarily high priorities, as doing so can negatively affect overall system responsiveness.

---

# Processor Affinity

Processor affinity allows a process or thread to prefer specific CPU cores.

Example:

```text
CPU 0

↓

Application A

-------------------

CPU 1

↓

Application B
```

Affinity can improve performance in specialized workloads but is rarely required for everyday administration.

---

# Enterprise Example

An enterprise web browser launches.

```text
Browser Process

├── UI Thread
├── Renderer Threads
├── GPU Thread
├── Audio Thread
├── Network Threads
└── Extension Threads
```

The scheduler distributes these threads across available CPU cores to maintain a responsive user experience.

---

# Cybersecurity Perspective

Understanding process internals helps analysts detect sophisticated attacks.

Examples include:

- DLL hijacking
- Process injection
- Handle duplication abuse
- Memory tampering
- Malicious child processes
- Suspicious IPC activity

Security tools often monitor process creation, DLL loading, and inter-process interactions to identify malicious behavior.

---

# Business Impact

Knowledge of process internals enables organizations to:

- Diagnose application failures
- Improve performance
- Detect advanced threats
- Reduce downtime
- Support forensic investigations
- Improve endpoint security

Efficient process management contributes to reliable business operations.

---

# Enterprise Best Practices

- Monitor unexpected DLL loading behavior.
- Investigate suspicious parent-child process relationships.
- Keep applications and operating systems updated.
- Minimize unnecessary administrative privileges.
- Use endpoint detection and response (EDR) solutions to monitor process activity.
- Review long-running processes consuming excessive resources.
- Follow secure software development practices to reduce DLL-related vulnerabilities.

---

# Practical Labs

## Lab 1 — View Loaded Modules

Using **Process Explorer** (Microsoft Sysinternals, if available):

1. Select a running process.
2. View its loaded DLLs.
3. Identify common Windows DLLs.

Document your observations.

---

## Lab 2 — Display Environment Variables

Open **Command Prompt**.

Run:

```cmd
set
```

Identify:

- PATH
- TEMP
- USERNAME
- SystemRoot

Observe how these variables influence command execution.

---

## Lab 3 — View Handles (Optional)

Using **Process Explorer**:

1. Select a running process.
2. View open handles.
3. Identify handles to files, registry keys, or synchronization objects.

Do not modify handles on production systems.

---

# Key Takeaways

- Every process has its own virtual address space.
- Threads share process resources but maintain individual stacks.
- DLLs provide reusable functionality shared by multiple applications.
- Handles allow processes to interact with operating system objects.
- Processes communicate using IPC mechanisms such as pipes, shared memory, and sockets.
- The Windows scheduler allocates CPU time to threads, not processes.
- Understanding process internals is essential for administration, troubleshooting, and cybersecurity.

---

# Interview Questions

1. What is virtual memory, and why is it important?
2. What is the difference between the stack and the heap?
3. What is a DLL?
4. What is DLL hijacking?
5. What is a process handle?
6. Name four IPC mechanisms available in Windows.
7. Why does each thread have its own stack?
8. What is a scheduling quantum?
9. What is processor affinity?
10. Why is process internals knowledge important in malware analysis?

---

# References

- Microsoft Learn
- Microsoft Windows Process Architecture Documentation
- Microsoft Sysinternals Documentation
- Microsoft Windows Memory Management Documentation
- *Windows Internals* (Mark Russinovich, David Solomon, Alex Ionescu)

---

