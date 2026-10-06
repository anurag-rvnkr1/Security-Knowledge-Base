# Chapter 13 – Detection Tuning, False Positives & Performance

> Detection engineering does not end when an alert fires. Production detections must be continuously tuned to reduce unnecessary noise, preserve true positives, maintain acceptable query performance, and remain effective as the environment changes. Good tuning improves both security outcomes and analyst efficiency.

---

# 1. Introduction

A detection can be technically correct and still be operationally poor.

Example:

```text
Detection:
Suspicious PowerShell

Result:
50,000 alerts/day
```

If most alerts are legitimate:

```text
Analyst Overload
      ↓
Alert Fatigue
      ↓
Missed Threats
      ↓
Reduced Security
```

Therefore:

```text
Detection
+
Tuning
+
Performance
+
Continuous Validation
```

are all necessary.

---

# 2. What Is Detection Tuning?

Detection tuning is the process of improving detection behavior by adjusting:

```text
Logic
Thresholds
Time Windows
Filters
Exceptions
Context
Correlation
Severity
Confidence
Risk
```

The objective is:

```text
Maximum Useful Detection
with
Minimum Unnecessary Noise
```

---

# 3. Why Detection Tuning Matters

Poorly tuned detections can cause:

```text
High Alert Volume
False Positives
Slow Investigations
Analyst Fatigue
Query Performance Problems
Missed Threats
```

Good tuning provides:

```text
Higher Precision
Better Context
Lower Noise
Faster Investigation
Better SOC Efficiency
```

---

# 4. Detection Quality

Detection quality can be evaluated using:

```text
Precision
Recall
False Positive Rate
False Negative Rate
Alert Volume
Latency
Performance
Coverage
Analyst Feedback
```

---

# 5. Precision

Precision measures:

```text
How many generated alerts are meaningful?
```

Formula:

```text
Precision =
TP / (TP + FP)
```

High precision generally means:

```text
Less Alert Noise
```

---

# 6. Recall

Recall measures:

```text
How many relevant malicious events were detected?
```

Formula:

```text
Recall =
TP / (TP + FN)
```

High recall generally means:

```text
Fewer Missed Threats
```

---

# 7. Precision vs Recall

Conceptually:

```text
Increase Detection Sensitivity
        ↓
Recall ↑
        ↓
False Positives may ↑
        ↓
Precision ↓
```

The opposite can also occur.

Detection tuning is therefore a balancing process.

---

# 8. False Positive

A false positive occurs when:

```text
Legitimate Activity
        ↓
Detection
        ↓
Alert
```

Example:

```text
Authorized Administrator
uses
PowerShell
```

Detection:

```text
Suspicious PowerShell
```

Result:

```text
False Positive
```

---

# 9. False Negative

A false negative occurs when:

```text
Malicious Activity
        ↓
No Detection
```

This can be more dangerous than a false positive because the threat may remain unnoticed.

---

# 10. True Positive

```text
Malicious Activity
        ↓
Detection
        ↓
Alert
```

This is the desired outcome.

---

# 11. True Negative

```text
Legitimate Activity
        ↓
No Alert
```

This is also important because excessive alerts reduce SOC efficiency.

---

# 12. Confusion Matrix

```text
                    Actual

                 Malicious   Benign

Detected           TP          FP

Not Detected       FN          TN
```

---

# 13. False Positive Rate

Conceptually:

```text
FPR =
FP / (FP + TN)
```

Lower is generally better, but extremely aggressive suppression can increase false negatives.

---

# 14. Detection Tuning Loop

```text
Detection
    ↓
Production
    ↓
Measure
    ↓
Investigate Alerts
    ↓
Identify Noise
    ↓
Tune
    ↓
Test
    ↓
Deploy
    ↓
Measure Again
```

---

# 15. Alert Analysis

When tuning a detection, examine:

```text
Who?
What?
Where?
When?
Why?
How?
```

Example:

```text
User:
Admin

Host:
Management Server

Process:
PowerShell

Time:
Business Hours

Change Ticket:
Present
```

This may be legitimate.

---

# 16. Alert Context

Useful context includes:

```text
User
Host
Asset Criticality
Process
Parent Process
Command Line
IP
Domain
Location
Device
Application
Cloud Role
Threat Intelligence
Historical Behavior
```

Better context improves tuning decisions.

---

# 17. Baseline

A baseline describes normal behavior.

Examples:

```text
Normal Login Locations
Normal Processes
Normal Network Destinations
Normal API Rates
Normal Administrative Activity
Normal Cloud Changes
```

Tuning often begins with understanding the baseline.

---

# 18. Static Threshold

Example:

```text
Alert if:

failed_logins > 10
```

Problem:

```text
Different users have different normal behavior.
```

---

# 19. Dynamic Threshold

Instead:

```text
Alert if:

current_behavior >
user_baseline × factor
```

Dynamic thresholds can adapt to different entities.

---

# 20. Entity-Based Baselines

Build baselines per:

```text
User
Host
Application
Service Account
Cloud Account
Container
Network Segment
```

---

# 21. Peer-Based Baselines

Compare an entity with similar entities.

Example:

```text
Developer User
vs
Other Developers
```

or:

```text
Production Server
vs
Other Production Servers
```

---

# 22. Time-Based Baselines

Behavior may vary by:

```text
Hour
Day
Week
Month
```

Example:

```text
Login at 10 AM
→ Normal

Login at 3 AM
→ Potentially unusual
```

But time anomalies alone should not automatically imply malicious activity.

---

# 23. Geographic Baselines

Monitor:

```text
Normal Countries
Normal Regions
Normal IP Ranges
Normal VPN
```

Unexpected locations can be useful context.

---

# 24. Device Baselines

Monitor:

```text
Known Devices
New Devices
Device Type
Operating System
Browser
Endpoint Health
```

---

# 25. Application Baselines

Monitor:

```text
Normal Endpoints
Normal Request Rates
Normal Users
Normal Response Sizes
Normal Error Rates
```

---

# 26. Cloud Baselines

Monitor:

```text
Normal Regions
Normal API Calls
Normal Roles
Normal Resources
Normal Deployment Patterns
```

---

# 27. Container Baselines

Monitor:

```text
Normal Images
Normal Processes
Normal Network Destinations
Normal Privileges
Normal Service Accounts
```

---

# 28. Why Baselines Matter

Without baselines:

```text
Unusual
```

may be confused with:

```text
Malicious
```

The goal is to identify:

```text
Unusual + Risky + Contextually Suspicious
```

---

# 29. Tuning Through Filtering

Example:

```text
Detection:
Any PowerShell Execution
```

Tune to:

```text
PowerShell
+
Suspicious Parent
+
Suspicious Command
```

This reduces unnecessary alerts.

---

# 30. Filtering

Filters can remove known benign patterns.

Examples:

```text
Known Monitoring Host
Known Scanner
Known Deployment System
Known Backup Account
```

Filters should be narrow.

---

# 31. Broad Exceptions

Avoid:

```text
Exclude entire organization
```

or:

```text
Exclude all administrator activity
```

These can create large blind spots.

---

# 32. Narrow Exceptions

Prefer:

```text
Specific User
+
Specific Host
+
Specific Process
+
Specific Activity
```

Example:

```text
Approved CI runner
+
Known deployment process
```

---

# 33. Exception Documentation

Every important exception should explain:

```text
Why?
Who approved?
Scope?
Created?
Expires?
Owner?
Review date?
```

---

# 34. Temporary Exceptions

Prefer:

```text
Expiration Date
```

rather than:

```text
Permanent Suppression
```

Example:

```text
Exception:
Deployment Project

Expires:
30 days
```

---

# 35. Exception Lifecycle

```text
Request
 ↓
Review
 ↓
Approve
 ↓
Deploy
 ↓
Monitor
 ↓
Review
 ↓
Expire / Renew
```

---

# 36. Exception Risk

Every exception can create:

```text
Detection Blind Spot
```

Therefore:

```text
Exception Scope
+
Exception Duration
```

should be minimized.

---

# 37. Threshold Tuning

Suppose:

```text
Current:
> 5 events / 5 minutes
```

Produces:

```text
10,000 alerts
```

Try:

```text
> 20 events / 5 minutes
```

Then evaluate:

```text
Precision
Recall
Alert Volume
```

---

# 38. Threshold Tuning Mistake

Do not simply increase:

```text
5
→
50
→
500
```

until alert volume disappears.

You may suppress real attacks.

---

# 39. Contextual Thresholds

Instead of:

```text
> 50 logins
```

use:

```text
> baseline + anomaly factor
```

or combine:

```text
High Failure Rate
+
Successful Login
+
New Device
```

---

# 40. Time-Window Tuning

