# Chapter 51 – Pod Security Standards

## Overview

Kubernetes workloads run inside Pods, and Pods can potentially access sensitive host and cluster resources.

For example, an overly privileged Pod may be configured with:

```yaml
securityContext:

  privileged: true
```

or:

```yaml
hostNetwork: true
```

or:

```yaml
hostPID: true
```

Such configurations can significantly increase the impact of a compromised workload.

Kubernetes provides:

```text
Pod Security Standards (PSS)
```

to define security requirements for Pods.

These standards are enforced by:

```text
Pod Security Admission (PSA)
```

The three Pod Security Standards are:

```text
Privileged
Baseline
Restricted
```

---

# Learning Objectives

After completing this chapter, you will understand:

- What Pod Security Standards are
- Why Pod Security matters
- Pod Security Admission
- Privileged profile
- Baseline profile
- Restricted profile
- Pod Security levels
- Namespace labels
- `enforce`
- `audit`
- `warn`
- SecurityContext
- Running as non-root
- Linux capabilities
- Privileged containers
- Host networking
- Host PID
- Host IPC
- HostPath
- Seccomp
- AppArmor
- SELinux
- `allowPrivilegeEscalation`
- Read-only root filesystem
- Namespace isolation
- Security policy design
- Pod Security migration
- Production hardening
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Are Pod Security Standards?

Pod Security Standards define security requirements for Pods.

They provide three policy levels:

```text
Privileged
Baseline
Restricted
```

The levels progressively increase security restrictions.

Conceptually:

```text
                    Security
                       ↑
                       │
                 Restricted
                       │
                   Baseline
                       │
                  Privileged
                       │
                       └──────────────→ Flexibility
```

---

# Why Pod Security Matters

A compromised application should have as little ability as possible to:

```text
Access the host
Escalate privileges
Access sensitive files
Interact with other workloads
Modify kernel behavior
Access host processes
```

Pod security reduces the attack surface.

---

# Pod Security Architecture

```text
Developer
    │
    ▼
Pod Manifest
    │
    ▼
Kubernetes API Server
    │
    ▼
Pod Security Admission
    │
    ▼
Pod Security Standard
    │
 ┌──┴───────────────┐
 ▼                  ▼
Allowed           Rejected
 │
 ▼
Pod Created
```

---

# Pod Security Admission

Pod Security Admission is a built-in Kubernetes admission mechanism that enforces Pod Security Standards.

It works primarily at the namespace level through labels.

Example:

```yaml
metadata:

  labels:

    pod-security.kubernetes.io/enforce: restricted
```

This means Pods in the namespace must satisfy the:

```text
Restricted
```

profile for enforcement.

---

# Pod Security Levels

There are three levels:

```text
1. Privileged
2. Baseline
3. Restricted
```

---

# Privileged

The:

```text
Privileged
```

level is intentionally permissive.

It allows many configurations that are restricted by the other profiles.

Typical use cases may include:

```text
System-level workloads
Infrastructure agents
Certain networking components
Specialized node-management workloads
```

It should not be selected merely for convenience.

---

# Baseline

The:

```text
Baseline
```

profile prevents many known privilege-escalation configurations while allowing common application workloads.

It is a practical security baseline for many environments.

---

# Restricted

The:

```text
Restricted
```

profile provides stronger security restrictions.

It is designed for workloads that can operate under strict security requirements.

Typical requirements include:

```text
Non-root execution
Restricted capabilities
Seccomp
No privilege escalation
Safer volume usage
```

---

# Comparison

| Profile | Security | Flexibility | Typical Use |
|---|---|---|---|
| Privileged | Lowest | Highest | System workloads |
| Baseline | Medium | Medium | General workloads |
| Restricted | Highest | Lowest | Security-sensitive workloads |

---

# Pod Security Modes

Pod Security Admission supports three modes:

```text
enforce
audit
warn
```

These can be configured independently.

---

# `enforce`

Violating Pods are rejected.

Example:

```yaml
metadata:

  labels:

    pod-security.kubernetes.io/enforce: restricted
```

If a Pod violates the Restricted profile:

```text
Admission
   ↓
Violation
   ↓
Request rejected
```

---

# `audit`

Violations are recorded in audit information.

The Pod may still be admitted.

Conceptually:

```text
Pod
 ↓
Policy violation
 ↓
Audit event
 ↓
Pod may continue
```

---

# `warn`

The user receives a warning.

Example:

```text
Warning:
would violate PodSecurity "restricted"
```

The request can still succeed if no enforcing policy rejects it.

---

# Combining Modes

A namespace can use:

```text
enforce=baseline
audit=restricted
warn=restricted
```

Conceptually:

```text
Baseline
 ↓
Must pass

Restricted
 ↓
Audit violations

Restricted
 ↓
Warn developer
```

This is useful during gradual security adoption.

---

# Recommended Migration Strategy

Instead of immediately enforcing the most restrictive profile:

```text
Existing workloads
       ↓
warn restricted
       ↓
audit restricted
       ↓
Fix violations
       ↓
enforce restricted
```

This reduces unexpected production outages.

---

# Namespace Labels

Pod Security Admission is commonly configured using namespace labels.

Example:

```bash
kubectl label namespace production \
  pod-security.kubernetes.io/enforce=restricted
```

---

# Audit Label

```bash
kubectl label namespace production \
  pod-security.kubernetes.io/audit=restricted
```

---

# Warning Label

```bash
kubectl label namespace production \
  pod-security.kubernetes.io/warn=restricted
```

---

# Check Namespace Labels

```bash
kubectl get namespace production --show-labels
```

---

# View Namespace YAML

```bash
kubectl get namespace production -o yaml
```

Look for:

```text
pod-security.kubernetes.io/enforce
pod-security.kubernetes.io/audit
pod-security.kubernetes.io/warn
```

---

# SecurityContext

Pod security is closely related to:

```text
securityContext
```

A security context defines security-related settings for:

```text
Pod
Container
```

---

# Pod SecurityContext

Example:

```yaml
spec:

  securityContext:

    runAsNonRoot: true

    seccompProfile:

      type: RuntimeDefault
```

---

# Container SecurityContext

Example:

```yaml
containers:

- name: app

  image: nginx:1.30

  securityContext:

    allowPrivilegeEscalation: false

    capabilities:

      drop:

      - ALL
```

---

# Pod-Level vs Container-Level

Pod-level:

```yaml
spec:

  securityContext:
```

Container-level:

```yaml
containers:

- securityContext:
```

Some security settings are container-specific, while others can apply to the Pod.

---

# Running as Non-Root

Running applications as non-root reduces the impact of a container compromise.

Example:

```yaml
securityContext:

  runAsNonRoot: true
```

This tells Kubernetes that the container should not run as UID 0.

---

# `runAsUser`

You can specify a UID:

```yaml
securityContext:

  runAsUser: 1000
```

This means the process should run as:

```text
UID 1000
```

---

# `runAsGroup`

You can specify the primary group:

```yaml
securityContext:

  runAsGroup: 1000
```

---

# `fsGroup`

`fsGroup` can influence group ownership of supported mounted volumes.

Example:

```yaml
securityContext:

  fsGroup: 1000
```

Use it only when needed.

---

# Why Non-Root Matters

Bad:

```text
Container
   ↓
root
   ↓
Application compromise
   ↓
Potentially greater impact
```

Better:

```text
Container
   ↓
Non-root
   ↓
Application compromise
   ↓
Reduced privileges
```

Running as non-root does not make a container automatically secure, but it is an important defense layer.

---

# Privileged Containers

A privileged container has significantly expanded access to the host.

Example:

```yaml
securityContext:

  privileged: true
```

This should be avoided for ordinary application workloads.

---

# Why Privileged Containers Are Dangerous

A compromised privileged container may have significantly greater ability to:

```text
Interact with host devices
Access kernel interfaces
Modify host state
Escape container isolation
```

The exact impact depends on the runtime and host configuration.

---

# Baseline Restrictions

The Baseline profile blocks several risky configurations, including certain:

```text
Privilege escalation mechanisms
Host namespace usage
Host filesystem access
Linux capability configurations
```

The exact requirements are version-specific.

---

# Host Network

A Pod can request:

```yaml
hostNetwork: true
```

This places the Pod in the host's network namespace.

---

# Why Host Network Is Sensitive

Instead of:

```text
Pod Network
```

the application may use:

```text
Node Network
```

This can:

```text
Reduce network isolation
Expose host interfaces
Create port conflicts
Increase attack surface
```

Avoid it unless required.

---

# Host PID

A Pod can request:

```yaml
hostPID: true
```

This allows the Pod to share the host process namespace.

This is highly sensitive because processes on the host may become visible to the container.

---

# Host IPC

A Pod can request:

```yaml
hostIPC: true
```

This shares the host IPC namespace.

It can reduce isolation and should be avoided for ordinary workloads.

---

# Host Namespace Isolation

The following are particularly important:

```text
hostNetwork
hostPID
hostIPC
```

Security-focused policies generally restrict these configurations.

---

# HostPath

`hostPath` mounts a path from the Kubernetes node filesystem into a Pod.

Example:

```yaml
volumes:

- name: host-data

  hostPath:

    path: /var/lib/data
```

---

# Why HostPath Is Dangerous

A container may gain access to sensitive node files.

For example:

```text
Node filesystem
       ↓
hostPath
       ↓
Container
```

Potentially exposed information could include:

```text
System files
Container runtime data
Credentials
Application data
Configuration
```

Use `hostPath` only when there is a clear requirement.

---

# Linux Capabilities

Linux capabilities divide root privileges into smaller units.

Examples include:

```text
NET_ADMIN
NET_RAW
SYS_ADMIN
SYS_PTRACE
```

Some capabilities are especially powerful.

---

# Drop Capabilities

