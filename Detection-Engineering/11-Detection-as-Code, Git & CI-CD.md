# Chapter 11 – Detection-as-Code, Git & CI/CD

> Detection-as-Code applies software engineering principles to security detections. Instead of treating SIEM and detection rules as manually managed configuration, detections become version-controlled, testable, reviewable, deployable, and measurable code-like artifacts.

---

# 1. Introduction

Traditional detection management often looks like:

```text
Analyst
   ↓
Create Rule in SIEM
   ↓
Save
   ↓
Enable
```

This creates problems:

```text
No Version History
No Consistent Review
Limited Testing
Manual Deployment
Difficult Rollback
Poor Auditability
```

Detection-as-Code changes this into:

```text
Detection Source
      ↓
Git
      ↓
Code Review
      ↓
Validation
      ↓
Testing
      ↓
CI/CD
      ↓
Deployment
      ↓
Monitoring
```

---

# 2. What Is Detection-as-Code?

Detection-as-Code means managing detections using software engineering practices such as:

```text
Version Control
Code Review
Testing
Automation
CI/CD
Documentation
Change Management
Rollback
Monitoring
```

The goal is:

```text
Reliable Detection Engineering
```

rather than simply:

```text
Rule Creation
```

---

# 3. Why Detection-as-Code Matters

Benefits include:

```text
Reproducibility
Consistency
Auditability
Collaboration
Testing
Automation
Rollback
Versioning
Scalability
Quality Control
```

---

# 4. Detection Lifecycle

A typical lifecycle:

```text
Idea
 ↓
Design
 ↓
Development
 ↓
Review
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
Retirement
```

---

# 5. Detection Artifact

A detection should be represented as a structured artifact containing information such as:

```text
ID
Name
Description
Query
Logic
Severity
Confidence
Tactics
Techniques
Data Sources
Tests
Owner
Status
Version
Exceptions
```

---

# 6. Example Detection Structure

```yaml
id: DET-001

name: Suspicious PowerShell Execution

description: >
  Detects suspicious PowerShell behavior
  based on execution context and command patterns.

severity: high

confidence: medium

status: development

platform:
  - windows

data_sources:
  - endpoint

techniques:
  - T1059

query: |
  ...

tests:
  - positive_case
  - negative_case
```

The exact schema should be standardized for the organization.

---

# 7. Detection Repository

A repository may look like:

```text
detections/
├── endpoint/
├── identity/
├── network/
├── cloud/
├── application/
├── container/
├── tests/
├── schemas/
└── documentation/
```

---

# 8. Organizing by Domain

Possible structure:

```text
detections/
├── endpoint/
├── network/
├── identity/
├── cloud/
├── application/
└── container/
```

This improves discoverability.

---

# 9. Organizing by Threat

Another approach:

```text
detections/
├── account-takeover/
├── lateral-movement/
├── persistence/
├── credential-access/
├── ransomware/
└── exfiltration/
```

The best structure depends on team workflows.

---

# 10. Hybrid Repository

A mature repository can combine:

```text
Domain
+
Threat
+
ATT&CK
```

Example:

```text
detections/
└── identity/
    └── account-takeover/
        └── suspicious-login.yml
```

---

# 11. Naming Conventions

Use predictable names.

Example:

```text
suspicious_powershell.yml
privileged_login_anomaly.yml
cloud_access_key_creation.yml
kubernetes_secret_access.yml
```

Avoid:

```text
final_rule.yml
new_rule2.yml
test_latest.yml
```

---

# 12. Detection IDs

Every detection should have a unique ID.

Example:

```text
DET-ENDPOINT-001
DET-IDENTITY-002
DET-CLOUD-003
```

IDs should remain stable even when names change.

---

# 13. Why Stable IDs Matter

Stable IDs support:

```text
Tracking
Metrics
Deployment
Testing
References
Incidents
Documentation
```

---

# 14. Git

Git provides:

```text
Version Control
Branching
History
Diffs
Merging
Revert
Collaboration
```

Detection engineers should use Git similarly to software engineers.

---

# 15. Git Repository Benefits

With Git, you can answer:

```text
Who changed this detection?
When?
What changed?
Why?
Who reviewed it?
What version was deployed?
```

---

# 16. Commit History

Example:

```text
Initial detection
 ↓
Add false-positive exception
 ↓
Improve command-line logic
 ↓
Add test cases
 ↓
Tune threshold
```

This provides an audit trail.

