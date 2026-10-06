# Chapter 11 – Incident Response & SIEM Workflows

> Incident response is the structured process used to detect, analyze, contain, eradicate, and recover from security incidents. A SIEM provides the visibility, evidence, correlation, alerting, and investigation capabilities that support this process.

---

# 1. Introduction

A security incident is not simply:

```text
One suspicious event
```

It may involve:

```text
Multiple Alerts
Multiple Users
Multiple Hosts
Multiple Attack Techniques
Multiple Data Sources
```

Incident response turns these signals into an organized process:

```text
Detection
   ↓
Triage
   ↓
Investigation
   ↓
Incident Declaration
   ↓
Containment
   ↓
Eradication
   ↓
Recovery
   ↓
Lessons Learned
```

---

# 2. What is Incident Response?

Incident response is the organized approach for handling security incidents.

Its objectives are to:

```text
Detect
Analyze
Contain
Eradicate
Recover
Learn
```

The exact workflow varies by organization and incident type.

---

# 3. Event vs Alert vs Incident

These concepts must be distinguished.

## Event

A recorded activity:

```text
Successful Login
```

## Alert

A security detection:

```text
Suspicious Login
```

## Incident

A confirmed or strongly suspected security event requiring coordinated response:

```text
Compromised Account
```

Conceptually:

```text
EVENT
  ↓
DETECTION
  ↓
ALERT
  ↓
TRIAGE
  ↓
INCIDENT
```

Not every event or alert becomes an incident.

---

# 4. Incident Response Lifecycle

A practical lifecycle is:

```text
Preparation
    ↓
Detection & Analysis
    ↓
Containment
    ↓
Eradication
    ↓
Recovery
    ↓
Post-Incident Activity
```

This is commonly associated with established incident-response frameworks, although terminology can vary.

---

# 5. Phase 1 – Preparation

Preparation happens before an incident.

It includes:

```text
Logging
Monitoring
Playbooks
Communication Plans
Access Controls
Backups
Endpoint Visibility
Threat Intelligence
Training
Incident Roles
```

---

# 6. SIEM Preparation

For SIEM specifically:

```text
Identify Data Sources
       ↓
Collect Logs
       ↓
Normalize
       ↓
Create Detections
       ↓
Create Correlation Rules
       ↓
Test Alerts
       ↓
Create Dashboards
       ↓
Define Escalation
```

---

# 7. Incident Response Roles

Typical roles may include:

```text
SOC Analyst
Incident Responder
Detection Engineer
Threat Hunter
Security Engineer
IT Administrator
Cloud Engineer
Legal
Privacy
Management
Communications
```

The exact structure depends on organization size.

---

# 8. Incident Severity

Organizations may classify incidents as:

```text
Critical
High
Medium
Low
```

Severity may depend on:

```text
Business Impact
Data Sensitivity
Asset Criticality
Scope
Confidence
Attacker Access
Persistence
Privilege Level
Regulatory Impact
```

---

# 9. Critical Incident Example

```text
Ransomware
+
Critical Servers
+
Sensitive Data
+
Large Scope
```

Potential classification:

```text
Critical
```

---

# 10. Low-Severity Incident Example

```text
Compromised Test Account
+
Isolated Lab System
+
No Sensitive Data
+
No Lateral Movement
```

Potential classification:

```text
Low / Medium
```

Actual classification should follow organizational policy.

---

# 11. Incident Identification

An incident can originate from:

```text
SIEM Alert
EDR
Firewall
Threat Intelligence
User Report
Cloud Detection
Email Security
Vulnerability Assessment
Threat Hunt
Third Party
```

---

# 12. SIEM-to-Incident Workflow

```text
SIEM Alert
    ↓
Alert Validation
    ↓
Triage
    ↓
Related Alerts
    ↓
Evidence Collection
    ↓
Incident Declaration
    ↓
Case Creation
    ↓
Investigation
    ↓
Response
```

---

# 13. Alert Validation

Ask:

```text
Why did it trigger?

Which rule?

Which event?

Which user?

Which host?

Which IP?

Is the activity expected?

Is the data trustworthy?
```

---

# 14. Incident Declaration

An alert becomes an incident when evidence indicates:

```text
Confirmed Malicious Activity
```

or:

```text
Strong Evidence of Compromise
```

Examples:

```text
Known Malware Executed
Compromised Credentials
Unauthorized Privilege Escalation
Confirmed Data Exfiltration
Ransomware Activity
```

---

# 15. Incident Case

A case should contain:

```text
Incident ID
Title
Severity
Status
Owner
Created Time
Detection Source
Affected Assets
Affected Users
Timeline
Evidence
Queries
Findings
Actions
Communication
Resolution
```

---

# 16. Case Status

Typical statuses:

```text
New
Assigned
Investigating
Contained
Eradication
Recovery
Resolved
Closed
```

Organizations may use different naming.

---

# 17. Incident Timeline

Example:

```text
09:45  Phishing Email
09:50  User Click
09:51  File Download
09:52  Process Execution
09:55  C2 Connection
10:01  Credential Access
10:07  Remote Login
10:15  Detection
10:25  Host Isolated
```

This timeline becomes the foundation of the investigation.

---

# 18. Detection Time

Important timestamps include:

```text
Event Time
Detection Time
Alert Time
Analyst Time
Containment Time
Recovery Time
```

These allow teams to measure response performance.

---

# 19. MTTD

MTTD:

```text
Mean Time To Detect
```

Conceptually:

```text
Detection Time
-
Attack Start Time
```

Lower is generally better.

---

# 20. MTTA

MTTA:

```text
Mean Time To Acknowledge
```

Measures how long it takes for an alert or incident to receive analyst attention.

---

# 21. MTTR

MTTR is commonly used for:

```text
Mean Time To Respond
```

or:

```text
Mean Time To Recover
```

depending on the organization's definition.

Always define the metric before comparing it.

---

# 22. Why Response Metrics Matter

Example:

```text
Attack Start
09:00

Detection
09:15

Acknowledgement
09:18

Containment
09:30

Recovery
11:00
```

This allows measurement of:

```text
Detection
Acknowledgement
Containment
Recovery
```

---

# 23. Containment

Containment limits attacker access or prevents further damage.

Examples:

```text
Isolate Endpoint
Disable Account
Revoke Sessions
Block IP
Block Domain
Disable Access Key
Segment Network
```

Actions should follow approved incident-response procedures.

---

# 24. Short-Term Containment

Goal:

```text
Stop immediate spread.
```

Examples:

```text
Endpoint Isolation
Account Disablement
Network Blocking
Session Revocation
```

---

# 25. Long-Term Containment

Goal:

```text
Maintain business operations
while preparing permanent remediation.
```

Examples:

```text
Network Segmentation
Temporary Access Restrictions
Temporary Service Isolation
Credential Restrictions
```

---

# 26. Eradication

Eradication removes the underlying threat.

Examples:

```text
Remove Malware
Delete Persistence
Reset Credentials
Rotate Keys
Patch Vulnerability
Remove Malicious Accounts
Clean Systems
```

---

# 27. Recovery

Recovery restores normal operations.

Examples:

```text
Restore Systems
Validate Integrity
Re-enable Accounts
Monitor Systems
Verify Security Controls
```

Recovery should be controlled rather than simply returning everything to its previous state.

---

# 28. Recovery Monitoring

After recovery:

```text
Increased Monitoring
       ↓
Watch for Re-infection
       ↓
Watch for Re-entry
       ↓
Validate Controls
```

---

# 29. Re-Compromise

A system may become compromised again if:

```text
Root Cause Not Fixed
Persistence Remains
Credentials Not Rotated
Vulnerability Not Patched
Attacker Infrastructure Still Accessible
```

Therefore eradication must address the cause, not just the visible symptom.

---

# 30. Post-Incident Activity

After an incident:

```text
Lessons Learned
Detection Improvements
Control Improvements
Root Cause Analysis
Documentation
Training
Policy Updates
```

---

# 31. Root Cause Analysis

Ask:

```text
How did the attacker enter?

Why was the attack successful?

Why wasn't it detected earlier?

Why did controls fail?

What allowed persistence?

What allowed lateral movement?
```

---

# 32. Five Whys

Example:

```text
Why was the account compromised?
        ↓
Phishing

Why did phishing succeed?
        ↓
User clicked malicious link

Why wasn't it blocked?
        ↓
Domain was newly registered

Why wasn't the activity detected?
        ↓
No effective detection

Why?
        ↓
Missing telemetry/detection coverage
```

This helps identify systemic weaknesses.

---

# 33. SIEM Investigation Workflow

