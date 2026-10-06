# Chapter 05 – IOC, Signature & Indicator-Based Detection

> Indicator-based detection identifies potentially malicious activity by matching observed telemetry against known indicators or recognizable signatures. It is one of the fastest ways to detect known threats, but it must be combined with behavioral and contextual detection to remain effective against changing adversaries.

---

# 1. What Is an IOC?

**IOC** stands for **Indicator of Compromise**.

An IOC is an observable artifact that may indicate malicious activity or compromise.

Common IOCs include:

```text
IP Addresses
Domains
URLs
File Hashes
Email Addresses
File Names
File Paths
Certificates
Registry Values
User Agents
Mutexes
```

Conceptually:

```text
Observed Activity
       ↓
Indicator Extraction
       ↓
Threat Intelligence
       ↓
IOC Match
       ↓
Detection
```

---

# 2. IOC vs Indicator

An **indicator** is a broader term for an observable value associated with activity.

An IOC generally represents evidence associated with compromise.

Examples:

```text
Indicator:
Suspicious Domain

IOC:
Domain confirmed to be associated
with a known malicious campaign
```

The exact terminology can vary between security teams and platforms.

---

# 3. Why IOC Detection Matters

IOC detection is particularly useful for:

```text
Known Malware
Known C2 Infrastructure
Known Phishing Infrastructure
Known Malicious Files
Known Attack Campaigns
Known Threat Actors
```

Advantages:

```text
Fast
Simple
Explainable
Easy to Automate
Easy to Share
```

---

# 4. Common IOC Types

Major categories:

```text
Network IOCs
Host IOCs
File IOCs
Email IOCs
Identity IOCs
Cloud IOCs
Application IOCs
```

---

# 5. IP Address IOC

Example:

```text
203.0.113.50
```

Potentially associated with:

```text
C2
Scanning
Malware Hosting
Phishing
Botnet Infrastructure
```

Detection:

```text
IF destination.ip = known_bad_ip
THEN alert
```

---

# 6. Domain IOC

Example:

```text
malicious-example.example
```

Detection:

```text
IF dns.question.name = known_bad_domain
THEN alert
```

Domains are commonly used for:

```text
Phishing
C2
Malware Delivery
Redirects
Tracking Infrastructure
```

---

# 7. URL IOC

A URL provides more detail:

```text
https://example.invalid/payload
```

Compared with a domain:

```text
example.invalid
```

a URL may include:

```text
Protocol
Domain
Port
Path
Query
Fragment
```

---

# 8. File Hash IOC

Common hashes:

```text
MD5
SHA-1
SHA-256
```

Example:

```text
File
 ↓
SHA-256
 ↓
Threat Intelligence
 ↓
Known Malicious?
```

Hash-based detection is highly precise when the hash is trustworthy.

---

# 9. Why Hashes Are Limited

A tiny file modification can produce a completely different hash.

```text
Malware A
→ Hash A

Modified Malware A
→ Hash B
```

Therefore:

```text
Hash Detection
≠
Complete Malware Detection
```

Behavioral detection can detect related variants.

---

# 10. Email IOC

Examples:

```text
Sender Address
Reply-To Address
Attachment Hash
Malicious URL
Sender Domain
Message ID
```

Potential phishing detection:

```text
Email
+
Known Malicious Domain
+
Malicious Attachment
```

---

# 11. File Name IOC

Example:

```text
suspicious.exe
```

However, filenames are weak indicators because legitimate files can have the same name.

Better:

```text
Filename
+
Path
+
Hash
+
Signer
+
Parent Process
```

---

# 12. File Path IOC

Example:

```text
/path/to/suspicious/file
```

Paths can be useful when associated with known malicious activity.

But hardcoded paths can become unreliable when attackers change location.

---

# 13. Registry IOC

On Windows, suspicious registry artifacts may be useful indicators.

Examples:

```text
Registry Key
Registry Value
Persistence Location
Configuration
```

Detection should consider:

```text
Key
Value
Process
User
Time
Context
```

---

# 14. Certificate IOC

TLS certificates can sometimes be associated with malicious infrastructure.

Useful fields:

```text
Certificate Hash
Subject
Issuer
Serial Number
Validity
Public Key
```

Certificate-based detection can provide additional infrastructure context.

---

# 15. User-Agent IOC

A suspicious or known malicious user agent may be useful.

Example:

```text
User-Agent:
KnownMalwareClient/1.0
```

However, user agents are easy to spoof.

Therefore:

```text
User-Agent
+
Destination
+
Process
+
Network Behavior
```

is stronger.

---

# 16. Network IOC Categories

Network indicators include:

```text
IP
Domain
URL
Port
Protocol
Certificate
ASN
User-Agent
JA3/JA4-like fingerprints
```

Fingerprints should be treated carefully because legitimate applications can share infrastructure or characteristics.

---

# 17. Host IOC Categories

Host indicators include:

```text
File Hash
Filename
File Path
Registry Key
Process Name
Service
Scheduled Task
Mutex
Named Pipe
```

Again, context is critical.

---

# 18. IOC Confidence

Not every IOC is equally trustworthy.

Possible confidence levels:

```text
Low
Medium
High
Confirmed
```

Example:

```text
Threat Feed:
Low Confidence

Internal Incident Evidence:
High Confidence

Confirmed Malware:
Very High Confidence
```

---

# 19. IOC Confidence Sources

Confidence can depend on:

```text
Source Reputation
Evidence Quality
Age
Number of Confirmations
Internal Validation
Threat Intelligence Context
False Positive History
```

---

# 20. IOC Freshness

IOCs have a lifecycle.

```text
New IOC
   ↓
Active
   ↓
Aged
   ↓
Possibly Stale
   ↓
Retired
```

An old IOC should not automatically remain a high-confidence blocking or alerting indicator.

---

# 21. IOC Aging

Example:

```text
Day 1:
Known Malicious IP

Day 30:
Still Relevant?

Day 180:
Still Malicious?

Day 365:
Should It Still Be Active?
```

Threat intelligence must be continuously evaluated.

---

# 22. IOC Expiration

An IOC may have:

```text
Created Time
First Seen
Last Seen
Expiration Time
Confidence
Source
Status
```

Example:

```text
IOC:
malicious.example

First Seen:
2026-07-01

Last Seen:
2026-08-10

Status:
Active
```

---

# 23. IOC Lifecycle

A professional IOC lifecycle:

```text
Discovery
   ↓
Validation
   ↓
Enrichment
   ↓
Scoring
   ↓
Deployment
   ↓
Monitoring
   ↓
Review
   ↓
Expiration / Retirement
```

---

# 24. IOC Discovery

IOCs may originate from:

```text
Threat Intelligence
Incident Response
Malware Analysis
Threat Hunting
Security Vendors
CERTs
Internal Research
Sandboxing
EDR
Network Detection
```

---

# 25. IOC Validation

Before deployment, ask:

```text
Is the IOC accurate?

Is the source trustworthy?

Is it still active?

Could it be shared infrastructure?

Could it be legitimate?

What evidence supports it?
```

---

# 26. IOC Enrichment

Add:

```text
Threat Actor
Campaign
Malware Family
First Seen
Last Seen
Confidence
Source
Geolocation
ASN
Related Domains
Related Hashes
```

This makes the indicator more useful.

---

# 27. IOC Reputation

An indicator may have a reputation:

```text
Malicious
Suspicious
Unknown
Benign
```

Reputation can change over time.

---

# 28. IOC Context

Example:

```text
IP = 203.0.113.10
```

alone is weak.

Add:

```text
IP
+
Known C2
+
Malware Family
+
Recent Activity
+
Internal Connection
```

Now confidence increases.

---

# 29. Indicator Matching

Common matching methods:

```text
Exact Match
Prefix Match
Suffix Match
Substring
Wildcard
Regex
Set Membership
Hash Match
Normalized Match
```

