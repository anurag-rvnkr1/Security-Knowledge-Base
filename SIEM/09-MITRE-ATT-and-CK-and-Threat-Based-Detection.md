# Chapter 09 – MITRE ATT&CK & Threat-Based Detection

> MITRE ATT&CK provides a structured knowledge base of adversary tactics and techniques. In a SIEM/SOC, it helps security teams understand attacker behavior, map detections to attack techniques, identify visibility gaps, prioritize detection engineering, and organize threat hunting.

---

# 1. Introduction

A SIEM tells us:

```text
What happened?
```

Threat intelligence tells us:

```text
What is this indicator associated with?
```

MITRE ATT&CK helps answer:

```text
What attacker behavior does this represent?

What objective was the attacker pursuing?

What technique could have been used?

Do we have telemetry to detect it?

Do our existing detections cover it?
```

The overall relationship is:

```text
ATTACKER
   ↓
TACTIC
   ↓
TECHNIQUE
   ↓
SUB-TECHNIQUE
   ↓
BEHAVIOR
   ↓
TELEMETRY
   ↓
DETECTION
   ↓
ALERT
   ↓
INVESTIGATION
```

---

# 2. What is MITRE ATT&CK?

MITRE ATT&CK is a knowledge base describing adversary tactics and techniques based on observed real-world behavior.

It is commonly used for:

```text
Detection Engineering
Threat Hunting
Incident Response
Adversary Emulation
Security Testing
Purple Teaming
Security Architecture
SOC Training
Coverage Assessment
```

---

# 3. What Does ATT&CK Represent?

At a high level:

```text
TACTIC
    ↓
Why the attacker is doing something

TECHNIQUE
    ↓
How the attacker achieves an objective

SUB-TECHNIQUE
    ↓
More specific implementation of a technique
```

---

# 4. Tactic

A tactic represents the attacker's objective.

Examples include concepts such as:

```text
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

The exact ATT&CK catalog can evolve, so always verify current technique/tactic identifiers when producing production mappings.

---

# 5. Technique

A technique describes a method an adversary can use to achieve a tactical objective.

Examples:

```text
Phishing
Command and Scripting Interpreter
Credential Dumping
Remote Services
Data from Local System
Application Layer Protocol
```

---

# 6. Sub-Technique

A sub-technique provides more specific detail.

For example, a broad technique involving command interpreters can have separate sub-techniques for different interpreters.

Conceptually:

```text
Technique
   ↓
Command and Scripting Interpreter
   ├── PowerShell
   ├── Windows Command Shell
   ├── Unix Shell
   └── Other Interpreters
```

---

# 7. Tactic vs Technique

Remember:

```text
TACTIC
=
Why

TECHNIQUE
=
How
```

Example:

```text
Tactic:
Credential Access

Technique:
Credential Dumping
```

---

# 8. Why SOC Teams Use ATT&CK

ATT&CK provides a common language.

Instead of saying:

```text
"Some suspicious PowerShell activity happened."
```

a SOC can describe:

```text
Command and Scripting Interpreter
→ PowerShell
```

This improves:

```text
Communication
Detection Documentation
Threat Hunting
Coverage Measurement
Reporting
```

---

# 9. ATT&CK IDs

ATT&CK techniques have identifiers.

Conceptually:

```text
Txxxx
```

Sub-techniques may appear as:

```text
Txxxx.xxx
```

Example:

```text
T1059
```

represents a technique family, while a specific sub-technique can have a more detailed identifier.

Always verify identifiers against the current ATT&CK knowledge base before using them in production documentation.

---

# 10. Enterprise ATT&CK

The Enterprise matrix focuses on adversary behavior affecting enterprise environments.

It is commonly relevant to:

```text
Windows
Linux
macOS
Cloud
Identity
Networked Enterprise Systems
```

---

# 11. Other ATT&CK Domains

MITRE maintains ATT&CK knowledge across different technology domains.

Depending on the security program, teams may encounter:

```text
Enterprise
Mobile
ICS
```

The exact scope depends on the environment being defended.

---

# 12. Attack Lifecycle

A simplified attack chain can be visualized as:

```text
Initial Access
      ↓
Execution
      ↓
Persistence
      ↓
Privilege Escalation
      ↓
Defense Evasion
      ↓
Credential Access
      ↓
