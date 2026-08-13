# Chapter 08 – Threat Intelligence & IOC Integration

> Threat intelligence gives the SIEM external context about threats, while IOC integration allows security telemetry to be compared against known indicators such as malicious IP addresses, domains, URLs, file hashes, and other observable artifacts.

---

# 1. Introduction

A SIEM primarily tells us:

```text
What happened?
```

Threat intelligence helps answer:

```text
Is this associated with a known threat?

Who or what may be behind it?

How dangerous is it?

Has this indicator been observed elsewhere?

What should we investigate next?
```

The combined workflow is:

```text
Security Telemetry
       ↓
Observable
       ↓
Threat Intelligence Lookup
       ↓
Context
       ↓
Detection / Enrichment
       ↓
Risk Evaluation
       ↓
Alert
       ↓
Investigation
```

---

# 2. What is Threat Intelligence?

Threat intelligence is information about threats that is collected, analyzed, contextualized, and used to support security decisions.

It can include:

```text
Indicators
Threat Actors
Campaigns
Malware
Tactics
Techniques
Vulnerabilities
Infrastructure
Victimology
Behavior
Relationships
Confidence
Context
```

---

# 3. Threat Intelligence vs Threat Data

These terms should not be treated as identical.

## Threat Data

Raw observations:

```text
203.0.113.50
malicious.example
SHA256 = abc123...
```

## Threat Intelligence

Interpreted information:

```text
203.0.113.50

Associated with:
Known malware infrastructure

Confidence:
High

First Seen:
...

Last Seen:
...

Recommended Action:
Investigate outbound connections.
```

Therefore:

```text
Data
 ↓
Analysis
 ↓
Context
 ↓
Intelligence
```

---

# 4. Why Threat Intelligence Matters to SIEM

Without intelligence:

```text
Connection to IP X
```

With intelligence:

```text
Connection to IP X

IP X:
Known malicious infrastructure
Associated with malware campaign
High confidence
```

The second event is much more actionable.

---

# 5. Threat Intelligence Types

Threat intelligence is commonly discussed at different levels:

```text
Strategic
Operational
Tactical
Technical
```

---

# 6. Strategic Threat Intelligence

Focuses on high-level business decisions.

Examples:

```text
Threat Trends
Industry Risks
Geopolitical Threats
Adversary Activity
Business Impact
```

Audience:

```text
Executives
Security Leadership
Risk Teams
```

---

# 7. Operational Threat Intelligence

Focuses on campaigns and adversary activity.

Examples:

```text
Threat Actor Campaign
Attack Infrastructure
Targeting
Attack Methods
Campaign Timeline
```

Audience:

```text
Threat Intelligence Analysts
Incident Responders
Security Operations
```

---

# 8. Tactical Threat Intelligence

Focuses on attacker techniques.

Examples:

```text
Credential Theft
PowerShell Abuse
Lateral Movement
Persistence
Defense Evasion
```

Often maps to:

```text
MITRE ATT&CK
```

---

# 9. Technical Threat Intelligence

Focuses on machine-readable indicators.

Examples:

```text
IP
Domain
URL
Hash
Email
Certificate
File
```

This is especially useful for SIEM automation.

---

# 10. What is an IOC?

IOC means:

```text
Indicator of Compromise
```

An IOC is an observable artifact that may indicate malicious activity or compromise.

Examples:

```text
IP Address
Domain
URL
File Hash
Email Address
File Name
Registry Key
Certificate
User-Agent
```

---

# 11. IOC Categories

Common IOC categories:

```text
Network
Endpoint
Email
Web
Identity
Cloud
File
Infrastructure
```

---

# 12. IP Address IOC

Example:

```text
203.0.113.10
```

Potentially associated with:

```text
C2
Scanning
Malware Hosting
Phishing
Brute Force
```

But:

> An IP address alone does not prove malicious activity.

IPs can be:

```text
Dynamic
Shared
Cloud-Hosted
Reassigned
Compromised
NATed
```

---

# 13. Domain IOC

Example:

```text
malicious-example.com
```

May be associated with:

```text
Phishing
C2
Malware Distribution
Credential Harvesting
```

Domains can change rapidly, so freshness matters.

---

# 14. URL IOC

Example:

```text
https://example.com/payload
```

URLs can provide more context than domains:

```text
Domain
Path
Parameters
Protocol
```

---

# 15. File Hash IOC

