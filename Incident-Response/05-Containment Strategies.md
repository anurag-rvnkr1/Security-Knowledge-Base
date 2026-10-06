# Containment Strategies

> **An enterprise guide to limiting attacker activity, preventing further compromise, protecting critical assets, preserving evidence, and making defensible containment decisions during cybersecurity incidents.**

---

## Overview

Containment is the process of **limiting the spread and impact of a cybersecurity incident while preventing the attacker from continuing harmful activity**.

Containment sits between investigation and eradication, but in a real incident these activities frequently overlap.

A simplified model is:

```text id="z0z1ik"
Detection
   │
   ▼
Triage
   │
   ▼
Analysis
   │
   ▼
Containment
   │
   ▼
Eradication
   │
   ▼
Recovery
```

The objective of containment is not necessarily to immediately remove every trace of the attacker.

Instead, the immediate goal is:

> **Stop the incident from becoming worse.**

---

# Why It Matters

An attacker who has gained access may continue:

- Executing commands
- Stealing credentials
- Moving laterally
- Accessing sensitive data
- Creating persistence
- Exfiltrating information
- Encrypting systems
- Destroying evidence
- Disabling security controls

Without containment:

```text id="0uy6kd"
Compromised Host
      │
      ├── Credential Theft
      │
      ├── Lateral Movement
      │
      ├── Persistence
      │
      ├── Data Collection
      │
      └── Exfiltration
              │
              ▼
         Business Impact
```

Effective containment changes the trajectory:

```text id="iy8i0n"
Compromised Host
      │
      ▼
Detection
      │
      ▼
Containment
      │
      ├── Host Isolated
      ├── Account Secured
      ├── Network Blocked
      └── Session Revoked
              │
              ▼
       Attack Progression
            Interrupted
```

---

# Containment Objectives

Containment should accomplish one or more of the following:

- Stop active attacker execution
- Prevent lateral movement
- Protect critical systems
- Prevent additional credential theft
- Stop data exfiltration
- Restrict malicious infrastructure
- Prevent ransomware propagation
- Protect backups
- Preserve evidence
- Reduce business impact

---

# Containment Is a Decision Problem

Containment is rarely as simple as:

> "Disconnect everything."

A security team must balance:

```text id="gqbr8t"
             SECURITY
                ▲
                │
                │
                │
                │
                └──────────────► BUSINESS CONTINUITY
```

Aggressive containment can:

- Interrupt production
- Destroy volatile evidence
- Break dependencies
- Alert attackers
- Cause unnecessary outages

Insufficient containment can:

- Allow lateral movement
- Increase data loss
- Allow persistence
- Expand the compromise

The best decision depends on the incident.

---

# Containment Principles

## 1. Stop the Threat

Prevent continued attacker activity.

## 2. Protect Critical Assets

Prioritize:

- Identity
- Production
- Databases
- Backups
- Security infrastructure

## 3. Preserve Evidence

Avoid unnecessary destructive actions.

## 4. Limit Business Disruption

Contain precisely where possible.

## 5. Assume Scope May Expand

Containment decisions should consider related systems.

## 6. Document Actions

Every significant containment action should be recorded.

---

# Types of Containment

A practical model divides containment into:

### Short-Term Containment

Immediate actions designed to stop active attacker activity.

Examples:

- Host isolation
- Account disablement
- IP blocking
- Session revocation

### Long-Term Containment

Actions that stabilize the environment while deeper remediation occurs.

Examples:

- Network segmentation
- Temporary firewall restrictions
- Service restrictions
- Credential rotation
- Temporary access controls

---

# Containment Lifecycle

```text id="4w2jif"
Incident Identified
       │
       ▼
Assess Risk
       │
       ▼
Identify Critical Assets
       │
       ▼
Choose Containment Strategy
       │
       ▼
Execute
       │
       ▼
Validate
       │
       ▼
Monitor
       │
       ▼
Adjust
```

Containment should be treated as an iterative process.

---

# Containment Decision Framework

Before taking an action, ask:

```text id="0imjqe"
What is happening?

Is the attacker active?

What is the current scope?

What will this action stop?

What evidence could be lost?

What business systems could be affected?

Can the action be reversed?

Is approval required?

How will we validate containment?
```

