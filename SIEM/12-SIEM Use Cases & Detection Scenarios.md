# Chapter 12 – SIEM Use Cases & Detection Scenarios

> SIEM use cases translate security requirements and attacker behaviors into concrete detections, correlation rules, investigations, alerts, and response workflows. A mature SIEM is not measured by how many rules it contains, but by how effectively those rules identify meaningful threats with actionable context.

---

# 1. Introduction

A SIEM becomes operationally valuable when it can answer questions such as:

```text
Can we detect brute-force attacks?

Can we identify compromised accounts?

Can we detect suspicious endpoint execution?

Can we identify lateral movement?

Can we detect command-and-control activity?

Can we identify data exfiltration?

Can we detect ransomware behavior?

Can we investigate cloud compromise?
```

A complete SIEM use case connects:

```text
Threat
   ↓
Behavior
   ↓
Telemetry
   ↓
Detection Logic
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
```

---

# 2. What is a SIEM Use Case?

A SIEM use case is a defined security monitoring objective implemented through:

```text
Logs
+
Detection Logic
+
Correlation
+
Context
+
Alerting
+
Investigation
+
Response
```

Example:

```text
Use Case:
Password Spraying

Telemetry:
Authentication Logs

Detection:
Many failed logins
against many users
from one source

Alert:
Possible Password Spraying

Response:
Investigate source
and affected accounts
```

---

# 3. Detection Scenario

A detection scenario describes a specific situation the SIEM should identify.

Example:

```text
Scenario:
Privileged account logs in
from an unusual location.

Detection:
Unusual privileged login

Context:
User + IP + Device + Time

Risk:
High
```

---

# 4. Use Case Lifecycle

A good use case follows:

```text
Identify Threat
      ↓
Define Objective
      ↓
Identify Telemetry
      ↓
Normalize Data
      ↓
Design Detection
      ↓
Test
      ↓
Deploy
      ↓
Tune
      ↓
Monitor
      ↓
Retire / Improve
```

---

# 5. Use Case Requirements

Each use case should define:

```text
Use Case ID
Name
Objective
Threat
Data Sources
Required Fields
Detection Logic
Threshold
Time Window
Severity
Risk Score
MITRE Mapping
False Positives
Exceptions
Response
Owner
```

---

# 6. Use Case Example

```yaml
id: UC-AUTH-001

name: Password Spraying Detection

objective: Detect authentication attempts against
multiple accounts from a common source.

data_sources:
  - authentication
  - VPN
  - identity_provider

logic:
  failed_attempts > threshold
  unique_users > threshold

window:
  10 minutes

severity:
  high
```

The exact thresholds should be tuned to the environment.

---

# 7. Use Case Categories

Common SIEM use-case categories include:

```text
Authentication
Identity
Endpoint
Network
Malware
Web
Email
Cloud
Data Security
Privilege
Threat Intelligence
Insider Risk
Compliance
```

---

# 8. Authentication Use Cases

Authentication is one of the highest-value SIEM monitoring areas.

Common detections:

```text
Brute Force
Password Spraying
Impossible Travel
Unusual Login
Privileged Login
MFA Manipulation
New Device
Multiple Failed Logins
Credential Stuffing
Account Lockout
```

---

# 9. Use Case – Brute Force

Objective:

```text
Detect repeated authentication failures
against a single account.
```

Logic:

```text
Same user
+
Many failed logins
+
Short time window
```

Example:

```text
user = alice

failed attempts = 50

window = 5 minutes
```

↓

```text
Possible Brute Force
```

---

# 10. Brute Force Detection

Conceptually:

```text
Authentication Failure
       ↓
Group by User
       ↓
Count Failures
       ↓
Threshold
       ↓
Alert
```

---

# 11. Brute Force False Positives

Possible causes:

```text
Expired Password
Misconfigured Application
Mobile Device
Service Account
User Mistake
```

Therefore add context:

```text
Source IP
Device
Application
User Type
Historical Behavior
```

---

# 12. Use Case – Password Spraying

Password spraying differs from brute force.

Instead of:

```text
One User
Many Password Attempts
```

the attacker may use:

```text
One/Few Passwords
Against Many Users
```

Detection:

```text
Same source
+
Many unique users
+
Authentication failures
+
Short time window
```

