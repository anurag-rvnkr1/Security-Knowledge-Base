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

# Part 2 — Unit Files, Dependencies, Service Configuration, Logging with `journalctl`, and Advanced Service Management

---

# Introduction

While `systemctl` is used to control services, the **behavior** of those services is defined by **unit files**.

A unit file specifies:

- How a service starts
- Which user runs it
- What executable is launched
- Restart policies
- Dependencies
- Environment variables
- Resource limits

Understanding unit files is essential for troubleshooting, automation, and securely managing production services.

---

# Unit File Architecture

```text
             systemctl

                  │

                  ▼

          systemd (PID 1)

                  │

                  ▼

          Unit File (.service)

                  │

      ┌───────────┼────────────┐

      │           │            │

  Dependencies  Commands   Restart Policy

                  │

                  ▼

             Running Process
```

---

# Unit File Locations

Common locations:

| Directory | Purpose |
|-----------|----------|
| `/usr/lib/systemd/system/` | Vendor-provided unit files (common on many distributions) |
| `/lib/systemd/system/` | Vendor-provided unit files (used by some distributions) |
| `/etc/systemd/system/` | Administrator-managed units and overrides |
| `/run/systemd/system/` | Runtime-generated units |

> Distribution-specific paths may differ. Administrator customizations typically belong under `/etc/systemd/system/`.

---

# Viewing a Unit File

Display the unit definition:

```bash
systemctl cat ssh
```

or

```bash
systemctl cat ssh.service
```

This shows the active configuration, including any drop-in overrides.

---

# Typical Unit File Structure

```ini
[Unit]
Description=Example Service

[Service]
ExecStart=/usr/bin/example

[Install]
WantedBy=multi-user.target
```

Every section has a specific purpose.

---

# Main Sections

| Section | Purpose |
|----------|----------|
| `[Unit]` | Metadata and dependencies |
| `[Service]` | Runtime configuration |
| `[Install]` | Boot-time integration |

---

# The `[Unit]` Section

Example:

```ini
[Unit]
Description=NGINX Web Server
Documentation=https://nginx.org/
After=network.target
```

Common directives:

| Directive | Purpose |
|-----------|----------|
| `Description=` | Human-readable service description |
| `Documentation=` | Reference documentation |
| `After=` | Start ordering |
| `Before=` | Start ordering |
| `Requires=` | Hard dependency |
| `Wants=` | Soft dependency |

---

# Dependency Relationships

```text
Database

↓

Web Server

↓

Application
```

The application depends on the web server.

The web server depends on networking.

---

# `Requires=` vs `Wants=`

| Directive | Behavior |
|-----------|----------|
| `Requires=` | Required dependency. Failure affects the dependent unit. |
| `Wants=` | Preferred dependency. The dependent unit can still start if this unit is unavailable, subject to its own requirements. |

Example:

```ini
Requires=postgresql.service
```

The service expects PostgreSQL to be available.

---

# `After=` and `Before=`

These directives control **startup order**, not whether another unit is started.

Example:

```ini
After=network.target
```

Meaning:

```text
Network

↓

Application
```

The application starts after networking is available.

---

# The `[Service]` Section

This section defines how the service runs.

Example:

```ini
[Service]
ExecStart=/usr/bin/example
Restart=on-failure
User=appuser
Group=appgroup
```

---

# Important Service Directives

| Directive | Purpose |
|-----------|----------|
| `ExecStart=` | Command used to start the service |
| `ExecStop=` | Command used to stop the service |
| `ExecReload=` | Reload command |
| `WorkingDirectory=` | Working directory |
| `Environment=` | Environment variables |
| `User=` | Service user |
| `Group=` | Service group |
| `Restart=` | Restart behavior |

---

# `ExecStart`

Example:

```ini
ExecStart=/usr/bin/python3 app.py
```

When the service starts:

```text
systemd

↓

Python

↓

Application
```

---

# Running Services as Non-Root

Example:

```ini
User=nginx

Group=nginx
```

Benefits:

- Reduced attack surface
- Least privilege
- Better isolation

Avoid running services as `root` unless necessary.

---

# Working Directory

Example:

```ini
WorkingDirectory=/opt/app
```

The service starts from this directory.

Useful for:

- Relative paths
- Log files
- Configuration files

---

# Environment Variables

Example:

```ini
Environment=PORT=8080
Environment=MODE=production
```

Applications can read these variables at runtime.

---

# Restart Policies

Common options:

| Value | Behavior |
|--------|----------|
| `no` | Never restart automatically |
| `always` | Always restart |
| `on-success` | Restart only after successful exit |
| `on-failure` | Restart after failures |
| `on-abnormal` | Restart after abnormal termination |

