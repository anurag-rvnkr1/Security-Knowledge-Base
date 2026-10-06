# Chapter 46 – Kubernetes Security Fundamentals

## Overview

Kubernetes security is not a single feature.

It is a **defense-in-depth security model** involving multiple layers:

```text
                    Kubernetes Security

                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Control Plane       Workloads         Network
          │                │                │
          ▼                ▼                ▼
    Authentication      Containers      NetworkPolicy
    Authorization       Pods            TLS
    API Security        Security        Segmentation
          │                │
          ▼                ▼
       Secrets         Runtime Security
          │                │
          └───────┬────────┘
                  ▼
             Monitoring
                  │
                  ▼
             Audit Logging
```

A Kubernetes environment can be attacked through:

```text
API Server
Worker Nodes
Containers
Images
Secrets
Network
RBAC
Service Accounts
Admission Controls
Supply Chain
Runtime
```

Therefore, Kubernetes security requires controls at every layer.

> **Kubernetes security is a defense-in-depth approach that protects the control plane, nodes, workloads, identities, network, data, and software supply chain.**

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes security model
- Defense in depth
- Control plane security
- Worker Node security
- Pod security
- Container security
- API Server security
- Authentication
- Authorization
- RBAC
- Service Accounts
- Secrets
- Network Policies
- Pod Security Standards
- Admission Control
- Security Contexts
- Linux capabilities
- Privileged containers
- Image security
- Runtime security
- Supply chain security
- Encryption
- Audit logging
- Security monitoring
- Common Kubernetes attack paths
- Security best practices
- Hands-on Labs
- Common mistakes
- Quick Revision
- Interview Questions

---

# Kubernetes Security Model

A Kubernetes cluster can be divided into several security boundaries:

```text
                    Kubernetes Cluster
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
      Control Plane       Nodes          External Users
          │                │                │
          ▼                ▼                ▼
      API Server         Kubelet         kubectl
      etcd               Runtime         Applications
      Scheduler          Pods
      Controllers
```

Each component requires different security controls.

---

# Security Layers

A practical Kubernetes security model includes:

```text
1. Infrastructure Security
2. Control Plane Security
3. API Security
4. Identity Security
5. Authorization
6. Workload Security
7. Container Security
8. Network Security
9. Data Security
10. Image Security
11. Runtime Security
12. Supply Chain Security
13. Monitoring and Auditing
```

---

# Defense in Depth

Defense in depth means:

```text
Do not depend on one security control.
```

Example:

```text
Attacker
   ↓
Network Firewall
   ↓
NetworkPolicy
   ↓
Authentication
   ↓
RBAC
   ↓
Admission Policy
   ↓
Pod Security
   ↓
Container Security
   ↓
Runtime Detection
```

If one layer fails, another layer can still reduce the impact.

---

# Example

Suppose an attacker compromises an application Pod.

Without defense in depth:

```text
Compromised Pod
     ↓
Access other Pods
     ↓
Access Secrets
     ↓
Access Kubernetes API
     ↓
Cluster compromise
```

With multiple controls:

```text
Compromised Pod
     ↓
NetworkPolicy blocks traffic
     ↓
RBAC limits API permissions
     ↓
Service Account has minimal privileges
     ↓
Pod Security prevents privileged operations
     ↓
Runtime monitoring detects suspicious behavior
```

The attacker has fewer opportunities to escalate.

---

# Shared Responsibility

Kubernetes security involves multiple parties.

In a self-managed cluster:

```text
Organization
    ↓
Responsible for:
Control Plane
Nodes
Network
Kubernetes Configuration
Applications
Images
Secrets
```

In a managed Kubernetes service:

```text
Cloud Provider
    ↓
Some infrastructure/control-plane responsibilities

Organization
    ↓
Workloads
Identity
RBAC
Network
Secrets
Applications
Configuration
```

The exact responsibility boundary depends on the platform.

---

# Control Plane Security

The Kubernetes control plane contains highly privileged components.

Important components include:

```text
API Server
etcd
Scheduler
Controller Manager
```

Compromise of the control plane can potentially compromise the entire cluster.

Therefore:

```text
Control Plane
    ↓
Highest Security Priority
```

---

# Kubernetes API Server

The API Server is the central entry point for Kubernetes API operations.

Clients interact with Kubernetes through:

```text
kubectl
Controllers
Operators
Applications
CI/CD Systems
```

Conceptually:

```text
User / Tool
     ↓
API Server
     ↓
Authentication
     ↓
Authorization
     ↓
Admission
     ↓
API Request
```

---

# API Security Pipeline

A simplified request flow:

```text
                API Request
                     │
                     ▼
              Authentication
                     │
                     ▼
               Authorization
                     │
                     ▼
               Admission
                     │
                     ▼
              API Validation
                     │
                     ▼
                  etcd
```

This is a fundamental Kubernetes security concept.

---

# Authentication

Authentication answers:

> **Who are you?**

Examples:

```text
User
Service Account
OIDC Identity
Certificate
Cloud Identity
```

Authentication comes before authorization.

---

# Authorization

Authorization answers:

> **What are you allowed to do?**

For example:

```text
User A

Can:
get Pods

Cannot:
delete Deployments
```

Kubernetes commonly uses:

```text
RBAC
```

for authorization.

---

# Authentication vs Authorization

| Concept | Question |
|---|---|
| Authentication | Who are you? |
| Authorization | What can you do? |

