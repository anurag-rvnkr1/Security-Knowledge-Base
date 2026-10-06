# Chapter 75 – Runtime Threat Detection

## Overview

Runtime Threat Detection is the process of identifying suspicious or malicious activity while Kubernetes workloads, containers, nodes, and cluster components are actively running.

Unlike vulnerability scanning, which primarily asks:

```text
"What could be vulnerable?"
```

runtime threat detection asks:

```text
"What is happening right now?"
```

A modern Kubernetes security architecture therefore combines:

```text
Image Security
      +
Configuration Security
      +
Identity Security
      +
Network Security
      +
Runtime Threat Detection
```

Runtime detection can identify behaviors such as:

```text
Unexpected Shell Execution
Privilege Escalation
Container Escape Attempts
Sensitive File Access
Suspicious Network Connections
Cryptocurrency Mining
Malware Execution
Credential Access
Kubernetes API Abuse
Persistence
Lateral Movement
```

A simplified runtime detection lifecycle is:

```text
Runtime Activity
      ↓
Telemetry
      ↓
Detection
      ↓
Alert
      ↓
Triage
      ↓
Investigation
      ↓
Containment
      ↓
Incident Response
```

---

# Learning Objectives

After completing this chapter, you will understand:

- Runtime threat detection fundamentals
- Runtime security
- Runtime vs image security
- Runtime vs vulnerability scanning
- Runtime attack surface
- Process monitoring
- File monitoring
- Network monitoring
- System call monitoring
- Container monitoring
- Pod monitoring
- Node monitoring
- Kubernetes API monitoring
- Behavioral detection
- Anomaly detection
- Rule-based detection
- Signature-based detection
- eBPF
- Linux Security Modules
- seccomp
- AppArmor
- SELinux
- Falco
- Tetragon
- Tracee
- Runtime security architecture
- Container escape detection
- Privilege escalation detection
- Suspicious shell detection
- Unexpected process detection
- Sensitive file access
- Credential access
- Secret access
- Network connection detection
- DNS detection
- Reverse shell detection
- Cryptocurrency mining detection
- Malware detection
- Persistence detection
- Kubernetes API abuse
- `kubectl exec` detection
- ServiceAccount abuse
- RBAC abuse
- Host namespace abuse
- Privileged container detection
- HostPath detection
- Capability abuse
- Namespace monitoring
- Runtime policies
- Detection rules
- Alert severity
- Alert triage
- False positives
- Detection engineering
- Threat intelligence
- MITRE ATT&CK
- Kubernetes Threat Matrix
- SIEM integration
- SOAR integration
- Incident-response integration
- Runtime telemetry
- eBPF-based security
- Production runtime security
- Performance considerations
- Detection coverage
- Security monitoring
- Best practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions

---

# What Is Runtime Security?

Runtime security protects workloads while they are executing.

Conceptually:

```text
Container Image
      ↓
Deployment
      ↓
Running Container
      ↓
Runtime Security
```

Runtime security can observe:

```text
Processes
Files
Network
System Calls
Container Events
Kubernetes Activity
```

---

# Runtime vs Image Security

Image scanning:

```text
Before Deployment
```

Runtime security:

```text
During Execution
```

Example:

```text
Image Scan
   ↓
No Known CVE
   ↓
Application Starts
   ↓
Compromised Dependency Exploits Runtime
   ↓
Runtime Detection
```

---

# Runtime vs Vulnerability Scanning

| Vulnerability Scanning | Runtime Detection |
|---|---|
| Finds known weaknesses | Detects behavior |
| Mostly static | Dynamic |
| Package/config focused | Process/network/syscall focused |
| Pre-deployment and periodic | Continuous |
| CVE-oriented | Behavior-oriented |

Both are required.

---

# Runtime Attack Surface

Potential runtime targets include:

```text
Container
Pod
Node
Kernel
Container Runtime
Kubernetes API
ServiceAccount
Network
Filesystem
Secrets
```

---

# Runtime Telemetry

Runtime security can collect:

```text
Process Events
File Events
Network Events
System Calls
Container Events
Kubernetes API Events
```

---

# Process Monitoring

Monitor:

```text
Process Creation
Process Termination
Parent/Child Relationships
Command Arguments
Executable Paths
User IDs
Capabilities
```

---

# Suspicious Process Example

A web application container normally runs:

```text
python app.py
```

Suddenly:

```text
/bin/sh
```

appears.

This may be suspicious.

---

# Shell Detection

Detect unexpected:

```text
/bin/sh
/bin/bash
/bin/zsh
```

inside application containers.

However, legitimate administrative or debugging activity can also create shells, so context is essential.

---

# Process Anomaly

Example:

```text
Expected:
python
gunicorn

Observed:
curl
wget
bash
nc
```

This may indicate:

```text
Command Execution
Post-Exploitation
Tool Download
Network Activity
```

---

# Parent-Child Process Analysis

Process relationships can reveal suspicious behavior.

Example:

```text
nginx
  └── /bin/sh
       └── curl
```

This is potentially suspicious because the web server spawned a shell that launched an external utility.

---

# File Monitoring

Monitor sensitive files such as:

```text
/etc/passwd
/etc/shadow
/etc/ssh/
```

and application-sensitive locations.

---

# Sensitive File Access

Unexpected access to:

```text
/etc/shadow
Cloud Credential Files
SSH Keys
ServiceAccount Data
Application Secrets
```

can indicate credential theft.

---

# File Modification

Detect:

```text
Unexpected Binary Creation
Modified System Files
Persistence Files
Malware Drops
Configuration Changes
```

---

# Network Monitoring

Monitor:

```text
Outbound Connections
Inbound Connections
Ports
Protocols
Destination IPs
DNS
Connection Frequency
```

---

# Suspicious Network Connection

Example:

```text
Application Pod
      ↓
Unknown External IP
      ↓
Unusual Port
```

This may require investigation.

---

# DNS Monitoring

DNS activity can reveal:

```text
Command-and-Control
Malware Infrastructure
Data Exfiltration
Unexpected External Services
```

---

# DNS Anomalies

Potential indicators:

```text
High Query Volume
Random-Looking Domains
New External Domains
Known Malicious Domains
Frequent Failed Queries
```

---

# System Call Monitoring

Linux applications interact with the kernel through system calls.

Examples include:

```text
execve
openat
connect
ptrace
mount
setuid
```

Runtime security tools can monitor system-call behavior.

---

# Why System Calls Matter

Instead of only observing:

```text
Process = bash
```

security telemetry can reveal:

```text
Process
 ↓
execve()
 ↓
New Command
```

This provides more behavioral context.

---

# eBPF

eBPF allows programs to run safely within the Linux kernel infrastructure and observe or enforce certain system and networking behaviors.

Security tools can use eBPF for:

```text
Process Monitoring
Network Monitoring
System Call Visibility
Security Detection
```

---

# eBPF Security Architecture

Conceptually:

```text
Application
     ↓
Kernel
     ↓
eBPF
     ↓
Telemetry
     ↓
Detection Engine
     ↓
Alert
```

---

# Advantages of eBPF

Potential benefits:

```text
Low-Level Visibility
Rich Telemetry
Efficient Event Collection
Kernel-Level Context
```

Actual performance depends on implementation and workload.

---

# eBPF Limitations

Consider:

```text
Kernel Compatibility
Program Complexity
Performance Overhead
Operational Complexity
Data Volume
```

---

# seccomp

seccomp restricts the system calls available to a process.

Conceptually:

```text
Application
     ↓
System Call
     ↓
seccomp Policy
     ↓
Allow / Restrict
```

---

# Why seccomp Matters

If an application does not need certain system calls, restricting them can reduce attack surface.

---

# seccomp and Detection

seccomp is primarily a restriction mechanism, but violations or blocked behavior can also provide security signals depending on configuration and runtime.

---

# AppArmor

AppArmor provides Linux security policies based on application profiles.

It can restrict:

```text
File Access
Capabilities
Network Behavior
```

---

# SELinux

SELinux provides mandatory access control based on security labels and policies.

It can restrict interactions between:

```text
Processes
Files
Resources
```

---

# Linux Security Controls

Important mechanisms include:

```text
seccomp
AppArmor
SELinux
Linux Capabilities
Namespaces
cgroups
```

These complement runtime detection.

---

# Falco

Falco is a runtime security and threat detection project commonly used to detect suspicious behavior across Linux, containers, and Kubernetes environments.

It can detect events such as:

```text
Shell Execution
Unexpected Process
Sensitive File Access
Network Activity
Privilege Changes
```

---

# Falco Architecture

Conceptually:

```text
Kernel / Runtime
       ↓
Event Collection
       ↓
Falco Rules
       ↓
Detection
       ↓
Alert
       ↓
SIEM / SOC
```

---

# Falco Rule Concept

A rule conceptually contains:

```text
Event
+
Condition
+
Output
+
Priority
```

Example concept:

```text
If a shell is executed inside a production container
and the process is unexpected
then generate a high-priority alert.
```

---

# Tetragon

Tetragon is a Kubernetes-aware runtime security and observability project that uses eBPF-based mechanisms to provide process and security visibility and enforcement capabilities.

It can help monitor:

```text
Process Execution
Network Activity
Privilege Changes
Kubernetes Context
```

---

# Tracee

Tracee is an eBPF-based tracing and security tool that can provide visibility into Linux events and detect suspicious behaviors.

It can assist with:

```text
System Call Monitoring
Security Events
Process Activity
Container Activity
```

---

# Runtime Security Tools

| Tool | Primary Focus |
|---|---|
| Falco | Runtime threat detection |
| Tetragon | eBPF-based runtime enforcement/observability |
| Tracee | eBPF tracing and security |
| seccomp | System-call restriction |
| AppArmor | Mandatory application profiles |
| SELinux | Mandatory access control |

