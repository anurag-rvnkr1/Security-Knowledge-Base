# Chapter 15 – Container Forensics

## Overview

Container Forensics is the discipline of collecting, preserving, analyzing, and reporting digital evidence from containerized environments after a security incident. It applies the principles of traditional digital forensics to Docker, Kubernetes, and other cloud-native platforms while addressing the unique characteristics of containers, such as their ephemeral nature, layered filesystems, and dynamic orchestration.

Unlike traditional virtual machines or physical servers, containers may exist for only a few seconds before being destroyed or replaced. As a result, investigators must rely on a combination of:

- Container metadata
- Runtime information
- Docker Engine artifacts
- Container images
- Host operating system evidence
- Centralized logs
- Cloud audit logs
- Registry metadata
- Orchestrator events

Container forensics plays a vital role in:

- Incident Response
- Threat Hunting
- Malware Analysis
- Insider Threat Investigations
- Compliance Audits
- Digital Evidence Collection
- Root Cause Analysis
- Legal and Regulatory Investigations

---

# Why It Matters

Suppose an attacker compromises a production container.

```
Internet

      │

      ▼

Web Container

      │

      ▼

Remote Code Execution

      │

      ▼

Credential Theft

      │

      ▼

Data Exfiltration

      │

      ▼

Container Deleted
```

Without forensic preparation:

- Evidence disappears.
- Runtime artifacts are lost.
- Root cause cannot be determined.
- Regulatory reporting becomes difficult.

With proper forensic readiness:

```
Incident

↓

Evidence Collection

↓

Analysis

↓

Timeline

↓

Root Cause

↓

Report
```

Organizations can reconstruct the attack and improve future defenses.

---

# What is Digital Forensics?

Digital forensics is the scientific process of:

- Identifying evidence
- Preserving evidence
- Collecting evidence
- Examining evidence
- Analyzing evidence
- Reporting findings

The objective is to maintain evidence integrity while determining what happened during an incident.

---

# Container Forensics Challenges

Containers introduce several unique challenges.

```
Ephemeral Containers

↓

Rapid Scaling

↓

Dynamic Networking

↓

Shared Kernel

↓

Layered Filesystems

↓

Short-Lived Processes
```

These characteristics require investigators to adapt traditional forensic techniques.

---

# Container Forensics Workflow

```
Incident

      │

Identify Evidence

      │

Preserve Evidence

      │

Collect Artifacts

      │

Analyze Evidence

      │

Build Timeline

      │

Determine Root Cause

      │

Prepare Report
```

Every step should follow organizational forensic procedures and applicable legal requirements.

---

# Sources of Evidence

Evidence may be collected from multiple layers.

```
Application

↓

Container

↓

Image

↓

Docker Engine

↓

Host Operating System

↓

Cloud Platform
```

No single source provides the complete picture.

---

# Container-Level Evidence

Examples include:

- Container metadata
- Running processes
- Environment variables
- Mounted volumes
- Container logs
- Network configuration
- Restart history
- Resource usage
- Image identifier

These artifacts help reconstruct container activity.

---

# Image-Level Evidence

Investigators may analyze:

- Base image
- Installed packages
- Image layers
- Dockerfile
- Build history
- Image digest
- Image signatures
- Software Bill of Materials (SBOM)

Image analysis helps identify vulnerable or malicious components.

---

# Host-Level Evidence

The Docker host often contains critical evidence.

Examples:

- System logs
- Docker daemon logs
- Authentication logs
- Kernel logs
- File system metadata
- Process information
- Network connections
- Memory artifacts (where applicable)

Host analysis is especially important if container isolation may have been bypassed.

---

# Cloud Evidence

Cloud-native environments generate valuable evidence.

Examples:

- Cloud audit logs
- Identity and access events
- Network flow logs
- Object storage logs
- Registry activity
- Security alerts
- Infrastructure change history

Cloud evidence helps reconstruct actions beyond the container itself.

---

# Registry Evidence

Container registries provide:

- Image history
- Tags
- Digests
- Push events
- Pull events
- User activity
- Image scanning results

Registry metadata can reveal when compromised images were introduced or deployed.

---

# Types of Evidence

## Volatile Evidence

Examples:

- Running processes
- Active network connections
- Memory contents
- Runtime environment variables
- Temporary files

Volatile evidence may disappear when a container stops.

---

## Non-Volatile Evidence