Common hashes:

```text
MD5
SHA-1
SHA-256
```

Example:

```text
SHA256:
abcdef123456...
```

Hash matching can provide high-confidence identification of known files.

---

# 16. Hash Limitations

A hash changes when the file changes.

Therefore:

```text
Known Malware
    ↓
Modified Malware
    ↓
Different Hash
```

This is why behavior-based detections are important.

---

# 17. Email IOC

Examples:

```text
Malicious Sender
Sender Domain
Reply-To Address
Attachment Hash
Malicious URL
```

Email investigations often combine multiple indicators.

---

# 18. Certificate IOC

Attackers may use certificates associated with suspicious infrastructure.

Useful fields:

```text
Certificate Hash
Issuer
Subject
Serial Number
Validity
Fingerprint
```

---

# 19. User-Agent IOC

Suspicious user agents may indicate:

```text
Malware
Automation
Scanning
C2
Tooling
```

However, user agents can easily be spoofed.

---

# 20. File Name IOC

Example:

```text
invoice.exe
update.ps1
svchost2.exe
```

File names alone are weak indicators because legitimate and malicious files can share names.

Combine with:

```text
Path
Hash
Signer
Parent Process
Behavior
```

---

# 21. IOC Confidence

Not every indicator has equal reliability.

Example:

```text
Indicator A:
High confidence

Indicator B:
Medium confidence

Indicator C:
Low confidence
```

Confidence should influence how the SOC responds.

---

# 22. IOC Reputation

An intelligence provider may assign reputation such as:

```text
Malicious
Suspicious
Benign
Unknown
```

Do not blindly treat every:

```text
Unknown
```

as malicious.

---

# 23. IOC Lifecycle

Indicators have a lifecycle:

```text
Discovered
   ↓
Validated
   ↓
Enriched
   ↓
Distributed
   ↓
Detected
   ↓
Investigated
   ↓
Expired
   ↓
Retired
```

---

# 24. IOC Aging

Indicators become less useful over time.

Example:

```text
Malicious IP
```

may later become:

```text
Reassigned to another customer
```

Therefore:

```text
Indicator
+
Age
+
Last Seen
+
Confidence
```

should be considered together.

---

# 25. IOC Expiration

An organization can define expiration:

```text
IOC Added:
Day 1

Review:
Day 30

Expiration:
Day 60
```

The exact lifecycle depends on the indicator type and confidence.

---

# 26. Threat Intelligence Sources

Threat intelligence can come from:

```text
Commercial Feeds
Open-Source Intelligence
Government Sources
Industry Sharing Groups
Internal Intelligence
Security Vendors
Incident Response
Research Teams
Community Sources
```

---

# 27. Internal Threat Intelligence

One of the most valuable sources is your own environment.

Examples:

```text
Previously Compromised IP
Known Phishing Domain
Observed Malware Hash
Past Incident Infrastructure
Internal Honeypot
Incident Response Findings
```

---

# 28. Open-Source Intelligence

OSINT can provide:

```text
Malware Information
Threat Actor Reports
IOC Lists
Campaign Reports
Security Research
Vulnerability Intelligence
```

Always evaluate:

```text
Source Reliability
Freshness
Context
Confidence
```

---

# 29. Commercial Intelligence

Commercial feeds may provide:

```text
Large-Scale IOC Collection
Reputation
Actor Attribution
Campaign Context
Malware Intelligence
Automated Updates
```

Commercial does not automatically mean:

```text
Always Accurate
```

Feed quality must still be measured.

---

# 30. Threat Intelligence Quality

Evaluate a feed based on:

```text
Accuracy
Freshness
Coverage
False Positive Rate
Context
Update Frequency
Availability
Source Transparency
```

---

# 31. IOC Feed

An IOC feed may contain:

```text
Indicator
Type
Confidence
First Seen
Last Seen
Source
Threat
Tags
Expiration
```

Example:

```text
Indicator:
203.0.113.10

Type:
IPv4

Confidence:
High

Threat:
Malware

Last Seen:
Recent
```

---

# 32. Feed Ingestion

Typical architecture:

```text
Threat Intelligence Provider
          ↓
        API/Feed
          ↓
      TI Collector
          ↓
     Normalization
          ↓
       Validation
          ↓
       SIEM Store
          ↓
      Enrichment
          ↓
       Detection
```

---

# 33. Threat Intelligence Platform

A TIP may centralize:

```text
Collection
Normalization
Enrichment
Correlation
Indicator Management
Sharing
Expiration
Scoring
```

The SIEM can consume intelligence from the TIP.

---

# 34. SIEM + TIP Architecture

```text
               Threat Sources
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Vendor         OSINT       Internal
       Feed          Feed       Intel
        │            │            │
        └────────────┼────────────┘
                     ▼
                    TIP
                     │
              Normalize/Enrich
                     │
                     ▼
                    SIEM
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
     Search       Detection     Alert
```

---

# 35. IOC Normalization

Different sources may represent the same indicator differently.

Example:

```text
HTTP://Example.COM/
example.com
example.com.
```

Normalization may produce:

```text
example.com
```

This improves matching.

---

# 36. IP Normalization

Consider:

```text
IPv4
IPv6
CIDR
IPv4-mapped IPv6
```

Normalization prevents inconsistent matching.

---

# 37. Domain Normalization

Consider:

```text
Case
Trailing dot
Internationalized domains
Subdomains
Punycode
```

Careful normalization is necessary to avoid false matches.

---

# 38. URL Normalization

URL matching may require handling:

```text
Scheme
Host
Port
Path
Query
Encoding
Case
Trailing slash
```

Over-normalization can also remove meaningful distinctions.

---

# 39. Hash Normalization

Hashes should be normalized by:

```text
Algorithm
Case
Formatting
```

Example:

```text
SHA256:
ABCDEF...

```

and:

```text
abcdef...
```

represent the same hexadecimal value.

---

# 40. IOC Matching

The SIEM can compare telemetry against threat intelligence.

Example:

```text
DNS Query
    ↓
domain = malicious.example
    ↓
Threat Intelligence Match
    ↓
High Confidence
    ↓
Alert
```

---

# 41. IP Matching

```text
Firewall Event
source.ip = X

        ↓

Threat Intelligence
X = malicious

        ↓

Detection

        ↓

Alert
```

---

# 42. Hash Matching

```text
Endpoint Event
file.hash.sha256 = X

        ↓

Threat Intelligence
X = known malware

        ↓

High-Confidence Detection
```

---

# 43. Domain Matching

```text
DNS
 ↓
Suspicious Domain
 ↓
Threat Intelligence Match
 ↓
Alert
```

Then investigate:

```text
Which host?
Which user?
How many queries?
What happened afterward?
```

---

# 44. IOC Enrichment

Not every IOC match should immediately create a high-priority alert.

Instead:

```text
Event
 ↓
IOC Match
 ↓
Enrichment
 ↓
Confidence
 ↓
Asset Context
 ↓
User Context
 ↓
Risk
 ↓
Alert
```

---

# 45. IOC Match Quality

A match should consider:

```text
Indicator Confidence
Indicator Age
Source Reliability
Direction
Context
Asset
User
Frequency
```

---

# 46. Context Matters

Suppose:

```text
Internal host
connected to known malicious IP
```

This is more concerning than:

```text
Security scanner
queried an IP
```

Context determines response.

---

# 47. Direction Matters

For an IP:

```text
Outbound connection
```

may indicate:

```text
C2
Malware
Exfiltration
```

While:

```text
Inbound connection
```

may indicate:

```text
Scanning
Attack
Hosting
```

Different context, different interpretation.

---

# 48. Threat Intelligence + Asset Criticality

Example:

```text
IOC Match
+
Critical Database Server
```

should generally receive greater attention than:

```text
IOC Match
+
Isolated Test Machine
```

---

# 49. Threat Intelligence + User Context

Example:

```text
Privileged Administrator
+
Malicious IP Connection
```

is potentially higher risk than:

```text
Low-privilege test account
+
Same indicator
```

---

# 50. IOC-Based Detection

Basic:

```text
IF
indicator matches threat feed

THEN
alert
```

Better:

```text
IF
indicator matches high-confidence feed

AND

source is internal endpoint

AND

connection is outbound

THEN

generate high-risk alert
```

---

# 51. Threat Intelligence Confidence

Example:

```text
Feed A:
Confidence = 95

Feed B:
Confidence = 60

Feed C:
Confidence = 20
```

A match from Feed A may deserve more immediate action.

---

# 52. Multiple-Source Confirmation

An indicator appearing in multiple independent sources may increase confidence.

Example:

```text
Source A → malicious
Source B → malicious
Source C → malicious
```

