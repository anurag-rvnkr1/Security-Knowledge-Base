# Chapter 14 – Detection Operations, Coverage & Lifecycle Management

> Detection engineering becomes a mature capability only when detections are operated as a continuous security program. This requires ownership, coverage measurement, health monitoring, deployment governance, documentation, maintenance, and deliberate retirement. A detection that exists but is not monitored, tested, maintained, or reviewed should not be considered a healthy production capability.

---

# 1. Introduction

Creating a detection is only one part of the lifecycle.

The complete operational model is:

```text
Threat Intelligence
       ↓
Detection Design
       ↓
Development
       ↓
Testing
       ↓
Deployment
       ↓
Production Operation
       ↓
Monitoring
       ↓
Tuning
       ↓
Coverage Review
       ↓
Lifecycle Review
       ↓
Retirement
```

The objective is to ensure that detections remain:

```text
Relevant
Available
Accurate
Performant
Tested
Owned
Actionable
```

---

# 2. Detection Operations

Detection operations include:

```text
Deployment
Monitoring
Alert Management
Health Checks
Tuning
Incident Feedback
Coverage Management
Change Management
Documentation
Retirement
```

---

# 3. Detection Ownership

Every production detection should have an owner.

Possible ownership:

```text
Detection Engineer
SOC Team
Threat Detection Team
Cloud Security Team
Identity Security Team
Application Security Team
```

---

# 4. Why Ownership Matters

Without ownership:

```text
Detection Breaks
      ↓
Nobody Notices
      ↓
No Fix
      ↓
Coverage Degrades
```

Ownership creates:

```text
Accountability
Maintenance
Review
Escalation
```

---

# 5. Detection Owner Responsibilities

The owner should typically manage:

```text
Logic
Testing
Performance
Tuning
Documentation
Coverage
Dependencies
Review
Retirement
```

---

# 6. Detection Metadata

A production detection should maintain:

```yaml
id:
name:
description:
owner:
team:
status:
severity:
confidence:
version:
created:
updated:
review_date:
data_sources:
dependencies:
techniques:
```

---

# 7. Detection Status

Useful states:

```text
Draft
Development
Testing
Staging
Production
Degraded
Deprecated
Retired
```

---

# 8. Production Detection

A production detection should have:

```text
Approved Logic
Valid Tests
Owner
Required Telemetry
Documentation
Monitoring
Rollback Strategy
```

---

# 9. Detection Health

A detection can be:

```text
Healthy
Degraded
No Data
Failing
Disabled
Retired
```

---

# 10. Detection Health Signals

Monitor:

```text
Execution Success
Input Events
Query Errors
Latency
Alert Volume
Data Availability
Dependencies
```

---

# 11. Detection Heartbeat

For critical detection infrastructure, establish a mechanism to determine:

```text
Is the detection executing?
```

Possible signals:

```text
Successful Query Execution
Execution Metrics
Scheduled Job Completion
Pipeline Health
```

---

# 12. No-Data Condition

A detection producing:

```text
0 alerts
```

does not necessarily mean:

```text
No Threats
```

It could mean:

```text
No Telemetry
Query Failure
Parser Failure
Data Pipeline Failure
Rule Disabled
Environment Changed
```

---

# 13. Alert Volume Monitoring

Track:

```text
Alerts / Hour
Alerts / Day
Alerts / User
Alerts / Host
Alerts / Detection
```

---

# 14. Alert Spike

Example:

```text
100 alerts/day
      ↓
50,000 alerts/day
```

Possible causes:

```text
Attack
False Positive
Parser Change
Configuration Change
Rule Bug
```

---

# 15. Alert Drop

Example:

```text
100 alerts/day
      ↓
0 alerts/day
```

Potential:

```text
Telemetry Failure
Detection Failure
Environment Change
Rule Disabled
```

---

# 16. Detection Latency Monitoring

Track:

```text
Event Time
Ingestion Time
Detection Time
Alert Time
```

---

# 17. Detection Availability

Critical detections should have measurable:

```text
Uptime
Execution Success
Data Availability
```

---

# 18. Detection SLO

A detection SLO may define:

```text
Execution Success ≥ Target
Detection Latency ≤ Target
Data Availability ≥ Target
```

Exact targets should depend on detection criticality.

---

# 19. Detection SLA vs SLO

### SLA