Discovery
      ↓
Lateral Movement
      ↓
Collection
      ↓
Command & Control
      ↓
Exfiltration
      ↓
Impact
```

Real attacks do not necessarily follow this exact linear order.

Attackers can:

```text
Skip stages
Repeat stages
Move backward
Run multiple techniques simultaneously
```

---

# 13. Initial Access

Objective:

```text
Gain entry into the environment.
```

Possible behaviors:

```text
Phishing
Exploit Public-Facing Application
Valid Accounts
External Remote Services
Drive-by Compromise
```

Telemetry may include:

```text
Email
Web
VPN
Identity
Firewall
Application Logs
```

---

# 14. Execution

Objective:

```text
Run attacker-controlled code.
```

Examples:

```text
PowerShell
Command Shell
Scripting
Malicious Files
Remote Execution
```

Telemetry:

```text
Endpoint
Process
EDR
Application
Command-Line Logging
```

---

# 15. Persistence

Objective:

```text
Maintain access after initial compromise.
```

Examples:

```text
Scheduled Tasks
Services
Startup Items
Account Manipulation
Cloud Persistence
```

Telemetry:

```text
Endpoint
Identity
System
Cloud
Configuration
```

---

# 16. Privilege Escalation

Objective:

```text
Obtain higher privileges.
```

Examples:

```text
Privilege Abuse
Exploitation
Account Manipulation
Token Abuse
```

Telemetry:

```text
Identity
Endpoint
Process
Security Logs
```

---

# 17. Defense Evasion

Objective:

```text
Avoid detection or weaken security controls.
```

Examples:

```text
Disable Security Tools
Modify Logs
Obfuscated Files
Masquerading
Indicator Removal
```

Telemetry:

```text
Endpoint
Security Tools
System Logs
Configuration Logs
```

---

# 18. Credential Access

Objective:

```text
Obtain authentication material.
```

Examples:

```text
Credential Dumping
Password Stores
Keylogging
Input Capture
Browser Credentials
```

Telemetry:

```text
EDR
Authentication
Process
File
Memory Security Events
```

---

# 19. Discovery

Objective:

```text
Understand the environment.
```

Examples:

```text
System Discovery
Account Discovery
Network Discovery
Process Discovery
File Discovery
Cloud Resource Discovery
```

Telemetry:

```text
Endpoint
Network
Cloud
Identity
Process
```

---

# 20. Lateral Movement

Objective:

```text
Move from one system to another.
```

Examples:

```text
Remote Services
Remote Desktop
SMB
Valid Accounts
Administrative Shares
```

Telemetry:

```text
Authentication
Network
Endpoint
Remote Access
```

---

# 21. Collection

Objective:

```text
Gather useful information.
```

Examples:

```text
File Collection
Email Collection
Screen Capture
Archive Collected Data
Data from Local System
```

Telemetry:

```text
Endpoint
File
Email
DLP
Application
```

---

# 22. Command and Control

Objective:

```text
Communicate with attacker infrastructure.
```

Examples:

```text
Web Protocols
DNS
Encrypted Channels
Application Layer Protocols
Proxy-based Communication
```

Telemetry:

```text
DNS
Proxy
Firewall
Network Flow
Endpoint
```

---

# 23. Exfiltration

Objective:

```text
Move stolen data outside the environment.
```

Examples:

```text
Exfiltration Over Web Service
Automated Exfiltration
Exfiltration Over C2 Channel
```

Telemetry:

```text
Proxy
Firewall
DLP
Cloud
Network Flow
Endpoint
```

---

# 24. Impact

Objective:

```text
Disrupt or damage systems and data.
```

Examples:

```text
Data Destruction
Data Encrypted for Impact
Service Stop
Resource Hijacking
```

Telemetry:

```text
Endpoint
Application
Cloud
Storage
Security Controls
```

---

# 25. ATT&CK and SIEM

A SIEM can map:

```text
Event
 ↓
Detection
 ↓
Technique
 ↓
Tactic
```

Example:

```text
PowerShell Process
      ↓
Detection
      ↓
PowerShell Technique
      ↓
Execution
```

---

# 26. ATT&CK-Based Detection

Instead of starting with:

```text
"Which logs do we have?"
```

start with:

```text
"What adversary behavior do we need to detect?"
```

Then:

```text
Behavior
 ↓