Example:

```text
10 failed logins
within 5 minutes
```

Possible tuning:

```text
10 / 5 minutes
```

vs:

```text
20 / 15 minutes
```

Choose based on:

```text
Attack Pattern
Normal Behavior
Telemetry
Response Requirements
```

---

# 41. Correlation Window

Too short:

```text
Events missed
```

Too long:

```text
Unrelated events correlated
```

The correct window should represent realistic attack behavior.

---

# 42. Sequence Tuning

Example:

```text
Login
→ Privilege Change
→ Sensitive Access
```

If the time window is too long:

```text
Unrelated events
```

may be combined.

---

# 43. Aggregation Tuning

Instead of:

```text
1 alert per event
```

use:

```text
1 alert per entity + time window
```

Example:

```text
100 suspicious events
→
1 correlated alert
```

This can significantly reduce noise.

---

# 44. Alert Deduplication

If the same event generates:

```text
10 identical alerts
```

deduplicate using keys such as:

```text
Detection ID
User
Host
Destination
Time Window
```

---

# 45. Alert Suppression

Suppression temporarily prevents repeated alerts.

Example:

```text
After alert:
Suppress same entity for 30 minutes.
```

Use carefully.

---

# 46. Suppression Risk

Over-suppression can hide:

```text
Repeated Attack
Escalation
New Context
```

Better suppression may consider:

```text
Same Entity
+
Same Behavior
+
Same Context
```

---

# 47. Alert Grouping

Group related events:

```text
User
+
Host
+
Process
+
Network
```

into one investigation object.

---

# 48. Alert Enrichment

Add:

```text
Asset Criticality
User Risk
Threat Intelligence
Geo
Device
Process Reputation
Historical Activity
```

Enrichment can improve analyst decision-making without changing the core detection.

---

# 49. Severity Tuning

Severity should reflect:

```text
Impact
Confidence
Asset Criticality
Identity Privilege
Threat Intelligence
```

---

# 50. Severity vs Confidence

These are different.

### Severity

```text
How serious is the potential impact?
```

### Confidence

```text
How likely is the alert to represent malicious activity?
```

Example:

```text
High Severity
+
Low Confidence
```

may require investigation but not immediate automated containment.

---

# 51. Risk-Based Tuning

A detection can calculate:

```text
Risk =
Behavior
+
Asset
+
Identity
+
Threat Intelligence
+
Historical Context
```

---

# 52. Example Risk Model

Conceptual:

```text
Base Score: 30

Privileged User: +20

Critical Asset: +25

Rare Destination: +10

Threat Intelligence Match: +25

Final:
110
```

Actual scoring should be calibrated to the organization's risk model.

---

# 53. Confidence Scoring

Possible factors:

```text
Behavior Match
Threat Intelligence
User Context
Asset Context
Multiple Signals
Historical Behavior
```

---

# 54. Multi-Signal Detection

Weak:

```text
Rare Domain
```

Stronger:

```text
Rare Domain
+
Suspicious Process
+
Periodic Connection
+
New Device
```

---

# 55. Alert Correlation

Combine:

```text
Identity
+
Endpoint
+
Network
+
Cloud
+
Application
```

to reduce ambiguity.

---

# 56. Noise Reduction

Noise reduction techniques:

```text
Filtering
Baselines
Thresholds
Aggregation
Deduplication
Suppression
Correlation
Enrichment
Risk Scoring
```

---

# 57. Alert Fatigue

Alert fatigue occurs when analysts receive too many low-value alerts.

Symptoms:

```text
Alerts Ignored
Alerts Closed Quickly
Slow Investigation
Repeated Escalation
Analyst Burnout
```

---

# 58. Alert Fatigue Is a Security Risk

Too much noise can cause:

```text
True Positive Missed
```

Therefore:

```text
Alert Quality
=
Security Control
```

---

# 59. Alert-to-Action Ratio

A useful internal metric:

```text
Actionable Alerts
/
Total Alerts
```

Higher is generally better.

---

# 60. Alert Closure Analysis

Analyze closure reasons:

```text
True Positive
Benign
False Positive
Duplicate
Expected Activity
Insufficient Data
```

These categories can guide tuning.

---

# 61. SOC Feedback Loop

```text
Alert
 ↓
Analyst Investigation
 ↓
Closure Reason
 ↓
Detection Engineer
 ↓
Tuning
 ↓
Retest
 ↓
Deployment
```

