# Chapter 53 – Secret Management

## Overview

Applications running in Kubernetes frequently require sensitive information such as:

```text
Passwords
API Keys
Database Credentials
TLS Certificates
OAuth Tokens
Cloud Credentials
SSH Keys
Encryption Keys
```

Kubernetes provides a native resource called:

```text
Secret
```

for storing and distributing sensitive configuration.

However, Kubernetes Secrets should **not** automatically be considered a complete secrets-management solution.

A secure production architecture may combine:

```text
Kubernetes Secrets
+
RBAC
+
Encryption at Rest
+
KMS
+
External Secret Manager
+
Secret Rotation
+
Workload Identity
+
Audit Logging
```

---

# Learning Objectives

After completing this chapter, you will understand:

- What Kubernetes Secrets are
- Why secret management matters
- Secret types
- Secret objects
- `data`
- `stringData`
- Base64 encoding
- Base64 vs encryption
- Creating Secrets
- Consuming Secrets
- Environment variables
- Secret volumes
- Secret rotation
- Secret lifecycle
- Encryption at rest
- EncryptionConfiguration
- KMS integration
- External secret management
- External Secrets Operator
- HashiCorp Vault
- Cloud secret managers
- Secrets Store CSI Driver
- Secret access control
- RBAC and Secrets
- Secret leakage
- Environment-variable exposure
- Secret exposure through logs
- Git secret management
- Sealed Secrets
- Secret scanning
- Secret rotation strategies
- Short-lived credentials
- Workload Identity
- Secret security architecture
- Secret incident response
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Is a Kubernetes Secret?

A Kubernetes Secret is an API object designed to hold small amounts of sensitive data.

Example:

```yaml
apiVersion: v1

kind: Secret

metadata:

  name: database-secret

type: Opaque

data:

  username: <base64-value>

  password: <base64-value>
```

A Secret can then be consumed by workloads.

---

# Why Secrets Are Needed

Applications often need credentials.

For example:

```text
Application
     ↓
Database
```

The application may need:

```text
DB_USERNAME
DB_PASSWORD
```

Hardcoding them into the image is dangerous.

Bad:

```python
DATABASE_PASSWORD = "MySuperSecretPassword"
```

Instead:

```text
Application
     ↓
Kubernetes Secret
     ↓
Credential
```

---

# Secret Management Architecture

A basic architecture:

```text
Developer
    │
    ▼
Kubernetes Secret
    │
    ▼
RBAC
    │
    ▼
Pod
    │
    ▼
Application
```

A stronger production architecture may use:

```text
External Secret Manager
          │
          ▼
Secret Synchronization
          │
          ▼
Kubernetes
          │
          ▼
Pod
```

---

# Secret vs ConfigMap

This distinction is important.

```text
ConfigMap
=
Non-sensitive configuration
```

```text
Secret
=
Sensitive configuration
```

Examples:

### ConfigMap

```text
APP_ENV=production
LOG_LEVEL=info
APP_PORT=8080
```

### Secret

```text
DB_PASSWORD
API_TOKEN
PRIVATE_KEY
```

---

# Important Security Note

Kubernetes Secret data is commonly represented using:

```text
Base64
```

Base64 is **encoding**, not encryption.

Therefore:

```text
Base64 ≠ Encryption
```

---

# Base64 Encoding

Example:

```text
password
```

can be encoded as:

```text
cGFzc3dvcmQ=
```

Anyone who can read the Secret data can decode it.

Base64 provides:

```text
Representation
```

not:

```text
Confidentiality
```

---

# Base64 Decoding

Linux:

```bash
echo 'cGFzc3dvcmQ=' | base64 --decode
```

Result:

```text
password
```

This demonstrates why Base64 should never be treated as encryption.

---

# Secret Structure

A typical Secret:

```yaml
apiVersion: v1

kind: Secret

metadata:

  name: app-secret

type: Opaque

data:

  username: YWRtaW4=

  password: cGFzc3dvcmQ=
```

---

# `data`

The:

```yaml
data:
```

field contains values represented using Base64 encoding.

Example:

```yaml
data:

  username: YWRtaW4=
```

---

# `stringData`

Kubernetes also supports:

```yaml
stringData:
```

This allows values to be specified as strings.

Example:

```yaml
apiVersion: v1

kind: Secret

metadata:

  name: app-secret

type: Opaque

stringData:

  username: admin

  password: password123
```

Kubernetes processes the values into Secret data.

---

# `data` vs `stringData`

| Field | Input |
|---|---|
| `data` | Base64-encoded values |
| `stringData` | Plain string values |

For authoring manifests, `stringData` can be more convenient.

However, the resulting Secret remains sensitive.

---

# Secret Types

Kubernetes supports several Secret types.

Common examples:

```text
Opaque
kubernetes.io/tls
kubernetes.io/dockerconfigjson
kubernetes.io/basic-auth
kubernetes.io/ssh-auth
service-account-token
```

---

# Opaque

The default generic Secret type is:

```text
Opaque
```

Example:

```yaml
type: Opaque
```

It can store arbitrary application data.

---

# TLS Secret

TLS certificates can be stored using:

```yaml
type: kubernetes.io/tls
```

Typically:

```text
tls.crt
tls.key
```

are stored.

---

# Docker Registry Secret

A registry credential Secret may use:

```text
kubernetes.io/dockerconfigjson
```

This can be referenced using:

```yaml
imagePullSecrets:
```

---

# Basic Authentication Secret

A Secret can represent basic authentication credentials using:

```text
kubernetes.io/basic-auth
```

---

# SSH Authentication Secret

SSH credentials can use:

```text
kubernetes.io/ssh-auth
```

---

# Service Account Token Secrets

Historically, Service Account tokens could be stored in Secret objects.

Modern Kubernetes generally uses short-lived, automatically managed Service Account tokens through:

```text
TokenRequest
```

and projected volumes.

Long-lived manually managed Service Account token Secrets should generally be avoided unless there is a specific requirement.

---

# Creating a Secret

Using literals:

```bash
kubectl create secret generic app-secret \
  --from-literal=username=admin \
  --from-literal=password='MyPassword'
```

---

# List Secrets

```bash
kubectl get secrets
```

---

# Get Secret

```bash
kubectl get secret app-secret
```

Avoid casually printing Secret contents in shared terminals or logs.

---

# Inspect Secret Metadata

```bash
kubectl describe secret app-secret
```

This normally shows metadata and key names without directly displaying values.

---

# Retrieve Secret Data

```bash
kubectl get secret app-secret \
  -o jsonpath='{.data.password}'
```

This returns the encoded value.

Decoding it exposes the secret.

Use caution.

---

# Secret From File

Create:

```bash
echo -n 'admin' > username.txt
```

Then:

```bash
kubectl create secret generic app-secret \
  --from-file=username=username.txt
```

---

# Secret From Environment File

Example:

```text
username=admin
password=secret
```

Create:

```bash
kubectl create secret generic app-secret \
  --from-env-file=.env
```

Be extremely careful with `.env` files.

They should generally not be committed to Git.

---

# Consuming Secrets

Secrets can be consumed through:

```text
Environment Variables
Volume Mounts
Image Pull Secrets
Projected Volumes
External Secret Integrations
```

---

# Secret as Environment Variable

Example:

```yaml
env:

- name: DB_PASSWORD

  valueFrom:

    secretKeyRef:

      name: database-secret

      key: password
```

The application receives:

```text
DB_PASSWORD
```

---

# Secret as Volume

Example:

```yaml
volumes:

- name: secret-volume

  secret:

    secretName: database-secret
```

Mount:

```yaml
volumeMounts:

- name: secret-volume

  mountPath: /etc/secrets

  readOnly: true
```

The Secret becomes available as files.

---

# Environment Variable vs Volume

| Method | Advantage | Risk |
|---|---|---|
| Environment | Easy application integration | Can leak through process/debug tooling |
| Volume | File-based access | Application must read files |

Neither should be considered universally safer.

The correct choice depends on:

```text
Application
Threat Model
Runtime
Operational Requirements
```

---

# Secret Volume

Suppose the Secret contains:

```text
username
password
```

The Pod may see:

```text
/etc/secrets/username
/etc/secrets/password
```

The application can read these files.

---

# Secret Updates

Kubernetes can update Secret-backed volumes when the Secret changes, subject to how the volume is consumed and implementation details.

However, applications may not automatically reload the new value.

For example:

```text
Secret updated
      ↓
Volume updated
      ↓
Application
      ↓
Still using old credential
```

The application may need:

```text
Reload
Restart
Signal
```

depending on its implementation.

---

# Environment Variable Rotation

Secret values injected as environment variables are not dynamically updated inside an already-running process.

Typically:

```text
Secret updated
      ↓
Existing Pod
      ↓
Old environment value
```

A Pod restart is generally needed for the process to receive the new environment value.

---

# Secret Rotation

Secret rotation means replacing a credential with a new credential.

Example:

```text
Old Password
     ↓
New Password
```

---

# Why Rotate Secrets?

Secret rotation reduces the impact of:

```text
Credential Theft
Accidental Exposure
Employee Departure
Long-Lived Credentials
Security Incidents
```

---

# Rotation Strategy

A basic strategy:

```text
Generate New Credential
       ↓
Update External System
       ↓
Update Kubernetes Secret
       ↓
Restart / Reload Application
       ↓
Verify
       ↓
Revoke Old Credential
```

---

# Zero-Downtime Rotation

For systems that support multiple credentials:

```text
Credential A
Credential B
```

The application can temporarily accept both.

Process:

```text
Create B
   ↓
Deploy B
   ↓
Verify B
   ↓
Revoke A
```

This can avoid downtime.

---

# Secret Lifecycle

A mature lifecycle is:

```text
Create
  ↓
Store
  ↓
Access
  ↓
Rotate
  ↓
Audit
  ↓
Revoke
  ↓
Delete
```

---

# Encryption at Rest

Kubernetes Secrets are stored in:

```text
API Server storage
```

typically:

```text
etcd
```

Therefore, protecting storage is critical.

Encryption at rest can protect Secret data stored in the cluster datastore.

---

# Encryption at Rest Architecture

Without encryption at rest:

```text
Secret
 ↓
etcd
 ↓
Stored Data
```

With encryption:

```text
Secret
 ↓
API Server Encryption
 ↓
Encrypted Storage
 ↓
etcd
```

---

# EncryptionConfiguration

Kubernetes can configure encryption at rest using an:

```text
EncryptionConfiguration
```

This specifies encryption providers for resources stored by the API Server.

---

# Example Concept

A simplified conceptual configuration:

```yaml
apiVersion: apiserver.config.k8s.io/v1

kind: EncryptionConfiguration

resources:

- resources:

  - secrets

  providers:

  - aescbc:

      keys:

      - name: key1

        secret: <base64-key>

  - identity: {}
```

The exact provider and operational configuration should be selected carefully for the Kubernetes environment.

---

# Encryption Providers

Kubernetes supports multiple encryption approaches depending on version and configuration.

Examples include:

```text
aescbc
secretbox
kms
identity
```

---

# KMS

KMS means:

```text
Key Management Service
```

A KMS can provide external key management.

Architecture:

```text
Kubernetes API Server
        │
        ▼
       KMS
        │
        ▼
External Key Management
```

---

# Why KMS Matters

Instead of relying entirely on keys stored with the cluster:

```text
Kubernetes
    ↓
External Key Management
```

can provide:

```text
Key Rotation
Centralized Control
Auditing
Separation of Duties
```

---

# KMS Architecture

Conceptually:

```text
Secret
  ↓
API Server
  ↓
KMS Plugin
  ↓
External KMS
  ↓
Encrypted Data
  ↓
etcd
```

---

# Protect etcd

etcd contains critical Kubernetes state.

Protect it using:

```text
Encryption at Rest
Network Isolation
TLS
Authentication
Access Control
Backups
```

---

# RBAC and Secrets

Secrets are protected by Kubernetes authorization mechanisms.

For example:

```text
get secrets
```

is a sensitive permission.

---

# Dangerous RBAC

Avoid giving broad permissions such as:

```yaml
resources:

- secrets

verbs:

- get
- list
- watch
```

unless genuinely required.

---

# Why `list` Is Sensitive

A user who can list Secrets may potentially access many sensitive objects.

Therefore:

```text
Secret permissions
=
Highly sensitive
```

---

# Least Privilege

Instead of:

```text
All Secrets
```

prefer:

```text
Specific Namespace
+
Specific Secret
+
Required Operations
```

where feasible.

---

# Secret Access Model

```text
User / ServiceAccount
        ↓
RBAC
        ↓
Secret
        ↓
Allowed / Denied
```

---

# Service Account Access

Applications commonly access Secrets through their Pod identity.

Example:

```text
Pod
 ↓
ServiceAccount
 ↓
RBAC
 ↓
Secret
```

Avoid giving every application:

```text
get secrets
```

across the cluster.

---

# Secret Exposure Through Environment Variables

Environment variables can potentially appear through:

```text
Process inspection
Debugging
Crash dumps
Application diagnostics
Logs
Support tooling
```

Therefore, avoid printing them.

Bad:

```python
print(os.environ)
```

---

# Secret Exposure Through Logs

Never log:

```text
Passwords
API Tokens
Private Keys
Session Tokens
Database Credentials
```

Bad:

```text
DB_PASSWORD=SuperSecret123
```

Better:

```text
Database authentication failed
```

---

# Secret Exposure Through Error Messages

Applications should avoid including secrets in:

```text
Exceptions
HTTP responses
Stack traces
Debug output
Metrics labels
```

---

# Secret Exposure Through Kubernetes Manifests

Avoid putting real secrets directly into:

```text
Git
Helm values
Terraform files
CI logs
Pull requests
Issue trackers
```

---

# Git Secret Management

Never commit:

```yaml
stringData:

  password: MyProductionPassword
```

to a public or untrusted repository.

Even private repositories require careful secret handling.

---

# `.gitignore`

Sensitive local files can be excluded:

```gitignore
.env
.env.*
*.secret
credentials.yaml
```

However:

```text
.gitignore
```

does not remove secrets that were already committed.

---

# If a Secret Is Committed

Assume compromise.

Do:

```text
1. Revoke credential
2. Rotate credential
3. Remove secret from current files
4. Rewrite repository history if appropriate
5. Scan repository
6. Review access
```

Deleting the file in a later commit is not sufficient because Git history may still contain it.

---

# Secret Scanning

Use secret scanning to detect:

```text
API Keys
Cloud Credentials
Tokens
Private Keys
Passwords
```

Tools may include:

```text
GitHub Secret Scanning
Gitleaks
TruffleHog
GitLab Secret Detection
Cloud-native scanners
```

---

# Sealed Secrets

A popular approach is:

```text
Sealed Secrets
```

It allows encrypted Secret manifests to be stored in Git.

Conceptually:

```text
Secret
  ↓
Sealing Controller / Tool
  ↓
Encrypted Manifest
  ↓
Git
  ↓
Cluster
  ↓
Decrypt
  ↓
Kubernetes Secret
```

---

# Why Sealed Secrets?

Instead of committing:

```text
Plain Secret
```

commit:

```text
Encrypted Secret
```

The cluster controller can decrypt it.

---

# Important Sealed Secrets Limitation

The encryption system must itself be protected.

If the relevant decryption key is compromised:

```text
Encrypted Secrets
       ↓
Potentially Decrypted
```

Therefore, key management remains critical.

---

# External Secret Management

A stronger enterprise architecture often stores secrets outside Kubernetes.

Examples:

```text
HashiCorp Vault
AWS Secrets Manager
Azure Key Vault
Google Secret Manager
```

The application retrieves or synchronizes credentials through an integration.

---

# External Secrets Operator

The:

```text
External Secrets Operator
```

can synchronize secrets from external secret managers into Kubernetes Secret objects.

Conceptually:

```text
External Secret Manager
          │
          ▼
External Secrets Operator
          │
          ▼
Kubernetes Secret
          │
          ▼
Pod
```

---

# Why External Secret Managers?

They can provide:

```text
Centralized Secret Management
Rotation
Access Policies
Auditing
Key Management
Cross-Platform Access
```

---

# HashiCorp Vault

Vault is a dedicated secrets-management platform.

It can provide:

```text
Secret Storage
Dynamic Credentials
Secret Rotation
Authentication
Policy
Audit
Encryption
```

---

# Vault Dynamic Credentials

Instead of storing a permanent database password:

```text
Application
    ↓
Vault
    ↓
Temporary Database Credential
```

The credential can expire.

This reduces the value of stolen credentials.

---

# Cloud Secret Managers

Cloud platforms provide managed secret systems.

Examples:

```text
AWS Secrets Manager
Azure Key Vault
Google Secret Manager
```

Applications can authenticate using workload identity mechanisms and retrieve secrets without embedding long-lived cloud credentials.

---

# Workload Identity

Workload identity allows a workload to authenticate to cloud services using an identity associated with the workload.

Conceptually:

```text
Pod
 ↓
Workload Identity
 ↓
Cloud IAM
 ↓
Secret Manager
```

This can reduce the need for:

```text
Static Cloud Access Keys
```

---

# Short-Lived Credentials

Prefer:

```text
Short-lived credential
```

over:

```text
Long-lived credential
```

Example:

```text
Token
 ↓
Expires in 15 minutes
```

instead of:

```text
Token
 ↓
Never expires
```

---

# Secrets Store CSI Driver

The:

```text
Secrets Store CSI Driver
```

allows Pods to access secrets from external secret-management systems through CSI volumes.

Conceptually:

```text
External Secret Manager
        │
        ▼
Secrets Store CSI Driver
        │
        ▼
Pod Volume
        │
        ▼
Application
```

---

# External Secrets vs CSI

These approaches differ.

### External Secrets

Often:

```text
External Manager
 ↓
Kubernetes Secret
 ↓
Pod
```

### Secrets Store CSI Driver

Often:

```text
External Manager
 ↓
CSI Volume
 ↓
Pod
```

The correct choice depends on:

```text
Application
Secret Lifecycle
Compatibility
Security Requirements
Operational Model
```

---

# Secret Architecture Comparison

| Approach | Storage | Rotation | Complexity |
|---|---|---|---|
| Kubernetes Secret | Kubernetes | Manual/Automated | Low |
| Sealed Secrets | Git encrypted + cluster | Depends | Medium |
| External Secrets | External manager + optional K8s Secret | Strong | Medium |
| CSI Driver | External manager | Strong | Medium |
| Vault | External | Strong | High |

---

# Secret Security Architecture

A mature architecture:

```text
                    External KMS
                         │
                         ▼
                 Secret Manager
                         │
                         ▼
                 External Secrets
                         │
                         ▼
                 Kubernetes Secret
                         │
                       RBAC
                         │
                         ▼
                       Pod
                         │
                         ▼
                    Application
```

---

# Secret Access Defense in Depth

```text
Authentication
      ↓
Authorization
      ↓
Secret Access
      ↓
Encryption
      ↓
Application
      ↓
Audit
```

---

# Secret Rotation Architecture

```text
Secret Manager
      │
      ▼
Generate New Credential
      │
      ▼
Synchronize
      │
      ▼
Kubernetes
      │
      ▼
Application Reload
      │
      ▼
Verify
      │
      ▼
Revoke Old Credential
```

---

# Secret Incident Response

If a credential is exposed:

```text
1. Identify secret
2. Determine scope
3. Revoke immediately
4. Generate replacement
5. Update workloads
6. Search for persistence
7. Review access logs
8. Investigate compromise
9. Remove exposed secret
10. Document incident
```

---

# Example Incident

Suppose:

```text
Production API token
```

was accidentally committed to Git.

Do not simply delete the file.

Instead:

```text
Exposed Token
     ↓
Revoke
     ↓
Generate New Token
     ↓
Update Secret Manager
     ↓
Update Application
     ↓
Search Git History
     ↓
Investigate Usage
```

---

# Secret Access Auditing

Monitor:

```text
Who accessed the Secret?
When?
From where?
Which ServiceAccount?
Which API operation?
```

Kubernetes audit logging can help provide visibility into API access.

---

# Secret Management and CI/CD

Avoid:

```text
Secret
 ↓
CI log
```

Instead:

```text
CI/CD
 ↓
Secret Manager
 ↓
Temporary Credential
 ↓
Deployment
```

---

# CI/CD Secret Best Practices

Use:

```text
Secret Store Integration
Masked Variables
Short-Lived Credentials
OIDC / Workload Identity
Restricted Permissions
Audit Logging
```

Avoid:

```text
Hardcoded Secrets
Plaintext Environment Files
Long-Lived Tokens
Secrets in Build Logs
```

---

# Secret Management and GitOps

GitOps introduces an important challenge:

```text
Desired State
```

is stored in Git.

Secrets should not normally be stored in plaintext.

Possible approaches:

```text
Sealed Secrets
External Secrets
SOPS
Secret Manager Integration
```

---

# SOPS

SOPS can encrypt sensitive configuration files before storing them in Git.

Conceptually:

```text
Secret File
    ↓
SOPS Encryption
    ↓
Encrypted Git File
    ↓
GitOps
    ↓
Decryption During Deployment
```

---

# Secret Management Threat Model

Potential threats:

```text
Secret Theft
Credential Leakage
Excessive RBAC
etcd Compromise
Git Exposure
Log Exposure
Environment Exposure
Insider Threat
Credential Reuse
Long-Lived Credentials
```

Controls:

```text
Encryption
RBAC
KMS
Secret Manager
Rotation
Short-Lived Credentials
Secret Scanning
Audit
Workload Identity
```

---

# Troubleshooting Secret Access

If a Pod cannot access a Secret:

```text
1. Does the Secret exist?
2. Is it in the correct namespace?
3. Does the key exist?
4. Does the ServiceAccount have permission?
5. Is the volume correctly mounted?
6. Is the environment variable correctly referenced?
7. Is the external secret synchronized?
8. Are the external credentials valid?
```

---

# Check Secret

```bash
kubectl get secret app-secret
```

---

# Check Secret Keys

```bash
kubectl describe secret app-secret
```

---

# Check Pod

```bash
kubectl describe pod <pod>
```

Look for:

```text
Mount errors
Secret not found
Environment variable errors
Volume errors
```

---

# Check External Secrets

If using an external secret system, inspect the relevant resource:

```bash
kubectl get externalsecrets
```

The exact command depends on the installed controller and API version.

---

# Check Secret Volume

Inside the Pod:

```bash
kubectl exec -it <pod> -- ls -la /etc/secrets
```

Do not print sensitive files unnecessarily.

---

# Common Secret Error

```text
secret "app-secret" not found
```

Possible cause:

```text
Secret exists in another namespace
```

Remember:

```text
Secrets are namespace-scoped.
```

---

# Common Secret Error

Environment variable is empty.

Check:

```yaml
secretKeyRef:

  name: app-secret

  key: password
```

Ensure:

```text
Secret exists
Key exists
Namespace matches
```

---

# Common Secret Error

External Secret is not synchronized.

Investigate:

```text
External Secret status
Controller logs
External provider credentials
Network connectivity
Secret manager permissions
```

---

# Hands-on Lab 1 – Create a Secret

Create:

```bash
kubectl create secret generic app-secret \
  --from-literal=username=admin \
  --from-literal=password='TestPassword123'
```

Check:

```bash
kubectl get secret app-secret
```

---

# Hands-on Lab 2 – Inspect Secret

Run:

```bash
kubectl describe secret app-secret
```

Observe:

```text
Secret name
Type
Keys
```

Then retrieve an encoded value:

```bash
kubectl get secret app-secret \
  -o jsonpath='{.data.password}'
```

Decode it only in your disposable lab environment.

---

# Hands-on Lab 3 – Use Secret as Environment Variable

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: secret-env

spec:

  containers:

  - name: app

    image: nginx:1.30

    env:

    - name: APP_PASSWORD

      valueFrom:

        secretKeyRef:

          name: app-secret

          key: password
```

Apply:

```bash
kubectl apply -f secret-env.yaml
```

---

# Hands-on Lab 4 – Use Secret as Volume

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: secret-volume

spec:

  containers:

  - name: app

    image: nginx:1.30

    volumeMounts:

    - name: secrets

      mountPath: /etc/app-secrets

      readOnly: true

  volumes:

  - name: secrets

    secret:

      secretName: app-secret
```

Check:

```bash
kubectl exec -it secret-volume -- \
  ls -la /etc/app-secrets
```

---

# Hands-on Lab 5 – Test Secret Rotation

1. Create a Secret.
2. Mount it as a volume.
3. Update the Secret.
4. Observe the mounted files.
5. Compare with an environment-variable-based Secret.
6. Determine when the application receives the new value.

---

# Hands-on Lab 6 – RBAC Secret Access

Create a dedicated ServiceAccount:

```bash
kubectl create serviceaccount secret-reader
```

Create a narrowly scoped Role allowing access to one Secret.

Then create a RoleBinding.

Test:

```text
Allowed Secret
```

and:

```text
Other Secret
```

Verify least privilege.

---

# Hands-on Lab 7 – Secret Exposure Review

Search a test application for:

```text
print(environment)
logging passwords
hardcoded tokens
debug output
```

Remove all sensitive output.

---

# Hands-on Lab 8 – Secret Scanning

Install a secret scanning tool in a disposable repository.

Create a fake credential:

```text
API_KEY=example-secret
```

Run the scanner.

Observe how it identifies potential secrets.

Never use real production credentials for this exercise.

---

# Hands-on Lab 9 – Encryption at Rest

In a disposable cluster or local Kubernetes environment, inspect whether:

```text
Secrets
```

are encrypted at rest.

Review the cluster's:

```text
EncryptionConfiguration
```

if you administer the control plane.

---

# Hands-on Lab 10 – External Secret Architecture

Deploy an external secret manager integration in a lab environment.