Potential:

```text
Higher Confidence
```

But source independence matters.

---

# 53. Threat Intelligence Correlation

Example:

```text
IOC Match
     +
Suspicious Process
     +
Unusual User
```

↓

```text
High-Confidence Alert
```

---

# 54. IOC and Behavioral Detection

IOC:

```text
Known malicious IP
```

Behavior:

```text
Host establishes repeated outbound connections
to unusual infrastructure.
```

Strong detection may combine both.

---

# 55. IOC Limitations

IOC-based detection can fail when attackers:

```text
Change Infrastructure
Use Fast-Flux
Use Compromised Hosts
Use Legitimate Cloud Services
Modify Malware
Use Domain Generation Algorithms
Use Short-Lived Domains
```

Therefore:

> IOC detection should complement behavioral and contextual detection.

---

# 56. Indicator of Attack vs Indicator of Compromise

### IOC

Evidence that may indicate compromise.

Examples:

```text
Known malware hash
Known C2 domain
Known malicious IP
```

### Indicator of Attack

Evidence of attacker behavior.

Examples:

```text
Credential dumping
Mass authentication failures
Suspicious privilege escalation
Lateral movement
```

Behavioral indicators can be useful even when no known IOC exists.

---

# 57. IOC vs IOA

```text
IOC
"What artifact is associated with compromise?"

IOA
"What behavior suggests an attack?"
```

Modern SOCs benefit from both.

---

# 58. Threat Intelligence Confidence vs Detection Confidence

These are different.

### TI Confidence

How confident the intelligence provider is about the indicator.

### Detection Confidence

How confident the SOC is that the observed activity represents malicious behavior.

Example:

```text
High-confidence malicious IP
```

but:

```text
Connection was made by a controlled security scanner.
```

Detection confidence may be lower.

---

# 59. Threat Intelligence Expiration

Old indicators can become:

```text
Stale
Reassigned
Benign
Irrelevant
```

Therefore:

```text
Feed Updates
+
Expiration
+
Review
```

are important.

---

# 60. Threat Intelligence False Positives

Possible causes:

```text
Shared Hosting
Cloud Infrastructure
CDNs
Dynamic IPs
Reassigned Domains
Legitimate Security Research
Security Scanners
Compromised-but-recovered Infrastructure
```

---

# 61. Avoid Blind Blocking

A dangerous workflow is:

```text
Threat Feed
 ↓
Match
 ↓
Automatically Block Everything
```

Better:

```text
Threat Feed
 ↓
Validate
 ↓
Confidence
 ↓
Context
 ↓
Risk
 ↓
Response
```

Automated blocking should be reserved for well-understood, high-confidence scenarios with appropriate safeguards.

---

# 62. Threat Intelligence Scoring

An organization may score an IOC based on:

```text
Source Reliability
Indicator Confidence
Age
Number of Sources
Observed Activity
Asset Criticality
```

Example:

```text
IOC Score =
40% Confidence
+
20% Freshness
+
20% Source Reliability
+
20% Corroboration
```

This is an illustrative model, not a universal formula.

---

# 63. Threat Intelligence Tags

Useful tags:

```text
malware
phishing
c2
ransomware
botnet
credential-theft
apt
scanner
spam
```

Tags enable filtering and detection.

---

# 64. Malware Family Context

Example:

```text
Indicator:
Domain X

Associated Malware:
Family Y

Technique:
C2

Confidence:
High
```

This helps analysts investigate beyond the raw indicator.

---

# 65. Threat Actor Context

Threat intelligence may associate indicators with:

```text
Threat Actor
Campaign
Malware Family
Target Sector
Region
```

Attribution should be treated carefully because it can be uncertain.

---

# 66. Attribution Confidence

Example:

```text
Observed Infrastructure
       ↓
Technical Evidence
       ↓
Possible Actor
```

Do not automatically conclude:

```text
IP = Threat Actor
```

Infrastructure can be:

```text
Compromised
Leased
Resold
Shared
Spoofed
```

---

# 67. STIX

**STIX** is a standardized language/model for representing cyber threat intelligence.

It can represent relationships among:

```text
Indicators
Malware
Threat Actors
Campaigns
Techniques
Infrastructure
Observables
```

---

# 68. STIX Objects

Conceptually:

```text
Indicator
    ↓
indicates
    ↓
Malware

Threat Actor
    ↓
uses
    ↓
Infrastructure
```

