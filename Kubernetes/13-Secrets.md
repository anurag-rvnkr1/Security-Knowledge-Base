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