A formal commitment between parties.

### SLO

An operational reliability objective.

Example:

```text
Critical Detection:
99.9% successful execution
```

---

# 20. Detection Error Monitoring

Monitor:

```text
Syntax Error
Query Error
Timeout
Data Error
Permission Error
Dependency Failure
Deployment Error
```

---

# 21. Detection Failure Workflow

```text
Failure
 ↓
Detect
 ↓
Classify
 ↓
Notify Owner
 ↓
Investigate
 ↓
Fix
 ↓
Validate
 ↓
Restore
 ↓
Document
```

---

# 22. Detection Incident

A detection failure can itself become a security incident when:

```text
Critical Visibility
is Lost
```

Example:

```text
Identity Telemetry
      ↓
Unavailable
      ↓
Account-Takeover Detection
      ↓
Blind
```

---

# 23. Detection Dependency Monitoring

Dependencies may include:

```text
Log Source
Parser
Schema
Lookup
Threat Feed
Enrichment
API
Reference Data
```

---

# 24. Dependency Failure

Example:

```text
Detection
 ↓
Requires field:
user.name
 ↓
Parser changes field
 ↓
user.name missing
 ↓
Detection fails
```

---

# 25. Schema Monitoring

Track:

```text
Field Names
Field Types
Field Availability
Event Types
Data Volume
```

---

# 26. Data Availability

Monitor:

```text
Expected Events
Actual Events
```

Example:

```text
Expected:
1M endpoint events/hour

Observed:
100K/hour
```

Potential telemetry degradation.

---

# 27. Detection Coverage

Detection coverage measures how well the detection program addresses:

```text
Threats
Techniques
Assets
Data Sources
Attack Paths
```

---

# 28. Coverage Dimensions

Coverage can be measured across:

```text
ATT&CK Techniques
Threat Actors
Attack Stages
Assets
Data Sources
Business Services
Cloud Accounts
Endpoints
Applications
```

---

# 29. ATT&CK Coverage

Map detections to:

```text
Tactic
Technique
Sub-Technique
```

Then identify:

```text
Covered
Partially Covered
Not Covered
```

---

# 30. Technique Coverage

Example:

```text
Technique:
Credential Dumping

Telemetry:
Yes

Detection:
Yes

Testing:
Yes

Coverage:
Strong
```

---

# 31. Partial Coverage

Example:

```text
Technique:
Lateral Movement

Detection:
Only one protocol covered
```

Result:

```text
Partial Coverage
```

---

# 32. Coverage ≠ Detection Count

Example:

```text
500 detections
```

does not automatically mean:

```text
High Coverage
```

Five hundred overlapping detections may cover fewer meaningful behaviors than a smaller, well-designed program.

---

# 33. Coverage Quality

A mature coverage model considers:

```text
Telemetry
Detection
Testing
Context
Response
```

---

# 34. Coverage Confidence

Example model:

```text
Telemetry Only
→ Low

Detection Exists
→ Medium

Detection Tested
→ High

Detection + Purple Team
→ Very High
```

The organization should define its own formal confidence levels.

---

# 35. Coverage Matrix

| Technique | Telemetry | Detection | Tested | Response | Coverage |
|---|---|---|---|---|---|
| T1 | Yes | Yes | Yes | Yes | Strong |
| T2 | Yes | Yes | No | Yes | Partial |
| T3 | Yes | No | — | — | Gap |
| T4 | No | No | — | — | Visibility Gap |

---

# 36. Coverage Heatmap

A heatmap can represent:

```text
Strong
Moderate
Weak
Missing
```

across:

```text
Tactics
Techniques
Assets
```

---

# 37. Threat-Informed Coverage

Coverage should prioritize:

```text
Relevant Threats
Relevant Techniques
Relevant Assets
Relevant Attack Paths
```

rather than attempting to detect everything equally.

---

# 38. Crown-Jewel Coverage

Identify:

```text
Critical Assets
Critical Applications
Sensitive Data
Identity Infrastructure
Production Systems
```

Then prioritize detections around them.

---

# 39. Attack Path Coverage

Consider:

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

A mature program should understand detection coverage across the attack path.

---

# 40. Detection Coverage Gaps

Common gaps:

```text
No Telemetry
No Detection
No Correlation
No Context
No Testing
No Response
```

---

# 41. Telemetry Gap