This allows richer intelligence relationships than simple IOC lists.

---

# 69. TAXII

**TAXII** is a protocol used to exchange cyber threat intelligence.

Conceptually:

```text
Threat Intelligence Provider
          ↓
         TAXII
          ↓
     Intelligence
     Consumer
```

---

# 70. STIX + TAXII

Simple mental model:

```text
STIX
=
How intelligence is represented

TAXII
=
How intelligence is exchanged
```

They are complementary concepts.

---

# 71. SIEM Threat Intelligence Pipeline

```text
             TI Sources
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
      OSINT   Vendor    Internal
        │        │        │
        └────────┼────────┘
                 ▼
             Normalize
                 │
                 ▼
             Validate
                 │
                 ▼
             Enrich
                 │
                 ▼
              Score
                 │
                 ▼
               Store
                 │
                 ▼
               Match
                 │
                 ▼
              Correlate
                 │
                 ▼
                Risk
                 │
                 ▼
               Alert
```

---

# 72. Feed Failure

What happens if the threat feed stops updating?

Potential effects:

```text
Stale Intelligence
Missed New Indicators
Incorrect Confidence
Detection Degradation
```

Therefore monitor:

```text
Last Successful Update
Indicator Count
Update Frequency
Feed Errors
API Availability
```

---

# 73. Feed Health Monitoring

Example:

```text
Feed:
ThreatFeed-A

Last Update:
10 minutes ago

Expected:
Every 15 minutes

Status:
Healthy
```

If:

```text
Last Update:
8 hours ago
```

↓

```text
Investigate Feed Health
```

---

# 74. Feed Quality Metrics

Track:

```text
Freshness
Match Rate
False Positive Rate
Unique Indicators
Expiration Rate
Update Failures
Detection Yield
```

---

# 75. Match Rate

If:

```text
1,000,000 events
```

and:

```text
10,000 IOC matches
```

match rate:

```text
1%
```

But a high match rate does not automatically mean:

```text
High Threat Level
```

It may indicate:

```text
Low-quality Feed
Common Infrastructure
Overly Broad Matching
```

---

# 76. Detection Yield

Measure:

```text
IOC Matches
      ↓
Alerts
      ↓
True Positives
```

This helps determine whether the feed is actually useful.

---

# 77. Threat Intelligence Tuning

If a feed generates too much noise:

```text
Analyze Indicators
       ↓
Identify Problem Categories
       ↓
Adjust Confidence
       ↓
Add Context
       ↓
Tune Matching
```

Do not simply discard the entire feed.

---

# 78. Threat Intelligence Use Cases

Common SIEM use cases:

```text
Malicious IP Detection
Malicious Domain Detection
Malware Hash Detection
Phishing Detection
C2 Detection
Known Scanner Detection
Threat Actor Infrastructure
Ransomware Intelligence
Vulnerability Intelligence
Campaign Tracking
```

---

# 79. Use Case – Malicious IP

```text
Firewall Event
     ↓
Destination IP
     ↓
Threat Feed Match
     ↓
Malicious
     ↓
Risk Score
     ↓
Alert
```

---

# 80. Use Case – Malicious Domain

```text
DNS Event
     ↓
Domain
     ↓
TI Match
     ↓
Malware-associated
     ↓
Alert
```

---

# 81. Use Case – Malware Hash

```text
EDR Event
     ↓
SHA256
     ↓
TI Match
     ↓
Known Malware
     ↓
High-Confidence Alert
```

---

# 82. Use Case – Phishing

Combine:

```text
Email Sender
+
Domain
+
URL
+
Attachment Hash
```

Then enrich against:

```text
Threat Intelligence
```

---

# 83. Use Case – C2

Combine:

```text
Outbound Connection
+
Known C2 IP
+
Suspicious Process
+
Repeated Beaconing
```

↓

```text
High-Confidence C2 Detection
```

---

# 84. Threat Intelligence and Detection Engineering

Threat intelligence can directly support detection development.

Workflow:

```text
New Threat Intelligence
        ↓
Understand Threat
        ↓
Identify Behavior
        ↓
Identify Telemetry
        ↓
Create Detection
        ↓
Test
        ↓
Deploy
```

---

# 85. Threat Intelligence and Threat Hunting

Example:

```text
Threat Report
      ↓
New C2 Domain Pattern
      ↓
Search Historical DNS
      ↓
Search Proxy
      ↓
Search Endpoint
      ↓
Identify Matches
      ↓
Investigate
```