---

# Runtime Detection Architecture

```text
                Kubernetes Cluster
                       │
        ┌──────────────┼──────────────┐
        ▼              ▼              ▼
     Pods            Nodes         API Server
        │              │              │
        └──────────────┼──────────────┘
                       ▼
                 Runtime Sensors
                       │
              ┌────────┴────────┐
              ▼                 ▼
            eBPF            Runtime Events
              │                 │
              └────────┬────────┘
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

---

# Behavioral Detection

Behavioral detection looks for activity that deviates from expected behavior.

Example:

```text
Expected:
Web Server → Database

Observed:
Web Server → External IP → Unusual Port
```

---

# Anomaly Detection

Anomaly detection identifies activity outside an expected baseline.

Example:

```text
Normal:
10 API Calls / Minute

Observed:
10,000 API Calls / Minute
```

This may indicate:

```text
Abuse
Enumeration
Compromise
Misconfiguration
```

---

# Rule-Based Detection

Rule-based detection uses predefined conditions.

Example:

```text
IF
container executes shell
AND
container label = production

THEN
generate alert
```

---

# Signature-Based Detection

Signature detection looks for known patterns.

Examples:

```text
Known Malware Hash
Known Command Pattern
Known Network Indicator
Known Exploit Signature
```

---

# Behavioral vs Signature Detection

| Signature | Behavioral |
|---|---|
| Known pattern | Suspicious behavior |
| Good for known threats | Good for novel behavior |
| Can be precise | Can generate more false positives |

Use both where appropriate.

---

# Detection Engineering

Detection engineering is the process of designing:

```text
Telemetry
 ↓
Detection Logic
 ↓
Alert
 ↓
Investigation Context
```

---

# Good Detection

A useful alert should answer:

```text
What happened?
Where?
When?
Who?
Why is it suspicious?
```

---

# Bad Detection

Example:

```text
"Something suspicious happened."
```

This provides insufficient context.

---

# Alert Context

A useful runtime alert may include:

```text
Cluster
Namespace
Pod
Container
Node
Process
User
Command
Image
Image Digest
Source IP
Destination IP
Timestamp
```

---

# Alert Severity

Common levels:

```text
Critical
High
Medium
Low
Informational
```

Severity should reflect:

```text
Behavior
Impact
Confidence
Asset Criticality
```

---

# False Positives

A legitimate action can look malicious.

Example:

```text
kubectl exec
```

may be used by:

```text
Administrator
Developer
Automation
Attacker
```

Therefore:

```text
Detection
 ↓
Context
 ↓
Validation
```

is required.

---

# Reducing False Positives

Use:

```text
Allow Lists
Context
Labels
Namespaces
ServiceAccounts
Expected Processes
Expected Network Destinations
```

Do not create overly broad exclusions.

---

# Production Context

Consider:

```text
Production
Staging
Development
```

A shell in a development container may be expected.

A shell in a hardened production application container may be much more suspicious.

---

# Container Escape Detection

Potential signals include:

```text
Unexpected Host Access
Privileged Container
Host Namespace Usage
Sensitive Device Access
Unexpected Mount
Suspicious Kernel Interaction
```

---

# Privileged Container Detection

Monitor Pods using:

```yaml
securityContext:
  privileged: true
```

Privileged workloads require strong justification.

---

# Host Namespace Detection

Monitor:

```yaml
hostPID: true
hostNetwork: true
hostIPC: true
```

These can increase the attack surface.

---

# HostPath Detection

Monitor:

```yaml
volumes:
  - hostPath:
```

Host filesystem access can create security risk.

---

# Capability Abuse

Linux capabilities can provide additional privileges.

Monitor dangerous or unnecessary capabilities.

Example:

```yaml
capabilities:
  add:
    - SYS_ADMIN
```

Capabilities should be minimized.

---

# Privilege Escalation

Monitor:

```text
setuid
setgid
Capability Changes
Privilege Changes
Unexpected Root Processes
```

---

# Kubernetes API Abuse

Runtime security should complement Kubernetes audit logging.

Monitor suspicious:

```text
Pod Creation
Secret Access
RBAC Changes
ServiceAccount Changes
Exec
Port Forwarding
Node Access
```

---

# kubectl exec Detection

Unexpected:

```text
kubectl exec
```

may indicate:

```text
Interactive Access
Troubleshooting
Post-Exploitation
```

Correlate:

```text
Identity
Source IP
Pod
Command
Time
```

---

# ServiceAccount Abuse

Monitor:

```text
Unexpected API Activity
Unusual Namespace Access
Secret Enumeration
RBAC Queries
Mass Resource Discovery
```

---

# RBAC Abuse

Potential indicators:

```text
New ClusterRoleBinding
New RoleBinding
Wildcard Permissions
Privilege Changes
```

---

# Secret Access Detection

Monitor access to:

```text
Kubernetes Secrets
Cloud Credentials
Application Credentials
SSH Keys
```

Unexpected access should be investigated.

---

# Reverse Shell Detection

Potential behavioral signals:

```text
Shell
+
Network Connection
+
Unexpected Parent Process
```

For example:

```text
Web Server
 ↓
