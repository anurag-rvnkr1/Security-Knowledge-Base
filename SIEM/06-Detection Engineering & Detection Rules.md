# Chapter 06 – Detection Engineering & Detection Rules

> Detection engineering is the discipline of converting security knowledge, threat intelligence, attack behaviors, and telemetry into reliable, testable, maintainable detections that identify malicious or suspicious activity while minimizing false positives.

---

# 1. Introduction

A SIEM becomes useful when it can continuously answer:

```text
"Is something suspicious happening right now?"
```

Instead of relying on an analyst to manually search every event, detection engineering turns investigation logic into automated rules.

The basic lifecycle is:

```text
Threat
  ↓
Behavior
  ↓
Hypothesis
  ↓
Telemetry
  ↓
Query
  ↓
Detection Logic
  ↓
Testing
  ↓
Deployment
  ↓
Alert
  ↓
Tuning
  ↓
Continuous Improvement
```

---

# 2. What is Detection Engineering?

Detection engineering is the process of designing and maintaining detections that identify potentially malicious or otherwise security-relevant behavior.

It combines:

```text
Threat Intelligence
+
MITRE ATT&CK
+
Security Research
+
Log Analysis
+
Query Engineering
+
Detection Logic
+
Testing
+
Operational Feedback
```

---

# 3. Detection vs Alert

These terms are related but different.

### Detection

The logic used to identify suspicious behavior.

```text
IF
multiple authentication failures
occur from one source
within a short time window
```

### Alert

The operational notification generated when the detection condition is satisfied.

```text
Alert:
Possible Brute Force Attack
```

Therefore:

```text
Detection
    ↓
Condition Match
    ↓
Alert
```

---

# 4. Why Detection Engineering Matters

Good detection engineering provides:

```text
Early Threat Identification
Consistent Monitoring
Reduced Analyst Workload
Repeatable Investigation
Improved Detection Coverage
Faster Response
Measurable Security Capability
```

Poor detection engineering creates:

```text
Alert Fatigue
False Positives
Missed Attacks
Duplicate Alerts
Unmaintainable Rules
Poor SOC Efficiency
```

---

# 5. Detection Engineering Mindset

A good detection engineer asks:

```text
What behavior am I trying to detect?

Why is this behavior suspicious?

Which telemetry shows it?

What fields are required?

What legitimate activity looks similar?

How can I reduce false positives?

How can I test the rule?

What happens when the data format changes?
```

---

# 6. Detection Lifecycle

A mature detection lifecycle looks like:

```text
1. Identify Threat

2. Define Behavior

3. Identify Telemetry

4. Build Hypothesis

5. Explore Data

6. Write Query

7. Validate Pattern

8. Create Detection

9. Test Detection

10. Tune Detection

11. Deploy

12. Monitor

13. Review

14. Retire or Improve
```

---

# 7. Step 1 – Identify the Threat

Start with:

```text
Threat
```

Examples:

```text
Brute Force
Password Spraying
Malware
Credential Theft
PowerShell Abuse
Lateral Movement
Data Exfiltration
Persistence
Privilege Escalation
Cloud Account Abuse
```

---

# 8. Step 2 – Define the Behavior

Avoid overly broad statements such as:

```text
"Detect attackers."
```

Instead:

```text
"Detect repeated authentication failures
against multiple users from one source."
```

This is measurable.

---

# 9. Step 3 – Identify Telemetry

Determine which data sources can observe the behavior.

Example:

```text
Password Spraying
       ↓
Identity Logs
       ↓
Authentication Events
```

Potential sources:

```text
Active Directory
Cloud Identity
VPN
SSO
Endpoint
Firewall
```

---

# 10. Step 4 – Define Required Fields

For a password-spraying detection:

```text
@timestamp
source.ip
user.name
event.category
event.outcome
```

Potential additional fields:

```text
host.name
authentication.method
application
geo
device
```

---

# 11. Step 5 – Explore the Data

