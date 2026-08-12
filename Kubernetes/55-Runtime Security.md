# Chapter 55 – Runtime Security

## Overview

Container image security protects workloads **before deployment**.

Runtime security protects workloads **while they are running**.

A secure Kubernetes environment therefore needs multiple layers:

```text
Source Security
      ↓
Image Security
      ↓
Pod Security
      ↓
Network Security
      ↓
Runtime Security
      ↓
Detection & Response
```

Runtime security focuses on detecting and preventing suspicious behavior such as:

```text
Container Escape
Privilege Escalation
Unexpected Processes
Reverse Shells
Malware Execution
Cryptocurrency Mining
Credential Theft
File Manipulation
Network Scanning
Lateral Movement
Persistence
```

A useful security principle is:

> **Do not assume that a running container will always behave as intended simply because its image was trusted.**

---

# Learning Objectives

After completing this chapter, you will understand:

- Kubernetes runtime security
- Container runtime security
- Runtime threat models
- Runtime attack surfaces
- Container escape
- Privilege escalation
- Linux capabilities
- Seccomp
- AppArmor
- SELinux
- Rootless containers
- Runtime detection
- Process monitoring
- File monitoring
- Network monitoring
- System call monitoring
- eBPF
- Falco
- Tetragon
- Audit logs
- Container runtime events
- Suspicious processes
- Reverse shell detection
- Cryptocurrency mining
- Malware detection
- Persistence
- Lateral movement
- Credential theft
- Container escape detection
- Runtime policies
- Kubernetes runtime security architecture
- Runtime security vs image security
- Runtime security vs Pod Security
- Incident response
- Evidence collection
- Runtime forensics
- Production deployment
- Security monitoring
- Troubleshooting
- Hands-on Labs
- Common mistakes
- Best practices
- Quick revision
- Interview questions

---

# What Is Runtime Security?

Runtime security protects workloads during execution.

For example:

```text
Container Starts
      ↓
Application Runs
      ↓
Runtime Monitoring
      ↓
Behavior Observed
      ↓
Normal / Suspicious
```

Runtime security can detect behavior that was not visible during image scanning.

---

# Why Runtime Security Matters

Consider a trusted image:

```text
Trusted Image
     ↓
Pod
     ↓
Application Vulnerability
     ↓
Attacker Gains Code Execution
     ↓
Suspicious Process
     ↓
Network Connection
     ↓
Credential Theft
```

Image scanning cannot necessarily detect the entire attack sequence.

Runtime monitoring can detect:

```text
Unexpected Process
Unexpected Network Connection
Unexpected File Access
Unexpected Privilege Change
```

---

# Runtime Security Layers

A production environment may use:

```text
Pod Security
      +
Linux Security Controls
      +
Seccomp
      +
AppArmor / SELinux
      +
Runtime Detection
      +
NetworkPolicy
      +
eBPF
      +
Audit Logging
      +
Incident Response
```

---

# Runtime Threat Model

An attacker may begin with:

```text
Internet
   ↓
Application Vulnerability
   ↓
Container
```

Then attempt:

```text
Privilege Escalation
Container Escape
Credential Theft
Network Discovery
Lateral Movement
Persistence
Data Exfiltration
```

Runtime security aims to detect or prevent these behaviors.

---

# Runtime Attack Surface

A running container interacts with:

```text
Processes
Filesystem
Kernel
Network
IPC
Devices
Capabilities
Namespaces
System Calls
Service Accounts
Secrets
```

Each interaction can represent a security boundary.

---

# Container Isolation

Containers use Linux mechanisms such as:

```text
Namespaces
Control Groups
Capabilities
Seccomp
LSM Security
```

These help isolate workloads.

---

# Linux Namespaces

Namespaces isolate aspects of the system.

Examples include:

```text
PID
Network
Mount
IPC
UTS
User
```

Conceptually:

```text
Container
   │
   ├── Process Namespace
   ├── Network Namespace
   ├── Mount Namespace
   └── User Namespace
```

---

# Process Namespace

A container generally sees its own process namespace.

Example:

```text
Container
 ├── PID 1
 ├── PID 10
 └── PID 20
```

This helps isolate processes.

---

# Network Namespace

Containers can have separate network namespaces.

Conceptually:

```text
Pod Network Namespace
      │
      ├── eth0
      ├── Routes
      └── Interfaces
```

---

# Mount Namespace

A container has its own filesystem view.

Example:

```text
Container
 └── /
     ├── app
     ├── etc
     └── tmp
```

Host files should not normally be visible.

---

# Container Escape

A container escape occurs when an attacker breaks intended isolation and gains access to the host or other protected resources.

Conceptually:

```text
Container
    ↓
Isolation Boundary
    ↓
Escape
    ↓
Host
```

This is a high-impact security event.

---

# Causes of Container Escape

Potential causes include:

```text
Kernel Vulnerability
Runtime Vulnerability
Privileged Container
Dangerous Capabilities
Host Filesystem Mount
Host Namespace Sharing
Misconfiguration
```

---

# Privileged Containers

A Pod can be configured with:

```yaml
securityContext:

  privileged: true
```

This significantly increases container privileges and should generally be avoided unless there is a strong operational requirement.

---

# Why Privileged Containers Are Dangerous

A privileged workload may gain access to capabilities and host resources that normal containers should not have.

Architecture:

```text
Normal Container
     ↓
Restricted

Privileged Container
     ↓
Much Broader Host Access
```

---

# Host Filesystem Mount

A workload may mount host paths:

```yaml
volumes:

- name: host

  hostPath:

    path: /
```

This can expose sensitive host resources.

