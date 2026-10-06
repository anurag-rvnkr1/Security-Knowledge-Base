# Incident Response Fundamentals

> **A practical foundation for understanding, organizing, and executing cybersecurity incident response in an enterprise environment.**

---

## Overview

Incident Response (IR) is the structured process used by an organization to **prepare for, detect, analyze, contain, eradicate, recover from, and learn from cybersecurity incidents**.

Incident response is broader than simply reacting to malware or alerts.

A mature incident response capability answers questions such as:

- What happened?
- When did it happen?
- How did the attacker gain access?
- Which systems were affected?
- Which identities were compromised?
- What actions did the attacker perform?
- Did the attacker establish persistence?
- Did the attacker move laterally?
- Was sensitive data accessed?
- Was data exfiltrated?
- What evidence supports the findings?
- What is the current risk?
- How should the organization contain the threat?
- How can systems be safely restored?
- How can the organization prevent recurrence?

A successful incident response program combines **people, processes, technology, evidence, communication, and decision-making**.

---

# Why It Matters

A security control can fail.

An endpoint can be compromised.

A credential can be stolen.

A vulnerability can be exploited.

A malicious email can bypass filtering.

A cloud identity can be abused.

The difference between a manageable incident and a catastrophic breach often depends on **how quickly and effectively the organization responds**.

Consider:

```text
Vulnerability
     │
     ▼
Initial Access
     │
     ▼
Execution
     │
     ▼
Persistence
     │
     ▼
Privilege Escalation
     │
     ▼
Lateral Movement
     │
     ▼
Data Access
     │
     ▼
Exfiltration
     │
     ▼
Business Impact
```

Incident response attempts to interrupt this chain as early as possible.

```text
             ATTACK PROGRESSION
                    │
                    ▼
              ┌───────────┐
              │ Detection │
              └─────┬─────┘
                    │
                    ▼
              ┌───────────┐
              │  Triage   │
              └─────┬─────┘
                    │
                    ▼
              ┌───────────┐
              │ Analysis  │
              └─────┬─────┘
                    │
                    ▼
              ┌───────────┐
              │Containment│
              └─────┬─────┘
                    │
                    ▼
               Attack Path
               Interrupted
```

The earlier an organization identifies and contains malicious activity, the lower the potential impact.

---

# Event vs Alert vs Incident

One of the most important concepts in incident response is understanding the difference between an **event**, an **alert**, and an **incident**.

## Security Event

A security event is an observable activity.

Examples:

```text
User logged in
Process started
File created
DNS query generated
Firewall connection allowed
Password changed
Cloud API call executed
```

A security event is not necessarily malicious.

---

## Security Alert

An alert is generated when a security control identifies activity that may require investigation.

Examples:

```text
Multiple failed logins
Suspicious PowerShell execution
Known malware detected
Impossible-travel login
Known malicious IP connection
Privilege escalation behavior
```

An alert is a **signal**, not automatically a confirmed incident.

---

## Security Incident

An incident is a confirmed or sufficiently suspected security event that requires coordinated response.

For example:

```text
10 failed logins
        │
        ▼
Authentication Alert
        │
        ▼
Investigation
        │
        ├── Legitimate user
        │
        └── Successful login
                │
                ▼
        Suspicious PowerShell
                │
                ▼
        Credential Dumping
                │
                ▼
        Confirmed Compromise
                │
                ▼
             INCIDENT
```

The distinction is critical.

> **Not every event is an alert, not every alert is an incident, and not every incident begins with an automated alert.**

---

# Incident Response Lifecycle

A practical incident response lifecycle consists of several interconnected phases.

```text
                    ┌──────────────┐
                    │ Preparation  │
                    └──────┬───────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Detection /     │
                  │ Identification  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Triage /        │
                  │ Classification  │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Analysis /      │
                  │ Scoping         │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Containment     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Eradication     │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Recovery        │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Lessons Learned │
                  └────────┬────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │ Improve Security │
                  └────────┬────────┘
                           │
                           └──────────────► Preparation
```

The lifecycle should be considered a **continuous feedback loop**, not a linear checklist.

