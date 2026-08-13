# Chapter 07 – Correlation Rules, Risk Scoring & Alerting

> Individual security events often provide incomplete evidence. Correlation connects related events, risk scoring prioritizes their significance, and alerting converts meaningful detections into actionable SOC work.

---

# 1. Introduction

A single event may not be enough to determine whether an attack is occurring.

For example:

```text
Successful Login
```

could be completely normal.

But:

```text
Failed Login
      ↓
Successful Login
      ↓
New MFA Configuration
      ↓
Privilege Change
      ↓
Sensitive Data Access
```

tells a very different story.

This is the purpose of:

```text
Correlation
+
Risk Scoring
+
Alerting
```

The overall workflow is:

```text
Raw Events
    ↓
Individual Detections
    ↓
Correlation
    ↓
Risk Evaluation
    ↓
Alert Prioritization
    ↓
Alert
    ↓
Triage
    ↓
Investigation
    ↓
Response
```

---

# 2. What is Event Correlation?

Event correlation is the process of identifying relationships between multiple events based on:

```text
Time
User
Host
IP
Process
Application
Resource
Sequence
Behavior
Threat Intelligence
```

Example:

```text
Event A:
Failed Login

Event B:
Successful Login

Event C:
Privilege Change
```

Correlation:

```text
A + B + C
   ↓
Potential Account Compromise
```

---

# 3. Why Correlation Matters

Attackers rarely perform only one action.

A typical attack may involve:

```text
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Exfiltration
```

Individual events may appear harmless.

Correlation can reveal the broader attack chain.

---

# 4. Event vs Signal vs Alert

These terms should be distinguished.

### Event

A raw or normalized security record.

```text
Successful Login
```

### Signal / Detection Result

A security condition identified by a rule.

```text
Unusual Login Detected
```

### Alert

An operational security notification requiring attention.

```text
Possible Account Compromise
```

Conceptually:

```text
Events
  ↓
Detection Signals
  ↓
Correlation
  ↓
Alert
```

---

# 5. Simple Correlation

The simplest correlation is:

```text
Event A
+
Event B
```

Example:

```text
Failed Login
+
Successful Login
```

within:

```text
5 minutes
```

---

# 6. Multi-Event Correlation

More advanced:

```text
Failed Login
    ↓
Successful Login
    ↓
Suspicious Process
    ↓
External Connection
```

Potential conclusion:

```text
Possible Account Compromise
```

---

# 7. Correlation Dimensions

Events can be correlated using:

```text
Same User
Same Host
Same IP
Same Process
Same Session
Same Account
Same Destination
Same File
Same Cloud Resource
Same Incident
```

---

# 8. Correlation by User

Example:

```text
user.name = alice
```

Events:

```text
Login
Password Change
Privilege Change
File Access
```

Correlation:

```text
Alice's Activity
```

---

# 9. Correlation by Host

Example:

```text
host.name = WEB01
```

Events:

```text
Process Creation
DNS Query
Network Connection
File Creation
Authentication
```

This creates a host activity timeline.

---

# 10. Correlation by Source IP

Example:

```text
source.ip = 10.10.10.20
```

Events:

```text
Failed Login
VPN Login
Web Request
DNS Query
Port Scan
```

This can reveal relationships across multiple systems.

---

# 11. Correlation by Process

Example:

```text
process.pid = 1234
```

Events:

```text
Process Creation
Child Process
Network Connection
File Creation
```

This is useful for endpoint investigations.

---

# 12. Correlation by Session

A session identifier can connect:

```text
Login
API Requests
Privilege Changes
Logout
```

This is particularly useful for:

```text
Web Applications
Cloud Services
Identity Systems
Remote Access
```

---

# 13. Temporal Correlation

Temporal correlation connects events based on time.

Example:

```text
Event A:
10:00:01

Event B:
10:00:30

Event C:
10:02:10
```

Rule:

```text
All events within 5 minutes
```

---

