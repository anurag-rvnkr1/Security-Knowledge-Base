# Chapter 03 – Detection Logic, Rules & Query Development

> Detection logic is the core of detection engineering. It transforms raw security telemetry into conditions that identify suspicious behavior, prioritize risk, and generate actionable alerts.

---

# 1. What Is Detection Logic?

**Detection logic** is a set of conditions used to determine whether observed activity matches a security-relevant pattern.

Simplified:

```text
Telemetry
    ↓
Conditions
    ↓
Logic
    ↓
Detection Match
    ↓
Alert
```

Example:

```text
Failed Login
+
Same User
+
Many Attempts
+
Short Time Window
        ↓
Potential Brute Force
```

---

# 2. Detection Rule

A **detection rule** is an implemented representation of detection logic.

A rule usually defines:

```text
What to search
What conditions to apply
What time window to use
What entities to group
What severity to assign
What action to take
```

Example:

```text
IF

failed_login_count >= 20

WITHIN

5 minutes

GROUP BY

user + source_ip

THEN

generate alert
```

---

# 3. Detection Rule vs Query

These terms are related but different.

### Query

Retrieves or analyzes data.

```text
Search authentication events
where outcome = failure
```

### Detection Rule

Uses a query or equivalent logic to identify a security condition.

```text
IF failed attempts exceed threshold
THEN create security alert
```

Therefore:

```text
Query
→ Find Data

Detection Rule
→ Identify Security Condition
```

---

# 4. Detection Logic Pipeline

```text
Raw Events
    ↓
Field Selection
    ↓
Filtering
    ↓
Aggregation
    ↓
Correlation
    ↓
Threshold
    ↓
Context
    ↓
Risk
    ↓
Alert
```

---

# 5. Core Components of Detection Logic

Most detections contain some combination of:

```text
Data Source
Fields
Filters
Conditions
Operators
Threshold
Time Window
Grouping
Correlation
Enrichment
Severity
Risk
Exceptions
Actions
```

---

# 6. Data Source

First determine where the required information exists.

Example:

```text
Detection:
Password Spray

Data Source:
Authentication Logs
```

Another:

```text
Detection:
Suspicious PowerShell

Data Source:
Endpoint Process Telemetry
```

---

# 7. Fields

Fields represent attributes of an event.

Example:

```text
user.name
source.ip
destination.ip
process.name
process.command_line
event.action
event.outcome
```

A detection should depend on reliable fields.

---

# 8. Field Selection

Avoid selecting unnecessary fields.

Instead of:

```text
Search every field
```

prefer:

```text
event.action
user.name
source.ip
event.outcome
```

This improves:

```text
Readability
Performance
Maintainability
```

---

# 9. Filtering

Filtering narrows the dataset.

Example:

```text
event.action = "login"
```

Then:

```text
event.outcome = "failure"
```

Then:

```text
user.name = "alice"
```

Conceptually:

```text
All Events
   ↓
Authentication
   ↓
Failures
   ↓
Specific User
```

---

# 10. Logical Operators

Common operators:

```text
AND
OR
NOT
```

Example:

```text
event.action = login
AND
event.outcome = failure
```

---

# 11. AND

All conditions must match.

```text
A AND B
```

Example:

```text
PowerShell
AND
Encoded Command
```

---

# 12. OR

Any condition may match.

```text
A OR B
```

Example:

```text
powershell.exe
OR
pwsh.exe
```

---

# 13. NOT

Excludes a condition.

```text
A AND NOT B
```

Example:

```text
Suspicious Login
AND
NOT Known Scanner
```

Use exclusions carefully.

---

# 14. Parentheses

Parentheses control logic order.

Example:

```text
A AND (B OR C)
```

Without correct grouping:

```text
(A AND B) OR C
```

may produce very different results.

---

# 15. Comparison Operators

Common operators:

```text
=
!=
>
<
>=
<=
```

Example:

```text
failed_count >= 20
```

---

# 16. Membership Operators

Common concepts:

```text
IN
NOT IN
```

Example:

```text
process.name IN (
    powershell.exe,
    pwsh.exe,
    cmd.exe
)
```

---

# 17. Pattern Matching

Common approaches:

```text
Exact Match
Prefix Match
Substring
Wildcard
Regex
```

Example:

```text
process.name starts_with "powershell"
```

Pattern matching should be used carefully because expensive patterns can affect query performance.

---

# 18. Exact vs Partial Matching

### Exact

```text
process.name = "powershell.exe"
```

### Partial

```text
process.name contains "power"
```

Partial matching may detect more variations but can also increase false positives.

---

# 19. Regular Expressions

Regex can identify patterns.

Example concept:

```text
^powershell(\.exe)?$
```

Regex is useful for:

```text
Pattern Detection
URL Matching
Command-Line Patterns
File Names
```

But avoid unnecessary regex when structured fields are available.

---

# 20. Query Performance

A query should be:

```text
Correct
Readable
Efficient
```

Prefer:

```text
Time Filter
+
Structured Fields
+
Narrow Dataset
```

Avoid:

```text
Entire Dataset
+
Complex Regex
+
Large Historical Range
```

---

# 21. Time Windows

Many detections depend on time.

Example:

```text
20 failed logins
within 5 minutes
```

Time windows help distinguish:

```text
Normal Activity
vs
Rapid Suspicious Activity
```

---

# 22. Fixed Time Window

Example:

```text
5 minutes
```

Detection:

```text
>= 20 failures
within 5 minutes
```

---

# 23. Sliding Window

A sliding window continuously evaluates recent activity.

Conceptually:

```text
10:00 ───────── 10:05
       Window

10:01 ───────── 10:06
       Window

10:02 ───────── 10:07
       Window
```

Useful for continuous behavioral detection.

---

# 24. Event Time vs Processing Time

Two concepts:

```text
Event Time
→ When activity occurred

Processing Time
→ When detection evaluated it
```

Delayed telemetry can affect detection logic.

---

# 25. Aggregation

Aggregation summarizes multiple events.

Common operations:

```text
COUNT
UNIQUE COUNT
SUM
AVG
MIN
MAX
GROUP BY
```

---

# 26. COUNT

Example:

```text
COUNT(failed_logins)
```

Used for:

```text
Threshold Detection
```

---

# 27. Unique Count

Example:

```text
UNIQUE(source.ip)
```

Useful for:

```text
Many IPs
One User
```

Potential:

```text
Password Spraying
```

---

# 28. GROUP BY

Grouping identifies relationships.

Example:

```text
GROUP BY user.name
```

Then:

```text
COUNT(failures)
```

becomes:

```text
Alice → 25
Bob   → 2
Carol → 31
```

---

# 29. Multi-Entity Grouping

Example:

```text
GROUP BY
user.name + source.ip
```

This helps distinguish:

```text
One User
+
One Source
```

from broader activity.

---

# 30. Threshold Detection

Example:

```text
COUNT(failed_login)
>= 20
```

Thresholds are simple and effective when carefully selected.

---

# 31. Threshold Problems

Too low:

```text
Threshold = 3
```

Potential:

```text
Many False Positives
```

Too high:

```text
Threshold = 1000
```

Potential:

```text
Missed Attacks
```

Therefore threshold tuning is important.

---

# 32. Static Threshold

Example:

```text
Failed Logins >= 20
```

Simple but may not account for different users.

---

# 33. Dynamic Threshold

Compare behavior against a baseline.

Example:

```text
User normally:
5 login attempts/day

Observed:
80 attempts/day
```

Potential:

```text
Behavioral Anomaly
```

---

# 34. Baseline

A baseline represents expected behavior.

Examples:

```text
Normal Login Time
Normal Data Volume
Normal Destination
Normal Process
Normal Authentication Count
```

Detection:

```text
Observed Behavior
vs
Expected Baseline
```

---

# 35. Entity-Based Detection

Group behavior around:

```text
User
Host
IP
Account
Process
Application
Cloud Resource
```

Example:

```text
User Alice
+
New Device
+
Unusual Location
```

---

