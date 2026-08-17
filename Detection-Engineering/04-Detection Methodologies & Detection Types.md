# Chapter 04 – Detection Methodologies & Detection Types

> Different threats require different detection strategies. A detection engineer must understand when to use signatures, IOCs, behavioral logic, thresholds, anomalies, statistical models, correlation, and hybrid approaches—and understand the strengths and limitations of each.

---

# 1. What Is a Detection Methodology?

A **detection methodology** is the approach used to identify suspicious or malicious activity from security telemetry.

Common methodologies include:

```text
Signature-Based
IOC-Based
Rule-Based
Threshold-Based
Behavior-Based
Anomaly-Based
Statistical
Correlation-Based
Sequence-Based
Risk-Based
Threat-Informed
Hybrid
```

No single methodology can detect every type of threat.

A mature detection program combines multiple approaches.

---

# 2. Detection Methodology Selection

The choice of methodology should depend on:

```text
Threat Type
Attacker Behavior
Available Telemetry
Detection Objective
Required Speed
Confidence
False Positive Risk
Environment
```

Conceptually:

```text
Threat
  ↓
Behavior
  ↓
Available Telemetry
  ↓
Detection Method
  ↓
Validation
```

---

# 3. Signature-Based Detection

Signature-based detection looks for a known pattern associated with malicious activity.

Examples:

```text
Known File Pattern
Known Command Pattern
Known Network Pattern
Known Malware Signature
Known Payload Pattern
```

Conceptually:

```text
Observed Data
     ↓
Known Signature
     ↓
Match?
     ↓
Alert
```

---

# 4. Signature Example

Suppose a known malicious file has a known hash:

```text
SHA-256:
abc123...
```

Detection:

```text
IF file.hash = known_malicious_hash
THEN alert
```

This is simple and high-confidence when the indicator is trustworthy.

---

# 5. Advantages of Signature Detection

```text
Simple
Fast
Easy to Explain
Easy to Test
Often High Precision
```

Useful for:

```text
Known Malware
Known Exploits
Known Malicious Files
Known Attack Patterns
```

---

# 6. Limitations of Signature Detection

Attackers can modify:

```text
File
Hash
Payload
Command
Infrastructure
```

Therefore:

```text
Signature
   ↓
Known Variant
```

does not necessarily detect:

```text
Modified Variant
```

---

# 7. IOC-Based Detection

IOC = **Indicator of Compromise**

Examples:

```text
IP Address
Domain
URL
File Hash
Email Address
Filename
Certificate
```

Detection:

```text
Observed Indicator
       ↓
Threat Intelligence
       ↓
Match
       ↓
Alert
```

---

# 8. Signature vs IOC

They overlap but are not identical.

### Signature

Looks for a recognizable pattern.

### IOC

Looks for a known indicator associated with compromise.

Example:

```text
Known Malicious IP
→ IOC

Known Malware Byte Pattern
→ Signature
```

---

# 9. IOC Advantages

```text
Fast
Easy to Implement
Useful for Known Threats
Good for Threat Intelligence Integration
```

---

# 10. IOC Limitations

IOCs can become:

```text
Stale
Reused
Changed
Blocked
Benign
Too Broad
```

Attackers frequently change infrastructure.

Therefore:

```text
IOC Detection
+
Behavior Detection
```

is stronger than relying only on IOCs.

---

# 11. Rule-Based Detection

Rule-based detection uses explicit conditions.

Example:

```text
IF
process.name = "powershell.exe"
AND
suspicious_command = true
THEN
alert
```

Rules can be:

```text
Simple
Complex
Contextual
Correlated
Stateful
```

---

# 12. Rule-Based Detection Advantages

```text
Predictable
Explainable
Testable
Easy to Review
Easy to Version
```

This makes rule-based detection extremely common in SOC environments.

---

# 13. Rule-Based Detection Limitations

Rules can become:

```text
Too Complex
Environment-Specific
Noisy
Difficult to Maintain
Easy to Break
```

A large rule is not automatically a better rule.

---

# 14. Threshold-Based Detection

Threshold detection triggers when activity exceeds a predefined limit.