---

# 62. Analyst Feedback

Analysts can identify:

```text
Missing Context
Repeated Noise
Bad Severity
Poor Correlation
Useful Signals
```

Detection engineering should incorporate this feedback.

---

# 63. Tuning Through Incident Analysis

A true incident may reveal:

```text
Detection Worked
but
Severity Too Low
```

or:

```text
Detection Triggered
but
Context Missing
```

This is a tuning opportunity.

---

# 64. Tuning Through Threat Hunting

Threat hunting can reveal:

```text
Missed Behavior
```

which may require:

```text
New Detection
```

rather than simply tuning an existing rule.

---

# 65. Tuning Through Purple Teaming

Purple team results may reveal:

```text
Detection Miss
```

or:

```text
Detection Too Noisy
```

Then:

```text
Tune
→
Retest
```

---

# 66. Performance Tuning

Detection performance concerns:

```text
Query Runtime
CPU
Memory
Storage
Events/sec
Latency
Concurrency
```

---

# 67. Why Performance Matters

A detection that takes:

```text
30 minutes
```

to execute may be useless for:

```text
Active Attack
```

---

# 68. Query Cost

Expensive queries may use:

```text
Large Joins
Regex
High-Cardinality Aggregations
Long Time Windows
Complex Correlation
Unindexed Fields
```

---

# 69. Filter Early

Bad:

```text
Process 1 billion events
        ↓
Filter later
```

Better:

```text
Filter relevant events first
        ↓
Process smaller dataset
```

---

# 70. Select Only Required Fields

Avoid unnecessary:

```text
SELECT *
```

when only a few fields are needed.

Prefer:

```text
user
host
process
timestamp
```

where appropriate.

---

# 71. Indexed Fields

Where supported, use fields optimized for searching:

```text
Timestamp
Host
User
Event Type
Source IP
```

The exact optimization depends on the platform.

---

# 72. Time Window Optimization

Avoid unnecessarily large windows.

Bad:

```text
30 days
```

when:

```text
15 minutes
```

is sufficient.

---

# 73. Aggregation

Instead of processing every event individually:

```text
Aggregate by:
User
Host
Destination
Time Window
```

Then evaluate the aggregate.

---

# 74. Pre-Aggregation

For high-volume environments, maintain:

```text
Hourly Counts
Daily Baselines
Entity Statistics
```

This can reduce query cost.

---

# 75. Caching

Cache stable enrichment:

```text
Asset Criticality
User Role
Known Scanner
Known Infrastructure
```

rather than repeatedly querying expensive sources.

---

# 76. Lookup Optimization

Reference tables should be:

```text
Small
Relevant
Updated
Indexed
```

Avoid enormous inefficient lookups.

---

# 77. Regex Performance

Prefer:

```text
Exact Match
Prefix
Suffix
Structured Fields
```

when possible.

Avoid unnecessary complex regex across massive datasets.

---

# 78. Cardinality

High-cardinality fields include:

```text
Request ID
Session ID
IP
User
Process ID
Container ID
```

Large aggregations over these fields can be expensive.

---

# 79. Correlation State

Sequence detection may need to store state:

```text
Event A
 ↓
Remember
 ↓
Event B
 ↓
Correlate
```

State should have:

```text
Expiration
Memory Limits
Cleanup
```

---

# 80. Query Concurrency

Too many expensive detections running simultaneously can cause:

```text
Resource Contention
Latency
Dropped Queries
```

Prioritize critical detections.

---

# 81. Detection Scheduling

Not every detection needs the same frequency.

Example:

```text
Critical:
Near Real-Time

Medium:
Every Few Minutes

Low:
Hourly / Daily
```

The correct schedule depends on risk.

---

# 82. Streaming vs Batch

### Streaming

```text
Low Latency
Near Real-Time
```

Useful for:

```text
Account Takeover
C2
Privilege Escalation
```

### Batch

```text
Periodic
Large Historical Analysis
```

Useful for:

```text
Long-Term Anomaly
Slow Trends
Periodic Review
```

---

# 83. Performance Testing

Measure:

```text
Average Runtime
P95 Runtime
P99 Runtime
Events/sec
Resource Usage
Latency
```

---

# 84. Tail Latency

Average runtime may look good:

```text
Average = 2 sec
```

while:

```text
P99 = 60 sec
```

Tail latency matters for security operations.

---

# 85. Performance Regression