# 36. Sequence Detection

Some attacks occur as sequences.

Example:

```text
Event A
 ↓
Event B
 ↓
Event C
```

For account compromise:

```text
Failed Login
 ↓
Successful Login
 ↓
MFA Change
 ↓
Privilege Change
```

Sequence detection can be stronger than isolated rules.

---

# 37. Sequence Ordering

A proper sequence should consider:

```text
Order
Time
Entity
Relationship
```

Example:

```text
A before B
within 10 minutes
for same user
```

---

# 38. Correlation

Correlation combines events.

Example:

```text
Suspicious Login
+
New Device
+
Sensitive Resource Access
```

↓

```text
Higher Confidence
```

---

# 39. Event Correlation

Correlate events using:

```text
User
Host
IP
Session
Process
Resource
Transaction
```

---

# 40. Cross-Source Correlation

Example:

```text
Email
 ↓
Endpoint
 ↓
DNS
 ↓
Network
```

Potential attack chain:

```text
Phishing
 ↓
Execution
 ↓
C2
```

Cross-source correlation provides stronger context.

---

# 41. Correlation Key

A correlation key identifies events belonging together.

Examples:

```text
user.name
host.name
source.ip
session.id
process.entity_id
```

---

# 42. Entity Resolution

Different sources may represent the same entity differently.

Example:

```text
Windows:
DOMAIN\alice

Cloud:
alice@example.com

Application:
alice
```

Identity resolution may be required.

---

# 43. Contextual Detection

A detection becomes stronger when context is added.

Basic:

```text
Admin Login
```

Contextual:

```text
Admin Login
+
New Device
+
Unusual Location
+
After Hours
+
Rare Application
```

---

# 44. Detection Enrichment

Enrichment can include:

```text
Threat Intelligence
GeoIP
ASN
Asset Criticality
User Role
Device Trust
Vulnerability
Business Context
```

---

# 45. Risk-Based Detection

Instead of using a single condition:

```text
Risk =
Event
+
Context
+
History
+
Asset
+
Threat Intelligence
```

Example:

```text
Malicious IP        +40
Privileged User     +30
Critical Server     +30
Unusual Location    +20
```

Total:

```text
120
```

---

# 46. Risk Threshold

Example:

```text
Risk >= 100
```

↓

```text
High-Priority Alert
```

Risk thresholds should be calibrated to the organization's environment.

---

# 47. Detection Severity

Common:

```text
Informational
Low
Medium
High
Critical
```

Severity should consider:

```text
Potential Impact
Asset Criticality
Privilege
Attack Stage
Confidence
```

---

# 48. Severity vs Confidence

Example:

```text
Critical Severity
+
Low Confidence
```

means:

```text
Potentially serious
but uncertain
```

Do not confuse:

```text
Impact
```

with:

```text
Evidence Strength
```

---

# 49. Detection Confidence

Confidence reflects:

```text
How strongly the evidence supports
the detection hypothesis.
```

Example:

```text
IOC Match
+
Suspicious Process
+
Known Attack Technique
```

may provide higher confidence than a single anomaly.

---

# 50. Exceptions

Exceptions identify known legitimate activity.

Example:

```text
Known Vulnerability Scanner
```

might trigger:

```text
Port Scan Detection
```

Possible narrow exception:

```text
Known Scanner IP
+
Known Scan Window
```

---

# 51. Safe Exceptions

Good:

```text
Specific
Documented
Time-Bounded
Reviewed
```

Bad:

```text
Entire Network
Entire Organization
All Administrators
```

---

# 52. Suppression

Suppression reduces repeated alerts.

Example:

```text
100 identical events
```

instead of:

```text
100 alerts
```

produce:

```text
1 grouped alert
+
event count = 100
```

---

# 53. Deduplication

Deduplication prevents repeated alerts for the same underlying condition.

Common keys:

```text
Rule
User
Host
IP
Time Window
```

---

# 54. Alert Grouping

Example:

```text
Host A
 ├── Process Alert
 ├── Network Alert
 ├── DNS Alert
 └── File Alert
```

Group into:

```text
Potential Compromise – Host A
```

This reduces analyst workload.

---

# 55. Stateful Detection

Some detections require remembering previous events.

Example:

```text
Previous:
Failed Login

Current:
Successful Login
```

The detection must retain enough state to correlate the two.

---

# 56. Stateless Detection

A stateless detection evaluates the current event independently.

Example:

```text
Hash = Known Malicious Hash
```

No historical context required.

---

# 57. Stateful vs Stateless

```text
Stateless
→ Current Event

Stateful
→ Current Event + Previous Context
```

---

# 58. Detection Logic Example – Brute Force

Conceptual:

```text
WHERE
event.action = "login"
AND
event.outcome = "failure"

GROUP BY
user + source_ip

COUNT >= 20

WITHIN
5 minutes
```

---

# 59. Detection Logic Example – Password Spray

Conceptual:

```text
WHERE
authentication = failure

GROUP BY
source_ip

COUNT_UNIQUE(user) >= 10

WITHIN
10 minutes
```

Difference:

```text
Brute Force
→ Many attempts against one/few accounts

Password Spray
→ Attempts against many accounts
```

---

# 60. Detection Logic Example – Impossible Travel

Conceptual:

```text
Successful Login A
+
Successful Login B

Same User

Different Geographic Locations

Travel Time < Physically Plausible Time
```

Consider:

```text
VPN
Proxy
Mobile Networks
Geolocation Accuracy
```

before generating a high-confidence alert.

---

# 61. Detection Logic Example – Suspicious PowerShell

Conceptual:

```text
process.name = powershell.exe

AND

(
    suspicious command characteristic
    OR
    unusual parent process
    OR
    suspicious network behavior
)
```

A robust implementation should rely on validated behavioral indicators rather than simply alerting on all PowerShell usage.

---

# 62. Detection Logic Example – Data Exfiltration

Potential sequence:

```text
Sensitive Data Access
        ↓
Large Archive
        ↓
Large Outbound Transfer
        ↓
External Destination
```

Correlation improves confidence.

---

# 63. Query Development Workflow

Use:

```text
1. Define Threat
        ↓
2. Identify Telemetry
        ↓
3. Inspect Sample Events
        ↓
4. Identify Fields
        ↓
5. Build Simple Filter
        ↓
6. Add Conditions
        ↓
7. Add Aggregation
        ↓
8. Add Correlation
        ↓
9. Test
        ↓
10. Optimize
        ↓
11. Convert to Detection
```

---

# 64. Start With Sample Data

Before writing a complex query:

```text
Find Example Events
        ↓
Inspect Fields
        ↓
Understand Values
        ↓
Build Detection
```

This prevents assumptions about:

```text
Field Names
Data Types
Values
Formats
```

---

# 65. Query Development Strategy

Start simple:

```text
event.action = login
```

Then:

```text
event.action = login
AND
event.outcome = failure
```

Then:

```text
GROUP BY user
```

Then:

```text
COUNT > threshold
```

Then:

```text
TIME WINDOW
```

Then:

```text
CONTEXT
```

---

# 66. Avoid Overengineering

Bad approach:

```text
50 Conditions
+
Complex Regex
+
Multiple Nested Queries
```

when:

```text
5 Simple Conditions
```

would work.

Prefer:

```text
Simple
Readable
Testable
Maintainable
```

---

# 67. Query Readability

Bad:

```text
a=b AND c=d OR e=f AND NOT g=h
```

Better:

```text
(
    a = b
    AND
    c = d
)
OR
(
    e = f
    AND
    NOT g = h
)
```

Readability reduces logic mistakes.

---

# 68. Query Comments

Where supported, document:

```text
Why the condition exists
Why an exclusion exists
Why a threshold was selected
```

Example:

```text
# Exclude known vulnerability scanner
# because it performs authorized scanning
```

---

# 69. Query Testing Dataset

Useful datasets include:

```text
Normal Events
Known Malicious Events
Historical Incidents
Synthetic Events
Attack Simulation Data
Edge Cases
```

---

# 70. Positive Dataset