---

# Risk-Based Containment

A useful conceptual model:

```text id="9t8qfn"
Containment Priority
        │
        ▼
Threat Severity
        ×
Asset Criticality
        ×
Attacker Activity
        ×
Potential Impact
```

This is a decision framework, not a universal mathematical formula.

---

# Host Isolation

One of the most common containment actions is isolating a compromised endpoint.

```text id="84l8ct"
Before

Internet
   │
   ▼
WS-104
 ├── User
 ├── File Server
 ├── DNS
 └── C2
```

After:

```text id="x3y0ce"
Internet
   │
   X
   │
WS-104
   │
   └── Security / IR Channel
```

EDR platforms often provide host isolation.

The responder should confirm what network access remains available after isolation.

---

# When to Isolate a Host

Host isolation may be appropriate when:

- Active malware is executing
- C2 communication is confirmed
- Credential theft is suspected
- Ransomware is active
- Lateral movement is occurring
- The endpoint is not business-critical

---

# When Immediate Isolation May Require Care

Consider additional analysis before isolating when:

- The system is highly critical
- Volatile evidence is important
- Isolation may cause major business disruption
- The attacker is actively interacting with the host
- A coordinated containment strategy is required

This does not mean:

> "Never isolate."

It means:

> **Understand the consequences before acting.**

---

# Account Containment

Compromised identities can be contained through:

- Account disablement
- Password reset
- Session revocation
- Token revocation
- MFA re-registration
- API key rotation
- Access key deactivation
- Privilege removal

Example:

```text id="sj4ik1"
Compromised Identity
        │
        ▼
Revoke Sessions
        │
        ▼
Reset Credential
        │
        ▼
Re-register MFA
        │
        ▼
Review Privileges
        │
        ▼
Monitor
```

---

# Privileged Account Containment

Privileged identities require special handling.

Examples:

- Domain administrators
- Cloud administrators
- Root accounts
- Database administrators
- Security administrators

Potential actions:

```text id="qv1wgs"
Revoke Sessions
       │
       ▼
Disable Account
       │
       ▼
Rotate Credentials
       │
       ▼
Review Privileged Access
       │
       ▼
Investigate Related Activity
```

---

# Credential Rotation

If credentials may have been exposed, rotate them appropriately.

Potential targets:

- User passwords
- Service account passwords
- API keys
- Cloud access keys
- SSH keys
- Application secrets
- Database credentials
- Certificates

Credential rotation should consider dependencies.

Immediately changing a service account password without understanding where it is used can cause service outages.

---

# Token and Session Revocation

Password resets may not invalidate existing sessions in every environment.

Therefore, responders may need to revoke:

- Active sessions
- Refresh tokens
- OAuth tokens
- API tokens
- Cloud sessions

Conceptually:

```text id="e3wq4q"
Compromised Account
        │
        ├── Password
        ├── Session
        ├── Refresh Token
        └── OAuth Token
                 │
                 ▼
          Revoke / Rotate
```

---

# Network Containment

Network controls can restrict attacker communication.

Potential actions:

- Block IP
- Block domain
- Block URL
- Block port
- Restrict VLAN
- Isolate subnet
- Apply firewall rule
- Disable routing
- Restrict egress

Example:

```text id="4v0i5v"
Compromised Host
      │
      ▼
Firewall
      │
 ┌────┴────┐
 ▼         ▼
Allow     Block
Trusted   C2
Traffic   Traffic
```

---

# Egress Containment

Outbound traffic controls are especially useful for:

- C2
- Data exfiltration
- Malware downloads
- Cloud credential abuse

A possible response:

```text id="mcb5h3"
Endpoint
   │
   ▼
Proxy / Firewall
   │
   ├── Internal → Allowed
   │
   └── Malicious External → Blocked
```

---

# DNS Containment

Potential controls include:

- Blocking malicious domains
- DNS sinkholing
- Threat intelligence-based blocking
- Domain monitoring

Example:

```text id="zft9x4"
Host
 │
 ▼
DNS Query
 │
 ▼
Malicious Domain
 │
 ▼
DNS Control
 │
 X
Blocked
```

DNS blocking can be useful but should not replace endpoint investigation.