---

# 13. Brute Force vs Password Spraying

```text
Brute Force
User A
 ↓
Many Attempts

Password Spraying
Source IP
 ├── User A
 ├── User B
 ├── User C
 ├── User D
 └── User E
```

This distinction is frequently tested in SOC interviews.

---

# 14. Use Case – Credential Stuffing

Credential stuffing uses previously compromised username/password combinations.

Detection signals:

```text
Many Accounts
+
Repeated Login Attempts
+
External Sources
+
Known Compromised Credentials
+
Unusual Login Patterns
```

---

# 15. Use Case – Account Lockout

A large number of account lockouts may indicate:

```text
Brute Force
Password Spraying
Credential Abuse
Misconfiguration
```

Correlation:

```text
Multiple Account Lockouts
+
Common Source
```

↓

```text
Potential Attack
```

---

# 16. Use Case – Successful Login After Failures

Sequence:

```text
Failed Login
      ↓
Failed Login
      ↓
Failed Login
      ↓
Successful Login
```

This may indicate:

```text
Potential Account Compromise
```

Context:

```text
Source IP
Device
Location
User
MFA
```

---

# 17. Use Case – Impossible Travel

Example:

```text
Login 1:
India

10 minutes later

Login 2:
United States
```

Potential:

```text
Impossible Travel
```

But investigate:

```text
VPN
Proxy
Cloud Access
Mobile Networks
Geolocation Accuracy
```

Geographic anomalies are signals, not automatic proof of compromise.

---

# 18. Use Case – Unusual Login Time

Example:

```text
User normally logs in:
09:00–18:00

New login:
03:00
```

Potentially suspicious.

Better:

```text
Unusual Time
+
Unusual Device
+
Unusual Location
```

---

# 19. Use Case – New Device Login

Detection:

```text
Known User
+
Previously Unseen Device
+
Unusual Location
```

Risk increases if:

```text
Privileged User
+
Sensitive Action
```

---

# 20. Use Case – Privileged Account Login

Monitor:

```text
Administrator
Root
Domain Admin
Cloud Admin
Security Admin
```

Detect:

```text
Unusual Source
Unusual Time
New Device
Privilege Change
Sensitive Action
```

---

# 21. Use Case – Privilege Escalation

Signals:

```text
Group Membership Change
Admin Role Assignment
Privilege Grant
Sudo Activity
Token Abuse
```

Correlation:

```text
Normal User
      ↓
Privilege Change
      ↓
Sensitive Action
```

---

# 22. Use Case – MFA Manipulation

Monitor:

```text
MFA Disabled
MFA Method Added
MFA Method Removed
Recovery Method Changed
Authentication Policy Changed
```

High-risk correlation:

```text
Suspicious Login
+
MFA Change
+
Sensitive Action
```

---

# 23. Endpoint Use Cases

Endpoint monitoring can detect:

```text
Malware
Suspicious Process
PowerShell
Command Shell
Script Execution
Persistence
Credential Access
Defense Evasion
Lateral Movement
```

---

# 24. Use Case – Suspicious PowerShell

Basic:

```text
PowerShell Execution
```

Better:

```text
PowerShell
+
Encoded Command
+
Unusual Parent
+
Network Connection
```

---

# 25. PowerShell Detection

Telemetry:

```text
Process Creation
PowerShell Logs
EDR
Command Line
Parent Process
Network
```

Detection:

```text
powershell.exe
+
suspicious behavior
```

---

# 26. PowerShell False Positives

Legitimate:

```text
System Administration
Configuration Management
IT Automation
Software Deployment
Monitoring
```

Therefore:

```text
PowerShell ≠ Malicious
```

---

# 27. Use Case – Suspicious Command Shell

Detect:

```text
cmd.exe
```

combined with:

```text
Unusual Parent
Suspicious Arguments
Unexpected User
Rare Host
Network Activity
```

---

# 28. Use Case – Office Application Spawning Shell

Potential sequence:

```text
winword.exe
      ↓
powershell.exe
```

or:

```text
excel.exe
      ↓
cmd.exe
```

This can be suspicious depending on context.

Investigate:

```text
Document
User
Command
Network
File Creation
```

---

