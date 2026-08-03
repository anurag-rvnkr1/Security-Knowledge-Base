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

## How It Works

Container Architecture works by combining Linux kernel features with a container runtime to create isolated environments for applications. Instead of virtualizing hardware like traditional Virtual Machines (VMs), containers virtualize the operating system.

Every container uses the host operating system's kernel while maintaining its own isolated view of processes, networking, filesystems, and resources. This architecture allows multiple applications to run independently on the same host with minimal overhead.

---

# Container Architecture Workflow

```
Application Source Code

          │

          ▼

Dockerfile

          │

          ▼

Container Image

          │

          ▼

Container Runtime

          │

          ▼

Linux Kernel

 ┌────────┼───────────┐

 ▼        ▼           ▼

Namespaces cgroups Filesystems

          │

          ▼

Running Container

          │

          ▼

Application Execution
```

Each layer contributes to creating a secure, lightweight, and isolated execution environment.

---

## Step 1 – Build the Container Image

Developers package an application into a container image.

The image typically contains:

- Application binaries
- Required libraries
- Runtime environment
- Configuration files
- Metadata

Images are immutable and reusable.

---

## Step 2 – Load the Image

The container runtime checks whether the image already exists locally.

If not, it retrieves the image from a container registry.

```
Container Runtime

        │

Image Exists?

   ┌────┴────┐

   │         │

 Yes        No

   │         │

   ▼         ▼

Create   Pull Image

            │

            ▼

      Store Locally

            │

            ▼

        Create Container
```

This ensures the required application image is available before execution.

---

## Step 3 – Create Namespaces

Before starting the application, the runtime creates isolated namespaces.

Typical namespaces include:

- PID Namespace
- Network Namespace
- Mount Namespace
- IPC Namespace
- UTS Namespace
- User Namespace

Example:

```
Host

├── Container A

│      PID 1

│      Hostname: app1

│

└── Container B

       PID 1

       Hostname: app2
```

Although both containers contain a process with PID 1, they are isolated from each other.

---

## Step 4 – Apply Resource Limits

Control Groups (cgroups) allocate and restrict resources.

Example:

```
Container A

CPU: 2 Cores

RAM: 4 GB

Disk I/O Limited


Container B

CPU: 1 Core

RAM: 1 GB

Disk I/O Limited
```

Resource limits prevent individual containers from consuming excessive system resources.

---

## Step 5 – Mount the Filesystem

The runtime assembles multiple image layers into a single unified filesystem.

```
Writable Layer

──────────────

Application Layer

──────────────

Dependency Layer

──────────────

Base Image
```

The writable layer stores runtime changes while lower image layers remain read-only.

This layered approach improves storage efficiency.

---

## Step 6 – Configure Networking

Each container receives an isolated network namespace.

Typical configuration includes:

- Virtual network interface
- IP address
- Routing table
- DNS configuration
- Firewall rules

Containers communicate through configured container networks rather than directly through the host network by default.

---

## Step 7 – Start the Main Process

After initialization:

- The runtime launches the application.
- The first application process becomes **PID 1** inside the container.
- The container remains active while this primary process is running.

```
Container

PID 1

↓

Application

↓

Listening for Requests
```

If the primary process exits, the container also stops unless restarted by a management system.

---

## Step 8 – Runtime Management

During execution, the runtime manages:

- Resource usage
- Process lifecycle
- Network connectivity
- Mounted volumes
- Logging
- Signals (e.g., SIGTERM, SIGKILL)

This ensures stable and predictable application execution.

---

## Step 9 – Stop and Remove the Container

When the workload is no longer required:

```
Running Container

        │

Stop

        │

Container Exits

        │

(Optional)

Remove Container
```

Removing a container does not remove the original image unless explicitly requested.

---

# Practical Examples

## Example 1 – Running Multiple Applications

Scenario:

A server hosts:

- Web Application
- API
- Database
- Redis Cache

Architecture:

```
Host OS

 │

Container Runtime

 ├── Web Container

 ├── API Container

 ├── Database Container

 └── Redis Container
```

Each service operates independently while sharing the same Linux kernel.

Benefits:

- Isolation
- Independent scaling
- Easier maintenance

---

## Example 2 – Resource Isolation

Scenario:

A data processing application consumes excessive CPU.

Without cgroups:

```
One Container

↓

Consumes Entire CPU

↓

Other Applications Slow Down
```

With cgroups:

```
CPU Allocation

Container A → 50%

Container B → 25%

Container C → 25%
```

Resource limits maintain system stability.

---

## Example 3 – Filesystem Layers

Scenario:

Three applications use Ubuntu as their base image.

Instead of storing Ubuntu three times:

```
Ubuntu Base Layer

      │

 ┌────┼────┐

 ▼    ▼    ▼

App1 App2 App3
```

All images reuse the same base layer.

Benefits:

- Smaller images
- Faster downloads
- Reduced storage consumption

---

## Example 4 – Process Isolation

Scenario:

Container A crashes.

Result:

```
Container A

↓

Crash

↓

Restart


Container B

↓

Unaffected
```

Failures are isolated to the affected container.

---

# Hands-on Commands

## View Docker System Information

```bash
docker info
```

Displays:

- Storage driver
- Container runtime
- Operating system
- Number of images
- Running containers
- CPU and memory information

---

## Display Docker Version

```bash
docker version
```

Shows client and server version information.

---

## List Running Containers

```bash
docker ps
```

Displays active containers.

---

## List All Containers

```bash
docker ps -a
```

Displays running and stopped containers.

---

## Inspect a Container

```bash
docker inspect <container_name>
```

Displays detailed JSON information including:

- Network configuration
- Mounted volumes
- Environment variables
- Image ID
- Process information
- Resource limits

---

## Inspect an Image

```bash
docker inspect <image_name>
```

Shows image metadata including:

- Layers
- Architecture
- Creation date
- Configuration
- Entrypoint

---

## Display Running Processes

```bash
docker top <container_name>
```

Shows processes running inside a container.

---

## View Resource Usage

```bash
docker stats
```

Displays real-time:

- CPU usage
- Memory usage
- Network traffic
- Disk I/O

---

## Display Image History

```bash
docker history <image_name>
```

Shows the layers that make up an image.

---

## Display Mounted Volumes

```bash
docker inspect <container_name>
```

Look for the **Mounts** section to view attached volumes and bind mounts.

---

# Best Practices

### 1. Understand the Architecture

Learn how:

- Linux kernel
- Namespaces
- cgroups
- Filesystems
- Container runtimes

work together before moving to orchestration platforms like Kubernetes.

---

### 2. Keep Containers Lightweight

Use minimal base images and install only required software to reduce image size and attack surface.

---

### 3. Limit Resource Consumption

Define CPU and memory limits to prevent resource exhaustion and improve host stability.

---

### 4. Design Stateless Containers

Store persistent data outside containers using volumes or external storage services whenever possible.

---

### 5. Prefer Immutable Images

Never modify production containers directly.

Rebuild images and redeploy containers instead.

---

### 6. Use Standardized Images

Adopt organization-approved base images to improve consistency, maintenance, and security.

---

### 7. Monitor Resource Usage

Regularly observe CPU, memory, storage, and network utilization to identify bottlenecks and optimize performance.

---

