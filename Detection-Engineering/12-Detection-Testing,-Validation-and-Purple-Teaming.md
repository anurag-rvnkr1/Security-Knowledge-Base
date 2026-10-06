# Chapter 12 – Detection Testing, Validation & Purple Teaming

> A detection that has never been tested is only a hypothesis. Detection testing validates that adversary behavior produces the expected telemetry, triggers the intended detection, creates an actionable alert, and remains effective under realistic variations. Purple teaming extends this process by bringing offensive and defensive teams together to continuously improve detection capability.

---

# 1. Introduction

Detection engineering does not end when a rule is written.

The actual lifecycle is:

```text
Detection Idea
      ↓
Detection Logic
      ↓
Implementation
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
Retesting
```

The key question is:

> **Can we prove that this detection works?**

---

# 2. Why Detection Testing Matters

Without testing, a detection may:

```text
Never Trigger
Trigger Too Often
Miss Variations
Depend on Missing Data
Break After Schema Changes
Perform Poorly
Generate Unactionable Alerts
```

Testing provides evidence.

---

# 3. Detection Testing vs Detection Validation

## Detection Testing

Determines whether:

```text
Expected Input
→
Expected Detection
```

occurs.

## Detection Validation

Determines whether the detection provides:

```text
Reliable
Accurate
Timely
Actionable
Security Value
```

---

# 4. Detection Testing Lifecycle

```text
Threat
 ↓
Technique
 ↓
Hypothesis
 ↓
Test Scenario
 ↓
Telemetry
 ↓
Detection
 ↓
Alert
 ↓
Analyst Validation
 ↓
Improvement
```

---

# 5. Detection Hypothesis

A detection hypothesis should describe:

```text
Expected Adversary Behavior
Expected Telemetry
Expected Detection
Expected Response
```

Example:

```text
Hypothesis:

An attacker executing suspicious scripting activity
may create a distinctive process chain and network
connection that can be detected using endpoint telemetry.
```

---

# 6. Test Objectives

A detection test should answer:

```text
Did the activity execute?
Did telemetry appear?
Did the rule trigger?
Did the alert contain context?
Was detection timely?
Was severity appropriate?
Could analysts investigate it?
```

---

# 7. Detection Test Levels

Testing can occur at several levels:

```text
Unit
Integration
System
End-to-End
Adversary Simulation
Purple Team
Production Validation
```

---

# 8. Unit Testing

Tests a small part of detection logic.

Example:

```text
Input:
Suspicious Command

Expected:
Match
```

---

# 9. Negative Unit Testing

Example:

```text
Input:
Known Legitimate Command

Expected:
No Match
```

This helps reduce false positives.

---

# 10. Integration Testing

Tests whether:

```text
Telemetry
+
Parser
+
Detection
```

work together.

Example:

```text
Endpoint Event
 ↓
Parser
 ↓
Normalized Event
 ↓
Detection
```

---

# 11. End-to-End Testing

Tests the complete pipeline:

```text
Simulated Activity
 ↓
Endpoint / Network / Identity
 ↓
Log Collection
 ↓
SIEM
 ↓
Detection
 ↓
Alert
 ↓
SOC Workflow
```

---

# 12. Telemetry Validation

Before testing the rule, confirm:

```text
Required Data Source
Required Fields
Correct Timestamp
Correct Entity
Correct Event
```

A detection cannot work if its required telemetry is missing.

---

# 13. Test Data Sources

Possible telemetry:

```text
Endpoint
Network
Identity
Cloud
Application
Container
Kubernetes
Email
DNS
Proxy
Firewall
```

---

# 14. Test Environment

Prefer:

```text
Dedicated Lab
Test Tenant
Test Account
Test Host
Controlled Network
```

rather than uncontrolled production activity.

---

# 15. Authorization

Security testing should be:

```text
Authorized
Controlled
Documented
Scoped
Reversible
```

---

# 16. Atomic Testing

Atomic testing validates a specific behavior or technique independently.

Conceptually:

```text
Technique
 ↓
Controlled Test
 ↓
Telemetry
 ↓
Detection
```

It answers:

```text
Can we detect this specific behavior?
```

---

# 17. Atomic Test Characteristics

A good atomic test should define:

```text
Objective
Technique
Prerequisites
Execution
Expected Telemetry
Expected Detection
Cleanup
```

---

# 18. Atomic Test Example

Conceptual:

```text
Technique:
Suspicious Script Execution

Test:
Execute controlled benign script

Expected:
Process creation event

Expected Detection:
Script execution alert
```

The test should use a safe, authorized simulation.

---

# 19. Adversary Simulation

Adversary simulation combines multiple behaviors:

```text
Initial Access
 ↓
Execution
 ↓
Persistence
 ↓
Discovery
 ↓
Lateral Movement
```

This tests whether detections work across a realistic attack chain.

---

# 20. Scenario-Based Testing

Instead of testing isolated rules:

```text
Test Detection A
Test Detection B
Test Detection C
```

test:

```text
Attack Scenario
 ↓
Multiple Behaviors
 ↓
Multiple Detections
```

This reveals correlation gaps.

---

# 21. Purple Teaming

Purple teaming combines:

```text
Offensive Security
+
Defensive Security
```

The goal is collaborative improvement.

It is not simply:

```text
Red Team attacks
Blue Team watches
```

Instead:

```text
Attack
 ↓
Observe
 ↓
Detect
 ↓
Investigate
 ↓
Improve
 ↓
Retest
```

---

# 22. Red Team Role

The offensive side may:

```text
Simulate Adversary Behavior
Execute Authorized Scenarios
Test Defensive Assumptions
Identify Blind Spots
```

---

# 23. Blue Team Role

The defensive side:

```text
Monitor
Detect
Investigate
Hunt
Respond
Identify Gaps
Improve Detections
```

---

# 24. Purple Team Role

Purple teaming creates the feedback loop:

```text
Red Activity
      ↓
Blue Observation
      ↓
Gap Identified
      ↓
Detection Improvement
      ↓
Retest
```

---

# 25. Purple Team Objectives

Typical objectives:

```text
Validate Detection
Measure Visibility
Find Telemetry Gaps
Improve Alert Quality
Measure Detection Latency
Validate Response
Improve Coverage
```

---

# 26. Purple Team Planning

Before an exercise define:

```text
Objective
Scope
Threat Scenario
Techniques
Assets
Telemetry
Expected Detections
Success Criteria
Safety Controls
Cleanup
```

---

# 27. Scope

Define:

```text
Hosts
Users
Accounts
Cloud Resources
Applications
Networks
Time Window
```

Avoid ambiguous scope.

---

# 28. Success Criteria

Example:

```text
Technique:
TXXXX

Expected:
Telemetry within 30 seconds

Detection:
Triggered within 2 minutes

Alert:
Contains user + host + process

Result:
PASS
```

---

# 29. Detection Test Matrix

| Test | Telemetry | Detection | Alert | Latency | Result |
|---|---|---|---|---|---|
| Test A | Yes | Yes | Yes | 20s | Pass |
| Test B | Yes | No | — | — | Fail |
| Test C | Partial | Yes | Yes | 90s | Partial |

---

# 30. Detection Coverage Test

For each technique:

```text
Technique
 ↓
Simulation
 ↓
Telemetry
 ↓
Detection
 ↓
Alert
```

Record the result.

---

# 31. Coverage Categories

Use:

```text
Detected
Partially Detected
Telemetry Only
Not Detected
Not Applicable
```

---

# 32. Detection Gap

Example:

```text
Attack Executed
      ↓
Telemetry Available
      ↓
No Detection
```

This is a detection engineering gap.

---

# 33. Telemetry Gap

Example:

```text
Attack Executed
      ↓
Required Telemetry Missing
      ↓
Detection Impossible
```

This is a visibility/collection gap.

---

# 34. Alert Context Gap

Example:

```text
Detection Triggered
      ↓
Alert Missing User
Missing Host
Missing Process
```

The detection may technically work but remain difficult to investigate.

---

# 35. Response Gap

Example:

```text
Detection
 ↓
Alert
 ↓
No Documented Response
```

The detection capability exists, but operational response is weak.

---

# 36. Testing Pyramid

A useful model:

```text
            Purple Team
          / Adversary Test \
        ---------------------
        End-to-End Testing
      -------------------------
       Integration Testing
    -----------------------------
         Unit Testing
```

