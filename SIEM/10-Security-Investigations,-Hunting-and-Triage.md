# Chapter 10 – Security Investigations, Hunting & Triage

> Security triage determines what deserves immediate attention, investigation establishes what happened and how far it spread, and threat hunting proactively searches for malicious behavior that automated detections may have missed.

---

# 1. Introduction

A SIEM can generate thousands of events and alerts.

The SOC analyst must determine:

```text
What happened?
Is it legitimate?
Is it suspicious?
Is it malicious?
How serious is it?
What systems are affected?
What should happen next?
```

This creates three closely related activities:

```text
TRIAGE
   ↓
INVESTIGATION
   ↓
HUNTING
```

They are related but different.

---

# 2. Triage

Triage is the rapid process of determining:

```text
Priority
Validity
Severity
Scope
Next Action
```

The goal is not always to fully investigate an event immediately.

Instead:

```text
Alert
 ↓
Quick Assessment
 ↓
Prioritize
 ↓
Investigate / Escalate / Close
```

---

# 3. Investigation

Investigation goes deeper.

It attempts to establish:

```text
What happened?
When?
Who?
Where?
How?
Why?
What was affected?
What happened before?
What happened after?
```

---

# 4. Threat Hunting

Threat hunting is proactive.

Instead of:

```text
Alert
 ↓
Investigation
```

the analyst starts with:

```text
Hypothesis
 ↓
Search
 ↓
Analysis
 ↓
Evidence
```

The goal is to discover threats that may not have generated alerts.

---

# 5. Triage vs Investigation vs Hunting

| Activity | Starting Point | Goal |
|---|---|---|
| Triage | Alert | Determine priority and validity |
| Investigation | Suspicious event/alert | Establish facts and scope |
| Hunting | Hypothesis/question | Discover hidden threats |

---

# 6. Investigation Lifecycle

A practical workflow:

```text
ALERT
  ↓
VALIDATE
  ↓
UNDERSTAND
  ↓
SCOPE
  ↓
TIMELINE
  ↓
PIVOT
  ↓
CORRELATE
  ↓
ASSESS IMPACT
  ↓
DETERMINE ROOT CAUSE
  ↓
ESCALATE / RESPOND
  ↓
DOCUMENT
```

---

# 7. Step 1 – Validate the Alert

Ask:

```text
Why did it trigger?
Which detection?
Which event?
Which entities?
What conditions matched?
```

Never begin with:

```text
"This is definitely an attack."
```

Start with:

```text
"What evidence caused this alert?"
```

---

# 8. Step 2 – Understand the Detection

Review:

```text
Detection Name
Rule Logic
Threshold
Time Window
Severity
MITRE Mapping
Required Fields
Known Exceptions
```

This helps determine whether the alert is behaving as expected.

---

# 9. Step 3 – Identify Key Entities

Extract:

```text
User
Host
Source IP
Destination IP
Domain
Process
File
Application
Cloud Account
Session
```

These become investigation pivots.

---

# 10. Investigation Pivot

A pivot means:

```text
Take one known piece of evidence
and search for related activity.
```

Example:

```text
Suspicious IP
   ↓
Search all events involving IP
```

Then:

```text
User
   ↓
Search user's activity
```

Then:

```text
Host
   ↓
Search host timeline
```

---

# 11. Common Pivot Types

```text
User → Host
User → IP
Host → Process
Process → Network
IP → Domain
Domain → Hosts
Hash → Hosts
Session → Actions
Cloud Account → Resources
```

---

# 12. Investigation Starting Point

Suppose the alert says:

```text
Suspicious PowerShell
```

Extract:

```text
Host:
WS-101

User:
alice

Process:
powershell.exe

Parent:
winword.exe

Command:
...

Time:
10:14 UTC
```

These fields become your investigation starting points.

---

# 13. Timeline Analysis

A timeline arranges events chronologically.

Example:

```text
09:58  Email Received
10:02  Office Document Opened
10:03  PowerShell Started
10:04  File Created
10:05  DNS Query
10:06  External Connection
10:08  Credential Access
10:12  Remote Login
```