Contains:

```text
Expected Detection Matches
```

Example:

```text
Attack Simulation
```

---

# 71. Negative Dataset

Contains:

```text
Legitimate Activity
```

Example:

```text
Normal Administrator Activity
```

---

# 72. Regression Testing

Whenever detection logic changes:

```text
Old Tests
+
New Tests
```

should be executed.

Goal:

```text
New Change
↓
No Unexpected Detection Breakage
```

---

# 73. Detection Test Case

A test case can define:

```text
Input
Expected Match
Expected Severity
Expected Technique
Expected Result
```

Example:

```text
Input:
21 failed logins

Expected:
Alert

Severity:
Medium
```

---

# 74. Query Debugging

If a query returns no results:

```text
Check Time Range
 ↓
Check Data Source
 ↓
Check Field Names
 ↓
Check Field Values
 ↓
Check Data Types
 ↓
Remove Conditions
 ↓
Test Incrementally
```

---

# 75. Incremental Debugging

Suppose final query:

```text
A AND B AND C AND D AND E
```

Test:

```text
A
```

then:

```text
A AND B
```

then:

```text
A AND B AND C
```

Continue until:

```text
No Results
```

This identifies the problematic condition.

---

# 76. Query Performance Optimization

Use:

```text
Time Restrictions
+
Indexed Fields
+
Structured Filters
+
Selective Data Sources
```

Avoid:

```text
Full Historical Scan
+
Wildcard Everywhere
+
Complex Regex
```

---

# 77. High Cardinality

Fields with many unique values:

```text
UUID
Request ID
Session ID
Full URL
```

Grouping by them can be expensive.

Example:

```text
GROUP BY request_id
```

may produce enormous numbers of groups.

---

# 78. Query Cost

Query cost can increase with:

```text
Data Volume
Time Range
Regex
Joins
Aggregations
Cardinality
Frequency
```

---

# 79. Query Frequency

A query running:

```text
Every 5 minutes
```

has different resource requirements from:

```text
Every 1 hour
```

Detection frequency should match:

```text
Threat Speed
Risk
Telemetry Volume
Operational Need
```

---

# 80. Real-Time vs Scheduled Detection

### Real-Time

```text
Event
 ↓
Immediate Evaluation
 ↓
Alert
```

Useful for:

```text
High-Speed Threats
Critical Events
```

### Scheduled

```text
Events Accumulate
 ↓
Query Runs
 ↓
Results
```

Useful when:

```text
Aggregation
Historical Context
Periodic Analysis
```

is required.

---

# 81. Detection Window vs Alert Window

Detection window:

```text
How much activity is evaluated
```

Alert suppression window:

```text
How frequently repeated alerts are allowed
```

These should not be confused.

---

# 82. Threshold vs Frequency

Example:

```text
COUNT >= 20
WITHIN 5 minutes
```

defines:

```text
Threshold
+
Time Window
```

Frequency determines:

```text
How often the detection evaluates.
```

---

# 83. Detection Query Components

A useful conceptual template:

```text
DATA SOURCE
    ↓
TIME RANGE
    ↓
FILTER
    ↓
GROUP
    ↓
AGGREGATE
    ↓
CORRELATE
    ↓
THRESHOLD
    ↓
ENRICH
    ↓
RISK
    ↓
ALERT
```

---

# 84. Detection Rule Template

```text
Name:
Description:
Objective:

Data Sources:

Required Fields:

Detection Logic:

Time Window:

Grouping:

Threshold:

Severity:

Confidence:

Exceptions:

MITRE ATT&CK:

False Positives:

Test Cases:

Response Guidance:

Owner:
Version:
```

---

# 85. Detection Rule Example

```text
Name:
Potential Password Spray

Objective:
Identify authentication failures against
multiple user accounts from a common source.

Data Source:
Authentication Logs

Fields:
source.ip
user.name
event.outcome
@timestamp

Logic:
failure events

Group:
source.ip

Threshold:
10+ unique users

Window:
10 minutes

Severity:
Medium

False Positives:
Authorized security testing,
known authentication gateways.

Response:
Investigate source IP,
affected accounts,
authentication patterns,
and subsequent successful logins.
```