After changing a detection:

```text
Old:
2 sec

New:
20 sec
```

The detection may be logically better but operationally worse.

Performance should therefore be part of regression testing.

---

# 86. Alert Volume Regression

Similarly:

```text
Old:
50 alerts/day

New:
5,000 alerts/day
```

This should trigger investigation.

---

# 87. Tuning Validation

After every significant tuning change:

```text
Positive Test
+
Negative Test
+
Regression Test
+
Performance Test
```

---

# 88. Canary Tuning

Deploy tuned detection to:

```text
Small Scope
```

Measure:

```text
Alert Rate
Precision
Latency
Performance
```

Then expand.

---

# 89. Shadow Tuning

Run:

```text
Old Rule
+
New Rule
```

simultaneously.

Compare:

```text
Matches
Alerts
Misses
Noise
```

---

# 90. A/B Detection Comparison

Conceptually:

```text
Version A
vs
Version B
```

Compare:

```text
Precision
Recall
Alert Volume
Latency
Performance
```

---

# 91. Detection Tuning Experiment

Document:

```text
Hypothesis
Change
Expected Result
Observed Result
Metrics
Decision
```

Example:

```text
Hypothesis:
Adding parent-process context will reduce false positives.

Change:
Add parent-process condition.

Result:
FP rate reduced.

Decision:
Deploy.
```

---

# 92. Tuning Trade-Offs

Every tuning decision can affect:

```text
Precision
Recall
Performance
Coverage
```

Example:

```text
More Filtering
→
Performance ↑
Noise ↓
Potential Recall ↓
```

---

# 93. Never Optimize Only One Metric

Avoid:

```text
Alert Volume = 0
```

as the goal.

The correct objective is:

```text
Useful Detection
+
Acceptable Noise
+
Acceptable Performance
```

---

# 94. Detection Quality Triangle

```text
          Detection Quality
             /       \
            /         \
       Accuracy ---- Performance
```

All three matter.

---

# 95. Detection Tuning Maturity

### Level 1

Manual tuning.

### Level 2

Alert feedback.

### Level 3

Metrics-driven tuning.

### Level 4

Baseline-aware tuning.

### Level 5

Automated tuning experiments.

### Level 6

Continuous adaptive detection.

---

# 96. Automated Tuning

Possible automation:

```text
Alert Analysis
 ↓
False Positive Classification
 ↓
Baseline Update
 ↓
Suggested Threshold
 ↓
Engineer Review
```

Automation should not blindly suppress alerts.

---

# 97. Machine Learning for Tuning

ML can help identify:

```text
Normal Behavior
Anomalies
Clusters
Peer Groups
Outliers
```

But:

```text
Model Output
≠
Ground Truth
```

Human validation remains important.

---

# 98. Adaptive Detection

An adaptive detection can respond to:

```text
Baseline Changes
Threat Intelligence
Asset Criticality
User Risk
Environment Changes
```

But adaptive systems require safeguards against:

```text
Model Drift
Feedback Loops
Adversarial Manipulation
Over-Suppression
```

---

# 99. Detection Drift Monitoring

Monitor:

```text
Alert Volume
Precision
Recall
Input Volume
Query Runtime
Schema
Environment
```

---

# 100. Tuning Trigger Conditions

Revisit a detection when:

```text
Alert Volume Spikes
Alert Volume Drops
False Positives Increase
Threat Changes
Environment Changes
Telemetry Changes
Performance Degrades
New Incident Occurs
ATT&CK Changes
```

---

# 101. Detection Review Cadence

Possible:

```text
Critical:
Monthly

Important:
Quarterly

Low Priority:
Semi-Annual
```

Exact schedules should be defined by risk and organizational policy.

---

# 102. Detection Performance Budget

Define acceptable:

```text
Query Runtime
CPU
Memory
Latency
Event Processing Cost
```

This prevents detection logic from consuming disproportionate resources.

---

# 103. Cost-Aware Detection

In large environments, consider:

```text
Data Ingestion Cost
Storage Cost
Query Cost
Compute Cost
Alert Processing Cost
```

A detection should provide enough security value to justify its operational cost.

---

# 104. Detection ROI

Conceptually:

```text
Detection Value
/
Operational Cost
```

High-value detections:

```text
High Threat Relevance
+
High Detection Value
+
Acceptable Cost
```

---

# 105. Noise Budget

Teams may define an acceptable amount of:

```text
Low-Value Alerts
```

If a detection exceeds the budget:

```text
Tune
or
Redesign
```

---

# 106. Alert Quality Score

A custom score may consider:

```text
True Positive
Context
Severity Accuracy
Investigation Time
Response Value
```

Example:

```text
Quality Score =
0.30 Precision
+
0.20 Context
+
0.20 Severity Accuracy
+
0.30 Analyst Value
```

The formula is illustrative; organizations should calibrate their own model.

---

# 107. Detection Tuning Documentation

Record:

```text
Detection ID
Problem
Evidence
Change
Expected Impact
Actual Impact
Tests
Reviewer
Deployment
Rollback
```

---

# 108. Tuning Record Example

```yaml
detection_id: DET-001

issue:
  type: false_positive
  volume: high

cause:
  approved_admin_activity

change:
  added_context:
    - user_role
    - host_group

tests:
  positive: pass
  negative: pass
  regression: pass

result:
  alert_reduction: 65%

status: deployed
```

---

# 109. Detection Tuning Checklist

```text
[ ] Alert volume measured
[ ] False positives categorized
[ ] False negatives considered
[ ] Baseline reviewed
[ ] Threshold evaluated
[ ] Time window evaluated
[ ] Correlation evaluated
[ ] Context evaluated
[ ] Exceptions reviewed
[ ] Exceptions documented
[ ] Expiration defined
[ ] Query performance measured
[ ] Resource usage measured
[ ] Positive test passed
[ ] Negative test passed
[ ] Regression test passed
[ ] Performance test passed
[ ] Canary completed
[ ] Analyst feedback collected
[ ] Documentation updated
[ ] Owner assigned
[ ] Review date defined
```

---

# 110. Interview Questions

### What is detection tuning?

> The process of improving detection logic, thresholds, context, exceptions, and correlation to increase useful detection while controlling false positives and performance costs.

### What is a false positive?

> Legitimate activity incorrectly identified as suspicious or malicious.

### What is a false negative?

> Malicious or relevant activity that the detection fails to identify.

### Why are false positives dangerous?

> Excessive false positives create alert fatigue, consume analyst capacity, and can cause real threats to be overlooked.

### How do you reduce false positives?

> Understand the baseline, add contextual signals, use narrow exceptions, improve correlation, tune thresholds, and validate changes with positive and negative tests.

### Should you simply increase a threshold to reduce alert volume?

> No. Increasing thresholds can reduce noise but may also increase false negatives. The change should be evaluated against both detection quality and attack behavior.

### What is a baseline?

> A representation of expected normal behavior for an entity, peer group, application, workload, or environment.

### Why are dynamic thresholds useful?

> They adapt to different behavioral patterns instead of applying one static threshold to every entity.

### What is alert suppression?

> Temporarily preventing repeated alerts for a defined condition or context.

### What is alert deduplication?

> Combining identical or highly similar alerts so analysts do not investigate the same underlying activity repeatedly.

### What is the difference between severity and confidence?

> Severity describes potential impact, while confidence describes how likely the observed behavior is malicious or meaningful.

### How do you tune a high-volume detection?

> Analyze alert samples and closure reasons, identify common benign patterns, add contextual conditions or narrow exceptions, validate against known malicious cases, and monitor the result in a controlled rollout.

### How do you optimize an expensive detection?

> Filter early, reduce the time window, select only necessary fields, optimize joins and aggregations, use indexed fields, pre-aggregate where appropriate, and measure query performance before and after the change.

### What is detection performance regression?

> A situation where a detection remains logically correct but becomes significantly more expensive or slower after a change.

### What is alert fatigue?

> A condition where excessive low-value alerts reduce analyst attention and increase the risk of missing meaningful threats.

---

# 111. Quick Revision

