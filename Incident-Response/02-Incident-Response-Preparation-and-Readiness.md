# Incident Response Preparation and Readiness

> **A practical enterprise guide to building the people, processes, technology, evidence, communications, and operational readiness required before a cybersecurity incident occurs.**

---

## Overview

The most effective incident response begins **before the incident**.

Organizations that wait until a breach occurs to decide:

- Who is responsible?
- Which systems are critical?
- Where are the logs?
- Who can isolate a server?
- Who can disable an account?
- Where are backups?
- Who contacts legal?
- How is evidence preserved?
- Who communicates with leadership?
- Which playbook should be followed?

are already operating at a disadvantage.

Incident response preparation establishes the capabilities required to respond quickly and consistently when security incidents occur.

A mature preparation program combines:

```text
People
   +
Processes
   +
Technology
   +
Visibility
   +
Evidence
   +
Communication
   +
Exercises
   +
Governance
```

The objective is not to predict every possible attack.

The objective is to build an organization that can **respond effectively even when the exact attack is unknown**.

---

# Why It Matters

During a major security incident, time is limited.

Attackers may be:

- Moving laterally
- Stealing credentials
- Establishing persistence
- Encrypting systems
- Exfiltrating data
- Deleting logs
- Disabling security controls

At the same time, defenders must make decisions.

```text
                    INCIDENT
                       │
        ┌──────────────┼──────────────┐
        │              │              │
        ▼              ▼              ▼
     Attacker       Business        Defender
     Activity        Impact          Decisions
        │              │              │
        └──────────────┼──────────────┘
                       │
                       ▼
                  Time Pressure
```

Preparation reduces the amount of decision-making that must happen from scratch.

---

# Incident Response Readiness Model

A mature IR program can be viewed as several interconnected capabilities.

```text
                         IR READINESS
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
      People               Process              Technology
        │                     │                     │
        ├── SOC              ├── IR Plan          ├── SIEM
        ├── IR Team          ├── Playbooks        ├── EDR
        ├── IT              ├── Escalation       ├── NDR
        └── Leadership      └── Communication     └── Cloud
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
                 Evidence            Exercises
                    │                   │
                    ▼                   ▼
                 Forensics          Tabletop
                                      Purple Team
```

---

# Preparation Objectives

An enterprise should be able to answer the following questions **before an incident occurs**:

### People

- Who leads an incident?
- Who investigates endpoints?
- Who handles cloud incidents?
- Who handles forensics?
- Who communicates with executives?
- Who contacts legal?

### Technology

- What telemetry is available?
- Is EDR deployed?
- Is SIEM operational?
- Are authentication logs retained?
- Are cloud audit logs enabled?

### Process

- How is an incident declared?
- How is severity assigned?
- How is escalation performed?
- Who can authorize containment?

### Evidence

- Where are logs stored?
- How are logs preserved?
- How is chain of custody maintained?
- How are forensic images handled?

### Recovery

- Are backups available?
- Are backups isolated?
- Has restoration been tested?
- Can critical services be rebuilt?

If the organization cannot answer these questions, there are likely readiness gaps.

---

# Incident Response Policy

An **incident response policy** establishes the organization's formal commitment to responding to cybersecurity incidents.

It should define:

- Purpose
- Scope
- Authority
- Roles
- Responsibilities
- Incident definitions
- Severity
- Escalation
- Evidence handling
- Communication
- Documentation
- Regulatory considerations
- Review frequency

The policy should answer:

> **Who has the authority to initiate and coordinate incident response?**

---

# Incident Response Plan

The IR plan translates policy into an operational framework.

A plan may define:

```text
Incident Detected
       │
       ▼
Create Incident Record
       │
       ▼
Assign Incident Commander
       │
       ▼
Classify Severity
       │
       ▼
Activate Response Team
       │
       ▼
Investigate
       │
       ▼
Contain
       │
       ▼
Eradicate
       │
       ▼
Recover
       │
       ▼
Review
```