---

# 30. Exact Matching

Example:

```text
source.ip = 203.0.113.10
```

Advantages:

```text
Fast
Precise
Predictable
```

---

# 31. Set-Based Matching

Maintain a set:

```text
Known_Bad_IPs
```

Then:

```text
IF source.ip IN Known_Bad_IPs
THEN alert
```

This is commonly more manageable than embedding hundreds of indicators directly into detection logic.

---

# 32. Lookup Tables

A lookup structure may contain:

```text
Indicator
Type
Confidence
Source
First Seen
Last Seen
Expiration
Threat Actor
Campaign
```

Example:

```text
| Indicator | Type | Confidence | Status |
|---|---|---|---|
| 203.0.113.10 | IP | High | Active |
| example.invalid | Domain | Medium | Active |
```

---

# 33. Indicator Normalization

Before matching, normalize data.

Examples:

```text
Domain:
EXAMPLE.COM
example.com
```

may need consistent normalization.

Similarly:

```text
IP
URL
Hash
Email
```

may require format normalization.

---

# 34. Domain Normalization

Consider:

```text
Case
Trailing Dot
Punycode
Subdomains
Internationalized Domains
```

Example:

```text
EXAMPLE.COM.
```

and:

```text
example.com
```

may represent the same domain depending on processing.

---

# 35. URL Normalization

URLs may vary by:

```text
Scheme
Case
Encoding
Port
Path
Query
Trailing Slash
```

Normalization helps avoid missed matches.

---

# 36. IP Normalization

Consider:

```text
IPv4
IPv6
Mapped Addresses
Representation Differences
```

Ensure the matching system handles the formats correctly.

---

# 37. Hash Normalization

Hashes should generally be normalized consistently:

```text
Lowercase
Correct Length
Correct Algorithm
No Whitespace
```

Example:

```text
SHA-256
64 hexadecimal characters
```

---

# 38. Exact vs Broad IOC Matching

### Exact

```text
domain = example.invalid
```

### Broad

```text
domain contains "example"
```

Broad matching can produce:

```text
False Positives
```

Use the narrowest reliable matching strategy.

---

# 39. Indicator Allowlisting

Some indicators may be known benign.

Example:

```text
Known Corporate Proxy
Known Vulnerability Scanner
Known Security Vendor
Known CDN
```

Allowlisting should be:

```text
Specific
Documented
Reviewed
```

---

# 40. Why Broad Allowlisting Is Dangerous

Bad:

```text
Allowlist entire ASN
```

or:

```text
Ignore all traffic from large network
```

Potential result:

```text
Large Detection Blind Spot
```

---

# 41. Shared Infrastructure Problem

An IP may host:

```text
Multiple Websites
Multiple Customers
Multiple Applications
```

Therefore:

```text
IP = Malicious
```

does not always mean:

```text
Every connection to IP = Malicious
```

Context matters.

---

# 42. CDN Problem

CDNs can serve:

```text
Benign Content
Malicious Content
```

The same infrastructure may host many unrelated domains.

Domain-level context can therefore be more useful than an IP-only match in some situations.

---

# 43. Cloud Infrastructure Problem

Cloud providers use dynamic infrastructure.

An IP may:

```text
Change Ownership
Change Customer
Change Purpose
```

Therefore cloud IOCs should be monitored for freshness.

---

# 44. False Positives in IOC Detection

Causes include:

```text
Shared Infrastructure
Stale Indicators
Compromised Legitimate Services
Incorrect Intelligence
Broad Matching
Legitimate Security Tools
CDNs
VPNs
Proxies
```

---

# 45. False Negative in IOC Detection

An IOC detection can miss activity because:

```text
Indicator Changed
Domain Changed
IP Changed
Hash Changed
Traffic Encrypted
Telemetry Missing
Indicator Not Yet Known
```

---

# 46. IOC Detection vs Behavioral Detection

### IOC

```text
Known Bad
```

### Behavioral