Example:

```text
Failed Login Count >= 20
within 5 minutes
```

Common use cases:

```text
Brute Force
Port Scanning
Large Data Transfer
Authentication Failures
Repeated API Calls
```

---

# 15. Threshold Structure

A threshold detection usually contains:

```text
Event
+
Entity
+
Count/Value
+
Threshold
+
Time Window
```

Example:

```text
Authentication Failure
+
Same User
+
20 Events
+
5 Minutes
```

---

# 16. Threshold Advantages

```text
Simple
Fast
Easy to Explain
Easy to Implement
Easy to Tune
```

---

# 17. Threshold Limitations

Static thresholds may fail when normal behavior varies.

Example:

```text
Normal User:
5 logins/day

Administrator:
200 logins/day
```

A single threshold may not work equally well for both.

---

# 18. Static Threshold

Example:

```text
IF
failed_logins >= 20
THEN
alert
```

The threshold is fixed.

---

# 19. Dynamic Threshold

Dynamic thresholds adapt to expected behavior.

Example:

```text
Normal:
10 events/day

Observed:
100 events/day
```

Instead of asking:

```text
Is count > 20?
```

we ask:

```text
Is behavior significantly above baseline?
```

---

# 20. Behavioral Detection

Behavioral detection focuses on **what an entity does** rather than only matching known indicators.

Example:

```text
Office Application
      ↓
PowerShell
      ↓
Network Connection
```

The exact file hash or IP may be unknown.

The behavior itself is suspicious.

---

# 21. Behavioral Detection Advantages

Behavioral detection can detect:

```text
Unknown Variants
Modified Malware
New Infrastructure
Living-off-the-Land Activity
Attack Chains
```

It is often more resilient to indicator changes.

---

# 22. Behavioral Detection Limitations

Behavioral patterns may also be legitimate.

Example:

```text
PowerShell
```

could be:

```text
Administrator Activity
Automation
Software Deployment
Malicious Activity
```

Therefore context is important.

---

# 23. Contextual Behavioral Detection

Weak:

```text
PowerShell executed
```

Stronger:

```text
PowerShell
+
Unusual Parent
+
Encoded Command
+
External Connection
```

The second pattern provides more evidence.

---

# 24. Anomaly Detection

Anomaly detection identifies activity that deviates from expected behavior.

Concept:

```text
Normal Baseline
      ↓
Observed Behavior
      ↓
Deviation
      ↓
Anomaly
```

---

# 25. Examples of Anomalies

```text
New Login Location
Unusual Login Time
Unusual Data Volume
Rare Process
Rare Destination
Unexpected Privilege
Unusual Cloud API Activity
```

---

# 26. Anomaly Detection Advantages

Useful for:

```text
Unknown Threats
Insider Risk
Account Compromise
Novel Behavior
Abnormal Resource Usage
```

---

# 27. Anomaly Detection Limitations

Anomalies are not automatically malicious.

Example:

```text
Employee Travels
```

could cause:

```text
New Location
```

but may be completely legitimate.

Therefore:

```text
Anomaly
≠
Compromise
```

---

# 28. Baseline

A baseline represents expected activity.

Examples:

```text
Normal Login Time
Normal Device
Normal Location
Normal Data Volume
Normal Process
Normal Network Destination
```

---

# 29. Baseline Example

User normally:

```text
09:00–18:00
Laptop-A
Office Network
```

Observed:

```text
03:00
New Device
Foreign Location
```

This is anomalous.

Additional context is needed before concluding compromise.

---

# 30. Statistical Detection

Statistical detection uses mathematical properties of observed data.

Examples:

```text
Mean
Median
Variance
Standard Deviation
Percentiles
Frequency
Distribution
```

---

# 31. Standard Deviation Concept

Suppose normal activity has:

```text
Mean = 10
Std Dev = 2
```

Observed:

```text
Value = 20
```

This may represent a significant deviation from the baseline.

The exact threshold depends on the detection design and data distribution.

---

# 32. Z-Score

A common statistical concept:

```text
z = (x - μ) / σ
```

Where:

```text
x = observed value
μ = mean
σ = standard deviation
```

A large absolute z-score can indicate an unusual observation.

---

# 33. Percentile-Based Detection

Instead of standard deviation:

```text
95th Percentile
99th Percentile
99.9th Percentile
```

can be used.

Example:

```text
Normal outbound transfer
< 500 MB

99th percentile:
500 MB
```

An event above that level may deserve investigation.

---

# 34. Statistical Detection Advantages

```text
Adaptive
Data-Driven
Useful for Large Datasets
Can Detect Unusual Behavior
```

---

# 35. Statistical Detection Limitations

Challenges include:

```text
Poor Baseline
Seasonality
Data Drift
Outliers
Small Datasets
Changing Environment
```

---

# 36. Seasonality

Behavior may vary by:

```text
Hour
Day
Week
Month
Business Cycle
```

Example:

```text
High Traffic:
Monday Morning

Low Traffic:
Sunday
```

A detection should not treat every difference as malicious.

---

# 37. Correlation-Based Detection

Correlation combines multiple events.

Example:

```text
Failed Login
+
Successful Login
+
MFA Change
+
Privilege Change
```

↓

```text
Potential Account Takeover
```

---

# 38. Correlation Advantages

```text
Higher Context
Higher Confidence
Attack Chain Visibility
Reduced Isolated Alerts
```

---

# 39. Correlation Limitations

Correlation can become:

```text
Complex
Resource Intensive
Difficult to Debug
Sensitive to Missing Events
```

If one event is missing:

```text
Entire Correlation
     ↓
May Fail
```

---

# 40. Sequence Detection

Sequence detection focuses on ordered events.

Example:

```text
Initial Access
      ↓
Execution
      ↓
Credential Access
      ↓
Lateral Movement
```

Sequence is particularly useful for attack-chain detection.

---

# 41. Sequence vs Correlation

### Correlation

```text
A + B + C
```

does not always require strict order.

### Sequence

```text
A → B → C
```

requires ordering.

---

# 42. Entity-Based Detection

Behavior is grouped around an entity.

Entities include:

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
 ↓
10 Failed Logins
 ↓
Successful Login
 ↓
MFA Change
```

---

# 43. Risk-Based Detection

Risk-based detection combines multiple signals into a score.

Example:

```text
Malicious IP       +40
Privileged User    +30
Critical Host      +30
Behavioral Anomaly +20
```

Total:

```text
120
```

Then:

```text
IF risk >= 100
THEN high-priority alert
```

---

# 44. Risk-Based Advantages

```text
Prioritization
Context
Aggregation
Reduced Alert Noise
```

Instead of:

```text
20 Independent Alerts
```

you can create:

```text
1 High-Risk Investigation
```

---

# 45. Risk-Based Limitations

Risk scoring can fail if:

```text
Weights Are Poor
Context Is Wrong
Data Is Missing
Risk Never Decays
Scores Become Inflated
```

Risk models require calibration.

---

# 46. Threat-Informed Detection

Threat-informed detection starts with:

```text
Threat Intelligence
+
Adversary Behavior
+
ATT&CK
+
Internal Incidents
```

Then builds:

```text
Detection Coverage
```

---

# 47. Threat-Informed Workflow

```text
Threat
 ↓
Adversary Behavior
 ↓
ATT&CK Technique
 ↓
Telemetry
 ↓
Detection
 ↓
Testing
 ↓
Coverage
```

---

# 48. Hybrid Detection

Hybrid detection combines multiple methodologies.

Example:

```text
IOC
+
Behavior
+
Anomaly
+
Correlation
+
Risk
```

This can provide stronger detection than any single method.

---

# 49. Hybrid Example

Suppose:

```text
User Login
```

Signals:

```text
New Device
+
Unusual Location
+
Known Malicious IP
+
Sensitive Resource Access
```

Then:

```text
Risk Score ↑
```

---

# 50. Detection Layering

A mature detection architecture can use multiple layers:

```text
Layer 1 → IOC
Layer 2 → Signature
Layer 3 → Behavior
Layer 4 → Anomaly
Layer 5 → Correlation
Layer 6 → Risk
```

The layers reinforce each other.

---

# 51. Defense in Depth for Detection

Do not rely on:

```text
One Detection
```

Instead:

```text
Multiple Independent Signals
```

Example:

```text
Email Detection
      +