The timeline reveals relationships.

---

# 14. Why Timelines Matter

Individual events may appear harmless.

Timeline:

```text
Email
 ↓
Execution
 ↓
File Creation
 ↓
Network
 ↓
Credential Access
```

may reveal:

```text
Possible Compromise
```

---

# 15. Event Ordering

Always verify:

```text
What happened first?
What happened next?
What happened immediately before the alert?
What happened immediately after?
```

This can distinguish:

```text
Cause
```

from:

```text
Effect
```

---

# 16. Before-and-After Analysis

For an alert at:

```text
10:15
```

search:

```text
10:00–10:15
```

and:

```text
10:15–10:30
```

The exact window should depend on the incident.

---

# 17. Scope Analysis

Scope determines:

```text
How many users?
How many hosts?
How many accounts?
How many IPs?
How many files?
How many applications?
```

Example:

```text
1 Host
```

vs:

```text
250 Hosts
```

represent very different incidents.

---

# 18. Scope Questions

Ask:

```text
Is this isolated?

Are other hosts affected?

Are other users involved?

Did the same IP contact other systems?

Did the same hash appear elsewhere?

Did the same process execute elsewhere?
```

---

# 19. Blast Radius

Blast radius describes the extent of impact.

Example:

```text
1 workstation
```

has a smaller blast radius than:

```text
100 servers
```

Determine:

```text
Affected Assets
Affected Users
Affected Data
Affected Services
```

---

# 20. Root Cause

Root cause asks:

```text
How did this activity begin?
```

Possible causes:

```text
Phishing
Stolen Credentials
Exploited Vulnerability
Misconfiguration
Malicious Insider
Compromised Vendor
Exposed Service
```

---

# 21. Initial Access Investigation

If compromise is suspected, investigate:

```text
Email
VPN
Remote Access
Web Applications
Exposed Services
Cloud Login
Credentials
Vulnerabilities
```

---

# 22. Account Investigation

For suspicious user activity:

```text
Login History
Source IPs
Locations
Devices
MFA Events
Password Changes
Privilege Changes
Application Access
Cloud Activity
```

---

# 23. Host Investigation

For suspicious host activity:

```text
Processes
Users
Network Connections
Files
Persistence
Scheduled Tasks
Services
Security Events
DNS
```

---

# 24. Process Investigation

For suspicious process:

```text
Process Name
PID
Parent Process
Command Line
User
Executable Path
Hash
Signer
Start Time
Network Activity
Child Processes
```

---

# 25. Parent-Child Process Analysis

Example:

```text
winword.exe
     ↓
powershell.exe
     ↓
cmd.exe
     ↓
unknown.exe
```

This chain may be suspicious depending on context.

Process lineage is often more informative than a single process name.

---

# 26. Command-Line Analysis

Look for:

```text
Encoded Commands
Obfuscation
Unexpected Parameters
Download Operations
Credential Access
Script Execution
Remote Connections
```

But command-line content should always be interpreted in context.

---

# 27. Network Investigation

For suspicious communication:

```text
Source
Destination
Port
Protocol
Domain
DNS
Bytes
Frequency
Duration
Direction
Process
```

---

# 28. DNS Investigation

Search:

```text
Domain
Query Count
Hosts
Users
First Seen
Last Seen
Response
```

Look for:

```text
Rare Domains
New Domains
Suspicious Patterns
Known Malicious Domains
High Query Volume
```

---

# 29. Firewall Investigation

Review:

```text
Source IP
Destination IP
Port
Action
Bytes
Protocol
Timestamp
```

Determine:

```text
Allowed?
Blocked?
Repeated?
Outbound?
Inbound?
```

---

# 30. Proxy Investigation

Review:

```text
URL
Domain
User
Host
HTTP Method
Response Code
User-Agent
Bytes
```

Useful for:

```text
Web Attacks
C2
Malware Download
Data Exfiltration
Phishing
```

