# Incident Response Playbooks and Case Studies

> **An enterprise collection of incident response playbooks, decision workflows, investigation checklists, and realistic case studies for SOC analysts, incident responders, threat hunters, and security engineers.**

---

# Overview

Incident response becomes significantly more effective when responders have **repeatable playbooks** for common incident categories.

A playbook converts:

```text
Detection
   │
   ▼
Investigation
   │
   ▼
Decision
   │
   ▼
Action
   │
   ▼
Validation
```

into a documented and reproducible workflow.

A playbook should not replace professional judgment.

Instead, it should provide:

- Consistency
- Speed
- Escalation criteria
- Required evidence
- Containment options
- Investigation steps
- Recovery requirements
- Documentation requirements

---

# Why Playbooks Matter

Without playbooks, responders may:

- Forget critical steps
- Perform inconsistent containment
- Miss evidence
- Delay escalation
- Repeat mistakes
- Produce incomplete documentation

A mature SOC uses playbooks as operational guidance.

---

# Playbook Architecture

```text
Alert
  │
  ▼
Validate
  │
  ▼
Classify
  │
  ▼
Scope
  │
  ▼
Contain
  │
  ▼
Investigate
  │
  ▼
Eradicate
  │
  ▼
Recover
  │
  ▼
Validate
  │
  ▼
Close
```

---

# Playbook Structure

Each playbook should ideally define:

```text
Trigger
Severity
Objective
Required Evidence
Initial Triage
Investigation
Containment
Eradication
Recovery
Escalation
Validation
Documentation
Metrics
```

---

# Severity and Escalation

A playbook should define escalation thresholds.

Example:

```text
P1 — Critical
Active ransomware
Domain compromise
Major data breach

P2 — High
Confirmed malware
Privileged account compromise
Confirmed C2

P3 — Medium
Suspicious endpoint
Potential phishing
Unauthorized application

P4 — Low
Low-confidence alert
Policy violation
Informational event
```

Organizations should customize severity definitions to their risk model.

---

# Playbook 01 — Phishing

## Trigger

Potential phishing email detected.

Indicators:

- Malicious attachment
- Credential-harvesting URL
- Suspicious sender
- Impersonation
- Malicious redirect

---

## Objective

Determine:

- Whether the email is malicious
- Who received it
- Who interacted with it
- Whether credentials were submitted
- Whether malware executed

---

## Workflow

```text
Phishing Alert
      │
      ▼
Analyze Email
      │
      ▼
Identify Recipients
      │
      ▼
Check User Interaction
      │
      ▼
Investigate Endpoint
      │
      ▼
Investigate Identity
      │
      ▼
Contain
      │
      ▼
Search Enterprise
```

---

## Evidence

Collect:

- Email headers
- Message ID
- Sender
- Recipient
- URLs
- Attachments
- Authentication results
- Endpoint telemetry
- Identity events

---

## Containment

Potential actions:

- Quarantine email
- Remove copies
- Block malicious URL/domain
- Isolate infected endpoint
- Revoke sessions
- Reset credentials if required

---

## Validation

Confirm:

```text
[ ] Malicious messages removed
[ ] No additional recipients missed
[ ] No malware execution
[ ] No credential compromise
[ ] No continued sessions
```

---

# Playbook 02 — Malware Detection

## Trigger

EDR detects suspicious malware.

---

## Workflow

```text
EDR Alert
   │
   ▼
Validate
   │
   ▼
Identify Process
   │
   ▼
Identify User
   │
   ▼
Identify Network
   │
   ▼
Contain Host
   │
   ▼
Search IOC
   │
   ▼
Investigate Persistence
   │
   ▼
Eradicate
   │
   ▼
Recover
```

---

## Evidence

- File hash
- Process tree
- Command line
- Parent process
- Network connections
- DNS
- Persistence
- User
- EDR telemetry

---

## Containment

Possible actions:

```text
Host Isolation
Credential Protection
C2 Blocking
```

---

## Validation

Search for:

- Same hash
- Same domain
- Same IP
- Same process behavior
- Same persistence mechanism

---

# Playbook 03 — Compromised Account

## Trigger