Endpoint Detection
      +
DNS Detection
      +
Identity Detection
```

---

# 52. Detection Methodology Comparison

| Method | Best For | Strength | Weakness |
|---|---|---|---|
| Signature | Known patterns | Fast | Easy to evade |
| IOC | Known threats | Simple | Indicators change |
| Rule | Explicit behavior | Explainable | Can become complex |
| Threshold | Repetition | Simple | Static limits |
| Behavioral | TTPs | Resilient | Context required |
| Anomaly | Deviations | Finds unusual activity | False positives |
| Statistical | Quantitative anomalies | Adaptive | Baseline problems |
| Correlation | Multiple signals | High context | Complexity |
| Sequence | Attack chains | Order-aware | Missing events |
| Risk | Prioritization | Aggregates context | Calibration |
| Hybrid | Complex threats | Strong coverage | More engineering |

---

# 53. Choosing the Right Method

Ask:

```text
Is the threat known?
```

If yes:

```text
IOC / Signature
```

Then:

```text
Is there a repeatable behavior?
```

If yes:

```text
Rule / Behavioral
```

Then:

```text
Does the behavior depend on unusual activity?
```

If yes:

```text
Anomaly / Statistical
```

Then:

```text
Are multiple signals required?
```

If yes:

```text
Correlation / Sequence
```

Then:

```text
Does prioritization require multiple risk factors?
```

If yes:

```text
Risk-Based
```

Often the best answer is:

```text
Hybrid
```

---

# 54. Known Threat vs Unknown Threat

### Known Threat

Use:

```text
IOC
Signature
Known Pattern
```

### Unknown Threat

Consider:

```text
Behavior
Anomaly
Statistical
Correlation
```

---

# 55. Indicator-Based Detection

Useful when:

```text
Indicator is Reliable
Threat Is Active
Indicator Is Fresh
```

Example:

```text
Known Malicious Domain
```

---

# 56. Behavior-Based Detection

Useful when:

```text
Indicators Change Frequently
Attack Technique Is Stable
Behavior Is Observable
```

Example:

```text
Credential Dumping Behavior
```

---

# 57. Detection Evasion

Attackers may evade:

```text
IOC Detection
```

by changing:

```text
IP
Domain
Hash
Filename
```

Behavioral detections may remain useful if:

```text
Underlying TTP
```

remains similar.

---

# 58. Living-off-the-Land

Attackers may use legitimate tools:

```text
PowerShell
WMI
Windows Utilities
SSH
Python
Cloud APIs
```

Static malware signatures may fail.

Behavioral detection becomes particularly important.

---

# 59. Example – PowerShell

Weak:

```text
PowerShell Executed
```

Better:

```text
PowerShell
+
Unusual Parent
+
Suspicious Arguments
+
External Network
```

---

# 60. Example – DNS C2

Weak:

```text
DNS Query Exists
```

Better:

```text
Rare Domain
+
High Query Frequency
+
Long Queries
+
Suspicious Entropy
+
Periodic Connections
```

This is a behavioral/hybrid approach.

---

# 61. Example – Brute Force

Method:

```text
Threshold
```

Logic:

```text
20+ failures
within 5 minutes
against same account
```

Potential improvement:

```text
+
Known Scanner Context
+
User Criticality
+
Successful Login
```

---

# 62. Example – Password Spray

Method:

```text
Threshold
+
Entity Correlation
```

Logic:

```text
One Source IP
+
Many Usernames
+
Authentication Failures
```

---

# 63. Example – Account Takeover

Method:

```text
Behavior
+
Anomaly
+
Correlation
+
Risk
```

Sequence:

```text
Unusual Login
 ↓
New Device
 ↓
MFA Change
 ↓