A security-focused container can drop capabilities:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL
```

Then add back only what is genuinely required.

---

# Add Specific Capability

Example:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL

    add:

    - NET_BIND_SERVICE
```

This follows:

```text
Drop Everything
 ↓
Add Only Required
```

---

# Why Capabilities Matter

Instead of:

```text
Full root privileges
```

Linux capabilities allow:

```text
Specific privileged operations
```

This supports least privilege.

---

# `allowPrivilegeEscalation`

Example:

```yaml
securityContext:

  allowPrivilegeEscalation: false
```

This prevents a process from gaining more privileges than its parent process through supported Linux privilege escalation mechanisms.

---

# Why Disable Privilege Escalation?

If the application does not require privilege escalation:

```text
allowPrivilegeEscalation: false
```

reduces attack opportunities.

---

# Read-Only Root Filesystem

A container can use:

```yaml
securityContext:

  readOnlyRootFilesystem: true
```

This prevents writes to the container's root filesystem.

---

# Why Read-Only Root Filesystem?

If an attacker compromises the application:

```text
Compromise
 ↓
Attempt to write malware
 ↓
Root filesystem read-only
 ↓
Write blocked
```

Applications may still need writable temporary storage.

---

# Temporary Writable Storage

A common pattern is to mount an `emptyDir` volume:

```yaml
volumes:

- name: tmp

  emptyDir: {}
```

Then mount it:

```yaml
volumeMounts:

- name: tmp

  mountPath: /tmp
```

This allows:

```text
/tmp
```

to remain writable while the root filesystem is read-only.

---

# Seccomp

Seccomp stands for:

```text
Secure Computing
```

It restricts the system calls a process can make.

Linux system calls include operations such as:

```text
open
read
write
execve
socket
clone
```

A seccomp profile can limit which calls are permitted.

---

# RuntimeDefault

A common secure configuration is:

```yaml
securityContext:

  seccompProfile:

    type: RuntimeDefault
```

This uses the container runtime's default seccomp profile where supported.

---

# Custom Seccomp Profiles

Advanced environments can define custom profiles.

Conceptually:

```text
Application
 ↓
System Calls
 ↓
Seccomp Policy
 ↓
Allowed / Blocked
```

Custom profiles require careful testing because blocking required system calls can break applications.

---

# AppArmor

AppArmor is a Linux security mechanism that can restrict application behavior using profiles.

Conceptually:

```text
Application
 ↓
AppArmor Profile
 ↓
Allowed / Denied Operations
```

Availability and configuration depend on the underlying Linux distribution and node configuration.

---

# SELinux

SELinux provides mandatory access controls.

It can enforce:

```text
Labels
Policies
Process Restrictions
File Access Restrictions
```

Kubernetes can integrate with SELinux when the node operating system and container runtime support it.

---

# AppArmor vs SELinux

Both provide additional host-level security controls.

Conceptually:

```text
AppArmor
=
Profile-based access control
```

```text
SELinux
=
Label/policy-based mandatory access control
```

The exact capabilities and operational model depend on the host operating system.

---

# SecurityContext Example

A hardened container might use:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: secure-app

spec:

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

    volumeMounts:

    - name: tmp

      mountPath: /tmp

  volumes:

  - name: tmp

    emptyDir: {}
```

This provides several layers of hardening.

---

# SecurityContext Hardening

A useful baseline is:

```text
Non-root
+
No privilege escalation
+
Drop capabilities
+
RuntimeDefault seccomp
+
Read-only root filesystem
```

Not every application can use every setting immediately.

Test applications carefully.

---

# Pod Security and Images

Pod Security Standards focus on how Pods run.

Image security is a related but separate control.

For example:

```text
Pod Security
 ↓
How does the container run?

Image Security
 ↓
What code is being executed?
```

Both are necessary for defense in depth.

---

# Pod Security and RBAC

RBAC controls:

```text
Who can create Pods?
```

Pod Security controls:

```text
What security characteristics can those Pods have?
```

Example:

```text
Developer
 ↓
RBAC = Can create Pod
 ↓
Pod Security = Privileged Pod rejected
```

---

# Pod Security and NetworkPolicy

Pod Security controls:

```text
Container privileges
```

NetworkPolicy controls:

```text
Network communication
```

Example:

```text
Pod Security
 ↓
No privileged container

NetworkPolicy
 ↓
Only approved network connections
```

---

# Pod Security and Runtime Security

Runtime security detects suspicious activity after workloads are running.

Example:

```text
Pod Security
 ↓
Prevent dangerous configuration

Runtime Security
 ↓
Detect suspicious behavior
```

---

# Pod Security Standards and Namespaces

A common enterprise strategy is:

```text
system namespaces
    ↓
Privileged / specialized policy

development
    ↓
Baseline

production
    ↓