Before writing a production rule:

```text
Search Historical Events
        ↓
Understand Normal Behavior
        ↓
Find Suspicious Pattern
        ↓
Identify Edge Cases
```

This prevents building detections based on assumptions.

---

# 12. Step 6 – Write the Query

Example:

```text
event.category = authentication
AND
event.outcome = failure
```

Then aggregate:

```text
GROUP BY source.ip
```

Calculate:

```text
COUNT(events)
COUNT(DISTINCT user.name)
```

---

# 13. Step 7 – Define Threshold

Example:

```text
More than 20 failures
```

But threshold selection should be evidence-based.

Instead of randomly choosing:

```text
20
```

analyze:

```text
Normal failure rates
Peak hours
User behavior
Service accounts
Applications
Historical incidents
```

---

# 14. Step 8 – Add a Time Window

Example:

```text
20 failures
within 5 minutes
```

The complete logic becomes:

```text
IF

authentication failures > 20

AND

unique users > 5

FROM

same source.ip

WITHIN

5 minutes

THEN

generate alert
```

---

# 15. Detection Logic

A detection can be represented as:

```text
INPUT
  ↓
FILTER
  ↓
GROUP
  ↓
AGGREGATE
  ↓
THRESHOLD
  ↓
CONTEXT
  ↓
DECISION
  ↓
ALERT
```

---

# 16. Detection Types

Common detection categories include:

```text
Threshold-Based
Rule-Based
Signature-Based
Behavioral
Anomaly-Based
Statistical
Sequence-Based
Correlation-Based
IOC-Based
Risk-Based
Threat-Intelligence-Based
Machine-Learning-Assisted
```

---

# 17. Signature-Based Detection

Looks for known patterns.

Example:

```text
file.hash.sha256 = known_malicious_hash
```

Advantages:

```text
Simple
Fast
High Precision for Known Indicators
```

Limitations:

```text
Cannot reliably detect unknown variants
Indicators can change
Attackers can modify artifacts
```

---

# 18. IOC-Based Detection

IOC:

```text
Indicator of Compromise
```

Examples:

```text
IP
Domain
URL
File Hash
Email Address
Certificate
```

Detection:

```text
source.ip IN threat_intelligence.ip_list
```

---

# 19. Rule-Based Detection

Example:

```text
IF
new_admin_account = true

THEN
alert
```

This is straightforward and deterministic.

---

# 20. Threshold Detection

Example:

```text
IF
failed_login_count > 50
WITHIN
5 minutes
THEN
alert
```

Useful for:

```text
Brute Force
Scanning
Flooding
Repeated Errors
Abuse
```

---

# 21. Behavioral Detection

Instead of matching a specific indicator, detect behavior.

Example:

```text
Office
  ↓
PowerShell
  ↓
Network Connection
```

The exact file hash or IP may change, but the behavior may remain.

Behavior-based detection can therefore be more resilient to indicator changes.

---

# 22. Sequence Detection

Sequence detections look for events occurring in a particular order.

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

This may indicate account compromise.

---

# 23. Stateful Detection

A stateful rule tracks events over time.

Example:

```text
User Alice

Failed Login = 5
Successful Login = 1
Admin Role Change = 1
```

The detection maintains context across events.

---

# 24. Stateless Detection

A stateless detection evaluates one event at a time.

Example:

```text
event.action = malware_detected
```

↓

```text
Alert
```

No historical context is required.

---

# 25. Anomaly Detection

Anomaly detection identifies activity that differs significantly from expected behavior.

Example:

```text
Normal:
5 login attempts/day

Observed:
500 login attempts
```

Potential anomaly.

---

# 26. Baseline-Based Detection

Example:

```text
User normally logs in:
09:00–18:00

Observed:
02:00
```

Possible anomaly.

Baseline-based detection requires enough historical data and careful handling of legitimate changes.

---

# 27. Statistical Detection

Example:

```text
Average:
10 connections/minute

Current:
500 connections/minute
```

The deviation may be significant.

Possible causes:

```text
Attack
Application Change
Backup
Monitoring
Misconfiguration
```

Statistical deviation requires context.

---

# 28. Detection Using Multiple Signals

A stronger detection may combine:

```text
Authentication Anomaly
+
Endpoint Anomaly
+
Network Anomaly
```

Example:

```text
Unusual Login
+
Suspicious PowerShell
+
Rare External Connection
```

↓

```text
Higher Confidence
```

---

# 29. Detection Confidence

Not every alert has the same confidence.

Example:

```text
Known malicious hash:
High confidence

Suspicious PowerShell:
Medium confidence

Unusual login time:
Low confidence
```

Confidence can be used alongside severity and risk.

---

# 30. Severity

Common severity levels:

```text
Informational
Low
Medium
High
Critical
```

Severity should reflect potential impact and urgency.

---

# 31. Severity vs Confidence

These are different.

### Severity

How serious could the activity be?

### Confidence

How confident are we that the activity is malicious?

Example:

```text
Critical severity
+
Low confidence
```

could mean:

```text
Potentially devastating behavior,
but evidence is weak.
```

---

# 32. Risk-Based Detection

Risk combines multiple signals.

Example:

```text
Suspicious Login          +20
Malicious IP              +40
Privilege Escalation      +50
Critical Server           +30
```

Total:

```text
140
```

The organization can prioritize based on risk.

---

# 33. Detection Context

A detection should include enough information for investigation.

Bad:

```text
"Suspicious Login"
```

Better:

```text
User:
alice

Source IP:
203.0.113.10

Host:
VPN01

Time:
10:15 UTC

Failures:
35

Unique Users:
12
```

---

# 34. Alert Enrichment

Alerts can be enriched with:

```text
Asset Criticality
User Role
Threat Intelligence
GeoIP
Vulnerability
MITRE ATT&CK
Previous Alerts
Related Cases
```

This reduces analyst lookup time.

---

# 35. False Positive

A false positive occurs when a detection alerts on legitimate activity.

Example:

```text
Backup system
generates 10,000 authentication requests
```

Detection:

```text
High authentication failures
```

↓

```text
Alert
```

But activity is legitimate.

---

# 36. False Negative

A false negative occurs when malicious activity is not detected.

Example:

```text
Attacker performs slow password spraying
```

Detection:

```text
50 failures in 5 minutes
```

Attacker:

```text
5 failures/hour
```

↓

```text
Detection misses it
```

---

# 37. Detection Trade-Off

There is often a trade-off:

```text
High Sensitivity
     ↓
More Alerts
     ↓
More False Positives
```

while:

```text
High Specificity
     ↓
Fewer Alerts
     ↓
Potential Missed Attacks
```

Good detection engineering balances:

```text
Coverage
Precision
Operational Cost
Risk
```

---

# 38. Precision

Precision asks:

> Of the alerts generated, how many are actually relevant/true positives?

Conceptually:

```text
Precision =
True Positives /
(True Positives + False Positives)
```

Higher precision generally means less alert noise.

---

# 39. Recall

Recall asks:

> Of all actual malicious events, how many did the detection identify?

Conceptually:

```text
Recall =
True Positives /
(True Positives + False Negatives)
```

---

# 40. Detection Coverage

Coverage asks:

```text
What threats or behaviors can we detect?
```

Example:

```text
Initial Access       ✓
Execution            ✓
Persistence           ✓
Privilege Escalation  ✓
Defense Evasion       ?
Credential Access     ✓
Discovery             ✓
Lateral Movement      ?
Exfiltration          ?
```

Coverage should be measured against relevant threats and telemetry.

---

# 41. Detection Gaps

A gap exists when:

```text
Threat Behavior
       ↓
No Reliable Telemetry
```

or:

```text
Telemetry
       ↓
No Detection
```