The plan should be accessible during an outage or security incident.

It should not exist only as a document stored on a potentially compromised internal system.

---

# Incident Response Plan Components

A practical plan should contain:

```text
Purpose
Scope
Definitions
Roles
Contact Information
Severity Model
Escalation Process
Incident Lifecycle
Communication Plan
Evidence Handling
Legal Requirements
Technical Response
Business Continuity
Recovery
Documentation
Lessons Learned
Review Process
```

---

# Roles and Responsibilities

Preparation requires clearly defined ownership.

A common structure:

```text
                         Incident Commander
                                │
       ┌────────────────────────┼────────────────────────┐
       │                        │                        │
       ▼                        ▼                        ▼
      SOC                     IT/Infra                 Legal
       │                        │                        │
       ▼                        ▼                        ▼
Incident Response           System Owners           Privacy
       │
 ┌─────┼─────────────┬──────────────┐
 │     │             │              │
 ▼     ▼             ▼              ▼
IR   Hunt         Forensics        Cloud
```

Every organization may structure these responsibilities differently.

The important principle is:

> **Responsibilities must be clear before the incident begins.**

---

# RACI for Incident Response

A RACI model can help define ownership.

| Activity | SOC | IR | IT | Legal | Leadership |
|---|---|---|---|---|---|
| Alert Triage | R | C | I | I | I |
| Incident Declaration | C | R | C | C | I |
| Endpoint Isolation | C | R | R | I | I |
| Evidence Collection | C | R | C | C | I |
| Legal Assessment | I | C | I | R | C |
| Executive Communication | I | C | I | C | R |
| Recovery | C | C | R | I | C |
| Lessons Learned | C | R | C | C | C |

Where:

- **R** = Responsible
- **A** = Accountable
- **C** = Consulted
- **I** = Informed

The exact assignment depends on the organization's structure.

---

# Incident Response Contact Matrix

Maintain a contact matrix that is accessible during an incident.

Example:

```text
Incident Commander
Security Operations
Infrastructure
Identity
Cloud
Network
Application Security
Forensics
Legal
Privacy
Compliance
Communications
Executive Leadership
External IR Provider
Cloud Provider
Cyber Insurance
Law Enforcement
```

The matrix should contain appropriate:

- Names
- Roles
- Contact methods
- Escalation order
- Backup contacts

Avoid relying exclusively on corporate email.

If the organization loses access to its primary identity or email environment, alternative communication channels may be required.

---

# Emergency Communication

A mature IR plan should define secure communication channels.

Potential options include:

- Emergency phone bridge
- Secure messaging
- Dedicated incident channel
- Out-of-band communications
- Emergency conference bridge

During a suspected account compromise, avoid assuming that the compromised environment is trustworthy.

For example:

```text
Compromised Email
       │
       X
       │
       ▼
Secure Out-of-Band Channel
       │
       ▼
Incident Team
```

---

# Asset Inventory

Incident response depends heavily on knowing what exists.

An organization should maintain visibility into:

- Workstations
- Servers
- Network devices
- Applications
- Databases
- Cloud resources
- Containers
- Kubernetes clusters
- Identity systems
- SaaS applications
- Security infrastructure

A useful asset record may contain:

```text
Asset ID
Hostname
IP
Owner
Business Unit
Operating System
Environment
Criticality
Location
Application
Data Classification
EDR Status
Logging Status
Backup Status
```

---

# Critical Asset Identification

Not every system has equal business importance.

Organizations should identify:

### Tier 0

Identity and security infrastructure.

Examples:

- Domain Controllers
- Identity providers
- Privileged access systems
- Certificate authorities

### Tier 1

Critical business infrastructure.

Examples:

- Production databases
- Payment systems
- Core applications

### Tier 2

Important supporting systems.

Examples:

- Internal applications
- File servers
- Department systems

### Tier 3

Lower-criticality systems.

