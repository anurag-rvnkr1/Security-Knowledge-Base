# Chapter 08 – MITRE ATT&CK & Threat-Informed Detection

> Threat-informed detection uses knowledge about real-world adversaries, attack techniques, procedures, campaigns, and objectives to design detections that are relevant to actual threats. MITRE ATT&CK provides a structured framework for understanding adversary behavior and mapping that behavior to telemetry, detections, tests, and defensive coverage.

---

# 1. Introduction

Traditional detection development may begin with:

```text
What logs do we have?
        ↓
What rules can we write?
```

Threat-informed detection reverses the perspective:

```text
What threats matter to us?
        ↓
How do those threats operate?
        ↓
What TTPs do they use?
        ↓
What telemetry would reveal those TTPs?
        ↓
What detections should we build?
        ↓
How do we test coverage?
```

This produces detections that are driven by:

```text
Threats
+
Adversary Behavior
+
Organizational Risk
```

rather than simply by available data.

---

# 2. What Is Threat-Informed Detection?

Threat-informed detection is the practice of designing and prioritizing detections based on:

```text
Threat Actors
Attack Campaigns
Malware
Tactics
Techniques
Procedures
Targeting
Infrastructure
Business Risk
```

The goal is:

```text
Relevant Threat
      ↓
Expected Adversary Behavior
      ↓
Observable Telemetry
      ↓
Detection
      ↓
Validation
```

---

# 3. Why Threat Intelligence Matters

A detection team has limited:

```text
Time
Engineering Capacity
Telemetry
Analyst Capacity
Infrastructure
```

Therefore, not every possible attack can receive equal detection effort.

Threat intelligence helps answer:

```text
Which threats are most relevant?
Which techniques are most likely?
Which assets are targeted?
Which behaviors should we prioritize?
```

---

# 4. MITRE ATT&CK

:contentReference[oaicite:0]{index=0} ATT&CK is a knowledge base and framework for describing adversary behavior.

It organizes adversary activity into concepts such as:

```text
Tactics
Techniques
Sub-Techniques
Procedures
Groups
Software
Campaigns
Mitigations
Data Sources
```

---

# 5. ATT&CK Enterprise

The Enterprise knowledge base focuses on adversary behavior against enterprise environments.

It covers areas such as:

```text
Windows
Linux
macOS
Cloud
Identity
Containers
Network Infrastructure
Applications
```

The exact platform coverage evolves over time.

---

# 6. ATT&CK Tactics

Tactics represent the adversary's high-level objectives.

Common Enterprise tactics include:

```text
Reconnaissance
Resource Development
Initial Access
Execution
Persistence
Privilege Escalation
Defense Evasion
Credential Access
Discovery
Lateral Movement
Collection
Command and Control
Exfiltration
Impact
```

Not every attack uses every tactic.

---

# 7. Tactic vs Technique

### Tactic

Answers:

```text
WHY?
```

Example:

```text
Credential Access
```

### Technique

Answers:

```text
HOW?
```

Example:

```text
Credential Dumping
```

---

# 8. Sub-Techniques

Some techniques have more specific subdivisions.

Conceptually:

```text
Technique
   ├── Sub-Technique A
   ├── Sub-Technique B
   └── Sub-Technique C
```

Sub-techniques allow more precise detection mapping.

---

# 9. Procedures

A procedure describes how an adversary or software has actually used a technique.

Example:

```text
Technique:
Command and Scripting Interpreter

Procedure:
Adversary uses a scripting interpreter
to execute commands.
```

Different adversaries may implement the same technique differently.

---

# 10. TTP Model

The hierarchy can be remembered as:

```text
Tactic
   ↓
Technique
   ↓
Procedure
```

Example:

```text
Credential Access
       ↓
Credential Dumping
       ↓
Specific Tool / Method
```

---

# 11. Why TTPs Are Valuable

Attackers can change:

```text
Hashes
Domains
IP Addresses
Malware Samples
Filenames
Infrastructure
```

But the underlying objective and technique may remain similar.

Therefore:

```text
IOC Detection
      +
TTP Detection
```

is stronger than IOC detection alone.

---

# 12. Threat-Informed Detection Lifecycle

```text
Threat Intelligence
       ↓
Threat Prioritization
       ↓
TTP Identification
       ↓
Telemetry Mapping
       ↓
Detection Design
       ↓
Implementation
       ↓
Testing
       ↓
Coverage Measurement
       ↓
Tuning
       ↓
Continuous Improvement
```

---

# 13. Threat Intelligence Sources

Potential sources include:

```text
Internal Incidents
Threat Research
Security Vendors
Government Advisories
CERTs
ISACs
Incident Response Teams
Malware Analysis
Threat Hunting
Security Communities
```

Source quality should always be evaluated.

---

# 14. Strategic Threat Intelligence

Strategic intelligence answers:

```text
Who may target us?
Why?
What are their objectives?
What sectors are targeted?
What trends are emerging?
```

It helps leadership make security decisions.

---

# 15. Operational Threat Intelligence

Operational intelligence focuses on:

```text
Campaigns
Threat Actors
Attack Patterns
Targeting
Infrastructure
Timing
```

It helps security teams understand active campaigns.

---

# 16. Tactical Threat Intelligence

Tactical intelligence focuses on:

```text
Tactics
Techniques
Procedures
Adversary Behavior
```

This is particularly useful for detection engineering.

---

# 17. Technical Threat Intelligence

Technical intelligence includes:

```text
IPs
Domains
URLs
Hashes
Certificates
Email Addresses
Malware Artifacts
```

These indicators can feed:

```text
SIEM
EDR
Firewall
Email Security
SOAR
```

---

# 18. Threat Intelligence Pyramid

A useful conceptual model:

```text
                 Strategic
              ───────────────
                Operational
            ───────────────────
                  Tactical
        ───────────────────────────
                 Technical
```

Detection engineering often benefits from tactical intelligence while using technical intelligence for IOC-based detections.

---

# 19. Threat Prioritization

Not every threat deserves the same detection effort.

Consider:

```text
Likelihood
Impact
Targeting
Exposure
Business Criticality
Threat Intelligence
Existing Controls
Detection Gaps
```

---

# 20. Threat Relevance

A threat may be highly dangerous but irrelevant to an organization.

Example:

```text
Threat targets:
Industrial Control Systems

Organization:
Cloud-only SaaS
```

Detection priorities should reflect actual exposure.

---

# 21. Threat Modeling

Threat modeling asks:

```text
What are we protecting?
Who might attack?
How could they attack?
What would they target?
What controls exist?
Where are the gaps?
```

---

# 22. Threat-Informed Detection Example

Suppose intelligence indicates a threat actor commonly uses:

```text
Phishing
Credential Access
PowerShell
Remote Services
Cloud Account Abuse
```

Detection priorities become:

```text
Email Detection
+
Identity Detection
+
Endpoint Detection
+
Lateral Movement Detection
+
Cloud Detection
```

---

# 23. Threat-to-Detection Mapping

Create a mapping:

| Threat | Tactic | Technique | Telemetry | Detection |
|---|---|---|---|---|
| Threat A | Execution | Technique X | EDR | Rule A |
| Threat A | Credential Access | Technique Y | Identity | Rule B |
| Threat A | Lateral Movement | Technique Z | Network | Rule C |

This turns intelligence into engineering work.

---

# 24. ATT&CK Navigator Concept

ATT&CK coverage can be visualized as a matrix of:

```text
Tactics
     ×
Techniques
```

A team can mark:

```text
Covered
Partially Covered
Not Covered
Tested
High Priority
```

This makes gaps easier to communicate.

---

# 25. Coverage Does Not Mean Detection Exists

A technique should not be considered fully covered simply because:

```text
A rule exists.
```

Meaningful coverage requires:

```text
Telemetry
+
Detection
+
Testing
+
Relevant Environment
+
Acceptable Quality
```

---

# 26. Detection Coverage Levels

A useful internal model:

```text
0 = No Coverage

1 = Telemetry Only

2 = Detection Exists

3 = Detection Tested

4 = Detection Tuned

5 = Detection Monitored
```

Organizations can define their own maturity model.

---

# 27. Telemetry Coverage

Before writing a detection, determine:

```text
What data source reveals the technique?
```

Examples:

```text
Process Creation
Authentication
DNS
Network Traffic
Cloud Audit Logs
Email
File Events
Registry
API Calls
```

---

# 28. ATT&CK Data Sources

ATT&CK can help identify relevant telemetry categories.

Conceptually:

```text
Technique
   ↓
Required Observation
   ↓
Data Source
   ↓
Telemetry
```

This helps detection engineers identify logging gaps.

---

# 29. Telemetry Gap

Example:

```text
Technique:
Credential Access

Required:
Endpoint Telemetry

Available:
Only Network Logs
```

Result:

```text
Detection Gap
```

Possible actions:

```text
Improve Logging
Deploy EDR
Use Alternative Detection
Accept Risk
```

---

# 30. Detection Gap

Example:

```text
Telemetry:
Available

Detection:
Missing
```

This is an engineering gap rather than a collection gap.

---