Identity system detects suspicious account activity.

---

## Workflow

```text
Identity Alert
     │
     ▼
Validate Authentication
     │
     ▼
Review Device
     │
     ▼
Review Location
     │
     ▼
Review Sessions
     │
     ▼
Review Privileges
     │
     ▼
Contain Identity
     │
     ▼
Scope
```

---

## Containment

Potential actions:

- Revoke sessions
- Disable account
- Reset password
- Rotate keys
- Revoke tokens
- Review MFA
- Remove unauthorized privileges

---

# Playbook 04 — Privileged Account Compromise

## Trigger

Suspicious activity involving privileged identity.

---

## Priority

```text
CRITICAL
```

---

## Workflow

```text
Privileged Account Alert
        │
        ▼
Immediate Validation
        │
        ▼
Protect Identity
        │
        ▼
Revoke Sessions
        │
        ▼
Rotate Credentials
        │
        ▼
Review Privilege Changes
        │
        ▼
Scope Accessed Systems
```

---

## Investigate

Determine:

- Authentication sources
- Commands
- Administrative actions
- Group changes
- Cloud roles
- New accounts
- Persistence

---

# Playbook 05 — Ransomware

## Trigger

Evidence of mass encryption or ransomware behavior.

---

## Priority

```text
CRITICAL
```

---

## Immediate Objectives

```text
STOP SPREAD
PROTECT IDENTITY
PROTECT BACKUPS
PRESERVE EVIDENCE
```

---

## Workflow

```text
Ransomware Alert
       │
       ▼
Confirm Activity
       │
       ▼
Identify Affected Hosts
       │
       ▼
Isolate
       │
       ▼
Protect Backups
       │
       ▼
Secure Privileged Accounts
       │
       ▼
Investigate Lateral Movement
       │
       ▼
Assess Data Theft
       │
       ▼
Recovery Planning
```

---

## Important Questions

```text
When did encryption begin?
Which host started first?
Which accounts were used?
Was lateral movement observed?
Were backups accessed?
Was data exfiltrated?
Are domain controllers affected?
```

---

# Playbook 06 — Data Exfiltration

## Trigger

Potential unauthorized data transfer.

---

## Workflow

```text
Exfiltration Alert
      │
      ▼
Identify Source
      │
      ▼
Identify Data
      │
      ▼
Identify Destination
      │
      ▼
Determine Method
      │
      ▼
Contain
      │
      ▼
Assess Scope
```

---

## Investigate

Look for:

- Archive creation
- Compression
- Cloud uploads
- Large transfers
- Unusual destinations
- Database exports
- API downloads

---

# Playbook 07 — Web Application Compromise

## Trigger

Evidence of successful exploitation.

---

## Workflow

```text
WAF / Application Alert
        │
        ▼
Validate Request
        │
        ▼
Application Logs
        │
        ▼
Server Process Tree
        │
        ▼
Network
        │
        ▼
Persistence
        │
        ▼
Database
```

---

## Investigate

Determine:

```text
Was exploitation successful?
Was code execution achieved?
Was a web shell created?
Was persistence established?
Was data accessed?
```

---

# Playbook 08 — Web Shell

## Trigger

Suspicious server-side file or web process spawning shell.

---

## Workflow

```text
Web Shell Alert
     │
     ▼
Preserve Evidence
     │
     ▼
Identify File
     │
     ▼
Identify Request
     │
     ▼
Identify Process
     │
     ▼
Identify C2
     │
     ▼
Scope Server
```

---

## Containment

Potential actions:

- Restrict application
- Isolate server
- Block attacker infrastructure
- Preserve suspicious file
- Restrict administrative access

---

# Playbook 09 — Cloud Account Compromise

## Trigger

Suspicious cloud authentication or API activity.

---

## Workflow

```text
Cloud Alert
   │
   ▼
Identity
   │
   ▼
API Activity
   │
   ▼
IAM Changes
   │
   ▼
Resource Access
   │
   ▼
Persistence
```

---

## Investigate

Look for:

- New access keys
- Role changes
- New users
- New service principals
- Storage access
- Security group modifications
- Compute deployment

---