# 29. Use Case – Suspicious Process Chain

Example:

```text
Browser
  ↓
Office
  ↓
Script Interpreter
  ↓
Unknown Executable
  ↓
External Network
```

Correlation can produce:

```text
Potential Malware Execution
```

---

# 30. Use Case – Unsigned Executable

Potential signals:

```text
Unknown Binary
+
Unsigned
+
User-Writable Directory
+
Network Connection
```

Investigate:

```text
Hash
Path
Parent
User
Prevalence
Network
```

---

# 31. Use Case – Rare Process

Detection:

```text
Process
+
Very Low Prevalence
```

Useful enrichment:

```text
Signed?
Known?
Hash?
Parent?
User?
Network?
```

Rare does not automatically mean malicious.

---

# 32. Use Case – Persistence

Monitor:

```text
Scheduled Tasks
Services
Startup Items
Registry Changes
New Accounts
Cloud Credentials
```

Correlation:

```text
New Persistence
+
Suspicious Process
+
External Connection
```

---

# 33. Use Case – Scheduled Task

Example:

```text
Scheduled Task Created
+
Unknown User
+
Suspicious Command
```

↓

```text
Potential Persistence
```

---

# 34. Use Case – Service Creation

Monitor:

```text
New Service
+
Unexpected Executable
+
Privileged User
```

Investigate:

```text
Binary
Path
Signer
Creator
Network
```

---

# 35. Use Case – Credential Access

Signals:

```text
Sensitive Process Access
Credential Store Access
Browser Credential Access
Credential Dumping Tools
Suspicious Memory Access
```

Correlation:

```text
Suspicious Process
+
Credential Access
+
Outbound Connection
```

---

# 36. Use Case – Lateral Movement

Monitor:

```text
Remote Authentication
Remote Services
SMB
RDP
SSH
Administrative Shares
Remote Execution
```

---

# 37. Use Case – Unusual RDP

Detection:

```text
RDP Login
+
New Source Host
+
Privileged Account
+
Unusual Time
```

Potential:

```text
Lateral Movement
```

---

# 38. Use Case – Unusual SSH

Detection:

```text
SSH Login
+
New Source
+
Privileged User
+
Rare Destination
```

Investigate:

```text
Commands
Process
Network
Authentication
```

---

# 39. Use Case – Lateral Movement Sequence

```text
Credential Access
      ↓
Remote Authentication
      ↓
New Host
      ↓
Remote Process
```

↓

```text
Possible Lateral Movement
```

---

# 40. Network Use Cases

Network SIEM use cases include:

```text
Port Scanning
C2
DNS Tunneling
Beaconing
Malicious IP
Malicious Domain
Data Exfiltration
Unusual Protocol
Rare Destination
```

---

# 41. Use Case – Port Scanning

Signals:

```text
One Source
+
Many Destination Ports
```

or:

```text
One Source
+
Many Destination Hosts
```

within a short window.

---

# 42. Port Scan Detection

```text
source.ip = X

unique(destination.ip) > threshold
OR
unique(destination.port) > threshold
```

Thresholds should be tuned for the environment.

---

# 43. Port Scan False Positives

Possible legitimate sources:

```text
Vulnerability Scanners
Monitoring Systems
Network Management
Security Tools
Asset Discovery
```

Allowlisting may be appropriate where justified.

---

# 44. Use Case – Malicious IP

```text
Network Connection
       ↓
Destination IP
       ↓
Threat Intelligence
       ↓
High Confidence
       ↓
Risk
       ↓
Alert
```

---

# 45. Use Case – Malicious Domain

```text
DNS Query
       ↓
Domain
       ↓
Threat Intelligence
       ↓
Malicious
       ↓
Alert
```

Then investigate:

```text
Host
User
Process
Subsequent Connection
```

---

# 46. Use Case – DNS Tunneling

Potential signals:

```text
Very Long Queries
High Query Volume
High Entropy Subdomains
Unusual Record Types
Rare Domains
Periodic Queries
```

A single signal is not enough.

---

# 47. DNS Tunneling Correlation

```text
Host
+
High DNS Query Volume
+
Long Random Subdomains
+
Rare Domain
+
Repeated Timing
```

↓

```text
Potential DNS Tunneling
```

---