Technique
 ↓
Telemetry
 ↓
Detection
```

This is called:

```text
Threat-Informed Detection Engineering
```

---

# 27. Threat-Informed Detection Engineering

Workflow:

```text
Threat
   ↓
Adversary Behavior
   ↓
ATT&CK Technique
   ↓
Required Telemetry
   ↓
Detection Logic
   ↓
Testing
   ↓
Deployment
```

---

# 28. Example – PowerShell

Behavior:

```text
Attacker executes PowerShell.
```

ATT&CK mapping:

```text
Execution
   ↓
Command and Scripting Interpreter
   ↓
PowerShell
```

Telemetry:

```text
Process Creation
Command Line
PowerShell Logs
EDR
```

Detection:

```text
PowerShell
+
Suspicious Arguments
+
Suspicious Parent
```

---

# 29. Example – Credential Dumping

Behavior:

```text
Process attempts to access
credential-related memory.
```

Potential ATT&CK mapping:

```text
Credential Access
   ↓
Credential Dumping
```

Telemetry:

```text
EDR
Process Access
Security Logs
```

Detection:

```text
Suspicious Process
+
Sensitive Process Access
```

---

# 30. Example – Remote Desktop

Behavior:

```text
Remote login to another host.
```

Potential mapping:

```text
Lateral Movement
   ↓
Remote Services
   ↓
Remote Desktop Protocol
```

Telemetry:

```text
Authentication
Network
Endpoint
Remote Desktop Logs
```

Detection:

```text
Unusual RDP Login
+
Privileged Account
+
New Source Host
```

---

# 31. Example – Scheduled Task

Behavior:

```text
New scheduled task created.
```

Potential mapping:

```text
Persistence
```

Telemetry:

```text
Windows Event Logs
Endpoint
Task Scheduler
```

Detection:

```text
New Scheduled Task
+
Suspicious Command
+
Unexpected User
```

---

# 32. ATT&CK Mapping Should Not Be Arbitrary

A detection should not be mapped to a technique merely because the technique sounds related.

Bad:

```text
Any PowerShell Event
→
Credential Access
```

Better:

```text
PowerShell used to access
credential material
→
Credential Access technique
```

Mapping should reflect the actual behavior detected.

---

# 33. One Detection Can Map to Multiple Techniques

Some detections may involve multiple behaviors.

Example:

```text
PowerShell
+
Encoded Command
+
Credential Access
```

Possible mappings:

```text
Execution
Defense Evasion
Credential Access
```

Document mappings carefully.

---

# 34. One Technique Can Have Multiple Detections

Example:

```text
Credential Dumping
```

may be detected through:

```text
EDR
Process Access
Memory Access
Known Tools
Suspicious Command Lines
```

This creates defense-in-depth.

---

# 35. Detection Coverage

A coverage matrix can show:

```text
Technique
Telemetry
Detection
Status
```

Example:

```text
Technique              Detection
--------------------------------------
PowerShell              ✓
Credential Dumping      ✓
Remote Desktop          ✓
Cloud Account Abuse     ?
DNS Tunneling           ?
Data Exfiltration       ✓
```

---

# 36. Coverage Does Not Equal Security

A team may claim:

```text
90% ATT&CK Coverage
```

but this does not automatically mean:

```text
90% Security
```

Why?

Because coverage may differ in:

```text
Detection Quality
Telemetry Quality
Technique Variants
False Positives
Detection Latency
Analyst Usability
```

---

# 37. Detection Coverage Levels

A useful model:

```text
Level 0:
No Visibility

Level 1:
Telemetry Exists

Level 2:
Basic Detection

Level 3:
High-Quality Detection

Level 4:
Correlation

Level 5:
Automated Response
```

This is a conceptual maturity model, not an official ATT&CK rating.

---

# 38. Telemetry Coverage

Before creating a detection:

```text
Do we have the required telemetry?
```

Example:

```text
Technique:
PowerShell

Required:
Process Creation

Available:
Yes

Detection:
Yes
```

---

# 39. Detection Gap

Example:

```text
Technique:
Credential Dumping

Telemetry:
Limited

Detection:
None
```

This is a:

```text
Detection Gap
```

---

# 40. Visibility Gap

Different problem:

```text
Technique:
Cloud Account Abuse