Example:

```text
Credential Dumping
       ↓
Endpoint telemetry exists
       ↓
No detection
```

---

# 42. Detection Dependencies

A detection may depend on:

```text
Log Source
Parser
Normalized Field
Threat Intelligence
Asset Inventory
Identity Data
Time Synchronization
```

If a dependency fails:

```text
Detection Reliability ↓
```

---

# 43. Detection Metadata

A production detection should contain metadata such as:

```text
Detection ID
Name
Description
Severity
Confidence
Author
Version
Created Date
Updated Date
Data Sources
Required Fields
MITRE Technique
References
False Positive Guidance
Response Guidance
```

---

# 44. Detection ID

Example:

```text
DET-AUTH-001
```

or:

```text
SOC-AD-PS-001
```

A unique identifier makes detections easier to:

```text
Track
Version
Test
Reference
Retire
```

---

# 45. Detection Description

Bad:

```text
Detect brute force.
```

Better:

```text
Detects a high volume of authentication
failures originating from the same source
against multiple accounts within a short
time window.
```

---

# 46. Required Data Sources

Example:

```text
Primary:
Identity Authentication Logs

Optional:
VPN
EDR
Firewall
Threat Intelligence
```

This helps troubleshoot missing telemetry.

---

# 47. Required Fields

Example:

```text
source.ip
user.name
event.outcome
event.category
@timestamp
```

A detection should fail safely or degrade gracefully when required fields are unavailable.

---

# 48. False Positive Guidance

Example:

```text
Possible legitimate sources:

- Vulnerability scanners
- Monitoring systems
- Identity synchronization
- Automated applications
```

The analyst should know what to verify.

---

# 49. Exception Handling

Some legitimate entities may need exceptions.

Example:

```text
Scanner IP:
10.10.10.50
```

But avoid broad permanent exclusions.

Prefer:

```text
Narrow Scope
+
Documented Reason
+
Expiration
+
Review
```

---

# 50. Allowlists

Example:

```text
Known Security Scanner
```

may be excluded from a brute-force detection.

However:

> Allowlists can create blind spots if attackers compromise or abuse trusted infrastructure.

Therefore they should be:

```text
Minimal
Documented
Reviewed
Monitored
```

---

# 51. Detection Tuning

Tuning modifies a detection to improve its usefulness.

Examples:

```text
Change threshold
Change time window
Add context
Exclude known benign source
Require multiple signals
Change severity
```

---

# 52. Threshold Tuning

Initial:

```text
> 10 failures / 5 minutes
```

Produces:

```text
500 alerts/day
```

After analysis:

```text
> 30 failures / 5 minutes
```

Produces:

```text
40 alerts/day
```

But tuning should not simply reduce alert count. It should preserve meaningful detection coverage.

---

# 53. Contextual Tuning

Instead of:

```text
PowerShell execution
```

use:

```text
PowerShell execution
+
Encoded command
+
Network connection
```

This can improve precision.

---

# 54. Risk-Based Tuning

A suspicious action on:

```text
Critical Domain Controller
```

may deserve higher priority than the same action on:

```text
Test Workstation
```

Context matters.

---

# 55. Detection Testing

Never deploy a detection without testing.

Test:

```text
True Positive
False Positive
Edge Case
Missing Data
Delayed Data
Duplicate Data
Legitimate Similar Behavior
```

---

# 56. Positive Test

Generate expected malicious/suspicious behavior.

Example:

```text
20 authentication failures
from one IP
against multiple users
```

Expected:

```text
Detection triggers
```

---

# 57. Negative Test

Generate legitimate behavior.

Example:

```text
Normal user authentication
```

Expected:

```text
No alert
```

---

# 58. Edge Case Test

Example:

```text
19 failures
```

If threshold is:

```text
> 20
```

Expected:

```text
No alert
```

Then test:

```text
21 failures
```

Expected:

```text
Alert
```

---

# 59. Boundary Testing