```text
Suspicious Activity
```

Example:

```text
IOC:
Known C2 Domain

Behavior:
Periodic outbound connections
to a rare external destination
```

Behavior can remain useful when infrastructure changes.

---

# 47. Signature Detection

A signature identifies a known recognizable pattern.

Examples:

```text
Malware Byte Pattern
Command Pattern
Network Payload Pattern
File Structure
Known Attack Pattern
```

---

# 48. Signature Matching

Conceptually:

```text
Observed Data
      ↓
Signature Database
      ↓
Pattern Match
      ↓
Alert
```

---

# 49. Signature Advantages

```text
Fast
Deterministic
Explainable
Easy to Validate
```

---

# 50. Signature Limitations

Signatures can fail against:

```text
Obfuscation
Encryption
Packing
Polymorphism
Modified Malware
New Variants
```

---

# 51. Polymorphic Malware

The underlying malicious functionality may remain similar while the representation changes.

Example:

```text
Variant A
→ Hash A

Variant B
→ Hash B

Variant C
→ Hash C
```

Hash-only detection may miss B and C.

---

# 52. Obfuscation

Attackers may modify:

```text
Command Syntax
Variable Names
Encoding
Whitespace
String Construction
```

to evade simple signatures.

Behavioral detection can help identify the underlying activity.

---

# 53. Indicator Chaining

Combine multiple indicators.

Example:

```text
Malicious Domain
+
Suspicious Process
+
Known Malware Hash
```

↓

```text
High Confidence
```

---

# 54. IOC Correlation

Example:

```text
Host A
 ↓
Connects to Known C2
 ↓
Downloads Known Malware Hash
 ↓
Creates Persistence Artifact
```

This is much stronger than a single IOC match.

---

# 55. IOC Severity

Not every IOC match should produce the same severity.

Example:

```text
Known Malicious Hash
on Critical Server
```

may be:

```text
Critical
```

while:

```text
Suspicious Domain
from Isolated Test System
```

may be:

```text
Low / Medium
```

Context determines priority.

---

# 56. IOC Risk Scoring

Example:

```text
Known C2 IP       +40
Critical Host     +30
Privileged User   +30
Malware Hash      +50
```

Total:

```text
150
```

Potential:

```text
Critical Investigation
```

---

# 57. Threat Intelligence Integration

Typical pipeline:

```text
Threat Feed
    ↓
Collection
    ↓
Validation
    ↓
Normalization
    ↓
Enrichment
    ↓
Scoring
    ↓
Storage
    ↓
Detection
```

---

# 58. Threat Intelligence Feed Types

Possible sources:

```text
Commercial Feeds
Open-Source Intelligence
Government Sources
ISAC/ISAO
Internal Intelligence
Vendor Intelligence
Incident Response
Research Teams
```

---

# 59. Feed Quality

Evaluate:

```text
Accuracy
Freshness
Coverage
Relevance
False Positive Rate
Context
Update Frequency
Attribution Quality
```

---

# 60. Feed Noise

Adding every available feed can create:

```text
Millions of Indicators
        ↓
Many Matches
        ↓
Alert Noise
```

More intelligence does not automatically mean better intelligence.

---

# 61. Intelligence Prioritization

Prioritize indicators based on:

```text
Confidence
Relevance
Freshness
Threat Actor
Campaign
Internal Exposure
Asset Exposure
```

---

# 62. Internal vs External Intelligence

### External

```text
Vendor
Community
Government
Research
```

### Internal

```text
Incident
Hunting
EDR
SOC
Malware Analysis
```

Internal intelligence is often highly relevant because it reflects the organization's own environment.

---

# 63. IOC Deployment Locations

IOCs can be used in:

```text
SIEM
EDR
Firewall
Proxy
DNS Security
Email Security
WAF
NDR
SOAR
Cloud Security
```

---

# 64. Detection vs Blocking

IOC matching can support:

```text
Detection
Alerting
Blocking
Quarantine
Investigation
```