Practice:

```text
External Secret
      ↓
Controller
      ↓
Kubernetes Secret
      ↓
Pod
```

Observe synchronization and rotation behavior.

---

# Common Mistakes

## 1. Treating Base64 as Encryption

Remember:

```text
Base64 = Encoding
```

not:

```text
Encryption
```

---

## 2. Committing Secrets to Git

Never store production credentials directly in source control.

---

## 3. Logging Secrets

Avoid:

```text
Passwords
Tokens
Private Keys
```

in logs.

---

## 4. Giving Broad Secret Permissions

Avoid unnecessary:

```text
get/list/watch secrets
```

permissions.

---

## 5. Using Long-Lived Credentials

Prefer:

```text
Short-Lived Credentials
```

where possible.

---

## 6. Forgetting Namespace Scope

A Secret in:

```text
namespace-a
```

is not automatically available in:

```text
namespace-b
```

---

## 7. Assuming Secret Volume Updates Mean Application Updates

The mounted value may update, but the application must actually reload it.

---

## 8. Assuming Environment Variables Rotate Automatically

Existing processes generally continue using their current environment values.

---

## 9. Storing Secrets in Container Images

Never bake credentials into:

```text
Dockerfile
Container Image
```

---

## 10. Storing Secrets in Helm Values

Avoid plaintext production credentials in:

```text
values.yaml
```

---

## 11. Sharing One Credential Across Many Applications

Use separate credentials whenever possible.

---

## 12. Never Rotating Credentials

Long-lived credentials increase exposure time.

---

# Best Practices

### 1. Never Hardcode Secrets

Use:

```text
Secret Manager
Kubernetes Secret
External Secret
```

---

### 2. Encrypt Secrets at Rest

Protect:

```text
etcd
```

using appropriate encryption mechanisms.

---

### 3. Use KMS Where Appropriate

External key management can strengthen:

```text
Key Protection
Rotation
Auditing
```

---

### 4. Use Least-Privilege RBAC

Restrict:

```text
Who can read Secrets
```

---

### 5. Prefer External Secret Management for Sensitive Production Environments

Examples:

```text
Vault
AWS Secrets Manager
Azure Key Vault
Google Secret Manager
```

---

### 6. Rotate Credentials

Establish:

```text
Rotation Frequency
Emergency Rotation Procedure
Ownership
```

---

### 7. Prefer Short-Lived Credentials

Reduce:

```text
Credential Lifetime
```

where possible.

---

### 8. Use Workload Identity

Avoid embedding cloud access keys into Pods.

---

### 9. Scan Source Code

Use:

```text
Secret Scanning
```

in CI/CD.

---

### 10. Protect Logs

Never expose:

```text
Passwords
Tokens
Private Keys
```

---

### 11. Use Git-Safe Secret Management

Consider:

```text
Sealed Secrets
SOPS
External Secrets
Secret Managers
```

---

### 12. Audit Secret Access

Monitor:

```text
Secret Reads
Permission Changes
Unexpected Access
```

---

### 13. Separate Credentials

Use separate credentials for:

```text
Development
Staging
Production
```

---

### 14. Build an Incident Response Process

If a secret leaks:

```text
Revoke
Rotate
Investigate
Contain
Monitor
Document
```

---

# Production Secret Architecture

A strong enterprise design:

```text
                    Cloud KMS
                       │
                       ▼
                Secret Manager
                       │
                       ▼
              External Secret System
                       │
                       ▼
                Kubernetes Secret
                       │
                    RBAC
                       │
                       ▼
                      Pod
                       │
                       ▼
                  Application
```

Additional controls:

```text
Audit Logging
Secret Scanning
Rotation
Workload Identity
Network Security
```

---

# Defense-in-Depth

```text
                Secret
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    Encryption    RBAC     Rotation
        │          │          │
        └──────────┼──────────┘
                   ▼
             Secret Manager
                   │
                   ▼
                 Pod
                   │
                   ▼
              Application
                   │
                   ▼
               Monitoring
```

---

# Secret Threat Model

| Threat | Example | Control |
|---|---|---|
| Git leak | Password committed | Secret scanning |
| etcd theft | Storage compromise | Encryption at rest |
| RBAC abuse | User reads Secrets | Least privilege |
| Log leak | Token printed | Log hygiene |
| Credential theft | API key stolen | Rotation |
| Long-lived token | Permanent credential | Short-lived credentials |
| Pod compromise | Credential mounted | Workload isolation |
| Cloud key leak | Static access key | Workload identity |

---

# Quick Revision

## Secret

```text
Sensitive configuration object
```

---

## `data`

```text
Base64-encoded values
```

---

## `stringData`

```text
String input converted into Secret data
```

---

## Base64

```text
Encoding, not encryption
```

---

## `Opaque`

```text
Generic Secret type
```

---

## TLS Secret

```text
kubernetes.io/tls
```

---

## Image Pull Secret

```text
kubernetes.io/dockerconfigjson
```

---

## Secret Volume

```text
Expose Secret as files
```

---

## Secret Environment Variable

```text
Expose Secret as process environment
```

---

## Encryption at Rest

```text
Protect stored Secret data
```

---

## KMS

```text
External key management
```

---

## External Secret Manager

```text
Dedicated system for managing credentials
```

---

## Workload Identity