Most routine tests should be automated at lower levels.

---

# 37. Test Frequency

Different tests can run at different frequencies:

```text
Unit Tests
→ Every Change

Integration Tests
→ Every Change / Release

Regression Tests
→ Every Change

Production Validation
→ Periodic

Purple Team
→ Scheduled Exercises
```

---

# 38. Regression Testing

Whenever detection logic changes:

```text
Existing Tests
+
New Tests
```

should run.

---

# 39. Regression Example

Original:

```text
Detect suspicious process.
```

Change:

```text
Add exception for admin hosts.
```

Regression tests must confirm:

```text
Suspicious process
→ Still detected

Admin host
→ Expected suppression
```

---

# 40. Boundary Testing

Test around thresholds.

If rule triggers at:

```text
10 events
```

test:

```text
9
10
11
```

---

# 41. Time-Window Testing

For a:

```text
5-minute correlation
```

test:

```text
4:59
5:00
5:01
```

This catches timing bugs.

---

# 42. Null Testing

Test missing values:

```text
user = null
host = null
source.ip = null
process = null
```

Detection behavior should be predictable.

---

# 43. Duplicate Event Testing

Duplicate telemetry can cause:

```text
Duplicate Alerts
Incorrect Counts
Incorrect Risk Scores
```

Test:

```text
Same Event
Repeated Twice
```

---

# 44. Delayed Event Testing

Distributed systems can produce:

```text
Event Time:
10:00

Arrival Time:
10:03
```

Detection logic should account for ingestion delay where appropriate.

---

# 45. Out-of-Order Events

Example:

```text
Event B arrives
before
Event A
```

Sequence detections must account for event ordering problems.

---

# 46. Missing Event Testing

Test:

```text
Expected Event A
Missing

Event B
Present
```

This can reveal fragile correlation logic.

---

# 47. Replay Testing

Replay historical or synthetic events:

```text
Dataset
 ↓
Detection
 ↓
Expected Results
```

Useful for regression and backtesting.

---

# 48. Historical Incident Replay

Known incidents can be replayed to determine:

```text
Would we detect it today?
```

This is one of the most valuable validation methods.

---

# 49. Detection Latency

Measure:

```text
Activity Time
 ↓
Telemetry Time
 ↓
Processing Time
 ↓
Detection Time
 ↓
Alert Time
```

---

# 50. Detection Latency Formula

Conceptually:

```text
Detection Latency =
Alert Time - Activity Time
```

More detailed measurement:

```text
Collection Latency
+
Processing Latency
+
Detection Latency
+
Alerting Latency
```

---

# 51. Mean Time to Detect

MTTD commonly represents:

```text
Average time required to detect an event.
```

Lower is generally better, but quality must not be sacrificed for speed.

---

# 52. Detection Quality Metrics

Track:

```text
Precision
Recall
False Positive Rate
False Negative Rate
Detection Latency
Alert Volume
Coverage
```

---

# 53. Precision

```text
Precision =
TP / (TP + FP)
```

Measures how many alerts are actually meaningful.

---

# 54. Recall

```text
Recall =
TP / (TP + FN)
```

Measures how many relevant malicious events are detected.

---

# 55. Detection Test Scoring

A simple internal score could consider:

```text
Telemetry
Detection
Context
Latency
Accuracy
Response
```

Example:

```text
Telemetry: 1
Detection: 1
Context: 1
Latency: 1
Response: 0

Score:
4 / 5
```

The scoring methodology should be defined internally.

---

# 56. False Positive Testing

Include known legitimate behaviors:

```text
Administrative Activity
Software Updates
Backup
Monitoring
Automation
Security Scanners
CI/CD
```

---

# 57. False Negative Testing

Attempt reasonable variations:

```text
Different User
Different Host
Different Tool
Different Path
Different Command
Different Timing
```

The goal is to identify detection brittleness.

---

# 58. Detection Evasion Testing

Evaluate whether minor variations bypass detection.

Conceptually:

```text
Original Behavior
      ↓
Detection

Variant Behavior
      ↓
Detection?
```

Testing should remain authorized and controlled.

---

# 59. Detection Robustness

