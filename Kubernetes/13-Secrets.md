# Chapter 13 – Secrets

## Overview

A **Secret** is a Kubernetes object used to store **sensitive information** securely.

Unlike ConfigMaps, which store general configuration, Secrets are designed for confidential data such as:

- Passwords
- API Keys
- Database Credentials
- OAuth Tokens
- TLS Certificates
- SSH Keys
- Private Keys
- Access Tokens
- Docker Registry Credentials

Secrets allow applications to access sensitive information **without embedding credentials inside container images or application code**.

> **Important:** By default, Secret values are **Base64-encoded**, **not encrypted**. For production environments, enable **Encryption at Rest** in etcd and implement strict RBAC policies.

---

# Learning Objectives

After completing this chapter, you will understand:

- What a Secret is
- Why Secrets are needed
- Secret Architecture
- Secret Types
- Creating Secrets
- Using Secrets
- Secrets as Environment Variables
- Secrets as Volumes
- Docker Registry Secrets
- TLS Secrets
- Best Practices

---

# Why Secrets?

Imagine an application.

```
Application

↓

Database Password

↓

Hardcoded
```

Problems:

- Password visible in source code
- Password stored in Git
- Password embedded in container image
- Difficult credential rotation

---

# Better Solution

Separate:

```
Application

↓

Code
```

from

```
Sensitive Data

↓

Secret
```

Now credentials can be updated independently.

---

# What is a Secret?

A Secret is a Kubernetes API object that stores sensitive key-value data.

Example:

```
Secret

│

├── username

│     admin

│

├── password

│     ********

│

└── api-key

      ********
```

Applications retrieve these values securely at runtime.

---

# Secret Architecture

```
                 Secret

                    │

        ┌───────────┼────────────┐

        ▼           ▼            ▼

 Environment     Volume      Image Pull

 Variables       Mount       Credentials

                    │

                    ▼

               Application
```

---

# ConfigMap vs Secret

| ConfigMap | Secret |
|------------|---------|
| Non-sensitive data | Sensitive data |
| Application configuration | Passwords & Tokens |
| Logging levels | API Keys |
| Feature flags | Certificates |
| Database hostnames | Private Keys |

---

# Secret Types

Kubernetes supports several Secret types.

```
Secrets

│

├── Opaque

├── kubernetes.io/tls

├── kubernetes.io/dockerconfigjson

├── kubernetes.io/basic-auth

├── kubernetes.io/ssh-auth

└── kubernetes.io/service-account-token
```

---

# 1. Opaque Secret

The default Secret type.

Example:

```yaml
type: Opaque
```

Stores arbitrary key-value data.

---

# 2. TLS Secret

Used for:

- HTTPS
- TLS Certificates
- Ingress Controllers

Contains:

```
tls.crt

tls.key
```

---

# 3. Docker Registry Secret

Stores credentials for pulling private container images.

Example:

```
Docker Hub

↓

Username

↓

Password

↓

Secret
```

---

# 4. Basic Authentication Secret

Stores:

```
Username

↓

Password
```

---

# 5. SSH Authentication Secret

Stores:

```
Private Key

↓

SSH Authentication
```

---

# Secret Structure

Example:

```yaml
apiVersion: v1

kind: Secret

metadata:

  name: database-secret

type: Opaque

data:

  username: YWRtaW4=

  password: U2VjdXJlUGFzcw==
```

> Values under `data` must be Base64-encoded.

---

# Secret YAML Breakdown

```
Secret

↓

Metadata

↓

Type

↓

Data
```

---

# Creating Secrets

Apply:

```bash
kubectl apply -f secret.yaml
```

Verify:

```bash
kubectl get secrets
```

---

# Creating from Command Line

```bash
kubectl create secret generic database-secret \
--from-literal=username=admin \
--from-literal=password=SecurePass123
```

---

# Creating from File

Example:

```bash
kubectl create secret generic app-secret \
--from-file=config.txt
```

---

# Creating TLS Secret

```bash
kubectl create secret tls tls-secret \
--cert=tls.crt \
--key=tls.key
```

---

# Viewing Secrets

List:

```bash
kubectl get secrets
```

Describe:

```bash
kubectl describe secret database-secret
```

View YAML:

```bash
kubectl get secret database-secret \
-o yaml
```

---

# Decoding Secret Values

View Base64 value:

```bash
kubectl get secret database-secret \
-o yaml
```

