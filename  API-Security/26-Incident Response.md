# 26 - API Incident Response

# Introduction

API Incident Response (API IR) is the structured process of identifying, analyzing, containing, eradicating, recovering from, and learning after security incidents involving APIs.

As APIs expose business-critical functionality and sensitive data, they have become a primary target for attackers.

A mature API Incident Response capability minimizes:

- Business disruption
- Data loss
- Financial impact
- Regulatory consequences
- Reputation damage
- Recovery time

```
Attack

   │

Detection

   │

Analysis

   │

Containment

   │

Eradication

   │

Recovery

   │

Lessons Learned

   ▼

Improved Security
```

---

# Learning Objectives

After completing this chapter, you will be able to:

- Understand the API Incident Response lifecycle.
- Prepare for API security incidents.
- Detect API attacks.
- Perform incident triage.
- Contain API compromises.
- Eradicate attacker persistence.
- Recover securely.
- Conduct post-incident analysis.
- Improve future security controls.

---

# What Is an API Security Incident?

An API security incident is any event that threatens the confidentiality, integrity, or availability of an API or the data it processes.

Examples include

- Authentication bypass
- Broken authorization
- Credential theft
- Token compromise
- Data exposure
- API abuse
- Business logic exploitation
- API gateway compromise
- Cloud credential exposure
- Supply chain compromise

---

# Incident Response Lifecycle

```
Preparation

      │

Detection

      │

Analysis

      │

Containment

      │

Eradication

      │

Recovery

      │

Lessons Learned
```

This lifecycle aligns with widely adopted security incident handling practices.

---

# Preparation

Preparation is the most important phase because it determines how effectively an organization responds.

Preparation includes

- Incident response plans
- Playbooks
- Logging
- Monitoring
- Detection rules
- Asset inventory
- Contact lists
- Backup procedures
- Training
- Tabletop exercises

---

# API Asset Inventory

Maintain an accurate inventory of

- Public APIs
- Internal APIs
- Partner APIs
- Mobile APIs
- API Gateways
- Authentication Services
- Databases
- Third-party APIs

Without an inventory, response efforts become significantly more difficult.

---

# Incident Severity Levels

| Severity | Example |
|----------|----------|
| Critical | Active data breach |
| High | Authentication bypass |
| Medium | API abuse affecting limited users |
| Low | Minor configuration issue |
| Informational | Suspicious activity requiring monitoring |

Severity determines escalation and response priorities.

---

# Incident Classification

Typical categories

- Authentication
- Authorization
- Data Exposure
- Malware
- Credential Compromise
- Denial of Service
- API Abuse
- Insider Activity
- Cloud Security
- Third-party Service

Proper classification improves response consistency.

---

# Detection

Incidents may be detected through

- SIEM alerts
- API Gateway alerts
- WAF alerts
- User reports
- SOC investigations
- Threat intelligence
- Monitoring dashboards
- Cloud alerts

```
Telemetry

     │

Detection Rules

     │

Alert

     ▼

SOC
```

---

# Initial Triage

The first questions responders should answer are

- What happened?
- When did it happen?
- Which APIs are affected?
- Which users are affected?
- Is the attack ongoing?
- Is sensitive data involved?
- Is business continuity affected?

Rapid triage supports timely containment.

---

# Incident Analysis

During analysis determine

- Attack vector
- Entry point
- Affected assets
- Impacted users
- Attacker objectives
- Timeline
- Scope
- Potential persistence

```
Alert

   │

Evidence

   │

Analysis

   │

Timeline

   ▼

Findings
```

---

# Evidence Collection

Collect evidence before making disruptive changes whenever possible.

Examples

- Application logs
- Gateway logs
- Authentication logs
- Audit logs
- Network captures
- Cloud audit records
- Container logs
- Memory snapshots (where appropriate)

Evidence should maintain integrity and chain of custody.

---

# Timeline Reconstruction

Reconstructing events helps understand attacker actions.

```
Login

   │

Privilege Escalation

   │

Data Access

   │

Configuration Change

   │

Detection

   ▼

Containment
```

Accurate timelines support both investigations and reporting.

---

# Indicators of Compromise (IOCs)

Common API-related IOCs include

- Unusual authentication failures
- Invalid token usage
- Unexpected administrative actions
- Large data exports
- Sequential object access
- Requests from unusual locations
- Requests to deprecated APIs
- Unexpected configuration changes

---

# Indicators of Attack (IOAs)

Unlike IOCs, IOAs focus on attacker behavior.

Examples

- API enumeration
- Privilege escalation attempts
- Token replay
- Excessive pagination
- High-rate object access
- API scraping
- Business workflow manipulation

Behavioral indicators often enable earlier detection.

---

# Containment

Containment limits further damage.

Possible actions

- Block malicious IP addresses
- Revoke tokens
- Disable compromised accounts
- Enable stricter rate limits
- Isolate affected services
- Disable vulnerable endpoints
- Apply temporary firewall rules

```
Incident

    │

Containment

    │

Attack Stopped

    ▼

Investigation
```

Containment should balance security with business continuity.

---

# Short-Term vs Long-Term Containment

| Short-Term | Long-Term |
|------------|-----------|
| Block IPs | Patch vulnerabilities |
| Disable accounts | Redesign controls |
| Revoke tokens | Improve monitoring |
| Restrict access | Update architecture |

Short-term actions stop the immediate threat, while long-term actions prevent recurrence.

---

# Eradication

After containment, remove the root cause.

Activities include

- Remove malicious accounts
- Patch vulnerable systems
- Rotate credentials
- Revoke compromised API keys
- Remove malware
- Eliminate persistence mechanisms
- Update configurations

