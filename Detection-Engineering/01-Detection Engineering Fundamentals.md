# Chapter 01 – Detection Engineering Fundamentals

> Detection Engineering is the discipline of designing, developing, testing, deploying, tuning, and maintaining security detections that identify meaningful adversary behavior from available security telemetry.

---

# 1. What Is Detection Engineering?

Detection Engineering transforms:

```text
Threat Intelligence
        +
Adversary Behavior
        +
Security Telemetry
        ↓
Detection Logic
        ↓
Security Alert
        ↓
Investigation
        ↓
Response
```

A detection engineer answers:

```text
What are we trying to detect?

Why is the behavior suspicious?

What telemetry exposes it?

What logic identifies it?

What legitimate activity could trigger it?

How do we test it?

How do we measure it?

How do we maintain it?
```

The goal is not:

```text
Create More Alerts
```

The goal is:

```text
Create Better Alerts
```

---

# 2. Why Detection Engineering Matters

Security teams receive enormous amounts of telemetry.

For example:

```text
Millions of Events
        ↓
Thousands of Interesting Events
        ↓
Hundreds of Alerts
        ↓
Dozens of Investigations
        ↓
Few Real Incidents
```

Detection engineering helps convert large volumes of telemetry into useful security signals.

```text
Raw Telemetry
      ↓
Detection
      ↓
Context
      ↓
Prioritization
      ↓
Investigation
```

Without effective detection engineering:

```text
Too Many Alerts
+
Poor Detection Coverage
+
High False Positives
+
Missed Threats
=
Ineffective SOC
```

---

# 3. Detection Engineering vs Detection

These are different concepts.

### Detection

A specific piece of logic that identifies suspicious activity.

Example:

```text
More than 20 failed logins
from one source against one account
within 5 minutes
```

### Detection Engineering

The complete discipline around that detection:

```text
Threat Research
 ↓
Telemetry Analysis
 ↓
Detection Design
 ↓
Query Development
 ↓
Testing
 ↓
Validation
 ↓
Deployment
 ↓
Monitoring
 ↓
Tuning
 ↓
Maintenance
```

---

# 4. Detection Engineering vs SOC Monitoring

SOC monitoring focuses on:

```text
Watching Alerts
Investigating Events
Responding to Incidents
```

Detection engineering focuses on:

```text
Creating
Improving
Testing
Maintaining
and Measuring
the detections that generate those alerts.
```

Relationship:

```text
Detection Engineer
        ↓
Builds Detection
        ↓
SOC
        ↓
Investigates Alert
        ↓
Provides Feedback
        ↓
Detection Engineer
        ↓
Improves Detection
```

This creates a feedback loop.

---

# 5. Detection Engineering vs Threat Hunting

### Threat Hunting

Proactively searches for threats.

```text
Hypothesis
   ↓
Search
   ↓
Investigation
   ↓
Finding
```

### Detection Engineering

Turns repeatable threat patterns into persistent detections.

```text
Hunt Finding
   ↓
Behavior Pattern
   ↓
Detection Logic
   ↓
Production Detection
```

Therefore:

```text
Threat Hunting
      ↓
Discovery
      ↓
Detection Engineering
      ↓
Continuous Detection
```

---

# 6. Detection Engineering vs Incident Response

### Detection Engineering

```text
Identify suspicious behavior
```

### Incident Response

```text
Investigate
Contain
Eradicate
Recover
```

Relationship:

```text
Detection
   ↓
Alert
   ↓
Investigation
   ↓
Incident Response
```

---

# 7. Detection Engineering vs SIEM Engineering

### SIEM Engineering

Concerned with:

```text
Data Ingestion
Parsing
Normalization
Storage
Search
Performance
Architecture
Availability
```

### Detection Engineering

Concerned with:

```text
Threat Detection
Detection Logic
Testing
Coverage
Tuning
Validation
Lifecycle
```

They overlap heavily.

```text
SIEM Engineering
       +
Detection Engineering
       +
SOC Operations
       ↓
Effective Security Monitoring
```