# 48. Use Case – Beaconing

Beaconing can appear as:

```text
Repeated Connections
+
Similar Time Intervals
+
Same Destination
```

Example:

```text
10:00
10:05
10:10
10:15
10:20
```

This may indicate automated communication.

Periodic traffic alone is not proof of C2.

---

# 49. Use Case – Command and Control

Combine:

```text
Suspicious Process
+
Repeated Outbound Connection
+
Rare Destination
+
Threat Intelligence
```

↓

```text
High-Confidence C2 Candidate
```

---

# 50. Use Case – Data Exfiltration

Signals:

```text
Large Outbound Transfer
+
Sensitive Data Access
+
Rare Destination
```

---

# 51. Data Exfiltration Detection

Example:

```text
Sensitive File Access
      ↓
Archive Creation
      ↓
Large Transfer
      ↓
External Destination
```

↓

```text
Potential Exfiltration
```

---

# 52. Data Transfer Baselines

Instead of fixed thresholds only:

```text
Normal:
10 MB/day

Current:
2 GB/day
```

Potential anomaly.

Better:

```text
Volume
+
Destination
+
User
+
Time
+
Process
+
Data Sensitivity
```

---

# 53. Web Use Cases

Web application monitoring:

```text
SQL Injection
XSS
Path Traversal
Authentication Abuse
Web Shell
Suspicious User-Agent
Credential Attacks
API Abuse
```

---

# 54. Use Case – SQL Injection

Potential signals:

```text
Suspicious Query Patterns
+
Web Server Error Spikes
+
Repeated Requests
```

SIEM can correlate:

```text
Web Logs
+
Application Logs
+
WAF
```

---

# 55. Use Case – Web Shell

Potential signals:

```text
New Web File
+
Executable Script
+
Unusual Parent
+
External Connection
```

Investigate:

```text
File
Hash
Web Server
Request
User
Network
```

---

# 56. Use Case – Authentication Attack on Web Application

```text
Many Failed Logins
+
Same Source
+
Multiple Accounts
```

or:

```text
Many Requests
+
Authentication Endpoint
+
High Failure Rate
```

---

# 57. Email Use Cases

Common detections:

```text
Phishing
Malicious Attachment
Malicious URL
Spoofing
BEC
Credential Harvesting
Mass Email
Suspicious Sender
```

---

# 58. Use Case – Phishing

Correlation:

```text
Email
 ↓
Suspicious Domain
 ↓
User Click
 ↓
Browser
 ↓
Download
 ↓
Process Execution
```

This is stronger than detecting the email alone.

---

# 59. Use Case – Business Email Compromise

Signals:

```text
Mailbox Rule Change
+
Unusual Login
+
New Forwarding Rule
+
Sensitive Email Access
```

Potential:

```text
Account Compromise
```

---

# 60. Use Case – Malicious Email Attachment

Combine:

```text
Attachment
+
Known Malicious Hash
+
User Opened
+
Process Execution
```

↓

```text
Potential Endpoint Compromise
```

---

# 61. Cloud Security Use Cases

Monitor:

```text
Cloud Login
IAM Changes
Access Keys
Privilege Changes
API Activity
Storage Access
Security Group Changes
New Resources
```

---

# 62. Use Case – Cloud Privilege Escalation

```text
User
 ↓
Role Change
 ↓
Privilege Increase
 ↓
Sensitive API Call
```

Potential:

```text
Cloud Account Compromise
```

---

# 63. Use Case – New Access Key

Monitor:

```text
Access Key Creation
+
Unusual User
+
Unusual Location
+
Immediate API Activity
```

---

# 64. Use Case – Cloud Storage Access

Detect:

```text
Sensitive Bucket Access
+
New Principal
+
Large Download
+
External Source
```

---

# 65. Use Case – Security Group Modification

Example:

```text
Security Group Changed
+
Internet Exposure
+
Sensitive Server
```

Potential:

```text
Cloud Misconfiguration
```

or:

```text
Potential Attack Preparation
```

---

# 66. Use Case – New Cloud Resource

Monitor:

```text
New VM
New Container
New Function
New User
New Key
```

Context:

```text
Who Created?
Where?
When?
Why?
What happened afterward?
```

---