Sensitive Access
```

---

# 64. Example – Ransomware

Method:

```text
Behavior
+
Threshold
+
Correlation
```

Signals:

```text
Mass File Changes
+
Suspicious Process
+
Backup Tampering
```

---

# 65. Example – Data Exfiltration

Method:

```text
Behavior
+
Statistical
+
Correlation
```

Signals:

```text
Sensitive Data Access
+
Unusual Volume
+
External Destination
```

---

# 66. Detection Confidence

Different methods provide different confidence levels.

Example:

```text
Known Malicious Hash
→ High Confidence

Single Anomaly
→ Lower Confidence

Multiple Correlated Behaviors
→ Higher Confidence
```

Confidence should be calibrated using evidence and testing.

---

# 67. Precision by Method

Conceptually:

```text
IOC / Signature
→ Often higher precision

Behavior
→ Variable

Anomaly
→ Often lower precision initially

Correlation
→ Can increase precision

Hybrid
→ Potentially strongest
```

Actual performance depends on implementation and environment.

---

# 68. Recall by Method

Conceptually:

```text
IOC
→ Limited to known indicators

Signature
→ Limited to known patterns

Behavior
→ Broader

Anomaly
→ Potentially broad

Hybrid
→ Can improve coverage
```

Again, real-world performance depends on telemetry and implementation quality.

---

# 69. Detection Coverage vs Detection Confidence

These are different.

### Coverage

```text
How much relevant behavior can we detect?
```

### Confidence

```text
How strongly does the evidence indicate malicious activity?
```

Example:

```text
High Coverage
+
Low Confidence
```

may create:

```text
Many Alerts
```

---

# 70. Detection Layer Strategy

Use:

```text
High-Confidence Detections
→ Immediate Alerts

Medium-Confidence Detections
→ Risk / Correlation

Low-Confidence Signals
→ Hunting / Enrichment
```

This prevents every weak signal from becoming an urgent alert.

---

# 71. Detection Pipeline

```text
Raw Event
    ↓
IOC Match?
    ↓
Behavior Match?
    ↓
Anomaly?
    ↓
Correlation?
    ↓
Risk?
    ↓
Severity
    ↓
Alert
```

---

# 72. Detection Chaining

One detection can become input to another.

Example:

```text
Suspicious Login
      ↓
Risk Score
      ↓
Sensitive Resource Access
      ↓
Higher Risk
      ↓
Incident
```

---

# 73. Detection Suppression

Low-confidence repetitive detections can be:

```text
Suppressed
Grouped
Aggregated
```

while high-confidence signals can remain immediate.

---

# 74. Detection Escalation

Conceptually:

```text
Low Risk
   ↓
Medium Risk
   ↓
High Risk
   ↓
Critical Risk
```

Context can escalate a signal.

Example:

```text
Anomalous Login
+
Privileged User
+
Critical Server
```

---

# 75. Detection Decay

Some signals should lose relevance over time.

Example:

```text
Risk = 100
 ↓
70
 ↓
40
 ↓
10
```

This prevents old activity from permanently increasing risk.

---

# 76. Detection Feedback

Analyst feedback can improve methodology selection.

Example:

```text
Detection
 ↓
100 Alerts
 ↓
90 False Positives
 ↓
Analysis
 ↓
Behavioral Context Added
 ↓
20 Alerts
 ↓
15 Useful
```

---

# 77. Detection Methodology Lifecycle

```text
Select Method
 ↓
Implement
 ↓
Test
 ↓
Measure
 ↓
Tune
 ↓
Compare
 ↓
Improve
```

Do not assume a methodology is effective simply because it is theoretically appropriate.

---

# 78. Combining Methodologies

Example:

```text
IOC
+
Behavior
```

or:

```text
Threshold
+
Anomaly
```

or:

```text
Behavior
+
Correlation
+
Risk
```

Hybrid detection is common in mature environments.

---

# 79. Detection Engineering Decision Tree

```text
             START
               │
               ▼
       Is indicator known?
          /           \
        YES            NO
        │               │
      IOC /          Is behavior
    Signature        observable?
                       /      \
                     YES       NO
                     │          │
                 Behavioral   Improve
                     │        Telemetry
                     ▼
              Is anomaly useful?
                 /        \
               YES         NO
               │            │
           Anomaly      Rule-Based
               │            │
               └─────┬──────┘
                     ▼
             Multiple signals?
                /          \
              YES           NO
               │             │
          Correlation      Single
          / Sequence       Detection
               │
               ▼
          Risk Required?
             /     \
           YES      NO
            │        │
          Risk     Alert
            │
            ▼
          ALERT