---

# 8. Detection Engineering Lifecycle

A professional detection follows a lifecycle:

```text
1. Threat Identification
        ↓
2. Threat Understanding
        ↓
3. Detection Hypothesis
        ↓
4. Telemetry Identification
        ↓
5. Detection Development
        ↓
6. Testing
        ↓
7. Validation
        ↓
8. Review
        ↓
9. Deployment
        ↓
10. Monitoring
        ↓
11. Tuning
        ↓
12. Measurement
        ↓
13. Improvement / Retirement
```

---

# 9. Step 1 – Threat Identification

Start with a threat.

Sources can include:

```text
Threat Intelligence
Incident Reports
Threat Hunting
Security Research
Vulnerability Reports
MITRE ATT&CK
Vendor Research
Internal Incidents
Red Team Findings
Purple Team Exercises
```

Example:

```text
Threat:
Credential Theft
```

---

# 10. Step 2 – Understand the Threat

Before writing a query, understand:

```text
How does the attacker operate?

What tools are used?

What processes are created?

What accounts are involved?

What network connections occur?

What files change?

What persistence is created?

What telemetry is generated?
```

Do not immediately jump to:

```text
"Write a SIEM rule."
```

First understand the behavior.

---

# 11. Step 3 – Detection Hypothesis

A detection hypothesis describes:

> **What observable behavior would indicate that a threat may be occurring?**

Example:

```text
Hypothesis:

An attacker attempting credential access
may access sensitive credential-related
processes from an unusual process context.
```

Then determine:

```text
What evidence would support this?
```

---

# 12. Detection Hypothesis Structure

A useful structure:

```text
Threat
+
Behavior
+
Observable Evidence
+
Context
```

Example:

```text
Threat:
Account Compromise

Behavior:
Unusual authentication

Evidence:
Successful login

Context:
New device + unusual location
```

---

# 13. Step 4 – Identify Required Telemetry

Ask:

```text
What data do I need?
```

For authentication detection:

```text
Timestamp
User
Source IP
Destination
Device
Authentication Result
Authentication Method
Location
```

Without required telemetry:

```text
No Reliable Detection
```

---

# 14. Telemetry Dependency

Every detection has dependencies.

Example:

```text
Detection:
Suspicious PowerShell

Requires:
Process Creation
Command Line
Parent Process
User
Host
Network
```

If command-line logging is missing:

```text
Detection Quality ↓
```

---

# 15. Detection Blind Spot

A blind spot occurs when required attacker activity cannot be observed.

Example:

```text
Threat:
Credential Theft

Required:
Endpoint Process Telemetry

Available:
Only Firewall Logs
```

Result:

```text
Detection Blind Spot
```

---

# 16. Visibility Before Detection

A fundamental rule:

```text
No Telemetry
     ↓
No Detection
```

Therefore:

```text
Detection Engineering
        +
Telemetry Engineering
```

must work together.

---

# 17. Step 5 – Detection Design

Now define the detection.

Example:

```text
Detect suspicious authentication:

IF
    authentication = success
AND
    new_device = true
AND
    unusual_location = true
AND
    user_risk > threshold

THEN
    generate alert
```

This is detection logic.

---

# 18. Detection Logic Components

A detection commonly contains:

```text
Data Source
Fields
Conditions
Threshold
Time Window
Correlation
Severity
Risk
Exceptions
Metadata
Response
```

Example:

```text
Data:
Authentication Logs

Condition:
Failed Login Count > 20

Window:
5 Minutes

Group:
User + Source IP

Severity:
Medium
```

---

# 19. Simple Rule

Example:

```text
IF failed_login_count > 20
WITHIN 5 minutes
FOR same user
THEN alert
```

This is a threshold detection.

---

# 20. Contextual Rule

More advanced:

```text
IF

failed_login_count > 20

AND

source_ip is unusual

AND

user is privileged

THEN

high-risk alert
```