Restricted
```

The exact policy should depend on workload requirements.

---

# System Workloads

Some system components may genuinely require elevated privileges.

Examples can include:

```text
CNI components
Node agents
Storage plugins
Monitoring agents
```

Do not blindly apply the most restrictive profile without checking workload requirements.

---

# Production Namespace Strategy

Example:

```text
development
  enforce=baseline
  warn=restricted
  audit=restricted

staging
  enforce=restricted

production
  enforce=restricted
```

This is an example strategy, not a universal requirement.

---

# Exception Handling

Some workloads may require exceptions.

For example:

```text
Networking Agent
```

may need:

```text
hostNetwork
```

Instead of weakening the security policy for an entire cluster:

```text
Document the exception
Limit its scope
Use a dedicated namespace
Use dedicated RBAC
Monitor the workload
```

---

# Security Policy Design

A good security policy asks:

```text
What does the workload need?
```

rather than:

```text
What settings can we enable?
```

Start with:

```text
Least Privilege
```

---

# Production Hardening Strategy

For application workloads:

```text
1. Run as non-root
2. Disable privilege escalation
3. Drop capabilities
4. Use RuntimeDefault seccomp
5. Use read-only root filesystem
6. Avoid host namespaces
7. Avoid hostPath
8. Use NetworkPolicy
9. Use minimal RBAC
10. Use trusted images
```

---

# Pod Security Migration

Suppose an existing cluster has many workloads running with:

```text
Privileged
```

Moving directly to:

```text
Restricted
```

may cause failures.

A safer process:

```text
Inventory
   ↓
Audit
   ↓
Warn
   ↓
Remediate
   ↓
Enforce
```

---

# Inventory Workloads

Identify:

```text
Privileged containers
HostNetwork
HostPID
HostIPC
HostPath
Root containers
Capabilities
Missing seccomp
Privilege escalation
```

---

# Audit Violations

Use Pod Security Admission's:

```text
audit
```

mode to identify policy violations without immediately blocking workloads.

---

# Warn Developers

Use:

```text
warn
```

to provide feedback during deployment.

Developers can then fix manifests before enforcement.

---

# Enforce

Once workloads satisfy the policy:

```text
enforce=restricted
```

can be introduced.

---

# Troubleshooting Pod Security

Suppose:

```bash
kubectl apply -f pod.yaml
```

returns:

```text
violates PodSecurity "restricted"
```

The error usually indicates which security requirement was violated.

Possible causes:

```text
Running as root
Privileged container
Host namespace
Unsafe capabilities
Missing seccomp
Privilege escalation
HostPath
```

---

# Check Namespace Policy

```bash
kubectl get namespace production -o yaml
```

Look for:

```text
pod-security.kubernetes.io/enforce
```

---

# Check Pod Security Context

```bash
kubectl get pod <name> -o yaml
```

Review:

```text
securityContext
hostNetwork
hostPID
hostIPC
volumes
capabilities
```

---

# Test a Pod Against Policy

Create the Pod in a test namespace.

Observe:

```text
Allowed
```

or:

```text
Rejected
```

Then modify the security configuration and test again.

---

# Common Violation

Example:

```yaml
securityContext:

  runAsUser: 0
```

This means:

```text
Root
```

A Restricted policy will generally reject such a configuration.

---

# Fix

Use a non-root UID:

```yaml
securityContext:

  runAsNonRoot: true

  runAsUser: 1000
```

Ensure the image supports running as that user.

---

# Common Violation: Privileged

Bad:

```yaml
securityContext:

  privileged: true
```

Fix:

```text
Remove privileged mode
```

unless the workload has a legitimate system-level requirement.

---

# Common Violation: Privilege Escalation

Bad:

```yaml
allowPrivilegeEscalation: true
```

For security-focused workloads:

```yaml
allowPrivilegeEscalation: false
```

---

# Common Violation: Capabilities

Bad:

```yaml
capabilities:

  add:

  - SYS_ADMIN
```

unless required.

Better:

```yaml
capabilities:

  drop:

  - ALL
```

and add only necessary capabilities.

---

# Common Violation: Seccomp

A security-focused workload should use:

```yaml
seccompProfile:

  type: RuntimeDefault
```

where supported.

---

# Common Violation: HostPath

Bad:

```yaml
volumes:

- name: host

  hostPath:

    path: /
```

Avoid exposing the node filesystem.

---

# Hands-on Lab 1 – Create Test Namespace

```bash
kubectl create namespace pss-lab
```

Label it:

```bash
kubectl label namespace pss-lab \
  pod-security.kubernetes.io/enforce=restricted
```

---

# Hands-on Lab 2 – Deploy Insecure Pod

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: insecure

spec:

  containers:

  - name: app

    image: nginx:1.30

    securityContext:

      privileged: true
```

Try:

```bash
kubectl apply -f insecure.yaml \
  -n pss-lab
```

Observe:

```text
Admission rejection
```

---

# Hands-on Lab 3 – Fix the Pod

Create a hardened version:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: secure