---

# 1. Preparation

Preparation occurs before an incident.

Organizations should establish:

- Incident response policy
- Incident response plan
- Roles and responsibilities
- Escalation procedures
- Communication channels
- Asset inventory
- Critical asset identification
- Logging requirements
- SIEM
- EDR/XDR
- Backup strategy
- Evidence collection procedures
- Contact lists
- Legal and compliance procedures
- Incident severity model
- Response playbooks
- Tabletop exercises

Without preparation, responders are forced to make important decisions during a crisis.

---

# 2. Detection and Identification

The organization identifies potentially malicious activity.

Detection sources include:

```text
SIEM
EDR/XDR
IDS/IPS
Firewall
DNS
Email Security
Cloud Security
IAM
Threat Intelligence
Threat Hunting
Users
Third Parties
Law Enforcement
Security Researchers
```

Not every incident begins with an automated detection.

For example:

> An employee reports that their account was used to send unexpected emails.

This may become the initial incident trigger.

---

# 3. Triage

Triage determines whether the alert or event requires further investigation.

A responder asks:

```text
Is the activity legitimate?

Is the alert technically valid?

Is there evidence of malicious behavior?

Which account is involved?

Which host is involved?

When did the activity occur?

Is the activity ongoing?

Is there evidence of compromise?

What is the potential impact?
```

Triage should be fast but evidence-driven.

---

# 4. Classification

The incident should be categorized.

Example categories:

| Category | Example |
|---|---|
| Malware | Trojan infection |
| Phishing | Malicious attachment |
| Credential Compromise | Stolen password |
| Account Takeover | Compromised SaaS account |
| Ransomware | File encryption |
| Data Breach | Unauthorized data access |
| Insider Threat | Malicious employee activity |
| Web Attack | Web shell |
| Cloud Compromise | Stolen cloud credentials |
| DDoS | Availability attack |
| Vulnerability Exploitation | Exploited internet-facing service |

Classification helps determine:

- Response team
- Severity
- Playbook
- Evidence requirements
- Escalation path

---

# 5. Analysis and Scoping

The response team determines the extent of the compromise.

Questions include:

```text
How did the attacker enter?

What was the first compromised asset?

What accounts were compromised?

What systems were accessed?

Did the attacker escalate privileges?

Did lateral movement occur?

Was persistence established?

What commands were executed?

What data was accessed?

Was data exfiltrated?

Are additional systems compromised?
```

The goal is to move from:

> **"We have a suspicious endpoint."**

to:

> **"We understand the attack path and current scope of compromise."**

---

# 6. Containment

Containment limits attacker activity.

Possible actions include:

- Isolating endpoint
- Disabling account
- Resetting credentials
- Revoking sessions
- Blocking malicious IP
- Blocking domain
- Blocking hash
- Disabling compromised API key
- Restricting network access
- Removing exposed service
- Disabling malicious OAuth application

Containment must consider business impact and evidence preservation.

---

# 7. Eradication

Eradication removes the attacker's presence.

Possible actions:

- Remove malware
- Remove persistence
- Reimage systems
- Patch exploited vulnerability
- Rotate credentials
- Remove unauthorized accounts
- Remove malicious scheduled tasks
- Remove rogue services
- Remove malicious applications
- Revoke compromised tokens
- Correct security misconfiguration

Eradication should address the **root cause**, not merely the visible symptom.

---

# 8. Recovery

Recovery returns the environment to a trusted operational state.

Recovery activities may include:

```text
Restore
  ↓
Validate
  ↓
Monitor
  ↓
Verify
  ↓
Return to Service
```

Important recovery questions:

- Is the system actually clean?
- Has persistence been removed?
- Were compromised credentials rotated?
- Were vulnerabilities fixed?
- Are backups trustworthy?
- Are monitoring controls active?
- Has the business owner validated functionality?

---

# 9. Lessons Learned

After the incident, the organization should determine:

- What happened?
- Why did it happen?
- What worked?
- What failed?
- What was missed?
- Which logs were unavailable?
- Which detections failed?
- Which controls failed?
- Was the response too slow?
- Were communication procedures effective?
- What should change?