```text
Detection Tuning
→ Improving detection quality and operational efficiency

False Positive
→ Benign activity incorrectly detected

False Negative
→ Malicious activity missed

True Positive
→ Malicious activity correctly detected

True Negative
→ Benign activity correctly ignored

Precision
→ TP / (TP + FP)

Recall
→ TP / (TP + FN)

Baseline
→ Expected normal behavior

Static Threshold
→ Fixed detection limit

Dynamic Threshold
→ Baseline-aware limit

Peer Baseline
→ Comparison against similar entities

Exception
→ Controlled exclusion

Suppression
→ Temporarily reducing repeated alerts

Deduplication
→ Combining duplicate alerts

Correlation
→ Combining multiple related signals

Enrichment
→ Adding contextual information

Severity
→ Potential impact

Confidence
→ Likelihood of maliciousness

Risk Score
→ Combined contextual security risk

Alert Fatigue
→ Analyst overload caused by excessive alerts

Query Optimization
→ Reducing detection execution cost

Cardinality
→ Number of unique values in a field

Pre-Aggregation
→ Computing statistics before detection

Canary
→ Limited deployment for validation

Shadow Mode
→ Detection runs without normal alerting

Performance Regression
→ Detection becomes slower or more expensive

Detection Drift
→ Detection effectiveness changes over time

Noise Budget
→ Acceptable alert-noise level

Detection ROI
→ Security value relative to operational cost
```

---

# 112. Golden Rules

```text
1. A detection that generates unlimited noise is not a successful detection.

2. Tune for useful detection, not merely low alert volume.

3. Never eliminate false positives by blindly suppressing alerts.

4. Always consider false negatives when tuning.

5. Use real alert data to identify noise patterns.

6. Understand the normal baseline before changing thresholds.

7. Prefer narrow exceptions over broad exclusions.

8. Document every important exception.

9. Give exceptions expiration dates when possible.

10. Review exceptions periodically.

11. Use multiple contextual signals.

12. Combine identity, endpoint, network, cloud, and application context.

13. Use dynamic thresholds when appropriate.

14. Tune correlation windows carefully.

15. Test threshold boundaries.

16. Test time-window boundaries.

17. Deduplicate repeated events.

18. Aggregate related activity when appropriate.

19. Distinguish severity from confidence.

20. Use risk scoring to prioritize meaningful alerts.

21. Monitor alert volume after every major change.

22. Monitor alert drops as well as alert spikes.

23. Measure query performance.

24. Optimize expensive queries.

25. Filter early.

26. Select only required fields.

27. Avoid unnecessary high-cardinality operations.

28. Avoid unnecessarily large time windows.

29. Test performance at realistic scale.

30. Treat performance as part of detection quality.

31. Validate tuning changes with positive tests.

32. Validate tuning changes with negative tests.

33. Run regression tests after tuning.

34. Use canary or shadow deployment for high-impact changes.

35. Collect analyst feedback.

36. Use incident findings to improve detections.

37. Use threat hunting to identify missed behaviors.

38. Use purple teaming to validate tuning.

39. Monitor detection drift.

40. Monitor schema and telemetry changes.

41. Revisit detections when the environment changes.

42. Do not optimize for one metric alone.

43. High precision with terrible recall is not automatically good.

44. High recall with overwhelming noise is not automatically good.

45. The goal is reliable, timely, actionable detection.

46. Every tuning change should have evidence behind it.

47. Every important tuning change should be tested.

48. Every production detection should have an owner.

49. Every production detection should have a review lifecycle.

50. Detection tuning is continuous engineering, not a one-time cleanup activity.
```

---

# 113. Final Mental Model

Think of detection tuning as a control loop:

```text
DETECTION
    ↓
PRODUCTION
    ↓
ALERTS
    ↓
ANALYST FEEDBACK
    ↓
METRICS
    ↓
NOISE / MISSES / PERFORMANCE
    ↓
TUNING
    ↓
TESTING
    ↓
CANARY
    ↓
PRODUCTION
    ↓
MEASURE AGAIN
```

The optimization objective is:

```text
                 Detection Quality
                       ↑
                       |
        Precision ←────┼────→ Recall
                       |
                       ↓
                  Performance
```

A mature detection balances:

```text
Security Coverage
+
Accuracy
+
Context
+
Performance
+
Analyst Usability
```

---

# 114. Practical Tuning Workflow

Use this process whenever a production detection generates too much noise:

```text
1. Identify the noisy detection.
        ↓
2. Measure alert volume.
        ↓
3. Sample alerts.
        ↓
4. Categorize closure reasons.
        ↓
5. Identify common benign patterns.
        ↓
6. Compare against malicious examples.
        ↓
7. Form a tuning hypothesis.
        ↓
8. Modify detection logic.
        ↓
9. Run positive tests.
        ↓
10. Run negative tests.
        ↓
11. Run regression tests.
        ↓
12. Measure performance.
        ↓
13. Deploy in shadow/canary mode.
        ↓
14. Compare old vs new behavior.
        ↓
15. Deploy broadly.
        ↓
16. Continue monitoring.
```