spec:

  securityContext:

    runAsNonRoot: true

    seccompProfile:

      type: RuntimeDefault

  containers:

  - name: app

    image: nginxinc/nginx-unprivileged:stable-alpine

    securityContext:

      allowPrivilegeEscalation: false

      capabilities:

        drop:

        - ALL
```

Apply it:

```bash
kubectl apply -f secure.yaml \
  -n pss-lab
```

Verify:

```bash
kubectl get pods -n pss-lab
```

---

# Hands-on Lab 4 – Test `warn`

Create a test namespace:

```bash
kubectl create namespace pss-warn
```

Apply:

```bash
kubectl label namespace pss-warn \
  pod-security.kubernetes.io/warn=restricted
```

Deploy a deliberately non-compliant Pod.

Observe the warning.

---

# Hands-on Lab 5 – Test `audit`

Label:

```bash
kubectl label namespace pss-warn \
  pod-security.kubernetes.io/audit=restricted
```

Deploy a non-compliant Pod.

Inspect Kubernetes audit information if audit logging is configured in your environment.

---

# Hands-on Lab 6 – Test Non-Root

Create:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: nonroot-demo

spec:

  securityContext:

    runAsNonRoot: true

  containers:

  - name: app

    image: nginx:1.30
```

The image may fail if it expects to run as root.

This demonstrates an important principle:

```text
Security policy
+
Application compatibility
```

must both be considered.

---

# Hands-on Lab 7 – Test Read-Only Root Filesystem

Create a Pod with:

```yaml
securityContext:

  readOnlyRootFilesystem: true
```

Run an application that attempts to write to:

```text
/
```

Observe the failure.

Then mount:

```text
emptyDir
```

at a writable path such as:

```text
/tmp
```

and test again.

---

# Hands-on Lab 8 – Test Capability Dropping

Create:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL
```

Deploy the container.

Then identify whether the application still functions.

This demonstrates:

```text
Least Privilege
```

at the Linux capability level.

---

# Hands-on Lab 9 – Inspect SecurityContext

Run:

```bash
kubectl get pod <name> -o yaml
```

Identify:

```text
runAsNonRoot
runAsUser
allowPrivilegeEscalation
capabilities
seccompProfile
readOnlyRootFilesystem
```

---

# Hands-on Lab 10 – Namespace Policy Review

Run:

```bash
kubectl get namespaces --show-labels
```

Identify namespaces using:

```text
enforce
audit
warn
```

Document the security posture of each namespace.

---

# Hands-on Lab 11 – Production Migration Simulation

Create:

```text
legacy
```

namespace.

Start with:

```text
warn=restricted
audit=restricted
```

Deploy several workloads.

Fix violations.

Then enable:

```text
enforce=restricted
```

This simulates a production migration process.

---

# Hands-on Lab 12 – Security Policy Checklist

For each workload, verify:

```text
☐ Non-root
☐ No privileged mode
☐ No hostNetwork
☐ No hostPID
☐ No hostIPC
☐ No unnecessary hostPath
☐ No privilege escalation
☐ Capabilities dropped
☐ RuntimeDefault seccomp
☐ Read-only root filesystem where possible
☐ Resource requests
☐ Resource limits
☐ Appropriate Service Account
```

---

# Common Mistakes

## 1. Running Everything as Root

Avoid:

```text
UID 0
```

when the application does not require it.

---

## 2. Using Privileged Containers

Do not use:

```yaml
privileged: true
```

for convenience.

---

## 3. Using Host Namespaces

Avoid:

```text
hostNetwork
hostPID
hostIPC
```

unless required.

---

## 4. Using HostPath Without Review

Host filesystem access can significantly increase risk.

---

## 5. Adding Powerful Capabilities

Avoid unnecessary:

```text
SYS_ADMIN
NET_ADMIN
SYS_PTRACE
```

and other powerful capabilities.

---

## 6. Forgetting Seccomp

Use:

```yaml
seccompProfile:

  type: RuntimeDefault
```

where appropriate.

---

## 7. Assuming Non-Root Alone Is Enough

Non-root is only one security layer.

Use:

```text
RBAC
NetworkPolicy
Image Security
Runtime Security
Admission
```

as additional controls.

---

## 8. Enforcing Restricted Immediately

Existing workloads may break.

Use:

```text
warn
audit
enforce
```

as a controlled migration strategy.

---

## 9. Ignoring Application Compatibility

A hardened filesystem or non-root configuration can break applications that assume:

```text
root
writable /
specific capabilities
```

Test before production enforcement.

---

## 10. Applying One Policy to Every Workload

System components may require different security settings from ordinary applications.

---

# Best Practices

### 1. Prefer Restricted for Compatible Applications

Use the strongest practical profile.

---

### 2. Start With Baseline

For legacy workloads, Baseline can be a useful intermediate step.

---

### 3. Use Warn and Audit Before Enforce

This helps identify violations.

---

### 4. Run as Non-Root

Use:

```yaml
runAsNonRoot: true
```

where compatible.

---

### 5. Disable Privilege Escalation

Use:

```yaml
allowPrivilegeEscalation: false
```

when possible.

---

### 6. Drop Capabilities

Prefer:

```yaml
capabilities:

  drop:

  - ALL