The goal is not to assign blame.

The goal is to **improve the security system**.

---

# Incident Response vs Incident Management

These terms are related but not identical.

## Incident Response

Focuses primarily on:

- Investigation
- Technical analysis
- Containment
- Eradication
- Recovery
- Evidence

## Incident Management

Includes the broader organizational coordination:

- Business impact
- Stakeholder communication
- Legal
- Compliance
- Public relations
- Customer communication
- Executive decisions
- Crisis management

A major breach may therefore involve:

```text
Technical IR
     │
     ├── SOC
     ├── Forensics
     ├── Threat Hunting
     ├── Malware Analysis
     └── Detection Engineering
     
Business Incident Management
     │
     ├── Executive Leadership
     ├── Legal
     ├── Privacy
     ├── Compliance
     ├── Communications
     └── Business Owners
```

---

# Incident Response Team

A mature incident response capability usually involves multiple specialists.

```text
                         Incident Commander
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
          ▼                     ▼                     ▼
        SOC / IR             Forensics              IT
          │                     │                     │
          ├───────────┬─────────┤                     │
          │           │         │                     │
          ▼           ▼         ▼                     ▼
       Threat       Malware    Cloud               Identity
      Hunting      Analysis   Security              Security
          │
          └──────────────────┬──────────────────────┘
                             │
                             ▼
                         Leadership
                             │
                    ┌────────┼────────┐
                    ▼        ▼        ▼
                  Legal    Privacy  Compliance
```

---

# Incident Commander

The Incident Commander coordinates the response.

Responsibilities may include:

- Establishing incident objectives
- Assigning responders
- Coordinating teams
- Tracking decisions
- Managing escalation
- Maintaining situational awareness
- Coordinating communications
- Managing response priorities
- Declaring incident status
- Coordinating closure

The Incident Commander does not necessarily perform every technical investigation task.

---

# SOC Analyst

The SOC is often the first security team to encounter an incident.

Responsibilities may include:

- Alert validation
- Initial triage
- IOC investigation
- SIEM searches
- EDR investigation
- Enrichment
- Initial classification
- Escalation

---

# Incident Responder

The incident responder performs deeper investigation and response.

Responsibilities may include:

- Scoping
- Timeline construction
- Host investigation
- Account investigation
- Network investigation
- Containment
- Eradication
- Recovery coordination

---

# Threat Hunter

Threat hunters help identify additional attacker activity that automated detections may have missed.

For example:

```text
Known compromised host
        │
        ▼
Identify user
        │
        ▼
Search authentication activity
        │
        ▼
Identify other hosts
        │
        ▼
Search process activity
        │
        ▼
Identify persistence
        │
        ▼
Expand incident scope
```

This is where incident response and threat hunting strongly overlap.

---

# Digital Forensics

Forensics focuses on evidence acquisition and analysis.

Potential evidence includes:

- Disk images
- Memory
- Logs
- Browser artifacts
- Event logs
- File timestamps
- Registry artifacts
- Network captures
- Cloud audit logs

---

# Detection Engineering

Incident response frequently exposes detection gaps.

For example:

```text
Incident
   │
   ▼
Attacker PowerShell
   │
   ▼
No Detection
   │
   ▼
IR Investigation
   │
   ▼
Detection Gap Identified
   │
   ▼
New Detection Rule
   │
   ▼
Validation
   │
   ▼
Future Attack Detected Faster
```

This creates a valuable feedback loop.

---

# Incident Severity

Severity determines the urgency and resources required.

A sample model:

## SEV-1 — Critical

Examples:

- Active ransomware
- Domain administrator compromise
- Major data breach
- Production environment compromise
- Critical infrastructure compromise

Response:

```text
Immediate
24/7 response
Executive escalation
Full IR activation
```

---

## SEV-2 — High

Examples:

- Confirmed endpoint compromise
- Privileged account compromise
- Significant malware outbreak
- Cloud administrator compromise

Response:

```text
Rapid escalation
Dedicated investigation
Containment priority
```

---

## SEV-3 — Medium