---

# Email Containment

For phishing incidents, containment may include:

- Remove malicious messages
- Block sender
- Block URL
- Block attachment hash
- Search all mailboxes
- Revoke sessions
- Reset credentials

Example:

```text id="2i8n7k"
Malicious Email
      │
      ├── User A
      ├── User B
      ├── User C
      └── User D
            │
            ▼
       Mail Search
            │
            ▼
       Remove / Quarantine
```

---

# Cloud Containment

Cloud incidents may require:

- Disabling compromised identity
- Revoking sessions
- Rotating access keys
- Removing unauthorized roles
- Restricting network access
- Disabling malicious workloads
- Blocking suspicious IPs
- Restricting storage access

Example:

```text id="xg8v9g"
Compromised Cloud Identity
          │
          ▼
Session Revocation
          │
          ▼
Credential Rotation
          │
          ▼
Privilege Review
          │
          ▼
API Activity Review
```

---

# Active Directory Containment

Potential actions include:

- Disable compromised account
- Reset password
- Revoke sessions
- Remove unauthorized group membership
- Isolate endpoint
- Protect privileged accounts
- Investigate Kerberos activity

If domain-level compromise is suspected, containment requires careful coordination because identity infrastructure is highly interconnected.

---

# Ransomware Containment

Ransomware requires rapid containment.

Possible priorities:

```text id="d0o1na"
Detect Encryption
      │
      ▼
Identify Affected Hosts
      │
      ▼
Isolate Hosts
      │
      ▼
Protect Backups
      │
      ▼
Secure Privileged Accounts
      │
      ▼
Restrict Lateral Movement
      │
      ▼
Assess Scope
```

Do not assume the first encrypted endpoint is the only affected system.

---

# Lateral Movement Containment

If lateral movement is suspected:

```text id="1oh3kr"
HOST-A
  │
  ├── SMB ──► HOST-B
  │
  ├── RDP ──► HOST-C
  │
  └── WinRM ► HOST-D
```

Potential controls:

- Isolate source
- Restrict remote administration
- Disable compromised credentials
- Block unnecessary protocols
- Segment networks
- Investigate destination hosts

---

# Network Segmentation

Segmentation can limit attacker movement.

Example:

```text id="zslkzu"
              Corporate Network
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
     User          Server        Critical
     VLAN            VLAN          VLAN
       │             │             │
       └─────── Restricted ────────┘
```

During an incident, temporary restrictions may be applied to prevent movement into critical networks.

---

# Application Containment

For compromised applications, options may include:

- Disable vulnerable endpoint
- Remove malicious component
- Restrict public access
- Enable WAF rule
- Disable affected API
- Rotate secrets
- Restrict database access

Example:

```text id="m23r4w"
Internet
   │
   ▼
Web Application
   │
   X
Compromised Endpoint Disabled
   │
   ▼
Forensic Investigation
```

---

# Database Containment

If database compromise is suspected:

- Restrict network access
- Disable compromised accounts
- Rotate database credentials
- Review queries
- Preserve database logs
- Validate integrity
- Protect backups

Avoid destructive actions before evidence requirements are understood.

---

# Container Containment

For container incidents:

```text id="pkwc6j"
Container
   │
   ▼
Suspicious Activity
   │
   ▼
Identify Image / Workload
   │
   ▼
Restrict Network
   │
   ▼
Preserve Evidence
   │
   ▼
Stop / Replace Workload
```

Investigate:

- Image
- Container
- Pod
- Node
- Service account
- Secrets
- Network connections

---

# Kubernetes Containment

Potential actions may include:

- Isolate affected pod
- Restrict network policy
- Disable compromised service account
- Rotate secrets
- Restrict cluster access
- Investigate node compromise

Example:

```text id="9ysc3g"
Cluster
  │
  ├── Node-01
  │     └── Pod-A
  │
  ├── Node-02
  │     └── Pod-B  ← Suspicious
  │
  └── Node-03
```

If node compromise is suspected, pod-level containment may be insufficient.

---

# Containment and Evidence Preservation

Containment can alter evidence.

For example:

```text id="w3h8px"
Live System
   │
   ├── Memory
   ├── Network Connections
   ├── Processes
   └── Sessions
```