---

# 17. Good Commit Message

```text
Improve suspicious PowerShell detection
```

Better:

```text
Tune PowerShell detection for approved admin hosts
```

Avoid:

```text
changes
fix
update
test
```

---

# 18. Branching

A typical workflow:

```text
main
 │
 └── feature/detection-001
```

The engineer works on the feature branch.

Then:

```text
Feature Branch
      ↓
Pull Request
      ↓
Review
      ↓
Tests
      ↓
Merge
```

---

# 19. Pull Requests

A detection PR should explain:

```text
What changed?
Why?
What threat does it address?
What ATT&CK technique?
What telemetry?
What tests?
What false positives?
What deployment impact?
```

---

# 20. Detection PR Example

```text
Title:
Add suspicious cloud privilege escalation detection

Threat:
Cloud account compromise

Technique:
Privilege Escalation

Telemetry:
Cloud audit logs

Testing:
Positive + Negative

Expected Impact:
New alerts for unexpected IAM changes
```

---

# 21. Code Review

Reviewers should evaluate:

```text
Correctness
Detection Logic
Threat Relevance
False Positives
False Negatives
Performance
Testing
Documentation
ATT&CK Mapping
Security
```

---

# 22. Detection Review Checklist

```text
[ ] Logic correct
[ ] Threat hypothesis clear
[ ] Query efficient
[ ] Required fields exist
[ ] Tests included
[ ] False positives considered
[ ] ATT&CK mapping correct
[ ] Severity justified
[ ] Exceptions documented
[ ] Performance acceptable
```

---

# 23. Detection Schema

A schema defines required fields.

Example:

```yaml
required:
  - id
  - name
  - description
  - query
  - severity
  - status
  - tests
```

This prevents incomplete detections from entering production.

---

# 24. Schema Validation

CI can automatically validate:

```text
Missing ID
Invalid Severity
Missing Query
Invalid ATT&CK ID
Invalid YAML
Missing Owner
```

If validation fails:

```text
Pipeline Stops
```

---

# 25. YAML Validation

Example invalid:

```yaml
id DET-001
```

Correct:

```yaml
id: DET-001
```

Automated validation catches syntax errors before deployment.

---

# 26. Detection Linting

Linting can identify:

```text
Bad Naming
Missing Metadata
Unsupported Fields
Invalid Syntax
Deprecated Fields
Unsafe Patterns
```

---

# 27. Query Validation

Before deployment, verify:

```text
Query Parses
Fields Exist
Operators Supported
Functions Supported
Syntax Valid
```

---

# 28. Query Compatibility

Different platforms use different languages:

```text
KQL
SPL
Sigma
SQL
YARA-L
Lucene
EQL
Custom DSL
```

A detection repository should document the target language.

---

# 29. Sigma

Sigma is a generic detection-rule format designed to describe log-based detections in a platform-independent way.

Conceptually:

```text
Detection Logic
      ↓
Sigma
      ↓
Backend Conversion
      ↓
SIEM Query
```

This can improve portability.

---

# 30. Sigma Example

```yaml
title: Suspicious PowerShell Execution

id: example-id

status: experimental

logsource:
  product: windows

detection:
  selection:
    Image|endswith:
      - '\powershell.exe'
  condition: selection

level: high
```

Real production rules should include appropriate metadata, testing, and environment-specific conditions.

---

# 31. Platform-Specific Detections

Sometimes generic rules are insufficient.

Example:

```text
Sigma
   ↓
Generic Logic
```

may need:

```text
Platform-specific fields
Platform-specific functions
Platform-specific data model
```

---

# 32. Generic vs Native Detection

### Generic

```text
Portable
Reusable
Cross-platform
```

### Native

```text
Optimized
Platform-specific
Potentially More Powerful
```

Use the appropriate abstraction level.

---

# 33. Detection Compilation

Conceptually:

```text
Source Detection
      ↓
Parser
      ↓
Validation
      ↓
Backend Translation
      ↓
Target Query
```

This is similar to compilation.

---

# 34. Detection CI Pipeline

A typical pipeline:

```text
Commit
 ↓
Syntax Check
 ↓
Schema Validation
 ↓
Lint
 ↓
Unit Tests
 ↓
Query Validation
 ↓
Coverage Check
 ↓
Build
 ↓
Deployment
```

---

# 35. CI

Continuous Integration ensures changes are automatically validated.

For detections:

```text
Every Pull Request
        ↓
Automatic Tests
```

---

# 36. CD

Continuous Delivery/Deployment automates moving approved detections toward production.

Conceptually:

```text
Approved
 ↓
Staging
 ↓
Validation
 ↓
Production
```

---

# 37. Staging Environment

Never assume:

```text
Development
=
Production
```

A staging environment allows validation of:

```text
Query
Fields
Performance
Alert Format
Integration
```

---

# 38. Detection Deployment Stages

Example:

```text
Draft
 ↓
Development
 ↓
Testing
 ↓
Staging
 ↓
Canary
 ↓
Production
```

---

# 39. Canary Deployment

Deploy the detection to a limited scope first.

Example:

```text
5% of Hosts
```

or:

```text
One Business Unit
```

Then monitor:

```text
Alert Volume
False Positives
Performance
Latency
```

---

# 40. Production Deployment

Only deploy after:

```text
Validation
Review
Testing
Approval
```

---

# 41. Rollback

If a detection causes:

```text
Alert Storm
Performance Issues
Incorrect Alerts
Data Query Problems
```

rollback should be quick.

Git helps:

```text
Current Version
      ↓
Previous Version
```

---

# 42. Detection Versioning

Example:

```text
v1.0
Initial

v1.1
Tune false positives

v1.2
Improve logic

v2.0
Major logic redesign
```

---

# 43. Semantic Versioning

A team may use:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
2.1.3
```

Meaning should be documented internally.

---

# 44. Detection Status

Possible states:

```text
Draft
Experimental
Testing
Staging
Production
Deprecated
Retired
```

---

# 45. Detection Ownership

Every production detection should have:

```text
Owner
Team
Reviewer
Escalation Contact
```

Ownership prevents orphaned rules.

---

# 46. Detection Metadata

Recommended metadata:

```yaml
id:
name:
description:
owner:
team:
status:
severity:
confidence:
priority:
version:
created:
updated:
author:
reviewer:
```

---

# 47. Threat Metadata

Include:

```yaml
tactics:
  - Execution

techniques:
  - T1059
```

---

# 48. Data Metadata

Include:

```yaml
data_sources:
  - endpoint
  - process
  - network

required_fields:
  - user
  - host
  - process
  - command_line
```

---

# 49. Test Metadata

Example:

```yaml
tests:
  positive:
    - test_powershell_download
  negative:
    - test_admin_script
```

---

# 50. Exception Metadata

Example:

```yaml
exceptions:
  - approved_admin_hosts
  - known_automation
```

Exceptions should reference controlled configuration rather than hard-coded logic whenever practical.

---

# 51. Detection Dependencies

A detection may depend on:

```text
Field
Data Source
Parser
Lookup
Enrichment
Reference Table
Threat Intelligence
```

Document dependencies explicitly.

---

# 52. Dependency Failure

Example:

```text
Detection
   ↓
Requires field X
   ↓
Parser changed
   ↓
Field X disappears
   ↓
Detection fails
```

CI and monitoring should detect this.

---

# 53. Data Contract

A data contract defines:

```text
Field Names
Types
Semantics
Availability
Normalization
```

Example:

```text
user.id = string
source.ip = IP
event.time = timestamp
```

---

# 54. Detection Contract

A detection contract defines:

```text
Inputs
Expected Fields
Outputs
Severity
Metadata
Dependencies
```

---

# 55. Unit Testing

Unit tests validate small pieces of detection logic.

Example:

```text
Input:
Suspicious Process

Expected:
Match
```

---

# 56. Negative Unit Test

```text
Input:
Known Legitimate Process

Expected:
No Match
```

---

# 57. Regression Testing

A regression test ensures a previously fixed issue does not return.

Example:

```text
Bug:
Admin host generated false positives.

Fix:
Exception added.

Regression:
Admin host must remain suppressed.
```

---

# 58. Detection Test Dataset

A repository may contain:

```text
tests/
├── positive/
├── negative/
├── edge/
├── regression/
└── performance/
```

---

# 59. Test Data

Test events should represent:

```text
Normal
Suspicious
Malicious
Boundary
Incomplete
Duplicate
Delayed
```

---

# 60. Synthetic Events

Synthetic events are useful when real incidents cannot be shared.

Example:

```text
Synthetic Login
Synthetic Process
Synthetic Network Event
```

---

# 61. Historical Replay

Replay historical data through the detection.

This can identify:

```text
False Positives
Missed Events
Performance Issues
```

---

# 62. Backtesting

Backtesting means evaluating a detection against historical telemetry.

Conceptually:

```text
Historical Data
      ↓