Avoid unnecessary:

```text
hostPath
```

usage.

---

# Host Namespace Sharing

Kubernetes allows certain host namespace settings such as:

```yaml
hostNetwork: true
```

and:

```yaml
hostPID: true
```

These reduce isolation and should only be used when required.

---

# Privilege Escalation

Privilege escalation occurs when a process gains more privileges than intended.

Example:

```text
Low Privilege Process
       ↓
Privilege Escalation
       ↓
Root / Elevated Privileges
```

---

# Preventing Privilege Escalation

Use:

```yaml
securityContext:

  allowPrivilegeEscalation: false
```

where compatible.

---

# Running as Non-Root

Prefer:

```yaml
securityContext:

  runAsNonRoot: true
```

and where appropriate:

```yaml
runAsUser: 1000
```

---

# Root vs Non-Root

Root:

```text
UID 0
```

Non-root:

```text
UID 1000
```

Running as non-root reduces the impact of certain application compromises.

---

# Linux Capabilities

Linux capabilities split traditional root privileges into smaller units.

Examples include:

```text
NET_ADMIN
NET_RAW
SYS_ADMIN
SYS_PTRACE
SYS_CHROOT
DAC_OVERRIDE
```

---

# Why Capabilities Matter

Instead of:

```text
Full Root Privileges
```

a workload can receive:

```text
Only Required Capability
```

This supports:

```text
Least Privilege
```

---

# Dropping Capabilities

Example:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL
```

Then add only required capabilities.

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

# Dangerous Capabilities

Some capabilities can significantly increase risk.

Examples:

```text
SYS_ADMIN
SYS_PTRACE
NET_ADMIN
NET_RAW
```

Do not grant them without a specific requirement.

---

# Seccomp

Seccomp stands for:

```text
Secure Computing
```

It restricts which Linux system calls a process can use.

Conceptually:

```text
Application
    ↓
System Call
    ↓
Seccomp Profile
    ↓
Allowed / Blocked
```

---

# Why Seccomp Matters

A compromised application may attempt to execute unusual system calls.

Seccomp can reduce the available attack surface.

---

# Seccomp Profile

Example:

```yaml
securityContext:

  seccompProfile:

    type: RuntimeDefault
```

This is a common baseline configuration.

---

# RuntimeDefault

Kubernetes can use the container runtime's default seccomp profile:

```yaml
type: RuntimeDefault
```

This is generally preferable to:

```text
Unconfined
```

when compatible with the workload.

---

# Unconfined

Example:

```yaml
seccompProfile:

  type: Unconfined
```

This removes seccomp restrictions.

Avoid unless there is a specific requirement.

---

# AppArmor

AppArmor is a Linux security mechanism that restricts application behavior using profiles.

Conceptually:

```text
Application
    ↓
AppArmor Profile
    ↓
Allowed / Denied
```

---

# SELinux

SELinux stands for:

```text
Security-Enhanced Linux
```

It provides mandatory access control based on security labels and policies.

Conceptually:

```text
Process
  +
Resource
  +
Security Context
       ↓
SELinux Policy
       ↓
Allow / Deny
```

---

# AppArmor vs SELinux

| Technology | Approach |
|---|---|
| AppArmor | Path/profile-oriented controls |
| SELinux | Label-based mandatory access control |

Both can provide additional runtime protection depending on the host operating system and Kubernetes environment.

---

# Rootless Containers

Rootless containers run container processes without requiring root privileges.

Benefits can include:

```text
Reduced Privilege
Smaller Impact of Compromise
Improved Isolation
```

However, compatibility and operational requirements must be considered.

---

# Runtime Detection

Runtime detection monitors behavior while workloads execute.

Possible events:

```text
Process Execution
File Access
Network Connection
Privilege Change
System Call
Container Start
Container Stop
```

---

# Runtime Detection Architecture

```text
Container
   │
   ▼
Runtime Events
   │
   ▼
Detection Engine
   │
   ├── Normal
   └── Suspicious
          │
          ▼
        Alert
          │
          ▼
    Investigation
```

---

# Process Monitoring

Monitor:

```text
Process Name
Command Line
Parent Process
User ID
Executable Path
Process Tree
```

---

# Suspicious Process Example

A web application normally runs:

```text
python app.py
```

But suddenly:

```text
/bin/sh
```

is spawned.

This may indicate:

```text
Command Injection
Remote Code Execution
Post-Exploitation
```

---

# Process Tree

Example:

```text
PID 1
 └── python
      └── sh
           └── curl
```

A security system may flag:

```text
Application → Shell
```

as suspicious depending on application behavior.

---

# Reverse Shell

A reverse shell occurs when a compromised workload establishes an outbound connection to an attacker-controlled system and provides command execution.

Conceptually:

```text
Compromised Pod
      │
      │ Outbound Connection
      ▼
Attacker
      │
      ▼