If a system is powered off:

```text id="7c9v2j"
Memory
   X
Lost
```

Therefore, evidence requirements should be considered before destructive actions when circumstances allow.

---

# Volatile Evidence

Potential volatile evidence includes:

- Memory
- Active processes
- Network connections
- Logged-in users
- Temporary files
- Active sessions
- Runtime state

The more volatile the evidence, the faster it may disappear.

---

# Containment vs Evidence Collection

These goals can conflict.

Example:

```text id="1a7b4m"
Active Malware
     │
     ├──────────────► Immediate Isolation
     │
     └──────────────► Evidence Collection
```

The correct balance depends on:

- Threat severity
- Business impact
- Evidence value
- Attacker activity
- Available tooling

There is no universal rule that applies to every incident.

---

# Containment Validation

After containment, verify that it actually worked.

Ask:

```text id="c4l08m"
Is the host still communicating?

Is the account still active?

Are attacker sessions still present?

Is C2 still occurring?

Are new processes appearing?

Is lateral movement continuing?

Are new alerts being generated?
```

Containment should never be assumed successful without validation.

---

# Containment Monitoring

After an action:

```text id="3q5vst"
Contain
   │
   ▼
Monitor
   │
   ├── No Activity
   │
   └── Activity Continues
           │
           ▼
      Adjust Strategy
```

If attacker activity continues, the containment strategy may need to expand.

---

# Containment Scope

Containment can occur at different levels.

### Endpoint

Isolate one machine.

### Identity

Disable or restrict one account.

### Network

Block a destination or isolate a segment.

### Application

Disable one service.

### Organization

Activate broad emergency controls.

The scope should be proportional to the threat.

---

# Precision Containment

Whenever possible, prefer targeted controls.

Example:

### Broad

```text
Block all outbound traffic
```

Potentially disruptive.

### Precise

```text
Block confirmed malicious destination
```

Potentially less disruptive.

Precision depends on confidence and available controls.

---

# Broad Containment

Broad containment may be appropriate when:

- Ransomware is spreading rapidly
- Domain compromise is suspected
- Active exfiltration is occurring
- Critical systems are at immediate risk
- The attacker has widespread access

Example:

```text id="j4v4dq"
Known Compromise
      │
      ▼
Rapid Segmentation
      │
      ▼
Stop Spread
      │
      ▼
Detailed Investigation
```

---

# Containment Decision Matrix

| Situation | Possible Action | Priority |
|---|---|---|
| Active malware | Host isolation | High |
| Compromised user | Session revocation | High |
| Privileged account compromise | Disable/secure identity | Critical |
| Known C2 | Network blocking | High |
| Ransomware spread | Network isolation | Critical |
| Suspicious cloud key | Disable/rotate key | High |
| Phishing campaign | Mail purge | High |
| Web attack | WAF restriction | High |

Actual actions should follow organizational procedures.

---

# Common Containment Mistakes

## 1. Isolating Only the First Host

The attacker may already have moved elsewhere.

## 2. Resetting One Password

The attacker may have compromised additional credentials.

## 3. Blocking Only One IP

Attackers may rotate infrastructure.

## 4. Killing a Process Without Investigating

This may destroy useful evidence.

## 5. Rebooting Immediately

This may destroy volatile evidence.

## 6. Deleting Malware

The sample may be important for analysis.

## 7. Destroying Logs

Never overwrite or delete relevant evidence.

## 8. Disabling Critical Systems Without Coordination

Containment can create major business impact.

## 9. Failing to Validate

A containment action may not work as expected.

## 10. Treating Containment as Eradication

Stopping activity does not necessarily remove the attacker.

---

# Containment Misconfigurations

### No EDR Isolation Capability

Responders cannot rapidly isolate endpoints.

### Excessive Firewall Privileges

Too many administrators can create uncontrolled changes.

### No Network Segmentation

Compromised endpoints can reach critical systems.

### Shared Administrative Accounts

Containment becomes difficult to attribute.

### No Session Revocation

Compromised credentials may remain active.

### Long-Lived Cloud Keys

Stolen keys may remain usable for long periods.

### No Emergency Change Process