A practical workflow:

```text
Alert
 ↓
Identify Rule
 ↓
Identify Entities
 ↓
Search Related Events
 ↓
Build Timeline
 ↓
Determine Scope
 ↓
Enrich
 ↓
Assess Risk
 ↓
Declare Incident
 ↓
Contain
 ↓
Eradicate
 ↓
Recover
 ↓
Improve Detection
```

---

# 34. Alert-to-Case Automation

A SIEM can automatically create:

```text
Case
```

when:

```text
High-risk alert
```

is generated.

Example:

```text
Risk > Threshold
      ↓
Create Case
      ↓
Assign SOC Queue
```

---

# 35. Case Enrichment

Automatically attach:

```text
Threat Intelligence
Asset Criticality
User Information
Related Alerts
MITRE ATT&CK
Historical Activity
GeoIP
Vulnerability Data
```

---

# 36. Case Correlation

Multiple alerts can be connected:

```text
Alert A
Suspicious Login

Alert B
PowerShell

Alert C
Credential Access

Alert D
Remote Login
```

↓

```text
Incident CASE-2026-001
```

---

# 37. Case Deduplication

If multiple detections represent the same behavior:

```text
100 Alerts
```

may become:

```text
1 Incident
+
100 Evidence Events
```

This reduces analyst overload.

---

# 38. Incident Ownership

Every incident should have:

```text
Owner
```

Example:

```text
Incident:
INC-1001

Owner:
SOC Analyst

Escalation:
Incident Response Team
```

Clear ownership prevents incidents from remaining unassigned.

---

# 39. Escalation

Escalate based on:

```text
Severity
Impact
Scope
Confidence
Data Sensitivity
Privilege
Business Criticality
Regulatory Requirements
```

---

# 40. Escalation Example

```text
Low:
SOC handles

Medium:
Senior Analyst

High:
Incident Response

Critical:
Incident Response
+
Security Leadership
+
Relevant Business Teams
```

Actual escalation paths must follow organizational policy.

---

# 41. Communication

Incident communication may involve:

```text
SOC
IT
Security Leadership
Management
Legal
Privacy
Business Owners
Vendors
```

Communication should be:

```text
Accurate
Timely
Need-to-Know
Documented
```

---

# 42. Incident Communication Template

```text
Incident ID:
INC-1001

Severity:
High

Summary:
Potential account compromise detected.

Affected:
2 users
3 endpoints

Initial Detection:
10:15 UTC

Current Status:
Containment in progress

Known Impact:
No confirmed data exfiltration.

Next Actions:
Credential reset
Session revocation
Endpoint investigation
```

---

# 43. Evidence Collection

Evidence may include:

```text
SIEM Logs
EDR Events
Firewall Logs
DNS
Proxy
Cloud Logs
Email
Authentication
Process Data
File Hashes
Network Connections
```

---

# 44. Evidence Integrity

Important considerations:

```text
Timestamp
Source
Collection Method
Storage
Access
Integrity
```

For formal investigations, evidence procedures should follow organizational, legal, and forensic requirements.

---

# 45. SIEM as Evidence Repository

The SIEM can provide:

```text
Historical Logs
Correlated Events
Detection Metadata
Alert History
Investigation Queries
Timeline
```

But:

> The SIEM should not automatically be treated as the sole source of truth.

Other systems may contain richer or authoritative evidence.

---

# 46. Log Preservation

During major incidents:

```text
Identify Relevant Sources
       ↓
Preserve Data
       ↓
Increase Retention if Needed
       ↓
Prevent Loss
```

Preservation should follow organizational procedures.

---

# 47. Incident Response Playbook

A playbook defines:

```text
Trigger
Initial Validation
Enrichment
Decision Points
Containment
Escalation
Recovery
Documentation
```

---

# 48. Example – Account Compromise Playbook

```text
Trigger:
Suspicious Account Activity

1. Validate login.
2. Check source IP.
3. Check device.
4. Check MFA.
5. Check recent actions.
6. Check privilege changes.
7. Search related activity.
8. Determine scope.
9. Revoke sessions if authorized.
10. Reset credentials.
11. Investigate affected endpoints.
12. Document findings.
```

---

# 49. Example – Malware Playbook