Example:

```ini
Restart=on-failure
```

This improves service resilience.

---

# The `[Install]` Section

Example:

```ini
[Install]
WantedBy=multi-user.target
```

This specifies how the unit integrates into the boot process when enabled.

---

# Enabling a Unit

```bash
sudo systemctl enable example.service
```

Internally, `systemd` creates the appropriate boot-time links so the service starts with its target.

---

# Reloading systemd Configuration

After creating or modifying a unit file:

```bash
sudo systemctl daemon-reload
```

This reloads unit definitions without rebooting.

---

# Restarting the Service

```bash
sudo systemctl restart example.service
```

Always restart or reload the service after updating its configuration, as appropriate.

---

# Viewing Service Logs

`systemd` integrates with the system journal.

Command:

```bash
journalctl
```

Displays journal entries from the local system.

---

# View Logs for One Service

Example:

```bash
journalctl -u ssh
```

or

```bash
journalctl -u nginx
```

Useful for troubleshooting service startup and runtime issues.

---

# Display Recent Entries

Example:

```bash
journalctl -n 50
```

Displays the last:

```text
50
```

journal entries.

---

# Follow Logs in Real Time

Equivalent to `tail -f`:

```bash
journalctl -f
```

Monitor a single service:

```bash
journalctl -fu nginx
```

---

# View Boot Logs

Current boot:

```bash
journalctl -b
```

Previous boot:

```bash
journalctl -b -1
```

Useful after reboot-related failures.

---

# Filter by Priority

Example:

```bash
journalctl -p err
```

Show:

- Errors
- Critical events
- Alerts
- Emergencies

---

# Common Priority Levels

| Priority | Meaning |
|----------|----------|
| `emerg` | System unusable |
| `alert` | Immediate action required |
| `crit` | Critical condition |
| `err` | Error |
| `warning` | Warning |
| `notice` | Normal but significant |
| `info` | Informational |
| `debug` | Debugging information |

---

# Viewing Unit Properties

Display detailed configuration:

```bash
systemctl show nginx
```

Examples of information returned:

- Active state
- Main PID
- Memory accounting
- Restart policy
- Unit dependencies

---

# Listing Dependencies

Display dependency tree:

```bash
systemctl list-dependencies nginx
```

This helps identify services required before the selected service starts.

---

# Masking a Service

Prevent a service from being started manually or automatically:

```bash
sudo systemctl mask example.service
```

This creates a stronger restriction than simply disabling the service.

---

# Unmasking a Service

Restore normal operation:

```bash
sudo systemctl unmask example.service
```

---

# Difference Between Disable and Mask

| Command | Effect |
|----------|---------|
| `disable` | Prevents automatic startup during boot |
| `mask` | Prevents the service from being started at all until unmasked |

---

# Viewing Failed Units

```bash
systemctl --failed
```

Typical workflow:

```text
Failed Unit

↓

View Status

↓

Review Journal

↓

Fix Configuration

↓

Restart Service

↓

Verify Health
```

---

# Enterprise Example

Production stack:

```text
systemd

│

├── nginx.service

│

├── postgresql.service

│

├── redis.service

│

└── application.service
```

Dependencies:

```text
Network

↓

Database

↓

Redis

↓

Application

↓

Load Balancer
```

Proper dependency configuration reduces startup failures during reboots.

---

# Cybersecurity Perspective

Security teams monitor for:

- Unauthorized services
- Modified unit files
- Unexpected restart loops
- Services running as `root` without justification
- Disabled security agents
- Newly enabled persistence services
- Suspicious `ExecStart` commands

Adversaries sometimes create malicious unit files to achieve persistence after a reboot.

---

# Business Impact

Proper service configuration enables organizations to:

- Improve application reliability.
- Reduce recovery time.
- Standardize deployments.
- Simplify troubleshooting.
- Support secure operations.
- Increase service availability.

---

# Enterprise Best Practices

- Store administrator-managed unit files under `/etc/systemd/system/`.
- Run services with dedicated non-privileged accounts whenever possible.
- Define explicit dependencies.
- Configure appropriate restart policies.
- Review service logs after configuration changes.
- Mask services that must never run.
- Document all custom services and overrides.

---

# Key Takeaways

- Unit files define how `systemd` manages services.
- `[Unit]`, `[Service]`, and `[Install]` are the primary sections of service unit files.
- `journalctl` is the primary tool for viewing `systemd` logs.
- Dependencies control startup ordering and service relationships.
- Proper unit configuration improves reliability, maintainability, and security.

---


