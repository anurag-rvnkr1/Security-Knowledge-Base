# Chapter 12 – ConfigMaps

## Overview

A **ConfigMap** is a Kubernetes object used to store **non-sensitive configuration data** separately from application code and container images.

Instead of hardcoding configuration values inside an application or rebuilding container images whenever configuration changes, Kubernetes allows applications to read configuration from ConfigMaps.

Examples of configuration include:

- Application settings
- Environment variables
- Configuration files
- Feature flags
- Logging configuration
- Database hostnames
- API URLs
- Port numbers

> **Important:** ConfigMaps are **not encrypted** and should **never** be used to store passwords, API keys, tokens, certificates, or other confidential information. Use **Secrets** for sensitive data.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a ConfigMap is
- Why ConfigMaps are needed
- ConfigMap Architecture
- Creating ConfigMaps
- Using ConfigMaps
- ConfigMaps as Environment Variables
- ConfigMaps as Volumes
- ConfigMaps from Files
- Updating ConfigMaps
- ConfigMap Limitations
- Best Practices

---

# Why ConfigMaps?

Imagine an application.

```
Application

↓

Database Host

↓

db.company.local

↓

Hardcoded
```

Later:

```
Database Changed

↓

Need New Image

↓

Redeploy
```

Every configuration change requires rebuilding the application image.

This violates one of the principles of cloud-native application design.

---

# Better Solution

Separate:

```
Application Code

↓

Container Image
```

from

```
Configuration

↓

ConfigMap
```

Now configuration can change independently of the application image.

---

# What is a ConfigMap?

A ConfigMap is a Kubernetes API object that stores configuration as **key-value pairs**.

Example:

```
ConfigMap

│

├── APP_ENV

│     production

│

├── LOG_LEVEL

│     INFO

│

└── API_URL

      https://api.company.com
```

Applications consume these values at runtime.

---

# ConfigMap Architecture

```
                ConfigMap

                     │

        ┌────────────┼────────────┐

        ▼            ▼            ▼

 Environment      Volume      Command Line

 Variables         Mount        Arguments

                     │

                     ▼

               Application
```

A ConfigMap can be consumed in multiple ways.

---

# Why Separate Configuration?

Following the **Twelve-Factor App** methodology:

```
Application

↓

Code

↓

Configuration

↓

Separate
```

Benefits:

- Easier deployments
- Environment-specific configuration
- Reusable container images
- Simpler maintenance

---

# ConfigMap Structure

```yaml
apiVersion: v1

kind: ConfigMap

metadata:

  name: app-config

data:

  APP_ENV: production

  LOG_LEVEL: INFO

  API_URL: https://api.company.com
```

---

# YAML Breakdown

```
ConfigMap

↓

Metadata

↓

Data

↓

Key-Value Pairs
```

---

# Creating a ConfigMap

Apply:

```bash
kubectl apply -f configmap.yaml
```

Verify:

```bash
kubectl get configmaps
```

or

```bash
kubectl get cm
```

---

# Viewing ConfigMaps

List:

```bash
kubectl get configmaps
```

Describe:

```bash
kubectl describe configmap app-config
```

View YAML:

```bash
kubectl get configmap app-config \
-o yaml
```

---

# Creating from Command Line

Single key:

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production
```

Multiple keys:

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production \
--from-literal=LOG_LEVEL=INFO
```

---

# Creating from a File

Suppose:

```
application.properties
```

Command:

```bash
kubectl create configmap app-config \
--from-file=application.properties
```

The file becomes part of the ConfigMap.

---

# Creating from a Directory

Suppose:

```
config/

├── app.conf

├── logging.conf

└── database.conf
```

Command:

```bash
kubectl create configmap app-config \
--from-file=config/
```

Each file becomes a separate key.

---

# Using ConfigMaps as Environment Variables

Example:

```yaml
env:

- name: APP_ENV

  valueFrom:

    configMapKeyRef:

      name: app-config

      key: APP_ENV
```

