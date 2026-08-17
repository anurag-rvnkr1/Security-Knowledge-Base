# Chapter 07 – Correlation, Sequence Detection & Risk-Based Detection

> Modern attacks rarely consist of a single suspicious event. Attackers typically generate multiple related signals across identities, endpoints, networks, applications, and cloud infrastructure. Correlation, sequence detection, and risk-based detection combine these signals to identify attack patterns, increase confidence, reduce alert noise, and prioritize the events that matter most.

---

# 1. Introduction

A single security event often provides limited context.

Example:

```text
PowerShell executed
```

This could be:

```text
Legitimate Administration
Automation
Software Deployment
Malicious Activity
```

Now consider:

```text
Suspicious Email
      ↓
Office Process
      ↓
PowerShell
      ↓
External Connection
      ↓
Credential Access
```

The combined sequence provides much stronger evidence.

This is the purpose of:

```text
Correlation
Sequence Detection
Risk-Based Detection
```

---

# 2. What Is Correlation?

**Correlation** is the process of connecting multiple events or signals based on relationships such as:

```text
Time
User
Host
IP
Process
Session
Resource
Application
Account
```

Conceptually:

```text
Event A
   +
Event B
   +
Event C
   ↓
Correlation
   ↓
Higher-Confidence Detection
```

---

# 3. Why Correlation Is Important

Correlation can:

```text
Increase Detection Confidence
Reduce Isolated Alerts
Identify Attack Chains
Connect Multiple Data Sources
Provide Context
Prioritize Investigations
```

Instead of:

```text
100 Individual Alerts
```

a SOC may produce:

```text
1 Potential Compromise
```

with the underlying events attached.

---

# 4. Correlation vs Individual Detection

Individual detection:

```text
Suspicious Login
```

Correlation:

```text
Suspicious Login
+
New Device
+
MFA Change
+
Privilege Change
```

The second approach provides substantially more context.

---

# 5. Correlation Dimensions

Events can be correlated using:

```text
Time
User
Host
IP
Account
Process
Session
Application
Cloud Resource
Transaction
File
```

---

# 6. Time-Based Correlation

Example:

```text
Event A
10:00

Event B
10:02

Event C
10:04
```

If all events occur within:

```text
10 minutes
```

they may be considered related.

---

# 7. Entity-Based Correlation

Example:

```text
Same User
+
Multiple Events
```

or:

```text
Same Host
+
Multiple Events
```

Example:

```text
User: alice

Failed Login
Successful Login
MFA Change
```

---

# 8. Multi-Entity Correlation

Some detections require several entities.

Example:

```text
User
+
Source IP
+
Destination Host
+
Process
```

This can reveal relationships that a single entity cannot.

---

# 9. Correlation Keys

A **correlation key** identifies events that belong to the same activity.

Common keys:

```text
user.id
host.id
source.ip
session.id
process.entity_id
transaction.id
cloud.account.id
```

A poor correlation key can create:

```text
False Correlations
```

or:

```text
Missed Correlations
```

---

# 10. Correlation Window

A correlation rule usually defines a time window.

Example:

```text
Event A
+
Event B
+
Event C

within 15 minutes
```

The window should match the expected attack behavior.

---

# 11. Window Too Short

Example:

```text
5-minute window
```

but the attack takes:

```text
30 minutes
```

Result:

```text
Missed Correlation
```

---

# 12. Window Too Long

Example:

```text
7-day window
```

may correlate unrelated events.

Result:

```text
False Correlation
```

Therefore:

```text
Choose a window based on behavior.
```

---

# 13. Correlation Logic

Conceptual example:

```text
IF

failed_login

AND

successful_login

AND

MFA_change

FOR

same_user

WITHIN

10_minutes

THEN

generate_high_confidence_alert
```

---

# 14. Sequence Detection

Sequence detection is a specialized form of correlation where **event order matters**.

Example:

```text
A
 ↓
B
 ↓
C
```

Instead of:

```text
A + B + C
```

sequence detection asks:

```text
Did A happen before B?
Did B happen before C?
Did all events occur within the expected time?
```

---

# 15. Correlation vs Sequence

### Correlation

```text
A + B + C
```

The exact order may not always matter.

### Sequence

```text
A → B → C
```

The order is part of the detection.

---

# 16. Sequence Example – Account Takeover

```text
Failed Login
      ↓
Successful Login
      ↓
New Device
      ↓
MFA Change
      ↓
Sensitive Resource Access
```

This provides a stronger account takeover hypothesis.

---

# 17. Sequence Example – Endpoint Compromise

```text
Email Attachment
      ↓
Office Application
      ↓
Script Interpreter
      ↓
External Connection
      ↓
Persistence
```

This can indicate a possible compromise chain.

---

# 18. Sequence Example – Lateral Movement

```text
Credential Access
      ↓
New Authentication
      ↓
Remote Service
      ↓
Destination Host
      ↓
Administrative Activity
```

---

# 19. Sequence State Machine

Complex sequences can be represented as states:

```text
[Normal]
   ↓
[Suspicious Login]
   ↓
[New Device]
   ↓
[MFA Change]
   ↓
[Privilege Change]
   ↓
[High Risk]
```

Each event advances the entity to another state.

---

# 20. Stateful Detection