A robust detection identifies:

```text
Underlying Behavior
```

rather than only:

```text
Exact String
```

---

# 60. Example of Brittle Detection

Bad:

```text
Command contains:
"exact-string"
```

An attacker may change:

```text
Whitespace
Case
Arguments
Encoding
```

and evade it.

---

# 61. Behavioral Detection

Better:

```text
Suspicious Parent
+
Sensitive Child Process
+
Unusual User
+
External Connection
```

This uses multiple behavioral signals.

---

# 62. Purple Team Detection Loop

```text
Threat Intelligence
      ↓
Scenario
      ↓
Simulation
      ↓
Telemetry
      ↓
Detection
      ↓
Alert
      ↓
Investigation
      ↓
Gap
      ↓
Engineering
      ↓
Retest
```

---

# 63. Detection Gap Categories

Record:

```text
Telemetry Gap
Detection Gap
Correlation Gap
Context Gap
Performance Gap
Response Gap
Coverage Gap
```

---

# 64. Correlation Gap

Example:

```text
Identity Event
+
Endpoint Event
+
Network Event
```

all exist but:

```text
No correlation
```

The individual detections work, but the attack chain is missed.

---

# 65. Context Gap

Alert:

```text
Suspicious Process
```

but lacks:

```text
User
Host
Parent
Destination
Command Line
```

Analyst investigation becomes harder.

---

# 66. Performance Gap

Detection:

```text
Correct
```

but:

```text
Takes 20 minutes
```

for an attack requiring rapid response.

---

# 67. Response Gap

Detection:

```text
Correct
```

but:

```text
No Playbook
No Owner
No Escalation
```

---

# 68. Purple Team Evidence

Capture:

```text
Test ID
Technique
Time
Host
User
Command / Activity
Telemetry
Alert
Screenshot
Detection ID
Result
```

Avoid storing unnecessary sensitive data.

---

# 69. Detection Test Evidence

A test record can contain:

```yaml
test_id: PT-001

technique: TXXXX

detection_id: DET-001

environment: lab

started_at: ...

completed_at: ...

telemetry_observed: true

detection_triggered: true

alert_created: true

latency_seconds: 32

result: pass
```

---

# 70. Test Result States

Use:

```text
PASS
FAIL
PARTIAL
BLOCKED
NOT APPLICABLE
```

---

# 71. Blocked Test

A test may be blocked because:

```text
Telemetry Missing
Environment Unavailable
Permission Missing
Safety Constraint
```

Do not classify blocked tests as passes.

---

# 72. Detection Validation Report

Include:

```text
Executive Summary
Scope
Techniques
Tests
Results
Detection Gaps
Telemetry Gaps
False Positives
Latency
Recommendations
Retest Status
```

---

# 73. Purple Team Report

A useful structure:

```text
1. Objective
2. Scope
3. Scenario
4. Techniques
5. Detection Results
6. Gaps
7. Improvements
8. Retest
9. Final Coverage
```

---

# 74. Example Purple Team Scenario

```text
Scenario:
Compromised Identity

Step 1:
Suspicious Authentication

Step 2:
Privilege Change

Step 3:
Endpoint Access

Step 4:
Internal Discovery

Step 5:
Remote Access

Step 6:
Data Access
```

Test each step.

---

# 75. Scenario Coverage Matrix

| Stage | Technique | Telemetry | Detection | Alert | Result |
|---|---|---|---|---|---|
| Authentication | T1 | Yes | Yes | Yes | Pass |
| Privilege | T2 | Yes | Yes | Yes | Pass |
| Discovery | T3 | Yes | No | No | Fail |
| Lateral Movement | T4 | Partial | Yes | Yes | Partial |

---

# 76. Purple Team Improvement

After a failed test:

```text
Identify Cause
      ↓
Improve Telemetry
or
Improve Detection
or
Improve Correlation
      ↓
Retest
```

---

# 77. Never Stop at the First Fix

After changing the rule:

```text
Retest Positive
+
Retest Negative
+
Retest Regression
```

---

# 78. Production Validation

After deployment:

```text
Verify Data
Verify Execution
Verify Alerts
Verify Latency
Verify Analyst Context
```

---

# 79. Detection Health Test