Examples:

- Images
- Dockerfiles
- Volumes
- Logs
- Audit records
- Registry metadata

These artifacts generally persist longer than runtime information.

---

# Chain of Custody

Evidence handling should be documented.

```
Collect

↓

Record

↓

Store

↓

Transfer

↓

Analyze

↓

Report
```

Maintaining a documented chain of custody helps preserve evidence integrity and supports legal or regulatory requirements.

---

# Timeline Analysis

Investigators reconstruct events chronologically.

```
Container Created

↓

Image Pulled

↓

Application Started

↓

Attack Began

↓

Privilege Escalation

↓

Data Access

↓

Container Removed
```

Timeline analysis helps identify attacker actions and system responses.

---

# Goals of Container Forensics

- Preserve evidence
- Reconstruct attacker activity
- Determine root cause
- Identify affected systems
- Support incident response
- Improve security controls
- Meet compliance obligations

---

# Key Concepts

## Forensic Readiness

Prepare logging, monitoring, and evidence collection capabilities before incidents occur.

---

## Evidence Preservation

Collect volatile evidence as early as possible while avoiding unnecessary modification of affected systems.

---

## Multi-Layer Investigation

Investigations should consider:

- Application
- Container
- Image
- Host
- Cloud
- Registry

to achieve a complete understanding of the incident.

---

## Integrity

Evidence should remain complete, accurate, and protected against unauthorized modification.

---

## Root Cause Analysis

Determine not only what happened, but also why it happened and how recurrence can be prevented.

---

## Documentation

Maintain detailed records throughout the investigation to support reporting, lessons learned, and compliance.

---

## How It Works

Container Forensics is the process of identifying, preserving, collecting, analyzing, and reporting digital evidence from containerized environments. Because containers can be terminated automatically or replaced within seconds, investigators must prioritize rapid evidence collection while maintaining forensic integrity.

Unlike traditional systems, container investigations rarely rely on a single evidence source. Instead, investigators correlate information from:

- Running containers
- Container images
- Docker Engine
- Host operating system
- Container registry
- Cloud infrastructure
- Monitoring systems
- Centralized logging
- SIEM platforms

The objective is to reconstruct the incident timeline and determine the attack path without unnecessarily modifying the affected environment.

---

# Container Forensics Workflow

```
Security Incident

        │

        ▼

Identify Evidence

        │

        ▼

Preserve Volatile Data

        │

        ▼

Collect Evidence

        │

        ▼

Correlate Evidence

        │

        ▼

Timeline Analysis

        │

        ▼

Root Cause Analysis

        │

        ▼

Investigation Report
```

Each phase should follow organizational forensic procedures and evidence handling requirements.

---

# Step 1 – Incident Identification

Investigation begins after:

```
Security Alert

↓

SIEM Alert

↓

Runtime Alert

↓

User Report

↓

Monitoring Alert
```

Example triggers:

- Container escape attempt
- Suspicious outbound traffic
- Malware detection
- Privilege escalation
- Unauthorized image deployment

---

# Step 2 – Preserve Volatile Evidence

Volatile evidence may disappear when the container stops.

Examples:

```
Running Processes

↓

Network Connections

↓

Temporary Files

↓

Memory

↓

Runtime Metadata
```

This information should be collected before replacing or removing the affected container whenever feasible.

---

# Step 3 – Collect Container Evidence

Typical evidence includes:

```
Container Metadata

↓

Container Logs

↓

Environment Variables

↓

Mounted Volumes

↓

Process List

↓

Network Configuration

↓

Restart History
```

These artifacts help reconstruct runtime activity.

---

# Step 4 – Collect Image Evidence

Investigators examine:

```
Image

↓

Layers

↓

Packages

↓

Build History

↓

Dockerfile

↓

Image Digest

↓

SBOM
```

Image analysis helps determine whether:

- A vulnerable base image was used
- Malicious software was introduced
- Unexpected changes occurred during the build process

---

# Step 5 – Collect Host Evidence

Since containers share the host kernel, investigators also examine:

```
Docker Daemon Logs

↓

Authentication Logs

↓

Kernel Logs

↓

System Logs

↓

Running Processes

↓

Filesystem Metadata
```

Host evidence is particularly important when investigating potential container escape or host compromise.

---

# Step 6 – Collect Cloud Evidence

Cloud-native deployments generate additional forensic artifacts.