Shell
 ↓
Outbound Connection
```

This combination may be highly suspicious.

---

# Cryptocurrency Mining Detection

Indicators may include:

```text
Sustained High CPU
Unknown Mining Process
Mining Pool Connections
Unexpected External Traffic
```

---

# Malware Detection

Potential indicators:

```text
Unknown Binary
Suspicious Process
Known Hash
Persistence
Unexpected Network
File Modification
```

---

# Persistence Detection

Monitor creation or modification of:

```text
Deployments
DaemonSets
CronJobs
Jobs
ServiceAccounts
Secrets
Admission Components
```

---

# Namespace Monitoring

Monitor sensitive namespaces such as:

```text
kube-system
Production Namespaces
Security Namespaces
Infrastructure Namespaces
```

---

# kube-system Monitoring

Unexpected changes in `kube-system` can be particularly important because it commonly contains cluster infrastructure components.

---

# Runtime Policies

Runtime policies can define:

```text
Allowed Processes
Allowed Network
Allowed Files
Allowed Capabilities
Allowed System Calls
```

---

# Policy Example

Conceptually:

```text
Application Container
Allowed:
    python
    gunicorn

Unexpected:
    bash
    curl
    nc
```

An unexpected process should generate a security signal.

---

# Runtime Enforcement

Some security systems can do more than detect.

They may:

```text
Block
Kill
Isolate
Deny
```

Use enforcement carefully in production.

---

# Detection vs Prevention

Detection:

```text
Observe
 ↓
Alert
```

Prevention:

```text
Observe
 ↓
Block
```

A mature security architecture uses both.

---

# MITRE ATT&CK

Runtime detections can map to attacker behaviors such as:

```text
Execution
Persistence
Privilege Escalation
Defense Evasion
Credential Access
Discovery
Lateral Movement
Command and Control
Exfiltration
Impact
```

---

# Kubernetes Threat Matrix

Kubernetes-specific threat frameworks can help map attacker techniques to Kubernetes components.

Examples include behaviors involving:

```text
Kubernetes API
RBAC
Pods
Secrets
ServiceAccounts
Container Runtime
Cloud Infrastructure
```

---

# Detection Coverage

A security team should ask:

```text
Can We Detect Shell Execution?
Can We Detect Secret Access?
Can We Detect Privilege Escalation?
Can We Detect Container Escape?
Can We Detect Suspicious Network Activity?
Can We Detect RBAC Abuse?
```

---

# Detection Coverage Matrix

| Behavior | Detection Source |
|---|---|
| Shell Execution | Runtime |
| API Abuse | Audit Logs |
| Secret Access | Audit Logs |
| Network Anomaly | Network |
| Process Anomaly | Runtime |
| Container Escape | Runtime + Node |
| RBAC Change | Audit Logs |
| Malicious Image | Image Scanner |
| Persistence | Kubernetes + Runtime |

---

# Runtime Security and SIEM

Runtime events should flow into the SOC:

```text
Runtime Sensor
      ↓
Detection
      ↓
SIEM
      ↓
Correlation
      ↓
SOC
```

---

# Correlation Example

Individually:

```text
Shell Execution
```

may be low severity.

But:

```text
Shell Execution
+
Secret Access
+
External Network Connection
```

may indicate a serious incident.

---

# SIEM Correlation

Conceptually:

```text
Event A
+
Event B
+
Event C
 ↓
High Confidence Alert
```

---

# SOAR Integration

SOAR can automate safe response workflows:

```text
Runtime Alert
 ↓
SOAR
 ↓
Create Incident
 ↓
Enrich IOC
 ↓
Notify Analyst
 ↓
Quarantine if Approved
```

---

# Runtime Security and Incident Response

Runtime detection feeds incident response:

```text
Detection
 ↓
Triage
 ↓
Investigation
 ↓
Containment
 ↓
Eradication
 ↓
Recovery
```

---

# Runtime Security and Vulnerability Management

These controls answer different questions:

```text
Vulnerability Management:
"What weaknesses exist?"

Runtime Security:
"What suspicious activity is occurring?"
```

Together:

```text
Known Weakness
+
Observed Exploitation
=
High Priority
```

---

# Runtime Security and Image Security

Example:

```text
Image Scan
 ↓
No Known CVEs
 ↓
Deploy
 ↓
Compromised Credentials
 ↓
Malicious Activity
 ↓
Runtime Detection
```

No single security control is sufficient.

---

# Performance Considerations

Runtime telemetry consumes:

```text
CPU
Memory
Storage
Network
```

Optimize:

```text
Event Volume
Sampling
Rules
Retention
Aggregation
```

---

# High Event Volume

A large cluster may generate millions of events.

Avoid collecting everything without a purpose.

Focus on:

```text
High-Value Events
+
Security-Relevant Context
```

---

# Runtime Detection Pipeline

```text
Kernel
 ↓