# 14. Time Window

A correlation rule may specify:

```text
5 minutes
10 minutes
30 minutes
1 hour
24 hours
```

The correct window depends on the behavior.

---

# 15. Short vs Long Windows

### Short Window

Useful for:

```text
Brute Force
Scanning
Rapid Exploitation
Credential Abuse
```

### Long Window

Useful for:

```text
Persistence
Slow Reconnaissance
Periodic Beaconing
Long-Term Account Abuse
```

---

# 16. Sequence Correlation

Sequence correlation requires events in a specific order.

Example:

```text
1. Authentication Failure
2. Authentication Success
3. Privilege Change
```

The order matters.

---

# 17. Ordered vs Unordered Correlation

### Ordered

```text
A → B → C
```

must occur in that order.

### Unordered

```text
A + B + C
```

must all occur within a window, but order may not matter.

Use ordered correlation when attack progression is important.

---

# 18. Threshold Correlation

Example:

```text
>20 failed logins
FROM
same source IP
WITHIN
5 minutes
```

This detects a volume pattern.

---

# 19. Unique Entity Correlation

Example:

```text
One IP
+
10 unique users
+
authentication failures
```

This is more informative than:

```text
20 failures
```

because it can identify password spraying.

---

# 20. Count vs Unique Count

Example:

```text
100 failures
```

may represent:

```text
1 user × 100 attempts
```

or:

```text
50 users × 2 attempts
```

These are different behaviors.

Therefore:

```text
COUNT
+
COUNT DISTINCT
```

can be important.

---

# 21. Aggregation Correlation

Example:

```text
GROUP BY source.ip
```

Calculate:

```text
failure_count
unique_users
unique_hosts
```

Then evaluate:

```text
failure_count > 20
AND
unique_users > 5
```

---

# 22. Cross-Source Correlation

One of the strongest SIEM capabilities is connecting multiple data sources.

Example:

```text
Identity
   ↓
Successful Login

Endpoint
   ↓
PowerShell

Network
   ↓
Suspicious Connection

DNS
   ↓
Malicious Domain
```

Correlation:

```text
Potential Compromise
```

---

# 23. Cross-Layer Correlation

Example:

```text
Identity Layer
       ↓
Compromised Account

Endpoint Layer
       ↓
Suspicious Execution

Network Layer
       ↓
C2 Connection

Data Layer
       ↓
Sensitive Access
```

This creates a broader incident picture.

---

# 24. Correlation Rule Example

```text
IF

authentication success
AND
new privileged group membership
AND
suspicious process execution

FROM

same user

WITHIN

15 minutes

THEN

generate high-risk signal
```

---

# 25. Negative Conditions

Correlation can include things that should NOT happen.

Example:

```text
Successful Login
+
Admin Action
+
NO MFA Event
```

Potentially suspicious depending on the environment.

Negative conditions require careful validation because missing telemetry can look like absence of an event.

---

# 26. Absence-Based Detection

Sometimes the interesting condition is:

```text
Expected event did not occur.
```

Example:

```text
Privileged Login
BUT
No MFA event
```

This requires confidence that MFA logs are complete.

---

# 27. Sequence Example – Account Compromise

```text
Failed Login
      ↓
Successful Login
      ↓
MFA Change
      ↓
New Session
      ↓
Admin Action
```

Correlation:

```text
Potential Account Takeover
```

---

# 28. Sequence Example – Malware Execution

```text
Email Attachment
      ↓
Office Process
      ↓
PowerShell
      ↓
File Drop
      ↓
External Connection
```

Potential conclusion:

```text
Possible Malware Execution
```

---

# 29. Sequence Example – Lateral Movement

```text
Compromised Host
      ↓
Credential Use
      ↓
Remote Authentication
      ↓
Remote Process
      ↓
New Host Access
```

Potential conclusion:

```text
Possible Lateral Movement
```

---

# 30. Sequence Example – Data Exfiltration

