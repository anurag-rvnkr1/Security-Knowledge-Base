# Chapter 06 – Behavioral Detection & TTP-Based Detection

> Behavioral detection identifies suspicious activity based on how users, systems, applications, and adversaries behave rather than relying exclusively on known indicators. TTP-based detection focuses specifically on adversary Tactics, Techniques, and Procedures, making it more resilient against changing malware, infrastructure, and indicators.

---

# 1. What Is Behavioral Detection?

Behavioral detection identifies activity that is suspicious because of **what happened, how it happened, or the context in which it happened**.

Instead of asking:

```text
Is this IP malicious?
```

behavioral detection asks:

```text
What is this system/user/process doing?
Is that behavior expected?
Does the behavior resemble an attack?
```

Conceptually:

```text
Activity
   ↓
Behavior
   ↓
Context
   ↓
Detection Logic
   ↓
Alert
```

---

# 2. Why Behavioral Detection Matters

Attackers can change:

```text
IP Addresses
Domains
File Hashes
Filenames
Malware Samples
Payloads
```

But their objectives and techniques often remain recognizable.

Example:

```text
Attacker
   ↓
Credential Access
   ↓
Privilege Escalation
   ↓
Lateral Movement
```

The specific tools may change, but the underlying behavior can remain similar.

---

# 3. Indicator-Based vs Behavioral Detection

### Indicator-Based

```text
Known Malicious IP
Known Hash
Known Domain
```

### Behavioral

```text
Unusual Process
+
Suspicious Parent
+
Unexpected Privilege
+
External Connection
```

The second approach does not require the exact attacker infrastructure to be known beforehand.

---

# 4. What Is TTP?

TTP stands for:

```text
Tactics
Techniques
Procedures
```

These describe adversary behavior at different levels.

```text
Tactic
  ↓
Technique
  ↓
Procedure
```

---

# 5. Tactics

A **tactic** represents the attacker's objective.

Examples:

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

---

# 6. Techniques

A technique describes how an attacker achieves a tactical objective.

Example:

```text
Tactic:
Execution

Technique:
Command and Scripting Interpreter
```

The technique provides more specific behavioral detail.

---

# 7. Procedures

A procedure describes how a real adversary implements a technique.

Example:

```text
Technique:
Command and Scripting Interpreter

Procedure:
Use a scripting interpreter to execute
malicious commands.
```

Different threat actors may use different procedures for the same technique.

---

# 8. TTP Detection

TTP detection focuses on:

```text
What the attacker is trying to achieve
        +
How the attacker performs it
```

rather than only:

```text
What exact artifact did they use?
```

---

# 9. MITRE ATT&CK

:contentReference[oaicite:0]{index=0} ATT&CK is a knowledge base describing adversary tactics and techniques.

It can help detection engineers:

```text
Understand Threat Behavior
Identify Required Telemetry
Design Detections
Measure Coverage
Plan Threat Hunts
Validate Detections
```

---

# 10. TTP-Based Detection Workflow

```text
Threat
   ↓
Tactic
   ↓
Technique
   ↓
Observable Behavior
   ↓
Required Telemetry
   ↓
Detection
   ↓
Test
   ↓
Coverage
```

---

# 11. Behavior as a Detection Primitive

Instead of:

```text
Hash = X
```

use:

```text
Process A
launches
Process B
with
Suspicious Argument
from
Unexpected Parent
under
Unexpected User
```

This describes behavior rather than a single indicator.

---

# 12. Process Behavior

Important process relationships:

```text
Parent
Child
Grandparent
User
Command Line
Path
Signer
Hash
Network Activity
```

Example:

```text
Office Application
      ↓
Script Interpreter
      ↓
Network Connection
```

This chain can be more informative than the presence of a script interpreter alone.

---

# 13. Parent-Child Behavior

Example:

```text
winword.exe
    ↓
powershell.exe
```

This may deserve investigation depending on the environment.

Additional context:

```text
Command Line
User
Document
Network
Destination
```

can increase confidence.

---

# 14. Process Tree

A process tree:

```text
explorer.exe
    └── winword.exe
          └── powershell.exe
                └── unknown.exe
```

allows analysts to understand:

```text
Where execution originated
How processes were chained
What happened afterward
```

---

# 15. Command-Line Behavior

Behavioral detection can examine:

