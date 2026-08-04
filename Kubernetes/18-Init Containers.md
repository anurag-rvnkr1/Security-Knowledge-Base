# Chapter 18 – Init Containers

## Overview

An **Init Container** is a special type of container that **runs before the main application container starts**.

Unlike regular containers:

- Init Containers run **only once**
- They execute **sequentially**
- Each Init Container **must complete successfully**
- The application container starts **only after all Init Containers finish**

Init Containers are commonly used for:

- Waiting for dependencies
- Database initialization
- Configuration generation
- Environment validation
- Downloading files
- Setting file permissions
- Creating directories
- Running initialization scripts

---

# Learning Objectives

After completing this chapter, you will understand:

- What an Init Container is
- Why Init Containers are needed
- Init Container Architecture
- Init Container Lifecycle
- Sequential Execution
- Shared Volumes
- Failure Handling
- Restart Behavior
- Common Use Cases
- Best Practices

---

# Why Init Containers?

Imagine an application.

```
Application

↓

Starts

↓

Database Not Ready

↓

Connection Failed
```

The application crashes because its dependency is unavailable.

---

# Another Example

```
Application

↓

Needs Configuration File

↓

File Missing

↓

Startup Failed
```

Again:

```
Application

↓

Crash
```

---

# Solution

Use Init Containers.

```
Init Container

↓

Wait for Database

↓

Generate Configuration

↓

Success

↓

Application Starts
```

---

# What is an Init Container?

An Init Container is a container that performs initialization tasks before the application begins.

```
Pod

↓

Init Container

↓

Complete

↓

Application Container

↓

Running
```

---

# Pod Architecture

```
                    Pod

                     │

          ┌──────────┴──────────┐

          ▼                     ▼

   Init Container        App Container

     Executes              Waits

          │

          ▼

     Successful?

          │

         Yes

          ▼

   Application Starts
```

---

# Init Container Characteristics

Init Containers:

- Run before application containers
- Execute sequentially
- Must complete successfully
- Cannot serve application traffic
- Exit after completion

---

# Init Container vs Regular Container

| Init Container | Regular Container |
|---------------|-------------------|
| Runs before app | Runs application |
| Executes once | Runs continuously |
| Sequential execution | Parallel execution |
| Must finish successfully | Handles requests |
| Initialization tasks | Business logic |

---

# Multiple Init Containers

Pods can contain multiple Init Containers.

Execution order:

```
Init Container 1

↓

Complete

↓

Init Container 2

↓

Complete

↓

Init Container 3

↓

Complete

↓

Application Starts
```

Each Init Container waits for the previous one to finish.

---

# Init Container Workflow

```
Create Pod

↓

Init Container 1

↓

Success

↓

Init Container 2

↓

Success

↓

Application Container

↓

Running
```

---

# Init Container YAML

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: init-demo

spec:

  initContainers:

  - name: wait-db

    image: busybox

    command:

    - sh

    - -c

    - echo "Waiting for Database"

  containers:

  - name: app

    image: nginx
```

---

# YAML Structure

```
Pod

↓

Init Containers

↓

Containers

↓

Volumes
```

Notice:

```
initContainers

↓

Separate Section
```

---

# Execution Sequence

```
Pod Created

↓

Init Container

↓

Exit Code 0

↓

Application Starts
```

---

# Failure Handling

Suppose:

```
Init Container

↓

Exit Code 1
```

Result:

```
Application

↓

Never Starts
```

The Pod remains in the initialization phase until the Init Container succeeds.

---

# Restart Behavior

If an Init Container fails:

```
Restart

↓

Retry

↓

Success?

↓

Yes

↓

Continue
```

The retry behavior follows the Pod's `restartPolicy`.

---

# Pod Status

During initialization:

```bash
kubectl get pods
```

Example:

```
Init:0/2
```

Meaning:

```
0

↓

Completed

↓

Out of

↓

2 Init Containers
```

Later:

```
Init:1/2
```

Finally:

```
Running
```

---

# Viewing Init Container Logs

```bash
kubectl logs pod-name \
-c wait-db
```

Specify:

```
-c

↓

Container Name
```

---

# Shared Volumes

Init Containers commonly prepare data.

Architecture:

```
Init Container

↓

Shared Volume

↓

Application Container
```

---

# Example

Init Container:

```
Download Configuration

↓

Shared Volume
```

Application:

```
Read Configuration

↓

Start
```

---

# File Permission Example

Init Container:

```
chmod

↓

Shared Volume
```

Application:

```
Read Files

↓

Success
```

---

# Download Example

```
Init Container

↓

Download Data

↓

Shared Volume

↓

Application
```

The application starts only after the required files exist.

---

# Wait for Database Example

```
Init Container

↓

Check Database

↓

Available?

↓

Yes

↓

Start Application
```

---

# DNS Check Example

```
Init Container

↓

Resolve DNS

↓

Success

↓

Application Starts
```

---

# Migration Example

```
Init Container

↓

Database Migration

↓

Complete

↓

Application Starts
```

---

# Common Use Cases

## Database Readiness

```
Init

↓

Wait

↓

Database Ready
```

---

## Configuration Generation

```
Template

↓

Generate Config

↓

Application
```

---

## Download Files

```
Internet

↓

Download

↓

Volume
```

---

## Directory Creation

```
Init

↓

mkdir

↓

Shared Volume
```

---

## Secret Validation

```
Init

↓

Check Secrets

↓

Start App
```

---

# Viewing Init Containers

Describe Pod:

```bash
kubectl describe pod init-demo
```

Observe:

```
Init Containers
```

section.

---

# Important kubectl Commands

Create:

```bash
kubectl apply -f pod.yaml
```

View:

```bash
kubectl get pods
```

Describe:

```bash
kubectl describe pod init-demo
```

Logs:

```bash
kubectl logs init-demo \
-c wait-db
```

Delete:

```bash
kubectl delete pod init-demo
```

---

# Init Container Lifecycle

```
Create Pod

↓

Init Container 1

↓

Complete

↓

Init Container 2

↓

Complete

↓

Application Starts

↓

Running
```

---

# Init Container Architecture Summary

```
Pod

↓

Init Containers

↓

Shared Volume

↓

Application Container
```

---

# Best Practices

### 1. Keep Init Containers Small

They should perform only initialization tasks.

---

### 2. Separate Initialization Logic

Avoid embedding initialization scripts inside the main application container.

---

### 3. Use Shared Volumes

Exchange files between Init Containers and application containers using shared volumes.

---

### 4. Monitor Initialization Failures

Inspect Init Container logs whenever a Pod remains in the `Init` state.

---

### 5. Make Initialization Idempotent

Initialization scripts should safely handle repeated execution because they may be retried after failures.

---

## Next Section

How Init Containers Work Internally

Init Container Scheduling

Shared Volumes

Restart Behavior

Hands-on Labs

Common Mistakes

Quick Revision

References

---