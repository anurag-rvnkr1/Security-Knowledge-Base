# Chapter 2 – Container Architecture

## Overview

Container Architecture is the underlying design that enables containers to run lightweight, isolated applications while sharing the host operating system kernel. Unlike virtual machines, which virtualize hardware and require a complete guest operating system, containers virtualize the operating system by leveraging Linux kernel features.

A container architecture consists of multiple layers working together:

- Hardware
- Host Operating System
- Linux Kernel
- Container Runtime
- Container Images
- Running Containers
- Applications

These components collectively provide isolation, portability, efficiency, and scalability, making containers the preferred choice for modern cloud-native applications.

Understanding container architecture is fundamental to Docker, Kubernetes, container security, DevSecOps, and cloud computing.

---

# Why It Matters

Every container operation—creating an image, starting a container, managing resources, or enforcing security—depends on the underlying architecture.

A strong understanding of container architecture helps you:

- Troubleshoot container issues
- Optimize performance
- Secure workloads
- Understand Docker internals
- Learn Kubernetes more easily
- Design scalable applications
- Prepare for technical interviews
- Work effectively in DevOps and Cloud Security roles

Without understanding the architecture, containers often appear to function like "magic." This chapter explains what happens beneath the surface.

---

# High-Level Container Architecture

```
+------------------------------------------------------+
|                  Applications                        |
+------------------------------------------------------+
|                  Containers                          |
+------------------------------------------------------+
|             Container Runtime                        |
|     (Docker, containerd, CRI-O, Podman)             |
+------------------------------------------------------+
|              Linux Kernel Features                   |
|  Namespaces • cgroups • Filesystems • Networking    |
+------------------------------------------------------+
|             Host Operating System                    |
+------------------------------------------------------+
|                  Physical Hardware                   |
+------------------------------------------------------+
```

Each layer has a distinct responsibility while working together to execute containerized applications.

---

# Container Architecture Components

## 1. Physical Hardware

At the foundation is the physical infrastructure.

Examples:

- CPU
- Memory (RAM)
- Storage
- Network Interfaces
- GPUs
- Disk Controllers

The hardware provides compute resources for the host operating system.

---

## 2. Host Operating System

The host operating system manages hardware resources and provides the Linux kernel used by containers.

Examples:

- Ubuntu
- Debian
- Red Hat Enterprise Linux
- Rocky Linux
- Fedora
- SUSE Linux Enterprise

Although containers can run on Windows and macOS, they typically use a Linux kernel (directly or through virtualization).

Responsibilities include:

- Process scheduling
- Memory management
- Device management
- File systems
- Networking
- Security

---

## 3. Linux Kernel

The Linux kernel is the core of container technology.

Unlike virtual machines, containers **share the host kernel**.

```
Host Kernel

     │

 ┌───┼───────────────┐

 ▼   ▼               ▼

Container 1

Container 2

Container 3
```

The kernel provides:

- Process management
- Memory management
- Networking
- Filesystem support
- Security
- Resource isolation

Without Linux kernel features, modern containers would not exist.

---

## 4. Namespaces

Namespaces provide isolation between containers.

Each container receives its own view of system resources.

Types of namespaces include:

| Namespace | Purpose |
|-----------|---------|
| PID | Process isolation |
| NET | Network isolation |
| MNT | Mount point isolation |
| IPC | Inter-process communication isolation |
| UTS | Hostname isolation |
| USER | User and group isolation |
| CGROUP | cgroup visibility isolation |

Example:

```
Host

 ├── Container A

 │      PID 1

 │      eth0

 │      /

 │

 └── Container B

        PID 1

        eth0

        /
```

Although both containers believe they have PID 1 and an `eth0` interface, they are isolated from one another.

---

## 5. Control Groups (cgroups)

Control Groups (cgroups) manage and limit resource usage.

They control:

- CPU
- Memory
- Disk I/O
- Network bandwidth
- Process count

Example:

```
Host

 │

 ├── Container A

 │      CPU: 2 cores

 │      RAM: 2 GB

 │

 └── Container B

        CPU: 1 core

        RAM: 1 GB
```

Without cgroups, one container could consume all available system resources.

---

## 6. Union File Systems

Container images are built from multiple read-only layers.

```
Layer 5

Application

────────────

Layer 4

Dependencies

────────────

Layer 3

Libraries

────────────

Layer 2

Packages

────────────

Layer 1

Base Image
```

Advantages:

- Faster image downloads
- Layer reuse
- Efficient storage
- Smaller updates
- Reduced build times

Union file systems combine these layers into a single unified filesystem view.

---

## 7. Container Runtime

The runtime manages the complete lifecycle of containers.

Responsibilities include:

- Creating containers
- Starting containers
- Stopping containers
- Removing containers
- Configuring networking
- Applying namespaces
- Applying cgroups
- Mounting filesystems

Popular runtimes:

- containerd
- CRI-O
- Docker Engine
- Podman

The runtime acts as the bridge between container images and running processes.

---

## 8. Container Images

Images are immutable templates used to create containers.

They contain:

- Application binaries
- Libraries
- Runtime
- Configuration
- Metadata

Images do **not** contain:

- Running processes
- Temporary files
- Runtime state

Think of an image as a blueprint for creating containers.

---

## 9. Running Containers

A running container is an instantiated image.

```
Image

   │

Create

   │

Container

   │

Start

   │

Running Application
```

Each running container has:

- Its own filesystem
- Isolated processes
- Independent networking
- Resource limits
- Configurable environment variables

Multiple containers can be created from the same image.

---

# Container Lifecycle

```
Dockerfile

      │

      ▼

Build Image

      │

      ▼

Store Image

      │

      ▼

Pull Image

      │

      ▼

Create Container

      │

      ▼

Start Container

      │

      ▼

Running Container

      │

      ▼

Stop

      │

      ▼

Remove
```

The lifecycle illustrates how an application moves from source code to a running container.

---

# Key Concepts

### Shared Kernel

All containers running on the same host share a single Linux kernel.

This reduces resource usage and enables fast startup times.

---

### Process Isolation

Each container has its own process namespace.

Processes inside one container cannot normally see or interact with processes in another container.

---

### Filesystem Isolation

Containers receive their own filesystem view while sharing underlying image layers.

Changes made inside a running container affect only its writable layer unless persisted externally.

---

### Resource Isolation

CPU, memory, storage, and other resources can be limited using cgroups to prevent one container from monopolizing host resources.

---

### Immutability

Container images are treated as immutable artifacts.

Applications are updated by creating new images and replacing existing containers rather than modifying them in place.

---

### Portability

A container image built on one Linux system can generally run on another compatible Linux system without modification, assuming compatible architecture and runtime.

---