Examples:

- Test systems
- Development systems
- Non-production assets

This classification helps determine response priorities.

---

# Crown Jewels

The organization should identify its **crown jewels**.

These may include:

- Customer data
- Financial systems
- Intellectual property
- Source code
- Authentication infrastructure
- Production databases
- Cryptographic keys
- Cloud administration
- Payment infrastructure

During an incident, responders need to determine quickly:

> **Can the attacker reach the organization's most valuable assets?**

---

# Dependency Mapping

Critical services may depend on multiple systems.

For example:

```text
                 Customer Application
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
            API       Database     IAM
              │          │          │
              ▼          ▼          ▼
          Service A   Storage     Identity
```

If responders isolate one component without understanding dependencies, they may unintentionally disrupt critical services.

Dependency mapping therefore improves containment decisions.

---

# Logging Readiness

Logging is one of the most important IR preparation activities.

A basic enterprise telemetry model:

```text
Endpoints ───────┐
Servers ─────────┤
Network ─────────┤
Identity ────────┤
Cloud ───────────┤
Applications ────┤
Email ───────────┤
                 ▼
                SIEM
                 │
                 ▼
          Investigation
```

---

# Endpoint Logging

Useful endpoint telemetry includes:

- Process creation
- Command lines
- Parent-child process relationships
- Network connections
- File activity
- Authentication
- Services
- Scheduled tasks
- PowerShell activity
- Security control changes

Windows environments may use:

- Windows Event Logs
- Sysmon
- EDR

Linux environments may use:

- auditd
- journald
- authentication logs
- process telemetry
- EDR

---

# Network Logging

Important sources include:

- Firewall
- DNS
- Proxy
- VPN
- IDS/IPS
- NetFlow
- Network Detection and Response

Example:

```text
Endpoint
   │
   ├── DNS
   ├── HTTP
   ├── HTTPS
   ├── SMB
   └── RDP
        │
        ▼
     Network
        │
        ▼
Monitoring
```

---

# Identity Logging

Identity telemetry is essential for investigating modern attacks.

Collect relevant information about:

- Authentication
- MFA
- Password changes
- Account creation
- Privilege changes
- Group membership
- Token activity
- OAuth applications
- Service principals
- API keys

---

# Cloud Logging

Cloud environments require dedicated audit visibility.

Examples:

### AWS

- CloudTrail
- VPC Flow Logs
- GuardDuty
- IAM events

### Microsoft Cloud

- Entra ID sign-in logs
- Audit logs
- Defender telemetry
- Azure activity logs

### Google Cloud

- Cloud Audit Logs
- VPC Flow Logs
- Security Command Center

Without cloud audit logging, cloud incident investigation can become severely limited.

---

# Log Retention

Logs must remain available long enough to support investigations.

Retention should consider:

- Regulatory requirements
- Business requirements
- Threat dwell time
- Incident discovery delay
- Storage cost
- Forensic requirements

A useful concept is:

```text
Incident Discovery
       │
       │
       ▼
Historical Investigation
       │
       ▼
Required Log Retention
```

If an attacker remained undetected for months but logs were retained for only seven days, investigators may be unable to reconstruct the initial compromise.

---

# Time Synchronization

Incident timelines depend on accurate timestamps.

Systems should use a consistent time source.

Common approach:

```text
           NTP
            │
    ┌───────┼────────┐
    ▼       ▼        ▼
 Endpoint  Server   Network
    │       │        │
    └───────┼────────┘
            ▼
     Consistent Timeline
```

Without synchronization, investigators may see:

```text
Host A: 10:04
Host B: 09:58
SIEM:   10:11
```

even though the events occurred only seconds apart.

---

# EDR Readiness

Endpoint Detection and Response can significantly improve investigation capability.

A mature deployment should consider:

- Coverage
- Sensor health
- Telemetry retention
- Isolation capability
- Process visibility
- Network visibility
- File visibility
- Tamper protection