Critical containment changes may be delayed.

---

# Emergency Change Management

During a critical incident, organizations may need emergency changes.

A good process still records:

```text id="g51wzi"
Who requested?
What changed?
Why?
When?
Who approved?
What systems affected?
How was it validated?
How will it be reversed?
```

Incident response should not become an excuse for undocumented infrastructure changes.

---

# Containment Documentation

Every major action should be documented.

Example:

```text id="y4jv3h"
Action:
Isolated WS-104

Time:
10:52 UTC

Reason:
Active malware execution

Performed By:
IR Analyst

Expected Result:
Stop network communication

Evidence Impact:
Memory preserved before isolation

Validation:
No outbound connection observed after isolation

Next Step:
Forensic acquisition
```

---

# Containment Checklist

## Before Action

```text id="1u8f2p"
[ ] Incident validated
[ ] Scope understood
[ ] Business criticality checked
[ ] Evidence requirements reviewed
[ ] Authorization confirmed
[ ] Expected result defined
```

## During Action

```text id="v6l5se"
[ ] Action executed
[ ] Timestamp recorded
[ ] Operator recorded
[ ] Evidence preserved
[ ] Dependencies considered
```

## After Action

```text id="8t6jj2"
[ ] Action validated
[ ] Attacker activity checked
[ ] Related systems monitored
[ ] Incident record updated
[ ] Next response step assigned
```

---

# Practical Commands

These commands are intended for authorized defensive response.

---

## Windows

### Identify Active Connections

```powershell id="6m0k8s"
Get-NetTCPConnection
```

### Identify Processes

```powershell id="y2x6p9"
Get-Process
```

### Stop a Process

Use only when authorized and appropriate:

```powershell id="6s0f1j"
Stop-Process -Id <PID>
```

### Disable a User

Administrative example:

```powershell id="z8clm2"
Disable-ADAccount -Identity "<username>"
```

Use organizational procedures before modifying identity systems.

---

## Linux

### Identify Connections

```bash id="u0l3br"
ss -tunap
```

### Identify Processes

```bash id="n7z5m2"
ps aux
```

### Terminate a Process

```bash id="d9e7p0"
kill <PID>
```

Escalate carefully for critical systems.

---

# Firewall Example

A Linux environment may use a host firewall such as `ufw`.

Example defensive restriction:

```bash id="f3h1f9"
sudo ufw deny from <source-ip>
```

This should only be performed according to authorized incident response procedures.

---

# Practical Lab

# Lab — Containing a Compromised Endpoint

## Scenario

The SOC detects:

```text id="g9v8j5"
Host:
WS-104

User:
analyst01

Detection:
Suspicious PowerShell

Network:
Connection to known malicious infrastructure

Process:
powershell.exe

Severity:
High
```

The host is currently online.

---

# Step 1 — Assess

Determine:

```text id="v9x0d1"
Is malware still executing?

Is C2 active?

Is the user privileged?

Is the host business-critical?

Is lateral movement occurring?

Is evidence volatile?
```

---

# Step 2 — Preserve

Before destructive action where circumstances allow, consider collecting:

```text id="xk9f5v"
Process information
Network connections
Logged-in users
EDR telemetry
Relevant logs
File hashes
Memory, if appropriate
```

---

# Step 3 — Contain

Potential actions:

```text id="c5t1s4"
Isolate endpoint
Revoke user sessions
Reset credentials if compromise is suspected
Block confirmed malicious infrastructure
```

---

# Step 4 — Validate

Check:

```text id="n2w9e7"
Is C2 stopped?

Is the endpoint isolated?

Are other hosts communicating with the same IOC?

Are attacker sessions still active?
```

---

# Step 5 — Expand

Search the environment for:

```text id="1g0jz7"
Host
User
IP
Domain
Hash
Process
Authentication
```

---

# Expected Output

```text id="1ypjtb"
Containment Action:
WS-104 isolated

Identity:
analyst01 sessions revoked

Network:
Malicious destination blocked

Evidence:
EDR telemetry preserved
Relevant logs retained

Validation:
No further C2 observed

Next:
Forensic analysis
Scope expansion
Eradication
```

---

# Advanced Lab

# Lab — Ransomware Containment