# 31. Validation Gap

Example:

```text
Telemetry:
Available

Detection:
Available

Testing:
Missing
```

This means the team cannot confidently determine whether the detection works.

---

# 32. Coverage Gap Types

Common categories:

```text
Telemetry Gap
Detection Gap
Testing Gap
Tuning Gap
Response Gap
Visibility Gap
```

---

# 33. Threat-Informed Detection Prioritization

Prioritize techniques using:

```text
Threat Relevance
+
Asset Exposure
+
Technique Frequency
+
Potential Impact
+
Detection Gap
```

---

# 34. High-Priority Technique

Example:

```text
Threat Actor Uses Technique X
+
Organization Exposed
+
Critical Assets Targeted
+
No Existing Detection
```

This should likely become a high-priority engineering task.

---

# 35. Low-Priority Technique

Example:

```text
Rare Threat
+
No Organizational Exposure
+
Existing Strong Controls
+
Low Business Impact
```

May receive lower priority.

---

# 36. Detection Hypothesis

A detection hypothesis describes:

```text
What adversary behavior do we expect?
Why would it be suspicious?
What telemetry should reveal it?
What legitimate activity may look similar?
```

Example:

```text
Hypothesis:
An attacker gaining access to a privileged account
may authenticate from a new device and immediately
perform privilege-sensitive actions.
```

---

# 37. Hypothesis-Driven Detection

Workflow:

```text
Threat
 ↓
Hypothesis
 ↓
Observable Behavior
 ↓
Telemetry
 ↓
Detection
 ↓
Test
```

This is stronger than writing arbitrary rules.

---

# 38. Threat Hunting and Detection Engineering

Threat hunting can identify:

```text
New Behavior
Detection Gaps
New Procedures
False Assumptions
```

Then successful hunts can become:

```text
Production Detections
```

---

# 39. Hunt-to-Detection Lifecycle

```text
Threat Hypothesis
      ↓
Threat Hunt
      ↓
Observed Behavior
      ↓
Detection Logic
      ↓
Testing
      ↓
Production
```

---

# 40. Incident-to-Detection Lifecycle

Incidents can reveal detection gaps.

```text
Incident
   ↓
Root Cause
   ↓
Missed Signal
   ↓
Detection Hypothesis
   ↓
New Detection
   ↓
Validation
```

---

# 41. Intelligence-to-Detection Lifecycle

```text
Threat Report
      ↓
Relevant TTP
      ↓
Internal Exposure
      ↓
Telemetry Check
      ↓
Detection
      ↓
Simulation
```

---

# 42. Detection Engineering From ATT&CK

For each relevant technique:

```text
1. Understand the technique.
2. Identify procedures.
3. Identify telemetry.
4. Define detection hypothesis.
5. Write detection.
6. Test detection.
7. Tune false positives.
8. Measure coverage.
```

---

# 43. ATT&CK Mapping Metadata

A detection may contain:

```text
Detection ID
Technique ID
Sub-Technique ID
Tactic
Data Source
Severity
Confidence
Platform
Test Reference
Version
Owner
```

---

# 44. Detection Naming

Use consistent names.

Example:

```text
DET-EXEC-POWERSHELL-001
```

or:

```text
Windows Suspicious Script Interpreter Execution
```

A naming standard improves maintainability.

---

# 45. Detection IDs

Every production detection should ideally have a unique identifier.

Example:

```text
DET-2026-0042
```

This supports:

```text
Versioning
Testing
Metrics
Documentation
Change Management
```

---

# 46. ATT&CK Mapping Example

Conceptually:

```text
Detection:
Suspicious Script Interpreter Activity

Tactic:
Execution

Technique:
Command and Scripting Interpreter

Telemetry:
Process Creation
Command Line
Parent Process
Network
```

The exact ATT&CK mapping should be validated against the current ATT&CK version.

---

# 47. Detection Quality

A detection should be evaluated using:

```text
Precision
Recall
False Positive Rate
Detection Latency
Coverage
Stability
Performance
Analyst Value
```

---

# 48. Precision

Precision answers:

```text
Of the alerts generated,
how many were actually meaningful?
```

Conceptually:

```text
Precision =
True Positives
/
(True Positives + False Positives)
```

---

# 49. Recall

Recall answers:

```text
Of the relevant malicious events,
how many did we detect?
```

Conceptually:

```text
Recall =
True Positives
/
(True Positives + False Negatives)
```

---

# 50. Precision vs Recall

High precision:

```text
Few false alerts
```

High recall:

```text
Few missed threats
```

Detection engineering often requires balancing both.

---

# 51. ATT&CK Coverage vs Detection Quality