Questions to ask:

```text
How many endpoints have EDR?

Which endpoints do not?

Are critical servers covered?

Are sensors healthy?

Can responders isolate hosts?

Can historical telemetry be queried?
```

---

# SIEM Readiness

The SIEM should support:

- Centralized logging
- Search
- Correlation
- Alerting
- Investigation
- Retention
- Dashboards
- Incident management

The IR team should know:

```text
Which logs exist?
Where are they stored?
How far back can we search?
Who can access them?
How quickly can queries run?
```

---

# Evidence Readiness

Evidence handling should be designed before incidents.

Potential evidence includes:

```text
Memory
Disk
Logs
Network Captures
Cloud Logs
Authentication Data
Endpoint Artifacts
Email
Browser Artifacts
Files
Malware Samples
```

The organization should define:

- Collection procedures
- Storage
- Access control
- Hashing
- Chain of custody
- Retention
- Transfer procedures

---

# Chain of Custody

Chain of custody documents the handling of evidence.

Example:

```text
Evidence Identified
       │
       ▼
Collected
       │
       ▼
Hashed
       │
       ▼
Recorded
       │
       ▼
Transferred
       │
       ▼
Stored
       │
       ▼
Analyzed
       │
       ▼
Archived / Disposed
```

A basic record may contain:

```text
Evidence ID
Description
Collector
Collection Date
Collection Time
Source
Hash
Storage Location
Transfer History
Analyst
Purpose
```

---

# Backup Readiness

Backups are critical to recovery.

However:

> **A backup is not proven reliable until restoration has been tested.**

A mature backup strategy should consider:

- Offline backups
- Immutable backups
- Multiple recovery points
- Separate credentials
- Access controls
- Backup monitoring
- Restoration testing

Ransomware response particularly depends on backup resilience.

---

# Backup Architecture

A simplified resilient model:

```text
                 Production
                     │
                     ▼
                  Backup
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
      Recovery Copy        Immutable Copy
          │                     │
          ▼                     ▼
       Restore              Ransomware
       Testing              Protection
```

Backups should not depend entirely on the same identity and administrative infrastructure that could be compromised during an attack.

---

# Recovery Readiness

Organizations should identify:

- Critical services
- Recovery order
- Recovery owners
- Dependencies
- Recovery time objectives
- Recovery point objectives

### RTO

**Recovery Time Objective**

How quickly a service should be restored.

### RPO

**Recovery Point Objective**

How much data loss is acceptable.

Example:

```text
Database

RPO = 15 minutes
RTO = 2 hours
```

This means the organization targets a recovery point no more than approximately 15 minutes behind and restoration within approximately two hours, subject to the organization's actual definitions and capabilities.

---

# Incident Playbooks

Playbooks turn general response procedures into actionable workflows.

Example:

## Phishing Playbook

```text
Phishing Report
      │
      ▼
Validate Email
      │
      ▼
Extract Indicators
      │
      ├── Sender
      ├── URLs
      ├── Attachments
      └── Domains
      │
      ▼
Search Environment
      │
      ▼
Identify Victims
      │
      ▼
Contain
      │
      ▼
Credential Reset
      │
      ▼
Endpoint Investigation
      │
      ▼
Close / Escalate
```

---

# Recommended Playbooks

Organizations should consider maintaining playbooks for:

```text
Phishing
Credential Compromise
Business Email Compromise
Malware
Ransomware
Account Takeover
Password Spraying
Brute Force
Insider Threat
Data Exfiltration
Web Shell
Cloud Compromise
API Abuse
DDoS
Lost Device
Privileged Account Compromise
```

---

# Communication Playbooks

Technical playbooks are not enough.

Organizations should also prepare communication procedures.

For example:

```text
Technical Incident
      │
      ▼
Incident Commander
      │
      ├── Security Team
      ├── IT
      ├── Legal
      ├── Privacy
      ├── Communications
      └── Executive Leadership
```