```text
Workload-based authentication to external services
```

---

## Rotation

```text
Replace credentials periodically or after compromise
```

---

# Essential Commands

Create Secret:

```bash
kubectl create secret generic app-secret \
  --from-literal=username=admin \
  --from-literal=password='password'
```

List Secrets:

```bash
kubectl get secrets
```

Get Secret:

```bash
kubectl get secret app-secret
```

Describe Secret:

```bash
kubectl describe secret app-secret
```

Get encoded key:

```bash
kubectl get secret app-secret \
  -o jsonpath='{.data.password}'
```

Create from file:

```bash
kubectl create secret generic app-secret \
  --from-file=password=./password.txt
```

Create from env file:

```bash
kubectl create secret generic app-secret \
  --from-env-file=.env
```

Delete Secret:

```bash
kubectl delete secret app-secret
```

List Secrets in all namespaces:

```bash
kubectl get secrets -A
```

Check Pod:

```bash
kubectl describe pod <pod>
```

Check ServiceAccount:

```bash
kubectl get serviceaccount
```

Check RBAC:

```bash
kubectl get role,rolebinding
```

---

# Interview Questions

## Basic

- What is a Kubernetes Secret?
- Why are Secrets used?
- What is the difference between Secret and ConfigMap?
- What is Base64?
- Is Base64 encryption?
- What is `stringData`?
- What is `data`?
- What is an `Opaque` Secret?
- How can a Pod consume a Secret?
- What is a Secret volume?
- What is a Secret environment variable?

---

## Intermediate

- How do you create a Secret using `kubectl`?
- How do you mount a Secret as a volume?
- How do you expose a Secret as an environment variable?
- How do you restrict Secret access using RBAC?
- Why are Kubernetes Secrets considered sensitive even though they use Base64?
- What is encryption at rest?
- What is KMS?
- How do you rotate Kubernetes Secrets?
- What happens when a Secret changes?
- Are Secret environment variables automatically updated?
- Why should Secrets not be committed to Git?
- What is Sealed Secrets?
- What is External Secrets Operator?
- What is the Secrets Store CSI Driver?

---

## Advanced

- How would you design enterprise-grade Kubernetes Secret management?
- How would you protect Secrets stored in etcd?
- How would you integrate Kubernetes with an external secret manager?
- How would you implement zero-downtime credential rotation?
- How would you respond if a production API key was committed to Git?
- How would you prevent applications from accessing unrelated Secrets?
- How would you use Workload Identity to avoid cloud credentials in Pods?
- Compare Kubernetes Secrets, Sealed Secrets, External Secrets, and Vault.
- What are the risks of environment-variable-based Secrets?
- How can Secret access be audited?
- How would you design Secret management for a multi-tenant Kubernetes cluster?
- How would you prevent Secret leakage through CI/CD?
- How would you implement emergency credential rotation?
- How does encryption at rest protect Kubernetes Secrets?
- What security risks remain even when Secrets are encrypted at rest?

---

# Interview Scenario 1

### Question

> Are Kubernetes Secrets encrypted because their values are Base64 encoded?

### Answer

No.

Base64 is only an encoding mechanism.

```text
Base64
=
Encoding
```

not:

```text
Encryption
```

Anyone who can read the Secret data can decode it.

For stronger protection, use:

```text
Encryption at Rest
+
KMS
+
RBAC
+
External Secret Management
```

---

# Interview Scenario 2

### Question

> A Secret was accidentally committed to Git. What should you do?

### Answer

Treat it as compromised.

The response should be:

```text
1. Revoke the exposed credential
2. Generate a replacement
3. Update the Secret Manager / Kubernetes Secret
4. Restart or reload affected applications
5. Investigate whether the credential was used
6. Remove the secret from repository history where appropriate
7. Scan the repository
8. Review access
```

Deleting the file in a later Git commit is not enough because the old value may remain in Git history.

---

# Interview Scenario 3

### Question

> How would you securely provide database credentials to a production Pod?

### Answer

Prefer a dedicated external secret manager where practical:

```text
Secret Manager
      ↓
External Secret Integration
      ↓
Kubernetes
      ↓
Pod
```

Use:

```text
Least-Privilege RBAC
Encryption
Rotation
Audit Logging
Short-Lived Credentials
```

For cloud-native environments, workload identity can avoid storing long-lived cloud credentials in the Pod.

---

# Interview Scenario 4

### Question

> A Kubernetes Secret was rotated, but the application is still using the old password. Why?

### Answer

If the Secret was injected as an environment variable:

```text
Secret
 ↓
Pod creation
 ↓
Environment variable
 ↓
Application
```

the running process generally continues using the old value.

The application may need:

```text
Pod restart
```

or another reload mechanism.

If the Secret is mounted as a volume, the mounted content may update, but the application must actually reload the changed file.

---

# Interview Scenario 5

### Question

> How would you prevent developers from reading production Secrets?

### Answer

Use:

```text
RBAC
+
Namespace Separation
+
Least Privilege
+
Dedicated Service Accounts
+
Audit Logging
```

For example:

```text
Developer
 ↓
Production Namespace
 ↓
No Secret read permission
```

while:

```text
Production Workload
 ↓
Dedicated ServiceAccount
 ↓
Specific Secret
 ↓
Allowed
```

---

# Production Secret Management Checklist