Examples:

```
Cloud Audit Logs

↓

Identity Events

↓

Network Flow Logs

↓

Registry Activity

↓

Infrastructure Changes
```

Cloud logs help correlate events beyond the container environment.

---

# Step 7 – Correlate Evidence

No single artifact tells the complete story.

Example:

```
Application Log

+

Docker Events

+

Cloud Audit Log

+

SIEM Alert

+

Network Flow

↓

Complete Timeline
```

Correlation improves confidence in investigative findings.

---

# Step 8 – Timeline Reconstruction

Investigators arrange events chronologically.

```
Image Pulled

↓

Container Created

↓

Application Started

↓

Attacker Login

↓

Privilege Escalation

↓

Credential Access

↓

Data Exfiltration

↓

Container Deleted
```

Timeline analysis identifies:

- Initial access
- Attacker movement
- Impact
- Response actions

---

# Step 9 – Root Cause Analysis

Investigators determine:

- How the attacker gained access
- Which vulnerability was exploited
- Which systems were affected
- What data was accessed
- How similar incidents can be prevented

The objective is long-term improvement rather than simply restoring service.

---

# Real-World Investigation Workflow

Example:

```
Runtime Alert

↓

SOC Investigation

↓

Container Logs

↓

Docker Events

↓

Cloud Audit Logs

↓

Registry History

↓

Timeline

↓

Root Cause

↓

Incident Report
```

Multiple evidence sources are combined to produce a complete investigation.

---

# Practical Examples

## Example 1 – Malicious Process

Monitoring reports:

```
Container

↓

Unexpected Process

↓

Security Alert
```

Investigation:

```
Container Metadata

↓

Running Processes

↓

Logs

↓

Image History
```

Determine whether the process is legitimate or malicious.

---

## Example 2 – Suspicious Image

Registry activity shows:

```
Unknown Image

↓

Production Deployment
```

Investigators review:

- Registry history
- Image digest
- Build pipeline
- Deployment logs

to determine image provenance.

---

## Example 3 – Container Escape Investigation

Evidence sources:

```
Container Logs

↓

Docker Host Logs

↓

Kernel Messages

↓

Authentication Logs

↓

Cloud Audit Logs
```

Host analysis becomes critical when isolation boundaries may have been bypassed.

---

## Example 4 – Data Exfiltration

Monitoring detects:

```
Large Outbound Transfer

↓

Container

↓

Alert
```

Investigation correlates:

- Network flow logs
- Application logs
- Container metadata
- Cloud audit records

to determine the scope of data exposure.

---

# Hands-on Forensic Commands

> **Note:** These commands provide operational visibility into Docker environments. Organizations performing formal forensic investigations should follow approved evidence preservation procedures and use appropriate forensic tooling where required.

---

## List Running Containers

```bash
docker ps
```

Identify active containers.

---

## List All Containers

```bash
docker ps -a
```

Review current and recently stopped containers.

---

## Inspect Container Metadata

```bash
docker inspect container_name
```

Review:

- Configuration
- Environment variables
- Mounts
- Networks
- Image ID
- Restart policy

---

## View Container Logs

```bash
docker logs container_name
```

Review application activity and errors.

---

## Stream Container Logs

```bash
docker logs -f container_name
```

Observe live log output.

---

## Display Running Processes

```bash
docker top container_name
```

Identify expected and unexpected processes.

---

## Display Docker Events

```bash
docker events
```

Review lifecycle events including:

- Container creation
- Start
- Stop
- Restart
- Image pull
- Network creation

---

## View Resource Usage

```bash
docker stats
```

Identify unusual CPU, memory, or network utilization.

---

## Inspect Image Metadata

```bash
docker inspect image_name
```

Review image configuration.

---

## Review Image History

```bash
docker history image_name
```

Examine image layers and build history.

---

# Best Practices

### 1. Prepare for Forensics Before Incidents

Implement:

- Centralized logging
- Monitoring
- Audit logging
- Time synchronization
- Secure evidence storage

Preparation greatly improves investigative capability.

---

### 2. Collect Volatile Evidence First

Capture:

- Running processes
- Network connections
- Runtime metadata
- Temporary files

before the container terminates whenever practical.

---

### 3. Correlate Multiple Evidence Sources

Avoid relying on a single log or alert.

Combine:

- Container logs
- Docker metadata
- Host logs
- Cloud logs
- SIEM alerts
- Registry activity