Example:

```text
Authentication:

I am Alice.
```

```text
Authorization:

Alice can read Pods
but cannot delete Nodes.
```

---

# RBAC

RBAC stands for:

```text
Role-Based Access Control
```

It controls access using:

```text
Subjects
+
Roles
+
Bindings
```

The basic model:

```text
User / ServiceAccount

        ↓

Role / ClusterRole

        ↓

RoleBinding / ClusterRoleBinding

        ↓

Permissions
```

---

# Principle of Least Privilege

One of the most important security principles is:

> **Give identities only the permissions they actually need.**

Bad:

```text
Application
    ↓
cluster-admin
```

Better:

```text
Application
    ↓
Read ConfigMaps
```

Only grant the required permission.

---

# Service Accounts

Pods commonly use:

```text
Service Accounts
```

to authenticate to Kubernetes APIs.

Example:

```yaml
serviceAccountName: app-sa
```

A Pod should not automatically receive broad Kubernetes permissions.

---

# Default Service Account

If no Service Account is explicitly configured, a Pod generally uses the namespace's:

```text
default
```

Service Account.

This does not mean the Pod should be granted additional privileges.

---

# Security Context

Kubernetes supports:

```text
SecurityContext
```

to control how containers and Pods execute.

Examples include:

```text
runAsUser
runAsGroup
runAsNonRoot
readOnlyRootFilesystem
allowPrivilegeEscalation
capabilities
seccompProfile
```

---

# Example Security Context

```yaml
securityContext:

  runAsNonRoot: true

  seccompProfile:

    type: RuntimeDefault
```

This tells Kubernetes that the container should run as a non-root user and use the runtime's default seccomp profile.

---

# Running as Non-Root

Containers should generally avoid running as:

```text
root
```

when unnecessary.

Example:

```yaml
securityContext:

  runAsNonRoot: true
```

This reduces the impact of some container-level compromises.

---

# Privileged Containers

A privileged container can receive extensive access to the underlying host.

Example:

```yaml
securityContext:

  privileged: true
```

This should be avoided unless there is a legitimate, well-understood requirement.

A compromised privileged container can present significantly greater risk to the Node.

---

# AllowPrivilegeEscalation

Example:

```yaml
securityContext:

  allowPrivilegeEscalation: false
```

This prevents a process from gaining more privileges than its parent process through mechanisms controlled by this setting.

Use it where compatible with the workload.

---

# Linux Capabilities

Linux capabilities divide some root privileges into separate units.

Examples include:

```text
NET_ADMIN
NET_RAW
SYS_ADMIN
CHOWN
SETUID
SETGID
```

Instead of giving a container broad privileges, capabilities can be selectively added or removed.

---

# Drop Capabilities

Example:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL
```

Then add only what the application requires.

Example:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL

    add:

    - NET_BIND_SERVICE
```

---

# Why Drop Capabilities?

Suppose an application only needs to bind to a low-numbered network port.

Instead of giving broad privileges:

```text
ALL
```

use the minimum required capability:

```text
NET_BIND_SERVICE
```

This follows:

```text
Least Privilege
```

---

# Read-Only Root Filesystem

Example:

```yaml
securityContext:

  readOnlyRootFilesystem: true
```

This prevents normal writes to the container's root filesystem.

If the application needs temporary storage, explicitly provide:

```text
emptyDir
```

or another appropriate volume.

---

# Example

```yaml
containers:

- name: app

  image: example/app:1.0

  securityContext:

    runAsNonRoot: true

    allowPrivilegeEscalation: false

    readOnlyRootFilesystem: true

    capabilities:

      drop:

      - ALL
```

This is a useful baseline for many applications, subject to application compatibility.

---

# Seccomp

Seccomp stands for:

```text
Secure Computing
```

It restricts the system calls that a process can make.

Kubernetes supports:

```text
Seccomp profiles
```

Example:

```yaml
securityContext:

  seccompProfile:

    type: RuntimeDefault
```

---

# AppArmor

On supported Linux systems, AppArmor can restrict application behavior.

It can provide an additional security layer around container processes.

Availability depends on:

```text
Operating System
Container Runtime
Kubernetes Environment
```

---

# SELinux

SELinux provides mandatory access control on supported Linux systems.

It can restrict what processes can access even when traditional Unix permissions would otherwise allow it.

---

# Container Isolation

Containers are not equivalent to virtual machines.

Containers generally share:

```text
Host Kernel
```

Therefore:

```text
Container Security
+
Kernel Security
```

are both important.

---

# Container Escape

A container escape occurs when an attacker moves from:

```text
Container
```

to:

```text
Host
```

Potential risk factors include:

```text
Privileged containers
Dangerous capabilities
Host mounts
Kernel vulnerabilities
Weak runtime configuration
```

Defense includes:

```text
Non-root containers
Capability dropping
Seccomp
Pod Security
Runtime hardening
Kernel patching
```

---

# HostPath

`hostPath` mounts a path from the Node filesystem into a Pod.

Example:

```yaml
volumes:

- name: host-data

  hostPath:

    path: /var/lib/example
```

This can expose host resources to the container.

Use `hostPath` only when necessary and restrict access carefully.

---

# Host Network

A Pod can use:

```yaml
hostNetwork: true
```

This causes the Pod to use the Node's network namespace.

It reduces network isolation and should only be used when required.

