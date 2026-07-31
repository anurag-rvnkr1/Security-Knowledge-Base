# Cloud Security Cheat Sheet

## Overview

The Cloud Security Cheat Sheet is a quick-reference guide that consolidates the most important cloud security concepts, best practices, commands, principles, frameworks, and interview-ready facts into a single chapter. It is designed for rapid revision before interviews, certifications, security assessments, audits, and day-to-day cloud operations.

Rather than providing lengthy explanations, this cheat sheet focuses on concise, high-value information that can be quickly referenced by:

- Students
- Freshers
- Cloud Engineers
- Cloud Security Engineers
- SOC Analysts
- DevSecOps Engineers
- Security Architects
- Penetration Testers
- Incident Responders
- Compliance Professionals

---

## Why It Matters

Cloud environments evolve rapidly, making it difficult to remember every security concept, framework, service, and best practice.

A well-structured cheat sheet helps you:

- Revise quickly before interviews
- Recall important security principles
- Reduce common implementation mistakes
- Improve troubleshooting efficiency
- Prepare for certifications
- Standardize cloud security practices
- Support incident response activities
- Reinforce security-by-design principles

---

## Architecture

```
                  Cloud Users

                       │

                       ▼

            Identity & Access Management

                       │

                       ▼

               Zero Trust Controls

                       │

                       ▼

              Network Security Layer

                       │

                       ▼

         Compute • Containers • Kubernetes

                       │

                       ▼

          Applications • APIs • Serverless

                       │

                       ▼

           Data Protection & Encryption

                       │

                       ▼

         Monitoring • Logging • Detection

                       │

                       ▼

      Incident Response • Compliance • Audit

                       │

                       ▼

      Governance • DevSecOps • Improvement
```

---

## Key Concepts

### Shared Responsibility Model

| Cloud Provider Secures | Customer Secures |
|-------------------------|------------------|
| Physical infrastructure | Identities |
| Global network | Applications |
| Hypervisor | Data |
| Hardware | IAM policies |
| Managed services | Configurations |
| Cloud availability | Workloads |

---

### CIA Triad

| Principle | Purpose |
|-----------|---------|
| Confidentiality | Prevent unauthorized disclosure |
| Integrity | Prevent unauthorized modification |
| Availability | Ensure reliable access to systems and data |

---

### AAA Security Model

| Component | Purpose |
|----------|---------|
| Authentication | Verify identity |
| Authorization | Control permissions |
| Accounting (Auditing) | Record user activity |

---

### Zero Trust Principles

- Never trust, always verify
- Verify every identity
- Verify device posture
- Enforce least privilege
- Assume breach
- Continuously monitor
- Limit lateral movement
- Authenticate every request

---

### Principle of Least Privilege (PoLP)

Grant only the permissions required to perform a task.

Apply PoLP to:

- Users
- Roles
- Service accounts
- APIs
- Applications
- Containers
- Virtual machines

---

### Defense in Depth

```
Users
   │
IAM
   │
Network Security
   │
Application Security
   │
Data Encryption
   │
Monitoring
   │
Incident Response
```

Multiple security layers reduce the impact of individual control failures.

---

### Cloud Service Models

| Model | Customer Manages | Provider Manages |
|--------|------------------|------------------|
| IaaS | OS, Applications, Data | Infrastructure |
| PaaS | Applications, Data | Platform + Infrastructure |
| SaaS | Data & Configuration | Entire Platform |

---

### Cloud Deployment Models

| Model | Description |
|--------|-------------|
| Public Cloud | Shared provider infrastructure |
| Private Cloud | Dedicated organizational infrastructure |
| Hybrid Cloud | Combination of public and private cloud |
| Multi-Cloud | Multiple cloud providers |
| Community Cloud | Shared by organizations with common requirements |

---

### IAM Quick Facts

Always:

- Enable Multi-Factor Authentication (MFA)
- Use Role-Based Access Control (RBAC)
- Enforce least privilege
- Rotate credentials
- Review permissions regularly
- Disable unused accounts
- Monitor privileged activity

Never:

- Share credentials
- Use root accounts for daily tasks
- Hardcode secrets
- Grant unnecessary administrator access

---

### Encryption Quick Reference

| Type | Protects |
|------|----------|
| At Rest | Stored data |
| In Transit | Network communication |
| End-to-End | Sender-to-recipient communication |

Common algorithms:

- AES-256
- RSA
- ECC
- SHA-256 (Hashing)
- TLS 1.3

---

### Cloud Network Security Checklist

- Private subnets
- Security Groups
- Network ACLs
- Web Application Firewall (WAF)
- DDoS protection
- VPN or private connectivity
- Network segmentation
- Micro-segmentation
- Bastion hosts
- DNS security

---

### Data Protection Checklist

- Encrypt data at rest
- Encrypt data in transit
- Enable backups
- Test restores
- Classify sensitive data
- Rotate encryption keys
- Secure object storage
- Restrict access
- Enable audit logging
- Implement Data Loss Prevention (DLP)

---

### DevSecOps Essentials

Integrate security into every stage of the software development lifecycle.

Typical pipeline:

```
Plan

 │

 ▼

Code

 │

 ▼

Build

 │

 ▼

Security Scan

 │

 ▼

Test

 │

 ▼

Deploy

 │

 ▼

Monitor

 │

 ▼

Improve
```

Key controls:

- SAST
- DAST
- SCA
- IaC Scanning
- Container Scanning
- Secrets Scanning
- Artifact Signing

