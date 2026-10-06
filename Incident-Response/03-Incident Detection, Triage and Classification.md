# Incident Detection, Triage and Classification

> **A practical enterprise guide to identifying suspicious activity, validating security alerts, performing initial triage, determining incident severity, classifying incidents, and escalating confirmed threats.**

---

## Overview

Incident detection is the point at which an organization becomes aware that something potentially malicious may be happening.

Detection can originate from:

- SIEM alerts
- EDR/XDR detections
- Network security controls
- Cloud security platforms
- Identity systems
- Email security
- Threat intelligence
- Threat hunting
- Employees
- Security researchers
- External organizations

However:

> **Detection is not the same as confirmation.**

A security alert is a signal that requires investigation.

The purpose of triage is to quickly determine:

```text
Is this real?
     │
     ▼
Is it malicious?
     │
     ▼
Is there evidence of compromise?
     │
     ▼
What is affected?
     │
     ▼
How severe is it?
     │
     ▼
Who needs to respond?
```

A mature detection and triage capability prevents two major problems:

### Underreaction

A real attack is dismissed as a false positive.

### Overreaction

Every suspicious event becomes a major incident.

Effective triage balances **speed, accuracy, context, and risk**.

---

# Why It Matters

Modern enterprises generate enormous amounts of security telemetry.

A single environment may produce:

```text id="q0f9wq"
Authentication Events
        +
Endpoint Events
        +
DNS Events
        +
Firewall Events
        +
Cloud Events
        +
Application Events
        +
Email Events
        +
Identity Events
        │
        ▼
     Millions
     of Events
        │
        ▼
      Alerts
        │
        ▼
       SOC
```

Security teams cannot manually investigate every event in the same depth.

Triage therefore acts as a filtering and prioritization mechanism.

```text id="c2v9r7"
Millions of Events
        │
        ▼
Security Analytics
        │
        ▼
Alerts
        │
        ▼
Triage
        │
 ┌──────┼────────┐
 ▼      ▼        ▼
False  Suspicious Confirmed
Positive Activity Incident
 │      │        │
 ▼      ▼        ▼
Close  Investigate  IR
```

Good triage allows security teams to focus their deepest investigative resources where risk is highest.

---

# Detection Sources

A mature organization uses multiple detection sources.

## SIEM

Examples:

- Splunk
- Microsoft Sentinel
- Elastic Security
- IBM QRadar

Typical detections:

```text
Multiple authentication failures
Impossible travel
Suspicious process execution
Privilege escalation
Known malicious IP
Unusual cloud API activity
```

---

## EDR / XDR

Endpoint detection can identify:

- Suspicious processes
- Malicious files
- Credential theft
- PowerShell activity
- Persistence
- Process injection
- Network connections
- Security control tampering

---

## Network Security

Network detection may originate from:

- IDS
- IPS
- NDR
- Firewall
- Proxy
- DNS monitoring
- NetFlow

---

## Identity Security

Identity systems may detect:

- Impossible travel
- Password spraying
- MFA anomalies
- New device
- Risky login
- Privilege changes
- Suspicious OAuth activity

---

## Cloud Security

Cloud detections may identify:

- Stolen credentials
- Privilege escalation
- Suspicious API calls
- Public storage exposure
- New access keys
- Unusual resource creation

---

## Email Security

Email systems may detect:

- Malicious attachments
- Phishing URLs
- Spoofing
- Business email compromise
- Malicious forwarding rules

---

## Human Reporting

Employees remain an important detection source.

Example:

> "I received a password reset email that I did not request."

This may become the starting point for an account compromise investigation.

---

# Detection Pipeline

A typical enterprise pipeline:

```text id="d9azm3"
Telemetry
   │
   ▼
Collection
   │
   ▼
Normalization
   │
   ▼
Correlation
   │
   ▼
Detection Rule
   │
   ▼
Alert
   │
   ▼
Enrichment
   │
   ▼
Triage
   │
   ▼
Investigation
   │
   ▼
Incident
```

---

# Detection vs Triage vs Investigation

These concepts should not be confused.

## Detection

Identifies potentially suspicious behavior.

Example:

> "User has 30 failed logins within 5 minutes."

## Triage

Determines whether the activity requires deeper investigation.

Example:

> "The failures came from a known corporate application and occurred during a password migration."

## Investigation

Determines what actually happened.

Example:

> "The account was targeted by password spraying from an external IP, followed by a successful authentication."

---

# Alert Lifecycle

A professional alert lifecycle can be modeled as:

```text id="x7r8l3"
Alert Created
      │
      ▼
Enrichment
      │
      ▼
Triage
      │
      ├───────────────┐
      │               │
      ▼               ▼
False Positive     Suspicious
      │               │
      ▼               ▼
   Close          Investigate
                      │
                      ▼
                 Confirmed
                      │
                      ▼
                  Incident
                      │
                      ▼
                IR Workflow
```

---

# Initial Triage

The initial triage should answer the basic questions quickly.

### Who?

- User
- Account
- Process owner
- System owner

### What?

- Activity
- Detection
- IOC
- Behavior

### When?

- First observed
- Last observed
- Current activity

### Where?

- Host
- Network
- Cloud
- Geographic location

### How?

- Authentication
- Process execution
- Email
- Network connection
- API call

### Why?

Determine whether a legitimate business explanation exists.

---

# The 5W1H Model

A useful triage framework:

```text id="mxu4br"
                INCIDENT TRIAGE

                    WHAT?
                      │
                      ▼
WHO? ────────────► EVENT ◄──────────── WHEN?
                      │
                      │
                   WHERE?
                      │
                      ▼
                    HOW?
                      │
                      ▼
                    WHY?
```

This prevents investigators from focusing on only one indicator.

---

# Alert Enrichment

Raw alerts rarely contain enough information.

Example raw alert:

```text id="gsvk3e"
Suspicious Login
User: anurag
IP: 203.0.113.20
```

Enrichment might add:

```text id="n4t3mw"
User:
anurag

Department:
Security

Role:
Engineer

Device:
Unknown

IP:
203.0.113.20

Country:
Unknown / External

ASN:
Example Provider

Previous Seen:
Never

MFA:
Successful

Related Alerts:
3

Cloud Activity:
Yes
```

Enrichment dramatically improves triage speed.

---

# Common Enrichment Sources

A SOC may enrich alerts using:

- Asset inventory
- CMDB
- Identity directory
- Threat intelligence
- GeoIP
- WHOIS
- DNS
- EDR
- Vulnerability management
- Cloud inventory
- User behavior
- Previous incidents

---

# IOC Enrichment

Indicators of compromise may include:

```text
IP Address
Domain
URL
File Hash
Email Address
Filename
Registry Key
Process
Certificate
Cloud Resource
User Agent
```

A responder may ask:

```text
Is this IP malicious?

Has it been seen internally?

Which hosts contacted it?

When?

Which users were involved?

What process created the connection?
```

---

# Context Matters

An IOC is not inherently malicious in every context.

For example:

```text id="r7y3wp"
IP Address
    │
    ├── Threat Intelligence: Suspicious
    │
    ├── Corporate Proxy: Known
    │
    └── Internal Context: Legitimate Vendor
```

The correct response depends on the full context.

This is why:

> **Indicators should be investigated in context rather than treated as absolute proof.**

---

# False Positives

A false positive occurs when a detection identifies activity that initially appears suspicious but is legitimate.

Examples:

- Vulnerability scanner
- Penetration test
- IT automation
- Backup system
- Administrative script
- Software deployment
- Security testing

Example:

```text id="q7w0yn"
PowerShell Alert
      │
      ▼
Investigate Parent Process
      │
      ▼
SCCM / Endpoint Management
      │
      ▼
Authorized Software Deployment
      │
      ▼
False Positive
```

---

# False Negatives

A false negative occurs when malicious activity is not detected.

Examples:

- Attacker uses legitimate tools
- Logging is disabled
- Detection rule is incomplete
- Telemetry is missing
- Attacker behavior falls outside known signatures

False negatives are particularly dangerous because the security team may not know the attack occurred.

---

# Detection Quality

A useful conceptual model:

```text id="wy0i0h"
                Detection Quality
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Fidelity      Coverage      Context
          │            │            │
          ▼            ▼            ▼
      Low Noise     Visibility    Enrichment
```

A good detection should ideally be:

- Relevant
- Actionable
- Explainable
- High enough fidelity
- Supported by available telemetry
- Mapped to a response procedure

---

# Detection Fidelity

High-fidelity alerts have a high probability of representing meaningful suspicious activity.

Example:

```text
Known malicious executable
+
Unsigned binary
+
Rare execution
+
Suspicious parent process
```

This is generally stronger than:

```text
PowerShell executed
```

because PowerShell is commonly used legitimately.

---

# Alert Severity vs Incident Severity

These are not always the same.

Example:

```text id="r7j3ip"
High-Severity Alert
       │
       ▼
Triage
       │
       ▼
Authorized Red Team Activity
       │
       ▼
No Incident
```

Conversely:

```text id="b7n4o6"
Low-Severity Alert
       │
       ▼
Investigation
       │
       ▼
Privileged Account Compromise
       │
       ▼
SEV-1 Incident
```

Therefore:

> **Alert severity should not automatically determine incident severity.**

---

# Triage Prioritization

A practical priority model:

```text id="5u8s8x"
Priority =
Impact × Likelihood × Urgency
```

This is conceptual rather than a universal formula.

Consider:

### Impact

- Critical asset?
- Sensitive data?
- Privileged account?

### Likelihood

- Known malicious IOC?
- Strong behavioral evidence?
- Confirmed compromise?

### Urgency

- Attack ongoing?
- Active lateral movement?
- Active exfiltration?
- Ransomware execution?

---

# High-Priority Indicators

Indicators that may justify immediate escalation include:

```text
Active ransomware
Domain administrator compromise
Confirmed data exfiltration
Active lateral movement
Critical server compromise
Cloud administrator compromise
Security control tampering
Multiple systems infected
Credential dumping
```

---

# Incident Classification

Once an alert is validated, classify the incident.

Common categories:

```text
Phishing
Malware
Credential Compromise
Account Takeover
Ransomware
Data Breach
Data Exfiltration
Insider Threat
Web Attack
Cloud Compromise
Network Intrusion
Privilege Escalation
Lateral Movement
DDoS
Policy Violation
```

Classification should be based on the available evidence.

---

# Incident Classification Tree

```text id="0i0y4x"
                    Suspicious Activity
                           │
                           ▼
                     What occurred?
                           │
       ┌───────────────────┼───────────────────┐
       │                   │                   │
       ▼                   ▼                   ▼
   Identity              Endpoint           Network
       │                   │                   │
       ▼                   ▼                   ▼
 Account Takeover       Malware            Intrusion
 Password Attack        Persistence        C2
 MFA Abuse              Execution           Lateral Movement
       │                   │                   │
       └───────────────────┼───────────────────┘
                           ▼
                      Classification
```

---

# Incident Severity Assessment

Severity should consider:

```text id="d0ctg6"
Business Impact
Data Sensitivity
Asset Criticality
Privilege Level
Scope
Persistence
Availability
Regulatory Impact
Customer Impact
Attacker Activity
```

Example:

### Case A

One non-critical workstation with blocked malware.

Potentially:

```text
SEV-3
```

### Case B

Privileged identity actively compromised.

Potentially:

```text
SEV-1 / SEV-2
```

### Case C

Production database exfiltration confirmed.

Potentially:

```text
SEV-1
```

Actual severity depends on organizational policy.

---

# Triage Decision Matrix

| Question | Low Risk | Medium Risk | High Risk |
|---|---|---|---|
| Asset | User device | Important server | Critical system |
| Identity | Standard user | Elevated user | Privileged account |
| Malware | Blocked | Active | Spreading |
| Data | Public | Internal | Sensitive |
| Persistence | None | Suspected | Confirmed |
| Lateral Movement | None | Suspected | Confirmed |
| Exfiltration | None | Unknown | Confirmed |
| Availability | None | Degraded | Major outage |

---

# Investigation Time Window

The initial investigation should define a time window.

For example:

```text id="x5b2ah"
Alert
 │
 ▼
10:30
 │
 ├── Look backward
 │
 ▼
08:30
 │
 └── Look forward
 │
 ▼
Current Time
```

Investigators should expand the window when evidence suggests earlier or later activity.

---

# Look-Back Investigation

Ask:

> **What happened before the alert?**

Examples:

- Previous authentication
- Initial access
- File download
- Email delivery
- Process execution
- DNS activity

---

# Look-Forward Investigation

Ask:

> **What happened after the alert?**

Examples:

- Additional logins
- Lateral movement
- Persistence
- Data access
- Exfiltration
- Additional hosts

---

# Alert Correlation

One alert may be meaningless alone.

Multiple alerts may reveal an attack chain.

```text id="wh6y7c"
Impossible Login
      │
      ▼
MFA Activity
      │
      ▼
Mailbox Access
      │
      ▼
New Forwarding Rule
      │
      ▼
External Email Sent
      │
      ▼
Account Compromise
```

Correlation transforms isolated events into a coherent investigation.

---

# Alert Grouping

A single incident may generate many alerts.

Example:

```text id="72ag2j"
Compromised Host
      │
      ├── Malware Alert
      ├── PowerShell Alert
      ├── DNS Alert
      ├── EDR Alert
      ├── C2 Alert
      └── Credential Alert
```

These should not necessarily become six independent incidents.

They may represent one underlying compromise.

---

# Incident Declaration

An incident should be declared when evidence and risk justify coordinated response.

A conceptual workflow:

```text id="g2b3lq"
Alert
 │
 ▼
Triage
 │
 ▼
Suspicious?
 │
 ├── No ──► Close
 │
 ▼
Yes
 │
 ▼
Evidence of Compromise?
 │
 ├── No ──► Monitor / Investigate
 │
 ▼
Yes
 │
 ▼
Incident Declaration
```

Organizations should define formal criteria for incident declaration.

---

# Incident Escalation

Escalation should be predictable.

Example:

```text id="v5bqjr"
SOC Analyst
     │
     ▼
Senior Analyst
     │
     ▼
Incident Responder
     │
     ▼
Incident Commander
     │
     ├── Legal
     ├── IT
     ├── Cloud
     ├── Identity
     └── Leadership
```

Escalation may also occur directly for critical events.

---

# When to Escalate Immediately

Examples:

```text
Confirmed ransomware
Active data exfiltration
Domain compromise
Cloud root/admin compromise
Critical infrastructure compromise
Multiple-system malware outbreak
Active attacker lateral movement
Major customer data exposure
Security control destruction
```

Do not wait for every investigative question to be answered before escalating a clearly dangerous incident.

---

# SOC-to-IR Handoff

A good handoff prevents information loss.

The SOC should provide:

```text id="0ft6p6"
Incident ID
Detection Source
Alert Details
Timestamp
Affected User
Affected Host
Indicators
Initial Investigation
Relevant Logs
Initial Timeline
Severity
Actions Already Taken
Known Unknowns
```

---

# Poor Handoff

Example:

> "EDR says malware. Please investigate."

This creates unnecessary delay.

---

# Good Handoff

Example:

```text id="7fd1rc"
Incident: INC-2026-0142

Detection:
EDR malware detection

Host:
WS-104

User:
analyst01

Time:
10:42 UTC

Observed:
WINWORD.EXE spawned PowerShell.

PowerShell created:
C:\Users\analyst01\AppData\...\script.ps1

Network:
Connection to suspicious external domain.

Initial assessment:
Likely malicious execution.

Actions:
Host isolated.

Unknown:
Credential theft and lateral movement not yet determined.

Requested:
Scope user, host, and related network activity.
```

This gives the responder a useful starting point.

---

# Detection Enrichment Workflow

```text id="5zivx5"
Raw Alert
   │
   ▼
Asset Context
   │
   ▼
User Context
   │
   ▼
Threat Intelligence
   │
   ▼
Historical Activity
   │
   ▼
Related Alerts
   │
   ▼
Business Criticality
   │
   ▼
Risk Assessment
```

---

# Common Triage Errors

## 1. Trusting the Alert Description

An alert description is only a starting point.

Investigate the underlying telemetry.

---

## 2. Closing Too Quickly

A single benign explanation does not always explain all related activity.

---

## 3. Treating Every IOC as Malicious

Context matters.

---

## 4. Ignoring Business Context

A suspicious process on a development machine may have a different impact than the same process on a domain controller.

---

## 5. Focusing Only on One Host

Attackers may have compromised multiple systems.

---

## 6. Ignoring Identity