---

# Host PID

Example:

```yaml
hostPID: true
```

This allows the Pod to share the host process namespace.

This can expose host process information and should be carefully restricted.

---

# Host IPC

Example:

```yaml
hostIPC: true
```

This shares the host IPC namespace.

Again:

```text
Use only when necessary.
```

---

# Network Security

Kubernetes networking should follow:

```text
Default Deny
+
Explicit Allow
```

where appropriate.

NetworkPolicies can restrict:

```text
Ingress
Egress
```

between Pods and external destinations.

---

# Example Network Policy

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: deny-all

spec:

  podSelector: {}

  policyTypes:

  - Ingress

  - Egress
```

This establishes a default-deny policy for selected Pods, subject to the capabilities of the installed CNI implementation.

---

# Network Segmentation

Example architecture:

```text
Internet
   │
   ▼
Frontend
   │
   ▼
Backend
   │
   ▼
Database
```

NetworkPolicy can enforce:

```text
Frontend → Backend
Backend → Database
```

while blocking:

```text
Frontend → Database
```

---

# Secrets

Kubernetes provides:

```text
Secret
```

objects for sensitive configuration.

Examples:

```text
Passwords
API Keys
Tokens
Certificates
```

However:

> **Kubernetes Secrets should not automatically be treated as equivalent to a dedicated secrets-management system.**

Storage encryption and access control should be configured appropriately.

---

# Secret Access

An attacker who obtains sufficient RBAC permissions may be able to retrieve Secrets.

Therefore:

```text
Secret Security
=
RBAC
+
Encryption
+
Access Control
+
Monitoring
```

---

# Encryption at Rest

Sensitive Kubernetes data can be encrypted at rest.

For example:

```text
Secrets
```

can be protected using encryption mechanisms configured for the Kubernetes API storage layer.

In many Kubernetes installations:

```text
etcd
```

stores API objects.

---

# etcd Security

`etcd` contains critical cluster state.

It may contain:

```text
Secrets
Pods
Deployments
ConfigMaps
RBAC Objects
Cluster Configuration
```

Therefore:

```text
etcd compromise
=
Potential cluster compromise
```

Protect it with:

```text
Network restrictions
TLS
Authentication
Encryption at rest
Backups
Access controls
```

---

# API Server TLS

Kubernetes components communicate using secure channels where configured.

TLS helps protect:

```text
Confidentiality
Integrity
Authentication
```

Certificates are an important part of Kubernetes security.

---

# Kubelet Security

The Kubelet runs on worker Nodes and communicates with the control plane.

Kubelet security includes:

```text
Authentication
Authorization
TLS
Network exposure
Configuration
```

The Kubelet should not be unnecessarily exposed to untrusted networks.

---

# Node Security

Worker Nodes should be hardened.

Important areas:

```text
Operating System
Kernel
Container Runtime
Kubelet
Filesystem
SSH Access
Network
Packages
Credentials
```

---

# Node Hardening

Typical controls include:

```text
Minimal OS
Regular patching
Restricted SSH
Firewalling
Least privilege
Runtime hardening
Disk encryption
Monitoring
```

---

# Container Runtime

Kubernetes uses a container runtime to execute containers.

Examples include runtimes compatible with the Kubernetes Container Runtime Interface.

Runtime security matters because:

```text
Kubernetes
    ↓
Container Runtime
    ↓
Linux Kernel
```

A runtime vulnerability can affect workload isolation.

---

# Image Security

A secure image lifecycle includes:

```text
Trusted Base Image
      ↓
Dependency Scanning
      ↓
Vulnerability Scanning
      ↓
Image Signing
      ↓
Registry
      ↓
Admission Verification
      ↓
Deployment
```

---

# Image Sources

Avoid blindly deploying:

```text
Unknown Images
```

Prefer:

```text
Trusted Registries
Verified Images
Pinned Versions
Signed Images
```

---

# Image Tags

Avoid relying solely on:

```text
latest
```

Example:

```yaml
image: nginx:latest
```

Better:

```yaml
image: nginx:1.30.1
```

For stronger reproducibility, image digests can be used:

```yaml
image: nginx@sha256:<digest>
```

---

# Why Pin Images?

Mutable tags can change.

For example:

```text
myapp:latest
```

could refer to different image contents at different times.

A digest identifies a specific image content.

---

# Supply Chain Security

A Kubernetes workload depends on:

```text
Source Code
   ↓
Dependencies
   ↓
Build System
   ↓
Container Image
   ↓
Registry
   ↓
Kubernetes
```

An attacker can target any stage.

Therefore security should cover the complete software supply chain.

---

# Admission Control

Admission controllers intercept API requests after authorization and before persistence.

They can:

```text
Validate
Mutate
Reject
```

workloads.

Examples of security controls include:

```text
Pod Security Admission
Policy Engines
Image Verification
Custom Admission Webhooks
```

---

# Pod Security Standards

Kubernetes defines Pod Security Standards with levels such as:

```text
Privileged
Baseline
Restricted
```

They help define security expectations for Pod configurations.

---

# Privileged

The:

```text
Privileged
```

profile is intentionally permissive.

It is generally used for workloads requiring elevated privileges.

---

# Baseline

The:

```text
Baseline
```

profile prevents many known privilege-escalation patterns while allowing a broader range of workloads than Restricted.

---

# Restricted

The:

```text
Restricted
```

profile applies stronger hardening requirements.

It is appropriate for workloads where strong Pod isolation is desired and application compatibility permits it.

---

# Namespace Security

Security policies can be applied at namespace boundaries.

Example:

```text
production
staging
development
```

You can apply different controls to different environments.

---

# Example

```text
production
    ↓