Eradication should be validated before recovery.

---

# Credential Rotation

Rotate compromised

- API keys
- OAuth client secrets
- Database credentials
- Cloud credentials
- Certificates
- Service account secrets

Credential rotation reduces the likelihood of continued unauthorized access.

---

# Recovery

Recovery restores secure operations.

Checklist

- Validate patches.
- Restore services.
- Verify authentication.
- Test authorization.
- Confirm monitoring.
- Review logs.
- Notify stakeholders where required.

```
Patched System

      │

Validation

      │

Monitoring

      │

Normal Operations
```

Recovery should be gradual and carefully monitored.

---

# Communication During Incidents

Stakeholders may include

- Security Operations Center
- Engineering teams
- Management
- Legal
- Compliance
- Customer support
- External partners (when appropriate)

Communication should be timely, accurate, and coordinated.

---

# Regulatory Considerations

Depending on jurisdiction and industry, organizations may have obligations regarding

- Breach notification
- Evidence preservation
- Customer notification
- Regulatory reporting
- Audit documentation

Incident response processes should align with applicable legal and regulatory requirements.

---

# Digital Forensics

Digital forensics supports incident investigation by preserving and analyzing evidence.

Potential evidence sources

- API logs
- System logs
- Authentication records
- Memory captures
- Disk images
- Cloud audit trails
- Container artifacts

Forensic activities should preserve evidence integrity.

---

# Chain of Custody

Evidence should be tracked throughout its lifecycle.

```
Evidence

    │

Collection

    │

Documentation

    │

Storage

    │

Analysis

    ▼

Presentation
```

Maintaining chain of custody supports legal and investigative requirements.

---

# Threat Hunting

Threat hunting proactively searches for hidden attacker activity.

Examples

- Unauthorized API usage
- Dormant compromised accounts
- Abnormal service communication
- Suspicious administrative actions
- Unexpected API versions

Threat hunting complements reactive incident response.

---

# Threat Hunting Workflow

```
Hypothesis

     │

Telemetry Review

     │

Evidence

     │

Validation

     │

Findings

     ▼

Detection Improvement
```

---

# Post-Incident Review

Every significant incident should conclude with a structured review.

Review

- Root cause
- Timeline
- Detection effectiveness
- Response effectiveness
- Business impact
- Lessons learned
- Preventive actions

The goal is continuous improvement, not assigning blame.

---

# Root Cause Analysis

Determine

- Why the incident occurred
- Which control failed
- Why detection was delayed
- Which improvements reduce future risk

```
Incident

    │

Why?

    │

Why?

    │

Why?

    ▼

Root Cause
```

---

# Detection Engineering

Improve detections after every incident.

Examples

| Detection | Improvement |
|-----------|-------------|
| Authentication Abuse | Lower detection latency |
| API Enumeration | Add sequence detection |
| Token Replay | Detect duplicate token identifiers |
| Privilege Escalation | Monitor administrative endpoints |
| Data Exfiltration | Alert on abnormal export volume |

Each incident should strengthen future detection capabilities.

---

# SIEM Integration

Key telemetry sources

- API Gateway
- Authentication Service
- Identity Provider
- Application Logs
- Audit Logs
- Database Audit Logs
- Cloud Audit Logs
- WAF
- Kubernetes Audit Logs
- Endpoint Detection Platform

```
Telemetry

     │

Normalization

     │

Correlation

     │

Incident

     ▼

SOC
```

---

# Enterprise Incident Response Architecture

```
                 Clients

                    │

                    ▼

               API Gateway

                    │

      ┌─────────────┼─────────────┐

      ▼             ▼             ▼

   Application     Logs       Monitoring

      │             │             │

      └─────────────┼─────────────┘

                    ▼

                  SIEM

                    │

            Correlation Engine

                    │

          Incident Response Team

        ┌───────────┼───────────┐

        ▼           ▼           ▼

  Containment   Investigation  Recovery

                    │

                    ▼

              Lessons Learned
```

---

# API Incident Response Playbook

Example workflow

1. Receive alert.
2. Validate incident.
3. Classify severity.
4. Identify affected APIs.
5. Preserve evidence.
6. Contain the threat.
7. Eradicate the root cause.
8. Recover services.
9. Monitor for recurrence.
10. Conduct a post-incident review.

Documenting playbooks ensures consistent responses across incidents.

---

# Best Practices

Preparation

- Maintain current playbooks.
- Inventory all APIs.
- Conduct regular tabletop exercises.
- Test backups and recovery.

Response

- Preserve evidence.
- Contain quickly.
- Communicate clearly.
- Document every action.
- Validate recovery before closing the incident.

Improvement

- Update detections.
- Refine playbooks.
- Patch root causes.
- Share lessons learned.
- Track remediation to completion.

---

# Common Mistakes

Avoid

- Delaying containment.
- Destroying evidence during investigation.
- Failing to rotate compromised credentials.
- Poor incident documentation.
- Closing incidents without root cause analysis.
- Ignoring lessons learned.
- Restoring services before validating remediation.

---

# Key Takeaways

- Preparation is the foundation of effective incident response.
- Rapid detection and accurate triage reduce business impact.
- Evidence preservation supports investigation and compliance.
- Recovery should restore services securely while monitoring for recurrence.
- Every incident should drive measurable improvements to security controls and detection capabilities.

---

**Next:** Enterprise response workflows, ransomware and API-specific scenarios, advanced forensics, crisis communication, hands-on labs, troubleshooting, interview questions, chapter summary, and incident response maturity models.