```text
Unusual Login
      ↓
Sensitive File Access
      ↓
Archive Creation
      ↓
Large Outbound Transfer
```

Potential conclusion:

```text
Possible Data Exfiltration
```

---

# 31. Correlation Across Entities

An attack may change:

```text
IP
User
Host
Process
```

but relationships still exist.

Example:

```text
User Alice
   ↓
Host A
   ↓
Process P
   ↓
IP X
```

The SIEM can correlate these relationships.

---

# 32. Entity Graph

Conceptually:

```text
             User
              │
              ▼
             Host
              │
              ▼
           Process
              │
              ▼
              IP
              │
              ▼
            Domain
```

Graph-based investigation can reveal relationships that simple event searches may miss.

---

# 33. Risk Scoring

Risk scoring assigns numerical values to security signals.

Example:

```text
Suspicious Login       +20
Malicious IP            +40
Privilege Change        +50
Critical Asset          +30
```

Total:

```text
140
```

---

# 34. Why Risk Scoring?

A SOC may receive:

```text
1,000 alerts/day
```

Risk scoring helps answer:

```text
Which should analysts investigate first?
```

---

# 35. Risk vs Severity

These are not identical.

### Severity

Potential impact of a particular alert.

### Risk

Combined assessment of multiple factors affecting an entity or situation.

Example:

```text
Low-severity suspicious login
+
Critical server
+
Privileged account
+
Malicious IP
```

may produce:

```text
High overall risk
```

---

# 36. Risk Factors

Risk may consider:

```text
Alert Severity
Detection Confidence
Asset Criticality
User Privilege
Threat Intelligence
Historical Behavior
Number of Related Alerts
Attack Technique
Business Context
```

---

# 37. Example Risk Model

```text
Risk =
Detection Score
+
Asset Criticality
+
User Privilege
+
Threat Intelligence
+
Behavioral Anomaly
```

The actual formula varies by organization.

---

# 38. Risk Score Example

Suppose:

```text
Suspicious Login       = 20
Malicious IP            = 40
Admin Account           = 25
Critical Host           = 30
```

Total:

```text
115
```

Example priority:

```text
0–20     Low
21–50    Medium
51–100   High
101+     Critical
```

These thresholds are illustrative and must be tuned to the organization's environment.

---

# 39. Dynamic Risk

Risk can change over time.

Example:

```text
10:00
Risk = 20

10:05
Suspicious Login
Risk = 40

10:10
Privilege Change
Risk = 80

10:15
Malicious Connection
Risk = 120
```

The entity becomes increasingly suspicious.

---

# 40. Entity Risk Scoring

Risk can be associated with:

```text
User
Host
IP
Application
Cloud Account
Device
```

Example:

```text
User:
alice

Risk:
95
```

---

# 41. Risk Accumulation

Multiple related signals can accumulate.

```text
Event A → +20
Event B → +30
Event C → +40

Total = 90
```

This can reduce dependence on one high-noise detection.

---

# 42. Risk Decay

Old risk may become less relevant over time.

Conceptually:

```text
Risk today:
100

After time:
80

Later:
50

Eventually:
20
```

Risk decay prevents old events from permanently dominating current risk.

---

# 43. Why Risk Decay Matters

Without decay:

```text
One suspicious event
      ↓
Risk remains high forever
```

With decay:

```text
Old event
      ↓
Importance gradually decreases
```

Exact decay rules depend on the platform and organization.

---

# 44. Alert Generation

A correlation engine may produce:

```text
Signal
```

Then alert logic determines:

```text
Should an analyst be notified?
```

Not every signal needs to become a separate alert.

---

# 45. Signal vs Alert

Example:

```text
100 suspicious login signals
```

could become:

```text
1 grouped alert
```

This reduces noise.

---

# 46. Alert Deduplication

If the same event repeatedly triggers:

```text
Alert
Alert
Alert
Alert
```

the SIEM may suppress duplicates.

Example:

```text
Same rule
Same user
Same host
Same condition
Within 10 minutes
```

↓

```text
Group
```

---

# 47. Alert Suppression

Suppression temporarily prevents repeated alerts.

Example:

```text
One alert
per user
per 30 minutes
```

Suppression must be carefully designed because excessive suppression can hide attacks.

---

# 48. Alert Grouping

Related alerts can be grouped:

```text
User:
alice

Alerts:
Suspicious Login
PowerShell
Privilege Change
Malicious DNS
```

↓

```text
Potential Account Compromise
```

---

# 49. Alert Prioritization

A SOC can prioritize using:

```text
Severity
Risk
Confidence
Asset Criticality
User Privilege
Threat Intelligence
Attack Stage
```

---

# 50. Alert Severity Matrix

Conceptually:

```text
                 CONFIDENCE
              Low    Med    High
Severity
Low            Low    Low    Med
Medium         Low    Med    High
High           Med    High   Critical
Critical       High   Critical Critical
```

This is illustrative rather than universal.

---

# 51. Alert Context

A useful alert should contain:

```text
What happened?
When?
Who?
Where?
Why suspicious?
Which detection?
Which entities?
What evidence?
What ATT&CK technique?
What should the analyst investigate?
```

---

# 52. Poor Alert

```text
Title:
Suspicious Activity

Description:
A suspicious event occurred.
```

Not useful.

---

# 53. Good Alert

```text
Title:
Possible Password Spraying Attack

Source:
203.0.113.10

Target Users:
27

Failed Attempts:
86

Window:
8 minutes

Affected Service:
VPN

Detection:
DET-AUTH-005

Risk:
82

MITRE:
Credential Access

Reason:
One external source generated
authentication failures against
many accounts.
```

This is much more actionable.

---

# 54. Alert Enrichment

Useful enrichment:

```text
Threat Intelligence
Asset Criticality
User Role
GeoIP
Previous Alerts
Known Vulnerabilities
MITRE ATT&CK
Related Hosts
Related Users
```

---

# 55. Alert Routing

Different alerts can be routed differently.

```text
Critical
   ↓
Immediate SOC Escalation

High
   ↓
SOC Queue

Medium
   ↓
Standard Investigation

Low
   ↓
Dashboard / Review
```

---

# 56. Escalation

Escalation can be based on:

```text
Severity
Risk
Time Open
Asset Criticality
User Privilege
Business Impact
```

---

# 57. Alert Ownership

Every important alert should have a clear workflow:

```text
Generated
   ↓
Assigned
   ↓
Acknowledged
   ↓
Investigated
   ↓
Resolved
```

---

# 58. Alert SLA

Organizations may define response targets.

Example:

```text
Critical:
Immediate

High:
15 minutes

Medium:
1 hour

Low:
Business day
```

Actual SLAs depend on organizational requirements.

---

# 59. Alert Lifecycle

```text
NEW
 ↓
ASSIGNED
 ↓
ACKNOWLEDGED
 ↓
INVESTIGATING
 ↓
TRUE POSITIVE / FALSE POSITIVE
 ↓
ESCALATED / RESOLVED
 ↓
CLOSED
```

---

# 60. False Positive Management

When an alert is benign:

```text
Identify Reason
      ↓
Document
      ↓
Determine Pattern
      ↓
Tune Detection
```

Avoid immediately suppressing the alert without understanding why it fired.

---

# 61. Alert Fatigue

Alert fatigue occurs when analysts receive too many low-value alerts.

Symptoms:

```text
Alerts Ignored
Slow Triage
Missed Important Events
Analyst Burnout
```

---

# 62. Reducing Alert Fatigue

Use:

```text
Better Detection Logic
Correlation
Risk Scoring
Deduplication
Suppression
Alert Grouping
Context Enrichment
Prioritization
```

---

# 63. Correlation and Alert Fatigue

Without correlation:

```text
Failed Login
→ Alert

Successful Login
→ Alert

PowerShell
→ Alert

Network Connection
→ Alert
```

Potentially:

```text
4 separate alerts
```

With correlation:

```text
Possible Account Compromise
→ 1 higher-context alert
```

---

# 64. Alert Storms

An alert storm occurs when an abnormal condition causes huge alert volumes.

Example:

```text
Identity Provider Failure
       ↓
100,000 Login Failures
       ↓
100,000 Alerts
```

This can overwhelm the SOC.

---

# 65. Alert Storm Protection

Use:

```text
Rate Limiting
Grouping
Deduplication
Suppression
Thresholds
Circuit Breakers
Prioritization
```

But ensure critical signals remain visible.

---

# 66. Circuit Breaker Concept

If alert volume becomes extreme:

```text
Normal:
100 alerts/min

Abnormal:
100,000 alerts/min
```

The system may temporarily:

```text
Group
Throttle
Suppress duplicates
```

while preserving evidence and high-priority signals.

---

# 67. Correlation Rule Dependencies

A correlation rule may depend on:

```text
Identity Logs
Endpoint Logs
Network Logs
Threat Intelligence
Asset Data
```

If one source stops sending data:

```text
Correlation confidence ↓
```

---

# 68. Data Completeness

Correlation assumes data is available.

Example:

```text
Login Event
+
MFA Event
```

If MFA logs are missing:

```text
"No MFA"
```

does not necessarily mean:

```text
"MFA was not performed."
```

It may mean:

```text
MFA telemetry unavailable.
```

---

# 69. Correlation Pitfalls

Common problems:

```text
Incorrect Time Windows
Missing Data
Duplicate Events
Clock Drift
Incorrect Entity Mapping
Overly Broad Correlation
Overly Narrow Correlation
High Computational Cost
```

---

# 70. Entity Resolution

Suppose:

```text
Alice
alice@example.com
CORP\alice
```

all represent the same person.

If identity resolution fails:

```text
Correlation breaks
```

Therefore identity normalization is critical.

---

# 71. Correlation and Clock Synchronization

Example:

```text
Event A:
10:00:00

Event B:
09:59:30
```

If clocks are inaccurate, the sequence may appear incorrect.

Use:

```text
NTP
UTC
Reliable Timestamping
```

where appropriate.

---

# 72. Sliding Window Correlation

Example:

```text
Current Time
      ↓
┌───────────────────┐
│ Last 10 Minutes   │
└───────────────────┘
```

Events continuously enter and leave the window.

Useful for:

```text
Brute Force
Scanning
Network Abuse
Rate-Based Attacks
```

---

# 73. Tumbling Window

A tumbling window divides time into fixed non-overlapping intervals.

Example:

```text
10:00–10:05
10:05–10:10
10:10–10:15
```

Each event belongs to one window.

---

# 74. Sliding vs Tumbling

### Sliding

```text
10:00–10:05
10:01–10:06
10:02–10:07
```

### Tumbling

```text
10:00–10:05
10:05–10:10
10:10–10:15
```

Sliding windows provide more continuous analysis but can require more processing.

---

# 75. Sequence with Time Constraints

Example:

```text
A
 ↓
within 5 min
 ↓
B
 ↓
within 10 min
 ↓
C
```

This can represent:

```text
Login
→ Privilege Change
→ Data Access
```

---

# 76. Correlation Example – Brute Force

```text
Authentication Failures
       ↓
Group by source.ip
       ↓
Count failures
       ↓
Threshold > 20
       ↓
5-minute window
       ↓
Alert
```

---

# 77. Correlation Example – Password Spraying

```text
Authentication Failures
       ↓
Group by source.ip
       ↓
Unique user count
       ↓
> 10 users
       ↓
5-minute window
       ↓
Alert
```

---

# 78. Correlation Example – Account Takeover

```text
Unusual Login
       +
MFA Change
       +
New Device
       +
Sensitive Action
```

↓

```text
High Risk
```