Events
 ↓
Filter
 ↓
Enrich
 ↓
Detect
 ↓
Prioritize
 ↓
Alert
 ↓
SIEM
```

---

# Event Enrichment

Add context such as:

```text
Namespace
Pod
Container
Image
Node
ServiceAccount
Labels
Owner
Environment
```

This makes alerts more actionable.

---

# Detection Tuning

After deployment:

```text
Observe
 ↓
Review Alerts
 ↓
Identify False Positives
 ↓
Tune
 ↓
Measure
```

---

# Detection Quality Metrics

Track:

```text
True Positives
False Positives
Detection Coverage
Mean Time To Detect
Mean Time To Respond
Alert Volume
```

---

# Mean Time To Detect

MTTD measures:

```text
Incident Occurrence
        ↓
Detection
```

Lower is generally better.

---

# Mean Time To Respond

MTTR can measure:

```text
Detection
 ↓
Response
```

Organizations should define exactly which timestamps their metrics use.

---

# Runtime Security Architecture

A production architecture can look like:

```text
                    Kubernetes
                        │
       ┌────────────────┼─────────────────┐
       ▼                ▼                 ▼
    Pods              Nodes          API Server
       │                │                 │
       └────────────────┼─────────────────┘
                        ▼
               Runtime Telemetry
                        │
              ┌─────────┴─────────┐
              ▼                   ▼
             eBPF             Audit Logs
              │                   │
              └─────────┬─────────┘
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

---

# Production Runtime Security Strategy

Use layered controls:

```text
Secure Image
      +
Secure Configuration
      +
Least Privilege
      +
Network Security
      +
Runtime Detection
      +
Incident Response
```

---

# Common Mistakes

## 1. Relying Only on Image Scanning

A clean image can still be compromised at runtime.

---

## 2. Alerting on Everything

Excessive alerts create:

```text
Alert Fatigue
```

---

## 3. No Context

A raw process event is often insufficient.

Enrich it with:

```text
Pod
Namespace
Image
User
Node
```

---

## 4. Ignoring False Positives

Poorly tuned detections become unusable.

---

## 5. Overly Broad Exceptions

An exception such as:

```text
Ignore all bash
```

can hide real attacks.

---

## 6. Automatically Killing Everything Suspicious

Aggressive enforcement can cause:

```text
Application Outage
Evidence Loss
Operational Damage
```

---

## 7. Ignoring the Node

Container activity can be connected to node-level compromise.

---

## 8. Ignoring Kubernetes Audit Logs

Runtime telemetry alone does not show the complete control-plane story.

---

## 9. No Baseline

Without knowing expected behavior, anomaly detection becomes difficult.

---

## 10. Ignoring Performance

Excessive telemetry can create operational overhead.

---

# Best Practices

### 1. Monitor Runtime Behavior

Track:

```text
Process
File
Network
System Calls
```

---

### 2. Use eBPF Where Appropriate

Use mature tools and validate kernel compatibility.

---

### 3. Combine Detection Sources

Use:

```text
Runtime
+
Audit
+
Network
+
Cloud
```

---

### 4. Enrich Alerts

Include:

```text
Pod
Namespace
Container
Image
Node
Identity
```

---

### 5. Tune Detections

Continuously reduce:

```text
False Positives
Alert Noise
```

---

### 6. Maintain Baselines

Understand normal behavior.

---

### 7. Protect Sensitive Namespaces

Increase monitoring around:

```text
kube-system
Production
Security
Infrastructure
```

---

### 8. Use Least Privilege

Reduce the impact of compromise.

---

### 9. Integrate With SIEM

Centralize detection and correlation.

---

### 10. Integrate With Incident Response

Every high-confidence detection should have a response path.

---

# Hands-on Lab 1 – Process Monitoring

Deploy a test application.

Observe:

```bash
ps aux
```

Identify:

```text
Expected Processes
Unexpected Processes
```

---

# Hands-on Lab 2 – Shell Detection

Deploy a container.

Generate a controlled shell event.

Use your runtime-security tool to detect:

```text
/bin/sh
```

or:

```text
/bin/bash
```

---

# Hands-on Lab 3 – File Monitoring

Create a test workload that accesses a monitored file.

Detect:

```text
File Access
Process
Container
Timestamp
```

---

# Hands-on Lab 4 – Network Detection

Deploy a test Pod and generate controlled outbound traffic.

Monitor:

```text
Source Pod
Destination
Port
Protocol
Process
```

---

# Hands-on Lab 5 – DNS Detection

Generate controlled DNS requests.

Observe:

```text
Domain
Source Pod
Timestamp
Frequency
```

---

# Hands-on Lab 6 – Falco

Install Falco in a disposable Kubernetes environment.

Generate a controlled suspicious event.

Observe:

```text
Rule
Priority
Container
Process
Namespace
```