```text
☑ Never hardcode credentials
☑ Never commit plaintext Secrets
☑ Never log credentials
☑ Treat Base64 as encoding only
☑ Encrypt Secrets at rest
☑ Protect etcd
☑ Use least-privilege RBAC
☑ Restrict Secret access by namespace
☑ Prefer external Secret management where appropriate
☑ Use KMS where appropriate
☑ Rotate credentials
☑ Prefer short-lived credentials
☑ Use workload identity
☑ Scan Git repositories
☑ Protect CI/CD logs
☑ Audit Secret access
☑ Separate development/staging/production credentials
☑ Establish incident response procedures
```

---

# Recommended Practice

1. Create a Kubernetes Secret.
2. Inspect its metadata.
3. Understand Base64 encoding.
4. Consume the Secret as an environment variable.
5. Consume the Secret as a volume.
6. Update the Secret.
7. Observe volume behavior.
8. Observe environment-variable behavior.
9. Create a dedicated ServiceAccount.
10. Create a Role allowing limited Secret access.
11. Test RBAC restrictions.
12. Study encryption at rest.
13. Study KMS integration.
14. Study external secret managers.
15. Study External Secrets Operator.
16. Study Secrets Store CSI Driver.
17. Study Sealed Secrets.
18. Practice secret rotation.
19. Practice emergency credential revocation.
20. Run secret scanning against a test repository.
21. Design a production Secret management architecture.
22. Document your Secret incident-response process.

---

# References

## Official Kubernetes Documentation

- Secrets
- Secret Types
- Secret Security
- Encrypting Secret Data at Rest
- KMS Providers
- Service Accounts
- RBAC Authorization
- Secrets Store CSI Driver
- Workload Identity Concepts
- Kubernetes Audit Logging

---

# Chapter Summary

Kubernetes Secrets provide a mechanism for distributing sensitive configuration to workloads.

Common Secret data includes:

```text
Passwords
API Keys
Tokens
Certificates
Private Keys
Database Credentials
```

Secrets can be consumed through:

```text
Environment Variables
Volumes
Image Pull Secrets
Projected Volumes
External Secret Integrations
```

The most important concept is:

> **Base64 is encoding, not encryption.**

Therefore:

```text
Base64
≠
Confidentiality
```

Production environments should consider:

```text
Encryption at Rest
+
KMS
+
RBAC
+
Secret Rotation
+
External Secret Management
+
Audit Logging
```

Secret access should follow:

```text
Least Privilege
```

A workload should receive only the credentials it actually needs.

Avoid broad permissions such as:

```text
get/list/watch all Secrets
```

when a more restricted permission is possible.

Secrets should never be:

```text
Hardcoded
Committed to Git
Printed to logs
Stored in container images
Exposed through debug endpoints
```

For GitOps environments, safer approaches include:

```text
Sealed Secrets
SOPS
External Secrets
Secret Managers
```

For enterprise environments, external secret management can provide:

```text
Centralized Storage
Rotation
Auditing
Access Policies
Dynamic Credentials
KMS Integration
```

A secure architecture can look like:

```text
                     KMS
                      │
                      ▼
               Secret Manager
                      │
                      ▼
              External Secret
                  System
                      │
                      ▼
              Kubernetes Secret
                      │
                    RBAC
                      │
                      ▼
                     Pod
                      │
                      ▼
                Application
                      │
                      ▼
                  Auditing
```

Secret rotation should follow:

```text
Generate New
     ↓
Deploy New
     ↓
Verify
     ↓
Revoke Old
```

For sensitive credentials, prefer:

```text
Short-Lived Credentials
```

over:

```text
Long-Lived Static Credentials
```

Workload identity can further reduce the need to distribute cloud credentials directly to Pods.

If a secret is exposed:

```text
Revoke
 ↓
Rotate
 ↓
Contain
 ↓
Investigate
 ↓
Monitor
 ↓
Document
```

The key principle is:

> **A Kubernetes Secret is a delivery mechanism for sensitive data, not by itself a complete enterprise secrets-management system.**

A mature Kubernetes security architecture combines:

```text
Secret Management
+
Encryption
+
RBAC
+
Workload Identity
+
Rotation
+
Audit
+
Runtime Security
```

This provides defense in depth for one of the most valuable assets in a Kubernetes environment:

```text
Credentials
```

---

## Next Chapter

# Chapter 54 – Image Security

Topics will include:

- Container Image Security
- Why Image Security Matters
- Container Image Lifecycle
- Trusted Base Images
- Minimal Images
- Image Registries
- Private Registries
- Image Pull Secrets
- Image Tags
- `latest` Tag Risks
- Immutable Image Digests
- Image Signing
- Cosign
- Sigstore
- Software Bill of Materials (SBOM)
- Image Vulnerability Scanning
- CVE Management
- Critical Vulnerabilities
- Dependency Security
- Base Image Updates
- Distroless Images
- Rootless Containers
- Image Provenance
- SLSA
- Supply Chain Attacks
- Admission-Based Image Policies
- Trusted Registries
- Registry Authentication
- ImagePullPolicy
- Image Verification
- Runtime Image Security
- Kubernetes Image Security Architecture
- CI/CD Image Security
- Image Promotion
- Production Image Governance
- Image Incident Response
- Troubleshooting
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---