Detection
      ↓
Results
```

---

# 63. Backtesting Questions

Ask:

```text
How many alerts?
How many known incidents detected?
How many false positives?
What was detection latency?
```

---

# 64. Detection Quality Gate

A CI pipeline can require:

```text
Tests Pass
AND
Schema Valid
AND
Query Valid
AND
No Critical Errors
```

before merging.

---

# 65. Risk-Based Quality Gate

More advanced:

```text
Critical Detection
+
No Test
=
Block Deployment
```

while:

```text
Low-Risk Experimental Detection
```

may follow a different workflow.

---

# 66. ATT&CK Coverage Gate

CI can verify:

```text
Every Production Detection
has valid ATT&CK mapping
```

if the organization requires it.

---

# 67. Duplicate Detection Check

CI can detect:

```text
Same Detection ID
Duplicate Name
Duplicate Logic
Near-Duplicate Rules
```

This prevents unnecessary rule duplication.

---

# 68. Dead Detection Detection

A detection may exist but never receive relevant data.

Track:

```text
No Matching Events
No Alerts
No Data
```

This may indicate:

```text
Dead Rule
Telemetry Problem
Incorrect Query
```

---

# 69. Detection Health

Monitor:

```text
Enabled
Data Available
Execution Successful
Latency Normal
Alert Volume Normal
```

---

# 70. Detection Monitoring

A production detection should itself be monitored.

Example:

```text
Detection Execution Errors
Query Latency
Event Volume
Alert Volume
```

---

# 71. Alert Volume Monitoring

Sudden increase:

```text
10 alerts/day
      ↓
10,000 alerts/hour
```

could indicate:

```text
Attack
False Positive
Parser Change
Rule Bug
```

---

# 72. Alert Volume Drop

Sudden decrease:

```text
100 alerts/day
      ↓
0 alerts/day
```

may indicate:

```text
Telemetry Failure
Query Failure
Parser Change
Detection Disabled
```

---

# 73. Detection Drift

Detection drift can occur when:

```text
Environment Changes
Telemetry Changes
Attack Techniques Change
Applications Change
Cloud Architecture Changes
```

A previously effective rule may become ineffective.

---

# 74. Schema Drift

Example:

```text
old field:
user.name