The communication procedure should define:

- Who is informed
- When they are informed
- What information is shared
- Who approves external communications
- How updates are documented

---

# Legal and Regulatory Readiness

Some incidents may trigger:

- Regulatory obligations
- Contractual obligations
- Customer notification
- Privacy requirements
- Law enforcement considerations
- Insurance requirements

Incident responders should not independently determine legal obligations unless that is explicitly part of their role.

Instead:

```text
Technical Finding
       │
       ▼
Incident Commander
       │
       ▼
Legal / Privacy
       │
       ▼
Regulatory Assessment
```

Jurisdiction and contractual requirements vary, so organizations should establish the appropriate process with legal and compliance teams in advance.

---

# Cyber Insurance Readiness

Organizations with cyber insurance should understand:

- Notification requirements
- Approved vendors
- Forensic providers
- Legal providers
- Notification providers
- Coverage limitations
- Evidence requirements

Do not wait until a major incident to discover that a policy requires a specific notification procedure.

---

# Third-Party Incident Response

Organizations often depend on external providers.

Examples:

- Cloud providers
- SaaS platforms
- Managed security providers
- Payment processors
- Managed service providers
- Contractors

Preparation should identify:

```text
Third Party
    │
    ├── Security Contact
    ├── Incident Contact
    ├── Escalation Process
    ├── SLA
    └── Evidence / Log Availability
```

---

# Third-Party Risk Questions

Before an incident, determine:

- How quickly will the vendor respond?
- Who is the emergency contact?
- What logs can the vendor provide?
- How long are logs retained?
- What is the notification process?
- What contractual obligations exist?
- Can the organization independently investigate?

---

# Tabletop Exercises

A tabletop exercise is a discussion-based simulation of an incident.

Example:

> "At 08:00 Monday morning, EDR detects ransomware activity on a production file server."

Participants discuss:

- What happens first?
- Who declares the incident?
- Who is contacted?
- Which systems are isolated?
- How are backups validated?
- Who communicates with leadership?
- What evidence is preserved?

The goal is not to test whether someone can type commands.

The goal is to test **decision-making and coordination**.

---

# Tabletop Exercise Structure

```text
Scenario
   │
   ▼
Initial Inject
   │
   ▼
Team Response
   │
   ▼
New Evidence
   │
   ▼
Decision
   │
   ▼
New Inject
   │
   ▼
Escalation
   │
   ▼
Lessons Learned
```

---

# Purple Team Exercises

Purple teaming validates whether security controls actually detect attacker behavior.

```text
Red Team
   │
   │ Attack Simulation
   ▼
Environment
   │
   ▼
Detection
   │
   ▼
SOC / IR
   │
   ▼
Feedback
   │
   ▼
Detection Engineering
   │
   ▼
Improved Control
```

This creates a continuous validation cycle.

---

# Incident Response Readiness Testing

Readiness can be tested through:

### Tabletop Exercises

Test communication and decisions.

### Technical Simulations

Test actual response procedures.

### Purple Team

Test detections against simulated adversary behavior.

### Recovery Exercises

Test backup restoration.

### Forensic Exercises

Test evidence acquisition and analysis.

### Communication Exercises

Test executive and external communications.

---

# Common Preparation Gaps

## 1. Security Tools Without Coverage

An organization may own EDR but have large numbers of unmanaged endpoints.

### Problem

Tool ownership does not equal visibility.

---

## 2. Logs Without Retention

Logs may exist but disappear before an incident is discovered.

### Problem

Historical investigation becomes impossible.

---

## 3. Backups Without Recovery Tests

Backups may be corrupted, inaccessible, or incomplete.

### Problem

Recovery assumptions are unverified.

---

## 4. Plans Without Exercises

A well-written IR plan may fail during a real incident.

### Problem

Roles and communication have never been tested.

---

## 5. Excessive Administrative Access

Responders may be unable to contain an incident because required permissions are unclear.