```

---

# 80. Practical Exercise – Detection Method Selection

For each scenario, choose a methodology.

### Scenario 1

Known malicious hash.

Answer:

```text
IOC / Signature
```

### Scenario 2

50 failed logins within 5 minutes.

Answer:

```text
Threshold
```

### Scenario 3

User suddenly downloads 100x their normal data volume.

Answer:

```text
Anomaly / Statistical
```

### Scenario 4

Failed login → successful login → MFA change.

Answer:

```text
Sequence / Correlation
```

### Scenario 5

Known malicious IP + suspicious process + critical host.

Answer:

```text
Hybrid / Risk-Based
```

---

# 81. Practical Exercise – Build Layered Detection

Threat:

```text
Account Takeover
```

Build:

```text
Layer 1:
Known Malicious IP

Layer 2:
Unusual Login

Layer 3:
New Device

Layer 4:
MFA Change

Layer 5:
Sensitive Access
```

Then:

```text
Correlate
 ↓
Risk Score
 ↓
Prioritize
```

---

# 82. Practical Exercise – Compare Methods

Take:

```text
Password Spray
```

Implement conceptually using:

```text
Threshold
Behavior
Correlation
Risk
```

Compare:

```text
Alert Volume
Precision
Context
Complexity
Performance
```

---

# 83. Practical Exercise – Build an Anomaly

Choose:

```text
User Login Frequency
```

Establish:

```text
Baseline
```

Then detect:

```text
Significant Deviation
```

Test against:

```text
Normal Day
Weekend
Holiday
Incident
Legitimate Travel
```

---

# 84. Practical Exercise – Hybrid Detection

Threat:

```text
Suspicious Cloud Account
```

Combine:

```text
Unusual Login
+
New Device
+
MFA Change
+
Privilege Change
+
Sensitive API Activity
```

Then:

```text
Risk Score
```

---

# 85. Common Mistakes

## Mistake 1

Using only IOCs.

Problem:

```text
Indicators Change
```

---

## Mistake 2

Alerting on every anomaly.

Problem:

```text
Anomaly ≠ Malicious
```

---

## Mistake 3

Using static thresholds everywhere.

Problem:

```text
Different Users Have Different Baselines
```

---

## Mistake 4

Creating overly complex correlations.

Problem:

```text
Hard to Maintain
Hard to Debug
Sensitive to Missing Data
```

---

## Mistake 5

Ignoring context.

Problem:

```text
Low Confidence
High Alert Volume
```

---

## Mistake 6

Assuming one methodology fits every threat.

Correct:

```text
Choose Based on Threat + Telemetry + Objective
```

---

# 86. Methodology Selection Checklist

Before choosing a detection approach:

```text
[ ] Is the threat known?
[ ] Is a reliable IOC available?
[ ] Is the behavior observable?
[ ] Is a baseline available?
[ ] Is sufficient historical data available?
[ ] Are multiple signals required?
[ ] Is event ordering important?
[ ] Is risk prioritization required?
[ ] What is the acceptable false-positive rate?
[ ] What is the required detection speed?
[ ] What telemetry is available?
[ ] What is the query/compute cost?
```

---

# 87. Interview Questions

### What are common detection methodologies?

> Signature, IOC, rule-based, threshold, behavioral, anomaly, statistical, correlation, sequence, risk-based, threat-informed, and hybrid detection.

### What is signature-based detection?

> Detection based on a known pattern associated with malicious activity.

### What is IOC-based detection?

> Detection based on known indicators such as malicious IPs, domains, URLs, or hashes.

### What is behavioral detection?

> Detection based on suspicious activity patterns rather than relying only on known indicators.

### What is anomaly detection?

> Detection that identifies activity deviating from an established baseline or expected behavior.

### What is threshold detection?

> Detection that triggers when an event count or value crosses a predefined threshold within a defined context or time window.

### What is correlation detection?

> Combining multiple related events to identify a higher-confidence security condition.

### What is sequence detection?

> Detection that identifies a specific ordered chain of events.

### What is risk-based detection?

> Combining multiple signals and contextual factors into a risk score used for prioritization or alerting.

### Why use hybrid detection?

> Different methodologies have different strengths, and combining them can improve coverage, context, and confidence.

### Which is better: IOC or behavioral detection?

> Neither is universally better. IOCs are effective for known threats, while behavioral detection can better identify modified or previously unknown variants.

### Why can anomaly detection produce false positives?

> Legitimate changes in user, business, or system behavior can appear anomalous.

---

# 88. Quick Revision

```text
Signature
→ Known malicious pattern