---

# 31. Cloud Investigation

For suspicious cloud activity:

```text
User
Source IP
Device
API Call
Resource
Role
Authentication
MFA
Location
Session
```

Examples:

```text
New Access Key
Role Assumption
Privilege Change
Unusual API Calls
Cloud Storage Access
```

---

# 32. Identity Investigation

Identity logs can reveal:

```text
Authentication
MFA
Password Changes
Account Creation
Group Membership
Privilege Changes
Session Creation
```

Identity is often central to modern investigations.

---

# 33. Threat Intelligence Pivot

Suppose:

```text
Suspicious IP
```

Search intelligence for:

```text
Reputation
Malware
Campaign
Threat Actor
First Seen
Last Seen
Confidence
Related Domains
```

---

# 34. IOC Pivot

If you discover:

```text
Malware Hash
```

search:

```text
All endpoints
Email
File Events
Sandbox
Threat Intelligence
```

Determine:

```text
How many systems?
First seen?
Last seen?
Execution?
```

---

# 35. Related Alert Search

Search for:

```text
Same User
Same Host
Same IP
Same Process
Same Domain
Same Hash
```

This may reveal:

```text
Earlier alerts
Related activity
Duplicate alerts
Attack progression
```

---

# 36. Alert Correlation

Example:

```text
Alert 1:
Suspicious Login

Alert 2:
PowerShell

Alert 3:
Credential Access

Alert 4:
Lateral Movement
```

These may represent:

```text
One Incident
```

rather than four unrelated incidents.

---

# 37. Incident Timeline

Build:

```text
Time
Event
Entity
Source
Interpretation
```

Example:

| Time | Event | Entity | Interpretation |
|---|---|---|---|
| 09:58 | Email | Alice | Initial vector |
| 10:03 | PowerShell | WS-01 | Execution |
| 10:05 | DNS | WS-01 | Possible C2 |
| 10:08 | Credential Access | WS-01 | Credential activity |
| 10:12 | Remote Login | WS-02 | Possible lateral movement |

---

# 38. Evidence Classification

Classify evidence as:

```text
Confirmed
Likely
Possible
Unknown
Benign
```

Example:

```text
Confirmed:
PowerShell executed.

Likely:
User interaction initiated it.

Possible:
Malicious payload execution.

Unknown:
Attacker objective.
```

This prevents overclaiming.

---

# 39. Hypothesis

A hypothesis is a testable explanation.

Example:

> The user's account may have been compromised and used for lateral movement.

Then identify evidence:

```text
Supporting Evidence
+
Contradicting Evidence
```

---

# 40. Hypothesis-Driven Investigation

Workflow:

```text
Question
 ↓
Hypothesis
 ↓
Required Evidence
 ↓
Search
 ↓
Result
 ↓
Update Hypothesis
```

This prevents random searching.

---

# 41. Example Hypothesis

Hypothesis:

```text
The endpoint is communicating with C2.
```

Evidence to search:

```text
Repeated outbound connections
Rare destination
Periodic timing
Suspicious process
DNS behavior
Threat intelligence
```

---

# 42. Threat Hunting

Threat hunting starts with:

```text
"Could this threat be present
without triggering our detections?"
```

---

# 43. Hunting vs Alert Investigation

### Alert Investigation

```text
Known Signal
 ↓
Investigate
```

### Threat Hunting

```text
Hypothesis
 ↓
Search
 ↓
Discover
```

---

# 44. Hunt Hypothesis Examples

```text
Attackers may be using compromised
accounts outside normal working hours.

Attackers may be using PowerShell
for suspicious execution.

A compromised endpoint may be
communicating with rare domains.

Attackers may be performing
network discovery.

Sensitive files may be accessed
before large outbound transfers.
```

---

# 45. Hunt Types

Common approaches:

```text
IOC Hunting
IOA Hunting
Behavioral Hunting
Threat-Actor Hunting
Technique-Based Hunting
Anomaly Hunting
Hypothesis-Driven Hunting
```

