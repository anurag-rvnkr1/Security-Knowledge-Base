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


## How It Works

Docker storage separates **application execution** from **application data**. Containers are designed to be temporary, but application data often needs to persist long after a container has been stopped, replaced, or upgraded.

When a container writes data, Docker determines **where** that data should be stored based on the configured mount type:

- Writable Layer
- Docker Volume
- Bind Mount
- tmpfs Mount

This allows applications to maintain persistent data while keeping containers disposable and easy to replace.

---

# Docker Storage Workflow

```
Application

      │

      ▼

Container

      │

      ▼

Storage Request

      │

 ┌────┼──────────┬────────────┐

 ▼    ▼          ▼            ▼

Writable Layer Volume Bind Mount tmpfs

      │

      ▼

Store Data
```

The destination depends on the storage configuration used when the container starts.

---

# Step 1 – Container Starts

Example:

```bash
docker run postgres
```

Docker creates:

- Container
- Writable layer
- Filesystem
- Network
- Process

Initially, all writes go to the writable layer unless another storage option is configured.

---

# Step 2 – Writing Without a Volume

Suppose PostgreSQL stores database files.

```
PostgreSQL

↓

Writable Layer

↓

Database Files
```

If the container is removed:

```
Container Deleted

↓

Writable Layer Deleted

↓

Database Lost
```

This is why production databases should never rely solely on the writable layer.

---

# Step 3 – Writing with a Docker Volume

Example:

```bash
docker run

-v postgres_data:/var/lib/postgresql/data

postgres
```

Workflow:

```
PostgreSQL

↓

Docker Volume

↓

Host Storage

↓

Persistent Data
```

Now:

```
Container Removed

↓

Volume Remains

↓

Database Preserved
```

The data survives container replacement.

---

# Step 4 – Writing with a Bind Mount

Example:

```bash
docker run

-v /home/user/project:/app
```

Workflow:

```
Host Directory

↓

Bind Mount

↓

Container

↓

Read / Write
```

Any changes made:

- Inside the container
- On the host

are immediately visible in both locations.

This is especially useful during application development.

---

# Step 5 – Using tmpfs

Example:

```bash
docker run

--tmpfs /cache
```

Workflow:

```
Container

↓

RAM

↓

Temporary Files
```

Characteristics:

- Extremely fast
- No disk writes
- Data disappears when the container stops

Suitable for temporary or sensitive information.

---

# Step 6 – Reading Data

When the application requests data:

```
Application

↓

Container

↓

Mounted Storage

↓

Data Returned
```

The application is generally unaware of whether the data resides in:

- Volume
- Bind Mount
- Writable Layer
- tmpfs

The filesystem abstraction remains consistent.

---

# Step 7 – Container Replacement

Suppose an application is upgraded.

Old container:

```
Container V1

↓

Docker Volume
```

Upgrade:

```
Remove Container

↓

Create Container V2

↓

Attach Same Volume

↓

Application Continues
```

Persistent data remains available across deployments.

---

# Practical Examples

## Example 1 – PostgreSQL Database

Command:

```bash
docker run

-v postgres_data:/var/lib/postgresql/data

postgres
```

Workflow:

```
Database

↓

Docker Volume

↓

Persistent Storage
```

The database remains intact even if the container is recreated.

---

## Example 2 – Local Development

Command:

```bash
docker run

-v $(pwd):/app

python-app
```

Workflow:

```
Local Source Code

↓

Bind Mount

↓

Container

↓

Live Updates
```

Editing files on the host immediately affects the running container.

---

## Example 3 – Shared Volume

Two containers share a common volume.

```
Container A

↓

Docker Volume

↓

Container B
```

This enables controlled data sharing between applications.

---

## Example 4 – Temporary Cache

```
Application

↓

tmpfs

↓

RAM

↓

Fast Access
```

The cache is automatically cleared when the container stops.

---

# Hands-on Commands

## List Volumes

```bash
docker volume ls
```

Displays all Docker-managed volumes.

---

## Create a Volume

```bash
docker volume create myvolume
```

Creates a named volume.

---

## Inspect a Volume

```bash
docker volume inspect myvolume
```

Displays:

- Mount point
- Driver
- Labels
- Metadata

---

## Remove a Volume

```bash
docker volume rm myvolume
```

Deletes an unused volume.

---

## Remove Unused Volumes

```bash
docker volume prune
```

Deletes all unused volumes.

---

## Run with a Named Volume

```bash
docker run

-v myvolume:/data

ubuntu
```

Mounts the volume inside the container.

---

## Run with a Bind Mount

```bash
docker run

-v /home/user/project:/app

python
```

Mounts a host directory into the container.

---

## Run with a Read-Only Bind Mount

```bash
docker run

-v /home/user/config:/config:ro

nginx
```

The container can read the files but cannot modify them.

---

## Run with tmpfs

```bash
docker run

--tmpfs /cache

ubuntu
```

Creates an in-memory temporary filesystem.

---

## View Mounted Storage

```bash
docker inspect container_name
```

Review the **Mounts** section to see:

- Volume mounts
- Bind mounts
- Destination paths
- Read/write permissions

---

# Best Practices

### 1. Use Volumes for Persistent Data

Applications such as:

- PostgreSQL
- MySQL
- MongoDB
- Redis (when persistence is enabled)

should store important data in Docker volumes.

---

### 2. Use Bind Mounts for Development

Bind mounts are ideal when developers need to edit source code on the host while the application runs inside the container.

---

### 3. Avoid Storing Important Data in the Writable Layer

The writable layer is temporary.

Always store critical application data in persistent storage.

---

### 4. Use Read-Only Mounts When Appropriate

Configuration files that do not need modification should be mounted as read-only.

This reduces the risk of accidental changes.

---

### 5. Name Volumes Clearly

Instead of anonymous volumes, use descriptive names such as:

```
postgres_data

redis_data

uploads

logs
```

Named volumes are easier to identify and manage.

---

### 6. Back Up Volumes Regularly

Volumes may contain business-critical data.

Implement regular backup procedures and verify recovery processes.

---

### 7. Separate Application Code from Persistent Data

Keep source code, configuration, and persistent data in appropriate storage locations.

This improves maintainability, portability, and disaster recovery.

---