---

# 79. Correlation Example – Endpoint Compromise

```text
Office Process
      ↓
PowerShell
      ↓
File Creation
      ↓
Network Connection
```

↓

```text
Possible Malware Execution
```

---

# 80. Correlation Example – Lateral Movement

```text
Credential Use
      ↓
Remote Authentication
      ↓
Remote Service
      ↓
New Host
```

↓

```text
Possible Lateral Movement
```

---

# 81. Correlation Example – Exfiltration

```text
Sensitive File Access
      ↓
Archive Creation
      ↓
Large Outbound Transfer
      ↓
Rare Destination
```

↓

```text
Possible Exfiltration
```

---

# 82. Risk Scoring Example

```text
Detection:
Suspicious Login
Score = 20

Threat Intelligence:
Malicious IP
Score = 40

Identity:
Privileged User
Score = 30

Asset:
Critical Server
Score = 40

Total:
130
```

Potential priority:

```text
Critical
```

Again, thresholds are organization-specific.

---

# 83. Risk Aggregation

Risk can be calculated:

```text
Per Event
Per Alert
Per User
Per Host
Per IP
Per Incident
```

Entity-level scoring is particularly useful for identifying accounts or systems accumulating suspicious signals.

---

# 84. Risk Normalization

Different detections may produce different scores.

Example:

```text
Detection A = 10
Detection B = 90
Detection C = 40
```

Normalize scores into a consistent scale if necessary:

```text
0–100
```

This makes prioritization easier.

---

# 85. Risk Explainability

Analysts should understand:

```text
Why is risk 90?
```

Example:

```text
+30 Privilege Change
+25 Malicious IP
+20 Unusual Login
+15 Critical Asset
```

This is more useful than:

```text
Risk = 90
```

without explanation.

---

# 86. Risk Score Manipulation

Attackers may attempt to:

```text
Trigger low-risk behavior
Avoid high-risk behavior
Blend into normal activity
Compromise trusted infrastructure
```

Risk scoring should therefore not become the only detection mechanism.

---

# 87. Correlation Rule Maintenance

Review:

```text
Data Sources
Thresholds
Time Windows
Entity Mapping
False Positives
Performance
Threat Relevance
```

---

# 88. Correlation Performance

Complex correlation across:

```text
Large Time Windows
Many Fields
Multiple Data Sources
High Event Volumes
```

can be expensive.

Optimize by:

```text
Filtering Early
Using Structured Fields
Limiting Time Windows
Pre-Aggregating Data
Using Efficient Indexes
```

---

# 89. Alert Enrichment Workflow

```text
Detection
   ↓
Correlation
   ↓
Risk Score
   ↓
Asset Lookup
   ↓
Identity Lookup
   ↓
Threat Intelligence
   ↓
MITRE Mapping
   ↓
Alert
```

This creates an analyst-ready alert.

---

# 90. Alert Quality

A high-quality alert should be:

```text
Relevant
Actionable
Understandable
Prioritized
Context-Rich
Traceable
```

---

# 91. Alert Quality Questions

Ask:

```text
Can the analyst understand it quickly?

Can the analyst reproduce the evidence?

Does it identify affected entities?

Does it explain why it triggered?

Does it provide useful context?

Does it suggest investigation steps?
```

---

# 92. Alert vs Incident

Not every alert is an incident.

Example:

```text
Alert:
Suspicious Login
```

After investigation:

```text
Legitimate VPN Login
```

No incident.

Another:

```text
Alert:
Suspicious Login

+
Privilege Change
+
Malicious Process
```

↓

```text
Potential Incident
```

---

# 93. Alert-to-Incident Promotion

Conceptually:

```text
Alert
 ↓
Triage
 ↓
Evidence
 ↓
Confirmed Malicious
 ↓
Incident
```

---

# 94. Correlation and MITRE ATT&CK

Correlation can connect behaviors across attack techniques.

Example:

```text
Credential Access
       ↓
Execution
       ↓
Persistence
       ↓
Lateral Movement
```

Mapping correlated activity to ATT&CK can provide an attack-path perspective.

Detailed ATT&CK methodology will be covered in:

```text
Chapter 09
MITRE ATT&CK & Threat-Based Detection
```

---

# 95. Correlation Rule Documentation

Document:

```text
Rule ID
Name
Objective
Data Sources
Required Fields
Logic
Time Window
Threshold
Severity
Risk Score
Exceptions
False Positives
MITRE Mapping
Owner
Version
```

---

# 96. Practical Lab

Create a correlation rule:

```text
Failed Login
+
Successful Login
+
Privilege Change
```

Requirements:

```text
Same User
Within 15 Minutes
```

Then assign:

```text
Risk:
80
```

Generate:

```text
Alert:
Possible Account Compromise
```

---

# 97. Practical Risk Exercise

Create these signals:

```text
Unusual Login       +20
Malicious IP        +40
Admin Account       +25
Critical Server     +30
```

Calculate:

```text
Total Risk = 115
```

Then determine the alert priority using your organization's defined thresholds.

---

# 98. Practical Alert Grouping Exercise

Generate:

```text
20 identical alerts
for same host
within 5 minutes
```

Group them into:

```text
1 Alert
+
20 Related Events
```

Verify that:

```text
Evidence remains available
```

even though duplicate notifications are reduced.

---

# 99. Practical Investigation Exercise

Create:

```text
User:
alice
```

Events:

```text
09:00 Failed Login
09:01 Failed Login
09:02 Successful Login
09:03 MFA Change
09:05 PowerShell
09:07 Network Connection
09:10 Admin Group Change
```

Build:

```text
Timeline
+
Correlation
+
Risk Score
+
Alert
```

---

# 100. Interview Questions

### What is event correlation?

> Connecting multiple related events using attributes such as time, user, host, IP, process, or sequence to identify higher-level security behavior.

### Why is correlation useful?

> It provides context and can identify attacks that individual events cannot reliably reveal.

### What is temporal correlation?

> Correlating events that occur within a defined time window.

### What is sequence correlation?

> Detecting events occurring in a meaningful order.

### What is threshold correlation?

> Triggering when an event count or metric crosses a defined threshold within a time window.

### What is risk scoring?

> Assigning a numerical or categorical risk value based on security signals and contextual factors.

### What is the difference between severity and risk?

> Severity describes the potential impact or urgency of an alert, while risk can combine multiple signals and contextual factors to represent overall concern.

### What is alert deduplication?

> Combining or suppressing duplicate alerts representing the same underlying activity.

### What is alert suppression?

> Temporarily preventing repeated notifications that meet defined suppression conditions.

### What is alert grouping?

> Combining related signals or alerts into a higher-level investigation unit.

### What is alert fatigue?

> Analyst overload caused by excessive low-value or repetitive alerts.

### How do you reduce alert fatigue?

> Improve detection precision, correlate related events, enrich alerts, deduplicate, group, suppress carefully, and prioritize by risk.

### What is a sliding window?

> A continuously moving time interval used to evaluate recent events.

### What is a tumbling window?

> A set of fixed, non-overlapping time intervals used for aggregation.

### What is risk accumulation?

> Increasing an entity's risk based on multiple related security signals.

### What is risk decay?

> Gradually reducing the influence of older risk signals over time.

### Why should risk scoring be explainable?

> Analysts need to understand why an entity received its score so they can validate and investigate it efficiently.

### What is an alert storm?

> A sudden, extremely high volume of alerts that can overwhelm SOC operations.

### What is the difference between an alert and an incident?

> An alert is a security signal requiring evaluation; an incident is a confirmed or strongly suspected security event requiring formal response.

---

# 101. Quick Revision