If threshold:

```text
>= 20
```

test:

```text
19
20
21
```

This catches logic errors.

---

# 60. Detection Test Data

Possible sources:

```text
Synthetic Events
Replay Logs
Controlled Lab Activity
Atomic Red Team
Caldera
Purple Team Exercises
Historical Incidents
```

Only use security testing tools and activities within authorized environments.

---

# 61. Detection as Code

Detection rules can be stored as code/configuration.

Example:

```yaml
name: Password Spraying
severity: high

query: |
  authentication failures
  grouped by source.ip

threshold:
  failures: 20
  unique_users: 5

window:
  minutes: 5
```

Benefits:

```text
Version Control
Code Review
Testing
Rollback
Automation
Auditability
```

---

# 62. Version Control

Example:

```text
Detection v1
 ↓
Threshold change
 ↓
Detection v2
 ↓
Additional context
 ↓
Detection v3
```

History should remain available.

---

# 63. Detection CI/CD

A mature workflow:

```text
Developer
   ↓
Detection Code
   ↓
Git
   ↓
Automated Tests
   ↓
Peer Review
   ↓
Validation
   ↓
Deployment
   ↓
Production
```

---

# 64. Detection Unit Tests

Tests can verify:

```text
Expected Match
Expected No Match
Required Fields
Threshold
Time Window
Exceptions
```

Example:

```text
Input:
21 failures

Expected:
Alert
```

---

# 65. Regression Testing

A detection that worked previously may break after:

```text
Parser Update
Schema Change
SIEM Upgrade
Field Mapping Change
Rule Modification
```

Regression tests ensure previous behavior remains valid.

---

# 66. Detection Monitoring

After deployment, monitor:

```text
Alert Volume
False Positive Rate
True Positive Rate
Execution Errors
Query Latency
Data Availability
Coverage
Analyst Feedback
```

---

# 67. Alert Volume Monitoring

Example:

```text
Monday:
100 alerts

Tuesday:
110 alerts

Wednesday:
105 alerts

Thursday:
8,000 alerts
```

Possible cause:

```text
Data Change
Parser Change
Detection Bug
Attack
```

Investigate before assuming an attack.

---

# 68. Detection Health

A detection can be logically correct but operationally broken.

Example:

```text
Detection requires:
source.ip
```

Parser changes:

```text
source.ip → client.ip
```

Detection:

```text
No results
```

Therefore:

```text
Detection Health
+
Data Health
```

must both be monitored.

---

# 69. Detection Drift

Detection drift occurs when the environment changes and the detection becomes less effective.

Examples:

```text
New Cloud Platform
New Authentication System
New Application
New Network Architecture
New Attacker Technique
```

Detections should be periodically reviewed.

---

# 70. Detection Retirement

A detection may become obsolete.

Reasons:

```text
Technology Removed
Threat No Longer Relevant
Better Detection Replaced It
Data Source Removed
High False Positive Rate
Duplicate Coverage
```

Retirement should be documented.

---

# 71. Detection Catalog

A mature SOC maintains a catalog:

```text
Detection ID
Detection Name
Threat
MITRE Technique
Data Source
Severity
Owner
Status
Version
Last Reviewed
Performance
```

---

# 72. Detection Ownership

Each production detection should have an owner.

Example:

```text
Detection:
Suspicious PowerShell

Owner:
Detection Engineering Team
```

Owner responsibilities:

```text
Maintain
Tune
Test
Review
Retire
```

---

# 73. Detection Review

Review periodically:

```text
Does it still work?

Is telemetry available?

Are false positives acceptable?

Does the threat still matter?

Can it be improved?

Does another detection cover the same behavior?
```

---

# 74. Detection Naming

Good:

```text
Windows – Suspicious PowerShell Encoded Command
```

Poor:

```text
Rule123
```

Names should be:

```text
Descriptive
Consistent
Searchable
```

---

# 75. Detection Categories