Stateful detection remembers previous events.

Example:

```text
Previous:
Failed Login

Current:
Successful Login
```

The current event becomes more interesting because of historical state.

---

# 21. Stateless Detection

Stateless detection evaluates an event independently.

Example:

```text
Known Malicious Hash
```

No previous event is required.

---

# 22. State Storage

Stateful detection may require:

```text
Recent Events
Entity State
Correlation IDs
Counters
Timestamps
Risk Scores
```

The implementation must manage:

```text
State Expiration
Memory
Concurrency
Ordering
Late Events
```

---

# 23. Late Events

Telemetry may arrive after the actual event time.

Example:

```text
Event A
Occurred: 10:00
Received: 10:05

Event B
Occurred: 10:02
Received: 10:03
```

Detection systems must account for:

```text
Event Time
Processing Time
```

when correlation requires ordering.

---

# 24. Event Ordering

Ordering can be based on:

```text
Event Timestamp
Sequence Number
Session State
Transaction ID
```

Do not blindly assume ingestion order equals event order.

---

# 25. Correlation Across Data Sources

Attack activity may appear across:

```text
Email
Identity
Endpoint
DNS
Network
Cloud
Application
```

Example:

```text
Email
 ↓
Identity
 ↓
Endpoint
 ↓
Network
```

Cross-source correlation is a major capability of mature detection platforms.

---

# 26. Cross-Source Correlation Example

```text
Phishing Email
+
User Login
+
New Device
+
Suspicious Process
+
External C2
```

Potential result:

```text
Account + Endpoint Compromise
```

---

# 27. Correlation Graph

Events can be represented as a graph:

```text
User
 │
 ├── Login
 │
 ├── Device
 │
 └── Process
       │
       └── Network Connection
              │
              └── External Domain
```

Graphs can help analysts understand relationships.

---

# 28. Entity Graph

Example:

```text
Alice
  │
  ├── Laptop-A
  │      │
  │      └── powershell.exe
  │              │
  │              └── malicious.example
  │
  └── Cloud Account
         │
         └── IAM Change
```

This provides a broader incident view.

---

# 29. Correlation Confidence

Each event can contribute confidence.

Example:

```text
Suspicious Login       +20
New Device             +15
Malicious IP           +40
MFA Change             +30
Sensitive Access       +25
```

Total:

```text
130
```

Potentially:

```text
High Confidence
```

---

# 30. Risk-Based Detection

Risk-based detection combines multiple signals into a score.

Concept:

```text
Signal
+
Context
+
History
+
Asset Criticality
+
Identity
+
Threat Intelligence
=
Risk
```

---

# 31. Risk Score

Example:

```text
Malicious IP       +40
Privileged User    +30
Critical Host      +30
New Device         +20
MFA Change         +25
```

Total:

```text
145
```

Then:

```text
IF risk >= 100
THEN high_priority_alert
```

---

# 32. Risk vs Severity

These are different concepts.

### Risk

Represents the combined assessment of a situation.

### Severity

Represents how important the resulting alert is operationally.

Example:

```text
Risk Score:
125

Alert Severity:
High
```

---

# 33. Risk vs Confidence

Also distinguish:

```text
Confidence
```

from:

```text
Risk
```

Confidence:

```text
How strongly does the evidence support
the detection hypothesis?
```

Risk:

```text
How significant is the potential security impact?
```

---

# 34. Example – High Confidence, Low Impact

```text
Known Malware
on Isolated Test VM
```

Confidence:

```text
High
```

Impact:

```text
Low
```

---

# 35. Example – Lower Confidence, High Potential Impact

```text
Suspicious Activity
on Domain Controller
```

Confidence:

```text
Medium
```

Potential impact:

```text
Very High
```

This may still deserve immediate investigation.

---

# 36. Risk Factors

Common factors:

```text
User Privilege
Asset Criticality
Data Sensitivity
Threat Intelligence
Behavior Severity
Historical Risk
Authentication Context
Network Exposure
Vulnerability
Detection Confidence
```

---

# 37. Risk Weighting

A basic model:

```text
Risk =
Σ Signal Weight
```

Example:

```text
Signal A = 20
Signal B = 30
Signal C = 50

Risk = 100
```

More advanced systems can include:

```text
Multipliers
Decay
Context
Caps
Overrides
```

---

# 38. Risk Multipliers

Example:

```text
Base Risk = 40

Privileged Account Multiplier = 1.5

Final Risk = 60
```

Another:

```text
Critical Asset Multiplier = 2

Final Risk = 80
```

Multipliers should be carefully validated.

---

# 39. Risk Caps

Without a cap:

```text
Repeated Low-Risk Events
```

could cause:

```text
Risk = 1000
```

even when the behavior is not highly significant.

A risk cap can prevent uncontrolled score inflation.

---

# 40. Risk Decay

Old signals should often become less influential.

Example:

```text
Day 1:
Risk = 100

Day 2:
Risk = 70

Day 3:
Risk = 40

Day 4:
Risk = 20
```

This prevents historical events from permanently increasing risk.

---

# 41. Risk Decay Model

Conceptually:

```text
Current Risk =
Previous Risk × Decay Factor
+
New Risk
```

Example:

```text
Previous Risk = 100
Decay = 0.5

Remaining = 50
```