This turns intelligence into proactive hunting.

---

# 86. Historical Retro-Hunting

When a new IOC becomes known:

```text
New IOC
   ↓
Search Historical Data
   ↓
Last 7 days
   ↓
Last 30 days
   ↓
Last 90 days
```

This may reveal earlier compromise.

Retention determines how far back you can search.

---

# 87. IOC Retro-Hunting Example

New domain:

```text
malicious.example
```

Search:

```text
DNS
Proxy
Firewall
Endpoint
Email
```

Then identify:

```text
First Seen
Last Seen
Hosts
Users
Connections
```

---

# 88. First Seen / Last Seen

Useful intelligence fields:

```text
First Seen
Last Seen
```

Example:

```text
First Seen:
2026-07-01

Last Seen:
2026-08-10
```

This can help establish timelines.

---

# 89. Threat Intelligence and Incident Response

During an incident:

```text
Known IOC
      ↓
Search SIEM
      ↓
Find Related Events
      ↓
Identify Scope
      ↓
Identify Hosts
      ↓
Identify Users
      ↓
Contain
```

---

# 90. IOC Blocking

Possible automated response:

```text
High-confidence malicious IP
        ↓
Firewall Block
```

or:

```text
Malicious Domain
        ↓
DNS Block
```

or:

```text
Malware Hash
        ↓
Endpoint Quarantine
```

Automation should include safeguards and authorization.

---

# 91. Threat Intelligence + SOAR

Example:

```text
SIEM
 ↓
High-Confidence IOC Match
 ↓
SOAR
 ↓
Threat Intelligence Validation
 ↓
Firewall
 ↓
Block IP
 ↓
EDR
 ↓
Isolate Host
```

This connects intelligence to automated response.

---

# 92. Practical Lab

Build a simple IOC enrichment workflow.

Input:

```text
Firewall Logs
```

Extract:

```text
destination.ip
```

Match against:

```text
Threat Intelligence IP List
```

Then add:

```text
Threat
Confidence
Source
First Seen
Last Seen
```

Finally:

```text
Generate Alert
```

---

# 93. Practical IOC Exercise

Given:

```text
Host:
WORKSTATION01

User:
alice

Destination:
203.0.113.50

Threat Intelligence:
Malicious
Confidence:
High
```

Investigate:

```text
What process made the connection?

When?

How many times?

What DNS query occurred?

Did other hosts connect?

Was data transferred?

What happened before and after?
```

---

# 94. Practical Threat Intelligence Exercise

Suppose a threat report identifies:

```text
Domain:
evil-example.com

Hash:
SHA256-X

IP:
203.0.113.10
```

Search:

```text
DNS
Endpoint
Firewall
Proxy
Email
```

Then build:

```text
IOC Timeline
```

---

# 95. Practical Detection Exercise

Create:

```text
IF

internal host connects
to high-confidence malicious IP

AND

endpoint process is unusual

THEN

high-risk alert
```

Add:

```text
Asset Criticality
User
Process
Threat Family
MITRE Technique
```

---

# 96. Interview Questions

### What is threat intelligence?

> Information about threats that has been collected, analyzed, contextualized, and made useful for security decisions.

### What is an IOC?

> An observable artifact that may indicate malicious activity or compromise, such as an IP, domain, URL, or file hash.

### What are common IOC types?

> IP addresses, domains, URLs, file hashes, email addresses, certificates, filenames, and other observable artifacts.

### What is the difference between threat data and threat intelligence?

> Threat data is raw information; threat intelligence adds analysis, context, confidence, relationships, and actionable meaning.

### What is the difference between IOC and IOA?

> An IOC is an artifact associated with compromise, while an IOA focuses on behavior indicating an attack.

### Why is IOC age important?

> Indicators can become stale, reassigned, or benign, so old indicators may become less reliable.

### What is IOC enrichment?

> Adding contextual information such as reputation, confidence, threat family, source, first seen, and last seen to an indicator or event.

### What is STIX?

> A standardized framework for representing and sharing structured cyber threat intelligence.

### What is TAXII?

> A protocol used to exchange cyber threat intelligence, commonly with STIX-formatted information.

### Why shouldn't every IOC match automatically create a critical alert?

> Because indicators vary in confidence, freshness, context, and reliability, and many can generate false positives.