---

# 115. Example – Tuning a Suspicious Login Detection

Initial rule:

```text
Alert on:
Any login from a new country
```

Problem:

```text
High False Positives
```

Investigation finds:

```text
VPN Users
Traveling Employees
Cloud Proxies
```

Instead of simply excluding them:

```text
New Country
+
New Device
+
No Known VPN
+
Sensitive Application
+
Unusual Login Time
```

Now the detection has more context.

Expected result:

```text
False Positives ↓
Detection Quality ↑
```

---

# 116. Example – Tuning a Network Scan Detection

Initial:

```text
Alert if:
> 20 destinations / 5 minutes
```

Problem:

```text
Security Scanner
Monitoring System
Backup Infrastructure
```

Tune using:

```text
Source Role
+
Destination Pattern
+
Known Scanner Identity
+
Historical Baseline
```

Then test:

```text
Known Scanner
→ No Alert

Unexpected Workstation
→ Alert
```

---

# 117. Example – Tuning an Endpoint Detection

Initial:

```text
Alert:
PowerShell execution
```

Problem:

```text
Thousands of legitimate executions
```

Improve:

```text
PowerShell
+
Suspicious Parent
+
Suspicious Command
+
External Connection
```

Then:

```text
Positive Test → Alert
Admin Automation → No Alert
```

---

# 118. Example – Performance Optimization

Initial query:

```text
Search:
30 days
+
All fields
+
Multiple large joins
```

Observed:

```text
Runtime = 15 minutes
```

Optimize:

```text
Time Window → 30 minutes
Select Required Fields
Filter Early
Pre-Aggregate
Optimize Joins
```

Result:

```text
Runtime = 20 seconds
```

The detection should then be retested for correctness.

---

# 119. Final Detection Quality Framework

A production detection should be evaluated across:

```text
                THREAT
                  ↓
             RELEVANCE
                  ↓
              COVERAGE
                  ↓
             DETECTION
                  ↓
          ┌───────┼───────┐
          ↓       ↓       ↓
      Precision Recall Performance
          ↓       ↓       ↓
          └───────┼───────┘
                  ↓
               CONTEXT
                  ↓
              ANALYST
                  ↓
              RESPONSE
```

The final question is:

> **Does this detection reliably identify meaningful adversary behavior, quickly enough, with enough context, at an operational cost the SOC can sustain?**

---

# 120. Chapter Summary

This chapter covered:

```text
Detection Tuning
False Positives
False Negatives
True Positives
True Negatives
Precision
Recall
False Positive Rate
Baselines
Dynamic Thresholds
Static Thresholds
Peer Baselines
Time-Based Baselines
Geographic Baselines
Device Baselines
Application Baselines
Cloud Baselines
Container Baselines
Filtering
Exceptions
Temporary Exceptions
Exception Lifecycle
Threshold Tuning
Correlation Windows
Aggregation
Deduplication
Suppression
Alert Grouping
Enrichment
Severity
Confidence
Risk Scoring
Alert Fatigue
SOC Feedback
Incident-Driven Tuning
Threat-Hunting Feedback
Purple-Team Feedback
Query Performance
Query Optimization
Indexing
Pre-Aggregation
Caching
Cardinality
Correlation State
Streaming
Batch Detection
Performance Testing
Tail Latency
Performance Regression
Alert Volume Regression
Shadow Mode
Canary Deployment
A/B Detection Comparison
Tuning Experiments
Detection Drift
Noise Budgets
Detection ROI
Detection Performance Budgets
Automated Tuning
Adaptive Detection
Detection Review
Tuning Documentation
```

The central principle is:

> **A production detection must balance detection coverage, precision, recall, context, latency, performance, and analyst usability. Tuning should reduce unnecessary noise without creating blind spots, and every significant tuning change should be validated through testing and measurable evidence.**

The mature tuning lifecycle is:

```text
MEASURE
  ↓
UNDERSTAND
  ↓
HYPOTHESIZE
  ↓
TUNE
  ↓
TEST
  ↓
CANARY
  ↓
DEPLOY
  ↓
MONITOR
  ↓
REASSESS
```

The ultimate objective is not:

```text
Fewer Alerts
```

and not:

```text
More Alerts
```

It is:

```text
More Useful Alerts
+
Better Detection
+
Lower Noise
+
Acceptable Performance
+
Continuous Validation
```

---