Do not automatically block every IOC.

Blocking should consider:

```text
Confidence
Impact
Business Context
Potential False Positive
```

---

# 65. Detection-Only IOC

Useful when:

```text
Confidence = Medium
```

Action:

```text
Alert
+
Investigate
```

---

# 66. High-Confidence Blocking IOC

Potentially:

```text
Confirmed Malware Hash
```

Action:

```text
Block
+
Quarantine
+
Alert
```

depending on organizational policy.

---

# 67. IOC Expiration Strategy

Example:

```text
Indicator Added
      ↓
30-Day Review
      ↓
Still Active?
    /      \
  YES       NO
  ↓          ↓
Extend     Retire
```

Exact expiration periods should depend on threat type and intelligence quality.

---

# 68. IOC Metadata

Recommended fields:

```text
Indicator
Type
Source
Confidence
Severity
First Seen
Last Seen
Expiration
Threat Actor
Campaign
Malware Family
Description
Reference
Status
Owner
```

---

# 69. Indicator Status

Useful states:

```text
New
Active
Suspicious
Expired
Revoked
Benign
Retired
```

---

# 70. IOC Versioning

When intelligence changes:

```text
IOC v1
 ↓
Updated Confidence
 ↓
IOC v2
```

Versioning supports auditability.

---

# 71. IOC Provenance

Provenance answers:

```text
Where did this IOC come from?
Who added it?
When was it added?
What evidence supports it?
```

This is essential for trustworthy threat intelligence.

---

# 72. IOC Chain of Evidence

Example:

```text
Malware Sample
 ↓
Hash
 ↓
Sandbox
 ↓
C2 Domain
 ↓
IP
 ↓
Threat Intelligence
 ↓
Detection
```

The stronger the evidence chain, the stronger the confidence.

---

# 73. Indicator Relationship Graph

Indicators can be related:

```text
Threat Actor
     │
     ├── Campaign
     │      │
     │      ├── Domain
     │      ├── IP
     │      └── Hash
     │
     └── Malware Family
```

This helps analysts understand campaigns rather than isolated indicators.

---

# 74. Indicator Clustering

Group indicators by:

```text
Campaign
Threat Actor
Malware Family
Infrastructure
Time
Behavior
```

Example:

```text
Campaign X
 ├── 5 Domains
 ├── 3 IPs
 ├── 7 Hashes
 └── 2 Malware Families
```

---

# 75. Indicator Deduplication

Different feeds may provide the same indicator.

Example:

```text
Feed A → example.invalid
Feed B → example.invalid
Feed C → example.invalid
```

Deduplicate while preserving:

```text
Sources
Confidence
First Seen
Last Seen
```

---

# 76. Indicator Conflict

One feed says:

```text
Malicious
```

Another says:

```text
Benign
```

Do not blindly choose one.

Investigate:

```text
Source Quality
Freshness
Context
Evidence
Internal Observations
```

---

# 77. IOC Intelligence Scoring

Conceptual model:

```text
Score =
Source Reliability
+
Freshness
+
Evidence
+
Internal Confirmation
-
False Positive History
```

The exact scoring model should be designed for the organization's needs.

---

# 78. IOC Matching Pipeline

```text
Raw Event
   ↓
Normalize
   ↓
Extract Indicator
   ↓
Lookup
   ↓
Match?
 /   \
NO    YES
 |      |
Continue Enrich
        ↓
     Score
        ↓
      Alert
```

---

# 79. IOC Detection Example – DNS

Input:

```text
DNS Query:
malicious.example
```

Pipeline:

```text
Normalize Domain
      ↓
Threat Feed Lookup
      ↓
Known Malicious?
      ↓
YES
      ↓
Enrich
      ↓
Alert
```

Add:

```text
User
Host
Process
Destination IP
Threat Actor
```

for better investigation.

---

# 80. IOC Detection Example – File

```text
File Created
      ↓
Calculate SHA-256
      ↓
Threat Intelligence Lookup
      ↓
Known Malware?
      ↓
YES
      ↓
Endpoint Alert
```