Command Execution
```

---

# Reverse Shell Detection

Possible indicators:

```text
Unexpected shell
Unexpected outbound connection
Application spawning shell
Shell connecting to external IP
```

Controls:

```text
NetworkPolicy
Egress Controls
Runtime Detection
Process Monitoring
```

---

# Cryptocurrency Mining

Attackers may deploy cryptocurrency miners after compromising a workload.

Indicators can include:

```text
Unexpected CPU Usage
Unknown Binary
Mining Pool Connections
Long-Running Suspicious Process
```

---

# Runtime Malware Detection

Runtime monitoring can detect:

```text
Unknown Executables
Suspicious Processes
File Modifications
Network Connections
Persistence Attempts
```

---

# File Monitoring

Monitor sensitive paths such as:

```text
/etc
/tmp
/app
/bin
/usr/bin
```

depending on the workload.

Unexpected modifications can indicate compromise.

---

# Sensitive File Access

Potentially sensitive files include:

```text
/etc/passwd
/etc/shadow
Service Account Token
Application Credentials
Private Keys
```

Access should be monitored where appropriate.

---

# Service Account Token

A Pod may receive a ServiceAccount token.

Modern Kubernetes commonly projects short-lived tokens into Pods.

A compromised application could potentially attempt to access its token.

Therefore:

```text
RBAC
+
Bounded Service Account Permissions
```

are essential.

---

# Service Account Security

Avoid giving a workload:

```text
cluster-admin
```

unless absolutely required.

Prefer:

```text
Specific Role
+
Specific Permissions
```

---

# Credential Theft

An attacker may attempt to obtain:

```text
Service Account Token
Cloud Credentials
Database Credentials
API Keys
Environment Variables
Mounted Secrets
```

Runtime controls should reduce unnecessary access.

---

# Runtime Security and RBAC

These address different layers.

```text
RBAC
=
What can the Kubernetes identity do?
```

```text
Runtime Security
=
What is the workload actually doing?
```

Use both.

---

# Network Monitoring

Runtime security can monitor:

```text
Destination IP
Destination Port
Protocol
Connection Frequency
DNS
Outbound Traffic
```

This can help detect:

```text
C2
Scanning
Exfiltration
Unexpected External Access
```

---

# eBPF

eBPF allows programs to run safely within the Linux kernel under defined verification and execution mechanisms.

Security tools can use eBPF for:

```text
Process Monitoring
Network Monitoring
System Call Visibility
Security Detection
```

---

# Why eBPF Is Useful

Traditional monitoring may require:

```text
User-space Agents
Kernel Hooks
Log Collection
```

eBPF can provide deep kernel-level visibility with efficient event collection when implemented appropriately.

---

# Falco

Falco is an open-source runtime security tool designed to detect suspicious activity in Linux and cloud-native environments.

It can detect events such as:

```text
Unexpected Shell
Sensitive File Access
Unexpected Process
Suspicious Network Activity
```

---

# Falco Architecture

Conceptually:

```text
Kernel / Runtime Events
        ↓
      Falco
        ↓
Detection Rules
        ↓
     Alerts
```

---

# Example Falco Rule Concept

A conceptual rule might detect:

```text
Shell spawned inside a container
```

The exact rule syntax depends on the Falco version and configuration.

---

# Tetragon

Tetragon is a Kubernetes-aware security observability and enforcement tool built around eBPF.

It can provide visibility into:

```text
Process Execution
System Calls
Network Events
Kubernetes Identity
```

and can support runtime enforcement.

---

# Falco vs Tetragon

| Capability | Falco | Tetragon |
|---|---|---|
| Runtime Detection | Yes | Yes |
| eBPF | Supported | Core architecture |
| Kubernetes Awareness | Strong | Strong |
| Enforcement | Limited / integration-dependent | Supported |
| Process Monitoring | Yes | Yes |
| Network Visibility | Yes | Yes |

Exact capabilities depend on versions and deployment configuration.

---

# Runtime Enforcement

Detection answers:

```text
What happened?
```

Enforcement answers:

```text
Should this action be allowed?
```

Example:

```text
Suspicious Process
       ↓
Detection
       ↓
Policy
       ↓
Block / Kill / Deny
```

---

# Runtime Security Policies

A policy may enforce:

```text
No Shells
No Privilege Escalation
No Unexpected Binaries
No Sensitive File Access
No Unauthorized Network Connection
```

---

# Runtime Security vs Image Security

| Image Security | Runtime Security |
|---|---|
| Before deployment | During execution |
| Scans image | Monitors behavior |
| Detects known vulnerabilities | Detects suspicious activity |
| SBOM | Runtime events |
| Image signing | Process/network monitoring |

Both are required.

---

# Runtime Security vs Pod Security

Pod Security controls how workloads are configured.

Examples:

```text
Privileged
Capabilities
Host namespaces
HostPath
Seccomp
```

Runtime security monitors behavior after the workload starts.

---

# Three Layers

```text
Image Security
     ↓
Pod Security
     ↓
Runtime Security
```

Example:

```text
Image:
No known CVEs

Pod:
Non-root + seccomp

Runtime:
Unexpected shell detected
```

---

# Runtime Security Architecture

```text
                    Kubernetes
                        │
                        ▼
                       Pod
                        │
          ┌─────────────┼─────────────┐
          ▼             ▼             ▼
       Process        Network       Files
          │             │             │
          └─────────────┼─────────────┘
                        ▼
                   eBPF / Runtime
                        │
                        ▼
                Detection Engine
                        │
                        ▼
                      Alert
                        │
                        ▼
                   SIEM / SOC
                        │
                        ▼
                  Incident Response
```

---

# Runtime Security and SIEM

Runtime events can feed security monitoring platforms.

Architecture:

```text
Container
   ↓
Runtime Detection
   ↓
Security Events
   ↓
SIEM
   ↓
Correlation
   ↓
Alert
   ↓
SOC
```

---

# Runtime Security Events

Examples:

```text
Container spawned shell
Process executed from /tmp
Unexpected binary executed
Sensitive file accessed
Unexpected outbound connection
Privilege escalation attempted
```

---

# Detection Engineering

Runtime security rules should distinguish:

```text
Normal Behavior
```

from:

```text
Suspicious Behavior
```

---

# False Positives

A rule such as:

```text
Alert whenever shell starts
```

may produce false positives because legitimate applications may use shells.

Better:

```text
Shell spawned by specific production application
+
External network connection
```

This creates stronger context.

---

# Behavioral Baselines

Understand normal workload behavior.

Example:

```text
Backend normally:
Python
PostgreSQL
HTTPS
DNS
```

Unexpected:

```text
Backend
 ↓