A detection can have:

```text
Functional Test
```

and:

```text
Operational Health Test
```

Example:

```text
Functional:
Known behavior triggers.

Operational:
Detection continues receiving telemetry.
```

---

# 80. Detection Canary Validation

Deploy to:

```text
Limited Scope
```

Then compare:

```text
Expected Alert Rate
vs
Observed Alert Rate
```

---

# 81. Alert Storm Detection

A failed rule may cause:

```text
100 alerts
→
100,000 alerts
```

Detection testing should include volume safeguards.

---

# 82. Alert Suppression Testing

If suppression exists:

```text
Expected suppressed event
→ No alert

Expected malicious event
→ Alert
```

---

# 83. Exception Testing

For each exception:

```text
Exception Condition
+
Normal Activity
+
Suspicious Activity
```

Verify only intended events are suppressed.

---

# 84. Testing Threat-Informed Coverage

Use ATT&CK to identify:

```text
Relevant Techniques
```

Then test:

```text
Technique
 ↓
Simulation
 ↓
Detection
```

This creates measurable threat-informed coverage.

---

# 85. ATT&CK Coverage Validation

Do not report:

```text
Technique covered
```

unless there is evidence such as:

```text
Telemetry
+
Detection
+
Test
```

---

# 86. Coverage Confidence

A useful internal model:

```text
Telemetry Only
→ Low Confidence

Detection Exists
→ Medium Confidence

Detection Tested
→ High Confidence

Detection Tested + Purple Team
→ Very High Confidence
```

The exact terminology should be organization-specific.

---

# 87. Detection Testing in CI/CD

Automate:

```text
Schema
 ↓
Lint
 ↓
Unit Tests
 ↓
Regression Tests
 ↓
Query Tests
```

Manual:

```text
Purple Team
End-to-End
Production Validation
```

---

# 88. Automated vs Manual Testing

### Automate

```text
Syntax
Schema
Unit
Regression
Query
Performance
```

### Human-Led

```text
Threat Scenario
Purple Team
Investigation
Response
```

---

# 89. Test Automation

Example:

```text
Pull Request
      ↓
CI
      ↓
100 Detection Tests
      ↓
98 Pass
2 Fail
      ↓
Merge Blocked
```

---

# 90. Detection Test Coverage

Measure:

```text
Total Detections
vs
Detections With Tests
```

Example:

```text
200 detections
150 tested

Test Coverage:
75%
```

---

# 91. Test Coverage Is Not Detection Coverage

Important distinction:

```text
Test Coverage
≠
ATT&CK Coverage
```

A detection may have tests but still cover only a narrow procedure.

---

# 92. Test Quality

A high test count does not guarantee quality.

A good test should be:

```text
Relevant
Repeatable
Safe
Deterministic
Documented
```

---

# 93. Deterministic Testing

Prefer predictable inputs and expected outputs.

Avoid tests dependent on:

```text
Random External Infrastructure
Unstable Services
Uncontrolled Network
```

when possible.

---

# 94. Repeatability

A good test should produce consistent results:

```text
Run 1 → Pass
Run 2 → Pass
Run 3 → Pass
```

If results vary:

```text
Investigate
```

---

# 95. Test Cleanup

Every simulation should define cleanup:

```text
Temporary Accounts
Temporary Files
Test Resources
Temporary Permissions
Network Changes
```

---

# 96. Test Safety

Use:

```text
Isolated Assets
Controlled Credentials
Limited Scope
Non-Destructive Actions
Monitoring
Rollback
```

---

# 97. Test Documentation

Document:

```text
Purpose
Prerequisites
Steps
Expected Result
Observed Result
Cleanup
Owner
Date
```

---

# 98. Detection Test Naming

Example:

```text
TEST-IDENTITY-ACCOUNT-TAKEOVER-001
TEST-ENDPOINT-EXECUTION-002
TEST-CLOUD-IAM-003
```

---

# 99. Detection Test IDs

Stable IDs allow:

```text
Detection
 ↕
Test
```

to remain linked.

---

# 100. Detection-Test Mapping

Example:

```yaml
detection_id: DET-001

tests:
  - TEST-001
  - TEST-002
  - TEST-003
```

---