---

### Incident Response Phases

| Phase | Purpose |
|--------|---------|
| Preparation | Build readiness |
| Identification | Detect incidents |
| Containment | Limit impact |
| Eradication | Remove the threat |
| Recovery | Restore operations |
| Lessons Learned | Improve future response |

---

### Top Cloud Security Principles

1. Security by Design
2. Defense in Depth
3. Zero Trust
4. Least Privilege
5. Secure Defaults
6. Continuous Monitoring
7. Automation
8. Continuous Compliance
9. Risk-Based Decision Making
10. Continuous Improvement

---

## How It Works

The Cloud Security Cheat Sheet is intended to serve as a rapid-reference resource rather than a replacement for detailed documentation. It summarizes the most important concepts, controls, and best practices into concise sections that can be reviewed in minutes.

It is especially useful:

- Before technical interviews
- During certification preparation
- While designing cloud architectures
- During security assessments
- While responding to incidents
- During compliance audits
- When troubleshooting cloud environments

---

# Cloud Security Quick Reference Workflow

```
Understand Requirements

          │

          ▼

Identify Assets

          │

          ▼

Protect Identities

          │

          ▼

Secure Networks

          │

          ▼

Protect Data

          │

          ▼

Secure Workloads

          │

          ▼

Monitor Activity

          │

          ▼

Detect Threats

          │

          ▼

Respond & Recover

          │

          ▼

Continuously Improve
```

Every stage reinforces the overall security posture of the cloud environment.

---

## Practical Example

### Example 1 – Securing a New Cloud Environment

Before deploying workloads, verify:

| Area | Checklist |
|------|-----------|
| IAM | MFA enabled, RBAC configured, Least Privilege applied |
| Network | Private subnets, Security Groups, WAF configured |
| Storage | Encryption enabled, Public access disabled |
| Compute | Latest patches installed, Secure baseline applied |
| Logging | Audit logs enabled, Centralized logging configured |
| Backup | Automated backups enabled and tested |

---

### Example 2 – Quick Security Review Before Production

Review the following questions:

- Are administrator accounts protected with MFA?
- Are secrets stored in a Secrets Manager?
- Is encryption enabled everywhere required?
- Are unnecessary ports closed?
- Are logs being collected centrally?
- Are backups tested?
- Has the infrastructure passed compliance checks?
- Have vulnerabilities been remediated?

If every answer is **Yes**, the deployment is significantly more secure.

---

### Example 3 – Interview Revision

Suppose you have only **15 minutes** before a Cloud Security interview.

Suggested revision order:

1. Shared Responsibility Model
2. IAM
3. Zero Trust
4. Encryption
5. Networking
6. Containers & Kubernetes
7. DevSecOps
8. Monitoring & SIEM
9. Incident Response
10. Compliance Frameworks

This sequence covers the topics most frequently discussed in interviews.

---

### Example 4 – Security Assessment

During a cloud security review, quickly verify:

```
✓ IAM Policies

✓ MFA

✓ Encryption

✓ Logging

✓ Monitoring

✓ Backups

✓ Vulnerability Scanning

✓ Compliance

✓ Incident Response

✓ Disaster Recovery
```

This checklist provides a high-level health assessment before deeper technical analysis.

---

## Detection

The cheat sheet can also be used to quickly recall the indicators of common cloud security issues.

---

### Identity Threat Indicators

Watch for:

- Impossible travel logins
- Multiple failed login attempts
- Privilege escalation
- Unexpected administrator creation
- Disabled MFA
- Suspicious API token usage

---

### Network Threat Indicators

Monitor for:

- Port scanning
- Unusual outbound traffic
- Lateral movement
- DNS anomalies
- Unexpected internet exposure
- Distributed Denial-of-Service (DDoS) attacks

---

### Workload Threat Indicators

Look for:

- Unauthorized process execution
- Unexpected software installation
- Container privilege escalation
- Cryptocurrency mining
- Reverse shells
- Runtime policy violations

---

### Data Threat Indicators

Identify:

- Public storage buckets
- Large data downloads
- Unexpected database access
- Backup failures
- Encryption disabled
- Sensitive data exfiltration

---

### Configuration Drift Indicators

Detect:

- Firewall rule changes
- IAM permission changes
- Disabled logging
- Open storage permissions
- Missing encryption
- Unapproved infrastructure modifications

Continuous validation tools help identify drift before it becomes a security incident.

---

### Compliance Indicators

Continuously verify:

- Encryption compliance
- Resource tagging
- Logging configuration
- Backup policies
- Password policies
- Regulatory control adherence

Automated compliance monitoring reduces manual audit effort.

---

## Quick Detection Checklist

| Security Domain | Primary Indicators |
|-----------------|-------------------|
| Identity | Failed logins, privilege escalation, disabled MFA |
| Network | Port scans, lateral movement, abnormal traffic |
| Compute | Malware, unauthorized processes, runtime anomalies |
| Storage | Public access, excessive downloads, encryption disabled |
| Applications | API abuse, authentication failures, code vulnerabilities |
| Compliance | Policy violations, configuration drift, missing controls |

---

## Memory Aids

### CIA Triad

```
C → Confidentiality

I → Integrity

A → Availability
```

---

### Incident Response

```
Prepare

↓

Identify

↓

Contain

↓

Eradicate

↓

Recover

↓

Lessons Learned
```

---

### Zero Trust

```
Never Trust

↓

Always Verify

↓

Least Privilege

↓

Continuous Monitoring
```

---

