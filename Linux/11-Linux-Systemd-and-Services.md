# 11 - Linux Systemd and Services

# Part 1 — Introduction to `systemd`, Boot Targets, Units, Unit Types, Service Architecture, and Basic Service Management

---

# Introduction

Modern Linux systems rely on **systemd** as their initialization (init) system and service manager.

When a Linux machine boots:

- The kernel initializes hardware.
- The kernel starts the first userspace process.
- That process initializes the operating system.
- System services are started.
- User login becomes available.

On most modern Linux distributions, this first userspace process is:

```text
systemd
```

which runs as:

```text
PID 1
```

`systemd` is responsible for managing nearly every long-running service on the system.

---

# Learning Objectives

After completing this chapter, you will understand:

- What `systemd` is
- Why it replaced older init systems
- Unit files
- Unit types
- Boot targets
- Service management
- Startup process
- Enterprise service architecture

---

# What is systemd?

`systemd` is:

- The system initialization process
- A service manager
- A dependency manager
- A logging integration framework
- A process supervisor

It manages:

- Web servers
- SSH
- Databases
- Containers
- Scheduled services
- Monitoring agents
- Security software

---

# Evolution of Linux Init Systems

```text
System V Init

        │

        ▼

Upstart

        │

        ▼

systemd
```

Earlier systems relied on sequential startup scripts.

`systemd` introduced:

- Parallel service startup
- Dependency management
- Faster boot times
- Improved service supervision

---

# Why systemd Was Introduced

Older init systems had limitations:

- Slow sequential startup
- Limited dependency handling
- Weak process supervision
- Difficult service management

`systemd` addresses these challenges through:

- Parallel initialization
- Explicit dependencies
- Automatic service restart policies
- Unified management tools

---

# systemd Architecture

```text
              Linux Kernel

                     │

                     ▼

              systemd (PID 1)

                     │

      ┌──────────────┼──────────────┐

      │              │              │

   ssh.service   nginx.service   docker.service

      │              │              │

      ▼              ▼              ▼

  Worker Processes  Worker Processes  Containers
```

---

# Responsibilities of systemd

`systemd` is responsible for:

- Starting services
- Stopping services
- Restarting services
- Monitoring services
- Resolving dependencies
- Managing boot targets
- Handling shutdown and reboot
- Managing timers
- Recording service state

---

# Understanding Services

A **service** is a long-running background process that performs a specific function.

Examples:

| Service | Purpose |
|----------|----------|
| `sshd` | Remote administration |
| `nginx` | Web server |
| `httpd` | Apache web server |
| `docker` | Container runtime |
| `chronyd` | Time synchronization |
| `rsyslog` | System logging |
| `NetworkManager` | Network configuration |

---

# Service Lifecycle

```text
Installed

↓

Enabled

↓

Started

↓

Running

↓

Stopped

↓

Restarted

↓

Disabled

↓

Removed
```

---

# Understanding Units

Everything managed by `systemd` is represented as a **unit**.

Examples:

```text
ssh.service

↓

systemd Unit
```

```text
network.target

↓

systemd Unit
```

A unit is a configuration object that tells `systemd` how to manage a resource.

---

# Unit Types

| Unit Type | Extension | Purpose |
|-----------|-----------|----------|
| Service | `.service` | Background services |
| Target | `.target` | Boot grouping and synchronization |
| Socket | `.socket` | Socket activation |
| Mount | `.mount` | Filesystem mounts |
| Automount | `.automount` | On-demand mounts |
| Timer | `.timer` | Scheduled tasks |
| Device | `.device` | Hardware devices |
| Path | `.path` | Monitor filesystem paths |
| Scope | `.scope` | Externally created processes |
| Slice | `.slice` | Resource management groups |

---

# Service Units

Examples:

```text
sshd.service

nginx.service

docker.service
```

These define how services are:

- Started
- Stopped
- Restarted
- Supervised

---

# Target Units

Targets replace traditional runlevels.

Example:

```text
multi-user.target
```

Targets group related units into operational states.

---

# Boot Process Overview

```text
Firmware

↓

Bootloader

↓

Linux Kernel

↓

systemd (PID 1)

↓

Target Selected

↓

Required Services Start

↓

Login Available
```

---

# Traditional Runlevels

Older Linux systems used runlevels.

| Runlevel | Purpose |
|-----------|----------|
| 0 | Halt |
| 1 | Single-user mode |
| 3 | Multi-user (text) |
| 5 | Multi-user with graphical interface |
| 6 | Reboot |

Modern systems use targets instead.

---

# systemd Targets