# Playbook 10 — API Key Exposure

## Trigger

Credential discovered in:

- Source code
- Logs
- Public repository
- CI/CD
- Developer system

---

## Workflow

```text
Exposed Key
    │
    ▼
Determine Owner
    │
    ▼
Determine Permissions
    │
    ▼
Determine Exposure
    │
    ▼
Rotate
    │
    ▼
Investigate Usage
```

---

# Playbook 11 — DDoS

## Trigger

Availability degradation caused by abnormal traffic.

---

## Workflow

```text
Traffic Spike
     │
     ▼
Validate
     │
     ▼
Identify Pattern
     │
     ▼
Rate Limit
     │
     ▼
Upstream Mitigation
     │
     ▼
Validate Service
```

---

## Investigate

Determine:

- Attack type
- Source distribution
- Target
- Duration
- Volume
- Application impact

---

# Playbook 12 — Insider Security Incident

## Trigger

Potential unauthorized activity by an internal user.

---

## Principles

Do not assume malicious intent.

Investigate objectively.

```text
Observed Activity
      │
      ▼
Authorization
      │
      ▼
Business Context
      │
      ▼
Policy
      │
      ▼
Evidence
```

Coordinate with appropriate legal, HR, privacy, and leadership teams.

---

# Playbook 13 — Lost or Stolen Device

## Trigger

Corporate device reported lost or stolen.

---

## Actions

Potentially:

- Identify device
- Check last known activity
- Revoke sessions
- Rotate credentials where appropriate
- Remote lock/wipe according to policy
- Review recent activity
- Determine data exposure

---

# Playbook 14 — Suspicious OAuth Application

## Trigger

Unexpected OAuth application consent.

---

## Workflow

```text
OAuth Alert
    │
    ▼
Identify Application
    │
    ▼
Review Permissions
    │
    ▼
Identify Users
    │
    ▼
Revoke Consent
    │
    ▼
Revoke Tokens
    │
    ▼
Investigate Activity
```

---

# Playbook 15 — Domain Controller Incident

## Trigger

Potential compromise of domain-level infrastructure.

---

## Priority

```text
CRITICAL
```

---

## Investigate

Review:

- Privileged accounts
- Domain controller activity
- Authentication
- Group changes
- GPO changes
- Kerberos activity
- Service accounts
- Replication-related activity

---

## Response

This requires coordinated identity, endpoint, network, and forensic response.

Avoid making broad destructive changes without a coordinated recovery strategy.

---

# Case Study 01 — Phishing to Account Compromise

## Scenario

An employee receives an email containing a credential-harvesting link.

Timeline:

```text
09:01
Email delivered

09:04
User clicks link

09:05
Credentials submitted

09:06
Suspicious login

09:08
New session

09:12
Cloud application accessed
```

---

## Investigation

The SOC correlates:

```text
Email
 │
 ▼
Identity
 │
 ▼
Cloud
```

---

## Containment

Actions:

```text
Revoke Sessions
Reset Credentials
Review MFA
Block Phishing Domain
Search Other Recipients
```

---

## Lessons

The incident demonstrates why email, identity, and cloud telemetry must be correlated.

---

# Case Study 02 — Malware to Lateral Movement

## Scenario

EDR detects suspicious PowerShell.

```text
Word
 │
 ▼
PowerShell
 │
 ▼
Payload
 │
 ▼
C2
```

Later:

```text
Compromised Host
      │
      ▼
Administrative Credential
      │
      ▼
Server Access
```

---

## Investigation

The team discovers:

- Credential theft
- Remote access
- Additional host compromise

---

## Containment

```text
Isolate Source
Secure Identity
Investigate Destination
Block C2
Search IOC
```

---

## Lesson

The first infected host was not the full incident scope.

---

# Case Study 03 — Web Application Compromise

## Scenario

A WAF detects suspicious requests.

Application telemetry shows:

```text
Suspicious Request
      │
      ▼
Unexpected Application Error
      │
      ▼
Server-Side Process
      │
      ▼
Outbound Connection
```

---

## Investigation

The team identifies:

- Exploitation
- Code execution
- Suspicious file
- C2 communication

---

## Response