---

# 81. IOC Detection Example – Network

```text
Outbound Connection
      ↓
Destination IP
      ↓
IOC Lookup
      ↓
Known C2?
      ↓
YES
      ↓
Correlate Process + User + Host
      ↓
Risk
```

---

# 82. IOC Detection Example – Email

```text
Incoming Email
      ↓
Extract URLs
      ↓
Normalize
      ↓
IOC Lookup
      ↓
Known Phishing?
      ↓
Alert
```

---

# 83. IOC + Behavior Example

```text
Known C2 Domain
       +
Rare Process
       +
Periodic Connections
       ↓
High Confidence C2 Detection
```

---

# 84. IOC + Identity Example

```text
Known Malicious IP
       +
Privileged Account
       +
Successful Login
       +
New Device
       ↓
High-Risk Account Compromise
```

---

# 85. IOC + Endpoint Example

```text
Known Malware Hash
       +
Execution
       +
Persistence
       ↓
Potential Host Compromise
```

---

# 86. IOC + Cloud Example

```text
Known Malicious IP
       +
Cloud Login
       +
New Access Key
       +
Privilege Change
       ↓
Potential Cloud Account Takeover
```

---

# 87. Detection Resilience

A strong IOC program should not depend exclusively on indicators.

Use:

```text
IOC
+
Behavior
+
Context
+
Correlation
```

This provides resilience when:

```text
IOC Changes
```

---

# 88. IOC Rotation

Attackers may rotate:

```text
IP Addresses
Domains
Certificates
URLs
Hashes
```

Detection strategy:

```text
Indicator
+
Behavioral Detection
```

---

# 89. Threat Infrastructure Changes

Infrastructure can change quickly:

```text
Domain A
 ↓
Domain B
 ↓
Domain C
```

Static IOC lists may become stale.

Therefore:

```text
Threat Intelligence
+
Continuous Updating
```

is required.

---

# 90. Common IOC Detection Mistakes

## Mistake 1

Treating every IOC as equally trustworthy.

---

## Mistake 2

Never expiring indicators.

---

## Mistake 3

Using broad IP allowlists.

---

## Mistake 4

Relying only on hashes.

---

## Mistake 5

Ignoring shared infrastructure.

---

## Mistake 6

Alerting on every low-confidence IOC.

---

## Mistake 7

Not recording IOC provenance.

---

## Mistake 8

Failing to normalize indicators.

---

## Mistake 9

Not deduplicating feeds.

---

## Mistake 10

Using threat feeds without measuring quality.

---

# 91. IOC Detection Checklist

```text
[ ] Indicator type identified
[ ] Source documented
[ ] Confidence assigned
[ ] Freshness evaluated
[ ] Indicator normalized
[ ] Duplicate indicators removed
[ ] Context added
[ ] False positives evaluated
[ ] Expiration defined
[ ] Matching strategy selected
[ ] Detection location selected
[ ] Severity assigned
[ ] Owner assigned
[ ] Provenance recorded
[ ] Review process established
```

---

# 92. Interview Questions

### What is an IOC?

> An Indicator of Compromise is an observable artifact associated with potentially malicious activity or a known compromise.

### Give examples of IOCs.

> IP addresses, domains, URLs, file hashes, malicious email addresses, filenames, certificates, registry artifacts, and other observable indicators.

### Why are hashes useful?

> They can precisely identify known files when the hash is reliable.

### Why are hashes insufficient?

> Any file modification produces a different hash, so modified variants can evade hash-based detection.

### What is IOC freshness?

> The relevance of an indicator based on how recently it has been observed or validated as malicious.

### Why should IOCs expire?

> Threat infrastructure changes, indicators can become stale, and permanent indicators increase false positives.

### What is IOC enrichment?

> Adding context such as threat actor, campaign, malware family, confidence, timestamps, source, and related indicators.

### Why is IOC normalization important?