Telemetry:
Not collected
```

This is primarily a:

```text
Visibility Gap
```

You cannot build a reliable detection if critical telemetry is unavailable.

---

# 41. Detection Gap vs Visibility Gap

```text
Visibility Gap
=
Data missing

Detection Gap
=
Data exists but detection is missing/insufficient
```

This distinction is important for security engineering.

---

# 42. ATT&CK and Threat Hunting

ATT&CK can generate hunting hypotheses.

Example:

```text
Technique:
Discovery

Question:
Are compromised hosts performing
unusual network discovery?
```

Then:

```text
Search
 ↓
Analyze
 ↓
Pivot
 ↓
Validate
```

---

# 43. ATT&CK-Based Hunt

Example:

```text
Technique:
PowerShell

Hypothesis:
Attackers may be using PowerShell
for execution.
```

Search:

```text
PowerShell processes
```

Then filter:

```text
Encoded commands
Unusual parent
External network
Privileged user
Rare host
```

---

# 44. Threat Actor Profiling

Threat intelligence may indicate:

```text
Actor commonly uses:
PowerShell
Credential Dumping
Remote Services
```

SOC can prioritize:

```text
Those techniques
+
Relevant telemetry
```

---

# 45. Campaign-Based Detection

A campaign may involve:

```text
Phishing
 ↓
Credential Theft
 ↓
Cloud Login
 ↓
Persistence
 ↓
Data Access
```

Map each behavior to:

```text
ATT&CK
```

Then build detections across the chain.

---

# 46. Attack Chain Correlation

Example:

```text
Phishing Detection
       ↓
Credential Abuse
       ↓
PowerShell
       ↓
Discovery
       ↓
Lateral Movement
```

Correlation can elevate confidence.

---

# 47. ATT&CK Navigator Concept

Security teams can visualize:

```text
Techniques
Tactics
Coverage
Detection Status
```

A matrix can highlight:

```text
Green:
Strong Detection

Yellow:
Partial Detection

Red:
Gap
```

This helps prioritize engineering.

---

# 48. Coverage Matrix Example

```text
TACTIC              TECHNIQUE             STATUS
--------------------------------------------------
Initial Access      Phishing              ✓
Execution           PowerShell            ✓
Persistence         Scheduled Task        ✓
Credential Access   Credential Dumping    ✓
Discovery           Network Discovery     ?
Lateral Movement    Remote Services       ✓
C2                  DNS                   ?
Exfiltration        Web Service           ✗
Impact              Data Encryption       ✓
```

---

# 49. Detection Prioritization

Do not simply detect techniques because they are available.

Prioritize based on:

```text
Threat Relevance
Business Risk
Asset Exposure
Telemetry Quality
Attack Prevalence
Detection Difficulty
Existing Gaps
Incident History
```

---

# 50. Threat Modeling

A threat model asks:

```text
Who might attack us?

What do they want?

How might they enter?

What assets would they target?

What techniques could they use?

Where can we detect them?
```

ATT&CK helps structure the attacker behavior portion.

---

# 51. ATT&CK and Purple Teaming

Purple teaming connects:

```text
Offense
+
Defense
```

Workflow:

```text
ATT&CK Technique
      ↓
Controlled Emulation
      ↓
Telemetry
      ↓
Detection
      ↓
Alert
      ↓
Analyst Investigation
      ↓
Gap Identified
      ↓
Improve Detection
```

Only perform emulation in authorized environments.

---

# 52. Detection Validation

A detection mapped to ATT&CK should be validated.

Example:

```text
Technique:
PowerShell

Test:
Controlled PowerShell execution

Expected:
Telemetry

Expected:
Detection

Expected:
Alert
```

---

# 53. Purple Team Feedback

Suppose:

```text
Technique executed
```

but:

```text
No alert
```

Possible causes:

```text
No telemetry
Parser issue
Detection gap
Wrong field
Threshold too high
Rule disabled
```

This produces actionable engineering work.

---

# 54. ATT&CK and Incident Response

During an incident, map observed behavior:

```text
Observed Event
      ↓
Technique
      ↓
Tactic
      ↓