Restricted

staging
    ↓
Baseline

development
    ↓
More permissive
```

The exact policy should be based on organizational requirements.

---

# RBAC Security

RBAC should follow:

```text
Least Privilege
```

Avoid:

```text
cluster-admin
```

unless genuinely required.

Prefer:

```text
Namespace-specific Role
```

over:

```text
ClusterRole
```

when possible.

---

# Namespace Isolation

Namespaces provide organizational and administrative separation.

They are useful for:

```text
Environment Separation
Team Separation
Resource Organization
RBAC Scoping
```

However:

> **Namespaces are not complete security boundaries by themselves.**

Combine them with:

```text
RBAC
NetworkPolicy
Pod Security
ResourceQuota
Admission Policies
```

---

# Service Account Token Security

Applications should only receive Kubernetes API credentials when required.

Where possible:

```text
Disable unnecessary API access
```

and:

```text
Use dedicated Service Accounts
```

instead of sharing identities.

---

# Automounting Service Account Tokens

Example:

```yaml
automountServiceAccountToken: false
```

If an application does not need to communicate with the Kubernetes API, disabling automatic token mounting can reduce exposure.

---

# Security Context Example

A hardened Pod might include:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: secure-app

spec:

  automountServiceAccountToken: false

  securityContext:

    runAsNonRoot: true

    seccompProfile:

      type: RuntimeDefault

  containers:

  - name: app

    image: example/app:1.0

    securityContext:

      allowPrivilegeEscalation: false

      readOnlyRootFilesystem: true

      capabilities:

        drop:

        - ALL
```

The exact configuration must be adapted to application requirements.

---

# Security Context Checklist

For each workload, consider:

```text
☑ runAsNonRoot
☑ runAsUser
☑ runAsGroup
☑ allowPrivilegeEscalation
☑ capabilities
☑ readOnlyRootFilesystem
☑ seccompProfile
☑ privileged
☑ hostNetwork
☑ hostPID
☑ hostIPC
```

---

# Runtime Security

Runtime security detects suspicious activity after workloads are running.

Examples:

```text
Unexpected Shell
Process Execution
Privilege Escalation
Suspicious Network Connections
Unexpected File Access
Container Escape Attempts
```

Runtime security tools can observe:

```text
Process
System Calls
Network
Filesystem
```

---

# Monitoring

Security monitoring should cover:

```text
API Requests
Authentication
RBAC Changes
Pod Creation
Secret Access
Node Events
Network Traffic
Runtime Activity
```

---

# Audit Logging

Kubernetes Audit Logging records API activity.

Example:

```text
User Alice
    ↓
GET Secret
    ↓
API Server
    ↓
Audit Event
```

Audit logs can help answer:

```text
Who performed the action?
What action occurred?
When did it happen?
Which resource was affected?
From where?
```

---

# Audit Security Events

High-value events include:

```text
RoleBinding creation
ClusterRoleBinding creation
Secret access
ServiceAccount changes
Pod creation
Privileged Pod creation
Admission failures
Node changes
```

---

# Incident Example

Suppose an attacker obtains credentials for:

```text
Service Account
```

They attempt:

```text
get secrets
```

If RBAC denies the action:

```text
Request blocked
```

If audit logging is enabled:

```text
Attempt recorded
```

Security monitoring can then generate an alert.

---

# Common Kubernetes Attack Paths

A simplified attack chain:

```text
Initial Access
      ↓
Compromise Application
      ↓
Container Access
      ↓
Service Account Token
      ↓
Kubernetes API
      ↓
RBAC Abuse
      ↓
Secret Access
      ↓
Privilege Escalation
      ↓
Node / Cluster Impact
```

Security controls should disrupt the chain at multiple stages.

---

# Attack Path: Excessive RBAC

Bad configuration:

```text
Application ServiceAccount
        ↓
cluster-admin
```

If the application is compromised:

```text
Attacker
   ↓
ServiceAccount
   ↓
cluster-admin
   ↓
Cluster-wide access
```

Better:

```text
Application
   ↓
Dedicated ServiceAccount
   ↓
Minimal Role
   ↓
Only required resources
```

---

# Attack Path: Privileged Container

Bad configuration:

```text
privileged: true
```

combined with other host-access mechanisms can dramatically increase the impact of a container compromise.

Use privileged workloads only when necessary.

---

# Attack Path: Exposed Kubelet

An improperly secured Kubelet can expose sensitive Node-level capabilities.

Therefore:

```text
Kubelet
+
Network Exposure
+
Authentication
+
Authorization
```

must be carefully configured.

---

# Attack Path: Malicious Image

```text
Malicious Image
      ↓
Registry
      ↓
Kubernetes
      ↓
Pod
      ↓
Malicious Code
```

Defenses:

```text
Trusted Registry
Image Scanning
Signing
Verification
Admission Policies
SBOM
```

---

# Attack Path: Secret Exposure

```text
Application
      ↓
Secret
      ↓
Logs / Environment / Files
      ↓
Credential Exposure
```

Secrets should not be unnecessarily:

```text
Logged
Hardcoded
Embedded in Images
Shared
```

---

# Security Monitoring Architecture

```text
                Kubernetes Cluster
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼
    API Logs       Runtime Events   Network Events
       │               │               │
       └───────────────┼───────────────┘
                       ▼
                 SIEM / Platform
                       │
                       ▼
                    Detection
                       │
                       ▼
                     Alert
                       │
                       ▼
                  Incident Response
```

---

# Security Baseline

A Kubernetes security baseline should consider:

```text
Control Plane
Nodes
API Server
Authentication
RBAC
Service Accounts
Secrets
Network Policies
Pod Security
Container Runtime
Images
Admission
Audit Logs
Monitoring
Backups
```

---

# Production Security Checklist

## Control Plane

```text
☑ Secure API Server
☑ Protect etcd
☑ TLS
☑ Restrict administrative access
☑ Enable auditing
```

---

## Identity

```text
☑ Strong authentication
☑ Least-privilege RBAC
☑ Dedicated Service Accounts
☑ Avoid cluster-admin
```

---

## Workloads

```text
☑ Non-root
☑ No unnecessary privileges
☑ Drop capabilities
☑ Seccomp
☑ Read-only filesystem where possible
☑ Avoid host namespaces
```

---

## Network

```text
☑ Network segmentation
☑ NetworkPolicy
☑ Restrict ingress
☑ Restrict egress
☑ Encrypt sensitive traffic
```

---

## Images

```text
☑ Trusted registry
☑ Vulnerability scanning
☑ Pinned versions
☑ Image signing
☑ Admission verification
```

---

## Secrets

```text
☑ Encrypt at rest
☑ Restrict access
☑ Rotate credentials
☑ Avoid hardcoding
☑ Monitor access
```

---

## Runtime

```text
☑ Runtime monitoring
☑ Suspicious process detection
☑ Container escape detection
☑ Node monitoring
```

---

# Hands-on Lab 1 – Create Secure Pod

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: secure-pod

spec:

  automountServiceAccountToken: false

  securityContext:

    runAsNonRoot: true

    seccompProfile:

      type: RuntimeDefault

  containers:

  - name: app

    image: nginx:1.30

    securityContext:

      allowPrivilegeEscalation: false

      readOnlyRootFilesystem: true

      capabilities:

        drop:

        - ALL
```

Apply:

```bash
kubectl apply -f secure-pod.yaml
```

Observe whether the application functions correctly.

> A read-only root filesystem may require additional writable volumes for some applications.

---

# Hands-on Lab 2 – Inspect Security Context

Run:

```bash
kubectl get pod secure-pod -o yaml
```

Inspect:

```text
securityContext
```

and:

```text
automountServiceAccountToken
```

---

# Hands-on Lab 3 – Inspect Service Accounts

Run:

```bash
kubectl get serviceaccounts
```

Then:

```bash
kubectl describe serviceaccount default
```

---

# Hands-on Lab 4 – Create Dedicated Service Account

```yaml
apiVersion: v1

kind: ServiceAccount

metadata:

  name: app-sa
```

Apply:

```bash
kubectl apply -f serviceaccount.yaml
```

Use it:

```yaml
spec:

  serviceAccountName: app-sa
```

---

# Hands-on Lab 5 – Inspect RBAC

Run:

```bash
kubectl get roles
```

```bash
kubectl get rolebindings
```

```bash
kubectl get clusterroles
```

```bash
kubectl get clusterrolebindings
```

---

# Hands-on Lab 6 – NetworkPolicy

Create a default-deny policy:

```yaml
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: default-deny

spec:

  podSelector: {}

  policyTypes:

  - Ingress

  - Egress
```

Apply:

```bash
kubectl apply -f default-deny.yaml
```

Test connectivity in a disposable namespace.

---

# Hands-on Lab 7 – Test Pod Security

Create a namespace:

```bash
kubectl create namespace security-lab
```

Apply a Pod Security Standard label appropriate for the lab.

For example:

```bash
kubectl label namespace security-lab \
  pod-security.kubernetes.io/enforce=restricted
```

Attempt to deploy a Pod that violates Restricted requirements.

Observe the admission response.

---

# Hands-on Lab 8 – Audit RBAC

Create a read-only Role:

```yaml
apiVersion: rbac.authorization.k8s.io/v1

kind: Role

metadata:

  name: pod-reader

rules:

- apiGroups:

  - ""

  resources:

  - pods

  verbs:

  - get

  - list

  - watch
```

Create a RoleBinding for a test Service Account.

Then test:

```bash
kubectl auth can-i get pods \
  --as=system:serviceaccount:security-lab:app-sa
```

---

# `kubectl auth can-i`

This is an important security troubleshooting command.

Example:

```bash
kubectl auth can-i get pods
```

Check a Service Account:

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:security-lab:app-sa
```

Expected output:

```text
yes
```

or:

```text
no
```

---

# Hands-on Lab 9 – Test Least Privilege

Allow:

```text
get/list/watch Pods
```

but do not allow:

```text
delete Pods
```

Test:

```bash
kubectl auth can-i delete pods \
  --as=system:serviceaccount:security-lab:app-sa
```

Expected:

```text
no
```

This demonstrates:

```text
Least Privilege
```

---

# Troubleshooting

## Pod Rejected by Security Policy

Check:

```bash
kubectl describe pod <pod>
```