---

# Hands-on Lab 7 – Tetragon

Deploy Tetragon in a test cluster.

Observe:

```text
Process Events
Network Events
Security Events
```

---

# Hands-on Lab 8 – Tracee

Deploy Tracee in a suitable test environment.

Generate controlled Linux events.

Observe:

```text
System Calls
Process Activity
Container Context
```

---

# Hands-on Lab 9 – Privileged Pod Detection

Create a test Pod with:

```yaml
securityContext:
  privileged: true
```

Create a runtime detection rule for privileged workloads.

---

# Hands-on Lab 10 – Host Namespace Detection

Create a controlled Pod using:

```yaml
hostPID: true
```

Detect the configuration and runtime behavior.

---

# Hands-on Lab 11 – Capability Detection

Create a test Pod with an additional Linux capability.

Detect:

```text
Capability
Container
Namespace
```

---

# Hands-on Lab 12 – kubectl exec Detection

Perform:

```bash
kubectl exec
```

on a test Pod.

Correlate:

```text
Audit Log
+
Runtime Event
```

---

# Hands-on Lab 13 – ServiceAccount Abuse Simulation

Create a test ServiceAccount.

Perform authorized API operations.

Generate detection signals for:

```text
Unexpected Namespace Access
Secret Enumeration
RBAC Enumeration
```

---

# Hands-on Lab 14 – Cryptomining Detection Simulation

Use a harmless CPU-intensive workload.

Detect:

```text
High CPU
Unexpected Process
Network Connection
```

Do not use real mining software in the lab.

---

# Hands-on Lab 15 – SIEM Integration

Send runtime alerts to a SIEM.

Create a correlation rule:

```text
Shell Execution
+
Secret Access
+
External Connection
```

Generate a high-confidence alert.

---

# Hands-on Lab 16 – SOAR Integration

Create a safe workflow:

```text
Runtime Alert
 ↓
SIEM
 ↓
SOAR
 ↓
Create Incident
 ↓
Notify Analyst
```

Add analyst approval before disruptive actions.

---

# Hands-on Lab 17 – Detection Tuning

Generate:

```text
10 Legitimate Shell Events
2 Suspicious Shell Events
```

Tune the detection to reduce false positives without suppressing suspicious activity.

---

# Hands-on Lab 18 – Runtime Security Dashboard

Create a dashboard showing:

```text
Runtime Alerts
Top Threats
Affected Namespaces
Affected Pods
Process Events
Network Events
Severity
MTTD
```

---

# Hands-on Lab 19 – Detection Coverage

Create a matrix:

```text
Threat
Detection
Telemetry
Coverage
```

Include:

```text
Shell
Privilege Escalation
Secret Access
Container Escape
Network Anomaly
RBAC Abuse
Persistence
```

---

# Hands-on Lab 20 – Full Runtime Threat Detection Exercise

Simulate:

```text
Compromised Application
        ↓
Unexpected Shell
        ↓
Credential Access
        ↓
External Network Connection
```

Detect:

```text
Process
File
Network
API
```

Then execute:

```text
Triage
 ↓
Containment
 ↓
Investigation
 ↓
Eradication
```

---

# Quick Revision

## Runtime Security

```text
Security monitoring and protection during workload execution
```

---

## Runtime Threat Detection

```text
Detect suspicious behavior while systems are running
```

---

## eBPF

```text
Linux kernel technology used for efficient observability and security tooling
```

---

## seccomp

```text
Restricts system calls available to a process
```

---

## AppArmor

```text
Linux application security profiles
```

---

## SELinux

```text
Mandatory access control based on security labels and policies
```

---

## Falco

```text
Runtime threat detection
```

---

## Tetragon

```text
eBPF-based Kubernetes-aware runtime observability and enforcement
```

---

## Tracee

```text
eBPF-based Linux tracing and security
```

---

## Behavioral Detection

```text
Detect suspicious behavior
```

---

## Signature Detection

```text
Detect known patterns
```

---

## Anomaly Detection

```text
Detect deviation from expected behavior
```

---

## IOC

```text
Indicator of Compromise
```

---

## IOA

```text
Indicator of Attack
```

---

# Essential Commands

List Pods:

```bash
kubectl get pods -A
```

Pod details:

```bash
kubectl describe pod <pod>
```

Pod YAML:

```bash
kubectl get pod <pod> -o yaml
```

Pod logs:

```bash
kubectl logs <pod>
```

Previous logs:

```bash
kubectl logs <pod> --previous
```

Pod placement:

```bash
kubectl get pods -A -o wide
```

Events:

```bash
kubectl get events -A
```

ServiceAccounts:

```bash
kubectl get serviceaccounts -A
```

Roles:

```bash
kubectl get roles -A
```

RoleBindings:

```bash
kubectl get rolebindings -A
```

ClusterRoleBindings:

```bash
kubectl get clusterrolebindings
```

NetworkPolicies:

```bash
kubectl get networkpolicy -A
```