Attack Path
```

This helps responders understand:

```text
What happened?
Where are we in the attack?
What might happen next?
```

---

# 55. Predictive Use

If an attacker has performed:

```text
Credential Access
```

responders may investigate for:

```text
Lateral Movement
Persistence
Discovery
```

ATT&CK helps generate investigation hypotheses.

It does not predict attacker actions with certainty.

---

# 56. ATT&CK and SIEM Dashboards

A SOC dashboard can show:

```text
Alerts by Tactic

Execution:
20

Credential Access:
12

Lateral Movement:
8

C2:
5
```

This provides a behavioral view of the environment.

---

# 57. Detection Coverage Dashboard

Example:

```text
ATT&CK Coverage

Strong:
62%

Partial:
21%

Weak:
17%
```

These percentages are organization-specific and should be based on clearly defined methodology.

---

# 58. Technique-Based Alert Search

Analysts can search:

```text
attack.technique.id = "Txxxx"
```

or use normalized metadata such as:

```text
threat.technique.name
```

Exact fields vary by SIEM.

---

# 59. Detection Metadata Example

```yaml
id: DET-ENDPOINT-004

name: Suspicious PowerShell Execution

severity: high

tactic:
  - execution

technique:
  - command-and-scripting-interpreter

subtechnique:
  - powershell

data_sources:
  - endpoint
  - process_creation
  - powershell_logs
```

---

# 60. ATT&CK Mapping in Alerts

A useful alert can display:

```text
Tactic:
Execution

Technique:
Command and Scripting Interpreter

Sub-Technique:
PowerShell
```

This gives analysts immediate behavioral context.

---

# 61. ATT&CK and Threat Intelligence

Threat intelligence may provide:

```text
Threat Actor
+
Malware
+
Technique
```

Example:

```text
Malware Family
    ↓
Uses PowerShell
    ↓
Execution
```

This can guide detection development.

---

# 62. Threat-Informed Detection Pipeline

```text
Threat Report
      ↓
Adversary Behavior
      ↓
ATT&CK Technique
      ↓
Telemetry Mapping
      ↓
Detection Hypothesis
      ↓
Query
      ↓
Testing
      ↓
Production Rule
```

---

# 63. ATT&CK and Data Sources

Each technique may require different telemetry.

Example:

```text
PowerShell
→ Process + PowerShell Logs

Credential Dumping
→ EDR + Process Access

Network Discovery
→ Endpoint + Network

Cloud Account Abuse
→ Cloud Identity Logs
```

---

# 64. Data Source Prioritization

When a technique is important but telemetry is missing:

```text
Technique
 ↓
Required Data Source
 ↓
Logging Requirement
 ↓
Collection
 ↓
Normalization
 ↓
Detection
```

ATT&CK therefore supports not only detection engineering but also logging strategy.

---

# 65. Logging Strategy

Security teams should ask:

```text
Which ATT&CK behaviors matter most?

What telemetry observes them?

Are those logs collected?

Are they retained?

Are they searchable?

Are detections built?
```

---

# 66. ATT&CK Coverage Maturity

A mature SOC progresses:

```text
No ATT&CK Mapping
      ↓
Manual Mapping
      ↓
Detection Mapping
      ↓
Coverage Tracking
      ↓
Threat-Informed Engineering
      ↓
Continuous Validation
```

---

# 67. Common ATT&CK Mistakes

```text
1. Mapping every alert to ATT&CK.

2. Treating technique coverage as proof of security.

3. Ignoring telemetry quality.

4. Mapping based only on tool names.

5. Using outdated technique IDs.

6. Ignoring sub-techniques.

7. Creating detections only for easy techniques.

8. Measuring quantity instead of quality.

9. Ignoring false positives.

10. Never validating detections.
```

---

# 68. Technique Mapping Mistake

Bad:

```text
"PowerShell detected"

Therefore:

"Attacker detected"
```

Incorrect.

PowerShell is legitimate and widely used.

Better:

```text
PowerShell
+
Suspicious Arguments
+
Unusual Parent
+
External Connection
```

This provides stronger evidence.

---

# 69. Tool vs Technique

A tool is not automatically a technique.

Example:

```text
PowerShell
```

is a technology/interpreter.

The ATT&CK mapping concerns:

```text
How an adversary uses it
```

Similarly:

```text
PsExec
```

can be used legitimately or maliciously.

Detection should focus on behavior and context.

---

# 70. ATT&CK and False Positives

Many ATT&CK behaviors are dual-use.

Examples:

```text
PowerShell
Remote Services
Scheduled Tasks
Administrative Tools
Cloud APIs
```

Therefore:

```text
ATT&CK mapping
≠
Maliciousness
```

---

# 71. ATT&CK and Risk

A technique alone does not determine risk.

Risk depends on:

```text
Technique
+
User
+
Asset
+
Context
+
Threat Intelligence
+
Sequence
```

---

# 72. ATT&CK + Correlation

Example:

```text
PowerShell
   +