```text
Trigger:
Malware Detection

1. Validate detection.
2. Identify hash.
3. Identify host.
4. Identify user.
5. Inspect process tree.
6. Search other hosts.
7. Check network connections.
8. Check persistence.
9. Isolate endpoint if authorized.
10. Remove malware.
11. Investigate root cause.
12. Recover.
```

---

# 50. Example – Phishing Playbook

```text
Trigger:
Reported Phishing Email

1. Identify sender.
2. Extract URLs.
3. Extract attachments.
4. Check reputation.
5. Search mailboxes.
6. Determine recipients.
7. Determine clicks.
8. Identify downloads.
9. Investigate endpoint activity.
10. Remove malicious messages.
11. Reset credentials if necessary.
12. Document.
```

---

# 51. Example – Ransomware Playbook

```text
Trigger:
Mass Encryption Behavior

1. Validate detection.
2. Identify affected hosts.
3. Determine scope.
4. Isolate affected systems.
5. Protect backups.
6. Disable compromised accounts.
7. Search for lateral movement.
8. Identify persistence.
9. Preserve evidence.
10. Eradicate.
11. Restore systems.
12. Increase monitoring.
```

Actual response must follow the organization's ransomware procedures and business continuity requirements.

---

# 52. SIEM Workflow for Ransomware

```text
File Encryption Events
        ↓
Process Correlation
        ↓
Multiple Hosts
        ↓
High Risk
        ↓
Incident
        ↓
Containment
```

---

# 53. SIEM Workflow for Account Takeover

```text
Unusual Login
      ↓
MFA Change
      ↓
New Device
      ↓
Privilege Change
      ↓
High Risk
      ↓
Incident
```

---

# 54. SIEM Workflow for C2

```text
Endpoint
   ↓
Suspicious Process
   ↓
DNS
   ↓
Known Malicious Domain
   ↓
Outbound Connection
   ↓
Beaconing
   ↓
High Risk
```

---

# 55. SIEM Workflow for Data Exfiltration

```text
Sensitive Access
      ↓
Archive Creation
      ↓
Large Data Transfer
      ↓
Rare Destination
      ↓
Risk
      ↓
Incident
```

---

# 56. Incident Status Workflow

```text
NEW
 ↓
TRIAGED
 ↓
INVESTIGATING
 ↓
CONFIRMED
 ↓
CONTAINMENT
 ↓
ERADICATION
 ↓
RECOVERY
 ↓
RESOLVED
 ↓
CLOSED
```

---

# 57. Incident Closure Criteria

Before closing, confirm:

```text
Threat Removed
Persistence Removed
Affected Credentials Addressed
Vulnerability Fixed
Systems Recovered
Monitoring Enabled
Evidence Documented
Root Cause Identified
Required Notifications Completed
```

Exact closure requirements vary by incident and organization.

---

# 58. Lessons Learned

Ask:

```text
What worked?

What failed?

What was missing?

What should be automated?

Which detection failed?

Which logs were missing?

How can response time improve?
```

---

# 59. Detection Improvement After Incident

Incident:

```text
Compromised Account
```

Finding:

```text
No detection for MFA manipulation.
```

Improvement:

```text
Create Detection
       ↓
Test
       ↓
Deploy
       ↓
Monitor
```

---

# 60. Logging Improvement

Finding:

```text
Cloud API activity unavailable.
```

Improvement:

```text
Enable Logging
       ↓
Centralize
       ↓
Normalize
       ↓
Create Detection
```

---

# 61. Control Improvement

Incident may reveal:

```text
Weak MFA
Poor Segmentation
Excessive Privileges
Missing EDR
Poor Patch Management
Weak Email Security
```

Response should address systemic weaknesses.

---

# 62. SIEM Metrics

Useful metrics include:

```text
Alert Volume
True Positive Rate
False Positive Rate
MTTD
MTTA
MTTR
Mean Containment Time
Incident Volume
Escalation Rate
Detection Coverage
Data Source Health
```

---

# 63. False Positive Rate

Conceptually:

```text
False Positives
-------------------------
Total Alerts
```

High false positive rates may indicate poor detection tuning.

---

# 64. True Positive Rate

Conceptually:

```text
True Positives
-------------------------
Relevant Detected Cases
```

The exact metric definition should be standardized before operational use.

---

# 65. Alert-to-Incident Conversion

Measure:

```text
Incidents
----------------
Alerts
```

A very high conversion rate may indicate:

```text
Highly selective alerts
```