Useful categories:

```text
Authentication
Endpoint
Network
Cloud
Identity
Email
Application
Data Security
Privilege
Malware
Persistence
Lateral Movement
Exfiltration
```

---

# 76. Example Detection – Brute Force

```text
Name:
Multiple Authentication Failures

Logic:
authentication failure
+
same source.ip
+
>20 events
+
5-minute window

Severity:
Medium/High

Potential False Positives:
Monitoring
Misconfigured applications
Users repeatedly entering wrong passwords
```

---

# 77. Example Detection – Password Spraying

```text
Name:
Potential Password Spraying

Logic:
authentication failures
+
same source.ip
+
multiple unique users
+
short time window
```

Example:

```text
1 IP
50 failures
25 users
10 minutes
```

---

# 78. Example Detection – New Admin Account

```text
event.action = account_created
AND
new account assigned privileged role
```

Potential severity:

```text
High
```

Context:

```text
Who created it?
Which account?
Which host?
Which administrator?
Was there a change ticket?
```

---

# 79. Example Detection – Privilege Escalation

```text
Normal User
      ↓
Admin Group Added
      ↓
Privileged Account
```

Detection:

```text
Group membership change
+
privileged group
```

---

# 80. Example Detection – Suspicious PowerShell

Potential signals:

```text
process.name = powershell.exe

AND

encoded command

AND/OR

suspicious parent process

AND/OR

external network connection
```

The exact combination should be validated against the environment.

---

# 81. Example Detection – Rare Process

Baseline:

```text
Host normally runs:
explorer.exe
chrome.exe
outlook.exe
```

New:

```text
unknown.exe
```

Potential detection:

```text
Rare process
+
unsigned executable
+
network connection
```

---

# 82. Example Detection – Suspicious DNS

Signals:

```text
Rare domain
+
high query frequency
+
long subdomain
+
unusual entropy
```

Potentially associated with:

```text
DNS Tunneling
```

But legitimate software can also generate unusual DNS patterns.

---

# 83. Example Detection – Impossible Travel

Example:

```text
Login A:
India
10:00

Login B:
USA
10:20
```

Potential anomaly.

Need to consider:

```text
VPN
Proxies
Cloud Services
Travel
GeoIP Accuracy
Shared Accounts
```

---

# 84. Example Detection – Data Exfiltration

Signals:

```text
Large outbound transfer
+
unusual destination
+
rare user behavior
+
sensitive asset
```

This is stronger than simply:

```text
Large Transfer
```

---

# 85. Example Detection – Defense Evasion

Potential signals:

```text
Security Tool Disabled
+
Service Stop
+
Audit Policy Change
```

This may indicate attempts to weaken visibility.

---

# 86. Detection Chaining

Multiple detections can feed a higher-level detection.

```text
Detection A:
Suspicious Login

Detection B:
PowerShell

Detection C:
Credential Change

        ↓

Higher-Level Detection:
Possible Account Compromise
```

---

# 87. Detection Pyramid

A useful conceptual model:

```text
                 Behavioral
                  Detection
                     ▲
                     │
               Correlation
                     ▲
                     │
              Rule / Threshold
                     ▲
                     │
                 IOC Match
                     ▲
                     │
                 Raw Events
```

Higher layers generally provide more context but may require more data and engineering.

---

# 88. Detection Quality Metrics

Important metrics include:

```text
Alert Volume
True Positive Rate
False Positive Rate
Precision
Recall
Mean Time to Detect
Mean Time to Triage
Detection Coverage
Data Availability
Rule Execution Errors
```

---

# 89. Mean Time to Detect

MTTD:

```text
Time Attack Occurs
        ↓
Detection Generated
```

Lower is generally better for time-sensitive threats.

---

# 90. Mean Time to Triage

MTTT can be thought of as:

```text
Alert Generated
        ↓
Analyst Determines Significance
```

Good alert context can reduce this time.

---

# 91. Mean Time to Respond