## Scenario

EDR detects rapid file modifications across multiple systems.

```text id="n1i5cw"
FILE-01
FILE-02
WS-101
WS-104
WS-110
```

Users report inaccessible files.

---

## Task 1 — Determine Immediate Priorities

Prioritize:

```text id="qhzpml"
1. Stop spread
2. Protect backups
3. Protect identity infrastructure
4. Preserve evidence
5. Identify affected systems
6. Prevent additional access
```

---

## Task 2 — Containment Plan

Design:

```text id="7p0p8g"
Endpoint Isolation
        │
        ▼
Network Segmentation
        │
        ▼
Privileged Account Protection
        │
        ▼
Backup Protection
        │
        ▼
Scope Expansion
```

---

## Task 3 — Validate

Determine:

```text id="y9q6tw"
Are new systems still encrypting?

Are attacker sessions active?

Are backups accessible?

Is lateral movement continuing?

Are critical systems affected?
```

---

## Task 4 — Document

Create:

```text id="d08w9j"
Action
Time
Owner
Reason
Expected Result
Actual Result
Evidence Impact
Next Step
```

---

# Advanced Cloud Lab

## Scenario

A cloud administrator account shows:

```text id="o7q5k1"
Unusual login
     ↓
MFA event
     ↓
New access key
     ↓
Privilege change
     ↓
Storage API activity
```

### Containment Tasks

Determine whether to:

```text id="4c9m0x"
Revoke sessions
Disable account
Deactivate access key
Rotate credentials
Remove unauthorized privilege
Restrict storage access
Block suspicious source
```

Then validate:

```text id="zj8p3k"
No active attacker sessions
No unauthorized API activity
No new credentials
No continued data access
```

---

# Interview Questions

## 1. What is containment?

Containment is the process of limiting attacker activity and preventing additional compromise or damage during an incident.

---

## 2. What is the difference between short-term and long-term containment?

Short-term containment immediately stops active malicious activity.

Long-term containment stabilizes the environment while deeper eradication and recovery activities occur.

---

## 3. Should you always isolate a compromised system immediately?

Not necessarily.

The responder should consider:

- Threat severity
- Business impact
- Evidence preservation
- System criticality
- Current attacker activity

---

## 4. Why can shutting down a system be problematic?

It may destroy volatile evidence such as:

- Memory
- Active processes
- Network connections
- Runtime state

---

## 5. What is precision containment?

Precision containment applies the narrowest effective control to stop the threat while minimizing business disruption.

---

## 6. When would broad containment be justified?

Examples include:

- Rapid ransomware propagation
- Active widespread lateral movement
- Domain-level compromise
- Critical data exfiltration
- Severe ongoing attacker activity

---

## 7. How can you contain a compromised account?

Potential actions include:

- Disable account
- Reset credentials
- Revoke sessions
- Revoke tokens
- Rotate API keys
- Review privileges

---

## 8. Why is credential rotation important?

If credentials are compromised, the attacker may continue using them even after the original endpoint is contained.

---

## 9. Why should cloud sessions and tokens be considered?

Password resets may not invalidate all existing sessions or tokens.

---

## 10. How do you validate containment?

Check whether:

- Malicious processes continue
- C2 continues
- Attacker sessions remain active
- New systems are being accessed
- Lateral movement continues
- Suspicious API calls continue

---

## 11. What is the difference between containment and eradication?

Containment limits the attacker.

Eradication removes the attacker's presence and underlying persistence mechanisms.

---

## 12. Why should containment actions be documented?

Documentation provides:

- Accountability
- Reproducibility
- Auditability
- Incident timeline evidence
- Operational coordination

---

## 13. How would you contain ransomware?

Priorities generally include:

```text id="t7g3j0"
Stop Spread
Protect Backups
Secure Privileged Accounts
Isolate Affected Systems
Preserve Evidence
Determine Scope
```

Exact actions depend on the environment.

---

## 14. How would you contain a cloud account compromise?

Potential steps:

```text id="j2j2j7"
Revoke Sessions
Disable / Secure Identity
Rotate Keys
Remove Unauthorized Privileges
Review API Activity
Protect Data
Monitor
```

---

## 15. What is the biggest containment mistake?