```text
Preserve Evidence
      │
      ▼
Restrict Application
      │
      ▼
Investigate Host
      │
      ▼
Patch Vulnerability
      │
      ▼
Rebuild / Restore
      │
      ▼
Validate
```

---

# Case Study 04 — Ransomware

## Scenario

EDR reports rapid file modification.

Within minutes:

```text
WS-101
WS-102
WS-103
FILE-01
```

show similar activity.

---

## Investigation

The team finds:

```text
Compromised Account
      │
      ▼
Remote Administration
      │
      ▼
Multiple Hosts
      │
      ▼
Encryption
```

---

## Response

Immediate priorities:

```text
Stop Spread
Protect Backups
Secure Identity
Isolate Hosts
Preserve Evidence
```

Then:

```text
Scope
Eradicate
Recover
Monitor
```

---

# Case Study 05 — Cloud Credential Compromise

## Scenario

A cloud account creates an unfamiliar access key.

Shortly afterward:

```text
Storage Enumeration
      │
      ▼
Large Object Reads
      │
      ▼
External Network Activity
```

---

## Investigation

The team correlates:

- Authentication
- API activity
- IAM
- Storage
- Network

---

## Response

```text
Disable Key
Revoke Sessions
Review Roles
Investigate Data Access
Assess Exfiltration
Monitor
```

---

# Case Study 06 — Insider Data Exposure

## Scenario

An employee accesses a sensitive dataset outside their normal role.

Evidence:

```text
User
 │
 ▼
Database
 │
 ▼
Sensitive Table
 │
 ▼
Large Query
 │
 ▼
Export
```

---

## Investigation

Determine:

- Was access authorized?
- Was there a business purpose?
- Was data exported?
- Was policy violated?
- Was data transmitted externally?

Do not infer malicious intent without evidence.

---

# Playbook Decision Tree

```text
                   Alert
                     │
                     ▼
                 Validate
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
       Benign                 Suspicious
                                │
                                ▼
                              Scope
                                │
              ┌─────────────────┼─────────────────┐
              ▼                 ▼                 ▼
           Malware           Identity          Application
              │                 │                 │
              ▼                 ▼                 ▼
          Contain            Contain           Contain
              │                 │                 │
              └─────────────────┼─────────────────┘
                                ▼
                            Investigate
                                │
                                ▼
                           Eradicate
                                │
                                ▼
                             Recover
                                │
                                ▼
                            Validate
```

---

# Playbook Quality Standards

A good playbook should be:

### Actionable

The responder knows what to do.

### Specific

The workflow defines clear decision points.

### Flexible

It does not assume every environment is identical.

### Measurable

It defines useful metrics.

### Auditable

Actions are documented.

### Tested

The workflow has been exercised.

---

# Playbook Anti-Patterns

## Over-Automation

Automatically isolating every alert can create operational damage.

## Under-Specification

A playbook saying "investigate further" is not useful.

## No Escalation Criteria

Responders may not know when to involve senior teams.

## No Validation

Actions may be assumed successful.

## No Ownership

Nobody knows who performs the next step.

## No Maintenance

Old playbooks become inaccurate.

---

# Playbook Ownership

Every playbook should have:

```text
Owner
Approver
Version
Last Review
Next Review
Dependencies
```

Example:

```text
Playbook:
Ransomware Response

Owner:
Incident Response Team

Version:
2.1

Last Review:
2026-09-01

Next Review:
2026-12-01
```

---

# Playbook Testing

Use:

- Tabletop exercises
- Purple-team exercises
- Simulated alerts
- Recovery drills
- Ransomware exercises
- Phishing simulations

Example:

```text
Scenario
   │
   ▼
Execute Playbook
   │
   ▼
Measure
   │
   ▼
Identify Gaps
   │
   ▼
Improve
```

---

# Playbook Metrics

Useful measurements include:

### Time to Triage

Alert creation → triage completion.

### Time to Contain

Incident identification → effective containment.

### Time to Escalate

Detection → correct escalation.

### Playbook Completion Rate

Percentage of incidents where the expected workflow was followed.

### Playbook Exception Rate

How often responders had to deviate because the playbook was insufficient.