```text
Arguments
Encoding
URLs
File Paths
Script Names
Administrative Commands
```

Example:

```text
powershell.exe
+
encoded command
+
external network
```

can be more suspicious than:

```text
powershell.exe
```

alone.

---

# 16. Parent Process Anomaly

A process may be legitimate but launched from an unusual parent.

Example:

```text
Expected:

explorer.exe
   ↓
powershell.exe
```

Potentially unusual:

```text
document-reader.exe
   ↓
powershell.exe
```

This should be validated against legitimate application behavior before alerting.

---

# 17. Process Path Behavior

Potentially suspicious:

```text
Executable
+
Unexpected Temporary Directory
```

Example:

```text
C:\Users\...\Temp\unknown.exe
```

But path alone should not determine maliciousness.

Use:

```text
Path
+
Signer
+
Hash
+
Parent
+
User
+
Behavior
```

---

# 18. Living-off-the-Land Behavior

Attackers may use legitimate system utilities.

Examples include:

```text
PowerShell
WMI
Command Shell
SSH
Python
Cloud APIs
System Utilities
```

This makes:

```text
Known Malware Detection
```

less sufficient.

Behavioral detection becomes important.

---

# 19. LOLBins

**Living-off-the-Land Binaries** are legitimate tools that can be abused by attackers.

Detection should generally focus on:

```text
Tool
+
Context
+
Arguments
+
Parent
+
User
+
Destination
```

rather than simply:

```text
Tool Executed
```

---

# 20. Authentication Behavior

Behavioral identity detections may examine:

```text
Login Time
Location
Device
Source IP
Application
MFA
Authentication Method
Frequency
```

---

# 21. Login Anomaly

Normal:

```text
User
Office Device
Office Hours
Known Location
```

Observed:

```text
New Device
Unusual Time
Unusual Location
```

Potential:

```text
Account Compromise
```

But legitimate travel and VPN usage must be considered.

---

# 22. Authentication Sequence

A stronger detection:

```text
Multiple Failed Logins
       ↓
Successful Login
       ↓
New Device
       ↓
MFA Modification
```

This is more meaningful than:

```text
One Failed Login
```

---

# 23. Privilege Escalation Behavior

Look for:

```text
Role Change
Admin Group Membership
Privilege Assignment
sudo
IAM Policy Change
Service Account Abuse
```

Example:

```text
Normal User
     ↓
Admin Role
     ↓
Sensitive Resource Access
```

---

# 24. Persistence Behavior

Potential persistence behaviors:

```text
New Scheduled Task
New Service
Startup Modification
Registry Persistence
New Account
Cloud Access Key
OAuth Application
```

The exact detection should focus on:

```text
Who
What
When
Where
Why
```

---

# 25. Defense Evasion Behavior

Examples:

```text
Security Tool Modification
Log Clearing
Process Termination
Configuration Changes
File Deletion
Timestamp Manipulation
```

Detection should distinguish:

```text
Authorized Administrative Activity
```

from:

```text
Suspicious Security Control Manipulation
```

---

# 26. Discovery Behavior

Attackers often perform discovery before lateral movement.

Examples:

```text
Account Discovery
System Discovery
Network Discovery
Process Discovery
Service Discovery
Cloud Resource Discovery
```

A sequence of discovery actions can provide behavioral evidence.

---

# 27. Discovery Burst

Example:

```text
Host Information
+
User Enumeration
+
Network Enumeration
+
Service Enumeration
```

within a short period:

```text
Potential Reconnaissance
```

---

# 28. Lateral Movement Behavior

Potential signals:

```text
Unusual Remote Login
Remote Service Usage
New Host Access
Administrative Authentication
Remote Execution
```

Context:

```text
Source Host
Destination Host
User
Privilege
Time
Historical Relationship
```

is important.

---

# 29. Lateral Movement Example

Normal:

```text
Admin Workstation
   ↓
Server Cluster
```

Potentially unusual:

```text
Developer Laptop
   ↓
Domain Controller
```

The relationship itself may be meaningful.

---

# 30. Network Behavior

Behavioral network detection may consider:

```text
Connection Frequency
Destination Rarity
Port
Protocol
Bytes
Direction
Timing
Beaconing
```

---

# 31. Beaconing Behavior

C2 communication can exhibit periodic patterns.

Example:

```text
10:00
10:05
10:10
10:15
10:20
```

Potential:

```text
Periodic Outbound Connection
```

Combine with:

```text
Rare Destination
+
Unusual Process
```

for stronger detection.

---

# 32. Rare Destination

A destination contacted by:

```text
1 Host
```

may be more interesting than:

```text
Destination contacted by 10,000 hosts
```

But rarity alone is not maliciousness.

---

# 33. Domain Rarity

Potential signals:

```text
Rare Domain
+
New Domain
+
Suspicious Process
+
Periodic Requests
```

can identify potential C2.

---

# 34. DNS Behavioral Detection

Potential characteristics:

```text
High Query Frequency
Long Query Names
Unusual Entropy
Rare Domains
Periodic Queries
Large Number of Subdomains
```

These should be combined carefully because legitimate applications can exhibit similar patterns.

---

# 35. Data Transfer Behavior

Potential exfiltration indicators:

```text
Large Transfer
+
Sensitive Data
+
External Destination
+
Unusual Time
```

A large transfer alone is not sufficient because backups and legitimate data workflows may also be large.

---

# 36. File Behavior

Potential suspicious behaviors:

```text
Mass File Modification
Mass Rename
Mass Encryption-Like Changes
Unexpected Archive Creation
Sensitive File Access
```

---

# 37. Ransomware Behavior

Conceptual sequence:

```text
Suspicious Process
      ↓
Mass File Changes
      ↓
File Extensions Change
      ↓
Backup / Recovery Tampering
```

This behavioral approach can detect ransomware variants without relying solely on known hashes.

---

# 38. Cloud Behavioral Detection

Cloud activity can be evaluated using:

```text
Principal
API Action
Resource
Region
Source IP
User Agent
Time
Historical Behavior
```

---

# 39. Cloud Anomaly Example

Normal:

```text
User
Region: India
Resource: Standard
```

Observed:

```text
New Region
+
New Device
+
Privilege Change
+
Sensitive API Calls
```

Potential:

```text
Cloud Account Compromise
```

---

# 40. Application Behavior

Web applications can be monitored for:

```text
Request Patterns
Authentication
API Usage
Privilege Changes
Resource Access
Error Rates
```

---

# 41. Web Attack Behavior

Potential sequence:

```text
Repeated Invalid Requests
        ↓
Endpoint Enumeration
        ↓
Suspicious Parameter Patterns
        ↓
Successful Authentication
        ↓
Sensitive Resource Access
```

This may indicate an attack chain.

---

# 42. Sequence-Based Behavioral Detection

A behavioral sequence may be:

```text
A
 ↓
B
 ↓
C
```

Example:

```text
Phishing Email
 ↓
Process Execution
 ↓
C2 Connection
```

---

# 43. State Machines

Complex behavioral detections can be modeled as states.

Example:

```text
[Normal]
   ↓
[Suspicious Login]
   ↓
[New Device]
   ↓
[MFA Change]
   ↓
[Privilege Change]
   ↓
[High Risk]
```

Each transition represents new evidence.

---

# 44. Behavioral Baselines

A baseline can be created for:

```text
User
Host
Application
Network
Cloud Account
Service
```

Examples:

```text
Normal Login Locations
Normal Processes
Normal Destinations
Normal Data Volume
Normal Access Patterns
```

---

# 45. User Behavioral Baseline

Example:

```text
User:
Alice

Typical:
09:00–18:00
Laptop-A
Office Network
Finance Applications
```

Observed:

```text
03:00
New Device
New Country
Cloud Admin API
```

Behavioral risk increases.

---

# 46. Host Behavioral Baseline

Example:

```text
Server A
Normally:
Web Server
Port 443
Application Process
Database Connection
```

Observed:

```text
New Shell
New Administrative Tool
Outbound Connection
```

Potential anomaly.

---

# 47. Application Baseline

Example:

```text
Application A
Normally:
1000 API calls/hour
```

Observed:

```text
50,000 API calls/hour
```

Potential:

```text
Abuse
Automation
Attack
```

---

# 48. Behavioral Detection and Context

Context sources:

```text
Identity
Asset
Threat Intelligence
Historical Activity
Business Hours
Location
Privilege
Vulnerability
Application
```

The same behavior can have different meanings depending on context.

---

# 49. Contextual Example

Event:

```text
PowerShell Execution
```

### Developer Machine

Could be:

```text
Normal Development
```

### Domain Controller

Could be:

```text
Higher Risk
```

### Critical Server + Suspicious Parent

Potentially:

```text
High Priority
```

---

# 50. Behavioral Detection and Asset Criticality

Risk can be influenced by:

```text
Criticality
Data Sensitivity
Business Function
Exposure
```

Example:

```text
Behavior:
Suspicious Process

Host A:
Test VM

Host B:
Domain Controller
```

The second event deserves greater attention.

---

# 51. Behavioral Detection and User Privilege

Example:

```text
Privilege:
Standard User
```

versus:

```text
Privilege:
Domain Administrator
```

The same behavior can have very different impact.

---

# 52. Behavioral Detection and Threat Intelligence

Combine:

```text
Behavior
+
Threat Intelligence
```

Example:

```text
Rare Destination
+
Known Malicious Domain
```

This provides stronger confidence than either alone.

---

# 53. Behavioral Detection and Vulnerability Context

Example:

```text
Server Vulnerable to Exploit
+
Suspicious Process
+
External Connection
```

Potential risk is significantly higher than:

```text
Suspicious Process
```

alone.

---

# 54. Behavioral Detection and Attack Chains

An attacker may generate multiple behaviors:

```text
Initial Access
 ↓
Execution
 ↓
Persistence
 ↓
Credential Access
 ↓
Discovery
 ↓
Lateral Movement
```

Each stage can feed a larger detection model.

---

# 55. Attack Chain Detection

Example:

```text
Phishing
   ↓
Office Process
   ↓
PowerShell
   ↓
Credential Access
   ↓
Remote Login
```

Instead of five independent alerts:

```text
Potential Compromise Chain
```

can be created.

---

# 56. Behavioral Detection Advantages

```text
Resilient to IOC Changes
Detects Unknown Variants
Focuses on TTPs
Can Detect Living-off-the-Land
Supports Attack Chain Detection
```

---

# 57. Behavioral Detection Limitations

```text
Complexity
False Positives
Telemetry Dependency
Baseline Challenges
Performance Cost
Environmental Differences
```

---

# 58. Behavioral Detection vs Anomaly Detection

These are related but different.

### Behavioral Detection

Looks for known suspicious patterns.

```text
Office
→ PowerShell
→ External Connection
```

### Anomaly Detection

Looks for deviation from normal.

```text
User normally:
5 API calls/day

Observed:
500 API calls
```

---

# 59. Behavioral + Anomaly

Combining both can improve confidence.

Example:

```text
Unusual PowerShell
+
Rare on Host
+
New External Destination
```

Potential:

```text
High-Risk Behavior
```

---

# 60. TTP Detection vs Tool Detection

Tool-focused:

```text
Detect Tool X
```

TTP-focused:

```text
Detect Technique X
```

The second can detect:

```text
Tool A
Tool B
Tool C
```

if they perform the same relevant behavior.

---

# 61. Tool Agnostic Detection

Good TTP detection attempts to avoid unnecessary dependency on a specific tool.

Example:

Instead of:

```text
Detect ToolName.exe
```

consider:

```text
Detect Suspicious Credential Access Behavior
```

when the telemetry supports it.

---

# 62. ATT&CK Mapping

A detection should ideally map to:

```text
Tactic
Technique
Sub-Technique
```

where appropriate.

Example:

```text
Detection:
Suspicious PowerShell

ATT&CK:
Command and Scripting Interpreter
```

Exact mappings should be validated against the current ATT&CK knowledge base.

---

# 63. ATT&CK Coverage

Create a matrix:

| Technique | Telemetry | Detection | Test | Coverage |
|---|---|---|---|---|
| Technique A | Yes | Yes | Yes | High |
| Technique B | Yes | Partial | Yes | Medium |
| Technique C | No | No | No | Gap |

This helps identify weaknesses.

---

# 64. Detection Coverage Is Not ATT&CK Checkbox Counting

Avoid:

```text
Technique = Covered
```

simply because:

```text
One Rule Exists
```

Real coverage should consider:

```text
Telemetry
+
Technique Variants
+
Detection Quality
+
Testing
+
Environment
```

---

# 65. Procedure-Level Detection

A mature approach considers:

```text
Technique
   ↓
Known Procedures
   ↓
Observed Variations
   ↓
Detection Coverage
```

This helps avoid overly generic rules.

---

# 66. Threat Actor Behavior

Threat actors may have recurring:

```text
Tools
Techniques
Infrastructure
Targeting
Timing
Operational Patterns
```

These can inform behavioral detection.

---

# 67. Threat-Informed Behavioral Detection

Example:

```text
Threat Actor
    ↓
Known TTP
    ↓
Expected Telemetry
    ↓
Detection
    ↓
Simulation
    ↓
Coverage
```

---

# 68. Behavioral Detection Testing

Test:

```text
Malicious Behavior
Normal Behavior
Edge Cases
Alternative Tools
Different Users
Different Hosts
Missing Telemetry
```

---

# 69. Positive Behavioral Test

Example:

```text
Simulated Suspicious Process Chain
```

Expected:

```text
Detection Fires
```

---

# 70. Negative Behavioral Test

Example:

```text
Legitimate Administrative Script
```

Expected:

```text
No Alert
```

or:

```text
Low-Risk Signal
```

depending on design.

---

# 71. Evasion Testing

Test whether changing:

```text
Filename
IP
Domain
Command Syntax
Tool
User
```

still triggers behavior-based detection.

Goal:

```text
Detect Underlying Behavior
```

rather than only one implementation.

---

# 72. Behavioral Detection Tuning

Tune:

```text
Threshold
Context
Baseline
Correlation
Exceptions
Risk
```

Do not immediately suppress the entire behavior.

---

# 73. False Positives

Common sources:

```text
Administrative Activity
Automation
Software Deployment
Monitoring
Security Tools
Development
Testing
Backups
Scheduled Jobs
```

---

# 74. Contextual Exclusions

Instead of:

```text
Ignore PowerShell
```

use:

```text
Ignore known deployment server
+
specific process
+
expected execution context
```

when justified.

---

# 75. Behavioral Detection Anti-Patterns

Avoid:

```text
Alert on Any PowerShell
```

```text
Alert on Any Admin Login
```

```text
Alert on Any New Device
```

```text
Alert on Any Rare Domain
```

These are signals, not necessarily complete detections.

---

# 76. Signal vs Detection

A signal:

```text
Rare Login
```

A detection:

```text
Rare Login
+
New Device
+
Unusual Location
+
Privileged User
```

The distinction matters.

---

# 77. Signal Stacking

Combine multiple weak signals:

```text
Signal A +10
Signal B +20
Signal C +30
```

↓

```text
Risk = 60
```

This can produce a stronger detection.

---

# 78. Behavioral Risk Model

Conceptually:

```text
Risk =
Behavior Score
+
Anomaly Score
+
Threat Intelligence
+
Asset Criticality
+
Identity Context
```

---

# 79. Behavior Frequency

Frequency can be important.

Example:

```text
1 Process Execution
```

vs:

```text
500 Process Executions
```

within a short time.

Volume can change interpretation.

---

# 80. Behavior Rarity

Rarity can provide context.

Example:

```text
Process used by:
1 of 10,000 endpoints
```

may deserve investigation.

But:

```text
Rare ≠ Malicious
```

---

# 81. First-Seen Behavior

Potential signal:

```text
First time user accesses resource
```

But first-seen behavior is common in normal business activity.

Combine with:

```text
Privilege
Sensitivity
Timing
Device
Threat Intelligence
```

---

# 82. New Behavior

Examples:

```text
New Process
New Destination
New Application
New Device
New Cloud Region
New Privilege
```

Newness is useful context but not proof of maliciousness.

---

# 83. Behavioral Drift

Normal behavior changes over time.

Examples:

```text
New Software
Remote Work
Cloud Migration
New Office
New Business Process
```

Detection baselines must adapt.

---

# 84. Baseline Poisoning

An attacker may attempt to make malicious behavior appear normal over time.

Conceptually:

```text
Normal
 ↓
Small Suspicious Changes
 ↓
Repeated
 ↓
Baseline Adapts
 ↓
Malicious Activity Appears Normal
```

Therefore baselines should be carefully designed and monitored.

---

# 85. Cold Start Problem

A new user or system may have little historical data.

Example:

```text
New Employee
New Server
New Cloud Account
```

There may be insufficient baseline information.

Use:

```text
Peer Group
Organization Baseline
Role Baseline
Asset Type
Threat Intelligence
```

where appropriate.

---

# 86. Peer Group Baselines

Instead of comparing:

```text
User A
```

only against their own history:

compare against:

```text
Users in Same Role
```

Example:

```text
Finance User
vs
Finance Users
```

This can provide better context.

---

# 87. Entity Profiling

Maintain profiles for:

```text
Users
Hosts
Applications
Services
Cloud Accounts
```

Profile attributes:

```text
Normal Locations
Normal Times
Normal Processes
Normal Destinations
Normal Resource Access
```

---

# 88. User and Entity Behavior Analytics

UEBA commonly uses:

```text
Entity Profiles
Behavior Baselines
Anomaly Detection
Risk Scoring
Correlation
```

UEBA is covered in greater depth later in this curriculum.

---

# 89. Practical Exercise – Process Behavior

Create a detection hypothesis:

```text
Office Application
+
Script Interpreter
+
External Network
```

Identify:

```text
Required Telemetry
Expected False Positives
Positive Test
Negative Test
ATT&CK Mapping
```

---

# 90. Practical Exercise – Login Behavior

Build:

```text
User Login
+
New Device
+
Unusual Location
+
Privileged Account
```

Then assign:

```text
Severity
Confidence
Risk
```

---

# 91. Practical Exercise – C2 Behavior

Look for:

```text
Rare Domain
+
Periodic Connections
+
Unusual Process
```

Test:

```text
Normal Application
Malicious Simulation
CDN
Monitoring Agent
```

---

# 92. Practical Exercise – Ransomware Behavior

Conceptually detect:

```text
Mass File Changes
+
Suspicious Process
+
Recovery Tampering
```

Then test:

```text
Backup Job
File Migration
Software Update
Ransomware Simulation
```

---

# 93. Practical Exercise – TTP Mapping

Choose:

```text
Credential Access
```

Then document:

```text
Tactic
Technique
Behavior
Telemetry
Detection
Test
Coverage
```

---

# 94. Practical Exercise – Evasion Test

Take a behavior detection.

Change:

```text
Filename
Process Name
IP
Domain
Tool
Command Formatting
```

Determine:

```text
Does Detection Still Trigger?
```

If not:

```text
Improve Behavioral Logic
```

---

# 95. Practical Exercise – Attack Chain

Build:

```text
Initial Access
 ↓
Execution
 ↓
Persistence
 ↓
Credential Access
 ↓
Lateral Movement
```

Identify:

```text
Detection at Each Stage
```

Then identify:

```text
Which stage has no telemetry?
Which stage has no detection?
```

---

# 96. Behavioral Detection Checklist

```text
[ ] Threat behavior understood
[ ] Tactic identified
[ ] Technique identified
[ ] Procedure understood
[ ] Required telemetry available
[ ] Relevant fields identified
[ ] Baseline considered
[ ] Context identified
[ ] Behavioral logic created
[ ] False positives considered
[ ] Positive test created
[ ] Negative test created
[ ] Evasion testing performed
[ ] ATT&CK mapping validated
[ ] Severity assigned
[ ] Confidence assigned
[ ] Risk considered
[ ] Owner assigned
```

---

# 97. Interview Questions

### What is behavioral detection?

> Detection based on suspicious activity patterns and context rather than relying exclusively on known indicators.

### What does TTP mean?

> Tactics, Techniques, and Procedures—the objectives, methods, and implementation details associated with adversary behavior.

### Why is TTP-based detection valuable?

> Attackers can change tools, hashes, domains, and infrastructure, while underlying techniques and objectives may remain more stable.

### What is the difference between behavior and anomaly detection?

> Behavioral detection identifies known suspicious patterns, while anomaly detection identifies deviations from expected behavior.

### What is a process tree?

> A representation of parent-child process relationships that helps analysts understand how execution occurred.

### Why is PowerShell alone a weak detection?

> PowerShell is a legitimate administrative and development tool, so its execution alone does not establish malicious behavior.

### How do you detect living-off-the-land activity?

> Focus on tool usage combined with context such as parent process, command line, user, destination, frequency, and surrounding behavior.

### What is a behavioral baseline?

> A model or representation of expected activity for an entity such as a user, host, or application.

### What is baseline poisoning?