for a comprehensive investigation.

---

### 4. Preserve Evidence Integrity

Record:

- Collection time
- Collector
- Source
- Hash values (where applicable)
- Storage location

Maintain evidence according to organizational forensic procedures.

---

### 5. Use Trusted Images During Recovery

After investigation:

```
Trusted Image

↓

Deploy

↓

Validate

↓

Production
```

Avoid restoring from potentially compromised images.

---

### 6. Document Every Investigation

Include:

- Timeline
- Findings
- Evidence sources
- Root cause
- Impact
- Recommendations

Clear documentation supports future investigations and lessons learned.

---

### 7. Improve Security Controls

Each investigation should strengthen:

- Monitoring
- Detection
- Incident response
- Image security
- CI/CD controls
- Runtime protection

Continuous improvement is a core objective of mature forensic practices.

---

## Common Mistakes

Container Forensics requires careful planning, disciplined evidence handling, and a deep understanding of container technology. Because containers are ephemeral and highly dynamic, traditional forensic approaches are often insufficient.

The following are the most common mistakes encountered during container forensic investigations.

---

# 1. Deleting the Container Before Collecting Evidence

The most common mistake is:

```
Security Alert

↓

Delete Container

↓

Evidence Lost
```

Potentially lost evidence includes:

- Running processes
- Runtime metadata
- Temporary files
- Network connections
- Memory-resident artifacts
- Recent logs

Whenever practical, preserve and collect relevant evidence before removing or replacing the container.

---

# 2. Ignoring Volatile Evidence

Volatile evidence disappears quickly.

Examples:

```
Running Processes

↓

Memory

↓

Network Connections

↓

Temporary Files
```

Investigators should prioritize volatile data collection early in the response process.

---

# 3. Investigating Only the Container

A container is only one layer of the environment.

Investigations should also include:

```
Container

↓

Image

↓

Docker Engine

↓

Host

↓

Cloud Platform

↓

Registry
```

Multi-layer investigations produce more accurate findings.

---

# 4. Forgetting the Host Operating System

Containers share the host kernel.

Potential host evidence includes:

- Authentication logs
- Kernel logs
- Docker daemon logs
- System logs
- File system metadata

If a container escape or privilege escalation occurred, host evidence becomes especially important.

---

# 5. Modifying the Evidence

Examples:

```
Install Tools

↓

Delete Files

↓

Restart Container

↓

Overwrite Logs
```

Every modification may change or destroy evidence.

When feasible, collect evidence before making changes, following organizational forensic procedures.

---

# 6. Not Synchronizing Time

Different systems may report different timestamps.

Example:

```
Container

10:15

↓

Host

10:13

↓

Cloud

10:16
```

Consistent time synchronization is essential for accurate timeline reconstruction.

---

# 7. Ignoring Registry Evidence

The registry may reveal:

- Image origin
- Push history
- Pull history
- Tags
- Digests
- User activity

Registry metadata often explains how compromised images reached production.

---

# 8. Assuming Logs Tell the Whole Story

Logs may be:

- Incomplete
- Deleted
- Altered
- Misconfigured

Correlate logs with:

- Docker events
- Monitoring data
- Cloud audit logs
- Runtime alerts
- Registry records

No single evidence source should be considered definitive.

---

# 9. Forgetting the CI/CD Pipeline

The compromise may have occurred during software delivery.

Possible attack path:

```
Source Code

↓

CI/CD

↓

Container Image

↓

Registry

↓

Production
```

Investigate:

- Build history
- Pipeline logs
- Artifact repositories
- Deployment records

---

# 10. Ignoring Cloud Audit Logs

Cloud platforms record valuable events.

Examples:

- Identity activity
- Resource creation
- Network changes
- Storage access
- Registry operations

Cloud audit logs frequently provide evidence unavailable inside the container.

---

# 11. Failing to Preserve Chain of Custody

Without documentation:

```
Evidence

↓

Unknown Handling

↓

Reduced Trust
```

Maintain records of:

- Collection time
- Collector
- Storage location
- Transfer history
- Integrity verification

This is especially important for regulated environments and legal proceedings.

---

# 12. No Timeline Reconstruction

Investigations should reconstruct events in order.

```
Image Pulled

↓

Container Started

↓

Initial Access

↓

Privilege Escalation

↓

Credential Access

↓

Data Exfiltration

↓

Container Removed
```