Then new events are added.

---

# 42. Risk Aggregation

Multiple detections can contribute to one entity risk:

```text
User Alice
 ├── Login Anomaly       +20
 ├── Malicious IP        +40
 ├── MFA Change          +30
 └── Sensitive Access    +25

Total Risk = 115
```

---

# 43. Entity Risk

Risk can be tracked for:

```text
User
Host
IP
Cloud Account
Application
Resource
```

This creates a broader security context.

---

# 44. User Risk

Example:

```text
Alice

Login Anomaly       +20
Suspicious Device   +20
Privilege Change    +30
Malicious IP        +40

Risk = 110
```

---

# 45. Host Risk

Example:

```text
Server-A

Suspicious Process  +20
C2 Connection        +40
Credential Access    +30
Critical Asset       +20

Risk = 110
```

---

# 46. Risk Propagation

Risk can sometimes move through relationships.

Example:

```text
User
 ↓
Endpoint
 ↓
Server
```

Suspicious behavior on the endpoint may increase the relevance of related activity.

Risk propagation must be carefully designed to avoid uncontrolled escalation.

---

# 47. Correlation Rules

A correlation rule typically contains:

```text
Name
Data Sources
Events
Entities
Time Window
Conditions
Sequence
Threshold
Risk
Severity
Suppression
Exceptions
Response
```

---

# 48. Correlation Rule Template

```text
Name:
Potential Account Takeover

Events:
1. Authentication Failure
2. Successful Authentication
3. New Device
4. MFA Change

Entity:
User

Window:
15 minutes

Conditions:
Same User

Risk:
+25
+30
+20
+30

Threshold:
Risk >= 80

Severity:
High
```

---

# 49. Correlation Threshold

Example:

```text
3 suspicious signals
within 10 minutes
```

or:

```text
Risk >= 100
```

The threshold should be based on testing.

---

# 50. Event Count Correlation

Example:

```text
5 failed logins
+
1 successful login
```

This may be more meaningful than:

```text
1 failed login
```

---

# 51. Unique Entity Correlation

Example:

```text
One Source IP
+
10 Unique Users
+
Authentication Failures
```

Potential:

```text
Password Spray
```

---

# 52. Unique Destination Correlation

Example:

```text
One Host
+
20 External Destinations
+
Short Time Window
```

Potential:

```text
Network Scanning
```

depending on the host's expected role.

---

# 53. Correlation by Session

Example:

```text
Session ID
```

can connect:

```text
Authentication
API Request
Transaction
Privilege Change
```

This can be especially useful for application detection.

---

# 54. Correlation by Process

Use:

```text
process.entity_id
```

to connect:

```text
Process Creation
File Activity
Network Connection
Child Processes
```

This helps build endpoint activity chains.

---

# 55. Correlation by User

Useful for:

```text
Authentication
Cloud Activity
Application Access
Privilege Changes
Data Access
```

---

# 56. Correlation by Host

Useful for:

```text
Process Activity
Network Activity
File Activity
Authentication
Persistence
```

---

# 57. Multi-Stage Attack Detection

Example:

```text
Stage 1:
Phishing

Stage 2:
Execution

Stage 3:
Credential Access

Stage 4:
Lateral Movement

Stage 5:
Collection
```

A mature detection system can correlate multiple stages.

---

# 58. Attack Chain Risk

Example:

```text
Phishing           +20
Execution          +20
Credential Access  +30
Lateral Movement   +40
Critical Asset     +30
```

Total:

```text
140
```

Potential:

```text
Critical Investigation
```

---

# 59. Correlation and MITRE ATT&CK

Correlation can connect multiple ATT&CK techniques.

Example:

```text
Execution
    ↓
Credential Access
    ↓
Discovery
    ↓
Lateral Movement
```

The combined pattern provides stronger evidence of an intrusion.

---

# 60. Correlation and Kill Chain

A simplified model:

```text
Recon
 ↓
Initial Access
 ↓
Execution
 ↓
Persistence
 ↓
Privilege Escalation
 ↓
Credential Access
 ↓
Discovery
 ↓
Lateral Movement
 ↓
Collection
 ↓
Exfiltration
```

Detections can be correlated across stages.

---

# 61. Correlation and Detection Confidence

Suppose:

```text
Signal A:
Low confidence

Signal B:
Low confidence

Signal C:
Medium confidence
```

Together:

```text
Potentially High Confidence
```

provided the signals are logically related.

---

# 62. Avoid Naive Signal Addition

Do not assume:

```text
3 signals = 3 × confidence
```

because signals may be:

```text
Correlated
Duplicate
Dependent
Redundant
```

---

# 63. Duplicate Evidence

Example:

```text
EDR Alert
+
SIEM Alert
```

Both may represent:

```text
Same Underlying Event
```

Counting both as independent evidence can artificially inflate risk.

---

# 64. Evidence Independence

Stronger correlation often comes from partially independent evidence.

Example:

```text
Endpoint
+
Identity
+
Network
```

can provide more confidence than:

```text
Three Alerts
from the Same Sensor
```

---

# 65. Correlation Quality

Good correlation should answer:

```text
Why are these events related?
```

Possible answers:

```text
Same User
Same Host
Same Process
Same Session
Same IP
Same Resource
Same Time Window
```

---

# 66. Bad Correlation

Example:

```text
Any PowerShell
+
Any Login
+
Any DNS Query
```

This may correlate unrelated activity.

---

# 67. Good Correlation

Example:

```text
User Login
+
Same User
+
New Device
+
Same Session
+
MFA Change
+
15-minute Window
```

The relationship is explicit.

---

# 68. Sequence Conditions

A sequence may define:

```text
A before B
B before C
A and B within X minutes
C within Y minutes of B
```

This creates temporal structure.

---

# 69. Optional Sequence Steps

Some detections may permit:

```text
A
→
B
→
(optional C)
→
D
```

This improves resilience when some telemetry is missing.

---

# 70. Required vs Optional Events

Example:

```text
Required:
Successful Login
MFA Change

Optional:
New Device
Location Change
```

This can prevent the detection from failing because one enrichment source is unavailable.

---

# 71. Sequence Branches

A sequence can branch:

```text
          ┌── Process A
Login ────┤
          └── Process B
```

Both may indicate the same broader attack behavior.

---

# 72. Sequence Timeout

A sequence should expire if the next event does not arrive within a reasonable period.

Example:

```text
State:
Suspicious Login

Timeout:
30 minutes
```

After timeout:

```text
State Reset
```

---

# 73. State Explosion

Poorly designed stateful detections can create huge numbers of active states.

Example:

```text
Every User
×
Every Session
×
Every Host
×
Every Event
```

can become expensive.

Control state using:

```text
Narrow Keys
Time Limits
State Limits
Aggregation
```

---

# 74. Correlation Performance

Cost increases with:

```text
Event Volume
Time Window
Number of Entities
Cardinality
State
Cross-Source Joins
Correlation Frequency
```

---

# 75. Correlation Optimization

Use:

```text
Early Filtering
Relevant Fields
Reasonable Windows
Meaningful Correlation Keys
Efficient Lookups
Pre-Aggregation
```

Avoid unnecessary:

```text
Global Joins
Large Windows
High-Cardinality Grouping
```

---

# 76. Risk Model Design

A risk model should define:

```text
Signals
Weights
Multipliers
Decay
Thresholds
Caps
Overrides
Escalation
```

---

# 77. Risk Weight Example

```text
Known Malicious IOC       +40
Suspicious Behavior       +25
Privileged Account        +30
Critical Asset            +30
Successful Authentication +20
```

---

# 78. Risk Thresholds

Example:

```text
0–29
Low

30–59
Medium

60–99
High

100+
Critical
```

These are illustrative values; organizations should calibrate their own thresholds.

---

# 79. Risk-Based Alerting

Instead of:

```text
Alert on every event
```

use:

```text
Event
 ↓
Risk Contribution
 ↓
Entity Risk
 ↓
Threshold
 ↓
Alert
```

This can reduce analyst overload.

---

# 80. Risk-Based Prioritization

Example:

```text
Alert A:
Risk = 30

Alert B:
Risk = 95

Alert C:
Risk = 140
```

Analysts can prioritize:

```text
C → B → A
```

---

# 81. Risk-Based Suppression

Low-risk repeated events may be grouped:

```text
100 Low-Risk Signals
        ↓
1 Entity Risk Alert
```

This preserves evidence while reducing alert volume.

---

# 82. Risk-Based Escalation

Example:

```text
Risk < 50
→ Monitor

Risk 50–79
→ Analyst Review

Risk 80–99
→ Priority Investigation

Risk >= 100
→ Immediate Escalation
```

Exact thresholds should be tuned to the organization's SOC processes.

---

# 83. Risk Overrides

Certain conditions may justify immediate escalation.

Example:

```text
Confirmed Malware
on Critical Server
```

may override a normal numerical score.

---

# 84. Risk Explainability

Analysts should be able to answer:

```text
Why is this risk high?
```

Good:

```text
+40 Known C2
+30 Privileged Account
+25 MFA Change
+30 Critical Asset
```

Bad:

```text
Risk = 125
```

with no explanation.

---

# 85. Risk Auditability

Track:

```text
Original Score
Signals Added
Weights
Score Changes
Decay
Overrides
Threshold Crossings
```

This supports:

```text
Investigation
Tuning
Compliance
Model Validation
```

---

# 86. Risk Model Drift

Over time:

```text
Threats Change
Users Change
Infrastructure Changes
Business Processes Change
```

Risk weights may become inaccurate.

Review them periodically.

---

# 87. Risk Calibration

Use historical data:

```text
Known Incidents
False Positives
True Positives
Analyst Decisions
Simulation Results
```

to evaluate scoring.

---

# 88. Correlation Testing

Test:

```text
Correct Sequence
Wrong Sequence
Missing Event
Delayed Event
Duplicate Event
Unrelated Events
Multiple Entities
```

---

# 89. Positive Correlation Test

Input:

```text
A
→
B
→
C
```

Expected:

```text
Detection Fires
```

---

# 90. Negative Correlation Test

Input:

```text
A
→
X
→
C
```

where X is unrelated.

Expected:

```text
No Detection
```

---

# 91. Out-of-Order Test

Input arrival:

```text
C
A
B
```

Event timestamps:

```text
A
B
C
```