### Problem

Response actions are delayed.

---

## 6. No Out-of-Band Communication

The organization's primary communication environment may be compromised.

### Problem

Responders cannot coordinate securely.

---

## 7. No Asset Ownership

The team cannot quickly identify who owns the affected system.

### Problem

Containment decisions are delayed.

---

## 8. No Cloud Visibility

Cloud resources may operate without adequate audit logs.

### Problem

Cloud investigation becomes severely limited.

---

# IR Readiness Checklist

## Governance

```text
[ ] IR policy exists
[ ] IR plan exists
[ ] Roles defined
[ ] Severity model defined
[ ] Escalation process defined
[ ] Legal process defined
[ ] Regulatory process defined
```

---

## People

```text
[ ] Incident Commander identified
[ ] SOC contacts defined
[ ] IR contacts defined
[ ] IT contacts defined
[ ] Cloud contacts defined
[ ] Identity contacts defined
[ ] Legal contacts defined
[ ] Executive contacts defined
[ ] External contacts defined
```

---

## Technology

```text
[ ] SIEM deployed
[ ] EDR deployed
[ ] Network monitoring available
[ ] DNS logs available
[ ] Authentication logs available
[ ] Cloud audit logs enabled
[ ] Email security available
[ ] Asset inventory maintained
```

---

## Evidence

```text
[ ] Evidence collection procedure
[ ] Evidence storage
[ ] Hashing process
[ ] Chain of custody
[ ] Log preservation process
[ ] Forensic tooling
[ ] Evidence access controls
```

---

## Recovery

```text
[ ] Critical services identified
[ ] Backups available
[ ] Immutable/offline backups
[ ] Recovery procedures documented
[ ] Restoration tested
[ ] RTO defined
[ ] RPO defined
```

---

## Exercises

```text
[ ] Tabletop exercises
[ ] Purple-team exercises
[ ] Forensic exercises
[ ] Recovery exercises
[ ] Communication exercises
```

---

# Practical Lab

# Lab — Build an Incident Response Readiness Plan

## Objective

Design a basic IR readiness program for a fictional organization.

### Environment

Assume an organization has:

```text
500 Employees
1000 Endpoints
100 Servers
AWS Cloud
Microsoft Identity
Corporate Email
VPN
Customer Web Application
Production Database
```

---

## Task 1 — Identify Critical Assets

Create a table:

| Asset | Owner | Criticality | Telemetry | Backup |
|---|---|---|---|---|
| Identity | IT | Critical | Yes | Yes |
| Production DB | Engineering | Critical | Yes | Yes |
| Web App | Engineering | High | Yes | Yes |
| Employee Laptop | IT | Medium | EDR | N/A |
| Development Server | Engineering | Medium | Partial | Yes |

---

## Task 2 — Identify Telemetry

Determine whether the environment provides:

```text
[ ] Endpoint telemetry
[ ] Authentication telemetry
[ ] DNS
[ ] Firewall
[ ] VPN
[ ] Cloud audit logs
[ ] Email logs
[ ] Application logs
[ ] Database logs
```

---

## Task 3 — Create an Escalation Model

Example:

```text
SEV-1
   │
   ├── Incident Commander
   ├── SOC
   ├── IR
   ├── IT
   ├── Cloud
   ├── Legal
   └── Executive Leadership
```

---

## Task 4 — Create a Ransomware Playbook

Define:

1. Detection
2. Triage
3. Severity
4. Evidence preservation
5. Containment
6. Credential protection
7. Backup validation
8. Eradication
9. Recovery
10. Lessons learned

---

## Task 5 — Identify Readiness Gaps

Document:

```text
Gap
Risk
Priority
Owner
Remediation
Due Date
```

Example:

| Gap | Risk | Priority | Remediation |
|---|---|---|---|
| No EDR on servers | High | P1 | Deploy EDR |
| No immutable backup | Critical | P1 | Implement immutable storage |
| No tabletop exercise | Medium | P2 | Schedule exercise |