```text
Technique
 ↓
No Required Data
```

Solution:

```text
Collect / Improve Telemetry
```

---

# 42. Detection Gap

```text
Telemetry
 ↓
No Detection
```

Solution:

```text
Build Detection
```

---

# 43. Correlation Gap

```text
Events Exist
 ↓
No Attack Chain Detection
```

Solution:

```text
Correlation / Sequence Detection
```

---

# 44. Context Gap

```text
Alert
 ↓
Insufficient Information
```

Solution:

```text
Enrichment
Entity Resolution
Context
```

---

# 45. Response Gap

```text
Detection
 ↓
No Response Workflow
```

Solution:

```text
Playbook
Ownership
Escalation
```

---

# 46. Detection Inventory

Maintain a central inventory:

```text
Detection ID
Name
Owner
Status
Severity
ATT&CK
Data Sources
Version
Last Updated
Last Tested
Last Reviewed
```

---

# 47. Detection Catalog

A detection catalog helps teams answer:

```text
What detections exist?
Who owns them?
What threats do they cover?
Which are healthy?
Which need review?
```

---

# 48. Detection Search

Useful searchable metadata:

```text
Detection ID
Technique
Tactic
Owner
Data Source
Severity
Status
Platform
Application
Cloud
```

---

# 49. Detection Lifecycle

A mature lifecycle:

```text
Idea
 ↓
Design
 ↓
Development
 ↓
Testing
 ↓
Staging
 ↓
Production
 ↓
Monitoring
 ↓
Tuning
 ↓
Review
 ↓
Deprecation
 ↓
Retirement
```

---

# 50. Detection Review

Every detection should be periodically reviewed.

Review:

```text
Threat Relevance
Performance
False Positives
False Negatives
Coverage
Telemetry
Dependencies
Ownership
```

---

# 51. Review Frequency

Possible model:

```text
Critical:
Monthly

High:
Quarterly

Medium:
Semi-Annual

Low:
Annual
```

Exact cadence should depend on risk and operational requirements.

---

# 52. Stale Detection

A detection may become stale when:

```text
Threat Changes
Environment Changes
Telemetry Changes
Application Changes
Cloud Architecture Changes
```

---

# 53. Detection Freshness

Track:

```text
Last Modified
Last Tested
Last Reviewed
Last Triggered
```

---

# 54. Last Triggered Is Not Health

A detection that triggered recently may still be:

```text
Incorrect
Noisy
Incomplete
```

Therefore monitor more than alert frequency.

---

# 55. Detection Effectiveness

Evaluate:

```text
Precision
Recall
Coverage
Latency
Performance
Analyst Feedback
Incident Detection
```

---

# 56. Detection Retirement

Not every detection should live forever.

Retire when:

```text
Threat No Longer Relevant
Data Source Removed
Duplicate Detection
Better Detection Exists
Application Retired
Platform Migrated
Persistent Poor Value
```

---

# 57. Deprecation

Before retirement:

```text
Mark Deprecated
Notify Stakeholders
Validate Replacement
Monitor Usage
Plan Removal
```

---

# 58. Retirement Workflow

```text
Identify Candidate
       ↓
Impact Assessment
       ↓
Owner Review
       ↓
Replacement Check
       ↓
Deprecation
       ↓
Monitoring
       ↓
Disable
       ↓
Validate
       ↓
Archive
```

---

# 59. Safe Retirement

Before disabling:

```text
Check Active Incidents
Check Coverage
Check Dependencies
Check Replacement
Check Compliance
```

---

# 60. Detection Replacement

Example:

```text
Old Rule
   ↓
Deprecated

New Behavioral Rule
   ↓
Validated

Old Rule
   ↓
Retired
```

---

# 61. Duplicate Detection

Two detections may identify:

```text
Same Behavior
```

This creates:

```text
Duplicate Alerts
Maintenance Cost
Conflicting Severity
```

---

# 62. Detection Consolidation

Combine related detections when appropriate:

```text
Detection A
+
Detection B
+
Detection C
```

into:

```text
Correlated Detection
```

But avoid creating overly complex rules.

---

# 63. Detection Debt

Detection debt is accumulated technical and operational debt such as:

```text
Untested Rules
Unowned Rules
Stale Rules
Duplicate Rules
Broken Dependencies
Undocumented Exceptions
Poor Queries
```