Modern attacks frequently involve compromised credentials.

---

## 7. Failing to Preserve Evidence

Premature cleanup can destroy useful evidence.

---

## 8. Delaying Escalation

Do not wait for complete certainty before escalating high-risk activity.

---

## 9. Not Recording Negative Findings

Documenting what was checked and not found is useful.

Example:

```text
No lateral movement identified
No persistence identified
No evidence of exfiltration identified
```

---

## 10. Not Recording Unknowns

Unknown does not mean false.

Example:

```text
Exfiltration status: Unknown
```

is better than:

```text
No exfiltration
```

when evidence is insufficient.

---

# Common Detection Misconfigurations

## Missing Telemetry

A detection may depend on logs that are not consistently collected.

## Incorrect Parsing

Events may reach the SIEM but fields may be incorrectly parsed.

## Time Synchronization Problems

Events may appear in the wrong order.

## Duplicate Alerts

The same event may trigger multiple alerts.

## Overly Broad Rules

Generate excessive false positives.

## Overly Narrow Rules

Miss variants of malicious behavior.

## Missing Asset Context

The SOC cannot determine whether the system is critical.

## Missing Identity Context

The analyst cannot determine whether the user is privileged.

---

# Detection Engineering Feedback Loop

Triage findings should feed detection engineering.

```text id="p49q3c"
Alert
  │
  ▼
Triage
  │
  ▼
Investigation
  │
  ├── Good Detection
  │
  ├── False Positive
  │
  ├── Detection Gap
  │
  └── Visibility Gap
        │
        ▼
Detection Engineering
        │
        ▼
Improved Detection
```

This prevents repeated investigation of the same problem.

---

# Practical Commands

These examples support authorized defensive triage.

## Windows

### Current User

```powershell id="2o8j44"
whoami
```

### Process List

```powershell id="6w6n3k"
Get-Process
```

### Process Details

```powershell id="u5q3aw"
Get-CimInstance Win32_Process |
Select-Object ProcessId,ParentProcessId,Name,CommandLine
```

### Network Connections

```powershell id="1hsvqv"
Get-NetTCPConnection
```

### DNS Cache

```powershell id="w9y6th"
Get-DnsClientCache
```

### Recent Security Events

```powershell id="5d6p3r"
Get-WinEvent -LogName Security -MaxEvents 100
```

---

# Linux

### Processes

```bash id="m0z9r9"
ps aux
```

### Network Connections

```bash id="e6f3m7"
ss -tulpn
```

### Logged-In Users

```bash id="h4l2xq"
w
```

### Recent Authentication

```bash id="b5u1fe"
last
```

### Authentication Failures

```bash id="9qz2l5"
grep "Failed password" /var/log/auth.log
```

---

# DNS Triage

```bash id="c9d2b3"
dig suspicious-domain.example
```

Check:

- Resolution
- IP
- TTL
- Nameservers
- Historical context

---

# Hash Investigation

On Windows:

```powershell id="0m0p0n"
Get-FileHash suspicious.exe -Algorithm SHA256
```

On Linux:

```bash id="0c5a5s"
sha256sum suspicious
```

A hash can then be compared with authorized threat intelligence sources.

---

# Practical Lab

# Lab — From Alert to Incident

## Objective

Determine whether a suspicious authentication alert represents:

1. False positive
2. Suspicious activity
3. Confirmed account compromise

---

## Scenario

The SIEM generates:

```text id="6j4g6y"
ALERT

Detection:
Multiple Failed Logins

User:
employee01

Source:
198.51.100.25

Failures:
47

Time:
09:12–09:19 UTC

Success:
09:20 UTC
```

---

# Step 1 — Enrich the User

Determine:

```text
Department
Role
Privilege Level
Normal Login Locations
Normal Devices
Recent Password Change
MFA Status
```

---

# Step 2 — Investigate the Source

Determine:

```text
IP reputation
ASN
Geographic context
Previous activity
Other targeted users
```

---

# Step 3 — Investigate Authentication

Search:

```text
Failed logins
Successful login
MFA events
Device information
Session creation
Password changes
```

---

# Step 4 — Investigate Post-Authentication Activity

Search for:

```text
Mailbox access
Cloud API activity
File access
Privilege changes
New sessions
OAuth applications
```

---