---

# 46. IOC Hunting

Search known:

```text
IP
Domain
Hash
URL
Email
```

Example:

```text
New malicious domain
      ↓
Search DNS
      ↓
Find affected hosts
```

---

# 47. IOA Hunting

Search behaviors:

```text
Credential Dumping
Suspicious PowerShell
Remote Execution
Network Discovery
Privilege Escalation
```

This can detect unknown infrastructure.

---

# 48. Behavioral Hunting

Instead of:

```text
Known Malware Hash
```

search:

```text
Rare executable
+
Unsigned
+
External connection
+
Privileged execution
```

---

# 49. Anomaly Hunting

Search:

```text
Rare Users
Rare Processes
Rare Domains
Rare Destinations
Unusual Login Times
Unusual Data Transfers
```

Anomaly does not equal maliciousness.

It is a hunting signal.

---

# 50. Threat Actor Hunting

If intelligence indicates:

```text
Actor commonly uses:
PowerShell
Remote Services
Credential Theft
```

hunt for:

```text
Those behaviors
```

across relevant systems.

---

# 51. Technique-Based Hunting

Example:

```text
ATT&CK Technique:
Network Discovery
```

Question:

```text
Are endpoints performing
unusual network enumeration?
```

Search:

```text
Process
Command Line
Network
Endpoint
```

---

# 52. Hunt → Detection

A successful hunt may reveal:

```text
New Pattern
```

Then:

```text
Pattern
 ↓
Detection
 ↓
Testing
 ↓
Production
```

Threat hunting therefore improves detection engineering.

---

# 53. Hunt → Incident

A hunt may discover:

```text
Previously Unknown Compromise
```

Then:

```text
Hunt Finding
 ↓
Validation
 ↓
Incident
 ↓
Scope
 ↓
Response
```

---

# 54. Triage Priority

A practical priority model:

```text
Critical
High
Medium
Low
Informational
```

Consider:

```text
Impact
Confidence
Asset Criticality
User Privilege
Threat Intelligence
Scope
Attack Stage
```

---

# 55. High-Priority Alert Example

```text
Privileged Account
+
Known Malicious IP
+
Critical Server
+
Successful Authentication
+
Suspicious Process
```

This should generally receive significant attention.

---

# 56. Low-Priority Alert Example

```text
Single failed login
+
Known user
+
Normal device
+
No other suspicious activity
```

Likely lower priority.

---

# 57. Triage Decision Tree

```text
Alert
  ↓
Is evidence valid?
 ├── No → Close / Tune
 └── Yes
       ↓
Is activity expected?
 ├── Yes → Document / Close
 └── No
       ↓
Is there evidence of compromise?
 ├── No → Monitor / Investigate
 └── Yes
       ↓
Determine Scope
       ↓
Escalate / Respond
```

---

# 58. False Positive Investigation

Do not simply mark:

```text
False Positive
```

Ask:

```text
Why did it trigger?

What legitimate process caused it?

Can this pattern happen again?

Should the detection be tuned?

Should an exception be created?

```

---

# 59. True Positive Investigation

A true positive means the alert represents genuine suspicious/malicious activity.

Next:

```text
Determine Scope
Determine Impact
Identify Root Cause
Identify Persistence
Identify Lateral Movement
Contain
Remediate
```

---

# 60. Benign True Positive

A detection can correctly identify unusual activity while the activity is legitimate.

Example:

```text
Security Scanner
```

triggering:

```text
Network Scanning Detection
```

The detection may be correct even though the activity is authorized.

This is different from a detection bug.

---

# 61. False Positive vs Benign Positive

```text
False Positive:
Detection interpreted benign activity as malicious.

Benign Positive:
Detection correctly identified the behavior,
but the behavior was authorized/legitimate.
```

Terminology can vary between organizations.

---

# 62. Investigation Questions

Always ask:

```text
WHO?
WHAT?
WHEN?
WHERE?
HOW?
WHY?
```

Then:

```text
WHAT ELSE?
WHO ELSE?
WHERE ELSE?
WHEN ELSE?
```

---

# 63. The Five Ws + H

```text
Who?
What?
When?
Where?
Why?
How?
```

This is a useful investigation framework.

---

# 64. Scope Questions

```text
How many hosts?

How many users?

How many IPs?

How many accounts?

How many processes?

How many files?

How long has this occurred?
```

---

# 65. Root-Cause Questions

```text
How did the attacker enter?

Which credential was used?

Which vulnerability was exploited?

Which user interacted with the payload?

Which system was first compromised?
```

---

# 66. Persistence Questions

```text
Were accounts created?

Were services created?

Were scheduled tasks created?

Were startup items modified?

Were credentials changed?

Were cloud keys created?
```

---

# 67. Lateral Movement Questions

```text
Did the attacker access another host?

Which credentials were used?

Which protocols?

Which source host?

Which destination hosts?

Was remote execution observed?
```

---

# 68. Collection Questions

```text
What data was accessed?

Which files?

Which databases?

Which mailboxes?

Which cloud resources?
```

---

# 69. Exfiltration Questions

```text
Was data transferred externally?

How much?

Where?

When?

Which process?

Which protocol?
```

---

# 70. Persistence and Remediation

After compromise:

```text
Remove Persistence
Reset Credentials
Revoke Sessions
Rotate Keys
Patch Vulnerabilities
Remove Malware
Rebuild Systems
Block Infrastructure
```

Exact actions depend on incident scope and organizational procedures.

---

# 71. Evidence Preservation

During investigations:

```text
Preserve Relevant Logs
Preserve Alert Details
Preserve Timestamps
Preserve Hashes
Preserve Process Information
Preserve Network Evidence
```

Avoid unnecessarily modifying compromised systems before appropriate evidence collection procedures are followed.

---

# 72. Chain of Custody

For formal investigations, evidence handling may require:

```text
Who collected it?
When?
How?
Where stored?
Who accessed it?
Was it modified?
```

The exact requirements depend on organizational and legal context.

---

# 73. Investigation Documentation

Document:

```text
Alert ID
Timestamp
Analyst
Initial Hypothesis
Evidence
Queries
Findings
Scope
Impact
Actions
Decision
Final Classification
```

---

# 74. Query Documentation

Record important queries.

Example:

```text
Purpose:
Identify all hosts contacted by suspicious IP.

Query:
...

Time Range:
24 hours

Result:
12 hosts
```

This makes investigations reproducible.

---

# 75. Investigation Notebook

A useful structure:

```text
CASE
 ├── Summary
 ├── Hypothesis
 ├── Timeline
 ├── Evidence
 ├── Queries
 ├── Entities
 ├── Findings
 ├── Scope
 ├── Impact
 ├── Actions
 └── Conclusion
```

---

# 76. Entity Relationship Analysis

Example:

```text
User Alice
    │
    ▼
Host WS01
    │
    ▼
PowerShell
    │
    ▼
Domain X
    │
    ▼
IP Y
```

This relationship chain helps identify the attack path.

---

# 77. Investigation Graph

A graph may show:

```text
          User
           │
           ▼
          Host
         /    \
        ▼      ▼
    Process    File
       │
       ▼
      IP
       │
       ▼
    Domain
```

Graphs are particularly useful for complex incidents.

---

# 78. Search Strategy

Do not start with:

```text
"Search everything."
```

Start narrow:

```text
Known Entity
```

Then expand:

```text
Entity
 ↓
Related Events
 ↓
Related Entities
 ↓
Broader Time Range
 ↓
Environment
```

---

# 79. Narrow-to-Broad Investigation

Example:

```text
Suspicious IP
   ↓
Host
   ↓
User
   ↓
Process
   ↓
Other Hosts
   ↓
Historical Activity
```

This controls investigation complexity.

---

# 80. Broad-to-Narrow Hunting

Threat hunting often works differently:

```text
Environment
   ↓
Behavior
   ↓
Rare Events
   ↓
Suspicious Entities
   ↓
Specific Host/User
```