Deployments:

```bash
kubectl get deployments -A
```

DaemonSets:

```bash
kubectl get daemonsets -A
```

CronJobs:

```bash
kubectl get cronjobs -A
```

Check runtime containers:

```bash
crictl ps -a
```

Check runtime images:

```bash
crictl images
```

Inspect runtime container:

```bash
crictl inspect <container-id>
```

kubelet logs:

```bash
journalctl -u kubelet
```

Kernel logs:

```bash
journalctl -k
```

Processes:

```bash
ps aux
```

Network connections:

```bash
ss -antp
```

---

# Interview Questions

## Basic

- What is runtime security?
- What is runtime threat detection?
- How is runtime security different from image scanning?
- What is eBPF?
- What is seccomp?
- What is AppArmor?
- What is SELinux?
- What is Falco?
- What is Tetragon?
- What is Tracee?
- What is behavioral detection?
- What is anomaly detection?
- What is signature-based detection?
- What is an IOC?
- What is an IOA?

---

## Intermediate

- How would you detect a shell inside a container?
- How would you detect suspicious processes?
- How would you detect container escape attempts?
- How would you detect privilege escalation?
- How would you detect suspicious network connections?
- How would you detect cryptomining?
- How would you detect ServiceAccount abuse?
- How would you detect RBAC abuse?
- How would you detect unexpected `kubectl exec` activity?
- How do eBPF-based security tools work?
- Why is runtime detection important if images are scanned?
- How do you reduce runtime-security false positives?
- How do you integrate runtime alerts with a SIEM?

---

## Advanced

- Design a runtime threat-detection architecture for a production Kubernetes cluster.
- How would you detect container escape behavior?
- How would you detect lateral movement from a compromised Pod?
- How would you combine Kubernetes audit logs with runtime telemetry?
- How would you design behavioral detections for Kubernetes?
- How would you use eBPF for Kubernetes security?
- How would you balance runtime visibility against performance overhead?
- How would you design a detection strategy for a 1,000-node cluster?
- How would you detect a compromised ServiceAccount?
- How would you detect persistence in Kubernetes?
- How would you map Kubernetes detections to MITRE ATT&CK?
- How would you integrate runtime detection with SOAR and incident response?

---

# Interview Scenario 1

### Question

> A web application container suddenly executes `/bin/bash`. Is this automatically an attack?

### Answer

No.

It is a suspicious signal, but context is required.

Investigate:

```text
Who
When
Which Pod
Which Image
Parent Process
Command
Namespace
User
Network Activity
```

If a normal application process unexpectedly launches a shell followed by:

```text
Credential Access
+
External Network Connection
```

the confidence of malicious activity increases significantly.

---

# Interview Scenario 2

### Question

> Why is runtime security required if we already scan container images?

### Answer

Image scanning identifies known vulnerabilities before or around deployment.

Runtime security identifies malicious or unexpected behavior after the workload starts.

Example:

```text
Clean Image
 ↓
Credential Compromise
 ↓
Attacker Executes Shell
 ↓
Runtime Detection
```

Therefore both controls are complementary.

---

# Interview Scenario 3

### Question

> How would you detect container escape attempts?

### Answer

Monitor for:

```text
Privileged Containers
+
Host Namespace Usage
+
HostPath
+
Dangerous Capabilities
+
Unexpected Device Access
+
Suspicious Kernel Interaction
```

Combine runtime telemetry with Kubernetes configuration and node-level monitoring.

---

# Interview Scenario 4

### Question

> What is the advantage of eBPF for runtime security?

### Answer

eBPF enables security tooling to observe low-level Linux behavior with rich kernel context.

It can provide visibility into:

```text
Process Execution
System Calls
Network Activity
Container Context
```

This can enable detailed detection without requiring intrusive application instrumentation.

---

# Interview Scenario 5

### Question

> How would you reduce false positives in a runtime detection system?

### Answer

Use:

```text
Baselines
+
Context
+
Expected Process Lists
+
Namespace Context
+
ServiceAccount Context
+
Network Allow Lists
+
Application Ownership
```

Then continuously measure and tune detections.

---

# Interview Scenario 6

### Question

> How would you detect a cryptomining attack?

### Answer

Correlate:

```text
Sustained High CPU
+
Unexpected Process
+
Unknown External Connection
+
Mining-Related Destination
```

The combination provides stronger evidence than CPU usage alone.

---

# Interview Scenario 7

### Question

> How would you detect ServiceAccount abuse?

### Answer

Monitor:

```text
API Activity
+
Identity
+
Namespace
+
Resource
+
Verb
```

Look for:

```text
Unexpected Secret Access
RBAC Enumeration
Cluster-Wide Enumeration
Privilege Changes
```

---

# Interview Scenario 8

### Question

> How would you integrate runtime detection with a SOC?

### Answer

Use:

```text
Runtime Sensor
 ↓
Detection Engine
 ↓
SIEM
 ↓
Correlation
 ↓
SOC
 ↓
Incident Response
```