MTTR is commonly used for:

```text
Detection/Incident
       ↓
Response
```

Organizations define the exact measurement differently.

---

# 92. Detection Engineering and SOC

Detection engineers:

```text
Build
Test
Tune
Maintain
```

SOC analysts:

```text
Monitor
Investigate
Triage
Respond
```

Strong feedback between both roles improves detection quality.

---

# 93. Analyst Feedback Loop

```text
Detection
   ↓
Alert
   ↓
Analyst
   ↓
Investigation
   ↓
False Positive / True Positive
   ↓
Feedback
   ↓
Detection Engineering
   ↓
Tuning
```

This feedback loop is essential.

---

# 94. Production Detection Checklist

Before deployment:

```text
☐ Clear threat objective
☐ Defined behavior
☐ Required telemetry
☐ Required fields
☐ Query tested
☐ Positive test passed
☐ Negative test passed
☐ Boundary tests passed
☐ False positives evaluated
☐ Severity assigned
☐ MITRE mapping considered
☐ Investigation context included
☐ Owner assigned
☐ Documentation complete
☐ Version recorded
☐ Monitoring enabled
```

---

# 95. Practical Lab

Build a password-spraying detection.

## Step 1

Search:

```text
authentication failures
```

## Step 2

Group by:

```text
source.ip
```

## Step 3

Calculate:

```text
failure count
unique users
```

## Step 4

Apply:

```text
failure count > threshold
```

## Step 5

Apply:

```text
unique users > threshold
```

## Step 6

Apply:

```text
time window
```

## Step 7

Test:

```text
Normal Login
Brute Force
Password Spray
Scanner
```

## Step 8

Tune.

## Step 9

Deploy.

---

# 96. Detection Development Example

```text
THREAT
Password Spraying

        ↓

BEHAVIOR
One source attacks many users

        ↓

TELEMETRY
Authentication Logs

        ↓

FIELDS
source.ip
user.name
event.outcome
@timestamp

        ↓

QUERY
Authentication failures

        ↓

AGGREGATION
Count + Unique Users

        ↓

THRESHOLD
High failure count
+
multiple users

        ↓

TEST
Attack + Benign

        ↓

TUNE

        ↓

DEPLOY

        ↓

MONITOR
```

---

# 97. Interview Questions

### What is detection engineering?

> The discipline of designing, testing, deploying, monitoring, and maintaining security detections based on threats, behaviors, telemetry, and investigation requirements.

### What is the difference between a detection and an alert?

> A detection is the logic that identifies suspicious activity; an alert is the operational output generated when that logic matches.

### What is a false positive?

> A legitimate event incorrectly identified as suspicious.

### What is a false negative?

> Malicious or relevant activity that the detection fails to identify.

### What is detection tuning?

> Modifying detection logic, thresholds, context, or exclusions to improve effectiveness and reduce unnecessary alerts without creating unacceptable visibility gaps.

### What is threshold-based detection?

> A detection that triggers when an event count or metric crosses a defined threshold within a specified period.

### What is behavioral detection?

> A detection based on suspicious activity patterns rather than only matching known indicators.

### What is stateful detection?

> A detection that maintains context across multiple events or over time.

### What is detection coverage?

> The threats, behaviors, or attack techniques that the organization's telemetry and detections can identify.

### Why is detection testing important?

> To verify that the rule detects intended behavior, avoids common legitimate behavior, and continues working after changes.

### What is detection as code?

> Managing detection rules as version-controlled code or configuration with testing, review, deployment, and rollback practices.

### Why should detections have owners?

> To ensure someone is responsible for maintenance, tuning, testing, and periodic review.

### What is detection drift?

> The gradual loss of detection effectiveness as infrastructure, telemetry, applications, or attacker behavior changes.

### What is precision?

> The proportion of generated alerts that are true/relevant positives.

### What is recall?

> The proportion of actual relevant malicious events that the detection successfully identifies.