Therefore:

```text
Investigation:
Narrow → Broad

Hunting:
Broad → Narrow
```

This is a useful conceptual distinction.

---

# 81. Search Time Ranges

Choose ranges based on the question.

Examples:

```text
Minutes:
Attack sequence

Hours:
Incident scope

Days:
Persistence

Weeks:
Long-term compromise

Months:
Historical threat hunting
```

---

# 82. Historical Retention

Investigation quality depends on:

```text
Log Retention
Data Availability
Indexing
Timestamp Accuracy
Searchability
```

If logs are deleted:

```text
Historical investigation may be impossible.
```

---

# 83. Data Source Reliability

Before trusting absence:

```text
Is the log source healthy?
```

Example:

```text
No login events
```

could mean:

```text
No logins
```

or:

```text
Identity logging stopped
```

Always distinguish the two.

---

# 84. Triage Automation

Some triage steps can be automated:

```text
IOC Lookup
Asset Lookup
User Lookup
GeoIP
Threat Intelligence
Alert Grouping
Risk Calculation
Known Benign Checks
```

This allows analysts to focus on reasoning.

---

# 85. Automated Enrichment

Example:

```text
Alert
 ↓
IP Reputation
 ↓
Asset Information
 ↓
User Information
 ↓
Previous Alerts
 ↓
MITRE Mapping
 ↓
Risk
```

---

# 86. SOAR and Investigation

SOAR can automate repetitive actions:

```text
Alert
 ↓
Enrich
 ↓
Gather Evidence
 ↓
Create Case
 ↓
Notify Analyst
```

More advanced workflows can perform approved response actions.

---

# 87. Human-in-the-Loop

Not every response should be fully automated.

Example:

```text
High-Risk Alert
      ↓
Automated Enrichment
      ↓
Analyst Review
      ↓
Approved Response
```

This reduces accidental destructive actions.

---

# 88. Investigation Quality

A good investigation is:

```text
Evidence-Based
Reproducible
Time-Aware
Contextual
Scoped
Documented
```

---

# 89. Common Investigation Mistakes

```text
1. Assuming every alert is malicious.

2. Ignoring false positives.

3. Searching without a hypothesis.

4. Looking at only one event.

5. Ignoring events before the alert.

6. Ignoring events after the alert.

7. Failing to determine scope.

8. Trusting a single IOC blindly.

9. Ignoring missing telemetry.

10. Not documenting queries.

11. Not checking related alerts.

12. Not validating timestamps.

13. Closing alerts without understanding why they triggered.

14. Failing to identify the first compromised system.

15. Failing to distinguish evidence from assumptions.
```

---

# 90. Practical Investigation Scenario

Alert:

```text
Suspicious PowerShell Execution
```

Known:

```text
Host:
WS-101

User:
alice

Time:
10:15 UTC
```

Investigation:

```text
1. Inspect process tree.
2. Inspect command line.
3. Inspect parent process.
4. Search DNS around the timestamp.
5. Search network connections.
6. Search file creation.
7. Search user's recent logins.
8. Search same hash across environment.
9. Search related alerts.
10. Determine scope.
```

---

# 91. Scenario – Phishing Investigation

Start:

```text
Suspicious Email
```

Investigate:

```text
Sender
Recipient
URL
Domain
Attachment
Hash
User Click
Process
Network
```

Timeline:

```text
Email
 ↓
Click
 ↓
Browser
 ↓
File Download
 ↓
Process Execution
 ↓
Network Connection
```

---

# 92. Scenario – Account Compromise

Start:

```text
Unusual Login
```

Investigate:

```text
Source IP
Location
Device
MFA
Session
Password Changes
Privilege Changes
Cloud Activity
Sensitive Actions
```

Then:

```text
Search other users
```

if the same source appears elsewhere.

---

# 93. Scenario – Malware Investigation

Start:

```text
Malware Detection
```

Investigate:

```text
Hash
Path
Process
Parent
User
Network
Persistence
Other Hosts
First Seen
Last Seen
```

---

# 94. Scenario – Lateral Movement

Start:

```text
Remote Login
```

Investigate:

```text
Source Host
Destination Host
Account
Protocol
Authentication
Process
Commands
Subsequent Activity
```

---

# 95. Scenario – Data Exfiltration

Start:

```text
Large Outbound Transfer
```

Investigate:

```text
Source Host
User
Process
Destination
Data Type
Volume
Timing
Prior Access
Compression
Cloud Storage
```

---

# 96. Threat Hunting Scenario

Hypothesis:

> Attackers may be using compromised accounts outside normal working hours.

Search:

```text
Authentication Events
```

Filter:

```text
Outside normal hours
+
Rare device
+
Rare source IP
+
Privileged account
```

Then pivot:

```text
User
 ↓
Host
 ↓
Process
 ↓
Network
```

---

# 97. Hunting Scenario – Rare PowerShell

Hypothesis:

> Attackers may be using PowerShell from unusual parent processes.

Search:

```text
PowerShell
```

Group:

```text
Parent Process
```

Identify:

```text
Rare Parents
```

Then investigate:

```text
Host
User
Command
Network
```

---

# 98. Hunting Scenario – Rare Domain

Hypothesis:

> A compromised endpoint may be communicating with newly observed domains.

Search:

```text
DNS
```

Find:

```text
Rare Domains
```

Then enrich:

```text
Threat Intelligence
Domain Age
Hosts
Users
Network Connections
```

---

# 99. Hunt Validation

A hunt finding should be classified:

```text
Benign
Suspicious
Malicious
Unknown
```

Then determine:

```text
Detection Needed?
Incident?
Further Hunting?
```

---

# 100. Interview Questions

### What is SOC triage?

> The rapid assessment of an alert or security event to determine validity, priority, severity, scope, and the appropriate next action.

### What is a security investigation?

> A structured analysis of evidence to determine what happened, how it happened, what was affected, and what response is required.

### What is threat hunting?

> A proactive, hypothesis-driven search for malicious or suspicious activity that may not have been detected automatically.

### What is the difference between triage and investigation?

> Triage quickly determines priority and whether deeper investigation is warranted; investigation performs the detailed analysis needed to establish facts and scope.

### What is a pivot?

> Using a known entity or piece of evidence to search for related activity.

### What is a timeline?

> A chronological representation of relevant events used to understand the sequence and relationships of activity.

### What is blast radius?

> The scope or extent of systems, users, data, or services potentially affected by an incident.

### What is hypothesis-driven hunting?

> Starting with a testable assumption about attacker behavior and searching telemetry for supporting or contradicting evidence.

### What is the difference between IOC hunting and behavioral hunting?

> IOC hunting searches for known artifacts such as IPs or hashes, while behavioral hunting searches for attacker-like activity patterns regardless of known indicators.

### How do you investigate a suspicious login?

> Review the user, source IP, device, time, location, authentication method, MFA, previous activity, privilege changes, related alerts, and subsequent actions, then determine whether the behavior is expected and assess scope.

### How do you investigate suspicious PowerShell?

> Examine the process tree, parent process, command line, user, host, file activity, network connections, DNS, related alerts, and prevalence across the environment.

### How do you determine incident scope?

> Search related users, hosts, IPs, hashes, processes, domains, and timestamps across the relevant data sources and determine the number and type of affected entities.

### Why is a timeline important?

> It helps establish causality, sequence, attack progression, and relationships between events.

### What should you do if logs are missing?

> Verify the health of the relevant data source first; absence of events may represent missing telemetry rather than absence of activity.

### Why document investigation queries?

> To make the investigation reproducible, auditable, and easier for another analyst to continue.

---

# 101. Quick Revision