| Target | Purpose |
|----------|----------|
| `poweroff.target` | Shutdown |
| `rescue.target` | Single-user recovery |
| `multi-user.target` | Multi-user text environment |
| `graphical.target` | Graphical desktop environment |
| `reboot.target` | Reboot |
| `emergency.target` | Minimal emergency environment |

---

# Target Relationships

```text
graphical.target

        │

        ▼

multi-user.target

        │

        ▼

basic.target

        │

        ▼

sysinit.target
```

Targets build upon one another to provide progressively more functionality.

---

# Viewing Current Target

Display the active target:

```bash
systemctl get-default
```

Example:

```text
graphical.target
```

---

# Viewing Active Units

Display active units:

```bash
systemctl
```

Display only services:

```bash
systemctl --type=service
```

---

# Listing All Services

Include inactive units:

```bash
systemctl list-units --type=service --all
```

This is useful for identifying installed but inactive services.

---

# Checking Service Status

Syntax:

```bash
systemctl status SERVICE
```

Example:

```bash
systemctl status ssh
```

Typical output includes:

- Service state
- Main PID
- Startup time
- Recent log messages
- Unit file path

---

# Service States

Common service states include:

| State | Meaning |
|--------|----------|
| `active (running)` | Service is running |
| `active (exited)` | Service completed successfully but remains active |
| `inactive` | Service is not running |
| `failed` | Service encountered an error |
| `activating` | Service is starting |
| `deactivating` | Service is stopping |

---

# Starting a Service

Syntax:

```bash
sudo systemctl start SERVICE
```

Example:

```bash
sudo systemctl start ssh
```

The service begins immediately without changing its boot-time behavior.

---

# Stopping a Service

```bash
sudo systemctl stop ssh
```

This terminates the running service gracefully when supported.

---

# Restarting a Service

```bash
sudo systemctl restart ssh
```

Useful after:

- Configuration changes
- Software updates
- Troubleshooting

---

# Reloading a Service

Some services support configuration reloads without a full restart.

Example:

```bash
sudo systemctl reload nginx
```

This applies configuration changes while minimizing disruption.

> **Note:** Not every service supports the `reload` operation.

---

# Checking Whether a Service is Running

```bash
systemctl is-active ssh
```

Possible output:

```text
active
```

or

```text
inactive
```

---

# Checking Whether a Service is Enabled

```bash
systemctl is-enabled ssh
```

Example:

```text
enabled
```

or

```text
disabled
```

---

# Enable a Service at Boot

```bash
sudo systemctl enable ssh
```

This configures the service to start automatically during boot.

---

# Disable a Service at Boot

```bash
sudo systemctl disable ssh
```

The service remains installed but will no longer start automatically after reboot.

---

# Difference Between Start and Enable

| Command | Effect |
|----------|---------|
| `start` | Starts the service immediately |
| `stop` | Stops the running service |
| `restart` | Stops and starts the service |
| `reload` | Reloads configuration if supported |
| `enable` | Starts the service automatically at boot |
| `disable` | Prevents automatic startup at boot |

---

# Viewing Failed Services

Display failed units:

```bash
systemctl --failed
```

Example:

```text
UNIT                 LOAD ACTIVE SUB DESCRIPTION

example.service      loaded failed failed Example Service
```

This provides a quick overview of services requiring investigation.

---

# Enterprise Example

A production application stack:

```text
systemd

│

├── nginx.service

├── postgresql.service

├── redis.service

├── docker.service

└── monitoring-agent.service
```

Each service is supervised independently.

If one service fails, `systemd` can often detect the failure and apply configured recovery policies.

---

# Cybersecurity Perspective

Security-critical services managed by `systemd` include:

- SSH
- Audit daemon
- Endpoint Detection and Response (EDR) agents
- Log collection agents
- Firewall services
- Time synchronization
- Authentication services

SOC analysts frequently verify:

- Unexpected running services
- Disabled security agents
- Failed authentication services
- Unauthorized services configured for automatic startup

---

# Business Impact

Reliable service management enables organizations to:

- Improve application availability.
- Accelerate incident recovery.
- Reduce manual administration.
- Support high availability.
- Standardize operational procedures.
- Improve service reliability.

---

# Enterprise Best Practices

- Enable only required services.
- Disable unnecessary services to reduce attack surface.
- Monitor failed services proactively.
- Restart services only after reviewing configuration changes.
- Document service dependencies.
- Validate service status after maintenance activities.
- Review startup services regularly.

---

# Key Takeaways

- `systemd` is the default init system on most modern Linux distributions.
- `systemd` runs as PID 1 and manages system services.
- Everything managed by `systemd` is represented as a unit.
- Services, targets, timers, sockets, and mounts are all unit types.
- `systemctl` is the primary interface for service management.
- Understanding service states and startup behavior is essential for Linux administration.

---