### How would you reduce false positives?

> Analyze legitimate alert sources, add contextual conditions, improve thresholds, use asset/user context, create narrowly scoped exceptions, and continuously validate the detection.

---

# 98. Quick Revision

```text
DETECTION ENGINEERING
→ Build reliable security detections

THREAT
→ What are we trying to identify?

BEHAVIOR
→ What does the threat do?

TELEMETRY
→ Where can we observe it?

QUERY
→ How do we find it?

LOGIC
→ What conditions indicate suspicious activity?

THRESHOLD
→ How much activity is suspicious?

TIME WINDOW
→ Over what period?

CONTEXT
→ What additional information improves confidence?

TESTING
→ Does it actually work?

TUNING
→ Can we reduce noise without losing visibility?

DEPLOYMENT
→ Put it into production

MONITORING
→ Verify ongoing health

RETIREMENT
→ Remove obsolete detections
```

---

# 99. Golden Rules

```text
1. Start with a threat and behavior, not a random query.

2. Understand the telemetry before writing the rule.

3. Define required fields explicitly.

4. Use the smallest useful set of conditions.

5. Choose thresholds from observed behavior where possible.

6. Always consider a time window for rate-based detections.

7. Prefer behavioral detection when static indicators are insufficient.

8. Combine multiple signals when they meaningfully improve confidence.

9. Never solve every false positive with a broad allowlist.

10. Test both malicious and legitimate behavior.

11. Test boundary conditions.

12. Include investigation context in alerts.

13. Assign severity based on impact and confidence.

14. Document false-positive conditions.

15. Version-control important detections.

16. Monitor detection health after deployment.

17. Review detections as the environment changes.

18. Measure coverage and operational performance.

19. Retire detections that are obsolete or redundant.

20. A detection is not finished when it is deployed—it requires continuous maintenance.
```

---

# 100. Final Mental Model

Remember detection engineering as:

```text
THREAT
   ↓
BEHAVIOR
   ↓
TELEMETRY
   ↓
HYPOTHESIS
   ↓
SEARCH
   ↓
DETECTION LOGIC
   ↓
TEST
   ↓
TUNE
   ↓
DEPLOY
   ↓
ALERT
   ↓
ANALYST FEEDBACK
   ↓
IMPROVE
```

A production-quality detection should answer:

```text
What?
Why?
Where?
When?
Who?
How?
How confident?
How severe?
What telemetry?
What false positives?
What should the analyst do?
Who owns the rule?
When was it last tested?
```

---

# 101. Chapter Summary

Detection engineering transforms security knowledge into continuous monitoring capability.

The central workflow is:

```text
               THREAT
                  │
                  ▼
               BEHAVIOR
                  │
                  ▼
              TELEMETRY
                  │
                  ▼
               SEARCH
                  │
                  ▼
           DETECTION LOGIC
                  │
          ┌───────┴───────┐
          ▼               ▼
       POSITIVE         NEGATIVE
        TEST              TEST
          │               │
          └───────┬───────┘
                  ▼
                TUNE
                  │
                  ▼
               DEPLOY
                  │
                  ▼
                ALERT
                  │
                  ▼
             INVESTIGATE
                  │
                  ▼
               FEEDBACK
                  │
                  ▼
              IMPROVEMENT
```

The most important principle is:

> **A detection should be engineered as a security capability, not merely written as a query.**

A good detection is:

```text
Threat-Informed
Telemetry-Aware
Specific
Testable
Maintainable
Observable
Context-Rich
Operationally Useful
```

The next chapter builds on this by combining multiple detections and signals:

```text
Chapter 07 – Correlation Rules, Risk Scoring & Alerting
```

There we will move from **"this event is suspicious"** to **"these events together indicate a higher-confidence security threat"**, covering correlation logic, sequences, aggregation windows, risk scoring, alert prioritization, deduplication, suppression, alert grouping, escalation, and SOC alert management.