Examples:

- Limited malware infection
- Suspicious account activity
- Confirmed phishing compromise with limited scope

Response:

```text
Standard IR workflow
Focused investigation
```

---

## SEV-4 — Low

Examples:

- Low-impact suspicious activity
- Contained policy violations
- Limited security events

Response:

```text
SOC investigation
Document and monitor
```

Severity should be reassessed as new evidence becomes available.

---

# Severity Decision Factors

Severity should not depend on a single indicator.

Consider:

```text
                    SEVERITY
                       │
       ┌───────────────┼───────────────┐
       │               │               │
       ▼               ▼               ▼
    Business         Data            Identity
     Impact          Impact           Impact
       │               │               │
       └───────────────┼───────────────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
          Scope     Persistence  Privilege
             │         │         │
             └─────────┼─────────┘
                       ▼
                  Final Severity
```

Factors include:

- Number of affected systems
- Number of affected users
- Data sensitivity
- Privilege level
- Business criticality
- Attack persistence
- Regulatory requirements
- Customer impact
- Availability impact
- Potential for further spread

---

# Common Incident Categories

## Phishing

Malicious emails attempt to:

- Steal credentials
- Deliver malware
- Redirect users
- Exploit vulnerabilities

---

## Credential Compromise

Examples:

- Password theft
- Credential stuffing
- Password spraying
- Infostealer compromise
- Token theft

---

## Malware

Examples:

- Trojan
- RAT
- Infostealer
- Loader
- Botnet
- Worm

---

## Ransomware

Typical sequence:

```text
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Credential Access
      ↓
Lateral Movement
      ↓
Data Collection
      ↓
Exfiltration
      ↓
Encryption
```

---

## Web Application Compromise

Examples:

- SQL injection
- Command injection
- File upload abuse
- Authentication bypass
- Web shell deployment

---

## Cloud Compromise

Examples:

- Stolen access keys
- Compromised identity
- Excessive permissions
- OAuth abuse
- Cloud persistence
- Unauthorized resource deployment

---

## Insider Threat

Potential scenarios:

- Data theft
- Privilege abuse
- Unauthorized access
- Malicious configuration changes
- Intellectual property theft

---

# Detection Sources

Incident detection can originate from many sources.

```text
                         Detection
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
       ▼                    ▼                    ▼
    Automated             Human              External
     Controls             Reports             Sources
       │                    │                    │
       ├── SIEM             ├── Employee         ├── CERT
       ├── EDR              ├── Admin            ├── Vendor
       ├── IDS              ├── Security Team    ├── Customer
       ├── Email            └── User             └── Researcher
       └── Cloud
```

Examples:

- SIEM alert
- EDR detection
- IDS alert
- Firewall alert
- User report
- Security researcher report
- Threat intelligence notification
- Cloud security alert
- Law enforcement notification
- Third-party notification

---

# Incident Identification Without Alerts

Not every incident is automatically detected.

Example:

A finance employee notices that an unusual email was sent from their account.

```text
Employee Observation
        ↓
SOC Investigation
        ↓
Authentication Logs
        ↓
Suspicious Login
        ↓
New Device
        ↓
Mailbox Activity
        ↓
OAuth Application
        ↓
Account Compromise
```

This demonstrates why human reporting remains important.

---

# Evidence-Based Investigation

Incident response should separate observations from assumptions.

Consider:

> "The attacker accessed the server at 02:13."

This should be supported by evidence.

For example:

```text
02:11  Authentication success
02:12  VPN connection
02:13  SSH session
02:14  Command execution
02:16  File created
02:18  Outbound connection
```

The timeline creates an evidence-backed narrative.

---

# Facts vs Hypotheses

A responder should distinguish:

### Confirmed

Evidence directly demonstrates the activity.

### Highly Likely

Multiple indicators strongly support the conclusion.

### Possible

Evidence exists but is insufficient for confirmation.

### Unknown

Available evidence does not establish the answer.

Example:

```text
Confirmed:
User account authenticated from IP X.

Confirmed:
PowerShell executed on endpoint Y.

Likely:
The activity was attacker-controlled.

Possible:
Credentials were stolen from endpoint Y.

Unknown:
Whether data was exfiltrated.
```