The detection should behave according to its intended event-ordering model.

---

# 92. Missing Event Test

Input:

```text
A
C
```

when:

```text
B
```

is missing.

Determine whether:

```text
Detection Should Fail
```

or:

```text
Detection Should Still Trigger
```

based on whether B is required.

---

# 93. Duplicate Event Test

Input:

```text
A
A
B
C
```

Ensure duplicate ingestion does not incorrectly inflate:

```text
Count
Risk
Confidence
```

---

# 94. Correlation False Positives

Common causes:

```text
Broad Time Window
Weak Correlation Key
Shared Infrastructure
Legitimate Automation
Duplicate Events
Common Administrative Activity
```

---

# 95. Correlation False Negatives

Common causes:

```text
Missing Telemetry
Wrong Entity Mapping
Short Time Window
Incorrect Sequence
Delayed Events
Schema Changes
```

---

# 96. Correlation Anti-Patterns

Avoid:

```text
Huge Time Windows
```

```text
Weak Correlation Keys
```

```text
Unlimited State
```

```text
Counting Duplicate Signals
```

```text
Unexplained Risk Scores
```

```text
Overly Complex Sequences
```

```text
No Expiration
```

---

# 97. Practical Example – Account Takeover

## Signals

```text
Failed Login
Successful Login
New Device
Unusual Location
MFA Change
Sensitive Access
```

## Correlation

```text
Same User
Within 30 Minutes
```

## Risk

```text
Failure Burst       +15
Successful Login    +20
New Device          +20
Unusual Location    +15
MFA Change          +30
Sensitive Access    +30
```

Total:

```text
130
```

Result:

```text
High/Critical Priority
```

---

# 98. Practical Example – C2 Detection

Signals:

```text
Rare Domain
+
Periodic Connections
+
Unusual Process
+
Known Threat Intelligence
```

Risk:

```text
Rare Destination    +15
Beaconing            +25
Suspicious Process   +30
Known Malicious IOC  +40
```

Total:

```text
110
```

---

# 99. Practical Example – Ransomware

Signals:

```text
Suspicious Process
+
Mass File Changes
+
File Rename Burst
+
Recovery Tampering
```

Correlation:

```text
Same Host
Within 5 Minutes
```

Result:

```text
High Confidence
```

---

# 100. Practical Example – Password Spray

Signals:

```text
Authentication Failure
```

Group:

```text
Source IP
```

Conditions:

```text
10+ Unique Users
within 10 Minutes
```

Add:

```text
Successful Login
```

to increase investigation priority.

---

# 101. Practical Example – Lateral Movement

Sequence:

```text
Credential Access
      ↓
New Authentication
      ↓
Remote Service
      ↓
Destination Host
      ↓
Administrative Activity
```

Correlation:

```text
Same User
+
Related Hosts
+
30-Minute Window
```

---

# 102. Practical Example – Cloud Compromise

Sequence:

```text
Unusual Login
      ↓
New Region
      ↓
Access Key Creation
      ↓
Privilege Change
      ↓
Sensitive API Calls
```

Risk can accumulate at:

```text
User
Cloud Account
Resource
```

---

# 103. Practical Example – Web Application Abuse

Signals:

```text
Repeated Failed Requests
+
Endpoint Enumeration
+
Suspicious Parameters
+
Successful Authentication
+
Sensitive Data Access
```

Correlation:

```text
Same Session
+
Same Source
```

---

# 104. Correlation Architecture

Conceptually:

```text
             Telemetry
                 ↓
        Normalization Layer
                 ↓
        Detection Signals
                 ↓
        Correlation Engine
                 ↓
       ┌─────────┴─────────┐
       ↓                   ↓
   Sequence             Risk Engine
       ↓                   ↓
       └─────────┬─────────┘
                 ↓
              Alert
                 ↓
           Investigation
```

---

# 105. Detection Signal Layer

The correlation engine should ideally consume normalized signals such as:

```text
Suspicious Login
Malicious IOC
Suspicious Process
Privilege Change
Rare Destination
Sensitive Access
```

rather than repeatedly processing raw telemetry unnecessarily.

---

# 106. Correlation Engine Responsibilities

A correlation engine may handle:

```text
Event Matching
Entity Resolution
Time Windows
Sequences
State
Aggregation
Risk
Deduplication
Suppression
Alert Generation
```

---

# 107. Entity Resolution

Different systems may identify the same user differently:

```text
DOMAIN\alice
alice@example.com
alice
```

Correlation requires reliable identity mapping.

---

# 108. Host Resolution

A host may appear as:

```text
server01
server01.example.com
10.0.0.10
Asset-ID-123
```

These may represent the same system.

Poor resolution causes:

```text
Missed Correlation
```

---

# 109. Correlation Across Identity

Identity systems can provide:

```text
User
Role
Group
MFA
Authentication
Device
Application
```

This can significantly improve correlation.

---

# 110. Correlation Across Endpoint

Endpoint telemetry provides:

```text
Process
File
Registry
Network
User
Parent Process
Command Line
```

---

# 111. Correlation Across Network

Network telemetry provides:

```text
Source
Destination
Port
Protocol
Bytes
DNS
TLS
Connection Timing
```

---

# 112. Correlation Across Cloud