Add:

```text
SOAR
```

for controlled automation.

---

# Interview Scenario 9

### Question

> What would a high-confidence runtime alert look like?

### Answer

Instead of:

```text
Shell detected
```

provide:

```text
Production Pod
+
Unexpected bash
+
Web server spawned shell
+
Secret file accessed
+
Outbound connection to unknown IP
```

This gives analysts actionable context.

---

# Interview Scenario 10

### Question

> Design a complete Kubernetes runtime security architecture.

### Answer

```text
                Kubernetes
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
       Pod          Node       API Server
        │            │            │
        └────────────┼────────────┘
                     ▼
              Runtime Telemetry
                     │
             ┌───────┴────────┐
             ▼                ▼
            eBPF          Audit Logs
             │                │
             └───────┬────────┘
                     ▼
              Detection Engine
                     │
             ┌───────┴────────┐
             ▼                ▼
            SIEM             SOAR
             │                │
             ▼                ▼
            SOC          Response Actions
             │
             ▼
       Incident Response
```

Security controls should also include:

```text
seccomp
AppArmor / SELinux
NetworkPolicies
RBAC
Pod Security
Image Security
Admission Controls
```

---

# Production Runtime Security Checklist

```text
☑ Runtime monitoring enabled
☑ Process monitoring enabled
☑ Network monitoring enabled
☑ File monitoring enabled where required
☑ Kubernetes audit logging enabled
☑ eBPF-based visibility evaluated
☑ seccomp configured
☑ AppArmor / SELinux evaluated
☑ Privileged Pods monitored
☑ Host namespaces monitored
☑ HostPath monitored
☑ Dangerous capabilities monitored
☑ Shell execution monitored
☑ Sensitive file access monitored
☑ Secret access monitored
☑ ServiceAccount activity monitored
☑ RBAC changes monitored
☑ Suspicious network connections monitored
☑ DNS activity monitored
☑ Persistence monitored
☑ Container escape signals monitored
☑ SIEM integration configured
☑ Detection rules documented
☑ Alert severity defined
☑ False positives tracked
☑ Detection tuning process defined
☑ Incident-response integration tested
☑ Runtime telemetry performance monitored
☑ Detection coverage reviewed
```

---

# Chapter Summary

Runtime threat detection focuses on what is happening while Kubernetes workloads are running.

Important telemetry includes:

```text
Processes
Files
Network
System Calls
Kubernetes API
Containers
Nodes
```

Important technologies include:

```text
eBPF
seccomp
AppArmor
SELinux
Falco
Tetragon
Tracee
```

A mature runtime security architecture follows:

```text
Collect
 ↓
Enrich
 ↓
Detect
 ↓
Prioritize
 ↓
Alert
 ↓
Investigate
 ↓
Respond
```

Runtime detection is strongest when combined with:

```text
Image Security
+
Vulnerability Management
+
RBAC
+
Network Policies
+
Pod Security
+
Audit Logging
+
Incident Response
```

The most important principle is:

> **Do not rely solely on what software contains; continuously monitor what workloads actually do at runtime, correlate behavior with Kubernetes and identity context, and respond to high-confidence threats before they become larger incidents.**

---

## Next Chapter

# Chapter 76 – Compliance & Auditing

Topics will include:

- Kubernetes Compliance Fundamentals
- Security Auditing
- Compliance vs Security
- Governance
- Risk Management
- Regulatory Requirements
- Security Policies
- Kubernetes Audit Logs
- Audit Policy
- Audit Levels
- Audit Backends
- Log Retention
- Evidence Collection
- Evidence Integrity
- Access Control
- RBAC Auditing
- ServiceAccount Auditing
- Authentication Auditing
- Authorization Auditing
- Admission Auditing
- Network Policy Auditing
- Pod Security Auditing
- Secret Access Auditing
- Container Image Compliance
- Image Provenance
- SBOM Compliance
- Supply Chain Compliance
- Vulnerability Management Compliance
- Patch Management
- Configuration Compliance
- CIS Kubernetes Benchmark
- NIST
- ISO 27001
- SOC 2
- PCI DSS
- HIPAA
- GDPR
- Data Protection
- Cloud Compliance
- Multi-Cluster Compliance
- Policy as Code
- OPA
- Gatekeeper
- Kyverno
- Admission Policies
- Continuous Compliance
- Compliance Monitoring
- Compliance Dashboards
- Audit Evidence
- Audit Trails
- Control Mapping
- Security Controls
- Control Validation
- Compliance Exceptions
- Risk Acceptance
- Remediation
- Compliance Reporting
- Internal Audits
- External Audits
- Third-Party Audits
- Audit Preparation
- Audit Findings
- Corrective Actions
- Preventive Actions
- Continuous Improvement
- Security Governance
- Production Compliance
- Best Practices
- Hands-on Labs
- Common Mistakes
- Quick Revision
- Interview Questions
- References

---