A very low rate may indicate:

```text
Alert noise
```

But the metric must be interpreted with context.

---

# 66. Mean Time to Detect

Conceptually:

```text
Time of Detection
-
Time Attack Began
```

A lower value generally indicates faster detection.

---

# 67. Mean Time to Respond

Conceptually:

```text
Response Completion
-
Detection / Acknowledgement
```

Organizations should define exactly which timestamps are used.

---

# 68. Mean Time to Contain

Measures:

```text
Containment Time
-
Detection Time
```

Useful for understanding operational response speed.

---

# 69. Incident Severity Distribution

Dashboard:

```text
Critical: 2
High:     10
Medium:   35
Low:      80
```

This can help identify trends.

---

# 70. Incident Trends

Track:

```text
Incidents by Month
Incidents by Category
Incidents by Asset
Incidents by Attack Technique
Incidents by Source
```

Example:

```text
Credential Attacks ↑
Phishing ↓
Malware →
```

This can guide security priorities.

---

# 71. Incident Categories

Common categories:

```text
Malware
Phishing
Account Compromise
Data Exfiltration
Ransomware
Unauthorized Access
Insider Threat
Web Attack
Cloud Compromise
Policy Violation
```

---

# 72. SIEM and SOAR

SIEM:

```text
Collect
Normalize
Detect
Correlate
Search
Alert
```

SOAR:

```text
Orchestrate
Enrich
Automate
Respond
```

Together:

```text
SIEM
 ↓
Detection
 ↓
SOAR
 ↓
Automation
 ↓
Response
```

---

# 73. SOAR Enrichment Example

```text
Alert
 ↓
Lookup IP
 ↓
Lookup User
 ↓
Lookup Host
 ↓
Threat Intelligence
 ↓
MITRE
 ↓
Risk
 ↓
Create Case
```

---

# 74. SOAR Response Example

For a high-confidence malicious endpoint:

```text
SIEM Detection
      ↓
SOAR
      ↓
Validate
      ↓
Notify Analyst
      ↓
Isolate Endpoint
      ↓
Create Case
```

Automated containment should be carefully authorized and tested.

---

# 75. Human Approval

For risky actions:

```text
Detection
 ↓
Automation
 ↓
Evidence
 ↓
Analyst Approval
 ↓
Response
```

Examples:

```text
Account Disablement
Endpoint Isolation
Large-Scale Blocking
Cloud Permission Changes
```

---

# 76. Automation Guardrails

Automations should include:

```text
Confidence Threshold
Scope Limit
Approval
Rollback
Logging
Timeout
Exception Handling
```

---

# 77. Example Guardrail

Instead of:

```text
IF IP is malicious
THEN block everywhere
```

use:

```text
IF

IOC confidence = high
AND
recently observed
AND
internal host connected
AND
not on allowlist

THEN

create high-priority action
for analyst approval
```

---

# 78. Incident Response Documentation

A complete case may include:

```text
Executive Summary
Technical Summary
Timeline
Affected Assets
Affected Users
Attack Techniques
Evidence
Root Cause
Containment
Eradication
Recovery
Lessons Learned
Detection Improvements
```

---

# 79. Executive Summary

Example:

```text
A compromised user account was used to access
two internal systems. The attacker executed
suspicious PowerShell activity and attempted
lateral movement. The affected endpoint was
isolated and credentials were reset. No confirmed
data exfiltration was identified.
```

The executive summary should avoid unnecessary technical detail.

---

# 80. Technical Summary

Include:

```text
Initial Access
Execution
Credential Access
Lateral Movement
Persistence
C2
Data Access
Containment
```

Map relevant behaviors to ATT&CK when useful.

---

# 81. Incident Evidence Table

| Time | Source | Entity | Event | Interpretation |
|---|---|---|---|---|
| 09:45 | Email | Alice | Phishing email | Possible initial access |
| 09:52 | Endpoint | WS-01 | Process execution | Execution |
| 09:55 | DNS | WS-01 | Suspicious domain | Possible C2 |
| 10:02 | Identity | Alice | Remote login | Possible lateral movement |

---

# 82. Incident Handoff

When transferring a case:

```text
Current Status
Known Facts
Unknowns
Actions Taken
Actions Pending
Important Queries
Evidence Location
Recommended Next Steps
```

A good handoff prevents duplicated work.

---