Decode:

```bash
echo "YWRtaW4=" | base64 --decode
```

Output:

```
admin
```

> Base64 encoding is **not** encryption. Anyone with permission to read the Secret can decode it.

---

# Using Secrets as Environment Variables

Example:

```yaml
env:

- name: DB_PASSWORD

  valueFrom:

    secretKeyRef:

      name: database-secret

      key: password
```

Workflow:

```
Secret

↓

Environment Variable

↓

Container
```

---

# Importing All Secret Keys

```yaml
envFrom:

- secretRef:

    name: database-secret
```

Every key becomes an environment variable.

---

# Using Secrets as Volumes

Volume:

```yaml
volumes:

- name: secrets

  secret:

    secretName: database-secret
```

Mount:

```yaml
volumeMounts:

- name: secrets

  mountPath: /etc/secrets
```

---

# Volume Architecture

```
Secret

↓

Volume

↓

Container

↓

/etc/secrets
```

Each Secret key becomes a file.

---

# Mounted Secret Files

Secret:

```
username

password
```

Container:

```
/etc/secrets/

├── username

└── password
```

Applications can read these files.

---

# Docker Registry Secret

Create:

```bash
kubectl create secret docker-registry regcred \
--docker-server=<registry> \
--docker-username=<username> \
--docker-password=<password>
```

Use:

```yaml
imagePullSecrets:

- name: regcred
```

---

# Secret Lifecycle

```
Create

↓

API Server

↓

etcd

↓

Pod References Secret

↓

kubelet

↓

Application
```

---

# Namespace Scope

Secrets are Namespace-scoped.

Example:

```
development

↓

database-secret
```

```
production

↓

database-secret
```

These are independent Secrets.

---

# Secret Size

Secrets are designed for relatively small pieces of sensitive information.

Large files or backups should be stored using more appropriate storage solutions rather than Secrets.

---

# Important kubectl Commands

Create:

```bash
kubectl create secret generic app-secret \
--from-literal=password=Secure123
```

View:

```bash
kubectl get secrets
```

Describe:

```bash
kubectl describe secret app-secret
```

YAML:

```bash
kubectl get secret app-secret \
-o yaml
```

Delete:

```bash
kubectl delete secret app-secret
```

---

# Secret Architecture Summary

```
Secret

↓

API Server

↓

etcd

↓

Environment Variables

or

Volumes

↓

Application
```

---

# Best Practices

### 1. Never Store Passwords in ConfigMaps

Sensitive information belongs in Secrets.

---

### 2. Enable Encryption at Rest

Protect Secrets stored in etcd by enabling Kubernetes Encryption at Rest.

---

### 3. Apply Least-Privilege RBAC

Only authorized users and workloads should be able to read Secrets.

---

### 4. Rotate Secrets Regularly

Update passwords, tokens, and certificates on a regular schedule and after suspected compromise.

---

### 5. Avoid Logging Secret Values

Applications should never print credentials or tokens to logs.

---

# How Secrets Work Internally

## Overview

Secrets are one of the most security-critical resources in Kubernetes.

Although they appear similar to ConfigMaps, Kubernetes treats Secrets differently in several important ways:

- Access is controlled through RBAC
- Secrets are distributed only to Nodes that need them
- kubelet caches Secrets locally
- Secret values are never exposed unless explicitly requested
- Secrets can be mounted securely into running Pods

Understanding the internal workflow helps administrators troubleshoot authentication issues, design secure workloads, and implement production-grade security.

---

# High-Level Architecture

```
                 Secret

                    │

               API Server

                    │

                  etcd

                    │

                 kubelet

                    │

        ┌───────────┼────────────┐

        ▼           ▼            ▼

 Environment     Volume      Image Pull

 Variables       Mount       Secrets

                    │

                    ▼

               Application
```

---

# Complete Secret Workflow

```
Developer

↓

kubectl apply

↓

API Server

↓

Authentication

↓

Authorization

↓

Validation

↓

Store Secret

↓

etcd

↓

Pod Requests Secret

↓

kubelet

↓

Container Runtime

↓

Application
```

---

# Step 1 – Secret Creation

Example:

```yaml
apiVersion: v1

kind: Secret

metadata:

  name: db-secret

type: Opaque

stringData:

  username: admin

  password: SecurePass123
```