# 67. Ransomware Use Cases

Ransomware detection should focus on behavior.

Potential signals:

```text
Mass File Modifications
File Extension Changes
High Rename Rate
Shadow Copy Manipulation
Backup Tampering
Security Tool Changes
Multiple Hosts
```

---

# 68. Ransomware Correlation

```text
Mass File Changes
      +
Suspicious Process
      +
Backup Modification
      +
Multiple Hosts
```

↓

```text
Critical Risk
```

---

# 69. Ransomware Detection Challenges

Potential legitimate causes:

```text
Backup Systems
File Synchronization
Software Updates
Bulk Processing
Migration
```

Context is essential.

---

# 70. Insider Threat Use Cases

Potential signals:

```text
Unusual Data Access
Privilege Abuse
Mass Downloads
Rare Applications
After-Hours Activity
External Transfer
```

Insider risk detections require careful privacy and governance considerations.

---

# 71. Insider Threat Correlation

```text
Employee
+
Sensitive File Access
+
Large Download
+
External Upload
+
Unusual Time
```

↓

```text
Potential Data Exfiltration
```

Do not automatically conclude malicious insider intent.

---

# 72. Vulnerability-Driven Detection

Combine:

```text
Known Vulnerability
+
Affected Asset
+
Exploit-Like Activity
```

Example:

```text
Critical Web Server
+
Known Vulnerability
+
Suspicious Requests
```

↓

```text
High-Priority Investigation
```

---

# 73. Threat Intelligence + Vulnerability

Example:

```text
Asset has critical vulnerability
+
Known exploit activity exists
+
Suspicious network request observed
```

This combination can significantly increase risk.

---

# 74. Detection Scenario – Compromised Account

```text
Unusual Login
      ↓
New Device
      ↓
MFA Change
      ↓
Privilege Change
      ↓
Sensitive Access
```

↓

```text
Possible Account Takeover
```

---

# 75. Detection Scenario – Malware

```text
Email Attachment
      ↓
Office Process
      ↓
PowerShell
      ↓
File Creation
      ↓
C2 Connection
```

↓

```text
Possible Malware Infection
```

---

# 76. Detection Scenario – Lateral Movement

```text
Credential Access
      ↓
Remote Login
      ↓
New Host
      ↓
Remote Process
```

↓

```text
Possible Lateral Movement
```

---

# 77. Detection Scenario – Exfiltration

```text
Sensitive Access
      ↓
Archive Creation
      ↓
Large Transfer
      ↓
Rare External Destination
```

↓

```text
Potential Data Exfiltration
```

---

# 78. Detection Scenario – Ransomware

```text
Mass File Modification
      ↓
Suspicious Process
      ↓
Backup Tampering
      ↓
Multiple Hosts
```

↓

```text
Potential Ransomware
```

---

# 79. Detection Scenario – Cloud Compromise

```text
Unusual Cloud Login
      ↓
MFA Change
      ↓
Privilege Escalation
      ↓
New Access Key
      ↓
Sensitive API Calls
```

↓

```text
Potential Cloud Account Takeover
```

---

# 80. Detection Scenario – Phishing

```text
Suspicious Email
      ↓
User Click
      ↓
Suspicious Domain
      ↓
File Download
      ↓
Process Execution
```

↓

```text
Potential Phishing Compromise
```

---

# 81. Detection Scenario – C2

```text
Rare Domain
      ↓
DNS Query
      ↓
Periodic Connections
      ↓
Suspicious Process
      ↓
Known Malicious Infrastructure
```

↓

```text
Potential C2
```

---

# 82. Detection Scenario – Privilege Escalation

```text
Normal User
      ↓
Privilege Change
      ↓
Administrative Login
      ↓
Sensitive Action
```

↓

```text
Potential Privilege Abuse
```

---

# 83. Detection Scenario – Reconnaissance

```text
One Host
      ↓
Many Hosts
      ↓
Many Ports
      ↓
Short Time Window
```

↓

```text
Potential Network Scanning
```

---

# 84. Use Case Prioritization

Not all use cases should be built immediately.

Prioritize based on:

```text
Threat Relevance
Business Impact
Attack Probability
Asset Criticality
Telemetry Availability
Detection Feasibility
Historical Incidents
Regulatory Requirements
```