Cloud telemetry provides:

```text
Principal
API
Resource
Region
Source IP
Authentication
Permission
Configuration
```

---

# 113. Correlation Across Application

Application telemetry provides:

```text
Session
User
Request
Endpoint
Response
Resource
Transaction
```

---

# 114. Correlation Data Model

A normalized event might contain:

```text
timestamp
event.type
user.id
host.id
source.ip
destination.ip
process.id
session.id
resource.id
risk
```

Normalization simplifies cross-source correlation.

---

# 115. Correlation Metadata

Useful metadata:

```text
correlation_id
parent_event_id
sequence_id
entity_id
risk_score
confidence
detection_id
```

---

# 116. Correlation IDs

A correlation ID can connect related events:

```text
Correlation ID:
ABC123
```

Events:

```text
Login
Process
Network
File
```

all associated with:

```text
ABC123
```

---

# 117. Alert Aggregation

Instead of:

```text
Alert 1
Alert 2
Alert 3
Alert 4
```

create:

```text
Incident:
Potential Host Compromise
```

with:

```text
Underlying Signals:
1–4
```

---

# 118. Incident-Level Correlation

A mature system can correlate alerts into incidents:

```text
Alert
 ↓
Alert
 ↓
Alert
 ↓
Incident
```

This is different from simply suppressing alerts because the underlying evidence remains accessible.

---

# 119. Alert Suppression vs Correlation

### Suppression

Reduces repeated notifications.

### Correlation

Combines related evidence.

Example:

```text
Suppression:
100 identical alerts → 1 notification
```

```text
Correlation:
Login + Process + Network → 1 attack story
```

---

# 120. Correlation vs Aggregation

### Aggregation

Groups similar events.

```text
100 failed logins
```

### Correlation

Connects different but related events.

```text
Failed Login
+
Successful Login
+
MFA Change
```

---

# 121. Risk Aggregation

Risk can aggregate across:

```text
Events
Alerts
Users
Hosts
Incidents
```

Example:

```text
10 signals
→ User Risk = 90
```

---

# 122. Risk and Incident Prioritization

An incident queue may be sorted by:

```text
Risk
Confidence
Asset Criticality
Business Impact
Threat Intelligence
```

---

# 123. Business Context

Risk should consider business importance.

Example:

```text
Same Detection

Development VM:
Low Business Impact

Payment Server:
High Business Impact
```

The detection may have the same confidence but different priority.

---

# 124. Data Sensitivity

Potentially sensitive resources:

```text
Customer Data
Financial Data
Credentials
Source Code
Health Data
Secrets
```

Access to such resources may increase risk.

---

# 125. Privileged Identity

A suspicious event involving:

```text
Standard User
```

may be less concerning than the same event involving:

```text
Domain Administrator
Cloud Administrator
Root
```

---

# 126. Risk Explainability for Analysts

An analyst should quickly see:

```text
Why Alerted?
What Signals?
What Entities?
What Sequence?
What Risk?
What Context?
```

Example:

```text
Risk: 125

+40 Known C2
+30 Privileged User
+25 New Device
+30 Critical Host
```

---

# 127. Risk Visualization

Conceptually:

```text
User: Alice

Risk: 115
███████████████████

Signals:
[+] Malicious IP
[+] New Device
[+] MFA Change
[+] Sensitive Access
```

Good visualization supports investigation without hiding the evidence.

---

# 128. Correlation Investigation View

An analyst should be able to see:

```text
Timeline
Entity Graph
Process Tree
Network Connections
Authentication
Risk Score
Threat Intelligence
ATT&CK Mapping
```

---

# 129. Detection Explainability

Every correlation should explain:

```text
Why Events Were Related
Why Sequence Matched
Why Risk Increased
Why Alert Was Generated
```

Avoid black-box logic where possible.

---

# 130. Correlation Rule Documentation

Document:

```text
Purpose
Threat
Data Sources
Entities
Correlation Key
Time Window
Required Events
Optional Events
Sequence
Risk
Severity
Exceptions
False Positives
Performance
Tests
Owner
Version
```

---

# 131. Correlation Rule Example

```text
Name:
Potential Account Takeover

Threat:
Credential Compromise

Events:
1. Failed Authentication Burst
2. Successful Authentication
3. New Device
4. MFA Change
5. Sensitive Resource Access

Correlation Key:
User ID

Time Window:
30 Minutes

Required:
Events 2 and 4

Optional:
Events 1, 3, 5

Risk:
Event 1 = +15
Event 2 = +20
Event 3 = +20
Event 4 = +30
Event 5 = +30

Alert Threshold:
Risk >= 80

Severity:
High

False Positives:
Travel
Approved Device Enrollment
Helpdesk-Assisted MFA Reset
```

---

# 132. Testing Correlation Rules

Test:

```text
[ ] Correct events
[ ] Wrong order
[ ] Missing event
[ ] Duplicate event
[ ] Late event
[ ] Unrelated event
[ ] Different user
[ ] Different host
[ ] Boundary timestamps
[ ] Multiple simultaneous users
```

---

# 133. Boundary Testing

If window is:

```text
10 minutes
```

test:

```text
9:59
10:00
10:01
```

This identifies boundary-condition bugs.

---

# 134. Concurrency Testing