Adding context generally improves prioritization.

---

# 21. Behavioral Rule

Instead of looking for a fixed indicator:

```text
IF

User logs in from an unusual device

AND

unusual location

AND

unusual time

THEN

behavioral anomaly
```

---

# 22. Correlation Rule

Example:

```text
Failed Login
      ↓
Successful Login
      ↓
MFA Change
      ↓
Privilege Change
```

↓

```text
Potential Account Takeover
```

---

# 23. Step 6 – Detection Development

Implement the logic using the target platform.

Common detection languages include:

```text
Sigma
KQL
SPL
SQL
YARA
Regular Expressions
Platform-Specific Query Languages
```

The exact language depends on the security platform.

---

# 24. Sigma

Sigma is a generic, vendor-neutral format for describing detection logic.

Conceptually:

```text
Detection Idea
      ↓
Sigma Rule
      ↓
Platform Translation
      ↓
SIEM / Detection Platform
```

Benefits:

```text
Portability
Standardization
Version Control
Collaboration
```

---

# 25. Example Detection Metadata

A professional detection may contain:

```text
Title
Description
Author
Status
Severity
References
Tags
ATT&CK Technique
Data Sources
False Positives
Tests
Version
```

---

# 26. Detection Documentation

A detection should explain:

```text
What does it detect?

Why is it suspicious?

What telemetry does it require?

What are common false positives?

What should the analyst investigate?

Which ATT&CK technique is relevant?

Who owns the detection?
```

Poor:

```text
Detect suspicious login
```

Better:

```text
Detect successful authentication from a new
device and unusual geographic location when
preceded by repeated authentication failures.
```

---

# 27. Step 7 – Testing

Never assume:

```text
Query Works
```

just because it compiles.

Test:

```text
Does malicious activity trigger?

Does legitimate activity remain quiet?

Does missing data break the rule?

Does duplicate data create duplicate alerts?

Does the rule work at scale?
```

---

# 28. Positive Testing

Simulate or reproduce the behavior the rule is intended to detect.

Example:

```text
Repeated Authentication Failures
        ↓
Expected:
Alert
```

---

# 29. Negative Testing

Test legitimate behavior.

Example:

```text
Normal Authentication
        ↓
Expected:
No Alert
```

---

# 30. Boundary Testing

Suppose:

```text
Threshold = 20
```

Test:

```text
19
20
21
```

Why?

To verify threshold behavior.

---

# 31. Missing Data Testing

What happens if:

```text
Source IP = NULL
```

or:

```text
User = NULL
```

The detection should fail safely rather than silently producing incorrect conclusions.

---

# 32. Duplicate Event Testing

Suppose:

```text
Same Event
received 3 times
```

Does the system produce:

```text
1 alert
```

or:

```text
3 duplicate alerts?
```

Deduplication may be required.

---

# 33. Delayed Event Testing

Security telemetry can arrive late.

Example:

```text
Event Time:
10:00

SIEM Arrival:
10:05
```

Detection design should consider:

```text
Event Time
vs
Ingestion Time
```

---

# 34. Step 8 – Validation

Testing asks:

```text
Does the rule technically work?
```

Validation asks:

```text
Does it detect the intended threat effectively?
```

Validation can involve:

```text
Attack Simulation
Threat Hunting
Purple Teaming
Historical Data
Replay
Red Team Activity
```

---

# 35. Purple Team Validation

```text
Red Team
   ↓
Executes Behavior
   ↓
Telemetry
   ↓
Detection
   ↓
Blue Team
   ↓
Investigates
```

This validates the complete detection chain.

---

# 36. Detection Validation Questions

Ask:

```text
Did telemetry appear?

Was the behavior observable?

Did the detection fire?

How long did it take?

Was the alert understandable?

Was the severity appropriate?

Was the ATT&CK mapping correct?

Could the analyst investigate it?

Could an attacker bypass it?
```

---

# 37. Step 9 – Code Review

Production detections should ideally receive peer review.

Review:

```text
Logic
Performance
False Positives
False Negatives
Security Impact
ATT&CK Mapping
Testing
Documentation
```

---

# 38. Step 10 – Deployment

A safe deployment process:

```text
Development
 ↓
Testing
 ↓
Code Review
 ↓
Staging
 ↓
Shadow Mode
 ↓
Production
```

For critical environments:

```text
Canary Deployment
+
Monitoring
+
Rollback
```

---

# 39. Shadow Mode

A detection runs without generating normal analyst alerts.

```text
Detection
 ↓
Matches Events
 ↓
Record Results
 ↓
Analyze
 ↓
Tune
 ↓
Enable
```

Useful for:

```text
Noisy Rules
New Rules
High-Impact Rules
Large-Scale Deployments
```

---

# 40. Step 11 – Production Monitoring

Once deployed, monitor:

```text
Alert Volume
False Positives
Detection Latency
Query Performance
Errors
Data Availability
Coverage
Analyst Feedback
```

A detection is not finished when it reaches production.

---

# 41. Step 12 – Tuning

Suppose:

```text
1000 Alerts
900 False Positives
100 Useful Alerts
```

Precision is poor.

Investigate:

```text
Why are legitimate activities matching?
```

Then improve:

```text
Context
Correlation
Threshold
Exceptions
Entity Filtering
Risk Scoring
```

---

# 42. Avoid Blind Exclusions

Bad:

```text
Exclude:
10.0.0.0/8
```

Potential result:

```text
Huge Blind Spot
```

Better:

```text
Exclude only:
Known Scanner
Specific Host
Specific Service
Specific Scheduled Activity
```

with documentation and review.

---

# 43. Step 13 – Measure Detection

Useful measurements:

```text
Precision
Recall
False Positive Rate
Alert Volume
Detection Coverage
Detection Latency
Query Performance
Test Pass Rate
```

---

# 44. Detection Coverage

Coverage asks:

```text
What threats can we detect?
```

Example:

```text
ATT&CK Technique A → Covered
ATT&CK Technique B → Covered
ATT&CK Technique C → Partial
ATT&CK Technique D → Not Covered
```

---

# 45. Detection Gap

A detection gap occurs when:

```text
Important Threat
      +
Insufficient Telemetry or Detection
```

Example:

```text
Technique:
Credential Access

Telemetry:
Partial

Detection:
None
```

Result:

```text
Detection Gap
```

---

# 46. Detection Maturity

A conceptual maturity progression:

```text
Level 1
Reactive Rules

Level 2
Centralized Detection

Level 3
Detection Engineering

Level 4
Threat-Informed Detection

Level 5
Automated / AI-Assisted Detection
```

---

# 47. Level 1 – Reactive

Characteristics:

```text
Manual Rules
Limited Testing
High False Positives
Little Documentation
```

---

# 48. Level 2 – Centralized

```text
SIEM
Centralized Logs
Standard Rules
Basic Monitoring
```

---

# 49. Level 3 – Detection Engineering

```text
Detection-as-Code
Testing
Version Control
ATT&CK Mapping
Tuning
Coverage
```

---

# 50. Level 4 – Threat-Informed

```text
Threat Intelligence
Threat Modeling
Threat Hunting
Purple Teaming
Attack Simulation
Coverage Analysis
```

---

# 51. Level 5 – Modern Detection

```text
Behavior Analytics
Risk Engines
XDR
SOAR
AI Assistance
Graph Analytics
Continuous Validation
```

---

# 52. Detection Engineering Feedback Loop

A mature environment continuously learns:

```text
Incident
   ↓
Investigation
   ↓
Root Cause
   ↓
Detection Gap
   ↓
New Detection
   ↓
Testing
   ↓
Production
   ↓
Monitoring
   ↓
Improvement
```

---

# 53. Detection Quality Dimensions

Evaluate detections using:

```text
Accuracy
Coverage
Timeliness
Actionability
Performance
Maintainability
Resilience
```

---