This distinction is extremely important in professional incident reporting.

---

# Incident Timeline

Timeline reconstruction is one of the most useful IR techniques.

Example:

```text
08:14
Phishing email delivered
        │
        ▼
08:21
User clicked link
        │
        ▼
08:23
Credential submitted
        │
        ▼
08:27
Attacker authentication
        │
        ▼
08:31
Mailbox access
        │
        ▼
08:42
Malicious forwarding rule created
        │
        ▼
09:05
Additional accounts targeted
        │
        ▼
09:17
Incident detected
        │
        ▼
09:25
Account contained
```

The timeline allows responders to understand:

- Initial access
- Attacker dwell time
- Actions
- Detection delay
- Response delay
- Business impact

---

# Dwell Time

**Dwell time** is the period during which an attacker remains inside an environment before detection or containment.

Conceptually:

```text
Initial Compromise
       │
       ├───────────────────────────┐
       │                           │
       ▼                           ▼
   Attacker Activity            Detection
                                   │
                                   ▼
                              Containment
```

Long dwell time may indicate:

- Poor visibility
- Weak detection
- Insufficient logging
- Successful evasion
- Inadequate monitoring

Reducing dwell time is a major security objective.

---

# Mean Time Metrics

Organizations frequently measure incident response performance using metrics such as:

### MTTD

**Mean Time to Detect**

How long it takes to identify an incident.

### MTTA

**Mean Time to Acknowledge**

How long it takes for the security team to acknowledge an alert.

### MTTC

**Mean Time to Contain**

How long it takes to prevent further attacker activity.

### MTTR

**Mean Time to Respond/Recover**

Depending on organizational definition, this measures response or recovery time.

Example:

```text
Compromise
    │
    │  12 hours
    ▼
Detection
    │
    │  15 minutes
    ▼
Acknowledgement
    │
    │  30 minutes
    ▼
Containment
    │
    │  4 hours
    ▼
Recovery
```

Organizations should define metrics consistently before comparing performance.

---

# Incident Communication

Technical response is only one part of incident management.

Communication may involve:

```text
Incident Commander
       │
       ├── Security
       ├── IT
       ├── Legal
       ├── Privacy
       ├── Compliance
       ├── Communications
       ├── Business Owner
       └── Executive Leadership
```

Communication should be:

- Accurate
- Timely
- Controlled
- Evidence-based
- Appropriate for the audience

Technical details should not be unnecessarily distributed to people who do not require them.

---

# Incident Documentation

A professional incident record should contain:

```text
Incident ID:
Title:
Severity:
Status:
Detection Source:
Date / Time:
Incident Commander:

Summary:

Initial Indicators:

Affected Assets:

Affected Users:

Initial Timeline:

Investigation Findings:

Evidence:

Containment Actions:

Eradication Actions:

Recovery Actions:

Root Cause:

Business Impact:

Data Impact:

Detection Gaps:

Security Control Gaps:

Lessons Learned:

Follow-up Actions:

Owner:

Due Date:

Closure Date:
```

---

# Incident Status

A standardized incident status model can improve coordination.

```text
NEW
 │
 ▼
TRIAGE
 │
 ▼
INVESTIGATING
 │
 ▼
CONTAINING
 │
 ▼
ERADICATING
 │
 ▼
RECOVERING
 │
 ▼
MONITORING
 │
 ▼
CLOSED
```

An incident may move backward when new evidence changes the situation.

For example:

```text
Recovering
    │
    ▼
New Persistence Found
    │
    ▼
Investigating
    │
    ▼
Containment
```

Incident response is therefore dynamic.

---

# Common Incident Response Misconfigurations

Poor preparation can significantly increase incident impact.

## 1. No Centralized Logging

Without centralized logs:

- Timeline construction becomes difficult
- Evidence may disappear
- Correlation becomes difficult

---

## 2. Incomplete Endpoint Visibility

Some systems may lack:

- EDR
- Sysmon
- Audit logging
- Process telemetry

