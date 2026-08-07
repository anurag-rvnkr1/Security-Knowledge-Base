# Chapter 30 – Volumes

## Overview

Containers are designed to be **ephemeral**.

This means that when a container is stopped, deleted, or recreated, any data stored inside its writable filesystem is **lost**.

Example:

```
Container

↓

Creates file

↓

/app/data.txt
```

Container crashes:

```
Container Deleted

↓

New Container Created
```

Result:

```
data.txt

↓

Lost
```

For stateless applications, this behavior is acceptable.

However, many applications require persistent or shared data, such as:

- Databases
- Log files
- Uploaded images
- Configuration files
- Machine learning models
- Shared application data

Kubernetes solves this problem using **Volumes**.

A Volume provides storage that exists independently of the lifecycle of an individual container.

> **A Volume belongs to the Pod, not to an individual container.**

---

# Learning Objectives

After completing this chapter, you will understand:

- What Volumes are
- Why Volumes are required
- Volume Architecture
- Volume Lifecycle
- Volume Mounts
- EmptyDir
- hostPath
- ConfigMap Volumes
- Secret Volumes
- Projected Volumes
- CSI Volumes
- Ephemeral Volumes
- Volume Sharing
- Best Practices

---

# Why Do We Need Volumes?

Suppose a container writes:

```
/var/log/app.log
```

Container crashes:

```
Container Deleted
```

Log file:

```
Lost
```

Application loses valuable information.

---

## Solution

Store the data inside a Volume.

```
Container

↓

Volume

↓

Data Persists
```

If the container restarts:

```
New Container

↓

Same Volume

↓

Data Available
```

---

# What is a Volume?

A **Volume** is a storage resource attached to a Pod.

Characteristics:

- Exists for the Pod lifetime
- Can be shared by multiple containers
- Mounted inside containers
- Supports different storage backends

---

# High-Level Architecture

```
                    Pod

        ┌────────────────────────────┐

        │                            │

        │  Container A               │

        │       │                    │

        │       ▼                    │

        │     Volume                 │

        │       ▲                    │

        │       │                    │

        │  Container B               │

        │                            │

        └────────────────────────────┘
```

Both containers access the same storage.

---

# Volume Lifecycle

Container lifecycle:

```
Container

↓

Restart

↓

Filesystem Lost
```

Volume lifecycle:

```
Pod

↓

Running

↓

Volume Exists
```

The Volume survives container restarts but is removed when the Pod is deleted (for most ephemeral volume types).

---

# Volume vs Container Filesystem

| Container Filesystem | Volume |
|----------------------|--------|
| Ephemeral | Separate storage |
| Lost after restart | Survives container restart |
| Private | Can be shared |
| Writable layer | Mounted storage |

---

# Volume Mount

Volumes become usable only after being mounted.

Example:

```
Volume

↓

Mounted

↓

/data
```

The application reads and writes files through the mount path.

---

# YAML Example

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: nginx-volume

spec:

  containers:

  - name: nginx

    image: nginx

    volumeMounts:

    - name: app-storage

      mountPath: /usr/share/nginx/html

  volumes:

  - name: app-storage

    emptyDir: {}
```

---

# YAML Breakdown

```
volumes

↓

Storage
```

```
volumeMounts

↓

Mount Storage

↓

Container
```

---

# Volume Workflow

```
Pod Created

↓

Volume Created

↓

Container Starts

↓

Volume Mounted

↓

Application Uses Storage
```

---

# Volume Types

Kubernetes supports many volume types.

Common ones include:

```
emptyDir
```

```
hostPath
```

```
ConfigMap
```

```
Secret
```

```
CSI
```

```
PersistentVolume
```

```
Projected
```

Each serves a different purpose.

---

# emptyDir Volume

Created when:

```
Pod Starts
```

Deleted when:

```
Pod Deleted
```

Characteristics:

- Temporary storage
- Shared by containers in the Pod
- Survives container restarts
- Does **not** survive Pod deletion

Example:

```
Pod

↓

emptyDir

↓

Container A

↓

Container B
```

Common use cases:

- Scratch space
- Temporary caches
- Intermediate processing
- Shared files between sidecars

---

# hostPath Volume

Uses a directory from the Worker Node.

Example:

```
Worker Node