# Step 5 — Scope

Determine:

```text
Were other accounts targeted?

Were other IP addresses involved?

Was the same source successful elsewhere?

Did lateral movement occur?
```

---

# Step 6 — Classification

Possible outcomes:

### Outcome A

Known corporate scanner.

```text
False Positive
```

### Outcome B

Repeated failures with no successful login.

```text
Suspicious Activity
```

### Outcome C

Successful authentication followed by suspicious activity.

```text
Confirmed Account Compromise
```

---

# Step 7 — Severity

Consider:

```text
Is employee01 privileged?

Is sensitive data accessible?

Is the session active?

Was MFA bypassed?

Did the attacker perform additional actions?
```

Assign an appropriate severity according to the organization's policy.

---

# Expected Investigation Record

```text id="d7uvn6"
Incident ID:
INC-2026-XXXX

Detection:
Password Attack

Account:
employee01

Source:
198.51.100.25

Initial Time:
09:12 UTC

Successful Authentication:
09:20 UTC

MFA:
Confirmed / Unknown

Post-Login Activity:
Observed / Not Observed

Other Accounts:
None / Identified

Classification:
Account Compromise / Suspicious Activity

Severity:
SEV-X

Containment:
Session Revoked
Credential Reset

Next Actions:
Threat Hunt
Identity Investigation
Detection Review
```

---

# Advanced Lab

## Multi-Stage Detection Correlation

The SIEM generates these alerts:

```text id="8xw7u2"
09:01
Impossible Travel

09:03
MFA Authentication

09:07
New OAuth Application

09:12
Mailbox Rule Created

09:15
External Email Sent

09:19
Cloud File Download
```

### Task

Determine whether these represent:

- Independent events
- A false positive
- Account compromise
- Business Email Compromise
- Cloud account takeover

Build a timeline and identify:

```text
Initial Access
Persistence
Actions
Potential Impact
Containment
Evidence
Unknowns
```

---

# Interview Questions

## 1. What is security alert triage?

Alert triage is the process of validating, enriching, prioritizing, and determining the appropriate response to a security alert.

---

## 2. What is the difference between detection and investigation?

Detection identifies potentially suspicious activity.

Investigation determines what actually happened and establishes scope, impact, and evidence.

---

## 3. What information should you collect during initial triage?

At minimum:

- User
- Host
- Timestamp
- Source
- Destination
- Process
- IOC
- Detection rule
- Business context
- Related activity

---

## 4. What is alert enrichment?

Alert enrichment adds contextual information to a security alert, such as:

- Asset ownership
- User role
- Threat intelligence
- Historical activity
- Geographic information
- Vulnerability information

---

## 5. How do you determine whether an alert is a false positive?

Investigate the underlying activity and compare it with known legitimate behavior, asset context, user activity, authorized administrative operations, and related telemetry.

---

## 6. What is a false negative?

A false negative occurs when malicious activity exists but the security detection system fails to identify it.

---

## 7. Can a high-severity alert be a false positive?

Yes.

Alert severity represents the potential or configured importance of the detection; it does not guarantee that malicious activity occurred.

---

## 8. Can a low-severity alert become a critical incident?

Yes.

Additional investigation may reveal that the activity involves a privileged identity, critical infrastructure, ransomware, or significant data exposure.

---

## 9. When should an alert become an incident?

When evidence and risk indicate that coordinated incident response is required according to the organization's incident declaration criteria.

---

## 10. Why is context important in incident triage?

The same activity can be benign or malicious depending on:

- User
- Host
- Time
- Business process
- Authorization
- Asset criticality
- Related events

---

## 11. What is alert correlation?

Alert correlation combines related security events to identify a larger activity pattern or attack sequence.

---

## 12. What is the purpose of an incident severity model?

It ensures that incidents receive consistent prioritization and appropriate resources.

---

## 13. What is a SOC-to-IR handoff?

It is the transfer of an investigated or suspicious alert from the SOC to incident response with relevant evidence, context, timeline, actions, and known unknowns.

---

## 14. What should you do if you are unsure whether an incident is real?

Preserve relevant evidence, continue investigation, document uncertainty, and escalate when the potential risk justifies it.

Avoid both premature closure and unsupported conclusions.

---

## 15. Why should incident responders record unknowns?