> It ensures equivalent indicators are represented consistently and can be matched reliably.

### What is IOC provenance?

> Information describing where an indicator originated and what evidence supports it.

### Why shouldn't every IOC automatically block traffic?

> Some indicators may be stale, incorrect, shared, or low-confidence, so blocking can cause operational impact.

### How do you improve IOC detection?

> Combine IOCs with behavioral detection, contextual enrichment, correlation, confidence scoring, and regular intelligence updates.

---

# 93. Quick Revision

```text
IOC
→ Indicator associated with compromise

IP IOC
→ Malicious/suspicious network address

Domain IOC
→ Known suspicious domain

URL IOC
→ Known suspicious URL

Hash IOC
→ Known malicious file fingerprint

Signature
→ Known recognizable malicious pattern

IOC Confidence
→ Trustworthiness of the indicator

IOC Freshness
→ Current relevance of the indicator

IOC Provenance
→ Source and evidence behind the indicator

IOC Enrichment
→ Additional contextual information

IOC Normalization
→ Standardizing indicators before matching

IOC Expiration
→ Removing stale indicators

IOC Correlation
→ Combining indicators with other signals

Hybrid Detection
→ IOC + Behavior + Context
```

---

# 94. Golden Rules

```text
1. Not every indicator is equally trustworthy.

2. Validate indicators before production use.

3. Track indicator provenance.

4. Assign confidence to important indicators.

5. Track first-seen and last-seen information.

6. Expire stale indicators.

7. Normalize indicators before matching.

8. Deduplicate feeds.

9. Preserve source information during deduplication.

10. Avoid broad allowlists.

11. Be careful with shared infrastructure.

12. Do not rely exclusively on IP addresses.

13. Do not rely exclusively on file hashes.

14. Combine IOCs with behavioral context.

15. Use risk scoring when many signals are involved.

16. Measure feed quality.

17. Review false positives.

18. Keep detection logic separate from indicator storage when practical.

19. Treat threat intelligence as dynamic information.

20. Continuously update active indicators.

21. Use detection for uncertain indicators before blocking.

22. Use high-confidence indicators carefully for prevention.

23. Record why an IOC exists.

24. Review indicators periodically.

25. IOC detection is excellent for known threats—but behavior is necessary to detect what the attacker has not yet revealed.
```

---

# 95. Final Mental Model

Think of IOC detection as:

```text
KNOWN THREAT
     ↓
INDICATOR
     ↓
VALIDATE
     ↓
NORMALIZE
     ↓
ENRICH
     ↓
SCORE
     ↓
MATCH TELEMETRY
     ↓
CORRELATE
     ↓
ALERT / BLOCK / INVESTIGATE
```

But remember:

```text
IOC
 ↓
Known Threat

Behavior
 ↓
Potential Unknown Threat
```

The strongest detection strategy is therefore:

```text
Known Indicators
        +
Behavioral Detection
        +
Context
        +
Correlation
        +
Risk
        ↓
Resilient Detection
```

---

# 96. Chapter Summary

This chapter covered:

```text
IOC Fundamentals
Indicator Types
IP Detection
Domain Detection
URL Detection
Hash Detection
Email Indicators
Host Indicators
Network Indicators
Signature Detection
IOC Confidence
IOC Freshness
IOC Lifecycle
IOC Validation
IOC Enrichment
IOC Normalization
IOC Matching
IOC Deduplication
IOC Provenance
Threat Intelligence Integration
False Positives
Shared Infrastructure
IOC Correlation
IOC + Behavioral Detection
IOC Risk Scoring
```

The key principle is:

> **IOC detection provides fast and precise visibility into known threats, but indicators are temporary and attackers can change them. A mature detection program therefore uses IOCs as one layer within a broader behavioral, contextual, and threat-informed detection strategy.**

The next chapter moves into **Behavioral Detection & TTP-Based Detection**, where the focus shifts from *“Is this known malicious?”* to *“Does this activity resemble how an attacker operates?”*