### How would you integrate threat intelligence with a SIEM?

> Ingest feeds through APIs or supported protocols, normalize and validate indicators, store them in a searchable intelligence repository, enrich telemetry, match indicators against events, correlate results with context, and generate prioritized alerts.

### What is IOC expiration?

> Removing or deactivating indicators after they become stale or no longer meet intelligence criteria.

### What is retro-hunting?

> Searching historical security telemetry for newly discovered indicators or behaviors to determine whether they were previously present.

### How do you evaluate a threat intelligence feed?

> Consider accuracy, freshness, coverage, false positives, context, update reliability, source quality, and detection yield.

---

# 97. Quick Revision

```text
THREAT INTELLIGENCE
→ Context about threats

THREAT DATA
→ Raw observations

IOC
→ Observable artifact associated with compromise

IOA
→ Behavioral indication of attack

REPUTATION
→ Assessment of indicator trustworthiness

CONFIDENCE
→ How strongly the indicator is believed to be malicious

ENRICHMENT
→ Add contextual information

NORMALIZATION
→ Standardize indicators

MATCHING
→ Compare telemetry against intelligence

RETRO-HUNTING
→ Search historical telemetry

STIX
→ Threat intelligence representation

TAXII
→ Threat intelligence exchange

TIP
→ Threat Intelligence Platform

IOC LIFECYCLE
→ Discover → Validate → Enrich → Distribute → Detect → Review → Expire
```

---

# 98. Golden Rules

```text
1. Threat intelligence is more valuable when it has context.

2. An IOC is an indicator, not automatic proof of compromise.

3. Not all intelligence sources are equally reliable.

4. Always consider indicator confidence.

5. Always consider indicator age.

6. Normalize indicators before matching.

7. Context matters more than a raw IOC match.

8. Combine IOC detection with behavioral detection.

9. Do not blindly block every indicator.

10. Monitor feed health.

11. Measure false positives.

12. Track indicator freshness.

13. Expire stale indicators.

14. Use historical hunting when new intelligence arrives.

15. Protect threat intelligence systems and credentials.

16. Map intelligence to relevant threats and techniques.

17. Explain why an IOC generated an alert.

18. Consider asset and user criticality.

19. Use multiple independent sources when appropriate.

20. Threat intelligence should improve decisions, not simply increase alert volume.
```

---

# 99. Final Mental Model

Think about threat intelligence integration as:

```text
THREAT SOURCES
      ↓
COLLECTION
      ↓
NORMALIZATION
      ↓
VALIDATION
      ↓
ENRICHMENT
      ↓
CONFIDENCE
      ↓
STORAGE
      ↓
SIEM MATCHING
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

And for a SOC analyst:

```text
IOC MATCH
    ↓
WHO?
    ↓
WHAT HOST?
    ↓
WHAT USER?
    ↓
WHAT PROCESS?
    ↓
WHAT TIME?
    ↓
WHAT ELSE HAPPENED?
    ↓
HOW MANY HOSTS?
    ↓
HOW CONFIDENT?
    ↓
WHAT IS THE RISK?
    ↓
WHAT ACTION?
```

---

# 100. Chapter Summary

Threat intelligence extends SIEM visibility beyond the organization's own telemetry.

The key transformation is:

```text
RAW EVENT
    ↓
OBSERVABLE
    ↓
THREAT INTELLIGENCE
    ↓
CONTEXT
    ↓
CORRELATION
    ↓
RISK
    ↓
ACTION
```

A mature SOC does not simply ask:

```text
"Does this IP appear in a threat feed?"
```

It asks:

```text
Is the indicator trustworthy?

How recent is it?

What is it associated with?

What host contacted it?

Which user was involved?

Which process made the connection?

Was the activity inbound or outbound?

Is the asset critical?

Are there related indicators?

Has this occurred before?

What happened immediately before and after?

What is the appropriate response?
```

The most important principle is:

> **Threat intelligence should provide context and confidence that improve detection, investigation, and response—not simply create more alerts.**

The next chapter moves from individual indicators and intelligence into adversary behavior modeling:

```text
Chapter 09 – MITRE ATT&CK & Threat-Based Detection
```

There we will cover **MITRE ATT&CK tactics, techniques, sub-techniques, procedures, detection mapping, coverage matrices, adversary behavior, attack chains, threat-informed detection engineering, ATT&CK-based hunting, and practical SOC use cases.**