---

# 86. Detection Logic Layers

A mature detection can use layers:

```text
Layer 1:
Basic Indicator

Layer 2:
Behavior

Layer 3:
Context

Layer 4:
Correlation

Layer 5:
Risk
```

Example:

```text
Malicious IP
   ↓
Suspicious Process
   ↓
Critical Host
   ↓
Credential Access
   ↓
High Risk
```

---

# 87. Detection Confidence Ladder

Conceptually:

```text
Single Weak Signal
      ↓
Multiple Weak Signals
      ↓
Strong Behavioral Signal
      ↓
Correlated Attack Chain
      ↓
High Confidence Detection
```

---

# 88. Weak Signal

Example:

```text
PowerShell executed
```

Alone:

```text
Low Confidence
```

---

# 89. Stronger Signal

```text
PowerShell
+
Suspicious Parent
+
Encoded Command
```

Higher confidence.

---

# 90. Strong Correlation

```text
Phishing
+
PowerShell
+
C2
+
Credential Access
```

Potentially:

```text
High Confidence
```

---

# 91. Detection Resilience

Attackers may attempt:

```text
Rename Tools
Change IPs
Change Domains
Modify Commands
Use Living-off-the-Land Techniques
Encrypt Traffic
Disable Logging
```

Therefore:

```text
Static Detection
        ↓
May Be Evasive
```

Behavior-based detection can improve resilience.

---

# 92. Static vs Behavioral Detection

### Static

```text
Hash = X
```

### Behavioral

```text
Process
+
Parent
+
Command
+
Network
+
User
```

Behavioral detection can survive changes to specific indicators.

---

# 93. Hybrid Detection

Strong detection can combine:

```text
IOC
+
Behavior
+
Context
```

Example:

```text
Known Malicious Domain
+
Suspicious Process
+
Rare Host
```

---

# 94. Detection Rule Dependencies

A rule may depend on:

```text
Parser
Schema
Threat Feed
Lookup Table
Asset Database
Identity Mapping
Enrichment Service
```

Dependencies should be documented.

---

# 95. Detection Failure Modes

Common causes:

```text
Missing Data
Wrong Field
Schema Change
Parser Failure
Incorrect Threshold
Incorrect Time Window
Query Bug
Enrichment Failure
Data Delay
Performance Problem
```

---

# 96. Troubleshooting Detection Logic

Use:

```text
1. Is the data present?
2. Are the fields correct?
3. Are the values correct?
4. Does the simple filter work?
5. Does aggregation work?
6. Does correlation work?
7. Does threshold work?
8. Does enrichment work?
9. Does alerting work?
```

---

# 97. Detection Logic Anti-Patterns

Avoid:

```text
Alert on Every Event
```

```text
Huge Regex Without Need
```

```text
Broad Exclusions
```

```text
Hardcoded Environment Assumptions
```

```text
No Testing
```

```text
No Documentation
```

```text
No Ownership
```

---

# 98. Hardcoded Assumptions

Example:

```text
IF source.ip = 10.10.10.10
```

This may break when infrastructure changes.

Prefer:

```text
Known Asset List
+
Dynamic Context
```

where supported.

---

# 99. Environment-Aware Detection

Consider:

```text
Development
Staging
Production
```

The same behavior may have different meanings.

Example:

```text
Port Scan
```

in:

```text
Security Testing Environment
```

may be expected.

---

# 100. Detection Logic Checklist

Before deployment:

```text
[ ] Threat defined
[ ] Behavior understood
[ ] Data source confirmed
[ ] Fields validated
[ ] Time window selected
[ ] Conditions tested
[ ] Grouping validated
[ ] Threshold tested
[ ] Correlation validated
[ ] Exceptions reviewed
[ ] Positive test passed
[ ] Negative test passed
[ ] Edge cases tested
[ ] Performance tested
[ ] Documentation completed
```

---

# 101. Interview Questions

### What is detection logic?