Also inspect:

```bash
kubectl get namespace <namespace> -o yaml
```

Look for Pod Security labels.

---

# Container Cannot Start as Non-Root

Possible causes:

```text
Application expects UID 0
```

```text
Filesystem permissions
```

```text
Image configured for root
```

Fix the image or configure an appropriate non-root UID.

---

# Read-Only Filesystem Failure

An application may attempt:

```text
Write /tmp
Write application cache
Write logs
Write runtime files
```

Use an explicit writable volume where appropriate.

Example:

```yaml
volumes:

- name: tmp

  emptyDir: {}
```

Mount it:

```yaml
volumeMounts:

- name: tmp

  mountPath: /tmp
```

---

# NetworkPolicy Does Not Work

Possible causes:

```text
CNI does not implement NetworkPolicy
```

or:

```text
Policy selector is incorrect
```

or:

```text
Ingress/Egress policy is incomplete
```

Check:

```bash
kubectl get networkpolicy
```

---

# RBAC Permission Denied

Error:

```text
Forbidden
```

Check:

```bash
kubectl auth can-i ...
```

Inspect:

```bash
kubectl get role
kubectl get rolebinding
```

and:

```bash
kubectl describe rolebinding <name>
```

---

# Secret Access Denied

Check:

```text
ServiceAccount
Role
RoleBinding
Namespace
```

Remember:

```text
Role
```

is namespace-scoped.

```text
ClusterRole
```

can define cluster-scoped permissions.

---

# Common Mistakes

## 1. Running Everything as Root

Avoid:

```text
runAsUser: 0
```

unless explicitly required.

---

## 2. Giving cluster-admin to Applications

Avoid:

```text
cluster-admin
```

for ordinary workloads.

---

## 3. Ignoring NetworkPolicy

Without network restrictions, a compromised Pod may have broader network reach than necessary.

---

## 4. Trusting Container Images

Do not assume an image is safe because it is publicly available.

---

## 5. Using `latest`

Prefer immutable versioning or digests.

---

## 6. Mounting the Host Filesystem

Avoid unnecessary:

```text
hostPath
```

mounts.

---

## 7. Using Privileged Containers

Use:

```yaml
privileged: true
```

only when justified.

---

## 8. Leaving Service Account Tokens Unnecessary

If an application does not need Kubernetes API access:

```yaml
automountServiceAccountToken: false
```

can reduce exposure.

---

## 9. Ignoring etcd Security

etcd contains highly sensitive cluster state.

---

## 10. Assuming Namespaces Provide Complete Isolation

Namespaces are useful organizational and security scopes, but they are not complete isolation boundaries.

Combine them with:

```text
RBAC
NetworkPolicy
Pod Security
Admission Controls
```

---

## 11. Ignoring Audit Logs

Without auditing, investigating suspicious API activity becomes harder.

---

## 12. Overlooking the Node

A secure Pod does not compensate for an insecure host.

---

# Best Practices

### 1. Follow Defense in Depth

Use multiple independent security layers.

---

### 2. Apply Least Privilege

Minimize:

```text
RBAC Permissions
Linux Capabilities
Network Access
Filesystem Access
API Access
```

---

### 3. Run Containers as Non-Root

Where compatible:

```yaml
runAsNonRoot: true
```

---

### 4. Drop Unnecessary Capabilities

Start with:

```yaml
capabilities:

  drop:

  - ALL
```

and add only required capabilities.

---

### 5. Disable Privilege Escalation

Where appropriate:

```yaml
allowPrivilegeEscalation: false
```

---

### 6. Use Seccomp

Prefer:

```yaml
seccompProfile:

  type: RuntimeDefault
```

or a stricter custom profile when appropriate.

---

### 7. Restrict Network Communication

Use:

```text
NetworkPolicy
```

to implement segmentation.

---

### 8. Secure Secrets

Use:

```text
Encryption
RBAC
Rotation
External Secret Management
```

where appropriate.

---

### 9. Scan and Sign Images

Implement:

```text
Image Scanning
Image Signing
Verification
SBOM
```

in the software supply chain.

---

### 10. Enable Auditing

Record security-sensitive Kubernetes API operations.

---

### 11. Harden Nodes

Keep:

```text
OS
Kernel
Runtime
Kubelet
```

patched and restricted.

---

### 12. Monitor Runtime Behavior

Detect:

```text
Unexpected processes
Privilege escalation
Suspicious network connections
Container escape attempts
```

---

# Security Maturity Model

A useful way to think about Kubernetes security maturity:

```text
Level 1
Basic Access Control

↓

Level 2
RBAC + Secrets + NetworkPolicy

↓

Level 3
Pod Security + Image Security

↓

Level 4
Admission + Runtime Security + Auditing

↓

Level 5
Supply Chain Security + Continuous Detection + Response
```

---

# Kubernetes Security Architecture

A mature environment can look like:

```text
                         Users
                           │
                           ▼
                    Identity Provider
                           │
                           ▼
                     API Server
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   Authentication      Authorization      Admission
                           │                │
                           ▼                ▼
                          RBAC       Security Policies
                           │                │
                           └────────┬───────┘
                                    ▼
                                  etcd
                                    │
                                    ▼
                              Kubernetes State
                                    │
                 ┌──────────────────┼──────────────────┐
                 ▼                  ▼                  ▼
               Nodes              Network           Secrets
                 │                  │                  │
                 ▼                  ▼                  ▼
             Containers      NetworkPolicy       Encryption
                 │
                 ▼
          Runtime Security
                 │
                 ▼
             Monitoring
                 │
                 ▼
                SIEM
```