```

and add only required capabilities.

---

### 7. Use RuntimeDefault Seccomp

```yaml
seccompProfile:

  type: RuntimeDefault
```

---

### 8. Avoid Host Access

Avoid unnecessary:

```text
hostNetwork
hostPID
hostIPC
hostPath
```

---

### 9. Use Read-Only Root Filesystems

Where applications support it:

```yaml
readOnlyRootFilesystem: true
```

---

### 10. Keep Exceptions Narrow

Do not weaken security for an entire cluster because one workload requires elevated privileges.

---

### 11. Document Exceptions

For every exception, record:

```text
Reason
Owner
Scope
Risk
Compensating Controls
Review Date
```

---

### 12. Combine Pod Security With Other Controls

Use:

```text
PSS
+
RBAC
+
NetworkPolicy
+
Image Security
+
Runtime Security
```

---

# Production Hardening Example

```yaml
apiVersion: apps/v1

kind: Deployment

metadata:

  name: secure-app

spec:

  replicas: 2

  selector:

    matchLabels:

      app: secure-app

  template:

    metadata:

      labels:

        app: secure-app

    spec:

      serviceAccountName: secure-app-sa

      securityContext:

        runAsNonRoot: true

        seccompProfile:

          type: RuntimeDefault

      containers:

      - name: app

        image: example.com/secure-app@sha256:<digest>

        securityContext:

          allowPrivilegeEscalation: false

          readOnlyRootFilesystem: true

          capabilities:

            drop:

            - ALL

        resources:

          requests:

            cpu: 100m

            memory: 128Mi

          limits:

            cpu: 500m

            memory: 512Mi

        volumeMounts:

        - name: tmp

          mountPath: /tmp

      volumes:

      - name: tmp

        emptyDir: {}
```

This example combines:

```text
Non-root
Seccomp
No privilege escalation
Dropped capabilities
Read-only filesystem
Resource limits
Dedicated Service Account
Immutable image reference
```

The exact configuration must be adapted to the application's needs.

---

# Pod Security Defense-in-Depth

```text
                  Pod
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
    Non-root    Seccomp    Capabilities
        │          │          │
        └──────────┼──────────┘
                   ▼
             Pod Security
                   │
                   ▼
              NetworkPolicy
                   │
                   ▼
                 RBAC
                   │
                   ▼
             Runtime Security
```

---

# Pod Security Threat Model

Potential threats:

```text
Container Escape
Privilege Escalation
Host Filesystem Access
Host Network Access
Kernel Attack Surface
Credential Theft
Lateral Movement
Malicious Image
```

Controls:

```text
PSS
SecurityContext
Seccomp
AppArmor
SELinux
NetworkPolicy
RBAC
Image Security
Runtime Security
```

---

# Pod Security and Container Escape

No container isolation mechanism should be treated as an absolute guarantee.

The goal is:

```text
Reduce Attack Surface
+
Limit Privileges
+
Limit Host Access
+
Detect Suspicious Behavior
```

---

# Pod Security and Supply Chain

A secure Pod configuration does not guarantee a safe image.

For example:

```text
Secure Pod
   +
Malicious Image
   =
Risk
```

Therefore:

```text
Pod Security
+
Image Signing
+
Image Scanning
+
Trusted Registry
```

should work together.

---

# Pod Security and Secrets

Even a non-root Pod can potentially access application credentials if they are mounted.

Use:

```text
Least Privilege
Secret Scoping
RBAC
File Permissions
```

to reduce exposure.

---

# Pod Security and NetworkPolicy

If a compromised container cannot:

```text
Reach arbitrary internal services
```

the impact of compromise may be reduced.

Therefore:

```text
PSS
+
NetworkPolicy
```

provides stronger defense than either alone.

---

# Quick Revision

## Pod Security Standards

```text
Privileged
Baseline
Restricted
```

---

## Privileged

```text
Most permissive
```

---

## Baseline

```text
Blocks many known privilege escalation configurations
```

---

## Restricted

```text
Strongest standard
```

---

## Pod Security Admission

```text
Enforces PSS
```

---

## `enforce`

```text
Reject violations
```

---

## `audit`

```text
Record violations
```

---

## `warn`

```text
Warn user
```

---

## `runAsNonRoot`

```text
Prevent root execution
```

---

## `allowPrivilegeEscalation`

```text
Controls privilege escalation
```

---

## Capabilities

```text
Fine-grained Linux privileges
```

---

## Seccomp

```text
System call filtering
```

---

## AppArmor

```text
Linux application confinement
```

---

## SELinux

```text
Mandatory access control
```

---

## HostNetwork

```text
Uses host network namespace
```

---

## HostPID

```text
Uses host process namespace
```

---

## HostIPC

```text
Uses host IPC namespace
```

---

## HostPath

```text
Mounts node filesystem path
```

---

# Essential Commands

Create namespace:

```bash
kubectl create namespace pss-lab
```

Label namespace:

```bash
kubectl label namespace pss-lab \
  pod-security.kubernetes.io/enforce=restricted