---

# 64. Detection Debt Management

Track:

```text
Debt Item
Owner
Priority
Age
Impact
Remediation
```

---

# 65. Detection Backlog

Typical backlog items:

```text
New Detection
Detection Gap
False Positive Tuning
Performance Optimization
Telemetry Improvement
Coverage Expansion
Retirement
Testing
Documentation
```

---

# 66. Detection Prioritization

Prioritize based on:

```text
Threat Severity
Asset Criticality
Exposure
Likelihood
Coverage Gap
Detection Value
Operational Cost
```

---

# 67. Risk-Based Prioritization

Example:

```text
Critical Asset
+
High Threat Relevance
+
No Detection
=
High Priority
```

---

# 68. Detection Change Management

Production changes should be:

```text
Tracked
Reviewed
Tested
Approved
Deployable
Reversible
```

---

# 69. Emergency Detection Changes

During active incidents:

```text
Threat Identified
 ↓
Rapid Detection
 ↓
Emergency Deployment
```

Afterwards:

```text
Document
Test
Review
Harden
```

---

# 70. Detection Release Management

A release may contain:

```text
New Detections
Updated Detections
Retired Detections
Schema Changes
Performance Improvements
```

---

# 71. Release Notes

Example:

```text
Release:
2026.08

Added:
Cloud IAM privilege detection

Updated:
PowerShell behavior detection

Tuned:
VPN login detection

Retired:
Legacy scanner rule
```

---

# 72. Detection Deployment Validation

After deployment:

```text
Rule Enabled
 ↓
Data Available
 ↓
Query Executes
 ↓
Test Event
 ↓
Expected Alert
 ↓
Analyst Context
```

---

# 73. Production Smoke Test

A smoke test verifies:

```text
Basic Functionality
```

after deployment.

Example:

```text
Synthetic Event
→ Expected Alert
```

---

# 74. Rollback

Every critical change should have:

```text
Previous Version
Rollback Method
Owner
Validation
```

---

# 75. Detection Change Audit

Track:

```text
Who
What
When
Why
Approval
Version
Deployment
Result
```

---

# 76. Detection Documentation

Documentation should remain synchronized with:

```text
Logic
Metadata
Tests
Dependencies
Coverage
Operations
```

---

# 77. Runbooks

A detection runbook should tell analysts:

```text
What does this alert mean?
What should I check?
What context matters?
What is expected?
What is suspicious?
Who should be contacted?
```

---

# 78. Detection Runbook Example

```text
Alert:
Suspicious Cloud Privilege Change

Check:
1. User
2. Role
3. Previous Role
4. Source IP
5. MFA
6. Change Ticket
7. Resource
8. Follow-up Activity

Escalate if:
Unauthorized change
+
Sensitive resource
```

---

# 79. Detection-to-Playbook Mapping

Example:

```text
Detection
   ↓
Playbook
   ↓
Investigation
   ↓
Containment
```

---

# 80. Detection Coverage vs Response Coverage

A team may have:

```text
Detection = Yes
Response = No
```

This should not be considered complete operational coverage.

---

# 81. Operational Coverage Model

```text
Telemetry
   ↓
Detection
   ↓
Context
   ↓
Alert
   ↓
Investigation
   ↓
Response
```

Strong coverage considers all stages.

---

# 82. Detection Service Ownership

Large programs may use:

```text
Detection Engineering
SOC
Threat Intelligence
Cloud Security
Platform Engineering
Incident Response
```

---

# 83. RACI Model

Example:

```text
Detection Engineer:
Responsible

Security Lead:
Accountable

SOC:
Consulted

Incident Response:
Consulted

Platform:
Informed
```

Exact responsibility should be organization-specific.

---

# 84. Detection Operations Dashboard

Useful metrics:

```text
Total Detections
Production Detections
Healthy Detections
Failing Detections
Untested Detections
Stale Detections
Unowned Detections
Coverage
Alert Volume
False Positive Rate
Latency
Performance
```

---

# 85. Detection Coverage Dashboard

Track:

```text
ATT&CK Coverage
Threat Coverage
Asset Coverage
Cloud Coverage
Identity Coverage
Endpoint Coverage
Application Coverage
```

---

# 86. Detection Health Dashboard

Track:

```text
Execution Success
No Data
Query Errors
Latency
Alert Spikes
Alert Drops
Dependency Failures
```

---

# 87. Detection Lifecycle Dashboard

Track:

```text
New
Testing
Production
Deprecated
Retirement
```

---

# 88. Detection KPI

Possible KPIs:

```text
Detection Coverage
Detection Success Rate
Mean Detection Latency
False Positive Rate
Detection Test Coverage
Stale Detection Rate
Unowned Detection Rate
Detection Gap Age
```

---

# 89. KPI Warning

Metrics can be gamed.

Example:

```text
Goal:
Reduce alert volume
```

Bad outcome:

```text
Disable detections
```

Therefore measure multiple dimensions.

---

# 90. Balanced Detection Scorecard

Track:

```text
Coverage
Accuracy
Latency
Performance
Reliability
Testing
Response
```

---

# 91. Detection Maturity

### Level 1

Manual rules.

### Level 2

Central detection inventory.

### Level 3

Ownership and lifecycle.

### Level 4

Automated testing and deployment.

### Level 5

Coverage and health monitoring.

### Level 6

Threat-informed optimization.

### Level 7

Continuous adaptive detection operations.

---

# 92. Detection Operations Automation

Automate:

```text
Health Checks
Schema Checks
Coverage Reports
Test Execution
Deployment
Alert Metrics
Stale Detection Reports
Dependency Monitoring
```

---

# 93. Automated Stale Detection Report

Example:

```text
Detection:
DET-001

Last Review:
400 days ago

Last Test:
300 days ago

Status:
Needs Review
```

---

# 94. Automated Ownership Check

Identify:

```text
Production Detection
+
No Owner
```

and create:

```text
Ownership Gap
```

---

# 95. Automated Coverage Check

Example:

```text
Technique:
TXXXX

Telemetry:
Yes

Detection:
No

Result:
Coverage Gap
```

---

# 96. Automated Dependency Check

Example:

```text
Detection:
DET-001

Dependency:
Threat Feed A

Status:
Feed unavailable

Result:
Detection Degraded
```

---

# 97. Detection Lifecycle Automation

Conceptually:

```text
Create
 ↓
Validate
 ↓
Test
 ↓
Deploy
 ↓
Monitor
 ↓
Review
 ↓
Deprecate
 ↓
Retire
```

---

# 98. Detection Program Governance

Governance defines:

```text
Standards
Ownership
Review
Change Management
Risk
Compliance
Metrics
```

---

# 99. Detection Standards

Standardize:

```text
Naming
Metadata
Severity
Confidence
Testing
ATT&CK
Documentation
Exceptions
Deployment
```

---

# 100. Detection Quality Gates

Before production:

```text
Owner
+
Tests
+
Review
+
Documentation
+
Performance
+
Coverage
```

---

# 101. Production Readiness Checklist

```text
[ ] Unique ID
[ ] Owner
[ ] Description
[ ] Threat hypothesis
[ ] ATT&CK mapping
[ ] Required telemetry
[ ] Query validated
[ ] Positive tests
[ ] Negative tests
[ ] Regression tests
[ ] Performance tested
[ ] False positives documented
[ ] Exceptions documented
[ ] Severity assigned
[ ] Confidence assigned
[ ] Runbook available
[ ] Rollback available
[ ] Monitoring enabled
```

---

# 102. Detection Lifecycle Checklist

```text
[ ] Detection created
[ ] Metadata complete
[ ] Owner assigned
[ ] Tests created
[ ] Review completed
[ ] Production deployed
[ ] Health monitored
[ ] Alerts analyzed
[ ] Tuning performed
[ ] Coverage reviewed
[ ] Periodic review completed
[ ] Dependencies validated
[ ] Documentation updated
[ ] Deprecation considered
[ ] Retirement completed when appropriate
```

---

# 103. Interview Questions

### What is detection operations?

> The ongoing management of production detections, including deployment, monitoring, health checks, tuning, ownership, coverage, incident feedback, and lifecycle management.

### Why does every detection need an owner?

> Ownership ensures someone is accountable for maintaining, testing, tuning, reviewing, and retiring the detection.

### What is detection health?

> The operational state of a detection, including whether it executes successfully, receives telemetry, maintains expected performance, and produces expected outputs.

### Why is zero alert volume not necessarily good?