This creates investigation blind spots.

---

## 3. No Asset Inventory

Responders may not know:

- Which systems are affected
- Which systems are critical
- Who owns an asset

---

## 4. No Incident Severity Model

Without predefined severity criteria, teams may disagree about urgency.

---

## 5. No Escalation Procedure

A SOC analyst may identify a critical incident but not know:

- Who to contact
- Who has authority
- How quickly escalation should occur

---

## 6. No Tested Backups

Backups are not sufficient if restoration has never been validated.

---

## 7. No Incident Playbooks

Responders may waste time deciding basic response steps during an active attack.

---

## 8. No Tabletop Exercises

Plans that have never been tested may fail during real incidents.

---

# Prevention and Preparedness

Incident response begins before an incident.

Organizations should maintain:

### Asset Visibility

Know:

- Hosts
- Servers
- Applications
- Cloud resources
- Identities
- Critical systems

### Logging

Collect appropriate:

- Authentication logs
- Endpoint logs
- Network logs
- Cloud audit logs
- Application logs

### Detection

Deploy:

- SIEM
- EDR
- IDS/IPS
- Email security
- Cloud security monitoring

### Access Control

Use:

- MFA
- Least privilege
- Privileged access management
- Strong authentication

### Backup

Maintain:

- Offline or immutable backups
- Tested recovery procedures
- Multiple recovery points

### Exercises

Conduct:

- Tabletop exercises
- Purple-team exercises
- Incident simulations
- Recovery exercises

---

# Best Practices

## 1. Prepare Before the Incident

Do not create the response process during an emergency.

## 2. Centralize Evidence

Use appropriate centralized logging and evidence storage.

## 3. Maintain Accurate Time Synchronization

Timestamp inconsistencies can make timeline reconstruction difficult.

Use:

```text
NTP
```

across relevant systems.

## 4. Define Roles

Everyone should know:

- Who leads
- Who investigates
- Who communicates
- Who approves containment
- Who handles legal issues

## 5. Preserve Evidence

Do not unnecessarily destroy:

- Logs
- Memory
- Files
- Network captures
- Authentication records

## 6. Scope Beyond the First Host

The first compromised system may only be one part of a larger attack.

## 7. Track Decisions

Document important response decisions and their rationale.

## 8. Validate Recovery

Do not assume recovery succeeded simply because the system is online.

## 9. Improve Detection

Every incident should produce opportunities to improve security monitoring.

## 10. Conduct Lessons Learned

Use incidents to strengthen the organization.

---

# Commands and Investigation Examples

These commands are intended for **authorized defensive investigation**.

---

## Windows

### Identify Current User

```powershell
whoami
```

### System Information

```powershell
systeminfo
```

### Network Configuration

```powershell
ipconfig /all
```

### Active Connections

```powershell
netstat -ano
```

### Running Processes

```powershell
Get-Process
```

### Services

```powershell
Get-Service
```

### Scheduled Tasks

```powershell
Get-ScheduledTask
```

### Recent Windows Events

```powershell
Get-WinEvent -LogName Security -MaxEvents 50
```

---

## Linux

### Current User

```bash
whoami
```

### System Information

```bash
uname -a
```

### Network Connections

```bash
ss -tulpn
```

### Running Processes

```bash
ps aux
```

### Logged-In Users

```bash
w
```

### Recent Login Activity

```bash
last
```

### Failed Authentication

On systems using traditional authentication logs:

```bash
grep "Failed password" /var/log/auth.log
```

On systemd-based systems:

```bash
journalctl -u ssh
```

---

## DNS Investigation

Example:

```bash
nslookup suspicious-domain.example
```

or:

```bash
dig suspicious-domain.example
```

Investigators should correlate DNS activity with:

- Endpoint
- User
- Process
- Destination IP
- Timestamp

---

## Network Capture

Capture traffic in an authorized environment:

```bash
tcpdump -i eth0 -w incident.pcap
```

Read a capture:

```bash
tcpdump -r incident.pcap
```

For deeper analysis:

```text
incident.pcap
      │
      ▼
Wireshark
      │
      ├── DNS
      ├── HTTP
      ├── TLS
      ├── TCP
      └── Conversations
```

---

# Practical Lab

## Lab: Investigating a Suspected Compromised Endpoint

### Objective

Investigate a simulated compromised workstation and determine:

1. What happened?
2. Which account was involved?
3. Which process initiated the activity?
4. Which external systems were contacted?
5. Whether persistence exists?
6. What containment action should be taken?

---

## Scenario

A SOC alert reports:

```text
Suspicious PowerShell execution
Host: WS-104
User: analyst01
Time: 10:42 UTC
```

The EDR reports a suspicious process tree:

```text
WINWORD.EXE
     │
     └── powershell.exe
             │
             └── suspicious-script.ps1
```

---

## Investigation Steps

### Step 1 — Validate the User

Determine whether the user legitimately opened Microsoft Word.

Questions:

```text
Was the document expected?

Did the user receive it by email?

Was the sender trusted?

Was the document downloaded?
```

---

### Step 2 — Investigate the Process

Review:

```text
Parent process
Child process
Command line
Execution time
User
Integrity level
File path
Hash
```

---

### Step 3 — Investigate Network Activity

Determine:

```text
Destination IP
Destination domain
Port
Protocol
Connection time
Process responsible
```

---

### Step 4 — Search for Persistence

Investigate:

```text
Scheduled Tasks
Services
Startup folders
Registry Run keys
WMI subscriptions
New accounts
Browser extensions
```

---

### Step 5 — Scope the User

Search for:

```text
Previous logins
VPN activity
Cloud authentication
Email activity
Other endpoints
Password changes
MFA activity
```

---

### Step 6 — Scope the Host

Search for:

```text
Other suspicious processes
Other outbound connections
New files
Credential access
Security control changes
Additional persistence
```

---

### Step 7 — Determine Severity

Consider:

```text
Is the host critical?

Is the user privileged?

Is there persistence?

Is credential theft suspected?

Is lateral movement observed?

Is data access observed?
```

---

### Step 8 — Containment

Potential actions:

```text
Isolate endpoint
Reset credentials
Revoke sessions
Block malicious infrastructure
Preserve evidence
```

---

### Expected Investigation Output

Produce an incident summary:

```text
Incident:
Suspicious PowerShell Execution

Affected Host:
WS-104

Affected User:
analyst01

Initial Access:
Malicious Office document

Execution:
PowerShell

Persistence:
Unknown / Identified

Network Activity:
Suspicious outbound connection

Credential Access:
Unknown

Lateral Movement:
Not observed / Observed

Data Access:
Unknown

Containment:
Endpoint isolated

Severity:
SEV-2

Next Actions:
Forensic analysis
Credential reset
Threat hunt
Detection improvement
```

---

# Incident Response Checklist

## Before an Incident

```text
[ ] Incident response plan exists
[ ] Roles defined
[ ] Contact list maintained
[ ] Asset inventory maintained
[ ] Critical assets identified
[ ] Logging enabled
[ ] EDR deployed
[ ] SIEM configured
[ ] Backups tested
[ ] Playbooks created
[ ] Tabletop exercises conducted
```

---

## During an Incident

```text
[ ] Validate alert
[ ] Create incident record
[ ] Assign severity
[ ] Preserve evidence
[ ] Identify affected assets
[ ] Identify affected identities
[ ] Build timeline
[ ] Determine scope
[ ] Contain threat
[ ] Escalate appropriately
[ ] Document decisions
```

---

## After an Incident

```text
[ ] Eradicate root cause
[ ] Recover systems
[ ] Validate recovery
[ ] Monitor environment
[ ] Complete incident report
[ ] Conduct lessons learned
[ ] Identify detection gaps
[ ] Improve controls
[ ] Update playbooks
[ ] Track remediation
```

---

# Interview Questions

## Fundamentals

### 1. What is incident response?

Incident response is the structured process of preparing for, detecting, investigating, containing, eradicating, recovering from, and learning from cybersecurity incidents.

---

### 2. What is the difference between an event, alert, and incident?

An **event** is an observable activity.