A common major mistake is treating the first visible compromised asset as the complete scope of the incident.

---

# Containment Decision Worksheet

```text id="qzjyrq"
Incident:
________________________________

Current Scope:
________________________________

Threat Status:
[ ] Active
[ ] Contained
[ ] Unknown

Critical Assets At Risk:
________________________________

Evidence Requirements:
________________________________

Business Impact:
________________________________

Containment Options:
________________________________

Selected Action:
________________________________

Reason:
________________________________

Expected Result:
________________________________

Evidence Impact:
________________________________

Approval:
________________________________

Validation:
________________________________

Next Action:
________________________________
```

---

# Containment Maturity

## Level 1 — Reactive

- Manual isolation
- Unclear authority
- Limited documentation

## Level 2 — Repeatable

- Defined containment procedures
- Basic endpoint isolation
- Account response procedures

## Level 3 — Defined

- Playbooks
- Automated controls
- Network segmentation
- Cloud containment

## Level 4 — Measured

- Containment metrics
- Validation procedures
- Exercise results
- Response time analysis

## Level 5 — Optimized

- Automated risk-based containment
- Identity-aware controls
- SOAR integration
- Continuous validation
- Minimal business disruption

---

# Key Metrics

### Mean Time to Contain

Time from incident identification to effective containment.

### Containment Success Rate

Percentage of containment actions that successfully stopped the targeted activity.

### Lateral Movement After Containment

Measures whether attacker movement continued after the containment action.

### Business Impact

Measures operational disruption caused by containment.

### Recontainment Rate

Measures how often containment must be repeated because the initial action was insufficient.

Metrics should be interpreted in the context of incident severity.

---

# Containment and Automation

Automation can accelerate response.

Example:

```text id="8q7q7r"
High-Confidence EDR Detection
          │
          ▼
Automated Host Isolation
          │
          ▼
SOC Notification
          │
          ▼
Human Investigation
```

Automation should be carefully controlled.

Not every alert should automatically isolate a production system.

---

# SOAR Integration

Security Orchestration, Automation and Response platforms can automate repetitive actions.

Example:

```text id="l5z4br"
SIEM Alert
   │
   ▼
SOAR
   │
   ├── Enrich IOC
   ├── Query EDR
   ├── Query Identity
   ├── Check Threat Intel
   │
   ▼
Decision
   │
   ├── Auto Contain
   │
   └── Human Approval
```

Automation should be based on confidence and business risk.

---

# Key Takeaways

Containment is about **stopping the attack without creating unnecessary additional damage**.

The core workflow is:

```text id="lq7c2y"
Understand
   ↓
Assess Risk
   ↓
Preserve Evidence
   ↓
Choose Containment
   ↓
Execute
   ↓
Validate
   ↓
Monitor
   ↓
Expand or Adjust
```

The most important principles are:

- Contain active threats quickly
- Protect critical assets
- Protect identity infrastructure
- Protect backups
- Preserve evidence
- Prefer precise containment when possible
- Use broad containment when risk justifies it
- Consider business dependencies
- Document every significant action
- Validate containment instead of assuming success
- Remember that containment is not eradication

> **The purpose of containment is not simply to isolate a machine. It is to interrupt the attacker's ability to continue the operation while creating the conditions for safe eradication and recovery.**

---

# References

### NIST

**Computer Security Incident Handling Guide — SP 800-61**

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### CISA

Incident response and ransomware guidance:

https://www.cisa.gov/

### MITRE ATT&CK

Adversary tactics and techniques:

https://attack.mitre.org/

### CIS Controls

https://www.cisecurity.org/controls

### FIRST

https://www.first.org/

### SANS

https://www.sans.org/

---

# Chapter Summary

Effective containment requires responders to balance:

```text id="8n4cpr"
Threat Risk
     +
Evidence
     +
Business Impact
     +
Scope
     +
Speed
```

A mature response team should be capable of containing:

- Endpoints
- Identities
- Network connections
- Cloud accounts
- Applications
- Servers
- Containers
- Critical infrastructure

while maintaining enough evidence and operational context to continue the investigation.

> **Contain the threat. Protect the environment. Preserve the evidence. Validate the result.**