bash
 ↓
curl
 ↓
Unknown IP
```

may be high priority.

---

# Runtime Detection Correlation

One event may be benign.

Multiple events can indicate compromise:

```text
Unexpected Shell
      +
Unexpected Network Connection
      +
Sensitive File Access
      =
High-Confidence Incident
```

---

# Runtime Security and NetworkPolicy

These complement each other.

```text
NetworkPolicy
=
Where traffic is allowed
```

```text
Runtime Security
=
What the process is doing
```

---

# Runtime Security and Seccomp

Seccomp can prevent certain system calls.

Runtime monitoring can detect:

```text
System Call Behavior
```

Together:

```text
Seccomp
+
Runtime Detection
```

provide preventive and detective controls.

---

# Runtime Security and AppArmor

AppArmor can restrict:

```text
Files
Capabilities
Execution
```

Runtime monitoring can detect suspicious actions that still occur within allowed boundaries.

---

# Runtime Security and SELinux

SELinux can enforce mandatory access control.

Runtime security can add:

```text
Behavioral Monitoring
Detection
Alerting
```

---

# Container Escape Detection

Potential indicators include:

```text
Unexpected Host Namespace Access
Sensitive Device Access
Unexpected Mount Operations
Privileged Container
Kernel Exploitation Indicators
```

---

# Container Escape Prevention

Use:

```text
Non-root
Seccomp
AppArmor / SELinux
Dropped Capabilities
No Privileged Containers
Restricted HostPath
Restricted Host Namespaces
Updated Kernel
Updated Container Runtime
```

---

# Host Security

Containers share the host kernel.

Therefore:

```text
Container Security
+
Host Security
```

must be considered together.

Protect:

```text
Linux Kernel
Container Runtime
Kubelet
Node Filesystem
Node Network
```

---

# Container Runtime

Common container runtimes include:

```text
containerd
CRI-O
```

Runtime security must consider the runtime and its configuration.

---

# Container Runtime Attack Surface

Potential components include:

```text
Container Runtime
CRI
Kubelet
Kernel
CNI
CSI
Host Filesystem
```

A compromise of these components can affect many workloads.

---

# Node Compromise

If a Kubernetes node is compromised:

```text
Node
 ↓
Multiple Pods
 ↓
Potential Cluster Impact
```

Therefore runtime security should include node monitoring.

---

# Runtime Security and Node Monitoring

Monitor:

```text
Unexpected Root Processes
Kernel Events
New Services
Network Connections
File Changes
Container Runtime Activity
```

---

# Kubernetes Audit Logs

Kubernetes audit logging records API activity.

Example:

```text
User
 ↓
Kubernetes API
 ↓
Audit Event
```

Audit logs can help answer:

```text
Who changed the Pod?
Who accessed the Secret?
Who modified RBAC?
```

---

# Runtime Events vs Audit Events

These are different.

```text
Audit Log
=
Kubernetes API activity
```

```text
Runtime Event
=
What happened inside/on the workload and host
```

Both are useful.

---

# Runtime Incident Response

If suspicious behavior is detected:

```text
Alert
 ↓
Validate
 ↓
Contain
 ↓
Collect Evidence
 ↓
Investigate
 ↓
Eradicate
 ↓
Recover
 ↓
Monitor
```

---

# Runtime Incident Example

Suppose:

```text
Web Pod
```

suddenly executes:

```text
/bin/sh
```

and connects to:

```text
Unknown External IP
```

Response:

```text
1. Confirm alert
2. Identify Pod
3. Identify image
4. Identify node
5. Isolate workload
6. Preserve evidence
7. Inspect process tree
8. Inspect network connections
9. Check credentials
10. Rebuild from trusted image
11. Rotate exposed credentials
12. Investigate root cause
```

---

# Evidence Collection

Potential evidence:

```text
Pod YAML
Deployment YAML
Container Logs
Runtime Alerts
Network Flow Logs
Kubernetes Audit Logs
Node Logs
Process Information
Image Digest
Image SBOM
```

---

# Avoid Destroying Evidence

Do not immediately delete everything before collecting necessary evidence.

For example:

```text
kubectl delete pod
```

may remove useful runtime context.

Incident response should balance:

```text
Containment
```

with:

```text
Evidence Preservation
```

---

# Runtime Forensics

Runtime forensics attempts to understand:

```text
What happened?
When?
Which workload?
Which process?
Which user?
Which network connection?
Which credentials?
Which node?
```

---

# Runtime Security Workflow

```text
Detection
   ↓
Triage
   ↓
Context
   ↓
Containment
   ↓
Evidence
   ↓
Root Cause
   ↓
Remediation
   ↓
Recovery
   ↓
Lessons Learned
```

---

# Production Runtime Security Architecture

```text
                      Kubernetes Cluster
                              │
          ┌───────────────────┼───────────────────┐
          ▼                   ▼                   ▼
        Node A              Node B              Node C
          │                   │                   │
       Runtime             Runtime             Runtime
          │                   │                   │
          └───────────────────┼───────────────────┘
                              ▼
                         eBPF / Agent
                              │
                              ▼
                     Detection Platform
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                  SIEM               Alerts
                    │                   │
                    └─────────┬─────────┘
                              ▼
                         SOC / IR Team