### False Escalation Rate

How often incidents were unnecessarily escalated.

---

# Practical Lab

# Lab — Build a Phishing Playbook

Create a playbook containing:

```text
Trigger
Severity
Triage
Evidence
Containment
Investigation
Recovery
Escalation
Validation
Metrics
```

---

# Practical Lab — Build a Ransomware Playbook

Include:

```text
Initial Detection
Immediate Isolation
Identity Protection
Backup Protection
Scope
Evidence
Eradication
Recovery
Monitoring
Communications
```

---

# Practical Lab — Build a Cloud Account Compromise Playbook

Include:

```text
Authentication Investigation
Session Revocation
Credential Rotation
IAM Review
API Investigation
Data Access
Persistence
Recovery
Monitoring
```

---

# Practical Lab — Build a Web Application Incident Playbook

Include:

```text
WAF Alert
Application Logs
Endpoint Investigation
Process Tree
Database
Network
Containment
Patch
Rebuild
Validation
```

---

# Universal Incident Playbook Template

```text
# Incident Response Playbook

## Trigger

## Severity

## Objective

## Initial Triage

## Required Evidence

## Investigation

## Scope

## Containment

## Eradication

## Recovery

## Escalation

## Communications

## Validation

## Documentation

## Metrics

## References
```

---

# Incident Commander Checklist

```text
[ ] Incident declared
[ ] Severity assigned
[ ] Incident commander assigned
[ ] Technical lead assigned
[ ] Communications established
[ ] Evidence requirements defined
[ ] Containment approved
[ ] Scope tracked
[ ] Business impact tracked
[ ] Recovery criteria defined
[ ] Stakeholders updated
[ ] Closure approved
```

---

# Incident Communications

Communications should distinguish:

### Confirmed

What is known.

### Suspected

What is believed but not yet confirmed.

### Unknown

What remains under investigation.

Example:

```text
Confirmed:
WS-104 executed malware.

Suspected:
Credential theft occurred.

Unknown:
Whether additional hosts were accessed.
```

This prevents speculation from becoming organizational fact.

---

# Executive Incident Update Template

```text
Incident:
________________

Severity:
________________

Current Status:
________________

Business Impact:
________________

Affected Systems:
________________

Known Facts:
________________

Current Containment:
________________

Investigation:
________________

Next Actions:
________________

Risks:
________________

Next Update:
________________
```

---

# Incident Handoff

A good handoff contains:

```text
Incident Summary
Current Scope
Timeline
Known IOCs
Known TTPs
Actions Taken
Evidence Collected
Containment Status
Outstanding Questions
Next Actions
Owner
```

---

# Shift Handoff Example

```text
Incident:
IR-2026-041

Status:
Contained

Affected:
WS-104
USER-102

Known IOC:
malicious-domain.example

Actions:
Host isolated
Account secured

Outstanding:
Search enterprise for domain
Review cloud activity

Owner:
Threat Hunting Team
```

---

# Case Study Analysis Framework

For any incident, ask:

```text
1. What happened?
2. How did access occur?
3. What did the attacker do?
4. What systems were affected?
5. What identities were affected?
6. What data was affected?
7. How was the attack detected?
8. How was it contained?
9. How was it eradicated?
10. How was recovery validated?
11. What detection failed?
12. What control should improve?
```

---

# Lessons Learned

A case study should not end with:

> "Incident resolved."

It should end with:

```text
Finding
   │
   ▼
Root Cause
   │
   ▼
Control Gap
   │
   ▼
Improvement
   │
   ▼
Validation
```

---

# Incident Response Improvement Loop

```text
Incident
   │
   ▼
Investigation
   │
   ▼
Lessons Learned
   │
   ├── Detection Improvement
   ├── Control Improvement
   ├── Process Improvement
   ├── Training Improvement
   └── Architecture Improvement
            │
            ▼
         Validation
            │
            ▼
      Improved Readiness
```

---

# Interview Questions

## 1. What is an incident response playbook?

A documented workflow that provides repeatable guidance for detecting, investigating, containing, eradicating, and recovering from a particular incident type.

---

## 2. Why are playbooks important?

