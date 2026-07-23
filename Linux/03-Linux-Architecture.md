# 03 - Linux Architecture

# Part 1 — Linux Architecture Overview, Operating System Concepts, Kernel Overview, User Space vs Kernel Space, and System Components

---

# Introduction

Linux is designed with a modular architecture that separates hardware management from user applications. This layered design makes Linux highly stable, secure, scalable, and portable across a wide range of devices—from embedded systems and smartphones to enterprise servers and supercomputers.

Unlike monolithic applications, the Linux operating system consists of several cooperating components, each responsible for a specific function. Understanding these components is essential for:

- Linux Administration
- DevOps
- Cloud Computing
- Cybersecurity
- Detection Engineering
- Malware Analysis
- Performance Tuning
- Kernel Debugging

This chapter explores the internal architecture of Linux and explains how applications interact with hardware through the operating system.

---

# Learning Objectives

After completing this chapter, you will be able to:

- Explain the Linux architecture.
- Understand the role of the kernel.
- Differentiate between user space and kernel space.
- Understand system calls.
- Identify major Linux components.
- Describe how Linux interacts with hardware.
- Explain the importance of modular system design.
- Understand Linux architecture from an enterprise perspective.

---

# What is an Operating System?

An **Operating System (OS)** is system software that acts as an intermediary between computer hardware and user applications.

Without an operating system, every application would need to communicate directly with hardware devices, making software development extremely complex.

The operating system provides:

- Process management
- Memory management
- File management
- Device management
- Networking
- Security
- User interfaces

---

# Role of the Operating System

```
+--------------------------------------+
|          User Applications           |
+--------------------------------------+
|       Operating System (Linux)       |
+--------------------------------------+
| CPU | RAM | Disk | NIC | GPU | USB   |
+--------------------------------------+
```

The operating system abstracts hardware complexity and provides standardized interfaces for software.

---

# High-Level Linux Architecture

```
+----------------------------------------------------------+
|                  User Applications                       |
| Browsers | Databases | Docker | Python | Nginx | Git     |
+----------------------------------------------------------+
|                  User Space                              |
| Bash | Libraries | Services | Utilities | GUI            |
+----------------------------------------------------------+
|                 System Call Interface                    |
+----------------------------------------------------------+
|                   Linux Kernel                           |
| Process | Memory | Scheduler | Network | VFS | Drivers   |
+----------------------------------------------------------+
|                     Hardware                             |
| CPU | RAM | SSD | GPU | NIC | Keyboard | USB             |
+----------------------------------------------------------+
```

Each layer communicates with adjacent layers using well-defined interfaces.

---

# Why Linux Uses Layered Architecture

Layered architecture provides:

- Better maintainability
- Stronger security
- Hardware abstraction
- Portability
- Modular development
- Easier debugging
- Better scalability

This design has contributed significantly to Linux's widespread adoption.

---

# Major Components of Linux

A Linux operating system consists of several major components.

| Component | Purpose |
|-----------|---------|
| Kernel | Core operating system |
| Shell | Command interpreter |
| System Libraries | APIs for applications |
| Utilities | Administrative tools |
| File System | Organizes data |
| Bootloader | Starts the operating system |
| Init/System Manager | Starts system services |
| Applications | User software |

---

# Linux Component Relationships

```
Applications
      │
      ▼
Shell / GUI
      │
      ▼
System Libraries
      │
      ▼
System Calls
      │
      ▼
Linux Kernel
      │
      ▼
Hardware
```

Each layer builds upon the services of the lower layer.

---

# The Linux Kernel

The **Linux Kernel** is the core component of the operating system.

It is responsible for:

- CPU scheduling
- Process management
- Memory management
- Device drivers
- Networking
- File systems
- Hardware communication
- Security mechanisms

Every program running on Linux depends on kernel services.

---

# Responsibilities of the Kernel

```
Linux Kernel

├── Process Scheduler
├── Memory Manager
├── Virtual File System
├── Device Drivers
├── Network Stack
├── IPC
├── Security Modules
└── System Call Interface
```

Each subsystem works together to provide a stable and efficient operating environment.

---

# Why the Kernel is Important

Without the kernel:

- Applications cannot access memory.
- Files cannot be read or written.
- Network communication is impossible.
- Hardware devices become inaccessible.
- Process scheduling cannot occur.

The kernel is the foundation of every Linux system.

---

# Kernel Characteristics

Modern Linux kernels provide:

- Multiuser support
- Multitasking
- Multiprocessing (SMP)
- Virtual memory
- Modular drivers
- Loadable kernel modules
- High-performance networking
- Security frameworks
- Container support

