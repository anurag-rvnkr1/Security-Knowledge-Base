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

## Common Mistakes

Persistent storage is one of the most critical aspects of containerized applications. Many production outages and data-loss incidents occur because storage is misunderstood or configured incorrectly. The following are the most common mistakes related to Docker storage, along with recommended practices to avoid them.

---

# 1. Storing Important Data in the Writable Layer

This is the most common mistake.

```
Application

↓

Writable Layer

↓

Container Removed

↓

Data Lost
```

The writable layer exists only for the lifetime of the container.

**Recommended**

```
Application

↓

Docker Volume

↓

Persistent Storage
```

Critical data should always reside outside the writable layer.

---

# 2. Confusing Volumes with Bind Mounts

Many engineers use bind mounts when Docker volumes are more appropriate.

### Docker Volume

```
Docker

↓

Volume

↓

Persistent Storage
```

- Managed by Docker
- Portable
- Production-friendly
- Easier to back up

---

### Bind Mount

```
Host Directory

↓

Container
```

- Direct access to host files
- Excellent for development
- Depends on host directory structure

Choose the storage mechanism that matches your use case.

---

# 3. Forgetting Volume Backups

Volumes persist beyond the container lifecycle, but they are **not** automatically backed up.

Without backups:

```
Disk Failure

↓

Volume Lost

↓

Application Data Lost
```

Establish a regular backup and recovery strategy for production data.

---

# 4. Mounting the Wrong Directory

Example:

```bash
docker run

-v /home/user:/var/lib/postgresql/data
```

An incorrect host path may:

- Overwrite expected files
- Expose unintended data
- Prevent the application from starting

Always verify both the source and destination paths.

---

# 5. Running Databases Without Persistent Storage

Incorrect:

```bash
docker run postgres
```

Correct:

```bash
docker run

-v postgres_data:/var/lib/postgresql/data

postgres
```

Without persistent storage, deleting the container also deletes the database.

---

# 6. Giving Containers Unnecessary Write Access

Configuration files rarely need write access.

Example:

```bash
-v ./config:/app/config
```

Better:

```bash
-v ./config:/app/config:ro
```

Read-only mounts reduce the risk of accidental modification or compromise.

---

# 7. Ignoring File Permissions

A container process may not have permission to access mounted files.

Typical symptoms:

- "Permission denied"
- Application startup failures
- Read/write errors

Verify:

- File ownership
- User IDs (UIDs)
- Group IDs (GIDs)
- Read/write permissions

---

# 8. Using Anonymous Volumes Without Tracking Them

Example:

```dockerfile
VOLUME /data
```

Docker creates an anonymous volume with a generated name.

Over time:

```
Anonymous Volume

↓

Container Deleted

↓

Volume Remains

↓

Unused Disk Space
```

Named volumes are generally easier to manage.

---

# 9. Assuming Bind Mounts Are Portable

Example:

```bash
-v /home/user/project:/app
```

This path may not exist on another system.

Bind mounts depend on the host filesystem layout, while Docker volumes are more portable across environments.

---

# 10. Sharing Sensitive Host Directories

Avoid mounting directories such as:

```
/

or

/etc

or

/home
```

unless absolutely necessary.

Exposing large portions of the host filesystem increases security risk.

Grant containers access only to the files they genuinely require.

---

# 11. Ignoring Volume Cleanup

Development environments often accumulate:

- Unused named volumes
- Anonymous volumes
- Old test data

Regular cleanup helps reclaim storage and reduce clutter.

Example:

```bash
docker volume prune
```

---

# 12. Using tmpfs for Persistent Data

A `tmpfs` mount stores data in memory only.

```
tmpfs

↓

RAM

↓

Container Stops

↓

Data Disappears
```

Use `tmpfs` only for temporary information such as:

- Session data
- Temporary caches
- Sensitive temporary files

Never store important application data there.

---

# 13. Forgetting That Multiple Containers Can Share a Volume

Example:

```
Container A

↓

Docker Volume

↓

Container B
```

Concurrent writes may introduce:

- Race conditions
- File locking issues
- Data corruption

Ensure applications are designed for shared storage when using shared volumes.

---

# 14. Hardcoding Host Paths

Example:

```bash
-v C:\Users\John\Desktop:/app
```

or

```bash
-v /home/john/project:/app
```

Hardcoded, user-specific paths reduce portability.

Use environment variables, standardized project structures, or Compose configurations where appropriate.

---

# 15. Not Monitoring Storage Usage

Volumes can grow indefinitely.

Examples:

- Database growth
- Log accumulation
- Uploaded files
- Cache expansion

Regularly monitor:

- Disk usage
- Volume size
- Available storage
- Backup status

Monitoring helps prevent unexpected outages due to full disks.

---

# Docker Storage Quick Revision

## Storage Types

| Storage | Best Use |
|----------|----------|
| Writable Layer | Temporary runtime data |
| Docker Volume | Persistent production data |
| Bind Mount | Development and host integration |
| tmpfs | Temporary in-memory storage |

---

## Storage Workflow

```
Application

↓

Container

↓

Volume / Bind Mount

↓

Persistent Storage
```

---

## Common Volume Commands

```bash
docker volume ls

docker volume create

docker volume inspect

docker volume rm

docker volume prune
```

---

## Bind Mount Example

```bash
docker run

-v /home/user/project:/app
```

Maps a host directory into the container.

---

## Volume Example

```bash
docker run

-v postgres_data:/var/lib/postgresql/data

postgres
```

Stores PostgreSQL data persistently in a Docker-managed volume.

---

# Docker Storage Checklist

| Topic | Status |
|--------|:------:|
| Understand Writable Layer | ✓ |
| Understand Docker Volumes | ✓ |
| Understand Named Volumes | ✓ |
| Understand Anonymous Volumes | ✓ |
| Understand Bind Mounts | ✓ |
| Understand tmpfs Mounts | ✓ |
| Understand Persistent Storage | ✓ |
| Understand Volume Lifecycle | ✓ |
| Know Essential Storage Commands | ✓ |
| Understand Storage Best Practices | ✓ |
| Understand Read-Only Mounts | ✓ |
| Understand Volume Sharing | ✓ |
| Understand Backup Considerations | ✓ |
| Understand Storage Security | ✓ |
| Understand Common Storage Mistakes | ✓ |

---

# References

## Docker Documentation

- Docker Storage Documentation
- Docker Volumes Documentation
- Bind Mounts Documentation
- tmpfs Mount Documentation
- Docker CLI Documentation

---

## Linux Documentation

- Linux Filesystems
- OverlayFS Documentation
- tmpfs Documentation
- Linux Mount Documentation

---

## CNCF Resources

- Kubernetes Persistent Volumes Documentation
- Kubernetes Storage Classes
- Cloud Native Computing Foundation (CNCF)

---

## Security Resources

- NIST SP 800-190 — Application Container Security Guide
- OWASP Docker Security Cheat Sheet
- CIS Docker Benchmark
- OWASP Container Security Verification Standard

---

## Books

- *Docker Deep Dive* — Nigel Poulton
- *Docker in Action* — Jeff Nickoloff & Stephen Kuenzli
- *Container Security* — Liz Rice
- *Kubernetes in Action* — Marko Lukša

---

## Recommended Learning Resources

- Docker Official Documentation
- Docker Labs
- Play with Docker
- Linux Foundation Training
- CNCF Learning Paths
- NIST Computer Security Resource Center (CSRC)