# 101. Purple Team Test Mapping

Example:

```yaml
scenario_id: PT-001

techniques:
  - TXXXX
  - TYYYY

detections:
  - DET-001
  - DET-002
```

---

# 102. Detection Validation Dashboard

Useful metrics:

```text
Tests Executed
Tests Passed
Tests Failed
Coverage
Detection Latency
False Positives
Detection Gaps
Telemetry Gaps
```

---

# 103. Purple Team Metrics

Possible metrics:

```text
Technique Coverage
Detection Success Rate
Telemetry Coverage
Detection Latency
Alert Quality
Investigation Time
Response Success
Retest Success
```

---

# 104. Detection Success Rate

Conceptually:

```text
Successful Detection Tests
/
Total Applicable Tests
```

---

# 105. Retest Rate

Track:

```text
Failed Tests
→ Fixed
→ Retested
```

A failed test should remain visible until validated.

---

# 106. Detection Gap Aging

Track:

```text
Gap Identified
 ↓
Engineering Started
 ↓
Fix Completed
 ↓
Retested
```

This helps measure remediation speed.

---

# 107. Purple Team Backlog

Example:

```text
PT-001
Discovery Detection Gap
Priority: High

PT-002
Cloud IAM Detection Gap
Priority: Critical

PT-003
Container Visibility Gap
Priority: Medium
```

---

# 108. Common Testing Mistakes

## Mistake 1

Only testing whether the query runs.

```text
Query Works
≠
Detection Works
```

---

## Mistake 2

Only testing positive cases.

You also need:

```text
Negative
Regression
Edge
```

---

## Mistake 3

Testing only one procedure.

Attackers can vary implementation.

---

## Mistake 4

Ignoring telemetry.

A detection can fail before the query even executes.

---

## Mistake 5

Ignoring timing.

Sequence detections depend on event ordering and windows.

---

## Mistake 6

Ignoring duplicates.

Duplicate events can inflate counts.

---

## Mistake 7

Ignoring false positives.

A detection that overwhelms analysts is operationally weak.

---

## Mistake 8

No retesting.

A fix is not proven until validated.

---

## Mistake 9

No production validation.

Staging may not represent production accurately.

---

## Mistake 10

Treating purple teaming as an attack-only exercise.

The objective is defensive improvement.

---

# 109. Practical Exercise – Unit Testing

Create:

```text
1 Positive Event
1 Negative Event
1 Edge Event
```

Run:

```text
Detection
```

Expected:

```text
Positive → Match
Negative → No Match
Edge → Defined Behavior
```

---

# 110. Practical Exercise – Integration Test

Simulate:

```text
Event
 ↓
Parser
 ↓
Normalization
 ↓
Detection
 ↓
Alert
```

Verify every stage.

---

# 111. Practical Exercise – Historical Replay

Take a known historical event dataset.

Run:

```text
Current Detection
```

Measure:

```text
Detected
Missed
False Positive
Latency
```

---

# 112. Practical Exercise – Purple Team

Choose one relevant technique.

Document:

```text
Technique
Threat Scenario
Scope
Simulation
Expected Telemetry
Expected Detection
Actual Result
Gap
Fix
Retest
```

---

# 113. Practical Exercise – Detection Resilience

Test variations in:

```text
User
Host
Command
Path
Timing
Destination
Process
```

Determine:

```text
Detected
or
Missed
```

---

# 114. Practical Exercise – End-to-End

Build:

```text
Identity Event
 ↓
Endpoint Event
 ↓
Network Event
 ↓
Correlation
 ↓
Alert
 ↓
SOC Investigation
```

Measure the complete latency.

---

# 115. Test Case Template

```yaml
test_id: TEST-001

name: Suspicious Authentication Test

detection_id: DET-001

objective: >
  Validate detection of suspicious authentication behavior.

technique:
  - TXXXX

environment: test

preconditions:
  - test_account_exists

expected_telemetry:
  - authentication_event

expected_detection:
  - DET-001

expected_alert: true

expected_latency_seconds: 120

cleanup:
  - revoke_test_session

result: pass
```

---

# 116. Purple Team Scenario Template