Without a timeline, determining cause and impact becomes much more difficult.

---

# 13. Trusting Compromised Systems Completely

Attackers may:

- Modify logs
- Remove evidence
- Hide processes
- Change timestamps
- Disable monitoring

Validate findings using multiple independent evidence sources whenever possible.

---

# 14. Focusing Only on Technical Evidence

Effective investigations also consider:

- Change records
- Deployment approvals
- User activity
- Administrative actions
- Security policies
- Operational procedures

Human actions and process failures may contribute to an incident.

---

# 15. Closing the Investigation Without Improvements

Incorrect workflow:

```
Incident Closed

↓

No Improvements
```

Recommended workflow:

```
Investigation

↓

Lessons Learned

↓

Improve Controls

↓

Update Playbooks

↓

Training

↓

Future Preparedness
```

Every investigation should strengthen the organization's security posture.

---

# Container Forensics Quick Revision

## Investigation Workflow

```
Incident

↓

Preserve Evidence

↓

Collect

↓

Analyze

↓

Correlate

↓

Timeline

↓

Root Cause

↓

Report
```

---

## Evidence Sources

```
Application

↓

Container

↓

Image

↓

Docker Engine

↓

Host

↓

Cloud

↓

Registry
```

A complete investigation typically combines evidence from multiple layers.

---

## Volatile vs Non-Volatile Evidence

| Volatile | Non-Volatile |
|----------|--------------|
| Running processes | Container images |
| Active network connections | Dockerfiles |
| Runtime metadata | Volumes |
| Memory (where applicable) | Registry metadata |
| Temporary files | Audit logs |

Volatile evidence should generally be collected first because it may disappear quickly.

---

## Common Investigation Commands

```bash
docker ps

docker ps -a

docker inspect

docker logs

docker logs -f

docker top

docker stats

docker events

docker history
```

These commands provide valuable operational information but should be used within approved forensic and incident response procedures.

---

# Container Forensics Checklist

| Topic | Status |
|--------|:------:|
| Understand Digital Forensics | ✓ |
| Understand Forensic Readiness | ✓ |
| Understand Evidence Collection | ✓ |
| Understand Volatile Evidence | ✓ |
| Understand Non-Volatile Evidence | ✓ |
| Understand Timeline Analysis | ✓ |
| Understand Chain of Custody | ✓ |
| Understand Multi-Layer Investigation | ✓ |
| Understand Image Analysis | ✓ |
| Understand Host Analysis | ✓ |
| Understand Registry Evidence | ✓ |
| Understand Cloud Evidence | ✓ |
| Understand Best Practices | ✓ |
| Understand Common Mistakes | ✓ |
| Understand Continuous Improvement | ✓ |

---

# References

## Docker Documentation

- Docker Engine Documentation
- Docker CLI Documentation
- Docker Logging Documentation
- Docker Security Documentation
- Docker Build Documentation

---

## CNCF Resources

- Kubernetes Forensics Guidance
- Falco Documentation
- OpenTelemetry Documentation
- Cloud Native Computing Foundation (CNCF)

---

## Security Standards

- NIST SP 800-61 Rev. 2 — Computer Security Incident Handling Guide *(or the latest revision adopted by your organization)*
- NIST SP 800-190 — Application Container Security Guide
- CIS Docker Benchmark
- OWASP Docker Security Cheat Sheet
- OWASP Container Security Verification Standard

---

## Threat Intelligence & Frameworks

- MITRE ATT&CK
- MITRE ATT&CK for Containers
- National Vulnerability Database (NVD)
- CVE Program
- ATT&CK Evaluations (where applicable)

---

## Supply Chain & Integrity

- Sigstore Documentation
- Notary Documentation
- SPDX Specification
- CycloneDX Specification
- SLSA (Supply-chain Levels for Software Artifacts)

---

## Books

- *Container Security* — Liz Rice
- *Incident Response & Computer Forensics* — Jason T. Luttgens, Matthew Pepe & Kevin Mandia
- *Practical Cloud Native Security with Falco* — Loris Degioanni
- *Digital Forensics and Incident Response* — Gerard Johansen

---

## Recommended Learning Resources

- Docker Official Documentation
- Linux Foundation Training
- CNCF Learning Paths
- NIST Computer Security Resource Center (CSRC)
- OWASP Projects
- SANS DFIR Resources