```text
TRIAGE
→ Quickly assess priority and validity

INVESTIGATION
→ Establish facts and scope

THREAT HUNTING
→ Proactively search for threats

PIVOT
→ Search using a known entity

TIMELINE
→ Order events chronologically

SCOPE
→ Determine affected entities

BLAST RADIUS
→ Extent of potential impact

HYPOTHESIS
→ Testable explanation

IOC HUNT
→ Search known indicators

IOA HUNT
→ Search attack behaviors

BEHAVIORAL HUNT
→ Search suspicious patterns

ROOT CAUSE
→ Determine how the activity began

EVIDENCE
→ Facts supporting conclusions

CORRELATION
→ Connect related activity
```

---

# 102. Golden Rules

```text
1. Validate the alert before assuming maliciousness.

2. Understand why the detection triggered.

3. Extract key entities immediately.

4. Use pivots to expand the investigation.

5. Build a timeline.

6. Search both before and after the alert.

7. Determine scope early.

8. Distinguish evidence from assumptions.

9. Use hypotheses for complex investigations.

10. Verify missing telemetry before treating absence as evidence.

11. Use threat intelligence as context, not absolute truth.

12. Check related alerts.

13. Search historical activity when appropriate.

14. Investigate the first known suspicious event.

15. Determine whether persistence exists.

16. Determine whether lateral movement occurred.

17. Determine whether sensitive data was accessed.

18. Document important queries and findings.

19. Automate repetitive enrichment, not critical reasoning blindly.

20. A good investigation should explain what happened, how it happened, how far it spread, and what should happen next.
```

---

# 103. Final Mental Model

For alert investigation:

```text
ALERT
  ↓
WHY DID IT TRIGGER?
  ↓
WHAT HAPPENED?
  ↓
WHO?
  ↓
WHERE?
  ↓
WHEN?
  ↓
HOW?
  ↓
WHAT HAPPENED BEFORE?
  ↓
WHAT HAPPENED AFTER?
  ↓
WHAT ELSE IS RELATED?
  ↓
WHAT IS THE SCOPE?
  ↓
WHAT IS THE IMPACT?
  ↓
WHAT IS THE ROOT CAUSE?
  ↓
WHAT ACTION IS REQUIRED?
```

For threat hunting:

```text
HYPOTHESIS
   ↓
BEHAVIOR
   ↓
TELEMETRY
   ↓
SEARCH
   ↓
PIVOT
   ↓
CORRELATE
   ↓
VALIDATE
   ↓
SCOPE
   ↓
DETECTION / INCIDENT
```

---

# 104. Chapter Summary

Security investigation and threat hunting transform SIEM data into understanding.

The core difference is:

```text
TRIAGE
"What deserves attention?"

INVESTIGATION
"What actually happened?"

HUNTING
"Could something malicious be happening
without an alert?"
```

A strong investigation follows:

```text
ALERT
  ↓
VALIDATE
  ↓
PIVOT
  ↓
TIMELINE
  ↓
CORRELATE
  ↓
SCOPE
  ↓
IMPACT
  ↓
ROOT CAUSE
  ↓
RESPONSE
  ↓
DOCUMENT
```

A strong hunt follows:

```text
HYPOTHESIS
  ↓
TECHNIQUE / BEHAVIOR
  ↓
TELEMETRY
  ↓
SEARCH
  ↓
ANALYSIS
  ↓
PIVOT
  ↓
VALIDATION
  ↓
DETECTION / INCIDENT
```

The most important principle is:

> **Do not investigate events in isolation. Build context by connecting users, hosts, processes, network activity, identities, timelines, threat intelligence, and related alerts.**

A mature SOC analyst should be able to move from:

```text
One Alert
```

to:

```text
One Timeline
```

then:

```text
One Attack Story
```

and finally:

```text
One Defensible Security Decision
```

The next chapter moves from investigation into response operations:

```text
Chapter 11 – Incident Response & SIEM Workflows
```

There we will cover **incident lifecycle, preparation, detection, analysis, containment, eradication, recovery, post-incident activity, SIEM-to-case workflows, evidence handling, escalation, playbooks, response automation, SOAR integration, incident documentation, and practical incident-response scenarios.**
```