Credential Access
   +
Remote Authentication
   +
New Host
```

Map:

```text
Execution
+
Credential Access
+
Lateral Movement
```

This may represent a much higher-confidence attack chain than any single detection.

---

# 73. ATT&CK + Risk Scoring

Example:

```text
Execution              +20
Credential Access      +40
Lateral Movement       +50
Critical Server        +30
```

Total:

```text
140
```

The organization can prioritize the associated investigation.

---

# 74. ATT&CK + Alert Enrichment

Alert:

```text
Suspicious PowerShell
```

Add:

```text
Tactic:
Execution

Technique:
Command and Scripting Interpreter

Sub-Technique:
PowerShell

Related Alerts:
Credential Access
Network Connection

Risk:
85
```

This significantly improves triage context.

---

# 75. ATT&CK + Threat Hunting Workflow

```text
Select Technique
      ↓
Understand Behavior
      ↓
Identify Telemetry
      ↓
Build Query
      ↓
Search Historical Data
      ↓
Pivot
      ↓
Validate
      ↓
Create Detection
```

---

# 76. Practical Lab – ATT&CK Detection

Choose:

```text
PowerShell
```

Identify:

```text
Tactic:
Execution

Technique:
Command and Scripting Interpreter

Sub-Technique:
PowerShell
```

Then determine:

```text
Required Logs
Required Fields
Detection Logic
False Positives
Test Activity
```

---

# 77. Practical Lab – Coverage Matrix

Create:

```text
Technique
Telemetry
Detection
Severity
Status
Owner
```

Example:

```text
PowerShell
Process Logs
Yes
Medium
Covered

Credential Dumping
EDR
Partial
High
Partial

Cloud Account Abuse
Cloud Identity
No
High
Gap
```

---

# 78. Practical Lab – Threat Hunt

Hypothesis:

> An attacker may be using PowerShell for suspicious execution.

Search:

```text
PowerShell Events
```

Pivot:

```text
User
Host
Parent Process
Command Line
Network
```

Then identify:

```text
Rare
Suspicious
Privileged
External
```

activity.

---

# 79. Practical Lab – Attack Chain

Create controlled events representing:

```text
Initial Access
      ↓
Execution
      ↓
Discovery
      ↓
Lateral Movement
```

Map each event to:

```text
Tactic
Technique
Detection
```

Then determine:

```text
Which stage was detected?
Which stage was missed?
What telemetry was missing?
```

Only conduct simulated or emulated activity in systems where you have explicit authorization.

---

# 80. Interview Questions

### What is MITRE ATT&CK?

> A knowledge base of adversary tactics and techniques based on observed real-world behavior, commonly used for detection engineering, hunting, incident response, and security assessment.

### What is a tactic?

> The adversary's objective or goal, such as execution, credential access, or lateral movement.

### What is a technique?

> A method used by an adversary to achieve a tactical objective.

### What is a sub-technique?

> A more specific implementation or variation of a broader technique.

### Why is ATT&CK useful for SOC teams?

> It provides a common language for describing attacker behavior and helps organize detection, hunting, coverage, and threat-informed security engineering.

### What is ATT&CK-based detection?

> Detection engineering that uses known adversary behaviors and ATT&CK techniques to identify relevant activity in available telemetry.

### What is detection coverage?

> The extent to which relevant attacker behaviors or techniques can be identified by the organization's telemetry and detections.

### What is a visibility gap?

> A situation where required telemetry for observing a behavior is unavailable or insufficient.

### What is a detection gap?

> A situation where useful telemetry exists but the organization lacks an effective detection for the relevant behavior.

### Does ATT&CK technique mapping mean an event is malicious?

> No. Many techniques involve legitimate administrative tools and behaviors, so context and detection logic are required.

### How would you create an ATT&CK-based detection?

> Identify the threat behavior, map it to the relevant technique, determine required telemetry, validate available fields, build and test detection logic, map the resulting alert to ATT&CK metadata, and continuously tune it.

### How can ATT&CK support threat hunting?

> Analysts can select techniques, formulate behavior-based hypotheses, identify relevant telemetry, search historical data, pivot across entities, and use findings to create or improve detections.

### How can ATT&CK support purple teaming?

> It provides a common framework for selecting adversary behaviors to emulate and validating whether telemetry and detections identify those behaviors.

### Why isn't 100% ATT&CK coverage automatically good security?

> Coverage measurements can ignore detection quality, telemetry reliability, false positives, technique variations, latency, and business relevance.

---

# 81. Quick Revision

```text
MITRE ATT&CK
→ Adversary behavior knowledge base