---

# Advanced Lab

## Scenario

A company discovers suspicious authentication activity against a privileged cloud account.

Available telemetry:

```text
Identity Logs
Cloud Audit Logs
EDR
VPN
SIEM
DNS
```

The account shows:

```text
Successful login
Unknown device
New geographic location
MFA challenge
Privilege modification
Cloud API activity
```

### Your task

Develop a readiness-based response plan answering:

```text
1. Who should be notified?

2. What severity should be assigned?

3. What logs should be preserved?

4. What identity controls should be activated?

5. What cloud resources should be investigated?

6. What containment action is appropriate?

7. How should evidence be preserved?

8. What communications are required?

9. How would recovery be validated?

10. What readiness gaps did the incident expose?
```

---

# Interview Questions

## 1. What is incident response preparation?

It is the process of establishing the people, processes, technologies, evidence capabilities, communication mechanisms, and recovery procedures required to respond effectively to cybersecurity incidents.

---

## 2. Why is preparation important?

Preparation reduces response time, prevents confusion, improves evidence preservation, and allows organizations to make informed decisions during high-pressure incidents.

---

## 3. What should an incident response plan contain?

At minimum:

- Scope
- Roles
- Responsibilities
- Incident lifecycle
- Severity
- Escalation
- Communication
- Evidence handling
- Containment
- Recovery
- Documentation
- Lessons learned

---

## 4. What is an asset inventory and why is it important?

An asset inventory identifies systems, applications, identities, and infrastructure owned or managed by an organization.

It is essential because responders must know what they are protecting and who owns affected systems.

---

## 5. Why are critical assets important?

Critical assets require prioritized protection and response because their compromise may create significant business, security, or regulatory impact.

---

## 6. What is the difference between RTO and RPO?

**RTO** defines the target time for restoring a service.

**RPO** defines the target amount of recoverable data or acceptable data loss measured in time.

---

## 7. Why are backups not enough?

Backups may be:

- Corrupted
- Incomplete
- Inaccessible
- Encrypted by ransomware
- Missing recent data

Therefore restoration must be tested.

---

## 8. What is a tabletop exercise?

A tabletop exercise is a discussion-based simulation where participants walk through an incident scenario and make decisions without necessarily performing the technical actions themselves.

---

## 9. What is a purple-team exercise?

A purple-team exercise combines adversary simulation with defensive validation to determine whether security controls detect and respond to simulated attacker behavior.

---

## 10. What logs should an organization collect for incident response?

Depending on the environment:

- Authentication
- Endpoint
- Network
- DNS
- Firewall
- VPN
- Cloud
- Email
- Application
- Database
- Identity

---

## 11. Why is time synchronization important?

Accurate timestamps allow investigators to correlate activity across multiple systems and reconstruct reliable incident timelines.

---

## 12. Why should organizations maintain out-of-band communication?

During some incidents, internal email, identity systems, collaboration tools, or other communication infrastructure may itself be compromised or unavailable.

---

## 13. What is chain of custody?

Chain of custody documents who collected, handled, transferred, stored, and analyzed evidence to preserve its integrity and accountability.

---

## 14. What is the purpose of an incident response playbook?

A playbook provides repeatable, actionable procedures for handling a specific incident type.

---

## 15. What is the most important aspect of IR readiness?

There is no single control.

Effective readiness comes from the combination of:

```text
People
+
Process
+
Visibility
+
Technology
+
Evidence
+
Recovery
+
Practice
```

---

# Enterprise IR Readiness Architecture

A mature environment may look like:

```text
                         ENTERPRISE
                             │
       ┌─────────────────────┼─────────────────────┐
       │                     │                     │
       ▼                     ▼                     ▼
    Endpoints              Network              Cloud
       │                     │                     │
       ▼                     ▼                     ▼
      EDR                   NDR              Cloud Security
       │                     │                     │
       └─────────────────────┼─────────────────────┘
                             │
                             ▼
                            SIEM
                             │
                 ┌───────────┼───────────┐
                 │           │           │
                 ▼           ▼           ▼
                SOC       Detection    Threat
                           Engineering  Hunting
                 │           │           │
                 └───────────┼───────────┘
                             │
                             ▼
                     Incident Response
                             │
             ┌───────────────┼────────────────┐
             │               │                │
             ▼               ▼                ▼
         Forensics        Containment       Recovery
             │               │                │
             └───────────────┼────────────────┘
                             ▼
                     Lessons Learned
                             │
                             ▼
                     Security Improvement
```

---

# Readiness Metrics

Organizations can measure IR preparedness using metrics such as:

### Coverage

```text
EDR Coverage
=
Protected Endpoints / Total Endpoints
```

### Logging Coverage

```text
Logging Coverage
=
Assets With Required Logs / Critical Assets
```

### Playbook Coverage

```text
Playbook Coverage
=
Incident Types With Tested Playbooks
/
Priority Incident Types
```

### Exercise Completion

```text
Exercise Completion
=
Completed Exercises / Planned Exercises
```

Other useful measures include:

- Percentage of critical assets with EDR
- Percentage of critical systems with centralized logging
- Percentage of cloud accounts with audit logging
- Backup restoration success rate
- Mean time to identify readiness gaps
- Number of unresolved IR gaps
- Time required to activate response teams

Metrics should measure meaningful capability rather than simply the number of documents produced.

---

# Readiness Maturity Model

## Level 1 — Ad Hoc

```text
No formal plan
Limited logging
Unclear responsibilities
```

## Level 2 — Repeatable

```text
Basic IR plan
Basic logging
Defined escalation
```

## Level 3 — Defined

```text
Formal IR program
Playbooks
Exercises
Evidence procedures
```

## Level 4 — Measured

```text
Coverage metrics
Response metrics
Recovery testing
Detection validation
```

## Level 5 — Optimized

```text
Continuous validation
Automation
Threat-informed readiness
Advanced exercises
Continuous improvement
```

---

# Key Takeaways

Incident response preparation is the foundation of effective response.

The most important capabilities are:

```text
Know Your Environment
        ↓
Know Your People
        ↓
Know Your Data
        ↓
Know Your Telemetry
        ↓
Know Your Procedures
        ↓
Know Your Recovery Process
        ↓
Practice
        ↓
Measure
        ↓
Improve
```

A mature organization should not wait for a breach to discover that:

- Critical systems are undocumented
- Logs are missing
- EDR is not deployed
- Backups cannot be restored
- Contact information is outdated
- No one knows who is responsible
- Evidence cannot be preserved
- Cloud activity cannot be investigated

> **Incident response readiness is built during normal operations so that the organization can perform under abnormal conditions.**

---

# References

### NIST

**Computer Security Incident Handling Guide — SP 800-61**

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

**NIST Cybersecurity Framework**

https://www.nist.gov/cyberframework

### CISA

Cybersecurity and incident response resources:

https://www.cisa.gov/

### MITRE ATT&CK

Threat-informed defense and adversary behavior:

https://attack.mitre.org/

### CIS

CIS Critical Security Controls:

https://www.cisecurity.org/controls

### FIRST

Incident response and security team resources:

https://www.first.org/

### SANS

Incident response resources:

https://www.sans.org/

---

# Chapter Summary

Effective incident response is not created when an incident begins.

It is created through continuous preparation:

```text
Governance
   +
People
   +
Asset Visibility
   +
Telemetry
   +
Evidence
   +
Playbooks
   +
Backups
   +
Communication
   +
Exercises
   +
Measurement
        │
        ▼
IR READINESS
```

The ultimate objective is simple:

> **When an incident occurs, the organization should already know what to do, who should do it, what evidence to collect, how to contain the threat, how to recover, and how to improve afterward.**