A team may have:

```text
High ATT&CK Coverage
```

but:

```text
Poor Detection Quality
```

if rules produce excessive false positives or are not tested.

Therefore:

```text
Coverage ≠ Quality
```

---

# 52. Threat-Informed Detection Matrix

A useful matrix:

| Technique | Threat Relevance | Telemetry | Detection | Tested | Quality | Priority |
|---|---|---|---|---|---|---|
| T1 | High | Yes | Yes | Yes | High | High |
| T2 | High | Yes | No | No | — | Critical |
| T3 | Medium | Partial | Yes | No | Unknown | Medium |
| T4 | Low | No | No | No | — | Low |

---

# 53. Detection Gap Analysis

Ask:

```text
Which high-priority techniques have:
    No telemetry?
    No detection?
    No testing?
    Poor quality?
```

This provides an actionable engineering roadmap.

---

# 54. Threat Coverage vs Asset Coverage

A detection may work on:

```text
Windows
```

but not:

```text
Linux
Cloud
Containers
```

Therefore coverage should consider platform.

---

# 55. Platform-Specific Detection

The same technique may produce different telemetry:

```text
Windows
→ Event Logs + EDR

Linux
→ Audit Logs + EDR

Cloud
→ Cloud Audit Logs

Container
→ Runtime + Kubernetes Logs
```

Detection engineering must account for these differences.

---

# 56. Threat-Informed Detection for Identity

Focus on:

```text
Authentication
Privilege
MFA
Session
Access
Account Creation
Role Changes
```

Example:

```text
Threat:
Account Takeover

TTP:
Credential Access

Detection:
Unusual Authentication
+
New Device
+
Privilege Change
```

---

# 57. Threat-Informed Detection for Endpoint

Focus on:

```text
Process
File
Registry
Persistence
Command Line
Network
User
```

Example:

```text
Threat:
Malware Execution

Detection:
Suspicious Parent-Child Process
+
Unusual Command Line
+
External Connection
```

---

# 58. Threat-Informed Detection for Network

Focus on:

```text
DNS
Connections
Traffic
Protocols
Destinations
Certificates
Beaconing
```

---

# 59. Threat-Informed Detection for Cloud

Focus on:

```text
API Calls
Identity
Privilege
Resources
Regions
Access Keys
Configuration
```

---

# 60. Threat-Informed Detection for Applications

Focus on:

```text
Authentication
Sessions
API Requests
Authorization
Data Access
Error Patterns
```

---

# 61. Threat-Informed Detection for Containers

Focus on:

```text
Container Creation
Image
Runtime
Process
Network
Privilege
Kubernetes API
Service Account
```

---

# 62. Threat-Informed Detection for SaaS

Focus on:

```text
Authentication
OAuth
API
Administrative Actions
Data Access
File Sharing
External Collaboration
```

---

# 63. ATT&CK and Detection-as-Code

ATT&CK metadata can be stored with detection code.

Example:

```yaml
id: DET-EXEC-001

name: Suspicious Script Execution

techniques:
  - T1059

tactics:
  - Execution

severity: high
```

This makes detection metadata machine-readable.

---

# 64. ATT&CK Tags

Detection repositories can use tags such as:

```text
attack.execution
attack.credential-access
attack.persistence
attack.lateral-movement
```

This enables:

```text
Search
Reporting
Coverage Analysis
Automation
```

---

# 65. ATT&CK Coverage Automation

A CI/CD pipeline can calculate:

```text
Techniques Covered
Techniques Missing
Techniques Untested
Techniques Deprecated
```

This makes coverage measurable.

---

# 66. ATT&CK Versioning

ATT&CK evolves.

Techniques may be:

```text
Added
Updated
Renamed
Split
Merged
Deprecated
```

Detection mappings should therefore be reviewed when ATT&CK changes.

---

# 67. Mapping Drift

A detection may originally map correctly but later become outdated.

Example:

```text
ATT&CK Version 1
→ Technique X

ATT&CK Version 2
→ Technique X changed
```

Review mappings during framework updates.

---

# 68. Avoid Over-Mapping

Do not map a detection to many techniques simply to increase coverage.

Bad:

```text
One Rule
→ 10 Techniques
```

when only one technique is actually supported.

This creates misleading coverage metrics.

---

# 69. Avoid Under-Mapping

Similarly, do not map only the broad tactic when the detection clearly identifies a specific technique.

Good mapping should reflect:

```text
Actual Detection Behavior
```

---

# 70. Detection Evidence

A good ATT&CK mapping should be supported by:

```text
Detection Logic
Telemetry
Test
Behavior
Documentation
```