# 54. Accuracy

Does the detection correctly distinguish:

```text
Malicious
vs
Legitimate
```

---

# 55. Coverage

Does the detection cover:

```text
Relevant Variants
Attack Techniques
Attack Paths
Environments
```

---

# 56. Timeliness

How quickly does the detection fire?

```text
Attack
 ↓
Telemetry
 ↓
Detection
 ↓
Alert
```

Lower detection latency is generally preferable.

---

# 57. Actionability

An alert should help analysts answer:

```text
What happened?
Why is it suspicious?
Who is affected?
What should I investigate?
```

---

# 58. Performance

A detection should not unnecessarily consume:

```text
CPU
Memory
Storage
Query Capacity
Network
```

---

# 59. Maintainability

A detection should be:

```text
Readable
Documented
Versioned
Tested
Owned
```

---

# 60. Resilience

A detection should account for:

```text
Schema Changes
Telemetry Delays
Missing Fields
Tool Changes
Attacker Evasion
Environment Changes
```

---

# 61. Detection Dependencies

A detection may depend on:

```text
Data Source
Parser
Schema
Enrichment
Threat Intelligence
Lookup Table
Reference Set
External API
```

Document these dependencies.

---

# 62. Detection Metadata

Recommended metadata:

```text
Name
Description
Owner
Severity
Confidence
Status
Created Date
Modified Date
Version
Data Sources
ATT&CK Mapping
References
False Positives
Testing
Dependencies
Response Guidance
```

---

# 63. Severity vs Confidence

These are different.

### Severity

How serious would the activity be?

```text
Low
Medium
High
Critical
```

### Confidence

How confident are we that the detection represents malicious behavior?

```text
Low
Medium
High
```

Example:

```text
High Severity
+
Low Confidence
```

should not automatically result in aggressive response.

---

# 64. Risk

Risk can combine:

```text
Severity
+
Confidence
+
Asset Criticality
+
User Privilege
+
Threat Intelligence
+
Behavior
+
Historical Activity
```

Example:

```text
Suspicious Login       +20
Privileged Account     +30
Critical Server        +30
Malicious IP           +40
Behavioral Anomaly     +20
```

Total:

```text
140 Risk
```

---

# 65. Alert Prioritization

Instead of:

```text
Process Alerts in Arrival Order
```

use:

```text
Risk
+
Confidence
+
Impact
+
Asset Criticality
```

to prioritize.

---

# 66. Detection vs Prevention

Detection:

```text
Identify Threat
```

Prevention:

```text
Stop Threat
```

Example:

```text
EDR Prevention
→ Blocks Execution

SIEM Detection
→ Identifies Execution
```

Both are important.

---

# 67. Detection vs Response

```text
Detection
→ "Something suspicious happened."

Response
→ "What should we do about it?"
```

A good detection should provide enough context for effective response.

---

# 68. Detection Engineering and Threat Intelligence

Threat intelligence can provide:

```text
IOCs
TTPs
Threat Actors
Campaigns
Infrastructure
Malware Behavior
```

Detection engineering converts relevant intelligence into:

```text
Detections
Hunts
Monitoring
Coverage
```

---

# 69. Intelligence-to-Detection Pipeline

```text
Threat Intelligence
       ↓
Validate
       ↓
Extract Behavior
       ↓
Identify Telemetry
       ↓
Develop Detection
       ↓
Test
       ↓
Deploy
```

---

# 70. Detection Engineering and MITRE ATT&CK

ATT&CK can answer:

```text
What technique are we detecting?

What telemetry should expose it?

What other techniques occur around it?

What detection coverage do we have?
```

Example:

```text
Technique
   ↓
Required Data
   ↓
Detection
   ↓
Test
   ↓
Coverage
```

---

# 71. Detection Engineering and Threat Hunting

Strong SOCs connect both disciplines:

```text
Threat Hunt
    ↓
New Behavior
    ↓
Detection
    ↓
Production
    ↓
Future Alert
    ↓
Investigation
    ↓
New Hunt
```