Test:

```text
User A
Sequence A

User B
Sequence B
```

at the same time.

Ensure events are not incorrectly mixed.

---

# 135. Risk Model Testing

Test:

```text
Minimum Risk
Maximum Risk
Threshold - 1
Threshold
Threshold + 1
Decay
Duplicate Signals
Overrides
```

---

# 136. Correlation Performance Testing

Measure:

```text
Events/Second
Processing Latency
State Count
Memory
CPU
Alert Volume
Query Cost
```

---

# 137. Correlation Latency

Important metrics:

```text
Event Arrival
      ↓
Correlation
      ↓
Detection
      ↓
Alert
```

The difference between these timestamps is detection latency.

---

# 138. Real-Time Correlation

Useful for:

```text
Account Takeover
Ransomware
Active C2
Privilege Escalation
Critical Infrastructure Attacks
```

---

# 139. Scheduled Correlation

Useful for:

```text
Daily Anomaly
Long-Term Risk
Periodic Threat Hunting
Historical Analysis
```

---

# 140. Streaming Correlation

Conceptually:

```text
Event Stream
 ↓
Filter
 ↓
State
 ↓
Correlation
 ↓
Alert
```

Designed for continuous processing.

---

# 141. Batch Correlation

Conceptually:

```text
Historical Dataset
 ↓
Query
 ↓
Correlation
 ↓
Results
```

Useful when large historical windows are needed.

---

# 142. Hybrid Correlation

Combine:

```text
Real-Time Signals
+
Historical Context
```

Example:

```text
Current Login
+
30-Day User Baseline
```

This provides stronger context.

---

# 143. Historical Risk

A user may already have elevated risk:

```text
Previous Suspicious Activity
+
Current Suspicious Activity
```

can increase investigation priority.

Historical risk should still decay appropriately.

---

# 144. Risk Reset

After an incident is resolved:

```text
Risk
 ↓
Review
 ↓
Reset / Decay
```

The system should avoid permanently treating an entity as malicious.

---

# 145. Risk Contamination

Bad design:

```text
One False Positive
 ↓
Permanent High Risk
```

This creates:

```text
Alert Fatigue
```

Risk must be reversible.

---

# 146. Analyst Feedback

Analysts can classify:

```text
True Positive
False Positive
Benign
Expected Activity
Duplicate
Unknown
```

This feedback can improve:

```text
Correlation
Risk Weights
Exceptions
Thresholds
```

---

# 147. Feedback Loop

```text
Detection
 ↓
Alert
 ↓
Analyst
 ↓
Classification
 ↓
Tuning
 ↓
Improved Detection
```

This is an important part of detection engineering.

---

# 148. Correlation Maturity

### Level 1

Single Event:

```text
IOC Match
```

### Level 2

Multi-Event:

```text
IOC + Process
```

### Level 3

Entity Correlation:

```text
User + Host + Network
```

### Level 4

Sequence:

```text
A → B → C
```

### Level 5

Risk-Based:

```text
Signals + Context + History
```

### Level 6

Adaptive:

```text
Risk + Behavior + Threat Intelligence
+ Continuous Feedback
```

---

# 149. Common Mistakes

## Mistake 1

Using huge time windows.

Problem:

```text
Unrelated Events
```

---

## Mistake 2

Using weak correlation keys.

Problem:

```text
False Correlation
```

---

## Mistake 3

Ignoring event ordering.

Problem:

```text
Invalid Attack Sequence
```

---

## Mistake 4

Counting duplicate evidence.

Problem:

```text
Artificial Risk Inflation
```

---

## Mistake 5

No state expiration.

Problem:

```text
State Explosion
```

---

## Mistake 6

Unexplainable risk scores.

Problem:

```text
Analyst Distrust
```

---

## Mistake 7

Never decaying risk.

Problem:

```text
Permanent Risk
```

---

## Mistake 8

Overly complex correlation.

Problem:

```text
Maintenance Difficulty
Performance Problems
Debugging Difficulty
```

---

# 150. Practical Design Checklist

```text
[ ] Threat defined
[ ] Individual signals identified
[ ] Correlation relationship defined
[ ] Correlation key selected
[ ] Entity resolution validated
[ ] Time window selected
[ ] Event order defined
[ ] Required events identified
[ ] Optional events identified
[ ] State expiration defined
[ ] Duplicate handling defined
[ ] Late event handling defined
[ ] Risk model defined
[ ] Risk decay considered
[ ] Severity defined
[ ] Explainability implemented
[ ] Positive tests created
[ ] Negative tests created
[ ] Performance tested
[ ] False positives analyzed
[ ] Documentation completed
```

---

# 151. Interview Questions

### What is event correlation?

> Connecting multiple related security events based on shared attributes such as time, user, host, IP, process, or session.

### What is sequence detection?

> Detection that requires events to occur in a particular order within a defined time or contextual relationship.

### What is the difference between correlation and sequence detection?

> Correlation connects related events, while sequence detection additionally cares about the order in which those events occur.

### What is a correlation key?

> A field or combination of fields used to determine which events belong to the same activity or entity.

### What is stateful detection?

> Detection that maintains information about previous events or entity state when evaluating new events.

### What is risk-based detection?