```

---

# Runtime Security Threat Matrix

| Threat | Example | Preventive Control | Detection |
|---|---|---|---|
| Privilege escalation | Process gains privileges | `allowPrivilegeEscalation: false` | Runtime monitoring |
| Container escape | Host access | Seccomp, LSM, non-root | Runtime detection |
| Reverse shell | Outbound shell | Egress controls | Process + network monitoring |
| Crypto mining | Unknown miner | Restricted image/runtime | CPU/process detection |
| Credential theft | Token access | RBAC, secret restrictions | File/process monitoring |
| Lateral movement | Service scanning | NetworkPolicy | Network monitoring |
| Malware | Malicious binary | Image security | Runtime detection |

---

# Hands-on Lab 1 – Run as Non-Root

Create a Pod:

```yaml
apiVersion: v1

kind: Pod

metadata:

  name: non-root-test

spec:

  securityContext:

    runAsNonRoot: true

  containers:

  - name: app

    image: nginx:1.30

    securityContext:

      runAsUser: 101
```

Verify the process user.

---

# Hands-on Lab 2 – Disable Privilege Escalation

Create:

```yaml
securityContext:

  allowPrivilegeEscalation: false
```

Deploy the Pod.

Inspect:

```bash
kubectl get pod non-root-test -o yaml
```

---

# Hands-on Lab 3 – Use RuntimeDefault Seccomp

Configure:

```yaml
securityContext:

  seccompProfile:

    type: RuntimeDefault
```

Deploy the workload.

Verify:

```bash
kubectl get pod <pod> -o yaml
```

---

# Hands-on Lab 4 – Drop Capabilities

Use:

```yaml
securityContext:

  capabilities:

    drop:

    - ALL
```

Run the workload.

Determine whether the application continues functioning.

---

# Hands-on Lab 5 – Detect Unexpected Processes

Deploy a test application.

Observe its normal process tree.

Then intentionally launch a shell inside the container in a controlled lab.

Observe:

```text
Process Tree
```

Study how runtime detection systems can identify such behavior.

---

# Hands-on Lab 6 – Runtime Monitoring with Falco

Deploy Falco in a disposable cluster.

Generate a controlled event such as:

```text
Shell execution
```

Observe the resulting alert.

Study:

```text
Rule
Event
Alert
Context
```

---

# Hands-on Lab 7 – eBPF Runtime Monitoring

Deploy a suitable eBPF-based runtime security tool in a lab environment.

Observe:

```text
Process Events
Network Events
Kubernetes Metadata
```

---

# Hands-on Lab 8 – Network + Runtime Correlation

Create a test scenario:

```text
Application
   ↓
Unexpected Shell
   ↓
Outbound Connection
```

Monitor:

```text
Process Event
+
Network Event
```

Determine how correlation improves confidence.

---

# Hands-on Lab 9 – Secret Access Monitoring

Create a Pod with a test Secret.

Monitor access to the Secret-mounted file.

Determine:

```text
Which process accessed it?
When?
```

---

# Hands-on Lab 10 – Runtime Incident Response

Simulate:

```text
Compromised Test Pod
```

Generate:

```text
Unexpected Shell
Unexpected Network Connection
```

Practice:

```text
Detection
Triage
Containment
Evidence Collection
Recovery
```

Use only disposable lab credentials and workloads.

---

# Hands-on Lab 11 – Privileged Pod Review

Create a test Pod using:

```yaml
privileged: true
```

in a disposable cluster.

Compare its security context with a restricted Pod.

Understand why privileged workloads create increased risk.

Delete the test workload afterward.

---

# Hands-on Lab 12 – HostPath Security Review

Inspect workloads using:

```bash
kubectl get pods -A -o yaml
```

Look for:

```text
hostPath
hostNetwork
hostPID
hostIPC
privileged
```

Review whether each use is justified.

---

# Common Mistakes

## 1. Running Everything as Root

Root increases the impact of application compromise.

---

## 2. Using Privileged Containers

Avoid:

```yaml
privileged: true
```

unless absolutely necessary.

---

## 3. Granting All Capabilities

Avoid:

```yaml
capabilities:
  add:
  - ALL
```

Use only required capabilities.

---

## 4. Disabling Seccomp

Avoid:

```text
Unconfined
```

without a specific requirement.

---

## 5. Ignoring Runtime Behavior

A secure image can still behave maliciously after compromise.

---

## 6. Ignoring Host Security

Containers share the host kernel.

---

## 7. Giving Broad Service Account Permissions

Avoid:

```text
cluster-admin
```

for normal applications.

---

## 8. No Runtime Monitoring

Without runtime visibility, attacks may remain undetected.

---

## 9. Alerting Without Context

A single shell event may be legitimate.

Use contextual correlation.

---

## 10. Deleting Compromised Pods Immediately

You may destroy valuable evidence.

Follow incident-response procedures.

---

## 11. Ignoring Network Behavior

Unexpected outbound traffic can be an important compromise indicator.

---

## 12. Ignoring File Activity

Unexpected modification of sensitive files may indicate persistence or tampering.

---

# Best Practices

### 1. Run Containers as Non-Root

Use:

```yaml
runAsNonRoot: true
```

where compatible.

---

### 2. Disable Privilege Escalation

Use:

```yaml
allowPrivilegeEscalation: false
```

where compatible.

---

### 3. Drop Unnecessary Capabilities

Prefer:

```yaml
capabilities:

  drop:

  - ALL