↓

/var/log

↓

Mounted

↓

Pod
```

Advantages:

- Direct host access
- Useful for Node-level agents

Disadvantages:

- Tightly coupled to a specific Node
- Not portable
- Security risks if overused

Common use cases:

- Log collectors
- Monitoring agents
- Node diagnostics

---

# ConfigMap Volume

Stores configuration files.

Example:

```
ConfigMap

↓

Volume

↓

/etc/config
```

Application reads configuration without rebuilding the container image.

---

# Secret Volume

Stores sensitive information.

Example:

```
Secret

↓

Volume

↓

/etc/secret
```

Used for:

- Passwords
- API Keys
- Certificates
- Tokens

Secrets are mounted as files rather than embedded into the image.

---

# Projected Volume

Combines multiple sources into one mount.

Example:

```
ConfigMap

↓

Secret

↓

ServiceAccount Token

↓

Projected Volume
```

Applications access everything from one directory.

---

# CSI Volume

Provided through a **CSI Driver**.

Example:

```
AWS EBS

↓

CSI Driver

↓

Pod
```

Supports many storage providers including:

- AWS EBS
- Azure Disk
- Azure Files
- Google Persistent Disk
- Ceph
- NFS
- NetApp
- VMware vSphere

---

# Ephemeral CSI Volume

Temporary storage provided through a CSI driver.

Lifecycle:

```
Pod

↓

CSI Volume

↓

Pod Deleted

↓

Volume Deleted
```

Useful when advanced storage features are needed but persistence is not.

---

# Sharing Volumes

One Volume:

```
Volume

↓

Container A

↓

Container B

↓

Container C
```

All containers see the same files.

---

# Example

Sidecar logging pattern:

```
Application

↓

Writes Logs

↓

Volume

↓

Log Collector
```

Both containers share the same log directory.

---

# ReadOnly Mount

A volume can be mounted as read-only.

Example:

```yaml
volumeMounts:

- name: config

  mountPath: /etc/config

  readOnly: true
```

Ideal for:

- ConfigMaps
- Secrets
- Certificates

---

# Multiple Volumes

A Pod may mount several volumes.

Example:

```
Pod

↓

Logs Volume

↓

Config Volume

↓

Secret Volume

↓

Data Volume
```

Each serves a different purpose.

---

# Internal Architecture

```
Pod

↓

Volume

↓

Mount Point

↓

Container Filesystem

↓

Application
```

---

# Real-World Example

Microservice:

```
Application

↓

ConfigMap Volume

↓

Configuration
```

```
Application

↓

Secret Volume

↓

Credentials
```

```
Application

↓

Persistent Volume

↓

Database Files
```

```
Application

↓

emptyDir

↓

Temporary Cache
```

Multiple volume types often coexist in production Pods.

---

# View Pod

```bash
kubectl get pod
```

---

# Describe Pod

```bash
kubectl describe pod nginx-volume
```

Observe:

- Mounted volumes
- Mount paths
- Volume types

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f pod.yaml
```

View:

```bash
kubectl get pod
```

Describe:

```bash
kubectl describe pod nginx-volume
```

Delete:

```bash
kubectl delete pod nginx-volume
```

---

# Volume Architecture Summary

```
Pod

↓

Volume

↓

Mount

↓

Container

↓

Application
```

---

# Best Practices

### 1. Use the Right Volume Type

Choose storage based on the application's requirements.

---

### 2. Keep Secrets Separate

Never store credentials directly inside container images.

Use Secret volumes.

---

### 3. Use ConfigMaps for Configuration

Avoid hardcoding configuration into applications.

---

### 4. Minimize hostPath Usage

Use `hostPath` only when Node access is truly required.

---

### 5. Prefer Persistent Storage for Important Data

Use Persistent Volumes for:

- Databases
- User uploads
- Business-critical files

Avoid `emptyDir` for important data.

---

# Hands-on Lab 1 – Create an emptyDir Volume

Deploy a Pod using:

```yaml
emptyDir: {}
```

Create a file inside the mounted directory.

Restart the container (without deleting the Pod) and verify the file still exists.

---

# Hands-on Lab 2 – Share Data Between Containers

Create a Pod with:

- Application container
- Sidecar container