> Combining multiple signals and contextual factors into a score used to prioritize or trigger security detections.

### What is risk decay?

> Reducing the influence of older risk signals over time so historical activity does not permanently inflate an entity's risk.

### Why is explainability important in risk scoring?

> Analysts need to understand which signals contributed to the score so they can validate and investigate the alert.

### What problems can large correlation windows create?

> They increase processing cost and may correlate unrelated events, increasing false positives.

### Why is entity resolution important?

> Different systems may represent the same user, host, or resource differently; without reliable mapping, related events may not correlate correctly.

### How do you prevent duplicate events from inflating risk?

> Deduplicate events or identify repeated evidence before applying risk weights.

### How would you test a sequence detection?

> Test the correct sequence, incorrect order, missing events, duplicate events, delayed events, boundary timestamps, unrelated entities, and concurrent sequences.

---

# 152. Quick Revision

```text
Correlation
→ Connect related events

Correlation Key
→ Attribute used to relate events

Time Window
→ Period in which events must occur

Sequence
→ Ordered event chain

Stateful Detection
→ Maintains historical state

Risk Score
→ Combined security significance

Risk Weight
→ Contribution of a signal

Risk Decay
→ Reduces influence of old signals

Risk Threshold
→ Score required for escalation

Risk Override
→ Special condition that changes normal scoring

Entity Risk
→ Risk associated with user/host/account/etc.

Cross-Source Correlation
→ Connect events from multiple telemetry sources

Alert Aggregation
→ Groups related alerts

Entity Resolution
→ Maps different identifiers to the same entity

Correlation ID
→ Identifier linking related events

State Expiration
→ Removes stale detection state
```

---

# 153. Golden Rules

```text
1. A single event rarely tells the entire story.

2. Correlate events using meaningful relationships.

3. Choose correlation keys carefully.

4. Use time windows that match the expected attack behavior.

5. Sequence detection when event order matters.

6. Distinguish event time from processing time.

7. Handle delayed and out-of-order telemetry.

8. Define required and optional sequence steps.

9. Expire stale state.

10. Prevent duplicate evidence from inflating risk.

11. Resolve identities consistently across data sources.

12. Use cross-source correlation when it adds meaningful context.

13. Combine weak signals carefully.

14. Do not assume multiple signals automatically mean malicious activity.

15. Distinguish risk from confidence.

16. Consider asset criticality and identity privilege.

17. Use risk decay.

18. Make risk scores explainable.

19. Keep risk models auditable.

20. Test boundary conditions.

21. Test missing and duplicate events.

22. Test concurrent entities.

23. Measure correlation latency.

24. Monitor correlation performance.

25. Avoid unnecessarily complex sequences.

26. Aggregate related alerts without losing evidence.

27. Use analyst feedback to improve correlation.

28. Periodically recalibrate risk weights.

29. Treat correlation logic as production code.

30. The goal of correlation is not to create complicated rules—it is to connect meaningful evidence into an actionable security story.
```

---

# 154. Final Mental Model

Think about detection as progressively increasing context:

```text
Single Event
     ↓
Signal
     ↓
Multiple Signals
     ↓
Correlation
     ↓
Sequence
     ↓
Entity Context
     ↓
Threat Context
     ↓
Risk Score
     ↓
Prioritized Alert
     ↓
Investigation
```

Or:

```text
WHAT HAPPENED?
      ↓
WHEN?
      ↓
TO WHOM?
      ↓
ON WHICH SYSTEM?
      ↓
WHAT HAPPENED BEFORE?
      ↓
WHAT HAPPENED AFTER?
      ↓
WHAT OTHER SIGNALS SUPPORT IT?
      ↓
HOW IMPORTANT IS IT?
      ↓
WHAT SHOULD THE SOC DO?
```

The mature detection model is:

```text
Telemetry
    ↓
Detection Signals
    ↓
Correlation
    ↓
Sequence
    ↓
Context
    ↓
Risk
    ↓
Priority
    ↓
Investigation
    ↓
Response
```

---

# 155. Chapter Summary

This chapter covered:

```text
Correlation Fundamentals
Correlation Keys
Time-Based Correlation
Entity-Based Correlation
Cross-Source Correlation
Sequence Detection
Stateful Detection
State Machines
Event Ordering
Late Events
Correlation Windows
Attack Chains
Risk-Based Detection
Risk Scoring
Risk Weighting
Risk Multipliers
Risk Caps
Risk Decay
Risk Thresholds
Risk Overrides
Entity Risk
Historical Risk
Risk Explainability
Risk Auditability
Entity Resolution
Alert Aggregation
Correlation Testing
Risk Testing
Performance
Correlation Latency
Streaming Correlation
Batch Correlation
Hybrid Correlation
Analyst Feedback
Correlation Maturity
```

The key principle is:

> **Correlation turns isolated events into relationships, sequence detection turns relationships into attack stories, and risk-based detection turns those stories into actionable priorities.**

A strong detection system should therefore move beyond:

```text
"Something suspicious happened."
```

toward:

```text
"This user performed a sequence of related actions across
identity, endpoint, and network telemetry within a defined
time window, involving a critical asset and multiple
high-confidence signals, resulting in elevated risk."
```

That is the foundation of **high-confidence, analyst-friendly detection engineering**.

---