```text
CORRELATION
→ Connect related events

TEMPORAL CORRELATION
→ Connect by time

SEQUENCE
→ Connect ordered events

THRESHOLD
→ Trigger after a count/rate threshold

ENTITY CORRELATION
→ Connect by user, host, IP, process, etc.

CROSS-SOURCE CORRELATION
→ Connect identity, endpoint, network, cloud, etc.

RISK SCORING
→ Quantify security concern

RISK ACCUMULATION
→ Combine multiple signals

RISK DECAY
→ Reduce influence of old signals

ALERT GROUPING
→ Combine related alerts

DEDUPLICATION
→ Reduce duplicate notifications

SUPPRESSION
→ Temporarily prevent repeated alerts

ALERT PRIORITIZATION
→ Determine what analysts investigate first

ALERT ENRICHMENT
→ Add useful context

ALERT FATIGUE
→ Excessive low-value alerts

ALERT STORM
→ Extreme alert volume
```

---

# 102. Golden Rules

```text
1. A single event rarely tells the whole story.

2. Correlation provides context.

3. Use the correct entity for correlation.

4. Time windows must match the behavior.

5. Sequence order matters when attack progression matters.

6. Count and unique count represent different behaviors.

7. Missing telemetry is not proof that an event did not occur.

8. Correlation should account for duplicates and delayed events.

9. Risk should be explainable.

10. Severity and risk are not identical.

11. Old risk may need decay.

12. Not every detection signal needs to become an individual alert.

13. Group related alerts whenever appropriate.

14. Suppression must not create dangerous blind spots.

15. Alert enrichment should reduce analyst investigation time.

16. Protect against alert storms.

17. Monitor correlation performance.

18. Monitor data dependencies.

19. Every important alert should have clear ownership and workflow.

20. The goal of correlation is not more alerts—it is higher-confidence, more actionable security intelligence.
```

---

# 103. Final Mental Model

Think of SIEM correlation as:

```text
             INDIVIDUAL EVENTS
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    Identity     Endpoint     Network
        │           │           │
        └───────────┼───────────┘
                    ▼
                CORRELATION
                    │
                    ▼
              MULTI-EVENT SIGNAL
                    │
                    ▼
                RISK SCORE
                    │
                    ▼
              PRIORITIZATION
                    │
                    ▼
                  ALERT
                    │
                    ▼
                TRIAGE
                    │
                    ▼
              INVESTIGATION
                    │
                    ▼
                RESPONSE
```

---

# 104. Chapter Summary

Correlation, risk scoring, and alerting transform individual security signals into actionable SOC intelligence.

The complete workflow is:

```text
EVENTS
  ↓
DETECTIONS
  ↓
CORRELATION
  ↓
CONTEXT
  ↓
RISK
  ↓
PRIORITIZATION
  ↓
ALERT
  ↓
TRIAGE
  ↓
INVESTIGATION
  ↓
RESPONSE
```

The key principle is:

> **Correlation should increase context and confidence, while risk scoring should help the SOC prioritize limited analyst attention.**

A mature SIEM therefore does not simply generate alerts whenever a rule matches.

It should determine:

```text
Are these events related?
        ↓
How suspicious are they?
        ↓
How important is the affected entity?
        ↓
How confident are we?
        ↓
Should this become an alert?
        ↓
How should the alert be prioritized?
        ↓
What context does the analyst need?
```

This creates a much more effective SOC workflow:

```text
MORE DATA
   ↓
BETTER CORRELATION
   ↓
FEWER BUT BETTER ALERTS
   ↓
FASTER TRIAGE
   ↓
BETTER INVESTIGATION
   ↓
FASTER RESPONSE
```

The next chapter moves from internally generated SIEM signals to external intelligence:

```text
Chapter 08 – Threat Intelligence & IOC Integration
```

There we will cover **threat intelligence fundamentals, IOC types, feeds, enrichment, reputation, confidence, STIX/TAXII, IOC lifecycle, indicator matching, feed quality, false positives, threat-intelligence-driven detections, and practical SIEM integration workflows.**