> **Note:** When creating Secrets manually, `stringData` is often easier to use than `data`. Kubernetes automatically converts `stringData` values into Base64-encoded values stored under `data`.

Deploy:

```bash
kubectl apply -f secret.yaml
```

---

# Step 2 – API Server

The API Server:

- Authenticates user
- Authorizes request
- Validates Secret
- Stores Secret

Workflow:

```
kubectl

↓

API Server

↓

Secret Accepted
```

---

# Step 3 – Storage in etcd

Internally:

```
API Server

↓

etcd

↓

Secret Object
```

Unless **Encryption at Rest** is enabled:

```
Secret

↓

Base64 Encoded

↓

Stored
```

Remember:

```
Base64

≠

Encryption
```

---

# Step 4 – Pod References Secret

Example:

```yaml
secretKeyRef:

  name: db-secret

  key: password
```

Workflow:

```
Pod

↓

Secret Reference
```

The Pod stores only a **reference**, not the secret value itself.

---

# Step 5 – kubelet Retrieves Secret

Worker Node:

```
API Server

↓

kubelet

↓

Fetch Secret
```

Only the Node hosting the Pod retrieves the Secret.

This reduces unnecessary distribution across the cluster.

---

# Step 6 – Container Startup

Depending on configuration:

```
Secret

↓

Environment Variables
```

or

```
Secret

↓

Mounted Files
```

---

# Environment Variable Flow

```
Secret

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
DB_USER

↓

admin

DB_PASSWORD

↓

********
```

The variables are available when the container starts.

---

# Volume Mount Flow

```
Secret

↓

Volume

↓

Files

↓

Container
```

Example:

```
/etc/secrets/

├── username

└── password
```

Applications read the files directly.

---

# Secret Files

Example:

```
/etc/secrets/password
```

Contents:

```
SecurePass123
```

The application reads the file instead of an environment variable.

---

# Secret Distribution

Suppose:

```
Cluster

↓

10 Nodes
```

Pod runs only on:

```
Node 3
```

Result:

```
Secret

↓

Node 3 Only
```

The Secret is not proactively copied to every Node.

---

# Secret Cache

kubelet maintains a temporary cache.

```
API Server

↓

kubelet Cache

↓

Container
```

Benefits:

- Reduced API traffic
- Faster Pod startup
- Lower API Server load

---

# Secret Update

Modify:

```bash
kubectl edit secret db-secret
```

Workflow:

```
API Server

↓

etcd

↓

Updated Secret
```

How the application observes the update depends on how the Secret is consumed.

---

# Environment Variable Updates

```
Secret Updated

↓

Environment Variables

↓

Unchanged
```

Containers do **not** automatically reload environment variables.

To consume the updated value:

```
Restart Pod
```

---

# Mounted Secret Updates

Mounted Secret volumes behave differently.

```
Secret Updated

↓

kubelet Detects

↓

Mounted Files Updated
```

The application must reread the file if it does not automatically watch for configuration changes.

---

# Image Pull Secrets

Private Registry:

```
Pod

↓

ImagePullSecret

↓

Registry Login

↓

Image Download
```

Workflow:

```
Secret

↓

Container Runtime

↓

Authenticate

↓

Pull Image
```

---

# TLS Secret Workflow

```
TLS Secret

↓

Ingress

↓

HTTPS

↓

Application
```

The TLS certificate and private key are supplied from the Secret.

---

# ServiceAccount Secrets

Historically:

```
Service Account

↓

Secret

↓

API Authentication
```

Modern Kubernetes versions commonly use **projected service account tokens** instead of automatically creating long-lived Secret objects.

---

# Internal Architecture

```
Developer

↓

Secret

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

# Security Model

```
RBAC

↓

API Server

↓

Authorized?

↓

Yes

↓

Read Secret
```

Without permission:

```
Forbidden
```

RBAC is the primary mechanism controlling Secret access.

---

# Encryption at Rest

Production recommendation:

```
Secret

↓

API Server

↓

Encryption

↓

etcd
```

Benefits:

- Protects stored Secrets
- Improves compliance
- Reduces exposure if etcd storage is compromised

---

# Hands-on Lab 1 – Create Secret

```bash
kubectl create secret generic db-secret \
--from-literal=username=admin \
--from-literal=password=SecurePass123
```

Verify:

```bash
kubectl get secrets
```

---

# Hands-on Lab 2 – Use Environment Variables

Example:

```yaml
env:

- name: DB_PASSWORD

  valueFrom:

    secretKeyRef:

      name: db-secret

      key: password
```

Deploy:

```bash
kubectl apply -f pod.yaml
```

Verify:

```bash
kubectl exec -it <pod-name> -- printenv
```

---

# Hands-on Lab 3 – Mount Secret

Volume:

```yaml
volumes:

- name: secret-volume

  secret:

    secretName: db-secret
```

Verify:

```bash
kubectl exec -it <pod-name> -- ls /etc/secrets
```

Read:

```bash
kubectl exec -it <pod-name> -- cat /etc/secrets/password
```

---

# Hands-on Lab 4 – Update Secret

Edit:

```bash
kubectl edit secret db-secret
```

Observe:

- Mounted Secret files may refresh after a short delay.
- Environment variables remain unchanged until the Pod is restarted.

---

# Hands-on Lab 5 – Image Pull Secret

Create:

```bash
kubectl create secret docker-registry regcred \
--docker-server=<registry> \
--docker-username=<username> \
--docker-password=<password>
```

Reference:

```yaml
imagePullSecrets:

- name: regcred
```

Deploy a Pod using a private container image.

---

# Common Mistakes

## 1. Assuming Base64 Is Encryption

Incorrect:

```
Base64

↓

Secure
```

Correct:

```
Base64

↓

Encoding

↓

Enable Encryption at Rest
```

---

## 2. Storing Secrets in Git

Avoid committing:

```
secret.yaml
```

containing real credentials.

Use secure secret management workflows instead.

---

## 3. Printing Secrets

Avoid:

```bash
printenv
```

or application logs that expose credentials.

---

## 4. Giving Broad RBAC Permissions

Incorrect:

```
Everyone

↓

Read Secrets
```

Use least-privilege access.

---

## 5. Forgetting Secret Rotation

Long-lived credentials increase security risk.

Rotate:

- Passwords
- Tokens
- Certificates
- API Keys

regularly.

---

# Secrets Quick Revision

## Architecture

```
Secret

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
Secret

├── Environment Variables

├── Volume Mounts

└── Image Pull Secrets
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

Application Reload Needed
```

---

# Essential kubectl Commands

Create:

```bash
kubectl create secret generic db-secret \
--from-literal=password=Secure123
```

View:

```bash
kubectl get secrets
```

Describe:

```bash
kubectl describe secret db-secret
```

YAML:

```bash
kubectl get secret db-secret -o yaml
```

Delete:

```bash
kubectl delete secret db-secret
```

---

# Interview Questions

### Basic

- What is a Kubernetes Secret?
- How is a Secret different from a ConfigMap?
- What is Base64 encoding?

---

### Intermediate

- How can a Pod consume a Secret?
- What is an ImagePullSecret?
- What happens when a Secret is updated?

---

### Advanced

- Why is Base64 not considered encryption?
- How does kubelet securely distribute Secrets?
- What is Encryption at Rest?
- Why are Secrets Namespace-scoped?
- What are projected ServiceAccount tokens, and how do they differ from legacy ServiceAccount Secret tokens?

---

# References

## Official Kubernetes Documentation

- Secrets
- Secret Types
- Encryption at Rest
- Image Pull Secrets
- Service Accounts

---

## CNCF Resources

- Kubernetes Security Best Practices
- Cloud Native Computing Foundation (CNCF)
- Kubernetes Hardening Guide

---

## Security References

- CIS Kubernetes Benchmark
- NSA/CISA Kubernetes Hardening Guidance
- NIST SP 800-190
- OWASP Kubernetes Top 10

---

## Recommended Practice

1. Create Opaque Secrets using both `stringData` and `kubectl create secret`.
2. Consume Secrets through environment variables and mounted volumes.
3. Compare update behavior for environment variables versus mounted Secret files.
4. Configure an ImagePullSecret for a private container registry.
5. Create a TLS Secret and inspect its structure.
6. Review RBAC permissions for Secret access.
7. Enable Encryption at Rest in a lab cluster and verify Secret storage behavior.

---

# Chapter Summary

```
Developer

↓

Secret

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

Secrets provide Kubernetes with a secure mechanism for managing **credentials, certificates, tokens, and other confidential information**. When combined with **RBAC**, **Encryption at Rest**, and **regular credential rotation**, Secrets form a critical part of a production-grade Kubernetes security strategy.

---
