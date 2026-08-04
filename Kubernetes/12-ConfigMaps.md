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

# How ConfigMaps Work Internally

## Overview

A ConfigMap is much more than a simple collection of key-value pairs.

Internally, Kubernetes stores ConfigMaps as API objects inside **etcd**, and Pods retrieve their configuration through the **API Server**.

Depending on how the ConfigMap is used, Kubernetes injects the configuration into the container as:

- Environment Variables
- Mounted Files
- Command-Line Arguments

Understanding this internal workflow is essential for troubleshooting configuration-related issues in production clusters.

---

# High-Level Architecture

```
                 ConfigMap

                     │

               API Server

                     │

                  etcd

                     │

        ┌────────────┼────────────┐

        ▼            ▼            ▼

 Environment      Volume       Arguments

 Variables        Mount

                     │

                     ▼

               Running Container
```

---

# Complete Workflow

Suppose a ConfigMap is created.

```
Developer

↓

kubectl apply

↓

API Server

↓

Validation

↓

Store in etcd

↓

Pod Requests ConfigMap

↓

kubelet

↓

Container Runtime

↓

Application
```

---

# Step 1 – Create ConfigMap

Example:

```yaml
apiVersion: v1

kind: ConfigMap

metadata:

  name: app-config

data:

  APP_ENV: production

  LOG_LEVEL: INFO
```

Deploy:

```bash
kubectl apply -f configmap.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates the request
- Authorizes the request
- Validates the ConfigMap
- Stores it in etcd

Workflow:

```
kubectl

↓

API Server

↓

ConfigMap Stored
```

---

# Step 3 – etcd Storage

Internally:

```
etcd

↓

ConfigMap

↓

Key

↓

Value
```

Example:

```
APP_ENV

↓

production
```

---

# Step 4 – Pod Creation

Suppose a Pod references:

```yaml
configMapRef:

  name: app-config
```

Workflow:

```
Pod Created

↓

API Server

↓

ConfigMap Lookup
```

---

# Step 5 – kubelet

Worker node:

```
API Server

↓

kubelet

↓

Fetch ConfigMap
```

kubelet retrieves the ConfigMap before starting the container.

---

# Step 6 – Container Startup

Depending on configuration:

```
ConfigMap

↓

Environment Variables
```

or

```
ConfigMap

↓

Mounted Files
```

Both methods are supported.

---

# Environment Variable Flow

```
ConfigMap

↓

kubelet

↓

Container Runtime

↓

Environment Variables

↓

Application
```

Example:

```
APP_ENV=production

LOG_LEVEL=INFO
```

The values are available immediately when the container starts.

---

# Volume Mount Flow

```
ConfigMap

↓

Volume

↓

Files

↓

Container

↓

Application
```

Each key becomes a file.

---

# Example

ConfigMap:

```
APP_ENV

↓

production
```

Mounted:

```
/etc/config/

↓

APP_ENV
```

Contents:

```
production
```

---

# Multiple Keys

ConfigMap:

```
DATABASE_HOST

↓

LOG_LEVEL

↓

API_URL
```

Mounted directory:

```
/etc/config/

├── DATABASE_HOST

├── LOG_LEVEL

└── API_URL
```

Each file contains the corresponding value.

---

# ConfigMap Sharing

A single ConfigMap can be used by many Pods.

```
ConfigMap

↓

Pod A

↓

Pod B

↓

Pod C
```

This promotes consistent configuration across replicas.

---

# Namespace Scope

ConfigMaps are Namespace-scoped.

Example:

```
development

↓

app-config
```

```
production

↓

app-config
```

These are separate ConfigMaps.

---

# ConfigMap Lookup

Suppose:

```
Pod

↓

Namespace

↓

development
```

ConfigMap:

```
production/app-config
```

Result:

```
Not Found
```

Pods can only reference ConfigMaps in the **same Namespace**.

---

# ConfigMap Update

Modify:

```bash
kubectl edit configmap app-config
```

Updated:

```
API Server

↓

etcd

↓

New Values
```

What happens next depends on how the ConfigMap is consumed.

---

# Environment Variable Updates

Suppose:

```
ConfigMap Updated
```

Container:

```
Environment Variables
```

Result:

```
No Change
```

Environment variables are read when the container starts.

To use updated values:

```
Restart Pod
```

or recreate the Pod through the controller.

---

# Volume Updates

Mounted ConfigMaps behave differently.

```
ConfigMap Updated

↓

kubelet Detects Change

↓

Mounted Files Updated
```

Kubernetes periodically refreshes projected ConfigMap volumes.

> **Important:** The application itself must reread the updated file if it does not automatically monitor configuration changes.

---

# Immutable ConfigMaps

Large production clusters can mark ConfigMaps as immutable.

Example:

```yaml
immutable: true
```

Benefits:

- Better API Server performance
- Prevents accidental modifications
- Reduced watch overhead

To change an immutable ConfigMap:

```
Delete

↓

Create New
```

---

# Internal Architecture

```
Developer

↓

ConfigMap

↓

API Server

↓

etcd

↓

kubelet

↓

Container

↓

Application
```

---

# ConfigMap Access Modes

```
ConfigMap

│

├── Environment Variables

├── Volume Mount

└── Command Arguments
```

Each approach has different operational characteristics.

---

# Command-Line Arguments

Example:

```yaml
args:

- "--environment=$(APP_ENV)"
```

Combined with:

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

Container Argument

↓

Application
```

---

# Failure Scenario

Suppose:

```
Pod

↓

ConfigMap

↓

Not Found
```

Result:

```
Container

↓

Cannot Start
```

The Pod may remain in a waiting state until the referenced ConfigMap exists (or fail if the reference is mandatory).

---

# Hands-on Lab 1 – Create ConfigMap

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production \
--from-literal=LOG_LEVEL=INFO
```

Verify:

```bash
kubectl get cm
```

---

# Hands-on Lab 2 – Use Environment Variables

Create a Pod:

```yaml
envFrom:

- configMapRef:

    name: app-config
```

Deploy:

```bash
kubectl apply -f pod.yaml
```

Verify:

```bash
kubectl exec -it <pod-name> -- printenv
```

Observe:

```
APP_ENV

LOG_LEVEL
```

---

# Hands-on Lab 3 – Mount as Volume

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

- mountPath: /etc/config

  name: config
```

Verify:

```bash
kubectl exec -it <pod-name> -- ls /etc/config
```

Read a file:

```bash
kubectl exec -it <pod-name> -- cat /etc/config/APP_ENV
```

---

# Hands-on Lab 4 – Update ConfigMap

Edit:

```bash
kubectl edit configmap app-config
```

Observe:

- Mounted files may update automatically after a short delay.
- Environment variables remain unchanged until the Pod is restarted.

---

# Hands-on Lab 5 – Immutable ConfigMap

Example:

```yaml
immutable: true
```

Apply:

```bash
kubectl apply -f configmap.yaml
```

Attempt:

```bash
kubectl edit configmap app-config
```

Expected:

```
Rejected

↓

Immutable
```

---

# Common Mistakes

## 1. Storing Passwords

Incorrect:

```
ConfigMap

↓

Database Password
```

Correct:

```
Secret
```

---

## 2. Expecting Environment Variables to Update Automatically

```
ConfigMap Updated

↓

Container Environment

↓

Unchanged
```

Restart the Pod to load updated environment variables.

---

## 3. Assuming Volume Updates Restart the Application

Kubernetes updates mounted files.

It does **not** restart the application or force it to reload configuration.

---

## 4. Sharing One Large ConfigMap

Avoid:

```
One ConfigMap

↓

Entire Company
```

Prefer:

```
One Application

↓

One ConfigMap
```

This improves maintainability.

---

## 5. Hardcoding Configuration

Incorrect:

```
Container Image

↓

Database Host
```

Correct:

```
Container Image

↓

ConfigMap
```

---

# ConfigMaps Quick Revision

## Architecture

```
ConfigMap

↓

API Server

↓

etcd

↓

kubelet

↓

Container

↓

Application
```

---

## Access Methods

```
ConfigMap

├── Environment Variables

├── Mounted Files

└── Command Arguments
```

---

## Update Behavior

```
Environment Variables

↓

Restart Required
```

```
Mounted Files

↓

Automatically Refreshed

↓

Application Must Reload If Needed
```

---

# Essential kubectl Commands

Create:

```bash
kubectl create configmap app-config \
--from-literal=APP_ENV=production
```

View:

```bash
kubectl get cm
```

Describe:

```bash
kubectl describe configmap app-config
```

View YAML:

```bash
kubectl get cm app-config -o yaml
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

# Interview Questions

### Basic

- What is a ConfigMap?
- Why should ConfigMaps be used?
- What type of data belongs in a ConfigMap?

---

### Intermediate

- What are the ways to consume a ConfigMap?
- How are ConfigMaps mounted as volumes?
- What happens when a ConfigMap is updated?

---

### Advanced

- Why don't environment variables update automatically?
- How does kubelet keep mounted ConfigMaps up to date?
- What is an immutable ConfigMap?
- Why are ConfigMaps Namespace-scoped?
- When should ConfigMaps be preferred over rebuilding container images?

---

# References

## Official Kubernetes Documentation

- ConfigMaps
- Inject Data into Applications
- Volumes
- Environment Variables
- Immutable ConfigMaps

---

## CNCF Resources

- Kubernetes Best Practices
- Kubernetes Configuration Management
- Cloud Native Computing Foundation (CNCF)

---

## Security & Operations

- CIS Kubernetes Benchmark
- NIST SP 800-190
- Kubernetes Production Best Practices
- OWASP Kubernetes Top 10

---

## Recommended Practice

1. Create ConfigMaps using YAML, literals, files, and directories.
2. Consume ConfigMaps through environment variables and volume mounts.
3. Compare update behavior between environment variables and mounted files.
4. Create an immutable ConfigMap and observe update restrictions.
5. Share one ConfigMap across multiple Pods.
6. Inspect ConfigMap objects using `kubectl describe` and `kubectl get -o yaml`.
7. Practice troubleshooting Pods with missing ConfigMap references.

---

# Chapter Summary

```
Developer

↓

ConfigMap

↓

API Server

↓

etcd

↓

kubelet

↓

Environment Variables

or

Mounted Files

↓

Application
```

ConfigMaps provide a **declarative, reusable, and centralized configuration mechanism** for Kubernetes applications. By separating configuration from container images, they enable environment-specific deployments, easier updates, and better adherence to cloud-native application design principles.

---