```

and add only what is required.

---

### 4. Use Seccomp

Prefer:

```text
RuntimeDefault
```

or a carefully designed custom profile.

---

### 5. Use AppArmor or SELinux

Use the host's available mandatory access-control framework.

---

### 6. Avoid Privileged Containers

Only permit them for justified workloads.

---

### 7. Restrict Host Access

Minimize:

```text
hostPath
hostNetwork
hostPID
hostIPC
```

---

### 8. Restrict Service Account Permissions

Follow:

```text
Least Privilege
```

---

### 9. Use NetworkPolicy

Restrict:

```text
East-West
Egress
Ingress
```

---

### 10. Monitor Runtime Behavior

Monitor:

```text
Processes
Network
Files
System Calls
```

---

### 11. Correlate Security Events

Combine:

```text
Process
+
Network
+
File
+
Kubernetes
```

events.

---

### 12. Integrate With SIEM

Send important runtime events to centralized security monitoring.

---

### 13. Maintain Incident Response Procedures

Know:

```text
Who investigates?
Who contains?
Who rotates credentials?
Who restores workloads?
```

---

### 14. Keep Host and Runtime Updated

Patch:

```text
Linux Kernel
Container Runtime
Kubernetes
CNI
Security Tools
```

---

### 15. Use Defense in Depth

Combine:

```text
Image Security
+
Pod Security
+
Network Security
+
Runtime Security
```

---

# Runtime Security Policy

A production workload should ideally meet requirements such as:

```text
☑ Non-root
☑ No privileged mode
☑ No unnecessary capabilities
☑ Privilege escalation disabled
☑ Seccomp enabled
☑ AppArmor / SELinux where appropriate
☑ Restricted host access
☑ Least-privilege ServiceAccount
☑ NetworkPolicy
☑ Runtime monitoring
☑ Centralized logging
☑ Incident response process
```

---

# Runtime Security and Zero Trust

Zero-trust principles apply at runtime too.

Instead of:

```text
Container is trusted
```

use:

```text
Container
 ↓
Identity
 ↓
Permissions
 ↓
Expected Behavior
 ↓
Continuous Verification
```

---

# Runtime Security Maturity Model

## Level 1 – Basic

```text
Pod Security
RBAC
NetworkPolicy
```

---

## Level 2 – Hardened

```text
Non-root
Seccomp
Capabilities
AppArmor / SELinux
```

---

## Level 3 – Detection

```text
Runtime Monitoring
Process Monitoring
Network Monitoring
```

---

## Level 4 – Advanced

```text
eBPF
Behavioral Detection
SIEM
Automated Response
```

---

## Level 5 – Mature

```text
Prevent
Detect
Correlate
Respond
Automate
Continuously Improve
```

---

# Runtime Security Architecture for a SOC

```text
                 Kubernetes Cluster
                         │
            ┌────────────┼────────────┐
            ▼            ▼            ▼
          Node A       Node B       Node C
            │            │            │
         Runtime      Runtime      Runtime
            │            │            │
            └────────────┼────────────┘
                         ▼
                   Runtime Sensor
                         │
                         ▼
                  Detection Engine
                         │
                         ▼
                      SIEM
                         │
                         ▼
                   SOC Analysts
                         │
                         ▼
                  Incident Response
```

---

# Runtime Incident Severity

Example prioritization:

### Critical

```text
Container Escape
Node Compromise
Credential Theft
```

### High

```text
Reverse Shell
Malware Execution
Unexpected Privileged Process
```

### Medium

```text
Unexpected Shell
Unexpected File Access
Unexpected Network Connection
```

### Low

```text
Known Administrative Activity
```

Always evaluate:

```text
Context
Impact
Confidence
Exposure
```

---

# Runtime Security Investigation Questions

When an alert occurs, ask:

```text
What happened?
Which Pod?
Which container?
Which image?
Which digest?
Which process?
Which user?
Which node?
Which ServiceAccount?
Which network destination?
Which files were accessed?
Which credentials were available?
When did it start?
What happened immediately before it?
```

---

# Runtime Incident Investigation

```text
Alert
 ↓
Pod Identification
 ↓
Node Identification
 ↓
Image Identification
 ↓
Process Investigation
 ↓
Network Investigation
 ↓
Credential Investigation
 ↓
Timeline
 ↓
Containment
 ↓