They improve:

- Consistency
- Response speed
- Evidence handling
- Escalation
- Documentation
- Training

---

## 3. Should every response be fully automated?

No.

High-impact containment actions may require human approval because automated actions can cause significant business disruption.

---

## 4. What makes a good playbook?

It should be:

```text
Actionable
Specific
Flexible
Tested
Measurable
Auditable
```

---

## 5. What should a ransomware playbook prioritize?

Generally:

```text
Stop Spread
Protect Identity
Protect Backups
Preserve Evidence
Determine Scope
Recover
```

---

## 6. What should a compromised-account playbook include?

```text
Authentication Review
Session Review
Credential Reset
Token Revocation
Privilege Review
Persistence Review
Scope
Monitoring
```

---

## 7. What should a web application playbook include?

At minimum:

```text
WAF
Application Logs
Endpoint
Network
Database
Identity
Persistence
Containment
Recovery
```

---

## 8. How do you test a playbook?

Use:

- Tabletop exercises
- Simulated incidents
- Purple-team exercises
- Recovery drills
- Ransomware exercises

---

## 9. What is a playbook exception?

A situation where the responder cannot safely or effectively follow the documented workflow and must adapt the response.

Exceptions should be documented and used to improve the playbook.

---

## 10. Why should playbooks have owners?

Someone must be accountable for:

- Accuracy
- Updates
- Testing
- Approvals
- Lessons learned

---

# Integration With SOC

Playbooks connect detection to action:

```text
Detection
   │
   ▼
Triage
   │
   ▼
Playbook
   │
   ▼
Containment
   │
   ▼
Incident Response
```

---

# Integration With Threat Hunting

Hunting can identify gaps in existing playbooks.

Example:

```text
Threat Hunt
   │
   ▼
New Persistence Technique
   │
   ▼
Playbook Updated
   │
   ▼
New Detection
```

---

# Integration With Detection Engineering

Detection engineering should provide the signals that trigger playbooks.

Example:

```text
Detection Rule
     │
     ▼
High-Confidence Alert
     │
     ▼
Playbook
     │
     ▼
Automated / Human Response
```

---

# Enterprise Playbook Architecture

```text
                         Security Telemetry
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
       Endpoint               Network              Identity
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                               SIEM
                                │
                                ▼
                            Detection
                                │
                                ▼
                         Playbook Engine
                                │
          ┌─────────────────────┼─────────────────────┐
          ▼                     ▼                     ▼
       Malware              Identity              Network
       Playbook             Playbook              Playbook
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                ▼
                       Incident Response
                                │
                    ┌───────────┼───────────┐
                    ▼           ▼           ▼
                 Contain     Eradicate    Recover
                                │
                                ▼
                         Lessons Learned
```

---

# Key Takeaways

Playbooks transform incident response from an improvised activity into a repeatable operational capability.

A mature playbook should:

- Define its trigger.
- Establish severity.
- Identify evidence.
- Define investigation steps.
- Define containment options.
- Define escalation criteria.
- Define recovery requirements.
- Define validation.
- Assign ownership.
- Be tested regularly.
- Be updated after incidents.

The most important principle is:

> **A playbook should guide decisions, not replace judgment.**

The strongest organizations continuously improve playbooks using real incidents, exercises, threat intelligence, and lessons learned.

---

# References

### NIST

Computer Security Incident Handling Guide:

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### CISA

Cybersecurity and incident response resources:

https://www.cisa.gov/

### MITRE ATT&CK

https://attack.mitre.org/

### FIRST

Incident Response and Security Team resources:

https://www.first.org/

### SANS

Incident response resources:

https://www.sans.org/

### CIS Controls

https://www.cisecurity.org/controls

---

# Chapter Summary

The goal of incident response playbooks is not simply to provide checklists.

They should create a **repeatable decision system**:

```text
Signal
  ↓
Validation
  ↓
Context
  ↓
Decision
  ↓
Action
  ↓
Verification
  ↓
Learning
```

Case studies then provide the bridge between theoretical security concepts and real operational response.

> **Detect consistently. Investigate systematically. Contain deliberately. Recover safely. Learn continuously.**