---

# 85. High-Priority Use Cases

Many organizations prioritize:

```text
Authentication Attacks
Privileged Account Abuse
Malware
Endpoint Execution
Lateral Movement
C2
Data Exfiltration
Ransomware
Cloud Account Compromise
Critical Asset Attacks
```

The exact priorities depend on the environment.

---

# 86. Use Case Maturity

A simple maturity model:

```text
Level 1
Basic Alert

Level 2
Context Enrichment

Level 3
Correlation

Level 4
Risk-Based Detection

Level 5
Automated Response
```

---

# 87. Basic Alert

```text
PowerShell detected
```

---

# 88. Context-Enriched Alert

```text
PowerShell detected

User:
Alice

Host:
WS01

Parent:
Word

Network:
External connection
```

---

# 89. Correlated Alert

```text
Office
 ↓
PowerShell
 ↓
File Creation
 ↓
DNS
 ↓
External Connection
```

---

# 90. Risk-Based Alert

```text
Suspicious PowerShell
+
Critical Host
+
Privileged User
+
Malicious IP
```

↓

```text
Critical Risk
```

---

# 91. Automated Response

```text
High-Confidence Malware
        ↓
SIEM
        ↓
SOAR
        ↓
Analyst / Approved Automation
        ↓
Endpoint Isolation
```

---

# 92. Use Case Testing

Before production:

```text
Test Positive Case
Test Negative Case
Test Edge Cases
Test Missing Data
Test Duplicates
Test Delayed Events
```

---

# 93. Positive Test

Expected malicious/suspicious behavior:

```text
Detection:
TRIGGER
```

---

# 94. Negative Test

Expected legitimate behavior:

```text
Detection:
NO TRIGGER
```

---

# 95. Edge Case Testing

Test:

```text
Boundary Threshold
Time Window
Multiple Users
Multiple Hosts
IPv4 / IPv6
Missing Fields
Duplicate Events
Delayed Events
```

---

# 96. Detection Tuning

If too many alerts:

```text
Review False Positives
      ↓
Add Context
      ↓
Improve Threshold
      ↓
Add Exceptions
      ↓
Retest
```

---

# 97. Exception Management

Examples:

```text
Approved Scanner
Security Team
Monitoring Server
Backup System
Known Automation
```

Exceptions should be:

```text
Documented
Scoped
Reviewed
Time-Bounded where possible
```

Avoid broad permanent exclusions.

---

# 98. Detection Health

Monitor:

```text
Rule Enabled?
Data Available?
Trigger Rate?
False Positive Rate?
Latency?
Performance?
Recent Changes?
```

---

# 99. Detection Drift

A detection may become less effective because:

```text
Environment Changes
New Applications
New Cloud Services
New Attacker Techniques
New Logging Format
```

Therefore:

```text
Continuous Review
```

is necessary.

---

# 100. Detection Use Case Documentation

Example:

```yaml
id: UC-NET-005

name: Suspicious C2 Communication

objective: Detect endpoints communicating with
potential command-and-control infrastructure.

sources:
  - DNS
  - firewall
  - proxy
  - endpoint

logic:
  suspicious_domain
  AND
  repeated_outbound_connections
  AND
  unusual_process

severity: high

response:
  investigate_host
  enrich_indicator
  correlate_process
```

---

# 101. Use Case Dashboard

A SOC dashboard can show:

```text
Authentication:
45 alerts

Endpoint:
32 alerts

Network:
21 alerts

Cloud:
12 alerts

Data Security:
8 alerts
```

Then:

```text
Top Risks
Top Techniques
Top Affected Assets
Top Users
```

---

# 102. Use Case KPIs

Measure:

```text
Alert Volume
True Positive Rate
False Positive Rate
Detection Latency
Investigation Time
Incident Conversion
Coverage
Data Quality
```

---

# 103. Detection Effectiveness

A useful question:

```text
Does the detection identify
important malicious activity?
```

Not merely:

```text
How many alerts does it generate?
```

---

# 104. Detection Precision

Conceptually:

```text
True Positives
-------------------------
True Positives + False Positives
```

Higher precision generally means fewer false alarms among triggered alerts.

---

# 105. Detection Recall

Conceptually:

```text
True Positives
-------------------------
True Positives + False Negatives
```

Higher recall means more relevant malicious activity is detected.

In security, improving one may affect the other.

---

# 106. Precision vs Recall

```text
High Precision
→ Fewer false alarms

High Recall
→ Fewer missed threats
```

The right balance depends on:

```text
Threat
Risk
SOC Capacity
Response Cost
```

---

# 107. Detection Latency

Measure:

```text
Event Occurs
      ↓
Event Ingested
      ↓
Detection Executes
      ↓
Alert Generated
```

Large delays can reduce response effectiveness.

---

# 108. Use Case Performance

Complex detections may consume significant resources.

Optimize:

```text
Early Filtering
Field Selection
Time Windows
Aggregation
Indexes
Preprocessing
```

---

# 109. Use Case Dependencies

Example:

```text
C2 Detection
depends on:
DNS
Firewall
Endpoint
Threat Intelligence
```

If DNS disappears:

```text
Detection Confidence ↓
```

Track dependencies.

---

# 110. Use Case Failure

A detection can fail because:

```text
No Logs
Parser Failure
Field Mapping Error
Rule Disabled
Wrong Threshold
Incorrect Time Window
Performance Issue
Data Delay
```

---

# 111. Practical Lab – Authentication

Create detections for:

```text
Brute Force
Password Spraying
Impossible Travel
Privileged Login
MFA Change
```

For each define:

```text
Data
Logic
Threshold
Severity
Response
```

---

# 112. Practical Lab – Endpoint

Create:

```text
Suspicious PowerShell
Suspicious Process Chain
Persistence
Credential Access
Lateral Movement
```

Then map each to:

```text
ATT&CK
```

---

# 113. Practical Lab – Network

Create:

```text
Port Scan
Malicious IP
Malicious Domain
DNS Tunneling
Beaconing
C2
```

Test:

```text
Normal Traffic
Suspicious Traffic
```

---

# 114. Practical Lab – Cloud

Create:

```text
Unusual Cloud Login
Privilege Escalation
New Access Key
Sensitive Storage Access
Security Group Change
```

---

# 115. Practical Lab – Full Attack Chain

Simulate a controlled scenario:

```text
Phishing
 ↓
Execution
 ↓
Credential Access
 ↓
Lateral Movement
 ↓
C2
 ↓
Data Access
```

Then determine:

```text
Which detections trigger?

Which correlate?

What risk is produced?

What incident is created?

What response occurs?
```

Only use authorized test environments for attack simulation.

---

# 116. Interview Questions

### What is a SIEM use case?

> A defined security monitoring objective implemented through telemetry, detection logic, correlation, alerting, investigation, and response.

### What are common SIEM use cases?

> Authentication attacks, privilege abuse, malware, endpoint execution, lateral movement, command-and-control, data exfiltration, ransomware, phishing, cloud compromise, and suspicious administrative activity.

### How would you create a SIEM use case?

> Identify the threat, define the detection objective, identify required telemetry, normalize the data, design detection logic, test positive and negative cases, deploy, tune, and continuously monitor effectiveness.

### How would you detect brute force?

> Count repeated authentication failures against the same account within a defined time window, enriched with source, device, application, and user context.

### How is password spraying different?

> Password spraying targets many accounts with relatively few attempts per account, so unique-user counts and common source analysis are important.

### How would you detect account compromise?

> Correlate unusual authentication, new devices or locations, MFA changes, privilege changes, and sensitive actions.

### How would you detect suspicious PowerShell?

> Analyze PowerShell execution together with command line, parent process, user, host, network connections, and other suspicious behaviors.

### How would you detect lateral movement?

> Monitor unusual remote authentication and remote-service activity, then correlate source host, destination host, account, process, and subsequent actions.

### How would you detect C2?

> Combine suspicious outbound connections, periodic behavior, rare destinations, DNS or proxy activity, endpoint process context, and threat intelligence.

### How would you detect data exfiltration?

> Correlate sensitive data access with abnormal outbound transfer volume, unusual destinations, compression or staging behavior, and user/process context.

### How would you detect ransomware?

> Monitor mass file modifications, encryption-like behavior, backup or recovery-control changes, suspicious processes, and activity across multiple systems.