---

# 72. Detection Engineering and Purple Teaming

Purple teaming validates:

```text
Threat
 ↓
Attack Simulation
 ↓
Telemetry
 ↓
Detection
 ↓
Alert
 ↓
Investigation
```

This identifies:

```text
Detection Gaps
Telemetry Gaps
Logic Gaps
Response Gaps
```

---

# 73. Detection Engineering and Incident Response

Incident response provides valuable feedback.

Example:

```text
Incident
 ↓
Attacker Used Technique X
 ↓
No Detection
 ↓
Detection Gap
 ↓
Build Detection
 ↓
Test
 ↓
Deploy
```

---

# 74. Common Detection Engineering Mistakes

## Mistake 1

```text
Create Rule
→ Deploy
→ Forget
```

Correct:

```text
Create
→ Test
→ Deploy
→ Monitor
→ Tune
→ Review
```

---

## Mistake 2

```text
Use only IOCs
```

Problem:

```text
Attackers Change Indicators
```

Better:

```text
IOC
+
Behavior
+
Context
```

---

## Mistake 3

```text
Alert on Everything Suspicious
```

Result:

```text
Alert Fatigue
```

---

## Mistake 4

```text
Broad Exclusions
```

Result:

```text
Blind Spots
```

---

## Mistake 5

```text
No Testing
```

Result:

```text
Unknown Detection Quality
```

---

## Mistake 6

```text
No Documentation
```

Result:

```text
Nobody Understands the Rule
```

---

## Mistake 7

```text
No Owner
```

Result:

```text
Detection Becomes Orphaned
```

---

# 75. Detection Ownership

Every important production detection should have an owner.

Owner responsibilities:

```text
Maintain
Review
Tune
Test
Document
Respond to Failures
Retire When Necessary
```

---

# 76. Detection Status

Useful statuses:

```text
Experimental
Development
Testing
Staging
Production
Deprecated
Retired
```

---

# 77. Detection Versioning

Example:

```text
v1.0
Initial Detection

v1.1
Added Context

v1.2
Reduced False Positives

v2.0
Changed Detection Logic
```

Versioning supports:

```text
Auditability
Rollback
Change Tracking
Testing
```

---

# 78. Detection Retirement

Retire a detection when:

```text
Threat No Longer Relevant
+
Telemetry Removed
+
Replacement Detection Exists
+
Rule Provides Little Value
```

Before retirement:

```text
Review
 ↓
Check Dependencies
 ↓
Measure Usage
 ↓
Document
 ↓
Disable
 ↓
Monitor
```

---

# 79. Detection Engineering Architecture

Conceptually:

```text
                 THREAT INTELLIGENCE
                         │
                         ▼
                    THREAT MODEL
                         │
                         ▼
                  DETECTION DESIGN
                         │
                         ▼
                     TELEMETRY
                         │
                         ▼
                  DETECTION CODE
                         │
                         ▼
                     TESTING
                         │
                         ▼
                   CODE REVIEW
                         │
                         ▼
                     CI/CD
                         │
                         ▼
                    PRODUCTION
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
          MONITORING              SOC
              │                     │
              └──────────┬──────────┘
                         ▼
                       FEEDBACK
                         │
                         └──────────────►
```

---

# 80. Practical Example – Brute Force Detection

## Threat

```text
Credential Attack
```

## Behavior

```text
Repeated Authentication Failures
```

## Telemetry

```text
Timestamp
Username
Source IP
Destination
Result
Authentication Method
```

## Detection

```text
IF

failed_attempts >= 20

WITHIN

5 minutes

GROUP BY

username + source_ip

THEN

generate alert
```

## Context

Add:

```text
Privileged Account?
Known Scanner?
Known VPN?
Known Corporate NAT?
```

## Test

```text
19 failures → No Alert
20 failures → Alert
21 failures → Alert
Legitimate Authentication → No Alert
```

---

# 81. Practical Example – Suspicious PowerShell