```yaml
scenario_id: PT-001

name: Cloud Account Compromise

objective: >
  Validate detection of suspicious cloud identity activity.

scope:
  accounts:
    - test-account

techniques:
  - TXXXX
  - TYYYY

detections:
  - DET-001
  - DET-002

success_criteria:
  telemetry: true
  detection: true
  alert: true
  response: documented

status: completed
```

---

# 117. Detection Validation Checklist

```text
[ ] Threat scenario defined
[ ] Scope approved
[ ] Test environment ready
[ ] Required telemetry available
[ ] Positive test created
[ ] Negative test created
[ ] Regression test created
[ ] Edge cases tested
[ ] Timing tested
[ ] Duplicate events tested
[ ] Missing fields tested
[ ] Delayed events tested
[ ] Detection triggered
[ ] Alert generated
[ ] Alert context validated
[ ] Detection latency measured
[ ] False positives evaluated
[ ] False negatives considered
[ ] Cleanup completed
[ ] Results documented
[ ] Failed tests remediated
[ ] Retest completed
```

---

# 118. Interview Questions

### Why is detection testing important?

> It provides evidence that the detection actually observes and identifies the intended behavior instead of merely existing as configuration.

### What is the difference between testing and validation?

> Testing checks whether expected behavior triggers the detection; validation evaluates whether the resulting detection is reliable, timely, accurate, and useful to defenders.

### What is atomic testing?

> Testing an individual adversary behavior or technique in a controlled environment to verify the associated telemetry and detection.

### What is purple teaming?

> A collaborative process between offensive and defensive teams to simulate relevant adversary behavior, evaluate detection and response, identify gaps, and improve defenses.

### What is a telemetry gap?

> A situation where required data needed to detect a behavior is missing or unavailable.

### What is a detection gap?

> A situation where relevant telemetry exists but the organization lacks effective detection logic.

### What is a correlation gap?

> A situation where individual events are visible but are not combined into a meaningful attack sequence.

### Why test negative cases?

> To determine whether legitimate activity incorrectly triggers the detection and to control false positives.

### Why test boundary conditions?

> Threshold and time-window logic can behave incorrectly around boundaries, causing false positives or false negatives.

### What is regression testing?

> Re-running existing tests after changes to ensure previously correct behavior remains correct.

### What is detection latency?

> The time between the underlying activity and the resulting actionable detection or alert.

### Why test event delays?

> Distributed systems can deliver telemetry later than the event's actual occurrence, which can break time-based correlation.

### What should a purple team exercise measure?

> Telemetry visibility, detection success, alert quality, detection latency, investigation capability, response capability, and gaps.

### Why is historical replay valuable?

> It allows teams to determine whether current detections would have identified previously observed incidents.

---

# 119. Quick Revision

```text
Detection Testing
→ Proves detection behavior

Detection Validation
→ Evaluates reliability and operational value

Unit Test
→ Tests individual logic

Integration Test
→ Tests telemetry + parser + detection

End-to-End Test
→ Tests full detection pipeline

Atomic Test
→ Tests one specific behavior

Adversary Simulation
→ Tests realistic attack behavior

Purple Team
→ Offensive + defensive collaboration

Positive Test
→ Expected malicious behavior should trigger

Negative Test
→ Legitimate behavior should not trigger

Regression Test
→ Prevents previously fixed problems from returning

Boundary Test
→ Tests thresholds and time-window edges

Replay
→ Reuses historical or synthetic events

Backtesting
→ Evaluates detection against historical data

Telemetry Gap
→ Required visibility missing

Detection Gap
→ Telemetry exists but detection missing

Correlation Gap
→ Events exist but relationship is not detected

Context Gap
→ Alert lacks investigation information

Performance Gap
→ Detection is too slow or expensive

Response Gap
→ Detection exists but response workflow is missing

Detection Latency
→ Time from activity to alert

Purple Team Loop
→ Simulate → Observe → Detect → Improve → Retest
```

---

# 120. Golden Rules