An **alert** is a security signal requiring investigation.

An **incident** is a confirmed or sufficiently suspected security event requiring coordinated response.

---

### 3. What are the major phases of incident response?

A practical lifecycle includes:

```text
Preparation
Detection
Triage
Analysis
Containment
Eradication
Recovery
Lessons Learned
```

---

### 4. What is incident triage?

Triage is the process of rapidly evaluating an alert or suspected security event to determine its validity, severity, scope, and appropriate next action.

---

### 5. What is incident containment?

Containment limits attacker activity and prevents additional damage while allowing the response team to investigate and eradicate the threat.

---

### 6. What is eradication?

Eradication removes the attacker's presence and addresses the mechanisms that allowed the compromise.

---

### 7. What is recovery?

Recovery safely restores affected systems and services to trusted operational status.

---

### 8. What is the difference between containment and eradication?

**Containment** stops or limits the attack.

**Eradication** removes the attacker and the underlying cause of compromise.

---

### 9. Why is evidence preservation important?

Evidence allows investigators to:

- Reconstruct events
- Determine scope
- Establish root cause
- Validate conclusions
- Support legal or regulatory processes when applicable

---

### 10. What is an Incident Commander?

The Incident Commander coordinates the overall response, establishes priorities, assigns responsibilities, manages escalation, and maintains situational awareness.

---

### 11. What is dwell time?

Dwell time is the period during which an attacker remains within an environment before detection or containment.

---

### 12. What is root cause analysis?

Root cause analysis determines the underlying condition that allowed the incident to occur rather than focusing only on its immediate symptoms.

---

### 13. What should you do when you detect a compromised endpoint?

A reasonable high-level workflow is:

```text
Validate
   ↓
Preserve Evidence
   ↓
Investigate
   ↓
Scope
   ↓
Contain
   ↓
Eradicate
   ↓
Recover
   ↓
Monitor
```

---

### 14. Should you immediately shut down a compromised system?

Not always.

Depending on the incident, shutting down a system may:

- Destroy volatile evidence
- Interrupt forensic collection
- Prevent analysis of active connections

The response should consider:

- Threat severity
- Business impact
- Evidence requirements
- Persistence
- Risk of continued compromise

---

### 15. What should happen after an incident?

The organization should:

- Complete documentation
- Conduct lessons learned
- Identify root cause
- Identify detection gaps
- Improve controls
- Update playbooks
- Track remediation

---

# Key Takeaways

Incident response is fundamentally about **structured decision-making under uncertainty**.

The most important principles are:

```text
Prepare
  ↓
Detect
  ↓
Validate
  ↓
Investigate
  ↓
Scope
  ↓
Contain
  ↓
Eradicate
  ↓
Recover
  ↓
Learn
  ↓
Improve
```

A mature responder should be able to move from:

> **"We received an alert."**

to:

> **"We understand what happened, how it happened, what is affected, what evidence supports our findings, what risk remains, what action should happen next, and how the organization can prevent recurrence."**

---

# References

### NIST

**NIST SP 800-61 — Computer Security Incident Handling Guide**

https://csrc.nist.gov/publications/detail/sp/800-61/rev-2/final

### NIST Cybersecurity Framework

https://www.nist.gov/cyberframework

### CISA

Incident response and cybersecurity guidance:

https://www.cisa.gov/

### MITRE ATT&CK

Adversary tactics and techniques:

https://attack.mitre.org/

### FIRST

Incident response and security team resources:

https://www.first.org/

### SANS

Incident response resources and training:

https://www.sans.org/

### CIS

Security controls and defensive practices:

https://www.cisecurity.org/

---

# Chapter Summary

Incident response is not simply an emergency procedure.

It is an organizational capability built around:

```text
People
  +
Process
  +
Technology
  +
Evidence
  +
Communication
  +
Continuous Improvement
```

The strongest incident response programs prepare before incidents occur, investigate using evidence, contain threats deliberately, recover from a trusted state, and continuously feed lessons back into security engineering.

> **Detect early. Investigate systematically. Contain decisively. Recover safely. Learn continuously.**