---

# Security Incident Example

Suppose an attacker compromises a web application.

Initial position:

```text
Web Pod
```

The attacker attempts to access:

```text
Kubernetes API
```

But:

```text
automountServiceAccountToken = false
```

The Pod has no unnecessary API credential.

Next, the attacker attempts:

```text
Backend connection
```

NetworkPolicy blocks unauthorized traffic.

Next, the attacker tries:

```text
Privilege escalation
```

The container has:

```text
runAsNonRoot
allowPrivilegeEscalation=false
drop ALL capabilities
```

Runtime monitoring detects suspicious behavior.

This demonstrates:

```text
Defense in Depth
```

---

# Security Incident Response Flow

```text
Detection
   ↓
Validation
   ↓
Containment
   ↓
Eradication
   ↓
Recovery
   ↓
Lessons Learned
```

Kubernetes security operations will be covered in greater depth in the later:

```text
Module 10 — Kubernetes Security Operations
```

---

# Quick Revision

## Authentication

```text
Who are you?
```

---

## Authorization

```text
What can you do?
```

---

## RBAC

```text
Controls permissions
```

---

## Service Account

```text
Identity used by workloads
```

---

## Security Context

```text
Controls container/Pod execution security
```

---

## NetworkPolicy

```text
Controls Pod network traffic
```

---

## Pod Security Standards

```text
Privileged
Baseline
Restricted
```

---

## Seccomp

```text
Restricts system calls
```

---

## Linux Capabilities

```text
Fine-grained privileges
```

---

## Secrets

```text
Sensitive configuration
```

---

## Admission

```text
Validate / Mutate / Reject API requests
```

---

## Audit Logging

```text
Records Kubernetes API activity
```

---

## Defense in Depth

```text
Multiple security layers
```

---

# Essential kubectl Security Commands

Check current identity:

```bash
kubectl auth whoami
```

Check permissions:

```bash
kubectl auth can-i get pods
```

Check Service Account permissions:

```bash
kubectl auth can-i get secrets \
  --as=system:serviceaccount:default:default
```

List Service Accounts:

```bash
kubectl get serviceaccounts
```

List Roles:

```bash
kubectl get roles
```

List RoleBindings:

```bash
kubectl get rolebindings
```

List ClusterRoles:

```bash
kubectl get clusterroles
```

List ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

List NetworkPolicies:

```bash
kubectl get networkpolicies
```

List Secrets:

```bash
kubectl get secrets
```

List Pod Security labels:

```bash
kubectl get namespace --show-labels
```

Inspect Pod security:

```bash
kubectl get pod <name> -o yaml
```

View events:

```bash
kubectl get events --sort-by=.lastTimestamp
```

---

# Interview Questions

## Basic

- What is Kubernetes security?
- What is defense in depth?
- What is the difference between authentication and authorization?
- What is RBAC?
- What is a Service Account?
- What is a SecurityContext?
- What is a NetworkPolicy?
- What are Kubernetes Secrets?
- What are Pod Security Standards?
- What is a privileged container?

---

## Intermediate

- Explain the Kubernetes API request security flow.
- What is the difference between Role and ClusterRole?
- What is the difference between RoleBinding and ClusterRoleBinding?
- Why should applications not use `cluster-admin`?
- Why should containers run as non-root?
- What is `allowPrivilegeEscalation`?
- What are Linux capabilities?
- Why should capabilities be dropped?
- What is seccomp?
- What is the purpose of `readOnlyRootFilesystem`?
- What is the purpose of `automountServiceAccountToken: false`?
- How does NetworkPolicy improve Kubernetes security?
- What are the Pod Security Standard levels?

---

## Advanced

- Explain the complete Kubernetes API security pipeline.
- How would you secure a Kubernetes cluster against container escape?
- How would you implement least privilege for workloads?
- How would you secure the Kubernetes control plane?
- Why is etcd a high-value security target?
- How would you secure Kubernetes Secrets?
- How would you investigate suspicious API activity?
- How can a compromised Pod be prevented from accessing other Pods?
- How can you prevent unnecessary Kubernetes API access from workloads?
- How would you design defense in depth for a production Kubernetes cluster?
- Explain the relationship between RBAC, Service Accounts, and Pods.
- How would you secure container images throughout the supply chain?
- What security risks are associated with privileged containers?
- What are host namespaces and why are they dangerous?
- How would you detect a compromised Kubernetes workload?
- How would you reduce the blast radius after a Pod compromise?
- How do namespaces contribute to security, and why are they not sufficient by themselves?
- What Kubernetes components should be included in a security monitoring strategy?

---

# Security Interview Scenario

### Question

> A web application Pod has been compromised. How would you prevent the attacker from taking over the Kubernetes cluster?

### Answer Structure

Start with:

```text
1. Reduce Pod privileges
```

Use:

```text
runAsNonRoot
allowPrivilegeEscalation=false
drop capabilities
seccomp
```

Then:

```text
2. Restrict API access
```

Use:

```text
Dedicated ServiceAccount
Least-privilege RBAC
Disable unnecessary token mounting
```

Then:

```text
3. Restrict Network
```

Use:

```text
NetworkPolicy
```

Then:

```text
4. Secure the Node
```

Use:

```text
OS hardening
Kernel patching
Runtime security
```

Then:

```text
5. Secure Images
```

Use:

```text
Scanning
Signing
Verification
Pinned versions
```

Then:

```text
6. Monitor
```

Use:

```text
Audit Logs
Runtime Detection
Network Monitoring
SIEM
```

The overall objective is:

```text
Compromised Pod

       ↓

Limited Privileges

       ↓

Limited API Access

       ↓

Limited Network Access

       ↓

Limited Host Access

       ↓

Detection

       ↓

Containment
```

---

# Recommended Practice

1. Create a dedicated security-testing namespace.
2. Inspect default Service Accounts.
3. Create a dedicated Service Account.
4. Create a least-privilege Role.
5. Create a RoleBinding.
6. Test permissions using `kubectl auth can-i`.
7. Create a secure Pod using SecurityContext.
8. Test `runAsNonRoot`.
9. Test capability dropping.
10. Test `allowPrivilegeEscalation: false`.
11. Test `readOnlyRootFilesystem`.
12. Test `automountServiceAccountToken: false`.
13. Configure a default-deny NetworkPolicy.
14. Create explicit allow rules.
15. Apply Pod Security Standards.
16. Test privileged Pod rejection.
17. Inspect Kubernetes Secrets.
18. Study audit logging.
19. Scan container images.
20. Practice identifying Kubernetes attack paths.
21. Build a defense-in-depth architecture.
22. Document security controls and their purpose.

---

# References

## Official Kubernetes Documentation

- Kubernetes Security
- Kubernetes API Authentication
- Kubernetes Authorization
- RBAC Authorization
- Service Accounts
- Security Contexts
- Pod Security Standards
- Network Policies
- Secrets
- Admission Controllers
- Kubernetes Auditing
- Container Runtime Security
- Node Security
- Encrypting Confidential Data at Rest

---

## Kubernetes Security Resources

- Kubernetes SIG Security
- Kubernetes Security Checklist
- Kubernetes Threat Model
- Kubernetes Documentation

---

## Cloud Native Security

- Cloud Native Computing Foundation (CNCF)
- Cloud Native Security
- Kubernetes Security SIG

---

# Chapter Summary

Kubernetes security is a **multi-layer defense-in-depth problem**.

The major security layers are:

```text
Infrastructure
     ↓
Control Plane
     ↓
API
     ↓
Identity
     ↓
RBAC
     ↓
Admission
     ↓
Pod Security
     ↓
Container Security
     ↓
Network Security
     ↓
Secret Security
     ↓
Runtime Security
     ↓
Monitoring
```

The Kubernetes API request flow can be simplified as:

```text
Request
   ↓
Authentication
   ↓
Authorization
   ↓
Admission
   ↓
Validation
   ↓
Persistence
```

Remember:

```text
Authentication
=
Who are you?
```

```text
Authorization
=
What can you do?
```

RBAC provides authorization using:

```text
Role
ClusterRole
RoleBinding
ClusterRoleBinding
```

Workloads should use:

```text
Dedicated Service Accounts
```

with:

```text
Least Privilege
```

Pods should be hardened using:

```text
runAsNonRoot
allowPrivilegeEscalation=false
capability dropping
seccomp
readOnlyRootFilesystem
```

where compatible with the application.

Network security should use:

```text
NetworkPolicy
```

to limit unnecessary communication.

Sensitive data should be protected using:

```text
Secrets
RBAC
Encryption at Rest
Credential Rotation
External Secret Management
```

Container security should include:

```text
Trusted Images
Vulnerability Scanning
Image Signing
Digest Pinning
Admission Verification
```

Runtime security should monitor:

```text
Processes
System Calls
Network Activity
Filesystem Activity
Privilege Escalation
Container Escape Attempts
```

And Kubernetes API activity should be captured through:

```text
Audit Logging
```

The central security principle is:

> **Never rely on a single security control. Assume one layer can fail and design the remaining layers to limit the attacker's blast radius.**

A secure Kubernetes workload should therefore aim for:

```text
                    Secure Workload

                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
     Identity          Runtime          Network
        │                │                │
        ▼                ▼                ▼
      RBAC          SecurityContext   NetworkPolicy
        │                │                │
        └────────────────┼────────────────┘
                         ▼
                  Defense in Depth
                         │
                         ▼
                    Monitoring
                         │
                         ▼
                    Detection
```

The ultimate objective is not simply:

```text
Prevent every attack
```

but:

```text
Prevent
+
Limit
+
Detect
+
Respond
+
Recover
```

This foundation will be used throughout the remaining Kubernetes security chapters.

---

## Next Chapter

# Chapter 47 – Authentication

Topics will include:

- What is Authentication?
- Kubernetes Identity Model
- Authentication vs Authorization
- API Server Authentication
- Client Certificates
- Bearer Tokens
- Service Account Authentication
- OIDC
- External Identity Providers
- Cloud Identity
- Authentication Webhooks
- Anonymous Requests
- Authentication Configuration
- `kubeconfig`
- Client Credentials
- Certificate-Based Authentication
- Service Account Tokens
- Bound Service Account Tokens
- Token Projection
- TokenRequest API
- OIDC Authentication
- Identity Providers
- Authentication Security Best Practices
- Authentication Troubleshooting
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---