> Zero alerts may indicate no malicious activity, but it may also indicate missing telemetry, query failure, schema changes, or a disabled detection.

### What is detection coverage?

> The degree to which relevant threats, techniques, assets, and attack paths are supported by telemetry, detections, testing, and response capability.

### Why isn't detection count a good coverage metric?

> Many detections can overlap the same behavior while leaving important techniques or attack paths uncovered.

### What is a telemetry gap?

> A missing data source or field that prevents effective detection of relevant behavior.

### What is detection debt?

> Accumulated maintenance problems such as stale, untested, duplicate, undocumented, or unowned detections.

### When should a detection be retired?

> When its threat is no longer relevant, its data source is gone, a better replacement exists, it duplicates another detection, or its operational value is consistently poor.

### What should be checked before retiring a detection?

> Active incidents, coverage impact, dependencies, replacement detections, compliance requirements, and stakeholder ownership.

### What is a detection runbook?

> Operational guidance explaining what an alert means, what analysts should investigate, what context matters, and when to escalate.

### How do you measure detection program maturity?

> Evaluate coverage, reliability, testing, ownership, lifecycle management, performance, false positives, latency, response integration, and continuous improvement.

---

# 104. Quick Revision

```text
Detection Operations
→ Running and maintaining production detections

Detection Owner
→ Person/team accountable for detection lifecycle

Detection Health
→ Operational condition of detection

Detection SLO
→ Reliability/performance objective

Detection Coverage
→ Threat/technique/asset coverage

Coverage Gap
→ Missing security capability

Telemetry Gap
→ Missing required visibility

Detection Gap
→ Telemetry exists but detection does not

Correlation Gap
→ Related events are not combined

Context Gap
→ Alert lacks useful investigation information

Response Gap
→ Detection exists but response capability is missing

Detection Inventory
→ Central catalog of detections

Detection Lifecycle
→ Create → Test → Deploy → Operate → Review → Retire

Detection Debt
→ Accumulated maintenance and quality problems

Stale Detection
→ Detection requiring review or update

Deprecation
→ Marking detection for eventual removal

Retirement
→ Removing detection from active operation

Coverage Matrix
→ Structured view of security coverage

Runbook
→ Analyst investigation guidance

Smoke Test
→ Basic post-deployment functionality test

Release Management
→ Controlled detection deployment process

RACI
→ Responsibility and accountability model

Detection KPI
→ Metric used to measure program performance
```

---

# 105. Golden Rules

```text
1. Every production detection needs an owner.

2. Every critical detection needs health monitoring.

3. Zero alerts does not automatically mean success.

4. Monitor both alert spikes and alert drops.

5. Monitor detection execution failures.

6. Monitor telemetry availability.

7. Monitor schema changes.

8. Monitor dependencies.

9. Maintain a central detection inventory.

10. Give every detection a stable ID.

11. Track detection status.

12. Track last review date.

13. Track last test date.

14. Track detection version.

15. Measure coverage by threat and technique.

16. Do not measure coverage by detection count alone.

17. Prioritize crown-jewel assets.

18. Prioritize relevant threats.

19. Track telemetry gaps separately from detection gaps.

20. Track correlation gaps separately from detection gaps.

21. Track response gaps separately from detection gaps.

22. Maintain detection runbooks.

23. Connect detections to response workflows.

24. Review production detections periodically.

25. Watch for stale detections.

26. Manage detection debt.

27. Remove duplicate detections where appropriate.

28. Deprecate before retiring important detections.

29. Check coverage before retirement.

30. Validate replacements before disabling old detections.

31. Maintain rollback capability.

32. Record production changes.

33. Monitor detection latency.

34. Monitor detection performance.

35. Monitor false positives.

36. Monitor detection effectiveness.

37. Automate health checks where possible.

38. Automate coverage reporting where possible.

39. Automate stale-rule reporting where possible.

40. Treat detection failures as operational security failures.

41. Detection coverage should include telemetry, detection, testing, context, and response.

42. Detection lifecycle management is continuous.

43. A detection should earn its place in production through measurable security value.

44. A detection should be retired when its value no longer justifies its cost or risk.

45. Mature detection engineering is a managed security service, not a collection of static rules.
```

---

# 106. Final Mental Model

Think of the detection program as a continuously operated service:

```text
                    DETECTION PROGRAM
                           │
          ┌────────────────┼────────────────┐
          ↓                ↓                ↓
      COVERAGE           HEALTH          LIFECYCLE
          │                │                │
      Threats           Execution         Create
      Techniques        Telemetry         Test
      Assets             Latency          Deploy
      Attack Paths       Errors           Operate
          │                │                │
          └────────────────┼────────────────┘
                           ↓
                       QUALITY
                           ↓
                      SOC ACTION
```

A mature production detection follows:

```text
CREATE
  ↓
TEST
  ↓
APPROVE
  ↓
DEPLOY
  ↓
MONITOR
  ↓
TUNE
  ↓
REVIEW
  ↓
REASSESS
  ↓
DEPRECATE
  ↓
RETIRE
```

---

# 107. Detection Coverage Mental Model

Instead of asking:

```text
How many detections do we have?
```

ask:

```text
What threats matter?
        ↓
What techniques can they use?
        ↓
What telemetry exposes them?
        ↓
What detections identify them?
        ↓
Have those detections been tested?
        ↓
Can analysts investigate them?
        ↓
Can responders act?
```

That is meaningful detection coverage.

---

# 108. Detection Health Mental Model

A healthy detection should satisfy:

```text
DATA AVAILABLE
      +
QUERY WORKS
      +
DETECTION MATCHES
      +
ALERT GENERATED
      +
CONTEXT AVAILABLE
      +
PERFORMANCE ACCEPTABLE
      +
OWNER EXISTS
      +
TESTS PASS
```

If any critical component fails:

```text
Detection Capability
       ↓
Potentially Degraded
```

---

# 109. Detection Lifecycle Mental Model

```text
THREAT
  ↓
HYPOTHESIS
  ↓
DETECTION
  ↓
TEST
  ↓
DEPLOY
  ↓
OPERATE
  ↓
MEASURE
  ↓
TUNE
  ↓
REVIEW
  ↓
IMPROVE
  ↓
RETIRE
```

The most important point is:

> **Production deployment is not the end of detection engineering. It is the beginning of the operational lifecycle.**

---

# 110. Chapter Summary

This chapter covered:

```text
Detection Operations
Detection Ownership
Detection Metadata
Detection Status
Production Readiness
Detection Health
Detection Heartbeats
No-Data Conditions
Alert Monitoring
Alert Spikes
Alert Drops
Detection Latency
Detection Availability
Detection SLOs
Detection Errors
Detection Failures
Detection Dependencies
Schema Monitoring
Data Availability
Detection Coverage
ATT&CK Coverage
Technique Coverage
Partial Coverage
Coverage Confidence
Coverage Matrices
Threat-Informed Coverage
Crown-Jewel Coverage
Attack Path Coverage
Telemetry Gaps
Detection Gaps
Correlation Gaps
Context Gaps
Response Gaps
Detection Inventory
Detection Catalog
Detection Lifecycle
Detection Review
Stale Detections
Detection Freshness
Detection Effectiveness
Detection Retirement
Deprecation
Replacement
Duplicate Detection
Detection Consolidation
Detection Debt
Detection Backlog
Risk-Based Prioritization
Change Management
Emergency Changes
Release Management
Smoke Testing
Rollback
Audit Trails
Runbooks
Detection-to-Playbook Mapping
Operational Coverage
RACI
Detection Dashboards
Detection KPIs
Detection Maturity
Automation
Governance
Quality Gates
Production Readiness
Lifecycle Checklists
```

The central principle is:

> **A detection is a continuously operated security capability. It needs ownership, telemetry, testing, monitoring, tuning, coverage measurement, operational context, and lifecycle governance throughout its entire existence.**

The mature model is:

```text
THREAT
  ↓
DETECTION
  ↓
TEST
  ↓
DEPLOY
  ↓
OPERATE
  ↓
MONITOR
  ↓
MEASURE
  ↓
TUNE
  ↓
REVIEW
  ↓
RETIRE
```

And meaningful coverage is:

```text
TELEMETRY
    +
DETECTION
    +
TESTING
    +
CONTEXT
    +
RESPONSE
        ↓
OPERATIONAL DETECTION COVERAGE
```

The ultimate goal is not to maximize the number of detection rules.

The goal is to maintain a **reliable, measurable, threat-informed, operationally useful detection capability that continues to protect the environment as threats and infrastructure evolve.**

---