These features enable Linux to power everything from embedded devices to hyperscale cloud platforms.

---

# User Space

User space is where normal applications execute.

Examples include:

- Web browsers
- Text editors
- Databases
- Python programs
- Shells
- Desktop environments
- Monitoring tools

Characteristics:

- Restricted privileges
- No direct hardware access
- Isolated from other processes
- Protected by the kernel

---

# Kernel Space

Kernel space is reserved for trusted operating system code.

Characteristics:

- Full hardware access
- Highest privilege level
- Executes kernel subsystems
- Manages system resources
- Handles interrupts
- Controls memory allocation

Only the kernel and authorized kernel modules execute in kernel space.

---

# User Space vs Kernel Space

| Feature | User Space | Kernel Space |
|----------|------------|--------------|
| Privileges | Limited | Full |
| Hardware Access | No | Yes |
| Stability | Process failure usually isolated | Kernel failure can affect the whole system |
| Memory Access | Protected | Full access |
| Examples | Bash, Firefox, Python | Scheduler, Drivers, Network Stack |

This separation enhances both security and system stability.

---

# Why User Space is Isolated

Isolation prevents one application from:

- Accessing another process's memory
- Reading kernel memory
- Modifying hardware directly
- Crashing the operating system

This design is a cornerstone of modern operating system security.

---

# What Happens When an Application Starts?

Example:

```
User starts Firefox

↓

Firefox requests memory

↓

Kernel allocates RAM

↓

Kernel loads executable

↓

Scheduler assigns CPU time

↓

Application executes
```

Every stage involves interaction with kernel services.

---

# Communication Between User Space and Kernel Space

Applications cannot communicate directly with hardware.

Instead, communication follows this path:

```
Application

↓

System Call

↓

Kernel

↓

Device Driver

↓

Hardware
```

The kernel validates requests before interacting with hardware.

---

# Privilege Levels

Modern processors support multiple privilege levels, often called **rings**.

Simplified view:

| Ring | Typical Use |
|------|-------------|
| Ring 0 | Kernel |
| Ring 3 | User Applications |

Linux primarily uses:

- **Ring 0** for the kernel
- **Ring 3** for user processes

This hardware-enforced separation helps prevent unauthorized access to critical system resources.

---

# Hardware Abstraction

The kernel hides hardware-specific details from applications.

For example, a program reading a file does not need to know:

- The disk manufacturer
- The storage controller model
- The filesystem implementation
- The physical disk location

Instead, it interacts with standard system calls such as `open()`, `read()`, and `write()`.

---

# Advantages of Hardware Abstraction

- Improved portability
- Simplified application development
- Consistent APIs
- Support for diverse hardware
- Easier driver development
- Reduced application complexity

---

# Enterprise Architecture Example

```
                    Users
                      │
                      ▼
             Business Applications
                      │
                      ▼
              Linux User Space
                      │
                      ▼
             Linux Kernel Services
                      │
                      ▼
      Storage • Networking • Memory • CPU
                      │
                      ▼
              Physical Hardware
```

This architecture allows organizations to deploy the same applications across different hardware platforms with minimal changes.

---

# Linux in Modern Enterprise Infrastructure

Linux architecture underpins many technologies, including:

- Web servers
- Database servers
- Kubernetes clusters
- Container runtimes
- Virtualization platforms
- Network appliances
- SIEM platforms
- Security monitoring systems
- Cloud-native applications

Its modular design enables efficient scaling from single servers to large distributed environments.

---

# Business Impact

A strong understanding of Linux architecture enables organizations to:

- Improve troubleshooting accuracy.
- Optimize resource utilization.
- Design scalable infrastructure.
- Strengthen system security.
- Support cloud-native workloads.
- Simplify platform standardization.

---

# Enterprise Best Practices

- Use supported kernel versions.
- Keep kernel packages updated with security patches.
- Restrict unnecessary kernel modules.
- Document system architecture.
- Monitor kernel logs and system events.
- Validate third-party kernel modules before deployment.
- Apply least-privilege principles for user-space applications.

---

# Key Takeaways

- Linux follows a layered architecture that separates applications from hardware.
- The kernel is the central component responsible for managing system resources.
- User space and kernel space are isolated for security and stability.
- Applications access hardware through system calls rather than directly.
- Hardware abstraction allows Linux to support a wide range of devices and platforms.

---

# Part 2 — System Calls, Process Management, Context Switching, CPU Scheduling, Interrupts, and Inter-Process Communication (IPC)