---

# 71. Procedure-Aware Detection

If threat intelligence identifies:

```text
Threat Actor A
uses
Technique X
through
Procedure Y
```

detection engineers can ask:

```text
Can we detect Procedure Y?
Can we detect the broader Technique X?
What alternative procedures could evade us?
```

---

# 72. Procedure Diversity

One technique can have many implementations.

```text
Technique X
 ├── Procedure A
 ├── Procedure B
 ├── Procedure C
 └── Procedure D
```

A detection covering only Procedure A may provide incomplete technique coverage.

---

# 73. Detection Robustness

Test:

```text
Procedure A
Procedure B
Procedure C
```

to determine whether the detection identifies:

```text
Underlying Technique
```

rather than one implementation.

---

# 74. Threat Actor Profiling

Threat intelligence can provide:

```text
Targeting
Preferred Techniques
Infrastructure
Tools
Malware
Campaigns
```

This can inform detection priorities.

---

# 75. Campaign-Based Detection

A campaign may use:

```text
Phishing
→ Credential Theft
→ Cloud Access
→ Data Collection
```

Instead of detecting each activity independently, build a campaign-aware detection strategy.

---

# 76. Threat Actor vs Malware Detection

Malware-focused:

```text
Detect Malware X
```

Threat-informed:

```text
Detect behaviors commonly associated
with the adversary and its objectives.
```

The second can survive tool changes.

---

# 77. Intelligence Confidence

Threat reports may have different confidence levels.

Consider:

```text
Source Reliability
Evidence
Recency
Independent Confirmation
Internal Validation
```

Avoid treating uncertain intelligence as fact.

---

# 78. Intelligence Recency

Threat intelligence becomes stale.

Track:

```text
First Seen
Last Seen
Published
Updated
Expiration
```

---

# 79. Threat Intelligence Context

An indicator becomes more useful when associated with:

```text
Threat Actor
Campaign
Malware
Technique
Target
Time
Confidence
```

---

# 80. IOC + TTP

Combine:

```text
Known Malicious Domain
+
C2-like Beaconing
+
Suspicious Process
```

This provides stronger evidence than the domain match alone.

---

# 81. TTP + Asset Context

Example:

```text
Credential Access Behavior
+
Domain Controller
```

is more significant than:

```text
Credential Access Behavior
+
Test Machine
```

---

# 82. TTP + Identity Context

Example:

```text
Privilege Escalation
+
Privileged Account
```

may require immediate attention.

---

# 83. TTP + Vulnerability Context

Example:

```text
Exploit-Like Activity
+
Known Vulnerable Server
```

increases confidence and potential impact.

---

# 84. TTP + Network Context

Example:

```text
Remote Service
+
Unexpected Internal Destination
+
Privileged Credential
```

may indicate lateral movement.

---

# 85. Threat-Informed Risk Model

Conceptually:

```text
Risk =
Threat Relevance
+
Behavior
+
Asset Criticality
+
Identity Privilege
+
Detection Confidence
+
Threat Intelligence
```

---

# 86. Threat-Informed Detection Priority

A practical priority score can consider:

```text
Threat Relevance
×
Business Impact
×
Detection Gap
```

The exact formula should be defined and calibrated internally.

---

# 87. Detection Backlog

Maintain a backlog containing:

```text
Detection ID
Threat
Technique
Priority
Telemetry
Owner
Status
Test Status
Coverage
```

Example:

```text
DET-001
Technique: Txxxx
Priority: High
Status: Planned
```

---

# 88. Detection Roadmap

Prioritize:

```text
Critical Threats
+
High-Impact Techniques
+
Large Detection Gaps
+
Available Telemetry
```

Then schedule:

```text
Engineering
Testing
Deployment
Tuning
Review
```

---

# 89. Detection Engineering Metrics

Useful metrics:

```text
ATT&CK Coverage
High-Priority Technique Coverage
Detection Quality
False Positive Rate
False Negative Rate
Detection Latency
Mean Time to Validate
Detection Test Coverage
Telemetry Coverage
```

---

# 90. Coverage Trend

Track:

```text
Month 1:
45 techniques

Month 2:
52 techniques

Month 3:
60 techniques
```

But also track:

```text
Quality
Testing
False Positives
```

Increasing rule count alone is not success.

---

# 91. Detection Debt

Detection debt is accumulated work caused by:

```text
Untested Rules
Poorly Tuned Rules
Missing Telemetry
Outdated Mappings
Undocumented Logic
Stale Exceptions
```

Detection debt reduces long-term detection effectiveness.

---

# 92. Threat-Informed Detection Debt

Examples:

```text
High-Priority Technique
+
No Detection
```

or:

```text
Detection Exists
+
Never Tested
```

These should be visible in engineering metrics.

---

# 93. Detection Review

Periodic reviews should ask:

```text
Is the threat still relevant?
Is the technique still mapped correctly?
Does telemetry still exist?
Does the detection still work?
Are false positives acceptable?
Is the rule still needed?
```

---

# 94. Detection Retirement

Retire detections when:

```text
Threat No Longer Relevant
Telemetry Removed
Technique Deprecated
Rule Replaced
Business Context Changed
False Positive Cost Too High
```

Retirement should be documented rather than silently deleting the rule.

---

# 95. Threat-Informed Detection Testing

Testing should include:

```text
Adversary Simulation
Atomic Tests
Purple Team Exercises
Breach Simulation
Replay
Historical Data
Synthetic Events
```

---

# 96. Atomic Testing

An atomic test validates a specific behavior or technique.

Conceptually:

```text
Technique
   ↓
Controlled Simulation
   ↓
Expected Telemetry
   ↓
Detection
```

Testing must be authorized and performed safely.

---

# 97. Purple Teaming

Purple teaming combines:

```text
Red Team
+
Blue Team
```

to validate defensive capabilities.

The objective is not simply:

```text
Did the attack succeed?
```

but:

```text
Did we observe it?
Did detection trigger?
Was it actionable?
Could we improve it?
```

---

# 98. Purple Team Detection Loop

```text
Threat
 ↓
Technique
 ↓
Simulation
 ↓
Telemetry
 ↓
Detection
 ↓
Analyst
 ↓
Feedback
 ↓
Engineering
```

---

# 99. Threat-Informed Purple Teaming

Select scenarios based on:

```text
Relevant Threat Actors
Relevant Techniques
Critical Assets
Known Detection Gaps
```

This produces higher-value exercises than arbitrary testing.

---

# 100. Detection Validation Questions

After testing:

```text
Did telemetry arrive?
Did the correct rule trigger?
Was the alert timely?
Was the technique mapped correctly?
Was the alert actionable?
Were there false positives?
Did the detection survive minor variation?
```

---

# 101. Detection Resilience

A robust detection should survive reasonable changes in:

```text
Tool
Filename
Hash
IP
Domain
Command Formatting
User
Host
```

when those changes do not fundamentally alter the underlying behavior.

---

# 102. Threat-Informed Detection Architecture

```text
               Threat Intelligence
                       ↓
                Threat Modeling
                       ↓
                ATT&CK Mapping
                       ↓
               Detection Hypothesis
                       ↓
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
     Identity       Endpoint       Network
        ↓              ↓              ↓
        └──────────────┼──────────────┘
                       ↓
                  Correlation
                       ↓
                     Risk
                       ↓
                    Alert
                       ↓
                 Investigation
                       ↓
                    Response
                       ↓
                 Purple Team
                       ↓
                 Improvement
```

---

# 103. Common Mistakes

## Mistake 1 – Checkbox Coverage

```text
Rule exists
=
Technique covered
```

This is incorrect.

---

## Mistake 2 – Over-Mapping

Mapping one detection to many unrelated techniques inflates coverage.

---

## Mistake 3 – Threat Intelligence Without Context

A threat report does not automatically mean the organization is exposed.

---

## Mistake 4 – IOC-Only Detection

Threat actors can change infrastructure.

---

## Mistake 5 – Ignoring Procedures

Technique-level detection may miss procedure-specific gaps.

---

## Mistake 6 – No Testing

An untested detection is not reliable evidence of coverage.

---

## Mistake 7 – Ignoring Telemetry

A theoretically excellent detection cannot work without required data.

---

## Mistake 8 – Ignoring Platform Differences

Windows, Linux, cloud, containers, and SaaS environments expose different telemetry.

---

## Mistake 9 – Stale ATT&CK Mapping

Framework updates can change technique relationships.

---

## Mistake 10 – Measuring Only Rule Count

More rules do not necessarily mean better security.

---

# 104. Practical Exercise – Threat-to-Detection Mapping

Choose a relevant threat.

Document:

```text
Threat Actor:
__________

Target:
__________

Objective:
__________

Tactics:
__________

Techniques:
__________

Procedures:
__________

Required Telemetry:
__________

Existing Detections:
__________

Detection Gaps:
__________

Testing Method:
__________
```

---

# 105. Practical Exercise – ATT&CK Coverage

Create:

| Technique | Telemetry | Detection | Test | Quality | Gap |
|---|---|---|---|---|---|
| T1 | Yes | Yes | Yes | High | No |
| T2 | Yes | Yes | No | Unknown | Yes |
| T3 | Partial | No | No | — | Yes |
| T4 | No | No | No | — | Yes |

Then prioritize the gaps.

---

# 106. Practical Exercise – Detection Hypothesis

Write:

```text
Threat:
Account Takeover

Hypothesis:
An attacker using compromised credentials
may authenticate from a new device and perform
unusual privileged activity.

Telemetry:
Authentication
Device
MFA
Privilege
Resource Access

Detection:
New Device
+
Privileged Action
+
Unusual Location
```

---

# 107. Practical Exercise – Procedure Resilience

Take a detection.

Change:

```text
Tool
Filename
Hash
IP
Command Syntax
```

Ask:

```text
Does the detection still identify
the underlying technique?
```

---

# 108. Practical Exercise – Purple Team

Choose one technique.

Document:

```text
Technique
Threat Scenario
Simulation
Expected Telemetry
Expected Detection
Actual Detection
Latency
False Positives
Improvements
```

---

# 109. Detection Documentation Template

```yaml
id: DET-EXAMPLE-001

name: Example Threat-Informed Detection

description: >
  Detects suspicious behavior associated with
  a relevant adversary technique.

tactics:
  - Execution

techniques:
  - TXXXX

platforms:
  - Windows

data_sources:
  - Endpoint
  - Identity

severity: high

confidence: medium

priority: high

tests:
  - TEST-001

owner:
  team: Detection Engineering

status: production
```

---

# 110. Threat-Informed Detection Checklist

```text
[ ] Threat identified
[ ] Threat relevance validated
[ ] Threat actor/campaign understood
[ ] Tactics identified
[ ] Techniques identified
[ ] Relevant procedures reviewed
[ ] Organizational exposure evaluated
[ ] Critical assets identified
[ ] Required telemetry identified
[ ] Telemetry availability verified
[ ] Detection hypothesis documented
[ ] Detection implemented
[ ] ATT&CK mapping validated
[ ] Positive test created
[ ] Negative test created
[ ] Procedure variation tested
[ ] False positives reviewed
[ ] Coverage measured
[ ] Detection owner assigned
[ ] Review date defined
```

---

# 111. Interview Questions

### What is MITRE ATT&CK?

> A knowledge base and framework that describes adversary tactics, techniques, procedures, software, groups, and other information about real-world adversary behavior.

### What is a tactic?

> The adversary's high-level objective, such as Execution, Persistence, Credential Access, or Lateral Movement.

### What is a technique?

> A method an adversary can use to achieve a tactical objective.

### What is a procedure?

> A specific implementation of a technique used by an adversary or piece of software.

### Why is ATT&CK useful for detection engineering?

> It provides a common language for understanding adversary behavior, identifying telemetry requirements, designing detections, measuring coverage, and planning validation.

### What is threat-informed detection?

> Designing and prioritizing detections based on relevant threats, adversary behavior, organizational exposure, and business risk.

### Does one detection rule mean a technique is covered?

> No. Meaningful coverage should include appropriate telemetry, working detection logic, validation, and relevant environmental coverage.

### What is a detection gap?

> A situation where a relevant adversary behavior cannot be reliably detected because of missing telemetry, missing logic, insufficient testing, or poor detection quality.

### How do you prioritize ATT&CK techniques?

> Consider threat relevance, organizational exposure, asset criticality, potential impact, existing controls, telemetry availability, and detection gaps.

### What is purple teaming?

> A collaborative process where offensive and defensive teams validate whether adversary behaviors generate the expected telemetry and detections and then improve the defensive capability.

### Why should detections be tested against multiple procedures?

> Because the same technique can be implemented in different ways, and a detection tied too closely to one procedure may provide incomplete coverage.

### What is ATT&CK mapping drift?

> When changes to the ATT&CK framework or detection logic cause an existing technique mapping to become outdated or inaccurate.

---

# 112. Quick Revision

```text
Threat-Informed Detection
→ Detection driven by relevant threats and adversary behavior

MITRE ATT&CK
→ Adversary behavior knowledge base

Tactic
→ Adversary objective

Technique
→ Method used to achieve objective

Sub-Technique
→ More specific technique category

Procedure
→ Specific implementation

Threat Intelligence
→ Information about threats and adversaries

Threat Modeling
→ Understanding threats, assets, attack paths, and controls

Detection Hypothesis
→ Testable statement about expected adversary behavior

Telemetry
→ Data required to observe behavior

Detection Gap
→ Relevant behavior cannot be reliably detected

Coverage
→ Extent to which relevant behavior is observable and detectable

Purple Team
→ Collaborative offensive/defensive validation

Detection Debt
→ Accumulated maintenance, testing, telemetry, and quality gaps

ATT&CK Mapping
→ Connecting detection logic to adversary behavior

Threat Relevance
→ How applicable a threat is to the organization
```