Mount the same `emptyDir` volume in both containers.

Verify that files written by one container are visible to the other.

---

# Hands-on Lab 3 – Mount a ConfigMap

Create a ConfigMap.

Mount it into:

```
/etc/config
```

Verify that configuration files appear inside the container.

---

# Hands-on Lab 4 – Mount a Secret

Create a Secret.

Mount it as a Volume.

Verify that sensitive data appears as files with appropriate permissions.

---

# Hands-on Lab 5 – Inspect Mounted Volumes

Inside the Pod:

```bash
df -h
```

and

```bash
mount
```

Observe mounted filesystems and storage paths.

---

# Common Mistakes

## 1. Confusing Volumes with Persistent Storage

Not all volumes are persistent.

Example:

```
emptyDir

↓

Deleted

↓

Pod Deleted
```

---

## 2. Storing Secrets in Images

Incorrect:

```
Docker Image

↓

Password
```

Correct:

```
Secret Volume
```

---

## 3. Overusing hostPath

`hostPath` tightly couples Pods to specific Nodes and can introduce security risks.

---

## 4. Assuming Container Restarts Delete Volume Data

Container restart:

```
Volume

↓

Still Exists
```

For Pod-scoped volumes such as `emptyDir`, data survives container restarts.

---

## 5. Forgetting Read-Only Mounts

Configuration and Secret volumes should often be mounted as:

```
readOnly: true
```

to reduce accidental modification.

---

# Quick Revision

## Workflow

```
Pod Created

↓

Volume Created

↓

Mounted

↓

Application Reads/Writes
```

---

## Common Volume Types

```
emptyDir

hostPath

ConfigMap

Secret

Projected

CSI

PersistentVolume
```

---

## Sharing

```
One Volume

↓

Multiple Containers
```

---

# Essential kubectl Commands

View Pods:

```bash
kubectl get pods
```

Describe Pod:

```bash
kubectl describe pod <pod-name>
```

Open Shell:

```bash
kubectl exec -it <pod-name> -- sh
```

View Mounted Filesystems:

```bash
df -h
```

View Mount Points:

```bash
mount
```

---

# Interview Questions

### Basic

- What is a Kubernetes Volume?
- Why are Volumes required?
- What is the difference between a container filesystem and a Volume?

---

### Intermediate

- Explain the lifecycle of an `emptyDir` volume.
- When should you use `hostPath`?
- How do ConfigMap and Secret volumes differ?

---

### Advanced

- Explain how multiple containers share a Volume.
- Compare `emptyDir`, `hostPath`, and CSI volumes.
- Why are Volumes attached to Pods instead of containers?
- How are Volume mounts implemented inside Linux containers?
- Which volume types are suitable for production databases?

---

# References

## Official Kubernetes Documentation

- Volumes
- ConfigMap
- Secret
- Projected Volumes
- Ephemeral Volumes

---

## CNCF Resources

- Kubernetes Storage Concepts
- CSI Documentation
- SIG Storage
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- NIST SP 800-190
- Kubernetes Storage Best Practices

---

## Recommended Practice

1. Create Pods using different volume types.
2. Compare container filesystem behavior with mounted volumes.
3. Share files between multiple containers using `emptyDir`.
4. Mount ConfigMaps and Secrets into applications.
5. Inspect mounted filesystems inside running Pods.
6. Experiment with read-only mounts.
7. Prepare for Persistent Volumes (PV) by understanding Pod-scoped versus cluster-scoped storage.

---

# Chapter Summary

```
Application

↓

Container

↓

Volume Mount

↓

Volume

↓

Storage Backend
```

Kubernetes **Volumes** provide storage that is independent of an individual container's writable layer. By attaching storage to the **Pod** rather than the container, Kubernetes enables data sharing, configuration management, secret injection, temporary storage, and integration with persistent storage systems. Choosing the correct volume type is essential for building reliable, secure, and production-ready applications.

---

## Next Chapter

**Chapter 31 – Persistent Volumes (PV)**

Topics include:

- What is a Persistent Volume?
- Persistent Storage Architecture
- Static Provisioning
- PV Lifecycle
- Access Modes
- Reclaim Policies
- Storage Capacity
- Binding Process
- Production Use Cases
- Hands-on Labs
- Interview Questions

---