---

# Introduction

Applications running on Linux cannot directly communicate with hardware or access protected system resources. Instead, they rely on the **Linux kernel** through a well-defined mechanism called **system calls**.

The kernel manages thousands of running processes simultaneously by:

- Allocating CPU time
- Managing memory
- Handling hardware interrupts
- Coordinating communication between processes
- Enforcing security policies

Understanding these mechanisms is fundamental for Linux administrators, DevOps engineers, cloud architects, and cybersecurity professionals.

---

# System Calls

A **system call** is a controlled interface through which a user-space application requests services from the Linux kernel.

Instead of interacting directly with hardware, applications invoke kernel functions through system calls.

Examples include:

- Opening files
- Reading data
- Writing data
- Creating processes
- Allocating memory
- Sending network packets

---

# Why System Calls Exist

System calls provide:

- Hardware abstraction
- Security enforcement
- Resource management
- Standardized programming interfaces
- Controlled privilege escalation

Without system calls, user applications could compromise system stability and security.

---

# System Call Workflow

```text
Application
      │
      ▼
System Call
      │
      ▼
Kernel
      │
      ▼
Device Driver
      │
      ▼
Hardware
```

The kernel validates every request before performing the requested operation.

---

# Common Linux System Calls

| System Call | Purpose |
|-------------|---------|
| `open()` | Open a file |
| `close()` | Close a file |
| `read()` | Read data |
| `write()` | Write data |
| `fork()` | Create a new process |
| `execve()` | Execute a program |
| `wait()` | Wait for child process |
| `kill()` | Send signals |
| `socket()` | Create network socket |
| `connect()` | Connect to remote host |
| `mmap()` | Map memory |
| `clone()` | Create threads/containers |

---

# Example: Opening a File

When an application executes:

```bash
cat file.txt
```

The operating system performs a sequence similar to:

```text
cat

↓

open()

↓

Kernel validates permissions

↓

Filesystem driver locates file

↓

Disk reads data

↓

Kernel returns file descriptor

↓

read()

↓

Display output
```

The application never interacts directly with the storage device.

---

# Categories of System Calls

Linux system calls can be grouped into several categories.

| Category | Examples |
|----------|----------|
| Process Management | `fork()`, `execve()`, `wait()` |
| File Operations | `open()`, `read()`, `write()` |
| Device Management | `ioctl()` |
| Memory Management | `mmap()`, `brk()` |
| Networking | `socket()`, `bind()`, `connect()` |
| Security | `setuid()`, `chmod()` |
| IPC | `pipe()`, `shmget()`, `msgsnd()` |

---

# What is a Process?

A **process** is an executing instance of a program.

For example:

```bash
firefox
```

When launched, Linux creates a process containing:

- Program code
- Memory
- CPU registers
- Process ID
- Open files
- Security context
- Environment variables

Every running application is represented by one or more processes.

---

# Program vs Process

| Program | Process |
|----------|---------|
| Static executable file | Running instance of a program |
| Stored on disk | Stored in memory |
| Passive | Active |
| Example: `/usr/bin/vim` | Running `vim` editor |

---

# Process Lifecycle

```text
New
 │
 ▼
Ready
 │
 ▼
Running
 │
 ├──────────────┐
 ▼              │
Waiting         │
 │              │
 ▼              │
Ready ◄─────────┘
 │
 ▼
Terminated
```

A process transitions through several states during its lifetime.

---

# Process States

| State | Description |
|---------|-------------|
| New | Process created |
| Ready | Waiting for CPU |
| Running | Executing instructions |
| Waiting | Waiting for an event or I/O |
| Stopped | Suspended |
| Zombie | Finished but awaiting parent cleanup |
| Terminated | Execution completed |

---

# Process Control Block (PCB)

The kernel stores information about each process in a **Process Control Block (PCB)**.

Typical information includes:

- Process ID (PID)
- Parent PID
- CPU registers
- Scheduling information
- Memory mappings
- Open files
- User credentials
- Process state

The PCB enables the kernel to manage and resume processes efficiently.

---

# Process Hierarchy

Linux processes form a hierarchical tree.

```text
systemd (PID 1)

├── sshd
│     └── bash
│          └── vim
│
├── nginx
│
├── cron
│
└── docker
```

Every process (except PID 1) has a parent process.

---

# Process IDs (PID)

Every process receives a unique **Process ID (PID)**.

Example:

```bash
ps
```

Output:

```text
PID   COMMAND

1     systemd
245   sshd
620   bash
810   python3
```

The PID uniquely identifies a running process.