---

# 113. Golden Rules

```text
1. Build detections around relevant threats.

2. Understand the adversary before writing the rule.

3. Use ATT&CK as a behavioral framework, not a checkbox exercise.

4. Distinguish tactics, techniques, and procedures.

5. Identify telemetry before implementing detection logic.

6. Validate that the organization is actually exposed to the threat.

7. Prioritize high-impact detection gaps.

8. Do not treat every threat intelligence report as equally relevant.

9. Combine technical and tactical intelligence.

10. Do not rely exclusively on IOCs.

11. Test detections against multiple procedures.

12. Measure actual detection quality.

13. Coverage requires telemetry, detection, and validation.

14. Keep ATT&CK mappings accurate and current.

15. Avoid over-mapping detections.

16. Avoid under-mapping meaningful behavior.

17. Use threat hunting to discover new detection opportunities.

18. Turn valuable incident findings into detections.

19. Use purple teaming to validate real detection capability.

20. Track detection debt.

21. Track telemetry gaps separately from detection gaps.

22. Consider platform-specific differences.

23. Use threat relevance to prioritize engineering effort.

24. Document detection hypotheses.

25. Make detection mappings auditable.

26. Review detections as threats and environments evolve.

27. Measure coverage by meaningful adversary behavior, not rule count.

28. A detection that has never been tested should not be treated as proven coverage.

29. Threat-informed detection should continuously connect intelligence, engineering, testing, and operations.

30. The ultimate goal is not maximum ATT&CK coverage—it is reliable detection of the threats that matter most to the organization.
```

---

# 114. Final Mental Model

Think of threat-informed detection as:

```text
WHO MAY ATTACK US?
        ↓
WHY WOULD THEY ATTACK?
        ↓
WHAT ARE THEIR OBJECTIVES?
        ↓
WHAT TACTICS DO THEY USE?
        ↓
WHAT TECHNIQUES DO THEY USE?
        ↓
HOW ARE THOSE TECHNIQUES IMPLEMENTED?
        ↓
WHAT WOULD WE OBSERVE?
        ↓
DO WE HAVE THE TELEMETRY?
        ↓
CAN WE DETECT IT?
        ↓
CAN WE TEST IT?
        ↓
HOW GOOD IS THE DETECTION?
        ↓
WHAT ARE THE GAPS?
        ↓
HOW DO WE IMPROVE?
```

The complete loop is:

```text
Threat Intelligence
        ↓
Threat Modeling
        ↓
MITRE ATT&CK
        ↓
TTP Prioritization
        ↓
Telemetry Mapping
        ↓
Detection Engineering
        ↓
Testing
        ↓
Purple Teaming
        ↓
Coverage Measurement
        ↓
Tuning
        ↓
Continuous Improvement
```

---

# 115. Chapter Summary

This chapter covered:

```text
Threat-Informed Detection
MITRE ATT&CK
ATT&CK Enterprise
Tactics
Techniques
Sub-Techniques
Procedures
Threat Intelligence
Strategic Intelligence
Operational Intelligence
Tactical Intelligence
Technical Intelligence
Threat Modeling
Threat Prioritization
Threat Relevance
Detection Hypotheses
Telemetry Mapping
Detection Gaps
Coverage Gaps
ATT&CK Coverage
Detection Quality
Precision
Recall
Threat Hunting
Incident-to-Detection
Intelligence-to-Detection
ATT&CK Mapping
Procedure-Aware Detection
Threat Actor Profiling
Campaign-Based Detection
Detection Resilience
Detection Backlog
Detection Debt
Purple Teaming
Atomic Testing
Detection Validation
ATT&CK Versioning
Mapping Drift
```

The central principle is:

> **Detection engineering should begin with the threats that matter, translate those threats into adversary behaviors, map those behaviors to observable telemetry, build and test detections around them, and continuously measure whether the organization can actually detect the techniques it cares about.**

A mature detection program therefore follows:

```text
THREAT
  ↓
TTP
  ↓
TELEMETRY
  ↓
DETECTION
  ↓
TEST
  ↓
MEASURE
  ↓
TUNE
  ↓
IMPROVE
```

The objective is not to create the largest number of detection rules or claim the highest number of ATT&CK techniques. The objective is to build **reliable, tested, threat-relevant detection coverage that gives defenders meaningful visibility into adversary activity.**

---