## Threat

```text
Malicious Script Execution
```

## Telemetry

```text
Process
Parent Process
Command Line
User
Host
Network
```

## Detection Concept

```text
PowerShell
+
Suspicious Command Characteristics
+
Unusual Parent
+
External Network
```

The exact logic should be validated against the organization's environment.

---

# 82. Practical Example – Account Compromise

```text
Multiple Failed Logins
        ↓
Successful Login
        ↓
New Device
        ↓
MFA Change
        ↓
Privilege Change
```

Rather than creating five unrelated alerts:

```text
Correlate
 ↓
Risk Score
 ↓
High-Priority Investigation
```

---

# 83. Practical Example – Ransomware

Potential telemetry:

```text
Process Creation
File Modification
File Rename
Shadow Copy Changes
Endpoint Security Events
Network Authentication
```

Potential correlation:

```text
Suspicious Process
+
Mass File Changes
+
Backup Tampering
```

↓

```text
High-Risk Ransomware Candidate
```

---

# 84. Practical Example – Cloud Account Takeover

Telemetry:

```text
Cloud Authentication
Cloud IAM
API Calls
MFA
Resource Access
```

Potential sequence:

```text
Unusual Login
 ↓
MFA Modification
 ↓
Privilege Change
 ↓
New Access Key
 ↓
Sensitive API Calls
```

---

# 85. Detection Engineering Checklist

Before production:

```text
[ ] Threat clearly defined
[ ] Behavior understood
[ ] Required telemetry identified
[ ] Detection hypothesis documented
[ ] Detection logic implemented
[ ] Positive test created
[ ] Negative test created
[ ] Boundary cases tested
[ ] Missing data tested
[ ] Performance tested
[ ] False positives analyzed
[ ] ATT&CK mapping reviewed
[ ] Severity assigned
[ ] Confidence assigned
[ ] Documentation completed
[ ] Owner assigned
[ ] Code reviewed
[ ] Deployment plan created
[ ] Rollback plan available
```

---

# 86. Production Checklist

After deployment:

```text
[ ] Alert volume monitored
[ ] False positives monitored
[ ] Detection latency monitored
[ ] Query performance monitored
[ ] Data source health monitored
[ ] Analyst feedback collected
[ ] Detection coverage measured
[ ] Periodic review scheduled
[ ] Dependencies monitored
[ ] Version documented
```

---

# 87. Detection Engineering Mental Model

Remember:

```text
THREAT
  ↓
BEHAVIOR
  ↓
TELEMETRY
  ↓
HYPOTHESIS
  ↓
LOGIC
  ↓
TEST
  ↓
VALIDATE
  ↓
DEPLOY
  ↓
MONITOR
  ↓
TUNE
  ↓
MEASURE
  ↓
IMPROVE
```

---

# 88. Interview Questions

### 1. What is detection engineering?

> Detection engineering is the process of designing, developing, testing, deploying, tuning, and maintaining security detections that identify meaningful adversary behavior.

### 2. What is the first step when creating a detection?

> Understand the threat and attacker behavior before determining the telemetry and detection logic.

### 3. What is a detection hypothesis?

> A statement describing what observable behavior or evidence would indicate that a particular threat may be occurring.

### 4. Why is telemetry important?

> A detection can only identify behavior that is sufficiently observable in the available telemetry.

### 5. What is detection coverage?

> The extent to which relevant threats, techniques, assets, and behaviors are observable and detectable.

### 6. What is a false positive?

> A detection triggers on legitimate activity.

### 7. What is a false negative?

> Malicious activity occurs but the detection fails to identify it.

### 8. How do you reduce false positives?

> Add context, improve correlation, tune thresholds, use narrow exceptions, enrich events, and validate changes with testing.

### 9. Why shouldn't you simply disable a noisy detection?

> It may eliminate useful visibility and create a detection blind spot.

### 10. What is detection-as-code?

> Managing detections as version-controlled, testable, reviewable software artifacts.