```

Add warning:

```bash
kubectl label namespace pss-lab \
  pod-security.kubernetes.io/warn=restricted
```

Add audit:

```bash
kubectl label namespace pss-lab \
  pod-security.kubernetes.io/audit=restricted
```

View namespace labels:

```bash
kubectl get namespace pss-lab --show-labels
```

View namespace YAML:

```bash
kubectl get namespace pss-lab -o yaml
```

View Pod:

```bash
kubectl get pod <name> -o yaml
```

View security-related configuration:

```bash
kubectl describe pod <name>
```

List namespaces:

```bash
kubectl get namespaces
```

---

# Interview Questions

## Basic

- What are Pod Security Standards?
- What is Pod Security Admission?
- What are the three Pod Security levels?
- What is the difference between Privileged, Baseline, and Restricted?
- What is the difference between `enforce`, `audit`, and `warn`?
- What is a SecurityContext?
- What does `runAsNonRoot` do?
- What is a privileged container?
- What is `hostNetwork`?
- What is `hostPID`?
- What is `hostIPC`?
- What is `hostPath`?
- What is seccomp?

---

## Intermediate

- Why should containers run as non-root?
- What does `allowPrivilegeEscalation: false` do?
- What are Linux capabilities?
- Why should capabilities be dropped?
- What is `RuntimeDefault` seccomp?
- What is the purpose of a read-only root filesystem?
- How does Pod Security Admission work?
- How are Pod Security Standards configured?
- How would you migrate a namespace from Baseline to Restricted?
- What happens when a Pod violates an `enforce` policy?
- How would you troubleshoot a Pod Security rejection?

---

## Advanced

- Explain the complete Pod Security Admission architecture.
- How would you design Pod security for a production cluster?
- How would you migrate thousands of existing workloads to Restricted?
- How would you handle workloads that require privileged access?
- How can host namespaces increase security risk?
- Why is `hostPath` dangerous?
- How can Linux capabilities be abused?
- How does seccomp reduce attack surface?
- Compare AppArmor and SELinux.
- How would you combine PSS with NetworkPolicy and RBAC?
- How would you design security exceptions without weakening the entire cluster?
- How would you investigate a Pod that violates Restricted?
- What are the limitations of Pod Security Standards?
- Why is Pod Security alone insufficient for container security?
- How would you build a defense-in-depth strategy for Kubernetes workloads?

---

# Interview Scenario 1

### Question

> A developer can create Pods but receives a PodSecurity rejection. Why?

### Answer

RBAC and Pod Security perform different functions.

RBAC may allow:

```text
create Pods
```

but Pod Security Admission can still reject the specific Pod because it violates:

```text
Restricted
```

For example:

```yaml
privileged: true
```

The flow is:

```text
Authentication
      ↓
Authorization
      ↓
CREATE Pod = Allowed
      ↓
Pod Security Admission
      ↓
Violation
      ↓
Rejected
```

---

# Interview Scenario 2

### Question

> Your organization wants to move all production namespaces to Restricted. How would you do it safely?

### Answer

Do not immediately enforce it.

Use:

```text
1. Inventory workloads
2. Enable warn=restricted
3. Enable audit=restricted
4. Identify violations
5. Fix application manifests
6. Test workloads
7. Enforce restricted
8. Monitor production
```

Architecture:

```text
warn
 ↓
audit
 ↓
remediation
 ↓
testing
 ↓
enforce
```

---

# Interview Scenario 3

### Question

> A container requires `NET_ADMIN`. Should you disable all Pod security restrictions?

### Answer

No.

Follow least privilege.

Instead:

```text
Drop ALL capabilities
       ↓
Add NET_ADMIN
       ↓
Restrict other privileges
       ↓
Document exception
       ↓
Use dedicated namespace
       ↓
Apply compensating controls
```

Do not weaken the entire cluster because one workload has a special requirement.

---

# Interview Scenario 4

### Question

> Why is `hostPath` considered dangerous?

### Answer

`hostPath` exposes a path from the Kubernetes node filesystem to the container.

Conceptually:

```text
Node filesystem
       ↓
hostPath
       ↓