IOC
→ Known malicious indicator

Rule
→ Explicit conditions

Threshold
→ Count/value exceeds limit

Behavior
→ Suspicious activity pattern

Anomaly
→ Deviation from normal

Statistical
→ Mathematical deviation

Correlation
→ Multiple related events

Sequence
→ Ordered events

Risk
→ Combined prioritization

Threat-Informed
→ Detection based on adversary knowledge

Hybrid
→ Multiple methodologies combined
```

---

# 89. Golden Rules

```text
1. No single detection methodology detects everything.

2. Start with the threat and behavior.

3. Use IOCs for known threats.

4. Use signatures for recognizable patterns.

5. Use thresholds for repetitive behavior.

6. Use behavioral detection for attacker TTPs.

7. Use anomaly detection for deviations from expected behavior.

8. An anomaly is not automatically malicious.

9. Use statistical methods when quantitative baselines are reliable.

10. Use correlation when individual signals are weak.

11. Use sequence detection when event ordering matters.

12. Use risk scoring to prioritize multiple signals.

13. Use hybrid detection for complex threats.

14. Layer detections instead of depending on one signal.

15. Context generally improves detection quality.

16. Static thresholds may not work across different entities.

17. Baselines must account for seasonality and legitimate change.

18. Complex correlations can fail when telemetry is missing.

19. Measure precision and recall where practical.

20. Select methodology based on telemetry availability.

21. Consider performance and operational cost.

22. Test each methodology against realistic behavior.

23. Continuously tune detection methodologies.

24. Threat-informed detection should drive important coverage decisions.

25. The best methodology is the one that reliably produces useful security outcomes for the specific threat and environment.
```

---

# 90. Final Mental Model

Think of detection methodologies as different lenses:

```text
KNOWN?
  ↓
IOC / SIGNATURE

REPETITIVE?
  ↓
THRESHOLD

BEHAVIORAL?
  ↓
RULE / BEHAVIOR

UNUSUAL?
  ↓
ANOMALY / STATISTICAL

MULTIPLE SIGNALS?
  ↓
CORRELATION

ORDERED ATTACK?
  ↓
SEQUENCE

MULTIPLE RISK FACTORS?
  ↓
RISK

COMPLEX THREAT?
  ↓
HYBRID
```

A mature detection program combines these lenses:

```text
IOC
 +
Signature
 +
Behavior
 +
Anomaly
 +
Correlation
 +
Risk
      ↓
High-Confidence Detection
```

---

# 91. Chapter Summary

This chapter covered the major detection methodologies used in modern security operations:

```text
Signature-Based
IOC-Based
Rule-Based
Threshold-Based
Behavioral
Anomaly
Statistical
Correlation
Sequence
Risk-Based
Threat-Informed
Hybrid
```

The key lesson is:

> **Detection engineering is not about choosing the most sophisticated detection method. It is about choosing the appropriate method—or combination of methods—for the threat, telemetry, environment, and operational objective.**

The next chapter focuses specifically on **IOC, Signature & Indicator-Based Detection**, including indicator types, matching strategies, threat-intelligence integration, IOC lifecycle, freshness, confidence, false positives, and the limitations of indicator-driven detection.
```