Recovery
```

---

# Quick Revision

## Runtime Security

```text
Protect workloads during execution
```

---

## Container Escape

```text
Breaking container isolation to access host/protected resources
```

---

## Privileged Container

```text
Container with significantly elevated privileges
```

---

## Capability

```text
Fine-grained Linux privilege
```

---

## Seccomp

```text
System-call filtering
```

---

## AppArmor

```text
Linux application access-control mechanism
```

---

## SELinux

```text
Linux mandatory access control
```

---

## Rootless

```text
Run container without root privileges
```

---

## eBPF

```text
Kernel-level programmable observability/security mechanism
```

---

## Falco

```text
Runtime threat detection tool
```

---

## Tetragon

```text
eBPF-based Kubernetes-aware observability and enforcement tool
```

---

## Runtime Detection

```text
Detect suspicious behavior while workloads run
```

---

## Runtime Enforcement

```text
Block or restrict suspicious behavior
```

---

## Container Escape Prevention

```text
Non-root
+
Seccomp
+
LSM
+
Capabilities
+
No Privileged Mode
+
Restricted Host Access
```

---

# Essential Commands

List Pods:

```bash
kubectl get pods -A
```

Inspect Pod security configuration:

```bash
kubectl get pod <pod> -o yaml
```

Describe Pod:

```bash
kubectl describe pod <pod>
```

Inspect ServiceAccount:

```bash
kubectl get serviceaccount
```

Inspect RBAC:

```bash
kubectl get role,rolebinding
```

Inspect ClusterRole:

```bash
kubectl get clusterrole
```

Inspect NetworkPolicies:

```bash
kubectl get networkpolicies -A
```

View Pod logs:

```bash
kubectl logs <pod>
```

View previous container logs:

```bash
kubectl logs <pod> --previous
```

Execute a command:

```bash
kubectl exec -it <pod> -- <command>
```

Inspect Pod events:

```bash
kubectl describe pod <pod>
```

List nodes:

```bash
kubectl get nodes
```

Inspect node:

```bash
kubectl describe node <node>
```

---

# Interview Questions

## Basic

- What is runtime security?
- Why is runtime security required?
- What is container escape?
- What is privilege escalation?
- What is a Linux capability?
- What is Seccomp?
- What is AppArmor?
- What is SELinux?
- What is a privileged container?
- Why should containers run as non-root?
- What is eBPF?
- What is Falco?
- What is Tetragon?

---

## Intermediate

- How can you prevent container escape?
- How do you disable privilege escalation?
- How do you drop Linux capabilities?
- What is `RuntimeDefault` seccomp?
- What is the difference between image security and runtime security?
- What is the difference between runtime security and Pod Security?
- How can runtime monitoring detect reverse shells?
- How can runtime monitoring detect cryptocurrency miners?
- How can you monitor suspicious processes?
- How can you monitor suspicious network connections?
- What is the role of eBPF in runtime security?
- How does Falco detect threats?
- How does Tetragon provide runtime visibility?
- Why is host security important for Kubernetes?

---

## Advanced

- Design a Kubernetes runtime security architecture.
- How would you detect container escape attempts?
- How would you investigate a compromised Pod?
- How would you correlate process and network events?
- How would you detect reverse shells?
- How would you detect credential theft?
- How would you detect cryptocurrency mining?
- How would you use eBPF for runtime security?
- Compare Falco and Tetragon.
- How would you integrate runtime security with a SIEM?
- How would you design runtime security for a multi-tenant cluster?
- How would you balance runtime enforcement and application compatibility?
- How would you perform runtime forensics?
- How would you respond to a suspected node compromise?
- How would you build a runtime detection strategy for a SOC?

---

# Interview Scenario 1

### Question

> A web application container suddenly launches `/bin/sh`. Is that automatically an attack?

### Answer

Not necessarily.

A shell execution can be legitimate during:

```text
Administration
Debugging
Startup Scripts
Maintenance
```

However, if the application normally never launches a shell, it is suspicious.

Increase confidence by correlating:

```text
Unexpected Shell
+
Unexpected External Connection
+
Sensitive File Access
```

This is much stronger evidence of compromise.

---

# Interview Scenario 2

### Question

> How can you reduce the risk of container escape?

### Answer

Use defense in depth:

```text
Non-root
+
No Privileged Containers
+
Drop Capabilities
+
Seccomp
+
AppArmor / SELinux
+
Restricted HostPath
+
Restricted Host Namespaces
+
Updated Kernel
+
Updated Container Runtime
```

Also monitor runtime behavior for escape indicators.

---

# Interview Scenario 3

### Question

> What is the difference between Seccomp and AppArmor?

### Answer

Seccomp primarily restricts:

```text
System Calls
```

AppArmor primarily controls:

```text
Application Behavior / Resource Access
```

They operate at different layers and can complement each other.

---

# Interview Scenario 4

### Question

> Why is running a container as root dangerous?

### Answer

If the application is compromised, the attacker may initially obtain root privileges inside the container.

Although container root is not automatically equivalent to host root, elevated privileges can increase the impact of misconfigurations and escape vulnerabilities.

Therefore:

```yaml
runAsNonRoot: true
```

is preferred where possible.

---

# Interview Scenario 5

### Question

> How would you detect a reverse shell in Kubernetes?

### Answer

Correlate:

```text
Unexpected Shell Process
+
Unexpected Outbound Connection
```

For example:

```text
Web Application
      ↓
/bin/sh
      ↓
External IP
```

Use:

```text
Runtime Detection
+
Network Monitoring
+
NetworkPolicy
+
Egress Controls
```

---

# Interview Scenario 6

### Question

> What would you do if a production Pod is suspected to be compromised?

### Answer

First:

```text
Validate the alert
```

Then:

```text
Identify Pod
 ↓
Identify Node
 ↓
Identify Image
 ↓
Collect Evidence
 ↓
Contain
 ↓
Investigate
 ↓
Rotate Exposed Credentials
 ↓
Rebuild From Trusted Image
 ↓
Redeploy
 ↓