> An attempt to influence behavioral baselines so malicious activity becomes incorporated into what the system considers normal.

### What is a cold-start problem?

> The lack of sufficient historical data to establish a reliable baseline for a new user, host, application, or account.

### How do you improve behavioral detection accuracy?

> Add contextual enrichment, correlation, entity profiling, appropriate thresholds, carefully designed exceptions, and continuous validation.

---

# 98. Quick Revision

```text
Behavioral Detection
→ Detect suspicious activity patterns

TTP
→ Tactics + Techniques + Procedures

Tactic
→ Adversary objective

Technique
→ Method used to achieve objective

Procedure
→ Specific implementation

Behavior
→ What an entity does

Baseline
→ Expected behavior

Anomaly
→ Deviation from baseline

Process Tree
→ Parent-child execution relationship

Sequence
→ Ordered behavioral events

Context
→ Additional information improving interpretation

Behavioral Resilience
→ Ability to detect activity despite IOC/tool changes

Behavioral Drift
→ Normal activity changing over time

Baseline Poisoning
→ Manipulating the baseline

Cold Start
→ Insufficient history for baseline
```

---

# 99. Golden Rules

```text
1. Focus on behavior, not only indicators.

2. Understand the adversary's objective.

3. Map behavior to relevant TTPs.

4. Identify telemetry before designing detection logic.

5. Do not alert solely because a legitimate tool was executed.

6. Add parent-child process context.

7. Consider user and asset context.

8. Use behavioral sequences when appropriate.

9. Combine multiple weak signals when useful.

10. Anomaly does not automatically mean malicious.

11. Rare behavior is a signal, not proof.

12. New behavior is a signal, not proof.

13. Baselines must account for legitimate changes.

14. Consider peer-group baselines for new entities.

15. Test behavioral detections against legitimate activity.

16. Test whether simple attacker changes evade the detection.

17. Avoid tool-specific logic when the underlying TTP is what matters.

18. Monitor telemetry dependencies.

19. Map meaningful detections to ATT&CK.

20. Measure actual coverage rather than counting rules.

21. Consider baseline poisoning.

22. Consider cold-start scenarios.

23. Combine behavior with threat intelligence where useful.

24. Use risk and context to prioritize weak signals.

25. The goal is to detect the attacker's behavior—not merely the artifact they happened to use.
```

---

# 100. Final Mental Model

Behavioral detection can be summarized as:

```text
WHAT IS HAPPENING?
        ↓
WHO IS DOING IT?
        ↓
WHERE IS IT HAPPENING?
        ↓
WHEN IS IT HAPPENING?
        ↓
WHAT HAPPENED BEFORE?
        ↓
WHAT HAPPENED AFTER?
        ↓
IS IT NORMAL?
        ↓
DOES IT RESEMBLE A KNOWN TTP?
        ↓
WHAT OTHER SIGNALS SUPPORT IT?
        ↓
WHAT IS THE RISK?
        ↓
ALERT / INVESTIGATE
```

The most resilient detection approach is:

```text
Indicator
   +
Behavior
   +
Context
   +
TTP
   +
Correlation
   +
Risk
      ↓
Actionable Detection
```

---

# 101. Chapter Summary

This chapter covered:

```text
Behavioral Detection
TTP-Based Detection
Tactics
Techniques
Procedures
MITRE ATT&CK
Process Behavior
Process Trees
Command-Line Behavior
Living-off-the-Land
Authentication Behavior
Privilege Behavior
Persistence Behavior
Discovery Behavior
Lateral Movement
Network Behavior
Beaconing
DNS Behavior
Data Transfer Behavior
Cloud Behavior
Application Behavior
Behavioral Baselines
Entity Profiling
Peer-Group Baselines
Behavioral Anomalies
Behavioral Drift
Baseline Poisoning
Cold Start
Attack Chain Detection
Behavioral Testing
Evasion Testing
```

The central principle is:

> **Attackers can change their tools and indicators, but they still need to perform actions to achieve their objectives. Detecting those actions and the relationships between them makes TTP-based behavioral detection one of the most important foundations of modern detection engineering.**

The next chapter moves into **Anomaly Detection, Baselines & Statistical Detection**, focusing on how to model normal behavior, identify deviations, handle seasonality and drift, reduce anomaly-driven false positives, and build reliable statistical detections.
```