### 11. Why use Git for detections?

> It provides version control, collaboration, peer review, auditability, and rollback.

### 12. How do you validate a detection?

> Use positive and negative tests, historical data, attack simulation, threat hunting, or purple-team exercises.

### 13. What is purple teaming?

> A collaborative process where offensive and defensive teams validate whether attacker behaviors are visible and detectable.

### 14. What is the difference between severity and confidence?

> Severity represents potential impact, while confidence represents how strongly the evidence indicates malicious activity.

### 15. What makes a good detection?

> It should be accurate, actionable, tested, maintainable, performant, threat-relevant, and resilient to reasonable environmental changes.

---

# 89. Quick Revision

```text
Detection Engineering
→ Build and maintain security detections

Detection
→ Logic identifying suspicious behavior

Telemetry
→ Observable security data

Detection Hypothesis
→ Expected evidence of a threat

False Positive
→ Legitimate activity triggers detection

False Negative
→ Malicious activity is missed

Precision
→ How many alerts are actually useful

Recall
→ How much relevant malicious activity is detected

Correlation
→ Combine multiple signals

Behavioral Detection
→ Detect suspicious behavior patterns

Detection-as-Code
→ Version-controlled detection logic

Purple Teaming
→ Validate detections using attack simulation

Detection Coverage
→ What threats/techniques can be detected

Detection Tuning
→ Improve quality and reduce noise

Detection Lifecycle
→ Create → Test → Deploy → Monitor → Tune → Retire
```

---

# 90. Golden Rules

```text
1. Start with the threat, not the query.

2. Understand attacker behavior before writing detection logic.

3. Identify required telemetry before implementing the rule.

4. No telemetry means no reliable detection.

5. Prefer meaningful behavior over static indicators when appropriate.

6. Combine weak signals when correlation can increase confidence.

7. Always test positive and negative scenarios.

8. Test edge cases and missing data.

9. Never blindly trust a detection because it executes successfully.

10. Monitor detections after production deployment.

11. Tune false positives without creating broad blind spots.

12. Version-control detection logic.

13. Peer-review important production detections.

14. Document every important detection.

15. Assign an owner.

16. Map relevant detections to ATT&CK.

17. Measure detection coverage.

18. Validate detections through attack simulation where possible.

19. Design detections with attacker evasion in mind.

20. Optimize query performance.

21. Treat telemetry changes as potential detection-breaking changes.

22. Revalidate detections after platform or schema changes.

23. Retire detections that no longer provide meaningful value.

24. Use AI as an engineering assistant, not as an unquestioned authority.

25. A good detection should help an analyst make a better security decision.
```

---

# 91. Final Takeaway

Detection engineering can be summarized as:

```text
Understand the Threat
        ↓
Understand the Behavior
        ↓
Find the Telemetry
        ↓
Build the Detection
        ↓
Test the Detection
        ↓
Validate Against Realistic Behavior
        ↓
Deploy Safely
        ↓
Monitor
        ↓
Tune
        ↓
Measure
        ↓
Continuously Improve
```

The most important mindset is:

> **A detection is not finished when the rule works. It is finished only when it reliably detects meaningful behavior, produces actionable results, survives testing, performs effectively in production, and can be maintained over time.**

---

# 92. Chapter Summary

This chapter established the foundation for the rest of the Detection Engineering section.

You should now understand:

```text
What Detection Engineering is
        ↓
Why it matters
        ↓
How detections are designed
        ↓
How telemetry supports detection
        ↓
How detection logic is developed
        ↓
How detections are tested
        ↓
How they are validated
        ↓
How they are deployed
        ↓
How they are tuned
        ↓
How their effectiveness is measured
        ↓
How detections evolve throughout their lifecycle
```

The next chapters will progressively move from these fundamentals into **telemetry engineering, detection logic, detection methodologies, behavioral analytics, correlation, MITRE ATT&CK, Detection-as-Code, testing, tuning, cloud detection, and advanced modern detection engineering**.