Workflow:

```
ConfigMap

↓

Environment Variable

↓

Container
```

---

# Importing All Keys

Instead of referencing keys individually:

```yaml
envFrom:

- configMapRef:

    name: app-config
```

All keys become environment variables.

---

# Environment Variable Example

ConfigMap:

```
APP_ENV=production

LOG_LEVEL=INFO
```

Container:

```
printenv
```

Output:

```
APP_ENV=production

LOG_LEVEL=INFO
```

---

# Using ConfigMaps as Volumes

A ConfigMap can also be mounted as files.

Example:

```yaml
volumes:

- name: config

  configMap:

    name: app-config
```

Mount:

```yaml
volumeMounts:

- name: config

  mountPath: /etc/config
```

---

# Volume Architecture

```
ConfigMap

↓

Volume

↓

Container

↓

/etc/config
```

Each key becomes a file.

---

# Mounted Files

Example ConfigMap:

```
APP_ENV

LOG_LEVEL
```

Mounted directory:

```
/etc/config/

├── APP_ENV

└── LOG_LEVEL
```

Each file contains the corresponding value.

---

# ConfigMaps and Multiple Pods

One ConfigMap can be shared.

```
ConfigMap

↓

Pod A

↓

Pod B

↓

Pod C
```

This ensures consistent configuration.

---

# ConfigMap Lifecycle

```
Create

↓

Store Configuration

↓

Mount / Inject

↓

Application Reads

↓

Update

↓

Delete
```

---

# ConfigMap Scope

ConfigMaps are **Namespace-scoped**.

Example:

```
Development

↓

ConfigMap A
```

```
Production

↓

ConfigMap B
```

Each Namespace has its own ConfigMaps.

---

# Updating a ConfigMap

Modify:

```bash
kubectl edit configmap app-config
```

or

```bash
kubectl apply -f configmap.yaml
```

> **Note:** Whether applications immediately observe updated values depends on **how the ConfigMap is consumed**. This topic is covered later in the chapter.

---

# ConfigMap Limitations

ConfigMaps are intended for configuration, not large datasets.

General considerations:

- Store configuration only
- Avoid binary files
- Avoid sensitive data
- Keep ConfigMaps reasonably sized
- Use PersistentVolumes for large files

---

# ConfigMaps vs Secrets

| ConfigMap | Secret |
|------------|---------|
| Non-sensitive data | Sensitive data |
| Plain configuration | Passwords, Tokens, Certificates |
| Stored as regular configuration | Designed for confidential information |
| Used for application settings | Used for credentials |

---

# Common Use Cases

ConfigMaps commonly store:

- Application configuration
- Database hostnames
- Feature flags
- Logging levels
- API endpoints
- Time zones
- Port numbers
- Application properties
- NGINX configuration
- Spring Boot configuration

---

# Important kubectl Commands

Create:

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production
```

View:

```bash
kubectl get configmaps
```

Describe:

```bash
kubectl describe configmap app-config
```

YAML:

```bash
kubectl get configmap app-config \
-o yaml
```

Edit:

```bash
kubectl edit configmap app-config
```

Delete:

```bash
kubectl delete configmap app-config
```

---

# ConfigMap Architecture Summary

```
ConfigMap

↓

Environment Variables

↓

Volumes

↓

Application
```

---

# Best Practices

### 1. Keep Configuration Outside Container Images

Build once, configure at deployment time.

---

### 2. Store Only Non-Sensitive Data

Passwords and API keys belong in **Secrets**.

---

### 3. Organize ConfigMaps by Application

Example:

```
frontend-config

backend-config

nginx-config
```

Avoid one large ConfigMap for unrelated applications.

---

### 4. Use Environment Variables for Simple Settings

Examples:

- Port numbers
- Feature flags
- Environment names

---

### 5. Use Volume Mounts for Configuration Files

Examples:

- `nginx.conf`
- `application.properties`
- `config.yaml`
- `prometheus.yml`

---