# 83. Shift Handover

SOC teams operating 24/7 should communicate:

```text
Open Incidents
High-Risk Alerts
Pending Actions
Emerging Threats
System Issues
Feed Problems
```

---

# 84. Incident Communication Timeline

Maintain:

```text
Who was informed?
When?
What information?
What decision?
```

This creates accountability.

---

# 85. Third-Party Incidents

If a vendor is involved:

```text
Identify Vendor
Determine Data Exposure
Determine Access
Review Logs
Coordinate Response
Document Communication
```

Do not assume the third party has complete evidence.

---

# 86. Cloud Incident Response

Cloud incidents may require:

```text
Revoke Sessions
Rotate Access Keys
Review IAM
Review API Calls
Review Resource Changes
Review CloudTrail/Equivalent Logs
Check Persistence
```

The exact controls depend on the cloud provider.

---

# 87. Identity Incident Response

For account compromise:

```text
Disable / Restrict Account
Revoke Sessions
Reset Credentials
Reset MFA if compromised
Review Privileges
Review Recent Activity
Check Other Accounts
```

Carefully preserve evidence before destructive changes where appropriate.

---

# 88. Endpoint Incident Response

Typical steps:

```text
Identify Host
 ↓
Collect Evidence
 ↓
Isolate
 ↓
Analyze
 ↓
Remove Threat
 ↓
Patch
 ↓
Restore
 ↓
Monitor
```

---

# 89. Network Incident Response

Typical steps:

```text
Identify Source
 ↓
Identify Destination
 ↓
Determine Protocol
 ↓
Check Threat Intelligence
 ↓
Scope Other Connections
 ↓
Block / Segment if Authorized
 ↓
Monitor
```

---

# 90. Data Incident Response

For possible data exposure:

```text
Identify Data
 ↓
Identify Users
 ↓
Identify Systems
 ↓
Determine Volume
 ↓
Determine Destination
 ↓
Determine Exposure
 ↓
Escalate
```

Legal/privacy teams may need to be involved depending on the organization and jurisdiction.

---

# 91. Practical Lab – Full Incident

Create the following simulated timeline:

```text
09:30
Phishing Email

09:35
User Click

09:36
File Download

09:37
PowerShell

09:40
DNS Query

09:41
Outbound Connection

09:45
Credential Access

09:50
Remote Login

09:55
SIEM Alert
```

Build:

```text
Timeline
+
ATT&CK Mapping
+
Risk Score
+
Scope
+
Incident Classification
```

---

# 92. Practical Lab – Containment

Given:

```text
Compromised Endpoint
```

identify possible containment actions:

```text
Endpoint Isolation
Credential Reset
Session Revocation
Network Blocking
```

Then identify:

```text
Which actions are immediate?

Which require approval?

What evidence should be preserved first?
```

---

# 93. Practical Lab – Detection Improvement

Incident finding:

```text
Attack succeeded because
MFA changes were not monitored.
```

Build:

```text
Detection:
MFA Configuration Change

Context:
Privileged Account

Correlation:
Login + MFA Change + Sensitive Action

Risk:
High
```

---

# 94. Practical Lab – Incident Report

Create:

```text
Incident ID
Title
Severity
Executive Summary
Technical Summary
Timeline
Affected Assets
Affected Users
ATT&CK Mapping
Evidence
Root Cause
Containment
Eradication
Recovery
Lessons Learned
Detection Improvements
```

---

# 95. Interview Questions

### What is incident response?

> The structured process of detecting, analyzing, containing, eradicating, and recovering from security incidents.

### What are the major incident-response phases?

> Preparation, detection and analysis, containment, eradication, recovery, and post-incident activity.

### What is the difference between an alert and an incident?

> An alert is a security detection requiring evaluation; an incident is a confirmed or strongly suspected security event requiring coordinated response.

### What is containment?

> Actions taken to limit attacker access, spread, or damage.

### What is eradication?

> Removing the underlying threat, persistence, compromised credentials, malware, or vulnerability.

### What is recovery?

> Restoring systems and services to a secure operational state while validating that the threat has been removed.

### What is root-cause analysis?

> Determining how the incident began and identifying the underlying weaknesses that enabled it.

### What is MTTD?

> Mean Time To Detect, measuring the time between the beginning or occurrence of relevant malicious activity and its detection, based on the organization's defined timestamps.