Container
```

If the mounted path contains:

```text
Credentials
Runtime data
Configuration
Sensitive files
```

a compromised container may be able to access them.

Therefore:

```text
Avoid unnecessary hostPath
```

---

# Interview Scenario 5

### Question

> Is running a container as non-root enough to secure it?

### Answer

No.

Non-root is only one security layer.

A secure workload should also consider:

```text
No privilege escalation
Dropped capabilities
Seccomp
Read-only filesystem
No host namespaces
No unnecessary hostPath
NetworkPolicy
RBAC
Trusted images
Runtime monitoring
```

Defense in depth is essential.

---

# Production Pod Security Checklist

```text
☑ Run as non-root
☑ Disable privilege escalation
☑ Drop unnecessary capabilities
☑ Use RuntimeDefault seccomp
☑ Use read-only root filesystem where possible
☑ Avoid privileged containers
☑ Avoid hostNetwork
☑ Avoid hostPID
☑ Avoid hostIPC
☑ Avoid hostPath
☑ Use dedicated Service Accounts
☑ Use least-privilege RBAC
☑ Use NetworkPolicy
☑ Use trusted images
☑ Scan images
☑ Monitor runtime behavior
☑ Audit policy violations
☑ Document exceptions
```

---

# Recommended Practice

1. Create a test namespace.
2. Enable `warn=restricted`.
3. Deploy an insecure Pod.
4. Observe the warning.
5. Enable `audit=restricted`.
6. Inspect audit information.
7. Enable `enforce=restricted`.
8. Observe the Pod rejection.
9. Fix the Pod.
10. Test `runAsNonRoot`.
11. Test privilege escalation.
12. Test Linux capabilities.
13. Test seccomp.
14. Test read-only root filesystem.
15. Test temporary writable storage.
16. Test hostNetwork restrictions.
17. Test hostPID restrictions.
18. Test hostIPC restrictions.
19. Test hostPath restrictions.
20. Inspect security contexts.
21. Review namespace policies.
22. Simulate a migration from Baseline to Restricted.
23. Document an exception for a privileged workload.
24. Design a production Pod security baseline.
25. Combine PSS with RBAC and NetworkPolicy.

---

# References

## Official Kubernetes Documentation

- Pod Security Standards
- Pod Security Admission
- Configure Pod Security Admission
- Security Context
- Linux Capabilities
- Seccomp
- AppArmor
- SELinux
- Volumes
- Network Policies
- RBAC Authorization

---

# Chapter Summary

Pod Security Standards provide a standardized way to define security requirements for Kubernetes Pods.

The three profiles are:

```text
Privileged
Baseline
Restricted
```

They can be enforced through:

```text
Pod Security Admission
```

using namespace labels.

The three modes are:

```text
enforce
audit
warn
```

Their behavior is:

```text
enforce
=
Reject violations
```

```text
audit
=
Record violations
```

```text
warn
=
Warn the user
```

A practical migration strategy is:

```text
warn
 ↓
audit
 ↓
remediate
 ↓
enforce
```

Pod hardening should use SecurityContext settings such as:

```yaml
runAsNonRoot: true
```

```yaml
allowPrivilegeEscalation: false
```

```yaml
capabilities:
  drop:
  - ALL
```

```yaml
seccompProfile:
  type: RuntimeDefault
```

and, where compatible:

```yaml
readOnlyRootFilesystem: true
```

Dangerous configurations include:

```text
privileged=true
hostNetwork=true
hostPID=true
hostIPC=true
hostPath
```

because they can significantly reduce container isolation.

Linux capabilities provide more granular privileges than full root access. A strong approach is:

```text
Drop ALL
 ↓
Add only required capabilities
```

Seccomp reduces the available kernel attack surface by restricting system calls.

AppArmor and SELinux provide additional Linux security mechanisms.

However, Pod Security Standards are only one part of a secure Kubernetes architecture.

A mature security model combines:

```text
Pod Security
+
RBAC
+
NetworkPolicy
+
Image Security
+
Service Account Security
+
Runtime Security
+
Audit Logging
```

The central principle is:

> **Run workloads with the minimum privileges, host access, capabilities, and kernel interaction required for the application to function.**

A secure production workload can be visualized as:

```text
                     Pod
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
       Non-root    Seccomp    Capabilities
          │           │           │
          └───────────┼───────────┘
                      ▼
               Pod Security
                      │
                      ▼
                NetworkPolicy
                      │
                      ▼
                    RBAC
                      │
                      ▼
              Runtime Monitoring
                      │
                      ▼
                  Auditing
```

This provides defense in depth against:

```text
Privilege Escalation
Container Escape
Host Access
Lateral Movement
Credential Theft
Kernel Exploitation
```

The key principle to remember is:

> **Pod Security Standards control how securely workloads are allowed to run; RBAC controls who can manage them.**

---

## Next Chapter

# Chapter 52 – Network Security

Topics will include:

- Kubernetes Network Security Fundamentals
- Pod Network Security
- Service Network Security
- NetworkPolicy
- Default-Deny Policies
- Ingress Rules
- Egress Rules
- Namespace Selectors
- Pod Selectors
- IP Blocks
- Network Segmentation
- Zero-Trust Networking
- NetworkPolicy Limitations
- CNI Enforcement
- DNS Security
- Service Discovery Security
- East-West Traffic
- North-South Traffic
- Network Encryption
- mTLS
- Service Mesh Security
- Network Isolation
- Multi-Tenant Networking
- Egress Control
- Ingress Control
- API Server Network Security
- CNI Security
- Network Monitoring
- Network Troubleshooting
- Common Attack Paths
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---