Unknowns prevent investigators from accidentally presenting assumptions as facts and identify areas requiring additional investigation.

---

# Professional Triage Checklist

## Detection

```text
[ ] Alert source identified
[ ] Detection rule understood
[ ] Timestamp confirmed
[ ] Raw event reviewed
```

## Context

```text
[ ] User identified
[ ] Host identified
[ ] Asset owner identified
[ ] Asset criticality determined
[ ] Business context checked
```

## Enrichment

```text
[ ] IOC reputation checked
[ ] Historical activity checked
[ ] Related alerts searched
[ ] Identity activity checked
[ ] Network activity checked
```

## Investigation

```text
[ ] Look-back performed
[ ] Look-forward performed
[ ] Related systems checked
[ ] Related users checked
[ ] Persistence checked
[ ] Lateral movement checked
```

## Classification

```text
[ ] False positive assessed
[ ] Suspicious activity assessed
[ ] Incident category assigned
[ ] Severity assigned
```

## Escalation

```text
[ ] Incident record created
[ ] Evidence preserved
[ ] SOC-to-IR handoff completed
[ ] Incident Commander notified if required
[ ] Relevant teams notified
```

---

# Detection and Triage Maturity

## Level 1 — Reactive

- Manual alert review
- Limited context
- Inconsistent escalation

## Level 2 — Repeatable

- Standard triage checklist
- Basic enrichment
- Defined severity

## Level 3 — Defined

- Automated enrichment
- Alert correlation
- Formal SOC-to-IR process

## Level 4 — Measured

- Triage metrics
- Detection fidelity
- False-positive tracking
- Escalation metrics

## Level 5 — Optimized

- Risk-based prioritization
- Automated enrichment
- Advanced correlation
- Continuous detection validation
- Threat-informed triage

---

# Key Metrics

Useful metrics include:

### Mean Time to Triage

Time from alert creation to initial triage.

### Mean Time to Escalate

Time from validated suspicious activity to IR escalation.

### False Positive Rate

```text id="9l1u6b"
False Positive Rate
=
False Positive Alerts
/
Total Alerts
```

### Escalation Rate

```text id="yxy1vi"
Escalation Rate
=
Escalated Alerts
/
Total Alerts
```

### Detection Fidelity

Measures how often a detection produces useful security investigations.

Metrics should be interpreted alongside alert volume and business risk.

---

# Key Takeaways

Effective incident detection and triage is a disciplined filtering process:

```text id="0q4btl"
Telemetry
   ↓
Detection
   ↓
Alert
   ↓
Enrichment
   ↓
Triage
   ↓
Validation
   ↓
Classification
   ↓
Severity
   ↓
Escalation
   ↓
Incident Response
```

The strongest analysts do not simply ask:

> **"What does this alert say?"**

They ask:

> **"What evidence generated this alert, what does the surrounding activity tell me, what is the business context, what else is connected to it, and what risk exists right now?"**

The key principles are:

- Validate before concluding
- Enrich before prioritizing
- Correlate before scoping
- Preserve before modifying
- Escalate high-risk activity quickly
- Document facts and unknowns
- Treat severity as dynamic
- Feed findings back into detection engineering

> **A good detection finds something suspicious. A good triage process determines whether it matters.**

---

# References

### NIST

**Computer Security Incident Handling Guide — SP 800-61**

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### MITRE ATT&CK

https://attack.mitre.org/

### CISA

https://www.cisa.gov/

### FIRST

https://www.first.org/

### SANS

https://www.sans.org/

### CIS Controls

https://www.cisecurity.org/controls

### Sigma

Generic and vendor-neutral detection rule format:

https://sigmahq.io/

---

# Chapter Summary

Incident detection and triage form the bridge between **security monitoring and incident response**.

A mature process transforms:

```text
Millions of Events
       ↓
Relevant Signals
       ↓
Actionable Alerts
       ↓
Contextual Triage
       ↓
Confirmed Incidents
       ↓
Coordinated Response
```

The objective is not to investigate everything equally.

The objective is to **identify the threats that matter, prioritize them correctly, preserve the evidence, and move the right incidents into coordinated response quickly.**

> **Detect accurately. Triage intelligently. Classify consistently. Escalate decisively.**