new field:
user.id
```

A detection may stop working.

Automated schema validation helps detect this.

---

# 75. Query Drift

The platform may change:

```text
Function
Field
Syntax
Data Model
```

Detection code should be validated after platform changes.

---

# 76. ATT&CK Drift

Framework changes can require:

```text
Mapping Updates
Documentation Updates
Coverage Review
```

---

# 77. Dependency Drift

External dependencies may change:

```text
Threat Feed
Lookup Table
Parser
API
Enrichment
```

Monitor these dependencies.

---

# 78. Secrets in Detection Code

Never hard-code:

```text
API Keys
Passwords
Tokens
Private Keys
```

Bad:

```yaml
api_key: abc123
```

Use:

```text
Secret Manager
Environment Variables
Secure CI Variables
```

---

# 79. Sensitive Detection Data

Detection repositories may contain:

```text
Internal Hostnames
IP Ranges
Sensitive Paths
Detection Bypass Logic
Security Architecture
```

Repositories should have appropriate access controls.

---

# 80. Branch Protection

Protect important branches:

```text
main
production
release
```

Require:

```text
Review
CI Checks
```

before merging.

---

# 81. CODEOWNERS

Use ownership rules so appropriate teams review relevant detections.

Example:

```text
/cloud/*       Cloud Security Team
/identity/*    IAM Team
/endpoint/*    Endpoint Team
```

---

# 82. Review Approvals

Critical detections may require:

```text
Detection Engineer
+
SOC Analyst
+
Security Owner
```

depending on organizational policy.

---

# 83. Change Management

Production detection changes should be traceable to:

```text
Pull Request
Commit
Ticket
Incident
Threat Intelligence
Tuning Request
```

---

# 84. Emergency Changes

Sometimes urgent changes are required.

Example:

```text
Active Attack
 ↓
Immediate Detection
```

Emergency workflows should still preserve:

```text
Audit Trail
Testing
Review
Post-Change Validation
```

---

# 85. Detection Deployment Audit Trail

Record:

```text
Detection ID
Version
Commit
Author
Reviewer
Deployment Time
Environment
Result
```

---

# 86. Rollback Strategy

A rollback plan should define:

```text
Previous Version
Rollback Command
Owner
Validation
Communication
```

---

# 87. Feature Flags

Detection behavior can be controlled through:

```text
Enabled
Disabled
Shadow Mode
Canary
Production
```

---

# 88. Shadow Mode

A detection runs but does not generate normal analyst alerts.

Useful for:

```text
Testing
Tuning
False Positive Measurement
```

---

# 89. Canary Detection

Run with limited:

```text
Hosts
Users
Accounts
Regions
```

before broad deployment.

---

# 90. Detection Deployment Strategy

Example:

```text
Development
    ↓
Test
    ↓
Shadow
    ↓
Canary
    ↓
Production
```

---

# 91. Detection-as-Code Architecture

```text
                 Git Repository
                       ↓
                Pull Request
                       ↓
                Code Review
                       ↓
                  CI Pipeline
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     Linting       Unit Tests     Schema Check
        ↓              ↓              ↓
        └──────────────┼──────────────┘
                       ↓
                 Build / Compile
                       ↓
                    Staging
                       ↓
                   Validation
                       ↓
                    Canary
                       ↓
                  Production
                       ↓
                  Monitoring
                       ↓
                    Tuning
```

---

# 92. Detection Repository Example

```text
detection-engineering/
│
├── detections/
│   ├── endpoint/
│   ├── identity/
│   ├── network/
│   ├── cloud/
│   ├── application/
│   └── container/
│
├── tests/
│   ├── positive/
│   ├── negative/
│   ├── regression/
│   └── performance/
│
├── schemas/
│
├── pipelines/
│
├── scripts/
│
├── docs/
│
└── README.md
```

---

# 93. Detection Pull Request Template

```markdown
## Detection

ID:
DET-001

Name:
Suspicious Privilege Change

## Threat

Describe the threat.

## ATT&CK

Technique:
TXXXX

## Telemetry

List required data sources.

## Logic

Explain detection behavior.

## Testing

- [ ] Positive
- [ ] Negative
- [ ] Regression
- [ ] Performance

## False Positives

List expected benign activity.

## Deployment

Target environment and expected impact.

## Rollback

Describe rollback procedure.
```

---

# 94. CI Pipeline Example

Conceptually:

```yaml
stages:
  - validate
  - lint
  - test
  - build
  - deploy
```

Then:

```text
Validate
   ↓
Lint
   ↓
Test
   ↓
Build
   ↓
Staging
```

---

# 95. Detection Validation Pipeline

```text
YAML Syntax
     ↓
Schema
     ↓
ATT&CK IDs
     ↓
Query Syntax
     ↓
Required Fields
     ↓
Unit Tests
     ↓
Regression Tests
     ↓
Performance
```

---

# 96. Query Testing

Test:

```text
Expected Match
Unexpected Match
Missing Field
Null Field
Malformed Event
Large Event
```

---

# 97. Null Handling

Detection logic should define behavior when:

```text
user = null
host = null
source.ip = null
command_line = null
```

Poor null handling can cause:

```text
False Negatives
False Positives
Query Errors
```

---

# 98. Data Type Testing

Ensure fields have expected types:

```text
timestamp → timestamp
source.ip → IP
risk.score → number
user.id → string
```

---

# 99. Time Zone Handling

Distributed systems may use:

```text
UTC
Local Time
Cloud Region Time
```

Standardize timestamps, preferably using a consistent representation such as UTC.

---

# 100. Time Window Testing

If a detection uses:

```text
10 minutes
```

test:

```text
9:59
10:00
10:01
```

to catch boundary bugs.

---

# 101. Performance Testing

Measure:

```text
Query Runtime
CPU
Memory
Events/sec
Latency
Storage
```

---

# 102. Detection Scalability

A rule working on:

```text
1 million events/day
```

may behave differently at:

```text
1 billion events/day
```

Always consider production scale.

---

# 103. Query Optimization

Common techniques:

```text
Filter Early
Select Required Fields
Avoid Unnecessary Joins
Reduce Time Windows
Use Indexed Fields
Pre-Aggregate
```

---

# 104. Regex Optimization

Avoid expensive unrestricted regex.

Prefer:

```text
Exact Match
Prefix
Suffix
Structured Fields
```

where possible.

---

# 105. Detection Dependencies in CI

Check:

```text
Parser
Schema
Reference Lists
Threat Feeds
Enrichment
Lookup Tables
```

before deployment.

---

# 106. Threat Intelligence Dependency

If a detection depends on:

```text
IOC Feed
```

monitor:

```text
Feed Freshness
Feed Availability
Indicator Quality
Expiration
```

---

# 107. Detection Package

A deployable detection package may contain:

```text
Rule
Metadata
Tests
Dependencies
Documentation
Version
```

---

# 108. Artifact Versioning

Example:

```text
detection-package-2.4.1
```

The exact artifact can be traced back to:

```text
Git Commit
```

---

# 109. Immutable Releases

Once a production package is released:

```text
Version 2.4.1
```

do not silently modify it.

Instead:

```text
2.4.2
```

for a new release.

This improves auditability.

---

# 110. Detection Rollback Example

```text
Production:
v2.4.2

Problem:
Alert Storm

Rollback:
v2.4.1

Validate:
Alert Volume Normal
```

---

# 111. Detection Monitoring Dashboard

Track:

```text
Active Detections
Failed Detections
Alert Volume
False Positive Rate
Detection Latency
Coverage
Test Status
Stale Rules
```

---

# 112. Detection SLOs

Organizations can define objectives such as:

```text
Critical detections:
99% execution success

Deployment:
< X minutes

Detection latency:
< X minutes
```

Exact targets should be environment-specific.

---

# 113. Detection Reliability

A detection should be treated like a production service.

Important properties:

```text
Availability
Correctness
Latency
Performance
Observability
Recoverability
```

---

# 114. Detection Failure

Potential causes:

```text
Parser Change
Query Error
Data Loss
Field Rename
Backend Failure
Dependency Failure
Deployment Error
```

---

# 115. Detection Observability

Monitor:

```text
Did it execute?
Did it receive data?
Did it match?
How long did it take?
Did it generate alerts?
```

---

# 116. Detection Health States

Example:

```text
HEALTHY
DEGRADED
NO DATA
ERROR
DISABLED
```

---

# 117. Automated Detection Health

Automation can flag:

```text
No Input Events
Query Errors
Sudden Alert Drop
Sudden Alert Spike
Latency Increase
```

---

# 118. Detection Lifecycle Management

A detection should eventually move through:

```text
Draft
 ↓
Experimental
 ↓
Validated
 ↓
Production
 ↓
Tuned
 ↓
Reviewed
 ↓
Deprecated
 ↓
Retired
```

---

# 119. Detection Retirement Criteria

Consider retirement when:

```text
Threat No Longer Relevant
Data Source Removed
Better Detection Exists
Persistent False Positives
Duplicate Logic
Platform Migration
```

---

# 120. Detection Documentation

Documentation should explain:

```text
Purpose
Threat
Logic
Data Sources
ATT&CK
Tests
False Positives
Exceptions
Performance
Owner
Version
```

---

# 121. Detection Engineering Maturity

### Level 1

Manual rules.

### Level 2

Version-controlled rules.

### Level 3

Automated validation.

### Level 4

Automated testing.

### Level 5

CI/CD deployment.

### Level 6

Continuous detection monitoring.

### Level 7

Fully integrated detection engineering lifecycle.

---

# 122. Common Anti-Patterns

## Anti-Pattern 1

Editing production rules manually without Git.

Problem:

```text
No Audit Trail
```

---

## Anti-Pattern 2

No Tests.

Problem:

```text
Broken Detection
```

---

## Anti-Pattern 3

No Review.

Problem:

```text
Logic Bugs
```

---

## Anti-Pattern 4

Hard-Coded Secrets.

Problem:

```text
Credential Exposure
```

---

## Anti-Pattern 5

No Rollback.

Problem:

```text
Long Recovery
```

---

## Anti-Pattern 6

No Ownership.

Problem:

```text
Detection Debt
```

---

## Anti-Pattern 7

No Monitoring.

Problem:

```text
Silent Detection Failure
```

---

## Anti-Pattern 8

Only Testing Syntax.

Problem:

```text
Valid Query
≠
Effective Detection
```

---

## Anti-Pattern 9

No Production Scale Testing.

Problem:

```text
Performance Failure
```

---

## Anti-Pattern 10

Treating Detection-as-Code as Just Git.

Problem:

```text
Git + No Testing + No CI + No Lifecycle
```

is not a mature Detection-as-Code program.

---

# 123. Practical Exercise – Build a Detection Repository

Create:

```text
detections/
├── endpoint/
├── identity/
├── network/
├── cloud/
├── tests/
└── schemas/
```

Add:

```text
1 Detection
1 Positive Test
1 Negative Test
1 Metadata File
```

---

# 124. Practical Exercise – Build CI Validation

Implement:

```text
YAML Validation
Schema Validation
Detection ID Check
Required Metadata Check
Test Execution
```

Pipeline:

```text
Commit
 ↓
Validate
 ↓
Test
 ↓
Pass/Fail
```

---

# 125. Practical Exercise – Detection PR

Create:

```text
feature/detection-001
```

Make a change.

Then:

```text
Commit
 ↓
Push
 ↓
Pull Request
 ↓
Review
 ↓
CI
 ↓
Merge
```

---

# 126. Practical Exercise – Canary Deployment

Deploy to:

```text
Small Scope
```

Measure:

```text
Alert Volume
Latency
False Positives
Performance
```

Then:

```text
Expand
```

if results are acceptable.

---

# 127. Practical Exercise – Rollback

Simulate:

```text
Bad Detection
```

Then practice:

```text
Rollback
 ↓
Validate
 ↓
Document
```

---

# 128. Detection-as-Code Checklist

```text
[ ] Git repository
[ ] Detection schema
[ ] Naming convention
[ ] Stable IDs
[ ] Metadata
[ ] ATT&CK mapping
[ ] Query validation
[ ] Linting
[ ] Unit tests
[ ] Regression tests
[ ] Negative tests
[ ] Performance tests
[ ] Pull requests
[ ] Code review
[ ] CI
[ ] Staging
[ ] Canary
[ ] Production deployment
[ ] Rollback
[ ] Ownership
[ ] Monitoring
[ ] Documentation
[ ] Versioning
[ ] Retirement process
```

---

# 129. Interview Questions

### What is Detection-as-Code?

> Managing security detections using software engineering practices such as Git, testing, code review, CI/CD, versioning, and automated deployment.

### Why use Git for detections?

> Git provides version history, collaboration, change tracking, review, rollback, and auditability.

### What should a detection pull request contain?

> The threat, detection logic, ATT&CK mapping, telemetry requirements, tests, expected false positives, and deployment impact.

### What is detection CI?

> Automated validation and testing of detection changes before they are merged or deployed.

### Why are detection tests important?

> They ensure that a detection matches intended malicious behavior and avoids known benign behavior.

### What is regression testing?

> Testing that previously fixed detection behavior remains correct after future changes.

### What is canary deployment?

> Deploying a detection to a limited scope first to observe alert volume, performance, and correctness before broader deployment.

### What is shadow mode?

> Running a detection without producing normal analyst-facing alerts so its behavior can be evaluated safely.

### Why is rollback important?

> A faulty detection can cause alert storms, performance problems, or incorrect security decisions; rollback provides a rapid recovery mechanism.

### What is schema validation?

> Checking that a detection contains valid structure, required fields, data types, and supported values.

### What is detection drift?

> The degradation of detection effectiveness caused by changes in the environment, telemetry, threat behavior, or detection dependencies.

### Why should detection rules have stable IDs?

> Stable identifiers allow rules to be tracked consistently across versions, deployments, tests, incidents, and documentation.

### Why should detection repositories avoid hard-coded secrets?

> Detection repositories may be broadly accessible and version-controlled, so embedded credentials can create serious security risks.

### What is detection observability?

> Monitoring whether detections execute correctly, receive expected telemetry, maintain normal latency, and produce expected outputs.

---

# 130. Quick Revision

```text
Detection-as-Code
→ Detection managed like software

Git
→ Version control

Branch
→ Isolated development path

Pull Request
→ Proposed change for review

CI
→ Automated validation/testing

CD
→ Automated delivery/deployment

Schema
→ Required detection structure

Linting
→ Static quality checks

Unit Test
→ Tests individual detection behavior

Regression Test
→ Prevents previously fixed problems from returning

Backtesting
→ Testing against historical data

Canary
→ Limited production deployment

Shadow Mode
→ Detection runs without normal alerting

Rollback
→ Return to previous known-good version

Detection Health
→ Operational status of a detection

Detection Drift
→ Detection effectiveness changes over time

Detection Debt
→ Accumulated maintenance/testing gaps

Stable ID
→ Persistent detection identifier

Data Contract
→ Expected telemetry schema

Artifact
→ Deployable detection package

Detection SLO
→ Reliability/performance objective
```

---

# 131. Golden Rules

```text
1. Treat detections as production engineering artifacts.

2. Store detections in Git.

3. Give every detection a stable ID.

4. Use consistent naming.

5. Keep metadata with detection logic.

6. Require code review.

7. Validate syntax automatically.

8. Validate schemas automatically.

9. Test positive behavior.

10. Test negative behavior.

11. Maintain regression tests.

12. Test edge cases.

13. Test at production-scale volumes.

14. Validate ATT&CK mappings.

15. Document telemetry dependencies.

16. Never hard-code secrets.

17. Keep production branches protected.

18. Use CI before merging.

19. Use staging before production.

20. Use canary or shadow deployment for high-impact changes.

21. Monitor production detection health.

22. Monitor alert volume.

23. Monitor detection latency.

24. Monitor sudden alert increases.

25. Monitor sudden alert decreases.

26. Maintain rollback capability.

27. Track ownership.

28. Track versions.

29. Keep an audit trail.

30. Review detections periodically.

31. Detect schema drift.

32. Detect query drift.

33. Detect dependency drift.

34. Retire obsolete detections.

35. Avoid unnecessary duplicate rules.

36. Treat detection failures as production failures.

37. Detection-as-Code is more than storing rules in Git.

38. The complete model is:
    Code + Review + Test + Deploy + Monitor + Improve.
```

---

# 132. Final Mental Model

Think of a detection exactly like production software:

```text
IDEA
 ↓
DESIGN
 ↓
CODE
 ↓
TEST
 ↓
REVIEW
 ↓
BUILD
 ↓
STAGE
 ↓
CANARY
 ↓
PRODUCTION
 ↓
MONITOR
 ↓
TUNE
 ↓
VERSION
 ↓
RETIRE
```

The complete Detection-as-Code pipeline:

```text
Threat Intelligence
       ↓
Detection Hypothesis
       ↓
Detection Code
       ↓
Git
       ↓
Pull Request
       ↓
Code Review
       ↓
CI
 ┌─────┼─────┐
 ↓     ↓     ↓
Schema Lint Tests
 └─────┼─────┘
       ↓
     Build
       ↓
    Staging
       ↓
    Canary
       ↓
   Production
       ↓
   Monitoring
       ↓
    Feedback
       ↓
     Tuning
       ↓
   New Version
```

A mature detection team should be able to answer:

```text
What detection is running?
Who owns it?
What version is deployed?
Why was it created?
What threat does it detect?
What ATT&CK technique does it cover?
What telemetry does it require?
Has it been tested?
When was it last changed?
Who approved it?
How is it performing?
How do we roll it back?
```

If those questions cannot be answered, the detection lifecycle is probably not mature enough.

---

# 133. Chapter Summary

This chapter covered:

```text
Detection-as-Code
Git
Version Control
Detection Repositories
Naming Conventions
Stable Detection IDs
Metadata
Branches
Pull Requests
Code Review
Schemas
Linting
Query Validation
Sigma
Platform-Specific Detection
Detection Compilation
CI
CD
Staging
Canary Deployment
Shadow Mode
Rollback
Versioning
Detection Ownership
Data Contracts
Detection Contracts
Unit Testing
Negative Testing
Regression Testing
Historical Replay
Backtesting
Quality Gates
ATT&CK Gates
Duplicate Detection
Dead Detection
Detection Health
Detection Monitoring
Alert Volume Monitoring
Detection Drift
Schema Drift
Query Drift
Dependency Drift
Secret Management
Branch Protection
CODEOWNERS
Change Management
Emergency Changes
Deployment Audit Trails
Feature Flags
Detection Observability
Detection SLOs
Detection Reliability
Detection Lifecycle
Detection Retirement
Detection Maturity
```

The central principle is:

> **A detection is production software with a security purpose. It should be version-controlled, reviewed, tested, deployed safely, monitored continuously, and retired deliberately.**

The mature model is:

```text
DETECT
  ↓
CODE
  ↓
REVIEW
  ↓
TEST
  ↓
DEPLOY
  ↓
MONITOR
  ↓
TUNE
  ↓
VERSION
  ↓
RETIRE
```

Detection-as-Code transforms detection engineering from a collection of manually configured SIEM rules into a **repeatable, auditable, scalable engineering discipline**.