Monitor
```

Avoid destroying evidence before determining what needs to be preserved.

---

# Production Runtime Security Checklist

```text
☑ Run containers as non-root
☑ Disable privilege escalation
☑ Drop unnecessary capabilities
☑ Use seccomp
☑ Use AppArmor / SELinux
☑ Avoid privileged containers
☑ Restrict hostPath
☑ Restrict host namespaces
☑ Limit ServiceAccount permissions
☑ Use NetworkPolicy
☑ Restrict egress
☑ Monitor processes
☑ Monitor network activity
☑ Monitor sensitive file access
☑ Monitor system calls where appropriate
☑ Use runtime threat detection
☑ Integrate with SIEM
☑ Patch kernel and runtime
☑ Maintain incident response procedures
☑ Test runtime controls
```

---

# Recommended Practice

1. Run a Pod as non-root.
2. Disable privilege escalation.
3. Drop all unnecessary capabilities.
4. Enable `RuntimeDefault` seccomp.
5. Review AppArmor or SELinux availability.
6. Inspect privileged Pods.
7. Inspect `hostPath` usage.
8. Inspect `hostNetwork`.
9. Inspect `hostPID`.
10. Review ServiceAccount permissions.
11. Configure NetworkPolicy.
12. Monitor process execution.
13. Study eBPF.
14. Deploy Falco in a disposable cluster.
15. Deploy a suitable Tetragon lab.
16. Generate controlled runtime events.
17. Detect unexpected shell execution.
18. Detect unexpected network connections.
19. Study container escape defenses.
20. Build a runtime detection rule.
21. Integrate runtime events with a SIEM.
22. Practice incident response.
23. Practice evidence collection.
24. Design a runtime security architecture.
25. Build a production runtime-security checklist.

---

# References

## Official / Industry Documentation

- Kubernetes Security Contexts
- Kubernetes Pod Security Standards
- Kubernetes Seccomp
- Linux Capabilities
- Linux Namespaces
- Linux cgroups
- AppArmor
- SELinux
- eBPF
- Falco
- Tetragon
- Kubernetes Audit Logging
- Kubernetes NetworkPolicy
- Kubernetes RBAC
- Container Runtime Security Documentation

---

# Chapter Summary

Runtime security protects Kubernetes workloads while they are executing.

Image security answers:

```text
What are we deploying?
```

Runtime security asks:

```text
What is the workload doing right now?
```

A workload can originate from a trusted image and still become compromised because of:

```text
Application Vulnerability
Credential Theft
Dependency Exploitation
Remote Code Execution
Misconfiguration
```

Runtime security therefore monitors:

```text
Processes
Files
Network
System Calls
Privileges
```

Important Linux security mechanisms include:

```text
Namespaces
Capabilities
Seccomp
AppArmor
SELinux
```

A strong baseline is:

```yaml
securityContext:

  runAsNonRoot: true

  allowPrivilegeEscalation: false

  capabilities:

    drop:

    - ALL

  seccompProfile:

    type: RuntimeDefault
```

The exact configuration must be tested against application requirements.

Avoid unnecessary:

```text
Privileged Containers
hostPath
hostNetwork
hostPID
hostIPC
```

because these can weaken workload isolation.

Linux capabilities provide fine-grained privilege control.

Instead of giving a container full root privileges:

```text
Drop Everything
      ↓
Add Only Required Capabilities
```

Seccomp restricts system calls.

AppArmor and SELinux provide additional mandatory access-control mechanisms.

Runtime monitoring can detect:

```text
Unexpected Shells
Reverse Shells
Malware
Crypto Mining
Sensitive File Access
Privilege Escalation
Unexpected Network Connections
```

eBPF has become an important technology for modern runtime security because it can provide deep kernel-level visibility into:

```text
Processes
System Calls
Network Activity
Kubernetes Workloads
```

Tools such as:

```text
Falco
Tetragon
```

can use runtime and kernel-level telemetry for threat detection, with different architectures and capabilities.

Runtime detection should avoid simplistic rules.

Instead of:

```text
Shell = Attack
```

use contextual detection:

```text
Unexpected Shell
+
Unexpected External Connection
+
Sensitive File Access
```

This produces stronger security signals.

Runtime security should also integrate with:

```text
NetworkPolicy
RBAC
Pod Security
Image Security
SIEM
Incident Response
```

A mature runtime-security architecture is:

```text
                     Kubernetes
                         │
                         ▼
                        Pod
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Process      Network      Files
             │           │           │
             └───────────┼───────────┘
                         ▼
                    eBPF / Sensor
                         │
                         ▼
                  Detection Engine
                         │
                         ▼
                        SIEM
                         │
                         ▼
                       SOC
                         │
                         ▼
                 Incident Response
```

If a runtime compromise occurs:

```text
Detect
 ↓
Validate
 ↓
Contain
 ↓
Preserve Evidence
 ↓
Investigate
 ↓
Rotate Credentials
 ↓
Rebuild
 ↓
Recover
 ↓
Monitor
```

The most important principle is:

> **Runtime security assumes that prevention can fail and continuously verifies workload behavior during execution.**

A secure Kubernetes environment therefore follows:

```text
Prevent
+
Detect
+
Respond
+
Recover
```

rather than relying on image scanning or configuration hardening alone.

---

## Next Chapter

# Chapter 56 – Supply Chain Security

Topics will include:

- Kubernetes Software Supply Chain
- Supply Chain Security Fundamentals
- Software Supply Chain Threat Model
- Source Code Security
- Dependency Security
- Dependency Confusion
- Typosquatting
- Malicious Packages
- Compromised Dependencies
- Container Image Supply Chain
- Base Image Security
- Image Provenance
- SBOM
- SPDX
- CycloneDX
- Image Signing
- Cosign
- Sigstore
- Rekor
- Fulcio
- SLSA
- Build Provenance
- Reproducible Builds
- Secure CI/CD
- Build Isolation
- Build Attestations
- Artifact Integrity
- Registry Security
- Image Immutability
- Digest Pinning
- Admission Control
- Policy Enforcement
- Trusted Builders
- Software Bill of Materials
- Vulnerability Management
- Secret Security in CI/CD
- GitOps Supply Chain
- Helm Supply Chain Security
- Kubernetes Admission Security
- Dependency Pinning
- Artifact Promotion
- Release Security
- Supply Chain Attack Scenarios
- Compromised CI/CD
- Malicious Image
- Dependency Confusion Attack
- Build System Compromise
- Signing Key Compromise
- Incident Response
- Supply Chain Forensics
- Production Supply Chain Architecture
- Hands-on Labs
- Common Mistakes
- Best Practices
- Quick Revision
- Interview Questions
- References

---