---

# Parent and Child Processes

Most new processes are created using:

```text
fork()

↓

Child Process

↓

execve()
```

- `fork()` creates a copy of the current process.
- `execve()` replaces the copied process with a new program.

This model is fundamental to Unix and Linux process creation.

---

# Process Creation Workflow

```text
Parent Process

↓

fork()

↓

Child Process

↓

execve()

↓

New Program Runs
```

This design allows efficient process management and flexible program execution.

---

# Context Switching

A CPU can execute only one process per core at any given instant.

When multiple processes compete for CPU time, the kernel performs **context switching**.

During a context switch, the kernel:

- Saves the current process state.
- Loads the next process state.
- Transfers CPU execution.

---

# Context Switching Diagram

```text
CPU

Running Process A

↓

Save Registers

↓

Load Registers

↓

Running Process B
```

The PCB stores the information required to resume execution later.

---

# Why Context Switching is Necessary

Without context switching:

- Only one application could run at a time.
- Multitasking would not exist.
- Interactive computing would be impossible.

Modern Linux systems perform thousands of context switches every second.

---

# CPU Scheduling

The **scheduler** determines which process receives CPU time.

Its goals include:

- Fairness
- Responsiveness
- High throughput
- Low latency
- Efficient CPU utilization

---

# Linux Completely Fair Scheduler (CFS)

Modern Linux kernels primarily use the **Completely Fair Scheduler (CFS)**.

Characteristics:

- Fair CPU allocation
- Dynamic priorities
- Red-black tree scheduling
- Low latency
- Efficient handling of interactive and background workloads

CFS is designed to balance responsiveness with overall system performance.

---

# Scheduling Workflow

```text
Ready Queue

Process A

Process B

Process C

      │
      ▼

Linux Scheduler

      │
      ▼

CPU
```

The scheduler continually evaluates which process should run next.

---

# CPU-Bound vs I/O-Bound Processes

| CPU-Bound | I/O-Bound |
|------------|-----------|
| Heavy computation | Frequent disk/network operations |
| Uses CPU extensively | Often waits for I/O |
| Examples: Video encoding, encryption | Examples: Web servers, databases |

The scheduler attempts to balance these different workload types efficiently.

---

# Interrupts

An **interrupt** is a signal that temporarily pauses the CPU's current work so it can respond to an event requiring immediate attention.

Examples:

- Keyboard input
- Network packet arrival
- Disk completion
- Timer events

Interrupts allow hardware devices to notify the CPU asynchronously.

---

# Interrupt Handling

```text
Hardware Event

↓

Interrupt

↓

CPU Pauses Current Task

↓

Kernel Interrupt Handler

↓

Resume Previous Task
```

Interrupt handling enables responsive interaction with hardware.

---

# Types of Interrupts

| Type | Description |
|------|-------------|
| Hardware Interrupt | Generated by hardware devices |
| Software Interrupt | Generated by software requests |
| Timer Interrupt | Used for scheduling and timekeeping |
| Inter-Processor Interrupt (IPI) | Communication between CPU cores |

---

# Inter-Process Communication (IPC)

Processes often need to exchange data or coordinate actions.

Linux provides several IPC mechanisms.

Common examples:

- Pipes
- Named Pipes (FIFOs)
- Message Queues
- Shared Memory
- Semaphores
- UNIX Domain Sockets
- Signals

Each mechanism is suited to different communication patterns.

---

# IPC Overview

```text
Process A

↓

IPC Mechanism

↓

Kernel

↓

Process B
```

The kernel ensures synchronization and controlled data exchange between processes.

---

# Business Impact

Efficient process management and scheduling help organizations:

- Improve application responsiveness.
- Maximize CPU utilization.
- Support large numbers of concurrent users.
- Maintain predictable system performance.
- Reduce service interruptions.

---

# Enterprise Best Practices

- Monitor process behavior regularly.
- Avoid unnecessary background services.
- Keep kernel updates current for scheduler improvements and security fixes.
- Use appropriate process priorities for critical workloads.
- Monitor interrupt rates and CPU utilization on production systems.
- Choose IPC mechanisms appropriate for application design and performance requirements.

---

# Key Takeaways

- System calls provide a secure interface between applications and the kernel.
- Every running application is represented as a process with its own PCB and PID.
- Context switching enables multitasking by sharing CPU time among processes.
- The Linux Completely Fair Scheduler (CFS) balances responsiveness and fairness.
- Interrupts allow hardware to communicate efficiently with the CPU.
- IPC mechanisms enable controlled communication between processes.

---