> A set of conditions and relationships applied to security telemetry to identify suspicious or security-relevant behavior.

### What is the difference between a query and a detection rule?

> A query primarily searches or analyzes data, while a detection rule uses logic to identify a security condition and typically generate an alert.

### Why are time windows important?

> They help distinguish rapid suspicious behavior from normal activity and enable correlation across events.

### What is threshold detection?

> Detecting activity when an event count, value, or measurement crosses a defined threshold within a specified context or time window.

### What is correlation?

> Combining multiple events or signals based on time, entity, sequence, or other relationships to identify higher-confidence behavior.

### What is stateful detection?

> Detection that considers previous events or stored context when evaluating current activity.

### What is detection enrichment?

> Adding context such as threat intelligence, asset criticality, identity information, or geographic information to improve detection quality.

### How do you optimize detection queries?

> Restrict the time range, use structured fields, filter early, avoid unnecessary regex, reduce expensive aggregations, and control query frequency.

### Why are broad exclusions dangerous?

> They can eliminate visibility into real attacks and create large detection blind spots.

### How do you debug a detection query?

> Start with the data source, validate fields and values, simplify the query, add conditions incrementally, and identify which condition causes the failure.

---

# 102. Quick Revision

```text
Detection Logic
→ Conditions identifying suspicious behavior

Query
→ Searches/analyzes data

Detection Rule
→ Security logic that produces a detection outcome

Filter
→ Narrows events

Aggregation
→ Summarizes events

Threshold
→ Required count/value

Time Window
→ Period evaluated

Correlation
→ Combines related events

Stateful Detection
→ Uses historical context

Stateless Detection
→ Evaluates current event

Enrichment
→ Adds context

Suppression
→ Reduces repeated alerts

Deduplication
→ Removes duplicate alerts

Risk Scoring
→ Prioritizes based on combined evidence

Detection-as-Code
→ Version-controlled detection logic
```

---

# 103. Golden Rules

```text
1. Start with the threat.

2. Understand the behavior before writing the query.

3. Validate the telemetry and fields first.

4. Build queries incrementally.

5. Keep detection logic readable.

6. Use explicit parentheses when logic is complex.

7. Prefer structured fields over expensive text searches.

8. Use appropriate time windows.

9. Group events using meaningful entities.

10. Correlate events when individual signals are weak.

11. Add context before adding unnecessary complexity.

12. Test thresholds at and around their boundaries.

13. Test both malicious and legitimate behavior.

14. Consider delayed telemetry.

15. Distinguish event time from ingestion time.

16. Avoid broad exclusions.

17. Document exceptions.

18. Monitor query performance.

19. Consider high-cardinality fields.

20. Validate schema assumptions.

21. Treat detection logic as code.

22. Version important rules.

23. Test changes before production.

24. Design for attacker adaptation.

25. A detection should produce actionable security information—not merely a query result.
```

---

# 104. Final Mental Model

Every detection can be thought of as:

```text
WHAT?
  ↓
Data Source

WHICH?
  ↓
Fields

WHEN?
  ↓
Time Window

HOW?
  ↓
Conditions

HOW MANY?
  ↓
Threshold

RELATED TO WHAT?
  ↓
Correlation / Entity

HOW IMPORTANT?
  ↓
Severity / Risk

WHAT NEXT?
  ↓
Alert / Investigation / Response
```

---

# 105. Chapter Summary

This chapter established how raw telemetry becomes actual detection logic.

You should now understand:

```text
Queries
   ↓
Filters
   ↓
Conditions
   ↓
Time Windows
   ↓
Aggregation
   ↓
Thresholds
   ↓
Correlation
   ↓
Context
   ↓
Risk
   ↓
Alerts
```

The key principle is:

> **Good detection logic is not simply complex logic. It is the simplest reliable logic that identifies meaningful malicious behavior while remaining understandable, testable, performant, and maintainable.**

The next chapter moves into **Detection Methodologies & Detection Types**, covering signature, IOC, rule-based, threshold, behavioral, anomaly, statistical, correlation, and hybrid detection approaches.
```