TACTIC
→ Why

TECHNIQUE
→ How

SUB-TECHNIQUE
→ More specific how

TELEMETRY
→ What can observe the behavior

DETECTION
→ How we identify it

COVERAGE
→ What we can detect

VISIBILITY GAP
→ Missing telemetry

DETECTION GAP
→ Telemetry exists but detection is insufficient

THREAT HUNT
→ Proactively investigate behavior

PURPLE TEAM
→ Validate offensive behavior against defensive detection

ATT&CK MAPPING
→ Common behavioral language
```

---

# 82. Golden Rules

```text
1. ATT&CK describes behavior, not automatic maliciousness.

2. Tactics describe objectives.

3. Techniques describe methods.

4. Sub-techniques provide additional specificity.

5. Map detections based on actual behavior.

6. Do not map techniques simply because a tool appears in an event.

7. Determine telemetry requirements before building detections.

8. Separate visibility gaps from detection gaps.

9. Measure detection quality, not only technique count.

10. Use ATT&CK to guide threat hunting.

11. Use ATT&CK to structure detection engineering.

12. Use ATT&CK to support purple-team validation.

13. Keep technique identifiers and mappings current.

14. Combine ATT&CK with context, threat intelligence, and risk.

15. One technique may have many detections.

16. One detection may involve multiple techniques.

17. ATT&CK coverage does not equal complete security coverage.

18. Validate detections against realistic behavior.

19. Review mappings as detections evolve.

20. Use ATT&CK as a framework for thinking about attacker behavior—not as a checklist to complete mechanically.
```

---

# 83. Final Mental Model

Think of ATT&CK-based detection as:

```text
THREAT ACTOR
     ↓
OBJECTIVE
     ↓
TACTIC
     ↓
TECHNIQUE
     ↓
BEHAVIOR
     ↓
TELEMETRY
     ↓
DETECTION
     ↓
CORRELATION
     ↓
RISK
     ↓
ALERT
     ↓
INVESTIGATION
     ↓
RESPONSE
```

For detection engineering:

```text
ATT&CK TECHNIQUE
       ↓
What behavior does it represent?
       ↓
What telemetry shows it?
       ↓
What fields are required?
       ↓
What legitimate activity looks similar?
       ↓
What query detects it?
       ↓
How do we test it?
       ↓
How do we measure coverage?
```

---

# 84. Chapter Summary

MITRE ATT&CK provides a structured way to think about adversary behavior.

The most important relationship is:

```text
TACTIC
  ↓
TECHNIQUE
  ↓
BEHAVIOR
  ↓
TELEMETRY
  ↓
DETECTION
```

A mature SOC uses ATT&CK to connect:

```text
Threat Intelligence
       +
Detection Engineering
       +
Threat Hunting
       +
Incident Response
       +
Purple Teaming
       +
Security Monitoring
```

The key principle is:

> **Do not build detections merely because a technique exists in ATT&CK. Build detections because the technique represents a relevant threat to your environment and you have—or can obtain—the telemetry needed to detect meaningful instances of that behavior.**

The next chapter moves from threat modeling and detection coverage into active investigation:

```text
Chapter 10 – Security Investigations, Hunting & Triage
```

There we will cover **SOC triage methodology, investigation workflows, alert validation, evidence collection, entity pivoting, timelines, threat hunting, hypothesis-driven hunting, IOC/IOA hunting, scope analysis, root-cause analysis, escalation, and practical investigation scenarios.**