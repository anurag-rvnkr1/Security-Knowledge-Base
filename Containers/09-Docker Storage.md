# Chapter 9 – Docker Storage (Volumes & Bind Mounts)

## Overview

Containers are designed to be **ephemeral**, meaning they can be created, stopped, deleted, and recreated at any time. While this behavior makes containers lightweight and portable, it also introduces a challenge: **what happens to application data when a container is removed?**

By default, any data written inside a container's writable layer is lost when the container is deleted. Docker solves this problem through **persistent storage**, allowing data to exist independently of the container lifecycle.

Docker provides several storage mechanisms:

- Volumes
- Bind Mounts
- tmpfs Mounts (Linux)
- Named Volumes
- Anonymous Volumes

These storage options enable applications to preserve data across container restarts, upgrades, and replacements.

Persistent storage is essential for:

- Databases
- Application uploads
- Logs
- Configuration files
- Backups
- CI/CD pipelines
- Shared application data

Understanding Docker storage is fundamental for building reliable and production-ready containerized applications.

---

# Why It Matters

Imagine a PostgreSQL database running inside a container.

```
PostgreSQL

↓

Container

↓

Database Files
```

If the container is removed:

```
Container Deleted

↓

Database Deleted
```

Unless persistent storage is configured, all database data is lost.

Persistent storage allows:

```
Container

↓

Docker Volume

↓

Database Files

↓

Container Recreated

↓

Same Data Available
```

This separation of compute and storage is a core principle of containerized applications.

---

# Docker Storage Architecture

```
                 Container

                      │

             Writable Layer

                      │

      ┌───────────────┼───────────────┐

      ▼                               ▼

 Docker Volume                 Bind Mount

      │                               │

      ▼                               ▼

 Persistent Data             Host Filesystem
```

Docker routes storage operations through different mount types depending on the application's requirements.

---

# Types of Docker Storage

Docker supports three primary mount types.

| Storage Type | Purpose |
|--------------|---------|
| Volume | Docker-managed persistent storage |
| Bind Mount | Direct access to host files/directories |
| tmpfs Mount | In-memory temporary storage (Linux) |

Each type is designed for different use cases.

---

# Writable Layer

Every container has a writable layer.

```
Container

↓

Writable Layer

↓

Temporary Data
```

Characteristics:

- Created when the container starts
- Deleted when the container is removed
- Not intended for persistent application data

The writable layer is suitable only for temporary runtime changes.

---

# Docker Volumes

A Docker Volume is the recommended mechanism for persistent storage.

```
Container

↓

Docker Volume

↓

Host Storage
```

Characteristics:

- Managed by Docker
- Independent of container lifecycle
- Easy to back up
- Portable between containers
- Preferred for production workloads

Typical use cases:

- Databases
- Persistent application data
- Logs
- Shared storage between containers

---

# Named Volumes

Named volumes have an explicit identifier.

Example:

```bash
docker volume create postgres_data
```

Usage:

```
postgres_data

↓

Container

↓

Persistent Storage
```

Advantages:

- Easy identification
- Reusable across containers
- Simple backup and migration
- Managed lifecycle

---

# Anonymous Volumes

Anonymous volumes are created automatically when a mount point is specified without a name.

Example:

```dockerfile
VOLUME /data
```

Docker generates a random volume name.

Characteristics:

- Docker-managed
- Difficult to identify manually
- Suitable for temporary or internal storage needs

---

# Bind Mounts

Bind mounts map a host file or directory directly into a container.

Example:

```
Host Directory

↓

Container Directory
```

Command:

```bash
docker run

-v /home/user/app:/app
```

The container accesses the actual files stored on the host.

Typical use cases:

- Local development
- Source code editing
- Configuration files
- Log collection

---

# tmpfs Mounts

A tmpfs mount stores data only in memory.

```
Container

↓

RAM

↓

Temporary Files
```

Characteristics:

- Extremely fast
- Never written to disk
- Data disappears when the container stops

Typical use cases:

- Temporary secrets
- Session data
- Temporary caches
- Sensitive information

Currently supported on Linux.

---

# Volume Lifecycle

```
Create Volume

      │

Attach to Container

      │

Application Writes Data

      │

Container Removed

      │

Volume Remains

      │

Attach to New Container

      │

Data Preserved
```

This independence from the container lifecycle makes volumes ideal for persistent application data.

---

# Bind Mount Workflow

```
Host Directory

      │

Bind Mount

      │

Container

      │

Read / Write
```

Changes made in the host directory are immediately visible inside the container, and vice versa.

---

# Volume vs Bind Mount

| Feature | Volume | Bind Mount |
|---------|--------|------------|
| Managed by Docker | ✓ | ✗ |
| Uses Host Filesystem Directly | ✗ | ✓ |
| Portable | ✓ | Depends on host path |
| Easy Backup | ✓ | Depends on host tools |
| Best for Production | ✓ | Usually development/configuration |
| Easy Sharing Between Containers | ✓ | ✓ |

---

# Common Use Cases

### Databases

```
PostgreSQL

↓

Docker Volume

↓

Persistent Database
```

---

### Web Development

```
Source Code

↓

Bind Mount

↓

Container

↓

Instant Updates
```

---

### Shared Logs

```
Application

↓

Volume

↓

Log Collector
```

---

### Temporary Cache

```
Application

↓

tmpfs

↓

Memory
```

---

# Key Concepts

## Persistent Storage

Volumes and bind mounts allow data to outlive individual containers.

---

## Decoupling Storage

Application data should be stored separately from the container lifecycle.

---

## Data Portability

Volumes can be reused by multiple containers and backed up independently.

---

## Host Integration

Bind mounts allow containers to interact directly with files on the host system.

---

## Temporary Storage

The writable layer and tmpfs mounts are intended for non-persistent data.

---

## Storage Flexibility

Docker offers multiple storage mechanisms to support development, testing, and production workloads.

---

## Next Section

How It Works

Practical Examples

Hands-on Commands

Best Practices

Common Mistakes

References

---
