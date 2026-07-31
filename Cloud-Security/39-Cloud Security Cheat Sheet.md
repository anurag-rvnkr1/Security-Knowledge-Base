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

## Next Section

How It Works

Practical Example

Detection

Prevention

Best Practices

Common Mistakes

References

---