### What is detection tuning?

> Adjusting logic, thresholds, exclusions, context, and correlation to improve detection quality and reduce unnecessary alerts.

### What is detection precision?

> The proportion of triggered detections that are true positives.

### What is detection recall?

> The proportion of relevant malicious activity that is successfully detected.

---

# 117. Quick Revision

```text
SIEM USE CASE
→ Security monitoring objective

DETECTION SCENARIO
→ Specific suspicious behavior

BRUTE FORCE
→ Many attempts against one account

PASSWORD SPRAYING
→ Attempts across many accounts

CREDENTIAL STUFFING
→ Reuse of compromised credentials

PRIVILEGE ABUSE
→ Suspicious elevation or privileged action

MALWARE
→ Malicious or suspicious endpoint activity

LATERAL MOVEMENT
→ Movement between systems

C2
→ Attacker communication

EXFILTRATION
→ Unauthorized data transfer

RANSOMWARE
→ Malicious data/system impact

PHISHING
→ Malicious social-engineering delivery

CLOUD COMPROMISE
→ Unauthorized cloud identity/resource activity

PRECISION
→ How many alerts are actually useful

RECALL
→ How much relevant malicious activity is detected

TUNING
→ Improve detection quality
```

---

# 118. Golden Rules

```text
1. Build use cases around threats, not around available logs alone.

2. Start with a clear detection objective.

3. Identify required telemetry before writing the rule.

4. Use multiple signals when one signal is weak.

5. Add entity and business context.

6. Do not treat anomalies as automatically malicious.

7. Test both positive and negative scenarios.

8. Measure false positives.

9. Measure missed detections when possible.

10. Document every important use case.

11. Keep exceptions narrow and controlled.

12. Monitor detection health.

13. Review use cases when the environment changes.

14. Retire detections that no longer provide value.

15. Prefer actionable alerts over high alert volume.

16. Correlation often produces better context than isolated rules.

17. Use threat intelligence to enrich detections.

18. Map relevant behaviors to ATT&CK.

19. Automate carefully.

20. The goal of a SIEM use case is not to generate an alert—it is to enable a better security decision.
```

---

# 119. Final Mental Model

Think of every SIEM use case as:

```text
THREAT
  ↓
ATTACK BEHAVIOR
  ↓
TELEMETRY
  ↓
NORMALIZATION
  ↓
DETECTION
  ↓
CORRELATION
  ↓
CONTEXT
  ↓
RISK
  ↓
ALERT
  ↓
INVESTIGATION
  ↓
RESPONSE
  ↓
LESSONS LEARNED
  ↓
DETECTION IMPROVEMENT
```

A mature use case should answer:

```text
What threat are we detecting?

Why does it matter?

What logs do we need?

What behavior are we looking for?

What legitimate activity looks similar?

How do we reduce false positives?

What context should the alert contain?

How should analysts investigate it?

What response should follow?

How do we measure whether it works?
```

---

# 120. Chapter Summary

SIEM use cases are the practical bridge between security requirements and SOC operations.

The most valuable use cases typically combine:

```text
Events
+
Behavior
+
Context
+
Threat Intelligence
+
Correlation
+
Risk
```

Instead of:

```text
One Event
    ↓
One Alert
```

prefer:

```text
Multiple Signals
      ↓
Context
      ↓
Correlation
      ↓
Risk
      ↓
Actionable Alert
```

The major use-case families to master are:

```text
Authentication
Identity
Endpoint
Malware
Privilege
Lateral Movement
Network
C2
Web
Email
Cloud
Data Security
Ransomware
Insider Risk
Threat Intelligence
```

The key principle is:

> **A strong SIEM use case detects meaningful attacker behavior, provides enough context for an analyst to make a decision, and connects naturally to investigation and response.**

The next chapter moves from individual detection scenarios into the engineering discipline required to operate them at scale:

```text
Chapter 13 – SIEM Engineering, Tuning & Optimization
```

There we will cover **SIEM architecture from an engineering perspective, parsing and normalization, schema design, detection-as-code, rule lifecycle, performance optimization, indexing, storage, retention, false-positive tuning, alert quality, pipeline health, scalability, reliability, testing, deployment, version control, monitoring, and production best practices.**