```text
1. A detection that has never been tested is only a hypothesis.

2. Test both positive and negative behavior.

3. Test realistic variations.

4. Test telemetry before blaming detection logic.

5. Validate the entire detection pipeline.

6. Test thresholds and time boundaries.

7. Test delayed and out-of-order events.

8. Test duplicate events.

9. Test missing fields.

10. Maintain regression tests.

11. Use historical incidents for replay where possible.

12. Measure detection latency.

13. Measure alert quality.

14. Measure false positives.

15. Consider false negatives.

16. Test at realistic event volumes.

17. Validate alert context.

18. Test exceptions.

19. Test suppression behavior.

20. Retest every important fix.

21. Use ATT&CK to guide threat-informed testing.

22. Use atomic tests for repeatable behavior validation.

23. Use end-to-end tests for operational validation.

24. Use purple teaming for realistic adversary scenarios.

25. Purple teaming is collaborative improvement, not competition.

26. Document every important test result.

27. Do not classify blocked tests as passes.

28. Track unresolved detection gaps.

29. Track the age of detection gaps.

30. Test detections after major telemetry changes.

31. Test detections after schema changes.

32. Test detections after query changes.

33. Test detections after environment changes.

34. Validate production behavior after deployment.

35. Treat detection testing as a continuous lifecycle.

36. The goal is not to prove that a rule exists.

37. The goal is to prove that defenders can reliably observe, detect, investigate, and respond to relevant adversary behavior.
```

---

# 121. Final Mental Model

Think of detection validation as:

```text
CAN WE SEE IT?
      ↓
CAN WE DETECT IT?
      ↓
CAN WE CORRELATE IT?
      ↓
CAN WE ALERT ON IT?
      ↓
CAN AN ANALYST UNDERSTAND IT?
      ↓
CAN WE RESPOND?
      ↓
CAN WE REPEAT THE TEST?
      ↓
CAN WE PROVE IT STILL WORKS?
```

The mature detection validation lifecycle is:

```text
THREAT
  ↓
SCENARIO
  ↓
SIMULATION
  ↓
TELEMETRY
  ↓
DETECTION
  ↓
ALERT
  ↓
INVESTIGATION
  ↓
RESPONSE
  ↓
GAP
  ↓
ENGINEERING
  ↓
RETEST
```

And the purple-team feedback loop is:

```text
RED ACTIVITY
     ↓
BLUE VISIBILITY
     ↓
DETECTION
     ↓
INVESTIGATION
     ↓
GAP
     ↓
FIX
     ↓
RETEST
     ↓
IMPROVED DEFENSE
```

---

# 122. Chapter Summary

This chapter covered:

```text
Detection Testing
Detection Validation
Detection Hypotheses
Test Objectives
Unit Testing
Integration Testing
End-to-End Testing
Atomic Testing
Adversary Simulation
Purple Teaming
Threat Scenarios
Test Scope
Success Criteria
Detection Coverage
Telemetry Gaps
Detection Gaps
Correlation Gaps
Context Gaps
Performance Gaps
Response Gaps
Regression Testing
Boundary Testing
Time-Window Testing
Null Testing
Duplicate Event Testing
Delayed Event Testing
Out-of-Order Testing
Missing Event Testing
Replay
Historical Incident Replay
Backtesting
Detection Latency
MTTD
Precision
Recall
False Positive Testing
False Negative Testing
Detection Evasion Testing
Detection Robustness
Purple Team Evidence
Validation Reports
Detection Test Automation
CI/CD Testing
Production Validation
Canary Validation
Alert Storm Testing
Exception Testing
ATT&CK Coverage Validation
Test Coverage
Test Quality
Repeatability
Safety
Cleanup
Detection-Test Mapping
Purple Team Metrics
Detection Gap Aging
```

The central principle is:

> **Detection testing turns assumptions into evidence. Purple teaming turns that evidence into continuous defensive improvement.**

A mature security team should be able to demonstrate:

```text
THIS IS THE THREAT
        ↓
THIS IS THE BEHAVIOR
        ↓
THIS IS THE TELEMETRY
        ↓
THIS IS THE DETECTION
        ↓
THIS IS THE TEST
        ↓
THIS IS THE ALERT
        ↓
THIS IS THE INVESTIGATION
        ↓
THIS IS THE RESPONSE
        ↓
THIS IS THE GAP
        ↓
THIS IS THE FIX
        ↓
THIS IS THE RETEST
```

That is the foundation of a **measurable, threat-informed, continuously validated detection engineering program**.