### What is MTTR?

> Mean Time To Respond or Recover, depending on the organization's metric definition.

### How does SIEM support incident response?

> SIEM provides centralized telemetry, correlation, detections, alerts, historical search, enrichment, timelines, and evidence that support investigation and response.

### How does SOAR complement SIEM?

> SOAR automates enrichment, orchestration, case management, and approved response actions around SIEM detections.

### What should an analyst do after receiving a high-severity alert?

> Validate the alert, understand the detection, identify entities, search related events, build a timeline, determine scope and impact, enrich the evidence, and escalate or initiate response according to procedure.

### What is a playbook?

> A documented sequence of investigation and response steps for a specific incident type.

### Why is incident documentation important?

> It provides an auditable record, supports handoffs, enables lessons learned, and helps improve security controls and detections.

---

# 96. Quick Revision

```text
INCIDENT RESPONSE
→ Structured handling of security incidents

PREPARATION
→ Build capabilities before incidents

DETECTION
→ Identify suspicious activity

TRIAGE
→ Validate and prioritize

INVESTIGATION
→ Establish facts and scope

CONTAINMENT
→ Limit damage

ERADICATION
→ Remove the threat

RECOVERY
→ Restore secure operations

POST-INCIDENT
→ Learn and improve

CASE
→ Central incident record

PLAYBOOK
→ Repeatable response procedure

MTTD
→ Time to detect

MTTA
→ Time to acknowledge

MTTR
→ Time to respond/recover depending on definition

SOAR
→ Automation and orchestration
```

---

# 97. Golden Rules

```text
1. Not every alert is an incident.

2. Validate before responding.

3. Preserve important evidence.

4. Determine scope early.

5. Build a timeline.

6. Identify root cause.

7. Containment limits damage.

8. Eradication removes the underlying threat.

9. Recovery restores secure operations.

10. Fix the root cause, not only the symptom.

11. Document important decisions.

12. Define clear incident ownership.

13. Escalate based on severity and impact.

14. Automate repetitive tasks carefully.

15. Keep humans involved in high-risk decisions where appropriate.

16. Monitor for re-compromise after recovery.

17. Turn incident findings into detection improvements.

18. Turn detection gaps into logging or engineering requirements.

19. Measure response performance consistently.

20. Every serious incident should produce lessons that improve the SOC.
```

---

# 98. Final Mental Model

The complete SIEM-driven incident-response workflow is:

```text
                  TELEMETRY
                      ↓
                  DETECTION
                      ↓
                    ALERT
                      ↓
                   TRIAGE
                      ↓
                INVESTIGATION
                      ↓
                 CORRELATION
                      ↓
                    SCOPE
                      ↓
               INCIDENT DECLARED
                      ↓
                 CONTAINMENT
                      ↓
                 ERADICATION
                      ↓
                   RECOVERY
                      ↓
              POST-INCIDENT REVIEW
                      ↓
              DETECTION IMPROVEMENT
                      ↓
                BETTER DEFENSE
```

A mature SOC continuously cycles through:

```text
DETECT
  ↓
INVESTIGATE
  ↓
RESPOND
  ↓
LEARN
  ↓
IMPROVE
  ↓
DETECT BETTER
```

---

# 99. Chapter Summary

Incident response transforms security detections into coordinated action.

The core workflow is:

```text
PREPARE
   ↓
DETECT
   ↓
TRIAGE
   ↓
INVESTIGATE
   ↓
CONTAIN
   ↓
ERADICATE
   ↓
RECOVER
   ↓
LEARN
```

The SIEM supports this lifecycle by providing:

```text
Centralized Telemetry
       +
Detection
       +
Correlation
       +
Threat Intelligence
       +
Historical Search
       +
Investigation
       +
Alerting
       +
Case Context
```

The most important principle is:

> **Incident response is not simply about stopping an attack. It is about understanding what happened, limiting damage, removing the underlying cause, restoring secure operations, and improving defenses so the same attack is harder to repeat.**

The next chapter moves into practical detection content:

```text
Chapter 12 – SIEM Use Cases & Detection Scenarios
```

There we will cover **high-value SOC use cases, authentication attacks, brute force, password spraying, account compromise, malware, phishing, PowerShell, privilege escalation, lateral movement, C2, data exfiltration, ransomware, insider threats, cloud attacks, and complete detection-to-response scenarios.**
```